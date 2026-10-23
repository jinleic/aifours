#!/usr/bin/env python3
"""SOURCE ONLY, UNEXECUTED. Finite negative/boundary controls, NOT qualification.

Operative oracle: beta-consumer-controls-plan-v2.json, pinned below. V1 plan is
superseded and never executed. No private-validator/source-text/wiring/default
or dummy-prefix position tests. Every genuine baseline, seven frozen negatives,
C1-C4, twenty full-prefix positions and derivation-success path remains deferred.
Exit 0 means only that the executable negative/boundary expectations matched.

Nothing is loaded, compiled, read, written or launched by importing this harness.
All work is inside run(), after external independent review, exact parent GO and
fresh stability gate. Those are external preconditions, not granted by this file.
Run only with -I -B; no arguments. One process, stdlib, no subprocess/network/
threads/signals/date helper. Parent owns timestamps, captures, exit and endedness.
"""
import copy
import errno
import hashlib
import json
import os
import stat
import sys
import time

RUN = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h'
MOLS = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39'
ROOT = RUN + '/evidence/beta-consumer-controls-v1'
PLAN_PATH = RUN + '/control/beta-consumer-controls-plan-v2.json'
PLAN_SHA = '4eaff62de8996e69c03f48499e40ba8d0bac3c855407276fed34dbbe29dcd4b8'
PINS = {
    'reader': (RUN + '/control/beta_parent_reader_v1.py', '1fc8f00c08cd9f78885c9a38fa0797ce5b01aba8e8ad39a6d19d7b6ce3370ec6'),
    'capture4': (RUN + '/control/beta_capture_audit_v4.py', '9b50052136d82bd21914ca0ec83f561881fbee280ef472f09a20354e89b6c645'),
    'schema2': (RUN + '/control/beta_schema_audit_v2.py', '9e910e2d90ad1b80266fd38abc69d73e597fc589763b4464cb9251dd209be103'),
    'adapter3': (RUN + '/control/beta_parent_adapter_v3.py', '74a12f3f60e83f736e85ba4f0c06c4167a75e55922a095982389273b2db0f662'),
    'mols39_plan_v5': (MOLS + '/evidence/ext-search-plan-v5.json', '254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731'),
    'ext4_gate': (MOLS + '/code/ext4_gate.py', '8d04c5ce7b9fdf3f42c5537bdf32c892b6c1af09e3e31096e41b2506597624fa'),
    'original_dm21': ('/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21/evidence/checker-controls-pass-v1/controls/pos_sage_dm21_k6.raw', '70c8c2e579961ead65bb2abf03cc2d86cc799d1976f31d5333b52b26a142e825'),
}
PROTECTED = (MOLS + '/mols39-ext-search-v4-audits', MOLS + '/runs-ext-search-v4', MOLS + '/evidence/n1-fault-v1')
ORDER = ('DATA', 'G-DATA', 'B-N6', 'J-N6', 'G-N6', 'B-N12', 'J-N12', 'G-N12',
         'B-P21', 'J-P21', 'G-P21', 'B-P57', 'J-P57', 'G-P57', 'B-BAD_DM',
         'J-BAD_DM', 'G-BAD_DM', 'B-BAD_PIN', 'J-BAD_PIN', 'G-CONTROLS')
RD_IDS = ('RD01', 'RD02', 'RD03', 'RD04', 'RD05A', 'RD05B', 'RD05D', 'RD05E',
          'RD06A', 'RD06B', 'RD07A', 'RD07C', 'RD08A', 'RD08B', 'RD08C', 'RD09',
          'RD10A', 'RD10B', 'RD10C', 'RD10D', 'RD10E', 'RD11A', 'RD11B')
CA_IDS = ('CA00', 'CA02', 'CA03', 'CA04', 'CA08', 'CA09', 'CA12', 'CA14', 'CA16',
          'CA18', 'CA20', 'CA21', 'CA25', 'CA28', 'CA30', 'CA31', 'CA33', 'CA36',
          'CA41', 'CA43', 'CA45', 'CA48', 'CA49', 'CA51', 'CA53', 'CA54', 'CA56',
          'CA58', 'CA60', 'CA61', 'CA62', 'CA64', 'CA65', 'CA66', 'CA67', 'CA68',
          'CA69', 'CA71', 'CA75', 'CA77', 'CA79', 'CA80', 'CA82', 'CA84', 'CA87',
          'CA88', 'CA90', 'CA92', 'CA94', 'CA98', 'CA99', 'CA100', 'CA101',
          'CA102', 'CA103', 'CA105')
SC_IDS = ('SC01', 'SC04', 'SC05', 'SC06', 'SC19', 'SC32', 'SC33')
AD_IDS = ('AD00', 'AD01', 'AD02', 'AD04', 'AD06', 'AD07', 'AD09', 'AD14', 'AD15',
          'AD16', 'AD18', 'AD20', 'AD22', 'AD23', 'AD24', 'AD25', 'AD26', 'AD27',
          'AD28', 'AD29', 'AD30', 'AD33', 'AD34', 'AD35', 'AD36', 'AD37', 'AD39', 'AD40')
RESULT = b'{"label":"SYNTHETIC_FIXTURE beta-consumer-controls-v1 result bytes; not plan evidence","status":"SYNTHETIC"}\n'
RECEIPT = b'{"label":"SYNTHETIC_FIXTURE receipt; binds bytes only, not runtime truth"}\n'
INPUT_A = b'SYNTHETIC_FIXTURE input pin A\n'
STDERR_NONEMPTY = b'SYNTHETIC_FIXTURE stderr line\n'
DATA_BYTES = b'0123456789abcdef0123456789abcdef'
ARMED_MESSAGE = 'LABELLED_ARMED original deadline expired (event-armed, never renewed)'
REAL_MESSAGE = 'LABELLED_REAL_MONOTONIC original deadline crossed after harness-induced sleep at the armed boundary'
MAX_STDOUT = 1 << 20
MAX_RETAINED = 20 << 20
MAX_CASE_LINE = 4096
MAX_SUMMARY = 16384
MAX_DETAIL = 65536


class HarnessRefusal(Exception):
    pass


class HarnessDeadlineExceeded(TimeoutError):
    pass


class HarnessBudgetExceeded(Exception):
    pass


class InconclusivePrecondition(Exception):
    pass


class ControlDeadlineExpired(Exception):
    pass


class InjectedAcquisitionFault(RuntimeError):
    pass


class InjectedReadFault(OSError):
    pass


class InjectedCloseFault(OSError):
    pass


class InjectedConsumerFault(RuntimeError):
    pass


class InjectedBaseInterrupt(BaseException):
    pass


class _StringSubclass(str):
    pass


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _json_bytes(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True,
                       allow_nan=False) + '\n').encode('ascii')


def _parse(data):
    def pairs(rows):
        out = {}
        for key, value in rows:
            if key in out:
                raise HarnessRefusal('duplicate JSON key')
            out[key] = value
        return out
    def bad(_):
        raise HarnessRefusal('nonfinite JSON')
    return json.loads(data.decode('utf-8'), object_pairs_hook=pairs, parse_constant=bad)


def _exact(a, b):
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return set(a) == set(b) and all(_exact(a[key], b[key]) for key in a)
    if type(a) is list:
        return len(a) == len(b) and all(_exact(x, y) for x, y in zip(a, b))
    return a == b


def _parts(path):
    if type(path) is not str or not path.startswith('/') or '\x00' in path:
        raise HarnessRefusal('normalized absolute path required by harness')
    parts = path.split('/')[1:]
    if not parts or any(x in ('', '.', '..') for x in parts):
        raise HarnessRefusal('non-normalized harness path')
    return parts


def _meta(info):
    return {key: getattr(info, 'st_' + key) for key in
            ('dev', 'ino', 'mode', 'nlink', 'size', 'mtime_ns', 'ctime_ns')}


def _prefix(value):
    return value.split('(', 1)[0] if type(value) is str else None


def _attempt(function):
    """Contain ordinary exceptions and ONLY our labelled BaseException sentinel."""
    try:
        return function(), None
    except (HarnessDeadlineExceeded, HarnessBudgetExceeded):
        raise
    except InjectedBaseInterrupt as exc:
        return None, exc
    except Exception as exc:
        return None, exc


def _pair(exc):
    return [type(exc).__name__, str(exc)] if exc is not None else None


def _outcome(function):
    value, exc = _attempt(function)
    return {'exception': type(exc).__name__} if exc is not None else value


def _rel(value, length):
    if value == length:
        return 'len'
    if value == length + 1:
        return 'len+1'
    return 'zero' if value == 0 else 'other'


def _obs_probe(row, length):
    return {'bytes_seen_rel': _rel(row['bytes_seen'], length), 'eof': row['eof'],
            'before_present': row['before'] is not None,
            'after_present': row['after'] is not None,
            'sha256_present': row['sha256'] is not None,
            'completed': row['completed'], 'error_prefix': _prefix(row['error'])}


def _all_closed(report):
    return all(row['state'] == 'CLOSED' and row['close_attempted'] is True
               for row in report['resources'])


class _Owned:
    """Harness-only descriptor registry. Mark before close; never retry a close."""
    def __init__(self):
        self.rows = []
        self.errors = []

    def retain(self, fd, label):
        row = {'fd': fd, 'label': label, 'close_attempted': False,
               'closed': False, 'close_error': None}
        self.rows.append(row)  # retain returned fd before any fstat/clock
        return row

    def close(self, row):
        if row['close_attempted']:
            return
        row['close_attempted'] = True
        try:
            os.close(row['fd'])
        except BaseException as exc:
            row['close_error'] = repr(exc)
            self.errors.append({'label': row['label'], 'error': repr(exc)})
            raise
        else:
            row['closed'] = True

    def close_since(self, index, keep=None):
        first = None
        for row in reversed(self.rows[index:]):
            if row is keep or row['close_attempted']:
                continue
            try:
                self.close(row)
            except BaseException as exc:
                if first is None:
                    first = exc
        if first is not None:
            raise first


def _open_dir(path, owned):
    mark = len(owned.rows)
    selected = None
    try:
        row = owned.retain(os.open('/', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW), '/')
        for part in _parts(path):
            row = owned.retain(os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                       dir_fd=row['fd']), path)
        selected = row
        return row
    finally:
        owned.close_since(mark, keep=selected)


