#!/usr/bin/env python3
"""Checker B for circular Florentine rectangles (separately written from checker A), format cfr-raw-v1.

Usage: cfr_check_posdiff.py FILE R N
Position-difference criterion: with pos_i[s] = column of symbol s in row i, the array is a CFR(R,N) iff for
every pair of rows i < j the map s -> (pos_i[s] - pos_j[s]) mod N is a permutation of Z_N.
(If pos_i[b]-pos_i[a] = pos_j[b]-pos_j[a] = m for a != b then the difference map takes the same value at a
and b, and conversely; m is then automatically nonzero because rows are permutations.)
Exit 0 and print 'CHECK_B PASS' only on success; otherwise 'CHECK_B FAIL: <reason>' and exit 1.
"""
import hashlib
import sys

DIGITS = "0123456789"


def bad(msg):
    sys.stdout.write("CHECK_B FAIL: %s\n" % msg)
    raise SystemExit(1)


def read_rows(raw, R, N):
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        bad("not ASCII")
    if text == "" or text[-1] != "\n":
        bad("missing final LF")
    body = text[:-1]
    lines = body.split("\n")
    if len(lines) != R:
        bad("row count %d != %d" % (len(lines), R))
    out = []
    for k in range(R):
        line = lines[k]
        fields = line.split(" ")
        if len(fields) != N:
            bad("row %d has %d fields, need %d" % (k, len(fields), N))
        vals = []
        for f in fields:
            if f == "" or any(ch not in DIGITS for ch in f):
                bad("row %d: field %r is not a decimal numeral" % (k, f))
            if len(f) > 1 and f[0] == "0":
                bad("row %d: field %r has a leading zero" % (k, f))
            vals.append(int(f))
        out.append(vals)
    return out


def main():
    if len(sys.argv) != 4:
        bad("usage: cfr_check_posdiff.py FILE R N")
    fname = sys.argv[1]
    R = int(sys.argv[2])
    N = int(sys.argv[3])
    with open(fname, "rb") as fh:
        raw = fh.read()
    sys.stdout.write("sha256 %s size %d\n" % (hashlib.sha256(raw).hexdigest(), len(raw)))
    rows = read_rows(raw, R, N)
    pos = []
    for k, row in enumerate(rows):
        p = [-1] * N
        for col, s in enumerate(row):
            if s >= N:
                bad("row %d: symbol %d out of range" % (k, s))
            if p[s] != -1:
                bad("row %d: symbol %d repeated" % (k, s))
            p[s] = col
        pos.append(p)
    pairs = 0
    for i in range(R):
        for j in range(i + 1, R):
            hit = [False] * N
            for s in range(N):
                d = (pos[i][s] - pos[j][s]) % N
                if hit[d]:
                    bad("rows %d,%d: difference map repeats value %d (not a permutation)" % (i, j, d))
                hit[d] = True
            pairs += 1
    sys.stdout.write("R %d N %d row pairs checked %d; implied distinct events R*N*(N-1) = %d\n"
                     % (R, N, pairs, R * N * (N - 1)))
    sys.stdout.write("CHECK_B PASS\n")


if __name__ == "__main__":
    main()
