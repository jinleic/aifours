# MIX_DEF_HIGH cycle 6 (task OlsonRunCount5, continued by parent direction): R1 = all-single-letter item-(iii) words with B >= 2

Directory created 2026-10-17T15:47:14-0700 (host clock, `date`) with exclusive create (os.makedirs exist_ok=False).  This README is FROZEN
(SHA-256 + host time appended to out/freeze.txt) before any computation of the cycle; later sections are appended with
host-clock times BEFORE the computations they describe.  Only c6/ is written.  c5/ and every earlier proof, receipt and
verdict are read-only and are not re-run (c5 computations are cited by their frozen receipts).  Files are created with
Python open(..., "x"); README.md and out/freeze.txt are only appended to; nothing is deleted, moved or overwritten.
Ownership: this lane owns the RUNS high-run residual; OlsonParity2 owns R*/PAR (nothing is written in inverse-parity/).
Labels: [W] written proof (unreviewed), [F] exact computation (aid only, never a hypothesis), [I] inference/conjecture.

## 1. Exact target (quantifiers preserved)

Original statement (unchanged): an inherited all-odd RGR word of length 4p - 2 is EXCLUDED if it has an identity
2p-subword; the residual RUNS item (iii) asks that every item-(iii) word (c3/README.md Sec. 1) be excluded.
Item-(iii) all-single-letter words: k = p + kB + B single-letter rotation runs on a cycle, B of them rho_(-1) (anti, d = -1)
at ANY positions, the other n = p + kB rho_1 (aligned, d = +1); kappa = k - p = kB + B; item (iii) means p + 2 <= k <= 2p - 3,
1 <= B <= kappa - 1 (i.e. kB >= 1), so kB + B <= p - 3.  B = 1 is W(p, kB) (closed by c3 W-ALL + c5 SEED, the latter under
review).  R1 := the all-single-letter item-(iii) words with B >= 2 that fail (H) (c3/proof-C-r1.md) and whose class
(p, k, B) fails the hypotheses of Theorem IND* (c4/proof-INDstar-r1.md; class lists for p <= 43 in c5/out/indstar_classes.txt:
481 classes with B >= 2).
T1 (priority, finite, [F]): the four p = 17 classes (k, B, kB) = (25, 3, 5), (25, 4, 4), (26, 4, 5), (27, 5, 5), every word
(one per dihedral class of anti-position sets): decide exactly
  (H)    every proper pattern certified by plain singleton extension (Lemma L) + a pin pair;
  (H')   for every proper Q, Q or Q^c is certified (plain) + a pin pair  [Lemma CC below gives (0.2) from (H')];
  (H's)  (H') with SEEDED singleton ranges (Lemma SL of c5/proof-SEED-r2.md, re-proved in c6 for this setting), seeds from
         isolated pair configurations.
  Each of these implies (0.2) of c3/proof-C-r1.md for an avoider, and the proof of Theorem C (n_ev,al = 0, case (i)) then
  gives a contradiction (that proof uses (H) only through (0.2); to be written as Lemma C0 in c6).  Words failing all three:
  exhaustive residue-level avoider search (all proper patterns, Lemma H windows); ANY avoider found by an arc-level search is
  only a candidate until an explicit word is built and replayed by the raw ordered-product DP ../../hw.py dp_has.
T2 (main, [W] only with full proof): a UNIFORM multi-anti-block statement for R1-type words: candidate "Theorem SEED-B":
  seeds for aligned AND anti runs from isolated pair configurations, seeded certification of every proper pattern or of its
  complement in an explicit region of (p, kB, B, anti-block structure), the pin, Lemma CC, Lemma C0 => no avoider.  First a
  structural claim on adjacent anti blocks (where plain certification fails: [F] at p = 11, 13 from c5 receipts).  No
  finite-range promotion: a statement is claimed for all p only with a proof valid for all p; finite checks stay [F].
Not claimed: NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson for D_(2p).

## 2. Headroom at freeze (2026-10-17T15:47:14-0700)

Deadline of the run: 2026-10-18T18:31:43-0700 (about 26.7 h).  Disk: 19.1 GB free on / (global free floor 12e9 bytes =>
c6 new data <= min(2 GiB, free - 12e9), checked before any run expected to write > 100 MB).  Memory: about 65 GB free +
inactive + speculative; c6 processes <= 4 GiB RSS each (a k = 27 full-pattern table: 2^27 bytes per byte array).  CPU: <= 2
busy c6 processes (host load average about 12 from other agents).  Native limits only: in-program time/node limits or
SIGTERM + bounded wait; no SIGKILL, no subprocess timeouts, no /tmp, no network, no model CLIs, no global config.

## 3. Representation (imported, not re-proved)

Lemma H (07:39 correction) and the Claim of Lemma BC (../../../inverse-parity/proof-PAR-K0.md Secs. 1-2): for all-odd
words, beta = 0 and, for a proper pattern Q with y := D_Q (aligned minus anti runs in Q) and m := m(Q) blocks,
   lambda(Q) = lam(y, m) := min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
   lambda(Q^c) = lamc(y, m) := min(p - m + 1, p - B - y + m, floor((p + kB - y)/2) + 1),   U(y, m) := p - lamc(y, m)
(D = n - B = p + kB - B); w avoids iff u_Q notin [1 - lambda(Q^c), lambda(Q) - 1] (mod p) for every proper Q (the empty
pattern never kills in item (iii)).  Lemma L (c3/proof-NOLP-r2.md Sec. 1), the c-coordinates and the proof of Theorem C
(c3/proof-C-r1.md, Codex ACCEPT), Corollary S.  Templates (c5, UNDER REVIEW, re-proved in c6 before any use): Lemma PS,
Lemma SL of c5/proof-SEED-r2.md.  Lemma CC (to be written, elementary): if X_[k] = p and Q^c satisfies X_(Q^c) <= U(Q^c),
then X_Q >= lambda(Q).

