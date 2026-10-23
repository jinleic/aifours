# Frozen representation for the no-window RGR residual: window-avoidance system (WAS)

Lane MathOlson.  FROZEN before any WAS computation (host clock read
2026-10-17T00:13:00-07:00 just before writing).  Builds only on proof-GR.md
(Lemma GR, hostile-reviewed).  Later edits go to an appended, dated section.

## 1. Representation (exact)

RGR word (proof-GR.md Sec. 1): x = 1, cyclic runs R_1 S_1 ... R_k S_k, R_i with a_i
letters rho_1 and b_i letters rho_{-1} (order inside R_i irrelevant), S_i =
sigma_{y_i}^{l_i}.  Put theta_i := y_{i-1} - y_i (y_0 := y_k), so sum_i theta_i = 0,
and every theta in Z_p^k with zero sum arises (y_i = y_0 - theta_1 - ... - theta_i).
For P subset of [k] let z_P be the pattern z_i = +1 iff i in P, and
W(P) := Ach(z_P) mod p  (Ach as in proof-GR.md Sec. 2; a set of even integers).

**Lemma WAS.**  The RGR word with run data (a, b, l) and reflection values y has NO
identity 2p-subword iff
    for every P subset of [k]:  sum_{i in P} theta_i  is not in  W(P)   (in Z_p).
Proof.  Lemma GR: a solution exists iff some z has t in Ach(z) with
t = tau(z) (mod p), tau(z) = -2^{-1} sum_i z_i (y_i - y_{i-1}) = 2^{-1} sum_i z_i theta_i.
With P = {z_i = +1}: sum_i z_i theta_i = sum_P theta - sum_{P^c} theta
= 2 sum_P theta (as sum theta = 0), so tau(z_P) = sum_{i in P} theta_i.  []

Consequences used for certificates:
* P = empty: tau = 0, value-independent.  Cyclic interval P = {i, ..., j}:
  tau = y_{i-1} - y_j (telescoping; one bracket sigma_{y_{i-1}} ... sigma_{y_j}).
  A union of m disjoint cyclic intervals has 2m pattern boundaries.
* Complement symmetry: W(P^c) = -W(P) and sum_{P^c} theta = -sum_P theta, so
  the constraints for P and P^c coincide (2^{k-1} distinct constraints).
* The run data (k; a_i, b_i, l_i) fixes every W(P); the reflection values enter
  ONLY through theta.  So "the RGR words with run data D are all solvable" is the
  statement "the WAS of D has no solution theta" -- a finite covering problem in
  Z_p^{k-1} per run datum, and a sumset problem in general.

## 2. Attack protocol (frozen)

Q1 (counterexample or certificate, exact): for run data D at length 4p-1 passing
the PROVED value-independent filters [E, P, Davenport-alpha (F >= 2), T0
(>= 2 odd reflection runs), Doubling j = 0 (a_i, b_i <= p-1), same-letter pairs
(sum floor(l_i/2) <= p-1), no full window (Cor. GR-W), 0 and +-2p not in
W(empty)], decide whether the WAS has a solution theta, by DFS over theta_1, ...,
theta_{k-1} (theta_k = -sum) checking every P subset of the assigned indices.
Any solution = candidate counterexample; it must be re-verified by an exact raw
ordered-product DP on the explicit word before any report.
Q2 (structure): for data D with no WAS solution, compute a minimum family of
patterns P certifying infeasibility, and test whether {empty} + cyclic intervals
(+ complements) always suffice; if so, attempt an all-p proof of the
"interval covering lemma" via the telescoping form y_{i-1} - y_j.

Controls (required before interpreting Q1/Q2):
* positive: at length 4p-2 the WAS solver must find NO instances (avoiders exist);
  at p = 5 each solver NO instance must be confirmed by raw DP, and the solver's
  WAS-solution set at length 18 must agree with an independent brute force over
  all reflection values for the same run data;
