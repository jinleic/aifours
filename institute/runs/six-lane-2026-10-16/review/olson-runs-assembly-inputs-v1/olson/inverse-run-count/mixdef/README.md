# MIX_DEF cycle (task OlsonRunCount, new bounded cycle requested by Main)

Frozen 2026-10-17 (host clock read at freeze, see Sec. 5) BEFORE substantive computation.
Nothing in ../ (proof-RUNS.md, README.md, code, out/) is edited by this cycle; the closed
results there (B = 0, kappa <= 1) and the p = 11 split-only canonicity obstruction are cited,
not rerun.

## 1. Target

MIX_DEF(p): every RGR word w of length 4p-2 with all reflection runs odd, 1 <= B < kappa and
B <= A has an identity 2p-subword (any k, no inherited hypothesis).  With Lemma OR and Lemma M0
(../proof-RUNS.md Secs. 11-12) this covers every word with kappa > B >= 1; together with the
closed parts and OlsonParity's kappa = B >= 1 it would give RUNS(p).

## 2. Frozen representation (shadow half-window form; exact consequence of ../README.md Sec. 2)

Runs t = 0..k-1 cyclically, d_t = a_t - b_t, D = A - B, kappa_B := kappa - B >= 1,
2 kappa_B = D + k - 2p, all reflection runs odd (beta = 0, h = H for every pattern).
WLOG (Lemma M0, which keeps kappa_B) every run is pure (a_t b_t = 0) or a (1,1)-pair.
For a proper pattern P with m intervals:
  U_P = min(p - m, D_P + m - kappa_B - 1, floor((B + D_P)/2)),
  L_P = min(p - m, D_{P^c} + m - kappa_B - 1, floor((B + D_{P^c})/2)),
  w avoids  iff  phi(P) notin [-L_P, U_P] (mod p) for all proper P, and B <= kappa.
No full window is assumed (a full window is an identity 2p-subword).  For P with nonempty
non-full window, lift(P) := the representative of phi(P) in the gap (U_P, p - L_P);
lift(P^c) = p - lift(P).  Canonical singleton lifts x_t := lift({t}).

## 3. Proposed intermediate lemmas (to be tested exactly before any proof attempt)

IL (interval lift additivity).  If w is as in Sec. 1, has no full window, and phi avoids
every interval window (all proper cyclic intervals, m = 1) and P = empty, then for every
proper cyclic interval Q, lift(Q) = sum_{t in Q} x_t.  Equivalently: every partition of the
cycle into three consecutive intervals has lift-sum exactly p.  (Consequence: sum_t x_t = p,
so the canonical lifts x are a valid lift vector for Lemma TL-type capacity counting,
without any chain.)

DG (defect greedy with canonical lifts).  Under IL, with bh_t = 2x_t - d_t,
Z = {bh_t <= 0}, delta_P = -sum_P bh: the set P obtained by adding the defects in order of
increasing depth until Phi_D(P) := D_P + 2m(P) + delta_P >= 2 kappa_B + 2, and then (if Z is
exhausted) isolated aligned runs with bh = 1, is killed: sum_P x_t in [-L_P, U_P].

Scope note: a counterexample to IL or DG is a counterexample to that lemma only (such phi are
still killed by other patterns, since no avoider with these parameters is known); it is NOT a
counterexample to MIX_DEF, RUNS or ordered Olson.

## 4. Protocol

Exact test (mixdef/il_check.py, using ../hwsingle for the interval-feasible phi):
p = 5 all MIX_DEF run data (all-odd, pure/(1,1) runs, 1 <= B < kappa, B <= A, no full
window), every interval-feasible phi; p = 7 sampled data, all interval-feasible phi up to a
cap.  For each phi: test IL (all intervals), then DG.  Resource caps: <= 2 CPU, <= 4 GiB,
<= 30 min per chunk.  Outputs to mixdef/out/.  A failure is reported with the exact word and
phi and re-verified by the raw DP of ../hw.py (dp_has) for the claimed non-kill / kill.

## 5. Clock
Freeze time: recorded in out/freeze.txt by the first command of the cycle.

