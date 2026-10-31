# Ordered dihedral selector at the `R=3p−3` boundary

Owner **MathOlson-2-2**. Actual native `/bin/date` immediately before writing: **Wed Oct 28 18:02:36 PDT 2026**. This is a **WRITTEN theorem candidate**, with the bounded local computations disclosed in §8. It has not yet received a disjoint reviewer, human/formal verification, configured-family review, or novelty clearance. It is self-contained apart from elementary modular arithmetic and the displayed dihedral relations; earlier same-owner packets are listed for provenance, not silently adopted as an external theorem.

## 1. The theorem and what it does NOT claim

Let p be ANY odd prime. In the dihedral group

`D_(2p) = <r,s | r^p=s^2=1, srs=r^(-1)>`,

let W be an arbitrary ACTUAL word of length `4p−1`, with exactly `3p−3` rotation occurrences and exactly `p+2` reflection occurrences, in arbitrary original order. Then W has an identity-product subsequence of **exactly 2p original occurrences in increasing original index order**.

The proof does not assume a split into monochromatic blocks, a prespecified zero, a fixed reflection anchor, a symmetric order, or a witness in a shortened/reordered word. This settles ONLY the stated R=3p−3 band if the written proof is correct. Other rotation counts, arbitrary groups, any original L_RES bridge, and novelty/priority are outside this theorem.

Notation: a rotation of exponent x is `r^x`; a reflection of exponent y is `r^y s`; exponents lie in F_p. `L=2p−1`, `n=p−2`, `R=L+n=3p−3`, and `F=p+2`. Assume for contradiction that W has NO such selector throughout §§3–7.

## 2. Two elementary ingredients

### 2.1 Unequal-value pairing and modular support

For a multiset of N values whose largest multiplicity is M, there are at least `min(floor(N/2),N−M)` disjoint pairs of unequal values. The upper bound is immediate. For a construction repeatedly pair one occurrence from each of the two largest piles. If f denotes this minimum, deleting these two occurrences reduces `floor(N/2)` by one. If the maximum pile size falls, `N−M` falls by at most one. If the maximum does not fall, at least three piles had that size, so `N>=3M`, implying `N−M−1>=floor(N/2)>=f`. Thus after each deletion the same bound is at least f−1; induction constructs f pairs.

If `d!=0` in F_p and A is a nonempty proper set, `A ∪ (A+d)` has at least |A|+1 elements: equality with A would make A invariant under a generator of the entire prime cyclic group. Hence p−1 independent nonzero binary swaps cover all F_p. Similarly, the subset-sum set of k nonzero increments has at least `min(p,k+1)` elements.

### 2.2 Exact missing-subset-sum lemma

If `d_1,...,d_n` is zero-sum-free in F_p, with `n=p−2`, its subset-sum set A has at least p−1 values. If `A=F_p\{m}`, then **every** `d_i=−m`.

Proof: zero-sum-free makes each d_i nonzero, and §2.1 gives the size bound. Fix i and let B be subset sums of the other p−3 elements. Then `|B|>=p−2`. If `|B|=p−1`, B=A and `B+d_i⊆A=B`, impossible for a proper nonempty set and nonzero translation. Thus `|B|=p−2`. Since both B and B+d_i avoid m, the two residues missing from B are `m` and `m−d_i`. Zero-sum-freeness gives `−d_i∉B`, so either `−d_i=m` or `−d_i=m−d_i`. The latter would give m=0, impossible because 0∈A. Thus `d_i=−m`. This also covers p=3 and the empty B sequence. QED.

## 3. Arbitrary-position signed pair and the identical core

Fix ANY two actual reflection positions i<j with exponents y_i,y_j. Sign each actual rotation exponent x as +x outside the interval and −x strictly between i,j. Its selection with the two reflections has exponent

`sum(selected signed rotation values) + y_i−y_j`.  (2)

If the signed multiset's largest multiplicity M is at most `2p−2`, §2.1 supplies p−1 disjoint unequal signed pairs. Omitting one occurrence of each pair from all `3p−3` rotations leaves exactly `2p−2` rotations; the omission sums cover F_p, so (2) can be made zero. Therefore the no-selector assumption forces EVERY actual reflection pair to have a unique signed majority of at least L=2p−1.

That majority is not zero. Otherwise at least L raw rotation exponents are zero; among the F>p reflections two have the same exponent, and those two plus `2p−2` actual zero rotations select identity.

Fix one pair and its nonzero signed majority h. Its majority class consists of L raw occurrences with exponents in `{h,−h}`. Any other pair's L-sized majority class intersects it in at least `2L−R=p+1` actual rotations; on a common rotation, both signed values are ± the same nonzero raw exponent. Thus every pair's majority is h or −h.

