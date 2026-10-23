#!/usr/bin/env python3
"""PA(19,8,6) R8 parent replay: bind split and rerun CNF records to exact (spec, placement list,
indices) inputs. Formula binding only. No solver, proof checker, CNF file or proof file is run,
read or written; a PASS here never certifies UNSAT, and PA(19,8,6) stays undecided.

Run from this directory with /opt/homebrew/opt/python@3.14/bin/python3.14 -B -I, one process at
a time, under nice. Subcommands:
  pin       pin sources/specs/ext lists/maps (live L vs snapshot S vs R0/R5/R6 pins); copy the
            exact replay sources into pinned-src/ (mode x); snapshot every split record (bytes
            SHA-256) and run the structural checks on all of them -> pins.json, population.jsonl
  sample    freeze the seeded stratified selection (seed 20261017; uses only population paths,
            filename indices and mtimes) -> sample-manifest.json (+ .sha256). Nothing is
            regenerated before this file exists.
  run       regenerate each selected formula in memory with the declared encoder, hash, compare,
            discard the bytes -> runs/run-NNN/progress.jsonl (append-only)
  finalize  freeze check, late-record listing, aggregation -> subcase-binding-result.json
"""
import hashlib
import json
import os
import random
import re
import resource
import signal
import subprocess
import sys
import time
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
REPO = HERE.parents[4]
LANE_REL = 'information-science/evidence/six-lane-20261016/packing-array19'
L = REPO / LANE_REL
COVER = REVIEW / 'pa19-parent-cover-replay-v1'
S = COVER / 'inputs'
R0 = COVER / 'pin-result.json'
R5 = REVIEW / 'pa19-cnf-binding-v1' / 'cnf-binding-result.json'
R6 = REVIEW / 'pa19-placement-binding-v1' / 'placement-binding-result.json'
R6PIN = REVIEW / 'pa19-placement-binding-v1' / 'pin-v1.json'
AUDITS = (REVIEW / 'pa19-cover-scout-audit-v1.md', REVIEW / 'pa19-encoder-scout-audit-v1.md')
PINNED = HERE / 'pinned-src'
PINS = HERE / 'pins.json'
POP = HERE / 'population.jsonl'
MANIFEST = HERE / 'sample-manifest.json'
MANIFEST_SHA = HERE / 'sample-manifest.sha256'
RUNS = HERE / 'runs'
RESULT = HERE / 'subcase-binding-result.json'
README = HERE / 'README.md'
STOPFILE = HERE / 'STOP'
SEED = 20261017
FREE_FLOOR = 12_000_000_000
RSS_STOP = int(2.5 * 1024 ** 3)  # cooperative stop well below the 3 GiB cap
NEWDATA_CAP = 500 * 1024 ** 2
TOPUP = 40
REPLAY_SOURCES = ('encode_e1.py', 'encode_skel.py', 'encode_full.py', 'encode_full2.py', 'encode_partq.py',
                  'encode_partbatch.py', 'encode_skel_b.py', 'stream_check4.py', 'stream_check5.py')
FAMILY_DIRS = (('a3', 'cycle2/a3'), ('part', 'cycle2/part'), ('m2part_drat', 'cycle2/m2part_drat'))
OTHER_SPLIT_TREES = ('cycle2/m2part', 'cycle2/m2part_strict')
NONRECORD = ('ext.json', 'summary.json', 'summary_batched.json')
SHARED_DATA = ('cases19skel/index.json', 'cycle2/skel-b/skeletons-b-ms01.json', 'cycle2/skel-b/skeletons-b-ms09.json',
               'cycle2/skel-b/compare-map-ms01.json', 'cycle2/skel-b/compare-map-ms09.json', 'cycle2/m2-jobs-part.txt',
               'cycle2/hard-tags-ms01.txt', 'cycle2/tags-ms09.txt', 'cycle2/hard-tags-ms06-ms09.txt',
               'data/profiles-19-8-6.json')
SINGLE = re.compile(r'^f(\d{5})(?:_([A-Za-z0-9]+))?\.json$')
BATCH = re.compile(r'^batch_(\d{5})_(\d{5})(?:_([A-Za-z0-9]+))?\.json$')
M1TAG = re.compile(r'^ms0([1-9])_s(\d{5})$')
M2DIR = re.compile(r'^ms0([1-9])_b(\d{5})$')
BASE = [4, 3, 3, 3, 3, 3]
STRATA = (('A3', 'a3', 'single', 1), ("A3'", 'part', 'single', 2), ("A3''", 'part', 'batch', 1),
          ('M2', 'm2part_drat', 'batch', None))  # None = census of the stratum at the snapshot
STOP = []


# ----------------------------------------------------------------------------- helpers
def sha(b):
    return hashlib.sha256(b).hexdigest()


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def host_date():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True,
                          check=True).stdout.strip()


def free_bytes():
    st = os.statvfs(HERE)
    return st.f_bavail * st.f_frsize


def usage():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return {'cpu_user_s': round(r.ru_utime, 2), 'cpu_sys_s': round(r.ru_stime, 2), 'maxrss_bytes': r.ru_maxrss}


def write_new(path, data):
    with open(path, 'xb') as f:
        f.write(data)
    return len(data)


def dump_new(path, obj):
    return write_new(path, (json.dumps(obj, indent=1, sort_keys=False) + '\n').encode())


def readme(msg):
    with open(README, 'a') as f:
        f.write('- %s %s\n' % (host_date(), msg))


def driver_sha():
    return sha(Path(__file__).resolve().read_bytes())


def proc_info():
    return {'orig_argv': getattr(sys, 'orig_argv', sys.argv), 'executable': sys.executable, 'version': sys.version,
            'flags': {'dont_write_bytecode': sys.flags.dont_write_bytecode, 'isolated': sys.flags.isolated},
            'cwd': os.getcwd(), 'pid': os.getpid(), 'nice': os.getpriority(os.PRIO_PROCESS, 0),
            'driver_sha256': driver_sha()}


def require_flags():
    if not (sys.flags.dont_write_bytecode and sys.flags.isolated):
        raise SystemExit('run with python3 -B -I')


def file_info(p, keep=False):
    try:
        st = p.stat()
        b = p.read_bytes()
    except FileNotFoundError:
        return ({'exists': False}, None) if keep else {'exists': False}
    d = {'exists': True, 'size': len(b), 'mtime_ns': st.st_mtime_ns,
         'mtime': time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime(st.st_mtime)), 'sha256': sha(b)}
    return (d, b) if keep else d


def read_record(p):
    """Read once; a record that is being written by the live runner is retried (bounded)."""
    data = None
    for _ in range(6):
        try:
            data = p.read_bytes()
        except FileNotFoundError:
            return None, None, 'missing'
        try:
            return data, json.loads(data), None
        except ValueError:
            time.sleep(2)
    return data, None, 'unparseable'


def sha_lines(text):
    out = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) == 2 and re.fullmatch(r'[0-9a-f]{64}', parts[0]):
            out[parts[1]] = parts[0]
    return out


def jdigest(obj):
    return sha(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode())


def on_term(signum, _frame):
    STOP.append('signal %d' % signum)


# ----------------------------------------------------------------------------- record rules
def parse_name(fname):
    m = SINGLE.match(fname)
    if m:
        lo = int(m.group(1))
        return 'single', lo, lo, m.group(2) or ''
    m = BATCH.match(fname)
    if m:
        return 'batch', int(m.group(1)), int(m.group(2)), m.group(3) or ''
    return None


def allowed_encoders(fam, kind, suf):
    if fam == 'a3' and kind == 'single':
        if suf == '':
            return ('encode_full.py',)
        if suf == 'exact':
            return ('encode_full2.py',)
        if suf in ('r2', 'r3'):
            return ('encode_full.py',)
        return ('encode_full.py', 'encode_full2.py')
    if fam == 'part' and kind == 'single':
        return ('encode_partq.py',)
    if fam == 'part' and kind == 'batch':
        return ('encode_partbatch.py',)
    if fam == 'm2part_drat' and kind == 'batch':
        return ('encode_skel_b.build_partbatch',)
    if fam == 'm2part_drat' and kind == 'single':
        return ('encode_skel_b.build_part',)
    return ()


EXPECTED_RUNNER = {'exact': ('rerun_exact.py', 4), 'r2': ('rerun_unknown.py', 4), 'r3': ('rerun5.py', 5)}


def checker_class(r):
    """Worker-recorded checker route of a record (never an acceptance in this task)."""
    rev = r.get('stream_check_revision')
    if 'lratstrict_verified' in r or rev == 6:
        return 'lane_written_lratstrict'
    if rev == 8:
        return 'retired_rev8_verdict_parser'
    if r.get('drat_trim_verified') is True:
        if rev == 9 and (r.get('drat_trim') or {}).get('s_lines') != ['s VERIFIED']:
            return 'rev9_flag_without_exact_s_line'
        return 'standard_drat_trim'
    if r.get('lrat_verified') is True:
        return 'retired_lrat_check_only'
    return 'no_verified_flag'


