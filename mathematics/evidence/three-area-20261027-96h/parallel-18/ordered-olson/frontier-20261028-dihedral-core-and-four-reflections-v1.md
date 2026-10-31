# Exact core reduction and a four-reflection selector

Owner **MathOlson-2-2**. Native `/bin/date` before this write: **Wed Oct 28 17:51:12 PDT 2026**. Scope **WRITTEN**, with separately disclosed exact bounded checks. This packet is a prospective theorem candidate, not a completed peer review, formal proof or novelty clearance.

## 1. Main written statements

Let p be any odd prime and W an actual ordered word in `D_(2p)` of original length `4p−1`, having exactly `R=3p−3` rotation occurrences and `F=p+2` reflection occurrences. Then:

**Core reduction.** If W has no original-order identity subsequence of length2p, one nonzero `a∈F_p` occurs as an actual rotation exponent exactly `2p−1` times. Write the remaining `p−2` rotation exponents as `b_1,...,b_(p−2)` and put `d_i=b_i−a`. Then the d_i form a zero-sum-free sequence: no nonempty subset sums to zero. For EVERY pair of reflections, the number of these `2p−1` core occurrences strictly between the two positions is neither `p−1` nor p.

**Run theorem.** W DOES have an original-order identity subsequence of length2p if it has either

1. a contiguous run of at least FOUR reflections, with arbitrary reflection exponents; or
2. a contiguous run of at least THREE reflections whose exponents are not all equal.

More precisely, if an avoiding W has a run of length at least three, then every reflection in that run has the same exponent and every non-core rotation exponent equals `−a`. The four-reflection conclusion follows constructively from this forced exceptional form. Neither theorem assumes rotations can be moved, or that the reflection run is a subsequence rather than an ACTUAL contiguous run.

## 2. Exact signed-pair input, included for clarity

For any actual chosen pair of reflection positions i<j, replace each raw rotation exponent x by `−x` if the rotation occurs strictly between i and j, and by x otherwise. Let M_ij be the maximum multiplicity of a resulting signed value.

If `M_ij<=2p−2`, then W has a selector using those two reflections and exactly `2p−2` rotations. Indeed the `3p−3` signed values contain `p−1` disjoint unequal pairs; omit one occurrence per pair. Each swap adds a nonzero difference in F_p. A nonempty proper set grows under union with any nonzero translate, so the p−1 independent swaps cover all p values. Choose the omissions to make the actual exponent `sum(retained signed values)+y_i−y_j` vanish.

This is the boundary specialization of `frontier-20261028-dihedral-signed-pair-selector-v1.md`, SHA256 `cc43e48c757c4fdba339a93598090ebaf9c42876c8547204b96ec3026032cac9`; its simple pairing lemma and translation-growth proof are reproduced here, not taken from an unexamined held artifact.

Thus, under the no-selector assumption, EVERY pair has a unique signed majority of at least `2p−1`. A zero majority is impossible: it would give `2p−1` zero rotations, and the `p+2` reflections contain two equal exponents, yielding an actual selector with those two reflections and `2p−2` zero rotations.

Fix one reflection pair and its nonzero signed majority h. At least `2p−1` raw rotations have exponents in `{h,−h}`. The majority classes for any two reflection pairs overlap in at least `2(2p−1)−(3p−3)=p+1` actual rotation occurrences, so every other majority is h or −h.

## 3. From a two-sign core to `2p−1` IDENTICAL rotations

Orient h as a so that m, the number of raw rotations equal to a, is at least p. This is possible because at least `2p−1` rotations are a or −a. Let n be the number equal to −a. If m>=2p, 2p copies of r^a already select identity; if both m,n>=p, p copies of each do. Therefore no selector implies

`p <= m <= 2p−1`, `n <= p−1`.

For any reflection pair i<j define `u_ij = #(a rotations strictly between i,j) − #(−a rotations strictly between i,j)`. Its signed +a multiplicity is `m−u_ij`, and its signed −a multiplicity is `n+u_ij`. Since its majority is one of ±a and has at least `2p−1` occurrences,

`u_ij <= m−(2p−1) <= 0`  OR  `u_ij >= (2p−1)−n >= p`.  (1)

Look at the `F−1=p+1` intervals between CONSECUTIVE actual reflections. Each interval with positive u needs at least p a-rotations by (1); because m<=2p−1, there is at most one such interval. Each negative-u interval contains at least one −a-rotation, so there are at most n<=p−1 such intervals. At least one consecutive interval therefore has u=0.

For that actual pair the signed multiplicities of ±a are m and n. Since n<2p−1 and a signed majority must have at least2p−1 occurrences, `m>=2p−1`. Combined with the opposite bound this proves `m=2p−1`; hence exactly `p−2` other rotations remain.

For any reflection pair, if `c` core rotations lie strictly between them, `p−1<=c<=p` would permit p−1 disjoint pairs each consisting of a core rotation inside and one outside: their signed values are −a and +a, different as p is odd. The same independent-swap argument from §2 would select identity using the pair. Thus the central crossing counts `p−1,p` are forbidden under no-selector.

## 4. Rotation-only selection and a sharp subset-sum lemma

As there are exactly `2p−1` core rotations, every nonempty set S of k extra rotations, `1<=k<=p−2`, can be supplemented by exactly `2p−k` actual core rotations. Their all-rotation exponent is

