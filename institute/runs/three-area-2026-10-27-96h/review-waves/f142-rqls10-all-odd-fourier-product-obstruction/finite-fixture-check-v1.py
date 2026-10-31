#!/usr/bin/env python3
"""Materialize and replay four exact negative controls against our own f142 checker."""
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKER_SHA = "35a89a1504832fee220c56a09af5e64fe28d1152b49c44d00529d92633e12ca1"
RECEIPT_SHA = "6b62ebed978c649785f215ac7cb20472c2b38176463edf59e026ec7ebc4e49c7"
checker_path = HERE / "finite-check-v1.py"
if hashlib.sha256(checker_path.read_bytes()).hexdigest() != CHECKER_SHA:
    raise ValueError("own checker SHA mismatch before import")
spec = importlib.util.spec_from_file_location("f142_own_finite_checker", checker_path)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
c = checker


def main():
    start_clock = c.clock()
    start = time.monotonic()
    c.require(c.sha(checker_path.read_bytes()) == CHECKER_SHA, "own_checker_sha")
    prior_bytes = (HERE / "finite-receipt-v1.json").read_bytes()
    c.require(c.sha(prior_bytes) == RECEIPT_SHA, "own_prior_receipt_sha")
    prior = c.strict_json(prior_bytes.decode("utf-8"))
    texts, fingerprints = c.read_pinned_inputs()
    certificate = c.strict_json(texts[2])
    rows, _ = c.build_rows()
    graph, _ = c.build_graph(rows)
    _, eligible = c.enumerate_triangles(graph)
    records = certificate["certificates"]
    c.bind_certificate(certificate, eligible, len(rows))

    iso_index = next(i for i, rec in enumerate(records) if "isolated" in rec)
    iso = records[iso_index]
    iso_graph = c.half_graph([c.ZERO, c.SECOND] + [rows[i] for i in iso["triple"]])
    wrong_iso = {**iso, "isolated": next(v for v in range(10) if iso_graph[v])}
    c.require(c.sha(c.json_bytes(wrong_iso)) == prior["mutation_controls"]["wrong_isolated_witness"]["input_sha256"], "wrong_isolate_binding")
    iso_records = list(records)
    iso_records[iso_index] = wrong_iso

    cut_index = next(i for i, rec in enumerate(records) if "odd_component" in rec)
    cut = records[cut_index]
    cut_graph = c.half_graph([c.ZERO, c.SECOND] + [rows[i] for i in cut["triple"]])
    old = set(cut["odd_component"])
    replacement = None
    for v in sorted(old):
        for w in sorted(set(range(10)) - old):
            trial = sorted((old - {v}) | {w})
            mask = sum(1 << x for x in trial)
            if any(cut_graph[x] & (((1 << 10) - 1) ^ mask) for x in trial):
                replacement = trial
                break
        if replacement is not None:
            break
    c.require(replacement is not None, "wrong_cut_not_constructible")
    wrong_cut = {**cut, "odd_component": replacement}
    c.require(c.sha(c.json_bytes(wrong_cut)) == prior["mutation_controls"]["wrong_crossing_odd_cut"]["input_sha256"], "wrong_cut_binding")
    cut_records = list(records)
    cut_records[cut_index] = wrong_cut

    controls = [
        ("removed", {**certificate, "certificates": records[:-1]}, "missing_triangles"),
        ("duplicated", {**certificate, "certificates": records + [records[0]]}, "duplicate_triple"),
        ("wrong-isolate", {**certificate, "certificates": iso_records}, "isolate_not_isolated"),
        ("wrong-cut", {**certificate, "certificates": cut_records}, "odd_cut_crosses"),
    ]
    c.require(c.sha(c.json_bytes(controls[0][1])) == prior["mutation_controls"]["removed_record"]["input_sha256"], "removed_binding")
    c.require(c.sha(c.json_bytes(controls[1][1])) == prior["mutation_controls"]["duplicated_record"]["input_sha256"], "duplicate_binding")
    receipt_path = HERE / "finite-fixture-receipt-v1.json"
    paths = [HERE / ("finite-fixture-" + name + "-v1.json") for name, _, _ in controls]
    c.require(not receipt_path.exists() and all(not path.exists() for path in paths), "fixture_output_exists")
    results = []
    for (name, payload, expected), path in zip(controls, paths):
        data = c.json_bytes(payload)
        with path.open("xb") as stream:
            stream.write(data)
        persisted = path.read_bytes()
        c.require(persisted == data, "fixture_write_mismatch", name)
        mutated = c.strict_json(persisted.decode("utf-8"))
        try:
            seen = c.bind_certificate(mutated, eligible, len(rows))
            c.check_record_graphs(seen, rows)
        except c.CheckError as exc:
            c.require(exc.reason == expected, "fixture_wrong_failure", {"name": name, "expected": expected, "actual": exc.reason})
            results.append({"name": name, "path": str(path), "bytes": len(persisted), "sha256": c.sha(persisted),
                            "expected_reason": expected, "actual_reason": exc.reason, "result": "REJECTED"})
        else:
            raise c.CheckError("fixture_not_rejected", name)
    positive = c.positive_half_control(rows, graph)
    receipt = {"kind": "F142_RETAINED_FIXTURE_REPLAY", "status": "ALL_CHECKS_PASSED_BEFORE_RECEIPT_WRITE",
               "observed_start_native_clock": start_clock,
               "observed_native_clock_immediately_before_receipt_write": c.clock(),
               "elapsed_monotonic_seconds_before_receipt_write": round(time.monotonic() - start, 3),
               "fixture_checker": {"path": str(Path(__file__).resolve()), "sha256": c.sha(Path(__file__).read_bytes())},
               "own_independent_checker_sha256": CHECKER_SHA, "own_original_receipt_sha256": RECEIPT_SHA,
               "frozen_inputs": fingerprints, "fixtures": results, "matching_positive_control": positive,
               "isolate_original": iso, "isolate_mutated": wrong_iso,
               "odd_cut_original": cut, "odd_cut_mutated": wrong_cut}
    encoded = (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")
    with receipt_path.open("xb") as stream:
        stream.write(encoded)
    print("PASS retained fixture replays; removed, duplicate, false isolate, crossing odd cut; matching positive")
    print("receipt_sha256", c.sha(encoded))
    print("elapsed_seconds", receipt["elapsed_monotonic_seconds_before_receipt_write"])


if __name__ == "__main__":
    try:
        main()
    except c.CheckError as exc:
        print("FAIL", str(exc), file=sys.stderr)
        sys.exit(1)
