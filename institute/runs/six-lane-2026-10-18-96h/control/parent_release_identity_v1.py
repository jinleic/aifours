#!/usr/bin/env python3
"""parent_release_identity_v1: CP2 historical identity-union consumer and fresh independent census callback.

NOEXEC SOURCE CANDIDATE: not accepted, not qualified, no runtime/release/signal/scheduling/science authority.
CP2 scope RUN/control/parent-release-cp1-cp2-implementation-scope-v1.json
1f717bf944e6d5a524aa0a65776d39726cd251bcd006971ba322f328de6bd314; exact design frozen before code in
RUN/control/parent-release-cp2-design-freeze-v1.json 3d6f48ced0d07293a81f44936c3559571e4d4f98919c024a257f32761a7af027.

CONVENTION. The owned_supervisor_v19 cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93 native identity
is reused unchanged: proc_listallpids; proc_pidinfo flavor 17 (uniqueid, idversion) and flavor 13 (pid, ppid, pgid,
status, euid, ruid, traced, comm) in the same unique/short/unique/short/unique bracket. start_fingerprint is
'sv19-incarnation-v1:<pid>:<uniqueid>:<idversion>' in census rows, PRT identity rows, launch.driver and parent wait
records alike. Mutable ppid/pgid/uid/comm are variant history, never part of the start fingerprint. The same pid with
another fingerprint is AMBIGUOUS, never proof of endedness.

UNION. build_identity_union consumes parent-captured supervisor19 histories (exact ACK or refusal stdout line, exact
receipt/settlement bytes, parent wait and launch records) for exactly one main and at least one oracle run. It binds
bytes to parent-supplied digests and to the exact producer serialization, re-checks the identity event tape, variants,
references, owned registry roots and edge proofs, unproved history and baseline, and unions every driver/oracle,
child, helper, descendant, reparented variant and unproved incarnation. Pid-only unknown incarnations are retained,
never given a fabricated fingerprint. A history is CLOSED only by rule H7: its LAST census is complete, its raw event
window holds exactly L.pids distinct baseline identities and nothing later, and every supervisor spawn precedes it.
A JSON complete:true, an empty current tree/group or a digest alone is never completeness; otherwise HELD with a
named prerequisite.

CENSUS. make_census returns a fresh in-process libproc census callback (no helper process, no signal, no cache) and
a parent-retained CensusLog of every attempt and served snapshot. evaluate_endedness joins the union with every served
snapshot: a live member uniqueid, a reused member pid, an occupied historical variant pgid or a child of a historical
pid is HELD.

DEADLINE. deadline_check is the caller's ORIGINAL nonrenewing deadline, checked before and after every read_bytes
callback, around every native census step and after result assembly. Late success is HELD (union/endedness) or raises
(census). BaseException always propagates. This module opens no descriptor, writes nothing, spawns nothing and sends
no signal. Parent observation authenticity, direct launch, supervisor19 qualification, non-descendant creation
channels, publication freeze and the CP1 join remain external conditions listed in every report.
"""
import ctypes
import errno
import hashlib
import json
import math
import os
import struct
import time

SCOPE_SHA256 = '1f717bf944e6d5a524aa0a65776d39726cd251bcd006971ba322f328de6bd314'
DESIGN_FREEZE_SHA256 = '3d6f48ced0d07293a81f44936c3559571e4d4f98919c024a257f32761a7af027'
SUPERVISOR19_SHA256 = 'cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93'
SUPERVISOR19_VERSION = 'owned_supervisor_v19'
MODULE = 'parent_release_identity_v1.py'
SCHEME = 'sv19-incarnation-v1'
REQUEST_FORMAT = 'parent-release-identity-request-v1'
UNION_FORMAT = 'parent-release-identity-union-v1'
ENDEDNESS_FORMAT = 'parent-release-identity-endedness-v1'
WAIT_FORMAT = 'parent-release-wait-v1'
CLOSED = 'CLOSED_CONDITIONAL'
ENDED = 'ENDED_CONDITIONAL'
HELD = 'HELD'
LIBPROC = '/usr/lib/libproc.dylib'
DOC_CAP = 1 << 20
RECEIPT_CAP = 4 << 20
CAPTURE_CAP = 16 << 20
REQUEST_CAP = 64 << 10
REQUEST_NODES = 4096
MAX_HISTORIES = 16
MAX_EVENTS = 1 << 20
MAX_LIST = 65536
MAX_MEMBERS = 65536
MAX_UNKNOWN = 65536
MAX_ROWS = 200000
MAX_VARIANTS = 64
MAX_EVIDENCE = 16
MAX_TEXT = 512
MAX_CALLBACK_LOG = 128
MAX_MISSING_SAMPLE = 64
ATTEMPTS_PER_CALL = 3
MAX_LOG_ATTEMPTS = 64
MAX_SERVED = 16
RETRY_PAUSE_S = 0.05
UINT32 = (1 << 32) - 1
UINT64 = (1 << 64) - 1
ACK_EXITS = (0, 10, 11)
REFUSAL_EXITS = (2, 12, 13, 14)
ROLE_PRIORITY = ('driver', 'oracle', 'main_child', 'oracle_child', 'helper', 'oracle_helper', 'descendant',
                 'unproved')
FAMILY_ROLES = {'main': ('driver', 'main_child', 'helper'), 'oracle': ('oracle', 'oracle_child', 'oracle_helper')}
IDENTITY_KEYS = frozenset(('pid', 'ppid', 'pgid', 'status', 'euid', 'ruid', 'traced', 'comm', 'uniqueid',
                           'idversion'))
SOURCES = frozenset(('pid_scan', 'measurement_bracket', 'measurement_final_bracket', 'edge_parent_before',
                     'edge_child', 'edge_parent_after', 'main_initial', 'main_recovery', 'main_signal',
                     'helper_initial', 'helper_cleanup_initial', 'helper_signal'))
HISTORY_ENTRY_KEYS = frozenset(('first_identity', 'last_identity', 'mono_first_begin', 'mono_first_seen',
                                'mono_last_begin', 'mono_last_seen', 'first_event_ref', 'last_event_ref', 'source',
                                'observations', 'variants'))
UNPROVED_KEYS = HISTORY_ENTRY_KEYS - {'source', 'observations', 'variants'}
OWNED_KEYS = frozenset(('identity', 'identity_event_ref', 'via', 'root', 'first_seen_mono', 'proof'))
PROOF_KEYS = frozenset(('parent_before_ref', 'child_ref', 'parent_after_ref'))
CENSUS_REQUIRED = frozenset(('phase', 'inside_helper', 'complete', 'aborted', 'mono_start', 'mono_complete',
                             'incomplete_n', 'incomplete', 'pids', 'owned_live', 'unproved_live', 'group_live',
                             'owned_zombies', 'owned_event_refs', 'unproved_event_refs', 'lane_pids', 'lane_rss',
                             'lane_busy_pids', 'lane_busy', 'measurements', 'mono_end'))
CENSUS_ALLOWED = CENSUS_REQUIRED | {'raw_measurements', 'mono_last_observation', 'abort_error', 'mono_aborted',
                                    'mono_aborted_error'}
COVERAGE_KINDS = ('identify', 'parent_edge', 'real_or_effective_uid_measurement')
HELPER_REPORT_KEYS = frozenset((
    'pid', 'identity', 'identity_event_ref', 'leader_reaped', 'rc', 'wait_lost', 'term_attempted', 'settled',
    'initial_identity_valid', 'stdout_closed', 'eof_proved', 'group_clear', 'descendants_clear',
    'coverage_complete', 'clock_failed', 'date', 'signal', 'proof', 'spawn_error', 'launch_commit',
    'mono_spawn', 'epoch_spawn', 'mono_pid_registered', 'call_deadline', 'cleanup_deadline',
    'native_wait_result', 'raw_wait_status', 'epoch_reaped', 'raw_identity_ref', 'clockless_probe_done',
    'clockless_probe_count', 'endpoint_errors', 'mono_call_start', 'mono_call_deadline', 'mono_cleanup_start',
    'mono_cleanup_deadline', 'mono_proof_complete', 'mono_reaped', 'mono_injection_start', 'mono_injection_end',
    'stability_expiry_before', 'stability_expiry_candidate', 'stability_expiry_effective', 'capture_hex'))
MAIN_WAIT_KEYS = ('pid', 'native_wait_result', 'raw_wait_status', 'leader_reaped', 'rc', 'mono_reaped',
                  'epoch_reaped')
RECON_KEYS = frozenset((
    'owned_identities', 'unproved_history', 'identity_history', 'coverage_history', 'identity_events',
    'initial_fit', 'authorization', 'accounting_observations', 'min_free_witness', 'census_observations',
    'observation_attempts', 'helpers', 'helper_log', 'failures', 'main_identity', 'main_signal', 'main_stop',
    'baseline_uniqueids', 'stability_expiry_mono', 'history_charge_bytes', 'history_cap_bytes', 'history_halted',
    'history_overflow', 'publication_resources', 'ack_resources', 'publication_payload_bytes',
    'last_accounting_observation', 'maxima', 'min_free', 'streams', 'mono_snapshot', 'timing_failed',
    'raw_acquisitions', 'last_native_free', 'main_wait'))
ACK_KEYS = frozenset((
    'supervisor', 'acknowledged', 'exit_code', 'settlement', 'config_sha256', 'receipt_sha256',
    'settlement_record_sha256', 'receipt_bytes', 'settlement_bytes', 'post_publish_mono', 'ack_commit',
    'publication_resources', 'ack_resources', 'publication_payload_bytes', 'child_returncode', 'failure_codes',
    'owned_live', 'unproved_live', 'ack_census', 'contract_violations', 'unproved_history', 'coverage_history',
    'census_observations', 'reconciliation'))
REFUSAL_REQUIRED = frozenset(('supervisor', 'acknowledged', 'exit_code', 'reason', 'clock_note', 'reconciliation'))
REFUSAL_EXTRA = frozenset(('config_sha256', 'error', 'error_code', 'diagnostic_error', 'payload_bytes', 'resources',
                           'reservation_bytes', 'receipt_sha256', 'settlement_record_sha256', 'post_publish_mono',
                           'publication_resources', 'ack_resources', 'publication_payload_bytes'))
