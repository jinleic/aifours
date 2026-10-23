# Large B: Lemmas RZ, RZ2, RZX (configurations that exist in every word) and Corollaries LB, LBX (computer-assisted class level)

Version r0, written 2026-10-17T19:10:42-0700 in c6/ (task OlsonRunCount5, cycle 6; parent direction 2026-10-17 19:0x: the large-B all-single-letter OPEN0
classes (B >= 4), the seed-failed class (31; 51, 24, 23), (11; 5, 3) and the p = 7 gap).
Status: Lemmas RZ, RZ2, RZX are [W] written proofs (not reviewed).  Corollaries LB and LBX are [W+F]: written implications whose
hypotheses (explicit integer inequalities for one parameter class) are verified class by class by exact arithmetic (c6/seedLB2.py),
i.e. computer-assisted.  They rest on Theorem SEED-G* (c6/proof-SEEDGstar.md, under review), Lemma GS (a) (c6/proof-SEEDG-r2.md),
Lemma C0+ (c6/proof-SEEDG-r2.md), and, for LBX, Lemma PR (c6/proof-SEEDG-cls.md, under review) and Lemma C0W (c6/proof-C0WB.md, under
review).  Paths relative to mixdef-high/.  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson.

## 0. Why new configurations

For large B (2B + kB >= p - 1) the configurations of Lemma CF (aligned runs only) do not give usable seeds: the term y + B - m of U
dominates and the aligned seed tops stay near B.  Configurations that also contain ANTI runs (and many blocks) do: their type (y, m)
can sit where all four arcs are moderate.  The point of this file is that such configurations exist at every run of every word,
whatever the positions of the anti runs.

## 1. Configurations present in every word

Setting of c3/proof-C-r1.md Sec. 0 (any NMH word w with R <= 2p - 3).  For a run t let P_t be the path formed by the k - 3 runs other than
t - 1, t, t + 1 (its two ends are at cyclic distance min(4, k - 4) >= 2, as k >= 7); let alpha, beta be its numbers of aligned and anti
runs (alpha >= n_al - 3, beta >= n_an - 3).  A 'block' is a set of consecutive runs of P_t; blocks are chosen pairwise non-adjacent, so
the union Q has m blocks, no run of Q is adjacent to t, and Q + t has m + 1 blocks; Q and Q + t are proper as 2m + 2 <= k.
**Lemma RZ (mixed singles).**  If i, j >= 0 satisfy 2i <= beta and 2(i + j) <= alpha, there are i anti runs and j aligned runs of P_t,
pairwise non-adjacent.
Proof.  Every other run of each maximal interval of consecutive anti runs of P_t gives ceil(l/2) >= l/2 pairwise non-adjacent anti runs,
>= beta/2 >= i in total (runs of different intervals are separated by a run of another kind); take i of them.  Delete these and their
neighbours: at most 2i aligned runs disappear, so >= alpha - 2i aligned runs remain, and every other run of each maximal interval of
remaining aligned runs gives >= (alpha - 2i)/2 >= j pairwise non-adjacent aligned runs, none adjacent to a chosen anti run.  []
**Lemma RZ2 (aligned singles and pairs).**  Let r be the number of maximal intervals of consecutive aligned runs of P_t (r <= number of
non-aligned runs of P_t + 1 <= n_an + n_pr + 1).  If j1, j2 >= 0 satisfy 3 j2 + 2 j1 <= alpha - r, there are j2 blocks of two adjacent
aligned runs and j1 single aligned runs in P_t, all pairwise non-adjacent.
Proof.  Blocks inside one aligned interval of length l, of sizes s_1, ..., s_q in {1, 2}, fit (separated by single unchosen runs) iff
sum (s_e + 1) <= l + 1; blocks in different intervals are separated by non-aligned runs.  Place the pairs greedily, as many per interval
as fit: this places min(j2, sum floor((l + 1)/3)) pairs, and sum floor((l + 1)/3) >= sum (l - 1)/3 = (alpha - r)/3 >= j2.  The leftover
capacities c = l + 1 - 3(pairs in the interval) satisfy sum c = alpha + r - 3 j2, and the singles that fit are sum floor(c/2) >=
(sum c - r)/2 = (alpha - 3 j2)/2 >= j1.  []
**Lemma RZX (mixed singles, any run lengths).**  In Lemma RZ the chosen runs may have any lengths; then the mass y = D_Q of their union
satisfies j - i - (E - e_t) <= y <= j - i + (E - e_t) (e_t := r_t - 1; the chosen runs carry at most E - e_t excess letters).  []
For all-single-letter words (E = 0): n_al = n = p + kB, n_an = B, n_pr = 0, so Lemma RZ applies with 2i <= B - 3 and 2(i + j) <= n - 3 and
gives type (y, m) = (j - i, i + j); Lemma RZ2 applies with 3 j2 + 2 j1 <= n - B - 4 and gives type (2 j2 + j1, j1 + j2).

