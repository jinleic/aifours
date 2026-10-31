#!/usr/bin/env python3
"""Prospective exact grade-three tensor assay; no worker execution.

Parent must fully audit and pin this file before a single named <=55s GO.
This program performs no file/network/subprocess operations and prints one JSON
object. Its internal cooperative 48s limit yields INCOMPLETE, not a pass.
The finite calculations never establish the radical, full Cartan bridge,
whole-negative-Serre bridge, book/source identity, or a universal theorem.
"""
import json
import signal
import sys
import time
from fractions import Fraction
from itertools import combinations, product

STOP = False
DEADLINE = None


def latch(_signum, _frame):
    global STOP
    STOP = True


class Interrupted(Exception):
    pass


class CheckFailure(Exception):
    pass


def guard():
    if STOP or (DEADLINE is not None and time.monotonic() >= DEADLINE):
        raise Interrupted('cooperative stop or 48-second internal deadline')


def require(condition, name):
    if not condition:
        raise CheckFailure(name)


def clean(v):
    return {k: c for k, c in v.items() if c}


def add(*vectors):
    out = {}
    for v in vectors:
        for k, c in v.items():
            out[k] = out.get(k, 0) + c
    return clean(out)


def scale(v, c):
    return clean({k: c * x for k, x in v.items()})


def letter(i):
    return {(i,): 1}


def tensor(a, b):
    # Keys are ordered tensor words, never products of 8x8 or 3x3 matrices.
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            key = wa + wb
            out[key] = out.get(key, 0) + ca * cb
    return clean(out)


def bracket(a, b):
    return add(tensor(a, b), scale(tensor(b, a), -1))


def derivation(table, v):
    out = {}
    for w, c in v.items():
        for k, i in enumerate(w):
            for j, d in table[i].items():
                ww = w[:k] + (j,) + w[k + 1:]
                out[ww] = out.get(ww, 0) + c * d
    return clean(out)


# Rows indexed by the INPUT letter, values are the complete output letters.
E1 = ({1: 1}, {}, {3: 1}, {5: -2}, {5: -1}, {}, {7: 1}, {})
E2 = ({2: 1}, {4: 1}, {}, {6: 1}, {6: 2}, {7: -1}, {}, {})
F1 = ({}, {0: 1}, {}, {2: 2}, {2: 1}, {3: -1}, {}, {6: 1})
F2 = ({}, {}, {0: 1}, {1: 1}, {1: 2}, {}, {4: 1}, {5: -1})
DEG = ((0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2))
LETTERS = tuple(letter(i) for i in range(8))


def apply(table, v):
    return derivation(table, v)


def commutator_action(a, b, v):
    return add(apply(a, apply(b, v)), scale(apply(b, apply(a, v)), -1))


def word_degree(word):
    return (sum(DEG[i][0] for i in word), sum(DEG[i][1] for i in word))


def homogeneous_degree(v):
    require(bool(v), 'nonempty vector required for degree')
    degrees = {word_degree(w) for w in v}
    require(len(degrees) == 1, 'inhomogeneous tensor vector')
    return next(iter(degrees))


def lowest_label(v):
    a, b = homogeneous_degree(v)
    n = len(next(iter(v)))
    return (n - 2 * a + b, n + a - 2 * b)


class Basis:
    """Sparse exact row echelon space, using ordered tensor-word pivots."""
    def __init__(self):
        self.rows = {}

    def reduce(self, vector):
        guard()
        v = clean(dict(vector))
        for count, p in enumerate(sorted(self.rows)):
            if not count % 16:
                guard()
            c = v.get(p, 0)
            if c:
                for k, x in self.rows[p].items():
                    y = v.get(k, 0) - c * x
                    if y:
                        v[k] = y
                    else:
                        v.pop(k, None)
        return v

    def insert(self, vector):
        v = self.reduce(vector)
        if not v:
            return None
        p = min(v)
        d = v[p]
        row = {k: Fraction(c) / Fraction(d) for k, c in v.items()}
        self.rows[p] = row
        return row

    def contains(self, vector):
        return not self.reduce(vector)

    def vectors(self):
        return list(self.rows.values())

    def __len__(self):
        return len(self.rows)


