# An exact mixed-envelope exclusion with the final node in the second odd band

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:52:06 PDT 2026**. **WRITTEN theorem candidate with WRITTEN-checked-in-kernel exact rational identities**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a nonvacuous fixed-odd-box/node result, not the unresolved all-box second-band theorem.

## 1. Statement and scope

For any all-Hurwitz independent monic septic box whose odd intervals are
\[
a_1\in[260,672],\quad a_3\in[292,293],\quad a_5\in[34,35],\quad a_7=1,
\]
no weak odd-canceling/eight-Vieta-vertex no-go can be supported on the five squared frequencies
\[
(t_1,t_2,t_3,t_4,t_5)=(2,3,5,6,8) \tag{1}
\]
plus infinity and zero-odd atoms, even if every finite atom uses an arbitrary actual box member and arbitrary positive weights. The odd-root bands are \([1,4],[7,13],[20,24]\); the final node 8 lies **inside** the second odd band, the case left open by `frontier-20261029-first-band-second-odd-tail-erratum-v1.md`, SHA-256 `c786730ef8de45ddd13d3021b16715f32ede6c0bb18c67a8607f573e394a0745`.

The result is nonvacuous: `frontier-20261029-fixed-odd-box-uniform-five-node-exclusion-v1.md`, SHA-256 `be552e11fcfb832f77cc15d4a523ee6eee7d0b5863313a17fd32c84eec84883e`, gives an explicit all-seven-positive-width all-Hurwitz box with precisely these odd intervals. That example supplies admission only, not the proof below.

## 2. Correct mixed envelopes and two circuits

The odd extrema are
\[
O_-=-(t-1)(t-13)(t-20),\qquad O_+=-(t-4)(t-7)(t-24).
\]
Odd cancellation reduces to two four-finite-plus-infinity rays, with supports \(X=(2,3,5,8;\infty)\) and \(Y=(2,3,6,8;\infty)\), exactly as in the named weak-circuit theorem: first-node odd sign negative, second positive, middle negative, last positive. Normalize each infinity mass to 1. Let
\[
F(t)=(-t)(11/2-t)(13-t). \tag{2}
\]
This is the average of the two closed Vieta vertices with middle roots 4 and 7, so any measure nonpositive at every Vieta vertex must pair nonpositively with \(F\).

At the nodes in (1), \(F\) evaluates to \((-77,-75,-20,21,100)\). Let \(E_-\le E_+\) be the actual box's even envelopes. For ray X, the first three pairings are bounded **below** with \(E_+\), and the final pairing with \(E_-\). For ray Y, the first two use \(E_+\), while the last two use \(E_-\). This explicitly respects the sign change in \(F\); it does not repeat the earlier incorrect upper-envelope substitution.

At 2 and 3 the actual even value is negative, while at 8 it is positive. Thus, for either ray, the worst positive contributions use \(O_-(2)\), \(O_+(3)\), and \(O_+(8)\). At the remaining middle node the odd value is always negative and the minimum over actual odd parts is at either \(O_-\) or \(O_+\), depending on the even-envelope sign. It therefore suffices to prove four endpoint cases.

## 3. Four exact Farkas identities

Use even-indexed interval variables \(\ell_k,u_k\) for coefficients \(a_{2k}\), \(k=0,1,2,3\), and let \(W_k=u_k-\ell_k\ge0\). Define five strictly positive stability margins
\[
A=-E_+(1),\quad B=-E_+(4),\quad C=E_-(7),\quad D=E_-(13),\quad E=-E_+(20). \tag{3}
\]
Let \(g_X^-\), \(g_X^+\), \(g_Y^-\), \(g_Y^+\) denote the appropriate **mixed-envelope** weighted sums with middle odd endpoint minus or plus. With the finite weights in (4) below, the following identities hold exactly:
\[
\begin{array}{c|r|rrrrr|rrrr}
&\text{scale}&A&B&C&D&E&W_0&W_1&W_2&W_3\\\hline
X^-&1158312960&16600080&31018925&0&3220880&610671&707180&21761840&383451920&5789258960\\
X^+&4401589248&58921968&144208043&0&10358192&1964121&806132&58240016&1139202608&17866293104\\
Y^-&3199150080&33483628&54511361&3580664&7785364&1399251&0&37250412&790412844&12795036012\\
Y^+&1919490048&19246100&33745387&10650184&3373868&645057&0&21770580&412223316&6186697236.
\end{array} \tag{4}
\]
Each row means `scale * g = A_coefficient*A + ... + W3_coefficient*W3`. Every coefficient is nonnegative, and at least one strict-margin coefficient is positive. Hence all four mixed-envelope sums are strictly positive for **every** eligible even interval box.

The physical finite circuit weights, in support order, are
\[
\begin{array}{c|rrrr}
X^-&1/7128&1/2520&1/43200&1/46080\\
X^+&1/7128&1/2520&1/3420&1/46080\\
Y^-&1/9504&1/3780&1/70560&1/30720\\
Y^+&1/9504&1/3780&1/5184&1/30720.
\end{array} \tag{5}
\]
For each row the four odd moments cancel with infinity weight 1. The table can be reproduced directly from \(w_i=[t_iO_i(t_i)\prod_{j\ne i}(t_i-t_j)]^{-1}\), (2), and the coefficientwise definitions of \(E_-\) and \(E_+\).

For arbitrary actual odd values the same conclusion follows from endpoint minimization, and arbitrary actual even values pair no smaller than the respective mixed envelopes. Each ray's pairing with \(F\) is strictly positive, so any nonzero positive combination of the rays is strictly positive. Since \(F\) is a convex combination of two required Vieta vertices, at least one of those vertices has a positive pairing. A weak no-go is impossible.

## 4. Evidence and limits

The four identities in (4) were checked by reconstructing all eight even-endpoint coefficients with exact Python `fractions.Fraction`/integers in one Eval host; the finite weights (5) and odd endpoint values were computed there as well. The signs of (3), endpoint minimization, circuit decomposition, interpolation and interlacing are written deductions. This is not a general proof for arbitrary odd bands or five-node placements, an actual negative certificate, formal proof, independent scientific review, parent adoption or novelty clearance. The original arbitrary-box synthesis-or-obstruction verdict remains **OPEN**. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
