#!/usr/bin/env python3
"""PA19FinalFormulaBindings bounded extend_b list replay v1 (Main OK ~05:0x): ONE child re-executing the unchanged lane
producer src/extend_b.py for the single producer-only M2 split list cycle2/m2part_drat/ms09_b00002/ext.json, with the
production argv (python3.14 <LANE>/src/extend_b.py <LANE>/cycle2/skel-b/skeletons-b-ms09.json 2 OUT); transformation:
OUT is a fresh desk FIFO (0 B on disk), bytes hashed/compared in RAM. Supervision: unchanged lane
enumeration_helper_guard_v3.run_helper with S = stream_check15, under ONE regular existing token (O_RDONLY flock, never
written) plus the existing helper lock taken by run_helper; helper_seconds 300, rss_cap 512 MiB, in-flight floor 12e9,
fresh admission gate 12,334,217,728 B. Comparator: byte equality, else parsed equality of ALL fields with identical
key sets (source must equal the production absolute skel path); no ignored field. List binding only.

Run: /opt/homebrew/opt/python@3.14/bin/python3.14 -B -I <desk>/fb_m2list_v1.py run --lane <LANE>
"""
import hashlib
import json
import os
import sys
import threading
import time
import types
from collections import OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
M2_SHA = '49506607d3f6a50a10f4d9ceb5b526b7729cef125023968d9b1cbd73a1ad6f58'


def _load(name, path, want):
    b = Path(path).read_bytes()
    if hashlib.sha256(b).hexdigest() != want:
        raise SystemExit('%s changed' % path)
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    sys.modules[name] = mod
    exec(compile(b, str(path), 'exec'), mod.__dict__)
    return mod


M = _load('fb_m2_v1', HERE / 'fb_m2_v1.py', M2_SHA)
F = M.F
L = F.L
EXTEND_B = (L / 'src' / 'extend_b.py', '31924ed66099baf6f03436e6d51793549cd45e96416200aeea8c23af651a26d7')
SKEL = 'cycle2/skel-b/skeletons-b-ms09.json'
STORED = ('cycle2/m2part_drat/ms09_b00002/ext.json', '3e170c366ffac37ba3906540a6f81f5588d03d94983f83c807dd6eee7962dd8d')
KEYS = {'source', 'index', 'raw_class_assignments', 'automorphisms', 'num_placements', 'placements'}


def compare(stored, replay):
    out = OrderedDict([('stored_sha256', F.sha(stored)), ('replay_sha256', F.sha(replay)), ('replay_bytes', len(replay))])
    if out['stored_sha256'] == out['replay_sha256']:
        out['verdict'] = 'BYTE_EQUAL'
        return out
    try:
        a, b = json.loads(stored), json.loads(replay)
    except ValueError as ex:
        out['verdict'], out['reason'] = 'MISMATCH', repr(ex)
        return out
    diffs = [] if (set(a) == KEYS and set(b) == KEYS) else ['key_set']
    if not diffs:
        diffs = [k for k in sorted(KEYS) if a[k] != b[k]]
        if a['source'] != str(L / SKEL):
            diffs.append('source_not_production_path')
    out['differences'] = diffs
    out['verdict'] = 'SEMANTIC_EQUAL_ALL_FIELDS' if not diffs else 'MISMATCH'
    return out


