#!/usr/bin/env python3
"""F156 reviewer-authored exact controls; standard library; no author-code imports.

Creates only reviewer-control-receipt-v2.json beside this script, with exclusive
creation.  The table for the nine-element object is generated directly from the
Rees multiplication definition.  All arithmetic is exact integer arithmetic.
"""
from datetime import datetime, timezone
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import platform
import sys

HERE = Path(__file__).resolve().parent
START = datetime.now(timezone.utc).isoformat()

class ControlFailure(Exception):
    pass

class AssociativityFailure(ControlFailure):
    pass

class ConeClosureFailure(ControlFailure):
    pass

class GroupIdentityFailure(ControlFailure):
    pass


def need(condition, reason):
    if not condition:
        raise ControlFailure(reason)


def table(elements, multiply):
    positions = {x: k for k, x in enumerate(elements)}
    need(len(positions) == len(elements), 'duplicate element labels')
    return [[positions[multiply(x, y)] for y in elements] for x in elements]


def idempotents(t):
    return [x for x in range(len(t)) if t[x][x] == x]


def associative(t):
    n = len(t)
    for a, b, c in product(range(n), repeat=3):
        left, right = t[t[a][b]][c], t[a][t[b][c]]
        if left != right:
            raise AssociativityFailure((a, b, c, left, right))
    return n ** 3


def inverses(t, a, subset=None):
    if subset is None:
        subset = range(len(t))
    return [b for b in subset if t[t[a][b]][a] == a and t[t[b][a]][b] == b]


def leq_idempotents(t, e, f):
    return t[e][f] == e and t[f][e] == e


def band_cones(t):
    es = idempotents(t)
    eset = set(es)
    result = {}
    for z in es:
        cone = [e for e in es if leq_idempotents(t, z, e)]
        for e, f in product(cone, repeat=2):
            ef = t[e][f]
            if ef not in eset:
                raise ConeClosureFailure(('nonidempotent_product', z, e, f, ef))
            if ef not in cone:
                raise ConeClosureFailure(('product_outside_cone', z, e, f, ef))
        result[z] = cone
    return result


def group_class(t, members, e):
    members = set(members)
    for a in members:
        if t[e][a] != a or t[a][e] != a:
            raise GroupIdentityFailure((e, a, t[e][a], t[a][e]))
    need(all(t[a][b] in members for a, b in product(members, repeat=2)),
         'group class not closed')
    need(all(any(t[a][b] == e and t[b][a] == e for b in members)
             for a in members), 'group class lacks an inverse')


def weak_e_violations(t):
    # Mitsch order a <= b iff a=x*b=b*y and x*a=a for x,y in S^1.
    # On regular semigroups this is the natural partial order.
    n = len(t)
    es = set(idempotents(t))
    def mul(x, y):
        if x == n:
            return y
        if y == n:
            return x
        return t[x][y]
    witnesses = []
    for e in sorted(es):
        for a in range(n):
            if a in es:
                continue
            xs = [x for x in range(n + 1) if mul(x, a) == e and mul(x, e) == e]
            ys = [y for y in range(n + 1) if mul(a, y) == e]
            if xs and ys:
                witnesses.append([e, a, xs[0], ys[0]])
    return witnesses


def rees(modulus, sandwich, adjoin_zero):
    elems = list(product(range(2), range(modulus), range(2)))
    if adjoin_zero:
        elems = [None] + elems
    def multiply(x, y):
        if x is None or y is None:
            return None
        i, g, lam = x
        j, h, mu = y
        return i, (g + sandwich(lam, j) + h) % modulus, mu
    return elems, table(elems, multiply)


