# A universal robustification and rational-certificate theorem for septic boxes

Owner: InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 14:32:54 PDT 2026**. Status: **WRITTEN theorem candidate**, independently derived below from the literal original problem definitions and the named standard facts; not parent-adopted, formally verified, independently reviewed, or novelty-cleared. No historical held SPR body or prior unreviewed scientific claim is a premise.

## 1. Result

Let \(K\) be **any** nonempty, closed, bounded, independent monic real septic coefficient box, including boxes with degenerate intervals, and suppose every member is strictly Hurwitz. Assume that \(K\) has **no** real numerator of exact degree seven that is strictly positive real against every member at every finite real frequency. Let \(K'\) be **any** independent monic septic box whose seven nonleading coefficient intervals strictly contain the corresponding intervals of \(K\).

Then:

1. The compact convex hull of all compactified four-corner pairing vectors of \(K'\) contains zero in its **full eight-dimensional interior**. The conclusion does not require \(K'\) itself to be stable.
2. There are at most **eight** positive-weight actual corner/frequency atoms of \(K'\), all at finite strictly positive squared frequencies, whose aggregate pairing vector is strictly negative in **every one of its eight monomial coordinates**.
3. If \(K'\) has rational endpoints, those squared frequencies and weights may be chosen rational. If \(K'\) is also robustly Hurwitz, this is an exact rational obstruction to every common exact-degree-seven SPR numerator.
4. For every sufficiently small \(\varepsilon>0\), there is a rational, seven-positive-width, robustly Hurwitz box \(K'\) strictly containing \(K\), with each endpoint moved by less than \(\varepsilon\). Such a box has the rational obstruction in (3). In fact a nonempty open set of real seven-positive-width robustly Hurwitz boxes around that \(K'\) is also nonsynthesizable.

Consequently, **if any real or degenerate original septic counterexample exists, then there is a full-width rational counterexample with a finite rational all-negative certificate of at most eight actual corner/frequency atoms.** An exact search over all such rational data is therefore complete for finding a counterexample: if one exists, the search eventually halts with one. No claim is made that the search terminates when the universal synthesis statement is true, and no particular counterexample is asserted.

The substantive coupling is the interior assertion: zero may initially be only a boundary annihilator for \(K\), but strict enlargement in **every independent coefficient direction** rules out every nonzero weak separator on \(K'\). This is not an assumed strict-negative certificate for the original \(K\), not a fixed-profile result, and not a restriction to preselected boxes.

## 2. Notation and exact corner reduction

Write
\[
a(s)=s^7+\sum_{j=0}^{6}a_js^j,\qquad b(s)=\sum_{j=0}^{7}b_js^j,
\]
\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3,
\]
and define \(E_b,O_b\) in the same way, with the actual \(b_7\) in \(O_b\). For \(t=\omega^2\ge0\),
\[
P_{a,b}(t)=E_a(t)E_b(t)+tO_a(t)O_b(t)
=\operatorname{Re}\bigl(b(i\omega)\overline{a(i\omega)}\bigr).
\]
Because \(a\) is Hurwitz, the original SPR inequality is exactly \(P_{a,b}(t)>0\) for all finite \(t\ge0\).

For each coefficient interval \([\ell_j,u_j]\), define
\[
\begin{aligned}
E_-&=\ell_0-u_2t+\ell_4t^2-u_6t^3,&
E_+&=u_0-\ell_2t+u_4t^2-\ell_6t^3,\\
O_-&=\ell_1-u_3t+\ell_5t^2-t^3,&
O_+&=u_1-\ell_3t+u_5t^2-t^3.
\end{aligned}
\]
For every \(t\ge0\), \(E_-\le E_a\le E_+\) and \(O_-\le O_a\le O_+\). The four pairs \((E_\pm,O_\pm)\) are actual members of the box. Since \(P\) is affine separately in the independently variable even and odd components, its minimum over the box at each \(t\) is attained at one of those four pairs. Thus all-member nonnegativity or strict positivity is exactly equivalent to the corresponding four-corner inequalities, without any external synthesis theorem.

Define the compactified row vector \(g_a(t)\in\mathbb R^8\), indexed by \(b_0,\ldots,b_7\), by
\[
(g_a(t))_{2r}=\frac{(-t)^rE_a(t)}{(1+t)^7},\quad
(g_a(t))_{2r+1}=\frac{t(-t)^rO_a(t)}{(1+t)^7},\qquad 0\le r\le3.
\]
Then \(b\cdot g_a(t)=P_{a,b}(t)/(1+t)^7\). At the compactification endpoints, \(g_a(0)=a_0e_0\) and \(g_a(\infty)=e_7\). The rows are continuous in \(t\in[0,\infty]\). Let \(S_K\) be the union of the four corner curves and let \(C_K=\operatorname{conv}S_K\). This set is compact.

## 3. Original synthesis is strict separation

A common exact-degree-seven numerator necessarily has \(b_7>0\): the finite-frequency ratio tends to \(b_7\), and the exact-degree condition excludes zero. Its pairings are strictly positive at every finite frequency and at infinity, so compactness and the four-corner reduction give \(b\cdot g\ge\delta>0\) for every \(g\in S_K\).

Conversely, if \(0\notin C_K\), strict finite-dimensional separation supplies \(b\) with \(b\cdot g>0\) on \(S_K\). The point \(e_7\in S_K\) forces \(b_7>0\), and the corner reduction gives the original all-member, all-finite-frequency inequalities. Therefore
\[
\boxed{\ K\text{ has no common numerator}\quad\Longleftrightarrow\quad 0\in C_K.\ } \tag{1}
\]
Carathéodory's theorem supplies a finite representation of zero by at most nine corner rows, including possible zero/infinity rows. No assumption about negative coordinates or rationality is made for this initial annihilator.

## 4. Every zero annihilator uses at least four positive frequencies

Take any finite nonnegative representation of zero in (1), discard zero weights, and merge rows sharing a positive finite squared frequency. At a node \(t_i\), their weighted mean denominator \(a_i\) lies in \(K\), since \(K\) is convex, and is Hurwitz. Endpoint atoms, if any, are nonnegative multiples of \(e_0\) or \(e_7\).

Suppose there are only \(m\le3\) distinct positive finite nodes \(t_1,\ldots,t_m\). If \(m=0\), endpoint rows alone cannot have a positive-weight sum zero. For \(m\ge1\), fix \(i\) and set
\[
H_i(s)=\prod_{j\ne i}(s^2+t_j),\qquad
q_i^{\rm odd}(s)=sH_i(s),\quad q_i^{\rm even}(s)=s^2H_i(s).
\]
Both polynomials have zero constant and zero \(s^7\) coefficient, because their degrees are at most five and six respectively; they therefore annihilate the endpoint rows. At every positive node except \(t_i\), both vanish. The zero-row sum dotted separately with their coefficient vectors gives, up to nonzero real scalar factors,
\[
t_i O_{a_i}(t_i)=0,\qquad t_i E_{a_i}(t_i)=0.
\]
The scalars include the positive merged weight and \(\prod_{j\ne i}(t_j-t_i)\ne0\). Thus \(a_i(i\sqrt{t_i})=0\), contradicting its strict Hurwitz stability. Hence every finite zero annihilator has at least **four distinct positive finite frequencies**, regardless of endpoint atoms. This lemma needs neither any five-frequency classification nor a strict-negative hypothesis.

## 5. Strict enlargement forces full-dimensional interior

By (1), choose a finite zero annihilator for \(K\). The preceding lemma supplies at least four distinct positive nodes. Every \(a_i\in K\) is an **interior point** of \(K'\) in all seven independently varying coefficients.

Assume \(0\) is not interior to \(C_{K'}\). Since \(C_K\subseteq C_{K'}\) under the affine four-corner reduction, \(0\in C_{K'}\); a supporting hyperplane gives a nonzero real polynomial coefficient vector \(b\) with
\[
b\cdot g\ge0\qquad(g\in S_{K'}).
\]
The four-corner reduction extends this to every \(a\in K'\). Pairing \(b\) with the zero annihilator for \(K\) gives a sum of nonnegative summands equal to zero; each summand at each positive node must therefore be zero. In particular \(P_{a_i,b}(t_i)=0\).

For fixed \(t_i>0\), \(P_{a,b}(t_i)\) is affine in the coefficients of \(a\). At the interior point \(a_i\) it is nonnegative throughout \(K'\) and equals zero. Varying \(a_0\) in both directions forces its coefficient \(E_b(t_i)\) to vanish; independently varying \(a_1\) forces \(t_iO_b(t_i)=0\). Hence \(b(i\sqrt{t_i})=0\) at each of at least four distinct positive \(t_i\). Because \(b\) has real coefficients, their conjugates are also zeros: at least eight distinct zeros. This is impossible for nonzero \(\deg b\le7\). The supporting vector cannot exist, proving
\[
\boxed{\ 0\in\operatorname{int}_{\mathbb R^8}C_{K'}.\ } \tag{2}
\]
This argument uses only the original stability of \(K\), strict coordinate containment, and the actual box affine structure; it does not assume stability of \(K'\).

## 6. Short strict certificates and rational reduction

By (2), for some \(\eta>0\) the vector \(-\eta(1,\ldots,1)\) lies in \(C_{K'}\). Rescale its convex representation, then apply conic Carathéodory in \(\mathbb R^8\): \(-(1,\ldots,1)\) is a nonnegative combination of at most eight actual corner rows. Discard zero weights. For any atom at zero or infinity, replace its endpoint by a sufficiently small or large strictly positive finite \(t\), keeping its corner and weight. Continuity of the compactified rows preserves all eight strict negative signs when the finitely many replacements are close enough. This works even when \(K'\) is not stable and an endpoint row is a negative multiple of \(e_0\). Thus at most eight positive-weight atoms at positive finite nodes give the desired certificate.

If the endpoints are rational, the finite rows are continuous functions of their strictly positive frequencies and rational functions with rational coefficients. Approximate the finitely many frequencies and positive weights by positive rationals closely enough that **all eight strict inequalities remain strict**. Multiplying each weight by the positive rational \((1+t_i)^{-7}\), if desired, converts the compactified row certificate into an uncompactified polynomial-pairing certificate. Thus all displayed data and all coordinate checks can be rational.

A strict-negative certificate rules out a common numerator when \(K'\) is robustly Hurwitz. Indeed, any common exact-degree numerator has \(b_7>0\); fix any Hurwitz member \(a\) and consider \((1-\theta)a+\theta b\), \(0\le\theta\le1\). On the imaginary axis its ratio to \(a\) has positive real part, and its leading coefficient is positive. By continuity of roots no imaginary-axis crossing or escape to infinity occurs, so \(b\) is Hurwitz. Its positive leading coefficient and real Hurwitz factorization imply every \(b_j>0\). Every certificate atom has strictly positive pairing with \(b\), but the strictly negative aggregate dotted with \(b>0\) is strictly negative: contradiction.

Finally, strict Hurwitz stability is open in the seven nonleading coefficients. Since \(K\) is compact and all its members are stable, a sufficiently small coefficientwise neighborhood of \(K\) is stable. Rational outward endpoint choices within any prescribed sufficiently small distance give a full-width rational \(K'\) satisfying strict containment and robust stability. At its rational strict certificate, all eight atom sums vary continuously with the 14 interval endpoints, and robust stability and positive widths also persist under sufficiently small perturbations. Thus an open neighborhood of \(K'\) consists of counterexamples.

## 7. Exact search consequence and limits

An effective, unbounded enumeration can range over rational ordered endpoint vectors, the four actual parity corners, at most eight positive rational squared frequencies, and positive rational weights. Exact rational arithmetic tests the eight strict-negative sums. Robust stability can be checked using the classical **Kharitonov four-polynomial theorem** for independent real interval polynomials, together with the exact Routh–Hurwitz determinant criterion on the four rational corners; monicity fixes the degree and degenerate intervals are allowed. These standard theorems are named imports for this **enumeration implementation**, not needed in the proof of the interior theorem. Fair enumeration by numerator/denominator height is complete for the negative case established above. No claim about practical complexity or a completed search follows.

Named other standard imports: finite-dimensional strict/supporting hyperplane separation; ordinary and conic Carathéodory; compactness; openness of Hurwitz stability and continuity of polynomial roots; elementary real-factor positivity. All have their exact hypotheses exhibited above. The mathematical deductions are WRITTEN only: no arithmetic interpreter, solver, finite search, formal checker, independent reviewer, or novelty screen is used or claimed for this theorem. The original septic synthesis-or-obstruction question and the status of every actual candidate box remain **OPEN**.
