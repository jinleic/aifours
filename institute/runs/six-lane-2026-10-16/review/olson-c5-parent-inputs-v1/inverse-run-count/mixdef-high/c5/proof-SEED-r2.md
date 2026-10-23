# Theorem SEED (version r2): no word of W(p, kB) is an avoider for (p + 5)/3 <= kB <= p - 4 (every prime p >= 11); with Theorem W-ALL, W(p, kB) is closed for every 1 <= kB <= p - 4

Version r2, written 2026-10-17T14:53:20-0700: replaces the UNFROZEN drafts c5/proof-SEED.md and c5/proof-SEED-r1.md (never cited;
kept, no deletion).  r1 differs from r2 only in Sec. 5, where it described the replayed kB at p >= 37 loosely ('one in
between'); r2 lists them exactly.  r1 itself replaced c5/proof-SEED.md, whose
'Consequences' paragraph said that the scope of Theorem IND lies inside the range of Theorem SEED (false at 3kB = p + 4,
e.g. Corollary IND-I's band at p = 11 is kB = 5, inside Theorem W-ALL's range), whose Remark (2) quoted Lemma NOLIFT(b) for
every kB parity as 3kB >= p + 7, and whose replay summary said 'ten kB each'.  Secs. 0-4 (statements and proofs) are
otherwise unchanged.

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).
Written in c5/ after host clock 2026-10-17T14:50:55-0700 (freeze time and SHA-256 in c5/out/freeze.txt).  Task OlsonRunCount5 (cycle 5 of
OlsonRunCount, targets T2 and T3 of c5/README.md).  Paths "c3/...", "c4/...", "c5/..." are relative to mixdef-high/.
Imported (not re-proved): Lemma H with the 07:39 correction and the Claim in the proof of Lemma BC
(../../../inverse-parity/proof-PAR-K0.md Secs. 1-2); the family W(p, kB), formulas (0.1), (0.2) and the c-coordinate
criterion (2.1) of c3/proof-WALL.md (Codex ACCEPT); Theorem W-ALL of c3/proof-WALL.md for the complementary range (only in
the Corollary).  Steps 1-3 of the proof of Theorem W-ALL are reproduced in Sec. 4 with one changed justification.
NOT used: Lemma L / singleton-extension certification with the plain singleton ranges (replaced by Lemma SL, proved here
from the Claim), the hypothesis (H), Lemma BC, Theorems KB0, IND, IND* (c4; they become special cases).
Scope: the single-letter family W(p, kB) (one anti run, B = 1; = the all-singleton item-(iii) words with B = 1) for every
prime p >= 11 and every integer kB with 3kB >= p + 5 and kB <= p - 4.  With Theorem W-ALL (3kB <= p + 4): every word of
W(p, kB), for every prime p >= 5 and every 1 <= kB <= p - 4, has an identity 2p-subword.  NOT a proof of NMH(p),
MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson for D_(2p); item (iii) also contains words with B >= 2 anti
runs and words with excess, which this file does not treat.

## 0. Setting

p >= 11 prime, kB an integer with 3kB >= p + 5 and kB <= p - 4; delta := p - kB, so 4 <= delta <= 2kB - 5 and
delta <= (2p - 5)/3.  W(p, kB) (c3/proof-WALL.md Sec. 0): k = p + 1 + kB single-letter rotation runs on a cycle, the anti
run 0 (d_0 = -1) and the aligned runs 1, ..., n (d_t = +1), n = p + kB, k = n + 1; B = 1, kappa = kB + 1; all reflection
runs odd (beta = 0).  For a proper pattern Q (Q != empty, [k]) with y := D_Q and m := m(Q) blocks, by (0.1), (0.2) of
c3/proof-WALL.md:
   lambda(Q)   = lam(y, m)  := min(p - m + 1, y + m - kB, floor((y + 1)/2) + 1),
   lambda(Q^c) = lamc(y, m) := min(p - m + 1, p - 1 - y + m, floor((p + kB - y)/2) + 1),       U(Q) := p - lambda(Q^c).
