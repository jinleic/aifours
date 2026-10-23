#!/usr/bin/env python3
"""Convert a (Z_G, K; 1) difference matrix (dm-raw) into a CFR(K-1, G) in cfr-raw-v1 (lane cfr33).

Usage: dm_to_cfr.py DMFILE K G OUT [ROWS]
Construction (README E2): e_i = d_i - d_0 (i = 1..K-1); e_1 is a bijection (columns -> Z_G) when D is a DM;
position maps p_i = e_i o e_1^{-1}; output row i = p_i^{-1} as a sequence (row[c] = symbol at column c).
Optional ROWS = number of leading CFR rows to write (default K-1). No validity is assumed: the output is
checked separately by cfr_check_events.py and cfr_check_posdiff.py. Writes OUT with mode 'x'.
"""
import hashlib, sys


def main():
    path, K, G, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    keep = int(sys.argv[5]) if len(sys.argv) > 5 else K - 1
    lines = open(path).read().split("\n")[:K]
    D = [[int(x) for x in ln.split(" ")] for ln in lines]
    E = [[(D[i][t] - D[0][t]) % G for t in range(G)] for i in range(1, K)]
    inv1 = [None] * G
    for t, s in enumerate(E[0]):
        assert inv1[s] is None, "e_1 not a bijection"
        inv1[s] = t
    rows = []
    for e in E[:keep]:
        p = [e[inv1[s]] for s in range(G)]          # position of symbol s
        row = [None] * G
        for s, c in enumerate(p):
            assert row[c] is None, "p_i not a bijection"
            row[c] = s
        rows.append(row)
    text = "".join(" ".join(str(x) for x in r) + "\n" for r in rows)
    with open(out, "x") as fh:
        fh.write(text)
    print("wrote %s rows %d n %d sha256 %s" % (out, len(rows), G, hashlib.sha256(text.encode()).hexdigest()))


if __name__ == "__main__":
    main()
