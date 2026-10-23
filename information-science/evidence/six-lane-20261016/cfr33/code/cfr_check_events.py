#!/usr/bin/env python3
"""Checker A for circular Florentine rectangles, strict raw format cfr-raw-v1 (lane cfr33).

Usage: cfr_check_events.py FILE R N
Definition-first: for every row and every start column i and distance m in 1..N-1 form the direct event
(row[i], row[(i+m) % N], m). The file is a CFR(R,N) iff it has exactly R rows that are permutations of
0..N-1 and all R*N*(N-1) events are pairwise distinct.
Exit 0 and print 'CHECK_A PASS' only on success; otherwise print 'CHECK_A FAIL: <reason>' and exit 1.
Standard library only; no knowledge of how the file was produced.
"""
import hashlib
import re
import sys

TOKEN = re.compile(rb"(0|[1-9][0-9]*)\Z")


def fail(msg):
    print("CHECK_A FAIL: " + msg)
    sys.exit(1)


def parse_strict(data, r, n):
    if not data.endswith(b"\n"):
        fail("file does not end with LF")
    for byte in data:
        if not (byte == 10 or byte == 32 or 48 <= byte <= 57):
            fail("byte %r outside [0-9 space LF]" % bytes([byte]))
    lines = data[:-1].split(b"\n")
    if len(lines) != r:
        fail("expected %d rows, found %d" % (r, len(lines)))
    rows = []
    for li, line in enumerate(lines):
        toks = line.split(b" ")
        if len(toks) != n:
            fail("row %d: expected %d tokens, found %d (single spaces only)" % (li, n, len(toks)))
        row = []
        for tok in toks:
            if not TOKEN.match(tok):
                fail("row %d: non-canonical token %r" % (li, tok))
            row.append(int(tok))
        rows.append(row)
    return rows


def main():
    if len(sys.argv) != 4:
        fail("usage: cfr_check_events.py FILE R N")
    path, r, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if r < 1 or n < 2:
        fail("bad R/N")
    data = open(path, "rb").read()
    print("file sha256 " + hashlib.sha256(data).hexdigest() + " bytes " + str(len(data)))
    rows = parse_strict(data, r, n)
    for li, row in enumerate(rows):
        if sorted(row) != list(range(n)):
            fail("row %d is not a permutation of 0..%d" % (li, n - 1))
    seen = {}
    count = 0
    for li, row in enumerate(rows):
        for i in range(n):
            for m in range(1, n):
                ev = (row[i], row[(i + m) % n], m)
                if ev in seen:
                    fail("event (a=%d, b=%d, m=%d) occurs in row %d and row %d" % (ev[0], ev[1], m, seen[ev], li))
                seen[ev] = li
                count += 1
    expected = r * n * (n - 1)
    if count != expected or len(seen) != expected:
        fail("event count %d / distinct %d, expected %d" % (count, len(seen), expected))
    print("rows %d n %d events %d distinct %d expected r*n*(n-1) = %d" % (r, n, count, len(seen), expected))
    print("CHECK_A PASS")


if __name__ == "__main__":
    main()
