#!/usr/bin/env python3
"""Independent finite original-order D_(2p) selector and turn-support audit.

Only stdlib is used. The checker multiplies semidirect-product pairs directly;
it does not import any candidate scripts or candidate outputs. The exhaustive
p=3 pass covers both nonzero a and every type-I word, not just the antecedent.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import random
import subprocess

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / 'independent-enumeration-v1.json'
SEED = 202610280103
SAMPLE_SIZE = 3000
rng = random.Random(SEED)
issues = []


def multiply(word, indices, p):
    """(x,b) represents r^x s^b; apply semidirect multiplication in order."""
    x, b = 0, 0
    for i in indices:
        y, c = word[i]
        x = (x + (-y if b else y)) % p
        b ^= c
    return x, b


def first_identity(word, allowed_indices, k, p, precomputed=None):
    choices = precomputed if precomputed is not None else combinations(allowed_indices, k)
    for chosen in choices:
        if multiply(word, chosen, p) == (0, 0):
            assert len(chosen) == k and len(set(chosen)) == k
            return chosen
    return None


def qzero_triplets(word, a, p):
    q = 0
    positions, qs = [], []
    for pos, (x, b) in enumerate(word):
        if b:
            positions.append(pos)
            qs.append(q)
        else:
            assert x in (a, (-a) % p)
            q += 1 if x == a else -1
    triples = []
    for js in combinations(range(len(positions)), 6):
        if all(qs[js[t]] == qs[js[t+1]] for t in (0, 2, 4)):
            triples.append(js)
    return positions, triples


def triple_category(word, positions, js, a, p):
    d = [(word[positions[js[t+1]]][0] - word[positions[js[t]]][0]) % p
         for t in (0, 2, 4)]
    two = (2 * a) % p
    if any(v not in (0, two) for v in d):
        return 'two_reflection_alternative'
    if 0 in d and two in d:
        return 'four_mixed'
    if d[0] == 0:
        return 'six_all_zero'
    return 'four_all_two' if p >= 5 else 'six_all_two_p3'


def zero_triplet_p3():
    p = 3
    n, f, k = 11, 6, 6
    summary = Counter()
    branches, witness_reflections = Counter(), Counter()
    examples = {}
    choices = list(combinations(range(n), k))
    for a in (1, 2):
        for positions in combinations(range(n), f):
            posset = set(positions)
            layout = [(0, 1) if i in posset else (a, 0) for i in range(n)]
            rpos, triples = qzero_triplets(layout, a, p)
            assert tuple(rpos) == positions and len(triples) <= 1
            eligible = [sel for sel in choices if sum(i in posset for i in sel) % 2 == 0]
            for ys in product(range(p), repeat=f):
                word = list(layout)
                for pos, y in zip(positions, ys):
                    word[pos] = (y, 1)
                summary['all_words'] += 1
                chosen = first_identity(word, range(n), k, p, eligible)
                if chosen is None:
                    summary['all_words_without_any_original_selector'] += 1
                    if 'all_no_selector' not in examples:
                        examples['all_no_selector'] = {'a': a, 'word': word}
                else:
                    summary['all_words_with_original_selector'] += 1
                if triples:
                    summary['hypothesis_words'] += 1
                    cat = triple_category(word, rpos, triples[0], a, p)
                    branches[cat] += 1
                    if chosen is None:
                        summary['hypothesis_without_selector'] += 1
                        if 'hypothesis_no_selector' not in examples:
                            examples['hypothesis_no_selector'] = {'a': a, 'word': word}
                    else:
                        witness_reflections[str(sum(word[i][1] for i in chosen))] += 1
                else:
                    summary['outside_triplet_hypothesis'] += 1
    assert summary['all_words'] == 2 * 462 * 729
    assert summary['hypothesis_words'] == 2 * 56 * 729
    return {'counts': dict(summary), 'first_triplet_branch_counts': dict(branches),
            'hypothesis_witness_reflection_counts': dict(witness_reflections),
            'counterexample_examples': examples}


def zero_triplet_p5_sample():
    p, n, k = 5, 19, 10
    summary, branches, witness_reflections = Counter(), Counter(), Counter()
    failures = []
    for _ in range(SAMPLE_SIZE):
        a = rng.randrange(1, p)
        word = [(a, 0)] * 9 + [((-a) % p, 0)] * 2
        word += [(rng.randrange(p), 1) for _ in range(8)]
        rng.shuffle(word)
        rpos, triples = qzero_triplets(word, a, p)
        summary['sampled_words'] += 1
        summary['qualifying_triples'] += len(triples)
        if not triples:
            summary['outside_triplet_hypothesis'] += 1
            continue
        summary['hypothesis_words'] += 1
        for js in triples:
            branches[triple_category(word, rpos, js, a, p)] += 1
        chosen = first_identity(word, range(n), k, p)
        if chosen is None:
            summary['hypothesis_without_selector'] += 1
            if len(failures) < 5:
                failures.append({'a': a, 'word': word, 'triples': triples})
        else:
            witness_reflections[str(sum(word[i][1] for i in chosen))] += 1
    return {'counts': dict(summary), 'all_qualifying_triple_branch_counts': dict(branches),
            'hypothesis_witness_reflection_counts': dict(witness_reflections),
            'counterexample_examples': failures}


def outside_matching(ys, turn, p):
    forbidden = {turn, turn + 1, turn + 2}
    edges = []
    i = 0
    while i + 1 < len(ys):
        if i not in forbidden and i + 1 not in forbidden and (ys[i+1]-ys[i]) % p:
            edges.append(i)
            i += 2
        else:
            i += 1
    return edges


def blocks_from_edges(length, edges):
    lefts = set(edges)
    assert len(lefts) == len(edges)
    assert all(0 <= e < length-1 for e in edges)
    assert all(e+1 not in lefts for e in edges)
    blocks = []
    i = 0
    while i < length:
        if i in lefts:
            blocks.append((i, i+1))
            i += 2
        else:
            blocks.append((i,))
            i += 1
    return blocks


def family_support(word, rpos, ys, p, edges):
    blocks = blocks_from_edges(len(ys), edges)
    assert len(blocks) == 2*p
    midpoint2 = 0
    for j, block in enumerate(blocks):
        part = sum(ys[i] for i in block) * (2 if len(block) == 1 else 1)
        midpoint2 += (-part if j % 2 else part)
    midpoint2 %= p
    pair_blocks = [j for j, block in enumerate(blocks) if len(block) == 2]
    support = set()
    for bits in product((0, 1), repeat=len(pair_blocks)):
        bmap = dict(zip(pair_blocks, bits))
        selected = [rpos[block[bmap[j]]] if len(block) == 2 else rpos[block[0]]
                    for j, block in enumerate(blocks)]
        assert selected == sorted(selected) and len(set(selected)) == 2*p
        x, parity = multiply(word, selected, p)
        assert parity == 0
        support.add(x)
    return blocks, midpoint2, support


def turn_audit(word, p, summary, examples):
    rpos = [i for i, (_, b) in enumerate(word) if b]
    ys = [word[i][0] for i in rpos]
    f = len(ys)
    assert f == 3*p-2
    d = [(ys[(j+1) % f] - ys[j]) % p for j in range(f)]
    zcyc = sum(x == 0 for x in d)
    turn_cyc = any(d[j] and d[(j+1) % f] and d[j] != d[(j+1) % f] for j in range(f))
    chosen = first_identity(word, rpos, 2*p, p)
    summary['reflection_words'] += 1
    summary['has_reflection_only_selector' if chosen is not None else 'no_reflection_only_selector'] += 1
    has_general = False
    for i in range(f-2):
        if not (d[i] and d[i+1] and d[i] != d[i+1]):
            continue
        outside = outside_matching(ys, i, p)
        if len(outside) < p-3:
            continue
        has_general = True
        common = outside[:p-3]
        b1, mu1, s1 = family_support(word, rpos, ys, p, common + [i])
        b2, mu2, s2 = family_support(word, rpos, ys, p, common + [i+1])
        sign1 = next(j for j, block in enumerate(b1) if i in block)
        sign2 = next(j for j, block in enumerate(b2) if i in block)
        assert sign1 == sign2
        predicted = ((-1 if sign1 % 2 else 1) * (d[i]-d[i+1])) % p
        summary['general_turn_matching_instances'] += 1
        if len(s1) < p-1 or len(s2) < p-1:
            issues.append({'kind': 'support_under_p_minus_1', 'p': p, 'ys': ys, 'i': i})
        if (mu1-mu2) % p != predicted or predicted == 0:
            issues.append({'kind': 'midpoint_flip', 'p': p, 'ys': ys, 'i': i})
        for mu, support in ((mu1, s1), (mu2, s2)):
            if {(mu-x) % p for x in support} != support:
                issues.append({'kind': 'complement_symmetry', 'p': p, 'ys': ys, 'i': i})
            if 0 not in support:
                summary['individual_matching_family_missing_zero'] += 1
                if len(support) != p-1 or mu != 0:
                    issues.append({'kind': 'missing_zero_midpoint', 'p': p, 'ys': ys, 'i': i})
        if 0 not in s1 and 0 not in s2:
            issues.append({'kind': 'both_matching_families_miss_zero', 'p': p, 'ys': ys, 'i': i})
    if has_general:
        summary['general_theorem_words'] += 1
        if chosen is None:
            issues.append({'kind': 'general_theorem_no_actual_selector', 'p': p, 'ys': ys})
    cyclic_qualifies = zcyc == 0 or (1 <= zcyc <= (p+1)//2 and turn_cyc)
    if cyclic_qualifies:
        summary['cyclic_theorem_words'] += 1
        if zcyc == 0:
            summary['cyclic_no_zero_words'] += 1
        else:
            summary['cyclic_cut_words'] += 1
            zero_edge = d.index(0)
            order = list(range(zero_edge+1, f)) + list(range(0, zero_edge+1))
            rotated = [rpos[j] for j in order]
            selected = first_identity(word, rotated, 2*p, p)
            if selected is None:
                issues.append({'kind': 'cyclic_cut_no_selector', 'p': p, 'ys': ys, 'edge': zero_edge})
            else:
                restored = tuple(sorted(selected))
                if tuple(selected) != restored:
                    summary['cyclic_cut_witnesses_cross_original_start'] += 1
                if multiply(word, restored, p) != (0, 0):
                    issues.append({'kind': 'cyclic_restore_failure', 'p': p, 'ys': ys, 'edge': zero_edge})
        if chosen is None:
            issues.append({'kind': 'cyclic_theorem_no_original_selector', 'p': p, 'ys': ys})
    else:
        summary['outside_cyclic_sufficient_conditions'] += 1
        if chosen is None and 'outside_cyclic_no_selector' not in examples:
            examples['outside_cyclic_no_selector'] = {'ys': ys, 'zcyc': zcyc, 'cyclic_turn': bool(turn_cyc)}


def turn_p3():
    summary = Counter()
    examples = {}
    # One full original-length interleaving for every ordered reflection tuple.
    # All other rotation placements/values are irrelevant to a reflection-only selector.
    rpos = (0, 2, 3, 5, 6, 8, 10)
    posset = set(rpos)
    for ys in product(range(3), repeat=7):
        word = [(0, 1) if j in posset else ((j+1) % 3, 0) for j in range(11)]
        for j, y in zip(rpos, ys):
            word[j] = (y, 1)
        turn_audit(word, 3, summary, examples)
    assert summary['reflection_words'] == 3**7
    return {'counts': dict(summary), 'examples': examples,
            'rotation_embedding': 'rpos=[0,2,3,5,6,8,10] zero-based; selected rotations=none'}


def turn_p5_sample():
    summary, examples = Counter(), {}
    for sample_index in range(SAMPLE_SIZE):
        ys = [rng.randrange(5) for _ in range(13)]
        if sample_index % 2 == 0:
            # N=19, R=6 nonzero rotations, at most one per cyclic reflection gap.
            gaps = set(rng.sample(range(13), 6))
            word = []
            for j, y in enumerate(ys):
                word.append((y, 1))
                if j in gaps:
                    word.append((rng.randrange(1, 5), 0))
            summary['singleton_gap_nonzero_rotation_sample'] += 1
        else:
            # General theorem also permits arbitrary rotations and gaps.
            word = [(y, 1) for y in ys] + [(rng.randrange(5), 0) for _ in range(6)]
            rng.shuffle(word)
            summary['unrestricted_rotation_interleaving_sample'] += 1
        assert len(word) == 19 and sum(b for _, b in word) == 13
        turn_audit(word, 5, summary, examples)
    return {'counts': dict(summary), 'examples': examples}


def main():
    results = {
        'procedure': 'Direct semidirect-product multiplication of actual distinct ordered selectors; no producer imports.',
        'seed': SEED,
        'p5_sample_size_each_candidate': SAMPLE_SIZE,
        'candidate1_p3_exhaustive_both_nonzero_a': zero_triplet_p3(),
        'candidate1_p5_seeded_sample': zero_triplet_p5_sample(),
        'candidate2_p3_exhaustive_reflection_tuples': turn_p3(),
        'candidate2_p5_seeded_sample': turn_p5_sample(),
        'scientific_or_check_issues': issues,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    results['native_clock_before_receipt'] = subprocess.check_output(
        ['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()
    with RECEIPT.open('x', encoding='utf-8') as f:
        json.dump(results, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