def worker_claim(r):
    dt = r.get('drat_trim') or {}
    return {'status': r.get('status'), 'checked': r.get('checked'), 'checker_interrupted': r.get('checker_interrupted'),
            'drat_trim_verified': r.get('drat_trim_verified'), 'lrat_verified': r.get('lrat_verified'),
            'lratstrict_verified': r.get('lratstrict_verified'), 'stream_check_revision': r.get('stream_check_revision'),
            'solver_head': (r.get('solver') or '')[:60], 'drat_trim_rc': dt.get('rc'), 'drat_trim_s_lines': dt.get('s_lines')}


def structural(fam, dname, fname, rec, ext_n):
    """Cheap per-record checks against filename, directory and the pinned list size ext_n.
    Returns (checks, kind, suffix, indices or None)."""
    kind, lo, hi, suf = parse_name(fname)
    c = OrderedDict()
    idxs = None
    if fam in ('a3', 'part'):
        c['tag_field_equals_dir'] = rec.get('tag') == dname
        if kind == 'single':
            field = ('full_index' if fam == 'a3' else 'sub_index') if suf in ('', 'exact') else 'index'
            v = rec.get(field)
            c['filename_index_equals_' + field] = type(v) is int and v == lo
            if suf not in ('', 'exact'):
                c['kind_field_ok'] = rec.get('kind') == fam
            idxs = [lo] if c['filename_index_equals_' + field] else None
        else:
            ind = rec.get('indices')
            ok = (isinstance(ind, list) and len(ind) >= 1 and all(type(x) is int for x in ind)
                  and all(a < b for a, b in zip(ind, ind[1:])))
            c['m1_indices_explicit_increasing_list'] = ok
            c['filename_range_equals_first_last'] = bool(ok and ind[0] == lo and ind[-1] == hi)
            if suf:
                c['index_field_equals_stem'] = rec.get('index') == 'batch_%05d_%05d' % (lo, hi)
                c['kind_field_ok'] = rec.get('kind') == 'partbatch'
            idxs = ind if ok else None
    else:
        m = M2DIR.match(dname)
        c['multiset_field_equals_dir'] = bool(m) and rec.get('multiset') == int(m.group(1))
        c['b_index_field_equals_dir'] = bool(m) and rec.get('b_index') == int(m.group(2))
        if kind == 'batch':
            ind = rec.get('indices')
            ok = isinstance(ind, list) and len(ind) == 2 and all(type(x) is int for x in ind) and ind[0] <= ind[1]
            c['m2_indices_lo_hi_pair'] = ok
            c['filename_range_equals_lo_hi'] = bool(ok and ind == [lo, hi])
            idxs = list(range(ind[0], ind[1] + 1)) if ok else None
        else:
            v = rec.get('sub_index')
            c['filename_index_equals_sub_index'] = type(v) is int and v == lo
            idxs = [lo] if c['filename_index_equals_sub_index'] else None
    if ext_n is None:
        c['indices_within_pinned_list'] = None
    else:
        c['indices_within_pinned_list'] = idxs is not None and all(0 <= i < ext_n for i in idxs)
    c['declared_encoder_expected'] = rec.get('encoder') in allowed_encoders(fam, kind, suf)
    if suf in EXPECTED_RUNNER:
        run, rev = EXPECTED_RUNNER[suf]
        c['rerun_runner_and_revision_expected'] = rec.get('runner') == run and rec.get('stream_check_revision') == rev
    return c, kind, suf, idxs


def struct_ok(c):
    return all(v is not False for v in c.values()) and c.get('indices_within_pinned_list') is True


# ----------------------------------------------------------------------------- reference data
def load_refs():
    r0 = json.loads(R0.read_bytes())['files']
    r5 = json.loads(R5.read_bytes())
    r6 = json.loads(R6.read_bytes())
    r6pin = json.loads(R6PIN.read_bytes())
    cases = OrderedDict((c['tag'], c) for c in r6['cases'])
    return r0, r5, r6, r6pin, cases


def m2_dir_name(case):
    return 'ms%02d_b%05d' % (case['multiset'], case['b_index'])


def case_dirs(cases):
    a3 = sorted(t for t in cases if t.startswith('ms01_'))
    part = sorted(t for t in cases if t.startswith('ms09_'))
    m2 = {m2_dir_name(c): t for t, c in cases.items()}
    return a3, part, m2


