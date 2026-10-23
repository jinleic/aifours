#!/usr/bin/env python3
"""PA19FinalFormulaBindings M2 driver v2 = v1 (49506607d3f6a50a10f4d9ceb5b526b7729cef125023968d9b1cbd73a1ad6f58) with
three changes for Main's delta request (IRC ~06:0x 2026-10-18): (1) `--no-token 1` replaces the lane token by a recorded
no-token context (Main: "Use no token unless a list replay is required"); (2) empty job files load as zero jobs; (3)
controls write m2-controls-v2.json (v1's receipt name already exists). No rebuild, comparator or check changed.
v1 docstring follows.
PA19FinalFormulaBindings M2 driver v1 -- formula binding only for the M2 direct (encode_skel_b.build_v2) and E0-B
(encode_q0b) CNFs. Main IRC ~02:5x 2026-10-18: after the frozen M1 jobs, rebuild all counted M2 direct CNFs from the
parent-bound B skeleton lists and the E0-B CNFs identified by their receipts; freeze the point-in-time record list
first, later only a delta for newly completed records. A PASS binds a record's recorded cnf_sha256/cnf_bytes to the
declared producer applied to its declared inputs; it is NOT an UNSAT acceptance, NOT M2 coverage (M2 stays open), and
no STATUS file is read. No solver, proof checker or proof file; CNF bytes only in RAM.

Reuses (hash-pinned imports, unchanged): fb_v1.py helpers (token/disk/log/x-mode writes/module loader) and
PA19FinalReceiptAudit m1_receipts_v1.stream_predicate (its strict stream-record schema; reported per record as
metadata, never as coverage).

Run: /opt/homebrew/opt/python@3.14/bin/python3.14 -B -I <desk>/fb_m2_v1.py CMD --lane <LANE> [options]
  pin      --name N [--base SHA]   freeze census (no rebuild) -> m2-pins-N.json, m2-jobs-N.jsonl.gz; with --base, only
                                   records absent from / changed since that earlier pin (delta)
  run      --pins SHA --name N     rebuild every job in RAM -> m2-N.jsonl.gz, m2-run-N.json
  controls --pins SHA              in-memory overlay controls -> m2-controls-v1.json
"""
import copy
import gzip
import json
import os
import sys
import time
import types
from collections import Counter, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
FB_V1 = HERE / 'fb_v1.py'
FB_V1_SHA = '23219f5d8feb806277b7368ac656c13dbba8e0e517fae800d4d69e811be875ee'


def _load_fb():
    import hashlib
    b = FB_V1.read_bytes()
    if hashlib.sha256(b).hexdigest() != FB_V1_SHA:
        raise SystemExit('fb_v1.py changed')
    mod = types.ModuleType('fb_v1')
    mod.__file__ = str(FB_V1)
    sys.modules['fb_v1'] = mod
    exec(compile(b, str(FB_V1), 'exec'), mod.__dict__)
    return mod


F = _load_fb()
L, REPO, S_IN, AUD = F.L, F.REPO, F.S_IN, F.AUD
M1R = (AUD / 'm1_receipts_v1.py', 'b4e7baa2605ab91776b1fc9cdff7f11a051d07f12fedddf8697f2251b9743a32')
ESB = (F.R8SRC / 'encode_skel_b.py', 'd0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5')
Q0B = (L / 'src' / 'encode_q0b.py', '3c431849be93bb198adf484e5dac144bd0ab56d86f541913bd9b17435586e24d')
R3 = (F.COVER / 'generator-semantic-check-v1.json', '939d1ea79a4a556920097b38497b22718855ffbcc4e5ef7a0d821c05026e3514')
P0 = [4, 3, 3, 3, 3, 3]
DIRECT = L / 'cycle2' / 'm2skel_drat'
E0B = L / 'm2q0c' / 'results'
SENT = '<fb_m2_v1 in-memory CNF sink>'


