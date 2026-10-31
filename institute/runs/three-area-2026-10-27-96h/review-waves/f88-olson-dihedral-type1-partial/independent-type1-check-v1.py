#!/usr/bin/env python3
"""Independent exact finite checks of the f88 type-I partial theorem.

No author code or data are imported. A witness finder uses D_(2p)'s
semidirect-product law; the separate selector validator acts on every vertex
of the p-gon by composing the selected permutations from right to left.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import random
import sys


def require(ok, text):
    if not ok:
        raise RuntimeError(text)


def valid_selector(word, chosen, p):
    if len(chosen) != 2*p:
        return 'wrong_length'
    if len(set(chosen)) != len(chosen):
        return 'duplicate_index'
    if any(i < 0 or i >= len(word) for i in chosen):
        return 'out_of_range'
    if tuple(sorted(chosen)) != tuple(chosen):
        return 'out_of_order'
    # r^x: z -> z+x; r^x s: z -> x-z.  The original group
    # product acts on the rightmost function first.
    for vertex in range(p):
        point = vertex
        for i in reversed(chosen):
            exponent, reflection = word[i]
            point = ((exponent-point) if reflection else (point+exponent)) % p
        if point != vertex:
            return 'nonidentity'
    return 'valid'


def semidirect_product(word, chosen, p):
    exponent, parity = 0, 0
    for i in chosen:
        x, is_reflection = word[i]
        exponent = (exponent + (-x if parity else x)) % p
        parity ^= is_reflection
    return exponent, parity


def prefix_data(word, p, a):
    q, refl, rot = {}, [], []
    running = 0
    for i, (x, b) in enumerate(word):
        if b:
            q[i] = running
            refl.append(i)
        else:
            require(x in (a, (-a) % p), 'unexpected rotation exponent')
            rot.append(i)
            running += 1 if x == a else -1
    require(len(word) == 4*p-1 and len(refl) == p+3, 'word layout')
    require(sum(x == a and not b for x, b in word) == 2*p-1, 'positive rotation count')
    require(sum(x == (-a) % p and not b for x, b in word) == p-3, 'negative rotation count')
    return q, tuple(refl), tuple(rot)


def zero_reflection_word(word):
    return tuple((0, 1) if b else (x, 0) for x, b in word)


def map_rotation_subsets(word0, rotations, reflections, p):
    """Enumerate all actual rotation selectors for fixed even reflections."""
    lookup = {}
    for selected_rotations in combinations(rotations, 2*p-len(reflections)):
        chosen = tuple(sorted(selected_rotations + reflections))
        x, b = semidirect_product(word0, chosen, p)
        require(b == 0, 'odd parity in even-reflection template')
        lookup.setdefault(x, chosen)
    return lookup


def signed_rotations(word, reflections, p, a):
    selected = set(reflections)
    sign = 1
    positive, negative = [], []
    for i, (x, b) in enumerate(word):
        if i in selected:
            require(b == 1, 'selected non-reflection as reflection')
            sign = -sign
        elif not b:
            s = sign*x % p
            if s == a:
                positive.append(i)
            elif s == (-a) % p:
                negative.append(i)
            else:
                raise RuntimeError('signed rotation not +/-a')
    return tuple(positive), tuple(negative)


def check_low_pair(word, pair, p, a, u, lookup):
    pos, neg = signed_rotations(word, pair, p, a)
    require(len(pos) == 2*p-1-u and len(neg) == p-3+u, 'pair signed multiplicities')
    require(min(len(pos), len(neg)) >= p-2, 'pair signed lower bound')
    signed = {i: a for i in pos}
    signed.update({i: -a for i in neg})
    omissions = {sum(signed[i] for i in group) % p
                 for group in combinations(tuple(signed), p-2)}
    require(omissions == set(range(1, p)), 'pair omission residues')
    missing = 2*(1-u)*a % p
    require(set(lookup) == set(range(p)) - {missing}, 'pair missing-target formula')
    require(sum(signed.values()) % p == missing, 'pair total signed sum')


def qualifying_quads(reflections, q, p):
    answer = []
    for quartet in combinations(reflections, 4):
        i, j, k, l = quartet
        u, v = q[j]-q[i], q[l]-q[k]
        if 1 <= u <= p+1 and 1 <= v <= p+1 and u+v <= p:
            answer.append((quartet, u, v))
    return answer


def four_selector(word, quartet, rotations, p, a, u, v):
    pos, neg = signed_rotations(word, quartet, p, a)
    require(len(pos) == 2*p-1-u-v and len(neg) == p-3+u+v, 'four signed counts')
    require(len(pos) >= p-1 and len(neg) >= p-1, 'four signed availability')
    omitted = set(pos[:p-1] + neg[:1])
    require(len(omitted) == p and ((p-2)*a) % p == (-2*a) % p,
            'four omitted sum or size')
    return tuple(sorted(tuple(i for i in rotations if i not in omitted) + quartet))


def exercise_quartet(word, quartet, lookups, constructed_four, p):
    i, j, k, l = quartet
    first_target = (word[j][0] - word[i][0]) % p
    second_target = (word[l][0] - word[k][0]) % p
    first = lookups[(i, j)].get(first_target)
    second = lookups[(k, l)].get(second_target)
    if first is not None:
        label, chosen = 'first_pair', first
    elif second is not None:
        label, chosen = 'second_pair', second
    else:
        label, chosen = 'four_reflections', constructed_four
    require(valid_selector(word, chosen, p) == 'valid', 'quartet selector failed independent vertex check')
    return label


def control_checks():
    # Six reflections then the five required positive rotations, p=3.
    positive = tuple([(0, 1)]*6 + [(1, 0)]*5)
    negative = tuple([(0, 1)]*5 + [(1, 1)] + [(1, 0)]*5)
    cases = {
        'positive': (positive, (0, 1, 2, 3, 4, 5), 'valid'),
        'wrong_length': (positive, (0, 1, 2, 3, 4), 'wrong_length'),
        'duplicate_index': (positive, (0, 0, 1, 2, 3, 4), 'duplicate_index'),
        'out_of_range': (positive, (0, 1, 2, 3, 4, 11), 'out_of_range'),
        'out_of_order': (positive, (1, 0, 2, 3, 4, 5), 'out_of_order'),
        'nonidentity': (negative, (0, 1, 2, 3, 4, 5), 'nonidentity'),
    }
    results = {}
    for name, (word, chosen, expected) in cases.items():
        got = valid_selector(word, chosen, 3)
        require(got == expected, 'wrong control result: '+name+' '+got)
        results[name] = got
    return results


def enumerate_p3():
    p = 3
    stats = Counter()
    pair_widths = Counter()
    quadruple_shapes = Counter()
    branch = Counter()
    first_counterexample = None
    for a in (1, 2):
        for reflections in combinations(range(4*p-1), p+3):
            rset = set(reflections)
            word0 = tuple((0, 1) if i in rset else (a, 0) for i in range(4*p-1))
            q, ref, rot = prefix_data(word0, p, a)
            require(ref == reflections, 'reflection order')
            pair_maps = {}
            for pair in combinations(ref, 2):
                lookup = map_rotation_subsets(word0, rot, pair, p)
                pair_maps[pair] = lookup
                u = q[pair[1]] - q[pair[0]]
                if 1 <= u <= p+1:
                    check_low_pair(word0, pair, p, a, u, lookup)
                    pair_widths[str(u)] += 1
                    stats['low_pair_layout_a_checks'] += 1
            quad_maps = {quad: map_rotation_subsets(word0, rot, quad, p)
                         for quad in combinations(ref, 4)}
            quads = qualifying_quads(ref, q, p)
            prepared = []
            for quad, u, v in quads:
                four = four_selector(word0, quad, rot, p, a, u, v)
                prepared.append((quad, four))
                quadruple_shapes[f'{u},{v}'] += 1
            stats['layouts_with_a'] += 1
            stats['layouts_qualifying_with_a'] += bool(quads)
            for ys in product(range(p), repeat=len(ref)):
                word = list(word0)
                for position, y in zip(ref, ys):
                    word[position] = (y, 1)
                stats['input_words'] += 1
                stats['qualifying_words'] += bool(quads)
                for quartet, four in prepared:
                    branch[exercise_quartet(word, quartet, pair_maps, four, p)] += 1
                    stats['qualifying_quartet_word_checks'] += 1
                # Independent exhaustive coverage of all possible even reflection
                # counts in any 6-position selector: 2, 4, or 6 (0 is impossible,
                # as the word has only 5 rotations).
                selected = None
                selected_nref = None
                for (i, j), table in pair_maps.items():
                    target = (word[j][0]-word[i][0]) % p
                    if target in table:
                        selected, selected_nref = table[target], 2
                        break
                if selected is None:
                    for (i, j, k, l), table in quad_maps.items():
                        target = (word[j][0]-word[i][0]+word[l][0]-word[k][0]) % p
                        if target in table:
                            selected, selected_nref = table[target], 4
                            break
                if selected is None:
                    six = tuple(ref)
                    if valid_selector(word, six, p) == 'valid':
                        selected, selected_nref = six, 6
                if selected is None:
                    stats['no_selector_words'] += 1
                    if first_counterexample is None:
                        first_counterexample = {'a': a, 'word': word}
                else:
                    require(valid_selector(word, selected, p) == 'valid', 'full p3 selector failed')
                    stats[f'full_word_witness_{selected_nref}_reflections'] += 1
    require(stats['input_words'] == 2*462*729, 'p3 enumeration size')
    require(stats['input_words'] == sum(stats[f'full_word_witness_{k}_reflections'] for k in (2,4,6))
            + stats['no_selector_words'], 'p3 full-word accounting')
    require(stats['qualifying_quartet_word_checks'] == sum(branch.values()), 'p3 branch accounting')
    return {'statistics': dict(stats), 'low_pair_width_checks': dict(sorted(pair_widths.items())),
            'quadruple_shapes_layout_a': dict(sorted(quadruple_shapes.items())),
            'qualifying_quartet_branches': dict(branch), 'first_no_selector_word': first_counterexample}


def sample_p5(n=5000, seed=88052026):
    p = 5
    rng = random.Random(seed)
    stats, branches, shapes, per_a = Counter(), Counter(), Counter(), Counter()
    for case in range(n):
        a = 1 + case % (p-1)
        per_a[str(a)] += 1
        word = ([(a, 0)]*(2*p-1) + [((-a)%p, 0)]*(p-3)
                + [(rng.randrange(p), 1) for _ in range(p+3)])
        rng.shuffle(word)
        q, ref, rot = prefix_data(word, p, a)
        quads = qualifying_quads(ref, q, p)
        stats['sampled_words'] += 1
        if not quads:
            stats['outside_condition'] += 1
            continue
        stats['qualifying_words'] += 1
        quartet, u, v = quads[case % len(quads)]
        shapes[f'{u},{v}'] += 1
        word0 = zero_reflection_word(word)
        i, j, k, l = quartet
        maps = {}
        for pair, width in (((i,j),u), ((k,l),v)):
            maps[pair] = map_rotation_subsets(word0, rot, pair, p)
            check_low_pair(word0, pair, p, a, width, maps[pair])
            stats['low_pair_checks'] += 1
        constructed_four = four_selector(word0, quartet, rot, p, a, u, v)
        branches[exercise_quartet(word, quartet, maps, constructed_four, p)] += 1
        # A separate deterministic copy forces both pair targets to be the
        # independently enumerated missing residues, so four reflections are
        # essential relative to the two specified pairs.
        forced = list(word)
        forced[j] = ((forced[i][0] + 2*(1-u)*a) % p, 1)
        forced[l] = ((forced[k][0] + 2*(1-v)*a) % p, 1)
        require((forced[j][0]-forced[i][0]) % p not in maps[(i,j)], 'first forced pair unexpectedly works')
        require((forced[l][0]-forced[k][0]) % p not in maps[(k,l)], 'second forced pair unexpectedly works')
        forced_branch = exercise_quartet(forced, quartet, maps, constructed_four, p)
        require(forced_branch == 'four_reflections', 'forced copy missed four branch')
        stats['forced_both_missing_copies'] += 1
    require(stats['sampled_words'] == n == stats['outside_condition'] + stats['qualifying_words'],
            'p5 sample accounting')
    require(sum(branches.values()) == stats['qualifying_words'] == stats['forced_both_missing_copies'],
            'p5 branch accounting')
    return {'seed': seed, 'sampling': '5000 shuffled raw words; a cycles 1,2,3,4; independent random reflection exponents; one qualifying quartet per qualifying word, chosen by case number modulo quartet count',
            'statistics': dict(stats), 'sampled_a': dict(sorted(per_a.items())),
            'chosen_quadruple_shapes': dict(sorted(shapes.items())), 'ordinary_branches': dict(branches)}


def main():
    require(len(sys.argv) == 2, 'usage: independent-check.py OUTPUT.json')
    controls = control_checks()
    p3 = enumerate_p3()
    p5 = sample_p5()
    result = {'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'controls': controls, 'p3_exhaustive': p3, 'p5_sample': p5}
    payload = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with open(sys.argv[1], 'x', encoding='utf-8') as out:
        out.write(payload)
    print(payload, end='')

if __name__ == '__main__':
    main()
