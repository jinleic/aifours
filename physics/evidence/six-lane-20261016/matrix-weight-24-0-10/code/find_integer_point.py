"""Find an integer lattice point of the genus-2 family near a strictly feasible real point, then test it
exactly: integrality, nonnegativity, the 84 rank-1 block functionals, and exact PSD (LDL^T over Q) of every AMH
block. Writes the candidate pair-count table (one value per allowed S3 orbit) to evidence/candidate.json.
"""
import json
import pickle
import sys
from fractions import Fraction

import sympy

from g2_polytope import load_space


def psd_exact(M):
    """Exact PSD test of a symmetric rational matrix by LDL^T with diagonal pivoting."""
    A = [row[:] for row in M]
    alive = list(range(len(A)))
    while alive:
        piv = max(alive, key=lambda i: A[i][i])
        d = A[piv][piv]
        if d < 0:
            return False
        if d == 0:
            return all(A[i][j] == 0 for i in alive for j in alive)
        alive.remove(piv)
        for i in alive:
            if A[i][piv] == 0:
                continue
            f = A[i][piv] / d
            for j in alive:
                A[i][j] -= f * A[piv][j]
    return True


def block_value(b, s):
    Bs = b["B"]
    m = len(b["idx"])
    return [[Bs[0][r][c] + sum(s[f] * Bs[f + 1][r][c] for f in range(len(s))) for c in range(m)] for r in range(m)]


def nearest_lattice_point(ref, s0, B):
    nf = len(s0)
    BT = sympy.Matrix(B).T  # columns = basis vectors
    rhs = sympy.Matrix([sympy.Rational(str(Fraction(r))) - s0[f] for f, r in enumerate(ref)])
    yexact = BT.LUsolve(rhs)
    yr = [int(sympy.floor(v + sympy.Rational(1, 2))) for v in yexact]
    return [s0[f] + sum(yr[j] * B[j][f] for j in range(nf)) for f in range(nf)]


def check_point(s, keys, free, c, V, st, blk):
    nf = len(free)
    x = [c[i] + sum(V[i][f] * s[f] for f in range(nf)) for i in range(len(keys))]
    integral = all(v.denominator == 1 for v in x)
    sF = [Fraction(v) for v in s]
    rank1_ok = all(Fraction(r["const"]) + sum(Fraction(q) * sF[f] for f, q in enumerate(r["coef"])) >= 0
                   for r in st["rank1"])
    bad = [(b["a"], b["k"]) for b in blk["blocks"] if b["nonzero"] and not psd_exact(block_value(b, sF))]
    return x, integral, rank1_ok, bad


if __name__ == "__main__":
    ref = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "../evidence/lp_rank1_center.json"))["s"]
    keys, piv, free, c, V = load_space()
    sub = "--subspace" in sys.argv
    L = json.load(open("../evidence/int_lattice_subspace.json" if sub else "../evidence/int_lattice.json"))
    s0 = [int(v) for v in L["s0"]]
    B = [[int(v) for v in row] for row in L["B"]]
    s = nearest_lattice_point(ref, s0, B)
    print("lattice point s:", s)
    print("offset from ref:", [round(float(s[f] - Fraction(ref[f])), 1) for f in range(len(s))])
    st = json.load(open("../evidence/block_structure.json"))
    blk = pickle.load(open("../evidence/amh_blocks24_exact.pkl", "rb"))
    x, integral, rank1_ok, bad = check_point(s, keys, free, c, V, st, blk)
    print("integral:", integral, "; min count:", min(x), "; negative counts:", sum(1 for v in x if v < 0))
    print("all 84 rank-1 block functionals >= 0:", rank1_ok)
    print("exact PSD failures:", bad)
    ok = integral and min(x) >= 0 and rank1_ok and not bad
    json.dump({"s": [str(v) for v in s], "counts": {json.dumps(keys[i]): str(x[i]) for i in range(len(keys))},
               "all_checks_passed": ok, "subspace_divisibility": sub},
              open("../evidence/candidate_subspace.json" if sub else "../evidence/candidate.json", "w"), indent=0)
    print("CANDIDATE OK" if ok else "CANDIDATE FAILED")
