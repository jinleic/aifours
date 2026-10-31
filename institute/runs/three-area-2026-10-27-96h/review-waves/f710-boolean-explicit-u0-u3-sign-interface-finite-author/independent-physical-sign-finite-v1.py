#!/usr/bin/env python3
# Prospective bounded finite source.  This file was not executed by its author.
# Parent must fully statically read and issue a separate GO before one run.
import json
import signal
import sys
import time

LIMIT_SECONDS = 45.0
START = time.monotonic()
DEADLINE = START + LIMIT_SECONDS
STOP = [0]
COUNTS = {}
FIRST_FAILURES = []
FAILURES = 0
OBS = {"reference_transports": 0, "sign_cases": 0,
       "sign_case_transports": 0, "all_32_caps_cases": 0,
       "all_32_caps_and_J1_cases": 0, "capped_inequality_failures": 0}


def latch(signum, _frame):
    STOP[0] = signum


signal.signal(signal.SIGINT, latch)
signal.signal(signal.SIGTERM, latch)


class Incomplete(Exception):
    pass


def guard():
    if STOP[0] or time.monotonic() >= DEADLINE:
        raise Incomplete("signal=%s or cooperative 45-second deadline" % STOP[0])


def emit(value):
    print(json.dumps(value, sort_keys=True, separators=(",", ":")), flush=True)


def check(name, condition, context=None):
    global FAILURES
    item = COUNTS.setdefault(name, {"tested": 0, "passed": 0, "failed": 0})
    item["tested"] += 1
    if condition:
        item["passed"] += 1
    else:
        item["failed"] += 1
        FAILURES += 1
        if len(FIRST_FAILURES) < 40:
            FIRST_FAILURES.append({"check": name, "context": context})


def bit(x, i):
    return (x >> i) & 1


def char(mask, point):
    return 1 - 2 * ((mask & point).bit_count() & 1)


def point(ell, h, j, b):
    return (ell << 5) | (h << 4) | (j << 2) | b


def f(j):
    return bit(j, 0) * bit(j, 1)


def phase(j, b):
    return (j & b).bit_count() & 1


def rho(b):
    return 1 - 2 * (1 ^ (bit(b, 0) * bit(b, 1)))


def xorsum(points):
    result = 0
    for p in points:
        result ^= p
    return result


def direct_walsh(values):
    # Independent ordinary dot-product definition, not a butterfly.
    return [sum(values[c] * CHARACTER[k][c] for c in range(len(values)))
            for k in range(len(values))]


def butterfly(values):
    out = list(values)
    width = 1
    while width < len(out):
        for start in range(0, len(out), 2 * width):
            for i in range(start, start + width):
                left, right = out[i], out[i + width]
                out[i], out[i + width] = left + right, left - right
        width *= 2
    return out


CHARACTER = [[char(k, c) for c in range(64)] for k in range(64)]
WCHAR = [[1, char(1, w), char(2, w), char(3, w)] for w in range(4)]
GRAPH = [point(1, f(j), j, b) for j in range(4) for b in range(4)]
D0 = [point(1, 1 ^ f(j), j, 0) for j in range(4)]
D3 = [point(1, 1 ^ f(j), j, b) for j in range(4) for b in (1, 2, 3)]
EROW = [point(0, h, j, 0) for j in (1, 2, 3) for h in (0, 1)]
FROW = [point(0, h, 0, 0) for h in (0, 1)]
ZSPEC = [(1, 1, 2, 2), (1, 1, 3, -2),
         (2, 1, 1, -2), (2, 1, 3, 2),
         (3, 0, 1, 2), (3, 0, 2, -2)]
Z2 = [point(0, h, j, b) for j, h, b, _ in ZSPEC]
ZSITES = [point(0, h, j, b) for j in range(4)
          for h in (0, 1) for b in (1, 2, 3)]
Z4SITES = [c for c in ZSITES if c not in Z2]
SIGNSITES = D3 + EROW + Z2
REFERENCE_Z4 = point(0, 0, 0, 1)
ALL_MASK = (1 << 24) - 1


