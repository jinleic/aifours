# Erratum 5 to proof-REFLHI-arcs-v5.md: the ONE consolidated review overlay

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T07:30:48-0700.  Overlay only; proof-REFLHI-arcs-v5.md
(4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c) is unchanged.  Written research; no computation.
Part I = required fixes from the reviews.  Part II = a NEW SINGLE-FAMILY proof branch (R >= 2p + 1), NOT accepted.
RUN/ = institute/runs/six-lane-2026-10-18-96h/.  Review inputs used:
* Foundation Claude review, RUN/review/olson-REFLHI-v5-foundation-claude-v1.prompt.note.md,
  300bebdaafb9864b7d4bddecc04d514799934f40af1f2d60d5319e9b3db26224: 0 FATAL / 0 MAJOR / 11 MINOR (F1-F11).
* Codex corollary review, RUN/review/olson-REFLHI-v5-corollaries-codex-v1.prompt.stdout.txt,
  7cf9cc103bb753dabc6e88c40c50d511e5ab4db742f7695477b172b949bb0880: 0 FATAL / 1 MAJOR / 1 MINOR, plus notes.
* Split freeze RUN/review/olson-REFLHI-v5-split-review-freeze-v1.json, 30d495949beb8a36f979a9996779eee070e504a63cbe837254c464e0c0b8c52c.
* The Claude corollary review returned no verdict (rc 143); nothing from it is used.

## 0. Governing relationship to v5 and errata 1-4

* Text of record: v5 read through erratum 1 (512e1d9e9a5dcdd4ad85840ce74d6d29ab8e1b8eb72db944ddff4a5683393331), erratum 2
  (b4451461bc6495e1b66588ddb762eb19ddd0428e8aad0c6b8fadc298476b8820), erratum 3
  (380106c91b0bcf250a8fd98583e75b39faf3d4c7d3ecd0eba2b2472bc15e669a), erratum 4
  (32811de59e1b5ca736a3db1a9b6592266dbcbcd8690cff27aa143b678e5907f1) and this erratum 5.  Where erratum 5 restates or
  replaces an item of v5 or of errata 1-4, erratum 5 governs; everything it does not mention stays as in v5 + errata 1-4.
* Erratum 1 (e1-e4): in force.  Erratum 2: e5 in force with the wording of I.7; e6 in force (record only).
  Erratum 3 (e7, e8): in force; the coverage sentences they correct are superseded by the exact coverage of I.14.
* Erratum 4: in force.  It GOVERNS Theorem SEG when Pi_need < 0 (R >= 2p + 1): there only the narrowed statement with
  Pi+ = max(0, Pi_need) is claimed; for Pi_need >= 0 it coincides with the printed statement.  For Pi_need < 0 the printed
  raw statement is unsupported by the v5 proof (it is not claimed false).  Part II below proves the printed statement for
  Pi_need < 0; it supersedes erratum 4's narrowing ONLY if the parent accepts it after a second-family review.
* No application uses Part II: every application of Theorem SEG has Pi_need >= 1 (SEG-p and MID: R = p; SEG-num: R = p + delta
  with 5 delta <= p - 10, so R <= 2p - 2); K2P+, TOP, FP and FP-1 do not use Theorem SEG.

## Part I. Required fixes

No theorem statement changes, except I.10 (ambient hypotheses of IIIb-X written out; scope unchanged) and I.11 (ETA
statement precisified).

