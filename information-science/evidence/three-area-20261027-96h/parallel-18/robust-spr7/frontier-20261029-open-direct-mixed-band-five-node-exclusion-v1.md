# An open mixed-band exclusion for direct strict five-node certificates

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:14:51 PDT 2026**. **WRITTEN theorem candidate with WRITTEN-checked-in-kernel exact rational duals and perturbation guard**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It is a direct strictly-negative-coordinate result on an explicit open region, not a universal SPR7 verdict.

## 1. Statement

Let \(\epsilon=10^{-40}\), and independently perturb the six ordered odd-band roots and five positive squared frequencies by at most \(\epsilon\):
\[
(a,b,c,d,e,f)\approx(1,4,7,13,20,24),\qquad
(t_1,t_2,t_3,t_4,t_5)\approx(2,3,5,6,8). \tag{1}
\]
The monic odd endpoint cubics are
\(O_-=-(t-a)(t-d)(t-e)\), \(O_+=-(t-b)(t-c)(t-f)\). Their difference retains strictly positive coefficients in \((1,t,t^2)\), so they define an actual independent odd coefficient box with positive odd widths.

For **every** all-Hurwitz independent monic septic box with those odd intervals and arbitrary positive even intervals, and arbitrary actual members and positive weights at the five nodes, no aggregate pairing functional can have **all eight numerator-monomial coordinates strictly negative**, even with any additional zero-odd, zero-frequency or infinity atoms. The final node stays inside the second odd band \((c,d)\), which is not covered by the universal outside-band direct theorem `frontier-20261029-direct-five-node-first-band-tail-exclusion-v1.md`, SHA-256 `6d5824dcccef37037b8fd23de103d55382920b2e1f8229c9fcf589d7ed4e2a55`.

This result is nonvacuous in every tuple: the even box centered at \((363/8,407/4,45/2,1)\) with radius \(1/1000\) is strictly Hurwitz with the perturbed odd box and has four positive even widths. The explicit marker and odd-width safeguards are in `frontier-20261029-open-odd-box-five-node-exclusion-v1.md`, SHA-256 `f9cdddb08d93ded38ea227e3b25a577b5dceb991ab7b3e744d3dec9b626212fd`; its proof uses a larger \(10^{-30}\) root neighborhood and applies here.

## 2. Sixteen direct odd-moment ray identities

Put \(\xi=(t_3+t_4)/2\) and
\[
F(t)=(-t)(\xi-t)(d-t).
\]
Its even numerator coefficients are \((b_0,b_2,b_4,b_6)=(0,\xi d,\xi+d,1)\), all nonnegative. Thus an aggregate with all eight coordinates strictly negative would have a strictly negative \(F\)-pairing. Zero-frequency and infinity atoms have zero \(F\)-pairing; removing an infinity atom only decreases the last odd coordinate. A zero-odd atom has nonnegative \(F\)-pairing because \(F\) and each actual even component have the same sign on all three odd-root bands, so removing it also preserves a negative \(F\)-sum. Merge coincident nodes by actual coefficient averaging.

As proved directly in the named outside-band theorem, a nonzero measure with all four odd coordinates nonpositive must have sign word \((- ,+,-,-,+)\), and its pointed odd-moment cone has exactly eight extreme rays: supports
\(X=(t_1,t_2,t_3,t_5)\), \(Y=(t_1,t_2,t_4,t_5)\), each with one of the four odd coordinates equal to \(-1\) and the other three zero. On four ordered support nodes \(u_i\), these ray weights are
\[
w_i^{(k)}=\frac{e_{3-k}(\{u_j:j\ne i\})}{u_i O_i(u_i)\prod_{j\ne i}(u_i-u_j)}>0,\quad k=0,1,2,3. \tag{2}
\]
The fixed odd endpoint choices at nodes 1, 2 and 5 that minimize the appropriate positive contributions are respectively \(O_-,O_+,O_+\); the middle odd value may be either endpoint. The signs of \(F\) require the **upper** even envelope at nodes 1,2,3 and the **lower** envelope at nodes 4,5. Thus there are exactly \(2\times4\times2=16\) fixed-endpoint mixed-envelope functionals to control.

At the base data, every one has an exact identity
\[
g=\sum_{j=1}^6\alpha_jS_j+\sum_{k=0}^3\beta_k(u_k-\ell_k)+\sum_{k=0}^3\gamma_k\ell_k,\qquad
\alpha_j,\beta_k,\gamma_k>0, \tag{3}
\]
where \(S=(-E_+(a),-E_+(b),E_-(c),E_-(d),-E_+(e),-E_+(f))\). All 16 sets of finite weights and 14 dual multipliers, their generator order, and the exact odd-moment/dual identities are frozen in `frontier-20261029-direct-mixed-band-strict-duals-frozen-v1.json`, SHA-256 `c93ec265d3473e118aca6b49f6b06bf02190a055050db226591a0a809b38834b`. Exact `fractions.Fraction` arithmetic in one Eval host checked the 16 eight-coordinate identities, 16 odd-moment vectors and all 224 strict multiplier signs. Every base \(\alpha_j<3\), and every \(\beta_k,\gamma_k\ge10607/234114048>10^{-6}\).

## 3. Explicit perturbation of the duals

For each case keep its six base \(\alpha_j\) fixed. Reconstruct the width and lower-coefficient multipliers uniquely from the perturbed target functional after subtracting \(\sum\alpha_jS_j\):
\[
\beta_k=\operatorname{coeff}_{u_k}(\text{remainder}),\qquad
\gamma_k=\operatorname{coeff}_{\ell_k}(\text{remainder})+\beta_k. \tag{4}
\]
At all points in (1), every denominator factor in (2) has magnitude at least \(4/5\), every linear factor is bounded by 50, and each input changes by at most \(\epsilon\). The elementary-symmetric factor has at most three monomials and degree at most three. Thus one target coefficient is a sum of four rational terms, each with at most three numerator monomials of at most nine linear factors and one seven-factor denominator. Telescoping and \(|D|>1/5\) give a per-term change at most
\[
270\epsilon50^8+1050\epsilon50^{15}. \tag{5}
\]
Each coefficient in a stability form changes by at most \(2000\epsilon\); since \(\sum_j\alpha_j<18\), every \(\beta_k\) changes by at most \(36000\epsilon+4(5)\), and every \(\gamma_k\) by at most twice that. Exact rational arithmetic gives
\[
2\left(36000\epsilon+4(270\epsilon50^8+1050\epsilon50^{15})\right)
=\frac{32043457031260546875000009}{1250000000000000000000000000000000000}<10^{-6}. \tag{6}
\]
Every perturbed \(\beta_k,\gamma_k\) therefore stays positive. The fixed \(\alpha_j\) remain positive and all six stability forms remain strict for any eligible box. Each of the 16 mixed-envelope ray pairings is strictly positive; arbitrary actual odd values cannot do worse than the tested endpoints. Every positive combination of the eight odd-cone rays therefore has strictly positive \(F\)-pairing, a contradiction.

## 4. Limits and evidence

This is a direct strict-coordinate exclusion in a concrete 11-parameter open family, including final nodes in the second odd band. It neither proves all five-node configurations impossible nor produces an eligible-box negative certificate; all larger supports and the original universal synthesis-or-obstruction verdict remain **OPEN**. The finite identities and bounds were checked exactly on one Python Eval host; interpolation, cone decomposition, endpoint selection and perturbation bounds are written deductions. No independent scientific review, formal proof, parent adoption or novelty clearance occurred. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
