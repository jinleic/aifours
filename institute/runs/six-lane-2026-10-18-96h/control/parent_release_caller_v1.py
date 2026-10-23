"""SOURCE ONLY, UNTESTED. CP1 parent caller integration for the parent release transaction v3.

Scope parent-release-cp1-cp2-implementation-scope-v1.json (1f717bf9...) item CP1; exact design
frozen in review/parent-release-cp1-checkpoint-001-v1.json before this source was written.
Definitions plus EMPTY in-memory ledgers only at import: no I/O, clock, environment, process or
signal operation, and the transaction module is never imported. invoke_release reads the PINNED
PRT3 bytes through the parent's ORIGINAL reader, executes exactly those verified bytes in a fresh
namespace, calls only its public decide_and_commit, observes the complete returned RELEASED
result, re-reads the disposition and registry, joins every retained reader's unresolved resources,
writes ONE exclusive caller receipt and acknowledges it, all under the SAME original deadline.
Only after a final original-deadline check is a RELEASED CallerOutcome registered as effective.
ReservationAccount.release accounts a held reservation only from that identical outcome object
plus a fresh receipt readback under the outcome's retained original deadline predicate. Registry
lines, dispositions, receipts, result dicts and reports are never authority by themselves.
No scheduler or admission, no new deadline, no v1/v2 fallback. Native calls and callbacks can
stall: checks follow completion; there is no hard-real-time guarantee.
"""
import hashlib
import json
import math
import os
import stat

MODULE = 'parent_release_caller_v1.py'
SCOPE_SHA256 = '1f717bf944e6d5a524aa0a65776d39726cd251bcd006971ba322f328de6bd314'
DESIGN_CHECKPOINT_SHA256 = '565a29ed61fb0c3f0d426330d55d516089e1de80e479a4cc396e9131008c291c'
AIFOURS_ROOT = '/Users/jinleic/repos/aifours'
RUN_ROOT = AIFOURS_ROOT + '/institute/runs/six-lane-2026-10-18-96h'
CALLER_PATH = RUN_ROOT + '/control/parent_release_caller_v1.py'
READER_PATH = RUN_ROOT + '/control/beta_parent_reader_v1.py'
READER_SHA256 = '1fc8f00c08cd9f78885c9a38fa0797ce5b01aba8e8ad39a6d19d7b6ce3370ec6'
PRT3_PATH = RUN_ROOT + '/control/parent_release_v3.py'
PRT3_SHA256 = '161ae04ce4ee98db76bb5b9b983cdfa13c769733b10159ebb5d31b5e377bd23a'
PRT3_BYTES = 81235
FORBIDDEN_PRT_SHA256 = frozenset((
    '6bc92891779feb3e50b3d9948a5d7fc0711a451665794d7fd32738807ad60127',   # v1, self-HOLD
    'addcdf4c75c08bd4cd1e6d13c833886d058851b9b1927557008bb41bf93992a1'))  # v2, HOLD 5M/1m
PRT_MODULE = 'parent_release_v3.py'
PRT_CONTRACT_SHA256 = '4d12287257f8bf74d9057a796a0c6f7a391387c411b95d5dcda1131aa4692d3e'
PRT_REPAIR_SCOPES = ['2fdf13b45e946df4f07881b0e6e2b5bc5452ea33d1df022afe896dded698b407',
                     '1f9befdb4d012800a8e2160c0ce8e822d255e34c88496fd26cb8875aac894030']
RESULT_FORMAT = 'parent-release-result-v3'
DISPOSITION_FORMAT = 'parent-release-disposition-v3'
REGISTRY_FORMAT = 'parent-release-registry-v3'
DISPOSITION_PREFIX = 'prt-v3-'
RECEIPT_FORMAT = 'parent-release-caller-receipt-v1'
RECEIPT_PREFIX = 'prt-caller-v1-'
OUTCOME_FORMAT = 'parent-release-caller-outcome-v1'
ACCOUNT_FORMAT = 'parent-release-reservation-account-v1'
PREREQUISITE_FORMAT = 'parent-release-cp1-prerequisite-v1'
PREREQUISITE_STATUS = 'DISCHARGED_BY_PARENT'
PREREQUISITE_ORIGIN = 'PARENT_ASSERTED_NOT_SOURCE_AUTHENTICATED'
PREREQUISITES = ('authority_execution_provenance', 'callback_provenance', 'identity_union_census_cp2',
                 'oracle_binding', 'publication_freeze_scope', 'registry_single_writer',
                 'finite_qualification')
OWNER_KEYS = frozenset(('item', 'allocation', 'reservation', 'commit_dir', 'receipt_dir', 'sources',
                        'prerequisites'))
RESULT_KEYS = frozenset(('format', 'state', 'decision', 'release_effective', 'ack', 'disposition', 'registry',
                         'uncertainty', 'runtime_authority', 'scientific_authority', 'final_deadline_check',
                         'release_effect', 'identity_boundary', 'causes', 'evidence',
                         'suppressed_evidence_counts', 'parts', 'original_deadline_crossed', 'callback_count',
                         'callback_events', 'callback_event_sha256', 'resources'))
RESULT_DISPOSITION_KEYS = frozenset(('path', 'sha256', 'bytes', 'create_attempted', 'created', 'bytes_written',
                                     'line_complete', 'identity', 'file_fsync', 'directory_fsync'))
RESULT_REGISTRY_KEYS = frozenset(('status', 'bytes_written', 'line_complete', 'fsync', 'closed', 'state',
                                  'line_sha256'))
RESULT_REGISTRY_OPTIONAL = frozenset(('path', 'detail'))
RESULT_RESOURCE_KEYS = frozenset(('acquired', 'closed', 'live', 'unresolved_total', 'unresolved'))
REGISTRY_ROW_KEYS = frozenset(('format', 'owner', 'item', 'state', 'decision_in_disposition', 'disposition',
                               'disposition_sha256', 'allocation_line_sha256', 'causes', 'recorded_at',
                               'reservation', 'remaining_output_reservation_bytes', 'release_effect'))
ACK_STATES = frozenset(('ACK_NOT_ATTEMPTED', 'ACK_OK', 'ACK_FAILED', 'ACK_UNPROVED_DEADLINE'))
FINAL_CHECKS = frozenset(('PASSED', 'CROSSED', 'NOT_PERFORMED_ALREADY_CROSSED', 'BASE_EXCEPTION',
                          'NOT_PERFORMED'))
PARTS_PASS = {'1': 'PASS', '2': 'PASS', '3': 'PASS', '4': 'PASS', '5': 'PASS'}
CAP = 16 << 20
DOC_CAP = 1 << 20
SPEC_CAP = 4 << 20
RESULT_CAP = 4 << 20
RECEIPT_CAP = 1 << 20
MAX_NODES = 131072
MAX_DEPTH = 256
MAX_INT_BITS = 4096
MAX_TEXT = 512
MAX_EVENTS = 128
MAX_READS = 64
MAX_EVIDENCE = 16
MAX_SAMPLE = 64
MAX_NATIVE_CALLS = 65536
CHUNK = 65536
CLOEXEC = getattr(os, 'O_CLOEXEC', 0)
DIR_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_NONBLOCK | CLOEXEC
NEW_FILE_FLAGS = os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_NONBLOCK | CLOEXEC
CAUSES = (
    'CP1_CALLBACKS_INVALID', 'CP1_READER_INVALID', 'CP1_OWNER_INVALID', 'CP1_SPEC_BINDING',
    'CP1_IDENTITY_UNION', 'CP1_PRT_SOURCE', 'CP1_SOURCE_PINS', 'CP1_PREREQUISITE_MISSING',
    'CP1_DEADLINE_PRE_INVOKE', 'CP1_PRT_EXCEPTION', 'CP1_PRT_BASE_EXCEPTION', 'CP1_RESULT_INVALID',
    'CP1_RESULT_NOT_RELEASED', 'CP1_ENDEDNESS', 'CP1_DEADLINE_POST_RESULT', 'CP1_DISPOSITION_READBACK',
    'CP1_REGISTRY_READBACK',
    'CP1_UNRESOLVED_RESOURCES', 'CP1_RECEIPT_WRITE', 'CP1_RECEIPT_ACK', 'CP1_DEADLINE_RECEIPT',
    'CP1_DEADLINE_FINAL', 'CP1_INTERNAL_ERROR', 'CP1_BASE_EXCEPTION')