class NoToken:
    """v2: recorded no-token context (Main-authorized for the delta stage only)."""
    name, acquired_at, waited_s = 'none (Main IRC 2026-10-18: no token for the M2 delta)', None, 0.0

    def __enter__(self):
        self.acquired_at = F.now()
        return self

    def __exit__(self, *a):
        return False


def tokctx(args):
    return NoToken() if args.get('--no-token') == '1' else F.Token()


def skel_rel(mi):
    return 'cycle2/skel-b/skeletons-b-ms%02d.json' % mi


def load_libs():
    sys.dont_write_bytecode = True
    m1r = F.load_module('m1_receipts_v1', M1R[0], M1R[1])
    esb = F.load_module('encode_skel_b', ESB[0], ESB[1])
    q0b = F.load_module('encode_q0b', Q0B[0], Q0B[1])
    return m1r, esb, q0b


def q0b_bytes(q0b, g6):
    """encode_q0b.main() unchanged with argv [script, g6, SENTINEL]; its module-global open() and print() are shadowed
    by in-memory sinks (production run_m2q0c.py ran `python encode_q0b.py g6 /dev/stdout` and stripped the trailing
    JSON summary line from stdout). Returns (cnf bytes, summary dict, runner-transform bytes)."""
    sink = F._Sink()
    calls, printed = [], []

    def fake_open(path, mode='r', *a, **k):
        calls.append([path, mode])
        if path != SENT or mode != 'w' or a or k:
            raise RuntimeError('unexpected open(%r, %r)' % (path, mode))
        return sink

    def fake_print(*a, **k):
        if k:
            raise RuntimeError('unexpected print kwargs %r' % k)
        printed.append(' '.join(str(x) for x in a))
    old = sys.argv
    sys.argv = [str(Q0B[0]), g6, SENT]
    q0b.open, q0b.print = fake_open, fake_print
    try:
        q0b.main()
    finally:
        del q0b.open, q0b.print
        sys.argv = old
    if calls != [[SENT, 'w']] or len(printed) != 1:
        raise RuntimeError('unexpected writer calls %r / prints %d' % (calls, len(printed)))
    cnf = ''.join(sink.parts).encode('ascii')
    stdout = cnf + printed[0].encode() + b'\n'          # what /dev/stdout received in production
    lines = stdout.split(b'\n')                         # run_m2q0c.py lines 33-37, verbatim logic
    while lines and not lines[-1].strip():
        lines.pop()
    info = json.loads(lines.pop().decode())
    runner_cnf = b'\n'.join(lines) + b'\n'
    return cnf, info, runner_cnf


# ----------------------------------------------------------------------------- pin
def record_row(m1r, kind, rel, data):
    rec = json.loads(data)
    why, tier = m1r.stream_predicate(rec)
    row = OrderedDict([('kind', kind), ('path', rel), ('rec_sha', F.sha(data)), ('bytes', len(data)),
                       ('rev', rec.get('stream_check_revision')), ('status', rec.get('status')),
                       ('solver_family', m1r.solver_family(rec)),
                       ('strict_predicate_reasons', why), ('strict_predicate_tier', tier),
                       ('checker_rejected', m1r.checker_rejected(rec)), ('sat_claim', m1r.sat_claim(rec)),
                       ('encoder', rec.get('encoder')), ('runner', rec.get('runner')),
                       ('recorded', [rec.get('cnf_sha256'), rec.get('cnf_bytes')])])
    if kind == 'm2direct':
        row['multiset'], row['b_index'], row['generator'] = rec.get('multiset'), rec.get('b_index'), rec.get('generator')
    else:
        row['graph_index'], row['graph6'], row['encoder_info'] = rec.get('graph_index'), rec.get('graph6'), rec.get('encoder_info')
    return row