def regular_and_local_inverse(t):
    need(all(inverses(t, a) for a in range(len(t))), 'nonregular element')
    corners = []
    for e in idempotents(t):
        local = sorted({t[t[e][a]][e] for a in range(len(t))})
        need(all(t[e][a] == a and t[a][e] == a for a in local), 'corner identity')
        need(all(t[a][b] in local for a, b in product(local, repeat=2)), 'corner closure')
        inv = {a: inverses(t, a, local) for a in local}
        need(all(len(v) == 1 for v in inv.values()), 'local inverse not unique')
        ies = [a for a in local if t[a][a] == a]
        need(all(t[a][b] == t[b][a] for a, b in product(ies, repeat=2)),
             'local idempotents do not commute')
        corners.append({'identity': e, 'elements': local, 'idempotents': ies,
                        'unique_inverses': {str(a): v[0] for a, v in inv.items()}})
    return corners


def run():
    # Requested nine-element Rees semigroup with a new absorbing zero.
    labels, s = rees(2, lambda lam, i: lam * i, True)
    triples = associative(s)
    es = idempotents(s)
    need(len(labels) == 9 and len(es) == 5, 'nine-element/idempotent count')
    corners = regular_and_local_inverse(s)
    need(all(s[0][a] == 0 and s[a][0] == 0 for a in range(9)), 'absorbing zero')
    need(all(leq_idempotents(s, 0, e) for e in es), 'zero not below all idempotents')
    e, f = labels.index((0, 0, 0)), labels.index((1, 1, 1))
    ef = s[e][f]
    need(e in es and f in es and ef == labels.index((0, 1, 1)), 'e/f/product mismatch')
    need(ef not in es and s[ef][ef] == labels.index((0, 0, 1)), 'ef unexpectedly idempotent')
    try:
        band_cones(s)
    except ConeClosureFailure as exc:
        cone_negative = list(exc.args[0])
        need(cone_negative[0] == 'nonidempotent_product' and cone_negative[1] == 0,
             'wrong intended cone failure')
    else:
        raise ControlFailure('nine-element cone negative was not rejected')
    weak_failures = weak_e_violations(s)
    need(any(w[0] == 0 and w[1] == ef for w in weak_failures), 'WEU zero witness missing')

    # Positive countercontrol: all-zero sandwich entries produce an orthodox
    # rectangular group with a new zero. Same size, same five idempotents.
    positive_labels, positive = rees(2, lambda lam, i: 0, True)
    need(positive_labels == labels, 'positive label mismatch')
    positive_triples = associative(positive)
    positive_cones = band_cones(positive)
    need(positive_cones[0] == idempotents(positive), 'positive zero cone mismatch')

    # A targeted table mutation must be rejected for associativity itself.
    mutated = [row[:] for row in s]
    mutated[0][e] = e
    try:
        associative(mutated)
    except AssociativityFailure as exc:
        assoc_negative = list(exc.args[0])
    else:
        raise ControlFailure('associativity mutation was not rejected')

    # Non-normal 15-element left regular band: nonempty words on abc with
    # no repeated letter; multiplication retains each letter's first occurrence.
    # The action swaps a,b and fixes c.
    band = [''.join(w) for k in range(1, 4) for w in permutations('abc', k)]
    def reduce_word(w):
        return ''.join(dict.fromkeys(w))
    bt = table(band, lambda a, b: reduce_word(a + b))
    band_triples = associative(bt)
    need(len(idempotents(bt)) == 15, 'B not a band')
    swap = {a: a.translate(str.maketrans('ab', 'ba')) for a in band}
    need(all(reduce_word(swap[a] + swap[b]) == swap[reduce_word(a + b)]
             for a, b in product(band, repeat=2)), 'swap not automorphism')
    normal_failure = next((list(x) for x in product(range(len(band)), repeat=3)
                           if bt[bt[bt[x[0]][x[1]]][x[2]]][x[0]] !=
                              bt[bt[bt[x[0]][x[2]]][x[1]]][x[0]]), None)
    need(normal_failure is not None, 'test band unexpectedly normal')

    # P(B,D4) -> P(B,D2), reduce actor group coordinates modulo two.
    # C4 acts through parity on the swap. The quotient is nontrivial and
    # idempotent-separating, so this also exercises group fibers/lifting/order.
    def pastijn(modulus):
        actor = list(product(range(2), range(modulus), range(2)))
        elems = list(product(band, actor))
        def mul(x, y):
            a, (i, g, lam) = x
            b, (j, h, mu) = y
            twist = (g + lam * j) % modulus
            return reduce_word(a + (swap[b] if twist % 2 else b)), (
                i, (g + lam * j + h) % modulus, mu)
        return elems, table(elems, mul)
    hs, ht = pastijn(4)
    us, ut = pastijn(2)
    hidx = {a: i for i, a in enumerate(hs)}
    uidx = {a: i for i, a in enumerate(us)}
    htriples, utriples = associative(ht), associative(ut)
    q = [uidx[(a, (i, g % 2, lam))] for a, (i, g, lam) in hs]
    need(len(set(q)) == len(us), 'quotient not onto')
    need(all(q[ht[a][b]] == ut[q[a]][q[b]] for a, b in product(range(len(hs)), repeat=2)),
         'quotient not a homomorphism')
    he, ue = idempotents(ht), idempotents(ut)
    lifts = {u: [h for h in he if q[h] == u] for u in ue}
    need(len(he) == len(ue) == 60 and all(len(v) == 1 for v in lifts.values()),
         'quotient lacks unique idempotent lifts')
    lift = {u: v[0] for u, v in lifts.items()}
    for x, (b, (i, g, lam)) in enumerate(hs):
        # Explicit inverse formula with j=nu=0: p_lam,0=p_0,i=0.
        y = hidx[(swap[b] if g % 2 else b, (0, (-g) % 4, 0))]
        need(ht[ht[x][y]][x] == x and ht[ht[y][x]][y] == y, 'explicit inverse formula')
    for a, b in product(he, repeat=2):
        need(leq_idempotents(ht, a, b) == leq_idempotents(ut, q[a], q[b]),
             'idempotent-order reflection failed')
    group_fibers = []
    for u in ue:
        members = [h for h in range(len(hs)) if q[h] == u]
        group_class(ht, members, lift[u])
        group_fibers.append({'image': u, 'identity': lift[u], 'members': members})
    ucones = band_cones(ut)
    for z, cone in ucones.items():
        actors = {hs[lift[e]][1] for e in cone}
        need(actors == {hs[lift[z]][1]}, 'actor cell forcing failed')
        bmap = {e: band.index(hs[lift[e]][0]) for e in cone}
        need(len(set(bmap.values())) == len(cone), 'band embedding not injective')
        for e, f in product(cone, repeat=2):
            need(lift[ut[e][f]] == ht[lift[e]][lift[f]], 'lifts not multiplicative')
            need(bmap[ut[e][f]] == bt[bmap[e]][bmap[f]], 'B-map not homomorphic')
    need(not weak_e_violations(ht) and not weak_e_violations(ut), 'positive WEU control failed')

    # Intended-reason boundary control: actor projection does not separate
    # idempotents; their actor images coincide but order need not reflect.
    d = (0, 0, 0)
    a, b = hidx[('a', d)], hidx[('b', d)]
    need(a in he and b in he and a != b and not leq_idempotents(ht, a, b),
         'nonseparating actor projection boundary not exercised')

    # Dropping regularity invalidates the classical lemma: {0,a}, a^2=0,
    # has one idempotent, and its universal congruence separates idempotents
    # but its idempotent class is not a group (0 does not act as identity).
    nilpotent = [[0, 0], [0, 0]]
    need(associative(nilpotent) == 8 and idempotents(nilpotent) == [0], 'nilpotent fixture')
    need(not inverses(nilpotent, 1), 'nilpotent fixture is regular')
    try:
        group_class(nilpotent, [0, 1], 0)
    except GroupIdentityFailure as exc:
        regularity_negative = list(exc.args[0])
    else:
        raise ControlFailure('nonregular group-class negative was not rejected')

    return {
        'nine_element': {
            'labels': ['ZERO' if x is None else list(x) for x in labels],
            'multiplication_table_indices': s,
            'associativity_triples': triples,
            'idempotents': es,
            'inverse_sets': {str(a): inverses(s, a) for a in range(9)},
            'local_inverse_corners': corners,
            'e_f_ef_ef_squared': [e, f, ef, s[ef][ef]],
            'zero_upper_cone': es,
            'expected_cone_closure_rejection': cone_negative,
            'weak_E_violations_with_Mitsch_witnesses': weak_failures,
        },
        'positive_orthodox_all_zero_sandwich': {
            'associativity_triples': positive_triples,
            'multiplication_table_indices': positive,
            'upper_cones': positive_cones,
        },
        'negative_associativity_mutation': {
            'change': [0, e, s[0][e], mutated[0][e]],
            'multiplication_table_indices': mutated,
            'expected_failure_triple_left_right': assoc_negative,
        },
        'pastijn_nontrivial_action_and_idempotent_separating_quotient': {
            'band_labels': band, 'band_table': bt,
            'band_associativity_triples': band_triples,
            'non_normal_band_witness_xyz': normal_failure,
            'H_order': len(hs), 'U_order': len(us),
            'H_associativity_triples': htriples,
            'U_associativity_triples': utriples,
            'H_idempotents': len(he), 'U_idempotents': len(ue),
            'idempotent_pairs_order_reflected': len(he) ** 2,
            'group_fibers_above_idempotents': group_fibers,
            'cone_cardinalities': [len(c) for c in ucones.values()],
            'all_cone_B_embeddings_checked': True,
            'H_and_U_weakly_E_unitary_by_Mitsch_exhaustion': True,
            'nonseparating_actor_projection_order_reflection_counterexample': {
                'H_elements': [a, b], 'band_labels': ['a', 'b'], 'common_actor': list(d),
                'actor_images_equal': True, 'upstairs_order': False,
            },
        },
        'negative_omitting_regularity': {
            'table': nilpotent, 'idempotents': [0], 'congruence': 'universal',
            'idempotent_separating': True,
            'expected_group_identity_failure_e_a_ea_ae': regularity_negative,
        },
    }


