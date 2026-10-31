from fractions import Fraction as F
from itertools import combinations, product
from time import monotonic

DEADLINE = None

class AuditError(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)

def need(condition, reason):
    if not condition:
        raise AuditError(reason)

def pulse():
    if DEADLINE is not None and monotonic() > DEADLINE:
        raise AuditError("TIME_LIMIT_INCOMPLETE")

def expect_bad(reason, callback):
    try:
        callback()
    except AuditError as exc:
        need(exc.reason == reason, "WRONG_REJECTION_REASON:" + exc.reason)
        return reason
    raise AuditError("EXPECTED_REJECTION_NOT_OBSERVED:" + reason)

def zero(n, m=None):
    if m is None:
        m = n
    return [[F(0) for _ in range(m)] for _ in range(n)]

def eye(n):
    a = zero(n)
    for j in range(n):
        a[j][j] = F(1)
    return a

def mt(a):
    return [list(row) for row in zip(*a)]

def madd(*args):
    n, m = len(args[0]), len(args[0][0])
    return [[sum((a[i][j] for a in args), F(0))
             for j in range(m)] for i in range(n)]

def mscale(a, s):
    return [[s * x for x in row] for row in a]

def msub(a, b):
    return madd(a, mscale(b, -1))

def mm(a, b):
    n, h, m = len(a), len(b), len(b[0])
    need(len(a[0]) == h, "MATRIX_DIMENSION")
    out = zero(n, m)
    for i in range(n):
        for k in range(h):
            x = a[i][k]
            if not x:
                continue
            for j in range(m):
                if b[k][j]:
                    out[i][j] += x * b[k][j]
    return out

def tr(a):
    return sum((a[j][j] for j in range(len(a))), F(0))

def trprod(a, b):
    return sum((a[i][j] * b[j][i]
                for i in range(len(a)) for j in range(len(a))), F(0))

def rank(a):
    b = [[F(x) for x in row] for row in a]
    rows, cols = len(b), len(b[0])
    r = 0
    for c in range(cols):
        pulse()
        pivot = next((i for i in range(r, rows) if b[i][c]), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        q = b[r][c]
        b[r] = [x / q for x in b[r]]
        for i in range(rows):
            if i != r and b[i][c]:
                q = b[i][c]
                b[i] = [x - q * y for x, y in zip(b[i], b[r])]
        r += 1
        if r == rows:
            break
    return r

def charpoly(a):
    n = len(a)
    b = eye(n)
    coeff = [F(1)]
    for k in range(1, n + 1):
        pulse()
        c = mm(a, b)
        ck = -tr(c) / k
        coeff.append(ck)
        for j in range(n):
            c[j][j] += ck
        b = c
    return tuple(coeff)

def rootpoly(roots):
    p = [F(1)]
    for e in roots:
        out = [F(0)] * (len(p) + 1)
        for j, c in enumerate(p):
            out[j] += c
            out[j + 1] -= c * e
        p = out
    return tuple(p)

def prefixes(values):
    out, s = [], F(0)
    for x in values:
        s += x
        out.append(s)
    return tuple(out)

def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])

def gconj(a):
    return (a[0], -a[1])

def gscale(a, s):
    return (s * a[0], s * a[1])

def inner(v, w):
    out = (F(0), F(0))
    for a, b in zip(v, w):
        c = gmul(gconj(a), b)
        out = (out[0] + c[0], out[1] + c[1])
    return out

def realvec(values):
    return [(x, 0) for x in values]

def linear(basis, coeff):
    n = len(basis[0])
    return [(sum(coeff[j] * basis[j][k][0] for j in range(len(coeff))),
             sum(coeff[j] * basis[j][k][1] for j in range(len(coeff))))
            for k in range(n)]

def tensor(v, w):
    return [gmul(a, b) for a in v for b in w]

UNITS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def pauli_map(word):
    n = len(word)
    dest, phase = [], []
    for k in range(1 << n):
        j, e = k, 0
        for q, letter in enumerate(word):
            mask = 1 << (n - 1 - q)
            bit = 1 if k & mask else 0
            if letter == "X":
                j ^= mask
            elif letter == "Y":
                j ^= mask
                e += 1 + 2 * bit
            elif letter == "Z":
                e += 2 * bit
            else:
                need(letter == "I", "PAULI_LETTER")
        dest.append(j)
        phase.append(e % 4)
    return dest, phase

