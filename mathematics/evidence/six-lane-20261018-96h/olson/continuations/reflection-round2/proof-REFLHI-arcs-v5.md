# Reflection half for o_F > p: arc systems, optional segments and balanced labellings (consolidated candidate v5)

Owner OlsonReflectionSuccessor (Slice B of R18/olson-two-slice-successor-brief-v1.md).  Written after host clock
2026-10-19T06:06:03-0700.  Status: CANDIDATE_UNVERIFIED; written research only; no computation; no model review.
This file is self-contained.  It consolidates proof-REFLHI-arcs-v4.md (7683eb17...7f0e), its addenda K2P+ (7f5b3dc5...383f)
and SEG-v2 (bfa29fd5...cedce1, with erratum-1 53d90ba7...2868), all kept unchanged, and adds Corollaries MID and TOP
(Sec. 6).  Map of changes at the end.  Scope: words of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0.  No claim about rotation values, INV*(p) as a whole, ordered Olson, Lean, novelty or priority.

Paths: REFL/ = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/;
R16/ = institute/runs/six-lane-2026-10-16/review/; R18/ = institute/runs/six-lane-2026-10-18-96h/review/.

## 0. Imports (parent-accepted, at their exact scopes; hashes re-checked 2026-10-19 03:5x PDT)

* (H0) Lemma H0, REFL/proof-K0star-r2.md, sha256 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1, L55-65,
  valid for every cyclic constant-block representation of every length; accepted in R16/olson-reflection-K0star-RED-parent-
  verdict-v1.md (879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a) as algebra on the accepted GRX.
* (P0) Same file, Sec. 1, "Facts for G-avoiders of length 4p - 2": e_R <= e_F + 2 kappa, empty runs counted as even rotation
  runs (from the accepted Theorem P).  Normalisation N (L35-36) keeps blocks, lengths, empty runs and swaps A, B; the
  automorphism normalising x to 1 keeps everything else.
* (AR) Lemma AR as cited in K0star-r2 L66-67: a word with R = 0 has an identity 2p-subword.
* (RED) REFL/proof-RED-r2.md, c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7: Theorem RED and its proof
  with its accepted imports ((I1)-(I4), K0*, K1*, SING, KB*, CAP, KBH*, TII, QQ), same verdict.
* (SMALLK) R16/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8).
* (FEW) REFL/proof-REFL-fewodd-r5.md (4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363; verdict
  R16/olson-refl-fewodd-parent-verdict-v1.md binds the errata-equivalent r4 1e447754...861d).
* (CD) Cauchy-Davenport (classical): nonempty A_1, ..., A_s in Z_p: |A_1 + ... + A_s| >= min(p, sum |A_i| - s + 1).
Not used: rotation rigidity, INV*, SLZ3, RED-r3, K0star-r3, any finite computation.

## 1. Target, residual, setting

REFL-HI(p): every avoider of length 4p - 2 with rotation letters in one {rho_x, rho_-x}, x != 0, and o_F >= p + 1 (odd
maximal cyclic CONSTANT blocks) has every maximal cyclic reflection run constant.  (FEW) and REFL-HI(p) together are REFL(p)
of REFL/README.md L17-19.  RES-HI(p): RES_<(p) (RED-r2 L132-133) has no avoider with kappa >= 2 and k >= p + 1.
**Lemma 1.1.**  RES-HI(p) implies REFL(p).  Proof: RED turns a violating word into an avoider of RES_<(p) with kappa >= 2,
which has k >= p + 1 by (SMALLK).  []
Both remain OPEN.  This file excludes large parts of RES-HI(p) (indeed of every class of all-odd words, any B).
Setting (S): p >= 5 prime; w = R_1 S_1 ... R_k S_k cyclic (run R_t precedes block S_t), length 4p - 2, F >= 1, R >= 1,
rotation letters in {rho_1, rho_-1}, A >= B, every maximal constant block S_t = sigma_(y_t)^(l_t) of ODD length; empty runs are
genuine (y_(t-1) != y_t).  Runs need not be pure.  kappa = p - 1 - H, d_t = a_t - b_t, u_t = (y_(t-1) - y_t)/2 in Z_p,
R = 2p - k + 2 kappa, H = p - 1 - kappa.  For a pattern P (set of runs): E+(P) := A_P + B_(P^c), E-(P) := R - E+(P).
**Lemma W.**  If a proper nonempty pattern P with m = m(P) maximal cyclic intervals has u_P := sum_(t in P) u_t congruent
mod p to an element of [-gamma_m(E-(P)), gamma_m(E+(P))], gamma_m(E) := min(p - m, E - kappa + m - 1, floor(E/2)), then w has
an identity 2p-subword.  Proof: (H0) with beta(P) = 0 (all blocks odd).  []
**Fact 2.1.**  gamma_m(E) = floor(E/2) iff ceil(E/2) >= kappa + 1 - m and floor(E/2) <= p - m.  (E - floor(E/2) = ceil(E/2).)  []
**Fact 2.2.**  If w avoids: R >= p, and every run has at most 2(R - p) + 1 letters.
Proof.  (P0) with e_F = 0: at most 2 kappa runs are even, so at least k - 2 kappa = 2p - R runs are odd, hence nonempty;
R >= 2p - R, and one run has at most R - (2p - R - 1) letters.  []

