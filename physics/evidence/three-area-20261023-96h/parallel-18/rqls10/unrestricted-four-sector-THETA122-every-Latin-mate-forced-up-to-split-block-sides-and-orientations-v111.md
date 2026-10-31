# RQLS10 v111 — THETA(1,2,2): every Latin mate of the S103 class pattern is forced up to two binary side-types and orientations

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:05:17 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written combinatorics only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This manuscript uses the THETA(1,2,2) E4 placement and the TEN classes N1,N2,P1,P2,Q1,Q2,U1,U2,V1,V2 of v103 §4, together with ANY completion L to an order-ten Latin square. H6 supports by row-pair are those of v104 §1.

Reading H6 rows and columns off v103 §4 gives:
- **N** (columns Xb', Yb', a1, a2, b1, b2): N1 rows v1.1, v1.2, v2.1, v3.1, v4.2, v5.1; N2 rows v1.1, v1.2, v2.2, v3.2, v4.1, v5.2.
- **P** (columns Xc', Ya', Yb', Yc', b1, b2): P1 rows v1.2, v2.*, v4.2, v5.*; P2 rows v1.1, v2.*, v4.1, v5.*.
- **Q** (columns Xa', Ya', Yb', Yc', a1, a2): Q1 rows v1.1, v2.2, v3.*, v4.*; Q2 rows v1.2, v2.1, v3.*, v4.*.
- **U** (columns Xa', Xb', Xc', Yc', b1, b2): U1 rows v1.1, v3.*, v4.*, v5.1; U2 rows v1.2, v3.*, v4.*, v5.2.
- **V** (columns Xa', Xb', Xc', Ya', a1, a2): V1 rows v1.1, v2.*, v3.1, v5.*; V2 rows v1.2, v2.*, v3.2, v5.*.

## 1. Theorem FORCED-L

In every L, the following hold.

1. **Forced class-pair blocks.** Intersecting class H6 columns with row-pair H6 supports gives four 2×2 Latin blocks:
   - P at (v5; Xc', Ya');
   - Q at (v3; Xa', Yc');
   - U at (v4; Xa', Yc');
   - V at (v2; Xc', Ya').
2. **Column completions.** Each of the columns below has H6 cells at three row-pairs, and only the three listed class pairs carry it in H6. Hence:
   - Xc' (v2, v3, v5; classes P, U, V): U fills Xc' at v3;
   - Ya' (v2, v4, v5; P, Q, V): Q fills Ya' at v4;
   - Xa' (v3, v4, v5; Q, U, V): V fills Xa' at v5;
   - Yc' (v2, v3, v4; P, Q, U): P fills Yc' at v2.
3. **Single dominoes.** The remaining allowed columns are exhausted, so:
   - P fills Yb' at v4;
   - U fills Xb' at v5;
   - Q fills Yb' at v2;
   - V fills Xb' at v3.
4. **N block.** Columns Yb' (v1, v2, v4; classes N, P, Q) and Xb' (v1, v3, v5; classes N, U, V) are now full except at v1. Hence N occupies the 2×2 block (v1; Xb', Yb').
5. **Remaining positions.**
   - v1: the a-columns carry Q1, V1 (row v1.1) and Q2, V2 (row v1.2); the b-columns carry P2, U1 (v1.1) and P1, U2 (v1.2).
   - v2: the b-columns carry P's second cells and N.
   - v3: the b-columns carry U's second cells and N.
   - v4: the a-columns carry Q's second cells and N.
   - v5: the a-columns carry V's second cells and N.
6. **Side types.** Columns b1 and b2 (H6 at v1, v2, v3; classes N, P, U) admit exactly two patterns:
   - **b-SPLIT:** P1 and P2 use different b-columns at v2.
   - **b-BLOCK:** P occupies a 2×2 block (v2; Yc', b_x). This forces U into the block (v3; Xc', b_{x'}), with P at v1 and N at v2 in b_{x'}, and U at v1 and N at v3 in b_x.

   Symmetrically, columns a1 and a2 (v1, v4, v5; classes N, Q, V) are a-SPLIT or a-BLOCK. In the a-BLOCK case Q occupies (v4; Ya', a_y) and V occupies (v5; Xa', a_{y'}).

Proof. Every step intersects allowed column sets or counts a column's six H6 cells among exactly three class pairs, each of which must appear once per column. In step 6, P1, P2, U1, U2, N1 and N2 each use both b-columns exactly once, which leaves only the two listed patterns. Both patterns are consistent with every row and column.

Hence L is determined by its side types (4 cases) together with finitely many block orientations and b/a labels. v103's L is the (b-SPLIT, a-SPLIT) case.

## 2. Corollaries for H6

- **(i) BLOCK4.** By the v107 argument, every class-pair 2×2 block above is an orthonormal 4-frame with a 2-dimensional hat. In every L this includes the N block at v1 and the V, Q, U, P blocks at v2, v3, v4, v5. In the BLOCK cases there are, in addition, P at v2, U at v3, Q at v4 and V at v5.
- **(ii) Squeezes.** By v104 §2 and the v101 SQUEEZE lemma, the forced triples hold as follows.
  - In the (b-SPLIT, a-SPLIT) case, every orthogonal triple split is forced exactly as in v104 §3:
    - v2: {Yc', b1, b2};
    - v3: {Xc', b1, b2};
    - v4: {Ya', a1, a2};
    - v5: {Xa', a1, a2};
    - v1: {Xb', Yb', x}.
  - In a BLOCK side the corresponding triple is instead {block columns, z}, where the plane of z is the hat of that block (v107 TRIPLE argument). For example, at v2 under b-BLOCK it is {Yc', b_x, z} with Π_z = Ĥ(P-block).
- **(iii) Scope of v104 §4.** The v104 §4 all-triple no-go was proved for v103's L, which is one (b-SPLIT, a-SPLIT) orientation. Its extension to the other orientations and to the BLOCK cases is NOT claimed here.

## 3. Status

This is a structural reduction for EVERY Latin mate of the S103 class pattern; no H6 existence or exclusion is claimed. Other THETA(1,2,2) class patterns, the BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v103 §4 classes; v104 §1/§2 supports and squeezes; v101 SQUEEZE; v107 BLOCK4/TRIPLE arguments. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S111. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 and S110 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
