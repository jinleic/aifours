#!/usr/bin/env python3
"""proof-reconstruct-v1.py -- f109 proof-reviewer independent reconstruction.

Standard library only (fractions, itertools, hashlib, json, math, random).
Nothing from the author's checker/replay is imported or executed; the only
author data consumed are the two coefficient digests copied from the pinned
certificate JSON so that my own digest can be COMPARED against them.

Sections
  A  E4/E3 system derived directly from y-coefficient matching (7 symbolic vars)
  B  same system derived from the power-series / [2/2]-Pade route
     sigma(w) = prod(1+u_i w) / (1+2w+(17/9)w^2)^2 ; den = s2^2 - s1 s3 etc.
  C  Dpol/Npol: integrality, counts, degrees, digests, Cramer + discriminant ids
  D  exact rational point battery + float global search re-checked exactly
  E  girth>=5 coefficient claim on explicit exact Metzler matrices (+controls)
  F  the 14 strongly connected 7-vertex/8-edge shapes and their girths
  G  z-sensitivity control (other z values; heuristic only)
Every PASS/FAIL line is produced by this file alone.
"""
import hashlib, itertools, json, math, random, sys, time
from fractions import Fraction as Fr

LOG = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); LOG.append(s)

# ------------------------------------------------------------------ polys
def P_const(c, nv):
    return {(0,)*nv: Fr(c)} if c else {}
def P_var(i, nv):
    e = [0]*nv; e[i] = 1; return {tuple(e): Fr(1)}
def P_add(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, Fr(0)) + v
    return {k: v for k, v in o.items() if v}
def P_scale(a, c):
    c = Fr(c)
    return {k: v*c for k, v in a.items()} if c else {}
def P_sub(a, b): return P_add(a, P_scale(b, -1))
def P_mul(a, b):
    o = {}
    for k, x in a.items():
        for l, y in b.items():
            key = tuple(i+j for i, j in zip(k, l))
            o[key] = o.get(key, Fr(0)) + x*y
    return {k: v for k, v in o.items() if v}
def P_eval(a, vals):
    tot = Fr(0)
    for k, v in a.items():
        term = v
        for e, x in zip(k, vals):
            if e: term *= Fr(x)**e
        tot += term
    return tot
def P_evalf(a, vals):
    tot = 0.0
    for k, v in a.items():
        term = float(v)
        for e, x in zip(k, vals):
            if e: term *= x**e
        tot += term
    return tot
def P_maxdeg(a, idx):
    return max((k[idx] for k in a), default=0)
def P_coeff_of(a, idx, deg):
    o = {}
    for k, v in a.items():
        if k[idx] == deg:
            kk = list(k); kk[idx] = 0; o[tuple(kk)] = v
    return o
def P_project(a, keep):
    """Drop variables not in `keep` (they must have exponent 0 everywhere)."""
    o = {}
    for k, v in a.items():
        assert all(k[i] == 0 for i in range(len(k)) if i not in keep), (k, keep)
        o[tuple(k[i] for i in keep)] = v
    return o
def Y_mul(A, B):
    out = [{} for _ in range(len(A)+len(B)-1)]
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a and b: out[i+j] = P_add(out[i+j], P_mul(a, b))
    return out

def elem_sym(vars_, k):
    o = {}
    for comb in itertools.combinations(vars_, k):
        term = None
        for v in comb: term = v if term is None else P_mul(term, v)
        o = P_add(o, term)
    return o

# ---------------------------------------------------------- Section A
Z = Fr(8, 9)
NV = 7                      # u0..u4, t, r
U = [P_var(i, NV) for i in range(5)]
T, R = P_var(5, NV), P_var(6, NV)
one = P_const(1, NV)

# D(y) = y [ (y+1)^2 + z ]^2, as list indexed by power of y (constants)
quad = [1+Z, Fr(2), Fr(1)]                       # y^2 + 2y + (1+z)
Dcoef = [Fr(0)]*6
sq = [Fr(0)]*5
for i in range(3):
    for j in range(3): sq[i+j] += quad[i]*quad[j]
