#!/opt/homebrew/bin/python3
"""Exact six-phase arithmetic and a ternary-half nonextension control."""
import argparse
import collections
import importlib.util
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
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
    rows=[]
    for w,c in [(136,10),(136,24),(136,26),(120,20),(120,22),(120,36)]:
        case1=[];case2=[]
        for j in range(4):
            counts={7:w-c,-7:210-w+c,3:j,-3:3-j,-5:c-j,5:43-c+j,1:0,-1:0}
            assert min(counts.values())>=0 and sum(counts.values())==256
            assert counts[-5]+counts[3]+counts[-1]+counts[7]==w
            assert counts[-5]+counts[3]==c
            val=sum(k*v for k,v in counts.items());assert val==14*w-24*c-1264+16*j
            case1.append(val)
        for u in (0,1):
            counts={7:w-c-u,-7:209-w+c+u,3:0,-3:0,-5:c,5:46-c,1:1-u,-1:u}
            assert min(counts.values())>=0 and sum(counts.values())==256
            assert counts[-5]+counts[3]+counts[-1]+counts[7]==w
            assert counts[-5]+counts[3]==c
            val=sum(k*v for k,v in counts.items());assert val==14*w-24*c-1232-16*u
            case2.append(val)
        assert not ({0,128}&set(case1+case2))
        rows.append({'Q_weight':w,'intersection':c,'case1_odd_sums':case1,'case2_odd_sums':case2})
    f=pathlib.Path(__file__).with_name('frontier-20261028-tenzero-mod8-lift-check.py')
    spec=importlib.util.spec_from_file_location('lift',f);lift=importlib.util.module_from_spec(spec);spec.loader.exec_module(lift)
    bits=int('7f737fee6bf9b579f1b6ffffb787feb45f3a1a0479f28b463527a4689b0edb52',16)
    g=[(lift.g0(x)+2*lift.h(x))%4 for x in range(256)]
    k=[2*g[x]-8*((bits>>x)&1) for x in range(256)]
    v=fw(k);assert all(x%128==0 for x in v);u=[x//128 for x in v]
    assert [(i,x) for i,x in enumerate(u) if abs(x)>1]==[(0,-2),(128,2)]
    assert u[31]==u[159]==0;u[0]+=1;u[128]-=1;u[31]=-1;u[159]=1;u=[-x for x in u]
    for pos,neg,diff in [(41,71,184),(91,15,250)]:
        assert u[pos]==1 and u[neg]==-1 and u[pos^diff]==u[neg^diff]==0
        u[pos]=u[neg]=0;u[pos^diff]=1;u[neg^diff]=-1
    assert sum(u)==0 and sum(x!=0 for x in u)==62 and u[0]==1
    fu=fw(u);assert all(x%2==0 for x in fu);k=[x//2 for x in fu]
    assert k[0]==0 and sum(k)==128 and all(x%2==0 for x in k) and max(map(abs,k))==6
    q=[(x//2)%2 for x in k];qanf=q[:]
    for j in range(8):
        for x in range(256):
            if x&(1<<j):qanf[x]^=qanf[x^(1<<j)]
    assert all(not qanf[x] or x.bit_count()<=2 for x in range(256))
    matrix=[0]*8
    for x,v in enumerate(qanf):
        if v and x.bit_count()==2:
            i,j=[t for t in range(8) if x&(1<<t)];matrix[i]|=1<<j;matrix[j]|=1<<i
    assert rank(matrix)==8
    result={'scope':'finite arithmetic and actual ternary half only, not a nine-variable target witness',
            'six_phase_arithmetic':rows,'ternary_u':u,'half_support':62,'half_spectrum':k,
            'half_peak':max(map(abs,k)),'half_zero_count':sum(x==0 for x in k),
            'q_polar_rank':rank(matrix),'balanced_half':sum(u)==0,'origin_sign':u[0],
            'unreviewed_floor_would_exclude_extension':True}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('six phases checked; concrete balanced ternary half: support 62, rank 8, peak 6')


if __name__=='__main__':main()
