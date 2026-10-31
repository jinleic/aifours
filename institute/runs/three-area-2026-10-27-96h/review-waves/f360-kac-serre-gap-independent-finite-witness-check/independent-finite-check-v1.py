#!/usr/bin/env python3
"""Independent exact finite (r,s,a,b,n)=(5,6,1,1,8) checker.

NOT RUN by the authoring review role. Run: python3 -B FILE --seconds 55
Standard library only; no file/network/subprocess access or dependencies.
All scientific arithmetic is integer/Fraction. Runtime measurement is metadata.
The identification with the actual Chevalley quotient remains conditional on
f360 packet S2 (full Cartan, free source, and J/K=P_+ direct-sum P_-).
No uniform theorem, B8, whole-level-eight, all-level, or novelty claim.
"""
from argparse import ArgumentParser
from collections import deque
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt
from time import monotonic
import sys

R, S, NMAX = 5, 6, 9
A = ((2, -1, -1), (-1, 2, -1), (-R, -S, 2))
BOUNDS = (1, 1, NMAX)
START, LIMIT = None, 55


class CheckError(Exception):
    pass


class Deadline(Exception):
    pass


def tick():
    if START is not None and monotonic() - START >= LIMIT:
        raise Deadline()


def need(condition, reason):
    if not condition:
        raise CheckError(reason)


def plus(p, q, c=1):
    out = dict(p)
    for word, value in q.items():
        value = out.get(word, 0) + c * value
        if value:
            out[word] = Q(value)
        else:
            out.pop(word, None)
    return out


def times(p, c):
    return {word: Q(c * value) for word, value in p.items() if c * value}


def tensor(p, q):
    tick()
    out = {}
    for u, a in p.items():
        for v, b in q.items():
            w = u + v
            out[w] = out.get(w, Q(0)) + a * b
    return {w: a for w, a in out.items() if a}


def bracket(p, q):
    return plus(tensor(p, q), tensor(q, p), -1)


def letter(i):
    return {(i,): Q(1)}


def ad_power(t, p, exponent):
    for _ in range(exponent):
        p = bracket(t, p)
    return p


class Space:
    """Sparse exact echelon rows plus unchanged independent input vectors."""
    def __init__(self):
        self.rows = {}
        self.vectors = []
        self.tags = []

    def remainder(self, p):
        p = dict(p)
        while p:
            tick()
            pivot = min(p)
            if pivot not in self.rows:
                break
            p = plus(p, self.rows[pivot], -p[pivot])
        return p

    def contains(self, p):
        return not self.remainder(p)

    def add(self, p, tag=None):
        rem = self.remainder(p)
        if not rem:
            return False
        pivot = min(rem)
        self.rows[pivot] = times(rem, 1 / rem[pivot])
        self.vectors.append(dict(p))
        self.tags.append(tag)
        return True

    def __len__(self):
        return len(self.vectors)


def coords(p, columns):
    """Solve in independent original columns, not merely reduced-row labels."""
    rows = {}
    count = len(columns)
    for j, column in enumerate(columns):
        rem, rep = dict(column), [Q(0)] * count
        rep[j] = Q(1)
        while rem:
            tick()
            pivot = min(rem)
            if pivot not in rows:
                a = rem[pivot]
                rows[pivot] = (times(rem, 1 / a), [v / a for v in rep])
                break
            row, rowrep = rows[pivot]
            a = rem[pivot]
            rem = plus(rem, row, -a)
            rep = [v - a * w for v, w in zip(rep, rowrep)]
        need(bool(rem), 'DEPENDENT-COORDINATE-COLUMNS')
    rem, answer = dict(p), [Q(0)] * count
    while rem:
        tick()
        pivot = min(rem)
        need(pivot in rows, 'VECTOR-OUTSIDE-CONSTRUCTED-SPAN')
        row, rep = rows[pivot]
        a = rem[pivot]
        rem = plus(rem, row, -a)
        answer = [v + a * w for v, w in zip(answer, rep)]
    return answer


