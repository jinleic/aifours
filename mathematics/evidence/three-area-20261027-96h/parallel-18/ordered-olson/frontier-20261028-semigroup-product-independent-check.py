#!/usr/bin/env python3
"""Independent exhaustive actual/absent-context check on an 8×18 product.

The two concrete Rees fixture definitions were disclosed in the author's
source; this implementation imports no author checker and provides no
proof of universal or infinite product theorems.
"""

import argparse
import itertools
import json


def table(items, multiplication):
    lookup = {x: i for i, x in enumerate(items)}
    return [[lookup[multiplication(a, b)] for b in items] for a in items]


def signatures(mult):
    n = len(mult)
    ids = [mult[i][i] == i for i in range(n)]
    contexts = [-1] + list(range(n))
    result = []
    for a in range(n):
        sig = bytearray()
        for x in contexts:
            xa = a if x == -1 else mult[x][a]
            for y in contexts:
                value = xa if y == -1 else mult[xa][y]
                sig.append(int(ids[value]))
        result.append(bytes(sig))
    return result, ids


def classify(values):
    mapping = {key: index for index, key in enumerate(dict.fromkeys(values))}
    return [mapping[x] for x in values], len(mapping)


def require_nonunital(mult, label):
    n = len(mult)
    if any(all(mult[e][x] == x == mult[x][e] for x in range(n)) for e in range(n)):
        raise ValueError(label + ' unexpectedly has an identity')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    A = list(itertools.product(range(2), range(2), range(2)))
    C = list(itertools.product(range(3), range(2), range(3)))
    P = ((0,0,0),(0,0,0),(0,0,1))

    def am(a, b):
        return a[0], (a[1]+b[1]) % 2, b[2]

    def cm(a, b):
        return a[0], (a[1]+P[a[2]][b[0]]+b[1]) % 2, b[2]

    ma, mc = table(A, am), table(C, cm)
    require_nonunital(ma, 'first factor')
    require_nonunital(mc, 'second factor')
    sa, ea = signatures(ma)
    sc, ec = signatures(mc)
    ida, qa = classify(sa)
    idc, qc = classify(sc)
    source = list(itertools.product(range(len(A)), range(len(C))))
    position = {s:i for i,s in enumerate(source)}
    mu = [[position[(ma[a][b], mc[c][d])] for b,d in source] for a,c in source]
    su, eu = signatures(mu)
    idu, qu = classify(su)
    factor_keys = [(ida[a], idc[c]) for a,c in source]
    factor_ids, factor_count = classify(factor_keys)
    for i,j in itertools.combinations(range(len(source)), 2):
        if (idu[i] == idu[j]) != (factor_ids[i] == factor_ids[j]):
            raise ValueError('actual product syntactic congruence does not factor')
    if qu != factor_count:
        raise ValueError('product class cardinality mismatch')
    for x in range(len(source)):
        if (idu[mu[x][x]] == idu[x]) != eu[x]:
            raise ValueError('product quotient is not idempotent pure')
    beta = [(A[a][0], A[a][2], C[c][0], C[c][2]) for a,c in source]
    if len({(beta[x], idu[x]) for x in range(len(source))}) != len(source):
        raise ValueError('explicit band/actor pair is not injective')
    for x,y in itertools.product(range(len(source)), repeat=2):
        predicted = (beta[x][0], beta[y][1], beta[x][2], beta[y][3])
        if beta[mu[x][y]] != predicted:
            raise ValueError('explicit rectangular-band map is not a homomorphism')
    idempotents = [x for x in range(len(source)) if eu[x]]
    pairs = [(e,f) for e,f in itertools.permutations(idempotents, 2) if idu[e] == idu[f]]
    r_pairs = [(e,f) for e,f in pairs if mu[e][f] == f and mu[f][e] == e]
    l_pairs = [(e,f) for e,f in pairs if mu[e][f] == e and mu[f][e] == f]
    if any(beta[e] == beta[f] for e,f in pairs):
        raise ValueError('explicit band did not separate same-actor idempotents')
    nonclosed = next(((e,f,mu[e][f]) for e,f in itertools.product(idempotents, repeat=2)
                      if not eu[mu[e][f]]), None)
    if nonclosed is None:
        raise ValueError('expected nonclosed idempotent source is orthodox')
    bad_beta = [(0, b[1], b[2], b[3]) for b in beta]
    if len({(bad_beta[x], idu[x]) for x in range(len(source))}) == len(source):
        raise ValueError('row-collapse negative control not detected')
    result = {'result': 'PASS_INDEPENDENT_FULL_PRODUCT_CONTEXTS',
              'factor_sizes': [len(A), len(C)], 'product_size': len(source),
              'contexts_per_product_element': (len(source)+1)**2,
              'factor_tau_classes': [qa,qc], 'actual_product_tau_classes': qu,
              'actual_product_tau_matches_factor_product': True,
              'product_idempotents': len(idempotents),
              'ordered_same_actor_distinct_idempotent_pairs': len(pairs),
              'ordered_same_actor_R_pairs': len(r_pairs), 'ordered_same_actor_L_pairs': len(l_pairs),
              'rectangular_band_and_actor_pair_is_injective': True,
              'nonidempotent_product_of_idempotents': [source[x] for x in nonclosed],
              'row_collapse_control_rejected': True,
              'scope': 'one explicit finite product; no proof of general equivalence'}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