def act(v, word):
    dest, phase = pauli_map(word)
    out = [(0, 0)] * len(v)
    for k, z in enumerate(v):
        out[dest[k]] = gmul(UNITS[phase[k]], z)
    return out

def outer(v, denominator):
    n = len(v)
    r, im = zero(n), zero(n)
    for i in range(n):
        for j in range(n):
            z = gmul(v[i], gconj(v[j]))
            r[i][j] = F(z[0]) / denominator
            im[i][j] = F(z[1]) / denominator
    return r, im

def padd(a, b):
    return madd(a[0], b[0]), madd(a[1], b[1])

def pscale(a, s):
    return mscale(a[0], s), mscale(a[1], s)

def ptranspose(a):
    return mt(a[0]), mt(a[1])

def pmm(a, b):
    return (msub(mm(a[0], b[0]), mm(a[1], b[1])),
            madd(mm(a[0], b[1]), mm(a[1], b[0])))

def ptrprod(a, b):
    return (trprod(a[0], b[0]) - trprod(a[1], b[1]),
            trprod(a[0], b[1]) + trprod(a[1], b[0]))

def conj_map(a, dest, phase):
    n = len(a[0])
    r, im = zero(n), zero(n)
    for k in range(n):
        for l in range(n):
            if not a[0][k][l] and not a[1][k][l]:
                continue
            z = gmul(UNITS[(phase[k] - phase[l]) % 4],
                     (a[0][k][l], a[1][k][l]))
            r[dest[k]][dest[l]] = z[0]
            im[dest[k]][dest[l]] = z[1]
    return r, im

def pcj(a, word):
    dest, phase = pauli_map(word)
    return conj_map(a, dest, phase)

def u_phase(a, qubit):
    n = len(a[0])
    phase = [(k >> (3 - qubit)) & 1 for k in range(n)]
    return conj_map(a, list(range(n)), phase)

def channel(a, p):
    out = zero(16), zero(16)
    for letters in product("IXYZ", repeat=4):
        pulse()
        weight = F(1)
        for letter in letters:
            weight *= 1 - 3 * p / 4 if letter == "I" else p / 4
        if weight:
            out = padd(out, pscale(pcj(a, "".join(letters)), weight))
    return out

def bits(k):
    return tuple((k >> (3 - q)) & 1 for q in range(4))

def extract(k, positions):
    out = 0
    for q in positions:
        out = 2 * out + ((k >> (3 - q)) & 1)
    return out

def partial(a, positions):
    other = tuple(q for q in range(4) if q not in positions)
    out = zero(1 << len(positions))
    for i in range(16):
        for j in range(16):
            if extract(i, other) == extract(j, other):
                out[extract(i, positions)][extract(j, positions)] += a[i][j]
    return out

def lift(a, positions):
    other = tuple(q for q in range(4) if q not in positions)
    out = zero(16)
    for i in range(16):
        for j in range(16):
            if extract(i, other) == extract(j, other):
                out[i][j] = a[extract(i, positions)][extract(j, positions)]
    return out

def physical_layers(rho):
    layers, marginals, lifted = {}, {}, {}
    for j in (1, 2, 3):
        h = zero(16)
        for s in combinations(range(4), j):
            pulse()
            marginal = partial(rho, s)
            need(mt(marginal) == marginal, "MARGINAL_HERMITIAN")
            need(tr(marginal) == 1, "MARGINAL_TRACE")
            term = lift(marginal, s)
            marginals[s] = marginal
            lifted[s] = term
            h = madd(h, term)
        layers[j] = h
    return layers, marginals, lifted

def paired(a, b, sign):
    v = [0] * 16
    v[a], v[b] = 1, sign
    return realvec(v)

