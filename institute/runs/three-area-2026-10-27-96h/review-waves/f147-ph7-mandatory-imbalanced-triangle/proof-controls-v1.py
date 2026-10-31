#!/usr/bin/env python3
"""proof-controls-v1.py -- f147 PROOF-SLICE reviewer-written exact controls (stdlib only).

Written by the f147 proof-slice reviewer.  Imports/executes NO author or sibling code.
The author certificate JSON is opened only as DATA (polynomial-digest linkage).  All
arithmetic is exact (fractions.Fraction / int).  Writes exactly one file:
proof-controls-result-v1.json in this directory.

Sections
  S1  target polynomial D(y)(y^2+py+q) and the E4/E3/p/q coefficient identities (exact symbolic)
  S2  elimination identities E4=Ax+B, E3=h1x+h0, A*q=Qpol/81+(f1-4)E4, A*E3=-Hpol/243+h1*E4 (exact symbolic,
      7 variables), with wrong-constant mutation controls; Qpol/Hpol monomial counts + digest linkage
  S3  sample Qpol/Hpol evaluations at zero faces (SAMPLE ONLY, not a positivity proof)
  S4  exact rational 7x7 Metzler graph controls (Gv=0, v>0, squares so S rational):
        chi_G, chi_S by Faddeev-LeVerrier AND by full 5040-permutation cycle-type expansion;
        per-cycle-type and per-unoriented-cycle comparison at y^6..y^3;
        -S PSD by all 127 principal minors; left Perron vector by exact nullspace; Cauchy row
        inequality (S+kI)h<=kh with rigorous rational sqrt bounds; q>0 Hurwitz check;
        no-triangle / reducible-S / balanced / two-balanced / unbalanced / one-way / similarity /
        wrong-sign (positive spectral bound) controls.
"""
import hashlib, itertools, json, os, platform, sys, time
from fractions import Fraction as Fr
from math import isqrt

HERE = os.path.dirname(os.path.abspath(__file__))
CERT = ('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/'
        'phase-type/frontier-20261028-ph7-girth4-critical-bernstein-certificate.json')
N = 7
T0 = time.time()
R = {'script': os.path.basename(__file__), 'python': sys.version, 'platform': platform.platform(),
     'start_epoch': T0, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(T0)),
     'checks': [], 'failures': [], 'cases': {}}


def check(name, ok, **info):
    ok = bool(ok)
    R['checks'].append({'name': name, 'pass': ok, **info})
    if not ok:
        R['failures'].append(name)
    return ok


def fs(x):
    return str(Fr(x))


# ---------------------------------------------------------------- univariate polys (low->high)
def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0)) for i in range(n)]


def pmul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def pscale(a, c):
    return [x * c for x in a]


