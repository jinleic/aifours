# Support 47 forces exactly 27 maximal coefficients (self-contained reduction)

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 13:15:40 PDT 2026` (last observation, not an exact completion time). **WRITTEN author candidate**, not reviewed, adopted, formally verified or novelty-cleared. No SAT/LRAT/solver result, no phase computation and no held, withdrawn or quarantined material is used. This packet does not exclude support 47 and makes no global claim.

This is a successor to `frontier-20261029-n47-residual-reduction-v1.md` (SHA-256 `9d727efb08543532eba75fd26dd647033743e74d0f67f2c9ec58face34c35681`), which is not edited. Changes: every unitary-support fact is now proved in §2, rather than cited from f141; the only recorded input is f113; v1's §4 consequences are dropped as not needed for this claim.

## 0. The single recorded input

**f113** — `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-maximal-coefficients29-parent-v1.md`, SHA-256 `86968ac972bf26f1f6cac6936bbccd23b27696487c96a9779be5ef0553723d9b`: *every AME(4,6) state has at most29 coefficients of modulus1/6.* It carries that record's classical no-OLS(6) import and its prior t≤30 boundary. It is used **only** to exclude t≥30.

## 1. Claim and setup

**Claim.** If ψ is a normalized complex AME(4,6) state, written in some product basis, with exactly N=47 nonzero coefficients, then exactly t=27 of them have modulus1/6.

For each of the three2|2 cuts, U=6ψ is a36×36 unitary. Let P be the positions with |U|=1, t=|P|, E the other nonzero positions, n=36−t. An entry of modulus1 exhausts the norm of its row and of its column, so it is the only nonzero entry of both. Hence the t rows (and t columns) through P contain nothing else. All of E lies in the remaining n rows and n columns, and the submatrix V on them is an n×n unitary. A row or column of V with one nonzero entry would have that entry of modulus1, putting it in P; so **every row and column of V has at least two nonzeros**. Thus |E|≥2n and `N=t+|E|≥72−t`.

With N=47: t≥25, and f113 gives t≤29. The row excess `e=|E|−2n=(47−t)−2(36−t)=t−25` is the same in all three cuts.

## 2. Unitary-support facts (V unitary, every line of degree ≥2)

Let G be the bipartite support graph of V (rows and columns as vertices).

- **(F1) Unique overlap.** Two distinct rows sharing exactly one nonzero column have inner product equal to one nonzero product, so they are not orthogonal. The same holds for columns.
- **(F2) Components are square.** If a connected component K has row set R and column set C, the rows of R are |R| orthonormal vectors supported on C, so |R|≤|C|. Symmetrically |C|≤|R|. The component's row excess `r(K)=#entries−2|R|` is at least0.
- **(F3) Excess-zero components.** If every line of K has degree2, K is a cycle r_1c_1r_2c_2…r_mc_m. If m≥3, rows r_1={c_m,c_1} and r_2={c_1,c_2} share exactly c_1, contradicting (F1). So m=2 and K is a full2×2 block.

For a component K with m≥3 rows, let s be its number of degree-2 rows and b the number of rows of degree at least3.

- **(F4) Disjoint pairs.** Two distinct degree-2 rows of K have disjoint column pairs. Sharing one column contradicts (F1). If they share both columns {c,c'}, their2×2 submatrix has orthonormal rows, so it is unitary. Its columns then have unit norm, so columns c,c' of V have no further nonzeros, and these two rows and two columns form a component of size2, not K.
- **(F5) Two higher neighbours.** Let ρ be a degree-2 row of K with pair {c,c'}. Every other row meeting c or c' contains both, by (F1). Column c has degree at least2, so such rows exist, and none has degree2 by (F4). Suppose only one, σ, existed. Then columns c,c' would be orthonormal vectors supported on {ρ,σ}, the2×2 submatrix on {ρ,σ}×{c,c'} would be unitary, and σ's norm would be used up on {c,c'}, giving σ degree2. Contradiction. So at least two rows of degree at least3 contain both c and c'.
- **(F6) Counting.** The s disjoint pairs lie among the m columns, so 2s≤m=s+b, i.e. s≤b. Each higher row contributes at least1 to the excess, so b≤r(K).
- **(F7) Parity of higher rows.** By (F1), a higher row meets the pair of each degree-2 row in0 or2 columns.