SETTLEMENT_KEYS = ('supervisor', 'config_sha256', 'settlement', 'receipt', 'receipt_sha256', 'child_returncode',
                   'failure_codes', 'trips', 'authority')
RECEIPT_REQUIRED = frozenset((
    'supervisor', 'supervisor_sha256', 'config_sha256', 'supervisor_pid', 'baseline', 'settlement', 'child_pid',
    'child_identity', 'identity_events', 'identity_history', 'owned_identities', 'unproved_history',
    'coverage_history', 'census_observations', 'helpers', 'raw_acquisitions', 'history_overflow', 'timing_failed',
    'main_wait'))
HISTORY_REQUEST_KEYS = ('family', 'producer', 'wait_record', 'launch_record', 'stdout', 'receipt', 'settlement')
U_CAUSES = (
    'U_REQUEST_INVALID', 'U_CALLBACKS_INVALID', 'U_FAMILY_INVALID', 'U_PRODUCER_PIN', 'U_WAIT_INVALID',
    'U_LAUNCH_INVALID', 'U_CAPTURE_INVALID', 'U_OUTPUT_LINE_INVALID', 'U_PRODUCER_UNSUPPORTED', 'U_EXIT_BINDING',
    'U_RECEIPT_BINDING', 'U_HISTORY_SCHEMA', 'U_HISTORY_INCOMPLETE', 'U_EVENT_TAPE_INCONSISTENT',
    'U_OWNED_REGISTRY_INCONSISTENT', 'U_UNPROVED_INCONSISTENT', 'U_BASELINE_INVALID', 'U_DRIVER_UNBOUND',
    'U_CHILD_HELPER_UNBOUND', 'U_LAST_CENSUS_OPEN', 'U_LAST_CENSUS_TAPE_MISMATCH', 'U_SPAWN_CHRONOLOGY',
    'U_ROW_CONFLICT', 'U_CAP_EXCEEDED', 'U_DEADLINE', 'U_INTERNAL_ERROR')
E_CAUSES = (
    'E_UNION_HELD', 'E_UNION_DIGEST', 'E_NO_SERVED_CENSUS', 'E_CENSUS_INCOMPLETE', 'E_OBSERVER_UNCOVERED',
    'E_MEMBER_ALIVE', 'E_PID_REUSE_AMBIGUOUS', 'E_GROUP_NONEMPTY', 'E_PID_CHILD_PRESENT', 'E_DEADLINE',
    'E_INTERNAL_ERROR')
PREREQUISITES = {
    'U_REQUEST_INVALID': 'exact parent-release-identity-request-v1 object',
    'U_CALLBACKS_INVALID': 'pinned parent read_bytes and the ORIGINAL deadline_check callables',
    'U_FAMILY_INVALID': 'exactly one main and >=1 oracle governed history; oracle launch_record null in v1',
    'U_PRODUCER_PIN': 'producer bytes identical to owned_supervisor_v19 cb828a78',
    'U_WAIT_INVALID': 'parent-observed parent-release-wait-v1 record using the sv19-incarnation-v1 fingerprint',
    'U_LAUNCH_INVALID': 'parent launch record whose item and driver identity equal the parent wait identity',
    'U_CAPTURE_INVALID': 'complete parent outer capture of supervisor stdout: eof, no overflow, exact bytes',
    'U_OUTPUT_LINE_INVALID': 'exactly one exact sv19 ACK or refusal stdout line',
    'U_PRODUCER_UNSUPPORTED': 'a governed owned_supervisor_v19 history per family; other drivers need a separately '
                              'reviewed producer format',
    'U_EXIT_BINDING': 'parent-observed exit equal to supervisor stdout exit_code (exit14 after ACK stays HELD)',
    'U_RECEIPT_BINDING': 'exact published receipt/settlement bytes bound to the ACK and its reconciliation',
    'U_HISTORY_SCHEMA': 'exact sv19 reconciliation, census, coverage and helper schemas',
    'U_HISTORY_INCOMPLETE': 'history without timing failure, history halt/overflow or pending raw acquisitions',
    'U_EVENT_TAPE_INCONSISTENT': 'consistent identity event tape, variants, counts, sources and references',
    'U_OWNED_REGISTRY_INCONSISTENT': 'consistent owned registry, roots and bracketed current-parent edge proofs',
    'U_UNPROVED_INCONSISTENT': 'unproved history equal to the unproved-flagged event set',
    'U_BASELINE_INVALID': 'complete prespawn baseline bound to the tape and to the receipt baseline',
    'U_DRIVER_UNBOUND': 'driver/oracle baseline self-observation equal to the parent wait identity, own group',
    'U_CHILD_HELPER_UNBOUND': 'main child and helper identities bound to owned registry and spawn records',
    'U_LAST_CENSUS_OPEN': 'last census complete with zero live owned/unproved/group/zombie incarnations, or a new '
                          'governed continuation history in the same convention that closes; never a current '
                          'empty tree/group',
    'U_LAST_CENSUS_TAPE_MISMATCH': 'raw event window of the last census holding exactly L.pids baseline '
                                   'identities and no later identification',
    'U_SPAWN_CHRONOLOGY': 'every supervisor spawn provably before the last census',
    'U_ROW_CONFLICT': 'conflict-free PRT rows: one driver, >=1 oracle, positive pid/pgid',
    'U_CAP_EXCEEDED': 'union within member/unknown/row caps; larger unions need a separately reviewed interface',
    'U_DEADLINE': 'a new call within the ORIGINAL deadline; no new allowance',
    'U_INTERNAL_ERROR': 'source defect review'}
CONDITIONS = (
    'PARENT_OBSERVATION_AUTHENTICITY: parent launch, wait and outer-capture records are authentic observations; '
    'JSON plus SHA-256 bind only the selected bytes',
    'PARENT_DIRECT_LAUNCH: driver and oracle supervisors were posix-spawned directly by the parent in their own new '
    'process groups with no intermediate or additional parent-side process for the item',
    'SUPERVISOR19_QUALIFICATION: owned_supervisor_v19 package v9, original22 and the full finite matrix remain '
    'unqualified; its histories are producer observations, not OS guarantees',
    'NON_DESCENDANT_CHANNELS: launchd/XPC/at/cron or other non-fork creation requested by run processes lies '
    'outside process-tree history',
    'PUBLICATION_FREEZE: every referenced file stays frozen against replacement during the call; fresh reads are '
    'not an atomic snapshot',
    'CP1_JOIN: effective release also requires the CP1 caller join of union, PRT result and endedness verdict')
BOUNDARY = ('Identity union and endedness evidence only. No release, reservation, runtime, signal, scheduling, '
            'publication or scientific authority; not source-qualified CP2.')


class IdentityRefusal(ValueError):
    """Typed bounded refusal inside the consumer; it can never certify completeness."""


class CensusRefusal(ValueError):
    """Census refusal: no partial, late or capped snapshot is ever returned as a positive."""


class _NativeError(OSError):
    """Native libproc acquisition failure; same failure class as sv19 GuardError(OSError)."""


class _Crossed(Exception):
    """Internal unwind after the original deadline became unavailable."""


_FAILED = object()


def _require(condition, message):
    if not condition:
        raise IdentityRefusal(message)


def _short(text):
    return text[:MAX_TEXT]


def _why(exc):
    try:
        text = type(exc).__name__ + ': ' + str(exc)
    except Exception:
        text = type(exc).__name__ + ': <unprintable>'
    return _short(text.replace('\x00', ' ').replace('\r', ' ').replace('\n', ' '))


def _int(value, positive=False):
    return type(value) is int and value >= (1 if positive else 0)


def _u32(value):
    return type(value) is int and 0 <= value <= UINT32


def _u64(value):
    return type(value) is int and 0 <= value <= UINT64


def _i32(value):
    return type(value) is int and -(1 << 31) <= value < (1 << 31)


def _finite(value):
    return type(value) is float and math.isfinite(value)


def _hex(value):
    return type(value) is str and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def _text(value, maximum=MAX_TEXT):
    _require(type(value) is str and 0 < len(value) <= maximum and '\x00' not in value
             and '\n' not in value and '\r' not in value, 'text type/length')
    return value


def _path(value):
    _require(type(value) is str and value.startswith('/') and 1 < len(value) <= 4096 and '\x00' not in value,
             'normalized absolute path required')
    _require(all(part not in ('', '.', '..') for part in value.split('/')[1:]), 'normalized absolute path required')
    return value


def _keys(value, wanted):
    _require(type(value) is dict and all(type(k) is str for k in value) and set(value) == set(wanted),
             'exact object keys required: ' + ','.join(sorted(wanted)))


def _exact(left, right):
    """Typed structural equality; bool never aliases int, float never aliases int."""
    stack = [(left, right)]
    while stack:
        a, b = stack.pop()
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            if set(a) != set(b):
                return False
            stack.extend((a[k], b[k]) for k in a)
        elif type(a) is list:
            if len(a) != len(b):
                return False
            stack.extend(zip(a, b))
        elif a != b:
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

    def constant(_):
        raise IdentityRefusal('nonfinite JSON constant')

    def floating(text):
        value = float(text)
        _require(math.isfinite(value), 'nonfinite JSON float')
        return value

    _require(type(data) is bytes, 'JSON bytes required')
    return json.loads(data.decode('ascii'), object_pairs_hook=pairs, parse_constant=constant,
                      parse_float=floating)


def _bytes_json(value):
    """Exact sv19 bytes_json serialization (receipt and settlement record)."""
    return (json.dumps(value, sort_keys=True, indent=1, allow_nan=False) + '\n').encode('ascii')


def start_fingerprint(pid, uniqueid, idversion):
    """The single frozen start-fingerprint text over exact sv19 native identity integers."""
    _require(_u32(pid) and _u64(uniqueid) and _i32(idversion), 'fingerprint integers')
    return '%s:%d:%d:%d' % (SCHEME, pid, uniqueid, idversion)


