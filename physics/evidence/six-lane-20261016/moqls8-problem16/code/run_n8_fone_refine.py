"""One child per invocation under frozen refinement r2. No source case changes.
Legacy R.certify is UNCHANGED; only ordered unit suffix/len(header) differ.
All outputs are producer candidates; parent measured-feed replay alone counts
final refutations. Source16 pass finishes first; pilot closure gates later
families. L1 then L2 BFS, no L3/retry, shared10400active-s/80MB family budget.
This worker is never launched directly: launch_n8_fone_refine_r4.py holds the
capacity lock and the pinned external supervisor around ALL preparation and
native work. Its post-qualification alone can close a producer tree.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import stat
import threading
import time
from datetime import datetime
from pathlib import Path
import darwin_process_metrics as metrics

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / 'evidence/n8_one_p4_template_runs_v1'
REFINES = RUNS / 'refine_v4'
SOURCE_SHA = '374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9'
DESIGN_SHA = 'bf9f71937d7fcc98fceb26b3aaf05505d8df68bdc5005fe90b61c9fb74422d1a'
R_SHA = '00435386034f9b1e60bbdf21d113ded9947cf2455c7b5f679e1734ed86bae3e9'
C_SHA = '9326589645ce7d871b4b1595d3c465577d1aee9f27143d43a2b8000c14d022c7'
F_SHA = '61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400'
DEADLINE = datetime.fromisoformat('2026-10-18T18:31:43-07:00').timestamp()
CAP = 10400
FAMILY_BYTES = 80000000
CHILD_BYTES = 10000000
FLOOR = 12200000000
LANE_CAP = 10200547328


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load(name, expected=None):
    path = ROOT / 'code' / (name + '.py')
    if expected and sha(path.read_bytes()) != expected:
        raise RuntimeError('frozen module changed: ' + name)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def new_json(path, obj):
    raw = json.dumps(obj, indent=1).encode()
    with path.open('xb') as f:
        f.write(raw)
    return sha(raw)


def disk_bytes(path):
    r = subprocess.run(['du', '-sk', str(path)], capture_output=True, text=True, check=True)
    return int(r.stdout.split()[0]) * 1024


def family_bytes(out, template):
    total = disk_bytes(out)
    prior = RUNS / 'refine_v3' / template
    if prior != out and prior.is_dir():
        total += disk_bytes(prior)
    patterns = ('N8_FONE_R[34].' + template + '.*', 'N8_PREFLIGHT_R4.' + template + '.*',
                'N8_PREFLIGHT_R3.pilot-' + template.replace('-', '') + '-*')
    for pattern in patterns:
        for path in (ROOT / 'evidence').glob(pattern):
            if path.is_file():
                total += path.stat().st_blocks * 512
    return total


def source_cases(B, C):
    design, cases = B.load_inputs()
    raw = (RUNS / 'RESULTS.jsonl').read_bytes()
    rows = [json.loads(x) for x in raw.splitlines() if x.strip()]
    if len(rows) != 16 or len({r['id'] for r in rows}) != 16 or {r['id'] for r in rows} != set(cases):
        raise SystemExit('DEFERRED: unchanged16-case source pass must finish first')
    for r in rows:
        x = cases[r['id']]
        if (r.get('manifest_sha256') != B.WMAN_SHA or r.get('base_cnf_sha256') != SOURCE_SHA
                or r.get('units') != x['units'] or r.get('cnf_sha256') != x['cnf_sha256']):
            raise RuntimeError('source receipt/WMAN identity mismatch')
    byid = {r['id']: r for r in rows}
    order = list(cases)
    unknown = [i for i in order if not C.strict_ok(byid[i])
               and byid[i].get('solver_returncode') != 10
               and 's SATISFIABLE' not in byid[i].get('solver_status_lines', [])]
    queue = ['P1-B1'] + [i for i in unknown if i != 'P1-B1']
    if 'P1-B1' not in unknown:
        raise SystemExit('Pilot source is not UNKNOWN; parent decision needed')
    return cases, byid, queue, sha(raw)


def latest(out):
    files = sorted(out.glob('LEDGER.v*.json'))
    if not files:
        return None, None
    raw = files[-1].read_bytes()
    return json.loads(raw), sha(raw)


def leaves(L):
    return [n for n in L['nodes'].values() if n['state'] != 'REFINED']


def closure(L):
    ts = leaves(L)
    return bool(ts) and all(n['state'] == 'LEGACY_CANDIDATE' and n.get('outer_completed_cleanly') is True for n in ts)


def model_check(text, body, units, nv):
    values = bytearray(nv + 1)
    for line in text.splitlines():
        if not line.startswith('v '):
            continue
        for token in line.split()[1:]:
            x = int(token)
            if not x:
                continue
            if not 1 <= abs(x) <= nv:
                return False
            value = 1 if x > 0 else 2
            if values[abs(x)] not in (0, value):
                return False
            values[abs(x)] = value
    for line in io.BytesIO(body):
        cl = map(int, line.split()[:-1])
        if not any(values[abs(x)] == (1 if x > 0 else 2) for x in cl):
            return False
    return all(values[abs(x)] == (1 if x > 0 else 2) for x in units)




def read_admission(path, expected):
    raw = Path(path).read_bytes()
    if sha(raw) != expected:
        raise RuntimeError('parent admission changed/revoked; no native launch')
    grant = json.loads(raw)
    if (grant.get('status') != 'DRAINED_RESERVED' or grant.get('owner') != 'PhysDepolarizing'
            or grant.get('lane_path') != str(ROOT) or grant.get('held_until_explicit_release') is not True
            or not grant.get('parent_process_markers') or not grant.get('family_scope')):
        raise RuntimeError('not a parent native-idle/reserved admission for this lane')
    release = grant.get('released_if_this_file_exists')
    if not release or Path(release).exists():
        raise RuntimeError('parent admission released or lacks immutable release-marker binding')
    return {'path': str(Path(path).resolve()), 'sha256': expected, 'grant': grant}




def capacity_available(snapshot, own_cap=6 * 2 ** 30):
    return (snapshot['foreign_RSS_bytes'] + own_cap <= 8 * 2 ** 30
            and snapshot['foreign_native_count'] + 2 <= 4)


def require_supervisor():
    script = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py')
    expected = '0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d'
    if (os.environ.get('K3_SUPERVISOR_PID') != str(os.getppid())
            or os.environ.get('K3_SUPERVISOR_SCRIPT') != str(script)
            or not os.environ.get('K3_SUPERVISOR_RECORD') or sha(script.read_bytes()) != expected
            or os.getpgrp() != os.getpid() or os.getsid(0) != os.getpid()):
        raise RuntimeError('whole-controller pinned owned-group supervisor required')
    return {'script': str(script), 'sha256': expected, 'record': os.environ['K3_SUPERVISOR_RECORD'],
            'PID': os.getppid()}


def prepare_directories(out, template, pins, source_hash, init_root, init_family):
    root_identity = {'schema': 'n8-fone-refinement-root/3', 'base_sha256': SOURCE_SHA, 'design_sha256': DESIGN_SHA}
    if init_root:
        REFINES.mkdir()
        new_json(REFINES / 'INIT.json', root_identity)
    elif json.loads((REFINES / 'INIT.json').read_bytes()) != root_identity:
        raise RuntimeError('existing refinement root has no matching recorded identity')
    identity = {'schema': 'n8-fone-refinement-family/3', 'template': template,
                'source16_results_sha256': source_hash, 'source_pins': pins}
    if init_family:
        out.mkdir()
        for name in ('cnf_s', 'cnf_c', 'proof'):
            os.mkfifo(out / ('w0.%s.fifo' % name))
        new_json(out / 'INIT.json', identity)
    else:
        if not out.is_dir() or json.loads((out / 'INIT.json').read_bytes()) != identity:
            raise RuntimeError('reuse requires the recorded existing family identity')
        for name in ('cnf_s', 'cnf_c', 'proof'):
            if not stat.S_ISFIFO((out / ('w0.%s.fifo' % name)).stat().st_mode):
                raise RuntimeError('recorded FIFO absent or replaced')


def import_source_epoch(path, expected, template, source_hash, units42, pins):
    raw = Path(path).read_bytes()
    if sha(raw) != expected or expected != '295da85e9ea32a738dc57096d16c900854cd55de7165e107d781928f659753a0':
        raise RuntimeError('source-epoch continuation anchor mismatch')
    L = json.loads(raw)
    if (L['template'] != template or L['base_sha256'] != SOURCE_SHA or L['design_sha256'] != DESIGN_SHA
            or L['source16_results_sha256'] != source_hash or L['source_template_units'] != units42
            or L['status'] != 'STOP_OUTER_UNKNOWN'):
        raise RuntimeError('source-epoch continuation has different logical inputs/status')
    L['source_epoch_parent'] = {'path': str(Path(path).resolve()), 'sha256': expected,
                                'old_status': L['status'], 'active_seconds_carried': L['active_seconds']}
    L['version'] = 0
    L['prev_sha256'] = None
    L['source_pins'] = pins
    L['status'] = 'OPEN'
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--template', required=True)
    ap.add_argument('--release', action='store_true', help='only after explicit parent resource release')
    ap.add_argument('--admission', required=True, help='parent-owned live DRAINED_RESERVED receipt')
    ap.add_argument('--admission-sha256', required=True)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--init-family', action='store_true')
    mode.add_argument('--reuse-family', action='store_true')
    ap.add_argument('--init-root', action='store_true')
    ap.add_argument('--rss-cap', type=int, required=True)
    ap.add_argument('--continue-from')
    ap.add_argument('--continue-sha256')
    a = ap.parse_args()
    step_start = time.monotonic()
    supervisor = require_supervisor()
    if not 0 < a.rss_cap <= 6 * 2 ** 30:
        raise RuntimeError('invalid admitted own RSS cap')
    admission = read_admission(a.admission, a.admission_sha256)
    if a.template not in admission['grant']['family_scope']:
        raise RuntimeError('this parent reservation does not cover the requested family')
    shared_markers = [str(ROOT)] + admission['grant']['parent_process_markers']
    B = load('n8_fone_refine_bytes')
    C = load('k5_cover', C_SHA)
    cases, source, queue, source_hash = source_cases(B, C)
    if a.template not in queue:
        raise SystemExit('not an eligible UNKNOWN source template')
    # Queue order cannot skip the pilot or an earlier open family.
    for prev in queue[:queue.index(a.template)]:
        old, _ = latest(REFINES / prev)
        if (not old or old.get('status') != 'CANDIDATE_CLOSED' or not closure(old)
                or old.get('design_sha256') != DESIGN_SHA or old.get('source16_results_sha256') != source_hash
                or old.get('WMAN_sha256') != B.WMAN_SHA or old.get('base_sha256') != SOURCE_SHA):
            raise SystemExit('DEFERRED: earlier family/pilot has not closed under these inputs: ' + prev)
    out = REFINES / a.template
    source_pins = {'controller_sha256': sha(Path(__file__).read_bytes()),
                   'helper_sha256': sha((ROOT / 'code/n8_fone_refine_bytes.py').read_bytes()),
                   'legacy_executor_sha256': R_SHA, 'strict_predicate_sha256': C_SHA, 'producer_sha256': F_SHA,
                   'process_metrics_sha256': sha((ROOT / 'code/darwin_process_metrics.py').read_bytes())}
    if B.DESIGN_SHA != DESIGN_SHA:
        raise RuntimeError('helper design identity differs')
    if a.init_family and (shutil.disk_usage(ROOT).free - FAMILY_BYTES < FLOOR
                          or disk_bytes(ROOT) + FAMILY_BYTES > LANE_CAP):
        info = {'template': a.template, 'status': 'DEFERRED_INITIAL_GROWTH', 'native_launched': False,
                'source_pins': source_pins, 'source16_results_sha256': source_hash}
        new_json(ROOT / 'evidence' / ('N8_INITIAL_DEFERRED_R4.' + str(time.time_ns()) + '.json'), info)
        print(json.dumps(info))
        return
    prepare_directories(out, a.template, source_pins, source_hash, a.init_root, a.init_family)
    L, lh = latest(out)
    if a.continue_from:
        if L is not None or not a.init_family or not a.continue_sha256:
            raise RuntimeError('continuation is explicit initial import into a NEW family epoch only')
        L = import_source_epoch(a.continue_from, a.continue_sha256, a.template, source_hash,
                                cases[a.template]['units'], source_pins)
    if L is None:
        initial_defer = out / 'INITIAL_DEFERRED.json'
        if initial_defer.exists() and not a.release:
            raise SystemExit('DEFERRED: initial resource deferral needs explicit parent release')
        free = shutil.disk_usage(ROOT).free
        lane_used = disk_bytes(ROOT)
        reason = None
        if free - FAMILY_BYTES < FLOOR or lane_used + FAMILY_BYTES > LANE_CAP:
            reason = 'DEFERRED_DISK'
        elif time.time() + CAP + 30 > DEADLINE:
            reason = 'DEFERRED_AUTHORISATION'
        if reason:
            info = {'template': a.template, 'status': reason, 'free': free, 'lane_bytes': lane_used,
                    'design_sha256': DESIGN_SHA, 'source16_results_sha256': source_hash,
                    'child_launched': False, 'source_pins': source_pins}
            if not initial_defer.exists():
                new_json(initial_defer, info)
            print(json.dumps(info))
            return
    if L is None:
        L = {'schema': 'n8-fone-refinement-ledger/2', 'version': 0, 'prev_sha256': None,
             'template': a.template, 'design_sha256': DESIGN_SHA, 'WMAN_sha256': B.WMAN_SHA,
             'base_sha256': SOURCE_SHA, 'source16_results_sha256': source_hash,
             'source_template_units': cases[a.template]['units'], 'source_template_sha256': cases[a.template]['cnf_sha256'],
             'active_seconds': 0.0, 'status': 'OPEN', 'nodes': {}, 'counting': 'legacy scheduling only; parent F4 required'}
        L['source_pins'] = source_pins
        for b in range(8):
            i = a.template + '.L1.%03d' % b
            L['nodes'][i] = {'id': i, 'level': 1, 'b': b, 'c': None, 'ancestor': a.template,
                            'state': 'UNSTARTED', 'receipt': None}
    elif (L['design_sha256'] != DESIGN_SHA or L['WMAN_sha256'] != B.WMAN_SHA
          or L['base_sha256'] != SOURCE_SHA or L['source16_results_sha256'] != source_hash
          or L['source_template_units'] != cases[a.template]['units'] or L.get('source_pins') != source_pins):
        raise RuntimeError('resume identity differs')

    if admission['sha256'] not in [x['sha256'] for x in L.get('admissions', [])]:
        L.setdefault('admissions', []).append(admission)
    def save():
        nonlocal L, lh
        L['prev_sha256'] = lh
        L['version'] += 1
        L['writer_sha256'] = sha(Path(__file__).read_bytes())
        lh = new_json(out / ('LEDGER.v%03d.json' % L['version']), L)

    if not L['version']:
        save()
    if list(out.glob('EMERGENCY.*.json')):
        raise SystemExit('BLOCKED: emergency guard evidence needs parent disposition')
    if L['status'].startswith('DEFERRED'):
        if not a.release:
            raise SystemExit('DEFERRED: explicit parent release required; no polling')
        L['status'] = 'OPEN'
        save()
    if L['status'] != 'OPEN':
        print(json.dumps({'family': a.template, 'status': L['status'], 'candidate_closed': closure(L), 'ledger_sha256': lh}))
        return
    if any(n['state'] == 'RUNNING' for n in L['nodes'].values()):
        raise SystemExit('BLOCKED: interrupted RUNNING node; do not repeat without parent decision')

    pending = sorted((n for n in L['nodes'].values() if n['state'] == 'UNSTARTED'),
                     key=lambda n: (n['level'], n['b'], -1 if n['c'] is None else n['c']))
    if not pending:
        L['status'] = 'CANDIDATE_CLOSED' if closure(L) else 'STOP_OPEN_UNKNOWN'
        save()
        print(json.dumps({'family': a.template, 'status': L['status'], 'ledger_sha256': lh}))
        return
    n = pending[0]
    free = shutil.disk_usage(ROOT).free
    if (free - CHILD_BYTES < FLOOR or family_bytes(out, a.template) + CHILD_BYTES > FAMILY_BYTES
            or disk_bytes(ROOT) + CHILD_BYTES > LANE_CAP):
        L['status'] = 'DEFERRED_DISK'
        save()
        print(json.dumps({'family': a.template, 'status': L['status'], 'free': free, 'ledger_sha256': lh}))
        return
    remaining = CAP - L['active_seconds'] - (time.monotonic() - step_start)
    if remaining < 1230 or time.time() + 1230 > DEADLINE:
        L['status'] = 'STOP_BUDGET'
        save()
        print(json.dumps({'family': a.template, 'status': L['status'], 'remaining': remaining, 'ledger_sha256': lh}))
        return

    F = load('n8_one_p4_formula', F_SHA)
    R = load('k5_resplit_r3', R_SHA)
    solver_path = shutil.which('cadical')
    runtime_binaries = {'solver_path': solver_path, 'solver_sha256': sha(Path(solver_path).read_bytes()),
                        'checker_path': R.DT, 'checker_sha256': sha(Path(R.DT).read_bytes())}
    if (runtime_binaries['solver_sha256'] != '601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa'
            or runtime_binaries['checker_sha256'] != '111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4'):
        raise RuntimeError('frozen native binary identity differs')
    base, _ = F.build()
    if base.sha != SOURCE_SHA:
        raise RuntimeError('actual weak base mismatch')
    admission = read_admission(a.admission, a.admission_sha256)
    before_native = metrics.shared_snapshot(shared_markers)
    if not capacity_available(before_native, a.rss_cap):
        L['status'] = 'DEFERRED_SHARED'
        L['shared_deferral'] = {'admission': admission, 'snapshot': before_native}
        L['active_seconds'] += time.monotonic() - step_start
        save()
        print(json.dumps({'family': a.template, 'status': L['status'], 'snapshot': before_native,
                          'ledger_sha256': lh, 'native_child_launched': False}))
        return
    units = B.path_units(cases[a.template]['units'], n['b'], n['c'])
    expected = base.leaf_sha(units)
    tag = n['id']
    n.update(state='RUNNING', units=units, expected_CNF_sha256=expected,
             clause_count=base.nc + len(units), start=datetime.now().astimezone().isoformat())
    n['outer_record'] = supervisor['record']
    n['outer_completed_cleanly'] = None
    if n['level'] == 1:
        n['planned_L2_children'] = [
            {'id': tag + '.L2.%03d' % c, 'level': 2, 'b': n['b'], 'c': c, 'ancestor': tag,
             'state': 'UNSTARTED', 'units': B.path_units(cases[a.template]['units'], n['b'], c),
             'expected_CNF_sha256': base.leaf_sha(B.path_units(cases[a.template]['units'], n['b'], c)),
             'receipt': None} for c in range(8)]
    save()
    child_meta = {'id': tag, 'template': a.template, 'ancestor': n['ancestor'], 'level': n['level'],
                  'units': units, 'expected_CNF_sha256': expected, 'header': B.header(units).decode(),
                  'WMAN_sha256': B.WMAN_SHA, 'design_sha256': DESIGN_SHA, 'source16_results_sha256': source_hash,
                  'executor_sha256': R_SHA, 'helper_sha256': sha((ROOT / 'code/n8_fone_refine_bytes.py').read_bytes()),
                  'controller_sha256': sha(Path(__file__).read_bytes()), 'base_sha256': SOURCE_SHA,
                  'solver_native_limit': 300, 'checker_native_limit': 900, 'wall_limit': 1200,
                  'worker_measured_feed_hashes': None, 'authority': 'legacy producer candidate; parent measured F4 only'}
    child_meta['runtime_binaries'] = runtime_binaries
    child_meta['parent_admission'] = admission
    child_meta['shared_prelaunch'] = before_native
    child_meta['outer_supervisor'] = supervisor
    new_json(out / (tag + '.input.json'), child_meta)
    fifos = tuple(str(out / ('w0.%s.fifo' % x)) for x in ('cnf_s', 'cnf_c', 'proof'))
    stop_request = Path(supervisor['record'] + '.stop.json')
    observer_done = threading.Event()

    def request_owner_stop(reason, snapshot=None):
        if not stop_request.exists():
            new_json(stop_request, {'id': tag, 'reason': reason, 'snapshot': snapshot,
                                    'method': 'file-only request to the pinned group owner; no PID signals'})

    def observe_shared_capacity():
        while not observer_done.wait(2):
            try:
                read_admission(a.admission, a.admission_sha256)
                snapshot = metrics.shared_snapshot(shared_markers)
                if snapshot['joint_RSS_bytes'] > 8 * 2 ** 30 or snapshot['joint_native_count'] > 4:
                    request_owner_stop('shared8GiB/4native limit exceeded', snapshot)
                    return
            except BaseException as ex:
                request_owner_stop('admission/capacity observation failed: ' + repr(ex))
                return

    threading.Thread(target=observe_shared_capacity, daemon=True).start()
    try:
        r = R.certify(tag, units, base.nv, base.nc, base.body, str(out), fifos, 300, a.rss_cap, checker_limit=900)
    except Exception as ex:
        L['status'] = 'STOP_IMPLEMENTATION_ERROR'
        n['state'] = 'UNKNOWN'
        n['error'] = repr(ex)
        L['active_seconds'] += time.monotonic() - step_start
        save()
        request_owner_stop('legacy execution raised: ' + repr(ex))
        raise
    finally:
        observer_done.set()
    if r['cnf_sha256'] != expected:
        L['status'] = 'STOP_BINDING_ERROR'
        n['state'] = 'UNKNOWN'
        n['observed_CNF_sha256'] = r['cnf_sha256']
        L['active_seconds'] += time.monotonic() - step_start
        save()
        raise RuntimeError('legacy executor input differs from planned child')
    candidate = C.strict_ok(r)
    sat = r['solver_returncode'] == 10 and 's SATISFIABLE' in r['solver_status_lines']
    stored_logs = {}
    for kind in ('solver', 'drat-trim'):
        path = out / (tag + '.' + kind + '.log')
        stored_logs[kind] = {'path': str(path.relative_to(ROOT)), 'sha256': sha(path.read_bytes()), 'bytes': path.stat().st_size}
    sat_model_valid = None
    if sat:
        sat_model_valid = model_check((out / (tag + '.solver.log')).read_text(), base.body, units, base.nv)
    rec = dict(child_meta)
    rec.update(r)
    rec.update(legacy_worker_strict=candidate, full_F4_worker_measurements_available=False,
               worker_measured_solver_feed_sha256=None, worker_measured_checker_feed_sha256=None,
               outer_qualification='PENDING_SUPERVISOR', stored_logs=stored_logs, SAT_model_checked=sat_model_valid,
               step_active_seconds=time.monotonic() - step_start)
    receipt_name = tag + '.receipt.json'
    receipt_sha = new_json(out / receipt_name, rec)
    with (out / 'RESULTS.jsonl').open('ab') as f:
        f.write(json.dumps(rec).encode() + b'\n')
    n['receipt'] = {'path': receipt_name, 'sha256': receipt_sha}
    if sat:
        n['state'] = 'SAT_PATTERN' if sat_model_valid else 'SAT_REPORT_INVALID_MODEL'
        L['status'] = 'STOP_SAT_PATTERN'
    elif candidate:
        n['state'] = 'LEGACY_CANDIDATE'
    elif n['level'] == 1:
        n['state'] = 'REFINED'
        for c in range(8):
            cid = tag + '.L2.%03d' % c
            child_units = B.path_units(cases[a.template]['units'], n['b'], c)
            L['nodes'][cid] = {'id': cid, 'level': 2, 'b': n['b'], 'c': c, 'ancestor': tag,
                               'state': 'UNSTARTED', 'units': child_units,
                               'expected_CNF_sha256': base.leaf_sha(child_units), 'receipt': None}
    else:
        n['state'] = 'UNKNOWN'
    L['active_seconds'] += time.monotonic() - step_start
    pending_left = any(x['state'] == 'UNSTARTED' for x in L['nodes'].values())
    if L['status'] == 'OPEN' and not pending_left:
        L['status'] = 'AWAITING_SUPERVISOR'
    save()
    summary = {'family': a.template, 'id': tag, 'child_CNF_sha256': expected,
               'solver_status': r['solver_status_lines'], 'checker_status': r['checker_status_lines'],
               'solver_returncode': r['solver_returncode'], 'checker_returncode': r['checker_returncode'],
               'seconds': r['secs'], 'peak_RSS': r['aggregate_peak_rss_bytes'], 'state': n['state'],
               'legacy_worker_strict': candidate, 'parent_F4_required': True,
               'receipt_path': str((out / receipt_name).relative_to(ROOT)), 'receipt_sha256': receipt_sha,
               'family_status': L['status'], 'family_active_seconds': L['active_seconds'],
               'family_counts': {s: sum(x['state'] == s for x in L['nodes'].values())
                                 for s in ('UNSTARTED', 'LEGACY_CANDIDATE', 'REFINED', 'UNKNOWN', 'SAT_PATTERN')},
               'ledger_version': L['version'], 'ledger_sha256': lh}
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
