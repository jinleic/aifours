#!/usr/bin/env python3
"""SOURCE ONLY, UNEXECUTED. Consumer-visible finite negative/boundary controls.

Oracle: beta-consumer-controls-plan-v3.json, frozen before this source. V1 source
and plans v1/v2 remain immutable, unexecuted historical records. SC19 is retired,
not renamed. No private-validator/source-text/wiring/default/mock-success oracle,
fixed ledger IDs/cardinality, persistence counts or production-message assertions.

All genuine baseline/seven negatives/C1-C4/twenty positions/derivation successes
remain deferred. Exit0 is NOT_QUALIFIED. No execution authority is granted here.
Nothing loads/compiles/reads/writes at import; run() is the explicit future entry.
Require independent review, separate exact parent GO, fresh gate and -I -B.
"""
import copy
import hashlib
import json
import os
import stat
import sys
import time

RUN = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h'
MOLS = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39'
ROOT = RUN + '/evidence/beta-consumer-controls-v1'
PLAN_PATH = RUN + '/control/beta-consumer-controls-plan-v3.json'
PLAN_SHA = 'd0bed613c1e169ef4b984e0101908ef3d7f23907de3eeacebc725586e2be3c54'
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
          'RD10A', 'RD10B', 'RD10C', 'RD10D', 'RD11A', 'RD11B')
CA_IDS = ('CA00', 'CA02', 'CA03', 'CA04', 'CA08', 'CA09', 'CA12', 'CA14', 'CA16',
          'CA18', 'CA20', 'CA21', 'CA25', 'CA28', 'CA30', 'CA31', 'CA33', 'CA36',
          'CA41', 'CA43', 'CA45', 'CA48', 'CA49', 'CA51', 'CA53', 'CA54', 'CA56',
          'CA58', 'CA60', 'CA61', 'CA62', 'CA64', 'CA65', 'CA66', 'CA67', 'CA68',
          'CA69', 'CA71', 'CA75', 'CA77', 'CA79', 'CA80', 'CA82', 'CA84', 'CA87',
          'CA88', 'CA90', 'CA92', 'CA94', 'CA98', 'CA99', 'CA100', 'CA101',
          'CA102', 'CA103', 'CA105')
SC_IDS = ('SC32', 'SC33')
AD_IDS = ('AD00', 'AD01', 'AD02', 'AD04', 'AD06', 'AD07', 'AD09', 'AD14', 'AD15',
          'AD16', 'AD18', 'AD22', 'AD23', 'AD24', 'AD25', 'AD26', 'AD27',
          'AD28', 'AD29', 'AD30', 'AD33', 'AD34', 'AD35', 'AD36', 'AD37', 'AD39', 'AD40')
RESULT = b'{"label":"SYNTHETIC_FIXTURE beta-consumer-controls-v1 result bytes; not plan evidence","status":"SYNTHETIC"}\n'
RECEIPT = b'{"label":"SYNTHETIC_FIXTURE receipt; binds bytes only, not runtime truth"}\n'
INPUT_A = b'SYNTHETIC_FIXTURE input pin A\n'
STDERR_NONEMPTY = b'SYNTHETIC_FIXTURE stderr line\n'
DATA_BYTES = b'0123456789abcdef0123456789abcdef'
MAX_STDOUT, MAX_RETAINED = 1 << 20, 20 << 20
MAX_CASE_LINE, MAX_SUMMARY, MAX_DETAIL = 4096, 16384, 65536


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


def _error_type(retained_repr):
    # Stable exception TYPE only, never production diagnostic wording.
    return retained_repr.split('(', 1)[0] if type(retained_repr) is str else None


def _attempt(function):
    try:
        return function(), None
    except (HarnessDeadlineExceeded, HarnessBudgetExceeded):
        raise
    except InjectedBaseInterrupt as exc:
        return None, exc
    except Exception as exc:
        return None, exc


def _exception_type(exc):
    return type(exc).__name__ if exc is not None else None


def _outcome(function):
    value, exc = _attempt(function)
    return {'exception': type(exc).__name__} if exc is not None else value


def _relative_bytes(value, initial_length):
    if value == initial_length:
        return 'len'
    if value == initial_length + 1:
        return 'len+1'
    return 'zero' if value == 0 else 'other'


def _observation(row, length):
    return {'bytes': _relative_bytes(row['bytes_seen'], length), 'eof': row['eof'],
            'before': row['before'] is not None, 'after': row['after'] is not None,
            'completed': row['completed']}


def _all_closed(report):
    return all(row['state'] == 'CLOSED' and row['close_attempted'] is True
               for row in report['resources'])


def _settled(report):
    return all(row['state'] in ('CLOSED', 'NOT_ACQUIRED') for row in report['resources'])


def _state(report):
    if type(report) is not dict or type(report.get('unresolved')) is not list:
        return 'UNAVAILABLE'
    return 'PRESENT' if report['unresolved'] else 'EMPTY'


def _file_observation(report, path, completed=None):
    for row in reversed(report['observations']):
        if row['kind'] == 'file' and row['path'] == path and (completed is None or row['completed'] is completed):
            return row
    return None


def _unknown_target(report, path, kind='fd'):
    # IDs are only dynamic relational joins to the public report's unresolved set.
    # No numeric ID or position/cardinality is an oracle.
    for row in report['resources']:
        if (row['path'] == path and row['kind'] == kind and row['state'] == 'UNKNOWN'
                and row['id'] in report['unresolved']):
            return row
    return None


def _same_unknown(report, prior):
    return prior is not None and any(row['id'] == prior['id'] and row['path'] == prior['path']
                                    and row['state'] == 'UNKNOWN' and row['id'] in report['unresolved']
                                    for row in report['resources'])


class _Owned:
    """Harness-owned fds: retain before observations; one close attempt, never retry.

    Cleanup records all failures without replacing an already propagating module
    BaseException. Every cleanup error latches final failure; ambiguity is never
    labelled closure. Failed close numbers remain retained, never blindly retried.
    """
    def __init__(self):
        self.rows, self.errors = [], []

    def retain(self, fd, label):
        row = {'fd': fd, 'label': label, 'close_attempted': False,
               'closed': False, 'close_error': None}
        self.rows.append(row)
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
        return first


def _open_dir(path, owned):
    mark, selected = len(owned.rows), None
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
    mark = len(owned.rows)
    try:
        parts = _parts(path)
        parent = _open_dir('/' + '/'.join(parts[:-1]), owned)
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


def _load_verified(source, path, digest, name):
    if type(source) is not bytes or _sha(source) != digest:
        raise HarnessRefusal('source pin mismatch: ' + path)
    namespace = {'__name__': name, '__file__': path}
    exec(compile(source, path, 'exec', dont_inherit=True), namespace)
    return namespace


class _Clock:
    def __init__(self, base):
        self.base, self.armed = base, False
        self.real_deadline, self.real_hook_ran = None, False

    def arm(self):
        self.armed = True

    def check(self):
        self.base()
        if self.armed or (self.real_deadline is not None and time.monotonic() > self.real_deadline):
            raise ControlDeadlineExpired('LABELLED original deadline expiry')


class _IteratorProxy:
    """Only explicit owning close is tracked; trusted scandir may close at EOF."""
    def __init__(self, proxy, rec):
        self.proxy, self.rec = proxy, rec

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.rec['handle'])

    def close(self):
        self.proxy.close_iterator(self.rec)


