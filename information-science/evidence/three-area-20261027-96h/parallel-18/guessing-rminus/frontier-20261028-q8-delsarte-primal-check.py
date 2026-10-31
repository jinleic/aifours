#!/usr/bin/env python3
"""Exact orbit/Fourier feasibility check for the q=8 Delsarte primal."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-q8-delsarte-primal-v1.json','9608294d56bcaa625fe4f59d113e1adda279b22fc5e8cd05d4d4587193b21fbf')
OUT=ROOT/'frontier-20261028-q8-delsarte-primal-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))


def group():
    edges={tuple(sorted((v-1,w-1))) for v in N for w in N[v]}
    for p in GEN:
        if set(p)!=set(range(10)) or {tuple(sorted((p[a],p[b]))) for a,b in edges}!=edges:raise ValueError('AUTOMORPHISM')
    e=tuple(range(10));seen={e};queue=[e]
    while queue:
        p=queue.pop()
        for g in GEN:
            q=tuple(g[p[i]] for i in range(10))
            if q not in seen:seen.add(q);queue.append(q)
    if len(seen)!=8:raise ValueError('GROUP')
    return seen


def image(mask,p):return sum(1<<p[i] for i in range(10) if mask>>i&1)


def orbits(masks,G):
    remain=set(masks);out=[]
    while remain:
        x=min(remain);o=sorted({image(x,p) for p in G})
        if not set(o)<=remain:raise ValueError('ORBIT_PARTITION')
        out.append(o);remain-=set(o)
    return out


def check(cert):
    if cert['alphabet_size']!=8 or cert['denominator']!=4724:raise ValueError('HEADER')
    G=group();nb=[sum(1<<(w-1) for w in N[v]) for v in range(1,11)]
    allowed=[s for s in range(1024) if all(s&nb[i] for i in range(10) if s>>i&1)]
    S=orbits(allowed,G);T=orbits(range(1024),G);rows=cert['orbits']
    if len(allowed)!=911 or len(S)!=162 or len(T)!=186 or len(rows)!=len(S):raise ValueError('COUNTS')
    nums=[]
    for row,orbit in zip(rows,S):
        if row['representative_mask']!=orbit[0] or row['orbit_size']!=len(orbit) or not isinstance(row['numerator'],int):raise ValueError('ORBIT')
        if row['numerator']<0:raise ValueError('NONNEGATIVE')
        nums.append(row['numerator'])
    if nums[0]!=cert['denominator']:raise ValueError('NORMALIZATION')
    tight=0;minimum=None
    for orbit in T:
        t=orbit[0];weight=t.bit_count();value=0
        for sub,numerator in zip(S,nums):
            coefficient=(8//len(sub))*sum((-1)**((s&t).bit_count())*7**(weight-(s&t).bit_count()) for s in sub)
            value+=coefficient*numerator
        if value<0:raise ValueError(('FOURIER',t,value))
        if value==0:tight+=1
        minimum=value if minimum is None else min(minimum,value)
    objective=Fraction(sum(nums),cert['denominator'])
    if objective!=Fraction(2256535552,1181) or objective<=Fraction(3*(2**20),2):raise ValueError('OBJECTIVE')
    return {'graph_automorphisms':len(G),'allowed_support_masks':len(allowed),'support_orbits':len(S),
            'character_orbits':len(T),'fourier_rows_checked':len(T),'tight_fourier_orbits':tight,
            'minimum_scaled_fourier_slack':minimum,'objective':str(objective),'exceeds_three_halves_triangle':True}


def main():
    raw=(ROOT/CERT[0]).read_bytes()
    if sha256(raw).hexdigest()!=CERT[1]:raise ValueError('HASH')
    cert=json.loads(raw);checks=check(cert);controls={}
    for name,mut,expected in (
        ('changed_normalization',lambda x:x['orbits'][0].__setitem__('numerator',x['orbits'][0]['numerator']-1),'NORMALIZATION'),
        ('negative_mass',lambda x:x['orbits'][1].__setitem__('numerator',-1),'NONNEGATIVE'),
        ('changed_fourier_mass',lambda x:x['orbits'][1].__setitem__('numerator',x['orbits'][1]['numerator']-1),'FOURIER')):
        bad=json.loads(json.dumps(cert));mut(bad)
        try:check(bad)
        except ValueError as exc:
            text=str(exc)
            if expected not in text:raise ValueError(('WRONG_REASON',name,text))
            controls[name]=expected
        else:raise ValueError(('CONTROL_ACCEPTED',name))
    out={'candidate_sha256':CERT[1],'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Fractional feasible point for the explicitly defined support-orbit Delsarte LP, not an actual code, entropy law or exact LP optimum.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
