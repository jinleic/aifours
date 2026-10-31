# RQLS10 v118 — THETA(1,2,2): a side-sum identity rules out splits at both v2 and v3 (and at both v4 and v5); BLOCK-PAIR no longer needs v1

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:57:31 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

We use the S103 THETA(1,2,2) class pattern with ANY Latin mate L, as described in v111.
- Π^v_k is the H6 plane of column k at row-pair v. A split at v is an orthogonal triple split (v104 §1).
- Columns b1 and b2 carry H6 cells only at v1, v2 and v3. Columns a1 and a2 carry H6 cells only at v1, v4 and v5.
- By v111, N1 has rows v2.1, v3.1, v4.2, v5.1 and N2 has rows v2.2, v3.2, v4.1, v5.2. In a b-SPLIT mate:
  - each of P1, P2, U1, U2 has exactly one b-cell at v1;
  - at v2, the b-cells are P's second cells and N's cells, one of each per b-column;
  - at v3, the b-cells are U's second cells and N's cells, one of each per b-column.

## 1. Lemma SIDE-SUM

Suppose v2 and v3 split with triples T2 ⊇ {b1, b2} and T3 ⊇ {b1, b2}. Let F and G be the planes of the third members of T2 and T3. Then:

    P(Π^{v1}_{b1}) + P(Π^{v1}_{b2}) = P_F + P_G,   and hence   Π^{v1}_{b1} + Π^{v1}_{b2} = F + G.

Proof.
1. Columns b1 and b2 each sum to I over v1, v2 and v3.
2. Each split triple sums to I, so the b-planes at v2 sum to I − P_F and those at v3 to I − P_G.
3. Subtracting gives the identity.
4. For positive operators, the range of a sum is the sum of the ranges.

## 2. Theorem B-PAIR (every b-SPLIT mate, any a-side, every orientation)

In a b-SPLIT mate, no MAX H6 splits at both v2 and v3.

Proof.
1. **The triples.** By v104 §3 and v112, the triples are forced:
   - T2 = {Yc', b1, b2}, with F = Π^{v2}_{Yc'} (the P domino);
   - T3 = {Xc', b1, b2}, with G = Π^{v3}_{Xc'} (the U domino).
   §1 applies.