class _FaultOS:
    """Separate verified reader namespace instrumentation, never process-wide os.

    Native identities are retained before post-call rules. Handles withheld by an
    acquisition fault are cleared using exact retained fd dev/ino or original
    iterator object identity. Ledger record IDs are never expected constants.
    """
    def __init__(self, rules):
        self.rules, self.rows, self.violations = rules, [], []

    def __getattr__(self, name):
        return getattr(os, name)

    def _fire(self, op, phase, target, result=None):
        for rule in self.rules:
            if rule.get('done') or rule['op'] != op or rule['phase'] != phase:
                continue
            if rule.get('target') is not None and rule['target'] != target:
                continue
            if rule.get('condition') == 'data' and not result:
                continue
            if rule.get('condition') == 'eof' and result != b'':
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
        self.violations.append('untracked/already-closed descriptor')
        raise RuntimeError('LABELLED proxy refuses untracked descriptor')

    def open(self, path, flags, *, dir_fd=None):
        target = path if path == '/' else os.path.basename(path)
        self._fire('open', 'before', target)
        fd = os.open(path, flags) if dir_fd is None else os.open(path, flags, dir_fd=dir_fd)
        rec = {'kind': 'fd', 'fd': fd, 'target': target, 'closed': False,
               'owning_close_attempted': False, 'native_closes': 0, 'harness_closes': 0,
               'orphan': False, 'identity': None}
        self.rows.append(rec)
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
        if rec['owning_close_attempted']:
            self.violations.append('second owning close attempt')
            raise RuntimeError('LABELLED duplicate owning close refused')
        try:
            self._fire('close', 'before', rec['target'])
        except BaseException:
            rec['orphan'] = True
            raise
        rec['owning_close_attempted'] = True
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
               'closed': False, 'owning_close_attempted': False,
               'native_closes': 0, 'harness_closes': 0, 'orphan': False}
        self.rows.append(rec)
        try:
            self._fire('scandir', 'after', anchor['target'])
        except BaseException:
            rec['orphan'] = True
            raise
        return _IteratorProxy(self, rec)

    def close_iterator(self, rec):
        if rec['owning_close_attempted']:
            self.violations.append('second explicit iterator close')
            raise RuntimeError('LABELLED duplicate iterator close refused')
        rec['owning_close_attempted'] = True
        rec['handle'].close()
        rec['closed'], rec['native_closes'] = True, rec['native_closes'] + 1

    def clear_orphans(self):
        for rec in self.rows:
            if rec['closed'] or not rec['orphan'] or rec['owning_close_attempted']:
                continue
            try:
                if rec['kind'] == 'fd':
                    info = os.fstat(rec['fd'])
                    if rec['identity'] != (info.st_dev, info.st_ino):
                        self.violations.append('orphan identity mismatch; no close')
                        continue
                    rec['owning_close_attempted'] = True
                    os.close(rec['fd'])
                else:
                    if id(rec['handle']) != rec['object_id']:
                        self.violations.append('iterator identity mismatch; no close')
                        continue
                    rec['owning_close_attempted'] = True
                    rec['handle'].close()
            except Exception as exc:
                self.violations.append('orphan cleanup uncertain: ' + type(exc).__name__)
                continue  # retained; never retry an attempted destructive close
            rec['closed'] = True
            rec['harness_closes'] += 1

    def closed_once(self, rec):
        return rec is not None and rec['closed'] and rec['native_closes'] + rec['harness_closes'] == 1

    def accounting_ok(self):
        return not self.violations and all(self.closed_once(row) for row in self.rows)

    def native(self, target, kind='fd'):
        return next((row for row in self.rows if row['target'] == target and row['kind'] == kind), None)


def _raise_instance(exc):
    def action():
        raise exc
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
        os.mkdir(name, 0o700, dir_fd=self.fd)
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
                'ino': info.st_ino, 'nlink': info.st_nlink, 'data': data, 'metadata': _meta(info)}

    def append_growth(self, name, data):
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
                raise OSError('short growth append')
        finally:
            self.ctx.owned.close(rec)

    def symlink(self, name, target):
        self._name(name)
        self._name(target)
        self.ctx.reserve(len(target.encode('utf-8')))
        os.symlink(target, name, dir_fd=self.fd)

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
    def __init__(self, owned, check, sources, namespaces, input_metadata):
        self.owned, self.check = owned, check
        self.sources, self.ns, self.input_metadata = sources, namespaces, input_metadata
        self.retained = 0
        self.root = self.fx = self.reports = None
        self.ca, self.last_reader = None, None
        self.retained_exception_readers, self.proxies = [], []
        self.budget_latched = False

    def reserve(self, count):
        if type(count) is not int or count < 0 or self.retained + count > MAX_RETAINED:
            self.budget_latched = True
            raise HarnessBudgetExceeded('retained-byte cap')
        self.retained += count

    def reader(self, check=None, rules=None):
        check = self.check if check is None else check
        proxy, namespace = None, self.ns['reader']
        if rules is not None:
            path, digest = PINS['reader']
            namespace = _load_verified(self.sources['reader'], path, digest,
                                       'beta_control_labelled_fault_reader')
            proxy = _FaultOS(rules)
            self.proxies.append(proxy)
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
    os.mkdir('beta-consumer-controls-v1', 0o700, dir_fd=parent['fd'])
    root = ctx.owned.retain(os.open('beta-consumer-controls-v1', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                                  dir_fd=parent['fd']), ROOT)
    ctx.owned.close(parent)
    ctx.owned.close(run)
    ctx.root = _Fx(ctx, ROOT, root)
    ctx.fx, ctx.reports = ctx.root.mkdir('fx'), ctx.root.mkdir('reports')


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


def _identity_matches(native, metadata):
    return native is not None and native['identity'] == (metadata['dev'], metadata['ino'])