def make_fixed():
    a, g, x = [0] * 64, [0] * 64, [0] * 64
    for j in range(4):
        for b in range(4):
            graph = point(1, f(j), j, b)
            mate = point(1, 1 ^ f(j), j, b)
            a[graph] = 1 - 2 * phase(j, b)
            g[graph] = rho(b)
            g[mate] = -2 * rho(b)
            x[graph] = 1 if b == j else -1
        x[point(1, 1 ^ f(j), j, 0)] = 2
    for h in (0, 1):
        for j in range(4):
            g[point(0, h, j, 0)] = 4 if j == 0 else -2
    for j, h, b, value in ZSPEC:
        x[point(0, h, j, b)] = value
    return a, g, x


def make_y(a, g, x, mask, z4site, z4sign):
    y = [0] * 64
    for c in GRAPH:
        y[c] = -a[c] * g[c] * x[c]
    for i, c in enumerate(SIGNSITES):
        y[c] = 2 * (1 - 2 * bit(mask, i))
    y[z4site] = 4 * z4sign
    return y


def inverse(x, a, g, y):
    # Return all 256 entries, along with exact divisibility failure count.
    u = []
    bad_divisions = 0
    for c in range(64):
        for w in range(4):
            n = x[c] + 3 * a[c] * WCHAR[w][1] + g[c] * WCHAR[w][2] + y[c] * WCHAR[w][3]
            if n % 4:
                bad_divisions += 1
            u.append(n // 4)
    return u, bad_divisions


def inverse_components(u, c):
    return [sum(u[4 * c + w] * WCHAR[w][k] for w in range(4))
            for k in range(4)]


def inverse_mismatches(u, x, a, g, y):
    names = ("U0", "U1_FIXED", "U2_FIXED", "U3")
    mismatches = set()
    for c in range(64):
        expected = (x[c], 3 * a[c], g[c], y[c])
        got = inverse_components(u, c)
        for k in range(4):
            if got[k] != expected[k]:
                mismatches.add(names[k])
    return mismatches


def profile(x, t, s, alpha):
    values = []
    for ell in range(2):
        for j in range(4):
            total = 0
            for h in range(2):
                for b in range(4):
                    c = point(ell, h, j, b)
                    total += x[c] * CHARACTER[t][c] * char(s, h) * char(alpha, b)
            values.append((total, total // 4))
    return values


def expected_profiles():
    return {
        (1, 0): {4: -1, 5: -1, 6: -1, 7: 1},
        (0, 1): {1: 1, 3: -1, 4: 1, 6: 1},
        (1, 1): {1: -1, 3: -1, 5: 1, 7: -1},
        (0, 2): {2: -1, 3: 1, 4: 1, 5: 1},
        (1, 2): {2: 1, 3: 1, 6: 1, 7: -1},
        (0, 3): {1: -1, 2: 1, 4: 1, 7: 1},
        (1, 3): {1: 1, 2: -1, 5: 1, 6: 1},
    }


def check_profiles(x, t):
    zero = profile(x, t, 0, 0)
    check("profile_zero_column", all(n == 0 for n, _ in zero), t)
    for (s, alpha), expected in expected_profiles().items():
        got = profile(x, t, s, alpha)
        check("profile_integrality", all(n % 4 == 0 for n, _ in got), [t, s, alpha])
        vals = [v for _, v in got]
        actual = {i: v for i, v in enumerate(vals) if v}
        check("profile_exact_seven_columns", actual == expected, [t, s, alpha, actual])
        entries = list(actual.items())
        product = 1
        for _, value in entries:
            product *= value
        check("profile_flat_odd_sign", len(entries) == 4
              and all(abs(v) == 1 for _, v in entries)
              and xorsum(i for i, _ in entries) == 0 and product == -1,
              [t, s, alpha])


def boolean_spectrum(fun):
    values = [1 - 2 * fun(j, b) for j in range(4) for b in range(4)]
    return [sum(values[4 * j + b] * char(alpha, b) * char(beta, j)
                for j in range(4) for b in range(4))
            for beta in range(4) for alpha in range(4)]


def check_fixed_graph(a, g, x):
    check("physical_site_census", len(set(GRAPH)) == 16 and len(set(D0)) == 4
          and len(set(D3)) == 12 and len(set(EROW)) == 6
          and len(set(FROW)) == 2 and len(set(Z2)) == 6
          and len(set(Z4SITES)) == 18 and len(set(ZSITES)) == 24
          and len(set(SIGNSITES)) == 24 and REFERENCE_Z4 in Z4SITES)
    check("all_six_z2_literal_sites_and_signs",
          all(x[point(0, h, j, b)] == value for j, h, b, value in ZSPEC)
          and sum(x[c] != 0 for c in ZSITES) == 6)
    check("fixed_a_graph_and_phase", all(a[c] == (1 - 2 * phase(j, b))
          for j in range(4) for b in range(4) for c in [point(1, f(j), j, b)])
          and all(a[c] == 0 for c in range(64) if c not in GRAPH))
    check("fixed_g_graph_mates_E_Z", all(g[point(1, f(j), j, b)] == rho(b)
          and g[point(1, 1 ^ f(j), j, b)] == -2 * rho(b)
          for j in range(4) for b in range(4))
          and all(g[c] == 4 for c in FROW)
          and all(g[c] == -2 for c in EROW)
          and all(g[c] == 0 for c in ZSITES))
    check("rank_two_quadratic_polar", all(
          (f(j ^ dj) ^ f(j) ^ f(dj) ^ f(0))
          == (bit(j, 0) * bit(dj, 1) ^ bit(j, 1) * bit(dj, 0))
          for j in range(4) for dj in range(4)))
    for name, fun in (
        ("bent_f_plus_q", lambda j, b: f(j) ^ 1 ^ (bit(b, 0) * bit(b, 1))),
        ("bent_phase", lambda j, b: phase(j, b)),
        ("bent_phase_plus_f", lambda j, b: phase(j, b) ^ f(j)),
    ):
        spec = boolean_spectrum(fun)
        check(name, len(spec) == 16 and all(abs(v) == 4 for v in spec))
    ah, gh = direct_walsh(a), direct_walsh(g)
    check("fixed_a_walsh_all_magnitude_four", all(abs(v) == 4 for v in ah))
    check("fixed_g_walsh_all_four_mod_eight", all(v % 8 == 4 for v in gh))
    check("fixed_a_g_walsh_direct_vs_butterfly", ah == butterfly(a) and gh == butterfly(g))


def check_reference(a, g, base_x, base_y):
    base_xh = direct_walsh(base_x)
    for t in range(64):
        guard()
        xt = [base_x[c] * CHARACTER[t][c] for c in range(64)]
        yt = [base_y[c] * CHARACTER[t][c] for c in range(64)]
        u, rem = inverse(xt, a, g, yt)
        xh, yh = direct_walsh(xt), direct_walsh(yt)
        check("reference_256_integral", rem == 0 and len(u) == 256, t)
        check("reference_256_ternary", all(v in (-1, 0, 1) for v in u), t)
        check("reference_recovered_fixed_a_g_and_xy", not inverse_mismatches(u, xt, a, g, yt), t)
        check("reference_same_graph_relation", all(yt[c] == -a[c] * g[c] * xt[c] for c in GRAPH), t)
        check("reference_physical_energy_and_support", sum(v != 0 for v in u) == 116
              and sum(v * v for v in xt) == 56 and sum(v * v for v in yt) == 128
              and sum(v == 0 for v in yt) == 23, t)
        check("reference_J1", sum(u[4 * c] != 0 for c in range(64)) % 2 == 1, t)
        check("reference_all_walsh_direct_vs_butterfly", xh == butterfly(xt) and yh == butterfly(yt), t)
        expected_zeros = {t ^ (nu << 5) ^ (beta << 2)
                          for nu in (0, 1) for beta in range(4)}
        check("reference_x_walsh_caps_zero_and_shift", xh[t] == 0
              and set(xh) <= {-8, 0, 8} and {i for i, v in enumerate(xh) if v == 0} == expected_zeros
              and all(xh[k] == base_xh[k ^ t] for k in range(64)), t)
        check("reference_y_walsh_failure_and_mod8", yh[t] == 44
              and all(v % 8 == 4 for v in yh), t)
        p = [c for c in GRAPH if xt[c] < 0]
        off = D0 + Z2
        neg = [c for c in off if xt[c] < 0]
        check("reference_physical_XOR_and_cardinality", len(p) % 2 == 0
              and (len(p) // 2 + len(neg)) % 2 == 1
              and xorsum(p) == xorsum(off) and xorsum(Z2) == 0
              and sorted(sum(1 for c in Z2 if (c & 3) == b) for b in (1, 2, 3)) == [2, 2, 2], t)
        check_profiles(xt, t)
        if t == 0:
            by_b = [sum(u[4 * point(1, f(j), j, b)] != 0 for j in range(4))
                    for b in range(4)]
            groups = [sum(u[4 * c] != 0 for c in group)
                      for group in (FROW, D0, D3 + EROW, Z2, [REFERENCE_Z4])]
            check("reference_w0_concrete_census", by_b == [3, 2, 2, 0]
                  and groups == [2, 4, 8, 3, 1] and sum(by_b) + sum(groups) == 27,
                  [by_b, groups])
        OBS["reference_transports"] += 1
        emit({"kind": "reference_transport", "t": t, "x": xt, "y": yt,
              "u_c_major_w_minor": u, "x_walsh": xh, "y_walsh": yh,
              "nonzero_u": sum(v != 0 for v in u),
              "J": sum(u[4 * c] != 0 for c in range(64)) % 2})


def sign_value(mask, index):
    return 1 - 2 * bit(mask, index)


def partial_forms(mask, site, k, s, alpha, beta):
    # Formula (12), evaluated from sign variables, not from the y array.
    a1 = 0
    for j in range(4):
        sigma = 1 if j == 0 else -1
        kappa = 3 if j in (0, 3) else 0
        graph = 4 * sigma * char(s, f(j)) if alpha == kappa else 0
        dsum = sum(sign_value(mask, 3 * j + b - 1) * char(alpha, b)
                   for b in (1, 2, 3))
        a1 += char(beta, j) * (graph + 2 * char(s, 1 ^ f(j)) * dsum)
    a0 = 0
    for j in (1, 2, 3):
        a0 += 2 * char(beta, j) * sum(
            sign_value(mask, 12 + 2 * (j - 1) + h) * char(s, h) for h in (0, 1))
    for zindex, (j, h, b, _) in enumerate(ZSPEC):
        a0 += 2 * char(beta, j) * char(s, h) * sign_value(mask, 18 + zindex) * char(alpha, b)
    ell = bit(site, 5)
    h, j, b = bit(site, 4), (site >> 2) & 3, site & 3
    if ell != 0:
        raise ValueError("Z4 site is not in ell=0")
    a0 += 4 * k * char(beta, j) * char(s, h) * char(alpha, b)
    return a0, a1


def patterns():
    out, seen = [], set()
    def add(mask, label):
        if mask not in seen:
            seen.add(mask)
            out.append((mask, label))
    add(0, "all-positive")
    for i in range(24):
        add(1 << i, "single-%02d" % i)
    add(ALL_MASK, "all-negative")
    for label, lo, hi in (("all-D3", 0, 12), ("all-E", 12, 18), ("all-Z2", 18, 24)):
        add(sum(1 << i for i in range(lo, hi)), label)
    for j in range(4):
        add(7 << (3 * j), "D3-row-%d" % j)
    for j in range(3):
        add(3 << (12 + 2 * j), "E-pair-%d" % j)
        add(3 << (18 + 2 * j), "Z2-pair-%d" % j)
    for coordinate in range(6):
        mask = sum((1 << i) for i, c in enumerate(SIGNSITES) if bit(c, coordinate))
        add(mask, "coordinate-%d" % coordinate)
        add(ALL_MASK ^ mask, "coordinate-complement-%d" % coordinate)
    return out


def audit_case_shape(y, a, g, x, site, zsign, mask):
    return (all(y[c] == -a[c] * g[c] * x[c] for c in GRAPH)
            and all(y[c] == 2 * sign_value(mask, i) for i, c in enumerate(SIGNSITES))
            and [c for c in range(64) if abs(y[c]) == 4] == [site]
            and site in Z4SITES and y[site] == 4 * zsign
            and sum(v == 0 for v in y) == 23 and sum(v * v for v in y) == 128)


def test_sign_cases(a, g, x, pats):
    seen_sites, seen_zsigns = set(), set()
    for site in Z4SITES:
        for zsign in (-1, 1):
            for mask, label in pats:
                guard()
                y = make_y(a, g, x, mask, site, zsign)
                context = [site, zsign, label]
                check("sign_case_same_physical_y_shape", audit_case_shape(y, a, g, x, site, zsign, mask), context)
                u, rem = inverse(x, a, g, y)
                check("sign_case_t0_inverse_256", rem == 0 and all(v in (-1, 0, 1) for v in u)
                      and sum(v != 0 for v in u) == 116 and not inverse_mismatches(u, x, a, g, y), context)
                yh = direct_walsh(y)
                check("sign_case_walsh_direct_vs_butterfly", yh == butterfly(y), context)
                expected_j = 1 ^ (mask.bit_count() & 1)
                check("sign_case_y_walsh_J_residue", all(v % 8 == 4 * expected_j for v in yh), context)
                n_by_row = [((mask >> (3 * j)) & 7).bit_count() for j in range(4)]
                n = sum(n_by_row)
                contrast = n_by_row[0] + n_by_row[1] + n_by_row[2] - n_by_row[3]
                allcaps = True
                max_full = 0
                for s in range(2):
                    for alpha in range(4):
                        for beta in range(4):
                            a0, a1 = partial_forms(mask, site, zsign, s, alpha, beta)
                            low = (s << 4) | (beta << 2) | alpha
                            plus, minus = yh[low], yh[low | 32]
                            check("pair_forms_vs_direct_64_walsh", plus == a0 + a1 and minus == a0 - a1,
                                  context + [s, alpha, beta, a0, a1, plus, minus])
                            check("max_pair_identity_on_actual_values", max(abs(plus), abs(minus)) == abs(a0) + abs(a1),
                                  context + [s, alpha, beta])
                            if abs(plus) > 12 or abs(minus) > 12:
                                allcaps = False
                            max_full = max(max_full, abs(plus), abs(minus))
                if allcaps:
                    OBS["all_32_caps_cases"] += 1
                    if expected_j == 1:
                        OBS["all_32_caps_and_J1_cases"] += 1
                    n_ok = 1 <= n <= 7
                    contrast_ok = 2 <= contrast <= 8
                    check("capped_case_graph_negative_bounds", n_ok and contrast_ok,
                          context + [n_by_row, n, contrast])
                    if not (n_ok and contrast_ok):
                        OBS["capped_inequality_failures"] += 1
                    emit({"kind": "sampled_all_caps_case", "mask": mask, "label": label,
                          "site": site, "z4_sign": zsign, "J": expected_j,
                          "n_by_row": n_by_row, "n": n, "contrast": contrast,
                          "max_abs_y_walsh": max_full})
                for t in range(64):
                    guard()
                    nonzeros = 0
                    divisible = True
                    for c in range(64):
                        numerator = CHARACTER[t][c] * (x[c] + y[c]) + 3 * a[c] + g[c]
                        if numerator % 4:
                            divisible = False
                        if numerator // 4:
                            nonzeros += 1
                    check("sign_case_all_t_J_and_w0_integrality",
                          divisible and nonzeros % 2 == expected_j, context + [t, nonzeros])
                    OBS["sign_case_transports"] += 1
                seen_sites.add(site)
                seen_zsigns.add(zsign)
                OBS["sign_cases"] += 1
    check("all_eighteen_z4_sites_and_both_signs_visited",
          seen_sites == set(Z4SITES) and seen_zsigns == {-1, 1})
    check("all_24_single_sign_flips_visited", all(any(mask == (1 << i) for mask, _ in pats)
          for i in range(24)))


def permitted_scope(claim, original_all_callers_covered, v_supplied):
    if claim == "one_nonwitness":
        return True
    if claim == "global_no_go":
        return original_all_callers_covered
    if claim == "completed_V_witness":
        return v_supplied and original_all_callers_covered
    return False


def controls(a, g, x, y):
    # These controls are mutations or scope guards, not mathematical theorems.
    t = 1
    xt = [x[c] * CHARACTER[t][c] for c in range(64)]
    yt = [y[c] * CHARACTER[t][c] for c in range(64)]
    base_u, _ = inverse(x, a, g, y)
    wrong_u = [base_u[4 * c + w] * CHARACTER[t][c] for c in range(64) for w in range(4)]
    reasons = inverse_mismatches(wrong_u, xt, a, g, yt)
    check("control_reject_modulating_whole_u_fixed_ag", "U1_FIXED" in reasons and "U2_FIXED" in reasons,
          sorted(reasons))
    direct_xt, base_xh = direct_walsh(xt), direct_walsh(x)
    check("control_reject_wrong_character_frequency", direct_xt[0] == base_xh[t]
          and direct_xt[0] != base_xh[0], [direct_xt[0], base_xh[t], base_xh[0]])
    wrong_y = list(y)
    graph_site = GRAPH[0]
    wrong_y[graph_site] *= -1
    check("control_reject_wrong_graph_y", wrong_y[graph_site] != -a[graph_site] * g[graph_site] * x[graph_site])
    wrong_y = list(y)
    wrong_y[REFERENCE_Z4] = 0
    wrong_y[Z2[0]] = 4
    bad_sites = [c for c in range(64) if abs(wrong_y[c]) == 4]
    check("control_reject_Z4_on_Z2", len(bad_sites) == 1 and bad_sites[0] not in Z4SITES
          and x[bad_sites[0]] != 0, bad_sites)
    one_flip = make_y(a, g, x, 1, REFERENCE_Z4, 1)
    u_flip, rem = inverse(x, a, g, one_flip)
    check("control_one_sign_flip_gives_even_J", rem == 0
          and sum(u_flip[4 * c] != 0 for c in range(64)) % 2 == 0)
    a0, a1 = partial_forms(0, REFERENCE_Z4, 1, 0, 0, 0)
    actual = max(abs(a0 + a1), abs(a0 - a1))
    check("control_reject_false_max_pair_identity", actual == abs(a0) + abs(a1)
          and actual != max(abs(a0), abs(a1)), [a0, a1, actual])
    check("scope_guard_one_nonwitness_not_global_no_go",
          permitted_scope("one_nonwitness", False, False)
          and not permitted_scope("global_no_go", False, False))
    check("scope_guard_V_not_supplied", not permitted_scope("completed_V_witness", False, False))


def run():
    a, g, x = make_fixed()
    y = make_y(a, g, x, 0, REFERENCE_Z4, 1)
    check_fixed_graph(a, g, x)
    check_reference(a, g, x, y)
    controls(a, g, x, y)
    pats = patterns()
    OBS["distinct_sign_patterns"] = len(pats)
    OBS["pattern_labels"] = [label for _, label in pats]
    OBS["z4_sites_available"] = len(Z4SITES)
    test_sign_cases(a, g, x, pats)
    guard()


def main():
    state = "INCOMPLETE"
    reason = None
    try:
        run()
        state = "FAIL_BOUNDED_CHECKS" if FAILURES else "COMPLETE_BOUNDED_CHECKS_ONLY"
    except Incomplete as exc:
        reason = str(exc)
    except Exception as exc:
        state = "ERROR"
        reason = "%s: %s" % (type(exc).__name__, exc)
    finally:
        inequality_status = ("NOTTESTED_NO_SAMPLED_ALL32_CAPS_CASE" if OBS["all_32_caps_cases"] == 0
                             else ("FAIL_ON_SAMPLED_CAP_CASES" if OBS["capped_inequality_failures"]
                                   else "PASS_ON_SAMPLED_CAP_CASES_ONLY"))
        emit({"kind": "summary", "status": state, "reason": reason,
              "elapsed_monotonic_seconds": time.monotonic() - START,
              "counts": COUNTS, "observed": OBS,
              "total_failed_checks": FAILURES, "first_failures": FIRST_FAILURES,
              "capped_necessary_inequalities": inequality_status,
              "local_H_explicit_definition": "NOTTESTED_NOT_IN_FROZEN_PACKET",
              "exhaustive_24_sign_assignments": "NOTTESTED",
              "V_140_signs_and_256_odd_caps": "NOT_SUPPLIED_NOTTESTED",
              "original_gauge_T_rank_atom_caller": "NOT_RESTORED_NOTTESTED",
              "global_no_go_or_boolean_witness": "NOT_PROVED",
              "parent_disposition": "SEPARATE_REQUIRED"})
    return 0 if state == "COMPLETE_BOUNDED_CHECKS_ONLY" else (2 if state == "INCOMPLETE" else 1)


if __name__ == "__main__":
    sys.exit(main())
