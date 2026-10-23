#!/usr/bin/env python3
"""expand_base_blocks.py -- rebuild the pinned witness from its six signed base blocks (explanation; stdlib only).

Points: rows 0..24 are Z_25, row 25 is inf (fixed).  Column 25*o + t (o = 0..4, t = 0..24) is the base block B_o
translated by t (x -> x + t mod 25, inf fixed, signs carried along); columns 125 + c (c = 0..4) are S + c.
Also prints, for every nonzero difference d in Z_25 and for inf, the multiset of sign products of the blocks
through the pair {0, d} (resp. {inf, 0}), which must be {+1, +1, -1, -1}.
Usage: expand_base_blocks.py OUT.brd      (OUT created exclusively)
"""
import hashlib
import sys

INF = 25
BASE = [
    [(0, -1), (13, -1), (16, -1), (18, -1), (24, +1)],
    [(3, -1), (8, +1), (16, +1), (22, -1), (24, -1)],
    [(2, +1), (7, -1), (10, +1), (11, +1), (17, +1)],
    [(1, +1), (10, -1), (12, +1), (13, +1), (14, -1)],
    [(3, -1), (6, -1), (13, +1), (24, +1), (INF, -1)],
]
SHORT = [(2, +1), (7, +1), (12, +1), (17, +1), (22, +1)]


def shift(block, t):
    return [((x + t) % 25 if x != INF else INF, s) for x, s in block]


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    cols = [shift(B, t) for B in BASE for t in range(25)] + [shift(SHORT, c) for c in range(5)]
    W = [[0] * 130 for _ in range(26)]
    for j, blk in enumerate(cols):
        for x, s in blk:
            W[x][j] = s
    text = "BRD 26 130 25 5 4\n" + "".join(" ".join(map(str, r)) + "\n" for r in W)
    with open(argv[1], "x") as f:
        f.write(text)
    print("sha256", hashlib.sha256(text.encode()).hexdigest())
    for d in list(range(1, 25)) + ["inf"]:
        a, b = (0, d) if d != "inf" else (INF, 0)
        prods = sorted(W[a][j] * W[b][j] for j in range(130) if W[a][j] and W[b][j])
        print(f"pair {{{a},{b}}}: products {prods}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
