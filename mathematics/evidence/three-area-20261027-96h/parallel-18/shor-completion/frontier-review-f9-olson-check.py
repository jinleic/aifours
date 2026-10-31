#!/usr/bin/env python3
"""Independent exact checks for f9; imports no author-produced code/data."""
from collections import Counter
from itertools import combinations, product
import json
import random


def dihedral_mul(a, b, p):
    x, e = a
    y, f = b
    return ((x + (-1 if e else 1) * y) % p, e ^ f)


def dihedral_exhaust():
    p = 3
    # Four chosen rotations and four reflections, plus three unchosen
    # identity rotations, constitute an original 11-occurrence word.
    word_count = pair_count = suff_count = 0
    for rot_positions in combinations(range(8), 4):
        rot_set = set(rot_positions)
        skeleton = [0 if i in rot_set else 1 for i in range(8)]
        for x in product(range(p), repeat=4):
            running = 0
            prefix = []
            pos_rot = 0
            for typ in skeleton:
                if typ == 0:
                    running += x[pos_rot]
                    pos_rot += 1
                else:
                    prefix.append(running % p)
            total = sum(x) % p
            for z in product(range(p), repeat=4):
                y = tuple((z[i] - 2 * prefix[i]) % p for i in range(4))
                hits = []
                for i, j in combinations(range(4), 2):
                    acc = (0, 0)
                    ir = jf = 0
                    for typ in skeleton:
                        if typ == 0:
                            acc = dihedral_mul(acc, (x[ir], 0), p)
                            ir += 1
                        else:
                            if jf in (i, j):
                                acc = dihedral_mul(acc, (y[jf], 1), p)
                            jf += 1
                    expected = ((total + z[i] - z[j]) % p, 0)
                    if acc != expected:
                        raise AssertionError(('incorrect original-order formula', x, y, i, j))
                    hits.append(acc == (0, 0))
                    pair_count += 1
                if total == 0 or len(set(z)) == p:
                    suff_count += 1
                    if not any(hits):
                        raise AssertionError(('sufficient condition failed', x, z))
                word_count += 1
    return {'prime': p, 'words_checked': word_count, 'reflection_pairs_checked': pair_count,
            'sufficient_condition_words': suff_count}


def support_sharpness():
    count = 0
    for p in (3, 5, 7):
        for delta in range(1, p):
            for bits in range(1, (1 << p) - 1):
                present = {i for i in range(p) if bits & (1 << i)}
                missing = next(i for i in range(p) if i not in present)
                cycle = [(missing + k * delta) % p for k in range(1, p + 1)]
                values = list(reversed([v for v in cycle if v in present]))
                sequence = values + [values[-1]] * max(0, p + 1 - len(values))
                if set(sequence) != present or any((sequence[j] - sequence[i]) % p == delta
                                                     for i in range(len(sequence))
                                                     for j in range(i + 1, len(sequence))):
                    raise AssertionError(('sharpness failure', p, delta, present))
                count += 1
    return {'proper_support_delta_pairs': count}


def vec_add(x, y, p):
    return tuple((a + b) % p for a, b in zip(x, y))


def kernel_enumeration():
    checked = []
    for p, d in ((2, 1), (2, 2), (3, 1)):
        vectors = list(product(range(p), repeat=d))
        m, D = p ** d, d * (p - 1)
        word_count = 0
        for word in product(vectors, repeat=m + D):
            count = 0
            for ids in combinations(range(m + D), m):
                total = tuple(sum(word[i][j] for i in ids) % p for j in range(d))
                count += total == (0,) * d
            if count % p != 1:
                raise AssertionError(('zero-selector count', p, d, word, count))
            word_count += 1
        sharp = [(0,) * d] * (m - 1)
        for j in range(d):
            sharp += [tuple(int(i == j) for i in range(d))] * (p - 1)
        def zeros(vs):
            return sum(all(sum(vs[i][j] for i in ids) % p == 0 for j in range(d))
                       for ids in combinations(range(len(vs)), m))
        if zeros(sharp) != 0 or zeros(sharp + [(0,) * d]) == 0:
            raise AssertionError(('sharpness word', p, d))
        checked.append({'p': p, 'd': d, 'words': word_count})
    # A larger sharpness word only; the huge whole-word domain is NOT enumerated.
    p, d, m = 3, 2, 9
    sharp = [(0, 0)] * (m - 1) + [(1, 0)] * (p - 1) + [(0, 1)] * (p - 1)
    count = sum(all(sum(sharp[i][j] for i in ids) % p == 0 for j in range(d))
                for ids in combinations(range(len(sharp)), m))
    if count != 0:
        raise AssertionError('larger sharpness check failed')
    return {'all_words': checked, 'p3d2_sharp_subsets': 220, 'p3d2_zero_selectors': count}


