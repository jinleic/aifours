#!/usr/bin/env python3
"""f170r control C -- independently authored by reviewer ReviewF170Sun8Sylow.

Exact checks, on actual finite groups, of the coset/index lemmas used by
claims (b) and (c), plus explicit realizations of the (b) coefficient
induction and an intended-reason negative.

  Pair lemma:   H_i g-cosets disjoint  <=>  g not in H_i H_j;
                H_i H_j != G  ==>  I_ij = lcm(m_i,m_j) c_ij, 1 <= c_ij < d_ij.
  Triple lemma: H_iH_j != G and H_iH_k != G  ==>
                I_ijk = lcm(I_ij,m_k) c', 1 <= c' < gcd(I_ij,m_k)
                      <= (d_ij - 1) lcm(d_ik,d_jk).
All subgroups of A5, S5, GL3(2), AGL(1,11) (pairs+triples) and A6 (pairs)
are enumerated (cyclic extension + conjugation).  Products H K are computed
as explicit element sets, never from the product formula.
No author code is imported or executed.  Usage: python3 -B this.py OUTFILE
"""
import itertools
import math
import sys
from collections import Counter

import numpy as np

OUTPATH = sys.argv[1]
LINES = []
RESULTS = []


def log(*a):
    s = " ".join(str(x) for x in a)
    LINES.append(s)
    print(s, flush=True)


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    log(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))


def neg(name, rejected, detail=""):
    RESULTS.append(("NEG " + name, bool(rejected)))
    log(("NEG-REJECTED-AS-INTENDED " if rejected else "NEG-NOT-REJECTED(BAD) ") + name
        + ((" :: " + detail) if detail else ""))


def lcm(a, b):
    return a * b // math.gcd(a, b)


def sign(p):
    n = len(p)
    seen = [False] * n
    s = 0
    for i in range(n):
        if not seen[i]:
            j, L = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            s += L - 1
    return -1 if s % 2 else 1


class Table:
    def __init__(self, elems, mult, e):
        self.elems = elems
        self.mult = mult
        self.N = len(elems)
        self.e = int(e)
        inv = np.empty(self.N, dtype=np.int64)
        r, c = np.nonzero(mult == self.e)
        inv[r] = c
        self.inv = inv
        self._conj = None
        self._order = None

    @property
    def conj(self):
        if self._conj is None:
            C = np.empty((self.N, self.N), dtype=np.int32)
            for g in range(self.N):
                C[g] = self.mult[self.mult[g], self.inv[g]]
            self._conj = C
        return self._conj

    @property
    def order(self):
        if self._order is None:
            o = np.ones(self.N, dtype=np.int64)
            for i in range(self.N):
                x, k = i, 1
                while x != self.e:
                    x = int(self.mult[x, i])
                    k += 1
                o[i] = k
            self._order = o
        return self._order

    def closure(self, gens):
        mask = np.zeros(self.N, dtype=bool)
        mask[self.e] = True
        gens = np.array(sorted(set(int(g) for g in gens)), dtype=np.int64)
        if gens.size == 0:
            return mask
        frontier = np.array([self.e], dtype=np.int64)
        while frontier.size:
            prods = np.unique(self.mult[frontier[:, None], gens[None, :]].ravel())
            new = prods[~mask[prods]]
            mask[new] = True
            frontier = new
        return mask


def perm_table(perms):
    perms = [tuple(p) for p in perms]
    n = len(perms[0])
    N = len(perms)
    P = np.array(perms, dtype=np.int64)
    w = n ** np.arange(n, dtype=np.int64)
    lookup = -np.ones(n ** n, dtype=np.int64)
    lookup[P @ w] = np.arange(N)
    mult = np.empty((N, N), dtype=np.int32)
    for i in range(N):
        mult[i] = lookup[P[i][P] @ w]
    assert (mult >= 0).all()
    return Table(perms, mult, perms.index(tuple(range(n))))


def generic_table(elems, mul, e):
    index = {x: i for i, x in enumerate(elems)}
    N = len(elems)
    mult = np.empty((N, N), dtype=np.int32)
    for i, a in enumerate(elems):
        for j, b in enumerate(elems):
            mult[i, j] = index[mul(a, b)]
    return Table(elems, mult, index[e])


def key_of(mask):
    return np.packbits(mask).tobytes()


