"""Parent replay of the 122 strictly rebound K5 root DRAT proofs (phys-1 lane moqls8; C11 root replay only).

Scope: for each of the 122 ledger-v003 CERTIFIED depth-1 roots, check the retained compressed DRAT proof against exactly
base CNF + that root's 7 unit clauses with the parent-pinned drat-trim build (SHA a46c0c71...8e37).  NOT whole-K5
acceptance: the 6 UNKNOWN roots are never replayed or accepted; the root cover itself is out of scope.

Phases (each creates a fresh exclusive attempt directory <phase>-aN/ inside this directory; nothing is overwritten):
  pin       exclusive copies of small lane metadata; cross-binding of ledger v003, strict receipts, retained-proof
            manifest + sidecar and old worker receipts; ONE full SHA-256 + strict structural validation of the base CNF;
            checker SHA.                                               -> pin-aN/PIN.json
  controls  scientific smoke controls through the same run_case() stream path. -> controls-aN/CONTROLS.json
  corpus    one receipt + raw checker stdout/stderr per root, ascending proof size; stops at the first non-PASS root.
  final     aggregate over all corpus attempts (latest attempt per root decisive) -> final-aN/FINAL.json

Stream path (exactly two busy processes: this Python process and one native drat-trim):
  leaf CNF  = b'p cnf V C+k\\n' + base body bytes (everything after the first line, unchanged) + b'<lit> 0\\n' per root
              literal in ledger order, written to an anonymous pipe that drat-trim opens as argv[1] = /dev/fd/N;
  proof     = retained .drat.zst read in chunks (SHA-256 of the compressed bytes), decompressed in-process with stdlib
              compression.zstd (multi-frame aware; truncation is an error), SHA-256 of the decompressed bytes both as
              produced and as delivered, written to drat-trim stdin; checker argv: drat-trim /dev/fd/N -i -t <limit>.
  Both pipes are non-blocking and multiplexed with select(); the child is reaped with wait4 (exact ru_maxrss); child
  and own RSS are sampled through libproc PROC_PIDTASKINFO; RSS guard / wall watchdog -> SIGTERM + bounded wait.
  No SIGKILL, no subprocess timeouts, no helper processes, no files outside this directory, nothing in /tmp.

Usage:  /opt/homebrew/bin/python3 -B k5_root_replay_v1.py {pin|controls|corpus [--retry ID,ID]|final}
"""
from __future__ import annotations

import ctypes
import datetime
import hashlib
import json
import os
import platform
import re
import resource
import select
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import compression.zstd as zstd

RUN = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16')
HERE = RUN / 'review' / 'moqls8-k5-root-parent-replay-v1'
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
K5 = LANE / 'evidence' / 'k5_split_v1'
BASE = LANE / 'evidence' / 'gram_dev_v1' / 'GA5L_K5_sb2.cnf'
DT = RUN / 'review' / 'moqls7-parent-proofcheck-v1' / 'drat-trim'

DT_SHA = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
BASE_SHA = '6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b'
BASE_BYTES = 137664569
BASE_VARS = 509915
BASE_CLAUSES = 5740230
ROOT_UNITS = 7
LEDGER_SHA = 'b9b3fc67fe5abdf6be197b7cb642226bc1c5f344348edb068b6388c02bc8b14b'
MANIFEST_SHA = '65f6e0dd47c582b108906aa808e3d2453ec45ac3b8bbfa19c01e586e989c3b5e'
SIDECAR_SHA = '4e10981379f7858c18b2611e000036eb1ca9239f24d41a44db20e12cceec9ca5'
MANIFEST_TOTAL_ZST_BYTES = 444419127
UNKNOWN_ROOTS = ('c016', 'c032', 'c048', 'c064', 'c080', 'c096')
N_ROOTS = 122

PINNED = (  # (name in pin dir, lane-relative source, expected SHA-256 or None = record only)
    ('LEDGER.v003.json', 'evidence/k5_split_v1/ledger/LEDGER.v003.json', LEDGER_SHA),
    ('strict_L1.RESULTS.jsonl', 'evidence/k5_split_v1/strict_L1/RESULTS.jsonl', None),
    ('strict_L1.META.1792275624.json', 'evidence/k5_split_v1/strict_L1/META.1792275624.json', None),
    ('RETAINED_ROOT_PROOFS_MANIFEST_v1.json', 'evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.json', MANIFEST_SHA),
    ('RETAINED_ROOT_PROOFS_MANIFEST_v1.sha256', 'evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.sha256',
     SIDECAR_SHA),
    ('all.RESULTS.jsonl', 'evidence/k5_split_v1/all/RESULTS.jsonl', None),
    ('pilot.RESULTS.jsonl', 'evidence/k5_split_v1/pilot/RESULTS.jsonl', None),
)

CHUNK = 1 << 20
T_NATIVE = 1500             # drat-trim -t: seconds since checker start; on expiry prints 's TIMEOUT' and exits 0
WALL_LIMIT = 1700.0         # per-case wall watchdog -> SIGTERM (keeps every case below the 30 min checkpoint bound)
STOP_GRACE = 60.0           # bounded wait after SIGTERM; SIGKILL is never sent
SAMPLE_S = 0.05
RSS_GUARD = int(1.40 * 2 ** 30)   # sampled aggregate (checker + this process) guard
RSS_HARD = int(1.50 * 2 ** 30)    # assigned ceiling: exact child ru_maxrss + own lifetime ru_maxrss must stay below
FREE_FLOOR = 12_000_000_000
FREE_MARGIN = 500_000_000
NEWDATA_CAP = 256 * 2 ** 20
STDOUT_READ_CAP = 64 * 2 ** 20

RUNNER_PATH = Path(__file__).resolve()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(CHUNK), b''):
            h.update(b)
    return h.hexdigest()


RUNNER_SHA = sha_file(RUNNER_PATH)


def write_new(path, data):
    with open(path, 'xb') as f:
        f.write(data)


def write_json_new(path, obj):
    write_new(path, (json.dumps(obj, indent=1) + '\n').encode())


def runner_identity():
    return {'path': str(RUNNER_PATH), 'sha256': RUNNER_SHA, 'argv': sys.argv, 'python': sys.executable,
            'python_realpath': os.path.realpath(sys.executable), 'python_version': sys.version,
            'zstd_version': getattr(zstd, 'zstd_version', None), 'platform': platform.platform(), 'pid': os.getpid()}


def attempt_dirs(prefix):
    ds = [p for p in HERE.glob(prefix + '-a*') if p.is_dir() and p.name[len(prefix) + 2:].isdigit()]
    return sorted(ds, key=lambda p: int(p.name[len(prefix) + 2:]))


def new_attempt(prefix):
    for n in range(1, 1000):
        d = HERE / ('%s-a%d' % (prefix, n))
        try:
            d.mkdir()
            return d
        except FileExistsError:
            continue
    raise SystemExit('no free attempt slot for ' + prefix)


def latest_ok(prefix, fname, ok):
    best = None
    for d in attempt_dirs(prefix):
        f = d / fname
        if f.is_file():
            obj = json.loads(f.read_bytes())
            if ok(obj):
                best = (d, obj)
    if best is None:
        raise SystemExit('no successful %s attempt usable by runner %s' % (prefix, RUNNER_SHA))
    return best


def dir_bytes(d):
    total = 0
    for root, _, files in os.walk(d):
        for name in files:
            total += os.lstat(os.path.join(root, name)).st_size
    return total


# ---------------------------------------------------------------- libproc RSS sampling (no helper processes)
class _TaskInfo(ctypes.Structure):
    _fields_ = ([(n, ctypes.c_uint64) for n in ('virtual_size', 'resident_size', 'total_user', 'total_system',
                                                'threads_user', 'threads_system')] +
                [(n, ctypes.c_int32) for n in ('policy', 'faults', 'pageins', 'cow_faults', 'messages_sent',
                                               'messages_received', 'syscalls_mach', 'syscalls_unix', 'csw',
                                               'threadnum', 'numrunning', 'priority')])


_LIBPROC = ctypes.CDLL('/usr/lib/libproc.dylib', use_errno=True)
_LIBPROC.proc_pidinfo.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int]
_LIBPROC.proc_pidinfo.restype = ctypes.c_int
PROC_PIDTASKINFO = 4


def rss_of(pid):
    ti = _TaskInfo()
    n = _LIBPROC.proc_pidinfo(pid, PROC_PIDTASKINFO, 0, ctypes.byref(ti), ctypes.sizeof(ti))
    return int(ti.resident_size) if n == ctypes.sizeof(ti) else None


# ---------------------------------------------------------------- base CNF validation (done once per base)
HEADER_RE = re.compile(rb'p cnf ([1-9][0-9]*) ([1-9][0-9]*)\n')
LINE_RE = re.compile(rb'(?:-?[1-9][0-9]* )+0')
DIGITS_RE = re.compile(rb'[0-9]+')


class BaseInvalid(Exception):
    pass