## 4. Stop rules (frozen)

S1 Every computation chunk <= 3 h wall clock; per-word exhaustive searches carry a native node/time limit; a limited or
   interrupted run is UNKNOWN and never counted.
S2 T1: if the measured time of a class projects beyond 3 h, the class is finished in a second chunk or reported as
   partially computed (exact counts of the words done), never extrapolated.
S3 T2: a theorem is written only after (a) a type-level exact check of every inequality on the claimed region for all
   primes up to 400 and (b) a hand proof of every inequality for all p; if (b) fails, the region is shrunk to what is
   proved, and the failure set is reported exactly.  Every written theorem gets an exact-control smoke: literal replay on
   explicit words with mutation controls that must fail.
S4 Stop at parent direction or at the deadline; README checkpoint at least every 30 min.

## 5. Handoff from c5 (deviations of cycle 5, carried over verbatim in substance; see c5/README.md Sec. 11)

(1) c5 receipts were created by shell redirection under noclobber and binaries by c++ -o (not Python "x"); (2) unfrozen
superseded drafts kept, never cited: c5/proof-SEED.md, proof-SEED-r1.md, proof-Cplus.md; (3) c5/out/hypdfs_shrink.txt came
from an inline python3 -c loop; (4) exploratory eval-kernel computations without receipts (one cell stopped by the harness
30 s limit: UNKNOWN, unused); (5) an unverified anti-seed formula quoted in c5 README Sec. 4 (a), unused; (6) plan changes
vs the frozen c5 protocol (one SEED proof for both ends, Theorem C+ for T4, extra famdfs runs, replaced positive control);
(7) resources within limits (<= 2 busy processes, peak RSS 2.69 GB, ~1.2 MB data).  c5 results under parent review:
proof-SEED-r2.md, proof-Cplus-r1.md (not yet accepted).  c5 computations are NOT re-run here.

## 6. Log (appended 2026-10-17T15:50:09-0700)

* Parent message: the Codex hostile review of c5 is ACCEPT with no findings (institute/runs/six-lane-2026-10-16/review/
  olson-c5-codex-review-v1.note.md; it independently re-verified all 139,250 proper-pattern instances for H1-H7); Theorem SEED /
  Corollary W-COMPLETE and Theorem C+ are accepted in their stated scopes; a Claude review of c5 is running.
* CPU reservation (parent): while the parent runs a raw ordered-product DP smoke, c6 keeps <= 1 busy scientific process and
  launches NO new native process (no compile, no solver) until the parent releases the reservation.  Effective from
  2026-10-17T15:50:09-0700: at that time c6 had no running native job; rcert.cpp (per-word certificates (H), (H'), (Hs0), (H's) with type-level
  two-pattern seeds) is written but not compiled.  Meanwhile: theory (type-level seed/certification analysis by hand and by
  short in-kernel checks only), and the written framework lemmas (Lemma TS two-pattern seeds, Lemma SL, Lemma CC complement
  closure, Lemma C0 = the proof of Theorem C from (0.2)).

## 7. Log (appended 2026-10-17T15:53:24-0700)

* Parent: raw ordered-product DP smoke of the c5 HYP structures PASSED (review/olson-c5-raw-ordered-parent-smoke-v1/
  result.json; finite consumer-path smoke); reservation RELEASED at about 15:53: c6 may use <= 2 busy processes, shared
  math-2 aggregate <= 4 including OlsonParity2 and parent checks (OlsonParity2 informed: c6 uses <= 2).
* During the reservation c6 ran only in its existing eval kernel (one process): an exploratory type-level check (stdout
  only, to be redone as a saved receipt) of the candidate SEED-B certificate for all-single-letter words with B >= 2:
  seeds for aligned AND anti runs from ISOLATED pair configurations (Q = m pairwise non-adjacent aligned pairs, none adjacent
  to t; types (2m, m) -> (2m + d_t, m + 1); best m; intersected with the canonical lift range), seeded certification of every
  pattern TYPE (j, e, m) requiring every realisable removal kind (aligned/anti, end/isolated) to satisfy (A^s), (B^s),
  complement closure, pin through an anti singleton.  Result (assuming realisability of the pair configurations): of the
  2,997 classes with B >= 2 and p <= 43, 2,113 pass; of the 481 IND*-uncovered B >= 2 classes (c5/out/indstar_classes.txt),
  423 pass (all 96 with B = 2, 327 of 385 with B >= 3, including ALL ten p = 17 classes, so all four priority classes); the
  58 failures are large-B corners (e.g. (p, k, B, kB) = (23, 43, 19, 1)) failing at aligned pair steps (B^s).
* Next (in this order): compile rcert.cpp and cross-check it against the frozen c5 receipt out/allsing_run.txt (per-class
  (H) and (Hs0) counts at p = 11, 13, rotation classes); then T1 = the four p = 17 classes (dihedral classes, saved
  receipts); in parallel the written SEED-B analysis: explicit region, realisability lemma for the pair configurations,
  hand proofs of the type inequalities, then a saved type-level receipt over primes <= 400.

## 8. T2 plan (appended 2026-10-17T16:03:55-0700, before the receipt computations it describes)

Candidate Theorem SEED-B (to be proved for all p, no finite-range promotion):
  all-single-letter words, B >= 2 anti runs at ANY positions, kB >= 1, k = p + kB + B, in the SMALL-B region
  2B + kB <= p - 2 (equivalently delta := p - kB >= 2B + 2), with [5kB + B + 13 <= 3p or kB + 3.5B + 14 <= 2p]
  (the bracket holds automatically for p >= 19; for p = 17 it holds for all four priority classes): no avoider.
