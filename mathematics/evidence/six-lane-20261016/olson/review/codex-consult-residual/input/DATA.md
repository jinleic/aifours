# Finite data (computer; NOT proofs), lane MathOlson 2026-10-16

Depth of a unit = max d with theta = [0] + sum_{s in Opt\0} c_s [s] in J^d in F_p[Z_p^2],
Opt = {(val(T), |T|/2) : T subset of the unit, even #reflections, even |T|}.
Full = depth floor(len/2).  Exact routine: tiling.py (unit_points, depth_at_least).

Bracket f[S]f' (left reflection, interior S, right reflection), exhaustive over all
values up to scaling (first nonzero of (C, values) = 1), C = y_f - y_f':
 p=7:  f[rr]f degenerate iff x1+x2 = C != 0;  f[ff]f never;  f[rrrr]f only constant
       runs x^4 with 4x in {2C,3C};  f[rrff]f, f[ffrr]f, f[rffr]f, f[frrf]f, f[ffff]f,
       f[rffffr]f, f[rrffrr]f, f[rffrrr]f, f[frrfrr]f, f[rrfrrf]f, f[rfrrfr]f: never.
       f[rrrrrr]f: 69 degenerate classes (incl. non-constant x^5 y patterns).
 p=11: f[rr]f, f[rrrr]f same pattern; f[ff]f, f[rffr]f, f[rrff]f, f[ffrr]f never.
Structured test (rotations in {1,a}, reflections in {0,c}), p=7: f[rrrrff]f HAS
 degenerate cases, e.g. sigma_0 rho_1^4 sigma_1 sigma_1 sigma_1 (inner ff equal values).
4-units: frrf degenerate iff x1+x2 = y1-y2 != 0; rfrf iff x1+x2 = y1-y2 and x2 != 0;
 frfr iff x1+x2 = y1-y2 and x1 != 0; rffr, rrff, ffrr, rrrr, ffff always full.
Tiling search (units <= 8 letters, one odd unit of length 1 or 3): every sampled word in
Res (p=7: 124 words from structured families) has a full tiling; frequent units:
rffr, rfffrf, frffrf, fffrfr, frrf, rfrf, frfr, frfffrff, ffrfffrf.
Exhaustive all-word checks: no counterexample to ordered Olson for D6, D10 (all words).
