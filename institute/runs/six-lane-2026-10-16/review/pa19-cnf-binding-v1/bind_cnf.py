#!/usr/bin/env python3
"""Parent R5 replay for PA(19,8,6): bind each of the 5577 non-balanced M1 base CNFs to its frozen
skeleton specification and to every worker pass-1 / later direct proof record for that tag.

Authority: the parent's pinned snapshot S = ../pa19-parent-cover-replay-v1/inputs. `prepare` copies
S/src/{encode_skel,encode_e1,stream_check4}.py byte-exactly into pinned-src/; `run` imports only from
there. Per tag (index order): read the S spec, rebuild encode_skel.build(spec) in memory, serialize with
stream_check4.cnf_bytes_of, SHA-256, discard. Then read each live lane record for the tag once, pin its
exact bytes, and compare the recorded cnf_sha256 plus the recorded size/count/path/tag metadata. Split
(a3/part f/batch) records are a separate obligation and are not compared here.

No solver, no proof checker; no CNF or proof is written, copied or read. Binding only: nothing here
accepts an UNSAT claim, a proof, a checker, the cover, or any PA(19,8,6) verdict.

Commands (interpreter flags -B -I are required: no bytecode cache, no user site/env):
  python3 -B -I bind_cnf.py dry N         first N index tags, imports from S, writes nothing
  python3 -B -I bind_cnf.py prepare       pin sources/small inputs, identity checks -> pins.json
  python3 -B -I bind_cnf.py run [--max-minutes M] [--max-tags N] [--stop-on-mismatch]
                                          resumable chunk -> chunks/chunk-NNN/progress.jsonl
  python3 -B -I bind_cnf.py finalize      final sweep of live records -> cnf-binding-result.json
"""
import ast
import difflib
import hashlib
import io
import json
import os
import re
import resource
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / 'pa19-parent-cover-replay-v1'
S = PARENT / 'inputs'
REPO = HERE.parents[4]
L = REPO / 'information-science' / 'evidence' / 'six-lane-20261016' / 'packing-array19'
PINNED = HERE / 'pinned-src'
PINNED_LANE = HERE / 'pinned-lane'
CHUNKS = HERE / 'chunks'
PINS = HERE / 'pins.json'
RESULT = HERE / 'cnf-binding-result.json'
MANIFEST = HERE / 'pinned-records.sha256'
SRC_FILES = ('encode_skel.py', 'encode_e1.py', 'stream_check4.py')
EXPECTED_COUNTS = {1: 3215, 2: 59, 3: 674, 4: 39, 5: 73, 6: 482, 7: 482, 8: 482, 9: 71}
BASE = [4, 3, 3, 3, 3, 3]
FREE_FLOOR = 12_000_000_000
RSS_CAP = 3 * 1024 ** 3
CHECKPOINT_S = 600
TAG_JSON = re.compile(r'^ms0[1-9]_s\d{5}\.json$')
CYCLE1_COMMIT = '97567e6dd46dd7e4f6bf9f36c847076076c2ea47'
LANE_REL = 'information-science/evidence/six-lane-20261016/packing-array19'
# (class, lane-relative path template, role)
CLASSES = (
    ('pass1', 'cases19skel/results/{}.json', 'pass1'),
    ('proofcheck', 'cases19skel/proofcheck/{}.json', 'direct'),
    ('proofstream', 'cycle2/proofstream/{}.json', 'direct'),
    ('hard', 'cycle2/hard/{}.json', 'direct'),
    ('hard5', 'cycle2/hard5/{}.json', 'direct'),
    ('archive_proofcheck_kill', 'archive/proofpass-kill-artifacts-0516/{}.json', 'archived_direct'),
    ('archive_pass0_sample', 'archive/skel-sample-pass0/results/{}.json', 'archived_informational'),
)
KNOWN_DIRS = {t.rsplit('/', 1)[0] for _, t, _ in CLASSES}
# tag-named JSON that is never a base-CNF record (classified by inspection, host clock 2026-10-17 13:49 PDT)
EXCLUDED = {'controls/': '13-row (13,5,4) control cases', 'cycle2/control13': '13-row control runs',
            'cases19skel/specs': 'the frozen specs themselves (inputs)', 'scratch/': 'scratch tests',
            'cases19full/ext': 'placement enumerations {source,raw,num_full,full}; no CNF hash'}
KEEP = ('status', 'pass1_status', 'kissat_rc', 'solver_rc', 'checked', 'ok', 'drat_trim_verified', 'lrat_verified',
        'checker_interrupted', 'stream_check_revision', 'mode', 'runner', 'encoder', 'solver', 'cnf_matches_pass1',
        'cnf_matches_pass1_sha', 'drat_sha256', 'drat_bytes', 'lrat_sha256', 'lrat_bytes')
STATUSES = ('PASS', 'PENDING', 'FAIL', 'REVIEW')
STOP = []


def sha(b):
    return hashlib.sha256(b).hexdigest()


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def free_bytes():
    st = os.statvfs(HERE)
    return st.f_bavail * st.f_frsize


def usage():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return {'cpu_user_s': round(r.ru_utime, 2), 'cpu_sys_s': round(r.ru_stime, 2),
            'maxrss_bytes': r.ru_maxrss}  # macOS getrusage reports bytes


def write_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'xb') as f:
        f.write(data)
    return len(data)


def dump_new(path, obj):
    return write_new(path, (json.dumps(obj, indent=1) + '\n').encode())


def rel(p):
    return str(Path(p).relative_to(HERE))


def repo_rel(p):
    return str(Path(p).relative_to(REPO))


def next_dir(parent, pattern):
    parent.mkdir(exist_ok=True)
    n = 1
    while (parent / (pattern % n)).exists():
        n += 1
    d = parent / (pattern % n)
    d.mkdir(exist_ok=False)
    return d


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


