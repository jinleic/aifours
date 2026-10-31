# A complete linear obstruction test after freezing the odd box and odd atoms

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:20:51 PDT 2026**. **WRITTEN exact original-box reduction**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It supplies a finite LP for fixed admissible data, not an actual feasible counterexample or a universal positive result.

## 1. Fix only odd data

Fix positive finite odd-coefficient intervals \([\ell_1,u_1]\), \([\ell_3,u_3]\), \([\ell_5,u_5]\), and fixed monic leading coefficient one. At \(t\ge0\) their odd extrema are
\[
O_-(t)=\ell_1-u_3t+\ell_5t^2-t^3,\qquad
O_+(t)=u_1-\ell_3t+u_5t^2-t^3. \tag{1}
\]
Require that both cubics have three simple positive roots, with the ordered bands
\[
0<o_1^-\le o_1^+<o_2^-\le o_2^+<o_3^-\le o_3^+, \tag{2}
\]
where \((o_1^-,o_1^+)\) are respectively the first roots of \((O_-,O_+)\), \((o_2^-,o_2^+)\) are the second roots of \((O_+,O_-)\), and \((o_3^-,o_3^+)\) the third roots of \((O_-,O_+)\). Equality within a band is permitted. These are actual endpoint roots.

Fix \(m\) positive finite nodes \(t_i\), actual odd components \(O_i\) inside this odd coefficient box, finite weights \(w_i>0\), and an optional compactified infinity weight \(\eta\ge0\). Require the four **exact** odd-cancellation identities
\[
\sum_{i=1}^m w_i t_iO_i(t_i)(-t_i)^k+\eta\mathbf1_{k=3}=0,\qquad k=0,1,2,3. \tag{3}
\]
Here \(w_i\) is an uncompactified finite-pairing weight, so the corresponding compactified finite row has weight \(w_i(1+t_i)^7\); infinity already has weight \(\eta\). The nodes may repeat, although merging them is allowed. Odd-zero or zero-frequency atoms are unnecessary for an obstruction and may be omitted as in the named weak-certificate theorem.

Define eight fixed Vieta-vertex cubics
\[
F_\nu(t)=(x_1-t)(x_2-t)(x_3-t),\quad
x_1\in\{0,o_1^-\},\quad x_2\in\{o_1^+,o_2^-\},\quad
x_3\in\{o_2^+,o_3^-\}. \tag{4}
\]

## 2. Exact LP and equivalence

Introduce even interval endpoints \(0<\ell_k\le u_k\), \(k=0,1,2,3\), for coefficients \(a_0,a_2,a_4,a_6\), and values \(x_i\). Define affine expressions
\[
E_-(t)=\ell_0-u_1t+\ell_2t^2-u_3t^3,\quad
E_+(t)=u_0-\ell_1t+u_2t^2-\ell_3t^3. \tag{5}
\]
These \(\ell_k,u_k\) are **even-indexed variables** and do not denote the fixed odd endpoints in §1. Normalize \(\ell_3+u_3=2\). Consider the following linear system with one additional variable \(\delta>0\):
\[
\begin{aligned}
&\ell_k\ge\delta,\quad u_k\ge\ell_k &&(k=0,1,2,3),\\
&E_+(o_1^-),E_+(o_1^+)\le-\delta,\quad
E_-(o_2^-),E_-(o_2^+)\ge\delta,\\
&E_+(o_3^-),E_+(o_3^+)\le-\delta,\\
&E_-(t_i)\le x_i\le E_+(t_i) &&(1\le i\le m),\\
&\sum_{i=1}^m w_i x_iF_\nu(t_i)\le0 &&(1\le\nu\le8).
\end{aligned} \tag{6}
\]
All coefficients are constants once the odd data, nodes and weights are fixed. In particular this is one finite **linear** feasibility problem in eight interval endpoints, \(m\) scalar evaluations, and \(\delta\).

**Theorem.** Under (1)–(3), (6) is feasible if and only if there is an all-Hurwitz independent monic septic coefficient box with exactly the fixed odd intervals and actual members \(a_i\) whose odd parts are \(O_i\), whose even evaluations at \(t_i\) are \(x_i\), and for which the given finite/infinity weights satisfy the weak eight-vertex obstruction. Such a box has **no** common exact-degree-seven SPR numerator.

