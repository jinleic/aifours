# author-candidate-v1.md

## Constructive common-SPR synthesis for an explicit full-dimensional septic-box class

**Status: AUTHOR CANDIDATE — not independently reviewed or automatically adopted.**

**Scientific result.** A single explicit monic septic numerator works for every member of a specified independent coefficient box, including an explicit enlargement in **all seven nonleading coefficients**. The proof covers the entire frequency axis and proves every denominator strictly Hurwitz. It supplies a genuine interior-root common test, controlling every actual R4 ray and both R5 orientations.

**Original-target boundary.** This does **not** prove synthesis for every all-Hurwitz independent septic box, and it does not produce an eight-strict-negative obstruction. It proves a whole-class sufficient theorem with explicit conditions, rather than another failure of a selected test or a reduction whose inequalities remain unpaid.

No scientific program was executed. Complete optional exact-check source is supplied below as **NOT RUN**.

---

## 1. The actual box and fixed numerator

Define
\[
F(t)=\left(\frac12-t\right)(2-t)(4-t)
     =4-11t+\frac{13}{2}t^2-t^3,
\]
and
\[
G(t)=(1-t)(3-t)(5-t)
     =15-23t+9t^2-t^3.
\]

The fixed numerator is
\[
\boxed{
q(s)=F(-s^2)+sG(-s^2)
=s^7+s^6+9s^5+\frac{13}{2}s^4+23s^3+11s^2+15s+4.
}
\]

First consider the independent box \(B_0\):
\[
a(s)=s^7+s^6+a_5s^5+\frac{13}{2}s^4+a_3s^3+11s^2+a_1s+a_0,
\]
where
\[
\boxed{
a_0\in[3,5],\quad
a_1\in[1197/80,15],\quad
a_3\in[23,467/20],\quad
a_5\in[179/20,9].
}
\]
All four intervals vary independently.

This contains the complete actual box in frozen S2/S3: its constant interval has been enlarged from \([15/4,17/4]\) to \([3,5]\), while its three odd intervals are unchanged.

For the full-dimensional enlargement, put
\[
m=\frac{65}{4096},\qquad
\gamma=\frac{m}{7^6},\qquad
\varepsilon_*=\frac{\gamma}{38}.
\]

For any \(0\le\varepsilon\le\varepsilon_*\), let \(B_\varepsilon\) be the independent monic septic box with
\[
\begin{aligned}
a_0&\in[3-\varepsilon,5+\varepsilon],\\
a_1&\in[1197/80-\varepsilon,15+\varepsilon],\\
a_2&\in[11-\varepsilon,11+\varepsilon],\\
a_3&\in[23-\varepsilon,467/20+\varepsilon],\\
a_4&\in[13/2-\varepsilon,13/2+\varepsilon],\\
a_5&\in[179/20-\varepsilon,9+\varepsilon],\\
a_6&\in[1-\varepsilon,1+\varepsilon].
\end{aligned}
\]
The leading coefficient remains exactly one. When \(\varepsilon>0\), all seven nonleading coefficient intervals have positive width.

### Theorem

For every \(0\le\varepsilon\le\varepsilon_*\):

1. Every actual member of \(B_\varepsilon\) is strictly Hurwitz.
2. Writing
   \[
   a(i\omega)=E_a(t)+i\omega O_a(t),\qquad t=\omega^2,
   \]
   one has
   \[
   \boxed{
   F(t)E_a(t)+tG(t)O_a(t)
   \ge(\gamma-19\varepsilon)(1+t)^6
   \ge\frac{\gamma}{2}(1+t)^6>0
   }
   \]
   for every actual member and every \(t\ge0\).
3. Consequently, the **same** \(q\) is a monic common equal-degree SPR numerator:
   \[
   \operatorname{Re}\frac{q(i\omega)}{a(i\omega)}>0
   \qquad
   (a\in B_\varepsilon,\ \omega\in\mathbb R).
   \]
