# MIX_DEF_HIGH cycle 2 (task OlsonRunCount): open items (i), (ii), (iii) of ../proof-MH.md Sec. 6

Frozen BEFORE substantive computation: freeze time and SHA-256 of this file are recorded in out/freeze.txt
by the first command after writing it.  Later sections are appended with their host-clock time and are
written before the computations they describe.  Only this directory (c2/) is written; ../ is read-only
except for appended, dated checkpoint lines in ../README.md if needed.  Safety: shell limits only via
`timeout -s TERM`, no Python subprocess timeouts, no SIGKILL, no deletion, <= 2 CPU, <= 4 GiB.

## 1. Representation (unchanged)

All-odd RGR words of length 4p-2, k runs, R = A + B, kappa = p - 1 - H, so R = 2p - k + 2kappa.  For a
proper pattern P with m = m(P) blocks and x := E+(P) = D_P + B (E-(P) = R - x):
   I(P) = [-g_m(R - x), g_m(x)],   g_m(E) = min(p - m, E + m - 1 - kappa, floor(E/2))   (../proof-MH.md (1.1)),
valid for any letters and any B.  "Full window": g_m(x) + g_m(R - x) >= p - 1; it gives an identity
2p-subword (Lemma HW, any length).  A "move" shifts one cut (boundary reflection run) to an adjacent free
reflection run; it toggles exactly one rotation run u and changes x by +-d_u, |d_u| <= r_u.

## 2. Item (i): R = 2p-2 -- statement and proof to be checked (written before any computation)

**Lemma R2.**  Let w be an all-odd RGR word of length 4p-2 (p >= 5 prime) with k >= p+1 runs and
R = 2p-2 (any letters, any B).  Then some pattern has a full window.
Notation.  k = 2kappa + 2 (so kappa >= 2), W := R - 2kappa + 1 = 2p - k + 1 (number of integers in
Z := [kappa, R - kappa]), E := sum_t (r_t - 1) = R - k = W - 3 (total excess), so every run has
r_t <= W - 2 and there are >= k - E = 2k - 2p + 2 >= 4 singleton runs (r = 1, d = +-1).
W = 3 mod 4 if kappa is odd, W = 1 mod 4 if kappa is even.  m0 := floor(kappa/2) + 1;
M := kappa (kappa even), M := kappa + 1 (kappa odd).
Claim 1'' (windows).  If m(P) = m0 and x is EVEN with M <= x <= R - M, then I(P) is full.
 Proof: y := R - x is even and in [M, R - M].  For E in {x, y}: E/2 >= kappa + 1 - m0 (kappa even:
 kappa + 1 - m0 = kappa/2 <= E/2; kappa odd: = (kappa+1)/2 <= E/2 as E >= kappa + 1), so the middle term
 of g_{m0}(E) is >= E/2; and E/2 <= (R - M)/2 <= p - m0 (kappa even: (R - kappa)/2 = p - 1 - kappa/2
 = p - m0; kappa odd: (R - kappa - 1)/2 = p - m0 - 1).  So g(x) + g(y) = (x + y)/2 = p - 1.  []
