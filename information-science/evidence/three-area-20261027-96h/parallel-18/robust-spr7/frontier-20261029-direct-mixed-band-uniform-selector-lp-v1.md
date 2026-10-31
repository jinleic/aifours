# An exact 16-ray selector LP for direct strict five-node certificates

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:17:44 PDT 2026**. **WRITTEN exact fixed-data characterization**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It is a concrete universal-proof route for one direct-certificate pattern, not an all-parameter theorem.

## 1. Data and the property

Fix an admissible odd coefficient box with global root bands \([a,b],[c,d],[e,f]\), and five positive squared frequencies
\[
a<t_1<t_2<b<t_3<t_4<c<t_5<d. \tag{1}
\]
For a parameter \(0\le\theta\le1\), let
\[
\xi=(1-\theta)t_3+\theta t_4,\qquad
F_\theta(t)=(-t)(\xi-t)(d-t). \tag{2}
\]
The corresponding even numerator coefficients \((0,\xi d,\xi+d,1)\) are nonnegative. The direct odd-moment cone for any negative-coordinate certificate has the eight four-node extreme rays from `frontier-20261029-direct-five-node-first-band-tail-exclusion-v1.md`, SHA-256 `6d5824dcccef37037b8fd23de103d55382920b2e1f8229c9fcf589d7ed4e2a55`: supports \(X=(t_1,t_2,t_3,t_5)\), \(Y=(t_1,t_2,t_4,t_5)\), each with any one odd moment \(-1\) and the other three zero.

The **direct uniform-selector property** is that one \(\theta\) makes the \(F_\theta\)-pairing strictly positive on **every** one of these eight rays, for every all-Hurwitz even interval box with the fixed odd box and every allowed actual member/odd value at each node. This property excludes a strictly negative eight-coordinate certificate on the five nodes, because the nonnegative-coefficient numerator would have a negative pairing against such a certificate. It is stronger than necessary and covers only (1).

## 2. Exact 16-case linear feasibility

For each ray \(r\in\{X,Y\}\), omitted odd moment \(k\in\{0,1,2,3\}\), and middle-node odd endpoint \(\sigma\in\{-,+\}\), form its normalized physical finite weights
\[
w_i^{(k)}=\frac{e_{3-k}(\{u_j:j\ne i\})}{u_iO_i(u_i)\prod_{j\ne i}(u_i-u_j)}. \tag{3}
\]
The first, second and final odd endpoint values are \(O_-(t_1),O_+(t_2),O_+(t_5)\). At the middle node use the chosen \(O_\sigma\). On X the middle even value is bounded below in the pairing using \(E_+\), on Y using \(E_-\); the first two use \(E_+\) and the fifth uses \(E_-\). These choices are valid for every \(\theta\in[0,1]\): the corresponding \(F_\theta\) signs do not change inside that interval.

The resulting 16 fixed-endpoint mixed-envelope functionals \(g_{r,k,\sigma}(\theta)\) are affine in \(\theta\) and linear in the eight even interval endpoints. Let \(S_j\) be the six strict root-band stability forms, \(W_j=u_j-\ell_j\ge0\), and \(\ell_j>0\), exactly as in `frontier-20261029-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `8a8f5ee8430b4c313846cdd61149e99a7ec433dab36971df57d75bcb44e7f6ac`. Seek
\[
\begin{aligned}
&0\le\theta\le1,\quad\delta>0,\\
&g_{r,k,\sigma}(\theta)=\sum_{j=1}^6\alpha_{r,k,\sigma,j}S_j
+\sum_{j=0}^3\beta_{r,k,\sigma,j}W_j+\sum_{j=0}^3\gamma_{r,k,\sigma,j}\ell_j,\\
&\alpha,\beta,\gamma\ge0,\quad
\sum_j\alpha_{r,k,\sigma,j}+\sum_j\gamma_{r,k,\sigma,j}\ge\delta
\quad\text{for all 16 cases}. \tag{4}
\end{aligned}
\]
Equality of forms means eight scalar coefficient equalities. This is a finite linear program in \(\theta,\delta\) and 224 nonnegative dual multipliers.

**Theorem.** For fixed odd box and nodes (1), (4) is feasible if and only if the direct uniform-selector property of §1 holds for the family (2). Feasibility gives an exact no-strict-certificate proof for those data and **every** admissible even box. Infeasibility does not provide a negative certificate: a box-dependent selector, another nonnegative numerator, or cancellation among rays could still suffice.

## 3. Justification and nonvacuity

The positive sign at the first two finite pairings makes the prescribed odd endpoint magnitudes worst there; positivity of both the actual even component and \(F_\theta\) at \(t_5\) makes \(O_+\) worst there. The middle odd value stays negative and the pairing is affine in its reciprocal, so one of its two endpoints is worst. Independent actual members realize the separate endpoint minima. For a stable even box, all \(S_j,\ell_j\) are strictly positive and all \(W_j\) nonnegative, so (4) implies strict positivity of all 16 ray pairings.

Conversely, if one \(\theta\) works uniformly, each of the 16 mixed-envelope linear forms is positive on the nonempty open stable-even-box cone. The finite-dimensional Motzkin strict linear alternative represents it by nonnegative combinations of the 14 defining forms, with a strictly positive total coefficient on the strict forms. Combining the 16 representations and choosing a common positive \(\delta\) gives (4), exactly as in the four-ray predecessor. The eight odd-cone rays exhaust every positive combination with the required nonpositive odd coordinates; zero-odd and endpoint atoms are removable in the precise \(F_\theta\)-pairing sense proved in the direct-tail predecessor.

At bands \((1,4,7,13,20,24)\), nodes \((2,3,5,6,8)\) and \(\theta=1/2\), all 16 cases have strictly positive exact rational dual witnesses in `frontier-20261029-direct-mixed-band-strict-duals-frozen-v1.json`, SHA-256 `c93ec265d3473e118aca6b49f6b06bf02190a055050db226591a0a809b38834b`. The resulting explicit nonvacuous \(10^{-40}\) neighborhood is `frontier-20261029-open-direct-mixed-band-five-node-exclusion-v1.md`, SHA-256 `c519196145154da3cef9f64366a97bccea90f244719a8215b7e775904a48a3f4`. These are author-written evidence with exact finite checks on one Eval host, not independent proof acceptance.

## 4. The precise open step

Prove (4) feasible for **every** admissible odd box and every node tuple satisfying (1), or exhibit one exact tuple making (4) infeasible. A universal feasible-selector proof would settle this one mixed-band placement of the direct five-frequency strict-certificate question; it would not settle the other phase patterns, larger supports or unrestricted SPR7 synthesis. No such universal proof or infeasible tuple is supplied. No formal proof, independent scientific review, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
