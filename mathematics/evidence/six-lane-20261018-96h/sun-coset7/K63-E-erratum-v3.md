# K63-E-erratum-v3: C-ROW (b) k3 >= 3 five-exclusion certificate, apex v = p, imports (no statement change)

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T02:04:19-0700.
- **Overlays:** `K63-E-v1.md` (sha256 73bcde10f4197ffc06c65107b5786ec9a03426c8ba86b7308343bfddac2d4de8), `K63-E-erratum-v1.md` (sha256 b5d07d06f50f44262985553ece0101268f523a0c53edf18fdaca924e52968480; time label withdrawn by
  `evidence/timing-addendum-v1.md`, sha256 030192f2e21f7d3a46c4f73f90e40310327326ef912612eff7ac1f4b812ba5d7) and `K63-E-erratum-v2.md` (J2, sha256 20fb0b0a68a3996d41f9991e9a28eeaeb77c24097d1c82290165c2870c6f601c). All frozen.
- **Source:** hostile reviews RUN/review/sun7-three-written-codex-v1.prompt.stdout.txt (Codex MAJOR D1) and RUN/review/sun7-three-written-claude-v1.prompt.note.md (Claude MINORs), relayed by the parent.

## J3 (Claude MINOR E-1): C-ROW (b), k3 >= 3
**Defect.** The parenthetical "a five would have been killed by y = 1/k5 + others" is not a certificate as written:
with y_d = 1/3 kept, in Sd (h_d >= 1) with k3 = 4 and one five f, {d, f} sums to 4/3; in Sp with p a three,
{p, f} sums to 1/3 + 1.
**Replacement.** "No C-neighbour of v has alpha_vc = 5 here. In S0 and Sp (h_d = 0) this is J2 item 1: y_d = y_f = 1
gives 2 alpha_vd + 5 = 9 units. In Sd (h_d >= 1, so every C-vertex is unmarked): y = 1/3 on the threes, 1/k5 on the
fives, y_d = 0, all other weights 0; threes (labels 3 w) and fives (labels 5 w) share no prime, sets of threes have
size <= 3 and sets of fives size <= 5, so the weights are feasible, and the value is >= k3 + 5 >= 8 units."
J2's sentence "The other k3 cases of K63-E-v1 and the repair J1 of erratum v1 are unchanged" is amended to: "...are
unchanged, except that the k3 >= 3 five-exclusion parenthetical of C-ROW (b) is replaced by J3."

## J4 (Claude MINOR E-2): the apex v = p
J2 items 2-4 presuppose v != p. If v = p, then v has no marked C-neighbour (the 3-marker is on d and the 5-marker on
v), and every C-five f has lambda_f = 5 w_f coprime to lambda_d (h_d = 0), so J2 item 1 removes all fives; the R3 and
R5 weights then overlap nothing and the original arguments of C-ROW (a) and (b) apply verbatim with v = p.

## J5 (Claude MINOR E-3): imports
As in `K63-D-erratum-v2.md` H5: the ROW-U standard weights and the min(N, 4) bound are used in the subset form of the
accepted K63-U0 Step 1 and LFC-erratum E8, not through ROW-U-deg of `K7-M1-erratum-v1.md` F3.

Theorem K63-E is unchanged.
