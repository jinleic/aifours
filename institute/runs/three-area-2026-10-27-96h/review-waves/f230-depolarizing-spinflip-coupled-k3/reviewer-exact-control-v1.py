#!/usr/bin/env python3
"""Reviewer-owned exact controls; no author modules or generated files."""
from fractions import Fraction as F
from itertools import combinations, product

Z = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))

def g(re=0, im=0):
    return (F(re), F(im))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def scale(a, c):
    return (a[0]*c, a[1]*c)

def conj(a):
    return (a[0], -a[1])

def real(a):
    assert a[1] == 0, a
    return a[0]

def matrix():
    return [[Z for _ in range(16)] for _ in range(16)]

def matrix_add(A, B, a=F(1), b=F(1)):
    return [[add(scale(A[i][j], a), scale(B[i][j], b))
             for j in range(16)] for i in range(16)]

def trace_product(A, B):
    out = Z
    for i in range(16):
        for j in range(16):
            out = add(out, mul(A[i][j], B[j][i]))
    return real(out)

def spin(A, conjugate=True):
    out = matrix()
    for i in range(16):
        for j in range(16):
            v = A[15-i][15-j]
            out[i][j] = scale(conj(v) if conjugate else v,
                              (-1)**((i.bit_count()+j.bit_count()) % 2))
    return out

def pauli_coeff(A, op):
    # op 0,1,2,3 denotes I,X,Y,Z; site 0 is the most-significant bit.
    mask = sum((1 << (3-i)) for i, p in enumerate(op) if p in (1, 2))
    nY = sum(p == 2 for p in op)
    phase = (ONE, I, g(-1), g(0, -1))[nY % 4]
    out = Z
    for j in range(16):
        parity = sum(((j >> (3-i)) & 1) for i, p in enumerate(op) if p in (2, 3))
        out = add(out, scale(mul(A[j][j ^ mask], phase), (-1)**parity))
    return real(out)

def sectors(A, B):
    aa = [F(0)]*5
    bb = [F(0)]*5
    cc = [F(0)]*5
    coeffsA = {}
    coeffsB = {}
    for op in product(range(4), repeat=4):
        w = sum(p != 0 for p in op)
        a, b = pauli_coeff(A, op), pauli_coeff(B, op)
        aa[w] += a*a
        bb[w] += b*b
        cc[w] += a*b
        coeffsA[op], coeffsB[op] = a, b
    return aa, bb, cc, coeffsA, coeffsB

def direct_trace(A, Q, p):
    # Apply Phi to each matrix unit via s|a><b|+(p/2)delta_ab I.
    s = 1-p
    ans = Z
    for a in range(16):
        for b in range(16):
            v = A[a][b]
            if v == Z:
                continue
            equal_bits = [j for j in range(4) if ((a >> j) & 1) == ((b >> j) & 1)]
            for r in range(len(equal_bits)+1):
                for replacement in combinations(equal_bits, r):
                    for bits in product((0, 1), repeat=r):
                        x, y = a, b
                        for j, bit in zip(replacement, bits):
                            x = (x & ~(1 << j)) | (bit << j)
                            y = (y & ~(1 << j)) | (bit << j)
                        ans = add(ans, scale(mul(v, Q[y][x]), s**(4-r)*(p/2)**r))
    return real(ans)

def report_pair(name, A, Q, parameters):
    aa, bb, cc, ca, cb = sectors(A, Q)
    G_A, G_Q = spin(A), spin(Q)
    kappa = trace_product(Q, G_Q)
    delta = trace_product(Q, A) - trace_product(Q, G_A)
    assert trace_product(Q, Q) == 3
    assert bb[0] == 9 and sum(bb) == 48
    assert bb[1]+bb[3] == 24-8*kappa
    assert bb[2]+bb[4] == 15+8*kappa
    assert 0 <= kappa <= 3 and bb[1] <= min(20, 24-8*kappa)
    assert delta == trace_product(G_Q, A) * (-1) + trace_product(Q, A)
    assert cc[1]+cc[3] == 8*delta
    for p in parameters:
        s, t = 1-p, abs(1-p)
        direct = direct_trace(A, Q, p)
        pauli = (F(3) + sum(s**j*cc[j] for j in range(1, 5)))/16
        assert direct == pauli, (name, p, direct, pauli)
        assert s*cc[1]+s**3*cc[3] == s*(1-t*t)*cc[1]+8*s**3*delta
        E = aa[2]+t**4*aa[4]
        assert (cc[2]+t*t*cc[4])**2 <= E*(15+8*kappa)
        assert cc[1]**2 <= aa[1]*bb[1]
        R = (3+8*t+6*t*t-t**4)/16
        print('PAIR', name, 'p=', p, 'trace=', direct, 'R=', R, 'gap=', R-direct)
    print('SECTORS', name, 'A=', aa, 'B=', bb, 'c=', cc, 'k=', kappa, 'delta=', delta)
    return aa, bb, cc, ca, cb, kappa, delta

