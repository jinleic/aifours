# Bounded peer reconstruction — Sun8 prime-seven reduction and generation

Observed before exclusive creation: **2026-10-23T14:18:24-0700 PDT**. Reviewer MathOlson-2, math-2. Assigned by `peer-review-wave-eighteen-v1.json`. This is ordinary in-harness written reconstruction by a different problem owner, not a blind, cross-vendor, human or formal review. Only this named review file is written for the review; author and shared files remain unchanged.

## Snapshot and boundary

Author source: `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md`.

**SHA256 independently observed:** `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`, exactly the assigned pin. Read the complete114-line manuscript, including full raw line104, and the complete36-line `selection-v1.md`, including its full source/trust paragraphs17/21. No different snapshot was substituted.

Read the literal S7 import in `sun7-complete-written-composition-parent-verdict-v1.md`, observed SHA256 `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`. Its theorem is for arbitrary groups, finite-index subgroups and pairwise disjoint LEFT cosets, without covering, normality, bounded-valuation or cofactor restrictions. This review **TRUSTS that named internal written theorem interface**; it does not reconstruct its transitive ledger, formalize it, or turn its historical acceptance into human/priority certification. The final-v17 operative erratum was already read in this reviewer's primary assignment and does not strengthen that interface.

Freshly read Zhu's primary <https://arxiv.org/html/0807.2207v1>, title/abstract, introduction, Theorem1.1 and elementary Lemma2.1 statements: Theorem1.1 gives Sun3/4 for arbitrary-group disjoint LEFT cosets with finite indices. Z3/Z4 are explicit classical theorem imports here, not re-proved in this review.

## Verdict

**No substantive defect found at the stated import/scope boundary. Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The checked result is R8 (relative to S7), the index-seven fibre formulas, G5/five-wise generation, inversion and no-normal-vertex consequences. It does **NOT** prove P7, Sun8, existence/nonexistence of an arithmetic index pattern, or novelty. A parent review remains separate.

## Independent written reconstruction

### 1. Finite core and coprime intersection — lines15–21

The common core N is finite-index normal and contained in every U_i. Consequently all U_i and all intersections contain N; taking full quotient preimages preserves the relevant indices and disjointness. No original-group finiteness hypothesis has been added.

For a=[G:H], b=[G:K] coprime, I=[G:H∩K] is divisible by ab, while the finite product-set formula gives |HK|/|G|=I/(ab)<=1. Thus I=ab and HK=G. The orientation is correct: xh=yk implies x^(-1)y=hk^(-1)∈HK; conversely x^(-1)y=hk gives xh=yk^(-1) in both left cosets. This is valid without HK being a subgroup in advance.

### 2. R8 incidence — lines25–38

In a Sun8 counterexample all pairwise gcds are between2 and7. S7 on every seven-subset forces a gcd7 pair in each. If A is the set of indices divisible7, such pairs are exactly pairs in A, so |A|>=3: a deletion would otherwise leave at most one A-vertex.

If j is outside A, every A-index must share one of2,3,5 with n_j. No such prime can divide two A-indices, since their gcd would then be at least14. Three or more nonempty disjoint supports on the three primes force |A|=3 and the singleton supports2,3,5. In particular n_j contains all three primes, and each A-index contains exactly its assigned one among2,3,5. Every other outside index must therefore contain all three primes too, since its gcd with each A-index exceeds1 but cannot contain7 or a prime greater7. There are five outside indices, so any pair of them has gcd at least30, contradiction. Thus A is all eight vertices. Dividing all indices by7 preserves precisely gcd(r_i,r_j)=1, including the permitted possibility that one r_i contains7. The P7 statement is consequently an exact residual relative to S7, not an ansatz.

### 3. Left-coset fibre formula — lines40–56

For [G:W]=7, the number of W-cosets met by g_iU_i is t_i=[U_i:U_i∩W]<=7: equality of g_i uW and g_i u'W is exactly u'^(-1)u∈U_i∩W. If hW meets g_iU_i at x, their intersection is x(U_i∩W). Translation by h^(-1) therefore gives a LEFT coset in W of the ACTUAL U_i∩W, without an unprovided conjugation. Its index is [W:W∩U_i]=[G:U_i]t_i/7=r_i t_i.

