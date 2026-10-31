# Support 47: a sharpened common-pair projection bound leaves two residual-alphabet profiles

Owner **PhysicsAME46-2**. Native clock before writing: `Thu Oct 29 09:25:14 PDT 2026`; not an exact completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified, or novelty-cleared. This additive packet sharpens §4 of `frontier-20261029-n47-residual-reduction-v1.md`, SHA-256 `9d727efb08543532eba75fd26dd647033743e74d0f67f2c9ec58face34c35681`; it does not edit that packet. Its N=47→(t,n,|E|)=(27,9,20) reduction remains a stated unreviewed prerequisite. The argument below is a general pair-partition identity and simple counting; no no-OLS theorem is used directly.

## 1. A general degree identity stronger than the fiber-incidence bound

For a normalized AME(4,6) state let P be all t modulus-1/6 positions, E all other nonzero positions, and `n=36−t`. In every coordinate-pair system, the maximal entries are isolated singleton rows; the other n pair values carry E and no P. This is a partition of all36 pair values because the flattening is unitary and has no zero rows.

For a local E symbol a at party i, let `m_i(a)=|{x∈P:x_i=a}|`. For ANY other party j, the P words with i-value a have distinct j values, since no two P words share a coordinate pair. All other j values are E-carried pairs. Therefore

`d_i(a):=|π_j(E_a)|=6−m_i(a)`                                     (D)

is **independent of j**. If d_i(a)=1, every coordinate j≠i would be constant on E_a, so E_a would have at most one word; that would be a singleton pair row and hence maximal, contrary to a∈π_i(E). Thus `d_i(a)≥2` and

`Σ_{a∈π_i(E)} d_i(a)=n`, so `|π_i(E)|≤floor(n/2)`.              (B)

This applies whether E-pair multiplicities are two, three, or larger. It is stronger than `2r≤3(n−r)` in several low-n cases because it uses the common P/E partition across **all three** pair systems involving i.

## 2. Only (3,4,4,4) and (4,4,4,4) at (t,n,|E|)=(27,9,20)

Assume the reduction prerequisite: N=47 gives t=27,n=9,|E|=20. Bound (B) makes every residual alphabet size at most4. Every pair projection has9 values, so an alphabet of size≤2 cannot occur: its product with a size≤4 alphabet is at most8. Thus all four alphabets have size3 or4.

Call a coordinate of a P word active if it lies in the corresponding E alphabet. If the sizes are r_i, the common partition gives `6r_i−9` P words active at i and `r_i r_j−9` active at both i,j. Therefore

`Σ_{x∈P}[k(x)−C(k(x),2)]=6Σ_i r_i−Σ_{i<j}r_i r_j+18≤27`,        (A)

since the per-word quantity is at most1. Equivalently `6Σr_i−Σ_{i<j}r_i r_j≤9`.

Among the five profiles with sizes3/4, the left side is respectively

- (3,3,3,3):18;
- (3,3,3,4):15;
- (3,3,4,4):11;
- (3,4,4,4):6;
- (4,4,4,4):0.

The first three are impossible by (A). Only **(3,4,4,4)** and **(4,4,4,4)** remain. This shrinks the earlier twelve-profile list to two; it does not decide either profile.

## 3. Heavy pair values have a cut-independent local degree

The residual support in each cut is one eight-entry 3×3 block plus three full2×2 blocks. Hence every one of the six pair systems has exactly two heavy pair values with multiplicity3, and seven others with multiplicity2.

For a residual symbol a of party i and another party j, let h_ij(a) be the number of heavy (i,j) values using a. Counting E words in the fiber gives

`|E_a|=2 d_i(a)+h_ij(a)`.

By (D), both |E_a| and d_i(a) are independent of j, so **h_ij(a) is also independent of j**, not merely congruent modulo2. Write it h_i(a). Its sum over a is2. Every party is therefore exactly one of:

- **split:** two distinct residual symbols each have h_i=1; these are exactly the two odd-sized E fibers;
- **merged:** one distinguished symbol has h_i=2 in every pair system involving i; all fibers are even.

There can be at most **one merged party**. If two parties i,j were merged, both distinct heavy (i,j) pair values would have to equal the same pair of their distinguished symbols, impossible. Thus at least three parties are split.

For a size-4 party, (D) gives degree multiset `(2,2,2,3)`. In profile (3,4,4,4), the size-3 party has degrees `(2,3,4)` or `(3,3,3)`, since its degrees sum to9 and each is at most its size-4 partners' alphabet size.

The two possible split fiber-size multisets at a size-4 party are `(4,4,5,7)` and `(4,5,5,6)` depending on whether the unique degree-3 symbol is distinguished. Merged fiber sizes are `(4,4,4,8)` or `(4,4,6,6)`.

These constraints are load-bearing candidates for the next common-six-marginal step, not exclusions or tensor witnesses. No claim is made about the feasibility of either remaining residual profile.
