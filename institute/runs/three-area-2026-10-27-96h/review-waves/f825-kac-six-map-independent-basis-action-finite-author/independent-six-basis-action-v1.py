#!/usr/bin/env python3
"""UNRUN candidate: six pinned grade-four basis/action dossiers; stdout JSONL only.

Run only after a complete parent source read and a separate, bounded GO. The
sole file inputs are the six literal pins below. This is not a source-identity,
novelty, formal-proof, human-review or global J=tau certificate.
"""

import hashlib
import itertools
import json
import math
import signal
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/parent-six-symbolic-minor-dossiers-v1')
SPECS = (
    ('weight-1-2.json', '945d4dd07897fd9fdc24bc6c44b71aa16a8c6aabf98417f06f0e0e726ce4ae1f', (1, 2), (4, 1), 4, 9),
    ('weight-2-1.json', '73507164325c2d489753b4b578dda12336044b3b3f409e08e88d65efb10502f0', (2, 1), (1, 4), 4, 8),
    ('weight-2-2.json', '5e1f7c3c83ad9b1be8bd393460f278d3a615000ebd1506d08ecae5ea2d663b55', (2, 2), (2, 2), 7, 23),
    ('weight-2-3.json', 'a4ba7e05a07cf9e69c7b52a72261f79d98147f96630c8a2bc06fa91c7ed64a0a', (2, 3), (3, 0), 6, 34),
    ('weight-3-2.json', '0467fbf56e335ec150419bb7bde6e7149a1eb99783081b2a87b1ef3a5d2dd29b', (3, 2), (0, 3), 6, 33),
    ('weight-3-3-compact.json', '757dc7ca0390aa9bd658e1ed888b1b710a9755887833653f94d3670097ebd3c7', (3, 3), (1, 1), 8, 62),
)
ALPHABET = 'xabcdefg'
DEG = dict(zip(ALPHABET, ((0, 0), (1, 0), (0, 1), (1, 1),
                          (1, 1), (2, 1), (1, 2), (2, 2))))

# The named eight-letter actual Levi interface, not matrices multiplying the
# letters. All tensor products below are concatenations in T(V).
E1 = {'x': {'a': 1}, 'b': {'c': 1}, 'c': {'e': -2},
      'd': {'e': -1}, 'f': {'g': 1}}
E2 = {'x': {'b': 1}, 'a': {'d': 1}, 'c': {'f': 1},
      'd': {'f': 2}, 'e': {'g': -1}}
F1 = {'a': {'x': 1}, 'c': {'b': 2}, 'd': {'b': 1},
      'e': {'c': -1}, 'g': {'f': 1}}
F2 = {'b': {'x': 1}, 'c': {'a': 1}, 'd': {'a': 2},
      'f': {'d': 1}, 'g': {'e': -1}}


class CheckFailure(Exception):
    def __init__(self, code, detail=''):
        super().__init__(code + (': ' + str(detail) if detail else ''))
        self.code = code
        self.detail = str(detail)


class Deadline(Exception):
    pass


def require(condition, code, detail=''):
    if not condition:
        raise CheckFailure(code, detail)


def emit(event, **fields):
    print(json.dumps({'event': event, **fields}, sort_keys=True, separators=(',', ':')), flush=True)


def add_scaled(out, vec, factor=1):
    if not factor:
        return
    for key, value in vec.items():
        z = out.get(key, 0) + factor * value
        if z:
            out[key] = z
        elif key in out:
            del out[key]


def bracket(left, right):
    out = {}
    for a, av in left.items():
        for b, bv in right.items():
            z = av * bv
            add_scaled(out, {a + b: z, b + a: -z} if a + b != b + a else {}, 1)
    return out


@lru_cache(maxsize=None)
def tree_tensor(tree):
    """The right-nested bracket tree [t0,[t1,...]], in the tensor algebra."""
    if len(tree) == 1:
        return {tree[0]: 1}
    return bracket({tree[0]: 1}, tree_tensor(tree[1:]))


def word_weight(word):
    a = b = 0
    for ch in word:
        x, y = DEG[ch]
        a += x
        b += y
    return (a, b)


def tensor_action(vector, operator):
    out = {}
    for word, coeff in vector.items():
        for pos, ch in enumerate(word):
            for replacement, factor in operator.get(ch, {}).items():
                new = word[:pos] + replacement + word[pos + 1:]
                add_scaled(out, {new: coeff * factor})
    return out


