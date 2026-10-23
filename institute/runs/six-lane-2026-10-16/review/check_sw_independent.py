#!/usr/bin/env python3
"""Strict definition-first symmetric-weighing-matrix checker; no lane imports."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


class WitnessError(ValueError):
    def __init__(self, kind, detail):
        super().__init__(f"{kind}: {detail}")
        self.kind = kind


def verify(data, expected_n, expected_w, expected_sha):
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected_sha:
        raise WitnessError("DIGEST", f"expected {expected_sha}, got {digest}")
    if not data.endswith(b"\n") or b"\r" in data:
        raise WitnessError("FORMAT", "LF lines and final LF required")
    try:
        lines = data.decode("ascii").splitlines()
    except UnicodeDecodeError as e:
        raise WitnessError("FORMAT", "non-ASCII input") from e
    if not lines:
        raise WitnessError("FORMAT", "empty file")
    m = re.fullmatch(r"SW ([1-9][0-9]*) ([1-9][0-9]*)", lines[0])
    if not m:
        raise WitnessError("HEADER", "expected SW n w")
    n, w = int(m[1]), int(m[2])
    if (n, w) != (expected_n, expected_w) or w > n:
        raise WitnessError("HEADER", f"expected ({expected_n},{expected_w}), got ({n},{w})")
    if len(lines) != n + 1:
        raise WitnessError("FORMAT", f"expected {n} matrix rows, got {len(lines)-1}")
    W = []
    for i, line in enumerate(lines[1:]):
        tokens = line.split(" ")
        if len(tokens) != n or any(t == "" or any(c.isspace() for c in t) for t in tokens):
            raise WitnessError("FORMAT", f"row {i} must have {n} single-space-separated entries")
        for j, t in enumerate(tokens):
            if t not in {"-1", "0", "1"}:
                raise WitnessError("ENTRIES", f"({i},{j}) is not ternary: {t!r}")
        W.append([int(t) for t in tokens])
    for i in range(n):
        for j in range(i + 1, n):
            if W[i][j] != W[j][i]:
                raise WitnessError("SYMMETRY", f"({i},{j})={W[i][j]}, ({j},{i})={W[j][i]}")
    weights = [sum(x != 0 for x in row) for row in W]
    if any(v != w for v in weights):
        raise WitnessError("WEIGHT", repr([(i, v) for i, v in enumerate(weights) if v != w]))
    products = 0
    for i in range(n):
        for j in range(i, n):
            value = sum(a * b for a, b in zip(W[i], W[j]))
            target = w if i == j else 0
            if value != target:
                raise WitnessError("ORTHO", f"row pair ({i},{j}) has product {value}, expected {target}")
            products += 1
    trace = sum(W[i][i] for i in range(n))
    return {"verdict": "VALID", "n": n, "w": w, "sha256": digest, "bytes": len(data),
            "entries": n * n, "row_weights": weights, "checked_gram_upper_triangle": products,
            "off_diagonal_row_pairs": n * (n - 1) // 2, "trace": trace,
            "diagonal_counts": {str(a): sum(W[i][i] == a for i in range(n)) for a in (-1, 0, 1)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("w", type=int)
    ap.add_argument("file", type=Path)
    ap.add_argument("sha256")
    ap.add_argument("--output", type=Path)
    a = ap.parse_args()
    try:
        result = verify(a.file.read_bytes(), a.n, a.w, a.sha256)
    except WitnessError as e:
        print("INVALID " + str(e), file=sys.stderr)
        return 1
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if a.output:
        with a.output.open("x") as f:
            json.dump(result, f, indent=1)
            f.write("\n")
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
