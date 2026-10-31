# RQLS10 v131 — THETA(1,2,2) S103: EQUALITY-KILL — no SQUARE plane-equality case in any mate, hence no split at v2..v5 in any mate

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:48:53 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

S103 pattern, notation of v114/v130. By v123, plane-equality cases occur only in (b-BLOCK, a-BLOCK) mates, so we work in a BB mate (v124/v129 §0): blocks P2 (v2; Yc', β), U3 (v3; Xc', β'), Q4 (v4; Ya', a_y), V5 (v5; Xa', a_{y'}), plus V2, Q3, U4, P5; V-dominoes (v1; a_y), (v3; Xb'); Q-dominoes (v1; a_{y'}), (v2; Yb'); P-dominoes (v1; β'), (v4; Yb'). Each class has six H6 cells forming an orthonormal basis of C^6; each column's three H6 planes are mutually orthogonal.

**LINE-INTERSECTION (elementary).** For a SQUARE (A' ⊥ B', A' ⊥ C', B' ⊥ D', C' ⊥ D') in its line case, with b0' spanning B' ∩ C' and a0' spanning A' ∩ D', we have (A' ⊕ C') ∩ (B' ⊕ D') = span(a0', b0'). Proof: in the v127 line geometry, C' = span(b0', cos θ b1' + sin θ h1') and D' = span(a0', cos φ a1' + sin φ h2') with sin θ·sin φ ≠ 0 and h1' ⊥ h2' in (A' ⊕ B')^⊥. Comparing h1'- and h2'-components, then a1'- and b1'-components, of a common vector leaves only span(a0', b0'). The same holds for (V2, P5) with a0 ∈ A ∩ D and b0 ∈ B ∩ C.

## 1. Lemma DIRECT-SUM(ii) (mirror of v129 for case (ii))

In case (ii) D = A, put W2 = A^⊥ = W(P2) = W(V5) (v124). Then B ∩ C = 0 and W2 = B ⊕ C.

Proof. V's identity P_{A⊕B} + P_{W2} + P_{Π^1_{a_y}} + P_{Π^3_{Xb'}} = 2I gives F1 = Π^1_{a_y} ⊥ F2 = Π^3_{Xb'} with F1 ⊕ F2 = B^⊥. The v5 split (z = Ya') gives G1 = Π^5_{a_y} ⊥ G2 = Π^5_{Xb'} with G1 ⊕ G2 = C^⊥. Columns a_y and Xb' give F1 ⊥ G1 and F2 ⊥ G2: a SQUARE with hat B. If G2 = F1, each V5-block cell is ⊥ its row-mate U-cell in G2 and its class-mate V-cell in F1, so ORTH2 gives W2 ⊥ G2 and G2 = A = Π^5_{Ya'}: TWIN at v5. If G1 = F2, the same with the N-cells at v5 gives Π^5_{a_y} = Π^5_{Ya'}: TWIN. In the line case, C = (G1 ⊕ G2)^⊥ = span(sin θ g1' − cos θ k1, sin φ f1' − cos φ k2) with k1, k2 ∈ B and sin θ·sin φ ≠ 0, so C ∩ B = 0. Both B and C lie in W2. ∎

## 2. Lemma DOUBLE-EQUALITY-KILL

Both SQUAREs cannot be in equality cases simultaneously.

- **(i) with (i') or (ii').** Let W = B^⊥ = W(P2) = W(V5); v129 gives W = A ⊕ D. Columns Xc' and Ya' give Π^3_{Xc'} = W ⊖ A and Π^4_{Ya'} = W ⊖ D. By v130 HAT-EQUALITY, W(U3) = W(Q4) = E^⊥ with E = B' in (i') and E = A' in (ii'). Hence E ⊥ (W ⊖ A) + (W ⊖ D) = W ⊖ (A ∩ D) = W, so E = B and W(U3) = W. Then Π^3_{β'} = W ⊖ Π^3_{Xc'} = A. Column β' gives Π^1_{β'} ⊥ A, and the P-domino sum (v129 §1(b)) gives Π^1_{β'} ⊥ D. So Π^1_{β'} ⊥ W, i.e. Π^1_{β'} = B = C = Π^5_{Xc'}: two (P1,P2)-planes on different position pairs coincide (v115 TWIN-PLANE).
- **(ii) with (i') or (ii').** Now Π^3_{Xc'} = (A ⊕ C)^⊥ = W2 ⊖ C and Π^4_{Ya'} = (B ⊕ A)^⊥ = W2 ⊖ B. As above, E ⊥ W2 ⊖ (B ∩ C) = W2 by §1, so E = A and W(U3) = W2, giving Π^3_{β'} = C. The v2 split (z = Xc') has complementary triple {Ya', Yb', β'}, so Π^2_{β'} ⊥ B; column β' gives Π^2_{β'} ⊥ C. Hence Π^2_{β'} ⊥ W2, i.e. Π^2_{β'} = A = Π^2_{Xc'}: TWIN at v2. ∎

## 3. Lemma HAT-SPLITTING

Suppose (V2, P5) is in an equality case with common hat Ĥ* = Ĥ(P2) = Ĥ(V5) (Ĥ* = B in (i), A in (ii)). By §2, (Q3, U4) is in its line case. Then Ĥ* = span(a0', b0') = (A' ∩ D') ⊕ (B' ∩ C').

Proof. Column Xa' gives A' ⊕ C' = Ĥ* ⊕ Π^5_{a_{y'}}, since Π^5_{Xa'} ⊕ Π^5_{a_{y'}} = W(V5) = Ĥ*^⊥. Column Yc' gives B' ⊕ D' = Ĥ* ⊕ Π^2_β. So Ĥ* lies in the 2-dimensional intersection of LINE-INTERSECTION. ∎

