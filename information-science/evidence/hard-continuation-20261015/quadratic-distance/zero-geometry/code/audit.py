#!/usr/bin/env python3
"""Independent exact proof/certificate arithmetic; no producer or solver imports.
Every acceptance check is explicit (not a Python assert), including under -O.
"""
import argparse
from collections import Counter
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]


def require(condition, label):
    if not condition:
        raise ValueError(label)


def q(x):
    return (((x >> 0) & 1) & ((x >> 1) & 1)) ^ (((x >> 2) & 1) & ((x >> 3) & 1))


def d(x):
    return q(x) ^ ((x >> 4) & 1)


def space(vectors):
    result = {0}
    for v in vectors:
        result |= {a ^ v for a in list(result)}
    return sorted(result)


def multiply(columns, x):
    value = 0
    while x:
        i = (x & -x).bit_length() - 1
        value ^= columns[i]
        x &= x - 1
    return value


def low_basis(rows):
    pivots = {}
    for value in rows:
        while value:
            pivot = (value & -value).bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return pivots


def in_span(value, basis):
    for p in sorted(basis):
        if value >> p & 1:
            value ^= basis[p]
    return value == 0


def nullspace(rows, n):
    R = list(rows)
    pivots = []
    used = 0
    for col in range(n):
        index = next((i for i in range(used, len(R)) if R[i] >> col & 1), None)
        if index is None:
            continue
        R[used], R[index] = R[index], R[used]
        for i in range(len(R)):
            if i != used and R[i] >> col & 1:
                R[i] ^= R[used]
        pivots.append(col)
        used += 1
    vectors = []
    for free in range(n):
        if free in pivots:
            continue
        v = 1 << free
        for i, p in enumerate(pivots):
            if R[i] >> free & 1:
                v |= 1 << p
        vectors.append(v)
    return len(pivots), vectors


def greedy_three_spaces(n):
    # Unique successive least-vector basis, not the producer's RREF enumeration.
    for a in range(1, 1 << n):
        for b in range(a + 1, 1 << n):
            if (a ^ b) < b:
                continue
            plane = (0, a, b, a ^ b)
            for c in range(b + 1, 1 << n):
                if any((c ^ v) < c for v in plane):
                    continue
                yield (a, b, c)


def coefficient_word(truth, n):
    # Direct subset sums of truth values, not the producer's in-place transform.
    output = 0
    for mask in range(1 << n):
        parity = 0
        submask = mask
        while True:
            parity ^= (truth >> submask) & 1
            if submask == 0:
                break
            submask = (submask - 1) & mask
        output |= parity << mask
    return output


def degree(truth, n):
    coefficients = coefficient_word(truth, n)
    return max((m.bit_count() for m in range(1 << n) if coefficients >> m & 1), default=-1)


def transform(values):
    N = len(values)
    return [sum(v * (1 if (a & x).bit_count() % 2 == 0 else -1) for a, v in enumerate(values)) for x in range(N)]


def fast_transform(values):
    a = list(values)
    for bit in range((len(a)).bit_length() - 1):
        step = 1 << bit
        for i in range(len(a)):
            if i & step:
                continue
            u, v = a[i], a[i | step]
            a[i], a[i | step] = u + v, u - v
    return a


def eval_polynomial(monomials, coefficients, point):
    return sum((coefficients >> i) & 1 for i, m in enumerate(monomials) if point & m == m) & 1