def reflection_collision():
    results = []
    for p in (3, 5):
        V = list(product(range(p), repeat=2))
        total = collisions = 0
        for v, w, u in product(V, repeat=3):
            if len({v, w, u}) < 3:
                continue
            vals = {tuple((a - b) % p for a, b in zip(x, y))
                    for x, y in ((v, w), (v, u), (w, u))}
            cond = all((v[j] + u[j] - 2 * w[j]) % p == 0 for j in range(2))
            if (len(vals) == 2) != cond or len(vals) not in (2, 3):
                raise AssertionError('incorrect collision iff')
            total += 1
            collisions += cond
        results.append({'p': p, 'd': 2, 'distinct_triples': total, 'collisions': collisions})
    return results


def multiply(g, h, signs, p=5):
    x, y, e = g
    u, v, f = h
    return ((x + (signs[0] if e else 1) * u) % p,
            (y + (signs[1] if e else 1) * v) % p, e ^ f)


def valid_selector(word, indices, signs):
    if len(indices) != 50 or sorted(set(indices)) != indices or any(i < 0 or i >= len(word) for i in indices):
        return False
    z = (0, 0, 0)
    for i in indices:
        z = multiply(z, word[i], signs)
    return z == (0, 0, 0)


def mixed_words():
    rnd = random.Random(2026102803)
    checked = controls = 0
    for signs in ((-1, -1), (-1, 1), (1, 1)):
        for trial in range(8):
            mode = trial % 4
            word = []
            for i in range(99):
                e = (rnd.randrange(2) if mode == 0 else 1 if mode == 1
                     else 0 if mode == 2 else i % 2)
                x, y = (0, 0) if mode == 2 else (rnd.randrange(5), rnd.randrange(5))
                word.append((x, y, e))
            blocks = []
            for j in range(33):
                ids = next((3*j+a, 3*j+b) for a, b in combinations(range(3), 2)
                           if word[3*j+a][2] == word[3*j+b][2])
                v = multiply(word[ids[0]], word[ids[1]], signs)
                if v[2] != 0:
                    raise AssertionError('bad quotient packet')
                blocks.append((ids, v[:2]))
            dp = {(0, 0, 0): ()}
            for idx, (_, (x, y)) in enumerate(blocks):
                upd = dict(dp)
                for (c, a, b), path in dp.items():
                    if c < 25:
                        upd.setdefault((c+1, (a+x)%5, (b+y)%5), path+(idx,))
                dp = upd
            path = dp.get((25, 0, 0))
            if path is None:
                raise AssertionError('packet selector absent')
            ids = [i for k in path for i in blocks[k][0]]
            if not valid_selector(word, ids, signs):
                raise AssertionError('physical original-order product not identity')
            if valid_selector(word, ids[:-1] + [ids[-2]], signs):
                raise AssertionError('duplicate-index control failed')
            if valid_selector(word, ids[:-1] + [len(word)], signs):
                raise AssertionError('out-of-range control failed')
            checked += 1
            controls += 2
    return {'original_words_checked': checked, 'invalid_index_controls_rejected': controls,
            'group_order': 50, 'word_length': 99, 'selector_length': 50,
            'actions': ['-I', 'diag(-1,1)', 'I'], 'seed': 2026102803}


if __name__ == '__main__':
    print(json.dumps({'dihedral': dihedral_exhaust(), 'support_sharpness': support_sharpness(),
                      'kernel': kernel_enumeration(), 'reflection_triples': reflection_collision(),
                      'mixed_words': mixed_words()}, indent=2, sort_keys=True))
