"""GB timing probe r2 (WORKER probe; not parent-qualified evidence).

r2 differs from r1 (b4c6ca46...b483) ONLY by: output dir gb_probe_v2, freeze GB_PROBE_FREEZE.r2,
drat-trim stdout relayed through a filter thread (full raw stream sha256/bytes recorded; per-line
"duplicate literal" normalisation warnings counted, not stored), and fatal-warning classification
(any other WARNING, early EOF or "less than expected" fails).

Sequential items: tiny transport controls, then GB P1-B4, then GB P0-B3.
GB formula bytes are produced IN MEMORY by the frozen adapter gb_one_p4_r2.py
(5ca7c0da...e262) functions and must equal the 22-MATCH hashes recorded in
evidence/GB_ONE_P4_OWN_HASHES.r2.json (9781c877...943f) before any feed.
Transport: CNF bytes -> anonymous pipes (/dev/fd/N) to kissat and to the parent
drat-trim, each writer hashing exactly the bytes it writes; kissat binary DRAT ->
owned named FIFO -> relay thread (sha256 + byte count) -> drat-trim stdin (-i).
No CNF or proof bytes on disk. Supervision: libproc resident-size sampling of
self+children (fail closed on unknown), aggregate cap, in-flight free floor,
deadline; SIGTERM only, bounded wait, never SIGKILL.
"""
from __future__ import annotations

import ctypes
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT/'code/gb_one_p4_r2.py'
GEN_SHA = '5ca7c0da82c5ddd308acbbc2424da1ac6b4a0db08d0571f656eda5e841ffe262'
OWN = ROOT/'evidence/GB_ONE_P4_OWN_HASHES.r2.json'
OWN_SHA = '9781c877728b6a6f53511ecdd618eb4fc4ed3e87369398e82892cb4da0d9943f'
WMAN = ROOT/'evidence/n8_one_p4_templates_v1/MANIFEST.json'
WMAN_SHA = '355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74'
KISSAT = '/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat'
KISSAT_SHA = '05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848'
DRAT = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/drat-trim'
DRAT_SHA = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
BODY_SHA = 'f5da05206f44ff72e5aeade076820e2de52c9d2352f58b048ded1df76bdbf1b9'
OUTDIR = ROOT/'evidence/gb_probe_v2'
TZ = ZoneInfo('America/Los_Angeles')
DEADLINE = datetime.fromisoformat('2026-10-18T08:56:00-07:00').timestamp()
AGG_CAP = 7516192768          # 7.0 GiB: self + kissat + drat-trim resident
FLOOR = 12000000000           # in-flight free bytes
FRESH = 12200000000           # fresh free bytes before each item (+ margin)
MARGIN = 50000000
LANE_CAP = 10200547328
GB_ITEMS = (('P1-B4', 600, 1200), ('P0-B3', 2700, 3600))   # id, kissat --time, drat-trim -t
TINY_UNSAT = b'p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n'
TINY_SAT = b'p cnf 2 3\n1 2 0\n-1 2 0\n1 -2 0\n'


def now():
    return datetime.now(TZ).isoformat()


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def xjson(path, obj):
    raw = json.dumps(obj, indent=1).encode()
    with open(path, 'xb') as f:
        f.write(raw)
    return sha_bytes(raw)


class RusageV2(ctypes.Structure):
    _fields_ = [('ri_uuid', ctypes.c_uint8 * 16)] + [(n, ctypes.c_uint64) for n in (
        'ri_user_time', 'ri_system_time', 'ri_pkg_idle_wkups', 'ri_interrupt_wkups', 'ri_pageins',
        'ri_wired_size', 'ri_resident_size', 'ri_phys_footprint', 'ri_proc_start_abstime',
        'ri_proc_exit_abstime', 'ri_child_user_time', 'ri_child_system_time', 'ri_child_pkg_idle_wkups',
        'ri_child_interrupt_wkups', 'ri_child_pageins', 'ri_child_elapsed_abstime',
        'ri_diskio_bytesread', 'ri_diskio_byteswritten')]