Proof skeleton (hand analysis done in the session, to be written out and checked):
  (i) Lemma TS: for proper Q not containing t with Q + t proper, u_t = some z in [lambda(Q + t) - U(Q), U(Q + t) - lambda(Q)]
      (mod p); with the canonical lift x_t this gives x_t in that interval when it meets [lambda({t}), U({t})] without
      wrap-around.
  (ii) Lemma IS (isolated configurations, always realisable): Q = m pairwise non-adjacent aligned runs none adjacent to t
      (m <= ceil((n - 3)/2)), or m pairwise non-adjacent aligned PAIRS none adjacent to t (m <= ceil((n - B - 4)/3)); in the
      generic regime (explicit inequalities (S1)-(S4) resp. (P1)-(P3)) the seed depends only on the parity of y = D_Q and
      satisfies, for every aligned run, (B - delta + 3)/2 <= x_t <= (delta - B - 1)/2 and, for every anti run,
      (B - delta + 1)/2 <= x_t <= (delta - B - 3)/2.
  (iii) Lemma SCW-B: with these seed ranges (and the canonical lower bounds 2 - kB, -kB), EVERY proper pattern is certified
      (Lemma SL): for |Q'| >= 2 each of the 9 + 9 term sums is >= (delta - B + 2)/2 > target (both removal kinds, m' in
      {m, m - 1}); the 2-run steps by a canonical-or-seed case split; pin through an anti singleton and its complement.
  (iv) Lemma C0: the proof of Theorem C (c3/proof-C-r1.md, case (i), n_ev,al = 0) uses (H) only through (0.2).
Receipts planned: seedB.py [F] (Part A: for every prime p <= 400 and every class of the region: the chosen configuration,
  every generic-regime inequality, realisability bound, the seed values and the real bounds of (ii), the 2-run steps and the
  pin, exact integers; Part B: every type step (j, e, m) of every size for primes <= 61 with the seed ranges of (ii) and the
  analytic lower bound (delta - B + 2)/2 of (iii); Part C: Claim E (existence of a configuration) for every prime 19 <= p <=
  2000 and its failure set for p <= 17; Part D mutation controls); replayB.py [F] literal replay on explicit words (random
  anti positions incl. long anti blocks) with independent kill re-check and mutation controls; T1 per-word census
  (running) as an independent check at p = 17.

## 9. Log (appended 2026-10-17T16:19:45-0700)

* T1 DONE ([F], out/rcert_T1.txt, 16:13): the four p = 17 classes, one word per dihedral class: (25, 3, 5) 52 words, (25, 4, 4) 286,
  (26, 4, 5) 328, (27, 5, 5) 1,534; every word satisfies (H') and (H's) (so each is excluded word by word via Lemma CC/SL + Lemma C0);
  (H) fails for exactly 1 + 13 words.  rcert2 was first validated against the frozen c5 receipt (out/rcert_X.txt: 36/36 classes agree).
* T2: proof-SEEDB-r2.md FROZEN (16:19:28): Theorem SEED-B (uniform, all p): every all-single-letter word with B >= 2, kB >= 1 and
  2B + kB <= p - 2 has no avoider for p >= 19, and for p = 11, 13, 17 except six classes (IND*-covered); covers the four priority
  classes analytically.  New ingredients: seeds for aligned AND anti runs from ISOLATED singles/pairs (always realisable), and a
  type-free certification of every proper pattern (36 term-sum bounds >= (delta - B + 2)/2).  Proposition AB (structural): an interval
  with D_Q <= -4 (kB odd) / <= -5 (kB even) is never certified by plain singleton extension; in the T1 classes these anti-heavy
  intervals are exactly the (H)-failures; exact control out/abcheck.txt (16 classes, 11,155 words, 0 violations; threshold sharp).
  Receipts: out/seedB.txt, out/replayB_mut0..3.txt, out/rmin_T1.txt, out/abcheck.txt.  proof-SEEDB.md, -r1.md: unfrozen drafts.
* Next: the large-B part of R1 (2B + kB >= p - 1, IND*-uncovered); first an exact list for p <= 43 and the structure of these classes.

## 10. Log (appended 2026-10-17T16:27:26-0700)

* Parent (16:2x): Claude review of c5 = ACCEPT-WITH-FIXES (review/olson-c5-claude-review-v1.note.md), Codex = ACCEPT.  Requested
  new frozen revisions SEED-r3 (S1, S2, S3, S4, S9, S10) and Cplus-r2 (C1 MAJOR status-only, C2, C3, optional C4).  DONE, frozen
  16:27:04 in the new subdirectory c6/c5-fixes/: proof-SEED-r3.md (474396f2...), proof-Cplus-r2.md (00e850cf...); the c5 r2/r1 files
  are untouched.  C4 was taken (Theorem C+ hypothesis (ii+) weakened by one, s0 >= 1/2, re-proved by integrality) with a new
  exact-control smoke (c6/cplus_half.py, out/cplus_half_mut0..2.txt).  S10's parity rule re-checked: out/c5fix_check.txt (252/252).
  Drafts c6/proof-SEED-r3.md, c6/proof-Cplus-r2.md (without the Paths paragraph) superseded, never cited.  SHAs sent to the parent.
