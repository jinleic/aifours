#!/usr/bin/env python3
"""Reviewer-owned exact controls; no author code or external inputs."""
from fractions import Fraction as F
from itertools import product, combinations
from math import isqrt

N = 16
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))

def z(a=0, b=0):
    return (F(a), F(b))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def conj(a):
    return (a[0], -a[1])

def scale(a, q):
    return (a[0]*q, a[1]*q)

def matzero():
    return [[ZERO for _ in range(N)] for _ in range(N)]

def pure(entries):
    v = [ZERO for _ in range(N)]
    for j, a in entries.items():
        v[j] = a
    norm = sum(a[0]*a[0] + a[1]*a[1] for a in v)
    assert norm > 0
    return [[scale(mul(v[i], conj(v[j])), F(1, 1)/norm) for j in range(N)] for i in range(N)]

def mix(items):
    m = matzero()
    assert sum(w for w, _ in items) == 1
    assert all(w >= 0 for w, _ in items)
    for w, a in items:
        for i in range(N):
            for j in range(N):
                m[i][j] = add(m[i][j], scale(a[i][j], w))
    return m

def addmat(mats):
    out = matzero()
    for a in mats:
        for i in range(N):
            for j in range(N):
                out[i][j] = add(out[i][j], a[i][j])
    return out

def matmul(a, b):
    out = matzero()
    for i in range(N):
        for j in range(N):
            x = ZERO
            for k in range(N):
                x = add(x, mul(a[i][k], b[k][j]))
            out[i][j] = x
    return out

def trace_product(a, b):
    out = ZERO
    for i in range(N):
        for j in range(N):
            out = add(out, mul(a[i][j], b[j][i]))
    assert out[1] == 0
    return out[0]

def projector(vectors):
    q = addmat([pure(v) for v in vectors])
    assert matmul(q, q) == q
    assert sum(q[i][i][0] for i in range(N)) == 3
    return q

def pauli_expect(a, pauli):
    # P maps |column> to phase*|row>, with Y|0>=i|1>, Y|1>=-i|0>.
    result = ZERO
    for column in range(N):
        row = column
        phase = ONE
        for site, symbol in enumerate(pauli):
            bit = (column >> (3-site)) & 1
            mask = 1 << (3-site)
            if symbol == 1:
                row ^= mask
            elif symbol == 2:
                row ^= mask
                phase = mul(phase, z(0, 1 if bit == 0 else -1))
            elif symbol == 3 and bit:
                phase = scale(phase, -1)
        result = add(result, mul(a[column][row], phase))
    assert result[1] == 0, (pauli, result)
    return result[0]

def pauli_data(a):
    vals = {}
    sums = [F(0) for _ in range(5)]
    for pauli in product(range(4), repeat=4):
        w = sum(symbol != 0 for symbol in pauli)
        value = pauli_expect(a, pauli)
        vals[pauli] = value
        sums[w] += value*value
    return vals, sums

def local_radii(vals):
    radii = []
    for site in range(4):
        v = []
        for symbol in (1, 2, 3):
            p = [0, 0, 0, 0]
            p[site] = symbol
            v.append(vals[tuple(p)])
        # All independently chosen densities have diagonal single-site marginals.
        assert v[0] == v[1] == 0
        radii.append(abs(v[2]))
    return radii

def apply_channel(a, p):
    # Direct tensor action on matrix units, independent of the Pauli expansion.
    s = 1-p
    out = a
    for site in range(4):
        mask = 1 << (3-site)
        nxt = matzero()
        for row in range(N):
            for col in range(N):
                value = scale(out[row][col], s)
                if bool(row & mask) == bool(col & mask):
                    r0, c0 = row & ~mask, col & ~mask
                    partial = add(out[r0][c0], out[r0 | mask][c0 | mask])
                    value = add(value, scale(partial, p/2))
                nxt[row][col] = value
        out = nxt
    return out

def reflect_q(q):
    # Y^tensor4 Q^T Y^tensor4 in the computational basis.
    out = matzero()
    for row in range(N):
        for col in range(N):
            sign = (-1)**(row.bit_count() + col.bit_count())
            out[row][col] = scale(q[15-col][15-row], sign)
    return out

