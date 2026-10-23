# Plan E10b (frozen before running; host clock 2026-10-18T04:55:38-0700)

E10 (out/e10_mxg_replay.json, code/e10_mxg_replay_v2.py 0fb093d7...6951) found 0 failures on 6661 interval-feasible data but
never reached Theorem A', AC', KS', ZP, C or R4' (every R*_G datum had B >= g + 1).  E10b uses the SAME replay function
(imported from e10_mxg_replay_v2.py's text, not re-implemented) on data generated lift-first near the residual: B <= g, anti
runs mostly c = 1 defects, aligned runs fillers or shallow defects, empty runs defects or not; bh_t drawn from small values with
bh = d mod 2 and sum bh = k - 2g, x_t = (d_t + bh_t)/2; kept only if interval-feasible and genuine (as in E10).  p in
{11, 13, 17, 19, 23}.  Same checks, same FAILURE definition, raw DP for p = 11 (every 3rd datum).  Caps: one process,
ulimit -t 1800, <= 3000 kept data per p, output out/e10b_mxg_residual.json (x).
