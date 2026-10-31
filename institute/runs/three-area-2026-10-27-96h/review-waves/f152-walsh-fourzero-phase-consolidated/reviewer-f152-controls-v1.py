#!/usr/bin/env python3
"""reviewer-f152-controls-v1.py

Independent same-harness exact controls for review wave
f152-walsh-fourzero-phase-consolidated (reviewer-authored; no author code imported
or executed).  Every control is written from the packet's *stated* claims and
my own derivations; results are reported as PASS/FAIL per named check, with
positive cases and intended-reason negative cases (mutated constants, mixed
classes, non-character signs, wrong subspaces, perturbed arrays).

Scope of what these controls can and cannot show is recorded in review-v1.md.
"""
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys
import time

import numpy as np

N = 9
SIZE = 1 << N
HALF = SIZE // 2  # 256

RESULTS = {"checks": [], "examples": {}}


def record(name, ok, detail=None, kind="positive"):
    RESULTS["checks"].append({"name": name, "kind": kind, "pass": bool(ok), "detail": detail})
    print(("PASS" if ok else "FAIL"), kind, name, "" if detail is None else detail)


def popcount(v):
    return bin(v).count("1")


def dot(a, x):
    return popcount(a & x) & 1


def fwht(vec):
    """W[a] = sum_x vec[x] * (-1)^{a.x}."""
    w = list(vec)
    h = 1
    n = len(w)
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                u, v = w[j], w[j + h]
                w[j], w[j + h] = u + v, u - v
        h *= 2
    return w


