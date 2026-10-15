#!/usr/bin/env python3
"""Staged cyclic LKTS search, with frozen rainbow infinity matchings.

Run with ortools==9.15.6755 (see sources/extended-search-protocol.md).
Stage2 uses native Kissat/CaDiCaL CNF, or CP-SAT. Stage3 resolves every
candidate STS and expands any success for the independent LKTS checker.
All search restrictions and timeout/skipped-candidate distinctions are logged.
"""
import argparse
from collections import Counter, defaultdict
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import random
import signal
import subprocess
import sys
import time

for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"

from ortools.sat.python import cp_model
import ortools
from search_cyclic import orbit_key, write_certificate

ACTIVE_SOLVER = None
ACTIVE_PROCESS = None
CANCELLED = False


def cancel(signum, frame):
    global CANCELLED
    CANCELLED = True
    if ACTIVE_SOLVER is not None:
        ACTIVE_SOLVER.stop_search()
    if ACTIVE_PROCESS is not None and ACTIVE_PROCESS.poll() is None:
        os.killpg(ACTIVE_PROCESS.pid, signal.SIGTERM)


signal.signal(signal.SIGTERM, cancel)
signal.signal(signal.SIGINT, cancel)


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def proto_hash(model):
    return hashlib.sha256(str(model.proto).encode()).hexdigest()


def cp_solve(model, seconds, threads, seed):
    global ACTIVE_SOLVER
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = max(0.001, seconds)
    solver.parameters.num_search_workers = threads
    solver.parameters.random_seed = seed
    solver.parameters.randomize_search = True
    ACTIVE_SOLVER = solver
    status = solver.solve(model)
    ACTIVE_SOLVER = None
    return solver, status, {"instance_sha256": proto_hash(model), "solver": "CP-SAT",
                           "status": solver.status_name(status), "cap_seconds": seconds,
                           "wall_seconds": solver.wall_time, "threads": threads, "seed": seed,
                           "branches": solver.num_branches, "conflicts": solver.num_conflicts}


