# MIX_DEF_HIGH cycle 3 (task OlsonRunCount3): item (iii) of ../proof-MH.md Sec. 6

Directory created 2026-10-17T11:43:44-0700 (host clock, `date`).  This README is FROZEN before any
substantive computation of the cycle: its SHA-256 and the host time are appended to out/freeze.txt
right after it is written.  Later sections are appended with host-clock times and are written before
the computations they describe.  Only this directory (c3/) is written; everything else is read-only
(c2/, ../, ../../, ../../../inverse-parity/, the parent review directory).  Files are created with
mode "x" (never overwritten); README.md and out/freeze.txt are only appended to.
Safety: <= 4 CPU workers, <= 8 GiB, <= 10 GiB new data; native time limits or `timeout -s TERM`
only (no SIGKILL, no Popen.kill(), no subprocess timeouts); an interrupted computation is UNKNOWN.
Labels: [W] written proof (unreviewed), [F] exact computation (aid only, never a hypothesis),
[I] inference/conjecture.

## 1. Target (quantifiers unchanged)

NMH(p) (../README.md Sec. 1): every all-odd RGR word w of length 4p-2 (p >= 5 prime) with
p+1 <= k <= 2p-2 rotation runs, every run pure or a (1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p-1,
has an identity 2p-subword.  Proved before this cycle ([W]): R >= 2p-2 (c2/proof-C2.md Theorem FW+),
and k = p+1, kB = 1 with (4.1) (../proof-MH.md Lemma ZSI-B), and the single family W(p, 4), p >= 11
(c2/proof-W4.md).  ITEM (iii) := the NMH words with R <= 2p-3 outside the ZSI-B case.  This cycle
attacks item (iii); every result states the exact sub-family it covers.  NMH(p), MIX_DEF_HIGH(p),
RUNS(p), INV and ordered Olson for D_{2p} are NOT claimed unless every piece is proved.

Parameters: kB := kappa - B >= 1, D := A - B = 2p - k + 2kB, R = A + B = 2p - k + 2kappa,
R <= 2p-3 <=> 2kappa <= k - 3; all runs have r_t >= 1, so k - p <= kappa <= (k-3)/2, total excess
R - k = 2(kappa - k + p); all-singleton words (R = k) are exactly kappa = k - p.
W(p, kB) (c2/proof-NOBC.md Sec. 1): k = p + 1 + kB single-letter runs, exactly one anti run, B = 1.

## 2. Representation (imported, not re-proved here)

Lemma H (../../../inverse-parity/proof-PAR-K0.md Sec. 1, with its 07:39 correction): for an all-odd
word and a proper pattern Q (m = m(Q) blocks, D_Q = sum_{t in Q} d_t),
   lambda(Q) = min(p - m + 1, D_Q + m - kB, floor((D_Q + B)/2) + 1),
and w avoids iff u_Q notin [1 - lambda(Q^c), lambda(Q) - 1] (mod p) for every proper Q and the empty
pattern does not kill (in NMH it never kills: A, B <= 2p-1 and B <= kappa - 1).
Lemma L, Lemma CORE (c2/proof-NOLP.md Sec. 1): singleton-extension certification; for an avoider and
singleton lifts x_t in [lambda({t}), p - lambda({t}^c)], every certified Q has
X_Q := sum_{t in Q} x_t in [lambda(Q), p - lambda(Q^c)].
c-coordinates (exact algebra, to be written out in the proofs): c_t := d_t - x_t, c(Q) := D_Q - X_Q;
lambda(Q) = D_Q - gamma(Q) with
   gamma(Q) := max(kB - m(Q), ceil((D_Q - B)/2) - 1, D_Q + m(Q) - p - 1),
so X_Q >= lambda(Q) <=> c(Q) <= gamma(Q).  If the total is pinned (X_[k] = p), sum_t c_t = D - p.
Defect (lifted bracket bh_t = 2x_t - d_t <= 0): c_t >= ceil(d_t/2); non-defect: c_t <= floor((d_t-1)/2).

## 3. Attack plan (frozen)

P1 [F, before proofs] (a) certification census: for W(p, kB), all 1 <= kB <= p - 4, and for general
item-(iii) words (p = 5, 7 all; p = 11, 13 samples), which patterns are certified by singleton
extension (subset DP over ALL patterns where 2^k allows, type-level check otherwise), and whether an
interval chain certifies a pattern Q0 with certified complement and lambda(Q0) + lambda(Q0^c) >= 1
(this pins X_[k] = p).  (b) integer feasibility (z3) of the small-pattern systems
{sum x = p, X_Q >= lambda(Q) for certified Q with |Q| <= s or |Q| >= k - s} for W(p, kB), several
(p, kB, s).  (c) a defect-set kill rule (candidate, to be stated in an appended section BEFORE its
test): Q = Z (all defects), a bounded subset of Z, or Z plus isolated non-defect aligned runs with
c_t = floor((d_t - 1)/2); test it on every integer point found in (b) and on random lift vectors.
P2 [W] written proofs, smallest family first: W(p, kB) for every kB in the range where P1 shows the
needed certification (target: all 1 <= kB <= p - 4, at least 4 <= kB < (p+6)/4); then all-singleton
words with B >= 2 anti runs; then runs with excess (a_t >= 2, b_t >= 2, (1,1)-pairs); reductions to
the single-letter case by merge/monotonicity lemmas where possible.  Every proof lists its scope,
hypotheses and imported lemmas, and is frozen (hash + host time) in out/freeze.txt.
P3 [F] map of item (iii): exhaustive at p = 5, 7 (all item-(iii) words, rotation classes x all
pure/(1,1) splits, as enumerated by ../mhc.cpp / c2/rrchain.cpp), samples at p = 11, 13: each word
labelled by the first proved result whose hypotheses it satisfies; the unlabelled remainder must be
exactly the sub-family declared open.
Controls (required): an independent Python re-implementation of the certification DP and of lambda
(cross-check against the C++ tool); mutation controls (lambda shifted by +-1 must change verdicts in
the expected direction); every kill re-checked by the raw Lemma H window test; any claimed avoider is
only a candidate until replayed by a raw ordered-product DP (../../../code/was_verify.py or ../../hw.py).
Answers to reviews of c2 files go into new versioned files here (c2 stays frozen).

## 4. Candidate theorem W-ALL and its kill rule (appended 2026-10-17T12:2x PDT -- exact time in out/freeze.txt; written BEFORE the tests below)

Exploration so far (not yet saved as receipts; to be reproduced by saved code before use): cert.cpp on
W(11, kB): every proper pattern is certified for kB <= 5, and NO pair is certified for kB = 6, 7 (the
first step {0} -> {0, s} fails condition (A)); a type-level check suggests the singleton-extension
certification of all patterns with <= kB + 1 runs and of the interval chain holds iff 3kB <= p + 4.
c2/famdfs: no avoider in W(11, 5..7), W(13, 6..9).

Candidate (to be proved in proof-WALL.md and tested first): Theorem W-ALL: for every prime p >= 5 and
1 <= kB <= min(p - 4, (p + 4)/3), no word of W(p, kB) is an avoider.
Certification lemma (candidate): if 3kB <= p + 4, every pattern with <= kB + 1 runs is certified
(order: the anti run first, then aligned runs, each new aligned run an end of a block or a new
singleton block), and so is the interval chain I_1 c ... c I_{p+kB} (I_i = {1..i}); the pair {0}, I_{p+kB}
pins X_[k] = p.
Kill rule KW-ALL (given integer lifts x with sum p; c_t := d_t - x_t, so sum c = kB - 1):
 Z_al := {aligned t : x_t <= 0}, Z := Z_al u ({0} if x_0 <= -1).
 (1) if |Z_al| >= kB: output any kB elements of Z_al;
 (2) else if c(Z) + m(Z) >= kB + 1: output Z;
 (3) else (then 0 in Z, Z is one cyclic interval, all aligned runs outside Z have x = 1): output
     Z u {s} for an aligned s outside Z adjacent to no run of Z.
Claim: the output Q has |Q| <= kB + 1 and X_Q < lambda(Q) (a kill).
Tests (wkill.py, frozen before running): for (p, kB) with 3kB <= p + 4, p in {11, 13, 17, 19, 23}:
integer lift vectors x with sum p satisfying the singleton bounds and ALL pair and triple constraints
(found by a randomized DFS; plus uniformly random singleton-feasible x), apply KW-ALL, re-check the kill
with an independent lambda routine, and check every intermediate claim (sum c, c(Z) >= kB - [0 in Z],
step (3) structure).  cert.cpp re-run (saved) at p = 11, 13, 17 for all kB <= p - 4 with k <= 26.

Correction (2026-10-17T11:58:25-0700): the heading of Sec. 4 says "12:2x PDT"; that label was a placeholder, not a clock read.  Sec. 4 was
appended at 2026-10-17T11:58:10-0700 (out/freeze.txt).  All later labels are copied from `date`.

## 5. Census results, protocol note, and the general rule RS (appended 2026-10-17T12:06:52-0700, before the RS test)

Protocol note on Sec. 4: wkill.py as written and run uses the singleton bounds and ALL PAIR constraints
(lower and upper), not triples (with triples the integer system is already infeasible for kB = 4, c2
intsmall.py, so nothing would be left to test); wkill2.py additionally restricts the DFS to
|Z_al| <= kB - 1 so that steps (2), (3) of KW-ALL are exercised.  Results (stdout, to be re-run with saved
receipts): 0 failures in every case run; step (3) occurs at (p, kB) = (11, 1), (11, 3), (13, 3), (13, 4).

[F] census3.cpp (out/census3_p5.txt, out/census3_p7.txt exhaustive; out/census3_p11.txt, 3,000 random words,
seed 1101, k = 12..19; out/census3_p13.txt, 500 random words, seed 1301, k = 14..22): EVERY item-(iii) word
at p = 5 (28 words; all are W(5, 1)) and at p = 7 (51,641 words incl. 11,590 ZSI-B) has ALL proper patterns
certified by singleton extension and a pin pattern; p = 11: 2,835 / 3,000 (kB <= 4: all but 25; none with
kB >= 6); p = 13: 456 / 500 (all with kB <= 4, 54/56 at kB = 5, 16/26 at kB = 6, none at kB >= 7).
Failures: high kB (singleton extension fails already for pairs) and some words with large B relative to p
(condition (B) fails through the middle term of lambda({t}^c)).

Candidate Theorem C (to be proved in proof-C.md if the test below shows no failure): every item-(iii)
word whose proper patterns are ALL certified and which has a pin pattern has an identity 2p-subword.
(By Lemma CORE such a word avoids iff the integer lambda-core with total p is nonempty.)
Rule RS (given integer lifts x with sum p; bh_t := 2x_t - d_t; Kill(Q) <=> bh(Q) <= B and
D_Q - bh(Q) + 2m(Q) >= 2kB + 2 and X_Q <= p - m(Q), i.e. X_Q < lambda(Q)):
 (1) Z := {t : bh_t <= 0}; if Kill(Z), output Z.
 (2) Else search a set S of runs u notin Z, adjacent to no run of Z, pairwise non-adjacent, such that
     Kill(Z u S) (exact DFS over such S; preference order: larger gain c_u + 1 = (d_u - bh_u)/2 + 1).
 (3) Else FAIL (record the word and x).
Test rstest.cpp: every all-certified item-(iii) word at p = 7 (exhaustive) and random ones at p = 11, 13;
hard lift vectors = integer x with sum p satisfying every singleton, pair, co-singleton and co-pair
constraint (randomized DFS, up to N per word); each output kill re-checked with lambda computed directly.
A FAIL refutes rule RS only, not Theorem C or NMH.

## 6. Log (appended 2026-10-17T12:22:00-0700)

* proof-WALL.md written (Theorem W-ALL: no word of W(p, kB) is an avoider for 1 <= kB <= min(p - 4, (p + 4)/3);
  Lemma CW: singleton-extension certification of all patterns with <= kB + 1 runs and of the interval chain iff
  3kB <= p + 4 on the type level).  Receipts: out/cw_check.txt (type-level replay, primes 5..199, 4,046 (p, kB)
  cases, 0 mismatches with 3kB <= p + 4), out/cert_W.txt (exact DP: all patterns certified for W(11, <=5),
  W(13, <=5), W(17, <=7); not for W(11, 6..7), W(13, 6..9), W(17, 8)), out/wkill.txt, out/wkill2.txt (0 failures),
  out/famdfs_W_high.txt (c2/famdfs, sha256 of source e579c31b... = c2 freeze: no avoider in W(11, 5..7),
  W(13, 6..9)).  Frozen now (hashes below in out/freeze.txt).
* Rule RS tests (README Sec. 5): out/rstest_p7.txt (all 51,641 item-(iii) words at p = 7 are all-certified; 51,245
  have no integer lift vector satisfying the singleton and pair constraints; the other 396 words: 1,056 vectors, all
  killed, 462 by Z, 594 by Z u S with |S| <= 2), out/rstest_p11.txt (2,832 all-certified of 3,000 random words;
  24,932 vectors, 0 failures, |S| <= 3), out/rstest_p13.txt (363 of 400; 4,023 vectors, 0 failures).  rstest2.cpp
  (instrumented copy): no pattern in the RS search ever satisfied (M) and (Fl) but not (P) (out/rstest2_*.txt).
* Safety note: four wkill2.py runs (p = 17 kB = 4, 5; p = 19 kB = 6; p = 23 kB = 8) were stopped by SIGTERM from
  this agent at about 12:10 PDT (a DFS restart loop without progress; results UNKNOWN, not used); one of them was
  running past its own `timeout -s TERM 600` wrapper's expected end only because the harness launched it later.
  No SIGKILL was used.  The saved wkill2 receipt (out/wkill2.txt) contains only cases that finished.
* Next: written proof of the all-singleton case for every B under the Lemma CORE hypothesis (Theorem S), then the
  general run structures (Theorem C), then the map (Sec. 3 P3).

Correction (2026-10-17T12:23:12-0700) to Sec. 6, safety note: the SIGTERMs were sent by a command that finished just before the host clock
read 2026-10-17T12:12:22-0700 (not 'about 12:10', which was not a clock read), and the sentence about a run 'past its own
timeout' is withdrawn: the observed run (pid 28418) had elapsed 8:54 < 600 s when it was terminated.

## 7. Candidate Theorem C (general run structures) and its replay test (appended 2026-10-17T12:29:57-0700, before the test)

Notation: n_ev,al := number of aligned runs of even length.  (H) := every proper pattern is certified by
singleton extension and some certified Q0 with certified complement has lambda(Q0) + lambda(Q0^c) >= 1
(the hypothesis of Lemma CORE; phi-independent, decidable per run datum).
Candidate Theorem C: every item-(iii) word (in fact every NMH word with R <= 2p-3) satisfying (H) and
   n_ev,al <= 4,   or   2kB <= p and n_ev,al <= 2kB + 2,
has an identity 2p-subword.  Corollary S: every all-singleton item-(iii) word (any B) satisfying (H).
Proof plan (bh_t = 2x_t - d_t, Z = {bh <= 0}, Phi(Q) = c(Q) + m(Q), Kill(Q) <=> Phi(Q) >= kB + 1 and
bh(Q) <= B and X_Q + m(Q) <= p):
 Case A (Phi(Z) >= kB + 1): Kill(Z) if n_ev,al <= 4 (then X_Z + m(Z) <= p automatically); if 2kB <= p,
   remove block ends of Z one at a time; the first pattern with Phi <= p has Phi >= kB + 1 (steps <= p - kB
   since c_t <= gamma({t}) <= p - kB - 1) and X_Q + m(Q) <= Phi(Q) (x_t <= c_t on defects).
 Case B (Delta := kB - Phi(Z) >= 0): S := Delta + 1 pairwise non-adjacent aligned runs of ODD length with
   bh = 1, outside Z and not adjacent to Z (exist: |X_o| >= 2 Delta + 2 + (kB + 1) - n_ev,al/2 - 1); Kill(Z u S):
   Phi >= kB + 1, bh(Z u S) <= B by bh(Z) = |Z| - 2kB - s and |Z| - D_Z <= B + n_an(Z), and
   X + m <= p - 2 - B/2 by the excess bound.
Replay test thmC.cpp (all item-(iii) words with (H) at p = 7 exhaustive, random at p = 11, 13; hard lift vectors
as in rstest.cpp): follow the proof literally for every vector, assert every intermediate inequality (sum
identities, Delta bounds, |X| and |X_o| lower bounds, (Fl) and (P) bounds) and the final window violation
X_Q < lambda(Q); count hypotheses per word.  A failed assertion refutes the written argument (not NMH).

## 8. Theorem C replay results and the map protocol (appended 2026-10-17T12:37:20-0700, before running map3)

Replay of the Sec. 7 argument (thmC.cpp, thmC2.cpp): 0 failures at p = 7 (all 51,641 words, 1,202,586 vectors),
p = 11 (2,807 words, 99,255 vectors), p = 13 (370 words, 14,517 vectors); mutation controls (thmC_mut.cpp) fail as
they must (|S| = Delta: all 288,545 Case B instances lose (M); windows shrunk by one: 962,485 kills lost).  Written
up as proof-C-r1.md (Theorem C, Corollary S).  proof-C.md is an UNFROZEN draft superseded by proof-C-r1.md (scope
sentence and Remark (3) corrected; same mathematics); it is kept (no deletion) and never cited.
Map protocol (map3.cpp): every NMH word with R <= 2p - 3 generated as in census3.cpp (p = 5, 7 exhaustive; p = 11, 13
random), ZSI-B words reported separately; label WALL (all runs single letters, B = 1, 3kB <= p + 4: proof-WALL.md,
no computation), C ((H) verified by the exact DP and the n_ev,al condition: proof-C-r1.md), open otherwise, with the
reason (some pattern uncertified / no pin / n_ev,al condition).  Cross-check: hcheck.py, an independent Python
implementation of lambda, of the singleton-extension certification DP and of the pin test, on the words dumped by
map3 (first DUMP words of each run), must reproduce the (H) verdicts; mutation control: hcheck.py with lambda shifted
by -1 in condition (B) must change some verdicts.

## 9. MAP of item (iii) after cycle 3 (appended 2026-10-17T12:41:11-0700)

Item (iii) := NMH words (all-odd, p+1 <= k <= 2p-2, runs pure or (1,1), 1 <= B <= kappa-1, B <= A <= 2p-1) with
R <= 2p-3, outside the ZSI-B case (k = p+1, kB = 1, (4.1)).  After this cycle it splits as follows.

CLOSED, by written proofs ([W], unreviewed):
 (C1) W(p, kB) = all-singleton words with B = 1 (exactly one anti run), for every prime p >= 5 and every
      1 <= kB <= min(p - 4, (p + 4)/3) -- Theorem W-ALL (proof-WALL.md).  No computation and no extra hypothesis.
      Includes Theorem W4 (kB = 4) and the whole range 4 <= kB < (p + 6)/4 asked for.
 (C2) Every item-(iii) word satisfying (H) [all proper patterns certified by singleton extension + a pin pattern]
      and [n_ev,al <= 4, or 2kB <= p and n_ev,al <= 2kB + 2] -- Theorem C (proof-C-r1.md); for all-singleton words
      (any B, any positions) the second condition is automatic (Corollary S).  (H) is a finite phi-independent
      condition on the run datum (no search over reflection values), verified per word by exact DP; it is NOT
      proved for any infinite family in this cycle.
OPEN (precisely): the item-(iii) words outside (C1) that fail (H) or fail the n_ev,al condition.

Exact checks of this map ([F], map3.cpp; labels WALL = (C1), C = (C2)):
 * p = 5 (exhaustive, out/map3_p5.txt): item (iii) = 28 words, ALL in W(5, 1) and in (C1) (and (C2)).  Open: none.
 * p = 7 (exhaustive, out/map3_p7.txt): 40,051 item-(iii) words: 781 in (C1) (W(7, 1..3)), all 40,051 in (C2)
   ((H) holds for every word, n_ev,al <= 2).  Open: none.  (The 11,590 ZSI-B words also satisfy (C2).)
 * p = 11 (6,000 random NMH words with R <= 2p-3, seed 1104, out/map3_p11.txt): 5,318 item-(iii) words: 339 (C1),
   4,959 (C2) (incl. the 339), 359 open: 356 fail (H) (some pattern not certified) and 3 fail only the n_ev,al
   condition (k = p+2, kB = 1, B = 4, excess 6).  The (H)-failures: kB >= 5 (mostly kB = 6, 7: 3kB > p + 4) or
   k = 2p-3 = 19 with large B (all-singleton, (kB, B) = (1, 7), (2, 6), (3, 5), (4, 4), ...), or k = 17, 18 with
   (kB, B) = (1, 5), (1, 6).
 * p = 13 (800 random, seed 1304, k <= 23, out/map3_p13.txt): 746 item-(iii) words: 30 (C1), 655 (C2), 91 open:
   87 fail (H) (kB >= 6, or kB = 5 with k = 21, or k = 21 with B = 8), 4 fail only the n_ev,al condition.
 * Independent re-check of (H) (hcheck.py, out/hcheck.txt): 28 (p = 5) + 400 (p = 7) + 257 (p = 11, k <= 16) dumped
   words, all verdicts reproduced; mutation control (out/hcheck_mut.txt): demanding p + 1 + MUT in condition (B)
   changes 400/400 verdicts at p = 7 for MUT = 4 (none for MUT <= 3: the p = 7 words have slack >= 3 there) and 1,
   resp. 19 of 257 at p = 11 for MUT = 1, 2.

Structure of the open part (what blocks the methods):
 * High kB.  For W(p, kB) with 3kB >= p + 5 the anti pair {0, s} is not certified by singleton extension (proved,
   proof-WALL.md Remark 2), so no lifting argument of the Lemma L type starts; and by the type-count bound of
   c2/nobc_bound.py ([F]; Lemma NOBC proves it only for 4 <= kB < (p+6)/4) these words have NO Lemma BC certificate
   for 4 <= kB <= 10 (p = 17), 4 <= kB <= 12 (p = 19), 4 <= kB <= 16 (p = 23).  So W(p, kB) with
   (p + 4)/3 < kB <= K_BC(p) (kB = 8..10 at p = 17, 8..12 at p = 19, 10..16 at p = 23) is beyond BOTH current
   techniques; [F] they have no avoider at p = 11, 13 (c2/famdfs, out/famdfs_W_high.txt; p = 17 running, Sec. 10).
 * Large B relative to p (all-singleton words near k = 2p-3): condition (B) of singleton extension fails already for
   pairs because lambda({t}^c) = min(p, p - B + 2, ...) is small; Theorem C's argument itself does not need small B.
 * Many even aligned runs (n_ev,al > max(4, 2kB + 2)): only (B1)/(A) of Theorem C fail; rare in the samples.

## 10. Log; extended certification experiment (appended 2026-10-17T12:44:17-0700, before running map3x)

* [F] c2/famdfs on the doubly obstructed words W(17, 8), W(17, 9), W(17, 10) (k = 26, 27, 28): NO avoider
  (65,913,908 / 124,364,043 / 209,776,856 checks; 0.6 / 1.3 / 2.6 s; peak RSS 170 / 338 / 673 MB),
  out/famdfs_W17_high_r2.txt.  (A first attempt, out/famdfs_W17_high.txt, did not run famdfs at all: in this
  harness `timeout` is a shell builtin, so `/usr/bin/time -l timeout ...` failed with "No such file or directory";
  that file records the failure only.)
* Re-read of proof-C-r1.md after freezing: no error found (the checks of Secs. 0-2 were redone by hand).
* Experiment (aid, not yet a written result): Lemma L extends verbatim to EXTENDED certification
  ("Q = Q' u Y with Q', Y certified and condition (b) of Lemma BC for X = Q', Y, Z = Q^c"; the induction step of
  Lemma L uses only the ranges of X_{Q'} and X_Y).  Question: does extended certification with |Y| <= 2 or 3
  turn the (H)-failures of the map into (H)-words?  map3x.cpp (map3.cpp + YMAX) on the same p = 11 sample
  (seed 1104) and p = 13 sample (seed 1304), YMAX = 2, 3.

## 11. Obstruction results for the open part (appended 2026-10-17T12:49:50-0700)

* map3x (extended certification, out/map3x_p11_y1.txt = map3 reproduced, out/map3x_p11_y2.txt with |Y| <= 2): only 4 of
  the 359 open p = 11 words become (H)-words (the (kB, B, k - p) = (1, 5, 6), (1, 6, 7) x 2, (3, 5, 8) ones); the high-kB
  and the large-B failures stay.  Not pursued further (Lemma NOLIFT below explains the high-kB part).
* proof-NOBCplus.md ([W]): Lemma NOBC+ (no Lemma BC certificate for W(p, kB) whenever rho(p + kB) - sigma < p + 1;
  explicit: p > kB + 7 + 18/(kB - 3); exact criterion: 4 <= kB <= p - 7 for all primes 17 <= p <= 199 except p = 19:
  p - 8), Lemma NOLIFT (for 3kB >= p + 5 no pattern {0, s} is certified; for 3kB > p + 6 nothing beyond singletons is
  certified, also with extended certification), and the doubly obstructed family DOB(p) (empty for p <= 13; e.g.
  DOB(17) = {8, 9, 10}, DOB(23) = {10..16}, DOB(199) = {68..192}).  [F] nobcplus.py / out/nobcplus.txt (exact rationals;
  cross-check with c2/nobc_bound.py: 119 (p, kB) pairs, 0 disagreements) and famdfs: no avoider in W(17, 8..10).
* Consequence for the map (Sec. 9): the open part of item (iii) contains, for every prime p >= 17, the explicit
  sub-family DOB(p) of W(p, kB), on which BOTH certificate types of this lane provably fail; a proof there needs a new
  idea (e.g. lifts with tracked winding numbers: for 3kB > p + 6 two singleton lifts can sum below the Claim range,
  which happens only for two "deep" runs with x_s, x_t <= (kB - p)/2 - 2 -- an observation, not used).

## 12. Status at the end of the cycle (appended 2026-10-17T12:51:21-0700)

Correction to Sec. 9, p = 13 line: the (H)-failures there are kB >= 6, or kB = 5 with k in {21, 23}, or
(k, kB, B) = (21, 1, 8) (the text said "kB = 5 with k = 21" only).

Written results of cycle 3 ([W], unreviewed; frozen with hashes in out/freeze.txt):
 * proof-W4-r2.md, proof-NOLP-r2.md: answers to the parent's Codex review (two MINOR fixes applied, c2 untouched).
 * proof-WALL.md: Theorem W-ALL (W(p, kB) has no avoider for 1 <= kB <= min(p - 4, (p + 4)/3), all primes p >= 5),
   Lemma CW (certification of all patterns with <= kB + 1 runs and of the interval chain iff 3kB <= p + 4).
 * proof-C-r1.md: Theorem C (every NMH word with R <= 2p - 3 satisfying (H) and [n_ev,al <= 4, or 2kB <= p and
   n_ev,al <= 2kB + 2] has an identity 2p-subword), Corollary S (all-singleton words with (H)).
 * proof-NOBCplus.md: Lemma NOBC+ (no Lemma BC certificate for W(p, kB) when rho(p + kB) - sigma < p + 1, in
   particular p > kB + 7 + 18/(kB - 3)), Lemma NOLIFT (singleton-extension lifting fails for 3kB >= p + 5 / > p + 6),
   the doubly obstructed family DOB(p).
Computed ([F], aids): census3/map3 (item (iii) at p = 5, 7 entirely in (C1) u (C2); samples at p = 11, 13: 93.2% /
87.8% covered), thmC/thmC2 replays (0 failures; mutation controls fail as they must), wkill/wkill2, cw_check,
cert, hcheck (independent (H) re-check, with mutation control), nobcplus (cross-checked with c2/nobc_bound.py),
famdfs (no avoider in W(11, 5..7), W(13, 6..9), W(17, 8..10)).
Open: item-(iii) words outside W-ALL that fail (H) or the n_ev,al condition; in particular DOB(p) for every prime
p >= 17, where both certificate types of the lane provably fail.  NMH(p), MIX_DEF_HIGH(p), RUNS(p) are NOT claimed.
Deviations: the README Sec. 4 heading time "12:2x" and the Sec. 6 phrase "about 12:10" were not clock reads (both
corrected in place by appended lines); five new source files (cert.cpp, census3.cpp, rstest.cpp, thmC.cpp, map3.cpp)
were created with the editor's write tool instead of Python mode "x" (each path was new; nothing was overwritten;
shell outputs used noclobber); proof-C.md is an unfrozen draft superseded by proof-C-r1.md; out/famdfs_W17_high.txt
records a failed launch (shell-builtin `timeout` under /usr/bin/time); four wkill2.py runs were stopped by SIGTERM
(UNKNOWN, unused).
