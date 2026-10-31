#!/usr/bin/env python3
"""reviewer-f146-controls-v1.py

Independently authored exact controls for review wave
f146-fourier-product-prime-field-obstruction (same-harness reviewer).

No author code was read, imported or executed. Everything here is exact:
elements of Z[zeta_L] are integer polynomials in zeta_L reduced modulo the
cyclotomic polynomial Phi_L, which is computed from scratch by exact division
of x^L-1 by the product of the lower Phi_d.

Objects under test (reviewer's own reconstruction of the author's formula):
  QLS cell (r,c) of order N=2p:  psi_(r,c)(t) = zeta_{2p}^{r t} K_{t,c} / sqrt(2p)
  with K an N x N Butson matrix given as an exponent matrix k[t][c] mod q,
  K_{t,c} = zeta_q^{k[t][c]}.  Inner products are taken in Z[zeta_L], L=lcm(2p,q).

Controls:
  A. machinery sanity: Phi_n table, zero tests (pos/neg), Hadamard checker
     (pos/neg), transversal search on cyclic Latin squares (Z3:3, Z5:15,
     Z7:133 transversals; Z4, Z6: 0).
  B. algebraic core: dimension over F of the F-linear relations among the
     p-th roots of unity for F = Q, Q(i), Q(zeta_3), Q(zeta_p) at p=3,5; and the
     explicit reducible-case relation w_u = zeta_p^u satisfying both linear
     conditions without vanishing.
  C. positive controls (Phi_p irreducible over F): p=3 with Paley BH(6,4) and
     p=5 with Paley BH(10,4), F=Q(i): zero same-parity distinct-column
     pairwise-orthogonal triples, zero transversals, pair lemma
     (orthogonal <=> h_d = -h_c) exact, sweep over all 720 row permutations
     (p=3) / seeded random row permutations (p=5).
  D. negative-hypothesis controls (Phi_p reducible over F): p=3 with Tao
     BH(6,3), F_6, F_2(x)F_3, F_3(x)F_2 over Q(zeta_3)=Q(zeta_6); p=5 with
     F_10, F_2(x)F_5, F_5(x)F_2 over Q(zeta_5)=Q(zeta_10): count same-parity
     triples, pair-lemma violations, and search transversals (all 720 row
     permutations for N=6; identity + seeded random row permutations for N=10).
Output: reviewer-f146-controls-v1.json next to this script.
"""
import datetime
import hashlib
import itertools
import json
import os
import platform
import random
import sys
import time
from fractions import Fraction
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, "reviewer-f146-controls-v1.json")

# --------------------------------------------------------------------------
# exact integer polynomial arithmetic (coefficient lists, low degree first)
# --------------------------------------------------------------------------

def ptrim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return ptrim(r)


