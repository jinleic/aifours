# Theorem B0S++: B = 0 beyond k <= p (R >= 4 kappa + 1, and k <= p + kappa + 1 or two disjoint heavy adjacent run pairs)

Owner OlsonReflectionRigidity.  r1 (2e9088ce...8b3a) written after host clock 2026-10-18T06:16:32-0700.  Status: written proof [W], UNREVIEWED; frozen for review.
r2 (c44a156f...3d56) written after 2026-10-18T06:17:44-0700 (aid provenance, fix map Sec. 5);
r3 (35f3b248...4282) written after 2026-10-18T06:18:23-0700: folds in the Codex review of proof-B0SP-r1.md
(R/olson-b0sp-r1-codex-v1.note.md, 8d6b66ab...4ca7: ACCEPT-WITH-FIXES 0/0/1 + 2 notes), fix map Sec. 6;
r4 (669e5d97...24dc) written after 2026-10-18T06:20:14-0700: one justification in the Corollary corrected (fix map Sec. 7); reviewed by Codex
(R/olson-b0spp-r4-codex-v1.note.md, b05a8059...8d9a: ACCEPT-WITH-FIXES 0/0/1).  r5 (this file) written after 2026-10-18T06:29:28-0700:
errata only (that MINOR), fix map Sec. 8; frozen for review.
Supersedes proof-B0SP-r1.md (2921280e...e2d7, Theorem B0S+, kept unchanged; B0S+ is the special case k <= p + kappa + 1 of
B0S++) and Secs. 1-3 of notes-B0L-cfunc-r1.md (62a130f2...acf4).  Self-contained relative to proof-B0S-r4.md (d76a179d...b89c;
its r2/r3 mathematics is parent-accepted, R/olson-reflection-smallk-parent-verdict-v1.md b71fcaf4...13b8).
Scope: B = 0 only; no statement about rotation values, INV*(p), REFL(p) or ordered Olson.

## 0. Statement, imports, import map

**Theorem B0S++.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters all equal one rho_x,
x != 0 (normalised rho_1, B = 0), with F, R >= 1, all maximal constant reflection blocks of odd length, kappa = p - 1 - H >= 1, and
any number of genuine empty runs.  Put Delta := k - p - kappa - 1.  Suppose
   (H) R >= 4 kappa + 1,  and   (D) Delta <= 0, or there are two disjoint pairs {s, s+1}, {t, t+1} of cyclically adjacent runs
       with r_s + r_(s+1) >= 2 Delta - 1 and r_t + r_(t+1) >= 2 Delta - 1.
Then w has an identity 2p-subword.
**Corollary.**  RES_<(p) has no avoider with B = 0 satisfying (H) and (D).  In particular none with B = 0, (H) and Delta <= 1
(for Delta = 1 the pairs in (D) only need mass >= 1; two disjoint pairs each containing a nonempty run exist as soon as two runs
are nonempty and k >= 4; here k >= p + 1 >= 6, and an avoider has at least k - n_E >= k - 2 kappa >= p + 1 - 2 kappa >= 2
nonempty runs (Sec. 1: n_E <= 2 kappa and 2 kappa <= p - 1).)
[r3] After the trivial cut (R >= 2p is solvable by rho_1^(2p), so assume R <= 2p - 1), k <= p implies (H) (then R >= p + 2 kappa
and p >= 2 kappa + 1, B0S-r4 Sec. 1) and Delta <= -kappa - 1 < 0; so B0S++ contains Theorem B0S.  Without the cut the literal
implication fails, e.g. (p, kappa, k, R) = (5, 3, 5, 11) with blocks (3,1,1,1,1) and runs (3,2,2,2,2) has k <= p but R < 4 kappa + 1
(Codex MINOR on B0SP-r1).  With Delta <= 0, B0S++ is Theorem B0S+ of proof-B0SP-r1.md (its (H3) follows from (H) and R <= 2p - 1).
[r3, Codex note] For k >= p + 1, (H) forces kappa <= (p - 3)/2: R = 2p - k + 2 kappa <= p - 1 + 2 kappa and R >= 4 kappa + 1 give
2 kappa <= p - 2, and p is odd.