Domain facts for a proper Q: -1 <= y <= n = p + kB; 1 <= m <= min(|Q|, k - |Q|) (the blocks of Q and of Q^c alternate
around the cycle), so 2m <= k = p + kB + 1.
(0.1) If w avoids (u_t in Z_p the half-sums of Lemma H, sum_t u_t = 0, u_Q := sum_{t in Q} u_t), then for every proper Q:
   lambda(Q) + lambda(Q^c) <= p, and u_Q is congruent mod p to an integer of the ARC [lambda(Q), U(Q)].
   [Lemma H: u_Q notin [1 - lambda(Q^c), lambda(Q) - 1] (mod p); if lambda(Q) + lambda(Q^c) >= p + 1 this interval has
   >= p integers and contains u_Q; otherwise its complement mod p is the arc.]
(0.2) Claim (Lemma BC, proof): if y is an integer, y = u_Q (mod p) and 1 - lambda(Q^c) <= y <= p + lambda(Q) - 1, then
   lambda(Q) <= y <= U(Q).
Canonical lifts.  Singleton values (c3/proof-WALL.md Sec. 0): for aligned t, lambda({t}) = 2 - kB and U({t}) =
p - Lambda1 = floor(delta/2); for the anti run, lambda({0}) = -kB and U({0}) = p - Lambda0 = floor(delta/2) - 1.  For
every run t let x_t be the unique integer in [lambda({t}), U({t})] congruent to u_t (it exists by (0.1); it is unique as
the interval has kB + floor(delta/2) - 1, resp. kB + floor(delta/2), integers, fewer than p because floor(delta/2) <=
(p - kB)/2 and kB <= p - 4).  X_Q := sum_{t in Q} x_t, so X_Q = u_Q (mod p).

## 1. Lemma PS (pair seeds)

**Lemma PS.**  Let w in W(p, kB) avoid (p, kB as in Sec. 0).  Then for every aligned run t
   a := 3 - ceil(delta/2) <= x_t <= b := floor(delta/2) - 1.
Proof.  (a) The configuration.  Put m := floor(kB/2) + 1, so kB + 1 <= 2m <= kB + 2 <= p - 2, hence 2m <= p - 3 (2m is
even, p - 2 odd).  If t <= n - 2 put P_1 := {t + 1, t + 2} and R := [1, t - 2] u [t + 4, n]; if t in {n - 1, n} put
P_1 := {t - 2, t - 1} and R := [1, t - 4] u [t + 2, n] (intervals of aligned runs; an interval with r < l is empty).
An interval [l, r] of aligned runs of length L := r - l + 1 >= 0 contains the floor((L + 1)/3) >= (L - 1)/3 pairwise
non-adjacent pairs {l, l + 1}, {l + 3, l + 4}, ... .  The pieces of R have total length >= n - 5 (t <= n - 2: lengths
max(t - 2, 0) and max(n - t - 3, 0), sum >= n - 5; t >= n - 1: [1, t - 4] has length t - 4 >= n - 5), so R contains at
least (n - 7)/3 such pairs, and (n - 7)/3 >= floor(kB/2) = m - 1 because 2(p + kB - 7) >= 3kB <=> kB <= 2p - 14 (true:
kB <= p - 4, p >= 11).  Let P_2, ..., P_m be m - 1 of them and Q := P_1 u ... u P_m.  Then: 0 notin Q and t notin Q; the
blocks of Q are exactly P_1, ..., P_m (two pairs in one piece are separated by a gap; pairs in different pieces are
separated by the excluded runs t - 1, ..., t + 3, resp. t - 3, ..., t + 1, or by run 0; the neighbours of P_1 are t and
t + 3, resp. t - 3 and t, and t + 3 = n + 1 means run 0); in Q + t := Q u {t} the run t is adjacent to P_1 and its other
neighbour (t - 1, resp. t + 1; possibly run 0) is not in Q, so Q + t has the m blocks P_1 u {t}, P_2, ..., P_m.  Both
patterns are proper, y(Q) = 2m, y(Q + t) = 2m + 1, m(Q) = m(Q + t) = m.
(b) The arcs.  lambda(Q) = lam(2m, m) = min(p - m + 1, 3m - kB, m + 1) = m + 1, since 3m - kB = m + (2m - kB) >= m + 1
and p - m + 1 >= m + 1.  lambda(Q^c) = lamc(2m, m) = min(p - m + 1, p - 1 - m, floor((p + kB - 2m)/2) + 1): as
p + kB - 2m <= p - 1 the last term is <= (p + 1)/2 <= p - 1 - m (2m <= p - 3), so lambda(Q^c) = floor((2p - delta - 2m)/2) + 1
= p - m - ceil(delta/2) + 1 and U(Q) = m - 1 + ceil(delta/2).  lambda(Q + t) = lam(2m + 1, m) = min(p - m + 1, 3m + 1 - kB,
m + 2) = m + 2 (3m + 1 - kB >= m + 2; p - m + 1 >= m + 2 as 2m <= p - 3).  lambda((Q + t)^c) = lamc(2m + 1, m) =
min(p - m + 1, p - 2 - m, floor((p + kB - 2m - 1)/2) + 1): the last term is <= floor((p - 2)/2) + 1 = (p - 1)/2 <= p - 2 - m,
so it equals floor((2p - 2m - (delta + 1))/2) + 1 = p - m - ceil((delta + 1)/2) + 1 = p - m - floor(delta/2), and
U(Q + t) = m + floor(delta/2).
(c) By (0.1) for Q and Q + t, u_t = u_(Q+t) - u_Q is congruent to an integer z in
   [lambda(Q + t) - U(Q), U(Q + t) - lambda(Q)] = [3 - ceil(delta/2), floor(delta/2) - 1] = [a, b].
