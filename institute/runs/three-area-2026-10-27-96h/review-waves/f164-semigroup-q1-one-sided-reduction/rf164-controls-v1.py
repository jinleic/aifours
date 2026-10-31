#!/usr/bin/env python3
"""rf164-controls-v1.py

Independent exact controls for review wave f164-semigroup-q1-one-sided-reduction.
Reviewer: ReviewF164SemigroupQ1 (same-harness).  Written from scratch by the
reviewer; it imports, reads or executes NO author code and NO author data.

Usage:  python3 -B rf164-controls-v1.py <logfile>

Exit status 0 iff every positive control held AND every negative control failed
for its intended reason (lines tagged NEG-*).  Any surprise is printed as
'UNEXPECTED:' and makes the exit status 1.
"""
import sys, itertools, random, time, math
import numpy as np

SEED = 20261029
random.seed(SEED)
LOG = open(sys.argv[1], "w", encoding="utf-8") if len(sys.argv) > 1 else None
UNEXPECTED = []
T0 = time.time()


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def expect(cond, msg):
    if not cond:
        UNEXPECTED.append(msg)
        log("UNEXPECTED:", msg)
    return bool(cond)


# ======================================================================
# 1. Generic finite-semigroup machinery (tables T[a][b] = a*b)
# ======================================================================
def label(keys):
    d, out = {}, []
    for k in keys:
        if k not in d:
            d[k] = len(d)
        out.append(d[k])
    return out


def is_assoc(T):
    A = np.asarray(T, dtype=np.int64)
    for a in range(A.shape[0]):
        if not np.array_equal(A[A[a]], A[a][A]):      # (ab)c == a(bc) for all b,c
            return False
    return True


def transpose(T):
    n = len(T)
    return [[T[b][a] for b in range(n)] for a in range(n)]


def adjoin1(T):
    n = len(T)
    U = [list(r) + [a] for a, r in enumerate(T)]
    U.append(list(range(n)) + [n])
    return U


def cong_gen(T, pairs):
    """Least congruence containing `pairs` (union-find + two-sided translate closure)."""
    n = len(T)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    cols = [[T[s][a] for s in range(n)] for a in range(n)]
    stack = list(pairs)
    while stack:
        a, b = stack.pop()
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        parent[ra] = rb
        Ta, Tb, ca, cb = T[a], T[b], cols[a], cols[b]
        for s in range(n):
            stack.append((Ta[s], Tb[s]))
            stack.append((ca[s], cb[s]))
    return label([find(x) for x in range(n)])


def pairs_of(P):
    first, out = {}, []
    for a, c in enumerate(P):
        if c in first:
            out.append((first[c], a))
        else:
            first[c] = a
    return out


def join(T, P, Q):
    return cong_gen(T, pairs_of(P) + pairs_of(Q))


def meet(P, Q):
    return label(list(zip(P, Q)))


def finer(P, Q):
    """P subset-of Q as equivalence relations."""
    m = {}
    for a in range(len(P)):
        if m.setdefault(P[a], Q[a]) != Q[a]:
            return False
    return True


def is_delta(P):
    return len(set(P)) == len(P)


def is_congruence(T, P):
    n, m = len(T), {}
    for a in range(n):
        for b in range(n):
            if m.setdefault((P[a], P[b]), P[T[a][b]]) != P[T[a][b]]:
                return False
    return True


def quotient(T, P):
    k = max(P) + 1
    rep = [None] * k
    for a, c in enumerate(P):
        if rep[c] is None:
            rep[c] = a
    return [[P[T[rep[c]][rep[d]]] for d in range(k)] for c in range(k)], rep


def closure(T, gens):
    S = set(gens)
    frontier = list(S)
    while frontier:
        new, cur = [], list(S)
        for a in frontier:
            Ta = T[a]
            for b in cur:
                for c in (Ta[b], T[b][a]):
                    if c not in S:
                        S.add(c)
                        new.append(c)
        frontier = new
    return sorted(S)


def sub_table(T, Sl):
    ix = {s: i for i, s in enumerate(Sl)}
    return [[ix[T[a][b]] for b in Sl] for a in Sl]


def all_congruences(T):
    n = len(T)
    princ = set()
    for a in range(n):
        for b in range(a + 1, n):
            princ.add(tuple(cong_gen(T, [(a, b)])))
    delta = tuple(range(n))
    seen, frontier = {delta}, [delta]
    while frontier:
        new = []
        for c in frontier:
            for p in princ:
                j = tuple(join(T, list(c), list(p)))
                if j not in seen:
                    seen.add(j)
                    new.append(j)
        frontier = new
    return [list(c) for c in seen]


def automorphisms(T):
    n = len(T)
    return [p for p in itertools.permutations(range(n))
            if all(p[T[a][b]] == T[p[a]][p[b]] for a in range(n) for b in range(n))]


def has_identity(T):
    n = len(T)
    return any(all(T[u][x] == x and T[x][u] == x for x in range(n)) for u in range(n))


class SG:
    def __init__(self, T):
        self.T = T
        n = self.n = len(T)
        self.isE = [T[a][a] == a for a in range(n)]
        self.E = [a for a in range(n) if self.isE[a]]
        self.R = label([frozenset([a] + list(T[a])) for a in range(n)])        # aS^1
        self.L = label([frozenset([a] + [T[s][a] for s in range(n)]) for a in range(n)])  # S^1a
        self.H = meet(self.R, self.L)
        self._V = None

    def V(self):
        if self._V is None:
            T, n = self.T, self.n
            self._V = [[x for x in range(n) if T[T[a][x]][a] == a and T[T[x][a]][x] == x]
                       for a in range(n)]
        return self._V

    def regular(self):
        T, n = self.T, self.n
        return all(any(T[T[a][x]][a] == a for x in range(n)) for a in range(n))

    def leq(self, a, b):
        """Nambooripad order: a = e b = b f for idempotents e, f (possibly different)."""
        T = self.T
        return any(T[e][b] == a for e in self.E) and any(T[b][f] == a for f in self.E)

    def leq_simultaneous(self, a, b):
        """The erratum's WRONG one-witness test e b = b e = a."""
        T = self.T
        return any(T[e][b] == a and T[b][e] == a for e in self.E)

    def weu(self):
        for s in range(self.n):
            if not self.isE[s]:
                for e in self.E:
                    if self.leq(e, s):
                        return False, (e, s)
        return True, None

    def local_band(self, g):
        T = self.T
        return [x for x in self.E if T[T[g][x]][g] == x]

    def simple(self):
        T, n = self.T, self.n
        for v in range(n):
            J = {v} | set(T[v]) | {T[s][v] for s in range(n)}
            J |= {T[T[s][v]][t] for s in range(n) for t in range(n)}
            if len(J) != n:
                return False
        return True


# ---------------- band identities ----------------
def local_monoids(T):
    n = len(T)
    return [[x for x in range(n) if T[T[e][x]][e] == x] for e in range(n)]


def id_regular(T, M):          # abaca = abca  (regular band identity) on M
    for a in M:
        Ta = T[a]
        for b in M:
            ab = Ta[b]
            Tab, Taba = T[ab], T[T[ab][a]]
            for c in M:
                if T[Taba[c]][a] != T[Tab[c]][a]:
                    return False
    return True


def id_left_regular(T, M):     # xyx = xy
    return all(T[T[x][y]][x] == T[x][y] for x in M for y in M)


def id_right_regular(T, M):    # xyx = yx
    return all(T[T[x][y]][x] == T[y][x] for x in M for y in M)


def id_commutative(T, M):
    return all(T[x][y] == T[y][x] for x in M for y in M)


def band_class(T, LM=None):
    if LM is None:
        LM = local_monoids(T)
    full = list(range(len(T)))
    return dict(SN=all(id_regular(T, M) for M in LM),
                LEFTSN=all(id_left_regular(T, M) for M in LM),
                RIGHTSN=all(id_right_regular(T, M) for M in LM),
                regular=id_regular(T, full),
                left_regular=id_left_regular(T, full),
                right_regular=id_right_regular(T, full))


