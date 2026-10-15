#!/usr/bin/env python3
"""Exact finite checks, not an all-order completion decision procedure."""
from collections import defaultdict, deque
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def words_from_pairs(pairs):
    return {'a' * i + 'b' + 'a' * j for i, j in pairs}


def sardinas_patterson(words):
    if '' in words:
        return False, []
    pending = deque()
    seen = set()
    for first in words:
        for second in words:
            if first != second and second.startswith(first):
                pending.append(second[len(first):])
    while pending:
        suffix = pending.popleft()
        if suffix == '':
            return False, sorted(seen)
        if suffix in seen:
            continue
        seen.add(suffix)
        for word in words:
            if word.startswith(suffix):
                pending.append(word[len(suffix):])
            if suffix.startswith(word):
                pending.append(suffix[len(word):])
    return True, sorted(seen)


def bayonet_difference_graph(pairs):
    """Cordero 2019 Proposition 2, independent representation of the same code."""
    edges = set()
    for i, j in pairs:
        for k, ell in pairs:
            if (i, j) != (k, ell):
                edges.add((abs(i-k), abs(j-ell)))
    adjacency = defaultdict(set)
    for left, right in edges:
        adjacency[left].add(right)
    reached = set()
    pending = list(adjacency[0])
    while pending:
        node = pending.pop()
        if node == 0:
            return False, sorted(edges), sorted(reached)
        if node in reached:
            continue
        reached.add(node)
        pending.extend(adjacency[node])
    return True, sorted(edges), sorted(reached)


def factor_automaton(words):
    """Flower automaton: each codeword is a separate path from state 0 to 0."""
    edges = defaultdict(lambda: defaultdict(set))
    next_state = 1
    for word in sorted(words):
        current = 0
        for pos, char in enumerate(word):
            target = 0 if pos + 1 == len(word) else next_state
            if target:
                next_state += 1
            edges[current][char].add(target)
            current = target
    return edges, frozenset(range(next_state))


def completeness(words, state_cap=50000):
    """Every state initial/final recognizes factors of words in X*.

    Subset reachability is exact. An empty reached subset supplies a missing word;
    exhaustion without it proves universality. A cap is UNKNOWN, never rejection.
    """
    edges, initial = factor_automaton(words)
    seen = {initial}
    pending = deque([(initial, '')])
    while pending:
        states, prefix = pending.popleft()
        for char in 'ab':
            following = frozenset(t for s in states for t in edges[s][char])
            word = prefix + char
            if not following:
                return {'complete': False, 'missing_factor': word, 'subsets': len(seen)}
            if following not in seen:
                seen.add(following)
                if len(seen) > state_cap:
                    return {'complete': None, 'reason': 'subset cap', 'subsets': len(seen)}
                pending.append((following, word))
    return {'complete': True, 'subsets': len(seen)}


def factor_occurs(words, pattern):
    edges, states = factor_automaton(words)
    for char in pattern:
        states = frozenset(t for s in states for t in edges[s][char])
    return bool(states)


def check_collisions(instance):
    left = set(instance['forced_left_exponents'])
    right = set(instance['forced_right_exponents'])
    pairs = set(map(tuple, instance['pairs']))
    assert left == {i for i, j in pairs if j == 0}
    assert right == {j for i, j in pairs if i == 0}
    checked = []
    for item in instance['collision_certificates']:
        scale = item['multiplier']
        scaled = []
        for l, r in [item['first'], item['second']]:
            assert l in left and r in right
            scaled.append((scale*l, r) if item['side'] == 'left' else (l, scale*r))
        one, two = scaled
        assert one != two
        assert sum(one) == sum(two) == item['sum']
        # One nonzero component difference smaller than 20 guarantees distinctness
        # in every Z_n with n>=20. This is not a sampled modular check.
        assert any(0 < abs(x-y) < 20 for x, y in zip(one, two))
        prime = item['forced_prime']
        assert prime >= 2 and all(prime % d for d in range(2, prime))
        remaining = scale
        while remaining % prime == 0:
            remaining //= prime
        assert remaining == 1
        checked.append({'side': item['side'], 'scale': scale, 'pairs': scaled,
                        'sum': item['sum'], 'prime': prime})
    return checked