def gadd(g, h):
    return tuple(a + b for a, b in zip(g, h))


def gsub(g, h):
    return tuple(a - b for a, b in zip(g, h))


def inside(g):
    return all(0 <= a <= b for a, b in zip(g, BOUNDS)) and any(g)


def all_grades():
    return sorted(((a, b, n) for a in range(2) for b in range(2)
                   for n in range(NMAX + 1) if a or b or n),
                  key=lambda g: (sum(g), g))


def free_lie(letter_grades):
    """Span ALL binary Lie brackets in the box, using tensor commutators.

    No dimension or quotient basis is an input. Retained expression trees
    allow a separate map into the imported eight-letter source.
    """
    done = {}
    for g in all_grades():
        tick()
        space = Space()
        for i, degree in enumerate(letter_grades):
            if degree == g:
                space.add(letter(i), ('g', i))
        for h, left in done.items():
            k = gsub(g, h)
            if k not in done or h > k:
                continue
            right = done[k]
            for i, (p, pt) in enumerate(zip(left.vectors, left.tags)):
                for j, (q, qt) in enumerate(zip(right.vectors, right.tags)):
                    if h == k and i >= j:
                        continue
                    space.add(bracket(p, q), ('b', pt, qt))
        done[g] = space
    return done


X, Y, T = letter(0), letter(1), letter(2)
RAW_GRADES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
V_GRADES = ((0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1),
            (1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 2, 1))


def lower(p, node, wrong_f=False):
    """Normal-order [f_node,p] = positive_part + right_h_part * h_node.

    For each occurrence e_node replace [f_node,e_node] by -h_node;
    commute h_node through its suffix with the FIXED Cartan row.
    wrong_f changes only the implemented f3 coefficient, not the actual A.
    """
    weights = list(A[node])
    if wrong_f and node == 2:
        weights[0] += 1  # gives i*(r-i), rather than i*(r-i+1), on X_i
    positive, right_h = {}, {}
    for word, c in p.items():
        for j, symbol in enumerate(word):
            if symbol != node:
                continue
            removed = word[:j] + word[j + 1:]
            suffix_weight = sum(weights[k] for k in word[j + 1:])
            right_h = plus(right_h, {removed: c}, -1)
            positive = plus(positive, {removed: c}, -suffix_weight)
    return positive, right_h


def raw_ideal(seeds):
    """Entire Lie ideal in the graded box: close under all generators.

    Jacobi makes closure under ad(e1), ad(e2), ad(e3) closure under every
    positive Lie word. All degrees are nonnegative, so pruning is exact.
    """
    ideals, queue = {}, deque()

    def insert(g, p):
        if inside(g) and ideals.setdefault(g, Space()).add(p):
            queue.append((g, p))

    for g, p in seeds:
        insert(g, p)
    while queue:
        tick()
        g, p = queue.popleft()
        for i, degree in enumerate(RAW_GRADES):
            h = gadd(g, degree)
            if inside(h):
                insert(h, bracket(letter(i), p))
    return ideals


def at(spaces, g):
    return spaces.get(g, Space())


# Ordinary 3x3 Levi module labels ONLY, never replacements for Lie tensors.
def matrix_unit(i, j):
    return tuple(tuple(Q(int((a, b) == (i, j))) for b in range(3))
                 for a in range(3))


ZERO = tuple((Q(0),) * 3 for _ in range(3))
L1, L2 = matrix_unit(0, 1), matrix_unit(1, 2)


def madd(a, b, c=1):
    return tuple(tuple(a[i][j] + c * b[i][j] for j in range(3))
                 for i in range(3))


def mscale(a, c):
    return tuple(tuple(c * v for v in row) for row in a)


def mmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def mbr(a, b):
    return madd(mmul(a, b), mmul(b, a), -1)