def validate_base(path):
    """Single pass: SHA-256 of the file and of its body, plus strict DIMACS structure: first line exactly
    'p cnf V C\\n' (canonical decimals); then exactly C lines, each one or more canonical nonzero decimal literals
    (|lit| <= V) separated by single spaces and terminated by ' 0\\n'; no comments, blank lines, octal-looking
    tokens, other whitespace or trailing bytes.  Guarantees drat-trim (fscanf %i) reads exactly these C clauses."""
    t0 = time.monotonic()
    h_all, h_body = hashlib.sha256(), hashlib.sha256()
    with open(path, 'rb') as f:
        header = f.readline(4096)
        m = HEADER_RE.fullmatch(header)
        if not m:
            raise BaseInvalid('header is not exactly "p cnf V C\\n": %r' % header[:80])
        nvars, nclauses = int(m.group(1)), int(m.group(2))
        h_all.update(header)
        lines = lit_occ = maxvar = body_bytes = 0
        carry = b''
        while True:
            b = f.read(8 * CHUNK)
            if not b:
                break
            h_all.update(b)
            h_body.update(b)
            body_bytes += len(b)
            block = carry + b
            cut = block.rfind(b'\n')
            if cut < 0:
                carry = block
                continue
            carry = block[cut + 1:]
            complete = block[:cut]
            for line in complete.split(b'\n'):
                if not LINE_RE.fullmatch(line):
                    raise BaseInvalid('malformed clause line %d: %r' % (lines + 1, line[:80]))
                lines += 1
            lit_occ += complete.count(b' ')
            maxvar = max(maxvar, max(map(int, DIGITS_RE.findall(complete)), default=0))
        if carry:
            raise BaseInvalid('file does not end with a newline-terminated clause line')
    if lines != nclauses:
        raise BaseInvalid('clause lines %d != header clauses %d' % (lines, nclauses))
    if maxvar > nvars:
        raise BaseInvalid('literal magnitude %d exceeds header vars %d' % (maxvar, nvars))
    return {'path': str(path), 'sha256': h_all.hexdigest(), 'bytes': len(header) + body_bytes,
            'header': header.decode('ascii'), 'nvars': nvars, 'nclauses': nclauses,
            'body_sha256': h_body.hexdigest(), 'body_bytes': body_bytes, 'clause_lines': lines,
            'literal_occurrences': lit_occ, 'max_var_seen': maxvar, 'validated_at': now(),
            'validation_s': round(time.monotonic() - t0, 2)}


# ---------------------------------------------------------------- pin phase
def build_plan(d, P):
    def req(cond, msg):
        if not cond:
            P.append(msg)
        return bool(cond)

    ledger = json.loads((d / 'LEDGER.v003.json').read_bytes())
    manifest = json.loads((d / 'RETAINED_ROOT_PROOFS_MANIFEST_v1.json').read_bytes())
    sidecar = (d / 'RETAINED_ROOT_PROOFS_MANIFEST_v1.sha256').read_text()

    def jsonl(name):
        out = {}
        for line in (d / name).read_bytes().split(b'\n'):
            if line:
                h = sha_bytes(line)
                req(h not in out, 'duplicate line in ' + name)
                out[h] = json.loads(line)
        return out

    strict = jsonl('strict_L1.RESULTS.jsonl')
    old = {'all/RESULTS.jsonl': jsonl('all.RESULTS.jsonl'), 'pilot/RESULTS.jsonl': jsonl('pilot.RESULTS.jsonl')}
    req(ledger.get('schema') == 'k5-cover-ledger/1' and ledger.get('version') == 3, 'ledger schema/version')
    req(ledger.get('base_cnf_sha256') == BASE_SHA, 'ledger base sha')
    req(ledger.get('base_vars') == BASE_VARS and ledger.get('base_clauses') == BASE_CLAUSES, 'ledger base dims')
    chain1 = (ledger.get('chain') or {}).get('1') or []
    req(len(chain1) == ROOT_UNITS and len(set(chain1)) == ROOT_UNITS and
        all(type(v) is int and 0 < v <= BASE_VARS for v in chain1), 'ledger chain[1] shape')
    leaves = ledger.get('leaves') or []
    req([x.get('id') for x in leaves] == ['c%03d' % i for i in range(128)], 'ledger leaves are not c000..c127')
    mrows = {}
    for r in manifest.get('rows') or []:
        req(r.get('id') not in mrows, 'duplicate manifest row %s' % r.get('id'))
        mrows[r.get('id')] = r
    req(manifest.get('roots') == N_ROOTS and len(mrows) == N_ROOTS, 'manifest root count')
    req(manifest.get('ledger_sha256') == LEDGER_SHA and manifest.get('base_cnf_sha256') == BASE_SHA,
        'manifest ledger/base binding')
    req(manifest.get('all_consistent') is True, 'manifest all_consistent')
    side = {}
    for line in sidecar.splitlines():
        if line.strip():
            parts = line.split('  ', 1)
            if req(len(parts) == 2 and re.fullmatch('[0-9a-f]{64}', parts[0]), 'sidecar format: ' + line[:90]):
                req(parts[1] not in side, 'duplicate sidecar path ' + parts[1])
                side[parts[1]] = parts[0]
    req(len(side) == N_ROOTS, 'sidecar entries != %d' % N_ROOTS)
    plan, excluded, used = [], [], set()
    for idx, leaf in enumerate(leaves):
        lid = leaf.get('id')
        canon = [v if (idx >> j) & 1 else -v for j, v in enumerate(chain1)]
        req(leaf.get('depth') == 1 and leaf.get('index') == idx and leaf.get('ancestor') is None, lid + ' identity')
        req(leaf.get('lits') == canon, lid + ' ledger lits differ from the canonical chain[1] sign pattern')
        ev = leaf.get('evidence') or {}
        if leaf.get('state') == 'UNKNOWN':
            req(lid in UNKNOWN_ROOTS and lid not in mrows, lid + ' unexpected UNKNOWN root or manifest row')
            excluded.append({'id': lid, 'index': idx, 'lits': leaf.get('lits'), 'state': 'UNKNOWN',
                             'evidence': ev, 'replayed': False, 'accepted': False})
            continue
        req(leaf.get('state') == 'CERTIFIED' and lid not in UNKNOWN_ROOTS, lid + ' state')
        req(ev.get('kind') == 'strict' and ev.get('file') == 'strict_L1/RESULTS.jsonl', lid + ' evidence kind/file')
        s = strict.get(ev.get('line_sha256'))
        if not req(s is not None, lid + ' strict line not found by ledger line hash'):
            continue
        used.add(ev['line_sha256'])
        req(s.get('id') == lid and s.get('index') == idx and s.get('depth') == 1 and s.get('ancestor') is None and
            s.get('lits') == leaf.get('lits'), lid + ' strict identity')
        req(s.get('base_cnf_sha256') == BASE_SHA and s.get('cnf_vars') == BASE_VARS and
            s.get('cnf_clauses') == BASE_CLAUSES + ROOT_UNITS, lid + ' strict cnf dims')
        req(s.get('solver_returncode') == 20 and s.get('solver_status_lines') == ['s UNSATISFIABLE'],
            lid + ' strict solver verdict')
        req(s.get('checker_returncode') == 0 and s.get('checker_status_lines') == ['s VERIFIED'],
            lid + ' strict checker verdict')
        req(s.get('relay_errors') == [] and s.get('feed_errors') == [] and s.get('rss_guard_tripped') is False and
            s.get('self_exit') is True and s.get('verified') is True and s.get('strict_ok') is True,
            lid + ' strict guards/ok')
        rb = s.get('retained_binding') or {}
        req(rb.get('retained') is True and rb.get('equals_strict_stream') is True and
            rb.get('file_matches_old_receipt') is True and rb.get('decompress_returncode') == 0,
            lid + ' strict retained-binding flags')
        req(rb.get('decompressed_sha256') == s.get('proof_stream_sha256') and
            rb.get('decompressed_bytes') == s.get('proof_stream_bytes') and
            rb.get('file_sha256') == rb.get('old_receipt_proof_sha256'), lid + ' strict retained-binding hashes')
        m = mrows.get(lid)
        if not req(m is not None, lid + ' no manifest row'):
            continue
        req(m.get('lits') == leaf.get('lits'), lid + ' manifest lits')
        req(m.get('leaf_cnf_sha256') == s.get('cnf_sha256') and m.get('leaf_cnf_clauses') == BASE_CLAUSES + ROOT_UNITS,
            lid + ' manifest leaf cnf')
        req(m.get('strict_receipt') == {'kind': 'strict', 'file': 'strict_L1/RESULTS.jsonl',
                                         'line_sha256': ev['line_sha256']}, lid + ' manifest strict receipt')
        req(m.get('strict_proof_stream_sha256') == s.get('proof_stream_sha256') and
            m.get('strict_proof_stream_bytes') == s.get('proof_stream_bytes') and
            m.get('decompressed_sha256') == s.get('proof_stream_sha256') and
            m.get('decompressed_bytes') == s.get('proof_stream_bytes'), lid + ' manifest stream hashes')
        req(m.get('retained_proof') == rb.get('file') and m.get('retained_proof_sha256') == rb.get('file_sha256'),
            lid + ' manifest retained file vs strict binding')
        req(m.get('retained_proof') in ('all/cube%03d.drat.zst' % idx, 'pilot/cube%03d.drat.zst' % idx),
            lid + ' retained path')
        req(side.get(m.get('retained_proof')) == m.get('retained_proof_sha256'), lid + ' sidecar hash')
        req(m.get('consistent') is True, lid + ' manifest consistent flag')
        ow = m.get('old_worker_receipt') or {}
        ofile = ow.get('file')
        req(ofile in old and str(m.get('retained_proof')).split('/')[0] == str(ofile).split('/')[0],
            lid + ' old receipt file/dir')
        o = old.get(ofile, {}).get(ow.get('line_sha256'))
        if req(o is not None, lid + ' old receipt line not found'):
            req(o.get('cube') == idx and o.get('lits') == leaf.get('lits') and
                o.get('proof_sha256') == m.get('retained_proof_sha256') and
                o.get('proof_bytes_zst') == m.get('retained_proof_bytes') and
                o.get('cnf_sha256') == s.get('cnf_sha256') and o.get('verified') is True and
                o.get('solver_status') == 'UNSAT', lid + ' old receipt fields')
        plan.append({'id': lid, 'index': idx, 'lits': leaf['lits'], 'ledger_evidence_line_sha256': ev['line_sha256'],
                     'expected_leaf_sha256': s['cnf_sha256'], 'leaf_clauses': BASE_CLAUSES + ROOT_UNITS,
                     'zst_rel': m['retained_proof'], 'zst_sha256': m['retained_proof_sha256'],
                     'zst_bytes': m['retained_proof_bytes'], 'raw_sha256': s['proof_stream_sha256'],
                     'raw_bytes': s['proof_stream_bytes'], 'old_receipt': {'file': ofile,
                                                                          'line_sha256': ow.get('line_sha256')}})
    req(len(plan) == N_ROOTS and len({r['id'] for r in plan}) == N_ROOTS, 'plan size')
    req(tuple(x['id'] for x in excluded) == UNKNOWN_ROOTS, 'excluded UNKNOWN roots')
    req(len(strict) == N_ROOTS and used == set(strict), 'strict lines not exactly the ledger-bound 122')
    req(sum(r['zst_bytes'] for r in plan) == MANIFEST_TOTAL_ZST_BYTES, 'total compressed bytes != 444419127')
    info = {'strict_lines': len(strict), 'old_receipts': {k: len(v) for k, v in old.items()},
            'manifest_rows': len(mrows), 'sidecar_entries': len(side), 'chain1': chain1,
            'total_zst_bytes': sum(r['zst_bytes'] for r in plan), 'total_raw_bytes': sum(r['raw_bytes'] for r in plan)}
    return plan, excluded, info


