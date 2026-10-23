#!/usr/bin/env python3
"""Calibration fixtures for involution_cnf_c21v1.py --calibration-plant (lane cfr33/cfr21, C21 involution SAT v1):
convert a CFR to a difference matrix and bring a difference matrix into the encoder's zero gauge.

Usage
  involution_fixture_c21v1.py cfr-to-dm CFR_RAW R N OUT_DMRAW
  involution_fixture_c21v1.py normalize-dm DM_RAW K N OUT_DMRAW

Inputs are strict: ASCII, LF-terminated lines, fields separated by single spaces, canonical decimals in 0..N-1.
cfr-to-dm     CFR_RAW (cfr-raw-v1) has R lines; entry c of line i is the symbol at circular position c, and each
              line is a permutation of 0..N-1. With P_i(s) = position of symbol s in line i, the (R+1) x N array
              with row 0 = 0 and row i+1 = P_i (column = symbol s) is a (Z_N, R+1; 1) difference matrix iff the CFR
              is valid: line i contains the event (a, b, delta) iff P_i(b) - P_i(a) = delta, so lines i != j share
              an event iff P_i - P_j is not injective (dm_to_cfr_c21v1.py is the inverse up to symbol renaming).
normalize-dm  DM_RAW (dm-raw) has K lines.
Both require the difference-matrix definition on every row pair, then normalize: subtract row 0 columnwise,
re-index columns by their row-1 entry t, and subtract A[r][0] from each row r. They re-check the definition and
the gauge (row 0 = 0, row 1 = 0..N-1, column 0 = 0) and write OUT_DMRAW (dm-raw) with mode 'x', printing the
input and output SHA-256. Any failure prints 'FIXTURE REJECT: ...', exits 1 and writes nothing.
The arbitrary row translations make this valid for --no-sym plants only; planted action controls must use
matrices that are already in gauge form and invariant (the encoder validates the gauge, not invariance).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

TOKEN = re.compile(r"(0|[1-9][0-9]*)\Z")


class Reject(Exception):
    pass


def read_rows(path, rows, n):
    raw = Path(path).read_bytes()
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        raise Reject("%s is not ASCII" % path)
    if not text.endswith("\n") or "\r" in text:
        raise Reject("%s must consist of LF-terminated lines" % path)
    lines = text[:-1].split("\n")
    if len(lines) != rows:
        raise Reject("%s has %d lines, expected %d" % (path, len(lines), rows))
    matrix = []
    for i, line in enumerate(lines):
        toks = line.split(" ")
        if len(toks) != n or not all(TOKEN.match(tok) for tok in toks):
            raise Reject("%s line %d is not %d single-space-separated decimals" % (path, i, n))
        row = [int(tok) for tok in toks]
        if max(row) >= n:
            raise Reject("%s line %d has an entry >= %d" % (path, i, n))
        matrix.append(row)
    return raw, matrix


def check_dm(matrix, n, what):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if sorted((matrix[i][c] - matrix[j][c]) % n for c in range(n)) != list(range(n)):
                raise Reject("%s: rows %d and %d differences are not a permutation of Z_%d" % (what, i, j, n))


def normalize(matrix, n):
    shifted = [[(row[c] - matrix[0][c]) % n for c in range(n)] for row in matrix]
    column_of = [None] * n
    for c in range(n):
        column_of[shifted[1][c]] = c
    reindexed = [[row[column_of[t]] for t in range(n)] for row in shifted]
    return [[(row[t] - row[0]) % n for t in range(n)] for row in reindexed]


def main():
    if len(sys.argv) != 6 or sys.argv[1] not in ("cfr-to-dm", "normalize-dm"):
        sys.exit(__doc__)
    mode, source, rows_text, n_text, out = sys.argv[1:]
    try:
        if not (TOKEN.match(rows_text) and TOKEN.match(n_text)):
            raise Reject("R/K and N must be canonical decimals")
        rows, n = int(rows_text), int(n_text)
        if n < 3 or rows < 2:
            raise Reject("need N >= 3 and at least 2 input lines")
        raw, matrix = read_rows(source, rows, n)
        if mode == "cfr-to-dm":
            dm = [[0] * n]
            for i, line in enumerate(matrix):
                if sorted(line) != list(range(n)):
                    raise Reject("CFR line %d is not a permutation of 0..%d" % (i, n - 1))
                position = [0] * n
                for c, symbol in enumerate(line):
                    position[symbol] = c
                dm.append(position)
        else:
            dm = matrix
        check_dm(dm, n, "input")
        gauge = normalize(dm, n)
        if any(gauge[0]) or gauge[1] != list(range(n)) or any(row[0] for row in gauge):
            raise Reject("internal error: normalization missed the gauge")
        check_dm(gauge, n, "normalized")
        text = "".join(" ".join(map(str, row)) + "\n" for row in gauge).encode("ascii")
        with open(out, "xb") as fh:
            fh.write(text)
    except (Reject, OSError) as exc:
        print("FIXTURE REJECT: %s" % exc)
        sys.exit(1)
    print(json.dumps({"mode": mode, "input": source, "input_sha256": hashlib.sha256(raw).hexdigest(),
                      "output": out, "output_sha256": hashlib.sha256(text).hexdigest(), "k": len(gauge), "n": n,
                      "gauge": "row 0 = 0, row 1 = 0..N-1, column 0 = 0"}, sort_keys=True))


if __name__ == "__main__":
    main()
