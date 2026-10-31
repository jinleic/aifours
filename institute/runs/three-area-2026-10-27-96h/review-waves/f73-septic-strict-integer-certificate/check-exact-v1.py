#!/usr/bin/env python3
"""Independent exact controls for the f73 review; no source code is imported.

This is a finite replay, not a proof search and not a negative-witness fixture.
All arithmetic is integer or Fraction; stdout is a reproducible JSON receipt.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, prod
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def corners(lo, hi):
    result = []
    for even_high, odd_high in ((0, 0), (0, 1), (1, 0), (1, 1)):
        a = []
        for j in range(7):
            high_for_minimum = (j // 2) % 2
            high = high_for_minimum ^ (even_high if j % 2 == 0 else odd_high)
            a.append(hi[j] if high else lo[j])
        result.append(a + [1])
    return result


def coeff_vector_t(a, t):
    """Raw pairing at w^2=t, indexed by ascending numerator degree."""
    return [sum(((-1 if ((k - j) // 2) % 2 else 1) * a[j]
                 * t ** ((j + k) // 2))
                for j in range(8) if (j + k) % 2 == 0)
            for k in range(8)]


def compact_vector(a, x):
    return [sum(((-1 if ((k - j) // 2) % 2 else 1) * a[j]
                 * x ** ((j + k) // 2) * (1 - x) ** (7 - (j + k) // 2))
                for j in range(8) if (j + k) % 2 == 0)
            for k in range(8)]


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def eval_complex(a, z):
    acc = (Q(0), Q(0))
    for coeff in reversed(a):
        r, i = mul(acc, z)
        acc = (r + coeff, i)
    return acc


def pairing_by_horner(a, b, w):
    return mul(eval_complex(b, (Q(0), w)), eval_complex(a, (Q(0), -w)))[0]


def det_bareiss(matrix):
    n = len(matrix)
    a = [list(row) for row in matrix]
    sign, old = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                require(num % old == 0, 'non-exact Bareiss division')
                a[i][j] = num // old
            a[i][k] = 0
        old = pivot
    return sign * a[-1][-1]


def det_permutations(matrix):
    n = len(matrix)
    total = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        total += (-1 if inversions % 2 else 1) * prod(matrix[i][p[i]] for i in range(n))
    return total


def det_fraction(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    answer = Q(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            answer = -answer
        d = a[k][k]
        answer *= d
        for i in range(k + 1, len(a)):
            ratio = a[i][k] / d
            for j in range(k + 1, len(a)):
                a[i][j] -= ratio * a[k][j]
    return answer


def hurwitz_minors(a, crosscheck=False):
    c = list(reversed(a))
    def coeff(index):
        return c[index] if 0 <= index < 8 else 0
    result = []
    for n in range(1, 8):
        h = [[coeff(2 * q - p) for q in range(1, n + 1)] for p in range(1, n + 1)]
        value = det_bareiss(h)
        if crosscheck:
            require(value == det_permutations(h), 'Hurwitz determinant disagreement')
        result.append(value)
    return result


def raw_sums(cs, frequencies, weights, indices):
    out = [0] * 8
    for w, weight, ix in zip(frequencies, weights, indices):
        vec = coeff_vector_t(cs[ix], w * w)
        out = [x + weight * y for x, y in zip(out, vec)]
    return out


def integer(x):
    return type(x) is int


def certificate_reason(lo, hi, frequencies, weights, indices):
    if not (len(lo) == len(hi) == 7 and len(frequencies) == len(weights) == len(indices) == 8):
        return 'shape'
    if any(not integer(x) or x <= 0 for x in lo + hi):
        return 'endpoint-not-positive-integer'
    if any(l >= u for l, u in zip(lo, hi)):
        return 'width-not-positive'
    if any(not integer(w) or w <= 0 for w in frequencies):
        return 'frequency-not-positive-integer'
    if len(set(frequencies)) != 8:
        return 'frequency-not-distinct'
    if any(not integer(n) or n <= 0 for n in weights):
        return 'weight-not-positive-integer'
    if any(not integer(ix) or not 0 <= ix < 4 for ix in indices):
        return 'corner-index'
    cs = corners(lo, hi)
    if any(d <= 0 for a in cs for d in hurwitz_minors(a)):
        return 'corner-not-hurwitz'
    if any(c >= 0 for c in raw_sums(cs, frequencies, weights, indices)):
        return 'coefficient-not-strictly-negative'
    return 'VALID_NEGATIVE_CERTIFICATE'


def main():
    # Actual box centered at (s+10)^7, independently varied by +/-1 per coefficient.
    center = [comb(7, j) * 10 ** (7 - j) for j in range(8)]
    lo = [x - 1 for x in center[:7]]
    hi = [x + 1 for x in center[:7]]
    cs = corners(lo, hi)
    freqs, weights, ids = list(range(1, 9)), list(range(1, 9)), [0, 1, 2, 3] * 2
    determinants = [hurwitz_minors(a, crosscheck=True) for a in cs]
    require(all(d > 0 for group in determinants for d in group), 'sample corner is not Hurwitz')
    require(all(group[-1] == a[0] * group[-2] for group, a in zip(determinants, cs)),
            'septic determinant orientation')
    sums = raw_sums(cs, freqs, weights, ids)
    direct_terms = [n * pairing_by_horner(cs[i], center, Q(w))
                    for w, n, i in zip(freqs, weights, ids)]
    require(all(x > 0 for x in direct_terms), 'positive sample pairing')
    require(sum(direct_terms) == sum(c * b for c, b in zip(sums, center)),
            'weighted direct pairing mismatch')

    # Direct complex Horner vs the parity expansion, including w=0.
    for a in cs:
        for w in map(Q, range(9)):
            vec = coeff_vector_t(a, w * w)
            require(sum(v * b for v, b in zip(vec, center)) == pairing_by_horner(a, center, w),
                    'raw pairing formula')
            for k in range(8):
                monomial = [0] * 8
                monomial[k] = 1
                require(vec[k] == pairing_by_horner(a, monomial, w), 'monomial orientation')
            x = w * w / (1 + w * w)
            require(compact_vector(a, x) == [v / (1 + w * w) ** 7 for v in vec],
                    'compactification identity')
        require(compact_vector(a, Q(0)) == [a[0]] + [0] * 7, 'zero endpoint')
        require(compact_vector(a, Q(1)) == [0] * 7 + [1], 'infinity endpoint')

    # Rational input: S_6 maps a rational box back to the integer sample.
    D = 6
    rational_corners = [[Q(v, D ** (7 - j)) for j, v in enumerate(a)] for a in cs]
    rational_b = [Q(v, D ** (7 - j)) for j, v in enumerate(center)]
    rational_freqs = [Q(w, D) for w in freqs]
    rational_sums = raw_sums(rational_corners, rational_freqs, weights, ids)
    for a, original in zip(cs, rational_corners):
        require([D ** (7 - j) * v for j, v in enumerate(original)] == a, 'endpoint scaling')
        for W in freqs:
            w = Q(W, D)
            before = coeff_vector_t(original, w * w)
            after = coeff_vector_t(a, Q(W * W))
            require(after == [D ** (7 + k) * v for k, v in enumerate(before)],
                    'individual pairing coefficient scaling')
            require(pairing_by_horner(a, center, Q(W)) == D ** 14 * pairing_by_horner(original, rational_b, w),
                    'full numerator pairing scaling')
    require(sums == [D ** (7 + k) * v for k, v in enumerate(rational_sums)], 'sum scaling')

    # Four distinct old positive-frequency actual members in ONE enlarged box.
    ts = [1, 4, 9, 16]
    lambdas = [Q(1, 10), Q(2, 10), Q(3, 10), Q(4, 10)]
    us, vs = [1, -1, 1, -1], [-1, 1, 1, -1]
    c = [lam / (1 + t) ** 7 for lam, t in zip(lambdas, ts)]
    even = [[c[j] * (-1) ** k * ts[j] ** k for j in range(4)] for k in range(4)]
    odd = [[c[j] * (-1) ** k * ts[j] ** (k + 1) for j in range(4)] for k in range(4)]
    vander = prod(ts[j] - ts[i] for i in range(4) for j in range(i + 1, 4))
    even_det, odd_det = det_fraction(even), det_fraction(odd)
    require(even_det == prod(c) * vander != 0, 'even Vandermonde')
    require(odd_det == prod(c) * vander * prod(ts) != 0, 'odd Vandermonde')
    delta = [Q(0)] * 8
    for t, lam, u, v in zip(ts, lambdas, us, vs):
        before = center[:]
        after = center[:]
        after[0] += u
        after[1] += v
        require(all(lo[j] <= after[j] <= hi[j] for j in range(7)), 'perturbed member outside box')
        x = Q(t, 1 + t)
        bv, av = compact_vector(before, x), compact_vector(after, x)
        delta = [d + lam * (aa - bb) for d, aa, bb in zip(delta, av, bv)]
    for k in range(4):
        require(delta[2*k] == sum(even[k][j] * us[j] for j in range(4)), 'even perturbation')
        require(delta[2*k+1] == sum(odd[k][j] * vs[j] for j in range(4)), 'odd perturbation')

    controls = {}
    def reject(name, expected, l=lo, h=hi, f=freqs, n=weights, ii=ids):
        actual = certificate_reason(l, h, f, n, ii)
        require(actual == expected, name + ': expected ' + expected + ', got ' + actual)
        controls[name] = actual
    reject('ordinary_positive_box_and_atoms', 'coefficient-not-strictly-negative')
    reject('duplicate_frequency', 'frequency-not-distinct', f=[1, 1, 3, 4, 5, 6, 7, 8])
    reject('zero_frequency', 'frequency-not-positive-integer', f=[0, 2, 3, 4, 5, 6, 7, 8])
    reject('zero_weight', 'weight-not-positive-integer', n=[0, 2, 3, 4, 5, 6, 7, 8])
    reject('out_of_range_corner', 'corner-index', ii=[4, 1, 2, 3, 0, 1, 2, 3])
    reject('zero_width', 'width-not-positive', h=[lo[0]] + hi[1:])
    reject('nonpositive_endpoint', 'endpoint-not-positive-integer', l=[0] + lo[1:])
    reject('unstable_positive_integer_box', 'corner-not-hurwitz', l=[1]*7, h=[2]*7)

    print(json.dumps({
        'result': 'EXACT_CONTROLS_PASSED',
        'not_a_negative_witness': True,
        'box': {'lo': lo, 'hi': hi, 'center_ascending': center,
                'all_member_common_numerator_reason': '|a(iw)-b(iw)|/|b(iw)| <= 7/10 < 1; b=(s+10)^7'},
        'corners_ascending': cs,
        'four_by_seven_determinants': [[str(x) for x in row] for row in determinants],
        'determinant_replay': 'Bareiss equals independent permutation expansion for all 28',
        'frequencies': freqs, 'weights': weights, 'corner_indices_zero_based': ids,
        'pairing_sums_ascending': [str(x) for x in sums],
        'positive_direct_pairing_terms': [str(x) for x in direct_terms],
        'direct_weighted_pairing': str(sum(direct_terms)),
        'monomial_Horner_checks': 4 * 9 * 8,
        'zero_infinity_checks': 'four corners each; V(0)=a0 e0, V(1)=e7',
        'scaling': {'D': D, 'rational_frequencies': [str(x) for x in rational_freqs],
                    'result': 'individual and summed C_k scaled by D^(7+k); full numerator pairing by D^14'},
        'perturbation': {'t': ts, 'weights': [str(x) for x in lambdas],
                         'u': us, 'v': vs, 'even_det': str(even_det), 'odd_det': str(odd_det),
                         'delta': [str(x) for x in delta], 'same_positive_width_box': True},
        'intended_rejection_controls': controls,
        'limits': 'Finite arithmetic controls only. Neither a negative search nor a universal synthesis proof.'
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