ACCOUNT_CAUSES = (
    'AC_OUTCOME_NOT_EFFECTIVE', 'AC_OUTCOME_LATCHED', 'AC_NOT_HELD', 'AC_RECEIPT_REF_INVALID',
    'AC_RECEIPT_READBACK', 'AC_UNRESOLVED_RESOURCES', 'AC_DEADLINE', 'AC_INTERNAL_ERROR',
    'AC_BASE_EXCEPTION')
ADMISSION = 'NONE: reservation accounting only; no scheduler, next-job admission or CPU/disk grant.'
RECEIPT_EFFECT = ('A caller receipt records one in-process CP1 observation and is never authority by '
                  'itself. Accounting requires the identical minted RELEASED CallerOutcome returned by '
                  'invoke_release in this parent process plus a fresh receipt readback under the same '
                  'original deadline (ReservationAccount.release). Partial or complete receipts, '
                  'dispositions and RELEASED registry lines never grant release.')
OUTCOME_EFFECT = ('Only the identical CallerOutcome object minted RELEASED after the final original-deadline '
                  'check, consumed once by ReservationAccount.release with a matching fresh receipt '
                  'readback, accounts a reservation. report() copies, dicts and disk bytes carry no authority.')
BOUNDARY = ('No scheduler, admission, runtime, scientific or publication authority. Native calls and '
            'callbacks can stall past the deadline; checks follow completion; no hard-real-time '
            'guarantee. In-process minting prevents accidental dict/copy use, not hostile in-process '
            'code. Named prerequisites are parent-asserted refs whose origin this source cannot '
            'authenticate; matching JSON or SHA256 authenticates selected bytes, not their origin.')


class CallerRefusal(ValueError):
    """Typed bounded refusal; it can never certify a release."""


class _Crossed(Exception):
    """Internal unwind after the original deadline became unavailable."""


def _require(condition, message):
    if not condition:
        raise CallerRefusal(message)


def _short(text):
    return text if len(text) <= MAX_TEXT else text[:MAX_TEXT]


def _why(exc):
    try:
        text = type(exc).__name__ + ': ' + str(exc)
    except Exception:
        text = type(exc).__name__ + ': <unprintable>'
    return _short(text)


def _text(value, maximum=MAX_TEXT):
    _require(type(value) is str and 0 < len(value) <= maximum and '\x00' not in value
             and '\n' not in value and '\r' not in value, 'text type/length')
    return value


def _hex(value):
    return type(value) is str and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def _count(value):
    return type(value) is int and value >= 0


def _path(value):
    _require(type(value) is str and value.startswith('/') and 1 < len(value) <= 4096
             and '\x00' not in value, 'normalized absolute path required')
    parts = value.split('/')[1:]
    _require(len(parts) <= 128 and all(part not in ('', '.', '..') for part in parts),
             'normalized path components required')
    return parts


def _mutation_path(value):
    parts = _path(value)
    _require(value == AIFOURS_ROOT or value.startswith(AIFOURS_ROOT + '/'), 'mutation target outside aifours')
    return parts


def _within(path, base):
    return path == base or path.startswith(base + '/')


def _ref(value):
    _require(type(value) is dict and set(value) == {'path', 'sha256'}, 'ref exact {path,sha256}')
    _path(value['path'])
    _require(_hex(value['sha256']), 'ref lowercase 64-hex digest')
    return value


def _exact(left, right):
    """Typed structural equality over detached JSON values; bool is never int."""
    stack = [(left, right)]
    while stack:
        a, b = stack.pop()
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            if set(a) != set(b):
                return False
            stack.extend((a[key], b[key]) for key in a)
        elif type(a) is list:
            if len(a) != len(b):
                return False
            stack.extend(zip(a, b))
        elif a != b:
            return False
    return True


def _string_cost(text):
    return 2 + (2 if text.isascii() and text.isprintable() else 12) * len(text)


def _preflight(value, cap):
    """Bound an in-memory JSON-shaped value BEFORE serialization: exact JSON types, no cycles or
    shared containers, finite floats, node/depth/int/size caps. No recursion."""
    stack, seen, nodes, cost = [(value, 0)], set(), 0, 0
    while stack:
        node, depth = stack.pop()
        nodes += 1
        _require(nodes <= MAX_NODES and depth <= MAX_DEPTH, 'JSON node/depth cap')
        kind = type(node)
        if kind is dict or kind is list:
            _require(id(node) not in seen, 'cycle or shared container')
            seen.add(id(node))
            _require(nodes + len(stack) + len(node) <= MAX_NODES, 'JSON container cap')
            if kind is dict:
                for key, item in node.items():
                    _require(type(key) is str, 'JSON object keys must be exact str')
                    cost += _string_cost(key) + 1
                    stack.append((item, depth + 1))
            else:
                for item in node:
                    cost += 1
                    stack.append((item, depth + 1))
            cost += 2
        elif kind is str:
            cost += _string_cost(node)
        elif kind is int:
            _require(node.bit_length() <= MAX_INT_BITS, 'integer bit cap')
            cost += 2 + node.bit_length() // 3
        elif kind is float:
            _require(math.isfinite(node), 'finite float required')
            cost += 32
        elif kind is bool or node is None:
            cost += 5
        else:
            raise CallerRefusal('non-JSON type ' + kind.__name__)
        _require(cost <= cap, 'serialized size cap')


def _canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True, allow_nan=False,
                       separators=(',', ':')) + '\n').encode('ascii')


def _pairs(rows):
    result = {}
    for key, value in rows:
        _require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def _no_constant(name):
    raise CallerRefusal('non-finite JSON constant ' + name)


def _finite_float(text):
    value = float(text)
    _require(math.isfinite(value), 'non-finite JSON float')
    return value


def _strict_json(data):
    _require(type(data) is bytes, 'JSON bytes required')
    return json.loads(data.decode('utf-8'), object_pairs_hook=_pairs, parse_constant=_no_constant,
                      parse_float=_finite_float)


def _detach(value, cap):
    """Bounded preflight, canonical bytes, strict reparse: (detached copy, sha256, byte count)."""
    _preflight(value, cap)
    raw = _canonical(value)
    _require(len(raw) <= cap, 'serialized cap')
    return _strict_json(raw), hashlib.sha256(raw).hexdigest(), len(raw)


def _date_text(value):
    _require(type(value) is str and len(value) == 24, 'owned /bin/date text length')
    for char, want in zip(value, 'dddd-dd-ddTdd:dd:dd+dddd'):
        if want == 'd':
            _require('0' <= char <= '9', 'owned date digit')
        elif want == '+':
            _require(char in '+-', 'owned date offset sign')
        else:
            _require(char == want, 'owned date separator')
    return value


def _slug(item):
    return ''.join(c if ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c in '-_') else '_'
                   for c in item)[:64] or 'item'


def _identity(meta, identity, digest, size):
    """Bind the reader's own completed observation to the expected created inode."""
    _require(type(meta) is dict and meta.get('completed') is True and meta.get('sha256') == digest
             and meta.get('bytes_seen') == size and meta.get('eof') is True, 'reader observation incomplete')
    after = meta.get('after')
    _require(type(after) is dict and type(identity) is dict and type(after.get('mode')) is int
             and stat.S_ISREG(after['mode']) and after.get('nlink') == 1 and after.get('size') == size
             and after.get('dev') == identity.get('dev') and after.get('ino') == identity.get('ino'),
             'observed inode is not the expected original created inode')


