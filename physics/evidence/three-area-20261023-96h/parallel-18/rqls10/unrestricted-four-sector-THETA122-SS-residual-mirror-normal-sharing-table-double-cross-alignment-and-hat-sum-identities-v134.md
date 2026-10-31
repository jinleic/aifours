# RQLS10 v134 — THETA(1,2,2) S103, SS residual: explicit mirror normal-sharing table, double cross-alignment, and the hat-sum identities Ω = Ĥ(V2) ⊕ Ĥ(P5), Ω' = Ĥ(Q3) ⊕ Ĥ(U4)

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 03:19:16 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra, read off the hand-checked v103 §5 Latin table. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This is the SS residual of v132/v133 in the v103 §5 orientation, with both SQUAREs in line cases. From v103 §5:
- **Q3 block.** d_{A'} = Q1(v3.1, Xa'), e_{A'} = Q2(v3.2, Xa'), d_{B'} = Q2(v3.1, Yc'), e_{B'} = Q1(v3.2, Yc').
- **U4 block.** U1_{C'} = U1(v4.1, Xa'), U2_{C'} = U2(v4.2, Xa'), U2_{D'} = U2(v4.1, Yc'), U1_{D'} = U1(v4.2, Yc').
- **U at v3.** The domino U2(v3.1, Xc'), U1(v3.2, Xc'), and the singles u31 = U1(v3.1, b1), u32 = U2(v3.2, b2).
- **Q at v4.** The domino Q1(v4.1, Ya'), Q2(v4.2, Ya'), and the singles q41 = Q2(v4.1, a1), q42 = Q1(v4.2, a2).

The (Q3, U4) line geometry (v127 mirror) gives orthogonal 3-spaces C6 = (B' + C') ⊕ (A' + D').

## 1. Lemma MIRROR-NORMAL-SHARING

Each U-cell at v3 and each Q-cell at v4 is orthogonal to its row-mate and its class-mate in each 3-space. So it lies in span(n', m'), with:
- n' ∈ B' + C', the normal to its row-mate in B' or C' and its class-mate in C' or B';
- m' ∈ A' + D', the corresponding normal.

Define eight normals:

| (B' + C') normal | Pair | (A' + D') normal | Pair |
|---|---|---|---|
| n'α | N(d_{B'}, U2_{C'}) | m'α | N(d_{A'}, U2_{D'}) |
| n'β | N(e_{B'}, U1_{C'}) | m'β | N(e_{A'}, U1_{D'}) |
| n'γ | N(d_{B'}, U1_{C'}) | m'γ | N(d_{A'}, U1_{D'}) |
| n'δ | N(e_{B'}, U2_{C'}) | m'δ | N(e_{A'}, U2_{D'}) |

Then:

| Cell | Plane |
|---|---|
| U2(v3.1, Xc') | span(n'α, m'α) |
| U1(v3.2, Xc') | span(n'β, m'β) |
| u31 | span(n'γ, m'γ) |
| u32 | span(n'δ, m'δ) |
| Q1(v4.1, Ya') | span(n'β, m'α) |
| Q2(v4.2, Ya') | span(n'α, m'β) |
| q41 | span(n'γ, m'δ) |
| q42 | span(n'δ, m'γ) |

Proof.
- **U-cells.** A U-cell in row v3.r is ⊥ the Q3 cells of that row: d_{A'}, d_{B'} for r = 1 and e_{A'}, e_{B'} for r = 2. By class it is ⊥ its own class's U4 cells in C' and D'.
- **Q-cells.** A Q-cell in row v4.r is ⊥ the U4 cells of that row: U1_{C'}, U2_{D'} for r = 1 and U2_{C'}, U1_{D'} for r = 2. By class it is ⊥ its own class's Q3 cells: Q1_{A'} = d_{A'}, Q1_{B'} = e_{B'}, Q2_{A'} = e_{A'}, Q2_{B'} = d_{B'}.
- **Reading off the planes.** v127 SQUEEZER-NORMALS places each component on the stated normal, and the pairs coincide as listed. For example, Q1(v4.1, Ya') pairs with U1_{C'} (row) and e_{B'} (class), giving n'β. ∎

This verifies explicitly the "same structure" stated at the end of v128 §2.

## 2. Theorem DOUBLE CROSS-ALIGNMENT

Put Ω = Π^3_{Xc'} + Π^4_{Ya'} (U-domino at v3 plus Q-domino at v4) and Ω' = Π^2_{Yc'} + Π^5_{Xa'} (as in v133).
- **(a)** Ω = span(n'α, n'β) ⊕ span(m'α, m'β) splits along (B' + C') ⊕ (A' + D'). Hence span(a0, b0) = Ω^⊥ = ℓ_{B'C'} ⊕ ℓ_{A'D'}, where
  - ℓ_{B'C'} = span(d_{B'}, U2_{C'}) ∩ span(e_{B'}, U1_{C'});
  - ℓ_{A'D'} = span(d_{A'}, U2_{D'}) ∩ span(e_{A'}, U1_{D'}).
- **(b)** (v133) Ω' = span(nα, nδ) ⊕ span(mα, mδ) splits along (B + C) ⊕ (A + D). Hence span(a0', b0') = ℓ_BC ⊕ ℓ_AD.

So each SQUARE's two-line plane splits along the OTHER SQUARE's orthogonal 3-space decomposition.

Proof of (a). By §1, Ω lies in span(n'α, n'β, m'α, m'β). Ω is 4-dimensional by v127 §1(c), so the two are equal. The complement is computed as in v133 §3. ∎

## 3. Lemma HAT-SUM

Ω = Ĥ(V2) ⊕ Ĥ(P5) and Ω' = Ĥ(Q3) ⊕ Ĥ(U4), both direct sums.

Proof. In the v127 basis, Ĥ(V2) = span(h1, h2) and Ĥ(P5) = span(x1, y1), with x1 = sin θ b1 − cos θ h1 and y1 = sin φ a1 − cos φ h2. Since sin θ·sin φ ≠ 0, these four vectors span span(a1, b1, h1, h2) = Ω (v127 §1(c)). The (Q3, U4) case is the mirror, with Ĥ(U4) = span(sin θ' b1' − cos θ' h1', sin φ' a1' − cos φ' h2') from v132 §2. ∎

## 4. Corollary SINGLES-SPLIT

The U/Q singles u31, u32, q41, q42 lie in W(N1) ∩ span(n'γ, n'δ, m'γ, m'δ) (v133 §1 and §1 above). The P/V singles lie in W(N1) ∩ span(nβ, nγ, mβ, mγ) (v133 §4).
- If either quadruple is linearly independent, W(N1) equals the corresponding normal span. Then W(N1) splits along that SQUARE's 3-space decomposition.
- If both are independent, W(N1) splits along BOTH decompositions. In that case Ĥ(N1) = λ_BC ⊕ λ_AD = λ_{B'C'} ⊕ λ_{A'D'}, with λ_BC = span(e_B, P1_C) ∩ span(d_B, P2_C) and analogous lines.

## 5. Status

§1–§4 complete the exact SS normal form. No contradiction is claimed. The SS line-case H6 is OPEN, with v1 split or not. So are:
- the other THETA(1,2,2) class patterns;
- BARBELL H6;
- C5 three-label patterns;
- dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v103 §5 table; v127 LINE-GEOMETRY/SQUEEZER-NORMALS; v128; v131 §0; v132 §2; v133; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S134. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