def _parse_fingerprint(text):
    _text(text)
    parts = text.split(':')
    _require(len(parts) == 4 and parts[0] == SCHEME, 'start_fingerprint scheme')
    for index, part in enumerate(parts[1:]):
        body = part[1:] if index == 2 and part.startswith('-') else part
        _require(body != '' and all(c in '0123456789' for c in body), 'start_fingerprint digits')
    pid, uniqueid, idversion = int(parts[1]), int(parts[2]), int(parts[3])
    _require(start_fingerprint(pid, uniqueid, idversion) == text, 'start_fingerprint not canonical')
    return pid, uniqueid, idversion


def _form(p):
    """sv19 identity_form: fingerprint plus comm."""
    return (p['pid'], p['uniqueid'], p['idversion'], p['euid'], p['ruid'], p['ppid'], p['pgid'], p['traced'],
            p['comm'])


def _sv19_fingerprint(p):
    return (p['pid'], p['uniqueid'], p['idversion'], p['euid'], p['ruid'], p['ppid'], p['pgid'], p['traced'])


class _State:
    def __init__(self, order):
        self.order, self.fired, self.evidence, self.suppressed = order, set(), {}, {}

    def fire(self, cause, detail):
        if cause not in self.order:
            cause = self.order[-1]
        self.fired.add(cause)
        values = self.evidence.setdefault(cause, [])
        if len(values) < MAX_EVIDENCE:
            values.append(_short(detail))
        else:
            self.suppressed[cause] = self.suppressed.get(cause, 0) + 1

    def causes(self):
        return [cause for cause in self.order if cause in self.fired]


class _Io:
    """Only read_bytes/deadline route: the SAME original deadline before and after every read."""

    def __init__(self, read_bytes, deadline_check):
        self.read_bytes, self.deadline_check = read_bytes, deadline_check
        self.crossed, self.reads = False, 0
        self.count, self.log, self.digest = 0, [], hashlib.sha256()

    def event(self, name, state, detail):
        row = {'callback': name, 'state': state, 'detail': _short(detail)}
        self.count += 1
        self.digest.update(_canonical(row))
        if len(self.log) < MAX_CALLBACK_LOG:
            self.log.append(row)

    def tick(self, stage):
        if self.crossed:
            return False
        try:
            value = self.deadline_check()
        except Exception as exc:
            self.crossed = True
            self.event('deadline_check', 'EXCEPTION', stage + ': ' + _why(exc))
            return False
        except BaseException as exc:
            self.event('deadline_check', 'BASE_EXCEPTION', stage + ': ' + type(exc).__name__)
            raise
        if value is not None:
            self.crossed = True
            self.event('deadline_check', 'BAD_RETURN', stage + ': ' + type(value).__name__)
            return False
        return True

    def read(self, path, cap):
        if not self.tick('before read_bytes'):
            raise _Crossed('no read_bytes after original deadline crossing')
        try:
            data = self.read_bytes(path, cap)
        except Exception as primary:
            self.event('read_bytes', 'EXCEPTION', path + ': ' + _why(primary))
            self.tick('read_bytes Exception completion')
            raise
        except BaseException as primary:
            self.event('read_bytes', 'BASE_EXCEPTION', path + ': ' + type(primary).__name__)
            raise
        self.reads += 1
        good = type(data) is bytes and len(data) <= cap
        self.event('read_bytes', 'RETURNED', path + (' bytes=%d sha256=%s' % (len(data), hashlib.sha256(data).hexdigest())
                                                     if good else ' wrong type or over cap'))
        if not self.tick('read_bytes completion'):
            raise _Crossed('read_bytes returned after the original deadline; retained only in the bounded log')
        _require(good, 'read_bytes wrong type or over cap')
        return data


def _guard(io, st, cause, label, bucket, function, *args):
    try:
        return function(*args)
    except _Crossed:
        raise
    except Exception as exc:
        st.fire(cause, label + ': ' + _why(exc))
        if bucket is not None and cause not in bucket:
            bucket.append(cause)
        if io is not None and io.crossed:
            raise _Crossed('primary failure retained; original deadline also unavailable') from exc
        return _FAILED


def _attach(exc, name, value):
    try:
        setattr(exc, name, value)
    except Exception:
        pass


# ---------------------------------------------------------------- native sv19 identity backend (runtime only)
def _bind_libproc():
    """sv19 lines 169-173 ABI, bound lazily per census factory; nothing is loaded at import."""
    lib = ctypes.CDLL(LIBPROC, use_errno=True)
    lib.proc_pidinfo.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int)
    lib.proc_pidinfo.restype = ctypes.c_int
    lib.proc_listallpids.argtypes = (ctypes.c_void_p, ctypes.c_int)
    lib.proc_listallpids.restype = ctypes.c_int
    return lib


def _pidinfo(lib, pid, flavor, size, zombies=False):
    """sv19 pidinfo 202-208: exact-size return or failure."""
    buf = ctypes.create_string_buffer(size)
    ctypes.set_errno(0)
    got = lib.proc_pidinfo(pid, flavor, 1 if zombies else 0, buf, size)
    if got != size:
        raise _NativeError(ctypes.get_errno() or errno.EIO, 'PIDINFO %d flavor %d bytes %d' % (pid, flavor, got))
    return buf.raw


def _unique(lib, pid):
    """sv19 unique 211-213: flavor 17, uniqueid '=Q'@16, idversion '=i'@32."""
    raw = _pidinfo(lib, pid, 17, 56, True)
    return struct.unpack_from('=Q', raw, 16)[0], struct.unpack_from('=i', raw, 32)[0]


def _short_info(lib, pid):
    """sv19 short 216-222: flavor 13 proc_bsdshortinfo."""
    raw = _pidinfo(lib, pid, 13, 64, True)
    p, pp, pg, st = struct.unpack_from('=IIII', raw)
    flags, uid = struct.unpack_from('=II', raw, 32)
    return {'pid': p, 'ppid': pp, 'pgid': pg, 'status': st, 'euid': uid,
            'ruid': struct.unpack_from('=I', raw, 44)[0], 'traced': bool(flags & 2),
            'comm': raw[16:32].split(b'\0')[0].decode('utf-8', 'replace')}


def _identify(lib, pid):
    """sv19 identify 234-242: unique/short/unique/short/unique bracket."""
    a, s1, b, s2, c = _unique(lib, pid), _short_info(lib, pid), _unique(lib, pid), _short_info(lib, pid), \
        _unique(lib, pid)
    if not (a == b == c):
        raise _NativeError(errno.EIO, 'IDENTITY_CHANGED %d' % pid)
    for s in (s1, s2):
        s.update(uniqueid=a[0], idversion=a[1])
    if _sv19_fingerprint(s1) != _sv19_fingerprint(s2):
        raise _NativeError(errno.EIO, 'IDENTITY_METADATA_CHANGED %d' % pid)
    return s2


def _check(deadline_check, stage):
    """Original deadline; Exception/BaseException from it propagate unchanged; non-None return refuses."""
    if deadline_check() is not None:
        raise CensusRefusal('original deadline_check returned non-None: ' + stage)


def _all_pids(lib, deadline_check):
    """sv19 all_pids 292-310 with the original deadline after every native list call."""
    _check(deadline_check, 'before pid list')
    count = lib.proc_listallpids(None, 0)
    _check(deadline_check, 'after pid list sizing')
    if count <= 0:
        raise _NativeError(errno.EIO, 'PID_LIST_FAILED')
    cap = count * 2 + 1024
    for _ in range(4):
        buf = (ctypes.c_int * cap)()
        n = lib.proc_listallpids(buf, ctypes.sizeof(buf))
        _check(deadline_check, 'after pid list')
        if n <= 0:
            raise _NativeError(errno.EIO, 'PID_LIST_FAILED')
        if n < cap:
            values = list(buf[:n])
            if any(p < 0 for p in values) or len(set(values)) != len(values):
                raise _NativeError(errno.EIO, 'PID_LIST_MALFORMED')
            return [p for p in values if p > 0]
        cap *= 2
    raise _NativeError(errno.EIO, 'PID_LIST_OVERFLOW')


class CensusLog:
    """Parent-retained evidence of every census attempt and served snapshot; never a cache or a positive source."""

    def __init__(self):
        self.calls, self.attempts, self.served, self.refusals = 0, [], [], []

    def served_count(self):
        return len(self.served)

    def summary(self):
        keys = ('call', 'attempts', 'complete', 'observer_ok', 'process_count', 'served_sha256', 'rows_sha256',
                'observed_at_mono')
        return {'calls': self.calls, 'attempts': [dict(a) for a in self.attempts],
                'served': [{k: s[k] for k in keys} for s in self.served], 'refusals': [dict(r) for r in self.refusals]}


def _attempt(lib, deadline_check, call, attempt):
    """One fresh full listing; per-pid identification failures are coverage gaps (complete False), not filtering."""
    me = os.getpid()
    before = _identify(lib, me)
    _check(deadline_check, 'census %d.%d observer bracket start' % (call, attempt))
    pids = _all_pids(lib, deadline_check)
    if len(pids) > MAX_ROWS:
        raise CensusRefusal('census process count above PRT cap')
    rows, missing, missing_n = [], [], 0
    for pid in pids:
        try:
            rows.append(_identify(lib, pid))
        except _NativeError as exc:
            missing_n += 1
            if len(missing) < MAX_MISSING_SAMPLE:
                missing.append([pid, _why(exc)])
        _check(deadline_check, 'census %d.%d after identification' % (call, attempt))
    after = _identify(lib, me)
    _check(deadline_check, 'census %d.%d observer bracket end' % (call, attempt))
    mine = [p for p in rows if p['pid'] == me]
    observer_ok = (len(mine) == 1 and _sv19_fingerprint(before) == _sv19_fingerprint(after)
                   == _sv19_fingerprint(mine[0]))
    complete = missing_n == 0 and observer_ok
    summary = {'call': call, 'attempt': attempt, 'listed': len(pids), 'identified': len(rows),
               'missing_n': missing_n, 'missing': missing, 'observer_ok': observer_ok, 'complete': complete,
               'rows_sha256': hashlib.sha256(_canonical(rows)).hexdigest()}
    return {'complete': complete, 'observer_ok': observer_ok, 'rows': rows, 'summary': summary}