rho = matrix()
weights = {0: 3, 3: 1, 5: 1, 14: 1}
for a, va in weights.items():
    for b, vb in weights.items():
        rho[a][b] = g(F(va*vb, 12))
assert trace_product(rho, rho) == 1 and trace_product(rho, spin(rho)) == 0
Q = matrix()
Q[0][0] = Q[5][5] = ONE
Q[3][3] = Q[15][15] = g(F(1, 2))
Q[3][15], Q[15][3] = g(0, F(-1, 2)), g(0, F(1, 2))
oldQ = matrix()
for a in (0, 3, 5):
    oldQ[a][a] = ONE
pvals = (F(0), F(9,16), F(2,3), F(1), F(4,3))
aa, bb, cc, ca, cb, k, delta = report_pair('complex-Q-pure', rho, Q, pvals)
assert aa == [1, F(73,36), F(145,36), F(215,36), F(107,36)]
assert bb == [9, 6, 12, 10, 11] and k == 1 and delta == F(1,2)
assert direct_trace(rho, Q, F(9,16)) == F(639301,2097152)
assert (3+8*F(7,16)+6*F(7,16)**2-F(7,16)**4)/16 == F(498847,1048576)
assert F(498847,1048576)-F(639301,2097152) == F(358393,2097152)
old_aa, old_bb, old_cc, _, _, old_k, old_delta = report_pair('186-diagonal-Q-pure', rho, oldQ, (F(2,3), F(4,3)))
assert old_bb == [9, 12, 6, 12, 9]
assert direct_trace(rho, oldQ, F(2,3)) == F(5,18)
assert direct_trace(rho, oldQ, F(4,3)) == F(41,324)

zero = matrix()
zero[0][0] = ONE
mixed = matrix_add(rho, zero, F(1,2), F(1,2))
evenmixed = matrix_add(rho, spin(rho), F(1,2), F(1,2))
assert trace_product(mixed, mixed) < 1 and trace_product(evenmixed, evenmixed) == F(1,2)
report_pair('complex-Q-mixed', mixed, Q, pvals)
_, _, _, _, _, _, even_delta = report_pair('complex-Q-spin-invariant-mixed', evenmixed, Q, pvals)
assert spin(evenmixed) == evenmixed and even_delta == 0

r = []
for site in range(4):
    values = []
    for p in (1, 2, 3):
        op = [0]*4
        op[site] = p
        values.append(ca[tuple(op)])
    assert values[0] == values[1] == 0
    r.append(abs(values[2]))
assert r == [F(5,6), F(2,3), F(2,3), F(2,3)]
print('MARGINAL_RADII', r)
for cut in ((0,), (1,), (2,), (3,), (0,1), (0,2), (0,3)):
    other = tuple(i for i in range(4) if i not in cut)
    def project(index, sites):
        return tuple((index >> (3-j)) & 1 for j in sites)
    rows = sorted(set(project(z, cut) for z in weights))
    cols = sorted(set(project(z, other) for z in weights))
    entries = {(project(z, cut), project(z, other)): value for z, value in weights.items()}
    found = None
    for a, b in combinations(rows, 2):
        for c, d in combinations(cols, 2):
            det = entries.get((a,c), 0)*entries.get((b,d), 0)-entries.get((a,d), 0)*entries.get((b,c), 0)
            if det:
                found = (a, b, c, d, det)
                break
        if found:
            break
    assert found and abs(found[-1]) == 3
    print('CUT_MINOR', cut, found, 'normalized=', F(found[-1],12))