def main():
    if sys.argv[1:2] != ['run']:
        raise SystemExit(__doc__)
    args = F.parse_args(sys.argv[2:])
    F.require_env(args)
    os.chdir(HERE)
    r0 = json.loads(F.REF['r0_pin_result'][0].read_bytes())['files']
    sk_sha, sk_l = F.sha_file(F.S_IN / SKEL)[0], F.sha_file(L / SKEL)[0]
    pins = {'extend_b.py': {'sha256': F.sha_file(EXTEND_B[0])[0], 'expected': EXTEND_B[1], 'R0_pin': r0.get('src/extend_b.py')},
            'skeletons-b-ms09.json': {'L_sha256': sk_l, 'S_sha256': sk_sha, 'R0_pin': r0.get(SKEL)},
            'stored_list': {'path': STORED[0], 'sha256': F.sha_file(L / STORED[0])[0], 'expected': STORED[1]},
            'interpreter': {'path': F.PY, 'sha256': F.sha_file(os.path.realpath(F.PY))[0]}, 'fb_m2_v1.py': M2_SHA,
            'driver_sha256': F.sha_file(Path(__file__).resolve())[0]}
    if not (pins['extend_b.py']['sha256'] == EXTEND_B[1] == pins['extend_b.py']['R0_pin'] and sk_sha == sk_l == r0.get(SKEL)
            and pins['stored_list']['sha256'] == STORED[1]):
        raise SystemExit('pin mismatch: %r' % pins)
    S = F.load_module('stream_check15', F.HELPER_MODS[0][1], F.HELPER_MODS[0][2])
    H = F.load_module('enumeration_helper_guard_v3', F.HELPER_MODS[1][1], F.HELPER_MODS[1][2])
    S.install_sigterm_handler()
    S.set_stop_files([str(F.STOPFILE)])
    d = HERE / 'm2list'
    d.mkdir(exist_ok=False)
    fifo = d / 'ms09_b00002.fifo'
    os.mkfifo(fifo)
    cmd = [F.PY, '-B', '-I', '-X', 'pycache_prefix=%s' % (HERE / 'nopyc'), str(EXTEND_B[0]), str(L / SKEL), '2', str(fifo)]
    stored = (L / STORED[0]).read_bytes()
    got = {'h': hashlib.sha256(), 'n': 0, 'buf': [], 'err': None, 'opened': False}

    def reader():
        try:
            fd = os.open(fifo, os.O_RDONLY)
            got['opened'] = True
            while True:
                b = os.read(fd, 1 << 20)
                if not b:
                    break
                got['h'].update(b)
                got['n'] += len(b)
                if got['n'] <= 32 * 1024 * 1024:
                    got['buf'].append(b)
            os.close(fd)
        except OSError as ex:
            got['err'] = repr(ex)
    rec = OrderedDict([('title', 'PA19 bounded extend_b replay of cycle2/m2part_drat/ms09_b00002/ext.json (list binding only)'),
                       ('pins', pins), ('cmd', cmd), ('started', F.now())])
    original_spawn = S.spawn

    def guarded_spawn(c, stdin=False):
        fb, need, ok = F.disk_gate(0)
        adm = {'fresh_free_bytes': fb, 'required_free_bytes': need, 'host_clock': F.now(),
               'inputs_unchanged': F.sha_file(EXTEND_B[0])[0] == EXTEND_B[1] and F.sha_file(L / SKEL)[0] == sk_l
               and F.sha_file(L / STORED[0])[0] == STORED[1]}
        rec['admission'] = adm
        if not ok or not adm['inputs_unchanged']:
            raise S.AdmissionDenied('admission gate: %r' % adm)
        tmp = HERE / 'tmp' / ('m2list-%d' % time.time_ns())
        tmp.mkdir(exist_ok=False)
        os.environ['TMPDIR'] = str(tmp)
        adm['owned_tmpdir'] = str(tmp)
        return original_spawn(c, stdin)
    S.spawn = guarded_spawn
    th = threading.Thread(target=reader, daemon=True)
    th.start()
    with F.Token() as tok:
        rec['token'] = {'name': tok.name, 'acquired_at': tok.acquired_at, 'waited_s': tok.waited_s}
        try:
            rc, text, info = H.run_helper(S, cmd, str(d), time.monotonic() + 600, F.RUN_WALL_DEADLINE - F.SHUTDOWN_RESERVE,
                                          helper_seconds=300.0, term_wait=60.0, sample_seconds=1.0, rss_cap_kb=512 * 1024,
                                          inflight_floor_bytes=F.INFLIGHT_FLOOR)
        except S.AdmissionDenied as ex:
            rc, text, info = None, '', {'admission_denied': str(ex), 'guard_tripped': True}
        finally:
            S.spawn = original_spawn
            if th.is_alive():
                try:
                    os.close(os.open(fifo, os.O_WRONLY | os.O_NONBLOCK))
                except OSError:
                    pass
                th.join(timeout=30)
    rec.update({'rc': rc, 'helper': info, 'out_tail': text[-1000:], 'fifo': {'bytes': got['n'], 'sha256': got['h'].hexdigest(),
                'opened': got['opened'], 'reader_error': got['err'], 'reader_alive': th.is_alive()}})
    if rc == 0 and not info.get('guard_tripped') and got['opened'] and not got['err'] and not th.is_alive() and got['n'] > 0:
        rec['comparison'] = compare(stored, b''.join(got['buf']))
        rec['status'] = rec['comparison']['verdict']
    else:
        rec['status'] = 'UNKNOWN'
    rec['post_inputs_unchanged'] = (F.sha_file(EXTEND_B[0])[0] == EXTEND_B[1] and F.sha_file(L / SKEL)[0] == sk_l
                                    and F.sha_file(L / STORED[0])[0] == STORED[1])
    if not rec['post_inputs_unchanged']:
        rec['status'] = 'UNKNOWN'
    rec['finished'] = F.now()
    F.dump_x(d / 'ms09_b00002-replay-v1.json', rec)
    F.log('m2list ms09_b00002: %s, %s s, peak child RSS %s KB; receipt sha %s' % (
        rec['status'], info.get('seconds'), info.get('peak_rss_kb'), F.sha_file(d / 'ms09_b00002-replay-v1.json')[0]))
    print(json.dumps({'status': rec['status'], 'seconds': info.get('seconds'), 'peak_rss_kb': info.get('peak_rss_kb')}))


if __name__ == '__main__':
    main()
