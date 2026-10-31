#!/usr/bin/env python3
"""Phase-0-only bounded smoke harness v2 for checker-v5.py (NOT RUN before Main's GO).

v1 preserved unmodified. v2 launch-fix deltas only: graceful child stop via
Popen(start_new_session=True) with PID/PGID retention, child internal timer
15 s, parent soft timeout 16 s, SIGTERM then SIGINT with bounded grace, never
automatic SIGKILL (an unsettled child is reported live for parent intervention
and all later cases stop); clock_start sampled before any work; actual child
durations recorded; root 120 s budget enforced before every CLI launch and
every direct case, drives the exit code, and is deliberately installed as the
imported checker's DEADLINE; every attempted phase yields an honest exclusive
0600 receipt even when setup/import/case construction fails. No real archive
byte is opened; no checker edits; no retry or cap inflation.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import os
import signal
import subprocess
import sys
import time
import zipfile
from pathlib import Path

OWNER = Path(__file__).resolve().parent
V5_NAME = 'checker-v5.py'
V5_SHA = '8258ab4935e3f42ca74e9dc8e2287b6e31a7ddbcffdfb06fc085a62bdc6f7a06'
MANIFEST_NAME = 'frontier-20261029-checker-v5-phase0-smoke-manifest-v2.json'
WALL_LIMIT_S = 120.0
CHILD_INTERNAL_TIMER_MS = 15000
PARENT_SOFT_TIMEOUT_S = 16.0
SIGTERM_GRACE_S = 2.0
SIGINT_GRACE_S = 2.0
PER_CHILD_BUDGET_S = 20.0
THREAD_ENV = {'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1',
              'VECLIB_MAXIMUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
              'PYTHONDONTWRITEBYTECODE': '1'}


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def native_date():
    return subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()


def elapsed(start):
    return time.monotonic() - start


def stop_child_gracefully(proc):
    """SIGTERM -> SIGINT with bounded grace; NEVER SIGKILL.

    Returns (settled, exit_code_or_None, note). An unsettled child is left
    running and reported for parent intervention.
    """
    try:
        proc.terminate()  # SIGTERM to the child itself
        proc.communicate(timeout=SIGTERM_GRACE_S)
        return True, proc.returncode, 'stopped_by_SIGTERM'
    except subprocess.TimeoutExpired:
        pass
    try:
        proc.send_signal(signal.SIGINT)
        proc.communicate(timeout=SIGINT_GRACE_S)
        return True, proc.returncode, 'stopped_by_SIGINT'
    except subprocess.TimeoutExpired:
        pass
    return False, None, 'UNSETTLED_LIVE_CHILD_REPORTED_FOR_PARENT_INTERVENTION'


def run_cli_child(spec, results, state, start):
    name = spec['name']
    argv = [sys.executable] + list(spec['argv'])[1:]  # 'python3' placeholder replaced
    entry = {'name': name, 'kind': 'cli', 'argv': argv,
             'expected_exit': spec['expected_exit'],
             'expected_status': spec['expected_status'],
             'output_path': spec['output_path'],
             'child_internal_timer_ms': CHILD_INTERNAL_TIMER_MS}
    if state['stop_all']:
        entry.update(outcome='FAIL', actual_exit=None, duration_s=None,
                     reason='SKIPPED_AFTER_UNSETTLED_CHILD')
        results.append(entry)
        return
    if elapsed(start) > WALL_LIMIT_S - PER_CHILD_BUDGET_S:
        entry.update(outcome='FAIL', actual_exit=None, duration_s=None,
                     reason='HARNESS_WALL_BUDGET_EXCEEDED_BEFORE_LAUNCH')
        state['budget_exceeded'] = True
        results.append(entry)
        return
    t0 = time.monotonic()
    proc = None
    try:
        proc = subprocess.Popen(argv, cwd=str(OWNER), stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True,
                                env={**os.environ, **THREAD_ENV},
                                start_new_session=True)
        entry['pid'] = proc.pid
        try:
            entry['pgid'] = os.getpgid(proc.pid)
        except OSError as exc:
            entry['pgid'] = None
            entry['pgid_note'] = f'{type(exc).__name__}:{exc}'
        try:
            out, err = proc.communicate(timeout=PARENT_SOFT_TIMEOUT_S)
            entry['actual_exit'] = proc.returncode
            entry['stop_note'] = 'exited_before_soft_timeout'
        except subprocess.TimeoutExpired:
            settled, code, note = stop_child_gracefully(proc)
            entry['stop_note'] = note
            if not settled:
                live_pgid = None
                try:
                    live_pgid = os.getpgid(proc.pid)
                except OSError:
                    pass
                entry.update(outcome='FAIL', actual_exit=None,
                             reason='CHILD_UNSETTLED_AFTER_SIGTERM_AND_SIGINT',
                             live_pid=proc.pid, live_pgid=live_pgid,
                             incomplete=True)
                entry['duration_s'] = round(time.monotonic() - t0, 3)
                state['stop_all'] = True
                results.append(entry)
                return
            entry['actual_exit'] = code
            out = err = ''
        try:
            entry['stdout_tail'] = (out or '')[-2000:]
            entry['stderr_tail'] = (err or '')[-2000:]
        except Exception:  # noqa: BLE001 - cosmetic only
            entry['stdout_tail'] = entry['stderr_tail'] = None
        entry['duration_s'] = round(time.monotonic() - t0, 3)
        path = Path(spec['output_path'])
        if path.is_file():
            raw = path.read_bytes()
            entry['output_sha256'] = sha256(raw)
            try:
                entry['actual_status'] = json.loads(raw.decode('utf-8')).get('status')
            except Exception as exc:  # noqa: BLE001 - recorded honestly
                entry['actual_status'] = None
                entry['parse_error'] = f'{type(exc).__name__}:{exc}'
        else:
            entry['actual_status'] = None
            entry['output_missing'] = True
        ok = (entry.get('actual_exit') == spec['expected_exit']
              and entry.get('actual_status') == spec['expected_status'])
        entry['outcome'] = 'PASS' if ok else 'FAIL'
    except Exception as exc:  # noqa: BLE001 - recorded honestly
        entry.update(outcome='FAIL', reason=f'HARNESS_ERROR:{type(exc).__name__}:{exc}',
                     duration_s=round(time.monotonic() - t0, 3) if proc else None,
                     pid=getattr(proc, 'pid', None))
    results.append(entry)


def outcome_of(call):
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


def build_direct_calls(m):
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

    plane23910 = [258, 516, 774]
    row_ok = {'plane': plane1456, 'J': 56, 'W': m.mask_of(visible1456),
              'category': 'noncover', 'proof_id': 'D1-color', 'missing_vertex': 1,
              'representative_missing_vertex': 1, 'proper_graph_action': identity_aid}

    def roster_call(row, universe, color):
        z, entry = roster_zip([row])
        return lambda: m.verify_plane_roster(
            z, entry, {m.plane_tuple(list(p)) for p in universe}, {},
            tuple(p for p in proper if m.factors_of_action(p) is not None),
            proper, {}, {}, 10, delete_one_color=color)

    return [
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
         'expected': {'returned': 'eq'},
         'function': lambda: m.row_vector(['syndrome-neighborhood', 6], scalar11,
                                          {'visibility_required': [6]}),
         'render': lambda v: v[1], 'accept': lambda v: v[1] == 'eq'},
        {'name': 'row-syndrome-neighborhood-undeclared-reject', 'target': 'row_vector',
         'expected': {'exception': 'Reject', 'reason': 'VISIBILITY_NOT_DECLARED'},
         'function': lambda: m.row_vector(['syndrome-neighborhood', 7], scalar11,
                                          {'visibility_required': [6]}),
         'expect_exception': 'Reject', 'expect_reason': 'VISIBILITY_NOT_DECLARED'},
        {'name': 'delete1-color-valid', 'target': 'validate_delete_one_color',
         'expected': {'returned': 'int-keyed map over vertices 2..10'},
         'function': lambda: m.validate_delete_one_color(dict(color_g1)),
         'render': lambda v: sorted(v),
         'accept': lambda v: sorted(v) == list(range(2, 11))},
        {'name': 'delete1-color-adjacent-clash', 'target': 'validate_delete_one_color',
         'expected': {'exception': 'Reject', 'reason': 'DELETE_ONE_COLOR_INVALID'},
         'function': lambda: m.validate_delete_one_color({**color_g1, '3': 0}),
         'expect_exception': 'Reject', 'expect_reason': 'DELETE_ONE_COLOR_INVALID'},
        {'name': 'delete1-color-wrong-domain', 'target': 'validate_delete_one_color',
         'expected': {'exception': 'Reject', 'reason': 'DELETE_ONE_COLOR_SCHEMA'},
         'function': lambda: m.validate_delete_one_color(
             {k: v for k, v in color_g1.items() if k != '10'}),
         'expect_exception': 'Reject', 'expect_reason': 'DELETE_ONE_COLOR_SCHEMA'},
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--manifest', default=str(OWNER / MANIFEST_NAME))
    args = parser.parse_args()
    start = time.monotonic()
    clock_start = native_date()  # sampled before ANY work
    receipt_path = Path(args.output)
    state = {'stop_all': False, 'budget_exceeded': False}
    problems = []
    results = []
    manifest_doc = manifest_sha = None
    module = None
    v5_sha = None
    try:
        if receipt_path.exists():
            problems.append(f'RECEIPT_ALREADY_EXISTS:{receipt_path}')
        mpath = Path(args.manifest)
        if not mpath.is_file():
            problems.append(f'MANIFEST_MISSING:{mpath}')
        else:
            raw = mpath.read_bytes()
            manifest_doc = json.loads(raw.decode('utf-8'))
            manifest_sha = sha256(raw)
            for label, entry in manifest_doc['pins'].items():
                path = Path(entry['path'])
                if not path.is_file():
                    problems.append(f'{label}:MISSING:{path}')
                    continue
                data = path.read_bytes()
                digest = sha256(data)
                if digest != entry['sha256']:
                    problems.append(f'{label}:SHA_MISMATCH:{path}')
                if 'bytes' in entry and len(data) != entry['bytes']:
                    problems.append(f'{label}:BYTES_MISMATCH:{path}')
                if 'LF' in entry and data.count(b'\n') != entry['LF']:
                    problems.append(f'{label}:LF_MISMATCH:{path}')
                if label == 'checker_v5':
                    v5_sha = digest
        if manifest_doc and not problems:
            spec = importlib.util.spec_from_file_location('checker_v5_under_smoke',
                                                          OWNER / V5_NAME)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if sha256((OWNER / V5_NAME).read_bytes()) != V5_SHA:
                problems.append('checker_v5:SHA_MISMATCH_AFTER_IMPORT')
            else:
                # Deliberate root-budget deadline for every direct case.
                module.DEADLINE = start + WALL_LIMIT_S
            for spec_cli in manifest_doc['cli_children']:
                run_cli_child(spec_cli, results, state, start)
    except Exception as exc:  # noqa: BLE001 - setup failures still yield a receipt
        problems.append(f'SETUP_ERROR:{type(exc).__name__}:{exc}')
        state['stop_all'] = True
    if module is not None and not state['stop_all']:
        try:
            calls = build_direct_calls(module)
        except Exception as exc:  # noqa: BLE001 - construction failure recorded
            results.append({'name': 'direct-api-construction', 'kind': 'meta',
                            'outcome': 'FAIL',
                            'reason': f'DIRECT_CASE_CONSTRUCTION_ERROR:{type(exc).__name__}:{exc}',
                            'expected': '15 constructed calls', 'actual': None})
            calls = []
        for call in calls:
            if state['stop_all']:
                results.append({'name': call['name'], 'kind': 'direct_api',
                                'target': call['target'], 'expected': call['expected'],
                                'actual': None, 'outcome': 'FAIL',
                                'reason': 'SKIPPED_AFTER_UNSETTLED_CHILD'})
                continue
            if elapsed(start) > WALL_LIMIT_S:
                state['budget_exceeded'] = True
                results.append({'name': call['name'], 'kind': 'direct_api',
                                'target': call['target'], 'expected': call['expected'],
                                'actual': None, 'outcome': 'FAIL',
                                'reason': 'HARNESS_WALL_BUDGET_EXCEEDED_BEFORE_CASE'})
                continue
            results.append(outcome_of(call))
    elif module is None and not problems:
        problems.append('MODULE_NOT_IMPORTED_WITHOUT_RECORDED_REASON')
    passed = sum(1 for r in results if r.get('outcome') == 'PASS')
    failed = sum(1 for r in results if r.get('outcome') != 'PASS')
    budget_exceeded = state['budget_exceeded'] or elapsed(start) > WALL_LIMIT_S
    receipt = {
        'kind': 'CHECKER_V5_PHASE0_SMOKE_RECEIPT_V2',
        'harness_sha256': sha256(Path(__file__).read_bytes()),
        'manifest_sha256': manifest_sha,
        'checker_v5_sha256': v5_sha,
        'clock_start': clock_start, 'clock_end': native_date(),
        'wall_limit_s': WALL_LIMIT_S, 'wall_s': round(elapsed(start), 3),
        'child_internal_timer_ms': CHILD_INTERNAL_TIMER_MS,
        'parent_soft_timeout_s': PARENT_SOFT_TIMEOUT_S,
        'per_child_budget_s': PER_CHILD_BUDGET_S,
        'stop_discipline': 'SIGTERM->SIGINT bounded grace; never automatic SIGKILL; unsettled children reported live',
        'prerequisite_problems': problems,
        'budget_exceeded': budget_exceeded,
        'unsettled_child_stopped_all': state['stop_all'],
        'cli_children': [r for r in results if r.get('kind') == 'cli'],
        'direct_api_checks': [r for r in results if r.get('kind') == 'direct_api'],
        'meta': [r for r in results if r.get('kind') == 'meta'],
        'totals': {'checks': len(results), 'passed': passed, 'failed': failed},
        'scope': ('Phase-0 synthetic smoke of checker-v5 only (v2 launch fixes). No real '
                  'archive byte opened; no PJ2 --final; no r382; no checker edit; no '
                  'retry. Not a theorem, replay or adoption claim.'),
    }
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
                      'budget_exceeded': budget_exceeded,
                      'sha256': sha256(payload)}, sort_keys=True))
    if problems:
        return 2
    if failed or budget_exceeded or state['stop_all']:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
