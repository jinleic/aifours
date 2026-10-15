#!/usr/bin/env python3
"""Bounded F55=C11 semidirect C5 starter/triangle/unrestricted-resolution search.

Coordinates are x+11*y; multiplication is (x,y)(z,t)=(x+3**y*z,y+t).
The two infinity starters are frozen only within each finite-triangle stage.
No automorphism of the base STS or its resolution is imposed.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import random
import signal
import subprocess
import sys
import time

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"

from group_blockset import digest, resolution_model

ACTIVE_SOLVER = None
CANCELLED = False


def cancel(signum, frame):
    global CANCELLED
    CANCELLED = True
    if ACTIVE_SOLVER is not None:
        ACTIVE_SOLVER.stop_search()


signal.signal(signal.SIGTERM, cancel)
signal.signal(signal.SIGINT, cancel)


def group_tables():
    product = [[(a % 11 + pow(3, a//11, 11)*(b % 11)) % 11 + 11*((a//11+b//11) % 5)
                for b in range(55)] for a in range(55)]
    inverse = [next(b for b in range(55) if product[a][b] == product[b][a] == 0) for a in range(55)]
    assert all(product[0][a] == product[a][0] == a for a in range(55))
    assert all(product[product[a][b]][c] == product[a][product[b][c]]
               for a in range(55) for b in range(55) for c in range(55))
    assert any(product[a][b] != product[b][a] for a in range(55) for b in range(55))
    return product, inverse


def orbit_key(block, product, inverse):
    finite = [x for x in block if x < 55]
    fixed = tuple(x for x in block if x >= 55)
    return min(tuple(sorted(product[inverse[t]][x] for x in finite))+fixed for t in finite)


def difference(a, b, product, inverse):
    d = product[inverse[a]][b]
    return min(d, inverse[d])


def validate_matchings(matchings, product, inverse):
    labels = {min(x, inverse[x]) for x in range(1, 55)}
    for matching in matchings:
        assert Counter(x for edge in matching for x in edge) == Counter(range(1, 55))
        assert Counter(difference(*edge, product, inverse) for edge in matching) == Counter(labels)
    assert not set(matchings[0]).intersection(matchings[1])


def validate_base(blocks, product, inverse):
    assert len(blocks) == len(set(blocks)) == 532
    assert Counter(pair for b in blocks for pair in itertools.combinations(b, 2)) == Counter(itertools.combinations(range(57), 2))
    assert len({orbit_key(b, product, inverse) for b in blocks}) == 532


def write_certificate(path, base, product):
    with path.open("w") as stream:
        stream.write("# F55 left development: point=x+11*y; fixed infinities55,56\nLKTS 57\n")
        for g in range(55):
            stream.write(f"\nKTS {g}\n")
            for c, parallel in enumerate(base):
                stream.write(f"CLASS {c}\n")
                for block in parallel:
                    stream.write(" ".join(map(str, sorted(product[g][x] if x < 55 else x for x in block)))+"\n")


def main():
    from ortools.sat.python import cp_model
    import ortools
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=7200)
    parser.add_argument("--starter-seconds", type=float, default=5)
    parser.add_argument("--triangle-seconds", type=float, default=300)
    parser.add_argument("--resolution-seconds", type=float, default=180)
    parser.add_argument("--candidates-per-starter", type=int, default=3)
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--seed", type=int, default=5501)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.threads <= 2 or args.candidates_per_starter < 1 or min(args.seconds, args.starter_seconds, args.triangle_seconds, args.resolution_seconds) <= 0:
        parser.error("threads1..2, positive deadlines and candidates-per-starter required")
    if any(args.output.with_suffix(suffix).exists() for suffix in (".json", ".jsonl", ".log")):
        parser.error("output already exists; preserve evidence")
    started = time.monotonic()
    deadline = started+args.seconds
    product, inverse = group_tables()
    triples = list(itertools.combinations(range(55), 3))
    triple_orbits = Counter(orbit_key(b, product, inverse) for b in triples)
    assert len(triple_orbits) == 477 and set(triple_orbits.values()) == {55}
    all_triple_orbits = Counter(orbit_key(b, product, inverse) for b in itertools.combinations(range(57), 3))
    assert len(all_triple_orbits) == 532 and set(all_triple_orbits.values()) == {55}
    source = Path(__file__).resolve()
    receipt = {"v": 57, "development_group": "C11 semidirect C5, faithful action3mod11; left regular on55points, fixes55,56",
        "restrictions": ["base KTS contains one representative of every F55 triple orbit",
                         "infinity-pair block normalized to {0,55,56}",
                         "starter pair fixed within each triangle stage, resampled across stages",
                         "no prescribed base block automorphism and no resolution invariance",
                         "point0 incident blocks fix resolution color names only",
                         "UNKNOWN triangle/resolution calls do not exclude their frozen starters/base STSs"],
        "source_sha256": digest(source), "resolution_helper_sha256": digest(source.with_name("group_blockset.py")),
        "cyclic_helper_import_sha256": digest(source.with_name("search_cyclic.py")),
        "checker_sha256": digest(source.with_name("check_lkts.py")),
        "group_instance_sha256": hashlib.sha256(json.dumps(product, separators=(",", ":")).encode()).hexdigest(),
        "group_validation": "identity,inverses,associativity,noncommutativity and all532 full triple-orbits checked",
        "group_triple_orbits": 532, "finite_triple_orbits": 477,
        "parameters": {k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
        "python": platform.python_version(), "ortools_version": ortools.__version__,
        "command": sys.argv, "wall_clock_cap_seconds": args.seconds, "threads": args.threads,
        "status": "RUNNING", "calls": Counter(), "starters": [], "candidates": []}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    data = args.output.parent / (args.output.name+"-data")
    data.mkdir()
    def save():
        receipt["runtime_seconds"] = time.monotonic()-started
        args.output.with_suffix(".json").write_text(json.dumps(receipt, indent=2)+"\n")
    save()
    with args.output.with_suffix(".jsonl").open("w", buffering=1) as ledger, args.output.with_suffix(".log").open("w") as log:
        def solve(model, stage, cap, seed, **context):
            global ACTIVE_SOLVER
            remaining = deadline-time.monotonic()
            if CANCELLED or remaining <= 0:
                return None, None
            solver = cp_model.CpSolver()
            solver.parameters.max_time_in_seconds = min(cap, remaining)
            solver.parameters.num_search_workers = args.threads
            solver.parameters.random_seed = seed
            solver.parameters.randomize_search = True
            solver.parameters.max_memory_in_mb = 3500
            solver.parameters.log_search_progress = True
            solver.parameters.log_to_stdout = False
            solver.log_callback = lambda text: log.write(text+"\n")
            instance = data / f"{stage}-{context['attempt']:04}-{context.get('candidate', 0):02}.pbtxt"
            if not model.export_to_file(str(instance)):
                raise OSError(f"cannot freeze CP-SAT instance: {instance}")
            info = {"stage": stage, **context, "instance_sha256": hashlib.sha256(str(model.proto).encode()).hexdigest(),
                    "instance_path": str(instance), "instance_file_sha256": digest(instance),
                    "parameters": str(solver.parameters), "cap_seconds": solver.parameters.max_time_in_seconds,
                    "seed": seed, "threads": args.threads, "started_elapsed_seconds": time.monotonic()-started}
            log.write("\nSTAGE "+json.dumps(info)+"\n")
            ledger.write(json.dumps({**info, "status": "STARTED"})+"\n")
            ACTIVE_SOLVER = solver
            status = solver.solve(model)
            ACTIVE_SOLVER = None
            info.update(status=solver.status_name(status), wall_seconds=solver.wall_time,
                        conflicts=solver.num_conflicts, branches=solver.num_branches,
                        finished_elapsed_seconds=time.monotonic()-started)
            ledger.write(json.dumps(info)+"\n")
            receipt["calls"][stage+":"+info["status"]] += 1
            log.flush()
            save()
            return status, solver
        starter_model = cp_model.CpModel()
        starter_rows = []
        columns = defaultdict(list)
        for side in range(2):
            for edge in itertools.combinations(range(1, 55), 2):
                x, y = edge
                var = starter_model.new_bool_var(f"m{side}_{x}_{y}")
                starter_rows.append((var, side, edge))
                for key in (("point", side, x), ("point", side, y), ("difference", side, difference(x, y, product, inverse)), ("edge", x, y)):
                    columns[key].append(var)
        for key, variables in columns.items():
            if key[0] == "edge":
                starter_model.add_at_most_one(variables)
            else:
                starter_model.add_exactly_one(variables)
        attempt = 0
        found = False
        while time.monotonic() < deadline and not CANCELLED and not found:
            seed = args.seed+1009*attempt
            rng = random.Random(seed)
            starter_model.minimize(sum(rng.randrange(-100, 101)*var for var, _, _ in starter_rows))
            status, solver = solve(starter_model, "starters", args.starter_seconds, seed, attempt=attempt)
            if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                if status == cp_model.INFEASIBLE:
                    receipt["status"] = "STARTER_SPACE_EXHAUSTED"
                    break
                attempt += 1
                continue
            chosen = [(var, side, edge) for var, side, edge in starter_rows if solver.value(var)]
            matchings = [sorted(edge for _, side, edge in chosen if side == s) for s in range(2)]
            validate_matchings(matchings, product, inverse)
            starter_model.add_bool_or([var.Not() for var, _, _ in chosen])
            starter_path = data / f"starter-{attempt:04}.json"
            starter_path.write_text(json.dumps({"matchings": matchings, "seed": seed}, separators=(",", ":")))
            receipt["starters"].append({"path": str(starter_path), "sha256": digest(starter_path)})
            forbidden = set(matchings[0]) | set(matchings[1])
            triangle_model = cp_model.CpModel()
            triangle_rows = []
            tcolumns = defaultdict(list)
            allowed = [b for b in triples if all(pair not in forbidden for pair in itertools.combinations(b, 2))]
            rng.shuffle(allowed)
            for block in allowed:
                var = triangle_model.new_bool_var(f"t{len(triangle_rows)}")
                triangle_rows.append((var, block))
                for pair in itertools.combinations(block, 2):
                    tcolumns[("pair",)+pair].append(var)
                tcolumns[("orbit",)+orbit_key(block, product, inverse)].append(var)
            required = {("pair",)+p for p in itertools.combinations(range(55), 2) if p not in forbidden}
            required.update(("orbit",)+key for key in triple_orbits)
            for key in sorted(required):
                triangle_model.add_exactly_one(tcolumns[key])
            for candidate in range(args.candidates_per_starter):
                status, solver = solve(triangle_model, "finite_triangles", args.triangle_seconds, seed+candidate,
                                       attempt=attempt, candidate=candidate, starter_sha256=digest(starter_path))
                if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                    break
                selected = [(var, block) for var, block in triangle_rows if solver.value(var)]
                blocks = sorted([block for _, block in selected] + [(0, 55, 56)] +
                                [tuple(sorted(edge+(55+side,))) for side, matching in enumerate(matchings) for edge in matching])
                validate_base(blocks, product, inverse)
                block_path = data / f"base-{attempt:04}-{candidate:02}.json"
                block_path.write_text(json.dumps({"blocks": blocks}, separators=(",", ":")))
                item = {"path": str(block_path), "sha256": digest(block_path), "validation": "pair cover and F55 orbit transversal passed"}
                receipt["candidates"].append(item)
                coloring, colors = resolution_model(blocks, 57, cp_model)
                rstatus, rsolver = solve(coloring, "unrestricted_resolution", args.resolution_seconds, seed+candidate,
                                         attempt=attempt, candidate=candidate, base_sha256=digest(block_path))
                item["resolution_status"] = "DEADLINE" if rstatus is None else rsolver.status_name(rstatus)
                if rstatus in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                    base = [[] for _ in range(28)]
                    for block, color in zip(blocks, colors):
                        base[rsolver.value(color)].append(block)
                    certificate = args.output.with_suffix(".txt")
                    write_certificate(certificate, base, product)
                    checked = subprocess.run([sys.executable, str(source.with_name("check_lkts.py")), str(certificate)], capture_output=True, text=True)
                    args.output.with_suffix(".check.json").write_text(checked.stdout)
                    receipt.update(status="CERTIFIED" if checked.returncode == 0 else "CHECKER_REJECTED",
                                   checker_exit_code=checked.returncode, checker_stderr=checked.stderr,
                                   certificate_sha256=digest(certificate))
                    found = True
                    break
                triangle_model.add_bool_or([var.Not() for var, _ in selected])
                save()
            attempt += 1
        if receipt["status"] == "RUNNING":
            receipt["status"] = "CANCELLED" if CANCELLED else "TIME_LIMIT_NO_CERTIFICATE"
    save()
    print(json.dumps({key: receipt[key] for key in ("status", "runtime_seconds", "calls")}, indent=2))


if __name__ == "__main__":
    main()
