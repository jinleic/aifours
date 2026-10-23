# K63-E-erratum-v2: J2, the k3 <= 2 cases of C-ROW when the 5-marked C-vertex p is a three (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:17:10-0700.
- **Overlays:** `K63-E-v1.md` (sha256 73bcde10f4197ffc06c65107b5786ec9a03426c8ba86b7308343bfddac2d4de8) and `K63-E-erratum-v1.md` (sha256 b5d07d06f50f44262985553ece0101268f523a0c53edf18fdaca924e52968480); both frozen. The time label
  in erratum v1 is withdrawn by `evidence/timing-addendum-v1.md`.
- **Source of the finding:** parent full read, received by IRC before this file was created.

## J2: C-ROW (a) and (b), cases k3 in {1, 2}, when p exists

**Defect.** If p (the C-vertex with h >= 1) exists and alpha_vp = 3, p is a three whose label 3 * 5^(h_p) w_p * ...
also shares the prime 5 with any unmarked five; then the R3 weights (1/k3 on the threes) and the R5 weights (1/k5 on
the unmarked fives) can both be positive on an allowed pair {p, five}, so the certificate "as in (a)" is not
automatically feasible.

**Repair (checked independently).** If p exists then h_d = 0 (at most one vertex has h >= 1), so
lambda_d = 3^(F_d) w_d alpha_vd with alpha_vd in {1, 2} has no prime 5.
1. *No C-five at v.* Any C-neighbour f with alpha_vf = 5 (unmarked, label 5 w_f, or p, label 5^(h_p + 1) w_p) has a
   label coprime to lambda_d. Put y_d = y_f = 1 and 0 elsewhere: no allowed set contains both (Sun(2)), every other set
   meets at most one of them, so y is feasible, and the value is 2 alpha_vd + 5 >= 7. So no C-entry at v equals 5.
2. *k3 = 1 and the only three is p.* With no fives, p's label 3 * 5^(h_p) w_p shares no prime with the four unmarked
   labels (alphas in {1, 2, 4}): y_p = 1 adds 3; standard weights on the four unmarked add min(4, 4) = 4; y_d = 0.
   Value >= 7.
3. *k3 = 2 with p and one unmarked three.* y = 1 on the unmarked three (its allowed sets through p or d have y = 0
   elsewhere) adds 3; the other three unmarked C-neighbours (alphas in {1, 2, 4}) add >= min(3, 4) = 3 with standard
   weights; y_p = y_d = 0. Value >= 6.
4. *k3 in {1, 2} with p not a three.* Then p's label 5^(h_p) w_p alpha_vp (alpha_vp != 3, and != 5 by item 1) shares no
   prime with the threes, and there are no fives, so the R3 weights do not overlap anything else; the original argument
   of K63-E-v1 section 3 (a) (and its use in (b)) stands as written.
These cover both C-ROW (a) and C-ROW (b), because item 1 holds for alpha_vd = 1 and alpha_vd = 2 alike. When p does not
exist the original text has no overlap issue (no C-vertex carries a 5 except through alpha = 5 itself, and R3/R5 are
then disjoint classes). The other k3 cases of K63-E-v1 and the repair J1 of erratum v1 are unchanged; Theorem K63-E is
unchanged.
