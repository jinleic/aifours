# Theorem SEED-G: seeded certification for every NMH word with R <= 2p - 3; Corollaries SA, PA (words with excess) and Propositions RA2, RA3 (large B, B <= 3)

Version r1, written 2026-10-17T17:27:14-0700 in c6/ (task OlsonRunCount5, cycle 6; parent direction 2026-10-17 17:1x: continue SEED-E/SEED-G
on large B and on the excess words) = the unfrozen draft c6/proof-SEEDG.md (2026-10-17T17:26:07-0700, sha256 97ac27034e6a3602...; kept, never
cited) with one wording correction in the [Details] of Lemma SCW-G (which sums use m' <= m and which use m' >= m - 1).
Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).  Freeze time and
SHA-256 in c6/out/freeze.txt.  Paths "c3/...", "c5/...", "c6/..." are relative to mixdef-high/.
Imported (not re-proved): Lemma H with beta = 0 and the Claim in the proof of Lemma BC (../../../inverse-parity/proof-PAR-K0.md
Secs. 1-2); c3/proof-C-r1.md Sec. 0 (setting, (0.1)), Secs. 1-2 (Theorem C, reviewed); c6/c5-fixes/proof-Cplus-r2.md Sec. 2
(Theorem C+, reviewed), used only through Lemma C0+ below; the proofs of Lemmas TS and SL of c6/proof-SEEDB-r3.md (reviewed),
which use only Lemma H and the Claim and are restated here for every NMH word.
Not used: (H), Lemma L, the certificate of Lemma BC, Theorem IND*, any computation.
Scope: every NMH word with R <= 2p - 3 in the setting of c3/proof-C-r1.md Sec. 0 (in particular every item-(iii) word).
Theorem SEED-G has per-word hypotheses; Corollaries SA, PA and Propositions RA2, RA3 are uniform in explicit parameter regions.
NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson for D_(2p).

## 0. Setting