def main():
    raw_path = ROOT/'evidence/raw-instance.json'
    instance = json.loads(raw_path.read_text())
    # Independent source recipe from the three unions in the page image.
    expected = {(0,j) for j in (0,1,7,13,14)}
    expected |= {(i,j) for i in (3,8) for j in (0,2,4,6)}
    expected |= {(11,j) for j in (0,1,2)}
    assert set(map(tuple, instance['pairs'])) == expected
    assert len(instance['pairs']) == len(expected) == 16
    words = words_from_pairs(instance['pairs'])
    ud, residuals = sardinas_patterson(words)
    graph_ud, edges, reached = bayonet_difference_graph(instance['pairs'])
    assert ud and graph_ud
    assert max(map(len, words)) == 15
    kraft = sum((Fraction(1, 2**len(w)) for w in words), Fraction())
    actual = completeness(words)
    assert actual['complete'] is False
    assert not factor_occurs(words, actual['missing_factor'])
    # Independently explicit missing factor: inter-b a-runs are at most 14+11.
    assert not factor_occurs(words, 'a'*26)
    collisions = check_collisions(instance)
    controls = []
    for name, control, want_ud, want_complete in [
        ('complete_prefix', {'a','b'}, True, True),
        ('ambiguous_complete', {'a','b','ab'}, False, True),
        ('incomplete_code', {'aa','b'}, True, False),
        ('paper_nonprefix_completion', {'b','ab','aaaa','aaba','aaab','aabb'}, True, True),
        ('shor_add_a_ambiguity', words|{'a'}, False, True),
    ]:
        got_ud, _ = sardinas_patterson(control)
        got_complete = completeness(control)
        assert got_ud == want_ud
        assert got_complete['complete'] == want_complete
        controls.append({'name':name, 'ud':got_ud, 'completeness':got_complete})
    corrupted = deepcopy(instance)
    corrupted['collision_certificates'][-1]['second'] = [0,13]
    try:
        check_collisions(corrupted)
    except AssertionError:
        controls.append({'name':'false_doubled_collision', 'accepted':False})
    else:
        raise AssertionError('false doubled collision was accepted')
    # The graph checker also rejects a genuine non-UD bayonet mutation.
    bad_pairs = instance['pairs'] + [[0,3]]
    bad_words = words_from_pairs(bad_pairs)
    assert not sardinas_patterson(bad_words)[0]
    assert not bayonet_difference_graph(bad_pairs)[0]
    controls.append({'name':'shor_add_ba3_ambiguity', 'ud':False})
    report = {
        'schema':'shor-finite-evidence/1', 'date':'2026-10-14 PT',
        'scope':'Partial necessary obstruction audit; not finite completion or noncompletion.',
        'source_sha256':sha256(raw_path.read_bytes()).hexdigest(),
        'word_count':len(words), 'maximum_length':max(map(len,words)),
        'original_uniquely_decipherable':ud, 'independent_difference_graph_ud':graph_ud,
        'sardinas_patterson_reachable_residuals':residuals,
        'difference_graph_edges':edges, 'difference_graph_nonempty_reachable':reached,
        'dyadic_kraft':str(kraft), 'original_completeness':actual,
        'explicit_missing_factor':'a'*26,
        'collision_certificates':collisions, 'mutation_and_positive_controls':controls,
        'full_resolution':False,
    }
    path=ROOT/'evidence/verification.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('word_count','maximum_length','original_uniquely_decipherable','independent_difference_graph_ud','dyadic_kraft','original_completeness','full_resolution')},indent=2))


if __name__ == '__main__':
    main()
