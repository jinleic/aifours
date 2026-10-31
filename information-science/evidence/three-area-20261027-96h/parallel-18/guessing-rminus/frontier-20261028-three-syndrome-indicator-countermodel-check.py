#!/usr/bin/env python3
"""Exact counterpolymatroid to a specified indicator-gate induction."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
ERR=('frontier-20261028-full-source-lp-optimum-v1-erratum-1.md','c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9')
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
OUT=ROOT/'frontier-20261028-three-syndrome-indicator-countermodel-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
V=(1<<10)-1;B=1<<10;FULL=(1<<11)-1

def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('PIN')
    return raw

def mask(names):return sum(1<<(ord(x)-ord('a')) for x in names)

def main():
    if b'REQUIRED BEFORE SOURCE' not in pin(ERR):raise ValueError('ERRATUM')
    source=json.loads(pin(BASE));h=[Fraction(0) for _ in range(V+1)];seen=set();allowed=set('abcdefghij')
    for x in source['primal_values']:
        if set(x['entropy_variables'])<=allowed:
            m=mask(x['entropy_variables'])
            if not m or m in seen:raise ValueError('BASE_COORDINATES')
            seen.add(m);h[m]=3*Fraction(x['value'])
    if len(seen)!=V:raise ValueError('BASE_COORDINATES')
    delta=h[V]-Fraction(2,3)*sum(h[1<<i] for i in range(10))
    if delta!=Fraction(7,92) or any(h[1<<i]!=3 for i in range(10)):raise ValueError('BASE_GAP')
    kappas=[2*delta,delta,delta,delta]
    hs=[[min(h[a]+k,h[V]) for a in range(V+1)] for k in kappas]
    def H(a,b):return hs[b-1][a&V] if a&B else h[a]
    count=0
    for branch in range(1,5):
        if H(V|B,branch)!=h[V] or H(B,branch)!=kappas[branch-1]:raise ValueError('AUX_DETERMINISM')
        for i in range(11):
            if H(FULL,branch)<H(FULL^(1<<i),branch):raise ValueError('MONOTONICITY')
        for i,j in combinations(range(11),2):
            a,b=1<<i,1<<j;rest=FULL^a^b;k=rest
            while True:
                if H(k|a,branch)+H(k|b,branch)-H(k|a|b,branch)-H(k,branch)<0:raise ValueError('CMI')
                count+=1
                if not k:break
                k=(k-1)&rest
        gate=3*h[V]+17*H(B,branch)-2*sum(H(B|(1<<i),branch) for i in range(10))
        if gate>0:raise ValueError('GATE')
    for v,nb in N.items():
        n=sum(1<<(u-1) for u in nb)
        if h[n|1<<(v-1)]!=h[n]:raise ValueError('FD')
    for a in range(V+1):
        s=hs[0][a]-h[a];ind=[hs[b][a]-h[a] for b in (1,2,3)]
        if any(x>s for x in ind) or s>sum(ind) or any(s>ind[j]+ind[k] for j,k in combinations(range(3),2)):raise ValueError('ONEHOT_OUTER')
    # Extend to a 14-coordinate abstract polymatroid: S and any two
    # indicator coordinates determine the same full syndrome rank.
    def H14(m):
        a=m&V;aux=m>>10
        if not aux:return h[a]
        if aux&1 or (aux>>1).bit_count()>=2:return hs[0][a]
        return hs[(aux>>1).bit_length()][a]
    full14=(1<<14)-1;full_count=0
    for i in range(14):
        if H14(full14)<H14(full14^(1<<i)):raise ValueError('FULL_MONOTONICITY')
    for i,j in combinations(range(14),2):
        a,b=1<<i,1<<j;rest=full14^a^b;k=rest
        while True:
            if H14(k|a)+H14(k|b)-H14(k|a|b)-H14(k)<0:raise ValueError('FULL_CMI')
            full_count+=1
            if not k:break
            k=(k-1)&rest
    old=h[V];h[V]+=Fraction(1,7)
    try:
        if hs[1][V]!=h[V]:raise ValueError('AUX_DETERMINISM')
    except ValueError as e:control=str(e)
    else:raise ValueError('MUTATION_ACCEPTED')
    h[V]=old
    out={'base_sha256':BASE[1],'required_pre_source_erratum_sha256':ERR[1],'scale':3,'gap':str(delta),'syndrome_entropy':str(kappas[0]),
         'indicator_entropies':[str(x) for x in kappas[1:]],'elemental_cmi_checks':count,'auxiliary_monotonicity_checks':44,
         'full_14_variable_cmi_checks':full_count,'full_14_variable_monotonicity_checks':14,
         'conditional_indicator_subsets':V+1,'all_checked':True,'negative_control':control,
         'limits':'Synthetic full 14-variable Shannon polymatroid with the listed indicator functional relations; it need not have a joint one-hot realization. Not an actual law, guessing strategy, or full-copy extension.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
