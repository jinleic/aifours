#!/usr/bin/env python3
"""Independent finite diagnostic for the frozen f345 four-qubit sector claim.

Only dependency: already-installed NumPy.
No network, subprocesses, scientific-input imports, writes, retries or asserts.
PASS_FINITE_DIAGNOSTIC is not a proof of any universal quantifier.
"""

import os

for _key in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_key] = "1"

import datetime
import hashlib
import itertools
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
import traceback

START = time.monotonic()
BUDGET_SECONDS = 55.0
ATOL = 2.0e-10
RTOL = 2.0e-10
ITOL = 5.0e-10
STRICT_MARGIN = 1.0e-8
CONTROL_MIN_GAP = 1.0e-5
SEED = 20261030
P_VALUES = (
    0.0,
    1.0 / 16.0,
    1.0 / 4.0,
    1.0 / 2.0,
    2.0 / 3.0,
    7.0 / 8.0,
    141.0 / 142.0,
    1.0,
    143.0 / 142.0,
    9.0 / 8.0,
    5.0 / 4.0,
    4.0 / 3.0,
)
CURRENT = "startup"
METRICS = {
    "successful_checks": 0,
    "successful_equalities": 0,
    "successful_inequalities": 0,
    "expected_control_rejections": 0,
    "channel_cases": 0,
    "max_successful_equality_residual": 0.0,
    "minimum_raw_inequality_slack": None,
}
np = None


class CheckError(Exception):
    def __init__(self, check, detail):
        super().__init__(detail)
        self.check = check
        self.detail = detail
        self.context = CURRENT


class BudgetExceeded(Exception):
    pass


def emit(kind, **fields):
    print(
        json.dumps(
            {"kind": kind, **fields},
            sort_keys=True,
            allow_nan=False,
            separators=(",", ":"),
        ),
        flush=True,
    )


def tick():
    if time.monotonic() - START >= BUDGET_SECONDS:
        raise BudgetExceeded("cooperative elapsed-time budget reached")


def alarm_handler(signum, frame):
    raise BudgetExceeded("cooperative alarm or termination signal: %d" % signum)


def fail(check, detail):
    raise CheckError(check, detail)


def finite(check, value):
    tick()
    if not bool(np.all(np.isfinite(np.asarray(value)))):
        fail(check, "nonfinite numerical value")
    METRICS["successful_checks"] += 1


def maxabs(value):
    a = np.asarray(value)
    return float(np.max(np.abs(a))) if a.size else 0.0


def near(check, actual, expected):
    tick()
    a = np.asarray(actual)
    b = np.asarray(expected)
    if a.shape != b.shape:
        fail(check + ".shape", "%r != %r" % (a.shape, b.shape))
    finite(check + ".actual_finite", a)
    finite(check + ".expected_finite", b)
    residual = maxabs(a - b)
    tolerance = ATOL + RTOL * max(maxabs(a), maxabs(b))
    if residual > tolerance:
        fail(
            check,
            "residual %.17g exceeds tolerance %.17g"
            % (residual, tolerance),
        )
    METRICS["successful_checks"] += 1
    METRICS["successful_equalities"] += 1
    METRICS["max_successful_equality_residual"] = max(
        METRICS["max_successful_equality_residual"], residual
    )
    return residual


def ge(check, left, right):
    tick()
    finite(check + ".left_finite", left)
    finite(check + ".right_finite", right)
    left = float(left)
    right = float(right)
    slack = left - right
    tolerance = ITOL * (1.0 + max(abs(left), abs(right)))
    if slack < -tolerance:
        fail(
            check,
            "slack %.17g below allowed -%.17g" % (slack, tolerance),
        )
    old = METRICS["minimum_raw_inequality_slack"]
    METRICS["minimum_raw_inequality_slack"] = (
        slack if old is None else min(old, slack)
    )
    METRICS["successful_checks"] += 1
    METRICS["successful_inequalities"] += 1
    return slack


def strict_gt(check, value, lower):
    finite(check + ".finite", value)
    if float(value) <= float(lower) + STRICT_MARGIN:
        fail(
            check,
            "%.17g is not above %.17g by %.17g"
            % (value, lower, STRICT_MARGIN),
        )
    METRICS["successful_checks"] += 1


def real_scalar(check, value):
    finite(check + ".finite", value)
    near(check + ".imaginary", float(np.imag(value)), 0.0)
    return float(np.real(value))


def sqrt_checked(check, value):
    ge(check + ".radicand", value, 0.0)
    # Clamp only after the explicit nonnegative-with-tolerance prerequisite.
    return math.sqrt(max(0.0, float(value)))


def observe(check, projector, matrix):
    return real_scalar(check, np.trace(projector @ matrix))


def kron_all(values):
    result = 1.0 + 0.0j
    for value in values:
        result = np.kron(result, value)
    return result


def unit(vector):
    vector = np.asarray(vector, dtype=np.complex128)
    finite("fixture.raw_vector", vector)
    length = float(np.linalg.norm(vector))
    if not math.isfinite(length) or length <= 0.0:
        fail("fixture.nonzero_norm", "cannot normalize fixture")
    return vector / length


def outer(vector):
    return np.outer(vector, vector.conj())


def spinflip(matrix):
    return W @ matrix.T @ W


def hermitian_spectrum(check, matrix, vectors=False):
    finite(check + ".matrix_finite", matrix)
    near(check + ".hermitian", matrix, matrix.conj().T)
    if vectors:
        values, basis = np.linalg.eigh(matrix)
        finite(check + ".vectors_finite", basis)
        near(check + ".basis_unitary", basis.conj().T @ basis, I16)
        near(
            check + ".eigen_reconstruction",
            (basis * values[None, :]) @ basis.conj().T,
            matrix,
        )
        finite(check + ".eigenvalues_finite", values)
        return values, basis
    values = np.linalg.eigvalsh(matrix)
    finite(check + ".eigenvalues_finite", values)
    return values