def mpoly(a):
    return {(i, j): a[i][j] for i in range(3) for j in range(3) if a[i][j]}


U0 = matrix_unit(2, 0)
U1, U2 = mbr(L1, U0), mbr(L2, U0)
U3, U4 = mbr(L1, U2), mbr(L2, U1)
U5 = mscale(mbr(L1, U3), Q(-1, 2))
U6 = mscale(mbr(L2, U4), Q(1, 2))
U7 = mbr(L1, U6)
U = (U0, U1, U2, U3, U4, U5, U6, U7)
U_COLUMNS = [mpoly(a) for a in U]


@lru_cache(maxsize=None)
def action_table(a):
    return tuple(tuple(coords(mpoly(mbr(a, u)), U_COLUMNS)) for u in U)


def levi_action(a, p):
    if a == ZERO or not p:
        return {}
    table, out = action_table(a), {}
    for word, c in p.items():
        for j, symbol in enumerate(word):
            for replacement, d in enumerate(table[symbol]):
                if d:
                    out = plus(out, {word[:j] + (replacement,) + word[j+1:]: c*d})
    return out


@lru_cache(maxsize=None)
def map_tree(tree):
    if tree[0] == 'g':
        i = tree[1]
        if i == 0:
            return L1, {}
        if i == 1:
            return L2, {}
        return ZERO, letter(0)
    a, p = map_tree(tree[1])
    b, q = map_tree(tree[2])
    out = plus(bracket(p, q), levi_action(a, q))
    return mbr(a, b), plus(out, levi_action(b, p), -1)


def seed_tree(symbol, exponent):
    tree = ('g', symbol)
    for _ in range(exponent):
        tree = ('b', ('g', 2), tree)
    return tree


def v_ideal(seeds):
    """Both full cyclic Levi modules, then their whole free-Lie ideal.

    Seeds are lowest vectors (checked below). PBW reordering of finite-Levi
    operators therefore reduces their complete modules to positive raisings.
    Include ALL eight outer letters, not only u0 or unmixed seed chains.
    """
    ideals, queue = {}, deque()

    def insert(g, p):
        if inside(g) and ideals.setdefault(g, Space()).add(p):
            queue.append((g, p))

    for g, p in seeds:
        insert(g, p)
    while queue:
        tick()
        g, p = queue.popleft()
        for a, degree in ((L1, (1, 0, 0)), (L2, (0, 1, 0))):
            h = gadd(g, degree)
            if inside(h):
                insert(h, levi_action(a, p))
        for i, degree in enumerate(V_GRADES):
            h = gadd(g, degree)
            if inside(h):
                insert(h, bracket(letter(i), p))
    return ideals


def verify_source(raw, vfree):
    mapped = {}
    for g in all_grades():
        if g[2] == 0:
            continue
        image = Space()
        for tree in raw[g].tags:
            a, p = map_tree(tree)
            need(a == ZERO, 'SOURCE-MAP-LEVI-LEAK')
            need(vfree[g].contains(p), 'SOURCE-MAP-OUTSIDE-FREE-LIE')
            image.add(p)
        need(len(image) == len(raw[g]) == len(vfree[g]), 'SOURCE-MAP-NOT-ISOMORPHISM')
        mapped[g] = image
    return mapped


def verify_ideal_interfaces(raw, raw_i, v_i):
    for g in all_grades():
        if g[2] == 0:
            continue
        columns = raw[g].vectors
        images = [map_tree(t)[1] for t in raw[g].tags]
        mapped = Space()
        for p in at(raw_i, g).vectors:
            coefficients = coords(p, columns)
            image = {}
            for c, q in zip(coefficients, images):
                image = plus(image, q, c)
            need(at(v_i, g).contains(image), 'RAW-IDEAL-NOT-IN-V-IDEAL')
            mapped.add(image)
        need(len(mapped) == len(at(raw_i, g)) == len(at(v_i, g)),
             'WHOLE-IDEAL-INTERFACE-RANK')
        for p in at(v_i, g).vectors:
            need(mapped.contains(p), 'V-IDEAL-NOT-IN-RAW-IDEAL')