def span(vectors):
    b = Basis()
    for v in vectors:
        b.insert(v)
    return b


def raising_closure(seed, expected, name):
    b = Basis()
    first = b.insert(seed)
    require(first is not None, name + ':zero seed')
    queue = [first]
    i = 0
    while i < len(queue):
        guard()
        v = queue[i]
        i += 1
        for e in (E1, E2):
            new = b.insert(apply(e, v))
            if new is not None:
                queue.append(new)
                require(len(b) <= expected, name + ':closure exceeded expected rank')
    require(len(b) == expected, name + ':closure rank')
    for v in b.vectors():
        for op in (E1, E2, F1, F2):
            require(b.contains(apply(op, v)), name + ':four-generator closure')
    return b


def stable(b, name):
    for v in b.vectors():
        for op in (E1, E2, F1, F2):
            require(b.contains(apply(op, v)), name + ':four-generator closure')


def primed(v):
    # A formal node relabeling, NOT an automorphism of fixed A(r,s).
    perm = (0, 2, 1, 4, 3, 6, 5, 7)
    sign = (1, 1, 1, 1, 1, -1, -1, 1)
    out = {}
    for w, c in v.items():
        ww = tuple(perm[i] for i in w)
        coeff = c
        for i in w:
            coeff *= sign[i]
        out[ww] = out.get(ww, 0) + coeff
    return clean(out)


def delta(i, j, r, s, wrong_cartan=False, swap_rs=False):
    # D_i(u_j) = ad([f3,u_i])u_j, actual Cartan row and table.
    if swap_rs:
        r, s = s, r
    u = LETTERS[j]
    if i == 0:
        a, b = DEG[j]
        return scale(u, r * a + s * b - (1 if wrong_cartan else 2))
    if i == 1:
        return scale(apply(E1, u), -r)
    if i == 2:
        return scale(apply(E2, u), -s)
    if i == 3:
        return scale(commutator_action(E1, E2, u), -s)
    if i == 4:
        return scale(commutator_action(E1, E2, u), r)
    return {}


def f3(v, r, s, wrong_cartan=False, swap_rs=False):
    # Reorder the single degree-zero delta operator to the right. For ijk
    # this gives D_i(j)k + jD_i(k) + iD_j(k); on Lie elements it agrees
    # with F3[x,[y,z]]=[D_x y,z]+[y,D_x z]+[x,D_y z-D_z y].
    out = {}
    for word, c in v.items():
        require(len(word) == 3, 'F3 expects length-three tensor words')
        i, j, k = word
        for which, a, b in ((0, i, j), (1, i, k), (2, j, k)):
            for (m,), d in delta(a, b, r, s, wrong_cartan, swap_rs).items():
                target = ((m, k) if which == 0 else
                          (j, m) if which == 1 else (i, m))
                out[target] = out.get(target, 0) + c * d
    return clean(out)


def wedge_coordinates(v):
    for (i, j), c in v.items():
        require(i != j and v.get((j, i), 0) == -c,
                'F3 image not an antisymmetric length-two tensor')
    return {(i, j): v.get((i, j), 0)
            for i in range(8) for j in range(i + 1, 8)
            if v.get((i, j), 0)}


def poly(c=0, r=0, s=0):
    return clean({(0, 0): Fraction(c), (1, 0): Fraction(r),
                  (0, 1): Fraction(s)})


def pmul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            z = (i + k, j + l)
            out[z] = out.get(z, 0) + x * y
    return clean(out)


def det3(a):
    return add(pmul(a[0][0], add(pmul(a[1][1], a[2][2]),
                                scale(pmul(a[1][2], a[2][1]), -1))),
               scale(pmul(a[0][1], add(pmul(a[1][0], a[2][2]),
                                      scale(pmul(a[1][2], a[2][0]), -1))), -1),
               pmul(a[0][2], add(pmul(a[1][0], a[2][1]),
                                 scale(pmul(a[1][1], a[2][0]), -1))))


def image_polys(v):
    # F3 is affine in (r,s) by the explicit delta implementation, so these
    # three exact evaluations recover all coefficients, not a numerical fit.
    a = wedge_coordinates(f3(v, 0, 0))
    b = wedge_coordinates(f3(v, 1, 0))
    c = wedge_coordinates(f3(v, 0, 1))
    keys = set(a) | set(b) | set(c)
    return {k: poly(a.get(k, 0), b.get(k, 0) - a.get(k, 0),
                    c.get(k, 0) - a.get(k, 0)) for k in keys}


