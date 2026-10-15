#!/usr/bin/env python3
"""Joint modular all-different encoding of a cyclic-transversal STS, then resolve.

Unlike search_staged.py, the two infinity matchings are NOT frozen samples:
all their positions and every finite-orbit shift are solved jointly. This is
an exact cyclic STS model; only candidate enumeration/resolution timeouts
limit the constructive portfolio. No nonidentity multiplier is imposed.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path
import subprocess
import sys
import time

import search_staged as staged
from ortools.sat.python import cp_model
import ortools


def build_model(v):
    n = v-2
    half = (n-1)//2
    representatives = sorted({staged.orbit_key(b,n) for b in itertools.combinations(range(n),3)})
    assert len(representatives) == (n-1)*(n-2)//6
    model = cp_model.CpModel()
    pair_positions = [[] for _ in range(half+1)]
    infinity_starts = []
    primary = []
    for side in range(2):
        starts = []
        endpoints = []
        for d in range(1,half+1):
            start = model.new_int_var(1,n-1,f"infinity{side}_d{d}")
            end = model.new_int_var(1,n-1,f"endpoint{side}_d{d}")
            model.add_modulo_equality(end,start+d,n)
            endpoints.extend((start,end))
            pair_positions[d].append(start)
            starts.append(start)
            primary.append(start)
        model.add_all_different(endpoints)
        infinity_starts.append(starts)
    # Swapping the infinity labels interchanges these distinct d=1 starts.
    # This is label symmetry only, not an automorphism required of the design.
    model.add(infinity_starts[0][0] < infinity_starts[1][0])
    shifts = []
    for oid,block in enumerate(representatives):
        shift = model.new_int_var(0,n-1,f"shift{oid}")
        shifts.append(shift)
        primary.append(shift)
        for pi,(x,y) in enumerate(itertools.combinations(block,2)):
            delta = (y-x)%n
            d = min(delta,n-delta)
            offset = x if delta == d else y
            position = model.new_int_var(0,n-1,f"pairpos{oid}_{pi}")
            model.add_modulo_equality(position,shift+offset,n)
            pair_positions[d].append(position)
    for d in range(1,half+1):
        assert len(pair_positions[d]) == n
        model.add_all_different(pair_positions[d])
    return model,primary,infinity_starts,shifts,representatives


def extract(v,solver,infinity_starts,shifts,representatives):
    n = v-2
    matchings = []
    for starts in infinity_starts:
        matchings.append(sorted(tuple(sorted((solver.value(var),(solver.value(var)+d)%n)))
                                for d,var in enumerate(starts,1)))
    staged.validate_matchings(n,matchings)
    blocks = [(0,n,n+1)]
    blocks.extend(tuple(sorted((x,y,n))) for x,y in matchings[0])
    blocks.extend(tuple(sorted((x,y,n+1))) for x,y in matchings[1])
    for var,block in zip(shifts,representatives):
        shift = solver.value(var)
        blocks.append(tuple(sorted((x+shift)%n for x in block)))
    staged.validate_base(v,blocks)
    return blocks,matchings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v",type=int,required=True)
    ap.add_argument("--seed",type=int,required=True)
    ap.add_argument("--seconds",type=float,default=7200)
    ap.add_argument("--sts-seconds",type=float,default=7200)
    ap.add_argument("--resolution-seconds",type=float,default=240)
    ap.add_argument("--output",type=Path,required=True)
    args = ap.parse_args()
    if args.v<9 or args.v%6 != 3:
        ap.error("v>=9 must be3 modulo6")
    started = time.monotonic()
    deadline = started+args.seconds
    args.output.parent.mkdir(parents=True,exist_ok=True)
    data_dir = args.output.parent/(args.output.name+"-data")
    data_dir.mkdir(exist_ok=True)
    model,primary,starts,shifts,reps = build_model(args.v)
    receipt = {"v":args.v,"model":"joint modular cyclic STS + unrestricted resolution; no frozen infinity matching",
               "parameters":{k:str(x) if isinstance(x,Path) else x for k,x in vars(args).items()},
               "source_sha256":staged.digest(__file__),"helper_sha256":staged.digest(staged.__file__),
               "ortools_version":ortools.__version__,"threads":1,"pid":staged.os.getpid(),
               "wall_clock_cap_seconds":args.seconds,"build_seconds":time.monotonic()-started,
               "initial_instance_sha256":staged.proto_hash(model),"primary_variables":len(primary),
               "total_integer_variables":len(model.proto.variables),"finite_triple_orbits":len(reps),
               "status":"RUNNING","command":sys.argv}
    args.output.with_suffix(".json").write_text(json.dumps(receipt,indent=2))
    phases = Counter()
    candidates = 0
    unknown_resolutions = 0
    with args.output.with_suffix(".jsonl").open("w",buffering=1) as ledger:
        while time.monotonic()<deadline and not staged.CANCELLED:
            remaining = deadline-time.monotonic()
            if remaining <= 0:
                break
            seed = args.seed+candidates
            solver,status,info = staged.cp_solve(model,min(args.sts_seconds,remaining),1,seed)
            phases["sts:"+info["status"]] += 1
            ledger.write(json.dumps({"phase":"sts","candidate":candidates,"blocked_candidates":candidates,
                                    "blocked_with_unknown_resolution":unknown_resolutions,**info})+"\n")
            if status not in (cp_model.OPTIMAL,cp_model.FEASIBLE):
                receipt["last_sts_status"] = solver.status_name(status)
                break
            blocks,matchings = extract(args.v,solver,starts,shifts,reps)
            values = [solver.value(var) for var in primary]
            candidate_file = data_dir/f"candidate-{candidates:05d}.json"
            candidate_file.write_text(json.dumps({"v":args.v,"blocks":blocks,"matchings":matchings,
                                                 "primary_assignment":values,"instance_sha256":info["instance_sha256"]}))
            remaining = deadline-time.monotonic()
            if remaining <= 0 or staged.CANCELLED:
                break
            base,res_info = staged.resolve(args.v,blocks,matchings,min(args.resolution_seconds,remaining),1,seed)
            phases["resolution:"+res_info["status"]] += 1
            ledger.write(json.dumps({"phase":"resolution","candidate":candidates,
                                    "candidate_sha256":staged.digest(candidate_file),**res_info})+"\n")
            candidates += 1
            if base is not None:
                cert = args.output.with_suffix(".txt")
                staged.write_certificate(cert,args.v,base)
                checked = subprocess.run([sys.executable,str(Path(__file__).with_name("check_lkts.py")),str(cert)],capture_output=True,text=True)
                args.output.with_suffix(".check.json").write_text(checked.stdout)
                if checked.returncode:
                    raise RuntimeError("independent checker failed: "+checked.stdout+checked.stderr)
                receipt.update(status="FOUND_VERIFIED",certificate=str(cert),certificate_sha256=staged.digest(cert),checker_exit_code=0)
                break
            if res_info["status"] == "UNKNOWN":
                unknown_resolutions += 1
            model.add_forbidden_assignments(primary,[values])
    if receipt["status"] == "RUNNING":
        receipt["status"] = "UNKNOWN_CANCELLED" if staged.CANCELLED else "UNKNOWN_PORTFOLIO_COMPLETE"
    receipt.update(wall_seconds=time.monotonic()-started,candidate_count=candidates,
                   unresolved_candidate_resolutions=unknown_resolutions,phase_counts=dict(phases),
                   ledger_sha256=staged.digest(args.output.with_suffix(".jsonl")),background_children_remaining=0)
    args.output.with_suffix(".json").write_text(json.dumps(receipt,indent=2))
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__":
    main()
