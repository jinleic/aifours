# Actual Tuscan11 distinct-centre 4+4, class (b) with d = 3 — the two-gap case is impossible

Actual `/bin/date` before this body: **Mon Oct 26 06:15:27 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Class (b) and the tools (L1)-(L3) are as in v57 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`). v46 (SHA256 `d212cc7d2c8b7907187f0e20732206224cfa0cee0dcfedb41d874342e5d9c5ca`) forbids full rows (of either face) on both loops.

With d = 3: r_1 = 4, r_2 = 7, b = a+15 in 16..30, and p+q = 40-2a.

**Counts.** For each of v and w (cut in F_1 iff eps = 1, lam loop copies), F_1 gives 2 + 2t1 + lam + eps = 4 and F_2 gives 2 + 2t2 + lam + 1 - eps = 7. So (t1, t2, lam, eps) is one of:
- (1, 2, 0, 0);
- (0, 1, 2, 0);
- (0, 2, 1, 1).

## 2. Passes of F_2 on T2

Use v57's F_2-positions (cycle length 70) and its least positive pass boundaries beta', gamma' in T2-coordinates.
- (L3) gives beta' ≠ gamma'.
- (L2) gives beta'+20 >= b+1 and gamma'+20 >= b+1.
- A pass meets three rows when its first boundary is at most b-11, and two otherwise. In the two-row case the second row reaches b_w, and if it ends exactly there, that b_w-visit is a boundary.
- As in v57, no row meets both passes. So 7 - n_f - n_b rows lie in the loop gaps, at most one per gap by (L1), and n_f + n_b >= 5.

Row reversal, with both loops re-oriented, keeps the class-(b) form and swaps the two passes of each face. So the two-gap case may be taken with **n_f = 3, n_b = 2**.

## 3. n_f = 3, n_b = 2 is impossible

Here gamma'+10 >= b gives b <= 20, and beta' <= b-11 <= 9.

**F_2's rows.**
- W_f0 = [beta'-10, beta'] holds b_v(0).
- W_f1 = [beta', beta'+10] lies inside T2.
- W_f2 = [beta'+10, beta'+20] holds b_w(b) strictly.
- In T2-coordinates, W_b0 = [gamma'-10, gamma'] holds or ends at b_v(2b+q), and W_b1 = [gamma', gamma'+10] holds or starts at b_w(b+q).
- Both gaps have length 10, giving gap rows O_w = F_2[beta'+20, beta'+30] on L_w and O_v on L_v. Hence q = 40+beta'+gamma'-2b and p = 30-beta'-gamma'.

**Which branch visit is touched.**
- O_w starts strictly inside L_w, and ends at b_w(b+q) iff gamma'+10 = b.
- O_v ends strictly inside L_v, and starts at b_v(2b+q) iff gamma' = 10.
- By v46 one of them touches, so gamma' is 10 or b-10. The touched visit is a boundary, hence that label's cut, in F_2.

**Copies.** O_w needs a loop v-copy on L_w, and O_v needs a loop w-copy on L_v. O_w also needs a loop w-copy on L_w when it is full; when it touches b_w, eps_w = 0. Either way lam_w = 2, and symmetrically lam_v = 2. So both labels take option (0, 1, 2, 0): t1 = 0, t2 = 1, and F_1 contains no v-cut or w-cut. Call the T2 copies c_v^T and c_w^T.
- W_f1 takes the forward visits of c_v^T and c_w^T.
- The backward visit of c_v^T lies in W_b1 (W_b0 has b_v), so s_v > gamma'.
- The backward visit of c_w^T lies in W_b0 (W_b1 has b_w), so s_w < gamma', and beta' < gamma'.
- The remaining v of W_f2, O_w and O_v come from the two loop v-copies and the v-cut. The remaining w of W_f0, O_w and O_v come from the two loop w-copies and the w-cut.

**3.1. gamma' = 10, b <= 19.**

The v-cut is b_v(2b+q), so the loop v-copies serve W_f2 and O_w and both lie on L_w. O_w is full, so one loop w-copy lies on L_w and the other on L_v. Thus L_v carries no v-copy and exactly one w-copy, and F_1 has no row inside L_v.

F_1's rows are therefore R_0 = [phi0, phi0+10], holding b_v(0) strictly (phi0 in -9..-1), then R_A, R_B, and R_1 = [phi0+30, phi0+40], holding b_v(2a+q) = b_v(20+beta'). That forces phi0 <= beta'-11 <= -3.

Measure along L_w in F_2's direction from b_w(b). Then O_w = [x, x+10] with x = beta'+20-b, and F_1's boundary sits at offset (5-phi0) mod 10 inside O_w. Both F_1 rows overlapping O_w are clean, so rule (R) (v49 §4) needs offset 4, 5 or 6. That leaves only phi0 = -9, with offset 4. Then the bd chain W_f2, R_-, O_w, R_+ (starts x-10, x-6, x, x+4) fires unless R_- leaves through the W_f2 end, i.e. unless x <= 5. Hence beta' <= b-15 = a, and phi0 = -9 <= beta'-11 gives beta' >= 2.

Now R_0 = [-9, 1] misses b_w(a), since a >= 2. And R_1 = [21, 31] misses b_w(a+q), since a+q = 20+beta'-a <= 20. So R_0 and R_1 both need the single w-copy on L_v. Contradiction.

**3.2. gamma' = 10, b = 20** (so a = 5, q = 10+beta', p = 20-beta').

Both cuts are branch visits. So the loop v-copies lie on L_w (they serve W_f2 and O_w) and the loop w-copies lie on L_v (they serve W_f0 and O_v). In F_1:
- a row holding a loop v-copy takes its w from a b_w-visit;
- a row holding a loop w-copy takes its v from a b_v-visit.

So F_1 has a boundary phi in 1..4, with the others at phi+10j.
- On L_w, take u from b_w(a) along F_1. Then O_w = [0, 10] (it ends at b_w(b+q), which is u = 0). F_1's rows with u-windows [phi-5, phi+5] and [phi+5, phi+15] are clean against O_w with k = 5-phi and phi+5. Rule (R) forces phi = 1.
- On L_v, take z from b_v(2a+q) along F_1. Then O_v = [10-beta', 20-beta'], and F_1's row [phi+30, phi+40] has z-window [phi+10-beta', phi+20-beta']. It is clean against O_v with k = phi = 1. Contradiction.

**3.3. gamma' = b-10 <= 9.**

The w-cut is b_w(b+q), so the loop w-copies serve W_f0 and O_v and both lie on L_v. O_v is full, so one loop v-copy lies on L_v and the other on L_w. Hence L_w carries one v-copy and no w-copy.

In F_1:
- the row R_B holding the L_v v-copy has no b_v and no v-cut, so it lies strictly inside L_v;
- the row R_A holding the L_w v-copy takes its w from a b_w-visit.

The cyclic order is R_0 (holding b_v(0); R_0 = [phi0, phi0+10] with phi0 in -9..-1), R_A, R_1 (holding b_v(2a+q)), R_B. Here 2a+q = beta'+b and q = 30+beta'-b.

In z (from b_v(2a+q) along F_1), O_v = [O, O+10] with O = 10-beta', and R_B starts at O+psi with psi = phi0+20-b in -8..3. O_v and R_B do not leave L_v, so (O_v, R_B) and O_v against R_B's F_1 neighbours are clean. Rule (R) then leaves psi in {-6, -5, -4}.
- **psi = -6:** the bd chain W_f0, R_B, O_v, R_0 (starts O-10, O-6, O, O+4).
- **psi = -5:** the shift-5 chain W_f0, R_B, O_v, R_0.
- **psi = -4:** phi0 = b-24 and R_A = [b-14, b-4]. Since a = b-15 and a+q = 15+beta' >= b-4 by (L2), R_A lies strictly inside L_w (equality would make b_w(a+q) an F_1 cut). Then R_A has no w.

Each case is a contradiction. QED

## 4. Result

In class (b) with d = 3, **the two-gap case (n_f + n_b = 5) is impossible**. What remains for d = 3 is n_f = n_b = 3 with exactly one gap row.

Still open:
- class (b): that case and d = 1;
- (a)-II: the v56 survivors (SHA256 `d1051179578875ea456550802ffe9c441b8d3c96b6d9bc3a6ce6f9627d4d77f9`) and the four/four shape at Sigma = 21;
- distinct 3+5;
- all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