LIBPROC = ctypes.CDLL('/usr/lib/libproc.dylib', use_errno=True)


def resident(pid):
    info = RusageV2()
    if LIBPROC.proc_pid_rusage(int(pid), 2, ctypes.byref(info)) != 0:
        return None, ctypes.get_errno()
    return max(info.ri_resident_size, info.ri_phys_footprint), 0


def lane_allocated(root):
    pending, seen, total = [Path(root)], set(), 0
    while pending:
        p = pending.pop(); s = p.lstat(); key = (s.st_dev, s.st_ino)
        if key in seen:
            continue
        seen.add(key); total += s.st_blocks * 512
        if p.is_dir() and not p.is_symlink():
            with os.scandir(p) as es:
                pending.extend(Path(e.path) for e in es)
    return total


def writer(fd, parts, res):
    h, total = hashlib.sha256(), 0
    try:
        for part in parts:
            mv = memoryview(part)
            for i in range(0, len(mv), 1 << 20):
                chunk = mv[i:i + (1 << 20)]
                n = 0
                while n < len(chunk):
                    n += os.write(fd, chunk[n:])
                h.update(chunk); total += len(chunk)
        res.update(ok=True, written=total, sha256=h.hexdigest(), error=None)
    except OSError as e:
        res.update(ok=False, written=total, sha256=h.hexdigest(), error=repr(e))
    finally:
        os.close(fd)


def relay(rfd, wfd, res):
    h, read, wrote, err = hashlib.sha256(), 0, 0, None
    try:
        while True:
            b = os.read(rfd, 1 << 20)
            if not b:
                break
            h.update(b); read += len(b)
            if err is None:
                try:
                    n = 0
                    while n < len(b):
                        n += os.write(wfd, b[n:])
                    wrote += len(b)
                except OSError as e:
                    err = repr(e)     # keep draining so the solver never blocks
    except OSError as e:
        err = err or repr(e)
    finally:
        os.close(rfd); os.close(wfd)
    res.update(proof_bytes_read=read, proof_bytes_relayed=wrote, proof_sha256=h.hexdigest(), error=err)


def log_filter(rfd, path, res):
    """Relay drat-trim stdout to a filtered log; hash/count the FULL raw stream."""
    h, raw_bytes, dup, kept, buf = hashlib.sha256(), 0, 0, 0, b''
    with open(path, 'xb') as out:
        try:
            while True:
                b = os.read(rfd, 1 << 20)
                if not b:
                    break
                h.update(b); raw_bytes += len(b); buf += b
                lines = buf.split(b'\n'); buf = lines.pop()
                for line in lines:
                    if b'WARNING: detected and deleted duplicate literal' in line:
                        dup += 1
                    else:
                        out.write(line + b'\n'); kept += 1
            if buf:
                if b'WARNING: detected and deleted duplicate literal' in buf:
                    dup += 1
                else:
                    out.write(buf); kept += 1
            res.update(ok=True, error=None)
        except OSError as e:
            res.update(ok=False, error=repr(e))
        finally:
            os.close(rfd)
    res.update(raw_stdout_sha256=h.hexdigest(), raw_stdout_bytes=raw_bytes, duplicate_literal_warning_lines=dup,
               kept_lines=kept)


def status_lines(path):
    raw = Path(path).read_bytes().replace(b'\r', b'')
    lines = raw.decode('utf-8', 'replace').split('\n')
    return [l for l in lines if l.startswith('s ')], lines


