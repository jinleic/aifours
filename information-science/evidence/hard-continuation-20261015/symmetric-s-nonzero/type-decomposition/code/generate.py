#!/usr/bin/env python3
"""Derive the dihedral support types; plant balanced controls; build exact PB branches."""
from pathlib import Path
import gzip
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
INPUT_SHA = '441e85e5289c34a15bc0caf5387cae77d9039da3a47efdbde9d429d5f7c91cbb'


def action(x, images):
    result = 0
    for i, image in enumerate(images):
        if x >> i & 1:
            result ^= image
    return result


def spectrum(bits):
    return [sum(1 - 2 * (b ^ ((a & x).bit_count() & 1)) for x, b in enumerate(bits)) for a in range(512)]


def support_xor(bits):
    s = 0
    for x, b in enumerate(bits):
        if b:
            s ^= x
    return s


def cap(bound, parity):
    residue = 4 * parity
    return bound - ((bound - residue) % 8)


def xor_expression(names):
    out = 'false'
    for name in names:
        out = '(xor ' + out + ' ' + name + ')'
    return out


def problem(cls, s, bound):
    n = len(cls['orbits'])
    lines = ['(set-logic QF_FD)'] + [f'(declare-fun x{j} () Bool)' for j in range(n)]
    rows = []
    for a, C in zip(cls['representatives'], cls['C']):
        parity = (a & s).bit_count() & 1
        peak = cap(bound, parity)
        L = sum(map(abs, C))
        low, high = max(0, (L - peak + 1) // 2), min(L, (L + peak) // 2)
        terms = [(j, abs(v), v > 0) for j, v in enumerate(C) if v]
        weights = ' '.join(str(w) for j, w, positive in terms)
        atoms = ' '.join(f'x{j}' if positive else f'(not x{j})' for j, w, positive in terms)
        lines += [f'(assert ((_ pbge {low} {weights}) {atoms}))',
                  f'(assert ((_ pble {high} {weights}) {atoms}))']
        rows.append({'frequency': a, 'parity_a_dot_s': parity, 'cap': peak, 'L': L,
                     'lower': low, 'upper': high, 'signed_weight_terms': terms})
    weights = ' '.join(map(str, cls['orbit_sizes']))
    atoms = ' '.join(f'x{j}' for j in range(n))
    lines.append(f'(assert ((_ pbeq 256 {weights}) {atoms}))')
    sx_terms = []
    for bit in range(9):
        names = [f'x{j}' for j, x in enumerate(cls['orbit_xors']) if x >> bit & 1]
        expr = xor_expression(names)
        rhs = 'true' if s >> bit & 1 else 'false'
        lines.append(f'(assert (= {expr} {rhs}))')
        sx_terms.append([int(name[1:]) for name in names])
    lines.append('(assert (not x0))')
    raw = ('\n'.join(lines) + '\n').encode()
    return raw, {'s': s, 'nominal_bound': bound, 'rows': rows,
                 'balance_weight': 256, 'balance_weights': cls['orbit_sizes'], 'fixed_support_xor_terms': sx_terms,
                 'output_complement_normalization': 'x0=false', 'smt_sha256': hashlib.sha256(raw).hexdigest(),
                 'primary_variables': n, 'assertions': 2 * len(rows) + 11}


def main():
    start = time.monotonic()
    input_raw = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    assert hashlib.sha256(input_raw).hexdigest() == INPUT_SHA
    imported = json.loads(gzip.decompress(input_raw))
    cls = imported['classes']['3-dsbf']
    # Actual linear permutation matrices, columns given by basis-vector images.
    rotation = [((1 << i) << 3 | (1 << i) >> 6) & 511 for i in range(9)]
    reversal = [1 << (8 - i) for i in range(9)]
    generators = [rotation, reversal]
    matrices = [[[image >> row & 1 for image in g] for row in range(9)] for g in generators]
    fixed = [s for s in range(512) if all(action(s, g) == s for g in generators)]
    assert fixed == [0, 146, 365, 511]
    # Reconstruct the group orbits from these matrices, not from an assumed type list.
    orbits, used = [], set()
    for x in range(512):
        if x in used:
            continue
        orbit, queue = {x}, [x]
        for y in queue:
            for g in generators:
                z = action(y, g)
                if z not in orbit:
                    orbit.add(z)
                    queue.append(z)
        orbits.append(sorted(orbit))
        used |= orbit
    assert orbits == cls['orbits'] and len(orbits) == 104
    span = {0}
    for v in cls['orbit_xors']:
        span |= {s ^ v for s in span}
    assert sorted(span) == fixed
    seed = next(v for v in imported['published_seeds'] if v['name'] == 'dsbf40')
    bits = list(map(int, seed['bits']))
    initial_weight = sum(bits)
    assert initial_weight == 250 and support_xor(bits) == 0
    # Exact finite DP minimizes the number of changed input points while
    # enforcing balance and support type; it does not optimize nonlinearity.
    states = {(initial_weight, 0): (0, 0)}
    for j, orbit in enumerate(orbits):
        delta_weight = (1 - 2 * bits[orbit[0]]) * len(orbit)
        new = dict(states)
        for (weight, sx), (distance, mask) in states.items():
            key = (weight + delta_weight, sx ^ cls['orbit_xors'][j])
            candidate = (distance + len(orbit), mask | (1 << j))
            if key not in new or candidate[0] < new[key][0]:
                new[key] = candidate
        states = new
    controls = []
    branches = []
    for s in fixed[1:]:
        distance, mask = states[(256, s)]
        planted = bits.copy()
        flipped_orbits = []
        for j, orbit in enumerate(orbits):
            if mask >> j & 1:
                flipped_orbits.append(j)
                for x in orbit:
                    planted[x] ^= 1
        complemented = bool(planted[0])
        if complemented:
            planted = [b ^ 1 for b in planted]
        assert sum(planted) == 256 and support_xor(planted) == s and planted[0] == 0
        W = spectrum(planted)
        peak = max(map(abs, W))
        for a, v in enumerate(W):
            assert v % 8 == 4 * ((a & s).bit_count() & 1)
            assert abs(v) <= cap(peak, (a & s).bit_count() & 1)
        text = ''.join(map(str, planted))
        controls.append({'s': s, 'bits': text, 'sha256_ascii_bits': hashlib.sha256(text.encode()).hexdigest(),
                         'weight': 256, 'support_xor': s, 'walsh': W, 'max_abs_W': peak,
                         'nominal_relaxed_bound': peak, 'changed_points_before_optional_complement': distance,
                         'flipped_orbits_from_published_seed': flipped_orbits, 'output_complemented': complemented})
        for label, bound in [('target', 28), ('control', peak)]:
            smt, meta = problem(cls, s, bound)
            path = ROOT / f'inputs/{label}-s{s}.smt2.gz'
            path.write_bytes(gzip.compress(smt, mtime=0))
            (ROOT / f'inputs/{label}-s{s}.encoding.json').write_text(json.dumps(meta, separators=(',', ':')) + '\n')
            if label == 'target':
                branches.append({'s': s, 'smt_path': str(path.relative_to(ROOT)), **meta})
    out = {'input_sha256': INPUT_SHA, 'generators_basis_images': generators, 'generator_matrices': matrices,
           'fixed_support_vectors_including_zero': fixed, 'nonzero_types': fixed[1:],
           'orbit_count': len(orbits), 'orbit_xor_span': sorted(span), 'branches': branches,
           'controls': controls, 'elapsed_seconds': time.monotonic() - start,
           'scope': 'Balanced3-DSBF, fixed nonzero support type, nominal peak<=28; no negative solver claim.'}
    (ROOT / 'inputs/decomposition.json').write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(json.dumps({'types': fixed[1:], 'control_peaks': {r['s']: r['max_abs_W'] for r in controls},
                      'control_distances': {r['s']: r['changed_points_before_optional_complement'] for r in controls},
                      'elapsed_seconds': out['elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
