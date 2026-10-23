# Theorem IND*: the independent-set certificate for general item-(iii) words (a replacement for (H))

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).
Written in c4/ after host clock 2026-10-17T14:08:11-0700 (freeze time and SHA-256 in c4/out/freeze.txt).  Task OlsonRunCount4, target
T4 (the item-(iii) words that fail (H)).  Imported: Lemma H with the 07:39 correction and the Claim in Lemma BC
(../../../inverse-parity/proof-PAR-K0.md Secs. 1-2).  This file generalises c4/proof-IND-r1.md (Theorem IND = the case
B = 1, all runs single letters, fixed seed) to every NMH word with R <= 2p - 3; the four steps are the same.
Scope: every item-(iii) word (more generally every NMH word with R <= 2p - 3) whose parameters satisfy the finitely
checkable hypotheses (W), (R), (C), (L*) below.  NO hypothesis (H) is needed.  NOT a proof of NMH(p), MIX_DEF_HIGH(p),
RUNS(p), INV or ordered Olson for D_{2p}.

## 0. Setting

p >= 5 prime; w an NMH word (all reflection runs odd, every rotation run pure or a (1,1)-pair, 1 <= B <= kappa - 1,
B <= A <= 2p - 1) with k runs, R = 2p - k + 2 kappa <= 2p - 3, kB := kappa - B >= 1, D := A - B = 2p - k + 2kB, excess
E := R - k.  T: any set of N >= 2 pairwise non-adjacent runs that are single letters rho_1 (d_t = 1, r_t = 1).
Availability: the runs that are not single rho_1 letters are the anti runs and pairs (at most B of them) and the
multi-letter aligned runs (at most E), so there are n1 >= k - B - E single rho_1 runs, and choosing every other run in
each maximal block of consecutive ones gives N >= ceil((k - B - E)/2) pairwise non-adjacent ones; every N between 2 and
that bound is admissible.
For S subset of T with |S| = j: S is proper, m(S) = j, D_S = j, and S^c has m = j, D_{S^c} = D - j.  Lemma H (beta = 0):
   L_j := lambda(S) = min(p - j + 1, 2j - kB, floor((j + B)/2) + 1),
   lambda(S^c) = min(p - j + 1, D - kB, floor((D - j + B)/2) + 1),   U_j := p - lambda(S^c),
and if w avoids, u_S lies outside [U_j + 1 - p, L_j - 1] (mod p).  (In NMH the empty and full patterns never kill.)
(For all-singleton words D - kB = p - B; for W(p, kB) also B = 1 and these are the arcs of c4/proof-IND-r1.md.)

## 1. Theorem IND*

Hypotheses on (p, k, kB, B, D, N):
 (W) L_j <= U_j for 1 <= j <= N  [if it fails for some j, any j-subset of T already has a full window];
 (R) R* := { y in [L_1, U_1] : for every 1 <= s <= N - 1 with A_s := [L_{s+1} - U_s, U_{s+1} - L_s] of fewer than p
     integers, y is congruent mod p to an element of A_s } is nonempty  [if empty, see the proof]; put
     alpha := min R*, h := max R*;
 (C) for 1 <= j <= N - 1:  max(L_j, j alpha) + alpha >= U_{j+1} + 1 - p  and  min(U_j, j h) + h <= p + L_{j+1} - 1;
 (L*) for every integer X with max(L_N, N alpha) <= X <= min(U_N, N h), the balanced vector b with sum X (q := floor(X/N),
     rho := X - qN entries q + 1 and N - rho entries q) violates s_j(b) >= L_j or t_j(b) <= U_j for some 1 <= j <= N - 1,
     where s_j(b) = jq + max(0, j - (N - rho)) and t_j(b) = jq + min(j, rho) (sums of the j smallest / largest entries).
**Theorem IND*.**  If (W) fails, or (R) fails, or (W), (R), (C), (L*) all hold, then w has an identity 2p-subword.

