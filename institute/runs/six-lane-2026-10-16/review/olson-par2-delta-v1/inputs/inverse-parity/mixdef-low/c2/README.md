# mixdef-low/c2: the residual case R* of MIX_low (and the PAR(p) assembly)

Owner OlsonParity2 (task from Main, six-lane run, slot math-2).  Directory created
2026-10-17T13:11:51-07:00 (host clock); this README frozen right after, before any
computation in this directory.  Everything outside c2/ is read-only for this task.

## 1. Frozen target

Setting (../README.md Sec. 1-2, ../proof-MIX-low-partial.md sha 61360ff0...bcbc): an RGR word
v of length 4p-2 (p >= 5 prime), all k reflection runs odd, k <= p, A >= B >= 1,
B < kappa <= k-1, g := kappa - B >= 1, every rotation run pure aligned (d >= 1), pure anti
(d = -c <= -1) or a (1,1)-pair (d = 0) (Lemma M0), A <= 2p-1 (so 2g + B <= k-1).  v avoids,
x = interval-chain lifts (Lemma S), bh = 2x - d, Z0 = {bh <= 0}, Y = complement,
Y_al = aligned runs in Y, m = m(Z0), a_Z = sum_{Z0} (d_t - 1).

R*(p): Phi(Z0) <= 2g+1 and |Y_al| + a_Z <= 2.

Target T1: show that no avoider of MIX_low(p) has its configuration in R*, for every prime
p >= 5 (then Theorem MIX-R gives MIX_low(p), hence PAR(p) with the reviewed pieces), or map
exactly the part of R* that remains open.
Target T2: answer the parent's Codex review of ../proof-MIX-low-partial.md in a NEW file
proof-MIX-low-partial-r2.md (when forwarded).
Target T3: if T1 closes, a frozen PAR(p) assembly listing every imported piece and its
review status.

## 2. Frozen representation

phi_t := d_t - x_t = (d_t - bh_t)/2 (an integer, as bh_t = d_t mod 2).  Lemma S is
equivalent to: sum_t phi_t = p - k + 2g and, for every proper cyclic interval Q,
  phi(Q) <= gam(D_Q),  gam(E) := max(E - p, g - 1, floor((E - B - 1)/2))
(x(Q) >= U_Q + 1 with U_Q = G_1(D_Q); complements give the upper interval bounds).
Defect: 2 phi_t >= d_t.  Phi(P) = 2 phi(P) + 2 m(P).  R*: phi(Z0) + m(Z0) <= g and
|Y_al| + a_Z <= 2.  Kill test (exact, Lemma WAS/H): pattern P kills iff x(P) mod p lies in
I(P) = [-G_m(D - D_P), G_m(D_P)] mod p, G_m(E) = min(p - m, E - g + m - 1, floor((E+B)/2)).

## 3. Frozen plan

C1 (exact census).  Enumerate, for p = 7 (all run data) and p = 11, 13 (all run data
compatible with R*, using only necessary conditions proved in writing before use), every
integer phi satisfying the interval system, and list those whose defect set is in R*.
Two independent implementations (different code paths: interval-system DFS vs a
brute-force over phi boxes with direct recomputation of Lemma S windows from Lemma H);
mutation controls (weakened gam must produce detected R* instances; corrupted kill test
must be rejected); any configuration claimed killed is re-checked by the exact mod-p
window test, and any word claimed to avoid by the raw ordered-product DP
(../../../code/was_verify.py dp_has) before any report.
C2 (proof).  From the census, extract the mechanism and write a uniform proof for all
p >= 5 (or the exact open remainder).  Every new lemma is replayed on the census data.
C3 (review answer) and C4 (assembly) as in Sec. 1.
Limits: <= 2 CPU processes, <= 4 GiB, chunks <= 30 min, no kill signals, host-clock labels,
files created with mode x, proofs frozen in out/freeze.txt (append-only, SHA-256 + time).

## 4. Progress log (host clock)