def compose_letter(first, second, ch):
    out = {}
    for middle, c in second.get(ch, {}).items():
        add_scaled(out, first.get(middle, {}), c)
    return out


def make_d_actions():
    e12 = {}
    for ch in ALPHABET:
        image = compose_letter(E1, E2, ch)
        add_scaled(image, compose_letter(E2, E1, ch), -1)
        if image:
            e12[ch] = image
    constant = {ch: {} for ch in ALPHABET}
    slope = {ch: {} for ch in ALPHABET}
    for ch, (i, j) in DEG.items():
        n = 3 * i + 4 * j - 2
        if n:
            constant['x'][ch] = {ch: n}
        if j:
            slope['x'][ch] = {ch: j}
    for source, op, c0, c1 in (('a', E1, -3, 0), ('b', E2, -4, -1),
                                ('c', e12, -4, -1), ('d', e12, 3, 0)):
        for ch, image in op.items():
            if c0:
                constant[source][ch] = {k: c0 * v for k, v in image.items()}
            if c1:
                slope[source][ch] = {k: c1 * v for k, v in image.items()}
    return constant, slope


D0, D1 = make_d_actions()


@lru_cache(maxsize=None)
def tree_f3(tree, component):
    """Actual F3 by the Lie-bracket recursion, not tensor pair deletion.

    D_u = ad([f3,u]) on V. For [u,v], the first term is D_u v;
    when v is a letter the second is -D_v u, otherwise it is [u,F3 v].
    """
    require(len(tree) >= 2, 'TREE_ACTION_DEGREE')
    actions = D0 if component == 0 else D1
    first, rest = tree[0], tree[1:]
    out = tensor_action(tree_tensor(rest), actions[first])
    if len(rest) == 1:
        add_scaled(out, actions[rest[0]].get(first, {}), -1)
    else:
        add_scaled(out, bracket({first: 1}, tree_f3(rest, component)))
    return out


