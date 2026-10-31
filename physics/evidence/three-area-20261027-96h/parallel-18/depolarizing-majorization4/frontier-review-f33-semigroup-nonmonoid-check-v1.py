#!/usr/bin/env python3
"""Exact finite nonunital, nontrivial-action instance for f33 review.

This checks one explicitly constructed model only, not Szendrei's theorem
or the arbitrary-cardinality canonical-presentation proof.
"""

import itertools
import json

B = tuple(itertools.product(range(2), repeat=2))
G = (0, 1)
S = tuple((row, col, g) for row, col in B for g in G)


def band(x, y):
    return x[0], y[1]


def action(g, x):
    return x[0] ^ g, x[1] ^ g


def product(a, b):
    x, g = a[:2], a[2]
    y, h = b[:2], b[2]
    result = band(x, action(g, y))
    return result[0], result[1], g ^ h


def context(x, a, y):
    value = a if x is None else product(x, a)
    return value if y is None else product(value, y)


def main():
    assert all(product(product(a, b), c) == product(a, product(b, c)) for a, b, c in itertools.product(S, repeat=3))
    identities = [u for u in S if all(product(u, a) == a and product(a, u) == a for a in S)]
    assert not identities
    idem = {a for a in S if product(a, a) == a}
    assert len(idem) == 4 and idem == {a for a in S if a[2] == 0}
    assert all(any(product(product(a, b), a) == a and product(product(b, a), b) == b for b in S) for a in S)
    assert all(product(e, f) in idem for e, f in itertools.product(idem, repeat=2))
    assert all(product(product(product(product(x, y), x), z), x) == product(product(product(x, y), z), x) for x, y, z in itertools.product(idem, repeat=3))
    for e, a in itertools.product(idem, S):
        if product(e, a) in idem or product(a, e) in idem:
            assert a in idem
    order_witnesses = 0
    for a in S:
        for e, f in itertools.product(idem, repeat=2):
            d = product(e, a)
            if d == product(a, f) and d in idem:
                order_witnesses += 1
                assert a in idem
    tau_pairs = 0
    contexts = (None,) + S
    for s, t in itertools.product(S, repeat=2):
        tau = all((context(x, s, y) in idem) == (context(x, t, y) in idem) for x, y in itertools.product(contexts, repeat=2))
        assert tau == (s[2] == t[2])
        tau_pairs += tau
    R = [(x, y) for x, y in itertools.product(idem, repeat=2) if x != y and product(x, y) == y and product(y, x) == x]
    L = [(x, y) for x, y in itertools.product(idem, repeat=2) if x != y and product(x, y) == x and product(y, x) == y]
    assert len(R) == 4 and len(L) == 4
    assert all(x[2] == y[2] and x[:2] != y[:2] for x, y in R + L)

    mixed = 0
    shifts = 0
    for u, s, t in itertools.product(G, S, S):
        left = band(action(u, s[:2]), action(u ^ s[2], t[:2]))
        right = action(u, product(s, t)[:2])
        assert left == right
        mixed += 1
    for v, u, s in itertools.product(G, G, S):
        assert action(v, action(u, s[:2])) == action(v ^ u, s[:2])
        shifts += 1
    assert len({(s[:2], s[2]) for s in S}) == len(S)
    print(json.dumps({"scope": "one exact nonunital B-semigroup-by-C2 example; not a proof of SZ87 or the universal theorem", "source_size": len(S), "identity_count": len(identities), "idempotents": len(idem), "actor_order": len(G), "band_action_nontrivial": action(1, (0, 0)) != (0, 0), "associativity_triples": len(S)**3, "tau_ordered_pairs": tau_pairs, "contexts_per_ordered_pair": len(contexts)**2, "same_q_ordered_distinct_R_idempotent_pairs": len(R), "same_q_ordered_distinct_L_idempotent_pairs": len(L), "weak_order_witness_cases": order_witnesses, "equivariant_mixed_relations_checked": mixed, "equivariant_shifts_checked": shifts, "faithful_band_group_pairs": len(S)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
