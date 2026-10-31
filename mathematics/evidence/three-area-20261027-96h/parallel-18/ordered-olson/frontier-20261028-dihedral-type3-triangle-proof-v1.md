# A prefix-triangle theorem for the two-sign `R=3p−4` subclass

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 18:33:07 PDT 2026**. This is a self-contained **WRITTEN proof candidate**, with the bounded actual-word checks in §6. No disjoint scientific review, formal proof, novelty or global-adoption verdict has yet occurred.

## 1. Exact theorem

Let p be ANY odd prime and `a∈F_p` nonzero. Let W be an actual original-order word of length `4p−1` in

`D_(2p)=<r,s | r^p=s^2=1, srs=r^(-1)>`.

Suppose its rotations consist of exactly `2p−3` occurrences of `r^a` and `p−1` occurrences of `r^(−a)`, in ARBITRARY original positions and order. The other `p+3` occurrences are arbitrary reflections `r^y s`, likewise in arbitrary positions. Then W has an identity-product subsequence of EXACTLY `2p` original occurrences in increasing index order.

Only this two-sign multiplicity subclass of the R=3p−4 band is claimed. No other multiplicity case, L_RES, all-band or original all-group closure follows. This proof does not depend on the unreviewed `R=3p−3`, `R=3p−2` or all-high candidates.

## 2. Combinatorial prefix-triangle lemma

Forget the reflection exponents temporarily. Define the INTEGER prefix Q at a reflection to be `#(r^a rotations before it) − #(r^(−a) rotations before it)`. For two actual reflection positions i<j call the edge **low** if

`−1 <= Q_j−Q_i <= p−1`.  (1)

**Lemma.** With `2p−3` plus rotations, `p−1` minus rotations and `p+3` reflections in arbitrary order, there are i<j<k whose THREE pair edges are all low.

*Proof.* Suppose no such triangle exists. Call a pair HIGH-POSITIVE if `Q_j−Q_i>=p`, and HIGH-NEGATIVE if `Q_j−Q_i<=−2`. A high-positive interval contains at least p actual plus rotations. Since the whole word has only `2p−3<2p` plus rotations, the sets of plus occurrences in any two high-positive intervals intersect. Each set is an interval in the linear order of plus occurrences, so ALL such sets share one plus occurrence: choose the greatest left endpoint and the least right endpoint. This is the elementary interval-Helly argument, with no external theorem import.

If there are NO high-positive intervals, every consecutive triple of reflections must contain a high-negative edge and therefore at least two minus rotations in its two gaps. There are `(p+3)−2=p+1` such windows. Each minus rotation belongs to at most two windows, so at least p+1 minus rotations would be required, contradicting p−1. Thus a high-positive interval exists.

Cut the actual word at a plus rotation shared by ALL high-positive intervals. Let L,R be the numbers of reflections on its left and right; L+R=p+3. There is no high-positive pair wholly inside either side. In a side with N reflections, each of its `(N−2)_+` consecutive triple windows must contain at least two minus rotations, since otherwise all its edges would be low. Counting windows, at least `(N−2)_+` minus occurrences are needed inside that side.

Both L and R are at least2: if, say, L<=1, the R-side alone would require at least `p` minus rotations. Therefore

`p−1 >= (L−2)+(R−2) = p−1`.

Equality holds everywhere. In each side, every consecutive triple window contains EXACTLY two minus rotations and each actual minus rotation is counted in exactly two of those windows. All p−1 minus rotations lie in side-internal gaps; none lies before the first reflection, after the last, or in the gap crossing the cut.

For a side with N>=3 reflections, write b_1,...,b_(N−1) for the numbers of minus rotations in its internal consecutive-reflection gaps. Equality means `b_1=b_(N−1)=0` (an end gap belongs to only one window) and `b_i+b_(i+1)=2` for every window. Hence the gap counts alternate `0,2,0,2,...,0`, and N is even. A side of size2 is also one doublet with zero minus in its sole gap. In particular, side size3 is impossible.

A gap with two minus rotations contains NO plus rotation. Otherwise, take either side-internal triple window containing it; the other gap in that window has zero minus rotations. With at least one plus in the two-minus gap, both individual prefix increments and their sum are at least −1. No high-positive pair lies within the side, so all three increments are at most p−1. That would be a low triangle, contrary to assumption.

Each side therefore consists of consecutive **doublets** of reflection occurrences. Inside a doublet there are zero minus rotations and some `z>=0` plus rotations; z<=p−1 because the doublet lies wholly on one side of the cut. Between consecutive doublets there are EXACTLY two minus rotations and no plus rotations. For each right-side doublet write its two INTEGER prefixes as `U_i<=V_i`. Then

`0<=V_i−U_i<=p−1`,  `U_(i+1)=V_i−2`.  (2)

Let X be the prefix of the last left-side reflection. No minus rotation crosses the cut and the cut is an actual plus rotation, so `U_1−X>=1`. Since `(X,U_i,V_i)` cannot be a low triangle and the doublet edge is low, either `U_i−X<=−2` or `V_i−X>=p`. For i=1 the former is impossible, so `V_1−X>=p`. By (2), `U_(i+1)−X=V_i−X−2>=p−2>=1`; induction gives `V_i−X>=p` for every right doublet. In particular the LAST reflection's prefix V satisfies

`V−X>=p`.  (3)