def pdivmod_monic(a, b):
    """Exact division of integer polynomial a by MONIC integer polynomial b."""
    a = list(a)
    assert b and b[-1] == 1, "divisor must be monic"
    db = len(b) - 1
    q = [0] * max(0, len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        coef = a[i]
        if coef:
            q[i - db] = coef
            for j in range(db + 1):
                a[i - db + j] -= coef * b[j]
    rem = a[:db] if len(a) > db else a
    return ptrim(q), ptrim(rem)


_PHI = {}


def cyclotomic(n):
    """Phi_n as integer coefficient list, via x^n-1 = prod_{d|n} Phi_d."""
    if n in _PHI:
        return _PHI[n]
    num = [0] * (n + 1)
    num[0] = -1
    num[n] = 1
    den = [1]
    for d in range(1, n):
        if n % d == 0:
            den = pmul(den, cyclotomic(d))
    q, r = pdivmod_monic(num, den)
    assert r == [], ("cyclotomic division not exact", n)
    _PHI[n] = q
    return q


def phi_euler(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


_ZERO_CACHE = {}


def is_zero_rootsum(coeffs, L):
    """True iff sum_e coeffs[e] * zeta_L^e == 0 in C (exact, via Phi_L)."""
    key = (tuple(coeffs), L)
    v = _ZERO_CACHE.get(key)
    if v is None:
        a = ptrim(list(coeffs))
        if not a:
            v = True
        else:
            _, r = pdivmod_monic(a, cyclotomic(L))
            v = (r == [])
        _ZERO_CACHE[key] = v
    return v


def rootsum_coords(coeffs, L):
    """Coordinates of sum_e coeffs[e] zeta_L^e in the power basis 1..zeta_L^(phi(L)-1)."""
    a = ptrim(list(coeffs))
    if not a:
        return [0] * phi_euler(L)
    _, r = pdivmod_monic(a, cyclotomic(L))
    r = r + [0] * (phi_euler(L) - len(r))
    return r


def inner_product_exps(a, b, L):
    """<a,b> = sum_t conj(a_t) b_t for vectors whose entries are exponents mod L
    (root of unity zeta_L^e) or None (zero entry). Returns dense coefficient list."""
    acc = [0] * L
    for x, y in zip(a, b):
        if x is None or y is None:
            continue
        acc[(y - x) % L] += 1
    return acc


def orthogonal_exps(a, b, L):
    return is_zero_rootsum(inner_product_exps(a, b, L), L)


# --------------------------------------------------------------------------
# exact rank over Q (Fraction Gaussian elimination)
# --------------------------------------------------------------------------

def rank_Q(rows):
    m = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    ncols = len(m[0]) if m else 0
    for col in range(ncols):
        piv = None
        for i in range(rank, len(m)):
            if m[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        pv = m[rank][col]
        m[rank] = [x / pv for x in m[rank]]
        for i in range(len(m)):
            if i != rank and m[i][col] != 0:
                f = m[i][col]
                m[i] = [x - f * y for x, y in zip(m[i], m[rank])]
        rank += 1
    return rank


# --------------------------------------------------------------------------
# Butson matrices as exponent matrices mod q
# --------------------------------------------------------------------------

def is_butson_hadamard(k, q):
    """Exact check: all distinct column pairs and row pairs orthogonal, entries exponents mod q."""
    N = len(k)
    cols = [[k[t][c] % q for t in range(N)] for c in range(N)]
    rows = [[k[t][c] % q for c in range(N)] for t in range(N)]
    for c in range(N):
        for d in range(c + 1, N):
            if not orthogonal_exps(cols[c], cols[d], q):
                return False
    for s in range(N):
        for t in range(s + 1, N):
            if not orthogonal_exps(rows[s], rows[t], q):
                return False
    return True


def fourier(n):
    return [[(t * c) % n for c in range(n)] for t in range(n)], n


def tensor_lex(kA, qA, kB, qB):
    """Kronecker product A (x) B with lexicographic index t = t1*nB + t2, exponents mod lcm."""
    nA, nB = len(kA), len(kB)
    q = qA * qB // gcd(qA, qB)
    k = [[0] * (nA * nB) for _ in range(nA * nB)]
    for t1 in range(nA):
        for t2 in range(nB):
            for c1 in range(nA):
                for c2 in range(nB):
                    k[t1 * nB + t2][c1 * nB + c2] = ((q // qA) * kA[t1][c1] + (q // qB) * kB[t2][c2]) % q
    return k, q


def tao_bh63():
    # Tao's 6x6 matrix with cube roots of unity (exponents of omega=zeta_3)
    k = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 2, 2],
        [0, 1, 0, 2, 2, 1],
        [0, 1, 2, 0, 1, 2],
        [0, 2, 2, 1, 0, 1],
        [0, 2, 1, 2, 1, 0],
    ]
    return k, 3


def paley_conference_prime(pr):
    """Symmetric conference matrix of order pr+1 for prime pr = 1 mod 4 (Jacobsthal bordered)."""
    squares = {(y * y) % pr for y in range(1, pr)}

    def chi(x):
        x %= pr
        if x == 0:
            return 0
        return 1 if x in squares else -1

    n = pr + 1
    S = [[0] * n for _ in range(n)]
    for j in range(1, n):
        S[0][j] = 1
        S[j][0] = 1
    for a in range(pr):
        for b in range(pr):
            S[1 + a][1 + b] = chi(b - a)
    return S


def paley_conference_gf9():
    """Symmetric conference matrix of order 10 from GF(9) = F_3[x]/(x^2+1)."""
    elems = [(a, b) for a in range(3) for b in range(3)]  # a + b x

    def mul(u, v):
        a, b = u
        c, d = v
        return ((a * c + 2 * b * d) % 3, (a * d + b * c) % 3)  # x^2 = -1 = 2

    def sub(u, v):
        return ((u[0] - v[0]) % 3, (u[1] - v[1]) % 3)

    squares = {mul(y, y) for y in elems if y != (0, 0)}

    def chi(x):
        if x == (0, 0):
            return 0
        return 1 if x in squares else -1

    n = 10
    S = [[0] * n for _ in range(n)]
    for j in range(1, n):
        S[0][j] = 1
        S[j][0] = 1
    for i, u in enumerate(elems):
        for j, v in enumerate(elems):
            S[1 + i][1 + j] = chi(sub(v, u))
    return S


def conference_checks(S):
    n = len(S)
    sym = all(S[i][j] == S[j][i] for i in range(n) for j in range(n))
    diag0 = all(S[i][i] == 0 for i in range(n))
    off = all(S[i][j] in (1, -1) for i in range(n) for j in range(n) if i != j)
    S2 = [[sum(S[i][k] * S[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    sq = all(S2[i][j] == ((n - 1) if i == j else 0) for i in range(n) for j in range(n))
    return {"symmetric": sym, "zero_diagonal": diag0, "pm1_offdiag": off, "S_squared_is_(n-1)I": sq}


def paley_bh4(S):
    """C = I + i S as exponent matrix mod 4 (1 -> 0, i -> 1, -i -> 3)."""
    n = len(S)
    k = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                k[i][j] = 0
            else:
                k[i][j] = 1 if S[i][j] == 1 else 3
    return k, 4


# --------------------------------------------------------------------------
# Fourier-product QLS of order N = 2p
# --------------------------------------------------------------------------

class FourierProductQLS:
    def __init__(self, k, q, p):
        self.N = N = 2 * p
        assert len(k) == N and all(len(row) == N for row in k)
        self.p = p
        self.q = q
        self.k = k
        self.L = L = (N * q) // gcd(N, q)
        self.a = L // N  # zeta_{2p} = zeta_L^a
        self.b = L // q  # zeta_q = zeta_L^b
        # cell exponent vectors
        self.cell = {}
        for r in range(N):
            for c in range(N):
                self.cell[(r, c)] = [((self.a * r * t) + self.b * k[t][c]) % L for t in range(N)]
        # orthogonality table by (Delta, c, d)
        self.tab = [[[None] * N for _ in range(N)] for _ in range(N)]
        for Delta in range(N):
            for c in range(N):
                for d in range(N):
                    acc = [0] * L
                    for t in range(N):
                        acc[(self.a * Delta * t + self.b * (k[t][d] - k[t][c])) % L] += 1
                    self.tab[Delta][c][d] = is_zero_rootsum(acc, L)

    def orth(self, r, c, s, d):
        return self.tab[(s - r) % self.N][c][d]

    def orth_direct(self, r, c, s, d):
        return orthogonal_exps(self.cell[(r, c)], self.cell[(s, d)], self.L)

    def check_table_against_direct(self):
        N = self.N
        for r, c, s, d in itertools.product(range(N), repeat=4):
            if self.orth(r, c, s, d) != self.orth_direct(r, c, s, d):
                return False
        return True

    def qls_axioms(self):
        N = self.N
        for r in range(N):
            for c in range(N):
                for d in range(c + 1, N):
                    if not self.orth(r, c, r, d):
                        return False
        for c in range(N):
            for r in range(N):
                for s in range(r + 1, N):
                    if not self.orth(r, c, s, c):
                        return False
        # unit norm: each cell has N entries of modulus 1 -> norm^2 = N/N = 1 (by construction)
        return True

    def pair_lemma_cd(self, c, d):
        """h_d(u) == -h_c(u) for all u, in exponent form (needs q even)."""
        q, p = self.q, self.p
        if q % 2:
            return False
        for u in range(p):
            lhs = (self.k[u + p][d] - self.k[u][d]) % q
            rhs = (self.k[u + p][c] - self.k[u][c] + q // 2) % q
            if lhs != rhs:
                return False
        return True

    def pair_statistics(self):
        N, p = self.N, self.p
        same_par_orth = 0
        mixed_par_orth = 0
        lemma_mismatch = 0  # (Delta even nonzero, c!=d): orth != lemma
        lemma_true_pairs = 0
        orth_same_par_but_lemma_false = 0
        for c in range(N):
            for d in range(N):
                if c == d:
                    continue
                lem = self.pair_lemma_cd(c, d)
                if lem:
                    lemma_true_pairs += 1
                for Delta in range(1, N):
                    o = self.tab[Delta][c][d]
                    if Delta % 2 == 0:
                        if o:
                            same_par_orth += 1
                            if not lem:
                                orth_same_par_but_lemma_false += 1
                        if o != lem:
                            lemma_mismatch += 1
                    else:
                        if o:
                            mixed_par_orth += 1
        # counts above are over ordered (c,d) and Delta in 1..N-1; each unordered cell pair
        # {(r,c),(s,d)} with r!=s corresponds to N choices of r for given Delta, so multiply by N/2
        return {
            "ordered_(Delta,c,d)_same_parity_orthogonal": same_par_orth,
            "ordered_(Delta,c,d)_mixed_parity_orthogonal": mixed_par_orth,
            "ordered_(c,d)_with_pair_lemma_true": lemma_true_pairs,
            "lemma_equivalence_mismatches": lemma_mismatch,
            "orthogonal_same_parity_pairs_violating_lemma": orth_same_par_but_lemma_false,
        }

    def same_parity_triples(self):
        N = self.N
        cnt = 0
        ex = None
        for par in (0, 1):
            rows = [r for r in range(N) if r % 2 == par]
            for r1, r2, r3 in itertools.combinations(rows, 3):
                for c1, c2, c3 in itertools.permutations(range(N), 3):
                    if self.orth(r1, c1, r2, c2) and self.orth(r1, c1, r3, c3) and self.orth(r2, c2, r3, c3):
                        cnt += 1
                        if ex is None:
                            ex = [[r1, c1], [r2, c2], [r3, c3]]
        return cnt, ex

    def any_parity_distinct_triples(self):
        """Pairwise-orthogonal triples in three distinct rows (any parity) and distinct columns."""
        N = self.N
        cnt = 0
        for r1, r2, r3 in itertools.combinations(range(N), 3):
            for c1, c2, c3 in itertools.permutations(range(N), 3):
                if self.orth(r1, c1, r2, c2) and self.orth(r1, c1, r3, c3) and self.orth(r2, c2, r3, c3):
                    cnt += 1
        return cnt


def transversal_search(N, orth, node_cap=None, keep=3):
    """Count orthogonal transversals (one cell per row and column, pairwise orthogonal).
    orth(r,c,s,d) -> bool. Returns dict with count, examples, nodes, complete flag."""
    count = 0
    nodes = 0
    examples = []
    chosen = []
    used = [False] * N
    capped = False

    def rec(r):
        nonlocal count, nodes, capped
        if capped:
            return
        if r == N:
            count += 1
            if len(examples) < keep:
                examples.append([[i, c] for i, c in enumerate(chosen)])
            return
        for c in range(N):
            if used[c]:
                continue
            nodes += 1
            if node_cap is not None and nodes > node_cap:
                capped = True
                return
            ok = True
            for s, d in enumerate(chosen):
                if not orth(s, d, r, c):
                    ok = False
                    break
            if ok:
                used[c] = True
                chosen.append(c)
                rec(r + 1)
                chosen.pop()
                used[c] = False

    rec(0)
    return {"count": count, "examples": examples, "nodes": nodes, "complete": not capped}


def verify_cells_pairwise(qls, cells):
    """Direct exact re-verification of pairwise orthogonality of a list of cells."""
    for (r, c), (s, d) in itertools.combinations([tuple(x) for x in cells], 2):
        if not qls.orth_direct(r, c, s, d):
            return False
    return True


def row_permute(k, perm):
    return [k[perm[t]] for t in range(len(k))]


# --------------------------------------------------------------------------
# controls
# --------------------------------------------------------------------------

def control_A_machinery():
    res = {}
    expected_phi = {
        1: [-1, 1], 2: [1, 1], 3: [1, 1, 1], 4: [1, 0, 1], 5: [1, 1, 1, 1, 1], 6: [1, -1, 1],
        10: [1, -1, 1, -1, 1], 12: [1, 0, -1, 0, 1], 15: [1, -1, 0, 1, -1, 1, 0, -1, 1],
        20: [1, 0, -1, 0, 1, 0, -1, 0, 1], 30: [1, 1, 0, -1, -1, -1, 0, 1, 1],
    }
    res["cyclotomic_table_ok"] = all(cyclotomic(n) == v for n, v in expected_phi.items())
    res["cyclotomic_degrees_ok"] = all(len(cyclotomic(n)) - 1 == phi_euler(n) for n in range(1, 61))
    zt = {
        "1+z3+z3^2 == 0": is_zero_rootsum([1, 1, 1], 3),
        "1+z3 != 0": not is_zero_rootsum([1, 1, 0], 3),
        "1+z4^2 == 0": is_zero_rootsum([1, 0, 1, 0], 4),
        "1+z6^3 == 0": is_zero_rootsum([1, 0, 0, 1, 0, 0], 6),
        "1+z6 != 0": not is_zero_rootsum([1, 1, 0, 0, 0, 0], 6),
        "sum z5^j == 0": is_zero_rootsum([1, 1, 1, 1, 1], 5),
        "1+z5+z5^2+z5^3 != 0": not is_zero_rootsum([1, 1, 1, 1, 0], 5),
        "sum z10^{2j} == 0": is_zero_rootsum([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], 10),
        "sum_{t<5} z10^t != 0": not is_zero_rootsum([1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 10),
        "z12^4 + z12^8 + 1 == 0": is_zero_rootsum([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 12),
    }
    res["zero_tests"] = zt
    res["zero_tests_all_ok"] = all(zt.values())
    # Hadamard checker: positives
    tao, q3 = tao_bh63()
    f6, q6 = fourier(6)
    f23, q23 = tensor_lex(*fourier(2), *fourier(3))
    f32, q32 = tensor_lex(*fourier(3), *fourier(2))
    had_pos = {
        "tao_bh63": is_butson_hadamard(tao, q3),
        "F6": is_butson_hadamard(f6, q6),
        "F2xF3_lex": is_butson_hadamard(f23, q23),
        "F3xF2_lex": is_butson_hadamard(f32, q32),
        "F10": is_butson_hadamard(*fourier(10)),
        "F2xF5_lex": is_butson_hadamard(*tensor_lex(*fourier(2), *fourier(5))),
        "F5xF2_lex": is_butson_hadamard(*tensor_lex(*fourier(5), *fourier(2))),
    }
    allones = [[0] * 6 for _ in range(6)]
    tao_bad = [row[:] for row in tao]
    tao_bad[1][1] = 1
    f6_bad = [row[:] for row in f6]
    f6_bad[2][3] = (f6_bad[2][3] + 1) % 6
    had_neg = {
        "all_ones_6x6_rejected": not is_butson_hadamard(allones, 3),
        "tao_one_entry_changed_rejected": not is_butson_hadamard(tao_bad, 3),
        "F6_one_entry_changed_rejected": not is_butson_hadamard(f6_bad, 6),
    }
    res["hadamard_checker_positives"] = had_pos
    res["hadamard_checker_negatives"] = had_neg
    res["hadamard_checker_ok"] = all(had_pos.values()) and all(had_neg.values())
    # transversal search on classical cyclic Latin squares (cells = basis vectors)
    tr = {}
    for n, expected in ((3, 3), (4, 0), (5, 15), (6, 0), (7, 133)):
        Lsq = [[(r + c) % n for c in range(n)] for r in range(n)]
        out = transversal_search(n, lambda r, c, s, d: Lsq[r][c] != Lsq[s][d])
        tr["Z%d" % n] = {"count": out["count"], "expected": expected, "complete": out["complete"]}
    res["cyclic_latin_square_transversals"] = tr
    res["transversal_search_ok"] = all(v["count"] == v["expected"] and v["complete"] for v in tr.values())
    res["all_ok"] = (res["cyclotomic_table_ok"] and res["cyclotomic_degrees_ok"] and res["zero_tests_all_ok"]
                     and res["hadamard_checker_ok"] and res["transversal_search_ok"])
    return res


def relation_dimension(p, field_conductor):
    """dim_F of {a in F^p : sum_j a_j zeta_p^j = 0}, F = Q(zeta_m), m=field_conductor (m=1: Q).
    Computed as (p*[F:Q] - rank_Q{zeta_p^j * beta})/[F:Q], beta over a Q-basis of F."""
    m = field_conductor
    M = (p * m) // gcd(p, m)
    degF = phi_euler(m)
    # Q-basis of F = Q(zeta_m): zeta_m^e, e=0..phi(m)-1 (power basis), as zeta_M^{e*M/m}
    vecs = []
    for j in range(p):
        for e in range(degF):
            coeffs = [0] * M
            coeffs[(j * (M // p) + e * (M // m)) % M] += 1
            vecs.append(rootsum_coords(coeffs, M))
    rk = rank_Q(vecs)
    num = p * degF - rk
    assert num % degF == 0
    return {"p": p, "field": ("Q" if m == 1 else "Q(zeta_%d)" % m), "[F:Q]": degF,
            "rank_Q": rk, "dim_F_relations": num // degF}


def control_B_algebraic_core():
    res = {"relation_dimensions": []}
    for p in (3, 5):
        for m in (1, 4, 3, p):
            d = relation_dimension(p, m)
            d["Phi_p_irreducible_over_F_expected"] = (gcd(m, p) == 1)
            d["consistent"] = (d["dim_F_relations"] == 1) == d["Phi_p_irreducible_over_F_expected"]
            res["relation_dimensions"].append(d)
    res["relation_dimensions_consistent"] = all(d["consistent"] for d in res["relation_dimensions"])
    # explicit reducible-case relation: w_u = zeta_p^u, u=0..p-1, satisfies
    # sum_u zeta_p^{u} w_u = 0 and sum_u w_u = 0 while w != 0 and the w_u are not all equal.
    expl = {}
    for p in (3, 5):
        s1 = [0] * p
        s2 = [0] * p
        for u in range(p):
            s1[(2 * u) % p] += 1  # zeta_p^u * zeta_p^u
            s2[u % p] += 1        # w_u
        expl["p=%d" % p] = {
            "sum_u zeta_p^u w_u == 0": is_zero_rootsum(s1, p),
            "sum_u w_u == 0": is_zero_rootsum(s2, p),
            "w_0 - w_1 != 0 (not all equal)": not is_zero_rootsum([1, -1] + [0] * (p - 2), p),
        }
    res["explicit_reducible_relation"] = expl
    res["explicit_reducible_relation_ok"] = all(all(v.values()) for v in expl.values())
    # irreducible case over Q: both conditions force w = 0 (kernel of the 2-condition system)
    irr = {}
    for p in (3, 5):
        rows = []
        for j in range(p):
            coeffs = [0] * p
            coeffs[j] = 1
            rows.append(rootsum_coords(coeffs, p))  # row j = coordinates of zeta_p^j
        # system: sum_j a_j zeta_p^j = 0  (p-1 Q-equations)  and sum_j a_j = 0 (1 equation)
        A = [[rows[j][i] for j in range(p)] for i in range(p - 1)] + [[1] * p]
        irr["p=%d" % p] = {"rank_of_two_condition_system_over_Q": rank_Q(A), "p": p, "forces_zero": rank_Q(A) == p}
    res["irreducible_two_conditions_force_zero_over_Q"] = irr
    res["all_ok"] = res["relation_dimensions_consistent"] and res["explicit_reducible_relation_ok"] \
        and all(v["forces_zero"] for v in irr.values())
    return res


def analyse_qls(name, k, q, p, full_direct_check=True, node_cap=None):
    t0 = time.time()
    qls = FourierProductQLS(k, q, p)
    out = {"name": name, "N": 2 * p, "p": p, "q": q, "L": qls.L}
    out["K_is_butson_hadamard"] = is_butson_hadamard(k, q)
    out["qls_axioms_exact"] = qls.qls_axioms()
    if full_direct_check:
        out["delta_table_matches_direct_cellwise"] = qls.check_table_against_direct()
    cnt3, ex3 = qls.same_parity_triples()
    out["same_parity_distinct_column_orthogonal_triples"] = cnt3
    out["same_parity_triple_example"] = ex3
    if ex3 is not None:
        out["same_parity_triple_example_reverified_direct"] = verify_cells_pairwise(qls, ex3)
    out["any_parity_distinct_rows_cols_orthogonal_triples"] = qls.any_parity_distinct_triples()
    out["pairs"] = qls.pair_statistics()
    ts = transversal_search(2 * p, qls.orth, node_cap=node_cap)
    out["transversals"] = ts
    if ts["examples"]:
        out["transversal_examples_reverified_direct"] = all(verify_cells_pairwise(qls, ex) for ex in ts["examples"])
    out["seconds"] = round(time.time() - t0, 3)
    return out, qls


def sweep_row_permutations(name, k, q, p, perms, node_cap=None):
    """For each row permutation of K, build the QLS and record triple count / transversal count."""
    N = 2 * p
    t0 = time.time()
    n_tested = 0
    n_with_triples = 0
    n_with_transversal = 0
    n_capped = 0
    first_transversal = None
    first_triple = None
    max_triples = 0
    for perm in perms:
        kk = row_permute(k, perm)
        qls = FourierProductQLS(kk, q, p)
        cnt3, ex3 = qls.same_parity_triples()
        ts = transversal_search(N, qls.orth, node_cap=node_cap, keep=1)
        n_tested += 1
        if cnt3:
            n_with_triples += 1
            max_triples = max(max_triples, cnt3)
            if first_triple is None:
                first_triple = {"row_perm": list(perm), "cells": ex3,
                                "reverified_direct": verify_cells_pairwise(qls, ex3)}
        if not ts["complete"]:
            n_capped += 1
        if ts["count"]:
            n_with_transversal += 1
            if first_transversal is None:
                first_transversal = {"row_perm": list(perm), "cells": ts["examples"][0],
                                     "count_for_this_perm": ts["count"],
                                     "reverified_direct": verify_cells_pairwise(qls, ts["examples"][0])}
    return {"name": name, "p": p, "q": q, "row_permutations_tested": n_tested,
            "perms_with_same_parity_triples": n_with_triples, "max_triples_in_a_perm": max_triples,
            "perms_with_transversal": n_with_transversal, "searches_capped": n_capped,
            "first_triple": first_triple, "first_transversal": first_transversal,
            "seconds": round(time.time() - t0, 3)}


def main():
    t_start = time.time()
    with open(os.path.abspath(__file__), "rb") as fh:
        self_sha = hashlib.sha256(fh.read()).hexdigest()
    report = {
        "script": os.path.basename(__file__),
        "script_sha256": self_sha,
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "started_local": datetime.datetime.now().astimezone().isoformat(),
        "python": sys.version,
        "platform": platform.platform(),
        "machine": platform.machine(),
    }
    print("script sha256", self_sha)

    report["A_machinery"] = control_A_machinery()
    print("A machinery all_ok:", report["A_machinery"]["all_ok"])

    report["B_algebraic_core"] = control_B_algebraic_core()
    print("B algebraic core all_ok:", report["B_algebraic_core"]["all_ok"])
    for d in report["B_algebraic_core"]["relation_dimensions"]:
        print("   p=%d F=%s dim_F(relations)=%d" % (d["p"], d["field"], d["dim_F_relations"]))

    # ---------------- positive controls (Phi_p irreducible over F = Q(i)) ----------------
    S6 = paley_conference_prime(5)
    S10 = paley_conference_gf9()
    report["conference_matrix_checks"] = {"order6_q5": conference_checks(S6), "order10_q9": conference_checks(S10)}
    print("conference checks:", report["conference_matrix_checks"])
    k6, q6 = paley_bh4(S6)
    k10, q10 = paley_bh4(S10)

    pos = {}
    o, _ = analyse_qls("Paley BH(6,4) I+iS, F=Q(i), p=3", k6, q6, 3)
    pos["p3_paley_bh64"] = o
    print("POS p=3 BH(6,4):", {kk: o[kk] for kk in ("K_is_butson_hadamard", "qls_axioms_exact",
          "delta_table_matches_direct_cellwise", "same_parity_distinct_column_orthogonal_triples",
          "any_parity_distinct_rows_cols_orthogonal_triples")}, o["pairs"], o["transversals"]["count"], o["transversals"]["complete"])
    o, _ = analyse_qls("Paley BH(10,4) I+iS, F=Q(i), p=5", k10, q10, 5, node_cap=5_000_000)
    pos["p5_paley_bh104"] = o
    print("POS p=5 BH(10,4):", {kk: o[kk] for kk in ("K_is_butson_hadamard", "qls_axioms_exact",
          "delta_table_matches_direct_cellwise", "same_parity_distinct_column_orthogonal_triples",
          "any_parity_distinct_rows_cols_orthogonal_triples")}, o["pairs"], o["transversals"]["count"], o["transversals"]["complete"], o["transversals"]["nodes"])
    # transposes (also F-Hadamard): theorem must hold for them too
    k6T = [list(col) for col in zip(*k6)]
    k10T = [list(col) for col in zip(*k10)]
    o, _ = analyse_qls("Paley BH(6,4) transpose, F=Q(i), p=3", k6T, q6, 3)
    pos["p3_paley_bh64_transpose"] = o
    o, _ = analyse_qls("Paley BH(10,4) transpose, F=Q(i), p=5", k10T, q10, 5, node_cap=5_000_000)
    pos["p5_paley_bh104_transpose"] = o
    # sweeps over row permutations
    all_perms6 = list(itertools.permutations(range(6)))
    pos["p3_paley_bh64_all_720_row_perms"] = sweep_row_permutations("Paley BH(6,4) all row perms", k6, q6, 3, all_perms6)
    print("POS sweep p=3:", pos["p3_paley_bh64_all_720_row_perms"])
    rng = random.Random(20261028)
    rand_perms10 = [tuple(range(10))] + [tuple(rng.sample(range(10), 10)) for _ in range(24)]
    pos["p5_paley_bh104_25_row_perms"] = sweep_row_permutations("Paley BH(10,4) identity+24 seeded row perms", k10, q10, 5, rand_perms10, node_cap=5_000_000)
    print("POS sweep p=5:", pos["p5_paley_bh104_25_row_perms"])
    report["C_positive_controls"] = pos
    pos_ok = True
    for key in ("p3_paley_bh64", "p5_paley_bh104", "p3_paley_bh64_transpose", "p5_paley_bh104_transpose"):
        o = pos[key]
        pos_ok &= o["K_is_butson_hadamard"] and o["qls_axioms_exact"] and o.get("delta_table_matches_direct_cellwise", True)
        pos_ok &= (o["same_parity_distinct_column_orthogonal_triples"] == 0)
        pos_ok &= (o["transversals"]["count"] == 0 and o["transversals"]["complete"])
        pos_ok &= (o["pairs"]["lemma_equivalence_mismatches"] == 0)
    for key in ("p3_paley_bh64_all_720_row_perms", "p5_paley_bh104_25_row_perms"):
        sw = pos[key]
        pos_ok &= (sw["perms_with_same_parity_triples"] == 0 and sw["perms_with_transversal"] == 0 and sw["searches_capped"] == 0)
    report["C_positive_controls_all_ok"] = bool(pos_ok)
    print("C positive controls all_ok:", pos_ok)

    # ---------------- negative-hypothesis controls (Phi_p reducible over F) ----------------
    neg = {}
    tao, qt = tao_bh63()
    f6, qf6 = fourier(6)
    f23, q23 = tensor_lex(*fourier(2), *fourier(3))
    f32, q32 = tensor_lex(*fourier(3), *fourier(2))
    for nm, (k, q) in (("tao_bh63", (tao, qt)), ("F6", (f6, qf6)), ("F2xF3_lex", (f23, q23)), ("F3xF2_lex", (f32, q32))):
        o, _ = analyse_qls(nm + " F=Q(zeta_3) p=3 (reducible)", k, q, 3)
        neg["p3_" + nm] = o
        print("NEG p=3", nm, "triples", o["same_parity_distinct_column_orthogonal_triples"],
              "pairs", o["pairs"], "transversals", o["transversals"]["count"])
        neg["p3_" + nm + "_all_720_row_perms"] = sweep_row_permutations(nm + " all row perms", k, q, 3, all_perms6)
        print("NEG sweep p=3", nm, neg["p3_" + nm + "_all_720_row_perms"])
    f10, qf10 = fourier(10)
    f25, q25 = tensor_lex(*fourier(2), *fourier(5))
    f52, q52 = tensor_lex(*fourier(5), *fourier(2))
    for nm, (k, q) in (("F10", (f10, qf10)), ("F2xF5_lex", (f25, q25)), ("F5xF2_lex", (f52, q52))):
        o, qls = analyse_qls(nm + " F=Q(zeta_5) p=5 (reducible)", k, q, 5, node_cap=5_000_000)
        neg["p5_" + nm] = o
        print("NEG p=5", nm, "triples", o["same_parity_distinct_column_orthogonal_triples"],
              "pairs", o["pairs"], "transversals", o["transversals"]["count"], o["transversals"]["complete"], o["transversals"]["nodes"])
        if nm == "F10":
            hand = [[0, 0], [2, 1], [4, 2]]
            neg["p5_F10_hand_triple_(0,0),(2,1),(4,2)_orthogonal"] = verify_cells_pairwise(qls, hand)
        neg["p5_" + nm + "_25_row_perms"] = sweep_row_permutations(nm + " identity+24 seeded row perms", k, q, 5, rand_perms10, node_cap=5_000_000)
        print("NEG sweep p=5", nm, neg["p5_" + nm + "_25_row_perms"])
    report["D_negative_hypothesis_controls"] = neg
    # intended-reason negative: in every reducible case the three-cell lemma must FAIL (triples exist)
    neg_triples = {k: v["same_parity_distinct_column_orthogonal_triples"] for k, v in neg.items()
                   if isinstance(v, dict) and "same_parity_distinct_column_orthogonal_triples" in v}
    report["D_every_reducible_case_has_same_parity_triples"] = all(v > 0 for v in neg_triples.values())
    report["D_reducible_transversal_found_anywhere"] = any(
        (isinstance(v, dict) and v.get("perms_with_transversal", 0) > 0) or
        (isinstance(v, dict) and isinstance(v.get("transversals"), dict) and v["transversals"]["count"] > 0)
        for v in neg.values())
    print("D every reducible case has same-parity triples:", report["D_every_reducible_case_has_same_parity_triples"])
    print("D reducible transversal found anywhere:", report["D_reducible_transversal_found_anywhere"])

    report["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    report["finished_local"] = datetime.datetime.now().astimezone().isoformat()
    report["elapsed_seconds"] = round(time.time() - t_start, 3)
    with open(OUT_JSON, "w") as fh:
        json.dump(report, fh, indent=1, sort_keys=False)
    print("wrote", OUT_JSON, "elapsed", report["elapsed_seconds"])


if __name__ == "__main__":
    main()