def global_identity(T, kind):
    """kind 'R': exeyexe = eyexe ; kind 'L': exeyexe = exeye   (all e,x,y)."""
    A = np.asarray(T, dtype=np.int64)
    n = A.shape[0]
    ar = np.arange(n)
    EXE = A[A, ar[:, None]]                               # EXE[e,x] = exe
    for e in range(n):
        X = EXE[e]
        lhs = A[A[X[:, None], X[None, :]], X[:, None]]     # (exe)(eye)(exe)
        rhs = A[X[None, :], X[:, None]] if kind == 'R' else A[X[:, None], X[None, :]]
        if not np.array_equal(lhs, rhs):
            return False
    return True


def kimura_pairs(T, S, LM):
    pr, pl = set(), set()
    for e in range(len(T)):
        M = LM[e]
        for i, x in enumerate(M):
            for y in M[i + 1:]:
                if S.R[x] == S.R[y]:
                    pr.add((x, y))
                if S.L[x] == S.L[y]:
                    pl.add((x, y))
    return sorted(pr), sorted(pl)


def kimura_band_check(T, allcong=True, sample_principal=0):
    n = len(T)
    S = SG(T)
    LM = local_monoids(T)
    bc = band_class(T, LM)
    pr, pl = kimura_pairs(T, S, LM)
    lam, rho = cong_gen(T, pr), cong_gen(T, pl)
    r = dict(n=n, cls=bc, npr=len(pr), npl=len(pl), lam=lam, rho=rho,
             nlam=max(lam) + 1, nrho=max(rho) + 1,
             lamR=finer(lam, S.R), rhoL=finer(rho, S.L), meetD=is_delta(meet(lam, rho)),
             lam_cong=is_congruence(T, lam), rho_cong=is_congruence(T, rho))
    QL, _ = quotient(T, lam)
    QR, _ = quotient(T, rho)
    r['QL_LEFTSN'] = band_class(QL)['LEFTSN']
    r['QR_RIGHTSN'] = band_class(QR)['RIGHTSN']
    # Step 1 / Step 2 internals
    s1 = s2 = True
    for e in range(n):
        M = LM[e]
        for x in M:
            for y in M:
                if x == y:
                    continue
                if S.R[x] == S.R[y]:
                    if any(T[T[x][w]][y] != T[T[y][w]][y] for w in M):
                        s1 = False
                    if any(S.R[T[x][z]] != S.R[T[y][z]] for z in range(n)):
                        s2 = False
                if S.L[x] == S.L[y]:
                    if any(T[T[x][w]][y] != T[T[x][w]][x] for w in M):
                        s1 = False
                    if any(S.L[T[z][x]] != S.L[T[z][y]] for z in range(n)):
                        s2 = False
    r['step1'], r['step2'] = s1, s2
    # Step 3: R_M is a congruence on each local monoid M and M/R_M is left regular
    s3 = True
    for e in range(n):
        M = LM[e]
        for x in M:
            for y in M:
                if S.R[x] == S.R[y]:
                    if any(S.R[T[x][z]] != S.R[T[y][z]] or S.R[T[z][x]] != S.R[T[z][y]] for z in M):
                        s3 = False
                if S.R[T[T[x][y]][x]] != S.R[T[x][y]]:
                    s3 = False
    r['step3'] = s3
    # definitional equivalences of LEFTSN/RIGHTSN with the displayed identities
    r['defR'] = (bc['RIGHTSN'] == global_identity(T, 'R'))
    r['defL'] = (bc['LEFTSN'] == global_identity(T, 'L'))
    # Kimura-recovery remark
    r['monoid'] = has_identity(T)
    r['lam_eq_R'] = (lam == label(S.R))
    r['rho_eq_L'] = (rho == label(S.L))
    # section 3(c) chain lemma pairs: comparable, R-, L-pairs
    comp = [(a, b) for a in range(n) for b in range(a + 1, n)
            if (T[a][b] == a and T[b][a] == a) or (T[a][b] == b and T[b][a] == b)
            or S.R[a] == S.R[b] or S.L[a] == S.L[b]]
    congs = []
    if allcong:
        congs = all_congruences(T)
    elif sample_principal:
        allp = [(a, b) for a in range(n) for b in range(a + 1, n)]
        random.shuffle(allp)
        congs = [cong_gen(T, [p]) for p in allp[:sample_principal]]
    mn = qc = cc = True
    nneg = 0
    for th in congs:
        Q, _ = quotient(T, th)
        c = band_class(Q)
        if bc['SN']:
            if c['LEFTSN'] != finer(lam, th) or c['RIGHTSN'] != finer(rho, th):
                mn = False
            if not c['LEFTSN']:
                nneg += 1
            if meet(join(T, lam, th), join(T, rho, th)) != th:
                qc = False
        if all(th[a] != th[b] for (a, b) in comp) != is_delta(th):
            cc = False
    r.update(ncong=len(congs), minimal=mn, quotcompat=qc, chain3c=cc, nonLEFTSN_quotients=nneg)
    return r


# ======================================================================
# 2. Free band (Green-Rees normal form) and the RIGHTSN invariant of the
#    instance-lemma file, both implemented independently
# ======================================================================
def fb_nf(w):
    if len(w) == 0:
        return ()
    c = len(set(w))
    if c == 1:
        return (w[0],)
    seen = set()
    for i, x in enumerate(w):
        if x not in seen:
            seen.add(x)
            if len(seen) == c:
                p0, a0 = w[:i], x
                break
    seen = set()
    for i in range(len(w) - 1, -1, -1):
        x = w[i]
        if x not in seen:
            seen.add(x)
            if len(seen) == c:
                a1, s1 = x, w[i + 1:]
                break
    return (fb_nf(p0), a0, a1, fb_nf(s1))


def build_free_band(k):
    order, rep = [], {}
    for x in range(k):
        nf = fb_nf((x,))
        rep[nf] = (x,)
        order.append(nf)
    changed = True
    while changed:
        changed = False
        cur = list(order)
        for x in cur:
            for y in cur:
                w = rep[x] + rep[y]
                nf = fb_nf(w)
                if nf not in rep:
                    rep[nf] = w
                    order.append(nf)
                    changed = True
    idx = {nf: i for i, nf in enumerate(order)}
    T = [[idx[fb_nf(rep[x] + rep[y])] for y in order] for x in order]
    return order, rep, idx, T


def rsn_nf(w):
    """(first letter, last-new-letter-from-right, nf(suffix after its last occurrence))."""
    if not w:
        return None
    c, seen = len(set(w)), set()
    for i in range(len(w) - 1, -1, -1):
        x = w[i]
        if x not in seen:
            seen.add(x)
            if len(seen) == c:
                return (w[0], x, rsn_nf(w[i + 1:]))


def rsn_rep(t):
    out = []
    while t is not None:
        a, b, t = t
        out.append(a)
        if a != b:
            out.append(b)
    return tuple(out)


def rsn_all(k):
    memo = {}

    def withC(C):
        if C in memo:
            return memo[C]
        if not C:
            return (None,)
        res = []
        for a in sorted(C):
            for b in sorted(C):
                for tail in withC(C - {b}):
                    res.append((a, b, tail))
        memo[C] = tuple(res)
        return memo[C]
    out = []
    for r in range(1, k + 1):
        for C in itertools.combinations(range(k), r):
            out.extend(withC(frozenset(C)))
    return out


def rsn_relabel(t, p):
    if t is None:
        return None
    a, b, tail = t
    return (p[a], p[b], rsn_relabel(tail, p))


# ======================================================================
# 3. Reviewer's explicit host model  T(B,D):  D = M[Z_m; I, Lambda; P],
#    Z_m acting on the band B by sigma^g ;  (b,x)(c,y) = (b * w(x,y).c , xy),
#    w((i,g,l),(j,h,k)) = g + P[l][j].
# ======================================================================
def rees(m, nI, nL, P):
    el = [(i, g, l) for i in range(nI) for g in range(m) for l in range(nL)]
    ix = {x: k for k, x in enumerate(el)}
    T = [[ix[(x[0], (x[1] + P[x[2]][y[0]] + y[1]) % m, y[2])] for y in el] for x in el]
    return el, T


