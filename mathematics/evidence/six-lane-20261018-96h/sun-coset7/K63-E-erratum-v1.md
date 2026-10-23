# K63-E-erratum-v1: repair of one weight in K63-E-v1 section 3 (C-ROW (b)) (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T01:07:41-0700.
- **Overlays:** `K63-E-v1.md`, sha256 73bcde10f4197ffc06c65107b5786ec9a03426c8ba86b7308343bfddac2d4de8 (frozen, unchanged).
- **Source of the finding:** parent full read (IRC at about 01:35 PDT); not yet a CLI review.

## J1: C-ROW (b), case k3 >= 3, remaining neighbours

The prescribed weights y_d = 1/3, y_p = 1/2 (p a remaining non-three with alpha_vp even) and y_u = 1/4 (a remaining
unmarked four u) are **infeasible when alpha_vp = 4 and the other remaining neighbour u has alpha_vu = 4** (k3 = 3): the
set {p, u, d} is allowed (gcd(lambda_p, lambda_u) = 4 >= 3; all pairwise gcds >= 2) and its sum is 1/2 + 1/4 + 1/3 =
13/12. **Repair:** in exactly this double-four case put y_p = 1/4. Then {p, u, d}: 1/4 + 1/4 + 1/3 = 5/6; {p, d}:
7/12; {p, u}: 1/2; no larger allowed set contains p (a set with a three and p or u has a gcd-1 pair). p still contributes
y_p alpha_vp = 1 unit, so the value remains >= k3 + 4/3 + (5 - k3) = 6 + 1/3. In every other case the weights of
K63-E-v1 stand (checked: alpha_vp = 2 with u in {1, 2, 4}, and alpha_vp = 4 with u in {1, 2}: every allowed set through p
has sum <= 1 because {p, u, d} is not allowed unless gcd(lambda_p, lambda_u) >= 3, i.e. unless both are fours).
Nothing else in K63-E changes.
