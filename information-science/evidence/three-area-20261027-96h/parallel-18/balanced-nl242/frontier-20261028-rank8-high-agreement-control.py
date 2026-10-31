#!/opt/homebrew/bin/python3
"""Construct a real high-agreement rank8 balanced Boolean non-target control."""
import argparse
import functools
import json
import pathlib
import random


def fw(a):
    a=list(a);n=len(a);s=1
    while s<n:
        for i in range(0,n,2*s):
            for j in range(i,i+s):
                x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def rank(rows):
    basis={}
    for v in rows:
        while v:
            i=v.bit_length()-1
            if i in basis:v^=basis[i]
            else:basis[i]=v;break
    return len(basis)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    rng=random.Random(20261028580)
    for attempt in range(1,1001):
        picked={0,*rng.sample(range(1,256),124)};last=functools.reduce(int.__xor__,picked,0)
        if last in picked:continue
        picked.add(last);assert len(picked)==126 and functools.reduce(int.__xor__,picked,0)==0
        rest=list(picked-{0});rng.shuffle(rest);u=[0]*256;u[0]=1
        for x in rest[:62]:u[x]=1
        for x in rest[62:]:u[x]=-1
        assert sum(u)==0 and sum(v!=0 for v in u)==126
        zero=[i for i,v in enumerate(u) if not v];rng.shuffle(zero);v=[0]*256
        for x in zero[:64]:v[x]=1
        for x in zero[64:]:v[x]=-1
        assert sum(v)==-2
        sign=[u[y]+v[y] for y in range(256)]+[u[y]-v[y] for y in range(256)]
        assert all(x in (-1,1) for x in sign)
        truth=[(1-x)//2 for x in sign];T=functools.reduce(int.__xor__,(i for i,b in enumerate(truth) if b),0)
        assert sum(truth)==256 and T==256 and truth[0]==0
        W=fw(sign);assert all(x%8==0 for x in W[:256])
        q=[(x//8)%2 for x in W[:256]]
        for j in range(8):
            for x in range(256):
                if x&(1<<j):q[x]^=q[x^(1<<j)]
        assert all(not q[x] or x.bit_count()<=2 for x in range(256))
        matrix=[0]*8
        for x,c in enumerate(q):
            if c and x.bit_count()==2:
                i,j=[t for t in range(8) if x&(1<<t)];matrix[i]|=1<<j;matrix[j]|=1<<i
        if rank(matrix)!=8:continue
        peak=max(map(abs,W));assert peak>28
        data={'format':'boolean-truth-v1','bits':''.join(str(x) for x in truth),
              'scope':'balanced rank8, m=126 actual Boolean NON-TARGET control, peak exceeds 28',
              'reported_peak':peak,'reported_T':T,'reported_agreeing_pairs':126,'reported_polar_rank':8,
              'rng_seed':20261028580,'attempt':attempt}
        with a.output.open('x',encoding='utf-8') as dst:json.dump(data,dst,indent=2,sort_keys=True);dst.write('\n')
        print('actual high-peak control: attempt',attempt,'T',T,'m=126 rank=8 peak=',peak)
        return
    raise RuntimeError('no bounded control found')


if __name__=='__main__':main()