def read_record(p):
    """Read once; a record being rewritten by the live writer is retried (bounded)."""
    data, t = None, now()
    for _ in range(6):
        try:
            data = p.read_bytes()
        except FileNotFoundError:
            return None, None, 'missing', now()
        t = now()
        try:
            return data, json.loads(data), None, t
        except ValueError:
            time.sleep(2)
    return data, None, 'unparseable', t


def func_source(text, name, cls=None):
    body = ast.parse(text).body
    if cls:
        body = next(n for n in body if isinstance(n, ast.ClassDef) and n.name == cls).body
    node = next(n for n in body if isinstance(n, ast.FunctionDef) and n.name == name)
    return ast.get_source_segment(text, node)


def serializer_variants(ref):
    out = {}
    for p in sorted((L / 'src').glob('stream_check*.py')):
        b = p.read_bytes()
        try:
            seg = func_source(b.decode(), 'cnf_bytes_of')
        except Exception as e:  # absent function or unparsable live file: record, do not guess
            seg = 'ERROR %r' % e
        out[p.name] = {'sha256': sha(b), 'identical_function': seg == ref}
    return out


def load_modules(srcdir):
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(srcdir))
    import encode_e1
    import encode_skel
    import stream_check4
    mods = {'encode_e1': encode_e1, 'encode_skel': encode_skel, 'stream_check4': stream_check4}
    for name, m in mods.items():
        if Path(m.__file__).resolve() != (srcdir / (name + '.py')).resolve():
            raise SystemExit('module %s imported from %s' % (name, m.__file__))
    if encode_skel.encode_e1 is not encode_e1:
        raise SystemExit('encode_skel uses a different encode_e1')
    return mods


def parent_pins():
    return json.loads((PARENT / 'pin-result.json').read_bytes())['files']


def profiles():
    return json.loads((S / 'data' / 'profiles-19-8-6.json').read_bytes())


def index_rows():
    b = (S / 'cases19skel' / 'index.json').read_bytes()
    return sha(b), json.loads(b)


def load_pins():
    b = PINS.read_bytes()
    return sha(b), json.loads(b)


def load_chunks():
    return [(p, p.read_bytes()) for p in sorted(CHUNKS.glob('chunk-*/progress.jsonl'))]


def check_index(idx):
    rows = idx['cases']
    probs = []
    if idx.get('num_cases') != 5577 or len(rows) != 5577:
        probs.append('num_cases')
    if any(set(r) != {'tag', 'multiset', 'skel'} for r in rows):
        probs.append('row_keys')
    if any(r['tag'] != 'ms%02d_s%05d' % (r['multiset'], r['skel']) for r in rows):
        probs.append('tag_format')
    tags = [r['tag'] for r in rows]
    if len(set(tags)) != len(tags):
        probs.append('duplicate_tags')
    counts = {}
    for mi in range(1, 10):
        sk = [r['skel'] for r in rows if r['multiset'] == mi]
        counts[mi] = len(sk)
        if sk != list(range(len(sk))):
            probs.append('ms%02d_not_contiguous_in_order' % mi)
    if counts != EXPECTED_COUNTS:
        probs.append('counts')
    if [r['multiset'] for r in rows] != sorted(r['multiset'] for r in rows):
        probs.append('multiset_order')
    spec_files = sorted(p.name for p in (S / 'cases19skel' / 'specs').iterdir())
    if spec_files != sorted(t + '.json' for t in tags):
        probs.append('spec_file_set')
    return probs, counts


