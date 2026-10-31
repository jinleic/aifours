# Definition-first common-row coupling III: no single other row can absorb all distance-two events of a row at odd order

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 14:51:13 PDT 2026**.

**NEW author-WRITTEN, unreviewed necessary original-row coupling.** At the original order11, every row's nine directed distance-two events must occur as adjacent events in at least TWO other rows; no other row can contain more than eight of them. The proof uses the global exact distance-one coverage, not just pairwise event compatibility. This is not a Tuscan-2(11) witness, full obstruction, support bound or novelty claim.

## 0. Scope and inputs

Same narrow S1 definition-first actual-row release and pre-body exposure ACK as `prerequisite-derivation-v1.md` (SHA256 `5c7e2c40f979b41c30608da7d75de7039ae458bfce949a50bc259f3d7a6b0b76`). Only the current S1/S2 packet is a problem source: SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37. No old completed-turn/converse, support, type8, author/reviewer or held/ZERO source is input. Prior authorship/exposure is not certified absent or clean.

**Imports:** elementary finite counts, bijections and directed paths on actual row positions. The proof is entirely below. Symbol parity here means only the parity of a position in ONE arbitrary actual row, not a symbol-class, cyclic family or WLOG restriction of the array.

No interpreter, calculator, arithmetic Eval, CAS, enumeration, program, selected numeric/control/boundary probe, solver, replay, modelCLI or GO. The sharpness statement is a universal symbolic family for every permitted n and split index, not a tested instance or a claim to extend that pair into a full array.

## 1. Original arrays and cross-layer incidence

Let n be odd, n≥5, and let n actual linear permutation rows over the same n-symbol set satisfy the original distance1 exact coverage and distance2 noncollision conditions. This includes the original n=11 with every support value left free.

Write D1(r) for the n−1 directed adjacent pairs of row r and D2(s) for the n−2 directed distance-two pairs of row s. Define

`C_rs := |D1(r) ∩ D2(s)|`.

The distances are not identified: an ordered pair appearing once at each distance is allowed. C records precisely this permitted cross-distance reuse. It does not assume Latin columns, regular missing pairs or an old turn representation.

### Lemma 1 — exact endpoint and transport facts

1. Every symbol starts exactly one row and ends exactly one row.
2. C_ss=0.
3. For every row s, `Σ_r C_rs=n−2`.

**Proof.** Each symbol occurs n times and has n−1 outgoing adjacencies, so it is last once; incoming adjacency counts make it first once. Within one actual row the same ordered pair cannot be both adjacent and distance-two, since its first symbol has one position. Finally every D2(s) event is a distinct ordered pair and hence has exactly one distance1 occurrence somewhere in the array; it is not in s. ∎

The third fact assigns each actual triple's outer pair to a unique DIFFERENT actual row. It is a common-array transport condition, not independently chosen pair margins.

## 2. Saturation obstruction

### Theorem 2

For every pair of distinct rows r,s in such an odd-order array,

`C_rs ≤ n−3`.

**Proof.** Suppose C_rs=n−2, so row r contains every D2(s) pair as a directed adjacency. Name the completely arbitrary order of row s as

`s=(x1,x2,…,x_n)`.

Its distance-two pairs form exactly TWO vertex-disjoint directed paths, partitioning all symbols:
- the odd-position path `O=(x1,x3,…,x_n)`;
- the even-position path `E=(x2,x4,…,x_{n−1})`.

If r contains all their directed edges as adjacent events, each entire path must occur as a contiguous block in r in its indicated order: every internal vertex already has its immediate successor fixed, and no symbol repeats. The two blocks partition all n symbols, so r is exactly O followed by E, or E followed by O. There is no room for a third block, an extra symbol or a separate relabelling.

Because n is odd, O contains BOTH endpoints of s. If r=O E, then r and s both start with x1. If r=E O, they both end with x_n. Both contradict Lemma1. Since C_rs cannot exceed n−2, it is at most n−3. ∎

### Original-size corollary

