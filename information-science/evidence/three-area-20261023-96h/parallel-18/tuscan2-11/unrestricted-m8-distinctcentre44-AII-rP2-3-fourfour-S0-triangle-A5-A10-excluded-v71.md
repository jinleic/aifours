# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape — triangle lemma: (S0) type (6,9) with o0 = 5 and type (9,6) with o0 = 10 are impossible

Actual `/bin/date` before this body: **Mon Oct 26 09:11:44 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Triangle lemma

**Lemma.** Let a thread X begin b_v, X[1], X[2], X[3], with labels v, x1, x2, x3. Suppose another stretch, vertex-disjoint from it, carries the complementary P4 of v-x1-x2-x3 (as rule (R) with k = 4 provides). Then:
- **(i)** all three pairs {x1,x2}, {x2,x3}, {x1,x3} occur as actual edges;
- **(ii)** the v-vertex of the complementary path has neighbours carrying x2 and x3.

Consequently, by (F2):
- no other actual edge carries a pair inside {x1, x2, x3};
- none of x1, x2, x3 equals a label that already shares an edge with v elsewhere.

*Proof.* The complement of v-x1-x2-x3 is x2-v-x3-x1 or its reverse x1-x3-v-x2. X supplies the edges {x1,x2} and {x2,x3}, and the complement supplies {x1,x3}, {v,x2} and {v,x3}. QED

The lemma is applied twice below, with the rows of v66 §2 (SHA256 `81c7dd124c2121003f24349c9b966a4a7ff9760cf5d6880df1de16d617551686`).

## 2. Type (6,9) with A = o0 = 5 is impossible

Here P is in {7, 8, 9}. B_0 = e5..e1, v, a1..a5 and B_3 = v, c1..c10 (B_3 starts at the v-cut b_v(25)). Also R_0 = c4..c1, v, e1..e6 and R_2 = c14..c4.
- **R_0 vs B_0** gives {c1, c2, c3, c4, e6} = {a1..a5}, so c1, c2, c3 lie in {a1..a5}.
- **R_2 vs B_3** is rule (R) with k = 4 (v49 §4): T3[11..14] is the complementary P4 of T3[0..3] = v, c1, c2, c3.
- **None of c1, c2, c3 is a1.** The edge b_v T1[1] already carries {v, a1}. b_v is adjacent to T3[1], and the T3 v-copy in T3[11..14] is adjacent to the vertices carrying c2 and c3.
- So {c1, c2, c3} is a 3-subset of {a2, a3, a4, a5}. Every such subset contains one of the T1 edge pairs {a2,a3}, {a3,a4} or {a4,a5}, all of which are actual edges of T1[2..5].
- By §1 all three pairs inside {c1, c2, c3} occur on T3. This is a repeat. QED

## 3. Type (9,6) with A = o0 = 10 is impossible

Here P is in {6, 7, 8}. B_0 = e10..e1, v (it ends at the v-cut b_v(0)), B_3 = b5..b1, v, c1..c5, R_0 = c6..c1, v, e1..e4 and R_1 = e4..e14.
- **R_0 vs B_3** gives {c6, e1, e2, e3, e4} = {b1..b5}, so e1, e2, e3 lie in {b1..b5}.
- **R_1 vs B_0** is rule (R) with k = 4: T4[11..14] is the complementary P4 of T4[0..3] = v, e1, e2, e3.
- By §1 all pairs inside {e1, e2, e3} occur on T4. They therefore avoid the T2 edge pairs {b1,b2}, {b2,b3}, {b3,b4}, {b4,b5}. The only such 3-subset of {b1..b5} is **{b1, b3, b5}**.
- But b1 is none of e1, e2, e3. The edge b_v T2[1] carries {v, b1}, b_v is adjacent to T4[1], and the T4 v-copy is adjacent to the vertices carrying e2 and e3. Contradiction. QED

## 4. Result

**(S0) type (6,9) with o0 = 5 and type (9,6) with o0 = 10 are impossible**, and so are their v<->w mirrors (types (1,4) and (4,1) with the parameters swapped).

With v69 (SHA256 `627942a9c34e0bd03583a2c03509fe0adb1f5c6a797e9cc240d253d280142046`) and v70 (SHA256 `20844c08ce0439d760a05575cbddb121b04ed55c74e13baf9c607580e31c2f2d`), **type (6,9) is entirely excluded**, and with it type (1,4). The four/four shape remains open only in (S0) type (9,6) with A in {8, 9} and P in {6, 7, 8}, and its mirror type (4,1).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