* 13:11:51 directory created; README frozen (Sec. 1-3).
* 13:50:19 r2 review answer frozen (out/freeze.txt; parent notified).  Census tools: rstar.py (Python,
  p = 5, 7), rstar_census2/3/4.cpp (joint (d, phi) DFS; versions add BK1 tests), xcheck.py
  (independent theta-domain check via gr_window.ach).  [F] p = 5: no interval-feasible phi at all.
  p = 7: 15 canonical interval-feasible (d, phi), 1 in R* (d = (-1,-1,1,1,7,1,1), phi = (0,0,0,0,2,0,0));
  xcheck agrees on all 15.  p = 11 (complete, 4.5 s): 211,911 canonical, 847 in R*, all killed;
  MIX-R construction with exact isolated-filler choice works on all (AV count is lossy).
  p = 13 (census2, CPU limit hit at 1700 s: complete for k <= 12 and k = 13 up to (g,B) = (2,4);
  rest UNKNOWN): Z0 + isolated fillers FAILS on 42 R* solutions (k = 13, g = 1, B = 7, 8), all
  killed by other 2-block patterns.  New candidate kill family BK1 (independent sets of runs
  mixing defects and fillers, Lemma K corollary) holds on all p = 7, 11 solutions; p = 13 BK1
  census (census4, chunked) running.
* 15:53:17 RULE DEVIATIONS (recorded precisely; parent informed 15:51):
  (a) eval cell "Controls for Case-B2 census variant" (~15:0x PDT, exact time not read) ran
      ./rstar_census8 13 4 13 1 0 via subprocess.run inside the eval tool; the tool's 30 s cell deadline
      raised KeyboardInterrupt and CPython's subprocess.run then called Popen.kill() (SIGKILL) on that
      child.  Result UNKNOWN (not used); the p = 13 Case-B2 unpruned census was later rerun to completion
      via bash (out/census8_B2noprune_p13.txt, 15:05:21-15:05:53).
  (b) 15:50 PDT eval cell ran bash -c "./rstar_relax15 11 4 11 1 1 | grep | head" via subprocess.run;
      same mechanism SIGKILLed the bash wrapper; the orphaned rstar_relax15 (pid 14349) was stopped by
      SIGTERM + bounded wait at 15:51:06 (exited within 1 s).  Output discarded, UNKNOWN.
  From 15:51 on: native children only via the bash tool with ulimit CPU limits, never inside eval.
  Earlier eval-hosted runs that completed normally (p = 7/11 census, controls) are unaffected.
* Interim results (host clock 14:50 checkpoint to parent): census complete p = 5, 7, 11, 13 (all
  interval-feasible (d, phi)); R* counts 0 / 1 / 847 / 29,577; p = 17, 19 partial (CPU-limit stops,
  SIGXCPU from ulimit -S -t, UNKNOWN beyond the recorded (k, g, B) index).  No avoider anywhere.
  Case split of R*: A (some bh >= B+1), B1 (some d >= 2p-B), B2 (all d <= 2g+B-2).  A and B1 have
  written arguments (to be frozen in proof-Rstar.md); B2 cap R*: empty at p <= 13 (complete) and
  p = 17 k <= 15 (+ k = 16 up to (g,B) = (3,6)); singleton-only relaxation (ML = 1, 2) is NOT empty,
  so a proof of B2 must use multi-run intervals.
