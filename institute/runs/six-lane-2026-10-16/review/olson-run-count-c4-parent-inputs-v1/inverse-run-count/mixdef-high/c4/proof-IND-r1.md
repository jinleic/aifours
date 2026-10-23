# Theorem IND (version r1): the parity-class (independent-set) certificate for W(p, kB) beyond Theorem W-ALL

Version r1, written 2026-10-17T13:58:32-0700: replaces the UNFROZEN draft c4/proof-IND.md, whose Sec. 3 misdescribed the [F] coverage
of the hypotheses (it said 'contiguous' and listed p = 17: 8..13, p = 23: 10..18; the receipt gives 7..13, 9..18 and
single holes at p = 67, 97, 107).  Secs. 0-2 (statements and proofs) are unchanged; Sec. 3 adds the DOB(p) coverage.

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).
Written in c4/ after host clock 2026-10-17T13:57:56-0700 (freeze time and SHA-256 in c4/out/freeze.txt).  Task OlsonRunCount4.
Imported (not re-proved): Lemma H with the 07:39 correction (../../../inverse-parity/proof-PAR-K0.md Sec. 1) and the Claim
in the proof of Lemma BC (same file, Sec. 2); the family W(p, kB) and formulas (0.1), (0.2) of c3/proof-WALL.md.
NOT used: Lemma L / singleton-extension certification of patterns with >= 2 runs (which fails for DOB*(p), see
c4/proof-NOBCplus-r3.md), and nothing about the anti run except that it lies outside T.
Scope: the single-letter family W(p, kB) (one anti run, B = 1) with kB in an explicit band (Corollary IND-I) and, more
generally, every (p, kB) satisfying the arithmetic hypotheses (S1)-(S3), (C), (L) below (finitely checkable for each
(p, kB)).  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), INV or ordered Olson for D_{2p}.

## 0. Setting and arcs

p >= 11 prime, kB an integer with 3kB >= p + 4 and kB <= p - 4; delta := p - kB (>= 4).  W(p, kB): anti run 0, aligned
runs 1, ..., n (n = p + kB), k = n + 1, B = 1, kappa - B = kB.  N := ceil((p + kB)/2) and T := {1, 3, 5, ..., 2N - 1}: N
aligned runs, pairwise non-adjacent in the k-cycle (2N - 1 <= n; run 1 is adjacent only to 0 and 2).  For S subset of T
with |S| = j >= 1: S is a proper pattern (its complement contains the anti run) with m(S) = j blocks and D_S = j, so by
(0.1), (0.2) of c3/proof-WALL.md (y = m = j, e = 0)
   L_j := lambda(S) = min(p - j + 1, 2j - kB, floor((j + 1)/2) + 1),
   lambda(S^c) = min(p - j + 1, p - 1, floor((p + kB - j)/2) + 1),   U_j := p - lambda(S^c) = max(j - 1, ceil((delta + j)/2) - 1)
(p - 1 - floor((p + kB - j)/2) = ceil((delta + j)/2) - 1; the term 1 of p - (p - 1) never wins as delta >= 4).  If w avoids,
Lemma H gives u_S notin [U_j + 1 - p, L_j - 1] (mod p), and (as w avoids) lambda(S) + lambda(S^c) <= p, i.e. L_j <= U_j; so
   u_S lies in the ARC [L_j, U_j] (mod p)   for every S subset of T, |S| = j.                                   (0.1)
Claim (Lemma BC): if y is an integer with y = u_S (mod p) and U_j + 1 - p <= y <= p + L_j - 1, then L_j <= y <= U_j.     (0.2)
Canonical lifts: x_t is the unique integer in [L_1, U_1] = [2 - kB, floor(delta/2)] with x_t = u_t (mod p) (unique as
U_1 - L_1 + 1 < p; it exists by (0.1)).  X_S := sum_{t in S} x_t.  The forbidden singleton window is
F_1 = [U_1 + 1, p + L_1 - 1] = [floor(delta/2) + 1, delta + 1].
j1 := min{ j >= 1 : 2j - kB >= floor((j + 1)/2) + 1 }.  The predicate is monotone in j (the left side grows by 2, the right
by at most 1), so it holds exactly for j >= j1; hence L_j = floor((j + 1)/2) + 1 whenever j >= j1 and p - j >= floor((j+1)/2).
Seed size s := max(delta, j1); A := [alpha, omega] with alpha := 3 - ceil(s/2), omega := floor(s/2) - 1;
r := -alpha = ceil(s/2) - 3, h := min(omega, floor(delta/2)).

## 1. Theorem IND

