"""Parent re-solve of a deterministic sample of PhysDepolarizing's streamed (non-retained) K5 refinement certificates
(phys-1 lane moqls8, ledger v007).  Independent re-solve evidence for sampled leaves only; NO verdict on K5.

Phases (each creates a fresh exclusive attempt directory <phase>-aN/ here; nothing is overwritten or deleted):
  pin       exclusive copies of ledger v007, strict_L3 + strict_L2 RESULTS/META and the parent-integrated encoder-binding
            receipts; one full SHA-256 + strict structural validation of the pinned base CNF; identity binding of every
            depth-2/3 leaf (canonical chain literals, ledger evidence line hash -> RESULTS record); SELECTION.json (rule
            + 17-leaf sample) is written BEFORE anything else is computed for the sample; then the in-process leaf-CNF
            SHA-256 of every sample leaf is compared with the worker's recorded cnf_sha256.        -> PIN.json
  controls  checker sensitivity / positive controls, tiny pipeline controls, wrong-cube binding, K5 classical SAT
            control (encoder binding C12 'strong' instance), real-leaf empty-prefix control with independent
            insufficiency evidence, joint-guard and solver-limit controls.                        -> CONTROLS.json
  sample    the 17 sample leaves, one at a time, in SELECTION order.                              -> per-case receipts
  final     aggregate receipt over the latest receipt of every sample leaf.                       -> FINAL.json

Per case (never more than two busy processes of ours; the python generator/feeder counts as busy while active):
  0  pre-bind: leaf CNF bytes generated in-process = b'p cnf V C+k\\n' + pinned base body (all bytes after its first
     line, unchanged) + b'<lit> 0\\n' per ledger literal; SHA-256 must equal the worker's cnf_sha256 (else
     REJECT_BINDING, nothing spawned).  Python alone.
  1  solve:  generator -> anonymous pipe -> cadical stdin ('-'); cadical -q -t 1800 writes binary DRAT into the named
     FIFO proof.fifo of the attempt dir; this process holds the FIFO reader plus a dummy writer (closed only after
     the solver is reaped, so EOF is unambiguous) and keeps the proof in RAM only, hashing it.  No proof file exists.
     Busy: generator + cadical while parsing; then cadical alone (the RAM reader is I/O-bound; its CPU is recorded).
  2  check:  only if the solver exited by itself with 10 or 20: the same CNF bytes (generated again, /dev/fd pipe)
     and the in-RAM proof (stdin pipe) are fed to the parent drat-trim (-i -t 1800).  Busy: feeder + drat-trim, then
     drat-trim alone.  Solve and check are staged (never concurrent) to lower the joint RSS peak.
  PASS = pre-bind equal; both CNF deliveries hash-equal; solver self-exit rc 20 with exactly 's UNSATISFIABLE';
         checker self-exit rc 0 with exactly one status line 's VERIFIED' ('\\r' stripped), proof bytes delivered =
         proof bytes produced = proof bytes drat-trim reports reading, expected header, empty stderr, no fatal
         warning; no guard trip.
Joint guard: every <= 2 s the RSS of all phys-1 processes (cwd inside the moqls8 lane or inside this directory, plus
their descendants; libproc, no helper processes) is summed; > 7.5 GiB -> SIGTERM our active process (the solver; the
checker if the solver had already finished), bounded wait 30 s, case UNKNOWN_CAP.  No SIGKILL ever.  Storage guard
before each case (projected growth + margin vs the 12e9 floor and the 1 GiB new-data target) and during it.
Checkpoint JSON at least every 25 min and after every case (CHECKPOINT-NNN.json in this directory).

Usage: /opt/homebrew/bin/python3 -B k5_refine_resolve_v1.py {pin|controls|sample|final}
"""
from __future__ import annotations

import ctypes
import datetime
import gc
import gzip
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
from collections import defaultdict
from pathlib import Path

RUN = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16')
HERE = RUN / 'review' / 'moqls8-k5-refine-parent-resolve-v1'
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
K5 = LANE / 'evidence' / 'k5_split_v1'
BASE = LANE / 'evidence' / 'gram_dev_v1' / 'GA5L_K5_sb2.cnf'
DT = RUN / 'review' / 'moqls7-parent-proofcheck-v1' / 'drat-trim'
CAD = Path('/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical')
BINDDIR = RUN / 'review' / 'moqls8-encoder-binding-v1'

DT_SHA = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
CAD_SHA = '601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa'
BASE_SHA = '6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b'
BASE_BYTES, BASE_VARS, BASE_CLAUSES = 137664569, 509915, 5740230
LEDGER_SHA = 'aba9dd48c45cb7d10026c1f5a280dac28fc877bf018567a8936b2ba9f0a86b03'
INTEG_SHA = '9020f45921e249abed51f3a2141363c3a9cb801dc87a37933413523805a5394f'
BINDV2_SHA = 'dce638a92804bd04f2c3e9f64c61ba35e1d5e7c098df9323ebdac57c56bb6112'
K5BIND_SHA = '0a1be0504563b9d41f8a10f8cc3493b63a8489d03b61c327e744fccf23494ce7'
NAMES_SHA = 'b8423861d03b6e837317c12ef1f2f297301d1bfbbfb7852b93ccec29b85e2522'
C12_STRONG_SHA = '419b2a3424df99fd3842f7ddd91f3a7d42441199831abe3281f26e5fc3acda53'
EXTRA_LEAF = 'c016.L2.040.L3.040'
KISSAT_PID = 53322

PINNED = (  # (name in pin dir, source, expected SHA-256 or None = record only)
    ('LEDGER.v007.json', K5 / 'ledger' / 'LEDGER.v007.json', LEDGER_SHA),
    ('LEDGER.v007.validation.93265896.json', K5 / 'ledger' / 'LEDGER.v007.validation.93265896.json', None),
    ('strict_L3.RESULTS.jsonl', K5 / 'strict_L3' / 'RESULTS.jsonl', None),
    ('strict_L3.META.1792284119.json', K5 / 'strict_L3' / 'META.1792284119.json', None),
    ('strict_L2.RESULTS.jsonl', K5 / 'strict_L2' / 'RESULTS.jsonl', None),
    ('strict_L2.META.1792281134.json', K5 / 'strict_L2' / 'META.1792281134.json', None),
    ('moqls8-encoder-parent-integration-v1.json', RUN / 'review' / 'moqls8-encoder-parent-integration-v1.json',
     INTEG_SHA),
    ('binding-result.v2.json', BINDDIR / 'binding-result.v2.json', BINDV2_SHA),
    ('K5.bind.json', BINDDIR / 'K5.bind.json', K5BIND_SHA),
    ('K5.names.json.gz', BINDDIR / 'K5.names.json.gz', NAMES_SHA),
)

CHUNK = 1 << 20
T_SOLVER = 1800
T_CHECKER = 1800
WALL_MARGIN = 120.0
JOINT_LIMIT = int(7.5 * 2 ** 30)
JOINT_PERIOD = 2.0
LOOP_S = 0.05
STOP_WAIT = 30.0
PROOF_CAP = 1 << 30
LOG_CAP = 128 << 20
FREE_FLOOR = 12_000_000_000
FREE_MARGIN = 512 << 20
RUN_FREE_MIN = FREE_FLOOR + (256 << 20)
NEWDATA_TARGET = 1 << 30
CASE_PROJECTION = 64 << 20
ADMIT_MAX = 40 * 60.0
ADMIT_MARGIN = 256 << 20
CHECKPOINT_S = 25 * 60.0
STDOUT_READ_CAP = 64 << 20
ENV = {'PATH': '/usr/bin:/bin', 'LC_ALL': 'C'}   # no CADICAL_* variables can reach the solver

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
            'platform': platform.platform(), 'pid': os.getpid(), 'cwd': os.getcwd()}


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


# ---------------------------------------------------------------- libproc (no helper processes)
class _TaskInfo(ctypes.Structure):
    _fields_ = ([(n, ctypes.c_uint64) for n in ('virtual_size', 'resident_size', 'total_user', 'total_system',
                                                'threads_user', 'threads_system')] +
                [(n, ctypes.c_int32) for n in ('policy', 'faults', 'pageins', 'cow_faults', 'messages_sent',
                                               'messages_received', 'syscalls_mach', 'syscalls_unix', 'csw',
                                               'threadnum', 'numrunning', 'priority')])


class _BsdInfo(ctypes.Structure):
    _fields_ = ([(n, ctypes.c_uint32) for n in ('flags', 'status', 'xstatus', 'pid', 'ppid', 'uid', 'gid', 'ruid',
                                                'rgid', 'svuid', 'svgid', 'rfu_1')] +
                [('comm', ctypes.c_char * 16), ('name', ctypes.c_char * 32)] +
                [(n, ctypes.c_uint32) for n in ('nfiles', 'pgid', 'pjobc', 'e_tdev', 'e_tpgid')] +
                [('nice', ctypes.c_int32), ('start_tvsec', ctypes.c_uint64), ('start_tvusec', ctypes.c_uint64)])


assert ctypes.sizeof(_BsdInfo) == 136 and ctypes.sizeof(_TaskInfo) == 96
_LIBPROC = ctypes.CDLL('/usr/lib/libproc.dylib', use_errno=True)
_LIBPROC.proc_pidinfo.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int]
_LIBPROC.proc_pidinfo.restype = ctypes.c_int
_LIBPROC.proc_listallpids.argtypes = [ctypes.c_void_p, ctypes.c_int]
_LIBPROC.proc_listallpids.restype = ctypes.c_int
PROC_PIDTBSDINFO, PROC_PIDTASKINFO, PROC_PIDVNODEPATHINFO = 3, 4, 9
VNODEPATHINFO_SIZE, CDIR_PATH_OFFSET = 2352, 152


def rss_of(pid):
    ti = _TaskInfo()
    n = _LIBPROC.proc_pidinfo(pid, PROC_PIDTASKINFO, 0, ctypes.byref(ti), ctypes.sizeof(ti))
    return int(ti.resident_size) if n == ctypes.sizeof(ti) else None


def bsd_of(pid):
    bi = _BsdInfo()
    n = _LIBPROC.proc_pidinfo(pid, PROC_PIDTBSDINFO, 0, ctypes.byref(bi), ctypes.sizeof(bi))
    return bi if n == ctypes.sizeof(bi) else None