To require all seven widths positive, assume the three fixed odd widths are positive and add \(u_k-\ell_k\ge\delta\) for the four even widths. The same equivalence holds for an all-seven-positive-width box.

For rational fixed coefficient intervals, nodes, odd components and weights, the six odd-root endpoints and the LP coefficients are exact real algebraic numbers; if these roots are rational, (6) is a rational LP. Real-algebraic linear programming/real-closed-field elimination can decide the fixed instance. A feasible system has an exact real-algebraic solution; no claim of a rational solution or of a solver run is made.

## 3. Proof: all-member stability and reconstruction

Under (2), the endpoint signs and \(O_-\le O\le O_+\) ensure every odd component has one simple positive root in each band and no others. For example, between the first and second bands both odd extrema are negative, between the second and third both are positive, while the odd constant is positive and the leading term is negative. Thus odd roots stay in the three disjoint bands; all six band endpoints are attained.

For an independently varying even cubic, (5) are the exact pointwise minimum and maximum. The six inequalities in (6) are therefore equivalent to every even component having signs \(-,+,-\) across the three closed odd bands. More precisely the endpoint signs and positive even constant force three distinct even roots in
\[
(0,o_1^-),\qquad(o_1^+,o_2^-),\qquad(o_2^+,o_3^-).
\]
A cubic has no additional roots, so its signs remain correct throughout the bands. Every possible even/odd component pair interlaces, hence every member is Hurwitz by Hermite–Biehler. The reverse implication follows by pairing each actual odd endpoint with every possible even component. Strictness and finite constraint count permit a common \(\delta>0\).

For each feasible \(x_i\), the interval \([E_-(t_i),E_+(t_i)]\) is attained by even coefficient vectors in the box: interpolate between the two actual even endpoint vectors that realize \(E_-\) and \(E_+\) at \(t_i\). If the endpoints coincide, use either. Combine the resulting even coefficients with the prescribed actual odd component \(O_i\) by box independence. Therefore every LP solution reconstructs the required actual member atoms.

Equation (3) cancels every odd numerator coefficient in the weighted sum of the actual finite pairings and the infinity pairing. The eight inequalities in (6) make every vertex even pairing nonpositive. Every common numerator, normalized by its positive \(s^6\) coefficient, has its three even roots in the stated gaps; its even cubic is a convex combination of the eight \(F_\nu\). Thus a common numerator would make the same weighted sum both strictly positive and nonpositive, contradiction. Conversely, any box and atom set as in the statement supplies the LP values directly; a common positive rescaling of all even coefficients and \(x_i\) achieves \(\ell_3+u_3=2\) without changing stability or (3)–(6).

## 4. The remaining outer problem

The eight-atom original-box alternative `frontier-20261029-eight-atom-vieta-alternative-v1.md`, SHA-256 `f107da4124a5a1b4516d1e9aeb7bde2ddbcc341367d869fe0916a1407da09e10`, says any original no-synthesis box has a weak certificate with at most eight actual corner atoms. Its same-frequency merging and odd-zero removal preserve a valid certificate; all retained finite weights become positive \(w_i\), with infinity as in (3). Thus the original negative-existence question is exactly an **outer search over admissible odd boxes, actual odd components, nodes and positive odd-canceling weights**, followed by the single inner LP (6). This statement imports that author-written alternative, not parent acceptance. No outer tuple or LP feasibility has been supplied here.

The representation is materially narrower than the bilinear formulation with simultaneous unknown even-box coefficients and atom weights: after the odd data and weights are fixed, the even box, actual even evaluations, all-member stability and the weak no-go inequalities are all linear. The difficult outer odd-cancellation/box search remains open; fixing arbitrary sample atoms and finding no solution is not a universal proof.

Named imports: Hermite–Biehler interlacing, elementary root continuity and finite-dimensional real-algebraic linear feasibility. The proof is written mathematics; no computational execution, independent scientific review, formal verification, parent adoption, novelty clearance or original-box verdict is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
