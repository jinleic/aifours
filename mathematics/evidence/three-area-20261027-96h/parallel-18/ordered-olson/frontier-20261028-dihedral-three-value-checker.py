#!/usr/bin/env python3
"""Independent exact checks for next-band diverse signed swaps."""
import argparse
from collections import Counter
import copy
import hashlib
import itertools
import json


def direct(word,indices,p):
    a,b=0,0
    for i in indices:
        x,y=word[i]
        a=(a+((-1 if b else 1)*x))%p
        b^=y
    return a,b


def inverse_check():
    report={}
    for p in (3,5,7):
        total=one_missing=full=0
        for values in itertools.product(range(1,p),repeat=p-2):
            total+=1
            support={0}
            for d in values:
                support |= {(x+d)%p for x in support}
            if len(support)<p-1:
                raise ValueError('translation growth failed')
            if len(support)==p-1:
                one_missing+=1
                d=values[0]
                if any(v not in (d,(-d)%p) for v in values):
                    raise ValueError('diverse increments with one-missing support')
            else:
                full+=1
        report[str(p)]={'total':total,'one_missing':one_missing,'full':full}
    return report


def check_pair(word,p,r):
    i,j=r['reflections']
    if not (0<=i<j<len(word) and word[i][1] and word[j][1]):
        raise ValueError('invalid reflection positions')
    signed={k:(-v if i<k<j else v)%p for k,(v,b) in enumerate(word) if not b}
    counts=Counter(signed.values())
    M=max(counts.values())
    major=max(counts,key=lambda x:(counts[x],x))
    classes={min((v-major)%p,(major-v)%p) for v in counts if v!=major}
    if (r['signed_max'],r['signed_support'],r['nonmajor_difference_classes'])!=(M,len(counts),len(classes)):
        raise ValueError('wrong signed-multiset summary')
    eligible=len(counts)>=3 and (M<=2*p-3 or (M==2*p-2 and len(classes)>=2))
    if eligible!=r['eligible']:
        raise ValueError('wrong sufficient-condition classification')
    if not eligible:
        return False
    pairs,omitted,selected=r['unequal_signed_pairs'],r['omitted_rotations'],r['selected_indices']
    if len(pairs)!=p-2 or any(len(pair)!=2 for pair in pairs):
        raise ValueError('wrong pair count')
    flat=[k for pair in pairs for k in pair]
    if len(set(flat))!=len(flat) or any(k not in signed for k in flat):
        raise ValueError('signed pair index reused')
    if any(signed[a]==signed[b] for a,b in pairs):
        raise ValueError('equal signed pair')
    deltas=[(signed[b]-signed[a])%p for a,b in pairs]
    if all(d in (deltas[0],(-deltas[0])%p) for d in deltas):
        raise ValueError('swap differences lack diversity')
    reachable={0}
    for d in deltas:
        reachable |= {(v+d)%p for v in reachable}
    if len(reachable)!=p:
        raise ValueError('swap sums not full Fp')
    if len(set(omitted))!=p-2 or any(len(set(pair).intersection(omitted))!=1 for pair in pairs):
        raise ValueError('wrong omitted occurrences')
    if len(selected)!=2*p or selected!=sorted(set(selected)) or any(k<0 or k>=len(word) for k in selected):
        raise ValueError('bad original selector indices')
    if set(selected)!=(set(signed)-set(omitted)) | {i,j}:
        raise ValueError('wrong selected complement')
    if direct(word,selected,p)!=(0,0):
        raise ValueError('nonidentity original product')
    return True


def check_word(case):
    p,word=case['p'],case['word']
    if len(word)!=4*p-1 or sum(b==0 for _,b in word)!=3*p-4 or any(x<0 or x>=p or b not in (0,1) for x,b in word):
        raise ValueError('wrong original word')
    refs=[k for k,(_,b) in enumerate(word) if b]
    expected=[list(pair) for pair in itertools.combinations(refs,2)]
    if [r['reflections'] for r in case['pairs']]!=expected:
        raise ValueError('incomplete reflection-pair coverage')
    return sum(check_pair(word,p,r) for r in case['pairs'])


def mutation(case,edit,expected):
    copied=copy.deepcopy(case)
    row=next(r for r in copied['pairs'] if r['eligible'])
    edit(row)
    try:
        check_pair(copied['word'],copied['p'],row)
    except ValueError as exc:
        if str(exc)==expected:
            return expected
        raise ValueError('mutation wrong failure: '+str(exc)) from exc
    raise ValueError('mutation survived')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:
        raw=source.read()
    data=json.loads(raw)
    counts=[check_word(case) for case in data['cases']]
    special_counts=[check_word(case) for case in data['special']]
    for case in data['special']:
        p=case['p']
        if not case['pairs'][0]['eligible'] or case['pairs'][0]['signed_max']!=2*p-2:
            raise ValueError('boundary-majority fixture mismatch')
    sample=data['special'][0]
    controls=[
        mutation(sample,lambda r:r['selected_indices'].__setitem__(1,r['selected_indices'][0]),'bad original selector indices'),
        mutation(sample,lambda r:r['unequal_signed_pairs'][0].__setitem__(1,r['unequal_signed_pairs'][0][0]),'signed pair index reused'),
        mutation(sample,lambda r:r.__setitem__('eligible',False),'wrong sufficient-condition classification'),
    ]
    result={'result':'PASS_INDEPENDENT_DIVERSE_SWAP_CHECK','input_sha256':hashlib.sha256(raw).hexdigest(),
            'random_words_checked':len(counts),'random_pairs_checked':sum(len(c['pairs']) for c in data['cases']),
            'random_actual_selectors_verified':sum(counts),
            'random_ineligible_pairs_not_decided':sum(len(c['pairs']) for c in data['cases'])-sum(counts),
            'boundary_words_checked':len(special_counts),'boundary_eligible_selectors_verified':sum(special_counts),
            'inverse_subset_sum_exhaustion':inverse_check(),
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words and finite lemma instances, not the all-prime proof'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
