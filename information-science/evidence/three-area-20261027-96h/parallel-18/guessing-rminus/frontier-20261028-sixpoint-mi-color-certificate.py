#!/usr/bin/env python3
"""Exact potential-MI graph color certificates for six selected 6-atom laws."""
from itertools import combinations
from math import prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-sixpoint-mi-color-certificate-result.json'
WEIGHTS=((20,20,1,1,1,1),(40,20,1,1,1,1),(50,5,1,1,1,1),
         (100,100,2,2,1,1),(100,50,3,2,1,1),(100,5,4,3,2,1))


def partitions():
    out=[]
    def visit(a):
        if len(a)==6:
            if 1<len(set(a))<6:out.append(tuple(a))
            return
        for x in range(max(a)+2):visit(a+[x])
    visit([0])
    if len(out)!=201:raise ValueError('PARTITIONS')
    return out


def factor(part,w):
    blocks=[sum(w[i] for i,x in enumerate(part) if x==v) for v in set(part)]
    return prod(z**z for z in blocks)


def potential(p,q,w,fp,fq,total):
    joint=factor(tuple(zip(p,q)),w)
    return fp*fq*fq>=total*joint*joint and fq*fp*fp>=total*joint*joint


def main():
    parts=partitions();results=[]
    for w in WEIGHTS:
        f=[factor(p,w) for p in parts];total=sum(w)**sum(w);n=len(parts);neighbors=[0]*n;edges=0
        for i,j in combinations(range(n),2):
            if potential(parts[i],parts[j],w,f[i],f[j],total):neighbors[i]|=1<<j;neighbors[j]|=1<<i;edges+=1
        colors=[-1]*n;pool=(1<<n)-1;count=0
        while pool:
            available=pool
            while available:
                bit=available&-available;i=bit.bit_length()-1;colors[i]=count;pool^=bit;available&=~bit;available&=~neighbors[i]
            count+=1
        if count>9 or any(colors[i]==colors[j] and neighbors[i]>>j&1 for i,j in combinations(range(n),2)):raise ValueError('COLOR')
        results.append({'weights':list(w),'potential_mi_edges':edges,'color_count':count,'partition_colors':colors})
    out={'partitions':[list(p) for p in parts],'cases':results,'all_checked':True,
         'limits':'Exact finite potential-MI graph coloring certificates. Entropy/FD and open-neighborhood deductions are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'partition_count':len(parts),'cases':[{'weights':x['weights'],'potential_mi_edges':x['potential_mi_edges'],'color_count':x['color_count']} for x in results],'all_checked':True},indent=2))


if __name__=='__main__':main()