4. Its even test has roots \((1/2,2,4)\), strictly inside the required common root intervals. It has strictly positive pairings on all nonzero actual odd-moment-cone combinations, including all R4 rays, both R5 orientations, zero-odd singletons and same-frequency cancellation rays.

The same conclusion holds for every nonempty independent coefficient subbox of \(B_\varepsilon\).

---

## 2. Every member of the core box is strictly Hurwitz

For \(a\in B_0\), write
\[
E_a(t)=F(t)+c,\qquad c=a_0-4\in[-1,1].
\]
The actual odd endpoint cubics are
\[
L(t)=
\left(\frac{19}{20}-t\right)
\left(\frac72-t\right)
\left(\frac92-t\right),
\qquad
U(t)=G(t).
\]
Their difference is
\[
U(t)-L(t)=\frac3{80}+\frac7{20}t+\frac1{20}t^2>0
\quad(t\ge0),
\]
and coefficient independence gives
\[
L(t)\le O_a(t)\le U(t).
\]

Set
\[
(a,b,c_1,d,e,f)
=\left(\frac{19}{20},1,3,\frac72,\frac92,5\right).
\]
The symbol \(c_1\) here is a root marker, not the constant perturbation \(c\).

Every actual odd cubic has a root in each of
\[
[a,b],\qquad[c_1,d],\qquad[e,f].
\]
These intervals are disjoint. Since the cubic has degree three, these are exactly its three roots, and all are simple.

On the three closed odd bands, the following uniform bounds hold:
\[
\begin{array}{c|c}
\text{Band}&\text{Bound on }F\\ \hline
[19/20,1]&F\le-27/20\\
[3,7/2]&F\ge9/4\\
[9/2,5]&F\le-5.
\end{array}
\]
The middle bound follows from \(F''(t)=13-6t<0\) there and
\[
F(3)=5/2,\qquad F(7/2)=9/4.
\]
The other two follow directly from the factored form.

Therefore every actual even cubic \(E_a=F+c\), \(|c|\le1\), is strictly negative, positive and negative, respectively, on these three bands. Also \(E_a(0)\ge3>0\). It follows that it has exactly one simple root in each of
\[
(0,19/20),\qquad(1,3),\qquad(7/2,9/2).
\]

Thus the actual even and odd roots strictly interlace for **every independent coefficient choice**. All original \(s\)-coefficients are positive, so the orientation condition at the real point \(s=1\) is positive.

The classical Hermite–Biehler criterion proves that every member of \(B_0\) is strictly Hurwitz. This is an all-member proof, not a numerical root calculation or finite-corner sampling inference.

In particular, \(q\in B_0\), so \(q\) itself is strictly Hurwitz.

---

## 3. A positive pairing on the entire core box

Define
\[
P_a(t)=F(t)E_a(t)+tU(t)O_a(t).
\]
Since \(E_a=F+c\), \(|c|\le1\),
\[
F(t)E_a(t)\ge F(t)^2-|F(t)|\ge-\frac14.
\]

The only intervals where \(L\) and \(U\) have opposite signs are
\[
J_1=[19/20,1],\qquad
J_2=[3,7/2],\qquad
J_3=[9/2,5].
\]
Outside their union,
\[
U(t)O_a(t)\ge0.
\]

Use the three even-root neighborhoods
\[
I_1=[1/4,3/4],\quad
I_2=[3/2,5/2],\quad
I_3=[15/4,17/4].
\]
These neighborhoods and the odd bands are disjoint. Their complement is handled separately.

### 3.1 First even-root neighborhood

On \(I_1\),
\[
U(t)\ge\frac{153}{64}>2,\qquad
L(t)\ge\frac{33}{16}>2.
\]
Thus \(O_a\ge L>2\), and \(t\ge1/4\) gives
\[
tUO_a\ge1.
\]
Consequently,
\[
\boxed{P_a(t)\ge3/4\qquad(t\in I_1).}
\]

### 3.2 Second even-root neighborhood

