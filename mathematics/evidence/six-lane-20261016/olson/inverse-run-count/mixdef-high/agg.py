"""Aggregate mhc summary lines by R-class (label semantics: "<=-3" means R <= 2p-4 (label bug in mhc.cpp,
R_minus_2p = -3 means R = 2p-3), -2 / -1 / ">=0" mean R = 2p-2 / 2p-1 / R >= 2p) and kB."""
import sys, json
from collections import defaultdict
agg = defaultdict(lambda: defaultdict(int))
for line in open(sys.argv[1]):
    if '"summary"' not in line: continue
    r = json.loads(line)
    lab = str(r['R_minus_2p'])
    cls = {'<=-3': 'R<=2p-4', '-3': 'R=2p-3', '-2': 'R=2p-2', '-1': 'R=2p-1', '>=0': 'R>=2p'}[lab]
    key = (r['p'], cls, 'kB=1' if r['kB'] == 1 else 'kB>=2', 'k=p+1' if r['k'] == r['p'] + 1 else 'k>=p+2')
    for f in ['data', 'FULL', 'ZSI', 'BC3', 'IK', 'M2K', 'M3K', 'AVOIDER']: agg[key][f] += r[f]
for key in sorted(agg): print(key, dict(agg[key]))