Imports (exact):
* the Lemma H0 instance of proof-B0S-r4.md (B = 0, beta = 0, every m >= 1; its "Imports" paragraph derives it from GRX):
  for a proper pattern P with m intervals and R_P = E, I(P) = [-g_m(R - E), g_m(E)], g_m(E) = min(p - m, E + m - kappa - 1,
  floor(E/2)); P kills (w is solvable) if some integer = u_P (mod p) lies in I(P);
* fact (P0) of proof-K0star-r2.md L73-75 (parent-accepted with K0*, R/olson-reflection-K0star-RED-parent-verdict-v1.md
  879aeee7...c02a): an avoider has e_R <= e_F + 2 kappa, where e_R counts runs of even length, EMPTY RUNS INCLUDED; here e_F = 0;
* proof-B0S-r4.md Secs. 3-5 (kill conditions, Case I, Case II), used with the lifts x_t of Sec. 2 below.

| piece here | source | status |
|---|---|---|
| Sec. 1 facts (R >= p, Delta <= kappa - 1, 2 kappa <= p - 1, windows nonempty) | new (uses P0) | written here |
| Lemma C1 (c-function, complement rule, split rule) | new | written here |
| Lemma C2 ((A') always, (B') from pair sums, c >= 0) | new | written here |
| Lemma SIGMA-2P (sum of singleton representatives = p) | new | written here; replaces B0S-r4 Sec. 2 (prefix lifts and the eight-case Step 1) |
| defect bound (2.1) | B0S-r4 Sec. 2 last part | re-derived from the singleton gap (Sec. 3) |
| kill conditions, Case I, Case II | B0S-r4 Secs. 3-5 | verbatim; every numerical inequality re-checked in Sec. 3 under (H) |

## 1. Set-up and facts

All blocks odd: o_F = k, beta(P) = 0, R = 2p - k + 2 kappa.  If R >= 2p, rho_1^(2p) is an identity, so R <= 2p - 1, k >= 2 kappa + 1.
Suppose w avoids.  (P0) gives n_E <= 2 kappa (n_E := number of empty runs); the k - n_E nonempty runs carry R letters, so
k - n_E <= R; hence k <= R + 2 kappa = 2p - k + 4 kappa, i.e. k <= p + 2 kappa, so R >= p and Delta <= kappa - 1.  By (H) and R <= 2p - 1,
2 kappa <= p - 1.  Write g(E) := g_1(E) = min(E - kappa, floor(E/2)) for 0 <= E <= R (the cap p - 1 is inactive); g(E) = E - kappa iff
E <= 2 kappa; g(E) = floor(E/2) >= (E - 1)/2 for E >= 2 kappa - 1, and in general g(E) >= min(E - kappa, (E - 1)/2)
[r5 erratum].
Interval windows.  For a proper cyclic interval Q of runs with mass m_Q := R_Q: I(Q) = [-g(R - m_Q), g(m_Q)].  It is nonempty:
g(E) + g(R - E) >= 0 for 0 <= E <= R, because if one term is truncated, by the symmetry E <-> R - E say g(E) = E - kappa, then the sum
is >= min(R - 2 kappa, (E + R - 1)/2 - kappa) >= min(R - 2 kappa, (R - 1)/2 - kappa) >= 0 by (H), and otherwise it is >= R/2 - 1 >= 0.
It is not full (w avoids).  So gap(Q) := [g(m_Q) + 1, p - g(R - m_Q) - 1] consists of between 1 and p - 1 consecutive integers and
contains exactly one representative of every residue outside I(Q); u_Q lies outside I(Q) mod p.

## 2. The c-function and Lemma SIGMA-2P

