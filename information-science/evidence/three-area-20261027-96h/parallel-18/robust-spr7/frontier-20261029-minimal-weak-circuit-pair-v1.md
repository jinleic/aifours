# Both minimum-support weak obstructions reduce to one adjacent duplicate and two circuits

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 16:00:28 PDT 2026**. **WRITTEN structural theorem candidate**; the one finite count stated in §4 was separately WRITTEN-checked-in-kernel with integer arithmetic. No independent review, parent adoption, formal proof or novelty clearance is claimed.

## 1. Scope and imported statement

Use the actual eligible septic box, compactified rows, root gaps, odd cancellation and eight Vieta vertices from `frontier-20261029-eight-atom-vieta-alternative-v1.md`, SHA-256 `f107da4124a5a1b4516d1e9aeb7bde2ddbcc341367d869fe0916a1407da09e10`. Import the weak-certificate six-location theorem and root-alignment proof from `frontier-20261029-vieta-weak-obstruction-six-support-v1.md`, SHA-256 `d6ffee1555fbde2dd7e29d477c64ceab07632db3b6eb6cc69b90e5ac3267cc0b`. Both are author-written, unreviewed candidates. As in the latter, merge same-frequency actual members, remove zero-odd rows, and retain a weak certificate whose odd row sum is zero and all eight even vertex sums are nonpositive.

**Theorem.** On either six-location frontier — (A) five positive finite nodes plus infinity, or (B) six positive finite nodes and no infinity — any weak obstruction has all of the following properties:

1. In the ordered finite nodes, the signs of the actual odd values have exactly **one adjacent repeated sign**; every other adjacent pair has opposite signs.
2. The repeated-sign pair is exactly the pair making the mandatory backward crossing of one even-root band. In particular these two nodes are adjacent, are in the same even gap, and have strictly opposite actual even signs in the backward order.
3. The positive odd-cancellation cone on these fixed finite nodes and infinity flag has exactly **two** extreme rays. They are the interpolation circuits obtained by omitting respectively the first and second node of that repeated-sign pair. Both rays occur with strictly positive coefficients in every obstruction supported at all six locations.
4. Consequently all eight Vieta inequalities reduce **exactly** to one positive scalar interval for the ratio of the two circuit weights. The interval coefficients have the divided-difference formula in §3.

These are necessary structural restrictions and an exact *fixed-data* feasibility test, not a claim that either frontier is feasible or impossible for actual boxes.

## 2. Alternation and the unique doubled node

In case A, the positive infinity mass requires at least one four-finite-node infinity circuit in a decomposition of the odd-canceling measure. Its odd signs are \((- ,+,-,+)\). Therefore the five finite odd signs have at least three changes. In case B, an extreme circuit has five finite nodes with alternating signs, so the six odd signs have at least four changes.

The imported root-alignment theorem forces a backward even-band crossing: two nodes lie in the same even gap and have reversed even signs. Every odd component has one fixed nonzero sign throughout that gap. The nodes and every finite node between them therefore have the same odd sign. Thus the odd sign word has at least one repeated adjacent sign. Since A has only four adjacencies and B only five, it has **exactly one** repetition. The crossing nodes must be precisely that adjacent repeated-sign pair: any intermediate node or another pair in the same gap would create at least two repetitions.

In case A the four possible odd sign words are
\[
--+-+,\quad -++-+,\quad -+--+,\quad -+-++. \tag{1}
\]
In case B the word is obtained from either alternating five-letter sign word by doubling exactly one of its letters. Deleting either of the doubled nodes restores the required alternating pattern. The backward odd-band crossing from the imported theorem lies outside this even-gap pair.

## 3. Two explicit circuits and their divided differences

