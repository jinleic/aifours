# Theorem W4 (revision r2): the Lemma-BC-resistant family W(p, 4) has no avoider (every prime p >= 11)

REVISION r2 (c3/proof-W4-r2.md), written after host clock 2026-10-17T11:44 PDT.  It supersedes
c2/proof-W4.md (frozen, unchanged; sha256 1e09d10f...) and answers the parent's Codex review
institute/runs/six-lane-2026-10-16/review/olson-w4-nobc-nolp-codex-review-v1.note.md (verdict W4
ACCEPT-WITH-FIXES, one MINOR finding at proof-W4.md:60).  The only mathematical change is in Step 2 (marked
[r2 fix]).  Sibling references (proof-NOLP.md, proof-NOBC.md, chaincheck.py, famdfs.*, intsmall.py, out/...)
mean the files in ../c2/; the ../../../ prefixes resolve identically from c3/.

Status: [W] = written proof, reviewed ACCEPT-WITH-FIXES (fix applied here); [F] = exact computation (aid
only).  Original version written 2026-10-17 after host clock 11:09 PDT (hashes: c2/out/freeze.txt).  Uses: Lemma H and the Claim in the proof
of Lemma BC (../../../inverse-parity/proof-PAR-K0.md Secs. 1-2), Lemma L of proof-NOLP.md Sec. 1, the family
W(p, kB) of proof-NOBC.md Sec. 1.  Scope: one explicit family inside item (iii); NOT a proof of NMH(p),
MIX_DEF_HIGH(p) or RUNS(p).  Its interest: Lemma BC cannot kill these words (Lemma NOBC) and, for p >= 17,
neither can any real Farkas combination of window constraints (Lemma NOLP); the argument below is an
integer argument on lifted constraints of patterns with at most 3 runs.

Setting.  w in W(p, 4): k = p + 5 single-letter runs, the anti run at position 0, aligned runs 1, ..., p + 4,
B = 1, kappa = 5, kB = 4; for proper Q with j aligned and e anti runs and m blocks,
lambda(Q) = min(p - m + 1, D_Q + m - 4, floor((D_Q + 1)/2) + 1), D_Q = j - e.  Values used (p >= 11):
   single aligned run: -2;  its complement: (p+5)/2;   anti run {0}: -4;  its complement: (p+7)/2;
   two non-adjacent aligned runs: 0;  their complement: (p+3)/2;
   {0, s}, s aligned not adjacent to 0: -2;  complement: (p+5)/2;
   three pairwise non-adjacent aligned runs: 2;  complement: (p+3)/2;
   {0, s, s'} pairwise non-adjacent (s, s' aligned): 0;  complement: (p+5)/2;
   I_i := {1, ..., i}: i - 3 for i <= 9, floor((i+1)/2) + 1 for 9 <= i <= p + 4 (so lambda(I_{p+4}) = (p+7)/2);
   I_i^c (1 <= i <= p + 3): c_i := p - i for i >= p - 6, floor((p + 4 - i)/2) + 1 for i <= p - 6.

## 1. Certification (condition (1.1) of proof-NOLP.md)

