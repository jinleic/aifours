#!/usr/bin/env python3
"""reviewer-f129-engine-v1.py -- independently written exact control for review
f129-ph7-girth-four-two-or-three-cycle (PH7 at z=8/9: girth>=4 is impossible).

No author code is imported or executed. Author files are only hashed; the
certificate JSON is parsed for its two pinned coefficient digests and its two
leaf-path lists, which are the objects under test.

Steps
 1  SHA-256/bytes/LF receipts of the manifest and its five inputs.
 2  Elementary symmetric polynomials of six rates by the product recursion
    prod_i (1 + u_i t); the seventh rate x is carried as an affine parameter.
 3  Coefficient match of D_z(y)(y^2+py+q), D_z(y)=y[(y+1)^2+z]^2, at general z,
    giving p, q, E4 = A x + B, E3 = h1 x + h0; Qnum = q0 A - qx B, Hnum = h0 A - h1 B.
    At z=8/9: Qpol = 81 Qnum, Hpol = -243 Hnum must be integral, degree <= 2 per
    variable, 168/435 terms, reproduce the two pinned digests, and agree with the
    candidate's literal f-form coefficient lists.
 4  Numeric spot checks: (CHAR) on a seeded bipartite girth>=4 Metzler matrix via
    Faddeev-LeVerrier plus explicit 2/3/4-cycle enumeration; the elimination
    identities q = Qpol/(81A), E3 = -Hpol/(243A) at seeded rational six-tuples.
 5  Own degree-2 tensor de Casteljau midpoint subdivision. Each certificate leaf
    list is checked for prefix-freeness and two-children completeness (exact
    partition of [0,1]^6); per leaf: depth >= 6, every coordinate split at least
    once, all 729 scaled coefficients >= 0, every vertex in the open cube > 0.
 6  Negative controls: sign-flipped constant, constant minus one, missing leaf,
    duplicate leaf, prefix-collision leaf, flipped bit convention, wrong z.
 7  Side claim: enumerate strongly connected 7-vertex 8-arc simple digraph shapes
    (theta / figure-eight) and count those of girth >= 4.
"""
import hashlib, itertools, json, math, random, sys, time
from datetime import datetime, timezone
from fractions import Fraction as Fr
from pathlib import Path

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
T0 = utc(); W0 = time.time()
RUN = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h')
EVID = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type')
OUT = RUN/'review-waves'/'f129-ph7-girth-four-two-or-three-cycle'
EXPECT = {
 OUT/'manifest-v1.json': 'bdfa01e52e02bfecbfd7e4f05e031411ce31445c2299f16be1b02087fcbec369',
 RUN/'dispositions/math-1-ph7-critical-short-cycle-parent-v1.md': 'de045d1b9278ef5d85d4d510ab0d8f8faa8296da3ce213bf95baef3b6e6c9892',
 EVID/'frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md': '76ff376815423d69546c10e2608f7c373a80f3e7752d306c911751e8eb50f33b',
 EVID/'frontier-20261028-ph7-girth4-critical-bernstein-check.py': '8f5fc02b87996bbda2ea8b7af1976b467ef3c9a46c3a9b9274e538eea941e1c4',
 EVID/'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json': 'b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8',
 EVID/'frontier-20261028-ph7-girth4-critical-integer-replay.py': 'ac5b069e3d4d5c108b9b9a6e3df12172f5bc360390f92c119a0af58e48116177',
}
R = {'engine': 'reviewer-f129-engine-v1.py', 'utc_start': T0, 'python': sys.version, 'inputs': {}}
for p, want in EXPECT.items():
    b = p.read_bytes(); got = hashlib.sha256(b).hexdigest()
    R['inputs'][str(p)] = {'sha256': got, 'bytes': len(b), 'LF': b.count(b'\n'), 'matches_manifest': got == want}
    if got != want: sys.exit(f'HASH MISMATCH {p}')