def make_census(deadline_check):
    """Return (census, log). census() is the PRT census callback over a NEW independent full libproc snapshot.

    Up to three fresh full attempts (sv19 full_census reuse, no merging); first complete attempt else last attempt
    with complete False. No helper process, no signal, no cache. Raises on deadline, native listing failure or log
    cap; BaseException propagates. Every attempt summary and every served snapshot (full raw identities, digest of
    the exact served dict) is retained in log for evaluate_endedness and the CP1 receipt.
    """
    _require(callable(deadline_check), 'deadline_check must be callable')
    log = CensusLog()
    bound = []

    def census():
        log.calls += 1
        call = log.calls
        try:
            _check(deadline_check, 'census %d start' % call)
            if len(log.served) >= MAX_SERVED or len(log.attempts) + ATTEMPTS_PER_CALL > MAX_LOG_ATTEMPTS:
                raise CensusRefusal('census log cap reached: refuse rather than discard evidence')
            if not bound:
                bound.append(_bind_libproc())
            chosen, attempt = None, 0
            while attempt < ATTEMPTS_PER_CALL:
                attempt += 1
                chosen = _attempt(bound[0], deadline_check, call, attempt)
                log.attempts.append(chosen['summary'])
                if chosen['complete']:
                    break
                if attempt < ATTEMPTS_PER_CALL:
                    _check(deadline_check, 'census %d before retry pause' % call)
                    time.sleep(RETRY_PAUSE_S)
                    _check(deadline_check, 'census %d after retry pause' % call)
            observed = time.monotonic()
            if type(observed) is not float or not math.isfinite(observed):
                raise CensusRefusal('monotonic clock unavailable; observed_at_mono is never fabricated')
            served = {'complete': chosen['complete'],
                      'processes': [{'pid': p['pid'], 'ppid': p['ppid'], 'pgid': p['pgid'], 'uid': p['euid'],
                                     'start_fingerprint': start_fingerprint(p['pid'], p['uniqueid'], p['idversion'])}
                                    for p in chosen['rows']],
                      'observed_at_mono': observed}
            record = {'call': call, 'attempts': attempt, 'complete': chosen['complete'],
                      'observer_ok': chosen['observer_ok'], 'process_count': len(chosen['rows']),
                      'rows': [dict(p) for p in chosen['rows']],
                      'served_sha256': hashlib.sha256(_canonical(served)).hexdigest(),
                      'rows_sha256': chosen['summary']['rows_sha256'], 'observed_at_mono': observed}
            _check(deadline_check, 'census %d before return' % call)
        except BaseException as exc:
            try:
                if len(log.refusals) < MAX_LOG_ATTEMPTS:
                    log.refusals.append({'call': call, 'error': _why(exc) if isinstance(exc, Exception)
                                         else type(exc).__name__})
            except Exception:
                pass
            raise
        log.served.append(record)
        return served

    return census, log


# ---------------------------------------------------------------- supervisor19 history consumer
def _request(request):
    """Bounded detach (no aliasing, no arbitrary objects/cycles) and exact request validation."""
    stack, nodes = [(request, 0)], 0
    while stack:
        value, depth = stack.pop()
        nodes += 1
        _require(nodes <= REQUEST_NODES and depth <= 8, 'request node/depth cap')
        if type(value) is dict:
            _require(len(value) <= REQUEST_NODES, 'request object size')
            for key, item in list(value.items()):
                _require(type(key) is str and len(key) <= 64, 'request key')
                stack.append((item, depth + 1))
        elif type(value) is list:
            _require(len(value) <= REQUEST_NODES, 'request list size')
            stack.extend((item, depth + 1) for item in value)
        elif type(value) is str:
            _require(len(value) <= 4096, 'request string length')
        else:
            _require(value is None or type(value) is bool or (type(value) is int and abs(value) <= UINT64),
                     'request scalar type')
    data = _canonical(request)
    _require(len(data) <= REQUEST_CAP, 'request byte cap')
    request = _json(data)
    _keys(request, ('format', 'item', 'histories'))
    _require(request['format'] == REQUEST_FORMAT, 'request format')
    _text(request['item'])
    histories = request['histories']
    _require(type(histories) is list and 0 < len(histories) <= MAX_HISTORIES, 'histories list 1..16')
    for h in histories:
        _keys(h, HISTORY_REQUEST_KEYS)
        _require(h['family'] in ('main', 'oracle'), 'family main|oracle')
        _ref(h['producer'])
        _ref(h['wait_record'])
        for key in ('launch_record', 'receipt', 'settlement'):
            if h[key] is not None:
                _ref(h[key])
        _capture_record(h['stdout'])
    return request


def _ref(value):
    _keys(value, ('path', 'sha256'))
    _path(value['path'])
    _require(_hex(value['sha256']), 'lowercase 64-hex digest required')
    return value


def _capture_record(value):
    _keys(value, ('path', 'sha256', 'bytes_seen', 'bytes_stored', 'eof', 'overflow', 'error'))
    _path(value['path'])
    _require(_hex(value['sha256']), 'capture digest')
    _require(_int(value['bytes_seen']) and _int(value['bytes_stored'])
             and value['bytes_seen'] == value['bytes_stored'] <= CAPTURE_CAP, 'capture byte counts')
    _require(value['eof'] is True and value['overflow'] is False and value['error'] is None,
             'capture must be complete: eof true, overflow false, error null')
    return value


def _v_families(request):
    families = [h['family'] for h in request['histories']]
    _require(families.count('main') == 1, 'exactly one main history required')
    _require(families.count('oracle') >= 1, 'at least one oracle history required (PRT part4 oracle incarnation)')
    for h in request['histories']:
        if h['family'] == 'main':
            _require(h['launch_record'] is not None, 'main launch_record required')
        else:
            _require(h['launch_record'] is None, 'oracle launch_record must be null in v1')
    return True


def _load(io, ref, cap):
    data = io.read(ref['path'], cap)
    _require(hashlib.sha256(data).hexdigest() == ref['sha256'], 'pinned byte digest mismatch: ' + ref['path'])
    return data


def _producer(io, ref):
    _require(ref['sha256'] == SUPERVISOR19_SHA256, 'producer is not the pinned owned_supervisor_v19 source')
    _load(io, ref, DOC_CAP)
    return True


def _wait(io, ref, role, item):
    value = _json(_load(io, ref, DOC_CAP))
    _keys(value, ('format', 'item', 'role', 'pid', 'pgid', 'start_fingerprint', 'raw_status', 'actual_exit',
                  'observed_by'))
    _require(value['format'] == WAIT_FORMAT and value['role'] == role and value['observed_by'] == 'parent',
             'parent wait format/role/observer')
    _require(type(value['item']) is str and value['item'] == item, 'wait item')
    _require(_int(value['pid'], True) and _int(value['pgid'], True), 'wait pid/pgid')
    pid, uniqueid, idversion = _parse_fingerprint(value['start_fingerprint'])
    _require(pid == value['pid'], 'wait start_fingerprint pid != wait pid')
    _require(_int(value['raw_status']) and type(value['actual_exit']) is int, 'wait status/exit types')
    _require(os.waitstatus_to_exitcode(value['raw_status']) == value['actual_exit'],
             'raw wait status does not decode to actual_exit')
    return {'pid': value['pid'], 'pgid': value['pgid'], 'start_fingerprint': value['start_fingerprint'],
            'uniqueid': uniqueid, 'idversion': idversion, 'actual_exit': value['actual_exit']}


def _launch(io, ref, item, wait):
    value = _json(_load(io, ref, DOC_CAP))
    _require(type(value) is dict and type(value.get('item')) is str and value['item'] == item, 'launch item')
    driver = value.get('driver')
    _keys(driver, ('pid', 'pgid', 'start_fingerprint'))
    _require(_exact(driver, {k: wait[k] for k in ('pid', 'pgid', 'start_fingerprint')}),
             'launch.driver != parent wait identity')
    return True


def _stdout(io, record):
    data = io.read(record['path'], record['bytes_stored'])
    _require(len(data) == record['bytes_stored'] and hashlib.sha256(data).hexdigest() == record['sha256'],
             'stdout capture actual bytes/hash/count mismatch')
    return data


def _line(data):
    _require(len(data) > 1 and data.endswith(b'\n') and data.count(b'\n') == 1,
             'supervisor stdout must be exactly one LF-terminated line')
    value = _json(data)
    _require(type(value) is dict, 'supervisor stdout line must be one JSON object')
    if value.get('acknowledged') is True:
        canonical = json.dumps(value, sort_keys=True, allow_nan=False, separators=(',', ':')) + '\n'
    else:
        canonical = json.dumps(value, allow_nan=False, separators=(',', ':')) + '\n'
    _require(canonical.encode('ascii') == data, 'stdout line is not the exact sv19 serialization')
    return value


def _producer_line(value):
    _require(value.get('supervisor') == SUPERVISOR19_VERSION, 'stdout line is not owned_supervisor_v19 output')
    if value.get('acknowledged') is True:
        _keys(value, ACK_KEYS)
        _require(type(value['exit_code']) is int and value['exit_code'] in ACK_EXITS, 'ACK exit_code')
        return 'ACK'
    _require(value.get('acknowledged') is False, 'acknowledged must be an exact bool')
    _require(REFUSAL_REQUIRED <= set(value) <= REFUSAL_REQUIRED | REFUSAL_EXTRA, 'refusal keys')
    _require(type(value['exit_code']) is int and value['exit_code'] in REFUSAL_EXITS, 'refusal exit_code')
    return 'REFUSAL'


def _exit_binding(wait, value):
    _require(wait['actual_exit'] == value['exit_code'], 'parent-observed exit != supervisor stdout exit_code')
    return True


