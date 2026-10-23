#!/usr/bin/env python3
"""Independent seed/action replay of the pinned gcDCQS(18^4:2) certificate.

Parent-side standard-library code. No lane module is imported or executed; the lane
seed is read only as data. The certificate is parsed by the parent's own hash-pinned
Format S parser (check_gcdcqs18_definition.py, one directory up).

Labels (lane seed format): group point p = 9a + 3*z1 + z2 with a in Z8 and
z = (z1, z2) in Z3^2, group(p) = a mod 4; stems are 72 and 73.
Group rebuilt from the README description with its own GF(9) arithmetic:
G = <t8, t31, t32, S^2>; t8: a -> a+1 swapping the stems; t31: z1 -> z1+1;
t32: z2 -> z2+1; S = multiplication by 1+i on GF(9) = Z3[i], i^2 = -1, z = z1 + z2*i.
Stem-frame kernel H = <t8^4, t31, t32> (README Lemma K; supplementary check).

Usage: python3 -B replay_seed.py CERT CERT_SHA256 SEED.json SEED_SHA256 NEW_RECEIPT.json [--wrong-t8-fixes-stems]
The flag replaces the described t8 by the near-miss a -> a+1 that fixes both stems.
"""
from collections import Counter, deque
from datetime import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PARSER_PATH = HERE.parent / 'check_gcdcqs18_definition.py'
PARSER_SHA256 = '11fa08bc77362ae853dc5612fdc4b25933ba70e3c50acc7dd73208f91082cba5'
V, N, STEMS = 74, 72, (72, 73)
GENERATOR_NAMES = ('t8', 't31', 't32', 'S^2')
FRAME_GENERATOR_NAMES = ('t8^4', 't31', 't32')
EXPECTED_ORBITS = Counter({288: 44, 144: 13, 72: 7, 18: 1})
SEED_KEYS = {'source', 'source_sha256', 'comment', 'groups', 'generators', 'frame_generators',
             'block_representatives', 'classes_at_0', 'block_orbit_sizes',
             'action_negative_control', 'byte_identical_regeneration'}
CONDITIONS = ('pin', 'parse', 'seed', 'group_description', 'action_description', 'group_seed',
              'action_seed', 'generator_equality', 'expansion', 'colouring', 'frames')


class ReplayError(ValueError):
    def __init__(self, condition, category, reason, details=None):
        super().__init__(reason)
        self.condition = condition
        self.category = category
        self.details = details or {}


def require(test, condition, category, reason, **details):
    if not test:
        raise ReplayError(condition, category, reason, details)


def label(a, z):
    return 9 * (a % 8) + 3 * (z[0] % 3) + z[1] % 3


def coordinates(p):
    return p // 9, (p // 3 % 3, p % 3)


def gf9_times(x, y):
    return ((x[0] * y[0] - x[1] * y[1]) % 3, (x[0] * y[1] + x[1] * y[0]) % 3)


def singer(z):
    return gf9_times((1, 1), z)


def point_map(rule, stem_images):
    return tuple([label(*rule(*coordinates(p))) for p in range(N)] + list(stem_images))


def compose(g, h):
    """Apply h first, then g."""
    return tuple(g[x] for x in h)


def inverse(g):
    result = [0] * V
    for p, q in enumerate(g):
        result[q] = p
    return tuple(result)


def element_order(g):
    identity, power, k = tuple(range(V)), g, 1
    while power != identity:
        power, k = compose(g, power), k + 1
    return k


def closure(generators):
    identity = tuple(range(V))
    seen, queue = {identity}, deque([identity])
    while queue:
        element = queue.popleft()
        for g in generators:
            product = compose(g, element)
            if product not in seen:
                seen.add(product)
                queue.append(product)
    return seen


def image(g, record):
    return tuple(sorted(g[p] for p in record))


def is_point(x):
    return type(x) is int and 0 <= x < V