def phase_pin():
    d = new_attempt('pin')
    rec = {'phase': 'pin', 'started_at': now(), 'runner': runner_identity(), 'files': {}, 'problems': []}
    P = rec['problems']
    for name, rel, expect in PINNED:
        src = LANE / rel
        data = src.read_bytes()
        h = sha_bytes(data)
        write_new(d / name, data)
        h_after, h_copy = sha_file(src), sha_file(d / name)
        rec['files'][name] = {'source': str(src), 'sha256': h, 'bytes': len(data), 'expected_sha256': expect,
                              'source_sha256_after_copy': h_after, 'copy_sha256': h_copy}
        if not h == h_after == h_copy:
            P.append('pin copy/hash instability: ' + name)
        if expect and h != expect:
            P.append('pinned SHA mismatch: %s %s != %s' % (name, h, expect))
    plan, excluded, info = build_plan(d, P)
    rec['plan_info'] = info
    try:
        base_rec = validate_base(BASE)
    except BaseInvalid as e:
        base_rec = None
        P.append('base CNF invalid: %s' % e)
    if base_rec:
        if base_rec['sha256'] != BASE_SHA or base_rec['bytes'] != BASE_BYTES:
            P.append('base CNF SHA/bytes mismatch')
        if (base_rec['nvars'], base_rec['nclauses']) != (BASE_VARS, BASE_CLAUSES):
            P.append('base CNF header dims mismatch')
    rec['base'] = base_rec
    rec['checker'] = {'path': str(DT), 'sha256': sha_file(DT), 'expected_sha256': DT_SHA}
    if rec['checker']['sha256'] != DT_SHA:
        P.append('checker SHA mismatch')
    rec['plan'] = plan
    rec['excluded_unknown_roots'] = excluded
    rec['ended_at'] = now()
    write_json_new(d / 'PIN.json', rec)
    print(json.dumps({'pin_dir': str(d), 'problems': P, 'roots': len(plan), 'excluded': len(excluded),
                      'base_validation_s': base_rec and base_rec['validation_s']}), flush=True)
    return 0 if not P else 2


# ---------------------------------------------------------------- one replay case (shared by controls and corpus)
class Truncated(Exception):
    pass


def zstd_chunks(zf, st):
    """Yield the decompressed bytes of a (possibly multi-frame) zstd file; hash/count compressed bytes as read."""
    def rd():
        c = zf.read(CHUNK)
        if c:
            st['zst_h'].update(c)
            st['zst_bytes'] += len(c)
        return c

    buf = rd()
    if not buf:
        raise Truncated('empty compressed file')
    while True:
        st['frames'].append({'magic': buf[:4].hex(), 'descriptor': buf[4] if len(buf) > 4 else None})
        d = zstd.ZstdDecompressor()
        while not d.eof:
            if d.needs_input:
                if not buf:
                    buf = rd()
                    if not buf:
                        raise Truncated('compressed file ended inside frame %d' % len(st['frames']))
                out = d.decompress(buf, max_length=CHUNK)
                buf = b''
            else:
                out = d.decompress(b'', max_length=CHUNK)
            if out:
                yield out
        buf = d.unused_data
        if not buf:
            buf = rd()
            if not buf:
                st['zst_eof'] = True
                return


class Feed:
    """Non-blocking writer of one generator-produced stream into one pipe; hashes exactly the delivered bytes."""

    def __init__(self, name, fd, src, st, hkey, nkey):
        self.name, self.fd, self.src, self.st, self.hkey, self.nkey = name, fd, src, st, hkey, nkey
        self.pending = memoryview(b'')
        self.closed = False
        self.source_done = False
        self.source_error = None
        self.sink_error = None
        self.closed_at = None

    def close(self, t0, note=None):
        if not self.closed:
            os.close(self.fd)
            self.closed = True
            self.closed_at = round(time.monotonic() - t0, 3)
            if note and not self.sink_error:
                self.sink_error = note

    def pump(self, t0):
        start = time.monotonic()
        while not self.closed:
            if not self.pending:
                try:
                    chunk = next(self.src)
                except StopIteration:
                    self.source_done = True
                    self.close(t0)
                    return
                except Exception as e:  # read/decompression failure: fail closed, stop this stream
                    self.source_error = '%s: %s' % (type(e).__name__, e)
                    self.close(t0)
                    return
                self.pending = memoryview(chunk)
                continue
            try:
                n = os.write(self.fd, self.pending)
            except BlockingIOError:
                return
            except OSError as e:
                self.sink_error = '%s: errno=%s %s' % (type(e).__name__, e.errno, e.strerror)
                self.close(t0)
                return
            self.st[self.hkey].update(self.pending[:n])
            self.st[self.nkey] += n
            self.pending = self.pending[n:]
            if time.monotonic() - start > SAMPLE_S:
                return

    def drain_source(self):
        """After an early stop, finish the source so that source-side hashes cover the complete inputs."""
        if self.source_done or self.source_error:
            return
        try:
            for _ in self.src:
                pass
            self.source_done = True
        except Exception as e:
            self.source_error = '%s: %s' % (type(e).__name__, e)

    def report(self):
        return {'source_done': self.source_done, 'source_error': self.source_error, 'sink_error': self.sink_error,
                'closed_at_s': self.closed_at}


WARN_KINDS = (  # (substring, kind, fatal)
    ('backward mode ignores deletion of (pseudo) unit clause', 'unit_deletion_ignored', False),
    ('early EOF of the input formula', 'early_eof_input', True),
    ('clauses less than expected', 'clauses_less_than_expected', True),
    ('wrong binary prefix', 'wrong_binary_prefix', True),
    ('detected and deleted duplicate literal', 'duplicate_literal', False),
    ('deleted clause on proof line', 'deleted_clause_absent', False),
    ('found a tautological clause in proof', 'tautological_clause', False),
    ('RAT check on proof pivot failed', 'rat_pivot_failed', False),
    ('no empty clause detected', 'no_empty_clause', True),
    ('clauses active if proof succeeds', 'active_clauses', True),
)
ERROR_MARKERS = ('ERROR', 'MEMOUT', 'illegal literal', 'error opening', 'failed', 'conflict claimed',
                 'formula contains empty clause', 'trivial UNSAT')