**I.1 (F1; Lemma ARC+ (i)-(ii)).**  Replace "Several segments in one gap are inserted in their cyclic order; the same argument
applies to each." by: several segments may lie in one base gap.  A segment Sigma' != Sigma in the same base gap is a set of
consecutive blocks disjoint from the consecutive set Sigma, so it lies entirely before the first block of Sigma or entirely
after its last block, i.e. in the first or the last sub-gap created by the blocks c_1, ..., c_(2t') chosen in Sigma; these two
sub-gaps keep the base label.  Inserting the segments one at a time, (i) and the +-W formula of (ii) apply to every segment
with the sign eps of the base gap containing it.

**I.2 (F2; Lemma ARC+ (iii), hence also Lemma ARC).**  Add: (a) the base is an arc system, so m_b >= 1; (b) each U_j contains
0 (t'_j = 0), so every summand of the Cauchy-Davenport count is nonempty; (c) E+-, E- >= 0, so the common window
[-floor(E-/2), floor(E+/2)] contains 0; (d) if the Cauchy-Davenport count reaches p, the u-set is all of Z_p, and if the window
has >= p integers it contains every residue; in either case the two sets meet.  In every use in v5 the base has >= 2 arcs
(Theorem SEG and MID: |O| >= N_O - 2 = 2 m_lo >= 2; K2P+: >= N0 arcs; TOP: 2 m_0 arcs; FP-1: p - 1 arcs).

**I.3 (F3 and the Codex MINOR; Lemma SEG and the remark after it).**  Erratum 1 e1 stays in force.  In the induction step
write 2U'' := {sum_(j in J'') delta_j : J'' in [3, b' - 1] with at most t - 1 maximal intervals}; halving is a bijection of
Z_p, so |U''| = |2U''|.  The induction hypothesis is applied to the segment formed by blocks 3, ..., b' (b' - 2 >= 1 blocks,
consecutive differences delta_3, ..., delta_(b'-1), at most t - 1 intervals); for b' = 3 it is one block and U'' = {0}.  The
sets J' in {1, 2} used in A are realised by c = (), (1, 2), (2, 3), (1, 3) for J' = {}, {1}, {2}, {1, 2}; the last two use
block 3, which exists as b' >= 3.  J' u J'' has at most t maximal intervals (pieces may merge).  The conclusion is the clipped
bound  |U| - 1 >= g(t) := min(p - 1, 2t, b' - 1)  (equivalent to the printed min(p, 1 + min(2t, b' - 1))).
Replace the remark after Lemma SEG by: a segment's guaranteed gain is g(t), not the uncapped capacity b' - 1; while
2t < b' - 1 and g(t) < p - 1, one more inserted pair raises g by 2, except that the last pair before saturation raises it by
1 when b' - 1 is odd.

**I.4 (F4; Sec. 3 notation and Lemma 3.1).**  From Sec. 3 on write |M_i| for the number of blocks of M_i (v5's b_i) and
e_i = |M_i| - 1; b_t keeps its Sec. 1 meaning (number of rho_-1 letters of run R_t).  So C = {i : |M_i| = 1},
AB = {i : |M_i| = 2}, L = {i : |M_i| >= 3}, and "floor(b_i/2)" in K2P+ (c) and TOP reads floor(|M_i|/2).  An arc choice must
have sum_i c_i >= 2 (so that it is an arc system); Lemma 3.1 is stated for such choices.

**I.5 (F5; Lemma 3.2).**  Add: segments insert an even number of single-block arcs inside one reflection run, so every c_i mod
2, hence z and T, and hence E+-, are those of the base for all configurations.  The condition ceil(E_min/2) >= kappa + 1 - m
only gets easier as m grows and floor(E_max/2) <= p - m only gets easier as m shrinks, so it suffices to check the first at
m = m_b and the second at m = m_b + sum_j t_j.

**I.6 (F6; Lemma BAL).**  Add: WLOG T > d (replace z by -z).  If q = 1 then |T| = |d(N_1)| <= d, and if d = 0 then T = 0;
so T > d forces q >= 2.  The least t with S(t) >= (T - d)/2 has t >= 1 (S(0) = 0 < (T - d)/2) and t <= q - 1, because
S(q - 1) = T - z_i d(N_i) >= T - d > (T - d)/2.  For it S(t - 1) < (T - d)/2 <= S(t) <= S(t - 1) + d < (T + d)/2, so
|T - 2 S(t)| <= d, and i' := i + t != i.

**I.7 (F7; realisation rule).**  v5 L107-108 is superseded by erratum 2 e5 (the printed sentence offers no move when M_j is
covered by arcs of >= 3 blocks).  Read the last sentence of e5 as: "Each of the three moves realises the parity change when
it is applicable; the order given is one sufficient choice."  In particular the move of K2P+ (f), adding a singleton on an
unused block of M_i even if M_i already carries a singleton, is valid: the parity flips, the arc count rises by 1, and no
pair is lost.

**I.8 (F8; Sec. 4 and Theorem FP).**  (a) The Sec. 4 data and Theorem FP are stated for w in setting (S) with R = p that
avoids.  (b) Balanced labelling, written out: apply Lemma BAL at i = n to the choice c^(n) (c_n = 0, c_j = 1 for j != n, each
arc a whole run M_j; sum p - 1, even).  Its two parity changes (add M_n as one arc; remove the arc M_(i')) give c^(i'), i.e.
the labelling z^(i'), with |T| <= d = 1; T is odd, so |T| = 1.  (c) If B = 0 every nonempty run is one rho_1 and
T(n) = (p + 1)/2 - (p - 1)/2 = 1 for every n (v3 L119-120).  (d) The Sec. 4 subsumption sentence is replaced by I.14.

**I.9 (F9; Theorem K2P+).**  Erratum 1 e2 stays in force; directly, at p = 5, H <= (p - 3)/2 = 1 contradicts H - delta >= 2.
Step (d) written out.  Pi* <= N0: from 2 kappa >= R + 1 and 2 ceil((R - d)/4) <= (R - d + 3)/2 <= (R + 3)/2,
N0 = 2 kappa + 4 - 2 ceil((R - d)/4) >= (R + 7)/2, while Pi* = p + 1 - ceil(R/2) <= p + 1 - R/2; so N0 - Pi* >= R - p + 5/2 > 0.
N0 + Pi* <= k - 1: with 2 kappa = k - 2p + R, N0 + Pi* = k - p + 5 + [R - 2 ceil((R - d)/4) - ceil(R/2)], the bracket is
<= R - (R - d)/2 - R/2 = d/2, and d <= p - 6 gives N0 + Pi* <= k - p/2 + 2 <= k - 1 (p >= 7).  Step (f): the final arc count
is N0 (no change needed, or the change at i' removes an arc) or N0 + 2 (it adds one), so m in {m_lo + 1, m_lo + 2}, inside
[m_lo, m_hi] by (a); the printed range [N0 - 2, N0 + 2] is a harmless superset.

**I.10 (F10; Corollary IIIb-X; scope unchanged).**  Statement with its ambient hypotheses: let p >= 7 be prime and w a word of
length 4p - 2 over D_(2p) whose rotation letters are all equal to one rho_x, x != 0 (B = 0 after normalisation), with exactly
R = p rotation letters, kappa = (p + 1)/2, and every maximal cyclic constant reflection block of odd length.  Then w has an
identity 2p-subword in increasing index order.  Proof: k = 2p - R + 2 kappa = 2p + 1 by (0.1) (a consequence, not a
hypothesis), and 2p + 1 >= 3 kappa + 3 = (3p + 9)/2 iff p >= 7; Theorem K2P+.  The foundation reviewer's remark that B = 0 is
not needed is recorded; the stated B = 0 scope of IIIb-X is not changed (the any-B statement is K2P+ itself).

**I.11 (F11; Theorem ETA, statement precisified).**
Statement.  Let w be in setting (S) with B = 0 and R <= 2 kappa + 1, so m* := kappa + 1 - floor(R/2) >= 1.  Choose the cyclic
start so that the run R_1 is nonempty if R is odd (any start if R is even); index the blocks S_1, ..., S_k from there, put
rho_j := r_1 + ... + r_j, eta_j := y_j/2 + rho_j in Z_p, and for a set Z of blocks eta(Z) := {eta_j : j in Z} (a set of
residues).  If w avoids, then for every partition of {1, ..., k} into 2m* nonempty consecutive segments Z_1 < ... < Z_(2m*)
(linear order), sum_i |eta(Z_i)| <= p + 2m* - 2.  (Such partitions exist: k - 2m* = 2p - 2 - [R odd] >= 0.)
Proof details.  For a_i in Z_(2i-1), b_i in Z_(2i), P := union over i of the runs R_(a_i + 1), ..., R_(b_i): the intervals are
nonempty, consecutive ones are separated by R_(b_i + 1), ..., R_(a_(i+1)), and the wrap-around gap contains R_1, so
m(P) = m* and P is proper.  With B = 0, x := E+(P) = D_P = sum_i (rho_(b_i) - rho_(a_i)), and u_P - D_P =
sum_i (eta_(a_i) - eta_(b_i)).  "G_(m*)" in v5 means gamma_(m*), evaluated directly (not by Fact 2.1):
gamma_(m*)(E) = min(H + floor(R/2), E - floor(R/2), floor(E/2)), as E - kappa + m* - 1 = E - floor(R/2) and
p - m* = H + floor(R/2).  The window I(P) = [-gamma_(m*)(R - x), gamma_(m*)(x)] is:
  R even, 0 <= x <= R: {x - R/2};   R odd, 1 <= x <= R - 1: {x - ceil(R/2), x - floor(R/2)};
  R odd, x = 0: {-floor(R/2)};      R odd, x = R: {floor(R/2)} (which misses x - floor(R/2)).
If R is odd, R_1 is nonempty and not in P, so x <= R - 1.  Hence x - floor(R/2) lies in I(P) in every case, and avoidance
(Lemma W) forbids sum_i (eta_(a_i) - eta_(b_i)) = -floor(R/2) (mod p).  These sums form the sumset
eta(Z_1) - eta(Z_2) + ... - eta(Z_(2m*)), which by (CD) has >= min(p, sum_i |eta(Z_i)| - 2m* + 1) residues; it misses one, so
sum_i |eta(Z_i)| - 2m* + 1 <= p - 1.  []

**I.12 (Codex MINOR; Theorem SEG proof, and Corollary MID).**  In Theorem SEG replace "Lower the t_j minimally keeping total
gain >= Pi_need: sum t_j <= Pi_need" by the following.  An optional pair is two single-block arcs and raises m by one; a base
pair-arc is one arc.  The certified gain of a configuration family is G_b + sum_j g_j(t_j), G_b := number of base pair-arcs,
g_j(t) := min(p - 1, 2t, b'_j - 1) (I.3).
* Pi_need >= 1.  By Fact 2.2 (R >= p), Pi_need <= (p - 1)/2.  Start with all t_j = 0; while the certified gain is < Pi_need,
  raise by one some t_j with 2t_j < b'_j - 1.  Such a j exists: if every t_j is saturated, either some g_j = p - 1 >= Pi_need, or
  sum_j g_j equals the uncapped capacity and G_b + sum_j g_j = g_E - |L n O| >= Pi_need by (H3).  Each step raises the certified
  gain by >= 1: before it, g_j(t_j) <= (certified gain) < Pi_need <= (p - 1)/2, so g_j(t_j) = 2t_j, and after it
  g_j >= min(p - 1, 2t_j + 1) = 2t_j + 1.  Hence the loop stops after at most Pi_need - G_b <= Pi_need steps: sum_j t_j <= Pi_need.
* Pi_need = 0 (R in {2p - 1, 2p}).  Take all t_j = 0.  (H1) gives m_hi >= m_lo + 1, so m_b in {m_lo, m_lo + 1} lies in
  [m_lo, m_hi], and the window sum floor(E+/2) + floor(E-/2) >= ceil(R/2) - 1 = p - 1 already.
* Pi_need < 0 (R >= 2p + 1).  Erratum 4 governs; Part II is the new branch.
The lower window condition at m = m_b uses m_lo = max(1, kappa + 1 - ceil((R - d)/4)) >= kappa + 1 - ceil((R - d)/4) (both
branches).  In Corollary MID (with erratum 1 e3) read every segment gain as clipped: the first pair of a segment with >= 3
blocks gains min(p - 1, 2, b' - 1) = 2, a surviving base pair-arc gains 1, and afterwards each useful step adds >= 1 until
Pi_need = (p - 1)/2 < p - 1 is reached; so sum_j t_j <= Pi_need - 1 as stated.

**I.13 (Codex note; Corollary SEG-num: the maximum in m_lo is inactive).**  Under the hypotheses of SEG-num an avoider has
m_lo >= 2.  If delta >= 1: kappa >= (p + 3 delta + 2)/4 = (R + 2 delta + 2)/4 >= R/4 + 1, so kappa >= ceil(R/4) + 1 >=
ceil((R - d)/4) + 1.  If delta = 0: d = 1 (v5 Sec. 4 data), ceil((p - 1)/4) = r, and kappa >= ceil((p + 2)/4) = r + 1 (p = 4a + 1:
a + 1; p = 4a + 3: a + 2).  So m_lo = kappa + 1 - ceil((R - d)/4) >= 2 and m_hi - m_lo = H - (floor((R + d)/4) -
ceil((R - d)/4)) >= H - floor(d/2) >= p - 1 - kappa - delta.  The printed parenthetical "(or more if m_lo = 1)" is WITHDRAWN:
the maximum with 1 can only shrink m_hi - m_lo, and the corollary does not use it.  Ranges: the exact integer nonemptiness
condition is ceil((p + 3 delta + 2)/4) <= floor((p - delta - 4)/2) (5 delta <= p - 10 is only necessary; e.g. no integer cell at
p = 11, delta = 0, where SEG-p covers); the covered k = p - delta + 2 kappa satisfy k = R (mod 2).

**I.14 (Codex coverage; replaces the v5 Sec. 4 subsumption sentence, the Sec. 6 closing statement and the Sec. 8 "Excluded"
line, as modified by e7 and e8).**  Exact universal coverage of this file for all-odd words with rotations in one pair (any
B), among residual cells kappa >= 2:
| R = p | excluded kappa | not excluded |
|---|---|---|
| p = 5 | 4 (TOP argument, e7) | 2 (excluded only under the FP-1 diversity hypothesis), 3 |
| p = 7 | 2 (SEG-p), 4 (K2P+), 5, 6 (TOP) | 3 (excluded only under the FP-1 diversity hypothesis) |
| p = 11 | 3, 4 (SEG-p), 5 (MID), 6-8 (K2P+), 9, 10 (TOP) | 2 |
| p >= 11 | ceil((p + 1)/4), ..., (p - 3)/2 (SEG-p); (p - 1)/2 (MID); (p + 1)/2, ..., p - 3 (K2P+); p - 2, p - 1 (TOP) | 2 <= kappa < ceil((p + 1)/4) |
For R = p + delta, delta >= 1: the integer bands ceil((p + 3 delta + 2)/4) <= kappa <= floor((p - delta - 4)/2) (SEG-num) and
ceil((p + delta + 1)/2) <= kappa <= p - delta - 3 (K2P+: k = p - delta + 2 kappa >= 2p + 1 and k >= 3 kappa + 3) are excluded;
further words are excluded when they satisfy the hypotheses of Theorem SEG or the FP-1 diversity conditions.

**I.15 (Codex note; Corollary TOP, exact arc count).**  With g := Pi_need + 2 = (p + 3)/2: 2m_0 - g >= 1 (room for the designated
singleton) and 2m_0 + g = k + (7 - p - 4r)/2 <= k.  This identity replaces the printed justification "(p + 5)/2 + 2 - 2r <= p".
If |M_l| is odd, the singleton fits beside floor(|M_l|/2) pairs of M_l; if |M_l| is even (>= 4), one pair of M_l is given up
(e4) and a pair still remains in M_l.  The two compensating moves at l (delete the singleton if the change at i' adds an arc,
split the designated pair if it removes one) keep the count exactly 2m_0 and lose at most two pairs in total.

## Part II. NEW SINGLE-FAMILY: Theorem SEG for Pi_need < 0 under its printed hypotheses (NOT accepted)

Status: new proof branch, first written by the Codex corollary reviewer (7cf9cc10...0880, Sec. 3, lines 83-147), re-derived
here step by step; the parent reported checking its algebra.  It is reviewed by one model family only and is NOT accepted.
It supersedes erratum 4's narrowing only after a second-family review and a parent verdict.  No application uses it.
**Claim.**  Theorem SEG holds as printed when Pi_need < 0 (i.e. R >= 2p + 1): an avoider in setting (S) with (H1)
m_hi - m_lo >= Pi_need + 1 and (H2) n_CA >= 2 m_lo + 2 does not exist.  (H3) is not used.
Proof.  Put l := m_lo, c := ceil(R/2) >= p + 1, a := ceil((R - d)/4), b := floor((R + d)/4); so m_hi = p - b and
Pi_need = p - c.  (H1) reads c - b >= l + 1.  Since a >= (R - d)/4 and b >= (R + d)/4 - 3/4, the integer a + b is
>= R/2 - 3/4, hence a + b >= c - 1; so a >= c - 1 - b >= l.  If l >= 2, then l = kappa + 1 - a <= kappa + 1 - l, so
2l <= kappa + 1 <= p and l <= (p - 1)/2 (p odd); if l = 1 this bound is trivial.
Build and balance the base exactly as in the printed proof (O_0 inside C u AB of size N_O = 2l + 2 by (H2); Lemma BAL; final O
with |O| in {N_O - 2, N_O}), and add no segments.  The base has m in {l, l + 1}, so 1 <= m <= (p + 1)/2, and |T| <= d.
Put f+- := floor(E+-/2).  Then f+ + f- >= c - 1 >= p (Lemma 3.2's computation) and max(f+, f-) <= b (E_max <= (R + d)/2), so
min(f+, f-) >= c - 1 - b >= l >= m - 1.  The lower condition of Fact 2.1 holds: ceil(E_min/2) >= a >= kappa + 1 - l >=
kappa + 1 - m.  Hence E - kappa + m - 1 >= floor(E/2) for E = E+-, and gamma_m(E+-) = min(p - m, f+-).  Their sum is >= p - 1:
with no clipping it is >= p; with one clipped term it is >= (p - m) + (m - 1) = p - 1; with both clipped it is
2(p - m) >= p - 1 as m <= (p + 1)/2.  So the common window of the base patterns has >= p integers and contains every residue;
any base pattern (Lemma 2.1) then gives an identity 2p-subword by Lemma W, a contradiction.  []
Shape remark (Codex): the hypotheses (H1)-(H3) admit Pi_need < 0 together with m_lo > m_hi, e.g. the shape parameters p = 11,
R = 25, kappa = 10, d = 3, q = 13 with nine C-runs and four AB-runs (m_lo = 5, m_hi = 4, Pi_need = -2); this is a shape
observation only, no avoidance claim.  In that regime the printed floor-window argument is unavailable, which is why the
branch uses the clipped endpoints gamma_m(E+-) = min(p - m, f+-).

## Scope and what is not covered

Ambient conditions of every claim (foundation review, Sec. C): p >= 5 prime; cyclic w of length 4p - 2 over D_(2p); rotation
letters in one pair {rho_x, rho_-x}, x != 0, normalised to x = 1 and A >= B; every maximal cyclic constant reflection block odd;
F, R >= 1; maximal decomposition (empty runs genuine); no purity, no B < kappa, no restriction on values.  Per-claim scopes
are those of the foundation review Sec. C, with I.10 and I.11.
Not part of this overlay (separate files, not in any current review set): proof-REFLHI-arcs-v5-addendum-SEGk-v2.md,
proof-REFLHI-transfer-v2.md, proof-REFLHI-regionB-v2.md and its addendum B'.
OPEN: REFL(p), REFL-HI(p), RES-HI(p), the reflection half of INV*(p), INV*(p), ordered Olson for D_(2p).  No novelty, Lean or
human-review claim.
