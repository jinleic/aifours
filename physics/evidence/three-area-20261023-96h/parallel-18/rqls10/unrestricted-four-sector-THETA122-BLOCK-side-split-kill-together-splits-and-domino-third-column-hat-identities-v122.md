# RQLS10 v122 — THETA(1,2,2) BLOCK sides: v2/v3 splits with the other b-column as third member are impossible; splits whose third member is a domino column force hat identities

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 01:36:46 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

We use the S103 THETA(1,2,2) pattern with a b-BLOCK mate (v111, v113 notation).
- P has the block (v2; Yc', β), and U has the block (v3; Xc', β').
- P has the domino (v1; β'), U has the domino (v1; β), and N has the dominoes (v2; β') and (v3; β).
- The V block (v2; Xc', Ya'), the Q block (v3; Xa', Yc'), and the dominoes Q(v2, Yb'), Q(v4, Ya'), V(v3, Xb'), V(v5, Xa'), P(v4, Yb') and U(v5, Xb') are forced in every mate.
- By v113 Z-CELL:
  - a v2 split is {Yc', β, z} | rest with Π^{v2}_z = Ĥ(P2);
  - a v3 split is {Xc', β', z'} | rest with Π^{v3}_{z'} = Ĥ(U3).

Notation (A, B, C, D, A', B', C', D') is that of v120.

## 1. Theorem TOGETHER-KILL

No MAX H6 splits at v2 with z = β'. No MAX H6 splits at v3 with z' = β. This holds regardless of what happens at the other row-pairs, so it supersedes v113 BLOCK-TOGETHER and v118 BLOCK-PAIR.

Proof for v2 with z = β'.
1. The complementary triple is {Xc', Ya', Yb'}, so Π^{v2}_{Yb'} = Ĥ(V2).
2. The rest is verbatim v121 §2:
   - TWIN-LINE on Q's dominoes forces case (i), so Π^{v3}_{Xc'} = Ĥ(V2). Here Π^{v3}_{Xc'} is U's block column.
   - DOUBLE-PAIR with the Q-block planes at v3 gives Ĥ(V2) = Ĥ(Q3).
   - Then {Xa', Yc', Xc'} is an orthogonal triple at v3. It separates U's v3-columns Xc' and β', contradicting SQUEEZE.

Proof for v3 with z' = β.
1. The complementary triple is {Xa', Xb', Yc'}, so Π^{v3}_{Xb'} = Ĥ(Q3).
2. TWIN-LINE on V's dominoes forces case (ii'), so Π^{v2}_{Yc'} = Ĥ(Q3). Here Π^{v2}_{Yc'} is P's block column.
3. DOUBLE-PAIR with A and B gives Ĥ(Q3) = Ĥ(V2).
4. Then {Xc', Ya', Yc'} is an orthogonal triple at v2. It separates P's v2-columns Yc' and β, contradicting SQUEEZE.

## 2. Theorem DOMINO-THIRD (hat identities)

**(a) A v2 split with z = Yb' forces:**
- Π^{v1}_{β'} = Ĥ(P2) = Π^{v2}_{Yb'};
- (V2, P5) in case (i);
- Π^{v3}_{Xc'} = Ĥ(V2) = Π^{v2}_{β'};
- Ĥ(U3) = Ĥ(P2).

Proof.
1. **PROPAGATION.** By v113 Z-CELL (3), Π^{v4}_{Yb'} ⊂ W(P2). By v115 PROPAGATION, the domino Π^{v1}_{β'} = Ĥ(P2).
2. **The complementary triple.** The complement is {Xc', Ya', β'}, which gives Π^{v2}_{β'} = Ĥ(V2).
3. **Column β'.** Column β' gives Ĥ(P2) ⊥ Ĥ(V2), so Ĥ(P2) ⊂ A ⊕ B. It also gives Π^{v3}_{β'} = (Ĥ(P2) ⊕ Ĥ(V2))^⊥.
4. **Π^{v3}_{Xc'} lies in Ĥ(V2).**
   - The U block gives Π^{v3}_{Xc'} ⊥ Π^{v3}_{β'}, so Π^{v3}_{Xc'} ⊂ Ĥ(P2) ⊕ Ĥ(V2).
   - Column Xc' gives Π^{v3}_{Xc'} ⊥ A.
   - A vector p + h of Π^{v3}_{Xc'}, with p ∈ Ĥ(P2) and h ∈ Ĥ(V2), therefore has p ∈ B ∩ Π^{v2}_{Yb'}.
   - That intersection is 0 by TWIN-LINE: these are two column planes at v2.
   - So Π^{v3}_{Xc'} = Ĥ(V2).
5. **Case (i) and the U-hat.**
   - Column Xc' gives C = (A ⊕ Ĥ(V2))^⊥ = B, which is case (i).
   - W(U3) = Ĥ(V2) ⊕ (Ĥ(P2) ⊕ Ĥ(V2))^⊥ = Ĥ(P2)^⊥, so Ĥ(U3) = Ĥ(P2).

**(b) Mirror at v3.** A v3 split with z' = Xb' forces:
- Π^{v1}_β = Ĥ(U3) = Π^{v3}_{Xb'};
- (Q3, U4) in case (ii');
- Π^{v2}_{Yc'} = Ĥ(Q3) = Π^{v3}_β;
- Ĥ(P2) = Ĥ(U3).

The proof is the same as (a). It uses:
- PROPAGATION for U with Π^{v5}_{Xb'} ⊂ W(U3);
- column β;
- TWIN-LINE between the column planes Π^{v3}_{Xb'} and A' at v3.

**(c) Corollary.** (a) and (b) cannot hold together. Otherwise Π^{v1}_{β'} = Ĥ(P2) = Ĥ(U3) = Π^{v1}_β, so two column planes at v1 coincide, contradicting TWIN.

**(d) a-BLOCK mirrors.** The same statements hold for the Q block (v4; Ya', a_y), the V block (v5; Xa', a_{y'}) and the N dominoes (v4; a_{y'}) and (v5; a_y), under the v112 relabeling.

## 3. Status

Remaining open b-BLOCK splits:
- v2 with z ∈ {Xc', Ya'};
- v3 with z' ∈ {Xa', Yc'};
- v2 with z = Yb' or v3 with z' = Xb', subject to §2.

Beyond these, the following remain OPEN:
- non-split row-pairs and v1;
- SS mates beyond v121;
- the other THETA class patterns;
- BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v101 SQUEEZE; v104 §2; v111 FORCED-L; v113 Z-CELL; v114 SQUARE; v115 TWIN-PLANE/PROPAGATION; v120 TWIN-LINE; v121 DOUBLE-PAIR/SPLIT-KILL; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S122. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
