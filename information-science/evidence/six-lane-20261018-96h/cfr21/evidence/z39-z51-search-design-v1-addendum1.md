# Addendum 1 to z39-z51-search-design-v1.md (sha 4efea8b2…) — involution-model heuristic, 2026-10-19T00:34:42-0700

Written arithmetic only (no search). Model: s = (mu, (12)(34)(56)) fixing row 0, f = gcd(mu+1,n) fixed columns,
g = (n-f)/2 two-cycles; rows 0, t, mu h(t), g(t), mu g(h(t)), j(t), mu j(h(t)) as in the old lane.
log10 E ≈ [g·6·log n − log g! − g·log 2 + f·3·log n − log f!]                     (configurations)
         + 3·[log g! + g·log 2 − g·log n + log f! − f·log f]                      (3 swapped pairs: ±-orbit covering)
         + 9·[log n! − n·log n] + 6·(log n − 1/2)                                 (9 free pair-orbits, sum correction)
(natural logs converted to log10; no division by residual symmetries ~ n·phi(n)).

| n | f | g | log10 E (labelled) |
|---|---|---|---|
| 21 | 1 | 10 | -3.12 |
| 21 | 3 | 9 | -4.49 |
| 21 | 7 | 7 | -9.08 |
| 39 | 1 | 19 | 7.64 |
| 39 | 3 | 18 | 6.52 |
| 39 | 13 | 13 | -5.77 |
| 51 | 1 | 25 | 19.51 |
| 51 | 3 | 24 | 18.49 |
| 51 | 17 | 17 | 0.74 |
| 15 | 1 | 7 | -4.12 |
| 15 | 3 | 6 | -5.63 |
| 15 | 5 | 5 | -7.84 |
| 13 | 1 | 6 | -4.08 |
| 7 | 1 | 3 | -2.65 |

Reading [HEURISTIC]: Z21 involution models are predicted empty (g00 -3.1, g10 -4.5, g16 -9.1; consistent with the old
lane's empty g16 and UNKNOWN g00/g10); Z39 mu in {1,14} and Z51 mu in {1,35} are predicted populated.
Calibration caveat: the same formula predicts ~1e-4 for n = 13 and ~1e-2.7 for n = 7, where solutions do exist
(prime fields: linear DMs and large automorphism groups), so it is NOT validated; for 3 | n linear structure is
excluded (L3), which is why it may be more relevant there, but this is unproved. Findability caveat: even with ~1e7
labelled Z39 solutions, a per-h exhaustive engine needs to visit ~1e14 admissible h; a first-solution strategy must
search (h, g, j) jointly (SAT/exact cover on the whole symmetric model) rather than enumerate h.
