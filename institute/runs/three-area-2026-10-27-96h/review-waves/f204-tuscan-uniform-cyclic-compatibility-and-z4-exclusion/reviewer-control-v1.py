#!/usr/bin/env python3
"""Independent bounded finite diagnostics, not a proof at order twelve."""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import gcd


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def shift(v, q, r, e=1):
    return ((v // r + e) % q) * r + v % r


def canon(c):
    i = c.index(0)
    return c[i:] + c[:i]


def pair_type(x, z, q, r):
    return (x % r, z % r, (z // r - x // r) % q)


def aligned_middle(x, y, q, r):
    return ((y // r - x // r) % q, y % r)


def events(c):
    n = len(c)
    return [(c[j], c[(j + 1) % n], c[(j + 2) % n]) for j in range(n)]


def cut_ok(triples, u):
    pairs = [(x, z) for x, y, z in triples if u not in (x, y, z)]
    return len(pairs) == len(set(pairs))


def compatible(records, q, r):
    orbit = {t * r for t in range(q)}
    groups = defaultdict(list)
    for lam, middle in records:
        groups[lam].append(middle)
    for (a, b, d), middles in groups.items():
        for (h, c), (hp, cp) in combinations(middles, 2):
            if not orbit <= {a, d * r + b, h * r + c, hp * r + cp}:
                return False
    return True


def family_control(n, q):
    r = n // q
    representatives = []
    seen = Counter()
    for rest in permutations(range(1, n)):
        c = (0,) + rest
        images = sorted({canon(tuple(shift(v, q, r, e) for v in c))
                         for e in range(q)})
        if c != images[0]:
            continue
        s = q // len(images)
        length = n // s
        stabilizers = [e for e in range(q)
                       if canon(tuple(shift(v, q, r, e) for v in c)) == c]
        check(len(stabilizers) == s, 'wrong stabilizer size')
        check(any(all(c[(j + length) % n] == shift(c[j], q, r, e)
                      for j in range(n)) for e in stabilizers),
              'missing length-step stabilizer generator')
        ts = [events(image) for image in images]
        triples = [triple for batch in ts for triple in batch]
        actual_arcs = [(x, y) for x, y, _ in triples]
        types = [pair_type(c[j], c[(j + 1) % n], q, r)
                 for j in range(length)]
        distinct_types = len(types) == len(set(types))
        actual_unique = len(actual_arcs) == len(set(actual_arcs))
        check(distinct_types == actual_unique, 'D1 type/actual inequivalence')
        seen['orbits'] += 1
        if not distinct_types:
            seen['D1_duplicate'] += 1
            continue
        records = [(pair_type(c[j], c[(j + 2) % n], q, r),
                    aligned_middle(c[j], c[(j + 1) % n], q, r))
                   for j in range(length)]
        check(len(records) == len(set(records)), 'repeated aligned triple')
        compat = compatible(records, q, r)
        direct = [cut_ok(triples, t * r) for t in range(q)]
        check(all(v == compat for v in direct), 'compatibility/cut inequivalence')
        seen['D1_unique'] += 1
        seen['compatible' if compat else 'incompatible'] += 1
        if len(representatives) < 180:
            representatives.append((set(types), records, triples))
    check(seen['D1_unique'] and seen['D1_duplicate'], 'missing D1 positive/negative')
    check(seen['compatible'] and seen['incompatible'], 'missing cut positive/negative')
    pair_checks = 0
    pair_good = 0
    for left, right in combinations(representatives, 2):
        if left[0] & right[0]:
            continue
        records = left[1] + right[1]
        triples = left[2] + right[2]
        check(len(records) == len(set(records)), 'cross-orbit repeated triple')
        compat = compatible(records, q, r)
        check(all(cut_ok(triples, t * r) == compat for t in range(q)),
              'two-orbit compatibility/cut inequivalence')
        pair_checks += 1
        pair_good += bool(compat)
    print(f'FAMILY n={n} q={q} counts={dict(seen)} '
          f'disjoint_D1_pairs={pair_checks} compatible_pairs={pair_good}')


def local_12_control(q):
    r = 12 // q
    O = {t * r for t in range(q)}
    c = Counter()
    max_multiplicity = Counter()
    for x in range(12):
        for z in range(12):
            if x == z:
                continue
            mids = [v for v in range(12) if v not in (x, z)]
            for y, yp in combinations(mids, 2):
                inside = O <= {x, y, yp, z}
                directly = all(not (v not in (x, y, z) and
                                    v not in (x, yp, z)) for v in O)
                check(inside == directly, 'four-set/cuts inequivalence')
                c['all_pairs'] += 1
                if not inside:
                    continue
                c['compatible_pairs'] += 1
                end_count = int(x in O) + int(z in O)
                if q == 2:
                    if end_count == 0:
                        check({y, yp} == O, 'q2 outside endpoints')
                    elif end_count == 1:
                        check((O - {x, z}) <= {y, yp}, 'q2 one endpoint')
                    else:
                        check(y not in O and yp not in O, 'q2 both endpoints')
                elif q == 3:
                    if ({x, y, z} <= O or {x, yp, z} <= O):
                        c['all_O_triple_excluded'] += 1
                        continue
                    check(end_count == 1 and {y, yp} == O - {x, z},
                          'q3 residual coincidence form')
                    c['q3_residual'] += 1
                else:
                    check({x, y, yp, z} == O, 'q4 coincidence not exactly O')
    # Exhaust every set of middles for one endpoint pair, including multiplicities >2.
    for x in range(12):
        for z in range(12):
            if x == z:
                continue
            mids = [v for v in range(12) if v not in (x, z)]
            category = int(x in O) + int(z in O)
            for mask in range(1 << len(mids)):
                chosen = [v for i, v in enumerate(mids) if mask & (1 << i)]
                if len(chosen) < 2:
                    continue
                if q == 3 and any({x, y, z} <= O for y in chosen):
                    continue
                if not all(O <= {x, z, y, yp} for y, yp in combinations(chosen, 2)):
                    continue
                max_multiplicity[category] = max(max_multiplicity[category], len(chosen))
                if q == 2:
                    check(len(chosen) <= (10 if category == 2 else 2), 'q2 multiplicity')
                elif q == 3:
                    check(category == 1 and len(chosen) == 2, 'q3 multiplicity')
                else:
                    check(category == 2 and len(chosen) == 2, 'q4 multiplicity')
    print(f'LOCAL12 q={q} counts={dict(c)} '
          f'max_repeated_multiplicity_by_endpoint_count={dict(max_multiplicity)}')


def negative_and_closure_control():
    for q, x, z, y, yp, missing in [(2, 1, 2, 3, 6, 0),
                                     (3, 1, 2, 0, 4, 8),
                                     (4, 0, 3, 6, 1, 9)]:
        r = 12 // q
        O = {t * r for t in range(q)}
        check(missing in O and not O <= {x, z, y, yp}, 'bad negative fixture')
        check(not cut_ok([(x, y, z), (x, yp, z)], missing),
              'negative did not collide at omitted cut')
    for x, y, z in permutations(range(3)):
        a = (y - x) % 3
        check(a in (1, 2) and z == (x + 2 * a) % 3, 'not a 3-orbit triple')
        translated = ((x + a) % 3, (y + a) % 3, (z + a) % 3)
        check(translated[:2] == (y, z) and translated[2] == x,
              '3-orbit arc does not force closure')
    expected = {1: {(2, 3), (3, 2)}, 2: {(1, 1), (3, 3)},
                3: {(1, 2), (2, 1)}}
    for d in (1, 2, 3):
        mids = [v for v in range(4) if v not in (0, d)]
        forced = {}
        observed = set()
        for y in mids:
            for t in range(4):
                x, mid, z = t, (y + t) % 4, (d + t) % 4
                arc = (x, mid)
                check(arc not in forced or forced[arc] == z, 'inconsistent forced arc')
                forced[arc] = z
                observed.add(((mid - x) % 4, (z - mid) % 4))
        check(observed == expected[d], 'wrong Z4 transition table')
        for arc in forced:
            x, y = arc
            visited = {x}
            for _ in range(5):
                if y in visited:
                    break
                visited.add(y)
                check((x, y) in forced, 'forced walk escaped')
                x, y = y, forced[(x, y)]
            else:
                raise AssertionError('no repeat in four-vertex forced walk')
            check(len(visited) <= 4, 'forced walk leaves O')
        partial = dict(forced)
        del partial[next(iter(partial))]
        check(len(partial) < len(forced), 'partial-negative failed to remove constraints')
        check(any((y, z) not in partial for (x, y), z in partial.items()),
              'partial-negative should permit escape from prescribed arcs')
    print('NEGATIVES omitted-orbit-cut=3/3; Z3 translated-triples=6/6; '
          'Z4 transition-tables=3/3 and incomplete-translation-negatives=3/3')


def capacity_and_jump_control():
    for s, wanted in [(2, {6}), (3, {4, 8})]:
        displacements = {k for k in range(12) if 12 // gcd(12, k) == s}
        check(displacements == wanted and 1 not in displacements, 'stabilizer displacement')
    arcs = [(x, y) for x in range(3) for y in range(3) if x != y]
    reasons = Counter()
    for (x, y), (z, w) in combinations(arcs, 2):
        if x == z or y == w:
            reasons['shared_tail_or_head'] += 1
        elif x == w and y == z:
            reasons['two_cycle'] += 1
        else:
            check(y == z or w == x, 'unclassified internal two-arc configuration')
            reasons['three_vertex_path'] += 1
    check(sum(reasons.values()) == 15, 'incomplete three-point arc pairs')
    z2 = [(a, 11 - 2*a) for a in range(1, 6)]
    z3 = [(a, 11 - 3*a) for a in range(2, 4)]
    z4 = [(a, b, 11 - 4*a - 2*b) for a in range(1, 3)
          for b in range(6) if 11 - 4*a - 2*b >= 0]
    check({f for _, f in z2} == {1, 3, 5, 7, 9}, 'q2 capacity')
    check(z3 == [(2, 5), (3, 2)], 'q3 capacity')
    check({a for a, b, c in z4} == {1, 2} and all(c % 2 for a, b, c in z4),
          'q4 capacity')
    identity_count = 0
    for q in (2, 4, 6, 8):
        for length in range(1, 5):
            for ds in product(range(q), repeat=length):
                actual = sum(ds[j] + ds[(j + 1) % length] for j in range(length)) % q
                check(actual == (2 * sum(ds)) % q, 'periodic jump identity')
                identity_count += 1
        for r in (1, 3, 5, 7):
            S = sum(d for a in range(r) for b in range(r) for d in range(q)
                    if (a, b, d) != (a, a, 0)) % q
            check(S == q // 2 and 2*S % q == 0, 'jump sum residue')
    ds = (1, 0)
    unwrapped = sum(ds[j] + ds[j+1] for j in range(len(ds)-1)) % 4
    check(unwrapped != 2 * sum(ds) % 4, 'unwrapped negative failed')
    print(f'CAPACITY displacements=2/2 internal_arc_pair_reasons={dict(reasons)} '
          f'Z2={z2} Z3={z3} Z4={z4}')
    print(f'JUMPS identities={identity_count}; even-q/odd-r residue cases=16; '
          f'unwrapped-negative=(q4,{ds},actual={unwrapped},claimed={2*sum(ds)%4})')


def main():
    for q in (2, 3, 4):
        local_12_control(q)
    negative_and_closure_control()
    capacity_and_jump_control()
    for n, q in ((8, 2), (9, 3), (8, 4)):
        family_control(n, q)
    print('CONTROL COMPLETED')


if __name__ == '__main__':
    main()