def _reader_case(case_id, ctx):
    d = ctx.fx.mkdir(case_id.lower())
    if case_id == 'RD01':
        data, empty = d.write('data.bin', DATA_BYTES), d.write('empty.bin', b'')
        r, _ = ctx.reader()
        got = r.read_bytes(data['path'], len(DATA_BYTES))
        last = r.last_file(data['path'])
        empty_got = r.read_bytes(empty['path'], 0)
        report = r.report()
        return {'read_equals_written': got == DATA_BYTES, 'exact_cap_completed': last['completed'],
                'actual_hash_matches': last['sha256'] == data['sha256'],
                'actual_metadata_matches_fixture': _exact(last['after'], data['metadata']),
                'actual_bytes_and_eof_retained': last['bytes_seen'] == len(DATA_BYTES) and last['eof'] is True,
                'empty_cap0_returns_empty': empty_got == b'',
                'all_resources_closed': _all_closed(report), 'unresolved_empty': not report['unresolved']}
    if case_id == 'RD02':
        target = d.write('target.bin', DATA_BYTES)
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
        ordinary = r.read_bytes(target['path'], len(DATA_BYTES))
        report = r.report()
        rows = [_file_observation(report, path) for path in paths]
        refusal = ctx.ns['reader']['EvidenceRefusal']
        return {'ordinary_target_readable': ordinary == DATA_BYTES,
                'symlink_leaf_native_oserror': isinstance(failures[0], OSError) and not isinstance(failures[0], refusal),
                'symlink_ancestor_native_oserror': isinstance(failures[1], OSError) and not isinstance(failures[1], refusal),
                'fifo_exception_type': _exception_type(failures[2]),
                'hardlink_exception_type': _exception_type(failures[3]),
                'failing_paths_publish_no_success': all(r.last_file(path) is None for path in paths),
                'failing_reads_accept_no_file_bytes': all(row is not None and row['bytes_seen'] == 0 for row in rows),
                'fifo_actual_metadata_matches_fixture': _exact(rows[2]['before'], _meta(d.lstat('fifo'))),
                'hardlink_actual_metadata_matches_fixture': _exact(rows[3]['before'], _meta(d.lstat('hl-a.bin'))),
                'known_resources_settled': _settled(report), 'unresolved_empty': not report['unresolved']}
    if case_id == 'RD03':
        data = d.write('ten.bin', b'0123456789')
        census = d.mkdir('census')
        for name in ('a', 'b', 'c'):
            census.write(name, b'x')
        r, _ = ctx.reader()
        below = _attempt(lambda: r.read_bytes(data['path'], 9))[1]
        exact = r.read_bytes(data['path'], 10)
        boolean = _attempt(lambda: r.read_bytes(data['path'], True))[1]
        names = r.directory_names(census.path)
        cap2 = _attempt(lambda: r.directory_names(census.path, 2))[1]
        failed = r.report()['observations'][-1]
        names3 = r.directory_names(census.path, 3)
        cap257 = _attempt(lambda: r.directory_names(census.path, 257))[1]
        report = r.report()
        return {'below_cap_exception_type': _exception_type(below), 'exact_cap_bytes_match': exact == b'0123456789',
                'bool_cap_exception_type': _exception_type(boolean), 'census_names': names,
                'entry_cap_exception_type': _exception_type(cap2),
                'entry_cap_retains_actual_names': sorted(failed['names']) == ['a', 'b', 'c'],
                'failed_census_not_completed': failed['completed'] is False,
                'exact_entry_cap_names': names3, 'over_max_entry_cap_exception_type': _exception_type(cap257),
                'known_resources_settled': _settled(report), 'unresolved_empty': not report['unresolved']}
    if case_id == 'RD04':
        a, b = d.write('same-a.bin', DATA_BYTES), d.write('same-b.bin', DATA_BYTES)
        r, _ = ctx.reader()
        av, bv = r.read_bytes(a['path'], 64), r.read_bytes(b['path'], 64)
        am, bm = r.last_file(a['path']), r.last_file(b['path'])
        report = r.report()
        return {'bytes_equal': av == bv, 'hashes_equal': am['sha256'] == bm['sha256'],
                'actual_inodes_distinct': am['after']['ino'] != bm['after']['ino'],
                'actual_identities_match_fixtures': _exact(am['after'], a['metadata']) and _exact(bm['after'], b['metadata']),
                'all_resources_closed': _all_closed(report), 'unresolved_empty': not report['unresolved']}
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
            native_before = tuple(id(row) for row in proxy.rows)
            second = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            if case_id == 'RD05E' and not clock.real_hook_ran:
                raise InconclusivePrecondition('real deadline crossed before native-return hook')
            observed = {'exception_type': _exception_type(exc),
                        'observation': _observation(_file_observation(report, data['path']), len(DATA_BYTES)),
                        'all_resources_closed': _all_closed(report), 'unresolved_empty': not report['unresolved'],
                        'no_success_snapshot': r.last_file(data['path']) is None,
                        'second_exception_type': _exception_type(second),
                        'second_attempt_acquires_no_native_handle': tuple(id(row) for row in proxy.rows) == native_before}
            if case_id == 'RD05E':
                observed['real_crossing_after_native_return'] = clock.real_hook_ran and time.monotonic() > clock.real_deadline
        finally:
            proxy.clear_orphans()
        observed['all_native_handles_closed_once'] = proxy.accounting_ok()
        ctx.retain_report(case_id, report)
        return observed
    if case_id in ('RD06A', 'RD06B'):
        data, nxt = d.write('close.bin', DATA_BYTES), d.write('next.bin', DATA_BYTES)
        clock = _Clock(ctx.check)
        action = _raise_instance(InjectedCloseFault('LABELLED close fault')) if case_id == 'RD06A' else clock.arm
        r, proxy = ctx.reader(clock.check, [_rule('close', 'after', 'close.bin', action)])
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            report = r.report()
            row = _file_observation(report, data['path'])
            retained = row is not None and row['bytes_seen'] == len(DATA_BYTES) and row['eof'] is True and _exact(row['after'], data['metadata'])
            native = proxy.native('close.bin')
            observed = {'exception_type': _exception_type(exc), 'actual_bytes_eof_metadata_retained': retained,
                        'no_success_snapshot': r.last_file(data['path']) is None}
            if case_id == 'RD06A':
                unknown = _unknown_target(report, data['path'])
                observed.update(unknown_leaf_retained=unknown is not None,
                                native_leaf_identity_matches_fixture=_identity_matches(native, data['metadata']),
                                unresolved_present=bool(report['unresolved']),
                                next_read_bytes_match=r.read_bytes(nxt['path'], 64) == DATA_BYTES,
                                same_unknown_leaf_persists=_same_unknown(r.report(), unknown))
            else:
                observed.update(all_resources_closed=_all_closed(report), unresolved_empty=not report['unresolved'])
        finally:
            proxy.clear_orphans()
        observed.update(original_leaf_closed_once=proxy.closed_once(native),
                        all_native_handles_closed_once=proxy.accounting_ok())
        ctx.retain_report(case_id, r.report())
        return observed
    if case_id in ('RD07A', 'RD07C'):
        data, nxt = d.write('acq.bin', DATA_BYTES), d.write('next.bin', DATA_BYTES)
        scan = d.mkdir('dir')
        primary = InjectedAcquisitionFault('LABELLED unexpected acquisition exception')
        rule = (_rule('open', 'after', 'acq.bin', _raise_instance(primary)) if case_id == 'RD07A'
                else _rule('scandir', 'after', 'dir', _raise_instance(primary)))
        r, proxy = ctx.reader(rules=[rule])
        try:
            operation = (lambda: r.read_bytes(data['path'], 64)) if case_id == 'RD07A' else (lambda: r.directory_names(scan.path))
            exc = _attempt(operation)[1]
            report = r.report()
            if case_id == 'RD07A':
                unknown = _unknown_target(report, data['path'])
                native = proxy.native('acq.bin')
                proxy.clear_orphans()
                observed = {'exception_type': _exception_type(exc), 'unknown_leaf_retained': unknown is not None,
                            'native_leaf_identity_matches_fixture': _identity_matches(native, data['metadata']),
                            'withheld_handle_cleared_once': native is not None and native['harness_closes'] == 1 and proxy.closed_once(native),
                            'unresolved_present': bool(report['unresolved']),
                            'next_read_bytes_match': r.read_bytes(nxt['path'], 64) == DATA_BYTES,
                            'same_unknown_leaf_persists': _same_unknown(r.report(), unknown)}
            else:
                iterator = proxy.native('dir', 'iterator')
                observed = {'exception_type': _exception_type(exc),
                            'primary_exception_preserved': exc.__context__ is primary and report['observations'][-1]['error'] == repr(primary),
                            'unknown_iterator_retained': _unknown_target(report, scan.path, 'scandir') is not None,
                            'native_anchor_identity_matches_fixture': iterator is not None and iterator['anchor_identity'] ==
                                (os.fstat(scan.fd).st_dev, os.fstat(scan.fd).st_ino),
                            'unresolved_present': bool(report['unresolved'])}
        finally:
            proxy.clear_orphans()
        if case_id == 'RD07C':
            observed['original_iterator_cleared_once'] = iterator is not None and iterator['harness_closes'] == 1 and proxy.closed_once(iterator)
        observed['all_native_handles_closed_once'] = proxy.accounting_ok()
        ctx.retain_report(case_id, r.report())
        return observed
    if case_id in ('RD08A', 'RD08B', 'RD08C'):
        data = d.write('rw.bin', DATA_BYTES)
        primary = (InjectedReadFault('LABELLED primary read fault') if case_id == 'RD08A'
                   else InjectedBaseInterrupt('LABELLED base interrupt'))
        rules = [_rule('read', 'before', 'rw.bin', _raise_instance(primary))]
        if case_id != 'RD08C':
            rules.append(_rule('close', 'after', 'rw.bin', _raise_instance(InjectedCloseFault('LABELLED close fault'))))
        r, proxy = ctx.reader(rules=rules)
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 64))[1]
            report = r.report()
            row = _file_observation(report, data['path'])
            native = proxy.native('rw.bin')
            observed = {'exception_type': _exception_type(exc),
                        'primary_error_preserved': row is not None and row['error'] == repr(primary)}
            if case_id == 'RD08C':
                ctx.retained_exception_readers.append(r)
                observed.update(same_primary_exception=exc is primary, reader_report_available=type(report) is dict,
                                all_resources_closed=_all_closed(report), unresolved_empty=not report['unresolved'])
            else:
                unknown = _unknown_target(report, data['path'])
                observed.update(exception_context_is_primary=exc.__context__ is primary,
                                cleanup_error_type=_error_type(unknown['close_error']) if unknown else None,
                                unresolved_present=bool(report['unresolved']),
                                native_leaf_identity_matches_fixture=_identity_matches(native, data['metadata']))
        finally:
            proxy.clear_orphans()
        if case_id != 'RD08C':
            observed['original_leaf_closed_once'] = proxy.closed_once(native)
        observed['all_native_handles_closed_once'] = proxy.accounting_ok()
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
        latest = _file_observation(report, data['path'])
        actual = _meta(d.lstat('stale.bin'))
        return {'first_read_matches': first == DATA_BYTES, 'second_exception_type': _exception_type(exc),
                'stale_snapshot_unchanged': _exact(stale, r.last_file(data['path'])),
                'stale_snapshot_one_link': stale['after']['nlink'] == 1,
                'current_file_multiple_links': actual['nlink'] > 1,
                'failed_read_not_completed': latest['completed'] is False,
                'failed_read_metadata_matches_current_file': _exact(latest['before'], actual),
                'known_resources_settled': _settled(report), 'unresolved_empty': not report['unresolved']}
    if case_id == 'RD10A':
        exc = _attempt(lambda: ctx.ns['reader']['EvidenceReader'](None))[1]
        return {'exception_type': _exception_type(exc)}
    if case_id == 'RD10B':
        failures, evidence = [], []
        for value in (True, False):
            r, proxy = ctx.reader(lambda v=value: v, rules=[])
            failures.append(_attempt(lambda: r.read_bytes(d.path + '/x.bin', 64))[1])
            evidence.append((r.report(), proxy))
        return {'true_exception_type': _exception_type(failures[0]), 'false_exception_type': _exception_type(failures[1]),
                'no_native_acquisition': all(not proxy.rows for _, proxy in evidence),
                'no_success_observation': all(not any(row['completed'] for row in report['observations']) for report, _ in evidence)}
    if case_id == 'RD10C':
        r, proxy = ctx.reader(rules=[])
        paths = ('relative/x', '/a/../b', '/' + '/'.join(['a'] * 129))
        failures = [_attempt(lambda p=path: r.read_bytes(p, 64))[1] for path in paths]
        return {'relative_exception_type': _exception_type(failures[0]), 'dotdot_exception_type': _exception_type(failures[1]),
                'component_limit_exception_type': _exception_type(failures[2]),
                'no_native_acquisition': not proxy.rows,
                'no_success_observation': not any(row['completed'] for row in r.report()['observations'])}
    if case_id == 'RD10D':
        clock = _Clock(ctx.check)
        clock.arm()
        r, proxy = ctx.reader(clock.check, rules=[])
        expired = True
        for _ in range(1024):
            exc = _attempt(lambda: r.read_bytes(d.path + '/never-opened.bin', 64))[1]
            expired = expired and type(exc) is ControlDeadlineExpired
        first = _attempt(lambda: r.read_bytes(d.path + '/never-opened.bin', 64))[1]
        second = _attempt(lambda: r.read_bytes(d.path + '/never-opened.bin', 64))[1]
        return {'documented_attempts_all_expired': expired, 'first_after_limit_exception_type': _exception_type(first),
                'second_after_limit_exception_type': _exception_type(second),
                'no_native_acquisition': not proxy.rows, 'unresolved_empty': not r.report()['unresolved']}
    if case_id in ('RD11A', 'RD11B'):
        initial = DATA_BYTES[:16]
        data = d.write('grow.bin', initial)
        rule = _rule('fstat', 'after', 'grow.bin', lambda: d.append_growth('grow.bin', b'x'))
        r, proxy = ctx.reader(rules=[rule])
        try:
            exc = _attempt(lambda: r.read_bytes(data['path'], 16 if case_id == 'RD11A' else 64))[1]
            report = r.report()
            row = _file_observation(report, data['path'])
            observed = {'exception_type': _exception_type(exc), 'observation': _observation(row, len(initial)),
                        'unresolved_empty': not report['unresolved']}
            if case_id == 'RD11A':
                observed['failed_read_metadata_matches_original'] = _exact(row['before'], data['metadata'])
            else:
                actual = _meta(d.lstat('grow.bin'))
                observed['native_sizes_show_growth'] = (row['before']['size'] == len(initial) and
                    row['after']['size'] == len(initial) + 1 and _exact(row['after'], actual))
        finally:
            proxy.clear_orphans()
        observed['all_native_handles_closed_once'] = proxy.accounting_ok()
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
    observed['source_pins'], observed['input_pins'] = copy.deepcopy(expectation['source_pins']), copy.deepcopy(expectation['input_pins'])
    records = (result, empty_result, stdout, stderr, empty_stdout, prefix_stdout, nonempty_stderr, receipt, input_a, same)
    snapshot = {record['path']: record['data'] for record in records}
    snapshot[PINS['capture4'][0]] = ctx.sources['capture4']
    ctx.ca = {'expectation': expectation, 'observed': observed, 'result': result, 'empty_result': empty_result,
              'stdout': stdout, 'stderr': stderr, 'empty_stdout': empty_stdout, 'prefix_stdout': prefix_stdout,
              'nonempty_stderr': nonempty_stderr, 'receipt': receipt, 'input_a': input_a, 'same': same,
              'empty_job_path': empty_job.path, 'no_job_path': no_job.path, 'path': d.path, 'snapshot': snapshot}
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
    callback = r.read_bytes
    capture, wrong = ctx.ns['capture4']['audit_capture'], _sha(b'other')
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
        return {'outcome': values, 'reader_state': _state(r.report())}
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
        return {'outcome': values, 'reader_state': _state(r.report())}
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
        d, pins = ctx.fx.mkdir('ca61'), {}
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
            value = 'SYNTHETIC leaf'
            for _ in range(40):
                value = {'nested': value}
            return value
        e['date_start'], o['date_start'] = nested(), nested()
    elif case_id == 'CA67':
        shared = {'v': [1, 2, {'SYNTHETIC': True}]}
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
        return {'outcome': values, 'reader_state': _state(r.report())}
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
        o['extra'] = 'SYNTHETIC extra'
    elif case_id == 'CA84':
        o['captures']['stdout'], o['captures']['bogus'] = None, 1
    elif case_id == 'CA87':
        e = None
    elif case_id == 'CA88':
        o = None
    elif case_id == 'CA90':
        r = None
        callback = lambda path, cap: _raise_instance(ValueError('LABELLED defined read refusal'))()
    elif case_id == 'CA92':
        def over_cap(path, cap):
            return b'\x00' * (cap + 1) if path == fixture['stdout']['path'] else r.read_bytes(path, cap)
        callback = over_cap
    elif case_id == 'CA94':
        r = None
        callback = lambda path, cap: _raise_instance(KeyError('LABELLED lookup fault'))()
    elif case_id == 'CA98':
        r = None
        callback = lambda path, cap: _raise_instance(InjectedBaseInterrupt('LABELLED base interrupt'))()
    elif case_id == 'CA99':
        e['input_pins'].update({fixture['receipt']['path']: fixture['receipt']['sha256'],
                                fixture['result']['path']: fixture['result']['sha256']})
        o['input_pins'] = copy.deepcopy(e['input_pins'])
        supplied = set()
        def single_use(path, cap):
            if path in supplied:
                raise OSError('LABELLED repeated coherent acquisition refused')
            supplied.add(path)
            return r.read_bytes(path, cap)
        callback = single_use
    elif case_id == 'CA100':
        e['input_pins'][fixture['receipt']['path']] = fixture['receipt']['sha256']
        o['input_pins'] = copy.deepcopy(e['input_pins'])
        failed = set()
        def latched_failure(path, cap):
            if path == fixture['receipt']['path']:
                if path in failed:
                    raise InjectedConsumerFault('LABELLED attempted replay of failed acquisition')
                failed.add(path)
                raise OSError('LABELLED receipt refusal')
            return r.read_bytes(path, cap)
        callback = latched_failure
    elif case_id == 'CA101':
        r = None
        snapshot = dict(fixture['snapshot'])
        def snapshot_read(path, cap):
            if path not in snapshot or len(snapshot[path]) > cap:
                raise OSError('LABELLED snapshot unavailable/cap')
            return snapshot[path]
        first = capture(e, o, snapshot_read)
        snapshot[fixture['stdout']['path']] = b'changed'
        second = capture(e, o, snapshot_read)
        return {'outcome': [first, second], 'reader_state': 'NOT_APPLICABLE'}
    elif case_id == 'CA102':
        o['actual_exit'], o['captures']['stdout'] = 5, None
        _use_stream(e, o, 'stderr', fixture['nonempty_stderr'])
        o['actual_artifact_names'].append('extra.bin')
        o['settlement']['unresolved'], o['resolved_argv'] = ['SYNTHETIC-unresolved'], ['SYNTHETIC mismatch']
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
        return {'outcome': values, 'reader_state': _state(r.report())}
    elif case_id != 'CA00':
        raise HarnessRefusal('unknown capture case')
    value = _outcome(lambda: capture(e, o, callback))
    return {'outcome': value, 'reader_state': _state(r.report()) if r is not None else 'NOT_APPLICABLE'}


