# F523 — Exact finite-check candidate for fixed-parity strictification and the binomial family

**Status: written reconstruction and explicit certificates; executable NOT RUN.**

This is the complete body for Main to materialize as `author-candidate-v1.md`. The independent checker source is included below in full. No repository files were changed, scientific programs executed, or external sources/models consulted.

## 1. Scope, bindings, and chronology

I read, in this order:

1. The complete 110-line manifest.
2. The complete 47-line freeze receipt.
3. The complete parent metadata supply and dispatch receipt.
4. All eleven permission/status controls, including their endings.
5. A direct pre-body acknowledgement was then sent.
6. The complete 878-line literal packet, in ordered raw reads of at most 20 LF, through its ending.

The packet contains complete logical source lines S1:1–823 and S2:1–53. S1 has 822 LF delimiters according to the supplied metadata.

Bindings supplied by the assignment and parent records:

- Manifest SHA256: `582c6f3e3c86619657d3e5fc4c4d8527789beb0558e8fe398894e092ff03782f`
- Receipt SHA256: `45d5090c239237ab7cb8e7ed1f8423e6df9ce252105a373369b3c9394b0df464`
- Packet SHA256: `e3fbe8dfc5f9042ce9ffeeac2c0bb62c782cb3560cb6dbe7b99a95c23e0f0b0b`
- S1 SHA256: `5ea7d6280ff7a4853f181f4d06030fdb79b46338eb637812aa9ee19a19e25fac`
- S2 SHA256: `fdd46b6ad702530fe0bcd07d4e7b86468dca9a40e00de5975b4773e292babf08`

These are **parent-supplied bindings**, not hashes computed by this child.

All held episodes and their proof, method, selection, planning, confidence, and reporting consumers remained NONINPUT. I did not follow the packet’s links to author implementations, sibling reviews, or earlier finite-check programs.

The active runtime prohibits scientific execution and file editing. Accordingly:

- **Scientific execution: NOT RUN.**
- **Executable mutation checks: NOT RUN.**
- **Measured runtime, stdout, exit status, native execution/hash receipt: unavailable.**
- The source below is a prospective checker, not an execution result.
- The mathematical calculations displayed here are written derivations.

## 2. Physical pairing derived from coefficient arrays

Use ascending coefficient order throughout:

\[
a(s)=\sum_{j=0}^{7}a_js^j,\qquad
q(s)=\sum_{j=0}^{7}q_js^j,\qquad a_7=q_7=1.
\]

For \(t=\omega^2\),

\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,
\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3.
\]

Define \(F=E_q\), \(G=O_q\). Direct multiplication, rather than a sign convention assumed from a row representation, gives

\[
\operatorname{Re}\!\left(q(i\omega)\overline{a(i\omega)}\right)
=F(t)E_a(t)+tG(t)O_a(t).
\]

Equivalently, its coefficient of \(t^\ell\) is

\[
\sum_{\substack{0\le j,k\le7\\j+k=2\ell}}
q_ja_k\operatorname{Re}(i^{\,j-k}).
\]

This is the coefficient-array route implemented independently of the parity-product route in the supplied checker.

The corresponding raw columns, in **ascending numerator-coefficient order**, are

\[
r_a(t)=
(E_a,\ tO_a,\ -tE_a,\ -t^2O_a,\
t^2E_a,\ t^3O_a,\ -t^3E_a,\ -t^4O_a).
\]

Thus \((q_0,\ldots,q_7)\cdot r_a=P_{q,a}\). The checker compares all three constructions: direct physical product, parity product, and raw-row contraction.

### Compactification and endpoints

Let \(u=t/(1+t)\). For any polynomial \(p(t)=\sum_{k=0}^7p_kt^k\),

\[
\mathcal C_7p(u)
=\sum_{k=0}^7p_ku^k(1-u)^{7-k}.
\]

This is an exact polynomial transformation, not frequency sampling.

Writing \(\widetilde E=(1-u)^3E(u/(1-u))\), and similarly for the other cubics,

