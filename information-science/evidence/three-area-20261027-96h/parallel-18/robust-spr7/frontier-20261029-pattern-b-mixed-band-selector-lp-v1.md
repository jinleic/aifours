# A mixed-envelope direct selector for the second residual phase pattern

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:43:48 PDT 2026**. **WRITTEN fixed-data LP characterization with a WRITTEN-checked-in-kernel nonvacuous exact instance**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. The universal pattern-B question remains open.

## 1. Exact fixed-data selector LP

For any admissible independent odd coefficient box with root bands \([a,b],[c,d],[e,f]\), fix nodes
\[
a<t_1<t_2<b<c<t_3<d<t_4<t_5<e. \tag{1}
\]
This is the remaining mixed-band portion of direct phase pattern \(B=(2,1,3,5,4)\) in `frontier-20261029-three-strict-pattern-eight-ray-reduction-v1.md`, SHA-256 `8591da67f304472da00e7afb7bf1ddfc1c2a7970802f7c844cf8cd495ee93686`. The actual odd signs required by a nonzero odd-moment ray are \((- ,+,-,+,+)\); the odd value at \(t_3\) is selected negative within the second odd band, while the odd values at \(t_4,t_5\) are positive for every member.

For \(0\le\theta\le1\), let
\[
\xi=(1-\theta)t_4+\theta t_5,\qquad F_\theta(t)=(-t)(c-t)(\xi-t). \tag{2}
\]
Its corresponding even numerator coefficients \((0,c\xi,c+\xi,1)\) are nonnegative; its roots lie in the closed global even-root gaps. Every zero-odd row has nonnegative \(F_\theta\)-pairing and can be deleted from a putative strictly negative certificate without losing the negative total or odd-coordinate signs.

The eight odd-moment cone rays have supports \(X=(t_1,t_2,t_3,t_4)\) and \(Y=(t_1,t_2,t_3,t_5)\), with four omitted-moment weights as in equation (4) of the named input. At the first three nodes, the worst odd endpoints are respectively \(O_-,O_+,O_-\), because their contributions to the correctly bounded pairing are positive. At the fourth node of each ray, both odd endpoints must be checked. The correct even envelopes are
\[
X:\quad(E_+,E_+,E_-,E_-),\qquad
Y:\quad(E_+,E_+,E_-,E_+). \tag{3}
\]
Thus there are 16 mixed-envelope forms, each affine in \(\theta\) and linear in the eight even interval endpoints.

Let \(S_j\) be the six strict odd-band stability forms, \(W_k=u_k-\ell_k\ge0\), and \(\ell_k>0\) the four even lower coefficients. The exact linear program asks for \(0\le\theta\le1\), \(\delta>0\), and 16 separate nonnegative multiplier sets such that
\[
g_{r,k,\sigma}(\theta)=\sum_{j=1}^6\alpha_jS_j+\sum_{i=0}^3\beta_iW_i+\sum_{i=0}^3\gamma_i\ell_i,
\qquad\sum_j\alpha_j+\sum_i\gamma_i\ge\delta. \tag{4}
\]
The equality is coefficientwise in the eight interval-endpoint variables. As in the pattern-A proof `frontier-20261029-direct-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `b5380caec863a2c4e807db1aab912ee3aed2bc37fe72d2d0382d7b1262c4f36e`, the finite-dimensional Motzkin strict alternative shows that (4) is feasible **if and only if** one selector (2) gives strictly positive pairing on every relevant odd ray uniformly over all stable even boxes and actual member choices. Feasibility rules out a direct strict certificate for those fixed odd/node data. Infeasibility rules out only this stronger uniform selector family, not a direct certificate or common numerator.

## 2. A fully realized pattern-B example

Take the odd intervals \([260,672]\), \([292,293]\), \([34,35]\) for \((a_1,a_3,a_5)\), whose root bands are \([1,4],[7,13],[20,24]\), and nodes
\[
(t_1,t_2,t_3,t_4,t_5)=(2,3,10,15,18). \tag{5}
\]
For \(\theta=1/2\), \(\xi=33/2\). All 16 direct-ray mixed-envelope functionals admit exact nonnegative dual identities with a positive strict-form coefficient. The 16 weights, multiplier vectors, odd-moment identities and even-coordinate identities are frozen in `frontier-20261029-pattern-b-mixed-sixteen-duals-frozen-v1.json`, SHA-256 `636918ffeb9fa6ca2216c810e5f0161901c297bc9223b7d13946e06281845328`. Exact `fractions.Fraction`/integer arithmetic on one Eval host checked all 16 odd vectors \(-e_k\) and all 16 eight-coordinate dual identities. Hence the selector excludes a direct strict certificate for **every** stable even box over these fixed odd intervals and nodes.

This fixed-data result is nonvacuous even at the level of the literal **phase-B placement**. Choose even interval endpoints
\[
\ell=(87/1000,36479/500,1089/50,911/1000),\qquad
u=(87/500,99099/1000,21867/1000,1089/1000). \tag{6}
\]
All seven coefficient widths are positive. Its six odd-band sign margins are
\[
12957/250,\quad9/100,\quad87/1000,\quad87/1000,\quad93/500,\quad174909/100,
\]
so the box is all-Hurwitz. At the five nodes choose odd endpoints \((O_-,O_+,O_-,O_-,O_+)\), and even endpoints \((E_-,E_-,E_-,E_-,E_+)\). Their exact parity sign sequence is
\[
(--),\ (-+),\ (+-),\ (-+),\ (++),
\]
i.e. phase word \((2,1,3,5,4)\). In particular \(-E_-(15)=261273/1000>0\) and \(E_+(18)=229443/500>0\), so the forced even-root reversal is literal. These marker, parity and reversal arithmetic facts were checked exactly on the same Eval host. The box and sign word are **not** an existing strict certificate: the 16 duals exclude one on these nodes.

## 3. Limits

The open step is to prove the LP in (4) feasible for every eligible odd box and node tuple (1), or find one exact tuple for which this uniform selector fails. Either outcome addresses only the mixed-band part of pattern B; pattern A's mixed-band branch, pattern C, larger support and original unrestricted SPR7 synthesis remain open. This written result imports the scoped author phase classification and strict linear alternative; it is not a formal proof, independent scientific review, parent adoption or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
