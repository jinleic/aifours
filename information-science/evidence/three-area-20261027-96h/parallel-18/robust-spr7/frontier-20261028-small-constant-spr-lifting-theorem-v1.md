# Lifting a common SPR numerator by a small positive constant term

**Status: WRITTEN theorem with a WRITTEN-checked-in-kernel full-width septic example; author candidate, not parent adoption.** This gives a constructive positive result for septic boxes with sufficiently small constant coefficient and a lower-degree tail having a common SPR numerator. It does not assert that an arbitrary stable septic box has such a tail or satisfies the smallness condition.

## General lifting theorem

Let \(n\ge2\). Let \(\mathcal Q\) be a nonempty compact set of monic Hurwitz polynomials of degree \(n-1\), and suppose a real exact-degree-\(n-1\) polynomial \(c\) is a common SPR numerator for \(\mathcal Q\). Write
\[
q(i\omega)=E_q(t)+i\omega O_q(t),\qquad
c(i\omega)=F_c(t)+i\omega G_c(t),\qquad t=\omega^2,
\]
and
\[
H_q(t)=F_c(t)E_q(t)+tG_c(t)O_q(t).
\]
The leading coefficient of \(c\) is positive. Compactness and strict positivity give \(\delta>0\) with \(H_q(t)\ge\delta(1+t)^{n-1}\) for all \(q,t\). Choose finite bounds
\[
|O_q(t)|\le M_O(1+t)^{n-1},\qquad
|G_c(t)|\le M_G(1+t)^{n-1}.
\]
For any \(\varepsilon>0\) and \(A>0\) such that
\[
\kappa:=\delta-\varepsilon M_O-A M_G>0,
\]
the **same** polynomial
\[
b(s)=s\,c(s)+\varepsilon
\]
is an exact-degree-\(n\) common SPR numerator for all
\[
p(s)=s\,q(s)+a_0,\qquad q\in\mathcal Q,\quad 0<a_0\le A.
\]
All such \(p\) are strictly Hurwitz. In particular, independent interval uncertainty in \(a_0\) and in the coefficients of \(q\) is allowed.

**Proof.** Direct multiplication gives the exact identity
\[
P_{p,b}(t)=tH_q(t)+\varepsilon a_0
 -\varepsilon tO_q(t)-a_0tG_c(t)
\ge \kappa t(1+t)^{n-1}+\varepsilon a_0>0.
\]
The final inequality includes \(t=0\). Thus \(p\) has no imaginary-axis root. To establish stability without assuming it, fix \(q\): at \(a_0=0\), \(sq\) has one simple root at zero and all other roots in the open left half-plane. For sufficiently small positive \(a_0\), the zero root moves left, since its derivative with respect to \(a_0\) at zero is \(-1/q(0)<0\); the other roots remain left by continuity. Along \(0<a_0\le A\), the displayed positive pairing excludes an imaginary-axis crossing, so the root count remains zero in the right half-plane. The real-part ratio is then strictly positive because its denominator \(|p(i\omega)|^2\) is nonzero. No uniform small-root neighborhood across different \(q\) is needed for that argument.

For an interval \(a_0\in[a_{\min},A]\) with \(a_{\min}>0\), the compactified pairing has the explicit bound
\[
\frac{P_{p,b}(t)}{(1+t)^n}\ge
\min\left\{\frac\kappa2,\frac{\varepsilon a_{\min}}{2^n}\right\}>0,
\]
by splitting at \(t/(1+t)=1/2\). The coefficients of \(b\) are all positive: for any \(q\in\mathcal Q\), the segment \((1-\theta)q+\theta c\) has no imaginary-axis zero because \(\operatorname{Re}(c/q)>0\), and its leading coefficient stays positive, so \(c\) is Hurwitz and all its coefficients are positive. Thus every such box excludes any finite nonpositive-coordinate atom certificate by dotting it with \(b\).

For \(n=7\), this theorem reduces the relevant part of the problem to a degree-six tail and an explicit constant-coefficient inequality. If one imports the existence theorem stated in the public [sixth-order interval preprint](https://arxiv.org/html/2609.26541v1), every robust sextic interval tail supplies some \(c\) and hence some nonzero admissible range of \(a_0\). That is a **named external import**, not independently verified here; the lifting theorem itself needs only the explicitly stated common-\(c\) hypothesis.

## Exact full-width septic example

Take \(q_*(s)=(s+1)^6\) and \(c=q_*\). Let each of its coefficients of degrees 0 through 5 vary independently by \(\pm1/1000\), retaining monic degree six. Since \(|q_*(i\omega)|^2=(1+t)^6\), \(\sum_j|c_j|=64\), and the coefficient perturbation has \(\ell^1\)-size at most \(6/1000\),
\[
H_q(t)/(1+t)^6\ge1-64(6/1000)=77/125.
\]
The same pairing bound and a homotopy to \(q_*\) prove every tail \(q\) is Hurwitz. Take
\[
M_O=32003/1000,\quad M_G=32,\quad
\varepsilon=1/100,\quad A=1/1000,\quad
\kappa=26397/100000>0.
\]
Here the two \(M\)'s are simple sums of absolute odd-part coefficients, and the stronger denominator \((1+t)^6\) makes those bounds valid throughout the half-line.

For \(a_0\in[1/2000,1/1000]\), all seven septic coefficient intervals are nondegenerate:
\[
\begin{aligned}
\ell&=(1/2000,999/1000,5999/1000,14999/1000,19999/1000,14999/1000,5999/1000),\\
u&=(1/1000,1001/1000,6001/1000,15001/1000,20001/1000,15001/1000,6001/1000).
\end{aligned}
\]
The common numerator is
\[
(b_0,\ldots,b_7)=(1/100,1,6,15,20,15,6,1).
\]
The lifting estimate yields \(P/(1+t)^7\ge1/25600000\), and with \(S=1+\sum u_j=64007/1000\),
\[
\operatorname{Re}[b(i\omega)/p(i\omega)]\ge5/524402694272>0.
\]
A separate direct four-corner Bernstein replay gives the stronger compactified pairing bound \(1/200000\); the all-member proof above does not depend on a four-corner stability converse.

## Evidence and limits

- Frozen exact example, bounds, four pairing polynomials and leaves: `frontier-20261028-small-constant-lift-example-frozen-v1.json`, SHA-256 `937a840bd0f554c7cd2bbeed4d0e2cb1cd04bd0292d6e34fd3a43b92dacefaee`.
- Standalone independent checker `frontier-20261028-small-constant-lift-independent-kernel-v1.py`, SHA-256 `fde8c42bcb8d17494d2e4ad713d31e96c8a873c75bb9a560cb25a6e4df22e398`, reconstructs \((s+1)^6\), all bounds, 24 sextic and 28 septic rational corner Hurwitz minors, all four lifting polynomial identities, and every direct Bernstein coefficient. A negative-margin control was rejected. Receipt `frontier-20261028-small-constant-lift-independent-result-v1.json`, SHA-256 `4d7c2034726dedcd785d20a4840138b1bd394b0283b18d86d329a0b61b5793cb`.

The general lifting proof is written mathematics, not a machine-checked universal theorem. Exact example arithmetic used integers and `fractions.Fraction` on one Python Eval host. No formal verification, cross-vendor review, novelty clearance or unrestricted septic verdict is claimed.
