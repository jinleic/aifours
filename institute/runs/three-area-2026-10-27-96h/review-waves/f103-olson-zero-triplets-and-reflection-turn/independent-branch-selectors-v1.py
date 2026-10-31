#!/usr/bin/env python3
"""Check prescribed zero-pair endpoints by exhaustive actual rotation subsets.

Uses only this reviewer's independent checker for direct D_(2p) multiplication
and zero-triplet identification; imports no author code or results.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import random
import runpy
import subprocess

HERE = Path(__file__).resolve().parent
base = runpy.run_path(str(HERE / 'independent-enumeration-v1.py'))
triplets_for = base['qzero_triplets']
category_for = base['triple_category']
multiply = base['multiply']
SEED = 202610280103


def check_triplet(word, rpos, js, a, p, counts, failures):
    cat = category_for(word, rpos, js, a, p)
    counts['triple_' + cat] += 1
    pairpos = [(rpos[js[t]], rpos[js[t+1]]) for t in (0,2,4)]
    delta = [(word[j][0]-word[i][0]) % p for i,j in pairpos]
    two = 2*a % p
    if cat == 'two_reflection_alternative':
        sets = [(i,) for i in range(3) if delta[i] not in (0, two)]
    elif cat == 'four_mixed':
        sets = [(i,j) for i in range(3) for j in range(3)
                if delta[i] == 0 and delta[j] == two]
    elif cat == 'four_all_two':
        sets = list(combinations(range(3), 2))
    else:
        sets = [(0,1,2)]
    rotpos = [i for i, (_, b) in enumerate(word) if not b]
    for pair_ids in sets:
        reflections = [j for t in pair_ids for j in pairpos[t]]
        need = 2*p - len(reflections)
        assert 0 <= need <= len(rotpos)
        counts['endpoint_requirements'] += 1
        counts['requirement_' + cat] += 1
        found = None
        for rotations in combinations(rotpos, need):
            chosen = tuple(sorted(reflections + list(rotations)))
            if multiply(word, chosen, p) == (0,0):
                assert len(chosen) == 2*p and len(set(chosen)) == 2*p
                found = chosen
                break
        if found is None:
            counts['failed_endpoint_requirements'] += 1
            if len(failures) < 10:
                failures.append({'p': p, 'a': a, 'word': word, 'triple': js,
                                 'category': cat, 'required_pairs': pair_ids})
        else:
            counts['verified_endpoint_requirements'] += 1


def exhaustive_p3():
    counts, failures = Counter(), []
    for a in (1,2):
        for refls in combinations(range(11),6):
            posset = set(refls)
            layout = [(0,1) if j in posset else (a,0) for j in range(11)]
            rpos, triples = triplets_for(layout,a,3)
            if not triples:
                continue
            assert len(triples) == 1
            for ys in product(range(3), repeat=6):
                word = list(layout)
                for pos,y in zip(refls,ys):
                    word[pos] = (y,1)
                counts['hypothesis_words'] += 1
                check_triplet(word,rpos,triples[0],a,3,counts,failures)
    assert counts['hypothesis_words'] == 81648
    return {'counts': dict(counts), 'failures': failures}


def sample_p5():
    counts, failures = Counter(), []
    rng = random.Random(SEED)
    for _ in range(3000):
        a = rng.randrange(1,5)
        word = [(a,0)]*9 + [((-a)%5,0)]*2
        word += [(rng.randrange(5),1) for _ in range(8)]
        rng.shuffle(word)
        rpos, triples = triplets_for(word,a,5)
        counts['sampled_words'] += 1
        if triples:
            counts['hypothesis_words'] += 1
        for js in triples:
            check_triplet(word,rpos,js,a,5,counts,failures)
    assert counts['hypothesis_words'] == 1502
    return {'counts': dict(counts), 'failures': failures}


def main():
    result = {
        'procedure': 'For each qualifying ordered triplet, enumerate actual rotation subsets with required pair endpoints and directly multiply in original order; all eligible pair choices are checked.',
        'base_independent_checker_sha256': hashlib.sha256((HERE / 'independent-enumeration-v1.py').read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'seed': SEED,
        'p3_exhaustive': exhaustive_p3(),
        'p5_seeded_sample': sample_p5(),
    }
    result['native_clock_before_receipt'] = subprocess.check_output(
        ['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()
    with (HERE / 'independent-branch-selectors-v1.json').open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