* Large-B part of R1 (2B + kB >= p - 1, IND*-uncovered): exact list for p <= 43 = 75 classes (all with k >= 2p - 7, i.e.
  kB + B >= p - 7): (F1) huge B, kB <= 9; (F2) B in 2..8, kB huge.  Exploratory type-level check (stdout only, kernel): with
  OPTIMISTIC seeds (intersection over all type transitions, realisability ignored) the first 30 of these classes pass the
  conservative type-level certification -- so the obstacle is realisability/narrow seeds, not the certification inequalities.
  Next: an exact per-class analysis of which seed configurations are realisable in every word of these near-maximal-k classes
  (k >= 2p - 7), aiming at a SEED-B' theorem for kB + B >= p - 7 (or a smaller explicit sub-family), then receipts + proof.

## 11. Exact map of RUNS item (iii) after W-ALL, SEED, SEED-B, IND*, C/C+ (appended 2026-10-17T16:35:42-0700; parent request (1))

Item (iii) = NMH words with R <= 2p - 3 outside the ZSI-B case.  A word has class (p, k, kappa, B), E := R - k (its excess,
even), kB = kappa - B, A = R - B.  Written exclusions and their status:
  W-ALL  c3/proof-WALL.md (ACCEPT): E = 0, B = 1, 3kB <= p + 4.                                              [W, uniform]
  SEED   c5/proof-SEED-r2.md (ACCEPT; fixes in c6/c5-fixes/proof-SEED-r3.md): E = 0, B = 1, 3kB >= p + 5.    [W, uniform]
  SEED-B c6/proof-SEEDB-r2.md (under review): E = 0, B >= 2, 2B + kB <= p - 2 and (E): all p >= 19; p <= 17 except
         six classes.                                                                                       [W, uniform]
  IND*   c4/proof-INDstar-r1.md (ACCEPT): every word whose class satisfies the finitely checkable hypotheses (class level, worst
         case N = ceil((k - B - E)/2)), or whose own T satisfies them.                       [W + F per class or per word]
  C, C+  c3/proof-C-r1.md (ACCEPT), c6/c5-fixes/proof-Cplus-r2.md (under review): every word with (H) and [n_ev,al <= 4, or
         2kB <= p and n_ev,al <= 2(k - kB - 2B) + n_pr - 1].                                          [W + F per word]
Class-level map ([F] c6/map6.py, out/map6.txt; every item-(iii) parameter class (k, kappa, B), primes 11..43): label W (B = 1),
SB (SEED-B), IS (E = 0, IND* class-level), IE (E >= 2, IND* worst-case class-level), OPEN0 (E = 0, none of these), OPENE
(E >= 2, IND* worst case fails):
   p = 11:    70 classes | W   7 | SB    7 | IS   14 | IE    18 | OPEN0   0 | OPENE    24
   p = 13:   135 classes | W   9 | SB   13 | IS   23 | IE    43 | OPEN0   0 | OPENE    47
   p = 17:   364 classes | W  13 | SB   35 | IS   43 | IE   136 | OPEN0   0 | OPENE   137
   p = 19:   540 classes | W  15 | SB   49 | IS   56 | IE   210 | OPEN0   0 | OPENE   210
   p = 23:  1045 classes | W  19 | SB   81 | IS   89 | IE   417 | OPEN0   1 | OPENE   438
   p = 29:  2275 classes | W  25 | SB  144 | IS  152 | IE   949 | OPEN0   4 | OPENE  1001
   p = 31:  2835 classes | W  27 | SB  169 | IS  175 | IE  1200 | OPEN0   7 | OPENE  1257
   p = 37:  5049 classes | W  33 | SB  256 | IS  258 | IE  2175 | OPEN0  14 | OPENE  2313
   p = 41:  7030 classes | W  37 | SB  324 | IS  320 | IE  3058 | OPEN0  22 | OPENE  3269
   p = 43:  8190 classes | W  39 | SB  361 | IS  353 | IE  3570 | OPEN0  27 | OPENE  3840
   totals: {'IE': 11776, 'IS': 1483, 'OPEN0': 75, 'OPENE': 12536, 'SB': 1439, 'W': 224}  (27,533 classes).
Exact remainder (what is NOT excluded by a theorem whose hypotheses are verified at class level):
 (R-a) all-single-letter, B >= 2, 2B + kB >= p - 1 (large B), IND* class check fails: OPEN0 = 75 classes for p <= 43
       (none at p <= 19; p = 23: 1; 29: 4; 31: 7; 37: 14; 41: 22; 43: 27), all with k >= 2p - 7; p = 43 list (k, B, kB):
       [[79, 35, 1], [80, 35, 2], [80, 36, 1], [81, 35, 3], [81, 36, 2], [81, 37, 1], [82, 3, 36], [82, 4, 35], [82, 31, 8], [82, 35, 4], [82, 36, 3], [82, 37, 2], [82, 38, 1], [83, 2, 38], [83, 3, 37], [83, 4, 36], [83, 5, 35], [83, 7, 33], [83, 8, 32], [83, 31, 9], [83, 32, 8], [83, 33, 7], [83, 35, 5], [83, 36, 4], [83, 37, 3], [83, 38, 2], [83, 39, 1]].  Two shapes: B huge with kB <= 9, or B in 2..8 with kB huge (kB + B >= p - 7).  Not computed for p >= 47.
 (R-b) the six small-B classes without condition (E) -- (p; kB, B) = (11; 4, 2), (11; 5, 2), (13; 5, 3), (13; 6, 2),
       (13; 7, 2), (17; 7, 4) -- are labelled IS, i.e. excluded by IND* at class level [W + F]; at p = 11 also word by word.
 (R-c) p = 11, 13: every all-single-letter class is W, SB or IS (no OPEN0); the excess classes are IE or OPENE (24 OPENE classes
       at p = 11, 47 at p = 13).  Word level: only the c3 random samples were mapped (every open sample word is covered,
       c6/c5-fixes/proof-Cplus-r2.md Remark (3)); the full excess-word population at p = 11, 13 is NOT enumerated.
 (R-d) words with excess (E >= 2) in OPENE classes: 12,536 classes for p <= 43 (45.5% of all classes; by E for p = 43:
       {'2': 140, '4': 136, '6': 137, '8': 141, '10': 145, '12': 150, '14': 228, '16': 348, '18': 362, '20': 343, '22': 319, '24': 302, '26': 270, '28': 234, '30': 195, '32': 156, '34': 117, '36': 78, '38': 39}).  Inside them a word is excluded only through per-word certificates ((H) + C/C+, or IND*
       with its own T).  This is by far the largest remaining part; at p = 31 and 43, 97% resp. 96% of the OPENE classes have
       kB <= p/3 or satisfy the small-B-type inequality delta' >= 2 max(B - E/2, 0) + 2 (delta' := 2p - A) (exploratory count).
 Nothing above is claimed beyond the stated classes; NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*, ordered Olson are
 NOT claimed.