def density(check, matrix):
    finite(check + ".finite", matrix)
    near(check + ".hermitian", matrix, matrix.conj().T)
    near(check + ".trace", np.trace(matrix), 1.0 + 0.0j)
    values = np.linalg.eigvalsh(matrix)
    finite(check + ".spectrum_finite", values)
    ge(check + ".psd", float(values[0]), 0.0)
    ge(check + ".largest_eigenvalue", 1.0, float(values[-1]))
    near(check + ".spectral_trace", float(np.sum(values)), 1.0)
    ge(check + ".frobenius_norm", 1.0, float(np.linalg.norm(matrix)))
    return values


def projector_check(check, projector):
    finite(check + ".finite", projector)
    near(check + ".hermitian", projector, projector.conj().T)
    near(check + ".idempotent", projector @ projector, projector)
    near(check + ".trace", np.trace(projector), 3.0 + 0.0j)
    near(check + ".norm", float(np.linalg.norm(projector)), math.sqrt(3.0))
    values = np.linalg.eigvalsh(projector)
    near(
        check + ".rank_three_spectrum",
        values,
        np.concatenate((np.zeros(13), np.ones(3))),
    )


def top3(check, matrix):
    values = hermitian_spectrum(check, matrix)
    return float(np.sum(values[-3:]))


def partial_trace(matrix, keep):
    keep = tuple(keep)
    if keep != tuple(sorted(set(keep))):
        fail("partial_trace.keep_order", "keep must be sorted and unique")
    tensor = matrix.reshape((2,) * 8)
    remaining = 4
    for site in range(3, -1, -1):
        if site not in keep:
            tensor = np.trace(
                tensor, axis1=site, axis2=site + remaining
            )
            remaining -= 1
    dimension = 1 << len(keep)
    return tensor.reshape(dimension, dimension)


def replace_one_site(matrix, site):
    # Explicitly move this site's row/column indices to the front.
    # This implementation does not call partial_trace or use Pauli layers.
    other = [j for j in range(4) if j != site]
    order = [site, site + 4] + other + [j + 4 for j in other]
    blocks = (
        matrix.reshape((2,) * 8)
        .transpose(order)
        .reshape(2, 2, 8, 8)
    )
    reduced = blocks[0, 0] + blocks[1, 1]
    replacement = (
        0.5
        * np.eye(2, dtype=np.complex128)[:, :, None, None]
        * reduced[None, None, :, :]
    )
    return (
        replacement.reshape((2,) * 8)
        .transpose(np.argsort(order))
        .reshape(16, 16)
    )


def replacement_channel(matrix, p):
    result = matrix.copy()
    for site in range(4):
        result = (
            (1.0 - p) * result
            + p * replace_one_site(result, site)
        )
    return result


def kraus_channel(matrix, p):
    q = 1.0 - p
    probabilities = np.array(
        [(1.0 + 3.0 * q) / 4.0] + [(1.0 - q) / 4.0] * 3,
        dtype=float,
    )
    near("kraus.probability_sum", float(np.sum(probabilities)), 1.0)
    ge("kraus.physical_probabilities", float(np.min(probabilities)), 0.0)
    result = matrix.copy()
    for site in range(4):
        updated = np.zeros((16, 16), dtype=np.complex128)
        for probability, operator in zip(probabilities, ON_SITE[site]):
            updated += probability * (operator @ result @ operator.conj().T)
        result = updated
    return result


def pauli_layers(matrix):
    # Direct traces against independently constructed tensor Pauli matrices.
    raw = np.einsum("kij,ji->k", PAULIS, matrix, optimize=False)
    near("pauli.coefficients_real", raw.imag, np.zeros(256))
    coefficients = raw.real
    layers = np.stack(
        [
            np.einsum(
                "k,kij->ij",
                coefficients[WEIGHTS == weight],
                PAULIS[WEIGHTS == weight],
                optimize=False,
            )
            for weight in range(5)
        ]
    )
    lengths = np.array(
        [
            np.sum(coefficients[WEIGHTS == weight] ** 2)
            for weight in range(5)
        ],
        dtype=float,
    )
    near("pauli.identity_coefficient", float(coefficients[0]), 1.0)
    near("pauli.reconstruction", np.sum(layers, axis=0) / 16.0, matrix)
    near("pauli.C0", layers[0], I16)
    gram = np.einsum("wij,vji->wv", layers, layers, optimize=False)
    near("pauli.layer_gram", gram, np.diag(16.0 * lengths))
    for weight in range(1, 5):
        near(
            "pauli.layer_traceless",
            np.trace(layers[weight]),
            0.0 + 0.0j,
        )
    reflected = sum(
        ((-1) ** weight) * layers[weight] for weight in range(5)
    ) / 16.0
    near("pauli.spinflip_parity", spinflip(matrix), reflected)
    return layers, lengths, coefficients


def pauli_channel(layers, q):
    return sum((q ** weight) * layers[weight] for weight in range(5)) / 16.0


def marginal_checks(matrix, coefficients, pure):
    marginals = {}
    spectra = {}
    for size in (1, 2, 3):
        for keep in itertools.combinations(range(4), size):
            tick()
            marginal = partial_trace(matrix, keep)
            values = density("marginal." + str(keep), marginal)
            marginals[keep] = marginal
            spectra[keep] = values
            supported = np.ones(256, dtype=bool)
            for site in range(4):
                if site not in keep:
                    supported &= CODES[:, site] == 0
            expected_purity = float(
                np.sum(coefficients[supported] ** 2) / (2 ** size)
            )
            near(
                "marginal.pauli_purity",
                real_scalar("marginal.purity_real", np.trace(marginal @ marginal)),
                expected_purity,
            )
    if pure:
        for keep, values in spectra.items():
            complement = tuple(site for site in range(4) if site not in keep)
            other = spectra[complement]
            padded = np.pad(values, (8 - len(values), 0))
            other_padded = np.pad(other, (8 - len(other), 0))
            near("marginal.complementary_spectra", padded, other_padded)

    radii = []
    local_spectra = []
    for site in range(4):
        marginal = marginals[(site,)]
        values = spectra[(site,)]
        bloch = np.array(
            [
                real_scalar("marginal.bloch_real", np.trace(marginal @ sigma))
                for sigma in SINGLE_PAULIS[1:]
            ]
        )
        radius = float(np.linalg.norm(bloch))
        near("marginal.radius_from_spectrum", radius, float(values[1] - values[0]))
        ge("marginal.radius_nonnegative", radius, 0.0)
        ge("marginal.radius_at_most_one", 1.0, radius)
        radii.append(radius)
        local_spectra.append(values.tolist())
    return np.array(radii, dtype=float), local_spectra