Orient h as a so that m copies of a occur, with m>=p. If m>=2p, choose 2p a-rotations; if at least p copies of −a also occur, choose p of each. Both are original all-rotation identity selectors. Hence no-selector implies

`p<=m<=L` and `N_-:=#(−a rotations)<=p−1`.

For any two reflections define `u = #(a rotations between) − #(−a rotations between)`. The signed multiplicities of +a and −a are `m−u` and `N_-+u`. Their unique majority is one of these and has at least L occurrences, so

`u <= m−L <= 0`  OR  `u >= L−N_- >= p`.  (3)

Among the F−1=p+1 intervals between consecutive reflections, at most one has positive u, since each such interval contains at least p a-rotations and m<=2p−1. At most N_-<=p−1 intervals have negative u, because each contains a distinct −a-rotation. Some consecutive-reflection interval therefore has u=0. Its signed majority must be +a, since `N_-<L`; thus m>=L. Consequently

`m=L=2p−1`,

and exactly n=p−2 other rotations, with exponents `b_1,...,b_n`, remain. For any nonempty subset S of k extras, select it and `2p−k` actual a-rotations. This is possible because k>=1; its exponent is `sum_(i∈S)(b_i−a)`. Thus the translated extras `d_i=b_i−a` are zero-sum-free. This is an exact necessary reduction, not an assumption about the word.

## 4. Adjacent reflection pairs and the forced triple

Suppose there is a pair of reflections with NO ROTATION between them. Choosing any subset S of extras and `2p−2−|S|` core rotations yields total rotation exponent `−2a+sum_(i∈S)d_i`; all selected rotations have the same sign relative to that pair. If A is the subset-sum set of the d_i, the pair succeeds exactly when `y_j−y_i∈−2a+A`.

By §2.2, no-selector implies A has exactly p−1 elements, all d_i are equal to one nonzero d, and all extra rotations have the same exponent `b=a+d != a`. Every such reflection pair must have the SAME ordered difference

`y_j−y_i = −2a−d = −a−b`.  (4)

Two disjoint ACTUAL adjacent reflection pairs cannot occur. If they did, (4) gives reflection exponent contribution `2(a+b)`. Select those four reflections, `p−2` actual a-rotations and all `p−2` actual b-rotations. Their rotation exponent is `(p−2)(a+b)=−2(a+b)`. No rotation lies inside either actual adjacent pair, so rotation signs are positive before, between and after the pairs. Their `2p` selected original occurrences have identity product.

In particular, there are at most two adjacent-reflection boundaries. If there are exactly two, they must overlap into one run of exactly three consecutive reflections. For the three pairs within that run there is no rotation between them, so (4) applies to all three. The first-to-third difference is both the sum of the two equal adjacent differences and the same common difference, hence the common difference is zero. Therefore the three reflections have equal exponents, and

`b=−a`: all n=p−2 extra rotations have exponent −a.  (5)

No assumption that the endpoint reflections belong to the triple is made.

## 5. Counting the actual reflection gaps

For each reflection count how many of the L core a-rotations occur before it, and let g be the number of distinct such prefix counts. Let A be the number of boundaries where two consecutive reflection occurrences are actually adjacent in W. Among the F−1 consecutive-reflection intervals, exactly F−g have zero core rotations. A of those are empty; each of the other `F−g−A` contains at least one extra rotation.

The remaining g−1 intervals contain c>=1 core rotations. Let k be the number of raw −a extra rotations inside one of them, and let n_- be the total number of −a extras, with `n_-<=n`. The signed +a and −a counts for the two endpoint reflections are

`L−c+k` and `n_-+c−k`.

Their majority must be ±a and at least L, by §3. Hence

`c<=k` OR `c>=L−n_-+k >= p+1`.  (6)

Call an interval LARGE when `c>=p+1`. At most one can be LARGE, since consecutive-reflection intervals are disjoint and `2(p+1)>L`. Every other positive-core interval satisfies `k>=c>=1` and therefore contains an extra rotation. Thus, for g>=2,

`p−2 >= (F−g−A)+(g−2) = p−A`,

while for g=1, `p−2>=F−1−A=p+1−A`. These imply A>=2 in the first case, A>=3 in the second. But §4 rules out two disjoint adjacent reflection pairs, which implies A<=2. Therefore g>=2 and A=2: the two adjacent boundaries are one actual consecutive triple, whose exponents are equal and for which all extras are −a by (5).

The displayed lower bound now uses **all p−2 extra occurrences exactly**. Hence there must be exactly one LARGE positive-core gap: if there were none, the extra lower bound would be p−1. Every other counted gap contains exactly one extra, the LARGE gap contains none, and no extra lies outside the first and last reflections. The unique LARGE gap alone contains at least p+1 actual core rotations. These consequences are of the no-selector assumption; no arbitrary gap counts have been substituted.

## 6. Endpoint reflections plus the triple