\[
\overline P(u)
=(1-u)\widetilde F(u)\widetilde E_a(u)
+u\widetilde G(u)\widetilde O_a(u).
\]

Consequently,

\[
\overline P(0)=q_0a_0,\qquad
\overline P(1)=q_7a_7=1.
\]

For fixed odd parity and the correctly constructed \(q_\delta\),

\[
\overline P
=u\widetilde O^2+
\delta(1-u)\widetilde E_*\widetilde E_a.
\]

For fixed even parity,

\[
\delta\overline P
=(1-u)\widetilde E^2+
\delta u\widetilde O_*\widetilde O_a.
\]

In the latter identity, \(\delta\overline P(1)=\delta\), not \(1\). The unscaled monic pairing still has \(\overline P(1)=1\).

## 3. Exact constants and an all-frequency certificate for all 128 binomial corners

Take the manuscript’s assigned instance

\[
B(s)=(s+1)^7,\qquad \varepsilon=\frac34.
\]

Its ascending coefficient array is

\[
B=(1,7,21,35,35,21,7,1).
\]

The actual independent box is

\[
a_j=B_j+\xi_j,\qquad |\xi_j|\le\frac34,\quad j=0,\ldots,6,
\qquad a_7=1.
\]

Its 128 corners are indexed without omission by
\(\sigma\in\{-1,1\}^7\), with \(\xi_j=(3/4)\sigma_j\).

The reciprocal-binomial constant is exactly

\[
C=\sum_{j=0}^6\frac1{\binom7j}
=1+\frac27+\frac2{21}+\frac2{35}
=\frac{151}{105}.
\]

Also,

\[
\frac{36}{25}-C=\frac1{525}.
\]

Let

\[
z=B(i\omega),\quad d=\sum_{j=0}^6\xi_j(i\omega)^j,\quad
S=(1+t)^7,\quad t=\omega^2.
\]

Weighted Cauchy–Schwarz yields

\[
|d|^2\le
\left(\sum_{j=0}^6\frac{\xi_j^2}{\binom7j}\right)
\left(\sum_{j=0}^6\binom7j t^j\right)
\le\frac{453}{560}S.
\]

Since

\[
\frac{81}{100}-\frac{453}{560}=\frac3{2800},
\]

we have

\[
\frac{81}{100}S-|d|^2\ge\frac3{2800}S.
\]

The following exact identity then certifies the desired margin:

\[
P_{B,a}-\frac1{10}S
=\frac59\left(
\left|\frac9{10}z+d\right|^2+
\frac{81}{100}S-|d|^2
\right)
\ge\frac1{1680}S.
\]

Therefore the stronger bound

\[
\boxed{P_{B,a}(t)\ge\frac{169}{1680}(1+t)^7
>\frac1{10}(1+t)^7}
\]

holds for **every actual member**, hence for all 128 actual corners, over the entire frequency axis.

### Explicit rational sum-of-squares form for each corner

This also supplies a finite, sign-indexed certificate without sampled frequencies.

Put \(c_j=\binom7j\), \(T=\sum_{j=0}^6c_jt^j\), and

\[
H=\sum_{j=0}^6\frac{\xi_j^2}{c_j}.
\]

The exact weighted Lagrange identity is

\[
HT-|d|^2
=
\sum_{0\le i<j\le6}
c_ic_j
\left|
\frac{\xi_i}{c_i}(i\omega)^j
-\frac{\xi_j}{c_j}(i\omega)^i
\right|^2.
\]

Each absolute square is the sum of the squares of two real, rational-coefficient polynomials in \(\omega\).

At every one of the 128 corners, \(H=453/560\), so

\[
\frac{81}{100}S-|d|^2
=
\frac3{2800}S+\frac{453}{560}t^7+
\sum_{i<j}c_ic_j
\left|
\frac{\xi_i}{c_i}(i\omega)^j
-\frac{\xi_j}{c_j}(i\omega)^i
\right|^2.
\]

This is an explicit exact all-frequency certificate for the entire finite corner family. It is a **written quadratic certificate**, not a claim that 128 Sturm computations were executed.

