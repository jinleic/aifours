# Theorem SEED-B (version r3): all-single-letter item-(iii) words with B >= 2 anti runs (any positions) in the small-B region

Version r3, written 2026-10-17T17:07:09-0700: = the frozen r2 (c6/proof-SEEDB-r2.md, sha256 616e0c4d3e70f83cb8b1af5d7e4025b4f28b930c0f41caa0bd9005e65b2ac6e4,
kept unchanged) with the fixes of the c6 reviews (institute/runs/six-lane-2026-10-16/review/olson-c6-codex-review-v1.note.md:
ACCEPT-WITH-FIXES, one MINOR; olson-c6-claude-review-v1.note.md: ACCEPT-WITH-FIXES, F1, F2 MINOR, F3-F8 INFO; neither review found a
mathematical error in Lemmas TS, IS, SL, SCW-B, C0, Theorem SEED-B, Claim E or Proposition AB).  Changes: Codex MINOR + Claude F3: the
anti-seed-cap remark of Sec. 6 now uses the integer cap and the exact y-parity gains; F1: exact accounting of what SEED-B leaves
(Scope paragraph); F2: the six-class exception list is derived in writing (new Claim E', Sec. 4), the Corollary cites out/seedB.txt
Part A (r2 wrongly cited Part C) and labels the exclusion of the six classes [W+F] computer-assisted; F4: wording in Lemma IS (b);
F5: the NMH membership facts are stated (Scope) and the Corollary's qualifiers restored; F6: the region is renamed RB (R also denotes
the number of rotation letters); F7: Proposition AB assumes NMH (for D > 0) and f >= 4 (resp. >= 5); F8 concerns
c6/c5-fixes/proof-Cplus-r2.md (new Sec. 7).  No statement, hypothesis or proof step of Lemmas TS, IS, SL, SCW-B, C0, Theorem SEED-B
or Claim E changed.  The r2 version note follows.

Version r2, written 2026-10-17T16:19:28-0700: = the unfrozen draft c6/proof-SEEDB-r1.md plus the exact control of Proposition AB
(last bullet of Sec. 6; out/abcheck.txt).  r1 replaced the UNFROZEN draft c6/proof-SEEDB.md (both kept, never cited).  Changes of r1:
(1.3) corrected (for anti runs 1 - a_t <= (delta - B + 1)/2, not (delta - B - 1)/2; the proof only uses the common bound
(delta - B + 1)/2); the wording of Lemma IS (b), (d) and of the 2-run steps made exact; the pin justification; Corollary SEED-B
(word-by-word coverage only at p = 11); the mutation-control counts of Sec. 5 made exact; NEW Sec. 6: Proposition AB (why (H)
fails: anti-heavy intervals) and the T1 census results.  The statements of Lemmas TS, IS, SL, SCW-B, C0, Theorem SEED-B and
Claim E are unchanged.

Status: [W] written proof (r2: Codex ACCEPT-WITH-FIXES, Claude ACCEPT-WITH-FIXES; the r3 changes are not yet re-reviewed); [F] exact
computation (aid only, never a hypothesis), except the exclusion of the six classes of Claim E', which is computer-assisted [W+F].
Written in c6/ after host clock 2026-10-17T17:07:09-0700 (freeze time and SHA-256 in c6/out/freeze.txt).  Task OlsonRunCount5, cycle 6 (r2: target T2
of c6/README.md).  Paths "c3/...", "c5/...", "c6/..." are relative to mixdef-high/.
Imported (not re-proved): Lemma H with the 07:39 correction and the Claim in the proof of Lemma BC
(../../../inverse-parity/proof-PAR-K0.md Secs. 1-2); c3/proof-C-r1.md (Codex ACCEPT): its setting (0.1), Sec. 1 and the proof of
Theorem C in case (i) (used through Lemma C0 below).  Re-proved here in the needed generality: Lemma SL (seeded singleton
extension; c5/proof-SEED-r2.md Lemma SL, Codex ACCEPT, was stated for W(p, kB) only) and the two-pattern seed (c5 Lemma PS (c)).
Not used: (H), Lemma L with plain singleton ranges, Lemma BC, Theorem IND*, any computation.
Scope: every prime p >= 11 and every all-single-letter word with k = p + kB + B single-letter rotation runs, exactly B of them
rho_(-1) at ANY positions, kB = kappa - B, such that (p, kB, B) lies in the region (called R in r2; renamed, as R also denotes the
number of rotation letters)
   RB:  B >= 2,  kB >= 1,  2B + kB <= p - 2,   and   (E):  5kB + B + 13 <= 3p   or   2kB + 7B + 28 <= 4p.