def rotation(theta, phi):
    cosine = math.cos(theta)
    sine = math.sin(theta)
    return np.array(
        [
            [cosine, -np.exp(-1.0j * phi) * sine],
            [np.exp(1.0j * phi) * sine, cosine],
        ],
        dtype=np.complex128,
    )


def ghz(u, phase):
    result = np.zeros(16, dtype=np.complex128)
    result[0] = math.sqrt(u)
    result[15] = np.exp(1.0j * phase) * math.sqrt(1.0 - u)
    return result


def pair_state(u, phase):
    return np.array(
        [
            math.sqrt(u),
            0.0,
            0.0,
            np.exp(1.0j * phase) * math.sqrt(1.0 - u),
        ],
        dtype=np.complex128,
    )


def make_fixtures():
    local_unitary = kron_all(
        [
            rotation(0.19, 0.23),
            rotation(0.31, 0.61),
            rotation(0.47, 1.17),
            rotation(0.59, 1.43),
        ]
    )
    near("fixture.local_unitary", local_unitary.conj().T @ local_unitary, I16)
    fixtures = []

    def add(
        name,
        vector,
        declared_sector=False,
        expected_s=None,
        expected_tau=None,
        product=False,
        outside=False,
    ):
        fixtures.append(
            {
                "name": name,
                "psi": np.asarray(vector, dtype=np.complex128),
                "declared_sector": bool(declared_sector),
                "expected_s": expected_s,
                "expected_tau": expected_tau,
                "product": bool(product),
                "outside": bool(outside),
            }
        )

    add(
        "product-zero",
        E16[:, 0],
        expected_s=4.0,
        expected_tau=0.0,
        product=True,
    )
    factors = [
        unit([1.0, 1.0 + 2.0j]),
        unit([2.0 - 1.0j, 3.0]),
        unit([1.0j, 2.0]),
        unit([2.0, 1.0 - 1.0j]),
    ]
    add(
        "product-complex",
        kron_all(factors),
        expected_s=4.0,
        expected_tau=0.0,
        product=True,
    )

    ghz_parameters = (
        ("ghz-zero", 0.5, 0.37, True, False),
        ("ghz-low-boundary", 3.0 / 8.0, 0.53, True, False),
        ("ghz-high-boundary", 5.0 / 8.0, 1.11, True, False),
        (
            "ghz-just-inside",
            3.0 / 8.0 + 1.0 / 4096.0,
            0.79,
            True,
            False,
        ),
        (
            "ghz-just-outside",
            3.0 / 8.0 - 1.0 / 4096.0,
            0.91,
            False,
            True,
        ),
    )
    for name, u, phase, declared, outside in ghz_parameters:
        add(
            name,
            ghz(u, phase),
            declared_sector=declared,
            expected_s=4.0 * (2.0 * u - 1.0) ** 2,
            expected_tau=4.0 * u * (1.0 - u),
            outside=outside,
        )
    add(
        "rotated-ghz-boundary",
        local_unitary @ ghz(3.0 / 8.0, 1.37),
        declared_sector=True,
        expected_s=0.25,
        expected_tau=15.0 / 16.0,
    )

    # Unequal local radii: (a,a,b,b), 2*a^2 + 2*b^2 = 1/4.
    a = 0.3
    b = math.sqrt(0.035)
    pair_boundary = kron_all(
        [
            pair_state((1.0 + a) / 2.0, 0.43),
            pair_state((1.0 + b) / 2.0, 1.29),
        ]
    )
    add(
        "rotated-pair-boundary",
        local_unitary @ pair_boundary,
        declared_sector=True,
        expected_s=0.25,
        expected_tau=(1.0 - a * a) * (1.0 - b * b),
    )
    add(
        "rotated-two-bells-zero",
        local_unitary
        @ kron_all([pair_state(0.5, 0.67), pair_state(0.5, 1.03)]),
        declared_sector=True,
        expected_s=0.0,
        expected_tau=1.0,
    )

    cluster = np.empty(16, dtype=np.complex128)
    for index in range(16):
        bits = [(index >> (3 - site)) & 1 for site in range(4)]
        edge_parity = (
            bits[0] * bits[1] + bits[1] * bits[2] + bits[2] * bits[3]
        )
        phase = sum(
            theta * bit
            for theta, bit in zip((0.17, 0.41, 0.83, 1.19), bits)
        )
        cluster[index] = ((-1) ** edge_parity) * np.exp(1.0j * phase) / 4.0
    add(
        "rotated-cluster-zero",
        local_unitary @ cluster,
        declared_sector=True,
        expected_s=0.0,
    )

    e4 = np.eye(4, dtype=np.complex128)
    bells = (
        (e4[:, 0] + e4[:, 3]) / math.sqrt(2.0),
        (e4[:, 0] - e4[:, 3]) / math.sqrt(2.0),
        (e4[:, 1] + e4[:, 2]) / math.sqrt(2.0),
        (e4[:, 1] - e4[:, 2]) / math.sqrt(2.0),
    )
    z = unit([1.0, 2.0j, -1.0 + 0.5j, 0.3 - 0.7j])
    correlated = sum(
        coefficient * np.kron(bell, bell)
        for coefficient, bell in zip(z, bells)
    )
    add(
        "rotated-bell-correlated-zero",
        local_unitary @ correlated,
        declared_sector=True,
        expected_s=0.0,
        expected_tau=float(abs(np.sum(z * z)) ** 2),
    )

    w_state = (
        E16[:, 1]
        + 1.0j * E16[:, 2]
        - E16[:, 4]
        + np.exp(1.0j * math.pi / 5.0) * E16[:, 8]
    ) / 2.0
    add(
        "phased-W",
        w_state,
        expected_s=1.0,
        expected_tau=0.0,
    )

    rng = np.random.Generator(np.random.PCG64(SEED))
    for index in range(4):
        vector = unit(rng.normal(size=16) + 1.0j * rng.normal(size=16))
        add("generic-complex-%d" % index, vector)

    if len(fixtures) != 17:
        fail("fixture.primary_count", "expected exactly 17 primary pure fixtures")
    return fixtures