PARSE_HDR_RE = re.compile(r'c parsing input formula with (\d+) variables and (\d+) clauses')
FINISHED_RE = re.compile(r'c finished parsing(?:, read (\d+) bytes from proof file)?')
CORE_RES = {'core_clauses': re.compile(r'c (\d+) of (\d+) clauses in core'),
            'core_lemmas': re.compile(r'c (\d+) of (\d+) lemmas in core using (\d+) resolution steps'),
            'core_rat': re.compile(r'c (\d+) RAT lemmas in core; (\d+) redundant literals in core lemmas'),
            'verification_time': re.compile(r'c verification time: (\S+) seconds')}
BINDING_CHECKS = ('checker_sha256', 'base_header', 'root_literals_valid', 'base_body_sha256', 'base_body_bytes',
                  'base_body_clause_lines', 'cnf_source_complete', 'leaf_source_sha256', 'leaf_source_bytes',
                  'zst_read_to_eof', 'zst_sha256', 'zst_bytes', 'decompress_ok', 'raw_source_sha256',
                  'raw_source_bytes')

_ACTIVE = {'pid': None}


def _forward_sigterm(signum, frame):
    pid = _ACTIVE.get('pid')
    if pid:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    raise SystemExit(128 + signum)


def parse_checker_output(text):
    lines = [x.strip() for x in text.split('\n')]
    lines = [x for x in lines if x]
    status = [x for x in lines if x.startswith('s ')]
    hdr = [m for m in (PARSE_HDR_RE.fullmatch(x) for x in lines) if m]
    fin = [m for m in (FINISHED_RE.fullmatch(x) for x in lines) if m]
    warn_counts, fatal_warn, unclassified = {}, [], []
    for x in lines:
        if x.startswith('c WARNING'):
            for sub, kind, fatal in WARN_KINDS:
                if sub in x:
                    warn_counts[kind] = warn_counts.get(kind, 0) + 1
                    if fatal:
                        fatal_warn.append(kind)
                    break
            else:
                unclassified.append(x[:200])
    errors = [x[:200] for x in lines if not x.startswith('c WARNING') and any(k in x for k in ERROR_MARKERS)]
    path = []
    if 'c UNSAT via unit propagation on the input instance' in lines:
        path.append('up_on_input')
    if any(x.startswith('c found complementary unit clauses') for x in lines):
        path.append('complementary_units')
    if 'c detected empty clause; start verification via backward checking' in lines:
        path.append('backward_check')
    core = {}
    for k, rx in CORE_RES.items():
        ms = [m for m in (rx.fullmatch(x) for x in lines) if m]
        if ms:
            core[k] = list(ms[-1].groups())
    return {'status_lines': status, 'parsed_header': [[int(m.group(1)), int(m.group(2))] for m in hdr],
            'finished_parsing_proof_bytes': [None if m.group(1) is None else int(m.group(1)) for m in fin],
            'reading_from_stdin': 'c reading proof from stdin' in lines, 'warning_counts': warn_counts,
            'fatal_warnings': sorted(set(fatal_warn)), 'unclassified_warnings': unclassified[:20],
            'error_lines': errors[:20], 'checker_path': path, 'core': core, 'line_count': len(lines)}


