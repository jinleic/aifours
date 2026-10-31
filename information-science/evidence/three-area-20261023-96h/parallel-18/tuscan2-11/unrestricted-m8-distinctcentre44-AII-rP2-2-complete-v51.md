# Actual Tuscan11 distinct-centre 4+4, class (a)-II — a two-row P2 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 05:05:02 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Two-row cycle lemma

**Lemma.** Let a face F have exactly two rows, meeting at the cuts z1 and z2. Then no row Q of the other face consists of eleven consecutive vertices of F's cycle traversed in the opposite direction.

*Proof.* Unroll F's 20-cycle onto a line of period 20, with F running left to right, so each vertex appears at positions p and p+20. Put Q = [x, x+10]; Q runs right to left.

- **Q contains no cut of F in its interior.** Then Q lies in one closed F-row arc of length 10, so Q is that arc. Q's two end vertices are then boundaries in both faces, so their labels are cut twice. Contradiction.
- **Q contains a cut z1 = x+k, 1 <= k <= 9.** Q holds only one cut, since the cuts are 10 apart. The F-row R_a starting at z1 covers [x+k, x+k+10] and ends at z2. The F-row R_b ending at z1 covers [x+k-10, x+k] and starts at z2.
  - (Q, R_a) share [x+k, x+10], reached from opposite ends. By v49 §4 rule (R) (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`), the labels of Q[x, x+k-1] equal those of R_a[x+11, x+k+10], which contains z2.
  - (Q, R_b) share [x, x+k], so the labels of Q[x+k+1, x+10] equal those of R_b[x+k-10, x-1], which also contains z2.
  - So the label of z2 occurs in both disjoint parts of the row Q. Contradiction. QED

## 2. Application: both cuts in P6

Take class (a)-II with r_P2 = 2 and both cuts in P6. By v49 (and v<->w), the remaining cases are X = 0 with X' = 0 or 1. v50 (SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`) excludes X' = 1, so only X = X' = 0 remains.

Let R_V be the rows whose v is one of H1's four run v's, and R_W the rows whose w is one of H2's four run w's. Then |R_V| = |R_W| = 4.
- A row holding an H1-interior position lies between b_v(0)'s row and b_v(35)'s row, so it is in R_V.
- A row holding an H2-interior position is in R_W.

Let s be the number of rows in both sets. Since 9 = 4 + 4 - s + o, there are o = s+1 >= 1 rows O in neither set.

Such a row meets neither H1 nor H2, so it holds no b_v or b_w visit. Hence it lies inside T3 or T4: eleven consecutive vertices of P2's 20-cycle, traversed opposite to P2. The lemma excludes this.

## 3. Result

The case analysis is:
- both cuts in P2: v47 (SHA256 `3a60200022a7d702a4589e6e0752fc2e86d7421f11f3d7210499b90a72d6a321`);
- exactly one cut in P2: v48 (SHA256 `aa59b87c9ceb6566a80b883fc70179f0dc6cbd947be28f9ab9c572f2268b1df0`);
- both cuts in P6: v49, v50 and §2 above.

So **in distinct-centre 4+4 class (a)-II, r_P2 = 2 is impossible**.

The lemma applies to any face with exactly two rows.

Still open in (a)-II: r_P2 = 3, 4, 5. Also open: class (b), distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