def sqrt_bounds(q):
    assert q >= 0
    k = 10**24
    n, d = q.numerator, q.denominator
    lower = F(isqrt(n*d*k*k), d*k)
    upper = lower if lower*lower == q else lower + F(1, d*k)
    assert lower*lower <= q <= upper*upper
    return lower, upper

def f_bounds(S, L, H, t, x):
    l1, u1 = sqrt_bounds(S*x)
    l2, u2 = sqrt_bounds(H*(39-x))
    return min(L, l1) + t*l2, min(L, u1) + t*u2

def budget(S, L, H, t):
    if S == 0:
        return F(0), f_bounds(S, L, H, t, F(0))
    u = L*L/S
    x0 = 39*S/(S+t*t*H)
    xstar = min(u, x0)
    assert 0 <= xstar <= u <= 20
    return xstar, f_bounds(S, L, H, t, xstar)

def r3(t):
    a, b = (1+t)/2, (1-t)/2
    r = a**4 + 2*a**3*b
    assert 16*r == 3+8*t+6*t*t-t**4
    return r

example = pure({0:z(3), 3:z(1), 5:z(1), 14:z(1)})
complex_rho = pure({0:z(1), 7:I, 9:z(2)})
ghz = pure({0:ONE, 15:ONE})
prod = pure({0:ONE})
id16 = [[z(F(1,16)) if i == j else ZERO for j in range(N)] for i in range(N)]
mixed = mix([(F(1,3), example), (F(1,3), complex_rho), (F(1,3), id16)])
q_example = projector([{0:ONE}, {3:ONE}, {5:ONE}])
q_top = projector([{0:ONE}, {1:ONE}, {2:ONE}])
q_ghz = projector([{0:ONE,15:ONE}, {1:ONE,14:ONE}, {2:ONE,13:ONE}])
q_complex = projector([{0:ONE,15:I}, {3:ONE,5:ONE}, {1:ONE,6:I}])
states = {'example':example, 'complex':complex_rho, 'mixed':mixed, 'GHZ':ghz, 'product':prod}
projectors = {'example_Q':q_example, 'top_Q':q_top, 'GHZ_Q':q_ghz, 'complex_Q':q_complex}
sd = {name:pauli_data(a) for name,a in states.items()}
qd = {name:pauli_data(a) for name,a in projectors.items()}
for name,(v,w) in sd.items():
    assert w[0] == 1 and sum(w) <= 15+1
for name,(v,w) in qd.items():
    assert w[0] == 9 and sum(w) == 48 and w[1] <= 20
assert qd['example_Q'][1] == [9,12,6,12,9]
assert qd['top_Q'][1][1] == 20
assert qd['GHZ_Q'][1][1] == 0

# Independent matrix-unit channel, signed Pauli expansion and actual-Q bounds.
count = 0
for sn, rho in states.items():
    av, A = sd[sn]
    rr = sorted(local_radii(av))
    S = sum(r*r for r in rr)
    L = rr[0]+rr[1]+3*rr[2]+3*rr[3]
    assert S == A[1]
    for p in (F(0), F(1,3), F(2,3), F(1), F(4,3)):
        s, t = 1-p, abs(1-p)
        H = A[2] + t*t*A[3] + t**4*A[4]
        assert H <= 15-S
        out = apply_channel(rho, p)
        xstar, (B_lo, B_hi) = budget(S,L,H,t)
        for qn, q in projectors.items():
            bv, bweights = qd[qn]
            x = bweights[1]
            observed = trace_product(q,out)
            expansion = F(3)
            for pauli, a in av.items():
                w = sum(symbol != 0 for symbol in pauli)
                if w:
                    expansion += s**w*a*bv[pauli]
            assert expansion == 16*observed, (sn, qn, p)
            assert sum(bweights[2:]) == 39-x
            actual_gap = 16*(r3(t)-observed)
            f_lo, f_hi = f_bounds(S,L,H,t,x)
            assert actual_gap >= t*(8+6*t-t**3-f_lo), (sn, qn, p)
            assert 16*observed <= 3+t*B_lo, (sn, qn, p)
            count += 1
print('PHYSICAL_EXACT_CASES:', count, '5 densities (including mixed/complex) x 4 actual projectors x 5 physical p')
print('Q_WEIGHT_BUDGETS:', 'example', qd['example_Q'][1], 'top x=20, GHZ x=0')