Take the FIRST left doublet, with prefixes `U<=V_0`. Its edge is low. Between V_0 and X, the integer prefix can decrease by at most the total p−1 minus rotations, so `(3)` gives `V−V_0>=p−(p−1)=1`. By the saturated count ALL p−1 minus rotations lie between the first and last reflections, and at most `2p−3` plus rotations do. Thus

`V−U <= (2p−3)−(p−1)=p−2`.

Since U<=V_0, this yields

`0<=V_0−U<=p−1`, `1<=V−V_0<=p−2`, `1<=V−U<=p−2`.

The first left doublet and the last reflection are therefore a low triangle, contradiction. QED.

## 3. Convert the low triangle to original selectors

For any pair i<j of the lemma, if `u=Q_j−Q_i`, the signed rotation multiset consists of

`2p−3−u` values +a and `p−1+u` values −a.

The edge is low exactly when both multiplicities are at most2p−2, equivalently both are at least p−2. Let T_ij be the sum of all these signed values. To select `2p−2` rotations, omit p−2 actual rotations. Every omission choice with q signed −a occurrences and p−2−q signed +a occurrences, `0<=q<=p−2`, is available. Its p−1 sums are all field residues except 0: the formal next q=p−1 sum is `−a−(−a)=0`. Consequently the obtainable **selected** signed rotation sums are exactly `F_p\{T_ij}`.

The actual product with reflections i<j is `r^[selected signed sum + y_i−y_j]`. Thus the pair succeeds unless `y_j−y_i=T_ij`.

Apply this to the lemma's i<j<k. The raw rotation total is

`T_0 = [(2p−3)−(p−1)]a = −2a !=0`.

Because the actual intervals (i,j),(j,k) are disjoint and partition (i,k),

`T_ij+T_jk−T_ik = T_0 !=0`.  (4)

The actual reflection differences necessarily satisfy `(y_j−y_i)+(y_k−y_j)−(y_k−y_i)=0`. They cannot all equal their respective T values in (4). Hence at least one of the THREE actual reflection pairs has an obtainable target, and it plus `2p−2` actual rotations is an original-order identity selector. This proves §1.

## 4. Proof boundary and gap coupling

Equation (4) uses all three ACTUAL reflection intervals and their shared raw rotations. No independent-packet lift, joint-affinity assertion, arbitrary Hessian interpolation, shortened word or assumed reflection exponents are involved. The selector uses exactly TWO actual reflections in this subclass, although this does not imply that two or four reflections suffice for all R=3p−4 words; the separate six-reflection family disproves that stronger assertion.

The elementary two-value missing-support calculation is rederived in §3. It is also consistent with, but does not import a review verdict from, the same-owner source `frontier-20261028-dihedral-two-support-cocycle-v1.md`, SHA256 `8fbfd99636eade69410dd700836995b62ec95575b9f33a3a612633fc3ede03e4`.

## 5. Explicit finite-search limits

Before finding the all-prime written proof, an author-run prefix DFS found no no-triangle prefix in the p=5,7,11 type-III budgets (325, 3,035 and 185,456 visited nodes, respectively). The saved results are `frontier-20261028-dihedral-prefix-obstruction-results.json` SHA256 `1095ef05d4a86a17926f08a72f9ee7b60a51aacf122f5cf53cd8b5c71066fd1f`; `frontier-20261028-dihedral-prefix-type3-p7-results.json` SHA256 `a3cde9bd7b4ad5601afbbb6eb3ec6f0f4663d5bf1af6a504c66b7c12fc481b3c`; and `frontier-20261028-dihedral-prefix-type3-p11-results.json` SHA256 `4d7b34dc1ad3d7e145fb4477420edde75d4a3cb824cd4f1f23fb220731652005`. These are bounded, unreviewed program outputs; they are NOT the reason for the universal theorem and are not advertised as independent executable certificates.

## 6. Actual original-word checks

`frontier-20261028-dihedral-type3-triangle-experiment.py`, SHA256 `fc80148607f034ed4cb4c3b40e840077e41ea1f8da10f1eb2e15f811dbc19b6d`, generated `frontier-20261028-dihedral-type3-triangle-results.json`, SHA256 `c953aa656bc5bd5a7e1f42cf3ff5c8fbff12be8013d2baf3869a689b149f328e`, containing 400 random full actual words at p=3,5,7,11,13 (80 each) and 220 full saturated-window family words at those primes. These include all placements of the cut relative to the two-minus-block groups within the coded family; this is not a claim to exhaust every arbitrary word.

Separately written checker `frontier-20261028-dihedral-type3-triangle-checker.py`, SHA256 `71dabac73dfed44fbc3bc90cbb08f4aa6fada7459432287b8ecb13bd74ad45d1`, imports no producer. It returned `PASS_INDEPENDENT_TYPE3_TRIANGLE_CHECK` in `frontier-20261028-dihedral-type3-triangle-check-results.json`, SHA256 `fd3f0d7fa93749fbdf023f607b5e44ce073fa0ac86bebfdb754f24cdee4970a5`: it recomputed actual type counts, integer prefix triangles, all three pair signed supports and raw-total cocycle; directly multiplied all620 distinct-index original selectors; reconstructed all220 saturated-layout words; and rejected duplicate-index, false-prefix and duplicate-triangle-index mutations for their intended reasons.

Those finite checks do not establish the universal prefix lemma, a formal proof, independent-model-family review or novelty. A complete disjoint written review is requested.

**END — type-III all-prime written candidate and actual evidence.**
