# Theorem SEED-G* (relaxed seed bounds (QS*)) and Corollary X* (computer-assisted class level)

Version r0, written 2026-10-17T18:16:46-0700 in c6/ (task OlsonRunCount5, cycle 6; parent direction 2026-10-17 17:5x: prioritise a written (QS*)).
Status: Lemma LF, Lemma SCW-G*, Lemma QQ and Theorem SEED-G* are [W] written proofs (not reviewed).  Corollary X* is [W+F]: a written
implication whose hypotheses are verified class by class by exact integer arithmetic (c6/seedXstar2.py), i.e. computer-assisted.
Depends on c6/proof-SEEDG-r2.md (sha256 353b0e95...30b7): setting, notation (Delta0, lam, lamc, U, (QS), seeds), Lemmas P0, TS, NW, GS,
SL, the displayed term-sum bounds in the proof of Lemma SCW-G, Lemma C0+, Lemma CF; and, for Corollary X* only, on
c6/proof-SEEDG-cls.md (Lemmas PR, CF', Corollary X; unreviewed).  Paths relative to mixdef-high/.  NOT a proof of NMH(p),
MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson.

## 1. The relaxed bounds

For an integer d with -min(B, E + 1) <= d <= E + 1 put mn := min(d, 0), mx := max(d, 0) and
  L_A(d) := min{ Delta0 + E + 2, Delta0 + E/2 + 1 - mn, (Delta0 + E)/2 + 2, Delta0 + E/2 - mn, Delta0 + E - d + 1,
                 (Delta0 + E - d - mn + 3)/2, (Delta0 + E + 3)/2 - d + mx/2, (R - d)/2 + 1 },
  L_B(d) := min{ Delta0 + E + 2, Delta0 + E/2 + mx, (Delta0 + E)/2 + 2, Delta0 + E/2 + mx + 1, Delta0 + E + d + 1,
                 (Delta0 + E + mx + d + 3)/2, (Delta0 + E + 3)/2 + d - mn/2, (R + d)/2 + 1 }.
These are exactly the lower bounds displayed in the proof of Lemma SCW-G (proof-SEEDG-r2.md Sec. 2, case s >= 3) for the nine (A^s)
term sums U_i + T_j, resp. the nine (B^s) term sums V_i + S_j (U1 + T3 and U3 + T1 share the bound (Delta0 + E)/2 + 2, as do V1 + S3,
V3 + S1).  There they are derived for every (y', m, m') of the domain from (2.1), (F1), (0.1'), (0.2') alone -- (QS) enters only in
the final comparison with the targets.
**Lemma LF (closed forms).**  For d >= 1: L_A(d) = min((Delta0 + E - d + 3)/2, Delta0 + E - d + 1), L_B(d) = (Delta0 + E)/2 + 2.
L_A(0) = L_B(0) = (Delta0 + E + 3)/2.  For d <= -1: L_A(d) = (Delta0 + E)/2 + 2, L_B(d) = min((Delta0 + E + d + 3)/2, Delta0 + E + d + 1).
Proof.  Compare the eight expressions, using Delta0 >= 3 and R - Delta0 - E = 2kappa >= 2 ((0.1')).  d >= 1: Delta0 + E/2 exceeds
(Delta0 + E - d + 3)/2 by (Delta0 + d - 3)/2 > 0, (R - d)/2 + 1 exceeds it by (2kappa - 1)/2, the remaining ones are larger; for L_B,
Delta0 + E/2 + d exceeds (Delta0 + E)/2 + 2 by Delta0/2 + d - 2 > 0, (Delta0 + E + 2d + 3)/2 by d - 1/2, (R + d)/2 + 1 >= (Delta0 + E)/2 + 2
as R - Delta0 - E + d >= 2.  d = 0: Delta0 + E/2 - (Delta0 + E + 3)/2 = (Delta0 - 3)/2 >= 0 and R/2 + 1 >= (Delta0 + E + 3)/2.  d = -b <= -1:
L_A: Delta0 + E/2 + b exceeds (Delta0 + E)/2 + 2 by Delta0/2 + b - 2 > 0 and (Delta0 + E + 2b + 3)/2 by b - 1/2; L_B: Delta0 + E/2 exceeds
(Delta0 + E - b + 3)/2 by (Delta0 + b - 3)/2 > 0 and (R - b)/2 + 1 exceeds it by (2kappa - 1)/2.  []
Consequently L_A(d) >= (Delta0 - d)/2 and L_B(d) >= (Delta0 + d)/2 (proof of Lemma SCW-G), and for |d| <= E + 1 the relaxation is at
least 3/2: e.g. for d >= 1, L_A(d) - (Delta0 - d)/2 = min((E + 3)/2, Delta0/2 + E - d/2 + 1) and L_B(d) - (Delta0 + d)/2 = (E - d)/2 + 2.

## 2. Seeded certification with (QS*)

**Lemma SCW-G*.**  Let w be an NMH word with R <= 2p - 3 that avoids, x its canonical lifts, and let every run t have a seed [a_t, b_t]
(Definition in proof-SEEDG-r2.md Sec. 1) such that
  (QS*)  1 - a_t <= ceil(L_A(d_t))  and  b_t + 1 <= ceil(L_B(d_t));
  (P2)   for every two distinct runs s, t, with m_st := 1 if s, t are adjacent and 2 otherwise:
         a_s + a_t >= 1 - lamc(d_s + d_t, m_st)  and  b_s + b_t <= p + lam(d_s + d_t, m_st) - 1;
  (PIN)  some run a has b_a - lambda({a}) <= p - 1.
Then every proper pattern is certified (Lemma SL with these ranges), and X_[k] = p.
Proof.  Induction on s = |Q| >= 2 as in Lemma SCW-G.  Case s >= 3: the (A^s) sum lam(y', m') + lamc(y, m) is an integer >= each of
the nine displayed bounds for the (A^s) term sums, hence >= ceil(L_A(d)) >= 1 - a_t; likewise the (B^s) sum is >= ceil(L_B(d)) >=
b_t + 1.  Case s = 2: Q = {s', t} has m(Q) = m_(s' t) and D_Q = d_(s') + d_t; (A^s), (B^s) are (P2).  Pin: with the run a of (PIN),
{a}^c is certified and X_[k] lies in [a_a + lambda({a}^c), b_a + p - lambda({a})]; the lower end is >= lambda({a}) + lambda({a}^c) >= 1
(a_a >= lambda({a}), Lemma P0) and the upper end is <= 2p - 1 by (PIN); X_[k] = 0 (mod p) gives X_[k] = p.  []
**Lemma QQ.**  (QS) implies (QS*); seeds satisfying (QS) for every run satisfy (P2) and (PIN).
Proof.  ceil(L_A(d)) >= (Delta0 - d)/2 >= 1 - a_t and ceil(L_B(d)) >= (Delta0 + d)/2 >= b_t + 1 under (QS).  (P2) and (PIN) are what the
proof of Lemma SCW-G derives from (QS) in its case s = 2 and its pin.  []
**Theorem SEED-G*.**  Let w be an NMH word with R <= 2p - 3 (p >= 5 prime) satisfying (i) or (ii+) of Lemma C0+.  Suppose that for every
run t either seeds from actual configurations (Lemma GS (a)) have empty intersection, or t has a seed satisfying (QS*), and that
these seeds satisfy (P2) and (PIN).  Then w has an identity 2p-subword.  (By Lemma QQ this contains Theorem SEED-G.)
Proof.  If w avoids, no run can have seeds with empty intersection; Lemmas SCW-G* and SL give X_Q >= lambda(Q) for all proper Q with
|Q| >= 2, the lifts give the singletons, and X_[k] = p; Lemma C0+ gives a contradiction.  []

## 3. Corollary X* [W+F] (class level, exact seeds)

In the notation of c6/proof-SEEDG-cls.md Sec. 3 (allowed profiles pi, exact seeds sigma_pi(d) from the families S1, P1, SA, PA by
Lemma GS (a)), call a weight d of pi live if sigma_pi(d) is nonempty, and let e(d) be the excess of a run of weight d.
**Corollary X*.**  Suppose that for every allowed profile pi of a parameter class either one of the weights a*, -b* (if b* >= 1),
0 (if n_pr >= 1) has sigma_pi empty, or: every live weight satisfies (QS*); every two live weights d1, d2 (equal or not) with
e(d1) + e(d2) <= E satisfy a1 + a2 >= 1 - lamc(d1 + d2, m) and b1 + b2 <= p + lam(d1 + d2, m) - 1 for m = 1 and m = 2
([a_i, b_i] := sigma_pi(d_i)); and every live weight d satisfies b - lam(d, 1) <= p - 1.  If moreover C+'s class condition holds,
no word of the class avoids.
Proof.  As for Corollary X (c6/proof-SEEDG-cls.md): for a word w with profile pi and a run t of weight d, sigma_pi(d) contains a seed of t
(Lemmas PR, CF, CF', GS (a)); a run whose weight has empty sigma_pi excludes w; otherwise every run has a seed inside sigma_pi(d_t),
so (QS*) holds, (P2) holds for every two runs s != t (their excesses add up to at most E, and m_st is 1 or 2), and (PIN) holds for every
run.  Theorem SEED-G* applies (C+'s class condition gives (i) or (ii+) for every word).  []
Coverage [F] (c6/seedXstar2.py MODE 0, out/seedXstar2_mode0.txt; every item-(iii) class, primes 11..31; OPENE classes of the c6 map):
    p | OPENE | SA/PA |  X   |  X*  | X*,noC+ | fail || OPEN0 | X*
   11 |    24 |    15 |    7 |    2 |     0 |   0 ||   0 |   0
   13 |    47 |    27 |   14 |    5 |     1 |   0 ||   0 |   0
   17 |   137 |    84 |   39 |    5 |     9 |   0 ||   0 |   0
   19 |   210 |   125 |   61 |    7 |    17 |   0 ||   0 |   0
   23 |   438 |   257 |  114 |   21 |    46 |   0 ||   1 |   0
   29 |  1001 |   572 |  232 |   64 |   133 |   0 ||   4 |   1
   31 |  1257 |   713 |  289 |   83 |   171 |   1 ||   7 |   1
(SA/PA = written regions of proof-SEEDG-r2.md; X = additionally by Corollary X; X* = additionally by Corollary X*; X*,noC+ = the
seed and certification hypotheses of X* hold but C+'s class condition fails.)  Totals p <= 31: of 3,114 OPENE classes, 1,793 (SA/PA,
written) + 756 (X) + 187 (X*) are excluded; for 377 more the seed part holds but C+'s class condition fails; 1 class (p = 31) fails the
seed part.  For OPEN0 nothing new (the 2 passing classes are the RA2 classes at p = 29, 31).
So, at p <= 31, the obstacle left for the excess classes is the COUNT condition of Theorem C+ (words with many even aligned runs), not
the certification.
Controls: MODE 1 ((QS) in place of (QS*), p <= 23) reproduces seedX2.py MODE 0 class for class (out/seedXstar2_mode1.txt; the
consistency check is exact); MODE 2 (every exact seed widened by one, p <= 23) changes only IS/IE classes (p = 19: 1, p = 23: 9 more
failures) and no OPENE class -- (QS*) has slack there, so MODE 2 is not a sensitivity control for OPENE.
Superseded (never cited): c6/seedXstar.py and out/seedXstar_mode0..2.txt (its (PIN) test accepted any live weight; the counts coincide).
