#!/usr/bin/env python3
"""Independent, bounded, read-free finite author source; NOT a caller finder.

No input files, network, subprocesses, or filesystem writes.  JSONL goes to
stdout.  A parent must statically read and separately authorize execution.
"""

import itertools
import json
import signal
import sys
import time
from collections import Counter

TIME_LIMIT_SECONDS = 45.0
STOP = False
STOP_REASON = None
DEADLINE = None


class CheckFailure(Exception):
    pass


class Incomplete(Exception):
    pass


def on_signal(signum, _frame):
    global STOP, STOP_REASON
    STOP = True
    STOP_REASON = "signal-" + str(signum)


def guard():
    if STOP:
        raise Incomplete(STOP_REASON)
    if time.monotonic() >= DEADLINE:
        raise Incomplete("cooperative-45-second-deadline")


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def emit(event, **fields):
    print(json.dumps({"event": event, **fields}, separators=(",", ":"),
                     sort_keys=True))


def sign_dot(a, b):
    return 1 - 2 * ((a & b).bit_count() & 1)


def direct_walsh(values):
    n = len(values)
    need(n > 0 and n & (n - 1) == 0, "WALSH_DIMENSION")
    return [sum(value * sign_dot(k, x) for x, value in enumerate(values))
            for k in range(n)]


def butterfly_walsh(values):
    result = list(values)
    n = len(result)
    need(n > 0 and n & (n - 1) == 0, "WALSH_DIMENSION")
    width = 1
    while width < n:
        for base in range(0, n, 2 * width):
            for offset in range(width):
                left = result[base + offset]
                right = result[base + offset + width]
                result[base + offset] = left + right
                result[base + offset + width] = left - right
        width *= 2
    return result


def checked_walsh(values):
    direct = direct_walsh(values)
    need(direct == butterfly_walsh(values), "WALSH_IMPLEMENTATIONS_DISAGREE")
    return direct


def c_index(ell, h, j, b):
    return ell | (h << 1) | (j << 2) | (b << 4)


def f(z):
    j = z & 3
    return (j & 1) & ((j >> 1) & 1)


def r(z):
    j = z & 3
    b = (z >> 2) & 3
    return ((j & 1) & (b & 1)) ^ (((j >> 1) & 1) & ((b >> 1) & 1))


def q(z):
    b = (z >> 2) & 3
    return 1 ^ ((b & 1) & ((b >> 1) & 1))


def polar_f(z, k):
    return f(z ^ k) ^ f(z) ^ f(k) ^ f(0)


def is_graph(c):
    return (c & 1) == 1 and ((c >> 1) & 1) == f(c >> 2)


def xor_all(items):
    result = 0
    for item in items:
        result ^= item
    return result


def make_a_g_x0():
    a, g, x0 = [], [], []
    for c in range(64):
        ell = c & 1
        h = (c >> 1) & 1
        j = (c >> 2) & 3
        b = (c >> 4) & 3
        graph = is_graph(c)
        a.append((1 - 2 * r(c >> 2)) if graph else 0)
        if ell == 0 and b == 0:
            g.append(4 if j == 0 else -2)
        elif ell == 1:
            rho = 1 - 2 * q(c >> 2)
            g.append(rho * (1 if graph else -2))
        else:
            g.append(0)
        if graph:
            negative = (j == 0 and b == 1) or (j != 0 and b == 0)
            x0.append(-1 if negative else 1)
        elif ell == 1 and h != f(c >> 2) and b == 0:
            x0.append(-2)
        elif ell == 0 and h == 0 and j in (0, 1, 2) and b in (2, 3):
            x0.append(2 if b == 2 else -2)
        else:
            x0.append(0)
    return a, g, x0


