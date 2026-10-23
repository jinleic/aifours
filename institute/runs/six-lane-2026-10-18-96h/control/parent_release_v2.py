"""SOURCE ONLY, UNTESTED. Independent parent five-part release transaction v2.

Base contract 4d122872; repair scope 2fdf13b4; design checkpoints001-003 govern.
Definitions only at import: no I/O, environment, clock, process or signal operations.
The parent supplies a qualified raw adapter, authentic authority/execution observations,
exclusive immutable publication freeze and COMPLETE historical identity-union binding.
No file/registry syntax alone is completed release authority: caller MUST observe return
state RELEASED after ACK and the final original deadline. CP1/CP2 are external prerequisites.
Caps bound bytes/memory, NOT synchronous syscall time. A detected original-deadline crossing
starts no further callback/I/O; only cleanup of already-owned descriptors remains permitted.
V1 stays immutable/self-HOLD. No v1 import, alias, baseline compatibility path or shim.
"""
import copy
import datetime
import hashlib
import json
import math
import os
import stat

CONTRACT_SHA256 = '4d12287257f8bf74d9057a796a0c6f7a391387c411b95d5dcda1131aa4692d3e'
REPAIR_SCOPE_SHA256 = '2fdf13b45e946df4f07881b0e6e2b5bc5452ea33d1df022afe896dded698b407'
AIFOURS_ROOT = '/Users/jinleic/repos/aifours'
RUN_ROOT = AIFOURS_ROOT + '/institute/runs/six-lane-2026-10-18-96h'
CAP = 16 << 20
DOC_CAP = 1 << 20
SPEC_CAP = 4 << 20
EMBED_CAP = 256 << 10
DECISION_CAP = 1 << 20
MAX_SPEC_NODES = 131072
MAX_JOB_ENTRIES = 4096
MAX_TREE_ENTRIES = 200000
MAX_TREE_DEPTH = 64
MAX_OPEN_CALLS = 1000000
MAX_READ_LOG = 256
MAX_CALLBACK_LOG = 128
MAX_EVIDENCE = 16
MAX_TEXT = 512
CHUNK = 65536
MAX_LATE_FILE_BYTES = 16 << 30
MAX_LATE_HASH_BYTES = 128 << 30
FREE_FLOOR = 12200000000
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_NONBLOCK
FILE_FLAGS = os.O_NOFOLLOW | os.O_NONBLOCK | getattr(os, 'O_CLOEXEC', 0)
SPEC_KEYS = frozenset(('item', 'go', 'allocation', 'gate', 'launch', 'exit', 'captures',
                       'publication', 'artifacts', 'oracle', 'identities', 'late_audit',
                       'reservation', 'exit_table'))
ROLES = frozenset(('driver', 'main_child', 'helper', 'descendant', 'unproved',
                   'oracle', 'oracle_child', 'oracle_helper'))
KINDS = frozenset(('file', 'dir', 'symlink', 'fifo', 'socket', 'device', 'other'))
ENTRY_KEYS = frozenset(('kind', 'dev', 'ino', 'mode', 'nlink', 'bytes', 'allocated_bytes',
                        'mtime_ns', 'ctime_ns', 'sha256'))
CAUSES = (
    'P1_SPEC_INVALID', 'P1_CALLBACKS_INVALID', 'P1_ITEM_INVALID', 'P1_GO_INVALID',
    'P1_LAUNCH_INVALID', 'P1_GO_LAUNCH_MISMATCH', 'P1_LAUNCH_IDENTITY', 'P1_GATE_INVALID',
    'P1_GATE_NOT_BEFORE_LAUNCH', 'P1_EXIT_TABLE_INVALID', 'P1_RESERVATION_INVALID',
    'P1_ALLOCATION_INVALID', 'P1_ALLOCATION_BINDING', 'P1_ALLOCATION_NOT_CURRENT',
    'P1_DEADLINE', 'P1_INTERNAL_ERROR', 'P1_BASE_EXCEPTION',
    'P2_EXIT_INVALID', 'P2_CAPTURE_STDOUT_INVALID', 'P2_CAPTURE_STDERR_INVALID',
    'P2_PUBLICATION_INVALID', 'P2_PUBLICATION_EXIT_INCONSISTENT', 'P2_ARTIFACTS_INVALID',
    'P2_ARTIFACT_SET_MISMATCH', 'P2_ARTIFACT_IDENTITY', 'P2_ARTIFACT_DIGEST',
    'P2_DEADLINE', 'P2_INTERNAL_ERROR', 'P2_BASE_EXCEPTION',
    'P3_ORACLE_INVALID', 'P3_ORACLE_GO_INVALID', 'P3_ORACLE_EXIT',
    'P3_ORACLE_CAPTURE_INVALID', 'P3_ORACLE_VERDICT', 'P3_ORACLE_BINDING',
    'P3_DEADLINE', 'P3_INTERNAL_ERROR', 'P3_BASE_EXCEPTION',
    'P4_IDENTITIES_INVALID', 'P4_ORACLE_IDENTITIES_MISSING', 'P4_CENSUS_FAILED',
    'P4_CENSUS_INCOMPLETE', 'P4_CENSUS_STALE', 'P4_IDENTITY_ALIVE',
    'P4_PID_REUSE_AMBIGUOUS', 'P4_OWNED_GROUP_NONEMPTY', 'P4_OWNED_DESCENDANT',
    'P4_DEADLINE', 'P4_INTERNAL_ERROR', 'P4_BASE_EXCEPTION',
    'P5_LATE_AUDIT_INVALID', 'P5_LATE_CENSUS_INCOMPLETE', 'P5_ACCOUNTING_UNAVAILABLE',
    'P5_LATE_UNDECLARED_NEW', 'P5_LATE_UNDECLARED_CHANGED', 'P5_LATE_UNDECLARED_REMOVED',
    'P5_FREE_BYTES_LOW', 'P5_OWNED_DATE_FAILED', 'P5_COMMIT_DIR_INVALID',
    'P5_DECISION_TOO_LARGE', 'P5_DEADLINE', 'P5_INTERNAL_ERROR', 'P5_BASE_EXCEPTION',
    'P5_COMMIT_WRITE_FAILED', 'P5_ACK_FAILED', 'P5_DEADLINE_AFTER_ACK',
    'P5_REGISTRY_APPEND_FAILED')
IDENTITY_NOTE = ('Endedness is conditional on the parent-authenticated COMPLETE historical identity '
                 'union. Supplied identities and a current pid/ppid census cannot prove no omitted, '
                 'escaped or reparented incarnation. CP2 raw-adapter/parent binding remains required.')
RELEASE_EFFECT = ('This file and a RELEASED registry line are not completed authority. Effective '
                  'release requires ACK_OK and the caller observing decide_and_commit return state '
                  'RELEASED after registry write/fsync/close and the final ORIGINAL deadline check. '
                  'CP1 caller receipt remains an external integration prerequisite, not implemented here.')
BOUNDARY = ('Reservation release only under trusted-parent preconditions; no next admission, '
            'runtime authority, scientific PASS, publication authority or raw supervisor acceptance.')


class ReleaseRefusal(ValueError):
    """Typed bounded refusal; it can never certify a release."""


class AccountingRefusal(ReleaseRefusal):
    """Actual logical/allocated accounting unavailable; never substitute zero."""


class _Crossed(Exception):
    """Internal unwind after the original deadline has become unavailable."""


def _require(condition, message):
    if not condition:
        raise ReleaseRefusal(message)


def _short(text):
    return text[:MAX_TEXT] if len(text) > MAX_TEXT else text


def _why(exc):
    try:
        text = type(exc).__name__ + ': ' + str(exc)
    except BaseException:
        text = type(exc).__name__ + ': <description unavailable>'
    return _short(text)


def _text(value, maximum=MAX_TEXT):
    _require(type(value) is str and 0 < len(value) <= maximum
             and '\x00' not in value and '\n' not in value and '\r' not in value, 'text type/length')
    return value


def _integer(value, positive=False):
    _require(type(value) is int and value >= (1 if positive else 0), 'exact nonnegative integer required')
    return value


def _hex(value):
    return type(value) is str and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def _parts(path):
    _require(type(path) is str and path.startswith('/') and 1 < len(path) <= 4096
             and '\x00' not in path, 'normalized absolute path required')
    parts = path.split('/')[1:]
    _require(len(parts) <= 128 and all(p not in ('', '.', '..') for p in parts), 'path components')
    return parts


def _mutation_parts(path):
    parts = _parts(path)
    _require(path == AIFOURS_ROOT or path.startswith(AIFOURS_ROOT + '/'), 'mutation target outside aifours')
    return parts


def _name(name):
    _text(name, 255)
    _require(name not in ('.', '..') and '/' not in name, 'plain name required')
    return name


def _keys(value, wanted):
    _require(type(value) is dict and all(type(k) is str for k in value)
             and set(value) == set(wanted), 'exact object keys required: ' + ','.join(sorted(wanted)))


def _exact(left, right):
    stack = [(left, right)]
    while stack:
        a, b = stack.pop()
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            if not all(type(k) is str for k in a) or not all(type(k) is str for k in b) or set(a) != set(b):
                return False
            stack.extend((a[k], b[k]) for k in a)
        elif type(a) is list:
            if len(a) != len(b):
                return False
            stack.extend(zip(a, b))
        elif type(a) not in (str, int, float, bool, type(None)) or a != b:
            return False
    return True


def _canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       separators=(',', ':')) + '\n').encode('ascii')


