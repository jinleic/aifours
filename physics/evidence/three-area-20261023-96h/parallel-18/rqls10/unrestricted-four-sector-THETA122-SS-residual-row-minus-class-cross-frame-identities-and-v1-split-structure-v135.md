# RQLS10 v135 — THETA(1,2,2) S103, SS residual: four row-minus-class cross-frame identities, the v1-split structure, and documented blocked approaches

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 03:27:35 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written operator identities from the v103 §5 incidences. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This is the SS residual (v132–v134) in the v103 §5 orientation. We write [x] for the rank-one projection onto a cell x. The cells used are:
- **Singles at v2..v5:**
  - P: p21 = P2(v2.1, b2), p22 = P1(v2.2, b1);
  - U: u31 = U1(v3.1, b1), u32 = U2(v3.2, b2);
  - Q: q41 = Q2(v4.1, a1), q42 = Q1(v4.2, a2);
  - V: v51 = V1(v5.1, a1), v52 = V2(v5.2, a2);
  - N: n21 = N1(v2.1, b1), n22 = N2(v2.2, b2), n31 = N1(v3.1, b2), n32 = N2(v3.2, b1), n41 = N2(v4.1, a2), n42 = N1(v4.2, a1), n51 = N1(v5.1, a2), n52 = N2(v5.2, a1).
- **Cells at v1:**
  - p11 = P2(v1.1, b1), p12 = P1(v1.2, b2);
  - u11 = U1(v1.1, b2), u12 = U2(v1.2, b1);
  - q11 = Q1(v1.1, a1), q12 = Q2(v1.2, a2);
  - v11 = V1(v1.1, a2), v12 = V2(v1.2, a1).

## 1. Theorem CROSS-FRAME IDENTITIES

Every MAX H6 of an SS mate satisfies the following four identities, linking the (V2, P5) planes A, B, C, D to the (Q3, U4) planes A', B', C', D'.
- **(RQ)** row v2 − class Q: P_A + 2P_B + P_D + [p21] + [p22] + [n21] + [n22] = P_{A'} + 2P_{B'} + P_{D'} + [q41] + [q42] + [q11] + [q12].
- **(RU)** row v5 − class U: P_A + 2P_C + P_D + [v51] + [v52] + [n51] + [n52] = P_{A'} + 2P_{C'} + P_{D'} + [u31] + [u32] + [u11] + [u12].
- **(RV)** row v3 − class V: 2P_A + P_B + P_C + [v51] + [v52] + [v11] + [v12] = 2P_{A'} + P_{B'} + P_{C'} + [u31] + [u32] + [n31] + [n32].
- **(RP)** row v4 − class P: P_B + P_C + 2P_D + [p21] + [p22] + [p11] + [p12] = P_{B'} + P_{C'} + 2P_{D'} + [q41] + [q42] + [n41] + [n42].

Proof for (RQ).
1. Row v2 is V2 + Π^2_{Yc'} + [p21] + [p22] + Π^2_{Yb'} + [n21] + [n22] = 2I.
2. Class Q is Q3 + Π^4_{Ya'} + [q41] + [q42] + Π^2_{Yb'} + [q11] + [q12] = 2I.
3. Subtracting cancels the shared Q-domino Π^2_{Yb'}.
4. Substitute column Yc' (Π^2_{Yc'} = I − P_{B'} − P_{D'}) and column Ya' (Π^4_{Ya'} = I − P_B − P_D).

The others follow the same pattern; in each, the row and the class share one domino, which cancels:
- **(RU)** shares the U-domino (v5; Xb'). It uses columns Xa' (V-domino at v5) and Xc' (U-domino at v3).
- **(RV)** shares the V-domino (v3; Xb'). It uses columns Xc' and Xa'.
- **(RP)** shares the P-domino (v4; Yb'). It uses columns Ya' and Yc'.

Each identity has trace 12 on both sides. ∎

## 2. Lemma v1-SPLIT STRUCTURE

Suppose v1 splits; by SQUEEZE the split is T = {Xb', Yb', x} with Π^1_x = Ĥ(N1) (v113 Z-CELL). For x = b1 the following hold; the other three x are the same after relabeling.
- **(i)** Π^2_{b1} ⊕ Π^3_{b1} = W(N1), so {n21, p22, u31, n32} is an orthonormal basis of W(N1).
- **(ii)** n21 ∈ K^N_2 and n32 ∈ K^N_1, each with both block components nonzero. Hence span(p22, u31) = (K^N_1 ⊖ n32) ⊕ (K^N_2 ⊖ n21).
- **(iii)** Lemma U6 (v100 §3) applies at v1. Put U = R^N_1 ⊕ span(p11), where R^N_r is the N-block row plane. Then:
  - U^⊥ = R^N_2 ⊕ span(u12);
  - u11, q11, v11 ∈ U^⊥ and p12, v12, q12 ∈ U;
  - P_U commutes with Π^1_{b2}, Π^1_{a1} and Π^1_{a2}, and has trace one against each.
- **(iv)** The remaining six squeezer singles have frame operator P_{W(N1)} + [n21] + [n32] (from v133 §1 and (i)).

Proof.
- (i) is column b1 with Π^1_{b1} = Ĥ(N1).
- (ii) is class orthogonality to the N block, together with MAX against N's block cells.
- (iii) is U6 for the orthogonal triples T and T'.
- (iv) subtracts [p22] + [u31] from 2P_{W(N1)}. ∎

## 3. Documented blocked approaches (no claim)

- **SS positivity.** In the BLOCK case, BALANCE produced 2P_W on one side (v132 §1). In SS, every row-minus-class identity carries rank-one singles on both sides; see §1 and the v133 §1 computation. Evaluating at a0, b0, a0', b0' gives only inequalities, and these are compatible with the orthogonality bounds (e.g. P_{A'} + 2P_{B'} + P_{D'} ≤ 2 on a unit vector). So no contradiction follows from positivity alone.
- **BARBELL v99 L.** Every row-pair except Z carries N-singles, and Z carries A/B-singles. The row-minus-class chains therefore close into column identities with no positivity content.
- **BARBELL completions of the v98 frame.** The per-row branching (e.g. two of {N2, A3, A4} occupy {Ba, Bb} in row r1.1) leaves many completions. A forced-structure classification analogous to v111 was not completed.

## 4. Status

The SS residual has exact necessary conditions (v127, v128, v133, v134 and §1–§2). Its existence or exclusion is OPEN, with v1 split or not. So are:
- the other THETA(1,2,2) class patterns;
- BARBELL H6;
- C5 three-label patterns;
- dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v100 §3 U6; v103 §5; v113 Z-CELL; v132 §1 technique; v133; v134; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S135. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112, S114 and S130 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54, v67 and v76 scope typos;
- the v77 stray-space and characterization typos;
- the v78 checkpoint typo;
- the v80 stray space;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
