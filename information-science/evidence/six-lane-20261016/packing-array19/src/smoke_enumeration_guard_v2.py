#!/usr/bin/env python3
"""[V2 repeats the9 required guard/I-O controls on cleanup-hardened helper, plus injected RSS-observation exception cleanup and quarantine-receipt I/O failure with capacity retained. No full enumeration rerun.]
Tiny owned-child resource/I-O controls for the new ms09 helper guard (no placement enumeration rerun).
One existing lane token covers this sequential smoke; COUNT/config/source/evidence files are never changed.
Controls: elapsed limit; simulated in-flight12e9 floor; chunk deadline; run deadline; stubborn child ignoring
SIGTERM (rc0 later, still UNKNOWN) with token+bigmem+helper flocks retained through quarantine; tiny RSS cap;
expired admission with0 children; x-mode receipt collision preserves original; AST comparison proves extend_b_x
changes only output open mode (module docstrings ignored). Every attempt has new creation-only receipt paths.
"""
import ast
import fcntl
import hashlib
import json
import os
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import enumeration_helper_guard_v2 as H
import stream_check15 as S

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, 'cycle2')


def main():
    S.install_sigterm_handler()
    S.set_stop_files([os.path.join(C2, 'STOP-hard12'), os.path.join(C2, 'STOP-m2r12')])
    root = os.path.join(C2, 'enumeration-guard-v2-smoke-%d' % time.time_ns())
    os.makedirs(root, exist_ok=False)
    os.environ['TMPDIR'] = root
    result = {'start': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'scope': 'tiny owned child resource/I-O tests only; no scientific enumeration/proof mutation', 'tests': {}}
    sleep_cmd = [sys.executable, '-c', 'import time; time.sleep(5)']

    def run(name, cmd=sleep_cmd, seconds=5.0, chunk=None, wall=None, rss=5*1024*1024):
        d = os.path.join(root, name)
        os.makedirs(d, exist_ok=False)
        return H.run_helper(S, cmd, d, time.monotonic()+10 if chunk is None else chunk,
                            time.time()+10 if wall is None else wall, helper_seconds=seconds,
                            term_wait=0.2, sample_seconds=0.02, rss_cap_kb=rss)

    try:
        with S.Token(stage='enumeration-guard-smoke') as token:
            result['token'] = token.name
            rc, _, info = run('elapsed', seconds=0.15)
            result['tests']['elapsed'] = {'rc': rc, 'info': info, 'expected': rc == -15 and info['guard_tripped'] and 'helper elapsed limit' in info['guard_reasons']}
            original_free, original_spawn = S.disk_free_bytes, S.spawn
            spawned = [None]

            def observed_spawn(cmd, stdin=False):
                p = original_spawn(cmd, stdin)
                spawned[0] = time.monotonic()
                return p

            def simulated_free(path=S.LANE):
                if spawned[0] is not None and time.monotonic() - spawned[0] >= 0.15:
                    return 12000000000 - 1
                return original_free(path)

            try:
                S.spawn, S.disk_free_bytes = observed_spawn, simulated_free
                rc, _, info = run('floor')
            finally:
                S.spawn, S.disk_free_bytes = original_spawn, original_free
            result['tests']['floor'] = {'rc': rc, 'info': info, 'expected': rc == -15 and info['guard_tripped'] and 'in-flight free-space floor' in info['guard_reasons']}
            rc, _, info = run('chunk', chunk=time.monotonic()+0.15)
            result['tests']['chunk_deadline'] = {'rc': rc, 'info': info, 'expected': rc == -15 and info['guard_tripped'] and 'chunk deadline' in info['guard_reasons']}
            rc, _, info = run('run', wall=time.time()+0.15)
            result['tests']['run_deadline'] = {'rc': rc, 'info': info, 'expected': rc == -15 and info['guard_tripped'] and 'run deadline' in info['guard_reasons']}
            marker = threading.Event()
            old_write = H.write_json_x

            def observed_write(path, value):
                old_write(path, value)
                if 'helper-quarantine-begin-' in os.path.basename(path):
                    marker.set()

            lock_probe = {}
            def probe():
                if not marker.wait(5):
                    lock_probe['quarantine_seen'] = False
                    return
                lock_probe['quarantine_seen'] = True
                for name, path in [('token', os.path.join(S.TOK, token.name)), ('bigmem', os.path.join(S.TOK, 'bigmem')), ('helper', S.HELPER_LOCK)]:
                    fd = os.open(path, os.O_RDWR)
                    try:
                        try:
                            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                            lock_probe[name + '_held'] = False
                            fcntl.flock(fd, fcntl.LOCK_UN)
                        except BlockingIOError:
                            lock_probe[name + '_held'] = True
                    finally:
                        os.close(fd)
            stubborn = [sys.executable, '-c', 'import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(1.2)']
            pt = threading.Thread(target=probe)
            try:
                H.write_json_x = observed_write
                with S.BigLock(True):
                    pt.start()
                    rc, _, info = run('stubborn', cmd=stubborn, seconds=0.15)
                    pt.join(timeout=5)
            finally:
                H.write_json_x = old_write
            result['tests']['stubborn_quarantine'] = {'rc': rc, 'info': info, 'lock_probe': lock_probe,
                    'expected': rc == 0 and info['guard_tripped'] and info['stop'] == 'quarantined'
                    and lock_probe.get('quarantine_seen') and all(lock_probe.get(k+'_held') for k in ('token','bigmem','helper'))}
            tiny_rss = [sys.executable, '-c', 'import time; b=bytearray(64*1024*1024); b[::4096]=b"x"*len(b[::4096]); time.sleep(5)']
            rc, _, info = run('rss', cmd=tiny_rss, rss=32*1024)
            result['tests']['rss'] = {'rc': rc, 'info': info, 'expected': rc == -15 and info['guard_tripped'] and 'helper RSS cap' in info['guard_reasons']}
            spawn_count = [0]
            real_spawn = S.spawn
            def counted_spawn(cmd, stdin=False):
                spawn_count[0] += 1
                return real_spawn(cmd, stdin)
            denied = False
            try:
                S.spawn = counted_spawn
                try:
                    run('expired', chunk=time.monotonic()-1)
                except S.AdmissionDenied:
                    denied = True
            finally:
                S.spawn = real_spawn
            result['tests']['expired_admission'] = {'denied': denied, 'children_started': spawn_count[0], 'expected': denied and spawn_count[0] == 0}
            path = os.path.join(root, 'creation-collision.json')
            H.write_json_x(path, {'kept': 1})
            original_hash = hashlib.sha256(open(path, 'rb').read()).hexdigest()
            refused = False
            try:
                H.write_json_x(path, {'overwritten': 1})
            except FileExistsError:
                refused = True
            result['tests']['creation_only_receipt'] = {'refused': refused, 'original_hash_preserved': hashlib.sha256(open(path, 'rb').read()).hexdigest() == original_hash,
                    'expected': refused and hashlib.sha256(open(path, 'rb').read()).hexdigest() == original_hash}
            old_ast = ast.parse(open(os.path.join(HERE, 'extend_b.py')).read())
            new_ast = ast.parse(open(os.path.join(HERE, 'extend_b_x.py')).read())
            for tree in (old_ast, new_ast):
                if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant) and isinstance(tree.body[0].value.value, str):
                    tree.body.pop(0)
            modes = 0
            for node in ast.walk(new_ast):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'open' and len(node.args) > 1 and isinstance(node.args[1], ast.Constant) and node.args[1].value == 'x':
                    node.args[1].value = 'w'
                    modes += 1
            same = ast.dump(old_ast, include_attributes=False) == ast.dump(new_ast, include_attributes=False)
            result['tests']['output_io_only_generator'] = {'changed_open_modes': modes, 'algorithm_ast_equal_after_mode_normalization': same, 'expected': modes == 1 and same}
            # Unexpected observation errors must terminate our live child before capacity is released.
            saved_rss, saved_spawn = S._rss_kb, S.spawn
            owned = []
            def remember_spawn(cmd, stdin=False):
                child = saved_spawn(cmd, stdin)
                owned.append(child)
                return child
            def broken_rss(pid):
                raise RuntimeError('injected RSS observation failure')
            saw = False
            started_error = time.monotonic()
            try:
                S.spawn, S._rss_kb = remember_spawn, broken_rss
                try:
                    run('exception-cleanup')
                except RuntimeError as exc:
                    saw = 'injected RSS' in str(exc)
            finally:
                S.spawn, S._rss_kb = saved_spawn, saved_rss
            result['tests']['exception_cleanup'] = {'saw_expected_error': saw,
                'owned_child_rc': owned[0].returncode if owned else None,
                'seconds': round(time.monotonic()-started_error, 3),
                'expected': saw and len(owned) == 1 and owned[0].returncode == -15 and time.monotonic()-started_error < 2}
            # Receipt-write failure cannot release quarantine around a surviving owned child.
            failed_marker = threading.Event()
            held_failed = {}
            real_write2 = H.write_json_x
            def failing_quarantine_write(path, value):
                if 'helper-quarantine-' in os.path.basename(path):
                    failed_marker.set()
                    raise OSError('injected quarantine receipt write failure')
                return real_write2(path, value)
            def probe_failed_receipt():
                held_failed['quarantine_seen'] = failed_marker.wait(5)
                if not held_failed['quarantine_seen']:
                    return
                for label, lockpath in [('token', os.path.join(S.TOK, token.name)), ('bigmem', os.path.join(S.TOK,'bigmem')), ('helper', S.HELPER_LOCK)]:
                    probe_fd = os.open(lockpath, os.O_RDWR)
                    try:
                        try:
                            fcntl.flock(probe_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                            held_failed[label+'_held'] = False
                            fcntl.flock(probe_fd, fcntl.LOCK_UN)
                        except BlockingIOError:
                            held_failed[label+'_held'] = True
                    finally:
                        os.close(probe_fd)
            fp_thread = threading.Thread(target=probe_failed_receipt)
            try:
                H.write_json_x = failing_quarantine_write
                with S.BigLock(True):
                    fp_thread.start()
                    rc, _, info = run('quarantine-receipt-failure', cmd=stubborn, seconds=0.15)
                    fp_thread.join(timeout=5)
            finally:
                H.write_json_x = real_write2
            reported_errors = [event for event in info['events'] if 'quarantine_receipt_error' in event]
            result['tests']['quarantine_receipt_failure'] = {'rc': rc, 'info': info, 'lock_probe': held_failed,
                'expected': rc == 0 and info['guard_tripped'] and info['stop'] == 'quarantined' and len(reported_errors) == 2
                and held_failed.get('quarantine_seen') and all(held_failed.get(k+'_held') for k in ('token','bigmem','helper'))}
        result['all_expected'] = all(r['expected'] for r in result['tests'].values())
    except (S.AdmissionDenied, SystemExit) as exc:
        result['deferred'] = repr(exc)
        result['all_expected'] = False
    finally:
        result['end'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        result['no_owned_child_remaining'] = not any(p.poll() is None for p in S.ACTIVE)
        dest = os.path.join(root, 'receipt.json')
        H.write_json_x(dest, result)
    print(dest)
    print(json.dumps({'all_expected': result.get('all_expected'), 'tests': {k:v['expected'] for k,v in result['tests'].items()}, 'no_owned_child_remaining': result['no_owned_child_remaining']}))


if __name__ == '__main__':
    main()
