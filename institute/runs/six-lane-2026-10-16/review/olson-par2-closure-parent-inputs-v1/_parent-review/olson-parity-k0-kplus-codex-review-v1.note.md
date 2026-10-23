VERDICT: **ACCEPT-WITH-FIXES**

- **proof-PAR-K0.md: ACCEPT**
- **proof-PAR-Kplus-partial.md: ACCEPT-WITH-FIXES**

Both SHA-256 values match. No FATAL or MAJOR defect found.

- **MINOR — [proof-PAR-Kplus-partial.md:31](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-parity-inputs-v1/inverse-parity/proof-PAR-Kplus-partial.md:31):** OR’s remark asserts inherited inequalities and `k ≤ p` without assuming them in OR itself. Replace this with conditional preservation: inherited inequalities persist when assumed; `k̃ = o_F ≤ p` requires the corresponding input bound. The subsequent proofs supply their bounds, so this creates no circular use of RUNS(p).

- **MINOR — [proof-PAR-Kplus-partial.md:202](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-parity-inputs-v1/inverse-parity/proof-PAR-Kplus-partial.md:202):** A1′ should justify connectivity for *coloured patterns*, since P and Pᶜ have identical uncoloured cut sets. Add the vacancy construction: use a free position to move each labelled cut to the next original cut position. This swaps the two arc colours and gives the required path to Pᶜ, with each move changing mass by one `r_u`.

- **MINOR — [proof-PAR-Kplus-partial.md:239](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-parity-inputs-v1/inverse-parity/proof-PAR-Kplus-partial.md:239):** KB’s capped-union argument drops the cap from the remaining positive term. Explicitly handle a second capped term: together with any negative term it contributes at least `p + 1 − B ≥ 2`. The displayed uncapped calculation handles the remaining case.

### What is established

For primes **p ≥ 5**, with the stated RGR and length hypotheses:

- **H:** the corrected empty/full residue condition and every proper-pattern half-window formula are correct. The simplified zero condition requires the stated bound on A and B.
- **BC:** valid, including its Claim when windows are empty or λ is negative.
- **K0:** proves PAR(p) for inherited avoiders with `k ≤ p` and `κ = 0`. Its stronger hypotheses `(P),(V)` suffice.
- **OR, K1, K1′:** avoidance survives OR; K1 excludes `κ = 1, B = 0` under `(V), k ≤ p`; K1′ excludes `κ = B = 1` with the additional `(D0)`.
- **IP:** valid for all-odd-reflection words with `B = 0`, `1 ≤ κ ≤ k−1`, and every integer vector of sum p. No `k ≤ p` assumption is needed.
- **S1′/A1′:** together with the trivial `R ≥ 2p` case and OR, exclude inherited avoiders with `B = 0, κ ≥ 1, k ≤ p`.
- **KB:** valid for `B = κ ≥ 1`, `(V)`, and `o_F ≤ p`, with arbitrary original k. `(D0)` remains necessary in its stated exceptional-segment case.

Thus PAR reduces to the still-open **MIX_low** range.

### What is imported/unchecked

GR/WAS provide the foundation. No closed proof uses RUNS(p), MIX_low, or the unproved lifting statement. The absent M0 source is optional normalization, not needed for these conclusions. Logged large enumerations and external review receipts were not reproduced.

Independent in-memory checks at p = 5,7 found no window-formula or certificate failures.