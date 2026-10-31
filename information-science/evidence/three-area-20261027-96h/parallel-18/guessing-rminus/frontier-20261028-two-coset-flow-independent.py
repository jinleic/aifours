#!/usr/bin/env python3
"""Independent integer flow/cut and FD replay for pinned two-coset examples."""
from hashlib import sha256
from math import prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-two-coset-flow-search-result.json','5c81fde2f95ace2debec5024e8e6f0f47b96e85c72d6e0ff15bf5f1d7036ca13')
OUT=ROOT/'frontier-20261028-two-coset-flow-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def geometry(factors):
    Ts=[TRI[t-1] for t in factors];pos={};k=0
    for v in range(1,11):pos[v]=list(range(k,k+sum(v in T for T in Ts)));k+=len(pos[v])
    if k!=18 or any(not pos[v] for v in pos):raise ValueError('GEOMETRY')
    C=[]
    for z in range(4096):
        w=0
        for t,T in enumerate(Ts):
            a=(z>>(2*t))&1;b=(z>>(2*t+1))&1
            for v,x in zip(T,(a,b,a^b)):
                slot=pos[v][[j for j,U in enumerate(Ts) if v in U].index(t)];w|=x<<slot
        C.append(w)
    if len(set(C))!=4096:raise ValueError('CODE')
    if C[0]!=0 or any(C[i]^C[1<<b]!=C[i^(1<<b)] for i in range(4096) for b in range(12)):raise ValueError('CODE_LINEARITY')
    outsider=0
    for t,T in enumerate(Ts):
        v=T[0];slot=pos[v][[j for j,U in enumerate(Ts) if v in U].index(t)];outsider|=1<<slot
    def conflict(z):
        active={v for v in N if any(z>>b&1 for b in pos[v])}
        return any(not(set(N[v])&active) for v in active)
    offsets={i for i,w in enumerate(C) if conflict(outsider^w)}
    return pos,C,outsider,offsets


def score(w,pos,weights):
    out=1
    for v in range(1,11):
        a=sum(((w>>bit)&1)<<j for j,bit in enumerate(pos[v]));out*=weights[v-1][a]**2
    return out


def check(r,geo):
    pos,C,outside,offsets=geo;weights=r['weights'];n=4096
    if len(weights)!=10 or any(len(weights[v-1])!=1<<len(pos[v]) or any(not isinstance(x,int) or x<0 for x in weights[v-1]) or not any(weights[v-1]) for v in range(1,11)):raise ValueError('WEIGHTS')
    if r['cross_degree']!=len(offsets) or r['cross_edges']!=len(offsets)*n:raise ValueError('EDGES')
    A=[score(C[i],pos,weights) for i in range(n)];B=[score(outside^C[i],pos,weights) for i in range(n)]
    L=set(r['selected_left']);R=set(r['selected_right'])
    if len(L)!=len(r['selected_left']) or len(R)!=len(r['selected_right']) or not L<=set(range(n)) or not R<=set(range(n)):raise ValueError('SUPPORT')
    if any((i^d) in R for i in L for d in offsets):raise ValueError('FD_CONFLICT')
    S=sum(A[i] for i in L)+sum(B[j] for j in R)
    if S!=r['max_weight']:raise ValueError('PRIMAL_WEIGHT')
    cover=sum(A[i] for i in range(n) if i not in L)+sum(B[j] for j in range(n) if j not in R)
    left=[0]*n;right=[0]*n;seen=set()
    for i,j,f in r['positive_cross_flows']:
        if not (0<=i<n and 0<=j<n) or (i^j) not in offsets or not isinstance(f,int) or f<=0 or (i,j) in seen:raise ValueError('FLOW_EDGE')
        seen.add((i,j));left[i]+=f;right[j]+=f
    if any(left[i]>A[i] or right[i]>B[i] for i in range(n)):raise ValueError('FLOW_CAPACITY')
    flow=sum(left)
    if flow!=sum(right) or flow!=r['maxflow'] or flow!=cover or flow!=r['cut_capacity']:raise ValueError('FLOW_TOTAL')
    D=prod(sum(x**3 for x in row)**2 for row in weights)
    if str(D)!=r['threshold'] or (S**3>D)!=r['strict_integer_witness']:raise ValueError('POLYNOMIAL')
    return {'factors':r['factors'],'trial':r['trial'],'cross_degree':len(offsets),'flow_edges':len(seen),
            'max_weight':S,'strict_integer_witness':S**3>D,'flow_equals_cut':True}


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);cache={};results=[]
    for r in src['cases']:
        key=tuple(r['factors'])
        if key not in cache:cache[key]=geometry(key)
        results.append(check(r,cache[key]))
    if len(results)!=8 or any(x['strict_integer_witness'] for x in results):raise ValueError('CASE_COUNT')
    bad=json.loads(json.dumps(src['cases'][0]));bad['positive_cross_flows'].pop()
    try:check(bad,cache[tuple(bad['factors'])])
    except ValueError as exc:
        if str(exc)!='FLOW_TOTAL':raise ValueError(('WRONG_REASON',str(exc)))
        control='FLOW_TOTAL'
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'cases':results,'all_checked':True,
         'controls':{'removed_positive_flow':control},
         'limits':'Eight specific integer-weight max-flow/min-cut certificates only; the outer weight search and mathematical oracle reduction are separate.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