Claim 2 (path with a reserved singleton).  Let s be a singleton run, s- its predecessor run, s+ its
successor run, and S_{s-2}, S_{s-1}, S_s, S_{s+1} the reflection runs around them (s lies between
S_{s-1} and S_s).  Let P_0 be any pattern with m0 blocks having cuts at S_{s-1} and S_{s+1}, no cut
at S_{s-2} and none at S_s (possible: k - 2m0 >= 2 free sites, see below).  Call c the cut at S_{s-1};
its forward arc is {s, s+}, its backward arc has >= 2 runs, the last one being rho := s-.  Run the
rotation of Theorem ALT (../../proof-RUNS.md Sec. 2) with i* := the cut preceding c: i* first moves to
S_{s-2}, then the cuts i*-1, i*-2, ... (cyclically backwards) each move to the original position of the
next cut, ending with c+ (the cut after c); then c moves to S_{s+1}; finally i* moves to S_{s-1}.  This is
a path P_0, ..., P_N = P_0^c of m0-block patterns, each step toggling one run.  Let tau be the last index
before c moves.  For every j <= tau, c sits at S_{s-1} and S_s is free, so moving c to S_s is a legal
move from P_j: it toggles s, keeps m0 blocks, and changes x by +-1.  After tau exactly three runs are
toggled (s, s+, rho), so |x(P_N) - x(P_tau)| <= 1 + r_{s+} + r_rho <= 3 + ex(s+) + ex(rho) <= 3 + E = W,
where ex(t) := r_t - 1; and x(P_N) = R - x(P_0).
Proof of Lemma R2.
 kappa even (W >= 5): take any singleton s.  If x(P_0) < kappa then x(P_tau) >= R - x(P_0) - W
 >= kappa; let j <= tau be the first index with x(P_j) >= kappa; steps are <= W - 2, so x(P_j) <=
 kappa - 1 + W - 2 = R - kappa - 2, i.e. x(P_j) in Z.  If x(P_0) > R - kappa, symmetrically some j <= tau
 has x(P_j) in Z; if x(P_0) in Z take j = 0.  If x(P_j) is even, Claim 1'' (M = kappa) applies.  If it is
 odd, then x(P_j) in [kappa + 1, R - kappa - 1] (kappa and R - kappa are even), and toggling s gives an
 m0-block pattern with even x in Z: Claim 1''.
 kappa odd, W = 3: then E = 0, all runs are singletons, every step changes x by +-1, the target is the
 single even value kappa + 1 = R - kappa - 1, and any path P_0 -> P_0^c (k - 2m0 >= 1) passes through it
 (x(P_0^c) = R - x(P_0)).
 kappa odd, W >= 7: choose a singleton s with ex(s-) + ex(s+) <= E - 2 (exists, see Claim 3).  Then
 |x(P_N) - x(P_tau)| <= 3 + E - 2 = W - 2.  Use Z' := [kappa + 1, R - kappa - 1] (W - 2 integers, even
 endpoints; a step <= W - 2 cannot jump over it).  If x(P_0) <= kappa then x(P_tau) >= R - kappa - (W - 2)
 = kappa + 1, so the first j with x(P_j) >= kappa + 1 has j <= tau and x(P_j) <= kappa + W - 2 =
 R - kappa - 1; symmetrically if x(P_0) >= R - kappa; if x(P_0) in Z' take j = 0.  If x(P_j) is even,
 Claim 1'' (M = kappa + 1); if odd, x(P_j) in [kappa + 2, R - kappa - 2] and toggling s gives an even
 value in Z'.  []
