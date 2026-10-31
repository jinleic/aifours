# Actual Tuscan11 distinct-centre 4+4 — class (b) with a three-row face (d = 5) is impossible

Actual `/bin/date` before this body: **Mon Oct 26 06:05:13 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Three tools, stated for rows that may end at a branch vertex

**(L1) Cross-thread lemma, non-leaving form.** On a cross path X, no face has two consecutive rows Q1 = [x, x+10] and Q2 = [x+10, x+20] that do not leave X. Either row may begin or end at the branch vertex that closes X.

The proof is that of v53 §1 (SHA256 `73c0724422c1c9be9e63acab22f7c5f55ee7845d58063d7f8dff973610bd7c08`). Its table uses only three facts:
- Q1 and Q2 are clean against every overlapping row of the other face (v50 §2);
- the bd and shift-5 paths lie inside Q1 or Q2;
- the other face's rows may leave X.

If x is the branch vertex and d = 0, that vertex is a boundary at one visit of each face, which is a second cut of its label.

**(L2) Self-dual lemma, non-leaving form.** The same holds for one pass of a doubly traversed thread. The proof is that of v54 §1 (SHA256 `a6d3578fdb396f71f2bbbcc08c1964cbc5acef3f078caf69fc7e4f288cf0405d`), with (L1) in place of v53.

**(L3) Boundary coincidence.** On a thread traversed twice by one face, the two passes have boundary residues beta and gamma (mod 10) in thread coordinates. If beta ≡ gamma and the thread has more than 10 edges, the least positive s ≡ beta is an interior vertex that is a boundary at both of its visits. That doubles a cut.

## 2. Class (b) with d = 5

Class (b) is as in v54 §2: F_1 = T1 L_w T1^- L_v and F_2 = T2 L_w^- T2^- L_v^-, with a = |T1|, b = |T2|, p = |L_v|, q = |L_w|. Here d = 5, so r_1 = 3, r_2 = 8, b = a+25 in 26..30 and p+q = 30-2a.

**Counts.** Every symbol labels exactly one of the 11 cuts, since each symbol occurs 11 times and its vertex visits come in even numbers. Let t1 and t2 be the numbers of v-copies on T1 and T2, lam_v the number on the loops, and eps_v = 1 if the v-cut lies in F_1.
- F_1 holds v three times: 2 + 2t1 + lam_v + eps_v = 3. So t1 = 0 and lam_v = 1 - eps_v <= 1.
- Likewise **lam_w <= 1**: at most one loop copy of w exists.

**F_2 on T2.** Put b_v(0) at F_2-position 0. Then T2-coordinate s sits at s on the forward pass and at 2b+q-s on the backward pass, b_w at b and b+q, and L_v^- runs over [2b+q, 80]. Let beta' and gamma' in 1..10 be the least positive boundaries of the two passes in T2-coordinates.
- (L3) gives beta' ≠ gamma'.
- (L2) gives beta'+20 >= b+1 and gamma'+20 >= b+1. Otherwise the pass rows [beta', beta'+10] and [beta'+10, beta'+20] do not leave T2.
- Since beta'+10 <= 20 < b, the forward pass meets exactly three rows: [beta'-10, beta'] (holding or starting at b_v(0)), [beta', beta'+10] (inside T2), and [beta'+10, beta'+20] (holding b_w(b) strictly inside).
- The backward pass likewise meets three rows.
- These six rows are distinct. A row meeting both passes would contain a whole loop together with both of its branch visits, i.e. one label twice.

**Gaps.** The remaining two rows of F_2 lie in two gaps:
- the L_w-gap, from position beta'+20 >= b+1 to position 2b+q-gamma'-20 <= b+q-1, so it is strictly inside L_w;
- the L_v-gap, from 2b+q-gamma'+10 to 70+beta'.

Their lengths G_w and G_v are non-negative multiples of 10 with G_w + G_v = 20. By (L1) neither gap holds two rows, so G_w = G_v = 10.

**Contradiction.**
- The L_w-gap row lies strictly inside L_w, so its w is a loop copy of w on L_w.
- The L_v-gap row lies on L_v, possibly ending at b_v. Its w is not b_w, so it is a loop copy of w on L_v.

That needs two loop copies of w, against lam_w <= 1. QED

## 3. Result

**Class (b) with d = 5 is impossible.** With v54 (d = 7), class (b) is now open only at d = 1 and d = 3. The (a)-II survivors are those of v56 (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`) together with the four/four shape at Sigma = 21 (v52).

Also open: distinct 3+5; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
