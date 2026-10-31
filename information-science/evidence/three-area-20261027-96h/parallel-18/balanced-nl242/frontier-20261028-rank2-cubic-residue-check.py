#!/opt/homebrew/bin/python3
"""Finite mod8 residue split and explicit six-radical cubic sharpness controls."""
import argparse
import collections
import json
import pathlib


def anf(vals,n):
    a=list(vals)
    for i in range(n):
        for x in range(1<<n):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return [x for x,v in enumerate(a) if v]


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    rows=[]
    for D,m,Z in ((12,118,8),(12,118,16),(12,118,24),(16,120,8),(16,120,16),(20,122,8)):
        E2=(7936-16*Z-64*m)//32;N=64-Z;res={0:set(),128:set()}
        for G3 in range(0,193,8):
            for low3 in range(max(0,E2-(192-G3)),min(E2,G3)+1):
                for plus4 in range(N+1):
                    total=6*(2*G3-192)+8*(E2-2*low3)+4*(2*plus4-N)
                    if total in res:res[total].add(G3)
        assert all(res.values())
        rows.append({'D':D,'m':m,'Z':Z,'E2':E2,'G3_by_even_first_sum':{str(k):sorted(v) for k,v in res.items()}})
    R={x for x in range(64) if x&7==0}
    qint=[(x&1)+((x>>1)&1)+int(x&3==3) for x in range(256)]
    h=[1^int((x>>2) in R) for x in range(256)]
    assert max(t.bit_count() for t in anf(h,8))==3
    g=[(qint[x]+2*h[x])%4 for x in range(256)]
    q=[int(x&3!=0) for x in range(256)];assert all(g[x]%2==q[x] for x in range(256))
    assert collections.Counter(g)=={0:8,1:72,2:56,3:120}
    even=[0]*256
    for i,x in enumerate([x for x in range(256) if g[x]==2]):even[x]=-4 if i<48 else 4
    for x in range(256):
        if g[x]==1:even[x]=-6
        if g[x]==3:even[x]=6
    assert sum(even)==128 and sum(x*x for x in even)==64*122 and max(map(abs,even))==6
    assert rows[-1]['G3_by_even_first_sum']['128'][-1]==120
    out={'scope':'even-half cubic/energy control only; not a target witness','rank2_residue_profiles':rows,
         'formal_even_half':{'k':even,'Z':8,'g3':120,'g1':72,'first_sum':128,
                            'squared_sum':7808,'cubic_correction_degree':3,'actual_Boolean_witness':False}}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('six cubic residue split tables; explicit even-half G3=120 first-sum128 non-witness')


if __name__=='__main__':main()
