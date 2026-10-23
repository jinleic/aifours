# KB_HIGH cycle: kappa = B >= 1 with o_F >= p+1 (task OlsonRunCount, option (A) of Main's cycle)

Frozen BEFORE substantive computation; the freeze time and the SHA-256 of this file and of
kbh.cpp are recorded in out/freeze.txt by the first command of the cycle.  Nothing outside this
directory is edited.  Closed results (../proof-RUNS.md Secs. 9-12, B = 0 and kappa <= 1) and the
p = 11 split/interval-lift obstructions (../proof-RUNS.md Sec. 13, ../mixdef/README.md Sec. 6) are
cited, not rerun.  The refuted IL route is not used.

## 1. Target

KB_HIGH(p): every RGR word w of length 4p-2 with F, R >= 1, A >= B = kappa >= 1 and at least
p+1 odd reflection runs (o_F >= p+1) has an identity 2p-subword.
(OlsonParity's Theorem KB, ../../inverse-parity/proof-PAR-Kplus-partial.md Sec. 6, covers
o_F <= p; kappa = B = 1 is closed by K1'.  KB_HIGH together with those and ../proof-RUNS.md
Sec. 11 leaves exactly MIX_DEF (kappa > B >= 1) for RUNS(p).)

Reduction (both steps proved in ../proof-RUNS.md Secs. 11-12): Lemma OR replaces w by the
all-odd word v with k = o_F runs and the same A, B, kappa; Lemma M0 (keeps kappa - B = 0, the
run count, all-odd) makes every rotation run pure or a (1,1)-pair.  Hence KB_HIGH(p) follows from

KB_HIGH*(p): every RGR word v of length 4p-2 with all reflection runs odd, k >= p+1 runs, every
rotation run pure or a (1,1)-pair, and B = kappa >= 1, has an identity 2p-subword
(no inherited hypothesis).

Elementary facts in this setting: R = 2p - k + 2B, so D := A - B = 2p - k, 1 <= D <= p-1,
B >= k - p, A >= B; k = 2p-1 is Theorem ALT, so WLOG k <= 2p-2 (D >= 2); no run has
d_t >= 2p-1 (the other k-1 >= p runs would need B >= k-1 > kappa).

## 2. Frozen representation

Runs t = 0..k-1 cyclically, d_t = a_t - b_t.  For a proper pattern P (set of runs) with m(P)
cyclic blocks and D_P = sum_{t in P} d_t (README Sec. 2 of ../ with h = H = p-1-kappa, beta = 0,
E+ = D_P + B, kappa = B):
   U_P = min(p - m, D_P + m - 1, floor((D_P + B)/2)),   L_P = U_{P^c},   lambda(P) := U_P + 1,
   v avoids  iff  phi(P) notin [-L_P, U_P] (mod p) for every proper P (B <= kappa holds).
Certificate language: Lemma BC (OlsonParity, ../../inverse-parity/proof-PAR-K0.md Sec. 2):
an ordered partition (P_1..P_s), s >= 2, with (a) sum lambda(P_t) >= p+1, (b) for 2 <= t <= s-1
with X = Q_{t-1}, Y = P_t, Z = Q_t^c: lambda(XuY) + lambda(YuZ) + lambda(ZuX) >= p+1 and
lambda(X) + lambda(Y) + lambda(Z) >= 1, (c) lambda(P_s) + lambda(P_s^c) >= 1, kills every phi.
s = 3 is the flat 3-partition certificate: sum lambda(P) >= p+1, sum lambda(P^c) >= p+1, (c).

## 3. Questions / candidate lemmas (tested exactly before any proof attempt)

SRC: Lemma BC with the single-run partition in cyclic order (some start/direction) works.
SR : Lemma BC with the single-run partition in SOME order works.
     (a) holds for every order (OlsonParity's computation: sum lambda({t}) >= p + (k + D_N)/2,
     D_N = sum of d_t <= 0 >= -B > -k; uncapped since d_t <= 2p-2).
     Known obstruction to check: at step t = 2 the upper inequality is at most 2D + 4 < p + 1 when
     D <= (p-5)/2, so SR must fail for k >= (3p+5)/2 unless a full window exists.
BC3: the flat 3-partition certificate works.     BCG: some Lemma BC certificate works.
A failure of SRC/SR/BC3/BCG is a failure of that certificate family only.  Only an explicit
phi verified by the raw ordered-product DP (../hw.py dp_has) would refute KB_HIGH*.

## 4. Protocol

kbh.cpp (this directory): exhaustive KB_HIGH* data at p = 5 (k = 6..8) and p = 7 (k = 8..12);
random KB_HIGH* data at p = 11 (k = 12..20).  Per datum: full window?; else SRC, SR, BC3 and
(k <= bcgmax) BCG.  For data where no certificate is found, an exact avoider search with
../hwsingle (all patterns) and, for any claimed avoider, the raw DP.  Single-threaded processes,
<= 2 CPU, <= 4 GiB, <= 30 min per chunk; outputs in out/.

## 5. Addendum (appended after the first census; Secs. 1-4 unchanged)

Census so far (out/kbh_p5_exh.txt, out/kbh_p7_exh.txt, out/kbh_p11_rnd.txt): every KB_HIGH*
datum at p = 5, 7 (all) and p = 11 (400 random) has a full window or a single-run Lemma BC
chain.  But the extreme family p = 11, k = 19, B = 8, R = 19 (all runs single letters) has
neither (R = 2p-3, and step 2 of any single-run chain is <= 2D + 4 = 10 < 12), yet ../hwsingle
finds no feasible phi even with intervals only (famM = 1; out/extreme_p11_k19.txt).
New candidate certificate in the SAME frozen representation (added before testing it):