def _ack_files(io, h, ack):
    _require(h['receipt'] is not None and h['settlement'] is not None, 'ACK requires receipt and settlement refs')
    _require(h['receipt']['sha256'] == ack['receipt_sha256']
             and h['settlement']['sha256'] == ack['settlement_record_sha256'], 'ACK digests != supplied refs')
    _require(_int(ack['receipt_bytes']) and _int(ack['settlement_bytes']), 'ACK byte counts')
    receipt_bytes = _load(io, h['receipt'], RECEIPT_CAP)
    settlement_bytes = _load(io, h['settlement'], DOC_CAP)
    _require(len(receipt_bytes) == ack['receipt_bytes'] and len(settlement_bytes) == ack['settlement_bytes'],
             'ACK receipt/settlement byte counts')
    receipt, settlement = _json(receipt_bytes), _json(settlement_bytes)
    _require(type(receipt) is dict and type(settlement) is dict, 'receipt/settlement objects')
    _require(_bytes_json(receipt) == receipt_bytes and _bytes_json(settlement) == settlement_bytes,
             'receipt/settlement are not the exact sv19 bytes_json serialization')
    _keys(settlement, SETTLEMENT_KEYS)
    _require(RECEIPT_REQUIRED <= set(receipt), 'receipt lacks required history fields')
    _require(settlement['supervisor'] == SUPERVISOR19_VERSION and receipt['supervisor'] == SUPERVISOR19_VERSION,
             'receipt/settlement producer version')
    _require(receipt['supervisor_sha256'] == SUPERVISOR19_SHA256, 'receipt supervisor_sha256 != pinned source')
    _require(settlement['receipt_sha256'] == ack['receipt_sha256'], 'settlement receipt digest')
    _require(settlement['receipt'] == h['receipt']['path'], 'settlement receipt path != supplied receipt path')
    _require(_hex(ack['config_sha256']) and receipt['config_sha256'] == ack['config_sha256']
             and settlement['config_sha256'] == ack['config_sha256'], 'config digests')
    _require(type(ack['settlement']) is str and receipt['settlement'] == ack['settlement']
             and settlement['settlement'] == ack['settlement'], 'settlement state')
    return receipt


def _refusal_refs(h):
    _require(h['receipt'] is None and h['settlement'] is None,
             'refusal history: receipt and settlement must be null in v1')
    return True


def _recon(value, kind):
    recon = value['reconciliation']
    _require(type(recon) is dict and RECON_KEYS <= set(recon) <= RECON_KEYS | {'mono_snapshot_error'},
             'reconciliation keys')
    if kind == 'ACK':
        for key in ('unproved_history', 'coverage_history', 'census_observations'):
            _require(_exact(value[key], recon[key]), 'ACK ' + key + ' != reconciliation')
        census = recon['census_observations']
        _require(type(census) is list and census and type(value['ack_census']) is dict
                 and _exact(value['ack_census'], census[-1]), 'ack_census != last census observation')
        _require(_exact(value['owned_live'], value['ack_census'].get('owned_live'))
                 and _exact(value['unproved_live'], value['ack_census'].get('unproved_live')),
                 'ACK live lists != ack_census')
    return recon


def _complete_flags(recon):
    _require(recon['timing_failed'] is False, 'timing_failed: missing clocks are incomplete evidence')
    _require(recon['history_halted'] is False and recon['history_overflow'] is None,
             'history halted/overflow: capped history is incomplete')
    _require(type(recon['raw_acquisitions']) is list and not recon['raw_acquisitions'],
             'pending raw acquisitions are not retained in the canonical tape')
    return True


def _pending(family, index, recon):
    """Informational pid-only records for acquisitions outside the canonical tape (history is HELD anyway)."""
    rows = []
    raw = recon['raw_acquisitions'] if type(recon['raw_acquisitions']) is list else []
    for item in raw[:MAX_UNKNOWN]:
        ident = item.get('identity') if type(item) is dict else None
        pid = ident.get('pid') if type(ident) is dict else None
        rows.append({'family': family, 'history': index, 'pid': pid if _u32(pid) else None,
                     'kind': 'raw_pending_acquisition'})
    overflow = recon['history_overflow']
    if type(overflow) is dict:
        for key in ('completed_identity_observation', 'completed_measurement'):
            observed = overflow.get(key)
            ident = observed.get('identity') if type(observed) is dict else None
            if type(ident) is dict:
                pid = ident.get('pid')
                rows.append({'family': family, 'history': index, 'pid': pid if _u32(pid) else None,
                             'kind': 'history_overflow:' + key})
    return rows


def _identity(value):
    _keys(value, IDENTITY_KEYS)
    for key in ('pid', 'ppid', 'pgid', 'status', 'euid', 'ruid'):
        _require(_u32(value[key]), 'identity ' + key)
    _require(type(value['traced']) is bool, 'identity traced')
    _require(type(value['comm']) is str and len(value['comm']) <= 16, 'identity comm')
    _require(_u64(value['uniqueid']) and _i32(value['idversion']), 'identity uniqueid/idversion')
    return value


def _tape(recon):
    events = recon['identity_events']
    _require(type(events) is list and len(events) <= MAX_EVENTS, 'identity event tape')
    for event in events:
        _require(type(event) is list and len(event) == 6, 'identity event shape')
        uid, index, status, begin, end, unproved = event
        _require(_u64(uid) and _int(index) and index < MAX_VARIANTS and _u32(status) and _finite(begin)
                 and _finite(end) and begin <= end and type(unproved) is bool, 'identity event fields')
    return events, _history_entries(recon['identity_history'], events)


def _history_entries(entries, events):
    _require(type(entries) is list and len(entries) <= MAX_LIST, 'identity_history list')
    hist = {}
    for entry in entries:
        _keys(entry, HISTORY_ENTRY_KEYS)
        variants = entry['variants']
        _require(type(variants) is list and 0 < len(variants) <= MAX_VARIANTS, 'identity variants')
        forms = [_form(_identity(v)) for v in variants]
        pid, uid = forms[0][0], forms[0][1]
        _require(len(set(forms)) == len(forms) and all(f[0] == pid and f[1] == uid for f in forms),
                 'variants must be distinct forms of one pid and uniqueid')
        _require(uid not in hist, 'duplicate identity_history uniqueid')
        for which in ('first', 'last'):
            _require(_form(_identity(entry[which + '_identity'])) in forms, which + '_identity is not a variant')
            _require(_int(entry[which + '_event_ref'], True) and entry[which + '_event_ref'] <= len(events),
                     which + '_event_ref range')
            _require(_finite(entry['mono_' + which + '_begin']) and _finite(entry['mono_' + which + '_seen']),
                     which + ' interval')
        _require(_int(entry['observations'], True), 'observations')
        _require(entry['source'] in SOURCES, 'first observation source outside the sv19 native acquisition sites')
        hist[uid] = {'entry': entry, 'forms': forms, 'refs': []}
    for ref, event in enumerate(events, 1):
        record = hist.get(event[0])
        _require(record is not None and event[1] < len(record['forms']), 'event without matching history variant')
        record['refs'].append(ref)
    for uid, record in hist.items():
        entry, refs = record['entry'], record['refs']
        _require(len(refs) == entry['observations'], 'observations != event tape count for uniqueid %d' % uid)
        ends = [events[r - 1][4] for r in refs]
        for which, extreme in (('first', min(ends)), ('last', max(ends))):
            event, ident = events[entry[which + '_event_ref'] - 1], entry[which + '_identity']
            _require(event[0] == uid and event[4] == extreme
                     and event[1] == record['forms'].index(_form(ident)) and event[2] == ident['status']
                     and event[3] == entry['mono_' + which + '_begin']
                     and event[4] == entry['mono_' + which + '_seen'],
                     which + ' event reference inconsistent for uniqueid %d' % uid)
    return hist


def _ref_matches(events, hist, ref, p):
    _require(_int(ref, True) and ref <= len(events), 'event reference range')
    event, record = events[ref - 1], hist.get(p['uniqueid'])
    _require(record is not None and event[0] == p['uniqueid'] and _form(p) in record['forms']
             and event[1] == record['forms'].index(_form(p)) and event[2] == p['status'],
             'event reference does not denote this identity observation')
    return True


def _baseline(recon, hist, events, receipt):
    ids = recon['baseline_uniqueids']
    _require(type(ids) is list and ids and all(_u64(u) for u in ids) and ids == sorted(set(ids)),
             'baseline uniqueids must be a sorted unique nonempty list')
    baseline = set(ids)
    _require(baseline <= set(hist), 'baseline identity without history entry')
    if receipt is not None:
        record = receipt['baseline']
        _keys(record, ('mono_complete', 'identities', 'event_refs'))
        identities, refs = record['identities'], record['event_refs']
        _require(type(identities) is list and type(refs) is list and len(identities) == len(refs)
                 == len(baseline), 'receipt baseline list sizes')
        for p, ref in zip(identities, refs):
            _identity(p)
            _ref_matches(events, hist, ref, p)
        _require({p['uniqueid'] for p in identities} == baseline, 'receipt baseline identities != baseline uniqueids')
        pids = [p['pid'] for p in identities]
        _require(pids == sorted(pids) and _finite(record['mono_complete']), 'receipt baseline order/time')
    return baseline


def _helpers(recon, hist, events):
    reports = recon['helpers']
    _require(type(reports) is list and len(reports) <= MAX_LIST, 'helper reports')
    seen = set()
    for report in reports:
        _keys(report, HELPER_REPORT_KEYS)
        _require(_int(report['pid'], True), 'helper pid')
        _require(report['mono_spawn'] is None or _finite(report['mono_spawn']), 'helper mono_spawn')
        _require(type(report['initial_identity_valid']) is bool, 'helper initial_identity_valid')
        ident = report['identity']
        if ident is not None:
            _identity(ident)
            _require(ident['pid'] == report['pid'] and ident['uniqueid'] in hist
                     and ident['uniqueid'] not in seen, 'helper identity pid/history/uniqueness')
            seen.add(ident['uniqueid'])
            if report['identity_event_ref'] is not None:
                _ref_matches(events, hist, report['identity_event_ref'], ident)
    return reports


def _via_parent(via):
    _require(type(via) is str and via.startswith('current_parent:'), 'owned via')
    digits = via[len('current_parent:'):]
    _require(digits != '' and all(c in '0123456789' for c in digits) and str(int(digits)) == digits,
             'current_parent uniqueid text')
    return int(digits)