def walsh_k(f):
    """f: 0/1 list of length SIZE.  Returns k = W_f/4 as integer list (requires W%4==0)."""
    W = fwht([1 - 2 * b for b in f])
    assert all(w % 4 == 0 for w in W), "W not divisible by 4"
    return [w // 4 for w in W]


def support(f):
    return [x for x in range(SIZE) if f[x]]


def xor_all(points):
    t = 0
    for p in points:
        t ^= p
    return t


def autocorr(k, b):
    return sum(k[a] * k[a ^ b] for a in range(SIZE))


def anf(tt, nvars):
    """Moebius transform: truth table (list of 0/1 indexed by integer) -> ANF coefficients."""
    c = list(tt)
    n = 1 << nvars
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                c[j + h] ^= c[j]
        h *= 2
    return c


def degree(tt, nvars):
    c = anf(tt, nvars)
    d = -1
    for m, v in enumerate(c):
        if v:
            d = max(d, popcount(m))
    return d


def rank_f2(rows):
    """rank over F2 of a list of integer bitmasks."""
    rows = list(rows)
    r = 0
    piv = []
    for row in rows:
        for p in piv:
            row = min(row, row ^ p)
        if row:
            piv.append(row)
            r += 1
    return r


def random_balanced(rng):
    f = [0] * SIZE
    for x in rng.sample(range(SIZE), HALF):
        f[x] = 1
    return f


# ---------------------------------------------------------------------------
# Even-half coordinates for T != 0: drop the lowest set bit j of T; the other
# eight bits parametrise K = T^perp bijectively (a_j is forced by a.T = 0).
# ---------------------------------------------------------------------------
class EvenHalf:
    def __init__(self, k, T):
        assert T != 0
        self.k = k
        self.T = T
        self.j = (T & -T).bit_length() - 1
        self.others = [i for i in range(N) if i != self.j]
        self.K = [a for a in range(SIZE) if dot(a, T) == 0]
        assert len(self.K) == HALF
        self.a_of = [self.to_a(al) for al in range(HALF)]
        assert sorted(self.a_of) == sorted(self.K)
        self.al_of = {a: al for al, a in enumerate(self.a_of)}
        # basis vectors b_i (coordinate i) as 9-bit vectors
        self.basis = [self.to_a(1 << i) for i in range(8)]
        # q = k/2 mod 2 on K in alpha coordinates
        for a in self.K:
            assert k[a] % 2 == 0
        self.q = [((k[a] // 2) % 2) for a in self.a_of]
        self.Bmat = [[self.B(1 << i, 1 << j2) for j2 in range(8)] for i in range(8)]
        self.rank = rank_f2([sum(self.Bmat[i][j2] << j2 for j2 in range(8)) for i in range(8)])
        self.rad = [r for r in range(HALF) if all(self.B(r, 1 << i) == 0 for i in range(8))]
        # odd half base point a0 = e_j (T_j = 1 so a0 . T = 1)
        self.a0 = 1 << self.j
        assert dot(self.a0, T) == 1
        self.Q = [(((k[self.a0 ^ a] - 1) // 2) % 2) for a in self.a_of]

    def to_a(self, al):
        a = 0
        for idx, i in enumerate(self.others):
            if (al >> idx) & 1:
                a |= 1 << i
        if dot(a, self.T):
            a |= 1 << self.j
        return a

    def B(self, x, y):
        return self.q[x ^ y] ^ self.q[x] ^ self.q[y] ^ self.q[0]

    def polarQ(self, x, y):
        return self.Q[x ^ y] ^ self.Q[x] ^ self.Q[y] ^ self.Q[0]


def receipts_begin():
    out = subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True)
    return out.stdout.strip()


# ===========================================================================
# A. Exact Boolean caller (4),(5) and converse
# ===========================================================================
def control_A():
    rng = random.Random(152001)
    f = random_balanced(rng)
    M = support(f)
    T = xor_all(M)
    k = walsh_k(f)
    ok = k[0] == 0
    for a in range(1, SIZE):
        n_a = sum(dot(a, x) for x in M)
        ok &= k[a] == n_a - 128
        ok &= (k[a] % 2) == dot(a, T)
    record("A1 k(a)=n_a-128, k(0)=0, k(a)=a.T mod 2 on random balanced f", ok)
    record("A2 Parseval sum k^2 = 2^14", sum(v * v for v in k) == 16384, sum(v * v for v in k))
    C = [autocorr(k, b) for b in range(SIZE)]
    record("A3 autocorrelation C(b)=2^14*[b=0] all 512 shifts", C[0] == 16384 and all(C[b] == 0 for b in range(1, SIZE)))
    # converse: U(x)=sum_a k(a)(-1)^{a.x}; U^2=2^14 and U/128 = (-1)^f
    U = fwht(k)
    record("A4 converse U(x)^2=2^14 and U/128=(-1)^f", all(u * u == 16384 for u in U) and all(U[x] // 128 == 1 - 2 * f[x] for x in range(SIZE)))
    # negative 1: unbalanced function (weight 255): W(0)=2 not divisible by 4
    g = list(f)
    g[M[0]] = 0
    W = fwht([1 - 2 * b for b in g])
    record("A5neg unbalanced (wt 255): W(0)=2, not 0 mod 4 -> caller hypotheses fail", W[0] == 2 and W[0] % 4 != 0, W[0], kind="negative")
    # negative 2: perturb one entry of k -> (5) fails at some shift and U^2 != 2^14 somewhere
    k2 = list(k)
    k2[7] += 2
    C2 = [autocorr(k2, b) for b in range(SIZE)]
    U2 = fwht(k2)
    bad_shift = sum(1 for b in range(1, SIZE) if C2[b] != 0)
    record("A6neg perturbed array: nonzero C(b) at some b != 0 and U^2 != 2^14 somewhere", bad_shift > 0 and any(u * u != 16384 for u in U2), {"nonzero_shifts": bad_shift, "C0": C2[0]}, kind="negative")
    RESULTS["examples"]["A_T"] = T


# ===========================================================================
# B. Support-moment identities (9), (11); q quadratic on K; polar(Q)=B
# ===========================================================================
def check_moments(f, label):
    M = support(f)
    T = xor_all(M)
    k = walsh_k(f)
    # (9) for all a,b: k(a+b)-k(a)-k(b) = -2 sum_{x in M} (a.x)(b.x)  (mod 4)
    bits = [sum(dot(a, x) << i for i, x in enumerate(M)) for a in range(SIZE)]  # 256-bit masks
    ok9 = True
    for a in range(SIZE):
        ba = bits[a]
        for b in range(SIZE):
            lhs = k[a ^ b] - k[a] - k[b]
            rhs = -2 * popcount(ba & bits[b])
            if (lhs - rhs) % 4 != 0:
                ok9 = False
                break
        if not ok9:
            break
    record(f"B1[{label}] identity (9) for all 512x512 (a,b)", ok9)
    if T == 0:
        return None
    E = EvenHalf(k, T)
    # first moments along basis of K are even
    m1 = [sum(dot(b, x) for x in M) for b in E.basis]
    record(f"B2[{label}] first support moments m_i even on a basis of K", all(m % 2 == 0 for m in m1), m1)
    # moments m_ij, m_ijl in alpha coordinates (bits of b_i . u)
    coords = []
    for x in M:
        coords.append([dot(b, x) for b in E.basis])
    m2 = {}
    m3 = {}
    for i, j2 in itertools.combinations(range(8), 2):
        m2[(i, j2)] = sum(c[i] & c[j2] for c in coords)
    for i, j2, l in itertools.combinations(range(8), 3):
        m3[(i, j2, l)] = sum(c[i] & c[j2] & c[l] for c in coords)
    ok11 = True
    ok11_no_cubic = True
    for al in range(HALF):
        bitsal = [(al >> i) & 1 for i in range(8)]
        rhs = sum((m1[i] // 2) * bitsal[i] for i in range(8))
        rhs -= sum(m2[(i, j2)] * bitsal[i] * bitsal[j2] for (i, j2) in m2)
        cubic = 2 * sum(m3[(i, j2, l)] * bitsal[i] * bitsal[j2] * bitsal[l] for (i, j2, l) in m3)
        lhs = k[E.a_of[al]] // 2
        if (lhs - rhs - cubic) % 4 != 0:
            ok11 = False
        if (lhs - rhs) % 4 != 0:
            ok11_no_cubic = False
    record(f"B3[{label}] identity (11) k/2 = sum m_i/2 a_i - sum m_ij a_i a_j + 2 sum m_ijl a_i a_j a_l (mod 4) on all 256 of K", ok11)
    record(f"B4neg[{label}] dropping the cubic-moment term breaks (11) mod 4", not ok11_no_cubic, kind="negative")
    # q quadratic on K; degree of q as 8-variable function
    dq = degree(E.q, 8)
    record(f"B5[{label}] q=k/2 mod 2 has algebraic degree <= 2 on K (deg={dq})", dq <= 2, dq)
    # outside K: all k odd (q undefined there) -- intended-reason negative for 'q on all of F_2^9'
    odd_outside = all(k[a] % 2 == 1 for a in range(SIZE) if dot(a, T) == 1)
    record(f"B6[{label}] all 256 frequencies outside K have odd k (T != 0)", odd_outside)
    # polar(Q) == B on all pairs; independence of a0
    okQ = all(E.polarQ(x, y) == E.B(x, y) for x in range(HALF) for y in range(HALF))
    record(f"B7[{label}] polar of odd-half Q equals B on all 256x256 pairs", okQ)
    a0b = E.a0 ^ E.a_of[rng_b.randrange(1, HALF)]
    Qb = [(((k[a0b ^ a] - 1) // 2) % 2) for a in E.a_of]
    pol_b = all((Qb[x ^ y] ^ Qb[x] ^ Qb[y] ^ Qb[0]) == E.B(x, y) for x in range(HALF) for y in range(HALF))
    record(f"B8[{label}] polar of Q with a different odd base point a0' still equals B", pol_b)
    # negative: perturb one odd k by +2 (toggles one Q value) -> polar changes somewhere
    kp = list(k)
    kp[a0b] += 2
    Qp = [(((kp[E.a0 ^ a] - 1) // 2) % 2) for a in E.a_of]
    pol_p = all((Qp[x ^ y] ^ Qp[x] ^ Qp[y] ^ Qp[0]) == E.B(x, y) for x in range(HALF) for y in range(HALF))
    record(f"B9neg[{label}] toggling a single odd coefficient class breaks polar(Q)=B", not pol_p, kind="negative")
    return E


rng_b = random.Random(152002)


def control_B():
    rng = random.Random(152003)
    for trial in range(3):
        f = random_balanced(rng)
        check_moments(f, f"rand{trial}")


# ===========================================================================
# C. Radical phase laws on actual balanced functions with rank(B)=6, q|R=0
# ===========================================================================
def find_rank6_examples(rng, want=3, max_tries=400):
    found = []
    tries = 0
    while len(found) < want and tries < max_tries:
        tries += 1
        f = random_balanced(rng)
        M = support(f)
        T = xor_all(M)
        if T == 0:
            continue
        k = walsh_k(f)
        E = EvenHalf(k, T)
        if E.rank != 6 or len(E.rad) != 4:
            continue
        if any(E.q[r] for r in E.rad):
            continue
        found.append((f, k, T, E, tries))
    return found


def control_C():
    rng = random.Random(152004)
    exs = find_rank6_examples(rng)
    record("C0 found actual balanced 9-variable functions with T!=0, rank(B)=6, |rad|=4, q|rad=0", len(exs) == 3, [e[4] for e in exs])
    for idx, (f, k, T, E, tries) in enumerate(exs):
        tag = f"ex{idx}"
        R = E.rad
        sha = hashlib.sha256(bytes(f)).hexdigest()
        RESULTS["examples"][tag] = {"truth_table_sha256": sha, "T": T, "rank": E.rank, "rad_alpha": R,
                                    "peak_abs_k": max(abs(v) for v in k), "zeros": sum(1 for v in k if v == 0),
                                    "q_zero_count": E.q.count(0)}
        # rho(r)=Q(x+r)+Q(x) constant in x for r in R, linear
        rho = {}
        ok = True
        for r in R:
            vals = {E.Q[x ^ r] ^ E.Q[x] for x in range(HALF)}
            ok &= len(vals) == 1
            rho[r] = vals.pop()
        lin = all(rho[r ^ s] == rho[r] ^ rho[s] for r in R for s in R)
        record(f"C1[{tag}] rho(r)=Q(x+r)+Q(x) is x-independent for every r in rad B, and linear", ok and lin, {str(r): rho[r] for r in R})
        # rho != 0 => wt(Q)=128 ; rho = 0 => wt(Q) in {112,144} and Q R-periodic
        wQ = sum(E.Q)
        if any(rho.values()):
            record(f"C2[{tag}] rho != 0 => Q balanced (wt 128)", wQ == 128, wQ)
        else:
            record(f"C2[{tag}] rho = 0 => wt(Q) in {{112,144}}", wQ in (112, 144), wQ)
        # delta_r(a) = (k(a+r)-k(a))/4 mod 2 well-defined on K and of degree <= 2 (general form of (10))
        okd = True
        degs = {}
        delta = {}
        for r in R:
            if r == 0:
                continue
            diffs = [k[E.a_of[x ^ r]] - k[E.a_of[x]] for x in range(HALF)]
            if any(d % 4 for d in diffs):
                okd = False
                continue
            dr = [(d // 4) % 2 for d in diffs]
            delta[r] = dr
            degs[r] = degree(dr, 8)
        record(f"C3[{tag}] k(a+r)-k(a) = 0 mod 4 on K for r in R and delta_r=(k(a+r)-k(a))/4 mod 2 has degree <= 2", okd and all(d <= 2 for d in degs.values()), {str(r): d for r, d in degs.items()})
        # translation law: k_t = (-1)^{a.t} k ; rho_t = rho + psi_t ; delta_r^t = delta_r + psi_t(r) q
        okt = True
        for trial in range(6):
            t = rng.randrange(SIZE)
            kt = [((-1) ** dot(a, t)) * k[a] for a in range(SIZE)]
            Et = EvenHalf(kt, T)
            okt &= Et.q == E.q
            for r in R:
                psi = dot(E.a_of[r], t)
                vals = {Et.Q[x ^ r] ^ Et.Q[x] for x in range(HALF)}
                okt &= vals == {rho[r] ^ psi}
                if r:
                    drt = [((kt[E.a_of[x ^ r]] - kt[E.a_of[x]]) // 4) % 2 for x in range(HALF)]
                    okt &= drt == [delta[r][x] ^ (psi & E.q[x]) for x in range(HALF)]
        record(f"C4[{tag}] translation law: q_t=q, rho_t=rho+psi_t, delta_r^t=delta_r+psi_t(r)q (6 random t)", okt)
        # complement law: k -> -k leaves rho and delta unchanged
        kc = [-v for v in k]
        Ec = EvenHalf(kc, T)
        okc = Ec.q == E.q
        for r in R:
            okc &= {Ec.Q[x ^ r] ^ Ec.Q[x] for x in range(HALF)} == {rho[r]}
            if r:
                okc &= [((kc[E.a_of[x ^ r]] - kc[E.a_of[x]]) // 4) % 2 for x in range(HALF)] == delta[r]
        record(f"C5[{tag}] global complement k->-k preserves q, rho and delta_r", okc)
        # every character of R* is realised by exactly 128 translations t
        cnt = {}
        r1, r2 = [r for r in R if r][:2]
        for t in range(SIZE):
            key = (dot(E.a_of[r1], t), dot(E.a_of[r2], t))
            cnt[key] = cnt.get(key, 0) + 1
        record(f"C6[{tag}] each of the 4 characters of R occurs for exactly 128 translations", sorted(cnt.values()) == [128] * 4, {str(key): value for key, value in cnt.items()})
        # negative: a 2-plane R' not inside rad B -> Q(x+r)+Q(x) not constant for some r in R'
        while True:
            s1, s2 = rng.randrange(1, HALF), rng.randrange(1, HALF)
            Rp = [0, s1, s2, s1 ^ s2]
            if len(set(Rp)) == 4 and not all(r in R for r in Rp):
                break
        nonconst = any(len({E.Q[x ^ r] ^ E.Q[x] for x in range(HALF)}) > 1 for r in Rp if r)
        record(f"C7neg[{tag}] for a 2-plane not inside rad B, Q(x+r)+Q(x) depends on x", nonconst, Rp, kind="negative")


# ===========================================================================
# D. Pointwise fiber inequalities, mutated constants, class mixing, summation (12)
# ===========================================================================
def max_gap(values):
    best = None
    arg = None
    for tup in itertools.product(values, repeat=4):
        E = sum(v * v for v in tup)
        S = sum(tup)
        g = 10 * E - S * S
        if best is None or g > best:
            best, arg = g, tup
    return best, arg


def control_D():
    g0, a0 = max_gap([4, -4])
    record("D1 q-zero even fiber {+-4}^4: max(10E-S^2)=640", g0 == 640, {"max": g0, "at": a0})
    record("D1neg constant 639 fails", g0 > 639, kind="negative")
    g1, a1 = max_gap([-6, 2])
    g1b, _ = max_gap([-2, 6])
    record("D2 q-one even fiber single class {-6,2}^4 and {-2,6}^4: max(10E-S^2)=864", g1 == 864 and g1b == 864, {"max": g1, "at": a1})
    record("D2neg constant 863 fails", g1 > 863, kind="negative")
    # closed form 64(n-3)(n-4)
    ok = True
    for n in range(5):
        E = 16 + 32 * n
        S2 = (8 - 8 * n) ** 2
        ok &= (S2 - 10 * E + 864) == 64 * (n - 3) * (n - 4)
    record("D3 closed form S^2-10E+864 = 64(n-3)(n-4) for n=0..4", ok)
    g1m, a1m = max_gap([-6, -2, 2, 6])
    record("D4neg mixed classes {+-2,+-6}^4: max(10E-S^2)=1440 > 864 (class constraint load-bearing)", g1m == 1440 and g1m > 864, {"max": g1m, "at": a1m}, kind="negative")
    g2, a2 = max_gap([-7, -3, 1, 5])
    g2b, _ = max_gap([7, 3, -1, -5])
    record("D5 odd fiber single class {-7,-3,1,5}^4 (and negative): max(10E-S^2)=1464", g2 == 1464 and g2b == 1464, {"max": g2, "at": a2})
    record("D5neg constant 1463 fails", g2 > 1463, kind="negative")
    vert = {n: 600 + 720 * n - 144 * n * n for n in range(5)}
    record("D6 vertex formula 600+720n-144n^2 for n entries -7, rest 5; max 1464 at n=2,3", vert == {0: 600, 1: 1176, 2: 1464, 3: 1464, 4: 1176}, vert)
    g2m, a2m = max_gap([-7, -5, -3, -1, 1, 3, 5, 7])
    record("D7neg mixed odd classes: max(10E-S^2)=1960 > 1464 (rho=lambda class constraint load-bearing)", g2m == 1960, {"max": g2m, "at": a2m}, kind="negative")
    # summation (12)
    summ = {}
    for z in (112, 144):
        n0 = (z - 4) // 4
        n1 = (256 - z) // 4
        bound = 10 * 16384 - 640 * n0 - 864 * n1 - 1464 * 64
        closed = 16384 + 56 * (z - 16)
        fibers_total = 1 + n0 + n1 + 64
        bound_mixed = 10 * 16384 - 640 * n0 - 1440 * n1 - 1960 * 64
        summ[z] = {"bound": bound, "closed_form": closed, "exceeds_16384": bound > 16384, "fibers": fibers_total,
                   "bound_with_mixed_classes": bound_mixed, "mixed_contradicts": bound_mixed > 16384}
    ok = all(summ[z]["bound"] == summ[z]["closed_form"] and summ[z]["exceeds_16384"] and summ[z]["fibers"] == 128 for z in summ)
    record("D8 summation (12): bound = 16384+56(z-16) > 16384 for z in {112,144}; 128 fibers", ok, summ)
    record("D9neg with mixed-class constants (1440,1960) the summation gives no contradiction", not any(summ[z]["mixed_contradicts"] for z in summ), kind="negative")
    # mod-8 sign identities
    ok8 = all(((-k) - (k + 4 * ((k // 2) % 2))) % 8 == 0 for k in (0, 2, -2, 4, -4, 6, -6))
    okodd = all((((-k - 1) // 2) % 2) == (1 - ((k - 1) // 2) % 2) for k in (1, -1, 3, -3, 5, -5, 7, -7))
    record("D10 (-1)k = k+4q (mod 8) for even |k|<=6, and odd negation toggles (k-1)/2 mod 2", ok8 and okodd)
    # (10)-class bookkeeping: with k(a+r)=k(a)+4 lambda(r) q (mod 8) and chi=(-1)^lambda, modulated entries share a class
    okcls = True
    for ka in (2, -2, 6, -6):
        for lam in (0, 1):
            for kr in (2, -2, 6, -6):
                if (kr - ka - 4 * lam) % 8:
                    continue
                mod = (-1) ** lam * kr
                okcls &= (mod - ka) % 8 == 0
    record("D11 even q-one fiber: chi(r)k(a+r) = k(a) (mod 8) whenever k(a+r)=k(a)+4lambda(r) (mod 8)", okcls)
    okodd2 = True
    for ka in (1, -1, 3, -3, 5, -5, 7, -7):
        for lam in (0, 1):
            for kr in (1, -1, 3, -3, 5, -5, 7, -7):
                if (kr - ka - 2 * lam) % 4:
                    continue  # Q(x+r)=Q(x)+rho(r) with rho=lambda
                mod = (-1) ** lam * kr
                okodd2 &= (mod - ka) % 4 == 0
    record("D12 odd fiber: with rho=lambda, chi(r)k(a0+x+r) = k(a0+x) (mod 4): single class {-7,-3,1,5} or negative", okodd2)
    # normalization counts
    record("D13 normalized counts (256-z)/2 = 72/56 and z-4 = 108/140", {z: (256 - z) // 2 for z in (112, 144)} == {112: 72, 144: 56} and {z: z - 4 for z in (112, 144)} == {112: 108, 144: 140})


# ===========================================================================
# E. Character orthogonality  sum_F S_F^2 = sum_{r in R} chi(r) C(r)  on actual functions
# ===========================================================================
def coset_sum(k, R, chi, reps):
    tot = 0
    for a in reps:
        S = sum(chi[i] * k[a ^ r] for i, r in enumerate(R))
        tot += S * S
    return tot


def control_E():
    rng = random.Random(152005)
    f = random_balanced(rng)
    k = walsh_k(f)
    # random 2-plane in F_2^9
    r1, r2 = rng.randrange(1, SIZE), rng.randrange(1, SIZE)
    while r1 == r2:
        r2 = rng.randrange(1, SIZE)
    R = [0, r1, r2, r1 ^ r2]
    chars = [[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]]
    # coset representatives: canonical (min) and random
    seen = set()
    reps_min = []
    for a in range(SIZE):
        if a in seen:
            continue
        cos = [a ^ r for r in R]
        seen.update(cos)
        reps_min.append(min(cos))
    reps_rand = [c ^ rng.choice(R) for c in reps_min]
    Cr = {r: autocorr(k, r) for r in R}
    ok = True
    for chi in chars:
        t1 = coset_sum(k, R, chi, reps_min)
        t2 = coset_sum(k, R, chi, reps_rand)
        rhs = sum(chi[i] * Cr[r] for i, r in enumerate(R))
        ok &= t1 == t2 == rhs == 16384
    record("E1 sum_F S_F^2 = sum_r chi(r)C(r) = 16384 for all 4 characters, representative-independent (actual f)", ok, {"R": R, "C": Cr})
    # sign orientation: changing representative by s multiplies S_F by chi(s)
    oks = True
    chi = chars[1]
    for a in reps_min:
        for i, s in enumerate(R):
            S1 = sum(chi[t] * k[a ^ r] for t, r in enumerate(R))
            S2 = sum(chi[t] * k[a ^ s ^ r] for t, r in enumerate(R))
            oks &= S2 == chi[i] * S1
    record("E2 S_F changes by the sign chi(s) under representative shift s; S_F^2 invariant", oks)
    # negative: non-character sign vector -> total depends on representatives
    sigma = [1, 1, 1, -1]
    t1 = coset_sum(k, R, sigma, reps_min)
    t2 = coset_sum(k, R, sigma, reps_rand)
    record("E3neg non-character sign vector (1,1,1,-1): coset total depends on representatives", t1 != t2, {"min_reps": t1, "rand_reps": t2}, kind="negative")
    # negative: non-Boolean array (perturbed k): identity holds but total != 16384 for some chi
    k2 = list(k)
    k2[r1] += 1
    k2[0] -= 1
    Cr2 = {r: autocorr(k2, r) for r in R}
    okid = True
    anydiff = False
    for chi in chars:
        t = coset_sum(k2, R, chi, reps_min)
        rhs = sum(chi[i] * Cr2[r] for i, r in enumerate(R))
        okid &= t == rhs
        anydiff |= t != 16384
    record("E4neg perturbed array: identity sum S^2 = sum chi C still holds but total != 16384 for some chi", okid and anydiff, Cr2, kind="negative")
    # E5: on the actual rank-6 examples with R = rad B and chi = (-1)^{rho}: sum S_F^2 = 16384 and the
    #     per-fiber 'gap' 10E_F - S_F^2 summed equals 10*16384-16384 = 147456 (identity, no inequality needed)
    rng2 = random.Random(152004)
    ex = find_rank6_examples(rng2, want=1)[0]
    f, k, T, E, _ = ex
    Ra = E.rad
    R9 = [E.a_of[r] for r in Ra]
    rho = {r: (E.Q[r] ^ E.Q[0]) for r in Ra}
    chi = [(-1) ** rho[r] for r in Ra]
    seen = set()
    reps = []
    for a in range(SIZE):
        if a in seen:
            continue
        cos = [a ^ r for r in R9]
        seen.update(cos)
        reps.append(a)
    tot = coset_sum(k, R9, chi, reps)
    gap = sum(10 * sum(k[a ^ r] ** 2 for r in R9) - sum(chi[i] * k[a ^ r] for i, r in enumerate(R9)) ** 2 for a in reps)
    record("E5 actual rank-6 example, R=rad B, chi=(-1)^rho: sum S_F^2 = 16384 and sum(10E_F - S_F^2) = 147456", tot == 16384 and gap == 147456, {"sum_S2": tot, "sum_gap": gap, "peak_abs_k": max(abs(v) for v in k)})


# ===========================================================================
# F. Six-variable vanishing lemma and quadratic weight census
# ===========================================================================
def monomials(nvars, maxdeg):
    mons = []
    for d in range(maxdeg + 1):
        for S in itertools.combinations(range(nvars), d):
            mons.append(S)
    return mons


def mono_tt(S, nvars):
    tt = 0
    for x in range(1 << nvars):
        if all((x >> i) & 1 for i in S):
            tt |= 1 << x
    return tt


def kernel_dim_on_zero_set(qtt, nvars, maxdeg):
    """dimension over F2 of {p: deg p <= maxdeg, p vanishes on {q=0}}."""
    mons = monomials(nvars, maxdeg)
    zero_pts = [x for x in range(1 << nvars) if not (qtt >> x) & 1]
    # columns = monomials; rows = zero points; rank of evaluation matrix
    rows = []
    for x in zero_pts:
        row = 0
        for ci, S in enumerate(mons):
            if all((x >> i) & 1 for i in S):
                row |= 1 << ci
        rows.append(row)
    rk = rank_f2(rows)
    return len(mons) - rk, len(zero_pts)


def control_F():
    nv = 6
    q_hyp = mono_tt((0, 1), nv) ^ mono_tt((2, 3), nv) ^ mono_tt((4, 5), nv)
    q_ell = q_hyp ^ mono_tt((0,), nv) ^ mono_tt((1,), nv)
    q_r4 = mono_tt((0, 1), nv) ^ mono_tt((2, 3), nv)
    res = {}
    for name, q in (("hyperbolic", q_hyp), ("elliptic", q_ell)):
        kd, nz = kernel_dim_on_zero_set(q, nv, 2)
        res[name] = {"kernel_dim_deg<=2": kd, "zero_count": nz, "weight": 64 - nz}
        kd1, _ = kernel_dim_on_zero_set(q, nv, 1)
        res[name]["kernel_dim_deg<=1"] = kd1
        kd3, _ = kernel_dim_on_zero_set(q, nv, 3)
        res[name]["kernel_dim_deg<=3"] = kd3
    record("F1 nondegenerate 6-var q: degree<=2 polynomials vanishing on {q=0} form a 1-dim space (={0,q}); zero counts 36/28",
           res["hyperbolic"]["kernel_dim_deg<=2"] == 1 and res["elliptic"]["kernel_dim_deg<=2"] == 1 and res["hyperbolic"]["zero_count"] == 36 and res["elliptic"]["zero_count"] == 28, res)
    record("F2 degree<=1 polynomials vanishing on {q=0}: only 0", res["hyperbolic"]["kernel_dim_deg<=1"] == 0 and res["elliptic"]["kernel_dim_deg<=1"] == 0)
    record("F3neg degree<=3 polynomials vanishing on {q=0}: dimension > 1 (degree bound load-bearing)", res["hyperbolic"]["kernel_dim_deg<=3"] > 1 and res["elliptic"]["kernel_dim_deg<=3"] > 1, {"hyp": res["hyperbolic"]["kernel_dim_deg<=3"], "ell": res["elliptic"]["kernel_dim_deg<=3"]}, kind="negative")
    kd4, nz4 = kernel_dim_on_zero_set(q_r4, nv, 2)
    record("F4 (comparison) rank-4 q=x0x1+x2x3 in 6 vars: kernel dim of degree<=2 vanishing polynomials", True, {"kernel_dim": kd4, "zero_count": nz4}, kind="info")
    # full weight census of all 2^22 degree<=2 functions in 6 variables (numpy uint64 truth tables)
    mons = monomials(nv, 2)
    tts = np.array([mono_tt(S, nv) for S in mons], dtype=np.uint64)
    arr = np.zeros(1, dtype=np.uint64)
    for m in tts:
        arr = np.concatenate([arr, arr ^ m])
    assert arr.shape[0] == 1 << 22
    # popcount via byte view
    b = arr.view(np.uint8).reshape(-1, 8)
    wts = np.unpackbits(b, axis=1).sum(axis=1)
    census = {int(w): int(c) for w, c in zip(*np.unique(wts, return_counts=True))}
    nonzero_weights = sorted(w for w in census if w != 0)
    record("F5 weights of nonzero degree<=2 functions in 6 variables = {16,24,28,32,36,40,48,64}", nonzero_weights == [16, 24, 28, 32, 36, 40, 48, 64], census)
    pair_sums = {a + b2 for a in nonzero_weights for b2 in nonzero_weights}
    record("F6 no two nonzero such weights sum to 28 or 36", 28 not in pair_sums and 36 not in pair_sums)
    # 5-variable census: minimum nonzero weight 8 = 2^(5-2); rank-0/2/4 weight sets {0,16,32},{8,16,24},{12,16,20}
    mons5 = monomials(5, 2)
    tts5 = [mono_tt(S, 5) for S in mons5]
    arr5 = np.zeros(1, dtype=np.uint64)
    for m in tts5:
        arr5 = np.concatenate([arr5, arr5 ^ np.uint64(m)])
    b5 = arr5.view(np.uint8).reshape(-1, 8)
    w5 = np.unpackbits(b5, axis=1).sum(axis=1)
    census5 = {int(w): int(c) for w, c in zip(*np.unique(w5, return_counts=True))}
    record("F7 5-variable degree<=2 census: nonzero weights subset of {8,12,16,20,24,32} (min 8 = 2^(5-2))", sorted(w for w in census5 if w) == [8, 12, 16, 20, 24, 32], census5)


# ===========================================================================
# G. T=0 exclusion: constructed balanced functions with T=0
# ===========================================================================
def control_G():
    rng = random.Random(152006)
    stats = []
    ok_all = True
    for trial in range(4):
        while True:
            pts = rng.sample(range(SIZE), HALF - 1)
            xs = xor_all(pts)
            if xs not in pts:
                break
        f = [0] * SIZE
        for p in pts + [xs]:
            f[p] = 1
        M = support(f)
        T = xor_all(M)
        k = walsh_k(f)
        all_even = all(v % 2 == 0 for v in k)
        q = [(v // 2) % 2 for v in k]
        dq = degree(q, N)
        w1q = SIZE - sum(q)
        peak = max(abs(v) for v in k)
        z0 = SIZE - sum(q)
        z1 = sum(q)
        bound = 16 * z0 + 36 * z1
        stats.append({"T": T, "all_even": all_even, "deg_q": dq, "wt(1+q)": w1q, "peak_abs_k": peak, "16z0+36z1": bound})
        ok_all &= (T == 0 and all_even and dq <= 2 and w1q >= 128 and peak >= 8 and bound <= 15872)
    record("G1 constructed balanced f with T=0 (4 seeds): all k even, deg q<=2 on F_2^9, wt(1+q)>=128, 16z0+36z1<=15872<16384, peak |k|>=8", ok_all, stats)
    # structured boundary example: g bent (x0x1+x2x3+x4x5+x6x7) xor x8 -> T=0, peak exactly 32 (|k|=8): T=0 exclusion is sharp at peak 28
    f = [0] * SIZE
    for x in range(SIZE):
        g = ((x >> 0) & (x >> 1) ^ (x >> 2) & (x >> 3) ^ (x >> 4) & (x >> 5) ^ (x >> 6) & (x >> 7)) & 1
        f[x] = g ^ ((x >> 8) & 1)
    M = support(f)
    T = xor_all(M)
    k = walsh_k(f)
    vals = sorted(set(k))
    record("G2 structured example g_bent xor x8: balanced, T=0, k in {0,+-8}, peak |k|=8 (=32 Walsh), 256 zeros", len(M) == 256 and T == 0 and vals == [-8, 0, 8] and k.count(0) == 256, {"T": T, "values": vals, "zeros": k.count(0)})
    record("G3neg structured peak-32 function: q=0 can have k=+-8, so q-zero square bound 16 used at peak<=28 fails", any(v*v > 16 and (v//2)%2 == 0 for v in k), kind="negative")
    # negative: random balanced f with T != 0 has odd k somewhere (global q undefined)
    f = random_balanced(rng)
    k = walsh_k(f)
    T = xor_all(support(f))
    record("G4neg random balanced f with T!=0: some k odd, global q undefined (T=0 hypothesis load-bearing)", T != 0 and any(v % 2 for v in k), {"T": T}, kind="negative")
    # min-support lemma induction step check for small n: wt(p0)+wt(p0+p1) >= wt(p1) is the triangle inequality; checked for all pairs of 3-var functions
    ok = True
    for p0 in range(256):
        for p1 in range(256):
            ok &= popcount(p0) + popcount(p0 ^ p1) >= popcount(p1)
    record("G5 triangle inequality wt(p0)+wt(p0+p1)>=wt(p1) for all 3-variable pairs (lemma induction step)", ok)


# ===========================================================================

def verify_receipt_pins():
    from pathlib import Path
    root = Path(__file__).resolve().parent
    mp = root / "manifest-v1.json"
    raw = mp.read_bytes()
    mh = hashlib.sha256(raw).hexdigest()
    assert mh == "8f10719b5e86f5198f79d3e1ad055169d0566489c2adb87584a528ac19a32f27"
    m = json.loads(raw)
    pins = []
    for item in m["inputs_in_read_order"]:
        blob = Path(item["path"]).read_bytes()
        observed = {"path": item["path"], "sha256": hashlib.sha256(blob).hexdigest(),
                    "bytes": len(blob), "LF": blob.count(b"\n")}
        for key in ("sha256", "bytes", "LF"):
            assert observed[key] == item[key], (key, observed, item)
        pins.append(observed)
    RESULTS["input_pins"] = {"manifest_sha256": mh, "inputs_in_order": pins}


def control_H():
    # Genuine structured 9-variable example. Baseline = 8-variable hyperbolic
    # bent form xor x8. Toggle 8 linearly independent points with 4 ones and
    # 4 zeros. This preserves weight 256 and generates a rank-six even q.
    f0 = [sum(((x >> i) & 1) * ((x >> (i + 1)) & 1) for i in (0, 2, 4, 6)) % 2 ^ ((x >> 8) & 1)
          for x in range(SIZE)]
    pts = [(1 << i) ^ (256 if i < 4 else 0) for i in range(8)]
    f = list(f0)
    before_bits = [f[p] for p in pts]
    for p in pts:
        f[p] ^= 1
    k = walsh_k(f)
    T = xor_all(support(f))
    E = EvenHalf(k, T)
    R = E.rad
    RESULTS["examples"]["structured_eight_toggles"] = {
        "truth_table_sha256": hashlib.sha256(bytes(f)).hexdigest(),
        "definition": "f0=sum(x[2i]*x[2i+1],i=0..3) xor x8; toggle e_i+e8 for i<4, e_i for 4<=i<8",
        "toggled_points": pts, "T": T, "rank": E.rank, "rad_alpha": R,
        "q_zero_count": E.q.count(0), "peak_abs_k": max(abs(v) for v in k),
        "walsh_zeros": k.count(0), "radical_values_k": [k[E.a_of[r]] for r in R],
    }
    ok = sum(before_bits) == 4 and sum(f) == 256 and T != 0 and E.rank == 6 and len(R) == 4 and all(E.q[r] == 0 for r in R)
    record("H1 structured actual balanced f: 8 point toggles, T!=0, rank B=6, |R|=4, q|R=0", ok, RESULTS["examples"]["structured_eight_toggles"])
    lam, rho = {}, {}
    okphase = True
    for r in R:
        ds = [((k[E.a_of[x ^ r]] - k[E.a_of[x]]) // 4) % 2 for x in range(HALF)]
        poss = [v for v in (0, 1) if ds == [v * E.q[x] for x in range(HALF)]]
        if len(poss) != 1:
            okphase = False
            continue
        lam[r] = poss[0]
        vals = {E.Q[x ^ r] ^ E.Q[x] for x in range(HALF)}
        if len(vals) != 1:
            okphase = False
            continue
        rho[r] = vals.pop()
    okphase &= len(lam) == len(rho) == 4
    okphase &= all(lam[r ^ s] == lam[r] ^ lam[s] and rho[r ^ s] == rho[r] ^ rho[s] for r in R for s in R)
    okphase &= all((k[E.a_of[x ^ r]] - k[E.a_of[x]] - 4 * lam[r] * E.q[x]) % 8 == 0 for x in range(HALF) for r in R)
    record("H2 on structured actual f, (10) holds with unique linear lambda and odd rho", okphase, {"lambda": lam, "rho": rho})
    record("H3neg structured actual f has lambda=rho!=0 but violates peak<=28 and Z=R: theorem is not universal", lam == rho and any(lam.values()) and max(abs(v) for v in k) > 7 and any(k[E.a_of[r]] != 0 for r in R), kind="negative")
    # Check genuine input translations (recompute Walsh from translated truth
    # tables) rather than just relabel signs in an array.
    chosen = [0]
    # Include one representative for each radical character plus 12 others.
    r1, r2 = [r for r in R if r][:2]
    chseen = set()
    for t in range(SIZE):
        ch = (dot(E.a_of[r1], t), dot(E.a_of[r2], t))
        if ch not in chseen:
            chosen.append(t)
            chseen.add(ch)
    rng = random.Random(152007)
    chosen += rng.sample(range(SIZE), 12)
    chosen = list(dict.fromkeys(chosen))
    okt = True
    norm_case = None
    for t in chosen:
        ft = [f[x ^ t] for x in range(SIZE)]
        kt = walsh_k(ft)
        Et = EvenHalf(kt, T)
        okt &= xor_all(support(ft)) == T
        okt &= kt == [(-1) ** dot(a, t) * k[a] for a in range(SIZE)]
        okt &= Et.q == E.q
        for r in R:
            psi = dot(E.a_of[r], t)
            okt &= all((kt[E.a_of[x ^ r]] - kt[E.a_of[x]] - 4 * (lam[r] ^ psi) * Et.q[x]) % 8 == 0 for x in range(HALF))
            okt &= {Et.Q[x ^ r] ^ Et.Q[x] for x in range(HALF)} == {rho[r] ^ psi}
        if all(dot(E.a_of[r], t) == rho[r] for r in R):
            norm_case = {"t": t, "weight_Q_t": sum(Et.Q), "all_rho_t_zero": all({Et.Q[x ^ r] ^ Et.Q[x] for x in range(HALF)} == {0} for r in R)}
    record("H4 structured f: genuine input translations recompute Walsh and obey lambda_t=lambda+psi, rho_t=rho+psi", okt, {"translations_tested": chosen})
    record("H5 structured f: a translation with psi=rho has rho_t=0 and wt(Q_t) in {112,144}", norm_case is not None and norm_case["all_rho_t_zero"] and norm_case["weight_Q_t"] in (112, 144), norm_case)
    # The original <=28 constants deliberately fail when applied outside
    # their caller: identify concrete actual fibers where the bound fails.
    R9 = [E.a_of[r] for r in R]
    chi = [(-1) ** lam[r] for r in R]
    seen = set()
    violations = []
    zero_fiber_energy = None
    for a in range(SIZE):
        if a in seen:
            continue
        F = [a ^ r for r in R9]
        seen.update(F)
        energy = sum(k[b] * k[b] for b in F)
        s2 = sum(chi[i] * k[a ^ r] for i, r in enumerate(R9)) ** 2
        if a == 0:
            zero_fiber_energy = energy
            continue
        if dot(a, T):
            typ, const = "odd", 1464
        elif E.q[E.al_of[a]]:
            typ, const = "q-one", 864
        else:
            typ, const = "q-zero", 640
        if s2 < 10 * energy - const:
            violations.append({"a": a, "type": typ, "k_fiber": [k[b] for b in F], "10E-S2": 10 * energy - s2, "constant": const})
    record("H6neg applying the <=28 fiber constants to structured outside-scope f fails on actual fibers; radical fiber not zero", len(violations) > 0 and zero_fiber_energy > 0, {"zero_fiber_E": zero_fiber_energy, "violation_count": len(violations), "first_violation": violations[0] if violations else None}, kind="negative")


def main():
    t0 = receipts_begin()
    print("clock_before:", t0)
    start = time.time()
    verify_receipt_pins()
    control_A()
    control_B()
    control_C()
    control_D()
    control_E()
    control_F()
    control_G()
    control_H()
    t1 = receipts_begin()
    elapsed = time.time() - start
    RESULTS["clock_before"] = t0
    RESULTS["clock_after"] = t1
    RESULTS["elapsed_s"] = round(elapsed, 2)
    RESULTS["python"] = sys.version.split()[0]
    RESULTS["numpy"] = np.__version__
    with open(__file__, "rb") as fh:
        RESULTS["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    pos = [c for c in RESULTS["checks"] if c["kind"] == "positive"]
    neg = [c for c in RESULTS["checks"] if c["kind"] == "negative"]
    RESULTS["summary"] = {
        "positive_total": len(pos), "positive_pass": sum(c["pass"] for c in pos),
        "negative_total": len(neg), "negative_pass": sum(c["pass"] for c in neg),
        "all_pass": all(c["pass"] for c in RESULTS["checks"] if c["kind"] != "info"),
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reviewer-f152-controls-v1-result.json")
    with open(out, "w") as fh:
        json.dump(RESULTS, fh, indent=1, default=str)
    print("clock_after:", t1, "elapsed", round(elapsed, 1), "s")
    print(json.dumps(RESULTS["summary"]))


if __name__ == "__main__":
    main()