class JointSampler:
    """phys-1 process set = processes whose cwd is inside the moqls8 lane or inside this directory, this process,
    and all descendants of those; RSS summed from libproc task info."""

    def __init__(self):
        self.pidbuf = (ctypes.c_int * 32768)()
        self.vbuf = ctypes.create_string_buffer(VNODEPATHINFO_SIZE)
        self.lane, self.here = str(LANE), str(HERE)
        self.samples = 0
        self.cost_s = 0.0

    def _in(self, cwd, root):
        return cwd == root or cwd.startswith(root + '/')

    def sample(self, top=12):
        t0 = time.monotonic()
        n = _LIBPROC.proc_listallpids(self.pidbuf, ctypes.sizeof(self.pidbuf))
        pids = [self.pidbuf[i] for i in range(max(n, 0)) if self.pidbuf[i] > 0]
        info = {}
        for pid in pids:
            bi = bsd_of(pid)
            if bi is None:
                continue
            k = _LIBPROC.proc_pidinfo(pid, PROC_PIDVNODEPATHINFO, 0, self.vbuf, VNODEPATHINFO_SIZE)
            cwd = ''
            if k == VNODEPATHINFO_SIZE:
                cwd = self.vbuf.raw[CDIR_PATH_OFFSET:CDIR_PATH_OFFSET + 1024].split(b'\0', 1)[0].decode('utf-8',
                                                                                                      'replace')
            info[pid] = (int(bi.ppid), bi.comm.decode('utf-8', 'replace'), cwd)
        me = os.getpid()
        members = {pid for pid, (_, _, cwd) in info.items() if self._in(cwd, self.lane) or self._in(cwd, self.here)}
        members.add(me)
        kids = defaultdict(list)
        for pid, (pp, _, _) in info.items():
            kids[pp].append(pid)
        stack = list(members)
        while stack:
            p = stack.pop()
            for c in kids.get(p, ()):
                if c not in members:
                    members.add(c)
                    stack.append(c)
        total = mine = 0
        rows = []
        for pid in members:
            r = rss_of(pid)
            if r is None:
                continue
            pp, comm, cwd = info.get(pid, (None, '?', ''))
            is_mine = pid == me or self._in(cwd, self.here)
            total += r
            mine += r if is_mine else 0
            rows.append([pid, pp, comm, r, 'here' if self._in(cwd, self.here) else
                         ('lane' if self._in(cwd, self.lane) else ('self' if pid == me else 'descendant')), is_mine])
        rows.sort(key=lambda x: -x[3])
        dt = time.monotonic() - t0
        self.samples += 1
        self.cost_s += dt
        return {'at': now(), 'total': total, 'mine': mine, 'others': total - mine, 'n_members': len(rows),
                'n_pids_scanned': len(pids), 'top': rows[:top], 'cost_s': round(dt, 4)}


def kissat_status():
    bi = bsd_of(KISSAT_PID)
    if bi is None:
        return {'pid': KISSAT_PID, 'alive': False}
    return {'pid': KISSAT_PID, 'alive': True, 'comm': bi.comm.decode('utf-8', 'replace'),
            'start_tvsec': int(bi.start_tvsec)}


class Checkpointer:
    def __init__(self, phase, attempt):
        self.phase, self.attempt, self.last = phase, attempt, -1e18

    def write(self, note, state):
        for n in range(1, 10000):
            p = HERE / ('CHECKPOINT-%03d.json' % n)
            try:
                with open(p, 'xb') as f:
                    f.write((json.dumps({'at': now(), 'phase': self.phase, 'attempt': str(self.attempt),
                                         'runner_sha256': RUNNER_SHA, 'note': note,
                                         'free_bytes': shutil.disk_usage(HERE).free, 'own_bytes': dir_bytes(HERE),
                                         'state': state}, indent=1) + '\n').encode())
                self.last = time.monotonic()
                return str(p)
            except FileExistsError:
                continue
        raise SystemExit('no checkpoint slot')

    def maybe(self, note, state_fn):
        if time.monotonic() - self.last >= CHECKPOINT_S:
            self.write(note, state_fn())


def wait_for_kissat(ck, state_fn):
    first = kissat_status()
    while True:
        s = kissat_status()
        if not s['alive'] or s.get('comm') != 'kissat':
            return {'initial': first, 'final': s}
        ck.maybe('waiting for worker kissat pid %d to exit' % KISSAT_PID, state_fn)
        time.sleep(5.0)


# ---------------------------------------------------------------- base CNF validation (once, at pin)
HEADER_RE = re.compile(rb'p cnf ([1-9][0-9]*) ([1-9][0-9]*)\n')
LINE_RE = re.compile(rb'(?:-?[1-9][0-9]* )+0')
DIGITS_RE = re.compile(rb'[0-9]+')


class BaseInvalid(Exception):
    pass


def validate_base(path):
    """Single pass: SHA-256 of file and body + strict DIMACS structure (exact header, exactly C canonical clause lines,
    |lit| <= V, no comments/blank lines/other whitespace/trailing bytes)."""
    t0 = time.monotonic()
    h_all, h_body = hashlib.sha256(), hashlib.sha256()
    with open(path, 'rb') as f:
        header = f.readline(4096)
        m = HEADER_RE.fullmatch(header)
        if not m:
            raise BaseInvalid('header is not exactly "p cnf V C\\n": %r' % header[:80])
        nvars, nclauses = int(m.group(1)), int(m.group(2))
        h_all.update(header)
        lines = maxvar = body_bytes = 0
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
            maxvar = max(maxvar, max(map(int, DIGITS_RE.findall(complete)), default=0))
        if carry:
            raise BaseInvalid('file does not end with a newline-terminated clause line')
    if lines != nclauses:
        raise BaseInvalid('clause lines %d != header clauses %d' % (lines, nclauses))
    if maxvar > nvars:
        raise BaseInvalid('literal magnitude %d exceeds header vars %d' % (maxvar, nvars))
    return {'path': str(path), 'sha256': h_all.hexdigest(), 'bytes': len(header) + body_bytes,
            'header': header.decode('ascii'), 'nvars': nvars, 'nclauses': nclauses, 'body_sha256': h_body.hexdigest(),
            'body_bytes': body_bytes, 'clause_lines': lines, 'max_var_seen': maxvar, 'validated_at': now(),
            'validation_s': round(time.monotonic() - t0, 2)}


# ---------------------------------------------------------------- CNF stream specification
class CnfSpec:
    """header + base body (optionally without the 0-based clause lines in `drop`) + one '<u> 0' line per unit."""

    def __init__(self, base_path, base_rec, units=(), drop=()):
        self.base_path, self.base_rec = Path(base_path), base_rec
        self.units = [int(u) for u in units]
        self.drop = sorted(set(int(i) for i in drop))
        self.clauses = base_rec['nclauses'] - len(self.drop) + len(self.units)
        self.header = b'p cnf %d %d\n' % (base_rec['nvars'], self.clauses)
        self.unit_bytes = b''.join(b'%d 0\n' % u for u in self.units)

    def describe(self):
        return {'base_path': str(self.base_path), 'base_sha256_pinned': self.base_rec['sha256'],
                'base_body_sha256_pinned': self.base_rec['body_sha256'], 'units': len(self.units),
                'units_sha256': sha_bytes(self.unit_bytes), 'dropped_line_indices': self.drop,
                'header': self.header.decode()}

    def chunks(self, st):
        """st collects: raw base header/body hash+bytes+newlines, dropped lines, generated bytes are hashed by the
        consumer.  Raises on a base header mismatch or any structural surprise (fail closed)."""
        st.update(body_h=hashlib.sha256(), body_bytes=0, body_newlines=0, dropped=[], gen_done=False)
        drop = self.drop
        with open(self.base_path, 'rb') as f:
            hdr = f.readline(4096)
            st['base_header_read'] = hdr.decode('ascii', 'replace')
            if hdr != self.base_rec['header'].encode():
                raise ValueError('base header changed: %r' % hdr[:80])
            yield self.header
            line_no, k, carry = 0, 0, b''
            while True:
                b = f.read(CHUNK)
                if not b:
                    break
                st['body_h'].update(b)
                st['body_bytes'] += len(b)
                nl = b.count(b'\n')
                st['body_newlines'] += nl
                if k >= len(drop):
                    if carry:
                        b = carry + b
                        carry = b''
                    yield b
                    continue
                block = carry + b
                cut = block.rfind(b'\n')
                if cut < 0:
                    carry = block
                    continue
                complete, carry = block[:cut + 1], block[cut + 1:]
                cnt = complete.count(b'\n')
                if drop[k] >= line_no + cnt:
                    yield complete
                    line_no += cnt
                    continue
                lines = complete.split(b'\n')[:-1]
                out = []
                for i, ln in enumerate(lines):
                    if k < len(drop) and drop[k] == line_no + i:
                        st['dropped'].append([line_no + i, ln.decode('ascii', 'replace')])
                        k += 1
                    else:
                        out.append(ln + b'\n')
                line_no += cnt
                if out:
                    yield b''.join(out)
            if carry:
                if k < len(drop):
                    raise ValueError('unterminated final base line while drops pending')
                yield carry
            if k != len(drop):
                raise ValueError('only %d of %d drop indices found' % (k, len(drop)))
        for i in range(0, len(self.unit_bytes), CHUNK):
            yield self.unit_bytes[i:i + CHUNK]
        st['gen_done'] = True


def prebind(cnf):
    """In-process generation + hash (python alone)."""
    t0 = time.monotonic()
    st = {}
    h, n = hashlib.sha256(), 0
    for c in cnf.chunks(st):
        h.update(c)
        n += len(c)
    return {'sha256': h.hexdigest(), 'bytes': n, 'base_body_sha256': st['body_h'].hexdigest(),
            'base_body_bytes': st['body_bytes'], 'base_body_newlines': st['body_newlines'],
            'dropped_lines': st['dropped'], 'secs': round(time.monotonic() - t0, 3)}


# ---------------------------------------------------------------- streaming helpers
class Feed:
    """Non-blocking writer of one generator stream into one pipe; hashes exactly the delivered bytes."""

    def __init__(self, name, fd, src):
        self.name, self.fd, self.src = name, fd, src
        self.h, self.n = hashlib.sha256(), 0
        self.src_h, self.src_n = hashlib.sha256(), 0
        self.pending = memoryview(b'')
        self.closed = self.source_done = False
        self.source_error = self.sink_error = None
        self.closed_at = self.done_at = None

    def close(self, t0, note=None):
        if not self.closed:
            os.close(self.fd)
            self.closed = True
            self.closed_at = round(time.monotonic() - t0, 3)
            if note and not self.sink_error and not self.source_done:
                self.sink_error = note

    def pump(self, t0):
        start = time.monotonic()
        while not self.closed:
            if not self.pending:
                try:
                    chunk = next(self.src)
                except StopIteration:
                    self.source_done = True
                    self.done_at = round(time.monotonic() - t0, 3)
                    self.close(t0)
                    return
                except Exception as e:  # generator failure: fail closed
                    self.source_error = '%s: %s' % (type(e).__name__, e)
                    self.close(t0)
                    return
                self.src_h.update(chunk)
                self.src_n += len(chunk)
                self.pending = memoryview(chunk)
                continue
            try:
                k = os.write(self.fd, self.pending)
            except BlockingIOError:
                return
            except OSError as e:
                self.sink_error = '%s: errno=%s %s' % (type(e).__name__, e.errno, e.strerror)
                self.close(t0)
                return
            self.h.update(self.pending[:k])
            self.n += k
            self.pending = self.pending[k:]
            if time.monotonic() - start > LOOP_S:
                return

    def report(self):
        return {'source_done': self.source_done, 'source_error': self.source_error, 'sink_error': self.sink_error,
                'source_sha256': self.src_h.hexdigest(), 'source_bytes': self.src_n,
                'delivered_sha256': self.h.hexdigest(), 'delivered_bytes': self.n,
                'delivered_complete': self.source_done and self.sink_error is None and self.n == self.src_n,
                'done_at_s': self.done_at, 'closed_at_s': self.closed_at}


