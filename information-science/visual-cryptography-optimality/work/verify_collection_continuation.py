#!/usr/bin/env python3
"""Six full-distribution impossibility checks; standard library, no solver.

The original certificate package is input-only. See collection-continuation.md
for coverage and support-pruning proofs. Every arithmetic certificate is exact.
"""
import argparse
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as F
import hashlib
from itertools import combinations_with_replacement
import json
from pathlib import Path
import sys
import time


OBLIGATIONS = [
    ('n5-3-5-6-9-10-28', 5, True),
    ('n5-3-5-9-22-26-28', 6, True),
    ('n5-3-5-10-12-22-25', 5, True),
    ('n5-3-5-10-22-25-28', 6, True),
    ('n5-7-11-13-19-21-25', 6, True),
    ('n5-7-11-13-19-21-25', 7, False),
]


def partition(record):
    n = record['n']
    qualified = [s for s in range(1 << n)
                 if any(s & a == a for a in record['minimal_qualified'])]
    forbidden = [s for s in range(1 << n) if s not in qualified]
    maximal = [s for s in forbidden if not any(s != t and s & t == s for t in forbidden)]
    assert 0 in forbidden and (1 << n)-1 in qualified
    assert all((1 << i) in forbidden for i in range(n))
    assert all(any(f | (1 << i) in qualified for f in forbidden) for i in range(n))
    return qualified, forbidden, maximal


def signature(columns, forbidden):
    # The complete multiset is the orbit of an entire projected matrix.
    return tuple(sorted(t & forbidden for t in columns))


def weights(columns, n):
    return tuple(sum(bool(t & s) for t in columns) for s in range(1 << n))


def check_lp(record):
    q, forbidden, _ = partition(record)
    k = 1 << record['n']
    cert = record['lp']
    primal = list(map(F, cert['primal']))
    u = list(map(F, cert['dual_inequality']))
    v = list(map(F, cert['dual_equality']))
    alpha = F(cert['alpha'])
    assert len(primal) == 2*k+1 and len(u) == len(q) and len(v) == len(forbidden)+1
    assert all(x >= 0 for x in primal) and all(x <= 0 for x in u)
    assert sum(primal[:k]) == sum(primal[k:2*k]) == 1
    assert primal[-1] == alpha > 0
    for s in range(k):
        gap = sum((primal[t]-primal[k+t]) for t in range(k) if not t & s)
        assert gap == 0 if s in forbidden else gap >= alpha
    assert sum(u) <= -1
    assert v[0]+v[1] == -alpha
    slack = [[], []]
    for color in range(2):
        for t in range(k):
            lhs = v[color]
            lhs += sum(value * (1 if color else -1) for s, value in zip(q, u) if not t & s)
            lhs += sum(value * (-1 if color else 1)
                       for s, value in zip(forbidden[1:], v[2:]) if not t & s)
            assert lhs <= 0, 'Invalid exact dual column inequality'
            slack[color].append(-lhs)
    allowed = [[t for t in range(k) if slack[color][t] == 0] for color in range(2)]
    tight = [s for s, value in zip(q, u) if value < 0]
    return alpha, allowed, tight


def check_basis(record, witness):
    q, forbidden, _ = partition(record)
    columns = [tuple(t for t, count in enumerate(witness[color]) for _ in range(count))
               for color in ('white', 'black')]
    assert len(columns[0]) == len(columns[1]) == witness['m']
    assert all(signature(columns[0], f) == signature(columns[1], f) for f in forbidden)
    w, b = [weights(c, record['n']) for c in columns]
    assert min(b[s]-w[s] for s in q) == witness['gap'] >= 1


def enumerate_supports(record, m, allowed, use_face):
    n = record['n']
    q, forbidden, maximal = partition(record)
    k = 1 << n
    requirements = set()
    for s in q:
        for f in forbidden:
            if f & s == f:
                requirements.add(frozenset(t for t in range(k) if t & s and not t & f))
    minimal_requirements = sorted((x for x in requirements if not any(y < x for y in requirements)),
                                  key=lambda x: (len(x), tuple(sorted(x))))
    black = []
    for columns in combinations_with_replacement(allowed[1], m):
        present = set(columns)
        if any(not present.intersection(r) for r in minimal_requirements):
            continue
        if any(all(t & f for t in columns) for f in maximal):
            continue
        black.append((columns, weights(columns, n)))
    black_keys = [{signature(c, f) for c, _ in black} for f in maximal]
    white = []
    assert 0 in allowed[0]
    for tail in combinations_with_replacement(allowed[0], m-1):
        columns = (0,)+tail
        if use_face:
            if any(all(t & f for t in columns) for f in maximal):
                continue
            if any(all(not t & (1 << i) for t in columns) for i in range(n)):
                continue
        elif not all(signature(columns, f) in keys for f, keys in zip(maximal, black_keys)):
            continue
        white.append((columns, weights(columns, n)))
    return white, black, minimal_requirements