def complex_pairs(vector):
    return [[float(z.real), float(z.imag)] for z in vector]


def pure_profile(item):
    psi = item["psi"]
    near("pure.vector_norm", float(np.linalg.norm(psi)), 1.0)
    rho = outer(psi)
    density("pure.input", rho)
    near("pure.input_purity", np.trace(rho @ rho), 1.0 + 0.0j)
    layers, lengths, coefficients = pauli_layers(rho)
    radii, local_spectra = marginal_checks(rho, coefficients, pure=True)
    ordered = np.sort(radii)[::-1]
    s = float(np.sum(radii ** 2))
    L = float(3.0 * ordered[0] + 3.0 * ordered[1] + ordered[2] + ordered[3])
    flipped = spinflip(rho)
    density("pure.spinflip", flipped)
    near("pure.spinflip_involution", spinflip(flipped), rho)

    raw_tau = float(abs(np.vdot(psi, W @ psi.conj())) ** 2)
    ge("pure.tau_nonnegative", raw_tau, 0.0)
    ge("pure.tau_at_most_one", 1.0, raw_tau)
    near(
        "pure.tau_density_overlap",
        raw_tau,
        real_scalar("pure.overlap_real", np.trace(rho @ flipped)),
    )
    # Endpoint clipping follows, and does not replace, the checked prerequisites.
    tau = min(1.0, max(0.0, raw_tau))

    near("pure.A1_equals_s", float(lengths[1]), s)
    near("pure.total_pauli_length", float(np.sum(lengths)), 16.0)
    near("pure.A3_identity", float(lengths[3]), 12.0 + s - 2.0 * lengths[2])
    near("pure.A4_identity", float(lengths[4]), 3.0 - 2.0 * s + lengths[2])
    near(
        "pure.complementary_purity_sum",
        (4.0 + 3.0 * s + 2.0 * lengths[2] + lengths[3]) / 8.0,
        2.0 + s / 2.0,
    )
    near("pure.A2_spinflip_identity", float(lengths[2]), s + 2.0 + 4.0 * tau)
    near(
        "pure.spinflip_alternating_length",
        tau,
        float(sum(((-1) ** j) * lengths[j] for j in range(5)) / 16.0),
    )
    near("pure.C1_top3", top3("pure.C1", layers[1]), L)
    ge("pure.L_cauchy_bound", math.sqrt(20.0 * s), L)

    c = math.sqrt(39.0 * (s + 2.0 + 4.0 * tau))
    near("pure.c_from_measured_A2", c * c, 39.0 * float(lengths[2]))
    ge("pure.C2_top3_bound", c, top3("pure.C2", layers[2]))
    kappa = 14.0 - L + 4.0 * tau - c
    near(
        "pure.monotonicity_polynomial_identity",
        c * c - (6.0 + 8.0 * tau) ** 2,
        39.0 * s + 42.0 + 60.0 * tau - 64.0 * tau * tau,
    )
    ge("pure.monotonicity_polynomial_bound", c * c - (6.0 + 8.0 * tau) ** 2, 38.0)
    strict_gt("pure.c_minus_6_gt_8tau", c - 6.0, 8.0 * tau)

    if item["expected_s"] is not None:
        near("fixture.expected_s", s, item["expected_s"])
    if item["expected_tau"] is not None:
        near("fixture.expected_tau", tau, item["expected_tau"])
    if item["outside"]:
        strict_gt("fixture.just_outside_sector", s, 0.25)
    if item["declared_sector"]:
        ge("fixture.declared_sector_membership", 0.25, s)

    # Additional numerically qualifying generic samples may exercise the bound,
    # but they are not used as construction-certified mixture components.
    sector = bool(item["declared_sector"] or s <= 0.25 - STRICT_MARGIN)
    if sector:
        ge("sector.L_bound", math.sqrt(5.0), L)
        ge("sector.c_squared_bound", 351.0 / 4.0 + 156.0 * tau, c * c)
        polynomial = (
            (93.0 / 8.0 + 4.0 * tau) ** 2
            - (351.0 / 4.0 + 156.0 * tau)
        )
        near(
            "sector.polynomial_identity",
            polynomial,
            3033.0 / 64.0 - 63.0 * tau + 16.0 * tau * tau,
        )
        ge("sector.polynomial_margin", polynomial, 25.0 / 64.0)
        strict_gt("sector.c_upper_margin", 93.0 / 8.0 + 4.0 * tau, c)
        strict_gt("sector.kappa_gt_one_eighth", kappa, 1.0 / 8.0)

    zero_s_family = item["expected_s"] == 0.0
    if zero_s_family:
        near(
            "zero_sector.explicit_kappa",
            kappa,
            14.0 + 4.0 * tau - math.sqrt(78.0 + 156.0 * tau),
        )
        ge("zero_sector.stronger_certificate", kappa, 18.0 - math.sqrt(234.0))

    emit(
        "PURE_PROFILE",
        name=item["name"],
        vector=complex_pairs(psi),
        input_sha256=hashlib.sha256(psi.astype("<c16").tobytes()).hexdigest(),
        radii=radii.tolist(),
        local_spectra=local_spectra,
        s=s,
        L=L,
        tau=tau,
        A=lengths.tolist(),
        c=c,
        kappa=kappa,
        declared_sector=item["declared_sector"],
        finite_numeric_sector=sector,
        expected_s=item["expected_s"],
        expected_tau=item["expected_tau"],
        product=item["product"],
    )
    return {
        **item,
        "rho": rho,
        "layers": layers,
        "coefficients": coefficients,
        "s": s,
        "L": L,
        "tau": tau,
        "c": c,
        "kappa": kappa,
        "sector": sector,
    }


