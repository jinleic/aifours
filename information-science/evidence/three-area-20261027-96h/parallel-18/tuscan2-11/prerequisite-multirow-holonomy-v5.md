# Definition-first common-row coupling V: a three-row defect count is insufficient at order11; exact block signs give a genuine triangle condition

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 14:58:49 PDT 2026**.

**NEW author-WRITTEN, unreviewed.** This records both an exact limitation of a proposed multirow counting argument and an actual three-row consistency condition. Neither is an original Tuscan-2(11) solution. No support stratum, numeric state or control is selected.

## 0. Inputs and notation

Only the current S1/S2 definition packet (SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37), the prospective release/pre-body ACK and elementary permutation signs/path counts are inputs.

Own input-clean predecessors: v1 (`prerequisite-derivation-v1.md`, `5c7e2c40f979b41c30608da7d75de7039ae458bfce949a50bc259f3d7a6b0b76`), v3 (`prerequisite-cross-layer-overlap-v3.md`, `0cbe329eaf589fe0a4aa8ed7465355676c7eed37c616e45ad741776b9b51279a`) and v4 (`prerequisite-cross-layer-reciprocity-v4.md`, `94ec05b2ac521136ac08c633513afe5ee9143f957669d2767b15c346f5b5036c`). No old candidate, sign/Latin/turn theorem, review, private method or held/ZERO source is used. Ordinary signs of position permutations are proved/used here, not an old Latin-square sign identity.

As before, `C_rs=|D1(r)∩D2(s)|` and `F_rs` maps a position in actual row r to the position of its symbol in s. Actual common rows satisfy `F_tr F_st F_rs=id`. Products act rightmost first.

No scientific execution, interpreter/calculator/Eval arithmetic/CAS, enumeration, selected numeric/control/boundary probe, solver, replay, modelCLI or GO. The symbolic case split covers every position of the single missing parity edge; no particular row family is assumed WLOG for the original target.

## 1. A valid multirow defect inequality that does NOT help at order11

For three actual rows r,s,t, put

`a=n−1−C_rs`, `b=n−1−C_st`, `c=n−1−C_tr`.

### Lemma 1

`n−1 ≤ a+2b+4c`, equivalently `C_rs+2C_st+4C_tr≤6(n−1)`.

**Proof.** Start with any of r's n−1 directed adjacent events. If it is not D2(s), charge it to one of the a defective r-edges.

Otherwise it is a two-step path of s. If either s-edge is not D2(t), charge to that defective s-edge. Each such edge occurs in at most two two-step paths of s, and distinct r-events have distinct endpoints and hence distinct s-paths, so at most2b events are charged here.

If both s-edges are D2(t), the three symbols have t-positions j,j+2,j+4, giving a four-step path of t. If any of its four t-edges is not D2(r), charge to that edge. Each defective t-edge belongs to at most four length-four t-paths; the r-events again have distinct endpoints, so at most4c events are charged here.

If all four t-edges were D2(r), the endpoints of the original r-adjacency would have r-position difference8, not1, impossible. The entire composition is on actual positions of the SAME labels, with no wraparound. Every r-event has therefore been charged. ∎

**Exact failure at the original size.** By v3, all three C-entries at n=11 are at most8. Hence the left side of the rearranged inequality is at most `7·8=56`, already below its right side `6·10=60`. It follows for EVERY allowed triple of overlap values, not a tested extremal instance. Thus this inequality, and its cyclic rotations, cannot exclude ANY transport triple already satisfying the one-entry bound at order11.

This is not a source gap or an original counterexample. It is a mathematically explicit failure of the attempted defect-count route: controlling only the NUMBER of defective edges loses their shared locations and cannot establish the desired gluing obstruction. No stronger conclusion is smuggled in from this inequality.

## 2. Exact signs of maximal cross-layer embeddings

Let n=2m+1 with m odd and n≥7 (the original n=11 is included). Suppose `C_rs=n−3`. By v4's proof, row r is the concatenation of the three directed blocks obtained by deleting exactly one edge of one of the source row s's two parity paths.

Write `s=(x1,…,x_n)`. Put

`ε=(-1)^{m(m+1)/2}`.

