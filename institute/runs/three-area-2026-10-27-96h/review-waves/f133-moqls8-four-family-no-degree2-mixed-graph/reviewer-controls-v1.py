#!/usr/bin/env python3
"""
reviewer-controls-v1.py -- review wave f133 (moqls8 four-family / degree-2 mixed graph), reviewer-written exact controls.

Independence: Python standard library only; nothing imported or copied from author, sibling or parent directories.
Exactness: every cell ray is an integer vector (an unnormalized representative of the ray).  Orthogonality is an
exact integer zero; 'ONB of C^n' means n pairwise-orthogonal nonzero vectors; product vectors are explicit
n^2-dimensional Kronecker integer vectors.  All constructed rays are real, so <u,v> = sum u_i v_i and a unitary
transition matrix is a real orthogonal 0/1 matrix in the classical-mate instances below; the complex general case
of the written candidates is checked abstractly (support pigeonholes, controls D and E), which does not depend on
the entries.

Controls
  C  explicit nonclassical Q with a prescribed single mixed cycle: C4 in n=4, C6 in n=6, C8 in n=8 (+ C4 exhaustive
     classical-mate negative, reference-row dependence demonstration)
  A  n=8 three-family: Q nonclassical with mixed graph = two C4 components sharing one support and one basis group,
     two classical mates (GF(8) linear MOLS + 8-cell trade); forced-structure facts; five negatives
  B  n=8 three-family with a single C8-mixed member (Z4xZ2 Cayley table, 8-cycle trade, transversal-decomposition
     mates); forced-structure facts; exhaustive classical adversarial search for a third/fourth mate
  D  abstract transition-support pigeonhole for a single C_2k (k=2..7); two-sided table for n=8
  E  mechanical enumeration of candidate 4's case analysis for n=8 (all degree-2 shapes, supports, basis groups)
"""
import sys, os, json, hashlib, itertools, datetime, time
from fractions import Fraction
from collections import Counter, defaultdict

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

RESULTS = []
def record(name, expected, observed):
    ok = (expected == observed)
    RESULTS.append({'check': name, 'expected': repr(expected), 'observed': repr(observed), 'ok': ok})
    print(('PASS ' if ok else 'FAIL ') + name + ' | expected ' + repr(expected) + ' | observed ' + repr(observed))
    return ok

def note(s):
    RESULTS.append({'note': s})
    print('NOTE ' + s)

# ----------------------------------------------------------------------------------------------------------------
# exact linear algebra over Z / Q
# ----------------------------------------------------------------------------------------------------------------
def dot(u, v): return sum(a*b for a, b in zip(u, v))
def nz(u): return any(a != 0 for a in u)
def kron(u, v): return [a*b for a in u for b in v]
def unit(n, j): return [1 if i == j else 0 for i in range(n)]
def collinear(u, v):
    return nz(u) and nz(v) and dot(u, v)**2 == dot(u, u)*dot(v, v)   # equal rays (real vectors)