(E) holds automatically for p >= 19 (Claim E, Sec. 4); for p = 11, 13, 17 exactly six classes of RB fail (E) (Claim E', Sec. 4).
These words are NMH words with R = k <= 2p - 4: all reflection runs odd, k >= p + 3, all runs pure, 1 <= B <= kappa - 1,
B <= A = p + kB <= 2p - 1, and kappa = k - p (../../../inverse-parity/proof-PAR-K0.md line 12 with o_F = k), consistent with
kB = kappa - B; in particular their item-(iii) members.  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or
ordered Olson for D_(2p).
Exact accounting (Claude F1).  Among the all-single-letter item-(iii) classes (kB >= 1, B >= 1, kB + B <= p - 3), SEED-B leaves exactly
 - B = 1 (the words W(p, kB), 1 <= kB <= p - 4): handled by c3/proof-WALL.md (Theorem W-ALL, 3kB <= p + 4) and c5/proof-SEED-r2.md
   (Theorem SEED, 3kB >= p + 5; fixes in c6/c5-fixes/proof-SEED-r3.md), both reviewed, not by this file;
 - B >= 2 with 2B + kB >= p - 1;
 - for p in {11, 13, 17} only, the six classes of RB failing (E) (Claim E'); their exclusion is at present computer-assisted only
   (IND* class hypotheses certified by [F]; at p = 11 also word by word).
All words with excess remain outside.

## 0. Setting

All reflection runs are odd (beta = 0); n := p + kB aligned runs (d = +1), B anti runs (d = -1), k = n + B, kappa = kB + B,
D = n - B; delta := p - kB, so RB gives delta >= 2B + 2, hence delta - B >= B + 2 >= 4.  For a proper pattern Q with y := D_Q
(aligned minus anti runs of Q) and m := m(Q) blocks, Lemma H gives
   lambda(Q)   = lam(y, m)  := min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
   lambda(Q^c) = lamc(y, m) := min(p - m + 1, p - B - y + m, floor((p + kB - y)/2) + 1),
   U(Q) := p - lambda(Q^c) = max(m - 1, y + B - m, ceil((delta + y)/2) - 1).
(lamc: Q^c has D - y, m blocks; p - floor((p + kB - y)/2) - 1 = ceil((delta + y)/2) - 1.)  For proper Q: -B <= y <= n and
1 <= m <= min(|Q|, k - |Q|), so 2m <= k and
   (F1)  p - m + 1 >= p + 1 - k/2 = (delta - B + 2)/2.
(0.1) If w avoids (u_t the half-sums, sum_t u_t = 0, u_Q := sum_(t in Q) u_t), then for every proper Q, lambda(Q) + lambda(Q^c) <= p
and u_Q is congruent to an integer of the arc [lambda(Q), U(Q)] (Lemma H; if lambda(Q) + lambda(Q^c) >= p + 1 the window has >= p
integers and contains u_Q).
(0.2) Claim (Lemma BC): if y is an integer, y = u_Q (mod p) and 1 - lambda(Q^c) <= y <= p + lambda(Q) - 1, then lambda(Q) <= y <= U(Q).
Singletons: aligned t: lambda({t}) = lam(1, 1) = 2 - kB, U({t}) = max(0, B, floor(delta/2)) = floor(delta/2) (delta >= 2B + 2);
anti t: lambda({t}) = -kB, U({t}) = max(0, B - 2, floor(delta/2) - 1) = floor(delta/2) - 1.  Canonical lift x_t: the unique integer
in [lambda({t}), U({t})] congruent to u_t (it exists by (0.1); unique as the interval has floor(delta/2) + kB - 1, resp.
floor(delta/2) + kB < p integers).  X_Q := sum_(t in Q) x_t = u_Q (mod p).

## 1. Seeds

**Lemma TS (two-pattern seed).**  Let w avoid, t a run, Q a proper pattern with t notin Q and Q + t := Q u {t} proper.  Then u_t is
congruent to an integer z in [lambda(Q + t) - U(Q), U(Q + t) - lambda(Q)].
Proof.  By (0.1), u_(Q+t) = z1 and u_Q = z2 (mod p) with z1 in [lambda(Q + t), U(Q + t)], z2 in [lambda(Q), U(Q)]; z := z1 - z2.  []
**Lemma IS (isolated configurations).**  Let (p, kB, B) satisfy RB and (E) and let w be a word of the class.  Put
   (singles)  if 5kB + B + 13 <= 3p:  m := ceil((2kB + B + 2)/3),  y := m;
   (pairs)    otherwise:              m := ceil((kB + floor(B/2) + 1)/2),  y := 2m.
For every run t of w (aligned, d_t = 1, or anti, d_t = -1) there is a pattern Q consisting of m pairwise non-adjacent aligned runs
(singles), resp. of m pairwise non-adjacent blocks of two adjacent aligned runs (pairs), no run of Q equal or adjacent to t.  For it
D_Q = y, m(Q) = m, D_(Q+t) = y + d_t, m(Q + t) = m + 1, and
   lambda(Q) = floor((y + B)/2) + 1,  lambda(Q + t) = floor((y + d_t + B)/2) + 1,  U(Q) = ceil((delta + y)/2) - 1,
   U(Q + t) = ceil((delta + y + d_t)/2) - 1.                                                                      (1.1)
Consequently, if w avoids, x_t lies in [s_lo(d_t), s_hi(d_t)] := [floor((y + d_t + B)/2) - ceil((delta + y)/2) + 2,
ceil((delta + y + d_t)/2) - floor((y + B)/2) - 2], explicitly (only the parity of y matters)
   aligned: y even [floor((B + 1)/2) + 2 - ceil(delta/2), floor(delta/2) - floor(B/2) - 1],  y odd [floor(B/2) + 2 - floor(delta/2),
            ceil(delta/2) - floor((B + 1)/2) - 1];
   anti:    y even [floor((B - 1)/2) + 2 - ceil(delta/2), floor(delta/2) - floor(B/2) - 2],  y odd [floor(B/2) + 1 - floor(delta/2),
            ceil(delta/2) - floor((B + 1)/2) - 2];
and in every case
   aligned t:  (B - delta + 3)/2 <= s_lo,  s_hi <= (delta - B - 1)/2;     anti t:  (B - delta + 1)/2 <= s_lo,  s_hi <= (delta - B - 3)/2.   (1.2)
Proof.  (a) Existence.  Delete t and its two neighbours; the remaining k - 3 runs form a path containing at least n - 3 aligned runs,
in maximal aligned intervals of lengths L_1, ..., L_r (r <= B + 1: the deleted segment splits at most one aligned interval of the
cycle, and the cycle has at most B of them).  An interval of length L contains ceil(L/2) pairwise non-adjacent runs and
floor((L + 1)/3) >= (L - 1)/3 pairwise non-adjacent pairs {l, l + 1}, {l + 3, l + 4}, ...; runs or pairs from different intervals are
not adjacent, and none is adjacent to t.  So at least sum ceil(L_i/2) >= (n - 3)/2 singles and at least sum (L_i - 1)/3 >=
(n - B - 4)/3 pairs are available.  Singles: m <= (2kB + B + 4)/3 <= (n - 3)/2 iff kB + 2B + 17 <= 3p, true as kB + 2B <= p - 2 and
p >= 11.  Pairs (case 2kB + 7B + 28 <= 4p): m <= (kB + floor(B/2) + 2)/2 <= (n - B - 4)/3 iff kB + 3 floor(B/2) + 2B + 14 <= 2p, implied.
The blocks of Q are its m runs (singles) or its m pairs; t is adjacent to no run of Q, so Q + t has m + 1 blocks.
(b) The values (1.1).  Singles (y = m), d := d_t.  lam(m, m) = min(p - m + 1, 2m - kB, floor((m + B)/2) + 1) and
lam(m + d, m + 1) = min(p - m, 2m + 1 + d - kB, floor((m + d + B)/2) + 1).  By the definition of m, 3m >= 2kB + B + 2, which gives
2m - kB >= (m + B + 2)/2 >= floor((m + B)/2) + 1; then for d = 1, 2m + 2 - kB >= floor((m + B)/2) + 3 >= floor((m + 1 + B)/2) + 1, and
for d = -1, 2m - kB >= floor((m - 1 + B)/2) + 1.  And 3m <= 2kB + B + 4 <= 2p - B - 3 (as kB + B <= p - 4) gives
p - m >= (m + B + 3)/2 >= floor((m + 1 + B)/2) + 1 >= floor((m + d + B)/2) + 1, which bounds both first terms.
U(m, m) = max(m - 1, B, ceil((delta + m)/2) - 1): m <= delta - 3 (from 5kB + B + 13 <= 3p: m <= (2kB + B + 4)/3 <= p - kB - 3) gives
m - 1 <= ceil((delta + m)/2) - 1, and delta >= 2B + 2 gives B <= ceil((delta + m)/2) - 1.  U(m + d, m + 1) = max(m, B + d - 1,
ceil((delta + m + d)/2) - 1): m + 1 <= (delta + m - 1)/2 (m <= delta - 3) and B + d <= ceil((delta + m + d)/2) (delta >= 2B + 2).
Pairs (y = 2m): lam(2m, m) = min(p - m + 1, 3m - kB, m + floor(B/2) + 1) with 2m >= kB + floor(B/2) + 1 (definition of m) and
2m <= kB + floor(B/2) + 2 <= p - floor((B + 1)/2) - 1 (as kB + B <= p - 4); lam(2m + d, m + 1) = min(p - m, 3m + 1 + d - kB,
m + floor((B + d)/2) + 1): 2m + d >= kB + floor((B + d)/2) for d = +-1 by the choice of m, and 2m <= p - floor((B + 1)/2) - 1
bounds the first term.  U(2m, m) = max(m - 1, m + B, m + ceil(delta/2) - 1) = m + ceil(delta/2) - 1 as B + 1 <= ceil(delta/2);
U(2m + d, m + 1) = max(m, m + B + d - 1, m + ceil((delta + d)/2) - 1) = m + ceil((delta + d)/2) - 1 as B + d <= ceil((delta + d)/2)
(both from delta >= 2B + 2).
(c) Seeds.  By Lemma TS and (1.1), u_t = z (mod p) with z in [s_lo, s_hi]; the explicit forms follow by inserting y = 2r or 2r + 1
(e.g. aligned, y = 2r: floor((2r + 1 + B)/2) - ceil((delta + 2r)/2) + 2 = floor((B + 1)/2) + 2 - ceil(delta/2)).  (1.2): with
floor(a/2) >= (a - 1)/2 and ceil(a/2) <= (a + 1)/2 each lower end is >= the stated bound and each upper end <= it (e.g. aligned,
y odd: floor(B/2) + 2 - floor(delta/2) >= (B - 1)/2 + 2 - delta/2 = (B - delta + 3)/2).
(d) x_t = z.  By (1.2): aligned t: s_hi - p <= (delta - B - 1)/2 - p < 2 - kB = lambda({t}) (as (delta - B - 1)/2 < delta + 2) and
s_lo + p >= (B - delta + 3)/2 + p > delta/2 >= U({t}) (as delta < p); anti t: s_hi - p <= (delta - B - 3)/2 - p < -kB = lambda({t})
and s_lo + p >= (B - delta + 1)/2 + p > delta/2 - 1 >= U({t}).  So x_t - z, a multiple of p, lies in [lambda({t}) - s_hi,
U({t}) - s_lo], strictly between -p and p; hence x_t = z.  []
Seed ranges.  For every run t put [a_t, b_t] := [max(lambda({t}), s_lo(d_t)), s_hi(d_t)]; by Lemma IS, x_t in [a_t, b_t], and by (1.2)
   aligned: 1 - a_t <= (delta - B - 1)/2, b_t + 1 <= (delta - B + 1)/2;  anti: 1 - a_t <= (delta - B + 1)/2, b_t + 1 <= (delta - B - 1)/2,  (1.3)
   a_t >= 2 - kB (aligned),  a_t >= -kB (anti).                                                                                      (1.4)

## 2. Seeded certification of every proper pattern

**Lemma SL.**  Let w avoid, x the canonical lifts, [a_t, b_t] integer intervals with x_t in [a_t, b_t].  Call a proper Q certified if
|Q| = 1, or Q = Q' u {t} (t notin Q') with Q' certified and
   (A^s) lo(Q') + a_t >= 1 - lambda(Q^c),     (B^s) hi(Q') + b_t <= p + lambda(Q) - 1,
where [lo(Q'), hi(Q')] := [a_s, b_s] if Q' = {s} and := [lambda(Q'), U(Q')] if |Q'| >= 2.  Then lambda(Q) <= X_Q <= U(Q) for every
certified Q with |Q| >= 2.
Proof.  Induction on |Q|: X_Q = X_(Q') + x_t lies in [lo(Q') + a_t, hi(Q') + b_t], inside [1 - lambda(Q^c), p + lambda(Q) - 1] by (A^s),
(B^s); X_Q = u_Q (mod p), so the Claim (0.2) gives lambda(Q) <= X_Q <= U(Q).  []
**Lemma SCW-B.**  In the setting of Lemma IS (w avoids), with the seed ranges [a_t, b_t]: every proper pattern is certified, and
X_[k] = p.
Proof.  Induction on s := |Q| >= 2.  Let t be an end run of some block of Q (a run of Q with at most one neighbour in Q); Q' := Q - {t}
is proper and nonempty with m' := m(Q') = m (t ended a block of >= 2 runs) or m - 1 (t was a block by itself); m' >= 1, m' <= m.
Q' is certified by induction (or |Q'| = 1).  Write y := D_Q, d := d_t, so D_(Q') = y - d.  If t is aligned, 1 - B <= y <= n; if t is
anti, -B <= y <= n - 1.
Case s >= 3 (|Q'| >= 2).  (A^s) <=> lam(y - d, m') + lamc(y, m) >= 1 - a_t and (B^s) <=> lam(y, m) + lamc(y - d, m') >= b_t + 1.  By (1.3)
both right sides are <= (delta - B + 1)/2, so it suffices that every term-sum below is >= (delta - B + 2)/2.  A sum of two minima is
the minimum of the 9 sums of one term from each, and floor(a/2) >= (a - 1)/2; (F1) applies to m and to m' <= m.
 Aligned t (d = 1):
  (A^s) terms U1 = p - m' + 1, U2 = y - 1 + m' - kB, U3 = floor((y - 1 + B)/2) + 1 >= 1; T1 = p - m + 1, T2 = p - B - y + m,
  T3 = floor((p + kB - y)/2) + 1 >= 1:
   U1 + T1 >= delta - B + 2;  U1 + T2 = 2p + 1 - B - y + (m - m') >= delta - B + 1;  U1 + T3 >= (delta - B + 4)/2;
   U2 + T1 = y + delta + (m' - m) >= delta - B;  U2 + T2 = delta - B - 1 + m + m' >= delta - B + 1;
   U2 + T3 >= (y + delta - 1)/2 + m' >= (delta - B + 2)/2;  U3 + T1 >= (delta - B + 4)/2;
   U3 + T2 >= p + m - (y + B)/2 >= (delta - B + 2)/2;  U3 + T3 >= (k + 1)/2.
  (B^s) terms V1 = p - m + 1, V2 = y + m - kB, V3 = floor((y + B)/2) + 1 >= 1; S1 = p - m' + 1, S2 = p - B - y + 1 + m',
  S3 = floor((p + kB - y + 1)/2) + 1 >= 1:
   V1 + S1 >= delta - B + 2;  V1 + S2 >= 2p + 1 - B - y >= delta - B + 1;  V1 + S3 >= (delta - B + 4)/2;  V2 + S1 >= y + delta + 1 >=
   delta - B + 2;  V2 + S2 = delta - B + 1 + m + m' >= delta - B + 3;  V2 + S3 >= (y + delta)/2 + m + 1 >= (delta - B + 5)/2;
   V3 + S1 >= (delta - B + 4)/2;  V3 + S2 >= p - (y + B)/2 + m' + 3/2 >= (delta - B + 5)/2;  V3 + S3 >= (k + 3)/2.
 Anti t (d = -1):
  (A^s) terms U1 = p - m' + 1, U2 = y + 1 + m' - kB, U3 = floor((y + 1 + B)/2) + 1 >= 1; T1, T2, T3 as above (T3 >= 1 as y <= n - 1):
   U1 + T1 >= delta - B + 2;  U1 + T2 >= 2p + 1 - B - y >= delta - B + 2;  U1 + T3 >= (delta - B + 4)/2;
   U2 + T1 = y + delta + 2 + (m' - m) >= delta - B + 1;  U2 + T2 = delta - B + 1 + m + m' >= delta - B + 3;
   U2 + T3 >= (y + delta + 3)/2 + m' >= (delta - B + 5)/2;  U3 + T1 >= (delta - B + 4)/2;  U3 + T2 >= p + 1 + m - (y + B)/2 >=
   (delta - B + 5)/2;  U3 + T3 >= (k + 3)/2.
  (B^s) terms V1, V2, V3 as above (V3 >= 1 as y + B >= 0); S1 = p - m' + 1, S2 = p - B - y - 1 + m', S3 = floor((p + kB - y - 1)/2) + 1 >= 1:
   V1 + S1 >= delta - B + 2;  V1 + S2 >= 2p - 1 - B - y >= delta - B;  V1 + S3 >= (delta - B + 4)/2;  V2 + S1 >= y + delta + 1 >=
   delta - B + 1;  V2 + S2 = delta - B - 1 + m + m' >= delta - B + 1;  V2 + S3 >= (y + delta)/2 + m >= (delta - B + 2)/2;
   V3 + S1 >= (delta - B + 4)/2;  V3 + S2 >= p - (y + B + 1)/2 + m' >= (delta - B + 2)/2;  V3 + S3 >= (k + 1)/2.
 (Used: y <= n = p + kB, resp. y <= n - 1, gives 2p - B - y >= delta - B, p - (y + B)/2 >= (delta - B)/2, etc.; y >= 1 - B, resp. -B,
 gives the U2/V2 bounds; delta - B >= 4 makes delta - B >= (delta - B + 2)/2; k + 1 >= delta - B + 2 as 2kB + 2B >= 1.)
Case s = 2: Q = {s', t}, Q' = {s'}, y in {2, 0, -2} (two aligned / one of each / two anti runs), m in {1, 2}.
 (B^s): b_s' + b_t <= delta - B - 1, resp. delta - B - 2, resp. delta - B - 3 (y = 2, 0, -2) by (1.2), while
 p + lam(y, m) - 1 = min(2p - m, p + y + m - kB - 1, p + floor((y + B)/2)) >= min(2p - 2, delta + y + m - 1, p + floor((y + B)/2)),
 which is >= delta + 2, resp. delta, resp. delta - 2 for y = 2, 0, -2 (m >= 1, B >= 2).
 (A^s): a_s' + a_t >= 1 - T for each term T of lamc(y, m) = min(p - m + 1, p - B - y + m, F + 1), F := floor((p + kB - y)/2).  By (1.2),
 a_s' + a_t >= B - delta + 3, B - delta + 2, B - delta + 1 for y = 2, 0, -2; this is >= m - p = 1 - (p - m + 1) (it is >= B + kB + 1 - p
 >= 2 - p >= m - p) and >= B + y - p >= 1 - (p - B - y + m) (the differences are kB + 1, kB + 2, kB + 3).  For T = F + 1 use either
 (1.2) or (1.4): by (1.4), a_s' + a_t >=
 4 - 2kB, 2 - 2kB, -2kB, which suffices if F >= 2kB - 4, 2kB - 2, 2kB; otherwise 2F <= 4kB - 10, 4kB - 6, 4kB - 2, so
 p + kB - y - 1 <= 2F gives p <= 3kB - 7, 3kB - 5, 3kB - 3 (y = 2, 0, -2), and then by (1.2) it suffices that F >= delta - B - 3,
 delta - B - 2, delta - B - 1, which follows from 2F >= p + kB - y - 1 and 3kB + 2B + 3 >= p.
Pin.  Let a be an anti run.  {a} and {a}^c are certified ({a}^c by the induction above), {a}^c has n aligned and B - 1 anti runs in one
block: lambda({a}^c) = lam(n - B + 1, 1) = min(p, p - B + 2, floor((p + kB + 1)/2) + 1) and U({a}^c) = p - lambda({a}) = p + kB.  So
X_[k] = x_a + X_({a}^c) lies in [-kB + lambda({a}^c), b_a + p + kB] (x_a >= -kB, Lemma SL for {a}^c), inside [1, 2p - 1]
(-kB + p - B + 2 >= 1 as kB + B <= p + 1; -kB + floor((p + kB + 1)/2) + 1 >= 1 as kB <= p + 1; b_a <= (delta - B - 3)/2 <= delta - 1),
and X_[k] = sum_t u_t = 0 (mod p): X_[k] = p.  []

## 3. Lemma C0 and Theorem SEED-B

**Lemma C0.**  Let w be an NMH word with R <= 2p - 3 and at most four even aligned runs.  If w avoids, there are no integers x_t with
sum_t x_t = p and X_Q >= lambda(Q) for every proper Q.
Proof.  This is the proof of Theorem C in c3/proof-C-r1.md Sec. 2 under hypothesis (i): it begins "Suppose w avoids; take x as in
(0.2)" and uses about x only sum_t x_t = p, X_Q >= lambda(Q) for proper Q (through the Kill lemma) and the definitions of Sec. 1
there; Case A is (A-i); Case B uses (2.1)-(2.3), (B1), (B2), all derived from sum x = p, the definitions and (0.1) there
(k >= 2kB + 2B + 3).  (H) enters Theorem C only through the existence of such x.  []
**Theorem SEED-B.**  Let p >= 11 be prime and (kB, B) satisfy RB and (E).  Then no all-single-letter word with k = p + kB + B runs,
exactly B of them rho_(-1) (at any positions), is an avoider: every such inherited all-odd RGR word of length 4p - 2 has an
identity 2p-subword.
Proof.  Suppose w avoids; take the canonical lifts x.  By Lemma IS, x_t in [a_t, b_t] for every run t; by Lemma SCW-B and Lemma SL,
X_Q >= lambda(Q) for every proper Q with |Q| >= 2, x_t >= lambda({t}) by the choice of the canonical lifts, and sum_t x_t = X_[k] = p.
w is an NMH word with R = k <= 2p - 3 (kB + B <= p - 4) and no even aligned runs, so Lemma C0 gives a contradiction.  []

## 4. Claim E and coverage

**Claim E.**  If p >= 19 and B >= 2, kB >= 1, 2B + kB <= p - 2, then (E) holds.
Proof.  If both inequalities of (E) fail, then with kB <= p - 2 - 2B: 3p < 5kB + B + 13 <= 5p - 9B + 3, so 9B < 2p + 3, and
4p < 2kB + 7B + 28 <= 2p + 3B + 24, so 3B > 2p - 24.  Hence 3(2p - 24) < 9B < 2p + 3, i.e. 4p < 75: p <= 18.  []
**Claim E'** (the exceptions; written derivation after Claude F2).  For p in {11, 13, 17} the classes of RB failing (E) are exactly
(kB, B) = (4, 2), (5, 2) for p = 11; (6, 2), (7, 2), (5, 3) for p = 13; (7, 4) for p = 17.
Proof.  If both inequalities of (E) fail, the proof of Claim E gives 9B < 2p + 3 and 3B > 2p - 24, and RB gives kB <= p - 2 - 2B.
p = 17: 3B > 10 and 9B < 37 give B = 4; then kB <= 7, and the failure of the first inequality (5kB > 34) gives kB = 7; (7, 4) fails
both (5 * 7 + 4 + 13 = 52 > 51, 2 * 7 + 28 + 28 = 70 > 68).  p = 13: 9B < 29 gives B in {2, 3}.  B = 2: the two failures read
5kB > 24 and 2kB > 10, and kB <= 7: kB in {6, 7}.  B = 3: 5kB > 23 with kB <= 5 gives kB = 5, and the second inequality fails as well
(2 * 5 + 21 + 28 = 59 > 52).  p = 11: 9B < 25 gives B = 2; 5kB > 18 with kB <= 5 gives kB in {4, 5}, and the second fails too
(2kB + 42 > 44).  Conversely each of the six classes lies in RB (2B + kB = 8, 9; 10, 11, 11; 15 <= p - 2) and fails both
inequalities (first: 35, 40 > 33; 45, 50, 41 > 39; 52 > 51; second: 50, 52 > 44; 54, 56, 59 > 52; 70 > 68).  []
([F] cross-check: out/seedB.txt Part A lists exactly these six classes of RB without (E).)
**Corollary SEED-B.**  For every prime p >= 19, every all-single-letter inherited all-odd RGR word of length 4p - 2 (an NMH word with
R = k) with B >= 2 anti runs (any positions), kB >= 1 and 2B + kB <= p - 2 has an identity 2p-subword.  For p = 11, 13, 17 the same
holds for every class of RB except the six classes of Claim E'.  Those six classes are excluded only computer-assisted [W+F]: they
satisfy the class-level hypotheses of Theorem IND* as certified by [F] (they are absent from the uncovered lists of
c5/out/indstar_classes.txt), and the two p = 11 classes are also excluded word by word in c5/out/allsing_run.txt.
In particular the four priority classes of c6/README.md T1, (p; kB, B) = (17; 5, 3), (17; 4, 4), (17; 5, 4), (17; 5, 5)
(k = 25, 25, 26, 27), satisfy RB and the singles case of (E) (5kB + B + 13 = 41, 37, 42, 43 <= 51): no word of them is an avoider.
Remarks.  (1) Where it applies, SEED-B replaces the hypothesis (H) (which fails for every word with an anti-heavy interval,
Proposition AB in Sec. 6) by the seeds: Lemma SCW-B certifies EVERY proper pattern although plain singleton extension does not.
(2) The region RB is used for: delta - B >= 2 (Case s >= 3), the generic values (1.1) (delta >= 2B + 2), realisability, and (E) for the
configuration.  Outside RB (2B + kB >= p - 1, "large B") the U-terms y + B - m dominate and the pair/single seeds widen; a type-level
exploration (c5/out/seedB_type.txt and c6 Sec. 7 log) shows failures there.

## 5. Exact computations [F] (aids; never hypotheses)

* seedB.py (out/seedB.txt): Part A, every prime 11 <= p <= 400 and every class of RB with (E) (860,700 classes; singles 706,795,
  pairs 153,905): every generic-regime inequality, realisability, the exact seeds computed from lam/U equal the closed forms,
  (1.2), no wrap-around, the 2-run steps, the pin, and every target <= ceil((delta - B + 2)/2): 0 failures; the classes of RB without (E)
  are exactly (11; 4, 2), (11; 5, 2), (13; 5, 3), (13; 6, 2), (13; 7, 2), (17; 7, 4).  Part B: the bound (delta - B + 2)/2 for both
  sums, both removal kinds, over all (y, m, m') of the domain, primes <= 31 (1,529,430 triples, 0 failures, minimum slack 0, i.e.
  the bound is attained), and all exact type steps (j, e, m) of every size, primes <= 19 (240,460 steps, 0 failures).  Part C:
  Claim E for every prime 19 <= p <= 600 (2,764,663 classes, 0 failures).  Part D (mutation controls, primes <= 23): canonical ranges
  instead of seeds: 32,980 of 661,885 type steps fail; seeds widened by 1: 0 fail (slack), by 2: 42, by 3: 1,443; one step outside RB
  (2B + kB = p - 1, primes < 200): all 4,000 configurations fail a generic-regime check.
* replayB.py (out/replayB_mut0.txt ... mut3.txt): literal replay on explicit words (anti runs in one block / spread / random) of the
  four p = 17 priority classes and 16 random classes of RB at p = 19, 23, 29, 37; Part 1 (full proof incl. the explicit configuration
  of Lemma IS for every run): 3,600 vectors: 720 singleton kills, 2,874 seed kills, 6 final kills; Part 2 (vectors in the seed
  boxes, later stages): 2,880 vectors: 825 pin-chain kills, 1,605 kills after Case A and 450 after Case B of Theorem C's procedure;
  every kill re-checked by c5's independent slow_lambda; 0 failures.  Mutation controls (each run draws its own 16 random classes):
  MUT 1 (canonical ranges instead of seeds): 940 of 6,480 vectors hit a failing certification step; MUT 2 (kill re-check against
  lambda - 1): 2,922 of 6,480 no-kill; MUT 3 (|S| = Delta in Theorem C's procedure): (M) breaks in all 286 Case B instances.
* Independent per-word census (c6/rcert2.cpp, all-pattern type-level two-pattern seeds, exhaustive certification DP; out/rcert_T1.txt,
  one word per dihedral class): (k, B, kB) = (25, 3, 5): 52 words, (25, 4, 4): 286, (26, 4, 5): 328, (27, 5, 5): 1,534 (2,200 words):
  every word satisfies (H') (plain certification closed under complements + pin) and the seeded (H's); (H) fails for exactly 14 words
  (1 + 13), the words of Proposition AB.  out/rcert_X.txt: rcert2 reproduces the frozen c5 receipt c5/out/allsing_run.txt (words,
  (H), (H^s), seedEmpty) on all 36 classes with p = 11, k <= 18 and p = 13, k <= 19.

## 6. Proposition AB: anti-heavy intervals are exactly what breaks (H) in the T1 classes

**Proposition AB.**  Let w be any all-single-letter NMH word (any prime p, kB >= 1, any B, any positions; NMH gives
B <= kappa - 1 < p + kB = A, so D = p + kB - B > 0).  If some interval Q (one cyclic block of
consecutive runs) has D_Q <= -4 when kB is odd, or D_Q <= -5 when kB is even, then Q is not certified by plain singleton extension
(Lemma L, singleton ranges [lambda({t}), U({t})]); in particular w fails (H).
Proof.  |Q| >= 4 and Q != [k] (D = p + kB - B > 0).  A certification of Q ends with a step Q = Q' u {t}, t in Q, Q' certified; its
condition (B) reads lambda(Q) + lambda(Q'^c) + lambda({t}^c) >= p + 1.  Put f := -D_Q (>= 4, resp. >= 5, by hypothesis), N := p + kB, d := d_t.  Taking one term of
each minimum: lambda(Q) <= D_Q + 1 - kB (m(Q) = 1), lambda(Q'^c) <= floor((N + f + d)/2) + 1 (D_(Q'^c) = D - D_Q + d), lambda({t}^c) <=
floor((N - d)/2) + 1.  So (B) needs floor((N + f + d)/2) + floor((N - d)/2) >= N + f - 2.  The left side is (2N + f - e)/2 where e is the
number of odd numbers among N + f + d, N - d: for N even (kB odd) e = 1 + [f even], for N odd (kB even) e = [f odd].  Hence (B) needs
f <= 3 - [f even] (N even), i.e. f <= 3, resp. f <= 4 - [f odd] (N odd), i.e. f <= 4.  For f >= 4 (kB odd), resp. f >= 5 (kB even), no
step into Q exists.  []
Consequences and data ([F] out/rcert_T1.txt, out/rmin_T1.txt):
* In the T1 classes, B <= 5: kB = 4 (even) would need D_Q <= -5, impossible with B = 4, and B = 3 makes D_Q <= -4 impossible: indeed all
  52 + 286 words of (25, 3, 5) and (25, 4, 4) satisfy (H).  For kB = 5 (odd) the anti-heavy intervals are AAAA and AAA1AA (A anti, 1
  aligned): (26, 4, 5) has exactly one such word (all four anti runs adjacent) and (27, 5, 5) exactly 13 (twelve containing AAAA, and
  AAA1AA); these are precisely the 1 + 13 words failing (H) in the census (with B = 5, D_Q <= -4 forces an interval
  with four anti runs and no aligned run, or five anti runs and at most one aligned run).  For six of them (anti sets {0,1,2,3} at
  k = 26, and {0,..,4}, {0,1,2,3,5}, {0,1,2,3,9}, {0,1,2,3,15}, {0,1,2,4,5} at k = 27) rmin.cpp counts ALL uncertified proper patterns:
  1, 5, 2, 1, 1, 1 (sizes in out/rmin_T1.txt) -- exactly the numbers of intervals with D_Q <= -4 in these words (e.g. for {0,..,4}:
  AAAA twice, AAAAA, and AAAAA with one adjacent aligned run on either side); there the uncertified patterns are exactly the intervals
  of Proposition AB.
* All 14 words satisfy (H') and (H's) (complements are certified), and all four classes are excluded by Theorem SEED-B, whose seeded
  certification (Lemma SCW-B) certifies the anti-heavy intervals.  The integer seed cap of an anti run (Lemma IS (c)) is
  s_hi = floor(delta/2) - floor(B/2) - 2 if y is even and ceil(delta/2) - floor((B + 1)/2) - 2 if y is odd (both <= floor((delta - B - 3)/2));
  it is lower than the plain cap floor(delta/2) - 1 by floor(B/2) + 1 (y even), resp. floor((B + 1)/2) + 1 - [delta odd] (y odd).  In the
  two classes that contain Proposition-AB words, (17; 5, 4) and (17; 5, 5), y = m = 6 is even, s_hi = 2 and the gain is 3 =
  floor(B/2) + 1; in general the gain depends on the parity of y, e.g. (17; 5, 3) (m = 5, delta = 12, s_hi = 2): gain 3, and (17; 4, 4)
  (m = 5, delta = 13, s_hi = 3): gain 2.  [r2 compared the real bound (delta - B - 3)/2 with the integer plain cap and stated the gain
  floor(B/2) + 1 in general; corrected after the Codex (rounding) and Claude (F3) reviews.]
* Exact control of Proposition AB (abcheck.cpp, out/abcheck.txt): every all-single-letter item-(iii) class with B >= 4 at p = 11
  (k <= 19) and p = 13 (k <= 20), every word (one per rotation class): 16 classes, 11,155 words, 2,143 intervals with D_Q <= -4 (kB odd)
  resp. <= -5 (kB even): none is certified by plain singleton extension (0 violations).  Sharpness (mutation of the threshold by one):
  of the 9,850 intervals with D_Q = -3 (kB odd) resp. -4 (kB even), 3,443 ARE certified, so the threshold cannot be raised by one.

## 7. Note on c6/c5-fixes/proof-Cplus-r2.md (Claude F8)

Lines 27-28 of c6/c5-fixes/proof-Cplus-r2.md ('Written in c5/ after host clock 2026-10-17T15:07:36-0700 ...', 'target T4 of
c5/README.md') are the r1 provenance, kept verbatim from r1; the r2 text itself was written 2026-10-17T16:26:30-0700 in c6/ (its
line 3).  No statement or proof step is affected, and the frozen r2 file is not changed.