def spec_problems(spec, row, D):
    probs = []
    mi, si = row['multiset'], row['skel']
    if spec.get('kind') != 'skel':
        probs.append('kind')
    if (spec.get('N'), spec.get('k'), spec.get('q')) != (19, 8, 6):
        probs.append('N_k_q')
    if spec.get('multiset_index') != mi:
        probs.append('multiset_index')
    if spec.get('skel_index') != si:
        probs.append('skel_index')
    if 'base_quad' in spec:
        probs.append('base_quad_key_present')
    ms = D['multisets'][mi]
    special = [list(p) for p in spec.get('special', [])]
    try:
        if sorted([BASE] * spec['c0'] + special) != sorted(list(p) for p in ms['profiles']):
            probs.append('profile_multiset')
    except (KeyError, TypeError):
        probs.append('profile_multiset')
    if any(p == BASE for p in special):
        probs.append('special_contains_base_profile')
    key = lambda p: (-sum(x * (x - 1) // 2 for x in p), [-x for x in p])  # noqa: E731
    if special != sorted(special, key=key):
        probs.append('special_order')
    if spec.get('L') != ms['zero_agreement_pairs']:
        probs.append('L')
    return probs


def build_cnf(mods, spec):
    t0 = time.perf_counter()
    F, _X, _info = mods['encode_skel'].build(spec)
    b = mods['stream_check4'].cnf_bytes_of(F)
    return {'cnf_sha256': sha(b), 'cnf_bytes': len(b), 'vars': F.nv, 'clauses': len(F.clauses),
            'build_seconds': round(time.perf_counter() - t0, 3)}


class _Sink(io.StringIO):
    def __init__(self, store):
        super().__init__()
        self._store = store

    def close(self):
        self._store.append(self.getvalue())
        super().close()


def write_path_sha(mods, spec):
    """Diagnostic only (on mismatch): pass 1 serialized via encode_e1.CNF.write; capture it in memory."""
    F, _X, _info = mods['encode_skel'].build(spec)
    store, e1 = [], mods['encode_e1']
    e1.open = lambda path, mode='r', *a, **k: _Sink(store)
    try:
        F.write('<memory>')
    finally:
        del e1.open
    return sha(store[0].encode())


def evaluate(cls, rec, tag, mi, built):
    if not isinstance(rec, dict):
        return {'match': False, 'problems': ['not_a_json_object'], 'alerts': [], 'drat_claim': False,
                'lrat_only_claim': False, 'fields': {}}
    probs, alerts = [], []
    expected_cnf = 'cases19skel/cnf/%s.cnf' % tag
    if rec.get('tag') != tag:
        probs.append('tag_field')
    rh = rec.get('cnf_sha256')
    if rh is None:
        probs.append('no_cnf_sha256')
    elif rh != built['cnf_sha256']:
        probs.append('cnf_sha256_mismatch')
    if 'cnf_bytes' in rec and rec['cnf_bytes'] != built['cnf_bytes']:
        probs.append('cnf_bytes')
    if cls in ('pass1', 'archive_pass0_sample'):
        for k in ('vars', 'clauses'):
            if rec.get(k) != built[k]:
                probs.append(k)
        if rec.get('multiset') != mi:
            probs.append('multiset')
    if cls in ('pass1', 'proofcheck', 'archive_proofcheck_kill') and rec.get('cnf') != expected_cnf:
        probs.append('cnf_path')
    if cls == 'proofstream' and rec.get('cnf_file') != expected_cnf:
        probs.append('cnf_path')
    for flag in ('cnf_matches_pass1', 'cnf_matches_pass1_sha'):
        if flag in rec and rec[flag] is not True:
            probs.append('worker_%s_not_true' % flag)
    if 'SAT' in (rec.get('status'), rec.get('pass1_status')) or rec.get('kissat_rc') == 10 or rec.get('solver_rc') == 10:
        alerts.append('SAT_recorded')
    drat = lrat = False
    if cls == 'proofcheck':
        drat = rec.get('kissat_rc') == 20 and rec.get('drat_trim_verified') is True
    elif cls in ('proofstream', 'hard5'):
        drat = rec.get('status') == 'UNSAT' and rec.get('drat_trim_verified') is True
    elif cls == 'hard':
        lrat = rec.get('status') == 'UNSAT' and rec.get('checked') is True and rec.get('lrat_verified') is True
    return {'recorded_cnf_sha256': rh, 'match': rh == built['cnf_sha256'], 'problems': probs, 'alerts': alerts,
            'drat_claim': drat, 'lrat_only_claim': lrat, 'fields': {k: rec[k] for k in KEEP if k in rec}}


def extra_classes(discovered):
    return tuple(('unclassified:' + d, d + '/{}.json', 'unclassified')
                 for d, v in sorted(discovered.items()) if v['kind'] == 'unclassified')


def discover_dirs():
    found = {}
    for root, dirs, files in os.walk(L):
        dirs.sort()
        n = sum(1 for f in files if TAG_JSON.match(f))
        if n:
            d = os.path.relpath(root, L)
            ex = [r for p, r in EXCLUDED.items() if d.startswith(p)]
            kind = 'known' if d in KNOWN_DIRS else ('excluded' if ex else 'unclassified')
            found[d] = {'tag_json_files': n, 'kind': kind, **({'reason': ex[0]} if ex else {})}
    return found


def look(tag, mi, built, classes, pin_root, known=None):
    """Read every candidate record once; with `known` (final sweep) keep only new/changed versions."""
    entries, missing, disappeared = [], [], []
    for cls, tmpl, role in classes:
        r = tmpl.format(tag)
        data, rec, err, t = read_record(L / r)
        if err == 'missing':
            if known is not None and r in known:
                disappeared.append({'class': cls, 'path': r, 'checked_at': t})
            elif role in ('pass1', 'direct'):
                missing.append(r)
            continue
        rsha = sha(data)
        if known is not None and known.get(r) == rsha:
            continue
        e = {'class': cls, 'role': role, 'path': r, 'record_sha256': rsha, 'record_bytes': len(data), 'read_at': t}
        if pin_root is not None:
            dst = pin_root / r
            write_new(dst, data)
            e['pinned'] = rel(dst)
        if known is not None:
            e['event'] = 'changed' if r in known else 'new'
        if err:
            e.update({'match': False, 'problems': ['unparseable'], 'alerts': [], 'drat_claim': False,
                      'lrat_only_claim': False, 'fields': {}})
        else:
            e.update(evaluate(cls, rec, tag, mi, built))
        entries.append(e)
    return entries, missing, disappeared


def split_dirs(tag):
    return [d for d in ('cycle2/a3/' + tag, 'cycle2/part/' + tag) if (L / d).is_dir()]


def classify(entries, splits, spec_probs, gone=()):
    gone = set(gone)
    disc = []
    if spec_probs:
        disc.append({'path': 'spec', 'problems': spec_probs})
    if not any(e['role'] == 'pass1' for e in entries):
        disc.append({'path': 'pass1', 'problems': ['pass1_missing']})
    for e in entries:
        if e['role'] in ('pass1', 'direct', 'archived_direct') and e['problems']:
            disc.append({'path': e['path'], 'record_sha256': e['record_sha256'], 'problems': e['problems']})
    review = [{'path': e['path'], 'record_sha256': e['record_sha256'], 'problems': e['problems']}
              for e in entries if e['role'] == 'unclassified' and e['problems']]
    current = {}
    for e in entries:  # latest version per path; disappeared paths are not current
        if e['role'] == 'direct' and e['path'] not in gone:
            current[e['path']] = e
    drat = sorted(p for p, e in current.items() if e['drat_claim'] and not e['problems'])
    lrat = sorted(p for p, e in current.items() if e['lrat_only_claim'] and not e['problems'])
    status = 'FAIL' if disc else 'REVIEW' if review else 'PASS' if drat else 'PENDING'
    reasons = []
    if status == 'PENDING':
        if splits:
            reasons.append('split_obligation_separate')
        if lrat:
            reasons.append('lrat_check_only_direct_records')
        if current and not lrat:
            reasons.append('direct_records_without_drat_trim_unsat_claim')
        if not current:
            reasons.append('no_direct_proof_record')
    return status, reasons, disc, review, drat, lrat


def process_tag(row, ctx, pin_root):
    tag, mi = row['tag'], row['multiset']
    sb = (S / 'cases19skel' / 'specs' / (tag + '.json')).read_bytes()
    spec, ssha = json.loads(sb), sha(sb)
    try:
        live = sha((L / 'cases19skel' / 'specs' / (tag + '.json')).read_bytes())
    except FileNotFoundError:
        live = None
    sprob = spec_problems(spec, row, ctx['D'])
    if ctx['ppins'].get('cases19skel/specs/%s.json' % tag) != ssha:
        sprob.append('snapshot_spec_differs_from_parent_pin')
    try:
        built = build_cnf(ctx['mods'], spec)
    except Exception as e:  # the encoder rejects the frozen spec (e.g. its L assertion): a binding failure
        built = {'cnf_sha256': None, 'cnf_bytes': None, 'vars': None, 'clauses': None, 'build_seconds': None,
                 'build_error': repr(e)}
        sprob.append('build_error')
    entries, missing, _ = look(tag, mi, built, ctx['classes'], pin_root)
    out = {'type': 'tag', 'tag': tag, 'multiset': mi, 'skel': row['skel'], 'spec_sha256': ssha,
           'live_spec_sha256': live, 'live_spec_identical': live == ssha, 'spec_problems': sprob, **built,
           'records': entries, 'missing': missing, 'split_dirs': split_dirs(tag), 'checked_at': now()}
    p1 = [e for e in entries if e['role'] == 'pass1']
    if p1 and p1[0]['problems'] and built['cnf_sha256'] is not None:
        out['diagnostic_write_path_sha256'] = write_path_sha(ctx['mods'], spec)
    status, reasons, disc, review, _drat, _lrat = classify(entries, out['split_dirs'], sprob)
    out.update({'status_at_read': status, 'reasons_at_read': reasons, 'discrepancies': disc, 'review': review})
    return out


def context(srcdir):
    discovered = discover_dirs()
    return {'D': profiles(), 'ppins': parent_pins(), 'mods': load_modules(srcdir),
            'classes': CLASSES + extra_classes(discovered), 'discovered': discovered}


def cmd_dry(n):
    require_flags()
    ctx = context(S / 'src')
    _, idx = index_rows()
    for row in idx['cases'][:n]:
        o = process_tag(row, ctx, None)
        print(json.dumps(o, separators=(',', ':')), flush=True)


def compute_pins():
    """All reads and checks for `prepare`; returns (pins, files to pin). Writes nothing."""
    ppins = parent_pins()
    blobs = {name: (S / 'src' / name).read_bytes() for name in SRC_FILES}
    sources = {}
    for name, b in blobs.items():
        live = (L / 'src' / name).read_bytes()
        sources[name] = {'snapshot_path': repo_rel(S / 'src' / name), 'snapshot_sha256': sha(b),
                         'parent_pin_sha256': ppins.get('src/' + name), 'pinned_path': rel(PINNED / name),
                         'live_path': LANE_REL + '/src/' + name, 'live_sha256': sha(live), 'live_identical': live == b}
    ref = func_source(blobs['stream_check4.py'].decode(), 'cnf_bytes_of')
    serializer = {'pinned_function': ref, 'live_stream_check_variants': serializer_variants(ref),
                  'pass1_writer': {'function': 'encode_e1.CNF.write',
                                   'source': func_source(blobs['encode_e1.py'].decode(), 'write', 'CNF'),
                                   'note': 'pass 1 (run_cases.py) wrote the CNF with CNF.write; equality with '
                                           'cnf_bytes_of is tested only through the pass-1 hash comparison'}}
    sums = (L / 'SHA256SUMS-cycle1.txt').read_bytes()
    cyc = {'commit': CYCLE1_COMMIT, 'manifest_line': next((x for x in sums.decode().splitlines()
                                                          if x.endswith('src/encode_skel.py')), None)}
    g = subprocess.run(['git', '-C', str(REPO), 'show', '%s:%s/src/encode_skel.py' % (CYCLE1_COMMIT, LANE_REL)],
                       capture_output=True)
    cyc['git_show_rc'] = g.returncode
    if g.returncode == 0:
        cyc['git_blob_sha256'] = sha(g.stdout)
        cyc['unified_diff_cycle1_to_pinned'] = ''.join(difflib.unified_diff(
            g.stdout.decode().splitlines(True), blobs['encode_skel.py'].decode().splitlines(True),
            'cycle1:encode_skel.py', 'pinned:encode_skel.py'))
    isha, idx = index_rows()
    iprobs, counts = check_index(idx)
    psha = sha((S / 'data' / 'profiles-19-8-6.json').read_bytes())
    r4b = (PARENT / 'cover-binding-result.json').read_bytes()
    r4 = json.loads(r4b)
    wb = (L / 'cycle2' / 'binding-pass1.json').read_bytes()
    pins = {'recorded_at': now(), 'process': proc_info(), 'sources': sources, 'serializer': serializer,
            'encode_skel_cycle1': cyc,
            'index': {'snapshot_sha256': isha, 'parent_pin_sha256': ppins.get('cases19skel/index.json'),
                      'live_sha256': sha((L / 'cases19skel' / 'index.json').read_bytes()), 'problems': iprobs,
                      'counts': {'ms%02d' % k: v for k, v in counts.items()}},
            'profiles': {'snapshot_sha256': psha, 'parent_pin_sha256': ppins.get('data/profiles-19-8-6.json')},
            'parent_R4_receipt': {'path': repo_rel(PARENT / 'cover-binding-result.json'), 'sha256': sha(r4b),
                                  'verdict': r4.get('verdict'), 'R4_A2_bindings': r4.get('R4_A2_bindings')},
            'parent_pin_result_sha256': sha((PARENT / 'pin-result.json').read_bytes()),
            'worker_binding_claim': {'pinned': rel(PINNED_LANE / 'cycle2' / 'binding-pass1.json'), 'sha256': sha(wb),
                                     'summary': json.loads(wb).get('summary')},
            'record_classes': [{'class': c, 'path': t, 'role': r} for c, t, r in CLASSES],
            'excluded_prefixes': EXCLUDED, 'discovered_dirs': discover_dirs(), 'free_bytes': free_bytes()}
    files = {PINNED / name: b for name, b in blobs.items()}
    files[PINNED_LANE / 'SHA256SUMS-cycle1.txt'] = sums
    files[PINNED_LANE / 'cycle2' / 'binding-pass1.json'] = wb
    pins['ok'] = (not iprobs and all(v['snapshot_sha256'] == v['parent_pin_sha256'] for v in sources.values())
                  and isha == ppins.get('cases19skel/index.json') and psha == ppins.get('data/profiles-19-8-6.json')
                  and r4.get('verdict') == 'PASS')
    return pins, files


def cmd_prepare():
    require_flags()
    pins, files = compute_pins()
    PINNED.mkdir(exist_ok=False)
    for p, b in files.items():
        write_new(p, b)
        if p.read_bytes() != b:
            raise SystemExit('pin read-back differs: ' + rel(p))
    for name in SRC_FILES:
        v = pins['sources'][name]
        v['pinned_sha256'] = sha((PINNED / name).read_bytes())
        v['pinned_bytes_identical'] = v['pinned_sha256'] == v['snapshot_sha256']
    pins['pinned_lane_files'] = {rel(p): sha(b) for p, b in files.items() if PINNED_LANE in p.parents}
    pins['ok'] = pins['ok'] and all(pins['sources'][n]['pinned_bytes_identical'] for n in SRC_FILES)
    dump_new(PINS, pins)
    CHUNKS.mkdir(exist_ok=False)
    print(json.dumps({'ok': pins['ok'], 'sources': {n: (v['snapshot_sha256'], v['live_identical'])
                                                    for n, v in pins['sources'].items()},
                      'index_problems': pins['index']['problems'],
                      'serializer_variants': pins['serializer']['live_stream_check_variants'],
                      'cycle1_git_blob': pins['encode_skel_cycle1'].get('git_blob_sha256'),
                      'discovered': pins['discovered_dirs']}, indent=1))


def done_tags():
    done = set()
    for _p, raw_all in load_chunks():
        for raw in raw_all.splitlines():
            try:
                o = json.loads(raw)
            except ValueError:
                continue
            if o.get('type') == 'tag':
                done.add(o['tag'])
    return done


def on_term(signum, _frame):
    STOP.append(signum)


def cmd_run(argv):
    require_flags()
    max_min, max_tags, stop_mm = 170.0, None, False
    it = iter(argv)
    for a in it:
        if a == '--max-minutes':
            max_min = min(float(next(it)), 175.0)
        elif a == '--max-tags':
            max_tags = int(next(it))
        elif a == '--stop-on-mismatch':
            stop_mm = True
        else:
            raise SystemExit('unknown argument ' + a)
    _psha, pins = load_pins()
    if not pins['ok']:
        raise SystemExit('pins.json not ok')
    for name in SRC_FILES:
        if sha((PINNED / name).read_bytes()) != pins['sources'][name]['pinned_sha256']:
            raise SystemExit('pinned source changed: ' + name)
    isha, idx = index_rows()
    if isha != pins['index']['snapshot_sha256']:
        raise SystemExit('snapshot index changed')
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    ctx = context(PINNED)
    done = done_tags()
    todo = [r for r in idx['cases'] if r['tag'] not in done]
    cdir = next_dir(CHUNKS, 'chunk-%03d')
    t0, last = time.time(), time.time()
    with open(cdir / 'progress.jsonl', 'x', buffering=1) as prog:
        def emit(o):
            prog.write(json.dumps(o, separators=(',', ':')) + '\n')
            prog.flush()
        emit({'type': 'start', 'host_time': now(), 'chunk': rel(cdir), 'process': proc_info(),
              'pinned_sources': {n: pins['sources'][n]['pinned_sha256'] for n in SRC_FILES},
              'modules': {n: m.__file__ for n, m in ctx['mods'].items()}, 'index_sha256': isha,
              'discovered_dirs': ctx['discovered'], 'done_before': len(done), 'todo': len(todo),
              'limits': {'max_minutes': max_min, 'max_tags': max_tags, 'stop_on_mismatch': stop_mm,
                         'free_floor': FREE_FLOOR, 'rss_cap': RSS_CAP}, 'free_bytes': free_bytes()})
        n, counts, fails, reason = 0, {}, [], 'complete'
        pin_root = cdir / 'records'
        for row in todo:
            if STOP:
                reason = 'signal_%d' % STOP[0]
            elif time.time() - t0 > max_min * 60:
                reason = 'deadline'
            elif max_tags is not None and n >= max_tags:
                reason = 'max_tags'
            elif free_bytes() < FREE_FLOOR:
                reason = 'free_floor'
            elif usage()['maxrss_bytes'] > RSS_CAP:
                reason = 'rss_cap'
            if reason != 'complete':
                break
            o = process_tag(row, ctx, pin_root)
            emit(o)
            n += 1
            counts[o['status_at_read']] = counts.get(o['status_at_read'], 0) + 1
            if o['status_at_read'] in ('FAIL', 'REVIEW'):
                fails.append(o['tag'])
                print(now(), 'DISCREPANCY', o['tag'], json.dumps(o['discrepancies'] + o['review']), flush=True)
                if stop_mm:
                    reason = 'stop_on_mismatch'
                    break
            if time.time() - last >= CHECKPOINT_S:
                last = time.time()
                ck = {'type': 'checkpoint', 'host_time': now(), 'done_in_chunk': n, 'done_total': len(done) + n,
                      'elapsed_s': round(last - t0, 1), **usage(), 'free_bytes': free_bytes(), 'counts': counts,
                      'fail_or_review_tags': fails, 'last_tag': o['tag']}
                emit(ck)
                print(json.dumps(ck), flush=True)
        end = {'type': 'end', 'host_time': now(), 'reason': reason, 'done_in_chunk': n, 'done_total': len(done) + n,
               'elapsed_s': round(time.time() - t0, 1), **usage(), 'free_bytes': free_bytes(), 'counts': counts,
               'fail_or_review_tags': fails}
        emit(end)
    print(json.dumps(end), flush=True)
    if reason == 'complete':
        return 0
    return 3 if reason == 'stop_on_mismatch' else 4 if reason in ('free_floor', 'rss_cap') else 2


def cmd_finalize():
    require_flags()
    t0 = time.time()
    psha, pins = load_pins()
    isha, idx = index_rows()
    rows = idx['cases']
    lines, chunks, seen_dirs = {}, [], {}
    for p, raw_all in load_chunks():
        meta = {'progress': rel(p), 'sha256': sha(raw_all), 'tags': 0, 'checkpoints': [], 'unparsed_lines': 0}
        for raw in raw_all.splitlines():
            try:
                o = json.loads(raw)
            except ValueError:
                meta['unparsed_lines'] += 1
                continue
            t = o.get('type')
            if t == 'tag':
                if o['tag'] in lines:
                    raise SystemExit('duplicate tag ' + o['tag'])
                lines[o['tag']] = o
                meta['tags'] += 1
            elif t == 'start':
                meta['start'] = {k: o[k] for k in ('host_time', 'process', 'pinned_sources', 'modules', 'index_sha256',
                                                   'done_before', 'todo', 'limits', 'free_bytes')}
                for d, v in o['discovered_dirs'].items():
                    if v['kind'] == 'unclassified':
                        seen_dirs[d] = v
            elif t == 'end':
                meta['end'] = o
            elif t == 'checkpoint':
                meta['checkpoints'].append({k: o[k] for k in ('host_time', 'done_total', 'elapsed_s', 'maxrss_bytes',
                                                              'free_bytes')})
        chunks.append(meta)
    absent = [r['tag'] for r in rows if r['tag'] not in lines]
    if absent:
        raise SystemExit('incomplete: %d tags not processed (first %s)' % (len(absent), absent[0]))
    discovered = discover_dirs()
    classes = CLASSES + extra_classes({**seen_dirs, **discovered})
    sweep = next_dir(HERE, 'final-sweep-%03d')
    sweep_started = now()
    per_tag, sweep_events, alerts, mism = [], [], [], []
    for row in rows:
        o = lines[row['tag']]
        tag, mi = o['tag'], o['multiset']
        built = {k: o[k] for k in ('cnf_sha256', 'cnf_bytes', 'vars', 'clauses')}
        known = {e['path']: e['record_sha256'] for e in o['records']}
        new, missing, gone = look(tag, mi, built, classes, sweep / 'records', known)
        for e in new:
            sweep_events.append({'tag': tag, 'path': e['path'], 'event': e['event'], 'match': e['match'],
                                 'problems': e['problems'], 'record_sha256': e['record_sha256']})
        for g in gone:
            sweep_events.append({'tag': tag, 'path': g['path'], 'event': 'disappeared', 'checked_at': g['checked_at']})
        entries = o['records'] + new
        gone_set = {g['path'] for g in gone}
        splits = split_dirs(tag)
        status, reasons, disc, review, drat, lrat = classify(entries, splits, o['spec_problems'], gone_set)
        for e in entries:
            for a in e['alerts']:
                alerts.append({'tag': tag, 'path': e['path'], 'alert': a})
            if e['problems']:
                mism.append({'tag': tag, 'path': e['path'], 'role': e['role'], 'record_sha256': e['record_sha256'],
                             'problems': e['problems'], 'recorded_cnf_sha256': e.get('recorded_cnf_sha256')})
        latest = {}
        for e in entries:
            latest[e['path']] = e
        p1s = [e for e in entries if e['role'] == 'pass1']
        per_tag.append({
            'tag': tag, 'multiset': mi, 'skel': o['skel'], 'spec_sha256': o['spec_sha256'],
            'cnf_sha256': o['cnf_sha256'], 'cnf_bytes': o['cnf_bytes'], 'vars': o['vars'], 'clauses': o['clauses'],
            'pass1_status': p1s[-1]['fields'].get('status') if p1s else None, 'status': status, 'reasons': reasons,
            'matching': sorted(p for p, e in latest.items() if e['match'] and not e['problems'] and p not in gone_set
                               and e['role'] != 'archived_informational'),
            'mismatching': disc + review, 'missing': missing,
            'drat_claim_records': drat, 'lrat_only_records': lrat, 'split_dirs': splits,
            'informational': [{'path': e['path'], 'match': e['match'], 'problems': e['problems']}
                              for e in entries if e['role'] == 'archived_informational'],
            'disappeared': sorted(gone_set), 'live_spec_identical': o['live_spec_identical'],
            'record_versions': len(entries), 'checked_at': o['checked_at']})
    sweep_ended = now()
    # end-of-run freeze verification of sources, serializer variants, index and specs
    end_sources = {name: {'snapshot_sha256': sha((S / 'src' / name).read_bytes()),
                          'pinned_sha256': sha((PINNED / name).read_bytes()),
                          'live_sha256': sha((L / 'src' / name).read_bytes())} for name in SRC_FILES}
    ref = func_source((PINNED / 'stream_check4.py').read_text(), 'cnf_bytes_of')
    spec_now = {'snapshot_changed': [], 'live_differs': [], 'live_missing': []}
    for t in per_tag:
        tag = t['tag']
        if sha((S / 'cases19skel' / 'specs' / (tag + '.json')).read_bytes()) != t['spec_sha256']:
            spec_now['snapshot_changed'].append(tag)
        try:
            if sha((L / 'cases19skel' / 'specs' / (tag + '.json')).read_bytes()) != t['spec_sha256']:
                spec_now['live_differs'].append(tag)
        except FileNotFoundError:
            spec_now['live_missing'].append(tag)
    freeze = {'checked_at': now(), 'sources': end_sources, 'serializers': serializer_variants(ref),
              'index': {'snapshot_sha256': isha, 'live_sha256': sha((L / 'cases19skel' / 'index.json').read_bytes())},
              'specs': spec_now, 'parent_R4_receipt_sha256': sha((PARENT / 'cover-binding-result.json').read_bytes())}
    freeze['sources_ok'] = (isha == pins['index']['snapshot_sha256'] and not spec_now['snapshot_changed'] and
                            all(v['snapshot_sha256'] == v['pinned_sha256'] == pins['sources'][n]['pinned_sha256']
                                for n, v in end_sources.items()))
    # pinned record manifest (sha256sum format, paths relative to this directory), read back from disk
    man = []
    for root in sorted(list(CHUNKS.glob('chunk-*/records')) + [sweep / 'records']):
        if root.is_dir():
            for p in sorted(x for x in root.rglob('*') if x.is_file()):
                man.append('%s  %s\n' % (sha(p.read_bytes()), rel(p)))
    man_bytes = ''.join(man).encode()
    write_new(MANIFEST, man_bytes)
    per_ms = {}
    for t in per_tag:
        m = per_ms.setdefault('ms%02d' % t['multiset'], {'cases': 0, **{s: 0 for s in STATUSES}, 'pending_reasons': {},
                                                          'pass1_status': {}, 'with_split_dirs': 0})
        m['cases'] += 1
        m[t['status']] += 1
        for r in t['reasons']:
            m['pending_reasons'][r] = m['pending_reasons'].get(r, 0) + 1
        m['pass1_status'][t['pass1_status']] = m['pass1_status'].get(t['pass1_status'], 0) + 1
        m['with_split_dirs'] += bool(t['split_dirs'])
    rec_counts = {}
    for row in rows:
        for e in lines[row['tag']]['records']:
            c = rec_counts.setdefault(e['class'], {'records': 0, 'match': 0, 'with_problems': 0, 'drat_claim': 0,
                                                   'lrat_only_claim': 0})
            c['records'] += 1
            c['match'] += bool(e['match'])
            c['with_problems'] += bool(e['problems'])
            c['drat_claim'] += bool(e['drat_claim'])
            c['lrat_only_claim'] += bool(e['lrat_only_claim'])
    totals = {s: sum(1 for t in per_tag if t['status'] == s) for s in STATUSES}
    pend = {}
    for t in per_tag:
        for r in t['reasons']:
            pend[r] = pend.get(r, 0) + 1
    base_bound = sum(1 for t in per_tag if 'cases19skel/results/%s.json' % t['tag'] in t['matching'])
    fail = [t['tag'] for t in per_tag if t['status'] == 'FAIL']
    review = [t['tag'] for t in per_tag if t['status'] == 'REVIEW']
    drivers = {c['start']['process']['driver_sha256'] for c in chunks if 'start' in c}
    same_driver = drivers == {driver_sha()} and pins['process']['driver_sha256'] == driver_sha()
    verdict = ('FAIL' if fail else
               'REVIEW' if review or alerts or not (freeze['sources_ok'] and pins['ok'] and same_driver) else
               'PASS' if totals['PASS'] == len(per_tag) else 'PASS_WITH_PENDING')
    wsum = pins['worker_binding_claim']['summary'] or {}
    files_bytes = alloc = nfiles = 0
    for p in HERE.rglob('*'):
        if p.is_file():
            st = p.stat()
            nfiles += 1
            files_bytes += st.st_size
            alloc += st.st_blocks * 512
    cpu_u = sum(c.get('end', {}).get('cpu_user_s', 0) for c in chunks)
    cpu_s = sum(c.get('end', {}).get('cpu_sys_s', 0) for c in chunks)
    result = {
        'title': 'PA(19,8,6) R5 parent replay: 5577 non-balanced M1 base CNFs bound to frozen specs and records',
        'scope': ('Binding only. encode_skel.build(spec) from the pinned snapshot, serialized with '
                  'stream_check4.cnf_bytes_of, hashed in memory, compared with the recorded cnf_sha256 (and '
                  'vars/clauses/cnf_bytes/path/tag/multiset metadata) of the pass-1 record and every later direct '
                  'record for that tag. Split f/batch records are a separate obligation (not compared).'),
        'not_claimed': ('No UNSAT correctness, proof validity, solver or checker soundness, cover completeness, '
                        'or PA(19,8,6) nonexistence claim. drat_claim flags are worker-recorded fields only.'),
        'started': chunks[0]['start']['host_time'] if chunks and 'start' in chunks[0] else None,
        'finalized': now(),
        'driver': {'path': rel(Path(__file__).resolve()), 'sha256': driver_sha(),
                   'prepare_driver_sha256': pins['process']['driver_sha256'], 'chunk_driver_sha256': sorted(drivers),
                   'same_driver_prepare_chunks_finalize': same_driver},
        'commands': [{'chunk': c['progress'], 'progress_sha256': c['sha256'], 'tags': c['tags'],
                      'orig_argv': c.get('start', {}).get('process', {}).get('orig_argv'),
                      'cwd': c.get('start', {}).get('process', {}).get('cwd'),
                      'nice': c.get('start', {}).get('process', {}).get('nice'),
                      'started': c.get('start', {}).get('host_time'), 'ended': c.get('end', {}).get('host_time'),
                      'end_reason': c.get('end', {}).get('reason'), 'elapsed_s': c.get('end', {}).get('elapsed_s'),
                      'cpu_user_s': c.get('end', {}).get('cpu_user_s'), 'cpu_sys_s': c.get('end', {}).get('cpu_sys_s'),
                      'maxrss_bytes': c.get('end', {}).get('maxrss_bytes'), 'checkpoints': c['checkpoints'],
                      'unparsed_lines': c['unparsed_lines']} for c in chunks],
        'prepare_command': pins['process'],
        'finalize_command': proc_info(),
        'pins': {'path': rel(PINS), 'sha256': psha, 'ok': pins['ok'], 'sources': pins['sources'],
                 'serializer_variants': pins['serializer']['live_stream_check_variants'],
                 'encode_skel_cycle1': pins['encode_skel_cycle1'], 'index': pins['index'], 'profiles': pins['profiles'],
                 'parent_R4_receipt': pins['parent_R4_receipt'],
                 'parent_pin_result_sha256': pins['parent_pin_result_sha256'],
                 'pinned_lane_files': pins.get('pinned_lane_files')},
        'freeze_check_at_finalize': freeze,
        'record_classes': [{'class': c, 'path': t, 'role': r} for c, t, r in classes],
        'excluded_prefixes': EXCLUDED,
        'status_rules': {
            'FAIL': 'spec identity problem, pass-1 record missing/unparseable, or any pass1/direct/archived_direct '
                    'record (any version seen) whose cnf_sha256 or compared metadata differs from the rebuild',
            'REVIEW': 'only an unclassified tag-named record dir disagrees',
            'PASS': 'no discrepancy, pass-1 binds, and a current direct record that binds carries a worker-recorded '
                    'drat-trim UNSAT claim (proofcheck: kissat_rc 20 and drat_trim_verified; proofstream/hard5: '
                    'status UNSAT and drat_trim_verified)',
            'PENDING': 'no discrepancy, but no bound current direct drat-trim claim (missing proof is not a hash failure)',
            'verdict': 'FAIL if any FAIL tag; REVIEW if any REVIEW tag, any alert (e.g. SAT recorded), pins not ok, '
                       'source freeze broken or driver hash changed; PASS if all tags PASS; else PASS_WITH_PENDING'},
        'discovered_record_dirs_at_finalize': discovered,
        'final_sweep': {'dir': rel(sweep), 'started': sweep_started, 'ended': sweep_ended, 'events': sweep_events},
        'counts': {'cases': len(per_tag), **totals, 'pending_reasons': pend,
                   'base_cnf_bound_to_pass1': base_bound, 'live_spec_differs': len(spec_now['live_differs'])},
        'counts_per_multiset': per_ms,
        'record_counts_main_pass': rec_counts,
        'mismatching_records': mism,
        'alerts': alerts,
        'worker_binding_claim_crosscheck': {
            'pinned': pins['worker_binding_claim']['pinned'], 'sha256': pins['worker_binding_claim']['sha256'],
            'summary': wsum, 'worker_says_all_pass1_bound': wsum.get('a2_mismatches') == 0 and
            wsum.get('a2_cases_rederived') == 5577, 'parent_all_pass1_bound': base_bound == len(per_tag)},
        'pinned_records': {'manifest': rel(MANIFEST), 'manifest_sha256': sha(man_bytes), 'files': len(man)},
        'resources': {'chunk_cpu_user_s': round(cpu_u, 2), 'chunk_cpu_sys_s': round(cpu_s, 2),
                      'chunk_max_rss_bytes': max((c.get('end', {}).get('maxrss_bytes', 0) for c in chunks), default=0),
                      'finalize': {**usage(), 'elapsed_s': round(time.time() - t0, 1)},
                      'output_files_before_result': nfiles, 'output_bytes_before_result': files_bytes,
                      'output_allocated_bytes_before_result': alloc, 'free_bytes_at_finalize': free_bytes(),
                      'free_floor': FREE_FLOOR, 'maxrss_unit': 'bytes'},
        'verdict': verdict,
        'fail_tags': fail, 'review_tags': review,
        'pending_tags': [t['tag'] for t in per_tag if t['status'] == 'PENDING'],
        'per_tag': per_tag,
    }
    dump_new(RESULT, result)
    print(json.dumps({'verdict': verdict, 'counts': result['counts'], 'mismatching': len(mism), 'alerts': len(alerts),
                      'sweep_events': len(sweep_events), 'freeze_sources_ok': freeze['sources_ok'],
                      'same_driver': same_driver, 'live_spec_differs': len(spec_now['live_differs'])}, indent=1))
    return 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'dry':
        cmd_dry(int(sys.argv[2]))
    elif cmd == 'prepare':
        cmd_prepare()
    elif cmd == 'run':
        sys.exit(cmd_run(sys.argv[2:]))
    elif cmd == 'finalize':
        sys.exit(cmd_finalize())
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
