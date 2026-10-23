# Reflection half for o_F > p: arc systems, balanced labellings, and two new high-k exclusions (candidate v4)

Owner OlsonReflectionSuccessor (Slice B of R18/olson-two-slice-successor-brief-v1.md).  Written after host clock
2026-10-19T05:41:05-0700.  Status: CANDIDATE_UNVERIFIED; written research only; no computation; no model review.
Extends proof-REFLHI-arcs-v3.md (2889509a...512f8f, sent 05:35, kept unchanged, with erratum-1 1fba1b33...5ee3): Secs. 0-3
and Theorem FP are repeated verbatim in substance; NEW are Lemma BAL (Sec. 4.3), Theorem K2P and Corollary K2P-num
(Sec. 5).  Fix map at the end.  Scope: words of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0.  No claim about rotation values, INV*(p) as a whole, ordered Olson, Lean, novelty or priority.

Paths: REFL/ = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/;
R16/ = institute/runs/six-lane-2026-10-16/review/; R18/ = institute/runs/six-lane-2026-10-18-96h/review/.

## 0. Imports (parent-accepted, at their exact scopes; hashes re-checked 2026-10-19 03:5x PDT)

* (H0) Lemma H0, REFL/proof-K0star-r2.md, sha256 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1, L55-65,
  for every cyclic constant-block representation of every length; accepted in R16/olson-reflection-K0star-RED-parent-
  verdict-v1.md (879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a) as algebra on the accepted GRX.
* (P0) Same file, Sec. 1, "Facts for G-avoiders of length 4p - 2": e_R <= e_F + 2 kappa (empty runs count as even rotation
  runs), from the accepted Theorem P.  Normalisation N (K0star-r2 L35-36) keeps blocks, lengths and empty runs, swaps A, B.
* (AR) Lemma AR as cited in K0star-r2 L66-67 (a G-word with R = 0 is solvable); used only to dismiss R = 0.
* (RED) REFL/proof-RED-r2.md, c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7, Theorem RED and its proof
  with its accepted imports, same verdict.
* (SMALLK) R16/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8).
* (FEW) REFL/proof-REFL-fewodd-r5.md (4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363; verdict
  R16/olson-refl-fewodd-parent-verdict-v1.md binds the errata-equivalent r4 1e447754...861d).
* (CD) Cauchy-Davenport (classical): nonempty A_1, ..., A_s in Z_p: |A_1 + ... + A_s| >= min(p, sum|A_i| - s + 1).
Not used: rotation rigidity, INV*, SLZ3, RED-r3, K0star-r3, MXG/B0S beyond (SMALLK), finite computation.

## 1. Frozen target and residual

REFL-HI(p): every avoider of length 4p - 2 over D_(2p) with rotation letters in one {rho_x, rho_-x}, x != 0, and
o_F >= p + 1 (odd maximal cyclic CONSTANT blocks) has every maximal cyclic reflection run constant.  (FEW) + REFL-HI(p)
= REFL(p) (REFL/README.md L17-19).  RES-HI(p): RES_<(p) (RED-r2 L132-133) has no avoider with kappa >= 2, k >= p + 1.
**Lemma 1.1.**  RES-HI(p) implies REFL(p).  Proof: RED turns a violating word into an avoider of RES_<(p) with kappa >= 2,
which has k >= p + 1 by (SMALLK).  []
Both remain OPEN; Secs. 4-5 exclude new parts of RES-HI(p) (indeed of every all-odd class), Sec. 7 states what remains.

## 2. Setting and windows

Setting (S): p >= 5 prime; w = R_1 S_1 ... R_k S_k cyclic (R_t precedes S_t), length 4p - 2, F >= 1, R >= 1, rotation letters
in {rho_1, rho_-1}, A >= B, every maximal constant block S_t = sigma_(y_t)^(l_t) of ODD length, empty runs genuine.  Runs
need not be pure.  kappa = p - 1 - H, d_t = a_t - b_t, u_t = (y_(t-1) - y_t)/2 in Z_p, R = 2p - k + 2 kappa (all odd).
For a pattern P: E+(P) := A_P + B_(P^c) = D_P + B, E-(P) := R - E+(P).
**Lemma W.**  If a proper nonempty pattern P with m = m(P) intervals has u_P := sum_(t in P) u_t congruent mod p to an
element of I(P) = [-gamma_m(E-(P)), gamma_m(E+(P))], gamma_m(E) := min(p - m, E - kappa + m - 1, floor(E/2)), then w has an
identity 2p-subword.  Proof: (H0) with beta(P) = 0.  []
**Fact 2.1.**  gamma_m(E) = floor(E/2) iff ceil(E/2) >= kappa + 1 - m and floor(E/2) <= p - m.  []
**Fact 2.2 (run sizes; avoiders).**  If w avoids, then R >= p, and every run has r_t <= 2(R - p) + 1.
Proof.  (P0) with e_F = 0: at most 2 kappa runs are even, so at least k - 2 kappa = 2p - R runs are odd, hence nonempty.
So at least 2p - R runs are nonempty, R >= 2p - R, and a single run has at most R - (2p - R - 1) letters.  []

