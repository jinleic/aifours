# F445 — independent exact finite-check deliverable

**Status: COMPLETE SOURCE / NOT RUN / NOT ADOPTED.**

The implementation below is independently authored from the frozen written formulas. I did not read, import, execute, or follow the original author’s program or its outcome.

A higher-priority role instruction restricts Bash to read-only version-control review commands. I therefore did **not** execute a scientific interpreter, write a script, or bypass that restriction through another tool. There is no execution transcript, measured runtime, or finite PASS to report.

## 1. Input binding and chronology

I read the complete manifest, freeze receipt, dispatch receipt, parent live-metadata supply, and all eight status/permission controls **before** reading the scientific packet. I then read packet LF 1–535 in ascending, contiguous, raw chunks of at most 20 LF, including its ending.

The following metadata is **parent-attributed**, not independently hashed or clocked by me:

- Manifest SHA-256: `d7a8f08ca51918c5867005c57ac632361055b3f3d543caa0709e905f4c59c246`.
- Freeze-receipt SHA-256: `61099c4028ead898c54adf0f3b36e637d681084ac2e85ffbf701b1cdb4268c3b`.
- Packet SHA-256: `09ea047253eade731283d256f8745a5f7739e110e5db51b37f3502c5e572b0e4`.
- Scientific source: F434 `review-v1.md`, whole-file SHA-256 `904626d4371b26e5a007313d186ff8bdbc89827df68dd2a76d480c32659f87d8`, **only LF 1–533**, as reproduced in the packet.
- Parent live observation: `2026-10-30T11:31:28-0700 PDT`. This is not my native start or execution time.

F439’s entire mathematical review episode and consumers remain **HELD/ZERO/NONINPUT**. The other quarantined PH, AME, CORE, privacy, and L1 payloads and their consumers were likewise not used as scientific premises.

This was the **FINITE** assignment, not a WRITTEN_ONLY assignment. Its expressly permitted selected controls are fully specified below; none is being represented as an admissible selected diagnostic for a written-only reviewer.

## 2. Actual inputs, not formal shadows

All polynomial coefficient arrays in the source are in **ascending powers of \(s\)**.

The actual numerator is
\[
q=(4,15,11,23,13/2,9,1,1).
\]

Its independently reconstructed physical parity is
\[
q(i\omega)=F(t)+i\omega G(t),\qquad t=\omega^2,
\]
where
\[
F=(4,-11,13/2,-1),\qquad G=(15,-23,9,-1).
\]

The core coefficient bounds, in order \(a_0,\ldots,a_6\), are
\[
[3,5],\ [1197/80,15],\ [11,11],\
[23,467/20],\ [13/2,13/2],\
[179/20,9],\ [1,1].
\]
The leading coefficient is exactly \(a_7=1\).

The maximum enlargement is
\[
m=\frac{65}{4096},\qquad
\gamma=\frac{65}{481890304},\qquad
\varepsilon_*=\frac{65}{18311831552}.
\]

The program constructs the **actual 128 distinct endpoint denominators** by independently choosing either enlarged endpoint in each of the seven nonleading coordinates. It does not substitute an abstract interval polynomial, relax coefficient independence, or permit a varying leading coefficient.

For every actual denominator,
\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3,
\]
and the physical spectral polynomial is
\[
P_a(t)=F(t)E_a(t)+tG(t)O_a(t).
\]

An independent double sum reconstructs
\(\operatorname{Re}(q(i\omega)\overline{a(i\omega)})\)
directly from the original \(s\)-coefficients. Thus the parity/pairing check does not merely compare two calls to the same parity formula.

### Four-envelope reduction

For \(t\ge0\), the lower physical even envelope selects
\[
a_0=\ell_0,\quad a_2=u_2,\quad a_4=\ell_4,\quad a_6=u_6,
\]
and the upper envelope selects the opposite endpoints. The lower odd envelope selects
\[
a_1=\ell_1,\quad a_3=u_3,\quad a_5=\ell_5,
\]
and the upper odd envelope selects the opposite endpoints. The coefficient of \(-t^3\) in \(O_a\) remains exactly one.

These give **four actual endpoint denominators**. At each frequency, the sign of \(F\) selects the minimizing even envelope, and the sign of \(G\) selects the minimizing odd envelope. Independence makes their combination an actual member.

The implementation checks the coefficientwise domination needed for this reduction for **every one of the 128 corners**, for all four sign combinations. It then checks the four physical endpoint polynomials on the **entire positive half-axis**, using exact Euclidean Sturm chains, not a frequency grid.

## 3. Written reconstruction, distinguished from execution

The following are written algebraic checks, **not program output**.

### Numerator stability

The exact Routh first column of \(q\), from \(s^7\) through \(s^0\), is
\[
1,\quad1,\quad\frac52,\quad\frac{17}{10},\quad
\frac{39}{17},\quad\frac{73}{26},\quad
\frac{135}{73},\quad4.
\]
All entries are positive.

