#!/usr/bin/env python3
"""Rebuild Sage's DM_55_7_1 (a (Z_55, 7; 1)-DM, Handbook III.3.72 per its docstring) from the pinned source file without
Sage (sub-lane cfr21, worker InfoCFR27Lift). Usage: sage_dm55_expand_c21v1.py SAGE_DATABASE_PY OUT.dmraw
Extracts the literal M of def DM_55_7_1 with ast.literal_eval and applies the Sage expansion verbatim:
Mb = [[0]*7] + [cyclic_shift(R, c) + [0] for R in zip(*M) for c in range(6)], cyclic_shift(l, i) = l[-i:] + l[:-i].
Mb is a list of 55 columns of 7 entries; OUT has 7 rows of 55 entries (dm-raw format), written with mode 'x'.
"""
import ast, hashlib, re, sys


def main():
    src = open(sys.argv[1]).read()
    body = src[src.index("def DM_55_7_1"):]
    body = body[:body.index("return G, Mb")]
    m = re.search(r"M = (\[\s*\[.*?\]\s*\])\s*\n\s*Mb = \[\[0,0,0,0,0,0,0\]\]", body, re.S)
    if not m:
        raise SystemExit("literal M not found")
    M = ast.literal_eval(m.group(1))
    if len(M) != 6 or any(len(r) != 9 for r in M):
        raise SystemExit("unexpected shape")
    cyclic_shift = lambda l, i: l[-i:] + l[:-i]
    Mb = [[0] * 7]
    for R in zip(*M):
        R = list(R)
        for c in range(6):
            Mb.append(cyclic_shift(R, c) + [0])
    if len(Mb) != 55:
        raise SystemExit("expected 55 columns")
    rows = [[col[x] % 55 for col in Mb] for x in range(7)]
    text = "".join(" ".join(map(str, r)) + "\n" for r in rows)
    with open(sys.argv[2], "x") as fh:
        fh.write(text)
    print("literal sha256 %s dmraw sha256 %s" % (hashlib.sha256(m.group(1).encode()).hexdigest(), hashlib.sha256(text.encode()).hexdigest()))


if __name__ == "__main__":
    main()