def _bootstrap_read(path, cap, owned, check):
    """Only for the reader source; actual NOFOLLOW parent walk and cap+1 read."""
    mark = len(owned.rows)
    try:
        parts = _parts(path)
        parent_path = '/' + '/'.join(parts[:-1])
        parent = _open_dir(parent_path, owned)
        leaf = owned.retain(os.open(parts[-1], os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW,
                                    dir_fd=parent['fd']), path)
        before = os.fstat(leaf['fd'])
        check()
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1 or before.st_size > cap:
            raise HarnessRefusal('bootstrap source kind/link/cap')
        chunks, total = [], 0
        while True:
            check()
            block = os.read(leaf['fd'], min(65536, cap + 1 - total))
            total += len(block)
            check()
            if total > cap:
                raise HarnessRefusal('bootstrap actual cap+1 overflow')
            if not block:
                break
            chunks.append(block)
        after = os.fstat(leaf['fd'])
        if _meta(before) != _meta(after) or after.st_size != total:
            raise HarnessRefusal('bootstrap identity/size changed')
        return b''.join(chunks)
    finally:
        owned.close_since(mark)


def _load_verified(source, path, expected_sha, name):
    if type(source) is not bytes or _sha(source) != expected_sha:
        raise HarnessRefusal('source pin mismatch: ' + path)
    namespace = {'__name__': name, '__file__': path}
    exec(compile(source, path, 'exec', dont_inherit=True), namespace)
    return namespace


class _Clock:
    """Labelled event arming; never clears/renews its armed deadline."""
    def __init__(self, base):
        self.base, self.calls, self.armed = base, 0, False
        self.real_deadline = None
        self.hook = None
        self.once = None
        self.real_hook_ran = False

    def arm(self):
        self.armed = True

    def check(self):
        self.base()
        self.calls += 1
        if self.hook is not None:
            self.hook(self)
        if self.once is not None:
            exc, self.once = self.once, None
            raise exc
        if self.real_deadline is not None and time.monotonic() > self.real_deadline:
            raise ControlDeadlineExpired(REAL_MESSAGE)
        if self.armed:
            raise ControlDeadlineExpired(ARMED_MESSAGE)


class _IteratorProxy:
    """Tracks explicit close only; trusted scandir may internally close at EOF."""
    def __init__(self, proxy, rec):
        self.proxy, self.rec = proxy, rec

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.rec['handle'])

    def close(self):
        self.proxy.close_iterator(self.rec)


class _FaultOS:
    """LABELLED boundary instrumentation; never modifies the process-wide os module.

    Rule dicts: op, phase, target (basename or '/'; None means any), occurrence,
    optional condition ('data'/'eof'), action (callable). Native fd acquisition
    is retained before a post-call rule. Orphans are closed using their retained
    dev/ino identity, not inferred descriptor-number ownership. Iterator cleanup
    uses the original retained native object, never an inferred internal fd.
    """
    def __init__(self, rules):
        self.rules = rules
        self.rows = []
        self.violations = []
        self.orphans_cleared = 0

    def __getattr__(self, name):
        return getattr(os, name)

    def _fire(self, op, phase, target, result=None):
        for rule in self.rules:
            if rule.get('done') or rule['op'] != op or rule['phase'] != phase:
                continue
            if rule.get('target') is not None and rule['target'] != target:
                continue
            condition = rule.get('condition')
            if condition == 'data' and not result:
                continue
            if condition == 'eof' and result != b'':
                continue
            rule['seen'] = rule.get('seen', 0) + 1
            if rule['seen'] != rule.get('occurrence', 1):
                continue
            rule['done'] = True
            rule['action']()

    def _fd(self, fd):
        for row in reversed(self.rows):
            if row['kind'] == 'fd' and row['fd'] == fd and not row['closed']:
                return row
        self.violations.append('untracked/already-closed descriptor requested')
        raise RuntimeError('LABELLED proxy refused an untracked/already-closed fd')

    def open(self, path, flags, *, dir_fd=None):
        target = path if path == '/' else os.path.basename(path)
        self._fire('open', 'before', target)
        fd = os.open(path, flags) if dir_fd is None else os.open(path, flags, dir_fd=dir_fd)
        rec = {'kind': 'fd', 'fd': fd, 'target': target, 'closed': False,
               'native_closes': 0, 'harness_closes': 0, 'orphan': False, 'identity': None}
        self.rows.append(rec)  # before fstat and rule
        try:
            info = os.fstat(fd)
            rec['identity'] = (info.st_dev, info.st_ino)
            self._fire('open', 'after', target)
        except BaseException:
            rec['orphan'] = True
            raise
        return fd

    def close(self, fd):
        rec = self._fd(fd)
        try:
            self._fire('close', 'before', rec['target'])
        except BaseException:
            rec['orphan'] = True
            raise
        os.close(fd)
        rec['closed'], rec['native_closes'] = True, rec['native_closes'] + 1
        self._fire('close', 'after', rec['target'])

    def read(self, fd, size):
        rec = self._fd(fd)
        self._fire('read', 'before', rec['target'])
        result = os.read(fd, size)
        self._fire('read', 'after', rec['target'], result)
        return result

    def fstat(self, fd):
        rec = self._fd(fd)
        self._fire('fstat', 'before', rec['target'])
        result = os.fstat(fd)
        self._fire('fstat', 'after', rec['target'], result)
        return result

    def scandir(self, fd):
        anchor = self._fd(fd)
        self._fire('scandir', 'before', anchor['target'])
        handle = os.scandir(fd)
        rec = {'kind': 'iterator', 'handle': handle, 'object_id': id(handle),
               'anchor_identity': anchor['identity'], 'target': anchor['target'],
               'closed': False, 'native_closes': 0, 'harness_closes': 0, 'orphan': False}
        self.rows.append(rec)
        try:
            self._fire('scandir', 'after', anchor['target'])
        except BaseException:
            rec['orphan'] = True
            raise
        return _IteratorProxy(self, rec)

    def close_iterator(self, rec):
        if rec['closed']:
            self.violations.append('second explicit iterator close')
            raise RuntimeError('LABELLED proxy refused second iterator close')
        rec['handle'].close()
        rec['closed'], rec['native_closes'] = True, rec['native_closes'] + 1

    def clear_orphans(self):
        for rec in self.rows:
            if rec['closed'] or not rec['orphan']:
                continue
            if rec['kind'] == 'fd':
                info = os.fstat(rec['fd'])
                if rec['identity'] != (info.st_dev, info.st_ino):
                    self.violations.append('orphan identity mismatch; no close attempted')
                    continue
                os.close(rec['fd'])
            else:
                if id(rec['handle']) != rec['object_id']:
                    self.violations.append('iterator object identity mismatch; no close attempted')
                    continue
                rec['handle'].close()
            rec['closed'] = True
            rec['harness_closes'] += 1
            self.orphans_cleared += 1

    def accounting_ok(self):
        return (not self.violations and all(row['closed'] and
                row['native_closes'] + row['harness_closes'] == 1 for row in self.rows))

    def native_closes(self, target):
        return sum(row['native_closes'] for row in self.rows if row['target'] == target)


def _raise(exception_class, message):
    def action():
        raise exception_class(message)
    return action


def _rule(op, phase, target, action, occurrence=1, condition=None):
    return {'op': op, 'phase': phase, 'target': target, 'action': action,
            'occurrence': occurrence, 'condition': condition}


