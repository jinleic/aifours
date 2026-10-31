#!/usr/bin/env python3
"""Independent exact bounded-context check for Bic×18-element Rees product."""

import argparse
import itertools
import json


def bic(a, b):
    i, j = a
    k, ell = b
    return i + max(0, k-j), ell + max(0, j-k)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    C = list(itertools.product(range(3), range(2), range(3)))
    P = ((0,0,0),(0,0,0),(0,0,1))
    index = {c:i for i,c in enumerate(C)}

    def cm(a, b):
        return a[0], (a[1]+P[a[2]][b[0]]+b[1]) % 2, b[2]

    cmul = [[index[cm(a,b)] for b in C] for a in C]
    cid = [cmul[i][i] == i for i in range(len(C))]
    ccontexts = [None]+list(range(len(C)))
    csig = []
    for a in range(len(C)):
        bits = bytearray()
        for x, y in itertools.product(ccontexts, repeat=2):
            xa = a if x is None else cmul[x][a]
            value = xa if y is None else cmul[xa][y]
            bits.append(int(cid[value]))
        csig.append(bytes(bits))
    mapping = {sig:i for i,sig in enumerate(dict.fromkeys(csig))}
    qid = [mapping[s] for s in csig]
    qreps = [qid.index(i) for i in range(len(mapping))]
    qisid = [qid[cmul[r][r]] == qid[r] for r in qreps]
    if any(qisid[qid[c]] != cid[c] for c in range(len(C))):
        raise ValueError('finite C actor is not pure')

    blabels = list(itertools.product(range(2), repeat=2))
    source = list(itertools.product(blabels, range(len(C))))
    contexts = [None]+source

    def multiply(a, b):
        return bic(a[0], b[0]), cmul[a[1]][b[1]]

    def idem(a):
        return a[0][0] == a[0][1] and cid[a[1]]

    signatures = []
    for a in source:
        data = bytearray()
        for x in contexts:
            xa = a if x is None else multiply(x, a)
            for y in contexts:
                value = xa if y is None else multiply(xa, y)
                data.append(int(idem(value)))
        signatures.append(bytes(data))
    predicted = [(a[0][0]-a[0][1], qid[a[1]]) for a in source]
    for i, j in itertools.combinations(range(len(source)), 2):
        if (signatures[i] == signatures[j]) != (predicted[i] == predicted[j]):
            raise ValueError('bounded product contexts disagree with actor factorization')
    if any((grade == 0 and qisid[actor]) != idem(a) for a,(grade,actor) in zip(source,predicted)):
        raise ValueError('bounded product actor purity failed')

    def bcoord(a):
        b, cindex = a
        c = C[cindex]
        return b[0], c[0], c[2]

    if len({(bcoord(a), predicted[i]) for i,a in enumerate(source)}) != len(source):
        raise ValueError('shift/rectangle host is not injective')
    wrong_shift = 0
    for i, a in enumerate(source):
        for j, b in enumerate(source):
            product = multiply(a,b)
            grade = predicted[i][0]
            good = (max(bcoord(a)[0], grade+bcoord(b)[0]), bcoord(a)[1], bcoord(b)[2])
            wrong = (max(bcoord(a)[0], -grade+bcoord(b)[0]), bcoord(a)[1], bcoord(b)[2])
            if good != bcoord(product):
                raise ValueError('shift/rectangle product identity failed')
            wrong_shift += int(wrong != bcoord(product))
    if not wrong_shift:
        raise ValueError('wrong action direction control not detected')

    ids = [i for i,a in enumerate(source) if idem(a)]
    same = [(i,j) for i,j in itertools.permutations(ids, 2) if predicted[i] == predicted[j]]
    rcount = lcount = 0
    for i,j in same:
        ab,ba = multiply(source[i],source[j]),multiply(source[j],source[i])
        rcount += int(ab == source[j] and ba == source[i])
        lcount += int(ab == source[i] and ba == source[j])
        if bcoord(source[i]) == bcoord(source[j]):
            raise ValueError('same-actor idempotents not separated')
    e, f = C.index((0,0,0)), C.index((2,1,2))
    if not cid[e] or not cid[f] or cid[cmul[e][f]]:
        raise ValueError('finite C idempotent nonclosure failed')
    result = {'result': 'PASS_INDEPENDENT_BOUNDED_BICYCLIC_REES',
              'bicyclic_labels': len(blabels), 'finite_C_elements': len(C),
              'product_labels': len(source), 'product_contexts_per_label': len(contexts)**2,
              'finite_C_contexts_per_element': len(ccontexts)**2,
              'finite_C_tau_classes': len(mapping), 'actual_bounded_context_actor_equivalence': True,
              'idempotents': len(ids), 'ordered_same_actor_pairs': len(same),
              'ordered_R_pairs': rcount, 'ordered_L_pairs': lcount,
              'host_multiplication_and_injection': True,
              'wrong_shift_direction_mismatches': wrong_shift,
              'source_products_never_truncated': True,
              'scope': 'all bounded contexts for these labels, not all infinite Bic contexts'}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