def _owned(recon, hist, events, helper_uids):
    entries = recon['owned_identities']
    _require(type(entries) is list and len(entries) <= MAX_LIST, 'owned identities list')
    owned = {}
    for entry in entries:
        _keys(entry, OWNED_KEYS)
        p = _identity(entry['identity'])
        uid, via = p['uniqueid'], entry['via']
        _require(uid not in owned and uid in hist, 'owned uniqueid duplicate or absent from history')
        _ref_matches(events, hist, entry['identity_event_ref'], p)
        _require(_u64(entry['root']) and _finite(entry['first_seen_mono']), 'owned root/time')
        parent = None
        if via in ('child', 'helper'):
            _require(entry['root'] == uid and entry['proof'] is None, 'direct owned root/proof')
        elif via == 'owned_group':
            _require(entry['proof'] is None, 'owned_group proof must be null')
        else:
            parent = _via_parent(via)
            proof = entry['proof']
            _keys(proof, PROOF_KEYS)
            for key, who in (('parent_before_ref', parent), ('child_ref', uid), ('parent_after_ref', parent)):
                ref = proof[key]
                _require(_int(ref, True) and ref <= len(events) and events[ref - 1][0] == who,
                         'current-parent edge proof reference ' + key)
        owned[uid] = {'entry': entry, 'via': via, 'parent': parent}
    for uid, record in owned.items():
        root = record['entry']['root']
        if record['via'] == 'owned_group':
            _require((root in owned and owned[root]['via'] in ('child', 'helper')) or root in helper_uids,
                     'owned_group root is not a direct child/helper incarnation')
        elif record['parent'] is not None:
            parent = owned.get(record['parent'])
            _require(parent is not None and parent['entry']['root'] == root, 'current-parent edge root')
    return owned


def _unproved(recon, hist, events, baseline):
    entries = recon['unproved_history']
    _require(type(entries) is list and len(entries) <= MAX_LIST, 'unproved history list')
    result = {}
    for entry in entries:
        _keys(entry, UNPROVED_KEYS)
        first, last = _identity(entry['first_identity']), _identity(entry['last_identity'])
        uid = first['uniqueid']
        _require(last['uniqueid'] == uid and uid in hist and uid not in baseline and uid not in result,
                 'unproved uniqueid')
        flagged = [r for r in hist[uid]['refs'] if events[r - 1][5]]
        _require(flagged, 'unproved entry without unproved-flagged event')
        ends = [events[r - 1][4] for r in flagged]
        for which, extreme, ident in (('first', min(ends), first), ('last', max(ends), last)):
            ref = entry[which + '_event_ref']
            _require(_int(ref, True) and ref in flagged, which + ' unproved event reference')
            event = events[ref - 1]
            _require(event[4] == extreme and event[3] == entry['mono_' + which + '_begin']
                     and event[4] == entry['mono_' + which + '_seen']
                     and event[1] == hist[uid]['forms'].index(_form(ident)) and event[2] == ident['status'],
                     which + ' unproved event inconsistent')
        result[uid] = entry
    _require({event[0] for event in events if event[5]} == set(result),
             'unproved-flagged events != unproved_history')
    return result


def _censuses(recon, hist, events):
    records = recon['census_observations']
    _require(type(records) is list and 0 < len(records) <= 4096, 'census observations')
    for record in records:
        _require(type(record) is dict and CENSUS_REQUIRED <= set(record) <= CENSUS_ALLOWED, 'census record keys')
        _require(type(record['complete']) is bool and type(record['aborted']) is bool
                 and _finite(record['mono_start'])
                 and (record['mono_complete'] is None or _finite(record['mono_complete']))
                 and _int(record['pids']) and _int(record['incomplete_n']) and type(record['incomplete']) is list,
                 'census record fields')
        for live, refs in (('owned_live', 'owned_event_refs'), ('unproved_live', 'unproved_event_refs')):
            ids, rows = record[live], record[refs]
            _require(type(ids) is list and type(rows) is list and len(ids) == len(rows), 'census ' + live)
            for p, ref in zip(ids, rows):
                _identity(p)
                _ref_matches(events, hist, ref, p)
        for key in ('group_live', 'owned_zombies'):
            _require(type(record[key]) is list and all(_u32(x) for x in record[key]), 'census ' + key)
    return records


def _coverage(recon):
    entries = recon['coverage_history']
    _require(type(entries) is list and len(entries) <= MAX_LIST, 'coverage history')
    gaps = []
    for entry in entries:
        _require(type(entry) is dict and set(entry) in ({'mono', 'observation'}, {'mono', 'observation', 'mono_error'}),
                 'coverage entry keys')
        observation = entry['observation']
        _require(type(observation) is list and len(observation) == 3 and _u32(observation[0])
                 and observation[1] in COVERAGE_KINDS and type(observation[2]) is str, 'coverage observation')
        gaps.append((observation[0], observation[1]))
    return gaps


def _receipt_prefix(receipt, recon):
    for key in ('identity_events', 'census_observations', 'coverage_history', 'owned_identities'):
        old, new = receipt[key], recon[key]
        _require(type(old) is list and type(new) is list and len(old) <= len(new) and _exact(old, new[:len(old)]),
                 'receipt ' + key + ' is not a prefix of the ACK reconciliation')
    for key in ('identity_history', 'unproved_history'):
        old, new = receipt[key], recon[key]
        _require(type(old) is list and type(new) is list and len(old) <= len(new), 'receipt ' + key + ' length')
        for a, b in zip(old, new):
            _require(type(a) is dict and type(b) is dict and type(a.get('first_identity')) is dict
                     and type(b.get('first_identity')) is dict
                     and _exact(a['first_identity'].get('uniqueid'), b['first_identity'].get('uniqueid')),
                     'receipt ' + key + ' uniqueid order')
            if key == 'identity_history':
                va, vb = a.get('variants'), b.get('variants')
                _require(type(va) is list and type(vb) is list and len(va) <= len(vb) and _exact(va, vb[:len(va)]),
                         'receipt variants are not a prefix')
    for key in ('helpers', 'main_wait', 'raw_acquisitions', 'history_overflow', 'timing_failed'):
        _require(_exact(receipt[key], recon[key]), 'receipt ' + key + ' != ACK reconciliation')
    _require(_exact(receipt['child_identity'], recon['main_identity']), 'receipt child_identity != main_identity')
    main = recon['main_wait']
    _require(_exact(receipt['child_pid'], None if main is None else main.get('pid')), 'receipt child_pid')
    return True


def _driver(wait, hist, baseline, receipt):
    _require(wait['pgid'] == wait['pid'], 'driver/oracle must lead its own process group (pgid == pid)')
    matches = [uid for uid, record in hist.items() if record['forms'][0][0] == wait['pid']]
    _require(len(matches) == 1, 'exactly one history incarnation must carry the waited pid')
    uid = matches[0]
    _require(uid in baseline, 'driver self-observation must be a baseline identity')
    _require(uid == wait['uniqueid'], 'wait fingerprint uniqueid != supervisor self-observation')
    _require(all(f[2] == wait['idversion'] and f[6] == wait['pgid'] for f in hist[uid]['forms']),
             'driver variants idversion/pgid != parent wait identity')
    if receipt is not None:
        _require(_exact(receipt['supervisor_pid'], wait['pid']), 'receipt supervisor_pid != waited pid')
    return uid


def _child_helper(recon, owned, helpers):
    main_wait, ident = recon['main_wait'], recon['main_identity']
    children = [uid for uid, record in owned.items() if record['via'] == 'child']
    if main_wait is not None:
        _keys(main_wait, MAIN_WAIT_KEYS)
        _require(_int(main_wait['pid'], True), 'main child pid')
    if ident is None:
        _require(not children, 'owned child without main identity')
    else:
        _identity(ident)
        _require(main_wait is not None and ident['pid'] == main_wait['pid'] and ident['pgid'] == ident['pid'],
                 'main identity pid/own group')
        _require(children == [ident['uniqueid']] and _exact(owned[ident['uniqueid']]['entry']['identity'], ident),
                 'main identity != owned child registration')
    helper_uids = set()
    for report in helpers:
        h = report['identity']
        if h is None:
            continue
        helper_uids.add(h['uniqueid'])
        if report['initial_identity_valid']:
            record = owned.get(h['uniqueid'])
            _require(h['pgid'] == h['pid'] and record is not None and record['via'] == 'helper',
                     'valid helper identity not registered owned via helper in its own group')
    for uid, record in owned.items():
        if record['via'] == 'helper':
            _require(uid in helper_uids, 'owned helper without a helper report')
    return True


def _last_census(records):
    last = records[-1]
    _require(last['complete'] is True and last['aborted'] is False and last['incomplete_n'] == 0
             and last['incomplete'] == [], 'last census incomplete or aborted')
    _require(last['owned_live'] == [] and last['unproved_live'] == [] and last['owned_event_refs'] == []
             and last['unproved_event_refs'] == [] and last['group_live'] == [] and last['owned_zombies'] == [],
             'last census shows live owned/unproved/group/zombie incarnations: history open after it')
    _require(_finite(last['mono_complete']) and last['mono_start'] <= last['mono_complete']
             and _int(last['pids'], True), 'last census window')
    return last


def _closure_tape(last, events, baseline):
    start, end, inside = last['mono_start'], last['mono_complete'], set()
    for uid, index, status, begin, finish, unproved in events:
        _require(begin <= end, 'identity observation after the last census')
        if finish < start:
            continue
        _require(start <= begin and finish <= end, 'identity observation straddles the last census window')
        _require(not unproved and uid in baseline, 'post-baseline or unproved identity inside the last census')
        inside.add(uid)
    _require(len(inside) == last['pids'], 'last census pid count != distinct identities in its raw event window')
    return True


def _chronology(last, recon, helpers, hist, events, receipt):
    start = last['mono_start']
    for report in helpers:
        _require(_finite(report['mono_spawn']) and report['mono_spawn'] < start,
                 'helper spawn not provably before the last census')
    if recon['main_wait'] is not None:
        if receipt is not None:
            _require(_finite(receipt.get('mono_spawn')) and receipt['mono_spawn'] < start,
                     'main spawn not provably before the last census')
        else:
            ident = recon['main_identity']
            _require(type(ident) is dict and ident.get('uniqueid') in hist
                     and any(events[r - 1][4] <= start for r in hist[ident['uniqueid']]['refs']),
                     'main spawn chronology unavailable without receipt mono_spawn')
    return True


