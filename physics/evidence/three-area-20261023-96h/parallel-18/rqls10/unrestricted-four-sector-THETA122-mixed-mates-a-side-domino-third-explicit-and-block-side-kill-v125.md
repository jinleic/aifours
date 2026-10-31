# RQLS10 v125 — THETA(1,2,2) mixed mates: the a-side DOMINO-THIRD made explicit, and in mixed mates every TOGETHER/DOMINO-THIRD split on the BLOCK side is impossible

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:04:06 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This manuscript treats the S103 THETA(1,2,2) pattern. In an a-BLOCK side (v111):
- Q occupies the block (v4; Ya', a_y) and V the block (v5; Xa', a_{y'});
- Q has dominoes (v1; a_{y'}) and (v2; Yb'), and V has dominoes (v1; a_y) and (v3; Xb');
- N has dominoes (v4; a_{y'}) and (v5; a_y).

Z-CELL (v113) applies to the squeezers Q at v4 and V at v5. The notation follows v120.

## 1. Theorem a-DOMINO-THIRD (explicit)

**(a) A v5 split with third column z = Xb' forces (V2, P5) into case (i).**
1. **PROPAGATION.** Z-CELL gives Π^{v5}_{Xb'} = Ĥ(V5). Z-CELL (3) gives Π^{v3}_{Xb'} ⊂ W(V5). PROPAGATION for V (blocks W(V5), W(V2); dominoes (v3; Xb') and (v1; a_y)) then gives Π^{v1}_{a_y} = Ĥ(V5).
2. **The P-block triple.** The complementary triple {Xc', Ya', a_y} contains both P5-block columns, so Π^{v5}_{a_y} = Ĥ(P5).
3. **Column a_y.** Column a_y gives:
   - Ĥ(V5) ⊥ Ĥ(P5), so Ĥ(V5) ⊂ C ⊕ D;
   - Π^{v4}_{a_y} = (Ĥ(V5) ⊕ Ĥ(P5))^⊥.
4. **Π^{v4}_{Ya'} lies in Ĥ(P5).**
   - The Q4 block gives Π^{v4}_{Ya'} ⊥ Π^{v4}_{a_y}, so Π^{v4}_{Ya'} ⊂ Ĥ(V5) ⊕ Ĥ(P5).
   - Column Ya' gives Π^{v4}_{Ya'} ⊥ D. So a vector v + p of Π^{v4}_{Ya'} (v ∈ Ĥ(V5), p ∈ Ĥ(P5)) has v ∈ C ∩ Π^{v5}_{Xb'}.
   - That intersection is 0, by TWIN-LINE on column planes at v5.
   - Hence Π^{v4}_{Ya'} = Ĥ(P5).
5. **Case (i).** Column Ya' then gives B = (Ĥ(P5) ⊕ D)^⊥ = C.

**(b) A v4 split with z = Yb' forces (Q3, U4) into case (ii').** The argument mirrors (a):
- Z-CELL and PROPAGATION for Q give Π^{v1}_{a_{y'}} = Ĥ(Q4);
- the U-block triple gives Π^{v4}_{a_{y'}} = Ĥ(U4);
- column a_{y'} gives Π^{v5}_{a_{y'}} = (Ĥ(Q4) ⊕ Ĥ(U4))^⊥;
- the V5 block and column Xa' give Π^{v5}_{Xa'} = Ĥ(U4), using TWIN-LINE at v4 for Π^{v4}_{Yb'} ∩ D' = 0;
- column Xa' then gives A' = D'.

This makes explicit the mirror claimed in v122 §2(d). The b-side statements of v122 §2(a)/(b) give case (i) at v2 and case (ii') at v3.

## 2. Theorem MIXED-BLOCK-KILL

Consider a mixed mate, i.e. one side SPLIT and the other BLOCK. Then, on the BLOCK side, no MAX H6 has:
- a TOGETHER split (v122 §1 and its mirror; these are excluded in every mate);
- a DOMINO-THIRD split, i.e. one of:
  - z = Yb' at v2 or z' = Xb' at v3 for b-BLOCK;
  - z = Yb' at v4 or z' = Xb' at v5 for a-BLOCK.

Proof. Every DOMINO-THIRD split forces a SQUARE plane-equality case: by v122 §2 on the b-side, and by §1 above on the a-side. In a mate with a SPLIT side, v123 SQUARE-LINE excludes all plane-equality cases. ∎

## 3. Consequences

In mixed mates:
- the SPLIT side never splits at its squeezed row-pairs (v121), and both SQUAREs are in line cases (v123);
- on the BLOCK side, the only possible splits at its squeezed row-pairs have SEPARATED third columns. These are z ∈ {Xc', Ya'} at v2 and z' ∈ {Xa', Yc'} at v3, or z ∈ {Xa', Yc'} at v4 and z' ∈ {Xc', Ya'} at v5.

## 4. Status

The following remain OPEN:
- the separated BLOCK-side splits and line cases in mixed mates;
- SS line cases with v1;
- BB line and equality cases (v124);
- the other THETA patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111; v113 Z-CELL; v114 SQUARE; v115 PROPAGATION/TWIN-PLANE; v120 TWIN-LINE; v122; v123 SQUARE-LINE; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S125. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