def _schema_case(case_id, ctx):
    schema = ctx.ns['schema2']['audit_schema']
    primary = InjectedReadFault('LABELLED primary read fault') if case_id == 'SC32' else InjectedBaseInterrupt('LABELLED base interrupt')
    rules = [_rule('read', 'before', 'ext4_gate.py', _raise_instance(primary))]
    if case_id == 'SC32':
        rules.append(_rule('close', 'after', 'ext4_gate.py', _raise_instance(InjectedCloseFault('LABELLED close fault'))))
    r, proxy = ctx.reader(rules=rules)
    try:
        value, exc = _attempt(lambda: schema(ctx.sources['mols39_plan_v5'], 'DATA', {}, [],
                                           ctx.sources['original_dm21'], ctx.check, r.read_bytes))
        report = r.report()
        row = _file_observation(report, PINS['ext4_gate'][0])
        native = proxy.native('ext4_gate.py')
        observed = {'outcome': {'exception': type(exc).__name__} if exc is not None else value,
                    'primary_error_preserved': row is not None and row['error'] == repr(primary),
                    'native_gate_identity_matches_pinned_acquisition': _identity_matches(native, ctx.input_metadata['ext4_gate'])}
        if case_id == 'SC32':
            unknown = _unknown_target(report, PINS['ext4_gate'][0])
            observed.update(unresolved_present=bool(report['unresolved']), unknown_gate_leaf_retained=unknown is not None,
                            cleanup_error_type=_error_type(unknown['close_error']) if unknown else None)
        else:
            ctx.retained_exception_readers.append(r)
            observed.update(same_primary_exception=exc is primary, all_resources_closed=_all_closed(report),
                            unresolved_empty=not report['unresolved'])
    finally:
        proxy.clear_orphans()
    if case_id == 'SC32':
        observed['original_leaf_closed_once'] = proxy.closed_once(native)
    observed['all_native_handles_closed_once'] = proxy.accounting_ok()
    ctx.retain_report(case_id, report)
    return observed


