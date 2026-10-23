# b63 family 1: exact remaining obstruction v1 (NOT an exclusion)

Written after host clock 2026-10-19T22:05:58-0700 by ContinuePA19d. Owner throttle (RUN/control/owner-workload-throttle-one-third-v1.json, SHA256 3ba3ca96e2a869d5fee8fa76186184e5d380cc296fec5713da9d97c35776f9de) directs finishing this deliverable at frozen scope and parking; the frozen scope (scope-v1.md) admits "exact remaining obstructions" as an outcome. **Family 1 is NOT excluded. b63 and PA(19,8,6) remain UNDECIDED; no count change.**

## Proven (candidate, unreviewed; parts 1-4 of this directory)
Every family-1 array has category T2, pair(A)={g,z}, and after the 1<->2 normalization pair(B)={13,24}, pair(C)={14,23}; exactly one privates-only quad Fq; (h_A,h_B,h_C) is (4,3,3), (3,4,3), (3,3,4) or (2,4,4) ((4,4,2) is impossible); in (4,3,3), (3,3,4), (2,4,4) Fq has occupancy 2 and each occupancy-3 quad holds a single W row. In (3,3,4) the column-B configurations (i-a1),(i-a2),(i-a3),(i-b1),(i-b2) and (ii) with r*=p3 are impossible, and within (ii) with r*=p1, W''=z, the C-arrangement (C4a) and the (C4b) sub-arrangement S1 are impossible.

## Exact remaining configurations (each must still be refuted for every row identity, empty-row placement and P0 completion)
- R1. Option (4,3,3): h_A=4 (all A-blocks have two nonempty rows; A-triples occupancy 1), h_B=3 (column B is one of the L1 configurations), h_C=3; Fq occupancy 2; one single-W quad in B and one in C.
- R2. Option (3,4,3): every configuration (Fq of occupancy 2 or 3).
- R3. Option (2,4,4): both occupancy-3 quads are A-quads holding single W rows; Fq occupancy 2 in B or C; column C per L2.
- R4. Option (3,3,4) with column-B configuration (ii):
  - R4a. r*=p1, W''=z, (C4b) with C-quads {z,p2},{13,p0*}: arrangement S2, i.e. A={24} (quad), {p1,p3} (quad), {23,04}, {13,p0*',p2}, {14,p0*}; C={04,p1},{z,p2},{13,p0*},{24,p0*'}; B={z,p0*,p1},{04,p2,p3},{W},{W',p0*'} with {W,W'}={14,23}.
  - R4b. r*=p1, W''=z, (C4b) with C-quads z's and 24's.
  - R4c. r*=p1, W''=23: B={23,p0*,p1},{04,p2,p3}, {W},{W',p0*'} with {W,W'}={z,14}; all A/C arrangements.
  - R4d. r*=p2, W'' in {z,14}: B4={04,p1,p3}; all A/C arrangements.

## Mathematical blocker
No single invariant found so far closes these residual classes; the closures obtained combine P1 compatibility, the incidence equalities x(r)+(occupancies)=const, and P0 partner menus for rows with x(r)=0. Each residual class is a finite list of P1 arrangements whose completion needs the same P0 menu analysis; it was not completed within this bounded, throttled slot. No feasibility of any residual class is claimed.
