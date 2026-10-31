# RQLS10 v129 — THETA(1,2,2) BB plane-equality case: domino squares, forced line cases, and the direct sum W = A ⊕ D

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:28:51 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

We work in a (b-BLOCK, a-BLOCK) mate of the S103 pattern, with (V2, P5) in case (i), C = B (v124). By v124:
- W(P2) = W(V5) = B^⊥ =: W;
- D ⊂ W and A ⊂ W;
- v2 splits as {Yc', β, Ya'} | {Xc', Yb', β'};
- v5 splits as {Xa', a_{y'}, Xc'} | {Ya', Xb', a_y}.

In a BB mate, every H6 column plane is a block column or a domino of one class pair (v111):
- P has dominoes (v1; β') and (v4; Yb');
- V has dominoes (v1; a_y) and (v3; Xb');
- U has the domino (v5; Xb');
- Q has the domino (v2; Yb');
- N has dominoes (v2; β'), (v3; β), (v4; a_{y'}) and (v5; a_y).

## 1. Lemma DOMINO-SUMS

The following hold.
- **(a)** V's dominoes are orthogonal and sum to A^⊥: Π^{v1}_{a_y} ⊕ Π^{v3}_{Xb'} = A^⊥. This follows from the projection identity P_{A⊕B} + P_W + P_{V-dom} = 2I.
- **(b)** P's dominoes are orthogonal and sum to D^⊥: Π^{v1}_{β'} ⊕ Π^{v4}_{Yb'} = D^⊥ (v124 §1(i)6).
- **(c)** The complementary triples give Π^{v2}_{Yb'} ⊕ Π^{v2}_{β'} = A^⊥ and Π^{v5}_{Xb'} ⊕ Π^{v5}_{a_y} = D^⊥.

## 2. Theorem DOMINO-SQUARES

There are two SQUAREs in the sense of v114:
- **V-square.** F1 = Π^{v1}_{a_y} and F2 = Π^{v3}_{Xb'}, with hat A, against G1 = Π^{v5}_{a_y} (column a_y) and G2 = Π^{v5}_{Xb'} (column Xb'). We have (G1 ⊕ G2)^⊥ = D.
- **P-square.** Π^{v1}_{β'} and Π^{v4}_{Yb'}, with hat D, against Π^{v2}_{β'} (column β') and Π^{v2}_{Yb'} (column Yb'). We have (Π^{v2}_{β'} ⊕ Π^{v2}_{Yb'})^⊥ = A.

Both SQUAREs are in the LINE case.

Proof for the V-square.
1. Suppose G2 = F1. Each V5-block cell is orthogonal to its row-mate U-cell in G2 and, by class, to its V-cell in F1. ORTH2 then gives W ⊥ G2, so G2 ⊂ B.
2. This means Π^{v5}_{Xb'} = B = C = Π^{v5}_{Xc'}, i.e. two column planes at v5 coincide. TWIN rules this out.
3. The case G1 = F2 is the same, using the N-cells at v5.

The P-square is handled in the same way, using the P2-block cells at v2 and TWIN at v2. ∎

## 3. Corollary DIRECT-SUM

In the line case of the V-square, D = (G1 ⊕ G2)^⊥ = span(sin θ g1' − cos θ k1, sin φ f1' − cos φ k2). Here:
- f1' ∈ F1 and g1' ∈ F2;
- k1, k2 ∈ A;
- sin θ and sin φ are nonzero.

Since F1, F2 and A are mutually orthogonal, D ∩ A = 0. Hence W = A ⊕ D, a direct but non-orthogonal sum.

## 4. Frame structure

W carries two Latin 4-frames: the P2 block, with row planes R^P_r and class planes K^P_i, and the V5 block, with R^V_r and K^V_j. The four cells of A and D each lie in an intersection of one frame's row plane with the other frame's class plane:
- d_A ∈ R^P_2 ∩ K^V_2;
- e_A ∈ R^P_1 ∩ K^V_1;
- P1_D ∈ K^P_2 ∩ R^V_{r'};
- P2_D ∈ K^P_1 ∩ R^V_r.

Here r and r' are the v5 rows of the two Ya' cells. Every cell is non-parallel to every other (MAX). TWIN-LINE forces A and D to meet the column planes of both frames trivially.

## 4b. Status

The BB plane-equality case is now reduced to the configuration of §4 together with the line-case domino squares. Its existence or exclusion is OPEN. So are:
- BB line cases;
- the residual line-case system for mates with a SPLIT side (v127/v128);
- the other THETA patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111; v114 SQUARE; v115 TWIN-PLANE/PROPAGATION-style projection identities; v120 TWIN-LINE; v123 ORTH2; v124; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S129. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112 and S114 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 and v67 scope typos;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