Step Q' -> Q = Q' u {t} needs (A) lambda(Q') + lambda(t) + lambda(Q^c) >= 1 and
(B) lambda(Q) + lambda(Q'^c) + lambda(t^c) >= p + 1.
* {s} -> {s, t} (non-adjacent aligned): (A) -4 + (p+3)/2 >= 1; (B) 0 + (p+5) >= p+1.
* {s} -> {0, s}: (A) -6 + (p+5)/2 >= 1 (p >= 9); (B) -2 + (p+5)/2 + (p+7)/2 = p + 4.
* {a, b} -> {a, b, c} (pairwise non-adjacent aligned): (A) 0 - 2 + (p+3)/2 >= 1; (B) 2 + (p+3)/2 + (p+5)/2 = p + 6.
* {s, s'} -> {0, s, s'}: (A) 0 - 4 + (p+5)/2 >= 1; (B) 0 + (p+3)/2 + (p+7)/2 = p + 5.
* I_i -> I_{i+1} (1 <= i <= p + 3; c_{p+4} := lambda({0}) = -4 fits the formula p - i):
  (A) <=> lambda(I_i) + c_{i+1} >= 3.  If i <= 9 and i + 1 < p - 6: i - 3 + floor((p+3-i)/2) + 1 >= 3, true for
  i >= 5 and, for i <= 4, since floor((p+3-i)/2) >= (p+2-i)/2 >= 5 - i as p >= 8 - i.  If i >= 9 and
  i + 1 < p - 6: both terms are >= 1 and their sum is >= 3.  If
  i + 1 >= p - 6: for i >= 9, floor((i+1)/2) + 1 + p - i - 1 >= p - i/2 >= (p - 3)/2 >= 3; for i < 9 (only
  p <= 15), i - 3 + p - i - 1 = p - 4 >= 3.
  (B) <=> lambda(I_{i+1}) + c_i >= (p - 3)/2.  If i + 1 <= 9 and i < p - 6: (i - 2) + floor((p+4-i)/2) + 1 >=
  (p + 1 + i)/2.  If i + 1 >= 9 and i < p - 6: >= (i+1)/2 + 1 + (p+3-i)/2 + 1 = (p + 8)/2.  If i >= p - 6:
  with i + 1 >= 9, floor((i+2)/2) + 1 + p - i >= p + 3/2 - i/2 >= (p - 3)/2 as i <= p + 6; with i + 1 <= 9
  (only p <= 13), (i - 2) + (p - i) = p - 2.
[F] chaincheck.py: all these steps and values for every prime 11 <= p <= 199 (and lpcert.py: at p = 11, 13
every proper pattern is certified).

## 2. Theorem W4 [W]

**Theorem W4.**  For every prime p >= 11, no word of W(p, 4) is an avoider; i.e. every inherited all-odd RGR
word of length 4p - 2 with p + 5 single-letter rotation runs, exactly one of them rho_{-1}, has an identity
2p-subword.

Proof.  Suppose w avoids.  Choose integer lifts x_t of u_t in [lambda({t}), p - lambda({t}^c)] and put
X_Q := sum_{t in Q} x_t.  By Lemma L and Sec. 1, X_Q >= lambda(Q) for every pair, anti pair, triple and anti
triple listed above, and X_{I_{p+4}} lies in [(p+7)/2, p - lambda({0})] = [(p+7)/2, p + 4].  Also
x_0 in [-4, p - (p+7)/2] = [-4, (p-7)/2].  So X_[k] = X_{I_{p+4}} + x_0 lies in [(p-1)/2, (3p+1)/2]; it is
= sum u_t = 0 (mod p), hence X_[k] = p.  Write a := sum of x_t over aligned t = p - x_0 <= p + 4.  Aligned
lifts are >= -2.
Step 1 (no negative aligned lift).  Let x_t <= -1 (t aligned) and N := the aligned runs other than t and its
neighbours, |N| >= p + 1.  For s in N, X_{s,t} >= 0 gives x_s >= 1; for non-adjacent s, s' in N,
X_{t,s,s'} >= 2 gives x_s + x_{s'} >= 3, so the elements of N with lift 1 are pairwise adjacent (at most 2).
Hence a >= 2|N| - 2 - 3*2 >= 2p - 6 > p + 4, a contradiction for p >= 11.
Step 2 (zeros).  If two non-adjacent aligned runs z1, z2 have lift 0, then every aligned c with
c notin {z1, z2} and c adjacent to neither z1 nor z2 has x_c >= 2 by X_{z1,z2,c} >= 2 ({z1, z2, c} is a set of
three pairwise non-adjacent aligned runs).  This excludes at most six aligned positions (z1, z2 and their at
most four neighbours), so at least (p + 4) - 6 = p - 2 such c exist; all other aligned lifts are >= 0 by
Step 1, so a >= 2(p - 2) = 2p - 4 > p + 4.  [r2 fix: c notin {z1, z2} made explicit.]  Hence the aligned
runs with lift 0 are pairwise adjacent: there are z <= 2 of them, all other aligned lifts are >= 1, and
a >= p + 4 - z, i.e. x_0 = p - a <= z - 4 <= -2.  So x_0 in {-4, -3, -2}.
Step 3.  x_0 = -4: for the p + 2 aligned s not adjacent to 0, X_{0,s} >= -2 gives x_s >= 2, so a >= 2p + 4 >
p + 4 = a.  x_0 = -3: X_{0,s} >= -2 gives x_s >= 1 for s not adjacent to 0, so a zero lift can sit only at
run 1 or run p + 4, which are not adjacent, so z <= 1; a = p + 3 >= p + 4 - z forces z = 1 and all other
aligned lifts equal to 1; then X_{0,3,5} = -3 + 1 + 1 < 0 = lambda({0,3,5}).  x_0 = -2: a = p + 2 forces
z = 2 (an adjacent pair {t, t+1}) and all other aligned lifts 1; one of t, t+1, say z0, is not adjacent to
0; for an aligned s with lift 1 adjacent to neither 0 nor z0, X_{0,z0,s} = -2 + 0 + 1 < 0.  Every case is
contradictory.  []

## 3. Exact computations [F]

* famdfs.py / famdfs.cpp (independent of this proof): no avoider in W(p, 4) for p = 11, 13, 17, 19, 23.
* intsmall.py (out/intsmall.txt; z3, integers): {sum x = p, x(Q) >= lambda(Q) for |Q| <= s or |Q| >= k - s}
  is feasible for s = 2 and infeasible for s = 3 at p = 11, 13, 17; deletion-minimal cores at p = 11, 13 use
  only aligned triples (lambda = 2) and anti triples (lambda = 0) besides sum x = p (37 resp. 47
  constraints).  The p = 17 core minimisation and the p = 19, 23 runs hit their 600 s limits: UNKNOWN.