def make_host(B, sigma, Dspec):
    m, nI, nL, P = Dspec
    Del, Dt = rees(m, nI, nL, P)
    nb, nd = len(B), len(Del)
    assert all(sigma[B[a][b]] == B[sigma[a]][sigma[b]] for a in range(nb) for b in range(nb))
    sp = [list(range(nb))]
    for _ in range(1, m):
        sp.append([sigma[x] for x in sp[-1]])
    assert [sigma[x] for x in sp[-1]] == list(range(nb)), "sigma^m != id"
    W = [[(Del[x][1] + P[Del[x][2]][Del[y][0]]) % m for y in range(nd)] for x in range(nd)]
    T = [[B[b][sp[W[x][y]][c]] * nd + Dt[x][y] for c in range(nb) for y in range(nd)]
         for b in range(nb) for x in range(nd)]
    return dict(B=B, sigma=sigma, Dspec=Dspec, Del=Del, Dt=Dt, W=W, sp=sp, nb=nb, nd=nd, T=T)


# ======================================================================
# 4. Source-level analysis (Theorem of the source one-sided reduction note)
# ======================================================================
def wmul(T, *xs):
    """Literal left-to-right product x1 x2 ... xk (no idempotency assumed)."""
    r = xs[0]
    for x in xs[1:]:
        r = T[r][x]
    return r


def instance_identity(T, q):
    """Count triples (e,x,y) with q(exe)=q(e)=q(eye) and the LITERAL words
    e x e y e x e != e y e x e  (e need not be idempotent)."""
    A = np.asarray(T, dtype=np.int64)
    n = A.shape[0]
    qa = np.asarray(q)
    ar = np.arange(n)
    EXE = A[A, ar[:, None]]                      # EXE[e,x] = (e x) e
    tested = viol = 0
    wit = None
    for e in range(n):
        X = EXE[e]
        idx = np.nonzero(qa[X] == qa[e])[0]      # admissible x (and y)
        if len(idx) == 0:
            continue
        Xs = X[idx]
        exeye = A[A[Xs[:, None], idx[None, :]], e]          # [x,y] -> e x e y e
        lhs = A[A[exeye, idx[:, None]], e]                    # ... x e
        rhs = A[A[Xs[None, :], idx[:, None]], e]              # [x,y] -> (e y e) x e
        tested += len(idx) ** 2
        bad = np.argwhere(lhs != rhs)
        if len(bad):
            viol += len(bad)
            if wit is None:
                wit = (e, int(idx[bad[0][0]]), int(idx[bad[0][1]]))
    return tested, viol, wit


def source_pairs(T, S):
    LB = {g: S.local_band(g) for g in S.E}
    pr, pl = set(), set()
    for g, M in LB.items():
        for i, x in enumerate(M):
            for y in M[i + 1:]:
                if S.R[x] == S.R[y]:
                    pr.add((x, y))
                if S.L[x] == S.L[y]:
                    pl.add((x, y))
    return LB, sorted(pr), sorted(pl)


def source_analysis(T, q, deep=True, maxpairs=40, inst_internal=400):
    n = len(T)
    S = SG(T)
    out = dict(n=n, assoc=is_assoc(T), regular=S.regular())
    m, hom = {}, True
    for a in range(n):
        for b in range(n):
            if m.setdefault((q[a], q[b]), q[T[a][b]]) != q[T[a][b]]:
                hom = False
    out['q_hom'] = hom
    labs = sorted(set(q))
    li = {v: i for i, v in enumerate(labs)}
    rep = {}
    for a in range(n):
        rep.setdefault(q[a], a)
    Dtab = [[li[q[T[rep[u]][rep[v]]]] for v in labs] for u in labs]
    out['target_CS'] = is_assoc(Dtab) and SG(Dtab).simple()
    out['nD'] = len(labs)
    out['pure'] = all(T[a][a] == a for a in range(n) if q[T[a][a]] == q[a])
    LB, pr, pl = source_pairs(T, S)
    out['local_regular'] = all(id_regular(T, M) for M in LB.values())
    out['RRL'] = all(id_right_regular(T, M) for M in LB.values())
    out['LRL'] = all(id_left_regular(T, M) for M in LB.values())
    out['original'] = (out['regular'] and hom and out['target_CS'] and out['pure']
                       and out['local_regular'])
    lam, rho = cong_gen(T, pr), cong_gen(T, pl)
    kq = label(q)
    out.update(npr=len(pr), npl=len(pl), lam=lam, rho=rho, nlam=max(lam) + 1, nrho=max(rho) + 1,
               nE=len(S.E))
    out['lam_R'] = finer(lam, S.R)
    out['rho_L'] = finer(rho, S.L)
    out['lam_kerq'] = finer(lam, kq)
    out['rho_kerq'] = finer(rho, kq)
    out['lam_meet_rho'] = is_delta(meet(lam, rho))
    out['H_kerq'] = is_delta(meet(S.H, kq))
    out['weu'] = S.weu()[0]
    out['fibre_formula'] = all(set(LB[e]) == {T[T[e][f]][e] for f in range(n) if q[f] == q[e]}
                               for e in S.E)
    for nm, P, side in (('lam', lam, 'left'), ('rho', rho, 'right')):
        Q, rp = quotient(T, P)
        qq = [q[rp[c]] for c in range(len(Q))]
        SQ = SG(Q)
        ok = is_congruence(T, P) and SQ.regular()
        ok = ok and all(Q[c][c] == c for c in range(len(Q)) if qq[Q[c][c]] == qq[c])
        LBQ = [SQ.local_band(g) for g in SQ.E]
        ok = ok and all(id_regular(Q, M) for M in LBQ)
        f = id_left_regular if side == 'left' else id_right_regular
        out[nm + '_quot_original'] = ok
        out[nm + '_quot_sided'] = all(f(Q, M) for M in LBQ)
        lift = all(any(P[e] == c for e in S.E) for c in SQ.E)
        img = all(set(P[x] for x in LB[e]) == set(SQ.local_band(P[e])) for e in S.E)
        out[nm + '_quot_lift'] = lift and img
        out[nm + '_quot_weu'] = SQ.weu()[0]
        if nm == 'lam':
            out['lam_quot_locinv'] = all(id_commutative(Q, M) for M in LBQ)
    if out['RRL']:
        out['RRL_rho_delta'] = is_delta(rho)
    # duality: S^op has lambda/rho swapped
    To = transpose(T)
    So = SG(To)
    _, pro, plo = source_pairs(To, So)
    out['dual_swap'] = (cong_gen(To, pro) == rho and cong_gen(To, plo) == lam)
    tested, viol, wit = instance_identity(T, q)
    out.update(inst_tested=tested, inst_viol=viol, inst_wit=wit)
    if not out['RRL']:
        # intended reason: a local band E(fSf) that is not right regular gives (f,p,r)
        found = False
        for g, M in LB.items():
            for p_ in M:
                for r_ in M:
                    if T[T[p_][r_]][p_] != T[r_][p_]:
                        e, x, y = g, p_, r_
                        if (q[wmul(T, e, x, e)] == q[e] == q[wmul(T, e, y, e)]
                                and wmul(T, e, x, e, y, e, x, e) != wmul(T, e, y, e, x, e)):
                            found = True
                        break
                if found:
                    break
            if found:
                break
        out['nonRRL_violation_from_local_band'] = found
    if deep:
        V = S.V()
        st1 = True
        for g, M in LB.items():
            Ms = set(M)
            for x in M:
                for y in M:
                    if x == y or S.R[x] != S.R[y]:
                        continue
                    for z in range(n):
                        v = T[g][z]
                        for vp in V[v]:
                            h = T[v][vp]
                            xh, yh, ht = T[x][h], T[y][h], T[T[g][h]][g]
                            ok = (T[x][z] == T[x][v] and S.R[T[x][v]] == S.R[xh] and T[g][h] == h
                                  and q[x] == q[g] and S.isE[xh] and S.isE[yh] and ht in Ms
                                  and T[T[x][h]][y] == T[T[y][h]][y]
                                  and T[xh][yh] == yh and T[yh][xh] == xh
                                  and S.R[T[x][z]] == S.R[T[y][z]])
                            if not ok:
                                st1 = False
        out['step1_internals'] = st1
        st2 = True
        for s in range(n):
            for t in range(n):
                if S.H[s] != S.H[t]:
                    continue
                for s1 in V[s]:
                    cand = [t1 for t1 in V[t] if S.H[t1] == S.H[s1]]
                    if len(cand) != 1:
                        st2 = False
                        continue
                    t1 = cand[0]
                    if T[t][t1] != T[s][s1] or T[t1][t] != T[s1][s]:
                        st2 = False
                    if S.R[T[s1][t]] != S.R[s1]:          # direct: s't R s' without t'
                        st2 = False
        out['step2_internals'] = st2
        cand = [(a, b) for a in range(n) for b in range(a + 1, n) if q[a] == q[b]]
        random.shuffle(cand)
        inj = True
        for (a, b) in cand[:maxpairs]:
            th = cong_gen(T, [(a, b)])
            if not any(th[e] == th[f] for i, e in enumerate(S.E) for f in S.E[i + 1:]):
                inj = False
        out['inj_lemma'] = inj
        out['inj_pairs'] = min(len(cand), maxpairs)
        if out['RRL']:
            # proof internals of the instance lemma on a sample of admissible triples
            ok = True
            cnt = 0
            trip = [(e, x, y) for e in range(n) for x in range(n) for y in range(n)]
            random.shuffle(trip)
            for (e, x, y) in trip:
                if cnt >= inst_internal:
                    break
                exe, eye = T[T[e][x]][e], T[T[e][y]][e]
                if not (q[exe] == q[e] == q[eye]):
                    continue
                cnt += 1
                e1 = V[e][0]
                f = T[e][e1]
                p = T[exe][e1]                                            # p = e x e e'
                r = T[eye][e1]                                            # r = e y e e'
                Mf = set(S.local_band(f))
                prp = T[T[p][r]][p]
                rp = T[r][p]
                ok = ok and S.isE[p] and S.isE[r] and p in Mf and r in Mf and prp == rp
                ok = ok and prp == wmul(T, e, x, e, y, e, x, e, e1) and rp == wmul(T, e, y, e, x, e, e1)
                ok = ok and T[prp][e] == wmul(T, e, x, e, y, e, x, e) and T[rp][e] == wmul(T, e, y, e, x, e)
            out['inst_internals'] = ok
            out['inst_internals_n'] = cnt
    if n <= 12:
        # full congruence lattice: (i) every idempotent-pure congruence theta has H ∩ theta = Delta;
        # (ii) pure + idempotent-separating => Delta (injectivity lemma, arbitrary pure actor);
        # (iii) every theta inside ker q gives an original quotient source.
        # Negative count: non-pure idempotent-separating nontrivial congruences.
        ok1 = ok2 = ok3 = True
        neg = npure = 0
        congs = all_congruences(T)
        for th in congs:
            cls = {}
            for a in range(n):
                cls.setdefault(th[a], []).append(a)
            pure_th = all(all(S.isE[a] for a in c) for c in cls.values() if any(S.isE[a] for a in c))
            sep = all(sum(S.isE[a] for a in c) <= 1 for c in cls.values())
            if pure_th:
                npure += 1
                ok1 = ok1 and is_delta(meet(S.H, th))
                if sep:
                    ok2 = ok2 and is_delta(th)
            elif sep and not is_delta(th):
                neg += 1
            if finer(th, kq):
                Q, rp = quotient(T, th)
                qq = [q[rp[c]] for c in range(len(Q))]
                SQ = SG(Q)
                good = SQ.regular() and all(Q[c][c] == c for c in range(len(Q)) if qq[Q[c][c]] == qq[c])
                good = good and all(id_regular(Q, SQ.local_band(g)) for g in SQ.E)
                ok3 = ok3 and good
        out.update(lat_n=len(congs), lat_pure=npure, lat_H=ok1, lat_inj=ok2, lat_quot=ok3, lat_neg=neg)
    return out


