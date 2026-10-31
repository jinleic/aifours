#!/usr/bin/env python3
"""Prospective exact f655 assay. CHILD NOT RUN. Run only after parent audit/GO.

Standard library only. No filesystem, network, subprocess, or deletion operations.
The deadline is cooperative, not a hard OS scheduling guarantee. Run with -B.
"""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import gcd
import json
import time


class Incomplete(Exception):
    pass


class Violation(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Violation(reason)


def expect(reason, fn):
    try:
        fn()
    except Violation as exc:
        if str(exc) == reason:
            return
        raise Violation("MUTATION_WRONG_REASON:" + reason + ":" + str(exc))
    raise Violation("MUTATION_NOT_REJECTED:" + reason)


class Budget:
    def __init__(self):
        self.deadline = time.monotonic() + 52.0
        self.steps = 0

    def tick(self):
        self.steps += 1
        if self.steps % 128 == 0:
            self.check()

    def check(self):
        if time.monotonic() >= self.deadline:
            raise Incomplete("COOPERATIVE_DEADLINE")


def members(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def mask_of(items):
    result = 0
    for item in items:
        result |= 1 << item
    return result


class Field:
    # Encode a+b*t as a+p*b, with t^2+u*t+1=0.
    def __init__(self, p, u):
        self.p, self.q, self.u = p, p * p, u
        q = self.q
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        self.neg = [0] * q
        for x in range(q):
            a, b = x % p, x // p
            self.neg[x] = (-a) % p + p * ((-b) % p)
            for y in range(q):
                c, d = y % p, y // p
                self.add[x][y] = (a + c) % p + p * ((b + d) % p)
                self.mul[x][y] = (a*c - b*d) % p + p * ((a*d + b*c - u*b*d) % p)
        self.inv = [None] * q
        for x in range(1, q):
            for y in range(1, q):
                if self.mul[x][y] == 1:
                    self.inv[x] = y
                    break

    def sub(self, x, y):
        return self.add[x][self.neg[y]]

    def validate(self, work):
        q, A, M = self.q, self.add, self.mul
        for x in range(1, q):
            require(self.inv[x] is not None, "NONFIELD_ZERO_DIVISOR")
            require(M[x][self.inv[x]] == 1, "FIELD_INVERSE")
        for x, y, z in product(range(q), repeat=3):
            work.tick()
            require(A[A[x][y]][z] == A[x][A[y][z]], "FIELD_ADD_ASSOC")
            require(M[M[x][y]][z] == M[x][M[y][z]], "FIELD_MUL_ASSOC")
            require(M[x][A[y][z]] == A[M[x][y]][M[x][z]], "FIELD_DISTRIBUTIVITY")
        for x in range(q):
            require(A[x][0] == x and A[x][self.neg[x]] == 0, "FIELD_ADD_IDENTITY")
            require(M[x][1] == x and M[x][0] == 0, "FIELD_MUL_IDENTITY")


class Group:
    def __init__(self, field, work):
        self.f, self.work = field, work
        q, A, M = field.q, field.add, field.mul
        raw = set()
        for a, b, c, d in product(range(q), repeat=4):
            work.tick()
            if field.sub(M[a][d], M[b][c]) == 1:
                raw.add(self.norm((a, b, c, d)))
        self.elts = sorted(raw)
        self.number = {x: i for i, x in enumerate(self.elts)}
        self.n = len(self.elts)
        self.all = (1 << self.n) - 1
        self.one = self.number[self.norm((1, 0, 0, 1))]
        self.inv = []
        for a, b, c, d in self.elts:
            self.inv.append(self.number[self.norm((d, field.neg[b], field.neg[c], a))])
        self.table = []
        for a, b, c, d in self.elts:
            row = []
            for e, f, g, h in self.elts:
                work.tick()
                matrix = (A[M[a][e]][M[b][g]], A[M[a][f]][M[b][h]],
                          A[M[c][e]][M[d][g]], A[M[c][f]][M[d][h]])
                row.append(self.number[self.norm(matrix)])
            self.table.append(row)
        for x in range(self.n):
            require(self.table[x][self.one] == x and self.table[self.one][x] == x,
                    "GROUP_IDENTITY")
            require(self.table[x][self.inv[x]] == self.one and
                    self.table[self.inv[x]][x] == self.one, "GROUP_INVERSE")

    def norm(self, matrix):
        negated = tuple(self.f.neg[x] for x in matrix)
        return min(matrix, negated)

    def check_center(self, normalize):
        ident = (1, 0, 0, 1)
        minus = tuple(self.f.neg[x] for x in ident)
        require(normalize(ident) == normalize(minus), "PROJECTIVE_CENTER")

    def gen(self, generators, max_size=None):
        generators = tuple(dict.fromkeys(generators))
        seen = 1 << self.one
        queue = [self.one]
        pos = 0
        while pos < len(queue):
            x = queue[pos]
            pos += 1
            for g in generators:
                self.work.tick()
                y = self.table[x][g]
                bit = 1 << y
                if not seen & bit:
                    seen |= bit
                    queue.append(y)
                    if max_size is not None and len(queue) > max_size:
                        return None
                    require(len(queue) <= self.n, "GENERATION_BOUND")
        return seen

    def subgroup(self, H):
        require(bool(H & (1 << self.one)), "SUBGROUP_IDENTITY")
        elements = list(members(H))
        for x in elements:
            require(bool(H & (1 << self.inv[x])), "SUBGROUP_INVERSE")
            for y in elements:
                self.work.tick()
                require(bool(H & (1 << self.table[x][y])), "SUBGROUP_CLOSURE")

    def conjugate(self, H, x):
        t, xi = self.table, self.inv[x]
        return mask_of(t[t[x][h]][xi] for h in members(H))

    def left(self, x, H):
        return mask_of(self.table[x][h] for h in members(H))

    def right(self, H, x):
        return mask_of(self.table[h][x] for h in members(H))

    def cosets(self, H):
        todo, result = self.all, []
        while todo:
            self.work.tick()
            x = (todo & -todo).bit_length() - 1
            C = self.left(x, H)
            require(C.bit_count() == H.bit_count() and C & todo == C,
                    "COSET_PARTITION")
            result.append((x, C))
            todo ^= C
        require(len(result) * H.bit_count() == self.n, "COSET_INDEX")
        return result

    def conjugates(self, H):
        result = set()
        for x in range(self.n):
            self.work.tick()
            result.add(self.conjugate(H, x))
        return result

    def order_at_most(self, g, limit):
        x = self.one
        for n in range(1, limit + 1):
            x = self.table[x][g]
            if x == self.one:
                return n
        return None


def elementary_generators(G):
    gens = []
    for x in range(1, G.f.q):
        gens.append(G.number[G.norm((1, x, 0, 1))])
        gens.append(G.number[G.norm((1, 0, x, 1))])
    return gens


def generation_and_perfectness(G):
    gens = elementary_generators(G)
    require(G.gen(gens) == G.all, "UNIPOTENT_GENERATION")
    comm = []
    t = G.table
    for x, y in product(gens, repeat=2):
        G.work.tick()
        comm.append(t[t[t[x][y]][G.inv[x]]][G.inv[y]])
    require(G.gen(comm) == G.all, "COMMUTATOR_GENERATION")
    return {"generators": len(gens), "commutators": len(set(comm))}


def point_stabilizers(G):
    F, q = G.f, G.f.q
    stabilizers = []
    for point in range(q + 1):
        H = []
        for g, (a, b, c, d) in enumerate(G.elts):
            G.work.tick()
            if point == q:
                image = q if c == 0 else F.mul[a][F.inv[c]]
            else:
                numerator = F.add[F.mul[a][point]][b]
                denominator = F.add[F.mul[c][point]][d]
                image = q if denominator == 0 else F.mul[numerator][F.inv[denominator]]
            if image == point:
                H.append(g)
        stabilizers.append(mask_of(H))
    require(len(set(stabilizers)) == q + 1, "POINT_STABILIZER_DISTINCT")
    for H in stabilizers:
        require(H.bit_count() * (q + 1) == G.n, "POINT_STABILIZER_INDEX")
    G.subgroup(stabilizers[0])
    return stabilizers


def normalizer_of_cyclic5(G, within):
    z = next((g for g in members(within) if G.order_at_most(g, 5) == 5), None)
    require(z is not None, "NO_ELEMENT_ORDER_FIVE")
    cyclic = G.gen([z])
    require(cyclic.bit_count() == 5, "ORDER_FIVE_CLOSURE")
    t = G.table
    normalizer = mask_of(x for x in members(within)
                         if cyclic & (1 << t[t[x][z]][G.inv[x]]))
    G.subgroup(normalizer)
    return normalizer


def find_a5(G):
    twos, threes, fives = [], [], set()
    for x in range(G.n):
        G.work.tick()
        order = G.order_at_most(x, 5)
        if order == 2:
            twos.append(x)
        elif order == 3:
            threes.append(x)
        elif order == 5:
            fives.add(x)
    attempts = 0
    for x, y in product(twos, threes):
        G.work.tick()
        if G.table[x][y] not in fives:
            continue
        attempts += 1
        if attempts > 4000:
            raise Incomplete("A5_SEARCH_CAP")
        H = G.gen((x, y), max_size=60)
        if H is not None and H.bit_count() == 60:
            G.subgroup(H)
            return H
    raise Incomplete("A5_NOT_CONSTRUCTED")


def subfield_pgl3(G):
    F = G.f
    require(F.p == 3 and F.q == 9 and F.mul[3][3] == 2, "PGL_FIELD")
    H = set()
    for a, b, c, d in product(range(3), repeat=4):
        det = F.sub(F.mul[a][d], F.mul[b][c])
        if det not in (1, 2):
            continue
        scale = 1 if det == 1 else 3
        matrix = tuple(F.mul[scale][x] for x in (a, b, c, d))
        H.add(G.number[G.norm(matrix)])
    H = mask_of(H)
    require(H.bit_count() == 24, "PGL3_ORDER")
    G.subgroup(H)
    return H


def outer_images(G, H):
    F = G.f
    squares = {F.mul[x][x] for x in range(1, F.q)}
    t = next(x for x in range(1, F.q) if x not in squares)
    t_inv = F.inv[t]
    images = []
    for diagonal, frobenius in product((False, True), repeat=2):
        transformed = []
        for g in members(H):
            G.work.tick()
            a, b, c, d = G.elts[g]
            if diagonal:
                b, c = F.mul[t][b], F.mul[t_inv][c]
            if frobenius:
                a, b, c, d = (F.mul[F.mul[x][x]][x] for x in (a, b, c, d))
            transformed.append(G.number[G.norm((a, b, c, d))])
        K = mask_of(transformed)
        require(K.bit_count() == H.bit_count(), "OUTER_IMAGE_COLLISION")
        G.subgroup(K)
        images.append(K)
    return images


def classes_from_outer(G, H, expected_size, expected_classes):
    classes, seen = [], set()
    for K in outer_images(G, H):
        if K in seen:
            continue
        orbit = G.conjugates(K)
        require(len(orbit) == expected_size, "CONJUGACY_CLASS_SIZE")
        require(not (orbit & seen), "CONJUGACY_ORBIT_OVERLAP")
        classes.append(orbit)
        seen.update(orbit)
    require(len(classes) <= expected_classes, "TOO_MANY_OUTER_CLASSES")
    return classes


def action6(G, H):
    cosets = G.cosets(H)
    require(len(cosets) == 6, "ACTION_NOT_DEGREE_SIX")
    representatives = [x for x, _ in cosets]
    point_of = {}
    for i, (_, C) in enumerate(cosets):
        for g in members(C):
            point_of[g] = i
    action = [[point_of[G.table[g][r]] for r in representatives] for g in range(G.n)]
    for perm in action:
        require(len(set(perm)) == 6, "ACTION_NOT_PERMUTATION")
    stabilizers = [mask_of(g for g in range(G.n) if action[g][i] == i) for i in range(6)]
    require(len(set(stabilizers)) == 6, "SIX_STABILIZERS_NOT_DISTINCT")
    for i in range(6):
        require(stabilizers[i] == G.conjugate(H, representatives[i]), "STABILIZER_CONJUGATE")
    cells = [[mask_of(g for g in range(G.n) if action[g][x] == y)
              for y in range(6)] for x in range(6)]
    for x, y in product(range(6), repeat=2):
        C = cells[x][y]
        require(C.bit_count() * 6 == G.n, "TRANSPORTER_SIZE")
        representative = next(members(C))
        require(C == G.left(representative, stabilizers[x]), "TRANSPORTER_LEFT_COSET")
    coords = list(product(range(6), repeat=2))
    for (x, y), (u, v) in product(coords, repeat=2):
        G.work.tick()
        intersection = (cells[x][y] & cells[u][v]).bit_count()
        if (x, y) == (u, v):
            require(intersection == G.n // 6, "SAME_CELL_INTERSECTION")
        elif x == u or y == v:
            require(intersection == 0, "ROW_COLUMN_NOT_DISJOINT")
        else:
            require(intersection == G.n // 30, "TWO_TRANSITIVITY_INTERSECTION")
    for triple in combinations(coords, 3):
        G.work.tick()
        sets = [cells[x][y] for x, y in triple]
        if all(not (sets[i] & sets[j]) for i, j in combinations(range(3), 2)):
            require(len({x for x, _ in triple}) == 1 or
                    len({y for _, y in triple}) == 1, "TRIPLE_NOT_ROW_OR_COLUMN")
    for i, omitted in product(range(6), repeat=2):
        row_union = 0
        col_union = 0
        for j in range(6):
            if j != omitted:
                row_union |= cells[i][j]
                col_union |= cells[j][i]
        require((G.all ^ row_union) == cells[i][omitted], "FIVE_ROW_COMPLEMENT")
        require((G.all ^ col_union) == cells[omitted][i], "FIVE_COLUMN_COMPLEMENT")
    return {"action": action, "stabilizers": stabilizers, "cells": cells}


def cross_class(G, H, first, second):
    action = second["action"]
    orbit = {action[h][0] for h in members(H)}
    require(len(orbit) == 6, "CROSS_CLASS_NOT_TRANSITIVE")
    for row1 in first["cells"]:
        for C in row1:
            for row2 in second["cells"]:
                for D in row2:
                    G.work.tick()
                    require((C & D).bit_count() == G.n // 36, "CROSS_CLASS_INTERSECTION")
    return 36 * 36


def check_disjoint(C, D):
    require(not (C & D), "FALSE_CROSS_CLASS_DISJOINTNESS")


def check_left(G, H, representative, C):
    require(C == G.left(representative, H), "COSET_SIDE")


def check_pack(G, pack):
    seen = set()
    for H, C in pack:
        require(C not in seen, "DOUBLE_COUNT")
        seen.add(C)
        representative = next(members(C))
        check_left(G, H, representative, C)
    for (H, C), (K, D) in combinations(pack, 2):
        require(not (C & D), "PACK_OVERLAP")
        require(gcd(G.n // H.bit_count(), G.n // K.bit_count()) <= 7, "PACK_GCD")


def all_subgroups(G, attempt_cap, universe=None):
    if universe is None:
        universe = G.all
    identity = 1 << G.one
    queue = [(identity, ())]
    seen = {identity}
    position = attempts = 0
    while position < len(queue):
        H, generators = queue[position]
        position += 1
        todo = universe ^ H
        while todo:
            G.work.tick()
            x = (todo & -todo).bit_length() - 1
            todo &= ~G.left(x, H)
            attempts += 1
            if attempts > attempt_cap:
                raise Incomplete("SUBGROUP_ENUMERATION_ATTEMPT_CAP")
            child_generators = generators + (x,)
            K = G.gen(child_generators)
            require(K & universe == K, "SUBGROUP_ENUMERATION_UNIVERSE")
            if K not in seen:
                seen.add(K)
                queue.append((K, child_generators))
    return seen, attempts


def q9_complement_extras(G, H):
    # H itself is a real representative of a sixth-transporter complement.
    subgroups, attempts = all_subgroups(G, 100000, H)
    vertices = []
    for U in sorted(subgroups):
        todo = H
        while todo:
            G.work.tick()
            representative = (todo & -todo).bit_length() - 1
            C = G.left(representative, U)
            require(C & H == C and C & todo == C, "COMPLEMENT_COSET_PARTITION")
            vertices.append((U, C))
            todo ^= C
    eligible = 0
    for (U, C), (V, D) in combinations(vertices, 2):
        G.work.tick()
        if gcd(G.n // U.bit_count(), G.n // V.bit_count()) <= 7:
            eligible += 1
            require(bool(C & D), "COMPLEMENT_TWO_EXTRA_COSETS_DISJOINT")
    return {"subgroups_in_complement_stabilizer": len(subgroups),
            "generation_attempts": attempts, "actual_contained_cosets": len(vertices),
            "low_gcd_coset_pairs_checked": eligible}


def q4_packing(G, subgroups, H6):
    vertices = []
    for H in sorted(subgroups):
        if H == G.all:
            continue
        for _, C in G.cosets(H):
            vertices.append((H, C))
    for (H, C), (K, D) in combinations(vertices, 2):
        G.work.tick()
        if gcd(G.n // H.bit_count(), G.n // K.bit_count()) == 1:
            require(bool(C & D), "COPRIME_ACTUAL_COSETS_DISJOINT")
    indices = sorted({G.n // H.bit_count() for H in subgroups if H != G.all})
    remaining = 0
    for values in combinations_with_replacement(indices, 8):
        G.work.tick()
        if any(not 2 <= gcd(x, y) <= 7 for x, y in combinations(values, 2)):
            continue
        if sum((Fraction(1, x) for x in values), Fraction()) <= 1:
            remaining += 1
    require(remaining == 0, "EIGHT_DENSITY_FEASIBLE_INDEX_PATTERNS")
    pack = [(H6, C) for _, C in G.cosets(H6)]
    require(len(pack) == 6, "Q4_SIX_COSET_FIXTURE")
    check_pack(G, pack)
    expect("DOUBLE_COUNT", lambda: check_pack(G, pack + [pack[0]]))
    witness = next((x for x in range(G.n) if G.left(x, H6) != G.right(H6, x)), None)
    require(witness is not None, "COSET_SIDE_MUTATION_UNAVAILABLE")
    check_left(G, H6, witness, G.left(witness, H6))
    expect("COSET_SIDE", lambda: check_left(G, H6, witness, G.right(H6, witness)))
    return {"subgroup_count_including_group": len(subgroups), "proper_indices": indices,
            "actual_cosets": len(vertices), "actual_disjoint_low_gcd_witness": 6,
            "eight_index_patterns_after_necessary_filters": remaining}


def check_label_fixture(G, labels, max_count):
    for H in labels:
        G.subgroup(H)
        require(H != G.all and G.n // H.bit_count() > 6, "LABEL_NOT_PROPER_GT6")
    for H, K in combinations(labels, 2):
        require(gcd(G.n // H.bit_count(), G.n // K.bit_count()) <= 7, "LABEL_GCD")
    require(len(labels) <= max_count, "MAX_LABEL")


def normal_cut_arithmetic(work):
    a = [1] * 6 + [2, 2]
    b = [66, 78, 102, 114, 138, 174, 2, 3]
    n = [a[i] * b[i] for i in range(8)]
    require(all(gcd(x, y) <= 7 for x, y in combinations(n, 2)), "NORMALCUT_ORIGINAL_GCD")
    require(all(2 <= gcd(b[j], b[k]) <= 7 for j in range(6) for k in (6, 7)),
            "NORMALCUT_FIBRE_GCD")
    density6 = sum((Fraction(1, x) for x in b[:6]), Fraction())
    require(density6 + max(Fraction(1, b[6]), Fraction(1, b[7])) <= 1,
            "NORMALCUT_FIBRE_DENSITY")
    possible = set()
    for d, e in product(range(2, 8), range(1, 8)):
        work.tick()
        if d * e <= 7:
            possible.add((d, e))
    expected = {(d, 1) for d in range(2, 8)} | {(2, 2), (2, 3), (3, 2)}
    require(possible == expected, "NORMALCUT_DE_ENUMERATION")
    return {"arithmetic_only_not_a_coset_realization": True, "a": a, "b": b,
            "n": n, "d": gcd(a[6], a[7]), "e": gcd(b[6], b[7]),
            "possible_d_e": sorted(possible)}


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def divisibility_grid(work):
    cases = repeated_triples = 0
    for p in (x for x in range(2, 48) if prime(x)):
        for f in range(2, 9):
            work.tick()
            q = p ** f
            if q in (4, 9):
                continue
            order = q * (q*q - 1) // gcd(2, q - 1)
            if p == 2:
                A, B = (9, 28) if q == 8 else (q + 1, 8)
                maximal_indices = [q + 1, (q // 2) * (q + 1), (q // 2) * (q - 1)]
                for r in (r for r in range(2, f + 1) if f % r == 0 and prime(r)):
                    q0 = p ** (f // r)
                    maximal_indices.append((q // q0) * (q*q - 1) // (q0*q0 - 1))
            else:
                A, B = (q + 1, p*p) if f >= 3 else ((q + 1) // 2, p*p)
                maximal_indices = [q + 1, q * (q + 1) // 2, q * (q - 1) // 2]
                for r in (r for r in range(2, f + 1) if f % r == 0 and prime(r)):
                    q0 = p ** (f // r)
                    suborder = q0 * (q0*q0 - 1) if r == 2 else q0 * (q0*q0 - 1) // 2
                    require(order % suborder == 0, "SUBFIELD_ORDER_DIVISION")
                    maximal_indices.append(order // suborder)
                if f == 2 and p % 10 in (3, 7):
                    require(order % 60 == 0, "A5_ORDER_DIVISION")
                    maximal_indices.append(order // 60)
            require(A > 7 and B > 7, "GRID_SMALL_DIVISOR")
            require(all(x % A == 0 or x % B == 0 for x in maximal_indices), "GRID_DIVISIBILITY")
            # product, not combinations: repeated proper labels are explicitly tested.
            for labels in product(maximal_indices, repeat=3):
                work.tick()
                require(any(gcd(x, y) >= 8 for x, y in combinations(labels, 2)), "GRID_J7_TRIPLE")
                repeated_triples += 1
            cases += 1
    return {"prime_bound_inclusive": 47, "exponent_range": [2, 8], "cases": cases,
            "ordered_label_triples_including_repetitions": repeated_triples,
            "scope": "finite arithmetic grid only; conditional on the stated maximal-index list"}


def main():
    work = Budget()
    out = {"overall": "INCOMPLETE", "child_execution_at_authoring": "NOT RUN",
           "stages": {}, "mutations": {}, "limitations": []}
    try:
        F4, F9 = Field(2, 1), Field(3, 0)
        F4.validate(work)
        F9.validate(work)
        expect("NONFIELD_ZERO_DIVISOR", lambda: Field(3, 1).validate(work))
        out["mutations"]["bad_field"] = "NONFIELD_ZERO_DIVISOR"
        G4, G9 = Group(F4, work), Group(F9, work)
        require(G4.n == 60 and G9.n == 360, "PROJECTIVE_GROUP_ORDERS")
        G9.check_center(G9.norm)
        expect("PROJECTIVE_CENTER", lambda: G9.check_center(lambda matrix: matrix))
        out["mutations"]["projective_center"] = "PROJECTIVE_CENTER"
        out["stages"]["orders_and_perfectness"] = {
            "q4_order": G4.n, "q9_order": G9.n,
            "q4": generation_and_perfectness(G4), "q9": generation_and_perfectness(G9)}
        P4, P9 = point_stabilizers(G4), point_stabilizers(G9)
        H46 = normalizer_of_cyclic5(G4, G4.all)
        require(H46.bit_count() == 10, "Q4_INDEX6_SUBGROUP")
        A46 = action6(G4, H46)
        out["stages"]["q4_actual_degree5_and_degree6"] = {
            "degree5_point_stabilizers": len(P4), "degree6_point_stabilizers": len(A46["stabilizers"]),
            "same_class_transporter_intersections_and_complements": "CHECKED"}
        H96 = find_a5(G9)
        H915 = subfield_pgl3(G9)
        c6 = classes_from_outer(G9, H96, 6, 2)
        c15 = classes_from_outer(G9, H915, 15, 2)
        first6 = action6(G9, H96)
        out["stages"]["q9_actual_subgroups"] = {
            "degree10_point_stabilizers": len(P9), "a5_conjugacy_class_count_constructed": len(c6),
            "pgl3_conjugacy_class_count_constructed": len(c15),
            "same_class_transporter_intersections_and_complements": "CHECKED"}
        if len(c6) == 2:
            H96b = next(iter(c6[1]))
            second6 = action6(G9, H96b)
            cross_pairs = cross_class(G9, H96, first6, second6)
            expect("FALSE_CROSS_CLASS_DISJOINTNESS",
                   lambda: check_disjoint(first6["cells"][0][0], second6["cells"][0][0]))
            out["mutations"]["false_cross_class_disjointness"] = "FALSE_CROSS_CLASS_DISJOINTNESS"
            out["stages"]["q9_cross_class"] = {"status": "CHECKED", "orbit_size": 6,
                                                "actual_coset_pairs": cross_pairs,
                                                "intersection_size": G9.n // 36}
        else:
            out["stages"]["q9_cross_class"] = {"status": "NOTTESTED", "reason": "second actual class unavailable"}
            out["mutations"]["false_cross_class_disjointness"] = "NOTTESTED"
            out["limitations"].append("SECOND_INDEX6_CLASS_NOT_CONSTRUCTED")
        H936 = normalizer_of_cyclic5(G9, H96)
        require(H936.bit_count() == 10, "Q9_INDEX36_SUBGROUP")
        labels = [P9[0], H915, H936]
        check_label_fixture(G9, labels, 3)
        expect("MAX_LABEL", lambda: check_label_fixture(G9, labels, 2))
        out["mutations"]["max_label_false_cap_two"] = "MAX_LABEL"
        out["stages"]["q9_real_low_gcd_gt6_labels"] = [G9.n // H.bit_count() for H in labels]
        out["stages"]["q9_complement_extras_first_class"] = q9_complement_extras(G9, H96)
        if len(c6) == 2:
            out["stages"]["q9_complement_extras_second_class"] = q9_complement_extras(G9, H96b)
        else:
            out["stages"]["q9_complement_extras_second_class"] = {"status": "NOTTESTED"}
        out["stages"]["normal_cut_arithmetic"] = normal_cut_arithmetic(work)
        out["stages"]["classification_conditional_grid"] = divisibility_grid(work)
        sub4, attempts4 = all_subgroups(G4, 100000)
        require(H46 in sub4 and P4[0] in sub4, "Q4_ENUMERATION_MISSING_SUBGROUP")
        out["stages"]["q4_actual_packing"] = q4_packing(G4, sub4, H46)
        out["stages"]["q4_actual_packing"]["subgroup_generation_attempts"] = attempts4
        out["mutations"]["coset_side"] = "COSET_SIDE"
        out["mutations"]["double_count"] = "DOUBLE_COUNT"
        sub9, attempts9 = all_subgroups(G9, 300000)
        C6 = set().union(*c6)
        C10 = set(P9)
        C15 = set().union(*c15)
        if len(c6) != 2 or len(c15) != 2:
            out["stages"]["q9_exhaustive_maximal_cover"] = {
                "status": "NOTTESTED", "reason": "required actual maximal class unavailable",
                "subgroup_count_including_group": len(sub9), "generation_attempts": attempts9}
            out["limitations"].append("EXPECTED_MAXIMAL_CLASSES_INCOMPLETE")
        else:
            cover = C6 | C10 | C15
            for H in cover:
                require(H in sub9, "COVER_SUBGROUP_MISSING")
            for H in sub9:
                work.tick()
                if H != G9.all:
                    require(any(H & K == H for K in cover), "MAXIMAL_COVER_FAILURE")
            for H in cover:
                require(not any(H != K and H & K == H and K != G9.all for K in sub9),
                        "CLAIMED_COVER_SUBGROUP_NOT_MAXIMAL")
            for index, claimed in ((6, C6), (10, C10), (15, C15)):
                actual = {H for H in sub9 if H.bit_count() * index == G9.n}
                require(actual == claimed, "INDEX_CLASS_COVER_FAILURE_" + str(index))
            out["stages"]["q9_exhaustive_maximal_cover"] = {
                "status": "CHECKED", "subgroup_count_including_group": len(sub9),
                "generation_attempts": attempts9, "index6": len(C6),
                "index10": len(C10), "index15": len(C15)}
        out["overall"] = "INCOMPLETE" if out["limitations"] else "PASS_BOUNDED_ASSAY_ONLY"
    except Incomplete as exc:
        out["limitations"].append(str(exc))
    except Violation as exc:
        out["overall"] = "FAIL"
        out["failure"] = str(exc)
    except Exception as exc:
        out["overall"] = "ERROR"
        out["failure"] = type(exc).__name__ + ": " + str(exc)
    out["budget_steps"] = work.steps
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
