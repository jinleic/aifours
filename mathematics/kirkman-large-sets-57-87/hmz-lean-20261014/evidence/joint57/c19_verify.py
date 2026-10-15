#!/usr/bin/env python3
"""Independently replay C19 orbit arithmetic and expanded fixed-KTS witnesses.

Standard library only; does not trust the searcher's orbit IDs or KTS checks.
It does not certify a negative CP-SAT answer. Positive full LKTS witnesses are
also passed to the existing group-independent checker.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def shifted(subset, amount):
    return tuple(sorted((point // 19) * 19 + (point + amount) % 19 for point in subset))


def key(subset):
    # Deliberately enumerate all group elements, unlike the searcher's shortcut.
    return min(shifted(subset, shift) for shift in range(19))


def check_fixed(candidate):
    starter = [tuple(block) for block in candidate["starter_class"]]
    seeds = [tuple(block) for block in candidate["fixed_class_seeds"]]
    classes = [[shifted(block, shift) for block in starter] for shift in range(19)]
    classes.extend([[shifted(seed, shift) for shift in range(19)] for seed in seeds])
    assert len(classes) == 28
    blocks = set()
    pair_counts = Counter()
    for parallel in classes:
        assert len(parallel) == 19
        assert Counter(point for block in parallel for point in block) == Counter(range(57))
        for block in parallel:
            assert len(set(block)) == 3 and all(0 <= point < 57 for point in block)
            assert block not in blocks
            blocks.add(block)
            pair_counts.update(itertools.combinations(block, 2))
    assert len(blocks) == 532
    assert pair_counts == Counter(itertools.combinations(range(57), 2))
    assert {shifted(block, 1) for block in blocks} == blocks
    assert {tuple(sorted(parallel)) for parallel in classes} == {
        tuple(sorted(shifted(block, 1) for block in parallel)) for parallel in classes}
    return {key(block) for block in blocks}


def verify_inventory(data):
    triples = list(itertools.combinations(range(57), 3))
    orbit_counts = Counter(key(block) for block in triples)
    assert len(orbit_counts) == 1540 and set(orbit_counts.values()) == {19}
    records = data["triple_orbits"]
    keys = [tuple(row["representative"]) for row in records]
    assert keys == sorted(orbit_counts)
    pair_keys = sorted({key(pair) for pair in itertools.combinations(range(57), 2)})
    assert len(pair_keys) == 84 and [tuple(pair) for pair in data["pair_orbits"]] == pair_keys
    pair_ids = {pair: index for index, pair in enumerate(pair_keys)}
    types = Counter()
    rejected = []
    for index, representative in enumerate(keys):
        record = records[index]
        kind = ("AAA", "AAB", "ABC")[len({point // 19 for point in representative}) - 1]
        types[kind] += 1
        assert kind == record["type"]
        assert [pair_ids[key(pair)] for pair in itertools.combinations(representative, 2)] == record["pair_orbits"]
        actual = Counter(pair for t in range(19) for pair in itertools.combinations(shifted(representative, t), 2))
        admissible = max(actual.values()) == 1
        assert admissible == record["fixed_admissible"]
        if not admissible:
            rejected.append(index)
            assert kind == "AAA"
    assert types == {"AAA": 153, "AAB": 1026, "ABC": 361}
    assert rejected == data["inadmissible_fixed_AAA_orbit_ids"] and len(rejected) == 27
    # Prove the nine AP orbits per layer are distinct using the full action.
    ap_keys = {key((layer * 19, layer * 19 + step, layer * 19 + (2 * step) % 19))
               for layer in range(3) for step in range(1, 19)}
    assert ap_keys == {keys[index] for index in rejected}
    return keys, pair_keys


def verify(receipt_path):
    receipt_path = Path(receipt_path)
    receipt = json.loads(receipt_path.read_text())
    assert receipt["status"] != "RUNNING", "a running receipt is not final evidence"
    prefix = receipt_path.with_suffix("")
    source_path = Path(str(prefix) + ".source.py")
    inventory_path = Path(str(prefix) + ".inventory.json")
    assert sha(source_path) == receipt["source_sha256"]
    assert sha(inventory_path) == receipt["inventory_sha256"]
    data = json.loads(inventory_path.read_text())
    keys, pair_keys = verify_inventory(data)
    key_to_id = {representative: index for index, representative in enumerate(keys)}
    current = set()
    generated = 0
    max_fixed = 0
    completion = None
    for phase in receipt["phases"]:
        if phase["phase"] == "fixed_candidate":
            assert phase["forbidden_orbit_ids"] == sorted(current)
            assert phase["index_in_packing"] == len(current) // 28
            assert 1 <= phase["threads"] <= 4 and phase["wall_limit_seconds"] > 0
            assert len(phase["instance_sha256"]) == 64
            assert Path(phase["log_path"]).is_file()
            if phase["status"] in ("FEASIBLE", "OPTIMAL"):
                candidate = phase["candidate"]
                actual = {key_to_id[orbit] for orbit in check_fixed(candidate)}
                assert len(actual) == 28 and actual == set(candidate["orbit_ids"])
                aaa = sum(len({point // 19 for point in block}) == 1 for block in candidate["starter_class"])
                assert aaa == phase["fixed_AAA"]
                assert not current.intersection(actual)
                current.update(actual)
                generated += 1
                max_fixed = max(max_fixed, len(current) // 28)
            else:
                assert phase["status"] in ("INFEASIBLE", "UNKNOWN")
                current.clear()
        elif phase["phase"] == "frozen_packing_completion":
            completion = phase
            assert len(current) == 28 * receipt["fixed_constituents"]
            remaining = set(range(1540)) - current
            assert remaining == set(phase["remaining_orbit_ids"])
            # Every pair-orbit has 55 occurrences among all triple-orbit seeds;
            # fixed constituents each remove one. Two bases need 38 in total.
            counts = Counter(pair for oid in remaining for pair in data["triple_orbits"][oid]["pair_orbits"])
            assert counts == Counter({pair: 38 for pair in range(84)})
            packing_path = Path(str(prefix) + ".frozen-packing.json")
            assert sha(packing_path) == receipt["frozen_packing_sha256"] == phase["frozen_packing_sha256"]
            saved = json.loads(packing_path.read_text())
            assert len(saved) == 17
            frozen_ids = set()
            for candidate in saved:
                actual = {key_to_id[orbit] for orbit in check_fixed(candidate)}
                assert not frozen_ids.intersection(actual)
                frozen_ids.update(actual)
            assert current == frozen_ids
    if receipt["status"] == "PROVED_IMPOSSIBLE":
        assert receipt["fixed_constituents"] == 36
        assert 4 * receipt["fixed_constituents"] > 153 - 27
    if receipt["status"] == "CERTIFICATE_FOUND":
        certificate = Path(str(prefix) + ".txt")
        assert sha(certificate) == receipt["certificate_sha256"]
        checked = subprocess.run([sys.executable, str(Path(__file__).with_name("check_lkts.py")), str(certificate)],
                                 capture_output=True, text=True)
        assert checked.returncode == 0, checked.stdout + checked.stderr
    result = {"receipt": str(receipt_path), "receipt_sha256": sha(receipt_path),
              "source_sha256": receipt["source_sha256"], "inventory_sha256": receipt["inventory_sha256"],
              "status": receipt["status"], "verdict": "PASS",
              "independently_checked_fixed_candidates": generated, "maximum_disjoint_fixed_packing": max_fixed,
              "completion_status": completion["status"] if completion else None,
              "scope": "orbit arithmetic and positive fixed-KTS witnesses; no negative solver proof replay"}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipts", type=Path, nargs="+")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("refusing to overwrite existing validation evidence")
    started = time.monotonic()
    results = [verify(receipt) for receipt in args.receipts]
    result = {"verdict": "PASS", "verifier_sha256": sha(__file__), "command": sys.argv,
              "total_seconds": time.monotonic() - started, "receipts": results}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