As ceil(delta/2) <= kB + 1 (delta <= 2kB - 5), [a, b] lies inside [2 - kB, floor(delta/2)] = [lambda({t}), U({t})], so z is the
canonical lift: x_t = z.  []
Remarks.  (1) [a, b] is the seed of Step 1 of Theorem IND (c4/proof-IND-r1.md) in its regime I (j1 <= delta), but here it
comes from the 2m-run pair patterns and exists for every kB <= p - 4; in particular in the regime j1 > delta, where the
independent-set seed s = j1 of Theorem IND is too wide (c5/proof-IND-r2.md Sec. 3).  At kB = p - 4 it forces x_t = 1.
(2) [F] c5/seeds.py Part C: at p = 37, 41, 43, 47, 53, 59, 61 no pattern type (D, m) -> (D + 1, m') (m' in {m - 1, m, m + 1})
gives a shorter usable seed for any beyond-W-ALL kB.

## 2. Lemma SL (seeded singleton extension)

**Lemma SL.**  Let w avoid, x the canonical lifts, and for every run t let [a_t, b_t] be an integer interval containing x_t
(its SEED RANGE).  Call a proper pattern Q certified if |Q| = 1, or if Q = Q' u {t} (t notin Q') with Q' certified and
   (A^s)  lo(Q') + a_t >= 1 - lambda(Q^c),        (B^s)  hi(Q') + b_t <= p + lambda(Q) - 1,
