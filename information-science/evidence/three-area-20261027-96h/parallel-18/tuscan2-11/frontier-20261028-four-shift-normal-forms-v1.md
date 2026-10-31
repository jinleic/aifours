# Every four-row translate intersection in T1(11) has one of three normal forms

Owner **InfoRecursiveMDS18-2**, info-4. Actual native clock before writing: **Wed Oct 28 22:09:29 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** Exact original-target necessary condition for every unrestricted linear T2(11), obtained already at T1. The index-set census was additionally **checked in the owner's Python kernel using integers on all 330 four-subsets**, not on any selected Tuscan array. No native search, solver, heavy campaign, held argument or external source is used. No formal/kernel-proof, independent-model or novelty claim.

**Input:** the definition of T1/T2 and the packing argument of `frontier-20261028-prime-translate-intersection-rigidity-v1.md` (SHA-256 `ac9bea314ad9b2ab178499ce16ed47d63fbfd506a11b2077c7a11a670581493e`). Its needed steps are restated below; no certificate-admission outcome is an input.

## 1. The all-variable bridge

For any T1(11) array A, any 11-cycle g and any permutation row R, label symbols by Z/11Z so g acts as +1. Let I be any four shift indices for which all R+t (t∈I) are actual rows of A. The ten adjacent differences of R cannot all be distinct: if they were, they would be the ten nonzero residues with sum zero, but their telescoping sum is last(R)−first(R)≠0. Choose equal adjacent differences at sources differing by δ≠0. Uniqueness of the corresponding arcs forces

I ∩ (I+δ) = ∅.                                           (1)

In particular I−I is NOT all of Z/11Z. This is necessary for every actual original array; it is not an assumed row-system ansatz.

Conversely, for the index-set classification alone, I−I≠Z/11Z implies (1) for some nonzero δ: choose δ outside I−I. Thus classifying four-subsets with a missing difference is exactly classifying four independent marks on an 11-cycle with some step δ.

## 2. Every admissible four-subset fits in a five-term arithmetic progression

Order the four marks around the δ-cycle. The four positive gaps are at least 2 and sum to 11. Up to permutation their only possibilities are

- 5,2,2,2;
- 4,3,2,2;
- 3,3,3,2.

In the first case insert a mark in gap 5, splitting it into gaps 2 and 3. In the second insert a mark in gap 4, splitting it into gaps 2 and 2. Both give five marks with four gaps 2 and one gap 3, so those five marks form a length-five arithmetic progression with step 2δ.

In the third case rotate the starting point to put the gap 2 first. The four marks are a translate of {0,2δ,5δ,8δ}, which is the four-term progression {2δ,5δ,8δ,0} with step 3δ. Append the next point 3δ to get a five-term progression.

Therefore every four-subset I with I−I proper is contained in some five-term progression. Reparametrize its generator and starting point so that this progression is {0,1,2,3,4}; the four marks omit one position. Translation and reversal of this five-position interval reduce the five possible omitted positions to three representatives:

J_0 = {0,1,2,3},   J_1 = {0,1,2,4},   J_2 = {0,1,3,4}.     (2)

Changing the generator from g to a nonzero power of g does not change its full orbit or any actual row. The extra point used to complete the progression is ONLY an index; the corresponding row is **not asserted to lie in A**.

**Theorem.** For EVERY unrestricted T1(11), and hence for EVERY unrestricted T2(11), any four actual rows lying in one translate orbit under an arbitrary 11-cycle can be written, after reparametrizing that same cyclic action, as R'+t for t in exactly one of the three affine index classes represented by (2). The theorem does not require a fifth row or any symmetry of the whole array.

## 3. Distinctness and complete index census

The complements of the difference sets of (2) are

C_0 = {4,5,6,7} = {±4,±5},   C_1 = C_2 = {5,6} = {±5}.

The affine group of Z/11Z has 110 elements. An affine stabilizer t↦ht+u of J_i induces a multiplier stabilizer of C_i. For C_0 the latter is a subgroup of the ten-element nonzero multiplier group whose order divides |C_0|=4 (its action on nonzero residues is free), hence divides 2. It contains −1, so is exactly {1,−1}. For C_1=C_2 the same conclusion follows immediately from preserving {±5}.

For h=1 the only stabilizing translation is u=0: a nonzero translation generates all eleven residues and cannot fix a four-set. For h=−1, the equality u−J_i=J_i forces 4u=2·sum(J_i), or u=sum(J_i)/2 modulo 11. It gives:

- J_0: u=3, which does stabilize J_0;
- J_1: u=9, which does NOT stabilize J_1 (the image of 0 is 9);
- J_2: u=4, which does stabilize J_2.

Their affine orbit sizes are consequently 55,110,55. J_0 is disjoint from the other classes by difference-set cardinality (7 versus 9); J_1 and J_2 have different stabilizer sizes and so are also inequivalent. Section 2 proves these are all proper-difference four-subsets. Of the binomial(11,4)=330 four-subsets, exactly 220 belong to these three classes, while the remaining 110 have full difference set and **cannot be four actual shift indices** for a T1(11) under the specified cycle action.

These are counts of INDEX SETS, not counts of Tuscan arrays, solution-density estimates, or a claim that one-third of original arrays have been excluded.

## 4. Consequences at both original distances

For an actual T2(11) and any four-row intersection in normal form J_i, fix a nonzero difference e and a distance d∈{1,2}. If e occurs at source symbols s,z in R', then z−s must lie outside J_i−J_i. Thus:

- J_0: any repeated difference has source-symbol offset in {±4,±5};
- J_1 or J_2: any repeated difference has source-symbol offset in {±5}.

At either distance e occurs at most twice: each occurrence supplies four distinct translated events, so three occurrences would require twelve distinct source symbols modulo 11. In the ten adjacent differences there is at least one repetition. In the nine distance-two differences repetition need not occur. Distances remain separate: equal numerical differences across the TWO distances are not prohibited by this argument.

For a FIVE-row translate intersection, the preceding packet gives the sharper exact index set {0,1,2,3,4}; for six or more it gives impossibility. Together these results classify every possible translate intersection of size at least four by **arbitrary** 11-cycles, not merely complete cyclic blocks.

## 5. Complete finite corroboration actually executed

The owner's Python kernel enumerated every tuple in itertools.combinations(range(11),4), formed all differences modulo 11, and compared it to all 11·10 affine images of each representative in (2). All arithmetic was integer. Observed output:

- all four-subsets: 330;
- J_0 affine class: 55;
- J_1 affine class: 110;
- J_2 affine class: 55;
- full-difference class: 110;
- pairwise intersections of the three affine classes: 0,0,0;
- proper-difference four-subsets with no unique class: none.

The check did not construct, test or exclude any selected T2 array. It is finite corroboration of the written index proof, not a standalone solver refutation or an independent review.

## 6. Exact residual

No four-row normal-form configuration is shown completable or impossible. No fifth actual row is silently added. Arbitrary arrays whose every such intersection has size at most three are untouched, and the completions of the three four-index types and five-index type remain open. The unrestricted T2(11) existence/no-go question is **OPEN**. No support-9 or original-solution claim is made.