class _Fx:
    def __init__(self, ctx, path, rec):
        self.ctx, self.path, self.rec = ctx, path, rec

    @property
    def fd(self):
        return self.rec['fd']

    def _name(self, name):
        if type(name) is not str or name in ('', '.', '..') or '/' in name or '\x00' in name:
            raise HarnessRefusal('fixture name is not plain')

    def mkdir(self, name):
        self._name(name)
        self.ctx.check()
        os.mkdir(name, 0o700, dir_fd=self.fd)  # exclusive: never exist_ok
        path = self.path + '/' + name
        rec = self.ctx.owned.retain(os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                           dir_fd=self.fd), path)
        return _Fx(self.ctx, path, rec)

    def write(self, name, data):
        self._name(name)
        if type(data) is not bytes:
            raise HarnessRefusal('fixture bytes required')
        self.ctx.reserve(len(data))
        path = self.path + '/' + name
        rec = self.ctx.owned.retain(os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                                           0o600, dir_fd=self.fd), path)
        try:
            view = memoryview(data)
            while view:
                self.ctx.check()
                written = os.write(rec['fd'], view)
                if written <= 0:
                    raise OSError('zero fixture write')
                view = view[written:]
        finally:
            self.ctx.owned.close(rec)
        info = os.stat(name, dir_fd=self.fd, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or info.st_size != len(data):
            raise HarnessRefusal('new fixture metadata mismatch')
        return {'path': path, 'sha256': _sha(data), 'bytes': len(data),
                'ino': info.st_ino, 'nlink': info.st_nlink, 'data': data}

    def append_growth(self, name, data):
        """Only the two labelled RD11 own fixtures use this additive mutation."""
        self._name(name)
        if name != 'grow.bin' or len(data) != 1:
            raise HarnessRefusal('growth fixture append scope')
        before = os.stat(name, dir_fd=self.fd, follow_symlinks=False)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise HarnessRefusal('growth fixture kind/link')
        self.ctx.reserve(len(data))
        rec = self.ctx.owned.retain(os.open(name, os.O_WRONLY | os.O_APPEND | os.O_NOFOLLOW,
                                           dir_fd=self.fd), self.path + '/' + name)
        try:
            actual = os.fstat(rec['fd'])
            if (actual.st_dev, actual.st_ino) != (before.st_dev, before.st_ino):
                raise HarnessRefusal('growth fixture identity')
            if os.write(rec['fd'], data) != 1:
                raise OSError('short labelled growth append')
        finally:
            self.ctx.owned.close(rec)

    def symlink(self, name, target):
        self._name(name)
        self._name(target)
        os.symlink(target, name, dir_fd=self.fd)
        self.ctx.reserve(len(target.encode('utf-8')))

    def fifo(self, name):
        self._name(name)
        os.mkfifo(name, 0o600, dir_fd=self.fd)

    def hardlink(self, source_dir, source_name, name):
        self._name(name)
        source_dir._name(source_name)
        info = os.stat(source_name, dir_fd=source_dir.fd, follow_symlinks=False)
        if not stat.S_ISREG(info.st_mode):
            raise HarnessRefusal('hardlink source must be real own regular file')
        os.link(source_name, name, src_dir_fd=source_dir.fd, dst_dir_fd=self.fd,
                follow_symlinks=False)

    def lstat(self, name):
        self._name(name)
        return os.stat(name, dir_fd=self.fd, follow_symlinks=False)


class _Context:
    def __init__(self, owned, check, sources, namespaces):
        self.owned, self.check = owned, check
        self.sources, self.ns = sources, namespaces
        self.retained = 0
        self.root = self.fx = self.reports = None
        self.ca = None
        self.last_reader = None
        self.retained_exception_readers = []
        self.budget_latched = False

    def reserve(self, count):
        if type(count) is not int or count < 0 or self.retained + count > MAX_RETAINED:
            self.budget_latched = True
            raise HarnessBudgetExceeded('retained-byte cap')
        self.retained += count  # conservative even if a later write partially fails

    def reader(self, check=None, rules=None):
        check = self.check if check is None else check
        proxy = None
        namespace = self.ns['reader']
        if rules is not None:
            path, digest = PINS['reader']
            namespace = _load_verified(self.sources['reader'], path, digest,
                                       'beta_control_labelled_fault_reader')
            proxy = _FaultOS(rules)
            namespace['os'] = proxy
        reader = namespace['EvidenceReader'](check)
        self.last_reader = reader
        return reader, proxy

    def retain_report(self, case_id, value):
        data = _json_bytes(value)
        if len(data) > MAX_DETAIL:
            data = _json_bytes({'format': 'beta-control-report-oversize-v1',
                                'full_serialized_bytes': len(data), 'sha256': _sha(data),
                                'retained': False, 'reason': '64KiB detail cap; not a full report'})
        return self.reports.write(case_id + '.json', data)


def _create_root(ctx):
    run = _open_dir(RUN, ctx.owned)
    try:
        info = os.stat('evidence', dir_fd=run['fd'], follow_symlinks=False)
    except FileNotFoundError:
        os.mkdir('evidence', 0o700, dir_fd=run['fd'])
        info = os.stat('evidence', dir_fd=run['fd'], follow_symlinks=False)
    if not stat.S_ISDIR(info.st_mode):
        raise HarnessRefusal('evidence parent is not a real directory')
    parent = ctx.owned.retain(os.open('evidence', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                    dir_fd=run['fd']), RUN + '/evidence')
    os.mkdir('beta-consumer-controls-v1', 0o700, dir_fd=parent['fd'])  # one exclusive attempt
    root = ctx.owned.retain(os.open('beta-consumer-controls-v1',
                                  os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                  dir_fd=parent['fd']), ROOT)
    ctx.owned.close(parent)
    ctx.owned.close(run)
    ctx.root = _Fx(ctx, ROOT, root)
    ctx.fx = ctx.root.mkdir('fx')
    ctx.reports = ctx.root.mkdir('reports')


def _capture_record(record):
    return {'present': True, 'path': record['path'], 'sha256': record['sha256'],
            'bytes_seen': record['bytes'], 'bytes_stored': record['bytes'],
            'eof': True, 'overflow': False, 'error': None}


def _artifact(record):
    return {key: record[key] for key in ('path', 'sha256', 'bytes', 'ino', 'nlink')}


def _base_records(job, result, stdout, stderr, receipt):
    expectation = {
        'format': 'beta-parent-audit-expectation-v1', 'mode': 'FIXTURE', 'item': 'B-BAD_PIN',
        'plan_sha256': PINS['mols39_plan_v5'][1], 'expected_exit': 2, 'outputs': ['result.json'],
        'job_dir': job.path, 'capture_paths': {'stdout': stdout['path'], 'stderr': stderr['path']},
        'receipt_path': receipt['path'], 'receipt_sha256': receipt['sha256'],
        'resolved_argv': ['SYNTHETIC-FIXTURE-ARGV', 'beta-consumer-controls-v1'],
        'go_sha256': _sha(b'SYNTHETIC_FIXTURE GO label beta-consumer-controls-v1; not a parent GO'),
        'source_pins': {}, 'input_pins': {},
        'date_start': {'kind': 'SYNTHETIC_FIXTURE_DATE_RECORD', 'not_bin_date': True, 'label': 'start'},
        'date_end': {'kind': 'SYNTHETIC_FIXTURE_DATE_RECORD', 'not_bin_date': True, 'label': 'end'},
    }
    observed = {key: copy.deepcopy(expectation[key]) for key in
                ('mode', 'item', 'plan_sha256', 'resolved_argv', 'go_sha256', 'source_pins',
                 'input_pins', 'date_start', 'date_end')}
    observed.update(format='beta-parent-audit-observation-v1', actual_exit=2,
                    captures={'stdout': _capture_record(stdout), 'stderr': _capture_record(stderr)},
                    artifacts={'result.json': _artifact(result)}, actual_artifact_names=['result.json'],
                    receipt={'path': receipt['path'], 'sha256': receipt['sha256']},
                    settlement={'reaped': True, 'group_empty': True, 'census_complete': True,
                                'unresolved': [], 'signals': []})
    return expectation, observed


def _reader_case(case_id, ctx):
    d = ctx.fx.mkdir(case_id.lower())
    if case_id == 'RD01':
        data, empty = d.write('data.bin', DATA_BYTES), d.write('empty.bin', b'')
        r, _ = ctx.reader()
        got = r.read_bytes(data['path'], len(DATA_BYTES))
        last = r.last_file(data['path'])
        empty_got = r.read_bytes(empty['path'], 0)
        empty_last = r.last_file(empty['path'])
        report = r.report()
        return {'read_equals_written': got == DATA_BYTES, 'last_file_completed': last['completed'],
                'last_file_sha_matches': last['sha256'] == data['sha256'],
                'last_file_ino_matches_lstat': last['after']['ino'] == d.lstat('data.bin').st_ino,
                'last_file_nlink': last['after']['nlink'],
                'last_file_bytes_seen_rel': _rel(last['bytes_seen'], len(DATA_BYTES)),
                'last_file_eof': last['eof'], 'empty_cap0_returns_empty': empty_got == b'',
                'empty_last_file_bytes_seen_rel': _rel(empty_last['bytes_seen'], 0),
                'calls': report['calls'], 'resource_count': len(report['resources']),
                'all_closed': _all_closed(report), 'unresolved': report['unresolved']}
    if case_id == 'RD02':
        d.write('target.bin', DATA_BYTES)
        d.symlink('leaf-link', 'target.bin')
        realdir = d.mkdir('realdir')
        realdir.write('inner.bin', DATA_BYTES)
        d.symlink('dir-link', 'realdir')
        d.fifo('fifo')
        d.write('hl-a.bin', DATA_BYTES)
        d.hardlink(d, 'hl-a.bin', 'hl-b.bin')
        r, _ = ctx.reader()
        paths = [d.path + '/' + name for name in ('leaf-link', 'dir-link/inner.bin', 'fifo', 'hl-a.bin')]
        failures = [_attempt(lambda p=path: r.read_bytes(p, 4096))[1] for path in paths]
        refusal = ctx.ns['reader']['EvidenceRefusal']
        report, counts = r.report(), {}
        for row in report['resources']:
            counts[row['state']] = counts.get(row['state'], 0) + 1
        return {'symlink_leaf_native_oserror': isinstance(failures[0], OSError) and not isinstance(failures[0], refusal),
                'symlink_leaf_errno_eloop': getattr(failures[0], 'errno', None) == errno.ELOOP,
                'symlink_ancestor_native_oserror': isinstance(failures[1], OSError) and not isinstance(failures[1], refusal),
                'fifo_leaf': _pair(failures[2]), 'hardlinked_leaf': _pair(failures[3]),
                'last_file_all_none': all(r.last_file(path) is None for path in paths),
                'state_counts': counts, 'unresolved': report['unresolved']}
    if case_id == 'RD03':
        data = d.write('ten.bin', b'0123456789')
        census = d.mkdir('census')
        for name in ('a', 'b', 'c'):
            census.write(name, b'x')
        r, _ = ctx.reader()
        low = _attempt(lambda: r.read_bytes(data['path'], 9))[1]
        exact = r.read_bytes(data['path'], 10)
        boolean = _attempt(lambda: r.read_bytes(data['path'], True))[1]
        names = r.directory_names(census.path)
        cap2 = _attempt(lambda: r.directory_names(census.path, 2))[1]
        retained = len(r.report()['observations'][-1]['names'])
        names3 = r.directory_names(census.path, 3)
        cap257 = _attempt(lambda: r.directory_names(census.path, 257))[1]
        report = r.report()
        return {'cap_below_size': _pair(low), 'cap_exact_read_ok': exact == b'0123456789',
                'cap_bool': _pair(boolean), 'census_names': names, 'census_cap2': _pair(cap2),
                'census_cap2_names_retained': retained, 'census_cap3_names': names3,
                'census_cap257': _pair(cap257), 'calls': report['calls'], 'unresolved': report['unresolved']}
    if case_id == 'RD04':
        a, b = d.write('same-a.bin', DATA_BYTES), d.write('same-b.bin', DATA_BYTES)
        r, _ = ctx.reader()
        av, bv = r.read_bytes(a['path'], 64), r.read_bytes(b['path'], 64)
        am, bm = r.last_file(a['path']), r.last_file(b['path'])
        return {'bytes_equal': av == bv, 'sha_equal': am['sha256'] == bm['sha256'],
                'ino_distinct': am['after']['ino'] != bm['after']['ino'],
                'ino_each_matches_lstat': am['after']['ino'] == d.lstat('same-a.bin').st_ino and
                                         bm['after']['ino'] == d.lstat('same-b.bin').st_ino,
                'unresolved': r.report()['unresolved']}
    if case_id.startswith('RD05'):
        data = d.write('obs.bin', DATA_BYTES)
        clock = _Clock(ctx.check)
        if case_id == 'RD05A':
            rule = _rule('read', 'after', 'obs.bin', clock.arm, condition='data')
        elif case_id == 'RD05B':
            rule = _rule('read', 'after', 'obs.bin', clock.arm, condition='eof')
        elif case_id == 'RD05D':
            rule = _rule('fstat', 'after', 'obs.bin', clock.arm, occurrence=2)
        else:
            clock.real_deadline = time.monotonic() + 1.0
            def sleep_crossing():
                while time.monotonic() <= clock.real_deadline:
                    ctx.check()
                    time.sleep(min(0.01, max(0.001, clock.real_deadline - time.monotonic() + 0.001)))
                clock.real_hook_ran = True
            rule = _rule('read', 'after', 'obs.bin', sleep_crossing, condition='data')
        r, proxy = ctx.reader(clock.check, [rule])
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            report = r.report()
            count = len(report['observations'])
            second = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            if case_id == 'RD05E' and not clock.real_hook_ran:
                raise InconclusivePrecondition('real monotonic deadline crossed before native-read sleep hook')
            observed = {'exception': type(exc).__name__,
                        'deadline_kind': 'REAL_MONOTONIC' if str(exc) == REAL_MESSAGE else 'ARMED',
                        'observation': _obs_probe(report['observations'][-1], len(DATA_BYTES)),
                        'all_closed': _all_closed(report), 'unresolved': report['unresolved'],
                        'last_file_none': r.last_file(data['path']) is None,
                        'second_call_exception': type(second).__name__,
                        'second_call_added_observation': len(r.report()['observations']) != count}
            if case_id == 'RD05E':
                observed['hook_slept_past_deadline'] = clock.real_hook_ran
        finally:
            proxy.clear_orphans()
        observed['proxy_accounting_ok'] = proxy.accounting_ok()
        ctx.retain_report(case_id, report)
        return observed
    if case_id in ('RD06A', 'RD06B'):
        data = d.write('close.bin', DATA_BYTES)
        nxt = d.write('next.bin', DATA_BYTES)
        clock = _Clock(ctx.check)
        action = _raise(InjectedCloseFault, 'LABELLED close fault') if case_id == 'RD06A' else clock.arm
        r, proxy = ctx.reader(clock.check, [_rule('close', 'after', 'close.bin', action)])
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            report = r.report()
            observed = {'exception': _pair(exc) if case_id == 'RD06A' else type(exc).__name__,
                        'unresolved': report['unresolved'],
                        'observation': _obs_probe(report['observations'][-1], len(DATA_BYTES)),
                        'last_file_none': r.last_file(data['path']) is None,
                        'leaf_native_closes': proxy.native_closes('close.bin')}
            if case_id == 'RD06A':
                leaf = report['resources'][-1]
                observed.update(leaf_state=leaf['state'], leaf_close_attempted=leaf['close_attempted'],
                                leaf_close_error_prefix=_prefix(leaf['close_error']),
                                next_read_ok=r.read_bytes(nxt['path'], 64) == DATA_BYTES,
                                unresolved_after_next_read=r.report()['unresolved'])
            else:
                observed.update(deadline_kind='ARMED', all_closed=_all_closed(report))
        finally:
            proxy.clear_orphans()
        observed.update(proxy_accounting_ok=proxy.accounting_ok(), orphans_cleared=proxy.orphans_cleared)
        ctx.retain_report(case_id, r.report())
        return observed
    if case_id in ('RD07A', 'RD07C'):
        data, nxt = d.write('acq.bin', DATA_BYTES), d.write('next.bin', DATA_BYTES)
        scan = d.mkdir('dir')
        action = _raise(InjectedAcquisitionFault, 'LABELLED unexpected acquisition exception')
        rule = _rule('open', 'after', 'acq.bin', action) if case_id == 'RD07A' else _rule('scandir', 'after', 'dir', action)
        r, proxy = ctx.reader(rules=[rule])
        try:
            operation = (lambda: r.read_bytes(data['path'], 64)) if case_id == 'RD07A' else (lambda: r.directory_names(scan.path))
            exc = _attempt(operation)[1]
            report = r.report()
            if case_id == 'RD07A':
                leaf = report['resources'][-1]
                observed = {'exception': type(exc).__name__, 'leaf_state': leaf['state'],
                            'leaf_fd_recorded': leaf['fd'] is not None,
                            'leaf_acquisition_error_prefix': _prefix(leaf['acquisition_error']),
                            'unresolved': report['unresolved']}
                proxy.clear_orphans()
                observed.update(next_read_ok=r.read_bytes(nxt['path'], 64) == DATA_BYTES,
                                unresolved_after_next_read=r.report()['unresolved'])
            else:
                observed = {'exception': _pair(exc), 'exception_context': type(exc.__context__).__name__,
                            'scandir_state': report['resources'][-1]['state'], 'unresolved': report['unresolved']}
        finally:
            proxy.clear_orphans()
        observed.update(proxy_accounting_ok=proxy.accounting_ok(), orphans_cleared=proxy.orphans_cleared)
        ctx.retain_report(case_id, r.report())
        return observed
    if case_id in ('RD08A', 'RD08B', 'RD08C'):
        data = d.write('rw.bin', DATA_BYTES)
        primary = InjectedReadFault if case_id == 'RD08A' else InjectedBaseInterrupt
        message = 'LABELLED primary read fault' if primary is InjectedReadFault else 'LABELLED base interrupt'
        rules = [_rule('read', 'before', 'rw.bin', _raise(primary, message))]
        if case_id != 'RD08C':
            rules.append(_rule('close', 'after', 'rw.bin', _raise(InjectedCloseFault, 'LABELLED close fault')))
        r, proxy = ctx.reader(rules=rules)
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            report = r.report()
            observed = {'exception': type(exc).__name__ if case_id == 'RD08C' else _pair(exc),
                        'observation_error_prefix': _prefix(report['observations'][-1]['error']),
                        'unresolved': report['unresolved']}
            if case_id == 'RD08C':
                ctx.retained_exception_readers.append(r)
                observed.update(report_available_after=type(report) is dict, all_closed=_all_closed(report))
            else:
                observed.update(exception_context=type(exc.__context__).__name__,
                                leaf_close_error_prefix=_prefix(report['resources'][-1]['close_error']),
                                leaf_native_closes=proxy.native_closes('rw.bin'))
        finally:
            proxy.clear_orphans()
        observed.update(proxy_accounting_ok=proxy.accounting_ok(), orphans_cleared=proxy.orphans_cleared)
        ctx.retain_report(case_id, report)
        return observed
    if case_id == 'RD09':
        data = d.write('stale.bin', DATA_BYTES)
        r, _ = ctx.reader()
        first = r.read_bytes(data['path'], 64)
        stale = r.last_file(data['path'])
        d.hardlink(d, 'stale.bin', 'stale-hl.bin')
        exc = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
        report = r.report()
        return {'first_read_ok': first == DATA_BYTES, 'second_read': _pair(exc),
                'last_file_unchanged_after_failure': _exact(stale, r.last_file(data['path'])),
                'stale_last_file_nlink': stale['after']['nlink'], 'current_lstat_nlink': d.lstat('stale.bin').st_nlink,
                'latest_observation_completed': report['observations'][-1]['completed'],
                'latest_observation_before_nlink': report['observations'][-1]['before']['nlink'],
                'unresolved': report['unresolved']}
    if case_id == 'RD10A':
        exc = _attempt(lambda: ctx.ns['reader']['EvidenceReader'](None))[1]
        return {'check_none': _pair(exc)}
    if case_id == 'RD10B':
        failures, reports = [], []
        for value in (True, False):
            r, _ = ctx.reader(lambda v=value: v)
            failures.append(_attempt(lambda: r.read_bytes(d.path + '/x.bin', 64))[1])
            reports.append(r.report())
        return {'returns_true': _pair(failures[0]), 'returns_false': _pair(failures[1]),
                'calls_each': [row['calls'] for row in reports],
                'observations_each': [len(row['observations']) for row in reports]}
    if case_id == 'RD10C':
        r, _ = ctx.reader()
        paths = {'relative': 'relative/x', 'dotdot': '/a/../b', 'components_129': '/' + '/'.join(['a'] * 129)}
        observed = {key: _pair(_attempt(lambda p=path: r.read_bytes(p, 64))[1]) for key, path in paths.items()}
        observed['calls'] = r.report()['calls']
        return observed
    if case_id == 'RD10D':
        clock = _Clock(ctx.check)
        clock.arm()
        r, _ = ctx.reader(clock.check)
        failures = []
        for _ in range(1026):
            failures.append(_attempt(lambda: r.read_bytes(d.path + '/never-opened.bin', 64))[1])
        report = r.report()
        return {'deadline_refusals_first_1024': sum(type(exc) is ControlDeadlineExpired for exc in failures[:1024]),
                'call_1025': _pair(failures[1024]), 'call_1026': _pair(failures[1025]),
                'calls': report['calls'], 'resources': len(report['resources']),
                'observations': len(report['observations'])}
    if case_id == 'RD10E':
        deep = d
        for index in range(1, 29):
            deep = deep.mkdir('d' + str(index).zfill(2))
        data = deep.write('deep.bin', b'x')
        if len(_parts(data['path'])) != 40:
            raise HarnessRefusal('deep fixture no longer has40 components')
        r, _ = ctx.reader()
        successes = 0
        while True:
            value, exc = _attempt(lambda: r.read_bytes(data['path'], 1))
            if exc is not None:
                break
            if value != b'x':
                raise HarnessRefusal('deep fixture actual bytes differ')
            successes += 1
            ctx.check()
        report = r.report()
        return {'successful_reads_before_cap': successes, 'cap_refusal': _pair(exc),
                'resources': len(report['resources']), 'all_closed': _all_closed(report),
                'unresolved': report['unresolved'], 'calls': report['calls']}
    if case_id in ('RD11A', 'RD11B'):
        initial = DATA_BYTES[:16]
        data = d.write('grow.bin', initial)
        rule = _rule('fstat', 'after', 'grow.bin', lambda: d.append_growth('grow.bin', b'x'))
        r, proxy = ctx.reader(rules=[rule])
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 16 if case_id == 'RD11A' else 64))[1]
            report = r.report()
            row = report['observations'][-1]
            observed = {'exception': _pair(exc), 'observation': _obs_probe(row, len(initial)),
                        'unresolved': report['unresolved']}
            if case_id == 'RD11B':
                observed.update(before_size_rel=_rel(row['before']['size'], len(initial)),
                                after_size_rel=_rel(row['after']['size'], len(initial)))
        finally:
            proxy.clear_orphans()
        observed.update(proxy_accounting_ok=proxy.accounting_ok(), orphans_cleared=proxy.orphans_cleared)
        ctx.retain_report(case_id, report)
        return observed
    raise HarnessRefusal('unknown reader case')