def common_channel_checks(name, rho, layers, p):
    q = 1.0 - p
    t = abs(q)
    ge("channel.p_lower", p, 0.0)
    ge("channel.p_upper", 4.0 / 3.0, p)
    actual = replacement_channel(rho, p)
    density("channel.actual_output", actual)
    near("channel.replacement_vs_kraus", actual, kraus_channel(rho, p))
    near("channel.measured_pauli_weight_scaling", actual, pauli_channel(layers, q))

    plus = replacement_channel(rho, 1.0 - t)
    density("channel.positive_branch_output", plus)
    near("channel.positive_branch_weight_scaling", plus, pauli_channel(layers, t))

    values, basis = hermitian_spectrum("channel.actual", actual, vectors=True)
    plus_values, plus_basis = hermitian_spectrum("channel.positive", plus, vectors=True)
    k3 = float(np.sum(values[-3:]))
    kp = float(np.sum(plus_values[-3:]))
    qmax = basis[:, -3:] @ basis[:, -3:].conj().T
    qplus = plus_basis[:, -3:] @ plus_basis[:, -3:].conj().T
    projector_check("channel.actual_Qmax", qmax)
    projector_check("channel.positive_Qmax", qplus)
    near("channel.actual_variational_equality", observe("channel.max_trace", qmax, actual), k3)
    near("channel.positive_variational_equality", observe("channel.plus_max_trace", qplus, plus), kp)
    near("channel.branch_spectrum", values, plus_values)

    if q <= 0.0:
        near("reflection.actual_channel_matrix", actual, spinflip(plus))
        reflected_max = spinflip(qplus)
        projector_check("reflection.transported_Qmax", reflected_max)
        near(
            "reflection.transported_maximizer_trace",
            observe("reflection.max_trace", reflected_max, actual),
            k3,
        )

    projectors = FIXED_PROJECTORS + [("actual-maximizer", qmax)]
    observations = []
    for projector_name, projector in projectors:
        projector_check("observable." + projector_name, projector)
        actual_trace = observe("observable.actual_trace", projector, actual)
        ge("observable.variational_bound", k3, actual_trace)
        consumer = spinflip(projector) if q < 0.0 else projector
        projector_check("observable.positive_branch_consumer", consumer)
        near(
            "observable.actual_reflected_duality",
            actual_trace,
            observe("observable.consumer_trace", consumer, plus),
        )
        if q <= 0.0:
            reflected = spinflip(projector)
            projector_check("observable.explicit_reflected_Q", reflected)
            near(
                "observable.reflection_trace_pairing",
                actual_trace,
                observe("observable.reflected_trace", reflected, plus),
            )
        observations.append((projector_name, projector, consumer, actual_trace))

    a = (1.0 + t) / 2.0
    b = (1.0 - t) / 2.0
    target = a ** 4 + 2.0 * a ** 3 * b
    near(
        "target.product_polynomial",
        16.0 * target,
        3.0 + 8.0 * t + 6.0 * t * t - t ** 4,
    )
    if p == 0.0:
        near("endpoint.identity_channel", actual, rho)
    if p == 1.0:
        near("endpoint.complete_depolarization", actual, I16 / 16.0)
        near("endpoint.complete_depolarization_k3", k3, 3.0 / 16.0)

    METRICS["channel_cases"] += 1
    return {
        "Y": actual,
        "plus": plus,
        "eigenvalues": values,
        "k3": k3,
        "kp": kp,
        "q": q,
        "t": t,
        "target": target,
        "observations": observations,
    }


def pure_channel_checks(profile, p):
    base = common_channel_checks(
        profile["name"], profile["rho"], profile["layers"], p
    )
    t = base["t"]
    tau = profile["tau"]
    L = profile["L"]
    c = profile["c"]
    kappa = profile["kappa"]
    alpha = 0.5 * t ** 3 * (1.0 + t)
    beta = 0.5 * t ** 3 * (1.0 - t)
    B = alpha * profile["rho"] - beta * spinflip(profile["rho"])
    decomposition = (
        B
        + (1.0 - t ** 4) * I16 / 16.0
        + (t - t ** 3) * profile["layers"][1] / 16.0
        + (t * t - t ** 4) * profile["layers"][2] / 16.0
    )
    near("decomposition.exact_matrix", base["plus"], decomposition)

    d = sqrt_checked("decomposition.d", 1.0 - (1.0 - t * t) * tau)
    lambda_plus = 0.5 * (t ** 4 + t ** 3 * d)
    lambda_minus = 0.5 * (t ** 4 - t ** 3 * d)
    expected_B_spectrum = np.sort(
        np.array([lambda_minus] + [0.0] * 14 + [lambda_plus])
    )
    near(
        "decomposition.rank_two_spectrum",
        hermitian_spectrum("decomposition.B", B),
        expected_B_spectrum,
    )
    near("decomposition.B_top3", top3("decomposition.B_top", B), lambda_plus)
    ge("decomposition.d_ge_t", d, t)
    ge("decomposition.lambda_plus_nonnegative", lambda_plus, 0.0)
    ge("decomposition.lambda_minus_nonpositive", 0.0, lambda_minus)

    bound8 = (
        3.0
        + L * t
        + c * t * t
        + (8.0 * d - L) * t ** 3
        + (5.0 - c) * t ** 4
    ) / 16.0
    ge("bound8.actual_positive_top3", bound8, base["kp"])
    rhs9 = (
        t * (1.0 - t * t) * (8.0 - L - (c - 6.0) * t)
        + 8.0 * t ** 3 * (1.0 - d)
    )
    near("bound9.algebraic_identity", 16.0 * (base["target"] - bound8), rhs9)
    ge("bound9.actual_gap", 16.0 * (base["target"] - base["kp"]), rhs9)

    f = 8.0 - L - (c - 6.0) * t + 4.0 * tau * t * t
    ge("bound10.square_root_step", 1.0 - 0.5 * (1.0 - t * t) * tau, d)
    ge("bound10.gap_relaxation", rhs9, t * (1.0 - t * t) * f)
    ge("bound10.f_ge_kappa", f, kappa)
    strict_gt("bound10.negative_f_derivative", c - 6.0, 8.0 * tau * t)

    factor = t * (1.0 - t * t)
    structural = base["target"] - kappa * factor / 16.0
    ge("structural.actual_top3_bound", structural, base["k3"])
    if kappa >= 0.0:
        ge("structural.sufficient_target_certificate", base["target"], base["k3"])

    slack_rows = []
    for projector_name, projector, consumer, actual_trace in base["observations"]:
        delta_B = lambda_plus - observe("slack.B_trace", consumer, B)
        delta1 = L - observe("slack.C1_trace", consumer, profile["layers"][1])
        delta2 = c - observe("slack.C2_trace", consumer, profile["layers"][2])
        ge("slack.delta_B_nonnegative", delta_B, 0.0)
        ge("slack.delta1_nonnegative", delta1, 0.0)
        ge("slack.delta2_nonnegative", delta2, 0.0)
        weighted = (
            16.0 * delta_B
            + (t - t ** 3) * delta1
            + (t * t - t ** 4) * delta2
        )
        gap16 = 16.0 * (base["target"] - actual_trace)
        near("slack.same_Q_exact_gap_identity", gap16, rhs9 + weighted)
        ge(
            "slack.same_Q_proved_lower_bound",
            gap16,
            factor * f + weighted,
        )
        ge("structural.same_Q_bound", structural, actual_trace)
        slack_rows.append(
            {
                "projector": projector_name,
                "actual_trace": actual_trace,
                "delta_B": delta_B,
                "delta1": delta1,
                "delta2": delta2,
                "weighted_slack": weighted,
            }
        )

    uniform = None
    if profile["sector"]:
        uniform = base["target"] - factor / 128.0
        ge("sector.actual_uniform_bound", uniform, base["k3"])
        for row in slack_rows:
            ge("sector.same_Q_uniform_bound", uniform, row["actual_trace"])

    if profile["product"]:
        near("positive_control.actual_product_target", base["k3"], base["target"])
    if p == 0.0:
        near("endpoint.pure_input_k3", base["k3"], 1.0)

    emit(
        "PURE_CHANNEL_CASE",
        name=profile["name"],
        p=p,
        q=base["q"],
        t=t,
        output_eigenvalues=base["eigenvalues"].tolist(),
        k3=base["k3"],
        positive_branch_k3=base["kp"],
        product_target=base["target"],
        target_gap=base["target"] - base["k3"],
        kappa=kappa,
        structural_upper=structural,
        structural_slack=structural - base["k3"],
        uniform_upper=uniform,
        uniform_slack=None if uniform is None else uniform - base["k3"],
        bound8=bound8,
        f=f,
        reflected_branch=bool(base["q"] < 0.0),
        same_Q_slacks=slack_rows,
        unproved_global_joint_slack_obligation_asserted=False,
    )
    return {"Y": base["Y"], "k3": base["k3"]}