def prune_lists(white, black, qualified, maximal, tight):
    rounds = []
    while white and black:
        wg = [defaultdict(list) for _ in maximal]
        bg = [defaultdict(list) for _ in maximal]
        for group, support in ((wg, white), (bg, black)):
            for index, (columns, _) in enumerate(support):
                for d, f in zip(group, maximal):
                    d[signature(columns, f)].append(index)

        def compatible(w, b):
            return all(b[q] > w[q] for q in qualified) and all(b[q] == w[q]+1 for q in tight)

        nw = [(c, w) for c, w in white if all(
            any(compatible(w, black[j][1]) for j in d[signature(c, f)])
            for d, f in zip(bg, maximal))]
        nb = [(c, b) for c, b in black if all(
            any(compatible(white[i][1], b) for i in d[signature(c, f)])
            for d, f in zip(wg, maximal))]
        rounds.append([len(nw), len(nb)])
        if len(nw) == len(white) and len(nb) == len(black):
            return nw, nb, rounds
        white, black = nw, nb
    return white, black, rounds


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask -= bit


def check_separator(white, black, forbidden, m, separator):
    terms = separator['terms']
    for term in terms:
        assert term['forbidden'] in forbidden
        assert isinstance(term['coefficient'], int)
        pattern = term['signature']
        assert len(pattern) == m and pattern == sorted(pattern)
        assert all(t & term['forbidden'] == t for t in pattern)
    scores = [[sum(term['coefficient'] for term in terms
                   if signature(c, term['forbidden']) == tuple(term['signature']))
               for c, _ in support] for support in (white, black)]
    assert min(scores[0]) >= separator['white_score_lower']
    assert max(scores[1]) <= separator['black_score_upper']
    assert separator['white_score_lower'] > separator['black_score_upper']
    return scores


def threshold_tree(white, black, q, forbidden, maximal, m, separator):
    # Each edge records a full forbidden projected-matrix orbit, plus ALL Q.
    wedges = [[0]*len(white) for _ in maximal]
    bedges = [[0]*len(black) for _ in maximal]
    for index, f in enumerate(maximal):
        groups = defaultdict(list)
        for j, (c, _) in enumerate(black):
            groups[signature(c, f)].append(j)
        for i, (c, w) in enumerate(white):
            for j in groups[signature(c, f)]:
                b = black[j][1]
                if all(b[s] > w[s] for s in q):
                    wedges[index][i] |= 1 << j
                    bedges[index][j] |= 1 << i
    wcut = {s: {t: sum(1 << i for i, (_, w) in enumerate(white) if w[s] < t)
                for t in range(1, m+1)} for s in q}
    bcut = {s: {t: sum(1 << j for j, (_, b) in enumerate(black) if b[s] >= t)
                for t in range(1, m+1)} for s in q}
    stats = {'nodes': 0, 'empty_leaves': 0, 'separated_leaves': 0, 'max_depth': 0}
    leaves = []

    def visit(wmask, bmask, depth):
        stats['nodes'] += 1
        stats['max_depth'] = max(depth, stats['max_depth'])
        while wmask and bmask:
            nw = sum(1 << i for i in bits(wmask) if all(row[i] & bmask for row in wedges))
            nb = sum(1 << j for j in bits(bmask) if all(row[j] & wmask for row in bedges))
            if (nw, nb) == (wmask, bmask):
                break
            wmask, bmask = nw, nb
        node = {'white': wmask.bit_count(), 'black': bmask.bit_count()}
        if not wmask or not bmask:
            stats['empty_leaves'] += 1
            node['result'] = 'empty'
            return node
        ws, bs = list(bits(wmask)), list(bits(bmask))
        choices = []
        for s in q:
            if max(white[i][1][s] for i in ws) >= min(black[j][1][s] for j in bs):
                children = [(t, wmask & wcut[s][t], bmask & bcut[s][t]) for t in range(1, m+1)]
                viable = [(t, w, b) for t, w, b in children if w and b]
                score = max((w.bit_count()+b.bit_count() for _, w, b in viable), default=0)
                choices.append((score, len(viable), s, children))
        if not choices:
            lw = [white[i] for i in ws]
            lb = [black[j] for j in bs]
            scores = check_separator(lw, lb, forbidden, m, separator)
            leaf = {'white': [list(c) for c, _ in lw], 'black': [list(c) for c, _ in lb],
                    'scores': scores, 'thresholds': {str(s): max(w[s] for _, w in lw)+1 for s in q}}
            node.update(result='integer_separator', leaf=len(leaves))
            leaves.append(leaf)
            stats['separated_leaves'] += 1
            return node
        _, _, s, children = min(choices)
        node['qualified'] = s
        node['children'] = []
        for t, w, b in children:
            if w and b:
                assert (w, b) != (wmask, bmask), 'Threshold branch did not shrink support'
                child = visit(w, b, depth+1)
            else:
                # Still explicitly retain all thresholds, including immediately empty ones.
                child = {'white': w.bit_count(), 'black': b.bit_count(), 'result': 'empty_before_pruning'}
            node['children'].append({'threshold': t, 'node': child})
        return node

    tree = visit((1 << len(white))-1, (1 << len(black))-1, 0)
    assert stats['separated_leaves'] == 1
    return stats, tree, leaves


