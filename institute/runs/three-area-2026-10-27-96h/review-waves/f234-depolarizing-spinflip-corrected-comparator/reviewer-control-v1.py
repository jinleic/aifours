#!/usr/bin/env python3
"""Independent finite checks for the frozen f234 written review; no author imports."""
from fractions import Fraction as F
from itertools import product, combinations

Z = (F(0), F(0))
O = (F(1), F(0))

def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def zmul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def zscale(a, x):
    return (a[0]*x, a[1]*x)

def zconj(a):
    return (a[0], -a[1])

def real(a):
    assert a[1] == 0, a
    return a[0]

def matrix():
    return [[Z for _ in range(16)] for _ in range(16)]

def spinflip(m, *, conjugate=True):
    out = matrix()
    for i in range(16):
        for j in range(16):
            v = m[15-i][15-j]
            if conjugate:
                v = zconj(v)
            sign = -1 if (i.bit_count()+j.bit_count()) % 2 else 1
            out[i][j] = zscale(v, sign)
    return out

def trprod(a, b):
    v = Z
    for i in range(16):
        for j in range(16):
            v = zadd(v, zmul(a[i][j], b[j][i]))
    return real(v)

def matmul(a, b):
    out = matrix()
    for i in range(16):
        for j in range(16):
            for k in range(16):
                out[i][j] = zadd(out[i][j], zmul(a[i][k], b[k][j]))
    return out

def pauli_coeff(m, ops):
    total = Z
    for j in range(16):
        v = O
        flip = 0
        for pos, op in enumerate(ops):
            bit = (j >> (3-pos)) & 1
            if op == 'X':
                flip ^= 1 << (3-pos)
            elif op == 'Y':
                flip ^= 1 << (3-pos)
                v = zmul(v, (F(0), F(-1 if bit else 1)))
            elif op == 'Z' and bit:
                v = zscale(v, -1)
        total = zadd(total, zmul(v, m[j][j ^ flip]))
    return real(total)

def sectors(m):
    values = {}
    norms = [F(0) for _ in range(5)]
    for ops in product('IXYZ', repeat=4):
        weight = sum(x != 'I' for x in ops)
        value = pauli_coeff(m, ops)
        values[ops] = value
        norms[weight] += value*value
    return values, norms

def overlaps(a, b):
    return [sum((a[o]*b[o] for o in a if sum(x != 'I' for x in o) == j), F(0)) for j in range(5)]

def channel_trace_by_units(rho, q, p):
    # Tensor the original single-qubit action on matrix units; no Pauli expansion.
    s = 1-p
    total = Z
    for a in range(16):
        for b in range(16):
            if rho[a][b] == Z:
                continue
            terms = [(0, 0, F(1))]
            for pos in range(4):
                abit = (a >> (3-pos)) & 1
                bbit = (b >> (3-pos)) & 1
                if abit == bbit:
                    factors = [(abit, abit, 1-p/2), (1-abit, 1-abit, p/2)]
                else:
                    factors = [(abit, bbit, s)]
                terms = [(2*u+iu, 2*v+iv, w*factor)
                         for u, v, w in terms for iu, iv, factor in factors]
            for u, v, factor in terms:
                total = zadd(total, zscale(zmul(rho[a][b], q[v][u]), factor))
    return real(total)

def ref3(t):
    return (3+8*t+6*t*t-t**4)/16

amps = {0: 3, 3: 1, 5: 1, 14: 1}
rho = matrix()
for a, va in amps.items():
    for b, vb in amps.items():
        rho[a][b] = (F(va*vb, 12), F(0))

q = matrix()
q[0][0] = O
q[5][5] = O
q[3][3] = q[15][15] = (F(1, 2), F(0))
q[3][15] = (F(0), F(-1, 2))
q[15][3] = (F(0), F(1, 2))
qd = matrix()
for i in (0, 3, 5):
    qd[i][i] = O
for projector in (q, qd):
    assert matmul(projector, projector) == projector
    assert sum(projector[i][i][0] for i in range(16)) == 3
    assert all(projector[i][j] == zconj(projector[j][i]) for i in range(16) for j in range(16))

