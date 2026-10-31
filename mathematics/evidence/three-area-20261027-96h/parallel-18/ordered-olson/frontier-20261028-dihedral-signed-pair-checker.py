#!/usr/bin/env python3
"""Independently replay signed-pair data and check actual ordered selectors."""
import argparse
from collections import Counter, defaultdict
import copy
import hashlib
import itertools
import json
import random


def direct_product(word,chosen,p):
    exponent, parity = 0,0
    for k in chosen:
        a,b = word[k]
        exponent = (exponent+((-1 if parity else 1)*a))%p
        parity ^= b
    return exponent,parity


def check_record(word,p,record):
    i,j = record['reflections']
    if not (0<=i<j<len(word) and word[i][1] and word[j][1]):
        raise ValueError('invalid reflection pair')
    rotations = [k for k,(_,b) in enumerate(word) if b==0]
    signed = {k: (word[k][0]*(-1 if i<k<j else 1))%p for k in rotations}
    maximum = max(Counter(signed.values()).values())
    if record['max_signed_multiplicity'] != maximum:
        raise ValueError('wrong signed multiplicity')
    eligible = maximum <= 2*p-2
    if record['eligible'] != eligible:
        raise ValueError('wrong eligibility classification')
    if not eligible:
        return False
    pairs, omitted, selected = record['unequal_signed_pairs'],record['omitted_rotations'],record['selected_indices']
    if len(pairs) != p-1 or len(omitted) != p-1:
        raise ValueError('wrong number of signed pairs')
    flattened = [x for pair in pairs for x in pair]
    if len(set(flattened)) != 2*(p-1) or any(x not in signed for x in flattened):
        raise ValueError('signed pair index reused')
    if any(len(pair)!=2 or signed[pair[0]]==signed[pair[1]] for pair in pairs):
        raise ValueError('pair is not signed-unequal')
    if len(set(omitted)) != p-1 or any(len(set(pair).intersection(omitted))!=1 for pair in pairs):
        raise ValueError('wrong pair omissions')
    if len(selected)!=2*p or selected!=sorted(set(selected)) or any(k<0 or k>=len(word) for k in selected):
        raise ValueError('bad selected indices')
    if set(selected)!=(set(rotations)-set(omitted)) | {i,j}:
        raise ValueError('wrong selected complement')
    if direct_product(word,selected,p)!=(0,0):
        raise ValueError('nonidentity actual product')
    return True


def check_case(case):
    p,word = case['p'],case['word']
    if len(word)!=4*p-1 or sum(b==0 for _,b in word)!=3*p-3 or any(a<0 or a>=p or b not in (0,1) for a,b in word):
        raise ValueError('wrong original word')
    refs = [i for i,(_,b) in enumerate(word) if b]
    expected = [list(pair) for pair in itertools.combinations(refs,2)]
    if [r['reflections'] for r in case['pairs']] != expected:
        raise ValueError('reflection-pair coverage mismatch')
    return sum(check_record(word,p,r) for r in case['pairs'])


def max_separated_pairs(bits):
    n = len(bits)
    best = [0]*(n+1)
    for i in range(n-1,-1,-1):
        best[i] = best[i+1]
        for j in range(i+1,n):
            if bits[i]==bits[j]:
                best[i] = max(best[i],1+best[j+1])
    return best[0]


def check_structured(case):
    p,word = case['p'],case['word']
    expected = [item for j in range(1,p+3) for item in ([1,0],[(-2*j)%p,1])]+[[2,0]]*(2*p-5)
    if word != expected:
        raise ValueError('structured family mismatch')
    if check_case(case) != len(case['pairs']):
        raise ValueError('structured reflection pair ineligible')
    rotations = [i for i,(_,b) in enumerate(word) if not b]
    refs = [i for i,(_,b) in enumerate(word) if b]
    fixed = rotations[:2*p-2]
    if any(direct_product(word,sorted(fixed+[i,j]),p)==(0,0) for i,j in itertools.combinations(refs,2)):
        raise ValueError('earlier fixed-I method succeeds')
    gaps = defaultdict(list)
    gap = 0
    for a,b in word:
        if b:
            gap += 1
        else:
            gaps[gap].append(a)
    if any(len(set(values))>1 for values in gaps.values()):
        raise ValueError('earlier same-gap matching succeeds')
    if any(word[i][1] and word[i+1][1] for i in range(len(word)-1)):
        raise ValueError('reflection pair unexpectedly adjacent')
    if max_separated_pairs([b for _,b in word])>=2*p-1:
        raise ValueError('earlier saturated-packet criterion succeeds')
    # First and third through (p-1)-st initial rotations; first two
    # reflections; first p suffix rotations. All indices are original.
    chosen_rotations = [0]+[2*(j-1) for j in range(3,p)]+list(range(2*(p+2),2*(p+2)+p))
    selector = sorted(chosen_rotations+[1,3])
    if len(selector)!=2*p or direct_product(word,selector,p)!=(0,0):
        raise ValueError('explicit structured selector fails')
    return True


def negative_control(case,edit,expected):
    c = copy.deepcopy(case)
    edit(c['pairs'][0])
    try:
        check_record(c['word'],c['p'],c['pairs'][0])
    except ValueError as exc:
        if str(exc)==expected:
            return expected
        raise ValueError('mutation failed for unintended reason: '+str(exc)) from exc
    raise ValueError('mutation survived')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.results,'rb') as source:
        raw=source.read()
    data=json.loads(raw)
    rng=random.Random(data['seed'])
    total=0
    for case in data['cases']:
        p=case['p']
        trial=case['label']['trial']
        mode=trial%3
        if case['label']['mode']!=mode:
            raise ValueError('mode mismatch')
        chosen=set(rng.sample(range(4*p-1),3*p-3))
        replay=[]
        for k in range(4*p-1):
            if k not in chosen:
                replay.append([rng.randrange(p),1])
            elif mode==0:
                replay.append([rng.randrange(p),0])
            elif mode==1:
                replay.append([rng.choice((1,1,1,p-1,0)),0])
            else:
                replay.append([1,0])
        if replay!=case['word']:
            raise ValueError('independent seed replay mismatch')
        total+=check_case(case)
    for case in data['structured']:
        check_structured(case)
    sample=data['structured'][0]
    controls=[
        negative_control(sample,lambda r:r['selected_indices'].__setitem__(1,r['selected_indices'][0]),'bad selected indices'),
        negative_control(sample,lambda r:r['unequal_signed_pairs'][0].__setitem__(1,r['unequal_signed_pairs'][0][0]),'signed pair index reused'),
        negative_control(sample,lambda r:r.__setitem__('eligible',False),'wrong eligibility classification'),
    ]
    result={'result':'PASS_INDEPENDENT_SIGNED_PAIR_REPLAY','input_sha256':hashlib.sha256(raw).hexdigest(),
            'seed':data['seed'],'random_words_replayed':len(data['cases']),
            'random_reflection_pairs_checked':sum(len(c['pairs']) for c in data['cases']),
            'random_actual_selectors_verified':total,
            'ineligible_reflection_pairs_not_decided':sum(len(c['pairs']) for c in data['cases'])-total,
            'structured_words_verified':len(data['structured']),
            'structured_actual_selectors_verified':sum(len(c['pairs']) for c in data['structured']),
            'structured_prior_certificate_failures_verified':True,
            'mutation_controls_rejected_for_intended_reasons':controls,
            'scope':'bounded actual words; not a proof of the all-prime statement or global coverage'}
    with open(args.output,'x',encoding='utf-8') as output:
        json.dump(result,output,sort_keys=True,indent=2)
        output.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