# Optimizer branch, transition and degeneracy controls; scalar points are relaxation controls.
cases = [
    ('INTERIOR', F(1),F(3),F(10),F(1), F(39,11), [F(0),F(1),F(39,11)-F(1,2),F(39,11)+F(1,2),F(9),F(20),F(39)]),
    ('CAP', F(1),F(2),F(4),F(1,2), F(4), [F(0),F(3),F(5),F(20),F(39)]),
    ('TRANSITION', F(1),F(3),F(10,3),F(1), F(9), [F(0),F(8),F(10),F(20),F(39)])]
for label,S,L,H,t,want,others in cases:
    xs,(lo,hi) = budget(S,L,H,t)
    assert xs == want
    for x in others:
        assert lo > f_bounds(S,L,H,t,x)[1], (label,x)
    print('OPTIMIZER_'+label+': x*=', xs)
for H,t in ((F(0),F(1,3)), (F(7),F(0))):
    xs, b = budget(F(1),F(2),H,t)
    assert xs == 4
    for x in (F(4),F(5),F(20),F(39)):
        assert f_bounds(F(1),F(2),H,t,x) == (F(2),F(2))
    print('OPTIMIZER_PLATEAU:', 'H=',H,'t=',t,'x in [4,39]')
xs,b = budget(F(0),F(0),F(2),F(1,3))
assert xs == 0 and b[0] > f_bounds(F(0),F(0),F(2),F(1,3),F(1))[1]
for H,t in ((F(0),F(1,3)),(F(2),F(0))):
    for x in (F(0),F(20),F(39)):
        assert f_bounds(F(0),F(0),H,t,x) == (F(0),F(0))
print('OPTIMIZER_ZERO_S: x=0 unique when tH>0; all x when tH=0')

# Exact example and all-Q strict certificate.
av,A = sd['example']
r = local_radii(av)
assert r == [F(5,6),F(2,3),F(2,3),F(2,3)]
assert A == [F(1),F(73,36),F(145,36),F(215,36),F(107,36)]
r_sorted = sorted(r)
S, L, t = A[1], r_sorted[0]+r_sorted[1]+3*r_sorted[2]+3*r_sorted[3], F(1,3)
H = A[2]+t*t*A[3]+t**4*A[4]
u, x0 = L*L/S, 39*S/(S+t*t*H)
assert (S,L,H,u,x0) == (F(73,36),F(35,6),F(13787,2916),F(1225,73),F(2075463,67004))
assert x0 > u and H*(39-u) == F(11181257,106434) < 121
assert L+t*11 == F(19,2) < F(269,27)
assert F(3,16)+t*F(19,2)/16 == F(37,96)
assert r3(t) == F(32,81) and F(32,81)-F(37,96) == F(25,2592)
print('EXAMPLE_MOMENTS:', 'r=',r,'A=',A,'H=',H,'u=',u,'x0=',x0)
print('ALL_Q:', 'B<19/2, K3<37/96, reference=32/81, gap>25/2592')
for p, expected, gap in ((F(2,3),F(5,18),F(19,162)), (F(4,3),F(41,324),F(29,108))):
    observed = trace_product(q_example, apply_channel(example,p))
    assert observed == expected and r3(t)-observed == gap
    f_lo,f_hi = f_bounds(S,L,H,t,F(12))
    assert S*12 == F(73,3) < 25 and H*27 == F(13787,108) < 144
    assert 8+6*t-t**3-f_hi > F(26,27)
    assert r3(t)-observed > F(13,648)
    print('SAME_ACTUAL_Q:', 'p=',p,'trace=',observed,'gap=',gap)
assert trace_product(q_example,apply_channel(example,F(4,3))) == trace_product(reflect_q(q_example),apply_channel(example,F(2,3)))
assert reflect_q(q_example) != q_example
assert trace_product(q_complex,apply_channel(complex_rho,F(4,3))) == trace_product(reflect_q(q_complex),apply_channel(complex_rho,F(2,3)))
print('REFLECTION: same rho, transformed actual Q; checked diagonal and complex cases')

