#!/usr/bin/env python3
"""Bounded synthetic controls for checker-v4; never open the scientific ZIP."""
import copy
import hashlib
import importlib.util
import itertools
import json
import os
import signal
import subprocess
import sys
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / 'checker-v4.py'
RECEIPT = ROOT / 'reviewer-controls-result.json'
LIMIT = time.monotonic() + 115


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(obj):
    return (json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()


def save(name, data):
    path = ROOT / name
    with open(path, 'xb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    return path


def require(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def tick():
    if time.monotonic() >= LIMIT:
        raise TimeoutError('CONTROL_TIME_LIMIT')


def stop(_sig, _frame):
    raise TimeoutError('CONTROL_INTERRUPTED_OR_LIMIT')


def expect(fn, exception, reason):
    try:
        fn()
    except exception as exc:
        require(str(exc) == reason, 'WRONG_NEGATIVE_REASON:' + str(exc) + ':expected:' + reason)
        return reason
    raise RuntimeError('NEGATIVE_NOT_REJECTED:' + reason)


def vector(terms):
    out = {}
    for key, value in terms:
        if key:
            out[key] = out.get(key, 0) + value
    return {k: v for k, v in out.items() if v}


def plain_cmi(i, j, k):
    return vector(((k | 1 << i, 1), (k | 1 << j, 1),
                   (k | 1 << i | 1 << j, -1), (k, -1)))


def branch_cmi(branch, i, j, k):
    def coord(mask):
        return 5 * (mask & 1023) + (branch if mask & 1024 else 0)
    return vector(((coord(k | 1 << i), 1), (coord(k | 1 << j), 1),
                   (coord(k | 1 << i | 1 << j), -1), (coord(k), -1)))


def family_controls(c):
    nine = {'type': 'entropy_bitmask', 'variables': list(range(2, 11)), 'nonempty_coordinates': 511}
    nine_scope = {'missing_vertex': 1, 'active_vertices': list(range(2, 11)), 'scale': 1}
    eleven = {'type': 'entropy_bitmask', 'variables': list(range(1, 11)) + ['S'], 'nonempty_coordinates': 2047}
    scalar_scope = {'factors': [1, 2], 'visibility_required': [1]}
    functional = {'type': 'functional_branch', 'coordinate_id': '5*A+b', 'A_vertex_subset_mask': [0, 1023],
                  'b': {'0': 'none', '1': 'S=(A_bit,B_bit)', '2': 'A_bit', '3': 'B_bit', '4': 'A_bit XOR B_bit'},
                  'nonempty_coordinates': 5119}
    scope = {'colors': [0, 1] + [None] * 8, 'coloring': '01--------', 'class_id_zero_based': 0}
    bit = lambda v: 1 << (v - 1)
    n1 = sum(bit(v) for v in (2, 3, 4, 5, 6, 7))
    n2 = sum(bit(v) for v in (1, 3, 7, 9, 10))
    local_selected_1 = sum(bit(v) for v in (2, 3, 4, 5))
    local_all_1 = sum(bit(v) for v in (2, 3, 4, 5, 6, 7))
    local_selected_2 = sum(bit(v) for v in (1, 3))
    tri1 = sum(bit(v) for v in (1, 2, 3))
    def fd(mask, v, state):
        return vector(((mask | bit(v) | state, 1), (mask | state, -1)))
    def fstate(mask, b):
        return vector(((5 * mask + b, 1), (5 * mask, -1)))
    cases = [
        ('n11-cmi', eleven, scalar_scope, ['cmi', 0, 1, 4], 'ge', plain_cmi(0, 1, 4)),
        ('n11-conditional-zero-rank-fd', eleven, scalar_scope, ['conditional-zero-rank-fd', local_selected_1, 1], 'eq', fd(local_selected_1, 1, 1024)),
        ('n11-fd', eleven, scalar_scope, ['fd', 1], 'eq', fd(n1, 1, 0)),
        ('n11-local-fd', eleven, scalar_scope, ['local-fd', 1], 'eq', fd(local_all_1, 1, 1024)),
        ('n11-mixed-local-fd', eleven, scalar_scope, ['mixed-local-fd', 1], 'eq', fd(local_selected_1, 1, 1024)),
        ('n11-syndrome-global-fd', eleven, scalar_scope, ['syndrome-global-fd'], 'eq', {2047: 1, 1023: -1}),
        ('n11-syndrome-neighborhood', eleven, scalar_scope, ['syndrome-neighborhood', 1], 'eq', {n1 | 1024: 1, n1: -1}),
        ('n9-cmi', nine, nine_scope, {'kind': 'cmi', 'i': 0, 'j': 1, 'conditioning_mask': 4, 'multiplier': 2}, 'ge', plain_cmi(0, 1, 4)),
        ('n9-conditional_entropy', nine, nine_scope, {'kind': 'conditional_entropy', 'i': 5, 'multiplier': 2}, 'ge', {511: 1, 479: -1}),
        ('n9-fd', nine, nine_scope, {'kind': 'fd', 'i': 0, 'multiplier': -1}, 'eq', {419: 1, 418: -1}),
        ('functional-aux-determined', functional, scope, ['aux-determined', 2], 'eq', {5117: 1, 5115: -1}),
        ('functional-cmi', functional, scope, ['cmi', 2, 0, 1, 1024], 'ge', branch_cmi(2, 0, 1, 1024)),
        ('functional-data-processing', functional, scope, ['data-processing', 1, 2], 'le', {7: 1, 6: -1}),
        ('functional-local-fd', functional, scope, ['functional-local-fd', 2, 0], 'eq', vector(((5 * (local_selected_2 | bit(2)) + 2, 1), (5 * local_selected_2 + 2, -1)))),
        ('functional-neighborhood', functional, scope, ['functional-neighborhood', 2, 0], 'eq', fstate(n2, 2)),
        ('functional-triangle', functional, scope, ['functional-triangle', 1], 'eq', fstate(tri1, 2)),
        ('functional-gate', functional, scope, ['gate', 1], 'le', vector([(5115, 3), (1, 17)] + [(5 * (1 << i) + 1, -2) for i in range(10)])),
        ('functional-graph-fd', functional, scope, ['graph-fd', 1], 'eq', vector(((5 * (n1 | bit(1)), 1), (5 * n1, -1)))),
        ('functional-mixed-local-fd', functional, scope, ['mixed-local-fd', 1], 'eq', vector(((5 * (local_selected_1 | bit(1)) + 1, 1), (5 * local_selected_1 + 1, -1)))),
        ('functional-mono', functional, scope, ['mono', 2, 0], 'ge', {5117: 1, 5112: -1}),
        ('functional-pair', functional, scope, ['pair-determines-state', 1, 3, 4], 'le', {6: 1, 5: 1, 8: -1, 9: -1}),
        ('functional-state-neighborhood', functional, scope, ['state-neighborhood', 1], 'eq', fstate(n1, 1)),
    ]
    require(len(cases) == 22, 'CONTROL_CASE_COUNT')
    for name, system, sc, descriptor, relation, expected in cases:
        tick()
        got, actual_relation = c.row_vector(descriptor, system, sc)
        require((got, actual_relation) == (expected, relation), 'ROW_FORMULA:' + name + ':' + str(got))
    return [case[0] for case in cases], (nine, nine_scope, eleven, scalar_scope, functional, scope)


def proper_certificate(c):
    # A 3-color decoder identity, expanded independently into elemental CMIs and
    # original induced-graph FDs, not an exporter or archived coefficient vector.
    active = list(range(2, 11))
    groups = [[2, 5, 8], [3, 6, 10], [4, 7, 9]]
    index = {v: i for i, v in enumerate(active)}
    rows = []
    def emit_cmi(x, y, conditioned, weight):
        i, j = sorted((index[x], index[y]))
        k = sum(1 << index[v] for v in conditioned)
        require(x != y and x not in conditioned and y not in conditioned, 'FIXTURE_CMI_OVERLAP')
        name = {'kind': 'cmi', 'i': i, 'j': j, 'conditioning_mask': k, 'multiplier': weight}
        rows.append({'name': name, 'relation': 'ge', 'multiplier': str(weight),
                     'image_vectors': [[[a, b] for a, b in sorted(plain_cmi(i, j, k).items())]]})
    for group in groups:
        for x_pos, x in enumerate(group):
            for y_pos, y in enumerate(group[:x_pos]):
                emit_cmi(x, y, group[:y_pos], 2)
    for gi in range(3):
        for gj in range(gi + 1, 3):
            for x_pos, x in enumerate(groups[gi]):
                for y_pos, y in enumerate(groups[gj]):
                    emit_cmi(x, y, groups[gi][:x_pos] + groups[gj][:y_pos], 1)
    for gi, group in enumerate(groups):
        other = {v for j, g in enumerate(groups) if j != gi for v in g}
        for pos, x in enumerate(group):
            neighbors = c.NEIGHBORS[x] & set(active)
            require(neighbors <= other, 'FIXTURE_GRAPH_COLOR')
            cond = set(neighbors)
            extras = sorted((other | set(group[:pos])) - cond)
            for y in extras:
                emit_cmi(x, y, cond, 1)
                cond.add(y)
            i = index[x]
            k = sum(1 << index[v] for v in neighbors)
            name = {'kind': 'fd', 'i': i, 'multiplier': -1}
            image = vector(((k | (1 << i), 1), (k, -1)))
            rows.append({'name': name, 'relation': 'eq', 'multiplier': '-1',
                         'image_vectors': [[[a, b] for a, b in sorted(image.items())]]})
    expected = {511: -3}
    expected.update({1 << i: 2 for i in range(9)})
    return {'certificate_id': 'D1-synthetic', 'source_member': 'sources/synthetic.json', 'source_index': 0,
            'coordinate_system': {'type': 'entropy_bitmask', 'variables': active, 'nonempty_coordinates': 511},
            'target_vector': [[k, str(v)] for k, v in sorted(expected.items())], 'target_relation': 'ge',
            'action_count': 1, 'actions': [list(range(9))],
            'scope': {'missing_vertex': 1, 'active_vertices': active, 'scale': 1}, 'rows': rows}


def binding_for(record, raw):
    binding = {k: record[k] for k in ('certificate_id', 'source_member', 'source_index', 'coordinate_system', 'scope')}
    binding['record_sha256'] = digest(raw)
    return binding


def cli(mode, paths, output, extra=()):
    cmd = [sys.executable, str(CHECKER), mode]
    for flag, path in paths:
        data = path.read_bytes()
        cmd.extend([flag, str(path), flag + '-sha256', digest(data)])
    cmd += ['--output', str(output), '--time-limit-ms', '10000', '--max-items', '5000'] + list(extra)
    tick()
    result = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    receipt = json.loads(output.read_bytes()) if output.exists() else None
    return {'argv': cmd, 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr,
            'output_sha256': digest(output.read_bytes()) if output.exists() else None, 'receipt': receipt}


def color_fixture(c):
    # Search a tiny synthetic four-factor plane, not the real archive.
    factors = [0, 3, 6, 9]
    for aa in range(1, 16):
        for bb in range(aa + 1, 16):
            cc = aa ^ bb
            if not bb < cc or (aa | bb) != 15:
                continue
            plane = tuple(sorted(sum(1 << factors[i] for i in range(4) if d & (1 << i)) for d in (aa, bb, cc)))
            masks = c.allowed_masks(plane)
            minimal = [m for m in sorted(masks, key=int.bit_count) if not any((q & m) == q for q in masks if q != m)]
            constraints = [[i for i in range(10) if m & (1 << i)] for m in minimal]
            order = sorted(range(10), key=lambda v: -sum(v in q for q in constraints))
            colors = [-1] * 10
            def search(pos):
                tick()
                if pos == len(order):
                    return list(colors)
                v = order[pos]
                for col in range(3):
                    colors[v] = col
                    if all(any(colors[x] < 0 for x in q) or len({colors[x] for x in q}) > 1 for q in constraints):
                        found = search(pos + 1)
                        if found is not None:
                            return found
                colors[v] = -1
                return None
            found = search(0)
            if found is not None:
                return {'plane': list(plane), 'coloring': found, 'allowed_masks': sorted(masks)}
    raise RuntimeError('SYNTHETIC_COLOR_NOT_FOUND')


def archive_fixture(c, record, raw, plane, label, corrupt_member=False, missing_member=False):
    graph = [list(a) for a in c.graph_actions()]
    factor = [a for a in graph if c.factors_of_action(tuple(a)) is not None]
    aid = next(i for i, a in enumerate(graph) if a[0] == 8)
    chosen, visible, _ = c.plane_info(tuple(plane))
    plane_record = {'plane': plane, 'J': sum(1 << (x - 1) for x in chosen), 'W': c.mask_of(visible),
                    'category': 'noncover', 'proof_id': record['certificate_id'], 'missing_vertex': 8,
                    'representative_missing_vertex': 1, 'proper_graph_action': aid}
    graph_data = {'factor_preserving_vertex_actions': factor,
                  'factor_actions_zero_based': [list(c.factors_of_action(tuple(a))) for a in factor],
                  'proper_subgraph_graph_actions_order8': graph,
                  'proper_delete_1_color': {str(v): col for col, group in enumerate(([2, 5, 8], [3, 6, 10], [4, 7, 9])) for v in group},
                  'visibility_generators': [sorted(x) for x in c.VISIBILITY_GENERATORS]}
    members = {
        'sources/synthetic.json': encoded({'synthetic_original': 'contains no certificate projection'}),
        'coefficients/synthetic.jsonl': raw,
        'data/graph.json': encoded(graph_data),
        'data/classes.json': encoded([]),
        'data/four.jsonl': b'',
        'data/planes.jsonl': encoded(plane_record),
    }
    table = [{'member': name, 'sha256': ('0' * 64 if corrupt_member and name == 'sources/synthetic.json' else digest(data)),
              'bytes': len(data), 'role': 'synthetic'} for name, data in members.items()]
    index = [{k: record[k] for k in ('certificate_id', 'source_member', 'source_index', 'coordinate_system', 'scope')}]
    index[0]['rows'] = len(record['rows'])
    categories = {'noncover': 1, 'four_factor': 0, 'full_visibility': 0, 'mixed_visibility': 0, 'residual_functional': 0}
    packet = {'members': table, 'coefficient_certificate_index': index, 'literal_coverage_data': {'category_records': categories}}
    packet_raw = encoded(packet)
    dest = ROOT / ('reviewer-synthetic-' + label + '.zip')
    with open(dest, 'xb') as output:
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            z.writestr('packet-manifest.json', packet_raw)
            for name, data in members.items():
                if not (missing_member and name == 'data/classes.json'):
                    z.writestr(name, data)
        output.flush()
        os.fsync(output.fileno())
    data = dest.read_bytes()
    present = [value for name, value in members.items() if not (missing_member and name == 'data/classes.json')]
    contract = {'sha256': digest(data), 'bytes': len(data), 'members': 1 + len(present),
                'uncompressed': len(packet_raw) + sum(map(len, present)), 'packet_sha256': digest(packet_raw),
                'certificates': 1, 'rows': len(record['rows']), 'planes': 1, 'four_cases': 0, 'classes': 0,
                'coefficient_members': ('coefficients/synthetic.jsonl',), 'graph_member': 'data/graph.json',
                'class_member': 'data/classes.json', 'four_member': 'data/four.jsonl', 'plane_member': 'data/planes.jsonl',
                'fixture_universe': [(1, 2, 3)]}
    source = {'path': 'synthetic fixture', 'sha256': digest(members['sources/synthetic.json']),
              'bytes': len(members['sources/synthetic.json'])}
    return dest, contract, [source]


def run():
    begin = clock()
    checker_sha = digest(CHECKER.read_bytes())
    spec = importlib.util.spec_from_file_location('f257_checker_v4', CHECKER)
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)
    c.DEADLINE = LIMIT
    manifest, declaration_raw, observed = c.verify_sources()
    declaration = c.parse_json(declaration_raw)
    forms, systems = family_controls(c)
    nine, nine_scope, eleven, scalar_scope, functional, scope = systems
    record = proper_certificate(c)
    raw = encoded(record)
    binding = binding_for(record, raw)
    identity = c.verify_identity(record, binding, 5000)
    negatives = {}
    def negative(name, fn, cls, reason):
        negatives[name] = expect(fn, cls, reason)
    broken = copy.deepcopy(declaration)
    broken['all_exported_descriptor_formulas'][0]['EXACT_unweighted_base_formula'] = 'changed'
    negative('declaration_formula', lambda: c.validate_declaration(broken), c.Reject, 'DECLARATION_FORMULA_MISMATCH')
    negative('declaration_hash', lambda: c.guard_declaration_digest(declaration_raw + b' '), c.Reject, 'DECLARATION_SHA_MISMATCH')
    negative('unknown_descriptor', lambda: c.row_vector(['unknown', 1], functional, scope), c.Unknown, "UNSUPPORTED_DESCRIPTOR:('functional_branch', 'unknown')")
    negative('unsupported_alias', lambda: c.row_vector(['branch-cmi', 1], functional, scope), c.Unknown, "UNSUPPORTED_DESCRIPTOR:('functional_branch', 'branch-cmi')")
    negative('descriptor_arity', lambda: c.row_vector(['gate', 1, 2], functional, scope), c.Reject, 'DESCRIPTOR_ARITY')
    negative('gate_selector', lambda: c.row_vector(['gate', 2], functional, scope), c.Reject, 'GATE_BRANCH_NOT_FULL_STATE')
    negative('pair_order', lambda: c.row_vector(['pair-determines-state', 1, 4, 2], functional, scope), c.Reject, 'PAIR_ORDER')
    negative('cmi_order', lambda: c.row_vector(['cmi', 1, 0, 4], eleven, scalar_scope), c.Reject, 'CMI_ORDER_OR_OVERLAP')
    negative('local_singleton_guard', lambda: c.row_vector(['functional-local-fd', 1, 0], functional, scope), c.Reject, 'LOCAL_DECODER_NOT_SINGLETON_COLOR')
    negative('functional_incidence', lambda: c.row_vector(['functional-neighborhood', 2, 1], functional, scope), c.Reject, 'FUNCTIONAL_NOT_INCIDENT')
    negative('state_visibility', lambda: c.row_vector(['state-neighborhood', 2], functional, scope), c.Reject, 'STATE_NOT_VISIBLE')
    negative('scalar_local_subset', lambda: c.row_vector(['conditional-zero-rank-fd', 0, 1], eleven, scalar_scope), c.Reject, 'LOCAL_MASK_MISSING_COMPONENTS')
    negative('missing_selected_factors', lambda: c.row_vector(['mixed-local-fd', 1], eleven, {}), c.Reject, 'SELECTED_FACTORS_REQUIRED')
    negative('scalar_visibility', lambda: c.row_vector(['syndrome-neighborhood', 2], eleven, scalar_scope), c.Reject, 'VISIBILITY_NOT_DECLARED')
    negative('duplicate_json_key', lambda: c.parse_json(b'{"x":1,"x":2}'), c.Reject, 'DUPLICATE_JSON_KEY:x')
    negative('float_json', lambda: c.parse_json(b'{"x":1.0}'), c.Reject, 'FLOAT_OR_NONFINITE_FORBIDDEN')
    negative('duplicate_vector', lambda: c.parse_vector([[1, 1], [1, 2]], 511, False), c.Reject, 'DUPLICATE_VECTOR_COORDINATE')
    negative('bad_rational', lambda: c.fraction('2/2'), c.Reject, 'NONCANONICAL_RATIONAL')
    negative('missing_file', lambda: c.read_pinned(ROOT / 'reviewer-never-created-input', '0' * 64, 8), c.Unknown,
             "INPUT_UNAVAILABLE:[Errno 2] No such file or directory: '" + str(ROOT / 'reviewer-never-created-input') + "'")
    negative('row_cap', lambda: c.verify_identity(record, binding, len(record['rows']) - 1), c.Unknown, 'ROW_CAP')
    for name, change, reason in [
        ('relation', lambda r: r['rows'][0].update(relation='le'), 'ROW_RELATION_MISMATCH'),
        ('sign', lambda r: (r['rows'][0]['name'].update(multiplier=-2), r['rows'][0].update(multiplier='-2')), 'ROW_SIGN'),
        ('inner_weight', lambda r: r['rows'][0]['name'].update(multiplier=7), 'INNER_MULTIPLIER_MISMATCH'),
        ('image', lambda r: r['rows'][0]['image_vectors'][0][0].__setitem__(1, 9), 'IMAGE_VECTOR_MISMATCH:D1-synthetic:row=0:action=0'),
        ('target', lambda r: r['target_vector'][0].__setitem__(1, '9'), 'TARGET_VECTOR_MISMATCH'),
        ('proper_action', lambda r: r['actions'][0].reverse(), 'PROPER_ACTION_NOT_SINGLE_IDENTITY'),
    ]:
        mutant = copy.deepcopy(record)
        change(mutant)
        negative(name, lambda mutant=mutant: c.verify_identity(mutant, binding, 5000), c.Reject, reason)
    old_deadline = c.DEADLINE
    c.DEADLINE = time.monotonic() - 1
    negative('deadline', c.tick, c.Unknown, 'TIME_LIMIT')
    c.DEADLINE = old_deadline
    negative('interrupt', lambda: c.stop(signal.SIGTERM, None), c.Unknown, 'INTERRUPTED_SIGNAL_' + str(signal.SIGTERM))
    negative('same_count_wrong_set', lambda: c.compare_plane_sets([(1, 2, 3)], [(1, 4, 5)], 3), c.Reject, 'PLANE_ACTUAL_SET_MISMATCH')
    record_path = save('reviewer-synthetic-record.json', raw)
    binding_path = save('reviewer-synthetic-binding.json', encoded(binding))
    action = next(list(a) for a in c.graph_actions() if a[0] == 8)
    proof_path = save('reviewer-synthetic-applicability.json', encoded({'kind': 'noncover', 'target_plane': [1, 2, 3], 'target_missing': 8, 'vertex_action': action}))
    plane_path = save('reviewer-synthetic-planes.json', encoded({'dimension': 2, 'planes': [[1, 2, 3]]}))
    color = color_fixture(c)
    color_path = save('reviewer-synthetic-color.json', encoded(color))
    commands = {}
    for mode, paths in [
        ('identity', [('--record', record_path), ('--binding', binding_path)]),
        ('applicability', [('--record', record_path), ('--binding', binding_path), ('--proof', proof_path)]),
        ('planes', [('--record', plane_path)]), ('color', [('--record', color_path)]),
    ]:
        result = cli(mode, paths, ROOT / ('reviewer-synthetic-' + mode + '-result.json'))
        require(result['exit'] == 0 and result['receipt']['status'].startswith('VALID_') and
                result['receipt']['theorem_verdict'] == 'UNKNOWN_SOURCE_PROJECTION_AND_ACTUAL_LAW_APPLICABILITY', 'CLI_FAILED:' + mode + ':' + str(result))
        commands[mode] = result
    archive, contract, source = archive_fixture(c, record, raw, [1, 2, 3], 'valid')
    archive_result = c.verify_archive(archive, contract, 1, 5000, 1, source)
    require(archive_result['planes'] == 1 and archive_result['certificates'] == 1 and
            'source-projection equality' in archive_result['claim'], 'ARCHIVE_RESULT_SCOPE')
    negative('archive_cap', lambda: c.verify_archive(archive, contract, 0, 5000, 1, source), c.Unknown, 'ARCHIVE_CERTIFICATE_CAP')
    wrong, wrong_contract, wrong_source = archive_fixture(c, record, raw, [1, 4, 5], 'wrong-plane')
    negative('archive_same_count_wrong_set', lambda: c.verify_archive(wrong, wrong_contract, 1, 5000, 1, wrong_source), c.Reject, 'PLANE_UNIVERSE_SET_MISMATCH')
    corrupt, corrupt_contract, _ = archive_fixture(c, record, raw, [1, 2, 3], 'bad-member', corrupt_member=True)
    negative('archive_member_hash', lambda: c.verify_archive(corrupt, corrupt_contract, 1, 5000, 1), c.Reject, 'MEMBER_PIN_MISMATCH:sources/synthetic.json')
    missing, missing_contract, _ = archive_fixture(c, record, raw, [1, 2, 3], 'missing-member', missing_member=True)
    negative('archive_member_set', lambda: c.verify_archive(missing, missing_contract, 1, 5000, 1), c.Reject, 'ARCHIVE_MEMBER_SET')
    return {'status': 'SYNTHETIC_CONTROLS_PASS', 'clock_start': begin, 'clock_end': clock(),
            'checker_sha256': checker_sha, 'controls_sha256': digest(Path(__file__).read_bytes()),
            'manifest_sha256': c.MANIFEST_SHA, 'declaration_sha256': c.DECLARATION_SHA,
            'source_bindings': observed, 'formulas_checked': forms, 'proper_identity': identity,
            'record_sha256': digest(raw), 'binding_sha256': digest(binding_path.read_bytes()),
            'synthetic_archive_sha256': contract['sha256'], 'synthetic_archive': archive_result,
            'synthetic_source_projection': 'INTENTIONALLY ABSENT: source JSON contains no certificate; archive result is conditional only',
            'negative_controls': negatives, 'cli': commands,
            'boundary': 'synthetic same-harness controls only; no real archive replay or theorem acceptance'}


def main():
    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGALRM):
        signal.signal(sig, stop)
    signal.setitimer(signal.ITIMER_REAL, 115)
    started = clock()
    try:
        result = run()
        code = 0
    except Exception as exc:
        result = {'status': 'UNKNOWN', 'clock_start': started, 'clock_end': clock(),
                  'reason': type(exc).__name__ + ':' + str(exc), 'checker_sha256': digest(CHECKER.read_bytes()),
                  'controls_sha256': digest(Path(__file__).read_bytes())}
        code = 3
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    payload = (json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + '\n').encode()
    save(RECEIPT.name, payload)
    print(json.dumps({'status': result['status'], 'reason': result.get('reason'), 'receipt': str(RECEIPT),
                      'sha256': digest(payload), 'exit': code}, sort_keys=True))
    return code


if __name__ == '__main__':
    sys.exit(main())