def described_generators(wrong_t8):
    require(all((x * x + 1) % 3 for x in range(3)), 'group_description', 'group.gf9',
            'x^2 + 1 is reducible over GF(3)')
    orbit, z = [], (1, 0)
    for _ in range(8):
        orbit.append(z)
        z = singer(z)
    require(z == (1, 0) and len(set(orbit)) == 8 and (0, 0) not in orbit, 'group_description',
            'group.singer', 'Multiplication by 1+i is not a Singer cycle of GF(9)', orbit=orbit)
    generators = {
        't8': point_map(lambda a, w: (a + 1, w), STEMS if wrong_t8 else STEMS[::-1]),
        't31': point_map(lambda a, w: (a, (w[0] + 1, w[1])), STEMS),
        't32': point_map(lambda a, w: (a, (w[0], w[1] + 1)), STEMS),
        'S^2': point_map(lambda a, w: (a, singer(singer(w))), STEMS),
    }
    field = {'gf9': 'Z3[i] with i^2 = -1; x^2 + 1 has no root mod 3',
             'singer_orbit_of_1_under_1+i': orbit,
             'S^2_images_of_basis': {'(1,0)': singer(singer((1, 0))), '(0,1)': singer(singer((0, 1)))}}
    return generators, field


def check_group(source, generators, cert):
    condition = 'group_' + source
    for name, g in generators.items():
        require(len(g) == V and sorted(g) == list(range(V)), condition, 'group.permutation',
                'Generator is not a permutation of 0..73', generator_source=source, generator=name)
    G = closure(list(generators.values()))
    require(len(G) == 288, condition, 'group.order', 'Generated group order is not 288',
            generator_source=source, order=len(G))
    groups = [frozenset(Gk) for Gk in cert['groups']]
    parts = set(groups) | {frozenset(STEMS)}
    for element in G:
        require({frozenset(element[p] for p in part) for part in parts} == parts, condition,
                'group.partition', 'A group element does not preserve the stem/group partition',
                generator_source=source, element=list(element))
    identity = tuple(range(V))
    translation_generators = [generators['t8'], generators['t31'], generators['t32']]
    translations = closure(translation_generators)
    multiplier = closure([generators['S^2']])
    stabilizer = {e for e in G if e[0] == 0}
    return G, {
        'status': 'PASS', 'order': len(G), 'elements_checked_for_partition': len(G),
        'generator_orders': {name: element_order(g) for name, g in generators.items()},
        'induced_action_on_groups': {name: [groups.index(frozenset(g[p] for p in Gk)) for Gk in groups]
                                     for name, g in generators.items()},
        'stem_images': {name: [g[72], g[73]] for name, g in generators.items()},
        'translation_subgroup_order': len(translations),
        'translation_generators_commute': all(compose(g, h) == compose(h, g)
                                              for g in translation_generators for h in translation_generators),
        'translations_regular_on_group_points': len(translations) == N
                                                and {e[0] for e in translations} == set(range(N)),
        'translations_normal_in_G': all(compose(compose(g, t), inverse(g)) in translations
                                        for g in generators.values() for t in translations),
        'multiplier_order': len(multiplier),
        'translations_meet_multiplier_trivially': translations & multiplier == {identity},
        'stabilizer_of_point_0_order': len(stabilizer),
        'stabilizer_of_point_0_equals_<S^2>': stabilizer == multiplier,
    }


def check_action(source, generators, blocks):
    block_set = set(blocks)
    for name, g in generators.items():
        bad = [B for B in blocks if image(g, B) not in block_set]
        require(not bad, 'action_' + source, 'action.block_invariance',
                'Certificate block set is not invariant under a generator',
                generator_source=source, generator=name, non_invariant_blocks=len(bad),
                non_invariant_blocks_with_a_stem=sum(any(s in B for s in STEMS) for B in bad),
                examples=[{'block': list(B), 'image': list(image(g, B))} for B in bad[:3]])
    return {'status': 'PASS', 'generators_checked': list(generators),
            'blocks_checked_per_generator': len(blocks)}


