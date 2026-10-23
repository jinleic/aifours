#!/usr/bin/env python3
"""Targeted tiny-child controls for final helper guard v3; NO repeat of the9 retained normal-path controls and NO
placement enumeration. New x-mode receipt directory per attempt. One existing lane token, original COUNT unchanged.
A: RSS sampler raises after spawn -> own child SIGTERM/bounded wait, UNKNOWN, token+bigmem+helper locks held during wait.
B: child completed before monitoring loop and final simulated free<12e9 -> UNKNOWN even rc0.
C: same fast child, final disk read raises -> UNKNOWN even rc0.
D: quarantine receipt writes fail (simulated), stubborn rc0 child remains capacity-quarantined until exit; no silent release.
"""
import fcntl
import json
import os
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import enumeration_helper_guard_v3 as H
import stream_check15 as S

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, 'cycle2')


def main():
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(C2, 'STOP-hard12'), os.path.join(C2, 'STOP-m2r12')])
    root = os.path.join(C2, 'enum-final-smoke-%d' % time.time_ns())
    os.makedirs(root, exist_ok=False)
    os.environ['TMPDIR'] = root
    result = {'start': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'tests': {},
              'normal_controls_reused': 'cycle2/enumeration-guard-smoke-1792311784358838000/receipt.json (9; unchanged normal paths)',
              'scope': 'targeted resource exception/final-floor/creation-failure controls only; no proof mutations or enumeration'}

    def run(name, cmd, limit=5):
        directory = os.path.join(root, name)
        os.makedirs(directory, exist_ok=False)
        return H.run_helper(S, cmd, directory, time.monotonic()+10, time.time()+10,
                            helper_seconds=limit, term_wait=0.2, sample_seconds=0.02)

    def locks_held(token):
        answer = {}
        for label, path in [('token', os.path.join(S.TOK,token.name)), ('bigmem', os.path.join(S.TOK,'bigmem')), ('helper',S.HELPER_LOCK)]:
            fd = os.open(path, os.O_RDWR)
            try:
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    answer[label] = False
                    fcntl.flock(fd, fcntl.LOCK_UN)
                except BlockingIOError:
                    answer[label] = True
            finally:
                os.close(fd)
        return answer

    try:
        with S.Token(stage='final-helper-targeted-smoke') as token:
            result['token'] = token.name
            original_spawn, original_rss = S.spawn, S._rss_kb
            wait_probes = []
            def observed_spawn(cmd, stdin=False):
                child = original_spawn(cmd, stdin)
                real_wait = child.wait
                def observed_wait(timeout=None):
                    wait_probes.append(locks_held(token))
                    return real_wait(timeout=timeout)
                child.wait = observed_wait
                return child
            def failing_rss(pid):
                raise RuntimeError('injected post-spawn RSS sampler error')
            try:
                S.spawn, S._rss_kb = observed_spawn, failing_rss
                with S.BigLock(True):
                    rc, _, info = run('A-sampler-error', [sys.executable,'-c','import time; time.sleep(5)'])
            finally:
                S.spawn, S._rss_kb = original_spawn, original_rss
            result['tests']['A_sampler_exception'] = {'rc':rc,'info':info,'wait_lock_probes':wait_probes,
                'expected':rc == -15 and info['guard_tripped'] and 'supervision exception' in info['guard_reasons']
                and wait_probes and all(all(p.values()) for p in wait_probes)}
            original_start, original_free = S._start, S.disk_free_bytes
            for name, read_error in [('B-final-floor',False),('C-final-read-error',True)]:
                completed = [False]
                def already_completed(cmd, stdin=False):
                    child, output, thread = original_start(cmd, stdin)
                    child.wait(timeout=2)
                    thread.join(timeout=2)
                    completed[0] = True
                    return child, output, thread
                def final_free(path=S.LANE):
                    if completed[0]:
                        if read_error:
                            raise OSError('injected final disk-read failure')
                        return 12000000000 - 1
                    return original_free(path)
                try:
                    S._start, S.disk_free_bytes = already_completed, final_free
                    rc, _, info = run(name, [sys.executable,'-c','pass'])
                finally:
                    S._start, S.disk_free_bytes = original_start, original_free
                reason = 'post-completion free-space read failed' if read_error else 'post-completion free-space floor'
                result['tests'][name] = {'rc':rc,'info':info,'monitor_loop_skipped':info['minimum_sampled_free_bytes'] is None,
                    'expected':rc == 0 and info['guard_tripped'] and reason in info['guard_reasons']
                    and info['minimum_sampled_free_bytes'] is None}
            marker = threading.Event()
            real_write = H.write_json_x
            probe = {}
            def failed_receipt(path,value):
                if 'helper-quarantine-' in os.path.basename(path):
                    marker.set()
                    raise OSError('injected quarantine receipt failure')
                return real_write(path,value)
            def inspect_locks():
                probe['quarantine_seen'] = marker.wait(5)
                if probe['quarantine_seen']:
                    probe['locks'] = locks_held(token)
            inspect = threading.Thread(target=inspect_locks)
            try:
                H.write_json_x = failed_receipt
                with S.BigLock(True):
                    inspect.start()
                    rc, _, info = run('D-receipt-failure', [sys.executable,'-c','import signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); time.sleep(1.2)'],limit=0.15)
                    inspect.join(timeout=5)
            finally:
                H.write_json_x = real_write
            errors = [e for e in info['events'] if 'quarantine_receipt_error' in e]
            result['tests']['D_quarantine_receipt_failure'] = {'rc':rc,'info':info,'lock_probe':probe,
                'expected':rc == 0 and info['guard_tripped'] and info['stop'] == 'quarantined' and len(errors) == 2
                and probe.get('quarantine_seen') and all(probe.get('locks',{}).values())}
        result['all_expected'] = all(bool(v['expected']) for v in result['tests'].values())
    except (S.AdmissionDenied,SystemExit) as exc:
        result['deferred'] = repr(exc)
        result['all_expected'] = False
    finally:
        result['end'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        result['no_owned_child_remaining'] = not any(p.poll() is None for p in S.ACTIVE)
        dest = os.path.join(root,'receipt.json')
        H.write_json_x(dest,result)
    print(dest)
    print(json.dumps({'all_expected':result.get('all_expected'),'tests':{k:bool(v['expected']) for k,v in result['tests'].items()},
                      'no_owned_child_remaining':result['no_owned_child_remaining']}))


if __name__ == '__main__':
    main()
