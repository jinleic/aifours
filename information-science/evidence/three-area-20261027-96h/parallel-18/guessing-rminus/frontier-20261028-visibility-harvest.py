#!/usr/bin/env python3
"""Re-solve named visibility sets with the stable LP and keep full duals.

Usage: python3 script.py OUT.json "2,5,9,10" "1,5,7,8,9" ...
Outputs floating dual supports only; exact reconstruction is separate.
"""
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
spec=spec_from_file_location('vis',ROOT/'frontier-20261028-visibility-set-stable-lp.py');vis=module_from_spec(spec);spec.loader.exec_module(vis)

def main():
    out=ROOT/sys.argv[1];cases=[]
    for text in sys.argv[2:]:
        W={int(x) for x in text.split(',')};stab=[p for p in vis.P if {p[v-1] for v in W}==W]
        r=vis.solve(W,stab,limit=40.0);r['group']=stab;cases.append(r)
        print(json.dumps({k:v for k,v in r.items() if k in ('W','group_size','status_float_unverified','objective_float_unverified')}),flush=True)
    with out.open('x',encoding='utf-8') as f:json.dump({'cases':cases,'limits':'Floating duals for exact reconstruction only.'},f,indent=2);f.write('\n')


if __name__=='__main__':main()
