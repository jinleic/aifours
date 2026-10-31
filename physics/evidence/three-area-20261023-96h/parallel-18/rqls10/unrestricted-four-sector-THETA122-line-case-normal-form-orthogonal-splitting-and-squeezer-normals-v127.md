# RQLS10 v127 — THETA(1,2,2) line-case normal form: the SQUARE splits C6 orthogonally into two 3-spaces, and every squeezer cell lies in a plane spanned by two forced normals

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:18:06 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Why the line case

By v123 and v126, every MAX H6 of the S103 THETA(1,2,2) pattern for a mate with a SPLIT side has three properties:
- both SQUAREs are in line cases (iii)/(iii');
- v2, v3, v4 and v5 are non-split;
- only v1 may split.

This manuscript records an exact normal form for that residual case, for future exact or computational work.

## 1. Lemma LINE-GEOMETRY (square (V2, P5), case (iii))

There is an orthonormal basis {a0, a1, b0, b1, h1, h2} with the following properties:
- A = span(a0, a1), B = span(b0, b1) and Ĥ(V2) = span(h1, h2);
- C = span(b0, c'), where c' = cos θ b1 + sin θ h1;
- D = span(a0, d'), where d' = cos φ a1 + sin φ h2;
- θ and φ lie in (0, π/2].

Then the following hold.
- **(a) Orthogonal splitting.** C6 = (B + C) ⊕ (A + D), where B + C = B ⊕ span(h1) and A + D = A ⊕ span(h2) are orthogonal 3-spaces.
- **(b) Dominoes and hats.** Put x1 = sin θ b1 − cos θ h1 and y1 = sin φ a1 − cos φ h2. Then:
  - the U-domino is X = Π^{v3}_{Xc'} = (A ⊕ C)^⊥ = span(x1, h2);
  - the Q-domino is Y = Π^{v4}_{Ya'} = (B ⊕ D)^⊥ = span(y1, h1);
  - Ĥ(P5) = span(x1, y1).
- **(c) The span Ω.** X ∩ Y = 0 and X ⊕ Y = Ω := span(a1, b1, h1, h2). Here Ω^⊥ = span(a0, b0) = (A ∩ D) + (B ∩ C).

Proof. Everything follows by writing the complements in the basis. For (c), a common vector of X and Y would need its a1- and b1-coordinates to vanish; this forces it to be 0, since sin θ and sin φ are nonzero.

## 2. Lemma SQUEEZER-NORMALS (b-SPLIT side, at v2)

Each P-cell at v2 lies in a plane span(n, m), with:
- n ∈ B + C the unit normal, inside B + C, to its row-mate V-cell in B and its class-mate P-cell in C;
- m ∈ A + D the unit normal, inside A + D, to its row-mate V-cell in A and its class-mate P-cell in D.

The P-cells at v2 are d_{Yc'} = P1(v2.1, Yc'), e_{Yc'} = P2(v2.2, Yc'), d_{P2} = P2(v2.1, b2) and e_{P1} = P1(v2.2, b1).

Proof. The cell is orthogonal to these four cells. Its component in each orthogonal 3-space of §1(a) is orthogonal to two non-parallel vectors of that 3-space, so the component is parallel to the normal. ∎

**The resulting system.** The P-cells at v2 must satisfy five orthogonalities: column Yc', rows v2.1 and v2.2, and classes P1 and P2. Writing each cell as x n + y m, these become five bilinear equations. By the complex Lagrange identity, each equation has the form x̄x'<n|n'> + ȳy'<m|m'> = 0, and every inner product of two normals is a product of two cell overlaps.

**Mirrors.** On an a-SPLIT side, the V-cells at v5 obey the same normal form. Their n is the normal to the row-mate P-cell in C and the class-mate V-cell in B; their m is the normal to the row-mate P-cell in D and the class-mate V-cell in A. The (Q3, U4) square gives the same normal form for U-cells at v3 and Q-cells at v4, with C6 = (B' + C') ⊕ (A' + D').

## 3. Status

§1–§2 give an exact NORMAL FORM, and no contradiction is claimed. The residual all-line-case system with non-split v2..v5 (and v1) is OPEN. So are:
- BB equality cases;
- the other THETA patterns;
- BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v114 SQUARE; v120; v123 ORTH2/SQUARE-LINE; v126; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S127. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
