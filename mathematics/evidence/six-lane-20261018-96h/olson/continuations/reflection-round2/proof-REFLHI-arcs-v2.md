# Reflection half for o_F > p: arc systems, Cauchy-Davenport kills, and a new high-k exclusion (candidate v2)

Owner OlsonReflectionSuccessor (Slice B of R18/olson-two-slice-successor-brief-v1.md).  Written after host clock
2026-10-19T05:25:39-0700.  Status: CANDIDATE_UNVERIFIED (written research only; no computation; no model review).
Supersedes the unsent partial draft proof-REFLHI-tools-v1.md (79741c7c...7a6e, kept unchanged; its Lemma RW proof is
garbled and RW is not used here).  Scope: words of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0.  No claim about rotation values, INV*(p) as a whole, ordered Olson, Lean, novelty or priority.

Paths: REFL/ = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/;
R16/ = institute/runs/six-lane-2026-10-16/review/; R18/ = institute/runs/six-lane-2026-10-18-96h/review/.

## 0. Imports (parent-accepted, at their exact scopes; hashes re-checked 2026-10-19 03:5x PDT)

* (H0) Lemma H0, REFL/proof-K0star-r2.md (6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1) L55-65;
  valid for every cyclic constant-block representation of any length.  Accepted in R16/olson-reflection-K0star-RED-
  parent-verdict-v1.md (879aeee7...c02a) as algebra on the accepted GRX.
* (P0) Fact (P0) of the same file (Sec. 1, "Facts for G-avoiders of length 4p - 2"): e_R <= e_F + 2 kappa, empty runs
  counted as even rotation runs (from the accepted Theorem P).  Also (Z0): an avoider has A, B <= 2p - 1 and, after the
  normalisation A >= B, B <= kappa.
* (RED) REFL/proof-RED-r2.md (c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7), Theorem RED and its
  proof, with (I1)-(I4), K0*, K1* and the lemmas named there, same verdict.
* (SMALLK) R16/olson-reflection-smallk-parent-verdict-v1.md: RES_<(p) has no avoider with k <= p.
* (FEW) REFL/proof-REFL-fewodd-r5.md (4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363; verdict
  R16/olson-refl-fewodd-parent-verdict-v1.md binds the errata-equivalent r4 1e447754...861d), Claim MON.
* (CD) Cauchy-Davenport: for nonempty A_1, ..., A_s in Z_p, |A_1 + ... + A_s| >= min(p, sum |A_i| - s + 1).
Not used: rotation rigidity, INV*, SLZ3, RED-r3, K0star-r3, any finite computation.

## 1. Frozen target and the exact residual

**REFL-HI(p).**  For prime p >= 5, every avoider w0 of length 4p - 2 over D_(2p) whose rotation letters lie in one set
{rho_x, rho_-x}, x != 0, and with o_F(w0) >= p + 1 (o_F = number of ODD blocks of the maximal cyclic CONSTANT reflection
block decomposition, not of maximal reflection runs) has every maximal cyclic reflection run constant.
(FEW) and REFL-HI(p) together are REFL(p) of REFL/README.md L17-19.
**RES-HI(p)** := RES_<(p) (RED-r2 L132-133) has no avoider with kappa >= 2 and k >= p + 1.
**Lemma 1.1.**  RES-HI(p) implies REFL(p).
Proof.  A violating word is turned by the proof of Theorem RED into an avoider of RES_<(p) with kappa >= 2; by (SMALLK)
it has k >= p + 1.  []
Status: RES-HI(p) is OPEN.  This file proves new exclusions inside it (Secs. 4-5) and records the remaining family
(Sec. 6).

## 2. Setting and windows

Setting (S): p >= 5 prime; w a cyclic word R_1 S_1 ... R_k S_k (run R_t precedes block S_t, indices mod k) of length
4p - 2 with F, R >= 1, rotations in {rho_1, rho_-1}, A >= B, every maximal constant block S_t = sigma_(y_t)^(l_t) of ODD
length (so beta(P) = 0 for every pattern), empty runs genuine (y_(t-1) != y_t).  kappa = p - 1 - H, g := kappa - B,
D = A - B, d_t = a_t - b_t, u_t = (y_(t-1) - y_t)/2 in Z_p, R = 2p - k + 2 kappa (all blocks odd).
**Lemma W.**  w avoids iff 0 notin I(empty) (mod p) and, for every proper nonempty pattern P with m = m(P) maximal
cyclic intervals, u_P := sum_(t in P) u_t is not congruent to an element of
   I(P) = [-G_m(D - D_P), G_m(D_P)],   G_m(x) := min(p - m, x - g + m - 1, floor((x + B)/2)).
