# RQLS10 v117 — THETA(1,2,2) SS joint configuration: T'-triples equal column decompositions; three planes shared by P and V; no mutual orthogonality; angle matching

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:43:54 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

Take a (b-SPLIT, a-SPLIT) mate of the S103 THETA(1,2,2) class pattern. Assume an MAX H6 in which:
- v2, v3, v4 and v5 split;
- the pair (V2, P5) is in SQUARE case (i);
- the pair (Q3, U4) is in SQUARE case (ii').

By v112 and v116 this is the joint configuration left open when v1 is the non-split row-pair. Write:
- A = Π^{v2}_{Xc'} and B = Π^{v2}_{Ya'}, so that Π^{v5}_{Xc'} = B (case (i));
- D = Π^{v5}_{Ya'};
- A' = Π^{v3}_{Xa'} = Π^{v4}_{Yc'} (case (ii')).

## 1. Lemma COLUMN-TRIPLES

The complementary triples T' coincide with column decompositions:
- the triple T' at v2 is column Xc''s decomposition {A, Ĥ(V2), B};
- the triple at v5 is column Ya''s decomposition {B, Ĥ(P5), D};
- the triple at v3 is column Yc''s decomposition {Ĥ(Q3), Π^{v3}_{Yc'}, A'};
- the triple at v4 is column Xa''s decomposition {A', Π^{v4}_{Xa'}, Ĥ(U4)}.

Proof. Substitute the identities of v116 §2 into the T' triples of v114 §2.

## 2. Lemma SHARED-PLANES

Each of the planes X1 = B, X2 = Ĥ(Q3) and X3 = Ĥ(U4) contains exactly two P-cells and two V-cells:

| Plane | P-cells | V-cells |
|---|---|---|
| X1 = B | P1, P2 at v5 in column Xc' | V1, V2 at v2 in column Ya' |
| X2 = Ĥ(Q3) | at v2 in column Yc' | at v3 in column Xb' |
| X3 = Ĥ(U4) | at v4 in column Yb' | at v5 in column Xa' |

Within each plane, the two P-cells and the two V-cells each form an orthonormal basis, because each pair shares a column. For each class, its cells in X1, X2 and X3 are mutually orthogonal because they lie in one class. By MAX, no V-cell is parallel to a P-cell.

## 3. Theorem NOT-ORTHOGONAL

X1, X2 and X3 are NOT mutually orthogonal.

Proof. Suppose they were, so that C6 = X1 ⊕ X2 ⊕ X3.
1. Column Xb' gives Ĥ(Q3) ⊥ Ĥ(P5).
2. W(P5) = B ⊕ D, so Ĥ(P5) ⊥ B.
3. Hence Ĥ(P5) ⊂ (X1 ⊕ X2)^⊥ = X3, so Ĥ(P5) = Ĥ(U4).
4. Then Π^{v4}_{Ya'} = Ĥ(P5) = Ĥ(U4) = Π^{v4}_{Yb'}. Two distinct column planes at the same row-pair v4 would coincide.
5. In that case the row-1 cell of Yb', being orthogonal to the row-1 cell of Ya', is parallel to the row-2 cell of Ya'. This is a repeated ray.

## 4. Lemma ANGLE-MATCH

For a plane X with P-basis (P1_X, P2_X), write V1_X = α_X P1_X + β_X P2_X. Here α_X·β_X ≠ 0. Suppose two of the planes X, Y have a nonzero cross-Gram matrix. In the P-bases this matrix has zero diagonal, of the form [[0, g],[h, 0]]. The V-orthogonality conditions are the pair of equations:
- conj(α_X) δ_Y g + conj(β_X) γ_Y h = 0;
- β_X conj(γ_Y) g + α_X conj(δ_Y) h = 0.

Here V1_Y = γ_Y P1_Y + δ_Y P2_Y. The pair has a nonzero solution only if the determinant vanishes, i.e. |α_X||δ_Y| = |β_X||γ_Y|, which gives |α_X| = |γ_Y|. So any two non-orthogonal planes among X1, X2, X3 carry the same P–V angle.

## 5. Status

Two facts are established for the open joint configuration: mutual orthogonality is impossible, and every non-orthogonal pair of shared planes must angle-match. Existence and exclusion of this configuration remain OPEN, as do the other THETA(1,2,2) H6 configurations, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v112/v114/v116 split criteria and SQUARE cases; v115 TWIN-PLANE; elementary 2×2 linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S117. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112 and S114 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
