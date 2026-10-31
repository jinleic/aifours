# A complete three-pole, positive-residue formulation of septic SPR synthesis

Owner InfoSPR7-2, info-2. Native clock observed before writing: **Thu Oct 29 15:28:55 PDT 2026**. **WRITTEN universal synthesis reduction with a WRITTEN-checked-in-kernel rational boundary example; not parent-adopted, independently reviewed, formally verified or novelty-cleared.** This is not a fixed numerator profile: every common numerator is covered, and the rational construction below loses no feasible box. It does not prove that the remaining three-pole feasibility problem is always feasible.

## 1. Original family and complete pole domain

Let \(K\) be any nonempty closed bounded independent monic septic coefficient box, with degenerate intervals permitted, all of whose members are strictly Hurwitz. Write
\[
a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t),\qquad t\ge0,
\]
with the parity cubics in the supplied original definitions. For an actual even component let its three positive roots be \(e_1<e_2<e_3\), and for an actual odd component \(o_1<o_2<o_3\). The degree-seven Hermite–Biehler criterion gives
\[
0<e_1<o_1<e_2<o_2<e_3<o_3.
\]
Because even and odd coefficients vary independently and any actual even component can be combined with any actual odd component, compactness gives the **strict globally separated bands**
\[
0<\underline e_1\le\overline e_1<\underline o_1\le\overline o_1
<\underline e_2\le\overline e_2<\underline o_2\le\overline o_2
<\underline e_3\le\overline e_3<\underline o_3\le\overline o_3. \tag{1}
\]
For example, combine an even component attaining \(\overline e_i\) with an odd component attaining \(\underline o_i\); that actual member is stable, so the inequality is strict. Root extrema are attained because the compact parity boxes consist of cubics with simple positive roots; the root maps are continuous. The image of each root map is an interval because its coefficient box is connected.

**Root-lock lemma.** If \(b\) is any original common exact-degree-seven numerator, its even roots \(x_1<x_2<x_3\) and odd roots \(y_1<y_2<y_3\) satisfy
\[
\begin{aligned}
0<x_1&<\underline o_1,&\overline o_1<x_2&<\underline o_2,&\overline o_2<x_3&<\underline o_3,\\
\overline e_1<y_1&<\underline e_2,&\overline e_2<y_2&<\underline e_3,&\overline e_3<y_3&<\infty. \tag{2}
\end{aligned}
\]
First \(b_7>0\) because \(b/a\to b_7\) at infinity and exact degree excludes zero. For a fixed stable \(a\in K\), the path \((1-\theta)a+\theta b\) has positive-real ratio to \(a\) on the imaginary axis and positive leading coefficient, so it cannot acquire an imaginary-axis root or lose degree. Since it starts Hurwitz, \(b\) is Hurwitz. In particular all \(b_j>0\), and its two parity cubics have simple positive alternating roots.

At every actual \(O_a\)-root, the pairing is \(E_aE_b>0\). The signs of \(E_a\) on the three odd-root bands are \(-,+,-\), so \(E_b\) has these strict signs throughout those bands. Together with \(E_b(0)>0\), \(E_b\) has one root in each of the three displayed odd-band gaps. Similarly, at an actual \(E_a\)-root the pairing is \(tO_aO_b>0\); the signs of \(O_a\) on the three even-root bands are \(+,-,+\), and \(O_b(t)\to-\infty\). This gives the three displayed odd-root gaps. The root images are entire bands by connectedness, so endpoint equality is also excluded.

## 2. Every common numerator has this positive-residue form

For strictly ordered positive \(x_1,x_2,x_3\), define
\[
H_x(s)=\prod_{i=1}^{3}(s^2+x_i),\qquad
H_{x,i}(s)=\prod_{j\ne i}(s^2+x_j).
\]
A complete normal form is
\[
b(s)=(c+d s)H_x(s)+s\sum_{i=1}^{3}w_iH_{x,i}(s),
\qquad c,d,w_1,w_2,w_3>0. \tag{3}
\]
This has exact degree seven, leading coefficient \(d>0\), and strictly positive coefficients.

