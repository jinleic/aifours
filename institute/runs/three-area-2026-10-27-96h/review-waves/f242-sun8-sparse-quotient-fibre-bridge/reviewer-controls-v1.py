#!/usr/bin/env python3
"""Independent finite exact witnesses; these do not prove a universal theorem."""
from collections import deque
from itertools import permutations
from math import gcd
import json


def projective_controls(p):
    def canon(m):
        m = tuple(v % p for v in m)
        return min(m, tuple((-v) % p for v in m))

    def mul(a, b):
        a0, a1, a2, a3 = a
        b0, b1, b2, b3 = b
        return canon((a0*b0 + a1*b2, a0*b1 + a1*b3,
                      a2*b0 + a3*b2, a2*b1 + a3*b3))

    def inv(a):
        return canon((a[3], -a[1], -a[2], a[0]))

    def upper(t):
        return canon((1, t, 0, 1))

    def lower(t):
        return canon((1, 0, t, 1))

    def action(m, x):
        a, b, c, d = m
        if x == p:
            return p if c == 0 else a * pow(c, -1, p) % p
        den = (c*x + d) % p
        return p if den == 0 else (a*x + b) * pow(den, -1, p) % p

    elements = {canon((a, b, c, d))
                for a in range(p) for b in range(p)
                for c in range(p) for d in range(p)
                if (a*d-b*c) % p == 1}
    ident = canon((1, 0, 0, 1))
    assert len(elements) == p*(p*p-1)//2
    assert {action(m, p) for m in elements} == set(range(p+1))
    seen = {ident}
    todo = deque([ident])
    while todo:
        m = todo.popleft()
        for g in (upper(1), lower(1)):
            n = mul(m, g)
            if n not in seen:
                seen.add(n)
                todo.append(n)
    assert seen == elements
    Binf = {m for m in elements if action(m, p) == p}
    Bzero = {m for m in elements if action(m, 0) == 0}
    Uinf = {upper(t) for t in range(p)}
    Uzero = {lower(t) for t in range(p)}
    assert len(Binf) == len(Bzero) == p*(p-1)//2
    assert len(Uinf) == len(Uzero) == p
    assert all(mul(mul(g, h), inv(g)) in Uinf for g in Binf for h in Uinf)
    assert all(mul(mul(g, h), inv(g)) in Uzero for g in Bzero for h in Uzero)

    squares = {a*a % p for a in range(1, p)}
    z = min(set(range(1, p)) - squares)
    A, B = Binf, Bzero
    C = {m for m in elements if action(m, 1) == z}
    assert ident in A & B
    assert upper(z-1) in A & C
    correct_lower = lower(pow(z, -1, p)-1)
    assert correct_lower in B & C
    assert not (A & B & C)
    assert all(m[1] == 0 and m[2] == 0 for m in A & B)
    assert len(C) == len(A)

    # Intended-reason negatives: a square creates a triple intersection;
    # replacing z^{-1}-1 by z-1 destroys the specified lower witness.
    square = 4
    C_square = {m for m in elements if action(m, 1) == square}
    wrong_lower = lower(z-1)
    assert canon((2, 0, 0, pow(2, -1, p))) in A & B & C_square
    assert wrong_lower in B and wrong_lower not in C

    # A second proper subgroup type witnesses why the p-divisible branch
    # cannot simply be discarded from the two-colour argument.
    torus = {canon((a, z*b, b, a)) for a in range(p) for b in range(p)
             if (a*a-z*b*b) % p == 1}
    assert len(torus) == (p+1)//2 and ident in torus
    assert all(mul(x, y) in torus for x in torus for y in torus)
    torus_index = len(elements)//len(torus)
    assert torus_index == p*(p-1)
    assert torus_index % p == 0 and torus_index % (p+1) != 0
    assert gcd(p+1, torus_index) <= 7
    return {"p": p, "order": len(elements), "generated_order": len(seen),
            "stabilizer_order": len(A), "point_index": len(elements)//len(A),
            "nonsquare": z,
            "helly_pair_sizes": [len(A & B), len(A & C), len(B & C)],
            "helly_triple_size": len(A & B & C),
            "negative_square_triple_size": len(A & B & C_square),
            "negative_wrong_lower_image": action(wrong_lower, 1),
            "negative_all_proper_indices_multiple_of_point_index": torus_index,
            "mixed_colour_gcd": gcd(p+1, torus_index)}


def fibre_control():
    def mul(a, b):
        return tuple(a[b[i]] for i in range(4))

    def inv(a):
        out = [0]*4
        for i, v in enumerate(a):
            out[v] = i
        return tuple(out)

    def even(a):
        return sum(a[i] > a[j] for i in range(4) for j in range(i+1, 4)) % 2 == 0

    group = set(permutations(range(4)))
    N = {a for a in group if even(a)}
    U = {a for a in group if a[3] == 3}
    K = U & N
    t = (1, 2, 3, 0)
    x = (1, 0, 2, 3)
    ti = inv(t)
    fibre = {mul(n, t) for n in N}
    assert fibre == {mul(t, n) for n in N}
    assert x in U & fibre
    lhs = {mul(y, ti) for y in U & fibre}
    xt = mul(x, ti)
    conj = {mul(mul(t, k), ti) for k in K}
    rhs = {mul(xt, k) for k in conj}
    no_conjugation = {mul(xt, k) for k in K}
    reverse_conjugation = {mul(xt, mul(mul(ti, k), t)) for k in K}
    assert lhs == rhs and lhs <= N
    assert lhs != no_conjugation and lhs != reverse_conjugation
    assert len(group)//len(U) == (len(N)//len(K)) == 4
    return {"group_order": len(group), "kernel_order": len(N),
            "subgroup_order": len(U), "intersection_order": len(K),
            "kernel_index": len(N)//len(K), "fibre_intersection_size": len(lhs),
            "correct_fibre_equality": lhs == rhs,
            "negative_no_conjugation_equal": lhs == no_conjugation,
            "negative_reversed_conjugation_equal": lhs == reverse_conjugation}


def repeat_control():
    # C2 has one proper subgroup, of index 2. For s=1, distinct-only
    # quantification is vacuous but the permitted repeated pair violates J_7.
    distinct_proper_subgroup_indices = [2]
    repeated_indices = [2, 2]
    distinct_pairs = [(a, b) for i, a in enumerate(distinct_proper_subgroup_indices)
                      for b in distinct_proper_subgroup_indices[i+1:]]
    repeated_pairs = [(a, b) for i, a in enumerate(repeated_indices)
                      for b in repeated_indices[i+1:]]
    assert not distinct_pairs and gcd(*repeated_pairs[0]) == 2 <= 7
    for s in range(11):
        labels = [2]*(s+1)
        assert all(gcd(a, b) <= 7 for i, a in enumerate(labels) for b in labels[i+1:])
    return {"group": "C2", "distinct_proper_subgroups": 1,
            "repeated_pair_gcd": gcd(*repeated_pairs[0]),
            "negative_distinct_only_vacuous": not distinct_pairs,
            "repetition_witnesses_s": list(range(11))}


if __name__ == "__main__":
    result = {"scope": "finite exact controls only; not universal proof",
              "projective": [projective_controls(11), projective_controls(13)],
              "fibre": fibre_control(), "repeat": repeat_control()}
    print(json.dumps(result, sort_keys=True, indent=2))
