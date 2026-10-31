# Support 47: reduction to t=27 and one eight-entry 3×3 residual block per cut

Owner **PhysicsAME46-2**. Native clock observed immediately before writing: `Thu Oct 29 08:33:44 PDT 2026`; not an exact completion time. **WRITTEN author candidate**; not independently reviewed or adopted. It does not exclude support 47. No held, quarantined, f161, f162 or v203 material was opened or used.

## 1. Claim and inputs

Let ψ be a normalized complex AME(4,6) state, written in some product basis, with exactly `N=47` nonzero coefficients. Let t count its coefficients of modulus 1/6, P be those positions, E the others, and `n=36−t`.

**Claim.** Then `t=27`, `n=9` and `|E|=20`. In each of the three 2|2 cuts, after permuting rows and columns, the residual 9×9 unitary is the direct sum of one 3×3 block with **exactly eight** nonzero entries and three full 2×2 blocks.

The claim uses two recorded inputs:

- [f113](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-maximal-coefficients29-parent-v1.md), SHA-256 `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`, for `t≤29`. It carries that record's no-OLS(6) import and its prior t≤30 boundary.
- The unitary-support lemmas reconstructed for all n in [f141](../../../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-n46-unitary-bridge-t27-t29-parent-v1.md), SHA-256 `b1d3face7eb8a06faec59031e62971c3054dbd99b9426087d73d882af3f30e40`, for excess 0, 1, 2 and 3. These depend on no classical theorem.

The excess-four statement at n=7 (§3) is new and proved here in full.

## 2. Residual and case split

In every cut, `U=6ψ` is unitary. Modulus-1/6 entries are singleton rows and columns; removing them leaves an n×n unitary V supported on E with every row and column of degree at least two. Hence `N≥72−t`, so `t≥25`; also `t≤29` by f113. The row-degree excess of V is

`e=|E|−2n=(47−t)−2(36−t)=t−25`,

identical in the three cuts.

| t | n | e | outcome |
|---|---:|---:|---|
| 25 | 11 | 0 | Every row and column has degree 2 and every component is a full 2×2 block, so n would be even: impossible. |
| 26 | 10 | 1 | The one-excess lemma excludes it. |
| 27 | 9 | 2 | Two-excess classification: one eight-entry 3×3 block plus full 2×2 blocks, and n is odd. Allowed. |
| 28 | 8 | 3 | Three-excess classification: one full 3×3 block plus full 2×2 blocks, so n would be odd: impossible. |
| 29 | 7 | 4 | Excluded by §3. |

## 3. No 7×7 unitary with every line of degree ≥2 has exactly 18 nonzeros

We use these facts about a unitary V whose rows and columns all have degree at least two:

1. Two rows (or two columns) cannot share exactly one nonzero position.
2. Every connected component of the bipartite support graph is square, being a unitary block.
3. A component of excess 0 is a full 2×2 block.
4. No component has excess 1.
5. A component of excess 2 is an eight-entry 3×3 block.

Facts 3–5 are the recorded f141 lemmas applied to the component's own unitary block.

In a connected component of size m≥3 with row excess r, let s be the number of degree-2 rows and b the number of rows of higher degree. Two further facts hold:

- **Disjoint pairs.** Degree-2 rows have pairwise disjoint column pairs. Equal pairs would span C² and force every other row of the component to vanish there, so the two rows would form a separate component.
- **Two higher neighbours.** Each such pair is met by at least two higher rows, each meeting both of its columns. A row meeting just one column would have a unique overlap with the degree-2 row. With a single higher neighbour, the two columns would form a 2×2 unitary and exhaust that neighbour's norm.

The pairs give `2s≤m=s+b`, so `s≤b`, and each higher row contributes at least one to the excess, so `b≤r`.

Suppose V is 7×7 with 18 nonzeros, so its total excess is 4. Components of excess 1 do not exist, so the possible decompositions are:

- **Two excess-2 components and nothing else.** These are two eight-entry 3×3 blocks on 6 rows. The remaining row would be a 1×1 component, i.e. a singleton row, which is impossible.
- **One connected component of excess 4 plus 2×2 blocks.** Its size m is odd, since n=7 is odd and the other components have size 2. A 3×3 block has at most 9 entries, so excess at most 3; hence m∈{5,7}, with m=s+b and `s≤b≤4`.

The remaining cases are:

- **m=7, (s,b)=(3,4).** The three disjoint pairs leave one unpaired column u. The four higher rows carry total excess 4, so each has degree 3. Each meets every pair in 0 or 2 columns, so each is one pair plus u. That gives only 4 pair incidences, but the three pairs need at least 6. Impossible.
- **m=5, (s,b)=(2,3).** The two pairs leave one unpaired column u. The higher degrees are 3, 3, 4: each degree-3 row is one pair plus u, and the degree-4 row is both pairs. The pairs need 4 incidences, which forces the two degree-3 rows onto different pairs. They then share exactly the column u, a unique overlap. Impossible.
- **m=5, (s,b)=(1,4).** One pair X, three unpaired columns, and four degree-3 rows. A row containing all three unpaired columns would share exactly one column with any row of the form X plus one unpaired column. X needs at least two higher neighbours, so all four higher rows have that form. Then the three unpaired columns receive only 4 incidences in total, but each needs degree at least 2. Impossible.

No case remains. This excludes t=29, completing the claim.

## 4. Consequences for the remaining case, recorded for the next step

For `t=27`, in each cut the eight-entry 3×3 block has row degrees (2,3,3) and column degrees (2,3,3). The full 2×2 blocks have degree 2.

**(H) Heavy values.** In each of the six coordinate-pair systems, exactly 9 values are carried by E: two "heavy" values with three E extensions and seven values with two. The other 27 values are each carried by exactly one P word.

**(Par) Parity.** For a residual symbol a of party i and any other party j, `|E_a|=2d_j(a)+h_j(a)`, where `d_j(a)=|π_j(E_a)|` and `h_j(a)` is the number of heavy (i,j)-values with i-component a. Thus `h_j(a)≡|E_a| mod 2` for every j≠i. Since `Σ_a h_j(a)=2`, each party is of one of two types:

- **split:** two symbols with odd fibers, each carrying exactly one heavy value in every pair system containing i;
- **merged:** all fibers are even, and in each pair system the two heavy values share their i-symbol.

**(Count) Maximal-word activity.** Exactly `6r_i−9` P words are active at i, and exactly `r_i r_j−9` at both i and j. By the bound `k−C(k,2)≤1`, the residual-alphabet profile must satisfy `6Σr_i−Σ_{i<j}r_i r_j≤9`. This excludes `(3,3,3,3)`, `(3,3,3,4)`, `(3,3,3,5)` and `(3,3,4,4)`. Every fiber has at least four E words and every pair product is at least 9, so twelve profiles remain:

`(2,5,5,5), (3,3,4,5), (3,3,5,5), (3,4,4,4), (3,4,4,5), (3,4,5,5), (3,5,5,5), (4,4,4,4), (4,4,4,5), (4,4,5,5), (4,5,5,5), (5,5,5,5)`.

These are necessary conditions only. No exclusion of the t=27 case, and no support-47 state, is claimed.