class _PublicFaultReader:
    """Labelled public-method fault timing; no private ledger or count oracle.

    A completed real census may perform an additive namespace mutation. A fresh
    actual reread (same path, successful second native acquisition) arms a later
    report fault/cutoff. These are injection triggers only, not tested counts or
    forwarding expectations. No mock bytes or fabricated consumer result.
    """
    def __init__(self, reader, clock, *, census_actions=(), before_read=None,
                 report_fail_after_reread=False, arm_after_reread_report=False):
        self.reader, self.clock = reader, clock
        self.census_actions = list(census_actions)
        self.before_read = before_read
        self.report_fail_after_reread = report_fail_after_reread
        self.arm_after_reread_report = arm_after_reread_report
        self.native_paths, self.fresh_reread = set(), False

    def read_bytes(self, path, cap):
        if self.before_read is not None:
            self.before_read(path)
        value = self.reader.read_bytes(path, cap)
        if path in self.native_paths:
            self.fresh_reread = True
        self.native_paths.add(path)
        return value

    def last_file(self, path):
        return self.reader.last_file(path)

    def directory_names(self, path, cap=256):
        names = self.reader.directory_names(path, cap)
        if self.census_actions:
            action = self.census_actions.pop(0)
            if action is not None:
                action()
        return names

    def report(self):
        if self.fresh_reread and self.report_fail_after_reread:
            raise InjectedConsumerFault('LABELLED report fault after fresh native reread')
        value = self.reader.report()
        if self.fresh_reread and self.arm_after_reread_report:
            self.clock.arm()
        return value


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
    own_paths = [d.path + '/' + name for name in ('expectation.json', 'observation.json', 'context.json', 'freeze.json')]
    immutable = set(own_paths + [PINS[name][0] for name in
                                ('capture4', 'schema2', 'mols39_plan_v5', 'original_dm21', 'ext4_gate')]
                    + [result['path'], stdout['path'], stderr['path'], receipt['path']])
    prefix_authority = []
    if case_id == 'AD04':
        context['format'] = 'beta-parent-schema-context-v1'
    elif case_id == 'AD06':
        wrong_original = d.write('wrong-original.raw', ctx.sources['original_dm21'] + b'SYNTHETIC_WRONG_ORIGINAL\n')
        context['original_dm21'] = _ref(wrong_original)
        immutable.add(wrong_original['path'])
    elif case_id == 'AD07':
        audit = d.write('synthetic-prefix-audit.json', b'{"label":"SYNTHETIC_FIXTURE not canonical audit evidence"}\n')
        immutable.add(audit['path'])
        context['prefix'] = [{'item': 'DATA', 'files': {}, 'audit': _ref(audit)} for _ in range(20)]
        prefix_authority = [{'item': 'DATA', 'audit_sha256': audit['sha256']} for _ in range(20)]
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
    if case_id in ('AD18', 'AD22'):
        immutable.update((d.path + '/derivation.json', d.path + '/upstream-observation.json'))
    freeze = {'format': 'beta-parent-publication-freeze-v1', 'mode': e['mode'],
              'job_dir': job.path, 'immutable_paths': sorted(immutable), 'prefix_authority': prefix_authority}
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
    if case_id in ('AD18', 'AD22'):
        upstream = copy.deepcopy(o)
        upstream['actual_exit'] = 2
        upstream_rec = d.write('upstream-observation.json', _json_bytes(upstream))
        manifest = {'format': 'beta-parent-synthetic-derivation-v1',
                    'expectation_sha256': er['sha256'], 'observation_sha256': or_['sha256'],
                    'upstream_observation': _ref(upstream_rec),
                    'mutations': [{'path': ['actual_exit'], 'value': 120}]}
        context['derivation'] = _ref(d.write('derivation.json', _json_bytes(manifest)))
    context['publication_freeze'] = _ref(freeze_rec)
    cr = d.write('context.json', _json_bytes(context))
    inputs = {'expectation': _ref(er), 'observation': _ref(or_), 'context': _ref(cr)}
    if case_id == 'AD01':
        del inputs['context']
    elif case_id == 'AD02':
        inputs['expectation']['sha256'] = _sha(b'other')
    poison = d.write('poison.bin', DATA_BYTES) if case_id == 'AD30' else None
    return {'dir': d, 'job': job, 'links': links, 'result': result, 'stdout': stdout,
            'context': context, 'inputs': inputs, 'expectation_record': er, 'poison': poison}