def _ca_fixture(ctx):
    if ctx.ca is not None:
        return ctx.ca
    d = ctx.fx.mkdir('ca')
    job, empty_job, no_job = d.mkdir('job'), d.mkdir('job-empty'), d.mkdir('job-noresult')
    cap, pins, other = d.mkdir('cap'), d.mkdir('pins'), d.mkdir('other')
    result = job.write('result.json', RESULT)
    empty_result = empty_job.write('result.json', b'')
    stdout, stderr = cap.write('stdout.bin', RESULT), cap.write('stderr.bin', b'')
    empty_stdout = cap.write('stdout-empty.bin', b'')
    prefix_stdout = cap.write('stdout-prefix.bin', RESULT[:64])
    nonempty_stderr = cap.write('stderr-nonempty.bin', STDERR_NONEMPTY)
    receipt, input_a = d.write('receipt.json', RECEIPT), pins.write('input-a.bin', INPUT_A)
    same = other.write('same.bin', RESULT)
    expectation, observed = _base_records(job, result, stdout, stderr, receipt)
    expectation['source_pins'] = {PINS['capture4'][0]: PINS['capture4'][1]}
    expectation['input_pins'] = {input_a['path']: input_a['sha256']}
    observed['source_pins'] = copy.deepcopy(expectation['source_pins'])
    observed['input_pins'] = copy.deepcopy(expectation['input_pins'])
    records = (result, empty_result, stdout, stderr, empty_stdout, prefix_stdout,
               nonempty_stderr, receipt, input_a, same)
    snapshot = {record['path']: record['data'] for record in records}
    snapshot[PINS['capture4'][0]] = ctx.sources['capture4']
    ctx.ca = {'expectation': expectation, 'observed': observed, 'result': result,
              'empty_result': empty_result, 'stdout': stdout, 'stderr': stderr,
              'empty_stdout': empty_stdout, 'prefix_stdout': prefix_stdout,
              'nonempty_stderr': nonempty_stderr, 'receipt': receipt, 'input_a': input_a,
              'same': same, 'empty_job_path': empty_job.path, 'no_job_path': no_job.path,
              'path': d.path, 'snapshot': snapshot}
    return ctx.ca


