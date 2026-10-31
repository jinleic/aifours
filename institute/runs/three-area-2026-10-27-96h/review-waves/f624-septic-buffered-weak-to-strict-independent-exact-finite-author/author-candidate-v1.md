# Independent exact finite author: actual buffered septic weak/strict consumers

**Status: AUTHOR CANDIDATE, UNADOPTED.** This is a concrete, exact physical example and a source design, not a proof of universal septic synthesis, the common-three-root condition, harmonic analysis, the universal all-box ROOT statement, novelty, or the f604 theorem. No scientific program, test, build, solver, numerical calculation, or source below was run in this child. The displayed identities and inequalities are written algebra, not observed executable output. Any PASS is prospective only and requires parent execution plus independent review and disposition.

## 1. Actual boxes and the weak separator

All polynomial arrays in this record are in ascending powers of `s` unless explicitly identified as polynomials in `t`. Set

- `A(s)=(s+1)^7`, coefficients `[1,7,21,35,35,21,7,1]`;
- `q(s)=s(s+1)^5`, coefficients `[0,1,5,10,10,5,1,0]`, so `q_0=q_7=0`;
- `K={A+d0+d1*s : |d0|,|d1|<=1/20}`;
- `L={A+d0+d1*s : |d0|,|d1|<=3/20}`.

Thus L is exactly the K box enlarged by `h0=h1=1/10`, independently in both coefficient directions, and all other coefficients are fixed. Both have four actual distinct coefficient corners. For an actual `a`, use the physical pairing `P(q,a;t)=F_q(t)E_a(t)+t G_q(t)O_a(t)`, with the frozen packet's even/odd convention and `t=omega^2`. For this q,

```
F_q = -5t + 10t^2 - t^3,
G_q = 1 - 10t + 5t^2,
P(q,A;t) = 2t(1+t)^5.
```

For any `b=A+d0+d1*s`, the **full** physical pairing is

```
P(q,b;t)/t = [2-5d0+d1] + [10+10d0-10d1]t
           + [20-d0+5d1]t^2 + 20t^3+10t^4+2t^5.
```

At the four L corners, ordered by `(d0,d1)=(-,-),(-,+),(+,-),(+,+)` with each magnitude `3/20`, these complete coefficient vectors are respectively

```
[13/5, 10, 97/5, 20, 10, 2]
[29/10, 7, 209/10, 20, 10, 2]
[11/10, 13, 191/10, 20, 10, 2]
[7/5, 10, 103/5, 20, 10, 2].
```

Every coefficient is positive. Each coefficient is affine in `(d0,d1)`, so its minimum over the entire actual L box is attained at a corner. The common coefficientwise lower bound is `[11/10,7,191/10,20,10,2]`. Hence `P(q,b;t)>0` for **all** `b in L` and `t>0`, and `P(q,b;0)=0`. This is not a grid claim; it is a polynomial coefficient proof over the entire nonnegative half-axis and all L members.

### Stability of every L member, not merely corners

For each actual `b=A+d0+d1*s`, use the connected path `b_lambda=A+lambda(d0+d1*s)`, `0<=lambda<=1`. It stays inside L. The preceding strict positivity at every positive t forbids `b_lambda(i omega)=0` for any nonzero real omega, because such a zero would force the physical pairing to vanish. At zero, `b_lambda(0)>=17/20>0`. The polynomials remain monic of fixed degree, so no root can cross the imaginary axis through infinity along this compact coefficient path. Since A is strictly Hurwitz, continuity of roots makes **every** L member strictly Hurwitz. Consequently K is eligible too. Four-corner Routh checks in the proposed source are additional exact diagnostics; they are not used as a corner-only stability theorem for the box.

## 2. One explicitly normalized strict numerator on the original K

Take the frozen theorem's actual reference `a_*=A` and `delta=1/10`. Since `q_7=0`, the mandatory normalization gives

```
Q=(q+(1/10)A)/(1/10)=A+10q
 =(s+1)^5(s^2+12s+1),
Q coefficients=[1,17,71,135,135,71,17,1].
```

It is monic and strictly Hurwitz: `(s+1)^5` is stable and the two roots of `s^2+12s+1` are negative (`-6 +/- sqrt(35)`). Its coefficients are strictly positive. The physical center pairing is

```
P(Q,A;t)=(1+t)^5(t^2+22t+1).
```

