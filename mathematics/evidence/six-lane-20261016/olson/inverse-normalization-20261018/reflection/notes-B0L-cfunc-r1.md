# B = 0, k >= p + 1: the c-function, Lemma SIGMA-2P and Theorem B0S++ (working file towards the B = 0 package)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T06:01:56-0700.  Status: Secs. 1-3 written proofs [W], UNREVIEWED;
Sec. 4 exact description of what remains.  Builds on proof-B0S-r4.md (d76a179d...b89c) and proof-B0SP-r1.md (2921280e...e2d7,
frozen, queued for review).  Scope: B = 0 only; no statement about rotation values, INV*(p), REFL(p) or ordered Olson.

## 1. Setting and the c-function

w: a word of length 4p - 2 over D_(2p), p >= 5 prime, all rotation letters rho_1 (B = 0), all maximal constant blocks odd,
kappa = p - 1 - H >= 1, genuine empty runs allowed; R = 2p - k + 2 kappa <= 2p - 1 (else rho_1^(2p)).  g(E) := min(E - kappa,
floor(E/2)) (= g_1(E) of B0S; the cap p - 1 is inactive for E <= R).  For a proper cyclic interval Q of runs, m_Q := R_Q,
I(Q) = [-g(R - m_Q), g(m_Q)] (Lemma H0), gap(Q) := [g(m_Q) + 1, p - g(R - m_Q) - 1].  Suppose w avoids.  Then every I(Q) is
nonempty and not full when R >= 2 kappa + 1 (B0S Step 0 computation), so gap(Q) is a set of between 1 and p - 1 consecutive
integers containing exactly one representative of every residue outside I(Q), and u_Q lies outside I(Q) mod p.
Singleton representatives: w_t := the representative of u_t in gap({t}); W(Q) := sum over Q of w_t (= u_Q mod p).
**Definition.**  c(Q) := the unique integer with W(Q) - c(Q) p in gap(Q).  J := (sum_t w_t)/p - 1 (an integer, as sum u_t = 0).
**Lemma C1.**  (a) c({t}) = 0.  (b) c(Q) + c(Q^c) = J for every proper interval Q; in particular J = c([k] \ {t}) for every t.
(c) Let Q = Q1 u Q2 be a split of a proper interval into two consecutive nonempty sub-intervals, Q3 := Q^c, m_i := m_(Q_i).
  (A') g(m1) + g(m2) + g(m3) >= -2 implies c(Q) >= c(Q1) + c(Q2);
  (B') g(m2 + m3) + g(m1 + m3) + g(m1 + m2) >= p - 2 implies c(Q) <= c(Q1) + c(Q2).
Proof.  (a) by definition.  (b) gap(Q^c) = p - gap(Q) (as sets) and W(Q) + W(Q^c) = (J + 1)p, so W(Q) - (J - c(Q^c))p lies in gap(Q).
(c) X := W(Q) - (c(Q1) + c(Q2))p lies in gap(Q1) + gap(Q2) = [U1 + U2 + 2, 2p - L1 - L2 - 2] (U_i = g(m_i), L_i = g(R - m_i)) and
X = u_Q mod p.  Under (A'), X >= -L_Q (L_Q = g(m3)); X avoids I(Q) + pZ, so X >= U_Q + 1, and W(Q) - c(Q)p <= p - L_Q - 1 gives
(c(Q) - c1 - c2)p >= U_Q + L_Q + 2 - p > -p.  Under (B'), X <= p + U_Q (as L1 + L2 + U_Q >= p - 2); X avoids I(Q) + p, so
X <= p - L_Q - 1, and W(Q) - c(Q)p >= U_Q + 1 gives (c1 + c2 - c(Q))p >= U_Q + L_Q + 2 - p > -p.  (U_Q + L_Q >= 0: I(Q) nonempty.)  []
So c is additive across every split satisfying (A') and (B'), and Sigma w_t = p iff J = 0.  [Remark: J = 0 is exactly what B0S
needs: its Secs. 3-5 use only integer lifts x_t = u_t in the singleton gaps with sum x_t = p; see Sec. 3.]

## 2. Regime R >= 4 kappa + 1

Put Delta := k - p - kappa - 1 = p + kappa - 1 - R.  For an avoider, P0 (proof-K0star-r2.md, from Theorem P) gives
n_E + #{even nonempty runs} <= 2 kappa, and k - n_E <= R, so k <= p + 2 kappa, R >= p and Delta <= kappa - 1.
**Lemma C2.**  Let R >= 4 kappa + 1.  (a) (A') holds for every split.  (b) (B') holds for every split whose three pair sums
m1 + m2, m1 + m3, m2 + m3 are all >= 2 Delta.  (c) c(Q) >= 0 for every proper interval Q, hence 0 <= c(Q) <= J.
Proof.  (a) Write g(m) >= m - kappa and g(m) >= (m - 1)/2; with m1 + m2 + m3 = R: if no m_i <= 2 kappa the sum is >= (R - 3)/2 >= 0;
one small: >= m1 - kappa + (R - m1 - 2)/2 >= (R - 2)/2 - kappa >= 0; two small: >= (m1 + m2)/2 + (R - 1)/2 - 2 kappa >= 0; three
small: = R - 3 kappa > 0.  (b) Any two pair sums add up to >= R >= 4 kappa + 1, so at most one pair sum s is <= 2 kappa.  If none is,
(B') >= R - 3/2 >= p - 2 (R >= p).  If one is, (B') >= (s - kappa) + (2R - s - 2)/2 = R - kappa - 1 + s/2 >= p - 2 iff s >= 2 Delta.
(c) Induction on |Q| with (a) and Lemma C1(c), base Lemma C1(a); then c(Q^c) >= 0 and Lemma C1(b).  []
**Lemma SIGMA-2P.**  Let R >= 4 kappa + 1 and suppose there are two disjoint adjacent pairs of runs {s, s+1}, {t, t+1} with
r_s + r_(s+1) >= 2 Delta and r_t + r_(t+1) >= 2 Delta (automatic if Delta <= 0, as k >= 4).  Then J = 0, i.e. sum_t w_t = p.
Proof.  Q := the interval from s to t - 1; it contains s, s + 1, and Q^c (from t to s - 1) contains t, t + 1.  For the chain
Q_j := [s, j], j = s + 1, ..., t - 1, split Q_j = Q_(j-1) u {j}: the pair sums are m(Q_j) >= r_s + r_(s+1), m({j} u Q_j^c) >=
m(Q^c) >= r_t + r_(t+1), and m(Q_(j-1) u Q_j^c) >= m(Q^c); all >= 2 Delta, so by Lemma C2(b) and C1(c), c(Q_j) <= c(Q_(j-1)) + 0.
Hence c(Q) <= c({s}) = 0, and c(Q) = 0 by Lemma C2(c).  Symmetrically c(Q^c) = 0 (chain [t, j]; the pair sums contain {t, t+1}
or Q).  Lemma C1(b): J = c(Q) + c(Q^c) = 0.  []

## 3. Theorem B0S++

**Theorem B0S++.**  Let w be as in Sec. 1 with R >= 4 kappa + 1, and suppose that k <= p + kappa + 1 or that there are two
disjoint adjacent pairs of runs each of mass >= 2(k - p - kappa - 1).  Then w has an identity 2p-subword.
Proof.  Suppose w avoids.  By Lemma SIGMA-2P, x_t := w_t satisfy sum x_t = p.  Each x_t lies in gap({t}) = [U^t + 1, p - L^t - 1].
Then B0S-r4 Secs. 3-5 apply verbatim with these x_t: a defect (bh_t = 2 x_t - r_t <= 0) has x_t <= floor(r_t/2), so the lower end
U^t + 1 forces U^t = r_t - kappa and (2.1) delta_t <= 2 kappa - 2 - r_t; empty defects lie in [1 - kappa, -1]; non-defects have
bh_t >= 1; sum bh_t = 2p - R = k - 2 kappa >= 1.  The numerical conditions used in Cases I, II are exactly those re-checked in
proof-B0SP-r1.md Sec. 3 (R >= 4 kappa + 1, 2 kappa <= p - 1, k >= 2 kappa + 1); here 2 kappa <= p - 1 follows from
4 kappa + 1 <= R <= 2p - 1.  Every case ends with a pattern P with x(P) in I(P): contradiction.  []
Remarks.  (1) B0S++ contains B0S+ (the case k <= p + kappa + 1, where Delta <= 0), and its proof replaces B0S's Step 1 (prefix
lifts and the eight-case bound) by Lemma SIGMA-2P; (H3) of B0S+ is implied by (H2).  (2) For Delta = 1 the two-pair condition
always holds in regime R >= 4 kappa + 1: if all mass-2 adjacent pairs met one run h, the path [k] \ {h} would alternate single
rotations and empty runs, forcing k <= 4 kappa + 2 and p <= 3 kappa, whereas R = p + kappa - 2 >= 4 kappa + 1 gives p >= 3 kappa + 3.

## 4. What remains for B = 0, k >= p + 1 (exact)

(T) Thin words in regime R >= 4 kappa + 1: Delta >= 2 and every two adjacent pairs of mass >= 2 Delta share a run (all heavy pairs
contain one run h).  These exist (e.g. p = 17, kappa = 4, k = 24, R = 18: fifteen runs rho_1, one run rho_1^3 flanked by empty runs,
eight empty runs; all adjacent pairs have mass <= 3 < 4 = 2 Delta).  Needed: J = 0 there, or a direct kill.  Partial facts: a
shortest interval Q with c(Q) >= 1 is light (m_Q < 2 Delta) or co-light; if light, m_Q <= 2 Delta - 2 and W(Q) >= p + m_Q - kappa + 1;
if moreover |Q| >= 3 and some extension of Q by at most |Q| - 2 runs has mass >= 2 Delta, a split into two shorter intervals is
(B')-good and gives a contradiction.
(III) R <= 4 kappa (then kappa >= p/4, k >= 2p - 2 kappa): (A') can fail, c need not be superadditive, and Case I's (L3) can fail
(E9b example p = 7, kappa = 3, R = 7).  Needed: a substitute for SIGMA and a selection lemma.
Finite aids (not premises): E11 (plan-E11.md 2ff0da78...28a5, code/e11_sigma_search.py 265e0a9e...9e895,
out/e11_sigma_search.json): 436,534 random assignments with sum w_t in {0, 2p} at p = 7, 11, 13: none was interval-feasible.