CERT = json.loads((EVID/'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json').read_bytes())

# ---------------------------------------------------------------- polynomials
def padd(a, b):
    r = dict(a)
    for k, v in b.items():
        s = r.get(k, 0) + v
        if s == 0: r.pop(k, None)
        else: r[k] = s
    return r
def pneg(a): return {k: -v for k, v in a.items()}
def psub(a, b): return padd(a, pneg(b))
def pscale(a, c):
    c = Fr(c)
    return {k: v*c for k, v in a.items()} if c != 0 else {}
def pmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x+y for x, y in zip(k1, k2)); s = r.get(k, 0) + v1*v2
            if s == 0: r.pop(k, None)
            else: r[k] = s
    return r
def pconst(c, n):
    c = Fr(c); return {(0,)*n: c} if c != 0 else {}
def pvar(i, n):
    e = [0]*n; e[i] = 1; return {tuple(e): Fr(1)}
def peval(a, pt):
    s = Fr(0)
    for k, v in a.items():
        t = v
        for e, x in zip(k, pt): t *= Fr(x)**e
        s += t
    return s
def elementary(n, kmax):
    E = [pconst(1, n)] + [{} for _ in range(kmax)]
    for i in range(n):
        u = pvar(i, n)
        for k in range(kmax, 0, -1): E[k] = padd(E[k], pmul(E[k-1], u))
    return E
