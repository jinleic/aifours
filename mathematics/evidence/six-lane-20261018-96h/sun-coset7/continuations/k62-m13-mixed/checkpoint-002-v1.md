# k62-m13-mixed checkpoint 002 — candidate route to the FULL M13 target found in thought; writing it now

- **Written:** `/bin/date` read at 2026-10-19T12:57:27-0700, immediately before this file.
- Previous: `checkpoint-001-v1.md`, sha256 46f168fe88b0d642cf7e043e3f7c536fb0a6053202287663f0da4fbef8a5ed98. Owner SunM13MixedFibres; written mathematics only; no computation.

## Actual result (thought-level, not yet frozen; CANDIDATE_UNVERIFIED)
A complete route to Theorem M13X (no configuration of M13, both orientations) appears to close:
1. **SG (subset granularity, mixed-family at t):** for every v in O and both families z,
   gcd(n_v, T_z(V minus {v, i*})) = 6. Chain d first; a multiplier 3 at an O-step forces a product equality
   (Pi^z_d cap Pi^z_e)(Pi^z_d cap Pi^z_c) = Pi^z_d, which forbids e, c from sharing a d-fibre of the z-configuration; but there
   deg_d(e) = deg_d(c) = n_d/2, so #both = #neither >= 1 (own fibre). Only v = t needs this; for v != t f_v = 1 suffices.
2. **i*-free certificates suffice everywhere they are needed:** the R4-type certificate (1 on entries 1, 1/2 on entries
   2 and d, 0 on i*; value 11/12 > 5/6) and the CI/VFC light-set argument use no i*-piece; with SG they hold at EVERY
   O-vertex, t and p included, in both families. Hence: no O-row of either family has all four O-entries in {1,2}
   (every H_x-degree in [1,3], degree 3 forces x' = 4 on the fourth pair, no K4, no bowtie), and a tight equal-X cherry
   is impossible at every apex (one-tight is impossible by Sun(2)).
3. **The MK-v2 combinatorial chain re-proved in M13** (MK is NOT imported): budget n_4(x) <= 8 - 2u(x) from accepted
   C2 (alpha*) and C2* (alpha); no (4,4,4) tau-16 triple; at most one (2,4,4) tau-8 triple; four-subset depth <= 4
   (FB-M argument); hence accepted Theorem DG (alpha*) and DG* (alpha) give two deep triples per family; so each H_x
   contains a diamond; two edge-disjoint diamonds on five vertices are impossible.
The inverted d-system's four-piece fibres enter only through the accepted M13-A (DG*, C2*); the new step avoids i*.

## Blocker
None identified yet; every step must still be written and re-checked line by line. Correctness unverified.

## Next bounded action
Freeze `K62-M13X-v1.md` (full proof + interface table), then the review package and manifest. Checkpoint <= 13:30.