The supplied program separately constructs the 128 physical pairing polynomials and requests exact Sturm certificates for

\[
\mathcal C_7P_{B,a}-\frac1{10}>0
\quad\text{on }[0,1].
\]

Those prospective Sturm computations remain **NOT RUN**.

### All-member stability

For every actual \(a=B+d\), follow \(B+\tau d\), \(0\le\tau\le1\). The same strict pairing bound excludes every imaginary-axis zero, including zero frequency. The segment is monic of fixed degree and has bounded coefficients. Roots cannot cross the imaginary axis or escape through infinity. Since \(B\) has seven roots at \(-1\), every actual member is strictly Hurwitz.

This is the stability proof. Corner Routh checks, if later executed, are corroborating finite checks and do not replace it.

## 4. A genuine fixed-parity box and a nontrivial dyadic strictifier

Restrict the same binomial family by fixing its odd coefficients:

\[
a_1=7,\qquad a_3=35,\qquad a_5=21,
\]

while retaining four independent even intervals:

\[
\begin{aligned}
a_0&\in[1/4,7/4],&
a_2&\in[81/4,87/4],\\
a_4&\in[137/4,143/4],&
a_6&\in[25/4,31/4].
\end{aligned}
\]

This is a nonsingleton, four-dimensional independent fixed-odd-parity box with 16 actual corners. Every member is Hurwitz by the preceding all-member argument.

Write

\[
E=1-21t+35t^2-7t^3,\qquad
O=7-35t+21t^2-t^3.
\]

Choose the explicitly requested dyadic parameter

\[
\delta=\frac12.
\]

The correctly scaled monic numerator is

\[
\boxed{
q_\delta(s)=
s^7+\frac72s^6+21s^5+\frac{35}{2}s^4
+35s^3+\frac{21}{2}s^2+7s+\frac12.
}
\]

If \(E_a=E+D\), then

\[
P_{q_\delta,a}
=\delta E(E+D)+tO^2
=\delta P_{B,a}+(1-\delta)tO^2.
\]

Consequently,

\[
\boxed{
P_{q_\delta,a}(t)
\ge\frac{169}{3360}(1+t)^7
>\eta(1+t)^7,\qquad \eta=\frac1{20}.
}
\]

This proves a certified margin for all actual members, not just the 16 corners.

### Stability of \(q_\delta\)

For \(\lambda\in[1/2,1]\), consider

\[
q_\lambda(s)=\lambda E(-s^2)+sO(-s^2).
\]

At nonzero imaginary frequency, a zero would require \(E(t)=O(t)=0\), contradicting the stability of \(B\). At zero frequency, \(q_\lambda(0)=\lambda>0\). This monic, bounded-coefficient homotopy starts at \(q_1=B\), so \(q_{1/2}\) is strictly Hurwitz.

The constructed numerator need not belong to the denominator box; indeed its \(s^6\) coefficient is outside that core box’s interval. The proof does not assume otherwise.

## 5. Explicit seven-interval thickening

For this numerator,

\[
Q=\sum_{j=0}^7|q_{\delta,j}|=96.
\]

Using the manuscript’s perturbation constant,

\[
\boxed{\rho=\frac{\eta}{14Q}=\frac1{26880}.}
\]

The seven independently variable intervals are therefore

| Coefficient | Thickened interval |
|---|---|
| \(a_0\) | \([1/4-\rho,\;7/4+\rho]\) |
| \(a_1\) | \([7-\rho,\;7+\rho]\) |
| \(a_2\) | \([81/4-\rho,\;87/4+\rho]\) |
| \(a_3\) | \([35-\rho,\;35+\rho]\) |
| \(a_4\) | \([137/4-\rho,\;143/4+\rho]\) |
| \(a_5\) | \([21-\rho,\;21+\rho]\) |
| \(a_6\) | \([25/4-\rho,\;31/4+\rho]\) |

For a coordinatewise perturbation \(h(s)=\sum_{j=0}^6h_js^j\), \(|h_j|\le\rho\),