class _Call:
    """One invocation/accounting context bound to ONE original deadline predicate and ONE reader.

    Every callback and native operation is pre-checked and followed by the SAME original check on
    success or Exception; the primary event is retained before the check and a secondary deadline
    failure is retained separately. After a crossing no new callback or I/O starts; only one close
    attempt per already-owned descriptor remains permitted. BaseException marks the path unsafe.
    """

    def __init__(self, reader, deadline_check, causes, internal, phase):
        self.reader, self.deadline, self.allowed, self.internal, self.phase = (
            reader, deadline_check, causes, internal, phase)
        self.fired, self.evidence, self.suppressed = set(), {}, {}
        self.events, self.event_count, self.event_digest = [], 0, hashlib.sha256()
        self.reads, self.read_count, self.read_digest = [], 0, hashlib.sha256()
        self.crossed, self.unsafe = False, False
        self.live, self.acquired, self.closed, self.unresolved = {}, 0, 0, []

    def fire(self, cause, detail):
        if cause not in self.allowed:
            cause = self.internal
        self.fired.add(cause)
        values = self.evidence.setdefault(cause, [])
        if len(values) < MAX_EVIDENCE:
            values.append(_short(detail))
        else:
            self.suppressed[cause] = self.suppressed.get(cause, 0) + 1

    def ordered(self):
        return [cause for cause in self.allowed if cause in self.fired]

    def event(self, name, state, detail):
        row = {'callback': name, 'state': state, 'detail': _short(detail)}
        self.event_count += 1
        self.event_digest.update(_canonical(row))
        if len(self.events) < MAX_EVENTS:
            self.events.append(row)

    def tick(self, stage):
        """The ORIGINAL nonrenewing deadline predicate; never renewed, never re-armed."""
        if self.crossed:
            return False
        try:
            value = self.deadline()
        except Exception as exc:
            self.crossed = True
            self.event('deadline_check', 'CROSSED', stage + ': ' + _why(exc))
            self.fire(self.phase, stage + ': ' + _why(exc))
            return False
        except BaseException as exc:
            self.unsafe = True
            self.event('deadline_check', 'BASE_EXCEPTION', stage + ': ' + _why(exc))
            raise
        if value is not None:
            self.crossed = True
            self.event('deadline_check', 'CROSSED', stage + ': non-None return')
            self.fire(self.phase, stage + ': deadline_check returned non-None')
            return False
        return True

    def must(self, stage):
        if not self.tick(stage):
            raise _Crossed(stage)

    def observe(self, name, function, *args):
        """Only route for reader/CP2 callbacks: pre-check, call, retain primary, SAME check."""
        self.must(name + ' pre-check')
        try:
            value = function(*args)
        except Exception as primary:
            self.event(name, 'EXCEPTION', _why(primary))
            try:
                self.tick(name + ' Exception completion')
            except BaseException as secondary:
                if secondary is not primary and secondary.__context__ is None:
                    secondary.__context__ = primary
                raise
            raise
        except BaseException as primary:
            self.unsafe = True
            self.event(name, 'BASE_EXCEPTION', _why(primary))
            raise
        self.event(name, 'RETURNED', type(value).__name__)
        if not self.tick(name + ' successful completion'):
            raise _Crossed(name + ' returned after the original deadline')
        return value

    def read(self, path, cap):
        data = self.observe('read_bytes', self.reader.read_bytes, path, cap)
        row = {'path': path, 'cap': cap, 'type': type(data).__name__}
        if type(data) is bytes:
            row.update({'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        self.read_count += 1
        self.read_digest.update(_canonical(row))
        if len(self.reads) < MAX_READS:
            self.reads.append(row)
        _require(type(data) is bytes and len(data) <= cap, 'read_bytes wrong type or over cap')
        return data

    def native(self, stage, function, *args, retain=None, **kwargs):
        """Native blocking step: pre-check, call, retain ownership BEFORE the completion check."""
        self.must(stage + ' pre-check')
        try:
            value = function(*args, **kwargs)
        except Exception as primary:
            self.event('native', 'EXCEPTION', stage + ': ' + _why(primary))
            try:
                self.tick(stage + ' Exception completion')
            except BaseException as secondary:
                if secondary is not primary and secondary.__context__ is None:
                    secondary.__context__ = primary
                raise
            raise
        except BaseException as primary:
            self.unsafe = True
            self.event('native', 'BASE_EXCEPTION', stage + ': ' + _why(primary))
            raise
        if retain is not None:
            retain(value)
        if not self.tick(stage + ' completion'):
            raise _Crossed(stage + ' completed after the original deadline')
        return value

    def own(self, fd, display, owned):
        self.live[fd] = display
        self.acquired += 1
        owned.append(fd)

    def close(self, fd, cause):
        """At most ONE close attempt per owned descriptor; permitted after a crossing."""
        if fd not in self.live:
            return True
        display = self.live.pop(fd)
        try:
            os.close(fd)
        except BaseException as exc:
            if len(self.unresolved) < MAX_SAMPLE:
                self.unresolved.append({'fd': fd, 'path': display, 'error': _why(exc)})
            _LEDGER.record('caller-fd', display + ': ' + _why(exc))
            self.fire(cause, 'unresolved close ' + _short(display) + ': ' + _why(exc))
            if not isinstance(exc, Exception):
                self.unsafe = True
                self.event('close', 'BASE_EXCEPTION', display + ': ' + _why(exc))
                raise
            self.event('close', 'EXCEPTION', display + ': ' + _why(exc))
            return False
        self.closed += 1
        if not self.crossed:
            self.tick('close ' + _short(display) + ' completion')
        return True

    def release(self, owned, cause):
        """Nested cleanup: every owned descriptor gets one attempt even after a BaseException;
        the FIRST BaseException is re-raised only after all attempts (later ones keep context)."""
        first, clean = None, True
        for fd in reversed(owned):
            try:
                clean = self.close(fd, cause) and clean
            except BaseException as exc:
                clean = False
                if first is None:
                    first = exc
        if first is not None:
            raise first
        return clean


class _Ledger:
    """Process-lifetime parent ledger. Readers and unresolved records are appended, never removed.

    Descriptor/iterator uncertainty is per process: process exit closes them, so the in-memory
    history legitimately ends with the process; nothing here survives or is claimed across it.
    """

    def __init__(self):
        self.readers, self.recorded, self.recorded_total = [], [], 0

    def retain(self, reader):
        for index, known in enumerate(self.readers):
            if known is reader:
                return index
        self.readers.append(reader)
        return len(self.readers) - 1

    def record(self, source, detail):
        self.recorded_total += 1
        if len(self.recorded) < MAX_SAMPLE:
            self.recorded.append({'source': _short(source), 'detail': _short(detail)})

    def snapshot(self):
        """Union of every retained reader's report()['unresolved'] plus recorded entries.
        An unavailable or malformed report is itself unresolved. BaseException propagates."""
        rows, clean, unclean = [], self.recorded_total == 0, 0
        for index, reader in enumerate(self.readers):
            try:
                report = reader.report()
                unresolved = report.get('unresolved') if type(report) is dict else None
                valid = type(unresolved) is list and all(type(value) is int for value in unresolved)
                error = None if valid else 'report()["unresolved"] is not a list of int'
            except Exception as exc:
                unresolved, valid, error = None, False, _why(exc)
            if not valid or unresolved:
                clean = False
                unclean += 1
                if len(rows) < MAX_SAMPLE:
                    rows.append({'reader_index': index, 'report_error': error,
                                 'unresolved_count': len(unresolved) if valid else None,
                                 'unresolved_ids': list(unresolved[:MAX_SAMPLE]) if valid else None})
        return {'clean': clean, 'readers_retained': len(self.readers), 'readers_unclean': unclean,
                'reader_rows': rows, 'recorded_total': self.recorded_total, 'recorded': list(self.recorded)}


_LEDGER = _Ledger()
_MINT = object()
_EFFECTIVE = {}   # id(outcome) -> the identical RELEASED outcome (strong reference: ids never reused)
_LATCHED = set()  # ids of effective outcomes already consumed or refused by an account


def retain_reader(reader):
    """Retain an ORIGINAL parent reader for the process lifetime. Its unresolved resources then
    block every later CP1 release and accounting in this process. Returns its ledger index."""
    return _LEDGER.retain(reader)


def record_unresolved(source, detail):
    """Parent records any other unresolved resource; permanent for this process."""
    _LEDGER.record(source if type(source) is str else '<non-str source>',
                   detail if type(detail) is str else '<non-str detail>')


def resource_report():
    """Current global unresolved-resource union (JSON-shaped; carries no authority)."""
    return _LEDGER.snapshot()


class CallerOutcome:
    """Read-only CP1 outcome minted only inside this module. Holds the ORIGINAL reader and the
    ORIGINAL deadline predicate. A dict, copy, deserialized report or foreign object is never
    effective; only the identical RELEASED object registered after the final check is."""

    __slots__ = ('_fields', '_reader', '_deadline')

    def __init__(self, token, fields, reader, deadline_check):
        if token is not _MINT:
            raise TypeError('CallerOutcome is minted only by invoke_release')
        object.__setattr__(self, '_fields', fields)
        object.__setattr__(self, '_reader', reader)
        object.__setattr__(self, '_deadline', deadline_check)

    def __setattr__(self, name, value):
        raise AttributeError('CallerOutcome is read-only')

    def __delattr__(self, name):
        raise AttributeError('CallerOutcome is read-only')

    def __reduce_ex__(self, protocol):
        raise TypeError('CallerOutcome cannot be copied or serialized')

    def __copy__(self):
        raise TypeError('CallerOutcome cannot be copied')

    def __deepcopy__(self, memo):
        raise TypeError('CallerOutcome cannot be copied')

    @property
    def state(self):
        return self._fields['state']

    @property
    def effective(self):
        """Informative: minted RELEASED and not yet consumed/refused by an account."""
        return _EFFECTIVE.get(id(self)) is self and id(self) not in _LATCHED

    @property
    def reader(self):
        """The retained original reader (never replaced)."""
        return self._reader

    def report(self):
        """Detached JSON copy of the outcome record; carries no authority."""
        return _strict_json(_canonical(self._fields))


class _State:
    def __init__(self):
        self.stage, self.nonce, self.reader_index, self.owner, self.spec = 'S0', None, None, None, None
        self.prt = {'path': PRT3_PATH, 'sha256': PRT3_SHA256, 'bytes': PRT3_BYTES, 'loaded': False,
                    'invoked': False, 'returned': False, 'raised': None}
        self.union, self.served_before, self.identity = None, None, None
        self.result, self.result_document = None, None
        self.disposition, self.registry, self.receipt, self.resources = None, None, None, None
        self.uncertainty, self.releasable, self.final_check, self.prt_base = [], False, 'NOT_PERFORMED', False


def _step(call, cause, function, *args):
    """Run one owning predicate: Exception => owning cause (deadline cause already separate)."""
    try:
        return function(*args)
    except _Crossed:
        raise
    except Exception as exc:
        call.fire(cause, _why(exc))
        if call.crossed:
            raise _Crossed(cause)
        return None


def _check_reader(reader, deadline_check):
    for name in ('read_bytes', 'report', 'last_file'):
        _require(callable(getattr(reader, name, None)), 'reader.' + name + ' not callable')
    _require(getattr(reader, '_check', None) is deadline_check,
             'reader is not structurally bound to the identical original deadline predicate')
    return True


def _check_callbacks(census, owned_date, identity):
    _require(callable(census) and callable(owned_date), 'census/owned_date must be callable')
    _require(type(identity) is dict and set(identity) == {'union', 'census_log', 'evaluate_endedness'}
             and callable(identity['evaluate_endedness']), 'identity exact {union,census_log,evaluate_endedness}')
    return True


def _owner_core(entry):
    _text(entry['item'])
    allocation = entry['allocation']
    _require(type(allocation) is dict and set(allocation) == {'registry_path', 'line_sha256', 'record'},
             'allocation exact {registry_path,line_sha256,record}')
    _mutation_path(allocation['registry_path'])
    _require(_hex(allocation['line_sha256']), 'allocation line digest')
    record = allocation['record']
    _require(type(record) is dict and _exact(record.get('item'), entry['item'])
             and record.get('state') == 'RUNNING', 'allocation record RUNNING for exact item')
    reservation = entry['reservation']
    _require(type(reservation) is dict and set(reservation) == {'bytes', 'cpu_slots'}
             and _count(reservation['bytes']) and _count(reservation['cpu_slots']), 'reservation exact counts')
    _require(_exact(record.get('reservation_bytes'), reservation['bytes']), 'record reservation_bytes != reservation.bytes')


def _owner(value):
    owner = _detach(value, DOC_CAP)[0]
    _require(type(owner) is dict and set(owner) == OWNER_KEYS, 'owner exact keys')
    _owner_core(owner)
    _mutation_path(owner['commit_dir'])
    _mutation_path(owner['receipt_dir'])
    sources = owner['sources']
    _require(type(sources) is dict and set(sources) == {'caller', 'reader'}, 'sources exact {caller,reader}')
    _require(_ref(sources['caller'])['path'] == CALLER_PATH, 'caller source path')
    reader = _ref(sources['reader'])
    _require(reader['path'] == READER_PATH and reader['sha256'] == READER_SHA256, 'reader source pin')
    prerequisites = owner['prerequisites']
    _require(type(prerequisites) is dict and set(prerequisites) == set(PREREQUISITES), 'prerequisite exact name set')
    for name in PREREQUISITES:
        _ref(prerequisites[name])
    return owner


def _spec(value, owner):
    detached, digest, size = _detach(value, SPEC_CAP)
    _require(type(detached) is dict, 'spec object')
    for key in ('item', 'allocation', 'reservation'):
        _require(key in detached and _exact(detached[key], owner[key]), 'spec.' + key + ' not typed-equal owner')
    artifacts = detached.get('artifacts')
    job_dir = artifacts.get('job_dir') if type(artifacts) is dict else None
    _path(job_dir)  # absent/invalid job_dir => destination exclusion unprovable => refusal
    for key in ('commit_dir', 'receipt_dir'):
        _require(not _within(owner[key], job_dir), key + ' equal to or below the artifact job_dir')
    return {'detached': detached, 'sha256': digest, 'bytes': size}


def _served(call, log):
    """CP2 CensusLog served-snapshot count through the original-deadline callback wrapper."""
    value = call.observe('census_log served count', log.served_count)
    _require(_count(value), 'CP2 served count must be an exact nonnegative int')
    return value


def _union(call, state, identity):
    union = _detach(identity['union'], SPEC_CAP)[0]
    _require(type(union) is dict and union.get('format') == 'parent-release-identity-union-v1'
             and union.get('state') == 'CLOSED_CONDITIONAL' and _hex(union.get('union_sha256')),
             'CP2 union not CLOSED_CONDITIONAL v1 with digest')
    _require('identities' in state.spec['detached']
             and _exact(union.get('prt_identities'), state.spec['detached']['identities']),
             'spec.identities not typed-equal CP2 union.prt_identities')
    state.union, state.served_before = union, _served(call, identity['census_log'])
    return union


def _load_prt(call, state):
    _require(_hex(PRT3_SHA256) and PRT3_SHA256 not in FORBIDDEN_PRT_SHA256 and type(PRT3_BYTES) is int
             and 0 < PRT3_BYTES <= CAP, 'PRT3 pin invalid or forbidden (no v1/v2 fallback)')
    data = call.read(PRT3_PATH, PRT3_BYTES)
    _require(len(data) == PRT3_BYTES and hashlib.sha256(data).hexdigest() == PRT3_SHA256,
             'PRT3 bytes differ from the pin')
    namespace = {'__name__': 'parent_release_v3_pinned', '__file__': PRT3_PATH}
    exec(compile(data, PRT3_PATH, 'exec', dont_inherit=True), namespace)  # exactly the verified bytes
    call.must('S4 pinned PRT3 definitions completion')
    entry = namespace.get('decide_and_commit')
    _require(callable(entry), 'pinned PRT3 decide_and_commit missing')
    state.prt['loaded'] = True
    return entry


def _sources(call, owner):
    for key in ('caller', 'reader'):
        ref = owner['sources'][key]
        data = call.read(ref['path'], CAP)
        _require(hashlib.sha256(data).hexdigest() == ref['sha256'], key + ' source bytes differ from declared pin')
    return True


def _prerequisite(call, owner, name):
    ref = owner['prerequisites'][name]
    data = call.read(ref['path'], DOC_CAP)
    _require(hashlib.sha256(data).hexdigest() == ref['sha256'], 'attestation digest')
    doc = _strict_json(data)
    _require(type(doc) is dict and doc.get('format') == PREREQUISITE_FORMAT and doc.get('prerequisite') == name
             and _exact(doc.get('item'), owner['item'])
             and doc.get('allocation_line_sha256') == owner['allocation']['line_sha256']
             and doc.get('status') == PREREQUISITE_STATUS, 'attestation fields')


def _prerequisites(call, owner):
    for name in PREREQUISITES:
        try:
            _prerequisite(call, owner, name)
        except _Crossed:
            raise
        except Exception as exc:
            call.fire('CP1_PREREQUISITE_MISSING', name + ': ' + _why(exc))
            if call.crossed:
                raise _Crossed(name)


def _result_shape(result):
    _require(type(result) is dict and set(result) == RESULT_KEYS, 'v3 result exact key set')
    _require(result['format'] == RESULT_FORMAT, 'result format')
    _require(result['state'] in ('RELEASED', 'HELD') and result['decision'] in ('RELEASED', 'HELD'), 'state/decision')
    _require(type(result['release_effective']) is bool and type(result['original_deadline_crossed']) is bool,
             'exact bool fields')
    _require(result['ack'] in ACK_STATES and result['final_deadline_check'] in FINAL_CHECKS, 'ack/final check')
    registry = result['registry']
    _require(type(registry) is dict and RESULT_REGISTRY_KEYS <= set(registry)
             and set(registry) <= RESULT_REGISTRY_KEYS | RESULT_REGISTRY_OPTIONAL, 'registry result keys')
    disposition = result['disposition']
    _require(disposition is None or (type(disposition) is dict and set(disposition) == RESULT_DISPOSITION_KEYS),
             'disposition result keys')
    resources = result['resources']
    _require(type(resources) is dict and set(resources) == RESULT_RESOURCE_KEYS
             and all(_count(resources[key]) for key in ('acquired', 'closed', 'live', 'unresolved_total'))
             and type(resources['unresolved']) is list, 'resources shape')
    _require(type(result['causes']) is list and all(type(cause) is str for cause in result['causes'])
             and type(result['parts']) is dict, 'causes/parts shape')


def _result(state, value):
    """Detach and shape-check a returned/attached PRT3 result; record its resources globally."""
    try:
        detached, digest, size = _detach(value, RESULT_CAP)
        _result_shape(detached)
    except Exception:
        _LEDGER.record('prt3', 'result malformed or not detachable; PRT3 resource state unknown')
        raise
    resources = detached['resources']
    state.result_document = detached
    state.result = {'format': detached['format'], 'sha256': digest, 'bytes': size, 'state': detached['state'],
                    'decision': detached['decision'], 'release_effective': detached['release_effective'],
                    'ack': detached['ack'], 'registry_status': detached['registry']['status'],
                    'registry_state': detached['registry']['state'],
                    'final_deadline_check': detached['final_deadline_check'],
                    'live': resources['live'], 'unresolved_total': resources['unresolved_total']}
    if resources['live'] or resources['unresolved_total'] or resources['unresolved']:
        _LEDGER.record('prt3', 'PRT3 reported live=%d unresolved_total=%d'
                       % (resources['live'], resources['unresolved_total']))
    return detached


def _not_released(result, owner):
    """Every predicate of a COMPLETE returned RELEASED result; returns the failing names."""
    registry, disposition, resources = result['registry'], result['disposition'], result['resources']
    checks = (
        ('state', result['state'] == 'RELEASED'),
        ('decision', result['decision'] == 'RELEASED'),
        ('release_effective', result['release_effective'] is True),
        ('ack', result['ack'] == 'ACK_OK'),
        ('final_deadline_check', result['final_deadline_check'] == 'PASSED'),
        ('original_deadline_crossed', result['original_deadline_crossed'] is False),
        ('causes', _exact(result['causes'], [])),
        ('parts', _exact(result['parts'], PARTS_PASS)),
        ('uncertainty', result['uncertainty'] is None),
        ('authority_flags', result['runtime_authority'] is False and result['scientific_authority'] is False),
        ('registry', registry['status'] == 'APPENDED' and registry['state'] == 'RELEASED'
         and registry['fsync'] is True and registry['closed'] is True and registry['line_complete'] is True
         and _hex(registry['line_sha256']) and registry.get('path') == owner['allocation']['registry_path']
         and 'detail' not in registry and _count(registry['bytes_written']) and registry['bytes_written'] > 0),
        ('disposition', disposition is not None and disposition['create_attempted'] is True
         and disposition['created'] is True and disposition['line_complete'] is True
         and disposition['file_fsync'] is True and disposition['directory_fsync'] is True
         and _hex(disposition['sha256']) and _count(disposition['bytes']) and disposition['bytes'] > 0
         and _exact(disposition['bytes_written'], disposition['bytes']) and type(disposition['path']) is str
         and type(disposition['identity']) is dict and set(disposition['identity']) == {'dev', 'ino'}
         and _count(disposition['identity']['dev']) and _count(disposition['identity']['ino'])
         and disposition['identity']['ino'] > 0),
        ('resources', resources['live'] == 0 and resources['unresolved_total'] == 0
         and resources['unresolved'] == []),
    )
    return [name for name, passed in checks if not passed]


def _endedness(call, state, identity):
    """CP2 join after the RELEASED return: endedness over the snapshots served during this call."""
    value = call.observe('evaluate_endedness', identity['evaluate_endedness'], state.union,
                         identity['census_log'], call.deadline)
    ended, digest, size = _detach(value, RESULT_CAP)
    _require(type(ended) is dict and ended.get('format') == 'parent-release-identity-endedness-v1'
             and ended.get('state') == 'ENDED_CONDITIONAL' and _exact(ended.get('causes'), [])
             and _hex(ended.get('endedness_sha256')), 'CP2 endedness not ENDED_CONDITIONAL v1')
    _require(ended.get('union_sha256') == state.union['union_sha256'],
             'endedness does not echo the evaluated union digest')
    served = _served(call, identity['census_log'])
    _require(served == state.served_before + 1,
             'not exactly one served census snapshot during this PRT3 call')
    state.identity = {'union_format': state.union['format'], 'union_sha256': state.union['union_sha256'],
                      'endedness_format': ended['format'], 'endedness_sha256': ended['endedness_sha256'],
                      'endedness_document_sha256': digest, 'endedness_document_bytes': size,
                      'served_before': state.served_before, 'served_after': served,
                      'origin': 'CP2 callables/log parent-supplied; provenance is prerequisite identity_union_census_cp2'}
    return state.identity


def _disposition(call, state, result):
    owner, record = state.owner, result['disposition']
    name = DISPOSITION_PREFIX + _slug(owner['item']) + '-' + record['sha256'] + '.json'
    _require(record['path'] == owner['commit_dir'] + '/' + name, 'disposition path is not the exact commit_dir name')
    data = call.read(record['path'], record['bytes'])
    _require(len(data) == record['bytes'] and hashlib.sha256(data).hexdigest() == record['sha256'],
             'disposition bytes/digest')
    _identity(call.observe('last_file', call.reader.last_file, record['path']), record['identity'],
              record['sha256'], record['bytes'])
    doc = _strict_json(data)
    _require(type(doc) is dict and doc.get('format') == DISPOSITION_FORMAT and doc.get('module') == PRT_MODULE
             and doc.get('scope_contract_sha256') == PRT_CONTRACT_SHA256
             and _exact(doc.get('repair_scope_sha256s'), PRT_REPAIR_SCOPES), 'disposition v3 format/module/scopes')
    _require(_exact(doc.get('item'), owner['item']) and doc.get('state') == 'RELEASED'
             and _exact(doc.get('causes'), []) and _exact(doc.get('parts'), PARTS_PASS),
             'disposition is not complete RELEASED for this item')
    _require(doc.get('spec_sha256') == state.spec['sha256'] and _exact(doc.get('spec_bytes'), state.spec['bytes']),
             'disposition spec digest differs from the caller-detached spec')
    _require(_exact(doc.get('reservation'), owner['reservation']) and doc.get('runtime_authority') is False
             and doc.get('scientific_authority') is False, 'disposition reservation/authority flags')
    state.disposition = {'path': record['path'], 'sha256': record['sha256'], 'bytes': record['bytes'],
                         'dev': record['identity']['dev'], 'ino': record['identity']['ino'],
                         'recorded_at': _date_text(doc.get('recorded_at'))}
    return state.disposition


def _registry(call, state, result):
    owner = state.owner
    allocation = owner['allocation']
    path, target = allocation['registry_path'], result['registry']['line_sha256']
    raw = call.read(path, CAP)
    _require(raw.endswith(b'\n'), 'registry empty or torn tail')
    rows, allocated, targets = [], [], []
    for index, line in enumerate(raw[:-1].split(b'\n')):
        row = _strict_json(line)
        _require(type(row) is dict, 'registry line is not a JSON object')
        digest = hashlib.sha256(line).hexdigest()
        if digest == allocation['line_sha256']:
            allocated.append(index)
        if digest == target:
            targets.append(index)
        rows.append(row)
    _require(len(allocated) == 1 and len(targets) == 1 and allocated[0] < targets[0],
             'unique allocation line followed by the unique returned registry line')
    _require(_exact(rows[allocated[0]], allocation['record']), 'allocation line not typed-equal record')
    row = rows[targets[0]]
    _require(set(row) == REGISTRY_ROW_KEYS and row['format'] == REGISTRY_FORMAT and row['owner'] == PRT_MODULE,
             'returned registry row is not v3')
    _require(_exact(row['item'], owner['item']) and row['state'] == 'RELEASED'
             and row['decision_in_disposition'] == 'RELEASED' and _exact(row['causes'], [])
             and _exact(row['remaining_output_reservation_bytes'], 0), 'returned registry row not RELEASED')
    _require(row['disposition'] == state.disposition['path'] and row['disposition_sha256'] == state.disposition['sha256']
             and row['allocation_line_sha256'] == allocation['line_sha256']
             and row['recorded_at'] == state.disposition['recorded_at']
             and _exact(row['reservation'], owner['reservation']), 'returned registry row binding')
    for index in range(allocated[0] + 1, len(rows)):
        other = rows[index]
        if index == targets[0] or not _exact(other.get('item'), owner['item']):
            continue
        _require(index < targets[0] and other.get('format') == REGISTRY_FORMAT and other.get('state') == 'HELD'
                 and other.get('allocation_line_sha256') == allocation['line_sha256'],
                 'another same-item row after the allocation (only earlier v3 HELD rows allowed)')
    state.registry = {'path': path, 'observed_bytes': len(raw), 'observed_sha256': hashlib.sha256(raw).hexdigest(),
                      'allocation_line_index': allocated[0], 'line_index': targets[0], 'line_sha256': target}
    return state.registry


def _joined(call, state, stage):
    snapshot = _LEDGER.snapshot()
    state.resources = snapshot
    if not call.tick(stage + ' global resource join completion'):
        return False
    if snapshot['clean'] is not True or call.live or call.unresolved:
        call.fire('CP1_UNRESOLVED_RESOURCES', stage + ': retained reader/recorded/caller resources unresolved')
        return False
    return True


def _prepare_receipt(state):
    owner = state.owner
    document = {
        'format': RECEIPT_FORMAT, 'module': MODULE, 'scope_sha256': SCOPE_SHA256,
        'design_checkpoint_sha256': DESIGN_CHECKPOINT_SHA256, 'invocation_nonce': state.nonce,
        'reader_ledger_index': state.reader_index, 'item': owner['item'], 'allocation': owner['allocation'],
        'reservation': owner['reservation'], 'commit_dir': owner['commit_dir'],
        'spec': {'sha256': state.spec['sha256'], 'bytes': state.spec['bytes']},
        'prt': {'path': PRT3_PATH, 'sha256': PRT3_SHA256, 'bytes': PRT3_BYTES, 'entry': 'decide_and_commit',
                'executed_from_verified_bytes': True},
        'sources_declared': owner['sources'],
        'sources_note': 'disk bytes hash-verified through the original reader; the running caller and reader '
                        'code identity is not provable by this source (prerequisite callback_provenance)',
        'prerequisites': owner['prerequisites'], 'prerequisite_origin': PREREQUISITE_ORIGIN,
        'identity': state.identity,
        'result': {'format': RESULT_FORMAT, 'sha256': state.result['sha256'], 'bytes': state.result['bytes'],
                   'state': 'RELEASED', 'ack': 'ACK_OK', 'final_deadline_check': 'PASSED'},
        'disposition': state.disposition, 'registry': state.registry,
        'resources': {'snapshot_sha256': hashlib.sha256(_canonical(state.resources)).hexdigest(),
                      'clean': True, 'readers_retained': state.resources['readers_retained']},
        'observed': 'PRT3_RETURNED_COMPLETE_RELEASED_CP2_ENDED_CONDITIONAL_READBACKS_MATCHED',
        'disposition_recorded_at': state.disposition['recorded_at'],
        'timestamp_note': 'copied owned /bin/date text from the PRT3 disposition; this module reads no clock',
        'release_effect': RECEIPT_EFFECT, 'runtime_authority': False, 'scientific_authority': False}
    data = _canonical(document)
    _require(len(data) < RECEIPT_CAP, 'receipt cap')
    digest = hashlib.sha256(data).hexdigest()
    name = RECEIPT_PREFIX + _slug(owner['item']) + '-' + digest + '.json'
    state.receipt = {'path': owner['receipt_dir'] + '/' + name, 'name': name, 'sha256': digest, 'bytes': len(data),
                     'create_attempted': False, 'created': False, 'identity': None, 'bytes_written': 0,
                     'complete': False, 'file_fsync': False, 'readback': False, 'closed': False,
                     'directory_fsync': False, 'handles_clean': None, 'ack': 'ACK_NOT_ATTEMPTED'}
    return data


def _anchored_directory(call, parts, owned):
    fd = call.native('receipt dir open /', os.open, '/', DIR_FLAGS,
                     retain=lambda value: call.own(value, '/', owned))
    location = ''
    for part in parts:
        location += '/' + part
        nxt = call.native('receipt dir open ' + location, os.open, part, DIR_FLAGS, dir_fd=fd,
                          retain=lambda value, where=location: call.own(value, where, owned))
        if not call.close(fd, 'CP1_RECEIPT_WRITE'):
            raise CallerRefusal('receipt directory walk close unresolved')
        fd = nxt
    return fd


def _write_receipt(call, state, data):
    """ONE exclusive receipt: anchored NOFOLLOW walk, O_CREAT|O_EXCL|O_NOFOLLOW 0444, every native
    completion followed by the original check, readback, one close per handle, directory fsync.
    Never overwrites, removes or repairs; partial bytes stay preserved and are never authority."""
    progress, owned = state.receipt, []
    try:
        directory = _anchored_directory(call, _mutation_path(state.owner['receipt_dir']), owned)
        progress['create_attempted'] = True  # an O_EXCL object may exist even if no fd is retained
        fd = call.native('receipt exclusive create', os.open, progress['name'], NEW_FILE_FLAGS, 0o444,
                         dir_fd=directory, retain=lambda value: call.own(value, progress['path'], owned))
        progress['created'] = True
        info = call.native('receipt created fstat', os.fstat, fd)
        _require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1 and info.st_ino > 0 and info.st_size == 0,
                 'receipt is not a new empty regular one-link inode')
        progress['identity'] = {'dev': info.st_dev, 'ino': info.st_ino}
        view, written, calls = memoryview(data), 0, 0
        while written < len(data):
            calls += 1
            _require(calls <= MAX_NATIVE_CALLS, 'receipt write call cap')
            count = call.native('receipt write', os.write, fd, view[written:])
            _require(type(count) is int and 0 < count <= len(data) - written, 'zero/invalid receipt write')
            written += count
            progress['bytes_written'] = written
        progress['complete'] = True
        call.native('receipt file fsync', os.fsync, fd)
        progress['file_fsync'] = True
        chunks, seen, calls = [], 0, 0
        while seen < len(data):
            calls += 1
            _require(calls <= MAX_NATIVE_CALLS, 'receipt readback call cap')
            block = call.native('receipt pread', os.pread, fd, min(CHUNK, len(data) - seen), seen)
            _require(type(block) is bytes and 0 < len(block) <= len(data) - seen, 'short/invalid receipt pread')
            chunks.append(block)
            seen += len(block)
        _require(b''.join(chunks) == data, 'receipt readback differs')
        after = call.native('receipt final fstat', os.fstat, fd)
        _require(stat.S_ISREG(after.st_mode) and after.st_dev == info.st_dev and after.st_ino == info.st_ino
                 and after.st_nlink == 1 and after.st_size == len(data), 'receipt inode changed')
        progress['readback'] = True
        progress['closed'] = call.close(fd, 'CP1_RECEIPT_WRITE')
        _require(progress['closed'], 'receipt close unresolved')
        call.native('receipt directory fsync', os.fsync, directory)
        progress['directory_fsync'] = True
    finally:
        progress['handles_clean'] = call.release(owned, 'CP1_RECEIPT_WRITE')


def _ack_receipt(call, state, data):
    progress = state.receipt
    progress['ack'] = 'ACK_ATTEMPTED'
    back = call.read(progress['path'], len(data))
    _require(back == data and hashlib.sha256(back).hexdigest() == progress['sha256'], 'receipt ACK bytes/digest')
    _identity(call.observe('last_file', call.reader.last_file, progress['path']), progress['identity'],
              progress['sha256'], len(data))
    progress['ack'] = 'ACK_OK'


def _invoke(call, state, entry, census, owned_date):
    state.prt['invoked'] = True
    try:
        value = entry(state.spec['detached'], call.reader.read_bytes, census, owned_date,
                      state.owner['commit_dir'], call.deadline)
    except Exception as exc:
        state.prt['raised'] = 'EXCEPTION'
        call.event('decide_and_commit', 'EXCEPTION', _why(exc))
        call.fire('CP1_PRT_EXCEPTION', _why(exc))
        _attached(state, exc)
        call.tick('PRT3 Exception completion')
        return None
    except BaseException as exc:
        state.prt['raised'], state.prt_base, call.unsafe = 'BASE_EXCEPTION', True, True
        call.event('decide_and_commit', 'BASE_EXCEPTION', _why(exc))
        call.fire('CP1_PRT_BASE_EXCEPTION', _why(exc))
        _attached(state, exc)
        raise
    state.prt['returned'] = True
    call.event('decide_and_commit', 'RETURNED', type(value).__name__)
    return value


def _attached(state, exc):
    """Pure in-memory: retain an attached PRT3 report (never as release) and its resources."""
    try:
        attached = getattr(exc, 'parent_release_result', None)
    except Exception:
        attached = None
    if attached is None:
        _LEDGER.record('prt3', 'PRT3 raised without parent_release_result; resource report unavailable')
        return
    try:
        _result(state, attached)
    except Exception:
        pass  # _result already recorded the unknown PRT3 resource state


def _run(call, state, owner, spec, census, owned_date, identity):
    state.stage = 'S1'
    if not callable(call.deadline):
        call.fire('CP1_CALLBACKS_INVALID', 'deadline_check not callable; no callback or I/O attempted')
        return
    reader_ok = _step(call, 'CP1_READER_INVALID', _check_reader, call.reader, call.deadline) is True
    identity_ok = _step(call, 'CP1_CALLBACKS_INVALID', _check_callbacks, census, owned_date, identity) is True
    state.nonce = call.native('S1 invocation nonce', os.urandom, 32).hex()
    state.stage = 'S2'
    state.owner = _step(call, 'CP1_OWNER_INVALID', _owner, owner)
    if state.owner is not None:
        state.stage = 'S3'
        state.spec = _step(call, 'CP1_SPEC_BINDING', _spec, spec, state.owner)
    if state.spec is not None and identity_ok:
        state.stage = 'S3b'
        _step(call, 'CP1_IDENTITY_UNION', _union, call, state, identity)
    entry = None
    if reader_ok:
        state.stage = 'S4'
        entry = _step(call, 'CP1_PRT_SOURCE', _load_prt, call, state)
        if state.owner is not None:
            state.stage = 'S5'
            _step(call, 'CP1_SOURCE_PINS', _sources, call, state.owner)
            state.stage = 'S6'
            _prerequisites(call, state.owner)
    if call.fired or entry is None or state.spec is None or state.union is None:
        state.uncertainty.append('pre-invocation refusal: PRT3 not invoked; this module wrote nothing')
        return
    state.stage = 'S7'
    call.must('S7 pre-invocation')
    call.phase = 'CP1_DEADLINE_POST_RESULT'
    returned = _invoke(call, state, entry, census, owned_date)
    if not state.prt['returned'] or call.crossed:
        return
    state.stage = 'S8'
    result = _step(call, 'CP1_RESULT_INVALID', _result, state, returned)
    if not call.tick('S8 PRT3 return and result detach completion') or result is None:
        return
    missing = _not_released(result, state.owner)
    if missing:
        call.fire('CP1_RESULT_NOT_RELEASED', 'returned result not complete RELEASED: ' + ','.join(missing))
        if 'resources' in missing:
            call.fire('CP1_UNRESOLVED_RESOURCES', 'PRT3 returned live/unresolved resources')
        return
    state.stage = 'S8b'
    if _step(call, 'CP1_ENDEDNESS', _endedness, call, state, identity) is None:
        return
    state.stage = 'S9'
    if _step(call, 'CP1_DISPOSITION_READBACK', _disposition, call, state, result) is None:
        return
    state.stage = 'S10'
    if _step(call, 'CP1_REGISTRY_READBACK', _registry, call, state, result) is None:
        return
    state.stage = 'S11'
    if not _joined(call, state, 'S11'):
        return
    state.stage = 'S12'
    call.must('S12 pre-receipt')
    call.phase = 'CP1_DEADLINE_RECEIPT'
    state.stage = 'S13'
    data = _step(call, 'CP1_RECEIPT_WRITE', _prepare_receipt, state)
    if data is None:
        return
    _step(call, 'CP1_RECEIPT_WRITE', _write_receipt, call, state, data)
    if call.fired or state.receipt.get('handles_clean') is not True:
        return
    state.stage = 'S14'
    _step(call, 'CP1_RECEIPT_ACK', _ack_receipt, call, state, data)
    if call.fired:
        return
    state.stage = 'S15'
    if not _joined(call, state, 'S15'):
        return
    state.releasable = True


def _notes(state):
    result = state.result or {}
    if result.get('registry_state') == 'RELEASED' or result.get('decision') == 'RELEASED':
        state.uncertainty.append('PRT3 RELEASED disposition/registry bytes may exist; CP1 did not complete '
                                 'observation, CP2 join, receipt and final check, so they are NOT authority; '
                                 'reservation stays HELD; preserve every object')
    if state.receipt is not None and state.receipt.get('create_attempted'):
        state.uncertainty.append('a partial or complete caller receipt may exist; it is NOT authority; preserve it')
    if state.prt['invoked'] and not state.prt['returned']:
        state.uncertainty.append('PRT3 did not return normally; partial disposition/registry bytes may exist')


def _fields(call, state, outcome_state):
    owner = state.owner if state.owner is not None else {}
    return {
        'format': OUTCOME_FORMAT, 'module': MODULE, 'scope_sha256': SCOPE_SHA256,
        'design_checkpoint_sha256': DESIGN_CHECKPOINT_SHA256, 'state': outcome_state,
        'invocation_nonce': state.nonce, 'reader_ledger_index': state.reader_index,
        'item': owner.get('item'), 'allocation': owner.get('allocation'), 'reservation': owner.get('reservation'),
        'commit_dir': owner.get('commit_dir'), 'receipt_dir': owner.get('receipt_dir'),
        'sources': owner.get('sources'), 'prerequisites': owner.get('prerequisites'),
        'prerequisite_origin': PREREQUISITE_ORIGIN,
        'spec': None if state.spec is None else {'sha256': state.spec['sha256'], 'bytes': state.spec['bytes']},
        'prt': dict(state.prt), 'identity': state.identity, 'result': state.result,
        'result_document': state.result_document, 'disposition': state.disposition, 'registry': state.registry,
        'receipt': state.receipt, 'causes': call.ordered(),
        'evidence': {cause: list(values) for cause, values in call.evidence.items()},
        'suppressed_evidence_counts': dict(call.suppressed), 'stage': state.stage,
        'original_deadline_crossed': call.crossed, 'unsafe_callback_path': call.unsafe,
        'final_deadline_check': state.final_check, 'events': list(call.events), 'event_count': call.event_count,
        'event_sha256': call.event_digest.hexdigest(), 'reads': list(call.reads), 'read_count': call.read_count,
        'read_sha256': call.read_digest.hexdigest(),
        'resources': {'caller': {'acquired': call.acquired, 'closed': call.closed, 'live': len(call.live),
                                 'unresolved': list(call.unresolved)}, 'global': state.resources},
        'uncertainty': list(state.uncertainty), 'release_effect': OUTCOME_EFFECT, 'boundary': BOUNDARY,
        'runtime_authority': False, 'scientific_authority': False, 'admission': ADMISSION}


def _held(call, state):
    _notes(state)
    return CallerOutcome(_MINT, _fields(call, state, 'HELD'), call.reader, call.deadline)


def _finalize(call, state):
    call.phase = 'CP1_DEADLINE_FINAL'
    if state.releasable and not call.fired and not call.crossed and not call.unsafe and not call.live:
        fields = _fields(call, state, 'RELEASED')
        if call.tick('S16 complete outcome assembly'):  # last check; only O(1) registration follows
            fields['final_deadline_check'] = 'PASSED'
            outcome = CallerOutcome(_MINT, fields, call.reader, call.deadline)
            _EFFECTIVE[id(outcome)] = outcome
            return outcome
        state.final_check = 'CROSSED'
    return _held(call, state)


def _raise_held(call, state, exc):
    call.unsafe = True
    if not state.prt_base:
        call.fire('CP1_BASE_EXCEPTION', _why(exc))
    try:
        outcome = _held(call, state)
    except Exception:
        outcome = None
    try:
        exc.parent_release_caller_outcome = outcome
    except Exception:
        pass
    raise exc


def invoke_release(owner, spec, reader, census, owned_date, deadline_check, identity):
    """CP1: one pinned PRT3 invocation plus caller observation and ONE exclusive receipt.

    owner: exact {item, allocation, reservation, commit_dir, receipt_dir, sources{caller,reader},
    prerequisites{<PREREQUISITES>: ref}}. spec: the PRT3 spec (detached here; item/allocation/
    reservation typed-equal owner). reader: the ORIGINAL pinned EvidenceReader built with this
    exact deadline_check; retained for the process lifetime FIRST. census/owned_date: passed to
    PRT3 unchanged (census must be the CP2 make_census callable paired with identity.census_log).
    identity: exact {union, census_log, evaluate_endedness} from CP2. deadline_check: the ORIGINAL
    nonrenewing predicate. Returns a CallerOutcome; RELEASED only when every step completed and
    the final original-deadline check passed. Any refusal returns HELD. A non-Exception
    BaseException propagates with exc.parent_release_caller_outcome (HELD) after one-close cleanup.
    """
    reader_index = _LEDGER.retain(reader)  # FIRST: the original reader is never dropped
    call = _Call(reader, deadline_check, CAUSES, 'CP1_INTERNAL_ERROR', 'CP1_DEADLINE_PRE_INVOKE')
    state = _State()
    state.reader_index = reader_index
    try:
        _run(call, state, owner, spec, census, owned_date, identity)
    except _Crossed:
        pass
    except Exception as exc:
        call.fire('CP1_INTERNAL_ERROR', _why(exc))
    except BaseException as exc:
        _raise_held(call, state, exc)
    try:
        return _finalize(call, state)
    except Exception as exc:
        call.fire('CP1_INTERNAL_ERROR', _why(exc))
        state.releasable = False
        return _held(call, state)
    except BaseException as exc:
        state.final_check = 'BASE_EXCEPTION' if state.releasable else state.final_check
        _raise_held(call, state, exc)


def _account_checks(call, account, fields, receipt_ref):
    key = fields['allocation']['line_sha256']
    entry = account._held.get(key)
    if entry is None or not (_exact(entry['item'], fields['item']) and _exact(entry['allocation'], fields['allocation'])
                             and _exact(entry['reservation'], fields['reservation'])):
        call.fire('AC_NOT_HELD', 'allocation not held here with identical item/allocation/reservation')
        return None
    receipt = fields['receipt']
    try:
        ref = _detach(receipt_ref, DOC_CAP)[0]
        _require(type(ref) is dict and set(ref) == {'path', 'sha256'} and ref['path'] == receipt['path']
                 and ref['sha256'] == receipt['sha256'], 'receipt_ref differs from the outcome receipt')
    except Exception as exc:
        call.fire('AC_RECEIPT_REF_INVALID', _why(exc))
        return None
    try:
        data = call.read(receipt['path'], receipt['bytes'])
        _require(hashlib.sha256(data).hexdigest() == receipt['sha256'], 'receipt bytes differ')
        _identity(call.observe('last_file', call.reader.last_file, receipt['path']), receipt['identity'],
                  receipt['sha256'], receipt['bytes'])
        doc = _strict_json(data)
        _require(type(doc) is dict and doc.get('format') == RECEIPT_FORMAT and doc.get('module') == MODULE
                 and doc.get('invocation_nonce') == fields['invocation_nonce']
                 and _exact(doc.get('item'), fields['item']) and _exact(doc.get('allocation'), fields['allocation'])
                 and _exact(doc.get('reservation'), fields['reservation'])
                 and _exact(doc.get('prt'), {'path': PRT3_PATH, 'sha256': PRT3_SHA256, 'bytes': PRT3_BYTES,
                                             'entry': 'decide_and_commit', 'executed_from_verified_bytes': True})
                 and type(doc.get('result')) is dict and doc['result'].get('sha256') == fields['result']['sha256']
                 and _exact(doc.get('identity'), fields['identity'])
                 and _exact(doc.get('disposition'), fields['disposition'])
                 and _exact(doc.get('registry'), fields['registry']), 'receipt does not bind this outcome')
    except _Crossed:
        raise
    except Exception as exc:
        call.fire('AC_RECEIPT_READBACK', _why(exc))
        return None
    snapshot = _LEDGER.snapshot()
    if not call.tick('account global resource join completion'):
        return None
    if snapshot['clean'] is not True:
        call.fire('AC_UNRESOLVED_RESOURCES', 'retained reader/recorded/caller resources unresolved')
        return None
    return key


def _account(account, outcome, receipt_ref):
    record = {'format': ACCOUNT_FORMAT, 'module': MODULE, 'state': 'HELD', 'item': None,
              'allocation_line_sha256': None, 'invocation_nonce': None, 'receipt': None,
              'released': {'bytes': 0, 'cpu_slots': 0}, 'causes': [], 'evidence': {},
              'final_deadline_check': 'NOT_PERFORMED', 'admission': ADMISSION, 'boundary': BOUNDARY}
    if type(outcome) is not CallerOutcome or _EFFECTIVE.get(id(outcome)) is not outcome:
        record['causes'] = ['AC_OUTCOME_NOT_EFFECTIVE']
        record['evidence'] = {'AC_OUTCOME_NOT_EFFECTIVE': ['not the identical minted RELEASED CallerOutcome; '
                                                           'dicts, copies, reports and disk bytes are never accounted']}
        return record
    if id(outcome) in _LATCHED:
        record['causes'] = ['AC_OUTCOME_LATCHED']
        record['evidence'] = {'AC_OUTCOME_LATCHED': ['outcome already consumed or refused; no second accounting']}
        return record
    _LATCHED.add(id(outcome))  # latched FIRST: this call accounts once or the outcome stays HELD forever
    fields = outcome._fields
    record.update({'item': fields['item'], 'allocation_line_sha256': fields['allocation']['line_sha256'],
                   'invocation_nonce': fields['invocation_nonce']})
    call = _Call(outcome._reader, outcome._deadline, ACCOUNT_CAUSES, 'AC_INTERNAL_ERROR', 'AC_DEADLINE')
    try:
        call.must('account start')
        key = _account_checks(call, account, fields, receipt_ref)
        if key is not None and not call.fired:
            accounted = dict(record)
            accounted.update({'state': 'RELEASED_ACCOUNTED', 'final_deadline_check': 'PASSED',
                              'released': {'bytes': fields['reservation']['bytes'],
                                           'cpu_slots': fields['reservation']['cpu_slots']},
                              'receipt': {'path': fields['receipt']['path'], 'sha256': fields['receipt']['sha256']}})
            returned = _strict_json(_canonical(accounted))
            if call.tick('account final assembly'):  # last check; only O(1) ledger moves follow
                del account._held[key]
                account._released[key] = accounted
                return returned
            record['final_deadline_check'] = 'CROSSED'
    except _Crossed:
        pass
    except Exception as exc:
        call.fire('AC_INTERNAL_ERROR', _why(exc))
    except BaseException as exc:
        call.fire('AC_BASE_EXCEPTION', _why(exc))
        record.update({'causes': call.ordered(),
                       'evidence': {cause: list(values) for cause, values in call.evidence.items()}})
        try:
            exc.parent_release_account_record = record
        except Exception:
            pass
        raise
    record.update({'causes': call.ordered(),
                   'evidence': {cause: list(values) for cause, values in call.evidence.items()}})
    return record


class ReservationAccount:
    """Parent reservation accounting only: no scheduler, no admission, no grant.

    hold() registers an allocation's reservation as HELD. release() moves exactly that reservation
    to released ONLY from the identical minted RELEASED CallerOutcome plus its receipt_ref, with a
    fresh receipt readback under the outcome's retained ORIGINAL deadline (no new deadline is
    accepted). Every refusal latches the outcome HELD. Registry/disposition/receipt bytes alone,
    result dicts and outcome reports are never accounted.
    """

    def __init__(self):
        self._held, self._released = {}, {}

    def hold(self, item, allocation, reservation):
        entry = _detach({'item': item, 'allocation': allocation, 'reservation': reservation}, DOC_CAP)[0]
        _owner_core(entry)
        key = entry['allocation']['line_sha256']
        _require(key not in self._held and key not in self._released, 'allocation already held or released here')
        self._held[key] = entry

    def release(self, outcome, receipt_ref):
        return _account(self, outcome, receipt_ref)

    def report(self):
        held = list(self._held.values())
        return {'format': ACCOUNT_FORMAT + '-report', 'admission': ADMISSION,
                'held': [_strict_json(_canonical(entry)) for entry in held],
                'held_totals': {'bytes': sum(entry['reservation']['bytes'] for entry in held),
                                'cpu_slots': sum(entry['reservation']['cpu_slots'] for entry in held)},
                'released': [_strict_json(_canonical(row)) for row in self._released.values()]}
