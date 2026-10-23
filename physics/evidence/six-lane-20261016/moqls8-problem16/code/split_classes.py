"""PLANNING ONLY (never used to skip, order-prune or close a leaf): necessary-condition classification of split leaves
by the support patterns they fix, to project run times. K5 depth-2 child of root S (supp Ψ1(2,0)) with T = supp Ψ1(3,0):
plausible iff T ≠ ∅, |T| ≤ 3 (W8), |T ∩ {1,2,3}| ≠ 1 (Lemma 2 vs Ψ1(1,0) = {1,2,3}), |T ∩ S| ≠ 1 (Lemma 2), T ∌ a if
S = {a}, and ROWLEX v(T) ≥ v(S) (k = 1 most significant). K4 root S = supp Q1(2,0): plausible iff 2 ∉ S, S ≠ ∅,
|S| ≤ 3, |S ∩ {2,3,4}| ≠ 1.
python -B split_classes.py k5d2 c016,c032,c048,c064,c080,c096 | python -B split_classes.py k4root
"""
from __future__ import annotations

import json
import sys


def bits(b):
    return {k + 1 for k in range(7) if (b >> k) & 1}


def vec(S):
    return tuple(1 if k in S else 0 for k in range(1, 8))


def k5d2(S, T):
    return (bool(T) and len(T) <= 3 and len(T & {1, 2, 3}) != 1 and len(T & S) != 1
            and not (len(S) == 1 and S <= T) and vec(T) >= vec(S))


def k4root(S):
    return 2 not in S and bool(S) and len(S) <= 3 and len(S & {2, 3, 4}) != 1


if __name__ == "__main__":
    if sys.argv[1] == "k5d2":
        out = {}
        for rid in sys.argv[2].split(","):
            S = bits(int(rid[1:]))
            out[rid] = ["%s.L2.%03d" % (rid, b) for b in range(128) if k5d2(S, bits(b))]
        print(json.dumps({k: len(v) for k, v in out.items()}))
        print(json.dumps(out))
    else:
        print(json.dumps(["c%03d" % b for b in range(128) if k4root(bits(b))]))