# ----------------------------------------------------------------------------- pin
def cmd_pin():
    require_flags()
    t0 = time.time()
    started = now()
    readme('pin start (driver %s)' % driver_sha())
    r0, r5, r6, r6pin, cases = load_refs()
    a3_tags, part_tags, m2_dirs = case_dirs(cases)
    wman = sha_lines((L / 'cycle2' / 'MANIFEST-cycle2-20261017T121839.sha256').read_text())
    delta_p = L / 'cycle2' / 'src-delta-vs-parent-inputs-20261017T133454.txt'
    delta = sha_lines(delta_p.read_text())
    pins = OrderedDict()
    pins['recorded_at'] = started
    pins['driver'] = proc_info()
    pins['paths'] = {'L': LANE_REL, 'S': str(S.relative_to(REPO)), 'here': str(HERE.relative_to(REPO))}
    pins['reference_receipts'] = OrderedDict(
        (k, {'path': str(p.relative_to(REPO)), 'sha256': sha(p.read_bytes())})
        for k, p in (('R0_pin_result', R0), ('R5_cnf_binding', R5), ('R6_placement_binding', R6), ('R6_pin', R6PIN),
                     ('cover_audit_R8', AUDITS[0]), ('encoder_audit', AUDITS[1])))
    pins['reference_receipts']['R5_verdict'] = r5.get('verdict')
    pins['reference_receipts']['R6_summary'] = {k: r6['result_summary'].get(k) for k in (
        'status_counts', 'all_cases_all_checks_true', 'm1_m2_raw_and_orbit_counts_equal_all', 'a_to_b_isomorphism_explicit_all')}
    pins['worker_manifests'] = {
        'cycle2_manifest_1218': {'path': 'cycle2/MANIFEST-cycle2-20261017T121839.sha256',
                                 **file_info(L / 'cycle2' / 'MANIFEST-cycle2-20261017T121839.sha256')},
        'src_delta_1334': {'path': str(delta_p.relative_to(L)), **file_info(delta_p)},
        'note': 'worker-recorded hashes; used only as time-stamped cross-references'}

    # sources: every live and snapshot src file
    r5_src = {n: v.get('live_sha256') for n, v in r5['pins']['sources'].items()}
    r5_ser = {n: v.get('sha256') for n, v in r5['pins']['serializer_variants'].items()}
    live = {p.name: p for p in (L / 'src').iterdir() if p.is_file()}
    snap = {p.name: p for p in (S / 'src').iterdir() if p.is_file()}
    src = OrderedDict()
    for n in sorted(set(live) | set(snap)):
        li = file_info(live[n]) if n in live else {'exists': False}
        si = file_info(snap[n]) if n in snap else {'exists': False}
        e = OrderedDict([('L', li), ('S', si),
                         ('R0_pin', r0.get('src/' + n)),
                         ('R5_pin', r5_src.get(n) or r5_ser.get(n)),
                         ('R6_pin_L', ((r6pin.get('sources') or {}).get(n) or {}).get('L', {}).get('sha256')),
                         ('worker_manifest_1218', wman.get('src/' + n)),
                         ('worker_src_delta_1334', delta.get('src/' + n))])
        ls = li.get('sha256')
        e['L_equals_S'] = (ls == si.get('sha256')) if (li['exists'] and si['exists']) else None
        e['deltas_vs_L'] = sorted(k for k in ('R0_pin', 'R5_pin', 'R6_pin_L', 'worker_manifest_1218', 'worker_src_delta_1334')
                                  if e[k] is not None and e[k] != ls)
        src[n] = e
    pins['sources'] = src
    pins['sources_summary'] = {
        'live_files': len(live), 'snapshot_files': len(snap),
        'live_only': sorted(set(live) - set(snap)), 'snapshot_only': sorted(set(snap) - set(live)),
        'changed_vs_S': sorted(n for n, e in src.items() if e['L_equals_S'] is False),
        'any_delta_vs_reference_pins': sorted(n for n, e in src.items() if e['deltas_vs_L'])}

    # replay sources: exact bytes copied into pinned-src/ (S bytes when S has the file, else live bytes)
    PINNED.mkdir(exist_ok=False)
    rep = OrderedDict()
    for n in REPLAY_SOURCES:
        e = src[n]
        origin = 'S' if e['S']['exists'] else 'L'
        b = ((S if origin == 'S' else L) / 'src' / n).read_bytes()
        write_new(PINNED / n, b)
        os.chmod(PINNED / n, 0o444)
        rep[n] = {'origin': origin, 'sha256': sha(b), 'size': len(b),
                  'pinned_copy_sha256': sha((PINNED / n).read_bytes()),
                  'L_sha256': e['L'].get('sha256'), 'L_mtime': e['L'].get('mtime'),
                  'equals_L': sha(b) == e['L'].get('sha256'),
                  'equals_R0_pin': (sha(b) == e['R0_pin']) if e['R0_pin'] else None,
                  'equals_R5_pin': (sha(b) == e['R5_pin']) if e['R5_pin'] else None,
                  'equals_R6_pin_L': (sha(b) == e['R6_pin_L']) if e['R6_pin_L'] else None,
                  'equals_worker_manifest_1218': (sha(b) == e['worker_manifest_1218']) if e['worker_manifest_1218'] else None,
                  'equals_worker_src_delta_1334': (sha(b) == e['worker_src_delta_1334']) if e['worker_src_delta_1334'] else None}
    pins['replay_sources'] = rep

    # shared data
    data = OrderedDict()
    for rel in SHARED_DATA:
        li = file_info(L / rel)
        si = file_info(S / rel)
        data[rel] = {'L': li, 'S': si, 'R0_pin': r0.get(rel),
                     'L_equals_S': li.get('sha256') == si.get('sha256') if li['exists'] and si['exists'] else None,
                     'S_equals_R0_pin': si.get('sha256') == r0.get(rel) if si['exists'] else None}
    pins['shared_data'] = data
    jobs = set((S / 'cycle2' / 'm2-jobs-part.txt').read_text().split())
    maps = {mi: json.loads((S / 'cycle2' / 'skel-b' / ('compare-map-ms%02d.json' % mi)).read_bytes())['a_to_b']
            for mi in (1, 9)}

    # per case: spec, M1 ext, M2 ext, A->B binding
    pc = OrderedDict()
    ext_n = {}
    for tag, c in cases.items():
        mi, si_ = int(tag[3]), int(tag[6:])
        fam = 'a3' if mi == 1 else 'part'
        spec_rel = 'cases19skel/specs/%s.json' % tag
        sl, slb = file_info(L / spec_rel, keep=True)
        ss = file_info(S / spec_rel)
        spec = json.loads(slb) if slb is not None else {}
        e = OrderedDict()
        e['multiset'], e['skel_index'], e['b_index'] = c['multiset'], c['skel_index'], c['b_index']
        e['spec'] = {'path': spec_rel, 'L': sl, 'S_sha256': ss.get('sha256'), 'R0_pin': r0.get(spec_rel),
                     'R6_spec_S': c['shas']['spec_S']}
        e['spec']['bound'] = (sl.get('sha256') is not None and sl.get('sha256') == ss.get('sha256') == r0.get(spec_rel)
                              == c['shas']['spec_S'])
        e['spec']['identity_ok'] = (spec.get('multiset_index') == mi and spec.get('skel_index') == si_
                                    and c['multiset'] == mi and c['skel_index'] == si_)
        m1_rel = 'cycle2/%s/%s/ext.json' % (fam, tag)
        ml, mlb = file_info(L / m1_rel, keep=True)
        ms_ = file_info(S / m1_rel)
        ref1 = c['shas']['m1_regen']
        e['m1_ext'] = {'path': m1_rel, 'L': ml, 'S_sha256': ms_.get('sha256'), 'R0_pin': r0.get(m1_rel),
                       'R6_m1_regen': ref1, 'R6_m1_stored': c['shas'].get('m1_stored')}
        ok1 = ml.get('sha256') is not None and ml.get('sha256') == ref1
        if ms_['exists']:
            ok1 = ok1 and ms_.get('sha256') == ml.get('sha256') == r0.get(m1_rel)
        n1 = None
        if mlb is not None:
            try:
                E = json.loads(mlb)
                n1 = len(E['full'])
                e['m1_ext']['fields_ok'] = (E.get('source') == tag + '.json' and E.get('num_full') == n1
                                            and n1 == c['counts']['m1_num_full'])
            except (ValueError, KeyError, TypeError) as ex:
                e['m1_ext']['parse_error'] = repr(ex)
                ok1 = False
        e['m1_ext']['bound'] = bool(ok1 and e['m1_ext'].get('fields_ok'))
        e['m1_ext']['n'] = n1
        if e['m1_ext']['bound']:
            ext_n[(fam, tag)] = n1
        d2 = m2_dir_name(c)
        m2_rel = 'cycle2/m2part_drat/%s/ext.json' % d2
        m2l, m2lb = file_info(L / m2_rel, keep=True)
        ref2 = c['shas']['m2_regen_normalized_production_source']
        e['m2_dir'] = d2
        e['m2_ext'] = {'path': m2_rel, 'L': m2l, 'R6_m2_regen_normalized_production_source': ref2,
                       'R6_m2_stored': c['shas'].get('m2_stored')}
        n2 = None
        ok2 = m2l.get('sha256') is not None and m2l.get('sha256') == ref2
        if m2lb is not None:
            try:
                E2 = json.loads(m2lb)
                n2 = len(E2['placements'])
                e['m2_ext']['fields_ok'] = (E2.get('index') == c['b_index'] and E2.get('num_placements') == n2
                                            and n2 == c['counts']['m2_num']
                                            and E2.get('source') == str(L / 'cycle2' / 'skel-b' / ('skeletons-b-ms%02d.json' % mi)))
                e['m2_ext']['source_field'] = E2.get('source')
            except (ValueError, KeyError, TypeError) as ex:
                e['m2_ext']['parse_error'] = repr(ex)
                ok2 = False
        e['m2_ext']['bound'] = bool(ok2 and e['m2_ext'].get('fields_ok'))
        e['m2_ext']['n'] = n2
        if e['m2_ext']['bound']:
            ext_n[('m2part_drat', d2)] = n2
        e['a_to_b'] = {'compare_map_S_value': maps[mi][si_], 'equals_R6_b_index': maps[mi][si_] == c['b_index'],
                       'in_m2_jobs_part': '%d:%d' % (mi, c['b_index']) in jobs,
                       'R6_case_status': c['status'], 'R6_iso_count': c.get('isomorphisms_a_to_b')}
        pc[tag] = e
    pins['cases'] = pc
    pins['cases_summary'] = {
        'cases': len(pc), 'spec_bound': sum(e['spec']['bound'] for e in pc.values()),
        'spec_identity_ok': sum(e['spec']['identity_ok'] for e in pc.values()),
        'm1_ext_bound': sum(e['m1_ext']['bound'] for e in pc.values()),
        'm2_ext_present': sum(e['m2_ext']['L']['exists'] for e in pc.values()),
        'm2_ext_bound': sum(e['m2_ext']['bound'] for e in pc.values()),
        'a_to_b_ok': sum(e['a_to_b']['equals_R6_b_index'] and e['a_to_b']['in_m2_jobs_part'] for e in pc.values())}

    # population snapshot
    pop_lines = []
    nonrec = []
    unknown_dirs = []
    other_trees = {t: (L / t).exists() for t in OTHER_SPLIT_TREES}
    snap_at = now()
    for fam, rel in FAMILY_DIRS:
        base = L / rel
        known = set(a3_tags) if fam == 'a3' else set(part_tags) if fam == 'part' else set(m2_dirs)
        for d in sorted(os.listdir(base)):
            dp = base / d
            if not dp.is_dir():
                nonrec.append({'path': '%s/%s' % (rel, d), 'kind': 'family_level_file', **file_info(dp)})
                continue
            if d not in known:
                unknown_dirs.append('%s/%s' % (rel, d))
            case = d if fam != 'm2part_drat' else m2_dirs.get(d)
            for fn in sorted(os.listdir(dp)):
                p = dp / fn
                prel = '%s/%s/%s' % (rel, d, fn)
                if fn in NONRECORD or parse_name(fn) is None:
                    nonrec.append({'path': prel, 'kind': fn if fn in NONRECORD else 'other', **file_info(p)})
                    continue
                try:
                    st = p.stat()
                except FileNotFoundError:
                    nonrec.append({'path': prel, 'kind': 'vanished_during_listing', 'exists': False})
                    continue
                data_, rec, err = read_record(p)
                kind, lo, hi, suf = parse_name(fn)
                e = OrderedDict([('path', prel), ('family', fam), ('dir', d), ('case', case), ('kind', kind),
                                 ('suffix', suf), ('name_lo', lo), ('name_hi', hi), ('size', len(data_ or b'')),
                                 ('mtime_ns', st.st_mtime_ns), ('sha256', sha(data_) if data_ is not None else None),
                                 ('parse', err or 'ok')])
                if rec is not None:
                    c, kind, suf, idxs = structural(fam, d, fn, rec, ext_n.get((fam, d)))
                    e['declared'] = {'encoder': rec.get('encoder'), 'runner': rec.get('runner'),
                                     'kind': rec.get('kind'), 'enumerator': rec.get('enumerator')}
                    if kind == 'batch' and fam in ('a3', 'part'):
                        ind = rec.get('indices') if isinstance(rec.get('indices'), list) else None
                        e['indices'] = {'count': len(ind) if ind else None,
                                        'contiguous': bool(ind) and ind == list(range(ind[0], ind[0] + len(ind))),
                                        'digest': jdigest(ind)}
                    elif kind == 'batch':
                        e['indices'] = {'lo_hi': rec.get('indices')}
                    e['cnf_sha256'] = rec.get('cnf_sha256')
                    e['cnf_bytes'] = rec.get('cnf_bytes')
                    e['leave'] = rec.get('leave')
                    e['claim'] = worker_claim(rec)
                    e['checker_class'] = checker_class(rec)
                    e['struct'] = c
                    e['struct_ok'] = struct_ok(c)
                pop_lines.append(json.dumps(e, separators=(',', ':')))
    pop_bytes = ('\n'.join(pop_lines) + '\n').encode()
    write_new(POP, pop_bytes)
    os.chmod(POP, 0o444)
    pops = [json.loads(x) for x in pop_lines]
    cnt = Counter((e['family'], e['kind'], e['suffix']) for e in pops)
    pins['population'] = {
        'path': POP.name, 'sha256': sha(pop_bytes), 'bytes': len(pop_bytes), 'snapshot_started': snap_at,
        'snapshot_ended': now(), 'records': len(pops),
        'by_family_kind_suffix': {'%s/%s/%s' % k: v for k, v in sorted(cnt.items())},
        'by_checker_class': dict(Counter('%s/%s' % (e['family'], e.get('checker_class')) for e in pops)),
        'unparseable_or_missing': [e['path'] for e in pops if e['parse'] != 'ok'],
        'structural_failures': [{'path': e['path'], 'failed': [k for k, v in e['struct'].items() if v is False]}
                                for e in pops if e['parse'] == 'ok' and any(v is False for v in e['struct'].values())],
        'structural_unevaluated_range': [e['path'] for e in pops if e['parse'] == 'ok'
                                         and e['struct'].get('indices_within_pinned_list') is None],
        'struct_ok_records': sum(1 for e in pops if e.get('struct_ok')),
        'nonrecord_files': nonrec, 'unknown_dirs': unknown_dirs, 'other_split_trees_exist': other_trees}
    pins['resources'] = {**usage(), 'elapsed_s': round(time.time() - t0, 2), 'free_bytes': free_bytes()}
    pins['finished'] = now()
    dump_new(PINS, pins)
    os.chmod(PINS, 0o444)
    readme('pin done: %d records (%s), struct_ok %d, structural failures %d, unbound-range %d; pins.json sha %s' % (
        len(pops), ', '.join('%s=%d' % ('/'.join(k), v) for k, v in sorted(cnt.items())),
        pins['population']['struct_ok_records'], len(pins['population']['structural_failures']),
        len(pins['population']['structural_unevaluated_range']), sha(PINS.read_bytes())))
    print(json.dumps({'records': len(pops), 'cases_summary': pins['cases_summary'],
                      'sources_summary': pins['sources_summary'],
                      'replay_sources': {n: {k: v for k, v in e.items() if k.startswith('equals') or k == 'origin'}
                                         for n, e in rep.items()},
                      'structural_failures': len(pins['population']['structural_failures']),
                      'unbound_range': len(pins['population']['structural_unevaluated_range']),
                      'unknown_dirs': unknown_dirs, 'other_trees': other_trees,
                      'resources': pins['resources']}, indent=1))