* negative: p = 5 at length 19 must yield no WAS solution (D10 has no avoider,
  finite-exact, README 5.1);
* mutation: enlarging one forbidden set W(P) by one residue must create spurious
  solutions that raw DP rejects (shows the check is load-bearing).

Scope: p = 5 (lengths 18, 19) and p = 7 (length 27), all run data up to cyclic
rotation, chunked and checkpointed (<= 30 min per chunk, <= 4 workers); p = 11
only for structurally selected families.  A WAS search is finite-exact for the
listed run data only; it is not a proof for other p.

## 3. Erratum to the frozen protocol (dated 2026-10-17T00:37 PDT, after the p = 5 runs)

Sec. 2 "mutation" says "enlarging one forbidden set W(P)"; enlarging a forbidden set
can only REMOVE solutions.  The control actually run (code/was_search.cpp, mut = 1)
SHRINKS every non-full window by its top element (weakens the constraints), which
must create spurious "solutions" that raw DP rejects.  No other protocol change.

## 4. Results (finite-exact unless marked; host clock read 2026-10-17T00:37:01 PDT)

Code: code/was_search.cpp (sha256 21ac8a2d...; binaries code/was_search 2916c2c7...
used for the p = 7 N = 27/26 runs, built from this source before the `fam`
argument was added -- fam = 0 default is identical; code/was_search_fam 27885769...
built from the current source); verifier code/was_verify.py (38ccd5ee...), whose DP
is written independently of coverage_all.py.  Outputs in evidence/was/.

p = 5 (D10):
* N = 19, all 3,825,737 rotation-canonical run data (filters off): 0 WAS solutions,
  i.e. every RGR word of length 19 is solvable (agrees with the exhaustive D10
  result; independent method).
* N = 18 (positive control, filters off): 210 run data have WAS solutions, each with
  exactly one theta; all 420 emitted words are avoiders by the fresh DP.  Their 105
  canonical class keys (rotation x automorphism) EQUAL the key set of the 3730
  exhaustive D10 length-18 avoiders (evidence/groups/D10.L18.avoiders.txt,
  converted from the table's "a then b" convention by reversal; every one of the
  3730 converted words was re-checked as an avoider and every one is RGR).
* Mutation (mut = 1, N = 19): 35 spurious run data, all 35 rejected by DP.
* Certificate families: patterns with Phi <= 2 (empty + single brackets) do NOT
  suffice (1247 run data at N = 19, all with k = 8, 9 runs); Phi <= 4 (at most two
  brackets) suffices for every run datum (filters on and off).

p = 7 (D14):
* N = 27 (target), proved filters on (E, P, Davenport-alpha, T0, pairs, Doubling
  j = 0): 4,086,788,695 rotation-canonical run data, every theta in Z_7^{k-1},
  k = 1..13: 0 WAS solutions (810.2 s).  With Lemma GR (proof) this is a
  FINITE-EXACT THEOREM: every RGR word of length 27 over D14 has an identity
  14-subword.  (Run data removed by the filters are solvable by the cited proved
  results; run data with a full window by Cor. GR-W.)
* N = 26 (positive control, filters off): 3738 run data with WAS solutions; all
  3738 emitted words are avoiders by the fresh DP.  k <= 7 = p for all of them.
* Structure of ALL avoider run data at length 4p-2 (p = 5: 210, p = 7: 3738): every
  reflection run odd, every rotation run odd and constant (a_i b_i = 0), all
  brackets equal (theta_i - (a_i - b_i) constant mod p), and k <= p.
  (theta checked for the emitted one per run datum at p = 7; all theta at p = 5.)

### 4.1 More p = 7 results (host clock 2026-10-17T00:50:26 PDT)

