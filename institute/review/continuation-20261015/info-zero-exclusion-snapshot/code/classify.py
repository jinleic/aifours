#!/usr/bin/env python3
"""Exact97155-flat E-extension classification, orbit maps,13-bit families and energy data.
This is necessary-condition evidence, conditional on the pinned candidate lemmas.
"""
from collections import Counter
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
ALL = (1 << 256) - 1
CUBICS = [m for m in range(256) if m.bit_count() <= 3]
REPS = {1: (1, 4, 32), 2: (1, 32, 64), 3: (32, 64, 128)}


def q(u):
    return ((u & 1) * ((u >> 1) & 1)) ^ (((u >> 2) & 1) * ((u >> 3) & 1))


def D(a):
    return q(a & 15) ^ ((a >> 4) & 1)


def apply(columns, x):
    y = 0
    for j, c in enumerate(columns):
        if x >> j & 1:
            y ^= c
    return y


def span(basis):
    points = [0]
    for v in basis:
        points += [x ^ v for x in points]
    return sorted(points)


def rank(rows):
    basis = {}
    for v in rows:
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def basis_of(points):
    result = []
    for v in sorted(points):
        if rank(result + [v]) > len(result):
            result.append(v)
    return result


def subspaces_3(n):
    for pivots in itertools.combinations(range(n), 3):
        pivots = tuple(reversed(pivots))
        free = [[j for j in range(p) if j not in pivots] for p in pivots]
        choices = [[(1 << p) | sum(((m >> i) & 1) << b for i, b in enumerate(free[k]))
                    for m in range(1 << len(free[k]))] for k, p in enumerate(pivots)]
        yield from itertools.product(*choices)


def image_basis(rows):
    pivots = {}
    for i, row in enumerate(rows):
        combination = 1 << i
        for p in sorted(pivots, reverse=True):
            if row >> p & 1:
                row ^= pivots[p][0]
                combination ^= pivots[p][1]
        if row:
            p = row.bit_length() - 1
            for j, (v, c) in list(pivots.items()):
                if v >> p & 1:
                    pivots[j] = (v ^ row, c ^ combination)
            pivots[p] = (row, combination)
    return pivots


def solve_image(target, pivots):
    combination = 0
    for p in sorted(pivots, reverse=True):
        if target >> p & 1:
            target ^= pivots[p][0]
            combination ^= pivots[p][1]
    return combination if target == 0 else None


def monomial_word(mask, n=8):
    return sum(int(a & mask == mask) << a for a in range(1 << n))


def anf(word, n=8):
    values = [(word >> a) & 1 for a in range(1 << n)]
    step = 1
    while step < len(values):
        for base in range(0, len(values), 2 * step):
            for j in range(step):
                values[base + step + j] ^= values[base + j]
        step *= 2
    return [a for a, bit in enumerate(values) if bit]


def polar(x, y):
    return (((x & 1) * ((y >> 1) & 1)) ^ (((x >> 1) & 1) * (y & 1)) ^
            (((x >> 2) & 1) * ((y >> 3) & 1)) ^ (((x >> 3) & 1) * ((y >> 2) & 1)))


def symplectic4():
    result = []
    for a in range(1, 16):
        for b in range(1, 16):
            if polar(a, b) != 1:
                continue
            orthogonal = [v for v in range(1, 16) if not polar(a, v) and not polar(b, v)]
            for c in orthogonal:
                for d in orthogonal:
                    if polar(c, d):
                        result.append((a, b, c, d))
    assert len(result) == len(set(result)) == 720
    return sorted(result)


def gl3():
    result = [cols for cols in itertools.product(range(1, 8), repeat=3) if rank(cols) == 3]
    assert len(result) == 168
    return result