# ---------------------------------------------------------------- multivariate polys (exact)
class MP:
    NV = 7

    def __init__(self, d=None):
        self.d = {k: Fr(v) for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def var(i):
        k = [0] * MP.NV
        k[i] = 1
        return MP({tuple(k): 1})

    @staticmethod
    def const(c):
        return MP({(0,) * MP.NV: Fr(c)})

    def _c(self, o):
        return o if isinstance(o, MP) else MP.const(o)

    def __add__(self, o):
        o = self._c(o)
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, Fr(0)) + v
        return MP(d)

    __radd__ = __add__

    def __neg__(self):
        return MP({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-self._c(o))

    def __rsub__(self, o):
        return self._c(o) - self

    def __mul__(self, o):
        o = self._c(o)
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                d[k] = d.get(k, Fr(0)) + v1 * v2
        return MP(d)

    __rmul__ = __mul__

    def iszero(self):
        return not self.d

    def nterms(self):
        return len(self.d)

    def maxdeg_var(self, i):
        return max((k[i] for k in self.d), default=0)

    def ev(self, vals):
        s = Fr(0)
        for k, v in self.d.items():
            t = v
            for e, x in zip(k, vals):
                if e:
                    t *= Fr(x) ** e
            s += t
        return s


def esym(vars_, k):
    s = MP()
    for comb in itertools.combinations(vars_, k):
        t = MP.const(1)
        for v in comb:
            t = t * v
        s = s + t
    return s


# ---------------------------------------------------------------- matrices
def det(M):
    n = len(M)
    A = [[Fr(x) for x in row] for row in M]
    d = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                for k in range(c, n):
                    A[r][k] -= f * A[c][k]
    return d


def nullspace(M):
    n = len(M)
    A = [[Fr(x) for x in row] for row in M]
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, n) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        f = A[r][c]
        A[r] = [x / f for x in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                g = A[i][c]
                A[i] = [x - g * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        vec = [Fr(0)] * n
        vec[fc] = Fr(1)
        for i, pc in enumerate(piv):
            vec[pc] = -A[i][fc]
        basis.append(vec)
    return basis


def charpoly_FL(G):
    """det(yI-G) coefficients low->high via Faddeev-LeVerrier (exact)."""
    n = len(G)

    def mm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    c = [Fr(0)] * (n + 1)
    c[n] = Fr(1)
    M = [[Fr(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        M = mm(G, M)
        for i in range(n):
            M[i][i] += c[n - k + 1]
        c[n - k] = -sum(mm(G, M)[i][i] for i in range(n)) / k
    return c


def perm_expansion(G):
    """Full permutation expansion of det(yI-G).
    Returns (by_type, by_cycle): by_type maps sorted nontrivial-cycle-length tuple -> poly;
    by_cycle maps ('tri', frozenset(vertices)) or ('quad', frozenset(undirected edges)) -> poly
    for single-3-cycle and single-4-cycle permutations (both orientations summed)."""
    n = len(G)
    by_type, by_cycle = {}, {}
    for perm in itertools.permutations(range(n)):
        seen = [False] * n
        cycles = []
        for i in range(n):
            if not seen[i]:
                j = i
                cyc = []
                while not seen[j]:
                    seen[j] = True
                    cyc.append(j)
                    j = perm[j]
                cycles.append(cyc)
        sgn = (-1) ** (n - len(cycles))
        nontriv = [c for c in cycles if len(c) > 1]
        scalar = Fr(sgn)
        poly = [Fr(1)]
        for i in range(n):
            if perm[i] == i:
                poly = pmul(poly, [-G[i][i], Fr(1)])
            else:
                scalar *= -G[i][perm[i]]
        if scalar == 0:
            continue
        term = pscale(poly, scalar)
        key = tuple(sorted(len(c) for c in nontriv))
        by_type[key] = padd(by_type.get(key, [Fr(0)]), term)
        if len(nontriv) == 1 and len(nontriv[0]) in (3, 4):
            c = nontriv[0]
            if len(c) == 3:
                ck = ('tri', frozenset(c))
            else:
                ck = ('quad', frozenset(frozenset((c[t], c[(t + 1) % 4])) for t in range(4)))
            by_cycle[ck] = padd(by_cycle.get(ck, [Fr(0)]), term)
    return by_type, by_cycle


def rsqrt(q):
    q = Fr(q)
    assert q >= 0
    rn, rd = isqrt(q.numerator), isqrt(q.denominator)
    assert rn * rn == q.numerator and rd * rd == q.denominator, 'not a perfect square: %s' % q
    return Fr(rn, rd)


SC = 10 ** 40


def sqrt_bounds(q):
    """rigorous rational lb<=sqrt(q)<=ub"""
    q = Fr(q)
    nd = q.numerator * q.denominator
    m = isqrt(nd * SC * SC)
    return Fr(m, q.denominator * SC), Fr(m + 1, q.denominator * SC)


def build_G(off, v):
    G = [[Fr(0)] * N for _ in range(N)]
    for (i, j), r in off.items():
        assert i != j and Fr(r) > 0
        G[i][j] = Fr(r)
    for i in range(N):
        G[i][i] = -sum(G[i][j] * v[j] for j in range(N) if j != i) / v[i]
    return G


def S_of(G):
    S = [[Fr(0)] * N for _ in range(N)]
    for i in range(N):
        S[i][i] = G[i][i]
        for j in range(N):
            if i != j:
                S[i][j] = rsqrt(G[i][j] * G[j][i])
    return S


def strongly_connected(G):
    def reach(adj):
        seen = {0}
        st = [0]
        while st:
            u = st.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    st.append(w)
        return len(seen) == N
    adj = [[j for j in range(N) if j != i and G[i][j] > 0] for i in range(N)]
    radj = [[j for j in range(N) if j != i and G[j][i] > 0] for i in range(N)]
    return reach(adj) and reach(radj)


def all_principal_minors_nonneg(M):
    n = len(M)
    mn, zeros, ok, count = None, 0, True, 0
    for r in range(1, n + 1):
        for idx in itertools.combinations(range(n), r):
            d = det([[M[i][j] for j in idx] for i in idx])
            count += 1
            if d < 0:
                ok = False
            if d == 0:
                zeros += 1
            mn = d if mn is None else min(mn, d)
    return ok, mn, zeros, count


def triangle_products(G):
    out = {}
    for i, j, k in itertools.combinations(range(N), 3):
        P = G[i][j] * G[j][k] * G[k][i]
        Pp = G[i][k] * G[k][j] * G[j][i]
        out[(i, j, k)] = (P, Pp)
    return out


def quad_products(G):
    out = {}
    for quad in itertools.combinations(range(N), 4):
        a = quad[0]
        for rest in itertools.permutations(quad[1:]):
            cyc = (a,) + rest
            if cyc[1] > cyc[3]:
                continue  # one representative per unoriented 4-cycle
            P = Fr(1)
            Pp = Fr(1)
            for t in range(4):
                P *= G[cyc[t]][cyc[(t + 1) % 4]]
                Pp *= G[cyc[(t + 1) % 4]][cyc[t]]
            edges = frozenset(frozenset((cyc[t], cyc[(t + 1) % 4])) for t in range(4))
            out[edges] = (P, Pp, cyc)
    return out


# =============================================================== S1  target polynomial identities
D = pmul([Fr(0), Fr(1)], pmul([Fr(17, 9), Fr(2), Fr(1)], [Fr(17, 9), Fr(2), Fr(1)]))  # y[(y+1)^2+8/9]^2
check('S1.D_expansion', D == [Fr(0), Fr(289, 81), Fr(68, 9), Fr(70, 9), Fr(4), Fr(1)],
      D=[fs(x) for x in D])
# D(y)(y^2+py+q) coefficient formulas are linear in (p,q): verify at 4 affinely independent (p,q)
samples = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(3, 7), Fr(-5, 11))]
ok = True
for p, q in samples:
    chi = pmul(D, [q, p, Fr(1)])
    want = {6: p + 4, 5: q + 4 * p + Fr(70, 9), 4: 4 * q + Fr(70, 9) * p + Fr(68, 9),
            3: Fr(70, 9) * q + Fr(68, 9) * p + Fr(289, 81)}
    ok &= all(chi[k] == want[k] for k in want) and chi[7] == 1
check('S1.target_coefficients_y6_y5_y4_y3', ok, samples=[(fs(p), fs(q)) for p, q in samples])

lam = [MP.var(i) for i in range(7)]
e = {k: esym(lam, k) for k in range(1, 5)}
f = {k: esym(lam[:6], k) for k in range(1, 5)}
x = lam[6]
p = e[1] - 4
q = e[2] - 4 * p - Fr(70, 9)
E4 = e[3] - 4 * e[2] + Fr(74, 9) * e[1] - Fr(28, 3)
E3 = e[4] - Fr(70, 9) * e[2] + Fr(212, 9) * e[1] - Fr(1007, 27)
c4_target = 4 * q + Fr(70, 9) * p + Fr(68, 9)
c3_target = Fr(70, 9) * q + Fr(68, 9) * p + Fr(289, 81)
check('S1.E4_identity_e3_minus_target', (e[3] - c4_target - E4).iszero())
check('S1.E3_identity_e4_minus_target', (e[4] - c3_target - E3).iszero())
check('S1.q_identity', (q - (e[2] - 4 * e[1] + Fr(74, 9))).iszero())
# mutation: a wrong constant must break the identity
E3_bad = e[4] - Fr(70, 9) * e[2] + Fr(212, 9) * e[1] - Fr(1007, 28)
check('S1.mutation_wrong_constant_detected', not (e[4] - c3_target - E3_bad).iszero())

# =============================================================== S2  elimination identities
A = f[2] - 4 * f[1] + Fr(74, 9)
B = f[3] - 4 * f[2] + Fr(74, 9) * f[1] - Fr(28, 3)
h0 = f[4] - Fr(70, 9) * f[2] + Fr(212, 9) * f[1] - Fr(1007, 27)
h1 = f[3] - Fr(70, 9) * f[1] + Fr(212, 9)
Qpol = 81 * (A * A - (f[1] - 4) * B)
Hpol = -243 * (h0 * A - h1 * B)
check('S2.E4_eq_Ax_plus_B', (E4 - (A * x + B)).iszero())
check('S2.E3_eq_h1x_plus_h0', (E3 - (h1 * x + h0)).iszero())
check('S2.A_q_eq_Qpol81_plus_f1m4_E4', (A * q - Qpol * Fr(1, 81) - (f[1] - 4) * E4).iszero())
check('S2.A_E3_eq_minusHpol243_plus_h1_E4', (A * E3 + Hpol * Fr(1, 243) - h1 * E4).iszero())
check('S2.A_zero_forces_Qpol_eq_minus81_f1m4_B', ((Qpol - 81 * (A * A)) + 81 * (f[1] - 4) * B).iszero())
# mutation controls
A_bad = f[2] - 4 * f[1] + Fr(73, 9)
check('S2.mutation_wrong_A_detected', not (E4 - (A_bad * x + B)).iszero())
check('S2.mutation_wrong_Qpol_detected',
      not (A * q - (81 * (A * A - (f[1] - 4) * B) + 1) * Fr(1, 81) - (f[1] - 4) * E4).iszero())
# Qpol/Hpol are integer polynomials in six variables (x-free), 168/435 terms, degree<=2 per variable
check('S2.Qpol_Hpol_x_free', Qpol.maxdeg_var(6) == 0 and Hpol.maxdeg_var(6) == 0)
check('S2.Qpol_Hpol_integer_coefficients',
      all(v.denominator == 1 for v in Qpol.d.values()) and all(v.denominator == 1 for v in Hpol.d.values()))
check('S2.Qpol_Hpol_term_counts', Qpol.nterms() == 168 and Hpol.nterms() == 435,
      Q_terms=Qpol.nterms(), H_terms=Hpol.nterms())
check('S2.Qpol_Hpol_degree_per_variable_2',
      all(Qpol.maxdeg_var(i) == 2 for i in range(6)) and all(Hpol.maxdeg_var(i) == 2 for i in range(6)))


def digest6(P):
    rows = [[list(k[:6]), str(int(v))] for k, v in sorted(P.d.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


cert_bytes = open(CERT, 'rb').read()
cert_sha = hashlib.sha256(cert_bytes).hexdigest()
C = json.loads(cert_bytes)
R['certificate_sha256_observed'] = cert_sha
R['certificate_bytes'] = len(cert_bytes)
check('S2.certificate_sha_matches_manifest',
      cert_sha == 'b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8')
check('S2.Qpol_digest_linkage', digest6(Qpol) == C['Q_coefficients_sha256'], mine=digest6(Qpol))
check('S2.Hpol_digest_linkage', digest6(Hpol) == C['H_coefficients_sha256'], mine=digest6(Hpol))
check('S2.certificate_leaf_counts_as_stated',
      len(C['Q_positive_compactified_binary_leaf_paths']) == 5332
      and len(C['H_positive_compactified_binary_leaf_paths']) == 5334)
check('S2.certificate_identity_string_matches_my_elimination',
      C['identity'] == 'E4=A*u7+B; q=Q/(81*A); E3=-H/(243*A)', identity=C['identity'])
R['certificate_scope_string'] = C['scope']

# =============================================================== S3  SAMPLE positivity (not a proof)
pts = [(0, 0, 0, 0, 0, 0), (0, 1, 0, 2, 0, 3), (Fr(1, 3), 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 100),
       (5, 5, 5, 5, 5, 0), (0, 0, 0, Fr(7, 2), Fr(7, 2), Fr(7, 2)), (1, 2, 3, 4, 5, 6), (0, 0, 2, 2, 0, 0)]
S3 = []
for pt in pts:
    vals = list(pt) + [0]
    qv, hv = Qpol.ev(vals), Hpol.ev(vals)
    S3.append({'point': [fs(t) for t in pt], 'Qpol': fs(qv), 'Hpol': fs(hv)})
check('S3.sample_zero_face_positivity_SAMPLE_ONLY', all(Fr(s['Qpol']) > 0 and Fr(s['Hpol']) > 0 for s in S3),
      samples=S3, note='sample evaluations only; full [0,inf)^6 positivity is the certificate-slice dependency')
check('S3.origin_values', Fr(S3[0]['Qpol']) == 2452 and Fr(S3[0]['Hpol']) == 21094)


# =============================================================== S4  graph controls
def analyze(name, G, expect):
    """expect: dict with keys irreducible(bool), triangles('none'|'balanced'|'unbalanced'),
    y4_equal(bool), y3_strict(bool|None), all_equal(bool), psd(bool)"""
    rec = {'expect': {k: ([fs(t) for t in val] if k == 'v' else val) for k, val in expect.items()}}
    irr = strongly_connected(G)
    rec['irreducible'] = irr
    check(f'{name}.irreducible_as_expected', irr == expect['irreducible'])
    S = S_of(G)
    rec['G'] = [[fs(x) for x in row] for row in G]
    rec['S'] = [[fs(x) for x in row] for row in S]
    rec['diag_negative'] = all(G[i][i] < 0 for i in range(N))
    tri = triangle_products(G)
    nz = {str(list(k)): (fs(P), fs(Pp)) for k, (P, Pp) in tri.items() if P or Pp}
    rec['triangles'] = nz
    if expect['triangles'] == 'none':
        check(f'{name}.no_directed_3cycle', not nz)
    elif expect['triangles'] == 'balanced':
        check(f'{name}.triangles_present_all_balanced', nz and all(P == Pp for P, Pp in tri.values()))
    else:
        check(f'{name}.some_triangle_unbalanced', any(P != Pp for P, Pp in tri.values()))
    quads = quad_products(G)
    rec['quad_cycles'] = [{'cycle': list(c), 'P': fs(P), 'Pp': fs(Pp)} for _, (P, Pp, c) in quads.items() if P or Pp]
    # characteristic polynomials: two independent methods each
    cG, cS = charpoly_FL(G), charpoly_FL(S)
    tG, qG = perm_expansion(G)
    tS, qS = perm_expansion(S)
    sumG = [Fr(0)] * (N + 1)
    for v in tG.values():
        sumG = padd(sumG, v)
    sumS = [Fr(0)] * (N + 1)
    for v in tS.values():
        sumS = padd(sumS, v)
    check(f'{name}.charpoly_FL_equals_permutation_expansion', sumG == cG and sumS == cS)
    rec['chi_G'] = [fs(c) for c in cG]
    rec['chi_S'] = [fs(c) for c in cS]
    rec['coef_diff_G_minus_S'] = {f'y{k}': fs(cG[k] - cS[k]) for k in range(N + 1)}
    check(f'{name}.y6_y5_equal', cG[6] == cS[6] and cG[5] == cS[5])
    check(f'{name}.y4_equal_as_expected', (cG[4] == cS[4]) == expect['y4_equal'],
          diff=fs(cG[4] - cS[4]))
    check(f'{name}.y4_direction_G_le_S', cG[4] <= cS[4])
    check(f'{name}.y3_direction_G_le_S', cG[3] <= cS[3], diff=fs(cG[3] - cS[3]))
    if expect['y3_strict'] is not None:
        check(f'{name}.y3_strict_as_expected', (cG[3] < cS[3]) == expect['y3_strict'])
    check(f'{name}.all_coefficients_equal_as_expected', (cG == cS) == expect['all_equal'])
    # per cycle-type comparison through y^3
    types_cmp = {}
    for key in sorted(set(tG) | set(tS), key=lambda t: (len(t), t)):
        a = tG.get(key, [Fr(0)] * (N + 1))
        b = tS.get(key, [Fr(0)] * (N + 1))
        a = a + [Fr(0)] * (N + 1 - len(a))
        b = b + [Fr(0)] * (N + 1 - len(b))
        types_cmp[str(key)] = {f'y{k}': fs(a[k] - b[k]) for k in range(3, 7)}
    rec['cycle_type_G_minus_S_y6_y5_y4_y3'] = types_cmp

    def tdiff(key, k):
        a = tG.get(key, [Fr(0)] * (N + 1))
        b = tS.get(key, [Fr(0)] * (N + 1))
        a = a + [Fr(0)] * (N + 1 - len(a))
        b = b + [Fr(0)] * (N + 1 - len(b))
        return a[k] - b[k]
    check(f'{name}.types_identity_2_22_identical_through_y3',
          all(tdiff(key, k) == 0 for key in [(), (2,), (2, 2)] for k in range(3, 7)))
    check(f'{name}.type3_y4_y3_equal_iff_balanced',
          ((tdiff((3,), 4) == 0 and tdiff((3,), 3) == 0) == (expect['triangles'] != 'unbalanced')))
    check(f'{name}.type3_direction_G_le_S', tdiff((3,), 4) <= 0 and tdiff((3,), 3) <= 0)
    check(f'{name}.type4_y3_direction_G_le_S', tdiff((4,), 3) <= 0)
    # per-unoriented-cycle AM-GM checks
    tri_cmp, quad_cmp = [], []
    for ck in sorted(set(qG) | set(qS), key=str):
        a = qG.get(ck, [Fr(0)] * (N + 1))
        b = qS.get(ck, [Fr(0)] * (N + 1))
        a = a + [Fr(0)] * (N + 1 - len(a))
        b = b + [Fr(0)] * (N + 1 - len(b))
        if ck[0] == 'tri':
            i, j, k = sorted(ck[1])
            P, Pp = tri[(i, j, k)]
            outside = sum(G[l][l] for l in range(N) if l not in ck[1])
            # G: y4 -> -(P+Pp), y3 -> (P+Pp)*outside ; S: with 2sqrt(P Pp)
            s2 = 2 * rsqrt(P * Pp)
            okk = (a[4] == -(P + Pp) and b[4] == -s2 and a[3] == (P + Pp) * outside and b[3] == s2 * outside
                   and a[4] <= b[4] and a[3] <= b[3])
            tri_cmp.append({'vertices': [i, j, k], 'P': fs(P), 'Pp': fs(Pp), 'outside_diag_sum': fs(outside),
                            'G_y4': fs(a[4]), 'S_y4': fs(b[4]), 'G_y3': fs(a[3]), 'S_y3': fs(b[3]), 'ok': okk})
        else:
            P, Pp, cyc = quads[ck[1]]
            s2 = 2 * rsqrt(P * Pp)
            okk = (a[3] == -(P + Pp) and b[3] == -s2 and a[3] <= b[3])
            quad_cmp.append({'cycle': list(cyc), 'P': fs(P), 'Pp': fs(Pp), 'G_y3': fs(a[3]), 'S_y3': fs(b[3]),
                             'strict': a[3] < b[3], 'ok': okk})
    rec['triangle_cover_terms'] = tri_cmp
    rec['quad_cover_terms'] = quad_cmp
    check(f'{name}.triangle_cover_terms_exact', all(t['ok'] for t in tri_cmp))
    check(f'{name}.quad_cover_terms_exact_AMGM', all(t['ok'] for t in quad_cmp))
    # wrong-sign: the reversed inequality must FAIL whenever any quad is strict
    if any(t['strict'] for t in quad_cmp):
        check(f'{name}.reversed_y3_inequality_fails', not (cG[3] >= cS[3]))
    # -S PSD via all principal minors
    negS = [[-S[i][j] for j in range(N)] for i in range(N)]
    psd, mn, zeros, cnt = all_principal_minors_nonneg(negS)
    rec['negS_principal_minors'] = {'count': cnt, 'all_nonneg': psd, 'min': fs(mn), 'zero_minors': zeros}
    check(f'{name}.negS_psd_as_expected', psd == expect['psd'])
    # S reducible?
    sadj = [[j for j in range(N) if j != i and S[i][j] > 0] for i in range(N)]
    seen = {0}
    st = [0]
    while st:
        u = st.pop()
        for w in sadj[u]:
            if w not in seen:
                seen.add(w)
                st.append(w)
    rec['S_irreducible'] = len(seen) == N
    if 'S_reducible' in expect:
        check(f'{name}.S_reducible_as_expected', (len(seen) != N) == expect['S_reducible'])
    if irr:
        # Perron data: Gv=0 (v known), left vector w from exact nullspace of G^T
        v = expect['v']
        check(f'{name}.Gv_zero', all(sum(G[i][j] * v[j] for j in range(N)) == 0 for i in range(N)))
        GT = [[G[j][i] for j in range(N)] for i in range(N)]
        ns = nullspace(GT)
        check(f'{name}.left_nullspace_dim1', len(ns) == 1)
        w = ns[0]
        if any(t < 0 for t in w):
            w = [-t for t in w]
        check(f'{name}.left_perron_positive', all(t > 0 for t in w))
        rec['v'] = [fs(t) for t in v]
        rec['w'] = [fs(t) for t in w]
        kk = max(-G[i][i] for i in range(N))
        rows = []
        allok = True

        def is_sq(qq):
            qq = Fr(qq)
            return isqrt(qq.numerator) ** 2 == qq.numerator and isqrt(qq.denominator) ** 2 == qq.denominator
        exact_h = all(is_sq(v[j] * w[j]) for j in range(N))
        rec['cauchy_h_all_rational'] = exact_h
        for i in range(N):
            if exact_h:
                # h_j rational: evaluate (S+kI)h <= k h exactly (equality allowed)
                lhs = sum((S[i][j] + (kk if i == j else 0)) * rsqrt(v[j] * w[j]) for j in range(N))
                rhs = kk * rsqrt(v[i] * w[i])
                rows.append({'row': i, 'exact_margin': fs(rhs - lhs), 'ok': rhs >= lhs, 'tight': rhs == lhs})
                allok &= rhs >= lhs
            else:
                lhs_ub = Fr(0)
                for j in range(N):
                    coef = S[i][j] + (kk if i == j else 0)
                    assert coef >= 0
                    if coef:
                        lhs_ub += coef * sqrt_bounds(v[j] * w[j])[1]
                rhs_lb = kk * sqrt_bounds(v[i] * w[i])[0]
                margin = rhs_lb - lhs_ub
                rows.append({'row': i, 'margin_lb': fs(margin), 'rigorous': margin > 0})
                allok &= margin > 0
        rec['cauchy_rows_k'] = fs(kk)
        rec['cauchy_rows'] = rows
        check(f'{name}.cauchy_row_inequality_' + ('exact' if exact_h else 'rigorous_bounds'), allok)
        # q>0 Hurwitz sanity: the actual quadratic quotient is not defined for controls (D does not divide chi_G);
        # instead verify spectral facts used: 0 is a simple root of chi_G (c0=0, c1!=0) and all other real
        # roots negative is implied by Perron; here check c0==0 and c1!=0 exactly
        check(f'{name}.zero_is_simple_eigenvalue', cG[0] == 0 and cG[1] != 0)
        # e_j of -S from chi_S and the derived p,q,E4,E3 values (record only)
        e1, e2, e3, e4 = cS[6], cS[5], cS[4], cS[3]
        pv = e1 - 4
        qv = e2 - 4 * pv - Fr(70, 9)
        rec['derived_from_S'] = {'e1': fs(e1), 'e2': fs(e2), 'e3': fs(e3), 'e4': fs(e4), 'p': fs(pv), 'q': fs(qv),
                                 'E4': fs(e3 - 4 * e2 + Fr(74, 9) * e1 - Fr(28, 3)),
                                 'E3': fs(e4 - Fr(70, 9) * e2 + Fr(212, 9) * e1 - Fr(1007, 27))}
    R['cases'][name] = rec


one = [Fr(1)] * N
# N1: no triangle, 2-cycles, unbalanced bidirectional 4-cycle, one-way 4-cycles via 1->4
N1 = {(0, 1): 2, (1, 0): 8, (1, 2): 1, (2, 1): 9, (2, 3): 3, (3, 2): 12, (3, 4): Fr(1, 2), (4, 3): 2,
      (4, 5): 5, (5, 4): 5, (5, 6): 1, (6, 5): 4, (6, 0): 3, (0, 6): 27, (0, 3): 2, (3, 0): 18, (1, 4): 7}
vN1 = [Fr(t) for t in (1, 2, 3, 1, 2, 1, 3)]
analyze('N1_no_triangle_oneway_quads', build_G(N1, vN1),
        dict(irreducible=True, triangles='none', y4_equal=True, y3_strict=True, all_equal=False, psd=True, v=vN1))
# N2: one-way 7-cycle + one bidirectional chord -> S reducible, no triangle, one-way 4-cycle
N2 = {(0, 1): 1, (1, 2): 2, (2, 3): 3, (3, 4): 1, (4, 5): 2, (5, 6): 1, (6, 0): 3, (2, 5): 2, (5, 2): 8}
analyze('N2_reducible_S_oneway_cycle', build_G(N2, one),
        dict(irreducible=True, triangles='none', y4_equal=True, y3_strict=True, all_equal=False, psd=True,
             S_reducible=True, v=one))
# B1: one balanced triangle {0,1,2} (18=18), unbalanced 4-cycles {3,4,5,6},{0,2,3,6}
B1 = {(0, 1): 2, (1, 0): 8, (1, 2): 1, (2, 1): 9, (2, 0): 9, (0, 2): Fr(1, 4), (2, 3): 3, (3, 2): 12,
      (3, 4): Fr(1, 2), (4, 3): 2, (4, 5): 5, (5, 4): 5, (5, 6): 1, (6, 5): 4, (6, 0): 3, (0, 6): 27,
      (3, 6): 2, (6, 3): 18}
vB1 = [Fr(t) for t in (1, 1, 2, 1, 3, 1, 2)]
analyze('B1_one_balanced_triangle', build_G(B1, vB1),
        dict(irreducible=True, triangles='balanced', y4_equal=True, y3_strict=True, all_equal=False, psd=True, v=vB1))
# B2: three balanced triangles {0,1,2},{0,2,3},{4,5,6}; balanced quad {0,1,2,3}; unbalanced quad {3,4,6,0}
B2 = {(0, 1): 2, (1, 0): 8, (1, 2): 1, (2, 1): 9, (2, 0): 9, (0, 2): Fr(1, 4), (2, 3): 3, (3, 2): 12,
      (0, 3): Fr(1, 4), (3, 0): 36, (3, 4): Fr(1, 2), (4, 3): 2, (4, 5): 5, (5, 4): 5, (5, 6): 1, (6, 5): 4,
      (4, 6): Fr(1, 2), (6, 4): 2, (6, 0): 3, (0, 6): 27}
vB2 = [Fr(t) for t in (2, 1, 1, 3, 1, 2, 1)]
analyze('B2_three_balanced_triangles_shared_edge', build_G(B2, vB2),
        dict(irreducible=True, triangles='balanced', y4_equal=True, y3_strict=True, all_equal=False, psd=True, v=vB2))
# B3: balanced triangle, NO 4-cycles at all -> y3 must be EQUAL (tests that only 4-cycles move y3)
B3 = {(0, 1): 2, (1, 0): 8, (1, 2): 1, (2, 1): 9, (2, 0): 9, (0, 2): Fr(1, 4), (2, 3): 3, (3, 2): 12,
      (3, 4): Fr(1, 2), (4, 3): 2, (4, 5): 5, (5, 4): 5, (5, 6): 1, (6, 5): 4, (6, 0): 3, (0, 6): 27}
analyze('B3_balanced_triangle_no_quads', build_G(B3, vB1),
        dict(irreducible=True, triangles='balanced', y4_equal=True, y3_strict=False, all_equal=False, psd=True, v=vB1))
# U1: B1 with triangle made unbalanced (8 vs 72): y4 equality must FAIL (hypothesis is load-bearing)
U1 = dict(B1)
U1[(2, 0)] = 4
U1[(0, 2)] = 1
analyze('U1_unbalanced_triangle_negative_control', build_G(U1, vB1),
        dict(irreducible=True, triangles='unbalanced', y4_equal=False, y3_strict=True, all_equal=False, psd=True, v=vB1))
# U2: one-way triangle 0->1->2->0 only
U2 = {(0, 1): 1, (1, 2): 2, (2, 0): 3, (2, 3): 1, (3, 2): 4, (3, 4): 2, (4, 3): 8, (4, 5): 1, (5, 4): 1,
      (5, 6): 3, (6, 5): 12, (6, 0): 1, (0, 6): 1}
analyze('U2_oneway_triangle_negative_control', build_G(U2, one),
        dict(irreducible=True, triangles='unbalanced', y4_equal=False, y3_strict=None, all_equal=False, psd=True, v=one))
# P1: G = D S0 D^{-1}: every cycle balanced; chi_G == chi_S exactly (positive control)
S0off = {frozenset((0, 1)): 1, frozenset((1, 2)): 2, frozenset((2, 3)): 1, frozenset((3, 4)): 3, frozenset((4, 5)): 1,
         frozenset((5, 6)): 2, frozenset((6, 0)): 1, frozenset((0, 3)): 1, frozenset((1, 4)): 2, frozenset((0, 2)): 1}
u = [Fr(t) for t in (1, 2, 1, 1, 2, 1, 1)]
dd = [Fr(t) for t in (1, 2, 3, 1, 2, 1, 4)]
S0 = [[Fr(0)] * N for _ in range(N)]
for ed, r in S0off.items():
    i, j = sorted(ed)
    S0[i][j] = S0[j][i] = Fr(r)
for i in range(N):
    S0[i][i] = -sum(S0[i][j] * u[j] for j in range(N) if j != i) / u[i]
GP1 = [[dd[i] * S0[i][j] / dd[j] for j in range(N)] for i in range(N)]
vP1 = [dd[i] * u[i] for i in range(N)]
analyze('P1_diagonal_similarity_all_balanced', GP1,
        dict(irreducible=True, triangles='balanced', y4_equal=True, y3_strict=False, all_equal=True, psd=True, v=vP1))
check('P1.S_equals_S0', S_of(GP1) == S0)
# R0: wrong-sign control: positive spectral bound (zero diagonal) -> -S not PSD
GB1 = build_G(B1, vB1)
GR0 = [[GB1[i][j] if i != j else Fr(0) for j in range(N)] for i in range(N)]
SR0 = S_of(GR0)
psdR0, mnR0, _, _ = all_principal_minors_nonneg([[-SR0[i][j] for j in range(N)] for i in range(N)])
check('R0_positive_spectral_bound_breaks_S_le_0', not psdR0, min_minor=fs(mnR0))
R['cases']['R0_positive_spectral_bound'] = {'note': 'B1 off-diagonals with zero diagonal; -S fails PSD', 'min_minor': fs(mnR0)}

# ---------------------------------------------------------------- finish
R['n_checks'] = len(R['checks'])
R['n_failures'] = len(R['failures'])
R['elapsed_s'] = time.time() - T0
R['end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
R['verdict'] = 'ALL_CONTROLS_PASS' if not R['failures'] else 'CONTROL_FAILURES'
out = os.path.join(HERE, 'proof-controls-result-v1.json')
with open(out, 'w') as fh:
    json.dump(R, fh, indent=1, sort_keys=False)
print(R['verdict'], R['n_checks'], 'checks', R['n_failures'], 'failures', 'elapsed %.1fs' % R['elapsed_s'])
for c in R['checks']:
    if not c['pass']:
        print('FAIL', c['name'], {k: v for k, v in c.items() if k not in ('name', 'pass')})