qa, A = sectors(rho)
qb, B = sectors(q)
qdb, Bd = sectors(qd)
assert A == list(map(F, [1])) + [F(73,36), F(145,36), F(215,36), F(107,36)]
assert B == list(map(F, [9, 6, 12, 10, 11]))
assert Bd == list(map(F, [9, 12, 6, 12, 9]))
assert trprod(rho, rho) == 1 and trprod(rho, spinflip(rho)) == 0
assert matmul(rho, spinflip(rho)) == matrix()
assert spinflip(spinflip(q)) == q
kappa = trprod(q, spinflip(q))
deltaq = trprod(q, rho) - trprod(q, spinflip(rho))
assert (kappa, deltaq) == (F(1), F(1,2))
assert B[1]+B[3] == 24-8*kappa
assert B[2]+B[4] == 15+8*kappa
assert B[1] <= min(20, 24-8*kappa)
cs = overlaps(qa, qb)
assert cs[1]+cs[3] == 8*deltaq
_, qflip_coeff = sectors(spinflip(q))
assert qflip_coeff == B
print('STATE_PAULI_A', A)
print('COMPLEX_PROJECTOR_B', B, 'KAPPA', kappa, 'Q_DIFF', deltaq, 'C', cs)
print('DIAGONAL_PROJECTOR_B', Bd)

# All seven cuts, with first site fixed on the row side to avoid duplicates.
minor_receipts = []
for bits in range(7):
    left = (0,) + tuple(i for i in (1,2,3) if bits & (1 << (i-1)))
    right = tuple(i for i in range(4) if i not in left)
    def key(v, positions):
        return tuple((v >> (3-i)) & 1 for i in positions)
    rows = sorted({key(v, left) for v in range(16)})
    cols = sorted({key(v, right) for v in range(16)})
    tab = {(key(v, left), key(v, right)): amps.get(v, 0) for v in range(16)}
    found = None
    for r0, r1 in combinations(rows, 2):
        for c0, c1 in combinations(cols, 2):
            det = tab[r0,c0]*tab[r1,c1] - tab[r0,c1]*tab[r1,c0]
            if abs(det) == 3:
                found = (left, right, r0, r1, c0, c1, det)
                break
        if found:
            break
    assert found is not None, (left, right)
    minor_receipts.append(found)
print('SEVEN_CUT_MINORS_UNNORMALIZED', minor_receipts)

# Exact local marginal radii from support probabilities.
radii = []
for pos in range(4):
    prob0 = sum(F(v*v,12) for i,v in amps.items() if not ((i >> (3-pos)) & 1))
    prob1 = 1-prob0
    radii.append(abs(prob0-prob1))
    assert all((a^b).bit_count() != 1 for a,b in combinations(amps,2))
assert radii == [F(5,6), F(2,3), F(2,3), F(2,3)]
print('ONE_SITE_RADII', radii)

S, L = F(73,36), F(35,6)
u = L*L/S
assert u == F(1225,73)
t = F(7,16)
T = 8+6*t-t**3
E = A[2]+t**4*A[4]
H = A[2]+t*t*A[3]+t**4*A[4]
assert (T,E,H) == (F(43177,4096), F(1084403,262144), F(12456587,2359296))
k0 = (24-u)/8
assert k0 == F(527,584)
y0 = 39*(1-t*t)**2*S/((1-t*t)**2*S+t*t*E)
assert y0-u == F(79223837221,10373979995) > 0
assert F(48,5)**2-E*(39-u) == F(58990999,239206400) > 0
assert F(81,20)**2-8*S == F(649,3600) > 0
assert F(51,4)**2-39*E == F(323067,262144) > 0
U0 = (1-t*t)*L + 8*t*t + t*F(48,5)
U2 = (1-t*t)*F(81,20) + 8*t*t + t*F(51,4)
assert (U0,U2) == (F(26747,2560), F(53167,5120))
assert U2 < U0 and T-U0 == F(1909,20480) > 0
assert t*(T-U0)/16 == F(13363,5242880)
x0 = 39*S/(S+t*t*H)
assert x0-u == F(412938801007,44654331921) > 0
assert H*(39-u)-((T-L)/t)**2 == F(2129511149,1406533632) > 0
assert T > L and t > 0
assert 39*(15-S)-(5+(8-L)/t)**2 == F(717713,1764) > 0
assert 4*S == F(73,9) > F(64,9)
assert 6*S < F(7,2)**2 and 23*E < F(49,5)**2
fixed_bracket = T-(1-t*t)*F(7,2)-4*t*t-t*F(49,5)
assert fixed_bracket == F(54437,20480)
assert t*fixed_bracket/16 == F(381059,5242880)
print('T_E_H_U_K0_Y0_MINUS_U', T,E,H,u,k0,y0-u)
print('UNIFORM_U0_U2_T_MINUS_U0_GAP', U0,U2,T-U0,t*(T-U0)/16)
print('COMPARATOR_FAILURE_X0_MINUS_U_SQUARED_EXCESS', x0-u,H*(39-u)-((T-L)/t)**2)
print('FIXED_Q_BRACKET_AND_GAP', fixed_bracket,t*fixed_bracket/16)