At n=11, `C_rs≤8` for every r≠s, while each column of C sums to9 and has zero diagonal. Thus every row's nine actual distance-two events must be supplied as adjacency events by at least two distinct other rows.

This forbids a concrete family of global gluing proposals: assigning all outer pairs of the triples of one row to the adjacency path of a single other row cannot extend to the original array, even if the two rows themselves have no same-distance collision.

**Why this is a genuinely global coupling.** The endpoint uniqueness used in the proof comes from all n(n−1) distance1 events forming ONE exact array. Two locally collision-free rows do not satisfy that global uniqueness merely because each is Hamilton. Hence a pairwise compatibility formulation that omits endpoint ownership misses this obstruction.

## 3. Exact pair-level sharpness; no stronger bound is inferred from two-row data alone

The bound n−3 is sharp among pairs that are themselves collision-free at the same distances and have distinct starting and ending symbols. This is not an original n-row construction or extension theorem.

Let n=2m+1≥5, let x1,…,x_n be arbitrary distinct symbols, and let ANY split index k satisfy `1≤k≤m−1`. Set

`s=(x1,x2,…,x_n)`,

`r=(x2,x4,…,x_{2k}, x1,x3,…,x_n, x_{2k+2},x_{2k+4},…,x_{2m})`.

These are actual Hamilton rows on the same symbols. The three blocks are a nonempty initial even-position block, the whole odd-position block, and a nonempty final even-position block.

**Cross-layer overlap.** Relative to D2(s), r keeps all odd-path edges and all even-path edges except the single edge `x_{2k}→x_{2k+2}`. The two new block-splice edges change index parity and cannot be D2(s) events. Thus C_rs=n−3.

**No common D1 events.** Within a block, the source index increases by2, whereas a D1(s) event increases it by1. Both splice edges strictly decrease the source index, so they are not D1(s) events either.

**No common D2 events.** Within a block, a two-step event increases the source index by4 rather than2. Every two-step event crossing exactly one block splice has endpoints of different index parity, so cannot lie in D2(s). The odd block has m+1≥3 vertices, so no two-step event crosses both splices. This exhausts every legal linear distance-two position, including single-vertex even blocks at the permitted extreme split indices.

**Distinct endpoints.** r begins with x2 and ends with x_{2m}=x_{n−1}, whereas s begins with x1 and ends with x_n. Their endpoint ownership does not already fail.

This is a universal proof for every size, symbol order and permitted split index, with no finite instance selected or evaluated. It shows that a putative improvement below n−3 needs a genuinely larger common-array constraint, not just the stated two-row conditions.

## 4. Exact caller, remaining gap and continuation

Theorem2 is a NECESSARY condition for all original arrays, proved directly from their actual rows. It is not advertised as a sufficient representation, and no converse from a matrix C to actual rows is asserted. The full original-row equivalence in v1 still requires coherent relative position maps and both event tests; the common-middle Laplacian in v2 is another necessary invariant, not an adopted existence criterion.

**Useful failed implication identified:** a collision-free pair with every D2 event of one row embedded into the other row's adjacency path cannot be promoted to a complete odd-order Tuscan array. The exact failure is repeated global endpoint ownership. Conversely the sharpness family warns against replacing this conclusion by an unsupported stronger two-row obstruction.

**Open:** no argument yet decides whether the original eleven rows can jointly realize all C columns with the common-middle identity and full triangle consistency. No original row array or universal contradiction is supplied; no support-specific theorem or old result is used.

**Next admitted step:** exploit simultaneous, not independently chosen, cross-layer embeddings across three or more actual rows. A mere C-matrix satisfying the displayed capacities has no common-realization converse. Seek an exact additional common-row implication or state the first unsupported step, without a selected numeric instance or old-source expansion.

All STOP/HOLD/ZERO and process qualifications, prior exposure, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist. Same-harness written only, unreviewed; no parent adoption, kernel/formal, executable, human, configured-family, priority or novelty gate.
