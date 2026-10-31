#!/usr/bin/env python3
"""Independently parse a paper-table transcription and trace all six pairs.

Real coefficient c=(a+b*sqrt(2))/sqrt(72). Uses direct dense partial traces,
not the sparse Gram implementation in the companion local-rotation script.
"""
import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path
import sys


class CertificateError(ValueError):
    pass


def load_table(path):
    raw = path.read_bytes()
    data = {}
    seen_cells = []
    for line_number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 3 or parts[0] not in "012345" or parts[1] not in "012345":
            raise CertificateError(f"bad record at line {line_number}")
        a, b = int(parts[0]), int(parts[1])
        if len(parts[0]) != 1 or len(parts[1]) != 1:
            raise CertificateError(f"bad cell labels at line {line_number}")
        seen_cells.append((a, b))
        for tok in parts[2:]:
            if len(tok) != 3 or tok[0] not in "+-s" or any(x not in "012345" for x in tok[1:]):
                raise CertificateError(f"bad coefficient token at line {line_number}")
            index = (a, b, int(tok[1]), int(tok[2]))
            if index in data:
                raise CertificateError(f"duplicate tensor coordinate at line {line_number}")
            data[index] = (0, 1) if tok[0] == "s" else (1 if tok[0] == "+" else -1, 0)
    if seen_cells != list(itertools.product(range(6), repeat=2)):
        raise CertificateError("expected all 36 cells in lexicographic order exactly once")
    return data, hashlib.sha256(raw).hexdigest()


def exact_partial_trace(data):
    norm_rational = sum(a*a + 2*b*b for a, b in data.values())
    norm_radical = sum(2*a*b for a, b in data.values())
    if (norm_rational, norm_radical) != (72, 0):
        raise CertificateError(f"normalization: {(norm_rational, norm_radical)} != (72, 0)")
    checks = []
    for keep in itertools.combinations(range(4), 2):
        trace = tuple(k for k in range(4) if k not in keep)
        examined = 0
        for row in itertools.product(range(6), repeat=2):
            for col in itertools.product(range(6), repeat=2):
                rr = ss = 0
                for hidden in itertools.product(range(6), repeat=2):
                    x = [0]*4
                    y = [0]*4
                    for k, v in zip(keep, row):
                        x[k] = v
                    for k, v in zip(keep, col):
                        y[k] = v
                    for k, v in zip(trace, hidden):
                        x[k] = y[k] = v
                    a, b = data.get(tuple(x), (0, 0))
                    c, d = data.get(tuple(y), (0, 0))
                    rr += a*c + 2*b*d
                    ss += a*d + b*c
                expected = (2 if row == col else 0, 0)
                if (rr, ss) != expected:
                    raise CertificateError(f"marginal {keep} row {row} col {col}: {(rr, ss)} != {expected}")
                examined += 1
        checks.append({"parties_zero_based": keep, "entries_checked": examined, "numerator": "2 I", "denominator": 72})
    return {"squared_norm_numerator": [norm_rational, norm_radical], "denominator": 72, "marginals": checks}


def support_structure(data):
    if len(data) != 60:
        raise CertificateError(f"support: expected 60, got {len(data)}")
    axes = []
    for axis in range(4):
        fibers = collections.Counter(tuple(v for j, v in enumerate(index) if j != axis) for index in data)
        if max(fibers.values(), default=0) != 1:
            raise CertificateError(f"Hamming-one support collision on axis {axis}")
        counts = [sum(index[axis] == v for index in data) for v in range(6)]
        if counts != [9, 12, 12, 9, 9, 9]:
            raise CertificateError(f"axis {axis} level counts differ: {counts}")
        axes.append({"axis": axis, "distinct_three_coordinate_fibers": len(fibers), "counts_by_level": counts})
    return axes


def must_reject(data, expected_prefix):
    try:
        exact_partial_trace(data)
    except CertificateError as exc:
        if not str(exc).startswith(expected_prefix):
            raise CertificateError(f"mutation rejected for wrong reason: {exc}") from exc
        return str(exc)
    raise CertificateError(f"mutation unexpectedly accepted; expected {expected_prefix}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    data, table_sha = load_table(args.table)
    structure = support_structure(data)
    marginals = exact_partial_trace(data)
    first = next(iter(data))
    removed = dict(data)
    removed.pop(first)
    flipped = dict(data)
    a, b = flipped[first]
    flipped[first] = (-a, -b)
    controls = {"remove_one": must_reject(removed, "normalization:"),
                "flip_one_sign": must_reject(flipped, "marginal ")}
    result = {"table": str(args.table), "table_sha256": table_sha,
              "support": len(data), "support_structure": structure,
              "exact_normalization_and_six_marginals": marginals,
              "mutation_controls": controls,
              "scope": "Real Q(sqrt(2)); one separate in-harness checker and parser, no third checker or external review."}
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