# Previously declared example, no assumption that its comparator is adopted.
t3 = F(1,3)
H3 = A[2]+t3*t3*A[3]+t3**4*A[4]
T3 = 8+6*t3-t3**3
x03 = 39*S/(S+t3*t3*H3)
assert (H3,x03,H3*(39-u)) == (F(13787,2916), F(2075463,67004), F(11181257,106434))
assert x03 > u and H3*(39-u) < 121
assert 39*(S+t3*t3*H3)-T3*T3 == F(680,2187) > 0
assert 39*(15-S)-(5+(8-L)/t3)**2 == F(1121,3) > 0
print('COMPARATOR_T_ONE_THIRD_H_X0_SQUARE', H3,x03,H3*(39-u))

for projector, coeffs, name in ((q,qb,'complex'), (qd,qdb,'diagonal')):
    cj = overlaps(qa, coeffs)
    qdiff = trprod(projector, rho)-trprod(projector, spinflip(rho))
    for p in (F(0),F(9,16),F(2,3),F(1),F(4,3)):
        s = 1-p
        observed = channel_trace_by_units(rho,projector,p)
        pauli = (3+sum((s**j*cj[j] for j in range(1,5)), F(0)))/16
        assert observed == pauli
        assert s*cj[1]+s**3*cj[3] == s*(1-s*s)*cj[1]+8*s**3*qdiff
        print('TRACE',name,'p',p,'TRACE',observed,'REF',ref3(abs(s)),'GAP',ref3(abs(s))-observed)
        if name == 'complex' and p == F(9,16):
            assert (observed,ref3(abs(s)),ref3(abs(s))-observed) == (F(639301,2097152),F(498847,1048576),F(358393,2097152))
        if name == 'diagonal' and p == F(2,3):
            assert (observed,ref3(abs(s))-observed) == (F(5,18),F(19,162))
        if name == 'diagonal' and p == F(4,3):
            assert (observed,ref3(abs(s))-observed) == (F(41,324),F(29,108))

# Exhaust the diagonal hypersimplex vertices: independent finite illustration,
# not a replacement for the convexity proof for arbitrary complex projectors.
maxx = 0
for selected in combinations(range(16),3):
    onebody = [sum(1 if not ((v >> (3-i)) & 1) else -1 for v in selected) for i in range(4)]
    maxx = max(maxx, sum(v*v for v in onebody))
assert maxx == 20
print('HYPERSIMPLEX_560_VERTICES_MAX_X', maxx)

# Intended-reason negatives. Each one checks a logically wrong formula or boundary,
# not a claim that the original k3 inequality is false.
wrong = spinflip(q, conjugate=False)
first = next((i,j,spinflip(q)[i][j],wrong[i][j]) for i in range(16) for j in range(16) if spinflip(q)[i][j] != wrong[i][j])
assert first == (0,12,(F(0),F(-1,2)),(F(0),F(1,2))) or first == (0,12,(F(0),F(1,2)),(F(0),F(-1,2)))
print('NEGATIVE_MISSING_CONJUGATION_FIRST_WRONG_ENTRY', first)
s = -F(1,3)
wrong_odd = s*(1-s*s)*cs[1]+8*abs(s)**3*deltaq
correct_odd = s*cs[1]+s**3*cs[3]
assert wrong_odd != correct_odd and wrong_odd-correct_odd == 8*abs(s)**3
print('NEGATIVE_DROPPED_EPSILON_ODD_ERROR', wrong_odd-correct_odd)
assert F(3,4) > F(5,6)**2 and F(3,4) < F(5,6)
print('NEGATIVE_AMPLITUDE_CONFUSED_WITH_SQUARE', 'amplitude_squared',F(3,4),'wrong_cap_squared',F(25,36),'valid_squared_cap',F(5,6))
assert 1-3*F(4,3)/4 == 0 and 1-3*F(3,2)/4 == -F(1,8)
print('NEGATIVE_UNPHYSICAL_P', F(3,2), 'IDENTITY_KRAUS_WEIGHT', -F(1,8))
print('ALL_EXACT_CONTROLS_PASSED')
