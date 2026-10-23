# MIX_DEF_HIGH cycle 4 (task OlsonRunCount4): item (iii) beyond Theorem W-ALL / Theorem C

Directory created 2026-10-17T13:16:25-0700 (host clock, `date`).  This README is FROZEN before any substantive
computation of the cycle: its SHA-256 and the host time are appended to out/freeze.txt right after it is written.
Later sections are appended with host-clock times and are written before the computations they describe.  Only
this directory (c4/) is written; everything else is read-only (c3/, c2/, ../, ../../, ../../../inverse-parity/,
the parent review directory).  Files are created with mode "x" (never overwritten); README.md and out/freeze.txt
are only appended to.  Safety: <= 2 CPU processes, <= 4 GiB RAM each, <= 2 GiB new data; native time limits or
`timeout -s TERM` only (never under /usr/bin/time, where `timeout` is a shell builtin), no SIGKILL, no
Popen.kill(), no subprocess timeouts; an interrupted computation is UNKNOWN.  Progress is logged here at least
every 30 minutes.  Labels: [W] written proof (unreviewed), [F] exact computation (aid only, never a hypothesis),
[I] inference/conjecture.

## 1. Targets (quantifiers exact)

Item (iii) is defined in ../c3/README.md Sec. 1 (NMH words with R <= 2p-3 outside the ZSI-B case).
T1 (review answer; first).  The parent's Codex review of cycle 3 (institute/runs/six-lane-2026-10-16/review/
   olson-c3-codex-review-v1.note.md: proof-WALL.md ACCEPT, proof-C-r1.md ACCEPT, proof-NOBCplus.md REJECT as
   written) found that DOB(p) does NOT obstruct every singleton-extension lifting argument (counterexample
   W(19, 8)).  Deliverable: c4/proof-NOBCplus-r2.md = erratum + corrected obstruction statement (DOB keeps its
   definition and is claimed only to have no Lemma BC certificate and to fail (H); the stronger "nothing beyond
   singletons is certified" is claimed only on DOB*(p) := {kB in DOB(p) : NOLIFT(b) applies}), the exact
   description of DOB(p) - DOB*(p), and corrections of ../c3/README.md lines 227 and 262 (c3 stays frozen).
T2 (generalise the reviewer's W(19, 8) argument).  Candidate: for every prime p = 1 (mod 6), p >= 13, and
   kB0 := (p + 5)/3, no word of W(p, kB0) is an avoider (anti triples certified by adjoining the anti singleton to a
   certified aligned pair; pin via a certified pair P, P^c with lambda(P) + lambda(P^c) >= 1; the defect argument
   of ../c3/proof-WALL.md with isolated aligned fillers).  Exact check of every certification step and of the
   kill at p = 13, 19, 31, 37, 43 (and all p = 1 mod 6 up to 199 on the type level) BEFORE the written proof.
T3 (beyond W-ALL, including DOB*).  Candidate theorem: for every prime p >= 11 and every kB with
   (p + 4)/3 < kB <= p - 4, no word of W(p, kB) is an avoider.  Candidate certificate (test first):
   the INDEPENDENT-SET SUBSET-SUM system.  T := pairwise non-adjacent aligned runs (e.g. 1, 3, 5, ...),
   N := |T| <= ceil((p + kB)/2).  Every S subset of T, |S| = j, is a proper pattern with D_S = m(S) = j, so by
   Lemma H its sum u_S must lie in the arc G_j := [lambda(j,j), p - lambda^c(j,j)] (mod p) with
   lambda(j,j) = min(p - j + 1, 2j - kB, floor((j+1)/2) + 1), lambda^c(j,j) = min(p - j + 1, p - 1,
   floor((p + kB - j)/2) + 1).  Claim to test: for 3kB >= p + 5 no v in Z_p^N has v_S in G_|S| for all S.
   Proof idea (to be checked): (a) swap-path spread lemma: lifted j-subset sums of T lie in ONE translate of G_j,
   so (sum of the j largest) - (sum of the j smallest) <= w_j - 1, w_j := |G_j|; (b) hence most values coincide;
   (c) integrality of the slope: j c in G_j (mod p) for a long range of j is impossible when 3kB >= p + 5.
T4 ((H)-failures).  Classify the item-(iii) words of the c3 samples that fail (H) or the n_ev,al condition
   (../c3/out/map3_p11.txt, map3_p13.txt; regenerated with saved dumps if needed), choose an infinite family
   (e.g. all-singleton words with several anti runs near k = 2p - 3, or B >= 2 analogues of W(p, kB) with large
   kB), and prove (H) or a replacement certificate (e.g. the T3 independent-set system) for it.
T5.  Updated exact map of item (iii) with the new labels.
NOT claimed unless every piece is proved and reviewed: NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV*,
ordered Olson for D_{2p}.  No literature priority is claimed.

## 2. Representation (imported, not re-proved)

Lemma H with the 07:39 correction (../../../inverse-parity/proof-PAR-K0.md Sec. 1), the Claim in Lemma BC
(same file Sec. 2), Lemma L (../c3/proof-NOLP-r2.md Sec. 1), the family W(p, kB) and formulas (0.1), (0.2) of
../c3/proof-WALL.md Sec. 0 (all reviewed ACCEPT / ACCEPT-WITH-FIXES).  For an all-odd word every proper pattern Q
has lambda(Q) = min(p - m + 1, D_Q + m - kB, floor((D_Q + B)/2) + 1) (m = m(Q) blocks); the word avoids iff
u_Q is not in [1 - lambda(Q^c), lambda(Q) - 1] (mod p) for every proper Q (empty/full never kill in NMH), where u
is any map from the runs to Z_p with sum 0 (every such u is realised by reflection values).  Allowed arc of Q:
[lambda(Q), p - lambda(Q^c)] (mod p).  In W(p, kB) lambda(Q) depends only on (D_Q, m(Q)), so W(p, kB) is ONE
avoidance instance per (p, kB) (reflection lengths enter only through H; the anti run sits at position 0).

## 3. Protocol (frozen)

P1 [F] review check: type-level and exact (subset DP, ../c3/cert.cpp logic re-implemented) verification of the
   reviewer's W(19, 8) certifications; DOB(p) - DOB*(p) for all primes 17 <= p <= 199 (nobcplus formulas).
P2 [F] T3 test: indep.cpp = DFS over multisets of residues (non-decreasing) with an incremental DP of the
   j-subset-sum sets, pruning as soon as some j-subset sum leaves G_j; output feasible/infeasible and the least N
   for which the system is infeasible, for all 1 <= kB <= p - 4, primes 5 <= p <= 43 (further if fast).
   Cross-check: an independent Python brute force (all sequences up to symmetry, small p) and a mutation control
   (windows shrunk by one, i.e. lambda - 1, must turn some infeasible cases feasible; inside the W-ALL range
   feasible systems must exist, e.g. the constant 1 at p = 17, kB = 4).
P3 [W] proofs, each with an exact replay that follows the written steps (assertions on every intermediate claim):
   proof-NOBCplus-r2.md (T1), proof-KB0.md (T2), proof-IND.md (T3).  Each finished proof is frozen (SHA-256 + host
   time) in out/freeze.txt.
P4 [F] (H)-failure classification and map (map4.cpp derived from ../c3/map3.cpp, new labels), with an
   independent Python re-check of every new label on dumped words and a mutation control.
Any claimed avoider is only a candidate until replayed by a raw ordered-product DP (../../hw.py dp_has).

## 4. Log (appended 2026-10-17T13:33:16-0700)

* T1 done: proof-NOBCplus-r3.md (erratum + corrected statement: DOB(p) = no Lemma BC certificate and (H) fails;
  DOB*(p) := DOB(p) with NOLIFT(b) = nothing beyond singletons certified; Lemma D: beyond W-ALL, aligned pairs are
  certified iff p = 1 (mod 6) and kB = (p+5)/3; DOB(p) - DOB*(p) = that value).  proof-NOBCplus-r2.md = unfrozen draft.
* T2 done: proof-KB0-r1.md (Theorem KB0: W(p, (p+5)/3) has no avoider, every prime p = 1 (mod 6), p >= 13; generalises
  the reviewer's W(19, 8) argument).  proof-KB0.md = unfrozen draft (two receipt counts misquoted; same mathematics).
  Receipts: out/review_check.txt, out/certk_kb0.txt, out/kb0_replay.txt (+ mutation controls), out/kb0_replay_s3.txt.
* T3 first data (P2): out/indep_all.txt (indep.cpp; primes 5..61, all 1 <= kB <= p - 4): the independent-set system on
  T = odd aligned positions is INFEASIBLE for every beyond-W-ALL kB when p <= 31 (p = 17: kB >= 6; 19: >= 8; 23: >= 9;
  29, 31: >= 12) but FEASIBLE in a gap (p + 4)/3 < kB < ~0.42p for p >= 37 (e.g. p = 37: kB = 14; p = 61: kB = 22..25),
  where every feasible multiset is "mostly 1" (indep_enum.cpp: e.g. 0^4 1^22 at (37, 14)).  So the parity-class system
  alone does not cover DOB*(p) for p >= 37; the gap needs the anti run and the sum condition (indep2.cpp with the anti
  run isolated is still feasible there with u_0 = 0).  indcyc.cpp (all independent sets of the cycle, sequence DFS):
  no avoider of that family at (17, 4), (17, 5), (17, 8), (13, 6), (19, 8); (23, 10) hit its node cap (UNKNOWN).
* Deviation: indep.cpp was created with the editor's write tool (new path, nothing overwritten); every later file is
  created with Python open(..., "x").

## 5. T3 plan refinement (appended 2026-10-17T13:45:59-0700, before the computations it describes)

indep_minJ.cpp (stdout only, exploratory; to be re-run with a saved receipt): the infeasibility of the parity-class
system needs only a few sizes, typically small ones (1..6) plus j = B := p - kB (where the arc is [floor((B+1)/2)+1, B-1]).
Candidate proof scheme "IND" for the single class T (|T| = N = ceil((p + kB)/2)), to be checked numerically first
(ind_cert.py, all primes 11 <= p <= 199, all beyond-W-ALL kB):
 (1) seed: for every size j <= N - 1 and t notin S (|S| = j), u_t = u_(S+t) - u_S lies in G_(j+1) - G_j (mod p) -- no
     lifting needed; intersecting with the canonical singleton range gives an improved integer range R for every lift;
 (2) size-chain certification inside T: sizes j -> j + 1 with the improved singleton range R (Lemma L-type condition with
     the actual lifted ranges [lo_j, hi_j]); success means every j-subset sum X_S lies in [L_j, U_j] (translate 0);
 (3) majorization: the balanced sequence (values q, q + 1) with the same total has larger bottom sums and smaller top
     sums than any sorted integer sequence, so (2) + feasibility imply a feasible two-valued profile;
 (4) the two-valued profiles are excluded by explicit arithmetic (to be computed: for which (p, kB) none survives).
The gap (p + 4)/3 < kB < ~3p/7 (p >= 37), where two-valued profiles survive, needs further patterns (both parity classes,
the anti run, the total); planned after (1)-(4).

## 6. Log (appended 2026-10-17T13:53:40-0700)

* ind_cert.py / ind_cert2.py (exploratory, stdout): scheme IND succeeds (p <= 61) on a middle band ~[3p/7, 3p/4] of
  the beyond-W-ALL range; failures at the low end are genuine two-valued {0,1} profiles (the parity-class system is
  feasible there), at the high end (kB > ~3p/4) the consecutive-size seed leaves deep residues and the size chain stops.
* ind_m.py (fixed seed s = max(B, j1), the version the written proof follows): exact coverage for primes 11..199 in its
  stdout run; regime I (j1 <= B) is covered contiguously from its lowest admissible kB; the closed-form band
  ceil((3p+2)/7) <= kB <= floor((3p-3)/5) lies inside the covered set for every prime 11 <= p < 400 (in-memory check).
  In regime II (j1 > B) the size chain fails at size 4 once kB > ~3p/5 + 9 (lower lift bound too weak).
* Next: proof-IND.md (Theorem IND with checkable hypotheses (S), (C), (L); analytic corollary for regime I), the literal
  replay with mutation controls (ind_replay.py), then the map of DOB(p) and T4.

## 7. Log (appended 2026-10-17T13:58:52-0700)

* proof-IND-r1.md frozen: Theorem IND (parity-class certificate; hypotheses (S1)-(S3), (C), (L) finitely checkable),
  Corollary IND-I (every prime p >= 11, (3p+1)/7 <= kB <= (3p-7)/5: W(p, kB) has no avoider).  proof-IND.md = unfrozen draft
  (coverage text of Sec. 3 wrong; mathematics identical).  Receipt out/ind_replay.txt: Part A (hypotheses, primes
  11..400; band failures: none), Part B (31,200 replayed vectors, 0 failures), Part C mutation controls (T shrunk by 2:
  91 no-kill; windows shrunk: 11,556 no-kill; seed skipped: 1,084 no-kill).
* DOB(p) status: fully excluded for p = 17, 19, 23, 29, 31 (KB0 + IND); open: DOB(37) {30}, DOB(41) {16, 33, 34},
  DOB(43) {17, 34, 35, 36}, and for larger p a low end ((p+5)/3 <= kB < ~3p/7, where the parity-class system is feasible)
  and a high end (kB > ~3p/5 + const).
* Next: T4 ((H)-failures: test whether scheme IND / the parity-class system extends to all-singleton words with B >= 2,
  which are the large-B (H)-failures of the c3 map), then the high-end and low-end gaps if time permits.

## 8. T4 protocol (appended 2026-10-17T14:05:08-0700, before the saved receipt runs)

* indepB.cpp + out/indepB_all.txt (p = 5..43, every all-singleton item-(iii) class (k, B), N = ceil((k - B)/2), worst
  case over anti positions): the parity-class system is feasible exactly for 494 classes (all with B <= kB roughly) and
  infeasible for the rest; the c3-sample (H)-failures among all-singleton words (p = 11: k = 17..19 with large B,
  W(11, 6..7); p = 13: k = 20..23) are all infeasible there.
* Theorem IND* (to be written in proof-INDstar.md): Theorem IND for all-singleton words with any B and any anti positions,
  seed = intersection over ALL consecutive-size arcs (lift range R), hypotheses (W) no full window, (C) size chain,
  (L*) every balanced profile with total in the certified range violates some arc -- all finitely checkable.
  ind_star.py (seed with fixed s and the strict condition alpha >= L_1) and ind_star2.py (all-seed range, but a replay
  branch that tagged empty R prematurely) are superseded drafts (never cited); ind_star3.py is the receipt code.
* Runs: ind_star3.py Part A p <= 43 with the indepB cross-check; Part B p <= 19; Part C MUT = 1, 2, 3.

## 9. MAP of item (iii) after cycle 4 (appended 2026-10-17T14:08:38-0700)

Item (iii) (c3/README.md Sec. 1): NMH words with R <= 2p - 3 outside the ZSI-B case.  Proved exclusions ([W], unreviewed
unless stated):
 (C1) Theorem W-ALL (c3/proof-WALL.md, Codex ACCEPT): W(p, kB), 1 <= kB <= min(p - 4, floor((p + 4)/3)).
 (C2) Theorem C (c3/proof-C-r1.md, Codex ACCEPT): (H) + [n_ev,al <= 4, or 2kB <= p and n_ev,al <= 2kB + 2].
 (C3) Theorem KB0 (c4/proof-KB0-r1.md): W(p, (p + 5)/3), every prime p = 1 (mod 6), p >= 13 (generalises the reviewer's
      W(19, 8) argument; aligned pairs certified, anti pairs not).
 (C4) Corollary IND-I (c4/proof-IND-r1.md): W(p, kB) for every prime p >= 11 and (3p + 1)/7 <= kB <= (3p - 7)/5 -- an
      infinite family of words failing (H) (p >= 17), excluded without (H).
 (C5) Theorem IND* (c4/proof-INDstar.md): every item-(iii) word whose (p, k, kB, B, E) satisfy the finitely checkable
      hypotheses (W), (R), (C), (L*) with N = ceil((k - B - E)/2) (or with the word's own set T of single rho_1 runs).
      Theorem IND (c4/proof-IND-r1.md) is its B = 1 special case.
Erratum (c4/proof-NOBCplus-r3.md): DOB(p) obstructs Lemma BC and (H) only; the "no lifting argument" claim of c3 is
withdrawn; DOB*(p) (NOLIFT(b)) is where singleton-extension certification gives nothing beyond singletons.
Exact consequences ([F] receipts named in the proofs):
 * DOB(p): fully excluded for p = 17, 19, 23, 29, 31 ((C3) + (C4)/(C5) with verified hypotheses).  Open: DOB(37) = {30},
   DOB(41) = {16, 33, 34}, DOB(43) = {17, 34, 35, 36}; for larger p, kB in [(p + 5)/3, ~3p/7) minus (C3) (the parity
   class is feasible there, e.g. W(37, 14) would be open without KB0 and W(41, 16) is open) and kB > ~3p/5 + c up to p - 7
   (hypotheses of (C5) fail; the parity-class system itself is infeasible for every p <= 61, [F] only).
 * The c3 samples: every open word of the c3 map with reason notH_cert at p = 11 and p = 13 is excluded by (C5) (worst-case
   N); what remains of those samples is the 3 + 4 words with reason "hyp" ((H) holds, the even-run condition of Theorem C
   fails, excess 6 or 8).  p = 5, 7: item (iii) was already entirely in (C1) u (C2) (c3).
 * All-singleton classes (any B, any positions), p <= 43: 2,623 of 3,221 classes satisfy (C5); 492 classes have a FEASIBLE
   parity-class system (no T-based certificate exists; these are the classes with B <= ~kB), 106 are infeasible corners
   not covered by (C5).
OPEN (precisely): item-(iii) words outside (C1)-(C5); in particular (i) W(p, kB) with (p + 4)/3 < kB < (3p + 1)/7 or
(3p - 7)/5 < kB <= p - 4 whose hypotheses fail (explicit lists for p <= 113 in out/ind_replay.txt), minus (C3);
(ii) words failing (H) whose parameters fail the hypotheses of (C5) (not enumerated beyond the classes above);
(iii) words with (H) failing only Theorem C's even-run condition and the hypotheses of (C5) (e.g. the 7 c3 "hyp" words).
NMH(p), MIX_DEF_HIGH(p), RUNS(p) are NOT claimed.

## 10. Status at the end of cycle 4 (appended 2026-10-17T14:10:31-0700)

Written results ([W], unreviewed; frozen with hashes in out/freeze.txt):
 * proof-NOBCplus-r3.md -- answer to the c3 review (erratum: DOB(p) blocks Lemma BC and (H) only; Lemma D: beyond
   W-ALL the aligned pairs are certified iff p = 1 (mod 6) and kB = (p+5)/3; DOB*(p) := DOB(p) minus that value is where
   singleton-extension certification gives nothing beyond singletons and the lifted system is satisfiable).
 * proof-KB0-r1.md -- Theorem KB0: W(p, (p+5)/3) has no avoider, every prime p = 1 (mod 6), p >= 13 (the reviewer's
   W(19, 8) argument, generalised; Lemma CW-K certification + pin P = {0,2,4}, P^c + defect argument with anti triples).
 * proof-IND-r1.md -- Theorem IND (parity-class certificate, B = 1) and Corollary IND-I: W(p, kB) has no avoider for
   every prime p >= 11 and (3p+1)/7 <= kB <= (3p-7)/5 (words failing (H) for p >= 17).
 * proof-INDstar.md -- Theorem IND*: the same certificate for every item-(iii) word (any B, excess, positions) with
   finitely checkable hypotheses; covers every (H)-failing word of the c3 samples at p = 11, 13.
Map: Sec. 9.  DOB(p) is fully excluded for p = 17, 19, 23, 29, 31; open from p = 37 on at both ends of DOB(p).
Deviations: (1) indep.cpp was written with the editor's write tool (new path; all other files Python mode "x").
(2) Unfrozen superseded drafts kept, never cited: proof-NOBCplus-r2.md, proof-KB0.md (two receipt counts misquoted),
proof-IND.md (coverage text), ind_star.py, ind_star2.py, ind_replayB.py (fixed-regime general-B evaluator, superseded by
ind_star3.py).  (3) Exploratory runs with stdout only (no receipt, not used as evidence in any proof file): indep_minJ,
ind_cert.py, ind_cert2.py, ind_m.py, indep2, indep_enum, and indcyc (the README Sec. 4 indcyc sentence is such an
stdout observation; its (37, 14) run was stopped by its own `timeout -s TERM 120` wrapper and (23, 10) hit its node cap:
both UNKNOWN).  (4) No SIGKILL, no deletion, no network; at most 1-2 CPU processes at a time; new data < 5 MB.

## 11. Correction (appended 2026-10-17T14:11:16-0700)

proof-INDstar.md (frozen 14:08:38) is superseded by proof-INDstar-r1.md: Step 1 cited (W) for the uniqueness of the
canonical lift; the correct reason is that the singleton window is nonempty in item (iii) (lambda({t}^c) >= kB + 2).
The replay codes compute the canonical lift as the unique integer in [L_1, U_1], so the receipts are unaffected.  The map
(Sec. 9) and Sec. 10 refer to Theorem IND* = proof-INDstar-r1.md from now on.