## 3. Arc systems and Lemma ARC

Arc: nonempty set X of consecutive blocks S_j, ..., S_(j+l) whose internal runs R_(j+1), ..., R_(j+l) are all EMPTY;
nu(X) := number of distinct values y in X (>= 2 if X has an internal run).  Arc system: 2m >= 2 pairwise disjoint arcs
X_1, Y_1, ..., X_m, Y_m in cyclic order; the gap after an arc (runs and blocks up to the next arc) contains the run right
after the arc; gaps after X_i are IN, after Y_i OUT; E_in := sum of d_t over IN-gap runs; E+ := E_in + B.
**Lemma 3.1.**  For a_i in X_i, b_i in Y_i, P := union over i of the runs R_(a_i + 1), ..., R_(b_i) is proper with exactly m
intervals, E+(P) = E+ (independent of the choice), and u_P = (1/2) sum_i (y_(a_i) - y_(b_i)).
Proof.  Each interval consists of internal (empty) runs of X_i after a_i, the IN-gap runs and internal runs of Y_i up to
b_i; OUT-gaps contain a run, so the intervals are separated and P != [k]; empty runs have d = 0; theta telescopes.  []
**Lemma ARC.**  If G := gamma_m(E+), G' := gamma_m(R - E+) satisfy G + G' >= 0 and
sum over the 2m arcs of (nu - 1) + G + G' >= p - 1, then w has an identity 2p-subword.
Proof.  All patterns of Lemma 3.1 share the window [-G', G]; their u_P form the sumset of the 2m sets (1/2)V(X_i),
-(1/2)V(Y_i), which by (CD) has >= min(p, 1 + sum(nu - 1)) residues; the window has min(p, G + G' + 1).  The counts add up to
>= p + 1, so they meet; Lemma W.  []

## 4. Reflection-run labellings

Let w avoid (setting (S)).  Let N_1, ..., N_q (q >= 1) be the nonempty runs in cyclic order and M_i the maximal reflection run
between N_i and N_(i+1) (for q = 1, the single reflection run); M_i is an arc with e_i internal (empty) runs and
b_i = e_i + 1 blocks; sum_i e_i = k - q.  An **arc choice** puts c_i pairwise disjoint arcs inside M_i, sum c_i = 2m even.
It induces z in {+1, -1}^q (up to a global sign) by z_(i+1) = -z_i iff c_i is odd; T := sum_j z_j d_(N_j) (d of the run N_j).
**Lemma 4.1 (labels).**  For an arc choice, with IN = the label +1 of z or of -z, E+ = (R + T)/2 or (R - T)/2.
Proof.  The run N_j lies in a gap (arcs contain only empty runs); passing from N_i to N_(i+1) crosses the c_i arcs of M_i, so
the gap label changes iff c_i is odd.  IN runs contribute a_j to E+, OUT runs b_j; so E+ - E- = sum_j z_j d_j = T.  []
**Lemma 4.2 (kill by a balanced arc choice).**  If an arc choice has m >= 1, the two values E+- = (R +- T)/2 satisfy
ceil(E_min/2) >= kappa + 1 - m and floor(E_max/2) <= p - m, and its arcs have sum(nu - 1) >= p - ceil(R/2), then w (assumed to
avoid) has an identity 2p-subword, a contradiction.
Proof.  By Fact 2.1, G + G' = floor(E+/2) + floor(E-/2) >= ceil(R/2) - 1 >= 0 (equality cases: R odd; R even with both
E+- odd); Lemma ARC.  []
**Lemma BAL (balancing).**  Let d := max_j |d_(N_j)|.  For every arc choice with sum c_i even and every index i there is an
index i' such that, after changing the parities of c_i and c_(i') (no change if |T| <= d already), |T| <= d.
Proof.  If |T| <= d there is nothing to do; else say T > d (T < -d is symmetric).  Let S(t) := sum_(j = i+1)^(i+t) z_j d_j for
t = 0, ..., q (indices mod q), S(0) = 0, S(q) = T, steps of absolute value <= d.  Let t be minimal with S(t) >= (T - d)/2; then
t >= 1, S(t) < (T - d)/2 + d = (T + d)/2, and t <= q - 1 (S(q) = T > (T + d)/2).  Changing the parities of c_i and c_(i+t)
flips z exactly on N_(i+1), ..., N_(i+t), so T becomes T - 2 S(t), of absolute value <= d.  []
A parity change of c_j is realised by: deleting a singleton arc of M_j if there is one; else adding a singleton arc on an
unused block of M_j if there is one; else splitting one 2-block arc of M_j into two singletons.  This changes 2m by +-1 and
the number of 2-block arcs by at most 1.