The source independently recomputes this column and checks it against these values. It also performs Routh checks on all 128 actual enlarged corners. Those corner checks are **not** used as an all-member Hurwitz theorem.

### Seven-region constants and enlargement margin

The seven final core lower bounds claimed in the input are
\[
\frac34,\quad\frac{43}{128},\quad\frac7{32},\quad
\frac{89}{400},\quad\frac{39}{320},\quad
\frac{77}{16},\quad\frac{65}{4096}.
\]
Their minimum is \(m=65/4096\).

The code checks each regional inequality directly on all four physical core endpoint polynomials. The complementary region is represented by its seven closed pieces, with an explicit no-gap coverage check.

It additionally checks, independently of the regional assembly:

- the tail certificate \(P_a(t)>(25/5184)t^7\) for the four core endpoint polynomials on \([6,\infty)\);
- the core weighted certificate \(P_a(t)>\gamma(1+t)^6\);
- the maximum-box weighted certificate
  \[
  P_a(t)>\frac{\gamma}{2}(1+t)^6
  \]
  for all four actual enlarged endpoint polynomials.

The strict polynomial certificates are stronger than the corresponding weak lower bounds required in the manuscript. **Whether these checks pass remains unobserved.**

The perturbation bookkeeping is also checked:
\[
|F|\le4(1+t)^3,\quad |G|\le15(1+t)^3,
\]
\[
|\delta E|\le\varepsilon(1+t)^3,\quad
|\delta O|\le\varepsilon(1+t)^2,
\]
and
\[
\gamma-19\varepsilon_*=\gamma/2>0.
\]

### Stability bridge: separate from finite certificate execution

If the four maximum-box spectral certificates pass, the stated envelope argument extends their bound to every coefficient choice in that box. Because \(q\) belongs to the box and is Hurwitz, the segment from \(q\) to any member stays inside the box. Strict physical pairing excludes imaginary-axis zeros along the segment; fixed monic degree and bounded coefficients exclude escape through infinity.

That is the **written bridge** needed for an all-member stability conclusion. It is not supplied by corner Routh checks alone, and the program’s finite output must not be relabeled as an independently accepted all-box theorem.

At \(t=0\), the physical identity gives \(P_a(0)=4a_0>0\). At infinity, \(P_a\) has degree seven and leading coefficient one, and the monic equal-degree ratio tends to one.

### Actual consumer read

I read the complete displayed moment consumer, S1 LF 476–530. Its algebraic cancellation is
\[
\sum_iw_it_iG(t_i)O_i
=15R_1+23R_3+9R_5+R_7\le0.
\]
Consequently, positive physical pairing implies
\(\sum_iw_iF(t_i)E_i>0\)
for a nonzero positive-weight finite family satisfying the four displayed signed inequalities.

This checks the displayed consumer algebra without dividing by an odd value. It does **not** independently reconstruct the absent S2/S3 interface, classify every R4/R5 representation, or adopt the original-target conclusion.

## 4. Controls and intended rejection reasons

All controls are fixed, exact, and included in the source.

Positive controls:

- the actual \(q\), including its exact Routh column and physical sum-of-squares spectral polynomial;
- \((s+1)^7\), for an independent stable septic;
- \(5\), \(1+t\), and \(t^2-2t+2\), for positive-half-axis checks including negative intermediate coefficients.

Negative controls:

1. **Wrong numerator coefficient:** change \(q_3\) from \(23\) to \(24\). Intended reason: `NUMERATOR_FACTOR_COEFFICIENT`.
2. **Nonmonic leading coefficient:** change \(q_7\) from \(1\) to \(2\). Intended reason: `MONIC_LEADING`.
3. **Wrong physical parity:** reverse the sign of the \(t\)-coefficient of the even component. Intended reason: `PHYSICAL_PARITY_RECONSTRUCTION`.
4. **Missing conjugation:** use the real part of \(q(i\omega)a(i\omega)\). Intended reason: `REAL_CONJUGATE_PRODUCT`.
5. **Missing spectral \(t\)-weight:** use \(FE+GO\). Intended reason: `DC_NORMALIZATION`.
6. **False spectral positivity:** use the physical monic denominator obtained from \(q\) by setting \(a_1=-15\). This is explicitly **outside the target box**. It has positive DC pairing and positive leading spectral coefficient, but
   \[
   P(1/2)=-8775/128<0.
   \]
   Intended reason: `STURM_POSITIVE_AXIS_ZERO`, not a membership or parsing error.
7. **False box membership:** move \(a_0\) one unit above the actual enlarged upper endpoint. Intended reason: `BOX_MEMBERSHIP`.
8. **Wrong stability orientation:** use the physical monic polynomial \(-q(-s)\). Intended reason: `ROUTH_NONPOSITIVE_FIRST_COLUMN`.
9. **Tangential spectral zero:** use \((t-1)^2\). Intended reason: `STURM_POSITIVE_AXIS_ZERO`, exercising an even-multiplicity zero that a sign-change grid could miss.