def load_seed(raw, cert_sha, cert, cert_line_1):
    try:
        seed = json.loads(raw.decode('utf-8'))
    except (UnicodeDecodeError, ValueError) as exc:
        raise ReplayError('seed', 'seed.json', 'Seed is not UTF-8 JSON') from exc
    require(isinstance(seed, dict) and set(seed) == SEED_KEYS, 'seed', 'seed.keys',
            'Seed keys differ from the documented seed format',
            keys=sorted(seed) if isinstance(seed, dict) else None)
    require(seed['source_sha256'] == cert_sha, 'seed', 'seed.source',
            'Seed is bound to another certificate', seed_source_sha256=seed['source_sha256'])
    require(seed['groups'] == [sorted(Gk) for Gk in cert['groups']], 'seed', 'seed.groups',
            'Seed groups differ from the certificate groups')

    def permutations(rows, names):
        require(isinstance(rows, list) and len(rows) == len(names), 'seed', 'seed.generators',
                'Wrong number of seed generators', expected=len(names))
        result = {}
        for name, row in zip(names, rows):
            require(isinstance(row, list) and len(row) == V and all(is_point(x) for x in row)
                    and len(set(row)) == V, 'seed', 'seed.generators',
                    'Seed generator is not a permutation of 0..73', generator=name)
            result[name] = tuple(row)
        return result

    def record(row, size, what):
        require(isinstance(row, list) and len(row) == size and all(is_point(x) for x in row)
                and len(set(row)) == size, 'seed', 'seed.record', 'Malformed seed record', what=what, record=row)
        return tuple(sorted(row))

    generators = permutations(seed['generators'], GENERATOR_NAMES)
    frame_generators = permutations(seed['frame_generators'], FRAME_GENERATOR_NAMES)
    require(isinstance(seed['block_representatives'], list), 'seed', 'seed.record', 'Representatives are not a list')
    representatives = [record(r, 4, 'block representative') for r in seed['block_representatives']]
    require(len(set(representatives)) == len(representatives), 'seed', 'seed.duplicate_representative',
            'A block representative is repeated')
    rows = seed['classes_at_0']
    require(isinstance(rows, list) and len(rows) == 37 and all(isinstance(C, list) and C for C in rows),
            'seed', 'seed.classes', 'Seed must list 37 nonempty point-0 classes')
    classes = []
    for j, C in enumerate(rows):
        triples = [record(t, 3, 'point-0 class %d triple' % j) for t in C]
        require(len(set(triples)) == len(triples), 'seed', 'seed.classes', 'Repeated triple in a seed class', colour=j)
        classes.append(frozenset(triples))
    claimed = seed['block_orbit_sizes']
    require(isinstance(claimed, dict) and all(isinstance(k, str) and k.isdigit() and type(v) is int
                                               for k, v in claimed.items()),
            'seed', 'seed.orbit_claim', 'Malformed block_orbit_sizes')
    info = {'status': 'PASS', 'keys': sorted(SEED_KEYS), 'generators': len(generators),
            'frame_generators': len(frame_generators), 'block_representatives': len(representatives),
            'point0_classes': len(classes), 'point0_triples': sum(len(C) for C in classes),
            'claimed_orbit_sizes': claimed, 'comment_equals_certificate_line_1': seed['comment'] == cert_line_1,
            'seed_claims_recorded_not_trusted': {'action_negative_control': seed['action_negative_control'],
                                                 'byte_identical_regeneration': seed['byte_identical_regeneration']}}
    return generators, frame_generators, representatives, classes, claimed, info


