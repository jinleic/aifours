# v162-B post-RETURN reviewer self-audit, notes C (PhysicsPPT44-2)

Preceding actual `/bin/date`: Mon Oct 26 19:41:46 PDT 2026.

**Purpose.** While blocked on Main's direction, I re-read the literal bodies that my returned review `peer-review-v162-B-v1.md` (8d104e35…c472) recorded as verified BEFORE the context compaction (notes-A). The review discloses that its 14 notes-A verdicts rest on pre-compaction reads. This audit re-reads those bodies and re-derives them after compaction, to test that disclosed dependence.

**Scope.**
- This is NOT primary work and NOT a new review scope.
- The returned review file is immutable. Any discrepancy found here would be issued as a separate erratum, never as an edit.
- WRITTEN only. No Eval, interpreter, CAS, program, enumeration, solver or replay was used, and I chose no new probe.
- The "all parameters 1" instance in RM-S028 §6 is the source's own control. I re-checked it; I did not choose it.

## Re-derived after compaction (no change to the returned verdicts)

- **RM-S036 (S204, 264 LF).**
  - C4 tables for v=2,5,6,9,10, with every cycle edge and both absent diagonals.
  - All ten T0 rows: the disjoint-triangle universe and every trace. Singletons occur only at T3{3}, T4{6}, T5{8}, T7{7}, T10{4}.
  - Lemma TRACE.
  - (R1) and (R2).
  - Case I.
  - Case II: (EX), the choice of w, and the collision exclusion at the same v.

  No defect.
- **RM-S021 (S203, 161 LF).**
  - All ten L/R bipartitions with their J_L/J_R profiles.
  - The six equal/separate column rows.
  - The exclusion lists for all ten positions, giving the repeat graph 2-5-9-10-2 plus 6-7.
  - The spanning-tree / two-component forest argument.
  - The at-least-two-distinct-edges check for every K_T: for E, p7≠p2,p10; for I, p6≠p5,p9.

  No defect.
- **RM-S015 (S202, 199 LF).**
  - E_u for all ten u under both FA and FQ.
  - FA-EQ / FQ-EQ necessity.
  - All 40 row sums of the FA and FQ arrays.
  - All comparisons.
  - The cut constraints p2,p5∈{04,14,24} and p9,p10∈{02,03,04}, and p4≠02,24.
  - A full rederivation of the p3=13 case, including both directions of each table.
  - The FQ application to the three p3=04 covers (B components 013/24, H components 02/134, A3≠0, A2≠A3, F1≠0, F1≠F2, C4≠0).
  - The §8 reselections at 7 and at 6.

  No defect.
- **RM-S008 (S201, 116 LF).**
  - Frame row sums for all four rows.
  - T={1,9,10} is independent and misses only J.
  - Equivalence with a common translate.
  - Exclusions:
    - at 1: star 8-9-10, with 8J=j and 9 changed by (d,i);
    - at 9: K2,2 {1,10}|{4,7}, with 1A=a and 7J=j;
    - at 10: K2,2 {1,9}|{3,6}, with 1B=b and 6J=j.
  - The N1 single-service count.
  - Only the two physical-9 tuples (0,0,i),(0,0,0) can coincide, and only when i=0.

  No defect.
- **RM-S028 (S205, 206 LF).**
  - Component table for all ten columns.
  - The twelve-parameter law.
  - Row sums (c−c cancellation).
  - Comparisons at 4 (01 h1, 03 b3, 12 b2, 13 b3, 23 h2), at 6 and at 7.
  - The §6 separations and both hub conditions.
  - The source's all-ones control (only 14 doubly separated at 5; only 03 at 10).

  No defect.
- **RM-S029 (S206, 191 LF).**
  - Component table and the ten-parameter law.
  - All four row sums ((−b)+b cancellation).
  - Comparisons at 3 (shared physical 4 = (b,0,0)), at 6 and at 7.
  - Separations, giving a,b,c,f,h,j≠0 and (d,g,i)≠0.
  - The κ image recomputed site by site: (01,14,24,13,04,12,23,34,03,02).

  No defect.
- **RM-S013 (S207, 235 LF).**
  - L/R/J table.
  - Rook lemma.
  - PIVOT 1⇔2⇔3, with the one-side extension in both directions.
  - Explicit m≥3 family: all ten local tuple rows recomputed from the four syndrome rows, and all ten obstruction value pairs recomputed (e.g. v2: δ=η1−η2 has T3=−1, T6=1; v8: δ=η4 has T3=2, leaf T5=1).
  - The (W0)–(W2) interface.

  No defect.
