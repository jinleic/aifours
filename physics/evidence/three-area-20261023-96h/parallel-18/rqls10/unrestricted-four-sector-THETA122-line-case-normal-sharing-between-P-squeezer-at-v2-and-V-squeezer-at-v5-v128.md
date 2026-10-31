# RQLS10 v128 — THETA(1,2,2) line case: the squeezer cells at v2 (P) and at v5 (V) share four normals in each orthogonal 3-space

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:23:04 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This is the S103 THETA(1,2,2) pattern in an SS mate, with (V2, P5) in the line case (iii). The notation is that of v127, written in the v103 orientation.
- V block at v2: d_A = V1(v2.1, Xc'), e_A = V2(v2.2, Xc'), d_B = V2(v2.1, Ya') and e_B = V1(v2.2, Ya').
- P block at v5, in one fixed Latin orientation: P1_C = P1(v5.1, Xc'), P2_D = P2(v5.1, Ya'), P2_C = P2(v5.2, Xc') and P1_D = P1(v5.2, Ya'). The other orientation only relabels.
- B + C and A + D are the orthogonal 3-spaces of v127 §1.

For non-parallel u, w in one 3-space, N(u, w) denotes their unit normal inside that 3-space.

## 1. Lemma NORMAL-SHARING

There are eight normals.

In B + C:
- nα = N(d_B, P1_C);
- nβ = N(e_B, P1_C);
- nγ = N(d_B, P2_C);
- nδ = N(e_B, P2_C).

In A + D:
- mα = N(d_A, P1_D);
- mβ = N(e_A, P1_D);
- mγ = N(d_A, P2_D);
- mδ = N(e_A, P2_D).

The squeezer cells lie in the following planes.

| Squeezer cell | Plane |
|---|---|
| P1(v2.1) = P1(v2.1, Yc') | span(nα, mα) |
| P1(v2.2) = P1(v2.2, b1) | span(nβ, mβ) |
| P2(v2.1) = P2(v2.1, b2) | span(nγ, mγ) |
| P2(v2.2) = P2(v2.2, Yc') | span(nδ, mδ) |
| V1(v5.1) = V1(v5.1, a1) | span(nβ, mγ) |
| V1(v5.2) = V1(v5.2, Xa') | span(nδ, mα) |
| V2(v5.1) = V2(v5.1, Xa') | span(nα, mδ) |
| V2(v5.2) = V2(v5.2, a2) | span(nγ, mβ) |

Proof.
1. A P_i-cell in row v2.r is orthogonal to two cells: its row-mate V-cell in B (resp. A), and its class-mate P_i-cell in C (resp. D).
2. A V_j-cell in row v5.r is orthogonal to two cells: its row-mate P-cell in C (resp. D), and its class-mate V_j-cell in B (resp. A).
3. These pairs coincide crosswise. For example, {e_B, P1_C} is the pair for both of the following:
   - P1's row-v2.2 cell (row with e_B, class with P1_C);
   - V1's row-v5.1 cell (class with e_B, row with P1_C).
4. v127 SQUEEZER-NORMALS then places each component on the stated normal. ∎

**Structure of the normals.**
- In B + C:
  - nα, nβ ⊥ P1_C, and nγ, nδ ⊥ P2_C;
  - nα, nγ ∈ span(e_B, h1), and nβ, nδ ∈ span(d_B, h1);
  - the two lines (B+C) ⊖ C = span(x1) and (B+C) ⊖ B = span(h1) are where these families meet.
- In A + D, analogously, with span(y1) and span(h2).

## 2. The coupled system

The coupled system has eight cells: P-cells u = a n + b m and V-cells w = c n + e m.
- **The P-cells at v2** satisfy the orthogonalities of rows v2.1 and v2.2, column Yc', and classes P1 and P2.
- **The V-cells at v5** satisfy those of rows v5.1 and v5.2, column Xa', and classes V1 and V2.
- **Each orthogonality** reads ā a'<n|n'> + b̄ b'<m|m'> = 0.
- **The Gram entries of the normals** are explicit, by the complex Lagrange identity: up to unit factors and normalisations, <N(a,b)|N(c,d)> ∝ <c|a><d|b> − <d|a><c|b>. Hence every entry is a product of two of the cross-overlaps <d_B|P_iC>, <e_B|P_iC>, <d_A|P_iD>, <e_A|P_iD>.
- **The free parameters** are the angles θ, φ, the cross-overlaps, and eight unit pairs (a, b), (c, e).

The (Q3, U4) square gives the same structure for U at v3 and Q at v4.

## 3. Status

This is an exact normal form coupling the two squeezers. NO contradiction is claimed. The residual line-case system remains OPEN; so do v1, the BB cases, the other THETA patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v114; v123 ORTH2; v127 LINE-GEOMETRY/SQUEEZER-NORMALS; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S128. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