# Spin flip, all seven cut minors, named comparisons and near-product bound.
v = [0]*16
for j,a in ((0,3),(3,1),(5,1),(14,1)):
    v[j] = a
spin = sum(((-1)**j.bit_count())*v[j]*v[15-j] for j in range(16))
assert spin == 0
cuts = [(0,),(1,),(2,),(3,),(0,1),(0,2),(0,3)]
for cut in cuts:
    other = [j for j in range(4) if j not in cut]
    m = [[0 for _ in range(1<<len(other))] for _ in range(1<<len(cut))]
    for basis,a in enumerate(v):
        row = sum(((basis>>(3-site))&1) << (len(cut)-1-k) for k,site in enumerate(cut))
        col = sum(((basis>>(3-site))&1) << (len(other)-1-k) for k,site in enumerate(other))
        m[row][col] = a
    found = None
    for rows in combinations(range(len(m)),2):
        for cols in combinations(range(len(m[0])),2):
            det = m[rows[0]][cols[0]]*m[rows[1]][cols[1]] - m[rows[0]][cols[1]]*m[rows[1]][cols[0]]
            if abs(det) == 3:
                found = (rows,cols,det)
                break
        if found is not None:
            break
    assert found is not None
    print('CUT_MINOR:', cut, found, 'normalized det=',F(found[2],12))
delta = 8-L
assert 4*S == F(73,9) > F(64,9)
assert delta == F(13,6)
assert 39*(15-S)-(5+delta/t)**2 == F(1121,3) > 0
assert 39*(S+t*t*H)-(8+6*t-t**3)**2 == F(680,2187) > 0
assert (1+r[1])/2 == F(5,6) < F(124,125)
assert F(3,4) > F(25,36)  # |<0000|psi>| = sqrt(3)/2 > 5/6.
print('NAMED_EXCLUSIONS: C=0, 4S+8C=73/9>64/9, D difference=1121/3, purity-test difference=680/2187')
print('OVERLAP_WORDING_NEGATIVE: amplitude |<0000|psi>|=sqrt(3)/2 > 5/6; squared product fidelity <=5/6')

# Physical-interval and same-actual-object intended-reason negative controls.
for p in (F(-1,3), F(0), F(1), F(4,3), F(3,2)):
    choi = [1-3*p/4, p/4, p/4, p/4]
    assert sum(choi) == 1
    if p in (F(-1,3),F(3,2)):
        assert min(choi) < 0
    else:
        assert min(choi) >= 0
    print('PHYSICAL_CHOI:', 'p=',p,'eigenvalues=',choi)
# Real top-Q is tight for the product reference at p=2/3; substituting x of
# a different, physical rank-three projector produces a false positive gap.
p = F(2,3); t = abs(1-p)
prodA = sd['product'][1]
Hprod = prodA[2]+t*t*prodA[3]+t**4*prodA[4]
actual = trace_product(q_top,apply_channel(prod,p))
assert actual == r3(t)
assert qd['top_Q'][1][1] == 20 and qd['GHZ_Q'][1][1] == 0
bad_upper = f_bounds(F(4),F(8),Hprod,t,F(0))[1]
assert 8+6*t-t**3-bad_upper > 0
print('NEGATIVE_WRONG_Q:', 'rho=|0000>, p=2/3, actual Q x=20 gives gap 0; replacing x by physical other Q x=0 falsely predicts positive gap')
assert actual > F(3,16)
print('NEGATIVE_WRONG_RHO: replacing product rho budgets by maximally mixed S=H=0 falsely bounds same actual trace by 3/16')
actual_neg = trace_product(q_example,apply_channel(example,F(4,3)))
incorrect_abs = trace_product(q_example,apply_channel(example,F(2,3)))
assert actual_neg != incorrect_abs
print('NEGATIVE_ABS_SIGN: same Q p=4/3 gives',actual_neg,'not p=2/3 value',incorrect_abs)
GHZA = sd['GHZ'][1]
assert GHZA == [1,0,6,0,9] and trace_product(q_ghz,apply_channel(ghz,F(0))) == 1
assert sqrt_bounds(F(585))[0] > 13
print('NEGATIVE_RHS: physical GHZ, same Q, p=0 has actual gap 0 while RHS=13-sqrt(585)<0')
print('ALL_REVIEWER_CONTROLS_PASS')
