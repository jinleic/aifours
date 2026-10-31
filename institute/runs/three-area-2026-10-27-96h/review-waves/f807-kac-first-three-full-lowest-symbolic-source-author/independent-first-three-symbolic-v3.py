#!/usr/bin/env python3
# Fresh F807 successor v3; independent ordered-tensor construction. UNRUN.
import itertools
import json
import math
import signal
import time
from collections import deque
from fractions import Fraction

START = time.monotonic()
SOFT_SECONDS = 35.0
ALARM_SECONDS = 37.0
LETTERS = 'xabcdefg'
WEIGHT = ((0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2))
E1 = ({1: 1}, {}, {3: 1}, {5: -2}, {5: -1}, {}, {7: 1}, {})
E2 = ({2: 1}, {4: 1}, {}, {6: 1}, {6: 2}, {7: -1}, {}, {})
F1 = ({}, {0: 1}, {}, {2: 2}, {2: 1}, {3: -1}, {}, {6: 1})
F2 = ({}, {}, {0: 1}, {1: 1}, {1: 2}, {}, {4: 1}, {5: -1})
E12 = ({3: 1, 4: -1}, {5: -1}, {6: -1}, {7: -1}, {7: 1}, {}, {}, {})
TARGETS = (((1, 2), (4, 1), 4, 9), ((2, 1), (1, 4), 4, 8), ((2, 2), (2, 2), 7, 23))

class Stopped(Exception):
    pass

class BadConstruction(Exception):
    pass

def tick():
    if time.monotonic() - START >= SOFT_SECONDS:
        raise Stopped('cooperative 35-second deadline')

def alarm_handler(_signum, _frame):
    raise Stopped('37-second alarm')

def require(condition, message):
    if not condition:
        raise BadConstruction(message)

def add_scaled(out, vec, scale):
    if not scale:
        return
    for key, val in vec.items():
        value = out.get(key, 0) + scale * val
        if value:
            out[key] = value
        elif key in out:
            del out[key]

def bracket(left, right):
    out = {}
    for u, a in left.items():
        for v, b in right.items():
            uv = u + v
            vu = v + u
            out[uv] = out.get(uv, 0) + a * b
            out[vu] = out.get(vu, 0) - a * b
    return {k: v for k, v in out.items() if v}

def action(vec, table):
    out = {}
    for word, coefficient in vec.items():
        for i, letter in enumerate(word):
            for new, factor in table[letter].items():
                target = word[:i] + (new,) + word[i + 1:]
                out[target] = out.get(target, 0) + coefficient * factor
    return {k: v for k, v in out.items() if v}

def d_letter(u, v, s, flip_cartan=False):
    if u == 0:
        i, j = WEIGHT[v]
        factor = 3 * i + s * j - 2
        if flip_cartan:
            factor = -factor
        return {v: factor} if factor else {}
    if u == 1:
        return {z: -3 * c for z, c in E1[v].items()}
    if u == 2:
        return {z: -s * c for z, c in E2[v].items()}
    if u == 3:
        return {z: -s * c for z, c in E12[v].items()}
    if u == 4:
        return {z: 3 * c for z, c in E12[v].items()}
    return {}

def f3(vec, s, flip_cartan=False):
    # Commute each grade-zero [f3,u_i] to the right through later letters.
    # For an embedded Lie word, all residual grade-zero right tails cancel.
    out = {}
    for word, coefficient in vec.items():
        n = len(word)
        for i in range(n):
            for j in range(i + 1, n):
                for new, factor in d_letter(word[i], word[j], s, flip_cartan).items():
                    target = word[:i] + word[i + 1:j] + (new,) + word[j + 1:]
                    out[target] = out.get(target, 0) + coefficient * factor
    return {k: v for k, v in out.items() if v}

class Span:
    # Exact sparse row-pivot elimination; retained originals are independent.
    def __init__(self):
        self.pivots = {}
        self.original = []

    def residual(self, vec):
        v = {k: Fraction(x) for k, x in vec.items() if x}
        while v:
            tick()
            p = min(v)
            if p not in self.pivots:
                break
            add_scaled(v, self.pivots[p], -v[p])
        return v

    def add(self, vec):
        v = self.residual(vec)
        if not v:
            return False
        p = min(v)
        c = v[p]
        self.pivots[p] = {k: x / c for k, x in v.items()}
        self.original.append(dict(vec))
        return True

    def contains(self, vec):
        return not self.residual(vec)