Next (parent request (2)): attack (R-d) with a written argument.  Plan (written before computing): "Theorem SEED-E" = SEED-B for
words with excess.  Notation Delta0 := 2p - R = k - 2 kappa (>= 3), delta' := 2p - A, beta' := B - E/2.  (a) Seeds for EVERY run t
(weight d_t = a_t, -b_t or 0) from isolated configurations of single-letter aligned runs: in the generic regime
x_t in [d_t/2 - (Delta0/2 - 1), d_t/2 + (Delta0/2 - 1)]; (b) the >= 3-run certification steps hold for ANY weight d by 18 + 18 term
sums, each >= (Delta0 - d)/2 resp. (Delta0 + d)/2 (hand analysis done: no region condition needed beyond the seeds);
(c) 2-run steps by a canonical-or-seed case split; (d) pin via a singleton and its complement; (e) Lemma C0 with Theorem C+'s
count, which holds for every word of a class with E <= 4, or 2kB <= p and E <= 2(k - kB - 2B) - 1.  Region: explicit
inequalities making the configuration generic for all weights in [-min(B, E + 1), E + 1] and realisable with
n1 >= k - B - E single-letter aligned runs.  Controls: type-level receipt over classes, literal replay on explicit excess words
with mutation controls.

## 12. Log (appended 2026-10-17T16:37:20-0700)

* Parent: Codex review of c6 = ACCEPT-WITH-FIXES (review/olson-c6-codex-review-v1.note.md): no substantive gap in SEED-B,
  Prop AB, the C+ weakening, SEED-r3; one MINOR (proof-SEEDB-r2.md Sec. 6 'exact gain floor(B/2) + 1' compares the REAL cap
  (delta - B - 3)/2 with the integer plain cap; use the integer cap floor((delta - B - 3)/2); e.g. p = 17, kB = 5, B = 4: integer
  gain 3) and a scope remark (R and (E) exact; for p >= 19 the residue is excess words and 2B + kB >= p - 1; at p = 11, 13, 17 the
  six exceptions remain unless IND* is invoked).  To be applied in a batched SEEDB-r3 after the Claude c6 note; r2 stays frozen.
* Parent CPU cap change: from now c6 uses <= 1 busy scientific process (OlsonParity2 <= 1; 2 slots for parent/reviewers).
  Effective at 2026-10-17T16:37:20-0700: no c6 background job is running; only the existing eval kernel computes, one cell at a time.  (Earlier
  c6 work used <= 2 busy processes as allowed then; only per-worker counts are claimed, not aggregate compliance.)
* SEED-E exploration (kernel, stdout only): requiring ONE configuration generic for all weights in [-min(B, E + 1), E + 1]
  passes only 50/137 (p = 17), 390/1,257 (p = 31), 1,158/3,840 (p = 43) OPENE classes -- too strict; next: one configuration per
  weight, and words with bounded run lengths.

## 13. Log (appended 2026-10-17T16:56:39-0700)

* Kernel restart (16:4x): the eval kernel was lost; helpers re-created (no file was written by the lost cells except README
  Sec. 12).  Exploratory SEED-E kernel checks after Sec. 12 (stdout only, no receipts): per-weight configurations do not help
  (p = 43: 1,159 of 3,840 OPENE classes); configurations of ARBITRARY isolated aligned runs: 2,021 (+40 without C+); words with
  single-letter anti runs and no pairs: 2,385 (+40), with 730 classes failing only through an EMPTY seed for some heavy weight
  (such runs exclude their words outright).  A hand derivation (to be written as Theorem SEED-G) shows: for ANY NMH word with
  R <= 2p - 3, if every run t has a seed x_t in [(d_t - Delta0)/2 + 1, (d_t + Delta0)/2 - 1] (Delta0 := 2p - R), then every proper
  pattern is certified -- the >= 3-run steps (36 term sums, each >= (Delta0 -+ d)/2), the 2-run steps (seed-or-canonical split;
  both failing would need 2B + 2E + y + 6 < 0), the pin and the no-wrap condition need NO further hypothesis.  Kernel check (stdout
  only) over all 7,264 item-(iii) classes with p <= 31, all weights d in [-min(B, E + 1), E + 1]: 0 failures.
