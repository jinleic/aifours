from fractions import Fraction as F
from itertools import combinations
import math
import sys
import time

START = time.monotonic()
DEADLINE = START + 55.0
PREFIX_TOL = 2e-9
RESIDUAL_TOL = 1e-10
PAIR_TOL = 1e-9
POLY_CHECKS = 0
MUTATIONS = 0

class Failure(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)

def must(condition, reason):
    if not condition:
        raise Failure(reason)

def tick():
    if time.monotonic() >= DEADLINE:
        raise Failure("DEADLINE_INCOMPLETE")

class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = F(r)
        self.i = F(i)

    def __add__(self, other):
        other = cg(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-cg(other))

    def __rsub__(self, other):
        return cg(other) - self

    def __mul__(self, other):
        other = cg(other)
        return G(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = cg(other)
        d = other.r * other.r + other.i * other.i
        must(d != 0, "ZERO_DIVISOR")
        return G((self.r * other.r + self.i * other.i) / d,
                 (self.i * other.r - self.r * other.i) / d)

    def __eq__(self, other):
        other = cg(other)
        return self.r == other.r and self.i == other.i

    def __bool__(self):
        return bool(self.r or self.i)

    def conj(self):
        return G(self.r, -self.i)

    def __repr__(self):
        if not self.i:
            return str(self.r)
        return "(" + str(self.r) + "," + str(self.i) + "i)"

def cg(x):
    return x if isinstance(x, G) else G(x)

Z = G()
ONE = G(1)
II = G(0, 1)

def weight(x):
    return bin(x).count("1")

def zero(n):
    return [[Z for _ in range(n)] for _ in range(n)]

def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = ONE
    return a

def copy_m(a):
    return [row[:] for row in a]

def add(a, b):
    return [[x + y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]

def scale(s, a):
    s = cg(s)
    return [[s * x for x in row] for row in a]

def adjoint(a):
    n = len(a)
    return [[a[j][i].conj() for j in range(n)] for i in range(n)]

def mm(a, b):
    n = len(a)
    c = zero(n)
    for i in range(n):
        tick()
        for k in range(n):
            x = a[i][k]
            if x:
                for j in range(n):
                    if b[k][j]:
                        c[i][j] = c[i][j] + x * b[k][j]
    return c

def tr(a):
    return sum((a[i][i] for i in range(len(a))), Z)

def expectation(q, a):
    n = len(a)
    return sum((q[i][j] * a[j][i]
                for i in range(n) for j in range(n)
                if q[i][j] and a[j][i]), Z)

def density(v):
    v = [cg(x) for x in v]
    norm = sum((x.r * x.r + x.i * x.i for x in v), F(0))
    must(norm > 0, "ZERO_SEED")
    return [[x * y.conj() / norm for y in v] for x in v]

def basis_projector(i, n=16):
    a = zero(n)
    a[i][i] = ONE
    return a

def check_density(a):
    must(a == adjoint(a), "DENSITY_HERMITICITY")
    must(tr(a) == ONE, "DENSITY_TRACE")

def check_projector(q, rank):
    must(q == adjoint(q), "PROJECTOR_HERMITICITY")
    must(mm(q, q) == q, "PROJECTOR_IDEMPOTENCE")
    must(tr(q) == G(rank), "PROJECTOR_RANK")

def project_bits(x, positions):
    y = 0
    for site in positions:
        y = (y << 1) | ((x >> (3 - site)) & 1)
    return y

def partial(a, positions):
    positions = tuple(positions)
    env = tuple(i for i in range(4) if i not in positions)
    local = [project_bits(i, positions) for i in range(16)]
    outside = [project_bits(i, env) for i in range(16)]
    out = zero(1 << len(positions))
    for i in range(16):
        tick()
        for j in range(16):
            if outside[i] == outside[j] and a[i][j]:
                x, y = local[i], local[j]
                out[x][y] = out[x][y] + a[i][j]
    return out

def lift(a, positions):
    positions = tuple(positions)
    env = tuple(i for i in range(4) if i not in positions)
    local = [project_bits(i, positions) for i in range(16)]
    outside = [project_bits(i, env) for i in range(16)]
    out = zero(16)
    for i in range(16):
        tick()
        for j in range(16):
            if outside[i] == outside[j]:
                out[i][j] = a[local[i]][local[j]]
    return out

def layers(a):
    h = [eye(16), zero(16), zero(16), zero(16), copy_m(a)]
    for size in (1, 2, 3):
        for positions in combinations(range(4), size):
            h[size] = add(h[size], lift(partial(a, positions), positions))
    return h

def spin(a):
    out = zero(16)
    for i in range(16):
        for j in range(16):
            sign = -1 if (weight(i) + weight(j)) % 2 else 1
            out[15 - j][15 - i] = sign * a[i][j]
    return out

def w_conjugate_without_transpose(a):
    out = zero(16)
    for i in range(16):
        for j in range(16):
            sign = -1 if (weight(i) + weight(j)) % 2 else 1
            out[15 - i][15 - j] = sign * a[i][j]
    return out

def spin_average(a):
    return scale(F(1, 2), add(a, spin(a)))

def pauli_action(kind, x, site):
    mask = 1 << (3 - site)
    bit = bool(x & mask)
    if kind == 0:
        return x, ONE
    if kind == 1:
        return x ^ mask, ONE
    if kind == 2:
        return x ^ mask, -II if bit else II
    return x, G(-1 if bit else 1)

def pauli_channel(a, p):
    p = F(p)
    must(0 <= p <= F(4, 3), "UNPHYSICAL_PAULI_PARAMETER")
    probabilities = [1 - 3 * p / 4, p / 4, p / 4, p / 4]
    must(all(x >= 0 for x in probabilities), "NEGATIVE_PAULI_WEIGHT")
    out = copy_m(a)
    for site in range(4):
        nxt = zero(16)
        for kind, probability in enumerate(probabilities):
            tick()
            if not probability:
                continue
            mapping = [pauli_action(kind, i, site) for i in range(16)]
            for i in range(16):
                di, pi = mapping[i]
                for j in range(16):
                    if out[i][j]:
                        dj, pj = mapping[j]
                        value = probability * pi * out[i][j] * pj.conj()
                        nxt[di][dj] = nxt[di][dj] + value
        out = nxt
    return out

def erasure_channel(h, p):
    p = F(p)
    retained, noise = 1 - p, p / 2
    out = zero(16)
    for j in range(5):
        out = add(out, scale(retained ** j * noise ** (4 - j), h[j]))
    return out

def real_matrix(a):
    must(all(not z.i for row in a for z in row), "EXPECTED_REAL_MATRIX")
    return [[z.r for z in row] for row in a]

def charpoly(a):
    r = real_matrix(a)
    n = len(r)
    b = [[F(i == j) for j in range(n)] for i in range(n)]
    coefficients = [F(1)]
    for degree in range(1, n + 1):
        c = [[F(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            tick()
            for k in range(n):
                if r[i][k]:
                    for j in range(n):
                        if b[k][j]:
                            c[i][j] += r[i][k] * b[k][j]
        coefficient = -sum((c[i][i] for i in range(n)), F(0)) / degree
        coefficients.append(coefficient)
        for i in range(n):
            c[i][i] += coefficient
        b = c
    must(all(not x for row in b for x in row), "CAYLEY_HAMILTON")
    return coefficients

def root_polynomial(roots):
    coefficients = [F(1)]
    for root in roots:
        out = [F(0)] * (len(coefficients) + 1)
        for i, value in enumerate(coefficients):
            out[i] += value
            out[i + 1] -= root * value
        coefficients = out
    return coefficients

def check_roots(a, roots, reason):
    global POLY_CHECKS
    coefficients = charpoly(a)
    must(coefficients == root_polynomial(roots), reason)
    POLY_CHECKS += 1
    return coefficients

def determinant(a):
    r = real_matrix(a)
    n = len(r)
    result = F(1)
    for k in range(n):
        tick()
        pivot = next((i for i in range(k, n) if r[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            r[k], r[pivot] = r[pivot], r[k]
            result = -result
        value = r[k][k]
        result *= value
        for i in range(k + 1, n):
            if r[i][k]:
                factor = r[i][k] / value
                for j in range(k + 1, n):
                    r[i][j] -= factor * r[k][j]
                r[i][k] = F(0)
    return result

def rank_real(a):
    r = real_matrix(a)
    n = len(r)
    row = 0
    for column in range(n):
        tick()
        pivot = next((i for i in range(row, n) if r[i][column]), None)
        if pivot is None:
            continue
        r[row], r[pivot] = r[pivot], r[row]
        value = r[row][column]
        for i in range(row + 1, n):
            if r[i][column]:
                factor = r[i][column] / value
                for j in range(column + 1, n):
                    r[i][j] -= factor * r[row][j]
                r[i][column] = F(0)
        row += 1
        if row == n:
            break
    return row

def prefixes(values):
    total = F(0)
    out = []
    for value in values:
        total += value
        out.append(total)
    return out

def reference_layer(j):
    a = zero(16)
    for i in range(16):
        zeros = 4 - weight(i)
        a[i][i] = G(math.comb(zeros, j) if zeros >= j else 0)
    return a

def reference_roots(j):
    a = reference_layer(j)
    return sorted((a[i][i].r for i in range(16)), reverse=True)

def reference_output_roots(t):
    a, b = (1 + t) / 2, (1 - t) / 2
    return [a ** (4 - w) * b ** w
            for w in range(5) for _ in range(math.comb(4, w))]

def dicke_output_roots(t):
    b = (1 - t) / 2
    rows = [(1, F(2), F(3), 1),
            (0, F(3, 2), F(5, 2), 2),
            (0, F(2, 3), F(5, 3), 3),
            (0, F(1, 6), F(7, 6), 6),
            (0, F(0), F(1), 4)]
    out = []
    for rho, h3, h2, multiplicity in rows:
        value = t ** 4 * rho + t ** 3 * b * h3
        value += t ** 2 * b ** 2 * h2 + 2 * t * b ** 3 + b ** 4
        out.extend([value] * multiplicity)
    must(out == sorted(out, reverse=True), "DICKE_OUTPUT_ORDER")
    return out

def numeric_eigenvalues(a):
    n = len(a)
    size = 2 * n
    original = [[0.0] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            x, y = float(a[i][j].r), float(a[i][j].i)
            original[i][j] = x
            original[i][j + n] = -y
            original[i + n][j] = y
            original[i + n][j + n] = x
    must(max(abs(original[i][j] - original[j][i])
             for i in range(size) for j in range(size)) <= 1e-14,
         "REALIFICATION_SYMMETRY")
    r = [row[:] for row in original]
    vectors = [[float(i == j) for j in range(size)] for i in range(size)]
    converged = False
    for _ in range(80):
        tick()
        off = max(abs(r[i][j]) for i in range(size) for j in range(i + 1, size))
        if off <= 1e-14:
            converged = True
            break
        for p in range(size):
            tick()
            for q in range(p + 1, size):
                apq = r[p][q]
                if abs(apq) <= 1e-16:
                    continue
                app, aqq = r[p][p], r[q][q]
                tau = (aqq - app) / (2.0 * apq)
                tangent = math.copysign(1.0, tau) / (
                    abs(tau) + math.hypot(1.0, tau))
                cosine = 1.0 / math.sqrt(1.0 + tangent * tangent)
                sine = tangent * cosine
                r[p][p] = app - tangent * apq
                r[q][q] = aqq + tangent * apq
                r[p][q] = r[q][p] = 0.0
                for k in range(size):
                    if k != p and k != q:
                        x, y = r[k][p], r[k][q]
                        r[k][p] = r[p][k] = cosine * x - sine * y
                        r[k][q] = r[q][k] = sine * x + cosine * y
                    x, y = vectors[k][p], vectors[k][q]
                    vectors[k][p] = cosine * x - sine * y
                    vectors[k][q] = sine * x + cosine * y
    must(converged, "JACOBI_CONVERGENCE")
    eigenvalues = [r[i][i] for i in range(size)]
    must(all(math.isfinite(x) for x in eigenvalues), "NONFINITE_EIGENVALUE")
    residual = 0.0
    for k in range(size):
        tick()
        square = 0.0
        for i in range(size):
            error = sum(original[i][j] * vectors[j][k] for j in range(size))
            error -= eigenvalues[k] * vectors[i][k]
            square += error * error
        residual = max(residual, math.sqrt(square))
    orthogonality = max(
        abs(sum(vectors[k][i] * vectors[k][j] for k in range(size))
            - float(i == j))
        for i in range(size) for j in range(size))
    must(residual <= RESIDUAL_TOL, "EIGENPAIR_RESIDUAL")
    must(orthogonality <= 1e-10, "EIGENVECTOR_ORTHOGONALITY")
    eigenvalues.sort(reverse=True)
    pair_gap = max(abs(eigenvalues[2 * i] - eigenvalues[2 * i + 1])
                   for i in range(n))
    must(pair_gap <= PAIR_TOL, "REALIFICATION_MULTIPLICITY")
    values = [(eigenvalues[2 * i] + eigenvalues[2 * i + 1]) / 2
              for i in range(n)]
    return values, residual, pair_gap

def assert_genuine_pure(a):
    must(expectation(a, a) == ONE, "PURE_SCHMIDT_PRECONDITION")
    cuts = [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3)]
    for cut in cuts:
        must(rank_real(partial(a, cut)) > 1, "GME_PRODUCT_CUT")

def reject(name, reason, operation):
    global MUTATIONS
    try:
        operation()
    except Failure as error:
        must(error.reason == reason, "WRONG_MUTATION_REASON:" + name)
    else:
        raise Failure("MUTATION_NOT_REJECTED:" + name)
    MUTATIONS += 1
    print("INTENDED_REJECTION", name, reason)

def run():
    must(sys.argv[1:] == ["--seconds", "55"], "ARGV_REQUIRES_SECONDS_55")
    tick()
    identity = eye(16)
    maximally_mixed = scale(F(1, 16), identity)
    product = basis_projector(0)
    dicke = density([ONE if weight(i) == 2 else Z for i in range(16)])
    hd = layers(dicke)
    reference = layers(product)
    for j in range(5):
        must(reference[j] == reference_layer(j), "REFERENCE_H" + str(j))

    pair = zero(4)
    pair[0][0] = pair[3][3] = G(F(1, 6))
    pair[1][1] = pair[2][2] = G(F(1, 3))
    pair[1][2] = pair[2][1] = G(F(1, 3))
    triple = zero(8)
    for i in range(8):
        for j in range(8):
            if weight(i) == weight(j) and weight(i) in (1, 2):
                triple[i][j] = G(F(1, 6))
    for cut in combinations(range(4), 1):
        marginal = partial(dicke, cut)
        must(marginal == scale(F(1, 2), eye(2)), "DICKE_SINGLE")
        check_roots(marginal, [F(1, 2)] * 2, "DICKE_SINGLE_POLYNOMIAL")
    for cut in combinations(range(4), 2):
        marginal = partial(dicke, cut)
        must(marginal == pair, "PARTIAL_TRACE")
        must(rank_real(marginal) == 3 and determinant(marginal) == 0,
             "DICKE_PAIR_RANK")
        check_roots(marginal, [F(2, 3), F(1, 6), F(1, 6), F(0)],
                    "DICKE_PAIR_POLYNOMIAL")
    for cut in combinations(range(4), 3):
        marginal = partial(dicke, cut)
        must(marginal == triple, "DICKE_TRIPLE")
        check_roots(marginal, [F(1, 2)] * 2 + [F(0)] * 6,
                    "DICKE_TRIPLE_POLYNOMIAL")

    diagonal2 = [F(1), F(3, 2), F(5, 3), F(3, 2), F(1)]
    diagonal3 = [F(0), F(1, 2), F(2, 3), F(1, 2), F(0)]
    for j, diagonal in [(2, diagonal2), (3, diagonal3)]:
        expected = zero(16)
        for x in range(16):
            for y in range(16):
                if x == y:
                    expected[x][y] = G(diagonal[weight(x)])
                elif weight(x) == weight(y) and weight(x ^ y) == 2:
                    expected[x][y] = G(F(1, 3))
        must(hd[j] == expected, "DICKE_ACTUAL_BLOCK_H" + str(j))

    spec2 = ([F(3)] + [F(5, 2)] * 2 + [F(5, 3)] * 3
             + [F(7, 6)] * 6 + [F(1)] * 4)
    spec3 = ([F(2)] + [F(3, 2)] * 2 + [F(2, 3)] * 3
             + [F(1, 6)] * 6 + [F(0)] * 4)
    check_roots(dicke, [F(1)] + [F(0)] * 15, "DICKE_DENSITY_POLYNOMIAL")
    check_roots(hd[1], [F(2)] * 16, "DICKE_H1_POLYNOMIAL")
    cp2 = check_roots(hd[2], spec2, "DICKE_H2_POLYNOMIAL")
    check_roots(hd[3], spec3, "DICKE_H3_POLYNOMIAL")
    det2 = determinant(hd[2])
    product2 = F(1)
    for value in spec2:
        product2 *= value
    must(det2 == product2 and cp2[-1] == det2, "DETERMINANT_CONSTANT")
    assert_genuine_pure(dicke)

    r1 = prefixes(reference_roots(1))
    r2 = prefixes(reference_roots(2))
    r3 = prefixes(reference_roots(3))
    s2, s3 = prefixes(spec2), prefixes(spec3)
    delta1 = [r1[k - 1] - 2 * k for k in range(1, 17)]
    delta2 = [r2[k] - s2[k] for k in range(16)]
    delta3 = [r3[k] - s3[k] for k in range(16)]
    sector = [(r3[k - 1] - min(2 * k, 8),
               r2[k - 1] - k - min(2 * k, 8),
               r1[k - 1] - 2 * k) for k in range(1, 17)]
    expected_sector = [
        (2,3,2), (1,3,3), (0,3,4), (-1,3,5),
        (0,5,6), (0,5,6), (0,5,6), (0,5,6),
        (0,5,6), (0,5,6), (0,5,6), (0,4,5),
        (0,3,4), (0,2,3), (0,1,2), (0,0,0)]
    expected_dicke = [
        (2,18,12), (3,21,9), (4,24,6), (5,32,8),
        (6,40,10), (6,36,6), (6,35,5), (6,34,4),
        (6,33,3), (6,32,2), (6,31,1), (5,24,0),
        (4,18,0), (3,12,0), (2,6,0), (0,0,0)]
    must(sector == expected_sector, "SECTOR_PREFIX_TABLE")
    actual_dicke = [(delta1[k], 6 * delta2[k], 6 * delta3[k])
                    for k in range(16)]
    must(actual_dicke == expected_dicke, "DICKE_PREFIX_TABLE")
    for k in range(16):
        print("EXACT_LAYER_GAP", k + 1, sector[k], actual_dicke[k])

    def sector_deficit(t):
        b = (1 - t) / 2
        value = -t ** 3 * b + 3 * t ** 2 * b ** 2 + 5 * t * b ** 3
        factored = t * b * (5 - 4 * t - 5 * t ** 2) / 4
        must(value == factored, "K4_FACTORIZATION")
        return value

    must(4 * 4 - 4 * 5 * (-5) == 4 * 29, "K4_ROOT_DISCRIMINANT")
    must(sector_deficit(F(4, 5)) == F(-7, 250), "K4_HIGH_T_DEFICIT")
    t, b = F(4, 5), F(1, 10)
    dicke_k4 = t ** 3 * b * delta3[3] + t ** 2 * b ** 2 * delta2[3]
    dicke_k4 += t * b ** 3 * delta1[3]
    must(dicke_k4 == F(133, 1250), "DICKE_K4_NOT_A_COUNTEREXAMPLE")

    u = [Z] * 16
    u[0], u[3] = ONE, II
    pure_u = density(u)
    complex_invariant = spin_average(pure_u)
    q = add(add(pure_u, basis_projector(5)), basis_projector(10))
    qp = spin(q)
    wrong_qp = w_conjugate_without_transpose(q)
    for candidate in (q, qp, wrong_qp):
        check_projector(candidate, 3)
    must(expectation(q, dicke) == G(F(5, 12)), "FIXED_Q_DICKE_INPUT")

    seed1 = density([G((i % 5) - 2, ((3 * i + 1) % 7) - 3)
                     for i in range(16)])
    seed2 = density([G(((i * i + 2) % 7) - 3, ((5 * i + 2) % 9) - 4)
                     for i in range(16)])
    mixed_seed = scale(F(1, 4),
                       add(add(scale(2, seed1), seed2), maximally_mixed))
    states = [
        ("Dicke", dicke),
        ("ComplexInvariant", complex_invariant),
        ("DenseSpinAverage", spin_average(seed1)),
        ("MixedSpinAverage", spin_average(mixed_seed)),
        ("MaxMixed", maximally_mixed)]
    parameters = [F(0), F(1, 2), F(1), F(4, 3)]
    exact_spectra = {
        F(0): [F(1)] + [F(0)] * 15,
        F(1, 2): ([F(49, 256)] + [F(27, 256)] * 2
                    + [F(17, 256)] * 3 + [F(11, 256)] * 6
                    + [F(9, 256)] * 4),
        F(1): [F(1, 16)] * 16,
        F(4, 3): ([F(27, 243)] + [F(21, 243)] * 2
                    + [F(16, 243)] * 3 + [F(13, 243)] * 6
                    + [F(12, 243)] * 4)}
    gap_numerators = {
        F(1, 2): [32,32,32,42,52,44,42,40,38,36,34,26,20,14,8,0],
        F(4, 3): [21,24,27,35,43,39,38,37,36,35,34,27,21,15,9,0]}
    channel_cases = 0
    exact_prefixes = 0
    numeric_prefixes = 0
    maximum_residual = 0.0
    maximum_pair_gap = 0.0
    dicke_negative_output = None
    for name, rho in states:
        tick()
        check_density(rho)
        must(spin(rho) == rho, "SPIN_INVARIANCE")
        h = hd if name == "Dicke" else layers(rho)
        must(h[1] == scale(2, identity), "INVARIANT_H1")
        must(h[2] == add(identity, h[3]), "INVARIANT_H2_H3")
        must([tr(h[j]) for j in (1, 2, 3)] == [G(32), G(24), G(8)],
             "ACTUAL_LAYER_TRACES")
        for p in parameters:
            tick()
            output = pauli_channel(rho, p)
            must(output == erasure_channel(h, p), "PAULI_ERASURE_EQUALITY")
            check_density(output)
            must(spin(output) == output, "OUTPUT_SPIN_INVARIANCE")
            if p == 1:
                must(output == maximally_mixed, "EXACT_FULL_PAULI_TWIRL")
            t = abs(1 - p)
            reference_prefix = prefixes(reference_output_roots(t))
            values, residual, pair_gap = numeric_eigenvalues(output)
            maximum_residual = max(maximum_residual, residual)
            maximum_pair_gap = max(maximum_pair_gap, pair_gap)
            must(min(values) >= -PREFIX_TOL, "NUMERICAL_OUTPUT_PSD")
            must(abs(sum(values) - 1.0) <= PREFIX_TOL, "NUMERICAL_TRACE")
            numerical_sum = 0.0
            for k, value in enumerate(values):
                numerical_sum += value
                must(float(reference_prefix[k]) - numerical_sum >= -PREFIX_TOL,
                     "NUMERICAL_PREFIX:" + name + ":" + str(p) + ":" + str(k + 1))
                numeric_prefixes += 1
            print("NUMERICAL_OUTPUT", name, "p=" + str(p),
                  "eigenvalues=" + ",".join(format(x, ".17g") for x in values),
                  "residual=" + format(residual, ".6g"),
                  "pair_gap=" + format(pair_gap, ".6g"))
            channel_cases += 1
            if name == "Dicke":
                roots = dicke_output_roots(t)
                must(roots == exact_spectra[p], "SELECTED_EXACT_SPECTRUM")
                check_roots(output, roots, "DICKE_OUTPUT_CHARACTERISTIC")
                actual_prefix = prefixes(roots)
                b = (1 - t) / 2
                gaps = []
                for k in range(16):
                    gap = reference_prefix[k] - actual_prefix[k]
                    expected = t ** 3 * b * delta3[k]
                    expected += t ** 2 * b ** 2 * delta2[k]
                    expected += t * b ** 3 * delta1[k]
                    must(gap == expected and gap >= 0, "EXACT_OUTPUT_PREFIX")
                    gaps.append(gap)
                    exact_prefixes += 1
                if p in gap_numerators:
                    denominator = 256 if p == F(1, 2) else 243
                    must(gaps == [F(x, denominator) for x in gap_numerators[p]],
                         "SELECTED_EXACT_GAP_TABLE")
                else:
                    must(gaps == [F(0)] * 16, "ENDPOINT_GAP_TABLE")
                print("EXACT_DICKE_OUTPUT", p, roots, "gaps", gaps)
                if p == F(4, 3):
                    dicke_negative_output = output

    must(expectation(q, dicke_negative_output) == G(F(7, 36)),
         "FIXED_Q_DICKE_OUTPUT")
    minus_c = None
    plus_c = None
    for label, rho in [("ComplexInvariant", complex_invariant),
                       ("UnaveragedDenseSeed", seed1)]:
        minus = pauli_channel(rho, F(4, 3))
        plus = pauli_channel(rho, F(2, 3))
        must(minus == spin(plus), "PHYSICAL_NEGATIVE_BRANCH_MATRIX")
        must(expectation(q, minus) == expectation(qp, plus),
             "Q_TRANSPOSE")
        print("EXACT_NEGATIVE_TRANSPORT", label, expectation(q, minus))
        if label == "ComplexInvariant":
            minus_c, plus_c = minus, plus
    must(expectation(q, minus_c) == G(F(31, 162)),
         "COMPLEX_Q_EXACT_EXPECTATION")
    must(expectation(wrong_qp, plus_c) == G(F(13, 81)),
         "OMITTED_TRANSPOSE_EXACT_EXPECTATION")
    must(expectation(q, minus_c) - expectation(wrong_qp, plus_c)
         == G(F(5, 162)), "OMITTED_TRANSPOSE_WITNESS")
    must(expectation(maximally_mixed, maximally_mixed) == G(F(1, 16)),
         "MAXMIX_PURITY")

    for j in (1, 2, 3):
        bad = copy_m(reference[j])
        bad[0][0] = bad[0][0] + 1
        reason = "REFERENCE_H" + str(j)
        reject(reason, reason,
               lambda bad=bad, j=j, reason=reason:
               must(bad == reference_layer(j), reason))
    bad_pair = copy_m(pair)
    bad_pair[0][0] = bad_pair[0][0] + F(1, 6)
    reject("partial_trace_entry", "PARTIAL_TRACE",
           lambda: must(bad_pair == partial(dicke, (0, 1)), "PARTIAL_TRACE"))
    bad_roots = spec2[:]
    bad_roots[-1] = F(0)
    reject("characteristic_multiplicity", "CHARACTERISTIC_MULTIPLICITY",
           lambda: must(cp2 == root_polynomial(bad_roots),
                        "CHARACTERISTIC_MULTIPLICITY"))
    reject("determinant_constant", "DETERMINANT_CONSTANT",
           lambda: must(cp2[-1] + 1 == det2, "DETERMINANT_CONSTANT"))
    bad_sector = sector[:]
    bad_sector[3] = (F(1), F(3), F(5))
    reject("fourth_prefix_sign", "K4_SIGN",
           lambda: must(bad_sector == expected_sector, "K4_SIGN"))
    reject("false_all_noise_relaxation", "K4_THRESHOLD",
           lambda: must(sector_deficit(F(4, 5)) >= 0, "K4_THRESHOLD"))
    reject("omitted_projector_transpose", "Q_TRANSPOSE",
           lambda: must(expectation(q, minus_c)
                        == expectation(wrong_qp, plus_c), "Q_TRANSPOSE"))
    reject("mixed_sector_or_hull_is_not_a_pure_GME_argument",
           "PURE_SCHMIDT_PRECONDITION",
           lambda: assert_genuine_pure(maximally_mixed))
    reject("pure_product_is_not_genuinely_entangled", "GME_PRODUCT_CUT",
           lambda: assert_genuine_pure(product))

    tick()
    must(channel_cases == 20, "CHANNEL_CASE_COUNT")
    must(exact_prefixes == 64, "EXACT_PREFIX_COUNT")
    must(numeric_prefixes == 320, "NUMERICAL_PREFIX_COUNT")
    must(POLY_CHECKS == 22, "CHARACTERISTIC_CHECK_COUNT")
    must(MUTATIONS == 11, "MUTATION_COUNT")
    print("PASS_SELECTED_FINITE_CASES_NOT_UNIVERSAL_PROOF")
    print("channel_cases", channel_cases,
          "exact_prefixes", exact_prefixes,
          "numerical_prefixes", numeric_prefixes,
          "exact_characteristic_checks", POLY_CHECKS,
          "intended_reason_mutations", MUTATIONS)
    print("maximum_numerical_eigenpair_residual", maximum_residual)
    print("maximum_realification_pair_gap", maximum_pair_gap)
    print("elapsed_seconds", time.monotonic() - START)

if __name__ == "__main__":
    try:
        run()
    except Failure as error:
        deadline = error.reason == "DEADLINE_INCOMPLETE"
        print("INCOMPLETE" if deadline else "FAIL", error.reason)
        sys.exit(2 if deadline else 1)