### 4.4 The cell R = p (from v3)

If R = p, Fact 2.2 gives r_t <= 1: every nonempty run is one letter, q = p, k = p + 2 kappa, sum e_i = 2 kappa, d = 1, and
T is odd, so |T| <= 1 means E+- = (p +- 1)/2.  With m_0 := max(1, kappa + 1 - ceil((p - 1)/4)) and m_1 := p - floor((p + 1)/4)
(m_0 <= m_1; ceil((p - 1)/4) = floor((p + 1)/4)), Fact 2.1 gives floor-type windows on both sides for m_0 <= m <= m_1, and
G + G' = (p - 1)/2.
**Theorem FP.**  R = p, w avoids: every arc choice with m_0 <= m <= m_1 and |T| = 1 has sum(nu - 1) <= (p - 3)/2.  (Lemma 4.2.)
**Lemma 4.3 (v3).**  The alternating labelling with one repeat across M_n has |T| = 1 for some n (for every n if B = 0).
(Proof in v3; it is also the case d = 1 of Lemma BAL applied to the labelling with all c_i = 1 except one.)
**Corollary FP-1 (v3).**  Length 4p - 2, rotations in one pair, exactly p rotation letters, all blocks odd,
kappa <= (p - 3)/2 + ceil((p - 1)/4), and sum_i (nu_i - 1) - max_i (nu_i - 1) >= (p - 1)/2 over the maximal reflection runs
(or, if all rotation letters are equal, the same with min in place of max): solvable.  (Proof as in v3.)

## 5. A uniform exclusion for k >= 2p + 3 (new)

**Theorem K2P.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0, all of whose maximal constant reflection blocks have odd length.  If
   k >= 2p + 3   and   k >= 3 kappa + 3,
where k is the number of these blocks and kappa = p - 1 - H, then w has an identity 2p-subword (in increasing index order).
No hypothesis on B, on run purity, on the reflection values or on o_F (here o_F = k) is made.
Proof.  If F = 0 there is nothing... (F = 0 means k = 0, excluded by k >= 2p + 3).  If R = 0, (AR).  Normalise x = 1 and
A >= B (N keeps k, kappa); then w is in setting (S).  Suppose w avoids.  Put delta := R - p >= 0 (Fact 2.2) and
d := max_j |d_(N_j)| <= 2 delta + 1 (Fact 2.2).  From R = 2p - k + 2 kappa: k >= 3 kappa + 3 is H - delta >= 2, and
k >= 2p + 3 is 2 kappa >= R + 3.  Put
   m_lo := kappa + 1 - ceil((R - d)/4),   m_hi := p - floor((R + d)/4),   Pi* := p - ceil(R/2) + 2.
(a) m_hi - m_lo = H - (floor((R + d)/4) - ceil((R - d)/4)) >= H - floor(d/2) >= H - delta >= 2.
(b) m_lo >= 1: kappa >= (R + 3)/2 and ceil((R - d)/4) <= (R + 3)/4.
(c) Pairs.  Let a 2-block arc ("pair") be two consecutive blocks of one M_i (necessarily joined by an empty run; nu = 2).
    M_i contains floor(b_i/2) = floor((e_i + 1)/2) >= e_i/2 disjoint pairs, so at least (k - q)/2 >= (k - R)/2 in all
    (q <= R).  As R = k (mod 2), (k - R)/2 >= Pi* iff k >= 2p + 4 - [R odd], which follows from k >= 2p + 3.
(d) Initial choice.  Take Pi* disjoint pairs and N0 - Pi* singleton arcs on unused blocks, N0 := 2 m_lo + 2.  This needs
    Pi* <= N0 (true: N0 >= 2 kappa + 4 - (R - d + 3)/2 >= p - R/2 + 2 >= Pi* because 2 kappa >= R + 3 >= p + 3) and
    N0 + Pi* <= k (true: N0 + Pi* <= 2 kappa + 4 - (R - d)/2 + p - R/2 + 2 = k - p + 6 + d/2, and d <= 2 delta + 1 <=
    2H - 3 <= p - 8 as H <= (p - 5)/2 from 2 kappa >= R + 3 >= p + 3).
