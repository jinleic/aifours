# Lemma SLZ, Lemma EXT and the reduction of the length-sensitive conjecture LS to its threshold length, v2

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T02:41:18-0700.  Status: CANDIDATE, written proof
[W], UNREVIEWED.  v2 (after /bin/date 2026-10-19T02:41:36-0700) supersedes v1 (a879aad1...4e51, never sent): one garbled
sentence in the proof of SLZ (why N is nonempty) rewritten; nothing else changed.  Scope frozen first: evidence/LS-scope-v1.md 80ae8041118d68f4c1417a67a2891ceaceeba181a375b29dfd73820957cfddfa.
LS itself (the parent's conjecture) is NOT proved here and is not assumed; Sec. 5 states only a conditional consequence.  No
computation is a premise.  No novelty claim; no Lean.  Not unrestricted INV*(p), not ordered Olson for D_2p, not the
all-groups target.

## 0. Notation and statements

p >= 5 prime; odd elements of C_(2p) = Z_(2p); kappa integer, 0 <= kappa <= p - 2.  (ZP_kappa): no zero-sum subsequence of
length in [2kappa + 2, 2p].  (S1_kappa): every zero-sum subsequence has length <= 2kappa.  A zero-sum of length >= 2kappa + 2
is LONG; under (ZP_kappa) a long zero-sum has length >= 2p + 2.  thr := p + 2kappa + 1.
LS(p, kappa) (conjecture): every sequence Y of odd elements with |Y| >= thr and (ZP_kappa) satisfies (S1_kappa).

**Lemma SLZ (shortest long zero-sum).**  Let Y satisfy (ZP_kappa) and let T be a long zero-sum of Y of minimal length N.  For
every term d of T, with 2t_d the longest zero-sum length of T - d: either N <= p + 1 + 2t_d, or N <= p + kappa + t_d.  In
particular N <= p + 2kappa + 1.

**Lemma EXT (extension).**  Let Y1 be a sequence of odd elements satisfying (S1_kappa), Z0 a longest zero-sum of Y1,
|Z0| = 2t0, and suppose |Y1| >= p + 2kappa and L := |Y1| - 2t0 >= p + 1.  If y is an odd element and Y1 y satisfies
(ZP_kappa), then Y1 y satisfies (S1_kappa).

**Corollary PROP.**  If Y satisfies (ZP_kappa) and has a subsequence Y1 satisfying (S1_kappa) with |Y1| >= p + 2kappa + 1, or
with |Y1| = p + 2kappa and no zero-sum of length 2kappa in Y1, then Y satisfies (S1_kappa).

**Corollary RED.**  LS(p, kappa) holds iff no sequence Y of exactly thr odd elements satisfies (ZP_kappa) and fails
(S1_kappa).  In a sequence Y of length thr satisfying (ZP_kappa) but not (S1_kappa), for every term d either Y - d fails
(S1_kappa), or Y - d satisfies (S1_kappa) and has a zero-sum of length exactly 2kappa (whose complement in Y - d has length
exactly p).

## 1. Imports

- Lemma FB (proof-FB-v1.md 339dcadc...cc6b + erratum 1 33de46d2...e202; parent verdict run review/olson-FB-parent-verdict-v1.md
  8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a), used through the following instantiation of its Setting (S'): if a sequence Y1 of odd elements has a
  longest zero-sum Z0 with |Z0| = 2t0, t0 >= 1, and L := |Y1| - 2t0 >= p + 1, then (S') holds with kappa' := t0 and
  k' := 2p - L (1 <= k' <= p - 1 because p + 1 <= L <= 2p - 1, Y1 - Z0 being zero-sum-free; (S1) at kappa' is the
  maximality of Z0; R = L + 2t0 = 2p + 2kappa' - k').  Hence, for every index-<1 generator g of Y1 - Z0 (coefficients a_i,
  W <= 2p - 1, m units, slack = 2p - 1 - W): Z0 = g^(n+) N, N = (-s_1 g) ... (-s_(n-) g), s_i odd, 1 <= s_i <= slack,
  S(N) = n+ and W + n+ <= 2p - 1; and m >= slack + 3 (ROT-ZR Setting fact).
- SC0 (index-one theorem, author statement via the parent import record); Davenport D(C_(2p)) = 2p.

## 2. Proof of Lemma SLZ

Every zero-sum of T - d is a proper zero-sum of T, hence not long (minimality of N), hence of length <= 2kappa: T - d
satisfies (S1_kappa).  Let Z0 be a longest zero-sum of T - d, |Z0| = 2t_d, L := N - 1 - 2t_d.  Suppose L >= p + 1.  If
t_d = 0, T - d is zero-sum-free of length N - 1 >= 2p + 1 > D(C_(2p)) - 1: impossible.  So t_d >= 1 and Sec. 1 applies to
Y1 := T - d: with g, W, n+, N as there, sigma(T - d) = (W + n+ - n+) g = W g, so d = -W g = (2p - W) g.  N is nonempty: if n- = 0
then n+ = 2t_d >= 2 while S(N) = 0, contradicting S(N) = n+.  Take a term -s g of N.  Since m >= slack + 3 > s, U := (T - d) minus s units g minus the
term -s g has sigma(U) = W g, so d U is a zero-sum of T of length N - s - 1, proper (s + 1 >= 2 terms omitted).  It is not
long, so N - s - 1 <= 2kappa.  With s <= slack = 2p - 1 - W <= 2p - 1 - L = 2p - N + 2t_d this gives
N - 2kappa - 1 <= 2p - N + 2t_d, i.e. N <= p + kappa + t_d (2N is even).  So L >= p + 1 implies N <= p + kappa + t_d, and
L <= p means N <= p + 1 + 2t_d.  Both bounds are <= p + 2kappa + 1 as t_d <= kappa.  []

## 3. Proof of Lemma EXT

If t0 = 0, Y1 is zero-sum-free of length >= p + 1; SC0 gives an odd generator g with W <= 2p - 1, every zero-sum of Y1 y
contains y = c g and has coefficient sum exactly 2p (c + W < 4p), so its length is 2p - (c - 1) - (mass of the other
terms) <= 2p: not long.  Let t0 >= 1 and take g, W, n+, N, m as in Sec. 1 for (Y1, Z0); C := Y1 - Z0, e' := W - L (the
total mass sum (a_i - 1) of C), h := number of heavy terms of C (a_i >= 3), so 2h <= e'; f(N0) := S(N0) + |N0| for N0 <= N,
so f(N) = n+ + n- = 2t0.
Step 1 (zero-sums of Y1 y).  Write y = c g with c odd in [1, 2p - 1].  Every term of Y1 y is b g with b one of a_i, 1 (the
units of Z0), -s_i, c.  For a subsequence S let sigma_g(S) be the integer sum of these b; S is a zero-sum iff
sigma_g(S) = 0 (mod 2p).  The positive b's of Y1 sum to W + n+ <= 2p - 1 and the negative ones to -n+ > -2p, so
sigma_g(S) lies in [-n+, 4p - 2] and a zero-sum has sigma_g(S) in {0, 2p}, the value 2p only if y lies in S.  Writing S_N for
the terms of S in N and mass_+(S) for the sum of (b - 1) over the positive terms of S, |S| = sigma_g(S) + f(S_N) - mass_+(S).
So a zero-sum with sigma_g = 0 has length <= f(N) = 2t0 <= 2kappa, and a zero-sum S containing y with sigma_g(S) = 2p has
length 2p + D(S), D(S) := f(S_N) - mass(S_C) - (c - 1), where S_C is the set of terms of S in C (the units of Z0 have mass
0).  (ZP_kappa) for Y1 y says: no such S has D(S) in [2kappa + 2 - 2p, 0].  (D(S) is even.)
Step 2 (small negative terms).  n+ <= 2p - 1 - W <= 2p - 1 - L and L = |Y1| - 2t0 >= p + 2kappa - 2t0 give
n+ <= p - 1 - 2kappa + 2t0, so sum (s_i - 1) = n+ - n- = 2n+ - 2t0 <= 2p - 2 - 4kappa + 2t0 <= 2p - 2 - 2kappa.  Hence every
s_i + 1 <= 2p - 2kappa.
Step 3 (descent).  Suppose Y1 y has a long zero-sum S*.  By Step 1, y lies in S*, sigma_g(S*) = 2p and D(S*) >= 2; write
S* = y H* U* N* with H* its terms among the heavy terms of C, U* its units (from C or Z0) and N* = S*_N.  From D(S*) >= 2,
f(N*) >= c + 1, so c <= f(N) - 1 = 2t0 - 1 <= 2kappa - 1.  For a sub-multiset N1 of N* put
    S(N1) := y H* N1 U(N1),  U(N1) := |U*| - S(N*) + S(N1) units taken from U*,
valid when |U(N1)| >= 0; then sigma_g(S(N1)) = c + A(H*) + |U*| - S(N*) = 2p (as sigma_g(S*) = 2p) and
D(S(N1)) = f(N1) - mass(H*) - (c - 1).  Remove the terms of N* one at a time (any order): D decreases by s + 1 <= 2p - 2kappa
per step (Step 2), from D(S*) >= 2 to D(S(empty)) = -mass(H*) - (c - 1) <= 0.  Let N1 be the first set reached with
D(S(N1)) <= 0; its predecessor has D >= 2, so D(S(N1)) >= 2 - (2p - 2kappa) = 2kappa + 2 - 2p.  If S(N1) is valid it is a
zero-sum of Y1 y of length 2p + D(S(N1)) in [2kappa + 2, 2p], contradicting (ZP_kappa).
Validity: |U(N1)| decreases along the removals, so it suffices that |U(N1)| >= 0 at the stopping set.  There
f(N1) >= 2kappa + 2 - 2p + mass(H*) + c - 1 and f(N1) <= 2 S(N1) (every s >= 1), so
    |U(N1)| = 2p - c - A(H*) + S(N1) >= (2p + 2kappa + 1 - c - A(H*) - |H*|) / 2,
using A(H*) = mass(H*) + |H*|.  Now c <= 2kappa - 1 and A(H*) + |H*| = mass(H*) + 2|H*| <= e' + 2h <= 2e', with
e' = W - L <= 2p - 1 - n+ - L <= p - 2 (W + n+ <= 2p - 1, L >= p + 1).  So c + A(H*) + |H*| <= 2p + 2kappa - 5 and
|U(N1)| >= 3.  (U(N1) is a sub-multiset of U*, as |U(N1)| <= |U*|.)  This contradiction shows that Y1 y has no long
zero-sum.  []

## 4. Proofs of the corollaries

PROP.  Order Y - Y1 as y_1, y_2, ...; Y1 y_1 ... y_j is a subsequence of Y, so it satisfies (ZP_kappa).  For j = 0 the
hypothesis of EXT holds (|Y1| >= p + 2kappa + 1 gives L >= p + 1 as t0 <= kappa; |Y1| = p + 2kappa with t0 <= kappa - 1 gives
L >= p + 2).  Inductively Y1 y_1 ... y_j satisfies (S1_kappa) and has length >= p + 2kappa + 1, so EXT applies again.
RED.  Let Y be a counterexample to LS(p, kappa) of minimal length R0 >= thr.  If R0 > thr, every Y - x (length >= thr,
(ZP_kappa)) satisfies (S1_kappa), so every long zero-sum of Y contains every term: Y itself is the only long zero-sum, and
SLZ applied to T = Y gives R0 <= p + 2kappa + 1 = thr, a contradiction.  So R0 = thr.  At length thr: if some Y - d satisfies
(S1_kappa) without a zero-sum of length 2kappa, PROP (with Y1 = Y - d, |Y1| = p + 2kappa) contradicts the failure of
(S1_kappa) for Y.  The same argument shows: any counterexample of length >= thr + 1 would contain a counterexample of
length exactly thr (shrink to length thr + 1; there no Y - d satisfies (S1), by PROP with |Y - d| = thr).  []

## 5. Conditional word-level consequence (not a claim of LS)

If LS(p, kappa) holds for every 0 <= kappa <= p - 2, then for every prime p >= 7 every admissible normal form with terminal
2 <= k <= p - 1 has (S1) at kappa^ (its rotation sequence has (ZP) at kappa^ by GRX, length 2p + 2kappa^ - k >= p + 2kappa^ + 1,
and kappa^ <= k - 1 <= p - 2 by DAV), so Theorem ROT-FB (a) (accepted) gives rotation rigidity (K1 for k = 1, K01 for
kappa^ = 0); restricted REFL and the ledger then give INV* and ordered Olson for every word with o_F <= p - 1.

## 6. Finite aids (not premises) and sharpness information

- probe v11 (evidence/probe-v11/RECEIPT-v11-v1.md b7e4c9ee...4d97): complete DFS over all (ZP_kappa) multisets, p = 7
  (kappa 4, 5) and p = 11 (kappa 8, 9; canonical): no counterexample to LS.
- probe v12 (pid 52130, rc 0; pre/post/stdout sha256 578dcb814d3247e993def38314d4822352428d54e380e17814e9d87dab6e41bb / 4ff2132239e66681e99db13e37a8bc6a0bce79222e1d18375e670830ec850940 /
  23552621ec8044fd0fbc4ef193470a51f714b04f24af2e43301ce721e107d698): length histograms of (ZP_kappa)-and-not-(S1_kappa) multisets: p = 7, kappa = 5: only length 16
  (12 multisets); p = 11, kappa = 8 (canonical): lengths 24, 25 (5, 2); p = 11, kappa = 9 (canonical): lengths 24..28
  (65, 57, 30, 10, 2); p = 13, kappa = 9: incomplete (no hit within 200 s).  So at p = 11, kappa = 9 the longest failures have
  length p + 2kappa - 1 = thr - 2 (e.g. g^18 (3g)^10 and g^21 (15g)^7), in which NO single term lies in every long zero-sum: a
  'common element' argument cannot be the general base case of RED, and the threshold of LS is at most 2 above sharp there.
- Remaining exact obstruction for LS: sequences of length exactly thr in which every Y - d fails (S1) or contains a
  zero-sum of length 2kappa (complement exactly p: the S(p)-type boundary).

## 7. Limits

Written mathematics relative to the imports; no Lean, no human review, no literature search; a search miss would never be
novelty evidence.  LS remains a parent conjecture supported only by the finite aids above.