def _use_stream(expectation, observed, stream, record):
    expectation['capture_paths'][stream] = record['path']
    observed['captures'][stream] = _capture_record(record)


def _empty_result(expectation, observed, fixture):
    expectation['job_dir'] = fixture['empty_job_path']
    observed['artifacts']['result.json'] = _artifact(fixture['empty_result'])
    _use_stream(expectation, observed, 'stdout', fixture['empty_stdout'])


def _subkey(record, key):
    value = record.pop(key)
    record[_StringSubclass(key)] = value


def _capture_case(case_id, ctx):
    fixture = _ca_fixture(ctx)
    e, o = copy.deepcopy(fixture['expectation']), copy.deepcopy(fixture['observed'])
    r, _ = ctx.reader()
    callback, extras = r.read_bytes, {}
    capture = ctx.ns['capture4']['audit_capture']
    wrong = _sha(b'other')
    if case_id == 'CA02':
        o['captures']['stdout'] = None
    elif case_id == 'CA03':
        o['captures']['stdout'].update(present=False, eof=False, error='SYNTHETIC incomplete too')
    elif case_id == 'CA04':
        o['captures']['stdout']['eof'] = False
    elif case_id == 'CA08':
        o['captures']['stdout']['sha256'] = wrong
    elif case_id == 'CA09':
        o['captures']['stdout'].update(bytes_seen=True, bytes_stored=True)
    elif case_id == 'CA12':
        values = {}
        for name, record in (('empty', fixture['empty_stdout']), ('prefix64', fixture['prefix_stdout'])):
            ee, oo = copy.deepcopy(e), copy.deepcopy(o)
            _use_stream(ee, oo, 'stdout', record)
            values[name] = capture(ee, oo, callback)
        return {'outcome': values, 'reader_unresolved': r.report()['unresolved']}
    elif case_id == 'CA14':
        _empty_result(e, o, fixture)
    elif case_id == 'CA16':
        o['captures']['stderr'] = None
    elif case_id == 'CA18':
        o['captures']['stderr']['eof'] = False
    elif case_id == 'CA20':
        _use_stream(e, o, 'stderr', fixture['nonempty_stderr'])
    elif case_id == 'CA21':
        values = {}
        for value in (5, 94, 120, -15, 258):
            oo = copy.deepcopy(o)
            oo['actual_exit'] = value
            values[str(value)] = capture(e, oo, callback)
        return {'outcome': values, 'reader_unresolved': r.report()['unresolved']}
    elif case_id == 'CA25':
        e['expected_exit'], o['actual_exit'] = 1, True
    elif case_id == 'CA28':
        e['expected_exit'], o['actual_exit'] = 300, 300
    elif case_id == 'CA30':
        e['job_dir'] = fixture['no_job_path']
        o['artifacts']['result.json']['path'] = e['job_dir'] + '/result.json'
    elif case_id == 'CA31':
        o['actual_artifact_names'].append('extra.bin')
    elif case_id == 'CA33':
        o['artifacts']['result.json']['sha256'] = wrong
    elif case_id == 'CA36':
        o['artifacts']['result.json']['ino'] = True
    elif case_id == 'CA41':
        o['artifacts']['result.json']['ino'] = fixture['same']['ino']
    elif case_id == 'CA43':
        o['settlement']['group_empty'] = 1
    elif case_id == 'CA45':
        o['settlement']['unresolved'] = ['SYNTHETIC-unresolved-identity']
    elif case_id == 'CA48':
        o['receipt']['sha256'] = wrong
    elif case_id == 'CA49':
        e['receipt_sha256'] = o['receipt']['sha256'] = wrong
    elif case_id == 'CA51':
        o['resolved_argv'] = ['SYNTHETIC-FIXTURE-ARGV', '--budget-s', '2']
    elif case_id == 'CA53':
        e['item'] = o['item'] = ''
        e['resolved_argv'], o['resolved_argv'] = [], []
    elif case_id == 'CA54':
        o['go_sha256'] = wrong
    elif case_id == 'CA56':
        e['source_pins'] = {PINS['capture4'][0]: wrong}
        o['source_pins'] = copy.deepcopy(e['source_pins'])
    elif case_id == 'CA58':
        o['input_pins'][fixture['input_a']['path']] = wrong
    elif case_id == 'CA60':
        e['source_pins'], o['source_pins'], e['input_pins'], o['input_pins'] = {}, {}, {}, {}
    elif case_id == 'CA61':
        d = ctx.fx.mkdir('ca61')
        pins = {}
        for index in range(257):
            rec = d.write('p' + str(index).zfill(3) + '.bin', b'SYNTHETIC_FIXTURE pin\n')
            pins[rec['path']] = rec['sha256']
        e['input_pins'], o['input_pins'] = pins, copy.deepcopy(pins)
    elif case_id == 'CA62':
        e['source_pins'] = {fixture['input_a']['path']: fixture['input_a']['sha256']}
        e['input_pins'] = {fixture['input_a']['path']: wrong}
        o['source_pins'], o['input_pins'] = copy.deepcopy(e['source_pins']), copy.deepcopy(e['input_pins'])
    elif case_id == 'CA64':
        e['date_start'], o['date_start'] = {'n': 1}, {'n': True}
    elif case_id == 'CA65':
        e['date_start'], o['date_start'] = {}, {}
    elif case_id == 'CA66':
        def nested():
            value = 'SYNTHETIC_FIXTURE leaf'
            for _ in range(40):
                value = {'nested': value}
            return value
        e['date_start'], o['date_start'] = nested(), nested()
    elif case_id == 'CA67':
        shared = {'v': [1, 2, {'SYNTHETIC_FIXTURE': True}]}
        e['date_end'] = {'a': shared, 'b': shared}
        o['date_end'] = {'a': copy.deepcopy(shared), 'b': copy.deepcopy(shared)}
    elif case_id == 'CA68':
        left, right = [], []
        left.append(left)
        right.append(right)
        e['date_start'], o['date_start'] = {'c': left}, {'c': right}
    elif case_id == 'CA69':
        values = {}
        for side in ('expectation_only', 'observation_only'):
            ee, oo = copy.deepcopy(e), copy.deepcopy(o)
            cycle = []
            cycle.append(cycle)
            ee['date_start'], oo['date_start'] = ({'c': cycle}, {'c': [[[]]]}) if side == 'expectation_only' else ({'c': [[[]]]}, {'c': cycle})
            values[side] = capture(ee, oo, callback)
        return {'outcome': values, 'reader_unresolved': r.report()['unresolved']}
    elif case_id == 'CA71':
        e['date_start'], o['date_start'] = {'v': float('nan')}, {'v': float('nan')}
    elif case_id == 'CA75':
        e['date_start'], o['date_start'] = {'t': (1, 2)}, {'t': (1, 2)}
    elif case_id == 'CA77':
        o['mode'] = 'PLAN'
    elif case_id == 'CA79':
        e['plan_sha256'] = o['plan_sha256'] = wrong
    elif case_id == 'CA80':
        o['item'] = 'J-BAD_PIN'
    elif case_id == 'CA82':
        o['extra'] = 'SYNTHETIC_FIXTURE extra'
    elif case_id == 'CA84':
        o['captures']['stdout'], o['captures']['bogus'] = None, 1
    elif case_id == 'CA87':
        e = None
    elif case_id == 'CA88':
        o = None
    elif case_id == 'CA90':
        r = None
        callback = lambda path, cap: _raise(ValueError, 'LABELLED defined read refusal')()
    elif case_id == 'CA92':
        def over_cap(path, cap):
            return b'\x00' * (cap + 1) if path == fixture['stdout']['path'] else r.read_bytes(path, cap)
        callback = over_cap
    elif case_id == 'CA94':
        r = None
        callback = lambda path, cap: _raise(KeyError, 'LABELLED lookup fault')()
    elif case_id == 'CA98':
        r = None
        callback = lambda path, cap: _raise(InjectedBaseInterrupt, 'LABELLED base interrupt')()
    elif case_id in ('CA99', 'CA100'):
        e['input_pins'][fixture['receipt']['path']] = fixture['receipt']['sha256']
        if case_id == 'CA99':
            e['input_pins'][fixture['result']['path']] = fixture['result']['sha256']
        o['input_pins'] = copy.deepcopy(e['input_pins'])
        reads = []
        def counted(path, cap):
            reads.append((path, cap))
            if case_id == 'CA100' and path == fixture['receipt']['path']:
                raise OSError('LABELLED receipt refusal')
            return r.read_bytes(path, cap)
        callback = counted
    elif case_id == 'CA101':
        r = None
        snapshot, calls = dict(fixture['snapshot']), []
        def snapshot_read(path, cap):
            calls.append(path)
            if path not in snapshot or len(snapshot[path]) > cap:
                raise OSError('LABELLED snapshot unavailable/type/cap')
            return snapshot[path]
        first = capture(e, o, snapshot_read)
        first_reads = calls.count(fixture['stdout']['path'])
        calls.clear()
        snapshot[fixture['stdout']['path']] = b'changed'
        second = capture(e, o, snapshot_read)
        return {'outcome': [first, second], 'reader_unresolved': None,
                'stdout_reads_per_call': [first_reads, calls.count(fixture['stdout']['path'])]}
    elif case_id == 'CA102':
        o['actual_exit'], o['captures']['stdout'] = 5, None
        _use_stream(e, o, 'stderr', fixture['nonempty_stderr'])
        o['actual_artifact_names'].append('extra.bin')
        o['settlement']['unresolved'] = ['SYNTHETIC-unresolved-identity']
        o['resolved_argv'] = ['SYNTHETIC mismatch']
    elif case_id == 'CA103':
        _empty_result(e, o, fixture)
        _use_stream(e, o, 'stderr', fixture['empty_stdout'])
    elif case_id == 'CA105':
        values = {}
        names = ('observation_date', 'expectation_date', 'captures_map', 'stdout_record',
                 'observation_top', 'expectation_top', 'capture_paths', 'artifacts_map',
                 'artifact_record', 'settlement', 'receipt_record', 'observed_pin_map', 'numeric_date_key')
        for name in names:
            ee, oo = copy.deepcopy(e), copy.deepcopy(o)
            if name == 'observation_date':
                _subkey(oo['date_start'], 'kind')
            elif name == 'expectation_date':
                _subkey(ee['date_start'], 'kind')
            elif name == 'captures_map':
                _subkey(oo['captures'], 'stdout')
            elif name == 'stdout_record':
                _subkey(oo['captures']['stdout'], 'present')
            elif name == 'observation_top':
                _subkey(oo, 'format')
            elif name == 'expectation_top':
                _subkey(ee, 'format')
            elif name == 'capture_paths':
                _subkey(ee['capture_paths'], 'stdout')
            elif name == 'artifacts_map':
                _subkey(oo['artifacts'], 'result.json')
            elif name == 'artifact_record':
                _subkey(oo['artifacts']['result.json'], 'nlink')
            elif name == 'settlement':
                _subkey(oo['settlement'], 'reaped')
            elif name == 'receipt_record':
                _subkey(oo['receipt'], 'path')
            elif name == 'observed_pin_map':
                _subkey(oo['input_pins'], fixture['input_a']['path'])
            else:
                ee['date_start'], oo['date_start'] = {1: 'SYNTHETIC'}, {1: 'SYNTHETIC'}
            values[name] = capture(ee, oo, callback)
        return {'outcome': values, 'reader_unresolved': r.report()['unresolved']}
    elif case_id != 'CA00':
        raise HarnessRefusal('unknown capture case')
    value = _outcome(lambda: capture(e, o, callback))
    if case_id == 'CA99':
        roles = {fixture[key]['path']: role for key, role in
                 (('stdout', 'stdout'), ('result', 'result'), ('stderr', 'stderr'),
                  ('receipt', 'receipt'), ('input_a', 'input-a'))}
        roles[PINS['capture4'][0]] = 'capture4'
        extras = {'read_roles': [roles.get(path, path) for path, _ in reads],
                  'caps': [cap for _, cap in reads],
                  'max_reads_per_path': max((sum(p == path for p, _ in reads) for path, _ in reads), default=0)}
    elif case_id == 'CA100':
        extras = {'receipt_reads': sum(path == fixture['receipt']['path'] for path, _ in reads)}
    return {'outcome': value, 'reader_unresolved': r.report()['unresolved'] if r is not None else None, **extras}