def cmd_pin(args):
    name = args['--name']
    out_p, jobs_p = F.HERE / ('m2-pins-%s.json' % name), F.HERE / ('m2-jobs-%s.jsonl.gz' % name)
    base = None
    if '--base' in args:
        bp = next(p for p in F.HERE.glob('m2-pins-*.json') if F.sha_file(p)[0] == args['--base'])
        base = json.loads(bp.read_bytes())
        base_jobs = {j['path']: j for j in (json.loads(x) for x in gzip.decompress(
            (F.HERE / base['jobs_file']['path']).read_bytes()).decode().splitlines())}
    fb, need, ok = F.disk_gate(8 * 1024 * 1024)
    if not ok:
        F.log('m2 pin %s DEFERRED: free %d < gate %d' % (name, fb, need))
        raise SystemExit('disk gate')
    m1r, esb, q0b = load_libs()
    t0 = time.time()
    with tokctx(args) as tok:
        token = {'name': tok.name, 'acquired_at': tok.acquired_at, 'waited_s': tok.waited_s}
        refs = F.check_refs()
        if not all(v['match'] for v in refs.values()):
            raise SystemExit('reference receipt mismatch: %s' % [k for k, v in refs.items() if not v['match']])
        r0 = json.loads(F.REF['r0_pin_result'][0].read_bytes())['files']
        r3 = json.loads(R3[0].read_bytes())
        if F.sha_file(R3[0])[0] != R3[1] or not all(F.sha_file(p)[0] == w for p, w in (M1R, ESB, Q0B)):
            raise SystemExit('pinned library/receipt changed')
        r3rows = {row['multiset']: row for row in r3['rows']}
        skels = OrderedDict()
        for mi in range(1, 10):
            rel = skel_rel(mi)
            sh, lh = F.sha_file(S_IN / rel)[0], F.sha_file(L / rel)[0]
            d = json.loads((S_IN / rel).read_bytes())
            skels[str(mi)] = {'path': rel, 'S_sha256': sh, 'L_sha256': lh, 'R0_pin': r0.get(rel),
                              'R3_B_byte_equal': (r3rows.get(mi) or {}).get('B_byte_equal'),
                              'R3_verdict': (r3rows.get(mi) or {}).get('verdict'),
                              'num_skeletons': len(d['skeletons']), 'c0': d['c0'],
                              'special': [p for p in d['profiles'] if list(p) != P0]}
            skels[str(mi)]['bound'] = (sh == lh == skels[str(mi)]['R0_pin'] and skels[str(mi)]['R3_B_byte_equal'] is True
                                       and d.get('multiset_index') == mi and d.get('num_skeletons') == len(d['skeletons']))
        g6s = [x.strip() for x in F.REF['r2_bound_graph6'][0].read_text().splitlines() if x.strip()]
        code = {'encode_skel_b.py': {'path': str(ESB[0].relative_to(REPO)), 'sha256': ESB[1],
                                     'L_src_sha256': F.sha_file(L / 'src' / 'encode_skel_b.py')[0], 'R0_pin': r0.get('src/encode_skel_b.py')},
                'encode_q0b.py': {'path': str(Q0B[0].relative_to(REPO)), 'sha256': Q0B[1], 'R0_pin': r0.get('src/encode_q0b.py')},
                'm1_receipts_v1.py(stream_predicate)': {'path': str(M1R[0].relative_to(REPO)), 'sha256': M1R[1]},
                'fb_v1.py(helpers)': {'sha256': FB_V1_SHA}, 'fb_m2_v1.py': {'sha256': F.sha_file(Path(__file__).resolve())[0]}}
        listing_started = F.now()
        rows, skipped = [], []
        for kind, base_dir, pat in (('m2direct', DIRECT, 'ms*_b*.json'), ('e0b', E0B, 'g*.json')):
            for p in sorted(base_dir.glob(pat)):
                rel = str(p.relative_to(L))
                try:
                    data = p.read_bytes()
                    row = record_row(m1r, kind, rel, data)
                    row['mtime_ns'] = p.stat().st_mtime_ns
                except (OSError, ValueError) as ex:
                    row = OrderedDict([('kind', kind), ('path', rel), ('rec_sha', None), ('unreadable', repr(ex))])
                if base is not None and rel in base_jobs and base_jobs[rel]['rec_sha'] == row.get('rec_sha'):
                    skipped.append(rel)
                    continue
                if base is not None:
                    row['delta'] = 'changed since base pin' if rel in base_jobs else 'new since base pin'
                rows.append(row)
        listing_ended = F.now()
        removed = sorted(set(base_jobs) - {str(p.relative_to(L)) for d_, pat in ((DIRECT, 'ms*_b*.json'), (E0B, 'g*.json'))
                                            for p in d_.glob(pat)}) if base is not None else []
        for i, r in enumerate(rows):
            r['i'] = i
        cnt = Counter('%s|rev=%s|%s|strict=%s' % (r['kind'], r.get('rev'), r.get('status'),
                                                 'pass' if r.get('strict_predicate_reasons') == [] else 'fail') for r in rows)
        pins = OrderedDict([
            ('title', 'PA19 M2 direct + E0-B formula-binding census %s (point-in-time freeze; no rebuild yet)' % name),
            ('recorded_started', listing_started), ('recorded_finished', listing_ended), ('token', token),
            ('proc', F.proc_info()), ('reference_receipts', refs), ('code', code),
            ('b_skeleton_lists', skels), ('graph6', {'path': str(F.REF['r2_bound_graph6'][0].relative_to(REPO)),
                                                     'sha256': F.REF['r2_bound_graph6'][1], 'lines': len(g6s),
                                                     'L_sha256': F.sha_file(L / 'data' / 'quadgraphs-8v-13to16e-D4.g6')[0]}),
            ('base_pin', args.get('--base')), ('delta_skipped_unchanged', len(skipped)), ('delta_removed', removed),
            ('census', {'records': len(rows), 'by_kind_rev_status_strict': dict(sorted(cnt.items())),
                        'strict_predicate_pass': sum(1 for r in rows if r.get('strict_predicate_reasons') == []),
                        'unreadable': [r['path'] for r in rows if r.get('rec_sha') is None]}),
            ('production_calls', {
                'm2direct': 'run_m2skel5-9.py / run_m2_12-15.py: d = skeletons-b-msXX.json; sk = d["skeletons"][b_index]; '
                            'special = [p for p in d["profiles"] if list(p) != [4,3,3,3,3,3]]; nv, cl = '
                            'encode_skel_b.build_v2(d["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special); '
                            'encode_skel_b.cnf_bytes(nv, cl)',
                'e0b': 'run_m2q0c.py: subprocess [python, encode_q0b.py, gs[i], /dev/stdout]; trailing summary line removed; '
                       'gs = non-empty stripped lines of data/quadgraphs-8v-13to16e-D4.g6'}),
            ('not_claimed', 'formula binding only; no UNSAT acceptance; M2 coverage open; STATUS not read'),
            ('resources', {**F.usage(), 'elapsed_s': round(time.time() - t0, 2), 'free_bytes_end': F.free_bytes()})])
    jb = gzip.compress(('\n'.join(F.jline(r) for r in rows) + '\n').encode(), mtime=0)
    F.write_x(jobs_p, jb)
    pins['jobs_file'] = {'path': jobs_p.name, 'sha256': F.sha(jb), 'bytes': len(jb), 'lines': len(rows)}
    F.dump_x(out_p, pins)
    ps = F.sha_file(out_p)[0]
    F.log('m2 pin %s: %d records (%s); strict-predicate pass %d; B lists bound %d/9; token %s waited %.1f s; %s sha %s' % (
        name, len(rows), dict(Counter(r['kind'] for r in rows)), pins['census']['strict_predicate_pass'],
        sum(1 for s in skels.values() if s['bound']), token['name'], token['waited_s'], out_p.name, ps))
    print(json.dumps({'pins_sha256': ps, 'census': pins['census'], 'skipped_unchanged': len(skipped), 'removed': removed,
                      'b_lists_bound': {k: v['bound'] for k, v in skels.items()}}, indent=1))


