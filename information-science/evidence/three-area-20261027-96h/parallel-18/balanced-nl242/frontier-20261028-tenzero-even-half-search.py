#!/opt/homebrew/bin/python3
"""Bounded exact search for a single ternary inverse in one fixed ten-zero model."""
import argparse
import importlib.util
import json
import pathlib
import time
import z3


def transform(a):
    a=list(a);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):
                x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
        step*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--timeout-ms',type=int,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or not 1<=args.timeout_ms<=20000:raise ValueError('invalid bounds/output')
    path=pathlib.Path(__file__).with_name('frontier-20261028-tenzero-mod8-lift-check.py')
    spec=importlib.util.spec_from_file_location('lift',path);lift=importlib.util.module_from_spec(spec);spec.loader.exec_module(lift)
    g=[(lift.g0(x)+2*lift.h(x))%4 for x in range(256)]
    classes={j:[x for x in range(256) if g[x]==j] for j in range(4)}
    assert [len(classes[j]) for j in range(4)]==[10,60,126,60]
    b={x:z3.Int(f'b_{x}') for x in classes[2]+classes[3]}
    s=z3.Solver();s.set(timeout=args.timeout_ms,random_seed=20261028)
    s.add(*[z3.And(v>=0,v<=1) for v in b.values()]);s.add(z3.Sum([b[x] for x in classes[2]])==25,z3.Sum([b[x] for x in classes[3]])==38)
    # Fixed formal histogram forces b=1 for every residue-1 point, and b=0 for residue-0 points.
    fixed=[2*g[x]-8*int(g[x]==1) for x in range(256)];base=transform(fixed)
    for y in range(256):
        v=base[y]-8*z3.Sum([(-1 if ((x&y).bit_count()%2) else 1)*b[x] for x in b])
        s.add(z3.Or(v==-128,v==0,v==128))
    start=time.monotonic();status=s.check();result={'status':str(status),'solve_seconds':time.monotonic()-start,
        'scope':'fixed even residues and fixed histogram only; a solution is one ternary half, not a target witness',
        'timeout_ms':args.timeout_ms}
    if status==z3.unknown:result['reason_unknown']=s.reason_unknown()
    if status==z3.sat:
        model=s.model();k=[fixed[x]-8*(model.eval(b[x]).as_long() if x in b else 0) for x in range(256)]
        inv=transform(k);assert all(v in (-128,0,128) for v in inv)
        assert sum(v!=0 for v in inv)==80 and len([v for v in k if v==0])==10
        result.update({'even_k':k,'inverse_ternary':[v//128 for v in inv],
                       'support':sum(v!=0 for v in inv),'ternary_inverse_verified':True})
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('fixed-half search:',status,'seconds',round(result['solve_seconds'],3),flush=True)


if __name__=='__main__':main()