This is the sign of the position list O E, where `O=(x1,x3,…,x_n)` and `E=(x2,x4,…,x_{n−1})`: each odd-indexed element x_{2j+1} has exactly j inversions with the even block, totaling `0+1+…+m=m(m+1)/2`.

### Lemma 2 — block-sign classification

For every such pair r,s,

`sgn(F_rs)=ε·(-1)^{e_rs}`,

where e_rs=1 exactly in the following case: the removed edge is in O, its prefix block O1 has odd length k, and the two odd blocks occur adjacent in r in the order O2 O1. In every other permitted case e_rs=0.

**Proof.** The sign of the relative-position permutation is the sign of the list of s-indices in r. Swapping two contiguous blocks of lengths u,v changes sign by `(-1)^{uv}`.

- **The cut is in E**, with prefix length k and suffix length m−k. Endpoint ownership requires the intact O block to be in the middle (v4).
  - For order E1 O E2, the sign relative to O E is `(-1)^{k(m+1)}=1`, since m+1 is even.
  - For order E2 O E1, the exponent is `(m−k)(m+1+k)`. Its parity is `(1−k)k=0` because m is odd and consecutive integers have even product. So the sign is again ε.
- **The cut is in O**, with prefix length k and suffix length m+1−k. Endpoint ownership permits only the separated order O2 E O1 or the adjacent odd-block orders O2 O1 E and E O2 O1 (v4).
  - For separated order O2 E O1, moving O1 to the end changes sign by `(-1)^{k(n−k)}=1`, since n is odd and k(n−k) is even. The sign is ε.
  - Swapping O1 and O2 changes sign by `(-1)^{k(m+1−k)}=(-1)^k`, since m+1 is even. Moving E across the whole odd block has exponent m(m+1), also even. Hence both adjacent odd-block orders have sign ε·(-1)^k.

This proves the classification for every source order, cut and permitted block order. Extra same-distance constraints may discard a block order, but cannot change its sign; no existence for any classified pair inside a complete array is inferred. ∎

## 3. A genuine three-row condition

### Theorem 3

Suppose three actual rows form a directed cycle of maximal overlaps:

`C_rs=C_st=C_tr=n−3`.

Then

`(-1)^{e_rs+e_st+e_tr}=ε`.

**Proof.** Full common-row holonomy gives `F_tr F_st F_rs=id`, so the product of the three signs is+1. Lemma2 gives that product as `ε³(-1)^{e_rs+e_st+e_tr}`. Since ε²=1, the asserted equation follows. ∎

**At the ORIGINAL order11:** m=5 gives ε=−1. Thus a directed triangle of overlap8 embeddings must have an ODD number of the exceptional positive-sign block types. In particular three nonexceptional types CANNOT form such a triangle. Their pairwise local realizations or overlap capacities would not certify gluing into actual rows.

More generally, on any directed cycle of maximal-overlap embeddings the sum of the exceptional indicators has the parity forced by the cycle length and ε. Equivalently the signs must be a coboundary of the actual row position-permutation signs, not arbitrary independent edge choices. This is a necessary multirow condition, not a converse.

This matters where §1's scalar defect inequality is entirely redundant at n=11: preserving the actual block-position signs detects incompatible triangles that the scalar capacities cannot distinguish.

## 4. Boundary of this result

These theorems apply to arbitrary actual arrays at the original size, conditionally on the stated overlaps. They do NOT assume that every array has a maximal-overlap triangle, and no argument establishing such a triangle has been supplied. Low-overlap or differently typed transport graphs remain unexcluded. In particular this does not select a purported WLOG family of original arrays or promote a restricted impossibility to a universal one.

**Exact remaining step:** either derive a coupling applicable also without maximal overlap (retaining the genuine common row-position maps), or obtain a valid all-array argument forcing a forbidden configuration. The implication from the displayed scalar transport constraints to either property is unproved and is NOT used.

No original witness/no-go, support restriction or novelty claim. The literal-definition actual-row equivalence remains v1; neither capacities, common-middle positivity nor sign consistency alone realizes the original rows. No newly proposed source is opened and no old source/method STOP is lifted.

All old findings, prior exposure, HOLD/ZERO, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Written only, unreviewed, same harness; no parent adoption or stronger verification/priority gate.