EPLUS = [paired(a, 15 - a, 1) for a in (0, 3, 5, 6)]
EMINUS = [paired(a, 15 - a, -1) for a in (0, 3, 5, 6)]
FPLUS = [paired(1 << (3 - q), 15 ^ (1 << (3 - q)), 1)
         for q in range(4)]
FMINUS = [paired(1 << (3 - q), 15 ^ (1 << (3 - q)), -1)
          for q in range(4)]

MAGIC = [
    [(0, 1), (0, 0), (0, 0), (0, 1)],
    realvec((1, 0, 0, -1)),
    realvec((0, 1, 1, 0)),
    [(0, 0), (0, 1), (0, -1), (0, 0)],
]

def sgen(j, k):
    out = zero(4)
    out[k][j], out[j][k] = F(1), F(-1)
    return out

def magic_matrix(word):
    out = zero(4)
    for j in range(4):
        v = [gmul((0, -1), z) for z in act(MAGIC[j], word)]
        for i in range(4):
            z = gscale(inner(MAGIC[i], v), F(1, 2))
            need(z[1] == 0, "MAGIC_GENERATOR_REAL")
            out[i][j] = z[0]
    return out

def xmatrix(r):
    a, b, c, d = r
    return [[a, b, c, d], [b, a, d, c],
            [c, d, a, b], [d, c, b, a]]

HAD = [[1, 1, 1, 1], [1, 1, -1, -1],
       [1, -1, 1, -1], [1, -1, -1, 1]]
ODD = [[1, -1, -1, -1], [1, -1, 1, 1],
       [1, 1, -1, 1], [1, 1, 1, -1]]

def frames():
    out = []
    for j in range(4):
        out.append(tuple(F(int(i == j)) for i in range(4)))
    out += [tuple(F(x, 2) for x in row) for row in HAD]
    out += [tuple(F(x, 2) for x in row) for row in ODD]
    return out

def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))

def cvalues(r, frame=None):
    if frame is None:
        frame = frames()
    norm = sum(x * x for x in r)
    return [4 * dot(v, r) ** 2 / norm for v in frame]

def error_coefficients(v, axis, basis):
    out = [[None] * 4 for _ in range(4)]
    for q in range(4):
        word = "".join(axis if i == q else "I" for i in range(4))
        w = act(v, word)
        for j in range(4):
            out[j][q] = gscale(inner(basis[j], w), F(1, 2))
    return out

def projected_real_block(a, basis):
    need(all(z[1] == 0 for v in basis for z in v), "REAL_BLOCK_BASIS")
    return [[sum((F(basis[i][k][0]) * a[k][l] *
                  F(basis[j][l][0])
                  for k in range(16) for l in range(16)), F(0)) / 2
             for j in range(4)] for i in range(4)]

def twirl_from_vectors(v, denominator, rho):
    out = mscale(rho, 2)
    for q in range(4):
        for axis in "XYZ":
            word = "".join(axis if i == q else "I" for i in range(4))
            r, im = outer(act(v, word), denominator)
            need(im == zero(16), "ERROR_OUTER_REAL")
            out = madd(out, mscale(r, F(1, 2)))
    return out

def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

def principal_psd3(a):
    minors = [a[i][i] for i in range(3)]
    minors += [a[i][i] * a[j][j] - a[i][j] * a[j][i]
               for i, j in combinations(range(3), 2)]
    minors.append(det3(a))
    return all(x >= 0 for x in minors)

def projector(q, expected_rank, reason):
    need(mt(q) == q, reason)
    need(mm(q, q) == q, reason)
    need(tr(q) == expected_rank, reason)
    need(rank(q) == expected_rank, reason)

def complex_projector(q, expected_rank):
    need(mt(q[0]) == q[0], "COMPLEX_PROJECTOR_HERMITIAN")
    need(mt(q[1]) == mscale(q[1], -1),
         "COMPLEX_PROJECTOR_HERMITIAN")
    need(pmm(q, q) == q, "COMPLEX_PROJECTOR_IDEMPOTENT")
    need((tr(q[0]), tr(q[1])) == (F(expected_rank), F(0)),
         "COMPLEX_PROJECTOR_RANK")