* Parent interjection (16:5x): assess whether OlsonParity2's Lemma W (inverse-parity/mixdef-low/c2/proof-Rstar-partial-v2.md,
  sha256 0df17ff8...4a40; its audit scope-W-audit.md) extends to high run and fills R-a.  Read-only reading; coordinated with
  OlsonParity2 by message; nothing written outside c6/.  Assessment sent to the parent: NO as it stands.  (1) Lemma W's Steps 1-3 and
  Lemma KL are generic but need lifts with sum x = p AND singleton bounds; MIX_low gets them from its Lemma S (needs D >= p + 2g).
  In high run the prefix-interval chain lifts are well defined (interval windows: lambda(P) + lambda(P^c) >= (p - kappa + 3)/2) with
  sum = p, but x_t >= lambda({t}) needs the BC step condition, which at the 2nd chain step reads lambda(d1 + d2) + lambda(D - d1) +
  lambda(D - d2) >= p + 1 and needs 2B + kB <= p + 2.  Exact kernel check, all 75 R-a classes p <= 43: the 57 classes with B >= kB + 1
  ('huge B, kB <= 9') all have 2B + kB >= p + 3 and fail it for all (d1, d2); the other 18 have B <= kB (Lemma W's hypothesis
  fails).  Canonical lifts have the singleton bounds, but sum = p is known only via full certification, which is what fails in R-a.
  (2) What transfers [I, unreviewed]: with canonical lifts and B >= kB + 1, Steps 1-3 + KL kill whenever sum xh <= p (every run with
  phi >= 0 is cheap for all-single-letter words, so W(cheap) >= p + 2kB); Lemma K (i), (iv), (vi) are automatic and (v) <=>
  c(P) <= D - kB + 2m - 1 holds if 2kB + B <= p + 3 (50 of the 57).  So Lemma W only yields 'R-a avoiders with B >= kB + 1 have
  sum xh >= 2p'.  (3) Side finding (kernel, stdout only): EXACT non-generic two-pattern seeds from always-realisable configurations
  (aligned singles, aligned pairs, anti singles) satisfy the SEED-G seed-quality bounds in 11 of the 75 R-a classes (all with
  B = 2 or 3, kB huge): (p; k, B, kB) = (29; 55, 2, 24), (31; 59, 2, 26), (37; 70, 3, 30), (37; 71, 2, 32), (37; 71, 3, 31),
  (41; 78, 3, 34), (41; 79, 2, 36), (41; 79, 3, 35), (43; 82, 3, 36), (43; 83, 2, 38), (43; 83, 3, 37); for B = 2 they force
  xh = 0 on aligned and -1 on anti runs, so sum xh = -2 is not 0 mod p (direct exclusion).
* Plan (frozen here, before writing): c6/proof-SEEDG.md = Theorem SEED-G (seed quality for every run + Theorem C+'s count
  => identity 2p-subword, any run structure), Lemma IS-G (generic configurations => quality seeds; explicit inequalities for
  singles / pairs of single-letter aligned runs in terms of n1, the maximal aligned length a* and the maximal anti length b*),
  corollaries for (a) R-a classes with B = 2, 3 (exact seeds) and (b) excess words; receipts: seedG.py (type-level verification
  of every lemma over parameter domains + class/profile-level coverage), replayG.py (literal replay on explicit words, with
  mutation controls).  Then the README map update.

## 14. Log (appended 2026-10-17T17:08:55-0700)

