#!/usr/bin/env python3
"""Independent exact finite controls; no author code or input files are read."""
import itertools
import json
import math
import sys
from fractions import Fraction


class Rejection(Exception):
    def __init__(self, reason, detail=None):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


def require(condition, reason, detail=None):
    if not condition:
        raise Rejection(reason, detail)


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def parity(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2


def product(a, b):
    return (compose(a[0], b[0]), a[1] ^ b[1], a[2] ^ b[2])


I = (0, 1, 2)
R = (1, 2, 0)
S = (0, 2, 1)
E = (I, 0, 0)
RO = (R, 0, 0)
SO = (S, 0, 0)
R2 = compose(R, R)
WORDS = {(0, 0): I, (0, 1): S, (1, 0): R, (1, 1): compose(R, S),
         (2, 0): R2, (2, 1): compose(R2, S)}
DECODE = {p: k for k, p in WORDS.items()}


class FiniteGroup:
    def __init__(self, elements, identity, multiply):
        self.elements = tuple(elements)
        self.ids = {g: i for i, g in enumerate(self.elements)}
        require(len(self.ids) == len(self.elements), 'DUPLICATE_GROUP_ELEMENT')
        require(identity in self.ids, 'IDENTITY_NOT_IN_GROUP')
        self.identity = self.ids[identity]
        self.size = len(self.elements)
        self.table = []
        for a in self.elements:
            row = []
            for b in self.elements:
                c = multiply(a, b)
                require(c in self.ids, 'MULTIPLICATION_NOT_CLOSED')
                row.append(self.ids[c])
            self.table.append(tuple(row))
        self.inverse = []
        for i in range(self.size):
            require(self.table[i][self.identity] == i and
                    self.table[self.identity][i] == i, 'IDENTITY_LAW')
            inverses = [j for j in range(self.size)
                        if self.table[i][j] == self.identity == self.table[j][i]]
            require(len(inverses) == 1, 'INVERSE_LAW')
            self.inverse.append(inverses[0])
        for a in range(self.size):
            for b in range(self.size):
                for c in range(self.size):
                    require(self.table[self.table[a][b]][c] ==
                            self.table[a][self.table[b][c]], 'ASSOCIATIVITY')

    def generated(self, generators):
        generators = set(generators)
        generators |= {self.inverse[g] for g in generators}
        seen = {self.identity}
        queue = [self.identity]
        for a in queue:
            for g in generators:
                b = self.table[a][g]
                if b not in seen:
                    seen.add(b)
                    queue.append(b)
        return frozenset(seen)

    def all_subgroups(self):
        first = frozenset([self.identity])
        known = {first}
        queue = [first]
        for subgroup in queue:
            for g in range(self.size):
                if g not in subgroup:
                    extension = self.generated(subgroup | {g})
                    if extension not in known:
                        known.add(extension)
                        queue.append(extension)
        return tuple(known)

    def cosets(self, subgroup):
        return {frozenset(self.table[g][h] for h in subgroup)
                for g in range(self.size)}


def check_relation(multiply):
    rr = multiply(RO, RO)
    require(multiply(multiply(SO, RO), SO) == rr,
            'S3_CONJUGACY_RELATION')
    require(multiply(SO, RO) != multiply(RO, SO), 'S3_NOT_NONABELIAN')


def normal_check(group, subgroup):
    for g in range(group.size):
        gi = group.inverse[g]
        for n in subgroup:
            require(group.table[group.table[g][n]][gi] in subgroup,
                    'KERNEL_NOT_NORMAL')


def hom_check(group, mapping):
    for a in group.elements:
        for b in group.elements:
            qa, qb, qab = mapping(a), mapping(b), mapping(product(a, b))
            require(qab == (qa[0] ^ qb[0], qa[1] ^ qb[1]),
                    'QUOTIENT_HOMOMORPHISM')


def left_coset_check(cosets, reps, subgroups):
    for k, (coset, rep, subgroup) in enumerate(zip(cosets, reps, subgroups)):
        require(coset == {product(rep, h) for h in subgroup},
                'ORIENTATION_NOT_LEFT', k)


def partition_check(universe, cosets):
    seen = set()
    for k, coset in enumerate(cosets):
        require(not (seen & coset), 'PARTITION_OVERLAP', k)
        seen.update(coset)
    require(seen == universe, 'PARTITION_COVERAGE', len(universe - seen))


def index_check(order, subgroups, claimed):
    for k, (h, n) in enumerate(zip(subgroups, claimed)):
        require(order % len(h) == 0 and order // len(h) == n,
                'COSET_INDEX', k)


def family_check(cosets, indices, threshold):
    require(len(cosets) == len(indices), 'FAMILY_LENGTH')
    for i in range(len(cosets)):
        require(bool(cosets[i]), 'FAMILY_EMPTY')
        for j in range(i):
            require(not (cosets[i] & cosets[j]), 'BAD_FAMILY_OVERLAP', [j, i])
            require(math.gcd(indices[i], indices[j]) <= threshold,
                    'BAD_FAMILY_GCD', [j, i])


def projection_check(images, expected):
    for k, (actual, wanted) in enumerate(zip(images, expected)):
        require(actual == wanted, 'PROJECTED_LINE_MISMATCH', k)


def triangle_check(images):
    a, b, c = images
    require(bool(a & b) and bool(a & c) and bool(b & c),
            'NONHELLY_PAIR_EMPTY')
    require(not (a & b & c), 'NONHELLY_TRIPLE_NONEMPTY')
    require(a & b == {(0, 0)} and a & c == {(0, 1)} and
            b & c == {(1, 0)}, 'NONHELLY_INTERSECTION_MISMATCH')


def packing_upper(indices, threshold):
    count = 0
    minimum = None
    minimum_tuple = None
    for seq in itertools.combinations_with_replacement(sorted(indices), 7):
        if all(math.gcd(seq[i], seq[j]) <= threshold
               for i in range(7) for j in range(i)):
            count += 1
            total = sum((Fraction(1, n) for n in seq), Fraction(0))
            if minimum is None or total < minimum:
                minimum, minimum_tuple = total, seq
            require(total > 1, 'PACKING_POSSIBLE_SEVEN',
                    {'indices': seq, 'mass': str(total)})
    require(minimum is not None, 'PACKING_NO_ADMISSIBLE_TYPES')
    return {'admissible_index_multisets': count, 'minimum_mass': str(minimum),
            'minimizing_indices': minimum_tuple}


def main(case):
    check_relation(product)
    elements = {(p, x, y) for p in itertools.permutations(range(3))
                for x in range(2) for y in range(2)}
    require(len(elements) == 24 and len(DECODE) == 6, 'GROUP_SIZE')
    group = FiniteGroup(sorted(elements), E, product)
    n_elements = {g for g in elements if parity(g[0]) == 0 and g[1] == 0}
    n_ids = frozenset(group.ids[g] for g in n_elements)
    n_group = FiniteGroup(sorted(n_elements), E, product)
    q_elements = {(e, x) for e in range(2) for x in range(2)}
    q_group = FiniteGroup(sorted(q_elements), (0, 0),
                          lambda a, b: (a[0] ^ b[0], a[1] ^ b[1]))
    quotient = lambda g: (parity(g[0]), g[1])
    hom_check(group, quotient)
    normal_check(group, n_ids)
    require(len(n_elements) == 6 and {quotient(g) for g in elements} == q_elements,
            'QUOTIENT_SIZE')
    require({g for g in elements if quotient(g) == (0, 0)} == n_elements,
            'QUOTIENT_KERNEL')

    def generated_elements(gens):
        return {group.elements[i] for i in group.generated({group.ids[g] for g in gens})}

    u0 = generated_elements([(I, 1, 0), (I, 0, 1)])
    u1 = generated_elements([(S, 0, 0), (I, 0, 1)])
    u2 = generated_elements([(S, 1, 0), (I, 0, 1)])
    require(u0 == {(I, x, y) for x in range(2) for y in range(2)},
            'U0_GENERATION')
    require(u1 == {(p, 0, y) for p in (I, S) for y in range(2)},
            'U1_GENERATION')
    require(u2 == {(I, 0, y) for y in range(2)} |
                  {(S, 1, y) for y in range(2)}, 'U2_GENERATION')
    reps = [E, (R, 0, 0), (R2, 1, 0), (S, 0, 0),
            (R, 1, 0), (R2, 0, 0)]
    subgroups = [u0, u1, u2, u0, u1, u2]
    cosets = [{product(g, h) for h in subgroup}
              for g, subgroup in zip(reps, subgroups)]
    claimed_rows = [
        {g for g in elements if DECODE[g[0]] == (0, 0)},
        {g for g in elements if DECODE[g[0]][0] == 1 and g[1] == 0},
        {g for g in elements if DECODE[g[0]][0] == 2 and
         (g[1] ^ DECODE[g[0]][1]) == 1},
        {g for g in elements if DECODE[g[0]] == (0, 1)},
        {g for g in elements if DECODE[g[0]][0] == 1 and g[1] == 1},
        {g for g in elements if DECODE[g[0]][0] == 2 and
         (g[1] ^ DECODE[g[0]][1]) == 0},
    ]
    left_coset_check(cosets, reps, subgroups)
    require(cosets == claimed_rows, 'LEFT_COSET_ROW_MISMATCH')
    partition_check(elements, cosets)
    index_check(group.size, subgroups, [6] * 6)
    family_check(cosets, [6] * 6, 7)
    intersections = [n_elements & u for u in (u0, u1, u2)]
    require(all(h == {(I, 0, y) for y in range(2)} for h in intersections),
            'KERNEL_INTERSECTION')
    require(all(len(n_elements) // len(h) == 3 for h in intersections),
            'KERNEL_INDEX')

    images = [{quotient(g) for g in c} for c in cosets]
    expected = [{(e, x) for e, x in q_elements if condition(e, x)}
                for condition in (lambda e, x: e == 0, lambda e, x: x == 0,
                                  lambda e, x: e ^ x == 1, lambda e, x: e == 1,
                                  lambda e, x: x == 1, lambda e, x: e ^ x == 0)]
    projection_check(images, expected)
    triangle_check(images[:3])
    require(all(len({quotient(h) for h in u}) == 2 for u in subgroups),
            'QUOTIENT_SUBGROUP_INDEX')

    if case == 'orientation':
        mutated = list(cosets)
        mutated[1] = {product(h, reps[1]) for h in subgroups[1]}
        left_coset_check(mutated, reps, subgroups)
    elif case == 'partition-overlap':
        mutated = list(cosets)
        mutated[5] = mutated[2]
        partition_check(elements, mutated)
    elif case == 'partition-missing':
        partition_check(elements, cosets[:-1])
    elif case == 'index':
        index_check(group.size, subgroups, [6, 7, 6, 6, 6, 6])
    elif case == 'projection-line':
        mutated = list(images)
        mutated[2] = set(images[5])
        projection_check(mutated, expected)
    elif case == 'triangle-pair':
        triangle_check([images[0], images[1], images[3]])
    elif case == 'triangle-total':
        triangle_check([images[0], images[1], images[5]])
    elif case == 'homomorphism':
        hom_check(group, lambda g: (int(g[0][0] != 0), g[1]))
    elif case == 'normal':
        normal_check(group, frozenset(group.ids[g] for g in u1))
    elif case == 'bad-family':
        singleton_cosets = [{g} for g in sorted(n_elements)]
        singleton_cosets[-1] = set(singleton_cosets[0])
        family_check(singleton_cosets, [6] * 6, 7)
    elif case == 'multiplication':
        def false_product(a, b):
            ta, ea = DECODE[a[0]]
            tb, eb = DECODE[b[0]]
            return (WORDS[((ta + tb) % 3, ea ^ eb)], a[1] ^ b[1], a[2] ^ b[2])
        check_relation(false_product)
    elif case not in ('positive', 'packing'):
        raise Rejection('UNKNOWN_CASE', case)

    n_singletons = [{g} for g in sorted(n_elements)]
    q_singletons = [{g} for g in sorted(q_elements)]
    family_check(n_singletons, [n_group.size] * n_group.size, 7)
    family_check(q_singletons, [q_group.size] * q_group.size, 7)
    all_subgroups = group.all_subgroups()
    for h in all_subgroups:
        require(group.size % len(h) == 0, 'SUBGROUP_LAGRANGE')
        require(len(group.cosets(h)) == group.size // len(h), 'COSET_PARTITION_COUNT')
    indices = {group.size // len(h) for h in all_subgroups if len(h) < group.size}
    require(indices == {2, 3, 4, 6, 8, 12, 24}, 'SUBGROUP_INDEX_SET')
    if case == 'packing':
        h8 = next(h for h in all_subgroups if group.size // len(h) == 8)
        c8 = list(group.cosets(h8))
        require(len(c8) == 8, 'INDEX8_COSET_COUNT')
        family_check(c8[:7], [8] * 7, 8)
        packing_upper(indices, 8)
    bound = packing_upper(indices, 7)
    return {
        'status': 'PASS', 'group_order': group.size, 'kernel_order': n_group.size,
        'quotient_order': q_group.size, 'subgroup_count': len(all_subgroups),
        'subgroup_indices': sorted(indices), 'coset_indices': [6] * 6,
        'kernel_intersection_order': 2, 'kernel_intersection_index': 3,
        'quotient_subgroup_indices': [2] * 6,
        'cosets_t_e_x_y': [sorted([list(DECODE[g[0]]) + [g[1], g[2]] for g in c])
                           for c in cosets],
        'quotient_images': [sorted([list(q) for q in a]) for a in images],
        'triangle_intersections': [[0, 0], [0, 1], [1, 0]],
        'B7_kernel': 6, 'B7_quotient': 4, 'B7_group': 6,
        'seven_coset_arithmetic_upper': bound,
    }


if __name__ == '__main__':
    try:
        require(len(sys.argv) == 2, 'ONE_CASE_REQUIRED')
        print(json.dumps(main(sys.argv[1]), sort_keys=True))
    except Rejection as error:
        print(json.dumps({'status': 'REJECT', 'reason': error.reason,
                          'detail': error.detail}, sort_keys=True), file=sys.stderr)
        sys.exit(2)
