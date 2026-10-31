# A sharp local even-root width constraint imposed by independent boxes

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:14:49 PDT 2026**. **WRITTEN theorem candidate with a nonvacuous WRITTEN-checked-in-kernel seven-width example**; not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a new box-specific necessary inequality, not an unrestricted synthesis verdict.

## 1. Universal coefficient-mixing bound

Let two monic Hurwitz septics have the **same odd part**, with its second positive root at \(t=T\). Suppose their even parts have the form
\[
E_b(t)=-L(t-a)(t-b)(t-c),\quad E_d(t)=-H(t-a)(t-d)(t-c),
\quad L,H>0,\quad 0<a<b<d<T<c. \tag{1}
\]
Write
\[
P_x=axc,\qquad S_x=ax+ac+xc,\qquad Q_x=a+x+c,\qquad r=H/L. \tag{2}
\]
Any independent coefficient box containing both polynomials and consisting entirely of Hurwitz members must have
\[
G(r):=\min(P_b,rP_d)-T\max(S_b,rS_d)
+T^2\min(Q_b,rQ_d)-T^3\max(1,r)>0. \tag{3}
\]
Indeed the coefficientwise minimum of the even value at \(T\) is exactly \(LG(r)\), and that minimizing even coefficient mix can be combined with the shared odd coefficients inside the box. For a Hurwitz member the even part at its second odd root is strictly positive by Hermite–Biehler interlacing. Formula (3) accounts for **all 16 independent even-coefficient choices** simultaneously; it is exact for the single frequency \(T\), not a claim of full-box stability.

## 2. Sharp scale-free threshold for an explicit continuous family

Fix
\[
a=1/2,\quad b=2,\quad c=5,\quad T=9/2,\quad 2<d<9/2. \tag{4}
\]
Then there exist positive \(L,H\) with \(G(H/L)>0\) **if and only if**
\[
d<\frac{2218}{959}=2+\frac{300}{959}. \tag{5}
\]
Thus (5) is a necessary condition for **any** all-Hurwitz independent box containing the two members in (1). It is sharp for the local single-frequency coefficient-mixing condition, but is not asserted sufficient for robust stability or common-SPR synthesis.

Proof. Here
\[
(P_b,S_b,Q_b)=(5,27/2,15/2),\quad
(P_d,S_d,Q_d)=(5d/2,(11d+5)/2,(2d+11)/2).
\]
The four switch points in (3) have the strict order
\[
0<\frac2d<\frac{27}{11d+5}<\frac{15}{2d+11}<1 \qquad(d>2). \tag{6}
\]
On these consecutive intervals \(G\) is linear. Its slope is positive before the third switch: the only nonobvious slope, on the middle interval, is
\(T^2Q_d-TS_d=(9/2)(89/4-d)>0\) for \(d<9/2\). Its slope is negative after that switch. Hence the unique maximum occurs at
\[
r_* =\frac{15}{2d+11},\qquad
G(r_*)=\frac{2218-959d}{4(2d+11)}. \tag{7}
\]
This proves the equivalence, including equality: at \(d=2218/959\) the maximum is zero and strict robustness is impossible. The previously displayed parity-product countermechanism with \(d=16/5\) violates (5); the additive vacuity correction is `frontier-20261029-box-hurwitz-minor-minimal-exclusion-erratum-v1.md`, SHA-256 `f325d35aa041d86f8705665dbbdc3a7ecec2471c135a35f55c5ad00fb0565e14`.

## 3. Nonvacuity: an explicit seven-positive-width stable box

Take \(d=201/100\), \(L=H=1\), and the shared odd component
\[
O(t)=-(t-9/10)(t-9/2)(t-7)
=567/20-(837/20)t+(62/5)t^2-t^3.
\]
The two even coefficient vectors \((a_0,a_2,a_4,a_6)\) are
\[
(5,27/2,15/2,1),\qquad
(201/40,2711/200,751/100,1).
\]
Take their coordinatewise even hull and independently enlarge **every one of the seven nonleading coefficient intervals** by \(\epsilon=1/1000\), keeping the \(s^7\) coefficient exactly one. All seven widths and all lower coefficients are positive. This box contains both members.

At the six rational squared-frequency markers
\[
(3/4,3/2,3,19/4,6,8),
\]
the required sign pairs \((E,O)\) are \((- ,+),(- ,-),(+,-),(+,+),(-,+),(-,-)\). For any box member, variation by \(\epsilon\) changes \(E\) at \(t\) by at most \(\epsilon(1+t+t^2+t^3)\), and \(O\) by at most \(\epsilon(1+t+t^2)\). The independently minimized sign margins at the six markers are, in order,
\[
\begin{array}{c|cc}
t&\text{even lower margin}&\text{odd lower margin}\\\hline
3/4&16573/12800&56213/16000\\
3/2&2711/1600&39581/4000\\
3&959/200&12587/1000\\
19/4&161609/64000&34197/16000\\
6&5339/250&7607/1000\\
8&535/4&24777/1000.
\end{array} \tag{8}
\]
All twelve are strictly positive; their minimum is \(16573/12800\). Together with positive constant terms and leading coefficients, the marker signs force three simple even roots and three simple odd roots in six disjoint, alternating intervals. Hermite–Biehler then makes **every** box member strictly Hurwitz. The endpoint and margin computations in (8) used exact Python `fractions.Fraction` and integers in one Eval host; the all-member root-order deduction is written mathematics.

Consequently the necessary inequality (5) applies to a genuine full-width eligible interval box; it is not merely a vacuous implication. The example itself does not establish a common numerator or exclude one.

## 4. Assurance and gap

Named classical import: odd-degree Hermite–Biehler root interlacing. The coefficient mixing, four-switch maximum and explicit perturbation bounds are derived above. No independent review, formal verification, parent adoption or novelty clearance has occurred. Parent-classified incidental source-display exposure is recorded in `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made. The open step is to combine box-induced inequalities like (3) across the mandatory even and odd reversed bands with the two-circuit conditions, or exhibit an eligible box meeting those conditions. Neither is proved here.