For every actual `a=A+d0+d1*s` in K,

```
F_Q=1-71t+135t^2-17t^3,
G_Q=17-135t+71t^2-t^3,
P(Q,a;t) - (9/10)(1+t)^7
 = (1/10)(1+t)^7 + 20t(1+t)^5 + d0 F_Q + d1 t G_Q.
```

The full coefficientwise bound for all four actual K corners, hence for all K by affine dependence, is

```
[1/20, 163/10, 443/5, 1991/10,
 4069/20, 1021/10, 207/10, 1/10].
```

Every entry is positive, so the polynomial on the left is positive on `[0,infinity)`. In particular the same actual stable monic Q satisfies

```
P(Q,a;t) >= (9/10)(1+t)^7 > 0   for every a in K and t>=0.
```

This proves a **single concrete** two-parity box instance, including the zero and compactified-infinity endpoints. No assumption that `a_*/a` itself is positive real is used. In contrast, q by itself has `P(q,A;0)=0` and `q_7=0`; one cannot simply omit delta or call q a monic septic. The 9/10 margin here is a separate explicit lower bound, not the implicit general delta choice in f604.

## 3. Actual finite physical consumers: P, all R4 placements, both R5 orientations

The following are exact selected source-design instances, not a proof by finite sampling of every ray. Let `O_a=7-35t+21t^2-t^3+d1`, and at each node take `d1=+1/20` for a desired positive odd value and `d1=-1/20` for a desired negative value. Independently choose the **actual K endpoint** `d0=-1/20` when `F_Q(t)>=0`, otherwise `d0=+1/20`; this is the actual even endpoint minimizing `F_Q(t)E_a(t)`. Therefore every node is an actual K corner, not a freely chosen parity marker. In particular `O_A(23/100)=48733/1000000`, so both signs occur there. The nearby node `230001/1000000` also has the required positive upper endpoint; a derivative bound on this tiny interval establishes it without floating point.

* **P:** at `t=23/100`, use the negative and positive odd endpoints, with respective positive weights `98733/1000000` and `1267/1000000`. All four signed odd moments cancel exactly.
* **R4:** use ascending nodes `23/100, 230001/1000000, 1/2, 2` with odd signs `(-,+,-,+)`. For each `k=0,1,2,3`, let `H4(x)=product_i(x-t_i)` and use the positive weights `e_(3-k)(other nodes)/(t_i O_i H4'(t_i))`. The signed odd-moment vector is exactly `-e_k`; every other odd moment is zero.
* **R5, positive orientation:** nodes `1/10, 23/100, 230001/1000000, 1/2, 2` have signs `(+,-,+,-,+)`; weights are `1/(t_i O_i H5'(t_i))`.
* **R5, negative orientation:** nodes `23/100, 230001/1000000, 1/2, 2, 20` have signs `(-,+,-,+,-)`; weights are `-1/(t_i O_i H5'(t_i))`.

All listed weights are positive because the sign of `H_n'(t_i)` alternates. Lagrange interpolation gives the R4 moment identity and the four zero odd moments for each R5; the code below constructs the actual rational member arrays, weights and all eight raw-row aggregates and checks them exactly. For any one of these positive-weight families, or indeed any finite actual family with all four signed odd moments nonpositive, the physical bound in Section 2 gives a strictly positive aggregate Q pairing. Since Q's odd coefficients are strictly positive and the signed odd moments are nonpositive, subtracting that nonpositive odd contribution leaves a **strictly positive even pairing**. This is the requested physical consumer mechanism. It does not establish the separate universal common-triple condition B.

## 4. A real weak-premise trap, and scope guards

Set `q_bad=(s^2+1)(s+1)^5`, coefficients `[1,5,11,15,15,11,5,1]`. On the eligible **point box** `{A}`,

```
P(q_bad,A;t)=(1-t)^2(1+t)^5 >= 0,
q_bad(i)=0.
```

Thus an unbuffered weak physical pair on one stable denominator does not exclude a positive imaginary-axis zero. This does **not** refute the buffered theorem: the same q_bad does not satisfy its L-wide weak premise. The actual member `b_bad=A-1/10` lies in L, and at `t=1001/1000`,

```
F_q_bad(t)=799999/200000000 > 0,
P(q_bad,b_bad;t)=(1/1000000)(2001/1000)^5 - 799999/2000000000 < 0.
```