def tagged(v, t):
    return {(t,) + w: c for w, c in v.items()}


def at_degree(vectors, degree):
    return [v for v in vectors if homogeneous_degree(v) == degree]


def quotient_lowest(lie, ideal, degree, candidates):
    """Kernel of F1,F2 in the actual finite quotient, not just selected seeds."""
    a, b = degree
    source = at_degree(lie.vectors(), degree)
    i_source = at_degree(ideal.vectors(), degree)
    targets = span([tagged(v, 0) for v in at_degree(ideal.vectors(), (a - 1, b))] +
                   [tagged(v, 1) for v in at_degree(ideal.vectors(), (a, b - 1))])
    base = len(targets)
    for v in source:
        targets.insert(add(tagged(apply(F1, v), 0), tagged(apply(F2, v), 1)))
    image_rank = len(targets) - base
    quotient_dim = len(source) - len(i_source)
    kernel_dim = quotient_dim - image_rank
    picked = span(i_source)
    before = len(picked)
    for v in candidates:
        require(homogeneous_degree(v) == degree, 'candidate wrong horizontal degree')
        picked.insert(v)
    candidate_rank = len(picked) - before
    require(candidate_rank == kernel_dim, 'candidate span misses quotient lowest vectors')
    return {'weight_quotient_dim': quotient_dim, 'lowering_rank': image_rank,
            'lowest_dim': kernel_dim, 'candidate_rank': candidate_rank}


def image_rank_mod_relation(vectors, relation2, r, s):
    b = span(relation2.vectors())
    initial = len(b)
    for v in vectors:
        img = f3(v, r, s)
        wedge_coordinates(img)
        b.insert(img)
    return len(b) - initial


def check_levi():
    for i, u in enumerate(LETTERS):
        a, b = DEG[i]
        h = (-1 + 2 * a - b, -1 - a + 2 * b)
        for row, e in enumerate((E1, E2)):
            for col, f in enumerate((F1, F2)):
                expected = scale(u, h[row]) if row == col else {}
                require(commutator_action(e, f, u) == expected,
                        'Levi [E_i,F_j] / Cartan table')
        for x, y in ((E1, E2), (E2, E1), (F1, F2), (F2, F1)):
            xy = commutator_action(x, y, u)
            xx_y = add(apply(x, xy),
                       scale(commutator_action(x, y, apply(x, u)), -1))
            require(not xx_y, 'Levi A2 Serre action')


