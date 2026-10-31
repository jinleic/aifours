#!/usr/bin/env python3
"""Independent exact Q/H reconstruction and complete closed-face Bernstein audit.

Only the frozen manifest and its seven declared inputs are read. Author and
prior reviewer programs are never imported or executed. Outputs are exclusive.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, prod
from pathlib import Path
import json
import subprocess

HERE = Path(__file__).resolve().parent
MANIFEST_SHA = '6ddba0f76b0183136dae7cd3cc822f24e1c591342fcc0c88c12dd7accbc41476'
N = 6
Z = (0,) * N
STRIDES = tuple(3 ** (N - 1 - j) for j in range(N))
CORNERS = tuple((bits, sum(2 * bits[j] * STRIDES[j] for j in range(N)))
                for bits in product((0, 1), repeat=N))


class CertificateError(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CertificateError(reason)


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, capture_output=True, text=True).stdout.strip()


def digest(data):
    return sha256(data).hexdigest()


def serial(obj):
    return json.dumps(obj, separators=(',', ':'), ensure_ascii=True).encode()


def no_duplicate_keys(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate-json-key: ' + key)
        out[key] = value
    return out


def bad_constant(token):
    raise CertificateError('nonfinite-json-constant: ' + token)


def json_strict(blob):
    return json.loads(blob.decode('utf-8'), object_pairs_hook=no_duplicate_keys,
                      parse_constant=bad_constant)


def read_frozen_inputs():
    manifest_bytes = (HERE / 'manifest-v1.json').read_bytes()
    require(digest(manifest_bytes) == MANIFEST_SHA, 'manifest-sha')
    manifest = json_strict(manifest_bytes)
    require(len(manifest['inputs_in_read_order']) == 7, 'input-count')
    records, blobs = [], []
    for item in manifest['inputs_in_read_order']:
        data = Path(item['path']).read_bytes()
        data.decode('utf-8')
        actual = (digest(data), len(data), data.count(b'\n'))
        expected = (item['sha256'], item['bytes'], item['LF'])
        require(actual == expected, 'input-integrity: ' + item['path'])
        require(data.endswith(b'\n'), 'missing-final-lf: ' + item['path'])
        records.append({'role': item['role'], 'path': item['path'],
                        'sha256': actual[0], 'bytes': actual[1], 'LF': actual[2]})
        blobs.append(data)
    return records, json_strict(blobs[4])


def lincomb(*terms):
    out = {}
    for multiplier, poly in terms:
        for powers, value in poly.items():
            out[powers] = out.get(powers, 0) + multiplier * value
    return {powers: value for powers, value in out.items() if value}


def multiply(left, right):
    out = {}
    for a, av in left.items():
        for b, bv in right.items():
            key = tuple(a[j] + b[j] for j in range(N))
            out[key] = out.get(key, 0) + av * bv
    return {powers: value for powers, value in out.items() if value}


def reconstruct():
    # Generate elementary symmetric functions by the product recurrence
    # prod_i (1 + t*u_i), not from any supplied coefficient table.
    one = {Z: 1}
    e = [one, {}, {}, {}, {}]
    for j in range(N):
        exponent = tuple(int(i == j) for i in range(N))
        variable = {exponent: 1}
        for k in range(4, 0, -1):
            e[k] = lincomb((1, e[k]), (1, multiply(variable, e[k-1])))
    f1, f2, f3, f4 = e[1:]
    # A9=9A, B9=9B, h027=27h0, h19=9h1.
    a9 = lincomb((9, f2), (-36, f1), (74, one))
    b9 = lincomb((9, f3), (-36, f2), (74, f1), (-84, one))
    h027 = lincomb((27, f4), (-210, f2), (636, f1), (-1007, one))
    h19 = lincomb((9, f3), (-70, f1), (212, one))
    f1minus4 = lincomb((1, f1), (-4, one))
    q = lincomb((1, multiply(a9, a9)), (-9, multiply(f1minus4, b9)))
    h = lincomb((3, multiply(h19, b9)), (-1, multiply(h027, a9)))
    return {'Q': q, 'H': h}


def coefficient_digest(poly):
    rows = [[list(key), str(value)] for key, value in sorted(poly.items())]
    return digest(serial(rows))


def make_tree(paths):
    require(isinstance(paths, list), 'paths-not-list')
    root = {}
    for path in paths:
        require(type(path) is str and path and set(path) <= {'0', '1'}, 'invalid-path')
        node = root
        for bit in path:
            require('leaf' not in node, 'prefix-collision: ' + path)
            node = node.setdefault(bit, {})
        require('leaf' not in node, 'duplicate-leaf: ' + path)
        require(not node, 'prefix-collision: ' + path)
        node['leaf'] = path

    def check(node, prefix):
        if 'leaf' in node:
            require(set(node) == {'leaf'} and node['leaf'] == prefix,
                    'invalid-terminal: ' + prefix)
            return 1, 0
        require(set(node) == {'0', '1'}, 'missing-child: ' + prefix)
        left_leaves, left_internal = check(node['0'], prefix + '0')
        right_leaves, right_internal = check(node['1'], prefix + '1')
        return left_leaves + right_leaves, 1 + left_internal + right_internal

    leaves, internal = check(root, '')
    require(internal == leaves - 1, 'binary-tree-count')
    return root, internal


def root_coefficients(poly):
    # For F(t)=prod(1-t_j)^2 P(t/(1-t)), its Bernstein coefficient at
    # multi-index a is c_a / prod binom(2,a_j). The returned integers are 64*F.
    out = [0] * (3 ** N)
    for powers, value in poly.items():
        require(all(0 <= exponent <= 2 for exponent in powers), 'degree-above-two')
        denominator = prod(comb(2, exponent) for exponent in powers)
        require(64 % denominator == 0, 'root-scale')
        index = sum(powers[j] * STRIDES[j] for j in range(N))
        out[index] = value * (64 // denominator)
    return out


def bisect(coeffs, axis):
    # Each result is 4 times the corresponding actual de Casteljau tensor.
    stride = STRIDES[axis]
    left = [0] * len(coeffs)
    right = [0] * len(coeffs)
    for block in range(0, len(coeffs), 3 * stride):
        for offset in range(stride):
            i = block + offset
            a, b, c = coeffs[i], coeffs[i + stride], coeffs[i + 2 * stride]
            midpoint = a + 2*b + c
            left[i], left[i + stride], left[i + 2*stride] = 4*a, 2*(a+b), midpoint
            right[i], right[i + stride], right[i + 2*stride] = midpoint, 2*(b+c), 4*c
    return left, right


def finite_corner_data(coeffs, numerators, levels, path):
    require(len(coeffs) == 3 ** N, 'coefficient-grid-size')
    require(min(coeffs) >= 0, 'negative-bernstein-coefficient: ' + path)
    require(all(level >= 1 for level in levels), 'unsplit-axis: ' + path)
    counts = Counter()
    interior = 0
    for bits, index in CORNERS:
        # The upper endpoint is 1 precisely for the rightmost dyadic interval.
        if any(bits[j] and numerators[j] + 1 == 2 ** levels[j] for j in range(N)):
            continue
        mask = sum((1 << j) for j in range(N)
                   if not bits[j] and numerators[j] == 0)
        require(coeffs[index] > 0,
                'nonpositive-finite-corner: ' + path + ':zero-mask=' + str(mask))
        counts[mask] += 1
        if mask == 0:
            interior += 1
    require(sum(counts.values()) > 0, 'no-finite-corner: ' + path)
    require(interior > 0, 'no-open-cube-corner: ' + path)
    return counts, interior


def audit(tree, root_coeffs):
    state = {'leaves': 0, 'internal_nodes': 0, 'coefficient_count': 0,
             'finite_corners': 0, 'strictly_interior_corners': 0,
             'zero_masks': Counter(), 'depths': Counter(), 'origin_leaf': None}

    def walk(node, coeffs, nums, levels, depth):
        if 'leaf' in node:
            path = node['leaf']
            counts, interior = finite_corner_data(coeffs, nums, levels, path)
            state['leaves'] += 1
            state['coefficient_count'] += len(coeffs)
            state['finite_corners'] += sum(counts.values())
            state['strictly_interior_corners'] += interior
            state['zero_masks'].update(counts)
            state['depths'][depth] += 1
            if all(value == 0 for value in nums):
                require(state['origin_leaf'] is None, 'duplicate-origin-leaf')
                state['origin_leaf'] = (path, coeffs.copy(), nums, levels)
            return
        state['internal_nodes'] += 1
        axis = depth % N
        left, right = bisect(coeffs, axis)
        next_levels = list(levels)
        next_levels[axis] += 1
        lo_nums, hi_nums = list(nums), list(nums)
        lo_nums[axis] *= 2
        hi_nums[axis] = 2 * hi_nums[axis] + 1
        walk(node['0'], left, tuple(lo_nums), tuple(next_levels), depth + 1)
        walk(node['1'], right, tuple(hi_nums), tuple(next_levels), depth + 1)

    walk(tree, root_coeffs, (0,) * N, (0,) * N, 0)
    require(state['origin_leaf'] is not None, 'missing-origin-leaf')
    require(set(state['zero_masks']) == set(range(64)), 'missing-zero-face-mask')
    return state


def expect_error(name, expected_prefix, action):
    try:
        action()
    except CertificateError as exc:
        require(str(exc).startswith(expected_prefix),
                'wrong-control-reason: ' + name + ': ' + str(exc))
        return {'name': name, 'expected_reason': expected_prefix, 'observed_reason': str(exc),
                'status': 'rejected-for-intended-reason'}
    raise CertificateError('control-not-rejected: ' + name)


def finite_cube(point):
    require(len(point) == N, 'domain-dimension')
    require(all(isinstance(value, Fraction) and 0 <= value < 1 for value in point),
            'domain-not-finite-nonnegative')


def point_via_tree(tree, root_coeffs, point):
    finite_cube(point)
    node, coeffs = tree, root_coeffs
    nums, levels = [0] * N, [0] * N
    depth = 0
    while 'leaf' not in node:
        axis = depth % N
        midpoint = Fraction(2 * nums[axis] + 1, 2 ** (levels[axis] + 1))
        take_right = point[axis] > midpoint
        left, right = bisect(coeffs, axis)
        coeffs = right if take_right else left
        node = node['1' if take_right else '0']
        nums[axis] = 2*nums[axis] + int(take_right)
        levels[axis] += 1
        depth += 1
    bases = []
    for j in range(N):
        t = point[j] * (2 ** levels[j]) - nums[j]
        require(0 <= t <= 1, 'point-not-in-chosen-leaf')
        bases.append(((1-t)**2, 2*t*(1-t), t**2))
    weighted = Fraction(0)
    for coord in product(range(3), repeat=N):
        weight = prod(bases[j][coord[j]] for j in range(N))
        if weight:
            index = sum(coord[j] * STRIDES[j] for j in range(N))
            weighted += coeffs[index] * weight
    return weighted / (64 * 4**depth), node['leaf']


def evaluate_original(poly, rates):
    return sum(Fraction(c) * prod(rates[j] ** powers[j] for j in range(N))
               for powers, c in poly.items())


def positive_control(name, rates, polys, trees, roots):
    rates = tuple(Fraction(value) for value in rates)
    point = tuple(r / (1 + r) for r in rates)
    finite_cube(point)
    results = {}
    for label in ('Q', 'H'):
        direct = evaluate_original(polys[label], rates)
        expected_f = direct * prod((1-t)**2 for t in point)
        from_leaf, leaf = point_via_tree(trees[label], roots[label], point)
        require(direct > 0 and from_leaf > 0 and from_leaf == expected_f,
                'positive-control-failed: ' + name + ':' + label)
        results[label] = {'original_value': str(direct), 'compactified_value': str(from_leaf),
                          'leaf': leaf}
    return {'name': name, 'rates': [str(r) for r in rates],
            'compactified_point': [str(t) for t in point], 'results': results,
            'status': 'exact-original-equals-exact-leaf-and-positive'}


def main():
    result_file = HERE / 'certificate-result-v1.json'
    require(not result_file.exists(), 'result-already-exists')
    started = clock()
    records, cert = read_frozen_inputs()
    fields = {'z', 'Q_coefficients_sha256', 'H_coefficients_sha256',
              'Q_variable_degrees', 'H_variable_degrees', 'Q_terms', 'H_terms',
              'Q_positive_compactified_binary_leaf_paths',
              'H_positive_compactified_binary_leaf_paths', 'split_axis',
              'compactification', 'identity', 'scope'}
    require(set(cert) == fields, 'certificate-fields')
    require(cert['z'] == '8/9', 'wrong-z')
    require(cert['split_axis'] == 'path depth modulo 6', 'split-axis-convention')
    require(cert['compactification'] == 'u_i=x_i/(1-x_i); multiply each (1-x_i)^2',
            'compactification-convention')
    require(cert['identity'] == 'E4=A*u7+B; q=Q/(81*A); E3=-H/(243*A)',
            'identity-convention')
    polys = reconstruct()
    trees, roots, states, summaries = {}, {}, {}, {}
    for label, expected_terms, expected_leaves in [('Q', 168, 5332), ('H', 435, 5334)]:
        poly = polys[label]
        degrees = [max(key[j] for key in poly) for j in range(N)]
        require(degrees == cert[label + '_variable_degrees'] == [2]*N, 'variable-degrees:' + label)
        require(len(poly) == cert[label + '_terms'] == expected_terms, 'term-count:' + label)
        cdigest = coefficient_digest(poly)
        require(cdigest == cert[label + '_coefficients_sha256'], 'coefficient-digest:' + label)
        paths = cert[label + '_positive_compactified_binary_leaf_paths']
        tree, internal = make_tree(paths)
        require(len(paths) == expected_leaves, 'leaf-count:' + label)
        root = root_coefficients(poly)
        state = audit(tree, root)
        require(state['leaves'] == expected_leaves and state['internal_nodes'] == internal,
                'leaf-traversal-count:' + label)
        require(state['coefficient_count'] == expected_leaves * 729, 'coefficient-total:' + label)
        trees[label], roots[label], states[label] = tree, root, state
        zero_by_multiplicity = Counter()
        for mask, count in state['zero_masks'].items():
            zero_by_multiplicity[mask.bit_count()] += count
        summaries[label] = {'coefficient_digest': cdigest, 'terms': len(poly),
                            'variable_degrees': degrees, 'leaves': state['leaves'],
                            'internal_nodes': internal,
                            'checked_bernstein_coefficients': state['coefficient_count'],
                            'strictly_positive_finite_corners': state['finite_corners'],
                            'strictly_positive_open_cube_corners': state['strictly_interior_corners'],
                            'finite_corners_by_zero_coordinate_count': dict(sorted(zero_by_multiplicity.items())),
                            'all_64_zero_coordinate_masks_represented': True,
                            'depth_counts': dict(sorted(state['depths'].items())),
                            'origin_leaf': state['origin_leaf'][0]}
    qpaths = cert['Q_positive_compactified_binary_leaf_paths']
    controls = []
    controls.append(expect_error('remove-first-Q-leaf', 'missing-child:',
                                 lambda: make_tree(qpaths[1:])))
    controls.append(expect_error('duplicate-first-Q-leaf', 'duplicate-leaf:',
                                 lambda: make_tree(qpaths + qpaths[:1])))
    controls.append(expect_error('add-Q-ancestor-leaf', 'prefix-collision:',
                                 lambda: make_tree(qpaths + [qpaths[0][:-1]])))
    path, original, nums, levels = states['Q']['origin_leaf']
    mutant = original.copy()
    require(original[0] > 0 and all(v == 0 for v in nums), 'zero-face-mutation-setup')
    mutant[0] = 0
    require(sum(a != b for a, b in zip(original, mutant)) == 1 and min(mutant) >= 0,
            'zero-face-mutation-not-isolated')
    open_count = 0
    for bits, index in CORNERS:
        if all((bits[j] or nums[j] > 0) and
               (not bits[j] or nums[j] + 1 < 2**levels[j]) for j in range(N)):
            require(mutant[index] > 0, 'zero-face-mutation-affected-interior')
            open_count += 1
    require(open_count > 0, 'zero-face-mutation-no-open-corner')
    control = expect_error('zero-origin-corner-only-Q-coefficient', 'nonpositive-finite-corner:',
                           lambda: finite_corner_data(mutant, nums, levels, path))
    control.update({'leaf': path, 'coefficient_index': [0]*N,
                    'old_integer': str(original[0]), 'new_integer': '0',
                    'original_grid_sha256': digest(serial(original)),
                    'mutated_grid_sha256': digest(serial(mutant)),
                    'all_coefficients_nonnegative': True,
                    'strictly_positive_open_cube_corners_unaffected': open_count})
    controls.append(control)
    controls.append(expect_error('reject-infinite-rate-coordinate-one', 'domain-not-finite-nonnegative',
                                 lambda: finite_cube((Fraction(1),) + (Fraction(0),)*5)))
    controls.append(expect_error('reject-negative-coordinate', 'domain-not-finite-nonnegative',
                                 lambda: finite_cube((Fraction(-1,100),) + (Fraction(0),)*5)))
    positives = [positive_control('six-zero-rates', (0,0,0,0,0,0), polys, trees, roots),
                 positive_control('multiple-zero-faces-and-internal-dyadic-face',
                                  (0,1,0,2,0,3), polys, trees, roots)]
    # Include hashes of precisely the in-memory mutated path arrays without writing fixtures.
    path_hashes = {'original_Q_paths': digest(serial(qpaths)),
                   'missing_first_Q_leaf': digest(serial(qpaths[1:])),
                   'duplicate_first_Q_leaf': digest(serial(qpaths + qpaths[:1]))}
    result = {'status': 'PASS_EXACT_NONNEGATIVE_SIX_RATE_DOMAIN',
              'started_native_clock': started, 'completed_native_clock_before_receipt': clock(),
              'manifest_sha256': MANIFEST_SHA,
              'engine_sha256': digest(Path(__file__).read_bytes()),
              'inputs': records, 'certificate_metadata_scope': cert['scope'],
              'mathematics': 'independently reconstructed integer elementary-symmetric polynomials; degree-two tensor Bernstein, 64*4^depth scaling',
              'summaries': summaries, 'negative_controls': controls,
              'negative_control_path_array_hashes': path_hashes,
              'positive_controls': positives,
              'limitations': ['same-harness, not formal or independent-family verification',
                              'no symmetrization, PH caller, original target or novelty claim']}
    with result_file.open('x', encoding='utf-8') as out:
        json.dump(result, out, indent=2, sort_keys=True)
        out.write('\n')
    print(json.dumps({'status': result['status'], 'clock_before_receipt': result['completed_native_clock_before_receipt'],
                      'engine_sha256': result['engine_sha256'], 'Q_leaves': summaries['Q']['leaves'],
                      'H_leaves': summaries['H']['leaves'], 'negative_controls': len(controls),
                      'positive_controls': len(positives)}, sort_keys=True))


if __name__ == '__main__':
    main()
