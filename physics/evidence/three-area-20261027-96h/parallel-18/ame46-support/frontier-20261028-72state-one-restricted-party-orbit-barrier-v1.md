# A 72-support barrier with one H/K-preserving party for the 72-term family

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:21:18 PDT 2026`; not an exact completion clock. **WRITTEN author candidate** with exact finite source checks; independent scientific review is required before adoption. This is not a global AME lower bound, an unrestricted four-factor orbit theorem, a formal proof, or a novelty claim.

## 1. Claim and scope

Use the H/K bases and four-color relabelings of `frontier-20261028-unrestricted-orbit-60-barrier-v1.md`, SHA-256 `d21c734fa2830bf20e7330e118f03d3e1367f1794815c82162075c7df6dac251`. Let E be the 48 signed Pauli-sector coefficients from [Pandya Table 1](https://arxiv.org/html/2610.16673#S2.T1), P the 12 even-color-permutation positions there, and P′ the 12 odd-color-permutation positions listed in [Eq. (6)](https://arxiv.org/html/2610.16673#S4.E6). Consider any tensor supported on exactly `E∪P∪P′` whose E coefficients are those of Table 1, all 24 P/P′ coefficients are nonzero, and whose six all-K 2×2 blocks in **each** 2|2 flattening are invertible. Its source support is 72.

Choose any party C and apply any `GL(2,C)⊕GL(4,C)` map on its H/K decomposition; the other three parties may use arbitrary `GL(6,C)` maps. Then the resulting tensor has at least 72 nonzero coefficients. Identity attains 72, so this restricted local-invertible orbit has exact minimum 72. The statement is algebraic and does not require the tensor itself to be AME; when it is AME, the block-preserving-unitary subcase is a physical family of output states.

This applies, in the displayed gauge, to the paper's nonendpoint `|δ|<1` states of [Eq. (3)](https://arxiv.org/html/2610.16673#S4.E3) satisfying the mixed-block phase congruences: all P/P′ entries are nonzero and those blocks are unitary up to the common factor, hence invertible. Local diagonal gauge changes can be absorbed into the arbitrary GL factors. In particular, the explicit tensor with E coefficients `±1`, P coefficients `1`, P′ coefficients `i`, and common normalization `1/√72` is an AME state with support 72.

A hypothetical support reduction below 72 by a fully arbitrary LU applied to such a state would therefore require the image of H to be non-coordinate at **every** party: if one image were coordinate, a support-preserving output permutation would make that unitary block diagonal. This is a necessary condition only. We do not prove a 72 lower bound for the full unrestricted four-factor orbit or a 60 lower bound for all AME states.

## 2. Source checks and the six 2×2 blocks

In each 2|2 cut, E has equal spectator K colors and its four active 2×2 H matrices are signed `I,X,Z,J=ZX`, one each. The 24 P/P′ positions have four distinct colors. For each unordered pair `{g,h}` of input K colors, the other two colors are `{a,b}` and the corresponding P/P′ positions form a full 2×2 block from ordered inputs `(g,h),(h,g)` to ordered outputs `(a,b),(b,a)`. Every one of the four entries is nonzero, and the statement assumes this block is invertible. The six unordered input pairs partition all 12 ordered unequal-color pairs.

`frontier-20261028-72state-block-isometry-v1.py`, SHA-256 `00a9c65d8be91f8f0ee8013eb97f12a9276995eb7af31a160101ec6dad15bf07`, checks all 18 such support blocks in the three cuts, and directly checks all `3·36²=3888` complex-integer Gram entries for the explicit E/P/P′ coefficients `±1,1,i`: each unnormalized flattening F has `F F†=2I`. Receipt `frontier-20261028-72state-block-isometry-v1.json`, SHA-256 `af5a829b5bf2711f7c0198383f910a3d7f7a35a41198c6d34f6e25a79cb4bce2`. It rejects a deleted P term at the support-count gate. Source table SHA-256 `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`; P′ is separately transcribed from the linked public equation. This source check of the special state does not by itself verify arbitrary parameter phases; for the general claim invertibility and nonzero coefficients are stated hypotheses.

## 3. Pure-H C covectors

Fix C and any distinct B; let A,D be the others. Contract with nonzero covectors and write the result as a 6×6 A-by-D matrix in H/K blocks. If the C covector `λ` is pure H, the matrix is `[[0,X],[Y,Z]]`. Both P and P′ vanish from this contraction.

For `u_K≠0`, the Pauli E matching gives nonzero X and Y, and a 2×2 minor across the zero upper-left block has determinant `−XY≠0`. For `u_K=0`, the nonzero `u_H` gives a 4×4 matching matrix Z whose entries are the four overlaps `u_H^T Q_g λ`. At least two are nonzero: otherwise λ would be a common eigenvector of two distinct anticommuting nonidentity Pauli matrices. Thus every pure-H contraction has rank at least 2, for every nonzero B covector.

## 4. Pure-K C covectors

Let the nonzero pure-K C covector be `t`, and write B's covector as `u=(u_H,u_K)`. As before,

`M(t,u)=[[F(t,u_K),X(t,u_H)],[Y(t,u_H),Z(t,u_K)]]`.            (1)

If `u_H≠0`, take a color g with `t_g≠0`. The Pauli E matching makes D-K column g of X and A-K row g of Y nonzero. Since P and P′ use four distinct colors, the **whole** entry `Z_{g,g}` is zero. A minor `[[F_ij,X],[Y,0]]` has nonzero determinant `−XY`, regardless of F. Hence rank is at least 2.

Now suppose `u_H=0`; then `u_K≠0` and (1) is block diagonal. Its H-by-H block is `F=Σ_g t_g u_g Q_g`. The four Q_g are linearly independent, so `F=0` forces `t_g u_g=0` for all g, i.e. t and u_K have disjoint color supports.

- If F and Z are both nonzero, the block-diagonal matrix has rank at least 2.
- If F=0, pick g in `supp(t)` and h in `supp(u_K)`; they are distinct. The reversed input product `t_h u_g` vanishes. The source block for the unordered pair `{g,h}` has **both** coefficients in the selected input column nonzero, so the two entries `Z_{a,b}` and `Z_{b,a}` for the complementary colors a,b are nonzero. The diagonal entries `Z_{a,a}, Z_{b,b}` vanish, yielding a nonzero 2×2 minor and `rank Z≥2`.
- If Z=0, invertibility of each of the six source 2×2 blocks implies that *all* nonmatching input products `t_g u_h` with `g≠h` vanish. Since t,u_K are both nonzero, their supports must each be the same singleton g. Then F is a nonzero scalar multiple of Q_g, hence `rank F=2`.

These cases show `rank M(t,u)≥2` for all nonzero pure-K t and nonzero u. Notice that the proof uses nonzero individual source block entries in the F=0 case, and full block invertibility in the Z=0 case; neither condition is silently inferred from support alone.

## 5. Support count

When the chosen local map on C preserves H/K, each of its six output-coordinate covectors is nonzero and pure H or pure K. The six B output-coordinate covectors are also nonzero. Sections 3–4 give rank at least 2 for each of the `6·6=36` A,D contraction matrices. Arbitrary invertible A,D maps preserve each matrix rank; a matrix of rank 2 has at least two nonzero entries. Since the 36 C,B output slices are disjoint, total support is at least `36·2=72`. Identity has support 72.

## 6. Unrestricted-orbit diagnostic, not a theorem

For the explicit δ=0, E/P/P′=`±1/1/i` state, a separate finite-field search used F_5 with `i=2`. For all 12 ordered choices C,B it exhausted all `3906²=15,256,836` nonzero projective covector pairs, `183,082,032` pairs total, and found no rank-at-most-one contraction. Search code `frontier-20261028-72state-rank-search-f5-v1.cpp`, SHA-256 `2c47157d813166638300bb0d050d31e7abe304ca374f3b45825a8167818f1fb0`; aggregate of its 12 receipts `frontier-20261028-72state-rank-search-aggregate-v1.json`, SHA-256 `cff522cb4cc795f7d92be0730d9a65a53e8679bed67f74df391d554332017e45`. Hashes in the aggregate were observed at aggregation, not execution-time attestations. Predicate checks include 10,000 rank-one positive controls, a zero positive, and 20,000 comparisons with separate modular Gaussian elimination; code SHA-256 `0af5a685febfaf39b14b3a4c5c31bd8483f3f00be7958daa9b8d2e18486c9472`, receipt SHA-256 `ba4c751c2b3bf193f18eeaed83ac9932f8cc70ec2f0c0dbfb6e2f7959ec6bf6d`.

The F_5 result does **not** imply the absence of complex rank-one contractions: solutions may exist only over an extension or in characteristic zero. Thus the suggested fully unrestricted ≥72 result remains an exact gap, not an accepted conclusion. The original unrestricted global AME(4,6) support minimum also remains open here.