def _schema_case(case_id, ctx):
    schema = ctx.ns['schema2']['audit_schema']
    plan, original = ctx.sources['mols39_plan_v5'], ctx.sources['original_dm21']
    if case_id in ('SC32', 'SC33'):
        primary = InjectedReadFault if case_id == 'SC32' else InjectedBaseInterrupt
        message = 'LABELLED primary read fault' if case_id == 'SC32' else 'LABELLED base interrupt'
        rules = [_rule('read', 'before', 'ext4_gate.py', _raise(primary, message))]
        if case_id == 'SC32':
            rules.append(_rule('close', 'after', 'ext4_gate.py', _raise(InjectedCloseFault, 'LABELLED close fault')))
        r, proxy = ctx.reader(rules=rules)
        try:
            value = _outcome(lambda: schema(plan, 'DATA', {}, [], original, ctx.check, r.read_bytes))
            report = r.report()
            observed = {'outcome': value, 'reader_unresolved': report['unresolved'],
                        'unknown_paths': [row['path'] for row in report['resources'] if row['state'] == 'UNKNOWN']}
            if case_id == 'SC32':
                observed.update(observation_error_prefix=_prefix(report['observations'][-1]['error']),
                                close_error_prefix=_prefix(report['resources'][-1]['close_error']))
            else:
                ctx.retained_exception_readers.append(r)
        finally:
            proxy.clear_orphans()
        observed.update(proxy_accounting_ok=proxy.accounting_ok(), orphans_cleared=proxy.orphans_cleared)
        ctx.retain_report(case_id, report)
        return observed
    reads, r = [], None
    check = ctx.check
    if case_id == 'SC01':
        check = None
    elif case_id == 'SC04':
        check = lambda: False
    elif case_id == 'SC05':
        clock = _Clock(ctx.check)
        clock.arm()
        check = clock.check
    elif case_id == 'SC06':
        plan += b' '
    elif case_id == 'SC19':
        r, _ = ctx.reader()
    def callback(path, cap):
        reads.append((path, cap))
        return r.read_bytes(path, cap) if r is not None else ctx.sources['ext4_gate']
    item = 'CAL-beta' if case_id == 'SC19' else 'DATA'
    value = _outcome(lambda: schema(plan, item, {}, [], original, check, callback))
    observed = {'outcome': value, 'gate_reads': len(reads),
                'reader_unresolved': r.report()['unresolved'] if r is not None else None}
    if case_id == 'SC19':
        observed['gate_path_and_cap_bound'] = reads == [(PINS['ext4_gate'][0], 1 << 20)]
    return observed


class _DelegatingReader:
    """Labelled report fault/arming only. Never supplies mock bytes or success."""
    def __init__(self, reader, clock, fail_reports=(), arm_report=None):
        self.reader, self.clock = reader, clock
        self.fail_reports, self.arm_report = set(fail_reports), arm_report
        self.report_calls = 0

    def read_bytes(self, path, cap):
        return self.reader.read_bytes(path, cap)

    def last_file(self, path):
        return self.reader.last_file(path)

    def directory_names(self, path, cap=256):
        return self.reader.directory_names(path, cap)

    def report(self):
        self.report_calls += 1
        if self.report_calls in self.fail_reports:
            raise InjectedConsumerFault('LABELLED consumer/report fault')
        result = self.reader.report()
        if self.report_calls == self.arm_report:
            self.clock.arm()
        return result


def _ref(record):
    return {'path': record['path'], 'sha256': record['sha256']}


def _adapter_fixture(case_id, ctx):
    d = ctx.fx.mkdir(case_id.lower())
    job, cap, links = d.mkdir('job'), d.mkdir('cap'), d.mkdir('links')
    result = job.write('result.json', RESULT)
    stdout, stderr = cap.write('stdout.bin', RESULT), cap.write('stderr.bin', b'')
    receipt = d.write('receipt.json', RECEIPT)
    e, o = _base_records(job, result, stdout, stderr, receipt)
    context = {'format': 'beta-parent-schema-context-v2',
               'plan': {'path': PINS['mols39_plan_v5'][0], 'sha256': PINS['mols39_plan_v5'][1]},
               'original_dm21': {'path': PINS['original_dm21'][0], 'sha256': PINS['original_dm21'][1]},
               'prefix': [], 'derivation': None, 'publication_freeze': None}
    own_paths = [d.path + '/' + name for name in
                 ('expectation.json', 'observation.json', 'context.json', 'freeze.json')]
    immutable = set(own_paths + [PINS[name][0] for name in
                                ('capture4', 'schema2', 'mols39_plan_v5', 'original_dm21', 'ext4_gate')]
                    + [result['path'], stdout['path'], stderr['path'], receipt['path']])
    if case_id == 'AD04':
        context['format'] = 'beta-parent-schema-context-v1'
    elif case_id == 'AD06':
        context['original_dm21']['sha256'] = _sha(b'other')
    elif case_id == 'AD07':
        audit = d.write('synthetic-prefix-audit.json', b'{"label":"SYNTHETIC_FIXTURE not a canonical audit"}\n')
        immutable.add(audit['path'])
        context['prefix'] = [{'item': 'DATA', 'files': {}, 'audit': _ref(audit)} for _ in range(20)]
    elif case_id == 'AD18':
        e['mode'] = o['mode'] = 'PLAN'
    elif case_id == 'AD22':
        o['actual_exit'] = 120
    elif case_id == 'AD25':
        other = d.mkdir('other')
        same = other.write('same.bin', RESULT)
        o['artifacts']['result.json']['ino'] = same['ino']
    elif case_id == 'AD26':
        o['artifacts'] = {}
    elif case_id == 'AD27':
        del e['job_dir']
    elif case_id == 'AD40':
        o['actual_exit'] = 5
    if case_id in ('AD18', 'AD20', 'AD22'):
        immutable.add(d.path + '/derivation.json')
        immutable.add(d.path + '/upstream-observation.json')
    freeze = {'format': 'beta-parent-publication-freeze-v1', 'mode': e['mode'],
              'job_dir': job.path, 'immutable_paths': sorted(immutable), 'prefix_authority': []}
    if case_id == 'AD09':
        freeze['mode'] = 'PLAN'
    if case_id == 'AD14':
        freeze['immutable_paths'].remove(PINS['ext4_gate'][0])
    freeze_bytes = _json_bytes(freeze)
    if case_id == 'AD28':
        freeze_bytes += b' ' * ((1 << 20) + 256 - len(freeze_bytes))
    freeze_rec = d.write('freeze.json', freeze_bytes)
    if case_id in ('AD28', 'AD29'):
        e['input_pins'] = {freeze_rec['path']: freeze_rec['sha256']}
        o['input_pins'] = copy.deepcopy(e['input_pins'])
    er, or_ = d.write('expectation.json', _json_bytes(e)), d.write('observation.json', _json_bytes(o))
    if case_id in ('AD18', 'AD20', 'AD22'):
        upstream = copy.deepcopy(o)
        upstream['actual_exit'] = 2
        upstream_rec = d.write('upstream-observation.json', _json_bytes(upstream))
        manifest = {'format': 'beta-parent-synthetic-derivation-v1',
                    'expectation_sha256': er['sha256'], 'observation_sha256': or_['sha256'],
                    'upstream_observation': _ref(upstream_rec),
                    'mutations': [{'path': ['actual_exit'], 'value': 120}]}
        if case_id == 'AD20':
            manifest['expectation_sha256'] = '0' * 64
        manifest_rec = d.write('derivation.json', _json_bytes(manifest))
        context['derivation'] = _ref(manifest_rec)
    context['publication_freeze'] = _ref(freeze_rec)
    cr = d.write('context.json', _json_bytes(context))
    inputs = {'expectation': _ref(er), 'observation': _ref(or_), 'context': _ref(cr)}
    if case_id == 'AD01':
        del inputs['context']
    elif case_id == 'AD02':
        inputs['expectation']['sha256'] = _sha(b'other')
    if case_id == 'AD30':
        d.write('poison.bin', DATA_BYTES)
    return {'dir': d, 'job': job, 'links': links, 'result': result, 'stdout': stdout,
            'context': context, 'inputs': inputs}