On \(I_2\), \(O_a\le U<0\), and
\[
|U(t)|=(t-1)(3-t)(5-t)\ge\frac58.
\]
Hence
\[
tUO_a\ge tU^2\ge\frac{75}{128},
\]
and therefore
\[
\boxed{P_a(t)\ge43/128\qquad(t\in I_2).}
\]

### 3.3 Third even-root neighborhood

On \(I_3\),
\[
L(t)=(t-19/20)(t-7/2)(9/2-t)\ge\frac7{40}>\frac18,
\]
while
\[
U(t)=(t-1)(t-3)(5-t)\ge\frac{99}{64}>1.
\]
Since \(t\ge15/4\),
\[
tUO_a\ge\frac{15}{32},
\]
so
\[
\boxed{P_a(t)\ge7/32\qquad(t\in I_3).}
\]

### 3.4 First odd band

On \(J_1\), \(L\le0\le U\), with
\[
U\le\frac{3321}{8000}<\frac12,\qquad
|L|\le\frac{3621}{8000}<\frac12.
\]
As \(t\le1\),
\[
tUO_a\ge tUL\ge-\frac14.
\]
Also \(|F|\ge27/20\), so
\[
F E_a\ge\frac{27}{20}\left(\frac{27}{20}-1\right)=\frac{189}{400}.
\]
Therefore
\[
\boxed{P_a(t)\ge89/400\qquad(t\in J_1).}
\]

### 3.5 Middle odd band: the sharper product bound

On \(J_2\), \(L\le0\le U\), and
\[
U|L|
=(t-1)(5-t)(t-19/20)(9/2-t)(t-3)(7/2-t).
\]

For every \(t\in[3,7/2]\),
\[
(t-1)(5-t)=4-(t-3)^2\le4,
\]
\[
(t-19/20)(9/2-t)\le
(3-19/20)(9/2-3)=\frac{123}{40},
\]
and
\[
(t-3)(7/2-t)\le\frac1{16}.
\]
The second product is decreasing on this interval: its derivative is \(109/20-2t<0\).

Using \(t\le7/2\),
\[
tUO_a\ge-tU|L|\ge-\frac{861}{320}.
\]
Meanwhile \(F\ge9/4\), so
\[
F E_a\ge\frac94\left(\frac94-1\right)=\frac{45}{16}.
\]
It follows that
\[
\boxed{P_a(t)\ge39/320\qquad(t\in J_2).}
\]

### 3.6 Last odd band

On \(J_3\), \(L\le0\le U\), and
\[
U|L|
=(t-1)(t-3)(t-19/20)(t-7/2)(5-t)(t-9/2).
\]
The bounds
\[
\begin{gathered}
t\le5,\quad t-1\le4,\quad t-3\le2,\\
t-19/20\le81/20,\quad t-7/2\le3/2,\\
(5-t)(t-9/2)\le1/16
\end{gathered}
\]
give
\[
tUO_a\ge-\frac{243}{16}.
\]
Since \(|F|\ge5\),
\[
F E_a\ge5(5-1)=20.
\]
Thus
\[
\boxed{P_a(t)\ge77/16\qquad(t\in J_3).}
\]

### 3.7 The remaining frequencies

Outside the three \(I_j\), the absolute value of \(F\) has the following bounds:
\[
\begin{array}{c|c}
\text{Interval}&|F(t)|\text{ lower bound}\\ \hline
[0,1/4]&105/64\\
[3/4,3/2]&65/64\\
[5/2,15/4]&91/64\\
[17/4,\infty)&135/64.
\end{array}
\]
The middle two use concavity of \(-F\) and \(F\), respectively; the first and last follow from the factored form.

Outside the odd bands as well, \(UO_a\ge0\). Hence
\[
P_a(t)\ge
\frac{65}{64}\left(\frac{65}{64}-1\right)
=\frac{65}{4096}.
\]

Together, the seven cases cover every \(t\ge0\). Their smallest displayed bound is \(65/4096\), proving
\[
\boxed{
P_a(t)\ge m=\frac{65}{4096}>0
\quad(a\in B_0,\ t\ge0).
}
\]