def pipeline(label, parts, expected_bytes, expected_sha, ksec, dsec, stopflag):
    fifo = OUTDIR/'fifo'/(label + '.drat.fifo')
    slog = OUTDIR/'logs'/(label + '.kissat.log'); clog = OUTDIR/'logs'/(label + '.drat.log')
    os.mkfifo(fifo)
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    fcntl.fcntl(rfd, fcntl.F_SETFL, fcntl.fcntl(rfd, fcntl.F_GETFL) & ~os.O_NONBLOCK)
    keep = os.open(fifo, os.O_WRONLY)
    sr, sw = os.pipe(); cr, cw = os.pipe(); pr, pw = os.pipe()
    rec = {'label': label, 'started_at': now(), 'kissat_argv': [KISSAT, '--time=%d' % ksec, '/dev/fd/<cnf>', str(fifo)],
           'drat_argv': [DRAT, '/dev/fd/<cnf>', '-i', '-t', str(dsec)], 'expected_feed_bytes': expected_bytes,
           'expected_feed_sha256': expected_sha, 'events': []}
    sl = open(slog, 'xb'); lr, lw = os.pipe(); lres = {}
    t0 = time.monotonic()
    dp = subprocess.Popen([DRAT, '/dev/fd/%d' % cr, '-i', '-t', str(dsec)], stdin=pr, stdout=lw,
                          stderr=subprocess.STDOUT, pass_fds=(cr,), cwd=str(OUTDIR/'tmp'))
    os.close(lw)
    lt = threading.Thread(target=log_filter, args=(lr, clog, lres)); lt.start()
    kp = subprocess.Popen([KISSAT, '--time=%d' % ksec, '/dev/fd/%d' % sr, str(fifo)], stdin=subprocess.DEVNULL,
                          stdout=sl, stderr=subprocess.STDOUT, pass_fds=(sr,), cwd=str(OUTDIR/'tmp'))
    for fd in (sr, cr, pr):
        os.close(fd)
    sres, cres, rres = {}, {}, {}
    ts = [threading.Thread(target=writer, args=(sw, parts, sres)), threading.Thread(target=writer, args=(cw, parts, cres)),
          threading.Thread(target=relay, args=(rfd, pw, rres))]
    for t in ts:
        t.start()
    live = {'kissat': kp.pid, 'drat': dp.pid}; done = {}; peak = {'kissat': 0, 'drat': 0, 'aggregate': 0}
    keep_open = True; stop_reason = None; last_free = 0.0; termed = None
    while live:
        for name, pid in list(live.items()):
            got, st, ru = os.wait4(pid, os.WNOHANG)
            if got == pid:
                rc = os.waitstatus_to_exitcode(st)
                done[name] = {'rc': rc, 'wall_s': round(time.monotonic() - t0, 3), 'ru_maxrss_bytes': ru.ru_maxrss,
                              'user_s': ru.ru_utime, 'sys_s': ru.ru_stime}
                del live[name]
                if name == 'kissat' and keep_open:
                    os.close(keep); keep_open = False
        agg = resident(os.getpid())[0] or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        unknown = []
        for name, pid in live.items():
            r, err = resident(pid)
            if r is None:
                got, st, ru = os.wait4(pid, os.WNOHANG)
                if got == pid:
                    rc = os.waitstatus_to_exitcode(st)
                    done[name] = {'rc': rc, 'wall_s': round(time.monotonic() - t0, 3), 'ru_maxrss_bytes': ru.ru_maxrss,
                                  'user_s': ru.ru_utime, 'sys_s': ru.ru_stime}
                    continue
                unknown.append((name, err))
            else:
                peak[name] = max(peak[name], r); agg += r
        for name in done:
            live.pop(name, None)
        if not keep_open and 'kissat' not in live:
            pass
        elif 'kissat' in done and keep_open:
            os.close(keep); keep_open = False
        peak['aggregate'] = max(peak['aggregate'], agg)
        tn = time.monotonic()
        if stop_reason is None:
            if unknown:
                stop_reason = 'unknown resident reading %r' % unknown
            elif agg > AGG_CAP:
                stop_reason = 'aggregate resident %d > cap %d' % (agg, AGG_CAP)
            elif time.time() >= DEADLINE:
                stop_reason = 'probe deadline 08:56 PDT'
            elif stopflag.get('sigterm'):
                stop_reason = 'driver SIGTERM'
            elif tn - last_free >= 2.0:
                last_free = tn; fb = shutil.disk_usage(ROOT).free
                if fb < FLOOR:
                    stop_reason = 'free bytes %d < in-flight floor %d' % (fb, FLOOR)
            if stop_reason:
                termed = tn
                rec['events'].append({'at': now(), 'event': 'SIGTERM', 'reason': stop_reason, 'targets': list(live)})
                for pid in live.values():
                    try:
                        os.kill(pid, signal.SIGTERM)
                    except ProcessLookupError:
                        pass
        if termed is not None and tn - termed > 120 and live:
            rec['events'].append({'at': now(), 'event': 'bounded wait exceeded; survivors recorded, no SIGKILL',
                                  'survivors': dict(live)})
            break
        if live:
            time.sleep(0.5)
    if keep_open:
        os.close(keep); keep_open = False
    for t in ts + [lt]:
        t.join(timeout=180)
    sl.close()
    os.unlink(fifo)
    ss, _ = status_lines(slog); cs, clines = status_lines(clog)
    warn = [l for l in clines if 'WARNING' in l or 'early EOF' in l or 'less than expected' in l]
    rec['drat_stdout_filter'] = lres
    rec.update(finished_at=now(), wall_s=round(time.monotonic() - t0, 3), kissat=done.get('kissat'), drat=done.get('drat'),
               kissat_status_lines=ss, drat_status_lines=cs, drat_warnings=warn,
               kissat_log={'path': str(slog.relative_to(ROOT)), 'sha256': sha_file(slog), 'bytes': slog.stat().st_size},
               drat_log={'path': str(clog.relative_to(ROOT)), 'sha256': sha_file(clog), 'bytes': clog.stat().st_size},
               solver_feed=sres, checker_feed=cres, proof=rres, sampled_peak_resident=peak, stop_reason=stop_reason,
               survivors=dict(live))
    feeds_ok = all(r.get('ok') and r.get('written') == expected_bytes and r.get('sha256') == expected_sha for r in (sres, cres))
    proof_ok = rres.get('error') is None and rres.get('proof_bytes_read') == rres.get('proof_bytes_relayed')
    rec['criteria'] = {'kissat_rc20': (done.get('kissat') or {}).get('rc') == 20, 'kissat_status_exact': ss == ['s UNSATISFIABLE'],
                       'drat_rc0': (done.get('drat') or {}).get('rc') == 0, 'drat_status_exact': cs == ['s VERIFIED'],
                       'no_fatal_drat_warning': not warn, 'drat_log_filter_ok': lres.get('ok') is True, 'feeds_measured_complete': feeds_ok, 'proof_relay_complete': proof_ok,
                       'no_stop': stop_reason is None and not live}
    rec['verdict'] = 'PASS' if all(rec['criteria'].values()) else ('STOPPED_UNKNOWN' if stop_reason else 'FAIL')
    return rec