def _json(data):
    def pairs(rows):
        result = {}
        for key, value in rows:
            _require(key not in result, 'duplicate JSON key')
            result[key] = value
        return result
    def bad(_):
        raise ReleaseRefusal('nonfinite JSON number')
    def floating(text):
        value = float(text)
        _require(math.isfinite(value), 'nonfinite JSON float')
        return value
    _require(type(data) is bytes and len(data) <= CAP, 'JSON bytes/cap')
    return json.loads(data.decode('utf-8'), object_pairs_hook=pairs,
                      parse_constant=bad, parse_float=floating)


def _preflight(value):
    """Bound JSON-shaped in-memory spec before serialization/copy; no recursive comparison."""
    stack, active, nodes, cost = [(value, False)], set(), 0, 1
    while stack:
        current, leaving = stack.pop()
        if leaving:
            active.remove(id(current))
            continue
        nodes += 1
        _require(nodes <= MAX_SPEC_NODES, 'spec node cap')
        kind = type(current)
        if kind in (dict, list):
            _require(id(current) not in active, 'cyclic spec')
            _require(len(current) <= MAX_SPEC_NODES and len(stack) + 2 * len(current) <= 2 * MAX_SPEC_NODES,
                     'spec container cap')
            active.add(id(current))
            stack.append((current, True))
            cost += 2 + max(0, len(current) - 1)
            if kind is dict:
                cost += len(current)
                for key, entry in current.items():
                    _require(type(key) is str, 'spec keys must be strings')
                    stack.append((key, False))
                    stack.append((entry, False))
            else:
                stack.extend((entry, False) for entry in current)
        elif kind is str:
            _require(len(current) <= SPEC_CAP, 'spec string cap')
            cost += 2
            for char in current:
                number = ord(char)
                cost += 2 if char in ('"', '\\', '\b', '\f', '\n', '\r', '\t') else 6 if number < 32 or 126 < number <= 65535 else 12 if number > 65535 else 1
                _require(cost <= SPEC_CAP, 'spec encoded byte cap')
        elif kind is int:
            _require(current.bit_length() <= 4096, 'spec integer representation cap')
            cost += len(str(current))
        elif kind is float:
            _require(math.isfinite(current), 'nonfinite spec float')
            cost += len(repr(current))
        elif kind is bool:
            cost += 4 if current else 5
        elif current is None:
            cost += 4
        else:
            raise ReleaseRefusal('spec contains non-JSON exact type')
        _require(cost <= SPEC_CAP, 'spec encoded byte cap')


def _date_value(text):
    _require(type(text) is str and len(text) == 24, 'date must be /bin/date 24-char text')
    pattern = 'dddd-dd-ddTdd:dd:dd+dddd'
    for char, expected in zip(text, pattern):
        _require(('0' <= char <= '9') if expected == 'd' else
                 (char in ('+', '-')) if expected == '+' else char == expected, 'date shape')
    hours, minutes = int(text[20:22]), int(text[22:24])
    _require(hours <= 23 and minutes <= 59, 'date timezone range')
    delta = datetime.timedelta(hours=hours, minutes=minutes)
    if text[19] == '-':
        delta = -delta
    return datetime.datetime(int(text[:4]), int(text[5:7]), int(text[8:10]),
                             int(text[11:13]), int(text[14:16]), int(text[17:19]),
                             tzinfo=datetime.timezone(delta))


def _stat_key(info):
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink, info.st_size,
            info.st_mtime_ns, info.st_ctime_ns, getattr(info, 'st_blocks', None))