**Lemma A.** If e=0 in a cut, every component is a full2×2 block (F3), so n is even.

**Lemma B.** No component has excess1. A component of size m≤2 has at most 2m entries, so excess0. If m≥3, then b≤1 by (F6), so s=m−b≥2>b, contradicting s≤b.

**Lemma C.** Every component of excess2 is a3×3 block with eight nonzeros. Here m≥3, b≤2 and s≤b, so m≤4. If m=4, then s=b=2: the two disjoint pairs cover all four columns, so by (F7) both higher rows have even degree. Yet their excesses sum to2 with each at least1, so both have degree3. Contradiction. Hence m=3, with 2·3+2=8 entries.

**Lemma D.** Every component of excess3 is a full3×3 block. Here b≤3 and s≤b give m≤6.

- m=3: 6+3=9 entries, full.
- m=4, (s,b)=(2,2): the pairs cover all columns, so higher degrees are even, but the excesses (1,2) give degrees3 and4. Contradiction.
- m=4, (s,b)=(1,3): one pair X and columns u,v. All three higher rows have degree3. A higher row avoiding X lies in {u,v}, so it has degree at most2. Hence each is X∪{u} or X∪{v}, giving u and v three incidences in total, while each needs at least two. Contradiction.
- m=5, (s,b)=(2,3): pairs X,Y and a column u. Every higher row has degree3 = one pair plus u, by (F7). Then only3 pair incidences exist, but (F5) needs at least2 for each pair. Contradiction.
- m=6, (s,b)=(3,3): the pairs cover all columns, so higher degrees are even, but all three are3. Contradiction.

**Lemma E.** No7×7 such V has exactly18 nonzeros (total excess4). Component excesses are nonnegative, sum to4 and avoid1 (Lemma B), so they are {4} or {2,2}, plus excess-0 components.

- {2,2}: two eight-entry3×3 blocks (Lemma C) use6 rows. Every other component has excess0, hence is a full2×2 block (F3) with two rows; but one row remains. Contradiction.
- {4}: one component K of excess4, the rest full2×2 blocks (F3). Its size m is odd because7 is odd. A3×3 block has excess at most3, so m∈{5,7}, with s≤b≤4.
  - m=7, (s,b)=(3,4): three disjoint pairs and one other column u. Four higher rows of total excess4, so each has degree3 = one pair plus u (F7). That gives4 pair incidences, but (F5) needs6. Contradiction.
  - m=5, (s,b)=(2,3): pairs X,Y and column u. The higher degrees are3,3,4. Each degree-3 row is one pair plus u. The degree-4 row has even pair contribution, so it is X∪Y. (F5) needs each pair met at least twice, so the two degree-3 rows lie on different pairs. Rows X∪{u} and Y∪{u} then share exactly u, contradicting (F1).
  - m=5, (s,b)=(1,4): pair X and columns u,v,w. Four higher rows, all of degree3. A row avoiding X is exactly {u,v,w}. It shares exactly one column with any row X∪{x}, x∈{u,v,w}, so if it occurred, X would have no higher neighbour, contradicting (F5). So all four rows have the form X∪{x}, giving u,v,w four incidences in total, while each needs at least two. Contradiction.

## 3. The case split

| t | n | e | conclusion |
|---:|---:|---:|---|
| ≤24 | | | impossible: N≥72−t |
| 25 | 11 | 0 | Lemma A: n would be even. Impossible. |
| 26 | 10 | 1 | component excesses are nonnegative and sum to1, so one equals1: Lemma B. Impossible. |
| 27 | 9 | 2 | not excluded here |
| 28 | 8 | 3 | excesses sum to3 with none equal to1, so one excess-3 component, a full3×3 block (Lemma D), plus2×2 blocks: n=3+even is odd. Impossible. |
| 29 | 7 | 4 | Lemma E. Impossible. |
| ≥30 | | | f113. Impossible. |

Hence t=27. ∎

## 4. Scope

Only f113 is imported, with its stated boundaries. §2 is elementary linear algebra on one unitary at a time; the excess is the same in all three cuts because |E| and n do not depend on the cut. The downstream t=27 exclusion is the separately frozen heavy-core packet; no combination into an N=47 or global statement is made here.
