#!/usr/bin/env python3
"""Exact nine-variable Shannon witness for the second cross-copy gluing cut."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-twofamilies-exact-candidate.json','437b5045b998718395469fd47f216e5f426a42fcdc0dd6cfb4e63eff49e0764c')
CAND=('frontier-20261028-crosspair-round3-noind-candidate.json','c22fab73d3b39a333b7c3242bfaa9578327e552f86ae8fe069beddf099cd8a58')
RAY=('frontier-20261028-cross-pair-round3-farkas-independent-result.json','b2e4e3d31006c40774601f0e91bd4ba6651aba1de9b4de3c75f87d64fd1904ac')
OUT=ROOT/'frontier-20261028-nine-variable-gluing-separation-check-result.json'
ORIGINAL=tuple('abcdefghij');PAIR=("g'2","f'3");VARS=ORIGINAL+PAIR
BG=sum(1<<i for i in (0,2,7));ACTIVE=(1,3,4,5,6,8,9,10,11)
COEFF={37:-1,60:-1,127:2,173:1,188:1,236:-1,237:1,255:-2,293:1,
       300:-1,316:1,317:-1,331:-1,347:1,364:1,365:-1,367:1,383:-1}


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def values(base,c12,c13,candidate):
    out={0:Fraction(0)};idx={v:i for i,v in enumerate(VARS)}
    def add(e,required=None):
        labs=e['entropy_variables'];m=sum(1<<idx[v] for v in labs)
        if not m or m in out or (required is not None and not required<=set(labs)):raise ValueError('DUPLICATE_OR_LABEL')
        out[m]=Fraction(e['value'])
    for e in base['primal_values']:
        if set(e['entropy_variables'])<=set(ORIGINAL):add(e)
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for doc,sym in ((c12,PAIR[0]),(c13,PAIR[1])):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if sym in labs and set(labs)<=set(ORIGINAL)|{sym}:add(e,{sym})
    if len(out)!=3072 or tuple(candidate['pair'])!=PAIR:raise ValueError('MARGINALS')
    for e in candidate['cross_values']:add(e,set(PAIR))
    if len(out)!=4096:raise ValueError('ALL_SIZE')
    return out


def elemental(arr,n):
    full=(1<<n)-1;count=0
    if len(arr)!=(1<<n) or arr[0]!=0 or min(arr)<0:raise ValueError(('VECTOR',n))
    for i in range(n):
        if arr[full]-arr[full^(1<<i)]<0:raise ValueError(('H',n,i))
        count+=1
    for i,j in combinations(range(n),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            if arr[z|a]+arr[z|b]-arr[z|a|b]-arr[z]<0:raise ValueError(('CMI',n,i,j,z))
            count+=1
            if not z:break
            z=(z-1)&(full^a^b)
    return count


def verify_nine(r,coeff):
    scale=lcm(*(x.denominator for x in r));ints=[int(x*scale) for x in r]
    rows=elemental(ints,9)
    if rows!=4617:raise ValueError('NINE_COUNT')
    value=sum((Fraction(c)*r[m] for m,c in coeff.items()),Fraction(0))
    if value!=Fraction(-7123,3450000):raise ValueError(('VALUE',str(value)))
    return value


def main():
    base,c12,c13,candidate,ray=map(pin,(BASE,C12,C13,CAND,RAY))
    if not ray['all_checked'] or ray['exact_identity']['known_constant']!='-7123/3450000':raise ValueError('RAY')
    mapped={}
    for m,c in ray['exact_identity']['known_terms']:
        if m&BG!=BG:raise ValueError('BACKGROUND')
        s=sum(1<<j for j,i in enumerate(ACTIVE) if m&(1<<i));mapped[s]=mapped.get(s,0)+int(Fraction(c))
    if mapped!=COEFF or sum(COEFF.values())!=0:raise ValueError('TERM_MAP')
    h=values(base,c12,c13,candidate);scale=lcm(*(v.denominator for v in h.values()));hi=[int(h[m]*scale) for m in range(4096)]
    rows12=elemental(hi,12)
    if rows12!=67596:raise ValueError('TWELVE_COUNT')
    r=[h[BG|sum(1<<ACTIVE[j] for j in range(9) if s&(1<<j))]-h[BG] for s in range(512)]
    value=verify_nine(r,COEFF)
    ci=h[1023|1024]+h[1023|2048]-h[4095]-h[1023]
    if ci<Fraction(7123,6900000):raise ValueError('FARKAS_CI')
    controls={}
    def expect(tag,mut):
        rr=list(r);cc=dict(COEFF);mut(rr,cc)
        try:
            if cc!=COEFF:raise ValueError('COEFFICIENT_MAP')
            verify_nine(rr,cc)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('nonzero_empty',lambda rr,cc:rr.__setitem__(0,Fraction(1)))
    expect('changed_witness_coordinate',lambda rr,cc:rr.__setitem__(37,rr[37]+Fraction(1,7)))
    expect('flipped_coefficient',lambda rr,cc:cc.__setitem__(37,1))
    expect('missing_witness_coordinate',lambda rr,cc:rr.pop())
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'twelve_variable_candidate_sha256':CAND[1],'ray_receipt_sha256':RAY[1],
         'twelve_variable_elemental_checks':rows12,'nine_variable_elemental_checks':4617,
         'nine_variable_order':['B=b','R=d','E=e','T=f','G=g','I=i','J=j',"P=g'2","Q=f'3"],
         'nine_variable_inequality':[[m,c] for m,c in sorted(COEFF.items())],
         'nine_variable_primal_values':[str(x) for x in r],
         'inequality_value':str(value),'conditional_mutual_information_DF_given_X':str(ci),
         'all_checked':True,'mutation_controls':controls,
         'limits':'Exact Shannon-cone separation for one 9-variable gluing inequality; no novelty, full source reoptimization, entropic realization or graph improvement is claimed.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='nine_variable_primal_values'},indent=2))


if __name__=='__main__':main()