This already proves strict common-SPR synthesis for the entire enlarged four-dimensional core box.

---

## 4. A quantitative tail bound

For \(t\ge6\), \(O_a\le U<0\), and
\[
|U(t)|=(t-1)(t-3)(t-5)
\ge\frac56t\cdot\frac12t\cdot\frac16t
=\frac5{72}t^3.
\]
Also \(F E_a\ge0\) there. Therefore
\[
P_a(t)\ge\frac{25}{5184}t^7.
\]

Since
\[
(1+t)^6\le(7/6)^6t^6<3t^6
\quad(t\ge6),
\]
we obtain
\[
\frac{P_a(t)}{(1+t)^6}\ge\frac{25}{2592}.
\]

For \(0\le t\le6\), the preceding global bound gives
\[
P_a(t)\ge m\ge\frac{m}{7^6}(1+t)^6.
\]
Because \(25/2592>\gamma=m/7^6\), both ranges yield
\[
\boxed{
P_a(t)\ge\gamma(1+t)^6
\quad(a\in B_0,\ t\ge0).
}
\]

---

## 5. Enlargement in every nonleading coefficient

Every \(a\in B_\varepsilon\) can be written
\[
a=a_*+\delta a,\qquad a_*\in B_0,
\]
with
\[
|\delta a_j|\le\varepsilon\quad(0\le j\le6),
\qquad \delta a_7=0.
\]
This follows coordinatewise by projection onto the core intervals.

The parity perturbations satisfy
\[
|\delta E(t)|
\le\varepsilon(1+t+t^2+t^3)
\le\varepsilon(1+t)^3,
\]
and
\[
|\delta O(t)|
\le\varepsilon(1+t+t^2)
\le\varepsilon(1+t)^2.
\]
Direct coefficient comparison gives
\[
|F(t)|\le4(1+t)^3,\qquad
|G(t)|\le15(1+t)^3.
\]
Thus
\[
\begin{aligned}
|F\delta E+tG\delta O|
&\le4\varepsilon(1+t)^6+
15\varepsilon t(1+t)^5\\
&\le19\varepsilon(1+t)^6.
\end{aligned}
\]
Combining this with the core bound proves
\[
\boxed{
F E_a+tG O_a
\ge(\gamma-19\varepsilon)(1+t)^6
\ge\frac{\gamma}{2}(1+t)^6>0.
}
\]

### All-member Hurwitz proof for the enlarged box

For a fixed enlarged member, use the coefficient path
\[
a_\lambda=a_*+\lambda\delta a,\qquad0\le\lambda\le1.
\]
The preceding positive pairing holds along the entire path. Therefore no \(a_\lambda\) has a zero on the imaginary axis, including zero.

The path is monic of fixed degree seven with bounded coefficients, so its roots have a uniform Cauchy bound. Roots cannot escape through infinity. By continuity of polynomial roots, a change from strict Hurwitz stability would therefore require an imaginary-axis crossing.

The initial member \(a_*\) is strictly Hurwitz by Section 2. No crossing is possible. Thus the final member—and every member of \(B_\varepsilon\)—is strictly Hurwitz.

This proves stability for every coefficient choice, not merely for corners.

Finally,
\[
\operatorname{Re}\frac{q(i\omega)}{a(i\omega)}
=
\frac{F(t)E_a(t)+tG(t)O_a(t)}
{E_a(t)^2+tO_a(t)^2}>0.
\]
Both polynomials are monic septics, so their ratio tends to one at infinite frequency.

---

## 6. The exact actual-ray consumer

The common test is
\[
\boxed{F(t)=(1/2-t)(2-t)(4-t).}
\]

For the core box,
\[
\frac12<\frac{19}{20},\qquad
1<2<3,\qquad
\frac72<4<\frac92,
\]
so all three roots satisfy the required strict interior placements.