\[
|h(i\omega)|\le7\rho(1+t)^3,\qquad
|q_\delta(i\omega)|\le Q(1+t)^{7/2}.
\]

Thus

\[
|P_{q_\delta,a+h}-P_{q_\delta,a}|
\le7\rho Q(1+t)^7
=\frac1{40}(1+t)^7.
\]

The stronger core margin above gives

\[
\boxed{
P_{q_\delta,a+h}(t)
\ge\frac{85}{3360}(1+t)^7
>\frac1{40}(1+t)^7.
}
\]

The no-crossing homotopy from the projected core member to each actual thickened member proves all-member Hurwitz stability. All seven intervals have positive width.

The checker below requests full-frequency Sturm certificates at all 128 thickened corners with the conservative margin \(1/40\).

## 6. Actual raw-row consumers

For either common numerator above, all eight numerator coefficients are strictly positive.

For every nonzero finite positive-weight combination of actual atoms,

\[
(q_0,\ldots,q_7)\cdot\sum_iw_ir_{a_i}(t_i)
=\sum_iw_iP_{q,a_i}(t_i)>0.
\]

Hence an all-eight-strict-negative aggregate is impossible **for these boxes**.

If the four signed odd coordinates satisfy \(R_1,R_3,R_5,R_7\le0\), then

\[
\sum_iw_it_iG(t_i)O_{a_i}(t_i)
=q_1R_1+q_3R_3+q_5R_5+q_7R_7\le0,
\]

and therefore

\[
\sum_iw_iF(t_i)E_{a_i}(t_i)>0.
\]

This written implication covers every actual configuration satisfying those inequalities, including the stated R4/R5 orientations and zero-odd degeneracies. It involves no division by an odd value. It is not a claim that continuous ray families were enumerated by the finite program.

## 7. Independent checker: obligations and mutation interpretation

The source below uses only the Python standard library and exact `Fraction` arithmetic. It has:

- 128 binomial-corner positivity obligations, margin \(1/10\);
- 16 fixed-parity-corner positivity obligations, margin \(1/20\);
- 128 thickened-corner positivity obligations, margin \(1/40\);
- exact physical/parity/raw-row identity checks for each;
- exact Routh checks for each corner and the numerators;
- square-free reduction and Sturm root counts, including tangential roots;
- nine specified mutation controls.

For every successful positivity obligation it emits the actual coefficient array, raw pairing polynomial, compactified margin polynomial, endpoint values, square-free gcd, Sturm chain, and endpoint variations. Thus a later run can produce inspectable certificates rather than a bare success count.

The mutation controls distinguish their intended invariants:

| Mutation | Intended discriminator |
|---|---|
| Wrong conjugation | Compactified infinity value is \(-1\), not \(1\) |
| Omitted factor \(t\) | Compactified infinity value becomes zero |
| Extra factor \(t\) | Physical degree becomes eight |
| Scaling the leading odd coefficient | Violates monicity and the infinity endpoint |
| Zero \(\delta\) | Zero-frequency strict positivity fails |
| Tangential zero | Positive endpoints but one interior root |
| Omitted raw coefficient | Raw-row contraction differs from physical product |
| Wrong raw-row order | Raw-row contraction differs from physical product |
| Omitted corner coordinate | Only a proper subgrid is covered |

For contract-only or identity-only controls, the source explicitly labels positivity discrimination **NOTTESTED**. In particular, a proper subbox can remain positive; positivity alone cannot detect an omitted box coordinate.

**All executable controls remain NOT RUN in this return.**

Proposed argv, after Main materializes the source:

- `python3`
- `-I`
- `-B`
- `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f523-septic-fixed-parity-and-binomial-family-independent-exact-finite-check/independent-f523-septic-exact-v1.py`

The script performs no file/network access, subprocess launch, installation, or deletion. Its fixed finite workload has a cooperative 55-second elapsed-time guard. No measured runtime or guaranteed completion within that guard is claimed; exhaustion exits distinctly without certification.

## 8. Full independent source