def orbit_map(points, tau, symplectic, linear3, cache):
    S = sorted({x & 15 for x in points})
    T = sorted({x >> 5 for x in points if x & 15 == 0})
    target_S = span((1, 4) if tau == 1 else (1,) if tau == 2 else ())
    target_T = span((1,) if tau == 1 else (1, 2) if tau == 2 else (1, 2, 4))
    key = ('M', tuple(S))
    if key not in cache:
        cache[key] = next(m for m in symplectic if sorted(apply(m, u) for u in S) == target_S)
    M = cache[key]
    key = ('N', tuple(T))
    if key not in cache:
        cache[key] = next(m for m in linear3 if sorted(apply(m, k) for k in T) == target_T)
    N = cache[key]
    S_basis = basis_of(S)
    U_basis = list(S_basis)
    for v in range(1, 16):
        if len(U_basis) == 4:
            break
        if rank(U_basis + [v]) > len(U_basis):
            U_basis.append(v)
    F_images = []
    for u in S_basis:
        k = min(x >> 5 for x in points if x & 15 == u)
        F_images.append(apply(N, k))
    F_images += [0] * (4 - len(F_images))
    F = {apply(U_basis, c): apply(F_images, c) for c in range(16)}
    def A(a):
        u, z, k = a & 15, (a >> 4) & 1, a >> 5
        transformed_u = apply(M, u)
        return transformed_u | ((z ^ q(transformed_u) ^ q(u)) << 4) | ((apply(N, k) ^ F[u]) << 5)
    columns = [A(1 << i) for i in range(8)]
    assert rank(columns) == 8
    assert all(A(a) == apply(columns, a) and D(A(a)) == D(a) for a in range(256))
    assert sorted(A(a) for a in points) == span(REPS[tau])
    return columns


def translate_word(word, input_bit):
    low = sum(((1 << input_bit) - 1) << start for start in range(0, 256, 2 * input_bit))
    high = ALL ^ low
    return ((word & low) << input_bit) | ((word & high) >> input_bit)


