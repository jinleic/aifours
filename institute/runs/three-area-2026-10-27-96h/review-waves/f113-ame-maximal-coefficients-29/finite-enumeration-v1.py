#!/usr/bin/env python3
"""Independent exact controls for the AME(4,6) forbidden-matching claim.

Directly enumerate all 81 four-tuples per normalized matching triple.  This
script does not import or execute the author's checkers.  Its one argument is
an output JSON path; output is created exclusively, never overwritten.
"""
import collections
import copy
import hashlib
import itertools
import json
import pathlib
import subprocess
import sys

MANIFEST = pathlib.Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f113-ame-maximal-coefficients-29/manifest-v1.json')
MANIFEST_SHA = '13e3696bd685bd9ee36ed655a53591706a409dfb77e764e85cf04a1024af139b'
P_SHA = '516cba122e2a7fbd252ccf06267e66410ab8e393089e0fe91c4d8b0f5690c083'
PAIRS = tuple(itertools.combinations(range(4), 2))
NAMES = ('AB', 'AC', 'AD', 'BC', 'BD', 'CD')
THREE = tuple(range(3))
FOUR_WORDS = tuple(itertools.product(THREE, repeat=4))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def native_clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def fail_if(condition, message):
    if condition:
        raise RuntimeError(message)


def histogram(counter):
    return {str(k): counter[k] for k in sorted(counter)}