def _decision_probe(decision):
    return {'verdict': decision.get('verdict'), 'causes': decision.get('causes'),
            'reader_state': _state(decision.get('reader')),
            'authority_flags': [decision.get(key) for key in
                                ('canonical_audit_written', 'release_authority', 'runtime_authority')],
            'has_retained_error': bool(decision.get('errors'))}


def _selected_bound(decision, fixture):
    selected = decision.get('selected_artifacts', {}).get('result.json')
    return (type(selected) is dict and selected.get('path') == fixture['result']['path']
            and selected.get('sha256') == fixture['result']['sha256']
            and selected.get('bytes') == fixture['result']['bytes']
            and _exact(selected.get('actual_metadata'), fixture['result']['metadata']))


def _adapter_case(case_id, ctx):
    fixture = _adapter_fixture(case_id, ctx)
    clock = _Clock(ctx.check)
    rules = ([_rule('open', 'after', 'poison.bin', _raise_instance(
        InjectedAcquisitionFault('LABELLED unexpected acquisition exception')))] if case_id == 'AD30' else None)
    r, proxy = ctx.reader(clock.check, rules)
    reader, inputs = r, fixture['inputs']
    original_inputs = copy.deepcopy(inputs)
    prior, poison_unknown, extras = None, None, {}
    if case_id in ('AD15', 'AD16'):
        if case_id == 'AD16':
            r.read_bytes(fixture['result']['path'], 16 << 20)
            prior = r.last_file(fixture['result']['path'])
        fixture['links'].hardlink(fixture['job'], 'result.json', 'result-hl.json')
    primary = InjectedBaseInterrupt('LABELLED base interrupt') if case_id == 'AD36' else InjectedConsumerFault('LABELLED consumer fault')
    if case_id == 'AD23':
        reader = _PublicFaultReader(r, clock, census_actions=(
            lambda: fixture['job'].write('late.bin', b'SYNTHETIC additive namespace fault\n'),))
    elif case_id == 'AD24':
        reader = _PublicFaultReader(r, clock, census_actions=(None,
            lambda: fixture['links'].hardlink(fixture['job'], 'result.json', 'result-hl2.json')))
    elif case_id in ('AD35', 'AD36'):
        def before_capture(path):
            if path == fixture['stdout']['path']:
                raise primary
        reader = _PublicFaultReader(r, clock, before_read=before_capture)
    elif case_id == 'AD39':
        mutated = [False]
        def mutate_refs(_):
            if not mutated[0]:
                mutated[0] = True
                inputs['expectation']['sha256'] = _sha(b'caller mutation')
                inputs['context'] = {'path': fixture['dir'].path + '/caller-mutated-context.json', 'sha256': _sha(b'caller')}
        reader = _PublicFaultReader(r, clock, before_read=mutate_refs)
    elif case_id == 'AD33':
        reader = _PublicFaultReader(r, clock, report_fail_after_reread=True)
    elif case_id == 'AD34':
        reader = _PublicFaultReader(r, clock, arm_after_reread_report=True)
    if case_id == 'AD30':
        poison_exc = _attempt(lambda: r.read_bytes(fixture['poison']['path'], 64))[1]
        poison_unknown = _unknown_target(r.report(), fixture['poison']['path'])
        proxy.clear_orphans()
        extras['poison_exception_type'] = _exception_type(poison_exc)
    check = (lambda: False) if case_id == 'AD37' else clock.check
    try:
        decision, exc = _attempt(lambda: ctx.ns['adapter3']['evaluate_pinned'](inputs, reader, check))
        if exc is not None:
            if isinstance(exc, InjectedBaseInterrupt):
                ctx.retained_exception_readers.append(r)
                report = r.report()
                observed = {'exception_type': _exception_type(exc), 'same_primary_exception': exc is primary,
                            'reader_report_available_after_exception': type(report) is dict,
                            'known_resources_settled': _settled(report), 'unresolved_empty': not report['unresolved']}
                ctx.retain_report(case_id, report)
                return observed
            return {'unexpected_exception_type': _exception_type(exc), 'reader_state': _state(r.report())}
        observed = _decision_probe(decision)
        if case_id == 'AD00':
            observed['selected_actual_bytes_and_identity_bound'] = _selected_bound(decision, fixture)
        elif case_id == 'AD02':
            actual = r.last_file(fixture['expectation_record']['path'])
            observed['actual_expectation_bytes_retained'] = (actual is not None and actual['completed'] is True
                and actual['sha256'] == fixture['expectation_record']['sha256']
                and _exact(actual['after'], fixture['expectation_record']['metadata']))
        elif case_id == 'AD16':
            observed['stale_success_retained_but_not_selected'] = (prior is not None and prior['completed'] is True
                and _exact(prior, r.last_file(fixture['result']['path']))
                and 'result.json' not in decision.get('selected_artifacts', {}))
        elif case_id in ('AD18', 'AD22'):
            synthetic = decision.get('synthetic_derivation')
            observed['synthetic_evidence'] = ({'requested': synthetic.get('requested'), 'verified': synthetic.get('verified'),
                'actual_exit_is_measured': synthetic.get('actual_exit_is_measured'),
                'manifest_matches_frozen_ref': _exact(synthetic.get('manifest'), fixture['context']['derivation']),
                'nested_kind': decision.get('nested_exit', {}).get('kind')} if type(synthetic) is dict else None)
        elif case_id == 'AD23':
            before, after = decision.get('directory_before'), decision.get('directory_after')
            observed['actual_census_retains_added_name'] = (type(before) is dict and type(after) is dict
                and 'late.bin' not in before['names'] and 'late.bin' in after['names'])
        elif case_id == 'AD24':
            report = r.report()
            failed = _file_observation(report, fixture['result']['path'], completed=False)
            actual = _meta(fixture['job'].lstat('result.json'))
            observed['selected_original_identity_retained'] = _selected_bound(decision, fixture)
            observed['failed_read_retains_changed_link_metadata'] = (failed is not None and failed['before'] is not None
                and actual['nlink'] > 1 and _exact(failed['before'], actual))
        elif case_id == 'AD25':
            observed['actual_result_identity_retained'] = _selected_bound(decision, fixture)
        elif case_id == 'AD30':
            observed['original_poison_uncertainty_retained'] = _same_unknown(r.report(), poison_unknown)
            observed['native_poison_identity_matches_fixture'] = _identity_matches(proxy.native('poison.bin'), fixture['poison']['metadata'])
        elif case_id == 'AD33':
            observed['caller_reader_report_available'] = type(r.report()) is dict
        elif case_id == 'AD39':
            inputs['expectation']['sha256'] = _sha(b'further caller mutation after return')
            inputs['context'] = None
            observed['decision_input_pins_equal_frozen_original'] = _exact(decision.get('input_pins'), original_inputs)
        observed.update(extras)
        ctx.retain_report(case_id, decision)
    finally:
        if proxy is not None:
            proxy.clear_orphans()
    if proxy is not None:
        observed['all_native_handles_closed_once'] = proxy.accounting_ok()
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
    if any(function not in os.supports_dir_fd for function in
           (os.open, os.mkdir, os.stat, os.symlink, os.link, os.mkfifo)):
        raise HarnessRefusal('required dir_fd operation unsupported')
    if os.scandir not in os.supports_fd or os.link not in os.supports_follow_symlinks:
        raise HarnessRefusal('required scandir-fd or NOFOLLOW link unsupported')
    for flag in ('O_NOFOLLOW', 'O_NONBLOCK', 'O_DIRECTORY', 'O_EXCL', 'O_APPEND'):
        if not hasattr(os, flag):
            raise HarnessRefusal('required os flag missing')


