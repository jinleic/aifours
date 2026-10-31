# Two low gaps with bounded total increment in the type-I subclass

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 18:42:44 PDT 2026**. This is a **WRITTEN sufficient-condition candidate**, with bounded checks below, not an independent review, full type-I solution, formal proof or novelty clearance.

## 1. The actual-word theorem

Let p be ANY odd prime and a∈F_p be nonzero. Let W be an actual original-order word of length `4p−1` in `D_(2p)` whose rotations are exactly `2p−1` copies of `r^a` and `p−3` copies of `r^(−a)`. Its other p+3 occurrences are arbitrary reflections. For each actual reflection i define the INTEGER prefix

`Q_i = #(r^a before i) − #(r^(−a) before i)`.

If there exist actual reflection positions `i<j<k<l` for which

`u=Q_j−Q_i`, `v=Q_l−Q_k`, `1<=u,v<=p+1`, and `u+v<=p`,  (1)

then W has an identity subsequence of EXACTLY2p original occurrences, in original order. The two selected pairs are chronologically separated, not merely disjoint as sets.

## 2. Exact low-pair missing target

For i<j with `1<=u<=p+1`, the ACTUAL signed rotation multiset has `2p−1−u` occurrences of +a and `p−3+u` occurrences of −a. Each count is at least p−2. Let T_ij be the sum of all these signed values. When choosing `2p−2` rotations, omitting p−2 actual rotations with q signed −a and p−2−q signed +a, q=0,...,p−2 yields all omission residues except 0. Hence the possible SELECTED signed sums are exactly `F_p\{T_ij}`.

The raw total is `T_0=[(2p−1)−(p−3)]a=2a`, so for this actual pair

`T_ij = T_0−2u a = 2(1−u)a`.  (2)

With actual reflection exponents y_i,y_j the pair succeeds unless `y_j−y_i=T_ij`. The same statement holds for (k,l) and v. This calculation uses the two original gaps, not interchangeable signed copies of their rotations.

## 3. Four-reflection original selector

If either specified pair succeeds by itself, use its two reflections and `2p−2` actual rotations. Otherwise BOTH actual missing-target equalities hold:

`y_j−y_i=2(1−u)a`,  `y_l−y_k=2(1−v)a`.

Select all four actual reflections i,j,k,l. Temporarily sign EVERY original rotation according to the parity of those selected reflections. The signed +a and −a multiplicities are

`P=2p−1−(u+v)`,  `N=p−3+(u+v)`.

Since u,v>=1 and u+v<=p, `P>=p−1` and `N>=p−1>=1`. The signed sum of all rotations together with the four-reflection contribution is

`[2−2(u+v)]a − 2(1−u)a − 2(1−v)a = −2a`.

OMIT any p−1 actual signed +a rotations and one actual signed −a rotation. The omitted signed sum is `(p−2)a=−2a`, so the remaining actual original product has exponent0. Exactly p rotations were omitted from `3p−4`, leaving `2p−4` rotations; together with i,j,k,l, exactly2p distinct original positions remain. Reflection parity is even. This constructs an original-order identity selector, not a shortened-word witness. QED.

## 4. Honest residual and context

Under a hypothetical no-selector in this type-I subclass, every two chronologically separated low pairs must have `u+v>=p+1`; there may instead be zero or one low pair, or low pairs whose intervals all overlap. This theorem does NOT prove that its condition always occurs, nor rule out those residuals.

The separate all-high candidate may cover words for which every signed pair has maximum at least2p−1, but it is NOT an input to this proof or an adopted verdict. The explicit all-prime six-reflection-minimum family also shows that no unrestricted two/four-reflection construction can resolve the entire type-I subclass by itself. No L_RES or original Olson closure follows here.

## 5. Exact bounded checks

`frontier-20261028-dihedral-type1-separated-experiment.py`, SHA256 `c54b74501a920982095d720dad8bd6f24afabb8131ea0c8fc0a7da2358722a8f`, saved actual full-word data in `frontier-20261028-dihedral-type1-separated-results.json`, SHA256 `a655844060d30ab5e8d9b1cb61e5a22179ca7b65bc650152651e464b87c61e33`. It attempted 120 random type-I layouts at each p=3,5,7,11,13. Patterns with no pair satisfying (1) were SKIPPED, not declared solved: 56,8,4,0,0 layouts respectively. Every qualifying layout was also copied with the two specified reflection pairs assigned their exact missing targets, to exercise the genuine four-reflection branch.

Separately written `frontier-20261028-dihedral-type1-separated-checker.py`, SHA256 `100feb5481c089e17c31add011ec3f9bd1ae6b4a7ef045ea6cf0f1bea6271df7`, imported no producer code and returned `PASS_INDEPENDENT_TYPE1_SEPARATED_CHECK`; result `frontier-20261028-dihedral-type1-separated-check-results.json` SHA256 `135df9cd487895f2d8d079648828fb49b7c5bf23063e488e755e69143dfb39ad`. It reconstructed all 1,064 qualifying full original words, their exact prefix increments and separated pair positions; checked the pair-gauge equalities and four-reflection total and omitted-sign counts where applicable; and directly multiplied every submitted distinct-index `2p` selector. Branches were 532 forced-pair-gauge/four, 517 random/two and 15 random/four. Duplicate-index, overlapping-pair and duplicate-omission mutations were rejected for their intended reasons.

These checks do not independently establish the universal written deduction or solve the skipped layouts. No human/cross-family review, formal proof or novelty determination is claimed.

**END — type-I sufficient condition and explicit remaining gap.**
