# RQLS10 v109 — C5: EVERY all-two-label TEN-class resolution is excluded (d=3 count, Fourier uniformity, site groups, hat collapse)

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 23:43:36 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written combinatorics and linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

Take the all-sparse C5 placement of v82 with ANY TEN-class resolution in which every class has two labels. Write L_i = (C_i, v_{i−1}) and T_i = (C_i, v_i) for the ten sites. By v105 SITE, each label of a two-label class contributes one site diagonal. By v86 Corollary R, the class types are:
- **A_i** = (L_i, T_{i+1}): the adjacent pair;
- non-adjacent pairs of C_i with C_{i+2}:
  - **B_i** = (T_i, L_{i+2});
  - **G_i** = (L_i, T_{i+2});
  - **LL_i** = (L_i, L_{i+2});
  - **TT_i** = (T_i, T_{i+2}).

The H6 position blocks are (u, d), meaning row-pair v_u and column pair c_{u+d} for d ∈ {2, 3, 4}. Each block holds 4 cells, so every d accounts for 20 H6 cells.

## 1. Lemma D3 (forced H6 rows and the d=3 count)

A two-label class has three full H6 row-pairs and three full H6 column pairs. Intersecting each row-pair's H6 columns with the class's H6 columns forces the following.
- **A_i:** v_{i+2} → c_{i+4}, v_{i+3} → c_{i+2}, v_i → c_{i+3}. Blocks (i,3), (i+2,2), (i+3,4); n_3 = 2.
- **B_i:** v_{i+3} → c_{i+1}, then v_{i+2} → c_{i+4} and v_{i+4} → c_{i+3}. Blocks (i+3,3), (i+2,2), (i+4,4); n_3 = 2.
- **LL_i:** blocks (i+3,3), (i+2,2), (i,3); n_3 = 4.
- **TT_i:** blocks (i+3,3), (i+4,4), (i+1,3); n_3 = 4.
- **G_i:** v_{i+3} → c_{i+1}. If x of the v_i rows go to c_{i+3}, then n_3 = 2 + 2x. For x = 0 the blocks are (i+3,3), (i,4), (i+1,2).

Here n_3 is the number of the class's H6 cells in d=3 blocks. Summing over the ten classes gives 20, while each class has n_3 ≥ 2. Hence EVERY class has n_3 = 2, i.e. every class is A, B or G with x = 0, and every class is block-structured.

## 2. Lemma UNIFORM

Let a_i, b_i, g_i be the multiplicities of the three types. Each block hosts exactly two classes, each on a diagonal; each site hosts two classes. This gives, for all j:
- (L) a_j + b_{j−2} + g_j = 2;
- (T) a_j + b_{j+1} + g_{j−1} = 2;
- (B3) a_j + b_{j+2} + g_{j+2} = 2;
- (B2) a_j + b_j + g_{j+1} = 2;
- (B4) a_j + b_{j−1} + g_{j−2} = 2.

Subtracting gives:
- b_{j−2} + g_j = b_{j+2} + g_{j+2};
- b_j + g_{j+1} = b_{j+1} + g_{j−1}.

At a nonzero Fourier frequency z (z^5 = 1, z ≠ 1), these become b̂ = ĝ(1+z)/z and b̂(1+z²)/z² = −ĝ. Hence ĝ(1 + z + z² + 2z³) = 0. Since 1 + z + z² + 2z³ = z³(1 − z) ≠ 0, ĝ = 0 and b̂ = 0. So a, b, g are constants with a + b + g = 2.

## 3. Lemma GROUP and the three survivors

Two sites of ONE circuit never share a site operator up to sign. Otherwise the P_C-line of the common eigenplane would be a C+ cell at both vertices, contradicting MAX.

By v105 MATCH, classes link the site operators of their two sites. Each mixed constant pattern links L_j to T_j:
- **(1,1,0):** L_j–T_{j+1}–L_{j+3}–T_{j+4}–L_{j+1}–T_{j+2}–L_{j+4}–T_j;
- **(1,0,1):** L_j–T_{j+1}–L_{j−1}–T_j;
- **(0,1,1):** L_j–T_{j+2}–L_{j+4}–T_{j+1}–L_{j+3}–T_j.

Hence the resolution is all-A (v108), all-B or all-G (x = 0). In each survivor every block hosts one class pair on its two diagonals, so v107 BLOCK4 and HAT hold along the row, column and class-pair lines.

## 4. Hat collapse for all-B and all-G

**all-B.** The class lines are S_i = {(i+3,3), (i+2,2), (i+4,4)}.
1. Block (u+4,3) lies on C_{u+2} with (u,2) and on S_{u+1} with (u,4). Hence H_{u+4,3} = H_{u,3} =: Q_3.
2. Row R_u gives H_{u,4} = (Q_3 ⊕ H_{u,2})^⊥. Column C_{u−1} = {(u,4), (u+1,3), (u+2,2)} gives H_{u,4} = (Q_3 ⊕ H_{u+2,2})^⊥.
3. Both H_{u,2} and H_{u+2,2} are orthogonal to Q_3, so H_{u,2} = H_{u+2,2}.

**all-G.** The class lines are S_i = {(i+3,3), (i,4), (i+1,2)}.
1. Block (u+4,4) lies on S_{u+4} with (u,2) and on C_{u+3} with (u,3). Hence H_{u+4,4} = H_{u,4}.
2. Block (u+1,2) lies on C_{u+3} with (u,3) and on S_u with (u,4). Hence H_{u+1,2} = H_{u,2}.

In both cases all fifteen hats lie in ONE decomposition Q_2 ⊕ Q_3 ⊕ Q_4. The v108 PURITY argument and MAX argument then apply verbatim, so no MAX H6 exists.

## 5. Theorem C5-TWO-LABEL-NO-GO and frontier

No original MAX1 array with the all-sparse C5 placement has a TEN-class resolution consisting only of two-label classes, for any frame and any Latin mate. Every surviving C5 resolution must therefore contain a three-label class {C_i, C_{i+1}, C_{i+3}} with a doubled label. Such patterns are OPEN; for them H6 need not be block-structured, and one example type admits n_3 = 0.

The H6 sectors of BARBELL and THETA(1,2,2), dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v82 placement; v86 Corollary R; v105 SITE/MATCH; v107 BLOCK4/HAT/PLS-LINE; v108 TRIANGLE/PURITY/NO-GO; v100 PLS3; finite Fourier analysis on Z5; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S109. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 pre-pin draft correction;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