# ----------------------------------------------------------------------------- sample
def load_pins_pop():
    pins_b = PINS.read_bytes()
    pins = json.loads(pins_b)
    pop_b = POP.read_bytes()
    if sha(pop_b) != pins['population']['sha256']:
        raise SystemExit('population.jsonl differs from pins.json')
    pop = [json.loads(x) for x in pop_b.decode().splitlines() if x]
    return pins, sha(pins_b), pop


def cmd_sample():
    require_flags()
    if MANIFEST.exists() or MANIFEST_SHA.exists():
        raise SystemExit('sample manifest already frozen')
    pins, pins_sha, pop = load_pins_pop()
    byp = {e['path']: e for e in pop}
    rng = random.Random(SEED)
    items = OrderedDict()

    def add(path, role):
        if path not in items:
            items[path] = {'path': path, 'roles': []}
        items[path]['roles'].append(role)

    parsed = [e for e in pop if e['parse'] == 'ok']
    reruns = sorted((e for e in parsed if e['suffix']), key=lambda e: e['path'])
    for e in reruns:
        add(e['path'], 'rerun:' + e['suffix'])
    missing_originals = []
    for e in reruns:
        stem = ('f%05d.json' % e['name_lo']) if e['kind'] == 'single' else ('batch_%05d_%05d.json' % (e['name_lo'], e['name_hi']))
        op = e['path'].rsplit('/', 1)[0] + '/' + stem
        if op in byp and byp[op]['parse'] == 'ok':
            add(op, 'rerun_original_of:' + e['path'])
        else:
            missing_originals.append({'rerun': e['path'], 'original': op})
    ordinary = [e for e in parsed if not e['suffix']]
    strata_info = OrderedDict()
    for name, fam, kind, k in STRATA:
        recs = [e for e in ordinary if e['family'] == fam and e['kind'] == kind]
        by_dir = defaultdict(list)
        for e in recs:
            by_dir[e['dir']].append(e)
        sel_before = sum(1 for it in items.values() if any(r.startswith('sample:%s:' % name) for r in it['roles']))
        for d in sorted(by_dir):
            rs = sorted(by_dir[d], key=lambda e: (e['name_lo'], e['name_hi'], e['path']))
            add(rs[0]['path'], 'sample:%s:index_first' % name)
            if len(rs) > 1:
                add(rs[-1]['path'], 'sample:%s:index_last' % name)
            interior = rs[1:-1]
            if k is None:
                for e in interior:
                    add(e['path'], 'sample:%s:census' % name)
            else:
                for e in rng.sample(interior, min(k, len(interior))):
                    add(e['path'], 'sample:%s:random_interior' % name)
        if recs:
            rs = sorted(recs, key=lambda e: (e['mtime_ns'], e['path']))
            add(rs[0]['path'], 'sample:%s:mtime_first' % name)
            add(rs[-1]['path'], 'sample:%s:mtime_last' % name)
        strata_info[name] = {'family': fam, 'kind': kind, 'dirs': len(by_dir), 'population': len(recs),
                             'per_dir_rule': 'index_first + index_last + %s' % (
                                 'all interior (census)' if k is None else '%d seeded random interior' % k),
                             'selected_with_this_stratum_role': sum(
                                 1 for it in items.values() if any(r.startswith('sample:%s:' % name) for r in it['roles'])) - sel_before}
    rest = sorted(e['path'] for e in ordinary if e['family'] in ('a3', 'part') and e['path'] not in items)
    for p in rng.sample(rest, min(TOPUP, len(rest))):
        add(p, 'sample:M1:uniform_topup')
    order = list(items)
    sample_ordinary = [p for p in order if any(r.startswith('sample:') for r in items[p]['roles'])]
    # deterministic mutation controls (expected outcome: generated hash differs from the target record)

    def first_role(name, pred=lambda e: True):
        for p in order:
            if any(r.startswith('sample:%s:' % name) for r in items[p]['roles']) and pred(byp[p]):
                return p
        return None
    noncontig = sorted(e['path'] for e in ordinary if e['family'] == 'part' and e['kind'] == 'batch'
                       and not e['indices']['contiguous'])
    controls = [
        {'id': 'C1_a3_neighbor_placement', 'target': first_role('A3'), 'mutation': 'placement index +1 (or -1 at the end)',
         'expect': 'generated cnf_sha256 differs from the target record'},
        {'id': 'C2_partq_neighbor_placement', 'target': first_role("A3'"), 'mutation': 'placement index +1 (or -1 at the end)',
         'expect': 'generated cnf_sha256 differs from the target record'},
        {'id': 'C3_exact_record_built_with_encode_full',
         'target': next((p for p in order if p.endswith('ms01_s02573/f00012_exact.json')), None),
         'mutation': 'encode_full.build instead of the declared encode_full2.build',
         'expect': 'differs from the _exact record; equals the recorded cnf_sha256 of the original f-record'},
        {'id': 'C4_m1_batch_drop_last_index', 'target': first_role("A3''", lambda e: (e['indices']['count'] or 0) >= 2),
         'mutation': 'explicit index list without its last element', 'expect': 'differs from the target record'},
        {'id': 'C5_m1_batch_read_as_lo_hi_range', 'target': noncontig[0] if noncontig else None,
         'mutation': 'non-contiguous M1 explicit list replaced by range(first, last+1) (M2 semantics)',
         'expect': 'differs from the target record', 'population_noncontiguous_m1_batches': len(noncontig)},
        {'id': 'C6_m2_batch_drop_last_index', 'target': first_role('M2', lambda e: e['name_hi'] > e['name_lo']),
         'mutation': '[lo, hi-1] instead of [lo, hi]', 'expect': 'differs from the target record'},
    ]
    man = OrderedDict()
    man['created'] = now()
    man['seed'] = SEED
    man['driver_sha256'] = driver_sha()
    man['python'] = sys.version
    man['pins_sha256'] = pins_sha
    man['population_sha256'] = pins['population']['sha256']
    man['population_records'] = len(pop)
    man['frozen_before_any_regeneration'] = True
    man['algorithm'] = (
        'random.Random(%d). Items in evaluation order: (1) every record with a filename suffix (_r2/_r3/_exact/any '
        'later suffix) at the snapshot, census; (2) the ordinary record each rerun repeats; (3) strata in order %s; '
        'per directory (sorted): the ordinary record with the lowest filename index, the one with the highest, and '
        'k seeded random interior records via rng.sample on the index-sorted interior (k: A3=1, A3\'=2, A3\'\'=1, '
        'M2=all, i.e. census); then per stratum the earliest and latest record by mtime; (4) %d records by '
        'rng.sample from the remaining ordinary M1 records sorted by path. Selection reads only paths, filename '
        'indices, family/dir and mtimes of the snapshot; no CNF was generated before this manifest was written.' % (
            SEED, [s[0] for s in STRATA], TOPUP))
    man['strata'] = strata_info
    man['counts'] = {'items': len(order), 'reruns': len(reruns),
                     'rerun_originals': sum(1 for p in order if any(r.startswith('rerun_original_of:') for r in items[p]['roles'])),
                     'sample_ordinary': len(sample_ordinary),
                     'sample_ordinary_by_family': dict(Counter(byp[p]['family'] + '/' + byp[p]['kind'] for p in sample_ordinary)),
                     'sample_dirs_covered': dict(Counter(byp[p]['family'] for p in {byp[q]['family'] + '|' + byp[q]['dir']: q
                                                                                     for q in sample_ordinary}.values())),
                     'missing_rerun_originals': missing_originals}
    man['items'] = [dict(items[p], sha256=byp[p]['sha256'], family=byp[p]['family'], dir=byp[p]['dir'],
                         kind=byp[p]['kind'], suffix=byp[p]['suffix']) for p in order]
    man['controls'] = controls
    b = (json.dumps(man, indent=1) + '\n').encode()
    write_new(MANIFEST, b)
    os.chmod(MANIFEST, 0o444)
    write_new(MANIFEST_SHA, ('%s  %s\n' % (sha(b), MANIFEST.name)).encode())
    os.chmod(MANIFEST_SHA, 0o444)
    readme('sample frozen: %d items (%d reruns, %d rerun originals, %d ordinary sample), sample-manifest.json sha %s; '
           'no CNF generated yet' % (len(order), len(reruns), man['counts']['rerun_originals'], len(sample_ordinary), sha(b)))
    print(json.dumps({'sha256': sha(b), 'counts': man['counts'], 'strata': strata_info,
                      'controls': [(c['id'], c['target']) for c in controls]}, indent=1))


