# RQLS10 v113 — THETA(1,2,2) BLOCK side-types: the z-cell split-plane lemma, and a no-go when both side columns stay together

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:21:04 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

We use the S103 THETA(1,2,2) class pattern with a Latin mate of v111 BLOCK type on the b-side. Write β = b_x and β' = b_{x'}.
- The P class sits in the 2×2 block (v2; Yc', β).
- The U class sits in the block (v3; Xc', β').
- P occupies the domino (v1; β'), with P1 at v1.2 and P2 at v1.1.
- U occupies the domino (v1; β).
- N occupies the dominoes (v2; β') and (v3; β).

For a 2×2 class-pair block with classes σ1, σ2 we use:
- W, the span of the block's four cells;
- K_σ, the span of σ's two cells in the block;
- Ĥ = W^⊥, as in v107.

## 1. Lemma Z-CELL (any squeezing class-pair block)

Suppose the class pair (σ1, σ2) squeezes row-pair v and occupies a block (v; m, m'') there. Then:

1. Any orthogonal triple split at v has the form {m, m'', z} with Π^v_z = Ĥ. This is the v107 TRIPLE argument.
2. σ1's cell in column z equals α d_{m2} + β e_{m1} with α·β ≠ 0 (v101 §4). Both cells d_{m2} and e_{m1} belong to σ2, since σ2 occupies the other diagonal. Hence σ1's z-cell lies in K_{σ2} with both block components nonzero, and symmetrically σ2's z-cell lies in K_{σ1}.
3. When the two z-cells sit at one row-pair R, their column plane satisfies Π^R_z ⊂ W and Π^R_z = (Π^R_z ∩ K_{σ1}) ⊕ (Π^R_z ∩ K_{σ2}).

For P at v2 in b-BLOCK, the pair (z, R) is one of (β', v1), (Yb', v4), (Xc', v5) or (Ya', v5).

## 2. Theorem BLOCK-TOGETHER

In every b-BLOCK mate, no MAX H6 has orthogonal triple splits at v1, v2 and v3 in which b1 and b2 lie in a common triple at all three row-pairs. Concretely, this excludes simultaneous splits of the following form:
- v1 = {Xb', Yb', x} with x ∈ {a1, a2};
- v2 = {Yc', β, β'};
- v3 = {Xc', β', β}.

The same holds on the a-side for a-BLOCK, under the v112 relabeling.

Proof.
1. **Plane Latin array.** Columns β and β' sum to I over v1, v2 and v3. Together with the third columns a_o, Yc' and Xc', they form a plane Latin array, so v100 PLS3 applies.
2. **The P1 form.** By §1, P1(v1.2, β') = α·P2(v2, β) + β·P2(v2, Yc'), with both coefficients nonzero.
3. **Classical case.** This cell lies in one decomposition member but has nonzero parts in two distinct members, which is impossible.
4. **K33 case.** Write Π^{v2}_β = (p1, q1) and Π^{v2}_{Yc'} = (p3, q3). By the v107 Fact, up to the x/y mirror:
   - Π^{v1}_{β'} = (p1, q3);
   - P2(v2, β) = x_{p1} and P2(v2, Yc') = y_{q3};
   - hence P1(v2, β) = y_{q1} and P1(v2, Yc') = x_{p3}.
5. **The P2 form gives the contradiction.** P2(v1.1, β') = α'·y_{q1} + β'·x_{p3} with α'·β' ≠ 0. This cell lies in Π^{v1}_{β'} = x_{p1} ⊕ y_{q3}, which is orthogonal to both y_{q1} and x_{p3}. Hence the cell would be zero, a contradiction.

In the BLOCK case the two P-forms land in ONE column plane at v1, which is why they collide. In the SPLIT case of v112 they landed in two different columns.

## 3. Consequence and remaining BLOCK frontier

Combining v112 with §2 settles part of the BLOCK frontier.
- **Mixed side-types.** If one side is SPLIT, every all-five-split H6 is excluded whenever v1's third column x lies on the opposite side. That case is covered by the v112 argument for the SPLIT side.
- **Remaining all-five-split cases.** For a BLOCK side, the open all-five-split cases are exactly those in which the side columns separate at the squeezed row-pairs:
  - b-side: z ≠ β' at v2, or z' ≠ β at v3;
  - a-side: the mirror conditions.
- **Non-triple H6.** Non-triple H6 structures remain open in every side-type.

H6 existence for THETA(1,2,2) is OPEN, as are BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v112 relabeling; v107 BLOCK4/TRIPLE/Fact; v101 §4 forced form; v100 PLS3. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S113. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110 and S112 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
