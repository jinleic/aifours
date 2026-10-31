# A forbidden even-root edge and a two-template mixture barrier

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 18:22:01 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel finite exact rational certificates**; no parent adoption, independent review, formal proof or novelty clearance. These statements do not resolve the arbitrary-box septic problem.

## 1. A nonvacuous forbidden region of even numerator roots

Use the explicit stable interval box in `frontier-20261029-pattern-c-entire-vieta-face-failure-v1.md`, SHA-256 `6ab23593f984a52e0585cb0c3d53edb629a2b2f891047f8eedabf73598b5bbf9`. Its odd-root bands have endpoints
\[
(a,b,c,d,e,f)=(1,21/20,221/20,241/20,441/20,461/20).
\]
For any common numerator, its normalized even roots satisfy \(x_1\in(0,a)\), \(x_2\in(b,c)\), \(x_3\in(d,e)\). They **cannot** additionally satisfy
\[
0<x_1\le 1/100,\quad b<x_2<c,\quad d<x_3\le d+1/100. \tag{1}
\]
In fact the negative atom pairing below holds throughout the *closed* rectangle \([0,1/100]\times[b,c]\times[d,d+1/100]\).

This exclusion is nonvacuous: the same box has a common numerator whose normalized even roots are \((1/2,2,20)\), with all-frequency evidence in `frontier-20261029-pattern-c-face-box-common-numerator-v1.md`, SHA-256 `82c4427dff213aa1b69d015c53b20300829e11de12a83e737c68fd6143c6311c`. Thus choosing a middle root such as 2 does not by itself determine whether a valid even numerator part can be completed by odd coefficients.

## 2. Six actual finite atoms

With the corner ordering 0: \((E_-,O_-)\), 1: \((E_-,O_+)\), 2: \((E_+,O_-)\), 3: \((E_+,O_+)\), take
\[
\begin{array}{c|c|l}
t&\text{corner}&w\\\hline
221/20&0&297435434913/5951275000000\\
111/10&1&831806484061/844285425000\\
12&0&1099462128037/8401800000000\\
241/20&1&709631061867/277029500000000\\
15&2&1541/20000000\\
24&2&61/100000000.
\end{array} \tag{2}
\]
There is no infinity atom. All six weights are positive and the four odd moments vanish exactly:
\[
\sum_iw_it_iO_i(t_i)(-t_i)^r=0\quad(r=0,1,2,3). \tag{3}
\]
The even-root pairing
\[
G(x_1,x_2,x_3)=\sum_iw_iE_i(t_i)\prod_{j=1}^3(x_j-t_i) \tag{4}
\]
is multi-affine in the three roots. Each of its eight endpoint values on the closed rectangle in (1) is strictly less than \(-1\), so the entire rectangle has \(G<-1\). If any odd numerator coefficients completed an even part from that rectangle to a common strictly positive-real numerator, all six actual-corner finite pairings would be positive; after multiplying by the positive weights and applying (3), their sum would equal a positive multiple of \(G\), contradiction.

The exact weights, moments, all eight signed rational endpoint values, and the positive value at \((1/2,2,20)\) are in `frontier-20261029-face-box-edge-region-frozen-v1.json`, SHA-256 `5b7fda174044384b8c126a67252f7cb85e76c38c52c94f1cb96c034a433d7`.

## 3. Why the two previously found opposite-face measures are not enough

Keep the *odd coefficient interval* fixed as in the named box, but allow **any** independent even coefficient box making the full box Hurwitz. Consider only nonnegative combinations, not both zero, of the two previously frozen odd-canceling templates: the five-finite-atom upper-face measure in the named face-failure packet and the seven-finite-atom lower-face measure in `frontier-20261029-face-box-opposite-odd-measure-frozen-v1.json`, SHA-256 `09a093ffa80fd0a48c92dc15c0c5c6a5131d8519c714cc94f1cb96c034a433d7`. Their specified even corners/interpolated first atom remain legitimate for every such even interval.

For each template separately, the weighted even pairing at the **closed Vieta selector**
\[
(x_1,x_2,x_3)=(0,2,d),\qquad
V(0,2,d)=\tfrac{181}{200}V(0,b,d)+\tfrac{19}{200}V(0,c,d), \tag{5}
\]
is strictly positive for every such stable even box. Hence no nonnegative mixture of those two templates can have all eight Vieta vertex pairings nonpositive, and this particular mixture approach cannot furnish the unrestricted weak no-go.

The fixed-support proof is a pair of rational Farkas identities. In even endpoint order \((l_0,l_2,l_4,l_6,u_0,u_2,u_4,u_6)\), use the fourteen inward cone rows
\[
(l_0,l_2,l_4,l_6,\ u_0-l_0,u_2-l_2,u_4-l_4,u_6-l_6,\ -E_+(a),-E_+(b),E_-(c),E_-(d),-E_+(e),-E_+(f)).
\]
Both selector pairing coefficient rows are exact nonnegative linear combinations of those rows, with a strictly positive multiplier on at least one of the six strict band rows. All multipliers, coefficient rows and exact identity checks are in `frontier-20261029-two-fixed-measures-uniform-cone-duals-v1.json`, SHA-256 `2cec9f519ebae6c21e82913fa05ce6acb70889d1b465feace3ba8b6b0ed66b61`. The strict band signs follow from robust Hurwitz interlacing; nonnegative endpoint widths suffice.

**Essential limitation:** the new six-atom measure (2), on the actual same box, has \(G(0,2,d)<-1\). Thus (5) is *not* a universal separator for arbitrary atom supports, even on that one solvable box. The two-template identity cannot be promoted to such a claim.

## 4. Assurance and remaining gap

Fractions, odd-moment equalities, eight multi-affine vertex inequalities, the two cone identities and the positive interior check were computed exactly with Python `fractions.Fraction`/integers on one Eval host. The box interlacing, convex interpolation and no-completion deductions are written arguments; no Lean/kernel proof or independent scientific verification is asserted. The general synthesis-or-actual-obstruction question and the residual five-frequency direct-certificate cases remain **OPEN**. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