# ----------------------------------------------------------------------------- run
def load_modules():
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(PINNED))
    import encode_e1
    import encode_full
    import encode_full2
    import encode_partbatch
    import encode_partq
    import encode_skel
    import encode_skel_b
    import stream_check4
    import stream_check5
    mods = {'encode_e1': encode_e1, 'encode_skel': encode_skel, 'encode_full': encode_full, 'encode_full2': encode_full2,
            'encode_partq': encode_partq, 'encode_partbatch': encode_partbatch, 'encode_skel_b': encode_skel_b,
            'stream_check4': stream_check4, 'stream_check5': stream_check5}
    for name, m in mods.items():
        if Path(m.__file__).resolve() != (PINNED / (name + '.py')).resolve():
            raise SystemExit('module %s imported from %s' % (name, m.__file__))
    for m in ('encode_full', 'encode_full2', 'encode_partq', 'encode_partbatch', 'encode_skel'):
        if mods[m].encode_e1 is not encode_e1:
            raise SystemExit('%s uses a different encode_e1' % m)
    return mods


class Inputs:
    """Spec / list / skeleton bytes, each hashed when read and compared with pins.json."""

    def __init__(self, pins):
        self.pins = pins
        self.cache = OrderedDict()

    def _get(self, key, path, want):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        b = path.read_bytes()
        h = sha(b)
        val = (h, json.loads(b) if h == want else None)
        self.cache[key] = val
        while len(self.cache) > 6:
            self.cache.popitem(last=False)
        return val

    def spec(self, tag):
        e = self.pins['cases'][tag]['spec']
        return self._get(('spec', tag), S / e['path'], e['L']['sha256'] if e['bound'] else '-')

    def ext(self, fam, d, tag):
        c = self.pins['cases'][tag]
        e = c['m2_ext'] if fam == 'm2part_drat' else c['m1_ext']
        want = e['L']['sha256'] if e['bound'] else '-'
        return self._get(('ext', fam, d), L / e['path'], want), e

    def skelb(self, mi):
        rel = 'cycle2/skel-b/skeletons-b-ms%02d.json' % mi
        e = self.pins['shared_data'][rel]
        ok = e['L_equals_S'] and e['S_equals_R0_pin']
        return self._get(('skelb', mi), S / rel, e['S']['sha256'] if ok else '-')


def build(mods, fam, kind, encoder, rev, spec, E, skb, b_index, idxs):
    """Rebuild one formula exactly as the declared production call did; returns (bytes, info, inputs digest pair)."""
    if fam in ('a3', 'part') and kind == 'single':
        enc = {'encode_full.py': mods['encode_full'], 'encode_full2.py': mods['encode_full2'],
               'encode_partq.py': mods['encode_partq']}[encoder]
        ser = {4: mods['stream_check4'], 5: mods['stream_check5']}[rev]
        sub = dict(spec)
        sub['placed'] = E['full'][idxs[0]]
        before = jdigest([spec, sub['placed']])
        F, X, info = enc.build(sub)
        b = ser.cnf_bytes_of(F)
        after = jdigest([spec, sub['placed']])
        return b, info, before == after, '%s.build + %s.cnf_bytes_of' % (encoder[:-3], ser.__name__)
    if fam == 'part' and kind == 'batch':
        if encoder != 'encode_partbatch.py':
            raise KeyError(encoder)
        ser = {4: mods['stream_check4'], 5: mods['stream_check5']}[rev]
        pls = [E['full'][i] for i in idxs]
        before = jdigest([spec, pls])
        F, X, sel = mods['encode_partbatch'].build(spec, pls)
        b = ser.cnf_bytes_of(F)
        after = jdigest([spec, pls])
        return b, None, before == after, 'encode_partbatch.build + %s.cnf_bytes_of' % ser.__name__
    if fam == 'm2part_drat' and kind == 'batch':
        if encoder != 'encode_skel_b.build_partbatch':
            raise KeyError(encoder)
        sk = skb['skeletons'][b_index]
        special = [p for p in skb['profiles'] if list(p) != BASE]
        pls = [E['placements'][i] for i in idxs]
        before = jdigest([skb['c0'], sk, special, pls])
        nv, cl = mods['encode_skel_b'].build_partbatch(skb['c0'], [tuple(t) for t in sk['types']], sk['empty'], special, pls)
        b = mods['encode_skel_b'].cnf_bytes(nv, cl)
        after = jdigest([skb['c0'], sk, special, pls])
        return b, None, before == after, 'encode_skel_b.build_partbatch + encode_skel_b.cnf_bytes'
    raise KeyError((fam, kind, encoder))


def header(b):
    h = b[:b.index(b'\n')].split()
    return int(h[2]), int(h[3])