Write the two adjacent repeated-sign finite nodes \(t_\ell<t_r\); the remaining finite nodes are shared. Let \(X\) contain all shared nodes and \(t_\ell\), and \(Y\) all shared nodes and \(t_r\). In A, each of \(X,Y\) has four finite nodes, the odd signs are \((- ,+,-,+)\), and both circuits contain infinity. In B, each has five finite nodes, the odd signs alternate in the same orientation, and neither has infinity. Let
\[
H_X(t)=\prod_{j\in X}(t-t_j),\quad H_Y(t)=\prod_{j\in Y}(t-t_j),\quad
 d_i=\frac{t_i O_{a_i}(t_i)}{(1+t_i)^7}\ne0. \tag{2}
\]
For A set \(c=1\); for B choose the common \(c\in\{-1,+1\}\) making all the weights positive. The two ray weights are
\[
\lambda_i^X=\begin{cases}c/[d_iH_X'(t_i)],&i\in X,\\0,&i\notin X,\end{cases}\quad
\lambda_i^Y=\begin{cases}c/[d_iH_Y'(t_i)],&i\in Y,\\0,&i\notin Y,\end{cases} \tag{3}
\]
with \(\lambda_\infty^X=\lambda_\infty^Y=1\) in case A and zero in case B. Positivity follows from the alternating signs and Lagrange's sign pattern. The four odd moments vanish by the usual interpolation identities: \(\sum t_i^k/H'(t_i)=0\) below degree \(|X|-1\), while the top identity is one. The signs of \(H'\) at the same ordinal place are the same for \(X\) and \(Y\), so the same \(c\) works in B.

The odd-row matrix has rank four. At six columns its kernel has dimension two; its nonnegative intersection is pointed. Both vectors in (3) are distinct positive extreme rays because each has minimal support of five actual locations. A pointed two-dimensional polyhedral cone has at most two extreme rays, so these are all of them. A single ray cannot obstruct by the imported alignment theorem, hence both coefficients are strictly positive.

Define actual ratios and their circuit vertex costs by
\[
R_i=\frac{E_{a_i}(t_i)}{t_iO_{a_i}(t_i)},\qquad
g_\nu^X=c\sum_{i\in X}\frac{F_\nu(t_i)R_i}{H_X'(t_i)},\quad
g_\nu^Y=c\sum_{i\in Y}\frac{F_\nu(t_i)R_i}{H_Y'(t_i)}. \tag{4}
\]
The factors \((1+t_i)^7\) cancel exactly, and the infinity row has zero even part. Equivalently, \(g_\nu^X/c\) is the divided difference of the finite data \(F_\nu(t_i)R_i\) on \(X\), with the analogous formula for \(Y\). Thus the original eight nonpositive vertex inequalities are equivalent to
\[
\exists h>0:\quad g_\nu^X+h g_\nu^Y\le0\quad(\nu=1,\ldots,8). \tag{5}
\]
Indeed every nonnegative odd-canceling combination is a combination of the two rays, both must be present for a no-go, and their union covers all six locations. For fixed algebraic/rational node and member data the signs and interval bounds in (5) can be checked exactly; no solver outcome is asserted here.

Each ray has at least one strictly positive vertex cost by root alignment. Therefore the interval can also be checked by the explicit cross-product conditions: if \(g_\nu^X>0\), then \(g_\nu^Y<0\) and \(h\ge g_\nu^X/(-g_\nu^Y)\); if \(g_\mu^Y>0\), then \(g_\mu^X<0\) and \(h\le(-g_\mu^X)/g_\mu^Y\). All other rows must obey their own inequality, including zero cases. In particular every such pair of active lower/upper constraints must satisfy
\[
g_\nu^X g_\mu^Y\le g_\mu^X g_\nu^Y. \tag{6}
\]
The converse uses **all** rows and zero cases as in (5), not only one cross-product.

## 4. Finite phase-word screen and boundary

For case A the preceding packet's integer-only enumeration leaves 12 conservative class words. Applying its same predicates to case B, with six class entries and an odd-sign subsequence of five alternating signs in either orientation, yields exactly **57** words. This count was checked on one Python Eval host by exhausting \(7^6\) integer words with `itertools.product` and `itertools.combinations`; it is a conservative necessary screen including allowed even-zero class assignments, not a proof that any word is realizable. The case-A twelve-word list and exhaustive predicates are in the imported packet. No numerical polynomial search, external theorem or model was used to derive the two-circuit claim.

The next representation is now explicit: for each actual-box realization of the twelve A or 57 B phase words, use the unique doubled even-band pair and the two divided-difference vectors (4), then prove that the scalar interval (5) is empty, or give an eligible box and exact algebraic data making it nonempty. A failure to find an instance is not an exclusion. Even ruling out both minimum frontiers leaves all certificates with seven or eight locations and therefore does not solve the universal septic target.

The only machine check claimed is the finite integer phase-word count. The root, sign, circuit, rank, and interval arguments are written mathematical deductions; no formal proof, separate scientific review, parent adoption, external-model review or novelty claim is made. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
