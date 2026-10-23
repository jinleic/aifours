# PAR(p): assembly of the proved pieces, the finite cases p <= 17, and the exact open condition

Owner OlsonParity2.  Written after host clock 2026-10-17T17:0x PDT (freeze time in out/freeze.txt).
Status: assembly [W] (every step is a citation of a frozen file below plus the short arguments marked
here); finite parts [F].  Nothing here proves PAR(p) for all primes, RUNS(p), INV, INV* or ordered Olson
for D_{2p}.

## 1. Statements

PAR(p) (../../../proof-INV-reduction.md Sec. 2): every inherited avoider w' in RGR_{4p-2}(p) with k <= p
has all 2k runs odd.
MIX_low(p) (../README.md Sec. 1, frozen 06:27:02): every RGR word of length 4p-2 with all k reflection
runs odd, k <= p, A >= B >= 1, B < kappa <= k-1, has an identity 2p-subword.

**Theorem PA (conditional, all p).**  For every prime p >= 5:  [R***(p) contains no avoider
configuration]  =>  MIX_low(p)  =>  PAR(p).
**Theorem PF (finite).**  PAR(p) and MIX_low(p) hold for p = 5, 7, 11, 13, 17.

## 2. Proof of Theorem PA (chain of citations)

(a) PAR(p) <= Theorem K0 (kappa = 0) and K+_viol(p) (../../proof-PAR-K0.md Sec. 3, 5;
    ../../proof-PAR-Kplus-partial-r2.md Sec. 4).  K+_viol(p) is proved there for kappa = 1 (Theorems K1,
    K1'), for B = 0 (Proposition S1', Lemma A1', trivial cut A >= 2p, via Lemma OR), for B = kappa
    (Theorem KB); the remaining range 1 <= B < kappa reduces, by Lemma OR (merged word w~: all o_F
    reflection runs odd, k(w~) = o_F <= k <= p, same A, B, kappa, and (V) gives kappa <= o_F - 1), to MIX_low(p).
(b) MIX_low(p): if A >= 2p, rho_1^{2p} is an identity 2p-subword.  Otherwise normalise by Lemma M0
    (../../../inverse-run-count/proof-RUNS.md Sec. 12: deleting rho_1 rho_{-1} from a run with r >= 3 and
    adding sigma_y sigma_y to a reflection run keeps k, every d_t, all parities and all phi, lowers A, B, kappa
    by 1 and shrinks every half window, so avoidance persists; rechecked here: E+ and E- both drop by 1,
    h rises by 1, g_P'(E-1) <= g_P(E)); iterate until every run is pure or a (1,1)-pair.  If B reaches 0,
    Proposition S1' / Lemma A1' / the trivial cut finish (kappa - B_original >= 1).  Otherwise the normalised
    word is in the setting of c2/proof-MIX-low-partial-r2.md (2g + B <= k - 1 <= p - 1).
(c) Normalised MIX_low avoider with interval-chain lifts (r2 Lemma S): if R* fails, Theorem MIX-R (r2 Sec. 5)
    kills it; if B >= g + 1, Lemma W kills it; if some d_t >= 2p - B, Lemma B1; in R* with some
    bh_t >= B + 1, Theorem A; in R* with every run cheap, Lemma AC; in R* with
    2 phi(Z0+) + alpha <= 2g + s - 1 + S_Z (and not every run cheap), Lemma KS
    (c2/proof-Rstar-partial-v2.md Sec. 1-6).  What is left is exactly R***(p) (Sec. 6 there).  []

## 3. Proof of Theorem PF

By Theorem PA it suffices that R***(p) has no avoider configuration.  Every avoider has interval-feasible
lifts (r2 Lemma S), so it suffices that the exact census of interval-feasible normalised MIX_low data
contains no R*** configuration:
* p = 5, 7, 11, 13 (rstar_census4.cpp, all k <= p, all (g, B), every interval-feasible (d, phi) up to
  rotation): 0 / 15 / 211,911 / 48,094,987 configurations, EVERY one killed by an exactly verified pattern
  (an independent-set KL certificate, checked by the mod-p window test), and R* intersect {B <= g} = empty;
  so MIX_low(p) holds directly.
* p = 17 (rstar_census21.cpp: all configurations of R* intersect {B <= g}; DFS pruned only by necessary
  conditions of R*, soundness argued in c2/proof-Rstar-partial-v2.md Sec. 7): 150 configurations, all with
  a run of bh >= B + 1 (Theorem A applies; the construction was replayed with the exact window test on all
  150), hence R**(17) = R***(17) = empty.
Consequently MIX_low(p) and, by Theorem PA (a), PAR(p) hold for p = 5, 7, 11, 13, 17.  (PAR(5), PAR(7)
were already known finite-exactly by a different route, ../../../proof-INV-reduction.md Sec. 3.1.)

## 4. Imports and their review status (exact)

| piece | file (sha256) | status |
|---|---|---|
| Lemma GR, Lemma WAS (and Lemma H's derivation) | ../../../proof-GR.md (33621e9e...), ../../../repr-WAS.md (87d7cade...) | [W] reviewed (Claude max; WAS minor fix applied) |
| PAR, RUNS, DR-Res definitions | ../../../proof-INV-reduction.md (f11c9de1...) | [W] reviewed (Claude max) |
| Lemma H, Lemma BC, Theorem K0 | ../../proof-PAR-K0.md (4b107fff...9a38) | [W] Codex ACCEPT-WITH-FIXES (review/olson-parity-k0-kplus-codex-review-v1), fixes applied |
| Lemma OR, K1, K1', S1', A1', KB | ../../proof-PAR-Kplus-partial-r2.md (8a13d982...fd04) | [W] same review, fixes applied; parent delta check PASS |
| Lemma M0 | ../../../inverse-run-count/proof-RUNS.md Sec. 12 (e3682f4d...) | [W] not independently reviewed; rechecked by OlsonParity (Kplus-r2 Sec. 4) and here (Sec. 2(b)) |
| Lemma S, Lemma K, MIX-R, R* | c2/proof-MIX-low-partial-r2.md (adf8cb70...6a22) | [W] r1 Codex ACCEPT-WITH-FIXES (review/olson-mixlow-codex-review-v1), r2 = fixes, parent delta check PASS (review/olson-mixlow-r2-parent-delta-check.json) |
| KL, W, B1, A, G1, KS, AC, R*** | c2/proof-Rstar-partial-v2.md (0df17ff8...4a40) | [W] Codex ACCEPT, no findings (review/olson-rstar-codex-review-v1.note.md, note sha 41fa3541...); Claude review pending at writing time |
| census p <= 13, p = 17 | c2/rstar_census4.cpp (2ac68aa5...), c2/rstar_census21.cpp (1c6e9c18...), outputs c2/out/ | [F] code-fidelity unreviewed; independent theta-domain cross-check (c2/xcheck*.py with ../../../code/gr_window.py 7d017cc1...): 0 mismatches; exact replays c2/lemma_replay*.cpp |

## 5. What remains open (exact)

PAR(p) for primes p >= 19 needs: no avoider configuration in R***(p) (definition: c2/proof-Rstar-partial-v2.md
Sec. 6-7).  No written argument for R***(p) = empty is known; it is empty in every exact census computed
(p <= 13 all configurations; p = 17 for B <= g) and in the singleton-only relaxation at p = 11.
