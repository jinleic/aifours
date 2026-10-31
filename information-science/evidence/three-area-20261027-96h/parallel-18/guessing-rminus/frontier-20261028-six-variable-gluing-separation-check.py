#!/usr/bin/env python3
"""Exact six-variable Shannon-cone separator for the universal gluing inequality.

Independently checks all 12-variable elemental inequalities for a pinned
extension, contracts its six background variables, checks every 6-variable
elemental inequality and compares the inequality with the pinned term map.
"""
from copy import deepcopy
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
CAND=('frontier-20261028-crosspair-without-independence-candidate.json','0259b6597fcaa899a77bf5ccc4274eaaae825ee452304815fa3b44543e1a5bcb')
MAP=('frontier-20261028-universal-gluing-term-map-check-result.json','26ef7de315636d0e0aad1728567953ea0b00e96467bc424f04e561d722a0c1ab')
OUTPUT=ROOT/'frontier-20261028-six-variable-gluing-separation-check-result.json'
ORIGINAL=tuple('abcdefghij');PAIR=("d'1","f'3");VARS=ORIGINAL+PAIR
BG=sum(1<<i for i in (0,4,5,6,8,9));ACTIVE=(1,2,3,7,10,11)
COEFF={3:-1,5:-1,15:2,19:1,21:1,23:-1,25:-1,27:1,31:-1,
       33:-1,35:1,37:1,41:1,42:-1,46:1,47:-2}


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def values(base,c12,c13,cand):
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
    if len(out)!=3072:raise ValueError('SINGLE_MARGINALS')
    if tuple(cand['pair'])!=PAIR:raise ValueError('PAIR')
    for e in cand['cross_values']:add(e,set(PAIR))
    if len(out)!=4096:raise ValueError('ALL_SIZE')
    return out


def elemental(arr,n):
    full=(1<<n)-1;checks=0
    if len(arr)!=(1<<n) or arr[0]!=0 or min(arr)<0:raise ValueError(('VECTOR',n))
    for i in range(n):
        if arr[full]-arr[full^(1<<i)]<0:raise ValueError(('MONOTONE',n,i))
        checks+=1
    for i,j in combinations(range(n),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            if arr[z|a]+arr[z|b]-arr[z|a|b]-arr[z]<0:raise ValueError(('CMI',n,i,j,z))
            checks+=1
            if not z:break
            z=(z-1)&(full^a^b)
    return checks


def check_six(r,coefficient):
    scale=lcm(*(x.denominator for x in r));ints=[int(x*scale) for x in r]
    count=elemental(ints,6)
    if count!=246:raise ValueError('SIX_CHECK_COUNT')
    value=sum((Fraction(c)*r[m] for m,c in coefficient.items()),Fraction(0))
    if value!=Fraction(-12637,1725000):raise ValueError(('VALUE',str(value)))
    return value


def main():
    base,c12,c13,candidate,termmap=map(pin,(BASE,C12,C13,CAND,MAP))
    if not termmap['exact_map_matches_written_proof'] or termmap['term_count']!=16:raise ValueError('TERM_MAP')
    # Contract the common background in the independently checked 12-variable map.
    mapped={}
    for e in termmap['term_map']:
        m=e['mask']
        if m&BG!=BG:raise ValueError('BACKGROUND_NOT_COMMON')
        s=sum(1<<j for j,i in enumerate(ACTIVE) if m&(1<<i))
        mapped[s]=mapped.get(s,0)+e['coefficient']
    if mapped!=COEFF:raise ValueError(('SIX_MAP',mapped))
    h=values(base,c12,c13,candidate);scale=lcm(*(v.denominator for v in h.values()));hi=[int(h[m]*scale) for m in range(4096)]
    c12rows=elemental(hi,12)
    if c12rows!=67596:raise ValueError('TWELVE_CHECK_COUNT')
    r=[]
    for s in range(64):
        m=BG|sum(1<<ACTIVE[j] for j in range(6) if s&(1<<j))
        r.append(h[m]-h[BG])
    value=check_six(r,COEFF)
    if sum(COEFF.values())!=0:raise ValueError('CONDITIONING_CONSTANT')
    mi=h[1023|1024]+h[1023|2048]-h[4095]-h[1023]
    if mi<Fraction(12637,3450000):raise ValueError('FARKAS_LOWER_BOUND')
    controls={}
    def expect(tag,mut):
        rr=list(r);cc=dict(COEFF);mut(rr,cc)
        try:
            if cc!=COEFF:raise ValueError('COEFFICIENT_MAP')
            check_six(rr,cc)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('nonzero_empty',lambda rr,cc:rr.__setitem__(0,Fraction(1)))
    expect('changed_witness_coordinate',lambda rr,cc:rr.__setitem__(3,rr[3]+Fraction(1,7)))
    expect('flipped_coefficient',lambda rr,cc:cc.__setitem__(3,1))
    expect('missing_witness_coordinate',lambda rr,cc:rr.pop())
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'twelve_variable_candidate_sha256':CAND[1],'term_map_receipt_sha256':MAP[1],
         'twelve_variable_elemental_checks':c12rows,'six_variable_elemental_checks':246,
         'six_variable_order':['B=b','C=c','R=d','H=h',"P=d'1","Q=f'3"],
         'six_variable_inequality':[[m,c] for m,c in sorted(COEFF.items())],
         'six_variable_primal_values':[str(x) for x in r],
         'inequality_value':str(value),'conditional_mutual_information_DF_given_X':str(mi),
         'all_checked':True,'mutation_controls':controls,
         'limits':'Exact separation of one universal 6-variable entropy inequality from the 6-variable Shannon cone; does not imply a new guessing-number upper bound or novelty clearance.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='six_variable_primal_values'},indent=2))


if __name__=='__main__':main()
