# Case-A working notes v6 (Sun7K62Successor) - navigation only, NOT a candidate

- **Written:** `/bin/date` immediately before this exclusive write: 2026-10-19T07:11:18-0700. Unchecked scratch; no computation.

## Kill rules (sketches)
- **K1** (2F3S at a single-four vertex): a single-x-four vertex a (row R3/R3', x-four f, x_ta = 4) dies if some W-vertex s
  with x_as in {1,2} has a rigid x*-row with L*_t subset L*_a or L*_f subset L*_a (TC transfer at apex a in C^(x*)).
  For R3' the same count gives P2 = 0.
- **K2**: a single-x-four vertex a and a single-x*-four vertex s whose x*-four is a cannot coexist (s's R3* gives
  L*_a = L*_t; x_as = 2 automatically since x_as = 1 would make s single-x-four too).
- **K3**: a transfer D_j cap D_u = empty at apex a with masses m_j + m_u > 5/6 (e.g. a four and a two) is a contradiction.
- R5 (1,2,4,4|e) and (2,2,4,4|1) also give L_f1 = L_f2 (every non-one / non-t fibre contains both fours).
- A (3,1) vertex forces every other W-vertex to have d >= 2 (K2), so structures with (3,1) vertices have
  n12 = n13 = 0; possible (n31, n21, n22) = (2,0,3), (2,2,1), (4,0,1); dually for (1,3).

## Status of structures
- (4,0,1), (0,4,1): DEAD (|P*| count).  (2,0,3), (0,2,3) [path/pentagram]: DEAD (notes v3).
- (2,2,1) without 3-vertices: DEAD in all shapes (F-i by 2F3S; F-ii (a1), (a2), (b), (c) by K1/K2).
- n31 = 2, (2,0,3), F* = path: DEAD (K1 kills unless alpha_t = 2 on v1, v2 and alpha_t in {1,4} on x, w; then Cor L +
  dual T-TIGHT kill 44222/44122, and 44422 dies by K3 at y in C^alpha*).
- n31 = 2, (2,0,3), F = K_{2,3} (TC-A22 section 4 example): K1 at v1 forces every 3-side alpha-row to be R2
  (alpha_t = 4); t's alpha-row is 44412 or 44422; counts at x so far satisfiable. OPEN.
- Still to examine: n31 = 2 with (2,2,1); n31 = 4 (4,0,1); duals.
