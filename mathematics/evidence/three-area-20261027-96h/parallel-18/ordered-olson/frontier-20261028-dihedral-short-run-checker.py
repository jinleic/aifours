#!/usr/bin/env python3
"""Independent replay and direct-product validation for short-run selectors."""

import argparse
from collections import Counter, defaultdict
import copy
import hashlib
import itertools
import json
import random


def direct(word, selected, p):
    exponent, sign, parity = 0, 1, 0
    for i in selected:
        value, kind = word[i]
        exponent = (exponent + sign*value) % p
        if kind:
            sign = -sign
            parity ^= 1
    return exponent, parity


def reflection_runs(word):
    result = []
    i = 0
    while i < len(word):
        if not word[i][1]:
            i += 1
            continue
        j = i
        while j < len(word) and word[j][1]:
            j += 1
        result.append(list(range(i,j)))
        i = j
    return result


def valid_candidates(word, p, s):
    output = []
    for run in reflection_runs(word):
        if len(run) < 2:
            continue
        differences = {(word[j][0]-word[i][0]) % p for i,j in itertools.combinations(run, 2)}
        if min(p, s+1)+len(differences)>p:
            output.append((run, differences))
    return output


def verify(case):
    p, word = case['p'], case['word']
    if len(word) != 4*p-1 or any(kind not in (0,1) or x < 0 or x >= p for x,kind in word):
        raise ValueError('invalid original word')
    rotations = [i for i, (_,kind) in enumerate(word) if not kind]
    if len(rotations) != case['R'] or case['t'] != len(rotations)-(2*p-2):
        raise ValueError('incorrect rotation count')
    counts = Counter(word[i][0] for i in rotations)
    maximum = min(len(rotations)//2, len(rotations)-max(counts.values(), default=0))
    pairs = case['all_rotation_pairs']
    if len(pairs) != maximum:
        raise ValueError('unequal matching count not maximum')
    seen = set()
    for a,b in pairs:
        if a>=b or a in seen or b in seen or a not in rotations or b not in rotations:
            raise ValueError('rotation pair reuse or order')
        if word[a][0] == word[b][0]:
            raise ValueError('rotation pair exponents equal')
        seen.update((a,b))
    t = case['t']
    s = min(t, maximum, p-1) if t >= 0 else 0
    if s != case['s']:
        raise ValueError('wrong adaptive pair count')
    candidates = valid_candidates(word, p, s)
    eligible = t >= 0 and bool(candidates)
    if eligible != case['eligible']:
        raise ValueError('incorrect sufficient-condition classification')
    if not eligible:
        if case['selected_indices'] is not None:
            raise ValueError('ineligible record has selector')
        return False
    run = case['reflection_run']
    if run not in [r for r,_ in candidates]:
        raise ValueError('not an actual qualifying reflection run')
    refs = case['selected_reflections']
    selected = case['selected_indices']
    if len(selected) != 2*p or selected != sorted(set(selected)) or any(i < 0 or i >= len(word) for i in selected):
        raise ValueError('bad selector indices')
    if [i for i in selected if word[i][1]] != refs or len(refs) != 2 or any(i not in run for i in refs):
        raise ValueError('wrong selected reflection pair')
    fixed, variable = case['fixed_omissions'], case['chosen_pair_omissions']
    covered = {x for pair in pairs[:s] for x in pair}
    if len(fixed) != t-s or len(set(fixed)) != len(fixed) or any(i not in rotations or i in covered for i in fixed):
        raise ValueError('bad fixed omissions')
    if len(variable) != s or len(set(variable)) != len(variable):
        raise ValueError('bad pair omission count')
    if any(len(set(pair).intersection(variable)) != 1 for pair in pairs[:s]):
        raise ValueError('one omission per pair failed')
    if set(rotations)-set(selected) != set(fixed) | set(variable):
        raise ValueError('selected rotation complement mismatch')
    if direct(word, selected, p) != (0,0):
        raise ValueError('actual original ordered product not identity')
    sums = {sum(word[i][0] for i in fixed) % p}
    for a,b in pairs[:s]:
        sums = {(x+word[i][0]) % p for x in sums for i in (a,b)}
    differences = {(word[j][0]-word[i][0]) % p for i,j in itertools.combinations(run,2)}
    if len(sums) < min(p,s+1) or len(sums) != case['omission_support_size']:
        raise ValueError('omission support bound mismatch')
    if len(differences) != case['difference_support_size']:
        raise ValueError('directed difference support mismatch')
    total = sum(word[i][0] for i in rotations) % p
    if not {(total-x) % p for x in sums}.intersection(differences):
        raise ValueError('actual support intersection empty')
    return True


def max_separated(bits):
    length = len(bits)
    dp = [0]*(length+1)
    for i in range(length-1,-1,-1):
        dp[i] = dp[i+1]
        for j in range(i+1,length):
            if bits[i] == bits[j]:
                dp[i] = max(dp[i], 1+dp[j+1])
    return dp[0]


def structured_prior_failures(case):
    p, word = case['p'], case['word']
    expected = [[1,0]]*(2*p-2)+[[0,1]]*2 + \
               [item for _ in range(p-1) for item in ([2,0],[0,1])] + [[0,1]]
    if word != expected:
        raise ValueError('structured word not matching family')
    rotations = [i for i,(_,kind) in enumerate(word) if not kind]
    refs = [i for i,(_,kind) in enumerate(word) if kind]
    fixed = rotations[:2*p-2]
    S = sum(word[i][0] for i in fixed) % p
    potentials = [(i,(word[i][0]+2*sum(word[j][0] for j in fixed if j<i)) % p) for i in refs]
    if S == 0 or any((b-a) % p == S for (_,a),(_,b) in itertools.combinations(potentials,2)):
        raise ValueError('prior fixed-I criterion unexpectedly succeeds')
    gap = 0
    groups = defaultdict(list)
    for x,kind in word:
        if kind:
            gap += 1
        else:
            groups[gap].append(x)
    if any(len(set(values))>1 for values in groups.values()):
        raise ValueError('structured same-gap criterion unexpectedly succeeds')
    if max(len(run) for run in reflection_runs(word)) >= p+1:
        raise ValueError('structured long-run criterion unexpectedly succeeds')
    if max_separated([kind for _,kind in word]) >= 2*p-1:
        raise ValueError('structured separated-packet criterion unexpectedly succeeds')
    return True


def intended_failure(case, edit, expected):
    altered = copy.deepcopy(case)
    edit(altered)
    try:
        verify(altered)
    except ValueError as exc:
        if str(exc) == expected:
            return expected
        raise ValueError('mutation rejected for unintended reason: '+str(exc)) from exc
    raise ValueError('mutation not detected')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    rng = random.Random(data['seed'])
    verified = 0
    for case in data['random_cases']:
        p, R = case['p'], case['label']['R']
        positions = set(rng.sample(range(4*p-1),R))
        expected = [[rng.randrange(p),0 if i in positions else 1] for i in range(4*p-1)]
        if expected != case['word']:
            raise ValueError('seed replay mismatch')
        verified += int(verify(case))
    for case in data['structured_cases']:
        if not verify(case) or not structured_prior_failures(case):
            raise ValueError('structured family failure')
    sample = next(c for c in data['structured_cases'] if c['p']==5)
    controls = [
        intended_failure(sample, lambda c: c['selected_indices'].__setitem__(1,c['selected_indices'][0]),
                         'bad selector indices'),
        intended_failure(sample, lambda c: c['all_rotation_pairs'][0].__setitem__(1,c['all_rotation_pairs'][0][0]),
                         'rotation pair reuse or order'),
        intended_failure(sample, lambda c: c.__setitem__('reflection_run',[0,1]),
                         'not an actual qualifying reflection run'),
    ]
    print(json.dumps({'result':'PASS_INDEPENDENT_SHORT_RUN_REPLAY',
                      'input_sha256':hashlib.sha256(raw).hexdigest(),
                      'random_words_replayed':len(data['random_cases']),
                      'qualifying_actual_selectors_verified':verified,
                      'structured_instances_verified':len(data['structured_cases']),
                      'structured_prior_certificate_failures_verified':True,
                      'mutation_controls_rejected_for_intended_reasons':controls,
                      'scope':'bounded actual words, not an all-prime proof or novelty clearance'},sort_keys=True))


if __name__ == '__main__':
    main()
