#!/usr/bin/env python3
"""NEW exclusive wrapper for the approved26 missing ms09 lists (parent growth-gate decision 2026-10-18 ~01:1x).
It reuses stream_check15.run_helper unchanged (owned registered child, helper flock, sampled5GiB cap/quarantine).
After ALL token+bigmem locks are held, a local spawn hook (also inside run_helper's helper lock) computes current
conservative lane-new-data usage and all remaining frozen generator-output bounds; refuses if the whole plan
would exceed the original10GiB cap (enforces stricter10e9B). It then requires fresh free bytes >=
max(12,334,217,728, 12,267,108,864 + this frozen output bound +1,048,576 receipt margin), rechecks immediately before
Popen, and records both the admission and result receipts. No proof predicate/cap change; no deletion or overwrite.
Exact complete num_placements/SHA are pinned after successful generation and before any batch solve. Any failed
gate/helper/cap/validation stops this chunk UNKNOWN; no further helper is started. Owned TMPDIR is lane-local.
Usage: extend_ms09_growth_guarded.py INVENTORY_JSON JOB [JOB ...]   (COUNT must be0)
"""
import fcntl
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_new_data_accounting as A
import stream_check15 as S

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, 'cycle2')
BASE_FREE = 12267108864
NORMAL_GATE = 12334217728
RECEIPT_MARGIN = 1048576
EXPECTED_INVENTORY_SHA = 'd45499bdcb4718a38fafa0f82f49c8d28d06ab680444b6e1ad2cad6c82ca414a'


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def ext_path(job):
    mi, bi = map(int, job.split(':'))
    return os.path.join(C2, 'm2part_drat', 'ms%02d_b%05d' % (mi, bi), 'ext.json')


