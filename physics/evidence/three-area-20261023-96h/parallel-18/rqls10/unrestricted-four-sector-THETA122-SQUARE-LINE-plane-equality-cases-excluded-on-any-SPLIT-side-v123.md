# RQLS10 v123 — THETA(1,2,2) SQUARE-LINE: if either side is SPLIT, both SQUAREs avoid every plane-equality case and lie in the line cases (iii)/(iii')

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 01:44:34 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting and an elementary principle

We work with the S103 THETA(1,2,2) pattern, any Latin mate (v111), and the notation of v114/v120. At row-pair v, d_k and e_k are the row-1 and row-2 cells of column k.

**Principle ORTH2.** A vector orthogonal to two non-parallel vectors of a plane W is orthogonal to W. In particular, if a cell is structurally orthogonal (row, column or class) to two cells of W lying at distinct positions, then MAX makes those two cells non-parallel and the cell is ⊥ W. This principle also underlies v121 DOUBLE-PAIR.

**Fact SPLIT-PLANES.** For two column planes Π_k and Π_j at one row-pair, span(d_k, e_j) ⊥ span(e_k, d_j). The proof uses only rows and columns. If Π_k ∩ Π_j = 0, which v120 TWIN-LINE forces under MAX, then Π_k + Π_j = span(d_k, e_j) ⊕ span(e_k, d_j).

## 1. Theorem SQUARE-LINE

Suppose the b-side of the mate is SPLIT, or the a-side is.
- (V2, P5) is in neither SQUARE case (i) nor case (ii). Hence it is in case (iii): C ∩ B and D ∩ A are lines.
- Likewise (Q3, U4) is in neither case (i') nor case (ii'). Hence it is in case (iii').

**Proof for (V2, P5), case (i) C = B, b-SPLIT.**

Work at v2 in the v103 orientation; every b-SPLIT orientation only relabels classes. The P-cells at v2 are:
- d_{Yc'} = P1(v2.1, Yc') and e_{Yc'} = P2(v2.2, Yc');
- d_{P2} = P2(v2.1, b_{s'}) and e_{P1} = P1(v2.2, b_s).

The N-cells are d_{N1} = (v2.1, b_s) and e_{N2} = (v2.2, b_{s'}). Put F = Π^{v2}_{Yc'}.

1. **The P-cells at v2 are ⊥ B.** B = C carries the V-cells d_B and e_B, and also the P-cells of C at v5. Each P-cell at v2 is orthogonal to its row-mate in B and, by class, to its own class's cell in C. ORTH2 then gives P-cell ⊥ B.
2. **B^⊥ = A + F.** Together with A ⊥ B, step 1 gives that B^⊥ contains A + F, which has dimension 4 since A ∩ F = 0 by TWIN-LINE. So B^⊥ = A + F, and d_{P2}, e_{P1} ∈ A + F.
3. **The b-cells of P in coordinates.**
   - d_{P2} is orthogonal to d_A, to d_{Yc'} (rows) and to e_{Yc'} (class P2). Solving in the basis {d_A, e_A, d_{Yc'}, e_{Yc'}} gives d_{P2} ∝ e_A − <d_{Yc'}|e_A> d_{Yc'}.
   - Likewise e_{P1} ∝ d_A − t̄ e_{Yc'}, where t = <d_A|e_{Yc'}> and |t| < 1 by MAX.
   - Hence, by SPLIT-PLANES, B^⊥ = Π1 ⊕ Π2 with Π1 = span(d_A, e_{Yc'}) and Π2 = span(e_A, d_{Yc'}) = span(d_{Yc'}, d_{P2}).
4. **Row v2.1.** Row v2.1 is orthonormal, and d_A, d_{Yc'}, d_{P2} ∈ B^⊥ while d_B ∈ B. Hence span(d_{Yb'}, d_{N1}) = span(r, e_B), where r ∈ Π1 is the unit vector ⊥ d_A. So r ∝ e_{Yc'} − t d_A.
5. **Column b_s.** Here d_{N1} ⊥ e_{P1}. Write d_{N1} = x r + y e_B. Since e_{P1} ∈ B^⊥, this gives x <r|e_{P1}> = 0. A direct computation gives <e_{Yc'} − t d_A | d_A − t̄ e_{Yc'}> = −t̄(1 − |t|²).
   - **If t ≠ 0**, then x = 0 and d_{N1} ∥ e_B: N's cell repeats V's cell.
   - **If t = 0**, then e_{P1} ∥ d_A: P's cell repeats V's cell.

   Either way MAX fails.

**Case (ii), D = A.** The same argument applies with A and B exchanged. A = D carries V-cells and P-cells, so the P-cells at v2 are ⊥ A and A^⊥ = B + F. The conclusion is that d_{N1} ∥ e_A, or e_{P1} ∥ d_B.

**a-SPLIT instead.** The same argument runs at v5. V squeezes v5, with its domino at (v5, Xa') and its a-cells. In case (i) the cells of C are paired by rows with V's v5 cells and by class with V's v2 cells, so V's v5 cells are ⊥ C and C^⊥ = D + Π^{v5}_{Xa'}. Then V's and N's a-cells at v5 give the same dichotomy. Case (ii) is symmetric.

**(Q3, U4).** The same proofs apply:
- at v3 with U as squeezer and the Q block, using U's b-cells and N's b-cells, for b-SPLIT;
- at v4 with Q as squeezer and the U block, using Q's a-cells and N's a-cells, for a-SPLIT.

Case (i') B' = C' carries Q-cells (v3) and U-cells (v4). Case (ii') A' = D' does the same. ∎

## 2. Consequences (prospective; no pinned file is edited)

- **(a)** By v120, a v2 or v5 split forces case (i), and a v3 or v4 split forces case (ii'). Theorem SQUARE-LINE therefore re-proves v121 SPLIT-KILL independently of DOUBLE-PAIR.
- **(b)** In every mate with at least one SPLIT side, every MAX H6 has both SQUAREs in the line cases.
  - In each SQUARE, the V-plane and the P-plane meet in exactly a line, and so do the Q-plane and the U-plane: C ∩ B, D ∩ A, C' ∩ B' and D' ∩ A' are lines.
  - In SS mates this sits on top of v121: only v1 may split.

## 3. Status

THETA(1,2,2) H6 existence or exclusion remains OPEN. In particular, the line cases (iii)/(iii') with non-split v2..v5 and v1 are open, and so are:
- BLOCK sides beyond v122;
- the other THETA class patterns;
- BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v104 §2; v111 FORCED-L; v114 SQUARE; v120 TWIN-LINE; v121; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S123. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