for i in range(5): Dcoef[i+1] = sq[i]           # multiply by y
say('D(y) coefficients (y^0..y^5):', [str(c) for c in Dcoef])
assert Dcoef == [Fr(0), Fr(289,81), Fr(68,9), Fr(70,9), Fr(4), Fr(1)]

# F(y) = prod_{i<5}(y+u_i) * (y^2 + t y + r), coefficients as polys in (u,t,r)
F = [one]
for i in range(5): F = Y_mul(F, [U[i], one])
F = Y_mul(F, [R, T, one])
assert len(F) == 8 and F[7] == one
# chi = D(y) Q(y), Q = y^2 + p y + q:  coeff y^m = D_{m-2} + p D_{m-1} + q D_m
def Dk(m): return Dcoef[m] if 0 <= m <= 5 else Fr(0)
# y^6:  F6 = D4 + p D5  -> p = (F6 - D4)/D5 ; D5 = 1
p_poly = P_scale(P_sub(F[6], P_const(Dk(4), NV)), 1/Dk(5))
# y^5:  F5 = D3 + p D4 + q D5 -> q
q_poly = P_scale(P_sub(P_sub(F[5], P_const(Dk(3), NV)), P_scale(p_poly, Dk(4))), 1/Dk(5))
# y^4, y^3 residuals
E4 = P_sub(P_sub(P_sub(F[4], P_const(Dk(2), NV)), P_scale(p_poly, Dk(3))), P_scale(q_poly, Dk(4)))
E3 = P_sub(P_sub(P_sub(F[3], P_const(Dk(1), NV)), P_scale(p_poly, Dk(2))), P_scale(q_poly, Dk(3)))
for nm, E in (('E4', E4), ('E3', E3)):
    assert P_maxdeg(E, 5) <= 1 and P_maxdeg(E, 6) <= 1, nm
    assert all(not (k[5] and k[6]) for k in E), nm + ' has t*r cross term'
say('A: E4,E3 are affine in (t,r) with no t*r term: PASS')
keep = (0, 1, 2, 3, 4)
a00 = P_project(P_coeff_of(E4, 5, 1), keep); a01 = P_project(P_coeff_of(E4, 6, 1), keep)
a10 = P_project(P_coeff_of(E3, 5, 1), keep); a11 = P_project(P_coeff_of(E3, 6, 1), keep)
b0 = P_project({k: v for k, v in E4.items() if k[5] == 0 and k[6] == 0}, keep)
b1 = P_project({k: v for k, v in E3.items() if k[5] == 0 and k[6] == 0}, keep)
# manuscript's (PQ): p = s1 + t - 4 ; q = s2 + t s1 + r - 4p - 70/9
U5 = [P_var(i, 5) for i in range(5)]
s = [None] + [elem_sym(U5, k) for k in range(1, 6)]
assert p_poly == P_add(P_add(elem_sym(U, 1), T), P_const(-4, NV)), 'p != s1+t-4'
qm = P_add(P_add(P_add(elem_sym(U, 2), P_mul(T, elem_sym(U, 1))), R), P_add(P_scale(p_poly, -4), P_const(Fr(-70,9), NV)))
assert q_poly == qm, 'q != s2 + t s1 + r - 4p - 70/9'
say('A: manuscript (PQ) reproduced exactly: PASS')
# hand-derived closed forms (my own derivation):
def S(k): return s[k]
hand = {
 'a00': P_add(P_add(S(2), P_scale(S(1), -4)), P_const(Fr(74,9), 5)),
 'a01': P_add(S(1), P_const(-4, 5)),
 'b0' : P_add(P_add(P_add(S(3), P_scale(S(2), -4)), P_scale(S(1), Fr(74,9))), P_const(Fr(-28,3), 5)),
 'a10': P_add(P_add(S(3), P_scale(S(1), Fr(-70,9))), P_const(Fr(212,9), 5)),
 'a11': P_add(S(2), P_const(Fr(-70,9), 5)),
 'b1' : P_add(P_add(P_add(S(4), P_scale(S(2), Fr(-70,9))), P_scale(S(1), Fr(212,9))), P_const(Fr(-1007,27), 5)),
}
got = {'a00': a00, 'a01': a01, 'b0': b0, 'a10': a10, 'a11': a11, 'b1': b1}
for k in hand: assert hand[k] == got[k], ('hand form mismatch', k)
say('A: hand-derived closed forms a00=s2-4s1+74/9, a01=s1-4, b0=s3-4s2+74s1/9-28/3,')
say('   a10=s3-70s1/9+212/9, a11=s2-70/9, b1=s4-70s2/9+212s1/9-1007/27 : all PASS')