def check_expansion(G, representatives, blocks, claimed):
    orbits = [frozenset(image(e, r) for e in G) for r in representatives]
    expanded = Counter(B for orbit in orbits for B in orbit)
    certificate = Counter(blocks)
    sizes = Counter(len(orbit) for orbit in orbits)
    info = {'representatives': len(representatives),
            'orbit_size_profile': {str(k): sizes[k] for k in sorted(sizes, reverse=True)},
            'stabilizer_order_profile': {str(288 // k): sizes[k] for k in sorted(sizes, reverse=True)},
            'orbits_pairwise_distinct': len(set(orbits)) == len(orbits),
            'expanded_block_records': sum(expanded.values()), 'expanded_distinct_blocks': len(expanded),
            'blocks_in_two_or_more_orbits': sum(m > 1 for m in expanded.values()),
            'certificate_block_records': sum(certificate.values()), 'certificate_distinct_blocks': len(certificate),
            'missing_from_expansion': sum((certificate - expanded).values()),
            'extra_in_expansion': sum((expanded - certificate).values()),
            'multiset_equal': expanded == certificate}
    require(expanded == certificate, 'expansion', 'expansion.multiset',
            'Expanded block multiset differs from the certificate block multiset', **info,
            missing_examples=[list(B) for B in sorted(certificate - expanded)[:4]],
            extra_examples=[list(B) for B in sorted(expanded - certificate)[:4]])
    require(sizes == EXPECTED_ORBITS, 'expansion', 'expansion.orbit_profile',
            'Orbit sizes differ from 288x44, 144x13, 72x7, 18x1', **info)
    require(Counter({int(k): v for k, v in claimed.items()}) == sizes, 'expansion', 'expansion.seed_claim',
            'Seed block_orbit_sizes differ from the recomputed orbit sizes', **info)
    info['status'] = 'PASS'
    return info


def check_colouring(G, seed_classes, cert):
    certificate = {y: [frozenset(C) for C in cert['points'][y]] for y in range(N)}
    require(seed_classes == certificate[0], 'colouring', 'colouring.seed_point0',
            'Seed point-0 classes differ from certificate POINT 0',
            differing_colours=[j for j in range(37) if seed_classes[j] != certificate[0][j]])
    least = {}
    for element in sorted(G):
        least.setdefault(element[0], element)
    require(sorted(least) == list(range(N)), 'colouring', 'colouring.transitivity',
            'G does not map point 0 onto exactly the 72 group points', images=sorted(least))
    mismatched = []
    for y in range(N):
        moved = [frozenset(image(least[y], t) for t in C) for C in seed_classes]
        if moved != certificate[y]:
            mismatched.append({'point': y, 'colours': [j for j in range(37) if moved[j] != certificate[y][j]]})
    partitions = {y: frozenset(certificate[y]) for y in range(N)}
    ordered_all = partition_all = 0
    for element in G:
        moved = [frozenset(image(element, t) for t in C) for C in seed_classes]
        ordered_all += moved == certificate[element[0]]
        partition_all += frozenset(moved) == partitions[element[0]]
    info = {'points_transported': N,
            'least_element_rule': 'lexicographically least image tuple among the 4 elements g with g(0) = y',
            'least_element_ordered_class_matches': N - len(mismatched),
            'triples_transported_per_point': sum(len(C) for C in seed_classes),
            'all_group_elements': len(G),
            'elements_matching_ordered_classes': ordered_all,
            'elements_matching_unordered_partition': partition_all}
    require(not mismatched, 'colouring', 'colouring.least_element_transport',
            'Least-element transport of the point-0 colouring differs from the certificate',
            **info, mismatched=mismatched[:5])
    info['status'] = 'PASS'
    return info


def check_frames(generators, seed_frame_generators, blocks, cert):
    t8 = generators['t8']
    described = {'t8^4': compose(t8, compose(t8, compose(t8, t8))), 't31': generators['t31'],
                 't32': generators['t32']}
    H = closure(list(described.values()))
    H_seed = closure(list(seed_frame_generators.values()))
    groups = [frozenset(Gk) for Gk in cert['groups']]
    require(len(H) == 18 and H == H_seed, 'frames', 'frames.kernel',
            'Frame kernel is not the order-18 group generated by t8^4, t31, t32',
            order=len(H), seed_order=len(H_seed), equal_to_seed=H == H_seed)
    require(all(h[72] == 72 and h[73] == 73 and all(frozenset(h[p] for p in Gk) == Gk for Gk in groups)
                for h in H), 'frames', 'frames.kernel_action', 'Kernel does not fix the stems and every group')
    require(all({h[min(Gk)] for h in H} == set(Gk) for Gk in groups), 'frames', 'frames.kernel_regular',
            'Kernel is not regular on every group')
    base = set(range(N))
    group_of = {p: k for k, Gk in enumerate(groups) for p in Gk}
    per_stem = []
    for alpha in STEMS:
        derived = {tuple(p for p in B if p != alpha) for B in blocks if alpha in B}
        remaining, orbits = set(derived), []
        while remaining:
            first = min(remaining)
            orbit = frozenset(image(h, first) for h in H)
            require(orbit <= remaining, 'frames', 'frames.kernel_invariance',
                    'Stem derived design is not invariant under the kernel', stem=alpha, triple=list(first))
            remaining -= orbit
            covered = set().union(*orbit)
            missing = set(range(4)) - {group_of[p] for p in covered}
            k = min(missing) if len(missing) == 1 else None
            require(len(orbit) == 18 and k is not None and covered == base - groups[k], 'frames',
                    'frames.orbit_not_parallel_class',
                    'A kernel orbit is not a parallel class of X minus S and one group',
                    stem=alpha, orbit_size=len(orbit), missing_groups=sorted(missing))
            orbits.append((k, orbit))
        certificate = Counter((k, frozenset(C)) for k, C in cert['stems'][alpha])
        mine = Counter(orbits)
        require(mine == certificate, 'frames', 'frames.certificate_mismatch',
                'Kernel-orbit frames differ from the certificate frames', stem=alpha,
                missing=sum((certificate - mine).values()), extra=sum((mine - certificate).values()))
        per_stem.append({'stem': alpha, 'derived_triples': len(derived), 'kernel_orbits': len(orbits),
                         'orbits_per_missing_group': [sum(k == j for k, _ in orbits) for j in range(4)],
                         'equal_to_certificate_frames': True})
    return {'status': 'PASS', 'scope': 'supplementary: certificate stem frames equal the kernel orbits (README Lemma K)',
            'kernel_order': len(H), 'kernel_equals_seed_frame_group': True,
            'kernel_generator_arrays_equal_seed': {name: described[name] == seed_frame_generators[name]
                                                   for name in FRAME_GENERATOR_NAMES},
            'per_stem': per_stem}


def main():
    args = sys.argv[1:]
    wrong_t8 = '--wrong-t8-fixes-stems' in args
    args = [a for a in args if a != '--wrong-t8-fixes-stems']
    if len(args) != 5:
        raise SystemExit(__doc__)
    cert_path, cert_sha, seed_path, seed_sha, receipt = args
    if Path(receipt).exists():
        raise SystemExit('Refusing to overwrite receipt')
    started = time.perf_counter()
    conditions = {name: {'status': 'NOT_RUN'} for name in CONDITIONS}
    phases = {}
    result = {'replay': 'Independent parent seed/action replay; lane code neither imported nor executed',
              'replay_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'parser': str(PARSER_PATH), 'parser_sha256_expected': PARSER_SHA256,
              'certificate': str(Path(cert_path).resolve()), 'seed': str(Path(seed_path).resolve()),
              'expected_certificate_sha256': cert_sha, 'expected_seed_sha256': seed_sha,
              'variant': 'wrong-t8-fixes-stems' if wrong_t8 else 'as-described',
              'python_optimization': sys.flags.optimize,
              'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'conditions': conditions, 'phase_seconds': phases}
    clock = [time.perf_counter()]

    def lap(name):
        now = time.perf_counter()
        phases[name] = now - clock[0]
        clock[0] = now

    try:
        cert_raw = Path(cert_path).read_bytes()
        seed_raw = Path(seed_path).read_bytes()
        parser_raw = PARSER_PATH.read_bytes()
        digests = {'certificate': hashlib.sha256(cert_raw).hexdigest(),
                   'seed': hashlib.sha256(seed_raw).hexdigest(),
                   'parser': hashlib.sha256(parser_raw).hexdigest()}
        result['observed_sha256'] = digests
        require(digests['certificate'] == cert_sha, 'pin', 'pin.certificate', 'Certificate SHA256 mismatch')
        require(digests['seed'] == seed_sha, 'pin', 'pin.seed', 'Seed SHA256 mismatch')
        require(digests['parser'] == PARSER_SHA256, 'pin', 'pin.parser', 'Parent parser SHA256 mismatch')
        conditions['pin'] = dict(status='PASS', **digests)
        lap('pin')
        spec = importlib.util.spec_from_file_location('parent_gcdcqs18_definition', PARSER_PATH)
        parser = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(parser)
        try:
            text = cert_raw.decode('ascii')
            cert = parser.Parser(text).parse()
        except (UnicodeDecodeError, parser.CertificateError) as exc:
            raise ReplayError('parse', 'parse.certificate', 'Certificate is rejected by the parent Format S parser',
                              parser_reason=str(exc)) from exc
        blocks = cert['blocks']
        conditions['parse'] = {'status': 'PASS', 'block_records': len(blocks),
                               'group_points_with_colourings': len(cert['points']),
                               'stem_points_with_frames': len(cert['stems'])}
        lap('parse')
        seed_generators, seed_frame_generators, representatives, seed_classes, claimed, info = \
            load_seed(seed_raw, digests['certificate'], cert, text.split('\n', 1)[0])
        conditions['seed'] = info
        lap('seed')
        require(cert['groups'] == [{p for p in range(N) if p // 9 % 4 == k} for k in range(4)]
                and cert['stem'] == set(STEMS), 'group_description', 'group.labelling',
                'Certificate groups/stems do not match the coordinate labelling')
        generators, field = described_generators(wrong_t8)
        G, info = check_group('description', generators, cert)
        conditions['group_description'] = {**info, **field,
                                           'generators': {n: list(g) for n, g in generators.items()}}
        conditions['action_description'] = check_action('description', generators, blocks)
        lap('group_and_action_description')
        G_seed, info = check_group('seed', seed_generators, cert)
        conditions['group_seed'] = info
        conditions['action_seed'] = check_action('seed', seed_generators, blocks)
        lap('group_and_action_seed')
        same = {name: generators[name] == seed_generators[name] for name in GENERATOR_NAMES}
        require(G == G_seed, 'generator_equality', 'generators.group_mismatch',
                'Described group differs from the seed group', generator_arrays_equal=same)
        conditions['generator_equality'] = {'status': 'PASS', 'groups_equal_as_permutation_sets': True,
                                            'generator_arrays_equal': same}
        lap('generator_equality')
        conditions['expansion'] = check_expansion(G, representatives, blocks, claimed)
        lap('expansion')
        conditions['colouring'] = check_colouring(G, seed_classes, cert)
        lap('colouring')
        conditions['frames'] = check_frames(generators, seed_frame_generators, blocks, cert)
        lap('frames')
        result['status'], rc = 'PASS', 0
    except ReplayError as exc:
        conditions[exc.condition] = {'status': 'FAIL', 'category': exc.category, 'reason': str(exc),
                                     'details': exc.details}
        result.update(status='FAIL', error_type=type(exc).__name__, condition=exc.condition,
                      category=exc.category, reason=str(exc), details=exc.details)
        rc = 1
    result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    result['runtime_seconds'] = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result['peak_rss_bytes'] = int(rss if sys.platform == 'darwin' else rss * 1024)
    with Path(receipt).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'condition': result.get('condition'),
                      'category': result.get('category'), 'runtime_seconds': result['runtime_seconds'],
                      'peak_rss_bytes': result['peak_rss_bytes']}))
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