For U_b<=W, t_b=1 and its fibre index is r_b. Two baseline cells cannot coincide because their fibre indices are coprime. If outlier i meets baseline b, coprime-intersection forces gcd(r_b,r_i t_i)=gcd(r_b,t_i)>1. Distinct baseline cofactors have disjoint prime supports, so at most omega(t_i) baseline cells can be met. These are necessary incidence bounds only.

### 4. G5: complete t=3 partition — lines58–76

Five baseline cosets leave exactly two holes among W's seven cells. Each of the other THREE cosets meets t cells but at most omega(t) baseline cells, hence t<=2+omega(t). Direct values for t=4,5,6,7 give right sides3,3,4,3, all too small; only1,2,3 remain. A t=3 outlier must meet both holes and the unique baseline cell whose cofactor contains3; all outlier cofactors are then3-free.

A t=1 outlier has fibre index coprime to3r_i, so it cannot share either hole with a t=3 outlier and has nowhere to lie. A t=2 outlier has gcd(3r_i,2r_j)=1 unless r_i is even. If that gcd is1 it can use neither hole and at most one baseline cell, not its required two cells. Thus coexistence forces the t=3 cofactor even.

This leaves exactly the author's three cases: one3 plus two2 gives one even3-cofactor, no even baseline, both2-outliers in both holes, and in each hole a forbidden Z3 triple with all gcds2; two3 plus one2 forces two coprime cofactors both even; three3 meets the unique baseline3-cell with that baseline, giving four indices all pairwise gcd3 and contradicting Z4. With t=1 already excluded, the partition is exhaustive.

### 5. G5: complete t=1,2 partition — lines78–98

If a baseline cofactor is even it is unique and all outlier cofactors are odd. Each t=1 outlier occupies a hole exclusively against the other outliers. Three1 or two1 plus one2 are impossible by hole/cell counts. One1 plus two2 forces the two2 pieces into the other hole and the baseline2-cell, where baseline plus two outliers contradict Z3. With three2 and no1 there are six required incidences but capacity at most2+2+1=5: each hole permits at most two by Z3; the even-baseline cell permits at most one outlier because it already contains the baseline piece.

If no baseline cofactor is even, every t=2 meets both holes. Three1 cannot share a hole by coprimality. Two1 plus one2 forces both1-cofactors even; one1 plus two2 forces the1-cofactor even and then gives a gcd2 triple in its hole; three2 gives a gcd2 triple in either hole. These exhaust the four possible numbers of t=1 outliers.

For any five subgroup vertices, their generated subgroup V contains each U_i, hence has finite index dividing all five n_i. Their common gcd is7, so [G:V] is1 or7. G5 excludes the latter, proving five-wise generation without a minimal-order or normality assumption.

### 6. Inverted orientation and normal vertex — lines100–104

Inversion is a bijection and (g_iU_i)^(-1)=U_i g_i^(-1)=g_i^(-1)(g_iU_i g_i^(-1)), so the new objects are indeed LEFT cosets of U_i^*. Disjointness and indices survive; applying G5 gives the separately conjugated five-wise generation statement, not a common conjugation.

If U_v is normal, V_j=U_vU_j is a subgroup. Pairwise cofactor coprimality gives lcm(n_v,n_j)=7r_vr_j, so alpha_vj is a positive integer. Product sizes give [G:V_j]=7/alpha_vj. Disjointness forces alpha_vj<7, and integrality/primality force alpha_vj=1. Thus every image of U_j in Q=G/U_v has index7.

The quotient-disjointness bridge is valid: if two image cosets overlap, select a common U_v-cell. Their nonempty fibre pieces there are cosets of U_i∩U_v and U_j∩U_v with indices r_i,r_j in U_v, because alpha_vi=alpha_vj=1. Coprimality forces their intersection in that cell, contradicting original disjointness. The image point of g_vU_v cannot lie in any other image coset for the same full-cell reason. But seven disjoint cosets of index7 in finite Q have total density1 and cover Q, contradiction. This establishes no-normal-vertex; normality is invariant under each stated conjugation.

## What this review does not establish

No common index-seven overgroup for five vertices has been forced. G5 says such an overgroup is impossible IF it contains five; five-wise generation does not imply that the remaining P7 geometry is impossible. The author preserves that gap in lines106–114. No independent execution, finite enumeration, formal/kernel replay, human review or novelty clearance occurred. Returning now to the ONE assigned primary problem, ordered Olson.