Take the FIRST and LAST actual reflections, with exponents y_1,y_F. By §5 every one of the n=p−2 extra rotations lies strictly between them, where its raw exponent −a becomes signed +a. At least p+1 core rotations lie strictly between them, where their raw exponent +a becomes signed −a. Thus the endpoint signed multiset has at least p−2 occurrences of each of +a and −a.

If it has at least p−1 of each, pair p−1 opposite signed values and apply §3 to obtain a two-reflection identity selector. Under no-selector, therefore, the signed +a multiplicity must be exactly p−2, since the signed −a multiplicity is at least p+1. It follows that NO core rotation lies outside the first/last reflections: the endpoint signed values are exactly

`(+a)^(p−2)` and `(−a)^(2p−1)`.

Select `2p−2` of these rotations, with t of the +a values and the remainder −a, for any `0<=t<=p−2`. Such a choice always exists. Its signed exponent is `2(t+1)a`, and as t varies these are ALL the nonzero elements of F_p. If `y_F−y_1` is nonzero, choose the corresponding t and the first and last reflections to get a `2p`-occurrence identity selector. Therefore no-selector forces

`y_1=y_F`.  (7)

Now select `p−2` signed +a rotations and `p−2` signed −a rotations, so their signed total is zero. Select also the first and last reflections, and two MORE distinct reflections from the consecutive equal-exponent triple. There are always two such reflections: F=p+2>=5, so first and last cannot both lie inside the triple.

The inserted two reflections do not change the original rotation signs: if the triple is interior they form an adjacent equal pair with no intervening rotations; if the triple contains an endpoint, the three selected equal reflections are contiguous and have the same net action as that endpoint alone. Their reflection exponent contribution is zero when the triple is interior, and their combined three-reflection contribution is the original endpoint's when the triple is at an end. In either case, by (7), the four selected reflections have net exponent zero and even parity.

The selected occurrences are distinct, in their original order, and total `(p−2)+(p−2)+4=2p`. Their product is identity. This contradicts the no-selector assumption and proves the theorem.

## 7. Provenance, checks and nonclaims

Earlier same-owner written stages, all fully disclosed and not treated as third-party review: arbitrary signed-pair sufficient theorem `frontier-20261028-dihedral-signed-pair-selector-v1.md`, SHA256 `cc43e48c757c4fdba339a93598090ebaf9c42876c8547204b96ec3026032cac9`; identical-core / contiguous-triple analysis `frontier-20261028-dihedral-core-and-four-reflections-v1.md`, SHA256 `5e7f65b8764d4f52ccddadd9ea2934d0635ca5c2085a3c41e520b336a93c767f`; and two-adjacent-pair theorem `frontier-20261028-dihedral-two-adjacent-pairs-v1.md`, SHA256 `fc4b420c2d4f66b2be06640dec5a161567fa35c4024e626653c15d8f29e8e363`. The self-contained proof above pays their mathematical content, and uses no held or quarantined guidance as a premise.

§2.2 was independently exhausted in a bounded local checker on all nonzero input tuples at p=3,5,7, as recorded in the named core packet. This validates those finite instances only, not the all-prime proof.

## 8. Actual endpoint construction experiment

`frontier-20261028-dihedral-endpoint-triple-experiment.py`, SHA256 `47e2045454febf2a4c58a1e1377dd1e499dc223db4a440359ef977990777d021`, generated 480 actual normal-form words at p=3,5,7,11, with arbitrary triple placement, a large actual core-only gap, balanced/single-extra gaps, and core rotations possibly outside the endpoints. Exact saved input `frontier-20261028-dihedral-endpoint-triple-results.json`, SHA256 `5dc30a47cbde7742acde4019b82eacc4f920004b862b0d3905cc4f4b853ec3dc`.

A separately written checker, `frontier-20261028-dihedral-endpoint-triple-checker.py`, SHA256 `b392c8dbfb706eb65c270237f9a0ba624453ea96bd3a5696424bcc440e694709`, did NOT import the producer. Its actual `PASS_INDEPENDENT_ENDPOINT_TRIPLE_CHECK` result, saved as `frontier-20261028-dihedral-endpoint-triple-check-results.json`, SHA256 `c8fa8d814920047ded06829808c68851f7fa8888da0ad0e99dd0b95057cbf141`, inspects the actual word/gaps and directly multiplies all480 submitted original-index selectors. Observed branches: 237 with outside core and two reflections; 117 without outside core and two reflections; 126 without outside core and four reflections. Duplicate-index, false-large-gap and altered-endpoint metadata mutations were rejected for their intended reasons.

This check is **not** exhaustive over all words, and it does not independently establish §§3–5, formal proof, novelty, or a finite certificate for the complete theorem. It verifies the endpoint construction on the 480 saved full actual words only. A disjoint full written review is requested.

**END — complete R=3p−3 written candidate and exact evidence boundary.**
