#!/usr/bin/env python3
"""Independent four-qubit defect verifier. SOURCE PREPARED; NOT RUN HERE."""
import argparse
import itertools
import math
import sys
import time
from fractions import Fraction as F

N = 16
ROOT = math.sqrt(15.0)
TOL = 2e-9
RES_TOL = 2e-11
DEADLINE = None
CHECKS = 0
SPECTRA = 0
PREFIX_COMPARISONS = 0
CHANNEL_CASES = 0
MAX_RESIDUAL = 0.0
MAX_ORTHOGONALITY = 0.0
MAX_ROW_RESIDUAL = 0.0

class CheckFailure(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason

class Incomplete(Exception):
    pass

def tick():
    if DEADLINE is not None and time.perf_counter() >= DEADLINE:
        raise Incomplete("cooperative calculation deadline")

def need(condition, reason):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise CheckFailure(reason)

def expect_rejection(reason, operation):
    try:
        operation()
    except CheckFailure as exc:
        need(exc.reason == reason, "WRONG_MUTATION_REJECTION_REASON")
        print("CONTROL_REJECTED", reason)
        return
    raise CheckFailure("MUTATION_NOT_REJECTED:" + reason)

class E:
    """Exact a+b*sqrt(15)+i*(c+d*sqrt(15)); division only by rationals."""
    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = F(a), F(b), F(c), F(d)

    def __bool__(self):
        return bool(self.a or self.b or self.c or self.d)

    def __eq__(self, other):
        if not isinstance(other, E):
            try:
                other = E(other)
            except (TypeError, ValueError):
                return NotImplemented
        return (self.a, self.b, self.c, self.d) == (
            other.a, other.b, other.c, other.d)

    def __add__(self, other):
        if not isinstance(other, E):
            other = E(other)
        if not self:
            return other
        if not other:
            return self
        return E(self.a + other.a, self.b + other.b,
                 self.c + other.c, self.d + other.d)

    __radd__ = __add__

    def __neg__(self):
        return E(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other):
        return self + (-other if isinstance(other, E) else E(-other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, E):
            s = F(other)
            return E(self.a*s, self.b*s, self.c*s, self.d*s)
        if not self or not other:
            return Z
        if not other.b and not other.c and not other.d:
            return self * other.a
        if not self.b and not self.c and not self.d:
            return other * self.a
        a, b, c, d = self.a, self.b, self.c, self.d
        u, v, w, x = other.a, other.b, other.c, other.d
        return E(a*u + 15*b*v - c*w - 15*d*x,
                 a*v + b*u - c*x - d*w,
                 a*w + 15*b*x + c*u + 15*d*v,
                 a*x + b*w + c*v + d*u)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (F(1) / F(scalar))

    def conj(self):
        return E(self.a, self.b, -self.c, -self.d)

    def rotate(self, power):
        p = power % 4
        if p == 0:
            return self
        if p == 1:
            return E(-self.c, -self.d, self.a, self.b)
        if p == 2:
            return -self
        return E(self.c, self.d, -self.a, -self.b)

    def approximate(self):
        return complex(float(self.a) + float(self.b)*ROOT,
                       float(self.c) + float(self.d)*ROOT)

Z = E()
O = E(1)
II = E(c=1)
SQ15 = E(b=1)

def rq(value):
    need(not value.b and not value.c and not value.d,
         "EXPECTED_REAL_RATIONAL")
    return value.a

def zero(n=N):
    return [[Z for _ in range(n)] for _ in range(n)]

def identity(n=N):
    out = zero(n)
    for i in range(n):
        out[i][i] = O
    return out

I = identity()

def scale(A, s):
    return [[x*s for x in row] for row in A]

def add(*matrices):
    n = len(matrices[0])
    return [[sum((A[i][j] for A in matrices), Z)
             for j in range(n)] for i in range(n)]

def sub(A, B):
    return add(A, scale(B, -1))

def mm(A, B):
    n = len(A)
    out = zero(n)
    for i in range(n):
        for k, x in enumerate(A[i]):
            if not x:
                continue
            for j, y in enumerate(B[k]):
                if y:
                    out[i][j] = out[i][j] + x*y
    return out

def trace(A):
    return sum((A[i][i] for i in range(len(A))), Z)

def trprod(A, B):
    return sum((A[i][j]*B[j][i]
                for i in range(len(A)) for j in range(len(A))
                if A[i][j] and B[j][i]), Z)

def adjoint(A):
    return [[A[j][i].conj() for j in range(len(A))]
            for i in range(len(A))]

def vec(entries):
    out = [Z for _ in range(N)]
    for index, value in entries.items():
        out[index] = value if isinstance(value, E) else E(value)
    return out

def dot(u, v):
    return sum((a.conj()*b for a, b in zip(u, v)), Z)

def outer(v):
    return [[a*b.conj() for b in v] for a in v]

def theta(v):
    out = [Z for _ in range(N)]
    for x, value in enumerate(v):
        out[15-x] = value.conj() * (-1 if x.bit_count() % 2 else 1)
    return out

def spin(A):
    return [[A[15-j][15-i] *
             (-1 if (i.bit_count()+j.bit_count()) % 2 else 1)
             for j in range(N)] for i in range(N)]

def conjugate_W(A):
    return [[A[15-i][15-j] *
             (-1 if (i.bit_count()+j.bit_count()) % 2 else 1)
             for j in range(N)] for i in range(N)]

def pure(v):
    norm = rq(dot(v, v))
    need(norm > 0, "PURE_VECTOR_NONZERO")
    rho = scale(outer(v), F(1)/norm)
    overlap = dot(v, theta(v))/norm
    eta = rq(overlap*overlap.conj())
    need(mm(rho, rho) == rho, "ACTUAL_PURE_DENSITY")
    return rho, eta

def positions(x, sites):
    answer = 0
    for site in sites:
        answer = 2*answer + ((x >> (3-site)) & 1)
    return answer

def lifted_marginal(rho, sites):
    """Partial trace first; lift in the original physical tensor positions."""
    sites = tuple(sites)
    outside = tuple(s for s in range(4) if s not in sites)
    small = zero(1 << len(sites))
    inside_index = [positions(x, sites) for x in range(N)]
    outside_index = [positions(x, outside) for x in range(N)]
    for x in range(N):
        for y in range(N):
            if outside_index[x] == outside_index[y]:
                a, b = inside_index[x], inside_index[y]
                small[a][b] = small[a][b] + rho[x][y]
    out = zero()
    for x in range(N):
        for y in range(N):
            if outside_index[x] == outside_index[y]:
                out[x][y] = small[inside_index[x]][inside_index[y]]
    return out

def layers(rho):
    out = [I]
    for j in range(1, 5):
        tick()
        pieces = [lifted_marginal(rho, sites)
                  for sites in itertools.combinations(range(4), j)]
        out.append(add(*pieces))
    return out

def action(labels):
    """P|x> = i**phase[x] |permutation[x]>; I,X,Y,Z = 0,1,2,3."""
    permutation, phases = [], []
    for x in range(N):
        y, phase = x, 0
        for site, label in enumerate(labels):
            bit = (x >> (3-site)) & 1
            if label in (1, 2):
                y ^= 1 << (3-site)
            if label == 2:
                phase += 1 if bit == 0 else 3
            elif label == 3 and bit:
                phase += 2
        permutation.append(y)
        phases.append(phase % 4)
    return permutation, phases

PAULIS = [(sum(label != 0 for label in labels), action(labels))
          for labels in itertools.product(range(4), repeat=4)]
LOCAL = []
for site in range(4):
    group = []
    for label in (1, 2, 3):
        labels = [0]*4
        labels[site] = label
        group.append(action(labels))
    LOCAL.append(group)

def conjugate_pauli(A, pauli):
    permutation, phases = pauli
    out = zero()
    for x in range(N):
        for y in range(N):
            if A[x][y]:
                out[permutation[x]][permutation[y]] = (
                    A[x][y].rotate(phases[x]-phases[y]))
    return out

def pauli_layers(rho):
    R = [zero() for _ in range(5)]
    S = [Z for _ in range(5)]
    for index, (weight, pauli) in enumerate(PAULIS):
        if index % 32 == 0:
            tick()
        permutation, phases = pauli
        coefficient = sum((rho[x][permutation[x]].rotate(phases[x])
                           for x in range(N)), Z)
        need(not coefficient.c and not coefficient.d,
             "PHYSICAL_PAULI_EXPECTATION_REAL")
        if weight == 0:
            need(coefficient == 1, "PAULI_IDENTITY_COEFFICIENT")
            continue
        S[weight] = S[weight] + coefficient*coefficient
        for x in range(N):
            y = permutation[x]
            R[weight][y][x] = R[weight][y][x] + coefficient.rotate(phases[x])
    return R, [rq(s) for s in S]

def channel_pauli(rho, p):
    """Actual four local Pauli-sum channels, not a spectral surrogate."""
    A = rho
    for local in LOCAL:
        tick()
        A = add(scale(A, 1-F(3, 4)*p),
                *(scale(conjugate_pauli(A, P), p/4) for P in local))
    return A

def channel_erasure(rho, H, p):
    u, c = 1-p, p/2
    return add(scale(rho, u**4), scale(H[3], u**3*c),
               scale(H[2], u*u*c*c), scale(H[1], u*c**3),
               scale(I, c**4))

def prefixes(values):
    out, total = [], F(0)
    for x in values:
        total += x
        out.append(total)
    return out

def eigenvalues(A):
    """Complex Hermitian Jacobi; NUMERICAL, never an exact-root certificate."""
    global SPECTRA, MAX_RESIDUAL, MAX_ORTHOGONALITY, MAX_ROW_RESIDUAL
    tick()
    original = [[x.approximate() for x in row] for row in A]
    n = len(A)
    B = [row[:] for row in original]
    V = [[complex(i == j) for j in range(n)] for i in range(n)]
    need(max(abs(B[i][j]-B[j][i].conjugate())
             for i in range(n) for j in range(n)) < 1e-12,
         "NUMERICAL_INPUT_HERMITIAN")
    for _ in range(80):
        tick()
        row_residual = max(sum(abs(B[i][j]) for j in range(n) if j != i)
                           for i in range(n))
        if row_residual <= 1e-13:
            break
        for p in range(n-1):
            for q in range(p+1, n):
                z = B[p][q]
                az = abs(z)
                if az <= 1e-16:
                    continue
                app, aqq = B[p][p].real, B[q][q].real
                tau = (aqq-app)/(2*az)
                t = math.copysign(1.0, tau)/(abs(tau)+math.hypot(1.0, tau))
                c = 1/math.sqrt(1+t*t)
                s = t*c
                phase = z/az
                for k in range(n):
                    if k == p or k == q:
                        continue
                    u, v = B[k][p], B[k][q]
                    B[k][p] = c*u-s*phase.conjugate()*v
                    B[p][k] = B[k][p].conjugate()
                    B[k][q] = s*phase*u+c*v
                    B[q][k] = B[k][q].conjugate()
                B[p][p] = complex(app-t*az)
                B[q][q] = complex(aqq+t*az)
                B[p][q] = B[q][p] = 0j
                for k in range(n):
                    u, v = V[k][p], V[k][q]
                    V[k][p] = c*u-s*phase.conjugate()*v
                    V[k][q] = s*phase*u+c*v
    row_residual = max(sum(abs(B[i][j]) for j in range(n) if j != i)
                       for i in range(n))
    diagonal = [B[i][i].real for i in range(n)]
    residual_squared = 0.0
    orthogonality = 0.0
    for i in range(n):
        tick()
        for j in range(n):
            residual = (sum(original[i][k]*V[k][j] for k in range(n))
                        - V[i][j]*diagonal[j])
            residual_squared += abs(residual)**2
            gram = sum(V[k][i].conjugate()*V[k][j] for k in range(n))
            orthogonality = max(orthogonality, abs(gram-(i == j)))
    residual = math.sqrt(residual_squared)
    need(row_residual <= RES_TOL, "JACOBI_OFFDIAGONAL_RESIDUAL")
    need(residual <= RES_TOL, "JACOBI_EIGENPAIR_RESIDUAL")
    need(orthogonality <= RES_TOL, "JACOBI_ORTHOGONALITY_RESIDUAL")
    need(abs(sum(diagonal)-rq(trace(A))) <= TOL,
         "NUMERICAL_TRACE_RESIDUAL")
    MAX_RESIDUAL = max(MAX_RESIDUAL, residual)
    MAX_ORTHOGONALITY = max(MAX_ORTHOGONALITY, orthogonality)
    MAX_ROW_RESIDUAL = max(MAX_ROW_RESIDUAL, row_residual)
    SPECTRA += 1
    return sorted(diagonal, reverse=True)

def spectral_prefixes(A, reference, required, reason, count_output=False):
    global PREFIX_COMPARISONS
    values = eigenvalues(A)
    s, r, worst = 0.0, 0.0, -float("inf")
    for value, ref in zip(values, reference):
        s += value
        r += float(ref)
        excess = s-r
        worst = max(worst, excess)
        if count_output:
            PREFIX_COMPARISONS += 1
        if required:
            need(excess <= TOL, reason)
    need(abs(s-r) <= TOL, "NUMERICAL_FULL_PREFIX_EQUALITY")
    return values, worst

def product_reference(p):
    t = abs(1-p)
    a, b = (1+t)/2, (1-t)/2
    return sorted((a**(4-x.bit_count())*b**x.bit_count()
                   for x in range(N)), reverse=True)

def projectors():
    # Complex v+, fourteen computational vectors, then its orthogonal v-.
    first = scale(outer(vec({3: O, 5: II})), F(1, 2))
    last = scale(outer(vec({3: O, 5: -II})), F(1, 2))
    order = [0, 15, 6] + [x for x in range(N) if x not in (0, 15, 6, 3, 5)]
    pieces = [first] + [outer(vec({x: O})) for x in order] + [last]
    out, Q = [], zero()
    for rank, piece in enumerate(pieces, 1):
        Q = add(Q, piece)
        need(Q == adjoint(Q) and mm(Q, Q) == Q and trace(Q) == rank,
             "ACTUAL_COMPLEX_ORTHOGONAL_PROJECTOR")
        out.append(Q)
    need(out[-1] == I, "COMPLETE_PROJECTOR_FLAG")
    return out

def mixed_accept(d2):
    return d2 <= F(3, 13)

def pure_accept(eta):
    return eta >= F(55, 72)

def arithmetic_checks(product_H):
    literal = {
        1: [4]+[3]*4+[2]*6+[1]*4+[0],
        2: [6]+[3]*4+[1]*6+[0]*5,
        3: [4]+[1]*4+[0]*11,
        4: [1]+[0]*15,
    }
    references = {}
    for j in range(1, 5):
        for x in range(N):
            n = 4-x.bit_count()
            expected = math.comb(n, j) if n >= j else 0
            need(product_H[j][x][x] == expected,
                 "ACTUAL_PRODUCT_HAMMING_LAYER")
            need(all(not product_H[j][x][y] for y in range(N) if y != x),
                 "ACTUAL_PRODUCT_LAYER_DIAGONAL")
        references[j] = sorted((rq(product_H[j][x][x])
                                for x in range(N)), reverse=True)
        need(references[j] == literal[j], "PRODUCT_LAYER_REFERENCE")
    columns = {}
    for r in (16, 13):
        column = []
        for k, target in ((2, 5), (3, 6), (4, 7)):
            need(F(target) > F(8*k, r), "CAUCHY_INCREASING_AT_TARGET")
            column.append(F(target*target, k)+F((8-target)**2, r-k))
        columns[r] = column
    need(columns[16] == [F(92, 7), F(160, 13), F(37, 3)],
         "RANK16_CAUCHEY_BOUNDARIES")
    need(columns[13] == [F(293, 22), F(62, 5), F(445, 36)],
         "RANK13_CAUCHEY_BOUNDARIES")
    need(min(columns[16]) == F(160, 13), "RANK16_MINIMUM")
    need(min(columns[13]) == F(445, 36), "RANK13_MINIMUM")
    need(10*(1+F(3, 13)) == F(160, 13), "MIXED_THRESHOLD")
    need(10*(1+F(17, 72)) == F(445, 36), "PURE_THRESHOLD")
    need(1-F(17, 72) == F(55, 72), "PURE_ETA_THRESHOLD")
    need(F(3, 13) < F(15, 64) <= F(17, 72), "PURE_ONLY_STATE_REGION")
    need(F(17, 72) < F(1, 4), "PURE_REGION_H2_COMPATIBILITY")
    need(F(3, 13) < F(1, 4), "MIXED_REGION_H2_COMPATIBILITY")
    b0 = sorted((F(3, 4)*sum(1 if not (x >> (3-i)) & 1 else -1
                             for i in range(4)) for x in range(N)),
                reverse=True)
    M = prefixes(b0)
    L2 = prefixes(references[2])
    for k in range(1, 17):
        if k <= 4:
            invariant = [3, 6, 9, 10][k-1]
            bound = invariant+F(1, 2)*M[k-1]
        elif k <= 10:
            bound = k+8+F(1, 2)*M[k-1]
        else:
            bound = F(24)
        need(bound <= L2[k-1], "H2_UNIFORM_HALF_DEFECT_TABLE")
    need(mixed_accept(F(3, 13)), "MIXED_ENDPOINT_INCLUDED")
    need(pure_accept(F(55, 72)), "PURE_ENDPOINT_INCLUDED")
    print("EXACT_CAUCHEY_BOUNDARIES", columns)
    print("EXACT_H2_TABLE_ALL16", "checked at d=1/2")
    return references

def make_cases():
    Dv = vec({x: O for x in range(N) if x.bit_count() == 2})
    yA = vec({3: II, 5: II, 6: II, 9: -II, 10: -II, 12: -II})
    yB = vec({3: O+II, 5: -O, 10: -O, 12: O-II})
    need(theta(Dv) == Dv and rq(dot(Dv, Dv)) == 6, "DICKE_VECTOR")
    for y in (yA, yB):
        need(theta(y) == y and dot(Dv, y) == 0 and dot(y, y) == 6,
             "ACTUAL_THETA_FIXED_ORTHOGONAL_Y")
    vectors = [
        ("pure_q15_16", vec({0: SQ15, 15: SQ15, 3: II, 12: II}), F(49, 64)),
        ("pure_q1_2_outside", vec({0: O, 15: O, 3: II, 12: II}), F(0)),
        ("dicke", Dv, F(1)),
        ("dicke_yA", [4*x+y.rotate(1) for x, y in zip(Dv, yA)], F(225, 289)),
        ("dicke_yB", [4*x+y.rotate(1) for x, y in zip(Dv, yB)], F(225, 289)),
        ("coherent_eta0_old", vec({0: 3, 1: 2, 2: 2, 4: 2, 8: 2}), F(0)),
    ]
    cases, by_name = [], {}
    for name, vector, expected_eta in vectors:
        rho, eta = pure(vector)
        need(eta == expected_eta, "EXACT_SELECTED_PURE_ETA")
        case = dict(name=name, rho=rho, pure=True, eta=eta, d2=1-eta)
        cases.append(case)
        by_name[name] = case
    product, product_eta = pure(vec({0: O}))
    need(product_eta == 0, "PRODUCT_BASE_DEFECT")
    white = scale(I, F(1, 16))
    B, D = by_name["dicke_yB"]["rho"], by_name["dicke"]["rho"]
    mixed = [
        ("mixed_product_6_13", add(scale(white, F(7, 13)),
                                   scale(product, F(6, 13))),
         product, F(1), F(6, 13)),
        ("mixed_product_1_2_H2_boundary", add(scale(white, F(1, 2)),
                                             scale(product, F(1, 2))),
         product, F(1), F(1, 2)),
        ("mixed_complex_B_white", add(scale(B, F(3, 4)), scale(white, F(1, 4))),
         B, F(64, 289), F(3, 4)),
        ("mixed_complex_B_D", add(scale(B, F(3, 4)), scale(D, F(1, 4))),
         B, F(64, 289), F(3, 4)),
        ("white_rank16", white, product, F(1), F(0)),
    ]
    for name, rho, base, base_d2, factor in mixed:
        delta = scale(sub(rho, spin(rho)), F(1, 2))
        base_delta = scale(sub(base, spin(base)), F(1, 2))
        need(delta == scale(base_delta, factor), "EXACT_MIXED_DEFECT_SCALING")
        case = dict(name=name, rho=rho, pure=False, eta=None,
                    d2=factor*factor*base_d2)
        cases.append(case)
        by_name[name] = case
    need(B[3][5] == E(F(11, 102), c=F(7, 102)),
         "COMPLEX_PAIR_COHERENCE")
    M = by_name["mixed_complex_B_white"]["rho"]
    need(M[3][5] == E(F(11, 136), c=F(7, 136)),
         "MIXED_COMPLEX_COHERENCE")
    for site in range(4):
        single = lifted_marginal(M, (site,))
        need(all(not single[x][y] for x in range(N) for y in range(N) if x != y),
             "MIXED_ONE_SITE_MARGINAL_DIAGONAL")
    need(bool(M[3][5]), "MIXED_NONPRODUCT_DISCRIMINATOR")
    return cases, by_name, product

def audit_case(case, references, Qs, product):
    global CHANNEL_CASES
    tick()
    name, rho, d2 = case["name"], case["rho"], case["d2"]
    need(rho == adjoint(rho) and trace(rho) == 1, "DENSITY_HERMITIAN_TRACE")
    sigma = scale(add(rho, spin(rho)), F(1, 2))
    delta = sub(rho, sigma)
    need(spin(sigma) == sigma, "ACTUAL_SIGMA_INVARIANT")
    need(delta == scale(sub(rho, spin(rho)), F(1, 2)), "ACTUAL_DEFECT_HALF")
    H = layers(rho)
    G = layers(sigma)
    R, S = pauli_layers(rho)
    need(rho == scale(add(I, *R[1:]), F(1, 16)), "ALL_FOUR_PAULI_SECTORS")
    need(sigma == scale(add(I, R[2], R[4]), F(1, 16)),
         "SAME_STATE_EVEN_PART")
    need(delta == scale(add(R[1], R[3]), F(1, 16)), "SAME_STATE_ODD_PART")
    need(H[1] == add(scale(I, 2), scale(R[1], F(1, 2))), "H1_PAULI_IDENTITY")
    need(H[2] == scale(add(scale(I, 6), scale(R[1], 3), R[2]), F(1, 4)),
         "H2_PAULI_IDENTITY")
    need(H[3] == scale(add(scale(I, 4), scale(R[1], 3),
                           scale(R[2], 2), R[3]), F(1, 8)), "H3_PAULI_IDENTITY")
    need(H[4] == rho, "H4_ACTUAL_DENSITY")
    error_sum = add(*(conjugate_pauli(rho, P) for group in LOCAL for P in group))
    need(H[3] == add(scale(rho, 2), scale(error_sum, F(1, 2))),
         "H3_PHYSICAL_TWELVE_ERRORS")
    need(G[1] == scale(I, 2) and G[2] == add(I, G[3]), "ACTUAL_INVARIANT_H2")
    need(sub(H[2], G[2]) == scale(R[1], F(3, 4)), "ACTUAL_H2_PERTURBATION")
    need(sub(H[3], G[3]) == scale(add(scale(R[1], 3), R[3]), F(1, 8)),
         "ACTUAL_H3_PERTURBATION")
    need([rq(trace(H[j])) for j in range(1, 5)] == [32, 24, 8, 1],
         "ALL_LAYER_TRACES")
    moment = rq(trprod(H[3], H[3]))
    sigma_moment = rq(trprod(G[3], G[3]))
    need(moment == 4+F(9*S[1]+4*S[2]+S[3], 4), "GENERAL_H3_MOMENT")
    need(moment == sigma_moment+F(9*S[1]+S[3], 4), "EVEN_ODD_MOMENT_SPLIT")
    need(sigma_moment <= 10, "INVARIANT_MOMENT_CAP")
    need(S[1] <= 4*d2 and S[1]+S[3] <= 8*d2, "ACTUAL_DEFECT_PAULI_BOUNDS")
    need(moment <= 10*(1+d2), "MIXED_DEFECT_MOMENT_BOUND")
    need(rq(trprod(delta, delta)) <= d2/2, "TRACELESS_DEFECT_HS_BOUND")
    if case["pure"]:
        eta = case["eta"]
        need(moment == 8+3*S[1]+2*eta, "PURE_MOMENT_2ETA")
        need(S[1]+S[3] == 8*(1-eta), "PURE_ODD_PURITY")
        need(2*S[2]+S[3] == 12+S[1], "PURE_COMPLEMENTARY_PURITY")
    defect_values = eigenvalues(delta)
    actual_d = sum(abs(x) for x in defect_values)
    need(abs(actual_d*actual_d-float(d2)) <= TOL, "ACTUAL_TRACE_NORM_DEFECT")
    required = mixed_accept(d2) or (
        case["pure"] and pure_accept(case["eta"])) or name == "coherent_eta0_old"
    h2_required = d2 <= F(1, 4) or name == "coherent_eta0_old"
    h3_required = moment <= F(160, 13) or (
        case["pure"] and moment <= F(445, 36)) or name == "coherent_eta0_old"
    layer_values = {}
    for j, flag in ((1, True), (2, h2_required), (3, h3_required), (4, True)):
        values, _ = spectral_prefixes(H[j], references[j], flag,
                                      "NUMERICAL_H%d_PREFIX" % j)
        layer_values[j] = values
        need(values[-1] >= -TOL, "NUMERICAL_LAYER_POSITIVITY")
    need(layer_values[3][0] <= 4+TOL, "NUMERICAL_H3_OPERATOR_CAP")
    if case["pure"]:
        need(sum(x > 1e-8 for x in layer_values[3]) <= 13,
             "NUMERICAL_PURE_H3_RANK")
    invariant_values = eigenvalues(G[3])
    need(invariant_values[0] <= 2+TOL and sum(invariant_values[:4]) <= 6+TOL,
         "NUMERICAL_ACTUAL_SIGMA_SHARP_REFERENCE")
    layer_prefixes = {j: prefixes(references[j]) for j in references}
    worst_output = -float("inf")
    for p in (F(0), F(1, 3), F(1, 2), F(2, 3), F(1), F(7, 6), F(4, 3)):
        tick()
        output = channel_pauli(rho, p)
        need(output == channel_erasure(rho, H, p), "PAULI_VS_ERASURE_CHANNEL")
        need(output == adjoint(output) and trace(output) == 1,
             "ACTUAL_CHANNEL_HERMITIAN_TRACE")
        reference = product_reference(p)
        reference_output = channel_pauli(product, p)
        need(all(not reference_output[x][y] for x in range(N)
                 for y in range(N) if x != y), "PRODUCT_CHANNEL_DIAGONAL")
        need(sorted((rq(reference_output[x][x]) for x in range(N)),
                    reverse=True) == reference, "ACTUAL_PRODUCT_CHANNEL_SPECTRUM")
        t, b = abs(1-p), (1-abs(1-p))/2
        positive = channel_pauli(rho, 1-t)
        need(positive == add(scale(rho, t**4), scale(H[3], t**3*b),
                             scale(H[2], t*t*b*b), scale(H[1], t*b**3),
                             scale(I, b**4)), "POSITIVE_RETENTION_EXPANSION")
        ref_prefix = prefixes(reference)
        for k, Q in enumerate(Qs, 1):
            exact_reference = (t**4+t**3*b*layer_prefixes[3][k-1]
                               +t*t*b*b*layer_prefixes[2][k-1]
                               +t*b**3*layer_prefixes[1][k-1]+k*b**4)
            need(exact_reference == ref_prefix[k-1], "EXACT_COORDERED_REFERENCE")
            actual_terms = (trprod(Q, rho)*t**4+trprod(Q, H[3])*t**3*b
                            +trprod(Q, H[2])*t*t*b*b
                            +trprod(Q, H[1])*t*b**3+E(k*b**4))
            need(trprod(Q, positive) == actual_terms, "ONE_COMMON_Q_EXPANSION")
            if required:
                for j in (1, 2, 3, 4):
                    need(rq(trprod(Q, H[j])) <= layer_prefixes[j][k-1],
                         "EXACT_SELECTED_COMMON_Q_LAYER")
                need(rq(trprod(Q, positive)) <= ref_prefix[k-1],
                     "EXACT_SELECTED_COMMON_Q_OUTPUT")
            if p > 1:
                need(output == spin(positive), "FULL_TRANSPOSE_OUTPUT_IDENTITY")
                transported = spin(Q)
                need(transported == adjoint(transported)
                     and mm(transported, transported) == transported
                     and trace(transported) == k, "FULL_TRANSPOSE_PROJECTOR")
                need(trprod(Q, output) == trprod(transported, positive),
                     "FULL_TRANSPOSE_COMMON_Q_EXPECTATION")
        values, worst = spectral_prefixes(output, reference, required,
                                          "NUMERICAL_OUTPUT_PREFIX", True)
        need(values[-1] >= -TOL, "NUMERICAL_OUTPUT_POSITIVITY")
        worst_output = max(worst_output, worst)
        CHANNEL_CASES += 1
    print("EXACT_CASE", name, "eta", case["eta"], "d_squared", d2,
          "S1", S[1], "TrH3_squared", moment,
          "new_or_old_scoped", required)
    print("NUMERICAL_CASE", name, "trace_norm_defect", actual_d,
          "maximum_sampled_output_prefix_excess", worst_output,
          "tolerance", TOL,
          "classification", "SCOPED" if required else "OUTSIDE_REGION_DIAGNOSTIC")
    case.update(H=H, sigma=sigma, moment=moment, S1=S[1], numerical_d=actual_d)

def mutation_checks(by_name, Qs, product):
    q = by_name["pure_q15_16"]
    B = by_name["dicke_yB"]
    need(q["S1"] == 0 and q["moment"] == F(305, 32),
         "Q15_EXACT_MOMENT_VALUE")
    need(B["S1"] == F(256, 2601) and B["moment"] == F(8542, 867),
         "COMPLEX_DICKE_EXACT_MOMENT_VALUE")
    expect_rejection("DEFECT_HALF_FACTOR",
        lambda: need(abs((2*q["numerical_d"])**2-float(q["d2"])) <= TOL,
                     "DEFECT_HALF_FACTOR"))
    expect_rejection("PURE_MOMENT_2ETA",
        lambda: need(q["moment"] == 8+3*q["S1"], "PURE_MOMENT_2ETA"))
    expect_rejection("SIGMA_IS_ACTUAL_AVERAGE",
        lambda: need(scale(I, F(1, 16)) == B["sigma"],
                     "SIGMA_IS_ACTUAL_AVERAGE"))
    p = F(4, 3)
    positive = channel_pauli(B["rho"], F(2, 3))
    negative = channel_pauli(B["rho"], p)
    Q = Qs[0]
    correct = rq(trprod(Q, negative))
    transported = rq(trprod(spin(Q), positive))
    wrong = rq(trprod(conjugate_W(Q), positive))
    need(correct == transported == F(77, 972), "COMPLEX_Q_CORRECT_VALUE")
    need(wrong == F(1193, 16524) and correct-wrong == F(29, 4131),
         "COMPLEX_Q_TRANSPOSE_DISCRIMINATOR")
    expect_rejection("FULL_TRANSPOSE_COMPLEX_Q",
        lambda: need(correct == wrong, "FULL_TRANSPOSE_COMPLEX_Q"))
    p = F(1, 2)
    actual_prefix = prefixes(product_reference(p))[1]
    relaxed_prefix = actual_prefix+F(3, 32)
    expect_rejection("REFERENCE_IS_ACTUAL_PRODUCT",
        lambda: need(relaxed_prefix == actual_prefix,
                     "REFERENCE_IS_ACTUAL_PRODUCT"))
    expect_rejection("MIXED_ENDPOINT_INCLUDED",
        lambda: need(F(3, 13) < F(3, 13), "MIXED_ENDPOINT_INCLUDED"))
    expect_rejection("PURE_ENDPOINT_INCLUDED",
        lambda: need(F(55, 72) > F(55, 72), "PURE_ENDPOINT_INCLUDED"))
    expect_rejection("PURE_BAND_NOT_MIXED",
        lambda: need(not (q["d2"] <= F(17, 72)), "PURE_BAND_NOT_MIXED"))
    white_H3 = by_name["white_rank16"]["H"][3]
    need(white_H3 == scale(I, F(1, 2)), "EXACT_MIXED_RANK16_CONTROL")
    def rank_scope(is_pure, proposed_cap):
        need(is_pure or proposed_cap == 16, "PURE_RANK_SCOPE")
    rank_scope(True, 13)
    rank_scope(False, 16)
    expect_rejection("PURE_RANK_SCOPE", lambda: rank_scope(False, 13))
    ghz_plus, ep = pure(vec({0: O, 15: O}))
    ghz_minus, em = pure(vec({0: O, 15: -O}))
    need(ep == em == 1, "GHZ_COMPONENTS_IN_PURE_REGION")
    mixture = scale(add(ghz_plus, ghz_minus), F(1, 2))
    separable = scale(add(outer(vec({0: O})), outer(vec({15: O}))), F(1, 2))
    need(mixture == separable, "EXACT_SEPARABLE_MIXTURE_DECOMPOSITION")
    expect_rejection("MIXTURE_GME_SCOPE",
        lambda: need(mixture != separable, "MIXTURE_GME_SCOPE"))
    print("EXACT_TRANSPOSE_EXPECTATIONS", correct, wrong, correct-wrong)
    print("SCOPE_CONTROLS",
          "endpoint, threshold, rank and GME controls are not channel counterexamples")

def main():
    global DEADLINE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=55.0)
    args = parser.parse_args()
    if not math.isfinite(args.seconds) or not 1 <= args.seconds <= 55:
        parser.error("--seconds must be finite and between 1 and 55")
    start = time.perf_counter()
    DEADLINE = start+max(0.1, args.seconds-0.75)
    try:
        print("ASSURANCE", "exact field Q(sqrt(15),i); spectra NUMERICAL")
        print("LIMITS", "finite selected states and parameters; no universal numerical proof")
        cases, by_name, product = make_cases()
        references = arithmetic_checks(layers(product))
        Qs = projectors()
        for case in cases:
            audit_case(case, references, Qs, product)
        mutation_checks(by_name, Qs, product)
        need(len(cases) == 11 and CHANNEL_CASES == 77
             and PREFIX_COMPARISONS == 1232, "COMPLETE_DESIGNED_COVERAGE")
        tick()
        print("NUMERICAL_RESIDUALS",
              "eigenpair_frobenius", MAX_RESIDUAL,
              "orthogonality_entrywise", MAX_ORTHOGONALITY,
              "offdiagonal_row", MAX_ROW_RESIDUAL)
        print("COUNTS", "exact_or_numeric_checks", CHECKS, "spectra", SPECTRA,
              "channel_cases", CHANNEL_CASES, "output_prefixes", PREFIX_COMPARISONS)
        print("ELAPSED_SECONDS", time.perf_counter()-start)
        print("RESULT", "FINITE_CHECK_COMPLETE",
              "exact identities and selected expectations checked;",
              "spectral conclusions NUMERICAL only; no unrestricted theorem")
        return 0
    except Incomplete as exc:
        print("RESULT", "INCOMPLETE", str(exc),
              "completed_channel_cases", CHANNEL_CASES,
              "completed_output_prefixes", PREFIX_COMPARISONS)
        return 2
    except CheckFailure as exc:
        print("RESULT", "FAIL", exc.reason)
        return 1

if __name__ == "__main__":
    sys.exit(main())