* Exact size of the no-window residual decided by the WAS DFS (run data passing the
  proved filters, no full window, 0 not in W(empty)): p = 5: 2,053 run data;
  p = 7: 3,427,632 run data (k = 5..11: 7,560 / 155,421 / 764,340 / 1,352,810 /
  880,298 / 245,049 / 22,154).  All are WAS-infeasible, i.e. solvable.
* Mutation (mut = 1, N = 27, k = 5..8, filters off): 12 spurious run data, all 12
  rejected by the fresh DP (they contain identity 14-subwords).
* Certificate families at N = 27: Phi <= 4 (at most two brackets) leaves 14,126 run
  data uncertified (k = 12, 13); Phi <= 6 (three brackets) certifies all.  With
  p = 5 (one bracket fails, two suffice) this is consistent with (p-1)/2 brackets
  being needed: the typical uncertified words are alternations of rotation
  singletons with 2p reflections in 2p-1 runs (one run of length 2), e.g. p = 7:
  a = (0^10,1,1,1), b = (1^10,0,0,0), l = (1^12,2).  Observation only (two primes);
  no all-p statement is claimed.
* Second route to the p = 7 theorem: INV(7) (repr data above) + Theorem DR
  (proof-DR.md) re-derive "every RGR word of length 27 is solvable" independently
  of the N = 27 search.

### 4.2 Complete extremal structure at p = 7 (host clock 2026-10-17T01:01:05 PDT)

`was_search_fam 7 26 1 13 all 0 0 0` (filters off, every theta printed;
evidence/was/p7_N26_all.jsonl sha256 231617f9...; 518.8 s): 3738 run data, each with
EXACTLY ONE theta.  Every one of the 3738 avoiders of RGR_26(7) (up to rotation and
the automorphisms used) has: all runs odd, every rotation run constant, all
brackets equal (theta_i - (a_i - b_i) = c for all i) with c = +-1 (i.e. +-x), and
k <= p.  Same at p = 5 (210 run data, one theta each).  Conjecture INV+(p): this is
the exact shape of every avoider in RGR_{4p-2}(p) for every prime p >= 5 (stronger
than INV(p)).  Finite-exact at p = 5, 7 only.

### 4.3 Conjectured exact shape of RGR avoiders at length 4p-2 (data p = 5, 7)

With c = +-1 the common bracket, call rotation run i aligned if c * eps_i = +1
(eps_i = sign of its constant letter), anti-aligned otherwise.  Every avoider run
datum at p = 5 (210) and p = 7 (3738) satisfies exactly one of
 (I)  no anti-aligned run, R = R_aligned in [p, 2p-1], F = 4p-2-R in [2p-1, 3p-2];
 (II) R_aligned = 2p-1, R_anti in [1, p-1], F = 2p-1-R_anti in [p, 2p-2];
in addition to: all runs odd, rotation runs constant, all brackets equal to rho_c,
k <= p.  Counts per (R_aligned, R_anti, F) are in evidence/was/p{5,7}_N*_all.jsonl
(e.g. p = 7: (7,0,19): 264, ..., (13,0,13): 2, (13,1,12): 12, ..., (13,6,7): 2).
Status: conjecture INV+(p); finite-exact only at p = 5, 7; no proof.

## 5. Review fix (dated; Claude claude-opus-5-5 max, review/claude-DR-math/receipt.json)

Lemma WAS, hypotheses stated explicitly: the RGR word has F, R >= 1 (so k >= 1),
rotation letters normalised to x = 1 (rho_1, rho_{-1}) with y the correspondingly
normalised reflection values, and it may have ANY length N = F + R: Lemma GR's
proof never uses N = 4p-1 (proof-GR.md Sec. 4), which is what licenses the WAS
runs at N = 4p-2 used for INV(5), INV(7).  Verdicts of the focused review: Lemma
WAS correct with this minor fix; Theorem DR correct; Corollary DR' correct.  The
earlier full review attempt (review/claude-WAS-DR) timed out without a verdict, so
the code-fidelity and finite-exact claims of Sec. 4 remain unreviewed.
