# RQLS10 v133 — THETA(1,2,2) S103, SS residual: the N-tight-frame of squeezer singles, squeezer orthogonality, and cross-frame alignment of Ω'

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 03:07:28 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

By v132, the only S103 mates that can carry a MAX H6 are (b-SPLIT, a-SPLIT). There both SQUAREs are in line cases (v123) and v2..v5 are non-split (v126). We use the v103 orientation and the v127/v128 notation. The SS layout (v103, v111) is:
- **v1.** The N block (Xb', Yb'). Row v1.1: b1 = P2, b2 = U1, a1 = Q1, a2 = V1. Row v1.2: b1 = U2, b2 = P1, a1 = V2, a2 = Q2.
- **v2.** The P-domino (Yc'), with P-singles p21 = P2(v2.1, b2) and p22 = P1(v2.2, b1), and N-singles N1(v2.1, b1), N2(v2.2, b2).
- **v3.** The U-domino (Xc'), with U-singles u31 = U1(v3.1, b1) and u32 = U2(v3.2, b2), and N-singles N1(v3.1, b2), N2(v3.2, b1).
- **v4, v5.** The a-side mirror. Q has its domino (v4; Ya') and two Q-singles at v4 in the a-columns. V has its domino (v5; Xa') and V-singles v51 = V1(v5.1, a1) and v52 = V2(v5.2, a2). N has two singles at each of v4 and v5.

The b-columns have H6 cells only at v1, v2, v3. The a-columns have them only at v1, v4, v5.

## 1. Lemma N-TIGHT-FRAME

Let S be the sum of the rank-one projections of the eight SQUEEZER SINGLES: p21, p22, u31, u32, the two Q-singles at v4, v51 and v52. Then S = 2P_{W(N1)}. Hence all eight singles lie in W(N1) = Π^1_{Xb'} ⊕ Π^1_{Yb'}, and they form a tight frame with constant 2 there.

Proof. Row v1 gives P_{W(N1)} + Σ_c P_{Π^1_c} = 2I, the sum running over c ∈ {b1, b2, a1, a2}. Class N gives P_{W(N1)} + Σ (eight N-singles) = 2I. Subtracting, Σ_c P_{Π^1_c} equals the sum of the eight N-singles.

Each such column c has projection sum I. Its four cells at v2 and v3 (or at v4 and v5) are one N-single and one squeezer single per row-pair. So Σ_c P_{Π^1_c} = 4I − (N-singles) − S. Therefore 4I − S = 2·(N-singles) = 2(2I − P_{W(N1)}). The positivity argument of v132 §1 then places every single in W(N1). ∎

**Structure of the frame.** The singles pair up by column: {p22, u31} in b1, {p21, u32} in b2, and two (Q, V) pairs in a1 and a2. These four orthogonal pairs span four planes whose projections sum to 2P_{W(N1)}. No two singles share a row or a class.

## 2. Lemma SQUEEZER-ORTHOGONALITY

Each squeezer's two singles are orthogonal to its own domino:
- span(p21, p22) ⊥ Π^2_{Yc'};
- span(u31, u32) ⊥ Π^3_{Xc'};
- the Q-singles at v4 are ⊥ Π^4_{Ya'};
- span(v51, v52) ⊥ Π^5_{Xa'}.

Proof (P at v2). P1(v2.1, Yc') is ⊥ p21 by row and ⊥ p22 by class. P2(v2.2, Yc') is ⊥ p21 by class and ⊥ p22 by row. The others are the same. ∎

## 3. Lemma CROSS-ALIGNMENT

Let Ω' = Π^2_{Yc'} + Π^5_{Xa'}. This is the P-domino at v2 plus the V-domino at v5, the (Q3, U4)-analogue of v127 §1(c). Then:
- **(a)** Ω' = span(nα, nδ) ⊕ span(mα, mδ), with the v128 normals nα, nδ ∈ B + C and mα, mδ ∈ A + D. So Ω' is compatible with the orthogonal splitting C6 = (B + C) ⊕ (A + D) of the (V2, P5) line geometry.
- **(b)** span(a0', b0') = Ω'^⊥ = ℓ_BC ⊕ ℓ_AD. Here a0' ∈ A' ∩ D' and b0' ∈ B' ∩ C' (the (Q3, U4) lines), and
  - ℓ_BC = span(d_B, P1_C) ∩ span(e_B, P2_C), a line in B + C;
  - ℓ_AD = span(d_A, P1_D) ∩ span(e_A, P2_D), a line in A + D.

Proof.
1. **Ω' lies in the span of four normals.** By the v128 table, the four domino cells P1(v2.1, Yc'), P2(v2.2, Yc'), V2(v5.1, Xa') and V1(v5.2, Xa') lie in span(nα, mα), span(nδ, mδ), span(nα, mδ) and span(nδ, mα) respectively. So Ω' ⊂ span(nα, nδ, mα, mδ).
2. **Ω' has dimension 4.** By LINE-INTERSECTION (v131 §0) for (Q3, U4), Π^5_{Xa'} = (A' ⊕ C')^⊥ and Π^2_{Yc'} = (B' ⊕ D')^⊥ meet in 0. So Ω' is 4-dimensional and equals span(nα, nδ, mα, mδ). In particular nα, nδ are independent, and so are mα, mδ.
3. **Complement.** Since B + C ⊥ A + D, the complement Ω'^⊥ is ((B + C) ⊖ span(nα, nδ)) ⊕ ((A + D) ⊖ span(mα, mδ)). Within B + C, the vectors ⊥ nα are span(d_B, P1_C), and those ⊥ nδ are span(e_B, P2_C). Their intersection is ℓ_BC; ℓ_AD is identical. Finally, Ω'^⊥ = span(a0', b0') by LINE-INTERSECTION. ∎

## 4. Corollary SINGLES-SPAN

By v128, p22 ∈ span(nβ, mβ), p21 ∈ span(nγ, mγ), v51 ∈ span(nβ, mγ) and v52 ∈ span(nγ, mβ). So these four singles lie in W(N1) ∩ span(nβ, nγ, mβ, mγ). If they are linearly independent, then W(N1) = span(nβ, nγ) ⊕ span(mβ, mγ). In that case W(N1) also splits along (B + C) ⊕ (A + D), and Ĥ(N1) is the sum of one line in B + C and one line in A + D.

## 5. Status

§1–§4 are exact necessary conditions on the SS residual. No contradiction is claimed. Existence or exclusion of the SS line-case H6 (v1 split or not) is OPEN. So are:
- the other THETA(1,2,2) class patterns;
- BARBELL H6;
- C5 three-label patterns;
- dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v103/v111 layout; v123; v126; v127 LINE-GEOMETRY; v128 NORMAL-SHARING; v131 §0 LINE-INTERSECTION; v132 §1 positivity argument; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S133. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112, S114 and S130 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54, v67 and v76 scope typos;
- the v77 stray-space and characterization typos;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
