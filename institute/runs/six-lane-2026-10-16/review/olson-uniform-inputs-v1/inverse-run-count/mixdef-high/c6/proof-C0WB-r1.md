# Count-free finishers for seeded words: Lemmas C0W and C0B, Theorem SEED-G**

Version r1, written 2026-10-17T20:21:42-0700 in c6/.  New immutable revision after static Codex and Claude reviews (both ACCEPT-WITH-FIXES;
Codex: 0 FATAL/MAJOR, 5 MINOR; Claude: 0 FATAL/MAJOR, 6 MINOR).  The r0 file (SHA ac52d85f...de77) stays unchanged.
Fixes: per-word SA**/PA** restatement with unchanged regions; explicit F3 AND/OR brackets and actual-empty cases discharged before
endpoint use; X** quantifies only non-excluded profiles; Case-B remarks are one-way sufficient obstructions; census ranges begin
at p=11 and finite region instantiations are [W+F]; mutation receipts are accounted separately; source path/review qualifier and
imports corrected.  DF/C0W/C0B proof steps and hypotheses are unchanged.  This version does not incorporate the separately proposed
A0/C0-all strengthening.  Its header supersedes the old status below.
Original r0 provenance: written 2026-10-17T18:59:49-0700 in c6/ (task OlsonRunCount5, cycle 6; parent direction 2026-10-17 18:2x: the count side for words that
have seeds -- the classes whose seed part passes but which fail Theorem C+'s count condition).
Status: Lemmas DF, C0W, C0B, Theorem SEED-G**, Corollary SA**/PA** are [W] written proofs (r0 reviewed with the stated fixes;
r1 fixes not yet independently re-reviewed).  Corollary X** is [W+F]
(hypotheses verified class by class by exact arithmetic, c6/seedXX.py).  [F] receipts are aids only.
Imported (not re-proved): c3/proof-C-r1.md Secs. 0-2 (setting, (0.1), Sec. 1 coordinates and the Kill lemma, identities
(2.1)-(2.3)); c6/c5-fixes/proof-Cplus-r2.md Sec. 2 (Theorem C+: steps (B1+), (B2+)); c6/proof-SEEDG-r2.md (canonical lifts, seeds,
Lemma C0+, Corollaries SA, PA), c6/proof-SEEDGstar-r1.md (review repairs to SCW-G*, SEED-G*, X*), and, for X** only,
c6/proof-SEEDG-cls-r1.md (Corollary X, Lemmas PR/CF').  The frozen star/cls originals received Codex/Claude ACCEPT-WITH-FIXES;
the revised texts preserve those repaired mathematical imports, not the superseded wording.  The argument of Lemma C0W is
that of Lemma W of OlsonParity2 (../../inverse-parity/mixdef-low/c2/proof-Rstar-partial-v2.md Sec. 2, a MIX_low setting with
k <= p), re-proved here in the high-run setting under the hypothesis (0.2) (that file: Codex ACCEPT, Claude ACCEPT-WITH-FIXES, per
OlsonParity2; the Claude review has six MINOR findings in the broader source, but Sec. 2's Lemma W received no fix.  Low-run
Lemma KL/K is not used here).  Paths relative to mixdef-high/.
NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson.

## 0. Setting and the system (0.2)

w is an NMH word with R <= 2p - 3 in the setting of c3/proof-C-r1.md Sec. 0 (all reflection runs odd, k >= p + 1, runs pure or
(1,1)-pairs, 1 <= B <= kappa - 1, B <= A <= 2p - 1, kB = kappa - B >= 1, (0.1) k >= 2kappa + 3, E = R - k, d_t <= E + 1 <= p - 3).  We
consider integers x_t (one per run) with
   sum_t x_t = p   and   X_Q >= lambda(Q) for every proper pattern Q (singletons included).                     (0.2)
Notation of c3 Sec. 1: c_t := d_t - x_t, bh_t := 2x_t - d_t (so x_t = bh_t + c_t), Phi(Q) := c(Q) + m(Q); Z := {t : bh_t <= 0} (the
defects); Kill lemma: for a proper Q, X_Q < lambda(Q) iff (M) Phi(Q) >= kB + 1, (Fl) bh(Q) <= B and (P) X_Q + m(Q) <= p.  If w avoids
and its seeds satisfy the certification hypotheses, its canonical lifts satisfy (0.2) by the PROOF of SEED-G* or SEED-G,
stopped before the final appeal to C0+, and in addition
x_t >= a_t for the seeds [a_t, b_t].  Theorems C, C+ show that (0.2) is infeasible under a count condition on n_ev,al; Lemmas C0W, C0B
below need no condition on n_ev,al.

**Lemma DF (small c on light runs).**  Let x satisfy (0.2) and let t be a run with bh_t <= 1.  Then c_t <= kB - 1.
Proof.  bh_t <= 1 gives x_t <= (d_t + 1)/2 < floor((d_t + B)/2) + 1 (B >= 1) and x_t <= (E + 2)/2 < p.  As x_t >= lambda({t}) =
min(p, d_t + 1 - kB, floor((d_t + B)/2) + 1) and x_t is below the first and third terms, x_t >= d_t + 1 - kB, i.e. c_t <= kB - 1.  []

## 1. Lemma C0W (the case B >= kB + 1)

**Lemma C0W.**  If B >= kB + 1 and 3kB + 1 <= p, the system (0.2) has no integer solution.
Proof.  Suppose x satisfies (0.2).  Call a run cheap if c_t >= 0 and bh_t <= 1, and put w_t := c_t + 1, W(P) := sum_(t in P) w_t.
(1) Every cheap run has 1 <= w_t <= kB (Lemma DF).
(2) sum_t w_t = sum_t c_t + k = (D - p) + k = p + 2kB (D = 2p - k + 2kB).  A run that is not cheap and has c_t >= 0 has bh_t >= 2, hence
    d_t = bh_t + 2c_t >= 2 and it is aligned, with w_t = (d_t - bh_t)/2 + 1 <= d_t/2; runs with c_t <= -1 have w_t <= 0.  So
    W(cheap) >= p + 2kB - (sum of d_t over aligned runs)/2 >= p + 2kB - A/2 >= p + 2kB - (2p - 1)/2 = 2kB + 1/2, hence W(cheap) >= 2kB + 1.
(3) There is a set U of pairwise non-adjacent cheap runs with W(U) >= kB + 1.  If some run is not cheap, the cheap runs form paths
    separated by non-cheap runs; in each path take the class of every other run (one of its two parity classes) of larger weight; the
    union U is pairwise non-adjacent and W(U) >= W(cheap)/2 > kB.  If every run is cheap, W(cheap) = p + 2kB; delete one run t0
    (w_(t0) <= kB) and take the heavier parity class U of the path [k] - {t0}; its two possible ends t0 + 1, t0 - 1 are not adjacent
    (k >= 4), so U is pairwise non-adjacent, and W(U) >= (p + kB)/2 >= kB + 1 (p >= kB + 2).
(4) Order U by decreasing weight and let S be its shortest prefix with W(S) >= kB + 1; all weights are >= 1, so |S| <= kB + 1.  List S
    with the runs of bh <= 0 first and the others (bh = 1) after them, and let P be the shortest prefix of this list with W(P) >= kB + 1.
    P is pairwise non-adjacent, so m(P) = |P| and Phi(P) = c(P) + |P| = W(P); adding a run raises W by at most kB, so
    kB + 1 <= Phi(P) <= 2kB.  bh(P) <= (number of runs of P with bh = 1) <= |P| <= kB + 1 <= B (if P contains a run with bh = 1, it
    contains all runs of S with bh <= 0).  X_P + m(P) = sum_P (bh_t + c_t + 1) = bh(P) + Phi(P) <= (kB + 1) + 2kB <= p.
    P is nonempty and proper (pairwise non-adjacent, k >= 4).  So P satisfies (M), (Fl), (P): X_P < lambda(P), contradicting (0.2).  []

## 2. Lemma C0B (the case k >= kB + 3B)

**Lemma C0B.**  Suppose k >= kB + 3B and (A*): every run t with bh_t <= 0 has c_t <= p - kB - 1.  Then the system (0.2) has no integer
solution x (with (A*) read for that x).  (A*) holds for every solution if 2kB <= p (Lemma DF: c_t <= kB - 1 <= p - kB - 1), and it holds
if the lifts lie in seeds [a_t, b_t] with min(kB - 1, d_t - a_t) <= p - kB - 1 for every run, in particular for seeds with (QS) of
proof-SEEDG-r2.md: d_t - a_t <= (d_t + Delta0)/2 - 1 <= (2p - k - 1)/2 <= p - kB - 1 (d_t <= E + 1, Delta0 + E = 2p - k, k >= 2kB + 1).
Proof.  Suppose x satisfies (0.2); use c3 Sec. 1 and the case split of the proof of Theorem C+.
Case A (Phi(Z) >= kB + 1): step (A-ii) of c3/proof-C-r1.md with its bound c_t + 1 <= p - kB replaced by (A*): if Phi(Z) <= p let Q := Z;
otherwise delete from Z, one at a time, a run with at most one neighbour in the current set; Phi drops by at most c_t + 1 <= p - kB per
step and reaches 0, so the first member Q with Phi(Q) <= p has Phi(Q) >= kB + 1.  (Fl) holds (Q is contained in Z), and (P):
X_Q + m(Q) <= c(Q) + m(Q) = Phi(Q) <= p (x_t <= c_t on defects).  Contradiction.
Case B (Phi(Z) <= kB, Delta := kB - Phi(Z) >= 0).  By (2.2) of c3, Delta = -f(Z) - m(Z) - n_ev/2 - sur with m(Z) >= 1 and sur >= 0, so
   n_ev/2 <= -f(Z) - 1.
Aligned runs have f_t >= 0, pairs f_t = -1 and anti runs f_t = -ceil((b_t + 1)/2); hence
   -f(Z) <= n_pr + sum_anti ceil((b_t + 1)/2) = n_pr + (B - n_pr + n_an + n_ev,an)/2
(ceil((b + 1)/2) = (b + 1 + [b even])/2, sum_anti b_t = B - n_pr).  With n_ev = n_pr + n_ev,an + n_ev,al this gives
   n_ev,al <= B + n_an - 2,  and, as n_an <= B - n_pr,   s0 := (k - kB - 2B) + (n_pr - n_ev,al)/2 >= k - kB - 3B + 1 + n_pr >= 1.
So step (B1+) of c6/c5-fixes/proof-Cplus-r2.md (whose count |X_o| >= 2 Delta + s0 uses no hypothesis on n_ev,al) gives
|X_o| >= 2 Delta + 1, and step (B2+) (which uses no hypothesis on n_ev,al) produces a proper Q with (M), (Fl), (P): contradiction.  []
Remark.  Case B gives the one-way bound n_ev,al<=B+n_an-2.  If n_ev,al=E, it requires E<=B+n_an-2; the equality n_ev,al=E is not
ruled out in general.  Under k>=kB+3B, words violating (ii+) through its n_ev,al clause form a sufficient family for which this
bound excludes Case B.  No converse or exact characterization is claimed.

## 3. Theorem SEED-G** and the uniform corollaries

**Theorem SEED-G-double-star.**  Let w be an NMH word with R<=2p-3, p>=5 prime.  If seeds from actual configurations of some run
have empty intersection, w has an identity 2p-subword immediately.  Otherwise suppose every run has a nonempty seed [a_t,b_t]
satisfying (QS*) and (P2) of proof-SEEDGstar-r1.md (quality seeds suffice by Lemma QQ), and suppose one of
 (F1) (i) or (ii+) of Lemma C0+;
 (F2) B>=kB+1 AND 3kB+1<=p;
 (F3) k>=kB+3B AND [2kB<=p OR (for EVERY run t, min(kB-1,d_t-a_t)<=p-kB-1)].
Then w has an identity 2p-subword.  The old explicit (PIN) check is automatic for canonical-contained seeds by P0 (see star-r1).
Proof.  The actual-empty case is already excluded.  Otherwise, if w avoids, the proof of SEED-G* (or SEED-G), stopped BEFORE C0+,
gives (0.2) for its canonical lifts, and the seed property gives x_t>=a_t.  Apply C0+, C0W or C0B according to F1/F2/F3.  []
**Corollary SA-double-star/PA-double-star (per word).**  Let w satisfy the parameter-region hypotheses of Corollary SA or PA of
proof-SEEDG-r2.md, with every region inequality, b* and m UNCHANGED.  Its configurations establish quality seeds or actual-empty
intersections.  Moreover w has an identity 2p-subword if [C0+'s (i) or (ii+)] OR [B>=kB+1 AND 3kB+1<=p] OR [k>=kB+3B].
In particular this holds for EVERY word of a region class satisfying [E<=4] OR [2kB<=p AND E<=2(k-kB-2B)-1] OR
[B>=kB+1 AND 3kB+1<=p] OR [k>=kB+3B].  These are sufficient CLASS conditions; the per-word (i)/(ii+) need not require them.
Proof.  Actual empty intersections exclude w first.  Otherwise quality seeds make F3's defect bound automatic, and the preceding
theorem supplies each listed finisher.  No SA/PA region, availability condition or NMH hypothesis is changed.  []
**Corollary X-double-star [W+F].**  In the class implications X/X* (proof-SEEDG-cls-r1.md, proof-SEEDGstar-r1.md), retain every
seed/profile hypothesis, and use the class finisher
 [C+'s class sufficient condition] OR [F2] OR [k>=kB+3B AND (2kB<=p OR A-profile)],
where A-profile means: for every allowed profile pi NOT already excluded by a configuration-derived empty sigma_pi at a guaranteed
occurring weight (a*, -b* if b*>=1, or 0 if pairs are present), and every live weight d of that profile,
 min(kB-1,d-a_pi(d))<=p-kB-1,  sigma_pi(d)=[a_pi(d),b_pi(d)].
Proof.  Dispatch excluded profiles before endpoint use.  Otherwise actual seeds are contained in sigma_pi, hence have lower endpoint
at least a_pi(d), so the defect bound transfers monotonically.  The preceding theorem applies; this quantifier order matches
seedXX.py's seed_part()/finisher(), including vacuous A-profile when every profile is already excluded.  []

## 4. Effect [F] (c6/seedXX.py; out/seedXX_*.txt)

* Finite region instantiation [W+F] of the WRITTEN per-word implication, c6/seedXX.py PART R (out/seedXX_R.txt), every item-(iii) class with 11 <= p <= 61 inside the region SA or PA of
  proof-SEEDG-r2.md: every such class is now finished by a class condition -- OPENE: 26,225 by C+'s condition, 22 by (F2), 602 by (F3)
  (IE: 21,308 / 0 / 5,062; IS, OPEN0, SB, W: C+ only); no region class is left under these finite checks.  Thus the computer-assisted application excludes every word of each
  instantiated region class for 11 <= p <= 61 (proof-SEEDG-r2.md Sec. 6 had listed 103 such OPENE classes for 11 <= p <= 43, and 190 at p = 61, as failing C+).
* Class level with exact seeds ([W+F], Corollary X**), PART X (out/seedXX_X.txt), every item-(iii) class, 11 <= p <= 31:
    p | OPENE |  C+   |  F2  | F3  | F3* | seed-fail || OPEN0 | C+ | seed-fail
   11 |    24 |    24 |    0 |   0 |   0 |   0 ||   0 |   0 |   0
   13 |    47 |    46 |    1 |   0 |   0 |   0 ||   0 |   0 |   0
   17 |   137 |   128 |    9 |   0 |   0 |   0 ||   0 |   0 |   0
   19 |   210 |   193 |   17 |   0 |   0 |   0 ||   0 |   0 |   0
   23 |   438 |   392 |   43 |   2 |   1 |   0 ||   1 |   0 |   1
   29 |  1001 |   868 |  119 |   7 |   7 |   0 ||   4 |   1 |   3
   31 |  1257 |  1085 |  154 |  10 |   7 |   1 ||   7 |   1 |   6
  ('C+' = seed part of Corollary X* and C+'s class condition, i.e. the written SA/PA regions plus Corollaries X, X*; F2, F3, F3* = the
  count-free finishers, F3* using the seed form of (A*)).  Of the 3,114 OPENE classes with 11 <= p <= 31, 3,113 are excluded; the one left
  is (p; k, kappa, B) = (31; 51, 24, 23) (kB = 1, E = 8), whose seed part fails (kernel identification after the receipt; large B).
  The 15 classes with 2kB > p of the parent's split are exactly the F3* classes.  OPEN0 (all-single-letter, large B): only the RA2
  classes (p = 29, 31); the other 10 fail the seed part, as before.
* Ablations, PART A (out/seedXX_A.txt), 11 <= p <= 23: without (F2), 56 OPENE classes are not finished; without (F3), 3; without the seed
  form of (A*), 1.
* Literal replay (replayW.py; out/replayW_mut0..3.txt): C0W on random words of 24 classes with B >= kB + 1 and 3kB + 1 <= p
  (p = 17, 19, 23, 29; many even aligned runs), vectors with sum p inside the singleton windows: 1,320 C0W constructions, all with
  (M), (Fl), (P) and X_P < lambda(P) (slow_lambda); C0B (c5's Theorem C+ procedure, whose '(B1+)' count assertion Lemma C0B proves
  without the n_ev,al hypothesis) on words violating C+'s count: 360 kills, all in Case A; 0 failures.  MUT 1 (target kB): (M) breaks
  in 1,151 of 1,440 constructions; MUT 3 (kill re-check against lambda - 1): 622 C0W and 19 C0B kills lost; MUT 2 (classes with
  3kB + 1 > p): no (P) failure observed (the bound 3kB + 1 <= p is sufficient, not shown tight).  Mutation runs draw their own
  words: MUT0 has 1,320 C0W + 360 C0B vectors; MUT1 has 1,440 C0W and NO C0B replay; MUT3 has 1,440 C0W + 420 C0B vectors.  Counts
  are stated per receipt, not generalized between modes.
* Case-B-biased replay (replayW2.py; out/replayW2_mut0..1.txt): 27 and 29 words, 1,080 and 1,160 vectors respectively: every instance
  is a Case-A kill, with ZERO Case-B instances.  These sampled words were generated with 2kB<=p and violate (ii+) through its n_ev,al
  clause.  Under k>=kB+3B this is a SUFFICIENT family for which the written bound n_ev,al<=B+n_an-2 excludes Case B; no converse is
  proved.  The receipts empirically check Case A only.  Case B rests on the written proof, not on a zero-instance replay.  MUT1 loses
  no kill in replayW2 (the sampled Case-A kills have slack).
* Deviation: the kernel identification of the remaining class (a seed computation, about 1 minute) overlapped with the replayW2 run,
  so for about one minute two busy processes ran for this slice.


For p=5,7 the region corollary itself still applies as written: E<=p-4 and E even imply E<=2, so C0+'s case(i) is automatic.
The cited R/X/A censuses did not compute those primes.  Missing p=7 seeds outside SA/PA, and (11;5,3), are not supplied by a finisher
alone; later construction files are separate results, not consequences of this historical census.  The arbitrary-p floating bounds
issue in the frozen seedXstar2.py does not affect its p<=31 use by seedXX.py.  Future computations use seedXstar3.py's doubled integers
and source hashes; old receipts are not retroactively assigned those hashes.