def primitive(vec):
    vec = {k: v for k, v in vec.items() if v}
    if not vec:
        return {}
    g = 0
    for value in vec.values():
        g = math.gcd(g, abs(value))
    sign = -1 if vec[min(vec)] < 0 else 1
    return {k: sign * (v // g) for k, v in vec.items()}


class IntSpan:
    """Sparse exact fraction-free echelon span over Q, with primitive rows."""
    def __init__(self):
        self.pivots = {}
        self.trees = []

    def copy(self):
        result = IntSpan()
        result.pivots = self.pivots.copy()
        result.trees = self.trees.copy()
        return result

    def remainder(self, vector):
        v = primitive(vector)
        while v:
            p = min(v)
            if p not in self.pivots:
                break
            basis = self.pivots[p]
            a, b = v[p], basis[p]
            g = math.gcd(abs(a), b)
            scale, take = b // g, a // g
            v = {k: scale * value for k, value in v.items()}
            add_scaled(v, basis, -take)
            v = primitive(v)
        return v

    def insert(self, vector):
        v = self.remainder(vector)
        if v:
            self.pivots[min(v)] = v
            return v
        return None

    def contains(self, vector):
        return not self.remainder(vector)

    def __len__(self):
        return len(self.pivots)


class TreeCoordinates:
    """Express tensors in the independently selected original bracket trees."""
    def __init__(self, trees):
        self.pivots = {}
        for index, tree in enumerate(trees):
            v = {k: Fraction(x) for k, x in tree_tensor(tree).items()}
            representation = {index: Fraction(1)}
            while v:
                p = min(v)
                if p not in self.pivots:
                    a = v[p]
                    self.pivots[p] = ({k: x / a for k, x in v.items()},
                                      {k: x / a for k, x in representation.items()})
                    break
                row, rep = self.pivots[p]
                a = v[p]
                add_scaled(v, row, -a)
                add_scaled(representation, rep, -a)
            else:
                raise CheckFailure('TREE_BASIS_DEPENDENT', index)

    def solve(self, vector):
        v = {k: Fraction(x) for k, x in vector.items() if x}
        result = {}
        while v:
            p = min(v)
            require(p in self.pivots, 'NOT_IN_FREE_LIE', p)
            row, rep = self.pivots[p]
            a = v[p]
            add_scaled(v, row, -a)
            add_scaled(result, rep, a)
        return result


def build_free_lie():
    spaces = {}
    for tree in itertools.product(ALPHABET, repeat=4):
        vector = tree_tensor(tree)
        if not vector:
            continue
        weight = word_weight(tree)
        basis = spaces.setdefault(weight, IntSpan())
        if basis.insert(vector) is not None:
            basis.trees.append(tree)
    require(sum(len(space) for space in spaces.values()) == 1008, 'FREE_LIE_DIMENSION')
    return spaces


def build_relation():
    # q3 = (ad x)^3 a. Close its entire cyclic module under E1,E2,
    # retaining independent primitive vectors at every horizontal weight.
    seed = tree_tensor(('x', 'x', 'x', 'a'))
    require(bool(seed), 'ZERO_RELATION_SEED')
    spaces = {}
    queue = []

    def offer(weight, vector):
        basis = spaces.setdefault(weight, IntSpan())
        residual = basis.insert(vector)
        if residual is not None:
            queue.append((weight, residual))

    offer((1, 0), seed)
    i = 0
    while i < len(queue):
        (a, b), vector = queue[i]
        i += 1
        offer((a + 1, b), tensor_action(vector, E1))
        offer((a, b + 1), tensor_action(vector, E2))
    require(sum(len(space) for space in spaces.values()) == 81, 'RELATION_DIMENSION')
    return spaces, queue


def relation_space(spaces, weight):
    return spaces.get(weight, IntSpan())


def lift_action(vector, weight, component, free, solvers):
    require(weight in free, 'NOT_IN_FREE_LIE', weight)
    if weight not in solvers:
        solvers[weight] = TreeCoordinates(free[weight].trees)
    coordinates = solvers[weight].solve(vector)
    out = {}
    for index, c in coordinates.items():
        add_scaled(out, tree_f3(free[weight].trees[index], component), c)
    return out


def check_relation(free, relation, rows, solvers):
    require(len(rows) == 81, 'RELATION_DIMENSION', len(rows))
    for (a, b), vector in rows:
        require((a, b) in free and free[(a, b)].contains(vector), 'RELATION_NOT_FREE', (a, b))
        for op, target in ((F1, (a - 1, b)), (F2, (a, b - 1)),
                           (E1, (a + 1, b)), (E2, (a, b + 1))):
            require(relation_space(relation, target).contains(tensor_action(vector, op)),
                    'RELATION_NOT_LEVI_STABLE', ((a, b), target))
        for component in (0, 1):
            require(not lift_action(vector, (a, b), component, free, solvers),
                    'RELATION_F3_DESCENT', ((a, b), component))


def duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'DUPLICATE_JSON_KEY', key)
        result[key] = value
    return result


def reject_float(_):
    raise CheckFailure('NONINTEGER_JSON_NUMBER')


def integer(value):
    require(isinstance(value, str) and value and
            (value.isdigit() or (value[0] == '-' and value[1:].isdigit())),
            'BAD_INTEGER', value)
    return int(value)


def parse_vector(raw, length, weight):
    pairs = list(raw.items()) if isinstance(raw, dict) else raw
    require(isinstance(pairs, list), 'BAD_VECTOR_CONTAINER')
    result = {}
    for pair in pairs:
        require(isinstance(pair, (list, tuple)) and len(pair) == 2, 'BAD_VECTOR_ENTRY')
        word, value = pair
        require(isinstance(word, str) and len(word) == length and
                all(ch in ALPHABET for ch in word), 'BAD_TENSOR_WORD', word)
        require(word_weight(word) == weight, 'BAD_TENSOR_WEIGHT', word)
        require(word not in result, 'DUPLICATE_TENSOR_WORD', word)
        n = integer(value)
        require(n != 0, 'ZERO_TENSOR_ENTRY', word)
        result[word] = n
    return result


def load_inputs():
    dossiers = []
    for name, pin, weight, label, dimension, quotient_dimension in SPECS:
        blob = (ROOT / name).read_bytes()
        require(hashlib.sha256(blob).hexdigest() == pin, 'INPUT_SHA256', name)
        data = json.loads(blob.decode('utf-8'), parse_int=str, parse_float=reject_float,
                          parse_constant=reject_float, object_pairs_hook=duplicate_keys)
        require(data.get('kind') == 'CAPTURED_COMPLETE_LOWEST_PENCIL_CERTIFICATE', 'INPUT_KIND', name)
        require(tuple(integer(x) for x in data['weight']) == weight, 'INPUT_WEIGHT', name)
        require(tuple(integer(x) for x in data['label']) == label, 'INPUT_LABEL', name)
        require(integer(data['multiplicity']) == dimension, 'INPUT_MULTIPLICITY', name)
        require(integer(data['quotient_dimension']) == quotient_dimension, 'INPUT_QUOTIENT_DIMENSION', name)
        tensors = [parse_vector(v, 4, weight) for v in data['lowest_tensors']]
        constant = [parse_vector(v, 3, weight) for v in data['constant_columns']]
        slope = [parse_vector(v, 3, weight) for v in data['coefficient_columns']]
        require(len(tensors) == len(constant) == len(slope) == dimension, 'INPUT_COLUMN_COUNT', name)
        dossiers.append((weight, label, dimension, quotient_dimension, tensors, constant, slope))
    return dossiers


def lower_checks(vectors, weight, free, relation):
    require(weight in free, 'MISSING_FREE_WEIGHT', weight)
    for column, vector in enumerate(vectors):
        require(free[weight].contains(vector), 'NOT_IN_FREE_LIE', column)
        for op, target in ((F1, (weight[0] - 1, weight[1])),
                           (F2, (weight[0], weight[1] - 1))):
            require(relation_space(relation, target).contains(tensor_action(vector, op)),
                    'LOWERING_OUTSIDE_RELATION', (column, target))
    span = relation_space(relation, weight).copy()
    for column, vector in enumerate(vectors):
        require(span.insert(vector) is not None, 'QUOTIENT_DEPENDENT', column)


def kernel_dimension(weight, free, relation):
    """Rank the simultaneous lowering into BOTH whole quotient targets."""
    a, b = weight
    target1, target2 = (a - 1, b), (a, b - 1)
    span = IntSpan()
    for vector in relation_space(relation, target1).pivots.values():
        span.insert({(1, word): c for word, c in vector.items()})
    for vector in relation_space(relation, target2).pivots.values():
        span.insert({(2, word): c for word, c in vector.items()})
    before = len(span)
    for tree in free[weight].trees:
        v = tree_tensor(tree)
        combined = {(1, word): c for word, c in tensor_action(v, F1).items()}
        combined.update({(2, word): c for word, c in tensor_action(v, F2).items()})
        span.insert(combined)
    induced_rank = len(span) - before
    return len(free[weight]) - induced_rank - len(relation_space(relation, weight)), induced_rank


def exact_int_vector(vector):
    out = {}
    for key, value in vector.items():
        value = Fraction(value)
        require(value.denominator == 1, 'NONINTEGRAL_ACTION', key)
        if value:
            out[key] = value.numerator
    return out


def compare_action(actual, emitted, component, column):
    if actual != emitted:
        words = sorted(set(actual) | set(emitted))
        first = next(word for word in words if actual.get(word, 0) != emitted.get(word, 0))
        raise CheckFailure('ACTION_COLUMN_MISMATCH', (component, column, first))


def vector_rank(columns):
    span = IntSpan()
    for column in columns:
        span.insert(column)
    return len(span)


def expect_rejection(reason, function):
    try:
        function()
    except CheckFailure as exc:
        require(exc.code == reason, 'CONTROL_WRONG_REASON', (reason, exc.code))
        return
    raise CheckFailure('CONTROL_NOT_REJECTED', reason)


def check_seed_samples():
    for component, expected in ((0, {'a': 4}), (1, {})):
        require(tree_f3(('x', 'a'), component) == expected, 'SEED_SAMPLE_XA', component)
    for component, expected in ((0, {'b': 6}), (1, {'b': 2})):
        require(tree_f3(('x', 'b'), component) == expected, 'SEED_SAMPLE_XB', component)
    for component in (0, 1):
        require(not tree_f3(('x', 'x', 'x', 'a'), component), 'SEED_SAMPLE_RELATION', component)


def check_type(dossier, free, relation, solvers):
    weight, label, dimension, qdimension, tensors, emitted0, emitted1 = dossier
    require(weight in free, 'MISSING_FREE_WEIGHT', weight)
    require(len(free[weight]) - len(relation_space(relation, weight)) == qdimension,
            'QUOTIENT_DIMENSION', weight)
    actual_kernel, induced_rank = kernel_dimension(weight, free, relation)
    require(actual_kernel == dimension, 'LOWEST_KERNEL_DIMENSION', (weight, actual_kernel))
    lower_checks(tensors, weight, free, relation)
    actual0, actual1 = [], []
    for col, tensor in enumerate(tensors):
        v0 = exact_int_vector(lift_action(tensor, weight, 0, free, solvers))
        v1 = exact_int_vector(lift_action(tensor, weight, 1, free, solvers))
        compare_action(v0, emitted0[col], 0, col)
        compare_action(v1, emitted1[col], 1, col)
        actual0.append(v0)
        actual1.append(v1)
    sample_ranks = []
    for shift in (0, 1):
        cols = []
        for v0, v1 in zip(actual0, actual1):
            v = v0.copy()
            add_scaled(v, v1, shift)
            cols.append(v)
        rank = vector_rank(cols)
        require(rank == dimension, 'SAMPLE_ACTION_RANK', (weight, shift + 4, rank))
        sample_ranks.append(rank)

    # In-memory intended-reason mutations; no fixture files or other inputs.
    bad_tensors = [v.copy() for v in tensors]
    key = min(bad_tensors[0])
    add_scaled(bad_tensors[0], {key: 1})
    expect_rejection('NOT_IN_FREE_LIE', lambda: lower_checks(bad_tensors, weight, free, relation))
    duplicate = [v.copy() for v in tensors]
    duplicate[-1] = duplicate[0].copy()
    expect_rejection('QUOTIENT_DEPENDENT', lambda: lower_checks(duplicate, weight, free, relation))
    changed = emitted1[0].copy()
    key = min(changed) if changed else 'xxx'
    add_scaled(changed, {key: 1})
    expect_rejection('ACTION_COLUMN_MISMATCH', lambda: compare_action(actual1[0], changed, 1, 0))
    return {'weight': weight, 'label': label, 'free_dimension': len(free[weight]),
            'relation_dimension': len(relation_space(relation, weight)),
            'quotient_dimension': qdimension, 'lowering_rank': induced_rank,
            'lowest_kernel_dimension': actual_kernel, 'basis_columns': dimension,
            'constant_and_slope_all_coefficients': 'MATCH', 'sample_s4_s5_ranks': sample_ranks,
            'mutation_reasons': ['NOT_IN_FREE_LIE', 'QUOTIENT_DEPENDENT', 'ACTION_COLUMN_MISMATCH']}


def control_omitted_relation(rows):
    spans = {}
    for weight, vector in rows[1:]:
        spans.setdefault(weight, IntSpan()).insert(vector)
    rank = sum(len(v) for v in spans.values())
    require(rank == 81, 'RELATION_DIMENSION', rank)


def main():
    stage = 'INPUTS'
    completed = []
    def alarm_handler(_signum, _frame):
        raise Deadline()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(40)
    try:
        dossiers = load_inputs()
        stage = 'SEED_SAMPLES'
        check_seed_samples()
        stage = 'FREE_LIE_ALL_WEIGHTS'
        free = build_free_lie()
        stage = 'WHOLE_RELATION'
        relation, rows = build_relation()
        solvers = {}
        stage = 'RELATION_MEMBERSHIP_LEVI_STABILITY_AND_F3_DESCENT'
        check_relation(free, relation, rows, solvers)
        expect_rejection('RELATION_DIMENSION', lambda: control_omitted_relation(rows))
        emit('GLOBAL_PASS', free_lie_dimension=1008, relation_dimension=81,
             free_weight_spaces=len(free), relation_weight_spaces=len(relation),
             relation_mutation='RELATION_DIMENSION', seed_samples='EXACT')
        for dossier in dossiers:
            stage = 'TYPE_' + '_'.join(str(x) for x in dossier[0])
            result = check_type(dossier, free, relation, solvers)
            completed.append(result)
            emit('TYPE_PASS', **result)
        stage = 'COMPLETE'
        signal.alarm(0)
        emit('END_COMPLETE', type_count=len(completed), scope='SIX_BASIS_AND_ACTUAL_F3_COLUMNS_ONLY')
        return 0
    except Deadline:
        signal.alarm(0)
        emit('PARTIAL_TIMEOUT', stage=stage, completed_types=[x['weight'] for x in completed])
        return 2
    except CheckFailure as exc:
        signal.alarm(0)
        emit('CHECK_FAILURE', stage=stage, code=exc.code, detail=exc.detail,
             completed_types=[x['weight'] for x in completed])
        return 3
    except Exception as exc:
        signal.alarm(0)
        emit('ERROR_NOT_PASS', stage=stage, error_type=type(exc).__name__, detail=str(exc),
             completed_types=[x['weight'] for x in completed])
        return 4


if __name__ == '__main__':
    sys.exit(main())