* 16:45:42 proof-Rstar-partial-v2.md frozen (sha256 0df17ff8d5b1...).  New [W]: Lemma KL (any proper S with
  phi <= g-1 on S, c(S) >= g+1, BH(S) <= B kills); Lemma W (B >= g+1 => kill, ANY configuration: W(cheap) >= 2g+1
  from A <= 2p-1); Lemma B1 (a run with d >= 2p-B => kill); Theorem A (R* with bh_T >= B+1); Lemma G1;
  Lemma KS (count/split inside R*); Lemma AC (all runs cheap).  Exact residual R*** (Sec. 6-7).
  [F] exact replay of every construction (lemma_replay*.cpp; p = 11, 13 all configurations; 0 failures;
  mutations rejected); p = 17 complete census of R* with B <= g: 150 configs, all Case A, killed.
  Independent theta-domain cross-check of the census (xcheck_pos.py / xcheck_run.py): 0 mismatches.
  Process: 16:27:30-16:27:45 three runs were briefly active (cap 2): SIGTERM + bounded wait stopped the
  relaxed rstar_relax19 p = 13 runs (ML = 1 pid 25687, ML = 2 pid 28144, ML = 3 pid 28189), UNKNOWN.
  The relaxed rstar_relax22 p = 13 run hit its ulimit CPU limit (900 s, SIGXCPU) without output: UNKNOWN.
  From 16:4x (parent's new cap) at most 1 busy process.
* 17:07:36 Codex review of proof-Rstar-partial-v2.md: ACCEPT, no findings (parent).  scope-W-audit.md frozen
  (k <= p is essential: Lemma S, Lemma K corollary, Fact F(c)); coordinated with OlsonRunCount5.
  proof-PAR-assembly.md frozen (sha256 95e79ed30b48...): Theorem PA (R***(p) empty => MIX_low(p) => PAR(p)) and
  Theorem PF (PAR(p), MIX_low(p) for p = 5, 7, 11, 13, 17; [W] + [F]).  Next: census R* & B <= g at p = 19 (chunked by k,
  1 process), and the written attack on R***.
* 17:53:26 proof-R4-closure.md frozen (sha256 74929e9c40eb...): Lemma R4 (dichotomy on an independent set N of
  Y-runs with s+1 <= BH(N) <= 2s: complement [k]\N kills if phi(N) is small, Z0+ u N kills otherwise) closes R4;
  hence Theorem M (MIX_low(p), all primes p >= 5) and Theorem P (PAR(p), all p >= 5), [W] UNREVIEWED.
  Replays: out/r4_replay_p11.json.  Run closed by the request budget; final report to Main.
* 2026-10-17T22:52:05-0700 Closure-packet reviews answered (Main IRC ~22:4x): Codex (olson-par2-closure-codex-review-v1, 3 MINOR) and
  Claude (olson-par2-closure-claude-review-v1, 11 MINOR), both ACCEPT-WITH-FIXES, no FATAL/MAJOR.  New files (originals
  unchanged), frozen in out/freeze.txt: proof-Rstar-r4.md (sha256 3b27db3f16341b2493bab1ef259e7cec8a1ce4d6d523b74518909bac541d3fa9),
  proof-R4-closure-r1.md (sha256 4432a2d840a2651540e38d4c2b2ad102d3ba7ad21fc25f74606b1d5c9f9f8837), proof-PAR-assembly-r2.md (sha256 0bb78d1f948e4646665ec89fbfe8048f81aa138bbd4d66af1328acbf82276648).
  [Correction, Codex MINOR-3 / Claude MINOR-10] The 17:07:36 entry's "Theorem PF (PAR(p), MIX_low(p) for p = 5, 7, 11,
  13, 17; [W] + [F])" is superseded: this superseded finite claim was conditional on unreviewed census code; the current
  assembly labels it Statement PF [W+F, conditional] (p = 7, 11, 13, 17; p = 5 is Theorem P5 [W]).  The universal
  written proof (Theorems M and P, proof-R4-closure-r1.md) now supplies these prime cases independently.  The 17:53:26
  entry's "[W] UNREVIEWED" now reads: r0 reviewed ACCEPT-WITH-FIXES, fixes in the new files, parent delta check pending.
  Stale lines outside c2/ (proof-PAR-K0.md L4, proof-PAR-Kplus-partial-r2.md L133) recorded in proof-PAR-assembly-r2.md
  Sec. 5.  Unchanged: RUNS(p), INV*(p) open; ordered Olson for D_(2p) not claimed.  No processes were run by this task
  between the last invstar freeze (19:35:15) and this revision.
