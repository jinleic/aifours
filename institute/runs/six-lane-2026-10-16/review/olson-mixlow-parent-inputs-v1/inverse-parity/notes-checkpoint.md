# inverse-parity checkpoint log (host-clock labels)

## 2026-10-17T03:24:51-07:00 checkpoint 1 (aids only; nothing here proves PAR for any new p)

Control B1 (README Sec. 2): half-window formula (par_windows.half_window_mask) equals
../code/gr_window.py ach halved on 258,094 random (p in {5,7,11,13}, k <= 8, all P)
cases; kappa-form interval windows agree on every interval tested.  0 mismatches.

F1 (exact, single run datum).  Single-bracket (cyclic-interval) patterns do NOT
suffice at p = 11.  Run datum k = 11, a = (2,1,1,1,1,1,1,1,1,1,6), b = 0,
l = (1,1,1,1,1,1,1,1,1,1,15) (R = 17, F = 25, kappa = 3, inherited, even rotation
runs 1 and 11): no zero certificate, no full interval window, best interval
partition sum = 11 = p.  A DFS over eta in Z_11^10 against all 110 proper interval
windows finds exactly 18 solutions (canonical x sum = 11 = p each), identical to the
integer points of the lap-linearised system.  All 18 violate some 2-bracket pattern
window (each is hit by ~500-790 patterns); raw DP (../code/was_verify.py dp_has) on
the explicit words: all 18 contain an identity 22-subword.  Positive control: the
extremal word a = 1^11, b = 0, l = (1^10, 21), theta = 2^11 is a DP avoider
(inherited) and the partition certificate below correctly fails (best = 11 = p).
Consequence: the frozen route A restricted to intervals cannot prove PAR(p) for all
p; multi-bracket patterns are needed for p >= 11.

F2 (general-pattern partition certificate).  For a pattern P with m blocks and beta_P
even reflection runs among its 2m boundary runs:
  lambda(P) := U_P + 1 = min(p - m + 1, E+_P - kappa + m - beta_P, floor(E+_P/2) + 1),
  L_P = -(lambda(P^c) - 1).
Certificate: a set partition of [k] into >= 2 parts, each with L_P <= 0 (or
lambda(P) <= 0), and sum lambda >= p + 1 (2-part = full window).  Valid for an
avoider whenever the canonical lifts x_i in [0, p-1] of u_{{i}} have sum <= p
("winding <= 1"): then x(P) in [0, p], so x(P) >= lambda(P), sum = p, contradiction.
Coverage (normalised B <= A, no zero certificate): p = 5 all k <= 5 (55,018 + 1,307
run data) and p = 7 k <= 6 (all, interval partitions suffice there, lap conditions
verified); p = 11: 3,989 random inherited violators, all certified.  Winding <= 1 is
NOT yet proved in general (Sec. A of README; lap conditions verified only in these
finite runs).

## 2026-10-17T04:08:26-07:00 checkpoint 2

P1 (proved, written): proof-PAR-K0.md.  Lemma BC (block-chain certificate; rigorous, no
winding hypothesis) and Theorem K0: PAR holds for every inherited avoider with kappa = 0
(all primes p >= 5).  Numerical control of the Theorem K0 construction: all kappa = 0
inherited violators k <= p at p = 5 (2,122) and p = 7 (289,645), 400 random each at
p = 11..31: 0 failures.

F3 (exact, data): all inherited avoiders in the existing complete dumps
(../evidence/was/p5_N18_all.jsonl, p7_N26_all.jsonl) have kappa = 0 and B = 0 after
normalisation; the kappa > 0 avoiders there (type (II) of ../repr-WAS.md 4.3) are all
NOT inherited.

F4 (data; why kappa >= 1 is harder).  (i) p = 17 run datum k = 17,
a = (1^9, 2^8) (this order), b = 0, l = (3^12, 1^5) (kappa = 4, inherited violator): best
set-partition sum of lambda = 17 = p (bestpart.cpp), so Lemma BC cannot certify it; LP
relaxation of {x(Q) >= lambda(Q) all Q, sum x = p} infeasible (min sum 18.1667, optimal
fractional cover by triples), integer min 22; exact WAS check: 56,348 interval-feasible
theta, none survives all patterns.  (ii) family k = p, r in {1,2} with 2kappa twos, all
l odd, b = 0 at p = 19: kappa = 3 gives LP min 18.75 < p (fractional certificates fail)
while integer min = 23 or 24 > p.  So integrality (parity) is essential for kappa >= 1.
scipy for these LPs was installed only into /tmp/olsonparity-pylib (scratch).