def load_m2_pins(sha):
    p = next((p for p in F.HERE.glob('m2-pins-*.json') if F.sha_file(p)[0] == sha), None)
    if p is None:
        raise SystemExit('no m2 pins file with sha %s' % sha)
    pins = json.loads(p.read_bytes())
    jb = (F.HERE / pins['jobs_file']['path']).read_bytes()
    if F.sha(jb) != pins['jobs_file']['sha256']:
        raise SystemExit('m2 jobs file changed')
    if not all(F.sha_file(q)[0] == w for q, w in (M1R, ESB, Q0B, R3)):
        raise SystemExit('pinned library/receipt changed')
    return pins, [json.loads(x) for x in gzip.decompress(jb).decode().splitlines() if x.strip()]


class Inputs:
    def __init__(self, pins):
        self.pins, self.sk, self.g6 = pins, {}, None

    def skel(self, mi):
        if mi not in self.sk:
            e = self.pins['b_skeleton_lists'].get(str(mi))
            b = (S_IN / e['path']).read_bytes() if e else None
            self.sk[mi] = json.loads(b) if (e and e['bound'] and F.sha(b) == e['S_sha256']) else None
        return self.sk[mi]

    def graph6(self):
        if self.g6 is None:
            b = F.REF['r2_bound_graph6'][0].read_bytes()
            if F.sha(b) != self.pins['graph6']['sha256']:
                raise SystemExit('graph6 list changed')
            self.g6 = [x.strip() for x in b.decode().splitlines() if x.strip()]
        return self.g6


