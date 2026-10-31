# An eight-atom odd-cancellation alternative for the original septic box

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 15:51:07 PDT 2026**. **WRITTEN universal synthesis-or-obstruction theorem candidate**, not parent-adopted, independently reviewed, formally verified or novelty-cleared. All mathematical reductions are derived below from the original box definition and explicitly named standard imports; no earlier unreviewed or held result is a premise. This theorem does not exhibit a negative box or prove every box positive.

## 1. Exact alternative

Let \(K\) be any nonempty bounded closed independent monic septic coefficient box, all of whose members are strictly Hurwitz. Intervals may be degenerate. Write
\[
a(i\sqrt t)=E_a(t)+i\sqrt t\,O_a(t),\qquad
E_a=a_0-a_2t+a_4t^2-a_6t^3,\quad O_a=a_1-a_3t+a_5t^2-t^3.
\]
Let \([\underline o_i,\overline o_i]\), \(i=1,2,3\), be the actual global bands of the three positive roots of the odd components, ordered and strictly separated as in §2. Form the following eight ordered triples by independently choosing one endpoint from each set:
\[
x_1\in\{0,\underline o_1\},\quad
x_2\in\{\overline o_1,\underline o_2\},\quad
x_3\in\{\overline o_2,\underline o_3\}.
\]
For each of the eight choices put
\[
e^{(\nu)}=(x_1x_2x_3,\ x_1x_2+x_1x_3+x_2x_3,\ x_1+x_2+x_3),\quad \nu=1,\ldots,8. \tag{1}
\]
Duplicates are harmless when bands degenerate.

For an actual corner \(a\), \(t\in[0,\infty]\), and \(0\le r\le3\), define compactified even and odd row coordinates
\[
u_r(a,t)=\frac{E_a(t)(-t)^r}{(1+t)^7},\qquad
v_r(a,t)=\frac{tO_a(t)(-t)^r}{(1+t)^7}. \tag{2}
\]
At infinity set \(u=(0,0,0,0)\) and \(v=(0,0,0,1)\); at zero \(u=(a_0,0,0,0)\), \(v=0\).

**Theorem.** Exactly one of the following holds:

* **Synthesis:** There is one real numerator of exact degree seven with \(\operatorname{Re}(b(i\omega)/a(i\omega))>0\) for every \(a\in K\) and every finite real \(\omega\).
* **Eight-atom obstruction:** There are \(1\le m\le8\) actual parity-corner/squared-frequency atoms \((a_i,t_i)\), \(t_i\in[0,\infty]\), and positive weights \(\lambda_i\) summing to one, for which
\[
\sum_i\lambda_i v(a_i,t_i)=0\in\mathbb R^4,\qquad
\sum_i\lambda_i\Bigl(e_0^{(\nu)}u_0+e_2^{(\nu)}u_1+e_4^{(\nu)}u_2+u_3\Bigr)(a_i,t_i)\le0
\quad\text{for every }\nu=1,\ldots,8. \tag{3}
\]

The atoms are actual corners, not arbitrary formal rows. This is a no-go certificate **for the given box itself**; it need not have strictly negative monomial coordinates and may include endpoint atoms. The eight test triples are explicitly determined by the box's odd-root bands, with no guessed numerator profile.

Equivalently, synthesis holds exactly when **every** odd-canceling convex atom measure has strictly positive even pairing at at least one of the eight triples in (1). These vertex choices may depend on the measure; the minimax proof below yields one common numerator despite that apparent quantifier order. Checking only individual extreme circuits is insufficient because mixtures of circuits can matter.

## 2. The box-dependent Vieta polytope

For any actual denominator, Hermite–Biehler gives three simple positive even and odd roots interlaced \(e_1<o_1<e_2<o_2<e_3<o_3\). Even and odd coefficient parts vary independently, so extrema of any even and odd roots can be combined in one actual stable member. Compactness and continuity of simple roots therefore give strict separation of successive global root bands. Each odd-root range is a full interval because the odd coefficient box is connected and the ordered root is continuous.