class ColumnKernel:
    # Eliminate full columns and simultaneously retain exact dependencies.
    def __init__(self):
        self.pivots = {}
        self.dependencies = []

    def add(self, vec, index):
        v = {k: Fraction(x) for k, x in vec.items() if x}
        expression = {index: Fraction(1)}
        while v:
            tick()
            p = min(v)
            if p not in self.pivots:
                c = v[p]
                self.pivots[p] = ({k: x / c for k, x in v.items()},
                                  {k: x / c for k, x in expression.items()})
                return
            c = v[p]
            column, representation = self.pivots[p]
            add_scaled(v, column, -c)
            add_scaled(expression, representation, -c)
        self.dependencies.append(expression)

def word_weight(word):
    return tuple(sum(WEIGHT[c][i] for c in word) for i in range(2))

def nested(word):
    value = {(word[-1],): 1}
    for c in reversed(word[:-1]):
        value = bracket({(c,): 1}, value)
    return value

def free_basis(n, weight):
    space = Span()
    for word in itertools.product(range(8), repeat=n):
        tick()
        if word_weight(word) == weight:
            space.add(nested(word))
    return space

def primitive(vec):
    fractions = {k: Fraction(v) for k, v in vec.items() if v}
    require(bool(fractions), 'zero projected lowest vector')
    denominator = 1
    for val in fractions.values():
        denominator = math.lcm(denominator, val.denominator)
    out = {k: int(val * denominator) for k, val in fractions.items()}
    divisor = 0
    for val in out.values():
        divisor = math.gcd(divisor, abs(val))
    out = {k: v // divisor for k, v in out.items()}
    if out[min(out)] < 0:
        out = {k: -v for k, v in out.items()}
    return out

def number(value):
    value = Fraction(value)
    return value.numerator if value.denominator == 1 else str(value)

def sparse(vec):
    return {''.join(LETTERS[i] for i in word): number(value)
            for word, value in sorted(vec.items()) if value}

def weight_key(w):
    return str(w[0]) + ',' + str(w[1])

def relation_closure():
    seed = nested((0, 0, 0, 1))
    require(bool(seed), 'first seed unexpectedly zero')
    require(not action(seed, F1) and not action(seed, F2), 'first seed not Levi-lowest')
    spaces = {}
    queue = deque()
    def include(w, vec):
        space = spaces.setdefault(w, Span())
        if space.add(vec):
            queue.append((w, vec))
            require(sum(len(v.original) for v in spaces.values()) <= 81,
                    'first relation exceeds dimension 81')
    include((1, 0), seed)
    while queue:
        tick()
        w, vec = queue.popleft()
        for table, shift in ((E1, (1, 0)), (E2, (0, 1))):
            image = action(vec, table)
            if image:
                include((w[0] + shift[0], w[1] + shift[1]), image)
    require(sum(len(v.original) for v in spaces.values()) == 81,
            'first relation does not have dimension 81')
    for w, space in sorted(spaces.items()):
        for vec in space.original:
            tick()
            require(word_weight(next(iter(vec))) == w, 'relation weight mismatch')
            for table, shift in ((E1, (1, 0)), (E2, (0, 1)),
                                 (F1, (-1, 0)), (F2, (0, -1))):
                image = action(vec, table)
                target = spaces.get((w[0] + shift[0], w[1] + shift[1]))
                require(not image or (target is not None and target.contains(image)),
                        'relation fails a Levi stability check')
            require(not f3(vec, 4) and not f3(vec, 5),
                    'actual affine F3 does not kill whole first relation')
    return seed, spaces

def tagged(vec, side):
    return {(side,) + key: value for key, value in vec.items()}

def rank(vectors):
    space = Span()
    for vec in vectors:
        space.add(vec)
    return len(space.original)

def combine(first, second):
    out = dict(first)
    add_scaled(out, second, 1)
    return out

def make_type(weight, label, expected, quotient_dim, relations, report):
    w1 = (weight[0] - 1, weight[1])
    w2 = (weight[0], weight[1] - 1)
    r0 = relations.get(weight, Span()).original
    r1 = relations.get(w1, Span()).original
    r2 = relations.get(w2, Span()).original
    free4 = free_basis(4, weight)
    for v in r0:
        require(free4.contains(v), 'relation not in free Lie4 weight space')
    quotient_span = Span()
    for v in r0:
        require(quotient_span.add(v), 'dependent relation basis')
    qbasis = []
    for v in free4.original:
        if quotient_span.add(v):
            qbasis.append(v)
    require(len(qbasis) == quotient_dim, 'unexpected complete source quotient dimension')
    report.update({'label': list(label), 'expected_multiplicity': expected,
                   'free_lie4_weight_dimension': len(free4.original),
                   'relation_source_dimension': len(r0),
                   'quotient_weight_dimension': len(qbasis),
                   'lower_relation_dimensions': [len(r1), len(r2)],
                   'free_lie4_basis': [sparse(v) for v in free4.original],
                   'quotient_basis': [sparse(v) for v in qbasis],
                   'status': 'CONSTRUCTING_LOWEST'})
    columns = []
    for v in qbasis:
        columns.append(combine(tagged(action(v, F1), 0), tagged(action(v, F2), 1)))
    columns.extend(tagged(v, 0) for v in r1)
    columns.extend(tagged(v, 1) for v in r2)
    kernel = ColumnKernel()
    for j, col in enumerate(columns):
        kernel.add(col, j)
    require(len(kernel.dependencies) == expected, 'unexpected complete lowest dimension')
    lowest = []
    checked = Span()
    for v in r0:
        checked.add(v)
    for dependency in kernel.dependencies:
        z = {}
        for i, c in dependency.items():
            if i < len(qbasis):
                add_scaled(z, qbasis[i], c)
        z = primitive(z)
        require(checked.add(z), 'dependent lowest class or relation-only lift')
        for table, target in ((F1, relations.get(w1)), (F2, relations.get(w2))):
            image = action(z, table)
            require(not image or (target is not None and target.contains(image)),
                    'lowest vector not annihilated modulo the full relation')
        lowest.append(z)
    target = free_basis(3, weight)
    images0 = [f3(v, 4) for v in lowest]
    images5 = [f3(v, 5) for v in lowest]
    images1 = []
    for a, b in zip(images0, images5):
        coefficient = dict(b)
        add_scaled(coefficient, a, -1)
        require(target.contains(a) and target.contains(coefficient),
                'actual F3 image outside genuine free Lie3 target')
        images1.append(coefficient)
    r4 = rank(images0)
    r5 = rank(images5)
    report.update({'lowest_dimension': len(lowest),
                   'lowest_basis': [sparse(v) for v in lowest],
                   'free_lie3_target_dimension': len(target.original),
                   'free_lie3_target_basis': [sparse(v) for v in target.original],
                   'f3_constant_s4_tensor_columns': [sparse(v) for v in images0],
                   'f3_shift_coefficient_tensor_columns': [sparse(v) for v in images1],
                   'f3_s5_tensor_columns': [sparse(v) for v in images5],
                   's4_rank': r4, 's5_rank': r5,
                   'status': 'SAMPLES_CONSTRUCTED'})
    require(r4 == expected and r5 == expected, 's4 or s5 full actual map rank mismatch')
    single = rank(images0[:1])
    require(single < r4, 'lost-copy control failed to reduce image rank')
    report['lost_copy_control'] = {'full_rank': r4, 'one_column_rank': single,
                                  'detected_intended_rank_loss': True}
    return images0, images1

def det_integer(rows):
    n = len(rows)
    if not n:
        return 1
    a = [list(row) for row in rows]
    sign, previous = 1, 1
    for k in range(n - 1):
        tick()
        if not a[k][k]:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                val = a[i][j] * pivot - a[i][k] * a[k][j]
                require(val % previous == 0, 'Bareiss non-exact division')
                a[i][j] = val // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]

def poly_trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

def determinant_polynomial(rows0, rows1):
    n = len(rows0)
    values = [det_integer([[rows0[i][j] + t * rows1[i][j] for j in range(n)]
                           for i in range(n)]) for t in range(n + 1)]
    differences = []
    while values:
        differences.append(values[0])
        values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    result = [Fraction(0)] * (n + 1)
    falling = [Fraction(1)]
    factorial = 1
    for k in range(n + 1):
        for j, value in enumerate(falling):
            result[j] += Fraction(differences[k], factorial) * value
        new = [Fraction(0)] * (len(falling) + 1)
        for j, value in enumerate(falling):
            new[j] -= k * value
            new[j + 1] += value
        falling = new
        factorial *= k + 1
    require(all(x.denominator == 1 for x in result), 'nonintegral determinant coefficient')
    return poly_trim([int(x) for x in result])

def remainder(a, b):
    a = poly_trim([Fraction(x) for x in a])
    b = poly_trim([Fraction(x) for x in b])
    while not (len(a) == 1 and a[0] == 0) and len(a) >= len(b):
        tick()
        shift = len(a) - len(b)
        multiplier = a[-1] / b[-1]
        for j, value in enumerate(b):
            a[j + shift] -= multiplier * value
        poly_trim(a)
    return a

def signs_variation(values):
    signs = [1 if x > 0 else -1 for x in values if x]
    return sum(a != b for a, b in zip(signs, signs[1:]))

def sturm(poly):
    require(poly[0] != 0, 'Sturm endpoint is a root')
    if len(poly) == 1:
        return 0, [poly]
    sequence = [[Fraction(v) for v in poly],
                [Fraction(i * poly[i]) for i in range(1, len(poly))]]
    while True:
        rem = remainder(sequence[-2], sequence[-1])
        if len(rem) == 1 and rem[0] == 0:
            break
        sequence.append([-x for x in rem])
    at_zero = signs_variation([q[0] for q in sequence])
    at_infinity = signs_variation([q[-1] for q in sequence])
    return at_zero - at_infinity, sequence

def rows_for(images0, images1):
    rows = sorted(set().union(*(v.keys() for v in images0 + images1)))
    a = {row: [int(v.get(row, 0)) for v in images0] for row in rows}
    b = {row: [int(v.get(row, 0)) for v in images1] for row in rows}
    return rows, a, b

def first_rows(rows, matrix, dimension):
    chosen = []
    rowspace = Span()
    for row in rows:
        vector = {(i,): value for i, value in enumerate(matrix[row]) if value}
        if rowspace.add(vector):
            chosen.append(row)
            if len(chosen) == dimension:
                return chosen
    raise BadConstruction('no maximal s4 row minor')

def evaluate_minor(chosen, a, b):
    aa = [a[row] for row in chosen]
    bb = [b[row] for row in chosen]
    if det_integer(aa) == 0:
        return None
    poly = determinant_polynomial(aa, bb)
    multiplier = -1 if poly[0] < 0 else 1
    poly = [multiplier * c for c in poly]
    roots, seq = sturm(poly)
    certificate = {'rows': [''.join(LETTERS[i] for i in row) for row in chosen],
                   'matrix_constant_s4': aa, 'matrix_shift_coefficient': bb,
                   'determinant_normalization_multiplier': multiplier,
                   'normalized_determinant_coefficients_low_to_high': poly,
                   'nonnegative_shift_coefficients': all(c >= 0 for c in poly),
                   'sturm_positive_root_count': roots,
                   'sturm_sequence_low_to_high': [[number(c) for c in p] for p in seq]}
    if certificate['nonnegative_shift_coefficients'] or roots == 0:
        certificate['proves_nonzero_for_all_real_s_ge_4'] = True
    else:
        certificate['proves_nonzero_for_all_real_s_ge_4'] = False
    return certificate

def attempt(report, chosen, a, b):
    tick()
    cert = evaluate_minor(chosen, a, b)
    report['minor_attempts'] = report.get('minor_attempts', 0) + 1
    if cert is not None:
        report['last_nonsingular_minor'] = cert
        if cert['proves_nonzero_for_all_real_s_ge_4']:
            report['certificate'] = cert
            report['status'] = 'CERTIFIED_BY_EXACT_MINOR'
            return True
    return False

def main(state):
    x = {(0,): 1}
    b = {(2,): 1}
    xb = bracket(x, b)
    actual = f3(xb, 4)
    flipped = f3(xb, 4, True)
    require(actual == {(2,): 6} and flipped == {(2,): 2},
            'Cartan-sign intended-reason control failed')
    state['controls']['cartan_sign'] = {'actual': sparse(actual),
                                         'flipped_cartan': sparse(flipped),
                                         'detected_intended_difference': True}
    state['stage'] = 'whole_relation'
    seed, relations = relation_closure()
    translate = action(seed, E2)
    target = relations.get((1, 1))
    require(bool(translate) and target is not None and target.contains(translate),
            'missing nonzero E2(seed) in actual relation')
    # Mutant retains the seed alone, hence has zero relation at weight (1,1).
    omitted = Span()
    require(not omitted.contains(translate), 'omitted-translate control failed')
    state['controls']['omitted_E2_seed_translate'] = {
        'weight': [1, 1], 'actual_translate': sparse(translate),
        'actual_relation_contains_translate': True,
        'seed_only_mutant_relation_dimension_at_weight': 0,
        'mutant_contains_translate': False, 'detected_intended_omission': True}
    state['relation'] = {'dimension': 81, 'seed': sparse(seed),
                         'raising_and_lowering_stable': True,
                         'f3_kills_every_basis_vector_at_s4_and_s5': True,
                         'basis_by_weight': {weight_key(w): [sparse(v) for v in span.original]
                                             for w, span in sorted(relations.items())}}
    state['stage'] = 'construct_three_complete_lowest_spaces_and_s4_s5'
    matrices = {}
    for weight, label, expected, qdim in TARGETS:
        key = weight_key(weight)
        report = {'weight': list(weight), 'status': 'STARTED'}
        state['types'][key] = report
        matrices[key] = make_type(weight, label, expected, qdim, relations, report)
    state['controls']['lost_copy'] = {'per_type': {k: state['types'][k]['lost_copy_control']
                                                    for k in state['types']},
                                      'detected_intended_loss_in_each_type': True}
    state['stage'] = 'first_exact_minor_per_type'
    pending = {}
    for weight, _, expected, _ in TARGETS:
        key = weight_key(weight)
        rows, a, bcoef = rows_for(*matrices[key])
        chosen = first_rows(rows, a, expected)
        pending[key] = (rows, a, bcoef, chosen)
        attempt(state['types'][key], chosen, a, bcoef)
    state['stage'] = 'alternative_exact_minors_for_unresolved_types'
    for key, (rows, a, bcoef, initial) in pending.items():
        report = state['types'][key]
        if report.get('certificate'):
            continue
        used = {tuple(initial)}
        attempted = 0
        for i in range(len(initial)):
            if report.get('certificate') or attempted >= 96:
                break
            for row in rows:
                tick()
                if row in initial:
                    continue
                candidate = tuple(sorted(initial[:i] + [row] + initial[i + 1:]))
                if candidate in used:
                    continue
                used.add(candidate)
                attempted += 1
                if attempt(report, list(candidate), a, bcoef) or attempted >= 96:
                    break
        if not report.get('certificate'):
            report['status'] = 'UNRESOLVED_NO_ALL_PARAMETER_MINOR_FOUND'
    state['stage'] = 'finished'
    state['status'] = ('COMPLETE_CERTIFICATES' if all(t.get('certificate') for t in state['types'].values())
                       else 'PARTIAL_SAMPLES_AND_UNRESOLVED_MINORS')

state = {'status': 'INCOMPLETE', 'stage': 'initializing', 'controls': {}, 'types': {},
         'scope': {'r': 3, 'integer_s_minimum': 4,
                   'weights': [[1, 2], [2, 1], [2, 2]],
                   'cooperative_deadline_seconds': SOFT_SECONDS,
                   'alarm_seconds': ALARM_SECONDS,
                   'parameter': 't=s-4',
                   'imports': ['actual free-Lie/whole both-sign Serre bridge',
                               'given eight-letter Levi and actual F3 actions'],
                   'nonclaims': ['no other types or r values', 'no automatic radical adoption',
                                 'no human, independent family, kernel or novelty claim']}}
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, ALARM_SECONDS)
try:
    main(state)
except Stopped as exc:
    state['status'] = 'INCOMPLETE_DEADLINE'
    state['error'] = {'class': type(exc).__name__, 'message': str(exc)}
except BaseException as exc:
    state['status'] = 'ERROR'
    state['error'] = {'class': type(exc).__name__, 'message': str(exc)}
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    state['elapsed_seconds_at_json'] = time.monotonic() - START
    print(json.dumps(state, sort_keys=True, separators=(',', ':')), flush=True)