class _Txn:
    def __init__(self, read_bytes, census, owned_date, deadline_check):
        self.callbacks = {'read_bytes': read_bytes, 'census': census,
                          'owned_date': owned_date, 'deadline_check': deadline_check}
        self.fired, self.evidence, self.suppressed = set(), {}, {}
        self.part, self.crossed, self.ack_done = 1, False, False
        self.unsafe, self.evaluated, self.blocked = set(), set(), set()
        self.read_count, self.read_log = 0, []
        self.read_digest = hashlib.sha256()
        self.callback_count, self.callback_log = 0, []
        self.callback_digest = hashlib.sha256()
        self.opened, self.closed, self.live, self.unresolved = 0, 0, {}, []
        self.streamed_bytes, self.hashed_files = 0, 0

    def fire(self, cause, detail):
        if cause not in CAUSES:
            cause = 'P%d_INTERNAL_ERROR' % self.part
        self.fired.add(cause)
        values = self.evidence.setdefault(cause, [])
        if len(values) < MAX_EVIDENCE:
            values.append(_short(detail))
        else:
            self.suppressed[cause] = self.suppressed.get(cause, 0) + 1

    def event(self, name, state, detail):
        row = {'callback': name, 'state': state, 'detail': _short(detail)}
        self.callback_count += 1
        self.callback_digest.update(_canonical(row))
        if len(self.callback_log) < MAX_CALLBACK_LOG:
            self.callback_log.append(row)

    def call(self, name, *args):
        function = self.callbacks[name]
        _require(callable(function), name + ' must be callable')
        try:
            return function(*args)
        except BaseException as exc:
            if not isinstance(exc, Exception):
                self.unsafe.add(name)
            raise

    def tick(self, stage, after_ack=False):
        if self.crossed:
            return False
        try:
            _require(self.call('deadline_check') is None, 'deadline_check returned non-None')
        except Exception as exc:
            self.crossed = True
            self.event('deadline_check', 'EXCEPTION_OR_BAD_RETURN', stage + ': ' + _why(exc))
            cause = 'P5_DEADLINE_AFTER_ACK' if after_ack or self.ack_done else 'P%d_DEADLINE' % self.part
            self.fire(cause, stage + ': ' + _why(exc))
            return False
        except BaseException as exc:
            self.event('deadline_check', 'BASE_EXCEPTION', stage + ': ' + _why(exc))
            raise
        return True

    def must_tick(self, stage):
        if not self.tick(stage):
            raise _Crossed(stage)

    def observe(self, name, *args, after_ack=False):
        """Every blocking callback success/Exception is followed by the SAME original check.

        Primary error retained before the check; secondary deadline error is separate. A secondary
        BaseException propagates with the primary as context. Unsafe BaseException is never retried.
        """
        if self.crossed:
            raise _Crossed('no callback after original deadline crossing')
        try:
            value = self.call(name, *args)
        except Exception as primary:
            self.event(name, 'EXCEPTION', _why(primary))
            try:
                self.tick(name + ' Exception completion', after_ack)
            except BaseException as secondary:
                if secondary is not primary and secondary.__context__ is None:
                    secondary.__context__ = primary
                raise
            raise  # primary preserved even when the original deadline also crossed
        except BaseException as primary:
            self.event(name, 'BASE_EXCEPTION', _why(primary))
            raise
        self.event(name, 'RETURNED', type(value).__name__)
        self.tick(name + ' successful completion', after_ack)
        return value

    def read(self, path, cap):
        data = self.observe('read_bytes', path, cap)
        row = {'path': path, 'cap': cap, 'type': type(data).__name__, 'late': self.crossed}
        if type(data) is bytes and len(data) <= cap:
            row.update({'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        self.read_count += 1
        self.read_digest.update(_canonical(row))
        if len(self.read_log) < MAX_READ_LOG:
            self.read_log.append(row)
        if self.crossed:
            raise _Crossed('late read retained in bounded observation log')
        _require(type(data) is bytes and len(data) <= cap, 'read_bytes wrong type or over cap')
        return data

    def open(self, path, flags, mode=0o444, parent=None, display=None):
        self.must_tick('before descriptor acquisition')
        _require(self.opened < MAX_OPEN_CALLS, 'descriptor acquisition cap')
        fd = os.open(path, flags, mode) if parent is None else os.open(path, flags, mode, dir_fd=parent)
        self.opened += 1
        self.live[fd] = display if display is not None else path
        try:
            self.must_tick('descriptor acquisition completion')
        except BaseException:
            self.close(fd, 'P%d_INTERNAL_ERROR' % self.part)
            raise
        return fd

    def close(self, fd, cause):
        if fd not in self.live:
            return True
        path = self.live.pop(fd)
        try:
            os.close(fd)
        except BaseException as exc:
            if len(self.unresolved) < 64:
                self.unresolved.append({'fd': fd, 'path': path, 'error': _why(exc)})
            if cause is not None:
                self.fire(cause, 'unresolved close ' + _short(path) + ': ' + _why(exc))
            if not isinstance(exc, Exception):
                raise
            return False
        self.closed += 1
        return True

    def directory(self, parts, cause):
        fd = self.open('/', DIR_FLAGS, display='/')
        location = ''
        try:
            for part in parts:
                location += '/' + part
                nxt = self.open(part, DIR_FLAGS, parent=fd, display=location)
                previous, fd = fd, nxt
                self.close(previous, cause)
            return fd
        except BaseException:
            self.close(fd, cause)
            raise


class _Ctx:
    def __init__(self):
        self.f, self.driver, self.commit_dir = {}, None, None
        self.spec_sha, self.spec_bytes, self.spec_embed = None, None, None
        self.registry, self.census, self.late = None, None, None
        self.date_text, self.date_child = None, None


def _need(txn, ctx, *names):
    if any(name not in ctx.f for name in names):
        txn.blocked.add(txn.part)
        return False
    return True


def _guard(txn, cause, function, *args):
    try:
        return function(*args)
    except _Crossed:
        raise
    except Exception as exc:
        txn.fire('P5_ACCOUNTING_UNAVAILABLE' if isinstance(exc, AccountingRefusal) else cause, _why(exc))
        if txn.crossed:
            raise _Crossed('callback primary retained; deadline also failed') from exc
        return None


def _v_ref(value):
    _keys(value, ('path', 'sha256'))
    _parts(value['path'])
    _require(_hex(value['sha256']), 'lowercase 64-hex digest required')
    return dict(value)


def _v_reservation(value):
    _keys(value, ('bytes', 'cpu_slots'))
    _integer(value['bytes'])
    _integer(value['cpu_slots'])
    return dict(value)


def _v_exit_table(value):
    _require(type(value) is list, 'exit_table list required')
    seen, result = set(), []
    for row in value:
        _keys(row, ('actual_exit', 'state'))
        _require(type(row['actual_exit']) is int, 'exit_table exact integer exit')
        _text(row['state'])
        _require(row['actual_exit'] not in seen, 'duplicate exit_table row')
        seen.add(row['actual_exit'])
        result.append(dict(row))
    return result


def _v_allocation(value):
    _keys(value, ('registry_path', 'line_sha256', 'record'))
    _mutation_parts(value['registry_path'])
    _require(_hex(value['line_sha256']), 'registry line digest')
    rec = value['record']
    _require(type(rec) is dict and all(type(k) is str for k in rec), 'allocation record object')
    _require(rec.get('state') == 'RUNNING', 'allocation record state RUNNING required')
    _text(rec.get('item'))
    _text(rec.get('abs_end'))
    _integer(rec.get('reservation_bytes'))
    _integer(rec.get('driver_pid'), True)
    _integer(rec.get('driver_pgid'), True)
    _require(_hex(rec.get('go_sha256')) and _hex(rec.get('launch_record_sha256')), 'allocation GO/launch pins')
    return copy.deepcopy(value)


def _v_exit(value):
    _keys(value, ('actual_exit', 'observed_by', 'wait_record'))
    _require(type(value['actual_exit']) is int and value['observed_by'] == 'parent', 'parent-observed exact exit')
    return {'actual_exit': value['actual_exit'], 'observed_by': 'parent', 'wait_record': _v_ref(value['wait_record'])}


def _v_capture(value):
    _keys(value, ('path', 'sha256', 'bytes_seen', 'bytes_stored', 'eof', 'overflow', 'error'))
    _parts(value['path'])
    _require(_hex(value['sha256']), 'capture digest')
    _integer(value['bytes_seen'])
    _integer(value['bytes_stored'])
    _require(value['bytes_seen'] == value['bytes_stored'] <= CAP and value['eof'] is True
             and value['overflow'] is False and value['error'] is None, 'complete capture required')
    return dict(value)


def _v_publication(value):
    _keys(value, ('path', 'sha256', 'expected_state'))
    _v_ref({k: value[k] for k in ('path', 'sha256')})
    _text(value['expected_state'])
    return dict(value)


def _v_artifacts(value):
    _keys(value, ('job_dir', 'declared'))
    _parts(value['job_dir'])
    _require(type(value['declared']) is dict and len(value['declared']) <= MAX_JOB_ENTRIES, 'artifact map/count')
    declared = {}
    for name, row in value['declared'].items():
        _name(name)
        _keys(row, ('sha256', 'bytes'))
        _require(_hex(row['sha256']), 'artifact digest')
        _integer(row['bytes'])
        _require(row['bytes'] <= CAP, 'part2 artifact > reader16MiB cap needs separate streaming interface')
        declared[name] = dict(row)
    return {'job_dir': value['job_dir'], 'declared': declared}


def _v_identities(value):
    _require(type(value) is list and 0 < len(value) <= MAX_TREE_ENTRIES, 'nonempty bounded identity union')
    seen, result, drivers = set(), [], 0
    for row in value:
        _keys(row, ('role', 'pid', 'pgid', 'start_fingerprint', 'source'))
        _require(type(row['role']) is str and row['role'] in ROLES, 'identity role')
        _integer(row['pid'], True)
        _integer(row['pgid'], True)
        _text(row['start_fingerprint'])
        _text(row['source'])
        key = (row['pid'], row['start_fingerprint'])
        _require(key not in seen, 'duplicate identity incarnation')
        seen.add(key)
        drivers += int(row['role'] == 'driver')
        result.append(dict(row))
    _require(drivers == 1, 'exactly one driver identity; driver always applicable')
    return result


def _roots(value):
    _require(type(value) is list and value, 'nonempty roots list')
    result = list(value)
    for root in result:
        _parts(root)
    _require(len(result) == len(set(result)), 'duplicate late roots')
    _require(RUN_ROOT in result, 'fresh whole-RUN root must be present (not a narrowed subdirectory)')
    return result


def _v_late(value):
    _keys(value, ('roots', 'baseline_manifest', 'allowed_new'))
    roots = _roots(value['roots'])
    _require(type(value['allowed_new']) is list, 'allowed_new list')
    allowed = list(value['allowed_new'])
    for entry in allowed:
        _require(type(entry) is str, 'allowed_new string')
        _parts(entry) if entry.startswith('/') else _name(entry)
    return {'roots': roots, 'baseline_manifest': _v_ref(value['baseline_manifest']), 'allowed_new': allowed}


def _v_digests(value):
    _require(type(value) is dict and len(value) <= MAX_JOB_ENTRIES, 'bound artifact digest map')
    for name, digest in value.items():
        _name(name)
        _require(_hex(digest), 'bound artifact digest')
    return dict(value)


def _shape_field(txn, ctx, source, key, target, cause, validator):
    try:
        _require(key in source, 'missing ' + key)
        ctx.f[target] = validator(source[key])
    except Exception as exc:
        txn.fire(cause, key + ': ' + _why(exc))


def _shape_captures(txn, ctx, source, prefix, cause_stdout, cause_stderr):
    if type(source) is not dict or set(source) != {'stdout', 'stderr'}:
        txn.fire(cause_stdout, prefix + ' capture keys')
        txn.fire(cause_stderr, prefix + ' capture keys')
    source = source if type(source) is dict else {}
    for stream, cause in (('stdout', cause_stdout), ('stderr', cause_stderr)):
        _shape_field(txn, ctx, source, stream, prefix + '.' + stream, cause, _v_capture)
    first, second = prefix + '.stdout', prefix + '.stderr'
    if first in ctx.f and second in ctx.f and ctx.f[first]['path'] == ctx.f[second]['path']:
        txn.fire(cause_stderr, prefix + ' stdout/stderr must be independent capture paths')
        del ctx.f[second]


def _shape(txn, ctx, spec, commit_dir):
    for name, function in txn.callbacks.items():
        if not callable(function):
            txn.fire('P1_CALLBACKS_INVALID', name + ' not callable')
    try:
        _mutation_parts(commit_dir)
        ctx.commit_dir = commit_dir
    except Exception as exc:
        txn.fire('P5_COMMIT_DIR_INVALID', _why(exc))
    source = {}
    try:
        _preflight(spec)
        raw = _canonical(spec)
        _require(len(raw) <= SPEC_CAP, 'spec byte cap')
        ctx.spec_bytes, ctx.spec_sha = len(raw), hashlib.sha256(raw).hexdigest()
        source = _json(raw)
        _require(type(source) is dict and set(source) == SPEC_KEYS, 'exact fourteen spec keys')
        if len(raw) <= EMBED_CAP:
            ctx.spec_embed = source
    except Exception as exc:
        txn.fire('P1_SPEC_INVALID', _why(exc))
        source = source if type(source) is dict else {}
    fields = (('item', 'P1_ITEM_INVALID', _text), ('go', 'P1_GO_INVALID', _v_ref),
              ('allocation', 'P1_ALLOCATION_INVALID', _v_allocation), ('gate', 'P1_GATE_INVALID', _v_ref),
              ('launch', 'P1_LAUNCH_INVALID', _v_ref), ('exit', 'P2_EXIT_INVALID', _v_exit),
              ('publication', 'P2_PUBLICATION_INVALID', _v_publication), ('artifacts', 'P2_ARTIFACTS_INVALID', _v_artifacts),
              ('identities', 'P4_IDENTITIES_INVALID', _v_identities), ('late_audit', 'P5_LATE_AUDIT_INVALID', _v_late),
              ('reservation', 'P1_RESERVATION_INVALID', _v_reservation), ('exit_table', 'P1_EXIT_TABLE_INVALID', _v_exit_table))
    for key, cause, validator in fields:
        _shape_field(txn, ctx, source, key, key, cause, validator)
    _shape_captures(txn, ctx, source.get('captures'), 'captures', 'P2_CAPTURE_STDOUT_INVALID', 'P2_CAPTURE_STDERR_INVALID')
    oracle = source.get('oracle')
    wanted = {'go', 'actual_exit', 'captures', 'verdict_path', 'verdict', 'bound_artifact_digests', 'wait_record'}
    if type(oracle) is not dict or set(oracle) != wanted:
        txn.fire('P3_ORACLE_INVALID', 'oracle keys (including parent wait_record)')
    oracle = oracle if type(oracle) is dict else {}
    for key, cause, validator in (('go', 'P3_ORACLE_GO_INVALID', _v_ref),
                                   ('wait_record', 'P3_ORACLE_EXIT', _v_ref),
                                   ('verdict_path', 'P3_ORACLE_VERDICT', _v_ref),
                                   ('bound_artifact_digests', 'P3_ORACLE_BINDING', _v_digests)):
        _shape_field(txn, ctx, oracle, key, 'oracle.' + key, cause, validator)
    _shape_field(txn, ctx, oracle, 'actual_exit', 'oracle.actual_exit', 'P3_ORACLE_EXIT',
                 lambda x: x if type(x) is int and x == 0 else (_require(False, 'oracle actual_exit exact int0')))
    _shape_field(txn, ctx, oracle, 'verdict', 'oracle.verdict', 'P3_ORACLE_VERDICT',
                 lambda x: x if type(x) is str and x == 'PASS' else (_require(False, 'oracle verdict PASS')))
    _shape_captures(txn, ctx, oracle.get('captures'), 'oracle.captures', 'P3_ORACLE_CAPTURE_INVALID', 'P3_ORACLE_CAPTURE_INVALID')
    if 'identities' in ctx.f:
        ctx.driver = next(row for row in ctx.f['identities'] if row['role'] == 'driver')
    if ctx.commit_dir is not None and 'artifacts' in ctx.f and ctx.commit_dir == ctx.f['artifacts']['job_dir']:
        txn.fire('P5_COMMIT_DIR_INVALID', 'commit_dir cannot be exact artifact directory')
        ctx.commit_dir = None


def _load(txn, ref, cap=DOC_CAP):
    data = txn.read(ref['path'], cap)
    _require(hashlib.sha256(data).hexdigest() == ref['sha256'], 'pinned byte digest mismatch')
    value = _json(data)
    _require(type(value) is dict, 'document object required')
    return value


def _argv(value):
    _require(type(value) is list and value, 'nonempty argv list')
    for entry in value:
        _text(entry, 4096)


def _pins(value):
    _require(type(value) is dict, 'pins object required (empty allowed)')
    for key, digest in value.items():
        _text(key, 4096)
        _require(_hex(digest), 'pin digest')


def _go_doc(txn, ctx):
    value = _load(txn, ctx.f['go'])
    _require(value.get('status') == 'PARENT_GO' and 'oracle_for' not in value, 'main PARENT_GO required')
    _require(_exact(value.get('item'), ctx.f['item']), 'GO item')
    _argv(value.get('argv'))
    _pins(value.get('pins'))
    _v_reservation(value.get('reservation'))
    _v_ref(value.get('gate'))
    _v_exit_table(value.get('exit_table'))
    return value


def _launch_doc(txn, ctx):
    value = _load(txn, ctx.f['launch'])
    _text(value.get('item'))
    _argv(value.get('argv'))
    _parts(value.get('cwd'))
    _require(_hex(value.get('env_sha256')), 'launch env digest')
    _pins(value.get('pins'))
    _v_reservation(value.get('reservation'))
    _date_value(value.get('started_at'))
    _v_ref(value.get('go'))
    _keys(value.get('driver'), ('pid', 'pgid', 'start_fingerprint'))
    _integer(value['driver']['pid'], True)
    _integer(value['driver']['pgid'], True)
    _text(value['driver']['start_fingerprint'])
    return value


def _go_launch(txn, ctx, go, launch):
    bad = [key for key in ('item', 'argv', 'pins', 'reservation') if not _exact(go.get(key), launch.get(key))]
    if not _exact(launch.get('go'), ctx.f['go']):
        bad.append('launch.go')
    _require(not bad, 'GO/launch mismatch: ' + ','.join(bad))


def _launch_identity(txn, ctx, launch):
    if not _need(txn, ctx, 'allocation', 'identities'):
        return
    record, actual = ctx.f['allocation']['record'], launch['driver']
    _require(actual['pid'] == record['driver_pid'] and actual['pgid'] == record['driver_pgid']
             and all(_exact(actual[k], ctx.driver[k]) for k in ('pid', 'pgid', 'start_fingerprint')),
             'launch/registry/driver identity mismatch')


def _gate_doc(txn, ctx):
    value = _load(txn, ctx.f['gate'])
    _require(value.get('verdict') == 'PASS' and _exact(value.get('reasons'), []), 'stability gate not PASS')
    _date_value(value.get('now_date'))
    return value


def _gate_order(txn, ctx, go, launch, gate):
    _require(_exact(go.get('gate'), ctx.f['gate']), 'GO did not cite exact prelaunch gate')
    _require(_date_value(gate['now_date']) <= _date_value(launch['started_at']), 'gate observed after launch')


def _held_for(row, item, allocation_sha):
    return (row.get('format') == 'parent-release-registry-v2' and row.get('state') == 'HELD'
            and _exact(row.get('item'), item) and row.get('allocation_line_sha256') == allocation_sha)


def _allocation(txn, ctx):
    ref = ctx.f['allocation']
    raw = txn.read(ref['registry_path'], CAP)
    _require(raw and raw.endswith(b'\n'), 'empty/torn registry')
    rows, matches = [], []
    for number, line in enumerate(raw[:-1].split(b'\n'), 1):
        try:
            row = _json(line)
            _require(type(row) is dict, 'registry line object')
        except Exception as exc:
            raise ReleaseRefusal('registry line %d: %s' % (number, _why(exc))) from exc
        rows.append(row)
        if hashlib.sha256(line).hexdigest() == ref['line_sha256']:
            matches.append(number - 1)
    _require(len(matches) == 1, 'allocation line digest must occur exactly once')
    index = matches[0]
    ctx.registry = {'path': ref['registry_path'], 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
                    'allocation_line': index + 1, 'allocation_line_sha256': ref['line_sha256']}
    if not _exact(rows[index], ref['record']):
        txn.fire('P1_ALLOCATION_INVALID', 'parsed allocation line not typed-equal spec.record')
    record = ref['record']
    if _need(txn, ctx, 'item', 'reservation', 'go', 'launch'):
        if (not _exact(record['item'], ctx.f['item']) or record['reservation_bytes'] != ctx.f['reservation']['bytes']
                or record['go_sha256'] != ctx.f['go']['sha256']
                or record['launch_record_sha256'] != ctx.f['launch']['sha256']):
            txn.fire('P1_ALLOCATION_BINDING', 'allocation item/reservation/GO/launch mismatch')
    for later in rows[index + 1:]:
        if _exact(later.get('item'), record['item']) and not _held_for(later, record['item'], ref['line_sha256']):
            txn.fire('P1_ALLOCATION_NOT_CURRENT', 'later non-v2-HELD/same-allocation entry for item')


def _part1(txn, ctx):
    go = _guard(txn, 'P1_GO_INVALID', _go_doc, txn, ctx) if _need(txn, ctx, 'go', 'item') else None
    launch = _guard(txn, 'P1_LAUNCH_INVALID', _launch_doc, txn, ctx) if _need(txn, ctx, 'launch') else None
    gate = _guard(txn, 'P1_GATE_INVALID', _gate_doc, txn, ctx) if _need(txn, ctx, 'gate') else None
    if go is not None and launch is not None:
        _guard(txn, 'P1_GO_LAUNCH_MISMATCH', _go_launch, txn, ctx, go, launch)
    if launch is not None:
        _guard(txn, 'P1_LAUNCH_IDENTITY', _launch_identity, txn, ctx, launch)
    if go is not None and launch is not None and gate is not None:
        _guard(txn, 'P1_GATE_NOT_BEFORE_LAUNCH', _gate_order, txn, ctx, go, launch, gate)
    if go is not None and _need(txn, ctx, 'exit_table') and not _exact(go.get('exit_table'), ctx.f['exit_table']):
        txn.fire('P1_EXIT_TABLE_INVALID', 'GO exit_table not typed-equal spec.exit_table')
    if go is not None and _need(txn, ctx, 'reservation') and not _exact(go.get('reservation'), ctx.f['reservation']):
        txn.fire('P1_RESERVATION_INVALID', 'GO reservation not typed-equal spec.reservation')
    if _need(txn, ctx, 'allocation'):
        _guard(txn, 'P1_ALLOCATION_INVALID', _allocation, txn, ctx)


def _wait(txn, ctx, ref, role, expected_exit):
    value = _load(txn, ref)
    _keys(value, ('format', 'item', 'role', 'pid', 'pgid', 'start_fingerprint',
                  'raw_status', 'actual_exit', 'observed_by'))
    _require(value['format'] == 'parent-release-wait-v1' and value['role'] == role
             and value['observed_by'] == 'parent', 'parent wait format/role/observer')
    _require(type(value['raw_status']) is int and value['raw_status'] >= 0
             and type(value['actual_exit']) is int and value['actual_exit'] == expected_exit,
             'parent wait status/exit type or value')
    _require(os.waitstatus_to_exitcode(value['raw_status']) == expected_exit, 'native wait status does not decode to exit')
    _integer(value['pid'], True)
    _integer(value['pgid'], True)
    _text(value['start_fingerprint'])
    if not _need(txn, ctx, 'item', 'identities'):
        return
    _require(_exact(value['item'], ctx.f['item']), 'wait item')
    identity = {k: value[k] for k in ('pid', 'pgid', 'start_fingerprint')}
    if role == 'driver':
        if not _need(txn, ctx, 'allocation'):
            return
        record = ctx.f['allocation']['record']
        _require(identity['pid'] == record['driver_pid'] and identity['pgid'] == record['driver_pgid']
                 and all(_exact(identity[k], ctx.driver[k]) for k in identity), 'driver wait identity')
    else:
        _require(any(row['role'] == 'oracle' and all(_exact(identity[k], row[k]) for k in identity)
                     for row in ctx.f['identities']), 'oracle wait identity not in oracle union')


def _capture(txn, row):
    data = txn.read(row['path'], row['bytes_stored'])
    _require(len(data) == row['bytes_stored'] and hashlib.sha256(data).hexdigest() == row['sha256'],
             'capture actual bytes/hash/count mismatch')


def _publication(txn, row):
    data = txn.read(row['path'], CAP)
    _require(hashlib.sha256(data).hexdigest() == row['sha256'], 'publication byte digest mismatch')


def _exit_state(txn, ctx):
    rows = [row for row in ctx.f['exit_table'] if row['actual_exit'] == ctx.f['exit']['actual_exit']]
    _require(len(rows) == 1 and rows[0]['state'] == ctx.f['publication']['expected_state'],
             'explicit exit_table missing/inconsistent expected_state')


def _names(txn, fd, path, cap):
    before, names = os.fstat(fd), []
    iterator = os.scandir(fd)
    try:
        for entry in iterator:
            names.append(entry.name)
            _require(len(names) <= cap, 'directory entry cap: ' + path)
    finally:
        iterator.close()
    _require(_stat_key(before) == _stat_key(os.fstat(fd)), 'directory changed during census: ' + path)
    return sorted(names)


def _artifacts(txn, ctx):
    record = ctx.f['artifacts']
    cause, fd = 'P2_ARTIFACT_IDENTITY', None
    try:
        fd = txn.directory(_parts(record['job_dir']), cause)
        names = _names(txn, fd, record['job_dir'], MAX_JOB_ENTRIES)
        txn.must_tick('artifact directory census')
        if names != sorted(record['declared']):
            txn.fire('P2_ARTIFACT_SET_MISMATCH', 'actual directory names differ declared exact set')
        for name, declared in record['declared'].items():
            path = record['job_dir'] + '/' + name
            before = None
            try:
                before = os.stat(name, dir_fd=fd, follow_symlinks=False)
                _require(stat.S_ISREG(before.st_mode) and before.st_nlink == 1 and before.st_ino > 0
                         and before.st_size == declared['bytes'], 'artifact regular/link/inode/size')
            except Exception as exc:
                txn.fire(cause, name + ': ' + _why(exc))
            try:
                data = txn.read(path, declared['bytes'])
                _require(len(data) == declared['bytes'] and hashlib.sha256(data).hexdigest() == declared['sha256'],
                         'artifact actual bytes/hash')
            except _Crossed:
                raise
            except Exception as exc:
                txn.fire('P2_ARTIFACT_DIGEST', name + ': ' + _why(exc))
                if txn.crossed:
                    raise _Crossed('artifact callback primary retained; deadline also failed') from exc
            if before is not None:
                try:
                    _require(_stat_key(before) == _stat_key(os.stat(name, dir_fd=fd, follow_symlinks=False)),
                             'artifact identity changed across read')
                except Exception as exc:
                    txn.fire(cause, name + ': ' + _why(exc))
    except _Crossed:
        raise
    except Exception as exc:
        txn.fire('P2_ARTIFACT_SET_MISMATCH', _why(exc))
    finally:
        if fd is not None:
            txn.close(fd, cause)


def _part2(txn, ctx):
    if _need(txn, ctx, 'exit'):
        value = ctx.f['exit']
        _guard(txn, 'P2_EXIT_INVALID', _wait, txn, ctx, value['wait_record'], 'driver', value['actual_exit'])
    for stream, cause in (('stdout', 'P2_CAPTURE_STDOUT_INVALID'), ('stderr', 'P2_CAPTURE_STDERR_INVALID')):
        field = 'captures.' + stream
        if _need(txn, ctx, field):
            _guard(txn, cause, _capture, txn, ctx.f[field])
    if _need(txn, ctx, 'publication'):
        _guard(txn, 'P2_PUBLICATION_INVALID', _publication, txn, ctx.f['publication'])
    if _need(txn, ctx, 'exit_table', 'exit', 'publication'):
        _guard(txn, 'P2_PUBLICATION_EXIT_INCONSISTENT', _exit_state, txn, ctx)
    if _need(txn, ctx, 'artifacts'):
        _artifacts(txn, ctx)


def _oracle_go(txn, ctx):
    value = _load(txn, ctx.f['oracle.go'])
    _require(value.get('status') == 'PARENT_GO' and _exact(value.get('oracle_for'), ctx.f['item']),
             'separate oracle PARENT_GO for exact item required')
    if _need(txn, ctx, 'go'):
        _require(not _exact(ctx.f['oracle.go'], ctx.f['go']), 'oracle needs separately pinned GO')


def _oracle_wait(txn, ctx):
    if _need(txn, ctx, 'exit'):
        _require(not _exact(ctx.f['oracle.wait_record'], ctx.f['exit']['wait_record']), 'oracle wait equals driver wait')
    _wait(txn, ctx, ctx.f['oracle.wait_record'], 'oracle', 0)


def _oracle_verdict(txn, ctx):
    value = _load(txn, ctx.f['oracle.verdict_path'])
    _require(value.get('verdict') == 'PASS' and _exact(value.get('item'), ctx.f['item']), 'oracle verdict/item not PASS')
    if _need(txn, ctx, 'oracle.bound_artifact_digests'):
        _require(_exact(value.get('bound_artifact_digests'), ctx.f['oracle.bound_artifact_digests']),
                 'verdict does not bind exact requested artifact digests')


def _part3(txn, ctx):
    if _need(txn, ctx, 'oracle.go', 'item'):
        _guard(txn, 'P3_ORACLE_GO_INVALID', _oracle_go, txn, ctx)
    if _need(txn, ctx, 'oracle.wait_record', 'oracle.actual_exit'):
        _guard(txn, 'P3_ORACLE_EXIT', _oracle_wait, txn, ctx)
    for stream in ('stdout', 'stderr'):
        field = 'oracle.captures.' + stream
        if _need(txn, ctx, field):
            _guard(txn, 'P3_ORACLE_CAPTURE_INVALID', _capture, txn, ctx.f[field])
    if _need(txn, ctx, 'oracle.verdict_path', 'oracle.verdict', 'item'):
        _guard(txn, 'P3_ORACLE_VERDICT', _oracle_verdict, txn, ctx)
    if _need(txn, ctx, 'oracle.bound_artifact_digests', 'artifacts'):
        declared = {name: row['sha256'] for name, row in ctx.f['artifacts']['declared'].items()}
        if not _exact(declared, ctx.f['oracle.bound_artifact_digests']):
            txn.fire('P3_ORACLE_BINDING', 'oracle digest map not typed-equal exact declared artifact map')


def _take_census(txn, ctx):
    snapshot = txn.observe('census')
    if txn.crossed:
        raise _Crossed('independent census returned late')
    _keys(snapshot, ('complete', 'processes', 'observed_at_mono'))
    _require(type(snapshot['complete']) is bool and type(snapshot['processes']) is list
             and len(snapshot['processes']) <= MAX_TREE_ENTRIES, 'census completeness/process type/count')
    seen, rows = set(), []
    for row in snapshot['processes']:
        _keys(row, ('pid', 'ppid', 'pgid', 'uid', 'start_fingerprint'))
        for key in ('pid', 'ppid', 'pgid', 'uid'):
            _integer(row[key])
        _text(row['start_fingerprint'])
        _require(row['pid'] not in seen, 'duplicate pid in complete census')
        seen.add(row['pid'])
        rows.append((row['pid'], row['ppid'], row['pgid'], row['uid'], row['start_fingerprint']))
    observed = snapshot['observed_at_mono']
    if type(observed) is not float or not math.isfinite(observed):
        txn.fire('P4_CENSUS_STALE', 'observed_at_mono must be finite float; no module clock is read')
    if snapshot['complete'] is not True:
        txn.fire('P4_CENSUS_INCOMPLETE', 'independent census declared incomplete')
    me = os.getpid()
    if me not in seen:
        txn.fire('P4_CENSUS_INCOMPLETE', 'census omitted observing parent pid (positive coverage check)')
    ctx.census = {'complete': snapshot['complete'], 'processes': len(rows), 'observer_pid_present': me in seen,
                  'freshness': 'callback invoked in this transaction after parts1-3; no cached census permitted'}
    return rows


def _part4(txn, ctx):
    rows = _guard(txn, 'P4_CENSUS_FAILED', _take_census, txn, ctx)
    if not _need(txn, ctx, 'identities'):
        return
    identities = ctx.f['identities']
    if not any(row['role'] == 'oracle' for row in identities):
        txn.fire('P4_ORACLE_IDENTITIES_MISSING', 'separately admitted oracle incarnation missing')
    if _need(txn, ctx, 'allocation'):
        rec = ctx.f['allocation']['record']
        if ctx.driver['pid'] != rec['driver_pid'] or ctx.driver['pgid'] != rec['driver_pgid']:
            txn.fire('P4_IDENTITIES_INVALID', 'driver identity not bound to allocation')
    if rows is None:
        return
    by_pid = {row[0]: row for row in rows}
    groups, pids = {row['pgid'] for row in identities}, {row['pid'] for row in identities}
    for identity in identities:
        process = by_pid.get(identity['pid'])
        if process is not None:
            cause = 'P4_IDENTITY_ALIVE' if process[4] == identity['start_fingerprint'] else 'P4_PID_REUSE_AMBIGUOUS'
            txn.fire(cause, identity['role'] + ' pid=' + str(identity['pid']))
    for pid, ppid, pgid, uid, fingerprint in rows:
        if pgid in groups:
            txn.fire('P4_OWNED_GROUP_NONEMPTY', 'pid=%d pgid=%d' % (pid, pgid))
        if ppid in pids:
            txn.fire('P4_OWNED_DESCENDANT', 'pid=%d current ppid=%d (not historical completeness)' % (pid, ppid))


def _kind(mode):
    if stat.S_ISREG(mode):
        return 'file'
    if stat.S_ISDIR(mode):
        return 'dir'
    if stat.S_ISLNK(mode):
        return 'symlink'
    if stat.S_ISFIFO(mode):
        return 'fifo'
    if stat.S_ISSOCK(mode):
        return 'socket'
    if stat.S_ISCHR(mode) or stat.S_ISBLK(mode):
        return 'device'
    return 'other'


def _metadata(info):
    """No unavailable field becomes zero. Count roots/directories just like every entry."""
    blocks = getattr(info, 'st_blocks', None)
    if (type(info.st_size) is not int or info.st_size < 0 or type(blocks) is not int or blocks < 0):
        raise AccountingRefusal('native st_size/st_blocks unavailable or invalid')
    for key in ('st_dev', 'st_ino', 'st_mode', 'st_nlink', 'st_mtime_ns', 'st_ctime_ns'):
        if type(getattr(info, key, None)) is not int:
            raise AccountingRefusal('native accounting/identity metadata unavailable: ' + key)
    _require(info.st_ino > 0 and info.st_nlink >= 1, 'late entry positive inode/link required')
    return {'kind': _kind(info.st_mode), 'dev': info.st_dev, 'ino': info.st_ino, 'mode': info.st_mode,
            'nlink': info.st_nlink, 'bytes': info.st_size, 'allocated_bytes': blocks * 512,
            'mtime_ns': info.st_mtime_ns, 'ctime_ns': info.st_ctime_ns, 'sha256': None}


def _hash_file(txn, parent, name, path, selected):
    _require(selected['bytes'] <= MAX_LATE_FILE_BYTES, 'late regular file cap16GiB')
    _require(txn.streamed_bytes + selected['bytes'] <= MAX_LATE_HASH_BYTES, 'late aggregate hash cap128GiB')
    fd = txn.open(name, os.O_RDONLY | FILE_FLAGS, parent=parent, display=path)
    try:
        before = os.fstat(fd)
        actual = _metadata(before)
        _require(actual['kind'] == 'file' and _exact(actual, selected), 'late file lstat/open inode or metadata mismatch')
        txn.must_tick('late regular file initial identity')
        digest, seen = hashlib.sha256(), 0
        while True:
            txn.must_tick('before late regular file chunk')
            try:
                block = os.read(fd, min(CHUNK, selected['bytes'] + 1 - seen))
            except Exception as primary:
                txn.event('native late read', 'EXCEPTION', _why(primary))
                if not txn.tick('native late read Exception completion'):
                    raise _Crossed('native read primary retained; original deadline crossed') from primary
                raise
            seen += len(block)
            txn.streamed_bytes += len(block)  # retain native progress before deadline or hash work
            timely = txn.tick('late regular file chunk completion')
            if block:
                digest.update(block)
            if not timely:
                raise _Crossed('late regular file chunk returned late')
            _require(seen <= selected['bytes'], 'late file grew during read')
            if not block:
                break
        after = os.fstat(fd)
        txn.must_tick('late regular file final identity')
        _require(seen == selected['bytes'] and _stat_key(before) == _stat_key(after), 'late file identity/size/metadata changed')
        result = dict(actual)
        result['sha256'] = digest.hexdigest()
        txn.hashed_files += 1
        return result
    finally:
        txn.close(fd, 'P5_LATE_CENSUS_INCOMPLETE')


def _scan(txn, fd, path, device, depth, entries):
    _require(depth <= MAX_TREE_DEPTH, 'late tree depth cap')
    before = os.fstat(fd)
    names = _names(txn, fd, path, MAX_TREE_ENTRIES)
    txn.must_tick('late directory name census')
    for name in names:
        full = path + '/' + name
        info = os.stat(name, dir_fd=fd, follow_symlinks=False)
        row = _metadata(info)
        txn.must_tick('late entry lstat completion')
        if row['kind'] == 'file':
            row = _hash_file(txn, fd, name, full, row)
        entries[full] = row
        _require(len(entries) <= MAX_TREE_ENTRIES, 'late tree entry cap')
        if row['kind'] == 'dir':
            _require(info.st_dev == device, 'cross-device directory makes late audit incomplete')
            child = txn.open(name, DIR_FLAGS, parent=fd, display=full)
            try:
                opened = os.fstat(child)
                _require(_stat_key(opened) == _stat_key(info), 'directory replaced/changed before descent')
                _scan(txn, child, full, device, depth + 1, entries)
            finally:
                txn.close(child, 'P5_LATE_CENSUS_INCOMPLETE')
    _require(_stat_key(before) == _stat_key(os.fstat(fd)), 'directory changed across late walk: ' + path)
    txn.must_tick('late directory completion')


def _under(path, roots):
    return any(path == root or path.startswith(root + '/') for root in roots)


def _totals(entries):
    unique = {}
    for path, row in entries.items():
        key = (row['dev'], row['ino'])
        if key in unique:
            _require(_exact(unique[key], row), 'same inode observed inconsistently across aliases')
        else:
            unique[key] = row
    return {'entries': len(entries), 'distinct_inodes': len(unique),
            'logical_bytes': sum(row['bytes'] for row in unique.values()),
            'allocated_bytes': sum(row['allocated_bytes'] for row in unique.values())}


def _account(entries, roots):
    return {'whole': _totals(entries),
            'by_root': {root: _totals({path: row for path, row in entries.items() if _under(path, [root])})
                        for root in roots}}


def _walk(txn, roots):
    entries = {}
    for root in roots:
        fd = txn.directory(_parts(root), 'P5_LATE_CENSUS_INCOMPLETE')
        try:
            info = os.fstat(fd)
            entries[root] = _metadata(info)  # roots/directories are included in distinct-inode totals
            _require(entries[root]['kind'] == 'dir', 'late root must be actual directory')
            _scan(txn, fd, root, info.st_dev, 0, entries)
        finally:
            txn.close(fd, 'P5_LATE_CENSUS_INCOMPLETE')
    accounting = _account(entries, roots)
    txn.must_tick('whole-RUN content census/accounting assembly')
    return {'entries': entries, 'accounting': accounting}


def _free_bytes(txn, roots):
    result = {}
    for root in roots:
        fd = txn.directory(_parts(root), 'P5_FREE_BYTES_LOW')
        try:
            native = os.fstatvfs(fd)
            _require(type(native.f_bavail) is int and native.f_bavail >= 0
                     and type(native.f_frsize) is int and native.f_frsize > 0, 'native free-byte fields unavailable')
            result[root] = native.f_bavail * native.f_frsize
            txn.must_tick('fstatvfs completion')
        finally:
            txn.close(fd, 'P5_FREE_BYTES_LOW')
    return result


def _baseline(txn, audit):
    value = _load(txn, audit['baseline_manifest'], CAP)
    _keys(value, ('format', 'roots', 'entries', 'accounting'))
    _require(value['format'] == 'parent-release-late-baseline-v2' and _exact(value['roots'], audit['roots']),
             'baseline-v2 format/root scope (no v1 compatibility)')
    _require(type(value['entries']) is dict and len(value['entries']) <= MAX_TREE_ENTRIES, 'baseline entry map/count')
    for path, row in value['entries'].items():
        _parts(path)
        _require(_under(path, audit['roots']), 'baseline path outside roots')
        _keys(row, ENTRY_KEYS)
        _require(type(row['kind']) is str and row['kind'] in KINDS, 'baseline kind')
        for key in ('dev', 'ino', 'mode', 'nlink', 'bytes', 'allocated_bytes', 'mtime_ns', 'ctime_ns'):
            _require(type(row[key]) is int, 'baseline exact integer field: ' + key)
        _require(row['ino'] > 0 and row['nlink'] >= 1 and row['bytes'] >= 0 and row['allocated_bytes'] >= 0
                 and row['allocated_bytes'] % 512 == 0 and row['kind'] == _kind(row['mode']), 'baseline metadata/accounting range')
        _require(_hex(row['sha256']) if row['kind'] == 'file' else row['sha256'] is None, 'baseline content digest kind')
    _require(all(root in value['entries'] and value['entries'][root]['kind'] == 'dir' for root in audit['roots']),
             'baseline actual directory root missing')
    _require(_exact(value['accounting'], _account(value['entries'], audit['roots'])), 'baseline distinct-inode accounting mismatch')
    return value


def _late_compare(txn, ctx, audit, baseline, fresh):
    allowed_paths = {s for s in audit['allowed_new'] if s.startswith('/')}
    allowed_names = set(audit['allowed_new']) - allowed_paths
    counts = {'new': 0, 'changed': 0, 'removed': 0}
    before, after = baseline['entries'], fresh['entries']
    for path in sorted(after):
        key = 'new' if path not in before else 'changed' if not _exact(after[path], before[path]) else None
        if key is not None:
            counts[key] += 1
            if path not in allowed_paths and path.rsplit('/', 1)[-1] not in allowed_names:
                txn.fire('P5_LATE_UNDECLARED_' + key.upper(), path)
    for path in sorted(before):
        if path not in after:
            counts['removed'] += 1
            if path not in allowed_paths and path.rsplit('/', 1)[-1] not in allowed_names:
                txn.fire('P5_LATE_UNDECLARED_REMOVED', path)
    ctx.late['delta_counts'] = counts


def _part5(txn, ctx):
    if not _need(txn, ctx, 'late_audit'):
        return
    audit = ctx.f['late_audit']
    baseline = _guard(txn, 'P5_LATE_AUDIT_INVALID', _baseline, txn, audit)
    fresh = _guard(txn, 'P5_LATE_CENSUS_INCOMPLETE', _walk, txn, audit['roots'])
    free = _guard(txn, 'P5_FREE_BYTES_LOW', _free_bytes, txn, audit['roots'])
    ctx.late = {'roots': audit['roots'], 'whole_RUN_included': RUN_ROOT in audit['roots'],
                'fresh_entries': len(fresh['entries']) if fresh is not None else None,
                'baseline_entries': len(baseline['entries']) if baseline is not None else None,
                'fresh_accounting': fresh['accounting'] if fresh is not None else None,
                'baseline_accounting': baseline['accounting'] if baseline is not None else None,
                'free_bytes': free, 'hashed_regular_files': txn.hashed_files, 'hashed_bytes': txn.streamed_bytes}
    if free is not None:
        for root, available in free.items():
            if available < FREE_FLOOR:
                txn.fire('P5_FREE_BYTES_LOW', root + ': free=' + str(available))
    if baseline is not None and fresh is not None:
        _late_compare(txn, ctx, audit, baseline, fresh)


def _evaluate(txn, ctx, spec, commit_dir):
    _shape(txn, ctx, spec, commit_dir)
    txn.must_tick('transaction start / frozen spec assembly')
    for number, function in enumerate((_part1, _part2, _part3, _part4, _part5), 1):
        if txn.crossed:
            return
        txn.part = number
        try:
            function(txn, ctx)
        except _Crossed:
            return
        except Exception as exc:
            txn.fire('P%d_INTERNAL_ERROR' % number, _why(exc))
        txn.evaluated.add(number)


def _owned_reading(value):
    _keys(value, ('settled', 'text', 'child', 'reaped', 'group_empty', 'stdout_eof', 'term_sent'))
    _require(all(value[key] is True for key in ('settled', 'reaped', 'group_empty', 'stdout_eof')),
             'owned /bin/date helper not fully settled')
    _require(type(value['term_sent']) is int and value['term_sent'] == 0, 'date TERM means overrun, not valid reading')
    _keys(value['child'], ('pid', 'pgid', 'start_fingerprint'))
    _integer(value['child']['pid'], True)
    _integer(value['child']['pgid'], True)
    _text(value['child']['start_fingerprint'])
    _require(value['child']['pid'] == value['child']['pgid'], 'date child must own process group')
    _date_value(value['text'])
    return value['text'], dict(value['child'])


def _stamp(txn, ctx):
    if txn.crossed:
        return
    txn.part = 5
    try:
        value = txn.observe('owned_date')
    except Exception as exc:
        txn.fire('P5_OWNED_DATE_FAILED', _why(exc))
        return
    if txn.crossed:
        return
    try:
        ctx.date_text, ctx.date_child = _owned_reading(value)
    except Exception as exc:
        txn.fire('P5_OWNED_DATE_FAILED', _why(exc))


def _statuses(txn):
    return {str(number): 'FAIL' if any(c.startswith('P%d_' % number) for c in txn.fired)
            else 'NOT_EVALUATED' if number not in txn.evaluated else 'BLOCKED' if number in txn.blocked else 'PASS'
            for number in range(1, 6)}


def _record(txn, ctx, decision, reduced=False):
    causes = [cause for cause in CAUSES if cause in txn.fired]
    evidence = {cause: values[:1] if reduced else values for cause, values in txn.evidence.items()}
    return {'format': 'parent-release-disposition-v2', 'module': 'parent_release_v2.py',
            'scope_contract_sha256': CONTRACT_SHA256, 'repair_scope_sha256': REPAIR_SCOPE_SHA256,
            'item': ctx.f.get('item'), 'state': decision, 'causes': causes,
            'evidence': evidence, 'suppressed_evidence_counts': txn.suppressed, 'parts': _statuses(txn),
            'recorded_at': ctx.date_text, 'timestamp_source': 'owned bounded /bin/date only',
            'date_child': ctx.date_child, 'spec_sha256': ctx.spec_sha, 'spec_bytes': ctx.spec_bytes,
            'spec': None if reduced else ctx.spec_embed, 'registry_observation': ctx.registry,
            'census': ctx.census, 'late_audit': ctx.late, 'read_count': txn.read_count,
            'read_observation_sha256': txn.read_digest.hexdigest(), 'reads': [] if reduced else txn.read_log,
            'callback_count': txn.callback_count, 'callback_event_sha256': txn.callback_digest.hexdigest(),
            'callback_events': [] if reduced else txn.callback_log, 'reservation': ctx.f.get('reservation'),
            'identity_union_completeness': 'EXTERNAL_PREREQUISITE_NOT_VERIFIED',
            'identity_boundary': IDENTITY_NOTE, 'release_effect': RELEASE_EFFECT,
            'runtime_authority': False, 'scientific_authority': False, 'boundary': BOUNDARY}


def _assemble(txn, ctx):
    statuses = _statuses(txn)
    if not txn.fired and any(status != 'PASS' for status in statuses.values()):
        txn.fire('P5_INTERNAL_ERROR', 'not every part PASS; no release by unevaluated/blocked default')
    decision = 'HELD' if txn.fired else 'RELEASED'
    data = _canonical(_record(txn, ctx, decision))
    if len(data) >= DECISION_CAP:
        txn.fire('P5_DECISION_TOO_LARGE', 'complete decision >=1MiB; reduced HELD only')
        decision, data = 'HELD', _canonical(_record(txn, ctx, 'HELD', True))
    _require(len(data) < DECISION_CAP, 'reduced decision exceeds cap')
    return decision, data


def _slug(item):
    text = item if type(item) is str else 'invalid-item'
    return ''.join(c if ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c in '-_') else '_'
                   for c in text)[:64] or 'item'


def _write_all(fd, data, retained):
    view, at, calls = memoryview(data), 0, 0
    while at < len(view):
        calls += 1
        _require(calls <= 65536, 'write call cap')
        count = os.write(fd, view[at:])
        _require(type(count) is int and 0 < count <= len(view) - at, 'zero/invalid write')
        at += count
        retained['bytes_written'] = at
    retained['line_complete'] = True


def _pread_exact(fd, count, offset=0):
    chunks, seen = [], 0
    _require(0 <= count <= CAP, 'pread cap')
    while seen < count:
        block = os.pread(fd, min(CHUNK, count - seen), offset + seen)
        _require(block, 'short pread')
        chunks.append(block)
        seen += len(block)
    return b''.join(chunks)


def _write_new(txn, dfd, name, data, retained):
    fd = txn.open(name, os.O_RDWR | os.O_CREAT | os.O_EXCL | FILE_FLAGS,
                  parent=dfd, display=retained['path'])
    retained['created'] = True
    closed = False
    try:
        original = os.fstat(fd)
        retained['identity'] = {'dev': original.st_dev, 'ino': original.st_ino}
        _require(stat.S_ISREG(original.st_mode) and original.st_nlink == 1 and original.st_ino > 0,
                 'new disposition regular one-link inode')
        _write_all(fd, data, retained)
        os.fsync(fd)
        retained['file_fsync'] = True
        _require(_pread_exact(fd, len(data)) == data, 'created inode readback mismatch')
        actual = os.fstat(fd)
        _require(actual.st_dev == original.st_dev and actual.st_ino == original.st_ino
                 and actual.st_nlink == 1 and actual.st_size == len(data), 'created inode changed')
    finally:
        closed = txn.close(fd, 'P5_COMMIT_WRITE_FAILED')
    _require(closed, 'new disposition close unresolved')
    os.fsync(dfd)
    retained['directory_fsync'] = True


def _ack(txn, dfd, name, data, retained, result):
    if txn.crossed:
        return False
    try:
        back = txn.observe('read_bytes', retained['path'], len(data), after_ack=True)
    except Exception as exc:
        result['ack'] = 'ACK_FAILED'
        txn.fire('P5_ACK_FAILED', _why(exc))
        return False
    if txn.crossed:
        result['ack'] = 'ACK_UNPROVED_DEADLINE'
        result['uncertainty'] = 'late readback; no further identity check/registry I/O'
        return False
    try:
        _require(type(back) is bytes and back == data
                 and hashlib.sha256(back).hexdigest() == retained['sha256'], 'ACK bytes/hash mismatch')
        actual = os.stat(name, dir_fd=dfd, follow_symlinks=False)
        identity = retained['identity']
        _require(stat.S_ISREG(actual.st_mode) and actual.st_nlink == 1 and actual.st_size == len(data)
                 and actual.st_dev == identity['dev'] and actual.st_ino == identity['ino'], 'ACK not original created inode')
    except Exception as exc:
        txn.fire('P5_ACK_FAILED', _why(exc))
        result['ack'] = 'ACK_FAILED'
        return False
    if not txn.tick('ACK original-inode identity completion', after_ack=True):
        result['ack'] = 'ACK_UNPROVED_DEADLINE'
        return False
    txn.ack_done, result['ack'] = True, 'ACK_OK'
    return True


def _commit(txn, ctx, data, result):
    if txn.crossed or ctx.commit_dir is None:
        result['uncertainty'] = 'no safe commit directory/original deadline; no I/O attempted'
        return False
    _mutation_parts(ctx.commit_dir)
    digest = hashlib.sha256(data).hexdigest()
    name = 'prt-v2-' + _slug(ctx.f.get('item')) + '-' + digest + '.json'
    retained = {'path': ctx.commit_dir + '/' + name, 'sha256': digest, 'bytes': len(data),
                'created': False, 'bytes_written': 0, 'line_complete': False, 'identity': None,
                'file_fsync': False, 'directory_fsync': False}
    result['disposition'] = retained
    dfd = None
    try:
        dfd = txn.directory(_mutation_parts(ctx.commit_dir), 'P5_COMMIT_WRITE_FAILED')
        _write_new(txn, dfd, name, data, retained)
        if not txn.tick('disposition write/file+directory fsync completion'):
            result['uncertainty'] = 'exclusive disposition may exist; no original deadline, ACK/registry forbidden'
            return False
        return _ack(txn, dfd, name, data, retained, result)
    except _Crossed:
        return False
    except Exception as exc:
        txn.fire('P5_COMMIT_WRITE_FAILED', _why(exc))
        result['ack'] = 'ACK_NOT_ATTEMPTED'
        return False
    finally:
        if dfd is not None:
            txn.close(dfd, 'P5_COMMIT_WRITE_FAILED')


def _registry_tail(txn, ctx, fd):
    observed, allocation = ctx.registry, ctx.f['allocation']
    info = os.fstat(fd)
    _require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1 and info.st_ino > 0
             and observed['bytes'] <= info.st_size <= CAP, 'registry identity/size/links')
    prefix = _pread_exact(fd, observed['bytes'])
    _require(hashlib.sha256(prefix).hexdigest() == observed['sha256'], 'observed registry prefix changed')
    suffix = _pread_exact(fd, info.st_size - observed['bytes'], observed['bytes'])
    _require(not suffix or suffix.endswith(b'\n'), 'new registry suffix torn')
    for line in suffix[:-1].split(b'\n') if suffix else []:
        row = _json(line)
        _require(type(row) is dict, 'registry suffix line object')
        if _exact(row.get('item'), ctx.f['item']):
            _require(_held_for(row, ctx.f['item'], allocation['line_sha256']), 'concurrent non-HELD item registry entry')
    return info.st_size