## 2. Corollary LB (all-single-letter words, large B)

**Corollary LB** [W+F].  Let (p, kB, B) be an all-single-letter item-(iii) class (k = p + kB + B <= 2p - 3), and suppose that for d = +1
and for d = -1 there is a type (y_d, m_d) of Lemma RZ or of Lemma RZ2 (with the constraints just stated) whose seed s_d :=
[max(lambda({t}), s_lo), min(U({t}), s_hi)] (s_lo = lam(y + d, m + 1) - U(y, m), s_hi = U(y + d, m + 1) - lam(y, m)), for which the no-wrap
condition of Lemma GS (a) holds, is either EMPTY for some d, or satisfies (QS*) for both d, and the two seeds satisfy (P2) and (PIN)
(c6/proof-SEEDGstar.md).  Then no word of the class avoids.
Proof.  Let w be a word of the class and t a run of weight d.  The configuration of type (y_d, m_d) exists at t (Lemma RZ or RZ2), so
by Lemma GS (a) s_d is a seed of t (the same interval for all runs of weight d).  If some s_d is empty, w (which has runs of both kinds)
does not avoid.  Otherwise Theorem SEED-G* applies: if w avoided, its canonical lifts would satisfy (0.2); w has no even aligned run, so
Lemma C0+ under (i) gives a contradiction.  []
Verification [F] (c6/seedLB2.py PART L, out/seedLB2_L.txt): EVERY all-single-letter item-(iii) class with B >= 2 and 2B + kB >= p - 1
for every prime 7 <= p <= 61 (4,184 classes: 3,569 by Lemma RZ types with (QS*) seeds, 608 by Lemma RZ2 types, 7 by an empty seed)
satisfies the hypotheses of Corollary LB.  This includes the two p = 7 classes (kB, B) = (2, 2), (1, 3) (RZ types (y, m) = (3, 3), (2, 2):
aligned singles only), the class (11; 5, 3) (type (5, 5)), all 75 OPEN0 classes of the c6 map with p <= 43 and all 351 with p <= 61,
among them (43; 83, 8, 32) (a Lemma RZ2 class).  Control (PART C, out/seedLB2_C.txt): with Lemma RZ restricted to i = 0 and the RZ2
capacity lowered by 6, 632 of the classes for p <= 61 are no longer covered.

## 3. Corollary LBX (the seed-failed excess class)

**Corollary LBX** [W+F].  No word of the class (p; k, kappa, B) = (31; 51, 24, 23) (kB = 1, E = 8) avoids.
Proof.  For every allowed run-length profile pi (Lemma PR of c6/proof-SEEDG-cls.md) and every weight d of pi, seedLB2.py PART X
(out/seedLB2_X.txt) finds Lemma RZX types (with n_an >= B - min(B, E) - e_an if pairs are present, n_an = B - e_an otherwise, 2i <= n_an - 3,
2(i + j) <= n_al - 3) whose seed, the hull over the mass range of Lemma RZX of the seeds of Lemma GS (a), is EMPTY for a weight that
every word of pi contains (77 of the 157 profiles) or satisfies (QS*), with (P2) and (PIN) for the live weights (80 profiles).  So
every run of every word has a seed as in Theorem SEED-G* (or the word is excluded), and if w avoided its lifts would satisfy (0.2).
B = 23 >= kB + 1 = 2 and 3kB + 1 = 4 <= 31, so Lemma C0W (c6/proof-C0WB.md) gives a contradiction.  []

## 4. What this leaves (class level, with all c6 files, aids only)

* All-single-letter item-(iii) classes: for 7 <= p <= 61 every class is now excluded -- B = 1 by W-ALL/SEED (written), the SEED-B region
  by SEED-B (written), the six Claim E' classes by SA/PA (written), large B with B <= 3 by RA2/RA3 (written, p >= 11/13), and large B
  with B >= 4, the p = 7 classes and (11; 5, 3) by Corollary LB (computer-assisted).  For p > 61 the large-B classes with B >= 4 are not
  covered (no uniform form of Corollary LB is proved).
* Classes with excess: for p <= 31 every OPENE class of the c6 map is now excluded (c6/proof-C0WB.md Sec. 4 and Corollary LBX here); for
  p > 31 those outside SA/PA (and outside IND*'s class check) remain.
* None of this is a proof of RUNS(p) for any p: several links are under review or computer-assisted, and the class-level map itself
  (c6/map6.py) is a finite computation.