def evaluate(item, pe, pins, inp, mods, byp):
    res = OrderedDict([('path', item['path']), ('roles', item['roles']), ('family', pe['family']), ('dir', pe['dir']),
                       ('case', pe['case']), ('kind', pe['kind']), ('suffix', pe['suffix'])])
    res['started'] = now()
    p = L / item['path']
    data, rec, err = read_record(p)
    checks = OrderedDict()
    mism = []
    if err:
        res['status'] = 'FAIL' if err == 'missing' else 'PENDING'
        res['reason'] = 'record %s at replay' % err
        return res
    fam, d, tag = pe['family'], pe['dir'], pe['case']
    res['record_sha256'] = sha(data)
    checks['record_bytes_equal_snapshot'] = res['record_sha256'] == pe['sha256']
    cpe = pins['cases'].get(tag) if tag else None
    if cpe is None:
        res['status'] = 'PENDING'
        res['reason'] = 'directory not bound to a parent-verified case'
        return res
    (eh, E), epin = inp.ext(fam, d, tag)
    st, kind, suf, idxs = structural(fam, d, item['path'].rsplit('/', 1)[1], rec, len(E['full'] if fam != 'm2part_drat' else E['placements']) if E is not None else None)
    checks.update(st)
    checks['case_identity_spec'] = cpe['spec']['identity_ok']
    checks['spec_bytes_bound'] = cpe['spec']['bound']
    sh, spec = inp.spec(tag)
    checks['spec_bytes_equal_pin_at_replay'] = spec is not None
    checks['ext_list_bound_to_R6'] = epin['bound']
    checks['ext_bytes_equal_pin_at_replay'] = E is not None
    res['inputs'] = {'spec_sha256': sh, 'ext_path': epin['path'], 'ext_sha256': eh,
                     'ext_reference': ('R6 m2_regen_normalized_production_source' if fam == 'm2part_drat' else 'R6 m1_regen')}
    skb = None
    b_index = None
    if fam == 'm2part_drat':
        b_index = cpe['b_index']
        checks['a_to_b_map_equals_R6_b_index'] = cpe['a_to_b']['equals_R6_b_index']
        checks['b_index_in_m2_jobs_part'] = cpe['a_to_b']['in_m2_jobs_part']
        kh, skb = inp.skelb(cpe['multiset'])
        checks['skel_b_bytes_bound'] = skb is not None
        res['inputs']['skel_b_sha256'] = kh
        res['inputs']['bound_m1_tag'] = tag
    res['declared'] = {'encoder': rec.get('encoder'), 'runner': rec.get('runner'),
                       'stream_check_revision': rec.get('stream_check_revision'), 'kind': rec.get('kind'),
                       'index': rec.get('index', rec.get('full_index', rec.get('sub_index'))),
                       'indices': rec.get('indices') if fam == 'm2part_drat' else (
                           None if not (isinstance(rec.get('indices'), list) and rec['indices']) else {
                               'first': rec['indices'][0], 'last': rec['indices'][-1], 'count': len(rec['indices']),
                               'digest': jdigest(rec['indices'])})}
    res['checker_class'] = checker_class(rec)
    res['worker_claim'] = worker_claim(rec)
    res['recorded'] = {'cnf_sha256': rec.get('cnf_sha256'), 'cnf_bytes': rec.get('cnf_bytes')}
    blockers = [k for k in ('record_bytes_equal_snapshot', 'spec_bytes_equal_pin_at_replay', 'ext_bytes_equal_pin_at_replay',
                            'skel_b_bytes_bound') if checks.get(k) is False]
    if (idxs is None or blockers or not checks['declared_encoder_expected']
            or checks.get('indices_within_pinned_list') is not True):
        res['checks'] = checks
        res['status'] = 'FAIL'
        res['mismatches'] = [k for k, v in checks.items() if v is False]
        res['reason'] = 'inputs or indices not bound; formula not regenerated'
        return res
    t = time.perf_counter()
    try:
        b, info, unmutated, call = build(mods, fam, kind, rec.get('encoder'), rec.get('stream_check_revision'),
                                         spec, E, skb, b_index, idxs)
    except KeyError as ex:
        res['checks'] = checks
        res['status'] = 'PENDING'
        res['reason'] = 'declared encoder/serializer not supported by this driver: %r' % (ex,)
        return res
    res['build_s'] = round(time.perf_counter() - t, 3)
    nv, nc = header(b)
    res['generated'] = {'cnf_sha256': sha(b), 'cnf_bytes': len(b), 'vars': nv, 'clauses': nc, 'call': call}
    del b
    checks['inputs_not_mutated_by_encoder'] = unmutated
    checks['cnf_sha256_equal'] = res['generated']['cnf_sha256'] == rec.get('cnf_sha256')
    checks['cnf_bytes_equal'] = res['generated']['cnf_bytes'] == rec.get('cnf_bytes')
    if info is not None and 'leave' in rec:
        checks['leave_vector_equal'] = info.get('leave') == rec.get('leave')
    if suf:
        stem = ('f%05d.json' % idxs[0]) if kind == 'single' else item['path'].rsplit('/', 1)[1].rsplit('_', 1)[0] + '.json'
        op = item['path'].rsplit('/', 1)[0] + '/' + stem
        od, orec, oerr = read_record(L / op)
        checks['rerun_original_present'] = orec is not None
        if orec is not None:
            res['original'] = {'path': op, 'sha256': sha(od), 'cnf_sha256': orec.get('cnf_sha256'),
                               'encoder': orec.get('encoder'), 'status': orec.get('status'), 'checked': orec.get('checked')}
            if kind == 'batch':
                checks['rerun_indices_equal_original'] = rec.get('indices') == orec.get('indices')
            if rec.get('encoder') == orec.get('encoder'):
                checks['rerun_recorded_cnf_equal_original_recorded'] = rec.get('cnf_sha256') == orec.get('cnf_sha256')
            else:
                res['original']['note'] = 'different declared encoder; CNF hashes are expected to differ'
                checks['rerun_cnf_differs_from_original_encoder_formula'] = rec.get('cnf_sha256') != orec.get('cnf_sha256')
                if 'leave' in rec:
                    checks['rerun_leave_equal_original_leave'] = rec.get('leave') == orec.get('leave')
    res['checks'] = checks
    res['mismatches'] = [k for k, v in checks.items() if v is False]
    res['status'] = 'FAIL' if res['mismatches'] else 'PASS'
    return res


def control(ctl, pins, inp, mods, byp):
    out = OrderedDict([('id', ctl['id']), ('target', ctl['target']), ('mutation', ctl['mutation']),
                       ('expect', ctl['expect'])])
    if not ctl['target']:
        out['status'] = 'NOT_APPLICABLE'
        return out
    pe = byp[ctl['target']]
    data, rec, err = read_record(L / ctl['target'])
    fam, d, tag, kind = pe['family'], pe['dir'], pe['case'], pe['kind']
    (eh, E), epin = inp.ext(fam, d, tag)
    sh, spec = inp.spec(tag)
    skb = inp.skelb(pins['cases'][tag]['multiset'])[1] if fam == 'm2part_drat' else None
    n = len(E['placements'] if fam == 'm2part_drat' else E['full'])
    st, kind, suf, idxs = structural(fam, d, ctl['target'].rsplit('/', 1)[1], rec, n)
    enc = rec.get('encoder')
    cid = ctl['id']
    if cid.startswith('C1') or cid.startswith('C2'):
        i = idxs[0] + 1 if idxs[0] + 1 < n else idxs[0] - 1
        idxs = [i]
    elif cid.startswith('C3'):
        enc = 'encode_full.py'
    elif cid.startswith('C4'):
        idxs = idxs[:-1]
    elif cid.startswith('C5'):
        idxs = list(range(idxs[0], idxs[-1] + 1))
    elif cid.startswith('C6'):
        idxs = idxs[:-1]
    t = time.perf_counter()
    b, info, unmut, call = build(mods, fam, kind, enc, rec.get('stream_check_revision'), spec, E, skb,
                                 pins['cases'][tag]['b_index'], idxs)
    out['build_s'] = round(time.perf_counter() - t, 3)
    g = sha(b)
    del b
    out['generated_cnf_sha256'] = g
    out['target_recorded_cnf_sha256'] = rec.get('cnf_sha256')
    out['mutated_indices'] = {'count': len(idxs), 'first': idxs[0], 'last': idxs[-1]}
    out['differs_from_target'] = g != rec.get('cnf_sha256')
    ok = out['differs_from_target']
    if cid.startswith('C3'):
        od, orec, oerr = read_record(L / ctl['target'].replace('_exact.json', '.json'))
        out['original_recorded_cnf_sha256'] = orec.get('cnf_sha256') if orec else None
        out['equals_original_recorded'] = orec is not None and g == orec.get('cnf_sha256')
        ok = ok and out['equals_original_recorded']
    out['status'] = 'AS_EXPECTED' if ok else 'UNEXPECTED'
    return out


def done_keys():
    keys = {}
    if RUNS.exists():
        for pf in sorted(RUNS.glob('run-*/progress.jsonl')):
            for line in pf.read_text().splitlines():
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get('event') in ('item', 'control') and r.get('status') in ('PASS', 'FAIL', 'AS_EXPECTED', 'UNEXPECTED',
                                                                                  'NOT_APPLICABLE'):
                    keys[r['key']] = r
    return keys


def cmd_run(argv):
    require_flags()
    max_min = float(argv[argv.index('--max-minutes') + 1]) if '--max-minutes' in argv else 150.0
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    mb = MANIFEST.read_bytes()
    if MANIFEST_SHA.read_text().split()[0] != sha(mb):
        raise SystemExit('manifest hash mismatch')
    man = json.loads(mb)
    pins, pins_sha, pop = load_pins_pop()
    if pins_sha != man['pins_sha256']:
        raise SystemExit('pins.json changed after sampling')
    for n, e in pins['replay_sources'].items():
        if sha((PINNED / n).read_bytes()) != e['sha256']:
            raise SystemExit('pinned source changed: %s' % n)
    byp = {e['path']: e for e in pop}
    mods = load_modules()
    inp = Inputs(pins)
    done = done_keys()
    RUNS.mkdir(exist_ok=True)
    k = 1
    while (RUNS / ('run-%03d' % k)).exists():
        k += 1
    rd = RUNS / ('run-%03d' % k)
    rd.mkdir(exist_ok=False)
    pf = open(rd / 'progress.jsonl', 'x')
    t0 = time.time()

    def emit(obj):
        pf.write(json.dumps(obj, separators=(',', ':')) + '\n')
        pf.flush()
        os.fsync(pf.fileno())

    emit({'event': 'start', 'at': now(), 'proc': proc_info(), 'manifest_sha256': sha(mb), 'pins_sha256': pins_sha,
          'free_bytes': free_bytes(), 'already_done': len(done), 'max_minutes': max_min})
    readme('run %s start (manifest %s, already done %d)' % (rd.name, sha(mb)[:16], len(done)))
    end_reason = 'complete'
    last_ck = time.time()
    n_done = 0
    todo = [('item', it) for it in man['items']] + [('control', c) for c in man['controls']]
    for kind, obj in todo:
        key = obj['path'] if kind == 'item' else obj['id']
        if key in done:
            continue
        if STOP:
            end_reason = 'stop: %s' % STOP[0]
            break
        if STOPFILE.exists():
            end_reason = 'stop file'
            break
        if time.time() - t0 > max_min * 60:
            end_reason = 'max minutes'
            break
        fb = free_bytes()
        if fb < FREE_FLOOR + 200_000_000:
            end_reason = 'disk floor (free %d)' % fb
            break
        u = usage()
        if u['maxrss_bytes'] > RSS_STOP:
            end_reason = 'rss stop (%d)' % u['maxrss_bytes']
            break
        try:
            if kind == 'item':
                r = evaluate(obj, byp[obj['path']], pins, inp, mods, byp)
            else:
                r = control(obj, pins, inp, mods, byp)
        except Exception as ex:  # a driver defect is recorded, never turned into a PASS
            import traceback
            r = {'path': obj.get('path'), 'id': obj.get('id'),
                 'status': 'PENDING' if kind == 'item' else 'UNEXPECTED',
                 'reason': 'driver exception %r' % (ex,), 'traceback': traceback.format_exc()[-2000:]}
        r['event'] = kind
        r['key'] = key
        r['ended'] = now()
        r['maxrss_bytes'] = usage()['maxrss_bytes']
        emit(r)
        n_done += 1
        if time.time() - last_ck > 1500:
            readme('run %s checkpoint: %d evaluated this run, %s' % (rd.name, n_done, json.dumps(usage())))
            last_ck = time.time()
    u = usage()
    emit({'event': 'end', 'at': now(), 'end_reason': end_reason, 'evaluated': n_done, 'elapsed_s': round(time.time() - t0, 1),
          **u, 'free_bytes': free_bytes()})
    pf.close()
    readme('run %s end: %s, %d evaluated, %s' % (rd.name, end_reason, n_done, json.dumps(u)))
    print(json.dumps({'run': rd.name, 'end_reason': end_reason, 'evaluated': n_done, **u}))


