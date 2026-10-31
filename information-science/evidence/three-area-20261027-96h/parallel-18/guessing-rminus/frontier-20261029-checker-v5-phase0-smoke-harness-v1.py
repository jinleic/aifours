#!/usr/bin/env python3
"""Phase-0-only bounded smoke harness for checker-v5.py (DO NOT RUN before Main's GO).

Real v5 CLI on the five pinned f257 synthetic JSON fixtures, plus direct
consuming-path regression checks of the repaired visibility contract and the
transported delete-1 colouring route (tiny SYNTHETIC in-memory roster; no real
archive byte is opened). One exclusive 0600 receipt; every attempt preserved;
no retry, no cap inflation, no checker edits. Wall <=120 s, one thread, each
child <=20 s. Honest failure on any missing/mutated prerequisite.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import time
import zipfile
from pathlib import Path

OWNER = Path(__file__).resolve().parent
V5_NAME = 'checker-v5.py'
V5_SHA = '8258ab4935e3f42ca74e9dc8e2287b6e31a7ddbcffdfb06fc085a62bdc6f7a06'
MANIFEST_NAME = 'frontier-20261029-checker-v5-phase0-smoke-manifest-v1.json'
WALL_LIMIT_S = 120.0
CHILD_TIMEOUT_S = 20.0
THREAD_ENV = {'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1',
              'VECLIB_MAXIMUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
              'PYTHONDONTWRITEBYTECODE': '1'}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def native_date():
    return subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()


def load_manifest(path):
    raw = path.read_bytes()
    doc = json.loads(raw.decode('utf-8'))
    return doc, sha256(raw)


def check_pin(entry, label, problems):
    path = Path(entry['path'])
    if not path.is_file():
        problems.append(f'{label}:MISSING:{path}')
        return None
    data = path.read_bytes()
    digest = sha256(data)
    if digest != entry['sha256']:
        problems.append(f'{label}:SHA_MISMATCH:{path}')
    if 'bytes' in entry and len(data) != entry['bytes']:
        problems.append(f'{label}:BYTES_MISMATCH:{path}')
    if 'LF' in entry and data.count(b'\n') != entry['LF']:
        problems.append(f'{label}:LF_MISMATCH:{path}')
    return digest


def run_cli_child(spec, results, start):
    name = spec['name']
    argv = [sys.executable] + list(spec['argv'])[1:]  # 'python3' placeholder replaced
    entry = {'name': name, 'kind': 'cli', 'argv': argv,
             'expected_exit': spec['expected_exit'],
             'expected_status': spec['expected_status'],
             'output_path': spec['output_path']}
    if time.monotonic() - start > WALL_LIMIT_S:
        entry.update(outcome='FAIL', actual_exit=None,
                     reason='HARNESS_WALL_BUDGET_EXCEEDED_BEFORE_LAUNCH')
        results.append(entry)
        return
    try:
        proc = subprocess.run(argv, cwd=str(OWNER), capture_output=True,
                              text=True, timeout=CHILD_TIMEOUT_S,
                              env={**os.environ, **THREAD_ENV})
        entry['actual_exit'] = proc.returncode
        entry['stdout_tail'] = proc.stdout[-2000:]
        entry['stderr_tail'] = proc.stderr[-2000:]
        out = Path(spec['output_path'])
        if out.is_file():
            entry['output_sha256'] = sha256(out.read_bytes())
            try:
                doc = json.loads(out.read_text())
                entry['actual_status'] = doc.get('status')
            except Exception as exc:  # noqa: BLE001 - recorded honestly
                entry['actual_status'] = None
                entry['parse_error'] = f'{type(exc).__name__}:{exc}'
        else:
            entry['actual_status'] = None
            entry['output_missing'] = True
        ok = (entry.get('actual_exit') == spec['expected_exit']
              and entry.get('actual_status') == spec['expected_status'])
        entry['outcome'] = 'PASS' if ok else 'FAIL'
    except subprocess.TimeoutExpired as exc:
        entry.update(outcome='FAIL', actual_exit=None,
                     reason='HARNESS_CHILD_TIMEOUT_20S',
                     stdout_tail=(exc.stdout or b'')[-2000:] if isinstance(exc.stdout, (bytes, bytearray)) else str(exc.stdout)[-2000:],
                     stderr_tail=(exc.stderr or b'')[-2000:] if isinstance(exc.stderr, (bytes, bytearray)) else str(exc.stderr)[-2000:])
    except Exception as exc:  # noqa: BLE001 - recorded honestly
        entry.update(outcome='FAIL', actual_exit=None,
                     reason=f'HARNESS_ERROR:{type(exc).__name__}:{exc}')
    entry['wall_s'] = None  # filled by caller loop bookkeeping if needed
    results.append(entry)


def outcome_of(call):
    """Run one direct-API expectation; return a record."""
    try:
        value = call['function']()
        actual = {'returned': call['render'](value) if call.get('render') else repr(value)}
        ok = call['accept'](value)
    except Exception as exc:  # noqa: BLE001 - v5 Reject/Unknown recorded by class
        actual = {'exception': type(exc).__name__, 'reason': str(exc)}
        ok = (type(exc).__name__ == call.get('expect_exception')
              and str(exc) == call.get('expect_reason'))
    return {'name': call['name'], 'kind': 'direct_api',
            'target': call['target'], 'expected': call['expected'],
            'actual': actual, 'outcome': 'PASS' if ok else 'FAIL'}


def roster_zip(rows):
    payload = ''.join(json.dumps(r, separators=(',', ':')) + '\n' for r in rows).encode()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('synthetic/roster.jsonl', payload)
    buf.seek(0)
    entry = {'member': 'synthetic/roster.jsonl', 'sha256': sha256(payload),
             'bytes': len(payload), 'records': len(rows)}
    return zipfile.ZipFile(buf), entry


def direct_api_checks(m, results):
    scalar11 = {'type': 'entropy_bitmask',
                'variables': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'S'],
                'nonempty_coordinates': 2047}
    plane1456 = [16, 40, 56]
    color_g1 = {'2': 0, '3': 1, '4': 2, '5': 0, '6': 1,
                '7': 2, '8': 0, '9': 2, '10': 1}  # spine delete-1 colouring
    swap = (1, 5, 6, 7, 2, 3, 4, 8, 9, 10)
    proper = tuple(sorted(m.graph_actions()))
    identity_aid = proper.index(tuple(range(1, 11)))
    visible1456 = m.plane_info(m.plane_tuple(plane1456))[1]

    def rv(scope):
        return lambda: m.required_visibility(scope)

    calls = [
        {'name': 'visibility-list-only', 'target': 'required_visibility',
         'expected': {'returned': [6]},
         'function': rv({'visibility_required': [6]}),
         'render': lambda v: sorted(v), 'accept': lambda v: sorted(v) == [6]},
        {'name': 'visibility-list-plus-singleton-union', 'target': 'required_visibility',
         'expected': {'returned': [3, 6]},
         'function': rv({'visibility_required': [6], 'syndrome_visibility_vertex': 3}),
         'render': lambda v: sorted(v), 'accept': lambda v: sorted(v) == [3, 6]},
        {'name': 'visibility-singleton-group-orbit', 'target': 'required_visibility',
         'expected': {'returned': [2, 5]},
         'function': rv({'syndrome_visibility_vertex': 2,
                         'group': [list(range(1, 11)), list(swap)]}),
         'render': lambda v: sorted(v), 'accept': lambda v: sorted(v) == [2, 5]},
        {'name': 'visibility-plane-accept-declared-subset', 'target': 'required_visibility',
         'expected': {'returned': sorted(visible1456)},
         'function': rv({'factors': [4, 5, 6], 'syndrome_plane': plane1456,
                         'visibility_required': [2]}),
         'render': lambda v: sorted(v),
         'accept': lambda v: sorted(v) == sorted(visible1456)},
        {'name': 'visibility-plane-reject-declared-invisible', 'target': 'required_visibility',
         'expected': {'exception': 'Reject',
                      'reason': 'DECLARED_VISIBILITY_NOT_VISIBLE_IN_PLANE'},
         'function': rv({'factors': [4, 5, 6], 'syndrome_plane': plane1456,
                         'visibility_required': [6]}),
         'expect_exception': 'Reject',
         'expect_reason': 'DECLARED_VISIBILITY_NOT_VISIBLE_IN_PLANE'},
        {'name': 'visibility-schema-bool-entry', 'target': 'required_visibility',
         'expected': {'exception': 'Reject', 'reason': 'VISIBILITY_REQUIREMENT_SCHEMA'},
         'function': rv({'visibility_required': [True]}),
         'expect_exception': 'Reject',
         'expect_reason': 'VISIBILITY_REQUIREMENT_SCHEMA'},
        {'name': 'row-syndrome-neighborhood-declared-accept', 'target': 'row_vector',
         'expected': {'returned': 'eq row vector'},
         'function': lambda: m.row_vector(['syndrome-neighborhood', 6], scalar11,
                                          {'visibility_required': [6]}),
         'render': lambda v: v[1], 'accept': lambda v: v[1] == 'eq'},
        {'name': 'row-syndrome-neighborhood-undeclared-reject', 'target': 'row_vector',
         'expected': {'exception': 'Reject', 'reason': 'VISIBILITY_NOT_DECLARED'},
         'function': lambda: m.row_vector(['syndrome-neighborhood', 7], scalar11,
                                          {'visibility_required': [6]}),
         'expect_exception': 'Reject', 'expect_reason': 'VISIBILITY_NOT_DECLARED'},
        {'name': 'delete1-color-valid', 'target': 'validate_delete_one_color',
         'expected': {'returned': 'int-keyed dict over vertices 2..10'},
         'function': lambda: m.validate_delete_one_color(dict(color_g1)),
         'render': lambda v: sorted(v), 'accept': lambda v: sorted(v) == list(range(2, 11))},
        {'name': 'delete1-color-adjacent-clash', 'target': 'validate_delete_one_color',
         'expected': {'exception': 'Reject', 'reason': 'DELETE_ONE_COLOR_INVALID'},
         'function': lambda: m.validate_delete_one_color({**color_g1, '3': 0}),
         'expect_exception': 'Reject', 'expect_reason': 'DELETE_ONE_COLOR_INVALID'},
        {'name': 'delete1-color-wrong-domain', 'target': 'validate_delete_one_color',
         'expected': {'exception': 'Reject', 'reason': 'DELETE_ONE_COLOR_SCHEMA'},
         'function': lambda: m.validate_delete_one_color(
             {k: v for k, v in color_g1.items() if k != '10'}),
         'expect_exception': 'Reject', 'expect_reason': 'DELETE_ONE_COLOR_SCHEMA'},
    ]

    def roster_call(row, universe, color):
        z, entry = roster_zip([row])
        return lambda: m.verify_plane_roster(
            z, entry, {m.plane_tuple(list(p)) for p in universe}, {},
            tuple(p for p in proper if m.factors_of_action(p) is not None),
            proper, {}, {}, 10, delete_one_color=color)

    plane23910 = [258, 516, 774]
    row_ok = {'plane': plane1456, 'J': 56, 'W': m.mask_of(visible1456),
              'category': 'noncover', 'proof_id': 'D1-color', 'missing_vertex': 1,
              'representative_missing_vertex': 1, 'proper_graph_action': identity_aid}
    calls += [
        {'name': 'noncover-D1color-transport-success', 'target': 'verify_plane_roster',
         'expected': {'returned': {'noncover': 1, 'four_factor': 0,
                                   'full_visibility': 0, 'mixed_visibility': 0,
                                   'residual_functional': 0}},
         'function': roster_call(row_ok, [plane1456], dict(color_g1)),
         'accept': lambda v: v == {'noncover': 1, 'four_factor': 0,
                                   'full_visibility': 0, 'mixed_visibility': 0,
                                   'residual_functional': 0}},
        {'name': 'noncover-wrong-missing-vertex-guard', 'target': 'verify_plane_roster',
         'expected': {'exception': 'Reject', 'reason': 'NONCOVER_TRANSPORT'},
         'function': roster_call({**row_ok, 'missing_vertex': 8}, [plane1456],
                                 dict(color_g1)),
         'expect_exception': 'Reject', 'expect_reason': 'NONCOVER_TRANSPORT'},
        {'name': 'noncover-D1color-missing-color-argument', 'target': 'verify_plane_roster',
         'expected': {'exception': 'Unknown',
                      'reason': 'MISSING_NONCOVER_DELETE_ONE_COLOR_ARGUMENT'},
         'function': roster_call(row_ok, [plane1456], None),
         'expect_exception': 'Unknown',
         'expect_reason': 'MISSING_NONCOVER_DELETE_ONE_COLOR_ARGUMENT'},
        {'name': 'noncover-missing-category-named', 'target': 'verify_plane_roster',
         'expected': {'exception': 'Unknown',
                      'reason': 'MISSING_NONCOVER_ARGUMENT_CATEGORY:representative=2'},
         'function': roster_call(
             {'plane': plane23910, 'J': 774,
              'W': m.mask_of(m.plane_info(m.plane_tuple(plane23910))[1]),
              'category': 'noncover', 'proof_id': 'D2', 'missing_vertex': 2,
              'representative_missing_vertex': 2,
              'proper_graph_action': identity_aid}, [plane23910], dict(color_g1)),
         'expect_exception': 'Unknown',
         'expect_reason': 'MISSING_NONCOVER_ARGUMENT_CATEGORY:representative=2'},
    ]
    for call in calls:
        results.append(outcome_of(call))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--manifest', default=str(OWNER / MANIFEST_NAME))
    args = parser.parse_args()
    start = time.monotonic()
    receipt_path = Path(args.output)
    problems = []
    manifest_doc = manifest_sha = None
    if receipt_path.exists():
        problems.append(f'RECEIPT_ALREADY_EXISTS:{receipt_path}')
    mpath = Path(args.manifest)
    if not mpath.is_file():
        problems.append(f'MANIFEST_MISSING:{mpath}')
    else:
        manifest_doc, manifest_sha = load_manifest(mpath)
        for label, entry in manifest_doc['pins'].items():
            check_pin(entry, label, problems)
    v5_path = OWNER / V5_NAME
    v5_sha = check_pin({'path': str(v5_path), 'sha256': V5_SHA,
                        'bytes': manifest_doc['pins']['checker_v5']['bytes'],
                        'LF': manifest_doc['pins']['checker_v5']['LF']},
                       'checker_v5', problems) if manifest_doc else None
    results = []
    module = None
    if not problems:
        spec = importlib.util.spec_from_file_location('checker_v5_under_smoke', v5_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for spec_cli in manifest_doc['cli_children']:
            run_cli_child(spec_cli, results, start)
        if time.monotonic() - start <= WALL_LIMIT_S:
            direct_api_checks(module, results)
        else:
            results.append({'name': 'direct-api-block', 'kind': 'direct_api',
                            'outcome': 'FAIL',
                            'reason': 'HARNESS_WALL_BUDGET_EXCEEDED_BEFORE_DIRECT_API',
                            'expected': '15 checks', 'actual': None})
    else:
        results.append({'name': 'prerequisites', 'kind': 'meta', 'outcome': 'FAIL',
                        'reason': '; '.join(problems), 'expected': 'all pins verified',
                        'actual': None})
    passed = sum(1 for r in results if r.get('outcome') == 'PASS')
    failed = sum(1 for r in results if r.get('outcome') != 'PASS')
    receipt = {
        'kind': 'CHECKER_V5_PHASE0_SMOKE_RECEIPT',
        'harness_sha256': sha256(Path(__file__).read_bytes()),
        'manifest_sha256': manifest_sha,
        'checker_v5_sha256': v5_sha,
        'clock_start': native_date(), 'clock_end': None,
        'wall_limit_s': WALL_LIMIT_S, 'child_timeout_s': CHILD_TIMEOUT_S,
        'prerequisite_problems': problems,
        'cli_children': [r for r in results if r.get('kind') == 'cli'],
        'direct_api_checks': [r for r in results if r.get('kind') == 'direct_api'],
        'meta': [r for r in results if r.get('kind') == 'meta'],
        'totals': {'checks': len(results), 'passed': passed, 'failed': failed},
        'budget_exceeded': time.monotonic() - start > WALL_LIMIT_S,
        'scope': ('Phase-0 synthetic smoke of checker-v5 only: four CLI modes on the five '
                  'pinned f257 fixtures plus direct consuming-path regressions with a tiny '
                  'synthetic in-memory roster. No real archive byte opened; no PJ2 --final; '
                  'no r382; no checker edit; no retry. Not a theorem, replay or adoption '
                  'claim.'),
    }
    receipt['clock_end'] = native_date()
    receipt['wall_s'] = round(time.monotonic() - start, 3)
    payload = (json.dumps(receipt, indent=1, sort_keys=True, allow_nan=False) + '\n').encode()
    try:
        fd = os.open(receipt_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
    except OSError as exc:
        print(f'RECEIPT_WRITE_FAILED:{exc}', file=sys.stderr)
        return 3
    print(json.dumps({'totals': receipt['totals'], 'receipt': str(receipt_path),
                      'sha256': sha256(payload)}, sort_keys=True))
    return 0 if (failed == 0 and not problems) else 1


if __name__ == '__main__':
    sys.exit(main())
