# MIX_DEF_HIGH cycle: kappa > B >= 1 with at least p+1 odd reflection runs (task OlsonRunCount)

Frozen BEFORE substantive computation; freeze time and SHA-256 of this file and of the census code
are recorded in out/freeze.txt by the first command of the cycle.  This directory is new (created
2026-10-17T08:18 PDT); nothing outside it is edited.  Cited, not rerun: ../proof-RUNS.md (Secs.
2, 9-12: Theorem ALT, C0-B', Lemma A1, Corollary B0, Lemma M0), ../kappaB-high/proof-KBH.md
(Theorem KBH, Lemma ZS; reviewed ACCEPT-WITH-FIXES, the fix concerning only the auxiliary Lemma H),
../mixdef/README.md Sec. 6 (refuted lemma IL; that route is not used), and OlsonParity's Lemma OR
(../../inverse-parity/proof-PAR-Kplus-partial.md Sec. 1).

## 1. Target

MIX_DEF_HIGH(p): every RGR word w of length 4p-2 with F, R >= 1, normalised A >= B, with
1 <= B < kappa := p - 1 - H and with o_F >= p+1 odd reflection runs has an identity 2p-subword.
(No inherited hypothesis.)  Together with OlsonParity's current o_F <= p half it would give
MIX_DEF(p); RUNS(p) is NOT claimed unless both halves are proved and reviewed.

Reduction (cited, all [W]): if A >= 2p, rho_1^{2p} is an identity subword.  Lemma OR replaces w by
the all-odd word w~ with k~ = o_F runs and the same A, B, kappa (w avoids => w~ avoids).  Lemma M0
(remove rho_1 rho_{-1} from one run with r >= 3, insert sigma sigma) keeps k, o, kB := kappa - B and
all-oddness and shrinks every window (incl. the empty pattern); iterate until every run is pure or
a (1,1)-pair; if B drops to 0, Corollary B0 / C0-B' / A1 / the trivial cut apply (kappa = kB >= 1,
no inherited hypothesis).  k = 2p-1 is Theorem ALT.  Hence it suffices to prove:

NMH(p): every all-odd RGR word of length 4p-2 with p+1 <= k <= 2p-2 runs, every run pure or a
(1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p-1, has an identity 2p-subword.

Parameters in NMH: kB = kappa - B >= 1, D := A - B = 2p - k + 2 kB, R = A + B = 2p - k + 2 kappa,
F = k + 2H.

## 2. Frozen representation (Lemma HW with the CORRECTED Lemma H condition)

Lemma HW (../README.md Sec. 2, exact, all patterns incl. empty/full): w avoids iff
phi(P) notin I(P) = [-g_P(E-), g_P(E+)] (mod p) for every pattern P.  Corrected Lemma H (review
olson-kbh-codex-review-v1, item 1): if A, B <= 2p-1, the empty and full patterns kill iff
min(A, B) >= kappa + 1.  In NMH (A <= 2p-1, B <= kappa - 1) they never kill, and for all-odd words
(beta = 0, h = H, E+ = D_P + B):
   U_P = min(p - m, D_P + m - 1 - kB, floor((D_P + B)/2)),  L_P = U(m, D - D_P),  m = m(P),
   I(P) = [-L_P, U_P];   w avoids iff phi(P) notin I(P) (mod p) for every proper nonempty P.
"Full window": U_P + L_P + 1 >= p.

## 3. Statements to test (exactly, before any proof attempt) and the proved obstruction to record

T1 (Lemma A1-mix): R = 2p-1 => some full window (expected from the proof of ../proof-RUNS.md
    Lemma A1 with x = E+(P) = D_P + B and steps |d_u| <= r_u).
T2: R >= 2p => some full window?    T3: R = 2p-2 => some full window?
T4: R <= 2p-3 has no full window (immediate: U + L <= R/2).  For these: does interval ZS
    (../kappaB-high/proof-KBH.md Lemma ZS, any window of p consecutive runs) work when kB = 1 and
    k = p+1?  Which pattern families are needed (intervals only / m <= 2 / all)?
T5: flat 3-partition Lemma BC certificate (s = 3, arbitrary parts) on data without full window.
T6: NO avoider at all (p = 5, 7 exhaustive; p = 11, 13 random).  Any claimed avoider must be
    confirmed with the raw ordered-product DP (../hw.py dp_has, in-process).
OBS (to be written as a proved lemma, phi-independent): for kB >= 2 no fixed-target pigeonhole
    certificate (chain prefix sums as in Lemma ZS, or Davenport zero-sum subsets, over n disjoint
    groups of runs) exists, because the reflection terms force (n-1) kB + n + 1 <= 2p, i.e. n < p.
A failure of T1-T5 is a failure of that statement/certificate only, not of NMH.

## 4. Protocol

mhc.cpp (this directory): enumerates NMH data (rotation classes of (r, l), all pure/(1,1) splits
with 1 <= B <= kappa-1, B <= A <= 2p-1; exhaustive at p = 5 (k = 6..8) and p = 7 (k = 8..12);
random at p = 11, 13) and reports per class of R: FULL, ZSI (Bellman-Ford, exact windows), BC3
(k <= 13), and an exact phi-search with pattern families m <= 1, m <= 2, all (DFS as in
../hwsearch.cpp).  Single-threaded, <= 2 CPU total, <= 4 GiB, chunks <= 30 min, shell limits only
via `timeout -s TERM`; no Python subprocess timeouts; no deletion; outputs in out/.

## 5. Results of the cycle (appended after the freeze; Secs. 1-4 unchanged)

Written results: proof-MH.md ([W] = written proofs, not yet independently reviewed; [F] = exact checks).
* Lemma OBS [W]: for kappa - B >= 2 no fixed-target pigeonhole certificate exists (any groups, any
  targets, any zero-sum family containing a partition of the index set and the whole set; for n = p
  every zero-sum family contains all singletons and the whole set).  Covers Lemma ZS along any chain
  and its Davenport version; for kappa - B = 1 such certificates are rigid (equality case).
* Theorem FWH [W]: every all-odd word with R in {2p-1, 2p} (and k >= 6 for R = 2p) has a full window;
  same for R >= 2p+1 if every run has |d_u| <= 2p-k+1.  [F] Claim 1 checked on 871,600,076 patterns
  (p = 7, all all-odd pure/(1,1) words with k >= p+1, R in {2p-1, 2p}), 0 failures.
* Lemma ZSI-B [W]: for k = p+1, kappa - B = 1, interval ZS applies iff every proper cyclic interval has
  D_Q <= min(2|Q| + B, |Q| + p - 1).  [F] equivalence checked on all boundary words at p = 5 (2,984) and
  p = 7 (857,281), 0 mismatches; exact p = 11 word violating it (killed by a flat 3-partition BC).
* Census [F] (out/mhc_*.txt, out/mhc_aggregate.txt; label "<=-3" in mhc.cpp output means R <= 2p-4):
  no avoider among 6,438 (p = 5, all), 3,317,913 (p = 7, all), 3,000 (p = 11) and 1,500 (p = 13)
  NMH words; R >= 2p-2 always has a full window; for R <= 2p-3 every sampled word at p = 11, 13 has a
  general Lemma BC certificate (bcgcheck.cpp: 788 + 8,945 words at p = 11, 340 at p = 13, k <= 15/16).
* Open (proof-MH.md Sec. 6): (i) R = 2p-2, (ii) R >= 2p+1 with a big run, (iii) R <= 2p-3 except the
  ZSI-B case.  (iii) is the core; RUNS(p) is not claimed.
* Coordination: OlsonParity owns o_F <= p (inverse-parity/mixdef-low/); notation agreed (their g = kB).
* Safety log: every computation was started by the shell with `timeout -s TERM`; no Python subprocess
  timeouts, no SIGKILL, no deletion, nothing outside this directory edited; all binaries are
  single-threaded (/usr/bin/time: bcgcheck p = 13 run 22.24 s real, 22.20 s user).  Note: the bash
  `time` keyword once reported 1m56s "user" for a 4.8 s bcgcheck run whose own /usr/bin/time profile on
  a smaller input is 1 CPU; that "user" figure is therefore not attributed to this process.

## 6. Additions (appended after host clock 2026-10-17T08:52 PDT; Secs. 1-5 unchanged)

* proof-MH.md Sec. 4: Lemma V [W] ((4.1)-violators in the boundary case need >= 2 anti runs and B >= 2)
  and Lemma BC3I-B [W] (an interval flat 3-partition certificate exists iff the cycle splits into three
  arcs with D <= B + 2); planted violators (boundviol.cpp): p = 11: 400/400 killed by flat 3-partitions
  (160 by interval ones); p = 13: 300 by flat 3-partitions, 100 by longer Lemma BC chains, 0 without a
  Lemma BC certificate.  A p = 17 planted run was stopped by `timeout -s TERM` (3^17 assignments per word
  in the flat 3-partition search); it is not used.
* proof-MH.md Sec. 3: [F] Claim 1 of Theorem FWH for R >= 2p and every m in [m_lo, m*]:
  2,143,400,456 patterns at p = 7, 0 failures (fwh_c_check.cpp, out/fwh_c_check_p5_p7.txt).
* Open part unchanged (proof-MH.md Sec. 6).

## 7. Correction (appended 2026-10-17T09:08 PDT; earlier sections unchanged)

Sec. 6 above says the p = 17 planted-violator run "was stopped by `timeout -s TERM` ... it is not used".
That is wrong: the run finished (683.9 s, under its 900 s TERM limit).  It was rerun with saved output
(out/boundviol_p11_p13_p17.txt, 09:02-09:07 PDT, same seeds, identical results): p = 17, 400 planted
violators, interval split in 120, flat 3-partition Lemma BC in 299, longer Lemma BC chains in 101,
0 without a Lemma BC certificate.  proof-MH.md Sec. 4 now cites these numbers.

## 8. Checkpoint (appended 2026-10-17T09:2x PDT)

Cycle 2 started in c2/ (frozen c2/README.md, hash in c2/out/freeze.txt): Lemma R2 (item (i)) written with
proof before any computation; items (ii), (iii) planned.
Checkpoint 2026-10-17T09:5x? -- see c2/out/freeze.txt for exact times: Lemma R2 checked (0 failures, p = 5, 7);
item (ii) jump lemma + refined construction written, under test.
Correction (2026-10-17T09:41:41-0700): the checkpoint line above (labelled '09:5x?') was written at 2026-10-17T09:41:30-0700.
Checkpoint 2026-10-17T09:44:39-0700: c2/proof-C2.md frozen (Lemma R2, Lemma BR, Theorem FW+); hashes in c2/out/freeze.txt. Next: item (iii).