def evaluate(libs, inp, job, ov=None):
    ov = ov or {}
    m1r, esb, q0b = libs
    res = OrderedDict([('i', job['i']), ('kind', job['kind']), ('path', job['path'])])
    checks = OrderedDict()
    try:
        data = (L / job['path']).read_bytes()
    except FileNotFoundError:
        res['status'], res['reason'] = 'UNRESOLVED', 'record_missing'
        return res
    res['rec_sha'] = F.sha(data)
    checks['record_sha_equals_pinned'] = res['rec_sha'] == job['rec_sha']
    if not checks['record_sha_equals_pinned']:
        res['checks_false'], res['status'] = ['record_sha_equals_pinned'], 'UNRESOLVED'
        return res
    rec = json.loads(data)
    if 'rec' in ov:
        rec = ov['rec'](copy.deepcopy(rec))
    fn = job['path'].rsplit('/', 1)[1]
    cs = rec.get('cnf_sha256')
    checks['recorded_cnf_sha256_wellformed'] = isinstance(cs, str) and F.HEX64.match(cs) is not None
    checks['recorded_cnf_bytes_positive_int'] = type(rec.get('cnf_bytes')) is int and rec.get('cnf_bytes') > 0
    t = time.perf_counter()
    if job['kind'] == 'm2direct':
        mi, bi = ov.get('mi_bi', (int(fn[2:4]), int(fn[6:11])))
        checks['canonical_filename'] = fn == 'ms%02d_b%05d.json' % (int(fn[2:4]), int(fn[6:11]))
        checks['multiset_field_equals_filename'] = rec.get('multiset') == int(fn[2:4])
        checks['b_index_field_equals_filename'] = rec.get('b_index') == int(fn[6:11])
        checks['declared_encoder_build_v2'] = rec.get('encoder') == 'encode_skel_b.build_v2'
        checks['declared_generator_gen_skel_b'] = rec.get('generator') == 'gen_skel_b.py'
        d = ov['skel'] if 'skel' in ov else inp.skel(mi)
        checks['b_list_bound'] = d is not None
        checks['b_index_within_list'] = d is not None and 0 <= bi < len(d['skeletons'])
        if any(v is False for v in checks.values()):
            res['checks_false'] = [k for k, v in checks.items() if v is False]
            res['status'] = 'FAIL_INPUT_BINDING' if not checks['b_list_bound'] else 'FAIL_STRUCTURAL'
            return res
        sk = d['skeletons'][bi]
        special = ov.get('special', [p for p in d['profiles'] if list(p) != P0])
        before = F.jdigest([d['c0'], sk, special])
        try:
            nv, cl = esb.build_v2(d['c0'], [tuple(t_) for t_ in sk['types']], sk['empty'], special)
            b = esb.cnf_bytes(nv, cl)
        except Exception as ex:  # encoder refused the inputs: never a PASS
            res['checks_false'], res['status'] = ['rebuild_possible'], 'UNRESOLVED'
            res['reason'] = 'rebuild not possible: %r' % (ex,)
            return res
        checks['inputs_not_mutated_by_encoder'] = before == F.jdigest([d['c0'], sk, special])
        res['call'] = 'encode_skel_b.build_v2 + encode_skel_b.cnf_bytes (S skeletons-b-ms%02d.json[%d])' % (mi, bi)
        del cl
    else:
        gi = int(fn[1:4])
        g6 = ov.get('graph6') or inp.graph6()[gi]
        checks['canonical_filename'] = fn == 'g%03d.json' % gi
        checks['graph_index_field_equals_filename'] = rec.get('graph_index') == gi
        checks['graph6_field_equals_bound_list'] = rec.get('graph6') == inp.graph6()[gi]
        checks['declared_encoder_q0b'] = rec.get('encoder') == 'encode_q0b.py'
        checks['declared_runner_m2q0c'] = rec.get('runner') == 'run_m2q0c.py'
        if any(v is False for v in checks.values()):
            res['checks_false'] = [k for k, v in checks.items() if v is False]
            res['status'] = 'FAIL_STRUCTURAL'
            return res
        try:
            b, info, runner_b = q0b_bytes(q0b, g6)
        except Exception as ex:
            res['checks_false'], res['status'] = ['rebuild_possible'], 'UNRESOLVED'
            res['reason'] = 'rebuild not possible: %r' % (ex,)
            return res
        checks['runner_transform_equals_writer_bytes'] = runner_b == b
        checks['encoder_info_equal'] = info == rec.get('encoder_info')
        res['call'] = 'encode_q0b.main (in-memory open/print) + run_m2q0c stdout transform'
    res['build_s'] = round(time.perf_counter() - t, 3)
    nvh, nch = F.header(b)
    res['gen'] = [F.sha(b), len(b), nvh, nch]
    res['rec'] = [rec.get('cnf_sha256'), rec.get('cnf_bytes')]
    del b
    checks['cnf_sha256_equal'] = res['gen'][0] == rec.get('cnf_sha256')
    checks['cnf_bytes_equal'] = res['gen'][1] == rec.get('cnf_bytes')
    bad = [k for k, v in checks.items() if v is False]
    res['checks_false'] = bad
    res['status'] = 'PASS' if not bad else ('MISMATCH' if all(
        k in ('cnf_sha256_equal', 'cnf_bytes_equal', 'encoder_info_equal', 'runner_transform_equals_writer_bytes',
              'inputs_not_mutated_by_encoder') for k in bad) else 'FAIL_STRUCTURAL')
    return res