F5 (data; DEF route, coordinated with OlsonRunCount who owns DEF for k >= p+1).  Chain
lifts x_t (increments of the arc-lifts of the prefixes (s, s+j]), bh_t = 2x_t - d_t,
sum bh = 2p - D = o_F - 2(kappa - B); defect set Z = {bh_t <= 0}.  kappa >= 1 violators,
150 random each at p = 11, 13, all prefix-feasible theta (<= 3000 per run datum,
33,284 total): Z kills DIRECTLY (x(Z) in [L_Z, U_Z]) in every case.  "Strong lap" (for
every proper Q, x(Q) in [1 - lambda(Q^c), p + lambda(Q) - 1]) held for every
interval-feasible theta tested (p = 17 example: 300; random p = 11, 13: 1,307).

P2 (proved, combinatorial core; not yet written): for B = 0, kappa >= 1, any integer
vector bh with bh_t = r_t (mod 2), sum bh = o_F - 2kappa violates
BH(Q) >= min(C(Q), T(Q), 1) [C = 2p + 2 - 2m - R_Q, T = R_Q + 2m - 2beta - 2kappa] for
Q = Z or Q = Z u {t} (t a non-defect adjacent to Z).  Hence PAR for kappa >= 1, B = 0
follows from strong lap for these two patterns.  Open: strong lap; B >= 1.

## 2026-10-17T04:28:55-07:00 checkpoint 3

P3 (proved, written: proof-PAR-Kplus-partial.md).  Lemma OR (odd-segment reduction: an
avoider w yields an avoider w~ with all reflection runs odd, same kappa, R, F, A, B);
Theorem K1 (kappa = 1, B = 0) and K1' (kappa = 1, B = 1; uses (D0) in the exceptional
case o_F = 2) via Lemma BC; Lemma IP (integer lemma for odd-reflection words, B = 0).
So PAR is proved for kappa <= 1; the open statement is K+_viol for kappa >= 2.
Controls: K1 certificate on all inherited kappa = 1, B = 0 data (p = 5: 2,366; p = 7:
426,275); K1' on all kappa = 1, B = 1 data (p = 5: 10,512; p = 7: 2,411,817); Lemma IP on
198,887 random integer instances: 0 failures each.

F6 (length 4p-1 reroute, aid).  Theorem DR can be rerouted: a length-(4p-1) avoider w has
kappa_w := (R + o_F - 1 - 2p)/2 >= 0; if kappa_w = 0 then (via RUNS and Theorem K0 on a
deletion from a rotation run or odd reflection run) w has no even reflection run and the
DR argument closes with K0 only; kappa_w >= 1 needs a separate statement.  Lemma BC on the
best partition covers all length-(4p-1) words with kappa_w >= 1 at p = 5 (44,330) and
p = 7 (k <= 5; 1,357,222) but fails at p = 19 (family + one rotation, best = p), so the
reroute does not remove the integrality issue.  Not written as a proof file.

## 2026-10-17T05:55:00-07:00 checkpoint 4

P4 (proved, written in proof-PAR-Kplus-partial.md Secs. 3', 6):
* Proposition S1' + Lemma A1' (re-derivations, for k <= p, of OlsonRunCount's Theorem S1 and
  Lemma A1, ../inverse-run-count/proof-RUNS.md Secs. 9, 11): with Lemma OR, every inherited
  word with k <= p, B = 0, kappa >= 1 is solvable.
* Theorem KB: every word with B = kappa >= 1, (V), o_F <= p (any k; capped type-(II) case uses
  (D0)) is solvable.  Controls: all inherited kappa = B >= 2 data k <= p at p = 5 (27,847) and
  p = 7 (30,970,359), 0 failures (capped: 9 and 1,575, all killed by the capped chain);
  random odd-reflection kappa = B, o_F <= p, 1,500 each at p = 11..23: 0 uncapped failures.
  For o_F >= p+1 the cyclic single-run chain fails Hi in ~20-40% of random data (p = 7, 11, 13):
  that range (needed only for RUNS) is not covered.
Status: PAR(p) <= MIX_DEF(p) on o_F <= p, i.e. "every all-odd-reflection RGR word of length
4p-2 with 1 <= B < kappa, B <= A, o_F <= p is solvable" (owned by OlsonRunCount for all k as
MIX_DEF; agreed split: OlsonParity kappa = B, OlsonRunCount kappa > B).
OlsonRunCount FYI (their mixdef/README.md Sec. 6): canonical singleton lifts are NOT
interval-additive in general for B >= 1 (p = 11, k = 19 = o_F > p example); not in our range.