def mixture_checks(name, members, profiles, outputs):
    weights = [weight for weight, member in members]
    near("mixture.weight_sum", float(sum(weights)), 1.0)
    for weight, member in members:
        ge("mixture.nonnegative_weight", weight, 0.0)
        if not profiles[member]["declared_sector"]:
            fail("mixture.component_construction", "component is not a declared sector family")
        ge("mixture.component_radius_condition", 0.25, profiles[member]["s"])
        strict_gt("mixture.component_certificate", profiles[member]["kappa"], 1.0 / 8.0)

    rho = sum(weight * profiles[member]["rho"] for weight, member in members)
    density("mixture.input", rho)
    layers, lengths, coefficients = pauli_layers(rho)
    radii, local_spectra = marginal_checks(rho, coefficients, pure=False)
    average_kappa = float(
        sum(weight * profiles[member]["kappa"] for weight, member in members)
    )
    emit(
        "MIXTURE_PROFILE",
        name=name,
        members=[{"weight": weight, "pure_name": member} for weight, member in members],
        mixed_radii=radii.tolist(),
        mixed_local_spectra=local_spectra,
        mixed_radius_condition_used_as_membership=False,
        membership_basis="explicit convex decomposition into checked declared pure families",
        average_component_kappa=average_kappa,
    )
    for index, p in enumerate(P_VALUES):
        global CURRENT
        CURRENT = "%s/p=%s" % (name, float(p).hex())
        base = common_channel_checks(name, rho, layers, p)
        linear_output = sum(
            weight * outputs[member][index]["Y"] for weight, member in members
        )
        near("mixture.actual_channel_linearity", base["Y"], linear_output)
        convex_top3 = float(
            sum(weight * outputs[member][index]["k3"] for weight, member in members)
        )
        ge("mixture.actual_K3_convexity", convex_top3, base["k3"])
        factor = base["t"] * (1.0 - base["t"] ** 2)
        stronger = base["target"] - average_kappa * factor / 16.0
        uniform = base["target"] - factor / 128.0
        ge("mixture.averaged_structural_bound", stronger, base["k3"])
        ge("mixture.uniform_sector_bound", uniform, base["k3"])
        same_q = []
        for projector_name, projector, consumer, actual_trace in base["observations"]:
            averaged_trace = float(
                sum(
                    weight
                    * observe("mixture.component_same_Q_trace", projector, outputs[member][index]["Y"])
                    for weight, member in members
                )
            )
            near("mixture.same_Q_linearity", actual_trace, averaged_trace)
            for weight, member in members:
                component_bound = (
                    base["target"]
                    - profiles[member]["kappa"] * factor / 16.0
                )
                component_trace = observe(
                    "mixture.component_bound_trace", projector, outputs[member][index]["Y"]
                )
                ge("mixture.component_fixed_Q_certificate", component_bound, component_trace)
            ge("mixture.same_Q_structural_bound", stronger, actual_trace)
            ge("mixture.same_Q_uniform_bound", uniform, actual_trace)
            same_q.append({"projector": projector_name, "actual_trace": actual_trace})
        emit(
            "MIXTURE_CHANNEL_CASE",
            name=name,
            p=p,
            q=base["q"],
            t=base["t"],
            output_eigenvalues=base["eigenvalues"].tolist(),
            k3=base["k3"],
            product_target=base["target"],
            convex_average_component_k3=convex_top3,
            averaged_structural_upper=stronger,
            uniform_upper=uniform,
            uniform_slack=uniform - base["k3"],
            same_Q=same_q,
        )


