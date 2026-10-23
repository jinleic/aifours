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