ZS (zero-sum interval certificate).  Let W = (w_1, ..., w_p) be p cyclically consecutive runs
(possible as k >= p+1).  If there are integers theta_t (t in W) with, for every nonempty
subinterval Q of W (a proper cyclic interval, m = 1),
      D_Q - U_Q <= theta(Q) := sum_{t in Q} theta_t <= D_Q + L_Q,
then every phi is killed.  Proof: put tau_t = d_t - theta_t and S_j = sum_{i <= j}
(phi_{w_i} - tau_{w_i}) mod p, j = 0..p; two of these p+1 residues coincide, S_i = S_j with
i < j, so Q = {w_{i+1}, ..., w_j} has phi(Q) = tau(Q) (mod p) and tau(Q) = D_Q - theta(Q) lies in
[-L_Q, U_Q] = I(Q).  The conditions are difference constraints on the prefix sums of theta, so
integer feasibility is decided exactly by Bellman-Ford (zs.cpp).  ZS0 := ZS with theta = 0, i.e.
every subinterval of W has D_Q in I(Q), i.e. (by the window formula) D_Q <= B.

## 6. Results of the cycle (appended; Secs. 1-5 unchanged)

* Theorem KBH (KB_HIGH(p) for every prime p >= 5) has a written proof: proof-KBH.md [W, not yet
  independently reviewed].  Route: segments of w (Lemma OR's observation) + Lemma ZS (pigeonhole on
  p+1 prefix sums over any p consecutive segments) + an explicit greedy theta.  No inherited
  hypothesis, no M0 normalisation needed.
* Exact finite checks: ZS feasible for every window on all KB_HIGH* data at p = 5, 7 and on
  20,000 random p = 11 data; proof replay with raw-DP end-to-end at p = 5..29 (Sec. 5 of
  proof-KBH.md).  SR/BC3/BCG census: out/kbh_*.txt (not needed by the proof).
* Consequence: with ../proof-RUNS.md Sec. 11 and OlsonParity's K0, K1', KB, RUNS(p) reduces
  exactly to MIX_DEF(p) (kappa > B >= 1), owned by OlsonParity in this cycle.
* Safety log (Main's rule of 06:2x PDT): no process in this cycle was stopped with SIGKILL; shell
  limits used `timeout -s TERM`; extreme_test.py used subprocess.run(timeout=400) BEFORE the rule
  arrived, and none of its 4 calls reached the timeout (all finished in < 0.1 s), so no SIGKILL
  was sent.  Earlier cycles: one run of ../check_C0B_ineq.py (p = 13) was interrupted by the
  1800 s cap of the shell tool (signal not recorded); its results were never claimed.

## 7. Review status (appended 2026-10-17 ~07:37 PDT; Secs. 1-6 and the bytes of proof-KBH.md unchanged)

* Hostile review of the frozen proof-KBH.md (sha256 76e32fe5..., recorded in out/summary.txt) by
  Codex CLI gpt-6.1-sol: verdict ACCEPT-WITH-FIXES.  Note:
  /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-kbh-codex-review-v1.note.md
  (receipt, prompt, stdout and stderr alongside).  No fatal or major defect in Lemma HW, Lemma ZS, the
  greedy theta or Theorem KBH; the conditional reduction RUNS(p) <= MIX_DEF(p) through the cited [W]
  results is accepted; the reviewer's own in-memory replays (HW vs raw DP: 729 words, 83,830
  patterns at p = 5, 7, 11; KBH: 540 random words, 6,200 windows, 269,375 subintervals, plus 3
  words violating (D0)) all passed.
* Its only finding is a minor scope correction in a CITED AUXILIARY statement, Lemma H of
  ../../inverse-parity/proof-PAR-K0.md (OlsonParity): replacing the empty/full-pattern conditions by
  min(A, B) <= kappa requires A, B <= 2p-1 (counterexample p = 5, rho_1^10 sigma_0^8).  The fix is
  assigned to OlsonParity; their file is not edited here.
* Why KBH is unaffected: (i) the proof uses only the direction "phi(P) in I(P) mod p for one proper
  pattern P => identity 2p-subword" of Lemma HW, never a converse (review item 2); (ii) in its
  setting A = D + B <= (p-1) + (p-1) = 2p-2 and B = kappa <= p-1, so A, B <= 2p-1 holds anyway
  (Step 0's case A >= 2p is in fact empty; harmless), and therefore the simplified representation
  line of Sec. 2 above ("avoids iff ... for every proper P (B <= kappa holds)") is exact on
  KB_HIGH* data; (iii) the results cited in the Corollary of proof-KBH.md are applied to avoiders,
  which satisfy A, B <= 2p-1 automatically (else rho_{+-1}^{2p} is an identity subword), and the
  odd-segment merge preserves A, B (review item 1).  The parenthetical "(min(A,B) <= kappa)" in the
  Lemma OR recheck of ../proof-RUNS.md Sec. 11 names the simplified form; the exact window I(empty)
  depends only on A, B, H, which the merge keeps, so that recheck is unaffected.
* Code: kbh.cpp and zs.cpp only certify kills; ../hwsingle and ../hw.py test the exact
  empty-pattern window.  Control review_control.py -> out/review_control.txt: for rho_1^10 sigma_0^8
  (p = 5) the exact I(empty) = [-5,-1] contains 0 mod p, ../hw.py reports non-avoiding and the raw DP
  finds the identity subword although min(A,B) <= kappa holds; for the IL counterexample of
  ../mixdef/README.md Sec. 6 (A = 12, B = 7 <= 21) the exact I(empty) = [-3,-2] and I([k]) = [2,3]
  do not contain 0 mod 11, so its stated empty-pattern avoidance is exact (the word is killed by
  other patterns, as recorded there).
