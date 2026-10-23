# Lemma NOBC+ and the doubly obstructed part of W(p, kB): beyond Lemma BC and beyond singleton-extension lifting

Status: [W] written proofs, NOT yet independently reviewed; [F] exact computations (aids only).  Written in c3/
after host clock 2026-10-17T12:48:55-0700 (freeze in c3/out/freeze.txt).  Task OlsonRunCount3.  Imported: Lemma H, Lemma BC
(../../../inverse-parity/proof-PAR-K0.md Secs. 1-2), Lemma L (c3/proof-NOLP-r2.md Sec. 1), the family W(p, kB) and
formula (0.1) of c3/proof-WALL.md Sec. 0.  Scope: obstruction results for the single-letter family W(p, kB); they
say which METHODS cannot settle these words, NOT whether the words are avoiders (by [F] below, the tested ones are not).
Lemma NOBC+ extends c2/proof-NOBC.md (Lemma NOBC: 4 <= kB < (p + 6)/4) to a range reaching kB = p - 7.

## 1. Lemma NOBC+

For kB >= 1 put, for integers j >= 1, h(j) := min(2j - kB, floor((j + 1)/2) + 1), and h0(0) := -kB,
h0(j) := min(2j - kB, floor(j/2) + 1) (j >= 1).  Let rho := max_{j >= 1} h(j)/j (a maximum: h(j)/j <= 1/2 + 3/(2j)
for all j, while h(j)/j > 1/2 for j = ceil((2kB + 3)/3) or j = ceil((2kB + 3)/3) + 1, so only finitely many j compete)
and sigma := min_{j >= 0} (rho j - h0(j)) (>= 0, as h0(j) <= h(j) <= rho j for j >= 1 and h0(0) = -kB < 0).
**Lemma NOBC+.**  Let p >= 5 be prime, 1 <= kB <= p - 4, and suppose rho (p + kB) - sigma < p + 1.  Then no word of
W(p, kB) admits a Lemma BC certificate: every ordered partition (P_1, ..., P_s), s >= 2, of the rotation runs into
nonempty proper patterns has sum_t lambda(P_t) <= p.
Proof.  Let P be a part with j aligned runs, e in {0, 1} anti runs and m <= j + e blocks.  By (0.1),
lambda(P) <= min(j - e + m - kB, floor((j - e + 1)/2) + 1).  If e = 0 (so j >= 1, m <= j) this is <= h(j).  If e = 1
and j >= 1 it is <= min(2j - kB, floor(j/2) + 1) = h0(j); if P = {0}, lambda(P) = -kB = h0(0).  Exactly one part contains
the anti run; call j0 its number of aligned runs.  The other parts have j_t >= 1 and sum_t j_t = p + kB - j0, so
   sum_t lambda(P_t) <= rho (p + kB - j0) + h0(j0) <= rho (p + kB) - sigma < p + 1,
and the integer on the left is <= p.  So condition (a) of Lemma BC fails for every ordered partition.  []
**Corollary (explicit range).**  rho <= (kB + 6)/(2kB + 3): indeed h(j) <= min(2j - kB, (j + 3)/2) <= ((kB + 6)/(2kB + 3)) j,
the two lines 2j - kB and (j + 3)/2 meeting at j = (2kB + 3)/3 where both equal ((kB + 6)/(2kB + 3)) j.  As sigma >= 0, the
hypothesis of Lemma NOBC+ holds whenever (p + kB)(kB + 6) < (p + 1)(2kB + 3), i.e. (for kB >= 4)
   p > kB + 7 + 18/(kB - 3);
e.g. for every prime p >= 37 and every 9 <= kB <= p - 9 (then 18/(kB - 3) <= 3 and kB + 10 <= p + 1).
[F] nobcplus.py (out/nobcplus.txt), exact rationals: for every prime 17 <= p <= 199 the exact criterion holds exactly
for 4 <= kB <= p - 7 (p - 8 at p = 19), for p = 11, 13 only for kB = 4 (as Lemma NOBC); every value so obtained for
p <= 31 is also marked "no Lemma BC certificate" by the independent type-count DP c2/nobc_bound.py (119 (p, kB) pairs
compared, 0 disagreements; the DP is slightly stronger, e.g. it also excludes kB = 12 at p = 19).

## 2. Singleton-extension lifting does not start (restated with proof)

**Lemma NOLIFT.**  In W(p, kB) (1 <= kB <= p - 4):
(a) if 3kB >= p + 5, no 2-run pattern containing the anti run is certified (Lemma L);
(b) if 3kB >= p + 7 (kB odd) or 3kB >= p + 6 (kB even), no 2-run pattern is certified, hence no proper pattern with
    >= 2 runs is certified, also under the extended certification of README Sec. 10 (Q = Q' u Y with Q', Y certified).
Proof.  A 2-run pattern {u, v} can only arise as {u} u {v}; condition (A) reads lambda({u}) + lambda({v}) +
lambda({u, v}^c) >= 1.  (a) u = 0, v aligned: lambda({0}) = -kB, lambda({v}) = 2 - kB, and by (0.2) of c3/proof-WALL.md
(j - e = 0) lambda({0, v}^c) = floor((p + kB)/2) + 1 (the other two terms are >= p - 1); (A) <=> floor((p + kB)/2) >= 2kB - 2,
which fails for 3kB >= p + 5 (kB odd: (p + kB)/2 < 2kB - 2; kB even: (p + kB - 1)/2 < 2kB - 2).  (b) u, v aligned:
lambda({u, v}^c) = floor((p + kB - 2)/2) + 1 (j - e = 2; the other terms are >= p - 2, and the floor term is <= p - 2 as
kB <= p - 4); (A) <=> floor((p + kB - 2)/2) >= 2kB - 4, i.e. p + 6 >= 3kB (kB odd), p + 5 >= 3kB (kB even).  Every
certification of a pattern with >= 3 runs passes through a certified pattern with 2 runs (a chain of singleton
extensions, or Q' u Y with |Y| >= 2 certified or |Q'| >= 2 certified).  []
So for W(p, kB) with 3kB >= p + 5 the lifted-constraint method of c3/proof-WALL.md and c3/proof-C-r1.md (Lemma L /
Lemma CORE) cannot even certify the patterns {0, s}; for 3kB > p + 6 it certifies nothing beyond singletons.

## 3. The doubly obstructed sub-family

DOB(p) := { W(p, kB) : 3kB >= p + 5 and rho (p + kB) - sigma < p + 1 }.  By Lemmas NOBC+ and NOLIFT, for words of
DOB(p) neither a Lemma BC certificate (any ordered partition, any s, hence also full windows and flat 3-partitions)
nor a Lemma L/CORE lifting argument starting from singleton extension exists.  [F] (out/nobcplus.txt): DOB(p) is
empty for p <= 13, and DOB(17) = {kB = 8, 9, 10}, DOB(19) = {8..11}, DOB(23) = {10..16}, DOB(29) = {12..22}, ...,
DOB(199) = {68..192}; asymptotically DOB(p) contains every kB with (p + 5)/3 <= kB <= p - 9 (Corollary of Sec. 1 for
p >= 37).  [F] c2/famdfs (exact avoider search over all patterns): NO avoider in W(17, 8), W(17, 9), W(17, 10)
(out/famdfs_W17_high_r2.txt), nor in W(11, 6..7), W(13, 6..9) (out/famdfs_W_high.txt; these are outside DOB but
beyond Theorem W-ALL).  So DOB(p) is a natural, explicit open core of item (iii): true at the tested p, but out of reach
of both certificate types used so far in this lane.