If \(b\) is a common exact-degree numerator, its leading coefficient is positive. For a fixed stable \(a\), the path \((1-\theta)a+\theta b\) has no imaginary-axis zeros and positive leading coefficient because its ratio to \(a\) has positive real part on the imaginary axis. Root continuity then makes \(b\) Hurwitz; in particular \(b_6>0\). Normalize \(b_6=1\) and write
\[
F_e(t)=E_b(t)=e_0-e_2t+e_4t^2-t^3.
\]
At any actual odd-root frequency the pairing reduces to \(E_aF_e>0\). The signs of \(E_a\) on the three odd bands are \(-,+,-\), so \(F_e\) has these signs throughout those bands. Together with \(F_e(0)>0\), this implies its three roots lie respectively in
\[
I_1=(0,\underline o_1),\quad I_2=(\overline o_1,\underline o_2),\quad I_3=(\overline o_2,\underline o_3). \tag{4}
\]
Conversely the root-gap condition (4) is exactly an open convex polyhedron \(\mathcal P_K\) in \(e\), given by strict linear sign inequalities at the odd-band endpoints and zero.

Its closure is exactly
\[
\overline{\mathcal P_K}=\operatorname{conv}\{e^{(1)},\ldots,e^{(8)}\}. \tag{5}
\]
To see this, the Vieta map \(V(x)=(x_1x_2x_3,\sum_{i<j}x_ix_j,\sum_i x_i)\) sends the open product of the three intervals in (4) onto \(\mathcal P_K\). Compactness and continuity extend its image to the product of the closed intervals, even when adjacent endpoints coincide. Since \(V\) is affine in **each** \(x_i\), every image point is a convex combination of the eight endpoint images using the product of the three barycentric weights. The reverse containment follows because \(\overline{\mathcal P_K}\) is closed and convex. The eight triples may describe boundary polynomials with a zero or repeated root; they are test points, not claimed original numerators.

## 3. A three-variable compact minimax

Let \(S\subset\mathbb R^8\) be the compact set of rows \((v(a,t),u(a,t))\) in (2), for the four actual parity corners and \(t\in[0,\infty]\), and put \(D=\operatorname{conv}S\). Define the compact convex odd-canceling slice
\[
D_0=\{u\in\mathbb R^4:(0,u)\in D\}.
\]
It is nonempty because a zero-frequency row has \(v=0\). For \(e\in\mathbb R^3\), set
\[
L_e(u)=e_0u_0+e_2u_1+e_4u_2+u_3,\qquad
m(e)=\min_{u\in D_0}L_e(u). \tag{6}
\]

For any fixed \(e\), there is an odd coefficient vector \(z=(b_1,b_3,b_5,b_7)\) and a uniform positive margin \(\delta\) such that every corner row satisfies
\[
L_e(u)+z\cdot v\ge\delta>0 \tag{7}
\]
if and only if \(m(e)>0\). Necessity follows by integrating (7) against any odd-canceling probability measure. For sufficiency, the compact convex hull of the points \((v,L_e(u))\) is disjoint from the closed ray \(\{(0,s):s\le0\}\). Strict separation gives a functional \(h\cdot v+\lambda L_e(u)>0\) with \(\lambda\ge0\). If \(\lambda=0\), add a sufficiently small positive multiple of \(L_e\), using compactness, and then divide by \(\lambda>0\). At infinity (7) gives \(b_7=z_3>0\); four-corner affine minimization supplies a common exact-degree numerator.

Moreover \(m(e)>0\) automatically forces \(e\in\mathcal P_K\): the zero-frequency corner row forces \(e_0>0\). An actual member's odd-root row has \(v=0\) and belongs to \(D\), since at that fixed frequency it is a convex combination of the four corner rows. Thus \(m(e)>0\) forces \(E_aF_e>0\) on every odd-root band. Hence synthesis is equivalent to
\[
\Gamma_K:=\max_{e\in\overline{\mathcal P_K}}m(e)>0. \tag{8}
\]
The maximum is attained because \(m\) is the minimum of a compact family of affine functions and is continuous, and the closed polytope is compact.

Finite-dimensional convex minimax applies to the compact convex sets \(\overline{\mathcal P_K}\) and \(D_0\), with the continuous bilinear-affine payoff \(L_e(u)\). Using (5),
\[
\Gamma_K
=\min_{u\in D_0}\max_{e\in\overline{\mathcal P_K}}L_e(u)
=\min_{u\in D_0}\max_{1\le\nu\le8}L_{e^{(\nu)}}(u). \tag{9}
\]
This is the exact reason that the vertex in the preceding paragraph may depend on the odd-canceling measure while one common numerator still exists.

