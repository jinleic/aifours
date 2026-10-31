#!/usr/bin/env python3
"""Prospective f707 exact certificate generator. NOT RUN by its author.

Fixed finite data, rational arithmetic only. No files, network, subprocesses,
input or deletion. Emits one JSON object to stdout after all checks pass.
The parent must fully read this source and issue a separate one-shot GO.
"""

from fractions import Fraction as F
from math import comb
import json


class Reject(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Reject(reason)


def expected_rejection(name, reason, call):
    try:
        call()
    except Reject as exc:
        if str(exc) != reason:
            raise RuntimeError(name + ": wrong rejection: " + str(exc)) from exc
        return {"control": name, "rejected_for": reason}
    except Exception as exc:
        raise RuntimeError(name + ": non-target exception") from exc
    raise RuntimeError(name + ": mutation was not rejected")


def vecstr(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, list) or isinstance(value, tuple):
        return [vecstr(v) for v in value]
    if isinstance(value, dict):
        return {str(k): vecstr(v) for k, v in value.items()}
    return value


def dot(a, b):
    require(len(a) == len(b), "DOT_DIMENSION")
    return sum((x * y for x, y in zip(a, b)), F(0))


def evaluate(poly, x):
    v = F(0)
    for c in reversed(poly):
        v = v * x + c
    return v


def convolution(a, b):
    out = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def parity(c):
    require(len(c) == 8, "SEPTIC_LENGTH")
    return ([c[0], -c[2], c[4], -c[6]],
            [c[1], -c[3], c[5], -c[7]])


def pairing_polynomial(q, a):
    fq, gq = parity(q)
    ea, oa = parity(a)
    fe, go = convolution(fq, ea), convolution(gq, oa)
    out = [F(0) for _ in range(8)]
    for i in range(7):
        out[i] += fe[i]
        out[i + 1] += go[i]
    return out


def complex_at_iw(c, omega):
    # Horner with rational real/imaginary pairs, independent of parity().
    re, im = F(0), F(0)
    for coefficient in reversed(c):
        re, im = coefficient - omega * im, omega * re
    return re, im


def physical_row(a, t):
    e, o = parity(a)
    ev, ov = evaluate(e, t), evaluate(o, t)
    return [ev, t * ov, -t * ev, -t**2 * ov,
            t**2 * ev, t**3 * ov, -t**3 * ev, -t**4 * ov]


def sample_check(q, a, omega, mutation=None):
    t = omega * omega
    qr, qi = complex_at_iw(q, omega)
    ar, ai = complex_at_iw(a, omega)
    direct = qr * ar + qi * ai
    fq, gq = parity(q)
    ea, oa = parity(a)
    f, g, e, o = (evaluate(fq, t), evaluate(gq, t),
                   evaluate(ea, t), evaluate(oa, t))
    require(qr == f and qi == omega * g, "Q_PARITY_COMPLEX_MISMATCH")
    require(ar == e and ai == omega * o, "A_PARITY_COMPLEX_MISMATCH")
    if mutation == "EVEN_SIGN":
        e = evaluate([a[0], a[2], a[4], -a[6]], t)
    if mutation == "ODD_SIGN":
        value = f * e - t * g * o
    else:
        value = f * e + t * g * o
    require(value == direct, "PARITY_COMPLEX_MISMATCH")
    poly_value = evaluate(pairing_polynomial(q, a), t)
    require(poly_value == direct, "CONVOLUTION_COMPLEX_MISMATCH")
    require(dot(q, physical_row(a, t)) == direct, "RAW_ROW_MISMATCH")
    return {"omega": omega, "t": t, "convolution": poly_value,
            "direct_complex": direct, "parity_formula": value}


def corner(center, h, sigma, tau):
    require(sigma in (-1, 1) and tau in (-1, 1), "CORNER_LABEL")
    a = list(center)
    for j in range(7):
        parity_label = sigma if j % 2 == 0 else tau
        a[j] = center[j] + parity_label * (-1)**(j // 2) * h[j]
    return a


def check_corner(center, h, sigma, tau, a):
    require(len(a) == 8 and a[7] == 1, "CORNER_NOT_MONIC")
    for j in range(7):
        label = sigma if j % 2 == 0 else tau
        expected = center[j] + label * (-1)**(j // 2) * h[j]
        require(a[j] == expected, "ENDPOINT_PARITY")


def check_uniform_numerator(qs, eta):
    require(len(qs) == 4 and all(len(q) == 8 for q in qs), "Q_SCOPE")
    require(all(q == qs[0] for q in qs[1:]), "NONUNIFORM_Q")
    require(qs[0][7] == 1, "Q7_NOT_MONIC")
    require(eta > 0, "ETA_NOT_POSITIVE")


def check_homotopy(center, h, proof_kind):
    # These exact hypotheses support the separate written global proof.
    require(proof_kind == "GLOBAL_PERTURBATION_HOMOTOPY",
            "CORNER_STABILITY_NOT_BOX_PROOF")
    require(center == [F(comb(7, j)) for j in range(8)],
            "CENTER_NOT_BINOMIAL")
    require(len(h) == 7 and all(x > 0 for x in h), "NOT_FULL_WIDTH")
    total = sum(h, F(0))
    require(total < 1, "HOMOTOPY_BOUND_NOT_STRICT")
    require(center[0] - h[0] > 0, "CONSTANT_ENDPOINT_NOT_POSITIVE")
    return F(1) - total


def check_consumer_scope(omitted_r4, r5_orientations):
    # Scope check only: this does not enumerate or prove any actual ray.
    require(set(omitted_r4) == {0, 1, 2, 3}, "R4_OMISSION_SCOPE")
    require(set(r5_orientations) == {"PLUS_MINUS_PLUS", "MINUS_PLUS_MINUS"},
            "R5_ORIENTATION_SCOPE")


def explicit_residual(sigma, tau):
    # These integer vectors are F*(1+t+t^2+t^3) and t*G*(1+t+t^2).
    a = [1, -20, 15, 8, 7, 28, -7, 0]
    b = [0, 7, -28, -7, -15, 20, -1, 0]
    return [F(comb(7, k), 2) + F(sigma * a[k] + tau * b[k], 1000)
            for k in range(8)]


def diagonal_matrix(entries):
    require(len(entries) == 4, "GRAM_DIMENSION")
    return [[entries[i] if i == j else F(0) for j in range(4)]
            for i in range(4)]


def check_gram(residual, m, n):
    require(len(residual) == 8 and len(m) == 4 and len(n) == 4,
            "GRAM_DIMENSION")
    reconstructed = [F(0) for _ in range(8)]
    for matrix in (m, n):
        require(all(len(row) == 4 for row in matrix), "GRAM_DIMENSION")
        for i in range(4):
            for j in range(4):
                if i != j:
                    require(matrix[i][j] == 0, "GRAM_NOT_DIAGONAL")
            require(matrix[i][i] >= 0, "GRAM_NOT_PSD")
    for i in range(4):
        for j in range(4):
            reconstructed[i + j] += m[i][j]
            reconstructed[i + j + 1] += n[i][j]
    require(reconstructed == residual, "GRAM_COEFFICIENT_IDENTITY")
    return [{"degree": k, "residual": residual[k], "gram": reconstructed[k]}
            for k in range(8)]


def verify_zero_hull(rows, weights):
    require(len(rows) == len(weights) and len(rows) > 0, "ZERO_HULL_LENGTH")
    require(all(len(row) == 8 for row in rows), "ZERO_HULL_DIMENSION")
    require(all(w > 0 for w in weights), "ZERO_HULL_WEIGHT")
    require(sum(weights, F(0)) == 1, "ZERO_HULL_NORMALIZATION")
    aggregate = [sum((weights[i] * rows[i][j] for i in range(len(rows))), F(0))
                 for j in range(8)]
    require(aggregate == [F(0)] * 8, "ZERO_HULL_AGGREGATE")
    return aggregate


def phase_score(q, rows):
    return min(dot(q, row) for row in rows)


def require_strict_phase(margin):
    require(margin > 0, "ZERO_OR_NEGATIVE_PHASE_NOT_STRICT")


def main():
    q = [F(comb(7, j)) for j in range(8)]
    h = [F(1, 1000) for _ in range(7)]
    eta = F(1, 2)
    labels = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    check_uniform_numerator([list(q) for _ in labels], eta)
    small_bound = check_homotopy(q, h, "GLOBAL_PERTURBATION_HOMOTOPY")
    check_consumer_scope({0, 1, 2, 3}, {"PLUS_MINUS_PLUS", "MINUS_PLUS_MINUS"})
    baseline = pairing_polynomial(q, q)
    require(baseline == [F(comb(7, k)) for k in range(8)], "BINOMIAL_PAIRING")
    require(small_bound == F(993, 1000), "SMALL_HOMOTOPY_MARGIN")

    corner_records = []
    first = None
    for sigma, tau in labels:
        a = corner(q, h, sigma, tau)
        if first is None:
            first = a
        check_corner(q, h, sigma, tau, a)
        pair = pairing_polynomial(q, a)
        residual = [pair[k] - eta * F(comb(7, k)) for k in range(8)]
        require(residual == explicit_residual(sigma, tau), "EXPLICIT_P_MISMATCH")
        require(all(x >= 0 for x in residual), "NEGATIVE_RESIDUAL_COEFFICIENT")
        require(pair[7] == 1 and residual[7] == F(1, 2), "INFINITY_BOUNDARY")
        m = diagonal_matrix([residual[k] for k in (0, 2, 4, 6)])
        n = diagonal_matrix([residual[k] for k in (1, 3, 5, 7)])
        identities = check_gram(residual, m, n)
        samples = [sample_check(q, a, w) for w in
                   (F(0), F(1, 2), F(1), F(2), F(3))]
        corner_records.append({"sigma": sigma, "tau": tau, "actual_a": a,
                               "P_coefficients_ascending": pair,
                               "p_coefficients_ascending": residual,
                               "M": m, "N": n, "coefficient_identities": identities,
                               "rational_sample_cross_checks_only": samples})
    require(sum(len(record["coefficient_identities"]) for record in corner_records) == 32,
            "NOT_32_IDENTITIES")

    wide_h = [F(9, 10)] + [F(1, 100) for _ in range(6)]
    wide_bound = check_homotopy(q, wide_h, "GLOBAL_PERTURBATION_HOMOTOPY")
    require(wide_bound == F(1, 25), "WIDE_UNIFORM_BOUND")
    lower, upper = q[0] - wide_h[0], q[0] + wide_h[0]
    ratio = upper / lower
    require(ratio == 19, "WIDE_CONSTANT_RATIO")
    require(F(1) + F(5, 6) == 11 * (F(1) - F(5, 6)),
            "BINOMIAL_FAMILY_RATIO_BOUND")
    require(ratio > 11, "STRICT_CONTAINMENT_COMPARISON")

    # Synthetic data, deliberately NOT an eligible common box.
    nodes = [F(1), F(2), F(3), F(4)]
    even_values = [F(-4), F(6), F(-4), F(1)]
    odd_values = [F(-1, 6), F(1, 4), F(-1, 6), F(1, 24)]
    synthetic_polynomials = [[even_values[i], nodes[i]**3 + odd_values[i],
                              F(0), F(0), F(0), F(0), F(0), F(1)]
                             for i in range(4)]
    raw = [physical_row(synthetic_polynomials[i], nodes[i]) for i in range(4)]
    e0 = [F(1)] + [F(0)] * 7
    e7 = [F(0)] * 7 + [F(1)]
    require(physical_row(synthetic_polynomials[3], F(0)) == e0,
            "SYNTHETIC_ZERO_ENDPOINT")
    require(all(a[7] == 1 for a in synthetic_polynomials), "SYNTHETIC_MONIC")
    raw_sum = [sum((row[j] for row in raw), F(0)) + e0[j] + e7[j]
               for j in range(8)]
    require(raw_sum == [F(0)] * 8, "SYNTHETIC_RAW_ZERO_IDENTITY")
    normalizers = [(1 + t)**7 for t in nodes]
    total = sum(normalizers, F(0)) + 2
    require(total == 96826, "SYNTHETIC_NORMALIZER")
    rows = [[entry / normalizers[i] for entry in raw[i]] for i in range(4)] + [e0, e7]
    weights = [v / total for v in normalizers] + [F(1) / total, F(1) / total]
    zero_aggregate = verify_zero_hull(rows, weights)
    zero_phase = phase_score([F(0)] * 8, rows)
    require(zero_phase == 0, "SYNTHETIC_ZERO_PHASE")
    monic_bound = -weights[-1] / (1 - weights[-1])
    require(monic_bound == F(-1, 96825), "SYNTHETIC_MONIC_BOUND")
    require(phase_score(q, rows) <= monic_bound, "SYNTHETIC_MONIC_EXAMPLE")
    require(synthetic_polynomials[0][0] < 0 and
            evaluate(synthetic_polynomials[0], F(2)) > 0,
            "SYNTHETIC_POSITIVE_ROOT_SIGN_BRACKET")

    wrong_corner = list(first)
    wrong_corner[0] = q[0] + h[0]
    changed_q = list(q)
    changed_q[0] += 1
    nonmonic = list(q)
    nonmonic[7] = F(2)
    residual0 = corner_records[0]["p_coefficients_ascending"]
    bad_m = [list(row) for row in corner_records[0]["M"]]
    bad_m[1][1] += 1
    negative_m = [list(row) for row in corner_records[0]["M"]]
    negative_m[0][0] = F(-1)
    bad_weights = list(weights)
    bad_weights[0], bad_weights[1] = bad_weights[1], bad_weights[0]
    controls = [
        expected_rejection("wrong even endpoint parity", "ENDPOINT_PARITY",
                           lambda: check_corner(q, h, -1, -1, wrong_corner)),
        expected_rejection("wrong even sign", "PARITY_COMPLEX_MISMATCH",
                           lambda: sample_check(q, first, F(1), "EVEN_SIGN")),
        expected_rejection("wrong odd sign", "PARITY_COMPLEX_MISMATCH",
                           lambda: sample_check(q, first, F(1), "ODD_SIGN")),
        expected_rejection("missing one R5 orientation (scope only)", "R5_ORIENTATION_SCOPE",
                           lambda: check_consumer_scope({0, 1, 2, 3}, {"PLUS_MINUS_PLUS"})),
        expected_rejection("nonuniform numerator", "NONUNIFORM_Q",
                           lambda: check_uniform_numerator([q, changed_q, q, q], eta)),
        expected_rejection("nonmonic q7", "Q7_NOT_MONIC",
                           lambda: check_uniform_numerator([nonmonic] * 4, eta)),
        expected_rejection("zero eta", "ETA_NOT_POSITIVE",
                           lambda: check_uniform_numerator([q] * 4, F(0))),
        expected_rejection("corner-only stability claim (scope only)",
                           "CORNER_STABILITY_NOT_BOX_PROOF",
                           lambda: check_homotopy(q, h, "CORNERS_ONLY")),
        expected_rejection("non-strict homotopy bound", "HOMOTOPY_BOUND_NOT_STRICT",
                           lambda: check_homotopy(q, [F(1)] + h[1:],
                                                  "GLOBAL_PERTURBATION_HOMOTOPY")),
        expected_rejection("changed gram coefficient", "GRAM_COEFFICIENT_IDENTITY",
                           lambda: check_gram(residual0, bad_m, corner_records[0]["N"])),
        expected_rejection("negative diagonal", "GRAM_NOT_PSD",
                           lambda: check_gram(residual0, negative_m, corner_records[0]["N"])),
        expected_rejection("changed convex weights", "ZERO_HULL_AGGREGATE",
                           lambda: verify_zero_hull(rows, bad_weights)),
        expected_rejection("zero phase called strictly positive", "ZERO_OR_NEGATIVE_PHASE_NOT_STRICT",
                           lambda: require_strict_phase(zero_phase)),
    ]

    result = {
        "role": "PROSPECTIVE_FINITE_SOURCE_PARENT_GO_REQUIRED",
        "limits": ["NOT a global ROOT or common-SPR theorem",
                   "No eligible zero-hull or strict-negative witness supplied",
                   "WIDE_SDP_NOT_TESTED", "Samples are checks, not all-frequency proof",
                   "Synthetic rows are NOT an eligible-box counterexample"],
        "small_box": {"center_q_ascending": q, "halfwidths_j0_to_j6": h,
                      "eta": eta, "global_homotopy_margin": small_bound,
                      "corners": corner_records, "coefficient_identity_count": 32,
                      "q7_and_normalized_P_at_infinity": F(1),
                      "normalized_residual_at_infinity": F(1, 2)},
        "wide_diagnostic": {"halfwidths": wide_h, "global_margin": wide_bound,
                            "constant_interval": [lower, upper], "ratio": ratio,
                            "scaled_binomial_family_ratio_strict_upper_bound": F(11),
                            "wide_sdp": "NOT_TESTED"},
        "synthetic_logical_guard": {
            "eligibility": "NOT_ELIGIBLE_SYNTHETIC_ONLY",
            "positive_real_root_bracket_first_polynomial": [F(0), F(2)],
            "polynomials_ascending": synthetic_polynomials, "nodes": nodes,
            "raw_rows": raw, "raw_endpoint_coefficients_e0_e7": [F(1), F(1)],
            "raw_sum_including_endpoints": raw_sum,
            "compact_rows": rows, "positive_convex_weights": weights,
            "weight_denominator": total, "compact_aggregate": zero_aggregate,
            "unrestricted_phase_max": F(0),
            "proof_of_max": "zero vector attains 0; weighted zero hull forces every minimum <= 0",
            "monic_phase_upper_bound": monic_bound,
            "monic_bound_proof": "e7 has positive weight and q7=1; weighted average is zero"},
        "controls": controls,
    }
    print(json.dumps(vecstr(result), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