# ----------------------------------------------------------------------------- finalize
def dir_bytes(p):
    tot = 0
    alloc = 0
    files = 0
    for root, _, fs in os.walk(p):
        for f in fs:
            st = os.stat(os.path.join(root, f))
            tot += st.st_size
            alloc += st.st_blocks * 512
            files += 1
    return files, tot, alloc


def cmd_finalize():
    require_flags()
    if RESULT.exists():
        raise SystemExit('result exists')
    t0 = time.time()
    mb = MANIFEST.read_bytes()
    man = json.loads(mb)
    pins, pins_sha, pop = load_pins_pop()
    byp = {e['path']: e for e in pop}
    runs = []
    results = {}
    for pfp in sorted(RUNS.glob('run-*/progress.jsonl')):
        lines = [json.loads(x) for x in pfp.read_text().splitlines() if x]
        st = [x for x in lines if x.get('event') == 'start']
        en = [x for x in lines if x.get('event') == 'end']
        runs.append({'run': pfp.parent.name, 'progress_sha256': sha(pfp.read_bytes()),
                     'start': st[0] if st else None, 'end': en[0] if en else None,
                     'items': sum(1 for x in lines if x.get('event') in ('item', 'control'))})
        for x in lines:
            if x.get('event') in ('item', 'control'):
                results[x['key']] = x
    items = []
    for it in man['items']:
        r = results.get(it['path'])
        if r is None:
            r = {'path': it['path'], 'roles': it['roles'], 'status': 'PENDING', 'reason': 'not evaluated in any run'}
        items.append(r)
    ctrls = [results.get(c['id'], {'id': c['id'], 'status': 'PENDING'}) for c in man['controls']]
    # freeze check: sources, specs, ext lists, shared data
    freeze = OrderedDict()
    for n, e in pins['replay_sources'].items():
        lv = file_info(L / 'src' / n)
        freeze['src/' + n] = {'pinned_copy_unchanged': sha((PINNED / n).read_bytes()) == e['sha256'],
                              'live_now_sha256': lv.get('sha256'), 'live_unchanged_since_pin': lv.get('sha256') == e['L_sha256']}
    used_cases = sorted({byp[i['path']]['case'] for i in man['items'] if byp[i['path']]['case']})
    for tag in used_cases:
        c = pins['cases'][tag]
        for key in ('spec', 'm1_ext', 'm2_ext'):
            e = c[key]
            if key == 'm2_ext' and not e['L']['exists']:
                lv = file_info(L / e['path'])
                freeze[e['path']] = {'absent_at_pin': True, 'now_exists': lv['exists'], 'now_sha256': lv.get('sha256'),
                                     'now_equals_R6_prediction': lv.get('sha256') == e['R6_m2_regen_normalized_production_source']}
                continue
            if key == 'm1_ext' and not e['L']['exists']:
                continue
            lv = file_info(L / e['path'])
            freeze[e['path']] = {'live_unchanged_since_pin': lv.get('sha256') == e['L']['sha256']}
    for rel, e in pins['shared_data'].items():
        lv = file_info(L / rel)
        freeze[rel] = {'live_unchanged_since_pin': lv.get('sha256') == e['L'].get('sha256')}
    freeze_ok = all(v.get('pinned_copy_unchanged', True) and v.get('live_unchanged_since_pin', True) for v in freeze.values())
    src_now = {p.name: sha(p.read_bytes()) for p in (L / 'src').iterdir() if p.is_file()}
    src_changes = {'new_since_pin': sorted(set(src_now) - set(n for n, e in pins['sources'].items() if e['L']['exists'])),
                   'changed_since_pin': sorted(n for n, h in src_now.items() if n in pins['sources']
                                               and pins['sources'][n]['L'].get('sha256') not in (None, h))}
    # late / changed records
    late, changed, removed = [], [], []
    seen = set()
    for fam, rel in FAMILY_DIRS:
        base = L / rel
        for d in sorted(os.listdir(base)):
            dp = base / d
            if not dp.is_dir():
                continue
            for fn in sorted(os.listdir(dp)):
                if fn in NONRECORD or parse_name(fn) is None:
                    continue
                prel = '%s/%s/%s' % (rel, d, fn)
                seen.add(prel)
                if prel not in byp:
                    stt = (dp / fn).stat()
                    late.append({'path': prel, 'size': stt.st_size,
                                 'mtime': time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime(stt.st_mtime))})
                else:
                    h = sha((dp / fn).read_bytes())
                    if h != byp[prel]['sha256']:
                        changed.append({'path': prel, 'snapshot_sha256': byp[prel]['sha256'], 'now_sha256': h})
    removed = sorted(p for p in byp if p not in seen)
    new_ext = []
    for tag, c in pins['cases'].items():
        e = c['m2_ext']
        if not e['L']['exists']:
            lv = file_info(L / e['path'])
            if lv['exists']:
                new_ext.append({'tag': tag, 'path': e['path'], 'sha256': lv['sha256'],
                                'equals_R6_prediction': lv['sha256'] == e['R6_m2_regen_normalized_production_source']})
    other_trees = {t: (L / t).exists() for t in OTHER_SPLIT_TREES}
    # aggregation
    cnt = Counter(r['status'] for r in items)
    by_role = defaultdict(Counter)
    for r in items:
        for role in r.get('roles', []):
            by_role[':'.join(role.split(':')[:2]) if role.startswith('sample:') else role.split(':')[0]][r['status']] += 1
    fails = [{'path': r['path'], 'mismatches': r.get('mismatches'), 'reason': r.get('reason'),
              'recorded': r.get('recorded'), 'generated': r.get('generated')} for r in items if r['status'] == 'FAIL']
    pend = [{'path': r['path'], 'reason': r.get('reason')} for r in items if r['status'] == 'PENDING']
    sample_paths = [i['path'] for i in man['items'] if any(x.startswith('sample:') for x in i['roles'])]
    sample_status = Counter(results.get(p, {}).get('status', 'PENDING') for p in sample_paths)
    rerun_paths = [i['path'] for i in man['items'] if any(x.startswith('rerun:') for x in i['roles'])]
    rerun_status = Counter(results.get(p, {}).get('status', 'PENDING') for p in rerun_paths)
    ctrl_ok = all(c.get('status') in ('AS_EXPECTED', 'NOT_APPLICABLE') for c in ctrls)
    if fails:
        verdict = 'FAIL'
    elif not freeze_ok or changed or removed:
        verdict = 'REVIEW'
    elif pend or not ctrl_ok:
        verdict = 'PASS_WITH_PENDING'
    else:
        verdict = 'PASS'
    files, tot, alloc = dir_bytes(HERE)
    res = OrderedDict()
    res['title'] = 'PA(19,8,6) R8 parent replay: split/rerun CNF records bound to exact (spec, placement list, indices) inputs'
    res['scope'] = (
        'Formula binding only, for the frozen selection: every split record with a rerun suffix (_r2, _r3, _exact; no '
        'other suffix existed at the snapshot), the ordinary record each rerun repeats, and a seeded stratified sample '
        '(seed %d) of ordinary f/batch records over all split families present at the snapshot (M1 A3 ms01 encode_full, '
        'M1 A3\' ms09 encode_partq, M1 A3\'\' ms09 encode_partbatch, M2 m2part_drat ms01 encode_skel_b.build_partbatch). '
        'Each formula was rebuilt in memory with the declared encoder from pinned copies of the lane sources, from the '
        'parent-pinned spec bytes and from the parent-verified (R6) placement list, using the declared indices with M1 '
        'explicit-list and M2 [lo,hi] semantics, then hashed and compared with the recorded cnf_sha256/cnf_bytes; bytes '
        'were discarded. Structural checks (filename index vs record field, batch ranges, list bounds, declared encoder) '
        'ran on every split record of the snapshot.' % SEED)
    res['not_claimed'] = (
        'No UNSAT acceptance or certification of any record (old drat-trim, retired lrat-check-only and lane-written '
        'checker records alike), no proof was read or re-checked, no solver ran, no claim about cover completeness, '
        'unsampled records, records written after the snapshot, or PA(19,8,6) existence/nonexistence. PA(19,8,6) '
        'remains undecided. checker_class and worker_claim fields are worker-recorded fields only.')
    res['verdict'] = verdict
    res['verdict_rules'] = {
        'item PASS': 'record bytes equal the snapshot, identity/name/index/range/encoder checks true, spec and placement '
                     'list bytes equal the parent pins, encoder did not mutate its inputs, generated cnf_sha256 and '
                     'cnf_bytes equal the record (plus leave vector and rerun-pair checks where applicable)',
        'item FAIL': 'any of those checks false (exact list in mismatches)',
        'item PENDING': 'not evaluated, or input/encoder not bound/supported',
        'overall': 'FAIL if any item FAIL; REVIEW if the source/spec/list freeze broke after the pin or a snapshot '
                   'record changed/vanished afterwards; PASS_WITH_PENDING if any PENDING or a mutation control not as '
                   'expected; else PASS (binding of the selection only)'}
    res['counts'] = {'items': len(items), 'by_status': dict(cnt), 'sample_ordinary': len(sample_paths),
                     'sample_ordinary_by_status': dict(sample_status), 'reruns': len(rerun_paths),
                     'reruns_by_status': dict(rerun_status), 'by_role': {k: dict(v) for k, v in sorted(by_role.items())},
                     'by_checker_class': dict(Counter('%s/%s' % (r.get('checker_class'), r['status']) for r in items))}
    res['mismatches'] = fails
    res['pending'] = pend
    res['mutation_controls'] = ctrls
    res['mutation_controls_all_as_expected'] = ctrl_ok
    res['reruns'] = [results.get(p) or {'path': p, 'status': 'PENDING'} for p in rerun_paths]
    res['items'] = items
    res['sample_manifest'] = {'path': MANIFEST.name, 'sha256': sha(mb), 'created': man['created'], 'seed': man['seed'],
                              'algorithm': man['algorithm'], 'strata': man['strata'], 'counts': man['counts'],
                              'driver_sha256_at_sampling': man['driver_sha256']}
    res['population_snapshot'] = {k: v for k, v in pins['population'].items() if k != 'nonrecord_files'}
    res['population_snapshot']['nonrecord_files'] = [{k: v for k, v in x.items() if k in ('path', 'kind', 'size', 'sha256')}
                                                     for x in pins['population']['nonrecord_files']]
    res['pins'] = {'path': PINS.name, 'sha256': pins_sha, 'recorded_at': pins['recorded_at'],
                   'reference_receipts': pins['reference_receipts'], 'worker_manifests': pins['worker_manifests'],
                   'replay_sources': pins['replay_sources'], 'sources_summary': pins['sources_summary'],
                   'source_deltas': {n: {k: e[k] for k in ('L', 'S', 'R0_pin', 'R5_pin', 'R6_pin_L', 'worker_manifest_1218',
                                                            'worker_src_delta_1334', 'L_equals_S', 'deltas_vs_L')}
                                     for n, e in pins['sources'].items() if e['deltas_vs_L'] or e['L_equals_S'] is False},
                   'shared_data': pins['shared_data'], 'cases_summary': pins['cases_summary'],
                   'cases': {t: {'spec': {k: c['spec'][k] for k in ('path', 'bound', 'identity_ok', 'R6_spec_S')},
                                 'm1_ext': {k: c['m1_ext'].get(k) for k in ('path', 'bound', 'n', 'R6_m1_regen')},
                                 'm2_dir': c['m2_dir'],
                                 'm2_ext': {k: c['m2_ext'].get(k) for k in ('path', 'bound', 'n',
                                                                             'R6_m2_regen_normalized_production_source')},
                                 'm2_ext_live_sha256_at_pin': c['m2_ext']['L'].get('sha256'),
                                 'a_to_b': c['a_to_b']} for t, c in pins['cases'].items()}}
    res['code'] = {'driver': {'path': Path(__file__).name, 'sha256': driver_sha(),
                              'sha256_at_pin': pins['driver']['driver_sha256'],
                              'sha256_at_sampling': man['driver_sha256'],
                              'sha256_per_run': [r['start']['proc']['driver_sha256'] for r in runs if r['start']]},
                   'pinned_src_dir': PINNED.name}
    res['runs'] = runs
    res['freeze_check_at_finalize'] = {'ok': freeze_ok, 'entries': freeze, 'lane_src_changes_since_pin': src_changes}
    res['after_snapshot'] = {'late_records': late, 'changed_records': changed, 'removed_records': removed,
                             'new_m2_ext_lists': new_ext, 'other_split_trees_exist': other_trees}
    nxt = []
    if late:
        by_dir = Counter(x['path'].rsplit('/', 1)[0] for x in late)
        nxt.append('Bind %d record(s) written after the snapshot (by dir: %s): rerun structural checks and regenerate the '
                   'formula with the declared encoder from the R6-bound list; M2 dirs need ext.json sha equal to the R6 '
                   'prediction first.' % (len(late), dict(by_dir)))
    if new_ext:
        nxt.append('New M2 ext lists after the pin: %s' % [(x['path'], x['equals_R6_prediction']) for x in new_ext])
    if any(other_trees.values()):
        nxt.append('Split trees %s now exist; add them as families (encoder per record).' % [t for t, v in other_trees.items() if v])
    nxt.append('Unsampled ordinary records stay formula-unbound beyond the structural checks; extend by a census or a '
               'fresh seeded sample if acceptance needs them.')
    nxt.append('UNSAT acceptance still needs a parent proof check per record route (drat-trim on regenerated CNF + '
               'stored/streamed proof); retired lrat-check-only (_r2) and lane-written checker records never count.')
    res['next_actions'] = nxt
    res['resources'] = {'finalize': {**usage(), 'elapsed_s': round(time.time() - t0, 2)},
                        'runs': [{k: (r['end'] or {}).get(k) for k in ('cpu_user_s', 'cpu_sys_s', 'maxrss_bytes', 'elapsed_s',
                                                                         'end_reason', 'free_bytes')} for r in runs],
                        'pin': pins['resources'], 'output_files_before_result': files,
                        'output_bytes_before_result': tot, 'output_allocated_bytes_before_result': alloc,
                        'free_bytes_at_finalize': free_bytes(), 'free_floor': FREE_FLOOR, 'maxrss_unit': 'bytes',
                        'limits': {'busy_cpu': 1, 'rss_bytes': 3 * 1024 ** 3, 'new_data_bytes': NEWDATA_CAP}}
    res['independence_and_limits'] = [
        'The replay re-executes the lane encoder code (pinned byte copies); it shows that each selected record\'s formula is '
        'exactly the declared encoder applied to the pinned spec, the parent-verified placement list and the declared '
        'indices. It does not re-derive the encoders\' clause semantics (see the encoder audit) or their soundness.',
        'Placement lists are bound through R6 (parent regeneration from pinned code); the A->B map through R4/R6 '
        '(compare-map a_to_b plus R6 explicit isomorphisms). Spec bytes through R0 pins and R6 spec_S.',
        'encode_full2.py, stream_check5.py and the rerun runners were not in snapshot S; their live bytes were pinned here '
        'and compared with the worker\'s time-stamped manifests (worker-recorded, not parent-verified).',
        'Records carry no encoder hash; the exact-version claim rests on byte-equal regenerated CNFs, plus encoder mtimes '
        'that precede the records (pins.json).',
        'Unsampled ordinary records are bound only by structural checks; the sample bounds the rate of formula '
        'mismatches but does not exclude isolated ones.']
    res['finalized'] = now()
    res['finalize_command'] = proc_info()
    dump_new(RESULT, res)
    os.chmod(RESULT, 0o444)
    readme('finalize: verdict %s; items %s; sample %s; reruns %s; controls ok %s; late %d changed %d removed %d; '
           'result sha %s' % (verdict, dict(cnt), dict(sample_status), dict(rerun_status), ctrl_ok, len(late),
                              len(changed), len(removed), sha(RESULT.read_bytes())))
    print(json.dumps({'verdict': verdict, 'counts': res['counts'], 'freeze_ok': freeze_ok, 'late': len(late),
                      'changed': len(changed), 'removed': len(removed), 'controls_ok': ctrl_ok,
                      'mismatches': fails[:5], 'pending': pend[:5]}, indent=1))


def main():
    os.chdir(HERE)
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'pin':
        cmd_pin()
    elif cmd == 'sample':
        cmd_sample()
    elif cmd == 'run':
        cmd_run(sys.argv[2:])
    elif cmd == 'finalize':
        cmd_finalize()
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
