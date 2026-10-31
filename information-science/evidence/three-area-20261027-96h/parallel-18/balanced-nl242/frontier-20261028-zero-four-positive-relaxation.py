#!/opt/homebrew/bin/python3
"""Seek four-zero spectrum counts satisfying moments, integrality and dual positivity.

A satisfying count vector is a RELAXATION, not a Boolean function or code.
"""
import argparse
import importlib.util
import json
import math
import pathlib
import time

import z3


def load_base():
    path = pathlib.Path(__file__).with_name('frontier-20261028-zero-four-relaxation.py')
    spec = importlib.util.spec_from_file_location('zero_four_base', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--timeout-ms', type=int, required=True)
    p.add_argument('--output', type=pathlib.Path, required=True)
    args = p.parse_args()
    if not 1 <= args.timeout_ms <= 60000:
        raise ValueError('timeout must be 1..60000 ms')
    if args.output.exists():
        raise FileExistsError(args.output)
    base = load_base()
    a = {t: z3.Int(f'b_{t:+d}') for t in range(-7, 8)}
    s = z3.Solver()
    s.set(timeout=args.timeout_ms, random_seed=20261028)
    s.add(*[z3.And(v >= 0, v <= 511) for v in a.values()])
    s.add(a[0] == 3, z3.Sum(list(a.values())) == 511)
    s.add(z3.Sum([t*a[t] for t in a]) == 128)
    s.add(z3.Sum([t*t*a[t] for t in a]) == 16384)
    s.add(z3.Sum([a[t] for t in a if t % 2]) == 256)
    even_first = z3.Sum([t*a[t] for t in a if not t % 2])
    # Distinct-support columns force D_255 in {0,1}; equivalently even_first in {0,128}.
    s.add(z3.Or(even_first == 0, even_first == 128))
    for j in range(15):
        s.add((z3.Sum([base.krawtchouk(14,7+t,j)*a[t] for t in a]) + base.h_coeff(j)) % 512 == 0)
    started=time.monotonic()
    result=s.check()
    receipt={'solver':'z3','timeout_ms':args.timeout_ms,'elapsed_seconds':time.monotonic()-started,
             'status':str(result),'scope':'histogram plus dual-positivity relaxation; no realization'}
    if result == z3.unknown:
        receipt['reason_unknown']=s.reason_unknown()
    if result == z3.sat:
        m=s.model(); v={t:m.eval(a[t]).as_long() for t in a}
        assert v[0]==3 and sum(v.values())==511
        assert sum(t*v[t] for t in v)==128 and sum(t*t*v[t] for t in v)==16384
        assert sum(v[t] for t in v if t%2)==256
        assert sum(t*v[t] for t in v if not t%2) in (0,128)
        residues=[(sum(base.krawtchouk(14,7+t,j)*v[t] for t in v)+base.h_coeff(j))%512 for j in range(15)]
        assert residues==[0]*15
        nums=[math.comb(256,j)+sum(v[t]*base.krawtchouk(256,128+t,j) for t in v) for j in range(257)]
        assert all(n%512==0 for n in nums)
        dual=[n//512 for n in nums]
        assert all(d>=0 for d in dual)
        assert dual[0]==1 and dual[1]==0 and dual[2]==0 and dual[255] in (0,1) and dual[256]==0
        # An exact sufficient dominance check shows why interior dual positivity
        # needs no model-dependent inequality; edge cases are verified directly.
        nondominated=[j for j in range(257) if math.comb(256,j)<511*max(abs(base.krawtchouk(256,128+t,j)) for t in v)]
        assert nondominated==[0,1,2,254,255,256]
        receipt.update({'histogram':{str(t):v[t] for t in v},'residues_15':residues,
                        'dual_nonnegative':True,'dual_coefficients_decimal':[str(x) for x in dual],
                        'interior_dominance_noncovered_indices':nondominated,
                        'mutation_control':any((n+(j==0))%512 for j,n in enumerate(nums))})
        assert receipt['mutation_control']
    with args.output.open('x',encoding='utf-8') as out:
        json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print('status=',result,'solve_seconds=',round(receipt['elapsed_seconds'],3),'histogram=',receipt.get('histogram'),flush=True)


if __name__=='__main__':
    main()