def json_hash(value):
    return digest(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def bind_sources():
    data = MANIFEST.read_bytes()
    fail_if(digest(data) != MANIFEST_SHA, 'manifest hash mismatch')
    manifest = json.loads(data)
    verified = []
    p_bytes = None
    for item in manifest['inputs_in_read_order']:
        raw = pathlib.Path(item['path']).read_bytes()
        actual = digest(raw)
        fail_if(actual != item['sha256'], 'source SHA mismatch: ' + item['path'])
        fail_if(len(raw) != item['bytes'], 'source byte count mismatch: ' + item['path'])
        fail_if(raw.count(b'\n') != item['LF'], 'source LF count mismatch: ' + item['path'])
        verified.append({'path': item['path'], 'sha256': actual,
                         'bytes': len(raw), 'LF': raw.count(b'\n')})
        if actual == P_SHA:
            p_bytes = raw
    fail_if(p_bytes is None, 'bound P diagnostic absent')
    return verified, p_bytes


def pair_projections(words):
    return [{(word[i], word[j]) for word in words} for i, j in PAIRS]


def cube_controls():
    vertices = tuple(itertools.product((0, 1), repeat=3))
    edges = [frozenset((v, w)) for v, w in itertools.combinations(vertices, 2)
             if sum(a != b for a, b in zip(v, w)) == 1]
    fail_if(len(edges) != 12, 'wrong cube edge construction')
    union_hist = collections.Counter()
    one_per_axis_hist = collections.Counter()
    intersection_hist = collections.Counter()
    triangle_like = 0
    star_count = 0
    for triple in itertools.combinations(edges, 3):
        union_hist[len(set().union(*triple))] += 1
        intersections = sum(bool(triple[i] & triple[j])
                            for i, j in itertools.combinations(range(3), 2))
        intersection_hist[intersections] += 1
        axes = []
        for edge in triple:
            u, v = tuple(edge)
            axes.append(next(k for k in range(3) if u[k] != v[k]))
        if len(set(axes)) == 3:
            one_per_axis_hist[len(set().union(*triple))] += 1
        if intersections == 3:
            if set.intersection(*(set(e) for e in triple)):
                star_count += 1
            else:
                triangle_like += 1
    fail_if(sum(union_hist.values()) != 220, 'incomplete cube edge triples')
    fail_if(sum(one_per_axis_hist.values()) != 64, 'incomplete axis-distinct triples')
    return {'vertices': len(vertices), 'edges': len(edges),
            'distinct_edge_triples': sum(union_hist.values()),
            'union_cardinality_histogram': histogram(union_hist),
            'distinct_axes_triples': sum(one_per_axis_hist.values()),
            'distinct_axes_union_cardinality_histogram': histogram(one_per_axis_hist),
            'pairwise_intersecting_pair_count_histogram': histogram(intersection_hist),
            'three_pairwise_intersections_with_common_vertex': star_count,
            'triangle_like_triples_without_common_vertex': triangle_like,
            'all_distinct_triples_cover_at_least_four': min(union_hist) >= 4}


def matching_controls():
    permutations = tuple(itertools.permutations(THREE))
    histogram_total = collections.Counter()
    histogram_fiber = collections.Counter()
    histogram_vector = collections.Counter()
    drop_hist = {name: collections.Counter() for name in NAMES}
    drop_fiber_hist = {name: collections.Counter() for name in NAMES}
    drop_examples = {}
    fix_hist = collections.Counter()
    badset_errors = []
    cases = []
    equality_cases = []
    candidate_visits = 0
    normalized_candidate_visits = 0
    for bc, bd, cd in itertools.product(permutations, repeat=3):
        # Independently label each matching as a set of forbidden pairs.
        forbidden = [set((x, x) for x in THREE) for _ in range(3)]
        forbidden.extend(set(enumerate(p)) for p in (bc, bd, cd))
        admitted = []
        dropped = {name: [] for name in NAMES}
        for word in FOUR_WORDS:
            candidate_visits += 1
            if all(word[0] != word[k] for k in (1, 2, 3)):
                normalized_candidate_visits += 1
            failures = [idx for idx, (i, j) in enumerate(PAIRS)
                        if (word[i], word[j]) in forbidden[idx]]
            if not failures:
                admitted.append(word)
                for name in NAMES:
                    dropped[name].append(word)
            elif len(failures) == 1:
                dropped[NAMES[failures[0]]].append(word)
        fiber_sizes = tuple(sum(word[0] == a for word in admitted) for a in THREE)
        histogram_total[len(admitted)] += 1
        histogram_fiber.update(fiber_sizes)
        histogram_vector[','.join(map(str, fiber_sizes))] += 1
        cases.append({'BC': bc, 'BD': bd, 'CD': cd, 'fiber_sizes_A012': fiber_sizes,
                      'admissible_tuples': admitted})
        for name in NAMES:
            relaxed = dropped[name]
            drop_hist[name][len(relaxed)] += 1
            drop_fiber_hist[name].update(sum(word[0] == a for word in relaxed) for a in THREE)
            previous = drop_examples.get(name)
            if previous is None or len(relaxed) > previous['count']:
                drop_examples[name] = {'BC': bc, 'BD': bd, 'CD': cd,
                                       'count': len(relaxed), 'admissible_tuples': relaxed}
        if len(admitted) == 12:
            projection_data = {}
            for (i, j), name in zip(PAIRS, NAMES):
                frequencies = collections.Counter((w[i], w[j]) for w in admitted)
                projection_data[name] = {'size': len(frequencies),
                    'extension_multiplicities': histogram(collections.Counter(frequencies.values()))}
            equality_cases.append({'BC': bc, 'BD': bd, 'CD': cd,
                                   'projection_data': projection_data})
        # Check each of the author's fixed-a subcases by direct bad-set construction.
        for a in THREE:
            cube = [(b, c, d) for b, c, d in itertools.product(THREE, repeat=3)
                    if a not in (b, c, d)]
            fix_count = sum(p[a] == a for p in (bc, bd, cd))
            fix_hist[fix_count] += 1
            bad = []
            for (i, j), p in zip(((0, 1), (0, 2), (1, 2)), (bc, bd, cd)):
                bad.append({v for v in cube if v[j] == p[v[i]]})
            for idx, (p, vertices) in enumerate(zip((bc, bd, cd), bad)):
                expected = 4 if p[a] == a else 2
                if len(vertices) != expected:
                    badset_errors.append({'a': a, 'triple': [bc, bd, cd], 'leaf_pair': idx,
                                          'expected_size': expected, 'actual_size': len(vertices)})
                if expected == 2 and len(vertices) == 2:
                    u, v = tuple(vertices)
                    if sum(x != y for x, y in zip(u, v)) != 1:
                        badset_errors.append({'a': a, 'triple': [bc, bd, cd], 'leaf_pair': idx,
                                              'error': 'two-vertex bad set is not a cube edge'})
            if len(cube) - len(set().union(*bad)) != fiber_sizes[a]:
                badset_errors.append({'a': a, 'triple': [bc, bd, cd],
                                      'error': 'bad-set complement differs from direct count'})
    fail_if(len(cases) != 216, 'wrong number of permutation triples')
    fail_if(candidate_visits != 216 * 81, 'incomplete four-tuple visits')
    fail_if(normalized_candidate_visits != 216 * 24, 'incomplete normalized fiber visits')
    fail_if(sum(histogram_fiber.values()) != 216 * 3, 'incomplete fiber histogram')
    equality_good = [x for x in equality_cases if all(
        p['size'] == 6 and p['extension_multiplicities'] == {'2': 6}
        for p in x['projection_data'].values())]
    return {'matching_triples': len(cases), 'A_fibers': sum(histogram_fiber.values()),
            'four_tuple_visits_before_A_constraints': candidate_visits,
            'four_tuple_visits_after_A_constraints': normalized_candidate_visits,
            'total_admissible_tuple_visits': sum(k * v for k, v in histogram_total.items()),
            'total_histogram': histogram(histogram_total),
            'fiber_histogram': histogram(histogram_fiber),
            'ordered_fiber_vector_histogram': {k: histogram_vector[k] for k in sorted(histogram_vector)},
            'max_per_fiber': max(histogram_fiber), 'max_total': max(histogram_total),
            'fix_count_histogram': histogram(fix_hist), 'badset_structure_errors': badset_errors,
            'matching_cases': cases, 'size_12_projection_cases': equality_cases,
            'size_12_cases_with_all_six_exact_degree_two_projections': len(equality_good),
            'drop_one_matching_controls': {name: {'total_histogram': histogram(drop_hist[name]),
                'fiber_histogram': histogram(drop_fiber_hist[name]),
                'maximum': max(drop_hist[name]), 'maximal_example': drop_examples[name]}
                for name in NAMES}}


class PError(ValueError):
    pass


def verify_p(records):
    if not isinstance(records, list) or len(records) != 30:
        raise PError('word_count')
    words = []
    for rec in records:
        if not isinstance(rec, dict) or set(rec) != {'active', 'coordinates'}:
            raise PError('record_shape')
        w = rec['coordinates']
        if not isinstance(w, list) or len(w) != 4 or any(type(x) is not int or not 0 <= x < 6 for x in w):
            raise PError('invalid_coordinate')
        if rec['active'] != [i for i, x in enumerate(w) if x < 3]:
            raise PError('active_metadata')
        words.append(tuple(w))
    if len(set(words)) != 30:
        raise PError('duplicate_word')
    active_hist = collections.Counter(sum(x < 3 for x in w) for w in words)
    if active_hist != {1: 12, 2: 18}:
        raise PError('active_distribution')
    projections = pair_projections(words)
    universe = set(itertools.product(range(6), repeat=2))
    summaries = {}
    for (i, j), name, projection in zip(PAIRS, NAMES, projections):
        if len(projection) != 30:
            raise PError('pair_collision')
        missing = universe - projection
        if len(missing) != 6 or any(a >= 3 or b >= 3 for a, b in missing):
            raise PError('residual_alphabet')
        if any(sum(a == x for a, b in missing) != 2 for x in THREE) or any(
                sum(b == x for a, b in missing) != 2 for x in THREE):
            raise PError('residual_not_2_regular')
        matching = sorted(set(itertools.product(THREE, repeat=2)) - missing)
        summaries[name] = {'P_pair_count': len(projection),
                           'residual_missing_from_P': sorted(missing),
                           'forbidden_active_matching': matching}
    for i in range(4):
        if any(sum(w[i] == x for w in words) != 4 for x in THREE):
            raise PError('active_multiplicity')
    return words, projections, histogram(active_hist), summaries


def diagnostic_controls(raw):
    src = json.loads(raw)
    fail_if(src.get('status') != 'sat', 'P source status is not sat metadata')
    records = src['records']
    words, projections, active_hist, summaries = verify_p(records)
    metadata_checks = {}
    for (i, j), name in zip(PAIRS, NAMES):
        claimed = src['direct_integer_pair_verification'][str(i) + str(j)]
        metadata_checks[name] = (claimed['unique_P_pairs'] == summaries[name]['P_pair_count'] and
                                 claimed['active_active_matching'] == summaries[name]['forbidden_active_matching'])
    all_words = tuple(itertools.product(range(6), repeat=4))
    remaining = list(all_words)
    sequential_counts = {'before_pair_tests': len(remaining)}
    for (i, j), name, projection in zip(PAIRS, NAMES, projections):
        remaining = [w for w in remaining if (w[i], w[j]) not in projection]
        sequential_counts['after_' + name] = len(remaining)
    direct = [w for w in all_words if all((w[i], w[j]) not in proj
                                            for (i, j), proj in zip(PAIRS, projections))]
    fail_if(direct != remaining, 'P direct compatibility differs from sequential test')
    dropped = {}
    for omitted, omitted_name in enumerate(NAMES):
        examples = [w for w in all_words if all((w[i], w[j]) not in proj
                    for idx, ((i, j), proj) in enumerate(zip(PAIRS, projections)) if idx != omitted)]
        dropped[omitted_name] = {'count': len(examples), 'tuples': examples}
    controls = {}
    mutations = []
    mutations.append(('drop_word', records[:-1], 'word_count'))
    m = copy.deepcopy(records); m[1] = copy.deepcopy(m[0])
    mutations.append(('duplicate_word', m, 'duplicate_word'))
    m = copy.deepcopy(records); m[0]['coordinates'][0] = 6
    mutations.append(('out_of_range', m, 'invalid_coordinate'))
    m = copy.deepcopy(records); m[0]['active'] = []
    mutations.append(('incorrect_active_metadata', m, 'active_metadata'))
    collision_mutation = None
    for idx, rec in enumerate(records):
        for coord, old in enumerate(rec['coordinates']):
            for replacement in range(6):
                if replacement == old or (replacement < 3) != (old < 3):
                    continue
                m = copy.deepcopy(records)
                m[idx]['coordinates'][coord] = replacement
                try:
                    verify_p(m)
                except PError as e:
                    if str(e) == 'pair_collision':
                        collision_mutation = (m, {'record': idx, 'coordinate': coord,
                                                  'old': old, 'new': replacement})
                        break
            if collision_mutation:
                break
        if collision_mutation:
            break
    fail_if(collision_mutation is None, 'could not construct pair collision mutation')
    mutations.append(('pair_collision', collision_mutation[0], 'pair_collision'))
    for name, mutated, expected in mutations:
        try:
            verify_p(mutated)
        except PError as e:
            observed = str(e)
        else:
            observed = 'accepted'
        controls[name] = {'expected_error': expected, 'observed': observed,
                          'correct_rejection': observed == expected,
                          'mutated_records_canonical_sha256': json_hash(mutated)}
    controls['pair_collision']['change'] = collision_mutation[1]
    identity = [[x, x] for x in THREE]
    return {'bound_P_sha256': digest(raw), 'source_status_metadata': src['status'],
            'word_count': len(words), 'distinct_word_count': len(set(words)),
            'active_count_histogram': active_hist,
            'per_pair': summaries, 'claimed_direct_summary_matches_parsed_records': metadata_checks,
            'all_six_forbidden_matchings_are_identity': all(
                data['forbidden_active_matching'] == identity for data in summaries.values()),
            'coordinate_symbol_counts': [histogram(collections.Counter(w[i] for w in words))
                                         for i in range(4)],
            'all_6_power_4_tuples_tested': len(all_words),
            'sequential_compatibility_counts': sequential_counts,
            'compatible_E_tuples': direct,
            'drop_one_P_pair_compatibility_controls': dropped,
            'intended_reason_mutations': controls,
            'interpretation': 'A P-only necessary-condition diagnostic; zero compatible E tuples, and no amplitudes or AME witness.'}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: python3 -B finite-enumeration-v1.py NEW_OUTPUT.json')
    out = pathlib.Path(sys.argv[1])
    if out.exists():
        raise SystemExit('output already exists; refusing overwrite')
    start = native_clock()
    sources, p_bytes = bind_sources()
    result = {'scope': 'Finite exact controls only; not a proof of the all-state AME theorem.',
              'start_clock_observed': start, 'manifest_sha256': MANIFEST_SHA,
              'sources_verified_in_manifest_order': sources,
              'script_sha256': digest(pathlib.Path(__file__).read_bytes()),
              'cube': cube_controls(), 'matching': matching_controls(),
              'P_only_diagnostic': diagnostic_controls(p_bytes),
              'before_receipt_write_clock_observed': native_clock()}
    with out.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'start': result['start_clock_observed'],
                      'before_receipt_write': result['before_receipt_write_clock_observed'],
                      'script_sha256': result['script_sha256'],
                      'receipt': str(out), 'receipt_sha256': digest(out.read_bytes()),
                      'matching_total_histogram': result['matching']['total_histogram'],
                      'matching_fiber_histogram': result['matching']['fiber_histogram'],
                      'cube_union_histogram': result['cube']['union_cardinality_histogram'],
                      'P_compatible_E_count': len(result['P_only_diagnostic']['compatible_E_tuples'])}, indent=2))


if __name__ == '__main__':
    main()