where [lo(Q'), hi(Q')] := [a_s, b_s] if Q' = {s}, and := [lambda(Q'), U(Q')] if |Q'| >= 2.  Then lambda(Q) <= X_Q <= U(Q) for
every certified Q with |Q| >= 2.
Proof.  Induction on |Q|.  For Q = Q' u {t}: X_(Q') lies in [lo(Q'), hi(Q')] (by the seed range if |Q'| = 1, by induction
otherwise) and x_t in [a_t, b_t], so X_Q = X_(Q') + x_t lies in [lo(Q') + a_t, hi(Q') + b_t], a subset of
[1 - lambda(Q^c), p + lambda(Q) - 1] by (A^s), (B^s); X_Q = u_Q (mod p), and the Claim (0.2) gives lambda(Q) <= X_Q <= U(Q).  []
(With [a_t, b_t] := [lambda({t}), U({t})] this is Lemma L of c3/proof-NOLP-r2.md.)

## 3. Lemma SCW (every proper pattern is certified; the pin)

Seed ranges: [a_t, b_t] := [a, b] = [3 - ceil(delta/2), floor(delta/2) - 1] for every aligned t (Lemma PS), and
[a_0, b_0] := [-kB, floor(delta/2) - 1] (the canonical range) for the anti run.
**Lemma SCW.**  Let w in W(p, kB) avoid (p, kB as in Sec. 0).  Every proper pattern is certified (Lemma SL with these seed
ranges), hence lambda(Q) <= X_Q <= U(Q) for every proper Q with |Q| >= 2 (and x_t >= lambda({t}) for singletons), and
X_[k] = p.
Proof.  Induction on s := |Q| >= 2, with the step of Lemma CW (c3/proof-WALL.md): if some block of Q has >= 2 runs, let t
be an aligned END run of such a block (its two ends are distinct and at most one is the anti run), so Q' := Q - {t} has
m' = m blocks; otherwise every block is a single run, let t be an aligned one (s >= 2 and there is one anti run), m' = m - 1.
In both cases t is aligned, y(Q') = y - 1, m' in {m, m - 1}, m' >= 1, and 0 <= y <= p + kB (Q contains the aligned run t).
Q' is certified by induction (or is a singleton); we verify (A^s), (B^s) with a_t = a, b_t = b.
Case s = 2.  (i) Q = {s', t}, both aligned, m in {1, 2}: lo(Q') + a = 2a = 6 - 2 ceil(delta/2), hi(Q') + b = 2b =
2 floor(delta/2) - 2; lambda(Q) = lam(2, m) = min(p - m + 1, 2 + m - kB, 2) = 2 + m - kB; lambda(Q^c) = lamc(2, m) =
min(p - m + 1, p - 3 + m, floor((p + kB - 2)/2) + 1) = floor((p + kB)/2) = p - ceil(delta/2) (the last term is
<= (p + kB)/2 <= p - 2 as kB <= p - 4).  (A^s) reads 6 - 2 ceil(delta/2) >= 1 - p + ceil(delta/2), i.e. 3 ceil(delta/2) <= p + 5,
true as ceil(delta/2) <= (delta + 1)/2 <= (p - 1)/3.  (B^s): 2 floor(delta/2) - 2 <= delta - 2 < p + (2 + m - kB) - 1 = delta + 1 + m.
(ii) Q = {0, t}, m in {1, 2}: lo(Q') + a = -kB + 3 - ceil(delta/2), hi(Q') + b = 2 floor(delta/2) - 2; lambda(Q) = lam(0, m) =
min(p - m + 1, m - kB, 1) = m - kB; lambda(Q^c) = lamc(0, m) = min(p - m + 1, p - 1 + m, floor((p + kB)/2) + 1) =
floor((p + kB)/2) + 1 = p - ceil(delta/2) + 1 (<= p - 1 as delta >= 4).  (A^s) reads -kB + 3 - ceil(delta/2) >= ceil(delta/2) - p,
i.e. delta + 3 >= 2 ceil(delta/2): true.  (B^s): 2 floor(delta/2) - 2 <= delta - 2 < p + (m - kB) - 1 = delta + m - 1.
Case s >= 3 (|Q'| >= 2).  As U(Q') = p - lambda(Q'^c), (A^s) <=> lambda(Q') + lambda(Q^c) >= 1 - a = ceil(delta/2) - 2 and
(B^s) <=> lambda(Q) + lambda(Q'^c) >= b + 1 = floor(delta/2).  A sum of two minima is the minimum of the sums of one term
of each, so it suffices to bound all nine sums in each case.  Terms (y = D_Q, D_(Q') = y - 1):
   lambda(Q')    = min(U1 = p - m' + 1, U2 = y - 1 + m' - kB, U3 = floor(y/2) + 1),
   lambda(Q^c)   = min(T1 = p - m + 1,  T2 = p - 1 - y + m,  T3 = floor((p + kB - y)/2) + 1),
   lambda(Q)     = min(V1 = p - m + 1,  V2 = y + m - kB,      V3 = floor((y + 1)/2) + 1),
   lambda(Q'^c)  = min(S1 = p - m' + 1, S2 = p - y + m',      S3 = floor((p + kB - y + 1)/2) + 1).
Facts used: m' <= m, 2m <= p + kB + 1 (so p - m + 1 >= (delta + 1)/2), 0 <= y <= p + kB (so T3, S3, U3, V3 >= 1), m, m' >= 1,
floor(z/2) >= (z - 1)/2.
(A^s), target ceil(delta/2) - 2:
 U1 + T1 = 2p + 2 - m - m' >= 2p + 2 - 2m >= delta + 1;      U1 + T2 = 2p - y + (m - m') >= 2p - y >= delta;
 U1 + T3 >= (p - m + 1) + 1 >= (delta + 3)/2;                 U2 + T1 = y + delta + (m' - m) >= delta - 1;
 U2 + T2 = delta - 2 + m + m' >= delta;                       U2 + T3 >= y + m' - kB + (p + kB - y - 1)/2 = (y + delta - 1)/2 + m' >= (delta + 1)/2;
 U3 + T1 >= 1 + (p - m + 1) >= (delta + 3)/2;                 U3 + T2 = p - ceil(y/2) + m >= p - ceil((p + kB)/2) + 1 = floor(delta/2) + 1;
 U3 + T3 >= (y - 1)/2 + (p + kB - y - 1)/2 + 2 = (p + kB)/2 + 1.
 Each bound is >= ceil(delta/2) >= ceil(delta/2) - 2 (delta >= 4).
(B^s), target floor(delta/2):
 V1 + S1 >= delta + 1;  V1 + S2 = 2p + 1 - y - (m - m') >= 2p - y >= delta;  V1 + S3 >= (p - m + 1) + 1 >= (delta + 3)/2;
 V2 + S1 = y + delta + 1 + (m - m') >= delta + 1;  V2 + S2 = delta + m + m' >= delta + 2;
 V2 + S3 >= y + m - kB + (p + kB - y)/2 + 1 = (y + delta)/2 + m + 1 >= delta/2 + 2;
 V3 + S1 >= 1 + (p - m + 1) >= (delta + 3)/2;  V3 + S2 = p + 1 - floor(y/2) + m' >= p + 2 - floor((p + kB)/2) = ceil(delta/2) + 2;
 V3 + S3 >= y/2 + (p + kB - y)/2 + 2 = (p + kB)/2 + 2.
 Each bound is >= floor(delta/2).
So every proper pattern is certified, and Lemma SL gives the first claim.
Pin.  {0} is certified (x_0 in [-kB, floor(delta/2) - 1]) and so is {0}^c = {1, ..., n} (one block, y = n):
lambda({0}^c) = lam(n, 1) = min(p, p + 1, floor((p + kB + 1)/2) + 1) = floor((p + kB + 1)/2) + 1 and U({0}^c) = p - lambda({0})
= p + kB.  Hence X_[k] = x_0 + X_({0}^c) lies in [floor((p + kB + 1)/2) + 1 - kB, p + kB + floor(delta/2) - 1], which is inside
[1, 2p - 1] (p + 1 >= kB; kB + floor(delta/2) <= p), and X_[k] = sum_t u_t = 0 (mod p); so X_[k] = p.  []

## 4. Theorem SEED

**Theorem SEED.**  Let p >= 11 be prime and kB an integer with (p + 5)/3 <= kB <= p - 4.  No word of W(p, kB) is an avoider:
every inherited all-odd RGR word of length 4p - 2 with p + 1 + kB single-letter rotation runs, exactly one of them rho_(-1),
has an identity 2p-subword.

Proof.  Suppose w avoids; take the canonical lifts x.  By Lemma SCW, X_Q >= lambda(Q) for every proper Q and X_[k] = p.
Put c_t := d_t - x_t and c(Q) := sum_(t in Q) c_t = D_Q - X_Q; then sum_t c_t = D - p = (p + kB - 1) - p = kB - 1, and by
c3/proof-WALL.md (2.1) (pure algebra from (0.1)), for every proper Q:
   X_Q >= lambda(Q)  <=>  c(Q) <= gamma(Q) := max(D_Q + m(Q) - p - 1, kB - m(Q), ceil((D_Q - 1)/2) - 1).
Let Z_al := {aligned t : c_t >= 1} = {aligned t : x_t <= 0}, e_Z := [c_0 >= 0], Z := Z_al u ({0} if e_Z = 1).
Step 1.  If |Z_al| >= kB, let Q consist of kB runs of Z_al: c(Q) >= kB, D_Q = kB, 1 <= m(Q) <= kB, so gamma(Q) <=
max(2kB - p - 1, kB - 1, ceil((kB - 1)/2) - 1) = kB - 1 < c(Q) (2kB - p - 1 <= kB - 5): contradiction.
Step 2.  So |Z_al| <= kB - 1 and |Z| <= kB.  Aligned runs outside Z have c_t <= 0 and the anti run, if outside Z, has
c_0 <= -1; hence c(Z) = (kB - 1) - c([k] - Z) >= kB - e_Z.  Z is nonempty (c(empty) = 0 < kB - e_Z unless kB = 1) and proper
(|Z| <= kB < k).  D_Z = |Z_al| - e_Z, and c(Z) >= max(|Z_al|, kB - e_Z) >= 0 (aligned members have c_t >= 1, the anti member
c_0 >= 0).  In gamma(Z): the third term is ceil((D_Z - 1)/2) - 1 <= ceil((|Z_al| - 1)/2) - 1 < max(|Z_al|, 0) <= c(Z); the
first term is D_Z + m(Z) - p - 1 <= (kB - 1) + kB - p - 1 = 2kB - p - 2 <= kB - 6 < kB - 1 <= c(Z).  [This is the only change
to Step 2 of the proof of Theorem W-ALL, which bounded the first term by < 0 <= c(Z) using 2kB <= p - 1; for 2kB > p that
bound is false, the one given here holds for every kB <= p - 4.]  Hence c(Z) <= gamma(Z) forces c(Z) <= kB - m(Z), and with
c(Z) >= kB - e_Z we get m(Z) <= e_Z <= 1: e_Z = 1 (0 in Z), m(Z) = 1 (Z is one cyclic interval through 0) and c(Z) = kB - 1.
Then c([k] - Z) = 0, and as every run outside Z is aligned with c_t <= 0, every aligned run outside Z has c_t = 0.
Step 3.  Z is an interval of at most kB runs, so at least k - kB - 2 = p - 1 >= 1 runs are neither in Z nor adjacent to Z;
let s be one (aligned, c_s = 0).  Q := Z u {s} has m(Q) = 2, c(Q) = kB - 1, D_Q = |Z_al| <= kB - 1, so
gamma(Q) <= max(kB - p, kB - 2, ceil((kB - 2)/2) - 1) = kB - 2 < c(Q): contradiction.  []

**Corollary W-COMPLETE.**  For every prime p >= 5 and every integer 1 <= kB <= p - 4, no word of W(p, kB) is an avoider.
Proof.  3kB <= p + 4: Theorem W-ALL (c3/proof-WALL.md, Codex ACCEPT).  3kB >= p + 5: Theorem SEED (this range is empty
for p = 5, 7, since (p + 5)/3 > p - 4 there).  []
Consequences (all for W(p, kB) only): DOB(p) (c4/proof-NOBCplus-r3.md; contained in 3kB >= p + 5, kB <= p - 4) is excluded
for every prime p, at both ends.  The scope of Theorem KB0 (c4/proof-KB0-r1.md = c5/proof-KB0-r2.md; 3kB = p + 5) lies inside
the range of Theorem SEED; the scope of Theorem IND / Corollary IND-I (c4/proof-IND-r1.md = c5/proof-IND-r2.md; 3kB >= p + 4)
lies inside the range of Corollary W-COMPLETE (its values with 3kB = p + 4, e.g. Corollary IND-I's band kB = 5 at p = 11, are
in Theorem W-ALL's range).  The open item (i) of c4/README.md Sec. 9 is closed.

Remarks.  (1) Hypotheses used: 3kB >= p + 5 only through delta <= 2kB - 5 (seed inside the canonical range, Lemma PS (c))
and delta <= (2p - 5)/3 (the aligned pair step, 3 ceil(delta/2) <= p + 5); kB <= p - 4 through delta >= 4 (anti pair step,
targets of Case s >= 3, closed forms of Lemma PS) and 2m <= p - 3; p >= 11 through the existence of the pair configuration
((n - 7)/3 >= floor(kB/2)).  (2) The new ingredient is the pair seed: with the plain singleton ranges, condition (A^s) is
Lemma L's condition (A) and fails for the anti pairs when 3kB >= p + 5 and for every pair when 3kB >= p + 7 (kB odd) or
3kB >= p + 6 (kB even) (Lemma NOLIFT, c4/proof-NOBCplus-r3.md Sec. 2); with the pair seeds every proper pattern is
certified, i.e. the conclusion of (H) holds although
(H) itself fails.  (3) Every proper pattern being certified, (0.2) of c3/proof-C-r1.md holds, so Corollary S of Theorem C
(whose proof uses (H) only through (0.2)) would also finish the proof; Sec. 4 uses only patterns with at most kB + 1 runs.
(4) Integrality is used (c_t >= 1 on Z_al); the pair seeds and Lemma SL are integer statements.

## 5. Exact computations [F] (aids; never hypotheses)

* seeds.py (out/seeds.txt): Part A, every prime 11 <= p <= 400 and every kB with 3kB >= p + 5, kB <= p - 4 (8,876 cases): the
  closed forms of Lemma PS (b), the seed [a, b], its containment in the canonical range, the realizability count, the
  pair steps, the closed forms of the pin: 0 failures.  Part B, every prime 5 <= p <= 113, the same kB: every type step
  (j, e, m) of every size in the Lemma CW order (9,228,694 steps): (A^s), (B^s) evaluated exactly, 0 failures (minimum
  slack 2 in Case s >= 3), and each of the 18 term-sum bounds of Sec. 3 holds.  Part C: the pair seed is optimal over all
  pattern types at p = 37, 41, 43, 47, 53, 59, 61 (every beyond-W-ALL kB).  Part D (mutation controls, primes 11..61): with
  the plain singleton ranges 381,343 of 758,098 type steps fail (A) (Lemma NOLIFT); lowering the seed's lower end by
  w = 3 or 4 makes a pair step fail in each of the 252 cases; shifting every lambda by +1 empties the pair seed or creates a
  full window in 54 of 252 cases.
* wordcheck.cpp (out/wordcheck.txt; independent C++ on explicit run lists, lambda recomputed from the general Lemma H
  formula with B, kappa, beta for every explicit pattern): p = 11, 13, 17, 37, 41, 43, 47, 53, 59, 61, every beyond-W-ALL kB
  (204 cases): the explicit pair configuration of Lemma PS exists for every aligned run t and gives exactly the seed [a, b]
  (16,242 runs, 0 failures); Lemma SCW checked EXHAUSTIVELY (the Lemma-CW step of every proper pattern with >= 2 runs) for
  W(11, 6..7), W(13, 6..9), W(17, 8..9) (217,841,472 steps, 0 failures), and along the full Lemma-CW chains of 93,952 random
  explicit patterns and intervals in the other 196 cases (3,427,533 steps, 0 failures; minimum slack 2); the pin holds in
  all 204 cases.
* replay.py (out/replay_mut0.txt ... replay_mut3.txt): literal replay of Secs. 1-4 on residue vectors, p = 11, 13, 17, 19, 23
  (every beyond-W-ALL kB) and p = 37: kB = 14, 15, 16, 23, 25, 30..33; 41: 16, 17, 18, 25, 27, 34..37; 43: 16, 17, 18, 26, 28,
  36..39; 47: 18, 19, 20, 29, 31, 40..43; 53: 20, 21, 22, 32, 34, 46..49; 59: 22..25, 36, 38, 52..55; 61: 22, 23, 24, 26, 37,
  39, 54..57 (95 (p, kB) in all, both ends of DOB(p) included), 60 vectors per (p, kB, part): 11,400
  vectors, every one ends with an explicit pattern whose u lies in its Lemma H window, re-checked by an independent slow
  lambda routine (stages: singleton 3,269, seed 3,297, pin chain 2,727, Step 1 107, Step 2 1,109, Step 3 891), every
  intermediate claim asserted, 0 failures.  Mutation controls: MUT = 1 (kill test against lambda - 1): 2,752 no-kill;
  MUT = 2 (certification with the plain singleton ranges): 4,133 failed certification steps; MUT = 3 (Step 3 with s
  adjacent to Z): 868 failures of the claim c(Q) > gamma(Q).
* Consistency with independent exhaustive searches (c2/famdfs, earlier cycles): no avoider in W(11, 5..7), W(13, 6..9)
  (c3/out/famdfs_W_high.txt) and W(17, 8..10) (c3/out/famdfs_W17_high_r2.txt), as Theorem SEED and W-ALL predict.