def _emit(value, output_state, summary=False):
    data = _json_bytes(value)
    if len(data) > (MAX_SUMMARY if summary else MAX_CASE_LINE) or output_state['bytes'] + len(data) > MAX_STDOUT:
        raise HarnessBudgetExceeded('stdout bound')
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    output_state['bytes'] += len(data)


def _emit_case(case, status, observed, elapsed, ctx, output_state):
    value = {'format': 'beta-consumer-control-case-v2', 'id': case['id'], 'type': case['type'],
             'status': status, 'qualification': 'NOT_QUALIFIED', 'elapsed_s': round(elapsed, 6),
             'expected_sha256': _sha(_json_bytes(case.get('expected', case.get('expected_when_available')))),
             'observed': observed}
    if len(_json_bytes(value)) > MAX_CASE_LINE:
        detail = _json_bytes(value)
        if len(detail) > MAX_DETAIL:
            raise HarnessBudgetExceeded('case detail cap')
        rec = ctx.reports.write(case['id'] + '-output.json', detail)
        value['observed'] = {'retained_detail': _ref(rec), 'bytes': len(detail)}
    _emit(value, output_state)


def run():
    start, owned, output_state, ctx = time.monotonic(), _Owned(), {'bytes': 0}, None
    deadline = start + 300.0
    def check():
        if time.monotonic() > deadline:
            raise HarnessDeadlineExceeded('original300s deadline exceeded')
    loader = None
    try:
        if len(sys.argv) != 1 or sys.flags.isolated != 1 or sys.flags.dont_write_bytecode != 1:
            raise HarnessRefusal('no arguments; -I -B required')
        _capabilities()
        try:
            os.lstat(ROOT)
        except FileNotFoundError:
            pass
        else:
            raise HarnessRefusal('evidence root already exists')
        reader_path, reader_sha = PINS['reader']
        reader_source = _bootstrap_read(reader_path, 1 << 20, owned, check)
        if owned.errors:
            raise HarnessRefusal('bootstrap harness descriptor uncertainty')
        reader_ns = _load_verified(reader_source, reader_path, reader_sha, 'beta_controls_real_reader')
        loader = reader_ns['EvidenceReader'](check)
        sources, namespaces, input_metadata = {'reader': reader_source}, {'reader': reader_ns}, {}
        for key, (path, digest) in PINS.items():
            if key == 'reader':
                continue
            data = loader.read_bytes(path, 1 << 20)
            if _sha(data) != digest:
                raise HarnessRefusal('input pin mismatch: ' + key)
            sources[key] = data
            input_metadata[key] = loader.last_file(path)['after']
            if key in ('capture4', 'schema2', 'adapter3'):
                namespaces[key] = _load_verified(data, path, digest, 'beta_controls_' + key)
            check()
        plan_bytes = loader.read_bytes(PLAN_PATH, 1 << 20)
        if _sha(plan_bytes) != PLAN_SHA:
            raise HarnessRefusal('operative plan pin mismatch')
        plan = _parse(plan_bytes)
        deferred_ids = tuple('DF' + str(i).zfill(2) for i in range(1, 16)) + tuple(
            'DP' + str(i).zfill(2) for i in range(24)) + ('DL01',)
        expected_ids = RD_IDS + CA_IDS + SC_IDS + AD_IDS + deferred_ids
        cases = plan['cases']
        if plan.get('format') != 'beta-consumer-controls-plan-v3' or type(cases) is not list:
            raise HarnessRefusal('operative plan format')
        if tuple(case['id'] for case in cases) != expected_ids:
            raise HarnessRefusal('frozen plan/harness case order mismatch')
        if len(cases) * MAX_CASE_LINE + MAX_SUMMARY > MAX_STDOUT:
            raise HarnessRefusal('worst-case stdout exceeds cap')
        for case in cases:
            deferred = case['id'] in deferred_ids
            if deferred != case['type'].startswith('DEFERRED_'):
                raise HarnessRefusal('deferred case/type mismatch')
            if not deferred and type(case.get('expected')) is not dict:
                raise HarnessRefusal('case missing frozen expectation')
            if deferred and not all(key in case for key in
                                    ('expected_when_available', 'missing_genuine_artifact', 'unreachable_entrypoint', 'prerequisites')):
                raise HarnessRefusal('deferred prerequisite/entrypoint missing')
        if tuple(_parse(sources['mols39_plan_v5'])['order']) != ORDER:
            raise HarnessRefusal('pinned MOLS plan order mismatch')
        if loader.report()['unresolved'] or owned.errors:
            raise HarnessRefusal('loader ownership uncertainty')
        check()
        ctx = _Context(owned, check, sources, namespaces, input_metadata)
        _create_root(ctx)
        if owned.errors:
            raise HarnessRefusal('harness root ownership uncertainty')
        protected_before = _protected_state()
        ctx.root.write('run-start.json', _json_bytes({
            'format': 'beta-negative-controls-run-start-v2', 'plan_sha256': PLAN_SHA,
            'pins': {key: {'path': value[0], 'sha256': value[1]} for key, value in PINS.items()},
            'interpreter': sys.executable, 'protected_before': protected_before,
            'qualification': 'NOT_QUALIFIED', 'authority': 'NEGATIVE_BOUNDARY_EVIDENCE_ONLY'}))
    except Exception as exc:
        owned.close_since(0)
        code = 5 if isinstance(exc, HarnessDeadlineExceeded) else 7
        _emit({'format': 'beta-consumer-controls-summary-v2', 'status': 'REFUSED_BEFORE_CASES',
               'exit_code': code, 'exception_type': type(exc).__name__, 'diagnostic': str(exc),
               'harness_close_errors': owned.errors, 'qualification': 'NOT_QUALIFIED'}, output_state, summary=True)
        return code
    except BaseException as exc:
        retained = None
        if loader is not None:
            try:
                retained = loader.report()
            except Exception as report_exc:
                retained = {'report_unavailable': type(report_exc).__name__}
        _emit({'format': 'beta-consumer-controls-summary-v2', 'status': 'BOOTSTRAP_BASE_EXCEPTION',
               'exception_type': type(exc).__name__, 'reader_state': _state(retained),
               'qualification': 'NOT_QUALIFIED'}, output_state, summary=True)
        owned.close_since(0)
        raise
    counts, stop = {}, None
    try:
        for case in cases:
            case_start, mark = time.monotonic(), len(owned.rows)
            status, observed = None, None
            if case['type'].startswith('DEFERRED_'):
                status, observed = 'DEFERRED_NOT_EXECUTED', {'executed': False,
                    'missing_genuine_artifact': case['missing_genuine_artifact'],
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
                    check()
                    if ctx.budget_latched:
                        raise HarnessBudgetExceeded('retained budget latched')
                    status = 'MATCH' if _exact(observed, case['expected']) else 'MISMATCH'
                except InconclusivePrecondition as exc:
                    status, observed = 'INCONCLUSIVE_PRECONDITION', {'rule': str(exc)}
                except HarnessDeadlineExceeded as exc:
                    stop = status = 'NOT_RUN_DEADLINE'
                    observed = {'case_started': True, 'exception_type': type(exc).__name__}
                except HarnessBudgetExceeded as exc:
                    stop = status = 'NOT_RUN_BUDGET'
                    observed = {'case_started': True, 'exception_type': type(exc).__name__}
                except Exception as exc:
                    status, observed = 'ERROR', {'exception_type': type(exc).__name__, 'diagnostic': str(exc)}
                except BaseException as exc:
                    retained = None
                    if ctx.last_reader is not None:
                        ctx.retained_exception_readers.append(ctx.last_reader)
                        try:
                            retained = ctx.last_reader.report()
                            ctx.retain_report(case['id'] + '-base-exception', retained)
                        except Exception as report_exc:
                            retained = {'report_unavailable': type(report_exc).__name__}
                    # Compact emergency line; no detail allocation may replace the
                    # module's BaseException. Cleanup also cannot replace it.
                    try:
                        _emit({'format': 'beta-consumer-control-case-v2', 'id': case['id'], 'type': case['type'],
                               'status': 'BASE_EXCEPTION', 'exception_type': type(exc).__name__,
                               'reader_state': _state(retained), 'qualification': 'NOT_QUALIFIED'}, output_state)
                    finally:
                        owned.close_since(mark)
                    raise
                finally:
                    cleanup_exc = owned.close_since(mark)
                if cleanup_exc is not None:
                    status = 'ERROR'
                    observed = {'harness_ownership_uncertainty': type(cleanup_exc).__name__}
            try:
                _emit_case(case, status, observed, time.monotonic() - case_start, ctx, output_state)
            except HarnessBudgetExceeded:
                stop = status = 'NOT_RUN_BUDGET'
                _emit_case(case, status, {'case_output_unretained': True}, time.monotonic() - case_start, ctx, output_state)
            counts[status] = counts.get(status, 0) + 1
            if time.monotonic() > deadline:
                stop = 'NOT_RUN_DEADLINE'
        protected_after = _protected_state()
        unchanged = _exact(protected_before, protected_after)
        if stop == 'NOT_RUN_DEADLINE':
            code = 5
        elif stop == 'NOT_RUN_BUDGET':
            code = 6
        elif counts.get('MISMATCH', 0) or counts.get('ERROR', 0) or not unchanged or owned.errors:
            code = 3
        elif counts.get('INCONCLUSIVE_PRECONDITION', 0):
            code = 4
        else:
            code = 0
        summary = {'format': 'beta-consumer-controls-summary-v2', 'exit_code': code,
                   'status': 'NEGATIVE_BOUNDARY_MATCHED_NOT_QUALIFIED' if code == 0 else 'NONZERO_NOT_QUALIFIED',
                   'counts': counts, 'plan_sha256': PLAN_SHA, 'qualification': 'NOT_QUALIFIED',
                   'mandatory_deferred_obligations_waived': False, 'protected_unchanged': unchanged,
                   'protected_after': protected_after, 'elapsed_s': round(time.monotonic() - start, 6),
                   'retained_bytes_before_summary': ctx.retained, 'stdout_bytes_before_summary': output_state['bytes'],
                   'evidence_root': ROOT, 'canonical_audit_written': False, 'release_authority': False,
                   'runtime_authority': False, 'scientific_authority': False}
        try:
            ctx.root.write('run-summary.json', _json_bytes({**summary, 'phase': 'PRE_FINAL_HARNESS_CLOSE_PROVISIONAL'}))
        except HarnessBudgetExceeded:
            code = 6
            summary.update(exit_code=6, status='RETAINED_BUDGET_NOT_QUALIFIED', summary_file_written=False)
        owned.close_since(0)
        if owned.errors:
            code = 3
            summary.update(exit_code=3, status='HARNESS_CLOSE_UNCERTAINTY_NOT_QUALIFIED', harness_close_errors=owned.errors)
        summary['phase'] = 'FINAL_AFTER_HARNESS_CLOSE'
        _emit(summary, output_state, summary=True)
        return code
    finally:
        owned.close_since(0)


if __name__ == '__main__':
    sys.exit(run())