def verify_lowering_stability(ideals):
    for g, space in ideals.items():
        for p in space.vectors:
            for node in range(3):
                target = list(g)
                target[node] -= 1
                positive, right_h = lower(p, node)
                need(not right_h, 'IDEAL-LOWERING-CARTAN-LEAK')
                need(at(ideals, tuple(target)).contains(positive), 'IDEAL-NOT-LOWERING-STABLE')


def zword(i, j):
    return bracket(ad_power(T, X, i), ad_power(T, Y, j))


def quotient_basis(raw, ideals, n):
    """Discover survivors; never insert the supplied four-element basis."""
    g = (1, 1, n)
    free, whole = raw[g], at(ideals, g)
    span = Space()
    for p in whole.vectors:
        need(free.contains(p), 'IDEAL-OUTSIDE-SOURCE')
        span.add(p)
    basis, labels = [], []
    for i in range(n + 1):
        p = zword(i, n - i)
        need(free.contains(p), 'Z-OUTSIDE-SOURCE')
        if span.add(p):
            basis.append(p)
            labels.append((i, n - i))
    need(len(span) == len(free), 'Z-FAMILY-DOES-NOT-EXHAUST-SOURCE')
    need(len(basis) == len(free) - len(whole), 'QUOTIENT-RANK')
    return basis, labels


