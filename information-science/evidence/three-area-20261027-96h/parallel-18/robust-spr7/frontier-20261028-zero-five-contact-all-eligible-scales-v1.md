# Exact synthesis with a zero-root boundary and five imaginary contacts

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** This is a different extreme boundary geometry from the positive-lower-constant five-contact family. It resolves only the explicit family below, not arbitrary septic boxes.

Let the boundary coefficient vectors be
\[
\ell=(0,70,32,86,179/14,18,1),\qquad
u=(20,104,358/11,87,13,19,179/154),
\]
with leading coefficient one. Put \(c=(\ell+u)/2\), and define \(K_\rho\) by independent intervals \([c_j-\rho(u_j-\ell_j)/2,c_j+\rho(u_j-\ell_j)/2]\). For \(\rho>0\) all seven widths are positive.

At \(\rho=1\), the actual parity endpoint cubics factor as
\[
\begin{aligned}
E_-&=-\frac{179}{154}t(t-4)(t-7),& E_+&=-(t-1)(t-2)(t-10),\\
O_-&=-(t-1)(t-7)(t-10),& O_+&=-(t-2)(t-4)(t-13).
\end{aligned}
\]
Consequently the boundary contains a root at \(s=0\) in the two \(E_-\) corners, and five imaginary-axis pairs at actual corner/frequency-squared combinations \((2,1),(3,2),(1,4),(0,7),(2,10)\), using the usual corner order \((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\).

**Exact stability classification.** Every member of \(K_\rho\) is strictly Hurwitz for \(0\le\rho<1\); no box with \(\rho\ge1\) is all-member strictly Hurwitz. At \(\rho<1\), the constant coefficient is strictly positive and the common parity sign sequence at \(t=0,1,2,4,7,10,\infty\) is
\[
(+,+),(-,+),(-,-),(+,-),(+,+),(-,+),(-,-).
\]
The signs at the five finite markers follow from the center signs and boundary extrema; the frozen packet records the exact marker intervals. Thus the even and odd roots occupy alternating disjoint intervals and no denominator can have an imaginary-axis root. The box is connected to the center, whose Routh column is strictly positive; monicity keeps all roots finite under that homotopy. At \(\rho=1\) the zero-root corner is in the box, and every larger box contains it.

## A single common numerator

For every \(0\le\rho<1\), every denominator in \(K_\rho\), and every real frequency, the following fixed monic numerator is strictly positive real:
\[
(b_0,\ldots,b_7)=\left(1,\frac{99941102599}{81462304},
\frac{128192745707}{37028320},\frac{78048311291}{74056640},
\frac{61297192141}{37028320},\frac{125448523153}{814623040},150,1\right).
\]

At the excluded boundary, the four actual corner pairings satisfy exact identities
\[
P_0=t(t-7)^2q_0,\quad P_1=t(t-4)^2q_1,\quad
P_2=(t-1)^2(t-10)^2q_2,\quad P_3=(t-2)^2q_3,
\]
where the residuals \(q_i\) are strictly positive on the half-line. Their positive rational Bernstein leaf counts are 3, 4, 1, 4. The center pairing has a four-leaf compactified bound
\[
\frac{P_{c,b}(t)}{(1+t)^7}\ge
\frac{60730970177313}{298967959076864}>0.
\]
Pairing is affine in the denominator, and its minimum over each independent box is attained at one of the four actual parity corners. Therefore the center bound multiplied by \((1-\rho)\) holds for every member. With \(S_1=1+\sum_j u_j=42767/154\), this gives
\[
\operatorname{Re}\frac{b(i\omega)}{a(i\omega)}\ge
(1-\rho)\frac{668040671950443}{253625819592147337216}>0.
\]
The estimate is not claimed sharp. As in the five-contact packet, the positive numerator excludes every finite nonzero nonnegative atom combination with all coefficient sums nonpositive for any **particular box in this family**; it says nothing about other boxes.

## Exact evidence

Frozen endpoints, root factors, five markers, origin contact, numerator, all four pairing factorizations, Bernstein leaves and constants: `frontier-20261028-zero-five-contact-uniform-numerator-frozen-v1.json`, SHA-256 `db0016d05c0792617af81724ed40875df4fb0eb34521a75fa707afb5c912a763`.

Standalone replay `frontier-20261028-zero-five-contact-independent-replay-kernel-v1.py`, SHA-256 `466776ee1174684420c00506d231c6a32967107f16f8fb3d073eaa34bde5db42`, independently reconstructs the root factorizations, both origin contacts, five imaginary contacts and center signs, center Routh column, 28 rational corner Hurwitz minors at \(999/1000\), all pairing factors and leaves, and the two constants. It rejects corrupted leaf and factor controls. Receipt `frontier-20261028-zero-five-contact-independent-replay-result-v1.json`, SHA-256 `8ac9d7f2bd71a5f52a12e2996066d9be9d5c35c6be064b6a6d544ea286793224`.

The numerator came from exact limiting-tangent feasibility and an exact rational one-variable simplification. The written argument imports elementary root continuity, polynomial signs, interval linearity and Bernstein positivity. Machine checks used integer and `fractions.Fraction` arithmetic in one Eval host. This is not formal verification, cross-vendor review, novelty clearance, or an unrestricted septic verdict.
