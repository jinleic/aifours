#!/usr/bin/env python3
"""Parent exact controls for AME(4,6) support >=45.

Re-enumerate the 4/4 and 3/4 F2 parity lemmas, check one mixed residual
support and its unique overlap, and check the elementary shadow example.
This finite computation does not prove the global written reduction.
"""
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys


CANDIDATE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-global-ame46-support-lower45-v1.md')
CANDIDATE_SHA = '26a4115ff62f56320af2647c550072255d0ab7c6c90de49ef83025d9219a1121'


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def graphs(width, wanted_degrees):
    choices = [sum(1 << i for i in c) for c in itertools.combinations(range(width), 2)]
    for rows in itertools.product(choices, repeat=4):
        degrees = sorted(sum(bool(row & (1 << i)) for row in rows) for i in range(width))
        if degrees == wanted_degrees:
            yield rows


def parity(left, right, mask, width):
    acc = 0
    for i in range(4):
        if mask & (1 << i):
            for x in range(width):
                if left[i] & (1 << x):
                    for y in range(4):
                        if right[i] & (1 << y):
                            acc ^= 1 << (4 * x + y)
    return acc


def repeated_pairs(rows):
    by_row = defaultdict(list)
    for i, row in enumerate(rows):
        by_row[row].append(i)
    return sorted(tuple(indices) for indices in by_row.values() if len(indices) == 2)


def r44():
    qs = list(graphs(4, [2, 2, 2, 2]))
    require(len(qs) == 90, 'Q_GRAPH_COUNT')
    histogram = Counter()
    for u in qs:
        for v in qs:
            for f in range(1, 16):
                if parity(u, v, f, 4):
                    continue
                histogram[f.bit_count()] += 1
                pu, pv = repeated_pairs(u), repeated_pairs(v)
                require(len(pu) == 2 and pu == pv, 'R44_PARTITION')
                if f.bit_count() == 2:
                    chosen = tuple(i for i in range(4) if f & (1 << i))
                    require(chosen in pu, 'R44_MASK')
    require(dict(histogram) == {2: 216, 4: 108}, 'R44_HISTOGRAM')
    require(parity((3, 3, 12, 12), (3, 12, 3, 12), 15, 4) != 0, 'R44_NEGATIVE_CONTROL')
    return {'graphs': len(qs), 'ordered_pairs': len(qs) ** 2, 'nonempty_masks_per_pair': 15, 'even_mask_histogram': dict(histogram), 'different_partitions_rejected': True}


def r34():
    ts = list(graphs(3, [2, 3, 3]))
    qs = list(graphs(4, [2, 2, 2, 2]))
    require(len(ts) == 36 and len(qs) == 90, 'T_GRAPH_COUNT')
    histogram = Counter()
    for u in ts:
        for v in qs:
            for f in range(1, 16):
                if parity(u, v, f, 3):
                    continue
                histogram[f.bit_count()] += 1
                pu, pv = repeated_pairs(u), repeated_pairs(v)
                chosen = tuple(i for i in range(4) if f & (1 << i))
                require(len(pu) == 1 and len(pv) == 2 and chosen == pu[0] and chosen in pv, 'R34_PARTITION')
    require(dict(histogram) == {2: 216}, 'R34_HISTOGRAM')
    require(parity((6, 6, 3, 5), (3, 3, 12, 12), 3, 3) == 0, 'R34_POSITIVE_CONTROL')
    require(parity((6, 6, 3, 5), (3, 3, 12, 12), 15, 3) != 0, 'R34_NEGATIVE_CONTROL')
    return {'ternary_graphs': len(ts), 'quaternary_graphs': len(qs), 'ordered_pairs': len(ts) * len(qs), 'nonempty_masks_per_pair': 15, 'even_mask_histogram': dict(histogram), 'positive_and_negative_controls': True}


def projection_check(words):
    if len(words) != 16 or len(set(words)) != 16:
        return False
    for i, j in itertools.combinations(range(4), 2):
        counts = Counter((w[i], w[j]) for w in words)
        if len(counts) != 8 or set(counts.values()) != {2}:
            return False
    return True


def mixed_support():
    words = [tuple(map(int, s)) for s in '0000 0001 0110 0111 1010 1011 1120 1121 2200 2220 2302 2322 3202 3222 3301 3321'.split()]
    require(projection_check(words), 'MIXED_PROJECTIONS')
    rows = defaultdict(set)
    for a, b, c, d in words:
        rows[(a, b)].add((c, d))
    overlap = rows[(0, 0)] & rows[(2, 2)]
    require(overlap == {(0, 0)}, 'MIXED_UNIQUE_OVERLAP')
    altered = words.copy()
    altered[0] = (3, 0, 0, 0)
    require(len(set(altered)) == 16 and not projection_check(altered), 'MIXED_MUTATION')
    return {'words': len(words), 'all_six_pair_projections_eight_cells_multiplicity_two': True, 'row_00_columns': sorted(rows[(0, 0)]), 'row_22_columns': sorted(rows[(2, 2)]), 'unique_overlap': sorted(overlap), 'altered_word_rejected': True, 'scope': 'One necessary-support candidate, not a physical AME tensor.'}


def shadow_control():
    points = [v for v in itertools.product(range(2), repeat=3) if sum(v) % 2 == 0]
    require(len(points) == 4, 'SHADOW_SUPPORT')
    for i, j in itertools.combinations(range(3), 2):
        require(Counter((v[i], v[j]) for v in points) == Counter(itertools.product(range(2), repeat=2)), 'SHADOW_MARGINAL')
    reduced = points[:-1]
    require(any(len({(v[i], v[j]) for v in reduced}) < 4 for i, j in itertools.combinations(range(3), 2)), 'SHADOW_DELETE_CONTROL')
    return {'uniform_even_parity_rank': 4, 'all_pair_marginals_I_over_4': True, 'deleted_component_breaks_pair_marginal': True, 'scope': 'Classical diagonal sharpness example; universal spin-flip identity is written mathematics.'}


def main():
    require(len(sys.argv) == 2, 'EXPECTED_NEW_OUTPUT_PATH')
    start = clock()
    require(hashlib.sha256(CANDIDATE.read_bytes()).hexdigest() == CANDIDATE_SHA, 'CANDIDATE_HASH')
    result = {'kind': 'PARENT_INDEPENDENT_AME45_PARITY_AND_SHADOW_CONTROLS', 'candidate_sha256': CANDIDATE_SHA, 'started_native_clock': start}
    result['r44'] = r44()
    result['r34'] = r34()
    result['mixed_support'] = mixed_support()
    result['shadow'] = shadow_control()
    result['observed_native_clock_after_checks'] = clock()
    result['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['limits'] = 'Exact finite controls on independently generated incidence graphs and one mixed support; not an all-state proof, verification of no-OLS(6), novelty, human, independent-family or formal-kernel certification.'
    with Path(sys.argv[1]).open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