def integral(a): return all(v.denominator == 1 for v in a.values())
def to_int(a): return {k: int(v) for k, v in a.items()}
def degrees(a, n): return [max((k[i] for k in a), default=0) for i in range(n)]
def canon_digest(a):
    rows = [[list(k), str(int(v))] for k, v in sorted(a.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()
def show(a, names):
    terms = []
    for k, v in sorted(a.items(), reverse=True):
        mon = '*'.join(f'{nm}^{e}' if e > 1 else nm for nm, e in zip(names, k) if e)
        terms.append(f'{v}' + (f'*{mon}' if mon else ''))
    return ' + '.join(terms)

# ---------------------------------------------------------------- derivation
def dz_coeffs(z):
    """D_z(y) = y[(y+1)^2+z]^2 = y^5 + d4 y^4 + d3 y^3 + d2 y^2 + d1 y."""
    c = 1 + Fr(z)
    return Fr(4), 4 + 2*c, 4*c, c*c
def derive(z, f1, f2, f3, f4, n):
    """e_k = f_k + f_{k-1} x with x the seventh rate (f_0 = 1). Match
    [y^6..y^3] of D_z (y^2+py+q) against e1, e2, e3, e4 - C4."""
    d4, d3, d2, d1 = dz_coeffs(z)
    one, zero = pconst(1, n), {}
    e1, e2, e3, e4 = (one, f1), (f1, f2), (f2, f3), (f3, f4)
    A_ = lambda a, b: (padd(a[0], b[0]), padd(a[1], b[1]))
    S_ = lambda a, c: (pscale(a[0], c), pscale(a[1], c))
    K_ = lambda c: (zero, pconst(c, n))
    p = A_(e1, K_(-d4))                                     # [y^6]: e1 = p + d4
    q = A_(A_(e2, S_(p, -d4)), K_(-d3))                     # [y^5]: e2 = q + d4 p + d3
    E4 = A_(A_(A_(e3, S_(q, -d4)), S_(p, -d3)), K_(-d2))     # [y^4]: e3 - (d4 q + d3 p + d2) = 0
    E3 = A_(A_(A_(e4, S_(q, -d3)), S_(p, -d2)), K_(-d1))     # [y^3]: e4 - (d3 q + d2 p + d1) = C4
    A, B = E4; h1, h0 = E3; qx, q0 = q
    return dict(D=(d4, d3, d2, d1), A=A, B=B, h1=h1, h0=h0, qx=qx, q0=q0,
                Qnum=psub(pmul(q0, A), pmul(qx, B)), Hnum=psub(pmul(h0, A), pmul(h1, B)))

N = 6
E6 = elementary(N, 4); F1, F2, F3, F4 = E6[1], E6[2], E6[3], E6[4]
Z = Fr(8, 9)
D = derive(Z, F1, F2, F3, F4, N)
R['D_coefficients_at_8_9'] = [str(c) for c in D['D']]
# author-stated closed forms (re-typed from the candidate), compared as polynomials
A_c = padd(padd(F2, pscale(F1, -4)), pconst(Fr(74, 9), N))
B_c = padd(padd(padd(F3, pscale(F2, -4)), pscale(F1, Fr(74, 9))), pconst(Fr(-28, 3), N))
h0_c = padd(padd(padd(F4, pscale(F2, Fr(-70, 9))), pscale(F1, Fr(212, 9))), pconst(Fr(-1007, 27), N))
h1_c = padd(padd(F3, pscale(F1, Fr(-70, 9))), pconst(Fr(212, 9), N))
R['closed_forms_match_candidate'] = {
    'A': D['A'] == A_c, 'B': D['B'] == B_c, 'h0': D['h0'] == h0_c, 'h1': D['h1'] == h1_c,
    'q_constant_equals_A': D['q0'] == D['A'], 'q_x_coefficient_equals_f1_minus_4': D['qx'] == padd(F1, pconst(-4, N))}
Qpol = pscale(D['Qnum'], 81); Hpol = pscale(D['Hnum'], -243)
R['Qpol'] = {'integral': integral(Qpol), 'terms': len(Qpol), 'degrees': degrees(Qpol, N)}
R['Hpol'] = {'integral': integral(Hpol), 'terms': len(Hpol), 'degrees': degrees(Hpol, N)}
assert R['Qpol']['integral'] and R['Hpol']['integral']
Qpol, Hpol = to_int(Qpol), to_int(Hpol)
R['Qpol']['digest'] = canon_digest(Qpol); R['Hpol']['digest'] = canon_digest(Hpol)
R['Qpol']['digest_matches_certificate'] = R['Qpol']['digest'] == CERT['Q_coefficients_sha256']
R['Hpol']['digest_matches_certificate'] = R['Hpol']['digest'] == CERT['H_coefficients_sha256']
R['certificate_header'] = {k: CERT[k] for k in ('z', 'Q_coefficients_sha256', 'H_coefficients_sha256',
                           'Q_variable_degrees', 'H_variable_degrees', 'Q_terms', 'H_terms', 'split_axis',
                           'compactification', 'identity', 'scope')}
R['certificate_counts_match'] = (CERT['Q_terms'] == len(Qpol) and CERT['H_terms'] == len(Hpol)
                                 and CERT['Q_variable_degrees'] == degrees(Qpol, N) == [2]*6
                                 and CERT['H_variable_degrees'] == degrees(Hpol, N) == [2]*6)
# literal f-form (abstract f1..f4) versus the candidate's section-3 lists
Fv = [pvar(i, 4) for i in range(4)]
Dl = derive(Z, *Fv, 4)
Ql = to_int(pscale(Dl['Qnum'], 81)); Hl = to_int(pscale(Dl['Hnum'], -243))
Q_lit = {(2,0,0,0):630, (1,1,0,0):-324, (1,0,1,0):-81, (1,0,0,0):-1908, (0,2,0,0):81, (0,1,0,0):36, (0,0,1,0):324, (0,0,0,0):2452}
H_lit = {(2,0,0,0):7356, (1,1,0,0):-5724, (1,0,1,0):108, (1,0,0,1):972, (1,0,0,0):-18612, (0,2,0,0):1890, (0,1,1,0):-972,
         (0,1,0,1):-243, (0,1,0,0):1707, (0,0,2,0):243, (0,0,1,0):3456, (0,0,0,1):-1998, (0,0,0,0):21094}
R['literal_f_form'] = {'Qpol_matches_candidate': Ql == Q_lit, 'Hpol_matches_candidate': Hl == H_lit,
                       'Qpol_f_form': show(Ql, ['f1','f2','f3','f4']), 'Hpol_f_form': show(Hl, ['f1','f2','f3','f4'])}

# ---------------------------------------------------------------- numeric spot checks
def charpoly(M):
    """Faddeev-LeVerrier: coefficients c[0..n] of det(yI-M) = sum c_k y^k, exact."""
    n = len(M); I = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    def mm(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    c = [Fr(0)]*(n+1); c[n] = Fr(1); Mk = [[Fr(0)]*n for _ in range(n)]
    for k in range(1, n+1):
        Mk = mm(M, Mk)
        for i in range(n): Mk[i][i] += c[n-k+1]
        P = mm(M, Mk); c[n-k] = -sum(P[i][i] for i in range(n))/k
    return c
def esym(vals, kmax):
    E = [Fr(1)] + [Fr(0)]*kmax
    for v in vals:
        for k in range(kmax, 0, -1): E[k] += E[k-1]*v
    return E
rng = random.Random(129)
def rq(): return Fr(rng.randint(1, 400), rng.randint(1, 40))
arcs = [(0,3),(0,4),(1,4),(1,5),(2,5),(2,6),(3,1),(4,2),(5,0),(6,0),(3,2),(6,1)]
W = {a: rq() for a in arcs}
U = [rq() for _ in range(7)]
G = [[Fr(0)]*7 for _ in range(7)]
for i in range(7): G[i][i] = -U[i]
for (i, j), w in W.items(): G[i][j] = w
def cycles_of_length(arcset, L):
    out = set()
    for seq in itertools.permutations(range(7), L):
        if seq[0] != min(seq): continue
        if all((seq[t], seq[(t+1) % L]) in arcset for t in range(L)): out.add(seq)
    return out
AS = set(arcs)
c2, c3, c4 = cycles_of_length(AS, 2), cycles_of_length(AS, 3), cycles_of_length(AS, 4)
C4 = sum(math.prod(W[(cy[t], cy[(t+1) % 4])] for t in range(4)) for cy in c4)
cp = charpoly(G); eU = esym(U, 4)
R['CHAR_spot_check'] = {'arcs': arcs, 'n_2cycles': len(c2), 'n_3cycles': len(c3), 'n_4cycles': len(c4),
    'four_cycles': [list(c) for c in sorted(c4)], 'c6_eq_e1': cp[6] == eU[1], 'c5_eq_e2': cp[5] == eU[2],
    'c4_eq_e3': cp[4] == eU[3], 'c3_eq_e4_minus_C4': cp[3] == eU[4] - C4, 'C4': str(C4),
    'c3_minus_e4': str(cp[3] - eU[4])}
assert len(c2) == 0 and len(c3) == 0 and len(c4) >= 3
elim = []
for _ in range(5):
    six = [rq() for _ in range(6)]; f = esym(six, 4)
    A = peval(D['A'], six); B = peval(D['B'], six); x = -B/A
    e = esym(six + [x], 4); p = e[1] - 4; q = e[2] - 4*p - Fr(70, 9)
    E4 = e[3] - 4*e[2] + Fr(74, 9)*e[1] - Fr(28, 3)
    E3 = e[4] - Fr(70, 9)*e[2] + Fr(212, 9)*e[1] - Fr(1007, 27)
    Qv = peval(Qpol, six); Hv = peval(Hpol, six)
    elim.append({'six': [str(s) for s in six], 'x': str(x), 'E4_zero': E4 == 0,
                 'q_eq_Qpol_over_81A': q == Qv/(81*A), 'E3_eq_minus_Hpol_over_243A': E3 == -Hv/(243*A),
                 'Qpol_positive': Qv > 0, 'Hpol_positive': Hv > 0, 'A_positive': A > 0, 'q': str(q), 'E3': str(E3)})
R['elimination_spot_checks'] = elim

# ---------------------------------------------------------------- Bernstein engine
STRIDE = [3**i for i in range(N)]
def bernstein_root(P):
    """Tensor Bernstein coefficients of prod(1-x_i)^2 * P(x/(1-x)) on [0,1]^6, times 64.
    b_k = c_k / prod C(2,k_i); little-endian index sum k_i 3^i."""
    arr = [0]*729
    for k, v in P.items():
        assert all(0 <= e <= 2 for e in k), k
        div = 1
        for e in k:
            if e == 1: div *= 2
        arr[sum(e*s for e, s in zip(k, STRIDE))] = v * (64 // div)
    return arr
def split_axis(arr, a):
    """Degree-2 de Casteljau at t=1/2 along axis a, both halves scaled by 4."""
    L = [0]*729; Rr = [0]*729; s = STRIDE[a]
    for idx in range(729):
        if (idx // s) % 3: continue
        b0, b1, b2 = arr[idx], arr[idx+s], arr[idx+2*s]; m = b0 + 2*b1 + b2
        L[idx], L[idx+s], L[idx+2*s] = 4*b0, 2*(b0+b1), m
        Rr[idx], Rr[idx+s], Rr[idx+2*s] = m, 2*(b1+b2), 4*b2
    return L, Rr
class Fail(Exception): pass
def verify_cover(root, leaves, lower_bit='0'):
    upper_bit = '1' if lower_bit == '0' else '0'
    leaves = list(leaves); S = set(leaves); res = {'n_leaves_given': len(leaves)}
    try:
        if len(S) != len(leaves): raise Fail('duplicate leaf path')
        proper = set()
        for p in leaves:
            for j in range(len(p)): proper.add(p[:j])
        coll = S & proper
        if coll: raise Fail(f'leaf {min(coll, key=len)!r} is a proper prefix of another leaf')
        nodes = proper | S
        for r in sorted(proper, key=len):
            if (r+'0') not in nodes or (r+'1') not in nodes: raise Fail(f'internal node {r!r} lacks a child')
        res['exact_partition'] = True; res['internal_nodes'] = len(proper)
        stack = [('', root, (False,)*N, (False,)*N)]
        seen = coeff = corners = maxd = 0; mind = 10**9; splits = [0]*N
        min_norm = None; min_interior_norm = None
        while stack:
            path, arr, lo_gt0, hi_lt1 = stack.pop(); d = len(path)
            if path in S:
                seen += 1; maxd = max(maxd, d); mind = min(mind, d)
                if d < N: raise Fail(f'leaf {path!r} shallower than 6')
                if not all(a or b for a, b in zip(lo_gt0, hi_lt1)): raise Fail(f'leaf {path!r}: coordinate never split')
                m = min(arr); coeff += 729; scale = 64 * 4**d
                nm = Fr(m, scale)
                if min_norm is None or nm < min_norm: min_norm = nm
                if m < 0: raise Fail(f'leaf {path!r}: negative Bernstein coefficient {m}')
                interior = 0
                for corner in itertools.product((0, 2), repeat=N):
                    if all((lo_gt0[i] if c == 0 else hi_lt1[i]) for i, c in enumerate(corner)):
                        interior += 1; corners += 1
                        v = arr[sum(c*s for c, s in zip(corner, STRIDE))]
                        if v <= 0: raise Fail(f'leaf {path!r}: open-cube vertex {corner} has coefficient {v}')
                        nv = Fr(v, scale)
                        if min_interior_norm is None or nv < min_interior_norm: min_interior_norm = nv
                if interior == 0: raise Fail(f'leaf {path!r}: no open-cube vertex')
                continue
            a = d % N; splits[a] += 1
            L, Rr = split_axis(arr, a)
            hiL = list(hi_lt1); hiL[a] = True; loR = list(lo_gt0); loR[a] = True
            stack.append((path+lower_bit, L, lo_gt0, tuple(hiL)))
            stack.append((path+upper_bit, Rr, tuple(loR), hi_lt1))
        if seen != len(S): raise Fail('not every leaf was reached')
        res.update(ok=True, leaves_verified=seen, coefficient_checks=coeff, open_cube_vertex_checks=corners,
                   min_depth=mind, max_depth=maxd, splits_per_axis=splits,
                   min_normalized_coefficient=str(min_norm), min_open_cube_vertex_value=str(min_interior_norm))
    except Fail as e:
        res.update(ok=False, reason=str(e))
    return res
QL = CERT['Q_positive_compactified_binary_leaf_paths']; HL = CERT['H_positive_compactified_binary_leaf_paths']
R['leaf_counts'] = {'Q': len(QL), 'H': len(HL), 'total': len(QL) + len(HL), 'all_binary_strings': all(set(p) <= {'0','1'} for p in QL + HL)}
t = time.time(); R['positive_Q'] = verify_cover(bernstein_root(Qpol), QL); R['positive_Q']['seconds'] = round(time.time() - t, 2)
t = time.time(); R['positive_H'] = verify_cover(bernstein_root(Hpol), HL); R['positive_H']['seconds'] = round(time.time() - t, 2)
assert R['positive_Q']['ok'] and R['positive_H']['ok'], (R['positive_Q'], R['positive_H'])

# ---------------------------------------------------------------- negative controls
ctrl = {}
zero6 = (0,)*N
Qflip = dict(Qpol); Qflip[zero6] = -Qflip[zero6]
ctrl['Q_constant_sign_flipped'] = {'digest_matches': canon_digest(Qflip) == CERT['Q_coefficients_sha256'], **verify_cover(bernstein_root(Qflip), QL)}
Qm1 = dict(Qpol); Qm1[zero6] -= 1
ctrl['Q_constant_minus_one'] = {'digest_matches': canon_digest(Qm1) == CERT['Q_coefficients_sha256'], **verify_cover(bernstein_root(Qm1), QL)}
Hflip = dict(Hpol); k_f1sq = (2,0,0,0,0,0); Hflip[k_f1sq] = -Hflip[k_f1sq]
ctrl['H_u0_squared_sign_flipped'] = {'digest_matches': canon_digest(Hflip) == CERT['H_coefficients_sha256'], **verify_cover(bernstein_root(Hflip), HL)}
ctrl['Q_missing_first_leaf'] = verify_cover(bernstein_root(Qpol), QL[1:])
ctrl['H_missing_middle_leaf'] = verify_cover(bernstein_root(Hpol), HL[:2500] + HL[2501:])
ctrl['Q_duplicate_leaf'] = verify_cover(bernstein_root(Qpol), QL + [QL[0]])
ctrl['Q_prefix_collision_leaf'] = verify_cover(bernstein_root(Qpol), QL + [QL[0] + '0'])
ctrl['Q_flipped_bit_convention'] = verify_cover(bernstein_root(Qpol), QL, lower_bit='1')
ctrl['H_flipped_bit_convention'] = verify_cover(bernstein_root(Hpol), HL, lower_bit='1')
def integerize(a):
    l = 1
    for v in a.values(): l = l * v.denominator // math.gcd(l, v.denominator)
    return to_int(pscale(a, l)), l
wrongz = {}
for z in (Fr(1, 2), Fr(1), Fr(7, 9), Fr(1, 1) + Fr(1, 9)):
    Dz = derive(z, F1, F2, F3, F4, N)
    Qz, lq = integerize(Dz['Qnum']); Hz, lh = integerize(Dz['Hnum'])
    Hz = {k: -v for k, v in Hz.items()}  # same sign convention as Hpol = -243*Hnum
    wrongz[str(z)] = {'D_coefficients': [str(c) for c in Dz['D']], 'Q_scale': lq, 'H_scale': lh,
        'Q_digest_matches': canon_digest(Qz) == CERT['Q_coefficients_sha256'],
        'H_digest_matches': canon_digest(Hz) == CERT['H_coefficients_sha256'],
        'Q_terms': len(Qz), 'H_terms': len(Hz), 'Q_value_at_all_ones': str(peval(Qz, [1]*6)), 'H_value_at_all_ones': str(peval(Hz, [1]*6)),
        'Q_cover': verify_cover(bernstein_root(Qz), QL), 'H_cover': verify_cover(bernstein_root(Hz), HL)}
ctrl['wrong_z'] = wrongz
R['negative_controls'] = ctrl

# ---------------------------------------------------------------- side claim: 8-arc shapes
shapes = []
for p2 in range(1, 7):
    s = 8 - p2
    for p1 in range(1, s):
        p3 = s - p1
        if p1 > p3 or (p1 == 1 and p3 == 1): continue
        cyc = sorted([p1 + p2, p3 + p2])
        shapes.append({'kind': 'theta', 'same_direction_paths': [p1, p3], 'return_path': p2, 'cycle_lengths': cyc, 'girth_ge_4': min(cyc) >= 4})
for L in range(2, 7):
    m = 8 - L
    if L > m: continue
    shapes.append({'kind': 'figure_eight', 'cycle_lengths': [L, m], 'girth_ge_4': min(L, m) >= 4})
R['eight_arc_shapes'] = {'count': len(shapes), 'girth_ge_4_count': sum(s['girth_ge_4'] for s in shapes),
    'girth_ge_5_count': sum(min(s['cycle_lengths']) >= 5 for s in shapes),
    'with_4_cycle_and_girth_ge_4': sum(s['girth_ge_4'] and min(s['cycle_lengths']) == 4 for s in shapes),
    'short_cycle_shapes': [s for s in shapes if not s['girth_ge_4']], 'shapes': shapes}

R['utc_end'] = utc(); R['wall_seconds'] = round(time.time() - W0, 2)
out = OUT/'reviewer-f129-engine-result-v1.json'
out.write_text(json.dumps(R, indent=1) + '\n')
print('Qpol digest match:', R['Qpol']['digest_matches_certificate'], '| Hpol digest match:', R['Hpol']['digest_matches_certificate'])
print('terms/degrees:', R['Qpol']['terms'], R['Qpol']['degrees'], R['Hpol']['terms'], R['Hpol']['degrees'])
print('literal f-form:', R['literal_f_form']['Qpol_matches_candidate'], R['literal_f_form']['Hpol_matches_candidate'])
print('closed forms:', R['closed_forms_match_candidate'])
print('CHAR spot:', {k: v for k, v in R['CHAR_spot_check'].items() if k not in ('arcs', 'four_cycles')})
print('elimination spot checks all ok:', all(all(v is True for kk, v in e.items() if isinstance(v, bool)) for e in elim))
print('positive Q:', R['positive_Q']); print('positive H:', R['positive_H'])
for k, v in ctrl.items():
    if k == 'wrong_z':
        for z, w in v.items(): print(f'wrong z={z}: Qdig={w["Q_digest_matches"]} Hdig={w["H_digest_matches"]} Qcover={w["Q_cover"].get("ok")} ({w["Q_cover"].get("reason","")}) Hcover={w["H_cover"].get("ok")} ({w["H_cover"].get("reason","")})')
    else: print(f'control {k}: ok={v.get("ok")} reason={v.get("reason","")} digest_matches={v.get("digest_matches")}')
print('shapes:', R['eight_arc_shapes']['count'], 'girth>=4:', R['eight_arc_shapes']['girth_ge_4_count'], 'girth>=5:', R['eight_arc_shapes']['girth_ge_5_count'])
print('wrote', out, 'wall', R['wall_seconds'], 's')