def expected_numeric_rejection(name, actual, expected):
    finite(name + ".mutant_finite", actual)
    finite(name + ".reference_finite", expected)
    residual = maxabs(np.asarray(actual) - np.asarray(expected))
    if residual < CONTROL_MIN_GAP:
        fail(
            name + ".control_separation",
            "mutant residual %.17g is below required %.17g"
            % (residual, CONTROL_MIN_GAP),
        )
    try:
        near(name, actual, expected)
    except CheckError as error:
        if error.check != name:
            raise
        METRICS["expected_control_rejections"] += 1
        emit(
            "EXPECTED_NUMERIC_REJECTION",
            control=name,
            residual=residual,
            intended_failure=error.check,
            detail=error.detail,
        )
        return
    fail(name + ".unexpected_acceptance", "scientific mutation was accepted")


def scientific_controls():
    global CURRENT
    CURRENT = "controls/dropped-conjugation"

    psi = ghz(0.5, math.pi / 4.0)
    near("control.ghz_norm", float(np.linalg.norm(psi)), 1.0)
    rho = outer(psi)
    density("control.ghz_density", rho)
    layers, lengths, coefficients = pauli_layers(rho)
    radii, spectra = marginal_checks(rho, coefficients, pure=True)
    s = float(np.sum(radii ** 2))
    true_tau = float(abs(np.vdot(psi, W @ psi.conj())) ** 2)
    bad_tau = float(abs(np.vdot(psi, W @ psi)) ** 2)
    near("control.correct_A2_identity", float(lengths[2]), s + 2.0 + 4.0 * true_tau)
    expected_numeric_rejection(
        "NEGATIVE_missing_vector_conjugation_A2_identity",
        float(lengths[2]),
        s + 2.0 + 4.0 * bad_tau,
    )

    bad_flip = W @ rho @ W
    density("control.bad_flip_still_physical", bad_flip)
    correct_parity_flip = sum(
        ((-1) ** weight) * layers[weight] for weight in range(5)
    ) / 16.0
    near("control.correct_flip_parity", spinflip(rho), correct_parity_flip)
    expected_numeric_rejection(
        "NEGATIVE_missing_matrix_transpose_spinflip_parity",
        bad_flip,
        correct_parity_flip,
    )

    CURRENT = "controls/actual-reflected-projector"
    vector = (E16[:, 0] + 1.0j * E16[:, 1]) / math.sqrt(2.0)
    rho = outer(vector)
    density("control.reflection_input", rho)
    projector = outer(vector) + outer(E16[:, 2]) + outer(E16[:, 3])
    projector_check("control.complex_Q", projector)
    strict_gt("control.Q_genuinely_complex", float(np.linalg.norm(projector.imag)), 0.0)
    t = 1.0 / 3.0
    plus = replacement_channel(rho, 1.0 - t)
    minus = replacement_channel(rho, 1.0 + t)
    density("control.plus_physical", plus)
    density("control.minus_physical", minus)
    near("control.plus_kraus", plus, kraus_channel(rho, 1.0 - t))
    near("control.minus_kraus", minus, kraus_channel(rho, 1.0 + t))
    near("control.actual_matrix_reflection", minus, spinflip(plus))
    reflected_Q = spinflip(projector)
    projector_check("control.correct_reflected_Q", reflected_Q)
    actual_pairing = observe("control.actual_minus_pairing", projector, minus)
    correct_pairing = observe("control.correct_plus_pairing", reflected_Q, plus)
    near("control.correct_projector_duality", actual_pairing, correct_pairing)
    expected_numeric_rejection(
        "NEGATIVE_stale_Q_under_actual_channel_reflection",
        actual_pairing,
        observe("control.stale_plus_pairing", projector, plus),
    )
    wrong_reflection = W @ projector @ W
    projector_check("control.wrong_reflection_still_projector", wrong_reflection)
    expected_numeric_rejection(
        "NEGATIVE_Q_reflection_missing_transpose",
        actual_pairing,
        observe("control.wrong_reflected_pairing", wrong_reflection, plus),
    )

    CURRENT = "controls/channel-scaling"
    layers, lengths, coefficients = pauli_layers(rho)
    p = 3.0 / 8.0
    correct_output = replacement_channel(rho, p)
    reference = pauli_channel(layers, 1.0 - p)
    near("control.correct_channel_scaling", correct_output, reference)
    near("control.correct_channel_kraus", correct_output, kraus_channel(rho, p))
    # Confuses replacement p with total nonidentity-Pauli probability.
    bad_output = replacement_channel(rho, 4.0 * p / 3.0)
    density("control.misscaled_channel_still_physical", bad_output)
    expected_numeric_rejection(
        "NEGATIVE_channel_Pauli_error_vs_replacement_scaling",
        bad_output,
        reference,
    )

    if METRICS["expected_control_rejections"] != 5:
        fail("control.rejection_count", "all five intended scientific mutations must fail")


def setup_operators():
    global SINGLE_PAULIS, I16, E16, CODES, WEIGHTS, PAULIS, W
    global ON_SITE, FIXED_PROJECTORS

    SINGLE_PAULIS = (
        np.eye(2, dtype=np.complex128),
        np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128),
        np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=np.complex128),
        np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128),
    )
    I16 = np.eye(16, dtype=np.complex128)
    E16 = I16.copy()
    CODES = np.array(list(itertools.product(range(4), repeat=4)), dtype=int)
    WEIGHTS = np.count_nonzero(CODES, axis=1)
    PAULIS = np.stack(
        [kron_all([SINGLE_PAULIS[code] for code in row]) for row in CODES]
    )
    W = kron_all([SINGLE_PAULIS[2]] * 4)
    near("operator.W_symmetric", W.T, W)
    near("operator.W_unitary", W.conj().T @ W, I16)
    for operator, weight in zip(PAULIS, WEIGHTS):
        tick()
        near("operator.Pauli_spinflip_parity", spinflip(operator), ((-1) ** int(weight)) * operator)

    ON_SITE = []
    for site in range(4):
        site_operators = []
        for code in range(4):
            factors = [SINGLE_PAULIS[0]] * 4
            factors[site] = SINGLE_PAULIS[code]
            site_operators.append(kron_all(factors))
        ON_SITE.append(site_operators)

    grid = np.arange(16, dtype=float)
    fourier = np.exp(2.0j * math.pi * np.outer(grid, grid) / 16.0) / 4.0
    near("operator.Fourier_unitary", fourier.conj().T @ fourier, I16)
    columns = fourier[:, [0, 1, 4]]
    q_fourier = columns @ columns.conj().T
    vector = (E16[:, 0] + 1.0j * E16[:, 1]) / math.sqrt(2.0)
    q_sparse = outer(vector) + outer(E16[:, 2]) + outer(E16[:, 3])
    FIXED_PROJECTORS = [
        ("complex-Fourier", q_fourier),
        ("complex-sparse", q_sparse),
    ]
    for name, projector in FIXED_PROJECTORS:
        projector_check("operator." + name, projector)
        strict_gt("operator.fixed_Q_complex", float(np.linalg.norm(projector.imag)), 0.0)