Only the specifically expected invariant error counts as successful rejection. An unrelated exception, timeout, or different rejection reason cannot count as a passed control.

## 5. Complete independent source and argv

**Execution status: NOT RUN.**

Exact argv: `python3 -I -B -`

Standard input: the complete source below after removing the literal leading `SRC|` from every source line. The prefix is a presentation envelope, not part of Python. No other transformation is required.

The source uses only the standard library, exact rational scientific arithmetic, fixed cases, and an internal cooperative 55-second deadline. It has no explicit file, network, subprocess, installation, deletion, random, or external-model operation. No scientific check uses `assert`.

SOURCE BEGIN
SRC|from fractions import Fraction as Q
SRC|from itertools import product
SRC|from time import monotonic
SRC|import sys
SRC|
SRC|START = monotonic()
SRC|DEADLINE = START + 55.0
SRC|AUDIT = []
SRC|CONTROL_LOG = []
SRC|
SRC|
SRC|class Incomplete(Exception):
SRC|    pass
SRC|
SRC|
SRC|class Failure(Exception):
SRC|    def __init__(self, code, detail=""):
SRC|        self.code = code
SRC|        super().__init__(code + (": " + detail if detail else ""))
SRC|
SRC|
SRC|def guard():
SRC|    if monotonic() >= DEADLINE:
SRC|        raise Incomplete("COOPERATIVE_DEADLINE_55_SECONDS")
SRC|
SRC|
SRC|def need(condition, code, detail=""):
SRC|    guard()
SRC|    if not condition:
SRC|        raise Failure(code, detail)
SRC|
SRC|
SRC|def trim(values):
SRC|    guard()
SRC|    p = [Q(c) for c in values]
SRC|    if not p:
SRC|        p = [Q(0)]
SRC|    while len(p) > 1 and p[-1] == 0:
SRC|        p.pop()
SRC|    return tuple(p)
SRC|
SRC|
SRC|ZERO = (Q(0),)
SRC|ONE = (Q(1),)
SRC|T = (Q(0), Q(1))
SRC|ONE_PLUS_T = (Q(1), Q(1))
SRC|
SRC|
SRC|def add(p, r):
SRC|    return trim(
SRC|        (p[k] if k < len(p) else 0)
SRC|        + (r[k] if k < len(r) else 0)
SRC|        for k in range(max(len(p), len(r)))
SRC|    )
SRC|
SRC|
SRC|def scale(p, c):
SRC|    return trim(Q(c) * x for x in p)
SRC|
SRC|
SRC|def sub(p, r):
SRC|    return add(p, scale(r, -1))
SRC|
SRC|
SRC|def mul(p, r):
SRC|    out = [Q(0)] * (len(p) + len(r) - 1)
SRC|    for i, x in enumerate(p):
SRC|        guard()
SRC|        for j, y in enumerate(r):
SRC|            out[i + j] += x * y
SRC|    return trim(out)
SRC|
SRC|
SRC|def times_t(p):
SRC|    return trim((Q(0),) + tuple(p))
SRC|
SRC|
SRC|def power(p, n):
SRC|    need(isinstance(n, int) and n >= 0, "POLYNOMIAL_POWER_DOMAIN")
SRC|    out = ONE
SRC|    for _ in range(n):
SRC|        out = mul(out, p)
SRC|    return out
SRC|
SRC|
SRC|def value(p, x):
SRC|    out = Q(0)
SRC|    for c in reversed(p):
SRC|        guard()
SRC|        out = out * x + c
SRC|    return out
SRC|
SRC|
SRC|def derivative(p):
SRC|    return trim(k * p[k] for k in range(1, len(p)))
SRC|
SRC|
SRC|def remainder(p, divisor):
SRC|    need(divisor != ZERO, "POLYNOMIAL_DIVISION_BY_ZERO")
SRC|    r = list(p)
SRC|    while len(r) >= len(divisor) and tuple(r) != ZERO:
SRC|        guard()
SRC|        offset = len(r) - len(divisor)
SRC|        factor = r[-1] / divisor[-1]
SRC|        for j, c in enumerate(divisor):
SRC|            r[offset + j] -= factor * c
SRC|        r = list(trim(r))
SRC|    return trim(r)
SRC|
SRC|
SRC|def positive_normalize(p):
SRC|    need(p != ZERO, "NORMALIZE_ZERO_POLYNOMIAL")
SRC|    return scale(p, Q(1) / abs(p[-1]))
SRC|
SRC|
SRC|def sturm_chain(p):
SRC|    need(p != ZERO, "STURM_ZERO_POLYNOMIAL")
SRC|    first = positive_normalize(p)
SRC|    second = derivative(first)
SRC|    chain = [first]
SRC|    if second == ZERO:
SRC|        return tuple(chain)
SRC|    chain.append(positive_normalize(second))
SRC|    while True:
SRC|        guard()
SRC|        nxt = scale(remainder(chain[-2], chain[-1]), -1)
SRC|        if nxt == ZERO:
SRC|            return tuple(chain)
SRC|        chain.append(positive_normalize(nxt))
SRC|
SRC|
SRC|def sign(x):
SRC|    return (x > 0) - (x < 0)
SRC|
SRC|
SRC|def variations(signs):
SRC|    nonzero = [s for s in signs if s != 0]
SRC|    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))
SRC|
SRC|
SRC|def variation_at(chain, x):
SRC|    if x is None:
SRC|        return variations(sign(p[-1]) for p in chain)
SRC|    return variations(sign(value(p, x)) for p in chain)
SRC|
SRC|
SRC|def certify_positive(p, left=Q(0), right=None, tag=""):
SRC|    p = trim(p)
SRC|    need(p != ZERO, "SPECTRAL_ZERO_POLYNOMIAL", tag)
SRC|    need(value(p, left) > 0, "LEFT_ENDPOINT_NOT_POSITIVE", tag)
SRC|    if right is None:
SRC|        need(p[-1] > 0, "INFINITE_LEADING_NOT_POSITIVE", tag)
SRC|    else:
SRC|        need(right >= left, "INTERVAL_ORDER", tag)
SRC|        need(value(p, right) > 0, "RIGHT_ENDPOINT_NOT_POSITIVE", tag)
SRC|    chain = sturm_chain(p)
SRC|    roots = variation_at(chain, left) - variation_at(chain, right)
SRC|    reason = (
SRC|        "STURM_POSITIVE_AXIS_ZERO"
SRC|        if left == 0 and right is None
SRC|        else "STURM_INTERVAL_ZERO"
SRC|    )
SRC|    need(roots == 0, reason, tag + "; distinct_roots=" + str(roots))
SRC|    AUDIT.append((tag, len(p) - 1, left, right, roots))
SRC|
SRC|
SRC|def factored_minus_t(markers):
SRC|    p = ONE
SRC|    for root in markers:
SRC|        p = mul(p, (Q(root), Q(-1)))
SRC|    return p
SRC|
SRC|
SRC|F = factored_minus_t((Q(1, 2), Q(2), Q(4)))
SRC|G = factored_minus_t((Q(1), Q(3), Q(5)))
SRC|QREF = tuple(Q(x) for x in (4, 15, 11, 23, Q(13, 2), 9, 1, 1))
SRC|M = Q(65, 4096)
SRC|GAMMA = M / (7 ** 6)
SRC|EPS = GAMMA / 38
SRC|
SRC|CORE = (
SRC|    (Q(3), Q(5)),
SRC|    (Q(1197, 80), Q(15)),
SRC|    (Q(11), Q(11)),
SRC|    (Q(23), Q(467, 20)),
SRC|    (Q(13, 2), Q(13, 2)),
SRC|    (Q(179, 20), Q(9)),
SRC|    (Q(1), Q(1)),
SRC|)
SRC|EXPANDED = tuple((lo - EPS, hi + EPS) for lo, hi in CORE)
SRC|
SRC|
SRC|def require_monic_septic(a):
SRC|    need(len(a) == 8, "SEPTIC_DEGREE")
SRC|    need(a[7] == 1, "MONIC_LEADING")
SRC|
SRC|
SRC|def physical_parity(a):
SRC|    require_monic_septic(a)
SRC|    even = tuple(((-1) ** k) * a[2 * k] for k in range(4))
SRC|    odd = tuple(((-1) ** k) * a[2 * k + 1] for k in range(4))
SRC|    return trim(even), trim(odd)
SRC|
SRC|
SRC|def compose_s(even, odd):
SRC|    out = [Q(0)] * 8
SRC|    need(len(even) <= 4 and len(odd) <= 4, "PARITY_DEGREE")
SRC|    for k, c in enumerate(even):
SRC|        out[2 * k] = ((-1) ** k) * c
SRC|    for k, c in enumerate(odd):
SRC|        out[2 * k + 1] = ((-1) ** k) * c
SRC|    return trim(out)
SRC|
SRC|
SRC|def require_numerator(a):
SRC|    require_monic_septic(a)
SRC|    need(a == QREF, "NUMERATOR_FACTOR_COEFFICIENT")
SRC|    need(a == compose_s(F, G), "NUMERATOR_FACTORIZATION")
SRC|
SRC|
SRC|def direct_real_product(q, a, conjugated=True):
SRC|    out = [Q(0)] * 8
SRC|    for i, qi in enumerate(q):
SRC|        guard()
SRC|        for j, aj in enumerate(a):
SRC|            if (i + j) % 2:
SRC|                continue
SRC|            k = (i + j) // 2
SRC|            exponent = k + (j if conjugated else 0)
SRC|            out[k] += ((-1) ** exponent) * qi * aj
SRC|    return trim(out)
SRC|
SRC|
SRC|def physical_pair(a, even=None, odd=None, pairing=None):
SRC|    actual_even, actual_odd = physical_parity(a)
SRC|    even = actual_even if even is None else trim(even)
SRC|    odd = actual_odd if odd is None else trim(odd)
SRC|    need(
SRC|        compose_s(even, odd) == a,
SRC|        "PHYSICAL_PARITY_RECONSTRUCTION",
SRC|    )
SRC|    if pairing is None:
SRC|        pairing = add(mul(F, even), times_t(mul(G, odd)))
SRC|    pairing = trim(pairing)
SRC|    need(pairing[0] == QREF[0] * a[0], "DC_NORMALIZATION")
SRC|    need(
SRC|        pairing == direct_real_product(QREF, a, True),
SRC|        "REAL_CONJUGATE_PRODUCT",
SRC|    )
SRC|    need(
SRC|        len(pairing) == 8 and pairing[-1] == 1,
SRC|        "MONIC_SPECTRAL_LEADING",
SRC|    )
SRC|    return pairing
SRC|
SRC|
SRC|def require_member(a, bounds):
SRC|    require_monic_septic(a)
SRC|    for j, (lo, hi) in enumerate(bounds):
SRC|        need(lo <= a[j] <= hi, "BOX_MEMBERSHIP", "coefficient=" + str(j))
SRC|
SRC|
SRC|def routh_first_column(a):
SRC|    require_monic_septic(a)
SRC|    upper = [a[7], a[5], a[3], a[1]]
SRC|    lower = [a[6], a[4], a[2], a[0]]
SRC|    first_column = [upper[0], lower[0]]
SRC|    need(
SRC|        all(x > 0 for x in first_column),
SRC|        "ROUTH_NONPOSITIVE_FIRST_COLUMN",
SRC|        "initial_rows",
SRC|    )
SRC|    for level in range(2, 8):
SRC|        guard()
SRC|        pivot = lower[0]
SRC|        row = [
SRC|            (pivot * upper[j + 1] - upper[0] * lower[j + 1]) / pivot
SRC|            for j in range(3)
SRC|        ] + [Q(0)]
SRC|        need(
SRC|            row[0] > 0,
SRC|            "ROUTH_NONPOSITIVE_FIRST_COLUMN",
SRC|            "row=" + str(level),
SRC|        )
SRC|        first_column.append(row[0])
SRC|        upper, lower = lower, row
SRC|    return tuple(first_column)
SRC|
SRC|
SRC|def endpoint_member(bounds, even_low, odd_low):
SRC|    out = []
SRC|    for j, (lo, hi) in enumerate(bounds):
SRC|        want_low = even_low if j % 2 == 0 else odd_low
SRC|        physical_sign = 1 if (j // 2) % 2 == 0 else -1
SRC|        take_lower_coefficient = (
SRC|            physical_sign > 0 if want_low else physical_sign < 0
SRC|        )
SRC|        out.append(lo if take_lower_coefficient else hi)
SRC|    return tuple(out) + (Q(1),)
SRC|
SRC|
SRC|def four_endpoints(bounds):
SRC|    return {
SRC|        (sf, sg): endpoint_member(bounds, sf > 0, sg > 0)
SRC|        for sf, sg in product((-1, 1), repeat=2)
SRC|    }
SRC|
SRC|
SRC|def mutated(a, index, new_value):
SRC|    out = list(a)
SRC|    out[index] = Q(new_value)
SRC|    return tuple(out)
SRC|
SRC|
SRC|def expect_rejection(name, expected_reason, operation):
SRC|    guard()
SRC|    try:
SRC|        operation()
SRC|    except Failure as exc:
SRC|        need(
SRC|            exc.code == expected_reason,
SRC|            "CONTROL_WRONG_REASON",
SRC|            name + "; expected=" + expected_reason + "; got=" + exc.code,
SRC|        )
SRC|        CONTROL_LOG.append((name, exc.code))
SRC|        return
SRC|    raise Failure("CONTROL_NOT_REJECTED", name)
SRC|
SRC|
SRC|def run_controls():
SRC|    require_numerator(QREF)
SRC|    require_member(QREF, CORE)
SRC|    expected_column = (
SRC|        Q(1), Q(1), Q(5, 2), Q(17, 10),
SRC|        Q(39, 17), Q(73, 26), Q(135, 73), Q(4),
SRC|    )
SRC|    need(
SRC|        routh_first_column(QREF) == expected_column,
SRC|        "Q_ROUTH_EXACT_COLUMN",
SRC|    )
SRC|    binomial_septic = tuple(Q(x) for x in (1, 7, 21, 35, 35, 21, 7, 1))
SRC|    routh_first_column(binomial_septic)
SRC|    certify_positive((Q(5),), tag="positive_constant")
SRC|    certify_positive((Q(1), Q(1)), tag="positive_linear")
SRC|    certify_positive((Q(2), Q(-2), Q(1)), tag="positive_nontrivial_quadratic")
SRC|    certify_positive(physical_pair(QREF), tag="q_physical_spectral_positive")
SRC|
SRC|    expect_rejection(
SRC|        "wrong_numerator_coefficient",
SRC|        "NUMERATOR_FACTOR_COEFFICIENT",
SRC|        lambda: require_numerator(mutated(QREF, 3, Q(24))),
SRC|    )
SRC|    expect_rejection(
SRC|        "nonmonic_leading",
SRC|        "MONIC_LEADING",
SRC|        lambda: require_numerator(mutated(QREF, 7, Q(2))),
SRC|    )
SRC|    even, odd = physical_parity(QREF)
SRC|    wrong_even = list(even)
SRC|    wrong_even[1] = -wrong_even[1]
SRC|    expect_rejection(
SRC|        "wrong_physical_parity",
SRC|        "PHYSICAL_PARITY_RECONSTRUCTION",
SRC|        lambda: physical_pair(QREF, tuple(wrong_even), odd),
SRC|    )
SRC|    unconjugated = direct_real_product(QREF, QREF, False)
SRC|    expect_rejection(
SRC|        "missing_conjugation",
SRC|        "REAL_CONJUGATE_PRODUCT",
SRC|        lambda: physical_pair(QREF, pairing=unconjugated),
SRC|    )
SRC|    missing_t = add(mul(F, even), mul(G, odd))
SRC|    expect_rejection(
SRC|        "missing_spectral_t_weight",
SRC|        "DC_NORMALIZATION",
SRC|        lambda: physical_pair(QREF, pairing=missing_t),
SRC|    )
SRC|    false_denominator = mutated(QREF, 1, Q(-15))
SRC|    false_spectral = physical_pair(false_denominator)
SRC|    need(
SRC|        value(false_spectral, Q(1, 2)) == Q(-8775, 128),
SRC|        "FALSE_SPECTRAL_CONTROL_WITNESS",
SRC|    )
SRC|    need(
SRC|        false_spectral[0] > 0 and false_spectral[-1] > 0,
SRC|        "FALSE_SPECTRAL_CONTROL_ENDPOINTS",
SRC|    )
SRC|    expect_rejection(
SRC|        "false_physical_spectral_positivity",
SRC|        "STURM_POSITIVE_AXIS_ZERO",
SRC|        lambda: certify_positive(false_spectral, tag="false_physical_spectrum"),
SRC|    )
SRC|    outside = mutated(QREF, 0, EXPANDED[0][1] + 1)
SRC|    expect_rejection(
SRC|        "false_actual_box_membership",
SRC|        "BOX_MEMBERSHIP",
SRC|        lambda: require_member(outside, EXPANDED),
SRC|    )
SRC|    wrong_orientation = tuple(
SRC|        -c if j % 2 == 0 else c for j, c in enumerate(QREF)
SRC|    )
SRC|    expect_rejection(
SRC|        "wrong_hurwitz_orientation",
SRC|        "ROUTH_NONPOSITIVE_FIRST_COLUMN",
SRC|        lambda: routh_first_column(wrong_orientation),
SRC|    )
SRC|    expect_rejection(
SRC|        "tangential_positive_axis_zero",
SRC|        "STURM_POSITIVE_AXIS_ZERO",
SRC|        lambda: certify_positive((Q(1), Q(-2), Q(1)), tag="touching_zero"),
SRC|    )
SRC|
SRC|
SRC|def check_constants():
SRC|    need(F == (Q(4), Q(-11), Q(13, 2), Q(-1)), "F_EXPANSION")
SRC|    need(G == (Q(15), Q(-23), Q(9), Q(-1)), "G_EXPANSION")
SRC|    need(compose_s(F, G) == QREF, "Q_FROM_FACTORS")
SRC|    need(GAMMA == Q(65, 481890304), "GAMMA_EXACT")
SRC|    need(EPS == Q(65, 18311831552), "EPSILON_EXACT")
SRC|    need(
SRC|        EPS > 0 and EPS < 1 and GAMMA - 19 * EPS == GAMMA / 2,
SRC|        "EPSILON_POSITIVE_MARGIN",
SRC|    )
SRC|    cubic_binomial = power(ONE_PLUS_T, 3)
SRC|    quadratic_binomial = power(ONE_PLUS_T, 2)
SRC|    need(
SRC|        all(abs(c) <= 4 * cubic_binomial[k] for k, c in enumerate(F)),
SRC|        "F_ABSOLUTE_COEFFICIENT_BOUND",
SRC|    )
SRC|    need(
SRC|        all(abs(c) <= 15 * cubic_binomial[k] for k, c in enumerate(G)),
SRC|        "G_ABSOLUTE_COEFFICIENT_BOUND",
SRC|    )
SRC|    need(all(c >= 1 for c in cubic_binomial), "DELTA_E_COEFFICIENT_BOUND")
SRC|    need(all(c >= 1 for c in quadratic_binomial), "DELTA_O_COEFFICIENT_BOUND")
SRC|    difference = sub(
SRC|        power(ONE_PLUS_T, 6),
SRC|        times_t(power(ONE_PLUS_T, 5)),
SRC|    )
SRC|    need(all(c >= 0 for c in difference), "SPECTRAL_WEIGHT_NORM_BOUND")
SRC|    need(Q(7, 6) ** 6 < 3, "TAIL_BINOMIAL_CONSTANT")
SRC|    need(Q(25, 2592) > GAMMA, "TAIL_NORMALIZED_CONSTANT")
SRC|
SRC|
SRC|def check_all_actual_corners(envelopes):
SRC|    corners = [
SRC|        tuple(EXPANDED[j][bit] for j, bit in enumerate(bits)) + (Q(1),)
SRC|        for bits in product((0, 1), repeat=7)
SRC|    ]
SRC|    need(len(corners) == 128 and len(set(corners)) == 128, "ACTUAL_CORNER_COUNT")
SRC|    need(len(set(envelopes.values())) == 4, "ACTUAL_ENVELOPE_COUNT")
SRC|    need(
SRC|        all(a in corners for a in envelopes.values()),
SRC|        "ENVELOPES_ARE_ACTUAL_CORNERS",
SRC|    )
SRC|    envelope_data = {}
SRC|    for key, a in envelopes.items():
SRC|        require_member(a, EXPANDED)
SRC|        e, o = physical_parity(a)
SRC|        envelope_data[key] = (e, o, physical_pair(a))
SRC|    for number, a in enumerate(corners):
SRC|        guard()
SRC|        require_member(a, EXPANDED)
SRC|        e, o = physical_parity(a)
SRC|        p = physical_pair(a)
SRC|        need(p[0] >= 4 * (3 - EPS), "ACTUAL_CORNER_DC_BOUND", str(number))
SRC|        routh_first_column(a)
SRC|        for (sf, sg), (ee, oo, pp) in envelope_data.items():
SRC|            need(
SRC|                all(sf * (x - y) >= 0 for x, y in zip(e, ee)),
SRC|                "EVEN_ENDPOINT_DOMINATION",
SRC|                str(number),
SRC|            )
SRC|            need(
SRC|                all(sg * (x - y) >= 0 for x, y in zip(o, oo)),
SRC|                "ODD_ENDPOINT_DOMINATION",
SRC|                str(number),
SRC|            )
SRC|            need(
SRC|                sub(p, pp)
SRC|                == add(mul(F, sub(e, ee)), times_t(mul(G, sub(o, oo)))),
SRC|                "ENVELOPE_PAIRING_DIFFERENCE_IDENTITY",
SRC|                str(number),
SRC|            )
SRC|    return len(corners)
SRC|
SRC|
SRC|def regional_specs():
SRC|    residual = (
SRC|        (Q(0), Q(1, 4)),
SRC|        (Q(3, 4), Q(19, 20)),
SRC|        (Q(1), Q(3, 2)),
SRC|        (Q(5, 2), Q(3)),
SRC|        (Q(7, 2), Q(15, 4)),
SRC|        (Q(17, 4), Q(9, 2)),
SRC|        (Q(5), None),
SRC|    )
SRC|    return (
SRC|        ("I1", ((Q(1, 4), Q(3, 4)),), Q(3, 4)),
SRC|        ("I2", ((Q(3, 2), Q(5, 2)),), Q(43, 128)),
SRC|        ("I3", ((Q(15, 4), Q(17, 4)),), Q(7, 32)),
SRC|        ("J1", ((Q(19, 20), Q(1)),), Q(89, 400)),
SRC|        ("J2", ((Q(3), Q(7, 2)),), Q(39, 320)),
SRC|        ("J3", ((Q(9, 2), Q(5)),), Q(77, 16)),
SRC|        ("residual", residual, M),
SRC|    )
SRC|
SRC|
SRC|def check_core_certificates():
SRC|    specs = regional_specs()
SRC|    need(min(bound for _, _, bound in specs) == M, "SEVEN_REGION_MINIMUM")
SRC|    cover = sorted(
SRC|        [interval for _, intervals, _ in specs for interval in intervals],
SRC|        key=lambda interval: interval[0],
SRC|    )
SRC|    need(cover[0][0] == 0 and cover[-1][1] is None, "REGION_COVER_ENDPOINTS")
SRC|    for previous, following in zip(cover, cover[1:]):
SRC|        need(previous[1] == following[0], "REGION_COVER_GAP_OR_OVERLAP")
SRC|    weight = power(ONE_PLUS_T, 6)
SRC|    tail = scale(power(T, 7), Q(25, 5184))
SRC|    core_endpoints = four_endpoints(CORE)
SRC|    for key, a in core_endpoints.items():
SRC|        require_member(a, CORE)
SRC|        p = physical_pair(a)
SRC|        for name, intervals, bound in specs:
SRC|            shifted = sub(p, (bound,))
SRC|            for index, (left, right) in enumerate(intervals):
SRC|                certify_positive(
SRC|                    shifted, left, right,
SRC|                    "core_" + str(key) + "_" + name + "_" + str(index),
SRC|                )
SRC|        certify_positive(
SRC|            sub(p, tail), Q(6), None,
SRC|            "core_tail_" + str(key),
SRC|        )
SRC|        certify_positive(
SRC|            sub(p, scale(weight, GAMMA)),
SRC|            tag="core_uniform_weighted_" + str(key),
SRC|        )
SRC|
SRC|
SRC|def check_maximum_box_certificates(envelopes):
SRC|    weight = power(ONE_PLUS_T, 6)
SRC|    for key, a in envelopes.items():
SRC|        p = physical_pair(a)
SRC|        certify_positive(
SRC|            sub(p, scale(weight, GAMMA / 2)),
SRC|            tag="maximum_box_uniform_weighted_" + str(key),
SRC|        )
SRC|
SRC|
SRC|def main():
SRC|    check_constants()
SRC|    run_controls()
SRC|    require_member(QREF, EXPANDED)
SRC|    envelopes = four_endpoints(EXPANDED)
SRC|    corner_count = check_all_actual_corners(envelopes)
SRC|    check_core_certificates()
SRC|    check_maximum_box_certificates(envelopes)
SRC|    guard()
SRC|    print("RESULT: VALID_FINITE_CERTIFICATES")
SRC|    print("actual_corners=" + str(corner_count))
SRC|    print("actual_endpoint_envelopes=" + str(len(envelopes)))
SRC|    print("corner_routh_checks=" + str(corner_count))
SRC|    print("sturm_certificates=" + str(len(AUDIT)))
SRC|    print("maximum_epsilon=" + str(EPS))
SRC|    print("certified_weighted_margin=" + str(GAMMA / 2))
SRC|    print("q_routh_first_column=" + ",".join(map(str, routh_first_column(QREF))))
SRC|    for name, reason in CONTROL_LOG:
SRC|        print("control_" + name + "=REJECTED:" + reason)
SRC|    print("elapsed_seconds=%.6f" % (monotonic() - START))
SRC|    print(
SRC|        "NOT_ESTABLISHED: parent_adoption; standalone_all_box_theorem; "
SRC|        "original_universal_synthesis; novelty; human_kernel_or_cross_family_review"
SRC|    )
SRC|    return 0
SRC|
SRC|
SRC|if __name__ == "__main__":
SRC|    try:
SRC|        status = main()
SRC|    except Incomplete as exc:
SRC|        print("RESULT: INCOMPLETE")
SRC|        print(str(exc))
SRC|        status = 2
SRC|    except Failure as exc:
SRC|        print("RESULT: REJECTED")
SRC|        print(str(exc))
SRC|        status = 1
SRC|    except Exception as exc:
SRC|        print("RESULT: INCOMPLETE")
SRC|        print("UNEXPECTED_EXCEPTION:" + type(exc).__name__ + ":" + str(exc))
SRC|        status = 2
SRC|    sys.exit(status)
SOURCE END

## 6. Results and remaining gates

**Observed executable results: none.** The source has not been parsed, run, timed, or independently checked by another implementation. The `VALID_FINITE_CERTIFICATES` text inside it is a prospective success output, **not an observed result**.

The remaining unpaid executable step is parent materialization/freezing of these exact source bytes, selection and attribution of the interpreter, and one permitted bounded execution with the stated argv. A timeout or unexpected exception must remain **INCOMPLETE**, not a scientific rejection or passed control. No paid computation or external-model call is requested or authorized.

Actual scientific imports were limited to the frozen S1 range: numerator and box definitions, seven-region claimed bounds, enlargement estimate, and displayed moment consumer. No additional public primary source was opened. The mathematical methods used are the exact Sturm root-count criterion, the Routh stability criterion, and the explicitly separated convexity/root-continuity bridge; this is not a kernel verification of those general theorems.

This is a **same-harness independent implementation**, not cross-family, human, kernel, novelty, or global-target credit. All candidate acceptance remains for parent disposition. The original universal common-SPR synthesis target is neither proved nor refuted here.

overall_correctness: correct

explanation: No substantive defect was established in the frozen written excerpt at its stated explicit-box scope. The independent finite implementation is NOT RUN, so this verdict does not assert executable success, parent adoption, or resolution of the original universal target.

confidence: 0.86