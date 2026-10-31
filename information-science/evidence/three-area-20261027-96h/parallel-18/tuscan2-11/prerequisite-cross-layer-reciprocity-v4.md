# Definition-first common-row coupling IV: reciprocal cross-layer concentration bounds, including an endpoint-sharp extreme

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 14:55:05 PDT 2026**.

**NEW author-WRITTEN, unreviewed necessary coupling.** The common array cannot independently realize arbitrary large cross-distance overlaps in both directions between two rows. In particular at order11 a row-pair with overlap8 in one direction has overlap at most2 in the other. No original witness, universal no-go or support bound is claimed.

## 0. Input scope

Same S1/S2 definition-first actual-row release and pre-body ACK as the prior three files. The only problem source remains exact packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37.

This continues `prerequisite-cross-layer-overlap-v3.md`, SHA256 `0cbe329eaf589fe0a4aa8ed7465355676c7eed37c616e45ad741776b9b51279a`. Imports are its directly proved endpoint/overlap facts and elementary actual-row paths and finite incidence counts. No old proof, support/turn/converse theorem, held/ZERO/private method or source expansion. Prior exposure survives, with no clean-cognition/independence claim.

No interpreter, scientific arithmetic, CAS, enumeration, program, selected numeric/control/boundary probe, solver, replay, modelCLI or GO. The cases below classify all path-block possibilities with arbitrary source row, size and cut position; they are written symbolic proof cases, not candidate/state sampling.

## 1. Definitions

For actual linear permutation rows r,s let

`C_rs=|D1(r)∩D2(s)|`,

as in v3. Under the original complete n-row requirements, C has zero diagonal, each column sums to n−2, and at odd n≥5 each off-diagonal entry is at most n−3.

No separate pair-margin realization is assumed: r,s share the same actual symbol set and positions. For the first bound below only their actual permutation orders are needed.

## 2. General reciprocal capacity inequality

### Theorem 1

For ANY two actual linear permutation rows on n≥3 symbols,

`2 C_rs + C_sr ≤ 2(n−1)`,

and, on exchanging rows,

`C_rs + 2 C_sr ≤ 2(n−1)`.

Consequently `3(C_rs+C_sr)≤4(n−1)`.

**Proof.** Call an adjacent edge of r good if its directed pair belongs to D2(s). There are C_rs good edges and `b=n−1−C_rs` other edges.

If BOTH adjacent edges of a consecutive triple of r were good, its three labels would have source positions j,j+2,j+4 in s. Its outer pair therefore could not be a D1(s) pair, whose source positions differ by1. Thus every one of the C_sr outer-pair events must use at least one of the b other adjacent edges.

An adjacent edge of r occurs in at most two consecutive triples, so it can account for at most two such events. Counting incidences yields `C_sr≤2b`, giving the first inequality. The other statements follow by exchanging rows and adding. All steps use legal linear positions; the first/last edge belongs to only one triple, so the bound does not assume an extra wraparound event. ∎

**Optional exact endpoint refinement.** If b_boundary counts the first and last adjacent edges of r that are not good, the same proof gives `C_sr≤2b−b_boundary`. This is a necessary inequality only, with the actual two boundary edges, not freely chosen boundary states.

## 3. Odd-order endpoint refinement at maximum permitted overlap

### Theorem 2

In an original odd-order n≥5 array, if `C_rs=n−3`, then `C_sr≤2`.

**Proof.** Name the arbitrary source row `s=(x1,…,x_n)`, and write n=2m+1. Its D2(s) edges are the odd-position directed path O from x1 to x_n and the even-position directed path E from x2 to x_{n−1}.

Exactly one of these n−2 edges is absent from r's adjacency path. Removing it splits the two paths into exactly THREE nonempty directed path blocks. Every retained edge is an actual adjacency in r, so these three blocks must occur contiguously in r in their indicated internal orders. Row r is their concatenation in some order. Within a block, a two-step event has source-index difference4 and cannot be a D1(s) pair. Hence C_sr arises only at block splices.

**The removed edge lies in E.** Let its two blocks be E1 (the prefix) and E2 (the suffix). The intact odd block O contains both endpoints of s. Global endpoint uniqueness forbids O as the first or last block of r. Thus O is the middle block, with E1/E2 on either side.
- At the splice into O, a crossing two-step event ends at x1 or x3. The one ending at x1 cannot increase the source index; the other can have difference1 only when its initial even index is2. So at most one D1(s) pair comes from that splice.
- At the splice out of O, a crossing two-step event starts at x_{n−2} or x_n. The one starting at x_n cannot increase the index; the other can have difference1 only when its final even index is n−1. So at most one comes from that splice.
- O has m+1≥3 vertices, so no two-step event crosses both splices.

Thus C_sr≤2.

**The removed edge lies in O.** Let O1 be its prefix, starting at x1, and O2 its suffix, ending at x_n. Endpoint uniqueness forbids O1 as the first block and O2 as the last block of r.
- If E lies between them, the order must be `O2 E O1`. Across the first splice the possible outer index pairs end at2 or4 after starting near n; across the second they start near n−1 before ending at1 or3. For n≥5 each difference is negative, never +1. Thus C_sr=0 here.
- Otherwise the two odd blocks are adjacent. Their order must be O2 followed by O1: the opposite order would put O1 first or O2 last. There is exactly one odd/even splice, contributing at most two D1(s) outer pairs. The odd/odd splice contributes none, since its outer labels have the same index parity, unlike a D1(s) pair.
- A triple could cross both splices only if the middle odd block were a singleton. If that singleton were O1={x1}, then the adjacency x1→x2 at its splice into E would repeat a D1(s) pair. If it were O2={x_n}, then E's end x_{n−1}→x_n would do so. Both violate the original distance1 noncollision. Hence no such extra triple occurs.

Again C_sr≤2. These exhaust which parity path loses the edge and whether its split blocks are separated by the intact path. ∎

## 4. Original-size consequences and limitation

For every pair of original eleven-symbol rows:
- `2 C_rs+C_sr≤20` and its reverse inequality;
- `C_rs+C_sr≤13`, by the integer consequence of `3(C_rs+C_sr)≤40`;
- if C_rs=8, then C_sr≤2, improving the general bound in that extreme.

These are simultaneous constraints on cross-layer transport in one common array, not independently assignable certificates for each matrix entry. In particular two high-overlap row embeddings cannot be chosen independently and then glued merely because they meet column sums.

No C-matrix satisfying these inequalities is asserted realizable by rows. The exact original-row converse remains v1 Lemmas1-3, with full relative-position coherence and event constraints. The common-middle form in v2 is another necessary condition; neither it nor these capacities is an existence or nonexistence proof.

**Remaining genuine step:** couple embeddings across THREE or more actual rows instead of only aggregating their overlap counts. An implication from feasible transport counts to actual coherent relative positions is unproved and is NOT used. No original support stratum is selected, no finite search or numerical state is proposed and no old-source permission is inferred.

Author-WRITTEN, unreviewed, no parent adoption or stronger verification/novelty gate. All prior exposure/STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP persist.
