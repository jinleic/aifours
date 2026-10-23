# Case-A working notes v4 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:07:02-0700. Unchecked scratch; no computation.

## General counting principle (sketch)
Single-four alpha-vertices lie in P, single-four alpha*-vertices in P*; P and P* are disjoint. If Gamma^alpha (complement of
F) is connected, |P*| >= 2 (Cor L); if Gamma^alpha* is connected, |P| >= 2. Dual T-TIGHT (in C^alpha*): if t's alpha-row on W
is 44222/44122 with fours P, no single-four alpha*-vertex with alpha_t = 2 has its alpha*-four in P.

## Structure (4,0,1) (and (0,4,1)): DEAD
F = P3 + P2 (degrees 2,1,1,1,1), complement connected, so |P*| >= 2; but the four degree-1 vertices are in P, so
|P*| <= 1.

## Structure (2,2,1), shape F-i: F = {A1A2, B1B2, B1C, B2C}, F* = {A1C, A2C, A1B1, A2B2}, N = {A1B2, A2B1}
- No twins possible except none: A1, A2 rows R3 (alpha_t = 4); B1, B2 single alpha*-four (alpha*_t = 4).
- Dual T-TIGHT forces C in P (else B1, B2 both ones of t's alpha-row); then P* = {B1, B2} and t's alpha*-row is tight.
- Apex A1 (C^alpha) with D_A2 avoiding D_z and D_t: forces alpha*_A1B2 = 2 and, if alpha*_A1A2 = 1, D_z inside D_C cap D_B1.
- No contradiction yet. Shapes F-ii (F = path with ends A1, A2) not yet examined; N-pairings to enumerate.