def _members(family, index, hist, baseline, owned, unproved, helper_uids, driver):
    names, members = FAMILY_ROLES[family], []
    for uid, record in hist.items():
        entry, forms = record['entry'], record['forms']
        via = owned[uid]['via'] if uid in owned else None
        categories = []
        if uid == driver:
            categories.append('driver_self_observation')
        if via is not None:
            categories.append('owned:' + ('current_parent' if via.startswith('current_parent:') else via))
        if uid in helper_uids:
            categories.append('helper_report')
        if uid in unproved:
            categories.append('unproved_history')
        if uid not in baseline:
            categories.append('post_baseline')
        if not categories:
            continue
        if uid == driver:
            role = names[0]
        elif via == 'child':
            role = names[1]
        elif via == 'helper' or uid in helper_uids:
            role = names[2]
        elif via is not None:
            role = 'descendant'
        else:
            role = 'unproved'
        pid, last, rows = forms[0][0], entry['last_identity'], []
        versions = sorted({f[2] for f in forms})
        for version in versions:
            pgid = last['pgid'] if last['idversion'] == version else [f[6] for f in forms if f[2] == version][-1]
            rows.append({'role': role, 'pid': pid, 'pgid': pgid,
                         'start_fingerprint': start_fingerprint(pid, uid, version),
                         'source': 'sv19:%s#%d:%s:uid=%d' % (family, index, categories[0], uid)})
        members.append({'family': family, 'history': index, 'uniqueid': uid, 'pid': pid, 'role': role,
                        'categories': categories, 'idversions': versions,
                        'pgids': sorted({f[6] for f in forms}), 'ppids': sorted({f[5] for f in forms}),
                        'euids': sorted({f[3] for f in forms}), 'ruids': sorted({f[4] for f in forms}),
                        'comms': sorted({f[8] for f in forms}), 'observations': entry['observations'],
                        'first_event_ref': entry['first_event_ref'], 'last_event_ref': entry['last_event_ref'],
                        'first_source': entry['source'], 'rows': rows})
    _require(len(members) <= MAX_MEMBERS, 'member cap')
    return members


def _unknowns(family, index, gaps, helpers, recon):
    rows = [{'family': family, 'history': index, 'pid': pid, 'kind': 'coverage:' + kind} for pid, kind in gaps]
    rows.extend({'family': family, 'history': index, 'pid': r['pid'], 'kind': 'helper_without_identity'}
                for r in helpers if r['identity'] is None)
    main = recon['main_wait']
    if main is not None and recon['main_identity'] is None:
        _require(type(main) is dict and _int(main.get('pid'), True), 'main child pid')
        rows.append({'family': family, 'history': index, 'pid': main['pid'], 'kind': 'main_child_without_identity'})
    _require(len(rows) <= MAX_UNKNOWN, 'unknown incarnation cap')
    return rows


def _analyze(io, st, item, index, h):
    """One governed history: every check fires its own cause; dependent checks are skipped, never passed."""
    family = h['family']
    tag, bucket = '%s#%d' % (family, index), []
    out = {'family': family, 'index': index, 'causes': bucket, 'kind': None, 'exit_code': None, 'outcome': None,
           'driver_uniqueid': None, 'last_census': None, 'members': [], 'unknowns': []}

    def guard(cause, label, function, *args):
        return _guard(io, st, cause, tag + ' ' + label, bucket, function, *args)

    guard('U_PRODUCER_PIN', 'producer', _producer, io, h['producer'])
    wait = guard('U_WAIT_INVALID', 'wait', _wait, io, h['wait_record'], FAMILY_ROLES[family][0], item)
    if family == 'main' and h['launch_record'] is not None and wait is not _FAILED:
        guard('U_LAUNCH_INVALID', 'launch', _launch, io, h['launch_record'], item, wait)
    data = guard('U_CAPTURE_INVALID', 'stdout', _stdout, io, h['stdout'])
    if data is _FAILED:
        return out
    line = guard('U_OUTPUT_LINE_INVALID', 'stdout line', _line, data)
    if line is _FAILED:
        return out
    kind = guard('U_PRODUCER_UNSUPPORTED', 'producer line', _producer_line, line)
    if kind is _FAILED:
        return out
    out['kind'], out['exit_code'] = kind, line['exit_code']
    out['outcome'] = line.get('settlement') if kind == 'ACK' else line.get('reason')
    if wait is not _FAILED:
        guard('U_EXIT_BINDING', 'exit', _exit_binding, wait, line)
    receipt, receipt_blocked = None, False
    if kind == 'ACK':
        receipt = guard('U_RECEIPT_BINDING', 'receipt', _ack_files, io, h, line)
        if receipt is _FAILED:
            receipt, receipt_blocked = None, True
    else:
        guard('U_RECEIPT_BINDING', 'refusal refs', _refusal_refs, h)
    recon = guard('U_HISTORY_SCHEMA', 'reconciliation', _recon, line, kind)
    if recon is _FAILED:
        return out
    guard('U_HISTORY_INCOMPLETE', 'completeness', _complete_flags, recon)
    pending = guard('U_HISTORY_SCHEMA', 'pending', _pending, family, index, recon)
    if pending is not _FAILED:
        out['unknowns'].extend(pending)
    tape = guard('U_EVENT_TAPE_INCONSISTENT', 'event tape', _tape, recon)
    if tape is _FAILED:
        return out
    events, hist = tape
    baseline = guard('U_BASELINE_INVALID', 'baseline', _baseline, recon, hist, events, receipt)
    helpers = guard('U_HISTORY_SCHEMA', 'helpers', _helpers, recon, hist, events)
    helper_uids = set() if helpers is _FAILED else {r['identity']['uniqueid'] for r in helpers
                                                     if r['identity'] is not None}
    owned = guard('U_OWNED_REGISTRY_INCONSISTENT', 'owned', _owned, recon, hist, events, helper_uids)
    unproved = _FAILED
    if baseline is not _FAILED:
        unproved = guard('U_UNPROVED_INCONSISTENT', 'unproved', _unproved, recon, hist, events, baseline)
    censuses = guard('U_HISTORY_SCHEMA', 'censuses', _censuses, recon, hist, events)
    gaps = guard('U_HISTORY_SCHEMA', 'coverage', _coverage, recon)
    if receipt is not None:
        guard('U_RECEIPT_BINDING', 'receipt prefix', _receipt_prefix, receipt, recon)
    driver = _FAILED
    if wait is not _FAILED and baseline is not _FAILED:
        driver = guard('U_DRIVER_UNBOUND', 'driver', _driver, wait, hist, baseline, receipt)
        if driver is not _FAILED:
            out['driver_uniqueid'] = driver
    if owned is not _FAILED and helpers is not _FAILED:
        guard('U_CHILD_HELPER_UNBOUND', 'child/helper', _child_helper, recon, owned, helpers)
    if censuses is not _FAILED:
        last = guard('U_LAST_CENSUS_OPEN', 'last census', _last_census, censuses)
        if last is not _FAILED:
            out['last_census'] = {'mono_start': last['mono_start'], 'mono_complete': last['mono_complete'],
                                  'pids': last['pids'], 'phase': last['phase']}
            if baseline is not _FAILED:
                guard('U_LAST_CENSUS_TAPE_MISMATCH', 'last census window', _closure_tape, last, events, baseline)
            if helpers is not _FAILED and not receipt_blocked:
                guard('U_SPAWN_CHRONOLOGY', 'spawn chronology', _chronology, last, recon, helpers, hist, events,
                      receipt)
    if not any(x is _FAILED for x in (baseline, owned, unproved, helpers)):
        members = guard('U_INTERNAL_ERROR', 'members', _members, family, index, hist, baseline, owned, unproved,
                        helper_uids, None if driver is _FAILED else driver)
        if members is not _FAILED:
            out['members'] = members
    if gaps is not _FAILED and helpers is not _FAILED:
        unknown = guard('U_HISTORY_SCHEMA', 'unknown incarnations', _unknowns, family, index, gaps, helpers, recon)
        if unknown is not _FAILED:
            out['unknowns'].extend(unknown)
    return out


def _caps(members, unknowns):
    _require(len(members) <= MAX_MEMBERS and len(unknowns) <= MAX_UNKNOWN, 'union member/unknown cap')
    return True


def _rows(members):
    chosen = {}
    for member in members:
        for row in member['rows']:
            key = (row['pid'], row['start_fingerprint'])
            old = chosen.get(key)
            if old is not None and {old['role'], row['role']} == {'driver', 'oracle'}:
                raise IdentityRefusal('one incarnation is both main driver and oracle')
            if old is None or ROLE_PRIORITY.index(row['role']) < ROLE_PRIORITY.index(old['role']):
                chosen[key] = row
    rows = sorted(chosen.values(), key=lambda r: (ROLE_PRIORITY.index(r['role']), r['pid'], r['start_fingerprint']))
    _require(len(rows) <= MAX_ROWS, 'PRT identity row cap')
    _require(sum(1 for r in rows if r['role'] == 'driver') == 1, 'exactly one driver row required')
    _require(any(r['role'] == 'oracle' for r in rows), 'at least one oracle row required')
    _require(all(r['pid'] >= 1 and r['pgid'] >= 1 for r in rows), 'PRT rows need positive pid/pgid')
    return [dict(r) for r in rows]