To derive it for an **arbitrary** common \(b\), write
\[
E_b(t)=c\prod_i(x_i-t),\qquad
\frac{O_b(t)}{\prod_i(x_i-t)}=d+\sum_i\frac{w_i}{x_i-t},
\]
where \(c=b_6>0\), \(d=b_7>0\), and
\[
w_i=\frac{O_b(x_i)}{\prod_{j\ne i}(x_j-x_i)}.
\]
Since \(x_1<y_1<x_2<y_2<x_3<y_3\), both numerator and denominator in this expression for \(w_i\) have signs \(+,-,+\), hence each \(w_i>0\). Polynomial partial fractions give (3) exactly. Conversely, positive parameters in (3) give an exact septic polynomial; the pairing tests below, not this formula alone, decide whether it is common.

**Exact existence reduction.** The original box \(K\) has a common numerator if and only if there are poles \(x\) in the three **open bounded** intervals in the first row of (2), and positive \(c,d,w_i\), for which (3) has strictly positive pairing with all four actual parity corners for every \(t\ge0\). The forward direction is the derivation above. The reverse direction uses only the actual four-corner affine reduction: at each frequency the worst independent even/odd coefficient choices are attained by one of the four endpoint pairs. This is a complete all-variable representation, not a claim that an arbitrarily selected pole triple succeeds.

For each fixed \(x\), all four corner pairing polynomials are **affine** in the five positive weights \((c,d,w_1,w_2,w_3)\). Thus the remaining feasibility problem consists of three bounded nonlinear pole variables and a convex five-weight semi-infinite feasibility problem. Positivity in the odd polynomial cannot be replaced by merely fixing or selecting one corner, and the three-pole gaps alone do not settle feasibility.

## 3. Rational pole and weight witnesses lose no positive cases

If any common numerator exists, the poles \(x_i\) and weights in (3) may all be chosen **rational**, still strictly inside their open gaps and strictly positive. Indeed, the exact degree and common pairing give a strictly positive uniform minimum of
\[
P_{a,b}(t)/(1+t)^7
\]
over the compactified half-line and four corners: its endpoint at infinity is \(d>0\). Formula (3) depends continuously on its eight real parameters, and the normalized pairing depends continuously on those parameters on that compact set. Therefore sufficiently small perturbations preserve the common inequalities and all strict parameter/gap inequalities. Rational parameters are dense.

In particular, for **any rational endpoint box** there is an exact unbounded synthesis search: enumerate all strictly ordered positive rational triples and positive rational weights in (3), and for each rational candidate test the four rational pairing polynomials for strict positivity on \([0,\infty)\) by an exact Sturm root-count, with their positive constant and leading coefficients checked explicitly. If the original rational box has a common numerator, the search halts and outputs one. No termination is claimed if no numerator exists, and no practical complexity bound is claimed. The proof does not rely on a prior counterexample-search result.

## 4. Fixed-pole finite convex certificate

Fix a pole triple. Let \(v_3(t)=(1,t,t^2,t^3)^T\). Existence of a positive weight vector in (3) with a common numerator is equivalent to existence of positive weights, \(\delta>0\), and, for each of the four corners \(a\), real positive-semidefinite symmetric \(4\times4\) matrices \(A_a,B_a\) such that
\[
P_{a,b}(t)-\delta(1+t)^7
=v_3(t)^TA_av_3(t)+t\,v_3(t)^TB_av_3(t). \tag{4}
\]
The forward direction chooses \(\delta\) below the uniform compactified margin and uses the classical one-variable half-line Markov–Lukács sum-of-squares theorem: a real polynomial of degree at most seven nonnegative on \([0,\infty)\) is \(\sigma_0+t\sigma_1\), with \(\sigma_0,\sigma_1\) sums of squares of degree-at-most-three polynomials. The converse is immediate. Coefficient matching in (4) is linear in the weights, \(\delta\), and Gram entries for fixed \(x\); this is an exact finite semidefinite feasibility problem, not a frequency grid.