- **RM-S034 (S208, 262 LF).**
  - O table for all eight peripherals and both hubs.
  - π-invariance of the O table.
  - The monochrome rule.
  - Both constant-hub cases.
  - All four two-block rows (v2, v5, v9, v10).
  - Both one-three-block-hub cases.
  - Both-three-block hubs:
    - C/J rows A–D and their f;
    - the allowed lists;
    - every cross-pair refinement at vertex 3/4;
    - the exceptional g with forcing (q,q);
    - (Q);
    - A,F∈C(g);
    - §7.2 and §7.3, including D∈{0,A}.

  No defect.

**Remaining to re-read (notes-A bodies).** RM-S014, S012, S035, S031, S030, S032.

## Append at actual `/bin/date` Mon Oct 26 19:44:42 PDT 2026 — remaining six bodies (no change to returned verdicts)

- **RM-S014 (S209, 213 LF).** All 40 row sums recomputed from the array:
  - T8 cancellations 2−1=1 and 2−2=0;
  - the rows reproduce η1..η4 exactly.

  Comparisons:
  - at 6 (S={0,1,3,4}; physical 5 zero on S; own values 0,(0,1,2),(1,1,1),(2,1,0), distinct for m≥3);
  - at 3 (shared (0,0,1)/(0,0,2) at physical 2/4);
  - at 2 (24 differs by A=2).

  No defect.
- **RM-S012 (S210, 144 LF).**
  - Rows mod 2.
  - d9 values, with the only collision at 24.
  - All 40 row sums mod 2 (row 4: T2,T3 = 1+1=0).
  - N9 zero on all rows.
  - b4−b2 = (1,1,0)@4 and (1,0,1)@7, so N4 is zero and 4,7 are nonadjacent.

  No defect.
- **RM-S035 (S211, 203 LF).**
  - E_u table for all ten u.
  - (EQ) necessity via T6 and T2.
  - All-solutions array: all row sums for rows 1, 2, 4 recomputed (T7: g+(η2G−g); T9: k+(η2I−k)).
  - X1 = d3(η1)−d3(η2) given η2F=0.
  - Comparisons at 6, 3 and 2.
  - τ family: (EQ); d6 values 0,(0,0,1),(0,1,0),(0,1,1); d3 differences (0,0,1),(1,1,0); d2 values (0,0,1),(1,0,0).

  No defect.
- **RM-S031 (S212, 205 LF).**
  - Component table for all ten columns from the cover (01,34,12,24,34,02,03,04,13,13).
  - The ten-parameter law.
  - All row sums (−b+b, i−i, −j+j).
  - Comparisons at 3 (six S pairs), 6 (J=−j) and 7.
  - The necessity differences (a,0,0), (0,0,−f), (0,0,j).
  - Separations a,b,c,f,h,j; hub (d,g,i)≠0.
  - Affine covariance.

  No defect.
- **RM-S030 (S213, 233 LF).**
  - C/J and A/F/B/H restrictions.
  - p3=12: p9=13; p4∈{14,24}; p4=14 fails at p10; p4=24 gives TYPE A.
  - p3=14: p2=24, p9=13, p4=23; four TYPE C covers, with every table checked.
  - TYPE C coefficient law, including the ε/δ switches for E and I.
  - Transport A and transport B arrays: all row sums and all ten comparisons in each.
  - The (RES) complement.
  - G-family bad pairs at 5 ({24,34}) and 10 ({12,13}).

  No defect.
- **RM-S032 (S214, 196 LF).**
  - MIXED array: all 40 row sums (εe+(1−ε)e=e, εe−εe=0, −b+b, i−i, −j+j).
  - Comparisons: at 3 (02, 03, 23, 24, 34; 04 deliberately omitted), at 7 (01, 04, 14), at 6 (12, 13; shared (b,0,i) and (0,εe,j) on labels 1–3).
  - Label 4's distinct physical 5 is unobserved by N3 and N7.

  No defect.

**Self-audit conclusion.**
- All 14 bodies verified before compaction (notes-A) have now been re-read from the literal parts and re-derived after compaction. No discrepancy with the returned review was found, so no erratum is needed.
- The disclosed pre-compaction reliance is now backed by a post-compaction re-derivation.
- This is still the same single reviewer and the same harness. It is not independent assurance.
