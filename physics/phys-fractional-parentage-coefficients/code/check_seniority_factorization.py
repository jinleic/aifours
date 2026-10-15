"""Exact check of Theorem A (seniority factorization of one-body CFPs, any integer spin f)
and of the spin-1 closed form of Bao & Li (2005).

For every parent |N v alpha L> = (P+)^n h_(v alpha L) (h harmonic, N = v + 2n) and every
daughter |N-1 v' alpha' L'> built the same way, the CFP is computed directly from the
polynomials and compared with
    v' = v-1 : cfp^2 = v (N+v+D-2) / (N (2v+D-2)) * r(v alpha L; v-1 alpha' L')^2,
    v' = v+1 : cfp^2 = (N-v)(v+D-2) / (N (2v+D-2)) * rt(v alpha L; v+1 alpha' L')^2,
with r = cfp at N = v and
    rt^2 = dim_v (2L'+1) / (dim_(v+1) (2L+1)) * r(v+1 alpha' L'; v alpha L)^2,
and with N-independent signs.  dim_v = dimension of the SO(D) irrep (v).
Run: $PY code/check_seniority_factorization.py
"""
import sys
from math import comb

from flint import fmpq

from fpc_core import SpinBosons


def dim_so(D, v):
    return comb(v + D - 1, D - 1) - (comb(v + D - 3, D - 1) if v >= 2 else 0)


def gs(B, vecs):
    out = []
    for v in vecs:
        w = dict(v)
        for u in out:
            c = B.inner(u, w) / B.norm2(u)
            for a, x in u.items():
                y = w.get(a, fmpq(0)) - c * x
                if y == 0:
                    w.pop(a, None)
                else:
                    w[a] = y
        assert w
        out.append(w)
    return out


def harmonic_states(B, vmax):
    """{(v, L): [orthogonal harmonic highest-weight polynomials]} for v <= vmax."""
    H = {}
    for v in range(0, vmax + 1):
        for L in range(0, B.f * v + 1):
            basis = B.hw_harmonic_basis(v, L)
            if basis:
                H[(v, L)] = gs(B, basis)
    return H


def run(f, Nmax):
    B = SpinBosons(f)
    D = B.D
    H = harmonic_states(B, Nmax)
    # states at each N: (v, L, alpha) -> polynomial
    states = {}
    for (v, L), hs in H.items():
        for alpha, h in enumerate(hs):
            p = h
            N = v
            while N <= Nmax:
                states[(N, v, L, alpha)] = p
                p = B.pair_cre(p)
                N += 2
    r = {}   # (v,L,alpha; L',alpha') -> (sq, sign) at N = v
    for (N, v, L, al), p in states.items():
        if N == v and v >= 1:
            for (N2, v2, L2, al2), q in states.items():
                if N2 == N - 1 and v2 == v - 1 and abs(L - L2) <= f:
                    r[(v, L, al, L2, al2)] = B.cfp_sq_sign(p, N, L, q, L2)
    nchk = 0
    for (N, v, L, al), p in states.items():
        if N < 1:
            continue
        tot = fmpq(0)
        for (N2, v2, L2, al2), q in states.items():
            if N2 != N - 1 or abs(L - L2) > f:
                continue
            sq, sg = B.cfp_sq_sign(p, N, L, q, L2)
            tot += sq
            if v2 == v - 1:
                r2, rs = r[(v, L, al, L2, al2)]
                pred = fmpq(v * (N + v + D - 2), N * (2 * v + D - 2)) * r2
                assert sq == pred and (sg == rs or sq == 0), (f, N, v, L, al, v2, L2, al2)
            elif v2 == v + 1:
                r2, rs = r[(v + 1, L2, al2, L, al)]
                rt2 = fmpq(dim_so(D, v) * (2 * L2 + 1), dim_so(D, v + 1) * (2 * L + 1)) * r2
                pred = fmpq((N - v) * (v + D - 2), N * (2 * v + D - 2)) * rt2
                assert sq == pred, (f, N, v, L, al, v2, L2, al2, sq, pred)
                # sign rule (derived in RESULTS.md, Theorem A):
                # cfp(N v L -> N-1 v+1 L') = (-1)^(L+L') sign r(v+1 L'; v L) * |cfp|
                if sq != 0:
                    rel = sg * rs
                    assert rel == (-1) ** (L + L2), ("sign rule", f, N, v, L, L2, rel)
                    r.setdefault(("rel", v, L, al, L2, al2), rel)
            else:
                assert sq == 0, (f, N, v, L, v2, L2)
            nchk += 1
        assert tot == 1, (f, N, v, L, al, tot)
    nrel = sum(1 for k in r if k[0] == "rel")
    return nchk, len(states), nrel


def spin1_bao_li(Nmax):
    """Bao-Li: theta^N_S = a [chi theta^(N-1)_(S+1)] + b [chi theta^(N-1)_(S-1)]."""
    B = SpinBosons(1)
    nchk = 0
    for N in range(1, Nmax + 1):
        for S in range(N % 2, N + 1, 2):
            n = (N - S) // 2
            parent = B.pair_cre_pow({(0, 0, S): fmpq(1)}, n)
            for Sp in (S - 1, S + 1):
                if Sp < 0 or Sp > N - 1:
                    continue
                np_ = (N - 1 - Sp) // 2
                daughter = B.pair_cre_pow({(0, 0, Sp): fmpq(1)}, np_)
                sq, sg = B.cfp_sq_sign(parent, N, S, daughter, Sp)
                if Sp == S + 1:
                    ref = fmpq((N - S) * (S + 1), N * (2 * S + 1))
                else:
                    ref = fmpq((N + S + 1) * S, N * (2 * S + 1))
                assert sq == ref, (N, S, Sp, sq, ref)
                # with P+ = sum_m (-1)^m a+_m a+_-m the S-1 branch is +, the S+1 branch is -
                assert sg == (1 if Sp == S - 1 else -1), (N, S, Sp, sg)
                nchk += 1
    return nchk


if __name__ == "__main__":
    n1 = spin1_bao_li(int(sys.argv[1]) if len(sys.argv) > 1 else 40)
    print(f"spin-1 Bao-Li closed form: {n1} CFPs equal exactly (N <= {sys.argv[1] if len(sys.argv) > 1 else 40})")
    for f, Nmax in ((1, 16), (2, 12), (3, 9), (4, 7)):
        nchk, nst, nrel = run(f, Nmax)
        print(f"f={f}: Theorem A verified exactly for all {nst} seniority states with N <= {Nmax}: "
              f"{nchk} CFPs, completeness sum = 1; sign rule (-1)^(L+L') holds for {nrel} v+1 couplings")
