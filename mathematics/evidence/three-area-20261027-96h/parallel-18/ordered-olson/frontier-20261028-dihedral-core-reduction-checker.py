#!/usr/bin/env python3
"""Check exact subset-sum lemma and structural reductions on saved words."""
import argparse
from collections import Counter
import hashlib
import itertools
import json


def product(word,idx,p):
    exponent,parity=0,0
    for i in idx:
        x,b=word[i]
        exponent=(exponent+(-x if parity else x))%p
        parity ^= b
    return exponent,parity


def valid_selector(word,idx,p):
    return len(idx)==2*p and len(set(idx))==2*p and product(word,sorted(idx),p)==(0,0)


def subsets(values,p):
    table={0:[]}
    for i,x in enumerate(values):
        new=dict(table)
        for value,inds in table.items():
            new.setdefault((value+x)%p,inds+[i])
        table=new
    return table


def no_nonempty_zero(values,p):
    support={0}
    for d in values:
        if (-d)%p in support:
            return False
        support |= {(x+d)%p for x in support}
    return True


def exhaustive_missing_sum_lemma():
    results={}
    for p in (3,5,7):
        tested=zero_free=one_missing=full=0
        for values in itertools.product(range(1,p),repeat=p-2):
            tested+=1
            if not no_nonempty_zero(values,p):
                continue
            zero_free+=1
            A=set(subsets(values,p))
            if len(A)<p-1:
                raise ValueError('subset growth failed')
            if len(A)==p-1:
                one_missing+=1
                missing=next(x for x in range(p) if x not in A)
                if any(d != (-missing)%p for d in values):
                    raise ValueError('missing-sum equality lemma false')
            else:
                full+=1
        results[str(p)]={'tested':tested,'zero_sum_free':zero_free,'one_missing':one_missing,'full_support':full}
    return results


def signed_eligible(word,p,i,j):
    count=Counter(((-x if i<k<j else x)%p) for k,(x,b) in enumerate(word) if not b)
    return max(count.values())<=2*p-2


def long_runs(word):
    refs=[]
    i=0
    while i<len(word):
        if not word[i][1]:
            i+=1
            continue
        j=i
        while j<len(word) and word[j][1]:
            j+=1
        if j-i>=3:
            refs.append(list(range(i,j)))
        i=j
    return refs


def analyze(case):
    p,word=case['p'],case['word']
    rotations=[i for i,(_,b) in enumerate(word) if b==0]
    refs=[i for i,(_,b) in enumerate(word) if b==1]
    if len(rotations)!=3*p-3 or len(refs)!=p+2:
        raise ValueError('wrong original count band')
    eligible=[(i,j) for i,j in itertools.combinations(refs,2) if signed_eligible(word,p,i,j)]
    if eligible:
        return 'signed-pair eligible',0
    values=Counter(word[k][0] for k in rotations)
    if values[0]>=2*p-1:
        by_value={}
        for i in refs:
            y=word[i][0]
            if y in by_value:
                idx=sorted([k for k in rotations if word[k][0]==0][:2*p-2]+[by_value[y],i])
                if not valid_selector(word,idx,p):
                    raise ValueError('zero core selector fails')
                return 'zero core selector',0
            by_value[y]=i
        raise ValueError('reflection duplicate missing')
    for a,m in values.items():
        if m>=2*p:
            idx=[k for k in rotations if word[k][0]==a][:2*p]
            if not valid_selector(word,idx,p):
                raise ValueError('constant rotation selector fails')
            return 'constant rotation selector',0
        if a and m>=p and values[-a%p]>=p:
            idx=[k for k in rotations if word[k][0]==a][:p]+[k for k in rotations if word[k][0]==(-a)%p][:p]
            if not valid_selector(word,idx,p):
                raise ValueError('opposite rotation selector fails')
            return 'opposite rotation selector',0
    cores=[a for a,m in values.items() if a!=0 and m==2*p-1]
    if len(cores)!=1:
        raise ValueError('concentration conclusion false')
    a=cores[0]
    core=[k for k in rotations if word[k][0]==a]
    extras=[k for k in rotations if word[k][0]!=a]
    if len(extras)!=p-2:
        raise ValueError('extra count mismatch')
    delta=[(word[k][0]-a)%p for k in extras]
    # All nonempty extra subsets correspond exactly to 2p rotations.
    for mask in range(1,1<<len(extras)):
        chosen=[extras[t] for t in range(len(extras)) if mask>>t&1]
        actual=sorted(chosen+core[:2*p-len(chosen)])
        if (sum(delta[t] for t in range(len(extras)) if mask>>t&1)%p==0) != valid_selector(word,actual,p):
            raise ValueError('rotation-only subset equivalence false')
    A=subsets(delta,p)
    for i,j in itertools.combinations(refs,2):
        between=sum(i<k<j for k in core)
        if between in (p-1,p):
            raise ValueError('unpaid central core crossing')
    if not no_nonempty_zero(delta,p):
        return 'core with rotation selector',0
    examined=0
    for run in long_runs(word):
        examined+=1
        missing_target=False
        for i,j in itertools.combinations(run,2):
            target=(word[j][0]-word[i][0]+2*a)%p
            if target in A:
                extra_indices=[extras[t] for t in A[target]]
                idx=sorted(extra_indices+core[:2*p-2-len(extra_indices)]+[i,j])
                if not valid_selector(word,idx,p):
                    raise ValueError('run pair selector fails')
                missing_target=True
                break
        if missing_target:
            continue
        if len(A)!=p-1 or any(d!=(-2*a)%p for d in delta):
            raise ValueError('exceptional run delta consequence false')
        if len({word[i][0] for i in run})!=1:
            raise ValueError('exceptional run not constant')
        if len(run)>=4:
            idx=sorted(core[:p-2]+extras+run[:4])
            if not valid_selector(word,idx,p):
                raise ValueError('four-reflection selector fails')
    return 'core residual',examined


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    raw=open(args.input,'rb').read()
    data=json.loads(raw)
    category=Counter()
    run_cases=0
    for case in data['cases']+data['structured']:
        kind,count=analyze(case)
        category[kind]+=1
        run_cases+=count
    proof_checks=exhaustive_missing_sum_lemma()
    result={'result':'PASS_CORE_REDUCTION_BOUNDED_CHECK',
            'input_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_original_words_reexamined':len(data['cases'])+len(data['structured']),
            'structural_categories':dict(category),'core_long_runs_examined':run_cases,
            'exhaustive_subset_sum_lemma':proof_checks,
            'scope':'bounded checks of written lemmas only; ineligible pairs are not no-go certificates'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,indent=2,sort_keys=True)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