def _decision_probe(decision, context):
    synthetic = decision.get('synthetic_derivation')
    if synthetic is not None:
        synthetic = {'requested': synthetic.get('requested'), 'verified': synthetic.get('verified'),
                     'actual_exit_is_measured': synthetic.get('actual_exit_is_measured'),
                     'manifest_matches_context_ref': _exact(synthetic.get('manifest'), context.get('derivation'))}
    report = decision.get('reader')
    return {'verdict': decision.get('verdict'), 'causes': decision.get('causes'),
            'error_stages': [row.get('stage') for row in decision.get('errors', [])],
            'tail_fallback': 'consumer_pins' not in decision, 'nested_exit': decision.get('nested_exit'),
            'synthetic': synthetic,
            'selected_artifacts': sorted(decision['selected_artifacts']) if 'selected_artifacts' in decision else None,
            'persistence_count': len(decision['snapshot_persistence']) if 'snapshot_persistence' in decision else None,
            'reader_unresolved': report.get('unresolved') if type(report) is dict else None,
            'authority_flags': [decision.get(key) for key in
                                ('canonical_audit_written', 'release_authority', 'runtime_authority')]}


def _adapter_case(case_id, ctx):
    fixture = _adapter_fixture(case_id, ctx)
    clock = _Clock(ctx.check)
    proxy, extras = None, {}
    rules = None
    if case_id == 'AD30':
        rules = [_rule('open', 'after', 'poison.bin',
                       _raise(InjectedAcquisitionFault, 'LABELLED unexpected acquisition exception'))]
    r, proxy = ctx.reader(clock.check, rules)
    reader = r
    inputs = fixture['inputs']
    original_inputs = copy.deepcopy(inputs)
    hook_state = {'fired': False}
    if case_id in ('AD15', 'AD16'):
        if case_id == 'AD16':
            r.read_bytes(fixture['result']['path'], 16 << 20)
            stale = r.last_file(fixture['result']['path'])
            extras.update(stale_last_file_completed=stale['completed'], stale_last_file_nlink=stale['after']['nlink'])
        fixture['links'].hardlink(fixture['job'], 'result.json', 'result-hl.json')
    if case_id in ('AD23', 'AD24'):
        needed = 1 if case_id == 'AD23' else 2
        def namespace_hook(_):
            # Instrumentation timing only: observe the exact reader's retained ledger,
            # not a private validator call or a source/wiring acceptance oracle.
            count = sum(row['kind'] == 'directory' and row['path'] == fixture['job'].path and row['completed']
                        for row in r._observations)
            if not hook_state['fired'] and count >= needed:
                hook_state['fired'] = True
                if case_id == 'AD23':
                    fixture['job'].write('late.bin', b'SYNTHETIC_FIXTURE additive namespace fault\n')
                else:
                    fixture['links'].hardlink(fixture['job'], 'result.json', 'result-hl2.json')
        clock.hook = namespace_hook
    elif case_id in ('AD35', 'AD36'):
        def consumer_hook(current_clock):
            if not hook_state['fired'] and any(row['path'] == fixture['stdout']['path'] for row in r._observations):
                hook_state['fired'] = True
                current_clock.once = (InjectedConsumerFault('LABELLED consumer/report fault') if case_id == 'AD35'
                                      else InjectedBaseInterrupt('LABELLED base interrupt'))
        clock.hook = consumer_hook
    elif case_id == 'AD39':
        def reference_hook(current_clock):
            if current_clock.calls == 2:
                inputs['expectation']['sha256'] = _sha(b'caller mutation')
                inputs['context'] = {'path': fixture['dir'].path + '/caller-mutated-context.json', 'sha256': _sha(b'caller')}
        clock.hook = reference_hook
    if case_id == 'AD30':
        exc = _attempt(lambda: r.read_bytes(fixture['dir'].path + '/poison.bin', 64))[1]
        extras['poison_exception'] = type(exc).__name__
        proxy.clear_orphans()
    if case_id == 'AD33':
        reader = _DelegatingReader(r, clock, fail_reports=(3, 4))
    elif case_id == 'AD34':
        reader = _DelegatingReader(r, clock, arm_report=3)
    check = (lambda: False) if case_id == 'AD37' else clock.check
    try:
        decision, exc = _attempt(lambda: ctx.ns['adapter3']['evaluate_pinned'](inputs, reader, check))
        if exc is not None:
            if isinstance(exc, InjectedBaseInterrupt):
                ctx.retained_exception_readers.append(r)
                report = r.report()
                row = next(row for row in reversed(report['observations']) if row['path'] == fixture['stdout']['path'])
                observed = {'exception': type(exc).__name__, 'decision_returned': False,
                            'reader_unresolved': report['unresolved'],
                            'stdout_observation_error_prefix': _prefix(row['error']),
                            'stdout_observation_completed': row['completed']}
                ctx.retain_report(case_id, report)
                return observed
            return {'unexpected_exception': _pair(exc), 'reader_unresolved': r.report()['unresolved']}
        observed = _decision_probe(decision, fixture['context'])
        if case_id == 'AD00':
            observed['selected_sha_matches_written'] = decision['selected_artifacts']['result.json']['sha256'] == fixture['result']['sha256']
        elif case_id in ('AD01', 'AD02'):
            observed.update(reader_calls=r.report()['calls'], input_pins_null=decision.get('input_pins') is None)
        elif case_id == 'AD28':
            observed['context_error_contains_cap_refusal'] = any(
                row.get('stage') == 'context_authority' and
                'cached immutable acquisition exceeds requested cap' in row.get('error', '')
                for row in decision['errors'])
        elif case_id in ('AD23', 'AD24', 'AD35'):
            observed['hook_fired'] = hook_state['fired']
        elif case_id == 'AD37':
            observed['reader_calls'] = r.report()['calls']
        elif case_id == 'AD39':
            observed.update(input_pins_equal_original=_exact(decision.get('input_pins'), original_inputs),
                            caller_inputs_mutated=not _exact(inputs, original_inputs),
                            input_pins_distinct_object=decision.get('input_pins') is not inputs)
        observed.update(extras)
        # Keep decision fields plus the complete report when <=64KiB; oversize is
        # explicitly digest-labelled by retain_report, never asserted full evidence.
        ctx.retain_report(case_id, decision)
    finally:
        if proxy is not None:
            proxy.clear_orphans()
    if proxy is not None:
        observed.update(proxy_accounting_ok=proxy.accounting_ok(), orphans_cleared=proxy.orphans_cleared)
    return observed


def _protected_state():
    result = {}
    for path in PROTECTED:
        try:
            result[path] = _meta(os.lstat(path))
        except FileNotFoundError:
            result[path] = None
    return result


def _capabilities():
    required = (os.open, os.mkdir, os.stat, os.symlink, os.link, os.mkfifo)
    if any(function not in os.supports_dir_fd for function in required):
        raise HarnessRefusal('required dir_fd operation unsupported')
    if os.scandir not in os.supports_fd or os.link not in os.supports_follow_symlinks:
        raise HarnessRefusal('required scandir-fd or NOFOLLOW link operation unsupported')
    for flag in ('O_NOFOLLOW', 'O_NONBLOCK', 'O_DIRECTORY', 'O_EXCL', 'O_APPEND'):
        if not hasattr(os, flag):
            raise HarnessRefusal('required os flag missing: ' + flag)


def _emit(value, output_state, summary=False):
    data = _json_bytes(value)
    bound = MAX_SUMMARY if summary else MAX_CASE_LINE
    if len(data) > bound or output_state['bytes'] + len(data) > MAX_STDOUT:
        raise HarnessBudgetExceeded('stdout bound')
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    output_state['bytes'] += len(data)