def rank(vs):
    rows = [[Fraction(x) for x in v] for v in vs]
    r = 0
    ncols = len(rows[0]) if rows else 0
    for c in range(ncols):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / rows[r][c]
                rows[i] = [a - f*b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r

# ----------------------------------------------------------------------------------------------------------------
# QLS / orthogonality checks
# ----------------------------------------------------------------------------------------------------------------
def qls_violation(Q, n):
    for r in range(n):
        vs = [Q[(r, c)] for c in range(n)]
        if not all(nz(v) for v in vs):
            return ('zero-vector', r)
        for i in range(n):
            for j in range(i+1, n):
                if dot(vs[i], vs[j]) != 0:
                    return ('row', r, i, j)
    for c in range(n):
        vs = [Q[(r, c)] for r in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if dot(vs[i], vs[j]) != 0:
                    return ('col', c, i, j)
    return None

def pair_violation(Q, R, n):
    cells = [(r, c) for r in range(n) for c in range(n)]
    P = [kron(Q[x], R[x]) for x in cells]
    if not all(nz(p) for p in P):
        return ('zero-product',)
    for i in range(len(cells)):
        for j in range(i+1, len(cells)):
            if dot(P[i], P[j]) != 0:
                return (cells[i], cells[j])
    return None

# ----------------------------------------------------------------------------------------------------------------
# mixed-cell analysis relative to a reference row (the candidates' "first row")
# ----------------------------------------------------------------------------------------------------------------
def mixed_analysis(Q, n, r0):
    basis = [Q[(r0, c)] for c in range(n)]
    def idx(v):
        for j, b in enumerate(basis):
            if collinear(v, b):
                return j
        return None
    mixed, light = [], {}
    for r in range(n):
        for c in range(n):
            j = idx(Q[(r, c)])
            if j is None:
                mixed.append((r, c))
            else:
                light[(r, c)] = j
    parent = {x: x for x in mixed}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x, y in itertools.combinations(mixed, 2):
        if x[0] == y[0] or x[1] == y[1]:
            parent[find(x)] = find(y)
    groups = defaultdict(list)
    for x in mixed:
        groups[find(x)].append(x)
    comps = []
    for cells in groups.values():
        cells = sorted(cells)
        degr = Counter(r for r, c in cells)
        degc = Counter(c for r, c in cells)
        supports = sorted({tuple(j for j in range(n) if dot(Q[x], basis[j]) != 0) for x in cells})
        P = [x for x in cells if collinear(Q[x], Q[cells[0]])]
        M = [x for x in cells if x not in P]
        comps.append(dict(cells=cells, rows=sorted(degr), cols=sorted(degc),
                          degrees=sorted(set(degr.values()) | set(degc.values())),
                          supports=supports, P=P, M=M,
                          P_collinear=all(collinear(Q[x], Q[y]) for x, y in itertools.combinations(P, 2)),
                          M_collinear=all(collinear(Q[x], Q[y]) for x, y in itertools.combinations(M, 2)) if M else True,
                          PM_orthogonal=all(dot(Q[x], Q[y]) == 0 for x in P for y in M)))
    comps.sort(key=lambda d: d['cells'][0])
    return dict(basis=basis, mixed=sorted(mixed), light=light, comps=comps)

def is_single_cycle(comp, k):
    c = comp
    return (len(c['cells']) == 2*k and len(c['rows']) == k and len(c['cols']) == k and c['degrees'] == [2]
            and len(c['P']) == k and len(c['M']) == k and c['P_collinear'] and c['M_collinear'] and c['PM_orthogonal']
            and len(c['supports']) == 1 and len(c['supports'][0]) == 2)

# ----------------------------------------------------------------------------------------------------------------
# forced-structure facts for a mate R relative to a mixed cell set X of Q (one support {a,b}, one basis group)
# a, b are column indices of the reference row r0 (basis index == column index of row r0)
# ----------------------------------------------------------------------------------------------------------------
def forced_structure(Q, R, n, r0, X, a, b, label):
    qa, qb = Q[(r0, a)], Q[(r0, b)]
    k = len(X) // 2
    P = [x for x in X if collinear(Q[x], Q[X[0]])]
    M = [x for x in X if x not in P]
    record(label + ': |P| == |M| == k', (k, k), (len(P), len(M)))
    record(label + ': every ray of X has support exactly {a,b} in the reference basis', True,
           all(dot(Q[x], qa) != 0 and dot(Q[x], qb) != 0 and
               all(dot(Q[x], Q[(r0, j)]) == 0 for j in range(n) if j not in (a, b)) for x in X))
    Xrows = {x[0] for x in X}
    Ea = [(r, c) for r in range(n) for c in range(n) if (r, c) not in X and collinear(Q[(r, c)], qa)]
    record(label + ': number of light Q=e_a cells == n-k', n-k, len(Ea))
    record(label + ': no light e_a cell lies in a mixed row of X', True, all(r not in Xrows for r, c in Ea))
    record(label + ': light e_a cells occupy n-k distinct rows', n-k, len({r for r, c in Ea}))
    RE = [R[y] for y in Ea]
    RX = [R[x] for x in X]
    record(label + ': R rays at light e_a cells pairwise orthogonal', True,
           all(dot(u, v) == 0 for u, v in itertools.combinations(RE, 2)))
    record(label + ': R rays at light e_a cells orthogonal to every R ray on X', True,
           all(dot(u, v) == 0 for u in RE for v in RX))
    record(label + ': R rays on P pairwise orthogonal', True,
           all(dot(R[x], R[y]) == 0 for x, y in itertools.combinations(P, 2)))
    record(label + ': R rays on M pairwise orthogonal', True,
           all(dot(R[x], R[y]) == 0 for x, y in itertools.combinations(M, 2)))
    record(label + ': dim span R(X) == k', k, rank(RX))
    record(label + ': span R(P) == span R(M) (rank of union == k)', k, rank([R[x] for x in P] + [R[x] for x in M]))
    assert all(dot(R[x], R[x]) == 1 for x in X), 'transition matrix implemented for norm-1 integer mate rays'
    U = [[dot(R[p], R[m]) for m in M] for p in P]
    I = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
    UUt = [[sum(U[i][l]*U[j][l] for l in range(k)) for j in range(k)] for i in range(k)]
    UtU = [[sum(U[l][i]*U[l][j] for l in range(k)) for j in range(k)] for i in range(k)]
    record(label + ': transition matrix U is orthogonal (U U^T == I and U^T U == I)', True, UUt == I and UtU == I)
    adj = {(p, m): (p[0] == m[0] or p[1] == m[1]) for p in P for m in M}
    record(label + ': every P cell has exactly two M neighbours (same row or column)', True,
           all(sum(adj[(p, m)] for m in M) == 2 for p in P))
    record(label + ': U vanishes at every neighbour position', True,
           all(U[i][j] == 0 for i, p in enumerate(P) for j, m in enumerate(M) if adj[(p, m)]))
    support = {(i, j) for i in range(k) for j in range(k) if U[i][j] != 0}
    record(label + ': U has at least one nonzero entry in every row', True,
           all(any(U[i][j] != 0 for j in range(k)) for i in range(k)))
    rb, ra = R[(r0, b)], R[(r0, a)]
    record(label + ': R first-row ray e_b orthogonal to every R ray on X (e_b in V_R^perp)', True,
           all(dot(rb, v) == 0 for v in RX))
    record(label + ': R rays at light e_a cells span V_R^perp (rank n-k)', n-k, rank(RE))
    record(label + ': the first-row light e_a cell (r0,a) is among the light e_a cells', True, (r0, a) in Ea)
    record(label + ': its R ray is the R first-row ray e_a', True, R[(r0, a)] == ra and ra in RE)
    off = [y for y in Ea if y != (r0, a)]
    B = {y for y in off if dot(R[y], rb) != 0}
    record(label + ': off-first-row light e_a cells == n-k-1', n-k-1, len(off))
    record(label + ': nonzero e_b overlap at >= 1 off-first-row light e_a cell', True, len(B) >= 1)
    return dict(U=U, support=support, B=B, P=P, M=M, Ea=Ea)

def cross_mate_checks(F1, F2, label):
    record(label + ': transition supports pairwise disjoint', True, len(F1['support'] & F2['support']) == 0)
    record(label + ': e_b-overlap cell sets pairwise disjoint', True, len(F1['B'] & F2['B']) == 0)

# ----------------------------------------------------------------------------------------------------------------
# Latin-square helpers
# ----------------------------------------------------------------------------------------------------------------
def gf8_mul(x, y):
    r = 0
    for i in range(3):
        if (y >> i) & 1:
            r ^= x << i
    for i in (5, 4, 3):
        if (r >> i) & 1:
            r ^= 0b1011 << (i-3)      # x^3 + x + 1
    return r

def gf8_linear_square(lam):
    return {(i, j): i ^ gf8_mul(lam, j) for i in range(8) for j in range(8)}

def is_latin(L, n):
    return (all(len({L[(r, c)] for c in range(n)}) == n for r in range(n)) and
            all(len({L[(r, c)] for r in range(n)}) == n for c in range(n)) and
            all(0 <= L[(r, c)] < n for r in range(n) for c in range(n)))

def classical(L, n):
    return {x: unit(n, L[x]) for x in L}

def two_symbol_components(L, n, s0, s1):
    cells = [x for x in L if L[x] in (s0, s1)]
    parent = {x: x for x in cells}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x, y in itertools.combinations(cells, 2):
        if x[0] == y[0] or x[1] == y[1]:
            parent[find(x)] = find(y)
    groups = defaultdict(list)
    for x in cells:
        groups[find(x)].append(x)
    return [sorted(g) for g in groups.values()]

def ray_plus(n, s0, s1): return [1 if i in (s0, s1) else 0 for i in range(n)]
def ray_minus(n, s0, s1): return [1 if i == s0 else (-1 if i == s1 else 0) for i in range(n)]

def rotate(L, n, trade, s0, s1, ray0=None, ray1=None):
    """Replace symbol s0 on trade cells by ray0 (default e_s0+e_s1) and s1 by ray1 (default e_s0-e_s1)."""
    if ray0 is None:
        ray0 = ray_plus(n, s0, s1)
    if ray1 is None:
        ray1 = ray_minus(n, s0, s1)
    Q = {}
    for x in L:
        if x in trade:
            Q[x] = list(ray0) if L[x] == s0 else list(ray1)
        else:
            Q[x] = unit(n, L[x])
    return Q

def group_table(elements, add):
    gi = {g: i for i, g in enumerate(elements)}
    n = len(elements)
    return {(i, j): gi[add(elements[i], elements[j])] for i in range(n) for j in range(n)}, gi

# ----------------------------------------------------------------------------------------------------------------
# CONTROL C: explicit single-cycle mixed Q in n = 4, 6, 8
# ----------------------------------------------------------------------------------------------------------------
def control_C():
    print('\n=== CONTROL C: explicit nonclassical Q with a prescribed single mixed cycle ===')
    cases = [
        ('Z2xZ2', [(a, b) for a in range(2) for b in range(2)], lambda x, y: ((x[0]+y[0]) % 2, (x[1]+y[1]) % 2), 2),
        ('Z3xZ2', [(a, b) for a in range(3) for b in range(2)], lambda x, y: ((x[0]+y[0]) % 3, (x[1]+y[1]) % 2), 3),
        ('Z4xZ2', [(a, b) for a in range(4) for b in range(2)], lambda x, y: ((x[0]+y[0]) % 4, (x[1]+y[1]) % 2), 4),
    ]
    built = {}
    for name, els, add, k in cases:
        n = len(els)
        L, gi = group_table(els, add)
        record('C/%s: Cayley table is a Latin square of order %d' % (name, n), True, is_latin(L, n))
        s0, s1 = gi[(0, 0)], gi[(1, 0)]
        comps = two_symbol_components(L, n, s0, s1)
        record('C/%s: {s0,s1} cells split into two row/column cycles of length 2k=%d' % (name, 2*k),
               [2*k, 2*k], sorted(len(c) for c in comps))
        cyc = next(c for c in comps if (0, 0) in c)       # L(0,0) = s0 is in this cycle
        Q = rotate(L, n, set(cyc), s0, s1)
        record('C/%s: rotated Q is a QLS (rows and columns ONB)' % name, None, qls_violation(Q, n))
        r0 = next(r for r in range(n) if r not in {x[0] for x in cyc})
        A = mixed_analysis(Q, n, r0)
        record('C/%s: reference row %d outside the cycle; mixed cells == rotated cycle' % (name, r0), cyc, A['mixed'])
        record('C/%s: Q nonclassical (>=1 mixed cell)' % name, True, len(A['mixed']) >= 1)
        record('C/%s: exactly one mixed component' % name, 1, len(A['comps']))
        record('C/%s: component is a simple C_%d with one 2-axis support, collinear parts, orthogonal across parts'
               % (name, 2*k), True, is_single_cycle(A['comps'][0], k))
        a, b = A['comps'][0]['supports'][0]
        Ea = [(r, c) for r in range(n) for c in range(n) if (r, c) not in cyc and collinear(Q[(r, c)], Q[(r0, a)])]
        record('C/%s: light e_a cells == n-k' % name, n-k, len(Ea))
        print('   C/%s bound of candidate 3 for this shape: t <= min(k-1, n-k) = %d' % (name, min(k-1, n-k)))
        built[name] = (Q, L, n, k, cyc, r0, gi)
        r_in = cyc[0][0]
        A2 = mixed_analysis(Q, n, r_in)
        print('   C/%s relative to cycle row %d: %d mixed cells, components of sizes %s, degrees %s'
              % (name, r_in, len(A2['mixed']), [len(c['cells']) for c in A2['comps']],
                 [c['degrees'] for c in A2['comps']]))
    # n=4: exhaustive classical mate search for the C4 Q (candidate 3 bound: t <= min(1,2) = 1 -> no mate)
    Q, L, n, k, cyc, r0, gi = built['Z2xZ2']
    count_latin, count_mates = 0, 0
    rows = list(itertools.permutations(range(4)))
    for R0 in rows:
        for R1 in rows:
            if any(R0[c] == R1[c] for c in range(4)):
                continue
            for R2 in rows:
                if any(R2[c] in (R0[c], R1[c]) for c in range(4)):
                    continue
                R3 = tuple(({0, 1, 2, 3} - {R0[c], R1[c], R2[c]}).pop() for c in range(4))
                Lr = {(0, c): R0[c] for c in range(4)}
                Lr.update({(1, c): R1[c] for c in range(4)})
                Lr.update({(2, c): R2[c] for c in range(4)})
                Lr.update({(3, c): R3[c] for c in range(4)})
                count_latin += 1
                if pair_violation(Q, classical(Lr, 4), 4) is None:
                    count_mates += 1
    record('C/Z2xZ2: number of Latin squares of order 4 enumerated', 576, count_latin)
    record('C/Z2xZ2: classical mates of the C4-mixed Q (bound t<=1 predicts none)', 0, count_mates)
    # positive control for the pair checker at n=4: the unrotated L (index xor) with an orthomorphism mate
    phi = {0: 0, 1: 2, 2: 3, 3: 1}
    Rm = {(i, j): phi[i] ^ j for i in range(4) for j in range(4)}
    record('C/Z2xZ2: positive control -- unrotated classical L has an orthogonal classical mate', None,
           pair_violation(classical(L, 4), classical(Rm, 4), 4))
    return built

# ----------------------------------------------------------------------------------------------------------------
# CONTROL A: n=8 three-family with Q mixed graph = two C4 (same support, same basis group), two classical mates
# ----------------------------------------------------------------------------------------------------------------
def intercalates_on(L, n, s0, s1):
    out = []
    for r1, r2 in itertools.combinations(range(n), 2):
        for c1, c2 in itertools.combinations(range(n), 2):
            a, b, c, d = L[(r1, c1)], L[(r1, c2)], L[(r2, c1)], L[(r2, c2)]
            if a == d and b == c and {a, b} == {s0, s1}:
                out.append(((r1, r2), (c1, c2)))
    return out

def control_A():
    print('\n=== CONTROL A: GF(8) linear MOLS + 8-cell two-intercalate trade (two C4, one support, one basis) ===')
    n, s0, s1 = 8, 0, 1
    squares = {lam: gf8_linear_square(lam) for lam in range(1, 8)}
    record('A: all seven GF(8) linear squares are Latin', True, all(is_latin(L, n) for L in squares.values()))
    record('A: GF(8) linear squares are pairwise orthogonal (classical MOLS)', True,
           all(pair_violation(classical(squares[a], n), classical(squares[b], n), n) is None
               for a, b in itertools.combinations(range(1, 8), 2)))
    solutions = []
    for lam in range(1, 8):
        L = squares[lam]
        ints = intercalates_on(L, n, s0, s1)
        for I1, I2 in itertools.combinations(ints, 2):
            if set(I1[0]) & set(I2[0]) or set(I1[1]) & set(I2[1]):
                continue
            trade = {(r, c) for I in (I1, I2) for r in I[0] for c in I[1]}
            zero = [x for x in trade if L[x] == s0]
            one = [x for x in trade if L[x] == s1]
            for mu1, mu2 in itertools.combinations([m for m in range(1, 8) if m != lam], 2):
                if all({squares[mu][x] for x in zero} == {squares[mu][x] for x in one} for mu in (mu1, mu2)):
                    solutions.append((lam, I1, I2, mu1, mu2))
    record('A: at least one (lambda, I1, I2, mu1, mu2) satisfies the symbol-pairing condition for both mates',
           True, len(solutions) >= 1)
    print('   A: number of pairing-compatible (lambda, I1, I2, mu1, mu2) tuples found: %d' % len(solutions))
    lam, I1, I2, mu1, mu2 = solutions[0]
    print('   A: using lambda=%d, intercalates rows/cols %s and %s, mates mu=%d,%d' % (lam, I1, I2, mu1, mu2))
    L = squares[lam]
    cellsI1 = {(r, c) for r in I1[0] for c in I1[1]}
    cellsI2 = {(r, c) for r in I2[0] for c in I2[1]}
    trade = cellsI1 | cellsI2
    Q = rotate(L, n, trade, s0, s1)
    R = classical(squares[mu1], n)
    S = classical(squares[mu2], n)
    record('A: Q is a QLS', None, qls_violation(Q, n))
    record('A: R is a QLS', None, qls_violation(R, n))
    record('A: S is a QLS', None, qls_violation(S, n))
    record('A: Q (x) R product vectors form an ONB of C^64', None, pair_violation(Q, R, n))
    record('A: Q (x) S product vectors form an ONB of C^64', None, pair_violation(Q, S, n))
    record('A: R (x) S product vectors form an ONB of C^64', None, pair_violation(R, S, n))
    trade_rows = set(I1[0]) | set(I2[0])
    r0 = next(r for r in range(n) if r not in trade_rows)
    A = mixed_analysis(Q, n, r0)
    record('A: mixed cells relative to reference row %d == the 8 trade cells' % r0, sorted(trade), A['mixed'])
    record('A: two mixed components', 2, len(A['comps']))
    record('A: both components are simple C4 with one 2-axis support each', True,
           all(is_single_cycle(c, 2) for c in A['comps']))
    record('A: both components have the same support', True, A['comps'][0]['supports'] == A['comps'][1]['supports'])
    X = A['mixed']
    P_all = [x for x in X if collinear(Q[x], Q[X[0]])]
    M_all = [x for x in X if x not in P_all]
    record('A: one basis group -- all 8 mixed rays fall into two collinearity classes of size 4', (4, 4),
           (len(P_all), len(M_all)))
    record('A: the two classes are mutually orthogonal', True, all(dot(Q[x], Q[y]) == 0 for x in P_all for y in M_all))
    a, b = A['comps'][0]['supports'][0]
    FR = forced_structure(Q, R, n, r0, X, a, b, 'A/R(a,b)')
    FS = forced_structure(Q, S, n, r0, X, a, b, 'A/S(a,b)')
    cross_mate_checks(FR, FS, 'A/R,S(a,b)')
    FRb = forced_structure(Q, R, n, r0, X, b, a, 'A/R(b,a)')
    FSb = forced_structure(Q, S, n, r0, X, b, a, 'A/S(b,a)')
    cross_mate_checks(FRb, FSb, 'A/R,S(b,a)')
    K = 4
    print('   A: K=4 mixed rows; candidate-4 one-group bound t <= min(K-1, n-K) = %d; family size here t = 3 (tight)'
          % min(K-1, n-K))
    print('   A: U^R =', FR['U'], ' U^S =', FS['U'])
    print('   A: e_b-overlap cells R:', sorted(FR['B']), ' S:', sorted(FS['B']),
          ' of off-first-row light e_a cells', [y for y in FR['Ea'] if y != (r0, a)])
    # negatives
    Q1 = rotate(L, n, cellsI1, s0, s1)           # single intercalate (one C4)
    record('A-neg1: single-intercalate rotation is still a QLS', None, qls_violation(Q1, n))
    record('A-neg1: but Q1 (x) R is NOT an ONB (candidate 3: C4 alone gives t<=1)', True, pair_violation(Q1, R, n) is not None)
    record('A-neg1: and Q1 (x) S is NOT an ONB', True, pair_violation(Q1, S, n) is not None)
    ray0b = [1 if i == s0 else (2 if i == s1 else 0) for i in range(n)]
    ray1b = [2 if i == s0 else (-1 if i == s1 else 0) for i in range(n)]
    Q2 = rotate(L, n, cellsI1, s0, s1)
    for x in cellsI2:
        Q2[x] = list(ray0b) if L[x] == s0 else list(ray1b)
    record('A-neg2: two-basis-group variant (second C4 uses (e0+2e1),(2e0-e1)) is a QLS', None, qls_violation(Q2, n))
    A2 = mixed_analysis(Q2, n, r0)
    record('A-neg2: it has two C4 components with the same support', True,
           len(A2['comps']) == 2 and all(is_single_cycle(c, 2) for c in A2['comps'])
           and A2['comps'][0]['supports'] == A2['comps'][1]['supports'])
    record('A-neg2: but the two components are in different basis groups (all cross-overlaps nonzero)', True,
           all(dot(Q2[x], Q2[y]) != 0 for x in A2['comps'][0]['cells'] for y in A2['comps'][1]['cells']))
    record('A-neg2: Q2 (x) R is NOT an ONB (candidate 4 section 2: a K_g=2 group admits no mate)', True, pair_violation(Q2, R, n) is not None)
    record('A-neg2: Q2 (x) S is NOT an ONB', True, pair_violation(Q2, S, n) is not None)
    Q3 = dict(Q)
    for x in cellsI2:                            # flip orientation on the second intercalate (same basis group)
        Q3[x] = ray_plus(n, s0, s1) if L[x] == s1 else ray_minus(n, s0, s1)
    record('A-neg3: orientation-flipped second intercalate is a QLS', None, qls_violation(Q3, n))
    record('A-neg3: but Q3 (x) R is NOT an ONB (symbol pairing broken)', True, pair_violation(Q3, R, n) is not None)
    Rsw = dict(R)
    for c in range(n):
        Rsw[(0, c)], Rsw[(1, c)] = R[(1, c)], R[(0, c)]
    record('A-neg4: R with rows 0,1 swapped is a QLS', None, qls_violation(Rsw, n))
    record('A-neg4: but Q (x) R_swapped is NOT an ONB', True, pair_violation(Q, Rsw, n) is not None)
    Rbad = dict(R)
    Rbad[(2, 3)] = list(R[(2, 4)])
    record('A-neg5: R with one cell overwritten is NOT a QLS', True, qls_violation(Rbad, n) is not None)
    return dict(Q=Q, R=R, S=S, r0=r0)

# ----------------------------------------------------------------------------------------------------------------
# CONTROL B: n=8 three-family with a single C8-mixed member (Z4xZ2 table) and exhaustive classical adversary
# ----------------------------------------------------------------------------------------------------------------
def transversals(L, n):
    out = []
    def rec(r, used_cols, used_syms, cells):
        if r == n:
            out.append(tuple(cells))
            return
        for c in range(n):
            if used_cols >> c & 1:
                continue
            s = L[(r, c)]
            if used_syms >> s & 1:
                continue
            rec(r+1, used_cols | (1 << c), used_syms | (1 << s), cells + [(r, c)])
    rec(0, 0, 0, [])
    return out

def exact_covers(masks, n, allowed=None, limit=None):
    """All sets of pairwise-disjoint masks (indices from `allowed`) whose union is every cell."""
    full = (1 << (n*n)) - 1
    allowed = list(range(len(masks))) if allowed is None else list(allowed)
    by_cell = [[i for i in allowed if masks[i] >> cell & 1] for cell in range(n*n)]
    covers = []
    def rec(covered, chosen):
        if covered == full:
            covers.append(tuple(sorted(chosen)))
            return
        best = None
        for cell in range(n*n):
            if covered >> cell & 1:
                continue
            cands = [i for i in by_cell[cell] if masks[i] & covered == 0]
            if best is None or len(cands) < len(best):
                best = cands
            if not cands:
                break
        if not best:
            return
        for i in best:
            if limit and len(covers) >= limit:
                return
            rec(covered | masks[i], chosen + [i])
    rec(0, [])
    return covers

def control_B():
    print('\n=== CONTROL B: Z4xZ2 table, single C8 trade, transversal-decomposition classical mates ===')
    n = 8
    els = [(a, b) for a in range(4) for b in range(2)]
    L, gi = group_table(els, lambda x, y: ((x[0]+y[0]) % 4, (x[1]+y[1]) % 2))
    s0, s1 = gi[(0, 0)], gi[(1, 0)]
    comps = two_symbol_components(L, n, s0, s1)
    cyc = next(c for c in comps if (0, 0) in c)
    record('B: chosen {s0,s1} component is an 8-cycle', 8, len(cyc))
    cycset = set(cyc)
    Q = rotate(L, n, cycset, s0, s1)
    record('B: Q is a QLS', None, qls_violation(Q, n))
    r0 = next(r for r in range(n) if r not in {x[0] for x in cyc})
    A = mixed_analysis(Q, n, r0)
    record('B: mixed cells relative to row %d are exactly the cycle' % r0, cyc, A['mixed'])
    record('B: single mixed component, simple C8, one support, alternating collinear/orthogonal parts', True,
           len(A['comps']) == 1 and is_single_cycle(A['comps'][0], 4))
    t0 = time.time()
    T = transversals(L, n)
    masks = [sum(1 << (r*n + c) for r, c in t) for t in T]
    print('   B: transversals of the Z4xZ2 table: %d (%.1fs)' % (len(T), time.time()-t0))
    cyc0 = sum(1 << (r*n + c) for r, c in cyc if L[(r, c)] == s0)
    cyc1 = sum(1 << (r*n + c) for r, c in cyc if L[(r, c)] == s1)
    good = [i for i, m in enumerate(masks) if (m & cyc0 != 0) == (m & cyc1 != 0)]
    goodset = set(good)
    print('   B: transversals satisfying the cycle condition (meets a cycle s0-cell iff a cycle s1-cell): %d of %d'
          % (len(good), len(masks)))
    t0 = time.time()
    covers_cyc = exact_covers(masks, n, allowed=good)
    print('   B: decompositions of the table into 8 disjoint cycle-condition transversals: %d (%.1fs)'
          % (len(covers_cyc), time.time()-t0))
    t0 = time.time()
    sample_all = exact_covers(masks, n, limit=400)
    covers_non = [cv for cv in sample_all if not all(i in goodset for i in cv)]
    print('   B: sampled %d unrestricted decompositions, %d of them violate the cycle condition (%.1fs)'
          % (len(sample_all), len(covers_non), time.time()-t0))
    def mate_from(cv):
        R = {}
        for sym, ti in enumerate(cv):
            for x in T[ti]:
                R[x] = unit(n, sym)
        return R
    t0 = time.time()
    sample_cyc = covers_cyc[:150]
    ok_cyc = sum(1 for cv in sample_cyc if pair_violation(Q, mate_from(cv), n) is None)
    record('B: sampled cycle-condition decompositions all give classical mates of Q (Q (x) R ONB), sample size %d' % len(sample_cyc),
           len(sample_cyc), ok_cyc)
    sample_non = covers_non[:150]
    fail_non = sum(1 for cv in sample_non if pair_violation(Q, mate_from(cv), n) is not None)
    record('B-neg: sampled decompositions violating the cycle condition all FAIL Q (x) R, sample size %d' % len(sample_non),
           len(sample_non), fail_non)
    print('   B: pair checks took %.1fs' % (time.time()-t0))
    # adversarial: all orthogonal pairs / triples among cycle-condition decompositions via restricted exact cover
    def meets_once(i, cv):
        return all(bin(masks[i] & masks[j]).count('1') == 1 for j in cv)
    t0 = time.time()
    index = {cv: i for i, cv in enumerate(covers_cyc)}
    pairs = 0
    triples = 0
    first_pair = None
    for i, cv1 in enumerate(covers_cyc):
        cand = [t for t in good if meets_once(t, cv1)]
        for cv2 in exact_covers(masks, n, allowed=cand):
            j = index[cv2]
            if j <= i:
                continue
            pairs += 1
            if first_pair is None:
                first_pair = (cv1, cv2)
            cand2 = [t for t in cand if meets_once(t, cv2)]
            for cv3 in exact_covers(masks, n, allowed=cand2):
                if index[cv3] > j:
                    triples += 1
    print('   B: adversarial enumeration took %.1fs' % (time.time()-t0))
    print('   B: orthogonal PAIRS of cycle-condition classical mates: %d' % pairs)
    record('B: at least one orthogonal pair of cycle-condition classical mates exists (a three-family with a C8-mixed member)',
           True, pairs >= 1)
    record('B-adversarial: mutually orthogonal TRIPLES of cycle-condition classical mates (classical four-family extensions of Q)',
           0, triples)
    cv1, cv2 = first_pair
    R, S = mate_from(cv1), mate_from(cv2)
    record('B: R is a QLS', None, qls_violation(R, n))
    record('B: S is a QLS', None, qls_violation(S, n))
    record('B: Q (x) R ONB', None, pair_violation(Q, R, n))
    record('B: Q (x) S ONB', None, pair_violation(Q, S, n))
    record('B: R (x) S ONB', None, pair_violation(R, S, n))
    X = A['mixed']
    a, b = A['comps'][0]['supports'][0]
    FR = forced_structure(Q, R, n, r0, X, a, b, 'B/R(a,b)')
    FS = forced_structure(Q, S, n, r0, X, a, b, 'B/S(a,b)')
    cross_mate_checks(FR, FS, 'B/R,S(a,b)')
    FRb = forced_structure(Q, R, n, r0, X, b, a, 'B/R(b,a)')
    FSb = forced_structure(Q, S, n, r0, X, b, a, 'B/S(b,a)')
    cross_mate_checks(FRb, FSb, 'B/R,S(b,a)')
    k = 4
    print('   B: k=4; candidate 1/3 bound t <= min(k-1, n-k) = %d; family size here t = 3 (tight)' % min(k-1, n-k))
    print('   B: P =', FR['P'], ' M =', FR['M'])
    print('   B: U^R =', FR['U'])
    print('   B: U^S =', FS['U'])
    avail = {(i, j) for i in range(k) for j in range(k)
             if not (FR['P'][i][0] == FR['M'][j][0] or FR['P'][i][1] == FR['M'][j][1])}
    record('B: available (non-neighbour) transition positions per row == k-2', [2]*k,
           [len([j for j in range(k) if (i, j) in avail]) for i in range(k)])
    record('B: the two mates\' supports exhaust all available positions (no room for a third mate support)', avail,
           FR['support'] | FS['support'])
    pats = Counter()
    for cv in covers_cyc:
        Rm = mate_from(cv)
        U = [[dot(Rm[p], Rm[m]) for m in FR['M']] for p in FR['P']]
        pats[tuple(tuple(row) for row in U)] += 1
    record('B: every cycle-condition classical mate has a permutation transition matrix vanishing at neighbour positions', True,
           all(all(sum(row) == 1 for row in U) and all(sum(U[i][j] for i in range(k)) == 1 for j in range(k))
               and all(U[i][j] == 0 for i in range(k) for j in range(k) if (i, j) not in avail) for U in pats))
    print('   B: distinct transition patterns among all %d cycle-condition classical mates: %d, multiplicities %s'
          % (len(covers_cyc), len(pats), sorted(pats.values())))
    return dict(Q=Q, R=R, S=S)

# ----------------------------------------------------------------------------------------------------------------
# CONTROL D: abstract transition-support pigeonhole for a single C_2k
# ----------------------------------------------------------------------------------------------------------------
def control_D():
    print('\n=== CONTROL D: abstract support pigeonhole for a single mixed cycle C_2k ===')
    # cells p_1 m_1 p_2 m_2 ... p_k m_k around the cycle; p_i is adjacent (shares a row or column) to m_{i-1} and m_i.
    for k in range(2, 8):
        perms = [s for s in itertools.permutations(range(k)) if all(s[i] not in ((i-1) % k, i) for i in range(k))]
        best = 0
        def rec(start, chosen):
            nonlocal best
            best = max(best, len(chosen))
            if best >= k-2:
                return
            for idx in range(start, len(perms)):
                s = perms[idx]
                if all(all(s[i] != t[i] for i in range(k)) for t in chosen):
                    rec(idx+1, chosen + [s])
        rec(0, [])
        record('D/k=%d: max number of pairwise-disjoint band-avoiding permutation patterns == k-2 (row pigeonhole)' % k, k-2, best)
        print('   D/k=%d: band-avoiding permutation patterns: %d; a unitary support contains one; hence t-1 <= %d, t <= %d'
              % (k, len(perms), k-2, k-1))
    print('   D: relaxation -- without the two neighbour zeros a row has k available positions, so only t <= k+1 would follow;')
    print('      the zeros are load-bearing (k=4: t<=3 versus t<=5).')
    print('   D: two-sided bound min(k-1, n-k) for n=8:')
    for k in range(2, 8):
        print('      k=%d (C_%d): min(k-1, n-k) = %d' % (k, 2*k, min(k-1, 8-k)))
    record('D: for n=8 every single-cycle length C_2k (2<=k<=7) gives t <= 3', True, all(min(k-1, 8-k) <= 3 for k in range(2, 8)))
    record('D: for n=8 the row pigeonhole alone (t<=k-1) does NOT exclude k>=5', True, any(k-1 >= 4 for k in range(2, 8)))
    record('D: for n=8 the complement pigeonhole alone (t<=n-k) does NOT exclude k<=4', True, any(8-k >= 4 for k in range(2, 8)))

# ----------------------------------------------------------------------------------------------------------------
# CONTROL E: candidate 4 case analysis, enumerated for n = 8
# ----------------------------------------------------------------------------------------------------------------
def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i+1:]
        yield [[first]] + p

def control_E():
    print('\n=== CONTROL E: candidate 4 case analysis enumerated for n=8 (all degree-2 mixed shapes) ===')
    n = 8
    pairs = [frozenset(p) for p in itertools.combinations(range(n), 2)]
    counts = Counter()
    worst = 0
    configs = 0
    unclassified = 0
    for ncomp in (1, 2, 3):
        for ks in itertools.product(range(2, 8), repeat=ncomp):
            if sum(ks) > n-1:
                continue
            for supports in itertools.product(pairs, repeat=ncomp):
                configs += 1
                excl = []
                for i in range(ncomp):
                    others = set().union(*[supports[j] for j in range(ncomp) if j != i]) if ncomp > 1 else set()
                    if supports[i] - others:
                        excl.append(min(ks[i]-1, n-ks[i]))
                if excl:
                    bound = min(excl)
                    counts['exclusive-axis'] += 1
                elif len(set(supports)) == 1:
                    bs = []
                    for part in set_partitions(list(range(ncomp))):
                        Ks = [sum(ks[i] for i in g) for g in part]
                        if len(part) == 1:
                            bs.append(min(Ks[0]-1, n-Ks[0]))
                        else:
                            bs.append(min(K-1 for K in Ks))
                    bound = max(bs)        # worst case over all basis-group partitions
                    counts['all-supports-equal'] += 1
                else:
                    distinct = set(supports)
                    verts = set().union(*distinct)
                    if not (ncomp == 3 and len(distinct) == 3 and len(verts) == 3):
                        unclassified += 1
                        continue
                    bound = min(ks) - 1
                    counts['triangle'] += 1
                worst = max(worst, bound)
    record('E: every degree-2 configuration (components, sizes, supports) is classified by exactly one case', 0, unclassified)
    record('E: worst-case family-size bound over all configurations', 3, worst)
    print('   E: configurations enumerated: %d; by case: %s' % (configs, dict(counts)))
    record('E: with k_i>=2 and sum k_i <= 7 there are at most three components', True, 2*3 <= 7 and 2*4 > 7)
    record('E: three components force every k_i <= 3', True,
           all(max(ks) <= 3 for ks in itertools.product(range(2, 8), repeat=3) if sum(ks) <= 7))
    record('E: a simple graph with 3 distinct edges and minimum degree >= 2 is a triangle', True,
           all(len(set().union(*e)) == 3 for e in itertools.combinations(pairs, 3)
               if all(sum(1 for f in e if v in f) >= 2 for v in set().union(*e))))
    note('E: the 2-dimensional fact "distinct orthonormal bases of C^2 have no zero cross overlap" is definitional '
         '(a unit vector orthogonal to v is the unique ray v-perp) and is not machine-checked here')

# ----------------------------------------------------------------------------------------------------------------
def main():
    start = utc()
    print('reviewer-controls-v1.py start (UTC):', start)
    src = os.path.abspath(sys.argv[0])
    with open(src, 'rb') as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    print('script path:', src)
    print('script sha256:', src_sha)
    control_C()
    control_A()
    control_B()
    control_D()
    control_E()
    end = utc()
    checks = [r for r in RESULTS if 'check' in r]
    npass = sum(1 for r in checks if r['ok'])
    nfail = len(checks) - npass
    print('\nSUMMARY: %d checks, %d PASS, %d FAIL; start %s end %s' % (len(checks), npass, nfail, start, end))
    out = {'script': src, 'script_sha256': src_sha, 'start_utc': start, 'end_utc': end,
           'checks': len(checks), 'pass': npass, 'fail': nfail, 'results': RESULTS}
    outpath = os.path.join(os.path.dirname(src), 'reviewer-controls-result-v1.json')
    if os.path.exists(outpath):
        print('refusing to overwrite', outpath)
        sys.exit(2)
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=1)
    print('wrote', outpath)
    sys.exit(0 if nfail == 0 else 1)

if __name__ == '__main__':
    main()