def cmd_run(args):
    pins, jobs = load_m2_pins(args['--pins'])
    name = args['--name']
    F.signal.signal(F.signal.SIGTERM, F.on_term)
    fb, need, ok = F.disk_gate(8 * 1024 * 1024)
    if not ok:
        F.log('m2 run %s DEFERRED: free %d < gate %d' % (name, fb, need))
        raise SystemExit('disk gate')
    libs = load_libs()
    inp = Inputs(pins)
    out_p = F.HERE / ('m2-%s.jsonl.gz' % name)
    raw = open(out_p, 'xb')
    gz = gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='')
    t0 = time.time()
    mono = time.monotonic() + F.CHUNK_SECONDS - F.SHUTDOWN_RESERVE
    started = F.now()
    st, n, end_reason, last_ck = Counter(), 0, 'complete', time.time()
    with tokctx(args) as tok:
        token = {'name': tok.name, 'acquired_at': tok.acquired_at, 'waited_s': tok.waited_s}
        F.log('m2 run %s start: %d jobs, token %s waited %.1f s' % (name, len(jobs), tok.name, tok.waited_s))
        for j in jobs:
            if F.STOP or F.STOPFILE.exists():
                end_reason = 'stop'
                break
            if time.monotonic() >= mono or time.time() >= F.RUN_WALL_DEADLINE - F.SHUTDOWN_RESERVE:
                end_reason = 'chunk/run deadline'
                break
            if n % 100 == 0 and (F.free_bytes() < F.INFLIGHT_FLOOR or F.usage()['maxrss_bytes'] > F.RSS_STOP_BYTES):
                end_reason = 'in-flight floor or rss stop'
                break
            if j.get('rec_sha') is None:
                r = OrderedDict([('i', j['i']), ('kind', j['kind']), ('path', j['path']), ('status', 'UNRESOLVED'),
                                 ('reason', 'unreadable at pin')])
            else:
                try:
                    r = evaluate(libs, inp, j)
                except Exception as ex:  # recorded, never a PASS
                    r = OrderedDict([('i', j['i']), ('kind', j['kind']), ('path', j['path']), ('status', 'UNRESOLVED'),
                                     ('reason', 'driver exception %r' % (ex,))])
            gz.write((F.jline(r) + '\n').encode())
            st['%s|%s' % (j['kind'], r['status'])] += 1
            n += 1
            if n % 200 == 0:
                gz.flush()
                raw.flush()
                os.fsync(raw.fileno())
            if time.time() - last_ck > 1500:
                F.log('m2 run %s checkpoint: %d evaluated, %s' % (name, n, dict(st)))
                last_ck = time.time()
        gz.close()
        raw.flush()
        os.fsync(raw.fileno())
        raw.close()
    res = OrderedDict([('name', name), ('pins_sha256', args['--pins']), ('started', started), ('finished', F.now()),
                       ('end_reason', end_reason), ('token', token), ('jobs', len(jobs)), ('evaluated', n),
                       ('by_kind_status', dict(st)), ('progress_file', {'path': out_p.name, 'sha256': F.sha_file(out_p)[0]}),
                       ('driver_sha256', F.sha_file(Path(__file__).resolve())[0]), ('fb_v1_sha256', FB_V1_SHA),
                       ('resources', {**F.usage(), 'elapsed_s': round(time.time() - t0, 2), 'free_bytes_end': F.free_bytes()}),
                       ('proc', F.proc_info())])
    F.dump_x(F.HERE / ('m2-run-%s.json' % name), res)
    F.log('m2 run %s %s: %d/%d evaluated, %s; maxrss %d; elapsed %.0f s; m2-run-%s.json sha %s' % (
        name, end_reason, n, len(jobs), dict(st), res['resources']['maxrss_bytes'], res['resources']['elapsed_s'], name,
        F.sha_file(F.HERE / ('m2-run-%s.json' % name))[0]))
    print(json.dumps({k: res[k] for k in ('end_reason', 'evaluated', 'by_kind_status', 'resources')}, indent=1))


