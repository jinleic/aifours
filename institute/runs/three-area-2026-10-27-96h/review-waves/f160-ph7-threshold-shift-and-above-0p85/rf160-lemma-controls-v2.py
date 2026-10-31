#!/usr/bin/env python3
"""rf160-lemma-controls-v2.py -- reviewer ReviewF160Threshold, wave f160.

v2 of rf160-lemma-controls.py (v1 and its log are retained unchanged).  v1's
negative control S- (projector r r^T/(r^T r)) was ILL-POSED: by the matrix
determinant lemma / Brauer's rank-one theorem, det((y+t)I-G-t r w^T/(w^T r)) =
C(y+t)*y/(y+t) for EVERY w with w^T r != 0, because G r = 0 alone fixes the
shifted spectrum; v1 therefore stopped (correctly) when that 'negative' passed.
v2 records that variant as a positive robustness check and replaces the
negative by two controls that fail for intended reasons.

Independently authored exact controls (no author code):
  S+  Lemma S on seeded random rational irreducible Metzler 7x7 matrices with G r = 0:
      exact left Perron vector, P^2=P, GP=PG=0, off-diagonal of G_t positive,
      G_t r = 0, l^T G_t = 0, and the exact polynomial identity
      (y+t) det(yI-G_t) = y det((y+t)I-G); plus the symbolic ratio map
      z -> z/(1+t)^2 after rescaling by 1+t.
  S+b Brauer variant: the identity also holds with r w^T/(w^T r), w = r and w = 1.
  S-a rank-one term built on a vector NOT in ker G (the all-ones vector):
      the identity must fail.
  S-b t = -1/10 (an upward shift in z): the Metzler sign pattern must fail at a
      zero off-diagonal entry of G.
  L5+ Lemma 3 / Lemma 5 coefficient extraction from the cover identity on seeded
      random rational 7x7 Metzler matrices whose bidirected pairs have square
      products (so S and every omega are rational): exact equality of the
      y^6..y^2 coefficients, and of the full cover identity.
  L5- dropping the 5-state term C5 (or using tr instead of e2 for 3-cycles)
      must break the y^2 identity.
  Floating diagnostics (not exact, not premises): interlacing-direction
      inequalities and the Lemma 5 inequality on the same matrices.
A log is written as rf160-lemma-controls-v2-log.txt next to this script.
"""
import itertools, math, random, sys, time
from fractions import Fraction as Fr
import numpy as np

RD = '/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f160-ph7-threshold-shift-and-above-0p85/'
LINES = []


def log(*a):
    s = ' '.join(str(t) for t in a)
    print(s, flush=True)
    LINES.append(s)


def check(cond, msg):
    if not cond:
        log('FAIL:', msg)
        open(RD + 'rf160-lemma-controls-v2-log.txt', 'w').write('\n'.join(LINES) + '\n')
        raise SystemExit(1)


# ---------------- exact linear algebra over Fractions
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), Fr(0)) for j in range(p)] for i in range(n)]


