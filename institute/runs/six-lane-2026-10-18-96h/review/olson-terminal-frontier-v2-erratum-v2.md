# Olson terminal frontier v2 — erratum v2 (corrected p=29 row; supersedes erratum v1's "no other row changes")

Recorded 2026-10-21T03:36:48-0700 (`/bin/date`). Governs olson-terminal-frontier-v2.md (1d72231e26b1382977b06db453d05100147e04fdc2a36b75639c039679ce6d0c) and its erratum v1 (bec9cfbf2a0213a16acdec3cfa8f3eab761b74a56d5a298dd7c0d2efa8d498df). Erratum v1 closed p=23 correctly but retained frontier v2's incorrect p=29 table and its inline "correction" paragraph, which conflicted with the BOTTOM composite's literal scope [(p−1)/2,p−2]=[14,27] at p=29. This erratum replaces the whole p=29 section. No accepted scope changes; this is a corrected union bookkeeping of already-accepted verdicts.

## Correct p=29, terminal k=30 row (full existential NF antecedent; range 0≤kappa_hat≤28)

| kappa_hat | accepted scope |
|---|---|
| 0 | K0T |
| 1,2,3 | LOWER-K1 (p≥11); K2 (p≥11); K3 (p≥13) |
| 4–7 | USK (3≤kappa_hat≤floor((p−1)/4)=7) |
| 8 | SCW (p=4·8−3=29) |
| 9 | FQW (p=4·9−7=29) |
| 10–11 | UFC U0 (p=4j−3, j=8, v∈{3,4}; T0 bound kappa≤(3p+5)/8=11.5) |
| **12–13** | **OPEN** (UFC complementary strip: v∈{5,6}, j=8≤2v−2; HIGH-COVER unproved; residual R_U) |
| 14–27 | upper-half composite [(p−1)/2,p−2] (BOTTOM verdict, p≥7) |
| 28 | PP1-EXCL (kappa_hat=p−1) |

Corrections made: kappa_hat=14 was never open (it lies in the BOTTOM composite's literal interval); kappa_hat=12 is open (UFC covers only kappa≤11 at p=29, not 12); the erroneous inline correction paragraph of frontier v2 is withdrawn. Bindings elsewhere in frontier v2 (FCW p=4κ−1, SCW p=4κ−3, TCW p=4κ−5, FQW p=4κ−7) are confirmed correct.

## General statement (unchanged in substance)

Open terminal middle cells for p≥23 are exactly those with floor((p+7)/4)<kappa_hat≤(p−3)/2 OUTSIDE UFC's T0 (kappa≤(3p+5)/8 for p≡1 mod4; ≤(3p+7)/8 for p≡3 mod4), minus separately proved cells (FC717: (7,17); FC19: (7,19),(8,19); FC1023: (10,23)). At p=23 this leaves nothing (row closed); at p=29 it leaves kappa_hat=12,13; for p≥31 the strip grows. Other terminal k, inverse-normalisation/assembly obligations and full ordered Olson remain OPEN. Union bookkeeping only; no new mathematics, no novelty claim.