For a written exact comparison, the first term is less than `243/1000000=486000/2000000000`, which is less than the subtracted term. No claim is made that q_bad is weak on the full nondegenerate K.

The sign rule is also an actual-member issue. At `t=1`, `F_q=4` and `G_q=-4`. Starting from the K upper corner `(d0,d1)=(1/20,1/20)`, the correct perturbations `(-1/10,+1/10)` remain in L and subtract `4/5` from the physical pair. Reversing both signs remains in L but adds `4/5`; it does **not** give the lower-bound inequality. A different mistaken use of L's full half-width `3/20` as an additional buffer at that K upper constant gives constant `6/5>23/20`, i.e. a nonmember of L. Both signs of the legitimate `1/10` perturbations are actually allowed; it would be wrong to call the opposite legitimate sign automatically off-box.

**SCOPE GUARDS ONLY, no counterexample asserted:** omitting the linear buffer destroys the stated two-dimensional rectangle argument but has not been shown here to make the theorem false; no example disproves `a_*/a` positive real for this K; and a weak property on a point or only on K may not replace the theorem's universal weak property on L. No new general counterexample is claimed for these guards.

## 5. Full exact source, inputs, run contract and outputs

The complete source below is also provided as `exact-finite-source-v1.py` in this wave. It has been **authored only, never executed**. It uses only Python standard-library `Fraction`, polynomial arithmetic, exact Routh first columns, and stdout JSON; it opens no data/output file, makes no network connection, launches no child, installs nothing, and deletes nothing. It has a 55-second POSIX alarm. There are no floating-point sign decisions or frequency grids. The script prints the full actual corner member arrays and full polynomial coefficient arrays, the exact point trap, and actual P/R4/R5 member arrays, weights, all eight aggregate coordinates, and physical/even pairings. It explicitly returns FAIL on any failed check. The mathematical all-L stability proof remains Section 1's path argument, not a finite-corner extrapolation.

Proposed **parent-only** one-shot argv, after parent source audit and authorization:

```
python3 -I -B /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f624-septic-buffered-weak-to-strict-independent-exact-finite-author/exact-finite-source-v1.py
```

No executable output or duration is observed. If it terminates with PASS, that is only a finite exact execution result for the listed objects; it is not independent source review, proof of harmonic analysis, ROOT, or novelty. Capture the actual stdout/exit independently and do not represent this expectation as a run.

```python
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
        ts = [F(23, 100), F(230001, 1000000), F(1, 2), F(20)]
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
```

## 6. Chronology, exposure and exact acceptance boundary

1. Read the memory summary and relevant written-acceptance/review/round skills, then the complete manifest, freeze and dispatch receipts, parent-live metadata, and all 15 declared control records through their endings. Parent metadata supplies the assigned hash bindings; this child did not recompute them.
2. Sent the direct pre-body ACK to `agent://Main` before opening the packet. There was no mathematical derivation before that ACK.
3. Read the ordered literal packet in raw windows of at most 20 lines: packet lines 1–581, including S1's logical line 533 and S2's line 46 and their endings. Only after the complete read did the written algebra and fresh example/source design above begin.
4. No links in the packet were followed. No external research, source import, sibling material, held episode, held consumer, scientific execution, test, build, lint, solver, or external model CLI was used. The two new files are exclusive to this wave. No claim of clean cognition or independent-family provenance is made.
5. Parent-supplied pins: manifest `27f19d22bc791e4b64a52023d7c14b5842680e4fbeeae874f2aca1dae5d3a6f3`, receipt `12136541781625b50ac3ba70dbb572a7078154f8187b79fecd776cb1da44ed9f`, packet `2c39dc8e13a15d5f00f5d29083f3461f1d87d6ce1bbcaf57101f2e7c61749f30`; S1 `870f63769e11b298073a3e23fc48684391789e61f40ea0330326f55bb3b84c3f`; S2 `5f35c9a1b1db95a89f928e7e7566492d29e05555d0b08822cfaf2f2a78ab58ae`.

Independent source audit and any parent-only one-shot run remain open; no such result was supplied by this child. The f604 universal proof, its harmonic step and ROOT equivalence require their own assigned gates. No actual strict-negative universal counterexample, worldwide novelty assessment, independent-family/human review, or formal/kernel verification is provided.