Hypotheses (arithmetic in p, kB only):
 (S1) s + 1 <= N;
 (S2) U_s = s - 1, U_{s+1} = s, L_s = floor((s + 1)/2) + 1, L_{s+1} = floor((s + 2)/2) + 1  (then [L_{s+1} - U_s, U_{s+1} - L_s] = A);
 (S3) omega <= delta + 1 and alpha >= 2 - kB;
 (C)  for every 1 <= j <= N - 1:  (C1) max(L_j, -jr) - r >= U_{j+1} + 1 - p   and   (C2) min(U_j, jh) + h <= p + L_{j+1} - 1;
 (L)  delta <= N - floor(j1/2) + 1, j1 <= N, L_{j1} = floor((j1 + 1)/2) + 1, delta <= N - 1, U_delta = delta - 1, U_N = N - 1.
**Theorem IND.**  If (S1)-(S3), (C) and (L) hold, no word of W(p, kB) is an avoider.

Proof.  Suppose w avoids.
Step 1 (seed: every lift is shallow).  Let t in T.  By (S1) there is S subset of T - {t} with |S| = s.  By (0.1),
u_t = u_{S u {t}} - u_S lies in [L_{s+1}, U_{s+1}] - [L_s, U_s] = [L_{s+1} - U_s, U_{s+1} - L_s] = A (mod p) (by (S2)).  So
u_t = y (mod p) for some integer y in [alpha, omega].  If y <= floor(delta/2), then y >= alpha >= 2 - kB = L_1 (S3), so y is in
[L_1, U_1] and x_t = y.  If y > floor(delta/2), then y is in [floor(delta/2) + 1, delta + 1] = F_1 (S3), so u_t lies in the
singleton window -- impossible.  Hence  -r = alpha <= x_t <= h  for every t in T.
Step 2 (size chain).  Claim: L_j <= X_S <= U_j for every 1 <= j <= N and every j-subset S of T.  For j = 1 this is the choice
of x.  Let 1 <= j <= N - 1, S' = S u {t} a (j + 1)-subset (S a j-subset, t notin S).  By induction and Step 1,
X_S is in [max(L_j, -jr), min(U_j, jh)] and x_t in [-r, h], so X_{S'} = X_S + x_t lies in [max(L_j, -jr) - r, min(U_j, jh) + h],
which by (C) is inside [U_{j+1} + 1 - p, p + L_{j+1} - 1]; X_{S'} = u_{S'} (mod p); by (0.2), L_{j+1} <= X_{S'} <= U_{j+1}.
Step 3 (two-valued reduction).  Sort the lifts x_(1) <= ... <= x_(N) and let s_j, t_j be the sums of the j smallest and of the
j largest.  By Step 2 (applied to those j-subsets) s_j >= L_j and t_j <= U_j for 1 <= j <= N, and X := s_N = X_T lies in
[L_N, U_N].  U_N = N - 1 by (L), and L_N >= 1 (p - N + 1 >= 1, 2N - kB >= p, floor((N + 1)/2) + 1 >= 1), so 1 <= X <= N - 1.
Let b be the 0/1 vector with X ones and N - X zeros (the balanced integer vector with sum X).  Majorization: for every j,
s_j(b) >= s_j and t_j(b) <= t_j.  [Proof: let y_1 >= ... >= y_N be the lifts in decreasing order, so t_j = y_1 + ... + y_j.  If
y_j >= 1, then t_j >= j >= min(j, X) = t_j(b).  If y_j <= 0, then y_i <= 0 for i > j, so t_j = X - (y_{j+1} + ... + y_N) >= X >=
min(j, X).  And s_j = X - t_{N-j} <= X - t_{N-j}(b) = s_j(b).]  Hence s_j(b) >= L_j and t_j(b) <= U_j for 1 <= j <= N.
Step 4 (contradiction).  At j = delta (delta <= N - 1): t_delta(b) = min(delta, X) <= U_delta = delta - 1, so X <= delta - 1.  At
j = j1 (<= N): s_{j1}(b) = max(0, j1 - (N - X)) >= L_{j1} = floor((j1 + 1)/2) + 1 >= 2, so j1 - N + X >= floor((j1 + 1)/2) + 1,
i.e. X >= N - floor(j1/2) + 1.  Together: N - floor(j1/2) + 1 <= delta - 1, contradicting (L).  []

Remarks.  (1) Only patterns inside T are used: the single seed difference u_{S+t} - u_S, the chain of Step 2 (every
subset of T), and in Steps 3-4 the sets of the j smallest / largest lifts.  No pattern needs singleton-extension
certification in the sense of Lemma L; Step 2 is a certification INSIDE T with the shallow seed range of Step 1 instead
of the singleton windows (with the singleton windows the chain fails at j = 2 exactly when NOLIFT(b) holds).
(2) The contradiction is an integrality one: Steps 1-2 hold for the real point x_t = constant (the analogue of the Lemma
NOLP point), and Step 3 replaces any integer profile by a 0/1 profile, which the arcs at j = delta and j = j1 cannot hold.

## 2. Corollary IND-I (a closed-form band)

**Corollary IND-I.**  Let p >= 11 be prime and kB an integer with (3p + 1)/7 <= kB <= (3p - 7)/5.  Then no word of W(p, kB)
is an avoider.
Proof.  We verify the hypotheses of Theorem IND.  The band gives 7kB >= 3p + 1, so 3kB >= p + 4 for p >= 13 (and for p = 11
the band is kB = 5, where 3kB = p + 4), and 5kB <= 3p - 7 gives kB <= p - 4.
j1.  Let c := ceil((2kB + 2)/3).  For j < (2kB + 2)/3 the predicate fails (j even: 2j - kB < j/2 + 1; j odd: 2j - kB <
(j + 1)/2 + 1), so j1 >= c.  If c is even, 3c >= 2kB + 2 gives 2c - kB >= c/2 + 1, so j1 = c; if c is odd, c + 1 is even and
satisfies the predicate.  Hence c <= j1 <= c + 1 <= (2kB + 7)/3.
Regime.  (2kB + 7)/3 <= p - kB iff 5kB <= 3p - 7; so j1 <= delta and s = delta.
(S1) N >= (p + kB)/2 >= p - kB + 1 = delta + 1 as 3kB >= p + 2.
(S2) U_delta = max(delta - 1, delta - 1) = delta - 1 and U_{delta+1} = max(delta, ceil((2 delta + 1)/2) - 1) = delta.
  L_delta: 2 delta - kB >= floor((delta + 1)/2) + 1 by monotonicity (delta >= j1), and p - delta + 1 = kB + 1 >= floor((delta + 1)/2) + 1
  as 2kB >= delta + 1 (3kB >= p + 1); so L_delta = floor((delta + 1)/2) + 1.  L_{delta+1}: the predicate holds at delta + 1, and
  p - delta = kB >= floor((delta + 2)/2) + 1 as 2kB >= delta + 4 (3kB >= p + 4); so L_{delta+1} = floor((delta + 2)/2) + 1.
(S3) omega = floor(delta/2) - 1 <= delta + 1; alpha = 3 - ceil(delta/2) >= 2 - kB as 2kB + 2 >= delta + 1.
  Hence h = floor(delta/2) - 1 <= (delta - 2)/2 and r = ceil(delta/2) - 3, 2r <= delta - 5.  Base: -r = alpha >= 2 - kB = L_1,
  h <= floor(delta/2) = U_1.
(C2) It suffices that U_j + h + 1 <= p + L_{j+1} for each of the three terms of L_{j+1} = min(p - j, 2j + 2 - kB,
  floor((j + 2)/2) + 1) and each of the two terms of U_j = max(j - 1, ceil((delta + j)/2) - 1), for 1 <= j <= N - 1.  With
  h <= (delta - 2)/2, ceil((delta + j)/2) <= (delta + j + 1)/2 and 2j <= 2N - 2 <= p + kB - 1:
  * j + h <= 2p - j (2j + h <= p + kB - 1 + (p - kB)/2 <= 2p);  j + h <= delta + 2j + 2;  j + h <= p + j/2 + 1
    (j/2 + h <= (p + kB)/4 + (p - kB)/2 <= p);
  * delta + (j - 1)/2 <= 2p - j (3j <= 3(p + kB)/2 <= 2p + 2kB... i.e. (3j - 1)/2 <= p + kB);  delta + (j - 1)/2 <= delta + 2j + 2;
    delta + (j - 1)/2 <= p + (j + 1)/2 + 1 (delta < p).
(C1) It suffices that L_j - r >= U_{j+1} + 1 - p, i.e. Lam := min(p - j - 1, p - 2, floor((p + kB - j - 1)/2)) >= r - term for
  each term of L_j, 1 <= j <= N - 1 (Lam = lambda(S'^c) - 1 for |S'| = j + 1).
  * term 2j - kB: r + kB - 2j <= p - j - 1 iff r <= delta + j - 1; <= p - 2 iff r <= delta + 2j - 2;
    <= (p + kB - j - 2)/2 iff 2r + 2 <= delta + 3j (true: 2r <= delta - 5).
  * term floor((j + 1)/2) + 1 >= 2: r - 2 <= (delta - 9)/2; p - j - 1 >= p - N >= (delta - 1)/2; p - 2 >= delta;
    floor((p + kB - j - 1)/2) >= floor((p + kB - N)/2) >= (p + kB - 4)/4 >= (delta - 9)/2 (as 3kB >= p - 14).
  * term p - j + 1: r - p + j - 1 <= p - j - 1 iff r <= 2p - 2j (2p - 2j >= delta + 1 > r); <= p - 2 (r + j <= 2p - 1);
    <= (p + kB - j - 2)/2 iff 2r + 3j <= 3p + kB, true as 3j <= 3(p + kB - 1)/2 and 2r <= p - kB - 5.
(L) j1 <= delta <= N - 1 (S1); U_delta = delta - 1 and U_N = N - 1 (N >= delta); L_{j1} = floor((j1 + 1)/2) + 1 because the
  predicate holds at j1 and p - j1 >= floor((j1 + 1)/2) (j1 <= delta <= (2p - 1)/3 as 3kB >= p + 1).  Finally
  N - floor(j1/2) + 1 >= (p + kB)/2 - (2kB + 7)/6 + 1 = (3p + kB - 1)/6 >= p - kB = delta iff 7kB >= 3p + 1.  []
Coverage: the band is nonempty for every prime p >= 11 ((3p - 7)/5 - (3p + 1)/7 = (6p - 54)/35 > 0): e.g. p = 17: kB = 8;
p = 19: 9, 10; p = 23: 10..12; p = 29: 13..16; p = 31: 14..17; p = 37: 16..20; p = 199: 86..118; asymptotically
0.4286p <= kB <= 0.6p.

## 3. What Theorem IND covers beyond the band, and what it cannot cover

* The hypotheses (S1)-(S3), (C), (L) are finitely checkable; [F] ind_replay.py Part A evaluates them for every prime
  11 <= p <= 400 and every kB with 3kB >= p + 4: the band of Corollary IND-I always satisfies them, and they hold on a
  larger set, printed for p <= 113 and p = 199 in out/ind_replay.txt: p = 17: kB = 7..13; 19: 8..15; 23: 9..18; 29: 12..23;
  31: 12..24; 37: 15..29; 41: 17..32; 43: 18..33; 47: 20..35; 53: 22..41; 59: 24..44; 61: 26..44; 67: 28..50 except 48;
  97: 41..68 except 66; 107: 45..74 except 72; 199: 84..128 (an interval for every printed p other than 67, 97, 107).  For
  such (p, kB) Theorem IND applies with hypotheses verified by exact integer arithmetic (the same status as (H) in
  c3/proof-C-r1.md).
* DOB(p) (c4/proof-NOBCplus-r3.md) after this file, Theorem KB0 (c4/proof-KB0-r1.md) and the verified hypotheses:
  p = 17: DOB = {8, 9, 10} all excluded (8 by Corollary IND-I, 9, 10 by Theorem IND); p = 19: {8, ..., 11} all excluded
  (8 also by KB0); p = 23: {10, ..., 16} all; p = 29: {12, ..., 22} all; p = 31: {12, ..., 24} all; p = 37: {14, ..., 30}
  except 30 (14 by KB0); p = 41: {16, ..., 34} except 16, 33, 34; p = 43: {16, ..., 36} except 17, 34, 35, 36 (16 by KB0).
* Low end: for (p + 4)/3 < kB < ~3p/7 (nonempty for p >= 37) the parity-class system is FEASIBLE ([F] c4/indep.cpp,
  out/indep_all.txt: e.g. (p, kB) = (37, 14) has the solution 0^4 1^22, (61, 22..25) similar), so no argument using only
  subsets of T can exclude these words; they need the anti run / the second parity class.
* High end: for kB > (3p - 7)/5 the seed is s = j1 > delta and r ~ kB/3; (C1) then fails at j = 3 once kB exceeds about
  (3p + 45)/5, and for kB > ~3(p + 1)/4 (S3) fails (omega > delta + 1: deep residues pass the seed).  The parity-class
  system itself is still infeasible there for every p <= 61 ([F] out/indep_all.txt); a proof needs better lower bounds for
  the lifts.

## 4. Exact computations [F] (aids; never hypotheses)

* ind_replay.py (out/ind_replay.txt): Part A as above, and the check that the band of Corollary IND-I satisfies the
  hypotheses for every prime 11 <= p <= 400.  Part B: literal replay of Steps 1-4 on random and structured u in Z_p^T for
  every (p, kB) satisfying the hypotheses with p <= 43 (300 vectors each; modes: uniform, 0/1 profiles, near-constant,
  {-1, 0, 1, 2}-valued, seed-range values): every vector yields a subset S of T whose half-sum lies in its Lemma H window,
  recomputed from the explicit pattern by an independent lambda routine.  Part C (mutation controls): T shrunk by two runs,
  windows shrunk by one, Step 1 skipped -- each produces "no kill" outcomes (counts in out/ind_replay.txt).
* Independent cross-check: indep.cpp (multiset DFS over the parity-class system, no lifting; out/indep_all.txt): the
  system is infeasible for every (p, kB) covered above with p <= 61.