Claim 3.  If kappa is odd, W >= 7 and there are >= 4 singletons, some singleton s has ex(s-) + ex(s+)
<= E - 2.  Proof: otherwise every singleton's two neighbours carry >= E - 1 of the excess.  If some
singleton has a singleton neighbour, its other neighbour u has ex(u) >= E - 1, and a singleton not
adjacent to u (exists: >= 4 singletons) has neighbours carrying <= 1 <= E - 2 (E = W - 3 >= 4).  Otherwise
all singletons have two non-singleton neighbours, so they sit alone in the q slots between consecutive
non-singleton runs (#singletons <= q); for any singleton the other q - 2 non-singletons carry <= 1 excess
in total, each >= 1, so q <= 3 and #singletons <= 3, a contradiction.  []
Free sites: k - 2m0 = kappa (kappa even) or kappa + 1 (kappa odd), >= 2 as kappa >= 2, so the cut
configuration of Claim 2 exists (four sites fixed, 2m0 - 2 further cuts on the other k - 4 sites).

Check protocol (exact, aids): r2_check.cpp, all all-odd pure/(1,1) words with R = 2p-2 and k >= p+1 (any
B >= 0 with B <= A) at p = 5 and p = 7: (a) Claim 1'' on every pattern with m0 blocks and even x in
[M, R-M]; (b) the construction of Claim 2 executed literally for EVERY admissible singleton s (kappa even:
all singletons; kappa odd, W >= 7: all singletons satisfying Claim 3's inequality) and several cut
completions per s, checking: path legality, |x(P_N) - x(P_tau)| bound, existence of the entry index
j <= tau, availability of the s-toggle, and a full window at the final pattern; (c) Claim 3 (existence).

## 3. Item (ii): R >= 2p+1 with a run |d_u| > 2p-k+1 -- plan (no proof yet)

Facts proved in ../proof-MH.md (Theorem FWH, Claim 1): for R >= 2p every m-block pattern with
m in [m_lo, m*] and x in [kappa, R - kappa] has a full window.  Elementary (to be written): at most one run
u has |d_u| >= W + 1 (W = 2p - k + 1), and then every other run has r_v <= j := R - 2p <= W - 3.  Plan:
(a) data study (big-run words, p = 5, 7 all; p = 11 random): which m and which pattern families
(u as a singleton block, at a block end, outside P, ...) contain a full window; (b) state a candidate
lemma and its proof in an appended dated section BEFORE its exhaustive check; (c) exhaustive check of
the written lemma at p = 5, 7.

## 4. Item (iii): structured Lemma BC chains -- plan

(a) Collect shape statistics of the general Lemma BC chains found by ../bcgchain.cpp-type DP on the p = 11,
13, 17 random and planted sets (number of parts s, part sizes, blocks m per part, adjacency, final part an
interval?, its length and D, position relative to anti runs); (b) state a deterministic construction rule
in an appended dated section; (c) only then test it on ALL p = 5, 7 words with R <= 2p-3 outside ZSI-B and
on the p = 11/13/17 sets; (d) proof attempt only if (c) shows no failure.

## 5. Item (ii): candidate lemma (appended 2026-10-17T09:36 PDT, before its exhaustive check)

**Jump lemma (to be checked).**  Let w be all-odd with k >= 6 runs, R >= 2p+1, and a run u with
|d_u| >= W + 1 (W = 2p - k + 1).  Normalise d_u > 0 by the flip rho_1 <-> rho_{-1} (it maps x to R - x for
every pattern and preserves R, kappa, k, blocks and the zone [kappa, R - kappa]).  Then every other run has
r_v <= j := R - 2p <= W - 3 (excess count: ex(u) >= W, total excess R - k = W + j - 1), so at most one
such u exists.  Let m in [m_lo, m*] with k >= 2m + 1.  If some m-block pattern P_0 with u in P_0 has
x(P_0) <= R - kappa, then some pattern has a full window.
Proof.  If x(P_0) >= kappa, P_0 itself (Claim 1 of ../proof-MH.md Theorem FWH).  Else x(P_0) < kappa; take
the rotation path P_0 -> P_0^c (one free site suffices), which toggles every run exactly once.  Before u is
toggled all steps are <= j < W, so either the zone is met or the value just before the u-step is
<= kappa - 1; the u-step removes u (u in P_0), so the value drops by d_u and stays < kappa; after it all
steps are again <= j < W and the path ends at R - x(P_0) > R - kappa, so it meets the zone.  []
Remaining condition (to be studied, then proved): (STAR) for some m in [m_lo, m*] with k >= 2m+1 there is
an m-block pattern containing u with x <= R - kappa; equivalently an m-block pattern Q with u not in Q and
x(Q) >= kappa.  Hypotheses to be used: A, B <= 2p-1 and min(A, B) <= kappa (otherwise rho_{+-1}^{2p} or the
empty pattern already gives an identity 2p-subword), k >= p+1.
Correction (2026-10-17T09:27 PDT): Sec. 5 above was appended at host clock 09:26:24 PDT (out/freeze.txt); the
"09:36" in its heading is a typo.

## 6. Item (ii): (STAR) data result and constructive candidate (appended 2026-10-17T09:5x PDT, before the
## exhaustive test of the construction)

star_study (out/star_study_p5_p7.txt): (STAR) holds at m = m_lo in all 380 + 83,828 big-run words in range at
p = 5, 7, with margins 0..2 (star_margin).  But m_lo is NOT enough in general: p = 13, k = 16, j = 6,
kappa = 11, B = 7, Omega = alternating aligned/anti singletons (8 + 7), a_u = 17: the best 3 intervals give
D = 3 < kappa - B = 4, while m = 4 works.  So the lemma must let m vary in [m_lo, m_max],
m_max := min(m*, floor((k-1)/2)).
Construction to be tested (flip-normalised d_u > 0; Omega = the path of the other k-1 runs; tau := kappa - B):
Q0 := union, over the maximal beta-free intervals of Omega that contain an aligned run, of the interval from
their first to their last aligned run ("alpha-stretches"); c := their number; N_alpha := aligned letters in
Omega.  Facts: N_alpha = tau + S with S = N_alpha + B - kappa >= k - kappa - 1 >= tau (B >= j + 1 by
A <= 2p-1), so N_alpha >= 2 tau.  Rule: if m_lo <= c <= m_max take Q = Q0 (D_Q = N_alpha >= tau); if
c > m_max take the m_max heaviest stretches (D_Q >= (m_max/c) N_alpha >= tau when c <= 2 m_max, and
c > 2 m_max forces tau < 0); if c < m_lo flip, one at a time, a cheapest run whose two neighbours share its
status (u counts as outside Q) until m_lo blocks.  Output P_0 := complement of Q (contains u) with
x(P_0) <= R - kappa iff D_Q >= tau; then the jump lemma.  Exact test: all big-run words in range at
p = 5, 7 and random ones at p = 11, 13, 17, with end-to-end verification of a full window.
Correction (host clock read 2026-10-17T09:35 PDT): Sec. 6 was appended at 09:34:52 PDT (out/freeze.txt); the
"09:5x" in its heading was a guess and is withdrawn.  The ../README.md Sec. 8 label "09:2x" was written at
09:19:44 PDT.  From now on every time label is copied from a clock read.

## 7. Item (ii): refined construction (appended at the host-clock time recorded in out/freeze.txt right after
## this section; written after bigrun_construct.cpp showed 18 failures of the Sec. 6 flip rule at p = 7,
## all of the form "no single flip available", e.g. k = 9, d = (-1,1,1,-1,-1,1,1,-1, 7))

Use the general target of Theorem FWH Claim 1 (R >= 2p): for m with k - p + 1 <= 2m <= p + 1 and
M_m := max(kappa, 2m - 2, k + 1 - 2m), every m-block pattern with x in [M_m, R - M_m] has a full window, and
the width of that interval exceeds j.  Let c_lo := ceil((k - p + 1)/2).  Facts: x(Q0) = B + N_alpha =
k - 1 + eps (eps := excess of the aligned and anti runs of Omega) >= k - 1 >= M_c for every c >= 1.
 (1) c < c_lo: m := c_lo; flip, one at a time, a run v != u whose two neighbours share its status (always
     exists: otherwise k <= 4b + 1 <= 4 c_lo - 3 < k); each run is flipped at most once, the loss is
     <= (c_lo - c) + eps, and x(Q) >= k - 1 - c_lo + c >= M_{c_lo} (c = 0 forces k >= p+3, c_lo >= 2).
 (2) c_lo <= c <= (p+1)/2: m := c, Q := Q0 (if k = 2c, i.e. k = p+1 and all parts have length 1, use
     m := c - 1 and drop one aligned run: x(Q) >= k - 2 = p - 1 >= M_{c-1}).
 (3) c > (p+1)/2: m := m_max, Q := the m_max heaviest stretches; target lower end kappa.
Then P_0 := Q^c contains u, has m blocks and x(P_0) <= R - M_m, and the jump argument (Sec. 5, with the zone
[M_m, R - M_m]) gives a full window.  Exact test: bigrun_construct2.cpp, all big-run words in range at
p = 5, 7 and random ones at p = 11..19, end-to-end.

## 8. Item (iii): shape-statistics protocol (appended 2026-10-17T09:45:11-0700, before collecting)

bcgstats.cpp: for NMH words with R <= 2p-3 that are NOT covered by interval ZS, run the general Lemma BC DP of
../bcgcheck.cpp (popcount order, predecessor tracking) and print every certificate found as a JSON line:
p, k, R, B, kB, D, the run classes (d values), and for each part in chain order: run set, size, blocks m, D,
lambda, lambda of the complement, whether it is an interval, and whether it contains anti runs.  Sets:
random p = 11 (k <= 15), p = 13 (k <= 16), and the planted boundary violators of ../boundviol.cpp (p = 11,
13).  agg_shapes.py aggregates: number of parts s, sizes, blocks, the final part (interval? length? share of
runs), and the composition of the early parts.  No rule is stated or tested in this step.

## 9. Item (iii): candidate rule RR, frozen before testing (appended 2026-10-17T09:52:18-0700)

Shape statistics (out/agg_shapes.txt, from out/stats_*.jsonl; DP certificates, popcount order, so biased):
BCG-only chains at p = 11 (2,131 words) and p = 13 (816 random + 111 planted) have s = 4 or 5 parts (6 in
4 words); the early parts mostly consist of pairwise non-adjacent runs (size = m in 5,201 of 6,673 early
parts at p = 11), with m - kB in {-1, 0, 1}, and attain lambda = floor((D_P + B)/2) + 1 = D_P + m - kB (both
terms equal in 5,258 of 6,673); the last part attains the floor term and is an interval in 932 of 2,131
(two blocks in 1,040).  Typical: the early parts interleave inside a front segment and the last part is
the rest, e.g. p = 13, k = 16, B = 1, kB = 3: {0,2,5}, {1,3,7}, {4,6,9} (lambda 3 each), {8,10,...,15}
(lambda 5).  Heuristic budget: each part can give at most floor((D_P + B)/2) + 1, so roughly
s >= (k - 2kB + 2)/(B + 2) parts are needed.

RULE RR (round robin).  lambda(P) := min(p - m + 1, D_P + m - kB, floor((D_P + B)/2) + 1) (Lemma H with
beta = 0).  Scan the tuples (s, L, j0, o) in the order s = 3, 4, ..., k; L = s-1, ..., k-1; j0 = 0, ..., k-1;
o = +1, -1.  For a tuple put J = (j0, j0 + o, ..., j0 + o(L-1)) mod k, assign its i-th run (i = 0..L-1) to
P_{1 + (i mod (s-1))}, and P_s := J^c.  RR succeeds on the word if some tuple gives a chain (P_1..P_s)
satisfying Lemma BC (a), (b), (c) exactly; its output is the first such tuple.  Test (rrchain.cpp): ALL NMH
words with R <= 2p-3 at p = 5, 7 (ZSI-B words reported separately), the random sets of Sec. 8 (p = 11 seed
1101, p = 13 seed 1301), planted sets (p = 11 seed 1111, p = 13 seed 1313, p = 17 seed 1717), and random
p = 17 words (seed 1701).  Failures of RR are failures of this family only (not counterexamples).

## 10. RR results and the large-k question (appended 2026-10-17T09:55:31-0700, before running bcgbig)

RR results (out/rr_*.txt, 2.6 s total): p = 5: 28/28; p = 7: 39,985/40,051 non-ZSI-B words (all 66 failures
k = 11, B = 1, kB = 3, R = 11, i.e. all runs singletons with one anti run) and 11,590/11,590 ZSI-B words;
p = 11 random: 7,121/7,720 (+1,286/1,286 ZSI-B); p = 13 random: 1,635/1,683 (+324/324); planted p = 11, 13,
17: 400/400 each; p = 17 random (k = 18..31): 683/1,037 (+52/52).  RR fails systematically when kB is large
relative to the front, e.g. the p = 7 failures need three interleaved classes covering the whole cycle
(a flat 3-colouring BC3 certificate), which RR cannot express (its last part is a nonempty interval).
The earlier census never sampled k >= 16 at p = 11 or k >= 17 at p = 13, where kB and k - p can be larger.
Experiment bcgbig.cpp (rrchain.cpp + ../bcgcheck.cpp DP + ../mhc.cpp exact phi DFS over all patterns, node
limit 4e9): random NMH words with R <= 2p-3 at p = 11 (k = 16..19, seed 1119, 400 draws) and p = 13 (k =
17..19, seed 1319, 400 draws); for every word where RR fails run the DP; if the DP finds nothing run the
exact DFS.  An avoider reported by the DFS is only a candidate until replayed by the RAW ordered-product DP.

## 11. Finding: Lemma BC cannot settle item (iii) (appended 2026-10-17T10:00:50-0700)

bcgbig (out/big_p11.txt, out/big_p13.txt): RR failed on 21/57 (p = 11, k = 16..19) and 55/166 (p = 13,
k = 17..19) words; the exact DP found a Lemma BC certificate for 20 resp. 52 of them, and NO certificate
for 1 resp. 3 words, all of the form "every run a single letter (R = k), one anti run, B = 1, kB = 4"
(p = 11, k = 16; p = 13, k = 18); for each the exact phi DFS over all patterns finds no avoider.
nobc_bound.py (out/nobc_bound.txt): for all-singleton words the type-count bound
MAXSUM = max over partitions of sum UB(j, e), UB(j, e) = max_{1<=m<=j+e} min(p-m+1, j-e+m-kB,
floor((j-e+B)/2)+1), is <= p (so condition (a) of Lemma BC fails for EVERY ordered partition) for
B = 1, kB = 4 at every tested p (11, ..., 31) and for many more classes at p >= 17 (marked * there).
Next (frozen now, before running): (1) famdfs.py, an independent Python implementation of the exact
avoider search written from Lemma H (../../../inverse-parity/proof-PAR-K0.md Sec. 1), on the two NO_BC
families; (2) a written proof of Lemma NOBC (k = p + 5, all runs single letters, one anti run, p >= 11);
(3) report to Main: the BC-chain route for (iii) is provably incomplete for p >= 11.

## 12. Bounded LP/Farkas exploration on W(13, 4) (appended 2026-10-17T10:06:39-0700; time box until 11:10 PDT, per Main)

Word: p = 13, k = 18, every run one letter, anti run at position 0 (B = 1, kappa = 5, kB = 4).
Lifted system: integer lifts x_t of u_t; a pattern Q is CERTIFIED if Q is a singleton or Q = Q' u {t} with
Q' certified and [lo(Q') + lo(t), hi(Q') + hi(t)] inside [1 - lambda(Q^c), p + lambda(Q) - 1], where
lo(Q) = lambda(Q), hi(Q) = p - lambda(Q^c); then X_Q := sum_{t in Q} x_t lies in [lo(Q), hi(Q)] (Claim of
Lemma BC).  LP: real x, all certified constraints, X_[k] = p z for an integer z.  lpcert.py computes the
certified family (subset DP), solves the LP exactly with z3 (QF_LRA) for every z with p z in the LP range
of X_[k], and, if every case is infeasible, extracts an unsat core and exact Farkas multipliers (z3 LRA on
the dual) and reports their shape (pattern sizes, blocks, positions).  Any candidate certificate is
re-checked by an independent exact verifier (rational arithmetic, fractions) before being reported.  A
feasible LP means only that this family is too weak (no claim about avoiders).

## 13. LP exploration, interim results (appended 2026-10-17T10:29:03-0700; cutgen.py was launched just before this note, at the
## time recorded in out/freeze.txt; it computes the SAME Sec. 12 LP by constraint generation)

* lpcert.py: on W(11, 4) and W(13, 4) every proper pattern is certified by singleton extension (65,534 resp.
  262,142 patterns) and the real LP is already infeasible WITHOUT the condition X_[k] = 0 (mod p)
  (out/lpcert_p11.txt 36 s; out/lpcert_p13.txt 942 s, 3.5 GB peak RSS -- too close to the 4 GiB cap to repeat
  at larger k, hence constraint generation for p = 17).
* farkas.py / farkas_win.py: exact Farkas certificates, independently re-checked in fractions (multipliers,
  coverage equations, bounds recomputed, every singleton-extension chain re-verified):
  p = 11: 11 constraints, all inside runs 0..9 (out/farkas_p11.txt): upper bounds on 4 sets of size 7-9
  containing the anti run (m <= 2), lower bounds on 7 sets of size 4-5 with 3-4 blocks; totals 170 vs 169.
  p = 13: LP restricted to runs at cyclic distance <= r from the anti run is feasible for r = 5, 6 and
  infeasible for r = 7; certificate with 14 constraints: upper bounds on {0..7, 11..13} (size 11, m = 2,
  bound 8, weight 76) and {0..7, 11..14, 16} (size 13, m = 3, bound 9, weight 81); lower bounds on 12 sets
  of size 4-5 with 3-4 blocks; totals 1338 vs 1337.
  Shape in both: a fractional partition of large sets U around the anti run (upper bound p - lambda(U^c),
  U^c an efficient all-aligned set) into small multi-block sets P with lambda(P)/|P| near 4/5 (lower
  bounds); the multipliers are irregular (not position- or type-uniform).

## 14. Lemma NOLP (real LP cannot kill W(p,4) for p >= 17) and exact avoider checks (appended 2026-10-17T10:31:52-0700)

Results since Sec. 13: cutgen.py found exact, re-checked Farkas certificates at p = 11 (1.6 s) and p = 13
(10.7 s) (out/cutgen_p11.txt, out/cutgen_p13.txt); at p = 17 it keeps finding violated constraints.
Observation (proof to be written in proof-NOBC.md Sec. 5): put phi_t = 4/5 on aligned runs, -1/5 on the anti
run.  The per-part bound of Lemma NOBC says lambda(Q) <= phi(Q) for EVERY proper Q, and phi([k]) =
(4(p + kB) - 1)/5.  So x_t := phi_t + (p - phi([k]))/k satisfies every lifted constraint
lambda(Q) <= X_Q <= p - lambda(Q^c) and X_[k] = p as soon as p >= 4kB - 1 (kB = 4: p >= 17).  Hence no real
Farkas combination of window constraints kills W(p, 4) for p >= 17; a certificate must use integrality.
With X_[k] = p the constraints of Q and Q^c coincide, so (when every pattern is certified) "avoider" <=>
"an integer point x with sum x = p and x(Q) >= lambda(Q) for all proper Q", an integer core of the set
function lambda (real core nonempty by Bondareva-Shapley iff no fractional partition beats p).
Exact check (ran just before this note, out/famdfs_p17.txt): famdfs.py p = 17, k = 22: NO avoider
(3,082,898 checks).  Next, frozen now: famdfs.cpp (port of famdfs.py) validated against famdfs.py at
p = 11, 13, 17 (no avoider) and the shrink controls, then run at p = 19 (k = 24) and p = 23 (k = 28).  Any
avoider found must be replayed by the RAW ordered-product DP (../../../code/was_verify.py dp_has) before
being called one.

## 15. Integer-core test with small patterns only (appended 2026-10-17T10:35:24-0700, before running intsmall.py)

nolp_check.cpp (out/nolp_check.txt): the explicit Lemma NOLP point satisfies all lifted constraints on ALL
patterns with total p for (p, kB) = (17,4), (19,4), (19,5), (23,4), (23,5), (23,6) (0 violations) and
violates them at p = 11, 13 (c < 0); lambda(Q) <= phi(Q) holds on all patterns in every case.
famdfs.cpp: NO avoider in W(19, 4) (15,714,162 checks) and W(23, 4) (526,419,554 checks).
Question: is integrality plus SMALL patterns enough?  intsmall.py: z3 integer feasibility of
{x in Z^k : sum x = p, x(Q) >= lambda(Q) for all proper Q with |Q| <= s or |Q| >= k - s} (Lemma CORE form;
dropping constraints only enlarges the set, so INFEASIBLE is a valid kill when every pattern is certified,
and FEASIBLE says nothing), for W(p, 4), p = 11, 13, 17, 19, 23 and s = 2, 3, 4; for infeasible cases a
deletion-minimal core is printed (shape only; any claimed proof will be written by hand and re-checked).

## 16. Close of the bounded LP exploration (appended 2026-10-17T11:11:25-0700)

Best shape found: NOT a real Farkas certificate (impossible for W(p, 4), p >= 17, by Lemma NOLP,
proof-NOLP.md; exact check nolp_check.cpp), but an INTEGER argument on lifted constraints of patterns with
<= 3 runs: Theorem W4 (proof-W4.md [W]): no word of W(p, 4) is an avoider, every prime p >= 11.  Ingredients:
Lemma L lifts (singleton-extension certification = Lemma BC step (b) with a one-run Y), the interval chain
I_1 c ... c I_{p+4} to pin X_[k] = p, then a three-step integer case analysis (no negative aligned lift;
zero lifts pairwise adjacent; x_0 in {-4,-3,-2} each contradicted by an anti pair or anti triple).
[F] chaincheck.py (out/chaincheck.txt): every certification step and lambda value used, primes 11..199.
intsmall.py (out/intsmall.txt): integer infeasibility already with |Q| <= 3 at p = 11, 13, 17 (s = 2 is
feasible); minimal cores at p = 11, 13 use only triples; p = 17 core minimisation and p = 19, 23 timed out
(UNKNOWN).  Lemma CORE (proof-NOLP.md) restates avoidance as an integer point of the lambda-core with total p
when all patterns are certified.  RUNS(p) is not claimed.