def cmd_controls(args):
    pins, jobs = load_m2_pins(args['--pins'])
    libs = load_libs()
    inp = Inputs(pins)
    out = []
    started = F.now()
    with tokctx(args) as tok:
        token = {'name': tok.name, 'acquired_at': tok.acquired_at, 'waited_s': tok.waited_s}
        d1 = next(j for j in jobs if j['kind'] == 'm2direct' and j.get('rec_sha') and j['path'].endswith('ms01_b00010.json'))
        d9 = next(j for j in jobs if j['kind'] == 'm2direct' and j.get('rec_sha') and j.get('strict_predicate_reasons') == []
                  and not j['path'].startswith('cycle2/m2skel_drat/ms01'))
        e0 = next(j for j in jobs if j['kind'] == 'e0b' and j['path'].endswith('g000.json'))
        nb = next(j for j in jobs if j['kind'] == 'm2direct' and j['path'].endswith('ms01_b00011.json'))
        other = json.loads((L / nb['path']).read_bytes())['cnf_sha256']
        g1 = inp.graph6()[1]

        def mut_sha(r, w=other):
            r['cnf_sha256'] = w
            return r

        def mut_enc(r):
            r['encoder'] = 'encode_skel_b.build'
            return r
        sk9 = inp.skel(9)
        spec_cases = [
            ('M2B_direct_ms01', d1, {}, ['PASS'], []),
            ('M2B_direct_other_ms', d9, {}, ['PASS'], []),
            ('M2B_e0b_g000', e0, {}, ['PASS'], []),
            ('M2C1_wrong_b_index', d1, {'mi_bi': (1, 11)}, ['MISMATCH'], ['cnf_sha256_equal']),
            ('M2C2_wrong_b_list', d1, {'skel': sk9, 'mi_bi': (1, 10)}, ['MISMATCH', 'UNRESOLVED'],
             ['cnf_sha256_equal', 'rebuild_possible']),
            ('M2C3_wrong_special', d1, {'special': []}, ['MISMATCH', 'UNRESOLVED'], ['cnf_sha256_equal', 'rebuild_possible']),
            ('M2C4_wellformed_wrong_sha', d1, {'rec': mut_sha}, ['MISMATCH'], ['cnf_sha256_equal']),
            ('M2C5_declared_encoder_v1', d1, {'rec': mut_enc}, ['FAIL_STRUCTURAL'], ['declared_encoder_build_v2']),
            ('E0BC1_graph_swap', e0, {'graph6': g1}, ['MISMATCH'], ['cnf_sha256_equal']),
            ('E0BC2_wellformed_wrong_sha', e0, {'rec': lambda r, w=other: dict(r, cnf_sha256=w)}, ['MISMATCH'], ['cnf_sha256_equal']),
        ]
        for cid, job, ov, want, why in spec_cases:
            try:
                r = evaluate(libs, inp, job, ov)
            except Exception as ex:
                r = {'status': 'EXCEPTION', 'reason': repr(ex)}
            got = r.get('checks_false') or ([r['reason']] if r.get('reason') else [])
            anyof = cid in ('M2C2_wrong_b_list', 'M2C3_wrong_special')  # wrong input: hash mismatch OR encoder refusal
            ok = r.get('status') in want and ((any(w in got for w in why)) if anyof else all(w in got for w in why))
            out.append(OrderedDict([('id', cid), ('target', job['path']), ('overlay', sorted(ov)), ('expected_status', want),
                                    ('expected_reasons', why), ('status', r.get('status')), ('reasons', got),
                                    ('gen', r.get('gen')), ('as_expected', ok)]))
    res = OrderedDict([('title', 'PA19 M2 direct / E0-B binding controls (in-memory overlays; no lane file modified)'),
                       ('started', started), ('finished', F.now()), ('pins_sha256', args['--pins']), ('token', token),
                       ('controls', out), ('all_as_expected', all(c['as_expected'] for c in out)),
                       ('driver_sha256', F.sha_file(Path(__file__).resolve())[0]), ('resources', F.usage())])
    F.dump_x(F.HERE / 'm2-controls-v2.json', res)
    F.log('m2 controls (v2): %d/%d as expected; m2-controls-v2.json sha %s' % (
        sum(c['as_expected'] for c in out), len(out), F.sha_file(F.HERE / 'm2-controls-v2.json')[0]))
    print(json.dumps({'all_as_expected': res['all_as_expected'], 'unexpected': [c for c in out if not c['as_expected']]}, indent=1))


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cmd = sys.argv[1]
    args = F.parse_args(sys.argv[2:])
    F.require_env(args)
    os.chdir(F.HERE)
    fn = {'pin': cmd_pin, 'run': cmd_run, 'controls': cmd_controls}.get(cmd)
    if fn is None:
        raise SystemExit(__doc__)
    fn(args)


if __name__ == '__main__':
    main()
