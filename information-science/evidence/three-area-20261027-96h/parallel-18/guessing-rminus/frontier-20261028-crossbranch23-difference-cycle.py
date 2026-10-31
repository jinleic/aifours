#!/usr/bin/env python3
"""Find an exact difference-constraint cycle for fixed cross-branch marginals.

Uses only a subset of full Shannon constraints and optional conditional
independence. A found negative cycle is an exact nonextension witness for the
specified auxiliary marginals, not for the original profile in general.
"""
from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-fixed-u-exact-candidate.json','9744448c5473f3781ef616d46c5615dff649c0f4581dcf7f9bbd4b5c25ee9ce1')
OUTPUT=ROOT/'frontier-20261028-crossbranch23-difference-cycle-result.json'
ORIGINAL=tuple('abcdefghij');PAIRS=(("d'1","f'3"),("d'1","g'3"),("g'2","f'3"))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def main():
    base=pin(BASE);c12=pin(C12);c13=pin(C13)
    original={tuple(sorted(e['entropy_variables'])):Fraction(e['value']) for e in base['primal_values'] if set(e['entropy_variables'])<=set(ORIGINAL)}
    if len(original)!=1023:raise ValueError('BASE_SIZE')
    records=[]
    for a,b in PAIRS:
        variables=ORIGINAL+(a,b);idx={v:i for i,v in enumerate(variables)}
        def mask(labels):return sum(1<<idx[v] for v in labels)
        known={0:Fraction(0)}
        for k,v in original.items():known[mask(k)]=v
        for doc,sym in ((c12,a),(c13,b)):
            for e in doc['auxiliary_values']:
                labs=e['entropy_variables']
                if sym in labs and set(labs)<=set(ORIGINAL)|{sym}:known[mask(labs)]=Fraction(e['value'])
        if len(known)!=3072:raise ValueError('MARGINAL_SIZE')
        scale=lcm(*(x.denominator for x in known.values()));fixed={m:int(x*scale) for m,x in known.items()}
        dummy=1024;edges=[];known_only=0;ignored=0
        def add(terms,meta,equality=False):
            nonlocal known_only,ignored
            C=0;coef={}
            for m,c in terms:
                if m in fixed:C+=c*fixed[m]
                else:
                    if m&3072!=3072:raise ValueError(('NOT_CROSS_MASK',m))
                    i=m&1023;coef[i]=coef.get(i,0)+c
            coef={i:c for i,c in coef.items() if c}
            if not coef:
                known_only+=1
                if (equality and C) or (not equality and C<0):raise ValueError(('KNOWN_CONTRADICTION',meta,C))
                return
            def edge_from(row,constant,sign):
                nonlocal ignored
                if len(row)==1:
                    i,c=next(iter(row.items()))
                    if c==1:src,dst=i,dummy
                    elif c==-1:src,dst=dummy,i
                    else:ignored+=1;return
                elif len(row)==2 and set(row.values())=={-1,1}:
                    src=next(i for i,c in row.items() if c==1);dst=next(i for i,c in row.items() if c==-1)
                else:ignored+=1;return
                edges.append({'src':src,'dst':dst,'cost':int(constant),'metadata':meta,
                              'orientation':sign,'terms':terms})
            edge_from(coef,C,1)
            if equality:edge_from({i:-c for i,c in coef.items()},-C,-1)
        full=4095
        for i in range(12):add(((full,1),(full^(1<<i),-1)),{'kind':'Hconditional','i':i})
        for i,j in combinations(range(12),2):
            x,y=1<<i,1<<j;z=full^x^y
            while True:
                add(((z|x,1),(z|y,1),(z|x|y,-1),(z,-1)),{'kind':'CMI','i':i,'j':j,'z':z})
                if not z:break
                z=(z-1)&(full^x^y)
        X=1023;u,v=1024,2048
        add(((X|u,1),(X|v,1),(X|u|v,-1),(X,-1)),{'kind':'conditional_independence'},True)
        # Entropy nonnegativity h(S,u,v)>=0 is Shannon-valid.
        for i in range(1024):
            edges.append({'src':i,'dst':dummy,'cost':0,'metadata':{'kind':'nonnegative','cross_mask':i},
                          'orientation':1,'terms':((i|3072,1),)})
        graph=[[] for _ in range(1025)]
        for k,e in enumerate(edges):graph[e['src']].append(k)
        dist=[0]*1025;pred=[None]*1025;depth=[0]*1025;queue=deque(range(1025));inq=[True]*1025;hit=None
        while queue and hit is None:
            u=queue.popleft();inq[u]=False
            for ei in graph[u]:
                e=edges[ei];v=e['dst'];x=dist[u]+e['cost']
                if x<dist[v]:
                    dist[v]=x;pred[v]=ei;depth[v]=depth[u]+1
                    if depth[v]>=1025:hit=v;break
                    if not inq[v]:queue.append(v);inq[v]=True
        cycle=[]
        if hit is not None:
            v=hit
            for _ in range(1025):
                if pred[v] is None:raise ValueError('NO_CYCLE_PREDECESSOR')
                v=edges[pred[v]]['src']
            start=v
            while True:
                ei=pred[v]
                if ei is None:raise ValueError('BROKEN_CYCLE')
                cycle.append(ei);v=edges[ei]['src']
                if v==start:break
                if len(cycle)>1025:raise ValueError('CYCLE_LENGTH')
            if sum(edges[i]['cost'] for i in cycle)>=0:raise ValueError('NONNEGATIVE_CYCLE')
        record={'pair':[a,b],'scale':str(scale),'known_only_shannon_checks':known_only,
                'difference_edges':len(edges),'non_difference_inequalities_ignored':ignored,
                'negative_cycle_found':bool(cycle),'cycle_cost_scaled':sum(edges[i]['cost'] for i in cycle) if cycle else None,
                'cycle_rows':[edges[i] for i in cycle]}
        records.append(record)
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],'pairs':records,
         'limits':'Any exact cycle obstructs only the particular fixed pair of auxiliary marginals; alternative source-LP auxiliary assignments and the original base profile may still extend.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps([{k:v for k,v in r.items() if k!='cycle_rows'} for r in records],indent=2))


if __name__=='__main__':main()
