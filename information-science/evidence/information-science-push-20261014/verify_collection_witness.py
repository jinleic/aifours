"""Exact full-row-distribution verifier for column-permuted collection VCS witnesses.

Input encodings are complete binary column masks, with rational probabilities.
Uniformly permuting all columns of a sampled encoding makes full projected
histogram distribution equality equivalent to full ordered projected-matrix
security. Expected column counts alone are explicitly not sufficient.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def probability(encoding):
    p = encoding["probability"]
    value = Fraction(int(p["numerator"]), int(p["denominator"]))
    if value <= 0:
        raise ValueError("Only positive support probabilities are allowed")
    return value


def projected_histogram(columns, rows):
    return tuple(sorted(Counter(column & rows for column in columns).items()))


def qualified_masks(n, minimal):
    return [q for q in range(1, 1 << n) if any(q & a == a for a in minimal)]


def verify_witness(witness):
    n, m = int(witness["n"]), int(witness["m"])
    if n < 1 or m < 1:
        raise ValueError("n and m must be positive")
    minimal = [int(a) for a in witness["minimal_qualified"]]
    if not minimal or any(a < 1 or a >= 1 << n for a in minimal):
        raise ValueError("Invalid minimal qualified sets")
    supports = [witness["encodings0"], witness["encodings1"]]
    for support in supports:
        if not support or sum((probability(e) for e in support), Fraction()) != 1:
            raise ValueError("Each secret must have a normalized nonempty support")
        for entry in support:
            if len(entry["columns"]) != m or any(
                    not isinstance(c, int) or c < 0 or c >= 1 << n for c in entry["columns"]):
                raise ValueError("Every encoding must have m valid n-bit columns")
    qualified = qualified_masks(n, minimal)
    forbidden = [f for f in range(1 << n) if f not in qualified]
    leaks = []
    for f in forbidden:
        distributions = []
        for support in supports:
            masses = defaultdict(Fraction)
            for encoding in support:
                masses[projected_histogram(encoding["columns"], f)] += probability(encoding)
            distributions.append(dict(masses))
        if distributions[0] != distributions[1]:
            leaks.append(f)
    gaps = {}
    for q in qualified:
        white_max = max(sum(bool(c & q) for c in e["columns"]) for e in supports[0])
        black_min = min(sum(bool(c & q) for c in e["columns"]) for e in supports[1])
        gaps[q] = black_min - white_max
    actual = min(gaps.values())
    valid = not leaks and actual >= int(witness["claimed_gap"]) >= 1
    return {"verified": valid, "n": n, "m": m, "actual_gap": actual,
            "claimed_gap": int(witness["claimed_gap"]), "forbidden_security_leaks": leaks,
            "qualified_gaps": gaps, "support_sizes": [len(s) for s in supports]}


def entry(columns, denominator=1):
    return {"columns": columns, "probability": {"numerator": 1, "denominator": denominator}}


def controls():
    basis = {"n": 3, "m": 4, "minimal_qualified": [7], "claimed_gap": 1,
             "encodings0": [entry([0, 3, 5, 6])],
             "encodings1": [entry([1, 2, 4, 7])]}
    mixed = {"n": 3, "m": 5, "minimal_qualified": [7], "claimed_gap": 1,
             "encodings0": [entry([0, 3, 5, 6, 1], 2), entry([0, 3, 5, 6, 2], 2)],
             "encodings1": [entry([1, 2, 4, 7, 1], 2), entry([1, 2, 4, 7, 2], 2)]}
    leaked = {"n": 3, "m": 6, "minimal_qualified": [7], "claimed_gap": 1,
              "encodings0": [entry([0, 3, 3, 3, 3, 6], 2), entry([0, 3, 3, 5, 5, 6], 2)],
              "encodings1": [entry([1, 2, 4, 7, 3, 3])]}
    # The leaked scheme passes every expected forbidden projected-COLUMN count,
    # yet leaks full projected-MATRIX information and must be rejected.
    for f in range(7):
        mean_columns = []
        for support in (leaked["encodings0"], leaked["encodings1"]):
            mean = defaultdict(Fraction)
            for e in support:
                for pattern, count in projected_histogram(e["columns"], f):
                    mean[pattern] += probability(e) * count
            mean_columns.append(dict(mean))
        if mean_columns[0] != mean_columns[1]:
            raise AssertionError("Security negative control lacks the intended first-moment match")
    rows = {"basis_positive": verify_witness(basis),
            "genuine_collection_positive": verify_witness(mixed),
            "higher_order_security_negative": verify_witness(leaked)}
    if not rows["basis_positive"]["verified"] or not rows["genuine_collection_positive"]["verified"]:
        raise AssertionError(rows)
    if rows["higher_order_security_negative"]["verified"]:
        raise AssertionError("Full-distribution security leak was accepted")
    bad_gap = dict(basis, claimed_gap=2)
    rows["contrast_negative"] = verify_witness(bad_gap)
    if rows["contrast_negative"]["verified"]:
        raise AssertionError("False reconstruction gap was accepted")
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = {"representation": "uniform global column permutations; exact rational support weights",
              "controls": controls(), "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.input:
        raw = args.input.read_bytes()
        candidate = json.loads(raw)
        witnesses = candidate if isinstance(candidate, list) else [candidate]
        report["input_sha256"] = hashlib.sha256(raw).hexdigest()
        report["witnesses"] = [verify_witness(w) for w in witnesses]
        if not all(r["verified"] for r in report["witnesses"]):
            raise AssertionError(report["witnesses"])
    report["verified"] = True
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
