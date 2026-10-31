#!/usr/bin/env python3
"""Bounded producer for high-rotation signed-pair D_(2p) selectors."""
import argparse
from collections import Counter, defaultdict
import itertools
import json
import random

SEED = 2026102807


def product(word, indices, p):
    x, parity = 0, 0
    for i in indices:
        a,b = word[i]
        x = (x + (-a if parity else a)) % p
        parity ^= b
    return x,parity


def pairs_from_buckets(signed):
    buckets = defaultdict(list)
    for idx,value in signed:
        buckets[value].append(idx)
    pairs = []
    while True:
        live = sorted((len(v),key) for key,v in buckets.items() if v)
        if len(live)<2:
            return pairs
        _,a = live[-1]
        _,b = live[-2]
        pairs.append(sorted((buckets[a].pop(),buckets[b].pop())))


def signed_values(word, i, j, p):
    return [(k, (-x if i<k<j else x) % p) for k,(x,b) in enumerate(word) if b==0]


def check_word(word,p,label):
    rotation = [k for k,(_,b) in enumerate(word) if not b]
    refs = [k for k,(_,b) in enumerate(word) if b]
    assert len(rotation)==3*p-3 and len(refs)==p+2 and len(word)==4*p-1
    records = []
    for i,j in itertools.combinations(refs,2):
        signed = signed_values(word,i,j,p)
        maximum = max(Counter(v for _,v in signed).values())
        possible = maximum <= 2*p-2
        pair_record = {'reflections':[i,j],'max_signed_multiplicity':maximum,'eligible':possible}
        if possible:
            pairs = pairs_from_buckets(signed)[:p-1]
            assert len(pairs)==p-1
            values = dict(signed)
            choices = {0:[]}
            for a,b in pairs:
                updated = {}
                for total,indices in choices.items():
                    for k in (a,b):
                        new = (total+values[k]) % p
                        if new not in updated:
                            updated[new] = indices+[k]
                choices = updated
            assert len(choices)==p
            target = (sum(values.values())+word[i][0]-word[j][0]) % p
            omitted = choices[target]
            selected = sorted((set(rotation)-set(omitted)) | {i,j})
            assert len(selected)==2*p and product(word,selected,p)==(0,0)
            pair_record.update({'unequal_signed_pairs':pairs,'omitted_rotations':omitted,'selected_indices':selected})
        records.append(pair_record)
    return {'p':p,'label':label,'word':word,'pairs':records}


def family(p):
    word = []
    for j in range(1,p+3):
        word += [[1,0],[(-2*j)%p,1]]
    word += [[2,0] for _ in range(2*p-5)]
    return word


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    rng = random.Random(SEED)
    cases = []
    for p in (3,5,7,11):
        R = 3*p-3
        for trial in range(120):
            chosen = set(rng.sample(range(4*p-1),R))
            mode = trial%3
            word = []
            for k in range(4*p-1):
                if k not in chosen:
                    word.append([rng.randrange(p),1])
                elif mode==0:
                    word.append([rng.randrange(p),0])
                elif mode==1:
                    word.append([rng.choice((1,1,1,p-1,0)),0])
                else:
                    word.append([1,0])
            cases.append(check_word(word,p,{'trial':trial,'mode':mode}))
    structured = [check_word(family(p),p,{'family':'all-isolated'}) for p in (5,7,11,13)]
    result = {'seed':SEED,'cases':cases,'structured':structured}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,separators=(',',':'),sort_keys=True)
        out.write('\n')
    pair_count = sum(len(case['pairs']) for case in cases)
    actual = sum(pair['eligible'] for case in cases for pair in case['pairs'])
    skipped = pair_count-actual
    structured_count = sum(len(case['pairs']) for case in structured)
    assert all(pair['eligible'] for case in structured for pair in case['pairs'])
    print(json.dumps({'result':'PASS_BOUNDED_SIGNED_PAIRS','words':len(cases),'reflection_pairs':pair_count,
                      'eligible_selectors':actual,'ineligible_not_decided':skipped,
                      'structured_words':len(structured),'structured_eligible_selectors':structured_count},sort_keys=True))


if __name__ == '__main__':
    main()
