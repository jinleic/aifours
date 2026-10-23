# PAR(p): assembly of the proved pieces, the finite cases, and the exact open condition (r1)

Owner OlsonParity2.  Version r1, written after host clock 2026-10-17T17:46:43-07:00; supersedes
proof-PAR-assembly.md (sha256 95e79ed3...6869, kept unchanged) after the parent's position statement and the
Claude review of proof-Rstar-partial-v2.md (MINOR-1 wording of the residual Corollary; MINOR-6b pruning
soundness; Observation MIX_low(5)).  Status: assembly [W] (citations of frozen files plus the short arguments
here); the finite part [F] is conditional on the census programs, whose code fidelity is UNREVIEWED.  Nothing
here proves PAR(p) for all primes, RUNS(p), INV, INV* or ordered Olson for D_{2p}; ordered Olson for D_{2p}
would additionally need RUNS(p) and INV*(p).

## 1. Statements

PAR(p) (../../../proof-INV-reduction.md Sec. 2): every inherited avoider w' in RGR_{4p-2}(p) with k <= p
has all 2k runs odd.
MIX_low(p) (../README.md Sec. 1, frozen 06:27:02): every RGR word of length 4p-2 with all k reflection runs
odd, k <= p, A >= B >= 1, B < kappa <= k-1, has an identity 2p-subword.

**Theorem PA (all primes p >= 5).**  If no interval-feasible normalized MIX_low data at p lie in R4(p)
(c2/proof-Rstar-r3.md Sec. 6; R4 is contained in R***), then MIX_low(p) holds, and MIX_low(p) implies PAR(p).
**Theorem P5 [W].**  MIX_low(5) and PAR(5) hold (written proofs only).
**Statement PF [W+F, conditional on unreviewed census code].**  MIX_low(p) and PAR(p) hold for
p = 7, 11, 13, 17.

## 2. Proof of Theorem PA (chain of citations)

(a) PAR(p) <= Theorem K0 (kappa = 0) and K+_viol(p) (../../proof-PAR-K0.md Sec. 3, 5;
    ../../proof-PAR-Kplus-partial-r2.md Sec. 4).  K+_viol(p) is proved there for kappa = 1 (Theorems K1, K1'),
    for B = 0 (Proposition S1', Lemma A1', the trivial cut, via Lemma OR) and for B = kappa (Theorem KB); the
    range 1 <= B < kappa reduces by Lemma OR (all o_F reflection runs of w~ odd, k(w~) = o_F <= k <= p, same
    A, B, kappa; (V) gives kappa <= o_F - 1) to MIX_low(p).
(b) MIX_low(p): if A >= 2p, rho_1^{2p}.  Otherwise Lemma M0 (../../../inverse-run-count/proof-RUNS.md Sec. 12;
    rechecked: for every pattern E+ and E- drop by 1 and h rises by 1, so g_P'(E-1) <= g_P(E) and every half
    window shrinks; k, d_t, parities, phi unchanged) makes every run pure or a (1,1)-pair; if B reaches 0,
    Proposition S1' / Lemma A1' / the trivial cut finish (kappa - B_original >= 1).  Otherwise we are in the
    setting of c2/proof-MIX-low-partial-r2.md, and the avoider has interval-chain lifts (r2 Lemma S).
(c) Its lift data are killed outside R4 by: Theorem MIX-R (r2), Lemmas W, B1, Theorem A, Lemmas KS, AC
    (c2/proof-Rstar-r3.md Sec. 1-6, reviewed in v2) and Lemmas ZP, C (r3, unreviewed).  Hence if no
    interval-feasible normalized data lie in R4(p), there is no avoider: MIX_low(p).  []
Theorem P5: c2/proof-Rstar-r3.md Sec. 6 Remark (MIX_low(5) from W, MIX-R, A, B1, G1), then (a).  []

## 3. Statement PF (finite; conditional)

Every avoider has interval-feasible lifts (r2 Lemma S); so it suffices that the exact census of
interval-feasible normalized MIX_low data at p meets no configuration that escapes all written kills:
* p = 7, 11, 13 (rstar_census4.cpp, all k <= p, all (g, B), every interval-feasible (d, phi) up to rotation):
  15 / 211,911 / 48,094,987 configurations, every one killed by an exactly verified certificate, and
  R* intersect {B <= g} is empty.
* p = 17 (rstar_census21.cpp, all configurations of R* intersect {B <= g}; the DFS is pruned only by necessary
  conditions of R*, soundness for the cyclic block count shown in c2/proof-Rstar-r3.md Sec. 7 with the code
  lines): 150 configurations, all with a run of bh >= B + 1 (Theorem A applies; replayed with the exact window
  test), so R**(17), R***(17), R4(17) are empty.
Caveats: the census programs are not reviewed; the independent theta-domain cross-check (c2/xcheck_pos.py,
c2/xcheck_run.py with ../../../code/gr_window.py) is sampled, not exhaustive.  Parent position (Main,
2026-10-17 ~17:2x): this is evidence, not an accepted theorem, until an independent replay exists.

## 4. Imports and review status (exact)

| piece | file (sha256) | status |
|---|---|---|
| Lemma GR, Lemma WAS | ../../../proof-GR.md (33621e9e...), ../../../repr-WAS.md (87d7cade...) | [W] reviewed (Claude max) |
| PAR, RUNS, DR-Res | ../../../proof-INV-reduction.md (f11c9de1...) | [W] reviewed (Claude max) |
| Lemma H, Lemma BC, Theorem K0 | ../../proof-PAR-K0.md (4b107fff...9a38) | [W] Codex ACCEPT on this file (review/olson-parity-k0-kplus-codex-review-v1) |
| Lemma OR, K1, K1', S1', A1', KB | ../../proof-PAR-Kplus-partial-r2.md (8a13d982...fd04) | [W] Codex ACCEPT-WITH-FIXES, fixes applied, parent delta check PASS |
| Lemma M0 | ../../../inverse-run-count/proof-RUNS.md Sec. 12 (e3682f4d...) | [W] not independently reviewed; rechecked (Kplus-r2 Sec. 4 and Sec. 2(b) here) |
| Lemma S, Lemma K, MIX-R, R* | c2/proof-MIX-low-partial-r2.md (adf8cb70...6a22) | [W] r1 Codex ACCEPT-WITH-FIXES; r2 = fixes; parent delta check PASS |
| KL, W, B1, A, G1, KS, AC | c2/proof-Rstar-partial-v2.md (0df17ff8...4a40) = r3 Sec. 1-6 | [W] Codex ACCEPT; Claude ACCEPT-WITH-FIXES (fixes in r3) |
| ZP, C, R4, Remark MIX_low(5) | c2/proof-Rstar-r3.md (acdde81f...4e2b) | [W] unreviewed (Remark observed by the Claude review) |
| census | c2/rstar_census4.cpp (2ac68aa5...), c2/rstar_census21.cpp (1c6e9c18...) | [F] unreviewed code; sampled independent cross-check 0 mismatches |

## 5. Open

PAR(p) for every prime p >= 19 (and, as a theorem rather than [W+F], for 7 <= p <= 17) needs a written argument
that R4(p) contains no interval-feasible normalized data (or no avoider data).