def run_case(out_dir, name, base_path, base_rec, lits, zst_path, exp, *, t_native=T_NATIVE, wall_limit=WALL_LIMIT,
             rss_guard=RSS_GUARD, meta=None):
    """Stream leaf CNF + retained proof into the pinned drat-trim and decide PASS / REJECT_* / UNKNOWN_*.
    exp: leaf_sha256, zst_sha256, zst_bytes, raw_sha256, raw_bytes."""
    t_case = time.monotonic()
    rec = {'case': name, 'meta': meta or {}, 'started_at': now(), 'runner_sha256': RUNNER_SHA,
           'inputs': {'base_path': str(base_path), 'base_sha256_pinned': base_rec['sha256'],
                      'base_body_sha256_pinned': base_rec['body_sha256'], 'lits': list(lits),
                      'zst_path': str(zst_path), 'expected': dict(exp)},
           'limits': {'t_native_s': t_native, 'wall_limit_s': wall_limit, 'rss_guard_bytes': rss_guard,
                      'rss_hard_bytes': RSS_HARD, 'stop_grace_s': STOP_GRACE, 'sample_s': SAMPLE_S}}
    dt_sha = sha_file(DT)
    rec['checker'] = {'path': str(DT), 'sha256': dt_sha, 'expected_sha256': DT_SHA}
    lits_ok = all(type(x) is int and x != 0 and abs(x) <= base_rec['nvars'] for x in lits)
    bf = open(base_path, 'rb')
    header = bf.readline(4096)
    rec['base_header_read'] = header.decode('ascii', 'replace')
    pre = {'checker_sha256': dt_sha == DT_SHA, 'base_header': header == base_rec['header'].encode(),
           'root_literals_valid': lits_ok}
    if not all(pre.values()):
        bf.close()
        rec.update({'spawned': False, 'checks': pre, 'reasons': [k for k, v in pre.items() if not v],
                    'status': 'REJECT_BINDING', 'accepted': False, 'ended_at': now(),
                    'case_wall_s': round(time.monotonic() - t_case, 3)})
        write_json_new(out_dir / ('%s.json' % name), rec)
        return rec
    k = len(lits)
    leaf_header = b'p cnf %d %d\n' % (base_rec['nvars'], base_rec['nclauses'] + k)
    unit_lines = [b'%d 0\n' % x for x in lits]
    leaf_bytes_expected = len(leaf_header) + base_rec['body_bytes'] + sum(len(u) for u in unit_lines)
    rec['leaf'] = {'header': leaf_header.decode(), 'unit_lines': [u.decode() for u in unit_lines],
                   'vars': base_rec['nvars'], 'clauses': base_rec['nclauses'] + k,
                   'bytes_expected': leaf_bytes_expected}
    st = {'body_h': hashlib.sha256(), 'body_bytes': 0, 'body_newlines': 0,
          'leaf_src_h': hashlib.sha256(), 'leaf_src_bytes': 0, 'leaf_h': hashlib.sha256(), 'leaf_bytes': 0,
          'zst_h': hashlib.sha256(), 'zst_bytes': 0, 'zst_eof': False, 'frames': [],
          'raw_src_h': hashlib.sha256(), 'raw_src_bytes': 0, 'raw_h': hashlib.sha256(), 'raw_bytes': 0}

    def leaf_piece(b):
        st['leaf_src_h'].update(b)
        st['leaf_src_bytes'] += len(b)
        return b

    def cnf_src():
        yield leaf_piece(leaf_header)
        while True:
            b = bf.read(CHUNK)
            if not b:
                break
            st['body_h'].update(b)
            st['body_bytes'] += len(b)
            st['body_newlines'] += b.count(b'\n')
            yield leaf_piece(b)
        for u in unit_lines:
            yield leaf_piece(u)

    zf = open(zst_path, 'rb')

    def proof_src():
        for out in zstd_chunks(zf, st):
            st['raw_src_h'].update(out)
            st['raw_src_bytes'] += len(out)
            yield out

    out_path = out_dir / ('%s.drat-trim.stdout' % name)
    err_path = out_dir / ('%s.drat-trim.stderr' % name)
    out_f, err_f = open(out_path, 'xb'), open(err_path, 'xb')
    cnf_r, cnf_w = os.pipe()
    prf_r, prf_w = os.pipe()
    argv = [str(DT), '/dev/fd/%d' % cnf_r, '-i', '-t', str(t_native)]
    env = {'PATH': '/usr/bin:/bin', 'LC_ALL': 'C'}
    rec['command'] = {'checker_argv': argv, 'checker_cwd': str(out_dir), 'checker_env': env,
                      'argv1': 'anonymous pipe (leaf CNF stream) opened by drat-trim via /dev/fd',
                      'stdin': 'anonymous pipe (in-process zstd-decompressed retained DRAT, binary mode -i)',
                      'stdout': out_path.name, 'stderr': err_path.name}
    t_spawn = time.monotonic()
    rec['spawned_at'] = now()
    try:
        proc = subprocess.Popen(argv, stdin=prf_r, stdout=out_f, stderr=err_f, pass_fds=(cnf_r,), env=env,
                                cwd=str(out_dir))
    except OSError as e:
        for fd in (cnf_r, cnf_w, prf_r, prf_w):
            os.close(fd)
        out_f.close()
        err_f.close()
        bf.close()
        zf.close()
        rec.update({'spawned': False, 'spawn_error': repr(e), 'checks': {}, 'reasons': ['spawn_error'],
                    'status': 'UNKNOWN_OTHER', 'accepted': False, 'ended_at': now(),
                    'case_wall_s': round(time.monotonic() - t_case, 3)})
        write_json_new(out_dir / ('%s.json' % name), rec)
        return rec
    _ACTIVE['pid'] = proc.pid
    rec['spawned'] = True
    rec['checker_pid'] = proc.pid
    os.close(cnf_r)
    os.close(prf_r)
    out_f.close()
    err_f.close()
    os.set_blocking(cnf_w, False)
    os.set_blocking(prf_w, False)
    feeds = [Feed('cnf', cnf_w, cnf_src(), st, 'leaf_h', 'leaf_bytes'),
             Feed('proof', prf_w, proof_src(), st, 'raw_h', 'raw_bytes')]
    child = None
    trip = {'rss': False, 'monitor': False, 'wall': False}
    term_at = None
    stop_failed = False
    peaks = {'child_rss': 0, 'self_rss': 0, 'agg_rss': 0, 'samples': 0, 'sample_failures': 0}
    trace = []
    consec_fail = 0
    last_sample = last_trace = 0.0

    def terminate(reason):
        rec.setdefault('sigterm', []).append({'reason': reason, 't_s': round(time.monotonic() - t_spawn, 3),
                                              'at': now()})
        try:
            os.kill(proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        return time.monotonic()

    while True:
        if child is None:
            pid, status, ru = os.wait4(proc.pid, os.WNOHANG)
            if pid == proc.pid:
                child = (status, ru, time.monotonic())
                proc.returncode = os.waitstatus_to_exitcode(status)
                _ACTIVE['pid'] = None
        live = [f for f in feeds if not f.closed]
        if child is not None and not live:
            break
        if live and child is None:
            try:
                _, w, _ = select.select([], [f.fd for f in live], [], SAMPLE_S)
            except InterruptedError:
                w = []
            for f in live:
                if f.fd in w:
                    f.pump(t_spawn)
        elif live:  # child gone: readers closed, remaining writes must fail (EPIPE) or be force-closed
            for f in live:
                f.pump(t_spawn)
            if time.monotonic() - child[2] > 5.0:
                for f in live:
                    f.close(t_spawn, 'forced close 5 s after checker exit')
            time.sleep(0.01)
        else:
            time.sleep(SAMPLE_S)
        t = time.monotonic()
        if child is None and t - last_sample >= SAMPLE_S:
            last_sample = t
            c, s = rss_of(proc.pid), rss_of(os.getpid())
            if c is None or s is None:
                peaks['sample_failures'] += 1
                consec_fail += 1
                if consec_fail > 100 and not trip['monitor']:
                    trip['monitor'] = True
                    term_at = term_at or terminate('rss monitor unavailable')
            else:
                consec_fail = 0
                peaks['samples'] += 1
                peaks['child_rss'] = max(peaks['child_rss'], c)
                peaks['self_rss'] = max(peaks['self_rss'], s)
                peaks['agg_rss'] = max(peaks['agg_rss'], c + s)
                if c + s > rss_guard and not trip['rss']:
                    trip['rss'] = True
                    rec['rss_guard_trip'] = {'aggregate_bytes': c + s, 'child_bytes': c, 'self_bytes': s,
                                             't_s': round(t - t_spawn, 3)}
                    term_at = term_at or terminate('rss guard')
                if t - last_trace >= 5.0:
                    last_trace = t
                    trace.append([round(t - t_spawn, 2), c, s])
        if child is None and t - t_spawn > wall_limit and not trip['wall']:
            trip['wall'] = True
            term_at = term_at or terminate('wall watchdog')
        if child is None and term_at is not None and t - term_at > STOP_GRACE:
            stop_failed = True
            break
    for f in feeds:
        if not f.closed:
            f.close(t_spawn, 'closed by runner after stop failure')
    for f in feeds:
        f.drain_source()
    bf.close()
    zf.close()
    self_maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rc = None
    if child is not None:
        status, ru, t_exit = child
        rc = os.waitstatus_to_exitcode(status)
        rec['exit'] = {'returncode': rc, 'signaled': rc < 0, 'signal': -rc if rc < 0 else None,
                       'wall_s': round(t_exit - t_spawn, 3), 'ru_maxrss_bytes': ru.ru_maxrss,
                       'ru_utime_s': round(ru.ru_utime, 3), 'ru_stime_s': round(ru.ru_stime, 3)}
    else:
        rec['exit'] = None
    rec['stop_failed'] = stop_failed
    rec['guard'] = {'rss_tripped': trip['rss'], 'monitor_tripped': trip['monitor'], 'wall_tripped': trip['wall'],
                    'peaks_sampled': peaks, 'self_maxrss_lifetime_bytes': self_maxrss, 'trace_5s': trace}
    out_size, err_size = out_path.stat().st_size, err_path.stat().st_size
    with open(out_path, 'rb') as f:
        out_b = f.read(STDOUT_READ_CAP)
    with open(err_path, 'rb') as f:
        err_b = f.read(STDOUT_READ_CAP)
    po = parse_checker_output(out_b.decode('utf-8', 'replace'))
    rec['checker_output'] = {'stdout_bytes': out_size, 'stdout_sha256': sha_file(out_path),
                             'stderr_bytes': err_size, 'stderr_sha256': sha_file(err_path),
                             'stderr_head': err_b[:400].decode('utf-8', 'replace'), **po}
    leaf_src_sha, leaf_sha = st['leaf_src_h'].hexdigest(), st['leaf_h'].hexdigest()
    raw_src_sha, raw_sha = st['raw_src_h'].hexdigest(), st['raw_h'].hexdigest()
    zst_sha = st['zst_h'].hexdigest()
    rec['streams'] = {
        'cnf': {'base_body_sha256': st['body_h'].hexdigest(), 'base_body_bytes': st['body_bytes'],
                'base_body_newlines': st['body_newlines'], 'leaf_source_sha256': leaf_src_sha,
                'leaf_source_bytes': st['leaf_src_bytes'], 'leaf_delivered_sha256': leaf_sha,
                'leaf_delivered_bytes': st['leaf_bytes'], **feeds[0].report()},
        'proof': {'zst_sha256': zst_sha, 'zst_bytes': st['zst_bytes'], 'zst_read_to_eof': st['zst_eof'],
                  'zst_frames': st['frames'], 'raw_source_sha256': raw_src_sha, 'raw_source_bytes': st['raw_src_bytes'],
                  'raw_delivered_sha256': raw_sha, 'raw_delivered_bytes': st['raw_bytes'], **feeds[1].report()}}
    exp_hdr = [base_rec['nvars'], base_rec['nclauses'] + k]
    checks = dict(pre)
    checks.update({
        'base_body_sha256': st['body_h'].hexdigest() == base_rec['body_sha256'],
        'base_body_bytes': st['body_bytes'] == base_rec['body_bytes'],
        'base_body_clause_lines': st['body_newlines'] == base_rec['nclauses'],
        'cnf_source_complete': feeds[0].source_done and feeds[0].source_error is None,
        'leaf_source_sha256': leaf_src_sha == exp['leaf_sha256'],
        'leaf_source_bytes': st['leaf_src_bytes'] == leaf_bytes_expected,
        'cnf_delivered_complete': (feeds[0].source_done and feeds[0].sink_error is None and
                                   st['leaf_bytes'] == st['leaf_src_bytes']),
        'leaf_delivered_sha256': leaf_sha == exp['leaf_sha256'],
        'zst_read_to_eof': st['zst_eof'],
        'zst_sha256': zst_sha == exp['zst_sha256'],
        'zst_bytes': st['zst_bytes'] == exp['zst_bytes'],
        'decompress_ok': feeds[1].source_done and feeds[1].source_error is None,
        'raw_source_sha256': raw_src_sha == exp['raw_sha256'],
        'raw_source_bytes': st['raw_src_bytes'] == exp['raw_bytes'],
        'proof_delivered_complete': (feeds[1].source_done and feeds[1].sink_error is None and
                                     st['raw_bytes'] == st['raw_src_bytes']),
        'raw_delivered_sha256': raw_sha == exp['raw_sha256'],
        'raw_delivered_bytes': st['raw_bytes'] == exp['raw_bytes'],
        'exit_normal_rc0': rc == 0,
        'status_exactly_verified': po['status_lines'] == ['s VERIFIED'],
        'no_native_timeout': 's TIMEOUT' not in po['status_lines'],
        'checker_parsed_header': po['parsed_header'] == [exp_hdr],
        'checker_read_proof_from_stdin': po['reading_from_stdin'],
        'checker_consumed_all_proof_bytes': po['finished_parsing_proof_bytes'] == [exp['raw_bytes']],
        'checker_single_path': len(po['checker_path']) == 1,
        'no_fatal_or_unclassified_warning': not po['fatal_warnings'] and not po['unclassified_warnings'],
        'no_error_lines': not po['error_lines'],
        'stderr_empty': err_size == 0,
        'stdout_within_cap': out_size <= STDOUT_READ_CAP,
        'no_rss_guard_trip': not trip['rss'] and not trip['monitor'],
        'no_wall_trip': not trip['wall'],
        'not_stop_failed': not stop_failed,
        'rss_hard_ceiling': rec['exit'] is not None and rec['exit']['ru_maxrss_bytes'] + self_maxrss <= RSS_HARD,
    })
    reasons = [kk for kk, v in checks.items() if not v]
    delivered = checks['cnf_delivered_complete'] and checks['proof_delivered_complete']
    if stop_failed:
        status = 'UNKNOWN_STOP_FAILED'
    elif any(not checks[kk] for kk in BINDING_CHECKS):
        status = 'REJECT_BINDING'
    elif trip['rss'] or trip['monitor'] or not checks['rss_hard_ceiling']:
        status = 'UNKNOWN_CAP'
    elif trip['wall'] or not checks['no_native_timeout']:
        status = 'UNKNOWN_TIMEOUT'
    elif not reasons:
        status = 'PASS'
    elif (delivered and rc == 1 and po['status_lines'] == ['s NOT VERIFIED'] and checks['checker_parsed_header'] and
          checks['checker_consumed_all_proof_bytes'] and checks['stderr_empty']):
        status = 'REJECT_CHECKER'
    else:
        status = 'UNKNOWN_OTHER'
    rec.update({'checks': checks, 'reasons': reasons, 'status': status, 'accepted': status == 'PASS',
                'ended_at': now(), 'case_wall_s': round(time.monotonic() - t_case, 3)})
    write_json_new(out_dir / ('%s.json' % name), rec)
    return rec


def observed(r):
    po = r.get('checker_output') or {}
    ex = r.get('exit') or {}
    return {'status_lines': po.get('status_lines'), 'returncode': ex.get('returncode'),
            'checker_path': po.get('checker_path')}


# ---------------------------------------------------------------- controls phase
def phase_controls():
    pin_dir, PIN = latest_ok('pin', 'PIN.json', lambda o: o.get('problems') == [] and
                             o['runner']['sha256'] == RUNNER_SHA)
    base_rec = PIN['base']
    plan = {r['id']: r for r in PIN['plan']}
    d = new_attempt('controls')
    fx = d / 'fixtures'
    fx.mkdir()
    rec = {'phase': 'controls', 'started_at': now(), 'runner': runner_identity(),
           'pin': {'dir': str(pin_dir), 'PIN_json_sha256': sha_file(pin_dir / 'PIN.json')}, 'fixtures': {},
           'controls': []}

    def fixture(fname, data):
        write_new(fx / fname, data)
        rec['fixtures'][fname] = {'sha256': sha_bytes(data), 'bytes': len(data)}
        return fx / fname

    def zfix(fname, raw):
        z = zstd.compress(raw, level=3)
        p = fixture(fname, z)
        return p, {'zst_sha256': sha_bytes(z), 'zst_bytes': len(z), 'raw_sha256': sha_bytes(raw),
                   'raw_bytes': len(raw)}

    def plan_exp(row):
        return {'leaf_sha256': row['expected_leaf_sha256'], 'zst_sha256': row['zst_sha256'],
                'zst_bytes': row['zst_bytes'], 'raw_sha256': row['raw_sha256'], 'raw_bytes': row['raw_bytes']}

    # tiny bases and hand-written expected leaves (independent of the streaming code)
    tiny_p = fixture('tiny_base_sat.cnf', b'p cnf 3 4\n1 2 3 0\n-1 2 3 0\n1 -2 3 0\n-1 -2 3 0\n')
    one_p = fixture('one_var_sat.cnf', b'p cnf 1 1\n1 0\n')
    tiny_rec, one_rec = validate_base(tiny_p), validate_base(one_p)
    leaf_m3 = fixture('expected_leaf_tiny_unit_m3.cnf', b'p cnf 3 5\n1 2 3 0\n-1 2 3 0\n1 -2 3 0\n-1 -2 3 0\n-3 0\n')
    leaf_p3 = fixture('expected_leaf_tiny_unit_p3.cnf', b'p cnf 3 5\n1 2 3 0\n-1 2 3 0\n1 -2 3 0\n-1 -2 3 0\n3 0\n')
    valid_raw = bytes([0x61, 0x02, 0x00, 0x61, 0x00])  # a (x1) 0 ; a () 0  -- RUP lemma x1, then empty clause
    empty_raw = bytes([0x61, 0x00])                    # a () 0           -- bare empty-clause claim
    fixture('tiny_valid.drat', valid_raw)
    fixture('empty_clause_only.drat', empty_raw)
    valid_z, valid_e = zfix('tiny_valid.drat.zst', valid_raw)
    empty_z, empty_e = zfix('empty_clause_only.drat.zst', empty_raw)
    tail_z, tail_e = zfix('valid_then_1MiB_wrong_prefix.drat.zst', valid_raw + b'x' * (1 << 20))
    m3_sha, p3_sha, one_sha = sha_file(leaf_m3), sha_file(leaf_p3), sha_file(one_p)

    U, A, B = plan['c004'], plan['c054'], plan['c014']  # smallest UP-refuted root; two smallest backward roots
    a_zst = (K5 / A['zst_rel']).read_bytes()
    if sha_bytes(a_zst) != A['zst_sha256']:
        raise SystemExit('control source c054 retained proof does not match the plan')
    flip = bytearray(a_zst)
    flip[len(flip) // 2] ^= 0xFF
    flip_p = fixture('c054_zst_byte_flip.drat.zst', bytes(flip))
    a_raw = zstd.decompress(a_zst)
    if sha_bytes(a_raw) != A['raw_sha256']:
        raise SystemExit('control source c054 decompressed proof does not match the plan')
    mut = bytearray(a_raw)
    mut[len(mut) // 2] ^= 0x01
    mut_p, mut_e = zfix('c054_raw_byte_mutation_recompressed.drat.zst', bytes(mut))
    trunc_p = fixture('c054_zst_first_half.drat.zst', a_zst[:len(a_zst) // 2])
    trunc_sha, trunc_n = sha_bytes(a_zst[:len(a_zst) // 2]), len(a_zst) // 2

    def tiny_exp(leaf_sha, e):
        return {'leaf_sha256': leaf_sha, **{kk: e[kk] for kk in ('zst_sha256', 'zst_bytes', 'raw_sha256', 'raw_bytes')}}

    real = dict(base_path=BASE, base_rec=base_rec)
    C = [
        ('P1_tiny_valid_unsat', 'valid small UNSAT proof (RUP lemma + empty clause) on base+unit must be accepted',
         dict(base_path=tiny_p, base_rec=tiny_rec, lits=[-3], zst_path=valid_z, exp=tiny_exp(m3_sha, valid_e)),
         'PASS', (), (), {'checker_path': ['backward_check']}),
        ('N1_bogus_empty_on_sat', 'bare empty-clause proof on a SAT leaf CNF must be rejected by the checker',
         dict(base_path=tiny_p, base_rec=tiny_rec, lits=[3], zst_path=empty_z, exp=tiny_exp(p3_sha, empty_e)),
         'REJECT_CHECKER', ('status_exactly_verified',), (), {'status_lines': ['s NOT VERIFIED'], 'returncode': 1}),
        ('N2_bogus_empty_on_unsat_not_up', 'bare empty-clause proof on an UNSAT leaf not refutable by UP: reject',
         dict(base_path=tiny_p, base_rec=tiny_rec, lits=[-3], zst_path=empty_z, exp=tiny_exp(m3_sha, empty_e)),
         'REJECT_CHECKER', ('status_exactly_verified',), (), {'status_lines': ['s NOT VERIFIED'], 'returncode': 1}),
        ('N3_lratcheck_mirror_sat', 'p cnf 1 1 / 1 0 with empty-clause proof (upstream lrat-check accepts): reject',
         dict(base_path=one_p, base_rec=one_rec, lits=[], zst_path=empty_z, exp=tiny_exp(one_sha, empty_e)),
         'REJECT_CHECKER', ('status_exactly_verified',), (), {'status_lines': ['s NOT VERIFIED'], 'returncode': 1}),
        ('F1_wrong_prefix_tail', 'valid proof + 1 MiB tail: checker stops reading and says VERIFIED; runner must '
         'still fail closed on incomplete consumption/delivery',
         dict(base_path=tiny_p, base_rec=tiny_rec, lits=[-3], zst_path=tail_z, exp=tiny_exp(m3_sha, tail_e)),
         'UNKNOWN_OTHER', ('checker_consumed_all_proof_bytes', 'no_fatal_or_unclassified_warning'),
         BINDING_CHECKS, {'status_lines': ['s VERIFIED'], 'returncode': 0}),
        ('R0_real_up_root_positive', 'real root c004 (smallest proof) through the corpus path must PASS',
         dict(**real, lits=U['lits'], zst_path=K5 / U['zst_rel'], exp=plan_exp(U)), 'PASS', (), (), {}),
        ('R0b_real_backward_root_positive', 'real root c054 (smallest backward-checked proof) must PASS',
         dict(**real, lits=A['lits'], zst_path=K5 / A['zst_rel'], exp=plan_exp(A)), 'PASS', (), (),
         {'checker_path': ['backward_check']}),
        ('N4_real_bogus_empty', 'real c054 leaf CNF with a bare empty-clause proof must be rejected by the checker',
         dict(**real, lits=A['lits'], zst_path=empty_z, exp=tiny_exp(A['expected_leaf_sha256'], empty_e)),
         'REJECT_CHECKER', ('status_exactly_verified',), (), {'status_lines': ['s NOT VERIFIED'], 'returncode': 1}),
        ('R1_corrupt_retained_zst_byte', 'retained c054 proof with one flipped compressed byte vs manifest hash',
         dict(**real, lits=A['lits'], zst_path=flip_p, exp=plan_exp(A)), 'REJECT_BINDING', ('zst_sha256',), (), {}),
        ('R2_raw_mutation_recompressed', 'c054 proof with one mutated decompressed byte, recompressed (compressed '
         'hash self-consistent) vs strict stream hash',
         dict(**real, lits=A['lits'], zst_path=mut_p,
              exp={**plan_exp(A), 'zst_sha256': mut_e['zst_sha256'], 'zst_bytes': mut_e['zst_bytes']}),
         'REJECT_BINDING', ('raw_source_sha256', 'raw_delivered_sha256'), ('zst_sha256', 'zst_bytes'), {}),
        ('R3_wrong_root_literals', 'c054 expectations with c014 root literals (wrong root binding)',
         dict(**real, lits=B['lits'], zst_path=K5 / A['zst_rel'], exp=plan_exp(A)), 'REJECT_BINDING',
         ('leaf_source_sha256', 'leaf_delivered_sha256'), ('zst_sha256', 'raw_source_sha256'), {}),
        ('R4_truncated_zst', 'first half of the c054 retained proof (own compressed hash): decompression must fail',
         dict(**real, lits=A['lits'], zst_path=trunc_p,
              exp={**plan_exp(A), 'zst_sha256': trunc_sha, 'zst_bytes': trunc_n}),
         'REJECT_BINDING', ('decompress_ok',), ('zst_sha256', 'zst_bytes'), {}),
        ('R5_other_root_proof', 'c054 expectations with the retained c014 proof file (wrong mapping)',
         dict(**real, lits=A['lits'], zst_path=K5 / B['zst_rel'], exp=plan_exp(A)), 'REJECT_BINDING',
         ('zst_sha256', 'raw_source_sha256'), (), {}),
        ('G1_rss_guard', 'real c004 with a 160 MiB aggregate guard: SIGTERM, bounded stop, UNKNOWN not FAIL/UNSAT',
         dict(**real, lits=U['lits'], zst_path=K5 / U['zst_rel'], exp=plan_exp(U), rss_guard=160 * 2 ** 20),
         'UNKNOWN_CAP', ('no_rss_guard_trip',), (), {'returncode': -15}),
        ('T1_native_timeout_rc0', 'real c054 with drat-trim -t 0: prints s TIMEOUT and exits 0; must be UNKNOWN',
         dict(**real, lits=A['lits'], zst_path=K5 / A['zst_rel'], exp=plan_exp(A), t_native=0),
         'UNKNOWN_TIMEOUT', ('status_exactly_verified', 'no_native_timeout'), (),
         {'status_lines': ['s TIMEOUT'], 'returncode': 0}),
        ('T2_wall_watchdog', 'real c004 with a 1 s wall watchdog: SIGTERM, bounded stop, UNKNOWN',
         dict(**real, lits=U['lits'], zst_path=K5 / U['zst_rel'], exp=plan_exp(U), wall_limit=1.0),
         'UNKNOWN_TIMEOUT', ('no_wall_trip',), (), {'returncode': -15}),
    ]
    for cname, purpose, kw, want, need, forbid, obs in C:
        r = run_case(d, cname, meta={'control': cname}, **kw)
        o = observed(r)
        ok = (r['status'] == want and set(need) <= set(r['reasons']) and not (set(forbid) & set(r['reasons'])) and
              all(o.get(kk) == v for kk, v in obs.items()))
        rec['controls'].append({'name': cname, 'purpose': purpose, 'expected_status': want,
                                'required_failed_checks': list(need), 'forbidden_failed_checks': list(forbid),
                                'expected_observations': obs, 'observed_status': r['status'],
                                'observed_failed_checks': r['reasons'], 'observed': o,
                                'receipt': '%s.json' % cname, 'receipt_sha256': sha_file(d / ('%s.json' % cname)),
                                'as_intended': ok})
        print(json.dumps({'control': cname, 'status': r['status'], 'as_intended': ok, 'observed': o}), flush=True)
    for cname, data, want in (
            ('V1_header_undercount', b'p cnf 3 3\n1 2 3 0\n-1 2 3 0\n1 -2 3 0\n-1 -2 3 0\n', 'clause lines 4 != header'),
            ('V2_octal_looking_literal', b'p cnf 9 1\n010 0\n', 'malformed clause line 1'),
            ('V3_comment_line', b'p cnf 3 1\nc note\n1 0\n', 'malformed clause line 1'),
            ('V4_literal_out_of_range', b'p cnf 3 1\n4 0\n', 'exceeds header vars')):
        p = fixture(cname + '.cnf', data)
        try:
            validate_base(p)
            got = 'ACCEPTED'
        except BaseInvalid as e:
            got = str(e)
        ok = want in got
        rec['controls'].append({'name': cname, 'purpose': 'base validation (gates every stream) must reject',
                                'expected_error_substring': want, 'observed_error': got, 'as_intended': ok})
        print(json.dumps({'control': cname, 'observed_error': got, 'as_intended': ok}), flush=True)
    rec['all_as_intended'] = all(c['as_intended'] for c in rec['controls'])
    rec['ended_at'] = now()
    write_json_new(d / 'CONTROLS.json', rec)
    print(json.dumps({'controls_dir': str(d), 'all_as_intended': rec['all_as_intended'],
                      'n': len(rec['controls'])}), flush=True)
    return 0 if rec['all_as_intended'] else 2


# ---------------------------------------------------------------- corpus phase
def phase_corpus(retry):
    pin_dir, PIN = latest_ok('pin', 'PIN.json', lambda o: o.get('problems') == [] and
                             o['runner']['sha256'] == RUNNER_SHA)
    pin_sha = sha_file(pin_dir / 'PIN.json')
    con_dir, CON = latest_ok('controls', 'CONTROLS.json', lambda o: o.get('all_as_intended') is True and
                             o['runner']['sha256'] == RUNNER_SHA and o['pin']['PIN_json_sha256'] == pin_sha)
    base_rec = PIN['base']
    prior = {}
    for a in attempt_dirs('corpus'):
        for row in PIN['plan']:
            if (a / ('%s.json' % row['id'])).is_file():
                prior.setdefault(row['id'], []).append(str(a))
    todo = [r for r in PIN['plan'] if r['id'] not in prior or r['id'] in retry]
    order = sorted(todo, key=lambda r: (r['raw_bytes'], r['id']))
    d = new_attempt('corpus')
    write_json_new(d / 'META.json', {'phase': 'corpus', 'started_at': now(), 'runner': runner_identity(),
                                     'pin': {'dir': str(pin_dir), 'PIN_json_sha256': pin_sha},
                                     'controls': {'dir': str(con_dir),
                                                  'CONTROLS_json_sha256': sha_file(con_dir / 'CONTROLS.json')},
                                     'retry': sorted(retry), 'prior_receipts': prior,
                                     'order': [r['id'] for r in order]})
    done = 0
    for pos, row in enumerate(order):
        free = shutil.disk_usage(HERE).free
        own = dir_bytes(HERE)
        if free < FREE_FLOOR + FREE_MARGIN or own > NEWDATA_CAP:
            write_json_new(d / 'STOP.json', {'at': now(), 'reason': 'disk floor / new-data cap', 'free_bytes': free,
                                             'own_bytes': own, 'next': row['id'], 'done': done})
            print(json.dumps({'stop': 'disk', 'free': free, 'own': own}), flush=True)
            return 4
        exp = {'leaf_sha256': row['expected_leaf_sha256'], 'zst_sha256': row['zst_sha256'],
               'zst_bytes': row['zst_bytes'], 'raw_sha256': row['raw_sha256'], 'raw_bytes': row['raw_bytes']}
        r = run_case(d, row['id'], BASE, base_rec, row['lits'], K5 / row['zst_rel'], exp,
                     meta={'root_id': row['id'], 'index': row['index'], 'order_position': pos,
                           'ledger_evidence_line_sha256': row['ledger_evidence_line_sha256'],
                           'retained_rel': row['zst_rel'], 'free_bytes_before': free, 'own_bytes_before': own})
        done += 1
        po = r.get('checker_output') or {}
        ex = r.get('exit') or {}
        print(json.dumps({'pos': pos, 'id': row['id'], 'status': r['status'], 'path': po.get('checker_path'),
                          'wall': ex.get('wall_s'), 'maxrss': ex.get('ru_maxrss_bytes'),
                          'agg_peak': r['guard']['peaks_sampled']['agg_rss'] if r.get('guard') else None,
                          'at': r['ended_at']}), flush=True)
        if r['status'] != 'PASS':
            write_json_new(d / 'STOP.json', {'at': now(), 'reason': 'first non-PASS root', 'id': row['id'],
                                             'status': r['status'], 'reasons': r['reasons'], 'done': done})
            return 3
    write_json_new(d / 'DONE.json', {'at': now(), 'done': done, 'planned': len(order)})
    return 0


# ---------------------------------------------------------------- final phase
def phase_final():
    pin_dir, PIN = latest_ok('pin', 'PIN.json', lambda o: o.get('problems') == [] and
                             o['runner']['sha256'] == RUNNER_SHA)
    pin_sha = sha_file(pin_dir / 'PIN.json')
    con_dir, CON = latest_ok('controls', 'CONTROLS.json', lambda o: o.get('all_as_intended') is True and
                             o['runner']['sha256'] == RUNNER_SHA and o['pin']['PIN_json_sha256'] == pin_sha)
    attempts = attempt_dirs('corpus')
    rows, problems = [], []
    for row in PIN['plan']:
        recs = [(a, a / ('%s.json' % row['id'])) for a in attempts if (a / ('%s.json' % row['id'])).is_file()]
        if not recs:
            rows.append({'id': row['id'], 'index': row['index'], 'lits': row['lits'], 'status': 'NOT_RUN',
                         'accepted': False, 'attempt_receipts': []})
            continue
        a, p = recs[-1]
        r = json.loads(p.read_bytes())
        exp = r['inputs']['expected']
        bound = (r['case'] == row['id'] and r['inputs']['lits'] == row['lits'] and r['runner_sha256'] == RUNNER_SHA and
                 exp == {'leaf_sha256': row['expected_leaf_sha256'], 'zst_sha256': row['zst_sha256'],
                         'zst_bytes': row['zst_bytes'], 'raw_sha256': row['raw_sha256'], 'raw_bytes': row['raw_bytes']}
                 and r['inputs']['zst_path'] == str(K5 / row['zst_rel']) and r['inputs']['base_path'] == str(BASE))
        if not bound:
            problems.append('receipt/plan binding mismatch for ' + row['id'])
        cs, po, ex, g = r.get('streams') or {}, r.get('checker_output') or {}, r.get('exit') or {}, r.get('guard') or {}
        rows.append({
            'id': row['id'], 'index': row['index'], 'lits': row['lits'], 'status': r['status'],
            'accepted': r['status'] == 'PASS' and bound, 'reasons': r['reasons'],
            'receipt': {'path': str(p), 'sha256': sha_file(p)},
            'attempt_receipts': [str(q) for _, q in recs],
            'base': {'path': str(BASE), 'sha256_pinned_once': PIN['base']['sha256'],
                     'body_sha256_streamed': (cs.get('cnf') or {}).get('base_body_sha256')},
            'cube_unit_lines': (r.get('leaf') or {}).get('unit_lines'),
            'leaf_cnf': {'header': (r.get('leaf') or {}).get('header'),
                         'sha256_delivered': (cs.get('cnf') or {}).get('leaf_delivered_sha256'),
                         'bytes_delivered': (cs.get('cnf') or {}).get('leaf_delivered_bytes'),
                         'expected_sha256_strict': row['expected_leaf_sha256']},
            'compressed_proof': {'path': str(K5 / row['zst_rel']), 'sha256': (cs.get('proof') or {}).get('zst_sha256'),
                                 'bytes': (cs.get('proof') or {}).get('zst_bytes'),
                                 'expected_sha256_manifest': row['zst_sha256']},
            'raw_proof': {'sha256_delivered': (cs.get('proof') or {}).get('raw_delivered_sha256'),
                          'bytes_delivered': (cs.get('proof') or {}).get('raw_delivered_bytes'),
                          'expected_sha256_strict': row['raw_sha256'], 'expected_bytes_strict': row['raw_bytes']},
            'checker': {'sha256': (r.get('checker') or {}).get('sha256'),
                        'argv': (r.get('command') or {}).get('checker_argv'),
                        'returncode': ex.get('returncode'), 'status_lines': po.get('status_lines'),
                        'checker_path': po.get('checker_path'), 'parsed_header': po.get('parsed_header'),
                        'proof_bytes_read': po.get('finished_parsing_proof_bytes'), 'core': po.get('core'),
                        'warning_counts': po.get('warning_counts'),
                        'stdout': {'path': str(p.parent / ('%s.drat-trim.stdout' % row['id'])),
                                   'sha256': po.get('stdout_sha256'), 'bytes': po.get('stdout_bytes')},
                        'stderr_bytes': po.get('stderr_bytes')},
            'resources': {'checker_wall_s': ex.get('wall_s'), 'case_wall_s': r.get('case_wall_s'),
                          'checker_ru_maxrss_bytes': ex.get('ru_maxrss_bytes'),
                          'checker_cpu_s': None if not ex else round(ex['ru_utime_s'] + ex['ru_stime_s'], 3),
                          'aggregate_rss_peak_sampled_bytes': (g.get('peaks_sampled') or {}).get('agg_rss'),
                          'self_maxrss_lifetime_bytes': g.get('self_maxrss_lifetime_bytes'),
                          'rss_guard_tripped': g.get('rss_tripped'), 'wall_tripped': g.get('wall_tripped')},
            'started_at': r.get('started_at'), 'ended_at': r.get('ended_at')})
    passed = [x['id'] for x in rows if x['accepted']]
    paths = {}
    for x in rows:
        key = '+'.join((x.get('checker') or {}).get('checker_path') or ['none'])
        paths[key] = paths.get(key, 0) + 1
    res = [x['resources'] for x in rows if x.get('resources')]
    d = new_attempt('final')
    fin = {
        'phase': 'final', 'written_at': now(), 'runner': runner_identity(),
        'scope': ('C11 root replay only: each of the 122 ledger-v003 CERTIFIED K5 roots checked with the parent-pinned '
                  'drat-trim against exactly base CNF + that root\'s 7 unit clauses, using the byte-bound retained '
                  'proof. Not whole-K5 acceptance; the 6 UNKNOWN roots are excluded and not accepted; the cover '
                  'argument, encoders and base-CNF semantics are separate gates.'),
        'pin': {'dir': str(pin_dir), 'PIN_json_sha256': pin_sha, 'files': PIN['files'], 'base': PIN['base'],
                'checker': PIN['checker'], 'plan_info': PIN['plan_info']},
        'controls': {'dir': str(con_dir), 'CONTROLS_json_sha256': sha_file(con_dir / 'CONTROLS.json'),
                     'all_as_intended': CON['all_as_intended'],
                     'summary': [{kk: c.get(kk) for kk in ('name', 'expected_status', 'observed_status',
                                                          'observed_error', 'as_intended')} for c in CON['controls']]},
        'corpus_attempts': [{'dir': str(a), 'META_sha256': sha_file(a / 'META.json') if (a / 'META.json').is_file()
                             else None,
                             'STOP': json.loads((a / 'STOP.json').read_bytes()) if (a / 'STOP.json').is_file() else None,
                             'DONE': json.loads((a / 'DONE.json').read_bytes()) if (a / 'DONE.json').is_file() else None}
                            for a in attempts],
        'counts': {'planned': len(rows), 'with_receipt': sum(1 for x in rows if x['status'] != 'NOT_RUN'),
                   'passed': len(passed), 'by_status': {}, 'checker_path': paths},
        'c11_passed_root_ids': passed,
        'non_passed': [{'id': x['id'], 'status': x['status'], 'reasons': x.get('reasons')} for x in rows
                       if not x['accepted']],
        'excluded_unknown_roots': PIN['excluded_unknown_roots'],
        'resources': {'max_checker_ru_maxrss_bytes': max((x['checker_ru_maxrss_bytes'] or 0) for x in res) if res else None,
                      'max_aggregate_rss_sampled_bytes': max((x['aggregate_rss_peak_sampled_bytes'] or 0) for x in res)
                      if res else None,
                      'max_self_maxrss_bytes': max((x['self_maxrss_lifetime_bytes'] or 0) for x in res) if res else None,
                      'sum_checker_wall_s': round(sum(x['checker_wall_s'] or 0 for x in res), 2),
                      'sum_case_wall_s': round(sum(x['case_wall_s'] or 0 for x in res), 2),
                      'sum_checker_cpu_s': round(sum(x['checker_cpu_s'] or 0 for x in res), 2),
                      'any_rss_guard_trip': any(x['rss_guard_tripped'] for x in res),
                      'any_wall_trip': any(x['wall_tripped'] for x in res)},
        'problems': problems, 'per_root': rows}
    for x in rows:
        fin['counts']['by_status'][x['status']] = fin['counts']['by_status'].get(x['status'], 0) + 1
    write_json_new(d / 'FINAL.json', fin)
    print(json.dumps({'final': str(d / 'FINAL.json'), 'passed': len(passed), 'counts': fin['counts'],
                      'problems': problems}), flush=True)
    return 0 if not problems and len(passed) == N_ROOTS else 3


def main():
    signal.signal(signal.SIGTERM, _forward_sigterm)
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cmd = sys.argv[1]
    if cmd == 'pin':
        return phase_pin()
    if cmd == 'controls':
        return phase_controls()
    if cmd == 'corpus':
        retry = set()
        if len(sys.argv) == 4 and sys.argv[2] == '--retry':
            retry = set(sys.argv[3].split(','))
        elif len(sys.argv) != 2:
            raise SystemExit('usage: corpus [--retry ID,ID]')
        return phase_corpus(retry)
    if cmd == 'final':
        return phase_final()
    raise SystemExit('unknown phase ' + cmd)


if __name__ == '__main__':
    sys.exit(main())