2. **The N-cells lie in (F+G) ⊖ F.** Take P_i's v2-columns m1 (row v2.1) and m2 (row v2.2), and third column m' ∈ {b1, b2}. By the v101 §4 forced form, P_i's m'-cell, which lies at v1, equals α·d_{m2} + β·e_{m1} with αβ ≠ 0.
   - In either orientation, one of d_{m2}, e_{m1} is P_{i'}'s Yc'-cell, which lies in F.
   - The other is the N-cell at v2 in P_i's own b-column, which lies in F^⊥ because T2 is orthogonal.
   - The m'-cell lies in Π^{v1}_{b} ⊂ F + G.

   Hence both N-cells at v2, x1 = N1(v2.1, b_σ) and x2 = N2(v2.2, b_σ'), lie in (F+G) ⊖ F. They are orthonormal because they sit in different T2-planes.
3. **The N-cells at v3.** The same argument with U_i's forms places the N-cells y1 = N1(v3.1, ·) and y2 = N2(v3.2, ·) in (F+G) ⊖ G. Since N1 uses each column once, y1 = N1(v3.1, b_σ') and y2 = N2(v3.2, b_σ).
4. **Dimensions.** dim((F+G) ⊖ F) ≥ 2. Hence F ∩ G = 0 and dim(F+G) = 4, so (F+G) ⊖ F = span(x1, x2) and (F+G) ⊖ G = span(y1, y2).
5. **Cross-orthogonality.** Every x is orthogonal to every y:
   - x1 ⊥ y1 (class N1);
   - x1 ⊥ y2 (column b_σ);
   - x2 ⊥ y1 (column b_σ');
   - x2 ⊥ y2 (class N2).

   So (F+G) ∩ G^⊥ ⊥ (F+G) ∩ F^⊥. Inside the 4-dimensional F+G this gives (F+G) ∩ G^⊥ = F, so F ⊥ G, G = span(x1, x2) and F = span(y1, y2).
6. **The contradiction.** Put K = (F ⊕ G)^⊥, which has dimension 2.
   - P_i's b-cell k_i at v2 is orthogonal to F (T2), to its own column's N-cell (column) and to the other N-cell (different T2-plane). So k_i ⊥ G, and k_i ∈ K. Hence K = span(k_1, k_2).
   - Likewise U_i's b-cells l_i at v3 lie in K.
   - In column b_σ, P's v2-cell and U's v3-cell are orthogonal. Inside the plane K, the U-cell is therefore parallel to P's v2-cell in column b_σ'.

   Two distinct positions then carry one ray, which contradicts MAX.

## 3. Theorem BLOCK-PAIR (every b-BLOCK mate, any a-side)

Use the v113 notation: P block (v2; Yc', β), U block (v3; Xc', β'), P domino (v1; β'), U domino (v1; β), N dominoes (v2; β') and (v3; β). No MAX H6 has both of the following:
- v2 split as {Yc', β, β'}, i.e. z = β';
- v3 split as {Xc', β', β}, i.e. z' = β.

This removes the v1 hypothesis from v113 BLOCK-TOGETHER.

Proof.
1. §1 applies with F = Π^{v2}_{Yc'} and G = Π^{v3}_{Xc'}.
2. By v113 Z-CELL, P_i's β'-cell lies at v1, inside Π^{v1}_{β'} ⊂ F+G, and equals a combination with both coefficients nonzero of P_{i'}'s block cells: one in F, one in Π^{v2}_β ⊥ F. Hence Π^{v2}_β ⊂ (F+G) ⊖ F, and by dimension F+G = F ⊕ Π^{v2}_β = W(P2).
3. Likewise, U's forms give F+G = G ⊕ Π^{v3}_{β'} = W(U3).
4. The split triples then give Π^{v2}_{β'} = W(P2)^⊥ = W(U3)^⊥ = Π^{v3}_β.
5. Both of these are (N1,N2) domino planes built from different positions, so v115 TWIN-PLANE gives a MAX contradiction.

## 4. Mirrors on the a-side

The a-columns carry H6 cells only at v1, v4 and v5. Q squeezes v4, V squeezes v5, and the N-cells there are N2(v4.1), N1(v4.2), N1(v5.1) and N2(v5.2). Repeating §2 and §3 gives:
- **A-PAIR (a-SPLIT).** No MAX H6 splits at both v4 and v5. Here F' = Π^{v4}_{Ya'}, G' = Π^{v5}_{Xa'} and the cross-orthogonalities are class/column exactly as in §2. The final repeat is V's v5 a-cell against Q's v4 a-cell in the other a-column.
- **a-BLOCK-PAIR.** With the Q block (v4; Ya', a_y) and the V block (v5; Xa', a_{y'}), v4 = {Ya', a_y, a_{y'}} and v5 = {Xa', a_{y'}, a_y} do not both hold, because the two N dominoes would coincide.

## 5. Consequences (prospective; no pinned file is edited)

- **(a)** In every (b-SPLIT, a-SPLIT) mate, at most THREE row-pairs split: v1, at most one of v2 and v3, and at most one of v4 and v5. Every MAX H6 therefore has at least two non-split row-pairs.
- **(b)** v112 SS-ALL-TRIPLE remains true, but it is SUPERSEDED by (a) for SS mates.
- **(c)** The hypothesis of the v116 §2 corollary and of v117 (v2, v3, v4 and v5 all split) is UNSATISFIABLE. v117's lemmas are vacuous rather than false. The single-split statements of v116 Theorem TWIN-SQUARE keep their content.
- **(d)** v113 BLOCK-TOGETHER is superseded by §3.

Open in the b-BLOCK case: v2 and v3 splits with separated third columns (z ≠ β' or z' ≠ β), apart from the one v115 sub-case.

## 6. Status

THETA(1,2,2) H6 existence or exclusion remains OPEN. In particular, H6 structures with non-split row-pairs, separated BLOCK splits, the other THETA class patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6 are all open. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v104 §3 and v112 forced triples; v101 §4 forced form; v113 Z-CELL; v115 TWIN-PLANE; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S118. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112 and S114 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