def main():
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(C2, 'STOP-extend')])
    inventory_path = os.path.abspath(sys.argv[1])
    assert sha(inventory_path) == EXPECTED_INVENTORY_SHA, 'not the frozen approved inventory'
    inv = json.load(open(inventory_path))
    requested = sys.argv[2:]
    rows = {row['job']: row for row in inv['jobs']}
    assert len(rows) == 26 and len(requested) == len(set(requested)) and all(job in rows for job in requested)
    assert open(os.path.join(S.TOK, 'COUNT')).read().strip() == '0', 'COUNT must be0'
    for name, expected in inv['source_sha256'].items():
        assert sha(os.path.join(HERE, name)) == expected, ('source changed', name)
    skpath = os.path.join(C2, 'skel-b', 'skeletons-b-ms09.json')
    assert sha(skpath) == inv['skeleton_file_sha256']
    for record in inv['hard_lists_unchanged']:
        assert sha(os.path.join(LANE, record['path'])) == record['sha256']
    tmpdir = os.path.join(LANE, 'scratch', 'ms09-owned-tmp', '%d-%d' % (os.getpid(), time.time_ns()))
    os.makedirs(tmpdir, exist_ok=False)
    os.environ['TMPDIR'] = tmpdir
    fds = []
    for name in ['t%d' % n for n in range(8)] + ['bigmem']:
        fd = os.open(os.path.join(S.TOK, name), os.O_CREAT | os.O_RDWR)
        fcntl.flock(fd, fcntl.LOCK_EX)
        fds.append(fd)
    for fd in fds[:8]:
        os.ftruncate(fd, 0)
        os.pwrite(fd, ('%d %.3f ms09-growth-exclusive\n' % (os.getpid(), time.time())).encode(), 0)
    original_spawn = S.spawn
    state = {}
    summary = {'start': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'inventory_sha256': sha(inventory_path),
               'owned_tmpdir': os.path.relpath(tmpdir, LANE), 'requested': requested, 'results': []}

    def guarded_spawn(cmd, stdin=False):
        # Called by unchanged run_helper AFTER its helper lock/headroom check, with all token/bigmem locks held.
        accounting = A.account(LANE)
        remaining = [r for job, r in rows.items() if not os.path.exists(ext_path(job))]
        planned_bound = sum(r['complete_output_upper_bytes'] + RECEIPT_MARGIN for r in remaining)
        output_bound = state['row']['complete_output_upper_bytes']
        required = max(NORMAL_GATE, BASE_FREE + output_bound + RECEIPT_MARGIN)
        for name, expected in inv['source_sha256'].items():
            if sha(os.path.join(HERE, name)) != expected:
                raise S.AdmissionDenied('frozen source changed after lock wait: ' + name)
        if sha(skpath) != inv['skeleton_file_sha256']:
            raise S.AdmissionDenied('frozen skeleton input changed after lock wait')
        free_now = S.disk_free_bytes()
        admission = {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'job': state['job'],
                     'all_token_bigmem_helper_locks_held': True, 'frozen_output_bound_bytes': output_bound,
                     'receipt_margin_bytes': RECEIPT_MARGIN, 'required_free_bytes': required, 'fresh_free_bytes': free_now,
                     'lane_new_data_accounting': accounting, 'remaining_whole_generator_plan_bound_bytes': planned_bound,
                     'plan_plus_current_usage_bytes': accounting['new_data_usage_upper_bytes'] + planned_bound,
                     'projected_plan_within_enforced_cap': accounting['known'] and
                         accounting['new_data_usage_upper_bytes'] + planned_bound <= A.ENFORCED_CAP_BYTES,
                     'proof_retention_bytes': 0}
        state['admission'] = admission
        S.write_json(os.path.join(state['dir'], 'growth-admission-%d.json' % time.time_ns()), admission)
        if not admission['projected_plan_within_enforced_cap']:
            raise S.AdmissionDenied('whole planned retained output exceeds known lane-new-data allowance')
        if free_now < required:
            raise S.AdmissionDenied('post-all-lock growth gate: free %d < %d' % (free_now, required))
        # No lock wait or unrelated work between this fresh check and the registered Popen call.
        immediately_before = S.disk_free_bytes()
        state['immediate_free_bytes'] = immediately_before
        state['spawn_clock'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        if immediately_before < required:
            raise S.AdmissionDenied('immediate pre-spawn growth gate: free %d < %d' % (immediately_before, required))
        return original_spawn(cmd, stdin)

    S.spawn = guarded_spawn
    try:
        for job in requested:
            out = ext_path(job)
            directory = os.path.dirname(out)
            os.makedirs(directory, exist_ok=True)
            if os.path.exists(out):
                e = json.load(open(out))
                assert e['num_placements'] == len(e['placements'])
                summary['results'].append({'job': job, 'skipped': 'complete retained list exists', 'num_placements': e['num_placements'],
                                           'sha256': sha(out)})
                continue
            _, bi = map(int, job.split(':'))
            tmp = '%s.tmp-%d-%d' % (out, os.getpid(), time.time_ns())
            state.clear()
            state.update({'job': job, 'row': rows[job], 'dir': directory})
            t0 = time.time()
            try:
                rc, text = S.run_helper([sys.executable, os.path.join(HERE, 'extend_b.py'), skpath, str(bi), tmp])
            except S.AdmissionDenied as exc:
                deferred = {'job': job, 'status': 'UNKNOWN/deferred', 'reason': str(exc), 'state': state}
                S.write_json(os.path.join(directory, 'growth-deferred-%d.json' % time.time_ns()), deferred)
                summary['results'].append({'job': job, 'status': 'UNKNOWN/deferred', 'reason': str(exc)})
                print(json.dumps(summary['results'][-1]), flush=True)
                break
            info = dict(S.LAST_HELPER, seconds=round(time.time() - t0, 2), job=job,
                        immediate_free_bytes=state.get('immediate_free_bytes'), spawn_clock=state.get('spawn_clock'),
                        admission=state.get('admission'), out_tail=text[-300:], tmp=os.path.relpath(tmp, LANE))
            if rc != 0 or info.get('cap_hit') or not os.path.exists(tmp):
                info['status'] = 'UNKNOWN/helper failed'
                S.write_json(os.path.join(directory, 'growth-failed-%d.json' % time.time_ns()), info)
                summary['results'].append({'job': job, 'status': info['status'], 'rc': rc, 'cap_hit': info.get('cap_hit')})
                print(json.dumps(summary['results'][-1]), flush=True)
                break
            e = json.load(open(tmp))
            valid = (e['num_placements'] == len(e['placements']) and e['raw_class_assignments'] <= rows[job]['raw_assignment_dp_upper']
                     and os.path.getsize(tmp) <= rows[job]['complete_output_upper_bytes'])
            if not valid:
                info['status'] = 'UNKNOWN/output bound or completeness validation failed'
                S.write_json(os.path.join(directory, 'growth-failed-%d.json' % time.time_ns()), info)
                summary['results'].append({'job': job, 'status': info['status']})
                print(json.dumps(summary['results'][-1]), flush=True)
                break
            assert not os.path.exists(out), 'refuse to overwrite retained placement list'
            os.rename(tmp, out)
            pin = {'job': job, 'status': 'COMPLETE placement denominator pinned before any batch solve',
                   'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'path': os.path.relpath(out, LANE), 'sha256': sha(out),
                   'bytes': os.path.getsize(out), 'raw_class_assignments': e['raw_class_assignments'],
                   'automorphisms': e['automorphisms'], 'num_placements': e['num_placements'],
                   'inventory_sha256': summary['inventory_sha256'], 'helper': info}
            S.write_json(os.path.join(directory, 'complete-denominator-%d.json' % time.time_ns()), pin)
            result = {k: pin[k] for k in ('job', 'sha256', 'bytes', 'raw_class_assignments', 'automorphisms', 'num_placements')}
            result['seconds'], result['peak_rss_kb'] = info['seconds'], info.get('peak_rss_kb')
            summary['results'].append(result)
            print(json.dumps(result), flush=True)
            if S.ABORT[0]:
                break
        for record in inv['hard_lists_unchanged']:
            assert sha(os.path.join(LANE, record['path'])) == record['sha256'], 'existing hard list changed'
        summary['hard_lists_unchanged'] = True
    finally:
        S.spawn = original_spawn
        with S._alock:
            live = [p for p in S.ACTIVE if p.poll() is None]
        for child in live:
            S.quarantine(child, 'exclusive wrapper owned survivor before unlock', [])
            S.unregister(child)
        for fd in fds:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
        summary['end'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        S.write_json(os.path.join(C2, 'ms09-growth-chunk-%d.json' % time.time_ns()), summary)


if __name__ == '__main__':
    main()
