# RQLS10 v130 — THETA(1,2,2) S103: DOMINO-THIRD-KILL in every mate, the SQUARE-governed split dichotomy, and a frontier ledger

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:33:28 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Inputs and notation

S103 pattern, ANY Latin mate (v111). SQUARE (V2, P5): A = Π^{v2}_{Xc'}, B = Π^{v2}_{Ya'}, C = Π^{v5}_{Xc'}, D = Π^{v5}_{Ya'}. SQUARE (Q3, U4): A' = Π^{v3}_{Xa'}, B' = Π^{v3}_{Yc'}, C' = Π^{v4}_{Xa'}, D' = Π^{v4}_{Yc'}. Cases (v114/v124): (i) C = B, (ii) D = A, (iii) line; (i') C' = B', (ii') D' = A', (iii') line. (V2, P5) GOVERNS v2 and v5; (Q3, U4) GOVERNS v3 and v4.

**TWIN at one row-pair.** If two column planes Π^v_k = Π^v_{k'} (k ≠ k') coincide, then (v.1,k) ⊥ (v.1,k') (row) and (v.1,k) ⊥ (v.2,k) (column) inside one plane, so (v.2,k) ∥ (v.1,k'): a repeat. MAX forbids it.

## 1. Lemma HAT-EQUALITY (any mate; steps 1–2 of v124 only use one BLOCK side)

- b-BLOCK, case (i): Ĥ(P2) = B. Case (ii): Ĥ(P2) = A.
- b-BLOCK, case (i'): Ĥ(U3) = B'. Case (ii'): Ĥ(U3) = A'.
- a-BLOCK, case (i): Ĥ(V5) = C. Case (ii): Ĥ(V5) = D.
- a-BLOCK, case (i'): Ĥ(Q4) = C'. Case (ii'): Ĥ(Q4) = D'.

Proof (b-BLOCK, (ii)). Each P2-block cell at v2 is ⊥ its row-mate V-cell in A (V block column Xc') and, by class, ⊥ its own-class P-cell in D = A (P5 block column Ya', present in every mate). These two cells are distinct, hence non-parallel (MAX), and span A. So W(P2) ⊥ A and, by dimension, Ĥ(P2) = A. The other seven items are the same argument: the squeezer block's cells meet the equal plane once by row (through the other block at that row-pair) and once by class (through the class's forced block at the partner row-pair). ∎

## 2. Theorem DOMINO-THIRD-KILL (every mate)

No MAX H6 has a DOMINO-THIRD split. That is, on a b-BLOCK side: no split at v2 with z = Yb', none at v3 with z' = Xb'. On an a-BLOCK side: no split at v4 with z = Yb', none at v5 with z = Xb'.

Proof.
- **v2, z = Yb'.** Z-CELL (v113 (1)) gives Π^{v2}_{Yb'} = Ĥ(P2), and v122 §2(a) gives case (i). By §1, Ĥ(P2) = B = Π^{v2}_{Ya'}. So Π^{v2}_{Yb'} = Π^{v2}_{Ya'}: TWIN at v2.
- **v3, z' = Xb'.** Π^{v3}_{Xb'} = Ĥ(U3), and v122 §2(b) gives case (ii'). By §1, Ĥ(U3) = A' = Π^{v3}_{Xa'}: TWIN at v3.
- **v5, z = Xb'.** Π^{v5}_{Xb'} = Ĥ(V5), and v125 §1(a) gives case (i). By §1, Ĥ(V5) = C = Π^{v5}_{Xc'}: TWIN at v5.
- **v4, z = Yb'.** Π^{v4}_{Yb'} = Ĥ(Q4), and v125 §1(b) gives case (ii'). By §1, Ĥ(Q4) = D' = Π^{v4}_{Yc'}: TWIN at v4. ∎

This extends v125 MIXED-BLOCK-KILL from mixed mates to BB mates. The hat identities of v122 §2 and v125 §1 remain valid implications, but their hypotheses are now unsatisfiable.

## 3. Theorem SPLIT-DICHOTOMY (every mate)

For each SQUARE:
- **(a) Line case ⇒ no governed split.** If (V2, P5) is in case (iii), neither v2 nor v5 splits. If (Q3, U4) is in case (iii'), neither v3 nor v4 splits.
- **(b) Equality case ⇒ BB and both governed splits.** If (V2, P5) is in case (i) or (ii), the mate is (b-BLOCK, a-BLOCK), and v2 and v5 BOTH split with the separated third columns of v124: (i) z = Ya' at v2, z = Xc' at v5; (ii) z = Xc' at v2, z = Ya' at v5. Mirror statements hold for (Q3, U4) at v3/v4.
- **(c) Exclusivity.** In a BB mate, (i) and (ii) cannot both hold, since §1 would give B = Ĥ(P2) = A (TWIN at v2). Likewise (i') and (ii').

Proof of (a). Take a governed row-pair v.
- If v lies on a SPLIT side (v2, v3 for b-SPLIT; v4, v5 for a-SPLIT), it never splits (v121).
- If v lies on a BLOCK side, SQUEEZE leaves four third columns. TOGETHER is killed in every mate (v122 §1 and its mirror). DOMINO-THIRD is killed by §2. The two SEPARATED columns are killed by v126 §1, which uses exactly the governing SQUARE (S = P2, O = V2, O* = P5 at v2; S = V5, O = P5, O* = V2 at v5; S = U3, O = Q3, O* = U4 at v3; S = Q4, O = U4, O* = Q3 at v4) in its line case.

Proof of (b). In mates with a SPLIT side, both SQUAREs are in line cases (v123). In BB mates, v124 gives the two forced splits. ∎

**Corollary.** In every MAX H6: v2 splits ⇔ v5 splits ⇔ (V2, P5) is in an equality case; and v3 splits ⇔ v4 splits ⇔ (Q3, U4) is in an equality case. In mates with a SPLIT side, v2..v5 never split (re-deriving v126 §2).

## 4. Supersession and vacuity ledger (selected entries, not exhaustive; prospective; no pinned file is edited)

- v112 SS-ALL-TRIPLE, v118 B/A-PAIR, v119 V1-TOGETHER/AT-MOST-TWO: true, superseded in strength by v121/v126.
- v113 BLOCK-TOGETHER, v118 BLOCK-PAIR, v115 §3 SUBCASE-EXCLUSION: superseded by v122 TOGETHER-KILL (their hypotheses include a TOGETHER split).
- v116 §2 and v117 (SS with v2..v5 all split): hypotheses unsatisfiable by v121.
- v122 §2 and v125 §1 DOMINO-THIRD hat identities: hypotheses unsatisfiable by §2.
- v125 MIXED-BLOCK-KILL: subsumed by §2–§3.
- LIVE tools: v101 SQUEEZE, v107 BLOCK4, v111 FORCED-L, v113 Z-CELL, v114 SQUARE, v115 TWIN-PLANE/PROPAGATION, v120 TWIN-LINE, v121 DOUBLE-PAIR, v123 ORTH2, v126 §1 SEPARATED-KILL, §1 HAT-EQUALITY.

## 5. Consolidated S103 frontier

Every MAX H6 of the S103 pattern (any mate) is in exactly one of two residual classes:
- **(L)** Both SQUAREs in line cases; v2..v5 non-split; v1 split or not. Any mate type. Normal forms: v127 (line geometry; b-SPLIT squeezer normals at v2) and v128 (SS mates: P-squeezer at v2 coupled with V-squeezer at v5). OPEN.
- **(E)** BB mate with at least one SQUARE in an equality case, its two governed row-pairs split as in §3(b), the v124 hat coincidences, and for (V2, P5) case (i) the v129 structure (domino squares in line cases, W = A ⊕ D). OPEN.

Both are OPEN, as are the other THETA patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v101; v111; v113 Z-CELL; v114 SQUARE; v121; v122; v123; v124; v125; v126; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S130. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
