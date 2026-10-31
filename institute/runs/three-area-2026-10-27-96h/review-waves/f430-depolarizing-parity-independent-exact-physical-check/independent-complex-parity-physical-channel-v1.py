from fractions import Fraction as F
from math import sqrt, copysign
from time import monotonic
import sys

START = monotonic()
DEADLINE = START + 54.0
TOL = 2e-9


class CheckError(Exception):
    pass


class GuardExpired(Exception):
    pass


def guard():
    if monotonic() >= DEADLINE:
        raise GuardExpired()


def need(condition, reason):
    if not condition:
        raise CheckError(reason)


class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        if isinstance(r, G):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = F(r), F(i)

    def __bool__(self):
        return bool(self.r or self.i)

    def __eq__(self, other):
        if not isinstance(other, (G, int, F)):
            return False
        other = z(other)
        return self.r == other.r and self.i == other.i

    def __add__(self, other):
        other = z(other)
        return G(self.r + other.r, self.i + other.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-z(other))

    def __rsub__(self, other):
        return z(other) - self

    def __mul__(self, other):
        other = z(other)
        return G(
            self.r * other.r - self.i * other.i,
            self.r * other.i + self.i * other.r,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = z(other)
        den = other.r * other.r + other.i * other.i
        if den == 0:
            raise ZeroDivisionError("Gaussian-rational division by zero")
        return G(
            (self.r * other.r + self.i * other.i) / den,
            (self.i * other.r - self.r * other.i) / den,
        )

    def __rtruediv__(self, other):
        return z(other) / self

    def conj(self):
        return G(self.r, -self.i)


def z(value):
    return value if isinstance(value, G) else G(value)


ZERO = G(0)
ONE = G(1)
II = G(0, 1)


def zeros(n):
    return [[ZERO for _ in range(n)] for _ in range(n)]


def eye(n):
    out = zeros(n)
    for i in range(n):
        out[i][i] = ONE
    return out


def trace(a):
    return sum((a[i][i] for i in range(len(a))), ZERO)


def transpose(a):
    return [list(row) for row in zip(*a)]


def adj(a):
    return [[a[j][i].conj() for j in range(len(a))]
            for i in range(len(a))]


def scale(a, weight):
    weight = z(weight)
    out = []
    for row in a:
        guard()
        out.append([weight * value for value in row])
    return out


def add(a, b):
    return [[x + y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def sub(a, b):
    return add(a, scale(b, -1))


def lin(terms):
    need(bool(terms), "EMPTY_LINEAR_COMBINATION")
    n = len(terms[0][1])
    out = zeros(n)
    for weight, a in terms:
        guard()
        need(len(a) == n and all(len(row) == n for row in a),
             "LINEAR_COMBINATION_DIMENSION")
        weight = z(weight)
        for i in range(n):
            guard()
            for j, value in enumerate(a[i]):
                if value:
                    out[i][j] = out[i][j] + weight * value
    return out


def mixture(terms):
    need(all(F(weight) >= 0 for weight, _ in terms),
         "NEGATIVE_ENSEMBLE_WEIGHT")
    need(sum((F(weight) for weight, _ in terms), F(0)) == 1,
         "ENSEMBLE_WEIGHT_SUM")
    return lin(terms)


def mm(a, b):
    n = len(a)
    need(len(b) == n, "MATRIX_PRODUCT_DIMENSION")
    out = zeros(n)
    for i in range(n):
        guard()
        for k, x in enumerate(a[i]):
            if not x:
                continue
            for j, y in enumerate(b[k]):
                if y:
                    out[i][j] = out[i][j] + x * y
    return out


def kron(a, b):
    na, nb = len(a), len(b)
    out = zeros(na * nb)
    for i in range(na):
        guard()
        for j, x in enumerate(a[i]):
            if not x:
                continue
            for k in range(nb):
                for ell, y in enumerate(b[k]):
                    if y:
                        out[i * nb + k][j * nb + ell] = x * y
    return out


def conjugate_by(u, a):
    return mm(mm(u, a), adj(u))


def pure(vector):
    vector = [z(value) for value in vector]
    norm = sum((v.r * v.r + v.i * v.i for v in vector), F(0))
    need(norm > 0, "ZERO_KET")
    return [[x * y.conj() / norm for y in vector] for x in vector]


def sparse_pure(n, entries):
    vector = [ZERO for _ in range(n)]
    for i, value in entries.items():
        vector[i] = z(value)
    return pure(vector)


def basis(n, index):
    return sparse_pure(n, {index: 1})


def support_projector(n, indices):
    out = zeros(n)
    for i in indices:
        out[i][i] = ONE
    return out


def projector(a, rank, reason="PROJECTOR"):
    need(a == adj(a), reason + "_HERMITIAN")
    need(mm(a, a) == a, reason + "_IDEMPOTENT")
    need(trace(a) == rank, reason + "_RANK")


def psd_exact(a, reason):
    need(a == adj(a), reason + "_HERMITIAN")
    work = [row[:] for row in a]
    n = len(work)
    for k in range(n):
        guard()
        pivot = work[k][k]
        need(pivot.i == 0 and pivot.r >= 0, reason + "_PIVOT")
        if pivot.r == 0:
            need(all(not work[k][j] for j in range(k + 1, n)),
                 reason + "_ZERO_PIVOT_ROW")
            continue
        for i in range(k + 1, n):
            guard()
            for j in range(i, n):
                value = (
                    work[i][j]
                    - work[i][k] * work[j][k].conj() / pivot
                )
                work[i][j] = value
                work[j][i] = value.conj()
        for i in range(k + 1, n):
            work[i][k] = ZERO
            work[k][i] = ZERO


def density(a, reason):
    need(trace(a) == 1, reason + "_TRACE")
    psd_exact(a, reason)


def expect(q, a):
    value = trace(mm(q, a))
    need(value.i == 0, "NONREAL_HERMITIAN_EXPECTATION")
    return value.r


def qubits(a):
    d = len(a)
    n = d.bit_length() - 1
    need((1 << n) == d and all(len(row) == d for row in a),
         "NON_QUBIT_DIMENSION")
    return n


def channel(a, s, off=None, diag=None):
    # Direct tensor expansion of physical one-qubit matrix units.
    n = qubits(a)
    d = len(a)
    off = F(s if off is None else off)
    diag = F(s if diag is None else diag)
    keep, flip = (1 + diag) / 2, (1 - diag) / 2
    out = zeros(d)
    for i in range(d):
        guard()
        for j, value in enumerate(a[i]):
            if not value:
                continue
            terms = [(0, 0, value)]
            for bit in range(n):
                guard()
                mask = 1 << (n - 1 - bit)
                ib, jb = i & mask, j & mask
                next_terms = []
                if ib != jb:
                    for u, v, weight in terms:
                        if off:
                            next_terms.append(
                                (u | ib, v | jb, weight * off)
                            )
                else:
                    for u, v, weight in terms:
                        if keep:
                            next_terms.append(
                                (u | ib, v | ib, weight * keep)
                            )
                        if flip:
                            next_terms.append(
                                (u | (ib ^ mask),
                                 v | (ib ^ mask), weight * flip)
                            )
                terms = next_terms
            for u, v, weight in terms:
                out[u][v] = out[u][v] + weight
    return out


def pauli_channel(a, s):
    # Separate physical Pauli-conjugation implementation.
    n = qubits(a)
    d = len(a)
    qi, q = (1 + 3 * s) / 4, (1 - s) / 4
    need(qi >= 0 and q >= 0, "NONPHYSICAL_PAULI_PARAMETER")
    work = a
    for bit in range(n):
        guard()
        mask = 1 << (n - 1 - bit)
        out = zeros(d)
        for i in range(d):
            guard()
            for j, value in enumerate(work[i]):
                if not value:
                    continue
                sign = -1 if bool(i & mask) != bool(j & mask) else 1
                out[i][j] = out[i][j] + qi * value
                out[i ^ mask][j ^ mask] = (
                    out[i ^ mask][j ^ mask] + q * value
                )
                out[i ^ mask][j ^ mask] = (
                    out[i ^ mask][j ^ mask] + q * sign * value
                )
                out[i][j] = out[i][j] + q * sign * value
        work = out
    return work


EVEN = [0, 3, 5, 6]
ODD = [7, 4, 2, 1]


def parity_pure(coefficients, odd):
    indices = ODD if odd else EVEN
    return sparse_pure(
        8, {indices[i]: value for i, value in enumerate(coefficients)}
    )


def block_prediction(coefficients, odd, s, conjugate_opposite=True):
    # Independent explicit diagonal/off-diagonal prediction.
    r = pure(coefficients)
    aa, bb = (1 + s) / 2, (1 - s) / 2
    same = ODD if odd else EVEN
    opposite = EVEN if odd else ODD
    out = zeros(8)
    for i in range(4):
        guard()
        for j in range(4):
            if i == j:
                out[same[i]][same[j]] = (
                    aa * bb * bb + aa * s * r[i][i]
                )
                out[opposite[i]][opposite[j]] = (
                    aa * aa * bb - bb * s * r[i][i]
                )
            else:
                out[same[i]][same[j]] = aa * s * s * r[i][j]
                value = r[i][j].conj() if conjugate_opposite else r[i][j]
                out[opposite[i]][opposite[j]] = bb * s * s * value
    return out


def reference(n, s):
    t = abs(s)
    aa, bb = (1 + t) / 2, (1 - t) / 2
    values = [F(1)]
    for _ in range(n):
        values = [value * aa for value in values] + [
            value * bb for value in values
        ]
    return sorted(values, reverse=True)


def exact_prefixes(values, ref, reason):
    need(len(values) == len(ref), reason + "_LENGTH")
    values, ref = sorted(values, reverse=True), sorted(ref, reverse=True)
    gaps = []
    total = F(0)
    for x, y in zip(values, ref):
        total += y - x
        need(total >= 0, reason + "_PREFIX")
        gaps.append(total)
    need(total == 0, reason + "_TRACE")
    return gaps


def resolution(a, terms, reason):
    n = len(a)
    need(lin([(1, p) for _, p, _ in terms]) == eye(n),
         reason + "_COMPLETE")
    values = []
    for i, (value, p, rank) in enumerate(terms):
        guard()
        projector(p, rank, reason + "_PROJECTOR")
        for _, previous, _ in terms[:i]:
            need(mm(p, previous) == zeros(n), reason + "_ORTHOGONAL")
        values.extend([F(value)] * rank)
    need(lin([(value, p) for value, p, _ in terms]) == a,
         reason + "_RECONSTRUCTION")
    return sorted(values, reverse=True)


def spin(a):
    y = [[ZERO, -II], [II, ZERO]]
    w = [[ONE]]
    for _ in range(qubits(a)):
        w = kron(w, y)
    return conjugate_by(w, a)


def partial_transpose(a, selected_bits):
    n, d = qubits(a), len(a)
    masks = [1 << (n - 1 - bit) for bit in selected_bits]
    out = zeros(d)
    for i in range(d):
        guard()
        for j in range(d):
            u, v = i, j
            for mask in masks:
                if bool(i & mask) != bool(j & mask):
                    u ^= mask
                    v ^= mask
            out[u][v] = a[i][j]
    return out


def permute(a, order):
    n, d = qubits(a), len(a)
    need(sorted(order) == list(range(n)), "INVALID_QUBIT_PERMUTATION")
    image = []
    for i in range(d):
        value = 0
        for position in order:
            value = (value << 1) | ((i >> (n - 1 - position)) & 1)
        image.append(value)
    out = zeros(d)
    for i in range(d):
        guard()
        for j in range(d):
            out[image[i]][image[j]] = a[i][j]
    return out


def numerical_spectrum(a):
    # Tolerance-based complex Hermitian Jacobi, not exact certification.
    n = len(a)
    h = [[complex(float(v.r), float(v.i)) for v in row] for row in a]
    converged = False
    for _ in range(80):
        guard()
        for p in range(n - 1):
            guard()
            for q in range(p + 1, n):
                x = h[p][q]
                magnitude = abs(x)
                if magnitude <= 1e-14:
                    continue
                app, aqq = h[p][p].real, h[q][q].real
                tau = (aqq - app) / (2.0 * magnitude)
                tangent = (
                    copysign(1.0, tau)
                    / (abs(tau) + sqrt(1.0 + tau * tau))
                )
                cosine = 1.0 / sqrt(1.0 + tangent * tangent)
                sine = tangent * cosine
                phase = x / magnitude
                for k in range(n):
                    if k == p or k == q:
                        continue
                    hp, hq = h[k][p], h[k][q]
                    vp = cosine * phase * hp - sine * hq
                    vq = sine * phase * hp + cosine * hq
                    h[k][p], h[p][k] = vp, vp.conjugate()
                    h[k][q], h[q][k] = vq, vq.conjugate()
                h[p][p] = complex(app - tangent * magnitude, 0.0)
                h[q][q] = complex(aqq + tangent * magnitude, 0.0)
                h[p][q] = h[q][p] = 0j
        residual = max(
            sum(abs(h[i][j]) for j in range(n) if j != i)
            for i in range(n)
        )
        if residual <= 1e-12:
            converged = True
            break
    need(converged, "JACOBI_NONCONVERGENCE")
    values = sorted((h[i][i].real for i in range(n)), reverse=True)
    need(min(values) >= -TOL, "NUMERICAL_NEGATIVE_EIGENVALUE")
    need(abs(sum(values) - float(trace(a).r)) <= TOL,
         "NUMERICAL_TRACE")
    return values, residual


def numerical_prefixes(a, ref):
    values, residual = numerical_spectrum(a)
    xsum, rsum = 0.0, 0.0
    gaps = []
    for x, r in zip(values, ref):
        xsum += x
        rsum += float(r)
        gap = rsum - xsum
        need(gap >= -TOL, "NUMERICAL_MAJOR_PREFIX")
        gaps.append(gap)
    need(abs(gaps[-1]) <= TOL, "NUMERICAL_MAJOR_TRACE")
    return gaps, residual


def intended_rejection(name, reason, callback):
    try:
        callback()
    except CheckError as error:
        need(str(error) == reason, "WRONG_MUTATION_REASON_" + name)
    else:
        raise CheckError("MUTATION_NOT_REJECTED_" + name)
    print("MUTATION_REJECTED", name, "reason=" + reason)


def exact_core():
    s = F(3, 4)
    w = sparse_pure(8, {4: 1, 2: II, 1: 1})
    eta = sparse_pure(8, {3: 1, 5: -II, 6: 1})
    p000, p111 = basis(8, 0), basis(8, 7)
    one_support = support_projector(8, [1, 2, 4])
    two_support = support_projector(8, [3, 5, 6])
    density(w, "EXACT_W_INPUT")
    x = channel(w, s)
    density(x, "EXACT_W_OUTPUT")
    need(x == pauli_channel(w, s), "EXACT_W_CHANNEL_ORACLE")
    terms = [
        (F(287, 512), w, 1),
        (F(35, 512), sub(one_support, w), 2),
        (F(7, 512), p111, 1),
        (F(57, 512), eta, 1),
        (F(21, 512), sub(two_support, eta), 2),
        (F(49, 512), p000, 1),
    ]
    values = resolution(x, terms, "EXACT_W_RESOLUTION")
    wanted = [F(v, 512) for v in [287, 57, 49, 35, 35, 21, 21, 7]]
    need(values == wanted, "EXACT_W_SPECTRUM")
    gaps = exact_prefixes(values, reference(3, s), "EXACT_W_MAJOR")
    need(gaps == [F(v, 512) for v in [56, 48, 48, 62, 34, 20, 6, 0]],
         "EXACT_W_GAPS")
    q = lin([(1, w), (1, eta), (1, p000)])
    projector(q, 3, "EXACT_Q3")
    need(any(v.i != 0 for row in q for v in row), "Q3_NOT_COMPLEX")
    need(expect(q, x) == F(393, 512), "EXACT_Q3_VALUE")

    p0, p1 = basis(2, 0), basis(2, 1)
    input4 = kron(p0, w)
    x4 = channel(input4, s)
    density(input4, "EXACT_SPECTATOR_INPUT")
    density(x4, "EXACT_SPECTATOR_OUTPUT")
    need(x4 == kron(channel(p0, s), x), "EXACT_SPECTATOR_FACTORIZATION")
    terms4 = [
        (factor * value, kron(p, projection), rank)
        for factor, p in [(F(7, 8), p0), (F(1, 8), p1)]
        for value, projection, rank in terms
    ]
    values4 = resolution(x4, terms4, "EXACT_SPECTATOR_RESOLUTION")
    wanted4 = [
        F(v, 4096) for v in
        [2009, 399, 343, 287, 245, 245, 147, 147,
         57, 49, 49, 35, 35, 21, 21, 7]
    ]
    need(values4 == wanted4, "EXACT_SPECTATOR_SPECTRUM")
    gaps4 = exact_prefixes(
        values4, reference(4, s), "EXACT_SPECTATOR_MAJOR"
    )
    need(
        gaps4 == [
            F(v, 4096) for v in
            [392, 336, 336, 392, 490, 294, 196, 98,
             90, 90, 90, 62, 34, 20, 6, 0]
        ],
        "EXACT_SPECTATOR_GAPS",
    )
    q4 = kron(p0, q)
    projector(q4, 3, "EXACT_Q4")
    need(expect(q4, x4) == F(2751, 4096), "EXACT_Q4_VALUE")
    print("EXACT_W3_SPECTRUM", " ".join(str(v) for v in values))
    print("EXACT_W3_PREFIX_GAPS", " ".join(str(v) for v in gaps))
    print("EXACT_Q3_VALUE", str(expect(q, x)))
    print("EXACT_W4_SPECTRUM", " ".join(str(v) for v in values4))
    print("EXACT_W4_PREFIX_GAPS", " ".join(str(v) for v in gaps4))
    print("EXACT_Q4_VALUE", str(expect(q4, x4)))
    return w, eta, x, q, q4


def build_three_qubit_cases():
    pure_specs = [
        ("basis_even", [1, 0, 0, 0], False),
        ("two_complex_zero_populations", [1, II, 0, 0], False),
        ("complex_W", [0, 1, II, 1], True),
        ("four_complex", [1, II, 1 + II, 2 - II], False),
        ("same_populations_other_phases",
         [II, 1, 1 - II, 2 + II], False),
        ("odd_four_complex", [1, 2 + II, -II, 1 - 2 * II], True),
    ]
    cases = []
    for name, coefficients, odd in pure_specs:
        components = [(F(1), coefficients, odd)]
        cases.append(
            (name, parity_pure(coefficients, odd), components)
        )
    mixed_terms = [
        (F(1, 2), pure_specs[2][1], True),
        (F(1, 3), pure_specs[3][1], False),
        (F(1, 6), pure_specs[0][1], False),
    ]
    same_parity_terms = [
        (F(2, 5), pure_specs[1][1], False),
        (F(3, 5), pure_specs[3][1], False),
    ]
    for name, terms in [
        ("mixed_both_parities", mixed_terms),
        ("mixed_same_parity", same_parity_terms),
    ]:
        state = mixture([
            (weight, parity_pure(coefficients, odd))
            for weight, coefficients, odd in terms
        ])
        cases.append((name, state, terms))
    return cases


def predict_three(components, s):
    return lin([
        (weight, block_prediction(coefficients, odd, s))
        for weight, coefficients, odd in components
    ])


def build_four_qubit_cases(cases3):
    p0 = basis(2, 0)
    plus_i = pure([1, II])
    sigma_mixed = mixture([(F(1, 2), p0), (F(1, 2), plus_i)])
    w = cases3[2][1]
    mixed_tau = cases3[6][1]
    all_complex = cases3[3][1]

    ux = [[G(F(3, 5)), G(0, F(4, 5))],
          [G(0, F(4, 5)), G(F(3, 5))]]
    uy = [[G(F(3, 5)), G(F(-4, 5))],
          [G(F(4, 5)), G(F(3, 5))]]
    uz = [[ONE, ZERO], [ZERO, II]]
    u = kron(kron(kron(ux, uy), uz), eye(2))
    need(mm(u, adj(u)) == eye(16), "PHYSICAL_LOCAL_UNITARY")
    order = [1, 2, 3, 0]

    state0 = kron(p0, w)
    state1 = kron(sigma_mixed, mixed_tau)
    state2 = permute(conjugate_by(u, kron(plus_i, all_complex)), order)

    def prediction0(s):
        return kron(channel(p0, s), channel(w, s))

    def prediction1(s):
        return kron(channel(sigma_mixed, s), channel(mixed_tau, s))

    def prediction2(s):
        return permute(
            conjugate_by(
                u, kron(channel(plus_i, s), channel(all_complex, s))
            ),
            order,
        )

    parts = [
        ("pure_spectator_W", state0, prediction0),
        ("mixed_spectator_mixed_parity", state1, prediction1),
        ("rotated_permuted_spectator", state2, prediction2),
    ]
    weights = [F(1, 3), F(2, 5), F(4, 15)]
    mixed_state = mixture([
        (weight, part[1]) for weight, part in zip(weights, parts)
    ])

    def mixed_prediction(s):
        return mixture([
            (weight, part[2](s))
            for weight, part in zip(weights, parts)
        ])

    cases = parts + [
        ("varying_spectator_local_basis_finite_hull",
         mixed_state, mixed_prediction)
    ]
    return cases, parts, weights


def phase_controls(cases3):
    s = F(3, 4)
    c = [1, II, 1 + II, 2 - II]
    d = [II, 1, 1 - II, 2 + II]
    a, b = cases3[3][1], cases3[4][1]
    xa, xb = channel(a, s), channel(b, s)
    u = zeros(8)
    for i in range(4):
        ratio = z(d[i]) / z(c[i])
        need(ratio * ratio.conj() == 1, "PHASE_RATIO_MODULUS")
        u[EVEN[i]][EVEN[i]] = ratio
        u[ODD[i]][ODD[i]] = ratio.conj()
    need(mm(u, adj(u)) == eye(8), "PHASE_TRANSPORT_UNITARY")
    need(xb == conjugate_by(u, xa), "PHASE_TRANSPORT_MATRIX")
    projector(a, 1, "SAME_PHASE_TEST_PROJECTOR")
    need(expect(a, xa) != expect(a, xb),
         "NONIDENTICAL_PHASE_FIXED_Q_NOT_DISTINGUISHED")
    print("PHASE_CONTROL_EXACT",
          "same populations and spectrum; fixed physical Q differs")


def mutation_controls(w, eta, x, q):
    s = F(3, 4)

    for name, off, diag, reason in [
        ("coherence_factor", s * s, s, "COHERENCE_FACTOR"),
        ("diagonal_factor", s, s * s, "DIAGONAL_FACTOR"),
    ]:
        # CPTP prerequisites for Bloch multipliers (off, off, diag).
        probabilities = [
            (1 + 2 * off + diag) / 4,
            (1 - diag) / 4,
            (1 - diag) / 4,
            (1 - 2 * off + diag) / 4,
        ]
        need(min(probabilities) >= 0 and sum(probabilities) == 1,
             "MUTANT_CHANNEL_NOT_CPTP_" + name)
        wrong = channel(w, s, off=off, diag=diag)
        density(wrong, "MUTANT_CHANNEL_OUTPUT_" + name)
        intended_rejection(
            name, reason,
            lambda wrong=wrong, reason=reason: need(wrong == x, reason),
        )

    wrong_block = block_prediction(
        [0, 1, II, 1], True, s, conjugate_opposite=False
    )
    density(wrong_block, "MUTANT_BLOCK_OUTPUT")
    need(expect(q, wrong_block) == F(361, 512),
         "MUTANT_BLOCK_WRITTEN_VALUE")
    intended_rejection(
        "complementary_block_conjugation",
        "COMPLEMENT_CONJUGATION",
        lambda: need(expect(q, wrong_block) == expect(q, x),
                     "COMPLEMENT_CONJUGATION"),
    )

    transposed = transpose(x)
    density(transposed, "FULL_TRANSPOSED_OUTPUT")
    need(expect(q, transposed) == F(137, 512),
         "TRANSPOSED_FIXED_Q_WRITTEN_VALUE")
    intended_rejection(
        "full_transpose_spectra_only",
        "SAME_Q_FULL_TRANSPOSE",
        lambda: need(expect(q, transposed) == expect(q, x),
                     "SAME_Q_FULL_TRANSPOSE"),
    )

    t = F(1, 4)
    positive, negative = channel(w, t), channel(w, -t)
    density(positive, "NEGATIVE_CONTROL_POSITIVE_OUTPUT")
    density(negative, "NEGATIVE_CONTROL_NEGATIVE_OUTPUT")
    need(negative == spin(transpose(positive)), "FULL_SPINFLIP_IDENTITY")
    qprime = spin(transpose(q))
    projector(qprime, 3, "TRANSPORTED_Q")
    need(expect(q, negative) == expect(qprime, positive),
         "CORRECT_NEGATIVE_Q_TRANSPORT")
    need(expect(q, negative) == F(197, 512),
         "NEGATIVE_FIXED_Q_WRITTEN_VALUE")
    need(expect(q, positive) == F(227, 512),
         "POSITIVE_FIXED_Q_WRITTEN_VALUE")

    partial_wrong = spin(partial_transpose(positive, [0]))
    density(partial_wrong, "PARTIAL_TRANSPOSE_MUTANT_OUTPUT")
    intended_rejection(
        "partial_instead_of_full_transpose",
        "PARTIAL_INSTEAD_OF_FULL_TRANSPOSE",
        lambda: need(expect(q, partial_wrong) == expect(q, negative),
                     "PARTIAL_INSTEAD_OF_FULL_TRANSPOSE"),
    )
    intended_rejection(
        "stale_negative_projector",
        "STALE_NEGATIVE_PROJECTOR",
        lambda: need(expect(q, negative) == expect(q, positive),
                     "STALE_NEGATIVE_PROJECTOR"),
    )

    missing_transpose_q = spin(q)
    projector(missing_transpose_q, 3, "MISSING_TRANSPOSE_Q")
    intended_rejection(
        "missing_projector_transpose",
        "MISSING_PROJECTOR_TRANSPOSE",
        lambda: need(
            expect(missing_transpose_q, positive) == expect(q, negative),
            "MISSING_PROJECTOR_TRANSPOSE",
        ),
    )

    product_output = channel(basis(8, 4), s)
    density(product_output, "BLOCK_PRODUCT_REFERENCE")
    need(all(
        not product_output[i][j]
        for i in EVEN for j in EVEN if i != j
    ), "PRODUCT_EVEN_BLOCK_NOT_DIAGONAL")
    block_reference_max = max(product_output[i][i].r for i in EVEN)
    need(block_reference_max == F(49, 512), "PRODUCT_EVEN_BLOCK_MAX")
    projector(eta, 1, "BLOCK_WITNESS_PROJECTOR")
    need(expect(eta, x) == F(57, 512), "ACTUAL_EVEN_BLOCK_WITNESS")
    intended_rejection(
        "independent_block_majorization",
        "INDEPENDENT_BLOCK_PREFIX1",
        lambda: need(expect(eta, x) <= block_reference_max,
                     "INDEPENDENT_BLOCK_PREFIX1"),
    )


def main():
    need(sys.argv[1:] == ["--run"], "ARGV_EXPECTED_--run")
    guard()
    w, eta, x, q3, q4 = exact_core()
    cases3 = build_three_qubit_cases()
    cases4, four_parts, four_weights = build_four_qubit_cases(cases3)
    phase_controls(cases3)

    parameters = [
        F(0), F(1, 4), F(1, 2), F(2, 3),
        F(7, 8), F(1), F(5, 4), F(4, 3),
    ]
    grouped3 = [
        (name, state,
         lambda s, components=components: predict_three(components, s))
        for name, state, components in cases3
    ]
    case_count, prefix_count = 0, 0
    worst_excess = 0.0
    worst_residual = 0.0

    for n, cases, q in [(3, grouped3, q3), (4, cases4, q4)]:
        for name, state, prediction in cases:
            guard()
            density(state, "INPUT_" + name)
            need(qubits(state) == n, "INPUT_QUBIT_COUNT")
            for p in parameters:
                guard()
                s = 1 - p
                actual = channel(state, s)
                density(actual, "OUTPUT_" + name)
                need(actual == pauli_channel(state, s),
                     "MATRIX_UNIT_PAULI_AGREEMENT")
                need(actual == prediction(s),
                     "BLOCK_OR_TENSOR_COVARIANCE_PREDICTION")
                ref = reference(n, s)
                need(expect(q, actual) <= sum(ref[:3], F(0)),
                     "SAME_PHYSICAL_RANK3_BOUND")
                if s < 0:
                    positive = channel(state, -s)
                    need(actual == spin(transpose(positive)),
                         "NEGATIVE_FULL_TRANSPOSE")
                    qprime = spin(transpose(q))
                    projector(qprime, 3, "NEGATIVE_TRANSPORTED_PROJECTOR")
                    need(expect(q, actual) == expect(qprime, positive),
                         "NEGATIVE_SAME_OBSERVABLE_TRANSPORT")
                gaps, residual = numerical_prefixes(actual, ref)
                case_count += 1
                prefix_count += len(actual)
                worst_excess = max(worst_excess, max(-g for g in gaps))
                worst_residual = max(worst_residual, residual)
                print(
                    "NUMERICAL_ALL_PREFIXES",
                    "n=" + str(n), "case=" + name, "p=" + str(p),
                    "gaps=" + ",".join(format(g, ".12g") for g in gaps),
                    "jacobi_residual=" + format(residual, ".6g"),
                )

    for p in parameters:
        guard()
        s = 1 - p
        mixture_output = channel(cases4[-1][1], s)
        component_outputs = [
            channel(part[1], s) for part in four_parts
        ]
        recombined = mixture([
            (weight, output)
            for weight, output in zip(four_weights, component_outputs)
        ])
        need(mixture_output == recombined, "FINITE_HULL_LINEARITY")
        same_q_sum = sum(
            (weight * expect(q4, output)
             for weight, output in zip(four_weights, component_outputs)),
            F(0),
        )
        need(expect(q4, mixture_output) == same_q_sum,
             "FINITE_HULL_SAME_PHYSICAL_Q")
        need(same_q_sum <= sum(reference(4, s)[:3], F(0)),
             "FINITE_HULL_RANK3_BOUND")

    mutation_controls(w, eta, x, q3)
    need(case_count == 96, "CASE_COVERAGE_COUNT")
    need(prefix_count == 1024, "PREFIX_COVERAGE_COUNT")
    guard()
    elapsed = monotonic() - START
    need(elapsed < 55.0, "ELAPSED_LIMIT")
    print("SUMMARY", "cases=" + str(case_count),
          "numerical_prefixes=" + str(prefix_count),
          "intended_mutations=8",
          "tolerance=" + str(TOL),
          "worst_numerical_excess=" + format(worst_excess, ".12g"),
          "worst_jacobi_residual=" + format(worst_residual, ".12g"),
          "elapsed_seconds=" + format(elapsed, ".6f"))
    print("RESULT PASS COMPLETE_FINITE_CHECK_NOT_UNIVERSAL_PROOF")
    return 0


if __name__ == "__main__":
    try:
        status = main()
    except GuardExpired:
        print("RESULT INCOMPLETE_TIME_GUARD NO_PASS")
        status = 2
    except CheckError as error:
        print("RESULT FAIL reason=" + str(error))
        status = 1
    raise SystemExit(status)