S, L, t = F(73,36), F(35,6), F(7,16)
T = 8+6*t-t**3
E = aa[2]+t**4*aa[4]
H = aa[2]+t*t*aa[3]+t**4*aa[4]
u = L*L/S
k0 = (24-u)/8
y0 = 39*(1-t*t)**2*S/((1-t*t)**2*S+t*t*E)
x0 = 39*S/(S+t*t*H)
U0 = (1-t*t)*L+8*t*t+t*F(48,5)
U2 = (1-t*t)*F(81,20)+8*t*t+t*F(51,4)
assert T == F(43177,4096) and E == F(1084403,262144)
assert H == F(12456587,2359296) and u == F(1225,73) and k0 == F(527,584)
assert 0 < k0 < 2 and u < 20
assert F(48,5)**2-E*(39-u) == F(58990999,239206400) > 0
assert y0-u == F(79223837221,10373979995) > 0
assert F(81,20)**2-8*S == F(649,3600) > 0
assert F(51,4)**2-39*E == F(323067,262144) > 0
assert U0 == F(26747,2560) and U2 == F(53167,5120) and U2 < U0
assert T-U0 == F(1909,20480) > 0
assert t*(T-U0)/16 == F(13363,5242880)
assert 6*S < F(7,2)**2 and 23*E < F(49,5)**2
fixed_bracket = T-(1-t*t)*F(7,2)-4*t*t-t*F(49,5)
assert fixed_bracket == F(54437,20480)
assert t*fixed_bracket/16 == F(381059,5242880)
assert x0-u == F(412938801007,44654331921) > 0
comparator_excess = H*(39-u)-((T-L)/t)**2
assert T > L and comparator_excess == F(2129511149,1406533632) > 0
Dfail = 39*(15-S)-(5+(8-L)/t)**2
assert Dfail == F(717713,1764) > 0
assert 4*S == F(73,9) > F(64,9)
print('CERTIFICATE', 'T=', T, 'E=', E, 'H=', H, 'u=', u, 'k0=', k0,
      'y0-u=', y0-u, 'x0-u=', x0-u, 'U0=', U0, 'U2=', U2,
      'T-U0=', T-U0, 'strict_gap=', t*(T-U0)/16,
      '186_failure_square=', comparator_excess, 'D_failure_square=', Dfail)

third = F(1,3)
H3 = aa[2]+third**2*aa[3]+third**4*aa[4]
x03 = 39*S/(S+third**2*H3)
assert H3 == F(13787,2916) and x03 == F(2075463,67004) and x03 > u
assert H3*(39-u) == F(11181257,106434) < 121
assert 39*(15-S)-(5+(8-L)/third)**2 == F(1121,3)
assert 39*(S+third**2*H3)-(8+6*third-third**3)**2 == F(680,2187)
print('186_ONE_THIRD', 'H=', H3, 'x0=', x03, 'radicand=', H3*(39-u))

# Physical CP boundaries: I,X,Y,Z Pauli-channel weights.
for p in (F(0), F(1), F(4,3)):
    coeffs = (1-3*p/4, p/4, p/4, p/4)
    assert sum(coeffs) == 1 and min(coeffs) >= 0
    print('CP_BOUNDARY', 'p=', p, 'weights=', coeffs)
for p in (F(-1,100), F(4,3)+F(1,100)):
    coeffs = (1-3*p/4, p/4, p/4, p/4)
    assert min(coeffs) < 0
    print('INTENDED_NEGATIVE', 'outside_CP_interval', 'p=', p, 'negative_weight=', min(coeffs))
assert 1+F(7,16) > F(4,3)
print('INTENDED_NEGATIVE', 'negative-s counterpart at t=7/16 is nonphysical p=', 1+F(7,16))

# Sharp projector-budget endpoint controls and a wrong-conjugation mutant.
sharp = matrix()
for z in (0, 1, 2):
    sharp[z][z] = ONE
_, sharpB, _, _, _, sharpK, _ = report_pair('x20-k0-boundary', rho, sharp, (F(1),))
assert sharpB[1] == 20 and sharpK == 0
invariant = matrix()
for z in (0, 1, 2):
    w = 15-z
    for i in (z, w):
        for j in (z, w):
            invariant[i][j] = g(F(1,2))
assert spin(invariant) == invariant and trace_product(invariant, spin(invariant)) == 3
_, invariantB, _, _, _, invariantK, _ = report_pair('spin-fixed-k3-boundary', rho, invariant, (F(1),))
assert invariantK == 3 and invariantB[1] == invariantB[3] == 0
wrong_spin = spin(Q, conjugate=False)
wrong_op = next(op for op in product(range(4), repeat=4)
                if pauli_coeff(wrong_spin, op) != (-1)**sum(p != 0 for p in op)*cb[op])
assert wrong_spin != spin(Q)
print('INTENDED_NEGATIVE', 'omitting_transpose_breaks_Pauli_parity', 'op=', wrong_op,
      'wrong=', pauli_coeff(wrong_spin, wrong_op),
      'correct=', (-1)**sum(p != 0 for p in wrong_op)*cb[wrong_op])
s = F(-1,3)
wrong_odd = s*(1-s*s)*cc[1]+8*abs(s)**3*delta
actual_odd = s*cc[1]+s**3*cc[3]
assert wrong_odd != actual_odd
print('INTENDED_NEGATIVE', 'losing_negative_shrinkage_sign', 'wrong=', wrong_odd, 'actual=', actual_odd)
assert comparator_excess > 0 and not (H*(39-u) <= ((T-L)/t)**2)
print('INTENDED_NEGATIVE', 'incorrectly_admitting_186_criterion', 'square_excess=', comparator_excess)
print('ALL_EXACT_CONTROLS_COMPLETED')