def identity(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def multiply(a, b):
    need(bool(a) and bool(b) and len(a[0]) == len(b), 'MATRIX-SHAPE')
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def columns_to_matrix(columns, nrows):
    return [[column[i] for column in columns] for i in range(nrows)]


def inverse(a):
    n = len(a)
    right = identity(n)
    rows = [[Q(v) for v in a[i]] + right[i] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        need(pivot is not None, 'SINGULAR-GRAM')
        rows[j], rows[pivot] = rows[pivot], rows[j]
        c = rows[j][j]
        rows[j] = [v / c for v in rows[j]]
        for i in range(n):
            if i != j:
                c = rows[i][j]
                rows[i] = [v - c*w for v, w in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def charpoly(a):
    # Faddeev-LeVerrier: no claimed eigenvalue formula is an input.
    n, b, coefficients = len(a), identity(len(a)), [Q(1)]
    for k in range(1, n + 1):
        b = multiply(a, b)
        c = -sum(b[i][i] for i in range(n)) / k
        coefficients.append(c)
        for i in range(n):
            b[i][i] += c
    need(all(not v for row in b for v in row), 'CAYLEY-HAMILTON')
    return coefficients


def evaluate(poly, x):
    value = Q(0)
    for c in poly:
        value = value * x + c
    return value


def integer_factor_roots(poly):
    need(poly[0] == 1 and all(c.denominator == 1 for c in poly), 'NONINTEGRAL-CHARPOLY')
    roots, remainder = [], list(poly)
    while len(remainder) > 1:
        tick()
        constant = abs(remainder[-1].numerator)
        if constant == 0:
            candidates = [0]
        else:
            divisors = set()
            for d in range(1, isqrt(constant) + 1):
                if constant % d == 0:
                    divisors.update((d, constant // d))
            candidates = sorted(divisors | {-d for d in divisors})
        root = next((r for r in candidates if evaluate(remainder, r) == 0), None)
        need(root is not None, 'UNFACTORED-CHARPOLY')
        quotient = [remainder[0]]
        for c in remainder[1:-1]:
            quotient.append(c + root * quotient[-1])
        need(remainder[-1] + root * quotient[-1] == 0, 'SYNTHETIC-DIVISION')
        roots.append(root)
        remainder = quotient
    return sorted(roots)


def reject_intended(name, reason, operation):
    try:
        operation()
    except CheckError as error:
        need(str(error) == reason, 'UNINTENDED-MUTATION-FAILURE:' + name + ':' + str(error))
        print('control', name, 'REJECTED:', reason)
    else:
        raise CheckError('MUTATION-ESCAPED:' + name)


def show_matrix(name, a):
    print(name)
    for row in a:
        print('  ' + ' '.join(str(v) for v in row))


def run():
    raw, vfree = free_lie(RAW_GRADES), free_lie(V_GRADES)
    verify_source(raw, vfree)
    gx, gy = (1, 0, R + 1), (0, 1, S + 1)
    qx, qy = ad_power(T, X, R + 1), ad_power(T, Y, S + 1)
    for seed in (qx, qy):
        for node in range(3):
            positive, right_h = lower(seed, node)
            need(not positive and not right_h, 'SEED-NOT-LOWEST-OR-NOT-SERRE')
    ax, vqx = map_tree(seed_tree(0, R + 1))
    ay, vqy = map_tree(seed_tree(1, S + 1))
    need(ax == ay == ZERO, 'SEED-MAP-LEVI-LEAK')
    need(vqx == times(ad_power(letter(0), letter(1), R), -1), 'FIRST-SEED-INTERFACE')
    need(vqy == times(ad_power(letter(0), letter(2), S), -1), 'SECOND-SEED-INTERFACE')
    seeds = [(gx, qx), (gy, qy)]
    whole = raw_ideal(seeds)
    first, second = raw_ideal(seeds[:1]), raw_ideal(seeds[1:])
    vi = v_ideal([(gx, vqx), (gy, vqy)])
    verify_ideal_interfaces(raw, whole, vi)
    verify_lowering_stability(whole)
    g = (1, 1, 8)
    print('source dimensions:', len(raw[g]), len(vfree[g]))
    print('ideal ranks first, second, union, intersection:',
          len(at(first, g)), len(at(second, g)), len(at(whole, g)),
          len(at(first, g)) + len(at(second, g)) - len(at(whole, g)))
    b7, labels7 = quotient_basis(raw, whole, 7)
    b8, labels8 = quotient_basis(raw, whole, 8)
    i7, i8 = at(whole, (1, 1, 7)).vectors, at(whole, g).vectors
    print('discovered quotient labels at 7:', labels7)
    print('discovered quotient labels at 8:', labels8)
    print('quotient dimension at 8:', len(b8))
    fcolumns = []
    for p in b8:
        positive, right_h = lower(p, 2)
        need(not right_h, 'F-CARTAN-LEAK')
        fcolumns.append(coords(positive, i7 + b7)[len(i7):])
    ecolumns = [coords(bracket(T, p), i8 + b8)[len(i8):] for p in b7]
    fmatrix = columns_to_matrix(fcolumns, len(b7))
    ematrix = columns_to_matrix(ecolumns, len(b8))
    ef = multiply(ematrix, fmatrix)
    # Independent direct composite and [E,F]=H on the actual degree-eight quotient.
    direct, commutator = [], []
    for p in b8:
        fp, fh = lower(p, 2)
        ep = bracket(T, p)
        fep, feh = lower(ep, 2)
        need(not fh and not feh, 'COMPOSITE-CARTAN-LEAK')
        efp = bracket(T, fp)
        direct.append(coords(efp, i8 + b8)[len(i8):])
        commutator.append(coords(plus(efp, fep, -1), i8 + b8)[len(i8):])
    need(ef == columns_to_matrix(direct, len(b8)), 'EF-COMPOSITION')
    hweight = 2 * 8 - R - S
    need(columns_to_matrix(commutator, len(b8)) ==
         [[hweight * v for v in row] for row in identity(len(b8))], 'EF-COMMUTATOR')
    show_matrix('F: degree8 -> degree7', fmatrix)
    show_matrix('E: degree7 -> degree8', ematrix)
    show_matrix('EF on discovered degree8 quotient basis', ef)
    poly = charpoly(ef)
    roots = integer_factor_roots(poly)
    print('characteristic polynomial coefficients, descending:', [str(c) for c in poly])
    print('discovered exact spectrum:', roots)
    need(len(b8) == 4 and roots == [5, 12, 21, 32], 'CLAIMED-FINITE-EXAMPLE-DOES-NOT-MATCH')
    gram = [[sum(U[i][a][b] * U[j][a][b] for a in range(3) for b in range(3))
             for j in range(8)] for i in range(8)]
    gram_inv = inverse(gram)
    need(multiply(gram, gram_inv) == identity(8), 'GRAM-COEVALUATION')
    need(all((i == 0 and gram_inv[0][i] == 1) or
             (i != 0 and gram_inv[0][i] == 0) for i in range(8)), 'ZERO-CHARGE-NORMALIZATION')
    for j, charge in enumerate(V_GRADES):
        if j == 0:
            continue
        target = (1 - charge[0], 1 - charge[1], 7)
        if min(target) < 0:
            # Nonnegative letter charges in imported L(V): no source at this degree.
            print('W', j, 'target', target, 'absent from nonnegative source support')
        else:
            dim = len(at(raw, target)) - len(at(whole, target))
            need(dim == 0, 'SURVIVING-NONZERO-CHARGE-LOWERING-TARGET')
            print('W', j, 'target', target, 'source/ideal/quotient:',
                  len(at(raw, target)), len(at(whole, target)), dim)
    show_matrix('Gram from independently derived Levi labels', gram)
    print('actual contraction multiplier:', gram_inv[0][0])

    def mandatory(ideals, grade, seed, reason):
        need(at(ideals, grade).contains(seed), reason)

    mandatory(whole, gx, qx, 'MISSING-FIRST-SEED')
    mandatory(whole, gy, qy, 'MISSING-SECOND-SEED')
    reject_intended('omit-second-seed', 'OMITTED-Y-SEED',
                    lambda: mandatory(first, gy, qy, 'OMITTED-Y-SEED'))
    late_seed = ad_power(T, X, R + 2)
    shifted = raw_ideal([((1, 0, R + 2), late_seed), (gy, qy)])
    reject_intended('shift-first-truncation-late', 'SHIFTED-X-TRUNCATION',
                    lambda: mandatory(shifted, gx, qx, 'SHIFTED-X-TRUNCATION'))
    print('mutated degree8 dimensions omitted/shifted:',
          len(raw[g]) - len(at(first, g)), len(raw[g]) - len(at(shifted, g)))

    def f_normalization(wrong):
        p, right_h = lower(bracket(T, X), 2, wrong_f=wrong)
        need(not right_h and p == times(X, R), 'F-COEFFICIENT')

    f_normalization(False)
    reject_intended('wrong-F-coefficient', 'F-COEFFICIENT', lambda: f_normalization(True))
    bad_inverse = [row[:] for row in gram_inv]
    bad_inverse[0][0] *= 2
    reject_intended('double-Gram-multiplier', 'GRAM-COEVALUATION',
                    lambda: need(multiply(gram, bad_inverse) == identity(8), 'GRAM-COEVALUATION'))
    print('PASS: conditional finite actual-quotient component only; all four controls rejected as intended.')
    print('No uniform theorem, B8=0, whole-level-eight, all-level, formal, independent-family, or novelty certification.')


def main():
    global START, LIMIT
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=int, default=55)
    args = parser.parse_args()
    if not 1 <= args.seconds <= 60:
        parser.error('--seconds must be an integer from 1 to 60')
    LIMIT, START = args.seconds, monotonic()
    try:
        run()
    except Deadline:
        print('INCOMPLETE: cooperative time bound reached; no PASS.', file=sys.stderr)
        return 2
    except CheckError as error:
        print('FAIL:', error, file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
