"""Bounded additional-seed experiment; exact neighborhoods, not symmetry classes."""
import argparse
import hashlib
import json
from pathlib import Path
from extra_seeds import EXTRA_SEEDS
from seeds import decode
from radius2 import search as radius2
from radius4 import search as radius4


p=argparse.ArgumentParser()
p.add_argument('--compare',action='store_true')
p.add_argument('--only-two',action='store_true')
a=p.parse_args()
out={'bit_order':'bits[x]=f(x); x_i=(x>>i)&1; hex MSB first','seeds':{}}
for name,hx in EXTRA_SEEDS.items():
    f=decode(hx)
    r2=radius2(f)
    r4=None if a.only_two else radius4(f)
    ac=[sum((1-2*f[x])*(1-2*f[x^t]) for x in range(512)) for t in range(512)]
    out['seeds'][name]={'hex':hx,'sha256_ascii_bits':hashlib.sha256(''.join(map(str,f)).encode()).hexdigest(),
                       'radius2':r2,'radius4':r4,'autocorrelation':ac,'absolute_indicator':max(map(abs,ac[1:]))}
    print(name,'weight',sum(f),'original forced distance',r2['original_minimum_balancing_distance'],
          'min shifted distance',r2['minimum_over_linear_shifts'],
          'indicator',max(map(abs,ac[1:])),
          'legal pairs',len(r2['pairs_preserving_bound']),
          'legal fours',None if r4 is None else len(r4['four_sets_preserving_bound']),flush=True)
if not a.only_two:
    path=Path('results/extra-seed-neighborhoods.json')
    if a.compare:
        assert json.loads(path.read_text())==out
    else:
        path.write_text(json.dumps(out,indent=2)+'\n')
    assert all(not rec['radius2']['pairs_preserving_bound_and_giving_a_zero'] and not rec['radius4']['four_sets_preserving_bound_and_giving_a_zero'] for rec in out['seeds'].values())
