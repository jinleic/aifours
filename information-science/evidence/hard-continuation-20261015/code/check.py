#!/usr/bin/env python3
"""Independent direct-character audit; imports no producer or solver module."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import random
import time

ROOT = Path(__file__).resolve().parents[1]
PIN = '200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d'
BASIS = [0] + [1 << j for j in range(8)] + [(1 << j) + (1 << k) for k in range(8) for j in range(k)]
CHAR = [[(-1 if (a & x).bit_count() & 1 else 1) for x in range(256)] for a in range(256)]


def direct(values):
    return [sum(s * v for s, v in zip(row, values)) for row in CHAR]


def qvalue(coefficients, b, monomials):
    return sum((coefficients >> i & 1) for i, monomial in enumerate(monomials) if b & monomial == monomial) % 2


def row(b):
    return sum(1 << k for k, monomial in enumerate(BASIS) if b & monomial == monomial)


def independent_kernel(points):
    # Lowest-column pivots, independent of the producer's highest-bit reduction.
    equations = [row(b) for b in points]
    current = 0
    pivots = []
    for col in range(37):
        pick = next((i for i in range(current, len(equations)) if equations[i] >> col & 1), None)
        if pick is None:
            continue
        equations[pick], equations[current] = equations[current], equations[pick]
        for i in range(len(equations)):
            if i != current and equations[i] >> col & 1:
                equations[i] ^= equations[current]
        pivots.append(col)
        current += 1
    free = [i for i in range(37) if i not in pivots]
    vectors = []
    for col in free:
        v = 1 << col
        for i, p in enumerate(pivots):
            if equations[i] >> col & 1:
                v |= 1 << p
        vectors.append(v)
    words = {0}
    for v in vectors:
        words |= {w ^ v for w in words}
    return len(pivots), words


def pull_half(text, normal):
    pivot = (normal & -normal).bit_length() - 1
    coords = [j for j in range(9) if j != pivot]
    pts = []
    for y in range(256):
        x = sum(((y >> i) & 1) << j for i, j in enumerate(coords))
        x |= (((x & normal).bit_count() & 1) << pivot)
        assert (normal & x).bit_count() % 2 == 0
        pts.append(x)
    return [int(text[x]) for x in pts], [int(text[x ^ (1 << pivot)]) for x in pts]


def classify(m):
    assert m % 4 == 2
    return ((m * m - 4) // 32) % 2


def canonical(m):
    assert m % 4 == 2
    return m * (1 if m % 8 == 2 else -1)


def audit_odd_table(bits, advertised=None):
    assert len(bits) == 256 and sum(bits) % 2
    H = direct([1 - 2 * b for b in bits])
    if advertised is not None:
        assert H == advertised, 'direct spectrum mismatch'
    assert sum(h * h for h in H) == 65536
    support = [x for x, b in enumerate(bits) if b]
    w = len(support)
    counts = [sum(x >> i & 1 for x in support) for i in range(8)]
    linear = [(c * (c - 1) // 2 + ((1 - w) // 2) * c) % 2 for c in counts]
    cross = {(i, j): ((counts[i] * counts[j]) + sum(((x >> i) & 1) * ((x >> j) & 1) for x in support)) % 2 for i in range(8) for j in range(i + 1, 8)}
    for a, h in enumerate(H):
        expected = (w * w - 1) // 8
        expected += sum(linear[i] * (a >> i & 1) for i in range(8))
        expected += sum(c * (a >> i & 1) * (a >> j & 1) for (i, j), c in cross.items())
        assert classify(abs(h)) == expected % 2, 'quadratic support-moment identity'
    K = [canonical(abs(h)) for h in H]
    inverse = direct(K)
    assert set(inverse) <= {-256, 256}, 'canonical inverse not Boolean'
    sx = 0
    for x in support:
        sx ^= x
    epsilon = (-1) ** ((w + 1) // 2)
    assert inverse == [epsilon * 256 * (1 - 2 * bits[x ^ sx]) for x in range(256)]
    squares = direct([h * h for h in H])
    for d in range(1, 256):
        ac = sum((1 - 2 * bits[x]) * (1 - 2 * bits[x ^ d]) for x in range(256))
        assert ac % 8 == 4 and squares[d] == 256 * ac
    return H


def controls(data, classes):
    # Direct-model controls independently evaluate the universal lemmas.
    rng = random.Random(202610150403)
    tables = []
    for w in (1, 3, 63, 127, 129, 191, 253, 255):
        chosen = set(rng.sample(range(256), w))
        tables.append([int(x in chosen) for x in range(256)])
    corrupt_rejected = 0
    for bits in tables:
        H = audit_odd_table(bits)
        corrupt = H.copy()
        corrupt[17] += 8
        try:
            audit_odd_table(bits, corrupt)
        except AssertionError as exc:
            assert str(exc) == 'direct spectrum mismatch'
            corrupt_rejected += 1
        else:
            raise AssertionError('corrupt spectrum accepted')
    # Every original source is a planted balanced bound-32 completion in its
    # fixed-half class.  These are genuine full models, not relaxed CNF models.
    planted = 0
    for case in classes:
        text = data['sources'][case['source']]['bits']
        g, h = pull_half(text, case['normal'])
        G = direct([1 - 2 * b for b in g])
        H = direct([1 - 2 * b for b in h])
        assert sum(g) + sum(h) == 256
        assert all(abs(v) + abs(w) <= 32 for v, w in zip(G, H))
        assert any(abs(v) == abs(w) for v, w in zip(G, H))
        assert set(direct([canonical(abs(v)) for v in H])) <= {-256, 256}
        for a in range(256):
            allowed = [m for m in range(2, 33 - abs(G[a]), 4) if classify(m) == classify(abs(H[a]))]
            assert abs(H[a]) in allowed
        planted += 1
    # Published NL242 seed gives a real, unbalanced bound-28 positive model.
    hx = ('68B7EF2DA03B0D3EA00DB6A96DD99AEAFDB9C842B6D5DC8C4526CE0DD29020DB'
          'B75FE3314568344E73688FF0CB2482E065231869E1AA4583765CC491F8A8DB12')
    text = ''.join(format(int(ch, 16), '04b') for ch in hx)
    support_xor = 0
    for x, b in enumerate(text):
        if b == '1':
            support_xor ^= x
    assert support_xor == 0
    # Its support XOR is zero: no odd slice exists.  This positive control
    # checks the general paired-spectrum bound, not the odd-spectrum lemma.
    found = 1
    g, h = pull_half(text, found)
    assert sum(g) % 2 == sum(h) % 2 == 0
    G = direct([1 - 2 * b for b in g])
    H = direct([1 - 2 * b for b in h])
    assert max(abs(x) + abs(y) for x, y in zip(G, H)) == 28
    assert not any(abs(x) == abs(y) for x, y in zip(G, H))
    return {'direct_odd_tables': len(tables), 'corrupt_spectra_rejected': corrupt_rejected,
            'planted_balanced_bound32_completions': planted,
            'published_unbalanced_bound28_positive_model_normal': found,
            'published_model_has_even_halves_not_odd_lemma_control': True}


def affine_solutions_low(equations, n):
    augmented = [left | (right << n) for left, right in equations]
    pivots = []
    used = 0
    for c in range(n):
        pick = next((j for j in range(used, len(augmented)) if augmented[j] >> c & 1), None)
        if pick is None:
            continue
        augmented[used], augmented[pick] = augmented[pick], augmented[used]
        for j in range(len(augmented)):
            if j != used and augmented[j] >> c & 1:
                augmented[j] ^= augmented[used]
        pivots.append(c)
        used += 1
    assert not any((v & ((1 << n) - 1)) == 0 and v >> n & 1 for v in augmented)
    particular = sum(((augmented[i] >> n) & 1) << c for i, c in enumerate(pivots))
    kernel = []
    for c in range(n):
        if c in pivots:
            continue
        v = 1 << c
        for i, p in enumerate(pivots):
            if augmented[i] >> c & 1:
                v |= 1 << p
        kernel.append(v)
    return len(pivots), particular, kernel


def mixed_difference(values, subset):
    # Explicit corner sum, not a Moebius-transform implementation.
    total = 0
    corner = subset
    while True:
        total += (-1) ** (subset.bit_count() - corner.bit_count()) * values[corner]
        if corner == 0:
            return total
        corner = (corner - 1) & subset


def audit_final(data, classes, certificate_bytes, mutate=False):
    cert = json.loads((ROOT / 'results/final-parity.json').read_text())
    if mutate:
        cert['moment_equations'][13]['mixed_difference'] += 2
    assert cert['screen_sha256'] == hashlib.sha256(certificate_bytes).hexdigest()
    cases = [r for r in classes if r['class_stage'] == 'UNKNOWN']
    assert len(cases) == 1 and (cases[0]['source'], cases[0]['normal']) == (96, 511)
    case = cases[0]
    candidates = [q for q in case['quadratic_candidates'] if q['rejected_by'] is None]
    assert len(candidates) == 1
    q = candidates[0]
    domains = q['magnitude_domains']
    maxima = [max(d) for d in domains]
    inverse = direct([canonical(m) for m in maxima])
    budget = (sum(m * m for m in maxima) - 65536) // 64
    assert budget == cert['energy_deficit_budget'] == 56
    local = []
    for upper, domain in zip(maxima, domains):
        choices = []
        for m in domain:
            assert (canonical(upper) - canonical(m)) % 16 == 0
            assert (upper * upper - m * m) % 64 == 0
            choices.append([(canonical(upper) - canonical(m)) // 16, (upper * upper - m * m) // 64, m])
        local.append(choices)
    assert local == cert['local_e_d_m_domains']
    active = [a for a, d in enumerate(local) if len(d) != 1]
    assert len(active) == 166 and active == cert['active_spectral_indices']
    assert all(local[a] == [[0, 0, 2]] for a in range(256) if a not in active)
    assert all(t % 16 == 0 for t in inverse)
    residues = [t // 16 - 16 for t in inverse]
    equations = []
    expected_moments = []
    for subset in range(256):
        k = subset.bit_count()
        if k > 4:
            continue
        difference = mixed_difference(residues, subset)
        factor = (-2) ** k
        assert difference % factor == 0
        rhs = (difference // factor) % 2
        expected_moments.append({'subset': subset, 'mixed_difference': difference, 'factor': factor, 'parity_rhs': rhs})
        mask = sum(1 << i for i, a in enumerate(active) if a & subset == subset)
        equations.append((mask, rhs))
    assert expected_moments == cert['moment_equations'], 'invalid final mixed-difference certificate'
    rank, particular, kernel = affine_solutions_low(equations, len(active))
    assert rank == cert['affine_rank'] == 147
    assert len(kernel) == cert['affine_dimension'] == 19
    # Validate the producer's different basis too: dimension, independence,
    # particular solution, and all homogeneous equations.
    supplied_part = int(cert['affine_particular'])
    supplied_basis = [int(v) for v in cert['affine_kernel_basis']]
    assert len(supplied_basis) == 19
    assert affine_solutions_low([(v, 0) for v in supplied_basis], 166)[0] == 19
    for left, right in equations:
        assert (left & supplied_part).bit_count() % 2 == right
        assert all((left & v).bit_count() % 2 == 0 for v in supplied_basis)
    costs = [min(d for e, d, m in local[a] if e % 2) for a in active]
    cost_masks = {}
    for i, c in enumerate(costs):
        cost_masks[c] = cost_masks.get(c, 0) | (1 << i)
    histogram = Counter()
    # Binary (not Gray) indexing and independent lowest-pivot affine basis.
    for index in range(1 << len(kernel)):
        word = particular
        remaining = index
        while remaining:
            bit = (remaining & -remaining).bit_length() - 1
            word ^= kernel[bit]
            remaining &= remaining - 1
        cost = sum(c * (mask & word).bit_count() for c, mask in cost_masks.items())
        histogram[cost] += 1
    assert dict(sorted(histogram.items())) == {int(k): v for k, v in cert['cost_histogram'].items()}
    assert sum(histogram.values()) == cert['enumerated_parities'] == 524288
    assert min(histogram) == cert['minimum_forced_deficit'] == 140
    assert min(histogram) > budget
    minimum = int(cert['minimum_word'])
    assert sum(c * (minimum & mask).bit_count() for c, mask in cost_masks.items()) == 140
    assert all((left & minimum).bit_count() % 2 == right for left, right in equations)
    # A planted bound-32 model in this same half validates the exact
    # finite-domain -> correction -> mixed-moment correspondence.
    g, h = pull_half(data['sources'][96]['bits'], 511)
    G = direct([1 - 2 * b for b in g])
    H = direct([1 - 2 * b for b in h])
    planted_max = [max(m for m in range(2, 33 - abs(v), 4) if classify(m) == classify(abs(w))) for v, w in zip(G, H)]
    planted_K0 = [canonical(m) for m in planted_max]
    planted_inverse = direct(planted_K0)
    e = [(k - canonical(abs(w))) // 16 for k, w in zip(planted_K0, H)]
    assert all((k - canonical(abs(w))) % 16 == 0 for k, w in zip(planted_K0, H))
    r = [v // 16 - 16 for v in planted_inverse]
    assert all(v % 16 == 0 for v in planted_inverse)
    assert all((t - rr) % 32 == 0 for t, rr in zip(direct(e), r))
    for subset in range(256):
        if subset.bit_count() > 4:
            continue
        factor = (-2) ** subset.bit_count()
        delta = mixed_difference(r, subset)
        assert delta % factor == 0
        assert sum(e[a] for a in range(256) if a & subset == subset) % 2 == (delta // factor) % 2
    return {'status': 'EXCLUDED', 'rank': rank, 'dimension': len(kernel),
            'parities': sum(histogram.values()), 'budget': budget,
            'minimum_forced_deficit': min(histogram), 'planted_bound32_moment_control': 'PASS'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutate-spectrum', action='store_true')
    parser.add_argument('--mutate-certificate', action='store_true')
    parser.add_argument('--mutate-final-certificate', action='store_true')
    parser.add_argument('--output', default='results/check.json')
    args = parser.parse_args()
    started = time.monotonic()
    raw = (ROOT / 'inputs/slice-screen.json.gz').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PIN
    data = json.loads(gzip.decompress(raw))
    certificate_bytes = (ROOT / 'results/screen.json.gz').read_bytes()
    certificate = json.loads(gzip.decompress(certificate_bytes))
    classes = certificate['classes']
    assert len(classes) == 252
    survivors = [r for r in data['cases'] if not r['rejections']]
    assert survivors == data['unresolved_case_records'] and len(survivors) == 252
    assert [(r['source'], r['normal']) for r in classes] == [(r['source'], r['normal']) for r in survivors]
    if args.mutate_spectrum:
        classes[0]['G'][0] += 8
    if args.mutate_certificate:
        classes[0]['quadratic_candidates'][0]['coefficient_mask'] ^= 1
    producer_basis = [0] + [1 << i for i in range(8)] + [(1 << i) | (1 << j) for i in range(8) for j in range(i + 1, 8)]
    stages = Counter()
    groups = {}
    group_ids = []
    total_q = 0
    for rec in classes:
        source = data['sources'][rec['source']]
        assert hashlib.sha256(source['bits'].encode()).hexdigest() == source['sha256_ascii_bits']
        g, _ = pull_half(source['bits'], rec['normal'])
        G = direct([1 - 2 * b for b in g])
        assert rec['G'] == G, 'fixed-half direct spectrum mismatch'
        assert rec['fixed_bits'] == ''.join(map(str, g)) and sum(g) % 2
        assert max(map(abs, G)) == 26 and sum(v * v for v in G) == 65536
        Z = [b for b, v in enumerate(G) if abs(v) == 26]
        rank, words = independent_kernel(Z)
        assert rank == rec['kernel_rank']
        expected_quadratics = {tuple(qvalue(w, b, BASIS) for b in range(256)) for w in words}
        got_quadratics = [tuple(qvalue(q['coefficient_mask'], b, producer_basis) for b in range(256)) for q in rec['quadratic_candidates']]
        assert len(set(got_quadratics)) == len(got_quadratics) == 1 << (37 - rank)
        assert set(got_quadratics) == expected_quadratics, 'incomplete or invalid quadratic certificate'
        stage1 = stage2 = stage3 = 0
        for q, Q in zip(rec['quadratic_candidates'], got_quadratics):
            total_q += 1
            domains = [[m for m in (2, 6, 10, 14, 18, 22, 26) if m + abs(v) <= 28 and classify(m) == bit] for v, bit in zip(G, Q)]
            if any(not d for d in domains):
                assert q['rejected_by'] == 'empty-domain'
                continue
            maxima = [max(d) for d in domains]
            S = sum(m * m for m in maxima)
            best_zero = max((S - maxima[b] ** 2 + G[b] ** 2 for b in range(256) if abs(G[b]) in domains[b]), default=-1)
            assert q['square_capacity'] == S and q['zero_capacity'] == best_zero
            if best_zero < 65536:
                assert q['rejected_by'] == 'quadratic-Parseval-zero'
                continue
            stage1 += 1
            transformed_squares = direct([m * m for m in maxima])
            distances = [min(abs(t - (1024 + 2048 * k)) for k in range((t - 1024) // 2048 - 1, (t - 1024) // 2048 + 3)) for t in transformed_squares[1:]]
            ac_distance = max(distances)
            assert ac_distance == q['ac_max_residue_distance']
            assert distances[q['ac_direction'] - 1] == ac_distance
            if ac_distance > S - 65536:
                assert q['rejected_by'] == 'autocorrelation-residue-energy'
                continue
            stage2 += 1
            K0 = [canonical(m) for m in maxima]
            inverse = direct(K0)
            for m0, k0, domain in zip(maxima, K0, domains):
                for m in domain:
                    assert 4 * abs(k0 - canonical(m)) <= m0 * m0 - m * m
            distances = [min(abs(t - 256), abs(t + 256)) for t in inverse]
            gap = max(distances)
            assert q['canonical_max_distance'] == gap
            assert distances[q['canonical_input']] == gap
            assert q['canonical_energy_L1_bound'] == (S - 65536) // 4
            if 4 * gap > S - 65536:
                assert q['rejected_by'] == 'canonical-inverse-energy'
                continue
            stage3 += 1
            assert q['rejected_by'] is None and q['magnitude_domains'] == domains
            assert q['maxima'] == maxima and q['canonical_maximum_inverse'] == inverse
        expected_stage = ('quadratic-Parseval-zero' if not stage1 else 'autocorrelation-residue-energy' if not stage2 else 'canonical-inverse-energy' if not stage3 else 'UNKNOWN')
        assert rec['class_stage'] == expected_stage
        stages[expected_stage] += 1
        key = tuple(map(abs, G))
        if key not in groups:
            groups[key] = len(groups)
        group_ids.append(groups[key])
    assert dict(stages) == certificate['stage_counts']
    assert len(groups) == certificate['literal_capacity_groups'] == 154
    assert group_ids == certificate['identity_spectral_group_for_all_252']
    ctrl = controls(data, classes)
    final = audit_final(data, classes, certificate_bytes, args.mutate_final_certificate)
    out = {'status': 'PASS', 'class_count': len(classes), 'stage_counts': dict(stages),
           'quadratics_exhaustively_checked': total_q,
           'identity_capacity_group_count': len(groups), 'controls': ctrl,
           'final_parity': final, 'resolved_classes': 252, 'unknown_classes': 0, 'unattempted_classes': 0,
           'input_sha256': PIN, 'certificate_sha256': hashlib.sha256(certificate_bytes).hexdigest(),
           'checker_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - started}
    (ROOT / args.output).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, sort_keys=True))


if __name__ == '__main__':
    main()
