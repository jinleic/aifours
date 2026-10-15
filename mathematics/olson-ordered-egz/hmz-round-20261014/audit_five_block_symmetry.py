#!/usr/bin/env python3
"""Count-DP checks of the new cyclic-cut and automorphism reductions."""
import json
from pathlib import Path
import random

rng = random.Random(2026101421)


def composition(total, parts):
    bars = [-1] + sorted(rng.sample(range(total+parts-1), parts-1)) + [total+parts-1]
    return [bars[i+1]-bars[i]-1 for i in range(parts)]


def count_identity(table, word, n):
    counts = [[0]*n for _ in range(n+1)]
    counts[0][0] = 1
    for element in word:
        for k in range(n, 0, -1):
            for product, count in enumerate(counts[k-1]):
                counts[k][table[product][element]] += count
    return counts[n][0]


results = []
for name in ['Dic3', 'D7']:
    table = json.loads(Path(name+'-search-best.json').read_text())['table']
    n, q = len(table), len(table)//2
    automorphisms = []
    for h in range(q):
        phi = list(range(q)) + [(a-h) % q + q for a in range(q)]
        assert len(set(phi)) == n and phi[0] == 0 and phi[1] == 1
        assert all(phi[table[a][b]] == table[phi[a]][phi[b]]
                   for a in range(n) for b in range(n))
        automorphisms.append(phi)
    for _ in range(300):
        rotation_count = rng.randrange(n)
        a = composition(rotation_count, 6)
        b = [x+1 for x in composition(2*n-1-rotation_count-5, 5)]
        v = [rng.randrange(q) for _ in range(5)]
        word, starts = [1]*a[0], []
        for j in range(5):
            starts.append(len(word))
            word.extend([q+v[j]]*b[j])
            word.extend([1]*a[j+1])
        assert len(word) == 2*n-1
        original = count_identity(table, word, n)
        assert original > 0, 'Sampled avoiding word: preserve it and enter the counterexample protocol'
        for j, start in enumerate(starts):
            cut = word[start:]+word[:start]
            transformed = [automorphisms[v[j]][x] for x in cut]
            assert transformed[0] == q
            assert count_identity(table, transformed, n) == original
    result = dict(group=name, full_parameter_words=300,
        transformed_words_checked=1500, all_identity_subset_counts_preserved=True,
        sampled_full_words_all_have_identity_sublist=True,
        all_q_offset_maps_checked_as_automorphisms=True,
        method='independent count DP, not raw-subset acceptance', seed=2026101421)
    results.append(result)
print(json.dumps(dict(status='checks_passed', results=results), indent=2))