## 4. Why eight actual atoms suffice on the original box

If \(K\) has no common numerator, (8)–(9) give an attained \((0,u^*)\in D\) with all eight vertex values \(L_{e^{(\nu)}}(u^*)\le0\). We show this point is a convex combination of at most eight actual corner rows.

If \(D\) has affine dimension at most seven, Carathéodory in its affine hull gives at most eight rows. Otherwise \(D\) is full dimensional. If \((0,u^*)\) were an interior point, for sufficiently small \(\epsilon>0\) the point \((0,u^*-\epsilon e_3)\) would still belong to \(D\), keeping the four odd moments zero. Since every \(L_e\) has coefficient **one** on \(u_3\), this would decrease the maximum of all eight vertex values by \(\epsilon\), contradicting minimality. Thus \((0,u^*)\) lies on a supporting face of dimension at most seven. Every row in a convex representation of that point lies in the face, and Carathéodory there again gives at most eight actual rows. Positive weights are normalized to sum one after zero weights are removed. This is precisely (3).

Conversely, suppose (3) holds and a common numerator exists. Normalize it by \(b_6=1\); §2 gives its even triple \(e\in\mathcal P_K\). By (5), \(e\) is a convex combination of the eight listed triples, so (3) gives \(L_e(\sum_i\lambda_i u_i)\le0\). The odd coordinates cancel, hence the same sum is the positive-weight average of the common numerator's compactified corner pairings. Every finite-frequency pairing is strictly positive and the infinity pairing is \(b_7>0\), a contradiction. The two alternatives are exhaustive and mutually exclusive.

## 5. Exact certificate data for rational boxes

If \(K\) has rational endpoints, each odd-band endpoint is a real algebraic root of one of the rational odd endpoint cubics. Indeed \(O_-(t)\le O_a(t)\le O_+(t)\) on \(t\ge0\): at the first and third positive roots, where the sign changes from positive to negative, the lower endpoint's root is earliest and the upper endpoint's root latest; at the second root, where the sign change is reversed, the upper endpoint's root is earliest and the lower endpoint's root latest. The global root-band order makes these comparisons unambiguous, including coincident endpoints. Thus all eight Vieta triples are real algebraic. If a no-go certificate exists, its existence is an existential semialgebraic statement over the real algebraic numbers: enumerate \(m\le8\), the finite corner assignments, endpoint flags, positive atom weights and nonnegative finite frequencies, impose the four equalities and eight inequalities (3), and clear only positive \((1+t)^7\) denominators. The transfer/quantifier-elimination theorem for real closed fields then guarantees an algebraic-frequency, algebraic-weight certificate; exact algebraic sign and equality checks verify it. Rational weights or frequencies are **not** claimed for the same original box.

For a rational box with a common numerator, a rational numerator and rational positive-definite Gram/SOS certificate can instead be obtained by compact uniform strictness, rational density in the coefficient/Gram affine space, and the one-variable interval Markov–Lukács theorem. Thus exact real-algebraic quantifier elimination in principle decides the fixed rational-box question and yields checkable positive or negative certificates. No such quantifier elimination was run here, no resource/runtime claim is made, and this fixed-instance decidability is not a universal yes/no verdict.

## 6. Assurance and exact remaining question

Named imports: odd-degree Hermite–Biehler interlacing; compactness, root continuity and strict finite-dimensional separation; Carathéodory; finite-dimensional convex minimax; and, only for §5, real-closed-field quantifier elimination and the interval Markov–Lukács theorem. The parity projection, explicit eight Vieta vertices, minimax use, face-support reduction and certificate verification are derived above. No numerical search, scientific program, historical held source, earlier unreviewed theorem or external model is used as a premise. Parent-classified incidental source-display exposure is carried in `owner-incidental-held-source-search-display-v1.json`; no clean-cognition assertion is made.

The original task is now a concrete unrestricted alternative: prove that every eligible box forbids a measure satisfying (3), or produce and verify one eligible box and such a measure. The theorem itself supplies neither. No independent review, formal proof, parent adoption or novelty clearance has occurred.
