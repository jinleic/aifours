# MIX_DEF_HIGH cycle 5 (task OlsonRunCount5): the remaining DOB(p) ranges of W(p, kB) and the c3 "hyp" words

Directory created 2026-10-17T14:29:36-0700 (host clock, `date`).  This README is FROZEN before any substantive computation of the cycle:
its SHA-256 and the host time are appended to out/freeze.txt right after it is written.  Later sections are appended
with host-clock times and are written before the computations they describe.  Only this directory (c5/) is written;
everything else is read-only (c4/, c3/, c2/, ../, ../../, ../../../inverse-parity/, the parent review directory).
Files are created with Python open(..., "x") (never overwritten); README.md and out/freeze.txt are only appended to.
Safety: <= 2 CPU processes, <= 4 GiB RAM, <= 2 GiB new data; native time limits (in-program clock checks) only; no
SIGKILL, no Popen.kill(), no subprocess timeouts, no /tmp, no network, no paid APIs or model CLIs, no global config;
an interrupted computation is UNKNOWN.  Progress is logged here at least every 30 minutes; compute chunks <= 3 h.
Labels: [W] written proof (unreviewed), [F] exact computation (aid only, never a hypothesis), [I] inference/conjecture.

## 1. Targets (quantifiers exact)

T1 (review fixes; done and frozen before anything else).  The parent's Codex review of cycle 4
   (institute/runs/six-lane-2026-10-16/review/olson-c4-codex-review-v1.note.md: ACCEPT-WITH-FIXES, no FATAL/MAJOR)
   has two MINOR findings: (a) c4/proof-KB0-r1.md:15 cites the unfrozen, superseded c4/proof-NOBCplus-r2.md ->
   c5/proof-KB0-r2.md cites c4/proof-NOBCplus-r3.md; (b) c4/proof-IND-r1.md:132: exceeding the corollary's upper bound
   (3p - 7)/5 does not imply j1 > delta (counterexample (p, kB) = (17, 9): j1 = 7 < 8 = delta) -> c5/proof-IND-r2.md
   restates the remark as "In the regime j1 > delta, the seed is s = j1 ...".  Mathematics unchanged; c4/ stays frozen.
T2 (LOW end of DOB(p)).  Claim to test, then prove: for every prime p >= 37 and every kB with (p + 5)/3 <= kB < (3p + 1)/7
   (the part of DOB(p) below Corollary IND-I; Theorem KB0 already covers kB = (p + 5)/3 when p = 1 mod 6), no word of
   W(p, kB) is an avoider.  The parity-class system of one independent set is FEASIBLE there (c4/out/indep_all.txt), so
   the certificate must use other patterns.  Candidate: SEEDED CERTIFICATION.
   (s1) seeds: for every aligned run t, u_t = u_(S+t) - u_S with S an independent set of delta := p - kB aligned runs
        (Step 1 of Theorem IND, regime I) gives x_t in [3 - ceil(delta/2), floor(delta/2) - 1]; for the anti run,
        u_0 = u_(S+0) - u_S with S independent and not adjacent to 0 gives x_0 in [2 - ceil(delta/2), floor(delta/2) - 1];
   (s2) Lemma L with the singleton ranges replaced by these seed ranges ("seeded Lemma L"; it certifies the anti pairs
        that Lemma NOLIFT(a) blocks for plain singleton ranges);
   (s3) a seeded Lemma CW: every proper pattern with <= kB + 1 runs and every interval I_i is certified;
   (s4) the pin X_[k] = p and Steps 1-3 of Theorem W-ALL (they need only (s3), the pin and 2kB <= p - 1).
T3 (HIGH end of DOB(p)).  Claim to test, then prove: for every prime p >= 37 and every kB with (3p - 7)/5 < kB <= p - 7
   (and kB in {p - 6, p - 5, p - 4} if the same proof works) no word of W(p, kB) is an avoider.  Candidate: BLOCK SEEDS.
   For a pattern Q of D aligned runs in m blocks and an aligned run t that extends one block (Q + t: D + 1 runs, m blocks),
   u_t = u_(Q+t) - u_Q lies in [lambda(Q+t) - U(Q), U(Q+t) - lambda(Q)] (mod p) (U := p - lambda(complement)); in the
   generic range this is [2m - kB, kB + 2 - 2m], of width 2kB + 3 - 4m, about delta when m is about (3kB - p)/4 -- as short
   as the regime-I seed and much shorter than the seed s = j1 of Theorem IND regime II (width about 2kB/3); then Steps 2-4
   of Theorem IND (size chain in the parity class T, balanced reduction, contradiction at sizes delta and j1).