SOURCE BEGIN — independent-f523-septic-exact-v1.py

import time
START = time.monotonic()

import sys
from fractions import Fraction as F
from math import comb

LIMIT_SECONDS = 55
ZERO = (F(0),)


class BudgetExhausted(Exception):
    pass


class VerificationError(Exception):
    pass


def tick():
    if time.monotonic() - START >= LIMIT_SECONDS:
        raise BudgetExhausted("cooperative 55-second limit reached")


def need(condition, message):
    if not condition:
        raise VerificationError(message)


def poly(values):
    values = [F(x) for x in values]
    if not values:
        return ZERO
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def add(a, b):
    tick()
    out = [F(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(b):
        out[j] += x
    return poly(out)


def scale(a, c):
    tick()
    return poly(x * c for x in a)


def shift(a, k):
    return poly([F(0)] * k + list(a))


def mul(a, b):
    tick()
    out = [F(0)] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return poly(out)


def derivative(a):
    return poly(j * a[j] for j in range(1, len(a)))


def value(a, x):
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def divide(a, b):
    tick()
    a = list(poly(a))
    b = poly(b)
    need(b != ZERO, "polynomial division by zero")
    out = [F(0)] * max(1, len(a) - len(b) + 1)
    while poly(a) != ZERO and len(a) >= len(b):
        tick()
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        out[k] += c
        for j in range(len(b)):
            a[k + j] -= c * b[j]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    return poly(out), poly(a)


def gcd_poly(a, b):
    a, b = poly(a), poly(b)
    while b != ZERO:
        tick()
        a, b = b, divide(a, b)[1]
    need(a != ZERO, "undefined zero/zero gcd")
    return scale(a, F(1) / a[-1])


def positive_normalize(a):
    need(a != ZERO, "cannot normalize zero polynomial")
    return scale(a, F(1) / abs(a[-1]))


def sturm(a):
    tick()
    a = poly(a)
    g = gcd_poly(a, derivative(a))
    squarefree, remainder = divide(a, g)
    need(remainder == ZERO, "square-free division has remainder")
    sequence = [positive_normalize(squarefree)]
    d = derivative(sequence[0])
    if d == ZERO:
        return g, tuple(sequence)
    sequence.append(positive_normalize(d))
    while True:
        tick()
        remainder = divide(sequence[-2], sequence[-1])[1]
        if remainder == ZERO:
            break
        sequence.append(positive_normalize(scale(remainder, -1)))
    return g, tuple(sequence)


def variations(sequence, x):
    signs = []
    for p in sequence:
        y = value(p, x)
        if y != 0:
            signs.append(1 if y > 0 else -1)
    return sum(signs[j] != signs[j - 1]
               for j in range(1, len(signs)))


def analyze_positive(a):
    tick()
    endpoints = (value(a, F(0)), value(a, F(1)))
    if endpoints[0] <= 0 or endpoints[1] <= 0:
        return False, endpoints, None, None, None, ()
    g, sequence = sturm(a)
    v0 = variations(sequence, F(0))
    v1 = variations(sequence, F(1))
    need(v0 >= v1, "negative Sturm root count")
    return v0 == v1, endpoints, v0, v1, g, sequence


def compact(a, degree=7):
    tick()
    a = poly(a)
    need(len(a) <= degree + 1, "compactification degree overflow")
    out = [F(0)] * (degree + 1)
    for k, c in enumerate(a):
        for r in range(degree - k + 1):
            out[k + r] += c * comb(degree - k, r) * ((-1) ** r)
    return poly(out)


def parity(a):
    need(len(a) == 8, "expected degree-seven coefficient array")
    even = poly((a[0], -a[2], a[4], -a[6]))
    odd = poly((a[1], -a[3], a[5], -a[7]))
    return even, odd


def physical(q, a, conjugate=True):
    tick()
    out = [F(0)] * 8
    for j, x in enumerate(q):
        for k, y in enumerate(a):
            phase = (j - k if conjugate else j + k) % 4
            if phase == 0:
                out[(j + k) // 2] += x * y
            elif phase == 2:
                out[(j + k) // 2] -= x * y
    return poly(out)


def parity_pair(q, a):
    f, g = parity(q)
    e, o = parity(a)
    return add(mul(f, e), shift(mul(g, o), 1))


def raw_columns(a):
    e, o = parity(a)
    columns = []
    for j in range(8):
        k = j // 2
        base = shift(e, k) if j % 2 == 0 else shift(o, k + 1)
        columns.append(scale(base, (-1) ** k))
    return tuple(columns)


def contract(q, columns):
    out = ZERO
    for c, column in zip(q, columns):
        out = add(out, scale(column, c))
    return out


def routh(a):
    tick()
    need(len(a) == 8 and a[7] == 1,
         "Routh input is not a monic septic")
    u = [a[7], a[5], a[3], a[1]]
    v = [a[6], a[4], a[2], a[0]]
    first_column = [u[0], v[0]]
    need(u[0] > 0 and v[0] > 0, "nonpositive initial Routh pivot")
    for row in range(2, 8):
        tick()
        need(v[0] > 0, "nonpositive Routh pivot")
        current = [
            (v[0] * u[j + 1] - u[0] * v[j + 1]) / v[0]
            for j in range(3)
        ] + [F(0)]
        need(current[0] > 0, "Routh stability failure")
        first_column.append(current[0])
        u, v = v, current
    return tuple(first_column)


def make_grid(lo, hi):
    varying = [j for j in range(7) if lo[j] != hi[j]]
    out = []
    for mask in range(1 << len(varying)):
        a = list(lo) + [F(1)]
        for bit, j in enumerate(varying):
            a[j] = hi[j] if (mask >> bit) & 1 else lo[j]
        out.append(tuple(a))
    return tuple(out)


def complete_grid(corners, lo, hi):
    if len(lo) != 7 or len(hi) != 7:
        return False
    if any(lo[j] > hi[j] for j in range(7)):
        return False
    count = 1 << sum(lo[j] != hi[j] for j in range(7))
    if len(corners) != count or len(set(corners)) != count:
        return False
    for a in corners:
        if len(a) != 8 or a[7] != 1:
            return False
        if any(a[j] not in (lo[j], hi[j]) for j in range(7)):
            return False
    return True


def fmt(a):
    return "(" + ", ".join(str(x) for x in a) + ")"


def certify_box(name, q, lo, hi, margin):
    tick()
    corners = make_grid(lo, hi)
    need(complete_grid(corners, lo, hi), name + ": incomplete grid")
    need(q[7] == 1, name + ": nonmonic numerator")
    print("BOX", name, "COUNT", len(corners), "MARGIN", margin)
    print("NUMERATOR_ASCENDING", fmt(q))
    print("NUMERATOR_ROUTH_FIRST_COLUMN", fmt(routh(q)))
    for mask, a in enumerate(corners):
        tick()
        p = physical(q, a)
        need(p == parity_pair(q, a), name + ": physical/parity mismatch")
        need(p == contract(q, raw_columns(a)),
             name + ": physical/raw-row mismatch")
        need(len(p) == 8 and p[7] == 1,
             name + ": wrong physical leading term")
        u = compact(p)
        need(value(u, F(0)) == q[0] * a[0],
             name + ": wrong zero-frequency endpoint")
        need(value(u, F(1)) == 1,
             name + ": wrong infinity endpoint")
        margin_polynomial = add(u, (-margin,))
        ok, endpoints, v0, v1, g, sequence = analyze_positive(
            margin_polynomial)
        need(ok, name + ": strict all-frequency margin failed")
        first_column = routh(a)
        print("CERTIFICATE", name, mask)
        print("DENOMINATOR_ASCENDING", fmt(a))
        print("PHYSICAL_PAIRING_ASCENDING", fmt(p))
        print("COMPACT_MARGIN_ASCENDING", fmt(margin_polynomial))
        print("ENDPOINTS", fmt(endpoints))
        print("SQUAREFREE_GCD_ASCENDING", fmt(g))
        print("STURM_VARIATIONS", v0, v1, "INTERIOR_ROOTS", v0 - v1)
        for index, row in enumerate(sequence):
            print("STURM_CHAIN", index, fmt(row))
        print("CORNER_ROUTH_FIRST_COLUMN", fmt(first_column))
    return len(corners)


def mutation(name, detected, discriminator, positivity_tested):
    tick()
    need(detected, "mutation was not discriminated: " + name)
    print("MUTATION", name, "DETECTED_BY", discriminator,
          "POSITIVITY_DISCRIMINATION",
          "TESTED" if positivity_tested else "NOTTESTED")


def main():
    tick()
    base = tuple(F(comb(7, j)) for j in range(8))
    eps = F(3, 4)
    delta = F(1, 2)
    c = sum((F(1, comb(7, j)) for j in range(7)), F(0))
    need(c == F(151, 105), "wrong reciprocal-binomial constant")
    need(F(36, 25) - c == F(1, 525), "wrong 6/5 comparison")
    slack = F(81, 100) - eps * eps * c
    need(slack == F(3, 2800), "wrong squared-norm slack")
    strengthened_margin = F(1, 10) + slack / F(9, 5)
    need(strengthened_margin == F(169, 1680),
         "wrong strengthened binomial margin")
    need(compact(base) == (F(1),),
         "compactification of (1+t)^7 is not one")

    qdelta = tuple(
        base[j] * (delta if j % 2 == 0 else F(1))
        for j in range(8))
    eta = delta / 10
    qnorm = sum(abs(x) for x in qdelta)
    rho = eta / (14 * qnorm)
    need(eta == F(1, 20), "wrong fixed-parity margin")
    need(qnorm == 96, "wrong numerator coefficient norm")
    need(rho == F(1, 26880), "wrong thickening radius")

    full_lo = tuple(base[j] - eps for j in range(7))
    full_hi = tuple(base[j] + eps for j in range(7))
    core_lo = tuple(
        base[j] - eps if j % 2 == 0 else base[j]
        for j in range(7))
    core_hi = tuple(
        base[j] + eps if j % 2 == 0 else base[j]
        for j in range(7))
    thick_lo = tuple(x - rho for x in core_lo)
    thick_hi = tuple(x + rho for x in core_hi)

    print("EXACT_CONSTANTS", c, slack, strengthened_margin,
          eta, qnorm, rho)
    count = certify_box(
        "binomial-128", base, full_lo, full_hi, F(1, 10))
    count += certify_box(
        "fixed-odd-16", qdelta, core_lo, core_hi, eta)
    count += certify_box(
        "thickened-128", qdelta, thick_lo, thick_hi, eta / 2)
    need(count == 272, "wrong total number of corner obligations")

    correct = physical(base, base)
    wrong_conjugate = physical(base, base, conjugate=False)
    mutation(
        "wrong-conjugation",
        wrong_conjugate != correct
        and value(compact(wrong_conjugate), F(1)) == -1,
        "negative-compact-infinity", True)

    e, o = parity(base)
    omitted_t = add(mul(e, e), mul(o, o))
    mutation(
        "omitted-t",
        omitted_t != correct
        and value(compact(omitted_t), F(1)) == 0,
        "zero-compact-infinity", True)

    extra_t = add(mul(e, e), shift(mul(o, o), 2))
    mutation(
        "extra-t",
        len(extra_t) == 9,
        "degree-eight-instead-of-seven", False)

    wrong_parity = tuple(
        base[j] * (delta if j % 2 == 1 else F(1))
        for j in range(8))
    mutation(
        "scaled-leading-odd-coefficient",
        wrong_parity[7] != 1
        and value(compact(physical(wrong_parity, base)), F(1)) == delta,
        "monicity-and-infinity-contract", False)

    zero_delta = tuple(
        F(0) if j % 2 == 0 else base[j]
        for j in range(8))
    zero_pair = compact(physical(zero_delta, base))
    mutation(
        "zero-delta",
        value(zero_pair, F(0)) == 0
        and not analyze_positive(zero_pair)[0],
        "zero-frequency-strictness", True)

    tangent = (F(1, 4), F(-1), F(1))
    tangent_result = analyze_positive(tangent)
    mutation(
        "tangential-interior-zero",
        not tangent_result[0]
        and tangent_result[1][0] > 0
        and tangent_result[1][1] > 0
        and tangent_result[2] - tangent_result[3] == 1,
        "one-distinct-interior-Sturm-root", True)

    columns = list(raw_columns(base))
    missing_column = list(columns)
    missing_column[6] = ZERO
    mutation(
        "omitted-raw-coefficient",
        contract(base, missing_column) != correct,
        "physical-versus-raw-identity", False)

    swapped_columns = list(columns)
    swapped_columns[0], swapped_columns[1] = (
        swapped_columns[1], swapped_columns[0])
    mutation(
        "wrong-raw-row-order",
        contract(base, swapped_columns) != correct,
        "physical-versus-raw-identity", False)

    full_grid = make_grid(full_lo, full_hi)
    omitted_coordinate_grid = tuple(
        tuple(a[j] if j != 6 else full_lo[6] for j in range(8))
        for a in full_grid)
    mutation(
        "omitted-corner-coordinate",
        not complete_grid(omitted_coordinate_grid, full_lo, full_hi)
        and len(set(omitted_coordinate_grid)) == 64,
        "incomplete-Cartesian-grid", False)

    tick()
    print("PASS: 272 exact full-frequency corner margin certificates.")
    print("PASS: physical/parity/raw identities and corner Routh checks.")
    print("PASS: nine controls discriminated their stated invariants.")
    print("No arbitrary-box, novelty, human, family, or kernel claim.")


if __name__ == "__main__":
    try:
        main()
    except BudgetExhausted as exc:
        print("NOT_CERTIFIED_BUDGET:", str(exc), file=sys.stderr)
        sys.exit(2)
    except VerificationError as exc:
        print("NOT_CERTIFIED_FAILURE:", str(exc), file=sys.stderr)
        sys.exit(1)

SOURCE END

## 9. Exact ceiling and remaining obligations

### Established here as written mathematics

- The physical conjugate-product, parity-product, compactification, endpoint, and raw-row identities.
- The constants \(151/105\), \(1/525\), \(3/2800\), and the conservative manuscript margin \(1/10\).
- An explicit stronger all-member binomial margin \(169/1680\), with an exact rational quadratic certificate covering all 128 actual corners.
- A genuine four-dimensional fixed-parity box within that binomial instance.
- A nontrivial dyadic strictifier \(\delta=1/2\), its stability homotopy, and margin \(1/20\).
- The exact seven-coordinate thickening radius \(1/26880\), with all-member stability and conservative margin \(1/40\).
- The stated raw-row consumer consequences for these sufficient classes.

### Not established by an execution

The 272 prospective Sturm checks, Routh outputs, and nine executable mutation controls were **not run**. No generated Sturm-chain transcript or successful execution receipt exists from this child. The program itself remains an unexecuted author artifact requiring Main’s actual replay before finite-execution credit.

### Original-target ceiling

This does **not** solve common-SPR synthesis for arbitrary all-Hurwitz independent septic boxes. It does not prove that numerators for different fixed-parity slices can be glued into one numerator for their union. It supplies no eligible box with an all-eight-strict-negative obstruction.

It does not reverify S2’s separate \(\gamma\)-family or earlier finite execution, and gives no mathematical disposition on f490, f513, or other waves. Historical holds are not rehabilitated. No novelty, source-wide correspondence, human review, independent-family acceptance, or formal/kernel verification is claimed.

**Overall correctness:** correct within the displayed written construction and identities.

**Explanation:** The assigned binomial instance, a genuine fixed-parity restriction, and its explicit seven-interval thickening have exact all-member, all-frequency written certificates. The independent executable is supplied completely but remains NOT RUN, so finite-replay acceptance is still unpaid.

**Confidence:** 0.96 for the written reconstruction; no execution-based confidence or acceptance credit claimed.