def _emit_case(case, status, observed, elapsed, ctx, output_state):
    value = {'format': 'beta-consumer-control-case-v1', 'id': case['id'], 'type': case['type'],
             'status': status, 'qualification': 'NOT_QUALIFIED', 'elapsed_s': round(elapsed, 6),
             'expected_sha256': _sha(_json_bytes(case.get('expected', case.get('expected_when_available')))),
             'observed': observed}
    if len(_json_bytes(value)) > MAX_CASE_LINE:
        detail = _json_bytes(value)
        if len(detail) > MAX_DETAIL:
            raise HarnessBudgetExceeded('case detail exceeds64KiB')
        rec = ctx.reports.write(case['id'] + '-output.json', detail)
        value['observed'] = {'retained_detail': _ref(rec), 'bytes': len(detail)}
    _emit(value, output_state)


def run():
    """Explicit future entrypoint. No caller may treat exit0 as qualification."""
    start = time.monotonic()
    deadline = start + 300.0
    def check():
        if time.monotonic() > deadline:
            raise HarnessDeadlineExceeded('original300s deadline exceeded')
    owned, output_state, ctx = _Owned(), {'bytes': 0}, None
    try:
        if len(sys.argv) != 1:
            raise HarnessRefusal('no arguments accepted')
        if sys.flags.isolated != 1 or sys.flags.dont_write_bytecode != 1:
            raise HarnessRefusal('isolated -I and no-bytecode -B required')
        _capabilities()
        try:
            os.lstat(ROOT)
        except FileNotFoundError:
            pass
        else:
            raise HarnessRefusal('evidence root already exists')
        reader_path, reader_sha = PINS['reader']
        reader_source = _bootstrap_read(reader_path, 1 << 20, owned, check)
        reader_ns = _load_verified(reader_source, reader_path, reader_sha, 'beta_controls_real_reader')
        loader = reader_ns['EvidenceReader'](check)
        sources, namespaces = {'reader': reader_source}, {'reader': reader_ns}
        for key, (path, digest) in PINS.items():
            if key == 'reader':
                continue
            data = loader.read_bytes(path, 1 << 20)
            if _sha(data) != digest:
                raise HarnessRefusal('input pin mismatch: ' + key)
            sources[key] = data
            if key in ('capture4', 'schema2', 'adapter3'):
                namespaces[key] = _load_verified(data, path, digest, 'beta_controls_' + key)
            check()
        plan_bytes = loader.read_bytes(PLAN_PATH, 1 << 20)
        if _sha(plan_bytes) != PLAN_SHA:
            raise HarnessRefusal('operative controls plan pin mismatch')
        plan = _parse(plan_bytes)
        deferred_ids = tuple('DF' + str(index).zfill(2) for index in range(1, 16)) + tuple(
            'DP' + str(index).zfill(2) for index in range(24))
        expected_ids = RD_IDS + CA_IDS + SC_IDS + AD_IDS + deferred_ids
        cases = plan['cases']
        if plan.get('format') != 'beta-consumer-controls-plan-v2' or type(cases) is not list:
            raise HarnessRefusal('operative plan format/cases')
        if tuple(case['id'] for case in cases) != expected_ids:
            raise HarnessRefusal('harness and frozen plan case set/order differ')
        if len(cases) * MAX_CASE_LINE + MAX_SUMMARY > MAX_STDOUT:
            raise HarnessRefusal('case-line worst-case stdout exceeds1MiB')
        for case in cases:
            is_deferred = case['id'] in deferred_ids
            if is_deferred != case['type'].startswith('DEFERRED_'):
                raise HarnessRefusal('deferred case/type mismatch')
            if not is_deferred and type(case.get('expected')) is not dict:
                raise HarnessRefusal('case missing frozen expectation')
            if is_deferred and not all(key in case for key in
                                       ('expected_when_available', 'missing_genuine_artifact', 'unreachable_entrypoint', 'prerequisites')):
                raise HarnessRefusal('deferred prerequisite/entrypoint missing')
        pinned_plan = _parse(sources['mols39_plan_v5'])
        if tuple(pinned_plan['order']) != ORDER:
            raise HarnessRefusal('pinned MOLS plan order disagrees')
        if loader.report()['unresolved'] != []:
            raise HarnessRefusal('bootstrap reader unresolved acquisition/close')
        check()
        ctx = _Context(owned, check, sources, namespaces)
        _create_root(ctx)
        protected_before = _protected_state()
        ctx.root.write('run-start.json', _json_bytes({
            'format': 'beta-negative-controls-run-start-v1', 'plan_sha256': PLAN_SHA,
            'pins': {key: {'path': value[0], 'sha256': value[1]} for key, value in PINS.items()},
            'interpreter': sys.executable, 'isolated': sys.flags.isolated,
            'dont_write_bytecode': sys.flags.dont_write_bytecode,
            'protected_before': protected_before, 'qualification': 'NOT_QUALIFIED',
            'authority': 'NEGATIVE_CONTROL_AND_BOUNDARY_EVIDENCE_ONLY'}))
    except Exception as exc:
        try:
            owned.close_since(0)
        except BaseException as close_exc:
            owned.errors.append({'stage': 'precase_cleanup', 'error': repr(close_exc)})
        code = 5 if isinstance(exc, HarnessDeadlineExceeded) else 7
        _emit({'format': 'beta-consumer-controls-summary-v1', 'status': 'REFUSED_BEFORE_CASES',
               'exit_code': code, 'error': _pair(exc), 'harness_close_errors': owned.errors,
               'qualification': 'NOT_QUALIFIED', 'runtime_authority': False}, output_state, summary=True)
        return code
    except BaseException as exc:
        _emit({'format': 'beta-consumer-controls-summary-v1', 'status': 'BOOTSTRAP_BASE_EXCEPTION',
               'exception': type(exc).__name__, 'qualification': 'NOT_QUALIFIED'}, output_state, summary=True)
        try:
            owned.close_since(0)
        finally:
            raise
    counts, stop = {}, None
    try:
        for case in cases:
            case_start = time.monotonic()
            mark = len(owned.rows)
            observed, status = None, None
            if case['type'].startswith('DEFERRED_'):
                status = 'DEFERRED_NOT_EXECUTED'
                observed = {'executed': False, 'missing_genuine_artifact': case['missing_genuine_artifact'],
                            'unreachable_entrypoint': case['unreachable_entrypoint']}
            elif stop is not None:
                status, observed = stop, {'executed': False}
            else:
                try:
                    check()
                    ctx.last_reader = None
                    if case['id'] in RD_IDS:
                        observed = _reader_case(case['id'], ctx)
                    elif case['id'] in CA_IDS:
                        observed = _capture_case(case['id'], ctx)
                    elif case['id'] in SC_IDS:
                        observed = _schema_case(case['id'], ctx)
                    else:
                        observed = _adapter_case(case['id'], ctx)
                    check()  # original deadline after EVERY case, before matching/output
                    if ctx.budget_latched:
                        raise HarnessBudgetExceeded('retained-byte budget latched')
                    status = 'MATCH' if _exact(observed, case['expected']) else 'MISMATCH'
                except InconclusivePrecondition as exc:
                    status, observed = 'INCONCLUSIVE_PRECONDITION', {'rule': str(exc)}
                except HarnessDeadlineExceeded as exc:
                    stop = status = 'NOT_RUN_DEADLINE'
                    observed = {'case_started': True, 'error': str(exc)}
                except HarnessBudgetExceeded as exc:
                    stop = status = 'NOT_RUN_BUDGET'
                    observed = {'case_started': True, 'error': str(exc)}
                except Exception as exc:
                    status, observed = 'ERROR', {'exception': _pair(exc)}
                except BaseException as exc:
                    retained = None
                    if ctx.last_reader is not None:
                        ctx.retained_exception_readers.append(ctx.last_reader)
                        try:
                            retained = ctx.last_reader.report()
                            ctx.retain_report(case['id'] + '-base-exception', retained)
                        except Exception as report_exc:
                            retained = {'report_unavailable': repr(report_exc)}
                    _emit_case(case, 'BASE_EXCEPTION', {'exception': type(exc).__name__,
                               'reader_unresolved': retained.get('unresolved') if type(retained) is dict else None},
                               time.monotonic() - case_start, ctx, output_state)
                    raise
                finally:
                    # At most one attempt, even if native close raises. Never retry.
                    owned.close_since(mark)
            counts[status] = counts.get(status, 0) + 1
            _emit_case(case, status, observed, time.monotonic() - case_start, ctx, output_state)
            # The cutoff is not renewed for deferred lines or cleanup/output work.
            if time.monotonic() > deadline:
                stop = 'NOT_RUN_DEADLINE'
        protected_after = _protected_state()
        protected_unchanged = _exact(protected_before, protected_after)
        if stop == 'NOT_RUN_DEADLINE':
            code = 5
        elif stop == 'NOT_RUN_BUDGET':
            code = 6
        elif counts.get('MISMATCH', 0) or counts.get('ERROR', 0) or not protected_unchanged:
            code = 3
        elif counts.get('INCONCLUSIVE_PRECONDITION', 0):
            code = 4
        else:
            code = 0
        summary = {'format': 'beta-consumer-controls-summary-v1', 'exit_code': code,
                   'status': 'NEGATIVE_CONTROLS_MATCHED_NOT_QUALIFIED' if code == 0 else 'NEGATIVE_CONTROLS_NONZERO_NOT_QUALIFIED',
                   'counts': counts, 'cases': len(cases), 'plan_sha256': PLAN_SHA,
                   'qualification': 'NOT_QUALIFIED', 'mandatory_deferred_obligations_waived': False,
                   'protected_unchanged': protected_unchanged, 'protected_after': protected_after,
                   'elapsed_s': round(time.monotonic() - start, 6), 'retained_bytes_before_summary': ctx.retained,
                   'stdout_bytes_before_summary': output_state['bytes'], 'evidence_root': ROOT,
                   'canonical_audit_written': False, 'release_authority': False,
                   'runtime_authority': False, 'scientific_authority': False}
        try:
            ctx.root.write('run-summary.json', _json_bytes(summary))
        except HarnessBudgetExceeded:
            summary.update(exit_code=6, status='RETAINED_BUDGET_NOT_QUALIFIED', summary_file_written=False)
            code = 6
        owned.close_since(0)
        if owned.errors:
            summary.update(exit_code=3, status='HARNESS_CLOSE_UNCERTAINTY_NOT_QUALIFIED',
                           harness_close_errors=owned.errors)
            code = 3
        _emit(summary, output_state, summary=True)
        return code
    finally:
        owned.close_since(0)


if __name__ == '__main__':
    sys.exit(run())