Proof.  (H0) with beta = 0 and kappa - B = g.  []
For B = 0: G_m(x) = min(p - m, x - kappa - 1 + m, floor(x/2)), and for integers x, the middle term is <= floor(x/2)
iff ceil(x/2) <= kappa + 1 - m (*).

## 3. Arc systems (new)

An **arc** is a nonempty set X of cyclically consecutive blocks S_j, ..., S_(j+l) such that every run strictly inside it
(R_(j+1), ..., R_(j+l)) is EMPTY; V(X) := {y_j, ..., y_(j+l)} and nu(X) := |V(X)|.  An arc with an internal run has
nu >= 2 (genuineness).
An **arc system** is a family of 2m >= 2 pairwise disjoint arcs, listed in cyclic order X_1, Y_1, X_2, Y_2, ..., X_m, Y_m.
The **gap** after an arc is the set of runs and blocks strictly between its last block and the first block of the next
arc; it contains at least one run (the run following the arc's last block).  Gaps after X_i are IN-gaps, gaps after Y_i
are OUT-gaps.  E_in := sum of d_t over the runs of all in-gaps.
**Lemma 3.1.**  For blocks a_i in X_i, b_i in Y_i (indices of blocks), let J_i be the run interval R_(a_i + 1), ...,
R_(b_i) and P := J_1 u ... u J_m.  Then P is a proper nonempty pattern with exactly m maximal intervals, D_P = E_in, and
u_P = (1/2) sum_i (y_(a_i) - y_(b_i)).
Proof.  J_i consists of the internal (empty) runs of X_i after a_i, all runs of the in-gap after X_i, and the internal
(empty) runs of Y_i up to b_i; it is a nonempty cyclic interval.  The runs of each out-gap, and the internal runs of Y_i
after b_i and of X_(i+1) up to a_(i+1), lie in no J_i; every out-gap has a run.  So the J_i are the maximal intervals of P,
P != [k], and m(P) = m.  Empty runs have d = 0, so D_P = E_in.  theta telescopes: sum over R_(a+1), ..., R_b of
(y_(t-1) - y_t)/2 = (y_a - y_b)/2.  []
**Lemma ARC.**  In setting (S), let an arc system with 2m arcs and in-mass E := E_in satisfy
   G_m(E) + G_m(D - E) >= 0   and   sum over the 2m arcs of (nu - 1)  +  G_m(E) + G_m(D - E)  >=  p - 1.
Then w has an identity 2p-subword.
Proof.  By Lemma 3.1 every choice (a_i, b_i) gives a pattern with the same m and D_P = E, hence the same window
I := [-G_m(D - E), G_m(E)] (Lemma W).  The values u_P form a set containing the sumset
(1/2)V(X_1) - (1/2)V(Y_1) + ... + (1/2)V(X_m) - (1/2)V(Y_m) of 2m sets of sizes nu; by (CD) it has at least
min(p, 1 + sum(nu - 1)) residues.  I has min(p, G_m(E) + G_m(D - E) + 1) residues.  The hypothesis makes the two sizes
add up to more than p, so some u_P is congruent to an element of I, and Lemma W gives an identity 2p-subword.  []
Remarks.  (1) Constant (single-block) arcs contribute nothing to the sum but count in m.  (2) Lemma TOG of the v1 draft
(regions of empty runs added to a fixed pattern) is the special case in which the arcs inside an out-gap form the
added regions; it is not needed below.

## 4. The cell R = p with B = 0 (all rotation letters equal, exactly p of them)

**Lemma 4.1 (structure).**  In setting (S) with B = 0 and R = p, if w avoids then every nonempty run consists of exactly
one rho_1, there are p nonempty and 2 kappa empty runs, k = p + 2 kappa, and w has exactly p maximal reflection runs
M_1, ..., M_p (M_i between the i-th and (i+1)-st nonempty run); if e_i is the number of (empty) runs inside M_i, then
sum e_i = 2 kappa.
Proof.  k = 2p - R + 2 kappa = p + 2 kappa.  (P0) with e_F = 0 gives e_R <= 2 kappa, so the number o_R of odd runs is
>= k - 2 kappa = p = R.  Odd runs have >= 1 letter, so o_R = p, each odd run is a single rho_1, and no even run is
nonempty.  Maximal reflection runs alternate with the p nonempty rotation runs; each M_i is an arc.  []
Put x_- := (p - 1)/2, x_+ := (p + 1)/2, m_0 := max(1, kappa + 1 - ceil(x_-/2)), m_1 := p - floor(x_+/2).  Then
m_0 <= m_1 (as kappa + 1 <= p and ceil(x_-/2) = floor(x_+/2) + [p = 3 mod 4] - [p = 3 mod 4] ... precisely: for
p = 4q + 1, ceil(x_-/2) = floor(x_+/2) = q; for p = 4q + 3, both are q + 1), and floor(x_-/2) + floor(x_+/2) = (p - 1)/2.
**Theorem FP.**  Let w be as in setting (S) with B = 0 and R = p, and suppose w avoids.  Fix i_0 in [p] and choose,
inside each maximal reflection run M_i, pairwise disjoint arcs, an ODD number of them for i != i_0 and an EVEN number
(possibly 0) for i = i_0, 2m arcs in all with m_0 <= m <= m_1.  Then the sum of (nu - 1) over all chosen arcs is at most
(p - 3)/2.
Proof.  Suppose the sum is >= (p - 1)/2.  The chosen arcs, in cyclic order, form an arc system (disjoint arcs; every gap
contains a run).  Labels IN/OUT alternate along consecutive gaps.  The p single-rho_1 runs N_1, ..., N_p lie in gaps;
N_i and N_(i+1) are separated exactly by the arcs inside M_i, so they lie in gaps of different labels iff the number of
arcs in M_i is odd.  Hence the labels of N_(i_0 + 1), N_(i_0 + 2), ..., N_(i_0) (cyclically, p of them) alternate p - 1
times and the first equals the last: (p + 1)/2 of them carry one label and (p - 1)/2 the other.  So
E = E_in in {x_-, x_+} and D - E = p - E is the other value.  For x in {x_-, x_+} and m_0 <= m <= m_1: by (*),
ceil(x/2) >= ceil(x_-/2) >= kappa + 1 - m gives that the middle term is >= floor(x/2); and p - m >= floor(x_+/2) >=
floor(x/2).  So G_m(x) = floor(x/2) and G_m(E) + G_m(p - E) = (p - 1)/2 >= 0.  The sum condition of Lemma ARC reads
(p - 1)/2 + (p - 1)/2 >= p - 1: true, so w does not avoid, a contradiction.  []
**Corollary FP-1 (new exclusion).**  Let p >= 5 be prime and w an all-odd G-word of length 4p - 2 whose rotation
letters are all equal (B = 0 after normalisation) and number exactly R = p.  If
   kappa <= (p - 3)/2 + ceil((p - 1)/4)                                                                  (K)
and at least (p - 1)/2 of the p maximal cyclic reflection runs of w are non-constant, then w has an identity 2p-subword.
Proof.  If w avoided, Lemma 4.1 applies.  If some M_(i_0) is constant (a single block), choose it; otherwise any i_0.
For i != i_0 take ONE arc in M_i: the two blocks around one internal (empty) run if M_i is non-constant (nu = 2), else
its single block.  Then 2m = p - 1, and m = (p - 1)/2 lies in [m_0, m_1]: m >= kappa + 1 - ceil(x_-/2) is (K), and
(p - 1)/2 <= p - floor(x_+/2).  The sum of (nu - 1) is the number of non-constant M_i with i != i_0, which is >= (p - 1)/2
(if a constant run exists it is M_(i_0); otherwise all p runs are non-constant and the count is p - 1).  Theorem FP gives
a contradiction.  []
Scope of FP-1 inside RES-HI: a word of RES_<(p) with B = 0 and R = p has k = p + 2 kappa >= p + 4, so it is in the
high-k residual; (K) allows every kappa up to about 3p/4 (kappa <= (p - 3)/2 + ceil((p - 1)/4)).  Lemma 4.1 also shows
that such a word has at least kappa non-constant... (not used).
**Corollary FP-2 (transfer to REFL).**  Let w0 be an avoider of length 4p - 2 whose rotation letters are all equal to one
rho_x, x != 0, with exactly p of them, all of whose maximal constant reflection blocks are odd, with kappa(w0)
satisfying (K) and with at least (p - 1)/2 non-constant maximal cyclic reflection runs.  Then w0 does not exist.
(Equivalently: such an avoider would have to have every reflection run constant, which the hypothesis excludes; so these
words are never avoiders.)
Proof.  w0 is in setting (S) with B = 0 and R = p (normalise x = 1); apply FP-1.  []

## 5. A general consequence for B = 0, R <= 2 kappa + 1 (structure, proved)

**Theorem ETA.**  In setting (S) with B = 0 and R <= 2 kappa + 1 put m* := kappa + 1 - floor(R/2) >= 1 and, for a block
index j counted linearly from a chosen run R_1, eta_j := y_j/2 + r_1 + ... + r_j (in Z_p).  If w avoids, then for every
partition of the blocks into 2m* nonempty cyclically consecutive arcs-of-blocks Z_1, ..., Z_(2m*) in cyclic order, Z_1
starting at block 1 (here "arcs-of-blocks" may contain nonempty runs), with r_1 >= 1 when R is odd,
   sum_(i = 1..2m*) |eta(Z_i)| <= p + 2 m* - 2.
Proof.  For a choice a_i in Z_(2i-1), b_i in Z_(2i) let P := union of the run intervals R_(a_i + 1), ..., R_(b_i).  As in
Lemma 3.1, P has exactly m* intervals (run R_1 and the runs after b_i up to a_(i+1) are outside P), and
u_P - D_P = sum_i (eta_(a_i) - eta_(b_i)) (telescoping, B = 0 so D_P = R_P).  For B = 0 and m = m*:
if R is even, G_(m*)(x) = x - R/2 for 0 <= x <= R (by (*) and p - m* >= R/2), so I(P) = {D_P - R/2}; if R is odd,
G_(m*)(x) = x - (R - 1)/2 for 0 <= x <= R - 1 and G_(m*)(R) = (R - 1)/2, so D_P - (R - 1)/2 lies in I(P) whenever
D_P <= R - 1, which holds as R_1 notin P and r_1 >= 1.  Avoidance therefore forbids sum_i (eta_(a_i) - eta_(b_i)) =
-floor(R/2) for all choices.  By (CD) the set of these sums has at least min(p, sum |eta(Z_i)| - 2m* + 1) elements and
misses a residue, whence the bound.  []
Comment.  In particular, when R = 2 kappa (m* = 1) every 2-arc split satisfies |eta(Z_1)| + |eta(Z_2)| <= p: the
sequence eta is highly repetitive on every split.  This is a necessary condition for the IIIb residual, not an exclusion.

## 6. What remains (precise) and failed directions

Remaining inside RES-HI(p) after this file (in addition to everything already open):
* B = 0, R = p: words with fewer than (p - 1)/2 non-constant maximal reflection runs, or with
  kappa > (p - 3)/2 + ceil((p - 1)/4).  Theorem FP still applies to them with several arcs per reflection run; it fails
  exactly when every admissible arc choice has sum (nu - 1) <= (p - 3)/2 (low value diversity, e.g. many reflection runs
  sigma_y sigma_y' sigma_y sigma_y' ... with two alternating values).
* B = 0, R != p: the arc method (Lemma ARC) applies verbatim, but balancing E_in requires control of run masses; for
  R <= 2 kappa the counting closes (with a balanced in-mass and about p - R/2 active arcs, available since there are at
  least p + kappa - R pairwise non-adjacent empty runs) but the balancing argument is not yet written.
* B >= 1, k >= p + 1: untouched except that Lemma ARC and Theorem ETA's method apply with D_P in place of masses.
Failed or limited directions (written reasoning only): local SPEC moves cannot lower o_F; window-level fusion of two odd
blocks enlarges windows; Theorem P has M = 3p - 3 - kappa + e_R/2 <= deg Q = 3p - 3 parameters for these words
(boundary e_R = 2 kappa only); plain toggles of single empty runs need about p - R/2 of them inside an m-range of length
H = p - 1 - kappa, which fails in IIIb; single-interval full windows need k <= p + 1 and a balanced interval, which can be
absent when one run carries most of A.