def mem_chunks(buf):
    mv = memoryview(buf)
    for i in range(0, len(mv), CHUNK):
        yield bytes(mv[i:i + CHUNK])


_ACTIVE = {'pid': None}


def _forward_sigterm(signum, frame):
    pid = _ACTIVE.get('pid')
    if pid:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    raise SystemExit(128 + signum)


class Guard:
    """Shared periodic checks for a running child: joint RSS, wall, output-file sizes, free space, proof cap."""

    def __init__(self, joint, ck, state_fn, joint_limit, wall_limit, logs, label):
        self.joint, self.ck, self.state_fn = joint, ck, state_fn
        self.joint_limit, self.wall_limit, self.logs, self.label = joint_limit, wall_limit, logs, label
        self.last = -1e18
        self.trips = {}
        self.peak = {'total': 0, 'mine': 0, 'others_at_peak': 0, 'mine_max': 0, 'others_max': 0, 'samples': 0,
                     'top_at_peak': None}
        self.trace = []
        self.last_trace = -1e18

    def tick(self, t_spawn, proof_len=0):
        """Returns the reason string of a NEW trip (caller sends SIGTERM), else None."""
        t = time.monotonic()
        reason = None
        if t - t_spawn > self.wall_limit and 'wall' not in self.trips:
            self.trips['wall'] = {'t_s': round(t - t_spawn, 2)}
            reason = 'wall watchdog'
        if proof_len > PROOF_CAP and 'proof_cap' not in self.trips:
            self.trips['proof_cap'] = {'bytes': proof_len}
            reason = reason or 'in-RAM proof cap'
        if t - self.last >= JOINT_PERIOD:
            self.last = t
            s = self.joint.sample()
            p = self.peak
            p['samples'] += 1
            p['mine_max'] = max(p['mine_max'], s['mine'])
            p['others_max'] = max(p['others_max'], s['others'])
            if s['total'] > p['total']:
                p.update(total=s['total'], mine=s['mine'], others_at_peak=s['others'], top_at_peak=s['top'])
            if t - self.last_trace >= 10.0:
                self.last_trace = t
                self.trace.append([round(t - t_spawn, 1), s['total'], s['mine'], s['others']])
            if s['total'] > self.joint_limit and 'joint' not in self.trips:
                self.trips['joint'] = {'t_s': round(t - t_spawn, 2), 'total': s['total'], 'mine': s['mine'],
                                       'others': s['others'], 'limit': self.joint_limit, 'top': s['top']}
                reason = reason or 'joint phys-1 RSS guard'
            for lp in self.logs:
                try:
                    sz = lp.stat().st_size
                except FileNotFoundError:
                    continue
                if sz > LOG_CAP and 'log_cap' not in self.trips:
                    self.trips['log_cap'] = {'file': lp.name, 'bytes': sz}
                    reason = reason or 'output file cap'
            free = shutil.disk_usage(HERE).free
            if free < RUN_FREE_MIN and 'storage' not in self.trips:
                self.trips['storage'] = {'free_bytes': free, 'min_free': RUN_FREE_MIN}
                reason = reason or 'storage floor guard'
            self.ck.maybe('running %s' % self.label, self.state_fn)
        return reason

    def report(self):
        return {'trips': self.trips, 'joint_limit': self.joint_limit, 'wall_limit_s': self.wall_limit,
                'peak_sampled': self.peak, 'trace_10s': self.trace}


def child_exit(child, t_spawn):
    if child is None:
        return None
    status, ru, t_exit = child
    rc = os.waitstatus_to_exitcode(status)
    return {'returncode': rc, 'signaled': rc < 0, 'signal': -rc if rc < 0 else None,
            'wall_s': round(t_exit - t_spawn, 3), 'ru_maxrss_bytes': ru.ru_maxrss,
            'ru_utime_s': round(ru.ru_utime, 3), 'ru_stime_s': round(ru.ru_stime, 3)}


def own_cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


# ---------------------------------------------------------------- solve stage
def solve_stage(d, name, cnf, joint, ck, state_fn, *, t_limit, extra_args=(), want_proof=True,
                joint_limit=JOINT_LIMIT):
    rec = {'stage': 'solve', 'started_at': now()}
    fifo = d / 'proof.fifo'
    prf_r = prf_dummy = None
    if want_proof:
        prf_r = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
        prf_dummy = os.open(fifo, os.O_WRONLY | os.O_NONBLOCK)
    argv = [str(CAD), '-q', *extra_args, '-t', str(t_limit), '-'] + ([str(fifo)] if want_proof else [])
    out_p, err_p = d / ('%s.solver.stdout' % name), d / ('%s.solver.stderr' % name)
    out_f, err_f = open(out_p, 'xb'), open(err_p, 'xb')
    cnf_r, cnf_w = os.pipe()
    rec['command'] = {'argv': argv, 'cwd': str(d), 'env': ENV, 'stdin': 'anonymous pipe (generated CNF stream)',
                      'proof': 'named FIFO %s read into RAM by the runner' % fifo.name if want_proof else None,
                      'stdout': out_p.name, 'stderr': err_p.name}
    cpu0 = own_cpu()
    t_spawn = time.monotonic()
    rec['spawned_at'] = now()
    proc = subprocess.Popen(argv, stdin=cnf_r, stdout=out_f, stderr=err_f, env=ENV, cwd=str(d), close_fds=True)
    _ACTIVE['pid'] = proc.pid
    rec['solver_pid'] = proc.pid
    os.close(cnf_r)
    out_f.close()
    err_f.close()
    os.set_blocking(cnf_w, False)
    st = {}
    feed = Feed('cnf', cnf_w, cnf.chunks(st))
    proof = bytearray()
    ph = hashlib.sha256()
    first_proof_t = None
    proof_eof = False
    guard = Guard(joint, ck, state_fn, joint_limit, t_limit + WALL_MARGIN, [out_p, err_p], 'solve ' + name)
    child = None
    term_at = None
    stop_failed = False
    sigterms = []

    def read_proof():
        nonlocal first_proof_t, proof_eof
        while prf_r is not None:
            try:
                b = os.read(prf_r, CHUNK)
            except BlockingIOError:
                return
            if not b:
                proof_eof = True
                return
            if first_proof_t is None:
                first_proof_t = round(time.monotonic() - t_spawn, 3)
            proof.extend(b)
            ph.update(b)

    while True:
        if child is None:
            pid, status, ru = os.wait4(proc.pid, os.WNOHANG)
            if pid == proc.pid:
                child = (status, ru, time.monotonic())
                _ACTIVE['pid'] = None
        if child is not None:
            if not feed.closed:
                feed.close(t_spawn, 'solver exited before the CNF was fully delivered')
            break
        rl = [prf_r] if prf_r is not None else []
        wl = [] if feed.closed else [cnf_w]
        try:
            r, w, _ = select.select(rl, wl, [], LOOP_S)
        except InterruptedError:
            r, w = [], []
        if r:
            read_proof()
        if w:
            feed.pump(t_spawn)
        reason = guard.tick(t_spawn, len(proof))
        if reason and term_at is None:
            sigterms.append({'reason': reason, 't_s': round(time.monotonic() - t_spawn, 3), 'at': now()})
            try:
                os.kill(proc.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            term_at = time.monotonic()
        if term_at is not None and time.monotonic() - term_at > STOP_WAIT:
            stop_failed = True
            break
    if prf_dummy is not None:
        os.close(prf_dummy)
    drain_t0 = time.monotonic()
    while prf_r is not None and not proof_eof and not stop_failed and time.monotonic() - drain_t0 < STOP_WAIT:
        r, _, _ = select.select([prf_r], [], [], 1.0)
        if r:
            read_proof()
    if prf_r is not None:
        os.close(prf_r)
    if not feed.closed:
        feed.close(t_spawn, 'closed by runner after stop failure')
    rec['exit'] = child_exit(child, t_spawn)
    rec['stop_failed'] = stop_failed
    rec['sigterm'] = sigterms
    rec['guard'] = guard.report()
    rec['runner_cpu_s_during_stage'] = round(own_cpu() - cpu0, 3)
    out_size = out_p.stat().st_size
    with open(out_p, 'rb') as f:
        out_b = f.read(STDOUT_READ_CAP)
    lines = [x.strip() for x in out_b.decode('utf-8', 'replace').split('\n')]
    rec['output'] = {'stdout_bytes': out_size, 'stdout_sha256': sha_file(out_p), 'stderr_bytes': err_p.stat().st_size,
                     'stderr_sha256': sha_file(err_p), 'status_lines': [x for x in lines if x.startswith('s ')],
                     'witness_lines': sum(1 for x in lines if x.startswith('v ')),
                     'comment_lines_head': [x for x in lines if x.startswith('c ')][:10]}
    rec['cnf_stream'] = dict(feed.report(), base_body_sha256=st.get('body_h').hexdigest() if st.get('body_h') else None,
                             base_body_bytes=st.get('body_bytes'), base_body_newlines=st.get('body_newlines'),
                             dropped_lines=len(st.get('dropped') or []), generator_done=st.get('gen_done'))
    rec['proof'] = {'wanted': want_proof, 'bytes': len(proof), 'sha256': ph.hexdigest(), 'eof_seen': proof_eof,
                    'first_byte_at_s': first_proof_t, 'kept_in_ram_only': True}
    rec['ended_at'] = now()
    return rec, proof, out_b


# ---------------------------------------------------------------- check stage
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
            'error_lines': errors[:20], 'no_conflict_line': 'c ERROR: no conflict' in lines, 'checker_path': path,
            'core': core, 'line_count': len(lines)}