def canonical_family(tau, Dword):
    if tau == 3:
        E0 = sum(int(a & 15 != 0) << a for a in range(256))
        K_basis = [32, 64, 128]
    else:
        E0 = 0
        for a in range(256):
            indicator = int(a & (2 | 4 | 8 | 128) == 0)
            beta = (((a >> 1) & 1) * ((a >> 7) & 1)) ^ ((a & 1) * ((a >> 1) & 1))
            E0 |= (1 ^ indicator ^ (D(a) * beta)) << a
        K_basis = [32, 64]
    B_monomials = [[0], [1], [2], [4], [8], [32], [64], [128], [5], [9], [6], [10], [3, 12]]
    B_words = []
    for polynomial in B_monomials:
        value = 0
        for monomial in polynomial:
            value ^= monomial_word(monomial)
        B_words.append(value)
    kernel = [Dword & b for b in B_words]
    assert rank(kernel) == 13
    assert all(max((m.bit_count() for m in anf(v)), default=-1) <= 3 for v in kernel)
    expected_quartic = [15]
    assert [m for m in anf(E0) if m.bit_count() >= 4] == expected_quartic
    counts = Counter()
    E = E0
    digest = hashlib.sha256()
    for index in range(8192):
        if index:
            E ^= kernel[(index & -index).bit_length() - 1]
        character = 0
        for j, k in enumerate(K_basis):
            difference = (E ^ translate_word(E, k)) & Dword
            assert difference in (0, Dword)
            if difference:
                character |= 1 << j
        counts[character] += 1
        digest.update(E.to_bytes(32, 'little') + bytes([character]))
    return {'tau': tau, 'representative_basis': REPS[tau], 'representative_points': span(REPS[tau]),
            'K_basis': K_basis, 'E0_truth_hex': hex(E0), 'B_polynomials_monomial_masks': B_monomials,
            'kernel_truth_hex': [hex(v) for v in kernel], 'kernel_dimension': 13,
            'E_family_size': 8192, 'all_D1_character_alignment_checked': True,
            'character_counts': dict(sorted(counts.items())), 'gray_enumeration_sha256': digest.hexdigest(),
            'D1_points': Dword.bit_count(), 'projected_energy_lower': 128 * 9,
            'fourier_slice_size': 1 << (8 - tau), 'projected_energy_upper': (1 << (8 - tau)) * 64 ** 2 // 256,
            'projection_contradiction': 128 * 9 > (1 << (8 - tau)) * 64 ** 2 // 256}


def main():
    started = time.monotonic()
    pins = {}
    for name in ('odd-pair-codex-attempt.txt', 'quadratic-distance-PROOF.txt', 'quadratic-distance-SHARPER.txt'):
        raw = (ROOT / 'inputs' / name).read_bytes()
        pins[name] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    Q0 = [a for a in range(256) if D(a) == 0]
    index_of = {a: i for i, a in enumerate(Q0)}
    rows = [sum(int(a & m == m) << i for i, a in enumerate(Q0)) for m in CUBICS]
    image = image_basis(rows)
    assert len(image) == 80
    dual = []
    for f in range(128):
        if f in image:
            continue
        word = 1 << f
        for p, (row, combination) in image.items():
            if row >> f & 1:
                word |= 1 << p
        assert all((word & row).bit_count() % 2 == 0 for row in rows)
        dual.append(word)
    assert len(dual) == 48
    F4 = sum(int(a & 15 == 15) << i for i, a in enumerate(Q0))
    group4, group3, cache = symplectic4(), gl3(), {}
    all_count, cases = 0, []
    for basis in subspaces_3(8):
        all_count += 1
        points = span(basis)
        if any(D(a) for a in points):
            continue
        radical_intersection = [a for a in points if a & 15 == 0]
        tau = (len(radical_intersection)).bit_length() - 1
        assert tau in (1, 2, 3)
        target = ((1 << 128) - 1) ^ F4 ^ sum(1 << index_of[a] for a in points)
        combination = solve_image(target, image)
        record = {'basis': basis, 'tau': tau, 'stabilizer_columns_to_representative': orbit_map(points, tau, group4, group3, cache),
                  'E_extension_exists': combination is not None}
        if combination is not None:
            record['P3_monomial_coefficient_hex'] = hex(combination)
        else:
            witness = next(word for word in dual if (word & target).bit_count() & 1)
            record['dual_refutation_truth_hex'] = hex(witness)
        cases.append(record)
    assert all_count == 97155 and len(cases) == 1891
    by_tau = Counter(c['tau'] for c in cases)
    passed = Counter(c['tau'] for c in cases if c['E_extension_exists'])
    assert by_tau == {1: 1680, 2: 210, 3: 1} and passed == {2: 210, 3: 1}
    Dword = sum(D(a) << a for a in range(256))
    families = [canonical_family(tau, Dword) for tau in (2, 3)]
    out = {'scope': 'Necessary zero-flat/E classification and conditional balanced(4,128) exclusion; profiles are not Boolean functions.',
           'candidate_dependency_status': 'UNVERIFIED_CANDIDATE_PENDING_PARENT_REVIEW', 'source_pins': pins,
           'normal_form': 'D=a0*a1+a2*a3+a4; K=span(e5,e6,e7)',
           'coordinates': ['u0', 'u1', 'u2', 'u3', 'z', 'k0', 'k1', 'k2'],
           'D0_points': Q0, 'P3_monomial_masks': CUBICS, 'all_linear_three_subspaces_F2_8': all_count,
           'D0_linear_three_flats': len(cases), 'RM3_restriction_rank': len(image), 'RM3_restriction_kernel_dimension': 13,
           'counts_by_tau': dict(by_tau), 'E_extension_counts_by_tau': dict(passed),
           'E_extension_compatible_flats': sum(passed.values()), 'symplectic4_matrices': len(group4), 'GL3_matrices': len(group3),
           'cases': cases, 'canonical_families': families, 'elapsed_seconds': time.monotonic() - started}
    raw = (json.dumps(out, separators=(',', ':')) + '\n').encode()
    path = ROOT / 'results/classification.json.gz'
    assert not path.exists(), 'Preserve the existing completed classification.'
    path.write_bytes(gzip.compress(raw, mtime=0))
    print(json.dumps({k: out[k] for k in ('all_linear_three_subspaces_F2_8', 'D0_linear_three_flats', 'counts_by_tau', 'E_extension_counts_by_tau', 'RM3_restriction_rank', 'elapsed_seconds')}, sort_keys=True))


if __name__ == '__main__':
    main()