def _append_registry(txn, ctx, releasable, result):
    retained = result['registry']
    if txn.crossed or ctx.registry is None or not _need(txn, ctx, 'allocation', 'item'):
        retained['detail'] = 'no safe original deadline/selected registry observation/allocation binding'
        return
    allocation, fd, dfd = ctx.f['allocation'], None, None
    _mutation_parts(allocation['registry_path'])
    state = 'RELEASED' if releasable else 'HELD'
    row = {'format': 'parent-release-registry-v2', 'owner': 'parent_release_v2.py', 'item': ctx.f['item'],
           'state': state, 'decision_in_disposition': result['decision'],
           'disposition': result['disposition']['path'], 'disposition_sha256': result['disposition']['sha256'],
           'allocation_line_sha256': allocation['line_sha256'], 'causes': [c for c in CAUSES if c in txn.fired],
           'recorded_at': ctx.date_text, 'reservation': ctx.f.get('reservation'),
           'remaining_output_reservation_bytes': 0 if releasable else allocation['record']['reservation_bytes'],
           'release_effect': RELEASE_EFFECT}
    line = (json.dumps(row, sort_keys=True, ensure_ascii=True, allow_nan=False) + '\n').encode('ascii')
    retained.update({'state': state, 'line_sha256': hashlib.sha256(line[:-1]).hexdigest(), 'path': allocation['registry_path']})
    closed = True
    try:
        _require(len(line) <= 65536, 'registry line cap')
        parts = _mutation_parts(allocation['registry_path'])
        dfd = txn.directory(parts[:-1], 'P5_REGISTRY_APPEND_FAILED')
        fd = txn.open(parts[-1], os.O_RDWR | os.O_APPEND | FILE_FLAGS, parent=dfd, display=allocation['registry_path'])
        before = _registry_tail(txn, ctx, fd)
        txn.must_tick('registry pre-append verification')
        _write_all(fd, line, retained)
        os.fsync(fd)
        retained['fsync'] = True
        _require(os.fstat(fd).st_size == before + len(line), 'registry concurrent growth violates single-writer premise')
        retained['status'] = 'APPENDED'
    except _Crossed:
        retained['status'] = 'NOT_APPENDED_DEADLINE'
    except Exception as exc:
        txn.fire('P5_REGISTRY_APPEND_FAILED', _why(exc))
        retained['status'], retained['detail'] = 'FAILED', _why(exc)
    finally:
        if fd is not None:
            closed = txn.close(fd, 'P5_REGISTRY_APPEND_FAILED') and closed
        if dfd is not None:
            closed = txn.close(dfd, 'P5_REGISTRY_APPEND_FAILED') and closed
        retained['closed'] = closed
    if not txn.crossed:
        txn.tick('registry append/fsync/close completion', after_ack=True)