(e) Balance.  By Lemma BAL (any i) change at most two parities; afterwards |T| <= d, the arc count 2m lies in
    [N0 - 2, N0 + 2] = [2 m_lo, 2 m_lo + 4], within [2 m_lo, 2 m_hi] by (a), and at least Pi* - 2 = p - ceil(R/2) pairs remain.
(f) Kill.  With m_lo <= m <= m_hi and E_min >= (R - d)/2, E_max <= (R + d)/2: ceil(E_min/2) >= ceil((R - d)/4) >= kappa + 1 - m
    and floor(E_max/2) <= floor((R + d)/4) <= p - m.  sum(nu - 1) >= number of pairs >= p - ceil(R/2).  Lemma 4.2 gives a
    contradiction.  []
**Corollary K2P-num.**  For prime p >= 11 and (p + 3)/2 <= kappa <= p - 3, no word of RES_<(p) (indeed no all-odd word with
rotations in one pair) with k >= max(2p + 3, 3 kappa + 3) avoids.  Every avoider of RES_<(p) has k <= p + 2 kappa (Fact 2.2:
R >= p), so the excluded cells are kappa in [(p + 3)/2, p - 3], max(2p + 3, 3 kappa + 3) <= k <= p + 2 kappa, both B = 0 and
1 <= B < kappa.  For p = 5, 7 the range is empty.  []
Examples: p = 11: (kappa, k) = (7, 25), (8, 27); p = 31: kappa = 17..28, e.g. kappa = 20 with k = 71..65 (R = p..p + 6).
Relation to known results: for B = 0 these cells have R = 2p - k + 2 kappa <= 2 kappa - 3 (regime IIIb, gap (d) of
REFL/results-r4.md) and are outside CJ''''/REFL-B0 (which need R >= 4 kappa - 4); for B >= 1 and k >= p + 1 nothing was
known (REFL/notes-B1-cfunc-r1.md).

## 6. Structure for B = 0 and R <= 2 kappa + 1 (Theorem ETA, from v3, unchanged)

In setting (S) with B = 0, R <= 2 kappa + 1, m* := kappa + 1 - floor(R/2), eta_j := y_j/2 + r_1 + ... + r_j (blocks indexed
from run R_1, nonempty if R odd): if w avoids, every partition of the blocks into 2m* consecutive segments has
sum |eta(Z_i)| <= p + 2m* - 2.  Proof in v3 Sec. 5.

## 7. Exact delta and what remains

Delta (all CANDIDATE): Lemma ARC, Lemmas 4.1-4.2, BAL; Theorem FP and Corollary FP-1 (R = p, any B, diversity hypothesis);
Theorem K2P and Corollary K2P-num (k >= max(2p + 3, 3 kappa + 3), any B, no further hypothesis); Theorem ETA (structure).
Remaining inside RES-HI(p):
* p + 1 <= k <= 2p + 2 (every B), except FP-1 words at R = p and the accepted B = 0 CJ''''/REFL-B0 ranges.  At these k the
  pair supply (k - R)/2 is below the need p - ceil(R/2) by up to (2p + 3 - k)/2; diversity (nu >= 3 inside reflection runs)
  or non-arc patterns must make up the difference.  The extreme IIIb family (B = 0, kappa = (p + 1)/2, R = p, k = 2p + 1) lies
  here, one unit short of K2P.
* k >= 2p + 3 with k < 3 kappa + 3 (H - delta <= 1: kappa near p - 1 or large runs): balancing tolerance is too small.
* Only for B = 0 do the accepted CJ''''/EDGE/REFL-B0 results apply; for B >= 1 the only new coverage is FP-1 and K2P.
Failed or limited directions (written reasoning only): local SPEC moves cannot lower o_F; window-level fusion of two odd
blocks raises H; Theorem P parameter count M = 3p - 3 - kappa + e_R/2 <= deg Q = 3p - 3; generalised Davenport items need
k - kappa zero-mass brackets; single-interval and E = 0 arc systems have empty m-ranges in IIIb (Sec. 6 of v3).

## Fix map v3 -> v4

1. New: Fact 2.2 (run sizes), Lemmas 4.1-4.2 (labels, balanced kill) for every q, Lemma BAL (general d), Theorem K2P and
   Corollary K2P-num.  Theorem FP is restated as the R = p case of Lemma 4.2.
2. v3 erratum-1 (scope sentence) is incorporated: the CJ'''' Corollary 2 range at R = p is kappa <= 2, or 4 kappa - 4 <= p
   and 6 kappa <= p + 10.
3. Sec. 7 replaces v3 Sec. 6.
