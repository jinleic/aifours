#!/usr/bin/env python3
"""C19 on Z_19 x {0,1,2}: fixed resolved KTSs and free constituent orbits.

Run from the target directory with OR-Tools 9.15.6755 installed:
  python work/c19_search.py --fixed 36 --seconds 7200 --output evidence/c19-36
  python work/c19_search.py --fixed 17 --seconds 7200 --output evidence/c19-17

The 36-fixed pattern has an elementary AAA-orbit obstruction. The 17-fixed
search freezes a greedily generated disjoint fixed-system packing, then solves
for two arbitrary resolved orbit-transversal bases on the remaining orbits.
Failure of that staged slice is NOT nonexistence of an invariant large set.
"""
import argparse
from array import array
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time


N = 19
V = 57
CLASSES = 28


def translate(block, shift):
    return tuple(sorted(N * (point // N) + (point % N + shift) % N for point in block))


def orbit_key(block):
    return min(translate(block, -(point % N)) for point in block)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + "\n")


def inventory():
    pairs = list(itertools.combinations(range(V), 2))
    pair_keys = sorted({orbit_key(pair) for pair in pairs})
    pair_ids = {key: index for index, key in enumerate(pair_keys)}
    keys = sorted({orbit_key(block) for block in itertools.combinations(range(V), 3)})
    orbit_ids = {key: index for index, key in enumerate(keys)}
    records = []
    for key in keys:
        layers = len({point // N for point in key})
        pair_orbits = [pair_ids[orbit_key(pair)] for pair in itertools.combinations(key, 2)]
        records.append({"representative": key, "type": ("AAA", "AAB", "ABC")[layers - 1],
                        "pair_orbits": pair_orbits,
                        "fixed_admissible": len(set(pair_orbits)) == 3})
    counts = Counter(row["type"] for row in records)
    invalid = [i for i, row in enumerate(records) if not row["fixed_admissible"]]
    assert len(pair_keys) == 84 and len(keys) == 1540
    assert counts == {"AAA": 153, "AAB": 1026, "ABC": 361}
    assert len(invalid) == 27
    assert all(records[i]["type"] == "AAA" for i in invalid)
    assert all(len({translate(key, t) for t in range(N)}) == N for key in keys)
    # Independent concrete check: precisely the AP orbits repeat a pair after development.
    ap_keys = {orbit_key((N * layer + (center - step) % N, N * layer + center,
                          N * layer + (center + step) % N))
               for layer in range(3) for center in range(N) for step in range(1, 10)}
    assert ap_keys == {keys[i] for i in invalid}
    for index, row in enumerate(records):
        expanded_pairs = [pair for t in range(N)
                          for pair in itertools.combinations(translate(keys[index], t), 2)]
        assert (len(set(expanded_pairs)) == 57) == row["fixed_admissible"]
    return {"point_encoding": "19*layer + coordinate", "pair_orbits": pair_keys,
            "triple_orbits": records, "counts": dict(counts),
            "inadmissible_fixed_AAA_orbit_ids": invalid}, orbit_ids


def check_kts(classes):
    assert len(classes) == CLASSES
    pairs = set()
    blocks = set()
    for parallel in classes:
        assert len(parallel) == 19
        assert sorted(point for block in parallel for point in block) == list(range(V))
        for block in parallel:
            assert len(set(block)) == 3 and block not in blocks
            blocks.add(block)
            for pair in itertools.combinations(sorted(block), 2):
                assert pair not in pairs
                pairs.add(pair)
    assert pairs == set(itertools.combinations(range(V), 2)) and len(blocks) == 532
    return blocks


def expand_fixed(candidate):
    return [[translate(block, shift) for block in candidate["starter_class"]]
            for shift in range(N)] + [
                [translate(block, shift) for shift in range(N)]
                for block in candidate["fixed_class_seeds"]]


def validate_fixed(candidate, orbit_ids):
    blocks = check_kts(expand_fixed(candidate))
    actual = {orbit_ids[orbit_key(block)] for block in blocks}
    assert len(actual) == 28 and actual == set(candidate["orbit_ids"])
    return actual


def model_hash(model):
    return digest(str(model.proto).encode())


def solve(model, seconds, threads, seed, log_path, cp_model):
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = max(0.001, seconds)
    solver.parameters.num_search_workers = threads
    solver.parameters.random_seed = seed
    solver.parameters.log_search_progress = True
    solver.parameters.log_to_stdout = False
    config = str(solver.parameters)
    with Path(log_path).open("w") as log:
        solver.log_callback = lambda text: log.write(text + "\n")
        status = solver.solve(model)
    summary = {"status": solver.status_name(status), "solver_wall_seconds": solver.wall_time,
               "wall_limit_seconds": seconds, "threads": threads, "seed": seed,
               "parameters": config, "branches": solver.num_branches,
               "conflicts": solver.num_conflicts, "log_path": str(log_path)}
    return solver, status, summary


def fixed_model(data, forbidden, aaa_count, cp_model):
    model = cp_model.CpModel()
    points = [[] for _ in range(V)]
    pairs = [[] for _ in range(84)]
    aaa = []
    rows = []
    for oid, record in enumerate(data["triple_orbits"]):
        if oid in forbidden or not record["fixed_admissible"]:
            continue
        if aaa_count == 4 and record["type"] == "ABC":
            shifts = ()  # z=2u-8=0, so these can only seed fixed classes.
        else:
            shifts = range(N)
        for shift in shifts:
            block = translate(record["representative"], shift)
            var = model.new_bool_var("")
            rows.append((oid, shift))
            for point in block:
                points[point].append(var)
            for pair in record["pair_orbits"]:
                pairs[pair].append(var)
            if record["type"] == "AAA":
                aaa.append(var)
        if record["type"] == "ABC":
            var = model.new_bool_var("")
            rows.append((oid, -1))
            for pair in record["pair_orbits"]:
                pairs[pair].append(var)
    for column in points + pairs:
        model.add_exactly_one(column)
    model.add(sum(aaa) == aaa_count)
    return model, rows


def extract_fixed(solver, rows, data):
    starter, seeds, orbit_ids = [], [], []
    for index, selected in enumerate(solver.response_proto.solution):
        if not selected:
            continue
        oid, shift = rows[index]
        orbit_ids.append(oid)
        key = data["triple_orbits"][oid]["representative"]
        (seeds if shift == -1 else starter).append(key if shift == -1 else translate(key, shift))
    assert len(starter) == 19 and len(seeds) == 9 and len(set(orbit_ids)) == 28
    return {"starter_class": sorted(starter), "fixed_class_seeds": sorted(seeds),
            "orbit_ids": sorted(orbit_ids)}


def completion_model(data, remaining, bases, cp_model):
    model = cp_model.CpModel()
    pair_ids = {pair: index for index, pair in enumerate(itertools.combinations(range(V), 2))}
    pair_columns = [[[] for _ in pair_ids] for _ in range(bases)]
    point_columns = [[[[] for _ in range(V)] for _ in range(CLASSES)] for _ in range(bases)]
    class_minima = [[[] for _ in range(CLASSES)] for _ in range(bases)]
    first_partners = [[] for _ in range(bases)]
    rows = array("I")
    blocks = []
    for oid in sorted(remaining):
        orbit_vars = []
        for shift in range(N):
            block = translate(data["triple_orbits"][oid]["representative"], shift)
            bid = len(blocks)
            blocks.append(block)
            pair_indices = [pair_ids[pair] for pair in itertools.combinations(block, 2)]
            if block[0] == 0:
                # Classes sorted by the least nonzero point in their 0-block.
                # Its c-th value lies in [c+1,2c+1], by the perfect matching.
                least = block[1]
                allowed_classes = range((least - 1 + 1) // 2, min(least - 1, CLASSES - 1) + 1)
            else:
                allowed_classes = range(CLASSES)
            for base in range(bases):
                for c in allowed_classes:
                    var = model.new_bool_var("")
                    rows.append((bid * bases + base) * CLASSES + c)
                    orbit_vars.append(var)
                    for point in block:
                        point_columns[base][c][point].append(var)
                    for pair in pair_indices:
                        pair_columns[base][pair].append(var)
                    if block[0] == 0:
                        class_minima[base][c].append((block[1], var))
                        if block[1] == 1:
                            first_partners[base].append((block[2], var))
        # Exactly one block from this orbit over all bases, not one per base.
        model.add_exactly_one(orbit_vars)
    for base in range(bases):
        for column in pair_columns[base]:
            model.add_exactly_one(column)
        for parallel in point_columns[base]:
            for column in parallel:
                model.add_exactly_one(column)
        minima = [sum(weight * var for weight, var in values) for values in class_minima[base]]
        for c in range(CLASSES - 1):
            model.add(minima[c] < minima[c + 1])
    if bases == 2:
        # The two base systems are interchangeable; their 0,1-completions differ.
        model.add(sum(weight * var for weight, var in first_partners[0]) <
                  sum(weight * var for weight, var in first_partners[1]))
    return model, rows, blocks


def extract_bases(solver, rows, blocks, bases):
    result = [[[] for _ in range(CLASSES)] for _ in range(bases)]
    for index, selected in enumerate(solver.response_proto.solution):
        if selected:
            quotient, c = divmod(rows[index], CLASSES)
            bid, base = divmod(quotient, bases)
            result[base][c].append(blocks[bid])
    for classes in result:
        check_kts(classes)
    return result


def write_certificate(path, fixed, bases):
    with Path(path).open("w") as stream:
        stream.write("# C19 on points 19*layer+coordinate\nLKTS 57\n")
        index = 0
        for candidate in fixed:
            stream.write(f"\nKTS {index}\n")
            for c, parallel in enumerate(expand_fixed(candidate)):
                stream.write(f"CLASS {c}\n")
                for block in parallel:
                    stream.write(" ".join(map(str, block)) + "\n")
            index += 1
        for classes in bases:
            for shift in range(N):
                stream.write(f"\nKTS {index}\n")
                for c, parallel in enumerate(classes):
                    stream.write(f"CLASS {c}\n")
                    for block in parallel:
                        stream.write(" ".join(map(str, translate(block, shift))) + "\n")
                index += 1
        assert index == 55


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixed", type=int, choices=(17, 36), required=True)
    parser.add_argument("--seconds", type=float, default=7200)
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--seed", type=int, default=191714)
    parser.add_argument("--fixed-aaa", type=int, choices=range(4, 10), default=4)
    parser.add_argument("--candidate-seconds", type=float, default=90)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.seconds <= 0 or args.candidate_seconds <= 0 or not 1 <= args.threads <= 4:
        parser.error("positive wall caps and 1..4 solver threads are required")
    started = time.monotonic()
    deadline = started + args.seconds
    prefix = args.output
    prefix.parent.mkdir(parents=True, exist_ok=True)
    receipt_path = Path(str(prefix) + ".json")
    if receipt_path.exists():
        parser.error("output receipt already exists; choose a fresh prefix")
    source = Path(__file__).read_bytes()
    Path(str(prefix) + ".source.py").write_bytes(source)
    receipt = {"v": V, "action": "(x,layer) -> (x+1 mod 19,layer)",
               "fixed_constituents": args.fixed, "free_constituent_orbits": (55 - args.fixed) // 19,
               "source_sha256": digest(source), "command": sys.argv, "python": platform.python_version(),
               "wall_clock_cap_seconds": args.seconds, "thread_cap": args.threads,
               "seed": args.seed, "status": "RUNNING", "phases": [],
               "restrictions": {"invariant_chosen_resolutions_of_fixed_systems": True,
                                "fixed_generation_AAA_per_starter": args.fixed_aaa,
                                "fixed_packing": "greedy, restart on failed candidate solve; first complete packing frozen",
                                "completion": "arbitrary two resolved orbit-transversal bases on frozen complement",
                                "class_symmetry_breaking": "sort 0-block least other points; order bases by 0,1 completion"}}
    data, orbit_ids = inventory()
    inventory_bytes = (json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n").encode()
    Path(str(prefix) + ".inventory.json").write_bytes(inventory_bytes)
    receipt["inventory_sha256"] = digest(inventory_bytes)
    receipt["phases"].append({"phase": "exhaustive_orbit_inventory", "status": "PASS",
                              "wall_seconds": time.monotonic() - started, "triple_orbits": 1540,
                              "pair_orbits": 84, "inadmissible_fixed_AAA": 27,
                              "admissible_fixed_AAA": 126})
    if 4 * args.fixed > 126:
        receipt.update(status="PROVED_IMPOSSIBLE", scope="entire specified resolved C19 constituent pattern",
                       obstruction={"required_AAA_orbits_at_least": 4 * args.fixed,
                                    "available_fixed_admissible_AAA_orbits": 126,
                                    "argument": "Every fixed resolved KTS has u>=4 AAA orbits; the 27 AP AAA orbits repeat pairs and cannot be used by fixed systems."},
                       total_seconds=time.monotonic() - started,
                       peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save_json(receipt_path, receipt)
        print(json.dumps(receipt, indent=2), flush=True)
        return 0
    from ortools.sat.python import cp_model
    import ortools
    receipt["ortools_version"] = ortools.__version__
    save_json(receipt_path, receipt)
    fixed, forbidden, attempt, restarts = [], set(), 0, 0
    while len(fixed) < args.fixed and time.monotonic() < deadline:
        phase_start = time.monotonic()
        model, rows = fixed_model(data, forbidden, args.fixed_aaa, cp_model)
        instance_hash = model_hash(model)
        build_seconds = time.monotonic() - phase_start
        cap = min(args.candidate_seconds, max(0.001, deadline - time.monotonic()))
        solver, status, phase = solve(model, cap, args.threads, args.seed + attempt,
                                      f"{prefix}.fixed-{attempt:04d}.log", cp_model)
        phase.update(phase="fixed_candidate", index_in_packing=len(fixed), attempt=attempt,
                     restart=restarts, instance_sha256=instance_hash, rows=len(rows),
                     forbidden_orbit_ids=sorted(forbidden), fixed_AAA=args.fixed_aaa,
                     build_seconds=build_seconds, wall_seconds=time.monotonic() - phase_start)
        if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
            candidate = extract_fixed(solver, rows, data)
            used = validate_fixed(candidate, orbit_ids)
            assert not forbidden.intersection(used)
            fixed.append(candidate)
            forbidden.update(used)
            phase["candidate"] = candidate
            phase["expanded_KTS_check"] = "PASS"
            save_json(f"{prefix}.packing-{restarts:03d}.json", fixed)
        else:
            # This only discards one greedy prefix; no claim of global infeasibility.
            phase["failed_prefix_length"] = len(fixed)
            fixed, forbidden = [], set()
            restarts += 1
        receipt["phases"].append(phase)
        receipt.update(fixed_systems_in_current_packing=len(fixed), restarts=restarts,
                       elapsed_seconds=time.monotonic() - started)
        save_json(receipt_path, receipt)
        print(json.dumps({"phase": phase["phase"], "attempt": attempt, "status": phase["status"],
                          "fixed": len(fixed), "elapsed_seconds": receipt["elapsed_seconds"]}), flush=True)
        attempt += 1
        del model, rows, solver
    receipt["fixed_systems_in_current_packing"] = len(fixed)
    if len(fixed) == args.fixed and time.monotonic() < deadline:
        remaining = set(range(1540)) - forbidden
        assert len(remaining) == 532 * receipt["free_constituent_orbits"]
        packing_path = Path(str(prefix) + ".frozen-packing.json")
        save_json(packing_path, fixed)
        receipt["frozen_packing_sha256"] = digest(packing_path.read_bytes())
        phase_start = time.monotonic()
        model, rows, blocks = completion_model(data, remaining, receipt["free_constituent_orbits"], cp_model)
        instance_hash = model_hash(model)
        build_seconds = time.monotonic() - phase_start
        phase = {"phase": "frozen_packing_completion", "status": "RUNNING", "rows": len(rows),
                 "instance_sha256": instance_hash, "remaining_orbit_ids": sorted(remaining),
                 "build_seconds": build_seconds, "frozen_packing_sha256": receipt["frozen_packing_sha256"]}
        receipt["phases"].append(phase)
        save_json(receipt_path, receipt)
        cap = max(0.001, deadline - time.monotonic())
        solver, status, summary = solve(model, cap, args.threads, args.seed + 1000000,
                                        f"{prefix}.completion.log", cp_model)
        phase.update(summary, wall_seconds=time.monotonic() - phase_start)
        receipt["status"] = "UNKNOWN" if status == cp_model.UNKNOWN else "RESTRICTED_" + solver.status_name(status)
        if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
            bases = extract_bases(solver, rows, blocks, receipt["free_constituent_orbits"])
            certificate = Path(str(prefix) + ".txt")
            write_certificate(certificate, fixed, bases)
            checked = subprocess.run([sys.executable, str(Path(__file__).with_name("check_lkts.py")),
                                      str(certificate)], text=True, capture_output=True)
            Path(str(prefix) + ".check.json").write_text(checked.stdout)
            receipt.update(certificate_sha256=digest(certificate.read_bytes()),
                           checker_exit_code=checked.returncode, checker_stderr=checked.stderr,
                           status="CERTIFICATE_FOUND" if checked.returncode == 0 else "CHECKER_FAILURE")
    else:
        receipt["status"] = "UNKNOWN"
        receipt["incomplete_stage"] = "greedy_fixed_packing"
    receipt.update(total_seconds=time.monotonic() - started,
                   peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                   scope="restricted staged slice, not all C19-invariant large sets")
    save_json(receipt_path, receipt)
    print(json.dumps({"status": receipt["status"], "total_seconds": receipt["total_seconds"],
                      "receipt": str(receipt_path)}), flush=True)
    return 1 if receipt["status"] == "CHECKER_FAILURE" else 0


if __name__ == "__main__":
    sys.exit(main())