def inverse(x, a, g, y):
    out = []
    for c in range(64):
        for w in range(4):
            s1 = sign_dot(w, 1)
            s2 = sign_dot(w, 2)
            numerator = x[c] + 3 * a[c] * s1 + g[c] * s2 + y[c] * s1 * s2
            need(numerator % 4 == 0, "NONINTEGRAL_PHYSICAL_INVERSE")
            out.append(numerator // 4)
    return out


def parity_j(u):
    return sum(u[4 * c] != 0 for c in range(64)) % 2


def make_y_u(x, a, g):
    z4 = c_index(0, 0, 3, 2)
    toggle = c_index(0, 0, 0, 2)
    y = []
    for c in range(64):
        if is_graph(c):
            y.append(-a[c] * g[c] * x[c])
        elif abs(g[c]) == 2:
            y.append(0 if x[c] else 2)
        elif g[c] == 0 and abs(x[c]) == 2:
            y.append(x[c])
        elif c == z4:
            y.append(4)
        else:
            y.append(0)
    need(abs(x[toggle]) == 2 and y[toggle] == x[toggle], "TOGGLE_BLOCK")
    u = inverse(x, a, g, y)
    toggled = parity_j(u) == 0
    if toggled:
        y[toggle] = -y[toggle]
        u = inverse(x, a, g, y)
    return y, u, toggled


def check_inverse(u, x, a, g, y):
    for c in range(64):
        for w in range(4):
            s1 = sign_dot(w, 1)
            s2 = sign_dot(w, 2)
            rhs = x[c] + 3 * a[c] * s1 + g[c] * s2 + y[c] * s1 * s2
            need(4 * u[4 * c + w] == rhs, "WRONG_INVERSE_NORMALIZATION")


def check_common_u(u, x, a, g, y):
    for c in range(64):
        block = u[4 * c:4 * c + 4]
        need(sum(block) == x[c], "COMMON_U_X")
        need(sum(block[w] * sign_dot(w, 1) for w in range(4)) == 3 * a[c],
             "COMMON_U_3A")
        need(sum(block[w] * sign_dot(w, 2) for w in range(4)) == g[c],
             "COMMON_U_G")
        need(sum(block[w] * sign_dot(w, 3) for w in range(4)) == y[c],
             "COMMON_U_Y")


def check_graph_relation(x, a, g, y):
    for c in range(64):
        if is_graph(c):
            need(y[c] == -a[c] * g[c] * x[c], "GRAPH_Y_RELATION")


def check_odd_j(u):
    need(parity_j(u) == 1, "J_NOT_ODD")


def check_y_residue(yhat):
    need(all(value % 8 == 4 for value in yhat), "Y_RESIDUE_NOT_4")


def check_x_cap(xhat):
    need(all(abs(value) <= 8 for value in xhat), "U0_CAP_NOT_PAID")


def check_balance(xhat, t):
    need(xhat[t] == 0, "SPECIFIED_BALANCE_NOT_ZERO")


def check_five_span(scope):
    need(scope == "five-span", "NOT_A_FIVE_SPAN_INPUT")


def no_unearned_witness_claim(xhat, v, original_caller_certificate):
    # This is only a necessary-condition guard, NEVER a full caller verifier.
    check_x_cap(xhat)
    need(v is not None, "COMPLEMENT_NOT_SUPPLIED")
    need(original_caller_certificate is not None, "ORIGINAL_CALLER_NOT_SUPPLIED")
    raise CheckFailure("FULL_CALLER_VERIFIER_NOT_PROVIDED")


def expect_reject(name, expected_reason, action):
    try:
        action()
    except CheckFailure as exc:
        need(str(exc) == expected_reason, "CONTROL_WRONG_REASON_" + name)
        emit("negative_control", name=name, rejected_for=expected_reason,
             classification="scope-or-mutation-control-not-a-counterexample")
        return
    raise CheckFailure("CONTROL_NOT_REJECTED_" + name)


def classify_blocks(x, a, g, y):
    classes = Counter()
    for c in range(64):
        if is_graph(c):
            need(abs(a[c]) == 1 and abs(g[c]) == 1 and abs(x[c]) == 1
                 and abs(y[c]) == 1, "GRAPH_BLOCK_FORM")
            classes["S"] += 1
        elif g[c] == 4:
            need(x[c] == y[c] == 0 and a[c] == 0, "FULL_BLOCK_FORM")
            classes["F"] += 1
        elif abs(g[c]) == 2:
            need(a[c] == 0, "D_A_NONZERO")
            if abs(x[c]) == 2 and y[c] == 0:
                classes["D0"] += 1
            else:
                need(x[c] == 0 and abs(y[c]) == 2, "D_BLOCK_FORM")
                classes["D3"] += 1
        else:
            need(a[c] == 0 and g[c] == 0, "Z_FIXED_FIBRES")
            if x[c] == 0 and y[c] == 0:
                classes["Z0"] += 1
            elif abs(x[c]) == 2 and abs(y[c]) == 2:
                classes["Z2"] += 1
            else:
                need(x[c] == 0 and abs(y[c]) == 4, "Z_BLOCK_FORM")
                classes["Z4"] += 1
    need(dict(classes) == {"S": 16, "F": 2, "D0": 4, "D3": 18,
                           "Z2": 6, "Z4": 1, "Z0": 17}, "BLOCK_COUNTS")
    return dict(classes)


def check_c(x):
    p = [c for c in range(64) if is_graph(c) and x[c] < 0]
    w = [c for c in range(64) if not is_graph(c) and abs(x[c]) == 2]
    n = [c for c in w if x[c] < 0]
    xp, xw = xor_all(p), xor_all(w)
    need(len(p) % 2 == 0 and (len(p) // 2 + len(n)) % 2 == 1
         and xp == xw and len(w) == 10, "PHYSICAL_C")
    return {"P": p, "W": w, "N": n, "P_count": len(p),
            "N_count": len(n), "XOR_P": xp, "XOR_W": xw}


def check_graph_y_characters(y):
    slopes = []
    for j in range(4):
        values = [y[c_index(1, f(j | (b << 2)), j, b)] for b in range(4)]
        need(all(abs(value) == 1 for value in values), "GRAPH_Y_SIGN")
        spectrum = checked_walsh(values)
        peaks = [k for k in range(4) if abs(spectrum[k]) == 4]
        need(len(peaks) == 1 and all(spectrum[k] == 0 for k in range(4)
                                     if k != peaks[0]), "GRAPH_Y_NOT_CHARACTER")
        slopes.append({"j": j, "values_by_b": values, "slope": peaks[0],
                       "signed_peak": spectrum[peaks[0]]})
    return slopes


def l_frequency(eta):
    return ((eta & 1) << 1) | ((eta & 2) << 3) | ((eta & 4) << 3)


def m_frequency(q0):
    return (q0 & 1) | ((q0 & 6) << 1)


def profile(x, t, L, eta):
    result = []
    for m_index in range(8):
        m = c_index(m_index & 1, 0, m_index >> 1, 0)
        total = sum(x[m ^ v] * sign_dot(t, m ^ v)
                    * sign_dot(eta, ((v >> 1) & 1) | (((v >> 4) & 3) << 1))
                    for v in L)
        need(total % 4 == 0, "PROFILE_NOT_INTEGRAL")
        result.append(total // 4)
    return result


def check_profiles(x, t, L, xhat):
    profiles = []
    for eta in range(8):
        z = profile(x, t, L, eta)
        zh = checked_walsh(z)
        for q0 in range(8):
            need(xhat[t ^ l_frequency(eta) ^ m_frequency(q0)] == 4 * zh[q0],
                 "PROFILE_FULL_WALSH_IDENTITY")
        if eta == 0:
            need(z == [0] * 8, "PRESCRIBED_ZERO_PROFILE")
        profiles.append({"eta": eta, "z": z, "energy": sum(v * v for v in z),
                         "z_walsh": zh,
                         "off_zero_profile_accepted": eta != 0 and
                         all(abs(v) == 2 for v in zh)})
    need(any(not p["off_zero_profile_accepted"] for p in profiles[1:]),
         "NONWITNESS_MUST_FAIL_A_PROFILE")
    return profiles


def energy_four_vectors():
    for position in range(8):
        for value in (-2, 2):
            vec = [0] * 8
            vec[position] = value
            yield vec
    for positions in itertools.combinations(range(8), 4):
        for signs in itertools.product((-1, 1), repeat=4):
            vec = [0] * 8
            for position, value in zip(positions, signs):
                vec[position] = value
            yield vec


def enumerate_profiles():
    total = accepted = singles = fours = flats = odd_flat_accepts = 0
    affine_flats = set()
    for vec in energy_four_vectors():
        guard()
        total += 1
        need(sum(v * v for v in vec) == 4, "ENUMERATION_ENERGY")
        support = tuple(i for i, value in enumerate(vec) if value)
        spectrum = checked_walsh(vec)
        observed = all(abs(value) == 2 for value in spectrum)
        if len(support) == 1:
            singles += 1
            category = "single-pm2"
            predicted = True
        else:
            fours += 1
            need(len(support) == 4 and all(abs(vec[i]) == 1 for i in support),
                 "ENUMERATION_SUPPORT")
            is_flat = xor_all(support) == 0
            sign_product = 1
            for i in support:
                sign_product *= vec[i]
            if is_flat:
                affine_flats.add(support)
                flats += 1
            predicted = is_flat and sign_product == -1
            if predicted:
                odd_flat_accepts += 1
            category = "four-pm1-flat" if is_flat else "four-pm1-nonflat"
        need(observed == predicted, "PROFILE_CLASSIFICATION_MISMATCH")
        accepted += int(observed)
        emit("energy4_vector", vector=vec, walsh=spectrum, category=category,
             accepted=observed)
    need((total, singles, fours) == (1136, 16, 1120), "ENUMERATION_COUNTS")
    need(len(affine_flats) == 14 and flats == 14 * 16, "AFFINE_FLAT_COUNTS")
    need(odd_flat_accepts == 14 * 8 and accepted == 16 + 14 * 8,
         "ACCEPTED_PROFILE_COUNTS")
    emit("energy4_summary", total=total, single_pm2=singles, four_pm1=fours,
         affine_two_flats=len(affine_flats), accepted=accepted,
         rejected=total - accepted, accepted_flat_signings=odd_flat_accepts)


def run():
    need(len(sys.argv) == 1, "NO_ARGUMENTS_ACCEPTED")
    emit("start", role="finite-source-author", child_scientific_run="NOT_RUN_BY_AUTHOR",
         deadline_seconds=TIME_LIMIT_SECONDS, ordering="c=ell+2h+4j+16b; u-index=4c+w")
    a, g, x0 = make_a_g_x0()
    S = [c for c in range(64) if is_graph(c)]
    need(len(S) == 16, "GRAPH_SIZE")

    bent_results = {}
    for name, fun in (("f+q", lambda z: f(z) ^ q(z)), ("r", r),
                      ("r+f", lambda z: r(z) ^ f(z))):
        guard()
        truth = [fun(z) for z in range(16)]
        wh = checked_walsh([1 - 2 * v for v in truth])
        need(all(abs(v) == 4 for v in wh), "BENT_" + name)
        bent_results[name] = {"truth_z_order": truth, "walsh": wh}
    K = [k for k in range(16) if all(polar_f(z, k) == 0 for z in range(16))]
    need(K == [0, 4, 8, 12], "RADICAL_K")
    need({(k >> 2) & 3 for k in K} == set(range(4)), "K_B_PROJECTION")
    H = []
    for k in K:
        derivative = f(k) ^ f(0)
        need(all((f(z ^ k) ^ f(z)) == derivative for z in range(16)),
             "RADICAL_DERIVATIVE")
        H.append((derivative << 1) | (k << 2))
    L = sorted(H + [h ^ 2 for h in H])
    need(len(set(H)) == 4 and len(set(L)) == 8, "H_L_DIMENSIONS")
    need(all((u ^ v) in H for u in H for v in H), "H_LINEAR")
    Lperp = [xi for xi in range(64) if all(sign_dot(xi, v) == 1 for v in L)]
    need(len(Lperp) == 8, "L_PERP_SIZE")
    d0 = [c for c in range(64) if abs(g[c]) == 2 and abs(x0[c]) == 2]
    need(len(d0) == 4 and len({min(c ^ v for v in L) for c in d0}) == 4,
         "D0_NOT_FOUR_DISTINCT_L_COSETS")
    for h in (0, 1):
        for j in range(4):
            cell = {c_index(0, h, j, 0) ^ v for v in H}
            need({(c >> 4) & 3 for c in cell} == set(range(4)), "H_CELL_B_ROWS")
    ahat, ghat = checked_walsh(a), checked_walsh(g)
    need(all(abs(v) == 4 for v in ahat), "ACTUAL_A_WALSH")
    need(sum(abs(v) == 4 for v in ghat) == 4 and
         all(abs(v) in (4, 12) for v in ghat) and
         all(v == 4 for v in ghat if abs(v) == 4), "ACTUAL_G_WALSH")
    emit("physical_fixed_data", a=a, g=g, x0=x0, a_walsh=ahat, g_walsh=ghat,
         graph=S, K_z=K, H_c=H, L_c=L, L_perp=Lperp, D0=d0,
         K_b_projection=sorted({k >> 2 for k in K}), bent=bent_results)

    x0hat = checked_walsh(x0)
    b1 = c_index(0, 0, 0, 2)
    need(x0hat[b1] == -16 and x0hat[0] == 0, "BASE_SPIKE_OR_DC")
    base_c = check_c(x0)
    need(base_c["P_count"] == 4 and base_c["N_count"] == 7 and
         base_c["XOR_P"] == 18 and base_c["XOR_W"] == 18, "BASE_C_COUNTS")
    saved = None
    for t in range(64):
        guard()
        x = [x0[c] * sign_dot(t, c) for c in range(64)]
        y, u, toggled = make_y_u(x, a, g)
        check_inverse(u, x, a, g, y)
        check_common_u(u, x, a, g, y)
        check_graph_relation(x, a, g, y)
        check_odd_j(u)
        need(all(value in (-1, 0, 1) for value in u), "NONTERNARY_U")
        need(sum(value != 0 for value in u) == 116, "U_SUPPORT")
        need(sum(value * value for value in x) == 56, "X_ENERGY")
        need(sum(value * value for value in y) == 128, "Y_ENERGY")
        need(sum(value == 0 for value in y) == 23, "Y_SPATIAL_ZEROS")
        classes = classify_blocks(x, a, g, y)
        c_record = check_c(x)
        xhat, yhat = checked_walsh(x), checked_walsh(y)
        need(all(xhat[k] == x0hat[k ^ t] for k in range(64)), "CARRIED_SHIFT")
        need(all(v % 8 == 0 for v in xhat), "X_DIVISIBILITY")
        need(all(xhat[t ^ xi] == 0 for xi in Lperp), "TRANSPORTED_ZERO_FLAT")
        check_balance(xhat, t)
        need(xhat[t ^ b1] == -16, "TRANSPORTED_SPIKE")
        check_y_residue(yhat)
        rows = [sum(1 for c in range(64) if (c & 1) == 0 and g[c] == 0
                    and abs(x[c]) == 2 and ((c >> 4) & 3) == b)
                for b in (1, 2, 3)]
        need(rows == [0, 3, 3], "NONWITNESS_Z2_ROWS")
        characters = check_graph_y_characters(y)
        profiles = check_profiles(x, t, L, xhat)
        emit("carried_physical_case", t=t, x=x, y=y, u=u, x_walsh=xhat,
             y_walsh=yhat, toggle_applied=toggled, J=parity_j(u), classes=classes,
             C=c_record, z2_rows_beta_gamma_betagamma=rows,
             graph_y_characters=characters, profiles=profiles,
             theorem3_mod16="NOT_TESTED: U0 cap fails; no theorem3 premise claimed")
        if t == 0:
            saved = (x, y, u, xhat, yhat)
    need(saved is not None, "BASE_CASE_MISSING")
    x, y, u, xhat, yhat = saved
    check_five_span("five-span")
    expect_reject("wrong-normalization", "WRONG_INVERSE_NORMALIZATION",
                  lambda: check_inverse([2 * value for value in u], x, a, g, y))
    expect_reject("free-balance-instead-of-specified-t", "SPECIFIED_BALANCE_NOT_ZERO",
                  lambda: check_balance(xhat, b1))
    expect_reject("independent-u", "COMMON_U_G",
                  lambda: check_common_u([0] * 256, x, a, g, y))
    bad_y = list(y)
    bad_y[S[0]] = -bad_y[S[0]]
    expect_reject("graph-y-relation", "GRAPH_Y_RELATION",
                  lambda: check_graph_relation(x, a, g, bad_y))
    even_y = list(y)
    toggle = c_index(0, 0, 0, 2)
    even_y[toggle] = -even_y[toggle]
    even_u = inverse(x, a, g, even_y)
    need(parity_j(even_u) == 0, "EVEN_J_MUTATION_DID_NOT_TOGGLE")
    even_yhat = checked_walsh(even_y)
    need(all(v % 8 == 0 for v in even_yhat), "EVEN_J_RESIDUE_PREMISE")
    expect_reject("odd-J", "J_NOT_ODD", lambda: check_odd_j(even_u))
    expect_reject("U3-residue", "Y_RESIDUE_NOT_4", lambda: check_y_residue(even_yhat))
    expect_reject("actual-U0-cap", "U0_CAP_NOT_PAID", lambda: check_x_cap(xhat))
    expect_reject("six-span-is-not-five-span", "NOT_A_FIVE_SPAN_INPUT",
                  lambda: check_five_span("six-span"))
    expect_reject("false-witness-scope-guard", "U0_CAP_NOT_PAID",
                  lambda: no_unearned_witness_claim(xhat, None, None))
    enumerate_profiles()
    emit("complete", actual_nonwitness_cases=64, energy4_vectors=1136,
         theorem3_mod16="NOT_TESTED", V="NOT_SUPPLIED", original_caller="NOT_RESTORED",
         no_five_span_exclusion=True, no_witness_claim=True)


def main():
    global DEADLINE
    DEADLINE = time.monotonic() + TIME_LIMIT_SECONDS
    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    try:
        run()
    except Incomplete as exc:
        emit("INCOMPLETE", reason=str(exc))
        return 2
    except CheckFailure as exc:
        emit("FAIL", reason=str(exc))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