def _new_result():
    return {'format': 'parent-release-result-v2', 'state': 'HELD', 'decision': 'HELD',
            'release_effective': False, 'ack': 'ACK_NOT_ATTEMPTED', 'disposition': None,
            'registry': {'status': 'NOT_ATTEMPTED', 'bytes_written': 0, 'line_complete': False,
                         'fsync': False, 'closed': False, 'state': None, 'line_sha256': None},
            'uncertainty': None, 'runtime_authority': False, 'scientific_authority': False,
            'release_effect': RELEASE_EFFECT, 'identity_boundary': IDENTITY_NOTE}


def _finish(txn, ctx, result):
    txn.part = 5
    decision, data = _assemble(txn, ctx)
    result['decision'] = decision
    if txn.crossed:
        result['uncertainty'] = 'original deadline unavailable; in-memory HELD only, no new I/O allowance'
        return
    if not txn.tick('complete decision assembly'):
        result['decision'] = 'HELD'
        result['uncertainty'] = 'deadline crossed after assembly; no commit/readback/registry I/O'
        return
    if not _commit(txn, ctx, data, result):
        result['registry']['detail'] = 'no successful ACK; registry append forbidden'
        return
    if txn.crossed:
        return
    releasable = decision == 'RELEASED' and not txn.fired
    _append_registry(txn, ctx, releasable, result)