ORIGINAL_KEYS = ['assoc', 'regular', 'q_hom', 'target_CS', 'pure', 'local_regular', 'original',
                 'lam_R', 'rho_L', 'lam_kerq', 'rho_kerq', 'lam_meet_rho', 'H_kerq', 'weu',
                 'fibre_formula', 'lam_quot_original', 'rho_quot_original', 'lam_quot_sided',
                 'rho_quot_sided', 'lam_quot_lift', 'rho_quot_lift', 'lam_quot_weu', 'rho_quot_weu',
                 'dual_swap']


def check_source(name, out, deep=True):
    for k in ORIGINAL_KEYS:
        expect(out[k], f"{name}: {k} failed")
    if deep:
        for k in ('step1_internals', 'step2_internals', 'inj_lemma'):
            expect(out[k], f"{name}: {k} failed")
    if 'lat_n' in out:
        for k in ('lat_H', 'lat_inj', 'lat_quot'):
            expect(out[k], f"{name}: congruence-lattice check {k} failed")
    if out['RRL']:
        expect(out['RRL_rho_delta'], f"{name}: RRL but rho_S != Delta")
        expect(out['lam_quot_locinv'], f"{name}: RRL but S/lambda not locally inverse")
        expect(out['inst_viol'] == 0, f"{name}: instance lemma violated in RRL source {out['inst_wit']}")
        if deep:
            expect(out['inst_internals'], f"{name}: instance-lemma proof internals failed")
    else:
        # NEG-5: dropping RRL must break the instance identity, via a non-right-regular local band
        expect(out['inst_viol'] > 0, f"{name}: NEG-5 non-RRL source satisfies instance identity")
        expect(out['nonRRL_violation_from_local_band'], f"{name}: NEG-5 reason not exhibited")


# ======================================================================
# MAIN
# ======================================================================
def section(t):
    log("")
    log("=" * 78)
    log(t, f"   [t+{time.time() - T0:.1f}s]")
    log("=" * 78)


section("S0. Erratum (natural order uses two idempotent witnesses)")
E4 = [[0, 0, 0, 0], [0, 1, 2, 3], [3, 2, 1, 0], [3, 3, 3, 3]]
S4 = SG(E4)
expect(is_assoc(E4), "erratum table not associative")
expect(S4.E == [0, 1, 3], "erratum table idempotents != {0,1,3}")
expect(S4.regular(), "erratum table not regular")
expect(E4[0][2] == 0 and E4[2][3] == 0 and E4[2][2] == 1, "erratum witness 0=0*2=2*3, 2^2=1 failed")
expect(S4.leq(0, 2), "two-witness order does not give 0<=2")
log("NEG-8 simultaneous one-witness test e2=2e=e finds 0<=2 :", S4.leq_simultaneous(0, 2),
    "(expected False: the wrong test misses it)")
expect(not S4.leq_simultaneous(0, 2), "NEG-8 simultaneous test unexpectedly detects 0<=2")
expect(not any(E4[e][2] == e and E4[2][e] == e for e in S4.E), "erratum: some e has e2=2e=e")
w4 = S4.weu()
log("erratum table WEU (two-witness):", w4)
expect(not w4[0], "erratum table judged WEU")
DSPECS = {
    'D8': (2, 2, 2, [[0, 0], [0, 1]]),
    'D4r': (2, 2, 1, [[0, 1]]),
    'D4c': (2, 1, 2, [[0], [1]]),
    'Z2': (2, 1, 1, [[0]]),
    'Z3': (3, 1, 1, [[0]]),
    'D12': (3, 2, 2, [[0, 0], [0, 1]]),
    'RB22': (1, 2, 2, [[0, 0], [0, 0]]),
}
for nm, spec in DSPECS.items():
    _, Dt = rees(*spec)
    SD = SG(Dt)
    triv = all((not SD.leq(a, b)) or a == b for a in range(SD.n) for b in range(SD.n))
    expect(is_assoc(Dt) and SD.simple() and SD.regular(), f"{nm} is not CS")
    expect(triv, f"natural order on CS {nm} is not equality")
    log(f"CS {nm}: |D|={SD.n}, simple={SD.simple()}, natural order trivial={triv}")
