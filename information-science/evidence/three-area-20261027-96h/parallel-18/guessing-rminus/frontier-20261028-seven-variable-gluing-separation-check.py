#!/usr/bin/env python3
"""Exact seven-variable Shannon witness for the second cross-copy gluing cut."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-all-cuts-exact-candidate.json','1d7263364c8c543bdd07a4b140c7a7ab2d65753c38506f26c02072fc9bd29703')
CAND=('frontier-20261028-crosspair-round2-noind-candidate.json','558e3cfb52d5090beeac4362bff5a6a429cc27a64b285b5722d55043a26fcc92')
RAY=('frontier-20261028-cross-pair-round2-farkas-independent-result.json','29341b5eb23bcfaecf7bc350514ff38f76b17b3de4d88326b4561778a897dff9')
OUT=ROOT/'frontier-20261028-seven-variable-gluing-separation-check-result.json'
ORIGINAL=tuple('abcdefghij');PAIR=("d'1","g'3");VARS=ORIGINAL+PAIR
BG=sum(1<<i for i in (0,2,6,7,9));ACTIVE=(1,3,4,5,8,10,11)
COEFF={7:-1,17:-1,31:2,39:1,41:-1,49:1,57:1,63:-2,65:-1,
       71:1,73:1,81:1,86:-1,89:-1,92:-1,93:1,94:2,95:-2}


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


def verify_seven(r,coeff):
    scale=lcm(*(x.denominator for x in r));ints=[int(x*scale) for x in r]
    rows=elemental(ints,7)
    if rows!=679:raise ValueError('SEVEN_COUNT')
    value=sum((Fraction(c)*r[m] for m,c in coeff.items()),Fraction(0))
    if value!=Fraction(-867,460000):raise ValueError(('VALUE',str(value)))
    return value


def main():
    base,c12,c13,candidate,ray=map(pin,(BASE,C12,C13,CAND,RAY))
    if not ray['all_checked'] or ray['exact_identity']['known_constant']!='-867/460000':raise ValueError('RAY')
    mapped={}
    for m,c in ray['exact_identity']['known_terms']:
        if m&BG!=BG:raise ValueError('BACKGROUND')
        s=sum(1<<j for j,i in enumerate(ACTIVE) if m&(1<<i));mapped[s]=mapped.get(s,0)+int(Fraction(c))
    if mapped!=COEFF or sum(COEFF.values())!=0:raise ValueError('TERM_MAP')
    h=values(base,c12,c13,candidate);scale=lcm(*(v.denominator for v in h.values()));hi=[int(h[m]*scale) for m in range(4096)]
    rows12=elemental(hi,12)
    if rows12!=67596:raise ValueError('TWELVE_COUNT')
    r=[h[BG|sum(1<<ACTIVE[j] for j in range(7) if s&(1<<j))]-h[BG] for s in range(128)]
    value=verify_seven(r,COEFF)
    ci=h[1023|1024]+h[1023|2048]-h[4095]-h[1023]
    if ci<Fraction(867,920000):raise ValueError('FARKAS_CI')
    controls={}
    def expect(tag,mut):
        rr=list(r);cc=dict(COEFF);mut(rr,cc)
        try:
            if cc!=COEFF:raise ValueError('COEFFICIENT_MAP')
            verify_seven(rr,cc)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('nonzero_empty',lambda rr,cc:rr.__setitem__(0,Fraction(1)))
    expect('changed_witness_coordinate',lambda rr,cc:rr.__setitem__(7,rr[7]+Fraction(1,7)))
    expect('flipped_coefficient',lambda rr,cc:cc.__setitem__(7,1))
    expect('missing_witness_coordinate',lambda rr,cc:rr.pop())
    out={'base_sha256':BASE[1],'cross12_sha256':C12[1],'cross13_sha256':C13[1],
         'twelve_variable_candidate_sha256':CAND[1],'ray_receipt_sha256':RAY[1],
         'twelve_variable_elemental_checks':rows12,'seven_variable_elemental_checks':679,
         'seven_variable_order':['B=b','R=d','E=e','T=f','I=i',"P=d'1","Q=g'3"],
         'seven_variable_inequality':[[m,c] for m,c in sorted(COEFF.items())],
         'seven_variable_primal_values':[str(x) for x in r],
         'inequality_value':str(value),'conditional_mutual_information_DF_given_X':str(ci),
         'all_checked':True,'mutation_controls':controls,
         'limits':'Exact Shannon-cone separation for one 7-variable gluing inequality; no novelty, full source reoptimization, entropic realization or graph improvement is claimed.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='seven_variable_primal_values'},indent=2))


if __name__=='__main__':main()