The same is true for each enlarged box at its own actual endpoint bands. Indeed, the unchanged even polynomial \(F\) is an actual even component in \(B_\varepsilon\). Every actual odd component can be paired with it. The all-member Hurwitz theorem and strict interlacing therefore place every first odd root in \((1/2,2)\), every second odd root in \((2,4)\), and every third odd root after \(4\). The endpoint-band ordering from the frozen actual-box interface then gives the required strict placements.

More strongly, let a nonzero finite family of positive-weight actual atoms satisfy all four signed odd-moment inequalities:
\[
R_1=\sum_iw_it_iO_i\le0,\quad
R_3=-\sum_iw_it_i^2O_i\le0,
\]
\[
R_5=\sum_iw_it_i^3O_i\le0,\quad
R_7=-\sum_iw_it_i^4O_i\le0.
\]
Then
\[
\sum_iw_it_iG(t_i)O_i
=15R_1+23R_3+9R_5+R_7\le0.
\]
Consequently,
\[
\begin{aligned}
\sum_iw_iF(t_i)E_i
&=\sum_iw_iP_i-
 \left(15R_1+23R_3+9R_5+R_7\right)\\
&\ge\sum_iw_iP_i>0.
\end{aligned}
\]

This applies to the **actual pointwise minimizing even envelope**, since every selected parity combination is an actual member of the same box. It also applies without alteration to:

- every R4 placement and omitted active moment;
- positive-first and negative-first R5 rays;
- zero-odd singleton rays;
- same-frequency opposite-odd cancellation rays.

No zero odd value is divided by. No orientation, node placement, envelope branch or frequency interval is omitted.

The coefficient vector of \(q\), in the raw-row order, is
\[
(4,15,11,23,13/2,9,1,1),
\]
with every coordinate strictly positive. Its positive pairing with every actual row also directly excludes any all-eight-strict-negative aggregate for these boxes.

---

## 7. Complete optional exact verifier — NOT RUN

**Execution status:** NOT RUN. No stdout, exit status, duration, memory measurement or computational PASS is claimed.

**Proposed filename:** `interior-common-spr-exact-verifier-v1.py`

**Proposed argv:** `python3 -B interior-common-spr-exact-verifier-v1.py`

The program uses standard-library exact rational arithmetic. It checks the displayed rational constants, checks the numerator’s Hurwitz determinants, and uses exact Sturm chains to check positivity on the complete positive half-axis for all four actual parity-envelope pairings of both the core box and the maximally enlarged box. It is not a frequency grid.

It has a cooperative 50-second guard, no network/file/subprocess operations and no random search. Its actual runtime has not been measured. The written theorem does not depend on executing it.

Below, the text after each `C|` is one complete source line. Strip only that prefix and retain the line breaks.

BEGIN SOURCE