def controls(leaf, forbidden, m, separator):
    # Equal aggregate projected column counts are NOT equal matrix distributions.
    first = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    second = {(0, 1): F(1)}
    assert sum(sum(c)*p for c, p in first.items()) == sum(sum(c)*p for c, p in second.items())
    assert first != second
    bad = deepcopy(separator)
    for term in bad['terms']:
        term['coefficient'] = 0
    white = [(tuple(c), ()) for c in leaf['white']]
    black = [(tuple(c), ()) for c in leaf['black']]
    try:
        check_separator(white, black, forbidden, m, bad)
    except AssertionError:
        pass
    else:
        raise AssertionError('Zeroed separating functional was accepted')
    return ['first-moment-only security rejected', 'zeroed separator rejected']


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--base', type=Path, default=Path('evidence/certificates-n5.json'))
    p.add_argument('--certificate', type=Path, default=Path('evidence/continuation-20261014/certificate.json'))
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    started = time.monotonic()
    data = json.loads(args.certificate.read_text())
    assert data['schema'] == 'full-projection-support-obstruction-v1' and data['gap'] == 1
    assert [(o['id'], o['m'], o['optimal_face']) for o in data['obligations']] == OBLIGATIONS
    records = {r['id']: r for r in json.loads(args.base.read_text())['records']}
    results = []
    for key, m, face in OBLIGATIONS:
        tick = time.monotonic()
        r = records[key]
        assert r['n'] == 5 and key == 'n5-'+'-'.join(map(str, r['minimal_qualified']))
        alpha, allowed, tight = check_lp(r)
        for mode in ('minimum_expansion', 'contrast_at_minimum', 'expansion_at_maximum_contrast'):
            check_basis(r, r[mode])
        q, forbidden, maximal = partition(r)
        if face:
            assert alpha == F(1, m)
        else:
            allowed, tight = [list(range(32)), list(range(32))], []
        white, black, requirements = enumerate_supports(r, m, allowed, face)
        initial = [len(white), len(black)]
        white, black, rounds = prune_lists(white, black, q, maximal, tight)
        result = {'id': key, 'm': m, 'optimal_face': face, 'qualified': q, 'forbidden': forbidden,
                  'maximal_forbidden': maximal, 'allowed_columns': allowed, 'tight_qualified': tight,
                  'black_hitting_sets': [sorted(x) for x in requirements],
                  'initial_support_sizes': initial, 'pruning_rounds': rounds}
        if white and black:
            sep = data['terminal_separator']
            assert sep['id'] == key and sep['m'] == m and not face
            stats, tree, leaves = threshold_tree(white, black, q, forbidden, maximal, m, sep)
            result.update(threshold_statistics=stats, threshold_tree=tree, terminal_leaves=leaves)
            result['negative_controls'] = controls(leaves[0], forbidden, m, sep)
        result['certified_infeasible'] = True
        result['seconds'] = time.monotonic()-tick
        results.append(result)
        print(json.dumps({k: result[k] for k in ('id', 'm', 'initial_support_sizes', 'pruning_rounds', 'seconds')}
                         | {'certified_infeasible': True}), flush=True)
    output = {'certified': True, 'command': sys.argv, 'python': sys.version,
              'arithmetic': 'integers and fractions; no solver', 'seconds': time.monotonic()-started,
              'sha256': {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in (args.base, args.certificate, Path(__file__))},
              'obligations': results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2)+'\n')


if __name__ == '__main__':
    main()