def _final(txn, ctx, result):
    effective = (result['decision'] == 'RELEASED' and not txn.fired and not txn.crossed
                 and result['ack'] == 'ACK_OK' and result['registry']['status'] == 'APPENDED'
                 and result['registry']['state'] == 'RELEASED' and result['registry']['fsync'] is True
                 and result['registry']['closed'] is True)
    result.update({'state': 'RELEASED' if effective else 'HELD', 'release_effective': effective,
                   'causes': [cause for cause in CAUSES if cause in txn.fired], 'evidence': txn.evidence,
                   'suppressed_evidence_counts': txn.suppressed, 'parts': _statuses(txn),
                   'original_deadline_crossed': txn.crossed,
                   'callback_count': txn.callback_count, 'callback_events': txn.callback_log,
                   'callback_event_sha256': txn.callback_digest.hexdigest(),
                   'fds': {'opened': txn.opened, 'closed': txn.closed, 'live': len(txn.live), 'unresolved': txn.unresolved}})
    if result['registry'].get('state') == 'RELEASED' and not effective:
        result['uncertainty'] = ('RELEASED registry bytes may survive but caller did NOT observe completed '
                                 'success; keep reservation HELD and preserve every partial object.')
    return result


def _chain(exc, pending):
    if pending is not None and exc is not pending and exc.__context__ is None:
        exc.__context__ = pending
    raise exc


