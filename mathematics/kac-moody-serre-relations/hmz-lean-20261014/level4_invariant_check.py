"""Exact original-row lowering on a constructed Levi invariant at level four.

This is a fixed local-part calculation in the free Lie algebra on the adjoint
sl3 module. It does not enumerate Cartan matrices, roots, or Serre ideals.
Coefficients of the lowering image are affine triples (constant, r, s).
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json


ZERO = (Q(0), Q(0), Q(0))


def affine_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def affine_scale(c, a):
    return tuple(c * x for x in a)


def matrix_unit(i, j):
    return tuple(Q(int(a == i and b == j)) for a in range(3) for b in range(3))


def matrix_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def matrix_scale(c, a):
    return tuple(c * x for x in a)


def matrix_mul(a, b):
    return tuple(sum(a[3 * i + k] * b[3 * k + j] for k in range(3))
                 for i in range(3) for j in range(3))


def matrix_bracket(a, b):
    return matrix_add(matrix_mul(a, b), matrix_scale(-1, matrix_mul(b, a)))


def trace(a):
    return a[0] + a[4] + a[8]


H1 = matrix_add(matrix_unit(0, 0), matrix_scale(-1, matrix_unit(1, 1)))
H2 = matrix_add(matrix_unit(1, 1), matrix_scale(-1, matrix_unit(2, 2)))
# Each entry denotes a vector of V, not a Cartan element in the ambient algebra.
BASIS = [matrix_unit(0, 1), matrix_unit(1, 2), matrix_unit(0, 2),
         matrix_unit(1, 0), matrix_unit(2, 1), matrix_unit(2, 0), H1, H2]
NAMES = ['E12', 'E23', 'E13', 'E21', 'E32', 'E31', 'H1-model', 'H2-model']
DEGREES = [(2, 1), (1, 2), (2, 2), (0, 1), (1, 0), (0, 0), (1, 1), (1, 1)]
DUAL = [BASIS[3], BASIS[4], BASIS[5], BASIS[0], BASIS[1], BASIS[2],
        matrix_scale(Q(1, 3), matrix_add(matrix_scale(2, H1), H2)),
        matrix_scale(Q(1, 3), matrix_add(H1, matrix_scale(2, H2)))]


def coordinates(a):
    assert trace(a) == 0
    answer = [a[1], a[5], a[2], a[3], a[7], a[6], a[0], -a[8]]
    reconstructed = (Q(0),) * 9
    for c, b in zip(answer, BASIS):
        reconstructed = matrix_add(reconstructed, matrix_scale(c, b))
    assert reconstructed == a
    return answer


def poly_add(left, right):
    result = dict(left)
    for w, c in right.items():
        result[w] = result.get(w, Q(0)) + c
        if not result[w]:
            del result[w]
    return result


def poly_scale(c, p):
    return {w: c * v for w, v in p.items() if c * v}


def poly_mul(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            w = a + b
            result[w] = result.get(w, Q(0)) + ca * cb
    return {w: c for w, c in result.items() if c}


def poly_bracket(left, right):
    return poly_add(poly_mul(left, right), poly_scale(-1, poly_mul(right, left)))


def affine_poly_add(left, right):
    result = dict(left)
    for w, c in right.items():
        result[w] = affine_add(result.get(w, ZERO), c)
        if result[w] == ZERO:
            del result[w]
    return result


def affine_poly_scale(c, p):
    return {w: affine_scale(c, v) for w, v in p.items() if affine_scale(c, v) != ZERO}


def affine_poly_mul(left, right):
    # left is affine, right is constant.
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            w = a + b
            result[w] = affine_add(result.get(w, ZERO), affine_scale(cb, ca))
    return {w: c for w, c in result.items() if c != ZERO}


def affine_poly_bracket(left, right):
    # [left, right], with left affine and right constant.
    backward = {b + a: ZERO for a in left for b in right}
    for a, ca in left.items():
        for b, cb in right.items():
            backward[b + a] = affine_add(backward[b + a], affine_scale(cb, ca))
    return affine_poly_add(affine_poly_mul(left, right), affine_poly_scale(-1, backward))


def action_on_poly(actor, p):
    result = {}
    for w, coefficient in p.items():
        for position, letter in enumerate(w):
            for new_letter, c in enumerate(coordinates(matrix_bracket(actor, BASIS[letter]))):
                if c:
                    replacement = w[:position] + (new_letter,) + w[position + 1:]
                    result[replacement] = result.get(replacement, Q(0)) + coefficient * c
    return {w: c for w, c in result.items() if c}


def leaf_lowering(letter):
    # The output is a Levi actor plus a multiple of the true h3.
    # Actor terms are (affine coefficient, sl3 matrix).
    if letter == 3:  # V-model E21 = w
        return [(ZERO[:2] + (Q(-1),), BASIS[1])], ZERO
    if letter == 4:  # V-model E32 = -u
        return [((Q(0), Q(1), Q(0)), BASIS[0])], ZERO
    if letter == 5:  # V-model E31 = v
        return [], (Q(-1), Q(0), Q(0))
    if letter == 6:  # V-model H1 = p
        return [((Q(0), Q(0), Q(-1)), BASIS[2])], ZERO
    if letter == 7:  # V-model H2 = -q
        return [((Q(0), Q(-1), Q(0)), BASIS[2])], ZERO
    return [], ZERO


def level_zero_action(image, p):
    actors, h3 = image
    result = {}
    for coefficient, actor in actors:
        result = affine_poly_add(result,
            {w: affine_scale(c, coefficient) for w, c in action_on_poly(actor, p).items()})
    assert h3[1:] == (Q(0), Q(0))  # no quadratic parameter products
    if h3[0]:
        for w, c in p.items():
            a = sum(DEGREES[letter][0] for letter in w)
            b = sum(DEGREES[letter][1] for letter in w)
            weight = (Q(2 * len(w)), Q(-a), Q(-b))
            term = affine_scale(c * h3[0], weight)
            result = affine_poly_add(result, {w: term})
    return result


def evaluate_and_lower(tree):
    if isinstance(tree, int):
        return {(tree,): Q(1)}, leaf_lowering(tree), 1
    a, da, na = evaluate_and_lower(tree[0])
    b, db, nb = evaluate_and_lower(tree[1])
    first = level_zero_action(da, b) if na == 1 else affine_poly_bracket(da, b)
    second = level_zero_action(db, a) if nb == 1 else affine_poly_bracket(db, a)
    return poly_bracket(a, b), affine_poly_add(first, affine_poly_scale(-1, second)), na + nb


def main():
    for i, j in product(range(8), repeat=2):
        assert trace(matrix_mul(BASIS[i], DUAL[j])) == int(i == j)
    dual_coordinates = [coordinates(a) for a in DUAL]
    # Reproduce the dossier's original-row level-two formulas before proceeding.
    _, dt1, _ = evaluate_and_lower((5, 4))  # t1 = -[E31, E32]
    dt1 = affine_poly_scale(-1, dt1)
    assert dt1 == {(4,): (Q(2), Q(-2), Q(0))}
    _, dt2, _ = evaluate_and_lower((5, 3))
    assert dt2 == {(3,): (Q(-2), Q(0), Q(2))}
    dz = {}
    for tree in [(5, 6), (5, 7), (4, 3)]:
        dz = affine_poly_add(dz, evaluate_and_lower(tree)[1])
    assert dz == {(6,): (Q(-2), Q(3), Q(2)), (7,): (Q(-2), Q(2), Q(3))}
    invariant, image = {}, {}
    nonzero_contractions = 0
    # An invariant covariant tensor, symmetric in the first pair and skew in the second.
    # Use trace-dual vectors to obtain the invariant contravariant tensor.
    for i, j, k, l in product(range(8), repeat=4):
        symmetric = matrix_add(matrix_mul(BASIS[i], BASIS[j]), matrix_mul(BASIS[j], BASIS[i]))
        coefficient = trace(matrix_mul(symmetric, matrix_bracket(BASIS[k], BASIS[l])))
        if not coefficient:
            continue
        nonzero_contractions += 1
        choices = [[(letter, value) for letter, value in enumerate(dual_coordinates[index])
                    if value] for index in (i, j, k, l)]
        for (a, ca), (b, cb), (c, cc), (d, cd) in product(*choices):
            scalar = coefficient * ca * cb * cc * cd
            value, lowered, _ = evaluate_and_lower((a, (c, (b, d))))
            invariant = poly_add(invariant, poly_scale(scalar, value))
            image = affine_poly_add(image, affine_poly_scale(scalar, lowered))
    assert invariant, 'This invariant tensor projects to zero in degree-four free Lie'
    for actor in [BASIS[0], BASIS[1], BASIS[3], BASIS[4], H1, H2]:
        assert not action_on_poly(actor, invariant), 'Candidate fails Levi invariance'
    assert all(sum(DEGREES[a][0] for a in w) == 4 and
               sum(DEGREES[a][1] for a in w) == 4 for w in invariant)
    assert all(sum(DEGREES[a][0] for a in w) == 4 and
               sum(DEGREES[a][1] for a in w) == 4 for w in image)
    # A single affine coefficient with one sign on r,s >= 4 proves nonvanishing.
    witness = None
    for word, coeff in sorted(image.items()):
        constant, r, s = coeff
        for orientation in [1, -1]:
            if (orientation * r >= 0 and orientation * s >= 0 and
                    orientation * (constant + 4 * r + 4 * s) > 0):
                witness = {'word': [NAMES[i] for i in word],
                           'coefficient_constant_r_s': [str(x) for x in coeff],
                           'orientation': orientation,
                           'oriented_value_at_4_4': str(orientation * (constant + 4*r + 4*s))}
                break
        if witness:
            break
    assert witness is not None, 'No same-sign coefficient found; no claimed detection'
    payload = {
        'scope': 'single trivial Levi summand in free L4(ad sl3); original D3; r,s >= 4',
        'full_goal_solved': False,
        'field': 'Q, exact affine parameter arithmetic',
        'nonzero_invariant_tensor_contractions': nonzero_contractions,
        'invariant_associative_words': len(invariant),
        'lowering_associative_words': len(image),
        'levi_invariance_all_six_generators_checked': True,
        'original_row_level_two_controls_checked': ['Dt1', 'Dt2', 'Dz'],
        'source_full_degree': [4, 4, 4], 'target_full_degree': [4, 4, 3],
        'nonvanishing_coefficient': witness,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'not_a_serre_counterexample': True,
        'not_all_primitive_summands_checked': True,
    }
    serialized_invariant = [{'word': [NAMES[i] for i in w], 'coefficient': str(c)}
                            for w, c in sorted(invariant.items())]
    serialized_image = [{'word': [NAMES[i] for i in w], 'constant_r_s': [str(x) for x in c]}
                        for w, c in sorted(image.items())]
    root = Path(__file__).resolve().parent
    (root/'level4-invariant-result.json').write_text(json.dumps(payload, indent=2)+'\n')
    (root/'level4-invariant-vectors.json').write_text(json.dumps({
        'basis_order': NAMES, 'invariant': serialized_invariant, 'lowering': serialized_image
    }, indent=2)+'\n')
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