* Parent (17:0x): c6 reviews Codex ACCEPT-WITH-FIXES and Claude ACCEPT-WITH-FIXES (no mathematical gap in SEED-B / Prop AB; Cplus-r2
  C4 accepted by both; target (3) SEED-r3 closed by the parent's own diff).  Applied as a NEW file: proof-SEEDB-r3.md FROZEN
  2026-10-17T17:07:23-0700, sha256 93620654fd9e160879b3babb2aa5c7704899628c3f58d15f3d924f0d6b56d62b (r2 unchanged).  Built in the
  kernel by asserted unique string replacements on the r2 text (Codex rounding + Claude F1-F8; F8 recorded as a note in its Sec. 7, no
  Cplus-r3).  SHA sent to the parent for a delta check.
* SEED-G exploration (kernel, stdout only): exact seeds intersected over always-realisable configuration TYPES (single-letter singles
  / pairs, arbitrary isolated aligned runs / adjacent aligned pairs with the y-range hull), quality test a >= (d - Delta0)/2 + 1,
  b <= (d + Delta0)/2 - 1, worst-case run-length profiles: p = 17: OPENE 125 + 9 (no C+) of 137; p = 31: OPENE 1,005 + 87 of 1,257,
  OPEN0 1 of 7 (202 s kernel).
* Hand derivation (to be written in proof-SEEDG.md): R-a classes with B <= 3 are exactly (B, kB) = (2, p - 5), (3, p - 6), (3, p - 7).
  With m := (p - 3)/2 pairs of adjacent aligned runs, (2, p - 5) gives x = 0 on every aligned and x = -1 on every anti run, so
  sum x = -2 is not 0 mod p: no avoider (p >= 11).  (3, p - 6) with m = (p - 3)/2 (p >= 13) and (3, p - 7) with m = (p - 5)/2 (p >= 11)
  give the quality seeds [0, 1] (aligned), [-1, 0] (anti), so Theorem SEED-G applies.

## 15. Log (appended 2026-10-17T17:27:24-0700)

* Parent (17:1x): SEEDB-r3 accepted by the parent's delta check (review/olson-c6-parent-delta-check-v1.md); remaining RUNS(iii):
  excess words and large B.  Continue SEED-E/SEED-G; notify when a written proof is frozen.
* FROZEN 2026-10-17T17:27:14-0700: proof-SEEDG-r1.md, sha256 fb3f8b9d2174ad1131e1e66cf7640429ef6fe8993b82ec19c4f60f0748d31e80
  (r0 draft proof-SEEDG.md kept, never cited: one wording slip in the [Details] of Lemma SCW-G).  Content: Theorem SEED-G (any NMH
  word with R <= 2p - 3, any run structure: quality seeds for every run + C+'s count => identity 2p-subword; the certification of
  every proper pattern needs NO further hypothesis), Lemma GS (seeds from any configuration; generic configurations give quality
  seeds), Corollaries SA, PA (explicit uniform regions for words with excess, configurations of arbitrary aligned runs / adjacent
  aligned pairs), Propositions RA2, RA3 (all large-B all-single-letter classes with B <= 3: (2, p - 5) for p >= 11, (3, p - 6) for
  p >= 13, (3, p - 7) for p >= 11).  Receipts (all [F], aids): seedG2.py Parts A-E, M (out/seedG2_*.txt) and replayG.py /
  replayG2.py (out/replayG_mut0.txt, out/replayG2_mut0..3.txt); numbers in the proof's Sec. 7.  seedG.py was superseded before
  any run (Part A too slow as written).  Each receipt run used one process at a time (cap <= 1 busy process respected).
* Class-level effect (proof Sec. 6, [F] Part E): p <= 43: 7,006 of the 12,536 OPENE classes and 11 of the 75 OPEN0 classes are now
  excluded by written uniform arguments; remaining: OPEN0 64 (all B >= 4), OPENE 5,530 (103 of them in a region but failing C+'s
  class condition).

## 16. Log (appended 2026-10-17T17:46:15-0700)

* Parent (17:3x): SEED-G r1 pinned (review/olson-c6g-parent-inputs-v1/) and sent to Codex and Claude reviews; continue B >= 4 large B
  and the excess classes with written arguments; <= 1 busy process.
* Large B >= 4 (kernel, stdout only): exact seeds of always-available configurations (aligned singles / pairs, anti singles) are
  never of quality in the 57 R-a classes with B >= kB + 1 (aligned seed tops ~ B); for the 7 R-a classes with B <= kB and B >= 4
  (p = 41, 43) the seeds are not of quality either, but an exact type-level certification with these seeds (all s >= 3 domains,
  2-run steps, pin) passes in 6 of them ((41; 4, 34), (41; 7, 31), (43; 4, 35), (43; 4, 36), (43; 5, 35), (43; 7, 33); fails for
  (43; 8, 32)).  A refined reading of the 18 term sums of Lemma SCW-G gives weaker sufficient seed bounds for the s >= 3 steps
  ((QS*): e.g. aligned 1 - a_t <= ceil((Delta0 + E - d + 3)/2), b_t + 1 <= ceil((Delta0 + E)/2 + 2)); not written yet (the 2-run
  steps and the pin would need re-checking).  [I]
* FROZEN 2026-10-17T17:45:31-0700: proof-SEEDG-cls.md, sha256 5a5038e4b22c9a00e95c11f5157357b65ab2cbb3311d241b5478dbcb4e8602ba:
  Lemma PR (run-length profiles), Lemma CF' (single-letter configurations) [W], Corollary X [W+F] (class-level exclusion by
  Theorem SEED-G with exact seeds of always-available configuration types; hypothesis verified per class by seedX2.py).  Receipts
  out/seedX2_mode0..2.txt (code seedX2.py).  p <= 31: of 3,114 OPENE classes, 1,798 by the written SA/PA and 757 more by Corollary X;
  207 with X but without C+'s class condition; 352 neither.  seedX.py (+ out/seedX_mode0..2.txt) superseded, never cited: its
  profile test accepted an empty seed of any weight, also of weights a word need not contain.