## 2. Arc systems (Lemma ARC) and optional segments (Lemmas ARC+, SEG)

Arc: a nonempty set of consecutive blocks whose internal runs are all EMPTY; nu(X) := number of distinct values in X (>= 2 if
X has an internal run).  Arc system: 2m >= 2 pairwise disjoint arcs X_1, Y_1, ..., X_m, Y_m in cyclic order; the gap after
an arc (runs and blocks up to the next arc) contains the run right after the arc; gaps after X_i are IN, after Y_i OUT;
E+ := B + sum of d_t over IN-gap runs.
**Lemma 2.1.**  For a_i in X_i, b_i in Y_i, P := union of the runs R_(a_i + 1), ..., R_(b_i) is a proper pattern with exactly m
intervals, E+(P) = E+, and u_P = (1/2) sum_i (y_(a_i) - y_(b_i)).
Proof.  The i-th interval consists of internal (empty) runs of X_i after a_i, the IN-gap runs and internal runs of Y_i up to
b_i; OUT-gaps contain a run, so intervals are separated and P != [k]; empty runs have d = 0; theta telescopes.  []
A **segment** is a nonempty set Sigma of consecutive blocks inside one maximal reflection run (internal runs empty).  Given a
base arc system and pairwise disjoint segments Sigma_j disjoint from all base arcs, with integers t_j >= 0, a configuration
chooses blocks c_1 < ... < c_(2t'_j) in each Sigma_j (0 <= t'_j <= t_j) and adds them as single-block arcs.
**Lemma ARC+.**  (i) Every configuration is an arc system with 2(m_b + sum t'_j) arcs and the base value of E+.  (ii) Its
u-value is u_base + sum_j eps_j W_j, u_base in the base sumset {(1/2) sum_i (y_(a_i) - y_(b_i))}, eps_j = +-1 fixed by the
base gap containing Sigma_j, W_j := (1/2) sum_s (y_(c_(2s)) - y_(c_(2s-1))).  (iii) If every m in [m_b, m_b + sum t_j]
satisfies Fact 2.1 for E+ and for E- = R - E+, and
   floor(E+/2) + floor(E-/2) + sum over base arcs of (nu - 1) + sum_j (|U_j| - 1) >= p - 1,
U_j := the set of possible W_j, then w has an identity 2p-subword.  (With no segments this is Lemma ARC.)
Proof.  (i) Sigma_j contains no nonempty run and meets no base arc, so it lies in one base gap; inserting 2t' arcs there
splits the gap into 2t' + 1 sub-gaps with alternating labels, the outer two keeping the old label; runs whose label changes
lie strictly inside Sigma_j and are empty.  Several segments in one gap are inserted in their cyclic order; the same
argument applies to each.  New gaps contain the run after their arc.  (ii) In an IN gap after X_i the roles read
X_i, c_1, c_2, ..., c_(2t'), Y_i = X, Y, X, ..., X, Y, the interval a_i..b_i becomes a_i..c_1, c_2..c_3, ..., c_(2t')..b_i
(t' more intervals) and u changes by (1/2)(-y_(c_1) + y_(c_2) - ... + y_(c_(2t'))) = W; in an OUT gap after Y_i the new
intervals are c_1..c_2, ..., c_(2t'-1)..c_(2t') (t' new intervals) and u changes by -W.  (iii) Fact 2.1 gives every
configuration the window [-floor(E-/2), floor(E+/2)].  The u-values contain the sumset of the base sets (1/2)V(X_i),
-(1/2)V(Y_i) and the eps_j U_j, which by (CD) has >= min(p, 1 + sum(nu - 1) + sum(|U_j| - 1)) residues; with the window's
min(p, floor(E+/2) + floor(E-/2) + 1) residues the counts reach p + 1, so they meet; Lemma W.  []
**Lemma SEG.**  If Sigma has b' blocks, the set U of values W with t' <= t has |U| >= min(p, 1 + min(2t, b' - 1)).
Proof.  Values v_1, ..., v_(b'), delta_j := v_(j+1) - v_j != 0.  2W = sum over j in J of delta_j, J = union of the separated
intervals [c_(2s-1), c_(2s) - 1]; conversely any J in [1, b' - 1] with at most t maximal intervals [x_s, x'_s] arises from
c = (x_1, x'_1 + 1, x_2, x'_2 + 1, ...).  Induction on b'.  If t = 0 or b' = 1: |U| >= 1.  If b' = 2 <= 2t + ..., t >= 1:
U contains 0 and delta_1/2.  If b' >= 3, t >= 1: A := {0, delta_1, delta_2, delta_1 + delta_2} has >= 3 elements (if
delta_1 + delta_2 = 0 it is {0, +-delta_1}, p odd; otherwise 0, delta_1, delta_1 + delta_2 are distinct).  U'' := sums over J''
in [3, b' - 1] with at most t - 1 intervals; by induction (blocks 3..b') |U''| >= min(p, 1 + min(2t - 2, b' - 3)).  J u J'' has
at most t maximal intervals, so 2U contains A + U'', and (CD) gives |U| >= min(p, |A| + |U''| - 1) >= min(p, 3 + min(2t - 2,
b' - 3)) = min(p, 1 + min(2t, b' - 1)).  []
So with t = ceil((b' - 1)/2) the gain |U| - 1 is >= b' - 1 (unless capped), and each unit of t, up to that value, adds at
least one unit of guaranteed gain.

## 3. Labellings and balance

Let w avoid.  N_1, ..., N_q (q >= 1) are the nonempty runs in cyclic order, M_i the maximal reflection run between N_i and
N_(i+1); M_i has b_i blocks and e_i = b_i - 1 internal (empty) runs; g_E := sum e_i = k - q.  d := max_j |d(N_j)|.  An arc
choice puts c_i pairwise disjoint arcs inside M_i, sum c_i even; it induces z in {+-1}^q (up to sign) by z_(i+1) = -z_i iff c_i
is odd, and T := sum_j z_j d(N_j).
**Lemma 3.1.**  E+ = (R + T)/2 or (R - T)/2 (IN = the label +1 of z or of -z).  Proof: N_j lies in a gap; crossing M_i crosses
c_i arcs; IN runs give a_j to E+, OUT runs b_j.  []
**Lemma 3.2 (balanced kill).**  If an arc choice (possibly with segments, Lemma ARC+) has all its m in a range on which
ceil(E_min/2) >= kappa + 1 - m and floor(E_max/2) <= p - m (E_min, E_max the two values (R -+ |T|)/2), and total gain
(base sum of nu - 1 plus segment gains) at least Pi_need := p - ceil(R/2), then w has an identity 2p-subword.
Proof.  floor(E+/2) + floor(E-/2) >= ceil(R/2) - 1; Lemma ARC+ (iii).  []
**Lemma BAL.**  For every arc choice with sum c_i even and every index i there is an index i' != i such that changing the
parities of c_i and c_(i') gives |T| <= d (nothing to do if |T| <= d).
Proof.  Say T > d.  S(t) := sum_(j = i+1..i+t) z_j d(N_j), S(0) = 0, S(q) = T, steps <= d.  The least t with S(t) >= (T - d)/2
has 1 <= t <= q - 1 and S(t) < (T + d)/2; the change flips z on N_(i+1..i+t), giving T - 2S(t), of absolute value <= d.  []
Realisations of a parity change at M_j: delete a singleton arc of M_j; add a singleton on an unused block of M_j; or split a
two-block arc of M_j into two singletons.  Each changes the arc count by +-1 and loses at most one two-block arc.

## 4. The cell R = p and Theorem FP

If R = p and w avoids, Fact 2.2 gives: every nonempty run is one letter, q = p, k = p + 2 kappa, g_E = 2 kappa, d = 1, and T is
odd, so |T| <= 1 means {E+, E-} = {(p - 1)/2, (p + 1)/2}.  With r := ceil((p - 1)/4) = floor((p + 1)/4), m_0 := max(1,
kappa + 1 - r) and m_1 := p - r, Fact 2.1 holds for both values exactly when m_0 <= m <= m_1, and then the window sum is
(p - 1)/2.  **Theorem FP:** every arc choice with m_0 <= m <= m_1 and |T| = 1 has sum(nu - 1) <= (p - 3)/2 (Lemma 3.2).  The
alternating labelling with one repeat across M_n is balanced for some n (Lemma BAL with all c_i = 1 but one; for B = 0, for
every n), which gives Corollary FP-1 of v3/v4 (diversity version); it is subsumed below except at kappa = (p - 1)/2 for p = 7.

## 5. Theorems K2P+ and SEG

**Theorem K2P+.**  Let w have length 4p - 2 over D_(2p), rotation letters in one pair, all maximal constant reflection blocks
odd.  If k >= 2p + 1 and k >= 3 kappa + 3, then w has an identity 2p-subword.  (Any B, purity, values.)
Proof.  R = 0: (AR).  Normalise; suppose w avoids; delta := R - p >= 0, d <= 2 delta + 1 (Fact 2.2).  k >= 3 kappa + 3 is
H - delta >= 2; k >= 2p + 1 is 2 kappa >= R + 1; R = k (mod 2).  Put m_lo := kappa + 1 - ceil((R - d)/4),
m_hi := p - floor((R + d)/4), Pi* := Pi_need + 1.  (a) m_hi - m_lo >= H - floor(d/2) >= H - delta >= 2.  (b) m_lo >=
(R + 1)/2 + 1 - (R + 3)/4 > 0.  (c) Each M_i holds floor(b_i/2) >= e_i/2 disjoint two-block arcs ("pairs", nu = 2); in all
>= g_E/2 >= (k - R)/2 >= Pi* (as k >= 2p + 2 - [R odd]).  (d) H <= (p - 3)/2, so d <= 2(H - 2) + 1 <= p - 6; N0 := 2 m_lo + 2
satisfies Pi* <= N0 and N0 + Pi* <= k - p + 5 + d/2 <= k - 1.  (e) Take Pi* pairs and N0 - Pi* singletons on unused blocks;
some block stays unused; let i index a reflection run with an unused block.  (f) Lemma BAL with this i: the change at i is
free (a singleton on the unused block), the change at i' loses at most one pair; afterwards |T| <= d, pairs >= Pi_need, arc
count in [N0 - 2, N0 + 2] = [2 m_lo, 2 m_lo + 4], inside [2 m_lo, 2 m_hi].  (g) |T| <= d gives ceil(E_min/2) >= ceil((R -
d)/4) >= kappa + 1 - m and floor(E_max/2) <= floor((R + d)/4) <= p - m; Lemma 3.2.  []
**Corollary IIIb-X.**  For p >= 7, no all-odd word with B = 0, R = p, kappa = (p + 1)/2 (k = 2p + 1) avoids (K2P+).
**Theorem SEG.**  Let w avoid (setting (S)); classes C = {i : b_i = 1}, AB = {i : b_i = 2}, L = {i : b_i >= 3}, n_CA :=
|C| + |AB|; m_lo := max(1, kappa + 1 - ceil((R - d)/4)), m_hi := p - floor((R + d)/4).  If (H1) m_hi - m_lo >= Pi_need + 1,
(H2) n_CA >= 2 m_lo + 2 and (H3) g_E >= Pi_need + 1, then w has an identity 2p-subword (contradiction).
Proof.  N_O := 2 m_lo + 2.  O_0 in C u AB with |O_0| = N_O (H2).  Base: the single block of M_i (i in C) or both blocks of
M_i as one arc (a pair-arc; i in AB), for i in O_0.  Lemma BAL with i in O_0; a change at j removes the base arc of M_j if it
has one, else adds the single block (C), the pair-arc (AB) or the FIRST block of M_j (L).  Final base set O: |O| in
{N_O - 2, N_O}, m_b in {m_lo, m_lo + 1}, |L n O| <= 1, |T| <= d.  Segments: M_j for j in (AB u L) \ O; M_j minus its first block
for j in L n O.  Potential gains (Lemma SEG, t_j = ceil((b' - 1)/2)): 1, e_j, e_j - 1; with base pair-arcs the potential total
is g_E - |L n O| >= Pi_need (H3).  Lower the t_j minimally keeping total gain >= Pi_need: sum t_j <= Pi_need.  All
configurations have m in [m_lo, m_lo + 1 + Pi_need], inside [m_lo, m_hi] (H1); as in K2P+ (g) Fact 2.1 holds; Lemma 3.2.  []
**Corollary SEG-p (R = p, every B).**  Length 4p - 2, rotations in one pair, exactly p rotation letters, all blocks odd,
(p + 1)/4 <= kappa <= (p - 3)/2: solvable.
Proof.  If avoiding: Sec. 4 data.  kappa + 1 - r >= 1 (p = 4a + 1: r = a, kappa >= a + 1; p = 4a + 3: r = a + 1, kappa >=
a + 1), so m_lo = kappa + 1 - r, m_hi = p - r, Pi_need = (p - 1)/2.  (H1): p - 1 - kappa >= (p + 1)/2.  (H2): L-runs have >= 2
empty runs, so |L| <= kappa, n_CA >= p - kappa >= 2 kappa + 4 - (p - 1)/2 >= 2 kappa + 4 - 2r iff kappa <= (p - 3)/2.
(H3): 2 kappa >= (p + 1)/2.  Theorem SEG.  []
**Corollary SEG-num.**  Length 4p - 2, rotations in one pair, all blocks odd, delta := R - p >= 0 and
(p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2: solvable.  (Nonempty only if 5 delta <= p - 10; then
(3p + delta + 2)/2 <= k <= 2p - 2 delta - 4.)
Proof.  If avoiding: d <= 2 delta + 1, q >= p - delta, k = p - delta + 2 kappa.  (H1): m_hi - m_lo >= p - 1 - kappa - delta (or
more if m_lo = 1) >= (p - delta)/2 + 1 >= Pi_need + 1.  (H3): g_E >= k - R = 2 kappa - 2 delta >= (p - delta)/2 + 1.  (H2):
|L| <= (k - q)/2, n_CA >= (3q - k)/2 >= p - delta - kappa; 2 m_lo + 2 <= max(4, 2 kappa + 4 - (p - delta - 1)/2) (as
R - d >= p - delta - 1); p - delta - kappa >= 2 kappa + 4 - (p - delta - 1)/2 iff kappa <= (p - delta - 3)/2, and
p - delta - kappa >= 4 as p - delta >= 10.  Theorem SEG.  []

## 6. Closing the R = p cell above (p + 1)/4 (new in v5)

**Corollary MID (R = p, kappa = (p - 1)/2, p >= 11, every B).**  Solvable.
Proof.  If avoiding: q = p, d = 1, g_E = p - 1, k = 2p - 1, m_lo = (p + 1)/2 - r >= 1, m_hi - m_lo = H = (p - 1)/2 =
Pi_need.  N_O := 2 m_lo + 2 = p + 3 - 2r.  |L| <= (p - 1)/2, so n_CA >= (p + 1)/2 and lambda_0 := max(0, N_O - n_CA) <=
(p + 5)/2 - 2r <= 3.  Choose O_0 of size N_O containing min(|AB|, N_O) AB-runs, then C-runs, then (only if needed) lambda_0
L-runs (base: first block).  Lemma BAL with i in O_0 n (C u AB) (nonempty as N_O - lambda_0 >= 1).  Afterwards |T| = 1,
m_b in {m_lo, m_lo + 1} and |L n O| <= lambda_0 + 1 <= 4.  Segments as in Theorem SEG (L-runs in O lose their first block); the
potential gain is >= g_E - 4 = p - 5 >= Pi_need + 1 (p >= 11).  Rate: if some AB-run carries a base pair-arc, the base gain is
>= 1; otherwise some segment has >= 3 blocks (an L-run outside O, or, if every L-run is in O, then |AB| <= 2 forces
sum over the <= 4 L-runs of e_j >= p - 3, so one of their segments has >= 3 blocks), and its first pair gains 2.  Either way the
minimal t's satisfy sum t_j <= Pi_need - 1, so all m lie in [m_lo, m_lo + Pi_need] = [m_lo, m_hi]; Lemma 3.2.  (If |AB| >= 3
then O_0 holds >= 3 AB-runs and at most two are removed, so the first case applies; if |AB| <= 2 and some L-run is outside O,
the second.)  []
**Corollary TOP (R = p, kappa in {p - 2, p - 1}, p >= 7, every B).**  Solvable.
Proof.  If avoiding: q = p, d = 1, g_E = 2 kappa >= 2p - 4, m_0 = kappa + 1 - r, m_1 = p - r, m_1 - m_0 = H in {1, 0}.  Some
run has b >= 3 (else g_E <= p < 2p - 4); call it l.  Pair capacity sum floor(b_i/2) >= kappa >= p - 2 >= Pi_need + 2 + 1.
Initial choice: Pi_need + 2 pairs, one of them in M_l, plus a singleton on another block of M_l, plus singletons on unused
blocks, with total arc count exactly 2 m_0 (2 m_0 >= Pi_need + 2, and 2 m_0 + Pi_need + 2 <= k as (p + 5)/2 + 2 - 2r <= p).
Lemma BAL with i = l: realise the change at i' by the rule of Sec. 3 (sign eps' = +-1 for the arc count); at l delete its
singleton if eps' = +1 and split its pair if eps' = -1.  The arc count stays 2 m_0, at most two pairs are lost, |T| = 1;
Lemma 3.2 with m = m_0.  []
So, for p >= 11 and every B, no all-odd word with R = p and kappa >= (p + 1)/4 avoids (SEG-p, MID, K2P+, TOP); for p = 7 the
same holds except kappa = 3 (FP-1 covers it under its diversity hypothesis); for p = 5, kappa in {3, 4} (TOP).

## 7. Structure for B = 0, R <= 2 kappa + 1 (Theorem ETA)

m* := kappa + 1 - floor(R/2), eta_j := y_j/2 + r_1 + ... + r_j (blocks indexed from run R_1, nonempty if R odd).  If w avoids,
every partition of the blocks into 2m* consecutive parts Z_i has sum |eta(Z_i)| <= p + 2m* - 2.  Proof: for a_i in Z_(2i-1),
b_i in Z_(2i), P := union of R_(a_i+1..b_i) has m* intervals, R_1 notin P, u_P - D_P = sum(eta_(a_i) - eta_(b_i)); Fact 2.1
gives G_(m*)(x) = x - floor(R/2) for 0 <= x <= R - 1 (and x = R if R even), G_(m*)(R) = floor(R/2) if R odd, so
D_P - floor(R/2) lies in I(P); avoidance forbids the value -floor(R/2), and (CD) gives the bound.  []

## 8. Delta, remaining, failed directions

Delta (all CANDIDATE): Lemmas W, 2.1, ARC+, SEG, 3.1, 3.2, BAL; Theorems FP, K2P+, SEG; Corollaries IIIb-X, SEG-p,
SEG-num, MID, TOP; Theorem ETA.
Excluded (all-odd, rotations in one pair, any B): k >= max(2p + 1, 3 kappa + 3); R = p with kappa >= (p + 1)/4 (p >= 11);
R = p + delta with (p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2.
Remaining in RES-HI(p) (B = 0 additionally keeps the accepted CJ''''/EDGE/REFL-B0 coverage):
* R = p, kappa < (p + 1)/4 (every B >= 1 cell; for B = 0 the cells above the CJ'''' Corollary 2 range); p = 7, kappa = 3;
* R >= p + 1 outside SEG-num and K2P+ (large delta or large d; small H; g_E <= Pi_need).
Arc-method limit (of the method, not an obstruction to REFL): each unit of gain in Lemma ARC+ uses an empty run, so the
method needs g_E > Pi_need (about k > p + R/2).  The Z_(2p)/Kneser variant (checkpoint-04) needs about twice the gain and is
not better.  Other failed directions: local SPEC moves cannot lower o_F; window-level fusion of odd blocks raises H;
Theorem P has M = 3p - 3 - kappa + e_R/2 <= 3p - 3 parameters; generalised Davenport items need k - kappa zero-mass brackets.

## Map v4 (+ addenda) -> v5

Content of v4, K2P+ and SEG-v2 (+ erratum-1) restated without mathematical change (Sec. 3 merges v4 Lemmas 4.1-4.2 and BAL;
SEG's "Ranges" uses the corrected k-range).  New: Corollaries MID and TOP (Sec. 6) and the closing statement for R = p.