C|from fractions import Fraction as Q
C|from time import monotonic
C|
C|DEADLINE = monotonic() + 50.0
C|
C|def guard():
C|    if monotonic() > DEADLINE:
C|        raise TimeoutError("cooperative 50-second calculation limit")
C|
C|def need(condition, reason):
C|    guard()
C|    if not condition:
C|        raise ValueError(reason)
C|
C|def trim(values):
C|    guard()
C|    out = [Q(value) for value in values] or [Q(0)]
C|    while len(out) > 1 and out[-1] == 0:
C|        out.pop()
C|    return tuple(out)
C|
C|ZERO = (Q(0),)
C|
C|def add(p, q):
C|    return trim(
C|        (p[i] if i < len(p) else Q(0))
C|        + (q[i] if i < len(q) else Q(0))
C|        for i in range(max(len(p), len(q)))
C|    )
C|
C|def scale(p, value):
C|    return trim(value * coefficient for coefficient in p)
C|
C|def multiply(p, q):
C|    out = [Q(0)] * (len(p) + len(q) - 1)
C|    for i, a in enumerate(p):
C|        guard()
C|        for j, b in enumerate(q):
C|            out[i + j] += a * b
C|    return trim(out)
C|
C|def derivative(p):
C|    return trim(i * p[i] for i in range(1, len(p)))
C|
C|def divrem(p, q):
C|    p, q = trim(p), trim(q)
C|    need(q != ZERO, "polynomial division by zero")
C|    quotient = [Q(0)] * max(1, len(p) - len(q) + 1)
C|    remainder = p
C|    while remainder != ZERO and len(remainder) >= len(q):
C|        guard()
C|        shift = len(remainder) - len(q)
C|        factor = remainder[-1] / q[-1]
C|        quotient[shift] += factor
C|        updated = list(remainder)
C|        for j, value in enumerate(q):
C|            updated[shift + j] -= factor * value
C|        remainder = trim(updated)
C|    return trim(quotient), remainder
C|
C|def normalize_positive(p):
C|    p = trim(p)
C|    if p == ZERO:
C|        return p
C|    return scale(p, Q(1) / abs(p[-1]))
C|
C|def sign(value):
C|    return (value > 0) - (value < 0)
C|
C|def variations(values):
C|    signs = [sign(value) for value in values if value != 0]
C|    return sum(a != b for a, b in zip(signs, signs[1:]))
C|
C|def sturm_chain(p):
C|    first = normalize_positive(p)
C|    second = normalize_positive(derivative(first))
C|    if second == ZERO:
C|        return (first,)
C|    chain = [first, second]
C|    while True:
C|        guard()
C|        _, remainder = divrem(chain[-2], chain[-1])
C|        if remainder == ZERO:
C|            break
C|        chain.append(normalize_positive(scale(remainder, Q(-1))))
C|        need(len(chain) <= len(first), "Sturm degrees must decrease")
C|    return tuple(chain)
C|
C|def positive_on_half_axis(p, label):
C|    p = trim(p)
C|    need(p[0] > 0, label + ": positive value at zero")
C|    need(p[-1] > 0, label + ": positive leading coefficient")
C|    chain = sturm_chain(p)
C|    at_zero = variations(poly[0] for poly in chain)
C|    at_infinity = variations(poly[-1] for poly in chain)
C|    count = at_zero - at_infinity
C|    need(count == 0, label + ": no positive real roots")
C|    print(label + ": positive_roots=" + str(count)
C|          + ", degree=" + str(len(p) - 1))
C|
C|def root_product(roots):
C|    p = (Q(1),)
C|    for root in roots:
C|        p = multiply(p, (Q(root), Q(-1)))
C|    return p
C|
C|F = root_product((Q(1, 2), Q(2), Q(4)))
C|G = root_product((Q(1), Q(3), Q(5)))
C|L = root_product((Q(19, 20), Q(7, 2), Q(9, 2)))
C|need(F == (Q(4), Q(-11), Q(13, 2), Q(-1)), "F expansion")
C|need(G == (Q(15), Q(-23), Q(9), Q(-1)), "G expansion")
C|need(
C|    L == (Q(1197, 80), Q(-467, 20), Q(179, 20), Q(-1)),
C|    "L expansion",
C|)
C|need(
C|    add(G, scale(L, Q(-1)))
C|    == (Q(3, 80), Q(7, 20), Q(1, 20)),
C|    "actual odd width",
C|)
C|
C|m = Q(65, 4096)
C|gamma = m / (7 ** 6)
C|epsilon = gamma / 38
C|margins = (
C|    Q(3, 4),
C|    Q(43, 128),
C|    Q(7, 32),
C|    Q(27, 20) * (Q(27, 20) - 1) - Q(1, 4),
C|    Q(9, 4) * (Q(9, 4) - 1) - Q(861, 320),
C|    Q(5) * (Q(5) - 1) - Q(243, 16),
C|    Q(65, 64) * (Q(65, 64) - 1),
C|)
C|need(
C|    margins == (
C|        Q(3, 4), Q(43, 128), Q(7, 32), Q(89, 400),
C|        Q(39, 320), Q(77, 16), Q(65, 4096),
C|    ),
C|    "displayed seven-region margins",
C|)
C|need(min(margins) == m, "global core margin")
C|need(Q(25, 2592) > gamma, "tail exceeds normalized margin")
C|need(Q(7, 6) ** 6 < 3, "tail normalization")
C|need(gamma - 19 * epsilon == gamma / 2, "enlargement margin")
C|need(0 < epsilon < Q(1, 100), "small positive enlargement")
C|
C|core = (
C|    (Q(3), Q(5)),
C|    (Q(1197, 80), Q(15)),
C|    (Q(11), Q(11)),
C|    (Q(23), Q(467, 20)),
C|    (Q(13, 2), Q(13, 2)),
C|    (Q(179, 20), Q(9)),
C|    (Q(1), Q(1)),
C|)
C|enlarged = tuple((lo - epsilon, hi + epsilon) for lo, hi in core)
C|need(all(0 < lo <= hi for lo, hi in enlarged), "positive intervals")
C|need(all(lo < hi for lo, hi in enlarged), "seven positive widths")
C|
C|q_coefficients = (
C|    Q(4), Q(15), Q(11), Q(23), Q(13, 2), Q(9), Q(1), Q(1)
C|)
C|need(
C|    tuple(((-1) ** r) * q_coefficients[2 * r] for r in range(4)) == F,
C|    "numerator even parity",
C|)
C|need(
C|    tuple(((-1) ** r) * q_coefficients[2 * r + 1] for r in range(4)) == G,
C|    "numerator odd parity",
C|)
C|need(all(value > 0 for value in q_coefficients), "positive raw separator")
C|
C|def actual_endpoint(bounds, even_high, odd_high):
C|    coefficients = [Q(0)] * 8
C|    for r in range(4):
C|        high = (r % 2 == 1) ^ even_high
C|        coefficients[2 * r] = bounds[2 * r][int(high)]
C|    for r in range(3):
C|        high = (r % 2 == 1) ^ odd_high
C|        coefficients[2 * r + 1] = bounds[2 * r + 1][int(high)]
C|    coefficients[7] = Q(1)
C|    need(
C|        all(lo <= value <= hi
C|            for value, (lo, hi) in zip(coefficients, bounds)),
C|        "actual endpoint membership",
C|    )
C|    even = tuple(((-1) ** r) * coefficients[2 * r] for r in range(4))
C|    odd = tuple(((-1) ** r) * coefficients[2 * r + 1] for r in range(4))
C|    return even, odd
C|
C|for box_label, bounds in (("core", core), ("enlarged", enlarged)):
C|    for even_high in (False, True):
C|        for odd_high in (False, True):
C|            guard()
C|            even, odd = actual_endpoint(bounds, even_high, odd_high)
C|            pairing = add(multiply(F, even), (Q(0),) + multiply(G, odd))
C|            need(len(pairing) == 8 and pairing[-1] == 1,
C|                 "monic degree-seven pairing")
C|            label = (
C|                box_label + "_E" + str(int(even_high))
C|                + "_O" + str(int(odd_high))
C|            )
C|            positive_on_half_axis(pairing, label)
C|
C|def determinant(matrix):
C|    a = [list(row) for row in matrix]
C|    result = Q(1)
C|    for column in range(len(a)):
C|        guard()
C|        pivot_row = next(
C|            (r for r in range(column, len(a)) if a[r][column] != 0),
C|            None,
C|        )
C|        if pivot_row is None:
C|            return Q(0)
C|        if pivot_row != column:
C|            a[column], a[pivot_row] = a[pivot_row], a[column]
C|            result = -result
C|        pivot = a[column][column]
C|        result *= pivot
C|        for r in range(column + 1, len(a)):
C|            factor = a[r][column] / pivot
C|            for j in range(column + 1, len(a)):
C|                a[r][j] -= factor * a[column][j]
C|            a[r][column] = Q(0)
C|    return result
C|
C|descending = tuple(reversed(q_coefficients))
C|for size in range(1, 8):
C|    matrix = []
C|    for i in range(size):
C|        row = []
C|        for j in range(size):
C|            index = 2 * j - i + 1
C|            row.append(descending[index] if 0 <= index < 8 else Q(0))
C|        matrix.append(row)
C|    value = determinant(matrix)
C|    need(value > 0, "positive numerator Hurwitz determinant")
C|    print("q_Hurwitz_Delta_" + str(size) + "=" + str(value))
C|
C|print("core_margin=" + str(m))
C|print("normalized_margin=" + str(gamma))
C|print("all_coefficient_epsilon=" + str(epsilon))
C|print("exact_algebraic_checks=PASS")
C|print("scope=the stated boxes only; not arbitrary septic interval families")

