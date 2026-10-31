# All three direct five-node patterns reduce to eight odd-moment rays

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:40:07 PDT 2026**. **WRITTEN theorem candidate**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It strengthens the direct strictly-negative-coordinate analysis, without settling the original question.

## 1. Universal eight-ray reduction

For an all-Hurwitz independent monic septic coefficient box, the named direct phase classification `frontier-20261029-strict-negative-certificate-two-band-obstruction-v1.md`, SHA-256 `33cce85c5451984a670de2ae05c921ea3a61d0c88c867c3c81a1bb94cd026783`, gives exactly three conservative phase words for a strictly negative all-eight-coordinate certificate with five distinct positive frequencies:
\[
A=(2,1,3,2,4),\quad B=(2,1,3,5,4),\quad C=(2,4,3,5,4). \tag{1}
\]
Use the standard signs by class \((++),(-+),(--),(+-),(++),(-+),(--)\). Their odd sign words are
\[
A:\ (-,+,-,-,+),\qquad B,C:\ (-,+,-,+,+). \tag{2}
\]
A zero odd value may be assigned either adjacent class in (1); for any even test cubic whose roots are in the closed common root gaps, that row has nonnegative test pairing and may be deleted without spoiling a hypothetical negative test sum.

For each of the three patterns, every nonzero positive weight vector with all four odd coordinates nonpositive is a positive combination of **at most eight extreme ray types**. The only possible four-node supports are
\[
\begin{array}{c|cc}
\text{pattern}&X&Y\\\hline
A&(1,2,3,5)&(1,2,4,5)\\
B,C&(1,2,3,4)&(1,2,3,5).
\end{array} \tag{3}
\]
For each support, four ray types indexed by \(k=0,1,2,3\) have physical finite weights
\[
w_i^{(k)}=\frac{e_{3-k}(\{u_j:j\ne i\})}{u_i O_i(u_i)\prod_{j\ne i}(u_i-u_j)}>0,\qquad
V_r=-\mathbf1_{r=k}\quad(r=0,1,2,3). \tag{4}
\]
Here \(u_i\) are the four increasing nodes of that support and \(e_j\) is an elementary symmetric polynomial. These rays involve **no added infinity atom**: the one remaining negative odd coordinate is part of the direct strict-certificate cone.

Proof. The oriented weak-moment sign lemma in `frontier-20261029-direct-five-node-first-band-tail-exclusion-v1.md`, SHA-256 `6d5824dcccef37037b8fd23de103d55382920b2e1f8229c9fcf589d7ed4e2a55`, requires an odd sign subsequence \((- ,+,-,+)\) or \((+,-,+,-,+)\). The sign words in (2) have only the displayed four-node subsequences and no five-node alternating subsequence. A pointed five-dimensional cone extreme ray has at least four independent active constraints. Supports of size below four are impossible by the sign lemma; support five would need all four odd moments zero and hence an alternating Vandermonde null vector, which (2) forbids. Thus an extreme ray has one of (3) and exactly three zero odd moments. Lagrange coefficient identities give the four positive formulas (4). Deleting an odd-zero atom cannot introduce a new support; a ray on a proper subset is already covered by (3) or is impossible. The cone decomposition is elementary finite-dimensional polyhedral geometry.

Consequently, to disprove a direct strict certificate in one of these patterns, it is sufficient to find **one** even-only nonnegative-coefficient test numerator whose pairing is nonnegative on every listed ray and strictly positive on at least one ray carrying weight. It is enough, but not claimed necessary, to choose a Vieta-gap cubic so odd-zero rows have nonnegative pairings and zero/infinity rows have zero pairing. The direct 16-ray mixed-envelope selector LP is one explicit way to seek such a test in pattern A when its fifth node lies in the second odd band.

## 2. A second universal direct exclusion

For pattern B, suppose its third positive node satisfies \(t_3\le c\), where \([c,d]\) is the second global odd-root band. Then no strictly negative all-eight-coordinate certificate exists, for **any** eligible septic box and any actual members or positive weights.

Indeed the first two nodes lie in the first odd band by the required backward odd crossing, the fourth and fifth lie in the third even-root band inside \((d,e)\) by the required backward even crossing, and the class-3 third node is in \((b,c]\) whenever it is nonzero. Both supports in (3) are therefore four-node circuits with first two nodes in the first odd band, the third in \((b,c]\), and the fourth in \((d,e)\). Use the same nonnegative-coefficient even test
\[
F(t)=(-t)(c-t)(d-t). \tag{5}
\]
Its sign is nonpositive at all four nodes. For \(t_3<c\), the \(k=3\) pairing on each of the eight even-root vertices is strictly positive by the four-node proof in `frontier-20261029-universal-first-odd-band-five-node-exclusion-v1.md`, SHA-256 `c2ee101472efe7e7c6ba4d10e8fd3ab1c78d40f1146307f0feb126b6c59129af`. For \(t_3=c\), the third contribution vanishes and the same quadratic-baseline argument is in `frontier-20261029-first-band-four-circuit-extension-v1.md`, SHA-256 `02014c2e520266977bb9fd157dbb5e92793513190d9c89c2c932c0566e79d465`, under the mandatory correction `frontier-20261029-first-band-second-odd-tail-erratum-v1.md`, SHA-256 `c786730ef8de45ddd13d3021b16715f32ede6c0bb18c67a8607f573e394a0745`.

The factors \(e_{3-k}(\widehat u_i)\) in (4) are nonincreasing with increasing \(u_i\). For vertex term signs \((+,+,+,+)\), \((+,+,+,-)\), or \((+,+,-,-)\), this preserves the positive \(k=3\) sum by the monotone-weight argument in the direct-tail predecessor. For \((+,+,-,+)\), its explicit monotone comparison (8) proves the second positive base term exceeds the magnitude of the third negative term, so every nonincreasing weight sequence preserves positivity. Thus all eight direct odd-cone rays have positive \(F\)-pairing, contradicting strict negativity of the even monomial coordinates. Actual even values are dominated correctly by the upper envelope because \(F\le0\) at all selected nodes. This proves the assertion, including zero-odd and endpoint atoms.

## 3. Exact remaining regions

Subject to the named three-word classification and these written candidates, direct strictly negative five-node certificates remain possible only in the following **unresolved** regions:

- Pattern A: the fifth node lies inside the second odd band \((c,d)\); the complement is excluded by the direct-tail predecessor.
- Pattern B: the third node lies inside the second odd band \((c,d)\); the complement is excluded by §2.
- Pattern C: the full classified placement remains open.

These are necessary residual regions, not existence claims and not an unrestricted SPR7 verdict. The fixed-data mixed-band 16-ray selector LP `frontier-20261029-direct-mixed-band-uniform-selector-lp-v1.md`, SHA-256 `b5380caec863a2c4e807db1aab912ee3aed2bc37fe72d2d0382d7b1262c4f36e`, addresses only pattern A's listed mixed-band region. No universal LP feasibility or impossibility result is claimed.

Named imports: the exact scoped author-written phase/root-band and four-node packets above, finite-dimensional cone decomposition, Lagrange interpolation and Hermite–Biehler interlacing. No formal proof, independent scientific review, parent adoption or novelty clearance is claimed. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
