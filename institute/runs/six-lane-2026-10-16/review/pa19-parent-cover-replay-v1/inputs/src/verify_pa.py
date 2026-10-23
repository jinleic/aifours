#!/usr/bin/env python3
"""Verifier 1 (row-pair definition) for packing arrays PA(N,k,q).

Strict format: exactly N non-empty lines, each with exactly k integers in [0,q)
separated by spaces/tabs; nothing else except a final newline.
Valid iff every pair of distinct rows agrees in at most one column.
Usage: verify_pa.py FILE N k q   -> prints JSON, exit 0 iff valid.
"""
import hashlib
import json
import sys


def check(path, N, k, q):
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    res = {"file": path, "sha256": sha, "N": N, "k": k, "q": q, "valid": False}
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        res["error"] = "non-ascii bytes"
        return res
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if len(lines) != N:
        res["error"] = "expected %d rows, got %d" % (N, len(lines))
        return res
    rows = []
    for i, line in enumerate(lines):
        toks = line.replace("\t", " ").split(" ")
        toks = [t for t in toks if t != ""]
        if len(toks) != k:
            res["error"] = "row %d has %d entries" % (i, len(toks))
            return res
        row = []
        for t in toks:
            if not t.isdigit():
                res["error"] = "row %d bad token %r" % (i, t)
                return res
            v = int(t)
            if not 0 <= v < q:
                res["error"] = "row %d symbol %d out of range" % (i, v)
                return res
            row.append(v)
        rows.append(row)
    worst = 0
    zero_pairs = 0
    for a in range(N):
        for b in range(a + 1, N):
            agree = sum(1 for c in range(k) if rows[a][c] == rows[b][c])
            if agree == 0:
                zero_pairs += 1
            if agree > worst:
                worst = agree
            if agree > 1:
                res["error"] = "rows %d,%d agree in %d columns" % (a, b, agree)
                res["max_agreement"] = agree
                return res
    counts = [sorted([sum(1 for r in rows if r[c] == s) for s in range(q)], reverse=True)
              for c in range(k)]
    res.update({"valid": True, "max_agreement": worst, "zero_agreement_pairs": zero_pairs,
                "column_profiles": counts})
    return res


if __name__ == "__main__":
    path, N, k, q = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    r = check(path, N, k, q)
    print(json.dumps(r))
    sys.exit(0 if r["valid"] else 1)
