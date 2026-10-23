#!/usr/bin/env python3
"""Short form of a 5 x 5 array of 5 x 5 circulants (Z_5 semiregular model) <-> strict SW file.

Usage:
  python3 -B code/expand_circulant_array.py extract STRICT.sw OUT.txt   # write the 25 first rows
  python3 -B code/expand_circulant_array.py expand IN.txt OUT.sw         # rebuild the strict file
Short form: 5 lines (block rows a = 0..4), each with 5 words (block columns b = 0..4); word f_ab is the first row
of block (a,b) over {+,-,0}, i.e. f_ab[x] = W[5a][5b+x].  Expansion: W[5a+u][5b+v] = f_ab[(v - u) mod 5].
'extract' refuses (exit 1) if the matrix is not of this form.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402

CH = {1: "+", -1: "-", 0: "0"}
VAL = {"+": 1, "-": -1, "0": 0}


def main():
    mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    if mode == "extract":
        n, w, W = C.read_strict(src)
        assert n == 25
        for a in range(5):
            for b in range(5):
                for u in range(5):
                    for v in range(5):
                        if W[5 * a + u][5 * b + v] != W[5 * a][5 * b + (v - u) % 5]:
                            print("not a circulant array")
                            sys.exit(1)
        lines = [" ".join("".join(CH[W[5 * a][5 * b + x]] for x in range(5)) for b in range(5)) for a in range(5)]
        with open(dst, "x") as f:
            f.write("\n".join(lines) + "\n")
        print("\n".join(lines))
    elif mode == "expand":
        rows = [ln.split() for ln in open(src).read().strip().split("\n")]
        assert len(rows) == 5 and all(len(r) == 5 for r in rows)
        W = [[0] * 25 for _ in range(25)]
        for a in range(5):
            for b in range(5):
                f = [VAL[c] for c in rows[a][b]]
                assert len(f) == 5
                for u in range(5):
                    for v in range(5):
                        W[5 * a + u][5 * b + v] = f[(v - u) % 5]
        with open(dst, "x") as fh:
            fh.write(C.to_strict(W, 25, 16))
        print("wrote", dst)
    else:
        raise ValueError(mode)


if __name__ == "__main__":
    main()