def _absorb(txn, exc, pending):
    if isinstance(exc, Exception):
        txn.fire('P%d_INTERNAL_ERROR' % txn.part, _why(exc))
        return pending
    if pending is not None:
        _chain(exc, pending)
    txn.fire('P%d_BASE_EXCEPTION' % txn.part, _why(exc))
    return exc


def _commit_safe(txn):
    return not txn.crossed and not txn.unsafe.intersection(('deadline_check', 'read_bytes', 'owned_date'))


def _attach_and_raise(exc, result):
    try:
        exc.parent_release_result = result
    except Exception:
        pass
    raise exc


def decide_and_commit(spec, read_bytes, census, owned_date, commit_dir, deadline_check):
    """Evaluate five independent parts, one new exclusive disposition/ACK, one append-only line.

    Only caller-observed returned state RELEASED is effective, conditional on the authentic
    parent authority/immutable freeze/full identity-union and caller-integration prerequisites.
    Any other outcome/exception holds the allocation. BaseException in evaluation attempts HELD
    only while the ORIGINAL deadline/reader/date remain safe; commit BaseException propagates.
    No new clock, process or signal. No v1 compatibility. Full schemas/controls in v2 design notes.
    """
    txn, ctx, result, pending = _Txn(read_bytes, census, owned_date, deadline_check), _Ctx(), _new_result(), None
    try:
        _evaluate(txn, ctx, spec, commit_dir)
    except _Crossed:
        pass
    except BaseException as exc:
        pending = _absorb(txn, exc, pending)
    if pending is not None and not _commit_safe(txn):
        _attach_and_raise(pending, _final(txn, ctx, result))
    if not txn.crossed:
        try:
            _stamp(txn, ctx)
        except BaseException as exc:
            pending = _absorb(txn, exc, pending)
    if pending is not None and not _commit_safe(txn):
        _attach_and_raise(pending, _final(txn, ctx, result))
    try:
        _finish(txn, ctx, result)
    except _Crossed:
        pass
    except Exception as exc:
        txn.fire('P5_INTERNAL_ERROR', _why(exc))
    except BaseException as exc:
        _chain(exc, pending)
    result = _final(txn, ctx, result)
    if pending is not None:
        _attach_and_raise(pending, result)
    return result


def build_late_baseline(roots, deadline_check):
    """Observation only: coherent content+metadata+accounting baseline-v2, no writes/processes.

    Separately admit. Parent serializes/pins output before launch. Whole RUN root mandatory;
    all applicable lane-root coverage remains parent-authenticated. No v1 schema accepted.
    No partial baseline or unavailable accounting returns as success. No generated timestamp.
    """
    selected = _roots(roots)
    txn = _Txn(None, None, None, deadline_check)
    txn.part = 5
    try:
        txn.must_tick('baseline start')
        snapshot = _walk(txn, selected)
        _require(not txn.fired and not txn.unresolved and not txn.live, 'incomplete baseline resources')
        result = {'format': 'parent-release-late-baseline-v2', 'roots': selected,
                  'entries': snapshot['entries'], 'accounting': snapshot['accounting']}
        _require(len(_canonical(result)) <= CAP, 'baseline exceeds16MiB cap')
        txn.must_tick('baseline-v2 assembly')
        return result
    except _Crossed as exc:
        raise ReleaseRefusal('original deadline crossed; no baseline returned') from exc
