# A finite coefficientwise cone for heterogeneous interval radii

**Status: WRITTEN candidate with one WRITTEN-checked-in-kernel example; author result, not parent adoption.** This all-degree sufficient condition certifies all-member Hurwitz stability and an explicit common numerator from the center's coefficients and **independent, unequal** coefficient radii. It is not a necessary condition or an arbitrary-box theorem.

Let \(a(s)=s^n+\sum_{j=0}^{n-1}a_js^j\) be a real monic Hurwitz polynomial. For nonnegative radii \(r_j\), define the independent monic box \(|p_j-a_j|\le r_j\). Write
\[
a(i\sqrt t)=E(t)+i\sqrt t\,O(t),\quad
A(t)=\sum_{\substack{0\le j<n\\j\ \rm even}}r_jt^{j/2},\quad
B(t)=\sum_{\substack{0\le j<n\\j\ \rm odd}}r_jt^{(j-1)/2},
\]
and let
\[
V(t)=E(t)^2+tO(t)^2,\qquad H(t)=A(t)^2+tB(t)^2.
\]
If **every monomial coefficient of \(V-H\) is nonnegative** and its constant coefficient \(a_0^2-r_0^2\) is strictly positive, then every box member is Hurwitz and the fixed numerator \(a\) is common SPR. The conclusion also applies to any subbox.

## Explicit bound

Put \(d=a_0^2-r_0^2>0\), \(\gamma=\min(d,1)/2^{n-1}\), and \(S=\sum_{j=0}^na_j+\sum_{j=0}^{n-1}r_j\). Then
\[
\operatorname{Re}\frac{a(i\omega)}{p(i\omega)}
\ge\frac{\gamma}{2S^2}>0.
\]
Indeed, \(V-H\) has leading coefficient 1 and nonnegative intermediate coefficients, so
\[
V-H\ge d+t^n\ge\gamma(1+t)^n.
\]
For any allowed denominator, Cauchy–Schwarz gives
\[
P_{p,a}(t)\ge V-\sqrt{VH}
=\frac{(V-H)\sqrt V}{\sqrt V+\sqrt H}
\ge\frac{V-H}{2}\ge\frac\gamma2(1+t)^n.
\]
The bound remains valid along the straight path from \(a\) to any box member, excluding imaginary-axis zeros; root continuity and monicity preserve Hurwitz stability. Since a Hurwitz real monic polynomial has positive coefficients, \(|p(i\sqrt t)|\le S(1+t)^{n/2}\), giving the ratio bound. A scaled version follows by applying this test to \(c^{-n}a(cz)\) and radii \(r_jc^{j-n}\).

The coefficientwise test is deliberately sufficient, not asserted necessary: actual interval positivity may hold even when some coefficients of \(V-H\) are negative. It is a finite explicit cone check and does not require optimizing a polynomial numerator.

## Exact heterogeneous septic example

Take \(a=(s+1)^7\), \(r_1=5/2\), and \(r_j=1/2\) for the other six nonleading coefficients. Then
\[
V-H=(3/4)+(1/4)t+(71/4)t^2+(125/4)t^3
+(135/4)t^4+(81/4)t^5+(27/4)t^6+t^7.
\]
The maximum radius exceeds 1, so the uniform-radius \(r<1\) theorem alone does not cover this box. Independent replay checked all 28 strict corner Hurwitz determinants and 72 strictly positive compactified pairing Bernstein coefficients, with actual compactified margin at least \(9/112\).

Frozen example: `frontier-20261029-heterogeneous-radius-cone-example-frozen-v1.json`, SHA-256 `206a92bb074759308c61990fc7db057da35196089a3d3817e30b19d31a5c6134`. Independent checker `frontier-20261029-heterogeneous-radius-cone-example-independent-kernel-v1.py`, SHA-256 `7b68abe83a66fa0eb64d1803d62bb825c9143489bcc06f06a0053c87d25cfd63`; receipt `frontier-20261029-heterogeneous-radius-cone-example-independent-result-v1.json`, SHA-256 `6307b23a1b4a382b6b7ef1012565f805c80b69fa34fcecbb44b6a8d647dd9c08`.

The cone proof uses elementary polynomial coefficient comparison, Cauchy–Schwarz and homotopy; the finite example used exact integers and `fractions.Fraction` on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, unrestricted negative certificate, or arbitrary-box verdict is claimed.