Mirror: if (Q3, U4) is in an equality case with hat Ĥ' = Ĥ(U3) = Ĥ(Q4) (B' in (i'), A' in (ii')), then (V2, P5) is in its line case and Ĥ' = span(a0, b0) = (A ∩ D) ⊕ (B ∩ C), using columns Xc' (A ⊕ C = Ĥ' ⊕ Π^3_{β'}) and Ya' (B ⊕ D = Ĥ' ⊕ Π^4_{a_y}).

## 4. Lemma ROW-KILL

**(a) (V2, P5) equality is impossible.** Keep §3. Let a1' and b1' be unit vectors with A' = span(a0', a1') and B' = span(b0', b1'); both are ⊥ Ĥ*. Column Xc' gives Π^3_{Xc'} = (A ⊕ C)^⊥, and this equals Ĥ*^⊥ ⊖ Y, where Y = A in (i) and Y = C in (ii) is the other plane in Ĥ*^⊥ among A, C.
1. **No Q3 cell lies in Ĥ*.** Suppose the Q3 cell q at row v3.r0 lies in Ĥ*. Let v be the V-domino cell at (v3.r0, Xb'), of class Vi. Then v ⊥ q (row) and v ⊥ Vi's cell in Ĥ* (class; Ĥ* is a V2-block column). By ORTH2, v ⊥ Ĥ*. Vi's three cells other than its dominoes and its Ĥ*-cell lie in Ĥ*^⊥, so Vi's domino cells span span(σ_i, η_j). Here σ_i ∈ Ĥ*^⊥ and η_j is Vj's cell in Ĥ*. So v ∥ σ_i, and Vi's other domino cell, at (v1, a_y), is ∥ η_j: a repeat.
2. **Hence Y = span(a1', b1').** Each U3 cell u_r at (v3.r, Xc') lies in Ĥ*^⊥, so it is ⊥ a0' and b0'. It is also ⊥ its row-mates q_r = α_r a0' + β_r a1' and q'_r = γ_r b0' + δ_r b1'. By step 1, β_r δ_r ≠ 0, so u_r ⊥ a1' and u_r ⊥ b1'. Thus a1' and b1' lie in Ĥ*^⊥ ⊖ Π^3_{Xc'} = Y.
3. **Contradiction.** W(Q3) = A' ⊕ B' = Ĥ* ⊕ Y, so Ĥ(Q3) = (Ĥ* ⊕ Y)^⊥ = Π^3_{Xc'} (column Xc'). Then {Xa', Yc', Xc'} is an orthogonal triple at v3 that separates U3's columns Xc' and β'. This contradicts SQUEEZE (v101), and also v130 §3(a). ∎

**(b) (Q3, U4) equality is impossible.** This is the mirror of (a), with the roles of the rows and blocks exchanged:
- v2 and P2 replace v3 and U3; the V2 block replaces Q3; column Yc' replaces Xc', giving Π^2_{Yc'} = (B' ⊕ D')^⊥ = Ĥ'^⊥ ⊖ Y' with Y' = D' in (i') and B' in (ii').
- The Q-domino cell at (v2.r0, Yb') replaces the V-domino cell. Its class-mate lies in Ĥ', a Q3-block column, and its partner domino cell is at (v1, a_{y'}).

Step 1 then forbids a V2 cell in Ĥ'. Step 2 gives Y' = span(a1, b1). Step 3 gives Ĥ(V2) = Π^2_{Yc'}, an orthogonal triple {Xc', Ya', Yc'} at v2 that separates P2's columns Yc' and β: SQUEEZE fails. ∎

## 5. Theorem EQUALITY-KILL and corollary

In every Latin mate of the S103 pattern, every MAX H6 has BOTH SQUAREs (V2, P5) and (Q3, U4) in their line cases (iii)/(iii'). Proof: v123 for mates with a SPLIT side; §2 and §4 for BB mates.

**Corollary NO-SPLIT-v2..v5 (every mate).** By v130 SPLIT-DICHOTOMY, no MAX H6 of the S103 pattern splits at v2, v3, v4 or v5, in ANY mate. Only v1 may split. This extends v126 NO-SQUEEZED-SPLIT to BB mates. The configurations of v124 and v129, and class (E) of v130 §5, have unsatisfiable hypotheses (prospective; no pinned file is edited).

## 6. Status

The S103 frontier is now the single residual class (L): both SQUAREs in line cases, v2..v5 non-split, v1 split or not, in every mate type. Exact normal forms exist for the b-SPLIT squeezer at v2 (v127) and the SS coupling (v128); BLOCK-side normal forms are not written. Existence or exclusion of (L) is OPEN. So are the other THETA patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v101 SQUEEZE; v111; v114 SQUARE; v115 TWIN-PLANE; v120 TWIN-LINE/TWIN; v123 ORTH2/SQUARE-LINE; v124; v127 line geometry; v129; v130; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S131. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112, S114 and S130 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54, v67 and v76 scope typos;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