END SOURCE

No output from this proposed execution is reported as observed evidence.

---

## 8. Provenance, chronology and assurance

Before scientific work, I read the manifest, freeze receipt, dispatch receipt, parent metadata supply and all seven permission/status controls. A pre-body acknowledgment was delivered before the scientific packet read.

The complete literal packet was then read in consecutive raw windows:
**1–225, 226–450, 451–675, 676–900 and 901–950**, including all source endings.

The assigned bindings are parent-supplied observations:

- Manifest: `1893bb990fe84d9506b5f757e4c6151748e0e817a6e8c1c8c52d3dbeeb9f072d`
- Freeze receipt: `ee9c9ec28f1355d87693513f3bf4414833da4464dbb379eb01ec64217d36d885`
- Literal packet: `b4126a855577077ccf4c5db387c4999508b85640fd9e00a6862aaf18816a2543`

The supplied **11:10:50 PDT** observation is a parent observation, not my native start, derivation, completion, hash execution or file-creation time.

After the complete packet read, I searched public literature and inspected the beginning of the sixth-order synthesis paper. That reader response was partial; I do not claim a complete read or import its synthesis theorem. The present argument was developed directly for the stated septics.

The full reader body of Olga Holtz’s [“Hermite–Biehler, Routh–Hurwitz, and total positivity,” Theorem 1](https://arxiv.org/html/math/0512591v1), including its ending, was read. Its classical interlacing criterion is the named external mathematical import in Section 2.

The written construction first established the smaller constant interval \([29/8,35/8]\). A sharper middle-band product bound then enlarged it to \([3,5]\), after which the quantitative seven-coefficient enlargement was derived. Both substantive stages were communicated to the parent. The smaller earlier result remains correct; it is superseded here by the explicitly larger proved region.

Scientific interpreter, CAS, solver, random-search and numerical-root executions: **zero**. No project file was written. The complete body and source are returned for parent materialization under the runtime read-only boundary; no write bypass was attempted.

No held scientific payload, sibling return or excluded consumer was opened. This is an access/use report, not a cognitive-isolation certificate.

The result is an author proof requiring disjoint checking and parent disposition. It is not human, independent-family, formal/kernel, worldwide-status, novelty or priority assurance.

---

## 9. Exact remaining original-target gap

The theorem proves strict synthesis on the explicitly stated actual seven-dimensional region, and therefore on every independent subbox within it. For the frozen example, it supplies the interior common test that the boundary-root obstruction did not supply.

The universal septic problem remains unpaid outside this region:

- There is no proof here that an arbitrary all-Hurwitz independent monic septic box is contained in, or reducible to, the proved region.
- No construction is given for every such arbitrary box.
- No eligible box is shown to lack every possible common test.
- No all-eight-strict-negative actual-member certificate is supplied.

For the proved class, however, there is **no weak-to-strict gap**: the displayed fixed numerator already satisfies strict inequalities for every member and every real frequency.

**Author conclusion:** The actual-box interior route succeeds on an explicit enlarged box and on a genuinely full-seven-coefficient neighborhood, with a complete all-member Hurwitz proof and a single strict common numerator. This is scoped constructive synthesis progress, not universal original-target closure or automatic parent adoption.