# ---------------------------------------------------------- Section B
# sigma(w) = Shat(w) * g(w)^2,  g = (1+2w+(17/9)w^2)^{-1} (series to w^4)
g = [Fr(1)]
for k in range(1, 5):
    g.append(-2*g[k-1] - (1+Z)*(g[k-2] if k >= 2 else 0))
h = [sum(g[i]*g[k-i] for i in range(k+1)) for k in range(5)]
say('B: g_k =', [str(x) for x in g], ' h_k = (g^2)_k =', [str(x) for x in h])
assert h == [Fr(1), Fr(-4), Fr(74,9), Fr(-28,3), Fr(1,27)]
Shat = [P_const(1, 5)] + [s[k] for k in range(1, 6)]       # coefficient of w^k
sig = []
for k in range(5):
    acc = {}
    for j in range(k+1): acc = P_add(acc, P_scale(Shat[j], h[k-j]))
    sig.append(acc)
assert sig[0] == P_const(1, 5)
assert a00 == sig[2] and a01 == sig[1] and b0 == sig[3]
assert a10 == P_add(sig[3], P_scale(sig[2], 4)) and a11 == P_add(sig[2], P_scale(sig[1], 4)) and b1 == P_add(sig[4], P_scale(sig[3], 4))
say('B: E4 == sigma3 + sigma2 t + sigma1 r ;  E3 == (sigma4+4sigma3) + (sigma3+4sigma2) t + (sigma2+4sigma1) r : PASS')
den_B = P_sub(P_mul(sig[2], sig[2]), P_mul(sig[1], sig[3]))
tn_B  = P_sub(P_mul(sig[1], sig[4]), P_mul(sig[2], sig[3]))
rn_B  = P_sub(P_mul(sig[3], sig[3]), P_mul(sig[2], sig[4]))
den = P_sub(P_mul(a00, a11), P_mul(a01, a10))
tn  = P_add(P_scale(P_mul(b0, a11), -1), P_mul(a01, b1))
rn  = P_add(P_scale(P_mul(a00, b1), -1), P_mul(b0, a10))
assert den == den_B and tn == tn_B and rn == rn_B
say('B: den = sigma2^2 - sigma1 sigma3, tn = sigma1 sigma4 - sigma2 sigma3, rn = sigma3^2 - sigma2 sigma4 : PASS')
# Cramer identities (polynomial identities)
assert P_add(P_add(P_mul(a00, tn), P_mul(a01, rn)), P_mul(b0, den)) == {}
assert P_add(P_add(P_mul(a10, tn), P_mul(a11, rn)), P_mul(b1, den)) == {}
say('B: Cramer identities a00 tn + a01 rn + b0 den = 0 and a10 tn + a11 rn + b1 den = 0 : PASS')