T4 (c3 "hyp" words).  Regenerate the 3 (p = 11) + 4 (p = 13) item-(iii) words of the c3 samples with reason "hyp" ((H)
   holds, Theorem C's n_ev,al condition fails) from c3/map3.cpp's generator and seeds; try (a) Theorem IND* with the
   word's own T, (b) seeded certification + a Theorem-C-type argument; a uniform argument only if one covers a stated
   family (otherwise word-level [F] receipts only, labelled as such).
T5 (map).  Exact map of W(p, kB) beyond W-ALL and of item (iii) after this cycle; a section "What remains".
NOT claimed unless every piece is proved and reviewed: NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson
for D_(2p).  No literature priority is claimed.

## 2. Representation (imported, not re-proved)

As c4/README.md Sec. 2: Lemma H with the 07:39 correction and the Claim in Lemma BC (../../../inverse-parity/
proof-PAR-K0.md Secs. 1-2), Lemma L (c3/proof-NOLP-r2.md Sec. 1), the family W(p, kB) and (0.1), (0.2), (2.1) of
c3/proof-WALL.md, Theorem W-ALL Steps 1-3 (c3/proof-WALL.md Sec. 2, Codex ACCEPT), Theorem IND Steps 1-4
(c4/proof-IND-r1.md, Codex ACCEPT-WITH-FIXES).  W(p, kB) is ONE avoidance instance per (p, kB): u in Z_p^k with
sum 0 and u_Q in [lambda(Q), p - lambda(Q^c)] (mod p) for every proper Q, lambda depending only on (D_Q, m(Q)).

## 3. Protocol (frozen)

P1 [F] type-level evaluation (Python, exact integers) for every prime 37 <= p <= 61 first, then 11 <= p <= 400 for the
   closed forms, every beyond-W-ALL kB: (i) independent-set and block seeds (every (D, m) type: arc width, liftability
   against the singleton window); (ii) seeded certification on the type level (j, e, m) with the Lemma CW induction order
   (remove an aligned end run of a block with >= 2 runs, else an isolated aligned run), all types with j + e <= kB + 1, and
   the interval chain I_i; (iii) the chain and (L) hypotheses of Theorem IND with block seeds.  Output: the (p, kB) covered
   by T2 and by T3, and the closed-form ranges to be proved.
P2 [F] independent cross-checks: (a) a second implementation working on explicit run sets of the actual word (random
   patterns, lambda recomputed from the run list) for the seed arcs and every certification step; (b) literal replay of
   each written proof on random residue vectors u (each vector must yield a pattern whose u_Q lies in its Lemma H window,
   re-checked by an independent lambda routine); (c) mutation controls (seed range widened by one, windows shrunk by
   one, a step skipped), which must produce failures.
P3 [W] proofs: c5/proof-LOW.md (T2), c5/proof-HIGH.md (T3), each frozen (SHA-256 + host time) in out/freeze.txt; then
   T4 and T5.  Any claimed avoider is only a candidate until replayed by a raw ordered-product DP (../../hw.py dp_has).

## 4. Log and plan refinement (appended 2026-10-17T14:39:18-0700, before the receipt computations it describes)

* T1 done: proof-KB0-r2.md, proof-IND-r2.md frozen (out/freeze.txt 14:30:11); diffs against the c4 r1 files: header +
  the cited file (KB0) / the High-end remark (IND) only.
* Exploratory in-memory computations (eval kernel, stdout only, no receipt yet; to be redone by saved receipt code):
  (a) best seed over ALL (D, m) -> (D +- 1, m') pattern types, primes 37..61, every beyond-W-ALL kB <= p - 4: the best
      aligned seed is ALWAYS [3 - ceil(delta/2), floor(delta/2) - 1] (the regime-I seed of Theorem IND), and it is attained
      at every kB by the PAIR family: Q = m := floor(kB/2) + 1 pairwise non-adjacent blocks of two aligned runs, t an
      aligned run extending one block to three runs (types (2m, m) -> (2m + 1, m)): lambda = m + 1, m + 2 and
      U = m - 1 + ceil(delta/2), m + floor(delta/2).  At the high end this is far better than the seed s = j1 of Theorem
      IND (e.g. kB = p - 4: x_t = 1 is forced).  Anti run: Q = the same pairs with {1, 2} in Q, n notin Q, run 0 extending
      {1, 2} (type (2m - 1, m)): x_0 in [2 - [kB odd] - ceil(delta/2), floor(delta/2) - 2].
  (b) With these seeds as the singleton ranges, Lemma L's two conditions become (A^s) lambda(Q') + lambda(Q^c) >=
      ceil(delta/2) - 2 and (B^s) lambda(Q) + lambda(Q'^c) >= floor(delta/2) (|Q'| >= 2), and on the type level (j, e, m)
      with the Lemma CW order they hold for EVERY proper pattern type (all sizes) and the interval chain, and the pin
      X_[k] = p holds, for every prime 5 <= p <= 89 and every kB with 3kB >= p + 5, kB <= p - 4 (also p = 101, 199).
      A hand check of the nine term sums suggests (A^s), (B^s) hold for |Q'| >= 2 whenever delta >= 4, and the pair steps
      need only 3kB >= p - 5.
  Consequence to be proved (T2 + T3 at once, every prime p >= 11): Theorem SEED -- W(p, kB) has no avoider for
  (p + 5)/3 <= kB <= p - 4: pair seeds (Lemma PS) -> seeded Lemma L (Lemma SL) -> every proper pattern certified and the
  pin (Lemma SCW) -> Steps 1-3 of Theorem W-ALL (their only use of 3kB <= p + 4 / 2kB <= p - 1 is replaced by
  c(Z) >= kB - 1 > 2kB - p - 2); alternatively Corollary S of Theorem C, whose proof uses (H) only through (0.2).
* Receipt plan (P1/P2 instantiated): seeds.py [F] (type level: optimal seeds over all (D, m) types, the pair-family
  closed forms, the certification inequalities of every type step, the pin; primes 5..400 for the closed forms, primes
  37..61 with the full optimal-seed search); wordcheck.cpp [F, independent] (explicit run lists of W(p, kB) at p = 37, 41,
  43, 47, 53, 59, 61 for EVERY beyond-W-ALL kB: explicit pair configurations for every run t, lambda recomputed from the
  run list for random explicit patterns and their CW predecessors, every certification step re-evaluated); replay.py [F]
  (literal replay of the written proof on random and structured residue vectors, every kill re-checked by an independent
  lambda routine on the explicit pattern; mutation controls: seed widened by one, windows shrunk by one, the anti seed
  replaced by the plain singleton range, pair steps with plain singleton ranges).

## 5. Log (appended 2026-10-17T14:53:59-0700)

* T2 + T3 DONE (both ends at once, every prime p >= 11): proof-SEED-r2.md frozen 14:53:31 -- Lemma PS (pair seeds: for every
  aligned run t, x_t in [3 - ceil(delta/2), floor(delta/2) - 1], from Q = floor(kB/2) + 1 pairwise non-adjacent pairs and
  Q + t), Lemma SL (Lemma L with seed ranges, proved from the Claim), Lemma SCW (EVERY proper pattern certified, the pin
  X_[k] = p; anti run with its plain canonical range -- no anti seed needed), Theorem SEED (Steps 1-3 of W-ALL; Step 2's
  first-term bound replaced by c(Z) >= kB - 1 > 2kB - p - 2) and Corollary W-COMPLETE: no word of W(p, kB) is an avoider for
  every prime p >= 5 and every 1 <= kB <= p - 4.  proof-SEED.md, proof-SEED-r1.md = unfrozen drafts (never cited).
* Receipts: out/seeds.txt (type level, primes up to 400 / 113, optimality of the pair seed at p = 37..61, mutation
  controls), out/wordcheck.txt (independent C++ on explicit run lists, exhaustive at p = 11, 13 and W(17, 8..9)),
  out/replay_mut0..3.txt (literal replay, 11,400 vectors, 0 failures; mutation controls fail as they must).
* Next: T4 (the c3 "hyp" words): regenerate them with c3/map3.cpp (same seeds 1104 / 1304) -- map3 prints only aggregated
  "hyp" lines, so a new dumping copy (c5/map5.cpp, derived from c3/map3.cpp, dump of the hyp words only) is compiled here;
  then (a) exact avoider search on each word (c2/famdfs logic re-implemented if needed), (b) seeded certification on the
  word, (c) a uniform argument if the word structure allows one.

## 6. Log (appended 2026-10-17T15:08:39-0700)

* T4 DONE: proof-Cplus-r1.md frozen (2026-10-17T15:08:39-0700) -- Theorem C+ (Theorem C with (ii) replaced by (ii+): 2kB <= p and
  n_ev,al <= 2(k - kB - 2B) + n_pr - 2; the change: step (B1) needs only |X_o| >= 2 Delta + 1, since every other run of the
  maximal blocks of X_o gives sum ceil(L_i/2) >= |X_o|/2 > Delta runs; the n_pr/2 term of c3's count is kept) and Corollary
  HYP: the 3 + 4 c3 hyp words (explicit run data H1-H7) are excluded ((H) [F] by map3/map5 and the frozen c3/hcheck.py,
  (ii+) by arithmetic).  proof-Cplus.md = unfrozen draft (never cited).
* Receipts: out/map5_p11.txt, map5_p13.txt (map5.cpp = c3/map3.cpp + hyp dump; non-dump output byte-identical to the c3 maps,
  `cmp` on the filtered output), out/hyprun.txt (membership, quantities, exhaustive avoider search hypdfs.cpp: no avoider;
  W(11, 5..7), W(13, 6..9) cross-check reproduces c3/out/famdfs_W_high.txt incl. check counts), out/hypdfs_shrink.txt
  (positive control; produced by an INLINE `python3 -B -c` loop over shrink = 0..8 calling ./hypdfs on the seven words --
  the code exists only in this log, see deviation (3) below), out/hcheck_hyp*.txt ((H) re-check by c3/hcheck.py, mutation
  sweep MUT = 1, 2, 3, 4, 6), out/cplus_replay_mut0..2.txt (literal replay, Part 2 on 240 random words incl. 165 outside
  Theorem C; 67 Case B instances need the refined count).
* Observation: six of the seven hyp words have kB = 1, k = p + 2, so D = p and the singleton bounds force x = d; Case A applies.
* Deviation (3): the positive-control receipt out/hypdfs_shrink.txt was produced by this inline command (run in c5/):
  python3 -B -c "import json,subprocess; ws=[json.loads(l) for f in ('out/map5_p11.txt','out/map5_p13.txt') for l in
  open(f) if 'hypword' in l]; for each word i: for s in 0..8: run ./hypdfs p a b l s; print the first s with an avoider
  and its u" (the literal one-liner is in the session transcript; its output format is the receipt's).
* Next: T5 map + "What remains"; then (time permitting) an exploratory [F] test of whether the pair-seed certification of
  proof-SEED-r2.md extends to all-singleton words with B >= 2 anti runs (the largest open class of item (iii)).

## 7. MAP of item (iii) after cycle 5 (appended 2026-10-17T15:30:25-0700)

Item (iii) (c3/README.md Sec. 1): NMH words (all reflection runs odd, p + 1 <= k <= 2p - 2, every rotation run pure or a
(1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p - 1) with R <= 2p - 3, outside the ZSI-B case.  Written exclusions (review
status in brackets; "unreviewed" = [W] of this cycle):
 (C1) Theorem W-ALL, c3/proof-WALL.md [Codex ACCEPT]: W(p, kB), 1 <= kB <= min(p - 4, floor((p + 4)/3)).
 (C2) Theorem C, c3/proof-C-r1.md [ACCEPT]: (H) and [n_ev,al <= 4, or 2kB <= p and n_ev,al <= 2kB + 2]; Corollary S:
      every all-singleton word (any B, any positions) with (H).
 (C3) Theorem KB0, c4/proof-KB0-r1.md [ACCEPT-WITH-FIXES]; the fix is c5/proof-KB0-r2.md (citation only).
 (C4) Theorem IND, Corollary IND-I, c4/proof-IND-r1.md [ACCEPT-WITH-FIXES]; the fix is c5/proof-IND-r2.md (remark only).
 (C5) Theorem IND*, c4/proof-INDstar-r1.md [ACCEPT]: every word whose (p, k, kB, B, E, N) satisfy its finitely checkable
      hypotheses (class level for all-singleton words: c4/out/ind_star3.txt, complete lists in c5/out/indstar_classes.txt).
 (C6) NEW Theorem SEED + Corollary W-COMPLETE, c5/proof-SEED-r2.md [unreviewed]: W(p, kB) has no avoider for every prime
      p >= 11 and (p + 5)/3 <= kB <= p - 4; with (C1): for every prime p >= 5 and EVERY 1 <= kB <= p - 4.  So the whole
      all-singleton B = 1 part of item (iii) is closed by written proofs, uniformly in p, without (H) or computation.
      (C3) and (C4) are special cases (their independent proofs remain valid).
 (C7) NEW Theorem C+ + Corollary HYP, c5/proof-Cplus-r1.md [unreviewed]: (H) and [n_ev,al <= 4, or 2kB <= p and
      n_ev,al <= 2(k - kB - 2B) + n_pr - 2] (contains (C2)); the 3 + 4 c3 "hyp" words H1-H7 ((H) and the count verified).
 Erratum on record: c4/proof-NOBCplus-r3.md [ACCEPT] (DOB(p) obstructs Lemma BC and (H) only).
Consequences (exact):
 * DOB(p) (c4/proof-NOBCplus-r3.md) is closed for EVERY prime p by (C6), at both ends: the low end (p + 5)/3 <= kB < (3p + 1)/7
   (single-parity-class system feasible there) and the high end (3p - 7)/5 < kB <= p - 4 (lift bounds of Theorem IND too
   weak there); in particular DOB(37) = {30}, DOB(41) = {16, 33, 34}, DOB(43) = {17, 34, 35, 36} and, for p = 37, 41, 43,
   47, 53, 59, 61, every beyond-W-ALL kB (also replayed: c5/out/replay_mut0.txt, wordcheck.txt).
 * c3 samples (p = 11: 5,318 item-(iii) words; p = 13: 746): no open word remains (WALL/C labels: before; 356 + 87
   notH_cert words: (C5) per the c4 receipt c4/out/ind_star_ex.txt; 3 + 4 hyp words: (C7)).  p = 5, 7: item (iii) lies in
   (C1) u (C2) (c3, exhaustive).
 * All-singleton words (B anti runs, any positions), class level ([F] c5/out/indstar_classes.txt, totals identical to
   c4/out/ind_star3.txt): of the 3,221 classes (p, k, B) with p <= 43, 2,623 satisfy the (C5) hypotheses; of the other 598,
   117 have B = 1 (closed by (C6)) and 481 have B >= 2.  Word level ([F] c5/out/allsing_run.txt, exploratory tool
   allsing.cpp, one word per rotation class; its (H) counts re-derived by the frozen c3/hcheck.py routine for the 13 classes
   with k <= 16, out/allsing_xcheck.txt: 13/13 agree, hcheck's MUT = 1 changes 6 classes): every word of the B >= 2
   uncovered classes at p = 11 (3 classes, 55 words), p = 13 (3 classes, 68 words) and at p = 17 with k <= 24 (6 classes,
   206 words) satisfies (H), so (C2) Corollary S applies.  Hence every all-singleton item-(iii) word with p = 11 or p = 13 is
   excluded by a written theorem whose hypotheses are verified by exact computation ([W] + [F], as (H) in c3); at p = 17 the
   only all-singleton classes not so covered are (k, B, kB) = (25, 3, 5), (25, 4, 4), (26, 4, 5), (27, 5, 5) (not computed).

## 8. What remains (appended 2026-10-17T15:30:25-0700; exact; nothing below is claimed)

Open part of item (iii) after cycle 5 = the item-(iii) words outside (C1)-(C7).  Precisely, a word is open iff it is NOT
W(p, kB) (i.e. B >= 2 or excess E >= 2), the IND* hypotheses fail for it (for every available independent set T of single
rho_1 runs), and either (H) fails, or (H) holds but n_ev,al >= 5 and [2kB > p or n_ev,al > 2(k - kB - 2B) + n_pr - 2].
 (R1) All-singleton words, B >= 2, failing (H), in the 481 classes (p <= 43) listed in c5/out/indstar_classes.txt (for
      p >= 47 the class lists are not computed).  Known: none at p = 11, 13; none in the six p = 17 classes with k <= 24.
      Unknown: p = 17 classes (25, 3, 5), (25, 4, 4), (26, 4, 5), (27, 5, 5); every class at p >= 19.  Evidence for the next
      step ([F], exploratory, out/allsing_run.txt): the seeded condition (H^s) (Lemma SL of c5/proof-SEED-r2.md with
      two-pattern seeds over ALL patterns, a per-word computable certificate) holds for every all-singleton item-(iii) word at
      p = 11 (all 7,460 rotation classes; 4,957 of them already have an empty seed set, i.e. no avoider) and at p = 13 with
      k <= 20 (4,197 words), including the 4,447 + 159 words where (H) fails.  Obstacle to a uniform proof (out/seedB_type.txt,
      type level, p <= 43): the B = 1 recipe of Theorem SEED (pair seeds for aligned runs, canonical ranges for anti runs)
      passes for all 224 B = 1 classes but for only 220 of the 2,997 B >= 2 classes; the failures are anti-only patterns
      (2,225 classes: adjacent anti runs need their own seeds), pair steps (348) and non-contiguous seed sets (204).
      Candidate theorem "SEED-B": seeds for anti runs (difference of two patterns that differ by the anti run) + seeded
      certification of every proper pattern + Corollary S; its written use of (H^s) also needs the remark that the
      proof of Theorem C uses (H) only through (0.2) (c5/proof-SEED-r2.md Remark (3)).
 (R2) Words with excess E >= 2 (multi-letter runs or (1,1)-pairs) that fail (H) and the IND* hypotheses.  Not enumerated
      beyond the c3 samples (none left there); c4/out/ind_star_ex.txt: 3,947 of 7,264 general classes (p = 11..31, worst-case
      N) satisfy the IND* hypotheses.
 (R3) Words with (H) where the count of Theorem C+ fails (n_ev,al >= 5 and [2kB > p or n_ev,al > 2(k - kB - 2B) + n_pr - 2])
      and IND* fails.  None in the c3 samples; nonempty parameter sets exist for larger p (n_ev,al <= E <= p - 4).
 (R4) Review: c5/proof-SEED-r2.md and c5/proof-Cplus-r1.md are unreviewed [W]; c5/proof-KB0-r2.md and c5/proof-IND-r2.md
      only apply the two MINOR fixes of the c4 review.
NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* and ordered Olson for D_(2p) are NOT claimed.

## 9. Log: independent exhaustive confirmations at new (p, kB) (appended 2026-10-17T15:31:18-0700, before the runs)

Plan: run the frozen c2/famdfs binary (sha256 adc75b10e0ae782c5231b7b84dd3f06e37b11e07531ffe86aed01eb6195f8e9e, source
c2/famdfs.cpp e579c31b...27fc0; exact avoider search over ALL patterns, Lemma H windows; read-only use, output to c5/out) on
W(17, 11), W(17, 12), W(19, 8), W(19, 9), W(19, 10) (k = 29, 30, 28, 29, 30; never searched before; peak memory <= 2^(k-1) x 5
bytes <= 2.7 GB < 4 GiB), sequentially, under /usr/bin/time -l, no time limit wrapper (each expected < 1 min); then the
positive control W(17, 11) with shrink = 2 (smaller windows; an avoider is expected).  Theorem SEED predicts "avoider: false"
for the five real runs.

## 10. Results of Sec. 9 (appended 2026-10-17T15:41:47-0700)

* out/famdfs_seed_confirm.txt: NO avoider in W(17, 11), W(17, 12), W(19, 8), W(19, 9), W(19, 10) (checks 317,216,306 /
  419,987,589 / 308,894,722 / 643,972,626 / 1,220,597,919; 5.2 / 10.4 / 2.7 / 5.5 / 11.3 s; peak RSS 1.34 / 2.69 / 0.67 /
  1.34 / 2.69 GB), as Theorem SEED predicts (first exhaustive checks at these (p, kB)).  The planned positive control
  W(17, 11) with shrink = 2 found NO avoider either (225,912,740,166 checks, 137.8 s): shrink 2 is not enough.
* Positive controls therefore re-run on smaller words (out/famdfs_seed_posctrl.txt): W(11, 6), W(11, 7), W(13, 8), W(17, 8):
  no avoider with shrink 1 or 2, an avoider with shrink 3 and 4 in all four (explicit u printed).  So the exhaustive search
  is not vacuous, and these words survive every window shrink by up to 2 -- matching the minimum slack 2 of the seeded
  certification steps (out/wordcheck.txt, out/seeds.txt Part B).

## 11. Status at the end of cycle 5 (appended 2026-10-17T15:41:47-0700)

Written results ([W], NOT yet independently reviewed; frozen with SHA-256 and host time in out/freeze.txt):
 * proof-KB0-r2.md, proof-IND-r2.md -- the two MINOR fixes of the c4 review (citation of proof-NOBCplus-r3.md; the High-end
   remark restated for the regime j1 > delta with the counterexample (17, 9)); mathematics unchanged.
 * proof-SEED-r2.md -- Lemma PS (pair seeds), Lemma SL (seeded singleton extension), Lemma SCW (every proper pattern
   certified, pin X_[k] = p), Theorem SEED (W(p, kB) has no avoider for every prime p >= 11 and (p + 5)/3 <= kB <= p - 4) and
   Corollary W-COMPLETE (with Theorem W-ALL: every prime p >= 5, every 1 <= kB <= p - 4).  Closes DOB(p) at both ends for
   every p (targets T2, T3).
 * proof-Cplus-r1.md -- Theorem C+ (Theorem C with the sharper count (ii+)) and Corollary HYP (the 3 + 4 c3 hyp words; T4).
Computed ([F], aids): seeds.py, wordcheck.cpp, replay.py (SEED; with mutation controls), map5.cpp, hypdfs.cpp, hyprun.py,
c3/hcheck.py re-check, cplus_replay.py (C+; with mutation controls), famdfs confirmations and positive controls, and the
exploratory map tools allsing.cpp / allsing_run.py / allsing_xcheck.py / seedB_type.py / indstar_classes.py (Secs. 7-8).
Map: Sec. 7; what remains: Sec. 8.  NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson: NOT claimed.
Deviations (all recorded here; none overwrote or deleted anything):
 (1) Receipts out/*.txt, out/*.err were created by shell redirection under `set -o noclobber` (creation fails if the file
     exists), and the binaries wordcheck, map5, hypdfs, allsing by `c++ -o` at new paths, instead of Python open(..., "x")
     (the practice of c3/c4); source and proof files were all created with Python mode "x"; the editor write tool was not
     used for any file.  The compiler may use its own temporary files in the system TMPDIR (not /tmp, not created by me).
 (2) Unfrozen superseded drafts kept, never cited: proof-SEED.md, proof-SEED-r1.md, proof-Cplus.md (hashes in freeze.txt).
 (3) out/hypdfs_shrink.txt was produced by an inline `python3 -B -c` loop (Sec. 6), not by a saved script.
 (4) Exploratory eval-kernel computations with stdout only (no receipt, not cited as evidence): the optimal-seed search and
     the type-level seeded-certification checks that found the pair seed (Sec. 4 (a), (b); redone with receipts by seeds.py),
     a first general-B type check (redone by seedB_type.py), and in-memory tests of replay.py / cplus_replay.py before the
     files were created.  One kernel cell (type-level domain check for primes up to 400) was stopped by the harness's 30 s
     cell limit (KeyboardInterrupt; not a signal sent by me): UNKNOWN, unused; redone for primes <= 89 in memory and for
     primes <= 113 by seeds.py Part B.
 (5) Sec. 4 (a) quoted an anti-run seed formula "x_0 in [2 - [kB odd] - ceil(delta/2), floor(delta/2) - 2]" from that
     exploration; it was never verified and is not used (proof-SEED-r2.md uses the canonical anti range).  Sec. 4 (b)'s
     "a hand check suggests" was an expectation written before the proof.
 (6) Plan changes relative to the frozen Sec. 3: one proof (proof-SEED-r2.md) covers both T2 and T3 instead of
     proof-LOW.md / proof-HIGH.md, with pair seeds instead of independent-set/block seeds and without anti seeds; T4 was
     closed by Theorem C+ rather than by IND* or seeded certification; the famdfs runs of Sec. 9 and the positive controls
     were added; the positive control planned in Sec. 9 (W(17, 11), shrink 2) did not produce an avoider and was replaced
     by smaller words (Sec. 10).
 (7) Resource use: at most 2 CPU-active processes at any time (the async allsing / cross-check jobs ran next to short
     kernel or script computations); peak RSS 2.69 GB (famdfs, k = 30); new data about 1.2 MB; no network, no /tmp, no
     model CLIs, no global configuration, no SIGKILL, no subprocess timeouts; the harness deadlines of the async jobs
     (3,600 s / 1,800 s) never fired.  wordcheck.cpp has an in-program time limit (not reached); no other run had a limit.