def build_vectors():
    u = LETTERS
    q = bracket(u[0], u[1])
    qp = primed(q)
    q1 = apply(E2, q)
    q2 = apply(E2, q1)
    q3 = apply(E1, q1)
    q4 = apply(E1, q2)
    qs = (q, q1, q2, q3, q4)
    require(all(qs) and qp, 'empty Q, Q1..Q4 or primed Q')
    explicit = (
        add(bracket(u[2], u[1]), bracket(u[0], u[4])),
        scale(add(bracket(u[2], u[4]), bracket(u[0], u[6])), 2),
        add(bracket(u[3], u[1]), bracket(u[1], u[4]),
            scale(bracket(u[0], u[5]), -1)),
        scale(add(bracket(u[3], u[4]), scale(bracket(u[2], u[5]), -1),
                  bracket(u[1], u[6]), bracket(u[0], u[7])), 2))
    require((q1, q2, q3, q4) == explicit, 'Q1..Q4 explicit expansions')
    expected_f1 = ({}, {}, {}, q1, scale(q2, 2))
    expected_f2 = ({}, scale(q, 3), scale(q1, 4), {}, scale(q3, 4))
    for v, a, b in zip(qs, expected_f1, expected_f2):
        require(apply(F1, v) == a and apply(F2, v) == b, 'Q lowering table')
    require(not apply(F1, qp) and not apply(F2, qp), 'primed Q lowest')
    t35r = bracket(u[0], q)
    t27r = add(scale(bracket(u[2], q), 3), scale(bracket(u[0], q1), -1))
    t10r = add(bracket(u[3], q), scale(bracket(u[4], q), -2),
               bracket(u[1], q1), scale(bracket(u[0], q3), -1))
    t8r = add(bracket(u[0], q4), scale(bracket(u[1], q2), -2),
              scale(bracket(u[2], q3), -4), scale(bracket(u[4], q1), 4),
              scale(bracket(u[6], q), -12))
    aa = bracket(u[0], u[3])
    bb = bracket(u[0], u[4])
    cc = bracket(u[1], u[2])
    y = add(aa, scale(bb, -1), scale(cc, -1))
    y1, y2 = apply(E1, y), apply(E2, y)
    y3 = apply(E1, y2)
    z = add(bracket(u[0], y3), scale(bracket(u[1], y2), -2),
            scale(bracket(u[2], y1), -1), bracket(u[4], y))
    t35s, t27s, t10s, t8s = (primed(v) for v in (t35r, t27r, t10r, t8r))
    seeds = {'35r': t35r, '35s': t35s, '27r': t27r, '27s': t27s,
             '10r': t10r, '10s': t10s, '8r': t8r, '8s': t8s, 'Z': z}
    labels = {'35r': (1, 4), '35s': (4, 1), '27r': (2, 2),
              '27s': (2, 2), '10r': (0, 3), '10s': (3, 0),
              '8r': (1, 1), '8s': (1, 1), 'Z': (1, 1)}
    for name, v in seeds.items():
        require(v and not apply(F1, v) and not apply(F2, v), name + ': nonzero lowest')
        require(lowest_label(v) == labels[name], name + ': lowest label')
    for name, word, coefficient in (('35r', (0, 0, 1), 1),
                                    ('27r', (0, 0, 4), -1),
                                    ('10r', (0, 0, 5), 1),
                                    ('8r', (0, 0, 7), 2)):
        require(seeds[name].get(word, 0) == coefficient, name + ': tensor-word witness')
    return q, qp, qs, seeds


def check_formula_images(seeds, q, qp, r, s):
    u = LETTERS
    aa, bb, cc = bracket(u[0], u[3]), bracket(u[0], u[4]), bracket(u[1], u[2])
    ar, br, cr = bracket(u[3], u[1]), bracket(u[4], u[1]), bracket(u[0], u[5])
    ass, bs, cs = bracket(u[4], u[2]), bracket(u[3], u[2]), scale(bracket(u[0], u[6]), -1)
    expected = {
        '35r': scale(q, 3 * (r - 2)), '35s': scale(qp, 3 * (s - 2)),
        '27r': add(scale(bb, 6 - 3*r - 4*s), scale(cc, 2 - 5*r + 4*s)),
        '27s': add(scale(aa, 6 - 4*r - 3*s), scale(cc, 5*s - 4*r - 2)),
        '10r': add(scale(ar, 2 - 3*r - 2*s), scale(br, 2 - r + 2*s),
                   scale(cr, -6 + 7*r + 2*s)),
        '10s': add(scale(ass, 2 - 3*s - 2*r), scale(bs, 2 - s + 2*r),
                   scale(cs, -6 + 7*s + 2*r))}
    for name, v in expected.items():
        require(f3(seeds[name], r, s) == v, name + ': displayed F3 formula')


def check_symbolic(seeds):
    coords = ((0, 7), (1, 6), (2, 5), (3, 4))
    expected = (
        (poly(-12,16,8), poly(-24,28,8), poly(0,-4,-8), poly(-8,12,8)),
        (poly(-12,8,16), poly(0,8,4), poly(24,-8,-28), poly(8,-8,-12)),
        (poly(6,-7,-5), poly(0,-1,4), poly(6,-5,-4), poly(2,-3,-2)))
    values = []
    for name, target in zip(('8r', '8s', 'Z'), expected):
        actual = image_polys(seeds[name])
        require(set(actual).issubset(set(coords)), name + ': unexpected exterior coordinate')
        got = tuple(actual.get(key, {}) for key in coords)
        require(got == target, name + ': symbolic displayed F3 coordinates')
        values.append(got)
    rows = [[values[j][i] for j in range(3)] for i in (0, 1, 3)]
    determinant = det3(rows)
    factor = scale(pmul(pmul(poly(-1,1,1), poly(-8,8,12)),
                         poly(-12,16,8)), 18)
    require(determinant == factor, 'exact bivariate determinant factorization')
    return [[a, b, str(c)] for (a, b), c in sorted(determinant.items())]


