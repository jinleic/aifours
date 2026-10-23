"""Summarise multistart JSONs, keeping only converged (success) and feasible (feas < 1e-9) runs."""
import sys, json, glob
from collections import Counter
for fn in sorted(glob.glob('evidence/multistart_*_seed*.json')):
    d = json.load(open(fn))
    rs = [r for r in d['results'] if 'L' in r]
    good = [r for r in rs if r['success'] and r['feas'] < 1e-9]
    bad = len(rs) - len(good)
    best = max(good, key=lambda r: r['L']) if good else None
    clusters = Counter(round(r['L'], 6) for r in good)
    print(fn, 'starts', d['nstarts'], 'converged+feasible', len(good), 'discarded', bad, 'errors', d['n_errors'])
    print('   L* =', d['Lstar'], ' best feasible L - L* =', best['L'] - d['Lstar'] if best else None)
    print('   local-max values (count):', sorted(clusters.items(), key=lambda kv: -kv[0])[:8])
    if best: print('   best n9:', best['n9'])