def _union_report(st, io, item, analyses, members, unknowns, rows):
    causes = st.causes()
    state = CLOSED if not causes else HELD
    histories = []
    for a in analyses:
        histories.append({'family': a['family'], 'index': a['index'], 'kind': a['kind'], 'exit_code': a['exit_code'],
                          'outcome': a['outcome'], 'driver_uniqueid': a['driver_uniqueid'],
                          'last_census': a['last_census'], 'causes': list(a['causes']),
                          'closure': 'H7_CLOSED' if not a['causes'] else 'OPEN_HELD'})
    closure = {(a['family'], a['index']): ('H7_CLOSED' if not a['causes'] else 'OPEN_HELD') for a in analyses}
    unknown_rows = [dict(u, closure=closure.get((u['family'], u['history']), 'OPEN_HELD')) for u in unknowns]
    report = {'format': UNION_FORMAT, 'module': MODULE, 'scheme': SCHEME, 'scope_sha256': SCOPE_SHA256,
              'design_freeze_sha256': DESIGN_FREEZE_SHA256, 'producer_sha256': SUPERVISOR19_SHA256,
              'item': item, 'state': state, 'causes': causes,
              'evidence': {cause: list(st.evidence[cause]) for cause in causes},
              'suppressed': {cause: st.suppressed[cause] for cause in causes if cause in st.suppressed},
              'prerequisites': [{'code': cause, 'needed': PREREQUISITES[cause]} for cause in causes],
              'histories': histories, 'members': members, 'unknown_incarnations': unknown_rows,
              'prt_identities': rows if state == CLOSED else None,
              'candidate_prt_identities': None if state == CLOSED else rows,
              'historical_pids': sorted({m['pid'] for m in members}),
              'historical_pgids': sorted({g for m in members for g in m['pgids']}),
              'reads': io.reads, 'callbacks': {'count': io.count, 'sha256': io.digest.hexdigest(), 'log': list(io.log)},
              'deadline_crossed': io.crossed, 'conditions': list(CONDITIONS), 'boundary': BOUNDARY}
    report['union_sha256'] = hashlib.sha256(_canonical(report)).hexdigest()
    return report


def _minimal_report(st, item):
    causes = st.causes() or ['U_INTERNAL_ERROR']
    report = {'format': UNION_FORMAT, 'module': MODULE, 'scheme': SCHEME, 'item': item if type(item) is str else None,
              'state': HELD, 'causes': causes, 'prerequisites': [{'code': c, 'needed': PREREQUISITES[c]} for c in causes],
              'members': [], 'unknown_incarnations': [], 'prt_identities': None, 'candidate_prt_identities': None,
              'historical_pids': [], 'historical_pgids': [], 'conditions': list(CONDITIONS), 'boundary': BOUNDARY}
    report['union_sha256'] = hashlib.sha256(_canonical(report)).hexdigest()
    return report


def build_identity_union(request, read_bytes, deadline_check):
    """CP2 historical identity-union consumer; observation only.

    Never raises Exception: every defect, gap, uncertainty or late completion is a HELD report naming the exact
    unfulfilled prerequisite. BaseException propagates after the bounded callback log is retained and a partial
    record is attached as parent_release_identity_partial. CLOSED_CONDITIONAL is the strongest state and remains
    conditional on the listed external conditions; it is not release authority.
    """
    st, io = _State(U_CAUSES), _Io(read_bytes, deadline_check)
    item, analyses, members, unknowns, rows = None, [], [], [], None
    try:
        try:
            if not callable(read_bytes) or not callable(deadline_check):
                st.fire('U_CALLBACKS_INVALID', 'read_bytes and deadline_check must be callable')
            elif not io.tick('union start'):
                st.fire('U_DEADLINE', 'original deadline unavailable at union start')
            else:
                detached = _guard(io, st, 'U_REQUEST_INVALID', 'request', None, _request, request)
                if detached is not _FAILED:
                    item = detached['item']
                    _guard(io, st, 'U_FAMILY_INVALID', 'families', None, _v_families, detached)
                    for index, history in enumerate(detached['histories']):
                        analyses.append(_analyze(io, st, item, index, history))
                    members = [m for a in analyses for m in a['members']]
                    unknowns = [u for a in analyses for u in a['unknowns']]
                    _guard(io, st, 'U_CAP_EXCEEDED', 'caps', None, _caps, members, unknowns)
                    built = _guard(io, st, 'U_ROW_CONFLICT', 'rows', None, _rows, members)
                    rows = None if built is _FAILED else built
        except _Crossed as exc:
            st.fire('U_DEADLINE', _why(exc))
        except Exception as exc:
            st.fire('U_INTERNAL_ERROR', _why(exc))
        try:
            report = _union_report(st, io, item, analyses, members, unknowns, rows)
        except Exception as exc:
            st.fire('U_INTERNAL_ERROR', 'assembly: ' + _why(exc))
            report = _minimal_report(st, item)
        if callable(deadline_check) and not io.crossed and not io.tick('union result assembled'):
            st.fire('U_DEADLINE', 'original deadline crossed during union result assembly')
            try:
                report = _union_report(st, io, item, analyses, members, unknowns, rows)
            except Exception as exc:
                st.fire('U_INTERNAL_ERROR', 'assembly: ' + _why(exc))
                report = _minimal_report(st, item)
        return report
    except BaseException as exc:
        _attach(exc, 'parent_release_identity_partial', {'causes': st.causes(), 'callbacks': list(io.log)})
        raise


# ---------------------------------------------------------------- endedness join
def _v_union(union):
    _require(type(union) is dict and union.get('format') == UNION_FORMAT and _hex(union.get('union_sha256')),
             'union format/digest field')
    body = {key: value for key, value in union.items() if key != 'union_sha256'}
    _require(hashlib.sha256(_canonical(body)).hexdigest() == union['union_sha256'],
             'union digest mismatch: mutated or foreign report')
    members = union.get('members')
    _require(type(members) is list and len(members) <= MAX_MEMBERS, 'union members')
    uids, by_pid, pids, pgids = set(), {}, set(), set()
    for member in members:
        _require(type(member) is dict and _u64(member.get('uniqueid')) and _u32(member.get('pid'))
                 and type(member.get('pgids')) is list and all(_u32(g) for g in member['pgids']), 'member shape')
        uids.add(member['uniqueid'])
        by_pid.setdefault(member['pid'], set()).add(member['uniqueid'])
        pids.add(member['pid'])
        pgids.update(member['pgids'])
    _require(_exact(union.get('historical_pids'), sorted(pids)) and _exact(union.get('historical_pgids'), sorted(pgids)),
             'historical pid/pgid sets differ from members')
    return {'uids': uids, 'by_pid': by_pid, 'pids': pids, 'pgids': pgids}


def _v_log(log):
    _require(type(log) is CensusLog, 'census log must be the CensusLog returned by make_census')
    served = list(log.served)
    _require(served, 'no served census snapshot: the census callback was never answered')
    return served


def _snapshot(st, sets, snap):
    tag = 'call %d' % snap['call']
    if snap['complete'] is not True:
        st.fire('E_CENSUS_INCOMPLETE', tag + ' served snapshot incomplete')
    if snap['observer_ok'] is not True:
        st.fire('E_OBSERVER_UNCOVERED', tag + ' observer bracket/coverage failed')
    for p in snap['rows']:
        where = '%s pid=%d ppid=%d pgid=%d uid=%d' % (tag, p['pid'], p['ppid'], p['pgid'], p['uniqueid'])
        if p['uniqueid'] in sets['uids']:
            st.fire('E_MEMBER_ALIVE', where)
        owners = sets['by_pid'].get(p['pid'])
        if owners is not None and p['uniqueid'] not in owners:
            st.fire('E_PID_REUSE_AMBIGUOUS', where)
        if p['pgid'] in sets['pgids']:
            st.fire('E_GROUP_NONEMPTY', where)
        if p['ppid'] in sets['pids']:
            st.fire('E_PID_CHILD_PRESENT', where)
    return True


def evaluate_endedness(union, log, deadline_check):
    """Join the union with EVERY served census snapshot; pure in-memory, original deadline at start and end.

    Never raises Exception (HELD with E_* causes); BaseException propagates. ENDED_CONDITIONAL requires a
    CLOSED_CONDITIONAL union with an intact digest, at least one served snapshot and no alive, reused-pid,
    occupied-group or child-of-historical-pid observation in any of them.
    """
    st, io = _State(E_CAUSES), _Io(None, deadline_check)
    union_sha, snapshots = None, []
    try:
        try:
            if not callable(deadline_check):
                st.fire('E_INTERNAL_ERROR', 'deadline_check must be callable')
            elif not io.tick('endedness start'):
                st.fire('E_DEADLINE', 'original deadline unavailable at endedness start')
            else:
                sets = _guard(io, st, 'E_UNION_DIGEST', 'union', None, _v_union, union)
                if sets is not _FAILED:
                    union_sha = union['union_sha256']
                    if union.get('state') != CLOSED or union.get('causes') != []:
                        st.fire('E_UNION_HELD', 'union state %r causes %r' % (union.get('state'), union.get('causes')))
                served = _guard(io, st, 'E_NO_SERVED_CENSUS', 'census log', None, _v_log, log)
                if served is not _FAILED:
                    keys = ('call', 'attempts', 'complete', 'observer_ok', 'process_count', 'served_sha256',
                            'rows_sha256', 'observed_at_mono')
                    snapshots = [{k: snap[k] for k in keys} for snap in served]
                    if sets is not _FAILED:
                        for snap in served:
                            _snapshot(st, sets, snap)
        except _Crossed as exc:
            st.fire('E_DEADLINE', _why(exc))
        except Exception as exc:
            st.fire('E_INTERNAL_ERROR', _why(exc))
        if callable(deadline_check) and not io.crossed and not io.tick('endedness result assembled'):
            st.fire('E_DEADLINE', 'original deadline crossed during endedness assembly')
        causes = st.causes()
        result = {'format': ENDEDNESS_FORMAT, 'module': MODULE, 'scheme': SCHEME, 'state': ENDED if not causes else HELD,
                  'causes': causes, 'evidence': {c: list(st.evidence[c]) for c in causes},
                  'suppressed': {c: st.suppressed[c] for c in causes if c in st.suppressed},
                  'union_sha256': union_sha, 'snapshots': snapshots, 'deadline_crossed': io.crossed,
                  'callbacks': {'count': io.count, 'sha256': io.digest.hexdigest(), 'log': list(io.log)},
                  'conditions': list(CONDITIONS), 'boundary': BOUNDARY}
        result['endedness_sha256'] = hashlib.sha256(_canonical(result)).hexdigest()
        return result
    except BaseException as exc:
        _attach(exc, 'parent_release_endedness_partial', {'causes': st.causes(), 'callbacks': list(io.log)})
        raise


def spec_identities_match(union, identities):
    """True only for an intact CLOSED_CONDITIONAL union whose PRT rows typed-equal spec.identities."""
    try:
        _v_union(union)
        return union.get('state') == CLOSED and type(union.get('prt_identities')) is list \
            and _exact(union['prt_identities'], identities)
    except Exception:
        return False
