# A five-atom negative sum that is explicitly ineligible

**Status: WRITTEN-checked-in-kernel exact finite countermechanism; not parent adoption.** This is **not** a negative answer to the original question: although all five displayed denominators are individually monic Hurwitz with real negative roots, their convex and interval hulls are not stable. It shows that individual stability plus the previously derived phase-class and ratio restrictions alone cannot replace all-member box stability.

## Exact negative atom sum for five individual denominators

Let \(a_i(s)=(s+\alpha_i)^7\), with
\[
\begin{aligned}
(\alpha_1,\ldots,\alpha_5)&=
\left(\frac{12587}{10000},\frac{11597}{2500},\frac{16331}{10000},
\frac{21703}{5000},\frac{10873}{5000}\right),\\
(\omega_1,\ldots,\omega_5)&=\left(1,\frac{11}{10},2,\frac{21}{10},3\right),\\
(w_1,\ldots,w_5)&=(10000000,4817,192326,2216,392).
\end{aligned}
\]
Each \(a_i\) is Hurwitz: all seven roots are \(-\alpha_i<0\). The standalone exact checker reconstructs the raw monomial pairing rows at the five positive frequencies and verifies
\[
C_j=\sum_{i=1}^5w_i\,[b_j]\operatorname{Re}\bigl(b(i\omega_i)a_i(-i\omega_i)\bigr)<0,
\qquad j=0,\ldots,7.
\]
All weights are strictly positive integers. If a common equal-degree SPR numerator for these five denominators existed, it would be Hurwitz with strictly positive coefficients, giving both \(C\cdot b<0\) and \(C\cdot b>0\), a contradiction. Thus the five individually stable polynomials have **no** common numerator.

Their exact unwrapped phase classes at the five nodes are \((2,1,3,2,4)\); they satisfy the pairwise class ordering \(q_i\le q_j+1\), and their mixed-sign evaluations satisfy the quantitative condition \(r_2>r_3\) from `frontier-20261029-strict-five-node-ratio-obstruction-v1.md`. The checker derives phase classes by exact rational quadrant tracking through the seven factors, without trigonometric or floating evaluation. Hence those particular necessary sign/order/ratio conditions are consistent with an all-negative atom sum when the denominators are only individually stable.

## Why this is not an eligible original box

The \(1/10\) convex mixture of the first two polynomials has fourth leading Hurwitz minor
\[
\Delta_4=-\frac{47881433336563746565940797976373297470445388670619}
{2000000000000000000000000000000000000000000}<0.
\]
Thus it is not Hurwitz, and **no all-member-Hurwitz convex family** can contain even those two endpoints. In particular no eligible independent coefficient box contains all five.

Independently, every coefficient box containing all five also contains the mixed coefficient vector formed from the interval endpoints of \((s+13/10)^7\) and \((s+9/2)^7\):
\[
\left(\frac{62748517}{10000000},\frac{33787663}{1000000},
\frac{1240029}{32},\frac{229635}{16},\frac{15379}{200},
\frac{3549}{100},\frac{63}{2},1\right).
\]
Its third leading Hurwitz minor is \(-32350634323/2500<0\). Both instabilities are independently reconstructed exactly, so this example cannot be relabeled as an original eligible box. In particular, it does **not** satisfy the premise of globally disjoint root bands for a single stable interval family.

## Evidence

Exact inputs and all eight aggregate coordinates: `frontier-20261029-individually-stable-five-atom-negative-frozen-v1.json`, SHA-256 `f7248ce91c4802e6888ec05d7934e6f28b3a66724ffc6c929881faf717f5e21f`. Checker `frontier-20261029-individually-stable-five-atom-negative-independent-kernel-v1.py`, SHA-256 `d6a9444abaeceff78cf2329b2db500eddcae2829e751d05cd1813ba9ce7703be`, independently verifies the five positive parameters and weights, all eight negative sums, phase classes and ratio, both negative Hurwitz minors and a negative-weight mutation. Receipt `frontier-20261029-individually-stable-five-atom-negative-independent-result-v1.json`, SHA-256 `56b7b9590df8233f56b827a4156e73d90c9c9ac7748b48750d2ba56e2d547f4a`. Arithmetic uses exact integers/`fractions.Fraction` on one Python Eval host. No formal proof, cross-vendor review, novelty clearance, or original interval-box verdict is claimed.