## 2026-10-17T07:03:04-07:00 checkpoint 5

Split update (Main's request to OlsonRunCount, ~06:20): OlsonRunCount took (A) kappa = B with
o_F >= p+1 and has CLOSED it (Theorem KBH, ../inverse-run-count/kappaB-high/proof-KBH.md [W],
zero-sum pigeonhole over p consecutive runs; not reviewed by me).  With Theorem KB (o_F <= p)
kappa = B is closed for all words.  OlsonParity took (B) MIX_DEF on o_F <= p (frozen in
mixdef-low/README.md at 06:27:02).  So PAR(p) <= MIX_low(p) and RUNS(p) <= MIX_DEF(p).
Data for MIX_low (aids):
* Counterexample hunt (inherited violators, kappa > B >= 1, k = p families at p = 11, 13, 17,
  19, 23): 52 run data decided exactly by interval-DFS + all patterns, 0 avoiders; 9 skipped
  (> 20,000 interval-feasible theta, too slow for the all-pattern check here) - UNKNOWN.
* Step-1 inequality S := U_j + L_{j-1} + L^t >= p - 2 (the phi-independent input of
  "x_t >= U^t + 1 for every run") holds at every chain position for 10,000 random MIX_low run
  data (p = 7..19).
* In MIX families (p = 17..23) the plain defect set Z0 = {bh <= 0} of the chain lifts kills
  directly for every interval-feasible theta tested (2,400), also with only the aligned
  defects; the truncation margin Phi(Z0) - (2g + 2) was >= 4 in the 1,412 tested at
  p = 19, 23.  Random MIX_low data (360 run data, p = 7, 11, 13) have NO interval-feasible
  theta at all.
Process note (parent safety rule 2026-10-17): no kill/SIGKILL used by this lane; subprocess
calls (bestpart) had no timeout argument; two eval cells exceeded their tool time limit and
were interrupted by the tool (KeyboardInterrupt in the Python kernel): the p = 7, k = 7
partition scan (only k <= 6 recorded, checkpoint 1) and a p = 11 regime-B full-window scan
(not recorded), plus one MIX statistics cell (partial output only, not used as evidence).

## 2026-10-17T07:39:40-07:00 correction log (Lemma H, from Main / Codex review)

Source of the finding: review/olson-kbh-codex-review-v1.note.md (Codex gpt-6.1-sol,
ACCEPT-WITH-FIXES), minor issue in proof-PAR-K0.md Lemma H (review snapshot lines 18-33,
snapshot preserved by the parent; not touched here): the empty/full-pattern condition was
replaced by min(A, B) <= kappa without the bound A, B <= 2p - 1; counterexample p = 5,
rho_1^10 sigma_0^8.  Fix applied: Lemma H now states the exact condition 0 notin I(empty)
(mod p) and its equivalence with min(A, B) <= kappa when A, B <= 2p - 1; avoiders satisfy
the bound; Lemma OR / Lemma M0 do not increase A, B.  Every use in this directory is the
necessary direction (avoider => zero condition), so no other statement changes.
SHA-256 before -> after:
  proof-PAR-K0.md          64de0812...e5c0 -> 4b107fff...9a38
  proof-PAR-Kplus-partial.md d4be1fa1...b256 -> cc289e5d...a7e5 (Lemma OR wording only)
  README.md: dated correction note appended to Sec. 3 (frozen Sec. 1 untouched), 24eaf6b1...bc51

## 2026-10-17T11:15:34-07:00 checkpoint 6 (MIX_low, o_F <= p)

(Overdue: previous entry 07:39; the eval kernel was lost in between, helpers re-created in
mixdef-low/relaxed_phi.py, sha 27fa7a02...b20b.)
* [W, not yet in a proof file] Step 1 for MIX_low: with G~(E) = min(p-1, E-g, (E+B-1)/2)
  (concave, G_1 >= G~), any interval 3-partition has union masses in [-B, D+B] summing to 2D,
  so the sum of the three G's is >= the value at a vertex, a permutation of (-B, D, D+B),
  which is >= p-2 when D >= p+2g, D+B <= 2p-1, B <= p+1, g >= 1.  Hence chain lifts satisfy
  x(Q) >= G_1(D_Q) + 1 for every proper interval Q.  Converse (complements of intervals are
  intervals): theta is interval-feasible iff its integer lift x (sum p) satisfies these
  lower bounds.  So "interval-feasible theta" = integer bh (bh = d mod 2) with
  BH(Q) >= h(D_Q) := 2G_1(D_Q) + 2 - D_Q for all proper intervals and sum bh = k - 2g.
* [F] Relaxed search (exhaustive DFS per mass vector): 1,002,499 random vectors p in {7,11,13}
  (5 solutions); 4,373 with k in {p, p-1, p-2} (195 solutions, 0 with Phi(Z0) < 2g+2);
  3,640 more (93 solutions, minimum margin Phi(Z0) - (2g+2) = 4); 6,825 structured vectors
  (anti/pair block, units around it, medium runs far away): 399 solutions, 7 with
  Phi(Z0) < 2g+2, every one killed by some pattern (full 2^k scan).
* [F] Plain-Z0 rule is FALSE in general: p = 13, k = 13, g = 2, B = 1,
  d = (-1,1,1,1,1,3,3,3,1,1,1,1,1), bh = (-1,-1,1,...,1), x = (-1,0,1,1,1,2,2,2,1,1,1,1,1)
  satisfies all interval bounds and Phi(Z0) = 4 < 6; it is killed by the 2-block pattern
  {1, 3} (aligned defect + isolated bh = 1 "filler": m = 2, D = 2, x = 1, window [-8, 1]).
  Earlier MIX data (chain lifts of random families) never hit this shape.  The MIX_low proof
  therefore needs a defect-plus-filler rule (each isolated filler: Phi += d+1, BH += 1).
* [F] LP duals of min Phi(Z0) for fixed defect structure use only bh >= 1 on non-defects and
  singleton bounds of big runs (d >= 2g forces bh >= 2): the slack sits in big runs.
* No avoider found; no raw-DP run needed.  All computations single-process, in-kernel.

## 2026-10-17T13:05:41-07:00 checkpoint 7 (final for this run)

* proof-PAR-Kplus-partial-r2.md (review fixes, frozen 11:45:29, sha 8a13d982...fd04); parent
  delta check PASS (review/olson-parity-parent-delta-v1/).
* [F] record mixdef-low/record-Z0-rule-counterexample.md (sha 8036d612...8ce9), script and
  JSON 33f5ca94... / 85a2f98f...; independently re-verified by the parent from the group
  definition (no worker code).
* [W, unreviewed] mixdef-low/proof-MIX-low-partial.md (sha 61360ff0...bcbc):
  - Lemma S (two-sided interval lift bounds, concavity);
  - Lemma K (direct kill, caps automatic when Phi <= 4g+1, BH <= B);
  - Lemma Phi (Phi(Z0) = 2g + a_Z + exc + 2m);
  - Lemma G (at most B fillers needed, within budget; greedy);
  - Lemma AV (enough isolated fillers when |Y_al| + a_Z >= 3).
  MIX_low is therefore reduced to the residual case R*: Phi(Z0) <= 2g+1 and
  |Y_al| + a_Z <= 2.
* [F] ILP (scipy milp): 1,914,626 random (d, Z) with failing Phi and "no bh = 1 isolated
  filler", and 1,482,446 residual (d, Z) structures: no integer solution in either.
  Evidence only.
* No avoider found anywhere; no raw-DP refutation needed.  No SIGKILL or timeout-kill used.