def all_subgroups(T):
    cyc = {}
    for g in range(T.N):
        k = key_of(T.closure([g]))
        if k not in cyc:
            cyc[k] = g
    cyc_gens = list(cyc.values())
    reps = []
    key2cls = {}

    def classify(mask, gens):
        k = key_of(mask)
        if k in key2cls:
            return
        idx = np.nonzero(mask)[0]
        inv = (int(idx.size), tuple(sorted(Counter(T.order[idx].tolist()).items())))
        for c, R in enumerate(reps):
            if R["inv"] == inv and R["mask"][T.conj[:, idx]].all(axis=1).any():
                key2cls[k] = c
                return
        reps.append(dict(mask=mask, idx=idx, gens=list(gens), inv=inv))
        key2cls[k] = len(reps) - 1

    triv = np.zeros(T.N, dtype=bool)
    triv[T.e] = True
    classify(triv, [])
    q = 0
    while q < len(reps):
        H = reps[q]
        q += 1
        for g in cyc_gens:
            if not H["mask"][g]:
                gens = H["gens"] + [g]
                classify(T.closure(gens), gens)
    subs = {}
    for R in reps:
        for g in range(T.N):
            m = np.zeros(T.N, dtype=bool)
            m[T.conj[g, R["idx"]]] = True
            subs.setdefault(key_of(m), m)
    return list(subs.values()), len(reps)


