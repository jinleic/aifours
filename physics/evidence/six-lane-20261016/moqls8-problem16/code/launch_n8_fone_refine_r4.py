"""Task-specific outer adapter. Only the pinned, read-only phys2 supervisor
owns/stops the process group. This process holds the capacity flock THROUGH
supervisor cleanup/quarantine and producer post-qualification. No raw PID
signals, no SIGKILL, no edits/copies of the supervisor or legacy R.certify.
Heavy F.build/du/nonprivileged metrics and ALL native work occur in the supervised worker.
The worker requests a stop by an immutable tiny file. The probe adapter only
checks that file (no ps/Popen/unbounded work in the owner), raises ONCE into
the supervisor's tested exception path, then delegates cleanup probes unchanged.
Unexpected shared-state stops are quarantined, never counted as clean proofs.
"""
from __future__ import annotations

import argparse
import copy
import fcntl
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / 'evidence/n8_one_p4_template_runs_v1'
SUPERVISOR = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py')
SUP_SHA = '0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d'
HELD_PILOT = '7ff6aa677a9ac2acb63a382d37d1fd0281484cd96519f97e9d0f51ed301ae206'
QUARANTINE = ROOT / 'evidence/N8_FONE_REFINE_R3_QUARANTINE.json'
LOCK = RUNS / 'REFINEMENT_R3_CAPACITY.lock'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load_file(name, path, expected=None):
    if expected is not None and sha(path.read_bytes()) != expected:
        raise RuntimeError('pinned source changed: ' + str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def caps_for(admission):
    grant = admission['grant']
    if admission['sha256'] == HELD_PILOT:
        # Parent's explicit native-idle/held reservation declares N8 desk paused
        # for this ONE pilot. A later released/new lease cannot use this pin.
        other = {'N8FoneParentReplay': 0}
    else:
        other = grant.get('other_declared_phys1_caps_bytes')
        if not isinstance(other, dict) or not other:
            raise RuntimeError('future lease must declare every other phys1 cap')
    if any(type(v) is not int or v < 0 for v in other.values()):
        raise RuntimeError('invalid declared other-lane cap')
    own = min(6 * 2 ** 30, 8 * 2 ** 30 - sum(other.values()))
    if own <= 0:
        raise RuntimeError('no declared shared RSS capacity')
    return own, other


def qualify_node(L, node_id, outer_clean):
    """Only metadata; no native work. Preserve the raw legacy receipt unchanged."""
    n = L['nodes'][node_id]
    n['outer_completed_cleanly'] = bool(outer_clean)
    if outer_clean:
        return
    if n['state'] in ('SAT_PATTERN', 'SAT_REPORT_INVALID_MODEL'):
        return
    if n['level'] == 1:
        plans = n.get('planned_L2_children')
        if not plans or len(plans) != 8:
            raise RuntimeError('uncertain L1 has no complete pinned L2 plan')
        n['state'] = 'REFINED'
        for child in plans:
            cid = child['id']
            if cid not in L['nodes']:
                L['nodes'][cid] = copy.deepcopy(child)
    else:
        n['state'] = 'UNKNOWN'


def finish_status(L, T, outer_clean):
    if L['status'] == 'STOP_SAT_PATTERN':
        return
    if not outer_clean:
        L['status'] = 'STOP_OUTER_UNKNOWN'
        return
    if L['status'].startswith(('DEFERRED', 'STOP_')):
        return
    if any(n['state'] == 'UNSTARTED' for n in L['nodes'].values()):
        L['status'] = 'OPEN'
    else:
        L['status'] = 'CANDIDATE_CLOSED' if T.closure(L) else 'STOP_OPEN_UNKNOWN'


def make_stop_probe(supervisor, stop_request, observations):
    def probe(pid):
        result = supervisor.probe(pid)
        if not observations['stop_requested'] and stop_request.exists():
            observations['stop_requested'] = True
            raise RuntimeError('worker requested reserved-group stop: ' + str(stop_request))
        return result
    return probe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--template', required=True)
    ap.add_argument('--admission', required=True)
    ap.add_argument('--admission-sha256', required=True)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--init-family', action='store_true')
    mode.add_argument('--reuse-family', action='store_true')
    ap.add_argument('--init-root', action='store_true')
    ap.add_argument('--release', action='store_true')
    ap.add_argument('--continue-from')
    ap.add_argument('--continue-sha256')
    a = ap.parse_args()
    t0 = time.monotonic()
    # Tiny entry preflight only; no F.build, du, selectors or native child here.
    if sha(SUPERVISOR.read_bytes()) != SUP_SHA:
        raise RuntimeError('approved supervisor source pin changed')
    T = load_file('n8_refinement_worker', ROOT / 'code/run_n8_fone_refine.py')
    admission = T.read_admission(a.admission, a.admission_sha256)
    if a.template not in admission['grant']['family_scope']:
        raise RuntimeError('family outside this resource reservation')
    own_cap, other_caps = caps_for(admission)
    free = shutil.disk_usage(ROOT).free
    reserve = T.FAMILY_BYTES if a.init_family else T.CHILD_BYTES
    if free - reserve < T.FLOOR:
        raise SystemExit('DEFERRED: fresh12.2e9+projected growth gate; report once, no polling')
    # Persistent file, never removed. This owner remains alive while supervise()
    # retains the controller leader and cleans/quarantines the reserved group.
    lock = LOCK.open('a+b')
    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    lock.seek(0)
    if lock.read() or QUARANTINE.exists():
        raise SystemExit('QUARANTINED: no native admission; parent disposition required')
    out = T.REFINES / a.template
    before, _ = T.latest(out)
    active_before = before['active_seconds'] if before else 0.0
    if a.continue_from:
        raw_anchor = Path(a.continue_from).read_bytes()
        if before is not None or not a.init_family or sha(raw_anchor) != a.continue_sha256:
            raise RuntimeError('invalid explicit source-epoch continuation')
        active_before = json.loads(raw_anchor)['active_seconds']
    remaining = min(T.CAP - active_before, T.DEADLINE - time.time())
    if remaining < 1232:
        raise SystemExit('STOP_BUDGET: no fresh full child allowance; no cap reset')
    serial = str(time.time_ns())
    record = ROOT / 'evidence' / ('N8_FONE_R4.' + a.template + '.' + serial + '.json')
    command = [sys.executable, '-B', str(ROOT / 'code/run_n8_fone_refine.py'),
               '--template', a.template, '--admission', str(Path(a.admission).resolve()),
               '--admission-sha256', a.admission_sha256, '--rss-cap', str(own_cap),
               '--init-family' if a.init_family else '--reuse-family']
    if a.init_root:
        command.append('--init-root')
    if a.release:
        command.append('--release')
    if a.continue_from:
        command.extend(['--continue-from', str(Path(a.continue_from).resolve()),
                        '--continue-sha256', a.continue_sha256])
    S = load_file('n8_approved_supervisor', SUPERVISOR, SUP_SHA)
    stop_request = Path(str(record) + '.stop.json')
    observations = {'stop_requested': False, 'request_file': str(stop_request)}
    guarded_probe = make_stop_probe(S, stop_request, observations)


    rec = S.supervise(command, 'N8-' + a.template + '-' + serial,
                      min(1200.0, remaining - 32), own_cap, 12000000000,
                      str(ROOT), str(record), str(QUARANTINE), grace=30.0, probe_fn=guarded_probe)
    # No raw PID/PGID work here. The approved owner has finished its group stop
    # and persisted quarantine on uncertainty BEFORE this post-qualification.
    try:
        if rec['uncertain'] and not QUARANTINE.exists():
            T.new_json(QUARANTINE, {'status': 'SUPERVISOR_UNCERTAIN', 'outer_record': str(record),
                                    'rule': 'no further native admission; parent disposition required'})
        L, lh = T.latest(out)
        qualified = None
        if L is not None:
            matching = [n for n in L['nodes'].values() if n.get('outer_record') == str(record)]
            if len(matching) > 1:
                raise RuntimeError('ambiguous current supervised node')
            if matching:
                n = matching[0]
                qualify_node(L, n['id'], rec['completed_cleanly'])
                n['outer_qualification_record'] = {'path': str(record.relative_to(ROOT)),
                                                   'sha256': sha(record.read_bytes())}
                qualified = {'id': n['id'], 'expected_CNF_sha256': n['expected_CNF_sha256'],
                             'state': n['state'], 'outer_completed_cleanly': rec['completed_cleanly'],
                             'outer_seconds': rec['seconds'], 'outer_peak_sampled_RSS_bytes': rec['peak_sampled_rss_bytes'],
                             'native_receipt': n.get('receipt'), 'parent_F4_required': True}
            L['active_seconds'] = active_before + (time.monotonic() - t0)
            finish_status(L, T, rec['completed_cleanly'])
            L['prev_sha256'] = lh
            L['version'] += 1
            L['writer_sha256'] = sha(Path(__file__).read_bytes())
            L['last_supervisor'] = {'path': str(record.relative_to(ROOT)), 'sha256': sha(record.read_bytes()),
                                    'completed_cleanly': rec['completed_cleanly'], 'own_cap': own_cap,
                                    'other_declared_caps': other_caps, 'shared_observations': observations}
            lh = T.new_json(out / ('LEDGER.v%03d.json' % L['version']), L)
        summary = {'template': a.template, 'supervisor_record': str(record.relative_to(ROOT)),
                   'supervisor_record_sha256': sha(record.read_bytes()), 'completed_cleanly': rec['completed_cleanly'],
                   'trip_reason': rec['trip_reason'], 'uncertain': rec['uncertain'], 'qualified_child': qualified,
                   'family_status': L['status'] if L else 'NO_FAMILY_LEDGER_PREPARATION_ONLY',
                   'family_active_seconds': L['active_seconds'] if L else None,
                   'ledger_sha256': lh, 'admission_sha256': a.admission_sha256,
                   'own_cap': own_cap, 'other_declared_caps': other_caps, 'quarantine': rec['quarantine_record'],
                   'shared_observations': observations, 'no_parent_refutation_count_claim': True}
        T.new_json(ROOT / 'evidence' / ('N8_FONE_R4.' + a.template + '.' + serial + '.qualified.json'), summary)
        print(json.dumps(summary), flush=True)
    except BaseException as ex:
        # Group is already quiescent OR the supervisor's quarantine persists.
        # Fail closed on any metadata ambiguity; never silently rerun a node.
        info = {'status': 'POSTQUALIFICATION_UNCERTAIN', 'error': repr(ex), 'outer_record': str(record),
                'recorded_at': datetime.now().astimezone().isoformat(), 'rule': 'no later native admission'}
        try:
            if not QUARANTINE.exists():
                T.new_json(QUARANTINE, info)
        finally:
            lock.write(json.dumps(info).encode() + b'\n')
            lock.flush()
            os.fsync(lock.fileno())
        raise
    raise SystemExit(0 if rec['completed_cleanly'] else 3)


if __name__ == '__main__':
    main()