def gate(label):
    fb = shutil.disk_usage(ROOT).free; used = lane_allocated(ROOT)
    ok = fb - MARGIN >= FRESH and used + MARGIN <= LANE_CAP and time.time() < DEADLINE - 60
    return {'item': label, 'at': now(), 'free_bytes': fb, 'lane_allocated_bytes': used, 'ok': ok}


def main():
    t_start = time.monotonic(); script_sha = sha_file(__file__)
    freeze = json.loads((ROOT/'review/GB_PROBE_FREEZE.r2.json').read_bytes())
    if freeze['script_sha256'] != script_sha:
        raise SystemExit('probe script not frozen')
    pins = {'generator': (GEN, GEN_SHA), 'own_hashes': (OWN, OWN_SHA), 'WMAN': (WMAN, WMAN_SHA),
            'kissat': (KISSAT, KISSAT_SHA), 'drat-trim': (DRAT, DRAT_SHA)}
    pin_res = {k: {'path': str(p), 'sha256': sha_file(p), 'expected': e} for k, (p, e) in pins.items()}
    if any(v['sha256'] != v['expected'] for v in pin_res.values()):
        raise SystemExit('pin mismatch %r' % pin_res)
    stopflag = {}
    signal.signal(signal.SIGTERM, lambda *a: stopflag.update(sigterm=True))
    for d in ('fifo', 'logs', 'tmp', 'receipts'):
        (OUTDIR/d).mkdir(exist_ok=True)
    summary = {'schema': 'gb-probe-r2-summary/1', 'started_at': now(), 'script_sha256': script_sha, 'pins': pin_res,
               'python': sys.version.split()[0], 'scope': 'WORKER timing probe; not parent-qualified; no CNF/proof on disk',
               'items': [], 'gates': []}
    own = json.loads(OWN.read_bytes()); expect = {x['id']: x for x in own['formulas']}
    # tiny transport controls
    controls = [('ctl-tiny-unsat', TINY_UNSAT, TINY_UNSAT, 'PASS expected'),
                ('ctl-sat-checker', TINY_UNSAT, TINY_SAT, 'checker must NOT verify (checker gets satisfiable CNF)')]
    for label, sbytes, cbytes, purpose in controls:
        if sbytes == cbytes:
            rec = pipeline(label, [sbytes], len(sbytes), sha_bytes(sbytes), 10, 10, stopflag)
            ok = rec['verdict'] == 'PASS'
        else:
            rec = control_mismatch(label, sbytes, cbytes, stopflag)
            ok = rec['drat_status_lines'] == ['s NOT VERIFIED'] and (rec['drat'] or {}).get('rc') != 0
        rec['purpose'] = purpose; rec['control_ok'] = ok
        rec['receipt_sha256'] = xjson(OUTDIR/'receipts'/(label + '.json'), rec)
        summary['items'].append({'label': label, 'control_ok': ok, 'receipt_sha256': rec['receipt_sha256']})
        if not ok:
            summary['stopped'] = 'control failed: ' + label
            return finish(summary, t_start)
    # in-memory GB generation through the frozen adapter functions
    spec = importlib.util.spec_from_file_location('frozen_gb_one_p4_r2', GEN)
    gen = importlib.util.module_from_spec(spec); sys.modules[spec.name] = gen; spec.loader.exec_module(gen)
    if sha_file(GEN) != GEN_SHA:
        raise SystemExit('generator changed')
    tg = time.monotonic(); gb = gen.load_gb(); original = gb.F
    try:
        gb.F = gen.make_sink(original, None)
        f = gb.encode(8, [1, 2, 3, 4, 5], 0, [1], True, fixg=None, g5=True, allrows=False, allcols=False)
    finally:
        gb.F = original
    f.guard(); body = f.body
    if sha_bytes(body) != BODY_SHA:
        raise SystemExit('GB body hash mismatch')
    summary['generation'] = {'seconds': round(time.monotonic() - tg, 3), 'body_bytes': len(body), 'body_sha256': BODY_SHA,
                             'variables': f.n, 'clauses': f.count,
                             'self_ru_maxrss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    cases = {x['id']: x for x in json.loads(WMAN.read_bytes())['cases']}
    for cid, ksec, dsec in GB_ITEMS:
        g = gate(cid); summary['gates'].append(g)
        if not g['ok'] or stopflag.get('sigterm'):
            summary['items'].append({'label': 'GB-' + cid, 'verdict': 'NOT_STARTED', 'gate': g})
            break
        units = gen.template_units(f, cases[cid])
        header = ('p cnf %d %d\n' % (f.n, f.count + 42)).encode(); tail = ''.join('%d 0\n' % v for v in units).encode()
        h = hashlib.sha256(header); h.update(body); h.update(tail)
        nbytes = len(header) + len(body) + len(tail)
        if h.hexdigest() != expect[cid]['CNF_sha256'] or nbytes != expect[cid]['bytes']:
            raise SystemExit('GB formula identity mismatch for ' + cid)
        rec = pipeline('GB-' + cid, [header, body, tail], nbytes, h.hexdigest(), ksec, dsec, stopflag)
        rec.update(formula_id=cid, gb_formula_sha256=h.hexdigest(), gb_formula_bytes=nbytes,
                   identity='equals GB_ONE_P4_OWN_HASHES.r2 and parent GBBINDING (22 MATCH)')
        rec['receipt_sha256'] = xjson(OUTDIR/'receipts'/('GB-' + cid + '.json'), rec)
        summary['items'].append({'label': 'GB-' + cid, 'verdict': rec['verdict'], 'wall_s': rec['wall_s'],
                                 'kissat': rec['kissat'], 'drat': rec['drat'], 'proof_bytes': rec['proof'].get('proof_bytes_read'),
                                 'proof_sha256': rec['proof'].get('proof_sha256'), 'peak': rec['sampled_peak_resident'],
                                 'stop_reason': rec['stop_reason'], 'receipt_sha256': rec['receipt_sha256']})
        if rec['verdict'] != 'PASS':
            break
    return finish(summary, t_start)


def control_mismatch(label, sbytes, cbytes, stopflag):
    """Solver gets sbytes; checker gets cbytes (a deliberately different CNF)."""
    parts_s, parts_c = [sbytes], [cbytes]
    fifo = OUTDIR/'fifo'/(label + '.drat.fifo')
    slog = OUTDIR/'logs'/(label + '.kissat.log'); clog = OUTDIR/'logs'/(label + '.drat.log')
    os.mkfifo(fifo)
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    fcntl.fcntl(rfd, fcntl.F_SETFL, fcntl.fcntl(rfd, fcntl.F_GETFL) & ~os.O_NONBLOCK)
    keep = os.open(fifo, os.O_WRONLY)
    sr, sw = os.pipe(); cr, cw = os.pipe(); pr, pw = os.pipe()
    sl, cl = open(slog, 'xb'), open(clog, 'xb')
    dp = subprocess.Popen([DRAT, '/dev/fd/%d' % cr, '-i', '-t', '10'], stdin=pr, stdout=cl, stderr=subprocess.STDOUT,
                          pass_fds=(cr,), cwd=str(OUTDIR/'tmp'))
    kp = subprocess.Popen([KISSAT, '--time=10', '/dev/fd/%d' % sr, str(fifo)], stdin=subprocess.DEVNULL, stdout=sl,
                          stderr=subprocess.STDOUT, pass_fds=(sr,), cwd=str(OUTDIR/'tmp'))
    for fd in (sr, cr, pr):
        os.close(fd)
    sres, cres, rres = {}, {}, {}
    ts = [threading.Thread(target=writer, args=(sw, parts_s, sres)), threading.Thread(target=writer, args=(cw, parts_c, cres)),
          threading.Thread(target=relay, args=(rfd, pw, rres))]
    for t in ts:
        t.start()
    _, kst, _ = os.wait4(kp.pid, 0); os.close(keep)
    _, dst, _ = os.wait4(dp.pid, 0)
    for t in ts:
        t.join(timeout=30)
    sl.close(); cl.close(); os.unlink(fifo)
    ss, _ = status_lines(slog); cs, _ = status_lines(clog)
    return {'label': label, 'at': now(), 'kissat': {'rc': os.waitstatus_to_exitcode(kst)}, 'drat': {'rc': os.waitstatus_to_exitcode(dst)},
            'kissat_status_lines': ss, 'drat_status_lines': cs, 'solver_feed': sres, 'checker_feed': cres, 'proof': rres,
            'kissat_log_sha256': sha_file(slog), 'drat_log_sha256': sha_file(clog)}


def finish(summary, t_start):
    summary['finished_at'] = now(); summary['seconds'] = round(time.monotonic() - t_start, 3)
    summary['self_ru_maxrss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    sh = xjson(OUTDIR/'SUMMARY.r2.json', summary)
    print(json.dumps({'summary_sha256': sh, 'items': summary['items']}, default=str), flush=True)


if __name__ == '__main__':
    main()