def check_stage(d, name, cnf, proof, joint, ck, state_fn, *, t_limit=T_CHECKER, joint_limit=JOINT_LIMIT):
    rec = {'stage': 'check', 'started_at': now(), 'checker': {'path': str(DT), 'sha256': sha_file(DT),
                                                               'expected_sha256': DT_SHA}}
    cnf_r, cnf_w = os.pipe()
    prf_r, prf_w = os.pipe()
    argv = [str(DT), '/dev/fd/%d' % cnf_r, '-i', '-t', str(t_limit)]
    out_p, err_p = d / ('%s.drat-trim.stdout' % name), d / ('%s.drat-trim.stderr' % name)
    out_f, err_f = open(out_p, 'xb'), open(err_p, 'xb')
    rec['command'] = {'argv': argv, 'cwd': str(d), 'env': ENV,
                      'argv1': 'anonymous pipe (generated CNF stream) opened by drat-trim via /dev/fd',
                      'stdin': 'anonymous pipe (in-RAM proof bytes, binary DRAT, -i)', 'stdout': out_p.name,
                      'stderr': err_p.name}
    cpu0 = own_cpu()
    t_spawn = time.monotonic()
    rec['spawned_at'] = now()
    proc = subprocess.Popen(argv, stdin=prf_r, stdout=out_f, stderr=err_f, pass_fds=(cnf_r,), env=ENV, cwd=str(d))
    _ACTIVE['pid'] = proc.pid
    rec['checker_pid'] = proc.pid
    os.close(cnf_r)
    os.close(prf_r)
    out_f.close()
    err_f.close()
    os.set_blocking(cnf_w, False)
    os.set_blocking(prf_w, False)
    st = {}
    feeds = [Feed('cnf', cnf_w, cnf.chunks(st)), Feed('proof', prf_w, mem_chunks(proof))]
    guard = Guard(joint, ck, state_fn, joint_limit, t_limit + WALL_MARGIN, [out_p, err_p], 'check ' + name)
    child = None
    term_at = None
    stop_failed = False
    sigterms = []
    while True:
        if child is None:
            pid, status, ru = os.wait4(proc.pid, os.WNOHANG)
            if pid == proc.pid:
                child = (status, ru, time.monotonic())
                _ACTIVE['pid'] = None
        live = [f for f in feeds if not f.closed]
        if child is not None and not live:
            break
        if live and child is None:
            try:
                _, w, _ = select.select([], [f.fd for f in live], [], LOOP_S)
            except InterruptedError:
                w = []
            for f in live:
                if f.fd in w:
                    f.pump(t_spawn)
        elif live:
            for f in live:
                f.pump(t_spawn)
            if time.monotonic() - child[2] > 5.0:
                for f in live:
                    f.close(t_spawn, 'forced close 5 s after checker exit')
            time.sleep(0.01)
        else:
            time.sleep(LOOP_S)
        if child is None:
            reason = guard.tick(t_spawn)
            if reason and term_at is None:
                sigterms.append({'reason': reason, 't_s': round(time.monotonic() - t_spawn, 3), 'at': now()})
                try:
                    os.kill(proc.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                term_at = time.monotonic()
            if term_at is not None and time.monotonic() - term_at > STOP_WAIT:
                stop_failed = True
                break
    for f in feeds:
        if not f.closed:
            f.close(t_spawn, 'closed by runner after stop failure')
    rec['exit'] = child_exit(child, t_spawn)
    rec['stop_failed'] = stop_failed
    rec['sigterm'] = sigterms
    rec['guard'] = guard.report()
    rec['runner_cpu_s_during_stage'] = round(own_cpu() - cpu0, 3)
    out_size, err_size = out_p.stat().st_size, err_p.stat().st_size
    with open(out_p, 'rb') as f:
        out_b = f.read(STDOUT_READ_CAP)
    with open(err_p, 'rb') as f:
        err_b = f.read(4096)
    rec['output'] = dict(parse_checker_output(out_b.decode('utf-8', 'replace')), stdout_bytes=out_size,
                         stdout_sha256=sha_file(out_p), stderr_bytes=err_size, stderr_sha256=sha_file(err_p),
                         stderr_head=err_b[:400].decode('utf-8', 'replace'))
    rec['cnf_stream'] = dict(feeds[0].report(),
                             base_body_sha256=st.get('body_h').hexdigest() if st.get('body_h') else None)
    rec['proof_stream'] = feeds[1].report()
    rec['ended_at'] = now()
    return rec


# ---------------------------------------------------------------- witness check (SAT controls)
def model_check(cnf, stdout_bytes, nvars):
    t0 = time.monotonic()
    val = bytearray(nvars + 1)          # 0 unassigned, 1 true, 2 false
    dup = bad = 0
    ended = False
    for line in stdout_bytes.decode('ascii', 'replace').split('\n'):
        if not line.startswith('v '):
            continue
        for tok in line[2:].split():
            x = int(tok)
            if x == 0:
                ended = True
                continue
            v = abs(x)
            if v > nvars:
                bad += 1
                continue
            if val[v]:
                dup += 1
            val[v] = 1 if x > 0 else 2
    unassigned = sum(1 for v in range(1, nvars + 1) if not val[v])
    unassigned_occurring = set()
    st = {}
    first = True
    violated = clauses = 0
    examples = []
    carry = b''
    for c in cnf.chunks(st):
        if first:
            first = False
            continue
        block = carry + c
        cut = block.rfind(b'\n')
        if cut < 0:
            carry = block
            continue
        carry = block[cut + 1:]
        for ln in block[:cut].split(b'\n'):
            clauses += 1
            sat = False
            for tok in ln.split():
                x = int(tok)
                if x == 0:
                    break
                v = abs(x)
                if not val[v]:
                    unassigned_occurring.add(v)
                elif val[v] == (1 if x > 0 else 2):
                    sat = True
                    break
            if not sat:
                violated += 1
                if len(examples) < 5:
                    examples.append(ln.decode('ascii', 'replace')[:120])
    return {'witness_terminated': ended, 'witness_duplicates': dup, 'witness_out_of_range': bad,
            'unassigned_vars_total': unassigned, 'unassigned_vars_occurring_in_instance': len(unassigned_occurring),
            'clauses_evaluated': clauses, 'expected_clauses': cnf.clauses, 'clauses_violated': violated,
            'violation_examples': examples, 'trailing_bytes': len(carry), 'secs': round(time.monotonic() - t0, 2),
            'ok': (ended and dup == 0 and bad == 0 and not unassigned_occurring and violated == 0 and
                   clauses == cnf.clauses and not carry)}


# ---------------------------------------------------------------- one case
def storage_ok():
    free = shutil.disk_usage(HERE).free
    own = dir_bytes(HERE)
    ok = free - CASE_PROJECTION - FREE_MARGIN >= FREE_FLOOR and own + CASE_PROJECTION <= NEWDATA_TARGET
    return ok, {'free_bytes': free, 'own_bytes': own, 'projection_bytes': CASE_PROJECTION, 'margin_bytes': FREE_MARGIN,
                'floor_bytes': FREE_FLOOR, 'newdata_target_bytes': NEWDATA_TARGET}


def admit(joint, ck, state_fn, expected_peak, joint_limit):
    t0 = time.monotonic()
    waits = 0
    while True:
        s = joint.sample()
        need = s['total'] + expected_peak
        if need <= joint_limit - ADMIT_MARGIN:
            return {'admitted': True, 'waited_s': round(time.monotonic() - t0, 1), 'polls': waits + 1,
                    'expected_peak_bytes': expected_peak, 'sample': s}
        if time.monotonic() - t0 > ADMIT_MAX:
            return {'admitted': False, 'proceeded_after_max_wait': True, 'waited_s': round(time.monotonic() - t0, 1),
                    'polls': waits + 1, 'expected_peak_bytes': expected_peak, 'sample': s}
        waits += 1
        ck.maybe('admission wait (joint %d + expected %d > limit-margin)' % (s['total'], expected_peak), state_fn)
        time.sleep(5.0)


def run_case(d, name, case, joint, ck, state_fn):
    t_case = time.monotonic()
    cnf = case['cnf']
    rec = {'case': name, 'kind': case['kind'], 'meta': case.get('meta', {}), 'started_at': now(),
           'runner_sha256': RUNNER_SHA, 'cnf_spec': cnf.describe(),
           'expected_cnf_sha256': case['expected_cnf_sha256'], 'plan': {
               'solve': case.get('solve', True), 'check': case.get('check', True),
               'solver_extra_args': case.get('solver_extra', []), 't_solver': case.get('t_solver', T_SOLVER),
               'want_proof': case.get('want_proof', True), 'joint_limit': case.get('joint_limit', JOINT_LIMIT),
               'proof_override_sha256': sha_bytes(case['proof_override']) if case.get('proof_override') is not None
               else None, 'model_check': case.get('model_check', False)}}

    def finish(status, reasons):
        rec.update({'status': status, 'reasons': reasons, 'accepted': status == 'PASS' and case['kind'] == 'leaf',
                    'ended_at': now(), 'case_wall_s': round(time.monotonic() - t_case, 3)})
        write_json_new(d / ('%s.json' % name), rec)
        ck.write('case %s -> %s' % (name, status), state_fn())
        return rec

    ok, sto = storage_ok()
    rec['storage_before'] = sto
    if not ok:
        return finish('UNKNOWN_STORAGE', ['storage projection would cross the floor or the new-data target'])
    pb = prebind(cnf)
    rec['prebind'] = pb
    if pb['sha256'] != case['expected_cnf_sha256'] or pb['base_body_sha256'] != cnf.base_rec['body_sha256']:
        return finish('REJECT_BINDING', ['prebind_cnf_sha256' if pb['sha256'] != case['expected_cnf_sha256']
                                         else 'base_body_sha256'])
    checks = {'prebind_cnf_sha256': True}
    joint_limit = case.get('joint_limit', JOINT_LIMIT)
    proof = case.get('proof_override')
    solver = None
    if case.get('solve', True):
        rec['admission'] = admit(joint, ck, state_fn, case.get('expected_peak', 1 << 30), JOINT_LIMIT)
        solver, proof, sout = solve_stage(d, name, cnf, joint, ck, state_fn, t_limit=case.get('t_solver', T_SOLVER),
                                          extra_args=case.get('solver_extra', []),
                                          want_proof=case.get('want_proof', True), joint_limit=joint_limit)
        rec['solve'] = solver
        ex = solver['exit'] or {}
        cs = solver['cnf_stream']
        checks.update({
            'solver_cnf_delivered_complete': cs['delivered_complete'],
            'solver_cnf_delivered_sha256': cs['delivered_sha256'] == case['expected_cnf_sha256'],
            'solver_base_body_sha256': cs['base_body_sha256'] == cnf.base_rec['body_sha256'],
            'solver_not_stopped': not solver['sigterm'] and not solver['stop_failed'],
            'solver_self_exit': bool(ex) and ex['returncode'] >= 0,
            'solver_stderr_empty': solver['output']['stderr_bytes'] == 0,
        })
        if case.get('want_proof', True):
            checks['proof_eof_seen'] = solver['proof']['eof_seen']
        if case.get('model_check') and ex.get('returncode') == 10:
            rec['model_check'] = model_check(cnf, sout, cnf.base_rec['nvars'])
            checks['model_check_ok'] = rec['model_check']['ok']
        del sout
    checker = None
    srv = (solver or {}).get('exit') or {}
    run_check = case.get('check', True) and (solver is None or (
        checks.get('solver_not_stopped') and checks.get('solver_self_exit') and srv.get('returncode') in (10, 20)
        and checks.get('solver_cnf_delivered_sha256')))
    if run_check:
        checker = check_stage(d, name, cnf, proof if proof is not None else b'', joint, ck, state_fn,
                              joint_limit=joint_limit)
        rec['check'] = checker
        co = checker['output']
        ex = checker['exit'] or {}
        exp_proof_sha = (solver['proof']['sha256'] if solver is not None else sha_bytes(case['proof_override']))
        exp_proof_n = len(proof) if proof is not None else 0
        read = co['finished_parsing_proof_bytes']
        checks.update({
            'checker_sha256': checker['checker']['sha256'] == DT_SHA,
            'checker_cnf_delivered_complete': checker['cnf_stream']['delivered_complete'],
            'checker_cnf_delivered_sha256': checker['cnf_stream']['delivered_sha256'] == case['expected_cnf_sha256'],
            'checker_proof_delivered_complete': checker['proof_stream']['delivered_complete'],
            'checker_proof_delivered_sha256': checker['proof_stream']['delivered_sha256'] == exp_proof_sha,
            'checker_not_stopped': not checker['sigterm'] and not checker['stop_failed'],
            'checker_header': co['parsed_header'] == [[cnf.base_rec['nvars'], cnf.clauses]],
            'checker_read_proof_from_stdin': co['reading_from_stdin'],
            'checker_consumed_all_proof_bytes': read == [exp_proof_n] or (exp_proof_n == 0 and read == [None]),
            'checker_stderr_empty': co['stderr_bytes'] == 0,
        })
        verified_clean = (ex.get('returncode') == 0 and co['status_lines'] == ['s VERIFIED'] and
                          not co['fatal_warnings'] and not co['unclassified_warnings'] and not co['error_lines'] and
                          len(co['checker_path']) == 1)
        not_verified = ex.get('returncode') == 1 and co['status_lines'] == ['s NOT VERIFIED']
        checks['checker_verified_clean'] = verified_clean
    reasons = [k for k, v in checks.items() if not v]
    stages = [x for x in (solver, checker) if x]
    trips = {k for s in stages for k in s['guard']['trips']}
    if any(s['stop_failed'] for s in stages):
        return finish('UNKNOWN_STOP_FAILED', reasons)
    if 'storage' in trips or 'log_cap' in trips:
        return finish('UNKNOWN_STORAGE', reasons)
    if 'joint' in trips or 'proof_cap' in trips:
        return finish('UNKNOWN_CAP', reasons)
    if 'wall' in trips:
        return finish('UNKNOWN_TIMEOUT', reasons)
    s_lines = solver['output']['status_lines'] if solver is not None else None
    rc = srv.get('returncode')
    if solver is not None and rc == 0 and s_lines == ['s UNKNOWN']:
        return finish('UNKNOWN_LIMIT' if '-c' in case.get('solver_extra', []) else 'UNKNOWN_TIMEOUT', reasons)
    binding_keys = ('solver_cnf_delivered_complete', 'solver_cnf_delivered_sha256', 'solver_base_body_sha256',
                    'checker_sha256', 'checker_cnf_delivered_complete', 'checker_cnf_delivered_sha256',
                    'checker_proof_delivered_complete', 'checker_proof_delivered_sha256', 'proof_eof_seen')
    if any(not checks[k] for k in binding_keys if k in checks):
        return finish('REJECT_BINDING', reasons)
    if solver is not None:
        if rc == 10 and s_lines == ['s SATISFIABLE']:
            return finish('SAT', reasons)
        if not (rc == 20 and s_lines == ['s UNSATISFIABLE']):
            return finish('UNKNOWN_OTHER', reasons)
        if checker is None:
            return finish('UNSAT_UNCHECKED', reasons)
    if checker is None:
        return finish('UNKNOWN_OTHER', reasons)
    co = checker['output']
    if 's TIMEOUT' in co['status_lines']:
        return finish('UNKNOWN_TIMEOUT', reasons)
    if not reasons:
        return finish('PASS' if solver is not None else 'CHECKER_VERIFIED', reasons)
    if (not_verified and checks['checker_header'] and checks['checker_consumed_all_proof_bytes'] and
            checks['checker_stderr_empty']):
        return finish('REJECT_CHECKER', reasons)
    return finish('UNKNOWN_OTHER', reasons)


def observed(r):
    so = ((r.get('solve') or {}).get('output') or {})
    se = ((r.get('solve') or {}).get('exit') or {})
    co = ((r.get('check') or {}).get('output') or {})
    ce = ((r.get('check') or {}).get('exit') or {})
    return {'status': r['status'], 'solver_rc': se.get('returncode'), 'solver_status': so.get('status_lines'),
            'checker_rc': ce.get('returncode'), 'checker_status': co.get('status_lines'),
            'checker_no_conflict_line': co.get('no_conflict_line'), 'checker_path': co.get('checker_path'),
            'sigterm': [x['reason'] for x in ((r.get('solve') or {}).get('sigterm') or [])] +
                       [x['reason'] for x in ((r.get('check') or {}).get('sigterm') or [])],
            'model_check_ok': (r.get('model_check') or {}).get('ok'), 'prebind_sha256': (r.get('prebind') or {}).get(
                'sha256'), 'solver_spawned': 'solve' in r, 'checker_spawned': 'check' in r}


# ---------------------------------------------------------------- pin phase
def canon(prefix, chain, index):
    return list(prefix) + [v if (index >> j) & 1 else -v for j, v in enumerate(chain)]


def phase_pin():
    d = new_attempt('pin')
    rec = {'phase': 'pin', 'started_at': now(), 'runner': runner_identity(), 'files': {}, 'problems': []}
    P = rec['problems']

    def req(cond, msg):
        if not cond:
            P.append(msg)
        return bool(cond)

    for name, src, expect in PINNED:
        data = src.read_bytes()
        h = sha_bytes(data)
        write_new(d / name, data)
        h_after, h_copy = sha_file(src), sha_file(d / name)
        rec['files'][name] = {'source': str(src), 'sha256': h, 'bytes': len(data), 'expected_sha256': expect,
                              'source_sha256_after_copy': h_after, 'copy_sha256': h_copy}
        req(h == h_after == h_copy, 'pin copy/hash instability: ' + name)
        if expect:
            req(h == expect, 'pinned SHA mismatch: %s %s != %s' % (name, h, expect))
    # parent-integrated encoder binding
    integ = json.loads((d / 'moqls8-encoder-parent-integration-v1.json').read_bytes())
    bind = json.loads((d / 'binding-result.v2.json').read_bytes())
    k5b = bind['bases']['K5']
    req(integ.get('binding_sha256') == BINDV2_SHA and integ.get('status') == 'CNF_BINDING_INTEGRATED_ONLY' and
        'C1' in integ.get('accepted_obligations', []), 'integration record does not bind binding-result.v2 / C1')
    req(k5b['regenerated'] == {'sha256': BASE_SHA, 'bytes': BASE_BYTES, 'vars': BASE_VARS, 'clauses': BASE_CLAUSES},
        'binding K5 regenerated base differs from the pinned base')
    req(all(k5b['C1_byte_identity'].values()), 'binding C1 byte identity not all true')
    req(k5b['full_name_table']['sha256'] == NAMES_SHA, 'binding name table SHA differs')
    rec['encoder_binding'] = {'integration_status': integ.get('status'), 'accepted': integ.get('accepted_obligations'),
                              'C11': integ.get('C11'), 'K5_regenerated': k5b['regenerated'],
                              'K5_C1_byte_identity': k5b['C1_byte_identity'], 'K5_encoder_copy': k5b['encoder_copy'],
                              'K5_encoder_argv_used': k5b['encoder_argv_used']}
    # base CNF (once)
    try:
        base_rec = validate_base(BASE)
    except BaseInvalid as e:
        base_rec = None
        P.append('base CNF invalid: %s' % e)
    if base_rec:
        req(base_rec['sha256'] == BASE_SHA and base_rec['bytes'] == BASE_BYTES, 'base CNF SHA/bytes mismatch')
        req((base_rec['nvars'], base_rec['nclauses']) == (BASE_VARS, BASE_CLAUSES), 'base dims mismatch')
    rec['base'] = base_rec
    rec['checker'] = {'path': str(DT), 'sha256': sha_file(DT), 'expected_sha256': DT_SHA}
    req(rec['checker']['sha256'] == DT_SHA, 'checker SHA mismatch')
    ver = subprocess.run([str(CAD), '--version'], capture_output=True, text=True, env=ENV)
    rec['solver'] = {'path': str(CAD), 'sha256': sha_file(CAD), 'expected_sha256': CAD_SHA,
                     'version': ver.stdout.strip(), 'version_rc': ver.returncode}
    req(rec['solver']['sha256'] == CAD_SHA and rec['solver']['version'] == '3.0.1', 'solver SHA/version mismatch')
    # ledger and RESULTS identity binding
    L = json.loads((d / 'LEDGER.v007.json').read_bytes())
    req(L.get('schema') == 'k5-cover-ledger/1' and L.get('version') == 7, 'ledger schema/version')
    req(L.get('base_cnf_sha256') == BASE_SHA and L.get('base_vars') == BASE_VARS and
        L.get('base_clauses') == BASE_CLAUSES, 'ledger base binding')
    chain = L['chain']
    leaves = {x['id']: x for x in L['leaves']}
    req(len(leaves) == len(L['leaves']), 'duplicate ledger ids')

    def jsonl(name):
        out = {}
        for line in (d / name).read_bytes().split(b'\n'):
            if line:
                h = sha_bytes(line)
                req(h not in out, 'duplicate line in ' + name)
                out[h] = json.loads(line)
        return out

    res = {'strict_L3/RESULTS.jsonl': jsonl('strict_L3.RESULTS.jsonl'),
           'strict_L2/RESULTS.jsonl': jsonl('strict_L2.RESULTS.jsonl')}
    used = {k: set() for k in res}
    bound = {}
    for lid, x in leaves.items():
        if x['depth'] < 2:
            continue
        anc = leaves.get(x['ancestor'])
        if not req(anc is not None and anc['depth'] == x['depth'] - 1 and anc['state'] == 'REFINED',
                   lid + ' ancestor'):
            continue
        req(x['lits'] == canon(anc['lits'], chain[str(x['depth'])], x['index']) and 0 <= x['index'] < 128,
            lid + ' lits are not ancestor + canonical chain pattern')
        ev = x.get('evidence') or {}
        f = ev.get('file')
        if not req(ev.get('kind') == 'strict' and f in res, lid + ' evidence kind/file'):
            continue
        r = res[f].get(ev.get('line_sha256'))
        if not req(r is not None, lid + ' evidence line not found'):
            continue
        used[f].add(ev['line_sha256'])
        req(r['id'] == lid and r['depth'] == x['depth'] and r['index'] == x['index'] and
            r['ancestor'] == x['ancestor'] and r['lits'] == x['lits'], lid + ' RESULTS identity')
        req(r['base_cnf_sha256'] == BASE_SHA and r['cnf_vars'] == BASE_VARS and
            r['cnf_clauses'] == BASE_CLAUSES + len(x['lits']), lid + ' RESULTS CNF dims')
        ok = r.get('strict_ok') is True
        req(ok == (x['state'] == 'CERTIFIED'), lid + ' strict_ok vs ledger state')
        if ok:
            req(r['solver_returncode'] == 20 and r['solver_status_lines'] == ['s UNSATISFIABLE'] and
                r['checker_returncode'] == 0 and r['checker_status_lines'] == ['s VERIFIED'] and
                r['verified'] is True and r['self_exit'] is True and r['rss_guard_tripped'] is False and
                not r['relay_errors'] and not r['feed_errors'], lid + ' strict_ok record fields')
        bound[lid] = (f, ev['line_sha256'], r)
    for f in res:
        req(used[f] == set(res[f]), f + ' has lines not bound by a ledger leaf')
    req(all(r['ancestor'] == 'c016' for r in res['strict_L2/RESULTS.jsonl'].values()), 'strict_L2 not all c016')
    # selection (frozen before any computation on the sample)
    d3 = sorted(lid for lid, (f, _, r) in bound.items() if f == 'strict_L3/RESULTS.jsonl' and r['strict_ok'] is True
                and leaves[lid]['state'] == 'CERTIFIED')
    d2 = sorted(lid for lid, (f, _, r) in bound.items() if f == 'strict_L2/RESULTS.jsonl' and r['strict_ok'] is True
                and leaves[lid]['state'] == 'CERTIFIED' and r['ancestor'] == 'c016')
    s3, s2 = d3[0::16], d2[0::16]
    req(len(s3) == 8 and len(s2) == 8, 'sample sizes are not 8 + 8')
    req(EXTRA_LEAF in d3 and EXTRA_LEAF not in s3, 'extra leaf not a separate strict-OK depth-3 child')
    order = s3 + s2 + [EXTRA_LEAF]
    sel = {
        'written_at': now(), 'runner_sha256': RUNNER_SHA,
        'rule': ("Frozen before any solve. D3 = ids of strict_L3/RESULTS.jsonl records with strict_ok == true whose "
                 "ledger-v007 leaf is CERTIFIED and binds that record by line SHA-256, sorted ascending (zero-padded "
                 "ids, string order = index order); D2 = the same for strict_L2/RESULTS.jsonl records with ancestor "
                 "'c016'. Sample = D3[0::16] + D2[0::16] + ['%s'] (the 268.9 s depth-3 child), solved in that "
                 "order, one at a time." % EXTRA_LEAF),
        'ledger_sha256': rec['files']['LEDGER.v007.json']['sha256'],
        'results_sha256': {'strict_L3': rec['files']['strict_L3.RESULTS.jsonl']['sha256'],
                           'strict_L2': rec['files']['strict_L2.RESULTS.jsonl']['sha256']},
        'D3_count': len(d3), 'D2_count': len(d2), 'D3_positions': list(range(0, len(d3), 16)),
        'D2_positions': list(range(0, len(d2), 16)), 'sample_depth3': s3, 'sample_depth2': s2,
        'extra': EXTRA_LEAF, 'order': order,
        'worker_records': {lid: {k: bound[lid][2][k] for k in (
            'id', 'depth', 'index', 'ancestor', 'lits', 'attempt_tag', 'cnf_sha256', 'cnf_clauses', 'cnf_vars', 'secs',
            'aggregate_peak_rss_bytes', 'proof_stream_bytes', 'proof_stream_sha256', 'solver_argv', 'checker_argv',
            'solver_returncode', 'checker_returncode', 'strict_ok')} | {'results_file': bound[lid][0],
                                                                        'line_sha256': bound[lid][1]}
            for lid in order}}
    write_json_new(d / 'SELECTION.json', sel)
    rec['selection'] = {'file': 'SELECTION.json', 'sha256': sha_file(d / 'SELECTION.json'), 'order': order}
    # pre-bind every sample leaf (python alone)
    rec['prebind'] = {}
    if base_rec:
        for lid in order:
            w = sel['worker_records'][lid]
            pb = prebind(CnfSpec(BASE, base_rec, units=leaves[lid]['lits']))
            pb['worker_cnf_sha256'] = w['cnf_sha256']
            pb['match'] = pb['sha256'] == w['cnf_sha256'] and pb['base_body_sha256'] == base_rec['body_sha256']
            req(pb['match'], lid + ' leaf CNF SHA differs from the worker record')
            rec['prebind'][lid] = pb
    rec['plan'] = [{'id': lid, 'depth': leaves[lid]['depth'], 'index': leaves[lid]['index'],
                    'ancestor': leaves[lid]['ancestor'], 'lits': leaves[lid]['lits'],
                    'expected_cnf_sha256': sel['worker_records'][lid]['cnf_sha256'],
                    'worker': sel['worker_records'][lid]} for lid in order]
    rec['kissat'] = kissat_status()
    joint = JointSampler()
    rec['joint_sample_at_pin'] = joint.sample(top=20)
    rec['ended_at'] = now()
    write_json_new(d / 'PIN.json', rec)
    print(json.dumps({'pin_dir': str(d), 'problems': P, 'order': order, 'base_validation_s': base_rec and
                      base_rec['validation_s'], 'joint_total': rec['joint_sample_at_pin']['total'],
                      'joint_top': rec['joint_sample_at_pin']['top'][:6]}), flush=True)
    return 0 if not P else 2


def load_pin():
    pin_dir, PIN = latest_ok('pin', 'PIN.json', lambda o: o.get('problems') == [] and
                             o['runner']['sha256'] == RUNNER_SHA)
    return pin_dir, PIN, sha_file(pin_dir / 'PIN.json')


# ---------------------------------------------------------------- controls phase
def gf8_mul(a, b):
    r = 0
    for k in range(3):
        if (b >> k) & 1:
            r ^= a
        a <<= 1
        if a & 0b1000:
            a ^= 0b1011
    return r


def classical_squares():
    """Independent construction of the binding's classical AG(2,8) configuration: L_m(i,j) = j + m*i over
    GF(8) = GF(2)[x]/(x^3+x+1); K5 slopes {1:1,2:4,3:5,4:6,5:7}; new row i <- old row [0,1,7,6,5,4,3,2][i]."""
    slopes = {1: 1, 2: 4, 3: 5, 4: 6, 5: 7}
    perm = [0, 1, 7, 6, 5, 4, 3, 2]
    return {s: [[j ^ gf8_mul(m, perm[i]) for j in range(8)] for i in range(8)] for s, m in slopes.items()}


def phase_controls():
    pin_dir, PIN, pin_sha = load_pin()
    base_rec = PIN['base']
    plan = {r['id']: r for r in PIN['plan']}
    d = new_attempt('controls')
    os.mkfifo(d / 'proof.fifo')
    fx = d / 'fixtures'
    fx.mkdir()
    ck = Checkpointer('controls', d)
    joint = JointSampler()
    rec = {'phase': 'controls', 'started_at': now(), 'runner': runner_identity(),
           'pin': {'dir': str(pin_dir), 'PIN_json_sha256': pin_sha}, 'fixtures': {}, 'controls': []}
    state = {'done': []}

    def state_fn():
        return {'controls_done': list(state['done'])}

    ck.write('controls start', state_fn())
    rec['kissat_wait'] = wait_for_kissat(ck, state_fn)

    def fixture(fname, data):
        write_new(fx / fname, data)
        rec['fixtures'][fname] = {'sha256': sha_bytes(data), 'bytes': len(data)}
        return fx / fname

    tiny_unsat = fixture('tiny_unsat_2vars_4clauses.cnf', b'p cnf 2 4\n1 2 0\n-1 2 0\n1 -2 0\n-1 -2 0\n')
    tiny_sat = fixture('tiny_sat.cnf', b'p cnf 3 2\n1 2 0\n-1 3 0\n')
    tu_rec, ts_rec = validate_base(tiny_unsat), validate_base(tiny_sat)
    hand_proof = bytes([0x61, 0x04, 0x00, 0x61, 0x00])   # a (2) 0 ; a () 0  -- RUP lemma x2, then empty clause
    fixture('tiny_valid_refutation.drat', hand_proof)
    fixture('empty.drat', b'')
    L3040, L2000, L3000 = plan[EXTRA_LEAF], plan['c016.L2.000'], plan['c016.L2.040.L3.000']

    def leaf_cnf(row, lits=None):
        return CnfSpec(BASE, base_rec, units=row['lits'] if lits is None else lits)

    # K5 classical SAT control: binding C12 'strong' instance, constructed here from pinned binding receipts
    bind = json.loads((pin_dir / 'binding-result.v2.json').read_bytes())
    k5bind = json.loads((pin_dir / 'K5.bind.json').read_bytes())
    sq = classical_squares()
    sq_listed = bind['controls']['c12_classical_set']['K5']['squares']
    squares_equal = all(sq[s] == sq_listed[str(s)] for s in sq)
    names = json.loads(gzip.decompress((pin_dir / 'K5.names.json.gz').read_bytes()))
    gnames = {v: nm for v, nm in names if nm[0] == 'g'}
    gunits = []
    for v in sorted(gnames):
        _, s, a, b = gnames[v]
        gunits.append(v if sq[s][a[0]][a[1]] == sq[s][b[0]][b[1]] else -v)
    alo = k5bind['classification']['p4']['alo_clause_indices']
    sb2 = k5bind['classification']['sb2_unit_index']
    sb2_sq1 = [i for i, sg, nm in sb2 if nm[1] == 1]
    strong_drop = sorted(alo + sb2_sq1)
    runs = {r['label']: r for r in bind['controls']['c12_solver_runs']['K5']}
    s1_cnf = CnfSpec(BASE, base_rec, units=gunits, drop=strong_drop)
    s1_pre = prebind(s1_cnf)
    gpos = {abs(u): u for u in gunits}
    mutated = [gpos[abs(x)] for x in L3040['lits']]
    s1_info = {
        'definition': 'binding C12 strong: base minus the P4 at-least-one (non-classical flag) clauses minus the SB2 '
                      'units of square 1, plus one unit per g variable fixing the classical Gram pattern',
        'classical_squares_constructed_here_equal_binding_listing': squares_equal,
        'g_variables': len(gunits), 'g_units_true': sum(1 for u in gunits if u > 0),
        'relaxation_dropped_clause_indices': strong_drop, 'p4_alo_indices': alo, 'sb2_square1_indices': sb2_sq1,
        'dropped_clauses_as_read': s1_pre['dropped_lines'],
        'sb2_square1_declared': [[i, sg, nm] for i, sg, nm in sb2 if nm[1] == 1],
        'binding_canonical_assignment_violations': bind['controls']['c12_canonical_assignment_full_base']['K5'],
        'instance_sha256': s1_pre['sha256'], 'binding_strong_instance_sha256': runs['K5:strong']['instance_sha256'],
        'instance_sha256_equals_binding_strong': s1_pre['sha256'] == C12_STRONG_SHA ==
        runs['K5:strong']['instance_sha256'],
        'instance_clauses': s1_cnf.clauses, 'binding_strong_instance_clauses': runs['K5:strong']['instance_clauses'],
        'mutated_cube_relation': {
            'leaf': EXTRA_LEAF, 'leaf_cube': L3040['lits'], 'classical_signs_on_leaf_cube_vars': mutated,
            'flipped_positions': [i for i, (a, b) in enumerate(zip(L3040['lits'], mutated)) if a != b],
            'note': 'the SAT control cube is the full 7840-literal classical Gram cube; on the 21 variables of the '
                    'leaf cube it is the leaf cube with the listed signs flipped'}}
    dropped = {i: ln for i, ln in s1_pre['dropped_lines']}
    g_by_name = {json.dumps(nm): v for v, nm in gnames.items()}
    sb2_ok = all(dropped.get(i, '').strip() == '%d 0' % (g_by_name[json.dumps(nm)] * (1 if sg else -1))
                 for i, sg, nm in sb2 if nm[1] == 1)
    alo_lines = [dropped.get(i) for i in alo]
    alo_vars = sorted({abs(int(t)) for ln in alo_lines if ln for t in ln.split()[:-1]})
    need = set(alo_vars)
    alo_names = {v: nm for v, nm in names if v in need}
    del names
    gc.collect()
    s1_info['sb2_dropped_lines_equal_declared_square1_units'] = sb2_ok
    s1_info['alo_dropped_lines'] = alo_lines
    s1_info['alo_literal_signs_all_positive'] = all(int(t) > 0 for ln in alo_lines if ln for t in ln.split()[:-1])
    s1_info['alo_literal_var_kinds'] = sorted({alo_names[v][0] for v in alo_vars if v in alo_names})
    s1_info['alo_literal_names_head'] = [[v, alo_names.get(v)] for v in alo_vars[:6]]
    s1_info['alo_clause_count'] = len([ln for ln in alo_lines if ln])
    rec['S1_construction'] = s1_info
    del gnames, g_by_name, alo_names
    gc.collect()

    C = [
        ('K1_tiny_empty_proof_sensitivity',
         'checker sensitivity: (1v2)(-1v2)(1v-2)(-1v-2) has no unit clause, so unit propagation alone cannot refute '
         'it; an EMPTY proof stream must NOT verify',
         dict(kind='control', cnf=CnfSpec(tiny_unsat, tu_rec), expected_cnf_sha256=tu_rec['sha256'], solve=False,
              proof_override=b''),
         'REJECT_CHECKER', {'checker_rc': 1, 'checker_status': ['s NOT VERIFIED'], 'checker_no_conflict_line': True,
                            'solver_spawned': False}),
        ('K2_tiny_hand_refutation_positive', 'positive checker control: hand-written RUP refutation (x2, empty)',
         dict(kind='control', cnf=CnfSpec(tiny_unsat, tu_rec), expected_cnf_sha256=tu_rec['sha256'], solve=False,
              proof_override=hand_proof),
         'CHECKER_VERIFIED', {'checker_rc': 0, 'checker_status': ['s VERIFIED'], 'checker_path': ['backward_check']}),
        ('K3_tiny_unsat_full_pipeline', 'positive pipeline control: cadical -> FIFO -> RAM -> drat-trim on the '
         'tiny UNSAT CNF', dict(kind='control', cnf=CnfSpec(tiny_unsat, tu_rec), expected_cnf_sha256=tu_rec['sha256'],
                               expected_peak=64 << 20),
         'PASS', {'solver_rc': 20, 'solver_status': ['s UNSATISFIABLE'], 'checker_rc': 0,
                  'checker_status': ['s VERIFIED']}),
        ('K4_tiny_sat_full_pipeline', 'tiny SAT CNF through the full pipeline: SAT, witness checked, checker '
         'must not verify', dict(kind='control', cnf=CnfSpec(tiny_sat, ts_rec), expected_cnf_sha256=ts_rec['sha256'],
                                 model_check=True, expected_peak=64 << 20),
         'SAT', {'solver_rc': 10, 'solver_status': ['s SATISFIABLE'], 'model_check_ok': True, 'checker_rc': 1,
                 'checker_status': ['s NOT VERIFIED']}),
        ('B1_wrong_cube_binding', 'leaf c016.L2.040.L3.000 with its last cube literal negated must fail the CNF '
         'hash binding before anything is spawned',
         dict(kind='control', cnf=leaf_cnf(L3000, L3000['lits'][:-1] + [-L3000['lits'][-1]]),
              expected_cnf_sha256=L3000['expected_cnf_sha256']),
         'REJECT_BINDING', {'solver_spawned': False, 'checker_spawned': False}),
        ('S1_classical_relaxed_K5_SAT', 'K5 SAT control: classical AG(2,8) configuration from the encoder binding '
         'as a full Gram cube on the base relaxed by the C12 strong drops (5 P4 at-least-one + 7 SB2 square-1 '
         'units); expected SAT with a checked model; checker must not verify',
         dict(kind='control', cnf=s1_cnf, expected_cnf_sha256=C12_STRONG_SHA, model_check=True,
              expected_peak=int(1.5 * 2 ** 30)),
         'SAT', {'solver_rc': 10, 'solver_status': ['s SATISFIABLE'], 'model_check_ok': True, 'checker_rc': 1,
                 'checker_status': ['s NOT VERIFIED']}),
        ('U1a_L3040_root_UP_independent', 'independent insufficiency evidence for the empty prefix: cadical with '
         'conflict limit 0 (root propagation only, no proof) on the L3.040 leaf CNF',
         dict(kind='control', cnf=leaf_cnf(L3040), expected_cnf_sha256=L3040['expected_cnf_sha256'],
              solver_extra=['-c', '0'], t_solver=300, want_proof=False, check=False, expected_peak=int(1.5 * 2 ** 30)),
         'UNKNOWN_LIMIT', {'solver_rc': 0, 'solver_status': ['s UNKNOWN'], 'checker_spawned': False}),
        ('U1b_L3040_empty_prefix', 'real leaf L3.040 with the proof stream truncated to its empty prefix (shown '
         'insufficient by U1a): must NOT verify',
         dict(kind='control', cnf=leaf_cnf(L3040), expected_cnf_sha256=L3040['expected_cnf_sha256'], solve=False,
              proof_override=b''),
         'REJECT_CHECKER', {'checker_rc': 1, 'checker_status': ['s NOT VERIFIED'], 'checker_no_conflict_line': True}),
        ('T1_solver_native_limit', 'cadical -t 1 on the L3.040 leaf: native limit reached -> UNKNOWN, no check',
         dict(kind='control', cnf=leaf_cnf(L3040), expected_cnf_sha256=L3040['expected_cnf_sha256'], t_solver=1,
              expected_peak=int(1.5 * 2 ** 30)),
         'UNKNOWN_TIMEOUT', {'solver_rc': 0, 'solver_status': ['s UNKNOWN'], 'checker_spawned': False}),
    ]
    for cname, purpose, case, want, obs in C:
        r = run_case(d, cname, case, joint, ck, state_fn)
        o = observed(r)
        ok = r['status'] == want and all(o.get(k) == v for k, v in obs.items())
        rec['controls'].append({'name': cname, 'purpose': purpose, 'expected_status': want,
                                'expected_observations': obs, 'observed': o, 'failed_checks': r['reasons'],
                                'receipt': '%s.json' % cname, 'receipt_sha256': sha_file(d / ('%s.json' % cname)),
                                'as_intended': ok})
        state['done'].append([cname, r['status'], ok])
        print(json.dumps({'control': cname, 'as_intended': ok, 'observed': o}), flush=True)
    # joint-guard control: limit = current phys-1 total + 192 MiB on a small real leaf
    base_sample = joint.sample()
    lim = base_sample['total'] + (192 << 20)
    gcase = dict(kind='control', cnf=leaf_cnf(L2000), expected_cnf_sha256=L2000['expected_cnf_sha256'],
                 joint_limit=lim, expected_peak=0)
    r = run_case(d, 'G1_joint_guard_trip', gcase, joint, ck, state_fn)
    o = observed(r)
    sv = r.get('solve') or {}
    ok = (r['status'] == 'UNKNOWN_CAP' and o['sigterm'][:1] == ['joint phys-1 RSS guard'] and
          not sv.get('stop_failed') and 'check' not in r and bool(sv.get('exit')))
    rec['controls'].append({'name': 'G1_joint_guard_trip', 'purpose': 'joint guard with an artificial limit (phys-1 '
                            'total at start + 192 MiB) on leaf c016.L2.000: SIGTERM to the solver only, bounded stop '
                            '<= 30 s, case UNKNOWN_CAP, no check', 'expected_status': 'UNKNOWN_CAP',
                            'limit_bytes': lim, 'phys1_total_at_start': base_sample['total'], 'observed': o,
                            'solver_exit': sv.get('exit'), 'trip': (sv.get('guard') or {}).get('trips'),
                            'failed_checks': r['reasons'], 'receipt': 'G1_joint_guard_trip.json',
                            'receipt_sha256': sha_file(d / 'G1_joint_guard_trip.json'), 'as_intended': ok})
    state['done'].append(['G1_joint_guard_trip', r['status'], ok])
    print(json.dumps({'control': 'G1_joint_guard_trip', 'as_intended': ok, 'observed': o}), flush=True)
    rec['all_as_intended'] = all(c['as_intended'] for c in rec['controls'])
    rec['joint_sampler'] = {'samples': joint.samples, 'cost_s': round(joint.cost_s, 3)}
    rec['ended_at'] = now()
    write_json_new(d / 'CONTROLS.json', rec)
    ck.write('controls end: all_as_intended=%s' % rec['all_as_intended'], state_fn())
    print(json.dumps({'controls_dir': str(d), 'all_as_intended': rec['all_as_intended'],
                      'n': len(rec['controls']), 'S1_sha_equal': s1_info['instance_sha256_equals_binding_strong']}),
          flush=True)
    return 0 if rec['all_as_intended'] else 2


# ---------------------------------------------------------------- sample phase
def phase_sample():
    pin_dir, PIN, pin_sha = load_pin()
    con_dir, CON = latest_ok('controls', 'CONTROLS.json', lambda o: o.get('all_as_intended') is True and
                             o['runner']['sha256'] == RUNNER_SHA and o['pin']['PIN_json_sha256'] == pin_sha)
    base_rec = PIN['base']
    d = new_attempt('sample')
    os.mkfifo(d / 'proof.fifo')
    ck = Checkpointer('sample', d)
    joint = JointSampler()
    state = {'done': [], 'current': None}

    def state_fn():
        return {'done': list(state['done']), 'current': state['current']}

    write_json_new(d / 'META.json', {'phase': 'sample', 'started_at': now(), 'runner': runner_identity(),
                                     'pin': {'dir': str(pin_dir), 'PIN_json_sha256': pin_sha},
                                     'controls': {'dir': str(con_dir),
                                                  'CONTROLS_json_sha256': sha_file(con_dir / 'CONTROLS.json')},
                                     'order': [r['id'] for r in PIN['plan']]})
    ck.write('sample start', state_fn())
    kw = wait_for_kissat(ck, state_fn)
    write_json_new(d / 'KISSAT_WAIT.json', kw)
    for pos, row in enumerate(PIN['plan']):
        state['current'] = row['id']
        case = dict(kind='leaf', cnf=CnfSpec(BASE, base_rec, units=row['lits']),
                    expected_cnf_sha256=row['expected_cnf_sha256'],
                    expected_peak=max(1 << 30, int(row['worker']['aggregate_peak_rss_bytes'])),
                    meta={'leaf_id': row['id'], 'depth': row['depth'], 'index': row['index'],
                          'ancestor': row['ancestor'], 'order_position': pos, 'worker': row['worker']})
        r = run_case(d, row['id'], case, joint, ck, state_fn)
        so = (r.get('solve') or {})
        co = (r.get('check') or {})
        state['done'].append([row['id'], r['status']])
        state['current'] = None
        print(json.dumps({'pos': pos, 'id': row['id'], 'status': r['status'],
                          'solver': (so.get('exit') or {}).get('returncode'),
                          'solve_wall': (so.get('exit') or {}).get('wall_s'),
                          'check_wall': (co.get('exit') or {}).get('wall_s'),
                          'proof_eq_worker': so.get('proof', {}).get('sha256') == row['worker']['proof_stream_sha256'],
                          'joint_peak': max([x['guard']['peak_sampled']['total'] for x in (so, co) if x] or [0]),
                          'admit_wait': (r.get('admission') or {}).get('waited_s'), 'at': r['ended_at']}), flush=True)
        if r['status'] in ('UNKNOWN_STOP_FAILED', 'UNKNOWN_STORAGE', 'REJECT_BINDING'):
            write_json_new(d / 'STOP.json', {'at': now(), 'reason': 'campaign stop on ' + r['status'], 'id': row['id'],
                                             'done': state['done']})
            ck.write('sample stopped on %s' % r['status'], state_fn())
            return 3
    write_json_new(d / 'DONE.json', {'at': now(), 'done': state['done'],
                                     'joint_sampler': {'samples': joint.samples, 'cost_s': round(joint.cost_s, 3)}})
    ck.write('sample done', state_fn())
    return 0


# ---------------------------------------------------------------- final phase
def phase_final():
    pin_dir, PIN, pin_sha = load_pin()
    con_dir, CON = latest_ok('controls', 'CONTROLS.json', lambda o: o.get('all_as_intended') is True and
                             o['runner']['sha256'] == RUNNER_SHA and o['pin']['PIN_json_sha256'] == pin_sha)
    attempts = attempt_dirs('sample')
    rows = []
    for row in PIN['plan']:
        recs = [a / ('%s.json' % row['id']) for a in attempts if (a / ('%s.json' % row['id'])).is_file()]
        if not recs:
            rows.append({'id': row['id'], 'status': 'NOT_RUN', 'accepted': False})
            continue
        p = recs[-1]
        r = json.loads(p.read_bytes())
        so, co = r.get('solve') or {}, r.get('check') or {}
        se, ce = so.get('exit') or {}, co.get('exit') or {}
        w = row['worker']
        rows.append({
            'id': row['id'], 'depth': row['depth'], 'index': row['index'], 'status': r['status'],
            'accepted_as_parent_resolve': r['status'] == 'PASS' and r['expected_cnf_sha256'] == w['cnf_sha256'],
            'reasons': r['reasons'], 'receipt': {'path': str(p), 'sha256': sha_file(p)},
            'attempt_receipts': [str(x) for x in recs],
            'cnf': {'worker_cnf_sha256': w['cnf_sha256'], 'prebind_sha256': (r.get('prebind') or {}).get('sha256'),
                    'solver_delivered_sha256': (so.get('cnf_stream') or {}).get('delivered_sha256'),
                    'checker_delivered_sha256': (co.get('cnf_stream') or {}).get('delivered_sha256'),
                    'bytes': (r.get('prebind') or {}).get('bytes'),
                    'match': (r.get('prebind') or {}).get('sha256') == w['cnf_sha256'] ==
                    (so.get('cnf_stream') or {}).get('delivered_sha256') ==
                    (co.get('cnf_stream') or {}).get('delivered_sha256')},
            'solver': {'argv': (so.get('command') or {}).get('argv'), 'returncode': se.get('returncode'),
                       'status_lines': (so.get('output') or {}).get('status_lines'), 'wall_s': se.get('wall_s'),
                       'ru_maxrss_bytes': se.get('ru_maxrss_bytes'),
                       'cpu_s': round(se['ru_utime_s'] + se['ru_stime_s'], 3) if se else None},
            'proof': {'bytes': (so.get('proof') or {}).get('bytes'), 'sha256': (so.get('proof') or {}).get('sha256'),
                      'worker_stream_bytes': w['proof_stream_bytes'], 'worker_stream_sha256': w['proof_stream_sha256'],
                      'identical_to_worker_stream': (so.get('proof') or {}).get('sha256') == w['proof_stream_sha256'],
                      'retained': False},
            'checker': {'argv': (co.get('command') or {}).get('argv'), 'sha256': (co.get('checker') or {}).get('sha256'),
                        'returncode': ce.get('returncode'), 'status_lines': (co.get('output') or {}).get('status_lines'),
                        'checker_path': (co.get('output') or {}).get('checker_path'),
                        'proof_bytes_read': (co.get('output') or {}).get('finished_parsing_proof_bytes'),
                        'core': (co.get('output') or {}).get('core'), 'wall_s': ce.get('wall_s'),
                        'ru_maxrss_bytes': ce.get('ru_maxrss_bytes'),
                        'stdout': {'path': str(p.parent / ('%s.drat-trim.stdout' % row['id'])),
                                   'sha256': (co.get('output') or {}).get('stdout_sha256')}},
            'resources': {
                'admission': {k: (r.get('admission') or {}).get(k) for k in ('admitted', 'waited_s',
                                                                             'expected_peak_bytes')},
                'joint_peak_sampled_bytes': max([x['guard']['peak_sampled']['total'] for x in (so, co) if x] or [0]),
                'ours_peak_sampled_bytes': max([x['guard']['peak_sampled']['mine_max'] for x in (so, co) if x] or [0]),
                'others_max_sampled_bytes': max([x['guard']['peak_sampled']['others_max'] for x in (so, co) if x] or
                                                [0]),
                'runner_cpu_s': round(sum(x.get('runner_cpu_s_during_stage', 0) for x in (so, co) if x), 3),
                'case_wall_s': r.get('case_wall_s'), 'guard_trips': {k: v for x in (so, co) if x
                                                                     for k, v in x['guard']['trips'].items()}},
            'worker': {'secs': w['secs'], 'aggregate_peak_rss_bytes': w['aggregate_peak_rss_bytes'],
                       'attempt_tag': w['attempt_tag']},
            'started_at': r.get('started_at'), 'ended_at': r.get('ended_at')})
    by = {}
    for x in rows:
        by[x['status']] = by.get(x['status'], 0) + 1
    done = [x for x in rows if x['status'] != 'NOT_RUN']
    tot = {
        'planned': len(rows), 'with_receipt': len(done), 'by_status': by,
        'pass_ids': [x['id'] for x in rows if x.get('accepted_as_parent_resolve')],
        'cnf_hash_matches': sum(1 for x in done if x['cnf']['match']),
        'proof_identical_to_worker_stream': sum(1 for x in done if x['proof']['identical_to_worker_stream']),
        'sum_solver_wall_s': round(sum(x['solver']['wall_s'] or 0 for x in done), 2),
        'sum_checker_wall_s': round(sum(x['checker']['wall_s'] or 0 for x in done), 2),
        'sum_case_wall_s': round(sum(x['resources']['case_wall_s'] or 0 for x in done), 2),
        'sum_solver_cpu_s': round(sum(x['solver']['cpu_s'] or 0 for x in done), 2),
        'max_solver_ru_maxrss_bytes': max([x['solver']['ru_maxrss_bytes'] or 0 for x in done] or [0]),
        'max_checker_ru_maxrss_bytes': max([x['checker']['ru_maxrss_bytes'] or 0 for x in done] or [0]),
        'max_joint_sampled_bytes': max([x['resources']['joint_peak_sampled_bytes'] for x in done] or [0]),
        'max_ours_sampled_bytes': max([x['resources']['ours_peak_sampled_bytes'] for x in done] or [0]),
        'sum_proof_bytes_in_ram': sum(x['proof']['bytes'] or 0 for x in done),
        'any_guard_trip': any(x['resources']['guard_trips'] for x in done)}
    d = new_attempt('final')
    fin = {'phase': 'final', 'written_at': now(), 'runner': runner_identity(),
           'scope': ('Independent parent re-solve of a frozen deterministic sample (17 of the 253 strict-OK depth-2/3 '
                     'refinement leaves) with CaDiCaL 3.0.1 and the parent drat-trim; leaf CNFs regenerated from the '
                     'pinned, encoder-bound base and the ledger-v007 cube. Sample evidence only: no verdict on K5, '
                     'no statement about unsampled leaves, the 7 UNKNOWN leaves or the cover argument.'),
           'pin': {'dir': str(pin_dir), 'PIN_json_sha256': pin_sha, 'files': PIN['files'], 'base': PIN['base'],
                   'checker': PIN['checker'], 'solver': PIN['solver'], 'selection': PIN['selection'],
                   'encoder_binding': PIN['encoder_binding']},
           'controls': {'dir': str(con_dir), 'CONTROLS_json_sha256': sha_file(con_dir / 'CONTROLS.json'),
                        'all_as_intended': CON['all_as_intended'],
                        'summary': [{k: c.get(k) for k in ('name', 'expected_status', 'as_intended')} |
                                    {'observed_status': c['observed']['status']} for c in CON['controls']],
                        'S1_construction': CON['S1_construction']},
           'sample_attempts': [{'dir': str(a), 'META_sha256': sha_file(a / 'META.json') if (a / 'META.json').is_file()
                                else None, 'STOP': json.loads((a / 'STOP.json').read_bytes())
                                if (a / 'STOP.json').is_file() else None,
                                'DONE': json.loads((a / 'DONE.json').read_bytes()) if (a / 'DONE.json').is_file()
                                else None} for a in attempts],
           'checkpoints': sorted(p.name for p in HERE.glob('CHECKPOINT-*.json')),
           'totals': tot, 'per_leaf': rows,
           'storage': {'own_bytes': dir_bytes(HERE), 'free_bytes': shutil.disk_usage(HERE).free}}
    write_json_new(d / 'FINAL.json', fin)
    print(json.dumps({'final': str(d / 'FINAL.json'), 'totals': tot}), flush=True)
    return 0


def main():
    signal.signal(signal.SIGTERM, _forward_sigterm)
    os.chdir(HERE)
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    cmd = sys.argv[1]
    fn = {'pin': phase_pin, 'controls': phase_controls, 'sample': phase_sample, 'final': phase_final}.get(cmd)
    if fn is None:
        raise SystemExit('unknown phase ' + cmd)
    return fn()


if __name__ == '__main__':
    sys.exit(main())