`sum_(i in S) b_i + (2p−k)a = sum_(i in S) (b_i−a) = sum_(i in S) d_i`.

Therefore a nonempty zero-sum subset of the d_i would give an actual length2p rotation-only selector. Under no-selector the d_i are nonzero and zero-sum-free.

We need this elementary **equality lemma**: if `d_1,...,d_(p−2)` is a zero-sum-free sequence of nonzero elements of F_p and its subset-sum set A misses exactly one residue m, then every `d_i=−m`.

*Proof.* Repeated translation growth gives `|A|>=p−1`. Suppose `|A|=p−1` and `A=F_p\{m}`. Fix i and let B be the subset-sum set of the other p−3 entries. The same growth gives `|B|>=p−2`. If `|B|=p−1` then B=A and `B+d_i⊆A` forces `B+d_i=B`, impossible because d_i is nonzero and B is a proper subset of the prime cyclic group. Hence `|B|=p−2`. Since B and B+d_i both avoid m, B omits exactly `m` and `m−d_i`.

Zero-sum-freeness says `−d_i` is not in B, since otherwise that subset together with d_i sums to zero. Therefore `−d_i=m` or `−d_i=m−d_i`. The latter gives m=0, impossible because 0∈A. Thus `d_i=−m` for every i. QED. This includes p=3, where B is the subset-sum set of the empty sequence.

## 5. Three/four consecutive reflections

Assume no selector and consider an ACTUAL contiguous run H of at least three reflections. For any subset S of the extra rotations, select S and `2p−2−|S|` core rotations. This is possible even when S is empty, since there are `2p−1` cores. All selected rotations lie outside H. Their possible total exponents are exactly

`T = −2a + A`,

where A is the subset-sum set of the zero-sum-free d_i. The original product with a pair i<j in H is identity exactly when `y_j−y_i∈T`. Since `|A|>=p−1`, either T is all F_p (then every pair works), or T misses only one residue w. Under no-selector every directed pair difference in H must equal w. Three ordered reflections give `y_2−y_1=w`, `y_3−y_2=w`, and `y_3−y_1=w`, hence w=0 and every reflection in H has the same exponent.

Because the missing residue of T is 0, the unique missing residue of A is `m=2a`. By the equality lemma every `d_i=−2a`, hence every extra rotation is `b_i=−a`. If H has at least four reflections, take ANY four from H and take `p−2` core rotations plus all `p−2` extra rotations. These are `2p` actual occurrences; the rotation product is identity and the four equal reflections also multiply to identity. Every chosen rotation lies outside H, so the original ordered product is identity. This contradicts the no-selector assumption and proves both parts of §1.

This argument also explains why the 4-reflection branch is necessary: with `2p−1` a's, `p−2` (−a)'s, and an all-equal reflection run, every selector using exactly two reflections from that run has a nonzero rotation exponent, but the displayed four-reflection selector works.

## 6. Exact checks and frontier

`frontier-20261028-dihedral-core-reduction-checker.py`, SHA256 `72e96543d5fb219d49c7466acb3c979545215c982308d80175b62ea150e0eb4e`, reexamined the already saved 480 random and four structured original words in `frontier-20261028-dihedral-signed-pair-results.json`, SHA256 `74e0f7a73f8e029abc782f9aa8626e24100d92e76d38e02107aaecef4d7842e8`. Actual output `frontier-20261028-dihedral-core-reduction-check-results.json`, SHA256 `7c26ac3ea6a80305b2c5a8455feb2379da26dc74db297dc3bdd146ab873af546`, reports 479 signed-pair-eligible words and five actual constant-rotation selectors; **zero sampled words reached the concentrated long-run branch**, so this sample is NOT evidence for that branch.

The same checker independently exhausts the subset-sum lemma's nonzero input sequences for p=3,5,7: respectively 2,64,7776 tuples tested, 2,16,36 zero-sum-free, and 2,4,6 of those with one missing subset sum; every one-missing instance has all entries equal to minus the missing residue. These finite computations do not replace the all-prime proof above.

An independent direct actual-word branch check `frontier-20261028-dihedral-core-run-witness-checker.py`, SHA256 `f37ff3fc9adc8ca689590a1fbda878974d97163e435cdccc306c7ff666c2ec8f`, returned `PASS_EXCEPTIONAL_FOUR_REFLECTION_FAMILY` in `frontier-20261028-dihedral-core-run-witness-check-results.json`, SHA256 `72619df5448f098e4b1b40f77770efc6226f8421dda0c10fb8a2d3e1507fbdf2`. For the actual all-prime family `r^(2p−1) s^(p+2) (r^(-1))^(p−2)` it checked p=3,5,7,11,13; the representative two-reflection supports are exactly the p−1 nonzero exponents, and the displayed four-reflection original-index selectors multiply directly to identity. This is five instances of one family, not an exhaustive check of the run theorem.

The original no-selector residual remains: **exactly 2p−1 equal nonzero rotations, zero-sum-free translated extras, only runs of length at most3, and a length-3 run only in the indicated equal/inverse exceptional form**. Other rotation-count bands and general finite groups remain open. No counterexample to the original theorem, external review, formal/kernel assurance or novelty is claimed.

**END — actual core reduction, run theorem, and precise residual.**
