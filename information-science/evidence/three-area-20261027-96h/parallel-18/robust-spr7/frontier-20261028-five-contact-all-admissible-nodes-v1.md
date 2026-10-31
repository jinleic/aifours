# All admissible last-node ratios in the five-contact family

**Status: WRITTEN-checked-in-kernel; author candidate, not parent adoption.** For the five-contact boundary construction with first four squared-frequency nodes \((1,2,3,6)\), this theorem covers **every** coefficient-admissible fifth node \(w>6\), every admissible remaining shape parameter, and every midpoint-centered radial subbox of scale \(0\le\rho<1\). The numerator has exact degree seven and is independent of \(\rho\). This is a special-family positive result, not the original arbitrary-box decision.

## Family and complete admissible domain

Let \(0<u<1<2<3<6<w<v\), \(\lambda>0\), and define the four boundary parity polynomials
\[
\begin{aligned}
E_-&=-\lambda(t-u)(t-3)(t-6),& E_+&=-(t-1)(t-2)(t-w),\\
O_-&=-(t-1)(t-6)(t-w),& O_+&=-(t-2)(t-3)(t-v).
\end{aligned}
\]
For \(a(s)=s^7+\sum_{j=0}^6a_js^j\), set \(E_a(t)=a_0-a_2t+a_4t^2-a_6t^3\) and \(O_a(t)=a_1-a_3t+a_5t^2-t^3\). The endpoints specify four actual parity corners \((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\) of an independent coefficient box when the widths are nonnegative. The respective even widths are
\[
2w-18\lambda u,\quad \lambda(9u+18)-(2+3w),\quad w+3-\lambda(u+9),\quad\lambda-1,
\]
and the odd widths are \(6(v-w),\ 7w-5v,\ v-w-2\).

Consequently the exact nonnegative-width conditions are
\[
\begin{gathered}
 w+2\le v\le 7w/5,\\
 \max\!\left(1,\frac{2+3w}{9u+18}\right)\le\lambda\le
 \min\!\left(\frac{w+3}{u+9},\frac{w}{9u}\right),\qquad 0<u<1.
\end{gathered}
\]
They force precisely
\[
\boxed{\;19/3\le w\le18\;},\qquad
\frac{9w-36}{6w+25}\le u\le
\min\!\left(w-6,\frac w9,\frac{w}{w+1}\right).
\]
The bounds are necessary: the lower-versus-upper \(\lambda\) comparisons yield \(u\ge(9w-36)/(6w+25)\), \(u\le w-6\), \(u\le w/9\), and \(u\le w/(w+1)\). Comparing the first with \(w-6\) gives \((3w-19)(w+3)\ge0\); comparing it with \(w/(w+1)\) gives \((w-18)(3w+2)\le0\). Conversely, the box can be nonempty exactly on the displayed interval: choose \(u\) between the displayed limits, any \(\lambda\) in the stated interval, and any \(v\) in its stated interval. Equality and zero-width coefficients are allowed. At \(w=19/3\), \(u=1/3,\lambda=1\); at \(w=18\), \(u=18/19,\lambda=19/9\).

For each admissible boundary box let \(K_\rho\) be its coefficientwise midpoint-centered radial subbox. Every \(K_\rho\), \(0\le\rho<1\), is strictly Hurwitz and has a common real numerator \(b\) of degree exactly seven. At \(\rho=1\) actual corners have imaginary-axis roots at each of the five contact frequencies; any larger centered box contains that ineligible boundary member. Common positive frequency scaling also covers contact ratios \(c^2(1,2,3,6,w)\), \(c>0\).

## Numerator, positivity, and stability

Set \(P_{a,b}(t)=E_a(t)E_b(t)+tO_a(t)O_b(t)\). At the contacts \((E_+,O_-,1)\), \((E_+,O_+,2)\), \((E_-,O_+,3)\), \((E_-,O_-,6)\), and \((E_+,O_-,w)\), impose \(\partial_tP_{a,b}=0\). Fix \(b_0=b_7=1\), \(b_6=1000\), and solve the resulting five linear equations for \(b_1,\ldots,b_5\). Writing their coefficient matrix as \(A\), right-hand side as \(r\), \(D=\det A\), and \(D_j\) for the determinant with column \(j\) replaced by \(r\), the solution has \(b_j=D_j/D\). The exact checks below show \(D<0\) on every parameter branch used here.

For the positive unnormalized vector use
\[
\widehat b_0=\widehat b_7=-D d^3Q^6,\qquad
\widehat b_6=-1000D d^3Q^6,\qquad
\widehat b_j=-D_jd^3Q^6\quad(1\le j\le5),
\]
where \(Q>0\) is the appropriate denominator of the affine \(u\)-parameterization and \(d>0\) is the product of the denominators of the active \(\lambda\)-endpoints; the exact branches are specified below and in the frozen records. The normalized numerator is the same Cramer solution on overlapping branches. All its coefficients are positive.

The finite certificate proves each boundary \(P_{a,\widehat b}\) nonnegative on \(t\ge0\), and proves the midpoint pairing satisfies
\[
P_{a_{\rm mid},\widehat b}(t)\ge m(1+t)^7,\qquad
m=215808507516026880>0.
\]
The bound is for the branch-dependent **unnormalized** vector; the previous \([8,18]\) minimum is larger. Since the coefficient sum of every boundary upper endpoint plus the monic term is less than 500, affine interpolation from the midpoint to the four actual boundary corners gives for all \(a\in K_\rho\) and all real \(\omega\)
\[
\operatorname{Re}\frac{\widehat b(i\omega)}{a(i\omega)}
\ge (1-\rho)\frac{2697606343950336}{3125}>0.
\]
Here the inequality uses \(|a(i\omega)|^2\le 500^2(1+\omega^2)^7\). Thus it excludes finite nonzero nonnegative atom combinations with all coefficient sums nonpositive **for these boxes only**.

At the markers \(0,1,2,3,6,w,\infty\), the signs of \((E_a,O_a)\) for \(\rho<1\) are respectively
\[
(+,+),\ (-,+),\ (-,-),\ (+,-),\ (+,+),\ (-,+),\ (-,-).
\]
At each positive marker the relevant boundary endpoint difference is nonzero because the indicated roots are distinct, even when some coefficient widths vanish. The six alternating root bands prove the midpoint Hurwitz by the odd-degree Hermite–Biehler criterion and exclude imaginary-axis roots throughout each connected box; homotopy then proves every member Hurwitz.

## Complete sub-eight parameterization

Write
\[
u_0=\frac{9w-36}{6w+25},\quad
u_a=\frac{3w-16}{9},\quad
u_s=\frac{9w}{8w+27},\quad
L=\frac{2+3w}{9u+18},\quad
H_s=\frac{w+3}{u+9},\quad H_p=\frac{w}{9u}.
\]
Parameterize each listed \(u\)-interval affinely by \(x\in[0,1]\), each listed \(\lambda\)-interval by \(z\in[0,1]\), and \(v\in[w+2,7w/5]\) by \(y\in[0,1]\). The positive \(d\) and \(Q\) used above are in the last column.

| \(w\) interval | branch | \(u\) interval | \(\lambda\) interval | \((d,Q)\) |
|---|---|---|---|---|
| \([19/3,27/4]\) | lower 1 | \([u_0,u_a]\) | \([L,H_s]\) | \(((9u+18)(u+9),\ 9(6w+25))\) |
| \([19/3,27/4]\) | lower 2 | \([u_a,w-6]\) | \([1,H_s]\) | \((u+9,\ 9)\) |
| \([27/4,8]\) | over 1 | \([u_0,u_a]\) | \([L,H_s]\) | \(((9u+18)(u+9),\ 9(6w+25))\) |
| \([27/4,8]\) | over 2 | \([u_a,u_s]\), in either orientation | \([1,H_s]\) | \((u+9,\ 9(8w+27))\) |
| \([27/4,8]\) | over 3 | \([u_s,w/9]\) | \([1,H_p]\) | \((9u,\ 9(8w+27))\) |

For the lower interval, \(u_0\le u_a\le w-6\le u_s\), so the two branches give exactly the admissible set. In the upper interval, \(u_a\) and \(u_s\) exchange order once. If \(u_a\le u_s\), the three branches are exact. If \(u_s<u_a\), over 1 and over 3 overlap and together contain every feasible point: on their overlap the true interval \([L,H_p]\) is contained in \([L,H_s]\) and in \([1,H_p]\). Over 2 is harmless additional coverage. Some synthetic parameter points in this algebraic overcover have unordered coefficient endpoints; they are **not** claimed to be interval boxes. The polynomial tensor check is valid there and only actual nonnegative-width points are used in the theorem. For \([8,18]\), use the two exact branches in `frontier-20261028-five-contact-maximal-node-domain-v1.md`.

## Continuum certificate and exact replay

On each sub-eight branch put \(u=N/Q\), with \(N\) of \(w\)-degree at most two and \(Q\) of degree at most one. Write the interpolated \(\lambda\) as \(Q N_\lambda/(AB)\). On lower/over 1 take \(A=9N+18Q,\ B=N+9Q\); on lower/over 2 take \(A=Q,\ B=N+9Q\); on over 3 take \(A=Q,\ B=9N\). Then \(d=AB/Q^2\), \(A,B\) have \(w\)-degree at most two, and \(N_\lambda\) at most three. An \(E_-\) coefficient has numerator degree at most five over \(AB\); only two tangent rows involve \(E_-\). After multiplying the tangent or Cramer determinant by \((AB)^2\), the fixed-contact rows have degree bounds \(1,1,5,5\), and the moving-contact row at \(t=w\) has bound 6. Thus the determinant numerator has degree at most 18; the remaining \(AB\) factor in \(d^3Q^6=(AB)^3\) gives numerator degree at most 22, and each pairing degree at most 23. In \(x,z,y\), the corresponding bounds are \(6,3,3\). Exact division by the contact squares, including \((t-w)^2\), cannot increase the degree in \(w\), and frequency Bernstein conversion is linear.

For each sub-eight branch, 116 scalar numerator, residual and midpoint-leaf polynomials therefore have tensor degree at most \((23,6,3,3)\). All \(311{,}808\) Bernstein coefficients per branch are strictly positive. An independently implemented exact replay checked all **1,559,040** sub-eight coefficients, including the exact minima, using integer Bareiss determinants, direct convolution and exact double-root division, dyadic de Casteljau subdivision, and monomial-Vandermonde/power-to-Bernstein conversion. The prior \([8,18]\) independent replay checked another 623,616 coefficients, for **2,182,656** in total. The smallest of the five new branch minima is the displayed \(m\).

Frozen sub-eight branches, signs and frequency leaves: `frontier-20261028-five-contact-below-eight-frozen-v1.json`, SHA-256 `f4aa43970d81d0ac3c11435cd347054819ceebc2684b36245fde86400b89d35f`. Independent sub-eight checker: `frontier-20261028-five-contact-below-eight-independent-kernel-v1.py`, SHA-256 `019aebe144c85dee96e351e6b62f87d7be9ee63fa36baf7b686ea87339354c95`; receipt: `frontier-20261028-five-contact-below-eight-independent-result-v1.json`, SHA-256 `b44d8a8ab47e8a1c86f666d66b8a4ec384c5935590bc1bed811543e12c6997f2`. The prior maximal-node theorem and its pinned replay are `frontier-20261028-five-contact-maximal-node-domain-v1.md`, SHA-256 `0af568fb02ad9042860a8c616d56d379292bb3a3931d243a13220f6d509e8e2d`.

The degree, admissibility, marker, homotopy and continuum inferences are written mathematics. The finite signs and identities were checked with integers and `fractions.Fraction` on one Python Eval host. This is not formal proof, cross-vendor review, novelty clearance, an arbitrary-node theorem, an arbitrary-box theorem, or a negative certificate.
