"""Long horizon (T = 40) cross-check, example 1: the discrete augmented-state game thresholds converge
at first order in dt to the continuous advanced-GRDE threshold, and both lie below the
infinite-horizon threshold gamma*_inf (evidence/numerics.json, E5).

Command (from this directory):
  OMP_NUM_THREADS=4 PYTHONPATH=. .../venv/bin/python check_long_horizon.py
writes ../evidence/long_horizon_T40.json
"""
import json
import time

from shp import Plant, bisect_gamma, disc_game, solve_grde

pl = Plant(A=[[1.0]], B=[[1.0]], C=[[1.0]], A0=[[0.5]], B0=[[0.4]], D0=[[1.0], [0.0]], D1=[[0.0], [1.0]])
res = {}
for h, dts in [(0.0, [0.01, 0.005, 0.0025]), (0.5, [0.01, 0.005])]:
    gc = bisect_gamma(lambda g: solve_grde(pl, g, h, 40.0, 0.005)['ok'], 1.0, 2.5, tol=1e-6)[1]
    rows = []
    for dt in dts:
        t = time.time()
        gd = bisect_gamma(lambda g: disc_game(pl, g, h, 40.0, dt)[0], 1.0, 2.5, tol=1e-6)[1]
        rows.append((dt, gd))
        print(f'h {h} dt {dt}: disc T=40 {gd:.6f} ({time.time()-t:.0f}s); cont T=40 (dt .005) {gc:.6f}', flush=True)
    res[str(h)] = dict(cont_T40=gc, disc_T40=rows)
json.dump(res, open('../evidence/long_horizon_T40.json', 'w'), indent=1)