## 6. Results of this cycle (appended after the freeze; Secs. 1-5 unchanged)

Host clock at writing: see out/summary.txt.
* IL: p = 5 exhaustive (426 MIX_DEF run data without full window, all 196 interval-feasible
  phi) and p = 7 sampled (300 data, 102,560 phi): IL and DG held throughout
  (out/il_p5_exhaustive.txt, out/il_p7_sample.txt).
* **IL is FALSE (exact counterexample, p = 11; scope: lemma IL only).**  out/verify_ilfail.txt:
  p = 11, k = 19, every run a singleton,
  a = (1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1), b = 1 - a, l = (1,1,1,1,1,3,1,1,1,1,1,1,3,1,1,1,1,1,1),
  so A = 12, B = 7, kappa = 8, kappa_B = 1, all reflection runs odd, no full window;
  phi = (1,1,1,1,1,1,0,4,5,1,1,4,5,1,4,7,1,4,1) (y_t = y_{t-1} - 2 phi_t, y_18 = 0) avoids every
  interval window and P = empty, but the canonical singleton lifts sum to 44 = 4p, and 262
  intervals have lift != sum of canonical lifts (shortest: the two adjacent anti singletons
  {7, 8}: lift -2 versus 4 + 5 = 9).  The raw ordered-product DP (../hw.py dp_has) confirms
  that this word DOES have an identity 2p-subword (it is killed, e.g. by the pattern {0, 2}
  with m = 2), so this is not a counterexample to MIX_DEF, RUNS or ordered Olson.
  Consequence: no proof of MIX_DEF can go through "interval-feasible => canonical singleton
  lifts form a valid lift vector"; lifts must be allowed to jump, and the kill must then come
  from patterns with m >= 2 (as in this example) or from a phi-dependent choice of lifts.
* The local induction routes to IL also fail at the phi-independent level: MFE (two-sided
  decomposition of each interval) has z3 counterexamples, realised as concrete words without
  full windows at p = 11, 13 (out/z3_mfe*.txt, out/mfe_realize.txt); the "some cut of every
  interval satisfies (A') and some satisfies (B')" induction holds at p = 7 (11,757
  intervals) but fails at p = 11 (969 intervals without a (B')-cut, 5 without an (A')-cut;
  out/anycut_p11.txt).
* DG was only tested where IL held (it held there); after the IL counterexample it has no
  standing as stated.
* Interface (OlsonParity, IRC): their kappa = B >= 1 theorem covers o_F <= p (any k, any
  parities; capped case uses (D0)); kappa = B with o_F >= p+1 is NOT covered by either worker.
* Resource note: the p = 11 il_check run used about 91 CPU-minutes in 4m48s wall (multi-threaded
  numerical libraries), above the 2-CPU share; later runs set OMP/OPENBLAS/VECLIB threads to 1.
* OlsonParity data point (IRC, not rerun here): every inherited word with 1 <= B < kappa at
  p = 5 (all k <= 5: 14,221 data) and p = 7 (k <= 5: 712,231) is killed by Lemma BC on w~
  (cyclic single-run chain 12,724 / 689,575; otherwise best partition + block chain 1,497 /
  22,656).  So for o_F <= p and p <= 7 no DEF argument is needed; they expect p = 17-type
  families (k~ = p, short runs) to need one.  Their files are final for kappa = 0, kappa = 1,
  B = 0 (k <= p) and kappa = B (o_F <= p); they are not working on kappa > B.

## 7. Review note (appended 2026-10-17 ~07:37 PDT; earlier sections unchanged)

The representation line of Sec. 2 ("w avoids iff ... for all proper P, and B <= kappa") uses the
simplified empty-pattern condition; by the review finding on the analogous Lemma H
(../kappaB-high/README.md Sec. 7) it is exact only when A, B <= 2p-1.  No claim here uses the
converse: the tested phi came from ../hwsingle, which checks the exact empty-pattern window, and the
IL counterexample (A = 12, B = 7) has exact I(empty) = [-3,-2], I([k]) = [2,3], neither containing
0 mod 11 (../kappaB-high/out/review_control.txt).