def peak_rss_mib():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes; Linux reports KiB.
    return float(raw / (1024.0 ** 2) if sys.platform == "darwin" else raw / 1024.0)


def finish(status, **fields):
    emit(
        "RESULT",
        status=status,
        elapsed_seconds=time.monotonic() - START,
        peak_rss_mib=peak_rss_mib(),
        memory_limit_os_enforced=False,
        cooperative_budget_seconds=BUDGET_SECONDS,
        metrics=METRICS.copy(),
        universal_proof=False,
        independent_model_family=False,
        formal_kernel_verification=False,
        novelty_acceptance=False,
        retries=0,
        **fields,
    )


def main():
    global np, CURRENT
    if len(sys.argv) != 1:
        fail("argv", "this fixed diagnostic accepts no arguments")

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.signal(signal.SIGTERM, alarm_handler)
    signal.signal(signal.SIGINT, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, BUDGET_SECONDS)

    import numpy as numpy_module

    np = numpy_module
    np.seterr(over="raise", divide="raise", invalid="raise")
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    emit(
        "RUN_HEADER",
        diagnostic="f354-independent-four-qubit-depolarizing-sector",
        source_sha256=source_hash,
        observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        python=sys.version,
        numpy=np.__version__,
        platform=sys.platform,
        pid=os.getpid(),
        pgid=os.getpgrp(),
        seed=SEED,
        p_values=list(P_VALUES),
        equality_atol=ATOL,
        equality_rtol=RTOL,
        inequality_tolerance_factor=ITOL,
        strict_margin=STRICT_MARGIN,
        control_minimum_gap=CONTROL_MIN_GAP,
        cooperative_budget_seconds=BUDGET_SECONDS,
        blas_thread_environment={
            key: os.environ[key]
            for key in (
                "OPENBLAS_NUM_THREADS",
                "OMP_NUM_THREADS",
                "MKL_NUM_THREADS",
                "VECLIB_MAXIMUM_THREADS",
                "NUMEXPR_NUM_THREADS",
            )
        },
        frozen_manifest_pin_parent_supplied=(
            "f2ddd9045b85cb19e198327d6c4bb4174306791ead40684c40c85046cd156516"
        ),
        frozen_candidate_pin_parent_supplied=(
            "22851a57a04a9ff9f7ea44b13ec3fd8677af03f92f3a3ca62da5de049d3d89cc"
        ),
        science_inputs_read_from_files=False,
        source_file_read_only_for_self_hash=True,
    )

    CURRENT = "operator-setup"
    setup_operators()
    CURRENT = "fixture-construction"
    fixtures = make_fixtures()
    scientific_controls()

    profiles = {}
    outputs = {}
    for item in fixtures:
        CURRENT = item["name"] + "/profile"
        profile = pure_profile(item)
        profiles[item["name"]] = profile
        outputs[item["name"]] = []
        for p in P_VALUES:
            CURRENT = "%s/p=%s" % (item["name"], float(p).hex())
            outputs[item["name"]].append(pure_channel_checks(profile, p))

    mixtures = (
        (
            "mixture-boundary-and-zero",
            (
                (0.2, "ghz-low-boundary"),
                (0.3, "rotated-pair-boundary"),
                (0.5, "rotated-bell-correlated-zero"),
            ),
        ),
        (
            "mixture-two-distinct-zero-families",
            (
                (0.4, "ghz-zero"),
                (0.6, "rotated-cluster-zero"),
            ),
        ),
    )
    for name, members in mixtures:
        CURRENT = name + "/profile"
        mixture_checks(name, members, profiles, outputs)

    expected_channel_cases = (len(fixtures) + len(mixtures)) * len(P_VALUES)
    if METRICS["channel_cases"] != expected_channel_cases:
        fail(
            "coverage.channel_case_count",
            "%d != %d" % (METRICS["channel_cases"], expected_channel_cases),
        )
    if METRICS["expected_control_rejections"] != 5:
        fail("coverage.control_count", "five intended numeric rejections required")

    tick()
    signal.setitimer(signal.ITIMER_REAL, 0.0)
    finish(
        "PASS_FINITE_DIAGNOSTIC",
        source_sha256=source_hash,
        primary_pure_inputs=len(fixtures),
        explicit_qualifying_mixtures=len(mixtures),
        physical_parameters=len(P_VALUES),
        completed_channel_cases=METRICS["channel_cases"],
        intended_scientific_mutations_rejected=5,
        interpretation=(
            "Finite numerical agreement only. No continuum, global theorem, "
            "mixed-radius membership, or unproved joint-slack acceptance."
        ),
    )


if __name__ == "__main__":
    exit_status = 0
    try:
        main()
    except CheckError as error:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        finish(
            "FAIL_FINITE_CHECK",
            context=error.context,
            failed_check=error.check,
            detail=error.detail,
            interpretation=(
                "Inspect the numerical failure and implementation. "
                "A finite diagnostic failure is not automatically a theorem counterexample."
            ),
        )
        exit_status = 1
    except (BudgetExceeded, KeyboardInterrupt) as error:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        finish("INCOMPLETE", context=CURRENT, detail=str(error))
        exit_status = 2
    except Exception as error:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
        finish(
            "INCOMPLETE",
            context=CURRENT,
            detail=repr(error),
            traceback=traceback.format_exc(),
        )
        exit_status = 2
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
    sys.exit(exit_status)