# transformation semigroups generated by <=3 maps on 3 points
maps = list(itertools.product(range(3), repeat=3))
mi = {f: i for i, f in enumerate(maps)}
comp = [[mi[tuple(g[f[x]] for x in range(3))] for g in maps] for f in maps]
subs = set()
for r in (1, 2, 3):
    for gens in itertools.combinations(range(27), r):
        subs.add(frozenset(closure(comp, gens)))
nreg = nweu = nweu_simul = 0
for Sset in subs:
    Tt = sub_table(comp, sorted(Sset))
    St = SG(Tt)
    if St.regular():
        nreg += 1
        if St.weu()[0]:
            nweu += 1
        if all(not St.leq_simultaneous(e, s) for s in range(St.n) if not St.isE[s] for e in St.E):
            nweu_simul += 1
log(f"T3 subsemigroups generated by <=3 maps: distinct={len(subs)}, regular={nreg}, "
    f"WEU(two-witness)={nweu}, 'WEU' under the wrong simultaneous test={nweu_simul}")

section("S1. All bands of order <= 5 (exhaustive labelled enumeration, iso classes)")


def enum_bands(n):
    T = [[-1] * n for _ in range(n)]
    for i in range(n):
        T[i][i] = i
    cells = [(i, j) for i in range(n) for j in range(n) if i != j]
    res = []
    R = range(n)

    def check(i, j):
        v = T[i][j]
        Ti, Tv, Tj = T[i], T[v], T[j]
        for c in R:
            l, jc = Tv[c], Tj[c]
            if l >= 0 and jc >= 0:
                r = Ti[jc]
                if r >= 0 and r != l:
                    return False
        for a in R:
            ai = T[a][i]
            if ai >= 0:
                l, r = T[ai][j], T[a][v]
                if l >= 0 and r >= 0 and l != r:
                    return False
        for a in R:
            Ta = T[a]
            for b in R:
                if Ta[b] == i:
                    bj = T[b][j]
                    if bj >= 0:
                        r = Ta[bj]
                        if r >= 0 and r != v:
                            return False
        for b in R:
            ib = Ti[b]
            if ib < 0:
                continue
            Tb, Tib = T[b], T[ib]
            for c in R:
                if Tb[c] == j:
                    l = Tib[c]
                    if l >= 0 and l != v:
                        return False
        return True

    def rec(k):
        if k == len(cells):
            res.append(tuple(tuple(r) for r in T))
            return
        i, j = cells[k]
        for v in R:
            T[i][j] = v
            if check(i, j):
                rec(k + 1)
        T[i][j] = -1
    rec(0)
    return res


def canon(T):
    n = len(T)
    best, naut = None, 0
    base = tuple(T[a][b] for a in range(n) for b in range(n))
    for p in itertools.permutations(range(n)):
        pinv = [0] * n
        for a in range(n):
            pinv[p[a]] = a
        U = tuple(p[T[pinv[x]][pinv[y]]] for x in range(n) for y in range(n))
        if U == base:
            naut += 1
        if best is None or U < best:
            best = U
    return best, naut


BANDS = []          # iso-class representatives, as lists of lists
for n in range(1, 6):
    lab = enum_bands(n)
    classes = {}
    for T in lab:
        c, _ = canon(T)
        classes.setdefault(c, T)
    reps = []
    orbit_sum = 0
    for c, T in classes.items():
        U = [list(c[a * n:(a + 1) * n]) for a in range(n)]
        expect(is_assoc(U) and all(U[a][a] == a for a in range(n)), "enumerated table not a band")
        _, naut = canon(U)
        orbit_sum += math.factorial(n) // naut
        reps.append(U)
    expect(orbit_sum == len(lab), f"orbit-stabilizer mismatch at n={n}")
    log(f"order {n}: labelled bands={len(lab)}, iso classes={len(reps)}, "
        f"orbit-stabilizer sum={orbit_sum} (== labelled: {orbit_sum == len(lab)})")
    BANDS.extend(reps)

section("S2. Kimura-type theorem on every band of order <= 5 and every B^1 (order <= 6)")
stats = dict(total=0, SN=0, nonSN=0, regular=0, monoid_regular=0, ncong=0, nonLEFTSN_q=0,
             lam_ne_R_regular_nonmonoid=0, nonSN_lamR_fail=0, SN_nonregular=0, with_both=0)
SMALL = []
for B in BANDS:
    SMALL.append(("B", B))
    SMALL.append(("B1", adjoin1(B)))
LZ2_seen = False
for tag, B in SMALL:
    r = kimura_band_check(B, allcong=True)
    stats['total'] += 1
    stats['ncong'] += r['ncong']
    cls = r['cls']
    expect(r['defR'] and r['defL'], f"definitional identity mismatch for {B}")
    expect(r['chain3c'], f"3(c) chain criterion failed for {B}")
    if cls['SN']:
        stats['SN'] += 1
        if not cls['regular']:
            stats['SN_nonregular'] += 1
        if r['npr'] and r['npl']:
            stats['with_both'] += 1
        for k in ('lamR', 'rhoL', 'meetD', 'lam_cong', 'rho_cong', 'QL_LEFTSN', 'QR_RIGHTSN',
                  'step1', 'step2', 'step3', 'minimal', 'quotcompat'):
            expect(r[k], f"Kimura {k} failed for SN band {B}")
        stats['nonLEFTSN_q'] += r['nonLEFTSN_quotients']
        # characteristic: automorphisms preserve lambda, rho
        for p in automorphisms(B):
            for P in (r['lam'], r['rho']):
                expect(all(P[p[a]] == P[p[b]] for (a, b) in pairs_of(P)),
                       f"lambda/rho not automorphism-invariant for {B}")
        if cls['regular']:
            stats['regular'] += 1
            if r['monoid']:
                stats['monoid_regular'] += 1
                expect(r['lam_eq_R'] and r['rho_eq_L'], f"regular monoid but lambda!=R or rho!=L: {B}")
            elif not (r['lam_eq_R'] and r['rho_eq_L']):
                stats['lam_ne_R_regular_nonmonoid'] += 1
    else:
        stats['nonSN'] += 1
        if not r['lamR']:
            stats['nonSN_lamR_fail'] += 1
log("small-band statistics:", stats)
expect(stats['lam_ne_R_regular_nonmonoid'] > 0, "no regular non-monoid band with lambda!=R or rho!=L found")
expect(stats['monoid_regular'] > 0 and stats['SN_nonregular'] >= 0, "no regular band monoids tested")
# LZ2 (left zero band) -- NEG-6 for the 'recovers Kimura' remark
LZ2 = [[0, 0], [1, 1]]
r = kimura_band_check(LZ2)
SL = SG(LZ2)
log("NEG-6 LZ2: regular band", r['cls']['regular'], "| lambda classes", r['nlam'], "rho classes", r['nrho'],
    "| L classes", max(SL.L) + 1, "| B/rho right regular:", band_class(quotient(LZ2, r['rho'])[0])['right_regular'])
expect(r['cls']['regular'] and r['nrho'] == 2 and max(SL.L) + 1 == 1
       and not band_class(quotient(LZ2, r['rho'])[0])['right_regular'],
       "NEG-6: LZ2 does not refute the literal 'recovers Kimura' remark")