* Correction (2026-10-17T17:46:21-0700) to the last bullet above: the p <= 31 OPENE figures are 1,793 (written SA/PA), 756 (additionally Corollary X),
  207 (X without C+'s class condition) and 358 (neither) of 3,114 classes, as computed in proof-SEEDG-cls.md Sec. 4 from
  out/seedX2_mode0.txt; the figures 1,798 / 757 / 352 typed above are wrong.

## 17. Log (appended 2026-10-17T18:06:43-0700)

* Parent (17:5x): SEED-G r1 reviews -- Codex ACCEPT-WITH-FIXES (MAJOR: large-B corollary needs p >= 11; MINOR: k >= 12 false, k >= 7;
  MINOR: off-by-one d_u > 2kB + B), Claude ACCEPT-WITH-FIXES (M1 = the MAJOR; M2 = k >= 12; M3 empty seeds; INFO).  Applied in a NEW
  file: proof-SEEDG-r2.md FROZEN 2026-10-17T17:58:44-0700, sha256 353b0e95c4e58d874038a11b5864514f4049753853d355015e27ebf7330130b7
  (asserted unique replacements on the r1 text; r1 unchanged).  New written coverage recorded there: the six Claim E' classes lie in
  SA/PA (so for p >= 11 the uncovered all-single-letter classes with B >= 2 are in {B >= 4, 2B + kB >= p - 1, outside SA/PA} u
  {(11; 5, 3)}); p = 7 classes (kB, B) = (2, 2), (1, 3) are a coverage gap (not counterexamples).  SHA sent to the parent.
* Parent: prioritise a WRITTEN (QS*) over more class census.  seedXstar.py (superseded before use in any proof text: its (PIN) test
  accepted any live weight; receipts out/seedXstar_mode0..2.txt never cited) showed that with the relaxed bounds every OPENE class
  but one at p <= 31 passes the seed and certification part; the remaining obstacle is C+'s class condition.  Corrected
  seedXstar2.py running (one process).  Next: proof-SEEDGstar.md (Lemma LF closed forms, Lemma SCW-G*, Theorem SEED-G*, Corollary X*).

## 18. Log (appended 2026-10-17T18:17:40-0700)

* FROZEN 2026-10-17T18:16:46-0700: proof-SEEDGstar.md, sha256 476e9a2871cc81352b7bcbb84c31f9c29606f76cb330d18556330578385f5b22
  (Lemma LF, Lemma SCW-G*, Lemma QQ, Theorem SEED-G* [W]; Corollary X* [W+F]); receipts out/seedXstar2_mode0..2.txt (seedXstar2.py);
  seedXstar.py + out/seedXstar_mode0..2.txt superseded, never cited.  SHA sent to the parent.
* Class level p <= 31 ([F]): of 3,114 OPENE classes 1,793 (SA/PA, written) + 756 (X) + 187 (X*) are excluded; 377 pass the seed part
  but fail C+'s class condition (kernel split, stdout only: 15 by 2kB > p, 362 by E > 2(k - kB - 2B) - 1); 1 fails the seed part.
  OPEN0 unchanged except the RA classes.  The remaining obstacle for excess words is the count condition of Theorem C+ (many even
  aligned runs), and for all-single-letter words the large-B classes B >= 4 (57 of the 64 at p <= 43 have B >= kB + 1: aligned seed
  tops ~ B; Lemma W-hi [I] only gives sum xh >= 2p there).
* Session CPU: every receipt ran as ONE background process at a time; kernel explorations ran only while no background job was
  running (<= 1 busy process for this slice since the 16:37 cap change; only per-worker counts are claimed).

## 19. Log (appended 2026-10-17T18:31:20-0700)

* Parent (18:2x): SEEDG-r2 and SEEDGstar received; a delegated delta check (r1 -> r2) and hostile reviews of SEEDGstar and SEEDG-cls run
  under the prefix olson-c6g-r2-; those files are not edited (fixes go into new files).  APPROVED next: the count side for seeded
  words (the 377 + 1 count-failing classes at p <= 31: 15 with 2kB > p, 362 with E > 2(k - kB - 2B) - 1); written lemmas wanted.
* Ownership (by message): OlsonParity2 takes RUNS on o_F <= p (citation-only) and INV*; I keep RUNS item (iii) (C+ count side, large B).
  OlsonParity2 agreed to my re-proof of its Lemma W idea in the presence of (0.2) (cite proof-Rstar-partial-v2.md Sec. 2).
* Hand derivation (plan, written before the receipts): two count-free finishers for (0.2):
  - Lemma C0W: if B >= kB + 1 and 3kB + 1 <= p, (0.2) is infeasible (Lemma W's cheap-run construction; Lemma DF: runs with bh <= 1 have
    c <= kB - 1 by the singleton bound; X_P + m(P) = bh(P) + Phi(P) <= (kB + 1) + 2kB);
  - Lemma C0B: if k >= kB + 3B and (A*) (defects have c <= p - kB - 1; automatic if 2kB <= p or for quality seeds), (0.2) is infeasible:
    in Case B, (2.2) forces n_ev,al <= B + n_an - 2, which makes Theorem C+'s s0 >= k - kB - 3B + 1 >= 1 without any n_ev,al hypothesis.
  Kernel tally (stdout only): of the 378 count-failing classes at p <= 31, C0W applies to 344, C0B (with 2kB <= p) to 76 (57 overlap),
  and the 15 with 2kB > p need C0B with the seed form of (A*).  Receipts seedXX.py (census) and replayW.py (literal replay with
  mutations) are running as one background process; proof text proof-C0WB.md drafted in memory, to be frozen after the receipts.

## 20. Log (appended 2026-10-17T18:59:58-0700)

* FROZEN 2026-10-17T18:59:49-0700: proof-C0WB.md, sha256 ac52d85fc04ebc29aacd5bffbe923355234af752c5b5e2a52efe8b9a9935de77:
  Lemma DF (light runs have c <= kB - 1), Lemma C0W ((0.2) infeasible if B >= kB + 1 and 3kB + 1 <= p; Lemma W's construction),
  Lemma C0B ((0.2) infeasible if k >= kB + 3B and (A*); Case B forces n_ev,al <= B + n_an - 2), Theorem SEED-G**, Corollaries
  SA**/PA** [W]; Corollary X** [W+F].  Receipts out/seedXX_R/X/A.txt, out/replayW_mut0..3.txt, out/replayW2_mut0..1.txt.
* Effect: every SA/PA region class with p <= 61 is now excluded by written uniform arguments (no class left by the count); with exact
  seeds ([W+F]) 3,113 of the 3,114 OPENE classes with p <= 31 are excluded, the remaining one being (31; 51, 24, 23) (kB = 1, E = 8,
  large B, seed part fails).  OPEN0 unchanged (RA only).
* Deviation: about one minute of overlap of a kernel seed computation with the replayW2 background run (two busy processes).

## 21. Log (appended 2026-10-17T19:12:11-0700)

* Large-B draft proof-LB.md frozen at 19:10 is NOT yet sent to the parent.  Before handoff, two wording/coverage points were found:
  (a) RZ's uniform bound 2i <= B - 3 must allow i = 0 even when B < 3 (choosing no anti run is always possible);
  (b) in seedLB2.py PART X, for a* >= 2 and no pairs, the profile's e_an is a MINIMUM, not the actual anti excess.  Hence
      n_an = B - e_an(min) may overestimate available anti runs.  Use the universally valid lower bound n_an >= B - E + a* - 1
      (since E = e_al + e_an + n_pr and e_al >= a* - 1).
* Plan before the replacement receipt: new seedLB3.py PART X uses this correct lower bound; proof-LB-r1.md will retain the Part L
  arithmetic (unchanged) and state i = 0 explicitly, give actual construction smokes with independent slow_lambda and mutation
  controls, and report only the corrected receipt.  The frozen r0 and its receipts remain untouched.