def classification_audit(data):
    cubics = [m for m in range(256) if m.bit_count() <= 3]
    require(cubics == data['P3_monomial_masks'], 'cubic monomial basis mismatch')
    Q0 = [a for a in range(256) if d(a) == 0]
    require(Q0 == data['D0_points'] and len(Q0) == 128, 'D0 coordinate mismatch')
    monomial_images = [sum(int(a & m == m) << i for i, a in enumerate(Q0)) for m in cubics]
    target_const = sum((1 ^ int(a & 15 == 15)) << i for i, a in enumerate(Q0))
    quartics_Y = [m for m in range(128) if m.bit_count() == 4]
    quartic_index = {m: i for i, m in enumerate(quartics_Y)}
    wedge_rows = []
    for beta in range(128):
        if beta.bit_count() != 2:
            continue
        image = 0
        for term in (3, 12):
            if not (term & beta):
                image ^= 1 << quartic_index[term | beta]
        wedge_rows.append(image)
    wedge = low_basis(wedge_rows)
    require(len(wedge) == 16 and in_span(1 << quartic_index[15], wedge), 'quartic wedge rank mismatch')
    cases = {}
    for record in data['cases']:
        points = tuple(space(record['basis']))
        require(len(points) == 8 and points not in cases, 'duplicate or deficient flat certificate')
        cases[points] = record
    require(len(cases) == 1891, 'flat certificate count mismatch')
    counts, passing, seen = Counter(), Counter(), set()
    all_Y = 0
    representatives = {1: space((1, 4, 32)), 2: space((1, 32, 64)), 3: space((32, 64, 128))}
    for basis in greedy_three_spaces(7):
        all_Y += 1
        Y = space(basis)
        # Direct graph-linearity test, independent of8D subspace enumeration.
        if any(q(a ^ b) != (q(a) ^ q(b)) for a in Y for b in Y):
            continue
        V = tuple(sorted((y & 15) | (q(y) << 4) | ((y >> 4) << 5) for y in Y))
        require(V in cases and V not in seen, 'missing or duplicate graph-flat coverage')
        seen.add(V)
        record = cases[V]
        radical_intersection = [a for a in V if not (a & 15)]
        tau = len(radical_intersection).bit_length() - 1
        require(len(radical_intersection) == 1 << tau and tau == record['tau'], 'radical intersection mismatch')
        counts[tau] += 1
        indicator = sum(1 << y for y in Y)
        coefficients = coefficient_word(indicator, 7)
        require(all(not (coefficients >> m & 1) for m in range(128) if m.bit_count() > 4), 'flat indicator degree mismatch')
        top = sum(((coefficients >> m) & 1) << i for i, m in enumerate(quartics_Y))
        possible = in_span(top ^ (1 << quartic_index[15]), wedge)
        require(possible == record['E_extension_exists'], 'E-extension compatibility mismatch')
        if possible:
            passing[tau] += 1
            coefficients_P = int(record['P3_monomial_coefficient_hex'], 16)
            require(coefficients_P < 1 << 93, 'invalid cubic coefficient width')
            require(all(eval_polynomial(cubics, coefficients_P, a) == (1 ^ int(a in V) ^ int(a & 15 == 15)) for a in Q0), 'invalid cubic E-extension certificate')
        else:
            dual = int(record['dual_refutation_truth_hex'], 16)
            require(0 < dual < 1 << 128, 'invalid dual refutation width')
            require(all((dual & row).bit_count() % 2 == 0 for row in monomial_images), 'invalid dual refutation kernel')
            target = target_const ^ sum(1 << i for i, a in enumerate(Q0) if a in V)
            require((dual & target).bit_count() % 2 == 1, 'invalid dual refutation contradiction')
        columns = record['stabilizer_columns_to_representative']
        require(len(columns) == 8 and len(low_basis(columns)) == 8, 'singular stabilizer certificate')
        mapping = [multiply(columns, a) for a in range(256)]
        require(sorted(mapping) == list(range(256)), 'stabilizer is not bijective')
        require(all(d(a) == d(mapping[a]) for a in range(256)), 'stabilizer does not preserve D')
        require(sorted(mapping[a] for a in V) == representatives[tau], 'stabilizer flat mapping mismatch')
        changed_quartic = sum((int(mapping[a] & 15 == 15) ^ int(a & 15 == 15)) << a for a in range(256))
        require(degree(changed_quartic, 8) <= 3, 'stabilizer does not preserve quartic class')
    require(all_Y == 11811 and all_Y == (127 * 126 * 124) // (7 * 6 * 4), 'incomplete7D subspace enumeration')
    require(seen == set(cases), 'incomplete zero-flat coverage')
    require(dict(counts) == {1: 1680, 2: 210, 3: 1}, 'geometric orbit counts mismatch')
    require(dict(passing) == {2: 210, 3: 1}, '211-flat compatibility count mismatch')
    require(data['all_linear_three_subspaces_F2_8'] == (255 * 254 * 252) // (7 * 6 * 4) == 97155, '8D subspace total mismatch')
    return {'independent_7D_spaces_enumerated': all_Y, 'zero_flats_checked': len(cases),
            'counts_by_tau': dict(counts), 'compatible_by_tau': dict(passing), 'compatible_total': sum(passing.values()),
            'quartic_wedge_rank': len(wedge)}, Q0, cubics


def derivative(word, shift, selected):
    return {((word >> a) ^ (word >> (a ^ shift))) & 1 for a in selected}


def family_audit(family, Q0, cubics):
    # Nullspace of the point-by-monomial matrix, transposed relative to producer.
    evaluation_rows = [sum(int(a & m == m) << j for j, m in enumerate(cubics)) for a in Q0]
    image_rank, coefficient_kernel = nullspace(evaluation_rows, 93)
    require(image_rank == 80 and len(coefficient_kernel) == 13, 'independent cubic kernel dimension mismatch')
    independent_kernel = [sum(eval_polynomial(cubics, coefficients, a) << a for a in range(256)) for coefficients in coefficient_kernel]
    require(len(low_basis(independent_kernel)) == 13, 'independent truth-kernel deficiency')
    supplied = [int(v, 16) for v in family['kernel_truth_hex']]
    require(len(supplied) == 13 and len(low_basis(supplied)) == 13, 'supplied kernel dimension mismatch')
    for word in supplied:
        require(degree(word, 8) <= 3, 'kernel cubic degree mismatch')
        require(all(not (word >> a & 1) for a in Q0), 'kernel does not vanish on D0')
        require(in_span(word, low_basis(independent_kernel)), 'kernel space mismatch')
    tau = family['tau']
    require(tau in (2, 3), 'wrong surviving geometry')
    expected_rep = (1, 32, 64) if tau == 2 else (32, 64, 128)
    Z = space(expected_rep)
    require(Z == family['representative_points'], 'representative flat mismatch')
    K_basis = (32, 64) if tau == 2 else (32, 64, 128)
    require(list(K_basis) == family['K_basis'], 'radical translation basis mismatch')
    E0 = int(family['E0_truth_hex'], 16)
    coefficients = coefficient_word(E0, 8)
    high = [m for m in range(256) if m.bit_count() >= 4 and coefficients >> m & 1]
    require(high == [15], 'quartic Pfaffian mismatch')
    require(all((E0 >> a & 1) == (1 ^ int(a in Z)) for a in Q0), 'particular E extension mismatch')
    D1 = [a for a in range(256) if d(a)]
    for k in K_basis:
        require(derivative(E0, k, D1) == {0}, 'particular E is not K-invariant')
        for word in independent_kernel:
            require(len(derivative(word, k, D1)) == 1, 'kernel lacks constant K-affinity on D1')
    characters = Counter()
    profiles = []
    for parameters in range(8192):
        E = E0
        # Binary order and independently derived coefficient kernel, not Gray order.
        for j, word in enumerate(independent_kernel):
            if parameters >> j & 1:
                E ^= word
        character = 0
        for j, k in enumerate(K_basis):
            values = derivative(E, k, D1)
            require(len(values) == 1, 'E family K-character mismatch')
            character |= next(iter(values)) << j
        characters[character] += 1
        if parameters == 0 or (character and len(profiles) == 1):
            profiles.append((E, character))
    require(sum(characters.values()) == family['E_family_size'] == 8192, 'incomplete E family coverage')
    require(dict(characters) == {int(k): v for k, v in family['character_counts'].items()}, 'E character histogram mismatch')
    lower = len(D1) * 3 ** 2
    upper = (1 << (8 - tau)) * 64 ** 2 // 256
    require(lower == family['projected_energy_lower'] == 1152, 'projection lower energy mismatch')
    require(upper == family['projected_energy_upper'], 'projection energy bound mismatch')
    require(lower > upper, 'projection contradiction lost')
    # Exact sharp upper-bound control: p=64*delta0 is not an admissible
    # magnitude profile, but genuinely has transform bounded by64.
    delta = [64] + [0] * 255
    controls = []
    for beta in range(1 << tau):
        scaled = []
        for a in range(256):
            total = 0
            for c in range(1 << tau):
                k = multiply(K_basis, c)
                total += (-1 if (beta & c).bit_count() & 1 else 1) * delta[a ^ k]
            scaled.append(total)
        energy = Fraction(sum(v * v for v in scaled), (1 << tau) ** 2)
        require(energy == upper, 'sharp projection equality control failed')
        transformed = fast_transform(scaled)
        require(transformed == transform(scaled), 'projection control transform mismatch')
        for x, v in enumerate(transformed):
            restriction = sum(((x & k).bit_count() & 1) << j for j, k in enumerate(K_basis))
            require(v == ((1 << tau) * 64 if restriction == beta else 0), 'projection dual-slice control failed')
        controls.append({'character': beta, 'projected_energy': int(energy)})
    formal = []
    for E, beta in profiles:
        p = [0 if a in Z else (3 if E >> a & 1 else -3) if d(a) else 2 for a in range(256)]
        H = fast_transform(p)
        require(H == transform(p), 'formal profile transform mismatch')
        scaled = []
        for a in range(256):
            scaled.append(sum((-1 if (beta & c).bit_count() & 1 else 1) * p[a ^ multiply(K_basis, c)] for c in range(1 << tau)))
        energy = Fraction(sum(v * v for v in scaled), (1 << tau) ** 2)
        require(energy >= lower and max(map(abs, H)) > 64, 'formal profile failed rejection control')
        formal.append({'character': beta, 'actual_transform_peak': max(map(abs, H)),
                       'projected_energy': str(energy), 'not_a_Boolean_Walsh_pair': True})
    return {'tau': tau, 'independent_restriction_rank': image_rank, 'kernel_dimension': len(independent_kernel),
            'independently_enumerated_E': 8192, 'character_counts': dict(characters),
            'energy_lower': lower, 'energy_upper': upper, 'strict_contradiction': lower > upper,
            'sharp_upper_controls': controls, 'formal_non_witness_rejection_controls': formal}, independent_kernel


def fiber_audit():
    counts = Counter()
    for bits in itertools.product((0, 1), repeat=8):
        W = transform([1 - 2 * b for b in bits])
        require(all(v % 2 == 0 for v in W), '3-variable transform parity error')
        require(len({(v // 2) % 2 for v in W}) == 1, '3-variable Walsh/2 parity not constant')
        if sum(bits) % 2:
            require(not all(v % 4 == 0 for v in W), 'odd sign-table discriminator failed')
            counts['odd_sign_tables'] += 1
            continue
        counts['even_sign_tables'] += 1
        require(degree(sum(b << i for i, b in enumerate(bits)), 3) <= 2, 'even sign table is not quadratic')
        support = [i for i, v in enumerate(W) if v]
        require(len(support) in (1, 4), 'even sign-table support shape mismatch')
        if len(support) == 1:
            require(abs(W[support[0]]) == 8, 'affine sign-table value mismatch')
        else:
            require(all(abs(W[i]) == 4 for i in support), 'quadratic sign-table value mismatch')
            origin = support[0]
            directions = {x ^ origin for x in support}
            require(len(low_basis(directions)) == 2, 'four-support is not an affine two-flat')
            xor = 0
            for x in support:
                xor ^= x
            require(xor == 0, 'affine label-flat XOR failure')
    q5 = [q(a) ^ ((a >> 4) & 1) for a in range(32)]
    zeros, ones = [a for a in range(32) if not q5[a]], [a for a in range(32) if q5[a]]
    require(len(low_basis(zeros)) == len(low_basis(ones)) == 5, 'rank4 quadratic level sets do not span')
    monomials = [m for m in range(32) if m.bit_count() <= 2]
    rows = [sum(int(a & m == m) << i for i, a in enumerate(zeros)) for m in monomials]
    require(len(low_basis(rows)) == 15, 'five-variable quadratic restriction rank mismatch')
    functions = [sum(int(a & m == m) << a for a in range(32)) for m in monomials]
    zero_word = sum(1 << a for a in zeros)
    qword = sum(v << a for a, v in enumerate(q5))
    kernel_words = set()
    value = 0
    for index in range(1 << 16):
        if index:
            value ^= functions[(index & -index).bit_length() - 1]
        if not (value & zero_word):
            kernel_words.add(value)
    require(kernel_words == {0, qword}, 'quadratic vanishing kernel is not {0,q}')
    # Meaningful rank-two countercontrol: q*x0 remains quadratic and
    # vanishes on q=0, but is neither0 norq. The rank-four lemma must not generalize.
    small_q = [((a & 1) * ((a >> 1) & 1)) ^ ((a >> 2) & 1) for a in range(16)]
    small_other = [v * (a & 1) for a, v in enumerate(small_q)]
    require(small_other != [0] * 16 and small_other != small_q, 'rank-two countercontrol trivial')
    require(all(not b for a, b in enumerate(small_other) if not small_q[a]), 'rank-two countercontrol fails vanishing')
    require(degree(sum(b << a for a, b in enumerate(small_other)), 4) <= 2, 'rank-two countercontrol degree mismatch')
    # Genuine balanced6-variable Boolean controls, not hypothetical profiles.
    genuine = []
    for pieces in (1, 2):
        e = [0] * 32
        for y in (0, 1, 2, 3):
            e[y] = -1 if y & 1 else 1
        if pieces == 2:
            for y in (16, 20, 24, 28):
                e[y] = -1 if y >> 2 & 1 else 1
        for flip in (False, True):
            bits = []
            for x in range(64):
                y, z = x & 31, x >> 5
                sign = e[y] if e[y] else (-1 if z else 1) * (-1 if flip and y == 4 else 1)
                bits.append((1 - sign) // 2)
            require(sum(bits) == 32, 'genuine fiber control not balanced')
            W = transform([1 - 2 * b for b in bits])
            require(W == fast_transform([1 - 2 * b for b in bits]), 'genuine fiber transform mismatch')
            sx = 0
            for x, b in enumerate(bits):
                if b:
                    sx ^= x
            require(sx in (0, 32), 'genuine fiber support type error')
            require(all(v % 4 == 0 and (v // 4) % 2 == ((a & sx).bit_count() % 2) for a, v in enumerate(W)), 'balanced fiber residue identity fails')
            require(all(W[a] % 8 == 0 for a in range(32)), 'fiber hyperplane divisibility fails')
            Q = sum(((W[a] // 8) & 1) << a for a in range(32))
            require(degree(Q, 5) <= 2 and not (Q & 1), 'fiber hyperplane residue is not quadratic')
            genuine.append({'support_xor': sx, 'weight': 32, 'hyperplane_quadratic_degree': degree(Q, 5),
                            'full_spectrum_peak': max(map(abs, W))})
    require(16 * 24 ** 2 == 9216 > 4096 == 64 ** 2, 'alternative fiber energy arithmetic mismatch')
    return {'all3_variable_sign_tables': 256, **dict(counts), 'rank4_q0_quadratic_restriction_rank': 15,
            'quadratics_enumerated': 65536, 'vanishing_kernel': 'exactly{0,q}',
            'both_level_sets_span_dimension': 5, 'rank2_countercontrol_passes': True,
            'genuine_balanced6_variable_controls': genuine, 'tau3_energy_lower': 9216, 'fiber_Parseval_energy': 4096}


def carry_audit(data, Q0, cubics):
    recorded = json.loads((ROOT / 'results/carry-probe.json').read_text())
    rows = [sum(int(a & m == m) << j for j, m in enumerate(cubics)) for a in Q0]
    r, coefficient_kernel = nullspace(rows, 93)
    require(r == 80, 'carry independent E-kernel rank mismatch')
    kernel = [sum(eval_polynomial(cubics, coefficients, a) << a for a in range(256)) for coefficients in coefficient_kernel]
    moments = [sum(int(a & m == m) << a for a in range(256)) for m in cubics]
    Dword = sum(d(a) << a for a in range(256))
    complete = []
    for family in data['canonical_families']:
        Z = set(family['representative_points'])
        free = [a for a in Q0 if a not in Z]
        moment_rows = [sum(int(a & m == m) << j for j, a in enumerate(free)) for m in cubics]
        # Nullspace of the transpose gives dependencies independently of
        # the producer's augmented-row elimination.
        columns = [sum(((row >> j) & 1) << i for i, row in enumerate(moment_rows)) for j in range(len(free))]
        rank_moments, dependencies = nullspace(columns, 93)
        require(rank_moments == 79 and len(dependencies) == 14, 'carry moment rank mismatch')
        passing = 0
        for parameters in range(8192):
            E = int(family['E0_truth_hex'], 16)
            for j, v in enumerate(kernel):
                if parameters >> j & 1:
                    E ^= v
            fixed_F = Dword & (((1 << 256) - 1) ^ E)
            rhs = 0
            for i, moment in enumerate(moments):
                numerator = (Dword & moment).bit_count() + 2 * (E & moment).bit_count()
                require(numerator % 4 == 0, 'carry numerator integrality mismatch')
                value = ((numerator // 4) & 1) ^ ((fixed_F & moment).bit_count() & 1)
                rhs |= value << i
            if all((rhs & dep).bit_count() % 2 == 0 for dep in dependencies):
                passing += 1
        require(passing == 8192, 'carry probe compatibility count mismatch')
        old = next(v for v in recorded['results'] if v['tau'] == family['tau'])
        require(old['moment_matrix_rank'] == rank_moments and old['E_passing_parity_test'] == passing, 'carry probe receipt mismatch')
        require(old['remaining_F_parity_dimension'] == len(free) - rank_moments == 41, 'carry parity dimension mismatch')
        complete.append({'tau': family['tau'], 'independently_checked_E': passing,
                         'moment_rank': rank_moments, 'remaining_F_parity_dimension': 41,
                         'not_used_in_exclusion': True})
    return complete


def one_zero_corollary_audit():
    pairs = 0
    for a in range(256):
        for b in range(a + 1, 256):
            require(a ^ b != 0, 'two distinct zero points have zero XOR')
            pairs += 1
    require(pairs == 32640, 'two-point zero-set coverage mismatch')
    minimum_control = (0, 1, 2, 3)
    value = 0
    for a in minimum_control:
        value ^= a
    require(len(minimum_control) == 4 and value == 0, 'four-point moment control mismatch')
    # Actual relaxed peak32 Boolean table: checks the linear-shift identity,
    # not existence or attainment of a one-zero extremizer.
    bits = []
    for x in range(512):
        bit = x & 1
        for i in (1, 3, 5, 7):
            bit ^= ((x >> i) & 1) * ((x >> (i + 1)) & 1)
        bits.append(bit)
    W = transform([1 - 2 * b for b in bits])
    require(W == fast_transform([1 - 2 * b for b in bits]), 'nine-variable shift-control transform mismatch')
    require(max(map(abs, W)) == 32 and sum(bits) == 256, 'relaxed peak32 control mismatch')
    zeros = [a for a, v in enumerate(W) if v == 0]
    selected = zeros[:2] + [next(a for a, v in enumerate(W) if v != 0)]
    shifts = []
    for shift in selected:
        shifted = [b ^ ((x & shift).bit_count() & 1) for x, b in enumerate(bits)]
        spectrum = fast_transform([1 - 2 * b for b in shifted])
        require(spectrum == [W[a ^ shift] for a in range(512)], 'linear output shift did not permute spectrum')
        require(sum(v == 0 for v in spectrum) == len(zeros), 'linear shift changed Walsh zero count')
        require((sum(shifted) == 256) == (W[shift] == 0), 'zero-to-balance shift equivalence failed')
        shifts.append({'shift': shift, 'balanced': sum(shifted) == 256, 'zero_count': len(zeros), 'peak': 32})
    require(all(((-2 * w) % 4 == 0) == (w % 2 == 0) for w in range(513)), 'zero implies even-weight modular check failed')
    return {'distinct_two_point_sets_checked': pairs, 'nonempty_even_XOR0_minimum': 4,
            'positive_four_point_set_control': list(minimum_control), 'linear_shift_controls': shifts,
            'one_to_three_Walsh_zeros_implies_peak_at_least': 32,
            'one_to_three_Walsh_zeros_implies_NL_at_most': 240,
            'uses_new_rank4_type_exclusion': False, 'one_zero_attainment_claim': False,
            'priority': 'UNRESOLVED; CMB2026/037 abstract context only, full text not checked'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--corrupt-classification', action='store_true')
    ap.add_argument('--corrupt-kernel', action='store_true')
    ap.add_argument('--corrupt-projection', action='store_true')
    args = ap.parse_args()
    started = time.monotonic()
    raw = (ROOT / 'results/classification.json.gz').read_bytes()
    data = json.loads(gzip.decompress(raw))
    for name, pin in data['source_pins'].items():
        source = (ROOT / 'inputs' / name).read_bytes()
        require(hashlib.sha256(source).hexdigest() == pin['sha256'] and len(source) == pin['bytes'], 'source pin mismatch')
    if args.corrupt_classification:
        next(c for c in data['cases'] if c['tau'] == 1)['E_extension_exists'] = True
    if args.corrupt_kernel:
        family = data['canonical_families'][0]
        word = int(family['kernel_truth_hex'][0], 16)
        # D*k0*k1 still vanishes on D0, but has forbidden quartics and
        # non-affine K-dependence. A restriction-only check would miss it.
        added = sum((d(a) * ((a >> 5) & 1) * ((a >> 6) & 1)) << a for a in range(256))
        family['kernel_truth_hex'][0] = hex(word ^ added)
    if args.corrupt_projection:
        data['canonical_families'][0]['projected_energy_upper'] = 2048
    geometry, Q0, cubics = classification_audit(data)
    families = []
    for family in data['canonical_families']:
        audited, independent_kernel = family_audit(family, Q0, cubics)
        families.append(audited)
    fibers = fiber_audit()
    carry = carry_audit(data, Q0, cubics)
    one_zero = one_zero_corollary_audit()
    review = json.loads((ROOT / 'inputs/parent-candidate-review.json').read_text())
    parent_audit = json.loads((ROOT / 'inputs/parent-candidate-audit.json').read_text())
    require(review['review']['verdict'] == 'correct-with-fixes', 'unexpected imported premise review status')
    require(parent_audit['status'] == 'PASS' and parent_audit['vector_controls'] == 601, 'imported audit receipt mismatch')
    require(parent_audit['candidate_sha256'] == data['source_pins']['odd-pair-codex-attempt.txt']['sha256'], 'reviewed candidate pin mismatch')
    out = {'status': 'PASS', 'scope': 'Independent finite geometry/kernel/projection audit, not a global nonexistence proof.',
           'classification': geometry, 'families': families, 'alternative_tau3_fiber_audit': fibers,
           'discarded_carry_route_independent_audit': carry,
           'one_to_three_zero_corollary_audit': one_zero,
           'imported_premises': 'CORRECT-WITH-FIXES review; errata applied in PROOF.md; new exclusion awaits fresh proof review.',
           'new_claim': 'Assuming the reviewed zero-set/magnitude and next-bit lemmas, balanced(rank4,weight128) is impossible.',
           'other_residue_types_excluded': 0, 'formal_verification': False,
           'classification_sha256': hashlib.sha256(raw).hexdigest(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - started}
    (ROOT / 'results/audit.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': out['status'], 'compatible_flats': geometry['compatible_total'],
                      'family_E_sizes': [f['independently_enumerated_E'] for f in families],
                      'projection_bounds': [[f['energy_lower'], f['energy_upper']] for f in families],
                      'elapsed_seconds': out['elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
