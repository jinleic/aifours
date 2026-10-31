#!/usr/bin/env python3
"""Unexecuted FINITEAUTHOR source; exact rational arithmetic, stdout only."""
import json
import signal
from fractions import Fraction as F
from itertools import product


def need(condition, message):
    if not condition:
        raise ValueError(message)


def poly(values):
    a = [F(x) for x in values]
    need(bool(a), "empty polynomial")
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    n = max(len(a), len(b))
    return poly((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                for i in range(n))


def scale(a, c):
    return poly(c * x for x in a)


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly(out)


def power(a, n):
    out = poly([1])
    for _ in range(n):
        out = mul(out, a)
    return out


def shift(a, n):
    return poly([F(0)] * n + list(a))


def value(a, x):
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def parts(a):
    need(len(a) <= 8, "polynomial exceeds degree seven")
    c = list(a) + [F(0)] * (8 - len(a))
    return poly([c[0], -c[2], c[4], -c[6]]), poly([c[1], -c[3], c[5], -c[7]])


def pairing(q, a):
    fq, gq = parts(q)
    ea, oa = parts(a)
    return add(mul(fq, ea), shift(mul(gq, oa), 1))


def raw_polynomial_row(a):
    e, o = parts(a)
    return (e, shift(o, 1), scale(shift(e, 1), -1),
            scale(shift(o, 2), -1), shift(e, 2), shift(o, 3),
            scale(shift(e, 3), -1), scale(shift(o, 4), -1))


def check_raw_identity(q, a):
    cs = list(q) + [F(0)] * (8 - len(q))
    result = poly([0])
    for c, r in zip(cs, raw_polynomial_row(a)):
        result = add(result, scale(r, c))
    need(result == pairing(q, a), "physical pair / raw-row mismatch")


def member(d0, d1, a):
    out = list(a)
    out[0] += d0
    out[1] += d1
    return poly(out)


def routh_first_column(a):
    need(len(a) == 8 and a[-1] == 1, "Routh input not monic septic")
    desc = list(reversed(a))
    r0 = desc[0::2]
    r1 = desc[1::2]
    first = [r0[0], r1[0]]
    need(r0[0] > 0 and r1[0] > 0, "nonpositive initial Routh column")
    for _ in range(2, 8):
        need(r1[0] != 0, "zero Routh pivot")
        nxt = [(r1[0] * r0[j + 1] - r0[0] * r1[j + 1]) / r1[0]
               for j in range(3)] + [F(0)]
        need(nxt[0] > 0, "nonpositive Routh column")
        first.append(nxt[0])
        r0, r1 = r1, nxt
    return first


def derivative_at(nodes, i):
    z = F(1)
    for j, u in enumerate(nodes):
        if j != i:
            z *= nodes[i] - u
    need(z != 0, "repeated node")
    return z


def elementary(values, k):
    e = [F(0)] * (k + 1)
    e[0] = F(1)
    for x in values:
        for j in range(k, 0, -1):
            e[j] += x * e[j - 1]
    return e[k]


def raw_at(a, t):
    return [value(p, t) for p in raw_polynomial_row(a)]


def result_for_ray(name, spec, weights, A, Q, eta, expected_odd):
    need(len(spec) == len(weights) and all(w > 0 for w in weights),
         name + ": nonpositive weight")
    aggregate = [F(0)] * 8
    physical = F(0)
    bound = F(0)
    records = []
    fq, _ = parts(Q)
    for (t, a), w in zip(spec, weights):
        need(t > 0 and a[-1] == 1, name + ": invalid node/member")
        need(a[0] in (F(19, 20), F(21, 20)) and
             a[1] in (F(139, 20), F(141, 20)) and
             a[2:] == A[2:], name + ": not an actual K corner")
        need(a[0] == (F(19, 20) if value(fq, t) >= 0 else F(21, 20)),
             name + ": not the minimizing even endpoint for F_Q")
        r = raw_at(a, t)
        for j in range(8):
            aggregate[j] += w * r[j]
        p = value(pairing(Q, a), t)
        need(p == sum(Q[j] * r[j] for j in range(8)),
             name + ": actual physical pairing mismatch")
        physical += w * p
        bound += eta * w * (1 + t) ** 7
        records.append({"t": t, "actual_member_coefficients": a,
                        "odd_value": value(parts(a)[1], t), "weight": w,
                        "physical_pair": p})
    odd = [aggregate[j] for j in (1, 3, 5, 7)]
    need(odd == expected_odd, name + ": odd moments differ from requested ray")
    need(all(x <= 0 for x in odd), name + ": odd moment positive")
    need(physical == sum(Q[j] * aggregate[j] for j in range(8)),
         name + ": aggregate / physical mismatch")
    even_pair = sum(Q[j] * aggregate[j] for j in (0, 2, 4, 6))
    need(physical >= bound > 0 and even_pair > 0,
         name + ": strict physical/even pairing not certified")
    return {"name": name, "nodes": records, "raw_aggregate": aggregate,
            "odd_moments": odd, "even_pair": even_pair,
            "physical_pair_sum": physical, "eta_weighted_bound": bound}


def make_corner(t, sign, A, Q):
    f, _ = parts(Q)
    d0 = -F(1, 20) if value(f, t) >= 0 else F(1, 20)
    a = member(d0, F(sign, 20), A)
    odd = value(parts(a)[1], t)
    need(sign * odd > 0, "selected endpoint does not have intended odd sign")
    return a


def ray4(k, A, Q, eta):
    ts = [F(23, 100), F(230001, 1000000), F(1, 2), F(2)]
    signs = [-1, 1, -1, 1]
    spec = [(t, make_corner(t, s, A, Q)) for t, s in zip(ts, signs)]
    weights = []
    for i, (t, a) in enumerate(spec):
        o = value(parts(a)[1], t)
        numerator = elementary([x for j, x in enumerate(ts) if i != j], 3 - k)
        weights.append(numerator / (t * o * derivative_at(ts, i)))
    expected = [F(-1) if j == k else F(0) for j in range(4)]
    return result_for_ray("R4 omitted moment " + str(k), spec, weights, A, Q, eta, expected)


def ray5(orientation, A, Q, eta):
    if orientation == 1:
        ts = [F(1, 10), F(23, 100), F(230001, 1000000), F(1, 2), F(2)]
        signs = [1, -1, 1, -1, 1]
    else:
        ts = [F(23, 100), F(230001, 1000000), F(1, 2), F(2), F(20)]
        signs = [-1, 1, -1, 1, -1]
    spec = [(t, make_corner(t, s, A, Q)) for t, s in zip(ts, signs)]
    weights = [F(orientation) / (t * value(parts(a)[1], t) * derivative_at(ts, i))
               for i, (t, a) in enumerate(spec)]
    return result_for_ray("R5 orientation " + str(orientation), spec, weights,
                          A, Q, eta, [F(0)] * 4)


def ray_pair(A, Q, eta):
    t = F(23, 100)
    minus = make_corner(t, -1, A, Q)
    plus = make_corner(t, 1, A, Q)
    o_minus = value(parts(minus)[1], t)
    o_plus = value(parts(plus)[1], t)
    return result_for_ray("same-frequency opposite-odd P", [(t, minus), (t, plus)],
                          [o_plus, -o_minus], A, Q, eta, [F(0)] * 4)


def run():
    one_plus = poly([1, 1])
    A = power(one_plus, 7)
    q = shift(power(one_plus, 5), 1)
    qbad = mul(poly([1, 0, 1]), power(one_plus, 5))
    Q = add(A, scale(q, 10))
    eta = F(9, 10)
    need(A == poly([1, 7, 21, 35, 35, 21, 7, 1]), "A coefficients")
    need(q == poly([0, 1, 5, 10, 10, 5, 1]), "q coefficients")
    need(qbad == poly([1, 5, 11, 15, 15, 11, 5, 1]), "q_bad coefficients")
    need(Q == poly([1, 17, 71, 135, 135, 71, 17, 1]), "Q coefficients")
    need(Q == mul(power(one_plus, 5), poly([1, 12, 1])), "Q factorization")
    need(all(x > 0 for x in Q), "Q coefficient positivity")
    need(pairing(q, A) == shift(scale(power(one_plus, 5), 2), 1), "weak center identity")
    need(pairing(Q, A) == mul(power(one_plus, 5), poly([1, 22, 1])),
         "strict center identity")
    for n in (q, qbad, Q):
        check_raw_identity(n, A)

    weak_lower = [F(11, 10), F(7), F(191, 10), F(20), F(10), F(2)]
    weak_records = []
    for d0, d1 in product((-F(3, 20), F(3, 20)), repeat=2):
        b = member(d0, d1, A)
        p = pairing(q, b)
        check_raw_identity(q, b)
        need(len(p) == 7 and p[0] == 0, "weak P/t degree or zero endpoint")
        c = list(p[1:])
        need(all(x >= y for x, y in zip(c, weak_lower)), "weak coefficient lower bound")
        weak_records.append({"member_coefficients": b, "Pq_over_t_coefficients": c,
                             "routh_first_column": routh_first_column(b)})
    weak_min = [min(r["Pq_over_t_coefficients"][j] for r in weak_records) for j in range(6)]
    need(weak_min == weak_lower, "weak all-corner minima differ from stated bound")

    strict_lower = [F(1, 20), F(163, 10), F(443, 5), F(1991, 10),
                    F(4069, 20), F(1021, 10), F(207, 10), F(1, 10)]
    strict_records = []
    for d0, d1 in product((-F(1, 20), F(1, 20)), repeat=2):
        a = member(d0, d1, A)
        check_raw_identity(Q, a)
        margin = add(pairing(Q, a), scale(power(one_plus, 7), -eta))
        need(len(margin) == 8, "strict margin degree")
        need(all(x >= y for x, y in zip(margin, strict_lower)), "strict margin coefficient bound")
        strict_records.append({"member_coefficients": a,
                               "margin_coefficients": margin,
                               "routh_first_column": routh_first_column(a)})
    strict_min = [min(r["margin_coefficients"][j] for r in strict_records) for j in range(8)]
    need(strict_min == strict_lower and all(x > 0 for x in strict_min),
         "strict all-corner minima differ from stated bound")

    bad_center = pairing(qbad, A)
    need(bad_center == mul(power(poly([1, -1]), 2), power(one_plus, 5)),
         "unbuffered weak bad numerator identity")
    need(value(bad_center, F(1)) == 0 and value(parts(qbad)[0], F(1)) == 0 and
         value(parts(qbad)[1], F(1)) == 0, "q_bad must vanish at i")
    bbad = member(-F(1, 10), F(0), A)
    tbad = F(1001, 1000)
    bad_value = value(pairing(qbad, bbad), tbad)
    bad_f = value(parts(qbad)[0], tbad)
    need(F(17, 20) <= bbad[0] <= F(23, 20) and bbad[1] == F(7),
         "bad example not an L member")
    need(bad_f == F(799999, 200000000) and bad_value < 0,
         "invalid buffered weak premise was not rejected")
    bad_routh = routh_first_column(bbad)

    fq, gq = parts(q)
    need(value(fq, F(1)) == 4 and value(gq, F(1)) == -4, "buffer sign guard")
    upper = member(F(1, 20), F(1, 20), A)
    chosen = member(-F(1, 10), F(1, 10), upper)
    need(F(17, 20) <= chosen[0] <= F(23, 20) and
         F(137, 20) <= chosen[1] <= F(143, 20), "correct sign member is not in L")
    need(value(pairing(q, chosen), F(1)) ==
         value(pairing(q, upper), F(1)) - F(4, 5), "buffer sign identity")
    wrong_width_constant = upper[0] + F(3, 20)
    need(wrong_width_constant > F(23, 20), "off-box buffer-width guard")
    need(q[0] == 0 and len(q) == 7 and
         Q == scale(add(q, scale(A, F(1, 10))), 10), "endpoint/monic guard")
    need(value(pairing(q, A), F(0)) == 0, "unrepaired endpoint is not zero")

    consumers = [ray_pair(A, Q, eta)]
    consumers.extend(ray4(k, A, Q, eta) for k in range(4))
    consumers.extend(ray5(orientation, A, Q, eta) for orientation in (1, -1))
    return {
        "status": "PASS",
        "qualification": "finite exact physical checks; all-box stability uses the written connected-homotopy proof, not a corner-only theorem",
        "coefficient_convention": "ascending powers",
        "A": A, "q": q, "q_bad": qbad, "Q": Q, "eta": eta,
        "weak_center_pair_coefficients": pairing(q, A),
        "strict_center_pair_coefficients": pairing(Q, A),
        "L_corners": weak_records, "L_coefficientwise_Pq_over_t_minima": weak_min,
        "K_corners": strict_records, "K_coefficientwise_strict_margin_minima": strict_min,
        "Q_routh_first_column": routh_first_column(Q),
        "bad_example": {"member_coefficients": bbad, "t": tbad,
                        "F_q_bad": bad_f, "physical_pair": bad_value,
                        "routh_first_column": bad_routh},
        "buffer_sign_example": {"K_member": upper, "actual_L_member": chosen,
                                "off_box_wrong_width_constant": wrong_width_constant},
        "actual_corner_consumers": consumers,
        "scope_guards": ["No counterexample claimed for omission of the linear buffer.",
                         "No claim that a_star/a is positive real is needed or tested.",
                         "Weakness on a point or on K is not substituted for weakness on L.",
                         "Finite examples do not prove the universal ROOT statement or novelty."]
    }


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    return x


def timeout_handler(_signum, _frame):
    raise TimeoutError("55-second source deadline exceeded")


def main():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(55)
    try:
        report = run()
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, sort_keys=True))
        return 1
    finally:
        signal.alarm(0)
    print(json.dumps(encode(report), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