def matching_pair(n, seed, seconds, patterned):
    rng = random.Random(seed)
    pairs = list(itertools.combinations(range(1, n), 2))
    rng.shuffle(pairs)
    model = cp_model.CpModel()
    columns = defaultdict(list)
    variables = []
    for side in range(2):
        for x, y in pairs:
            if patterned and side == 0 and (x+y) % n:
                continue
            var = model.new_bool_var(f"m{side}_{x}_{y}")
            variables.append((var, side, (x,y)))
            columns[("point",side,x)].append(var)
            columns[("point",side,y)].append(var)
            columns[("difference",side,min(y-x,n-y+x))].append(var)
            columns[("edge",x,y)].append(var)
    for side in range(2):
        for x in range(1,n):
            model.add_exactly_one(columns[("point",side,x)])
        for d in range(1,(n+1)//2):
            model.add_exactly_one(columns[("difference",side,d)])
    for x,y in pairs:
        model.add_at_most_one(columns[("edge",x,y)])
    # A seeded random linear objective diversifies matching samples. Only
    # feasibility is required; an optimality proof is not used downstream.
    model.minimize(sum(rng.randrange(-100,101)*var for var,_,_ in variables))
    solver,status,info = cp_solve(model,seconds,1,seed)
    if status not in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        return None,info
    result = [[],[]]
    for var,side,pair in variables:
        if solver.value(var):
            result[side].append(pair)
    return [sorted(x) for x in result],info


def certificate_matchings(path, n):
    # Read only the first constituent; no generator assumptions about its classes.
    blocks = []
    inside = False
    for raw in Path(path).read_text().splitlines():
        line = raw.partition("#")[0].strip()
        if line == "KTS 0":
            inside = True
        elif line.startswith("KTS ") and inside:
            break
        elif inside and line and line[0].isdigit():
            blocks.append(tuple(sorted(map(int,line.split()))))
    if (0,n,n+1) not in blocks:
        raise ValueError("validation certificate must already have infinity-pair block at0")
    result = []
    for infinity in (n,n+1):
        result.append(sorted(tuple(x for x in b if x != infinity) for b in blocks
                             if infinity in b and len([x for x in b if x >= n]) == 1))
    validate_matchings(n,result)
    return result


def validate_matchings(n, matchings):
    assert len(matchings) == 2
    for matching in matchings:
        assert Counter(x for p in matching for x in p) == Counter(range(1,n))
        assert sorted(min((y-x)%n,(x-y)%n) for x,y in matching) == list(range(1,(n+1)//2))
    assert not set(matchings[0]).intersection(matchings[1])


def finite_cover(n, matchings, seed):
    forbidden = set(matchings[0]) | set(matchings[1])
    triples = list(itertools.combinations(range(n),3))
    orbit_names = sorted({orbit_key(b,n) for b in triples})
    orbit_ids = {key:i for i,key in enumerate(orbit_names)}
    allowed_pairs = [p for p in itertools.combinations(range(n),2) if p not in forbidden]
    pair_ids = {p:i for i,p in enumerate(allowed_pairs)}
    rows = [b for b in triples if all(p not in forbidden for p in itertools.combinations(b,2))]
    random.Random(seed).shuffle(rows)
    columns = [[] for _ in range(len(allowed_pairs)+len(orbit_names))]
    for row_id,b in enumerate(rows,1):
        for pair in itertools.combinations(b,2):
            columns[pair_ids[pair]].append(row_id)
        columns[len(allowed_pairs)+orbit_ids[orbit_key(b,n)]].append(row_id)
    return rows,columns


class CNF:
    """Exactly-one: at-least-one plus Sinz sequential at-most-one clauses.

    For k>3 use prefix auxiliaries s1..s(k-1):
    (-x1,s1); (-xi,si),(-s(i-1),si),(-xi,-s(i-1)); (-xk,-s(k-1)).
    Small k uses pairwise clauses. A fixed-width header permits incremental
    blocking clauses without rewriting or retaining the whole CNF in RAM.
    """
    def __init__(self,path,primary,columns):
        self.path = Path(path)
        self.variables = primary
        self.clauses = 0
        with self.path.open("wb") as stream:
            self.stream = stream
            stream.write(self.header())
            for literals in columns:
                self.add(literals)
                if len(literals) <= 3:
                    for x,y in itertools.combinations(literals,2):
                        self.add((-x,-y))
                else:
                    aux = list(range(self.variables+1,self.variables+len(literals)))
                    self.variables += len(aux)
                    self.add((-literals[0],aux[0]))
                    for i in range(1,len(literals)-1):
                        self.add((-literals[i],aux[i]))
                        self.add((-aux[i-1],aux[i]))
                        self.add((-literals[i],-aux[i-1]))
                    self.add((-literals[-1],-aux[-1]))
            stream.seek(0)
            stream.write(self.header())
        self.stream = None

    def header(self):
        return f"p cnf {self.variables:014d} {self.clauses:014d}\n".encode()

    def add(self,literals):
        self.stream.write((" ".join(map(str,literals))+" 0\n").encode())
        self.clauses += 1

    def block(self,selected):
        with self.path.open("r+b") as stream:
            self.stream = stream
            stream.seek(0,2)
            self.add([-x for x in selected])
            stream.seek(0)
            stream.write(self.header())
        self.stream = None


def native_solve(cnf,primary,solver_name,config,seed,seconds,tmp,log_path):
    global ACTIVE_PROCESS
    cap = max(1,math.ceil(seconds))
    if solver_name == "kissat":
        command = ["kissat",f"--{config}",f"--seed={seed}",f"--time={cap}",str(cnf.path)]
    else:
        command = ["cadical",f"--{config}",f"--seed={seed}","--shuffle=true","--shufflerandom=true","-t",str(cap),str(cnf.path)]
    instance = digest(cnf.path)
    raw = tmp / "solver.stdout"
    started = time.monotonic()
    timed_out = False
    with raw.open("wb") as stream:
        ACTIVE_PROCESS = subprocess.Popen(command,stdin=subprocess.DEVNULL,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        try:
            returncode = ACTIVE_PROCESS.wait(timeout=cap+10)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(ACTIVE_PROCESS.pid,signal.SIGTERM)
            returncode = ACTIVE_PROCESS.wait(timeout=30)
        finally:
            ACTIVE_PROCESS = None
    selected = []
    status = "UNKNOWN"
    with raw.open() as stream, gzip.open(log_path,"wt") as log:
        for line in stream:
            if line.startswith("v "):
                selected.extend(x for x in map(int,line[2:].split()) if 0 < x <= primary)
            else:
                log.write(line)
                if line.startswith("s SATISFIABLE"):
                    status = "SAT"
                elif line.startswith("s UNSATISFIABLE"):
                    status = "UNSAT"
    if returncode not in (0,10,20,-signal.SIGTERM,128+signal.SIGTERM) and not timed_out and not CANCELLED:
        status = "ERROR"
    return sorted(set(selected)), {"instance_sha256":instance,"solver":solver_name,"config":config,
            "seed":seed,"threads":1,"cap_seconds":seconds,"native_rounded_cap_seconds":cap,
            "wall_seconds":time.monotonic()-started,"status":status,"exit_code":returncode,
            "external_timeout":timed_out,"command":command,"variables":cnf.variables,"clauses":cnf.clauses,
            "raw_output_sha256":digest(raw),"statistics_log":str(log_path)}


def validate_base(v,blocks):
    pairs = Counter(p for b in blocks for p in itertools.combinations(sorted(b),2))
    assert len(blocks) == v*(v-1)//6
    assert pairs == Counter(itertools.combinations(range(v),2))
    assert len({orbit_key(b,v-2) for b in blocks}) == len(blocks)


def resolve(v,blocks,matchings,seconds,threads,seed):
    n = v-2
    classes = (v-1)//2
    anchors = {0:(0,n,n+1)}
    for x,y in matchings[0]:
        anchors[min((y-x)%n,(x-y)%n)] = tuple(sorted((x,y,n)))
    reverse_anchor = {b:c for c,b in anchors.items()}
    model = cp_model.CpModel()
    columns = defaultdict(list)
    variables = []
    order = list(enumerate(blocks))
    random.Random(seed).shuffle(order)
    for bi,b in order:
        allowed = [reverse_anchor[b]] if b in reverse_anchor else range(classes)
        for c in allowed:
            if b not in reverse_anchor and set(b).intersection(anchors[c]):
                continue
            var = model.new_bool_var(f"b{bi}c{c}")
            variables.append((var,bi,c))
            columns[("block",bi)].append(var)
            for x in b:
                columns[("point",c,x)].append(var)
    for bi in range(len(blocks)):
        model.add_exactly_one(columns[("block",bi)])
    for c in range(classes):
        for x in range(v):
            model.add_exactly_one(columns[("point",c,x)])
    solver,status,info = cp_solve(model,seconds,threads,seed)
    if status not in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        return None,info
    base = [[] for _ in range(classes)]
    for var,bi,c in variables:
        if solver.value(var):
            base[c].append(blocks[bi])
    return base,info


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v",type=int,required=True)
    ap.add_argument("--solver",choices=["kissat","cadical","cpsat"],required=True)
    ap.add_argument("--config",choices=["default","sat","unsat"],default="default")
    ap.add_argument("--seed",type=int,required=True)
    ap.add_argument("--seconds",type=float,default=7200)
    ap.add_argument("--threads",type=int,default=1)
    ap.add_argument("--matching-seconds",type=float,default=5)
    ap.add_argument("--sts-seconds",type=float,default=180)
    ap.add_argument("--resolution-seconds",type=float,default=90)
    ap.add_argument("--candidates-per-matching",type=int,default=20)
    ap.add_argument("--patterned",action="store_true")
    ap.add_argument("--starter-from",type=Path)
    ap.add_argument("--output",type=Path,required=True)
    args = ap.parse_args()
    if args.v < 9 or args.v % 6 != 3 or not 1<=args.threads<=2:
        ap.error("v>=9 is3 mod6; this portfolio permits1 or2 threads per runner")
    started = time.monotonic()
    deadline = started+args.seconds
    n = args.v-2
    args.output.parent.mkdir(parents=True,exist_ok=True)
    artifact_dir = args.output.parent / (args.output.name+"-data")
    artifact_dir.mkdir(exist_ok=True)
    tmp = Path("/tmp/ai4s-lkts-staged")/(args.output.name+f"-{os.getpid()}")
    tmp.mkdir(parents=True,exist_ok=True)
    ledger_path = args.output.with_suffix(".jsonl")
    ledger = ledger_path.open("w",buffering=1)
    receipt = {"v":args.v,"model":"cyclic transversal; frozen rainbow infinity matchings; then STS; then resolution",
               "source_sha256":digest(__file__),"helper_sha256":digest(Path(__file__).with_name("search_cyclic.py")),
               "checker_sha256":digest(Path(__file__).with_name("check_lkts.py")),"parameters":vars(args).copy(),
               "ortools_version":ortools.__version__,"pid":os.getpid(),"thread_cap":args.threads,
               "wall_clock_cap_seconds":args.seconds,"status":"RUNNING","tmp":str(tmp),"command":sys.argv}
    receipt["parameters"] = {k:str(value) if isinstance(value,Path) else value for k,value in receipt["parameters"].items()}
    if args.solver != "cpsat":
        receipt["native_solver_version"] = subprocess.check_output([args.solver,"--version"],text=True).strip()
    args.output.with_suffix(".json").write_text(json.dumps(receipt,indent=2))
    counts = Counter()
    def log(phase,info,**extras):
        event = {"phase":phase,"elapsed_seconds":time.monotonic()-started,**info,**extras}
        counts[phase+":"+str(info.get("status","RECORDED"))] += 1
        ledger.write(json.dumps(event)+"\n")
    attempt = 0
    found = False
    while time.monotonic()<deadline and not CANCELLED and not found:
        seed = args.seed + attempt*100003
        remaining = deadline-time.monotonic()
        if remaining <= 0:
            break
        if args.starter_from:
            if attempt:
                break
            matchings = certificate_matchings(args.starter_from,n)
            matching_info = {"status":"INPUT_CERTIFICATE","cap_seconds":0,"wall_seconds":0,
                             "certificate_sha256":digest(args.starter_from),"seed":seed}
        else:
            matchings,matching_info = matching_pair(n,seed,min(args.matching_seconds,remaining),args.patterned)
        log("matchings",matching_info,attempt=attempt,patterned=args.patterned)
        if matchings is None:
            attempt += 1
            continue
        validate_matchings(n,matchings)
        matching_file = artifact_dir/f"matching-{attempt:05d}.json"
        matching_file.write_text(json.dumps({"n":n,"matchings":matchings,"seed":seed,"patterned":args.patterned},indent=2))
        rows,columns = finite_cover(n,matchings,seed)
        cnf = None
        cpmodel = None
        cpvars = None
        if args.solver == "cpsat":
            cpmodel = cp_model.CpModel()
            cpvars = [cpmodel.new_bool_var(f"t{i}") for i in range(len(rows))]
            for column in columns:
                cpmodel.add_exactly_one(cpvars[x-1] for x in column)
        else:
            cnf = CNF(tmp/"instance.cnf",len(rows),columns)
        log("encoding",{"status":"BUILT","primary_rows":len(rows),"exact_cover_columns":len(columns),
                        "matching_sha256":digest(matching_file),"row_order_seed":seed},attempt=attempt)
        skipped_resolution_unknown = 0
        for ci in range(args.candidates_per_matching):
            remaining = deadline-time.monotonic()
            if remaining <= 0 or CANCELLED:
                break
            solve_seed = (seed*1009+ci*97) % 2000000000
            cap = min(args.sts_seconds,remaining)
            if args.solver == "cpsat":
                solver,status,info = cp_solve(cpmodel,cap,args.threads,solve_seed)
                selected = [i+1 for i,var in enumerate(cpvars) if solver.value(var)] if status in (cp_model.OPTIMAL,cp_model.FEASIBLE) else []
                sat = status in (cp_model.OPTIMAL,cp_model.FEASIBLE)
            else:
                selected,info = native_solve(cnf,len(rows),args.solver,args.config,solve_seed,cap,tmp,
                                             artifact_dir/f"sts-{attempt:05d}-{ci:03d}.log.gz")
                sat = info["status"] == "SAT"
            log("sts",info,attempt=attempt,candidate=ci,blocked_candidates=ci,
                blocked_candidates_with_unresolved_resolution=skipped_resolution_unknown)
            if info["status"] in ("ERROR","MODEL_INVALID"):
                raise RuntimeError(f"solver error; see {ledger_path}")
            if not sat:
                break
            blocks = [(0,n,n+1)] + [tuple(sorted((x,y,n))) for x,y in matchings[0]] + [tuple(sorted((x,y,n+1))) for x,y in matchings[1]] + [rows[i-1] for i in selected]
            validate_base(args.v,blocks)
            candidate_file = artifact_dir/f"sts-{attempt:05d}-{ci:03d}.json"
            candidate_file.write_text(json.dumps({"v":args.v,"blocks":blocks,"selected_primary_literals":selected,
                                                 "matching_file":str(matching_file),"sts_instance_sha256":info["instance_sha256"]}))
            remaining = deadline-time.monotonic()
            if remaining <= 0 or CANCELLED:
                break
            base,resolution_info = resolve(args.v,blocks,matchings,min(args.resolution_seconds,remaining),args.threads,solve_seed)
            log("resolution",resolution_info,attempt=attempt,candidate=ci,candidate_sha256=digest(candidate_file))
            if base is not None:
                certificate = args.output.with_suffix(".txt")
                write_certificate(certificate,args.v,base)
                checked = subprocess.run([sys.executable,str(Path(__file__).with_name("check_lkts.py")),str(certificate)],capture_output=True,text=True)
                args.output.with_suffix(".check.json").write_text(checked.stdout)
                if checked.returncode:
                    raise RuntimeError("independent checker rejected candidate: "+checked.stdout+checked.stderr)
                receipt.update(status="FOUND_VERIFIED",certificate=str(certificate),certificate_sha256=digest(certificate),checker_exit_code=0)
                found = True
                break
            if resolution_info["status"] == "UNKNOWN":
                skipped_resolution_unknown += 1
            if args.solver == "cpsat":
                cpmodel.add_bool_or(cpvars[i-1].Not() for i in selected)
            else:
                cnf.block(selected)
        attempt += 1
    ledger.close()
    if not found:
        receipt["status"] = "UNKNOWN_CANCELLED" if CANCELLED else "UNKNOWN_PORTFOLIO_COMPLETE"
    receipt.update(wall_seconds=time.monotonic()-started,matching_attempts=attempt,phase_counts=dict(counts),
                   ledger_sha256=digest(ledger_path),background_children_remaining=0)
    args.output.with_suffix(".json").write_text(json.dumps(receipt,indent=2))
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__":
    main()