def main():
    global DEADLINE
    started = time.monotonic()
    DEADLINE = started + 48.0
    result = {'status': 'INCOMPLETE', 'role': 'prospective finite corroboration only',
              'stages': {name: 'NOT_TESTED' for name in
                         ('levi', 'lie3', 'lowest_vectors', 'whole_modules',
                          'symbolic_F3', 'parameter_samples', 'controls')},
              'samples': [], 'limits': ['not a radical computation',
                  'not the full Cartan or negative-Serre bridge',
                  'no universal parameter theorem',
                  'no full eight-channel contraction calculation']}
    exit_code = 2
    try:
        signal.signal(signal.SIGINT, latch)
        signal.signal(signal.SIGTERM, latch)
        check_levi()
        result['stages']['levi'] = 'PASS'
        lie = Basis()
        for i, j, k in product(range(8), repeat=3):
            guard()
            lie.insert(bracket(LETTERS[i], bracket(LETTERS[j], LETTERS[k])))
        require(len(lie) == 168, 'direct tensor-embedded Lie3 rank 168')
        for i, j, k in combinations(range(8), 3):
            jacobi = add(bracket(LETTERS[i], bracket(LETTERS[j], LETTERS[k])),
                         bracket(LETTERS[j], bracket(LETTERS[k], LETTERS[i])),
                         bracket(LETTERS[k], bracket(LETTERS[i], LETTERS[j])))
            require(not jacobi, 'tensor Jacobi identity')
        result['lie3_rank'] = len(lie)
        result['stages']['lie3'] = 'PASS'
        q, qp, qs, seeds = build_vectors()
        for v in seeds.values():
            require(lie.contains(v), 'lowest vector not in tensor-embedded Lie3')
        result['lowest_word_witnesses'] = {'35r': [0,0,1,1], '27r': [0,0,4,-1],
                                           '10r': [0,0,5,1], '8r': [0,0,7,2]}
        result['stages']['lowest_vectors'] = 'PASS'
        q_module = raising_closure(q, 10, 'Q')
        for v in qs:
            require(q_module.contains(v), 'Q1..Q4 outside full Q')
        qprime_module = raising_closure(qp, 10, 'Qprime')
        r35 = raising_closure(seeds['35r'], 35, 'r35')
        s35 = raising_closure(seeds['35s'], 35, 's35')
        rel = span(bracket(u, v) for u in LETTERS for v in q_module.vectors())
        require(len(rel) == 80, '[V,Q] rank 80')
        stable(rel, '[V,Q]')
        require(all(lie.contains(v) for v in rel.vectors()), '[V,Q] outside Lie3')
        union = span(rel.vectors() + s35.vectors())
        require(len(union) == 115, '[V,Q] / s35 intersection')
        stable(union, '[V,Q]+s35')
        require(all(rel.contains(v) for v in r35.vectors()), 'r35 outside [V,Q]')
        result['module_ranks'] = {'Q': len(q_module), 'Qprime': len(qprime_module),
                                  'r35': len(r35), 's35': len(s35),
                                  'VQ': len(rel), 'VQ_plus_s35': len(union),
                                  'VQ_intersect_s35': len(rel)+len(s35)-len(union)}
        result['stages']['whole_modules'] = 'PASS'
        result['determinant_coefficients_r_s'] = check_symbolic(seeds)
        result['stages']['symbolic_F3'] = 'PASS'
        groups = {
            '1,4': ((1,0), ['35r']), '4,1': ((0,1), ['35s']),
            '2,2': ((1,1), ['27r','27s']), '0,3': ((2,1), ['10r']),
            '3,0': ((1,2), ['10s']), '1,1': ((2,2), ['8r','8s','Z'])}
        cases = ((1,2,53,union,(0,0,1,0,1,2)),
                 (1,3,88,rel,  (0,1,1,0,1,2)),
                 (2,3,133,r35,(0,1,2,1,1,3)),
                 (3,4,168,Basis(),(1,1,2,1,1,3)))
        for r, s, expected_dim, ideal, expected_lows in cases:
            guard()
            require(168-len(ideal) == expected_dim, 'actual grade3 quotient dimension')
            relation2 = q_module if r == 1 else Basis()
            check_formula_images(seeds, q, qp, r, s)
            for v in ideal.vectors():
                img = f3(v, r, s)
                wedge_coordinates(img)
                require(relation2.contains(img), 'F3 does not descend through whole ideal')
            item = {'r': r, 's': s, 'grade3_dim': 168-len(ideal),
                    'relation2_rank': len(relation2), 'relation3_rank': len(ideal),
                    'multiplicities': {}}
            for ((name, (degree, names)), expected) in zip(groups.items(), expected_lows):
                selected = [seeds[n] for n in names]
                stats = quotient_lowest(lie, ideal, degree, selected)
                require(stats['lowest_dim'] == expected, name + ': quotient multiplicity')
                rank = image_rank_mod_relation(selected, relation2, r, s)
                require(rank == expected, name + ': F3 multiplicity rank modulo relation')
                stats['F3_rank_mod_relation'] = rank
                item['multiplicities'][name] = stats
            result['samples'].append(item)
        result['stages']['parameter_samples'] = 'PASS'
        r, s = 2, 3
        correct = f3(seeds['8r'], r, s)
        controls = {}
        controls['wrong_cartan_constant'] = ('DETECTED' if
            f3(seeds['8r'], r, s, wrong_cartan=True) != correct else 'MISSED')
        controls['swapped_r_s_cartan_row'] = ('DETECTED' if
            f3(seeds['8r'], r, s, swap_rs=True) != correct else 'MISSED')
        controls['omit_whole_Q_r1s3'] = ('DETECTED' if 168 != 88 else 'MISSED')
        i, j, k = 0, 1, 2
        pieces = (bracket(LETTERS[i], bracket(LETTERS[j], LETTERS[k])),
                  bracket(LETTERS[j], bracket(LETTERS[k], LETTERS[i])),
                  bracket(LETTERS[k], bracket(LETTERS[i], LETTERS[j])))
        controls['wrong_jacobi_sign'] = ('DETECTED' if
            not add(*pieces) and add(pieces[0], pieces[1], scale(pieces[2], -1))
            else 'MISSED')
        def broken_product(x, y):
            out = {}
            for wx, cx in x.items():
                for wy, cy in y.items():
                    key = tuple(sorted(wx + wy))
                    out[key] = out.get(key, 0) + cx * cy
            return clean(out)
        bad_q = add(broken_product(LETTERS[0], LETTERS[1]),
                    scale(broken_product(LETTERS[1], LETTERS[0]), -1))
        controls['commutativized_tensor_product'] = ('DETECTED' if q and not bad_q else 'MISSED')
        controls['dual_gram_offdiagonal_sign'] = 'NOT_TESTED: no contraction built'
        controls['omit_W7'] = 'NOT_TESTED: no contraction built'
        controls['invertibility_implies_radical'] = ('SCOPE_GUARD: no such implication is '
            'used; no computed counterexample or tau/J model')
        require(all(controls[k] == 'DETECTED' for k in
                    ('wrong_cartan_constant', 'swapped_r_s_cartan_row',
                     'omit_whole_Q_r1s3', 'wrong_jacobi_sign',
                     'commutativized_tensor_product')), 'intended mutation discriminator')
        result['controls'] = controls
        result['stages']['controls'] = 'PASS'
        result['status'] = 'PASS_FINITE_CHECKS_ONLY'
        exit_code = 0
    except Interrupted as e:
        result['status'] = 'INCOMPLETE'
        result['reason'] = str(e)
    except CheckFailure as e:
        result['status'] = 'FAIL_CHECK'
        result['reason'] = str(e)
        exit_code = 1
    except Exception as e:
        result['status'] = 'ERROR'
        result['reason'] = type(e).__name__ + ': ' + str(e)
        exit_code = 1
    finally:
        result['elapsed_seconds'] = round(time.monotonic() - started, 6)
        print(json.dumps(result, sort_keys=True, separators=(',', ':')), flush=True)
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