def ident(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def charpoly(M):
    """Faddeev-LeVerrier: list c with det(yI-M) = sum_k c[k] y^k, c[n] = 1."""
    n = len(M)
    c = [Fr(0)] * (n + 1)
    c[n] = Fr(1)
    Mk = [[Fr(0)] * n for _ in range(n)]
    I = ident(n)
    for k in range(1, n + 1):
        MM = matmul(M, Mk)
        Mk = [[MM[i][j] + c[n - k + 1] * I[i][j] for j in range(n)] for i in range(n)]
        AM = matmul(M, Mk)
        c[n - k] = -sum(AM[i][i] for i in range(n)) / k
    return c


def det(M):
    M = [row[:] for row in M]
    n = len(M)
    d = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            d = -d
        d *= M[col][col]
        for r in range(col + 1, n):
            f = M[r][col] / M[col][col]
            if f:
                for j in range(col, n):
                    M[r][j] -= f * M[col][j]
    return d


def nullspace(M):
    """basis of {v : M v = 0} over Q (reduced row echelon)."""
    M = [row[:] for row in M]
    n, m = len(M), len(M[0])
    pivots, r = [], 0
    for col in range(m):
        piv = next((i for i in range(r, n) if M[i][col] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][col]
        M[r] = [v / pv for v in M[r]]
        for i in range(n):
            if i != r and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivots.append(col)
        r += 1
    free = [j for j in range(m) if j not in pivots]
    basis = []
    for fj in free:
        v = [Fr(0)] * m
        v[fj] = Fr(1)
        for i, pc in enumerate(pivots):
            v[pc] = -M[i][fj]
        basis.append(v)
    return basis


def poly_eval(c, y):
    return sum((ck * Fr(y) ** k for k, ck in enumerate(c)), Fr(0))


def poly_mul(a, b):
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_shift(c, t):
    """coefficients of c(y+t)."""
    out = [Fr(0)] * len(c)
    for k, ck in enumerate(c):
        for m in range(k + 1):
            out[m] += ck * math.comb(k, m) * Fr(t) ** (k - m)
    return out


def strongly_connected(Adj):
    n = len(Adj)
    for s in range(n):
        seen, stack = {s}, [s]
        while stack:
            u = stack.pop()
            for v in range(n):
                if Adj[u][v] != 0 and v not in seen:
                    seen.add(v)
                    stack.append(v)
        if len(seen) < n:
            return False
    return True


# ---------------- S: Lemma S
def lemma_s(rng, trials=6):
    log('== S. Lemma S exact controls ==')
    n = 7
    for trial in range(trials):
        while True:
            K = [[Fr(0)] * n for _ in range(n)]
            dens = rng.choice([0.3, 0.45, 0.6])
            for i in range(n):
                for j in range(n):
                    if i != j and rng.random() < dens:
                        K[i][j] = Fr(rng.randint(1, 9), rng.randint(1, 5))
            if strongly_connected(K):
                break
        r = [Fr(rng.randint(1, 9), rng.randint(1, 4)) for _ in range(n)]
        G = [row[:] for row in K]
        for i in range(n):
            G[i][i] = -sum((K[i][j] * r[j] for j in range(n) if j != i), Fr(0)) / r[i]
        check(all(sum((G[i][j] * r[j] for j in range(n)), Fr(0)) == 0 for i in range(n)), 'G r = 0')
        GT = [[G[j][i] for j in range(n)] for i in range(n)]
        ns = nullspace(GT)
        check(len(ns) == 1, 'left kernel one-dimensional (simple Perron root 0)')
        l = ns[0]
        if l[0] < 0:
            l = [-v for v in l]
        check(all(v > 0 for v in l), 'left Perron vector positive')
        lr = sum((a * b for a, b in zip(l, r)), Fr(0))
        P = [[r[i] * l[j] / lr for j in range(n)] for i in range(n)]
        check(matmul(P, P) == P, 'P^2 = P')
        Z = [[Fr(0)] * n for _ in range(n)]
        check(matmul(G, P) == Z and matmul(P, G) == Z, 'GP = PG = 0')
        t = Fr(rng.choice([1, 3, 7, 13]), 10)
        Gt = [[G[i][j] + t * (P[i][j] - (1 if i == j else 0)) for j in range(n)] for i in range(n)]
        check(all(Gt[i][j] > 0 for i in range(n) for j in range(n) if i != j), 'off-diagonal of G_t positive')
        check(all(Gt[i][j] >= G[i][j] for i in range(n) for j in range(n) if i != j), 'G_t >= G off the diagonal')
        check(all(sum((Gt[i][j] * r[j] for j in range(n)), Fr(0)) == 0 for i in range(n)), 'G_t r = 0')
        check(all(sum((l[i] * Gt[i][j] for i in range(n)), Fr(0)) == 0 for j in range(n)), 'l^T G_t = 0')
        C = charpoly(G)
        Ct = charpoly(Gt)
        for yv in (Fr(0), Fr(1, 3), Fr(-2), Fr(5, 7)):
            check(poly_eval(C, yv) == det([[yv * (i == j) - G[i][j] for j in range(n)] for i in range(n)]), 'charpoly check')
        check(C[0] == 0 and C[1] != 0, 'C(0)=0, simple root')
        lhs = poly_mul([t, Fr(1)], Ct)                 # (y+t) C_t(y)
        rhs = poly_mul([Fr(0), Fr(1)], poly_shift(C, t))  # y C(y+t)
        check(lhs == rhs, '(y+t) det(yI-G_t) = y det((y+t)I-G)')
        nonP = np.linalg.eigvals(np.array([[float(v) for v in row] for row in G]))
        nonPt = np.linalg.eigvals(np.array([[float(v) for v in row] for row in Gt]))
        log('S+ trial %d: density %.2f, t=%s: l>0 exact, P^2=P, GP=PG=0, off-diag(G_t)>0, G_t r=0, l^T G_t=0, '
            '(y+t)C_t(y)=yC(y+t) EXACT PASS; float diag max Re eig G=%.2e, G_t=%.2e'
            % (trial, dens, t, max(nonP.real), max(nonPt.real)))
        # S+b: Brauer variant (w = r and w = 1) -- the identity only needs G r = 0
        one = [Fr(1)] * n
        for wname, wv in (('w=r', r), ('w=1', one)):
            wr = sum((a * b for a, b in zip(wv, r)), Fr(0))
            Pw = [[r[i] * wv[j] / wr for j in range(n)] for i in range(n)]
            Gw = [[G[i][j] + t * (Pw[i][j] - (1 if i == j else 0)) for j in range(n)] for i in range(n)]
            check(poly_mul([t, Fr(1)], charpoly(Gw)) == rhs, 'S+b Brauer variant %s' % wname)
            check(all(Gw[i][j] > 0 for i in range(n) for j in range(n) if i != j), 'S+b off-diagonal positive %s' % wname)
        # S-a: rank-one term on a vector outside ker G
        if any(sum((G[i][j] for j in range(n)), Fr(0)) != 0 for i in range(n)):
            Pb = [[Fr(1, n)] * n for _ in range(n)]
            Gb = [[G[i][j] + t * (Pb[i][j] - (1 if i == j else 0)) for j in range(n)] for i in range(n)]
            lhsb = poly_mul([t, Fr(1)], charpoly(Gb))
            check(lhsb != rhs, 'S-a identity must fail for a rank-one term on a vector outside ker G')
            sa = 'FAILS as intended'
        else:
            sa = 'skipped (ones vector happens to lie in ker G)'
        # S-b: negative t breaks the Metzler sign pattern where G_ij = 0
        zeros = [(i, j) for i in range(n) for j in range(n) if i != j and G[i][j] == 0]
        tn = Fr(-1, 10)
        Gn = [[G[i][j] + tn * (P[i][j] - (1 if i == j else 0)) for j in range(n)] for i in range(n)]
        if zeros:
            check(all(Gn[i][j] < 0 for (i, j) in zeros), 'S-b negative t must break the sign pattern at zero entries')
            sb = 'Metzler pattern FAILS at all %d zero off-diagonal entries as intended' % len(zeros)
        else:
            sb = 'skipped (G has no zero off-diagonal entry)'
        log('   S+b Brauer variants w=r, w=1: identity EXACT PASS (left vector not essential); S-a ones-vector rank-one term: '
            'identity %s; S-b t=-1/10: %s' % (sa, sb))
    # symbolic ratio map: z = (1+t)^2 z'
    # C(y) = y[(y+1)^2+z]^2 (y^2+q1 y+q0);  y*C(y+t)/(y+t) at y->(1+t)y  ==  (1+t)^5 y [(y+1)^2+z']^2 Qhat(y)
    rng2 = random.Random(7)
    for _ in range(5):
        t = Fr(rng2.randint(1, 30), 10)
        zp = Fr(rng2.randint(1, 99), 100)
        q1 = Fr(rng2.randint(1, 50), 10)
        q0 = Fr(rng2.randint(1, 50), 10)
        z = (1 + t) ** 2 * zp
        quad = lambda yy, zz: (yy + 1) ** 2 + zz
        for yv in [Fr(k, 7) for k in range(-6, 9)]:
            Y = (1 + t) * yv
            lhs = Y * quad(Y + t, z) ** 2 * ((Y + t) ** 2 + q1 * (Y + t) + q0)
            qhat = ((1 + t) * yv + t) ** 2 + q1 * ((1 + t) * yv + t) + q0
            rhs = (1 + t) ** 5 * yv * quad(yv, zp) ** 2 * qhat
            check(lhs == rhs, 'ratio map')
    log('S+ ratio map: after the shift and rescaling by 1+t the double factor becomes [(y+1)^2+z/(1+t)^2]^2 '
        '(exact at 5x15 rational sample points of a degree-7 identity in y, 5 parameter sets): PASS')


# ---------------- L5: cover identity coefficients
def directed_cycles(G):
    n = len(G)
    cyc = []
    for s in range(n):
        stack = [(s, [s])]
        while stack:
            u, path = stack.pop()
            for v in range(n):
                if v == u or G[u][v] == 0:
                    continue
                if v == s and len(path) >= 2:
                    cyc.append(tuple(path))
                elif v > s and v not in path:
                    stack.append((v, path + [v]))
    return cyc


def principal(M, U):
    return [[M[i][j] for j in U] for i in U]


def lemma5(rng, trials=8):
    log('== L5. Lemma 3 / Lemma 5 coefficient extraction (exact) ==')
    n = 7
    stats = []
    for trial in range(trials):
        G = [[Fr(0)] * n for _ in range(n)]
        dens = rng.choice([0.35, 0.5, 0.65, 0.8])
        for i in range(n):
            for j in range(i + 1, n):
                u = rng.random()
                if u < dens * 0.6:                 # bidirected pair with square product
                    a = Fr(rng.randint(1, 6), rng.randint(1, 3))
                    k = Fr(rng.randint(1, 5), rng.randint(1, 4))
                    if rng.random() < 0.5:
                        G[i][j], G[j][i] = a, a * k * k
                    else:
                        G[j][i], G[i][j] = a, a * k * k
                elif u < dens:                     # one-way edge
                    a = Fr(rng.randint(1, 6), rng.randint(1, 3))
                    if rng.random() < 0.5:
                        G[i][j] = a
                    else:
                        G[j][i] = a
        for i in range(n):
            G[i][i] = -Fr(rng.randint(20, 60), 1)   # strongly negative: -S positive definite (float diag)
        S = [[Fr(0)] * n for _ in range(n)]
        for i in range(n):
            S[i][i] = G[i][i]
            for j in range(n):
                if i != j and G[i][j] != 0 and G[j][i] != 0:
                    prod = G[i][j] * G[j][i]
                    num, den = math.isqrt(prod.numerator), math.isqrt(prod.denominator)
                    check(num * num == prod.numerator and den * den == prod.denominator, 'square product')
                    S[i][j] = Fr(num, den)
        A = [[-v for v in row] for row in S]
        cycles = [c for c in directed_cycles(G) if len(c) >= 3]
        extra = []                                   # (vertex set, omega)
        virt = {}
        for c in cycles:
            edges = list(zip(c, c[1:] + c[:1]))
            w = Fr(1)
            for (i, j) in edges:
                w *= G[i][j]
            if any(G[j][i] == 0 for (i, j) in edges):
                extra.append((frozenset(c), w))       # one-way cycle
            else:
                rev = (c[0],) + tuple(reversed(c[1:]))
                key = min(c, rev)
                virt.setdefault(key, []).append((c, w))
        nvirt = 0
        for key, lst in virt.items():
            check(len(lst) == 2, 'both orientations of a bidirected cycle present')
            s_ = Fr(1)
            for (i, j) in zip(key, key[1:] + key[:1]):
                s_ *= S[i][j]
            wp, wm = lst[0][1], lst[1][1]
            check(wp * wm == s_ * s_, 's_Gamma^2 = w+ w-')
            extra.append((frozenset(key), wp + wm - 2 * s_))   # (sqrt w+ - sqrt w-)^2
            nvirt += 1
        CG = charpoly(G)
        CS = charpoly(S)                       # det(yI-S) = det(yI+A) = prod (y+v_k)
        e = {k: CS[n - k] for k in range(n + 1)}
        def sub_cp(U):
            return charpoly(principal(S, U)) if U else [Fr(1)]
        W = sum((om for vs, om in extra if len(vs) == 3), Fr(0))
        C4 = sum((om for vs, om in extra if len(vs) == 4), Fr(0))
        C5 = sum((om for vs, om in extra if len(vs) == 5), Fr(0))
        T3 = Fr(0)
        E2_3 = Fr(0)
        T4 = Fr(0)
        for vs, om in extra:
            U = [i for i in range(n) if i not in vs]
            if len(vs) == 3:
                cp = sub_cp(U)                 # degree 4
                T3 += om * cp[3]               # tr(A_U)
                E2_3 += om * cp[2]             # e2(A_U)
            elif len(vs) == 4:
                cp = sub_cp(U)                 # degree 3
                T4 += om * cp[2]               # tr(A_U)
        check(CG[6] == e[1] and CG[5] == e[2], '[y^6]=e1, [y^5]=e2')
        check(CG[4] == e[3] - W, '[y^4]=e3-W')
        check(CG[3] == e[4] - T3 - C4, '[y^3]=e4-T3-C4')
        check(CG[2] == e[5] - E2_3 - T4 - C5, 'Lemma 5: [y^2]=e5-sum omega e2(A_U)-sum omega tr(A_U)-C5')
        # full cover identity (sets of pairwise disjoint extra cycles; at most two fit in 7 states)
        total = list(CS)
        for vs, om in extra:
            U = [i for i in range(n) if i not in vs]
            cp = sub_cp(U)
            for k, ck in enumerate(cp):
                total[k] -= om * ck
        for (v1, o1), (v2, o2) in itertools.combinations(extra, 2):
            if v1 & v2:
                continue
            U = [i for i in range(n) if i not in v1 and i not in v2]
            cp = sub_cp(U)
            for k, ck in enumerate(cp):
                total[k] += o1 * o2 * ck
        check(total == CG, 'full cover identity')
        # negatives
        bad1 = CG[2] == e[5] - E2_3 - T4            # C5 dropped
        bad2 = CG[2] == e[5] - T3 - T4 - C5         # tr instead of e2 for 3-cycles
        # floating diagnostics of the inequalities
        Af = np.array([[float(v) for v in row] for row in A])
        ev = np.sort(np.linalg.eigvalsh(Af))
        pd = ev[0] > 0
        m2 = sum(ev[i] * ev[j] for i, j in itertools.combinations(range(4), 2))
        S3 = ev[:3].sum()
        L4 = ev[3:].sum()
        ok_int, viol_rev = True, 0
        for vs, om in extra:
            U = [i for i in range(n) if i not in vs]
            mu = np.sort(np.linalg.eigvalsh(Af[np.ix_(U, U)]))
            if len(vs) == 3:
                e2U = sum(mu[i] * mu[j] for i, j in itertools.combinations(range(4), 2))
                ok_int &= e2U >= m2 - 1e-9 and mu.sum() <= L4 + 1e-9
                viol_rev += mu.sum() < L4 - 1e-9   # the reversed direction tr(A_U)>=L4 fails here
            elif len(vs) == 4:
                ok_int &= mu.sum() >= S3 - 1e-9
        E2v = float(e[5] - CG[2])
        E3v = float(e[4] - CG[3])
        E4v = float(W)
        lem5 = E2v >= E4v * m2 + S3 * max(0.0, E3v - E4v * L4) - 1e-6 * max(1.0, abs(E2v))
        stats.append((len(extra), nvirt, float(C5) != 0.0, bad1, bad2, pd, ok_int, lem5, viol_rev))
        log('L5+ trial %d: density %.2f, %d extra cycles (%d virtual), C5=%s: [y^6..y^2] and the FULL cover identity '
            'EXACT PASS | L5- C5 dropped -> %s, tr-for-e2 -> %s | float diag: A pd=%s, interlacing ineqs=%s, '
            'Lemma 5 ineq=%s, reversed-direction violations=%d'
            % (trial, dens, len(extra), nvirt, 'nonzero' if C5 != 0 else '0',
               'identity FAILS' if not bad1 else 'identity holds', 'identity FAILS' if not bad2 else 'identity holds',
               pd, ok_int, lem5, viol_rev))
    check(any(s[2] and not s[3] for s in stats), 'L5- C5-drop negative must fail on some trial with C5 != 0')
    check(any(not s[4] for s in stats), 'L5- tr-for-e2 negative must fail')
    check(all(s[6] and s[7] for s in stats if s[5]), 'float diagnostics')


if __name__ == '__main__':
    t0 = time.time()
    log('rf160-lemma-controls-v2 python=%s numpy=%s' % (sys.version.split()[0], np.__version__))
    lemma_s(random.Random(160))
    lemma5(random.Random(2026))
    log('RESULT: Lemma S exact controls PASS (S-a/S-b negatives FAIL as intended); Lemma 3/5 coefficient '
        'controls EXACT PASS (negatives FAIL as intended) (%.1fs)' % (time.time() - t0))
    open(RD + 'rf160-lemma-controls-v2-log.txt', 'w').write('\n'.join(LINES) + '\n')
