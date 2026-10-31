#!/usr/bin/env python3
"""Independent exact check of the specified finite Rees×meet source.

No author code is imported. Checks are bounded to this explicit 36-element
structure and do not prove the infinite cryptogroup theorem.
"""

import argparse
import itertools
import json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    elems = list(itertools.product(range(3), range(2), range(3), range(2)))
    lookup = {value: i for i, value in enumerate(elems)}
    sandwich = ((0, 0, 0), (0, 0, 0), (0, 0, 1))

    def raw_product(a, b):
        i, g, lam, level = a
        j, h, mu, other_level = b
        return i, (g + sandwich[lam][j] + h) % 2, mu, min(level, other_level)

    mult = [[lookup[raw_product(a, b)] for b in elems] for a in elems]
    n = len(elems)
    for a, b, c in itertools.product(range(n), repeat=3):
        if mult[mult[a][b]][c] != mult[a][mult[b][c]]:
            raise ValueError('associativity violation')
    ids = [x for x in range(n) if mult[x][x] == x]
    idset = set(ids)
    inverses = {}
    for a in range(n):
        values = [b for b in range(n) if mult[mult[a][b]][a] == a and mult[mult[b][a]][b] == b]
        if not values:
            raise ValueError('nonregular element')
        inverses[a] = values
        if not any(mult[a][b] == mult[b][a] for b in values):
            raise ValueError('element lacks a subgroup inverse')
    for a in range(n):
        if a in idset:
            continue
        for f in ids:
            fa = mult[f][a]
            if fa in idset and any(mult[a][g] == fa for g in ids):
                raise ValueError('weak E-unitarity violation')

    def product_chain(*words):
        result = words[0]
        for value in words[1:]:
            result = mult[result][value]
        return result

    corner_triples = 0
    for e in ids:
        corner = {product_chain(e, x, e) for x in range(n)}
        ecorner = [x for x in corner if x in idset]
        for a, b in itertools.product(ecorner, repeat=2):
            if mult[a][b] not in idset:
                raise ValueError('local idempotents not closed')
        for a, b, c in itertools.product(ecorner, repeat=3):
            corner_triples += 1
            if product_chain(a, b, a, c, a) != product_chain(a, b, c, a):
                raise ValueError('local regular-band identity violation')

    left = [frozenset([a] + [mult[x][a] for x in range(n)]) for a in range(n)]
    right = [frozenset([a] + [mult[a][x] for x in range(n)]) for a in range(n)]
    keys = [(left[a], right[a]) for a in range(n)]
    unique_h = {key: i for i, key in enumerate(dict.fromkeys(keys))}
    hid = [unique_h[key] for key in keys]
    for a, b in itertools.product(range(n), repeat=2):
        if hid[a] == hid[b]:
            for x in range(n):
                if hid[mult[a][x]] != hid[mult[b][x]] or hid[mult[x][a]] != hid[mult[x][b]]:
                    raise ValueError('H not a congruence')
    if len({hid[e] for e in ids}) != len(ids):
        raise ValueError('H fails to separate idempotents')

    bn = len(unique_h)
    breps = [hid.index(i) for i in range(bn)]
    bmul = [[hid[mult[a][b]] for b in breps] for a in breps]
    if any(bmul[x][x] != x for x in range(bn)):
        raise ValueError('H quotient is not a band')
    band_corner_triples = 0
    for e in range(bn):
        corner = {bmul[bmul[e][x]][e] for x in range(bn)}
        for a, b, c in itertools.product(corner, repeat=3):
            band_corner_triples += 1
            left_value = bmul[bmul[bmul[bmul[a][b]][a]][c]][a]
            right_value = bmul[bmul[bmul[a][b]][c]][a]
            if left_value != right_value:
                raise ValueError('H quotient local band is not regular')

    signatures = []
    contexts = [None] + list(range(n))
    for a in range(n):
        bits = 0
        position = 0
        for x, y in itertools.product(contexts, repeat=2):
            t = a if x is None else mult[x][a]
            t = t if y is None else mult[t][y]
            if t in idset:
                bits |= 1 << position
            position += 1
        signatures.append(bits)
    qmap = {sig: i for i, sig in enumerate(dict.fromkeys(signatures))}
    qid = [qmap[sig] for sig in signatures]
    for a, b in itertools.product(range(n), repeat=2):
        if qid[a] == qid[b] and ((a in idset) != (b in idset)):
            raise ValueError('syntactic quotient not idempotent pure')
        if qid[a] == qid[b]:
            for x in range(n):
                if qid[mult[a][x]] != qid[mult[b][x]] or qid[mult[x][a]] != qid[mult[x][b]]:
                    raise ValueError('syntactic equivalence not congruence')
    if len({(hid[x], qid[x]) for x in range(n)}) != n:
        raise ValueError('H and q pair is not injective')

    # Verify the finite quotient is simple with primitive idempotents directly.
    qn = len(qmap)
    representatives = [qid.index(i) for i in range(qn)]
    qmul = [[qid[mult[a][b]] for b in representatives] for a in representatives]
    qe = [i for i in range(qn) if qmul[i][i] == i]
    for e, f in itertools.product(qe, repeat=2):
        if qmul[e][f] == e and qmul[f][e] == e and e != f:
            raise ValueError('quotient idempotent not primitive')
    for a in range(qn):
        ideal = {a}
        ideal.update(qmul[x][a] for x in range(qn))
        ideal.update(qmul[a][y] for y in range(qn))
        ideal.update(qmul[qmul[x][a]][y] for x, y in itertools.product(range(qn), repeat=2))
        if len(ideal) != qn:
            raise ValueError('quotient has proper principal two-sided ideal')

    # Directly validate the particular claimed nonorthodox idempotent pair.
    e = lookup[(0, 0, 0, 0)]
    f = lookup[(2, 1, 2, 0)]
    ef = mult[e][f]
    if e not in idset or f not in idset or ef in idset or elems[ef] != (0, 1, 2, 0):
        raise ValueError('claimed nonclosure pair invalid')
    same_q = [(a, b) for a, b in itertools.combinations(ids, 2) if qid[a] == qid[b]]
    r_pairs = sum(right[a] == right[b] for a, b in same_q)
    l_pairs = sum(left[a] == left[b] for a, b in same_q)
    ideal0 = {x for x in range(n) if elems[x][3] == 0}
    if not ideal0 or len(ideal0) == n or any(mult[x][y] not in ideal0 or mult[y][x] not in ideal0
                                               for x in ideal0 for y in range(n)):
        raise ValueError('claimed proper ideal invalid')

    # Negative controls derived independently from the declared properties.
    q_only_collision = next(((a, b) for a, b in itertools.combinations(range(n), 2) if qid[a] == qid[b]), None)
    if q_only_collision is None:
        raise ValueError('control q-only host unexpectedly injective')
    bad_qid = qid.copy()
    nonid = next(a for a in range(n) if a not in idset)
    bad_qid[nonid] = qid[ids[0]]
    if not any(bad_qid[a] == bad_qid[b] and ((a in idset) != (b in idset))
               for a, b in itertools.combinations(range(n), 2)):
        raise ValueError('control purity mutation not detected')
    if mult[e][e] not in idset:
        raise ValueError('control identical idempotent product should be idempotent')

    result = {'result': 'PASS_INDEPENDENT_FINITE_STRUCTURE',
              'elements': n, 'associativity_triples': n**3, 'idempotents': len(ids),
              'local_regular_identity_triples': corner_triples,
              'band_local_regular_identity_triples': band_corner_triples,
              'h_classes': len(unique_h), 'syntactic_classes': qn,
              'proper_ideal_size': len(ideal0),
              'same_q_idempotent_pairs': len(same_q), 'same_q_R_pairs': r_pairs, 'same_q_L_pairs': l_pairs,
              'nonclosure_pair': [elems[e], elems[f]], 'nonidempotent_product': elems[ef],
              'q_simple_and_primitive': True, 'h_q_pair_injective': True,
              'negative_controls': {'q_only_host_collision': [elems[x] for x in q_only_collision],
                                    'collapsed_idempotent_nonidempotent_class_detected': True,
                                    'idempotent_times_itself_is_not_a_nonclosure_witness': True},
              'scope': 'one independently checked 36-element object; not proof of universal or infinite claims'}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