p >= 5 prime; w an NMH word with R <= 2p - 3: all reflection runs odd, k >= p + 1 rotation runs, every run pure aligned (a_t >= 1
letters rho_1, d_t = a_t), pure anti (b_t >= 1 letters rho_(-1), d_t = -b_t) or a (1,1)-pair (d_t = 0), 1 <= B <= kappa - 1,
B <= A <= 2p - 1, kB := kappa - B >= 1, D := A - B = 2p - k + 2kB, E := R - k = sum_t (r_t - 1) (even, E/2 = p - k + kappa), and
(c3 (0.1)) k >= 2kappa + 3.  Put
   Delta0 := 2p - R.   Then  R = p + kappa + E/2,  Delta0 = k - 2kappa = p - kappa - E/2 >= 3,  R - 2kappa = Delta0 + E = 2p - k,
   A - kappa = p - B + E/2,  A = p + kB + E/2,  2p - A = Delta0 + B,  A - kappa - Delta0 = kB + E.                      (0.1')
(k = p + kappa - E/2 from E/2 = p - k + kappa; the rest is arithmetic.)  For a run t let a+_t, b+_t be its numbers of letters
rho_1, rho_(-1) (so d_t = a+_t - b+_t; a pair has a+ = b+ = 1).  A run has r_t - 1 <= E, so
   -min(B, E + 1) <= d_t <= E + 1,  and for two runs s != t:  -B <= d_s + d_t <= E + 2                                 (0.2')
(d_s + d_t <= a+_s + a+_t <= (r_s - 1) + (r_t - 1) + 2; d_s + d_t >= -(b+_s + b+_t) >= -B).
Lemma H (beta = 0) for a proper pattern Q with y := D_Q and m := m(Q) blocks (Q^c has D - y and m blocks):
   lambda(Q)   = lam(y, m)  := min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
   lambda(Q^c) = lamc(y, m) := min(p - m + 1, A - kappa - y + m, floor((A - y)/2) + 1),     U(Q) := p - lambda(Q^c).
(D - y + m - kB = A - kappa - y + m and floor((D - y + B)/2) = floor((A - y)/2).)  The blocks of Q and Q^c alternate, so 2m <= k and
   (F1)  p - m + 1 >= p + 1 - k/2 = (Delta0 + E)/2 + 1.
If w avoids (u_t the half-sums of Lemma H, u_Q := sum_(t in Q) u_t, u_[k] = 0):
(ARC) for every proper Q, lambda(Q) + lambda(Q^c) <= p and u_Q is congruent to an integer of [lambda(Q), U(Q)];
(CLAIM) if y is an integer, y = u_Q (mod p) and 1 - lambda(Q^c) <= y <= p + lambda(Q) - 1, then lambda(Q) <= y <= U(Q).
**Lemma P0.**  For every run t, lambda({t}) + lambda({t}^c) >= 1.
Proof.  With d := d_t: lambda({t}) = min(p, d + 1 - kB, floor((d + B)/2) + 1), lambda({t}^c) = min(p, A - kappa - d + 1,
floor((A - d)/2) + 1); the sum is the least of the nine sums of one term from each.  The terms d + 1 - kB >= 1 - kappa, floor((d + B)/2) + 1
>= 1, A - kappa - d + 1 >= p - B - E/2 (d <= E + 1) and floor((A - d)/2) + 1 >= 1 (d <= a+_t <= A) are all > -p, so sums containing
a term p are >= 1.  Further (d + 1 - kB) + (A - kappa - d + 1) = Delta0 + E + 2; (d + 1 - kB) + floor((A - d)/2) + 1 >= (A + d + 3)/2 - kB >=
(A - B - 2kB + 3)/2 = (Delta0 + E + 3)/2 (d >= -B); floor((d + B)/2) + 1 + (A - kappa - d + 1) >= A - kappa + 1 + (B + 1 - d)/2 >=
p + 1 - B/2 (d <= E + 1); floor((d + B)/2) + floor((A - d)/2) + 2 >= R/2 + 1.  All are >= 1.  []
Canonical lifts.  If w avoids, x_t := the unique integer of [lambda({t}), U({t})] congruent to u_t (it exists by (ARC); the interval
has p + 1 - lambda({t}) - lambda({t}^c) <= p integers by Lemma P0).  X_Q := sum_(t in Q) x_t = u_Q (mod p).

## 1. Seeds

**Lemma TS** (c6/proof-SEEDB-r3.md, verbatim for any NMH word).  Let w avoid, t a run, Q a proper pattern with t notin Q and Q + t
:= Q u {t} proper.  Then u_t is congruent to an integer of [lambda(Q + t) - U(Q), U(Q + t) - lambda(Q)].
Proof.  u_(Q+t) = z1 and u_Q = z2 (mod p) with z1 in [lambda(Q + t), U(Q + t)], z2 in [lambda(Q), U(Q)] by (ARC); take z1 - z2.  []
**Definition.**  A seed for a run t (weight d := d_t) is an integer interval [a_t, b_t] with lambda({t}) <= a_t <= b_t <= U({t})
such that, if w avoids, x_t lies in [a_t, b_t].  It is a quality seed if
   (QS)  a_t >= (d - Delta0)/2 + 1   and   b_t <= (d + Delta0)/2 - 1.
(If the conditions defining [a_t, b_t] leave no integer, i.e. "a_t > b_t", then w does not avoid.)
**Lemma NW (no wrap).**  If s_lo >= (d - Delta0)/2 + 1 and s_hi <= (d + Delta0)/2 - 1, then lambda({t}) - s_hi > -p and
U({t}) - s_lo < p.
Proof.  lambda({t}) = min(p, d + 1 - kB, floor((d + B)/2) + 1) and lambda({t}) - s_hi >= lambda({t}) - (d + Delta0)/2 + 1.  Term p:
2p + 1 > (d + Delta0)/2 as d + Delta0 <= E + 1 + Delta0 = 2p - k + 1.  Term d + 1 - kB: d/2 + 2 - kB - Delta0/2 + p >=
d/2 + 2 + p/2 - kB/2 + B/2 > 0 (Delta0 <= p - kappa, d >= -B, kB < p).  Term floor((d + B)/2) + 1: >= (B - 1 - Delta0)/2 + 2 > -p.
U({t}) = max(0, d + B - E/2 - 1, ceil((Delta0 + B + d)/2) - 1) (as p - A + kappa = B - E/2 and 2p - A = Delta0 + B), and
U({t}) - s_lo <= U({t}) - (d - Delta0)/2 - 1.  Term 0: (Delta0 - d)/2 - 1 < p as Delta0 - d <= Delta0 + B < 2p.  Term d + B - E/2 - 1:
d/2 + B - E/2 + Delta0/2 - 2 <= B - kappa/2 + p/2 - 3/2 < p (d <= E + 1, Delta0 = p - kappa - E/2, B <= kappa - 1).  Term
ceil((Delta0 + B + d)/2) - 1: <= (2 Delta0 + B + 1)/2 - 2 < p as 2 Delta0 + B = 2p - 2kappa - E + B < 2p + 3.  []
**Lemma GS (seeds from configurations).**  Let t be a run and Q a proper pattern with t notin Q and Q + t proper; s_lo :=
lambda(Q + t) - U(Q), s_hi := U(Q + t) - lambda(Q), d := d_t.
(a) If lambda({t}) - s_hi > -p and U({t}) - s_lo < p, then [max(lambda({t}), s_lo), min(U({t}), s_hi)] is a seed for t.  The
    intersection of seeds for t is a seed for t.
(b) Call a pattern P generic if lambda(P) = floor((D_P + B)/2) + 1 and lambda(P^c) = floor((A - D_P)/2) + 1.  If Q and Q + t are
    generic, then (d - Delta0)/2 + 1 <= s_lo and s_hi <= (d + Delta0)/2 - 1; so the hypothesis of (a) holds (Lemma NW) and the seed
    of (a) is a quality seed.
Proof.  (a) Lemma TS gives z = x_t (mod p) with z in [s_lo, s_hi]; x_t - z lies in [lambda({t}) - s_hi, U({t}) - s_lo], strictly
between -p and p, and is a multiple of p: x_t = z.  (b) With y := D_Q and floor(a/2) >= (a - 1)/2:
s_lo = floor((y + d + B)/2) + 1 - p + floor((A - y)/2) + 1 >= (y + d + B - 1)/2 + (A - y - 1)/2 + 2 - p = (d + R)/2 + 1 - p =
(d - Delta0)/2 + 1, and s_hi = p - floor((A - y - d)/2) - 1 - floor((y + B)/2) - 1 <= p - (R - d - 2)/2 - 2 = (d + Delta0)/2 - 1.  []

## 2. Seeded certification of every proper pattern

**Lemma SL** (c6/proof-SEEDB-r3.md, verbatim for any NMH word).  Let w avoid, x the canonical lifts, [a_t, b_t] integer intervals
with x_t in [a_t, b_t].  Call a proper Q certified if |Q| = 1, or Q = Q' u {t} (t notin Q') with Q' certified and
   (A^s) lo(Q') + a_t >= 1 - lambda(Q^c),     (B^s) hi(Q') + b_t <= p + lambda(Q) - 1,
where [lo(Q'), hi(Q')] := [a_s, b_s] if Q' = {s} and := [lambda(Q'), U(Q')] if |Q'| >= 2.  Then lambda(Q) <= X_Q <= U(Q) for every
certified Q with |Q| >= 2.
Proof.  Induction on |Q|: X_Q = X_(Q') + x_t lies in [lo(Q') + a_t, hi(Q') + b_t], inside [1 - lambda(Q^c), p + lambda(Q) - 1] by (A^s),
(B^s); X_Q = u_Q (mod p), and (CLAIM) gives lambda(Q) <= X_Q <= U(Q).  []
**Lemma SCW-G.**  Let w avoid and let every run t have a quality seed [a_t, b_t].  Then every proper pattern is certified (with these
ranges), and X_[k] = p.
Proof.  Induction on s := |Q| >= 2.  Let t be an end run of a block of Q (a run of Q with at most one neighbour in Q; it exists as Q is
proper); Q' := Q - {t} is proper and nonempty, with m' := m(Q') in {m - 1, m} and m' >= 1 (m := m(Q)); Q' is certified by induction
(or |Q'| = 1).  Put y := D_Q, d := d_t, y' := y - d = D_(Q').  As Q' avoids t and Q contains t,
   -B - min(d, 0) <= y' <= A - max(d, 0),     -B + max(d, 0) <= y <= A + min(d, 0)                                    (2.1)
(y' >= -(B - b+_t), y' <= A - a+_t, a+_t >= max(d, 0), b+_t >= max(-d, 0)).  By (QS), 1 - a_t <= (Delta0 - d)/2 and b_t + 1 <= (Delta0 + d)/2.
Case s >= 3 (|Q'| >= 2).  (A^s) <=> lam(y', m') + lamc(y, m) >= 1 - a_t and (B^s) <=> lam(y, m) + lamc(y', m') >= b_t + 1, so it
suffices that each of the nine term sums below is >= (Delta0 - d)/2, resp. >= (Delta0 + d)/2.  Used: (F1) for m and m' <= m, (2.1),
(0.1'), (0.2'), floor(a/2) >= (a - 1)/2, R >= Delta0 (R >= k >= p + 1 > Delta0).
 (A^s) terms U1 = p - m' + 1, U2 = y' + m' - kB, U3 = floor((y' + B)/2) + 1 >= 1 (y' >= -B); T1 = p - m + 1, T2 = A - kappa - y + m,
 T3 = floor((A - y)/2) + 1 >= 1 (y <= A):
   U1 + T1 >= Delta0 + E + 2;   U1 + T2 >= p + 1 + A - kappa - y >= Delta0 + E/2 + 1 - min(d, 0);   U1 + T3 >= (Delta0 + E)/2 + 2;
   U2 + T1 >= y' - kB + p >= Delta0 + E/2 - min(d, 0);   U2 + T2 = A - kappa - kB - d + m + m' >= Delta0 + E - d + 1;
   U2 + T3 >= (y' + A - d + 1)/2 + m' - kB >= (Delta0 + E - d - min(d, 0) + 3)/2;   U3 + T1 >= (Delta0 + E)/2 + 2;
   U3 + T2 >= A - kappa - d + 1 + (B + 1 - y')/2 >= (Delta0 + E + 3)/2 - d + max(d, 0)/2;   U3 + T3 >= (R - d)/2 + 1.
 Each is >= (Delta0 - d)/2, using -(E + 1) <= d <= E + 1.
 (B^s) terms V1 = p - m + 1, V2 = y + m - kB, V3 = floor((y + B)/2) + 1 >= 1; S1 = p - m' + 1, S2 = A - kappa - y' + m',
 S3 = floor((A - y')/2) + 1 >= 1:
   V1 + S1 >= Delta0 + E + 2;   V1 + S2 >= p + A - kappa - y' >= Delta0 + E/2 + max(d, 0);   V1 + S3 >= (Delta0 + E)/2 + 2;
   V2 + S1 >= y - kB + p + 1 >= Delta0 + E/2 + max(d, 0) + 1;   V2 + S2 = A - kappa - kB + d + m + m' >= Delta0 + E + d + 1;
   V2 + S3 >= (y + A + d + 1)/2 + m - kB >= (Delta0 + E + max(d, 0) + d + 3)/2;   V3 + S1 >= (Delta0 + E)/2 + 2;
   V3 + S2 >= A - kappa + d + 1 + (B + 1 - y)/2 >= (Delta0 + E + 3)/2 + d - min(d, 0)/2;   V3 + S3 >= (R + d)/2 + 1.
 Each is >= (Delta0 + d)/2.
 [Details: U1 + T2 and V2 + S1 use m' <= m, U2 + T1 and V1 + S2 use m' >= m - 1, all four with (2.1) and p - kappa = Delta0 + E/2;
 U2 + T2 and V2 + S2 use
 A - kappa - kB = R - 2kappa = Delta0 + E; U2 + T3, V2 + S3 use m' >= 1, m >= 1 and A - B - 2kB = Delta0 + E; U3 + T2, V3 + S2 use
 A + B - 2kappa = Delta0 + E and (2.1).]
Case s = 2: Q = {s', t}, Q' = {s'}, y = d_(s') + d_t, m in {1, 2}; X_Q ranges over [a_(s') + a_t, b_(s') + b_t].
 (B^s): by (QS), b_(s') + b_t <= y/2 + Delta0 - 2; this is <= p - 1 + T for each term T of lam(y, m): T = p - m + 1 >= p - 1 (as
 y <= E + 2 and Delta0 + E/2 + 1 <= 2p - k + 1 <= 2p); T = y + m - kB >= y + 1 - kB (as Delta0 - p + kB = -B - E/2 and y >= -B);
 T = floor((y + B)/2) + 1 >= (y + B + 1)/2 (as Delta0 <= p + (B + 3)/2).
 (A^s): a_(s') + a_t >= 1 - T for each term T of lamc(y, m).  By (QS), a_(s') + a_t >= y/2 - Delta0 + 2.  T = p - m + 1 >= p - 1:
 y/2 - Delta0 + 2 >= 2 - p as y >= -B >= -2kappa - E = 2 Delta0 - 2p.  T = A - kappa - y + m >= A - kappa - y + 1: y/2 - Delta0 + 2 >=
 y + kappa - A as A - kappa - Delta0 + 2 = kB + E + 2 >= y/2 (y <= E + 2).  T = F + 1, F := floor((A - y)/2) >= 0: if 2 Delta0 <= A + 3,
 then y/2 - Delta0 + 2 >= -(A - y - 1)/2 >= -F.  Otherwise 2 Delta0 >= A + 4, i.e. (0.1') p >= 3kB + 2B + 3E/2 + 4.  Now
 a_u >= lambda({u}) = min(d_u + 1 - kB, floor((d_u + B)/2) + 1) for u = s', t (the term p is never the least: d_u + 1 - kB <= p).
  - If lambda({u}) = d_u + 1 - kB for both, a_(s') + a_t >= y + 2 - 2kB, which is >= -F as soon as A + y + 3 >= 4kB; if instead
    A + y + 3 < 4kB, i.e. p < 3kB - E/2 - y - 3, then 3kB + 2B + 3E/2 + 4 < 3kB - E/2 - y - 3, i.e. 2B + 2E + y + 7 < 0, impossible
    (y >= -B).
  - Otherwise some u has floor((d_u + B)/2) + 1 < d_u + 1 - kB, i.e. d_u > 2kB + B - 1, so lambda({u}) >= kB + B + 1, while the other run
    v has lambda({v}) >= min(d_v + 1 - kB, 1) >= 1 - B - kB (d_v >= -B); the sum is >= 2 > -F.
Pin.  Let a be any run.  {a}^c is certified (case s >= 2 above, |{a}^c| = k - 1 >= 2), so X_[k] = x_a + X_({a}^c) lies in
[a_a + lambda({a}^c), b_a + U({a}^c)].  Lower end: a_a >= lambda({a}), and lambda({a}) + lambda({a}^c) >= 1 (Lemma P0).  Upper end:
U({a}^c) = p - lambda({a}); with d := d_a, if lambda({a}) = d + 1 - kB then b_a - lambda({a}) <= (Delta0 - d)/2 + kB - 2 <= p - 1
(Delta0 + 2kB - d <= p + kB - B - E/2 + B <= 2p); if lambda({a}) = floor((d + B)/2) + 1 then b_a - lambda({a}) <= (Delta0 - B - 1)/2 - 1
< p - 1.  So X_[k] lies in [1, 2p - 1]; X_[k] = sum_t u_t = 0 (mod p), hence X_[k] = p.  []

## 3. Lemma C0+ and Theorem SEED-G

**Lemma C0+.**  Let w be an NMH word with R <= 2p - 3 satisfying (i) n_ev,al <= 4, or (ii+) 2kB <= p and n_ev,al <= 2(k - kB - 2B)
+ n_pr - 1 (n_ev,al: even aligned runs, n_pr: pairs).  If w avoids, there are no integers x_t with sum_t x_t = p and X_Q >= lambda(Q)
for every proper Q.
Proof.  This is the proof of Theorem C+ (c6/c5-fixes/proof-Cplus-r2.md Sec. 2, which runs c3/proof-C-r1.md Secs. 1-2 with the
steps (B1+), (B2+)).  It begins "Suppose w avoids; take x as in (0.2)" and uses about x only sum_t x_t = p and X_Q >= lambda(Q) for
proper Q (through the Kill lemma; in (A-ii) the singleton case X_({t}) >= lambda({t})); (H) enters Theorem C+ only through the
existence of such x (as for Lemma C0 of c6/proof-SEEDB-r3.md, there under (i)).  []
**Theorem SEED-G.**  Let w be an NMH word with R <= 2p - 3 (in particular any item-(iii) word) that satisfies (i) or (ii+) of Lemma
C0+ and in which every run has a quality seed.  Then w has an identity 2p-subword.
Proof.  Suppose w avoids; take the canonical lifts.  By Lemmas SCW-G and SL, X_Q >= lambda(Q) for every proper Q with |Q| >= 2, x_t >=
lambda({t}) by the choice of the lifts, and sum_t x_t = X_[k] = p.  Lemma C0+ gives a contradiction.  []
Remarks.  (1) A quality seed for t exists as soon as some Q has Q and Q + t generic (Lemma GS (b)); it may also come from non-generic
configurations (Lemma GS (a)), as in Proposition RA3.  If the seeds of a run are inconsistent (empty intersection), w is excluded
directly.  (2) Theorem SEED-B (c6/proof-SEEDB-r3.md) is the case E = 0 with the configurations of its Lemma IS: there
Delta0 = delta - B and (1.2) of SEED-B is (QS).  The new content here is that Lemma SCW-G needs nothing but (QS): no region, any run
lengths, (1,1)-pairs and long anti runs included.  (3) For words with excess the conditions (i)/(ii+) hold whenever E <= 4, or
2kB <= p and E <= 2(k - kB - 2B) - 1 (n_ev,al <= e_al <= E and n_pr >= 0, e_al the aligned excess).

## 4. Configurations, Corollaries SA and PA

**Lemma CF (configurations).**  Let w be an NMH word with R <= 2p - 3, t a run, n_al the number of aligned runs (n_al = k - B + e_an
>= k - B, where e_an := sum_anti (b_u - 1), since n_an + n_pr = B - e_an), e_t := r_t - 1 the excess of t.  Delete t and its two
neighbours; the remaining k - 3 runs form a path whose two ends are not adjacent in the cycle (k >= 12).
 (SA) If 1 <= m <= ceil((n_al - 3)/2), there are m pairwise non-adjacent aligned runs, none adjacent to t: the aligned runs of the
      path lie in maximal intervals of consecutive aligned runs of lengths L_i with sum L_i >= n_al - 3; take every other run of each
      interval, ceil(L_i/2) >= L_i/2 of them (runs from different intervals are separated by a run of the path).
 (PA) If 1 <= m <= ceil((n_al - B - 4)/3), there are m pairwise non-adjacent blocks {u, u + 1} of two adjacent aligned runs, none
      adjacent to t: the path contains at most n_an + n_pr <= B non-aligned runs, hence at most B + 1 maximal aligned intervals; an
      interval of length L contains floor((L + 1)/3) >= (L - 1)/3 blocks {l, l + 1}, {l + 3, l + 4}, ...
 In both cases Q (the union) has m blocks, Q + t has m + 1 blocks, and both are proper (2m + 2 <= k).  Its type: y := D_Q is the
 number of letters of the chosen runs, m <= y <= m + E - e_t (SA), resp. 2m <= y <= 2m + E - e_t (PA), since the chosen runs carry
 at most E - e_t excess letters; in particular y + d_t <= m + E + 1, resp. 2m + E + 1 (for an aligned t, d_t = e_t + 1; otherwise
 d_t <= 0).  (In a word without excess y = m, resp. 2m.)
**Corollary SA.**  Let (p, k, kappa, B) be the parameters of an NMH word w with R <= 2p - 3, E := R - k, b* := min(B, E + 1) (or any
upper bound for the lengths of the anti runs of w), and suppose some integer m satisfies
   (SA)  max(ceil((2kB + B + max(2, b*))/3), B + 2 - Delta0, 1) <= m <= min(floor((2p - B - E - 3)/3), Delta0 + B - b* - 2,
         ceil((k - B - 3)/2)).
Then every run of w has a quality seed; if w satisfies (i) or (ii+), w has an identity 2p-subword.
Proof.  For every run t take Q as in Lemma CF (SA) (m <= ceil((k - B - 3)/2) <= ceil((n_al - 3)/2)).  We show that Q and Q + t are
generic; Lemma GS (b) and Theorem SEED-G then finish.  Write d := d_t, so -b* <= d <= E + 1 and m <= y <= m + E, y + d <= m + E + 1,
and recall that a minimum equals its third term iff the other terms are >= it.  With floor(a/2) <= a/2:
 lambda(Q) = floor((y + B)/2) + 1: (a1) floor((y + B)/2) + 1 <= p - m + 1 follows from 3m + E + B <= 2p; (a2) floor((y + B)/2) + 1 <=
   y + m - kB: the difference RHS - LHS is non-decreasing in y, so y = m is worst, and (m + B)/2 + 1 <= 2m - kB is 3m >= 2kB + B + 2.
 lambda(Q + t) = floor((y + d + B)/2) + 1 (Q + t has m + 1 blocks): (b1) <= p - m follows from (y + d + B)/2 + 1 <= (m + E + 1 + B)/2 + 1
   <= p - m, i.e. 3m <= 2p - B - E - 3; (b2) <= y + d + m + 1 - kB: worst at the least y + d = m - b*, where (m - b* + B)/2 <=
   2m - b* - kB is 3m >= 2kB + B + b*.
 lambda(Q^c) = floor((A - y)/2) + 1: (c1) <= p - m + 1 follows from (A - y)/2 <= p - m, worst y = m: m <= 2p - A = Delta0 + B;
   (c2) <= A - kappa - y + m: RHS - LHS is non-increasing in y, worst y = m + E: (A - m - E)/2 + 1 <= A - kappa - E is
   m >= 2kappa + 2 - A + E = B + 2 - Delta0 (A - 2kappa = Delta0 + E - B).
 lambda((Q + t)^c) = floor((A - y - d)/2) + 1: (d1) <= p - (m + 1) + 1 = p - m: worst y + d = m - b*: (A - m + b*)/2 + 1 <= p - m is
   m <= Delta0 + B - b* - 2; (d2) <= A - kappa - (y + d) + m + 1: worst y + d = m + E + 1: m >= B + 1 - Delta0.
 (a1) and (c1) are implied by (b1) and (d1).  All hold under (SA).  []
**Corollary PA.**  Same setting.  Suppose Delta0 >= B + 1, b* <= Delta0 + B - 1 and some integer m satisfies
   (PA)  max(ceil((kB + floor(B/2) + 1)/2), ceil((kB + b* + floor((B - b*)/2))/2), 1) <= m
         <= min(floor((p - 1 - floor((E + B + 1)/2))/2), ceil((k - 2B - 4)/3)).
Then every run of w has a quality seed; if w satisfies (i) or (ii+), w has an identity 2p-subword.
Proof.  Q as in Lemma CF (PA) (m <= ceil((k - 2B - 4)/3) <= ceil((n_al - B - 4)/3)); 2m <= y <= 2m + E, y + d <= 2m + E + 1, d >= -b*.
 (a1) floor((y + B)/2) + 1 <= p - m + 1: worst y = 2m + E: m + floor((E + B)/2) <= p - m, implied by (b1).  (a2) floor((y + B)/2) + 1
 <= y + m - kB: worst y = 2m: m + floor(B/2) + 1 <= 3m - kB.  (b1) floor((y + d + B)/2) + 1 <= p - m: worst y + d = 2m + E + 1:
 m + floor((E + B + 1)/2) + 1 <= p - m.  (b2) floor((y + d + B)/2) + 1 <= y + d + m + 1 - kB: worst y + d = 2m - b*:
 m + floor((B - b*)/2) <= 3m - b* - kB.  (c1) floor((A - y)/2) + 1 <= p - m + 1: worst y = 2m: floor(A/2) <= p (A <= 2p - 1).
 (c2) floor((A - y)/2) + 1 <= A - kappa - y + m: worst y = 2m + E: floor((A - E)/2) + 1 <= A - kappa - E, i.e. ceil((A - E)/2) >= kappa + 1,
 i.e. A - E >= 2kappa + 1, i.e. Delta0 >= B + 1.  (d1) floor((A - y - d)/2) + 1 <= p - m: worst y + d = 2m - b*: floor((A + b*)/2) <= p - 1,
 i.e. b* <= 2p - 1 - A = Delta0 + B - 1.  (d2) floor((A - y - d)/2) + 1 <= A - kappa - (y + d) + m + 1: worst y + d = 2m + E + 1:
 ceil((A - E - 1)/2) >= kappa, i.e. Delta0 >= B.  (Monotonicity as in Corollary SA.)  Lemma GS (b), Theorem SEED-G.  []
Remark.  For E = 0 (all single letters, b* = 1) Corollary SA is the singles case of SEED-B's Lemma IS with the weaker condition
m >= B + 2 - Delta0 in place of delta >= 2B + 2; Corollary PA is its pairs case.  The regions are monotone in b*: a class satisfying
them with b* = min(B, E + 1) satisfies them for every word of the class, with the same m.

## 5. Large B with B <= 3: Propositions RA2 and RA3

The all-single-letter item-(iii) classes with B >= 2 and 2B + kB >= p - 1 (outside SEED-B's region) and B <= 3 are exactly
(B, kB) = (2, p - 5), (3, p - 6), (3, p - 7), since kB + B <= p - 3 (R = k = p + kB + B <= 2p - 3).  Here E = 0, A = n := p + kB,
kappa = kB + B, Delta0 = p - kappa, and every aligned run is a single letter.  Q := m pairwise non-adjacent blocks of two adjacent
aligned runs, none adjacent to t (Lemma CF (PA), available for m <= ceil((n - B - 4)/3)); type (2m, m), Q + t: (2m + d, m + 1).
**Proposition RA2.**  Let p >= 11 be prime.  No all-single-letter NMH word with B = 2 and kB = p - 5 (k = 2p - 3) avoids.
Proof.  m := (p - 3)/2; available: (p - 3)/2 <= (2p - 11)/3 for p >= 13, and for p = 11 the count is an integer >= 11/3, so >= 4 = m.
A = 2p - 5, kappa = p - 3, A - kappa = p - 2, Delta0 = 3.  Then (using m = (p - 3)/2):
 lam(2m, m) = min((p + 5)/2, 3m - p + 5 = (p + 1)/2, m + 2) = m + 2;  lamc(2m, m) = min(p - m + 1, p - 2 - m, p - m - 2) = p - m - 2, U = m + 2;
 aligned t: lam(2m + 1, m + 1) = min((p + 3)/2, (p + 5)/2, m + 2) = m + 2; lamc(2m + 1, m + 1) = min(p - m, p - 2 - m, p - m - 2) = p - m - 2,
   U = m + 2; seed [(m + 2) - (m + 2), (m + 2) - (m + 2)] = [0, 0];
 anti t: lam(2m - 1, m + 1) = min((p + 3)/2, (p + 1)/2, m + 1) = m + 1; lamc(2m - 1, m + 1) = min(p - m, p - m, p - m - 1) = p - m - 1, U = m + 1;
   seed [(m + 1) - (m + 2), (m + 1) - (m + 2)] = [-1, -1].
(Terms: lamc uses A - kappa - y + m' and floor((A - y)/2) + 1 with m' the number of blocks.)  Both seeds satisfy (QS) for Delta0 = 3
(aligned: [0, 1], anti: [-1, 0]), so Lemma NW and Lemma GS (a) apply: if w avoids, x_t = 0 on every aligned run and x_t = -1 on both
anti runs, so sum_t x_t = -2.  But sum_t x_t = u_[k] = 0 (mod p): contradiction.  []
**Proposition RA3.**  No all-single-letter NMH word with (a) B = 3, kB = p - 6 (k = 2p - 3), p >= 13 prime, or (b) B = 3, kB = p - 7
(k = 2p - 4), p >= 11 prime, avoids.
Proof.  E = 0 and n_ev,al = 0, so (i) holds and by Theorem SEED-G it suffices to give quality seeds.  (QS) asks for aligned seeds in
[0, 1] and anti seeds in [-1, 0] in both cases (Delta0 = 3, resp. 4).
(a) m := (p - 3)/2 (available: (2p - 13)/3 >= m for p >= 17; p = 13: the count is an integer >= 13/3, so >= 5 = m).  A = 2p - 6,
 kappa = p - 3, A - kappa = p - 3.  lam(2m, m) = min((p + 5)/2, (p + 3)/2, m + 2) = m + 2; lamc(2m, m) = min(p - m + 1, p - 3 - m, p - m - 2)
 = p - m - 3, U = m + 3.  Aligned t: lam(2m + 1, m + 1) = min(m + 3, (p + 7)/2, m + 3) = m + 3, lamc(2m + 1, m + 1) = min(p - m, p - 3 - m,
 p - m - 3) = p - m - 3, U = m + 3: seed [0, 1].  Anti t: lam(2m - 1, m + 1) = min(m + 3, m + 3, m + 2) = m + 2, lamc(2m - 1, m + 1) =
 min(p - m, p - 1 - m, p - m - 2) = p - m - 2, U = m + 2: seed [-1, 0].
(b) m := (p - 5)/2 (available: (2p - 14)/3 >= m for p >= 13; p = 11: the count is an integer >= 8/3, so >= 3 = m).  A = 2p - 7,
 kappa = p - 4, A - kappa = p - 3.  lam(2m, m) = min((p + 7)/2, (p - 1)/2, m + 2) = m + 2; lamc(2m, m) = min(p - m + 1, p - 3 - m, p - m - 3)
 = p - m - 3, U = m + 3.  Aligned t: lam(2m + 1, m + 1) = min(m + 5, m + 4, m + 3) = m + 3, lamc(2m + 1, m + 1) = min(p - m, p - 3 - m,
 p - m - 3) = p - m - 3, U = m + 3: seed [0, 1].  Anti t: lam(2m - 1, m + 1) = min(m + 5, m + 2, m + 2) = m + 2, lamc(2m - 1, m + 1) =
 min(p - m, p - 1 - m, p - m - 2) = p - m - 2, U = m + 2: seed [-1, 0].
In all cases the seeds satisfy (QS) (so Lemma NW applies) and Theorem SEED-G gives an identity 2p-subword.  []
Corollary (large B).  Together with SEED-B (c6/proof-SEEDB-r3.md) the all-single-letter item-(iii) classes with B >= 2 that are not
excluded by a written uniform argument are contained in {B >= 4, 2B + kB >= p - 1}, plus (p; kB, B) = (11; 5, 3) and the six classes
of Claim E' (both IND* [W+F]; see Sec. 6).

## 6. What remains of item (iii) (class level)

Class level, [F] c6/seedG2.py Part E (out/seedG2_E.txt): every item-(iii) parameter class (k, kappa, B), primes 11..61, with its
label of the c6 map (c6/map6.py 'classify', exec'ed read-only; README Sec. 11: W, SB, IS, IE, OPEN0, OPENE) and the written uniform
exclusions of this file: RA (Propositions RA2, RA3), SA, PA (Corollaries SA, PA with b* = min(B, E + 1); counted only if C+'s class
condition E <= 4, or 2kB <= p and E <= 2(k - kB - 2B) - 1, holds; 'no C+' = in a region but that condition fails).
    p |  OPENE |SA/PA | noC+ | remain ||OPEN0 |  RA |  PA | rem. ||     IE | SA/PA ||   IS | SA/PA/RA
   11 |     24 |    15 |    0 |      9 ||    0 |   0 |   0 |    0 ||     18 |     9 ||   14 |    9
   13 |     47 |    27 |    0 |     20 ||    0 |   0 |   0 |    0 ||     43 |    26 ||   23 |   15
   17 |    137 |    84 |    0 |     53 ||    0 |   0 |   0 |    0 ||    136 |    77 ||   43 |   26
   19 |    210 |   125 |    0 |     85 ||    0 |   0 |   0 |    0 ||    210 |   118 ||   56 |   32
   23 |    438 |   257 |    1 |    181 ||    1 |   0 |   0 |    1 ||    417 |   225 ||   89 |   50
   29 |   1001 |   572 |    6 |    429 ||    4 |   1 |   0 |    3 ||    949 |   487 ||  152 |   84
   31 |   1257 |   713 |    6 |    544 ||    7 |   1 |   0 |    6 ||   1200 |   608 ||  175 |   97
   37 |   2313 |  1292 |   18 |   1021 ||   14 |   3 |   0 |   11 ||   2175 |  1072 ||  258 |  141
   41 |   3269 |  1808 |   31 |   1461 ||   22 |   3 |   0 |   19 ||   3058 |  1489 ||  320 |  177
   43 |   3840 |  2113 |   41 |   1727 ||   27 |   3 |   0 |   24 ||   3570 |  1727 ||  353 |  197
   47 |   5147 |  2810 |   60 |   2337 ||   37 |   3 |   1 |   33 ||   4786 |  2296 ||  425 |  237
   53 |   7669 |  4141 |  104 |   3528 ||   57 |   3 |   1 |   53 ||   7031 |  3330 ||  543 |  307
   59 |  10864 |  5811 |  167 |   5053 ||   84 |   3 |   2 |   79 ||   9926 |  4666 ||  672 |  385
   61 |  12098 |  6457 |  190 |   5641 ||   98 |   3 |   2 |   93 ||  11044 |  5178 ||  714 |  413
For p <= 43 (the map of README Sec. 11): of the 12,536 OPENE classes, 7,006 are excluded by Corollaries SA/PA (written, uniform);
5,530 remain at class level (103 of them inside a region but failing C+'s class condition).  Of the 75 OPEN0 classes, 11 are
excluded by Propositions RA2/RA3; the remaining 64 all have B >= 4.  The regions also contain many classes labelled IE or IS
(previously excluded only by IND* [W+F]); for those the exclusion is now written and uniform as well.
What remains of item (iii) at class level after W-ALL, SEED, SEED-B, IND* and this file:
 (R-a'') all-single-letter, B >= 4, 2B + kB >= p - 1, outside IND*'s class-level check and outside PA (p <= 43: 64 classes;
         p = 61: 93);
 (R-d'') classes with excess outside SA/PA (with C+'s condition) and labelled OPENE (p <= 43: 5,530; p = 61: 5,641).
 Inside these classes, single words are still excluded by Theorem SEED-G whenever their own runs have quality seeds (e.g. from exact,
 non-generic configurations, as in Proposition RA3), by Theorems C/C+ under (H), or by IND* with their own T; none of that is
 counted here.  [I] An exploratory kernel computation (no receipt) intersecting the exact seeds of the configuration types of Lemma CF
 (and of single-letter singles/pairs) over worst-case run-length profiles found quality seeds for all words of 1,005 (+87 without C+)
 of the 1,257 OPENE classes at p = 31; not claimed.
NOT claimed: NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson.

## 7. Exact computations [F] (aids; never hypotheses)

* seedG2.py (supersedes the never-run draft seedG.py), receipts out/seedG2_A.txt ... out/seedG2_M.txt (all .err empty):
  Part A (Lemma SCW-G, case s >= 3): every class with p <= 23 exhaustively (all weights d in [-min(B, E + 1), E + 1], all y', all m <= k/2,
  m' in {m - 1, m}) and 150 random classes for each p = 29, 31, 37, 41, 43 (seed 7007): 58,283,118 instances, both sums >= the largest
  possible targets floor((Delta0 -+ d)/2): 0 failures, minimum slack 2.
  Part B (Lemma P0, Lemma NW, 2-run steps, pin), every class p <= 43 (27,533 classes): 528,214 P0 and NW instances, 14,919,286 two-run
  instances (all weight pairs within the excess and anti-letter budgets, m in {1, 2}, extreme quality seeds intersected with the
  canonical ranges), 484,390 pins: 0 failures (43,824 weight values have an empty extreme seed range, i.e. such runs are excluded
  outright).
  Part C (Propositions RA2, RA3), every prime 11 <= p <= 2000 (RA3 (a): 13 <= p): 299 / 298 / 299 primes, the seed values stated in the
  proofs, availability, (QS), no wrap and (RA2) sum -2 != 0 mod p: 0 failures.
  Part D (Corollaries SA, PA), every class p <= 61 inside the regions (41,587 SA classes, 47,157 PA classes), every weight
  d in [-b*, E + 1] and every y of the family's range (y <= m + E - e_t, resp. 2m + E - e_t): all four arcs generic and (QS): 0 failures.
  Part E: the counts of Sec. 6.
  Part M (mutation controls): M2 (Part D with m - 1 in place of the region's smallest m): 26,944 of 41,587 SA classes and all 47,157
  PA classes fail the generic check (28 also (QS)); M3 (RA configurations with m - 1): 0 of 299 / 298 / 299 primes pass; with m + 1:
  RA2 0, RA3 (a) 0, RA3 (b) 297 pass (m = (p - 3)/2 is also admissible in case (b), as the derivation shows); M4 (SA lower bound weakened
  by 3; 11,633 classes, p <= 43): 7,820 fail the generic check; M1 (Part B with every seed widened by one): 0 failures -- Part B has
  slack, so M1 is not a sensitivity control (the sensitive control of the certification is MUT 1 of the replay below).
* replayG.py (Part 1 only, out/replayG_mut0.txt) and replayG2.py (Part 1 = replayG.py's run, exec'ed read-only, plus Part 2 'deep';
  out/replayG2_mut0.txt ... mut3.txt): explicit words -- RA2 (p = 13, 17, 19, 23), RA3 (kB = p - 6: p = 13, 17, 19; kB = p - 7: p = 11, 13,
  17, 19) with the anti runs in a block / spread / random, and random words with excess (multi-letter aligned and anti runs, (1,1)-pairs)
  of 24 random classes in the SA / PA regions satisfying C+ (p = 17, 19, 23, 29), 3 words per class; for every run the configuration of
  the proof is built explicitly in the word and its four arcs are computed with c5's independent slow_lambda.  MUT 0, Part 1: 105
  words, 4,200 vectors: 1,409 singleton kills, 2,791 seed kills (every RA2 vector is killed before the sum test, as Proposition RA2
  predicts); all configurations exist with the asserted block counts, generic arcs (SA/PA) resp. the stated seed values (RA2/RA3)
  and quality.  Part 2 (93 words, 3,720 vectors inside the seed boxes with sum p): 2,063 pin-chain kills, 1,572 final kills after
  Case A and 85 after Case B of Theorem C+'s procedure.  Every kill re-checked with slow_lambda; 0 failures.  MUT 1 (canonical ranges
  in the certification steps): 716 RA3 deep vectors hit a failing certification step (600 at size 2, 116 at sizes 17-21), so the
  seeds are needed there; no failure for the sampled SA/PA words (their certification also works with canonical ranges).  MUT 2
  (kills re-checked against lambda - 1): 1,356 (Part 1) and 1,688 (Part 2) kills are lost.  MUT 3 (|S| = Delta in Theorem C+'s
  procedure): (M) breaks in all 39 Case B instances.
* Exploratory kernel computations of this cycle without receipts (README Secs. 12-14) are not cited as evidence.