def common_certificate(qrho, qlayer, rho, h):
    need(qrho == qlayer, "COMMON_PROJECTOR")
    projector(qrho, 4, "COMMON_PROJECTOR")
    need(trprod(qrho, rho) == 1, "COMMON_PROJECTOR")
    need(trprod(qlayer, h) == 6, "COMMON_PROJECTOR")

def polyadd(a, b):
    n = max(len(a), len(b))
    return tuple((a[i] if i < len(a) else F(0)) +
                 (b[i] if i < len(b) else F(0)) for i in range(n))

def polyscale(a, s):
    return tuple(s * x for x in a)

def polymul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)

def polypow(a, n):
    out = (F(1),)
    for _ in range(n):
        out = polymul(out, a)
    return out

def finite_audit():
    global DEADLINE
    started = monotonic()
    DEADLINE = started + 50.0
    controls = []
    i16 = eye(16)
    z16 = zero(16)

    expected_generators = [
        madd(sgen(0, 2), sgen(1, 3)),
        msub(sgen(0, 2), sgen(1, 3)),
        msub(sgen(0, 1), sgen(2, 3)),
        madd(sgen(0, 1), sgen(2, 3)),
        madd(mscale(sgen(0, 3), -1), sgen(1, 2)),
        madd(sgen(0, 3), sgen(1, 2)),
    ]
    words = ("XI", "IX", "ZI", "IZ", "YI", "IY")
    generators = [magic_matrix(word) for word in words]
    need(generators == expected_generators, "MAGIC_GENERATOR_TABLE")
    controls.append(expect_bad("MAGIC_ORIENTATION", lambda:
        need(generators[0] == mscale(expected_generators[0], -1),
             "MAGIC_ORIENTATION")))

    for d in ((1, 0, 0, 0), (1, -2, 3, 4)):
        pulse()
        lhs = linear([tensor(m, m) for m in MAGIC], d)
        a, b, c, e = d
        numerators = (-a + b, -a - b, c - e, c + e)
        rhs = linear(EPLUS, numerators)
        need(lhs == rhs, "NORMAL_FORM_CONVERSION")
        need(sum(x * x for x in numerators) ==
             2 * sum(x * x for x in d), "NORMAL_FORM_NORM")

    reflected_projector = outer(MAGIC[0], 1)
    need(reflected_projector[1] == zero(4), "REFLECTION_REAL")
    reflection = msub(eye(4), reflected_projector[0])
    need(charpoly(reflection) ==
         rootpoly((F(-1), F(1), F(1), F(1))), "REFLECTION_SPECTRUM")
    def real_pauli_matrix(word):
        dest, phase = pauli_map(word)
        out = zero(4)
        for k in range(4):
            need(UNITS[phase[k]][1] == 0, "REAL_PAULI")
            out[dest[k]][k] = F(UNITS[phase[k]][0])
        return out
    xleft = real_pauli_matrix("XI")
    zright = real_pauli_matrix("IZ")
    reflected_x = mm(mm(reflection, xleft), mt(reflection))
    commutator = msub(mm(reflected_x, zright),
                     mm(zright, reflected_x))
    controls.append(expect_bad("FIXED_SITE_PRODUCT", lambda:
        need(commutator == zero(4), "FIXED_SITE_PRODUCT")))

    def cnot(v):
        out = [(0, 0)] * 4
        for k in range(4):
            out[k ^ (1 if k & 2 else 0)] = v[k]
        return out
    bell = cnot(realvec((1, 0, 1, 0)))
    need(bell[0][0] * bell[3][0] -
         bell[1][0] * bell[2][0] != 0, "CNOT_ENTANGLES")
    cnot_magic = [[gscale(inner(MAGIC[i], cnot(MAGIC[j])), F(1, 2))
                   for j in range(4)] for i in range(4)]
    controls.append(expect_bad("CNOT_NOT_REAL_INTERFACE", lambda:
        need(all(z[1] == 0 for row in cnot_magic for z in row),
             "CNOT_NOT_REAL_INTERFACE")))

    frame = frames()
    for b in range(3):
        for i in range(4):
            for j in range(4):
                need(dot(frame[4 * b + i], frame[4 * b + j]) ==
                     int(i == j), "FRAME_ORTHONORMAL")
    for i, j in combinations(range(12), 2):
        target = F(0) if i // 4 == j // 4 else F(1, 2)
        need(abs(dot(frame[i], frame[j])) == target, "FRAME_CROSS")
    histogram = {}
    gram_count = 0
    for triple in combinations(range(12), 3):
        pulse()
        g = [[dot(frame[i], frame[j]) for j in triple] for i in triple]
        need(principal_psd3(msub(mscale(eye(3), 2), g)), "GRAM_BOUND")
        polynomial = charpoly(g)
        histogram[polynomial] = histogram.get(polynomial, 0) + 1
        gram_count += 1
    expected_histogram = {
        (F(1), F(-3), F(3), F(-1)): 12,
        (F(1), F(-3), F(5, 2), F(-1, 2)): 144,
        (F(1), F(-3), F(9, 4), F(-1, 2)): 48,
        (F(1), F(-3), F(9, 4), F(0)): 16,
    }
    need(gram_count == 220, "GRAM_COUNT")
    need(histogram == expected_histogram, "GRAM_CENSUS")
    triple = (0, 4, 9)
    g = [[dot(frame[i], frame[j]) for j in triple] for i in triple]
    doubled_cross = [[g[i][j] if i == j else 2 * g[i][j]
                      for j in range(3)] for i in range(3)]
    controls.append(expect_bad("GRAM_BOUND", lambda:
        need(principal_psd3(msub(mscale(eye(3), 2), doubled_cross)),
             "GRAM_BOUND")))

    product_vector = realvec((1,) + (0,) * 15)
    product_density = outer(product_vector, 1)
    reference_layers, _, _ = physical_layers(product_density[0])
    reference_layer_spectra = {}
    for j in (1, 2, 3):
        a = reference_layers[j]
        need(all(a[k][l] == 0 for k in range(16)
                 for l in range(16) if k != l), "REFERENCE_LAYER_DIAGONAL")
        reference_layer_spectra[j] = sorted(
            (a[k][k] for k in range(16)), reverse=True)
    expected_layer_spectra = {
        3: [F(4)] + [F(1)] * 4 + [F(0)] * 11,
        2: [F(6)] + [F(3)] * 4 + [F(1)] * 6 + [F(0)] * 5,
        1: [F(4)] + [F(3)] * 4 + [F(2)] * 6 + [F(1)] * 4 + [F(0)],
    }
    need(reference_layer_spectra == expected_layer_spectra,
         "REFERENCE_LAYER_SPECTRA")
    rprefix = {j: prefixes(reference_layer_spectra[j]) for j in (1, 2, 3)}
    coefficient_table = []
    for k in range(1, 17):
        m = F(6) if k == 4 else F(min(2 * k, 8))
        coefficient_table.append((rprefix[3][k - 1] - m,
                                  rprefix[2][k - 1] - k - m,
                                  rprefix[1][k - 1] - 2 * k))
    expected_table = [
        (2, 3, 2), (1, 3, 3), (0, 3, 4), (1, 5, 5),
        (0, 5, 6), (0, 5, 6), (0, 5, 6), (0, 5, 6),
        (0, 5, 6), (0, 5, 6), (0, 5, 6), (0, 4, 5),
        (0, 3, 4), (0, 2, 3), (0, 1, 2), (0, 0, 0),
    ]
    need(coefficient_table == expected_table, "PREFIX_COEFFICIENT_TABLE")

    apoly, bpoly = (F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2))
    reference_fourth_poly = polyadd(
        polypow(apoly, 4),
        polyscale(polymul(polypow(apoly, 3), bpoly), 3))
    f4poly = (F(1, 4), F(0), F(1), F(0), F(-1, 4))
    gap_poly = polyadd(reference_fourth_poly, polyscale(f4poly, -1))
    gap_factor_poly = (F(0), F(5, 8), F(-5, 8), F(-1, 8), F(1, 8))
    need(gap_poly == gap_factor_poly, "GAP_POLYNOMIAL_IDENTITY")
    controls.append(expect_bad("GAP_SIGN", lambda:
        need(gap_poly == polyscale(gap_factor_poly, -1), "GAP_SIGN")))

    parameters = (F(0), F(1, 2), F(1), F(4, 3))
    reference_outputs, reference_prefixes = {}, {}
    for p in parameters:
        actual = channel(product_density, p)
        need(actual[1] == z16, "REFERENCE_OUTPUT_REAL")
        need(all(actual[0][i][j] == 0 for i in range(16)
                 for j in range(16) if i != j), "REFERENCE_OUTPUT_DIAGONAL")
        spectrum = sorted((actual[0][j][j] for j in range(16)),
                          reverse=True)
        t = abs(1 - p)
        a, b = (1 + t) / 2, (1 - t) / 2
        expected = sorted((a ** (4 - sum(bits(k))) * b ** sum(bits(k))
                           for k in range(16)), reverse=True)
        need(spectrum == expected, "PHYSICAL_REFERENCE_SPECTRUM")
        reference_outputs[p] = spectrum
        reference_prefixes[p] = prefixes(spectrum)

    inputs = (
        ("sharp", (2, 1, 1, 0)),
        ("ghz", (1, 0, 0, 0)),
        ("equal", (1, 1, 1, 1)),
        ("signed_generic", (1, -2, 3, 4)),
    )
    case_results, retained = {}, {}
    for name, r in inputs:
        pulse()
        norm = sum(x * x for x in r)
        denominator = 2 * norm
        v = linear(EPLUS, r)
        rho_parts = outer(v, denominator)
        rho, im = rho_parts
        need(im == z16 and mt(rho) == rho, "INPUT_HERMITIAN")
        need(tr(rho) == 1 and rank(rho) == 1, "INPUT_PURE_DENSITY")
        need(pcj(ptranspose(rho_parts), "YYYY") == rho_parts,
             "INPUT_SPIN_FLIP")
        layers, marginals, lifted = physical_layers(rho)
        h = layers[3]
        need(len(marginals) == 14, "ALL_PROPER_MARGINALS")
        need(layers[1] == mscale(i16, 2), "H1_IDENTITY")
        need(layers[2] == madd(i16, h), "H2_IDENTITY")
        need(tr(h) == 8, "H3_TRACE")
        twirl = twirl_from_vectors(v, denominator, rho)
        need(twirl == h, "PHYSICAL_TWIRL")

        mx = xmatrix(r)
        my = xmatrix((r[0], -r[1], -r[2], -r[3]))
        mz = [[r[i] * HAD[i][j] for j in range(4)] for i in range(4)]
        actual_x = error_coefficients(v, "X", FPLUS)
        actual_y = error_coefficients(v, "Y", FMINUS)
        actual_z = error_coefficients(v, "Z", EMINUS)
        need(actual_x == [[(F(x), F(0)) for x in row] for row in mx],
             "X_PHYSICAL_ERROR_COLUMNS")
        need(actual_y == [[(F(0), F(x)) for x in row] for row in my],
             "Y_PHYSICAL_ERROR_COLUMNS")
        need(actual_z == [[(F(x), F(0)) for x in row] for row in mz],
             "Z_PHYSICAL_ERROR_COLUMNS")
        for matrix, basis in ((mx, FPLUS), (my, FMINUS), (mz, EMINUS)):
            predicted = mscale(mm(matrix, mt(matrix)), F(1, 2 * norm))
            need(projected_real_block(h, basis) == predicted,
                 "PHYSICAL_ERROR_BLOCK")
        even_block = [[F(2 * r[i] * r[j], norm) for j in range(4)]
                      for i in range(4)]
        need(projected_real_block(h, EPLUS) == even_block,
             "EVEN_PLUS_BLOCK")

        c = cvalues(r)
        hspectrum = sorted([F(2)] + [x / 2 for x in c] +
                           [F(0)] * 3, reverse=True)
        hpoly = charpoly(h)
        need(hpoly == rootpoly(hspectrum), "ACTUAL_H3_CHARPOLY")
        need(sum(hspectrum) == 8, "H3_SPECTRAL_TRACE")
        need(prefixes(hspectrum)[3] <= 6, "FINITE_H3_FOURTH")
        outputs = {}
        channel_results = {}
        for p in parameters:
            pulse()
            actual = channel(rho_parts, p)
            need(actual[1] == z16, "OUTPUT_REAL")
            t = abs(1 - p)
            a, b = (1 + t) / 2, (1 - t) / 2
            alpha, beta = t * t * a * b, a * a * b * b
            reduced = madd(mscale(rho, t ** 4), mscale(h, alpha),
                           mscale(i16, beta))
            need(actual[0] == reduced, "ACTUAL_CHANNEL_REDUCTION")
            expected_eigenvalues = sorted(
                [t ** 4 + 2 * alpha + beta] +
                [alpha * x / 2 + beta for x in c] + [beta] * 3,
                reverse=True)
            need(charpoly(actual[0]) == rootpoly(expected_eigenvalues),
                 "ACTUAL_OUTPUT_CHARPOLY")
            oprefix = prefixes(expected_eigenvalues)
            gaps = tuple(x - y for x, y in
                         zip(reference_prefixes[p], oprefix))
            need(all(x >= 0 for x in gaps), "ALL16_PREFIXES")
            need(gaps[-1] == 0, "OUTPUT_TRACE_ONE")
            if 0 < t < 1:
                need(all(x > 0 for x in gaps[:-1]),
                     "FINITE_PROPER_PREFIX_STRICTNESS")
            if name == "sharp":
                f4 = (1 + 4 * t * t - t ** 4) / 4
                gap = t * (1 - t) * (5 - t * t) / 8
                need(oprefix[3] == f4, "SHARP_F4")
                need(gaps[3] == gap, "SHARP_REFERENCE_GAP")
            outputs[p] = actual
            channel_results[p] = {
                "spectrum": tuple(expected_eigenvalues),
                "prefixes": oprefix,
                "reference_prefixes": reference_prefixes[p],
                "gaps": gaps,
            }
        case_results[name] = {
            "r": r, "normalizer_squared": norm,
            "H3_spectrum": tuple(hspectrum),
            "H3_charpoly": hpoly, "H3_rank": rank(h),
            "channels": channel_results,
        }
        retained[name] = (v, rho_parts, layers, lifted, twirl,
                          mx, my, mz, actual_y, outputs)

    (v, rho_parts, layers, lifted, twirl,
     mx, my, mz, actual_y, outputs) = retained["sharp"]
    rho, h = rho_parts[0], layers[3]
    need(rank(h) == 10, "SHARP_H3_RANK")
    uz = EMINUS[0]
    ux = linear(FPLUS, (1, 1, 1, 1))
    uy = linear(FMINUS, (1, -1, -1, 1))
    q = madd(rho, outer(uz, 2)[0], outer(ux, 8)[0], outer(uy, 8)[0])
    projector(q, 4, "SHARP_PROJECTOR")
    common_certificate(q, q, rho, h)
    need(charpoly(q) == rootpoly([F(1)] * 4 + [F(0)] * 12),
         "SHARP_PROJECTOR_CHARPOLY")

    controls.append(expect_bad("Y_VECTOR_PHASE", lambda:
        need(actual_y == [[(F(x), F(0)) for x in row] for row in my],
             "Y_VECTOR_PHASE")))
    bad_my = [row[:] for row in my]
    bad_my[0][1] = -bad_my[0][1]
    controls.append(expect_bad("Y_RELATIVE_SIGN", lambda:
        need(actual_y == [[(F(0), F(x)) for x in row] for row in bad_my],
             "Y_RELATIVE_SIGN")))
    wrong_z_block = mscale(mm(mt(mz), mz), F(1, 12))
    controls.append(expect_bad("TRANSPOSED_Z_FACTOR", lambda:
        need(projected_real_block(h, EMINUS) == wrong_z_block,
             "TRANSPOSED_Z_FACTOR")))
    missing = msub(h, lifted[(1, 2, 3)])
    controls.append(expect_bad("MISSING_MARGINAL", lambda:
        need(missing == twirl, "MISSING_MARGINAL")))
    bad_frame = list(frame)
    bad_frame[5] = bad_frame[4]
    bad_c = cvalues((2, 1, 1, 0), bad_frame)
    controls.append(expect_bad("C_SIGN", lambda:
        need(charpoly(h) == rootpoly(
            [F(2)] + [x / 2 for x in bad_c] + [F(0)] * 3), "C_SIGN")))

    extra = outer(EPLUS[3], 2)[0]
    q_rank5 = madd(q, extra)
    controls.append(expect_bad("RANK4_PROJECTOR", lambda:
        projector(q_rank5, 4, "RANK4_PROJECTOR")))
    q_other = madd(q, mscale(rho, -1), extra)
    projector(q_other, 4, "OTHER_PROJECTOR")
    other_traces = (trprod(q_other, rho), trprod(q_other, h))
    need(other_traces == (F(0), F(4)), "OTHER_PROJECTOR_TRACES")
    controls.append(expect_bad("COMMON_PROJECTOR", lambda:
        common_certificate(q, q_other, rho, h)))

    t, a, b = F(1, 2), F(3, 4), F(1, 4)
    bad_output = madd(mscale(rho, t ** 4),
                      mscale(h, t * t * b * b),
                      mscale(i16, a * a * b * b))
    controls.append(expect_bad("OUTPUT_ALPHA", lambda:
        need(outputs[F(1, 2)][0] == bad_output, "OUTPUT_ALPHA")))

    rotated_rho = u_phase(rho_parts, 0)
    rotated_q = u_phase((q, z16), 0)
    complex_projector(rotated_q, 4)
    need(pcj(ptranspose(rotated_rho), "YYYY") == rotated_rho,
         "ROTATED_INPUT_SPIN_FLIP")
    need(any(x for row in rotated_rho[1] for x in row),
         "COMPLEX_CONTROL_DISCRIMINATING_INPUT")
    positive = channel(rotated_rho, F(2, 3))
    negative = channel(rotated_rho, F(4, 3))
    need(negative == pcj(ptranspose(positive), "YYYY"),
         "NEGATIVE_BRANCH_FULL_TRANSPOSE")
    transported_q = pcj(ptranspose(rotated_q), "YYYY")
    complex_projector(transported_q, 4)
    need(ptrprod(rotated_q, negative) ==
         ptrprod(transported_q, positive), "PROJECTOR_TRANSPORT")
    correct_expectation = ptrprod(rotated_q, negative)
    omitted_transpose_q = pcj(rotated_q, "YYYY")
    wrong_expectation = ptrprod(omitted_transpose_q, positive)
    need(correct_expectation == (F(29, 81), F(0)),
         "COMPLEX_CONTROL_CORRECT_VALUE")
    need(wrong_expectation == (F(70, 243), F(0)),
         "COMPLEX_CONTROL_WRONG_VALUE")
    controls.append(expect_bad("FULL_TRANSPOSE", lambda:
        need(correct_expectation == wrong_expectation, "FULL_TRANSPOSE")))

    need(len(controls) == 14, "CONTROL_COUNT")
    pulse()
    return {
        "status": "PASS_FINITE_ONLY",
        "elapsed_seconds": monotonic() - started,
        "input_cases": case_results,
        "proper_marginals_per_source_input": 14,
        "magic_generator_count": 6,
        "normal_form_conversion_cases": 2,
        "gram_count": gram_count,
        "gram_principal_minors_checked": 7 * gram_count,
        "gram_charpoly_histogram": histogram,
        "prefix_coefficient_table": tuple(coefficient_table),
        "sharp_common_projector_traces": (trprod(q, rho), trprod(q, h)),
        "sharp_projector_rank": rank(q),
        "sharp_H3_rank": rank(h),
        "different_projector_traces": other_traces,
        "complex_transport_correct": correct_expectation,
        "complex_transport_omitted_transpose": wrong_expectation,
        "intended_reason_rejections": tuple(controls),
        "universal_SO4_surjectivity_proved_by_execution": False,
        "mixed_invariant_theorem_proved_by_samples": False,
        "unrestricted_four_qubit_claim": False,
    }

if __name__ == "__main__":
    RESULT = finite_audit()
