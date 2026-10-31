# A sharp all-degree synthesis theorem around real-rooted centers

**Status: WRITTEN; author candidate, not parent adoption.** This is a constructive positive result for a broad nondegenerate class of independent interval boxes, in every degree. It is not an arbitrary-box theorem.

## Theorem

Let \(n\ge1\), \(c>0\), and
\[
a(s)=\prod_{i=1}^n(s+\alpha_i)=s^n+\sum_{j=0}^{n-1}a_js^j,
\qquad \alpha_i\ge c.
\]
For any \(0\le r<1\), define the independent monic interval family
\[
K_{a,c,r}=\left\{p(s)=s^n+\sum_{j=0}^{n-1}p_js^j:
|p_j-a_j|\le r\,c^{n-j}\right\}.
\]
Every member is strictly Hurwitz, and the **single numerator \(a\)** makes \(a/p\) strictly positive real for every member. This also covers every subbox and any degenerate intervals.

Let \(B=\sum_{j=0}^n a_jc^{j-n}=a(c)/c^n>0\). For \(p\in K_{a,c,r}\) and every real \(\omega\),
\[
\operatorname{Re}\frac{a(i\omega)}{p(i\omega)}
\ge\frac{1-r}{(B+nr)^2}>0.
\]
The universal radius threshold \(r<1\) is sharp in the sense that \(r=1\) cannot be guaranteed for all such centers: for \(a(s)=(s+c)^n\), the lower endpoint of the constant coefficient is zero and that boundary member is not strictly Hurwitz. No claim is made that \(r=1\) fails for every center.

## Proof

Scale \(s=cz\). The monic scaled center is \(A(z)=c^{-n}a(cz)=\prod_i(z+\alpha_i/c)\), with all \(\alpha_i/c\ge1\), and the independent coefficient perturbations of \(P(z)=c^{-n}p(cz)\) each have magnitude at most \(r\). Write, for \(t=\omega_z^2\),
\[
A(i\omega_z)=E(t)+i\omega_zO(t),\qquad
E(t)^2+tO(t)^2=|A(i\omega_z)|^2
=\prod_i\bigl((\alpha_i/c)^2+t\bigr)\ge(1+t)^n.
\]
Define the two nonnegative geometric sums
\[
A_n(t)=\sum_{\substack{0\le j<n\\j\ \rm even}}t^{j/2},\qquad
B_n(t)=\sum_{\substack{0\le j<n\\j\ \rm odd}}t^{(j-1)/2}.
\]
The affine pairing satisfies
\[
\begin{aligned}
P_{P,A}(t)&=\operatorname{Re}\bigl(P(i\sqrt t)\overline{A(i\sqrt t)}\bigr)\\
&\ge |A(i\sqrt t)|^2-r\bigl(|E|A_n+t|O|B_n\bigr)\\
&\ge |A(i\sqrt t)|^2-r|A(i\sqrt t)|\sqrt{A_n^2+tB_n^2}.
\end{aligned}
\]
The last step is Cauchy–Schwarz on \((E,\sqrt t O)\) and \((A_n,\sqrt t B_n)\). Coefficientwise,
\[
A_n(t)^2+tB_n(t)^2\le(1+t)^n.\tag{1}
\]
Indeed, the coefficient of \(t^k\) on the left counts ordered pairs \((i,j)\in\{0,\ldots,n-1\}^2\) with \(i+j=2k\). It is at most \(n\), equals 1 at \(k=0\), and is zero at \(k=n\). For \(1\le k\le n-1\), \(\binom nk\ge n\). All coefficients are nonnegative, proving (1) on \(t\ge0\).

Thus \(\sqrt{A_n^2+tB_n^2}\le(1+t)^{n/2}\le|A(i\sqrt t)|\), and
\[
P_{P,A}(t)\ge(1-r)|A(i\sqrt t)|^2\ge(1-r)(1+t)^n>0.
\]
The same inequality holds along the straight coefficient path from \(A\) to \(P\), so that path has no imaginary-axis root. Since \(A\) is Hurwitz and all leading coefficients are one, homotopy proves \(P\) Hurwitz. Finally \(|P(i\sqrt t)|\le(B+nr)(1+t)^{n/2}\), giving the displayed ratio bound. Scaling back preserves the transfer ratio.

This proof uses elementary factorization, Cauchy–Schwarz, coefficient comparison and root continuity. It is written mathematics, not formal or cross-vendor verification, novelty clearance, a universal positive answer, or an unrestricted negative certificate.