# converse: products LEFTSN x RIGHTSN are SN
LS = [B for B in BANDS if len(B) <= 4 and band_class(B)['LEFTSN']]
RS = [B for B in BANDS if len(B) <= 4 and band_class(B)['RIGHTSN']]
nprod = 0
for Lb in LS:
    for Rb in RS:
        nl, nr = len(Lb), len(Rb)
        P = [[Lb[a // nr][b // nr] * nr + Rb[a % nr][b % nr] for b in range(nl * nr)] for a in range(nl * nr)]
        expect(band_class(P)['SN'], "product LEFTSN x RIGHTSN not SN")
        nprod += 1
log(f"converse: {nprod} products L x R (|L|,|R|<=4, L LEFTSN, R RIGHTSN) all SN")
# checker sanity (NEG-9): relations that should NOT hold are detected
Fo2, Fr2, Fi2, F2 = build_free_band(2)
F2u = adjoin1(F2)
rF = kimura_band_check(F2u, allcong=False)
SF = SG(F2u)
log("NEG-9 checker sanity on F2^1: lambda<=L ?", finer(rF['lam'], SF.L), "| R meet R trivial ?",
    is_delta(meet(SF.R, SF.R)), "(both expected False)")
expect(not finer(rF['lam'], SF.L) and not is_delta(meet(SF.R, SF.R)), "NEG-9 checker cannot fail")

section("S3. Free band F3 (159), its Kimura quotients, and the non-SN negative F3^1")
Fo3, Fr3, Fi3, F3 = build_free_band(3)
expect(len(F3) == 159, "|F3| != 159")
expect(is_assoc(F3) and all(F3[a][a] == a for a in range(159)), "F3 not a band")
r3 = kimura_band_check(F3, allcong=False, sample_principal=150)
log(f"|F3|={len(F3)} SN={r3['cls']['SN']} regular={r3['cls']['regular']} local R-pairs={r3['npr']} "
    f"local L-pairs={r3['npl']} |F3/lambda|={r3['nlam']} |F3/rho|={r3['nrho']}")
for k in ('lamR', 'rhoL', 'meetD', 'lam_cong', 'rho_cong', 'QL_LEFTSN', 'QR_RIGHTSN', 'step1', 'step2',
          'step3', 'minimal', 'quotcompat', 'chain3c', 'defR', 'defL'):
    expect(r3[k], f"F3: {k} failed")
expect(r3['cls']['SN'] and not r3['cls']['regular'], "F3 should be SN and not regular")
expect(r3['nlam'] == 51 and r3['nrho'] == 51, "F3/lambda or F3/rho not of size 51")
log(f"F3: {r3['ncong']} random principal congruences tested for minimality/quotient compatibility/3(c)")
# NEG-1: F3^1 (identity adjoined) is not SN; lambda <= R must fail for the intended reason
F3u = adjoin1(F3)
r3u = kimura_band_check(F3u, allcong=False)
S3u = SG(F3u)
ab, aba, c_, abc, abac = (Fi3[fb_nf(w)] for w in ((0, 1), (0, 1, 0), (2,), (0, 1, 2), (0, 1, 0, 2)))
one = 159
LM3u = local_monoids(F3u)
w_reg = None
for a in range(160):
    for b in range(160):
        for c in range(160):
            if F3u[F3u[F3u[F3u[a][b]][a]][c]][a] != F3u[F3u[F3u[a][b]][c]][a]:
                w_reg = (a, b, c)
                break
        if w_reg:
            break
    if w_reg:
        break
log("NEG-1 F3^1: SN =", r3u['cls']['SN'], "| lambda<=R =", r3u['lamR'],
    "| ab R aba:", S3u.R[ab] == S3u.R[aba], "| both in local monoid at 1:",
    ab in LM3u[one] and aba in LM3u[one],
    "| abc R abac:", S3u.R[abc] == S3u.R[abac],
    "| Step1 (ab)c(aba) == (aba)c(aba):", F3u[F3u[ab][c_]][aba] == F3u[F3u[aba][c_]][aba],
    "| regular-identity witness in F3:", w_reg is not None)
expect((not r3u['cls']['SN']) and (not r3u['lamR']) and S3u.R[ab] == S3u.R[aba]
       and S3u.R[abc] != S3u.R[abac] and F3u[F3u[ab][c_]][aba] != F3u[F3u[aba][c_]][aba]
       and w_reg is not None and r3u['lam'][abc] == r3u['lam'][abac],
       "NEG-1: F3^1 does not fail for the intended reason")

section("S4. RIGHTSN normal form of the instance-lemma file: Q3 vs F3/rho, and Q4")
for k in (3, 4):
    allt = rsn_all(k)
    ix = {t: i for i, t in enumerate(allt)}
    expect(all(rsn_nf(rsn_rep(t)) == t for t in allt), f"rsn_rep/rsn_nf mismatch k={k}")
    predicted = sum(math.comb(k, j) * math.factorial(j) * math.factorial(j - 1) * j for j in range(1, k + 1))
    Q = [[ix[rsn_nf(rsn_rep(x) + rsn_rep(y))] for y in allt] for x in allt]
    A = np.asarray(Q, dtype=np.int64)
    nq = len(allt)
    band_ok = bool(np.all(A[np.arange(nq), np.arange(nq)] == np.arange(nq))) and is_assoc(Q)
    # local monoids right regular (vectorised)
    ar = np.arange(nq)
    rr = True
    lr = True
    for e in range(nq):
        M = np.nonzero(A[A[e], e] == ar)[0]
        XY = A[np.ix_(M, M)]
        XYX = A[XY, M[:, None]]
        if not np.array_equal(XYX, XY.T):
            rr = False
        if not np.array_equal(XYX, XY):
            lr = False
    relab = True
    for p in itertools.permutations(range(k)):
        Pm = np.array([ix[rsn_relabel(t, p)] for t in allt])
        if not np.array_equal(A[np.ix_(Pm, Pm)], Pm[A]):
            relab = False
    compat = True
    words = [w for L_ in range(1, 5) for w in itertools.product(range(k), repeat=L_)]
    nfw = [ix[rsn_nf(w)] for w in words]
    for i, u in enumerate(words):
        for j, v in enumerate(words):
            if ix[rsn_nf(u + v)] != Q[nfw[i]][nfw[j]]:
                compat = False
    for _ in range(20000):
        u = tuple(random.randrange(k) for _ in range(random.randint(1, 12)))
        v = tuple(random.randrange(k) for _ in range(random.randint(1, 12)))
        if ix[rsn_nf(u + v)] != Q[ix[rsn_nf(u)]][ix[rsn_nf(v)]]:
            compat = False
    log(f"Q{k}: size={nq} predicted sum C(n,k)k!(k-1)!k={predicted} band+assoc={band_ok} "
        f"RIGHTSN={rr} LEFTSN={lr} relabel-automorphisms={relab} word-compatibility={compat}")
    expect(nq == predicted and band_ok and rr and (not lr) and relab and compat, f"Q{k} checks failed")
    if k == 3:
        f = [ix[rsn_nf(Fr3[x])] for x in Fo3]
        hom = all(f[F3[a][b]] == Q[f[a]][f[b]] for a in range(159) for b in range(159))
        same = (label(f) == r3['rho'])
        log(f"F3 -> Q3 via the invariant: homomorphism={hom}, onto={len(set(f)) == nq}, kernel == rho(F3): {same}")
        expect(hom and same and len(set(f)) == nq, "Q3 is not F3/rho")

section("S5/S6. Sources in the reviewer's host model, quotient sources, opposites")
# bands carrying a Z_m action
swapF2 = [Fi2[fb_nf(tuple(1 - z for z in Fr2[x]))] for x in Fo2]
swapF2u = swapF2 + [6]
RB22u = adjoin1([[(a // 2) * 2 + (b % 2) for b in range(4)] for a in range(4)])   # (i,j)(k,l)=(i,l)
rowswap = [2, 3, 0, 1, 4]


def free_one_sided(side):
    el = [(), (0,), (1,), (0, 1), (1, 0)]
    ix = {w: i for i, w in enumerate(el)}

    def mul(u, v):
        if side == 'R':
            return tuple(z for z in u if z not in v) + v
        return u + tuple(z for z in v if z not in u)
    T = [[ix[mul(u, v)] for v in el] for u in el]
    sw = [ix[tuple(1 - z for z in w)] for w in el]
    return T, sw


FRR2u, swR = free_one_sided('R')
FLR2u, swL = free_one_sided('L')
LZ3u = adjoin1([[a] * 3 for a in range(3)])
cyc3 = [1, 2, 0, 3]
for nm, B in (('F2u', F2u), ('RB22u', RB22u), ('FRR2u', FRR2u), ('FLR2u', FLR2u), ('LZ3u', LZ3u)):
    bc = band_class(B)
    log(f"band {nm}: |B|={len(B)} {bc}")
    expect(is_assoc(B) and bc['SN'], f"{nm} not an SN band")
expect(band_class(FRR2u)['right_regular'] and band_class(FLR2u)['left_regular'], "free one-sided bands wrong")
HOSTS = [
    ('F2u/swap/D8', F2u, swapF2u, 'D8'), ('F2u/swap/D4r', F2u, swapF2u, 'D4r'),
    ('F2u/swap/D4c', F2u, swapF2u, 'D4c'), ('F2u/id/D8', F2u, list(range(7)), 'D8'),
    ('F2u/swap/Z2', F2u, swapF2u, 'Z2'), ('RB22u/rowswap/D8', RB22u, rowswap, 'D8'),
    ('RB22u/id/D8', RB22u, list(range(5)), 'D8'), ('FRR2u/swap/D8', FRR2u, swR, 'D8'),
    ('FLR2u/swap/D8', FLR2u, swL, 'D8'), ('LZ3u/cyc/D12', LZ3u, cyc3, 'D12'),
    ('LZ3u/cyc/Z3', LZ3u, cyc3, 'Z3'),
]
SOURCES = []    # (name, table, q, host-or-None, element list)
for hn, B, sg, dn in HOSTS:
    H = make_host(B, sg, DSPECS[dn])
    TH = H['T']
    # host-model checks
    nd = H['nd']
    Eidx = [x for x in range(nd) if H['Dt'][x][x] == x]
    hm_assoc = is_assoc(TH)
    hm_idem = all(TH[b * nd + x][b * nd + x] == b * nd + x for b in range(H['nb']) for x in Eidx)
    hm_w = all(H['W'][x][x] == 0 for x in Eidx)
    # duality isomorphism T(B,D)^op ~ T(B^op, D*)
    m_, nI_, nL_, P_ = H['Dspec']
    Qs = [[(-P_[k_][i_]) % m_ for k_ in range(nL_)] for i_ in range(nI_)]
    Hs = make_host(transpose(B), sg, (m_, nL_, nI_, Qs))
    Dsix = {x: k_ for k_, x in enumerate(Hs['Del'])}
    Phi = []
    for s in range(len(TH)):
        b, x = divmod(s, nd)
        i_, g_, l_ = H['Del'][x]
        Phi.append(H['sp'][(-g_) % m_][b] * Hs['nd'] + Dsix[(l_, (-g_) % m_, i_)])
    dual_ok = (len(set(Phi)) == len(Phi)
               and all(Phi[TH[t][s]] == Hs['T'][Phi[s]][Phi[t]] for s in range(len(TH)) for t in range(len(TH))))
    # functoriality along the characteristic congruences lambda_B, rho_B
    SB = SG(B)
    prB, plB = kimura_pairs(B, SB, local_monoids(B))
    func_ok = True
    for PB in (cong_gen(B, prB), cong_gen(B, plB)):
        inv = all(PB[sg[a]] == PB[sg[b]] for (a, b) in pairs_of(PB))
        QB, rpB = quotient(B, PB)
        sb = [PB[sg[rpB[c]]] for c in range(len(QB))]
        Hb = make_host(QB, sb, H['Dspec'])
        phi = [PB[s // nd] * nd + s % nd for s in range(len(TH))]
        func_ok = func_ok and inv and all(phi[TH[s][t]] == Hb['T'][phi[s]][phi[t]]
                                          for s in range(len(TH)) for t in range(len(TH)))
    log(f"host {hn}: |T(B,D)|={len(TH)} assoc={hm_assoc} idempotent-actor=>idempotent={hm_idem} "
        f"trivial weight at idempotent actors={hm_w} op-iso={dual_ok} functorial(lambda_B,rho_B)={func_ok}")
    expect(hm_assoc and hm_idem and hm_w and dual_ok and func_ok, f"host model check failed for {hn}")
    # random regular subsemigroups
    found = {}
    tries = 0
    while len(found) < 10 and tries < 4000:
        tries += 1
        gens = random.sample(range(len(TH)), random.randint(2, 4))
        Sl = closure(TH, gens)
        key = tuple(Sl)
        if key in found or len(Sl) > 60:
            continue
        Ts = sub_table(TH, Sl)
        if SG(Ts).regular():
            found[key] = Ts
    if SG(TH).regular() and len(TH) <= 60:
        found[tuple(range(len(TH)))] = TH
    for key, Ts in found.items():
        qs = [s % nd for s in key]
        SOURCES.append((f"{hn}#{len(SOURCES)}", Ts, qs, H, list(key)))
log(f"host-generated regular sources: {len(SOURCES)}")
base = list(SOURCES)
# quotient sources S/theta(a,b) with q(a)=q(b)  (need not lie in any host)
QSRC = []
for (nm, Ts, qs, H, key) in base:
    cand = [(a, b) for a in range(len(Ts)) for b in range(a + 1, len(Ts)) if qs[a] == qs[b]]
    random.shuffle(cand)
    for (a, b) in cand[:2]:
        th = cong_gen(Ts, [(a, b)])
        if is_delta(th):
            continue
        Qt, rp = quotient(Ts, th)
        QSRC.append((nm + f"/theta({a},{b})", Qt, [qs[rp[c]] for c in range(len(Qt))], None, None))
OPS = [(nm + "^op", transpose(Ts), qs, None, None) for (nm, Ts, qs, H, key) in base[::3]]
ALL = base + QSRC + OPS
log(f"quotient sources: {len(QSRC)}; opposite sources: {len(OPS)}; total analysed: {len(ALL)}")
agg = dict(sources=0, original=0, RRL=0, LRL=0, RRL_with_Rpairs=0, both_pairs=0, nonRRL=0,
           inst_tested=0, inst_internal=0, quot_nontrivial_lam=0, inj_pairs=0, sizes=[],
           lattice_sources=0, lattice_congruences=0, lattice_pure=0, lattice_neg_nonpure_separating=0)
RRL_IN_HOST = []
for (nm, Ts, qs, H, key) in ALL:
    deep = len(Ts) <= 48
    out = source_analysis(Ts, qs, deep=deep)
    log(f"  {nm}: |S|={len(Ts)} |E|={out['nE']} |D|={out['nD']} RRL={out['RRL']} LRL={out['LRL']} "
        f"localR={out['npr']} localL={out['npl']} |S/lam|={out['nlam']} |S/rho|={out['nrho']} "
        f"inst(tested={out['inst_tested']},viol={out['inst_viol']}) deep={deep}")
    agg['sources'] += 1
    agg['sizes'].append(len(Ts))
    expect(out['original'], f"{nm}: not an original source (construction error)")
    check_source(nm, out, deep=deep)
    agg['original'] += out['original']
    agg['RRL'] += out['RRL']
    agg['LRL'] += out['LRL']
    agg['nonRRL'] += (not out['RRL'])
    agg['RRL_with_Rpairs'] += (out['RRL'] and out['npr'] > 0)
    agg['both_pairs'] += (out['npr'] > 0 and out['npl'] > 0)
    agg['inst_tested'] += out['inst_tested']
    agg['inst_internal'] += out.get('inst_internals_n', 0)
    agg['quot_nontrivial_lam'] += (out['nlam'] < len(Ts))
    agg['inj_pairs'] += out.get('inj_pairs', 0)
    if 'lat_n' in out:
        agg['lattice_sources'] += 1
        agg['lattice_congruences'] += out['lat_n']
        agg['lattice_pure'] += out['lat_pure']
        agg['lattice_neg_nonpure_separating'] += out['lat_neg']
    if H is not None and out['RRL']:
        RRL_IN_HOST.append((nm, Ts, qs, H, key, out))
agg['size_range'] = (min(agg['sizes']), max(agg['sizes']))
del agg['sizes']
log("source aggregate:", agg)
expect(agg['lattice_neg_nonpure_separating'] > 0,
       "NEG-10: no non-pure idempotent-separating nontrivial congruence found (purity necessity not exhibited)")

section("S6b. Matching note 2=>3 inside the host model; Kimura 3(b) fibre homomorphisms")
n23 = dict(sources=0, with_collapse=0, collapsed_pairs=0)
for (nm, Ts, qs, H, key, out) in RRL_IN_HOST:
    B, sg, nd = H['B'], H['sigma'], H['nd']
    SB = SG(B)
    _, plB = kimura_pairs(B, SB, local_monoids(B))
    rhoB = cong_gen(B, plB)
    QB, rpB = quotient(B, rhoB)
    sb = [rhoB[sg[rpB[c]]] for c in range(len(QB))]
    Hb = make_host(QB, sb, H['Dspec'])
    expect(band_class(QB)['RIGHTSN'], f"{nm}: B/rho_B not RIGHTSN")
    phi = [rhoB[s // nd] * nd + s % nd for s in key]
    n_ = len(Ts)
    expect(all(phi[Ts[a][b]] == Hb['T'][phi[a]][phi[b]] for a in range(n_) for b in range(n_)),
           f"{nm}: S -> T(B/rho_B,D) not a homomorphism")
    S_ = SG(Ts)
    lamS = out['lam']
    col = [(e, f) for i, e in enumerate(S_.E) for f in S_.E[i + 1:] if phi[e] == phi[f]]
    for (e, f) in col:
        expect(S_.L[e] == S_.L[f] and lamS[e] != lamS[f], f"{nm}: collapsed pair {e},{f} not L/separated")
    expect(len(set(zip(phi, lamS))) == n_, f"{nm}: product host (B/rho_B) x (S/lambda_S) not injective")
    # 3(b): on an idempotent actor fibre the band coordinate is multiplicative
    for a in range(n_):
        for b in range(n_):
            x, y = key[a] % nd, key[b] % nd
            if x == y and H['Dt'][x][x] == x:
                expect(key[Ts[a][b]] // nd == B[key[a] // nd][key[b] // nd], f"{nm}: 3(b) fibre hom fails")
    n23['sources'] += 1
    n23['with_collapse'] += bool(col)
    n23['collapsed_pairs'] += len(col)
log("2=>3 scenario (RRL sources with a faithful SN host in the model):", n23)

section("S6c. Actor transport (reviewer repair sketch for the canonical-host actor gap)")
Hk = make_host(F2u, swapF2u, DSPECS['D4r'])          # D_kappa: 2 rows, 1 column, P=[[0,1]]
ndk = Hk['nd']
u = [DSPECS['D4r'][3][0][i] for i in range(2)]      # u_i = P[0][i]
tau = [(Hk['Del'][x][1] + u[Hk['Del'][x][0]]) % 2 for x in range(ndk)]   # pure tau: D4r -> Z2
Hz = make_host(F2u, swapF2u, DSPECS['Z2'])
RB21 = [[a for b in range(2)] for a in range(2)]     # 2 rows x 1 column rectangular band = left zero band
BxRB = [[F2u[a // 2][b // 2] * 2 + RB21[a % 2][b % 2] for b in range(14)] for a in range(14)]
sgx = [swapF2u[a // 2] * 2 + a % 2 for a in range(14)]
Hx = make_host(BxRB, sgx, DSPECS['Z2'])
cands = {}
for _ in range(3000):
    gens = random.sample(range(len(Hk['T'])), random.randint(2, 4))
    Sl = closure(Hk['T'], gens)
    if len(Sl) > 40 or tuple(Sl) in cands:
        continue
    rows = {Hk['Del'][s % ndk][0] for s in Sl}
    Ts = sub_table(Hk['T'], Sl)
    if len(rows) == 2 and SG(Ts).regular():
        cands[tuple(Sl)] = Ts
ntw = npl_fail = 0
for Slt, Ts in cands.items():
    Sl = list(Slt)
    n_ = len(Ts)
    qt = [tau[s % ndk] for s in Sl]
    outk = source_analysis(Ts, qt, deep=False)
    expect(outk['original'], "transport demo source not original over the coarse actor")
    twist = [Hk['sp'][u[Hk['Del'][s % ndk][0]]][s // ndk] * 2 + tau[s % ndk] for s in Sl]
    plain = [(s // ndk) * 2 + tau[s % ndk] for s in Sl]
    hom_tw = all(twist[Ts[a][b]] == Hz['T'][twist[a]][twist[b]] for a in range(n_) for b in range(n_))
    hom_pl = all(plain[Ts[a][b]] == Hz['T'][plain[a]][plain[b]] for a in range(n_) for b in range(n_))
    comb = [(Hk['sp'][u[Hk['Del'][s % ndk][0]]][s // ndk] * 2 + Hk['Del'][s % ndk][0]) * 2 + tau[s % ndk]
            for s in Sl]
    hom_c = all(comb[Ts[a][b]] == Hx['T'][comb[a]][comb[b]] for a in range(n_) for b in range(n_))
    inj_c = len(set(comb)) == n_
    expect(hom_tw and hom_c and inj_c, "actor-transport: twisted/combined map failed")
    ntw += 1
    npl_fail += (not hom_pl)
log(f"transport demo: {ntw} regular two-row sources in T(F2^1,D4r) with pure coarse actor tau onto Z2; "
    f"twisted map S->T(F2^1,Z2) a homomorphism in all; twisted x rectangular-row coordinate injective "
    f"homomorphism into T(F2^1 x LZ2, Z2) in all; NEG-7 untwisted map fails to be a homomorphism in {npl_fail}")
expect(ntw > 0 and npl_fail > 0, "NEG-7 actor-transport negative did not occur")

section("S7. Remaining negative controls")
# NEG-2: purity dropped (Z2 with trivial actor)
Z2t = [[0, 1], [1, 0]]
o = source_analysis(Z2t, [0, 0], deep=False)
thu = [0, 0]
log(f"NEG-2 Z2/trivial actor: pure={o['pure']} H∩ker q = Δ: {o['H_kerq']} | universal congruence injective on E "
    f"but not Delta: {len(SG(Z2t).E) == 1 and not is_delta(thu)} | instance identity violations={o['inst_viol']} "
    f"witness={o['inst_wit']} | p=exee' idempotent: {Z2t[1][1] == 1}")
expect((not o['pure']) and (not o['H_kerq']) and o['inst_viol'] > 0 and Z2t[1][1] != 1,
       "NEG-2 purity-dropped control did not fail as intended")
# NEG-3: CS target dropped (F2^1 with q = identity onto a non-CS band)
o = source_analysis(F2u, list(range(7)), deep=False)
xg = [(x, g) for g in range(7) for x in range(7) if x != g and F2u[g][x] == x and F2u[x][g] == x]
log(f"NEG-3 F2^1 with q=id: target CS={o['target_CS']} pure={o['pure']} local R-pairs={o['npr']} "
    f"lambda<=ker q: {o['lam_kerq']} | x<g with q(x)!=q(g): {len(xg)}")
expect((not o['target_CS']) and o['pure'] and o['npr'] > 0 and (not o['lam_kerq']) and xg,
       "NEG-3 non-CS control did not fail as intended")
# NEG-4: 'common local band' restriction dropped (right zero band RZ2, q = id onto CS RZ2)
RZ2 = [[0, 1], [0, 1]]
o = source_analysis(RZ2, [0, 1], deep=False)
allR = cong_gen(RZ2, [(0, 1)])
log(f"NEG-4 RZ2 (CS, q=id): original={o['original']} lambda_S=Delta: {is_delta(o['lam'])} | "
    f"0 R 1: {SG(RZ2).R[0] == SG(RZ2).R[1]} | congruence of ALL R-related idempotents within ker q: "
    f"{finer(allR, [0, 1])} (expected False)")
expect(o['original'] and is_delta(o['lam']) and SG(RZ2).R[0] == SG(RZ2).R[1] and not finer(allR, [0, 1]),
       "NEG-4 control did not fail as intended")

section("SUMMARY")
log(f"runtime {time.time() - T0:.1f}s; unexpected outcomes: {len(UNEXPECTED)}")
for u_ in UNEXPECTED[:50]:
    log("  ", u_)
log("RESULT:", "ALL CONTROLS AS EXPECTED" if not UNEXPECTED else "SURPRISES PRESENT")
if LOG:
    LOG.close()
sys.exit(0 if not UNEXPECTED else 1)