Proof.  Suppose w avoids.  If L_j > U_j for some j <= N, then lambda(S) + lambda(S^c) >= p + 1 for a j-subset S of T, so
its window [1 - lambda(S^c), lambda(S) - 1] has >= p integers and contains u_S (mod p): contradiction.  So (W) holds and
every j-subset sum u_S lies in the arc [L_j, U_j] (mod p).
Step 1 (seed).  Let t in T and 1 <= s <= N - 1.  As |T - {t}| = N - 1 >= s there is an s-subset S of T - {t}; then
u_t = u_{S u {t}} - u_S lies in [L_{s+1}, U_{s+1}] - [L_s, U_s] = A_s (mod p).  Also u_t lies in [L_1, U_1] (mod p) (the
singleton {t}), and the canonical lift x_t (the unique integer in [L_1, U_1] congruent to u_t; unique as U_1 - L_1 < p by
(W)) therefore lies in R*.  So R* is nonempty (if (R) fails we already have a contradiction) and alpha <= x_t <= h.
Step 2 (size chain).  For every 1 <= j <= N and every j-subset S of T, L_j <= X_S <= U_j (X_S := sum_{t in S} x_t): for j = 1
by the choice of lifts; for S' = S u {t} (|S| = j <= N - 1), X_S is in [max(L_j, j alpha), min(U_j, j h)] and x_t in
[alpha, h], so X_{S'} lies in [max(L_j, j alpha) + alpha, min(U_j, j h) + h], inside [U_{j+1} + 1 - p, p + L_{j+1} - 1] by (C);
X_{S'} = u_{S'} (mod p), and the Claim of Lemma BC gives L_{j+1} <= X_{S'} <= U_{j+1}.
Step 3 (balanced reduction).  Sort the lifts; s_j, t_j := sums of the j smallest / largest.  By Step 2, s_j >= L_j and
t_j <= U_j (1 <= j <= N), and X := X_T lies in [L_N, U_N] and in [N alpha, N h].  Let b be the balanced vector with sum X.
Majorization: t_j(b) <= t_j and s_j(b) >= s_j for every j.  [Let y_1 >= ... >= y_N be the lifts.  If y_j >= q + 1, then
t_j >= j(q + 1) >= t_j(b).  If y_j <= q, then y_i <= q for i > j, so y_{j+1} + ... + y_N <= (N - j) q <= (sum of the N - j
smallest entries of b), and t_j = X - (y_{j+1} + ... + y_N) >= X - (that sum) = t_j(b).  Finally s_j = X - t_{N-j} <=
X - t_{N-j}(b) = s_j(b).]  Hence s_j(b) >= L_j and t_j(b) <= U_j for 1 <= j <= N - 1, contradicting (L*).  []

Remarks.  (1) Theorem IND (c4/proof-IND-r1.md) is the case B = 1, E = 0, N = ceil((p + kB)/2) with the single seed
s = max(delta, j1): its R* is contained in that seed's lift range, (C) there implies (C) here, and its Step 4 shows (L*).
Corollary IND-I (all primes p >= 11, (3p + 1)/7 <= kB <= (3p - 7)/5) is therefore a closed-form infinite family of words
excluded by Theorem IND*; for p >= 17 these words fail (H) (3kB >= p + 5, so the anti pairs are not certified,
c4/proof-NOBCplus-r3.md Lemma NOLIFT(a)).  (2) The certificate uses only subsets of T (one parity-type class of single
rho_1 runs); it never certifies a pattern by singleton extension.  It cannot work when the parity-class system is
feasible, e.g. W(37, 14) (c4/out/indep_all.txt).

## 2. Exact computations [F] (aids; never hypotheses)

* ind_star3.py (out/ind_star3.txt): all-singleton words (E = 0), every item-(iii) class (k, B) for primes 11 <= p <= 43
  (3,221 classes), N = ceil((k - B)/2) downwards: the hypotheses hold for 2,623 classes (for every word of the class, any
  anti positions).  Cross-check with the parity-class DFS indepB.cpp (out/indepB_all.txt, no lifting): 0 classes covered
  here are feasible there; of the uncovered ones, 492 are feasible there (no T-based argument exists) and 106 are
  infeasible corners with kB or B close to p.  Literal replay (Part B, p <= 19, random anti positions, 7,110 vectors): every
  vector gives a subset of T whose half-sum lies in its explicitly recomputed Lemma H window; 0 failures.  Mutation
  controls: T shrunk by two (41 no-kill), windows shrunk by one (2,642 no-kill), seed skipped (49 no-kill).
* ind_star_ex.py (out/ind_star_ex.txt): general classes (k, kappa, B) of item (iii) with worst-case N = ceil((k - B - E)/2):
  p = 11..31, 7,264 classes, hypotheses hold for 3,947.  Every open class of the c3 map with reason notH_cert
  (../c3/out/map3_p11.txt, map3_p13.txt; all-singleton and excess 2 or 4) satisfies the hypotheses with worst-case N, so
  every (H)-failing word of the c3 samples at p = 11 (5,318 item-(iii) words) and p = 13 (746) is excluded by Theorem IND*;
  the only c3-open words not covered are the 3 + 4 words with reason "hyp" ((H) holds, Theorem C's even-run condition
  fails; excess 6 or 8).
* ind_star_word.py (out/ind_star_word.txt): 420 explicit random item-(iii) words with excess (p = 11..31), T built from the
  actual runs: 343 satisfy the hypotheses; 10,290 replayed vectors, every kill re-checked with lambda computed from the
  word's d_t; 0 failures; mutation (windows shrunk by one): 3,788 no-kill.