For rational endpoints and rational \(x\), whenever (4) is feasible it also admits a **rational strict-positive-definite Gram certificate**: choose rational pole weights and \(\delta\) with residual compactified margin positive; subtract a sufficiently small rational multiple of \((1+t)\sum_{j=0}^{3}t^{2j}\), apply the same SOS theorem, then add that multiple of the identity to both Gram matrices. Coefficient equations have rational data, and rational points are dense in their affine solution space; positive definiteness is open. Rational matrix entries and their positive principal minors then provide a finite exact certificate. Neither this theorem nor the general three-pole reduction asserts feasibility for every \(K\).

## 5. A boundary warning: positive residues and stable \(b\) do not finish synthesis

A tempting missing step would be to infer all-frequency positivity merely from five boundary tangencies, strictly positive contact residues, and a Hurwitz numerator. That implication is false. Consider the following **boundary** parity endpoints:
\[
\begin{aligned}
E_-&=\tfrac{37}{32}(\tfrac12-t)(3-t)(6-t),&
E_+&=(1-t)(2-t)(8-t),\\
O_-&=(1-t)(6-t)(8-t),&
O_+&=(2-t)(3-t)(11-t).
\end{aligned}
\]
Their differences have positive coefficients:
\(E_+-E_-=179/32+t/64+t^2/64+5t^3/32\) and
\(O_+-O_-=18+t+t^2\). The five boundary contacts are \(1,2,3,6,8\), in the corner order \((E_+,O_-),(E_+,O_+),(E_-,O_+),(E_-,O_-),(E_+,O_-)\). This boundary family itself is not an eligible all-strictly-Hurwitz original box.

Let \(b\) have ascending integer coefficients
\[
(65405280,31255482,123643594,39200323,48829757,11543441,4496613,817566).
\]
At all five contacts, direct exact evaluation gives \(P'_{a,b}(t_i)=0\). For each contact put
\[
R_i=O'_{a_i}(t_i)E_b(t_i)-E'_{a_i}(t_i)O_b(t_i).
\]
These five values are, respectively,
\[
506148188,\quad247893624,\quad279086535/2,\quad
28314270411/16,\quad3001920180,
\]
all positive. Moreover, the exact Routh first column of \(b\) is positive. At the second contact, however,
\[
P''_{(E_+,O_+),b}(2)=-75882684<0,
\qquad
P_{(E_+,O_+),b}(19/10)=-1985818229633/5000000<0.
\]
Thus even this strongly constrained **Hurwitz** polynomial fails a boundary pairing. The displayed finite computations used exact integers and `fractions.Fraction` on one Python Eval host; they are not a counterexample to the original box problem.

For completeness, the strict residues themselves force \(b\) Hurwitz in this five-contact pattern when all \(b_j>0\): the tangency equation gives
\[
\operatorname{sgn}E_b(t_i)=\operatorname{sgn}O'_{a_i}(t_i),\qquad
\operatorname{sgn}O_b(t_i)=-\operatorname{sgn}E'_{a_i}(t_i).
\]
The resulting signs force the even roots into \((0,1),(2,3),(6,8)\) and the odd roots into \((1,2),(3,6),(8,\infty)\). These roots strictly interlace, so Hermite–Biehler proves stability. The example shows that this root/geometric information still does not establish the required whole-frequency pairing.

## 6. Imports, assurance and exact residual

Named classical imports are the odd-degree Hermite–Biehler root criterion; continuity of simple roots and compactness; the one-variable half-line Markov–Lukács SOS theorem; and exact Sturm root counting for the rational-search corollary. The homotopy, band extrema, residue signs, rational approximation, and coefficient-matching deductions are written above. No historical held source or earlier unreviewed result is used as a premise. Parent-classified incidental search-display exposure is carried in `owner-incidental-held-source-search-display-v1.json`; no clean-cognition claim is made.

The original remaining question is now explicit: **for every admissible box, does there exist a triple in the open bands (2) for which the positive-weight convex problem (4) is feasible, or can an eligible box be proved to have no such triple?** Neither existence nor nonexistence is proved here. No all-frequency certification is asserted for the boundary example, and no formal proof, independent review or novelty clearance has been performed.
