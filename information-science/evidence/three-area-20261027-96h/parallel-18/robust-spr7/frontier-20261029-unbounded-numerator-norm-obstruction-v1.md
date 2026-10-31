# No uniform coefficient-norm cap for common numerators

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact symbolic replay; not parent adoption.** On the explicit full-width, all-member-Hurwitz and constructively solvable septic family \(K_R\), \(R\ge1000\), from `frontier-20261029-unbounded-three-even-coefficients-v1.md` (SHA-256 `dad52df910b0b6fa7826bb2eba21976d0c12dff72e931c01b89e0939f5cc886f`), **every** common monic numerator satisfies
\[
\boxed{\quad
\frac{\|b\|_1}{\sup_{a\in K_R}\|a\|_1}>\frac{33}{1300}R.\quad}
\]
Here the coefficient \(\ell^1\)-norm includes the leading monic coefficient. Consequently no constant \(C\), independent of the actual box, can guarantee a common monic numerator of norm at most \(C\sup_{a\in K}\|a\|_1\), even on full-width stable boxes that **do** possess common numerators. This excludes global norm caps, not only coordinatewise caps.

## Bound and optimal order

The two separately certified actual-atom functionals give \(b_2>R^4/65\) and \(b_4>R^4/100\). Every common numerator is Hurwitz and has positive coefficients, so
\[
\|b\|_1>b_2+b_4>\frac{33}{1300}R^4.
\]
The new independent exact checker reconstructs the actual radial upper endpoints and proves \(\sup_{a\in K_R}\|a\|_1<R^3\) by seven strictly positive coefficients after clearing a positive power of \(R\) and setting \(R=1000+u\). The stated ratio follows.

This growth order is attained. Because every denominator coefficient is positive and the intervals are independent, its maximum norm is the sum of the seven upper endpoints plus 1. The checker verifies its leading term is \(R^3/2\). For the explicit common numerator \(b_R\), the earlier determinant replay gives leading coefficients \((1251/8425)R^4\) at \(b_2\) and \((8/337)R^4\) at \(b_4\), while all remaining coefficients are \(O(R^3)\). Hence
\[
\|b_R\|_1\sim\frac{1451}{8425}R^4,\qquad
\frac{\|b_R\|_1}{\sup_{a\in K_R}\|a\|_1}
\sim\frac{2902}{8425}R.
\]
Thus the infimum of the ratio over **all** common monic numerators is \(\Theta(R)\); no exact optimum constant or attainment is claimed. Since the ambient coefficient dimension is fixed, the same unboundedness holds for every coefficient \(\ell^p\)-norm by finite-dimensional norm equivalence.

Exact norm-gap data `frontier-20261029-unbounded-coefficient-norm-frozen-v1.json`, SHA-256 `be18e89408d87461d3c7dc89b30930bb15704fcef666680ccba167ea6be8ab8c`; standalone geometry/leading-coefficient checker `frontier-20261029-unbounded-coefficient-norm-independent-kernel-v1.py`, SHA-256 `2beac724bc7cf9c12b26e1e2fe423ec680ab0d519b0144e50efd8ada3ac22afc`; receipt `frontier-20261029-unbounded-coefficient-norm-independent-result-v1.json`, SHA-256 `bfd6966599c4685a14f7b6e2245fb143c904bc649df13e1a61f60372871a05f8`. The checker imports the pinned independent Laurent geometry and verifies all seven strict shifted coefficients and exact leading constants using `fractions.Fraction`. Atom positivity, Hurwitz stability, limiting comparisons and norm equivalence are written deductions supported by the pinned source packets. No formal proof, cross-vendor review, novelty clearance, strict-negative-coordinate certificate or arbitrary-box verdict is claimed.