# ---------------------------------------------------------- Section C
Dpol = P_scale(den, 81)
disc = P_sub(P_mul(tn, tn), P_scale(P_mul(rn, den), 4))
Npol = P_scale(disc, -19683)
assert all(v.denominator == 1 for v in Dpol.values()) and all(v.denominator == 1 for v in Npol.values())
say('C: 81*den and -19683*disc have integer coefficients: PASS')
say('C: term counts D,N =', len(Dpol), len(Npol), '; individual degrees D =', [P_maxdeg(Dpol, i) for i in range(5)], 'N =', [P_maxdeg(Npol, i) for i in range(5)])
assert (len(Dpol), len(Npol)) == (96, 1753)
assert [P_maxdeg(Dpol, i) for i in range(5)] == [2]*5 and [P_maxdeg(Npol, i) for i in range(5)] == [4]*5
def digest(P):
    rows = [[list(k), str(int(c))] for k, c in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
CERT_D = '5449296f6d105d2c1303053930dfb69ab16c606d64201b6e36311c6f094c4009'
CERT_N = '7c1ebd087490f5487db2851fb09b90bdd688983ae6929852637e04f55679f69e'
dD, dN = digest(Dpol), digest(Npol)
say('C: my digest(D) =', dD, 'matches certificate:', dD == CERT_D)
say('C: my digest(N) =', dN, 'matches certificate:', dN == CERT_N)
assert dD == CERT_D and dN == CERT_N
# discriminant identity: t^2-4r = disc/den^2 = -N/(3 D^2)
lhs = P_scale(P_mul(P_mul(Dpol, Dpol), disc), 3)
rhs = P_scale(P_mul(Npol, P_mul(den, den)), -1)
assert lhs == rhs
say('C: identity 3*Dpol^2*disc == -Npol*den^2  (i.e. t^2-4r = -Npol/(3 Dpol^2)) : PASS')
# minimal integer scaling check: is 81 the least k with k*den integral? is 19683 least for disc?
def min_scale(P):
    L = 1
    for v in P.values(): L = L*v.denominator//math.gcd(L, v.denominator)
    return L
say('C: least common denominators: den ->', min_scale(den), ' disc ->', min_scale(disc))
# Also record the two extreme constant/leading pieces
say('C: Dpol(0)=', P_eval(Dpol, [0]*5), ' Npol(0)=', P_eval(Npol, [0]*5))

# ---------------------------------------------------------- Section D
def DN_exact(u):
    return P_eval(Dpol, u), P_eval(Npol, u)
def sig_float(u, z=8/9):
    # float sigma_k via series; returns (den, disc) floats
    gq = [1.0]
    for k in range(1, 5): gq.append(-2*gq[k-1] - (1+z)*(gq[k-2] if k >= 2 else 0))
    hq = [sum(gq[i]*gq[k-i] for i in range(k+1)) for k in range(5)]
    e = [1.0, 0, 0, 0, 0, 0]
    for x in u:
        for k in range(5, 0, -1): e[k] += x*e[k-1]
    sg = [sum(e[j]*hq[k-j] for j in range(k+1)) for k in range(5)]
    dn = sg[2]**2 - sg[1]*sg[3]; tnn = sg[1]*sg[4] - sg[2]*sg[3]; rnn = sg[3]**2 - sg[2]*sg[4]
    return dn, tnn*tnn - 4*rnn*dn
battery = [
 [1,1,1,1,1], [Fr(4,5)]*5, [Fr(1,1000)]*5, [1000]*5, [4,0,0,0,0], [Fr(1,1000),Fr(1,1000),Fr(1,1000),Fr(1,1000),4],
 [1,2,3,4,5], [Fr(1,2),1,2,4,8], [Fr(1,10),Fr(1,10),10,10,10], [2,2,2,2,2], [Fr(2,3)]*5, [Fr(1,3)]*5,
 [Fr(3,2),Fr(3,2),Fr(3,2),Fr(3,2),Fr(1,1000)], [1,1,1,1,Fr(1,10**6)], [1,1,1,1,10**6],
 [Fr(17,9),Fr(17,9),1,1,1], [Fr(4,3),Fr(4,3),Fr(4,3),Fr(1,100),Fr(1,100)],
 [1,1,Fr(1,10**9),Fr(1,10**9),Fr(1,10**9)], [2,2,Fr(1,10**9),Fr(1,10**9),Fr(1,10**9)],
 [Fr(1,10**9)]*5, [10**9]*5, [Fr(8,9)]*5, [Fr(4,5),Fr(4,5),Fr(4,5),Fr(4,5),Fr(1,10**9)],
]
say('D: exact battery (u1..u5 -> Dpol, Npol):')
worstD = worstN = None
for u in battery:
    d, n = DN_exact(u)
    say('   ', [str(Fr(x)) for x in u], '-> D =', d, ' N =', n)
    assert d > 0 and n > 0, ('NONPOSITIVE', u, d, n)
    worstD = d if worstD is None or d < worstD else worstD
    worstN = n if worstN is None or n < worstN else worstN
say('D: battery minima D,N =', worstD, worstN, ' all strictly positive: PASS')

random.seed(20261028)
def local_search(f, dim=5, restarts=400, iters=1500, lo=-9.0, hi=7.0):
    best = (float('inf'), None)
    for _ in range(restarts):
        x = [random.uniform(lo, hi) for _ in range(dim)]
        fx = f([math.exp(v) for v in x]); step = 1.0
        for it in range(iters):
            y = [min(hi, max(lo, v + random.gauss(0, step))) for v in x]
            fy = f([math.exp(v) for v in y])
            if fy < fx: x, fx = y, fy; step = min(step*1.3, 3.0)
            else: step *= 0.97
            if step < 1e-7: break
        if fx < best[0]: best = (fx, x)
    return best
t0 = time.time()
bD = local_search(lambda u: sig_float(u)[0])
bN = local_search(lambda u: -sig_float(u)[1])     # minimize -disc  == minimize N/19683
say('D: float search (%.1fs): min den ~ %.6g at u=%s' % (time.time()-t0, bD[0], [round(math.exp(v), 6) for v in bD[1]]))
say('D: float search: min (-disc) ~ %.6g at u=%s' % (bN[0], [round(math.exp(v), 6) for v in bN[1]]))
for tag, b in (('argmin den', bD), ('argmin -disc', bN)):
    u = [Fr(math.exp(v)).limit_denominator(10**9) for v in b[1]]
    d, n = DN_exact(u)
    say('   exact recheck at', tag, '->', [float(x) for x in u], ' D =', float(d), ' N =', float(n), 'sign ok:', d > 0 and n > 0)
    assert d > 0 and n > 0
# scale-normalized search as well (avoid being dominated by large u): minimize N/(1+sum u)^8 and D/(1+sum u)^4
bD2 = local_search(lambda u: sig_float(u)[0]/(1+sum(u))**4, restarts=200)
bN2 = local_search(lambda u: -sig_float(u)[1]/(1+sum(u))**8, restarts=200)
say('D: normalized search: min den/(1+S)^4 ~ %.6g at %s' % (bD2[0], [round(math.exp(v), 6) for v in bD2[1]]))
say('D: normalized search: min -disc/(1+S)^8 ~ %.6g at %s' % (bN2[0], [round(math.exp(v), 6) for v in bN2[1]]))
for tag, b in (('argmin den/(1+S)^4', bD2), ('argmin -disc/(1+S)^8', bN2)):
    u = [Fr(math.exp(v)).limit_denominator(10**9) for v in b[1]]
    d, n = DN_exact(u)
    say('   exact recheck at', tag, '->', [float(x) for x in u], ' D =', float(d), ' N =', float(n), 'sign ok:', d > 0 and n > 0)
    assert d > 0 and n > 0
# dense random exact sampling
cnt = 0; minD = minN = None
for _ in range(3000):
    u = [Fr(random.randint(1, 2000), random.randint(1, 2000)) for _ in range(5)]
    d, n = DN_exact(u); cnt += 1
    assert d > 0 and n > 0, ('NONPOSITIVE random', u, d, n)
    minD = d if minD is None or d < minD else minD; minN = n if minN is None or n < minN else minN
say('D: 3000 exact random rational points: all D,N > 0 ; min D = %.6g, min N = %.6g' % (float(minD), float(minN)))

# ---------------------------------------------------------- Section E
def charpoly(A):
    """Faddeev-LeVerrier, exact. Returns coefficients c[0..n] of det(yI-A), c[n]=1."""
    n = len(A); I = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    def mm(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    c = [Fr(0)]*(n+1); c[n] = Fr(1); M = [[Fr(0)]*n for _ in range(n)]
    for k in range(1, n+1):
        M = mm(A, M)
        for i in range(n): M[i][i] += c[n-k+1]
        AM = mm(A, M)
        c[n-k] = -sum(AM[i][i] for i in range(n))/k
    return c
def esym_vals(vals, k):
    return sum(math.prod(c) for c in itertools.combinations(vals, k)) if k else Fr(1)
def rnd(): return Fr(random.randint(1, 50), random.randint(1, 7))
def build(edges, n=7):
    u = [rnd() for _ in range(n)]
    A = [[Fr(0)]*n for _ in range(n)]
    for i in range(n): A[i][i] = -u[i]
    for (i, j) in edges: A[i][j] = rnd()
    return u, A
def girth(edges, n=7):
    adj = {i: [] for i in range(n)}
    for i, j in edges: adj[i].append(j)
    best = None
    for s0 in range(n):
        dist = {s0: 0}; q = [s0]
        for v in q:
            for w in adj[v]:
                if w == s0: 
                    L = dist[v]+1; best = L if best is None or L < best else best
                elif w not in dist: dist[w] = dist[v]+1; q.append(w)
    return best
def strongly_connected(edges, n=7):
    adj = {i: set() for i in range(n)}; radj = {i: set() for i in range(n)}
    for i, j in edges: adj[i].add(j); radj[j].add(i)
    def reach(a, start):
        seen = {start}; q = [start]
        for v in q:
            for w in a[v]:
                if w not in seen: seen.add(w); q.append(w)
        return seen
    return len(reach(adj, 0)) == n and len(reach(radj, 0)) == n
cyc7 = [(i, (i+1) % 7) for i in range(7)]
theta57 = cyc7 + [(4, 0)]                  # 5-cycle 0..4 + 7-cycle (girth 5)
theta67 = cyc7 + [(5, 0)]                  # 6-cycle + 7-cycle (girth 6)
ctrl4   = cyc7 + [(3, 0)]                  # 4-cycle control
ctrl2   = cyc7 + [(1, 0)]                  # 2-cycle control
theta_1_3_4 = [(0,6),(0,1),(1,2),(2,6),(6,3),(3,4),(4,5),(5,0)]  # x=0,y=6: paths len1 (0-6), len3 (0-1-2-6), len4 (6-3-4-5-0): cycles 5 and 7
for name, E, expect_match in (('theta 5/7 (girth5)', theta57, True), ('theta 6/7 (girth6)', theta67, True),
                              ('theta {1,3},l3=4 (girth5)', theta_1_3_4, True),
                              ('7-cycle', cyc7, True), ('control 4-cycle', ctrl4, False), ('control 2-cycle', ctrl2, False)):
    assert strongly_connected(E)
    for trial in range(3):
        u, A = build(E)
        c = charpoly(A)
        match = all(c[7-k] == esym_vals(u, k) for k in range(1, 5))
        y2_match = (c[2] == esym_vals(u, 5))
        say('E: %-28s girth=%s trial%d: coeffs y^6..y^3 == e1..e4(diag): %s ; y^2 == e5(diag): %s' % (name, girth(E), trial, match, y2_match))
        assert match == expect_match
say('E: girth>=5 graphs match y^6..y^3 exactly; girth<=4 controls break it: PASS')
# nonnormal / overlapping cycles: random dense girth-5 graph on 7 vertices (add edges while girth>=5)
for trial in range(5):
    E = list(cyc7); cand = [(i, j) for i in range(7) for j in range(7) if i != j and (i, j) not in E]
    random.shuffle(cand)
    for e in cand:
        if girth(E + [e]) >= 5: E.append(e)
    u, A = build(E); c = charpoly(A)
    ok = all(c[7-k] == esym_vals(u, k) for k in range(1, 5))
    say('E: maximal girth>=5 supergraph trial%d: edges=%d girth=%d match=%s' % (trial, len(E), girth(E), ok)); assert ok

# ---------------------------------------------------------- Section F
def canon(edges, n=7):
    best = None
    for perm in itertools.permutations(range(n)):
        key = tuple(sorted((perm[i], perm[j]) for i, j in edges))
        if best is None or key < best: best = key
    return best
shapes = {}
# theta: x -> y via paths of lengths l1,l2 ; y -> x via l3 ; l1+l2+l3=8 ; 7 vertices
def path_edges(a, b, L, nxt):
    """directed path a->...->b with L edges, fresh internal vertices from nxt()"""
    es = []; prev = a
    for _ in range(L-1):
        v = nxt(); es.append((prev, v)); prev = v
    es.append((prev, b)); return es
for l1 in range(1, 8):
    for l2 in range(l1, 8):
        l3 = 8 - l1 - l2
        if l3 < 1 or (l1 == 1 and l2 == 1): continue
        cnt = [2]; nxt = lambda: (cnt.__setitem__(0, cnt[0]+1), cnt[0]-1)[1]
        E = path_edges(0, 1, l1, nxt) + path_edges(0, 1, l2, nxt) + path_edges(1, 0, l3, nxt)
        assert cnt[0] == 7 and len(E) == 8 and len(set(E)) == 8 and strongly_connected(E)
        shapes[canon(E)] = ('theta', (l1, l2, l3), girth(E))
for a in range(2, 8):
    b = 8 - a
    if b < a: continue
    cnt = [1]; nxt = lambda: (cnt.__setitem__(0, cnt[0]+1), cnt[0]-1)[1]
    E = path_edges(0, 0, a, nxt) + path_edges(0, 0, b, nxt)
    assert cnt[0] == 7 and len(E) == 8 and len(set(E)) == 8 and strongly_connected(E)
    shapes[canon(E)] = ('figure8', (a, b), girth(E))
# second, independent parametrization: 7-cycle + ear of length l from vertex 0 to vertex k (k=0 closed)
shapes2 = {}
for c1 in range(2, 8):
    l = 8 - c1
    for k in range(0, c1):
        cnt = [c1]; nxt = lambda: (cnt.__setitem__(0, cnt[0]+1), cnt[0]-1)[1]
        E = [(i, (i+1) % c1) for i in range(c1)] + path_edges(0, k, l, nxt)
        if len(set(E)) < 8 or any(i == j for i, j in E): continue   # duplicate edge or self-loop: not a simple off-diagonal graph
        assert cnt[0] == 7 and strongly_connected(E)
        shapes2[canon(E)] = (c1, l, k, girth(E))
say('F: distinct 7-vertex/8-edge strongly connected simple digraph shapes: theta/figure8 param ->', len(shapes), '; cycle+ear param ->', len(shapes2), '; same set:', set(shapes) == set(shapes2))
assert len(shapes) == 14 and set(shapes) == set(shapes2)
g5 = [v for v in shapes.values() if v[2] >= 5]
say('F: shapes with girth>=5:', len(g5), sorted(g5))
assert len(g5) == 5

# ---------------------------------------------------------- Section G
say('G: z-sensitivity control (float search of min den and min -disc; heuristic only, NOT a theorem):')
for z in (0.05, 0.25, 0.5, 8/9, 1.0, 2.0, 5.0):
    bd = local_search(lambda u: sig_float(u, z)[0], restarts=60, iters=800)
    bn = local_search(lambda u: -sig_float(u, z)[1], restarts=60, iters=800)
    say('   z=%-6g  min den ~ %+.4g   min(-disc) ~ %+.4g' % (z, bd[0], bn[0]))

say('ALL PROOF-REVIEWER RECONSTRUCTION ASSERTIONS PASSED')
from pathlib import Path
Path(__file__).with_suffix('.log').write_text('\n'.join(LOG) + '\n')
