# RQLS10 v112 — THETA(1,2,2), every (b-SPLIT, a-SPLIT) Latin mate: no MAX H6 has orthogonal triple splits at all five row-pairs

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:13:57 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra and combinatorics only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

v104 §4 proved the all-triple no-go for v103's L only. By v111 FORCED-L, every (b-SPLIT, a-SPLIT) mate has the v104 §3 forced triples:
- v1: {Xb', Yb', x};
- v2: {Yc', b1, b2};
- v3: {Xc', b1, b2};
- v4: {Ya', a1, a2};
- v5: {Xa', a1, a2}.

What may vary between such mates is their ORIENTATION.

## 1. Lemma ORIENT (b-side)

Let β_1 be P1's b-column at v2, and β_2 the other b-column. Let r be the row of P1's Yc' cell at v2, and r' the other row. Then every b-SPLIT mate has the following form.
- **v2:** row r holds P1 at Yc', P2 at β_2 and N_r at β_1. Row r' holds P2 at Yc', P1 at β_1 and N_{r'} at β_2. Here N_1 = N1 and N_2 = N2.
- **v1:** P1 sits at (v1.2, β_2) and P2 at (v1.1, β_1). U1 sits at (v1.1, β_2) and U2 at (v1.2, β_1).
- **v3:** U1's Xc' cell lies in row r' and its b-cell, in column β_1, lies in row r. U2 is the mirror. N_r sits at β_2 and N_{r'} at β_1.

Proof. P1, P2, U1, U2, N1 and N2 each use both b-columns once. N1's b-cells at v2 and v3 must therefore differ, and this forces U's Xc' row at v3 to be r'.

Hence, up to the label swap b1↔b2, the b-side has exactly the two orientations r = 1 and r = 2. v103's L has r = 1.

## 2. Theorem SS-ALL-TRIPLE

In every (b-SPLIT, a-SPLIT) mate, no MAX H6 has orthogonal triple splits at all five row-pairs. Precisely:
- if v1 splits with x ∈ {a1, a2}, then v2 or v3 has no orthogonal triple split;
- if v1 splits with x ∈ {b1, b2}, then v4 or v5 has none.

Proof, case x ∈ {a1, a2}, for both orientations r.
1. **Plane Latin array.** b1 and b2 share a triple at v1, v2 and v3. The third columns are a_o, Yc' and Xc'. Both b-columns sum to I, so (v1, v2, v3) × (b1, b2, third) is a plane Latin array. By v100 PLS3 it is Classical or K33.
2. **Forced forms (v101 §4), with d = row-1 and e = row-2 cells.**
   - P1 (r = 1 or r = 2 alike): (v1.2, β_2) = α·N_r(v2, β_1) + β·P2(v2, Yc').
   - P2: (v1.1, β_1) = α'·P1(v2, Yc') + β'·N_{r'}(v2, β_2).
   - U1 at v3:
     - for r = 1: (v1.1, β_2) = α''·U2(v3.1, Xc') + β''·N2(v3.2, β_1);
     - for r = 2: (v1.1, β_2) = α''·N1(v3.1, β_1) + β''·U2(v3.2, Xc').

   All coefficients are nonzero.
3. **Classical case.** The P1 form puts one cell into a single decomposition member, yet it has nonzero components in two distinct members. This is impossible.
4. **K33 case at v2.** Write the v2 planes as β_1 = (p1, q1), β_2 = (p2, q2) and Yc' = (p3, q3).
   - Entries in different rows and columns share exactly one index (v107 Fact). Containment of the P1 form therefore gives Π^{v1}_{β_2} = (p1, q3), N_r(v2, β_1) = x_{p1} and P2(v2, Yc') = y_{q3}, up to the x/y mirror.
   - The P2 form then gives Π^{v1}_{β_1} = (p3, q2) and N_{r'}(v2, β_2) = y_{q2}.
   - So every v2 cell is a K33 line: P1 = y_{q1} at β_1, P1 = x_{p3} at Yc', and P2 = x_{p2} at β_2.
5. **Completion at v1 and v3.** Latin completion gives:
   - v1: a_o = (p2, q1);
   - v3: β_1 = (p2, q3), β_2 = (p3, q1), Xc' = (p1, q2).
6. **Contradiction from the U1 form.** Containment in x_{p1} ⊕ y_{q3} forces:
   - for r = 1: U2(v3.1, Xc') = x_{p1} = N1(v2.1, β_1);
   - for r = 2: U2(v3.2, Xc') = x_{p1} = N2(v2.2, β_1).

   In either case two distinct cells carry one ray, contradicting MAX.

The x/y-mirrored case gives the mirrored identities and the same contradiction.

Case x ∈ {b1, b2}. This is the same argument on (v1, v4, v5) × (a1, a2, third), under the following relabeling:
- classes P1→Q2, P2→Q1, U1→V1, U2→V2, N→N;
- row-pairs v2→v4 (with its rows .1/.2 swapped), v3→v5, v1→v1;
- columns b→a, Yc'→Ya', Xc'→Xa'.

Renaming classes, and swapping rows .1/.2 within a single row-pair, are symmetries of the H6 problem: rows, columns, classes, triple splits and the forced form α·d_{m2} + β·e_{m1} are all invariant under them. Since both orientations are covered above, the a-side yields the corresponding repeat. (Pre-pin draft clarification: an earlier unpinned wording omitted the explicit class renaming P1→Q2, P2→Q1 and the row swap at v4. It was made explicit before the first pin.)

## 3. Status

v104 §4 is generalized from v103's L to EVERY (b-SPLIT, a-SPLIT) Latin mate. Every MAX H6 in these mates must therefore contain a row-pair without an orthogonal triple split. The BLOCK side-types of v111, the non-triple H6 structures, H6 existence, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v104 §3 and §4 method; v101 §4 forced form; v100 PLS3 and U6; v107 Fact on order-3 MOLS. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S112. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103 and S110 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