Singleton representatives: w_t := the representative of u_t in gap({t}); W(Q) := sum of w_t over t in Q, so W(Q) = u_Q (mod p).
c(Q) := the unique integer with W(Q) - c(Q) p in gap(Q); J := (sum_t w_t)/p - 1, an integer since sum_t u_t = 0.
**Lemma C1.**  (a) c({t}) = 0.  (b) c(Q) + c(Q^c) = J for every proper interval Q; in particular J = c([k] \ {t}) for every t.
(c) Let Q = Q1 u Q2 with Q1, Q2 nonempty consecutive sub-intervals, Q3 := Q^c, m_i := m_(Q_i) (m1 + m2 + m3 = R).
   (A') g(m1) + g(m2) + g(m3) >= -2 implies c(Q) >= c(Q1) + c(Q2);
   (B') g(m2 + m3) + g(m1 + m3) + g(m1 + m2) >= p - 2 implies c(Q) <= c(Q1) + c(Q2).
Proof.  (a) Definition.  (b) gap(Q^c) = [g(R - m_Q) + 1, p - g(m_Q) - 1] = p - gap(Q) (as sets) and W(Q) + W(Q^c) = (J + 1) p, so
W(Q) - (J - c(Q^c)) p = p - (W(Q^c) - c(Q^c) p) lies in gap(Q).  (c) Write U_i = g(m_i), L_i = g(R - m_i), U_Q = g(m1 + m2),
L_Q = g(m3).  X := W(Q) - (c(Q1) + c(Q2)) p lies in gap(Q1) + gap(Q2) = [U1 + U2 + 2, 2p - L1 - L2 - 2] and X = u_Q (mod p), so X
avoids I(Q) + pZ.  Under (A'), X >= -L_Q, hence X >= U_Q + 1; as W(Q) - c(Q) p <= p - L_Q - 1, (c(Q) - c(Q1) - c(Q2)) p >= U_Q + L_Q
+ 2 - p > -p (U_Q + L_Q >= 0).  Under (B'), X <= p + U_Q (as L1 + L2 + U_Q >= p - 2), hence X <= p - L_Q - 1; as W(Q) - c(Q) p >=
U_Q + 1, (c(Q1) + c(Q2) - c(Q)) p >= U_Q + L_Q + 2 - p > -p.  []
**Lemma C2.**  (a) (A') holds for every split.  (b) (B') holds for every split whose three pair sums m1 + m2, m1 + m3, m2 + m3 are
all >= 2 Delta - 1.  (c) c(Q) >= 0 for every proper interval Q; hence 0 <= c(Q) <= J and J >= 0.
Proof.  (a) Call m small if m <= 2 kappa.  None small: sum >= (R - 3)/2 >= 0.  One small (m1): >= m1 - kappa + (R - m1 - 2)/2 >=
R/2 - 1 - kappa >= 0.  Two small (m1, m2): >= m1 + m2 - 2 kappa + (R - m1 - m2 - 1)/2 >= (R - 1)/2 - 2 kappa >= 0.  Three small:
= R - 3 kappa > 0.  (All by (H).)  (b) The pair sums s1, s2, s3 add up to 2R and any two add up to >= R >= 4 kappa + 1, so at most
one, say s, is <= 2 kappa.  If none is, (B') >= (2R - 3)/2, so (B') >= R - 1 >= p - 1.  If s <= 2 kappa, the other two s', s'' are
floor terms with s' + s'' = 2R - s, and floor(s'/2) + floor(s''/2) >= R - 1 - s/2 if s is even, = R - (s + 1)/2 if s is odd; so
(B') >= R - kappa - 1 + ceil(s/2), which is >= p - 2 iff ceil(s/2) >= Delta (as Delta = p + kappa - 1 - R), i.e. iff s >= 2 Delta - 1.
(c) Induction on |Q|: |Q| = 1 is C1(a); for |Q| >= 2 use any split, (a) and C1(c).  Then c(Q^c) >= 0 and C1(b).  []
**Lemma SIGMA-2P.**  Under (H) and (D), J = 0, i.e. sum_t w_t = p.
Proof.  If Delta <= 0, every pair sum is >= 0 >= 2 Delta - 1, so by C2(b) and C1(c) c(Q) <= c(Q1) + c(Q2) for every split; induction
gives c(Q) <= 0, so c = 0 on all proper intervals and J = c([k] \ {t}) = 0.  Otherwise let {s, s+1}, {t, t+1} be as in (D);
Q := the interval from s to t - 1 contains s, s + 1, and Q^c (from t to s - 1) contains t, t + 1 (the pairs are disjoint).  For
j = s + 1, ..., t - 1 split Q_j := [s, j] as Q_(j-1) u {j}.  The pair sums are m(Q_j) >= r_s + r_(s+1), m({j} u Q_j^c) >= m(Q^c) >=
r_t + r_(t+1) and m(Q_(j-1) u Q_j^c) >= m(Q^c); all are >= 2 Delta - 1.  By C2(b) and C1(c), c(Q_j) <= c(Q_(j-1)), so c(Q) <= c({s})
= 0 and c(Q) = 0 by C2(c).  Symmetrically (chain [t, j]) c(Q^c) = 0.  C1(b): J = c(Q) + c(Q^c) = 0.  []

## 3. Proof of Theorem B0S++ (B0S-r4 Secs. 3-5 with x_t := w_t)

Suppose w avoids.  Put x_t := w_t; by SIGMA-2P, sum x_t = p, so bh_t := 2 x_t - r_t satisfies sum bh_t = 2p - R = k - 2 kappa, which
lies in [1, k - 1] (k >= 2 kappa + 1, kappa >= 1); x(P) = u_P (mod p) for every pattern P.  Defects (B0S-r4 (2.1), re-derived): if
bh_t <= 0 then x_t <= floor(r_t/2); x_t >= g(r_t) + 1 (lower end of gap({t})), so g(r_t) < floor(r_t/2), i.e. g(r_t) = r_t - kappa,
and delta_t := -bh_t = r_t - 2 x_t <= 2 kappa - 2 - r_t; an empty defect has x_t in [1 - kappa, -1] (x_t != 0 by genuineness);
r_t + delta_t is even and >= 2.  Non-defects have bh_t >= 1, empty non-defects bh_t >= 2.  This is exactly the input of B0S-r4
Secs. 3-5, which use nothing about the lifts beyond these facts.  Their numerical conditions, re-checked under (H), 2 kappa <= p - 1
and k >= 2 kappa + 1:
* Sec. 3: Z := defects is nonempty (else sum bh >= k) and proper (sum bh >= 1); Phi(P) is even.
* Case I (Phi(Z) >= 2 kappa + 2): the greedy P has 2 kappa + 2 <= Phi(P) <= 4 kappa.  (U1), (L1): Phi(P) <= 4 kappa <= 2p.
  (L2): 4 kappa <= 2R - 2 kappa - 2 iff R >= 3 kappa + 1.  (L3): delta_P <= Phi(P) - 2 <= 4 kappa - 2 <= R - 1 iff R >= 4 kappa - 1.
  (U2), (U3) by construction.  All hold by (H).
* Case II (Phi(Z) <= 2 kappa): delta_Z = 2 kappa - |Z| + s, |Z| <= kappa - m_Z, s <= g_Z - 2 m_Z, delta_Z - rho_Z >= 4 m_Z and
  2 <= d <= g_Z <= kappa - 1 are generic.  |F| >= d/2 needs k >= 2 + 2|Z| - rho_Z: true as k >= 2 kappa + 1 > 2 kappa >= 2 + 2|Z|.
  P = Z u W is proper (B0S-r4 Sec. 5, generic).  (U3): delta_P >= kappa + 1 - (kappa - 1)/2 > 0.  (L3): delta_P <= delta_Z <= 2 kappa - 2
  <= R - 1.  (U1): <= r_y + 1 <= 2p for W = {y}; <= 3 kappa - 7 < 2p otherwise.  (L1): <= 4 kappa - 4 < 2p.  (L2): W = {y}:
  2 kappa + r_y - 7 <= 2R - 2 kappa - 2 iff r_y <= 2R - 4 kappa + 5, true as r_y <= R and R >= 4 kappa - 5; otherwise
  4 kappa - 4 <= 2R - 2 kappa - 2 iff R >= 3 kappa - 1.  All hold by (H).
Every case yields a pattern P with x(P) in I(P), i.e. an identity 2p-subword: contradiction.  []

## 4. Remarks

(1) Where empty runs enter: zero-mass intervals in Sec. 1-2 (masses in [0, R], windows of mass-0 intervals [-g(R), -kappa]);
genuineness x_t != 0 for empty defects; P0 counts empty runs as even runs; Case II of B0S-r4 (needs two empty defects).
(2) What remains for B = 0, k >= p + 1: (T) thin words under (H): Delta >= 2 and every two adjacent pairs of mass >= 2 Delta - 1 share
a run (they exist, e.g. p = 17, kappa = 4, k = 24, R = 18: fifteen runs rho_1, one run rho_1^3 between two empty runs, eight empty runs;
heavy pairs need mass >= 3, and both contain the rho_1^3 run); (III) R <= 4 kappa.  Neither is claimed here.
(3) Finite aids (not premises): E11 (plan-E11.md 2ff0da78...28a5, out/e11_sigma_search.json): no interval-feasible datum with
sum w_t != p among 436,534 random assignments at p = 7, 11, 13.  E12 (plan-E12.md b1026438...9e5f, code/e12_thin_dfs.py
45c45093...68b3, out/e12_thin_dfs.json e8748f2b...6ab0): depth-first enumeration of interval-feasible
assignments of one thin datum (p = 13, kappa = 3, k = 19, empty runs at positions 1, 4, 7, 10, 13, 16, all other runs rho_1),
capped at 400,000 nodes: 218,273 interval-feasible leaves, all with J = 0; the first 20 are each killed by a 2-interval pattern.

## 5. Fix map r1 -> r2

Sec. 4(3) only: the depth-first aid quoted from an eval session in r1 (218,274 leaves, unsaved) is replaced by its saved,
reproducible version E12 (218,273 leaves: the session counted one node beyond the cap).  No statement or proof changed.

## 6. Fix map r2 -> r3 (Codex review of proof-B0SP-r1.md, applied to the shared statements)

1. Codex MINOR (B0SP-r1 L16, the containment B0S in B0S+): the containment remark of Sec. 0 now applies the trivial cut
   R <= 2p - 1 first; the reviewer's counterexample to the literal implication is recorded.  The Theorem itself was unaffected:
   its proof starts with the trivial cut (Sec. 1).
2. Codex note (nonemptiness of the new range forces kappa <= (p - 3)/2): recorded in Sec. 0.
3. Codex note (the eight case expressions of B0SP-r1 Step 1 are lower bounds from bounding floors, not exact values of S):
   not applicable here; B0S++ does not use B0SP's Step 1 (it is replaced by Lemma SIGMA-2P), and Lemma C2(b) states its
   bound as a lower bound with the parity cases made explicit.
The reviewer found no unrepaired use of k <= p in B0S-r4 Secs. 1-5; Sec. 3 of this file relies on that.

## 7. Fix map r3 -> r4 (author, before review)

Corollary (Sec. 0): the existence of two nonempty runs was justified by "R >= 2", which does not imply it (one run may carry
all rotations).  It now uses Sec. 1: an avoider has at least k - 2 kappa >= p + 1 - 2 kappa >= 2 nonempty runs.  For a non-avoider
there is nothing to prove.  No other change.

## 8. Fix map r4 -> r5 (errata only; Codex review of r4, R/olson-b0spp-r4-codex-v1.note.md)

Codex MINOR (r4 Sec. 1, L52-53): "g(E) >= (E - 1)/2 always" is false at small E (g(0) = -kappa; reviewer's example
(p, kappa, k, R) = (5, 1, 3, 9), r = (0, 1, 8), l = (3, 3, 3)).  Diff:
  r4:  E <= 2 kappa, and g(E) >= (E - 1)/2 always.
  r5:  E <= 2 kappa; g(E) = floor(E/2) >= (E - 1)/2 for E >= 2 kappa - 1, and in general g(E) >= min(E - kappa, (E - 1)/2).
Every later use of the floor lower bound is at a mass >= 2 kappa + 1 (the "floor" or "not small" cases of Sec. 1 and Lemma C2),
as the reviewer also checked; no other text changed.
