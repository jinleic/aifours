#!/opt/homebrew/bin/python3
"""Bounded fixed-even-lift inverse-divisibility search; UNKNOWN is not exclusion."""
import argparse
import json
import pathlib
import time
import z3


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--timeout-ms',type=int,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists() or not 1<=a.timeout_ms<=20000:raise ValueError('invalid output or timeout')
    k=json.loads(a.input.read_text())['spectrum_k'][:256];g=[(v//2)%4 for v in k];G=fw(g)
    assert all(v%4==0 for v in G) and len(k)==256 and k[0]==0
    rhs=[(v//4)%16 for v in G]
    for i in range(8):
        for x in range(256):
            if x&(1<<i):rhs[x]=(rhs[x]-rhs[x^(1<<i)])%16
    assert all(not rhs[x] for x in range(256) if x.bit_count()>3)
    bit={x:z3.Bool(f'flip_{x}') for x in range(256) if g[x]};s=z3.SolverFor('QF_BV')
    s.set(timeout=a.timeout_ms,random_seed=20261029)
    for mask in range(256):
        d=mask.bit_count()
        if d>3:continue
        width=4-d;assert rhs[mask]%(1<<d)==0
        target=(((-1)**d)*(rhs[mask]//(1<<d)))%(1<<width)
        vals=[z3.If(bit[x],z3.BitVecVal(1,width),z3.BitVecVal(0,width)) for x in bit if x&mask==mask]
        s.add(z3.Sum(vals)==z3.BitVecVal(target,width))
    s.add(z3.PbEq([(z3.Not(bit[x]) if g[x]==1 else bit[x],1) for x in bit if g[x] in(1,3)],8))
    s.add(z3.PbEq([(v,1) for v in bit.values()],sum(g)//4))
    start=time.monotonic();st=s.check();out={'scope':'one fixed even cubic g, E2=8, even first sum0; not an unrestricted search',
        'status':str(st),'timeout_ms':a.timeout_ms,'solve_seconds':time.monotonic()-start}
    if st==z3.unknown:out['reason_unknown']=s.reason_unknown()
    if st==z3.sat:
        model=s.model();even=[2*g[x]-8*int(z3.is_true(model.eval(bit[x]))) if x in bit else 0 for x in range(256)]
        F=fw(even);assert all(v%128==0 for v in F) and sum(even)==0 and sum(abs(v)==2 for v in even)==8
        out.update({'even_k':even,'inverse_divisible_by_128':True,'inverse_nonternary_count':sum(v not in(-128,0,128) for v in F)})
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('fixed even inverse-divisibility:',st,'seconds',round(out['solve_seconds'],3),flush=True)


if __name__=='__main__':main()