def pair_and_triple_checks(name, T, do_triples, primes_gt7):
    subs, ncls = all_subgroups(T)
    N = T.N
    n = len(subs)
    log(f"[{name}] |G|={N} subgroup classes={ncls} subgroups={n}")
    M = np.array(subs)
    orders = M.sum(axis=1)
    idxs = [np.nonzero(m)[0] for m in subs]
    m_ = [N // int(o) for o in orders]
    inter = (M.astype(np.int32) @ M.T.astype(np.int32))
    prod_is_G = np.zeros((n, n), dtype=bool)
    okP1 = okP2 = okP3 = okP4 = okP5 = True
    n_ne = n_eq = n_p5 = 0
    dmin_ne = 99
    for i in range(n):
        for j in range(n):
            HK = np.zeros(N, dtype=bool)
            HK[np.unique(T.mult[idxs[i][:, None], idxs[j][None, :]].ravel())] = True
            size = int(HK.sum())
            okP1 &= size * int(inter[i, j]) == int(orders[i]) * int(orders[j])
            # coset criterion for every g: H_i  and  g H_j  disjoint  <=>  g not in H_i H_j
            meet = M[i][T.mult[:, idxs[j]]].any(axis=1)
            okP2 &= bool((meet == HK).all())
            I = N // int(inter[i, j])
            d = math.gcd(m_[i], m_[j])
            L = lcm(m_[i], m_[j])
            c = I // L
            okP3 &= I % L == 0
            if size < N:
                n_ne += 1
                okP3 &= 1 <= c < d
                dmin_ne = min(dmin_ne, d)
                for p in primes_gt7:
                    if d <= 7 and m_[i] % p and m_[j] % p:
                        n_p5 += 1
                        okP5 &= I % p != 0
            else:
                prod_is_G[i, j] = True
                n_eq += 1
                okP4 &= c == d
    check(f"[{name}] |HK| (explicit) = |H||K|/|H cap K| for all {n * n} ordered pairs", okP1)
    check(f"[{name}] for every g: H and gK disjoint <=> g not in HK (all pairs, all g)", okP2)
    check(f"[{name}] HK != G ==> I = lcm*c with 1 <= c < d (pairs={n_ne}; min d={dmin_ne} >= 2)", okP3 and dmin_ne >= 2)
    neg(f"[{name}] planted 'c < d also when HK = G'", okP4 and n_eq > 0,
        f"{n_eq} pairs with HK=G all have c = d exactly (strictness needs disjointness)")
    if primes_gt7:
        check(f"[{name}] HK != G, d <= 7, p>7 free in both indices ==> p does not divide I "
              f"(p in {primes_gt7}; {n_p5} qualifying pairs)", okP5)
    if not do_triples:
        return
    bits = [int.from_bytes(np.packbits(m).tobytes(), "big") for m in subs]
    okT = True
    okTp = True
    ntr = 0
    ntp = 0
    negw = None
    maxratio = 0.0
    for i in range(n):
        for j in range(n):
            bij = bits[i] & bits[j]
            Iij = N // bij.bit_count()
            dij = math.gcd(m_[i], m_[j])
            for k in range(n):
                main_case = (not prod_is_G[i, j]) and (not prod_is_G[i, k])
                neg_case = (prod_is_G[i, j] and (not prod_is_G[i, k]) and negw is None
                            and min(m_[i], m_[j], m_[k]) > 1 and dij >= 2)
                if not (main_case or neg_case):
                    continue
                dik = math.gcd(m_[i], m_[k])
                djk = math.gcd(m_[j], m_[k])
                g = math.gcd(Iij, m_[k])
                B = (dij - 1) * lcm(dik, djk)
                if main_case:
                    Iijk = N // (bij & bits[k]).bit_count()
                    L = lcm(Iij, m_[k])
                    ntr += 1
                    cp = Iijk // L
                    okT &= (Iijk % L == 0) and (1 <= cp < g) and (g <= B)
                    maxratio = max(maxratio, g / B if B else 0)
                    for p in primes_gt7:
                        if m_[i] % p and m_[j] % p and m_[k] % p and dij <= 7 and p >= B:
                            ntp += 1
                            okTp &= Iijk % p != 0
                elif g > B:
                    negw = (m_[i], m_[j], m_[k], Iij, g, B)
    check(f"[{name}] triple lemma (2)+(3) on all {ntr} ordered triples with H_iH_j != G != H_iH_k "
          f"(max gcd/B = {maxratio:.3f})", okT)
    if primes_gt7:
        check(f"[{name}] triple common-Sylow consequence p>=B, p free ==> p does not divide I_ijk "
              f"({ntp} qualifying triples)", okTp)
    if negw is not None:
        neg(f"[{name}] planted bound (3) for a nondegenerate pair with H_iH_j = G "
            f"(all indices > 1, d_ij >= 2, c_ij = d_ij)", True,
            f"witness (m_i,m_j,m_k,I_ij,gcd(I_ij,m_k),B) = {negw}: bound (3) fails without disjointness")
    else:
        log(f"INFO [{name}] no nondegenerate triple with H_iH_j = G violated bound (3)")


def main():
    log("f170r control C: coset/index lemmas on actual groups and the (b) induction")
    A5 = perm_table([p for p in itertools.permutations(range(5)) if sign(p) == 1])
    S5 = perm_table(list(itertools.permutations(range(5))))
    A6 = perm_table([p for p in itertools.permutations(range(6)) if sign(p) == 1])

    def matmul2(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) % 2 for j in range(3)) for i in range(3))

    mats = []
    for bits in range(512):
        m = tuple(tuple((bits >> (3 * i + j)) & 1 for j in range(3)) for i in range(3))
        det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
               - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
               + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])) % 2
        if det == 1:
            mats.append(m)
    GL = generic_table(mats, matmul2, ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    aff = [(a, b) for a in range(1, 11) for b in range(11)]
    AGL = generic_table(aff, lambda s, t: (s[0] * t[0] % 11, (s[0] * t[1] + s[1]) % 11), (1, 0))
    pair_and_triple_checks("A5", A5, True, [])
    pair_and_triple_checks("S5", S5, True, [])
    pair_and_triple_checks("GL3(2)", GL, True, [])
    pair_and_triple_checks("AGL(1,11)", AGL, True, [11])
    pair_and_triple_checks("A6", A6, False, [])
    # ---------- (b) induction: A7 point stabilizers ----------
    A7 = [p for p in itertools.permutations(range(7)) if sign(p) == 1]
    cos = [frozenset(k for k, p in enumerate(A7) if p[i] == 0) for i in range(7)]
    disj = all(not (cos[i] & cos[j]) for i in range(7) for j in range(i + 1, 7))
    Is = []
    for t in range(1, 8):
        inter = sum(1 for p in A7 if all(p[i] == i for i in range(t)))
        Is.append(2520 // inter)
    cs = [I // 7 for I in Is]
    steps = [Is[t + 1] // lcm(Is[t], 7) for t in range(6)]
    check("A7 cosets {s: s(i)=0}, i=0..6, pairwise disjoint; I_t = 7 c_t with c_t 5-smooth; steps c' in 1..6",
          disj and all(I % 7 == 0 for I in Is) and all(set(factor(c)) <= {2, 3, 5} for c in cs)
          and all(1 <= s <= 6 for s in steps), f"I_t={Is} c'={steps}")
    # ---------- (b) induction: GL3(2) index-7 subgroups ----------
    def mv(m, v):
        return tuple(sum(m[r][k] * v[k] for k in range(3)) % 2 for r in range(3))

    vecs = [v for v in itertools.product(range(2), repeat=3) if any(v)]
    stab7 = []
    for v in vecs:
        stab7.append(frozenset(i for i, m in enumerate(GL.elems) if mv(m, v) == v))
    for f in vecs:  # stabilizers of the plane {x : f.x = 0}
        plane = [v for v in vecs if sum(a * b for a, b in zip(f, v)) % 2 == 0]
        stab7.append(frozenset(i for i, m in enumerate(GL.elems) if all(mv(m, v) in plane for v in plane)))
    ok = len(stab7) == 14 and all(len(s) == 24 for s in stab7)
    okprod = True
    for a, b in itertools.combinations(stab7, 2):
        HK = {int(GL.mult[x, y]) for x in a for y in b}
        okprod &= len(HK) < 168
    oksteps = True
    nseq = 0
    for r in range(2, 5):
        for seq in itertools.permutations(range(14), r):
            cur = stab7[seq[0]]
            I = 168 // len(cur)
            for s in seq[1:]:
                nxt = cur & stab7[s]
                I2 = 168 // len(nxt)
                cp = I2 // lcm(I, 7)
                oksteps &= (I2 % lcm(I, 7) == 0) and 1 <= cp <= 6 and math.gcd(I, 7) == 7
                cur, I = nxt, I2
            nseq += 1
    check(f"GL3(2): 14 index-7 subgroups, all pairwise products != G; every ordered chain of length <= 4 "
          f"({nseq}) has gcd(I_t,7)=7 and steps c' in 1..6", ok and okprod and oksteps)
    # ---------- (b) induction: explicit product group A7 x Z143 ----------
    pos0 = {i: frozenset(k for k, p in enumerate(A7) if p[i] == i) for i in range(7)}
    cosA = {i: frozenset(k for k, p in enumerate(A7) if p[i] == 0) for i in range(7)}
    Lfull = frozenset(range(143))
    L13 = frozenset(range(0, 143, 11))  # order 13
    L11 = frozenset(range(0, 143, 13))  # order 11
    verts = [(0, Lfull), (1, L13), (2, L11), (3, Lfull), (4, Lfull), (5, Lfull), (6, Lfull)]
    Gsize = 2520 * 143

    def subset(v):
        i, L = v
        return frozenset((s, z) for s in pos0[i] for z in L)

    def coset(v):
        i, L = v
        return frozenset((s, z) for s in cosA[i] for z in L)

    H = [subset(v) for v in verts]
    C = [coset(v) for v in verts]
    ms = [Gsize // len(h) for h in H]
    a_ = [m // 7 for m in ms]
    okd = all(not (C[i] & C[j]) for i in range(7) for j in range(i + 1, 7))
    okg = all(math.gcd(ms[i], ms[j]) == 7 for i in range(7) for j in range(i + 1, 7))
    e_idx = A7.index(tuple(range(7)))
    log("A7 x Z143 vertex indices:", ms, "cofactors:", a_)
    for p, sylow in ((13, frozenset((e_idx, z) for z in L13)),
                     (11, frozenset((e_idx, z) for z in L11))):
        J = [t for t in range(7) if a_[t] % p and math.gcd(a_[t], 30) == 1]
        cur = H[J[0]]
        I = Gsize // len(cur)
        A = a_[J[0]]
        okstep = True
        for t in J[1:]:
            nxt = cur & H[t]
            I2 = Gsize // len(nxt)
            cp = I2 // lcm(I, ms[t])
            okstep &= I2 % lcm(I, ms[t]) == 0 and 1 <= cp <= 6 and math.gcd(I, ms[t]) == 7
            A *= a_[t]
            cur, I = nxt, I2
        cJ = I // (7 * A)
        check(f"A7 x Z143, p={p}: J={J}; explicit intersection index I_J={I} = 7*{A}*{cJ} with c 5-smooth; "
              f"steps c' in 1..6; p does not divide I_J; the Sylow {p}-subgroup lies in the intersection",
              okd and okg and okstep and I % (7 * A) == 0 and set(factor(cJ)) <= {2, 3, 5}
              and I % p != 0 and sylow <= cur)
    # ---------- intended-reason negative: even cofactor in A7 x Z2 ----------
    H0 = frozenset((s, z) for s in pos0[0] for z in (0, 1))
    H1 = frozenset((s, z) for s in pos0[1] for z in (0, 1))
    H2 = frozenset((s, 0) for s in pos0[2])
    C0 = frozenset((s, z) for s in cosA[0] for z in (0, 1))
    C1 = frozenset((s, z) for s in cosA[1] for z in (0, 1))
    C2 = frozenset((s, 0) for s in cosA[2])
    Gs = 5040
    m0, m1, m2 = Gs // len(H0), Gs // len(H1), Gs // len(H2)
    I2 = Gs // len(H0 & H1)
    I3 = Gs // len(H0 & H1 & H2)
    cp = I3 // lcm(I2, m2)
    neg("planted 'c' <= 6 even when the selected cofactor is even' in A7 x Z2 (indices 7,7,14; cosets disjoint)",
        not (C0 & C1) and not (C0 & C2) and not (C1 & C2) and (m0, m1, m2) == (7, 7, 14)
        and math.gcd(I2, m2) == 14 and cp >= 7,
        f"I_2={I2}, gcd(I_2,14)={math.gcd(I2, m2)}, I_3={I3}, c'={cp}")
    npass = sum(1 for _, ok_ in RESULTS if ok_)
    log(f"SUMMARY: {npass}/{len(RESULTS)} checks as expected; failures: {[nm for nm, ok_ in RESULTS if not ok_]}")
    with open(OUTPATH, "w") as fh:
        fh.write("\n".join(LINES) + "\n")


def factor(n):
    f = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


if __name__ == "__main__":
    main()
