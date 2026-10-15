#!/usr/bin/env python3
"""Exact finite obstructions to two proposed reductions of Theorem G.

This does not compute a reduced B4/F4 basis. It reads the existing paired rule
transducers, independently enumerates whole homogeneous braid classes for four
short words, and rejects output-pruning and commutations-only normalization.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT.parent
CASES = [
    {'type': 'B4', 'N': 16, 'pairs': [('a','b',2),('a','c',2),('a','d',3),('b','c',4),('b','d',3),('c','d',2)],
     'pruning': ('dabda', 'bdbad', 'bdabd'),
     'commuting': ('daabbdabd', 'adaadbdaa', 'adaabdbaa')},
    {'type': 'F4', 'N': 24, 'pairs': [('a','b',2),('a','c',2),('a','d',3),('b','c',3),('b','d',4),('c','d',2)],
     'pruning': ('dbcdbc', 'bdbdcb', 'bdbcdb'),
     'commuting': ('dabdabdb', 'bdbdadbd', 'bdbadabd')},
]


def neighbors(word, pairs):
    for a, b, m in pairs:
        p = ''.join(a if k % 2 == 0 else b for k in range(m))
        q = ''.join(b if k % 2 == 0 else a for k in range(m))
        for source, dest in ((p, q), (q, p)):
            for i in range(len(word) - m + 1):
                if word[i:i+m] == source:
                    yield word[:i] + dest + word[i+m:]


def braid_class(word, pairs):
    seen, todo = {word}, [word]
    while todo:
        for nxt in neighbors(todo.pop(), pairs):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return sorted(seen)


def outputs(graph, word):
    outgoing = {}
    for source, dest, left, right in graph['edges']:
        assert len(left) == 1
        outgoing.setdefault((source, left), []).append((dest, right))
    states = {(graph['start'], '')}
    for letter in word:
        states = {(dest, old + right) for source, old in states
                  for dest, right in outgoing.get((source, letter), [])}
    return sorted({right for state, right in states if state == graph['accept']})


def check_word(left, right, smaller, case, graph):
    pairs = case['pairs']
    whole = braid_class(left, pairs)
    prefix = braid_class(left[:-1], pairs)
    suffix = braid_class(left[1:], pairs)
    assert len(left) < case['N'], 'Delta-freeness length argument unavailable'
    assert min(prefix) == left[:-1] and min(suffix) == left[1:]
    assert right in whole and min(whole) < left
    assert smaller in set(neighbors(right, pairs)) and smaller < right
    emitted = outputs(graph, left)
    assert right in emitted
    return {'left': left, 'right': right, 'one_braid_step_smaller': smaller,
            'whole_braid_class': whole, 'proper_prefix_class': prefix,
            'proper_suffix_class': suffix, 'all_transducer_outputs': emitted,
            'minimal_nonnormal_positive_word': True,
            'all_words_shorter_than_Delta': True}


results = []
for case in CASES:
    source = TARGET / 'evidence/certify' / (case['type'] + '_paired_rules.json')
    data = json.loads(source.read_text())
    assert data['order'] == [0, 2, 3, 1]
    assert data['graph']['filtered_minimal_leading'] is True
    pruning = check_word(*case['pruning'], case, data['graph'])
    assert pruning['all_transducer_outputs'] == [case['pruning'][1]]
    commuting = check_word(*case['commuting'], case, data['graph'])
    moves = list(neighbors(case['commuting'][1], [p for p in case['pairs'] if p[2] == 2]))
    assert not moves, 'The claimed singleton commutation class is wrong'
    results.append({'type': case['type'], 'N': case['N'], 'order': 'a<b<c<d, [s1,s3,s4,s2]',
                    'braid_relations': case['pairs'], 'paired_source': str(source),
                    'paired_source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                    'output_pruning_rejected': pruning,
                    'commutations_only_rejected': commuting})
receipt = {'schema': 'artin-reduced-shortcut-rejection/1', 'success': True,
           'scope': 'Four exact finite counterexamples; neither reduced rational bases nor their impossibility are proved.',
           'mathematical_bridge': 'Homogeneous braid-class exhaustion proves positive lex normality of both maximal proper factors. Their length is below N, hence Delta-free; baseline Lemma 2 identifies these with group normal words. Removing the sole rule for such a minimal nonnormal word destroys completeness (Lemma 1).',
           'cases': results}
(ROOT / 'reduced-filter-controls.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'success': True, 'cases': len(results), 'rejected_shortcuts': ['prune nonnormal outputs', 'normalize by commutations alone']}, indent=2))