if __name__ == '__main__':
    results = run()
    receipt = {
        'kind': 'INDEPENDENT_REVIEWER_EXACT_CONTROL',
        'status': 'PASS_ALL_REQUIRED_AND_INTENDED_REASON_CONTROLS',
        'started_UTC': START,
        'finished_UTC': datetime.now(timezone.utc).isoformat(),
        'python': sys.version, 'platform': platform.platform(),
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'author_code_imported_or_executed': False,
        'arithmetic': 'exact Python integers and finite multiplication-table equality',
        'results': results,
    }
    target = HERE / 'reviewer-control-receipt-v2.json'
    raw = (json.dumps(receipt, ensure_ascii=False, indent=2) + '\n').encode()
    with target.open('xb') as out:
        out.write(raw)
    print('PASS: requested nine-element table, 729 triples, five idempotents, all regular/local inverse checks')
    print('PASS: nonidempotent ef; zero upper cone rejected for nonidempotent product')
    print('PASS: positive orthodox variant and intended associativity/regularity/projection boundary negatives')
    print('PASS: 240->120 Pastijn quotient, nontrivial action, 60 unique idempotent lifts, group fibers, 3600 order pairs')
    print('PASS: all quotient upper cones embed in B; both hosts satisfy WEU by exact natural-order exhaustion')
    print('started_UTC=' + START)
    print('finished_UTC=' + receipt['finished_UTC'])
    print('script_sha256=' + receipt['script_sha256'])
    print('receipt_path=' + str(target))
    print('receipt_sha256=' + sha256(raw).hexdigest())
    print('receipt_bytes=' + str(len(raw)) + ' receipt_LF=' + str(raw.count(b'\n')))
