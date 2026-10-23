"""SOURCE ONLY, UNEXECUTED. Raw owned_supervisor_v19 evidence -> beta_parent_adapter_v3 input records bridge (v2).

Scope:     RUN/control/beta-supervisor19-scope-v1.json      4087d6f9eab6034f142d9706972774cbea04aed982fe7600f2753129f602315c
Interface: RUN/control/beta-supervisor19-interface-v1.json  91f709f6dc9b07a7d9c36bf2593dcae21175ffaaf0fbd8c3ca883591612b3086
Corrected: RUN/control/beta-supervisor19-interface-v2.json  073222bf77f4666ff9f584245d1f6f085e7f8f9c220a3d7a0c93590824fc31fa
Repair:    RUN/control/beta-supervisor19-v2-repair-scope-v1.json  64fe152a54e26aec87c7f150c72ba540f414a57ed4298e931d33ee4617c96fbd
Replaces:  RUN/control/beta_supervisor19_adapter_v1.py      fb857b959da63365bd39f438e99c5ee9b7dbe4e2286b003f5ec579419c33ab1c (HOLD)
Supervisor: physics rqls10 code/owned_supervisor_v19.py     cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93

    result = build_beta_inputs(request_ref, reader, deadline_check)

Pure consumer. It imports only copy/hashlib/json/math, performs no filesystem, process, signal, clock or /bin/date
operation of its own and writes nothing. Every byte comes from the CALLER-OWNED beta_parent_reader_v1 EvidenceReader
through read_bytes(path, cap) followed by last_file(path); report() is read once at the end. The bridge never
constructs, closes or replaces that reader; the caller retains it on every exception. Nothing runs at import.

Expected values come ONLY from parent authority (the pinned request, its expected GO/config, the pinned plan v5).
Actual values come ONLY from bound supervisor19 evidence (parent publication binding of the receipt, the actual
config/GO/launch record it names, MAIN stream records and their original-created capture files) and from the
parent's explicit external evidence (PRT wait doc, V9 captures of the supervisor process, identity union, freeze).
Equality checks between independent records are necessary joins, NEVER authenticity: matching JSON or SHA256
authenticates selected bytes, not their origin. Authenticity of the request, waits, captures, union, freeze, GO,
config, prefix and deadline remains the parent's external obligation (EXTERNAL_PREREQUISITES).

Sticky supervisor histories (interface-v2 C1-C3): every receipt or ACK unproved_history uniqueid, every ACK
coverage_history gap and every ACK contract violation is an always-blocking settlement label. No parent identity-union
status (ENDED_PROVED, PID-only or otherwise) waives it. The ACK histories must extend the receipt histories, so
post-receipt census retries are retained.

Missing, ambiguous, contradictory or unbound evidence yields state HELD with ordered causes and NO records. There
is no partial, default or success fallback. READY records are canonical JSON text the parent must publish
exclusively itself before calling beta_parent_adapter_v3.evaluate_pinned(result['adapter3_inputs'], reader, check).
READY is NOT an audit verdict, PASS, settlement, release, canonical audit, runtime or scientific authority.

The original deadline_check is called before and after every acquisition and after the complete result is assembled;
a raise or non-None return is HELD with no further acquisitions. Non-Exception BaseExceptions propagate unchanged.
Not implemented here (external): PRT five-part transaction, CP1 release integration, CP2 union completeness proof,
synthetic derivation contexts, the N1 fault-driver adapter and the two-link supervisor settlement record.
"""
import copy
import hashlib
import json
import math

RUN = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h'
MOLS = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39'
PLAN_PATH = MOLS + '/evidence/ext-search-plan-v5.json'
PLAN_SHA = '254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731'
GATE_PATH = MOLS + '/code/ext4_gate.py'
CAPTURE4_PATH = RUN + '/control/beta_capture_audit_v4.py'
SCHEMA2_PATH = RUN + '/control/beta_schema_audit_v2.py'
SUPERVISOR_VERSION = 'owned_supervisor_v19'
SUPERVISOR_SHA = 'cb828a78367dc2023bfc6e330696745f186f186811752361472747e5fe547e93'

REQUEST_FORMAT = 'beta-supervisor19-bridge-request-v1'
UNION_FORMAT = 'beta-supervisor19-identity-union-v1'
RESULT_FORMAT = 'beta-supervisor19-bridge-result-v1'
WAIT_FORMAT = 'parent-release-wait-v1'
FREEZE_FORMAT = 'beta-parent-publication-freeze-v1'
EXPECTATION_FORMAT = 'beta-parent-audit-expectation-v1'
OBSERVATION_FORMAT = 'beta-parent-audit-observation-v1'
CONTEXT_FORMAT = 'beta-parent-schema-context-v2'
UNION_COMPLETENESS = 'PARENT_ATTESTED_COMPLETE_HISTORICAL_UNION'
DATE_KIND = 'SUPERVISOR19_OWNED_BIN_DATE'
MODES = ('PLAN', 'FIXTURE')
STATE_EXIT = {'SETTLED': 0, 'UNSETTLED': 11}
JSON_CAP = 1 << 20
LARGE_CAP = 16 << 20  # beta_parent_reader_v1 MAX_CAP; larger evidence is READ_FAILED, never truncated
DETAIL_CAP = 600
EVIDENCE_ROWS = 64
PLAN_JOBS = 20

REQUEST_KEYS = frozenset(('format', 'mode', 'item', 'plan', 'job_dir', 'expected', 'parent_wait', 'parent_captures',
                          'publication', 'identity_union', 'context', 'publication_freeze', 'publish_paths'))
EXPECTED_KEYS = frozenset(('go', 'config', 'source_pins', 'input_pins', 'date_start', 'date_end'))
REQUEST_CONTEXT_KEYS = frozenset(('original_dm21', 'prefix'))
PUBLISH_NAMES = ('expectation', 'observation', 'context')
STREAM_NAMES = ('stdout', 'stderr')
V9_CAPTURE_KEYS = frozenset(('path', 'sha256', 'bytes', 'inode', 'eof'))
RECEIPT_BINDING_KEYS = frozenset(('path', 'sha256', 'bytes', 'inode', 'nlink'))
WAIT_KEYS = frozenset(('format', 'item', 'role', 'pid', 'pgid', 'start_fingerprint', 'raw_status', 'actual_exit',
                       'observed_by'))
UNION_KEYS = frozenset(('format', 'item', 'receipt_sha256', 'completeness', 'identities'))
UNION_ROW_KEYS = frozenset(('role', 'pid', 'pgid', 'start_fingerprint', 'uniqueid', 'source', 'status'))
UNION_ROLES = frozenset(('driver', 'main_child', 'helper', 'descendant', 'unproved', 'oracle', 'oracle_child',
                         'oracle_helper'))
UNION_STATUSES = ('ENDED_PROVED', 'UNRESOLVED')
FREEZE_KEYS = frozenset(('format', 'mode', 'job_dir', 'immutable_paths', 'prefix_authority'))
PREFIX_ROW_KEYS = frozenset(('item', 'files', 'audit'))
METADATA_KEYS = ('dev', 'ino', 'mode', 'nlink', 'size', 'mtime_ns', 'ctime_ns')
# Exact supervisor19 CONFIG key set (39 names, copied from owned_supervisor_v19.CONFIG).
CONFIG_KEYS = frozenset((
    'item', 'owner', 'purpose', 'lane', 'argv', 'env', 'stdout', 'stderr', 'stdout_cap_bytes', 'stderr_cap_bytes',
    'samples', 'samples_cap_bytes', 'launch_record', 'receipt', 'settlement_record', 'outputs', 'output_roots', 'pins',
    'max_wall_s', 'settle_s', 'sample_s', 'max_chunk_seconds', 'owned_compute_settled_by_epoch', 'rss_trip_bytes',
    'rss_projection_bytes', 'free_trip_bytes', 'launch_free_min_bytes', 'output_trip_bytes', 'lane_roots',
    'lane_disk_root', 'lane_disk_ceiling_bytes', 'lane_walk_s', 'busy_limit', 'busy_cpu_fraction', 'cpu_slots',
    'admission', 'helper_budget', 'fault_injection', 'creation_channel'))
ADMISSION_KEYS = frozenset(('go_path', 'stability_receipt_path', 'reservation_bytes', 'outstanding_reservations_bytes',
                            'lane_outstanding_reservations_bytes', 'stability_max_age_s'))
IDENTITY_KEYS = frozenset(('pid', 'ppid', 'pgid', 'status', 'euid', 'ruid', 'traced', 'comm', 'uniqueid', 'idversion'))
IDENTITY_INTS = ('pid', 'ppid', 'pgid', 'status', 'euid', 'ruid', 'uniqueid', 'idversion')
MAIN_WAIT_KEYS = frozenset(('pid', 'native_wait_result', 'raw_wait_status', 'leader_reaped', 'rc', 'mono_reaped',
                            'epoch_reaped'))
AUTHORIZATION_KEYS = frozenset(('go_sha256', 'stability_receipt_sha256', 'not_after_epoch', 'stability_epoch',
                                'stability_date'))
STREAM_COUNTERS = ('bytes_seen', 'bytes_written', 'cap_bytes', 'pending_bytes', 'prefix_bytes')
STREAM_FLAGS = ('overflow', 'write_inflight', 'closed', 'hash_pending', 'eof_seen', 'fsync_returned', 'out_closed',
                'pipe_closed')
STREAM_MONOS = ('mono_created', 'mono_last_update', 'mono_last_read', 'mono_last_write', 'mono_eof',
                'mono_close_completed')
STREAM_KEYS = frozenset(STREAM_COUNTERS + STREAM_FLAGS + STREAM_MONOS + ('error', 'sha256_prefix', 'sha256_written'))
ARTIFACT_KEYS = frozenset(('sha256', 'bytes', 'inode', 'nlink', 'birth_epoch'))
HELPER_KEYS = ('pid', 'identity', 'settled', 'signal')  # interface-v2 C4: mandatory in every receipt helper row
LAUNCH_KEYS = frozenset(('supervisor', 'supervisor_sha256', 'config_sha256', 'supervisor_pid', 'identity', 'argv', 'cwd',
                         'env', 'mono_spawn', 'epoch_spawn', 'start_date', 'baseline_count', 'authorization',
                         'launch_commit', 'cpu_slots', 'reservation_bytes'))
ACK_KEYS = frozenset(('supervisor', 'acknowledged', 'exit_code', 'settlement', 'config_sha256', 'receipt_sha256',
                      'settlement_record_sha256', 'receipt_bytes', 'settlement_bytes', 'post_publish_mono',
                      'ack_commit', 'publication_resources', 'ack_resources', 'publication_payload_bytes',
                      'child_returncode', 'failure_codes', 'owned_live', 'unproved_live', 'ack_census',
                      'contract_violations', 'unproved_history', 'coverage_history', 'census_observations',
                      'reconciliation'))
RECEIPT_REQUIRED = ('supervisor', 'supervisor_sha256', 'config_sha256', 'config_path', 'supervisor_pid', 'settlement',
                    'child_pid', 'child_identity', 'child_returncode', 'wait_status_lost', 'timing_failed',
                    'raw_acquisitions', 'main_wait', 'failures', 'trips', 'stop_request', 'signal',
                    'owned_identities', 'contract_violations', 'clear', 'unproved_history', 'coverage_history',
                    'history_overflow', 'helpers', 'streams', 'loop_status', 'artifacts', 'output_root_inventory',
                    'authorization', 'final_census', 'cancel')
TAMPER_CODES = frozenset(('ARTIFACT_IDENTITY_CHANGED', 'EVIDENCE_MUTATED', 'ARTIFACT_UNREADABLE', 'EVIDENCE_MISSING'))

HELD_CAUSES = (
    'REQUEST_INVALID', 'AUTHORITY_PIN_MISMATCH', 'PLAN_ITEM_INVALID', 'EXPECTED_GO_INVALID', 'EXPECTED_CONFIG_INVALID',
    'PARENT_WAIT_INVALID', 'SUPERVISOR_CAPTURE_UNBOUND', 'SUPERVISOR_ACK_INVALID', 'SUPERVISOR_EXIT_NOT_ELIGIBLE',
    'RECEIPT_UNBOUND', 'RECEIPT_INVALID', 'RECEIPT_EVIDENCE_INCOMPLETE', 'ACTUAL_CONFIG_INVALID', 'ACTUAL_GO_INVALID',
    'LAUNCH_RECORD_INVALID', 'NESTED_EXIT_UNAVAILABLE', 'MAIN_STREAM_UNBOUND', 'EVIDENCE_TAMPER_REPORTED',
    'ARTIFACT_UNBOUND', 'DATE_UNAVAILABLE', 'PIN_CLASSIFICATION_INVALID', 'IDENTITY_UNION_INVALID', 'CONTEXT_INVALID',
    'FREEZE_INVALID', 'FREEZE_COVERAGE_INCOMPLETE', 'READ_FAILED', 'DEADLINE', 'READER_UNRESOLVED',
    'BRIDGE_INTERNAL_EXCEPTION')
EXTERNAL_PREREQUISITES = (
    'REQUEST_GO_CONFIG_PLAN_AUTHORITY_AND_GENUINE_PREFIX_TRANSACTIONS',
    'AUTHENTIC_PARENT_RAW_WAIT_HISTORY_OF_THE_SUPERVISOR_PROCESS',
    'V9_PARENT_CAPTURE_ORIGINAL_CREATED_DESCRIPTOR_PROVENANCE',
    'RECEIPT_ORIGINAL_PUBLICATION_IDENTITY_BINDING',
    'COMPLETE_HISTORICAL_IDENTITY_UNION_AND_ENDEDNESS_CP2',
    'EXCLUSIVE_IMMUTABLE_PUBLICATION_FREEZE_FILES_NAMESPACES_ALIASES',
    'ORIGINAL_DEADLINE_AND_TRUSTED_INTERPRETER_IMPORT_STATE',
    'CALLER_RETAINS_GLOBAL_READER_REPORT_AND_OWNERSHIP',
    'TWO_LINK_SUPERVISOR_SETTLEMENT_RECORD_NOT_CONSUMED',
    'PARENT_EXCLUSIVE_PUBLICATION_OF_RECORDS_THEN_ADAPTER3_AND_FIVE_PART_PRT_CP1')


class _Held(Exception):
    """One fail-closed HELD cause raised inside a stage; never success."""

    def __init__(self, cause, detail):
        Exception.__init__(self, cause, detail)
        self.cause, self.detail = cause, detail


class _Stop(Exception):
    """The original deadline failed: no further acquisition or evaluation; result is HELD."""


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _hex64(value):
    return type(value) is str and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def _norm_abs(path):
    if type(path) is not str or not path.startswith('/') or '\x00' in path:
        return False
    parts = path.split('/')[1:]
    return bool(parts) and all(part not in ('', '.', '..') for part in parts)


def _below(path, root):
    return path == root or path.startswith(root + '/')


def _plain(name):
    return type(name) is str and name not in ('', '.', '..') and '/' not in name and '\x00' not in name


def _int(value, low=None):
    return type(value) is int and (low is None or value >= low)


def _text(value):
    return type(value) is str and value != ''


def _same_str(value, want):
    return type(value) is str and type(want) is str and value == want


def _keys(record, keys):
    return type(record) is dict and all(type(k) is str for k in record) and set(record) == set(keys)


def _exact(left, right):
    """Typed JSON equality: bool never equals int, int never equals float, nonfinite never equal."""
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return (all(type(k) is str for k in left) and all(type(k) is str for k in right)
                and set(left) == set(right) and all(_exact(left[k], right[k]) for k in left))
    if type(left) is list:
        return len(left) == len(right) and all(_exact(a, b) for a, b in zip(left, right))
    if type(left) is float:
        return math.isfinite(left) and math.isfinite(right) and left == right
    if left is None or type(left) in (str, int, bool):
        return left == right
    return False


def _inode(value):
    return type(value) is list and len(value) == 2 and _int(value[0], 0) and _int(value[1], 1)


def _ref(value):
    return _keys(value, ('path', 'sha256')) and _norm_abs(value['path']) and _hex64(value['sha256'])


def _pin_map(value):
    return type(value) is dict and all(_norm_abs(k) and _hex64(v) for k, v in value.items())


def _identity(value):
    return (_keys(value, IDENTITY_KEYS) and all(type(value[k]) is int for k in IDENTITY_INTS)
            and value['pid'] > 0 and value['uniqueid'] > 0 and type(value['traced']) is bool
            and type(value['comm']) is str)


def _finite_or_none(value):
    return value is None or (type(value) in (int, float) and math.isfinite(value))


def _metadata(after):
    return _keys(after, METADATA_KEYS) and all(type(after[k]) is int for k in METADATA_KEYS)


def _date_text(value):
    """Shape of an owned `/bin/date +%Y-%m-%dT%H:%M:%S%z` reading; ASCII digits only. Never a parsed clock."""
    if type(value) is not str or len(value) != 24:
        return False
    digits = value[:4] + value[5:7] + value[8:10] + value[11:13] + value[14:16] + value[17:19] + value[20:24]
    return (value[4] == '-' and value[7] == '-' and value[10] == 'T' and value[13] == ':' and value[16] == ':'
            and value[19] in ('+', '-') and len(digits) == 18 and all(c in '0123456789' for c in digits))


def _exit_from_status(status):
    """macOS/BSD wait-status decode equal to os.waitstatus_to_exitcode for terminal statuses; else None."""
    if type(status) is not int or not 0 <= status < (1 << 31):
        return None
    low = status & 0x7f
    if low == 0:
        return (status >> 8) & 0xff
    if low == 0x7f:
        return None  # stopped/continued or invalid: not a terminal exit
    return -low


def _parse(data, cause, label):
    """Strict JSON: UTF-8, duplicate keys and nonfinite numbers/constants rejected."""
    def pairs(rows):
        out = {}
        for key, value in rows:
            if key in out:
                raise ValueError('duplicate JSON key')
            out[key] = value
        return out

    def constant(text):
        raise ValueError('nonfinite JSON constant')

    def number(text):
        value = float(text)
        if not math.isfinite(value):
            raise ValueError('nonfinite JSON number')
        return value
    try:
        return json.loads(data.decode('utf-8'), object_pairs_hook=pairs, parse_constant=constant, parse_float=number)
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise _Held(cause, label + ': strict JSON parse failed: ' + type(exc).__name__)


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False) + '\n'


def _census(value):
    return (type(value) is dict and type(value.get('complete')) is bool and type(value.get('owned_live')) is list
            and type(value.get('unproved_live')) is list and type(value.get('group_live')) is list
            and all(_int(pid, 0) for pid in value['group_live']))


class _State:
    """Per-call evidence state. Private coherent cache: each path is acquired once per call."""

    def __init__(self, reader, deadline_check):
        self.reader, self.check = reader, deadline_check
        self.causes, self.evidence = set(), []
        self.cache, self.consumed = {}, []
        self.stopped = False

    def hold(self, cause, detail):
        if cause not in HELD_CAUSES:
            cause = 'BRIDGE_INTERNAL_EXCEPTION'
        self.causes.add(cause)
        if len(self.evidence) < EVIDENCE_ROWS:
            self.evidence.append({'cause': cause, 'detail': str(detail)[:DETAIL_CAP]})

    def tick(self):
        if self.stopped:
            raise _Stop()
        try:
            value = self.check()
        except Exception as exc:
            self.stopped = True
            self.hold('DEADLINE', 'deadline_check raised ' + type(exc).__name__)
            raise _Stop()
        if value is not None:
            self.stopped = True
            self.hold('DEADLINE', 'deadline_check returned a non-None value')
            raise _Stop()

    def stage(self, function, *args):
        """A _Held records its cause and yields None; _Stop, other Exceptions and BaseExceptions propagate."""
        try:
            return function(self, *args)
        except _Held as held:
            self.hold(held.cause, held.detail)
            return None

    def acquire(self, role, path, cap, cause):
        """One actual reader acquisition per path; the current completed observation must match the bytes."""
        if not _norm_abs(path):
            raise _Held(cause, role + ': acquisition path is not normalized absolute')
        self.tick()
        entry = self.cache.get(path)
        if entry is not None:
            if len(entry['data']) > cap:
                raise _Held('READ_FAILED', role + ': cached acquisition exceeds a stricter cap')
            if role not in entry['row']['roles']:
                entry['row']['roles'].append(role)
            return entry['data'], entry['after']
        try:
            data = self.reader.read_bytes(path, cap)
        except Exception as exc:
            raise _Held('READ_FAILED', role + ': reader refused or failed: ' + type(exc).__name__)
        try:
            meta = self.reader.last_file(path)
        except Exception as exc:
            raise _Held('READ_FAILED', role + ': last_file failed: ' + type(exc).__name__)
        after = meta.get('after') if type(meta) is dict else None
        if (type(data) is not bytes or len(data) > cap or type(meta) is not dict or meta.get('path') != path
                or meta.get('completed') is not True or meta.get('bytes_seen') != len(data)
                or meta.get('sha256') != _sha(data) or not _metadata(after) or after['size'] != len(data)):
            raise _Held('READ_FAILED', role + ': current completed acquisition not established')
        after = copy.deepcopy(after)
        row = {'roles': [role], 'path': path, 'sha256': _sha(data), 'length': len(data),
               'metadata': {k: after[k] for k in METADATA_KEYS}}
        self.cache[path] = {'data': data, 'after': after, 'row': row}
        self.consumed.append(row)
        self.tick()
        return data, after

    def pinned(self, role, ref, cap, cause):
        if not _ref(ref):
            raise _Held(cause, role + ': exact {path,sha256} reference required')
        data, after = self.acquire(role, ref['path'], cap, cause)
        if _sha(data) != ref['sha256']:
            raise _Held(cause, role + ': acquired bytes differ from the pinned sha256')
        return data, after

    def result(self, records, reader_unresolved):
        ready = records is not None and not self.causes
        out = {'format': RESULT_FORMAT, 'state': 'READY' if ready else 'HELD',
               'held_causes': [cause for cause in HELD_CAUSES if cause in self.causes],
               'held_evidence': copy.deepcopy(self.evidence),
               'records': copy.deepcopy(records) if ready else None,
               'adapter3_inputs': ({name: {'path': records[name]['path'], 'sha256': records[name]['sha256']}
                                    for name in PUBLISH_NAMES} if ready else None),
               'consumed': copy.deepcopy(self.consumed),
               'reader_unresolved': copy.deepcopy(reader_unresolved),
               'external_prerequisites_not_verified': list(EXTERNAL_PREREQUISITES),
               'authority': {'release': False, 'canonical_audit': False, 'runtime': False, 'scientific': False,
                             'publication_performed': False}}
        return out


def build_beta_inputs(request_ref, reader, deadline_check):
    """Return READY canonical expectation/observation/context records or HELD with ordered causes and no records."""
    state = _State(reader, deadline_check)
    records, reader_unresolved, reported = None, None, False
    try:
        if not callable(deadline_check):
            state.stopped = True
            state.hold('DEADLINE', 'deadline_check is not callable')
        else:
            assembled = _evaluate(state, request_ref)
            reader_unresolved, reported = _reader_unresolved(state), True
            if assembled is not None and not state.causes:
                records = _records(assembled)
            state.tick()  # Original deadline AFTER complete assembly; a late result is never READY.
    except _Stop:
        pass
    except Exception as exc:
        state.hold('BRIDGE_INTERNAL_EXCEPTION', repr(exc))
    if not reported:
        reader_unresolved = _reader_unresolved(state)  # In-memory report only; HELD is already certain.
    return state.result(records, reader_unresolved)


def _reader_unresolved(st):
    try:
        report = st.reader.report()
    except Exception as exc:
        st.hold('READER_UNRESOLVED', 'caller reader report unavailable: ' + type(exc).__name__)
        return None
    unresolved = report.get('unresolved') if type(report) is dict else None
    if type(unresolved) is not list:
        st.hold('READER_UNRESOLVED', 'caller reader report lacks an unresolved list')
        return None
    if unresolved:
        st.hold('READER_UNRESOLVED', 'caller reader retains unresolved acquisitions or closes')
    return copy.deepcopy(unresolved)


def _evaluate(st, request_ref):
    """Independent stages accumulate causes; dependents of a failed stage are skipped (already HELD)."""
    req = st.stage(_request, request_ref)
    if req is None:
        return None
    plan = st.stage(_plan, req)
    st.stage(_expected_go, req)
    expected_cfg = st.stage(_expected_config, req)
    if expected_cfg is not None:
        st.stage(_expected_pins, req, expected_cfg)
    wait = st.stage(_parent_wait, req)
    if wait is not None:
        st.stage(_eligible_exit, wait)
    ack = st.stage(_ack, req)
    rinfo = st.stage(_receipt, req)
    receipt = None if rinfo is None else rinfo['receipt']
    identities = hist = None
    if receipt is not None:
        st.stage(_receipt_complete, receipt)
        st.stage(_tamper, receipt)
        identities = st.stage(_receipt_identities, receipt, ack)
        if identities is not None and ack is not None:
            hist = st.stage(_ack_histories, ack, receipt, identities)
        if wait is not None:
            st.stage(_wait_joins, wait, receipt)
        if wait is not None and ack is not None:
            st.stage(_ack_joins, ack, wait, rinfo)
    nested = st.stage(_nested_exit, receipt) if receipt is not None else None
    cfg = st.stage(_actual_config, rinfo) if rinfo is not None else None
    go = launch = arts = pins = None
    captures = {}
    if cfg is not None:
        go = st.stage(_actual_go, cfg, receipt)
        launch = st.stage(_launch, cfg, receipt)
        for name in STREAM_NAMES:
            captures[name] = st.stage(_main_capture, name, cfg, receipt)
        arts = st.stage(_artifacts, cfg, receipt)
        pins = st.stage(_actual_pins, req, cfg)
    dates = st.stage(_dates, receipt, rinfo) if receipt is not None else None
    union = None
    if receipt is not None and wait is not None and hist is not None:
        union = st.stage(_union, req, receipt, rinfo, wait, hist)
    settlement = None
    if receipt is not None and ack is not None and union is not None and hist is not None:
        settlement = st.stage(_settlement, receipt, ack, union, hist)
    authority = st.stage(_context, req, plan) if plan is not None else None
    freeze = st.stage(_freeze, req, authority) if authority is not None else None
    if freeze is not None and plan is not None and expected_cfg is not None and cfg is not None and rinfo is not None:
        st.stage(_coverage, req, plan, expected_cfg, cfg, rinfo, freeze)
    if st.causes:
        return None
    return {'req': req, 'plan': plan, 'expected_cfg': expected_cfg, 'cfg': cfg, 'go': go, 'launch': launch,
            'nested': nested, 'captures': captures, 'arts': arts, 'rinfo': rinfo, 'settlement': settlement,
            'pins': pins, 'dates': dates}


def _v9(record):
    return (_keys(record, V9_CAPTURE_KEYS) and _norm_abs(record['path']) and _hex64(record['sha256'])
            and _int(record['bytes'], 0) and _inode(record['inode']) and record['eof'] is True)


def _request(st, ref):
    data, _ = st.pinned('request', ref, JSON_CAP, 'REQUEST_INVALID')
    req = _parse(data, 'REQUEST_INVALID', 'request')
    if not _keys(req, REQUEST_KEYS) or not _same_str(req['format'], REQUEST_FORMAT):
        raise _Held('REQUEST_INVALID', 'request exact keys/format')
    if type(req['mode']) is not str or req['mode'] not in MODES or not _text(req['item']) or not _norm_abs(req['job_dir']):
        raise _Held('REQUEST_INVALID', 'mode/item/job_dir')
    if not all(_ref(req[key]) for key in ('plan', 'parent_wait', 'identity_union', 'publication_freeze')):
        raise _Held('REQUEST_INVALID', 'plan/parent_wait/identity_union/publication_freeze references')
    expected = req['expected']
    if (not _keys(expected, EXPECTED_KEYS) or not _ref(expected['go']) or not _ref(expected['config'])
            or not _pin_map(expected['source_pins']) or not _pin_map(expected['input_pins'])
            or type(expected['date_start']) is not dict or not expected['date_start']
            or type(expected['date_end']) is not dict or not expected['date_end']):
        raise _Held('REQUEST_INVALID', 'expected authority fields')
    captures = req['parent_captures']
    if not _keys(captures, STREAM_NAMES) or not all(_v9(captures[name]) for name in STREAM_NAMES):
        raise _Held('REQUEST_INVALID', 'parent_captures must be exact V9 {path,sha256,bytes,inode,eof:true} records')
    if captures['stdout']['path'] == captures['stderr']['path'] or captures['stdout']['inode'] == captures['stderr']['inode']:
        raise _Held('REQUEST_INVALID', 'parent stdout/stderr captures must be distinct paths and inodes')
    publication = req['publication']
    binding = publication.get('receipt') if type(publication) is dict else None
    if (not _keys(publication, ('receipt',)) or not _keys(binding, RECEIPT_BINDING_KEYS) or not _norm_abs(binding['path'])
            or not _hex64(binding['sha256']) or not _int(binding['bytes'], 0) or not _inode(binding['inode'])
            or type(binding['nlink']) is not int or binding['nlink'] != 1):
        raise _Held('REQUEST_INVALID', 'publication.receipt binding')
    context = req['context']
    if not _keys(context, REQUEST_CONTEXT_KEYS) or not _ref(context['original_dm21']) or type(context['prefix']) is not list:
        raise _Held('REQUEST_INVALID', 'context original_dm21/prefix')
    publish = req['publish_paths']
    if not _keys(publish, PUBLISH_NAMES) or not all(_norm_abs(publish[name]) for name in PUBLISH_NAMES):
        raise _Held('REQUEST_INVALID', 'publish_paths')
    paths = [publish[name] for name in PUBLISH_NAMES]
    if len(set(paths)) != len(paths) or any(_below(path, req['job_dir']) for path in paths):
        raise _Held('REQUEST_INVALID', 'publish paths must be distinct and outside job_dir')
    return req


def _plan_tables(plan):
    if type(plan) is not dict or type(plan.get('jobs')) is not list or type(plan.get('order')) is not list:
        raise _Held('PLAN_ITEM_INVALID', 'plan jobs/order')
    table = {}
    for job in plan['jobs']:
        if type(job) is not dict or type(job.get('item')) is not str or job['item'] in table:
            raise _Held('PLAN_ITEM_INVALID', 'plan job identity')
        outputs = job.get('outputs')
        if (type(job.get('exit')) is not int or type(outputs) is not list or not outputs
                or not all(_plain(name) for name in outputs) or len(set(outputs)) != len(outputs)):
            raise _Held('PLAN_ITEM_INVALID', 'plan job exit/outputs')
        table[job['item']] = job
    order = plan['order']
    if len(table) != PLAN_JOBS or order != [job['item'] for job in plan['jobs']]:
        raise _Held('PLAN_ITEM_INVALID', 'plan order must list exactly the twenty jobs')
    calibrations = plan.get('future_calibration_jobs')
    if type(calibrations) is not list or any(type(c) is not dict or type(c.get('item')) is not str or c['item'] in table
                                              for c in calibrations):
        raise _Held('PLAN_ITEM_INVALID', 'calibration items must stay outside the twenty jobs')
    for key in ('dm21_path', 'base_dir', 'audit_dir'):
        if not _norm_abs(plan.get(key)):
            raise _Held('PLAN_ITEM_INVALID', 'plan ' + key)
    if not _hex64(plan.get('dm21_sha256')):
        raise _Held('PLAN_ITEM_INVALID', 'plan dm21_sha256')
    return table, order


def _plan(st, req):
    if not _exact(req['plan'], {'path': PLAN_PATH, 'sha256': PLAN_SHA}):
        raise _Held('AUTHORITY_PIN_MISMATCH', 'request plan is not the pinned ext-search-plan-v5')
    data, _ = st.pinned('plan', req['plan'], JSON_CAP, 'AUTHORITY_PIN_MISMATCH')
    plan = _parse(data, 'PLAN_ITEM_INVALID', 'plan')
    table, order = _plan_tables(plan)
    item = req['item']
    if item not in table:
        raise _Held('PLAN_ITEM_INVALID', 'item is not one of the twenty plan jobs (calibrations excluded)')
    job = table[item]
    if req['mode'] == 'PLAN':
        args = job.get('args')
        if type(args) is not list or not all(type(a) is str for a in args):
            raise _Held('PLAN_ITEM_INVALID', 'plan job args')
        hits = [i for i, arg in enumerate(args) if arg == '--job-root']
        if len(hits) != 1 or hits[0] + 1 >= len(args) or args[hits[0] + 1] != req['job_dir']:
            raise _Held('PLAN_ITEM_INVALID', 'PLAN job_dir must equal the plan job --job-root')
    elif any(_below(req['job_dir'], plan[key]) for key in ('base_dir', 'audit_dir')):
        raise _Held('PLAN_ITEM_INVALID', 'FIXTURE job_dir may not be inside the plan run or audit directory')
    return {'plan': plan, 'jobs': table, 'order': order, 'job': job, 'position': order.index(item)}


def _expected_go(st, req):
    data, _ = st.pinned('expected_go', req['expected']['go'], JSON_CAP, 'EXPECTED_GO_INVALID')
    go = _parse(data, 'EXPECTED_GO_INVALID', 'expected GO')
    if (type(go) is not dict or not _same_str(go.get('decision'), 'GO') or not _same_str(go.get('item'), req['item'])
            or not _same_str(go.get('mode'), req['mode']) or not _same_str(go.get('plan_sha256'), PLAN_SHA)
            or type(go.get('configs')) is not dict):
        raise _Held('EXPECTED_GO_INVALID', 'expected GO decision/item/mode/plan_sha256/configs binding')
    if req['expected']['config']['sha256'] not in go['configs']:
        raise _Held('EXPECTED_GO_INVALID', 'expected GO does not name the expected config')
    return go


def _config_shape(cfg, cause):
    if not _keys(cfg, CONFIG_KEYS):
        raise _Held(cause, 'config is not the exact supervisor19 CONFIG key set')
    argv = cfg['argv']
    if (not _text(cfg['item']) or not _norm_abs(cfg['lane']) or type(argv) is not list or not argv
            or not all(type(a) is str for a in argv) or not _norm_abs(argv[0]) or type(cfg['env']) is not dict):
        raise _Held(cause, 'config item/lane/argv/env')
    for key in ('stdout', 'stderr', 'samples', 'launch_record', 'receipt', 'settlement_record'):
        if not _norm_abs(cfg[key]):
            raise _Held(cause, 'config path ' + key)
    for key in ('stdout_cap_bytes', 'stderr_cap_bytes'):
        if not _int(cfg[key], 1):
            raise _Held(cause, 'config ' + key)
    outputs = cfg['outputs']
    if type(outputs) is not list or not all(_keys(o, ('path', 'required')) and _norm_abs(o['path'])
                                            and type(o['required']) is bool for o in outputs):
        raise _Held(cause, 'config outputs')
    if type(cfg['output_roots']) is not list or not all(_norm_abs(root) for root in cfg['output_roots']):
        raise _Held(cause, 'config output_roots')
    if type(cfg['pins']) is not list or not all(_keys(p, ('path', 'sha256')) and _norm_abs(p['path'])
                                                and _hex64(p['sha256']) for p in cfg['pins']):
        raise _Held(cause, 'config pins')
    admission = cfg['admission']
    if not _keys(admission, ADMISSION_KEYS) or not _norm_abs(admission['go_path']):
        raise _Held(cause, 'config admission')
    faults, channel = cfg['fault_injection'], cfg['creation_channel']
    if (type(faults) is not dict or not all(type(k) is str and v is False for k, v in faults.items())
            or type(channel) is not dict or channel):
        raise _Held(cause, 'not a beta science invocation: fault injection or creation channel present')
    return cfg


def _expected_config(st, req):
    data, _ = st.pinned('expected_config', req['expected']['config'], JSON_CAP, 'EXPECTED_CONFIG_INVALID')
    cfg = _config_shape(_parse(data, 'EXPECTED_CONFIG_INVALID', 'expected config'), 'EXPECTED_CONFIG_INVALID')
    if cfg['item'] != req['item']:
        raise _Held('EXPECTED_CONFIG_INVALID', 'expected config item differs from request item')
    return cfg


def _expected_pins(st, req, cfg):
    merged = {}
    for key in ('source_pins', 'input_pins'):
        for path, digest in req['expected'][key].items():
            if path in merged and merged[path] != digest:
                raise _Held('EXPECTED_CONFIG_INVALID', 'request source/input pin maps conflict on one path')
            merged[path] = digest
    declared = {}
    for pin in cfg['pins']:
        if pin['path'] in declared and declared[pin['path']] != pin['sha256']:
            raise _Held('EXPECTED_CONFIG_INVALID', 'expected config pins conflict on one path')
        declared[pin['path']] = pin['sha256']
    if not _exact(merged, declared):
        raise _Held('EXPECTED_CONFIG_INVALID', 'request pin classification differs from expected config pins')


def _parent_wait(st, req):
    data, _ = st.pinned('parent_wait', req['parent_wait'], JSON_CAP, 'PARENT_WAIT_INVALID')
    doc = _parse(data, 'PARENT_WAIT_INVALID', 'parent wait')
    if (not _keys(doc, WAIT_KEYS) or not _same_str(doc['format'], WAIT_FORMAT) or not _same_str(doc['role'], 'driver')
            or not _same_str(doc['observed_by'], 'parent') or not _same_str(doc['item'], req['item'])
            or not _int(doc['pid'], 1) or not _int(doc['pgid'], 1) or not _text(doc['start_fingerprint'])
            or type(doc['actual_exit']) is not int):
        raise _Held('PARENT_WAIT_INVALID', 'PRT wait doc exact schema for the supervisor (driver) process')
    decoded = _exit_from_status(doc['raw_status'])
    if decoded is None or decoded != doc['actual_exit']:
        raise _Held('PARENT_WAIT_INVALID', 'raw_status does not decode to actual_exit (macOS wait status)')
    return doc


def _eligible_exit(st, wait):
    code = wait['actual_exit']
    if code == 10:
        raise _Held('NESTED_EXIT_UNAVAILABLE', 'supervisor exit 10 NOT_LAUNCHED: no nested child exit exists')
    if code not in (0, 11):
        raise _Held('SUPERVISOR_EXIT_NOT_ELIGIBLE', 'parent-observed supervisor exit %d is not acknowledged 0/11' % code)


def _parent_capture(st, role, record):
    data, after = st.acquire(role, record['path'], LARGE_CAP, 'SUPERVISOR_CAPTURE_UNBOUND')
    if (len(data) != record['bytes'] or _sha(data) != record['sha256']
            or [after['dev'], after['ino']] != record['inode'] or after['nlink'] != 1):
        raise _Held('SUPERVISOR_CAPTURE_UNBOUND', role + ': independent reopen does not join V9 bytes/sha/original inode')
    return data


def _ack(st, req):
    captures = req['parent_captures']
    out = _parent_capture(st, 'supervisor_stdout_capture', captures['stdout'])
    err = _parent_capture(st, 'supervisor_stderr_capture', captures['stderr'])
    if err:
        raise _Held('SUPERVISOR_CAPTURE_UNBOUND', 'supervisor stderr is nonempty beside a claimed acknowledgement')
    if len(out) < 2 or not out.endswith(b'\n') or out.count(b'\n') != 1:
        raise _Held('SUPERVISOR_ACK_INVALID', 'supervisor stdout is not exactly one LF-terminated line')
    ack = _parse(out[:-1], 'SUPERVISOR_ACK_INVALID', 'supervisor ACK')
    if (not _keys(ack, ACK_KEYS) or not _same_str(ack['supervisor'], SUPERVISOR_VERSION) or ack['acknowledged'] is not True
            or type(ack['exit_code']) is not int or type(ack['settlement']) is not str
            or not all(_hex64(ack[key]) for key in ('config_sha256', 'receipt_sha256', 'settlement_record_sha256'))
            or not _int(ack['receipt_bytes'], 0) or not _int(ack['settlement_bytes'], 0)
            or not (ack['child_returncode'] is None or type(ack['child_returncode']) is int)
            or type(ack['failure_codes']) is not list or not all(type(c) is str for c in ack['failure_codes'])
            or type(ack['owned_live']) is not list or type(ack['unproved_live']) is not list
            or not _census(ack['ack_census'])):
        raise _Held('SUPERVISOR_ACK_INVALID', 'stdout line is not one exact successful supervisor19 ACK')
    return ack


def _receipt_shape(r):
    if type(r) is not dict or not all(type(k) is str for k in r):
        raise _Held('RECEIPT_INVALID', 'receipt must be a JSON object')
    missing = [key for key in RECEIPT_REQUIRED if key not in r]
    if missing:
        raise _Held('RECEIPT_INVALID', 'receipt lacks consumed fields: ' + ','.join(missing[:8]))
    if not _hex64(r['config_sha256']) or not _norm_abs(r['config_path']) or not _int(r['supervisor_pid'], 1):
        raise _Held('RECEIPT_INVALID', 'receipt config/supervisor pid fields')
    if type(r['settlement']) is not str or type(r['loop_status']) is not str:
        raise _Held('RECEIPT_INVALID', 'receipt settlement/loop_status')
    if not (r['child_pid'] is None or _int(r['child_pid'], 1)) or not (r['child_identity'] is None or _identity(r['child_identity'])):
        raise _Held('RECEIPT_INVALID', 'receipt child pid/identity')
    if type(r['wait_status_lost']) is not bool or type(r['timing_failed']) is not bool:
        raise _Held('RECEIPT_INVALID', 'receipt wait/timing flags')
    for key in ('raw_acquisitions', 'contract_violations', 'owned_identities', 'unproved_history', 'helpers',
                'failures', 'trips', 'coverage_history'):
        if type(r[key]) is not list:
            raise _Held('RECEIPT_INVALID', 'receipt list field ' + key)
    for key in ('streams', 'artifacts', 'output_root_inventory', 'cancel'):
        if type(r[key]) is not dict:
            raise _Held('RECEIPT_INVALID', 'receipt object field ' + key)
    for key in ('main_wait', 'clear', 'history_overflow', 'authorization', 'stop_request', 'signal'):
        if not (r[key] is None or type(r[key]) is dict):
            raise _Held('RECEIPT_INVALID', 'receipt nullable object field ' + key)
    codes = [f.get('code') if type(f) is dict else None for f in r['failures']]
    if not all(type(c) is str for c in codes) or len(set(codes)) != len(codes):
        raise _Held('RECEIPT_INVALID', 'receipt failure codes')
    if not all(type(t) is dict and type(t.get('trip')) is str for t in r['trips']):
        raise _Held('RECEIPT_INVALID', 'receipt trips')
    if r['stop_request'] is not None and type(r['stop_request'].get('reason')) is not str:
        raise _Held('RECEIPT_INVALID', 'receipt stop_request reason')
    if r['signal'] is not None and type(r['signal'].get('sent')) is not bool:
        raise _Held('RECEIPT_INVALID', 'receipt main signal sent flag')
    if not all(type(e) is dict and 'identity' in e for e in r['owned_identities']):
        raise _Held('RECEIPT_INVALID', 'receipt owned_identities')
    if not all(type(e) is dict and 'first_identity' in e and 'last_identity' in e for e in r['unproved_history']):
        raise _Held('RECEIPT_INVALID', 'receipt unproved_history')
    for h in r['helpers']:
        if (type(h) is not dict or not all(key in h for key in HELPER_KEYS) or not _int(h['pid'], 1)
                or type(h['settled']) is not bool or not (h['identity'] is None or type(h['identity']) is dict)
                or not (h['signal'] is None or (type(h['signal']) is dict and type(h['signal'].get('sent')) is bool))):
            raise _Held('RECEIPT_INVALID', 'receipt helper report (pid/identity/settled/signal keys mandatory)')
    for entry in r['coverage_history']:
        observation = entry.get('observation') if type(entry) is dict else None
        if type(observation) is not list or not observation or not _int(observation[0], 0):
            raise _Held('RECEIPT_INVALID', 'receipt coverage_history observation')
    if not _census(r['final_census']):
        raise _Held('RECEIPT_INVALID', 'receipt final_census')
    if not (r['cancel'].get('signal') is None or type(r['cancel'].get('signal')) is int):
        raise _Held('RECEIPT_INVALID', 'receipt cancel signal')


def _receipt(st, req):
    binding = req['publication']['receipt']
    data, after = st.acquire('receipt', binding['path'], LARGE_CAP, 'RECEIPT_UNBOUND')
    if (_sha(data) != binding['sha256'] or len(data) != binding['bytes']
            or [after['dev'], after['ino']] != binding['inode'] or after['nlink'] != 1):
        raise _Held('RECEIPT_UNBOUND', 'receipt bytes/inode/nlink differ from the parent publication binding')
    receipt = _parse(data, 'RECEIPT_INVALID', 'receipt')
    if type(receipt) is dict and not (_same_str(receipt.get('supervisor'), SUPERVISOR_VERSION)
                                      and _same_str(receipt.get('supervisor_sha256'), SUPERVISOR_SHA)):
        raise _Held('AUTHORITY_PIN_MISMATCH', 'receipt was not produced by pinned owned_supervisor_v19 cb828a78')
    _receipt_shape(receipt)
    return {'receipt': receipt, 'path': binding['path'], 'sha256': binding['sha256'], 'length': len(data)}


def _receipt_complete(st, r):
    if r['timing_failed'] or r['history_overflow'] is not None or r['raw_acquisitions']:
        raise _Held('RECEIPT_EVIDENCE_INCOMPLETE', 'timing_failed/history_overflow/pending raw acquisitions are HOLD')


def _tamper(st, r):
    reported = sorted({f['code'] for f in r['failures']} & TAMPER_CODES)
    if reported:
        raise _Held('EVIDENCE_TAMPER_REPORTED', 'supervisor reported ' + ','.join(reported))


def _receipt_identities(st, r, ack):
    found = {}

    def add(p, label):
        if not _identity(p):
            raise _Held('RECEIPT_INVALID', label + ': malformed identity')
        old = found.get(p['uniqueid'])
        if old is not None and old != p['pid']:
            raise _Held('RECEIPT_INVALID', label + ': one uniqueid reported with two pids')
        found[p['uniqueid']] = p['pid']
    if r['child_identity'] is not None:
        add(r['child_identity'], 'child_identity')
    for entry in r['owned_identities']:
        add(entry['identity'], 'owned_identities')
    for entry in r['unproved_history']:
        add(entry['first_identity'], 'unproved_history')
        add(entry['last_identity'], 'unproved_history')
        if entry['first_identity']['uniqueid'] != entry['last_identity']['uniqueid']:
            raise _Held('RECEIPT_INVALID', 'unproved_history entry spans two uniqueids')
    for h in r['helpers']:
        if h['identity'] is not None:
            add(h['identity'], 'helpers')
    for p in r['final_census']['owned_live'] + r['final_census']['unproved_live']:
        add(p, 'final_census')
    if ack is not None:
        census = ack['ack_census']
        for p in census['owned_live'] + census['unproved_live'] + ack['owned_live'] + ack['unproved_live']:
            add(p, 'ack_census')
    return found


def _ack_histories(st, ack, r, identities):
    """Interface-v2 C1-C3/C5: ACK histories extend the receipt's; post-receipt census retries stay sticky."""
    coverage, unproved, violations = ack['coverage_history'], ack['unproved_history'], ack['contract_violations']
    if type(coverage) is not list or type(unproved) is not list or type(violations) is not list:
        raise _Held('SUPERVISOR_ACK_INVALID', 'ACK coverage/unproved/violation histories must be lists')
    for entry in coverage:
        observation = entry.get('observation') if type(entry) is dict else None
        if type(observation) is not list or not observation or not _int(observation[0], 0):
            raise _Held('SUPERVISOR_ACK_INVALID', 'ACK coverage_history observation')
    found = dict(identities)

    def add(p, label):
        if not _identity(p):
            raise _Held('SUPERVISOR_ACK_INVALID', label + ': malformed identity')
        old = found.get(p['uniqueid'])
        if old is not None and old != p['pid']:
            raise _Held('SUPERVISOR_ACK_INVALID', label + ': one uniqueid reported with two pids')
        found[p['uniqueid']] = p['pid']
    ack_uids = set()
    for entry in unproved:
        if type(entry) is not dict or 'first_identity' not in entry or 'last_identity' not in entry:
            raise _Held('SUPERVISOR_ACK_INVALID', 'ACK unproved_history entry')
        add(entry['first_identity'], 'ACK unproved_history')
        add(entry['last_identity'], 'ACK unproved_history')
        if entry['first_identity']['uniqueid'] != entry['last_identity']['uniqueid']:
            raise _Held('SUPERVISOR_ACK_INVALID', 'ACK unproved_history entry spans two uniqueids')
        ack_uids.add(entry['first_identity']['uniqueid'])
    for violation in violations:
        add(violation, 'ACK contract_violations')
    for name, mine, theirs in (('coverage_history', r['coverage_history'], coverage),
                               ('contract_violations', r['contract_violations'], violations)):
        if len(theirs) < len(mine) or not _exact(theirs[:len(mine)], mine):
            raise _Held('SUPERVISOR_ACK_INVALID', 'receipt ' + name + ' is not an exact prefix of the ACK history')
    receipt_uids = {entry['first_identity']['uniqueid'] for entry in r['unproved_history']}
    if not receipt_uids <= ack_uids:
        raise _Held('SUPERVISOR_ACK_INVALID', 'receipt unproved_history uniqueids are not a subset of the ACK history')
    return {'identities': found, 'coverage': coverage, 'unproved_uids': sorted(receipt_uids | ack_uids),
            'violations': violations}


def _wait_joins(st, wait, r):
    if wait['pid'] != r['supervisor_pid']:
        raise _Held('PARENT_WAIT_INVALID', 'parent-waited supervisor pid differs from the receipt supervisor_pid')


def _ack_joins(st, ack, wait, rinfo):
    r = rinfo['receipt']
    if ack['exit_code'] != wait['actual_exit']:
        raise _Held('SUPERVISOR_ACK_INVALID', 'printed ACK exit_code differs from the parent-observed actual exit')
    if ack['settlement'] != r['settlement'] or STATE_EXIT.get(r['settlement']) != wait['actual_exit']:
        raise _Held('SUPERVISOR_ACK_INVALID', 'ACK/receipt settlement inconsistent with the actual exit')
    if ack['receipt_sha256'] != rinfo['sha256'] or ack['receipt_bytes'] != rinfo['length']:
        raise _Held('SUPERVISOR_ACK_INVALID', 'ACK receipt digest/length differ from the bound receipt')
    if ack['config_sha256'] != r['config_sha256'] or not _exact(ack['child_returncode'], r['child_returncode']):
        raise _Held('SUPERVISOR_ACK_INVALID', 'ACK config/child_returncode differ from the receipt')
    if not _exact(ack['failure_codes'], sorted(f['code'] for f in r['failures'])):
        raise _Held('SUPERVISOR_ACK_INVALID', 'ACK failure codes differ from the receipt')


def _nested_exit(st, r):
    if r['settlement'] not in STATE_EXIT:
        raise _Held('NESTED_EXIT_UNAVAILABLE', 'receipt settlement is not SETTLED/UNSETTLED with a launched child')
    child_pid, wait, identity = r['child_pid'], r['main_wait'], r['child_identity']
    if child_pid is None or wait is None or identity is None or identity['pid'] != child_pid:
        raise _Held('NESTED_EXIT_UNAVAILABLE', 'no launched main child with a retained identity and native wait')
    if not _keys(wait, MAIN_WAIT_KEYS) or wait['leader_reaped'] is not True or r['wait_status_lost'] is not False:
        raise _Held('NESTED_EXIT_UNAVAILABLE', 'main child leader not reaped or wait status lost')
    status, rc = wait['raw_wait_status'], wait['rc']
    if wait['pid'] != child_pid or not _exact(wait['native_wait_result'], [child_pid, status]):
        raise _Held('NESTED_EXIT_UNAVAILABLE', 'native wait tuple does not join the main child pid/status')
    decoded = _exit_from_status(status)
    if decoded is None or type(rc) is not int or decoded != rc or not _exact(r['child_returncode'], rc):
        raise _Held('NESTED_EXIT_UNAVAILABLE', 'raw wait status, rc and child_returncode disagree')
    return rc


def _actual_config(st, rinfo):
    r = rinfo['receipt']
    ref = {'path': r['config_path'], 'sha256': r['config_sha256']}
    data, _ = st.pinned('actual_config', ref, JSON_CAP, 'ACTUAL_CONFIG_INVALID')
    cfg = _config_shape(_parse(data, 'ACTUAL_CONFIG_INVALID', 'actual config'), 'ACTUAL_CONFIG_INVALID')
    if cfg['receipt'] != rinfo['path']:
        raise _Held('ACTUAL_CONFIG_INVALID', 'actual config receipt path differs from the bound receipt path')
    return cfg


def _actual_go(st, cfg, r):
    auth = r['authorization']
    if not _keys(auth, AUTHORIZATION_KEYS) or not _hex64(auth['go_sha256']):
        raise _Held('ACTUAL_GO_INVALID', 'receipt authorization unavailable')
    ref = {'path': cfg['admission']['go_path'], 'sha256': auth['go_sha256']}
    data, _ = st.pinned('actual_go', ref, JSON_CAP, 'ACTUAL_GO_INVALID')
    go = _parse(data, 'ACTUAL_GO_INVALID', 'actual GO')
    if (type(go) is not dict or not _same_str(go.get('decision'), 'GO') or not _same_str(go.get('item'), cfg['item'])
            or type(go.get('configs')) is not dict or r['config_sha256'] not in go['configs']):
        raise _Held('ACTUAL_GO_INVALID', 'actual GO decision/item/config binding')
    if type(go.get('mode')) is not str or go['mode'] not in MODES or not _hex64(go.get('plan_sha256')):
        raise _Held('ACTUAL_GO_INVALID', 'actual GO lacks explicit beta mode/plan_sha256 binding')
    return go


def _launch(st, cfg, r):
    digest = r.get('launch_record_sha256')
    if not _hex64(digest):
        raise _Held('LAUNCH_RECORD_INVALID', 'receipt has no published launch record digest')
    data, _ = st.pinned('launch_record', {'path': cfg['launch_record'], 'sha256': digest}, JSON_CAP,
                        'LAUNCH_RECORD_INVALID')
    launch = _parse(data, 'LAUNCH_RECORD_INVALID', 'launch record')
    if not _keys(launch, LAUNCH_KEYS):
        raise _Held('LAUNCH_RECORD_INVALID', 'launch record exact keys')
    if (not _same_str(launch['supervisor'], SUPERVISOR_VERSION) or not _same_str(launch['supervisor_sha256'], SUPERVISOR_SHA)
            or not _same_str(launch['config_sha256'], r['config_sha256']) or not _exact(launch['supervisor_pid'], r['supervisor_pid'])
            or not _exact(launch['identity'], r['child_identity']) or not _exact(launch['argv'], cfg['argv'])
            or not _same_str(launch['cwd'], cfg['lane']) or not _exact(launch['authorization'], r['authorization'])
            or not _exact(launch['start_date'], r.get('start_date'))):
        raise _Held('LAUNCH_RECORD_INVALID', 'launch record does not join receipt/config facts')
    return launch


def _main_capture(st, name, cfg, r):
    streams = r['streams']
    if set(streams) != set(STREAM_NAMES):
        raise _Held('MAIN_STREAM_UNBOUND', 'receipt lacks exactly the two MAIN stream records')
    rec = streams[name]
    if (not _keys(rec, STREAM_KEYS) or not all(_int(rec[k], 0) for k in STREAM_COUNTERS)
            or not all(type(rec[k]) is bool for k in STREAM_FLAGS) or not all(_finite_or_none(rec[k]) for k in STREAM_MONOS)
            or not (rec['error'] is None or type(rec['error']) is str) or not _hex64(rec['sha256_prefix'])
            or not (rec['sha256_written'] is None or _hex64(rec['sha256_written']))):
        raise _Held('MAIN_STREAM_UNBOUND', name + ': MAIN stream record is not the exact typed 22-field record')
    if rec['write_inflight'] or rec['hash_pending'] or rec['pending_bytes'] != 0 or rec['sha256_written'] is None:
        raise _Held('MAIN_STREAM_UNBOUND', name + ': ambiguous in-flight or unfinalized MAIN stream snapshot')
    cap = cfg[name + '_cap_bytes']
    closed = rec['error'] is None and rec['eof_seen'] and rec['out_closed'] and rec['pipe_closed']
    if (rec['sha256_written'] != rec['sha256_prefix'] or rec['prefix_bytes'] != rec['bytes_written']
            or rec['cap_bytes'] != cap or rec['bytes_written'] > min(rec['bytes_seen'], cap)
            or rec['overflow'] != (rec['bytes_seen'] > cap) or rec['closed'] != bool(closed)):
        raise _Held('MAIN_STREAM_UNBOUND', name + ': MAIN stream counters/hash/closure are internally inconsistent')
    path = cfg[name]
    art = r['artifacts'].get(path)
    if (not _keys(art, ARTIFACT_KEYS) or art['sha256'] != rec['sha256_written'] or art['bytes'] != rec['bytes_written']
            or type(art['nlink']) is not int or art['nlink'] != 1 or not _inode(art['inode'])):
        raise _Held('MAIN_STREAM_UNBOUND', name + ': receipt final read does not bind the capture file')
    data, after = st.acquire('main_' + name + '_capture', path, LARGE_CAP, 'MAIN_STREAM_UNBOUND')
    if (_sha(data) != rec['sha256_written'] or len(data) != rec['bytes_written']
            or [after['dev'], after['ino']] != art['inode'] or after['nlink'] != 1):
        raise _Held('MAIN_STREAM_UNBOUND', name + ': actual capture file differs from the original created capture')
    return {'present': True, 'path': path, 'sha256': rec['sha256_written'], 'bytes_seen': rec['bytes_seen'],
            'bytes_stored': rec['bytes_written'], 'eof': rec['eof_seen'], 'overflow': rec['overflow'],
            'error': rec['error']}


def _artifacts(st, cfg, r):
    names, directories = {}, set()
    for output in cfg['outputs']:
        directory, name = output['path'].rsplit('/', 1)
        if not _norm_abs(directory) or not _plain(name) or name in names:
            raise _Held('ARTIFACT_UNBOUND', 'actual outputs need distinct plain basenames in one job directory')
        directories.add(directory)
        names[name] = output['path']
    if len(directories) != 1:
        raise _Held('ARTIFACT_UNBOUND', 'actual outputs are not in exactly one job directory')
    job_dir = directories.pop()
    inventory = r['output_root_inventory'].get(job_dir)
    if type(inventory) is not list or not all(type(n) is str for n in inventory) or len(set(inventory)) != len(inventory):
        raise _Held('ARTIFACT_UNBOUND', 'receipt has no exact final inventory of the actual job directory')
    artifacts = {}
    for name, path in names.items():
        if path not in r['artifacts']:
            raise _Held('ARTIFACT_UNBOUND', 'receipt lacks the final read of a declared output')
        art = r['artifacts'][path]
        if art is None:
            continue  # Truthful absence at the supervisor's final read; capture4/adapter3 then judge X4.
        if (not _keys(art, ARTIFACT_KEYS) or not _hex64(art['sha256']) or not _int(art['bytes'], 0)
                or not _inode(art['inode']) or not _int(art['nlink'], 0)):
            raise _Held('ARTIFACT_UNBOUND', 'declared output final read is unreadable or incomplete')
        artifacts[name] = {'path': path, 'sha256': art['sha256'], 'bytes': art['bytes'], 'ino': art['inode'][1],
                           'nlink': art['nlink']}
    return {'job_dir': job_dir, 'artifacts': artifacts, 'names': sorted(inventory)}


def _dates(st, r, rinfo):
    records = {}
    for purpose, key in (('start', 'start_date'), ('end', 'end_date')):
        text = r.get(key)
        if not _date_text(text):
            raise _Held('DATE_UNAVAILABLE', 'receipt ' + key + ' is not an owned /bin/date reading')
        records[purpose] = {'kind': DATE_KIND, 'purpose': purpose, 'text': text, 'receipt_sha256': rinfo['sha256']}
    return records


def _actual_pins(st, req, cfg):
    source_keys = set(req['expected']['source_pins'])
    input_keys = set(req['expected']['input_pins'])
    seen, source, inputs = {}, {}, {}
    for pin in cfg['pins']:
        path, digest = pin['path'], pin['sha256']
        if path in seen and seen[path] != digest:
            raise _Held('PIN_CLASSIFICATION_INVALID', 'actual config pins conflict on one path')
        seen[path] = digest
        if path not in source_keys and path not in input_keys:
            raise _Held('PIN_CLASSIFICATION_INVALID', 'actual pin path is not classified by the parent request')
        if path in source_keys:
            source[path] = digest
        if path in input_keys:
            inputs[path] = digest
    return source, inputs


def _union(st, req, r, rinfo, wait, hist):
    data, _ = st.pinned('identity_union', req['identity_union'], LARGE_CAP, 'IDENTITY_UNION_INVALID')
    doc = _parse(data, 'IDENTITY_UNION_INVALID', 'identity union')
    if (not _keys(doc, UNION_KEYS) or not _same_str(doc['format'], UNION_FORMAT) or not _same_str(doc['item'], req['item'])
            or not _same_str(doc['receipt_sha256'], rinfo['sha256']) or not _same_str(doc['completeness'], UNION_COMPLETENESS)
            or type(doc['identities']) is not list or not doc['identities']):
        raise _Held('IDENTITY_UNION_INVALID', 'union exact keys/format/item/receipt/completeness attestation')
    by_uid, by_pid, keys = {}, {}, set()
    for row in doc['identities']:
        if (not _keys(row, UNION_ROW_KEYS) or type(row['role']) is not str or row['role'] not in UNION_ROLES
                or not _int(row['pid'], 1) or not _int(row['pgid'], 1) or not _text(row['start_fingerprint'])
                or not _text(row['source']) or type(row['status']) is not str or row['status'] not in UNION_STATUSES
                or not (row['uniqueid'] is None or _int(row['uniqueid'], 1))):
            raise _Held('IDENTITY_UNION_INVALID', 'union row exact schema')
        key = (row['pid'], row['start_fingerprint'])
        if key in keys or (row['uniqueid'] is not None and row['uniqueid'] in by_uid):
            raise _Held('IDENTITY_UNION_INVALID', 'union rows must be unique by (pid,start_fingerprint) and uniqueid')
        keys.add(key)
        if row['uniqueid'] is not None:
            by_uid[row['uniqueid']] = row
        by_pid.setdefault(row['pid'], []).append(row)
    drivers = [row for row in doc['identities'] if row['role'] == 'driver']
    if (len(drivers) != 1 or drivers[0]['pid'] != wait['pid'] or drivers[0]['pgid'] != wait['pgid']
            or drivers[0]['start_fingerprint'] != wait['start_fingerprint']):
        raise _Held('IDENTITY_UNION_INVALID', 'union needs exactly one driver row equal to the parent-waited supervisor')
    for uid, pid in hist['identities'].items():
        row = by_uid.get(uid)
        if row is None or row['pid'] != pid:
            raise _Held('IDENTITY_UNION_INVALID', 'union omits or contradicts supervisor identity uniqueid %d' % uid)
    child = by_uid.get(r['child_identity']['uniqueid']) if r['child_identity'] is not None else None
    if child is None or child['role'] != 'main_child':
        raise _Held('IDENTITY_UNION_INVALID', 'union main child row missing or not role main_child')
    for h in r['helpers']:
        if h['identity'] is None and not any(row['role'] == 'helper' for row in by_pid.get(h['pid'], [])):
            raise _Held('IDENTITY_UNION_INVALID', 'union omits identity-less helper pid %d' % h['pid'])
    for entry in hist['coverage']:
        if entry['observation'][0] not in by_pid:
            raise _Held('IDENTITY_UNION_INVALID', 'union omits supervisor coverage-gap pid %d' % entry['observation'][0])
    return doc['identities']


def _settlement(st, r, ack, rows, hist):
    final, at_ack = r['final_census'], ack['ack_census']
    unresolved, signals = set(), set()
    for label, census in (('FINAL', final), ('ACK', at_ack)):
        for p in census['owned_live']:
            unresolved.add('%s_OWNED_LIVE:%d' % (label, p['uniqueid']))
        for p in census['unproved_live']:
            unresolved.add('%s_UNPROVED_LIVE:%d' % (label, p['uniqueid']))
    for uid in hist['unproved_uids']:
        unresolved.add('UNPROVED_HISTORY:%d' % uid)  # Sticky: no union status (ENDED_PROVED or other) waives it.
    for index, entry in enumerate(hist['coverage']):
        unresolved.add('COVERAGE_GAP:%d:%d' % (index, entry['observation'][0]))  # Sticky; never a PID-only clearance.
    for h in r['helpers']:
        if h['settled'] is not True:
            unresolved.add('HELPER_UNSETTLED:%d' % h['pid'])
        if h['signal'] is not None and h['signal']['sent'] is True:
            signals.add('HELPER_SIGTERM_SENT:%d' % h['pid'])
    for failure in r['failures']:
        unresolved.add('SUPERVISOR_FAILURE:' + failure['code'])
    for trip in r['trips']:
        unresolved.add('SUPERVISOR_TRIP:' + trip['trip'])
    if r['settlement'] != 'SETTLED':
        unresolved.add('SUPERVISOR_STATE:' + r['settlement'])
    for violation in hist['violations']:
        unresolved.add('CONTRACT_VIOLATION:%d' % violation['uniqueid'])
    if r['loop_status'] != 'EXITED':
        unresolved.add('LOOP_STATUS:' + r['loop_status'])
    if r['clear'] is None:
        unresolved.add('CLEARANCE_NOT_ESTABLISHED')
    for row in rows:
        if row['status'] != 'ENDED_PROVED':
            uid = 'null' if row['uniqueid'] is None else str(row['uniqueid'])
            unresolved.add('UNION_UNRESOLVED:%s:%d:%s' % (row['role'], row['pid'], uid))
    if r['stop_request'] is not None:
        signals.add('STOP_REQUESTED:' + r['stop_request']['reason'])
    if r['signal'] is not None and r['signal']['sent'] is True:
        signals.add('MAIN_SIGTERM_SENT')
    if r['cancel'].get('signal') is not None:
        signals.add('SUPERVISOR_CANCEL_SIGNAL:%d' % r['cancel']['signal'])
    return {'reaped': True, 'group_empty': final['group_live'] == [] and at_ack['group_live'] == [],
            'census_complete': final['complete'] is True and at_ack['complete'] is True,
            'unresolved': sorted(unresolved), 'signals': sorted(signals)}


def _context(st, req, plan):
    dm21 = {'path': plan['plan']['dm21_path'], 'sha256': plan['plan']['dm21_sha256']}
    context = req['context']
    if not _exact(context['original_dm21'], dm21):
        raise _Held('CONTEXT_INVALID', 'original_dm21 must equal plan dm21_path/dm21_sha256')
    st.pinned('original_dm21', dm21, JSON_CAP, 'CONTEXT_INVALID')
    prefix, order, jobs = context['prefix'], plan['order'], plan['jobs']
    if len(prefix) != plan['position']:
        raise _Held('CONTEXT_INVALID', 'prefix must hold exactly the preceding plan items (no dependency bypass)')
    authority = []
    for index, row in enumerate(prefix):
        if not _keys(row, PREFIX_ROW_KEYS) or not _same_str(row['item'], order[index]) or not _ref(row['audit']):
            raise _Held('CONTEXT_INVALID', 'prefix row %d exact {item,files,audit} in plan order' % index)
        outputs = jobs[order[index]]['outputs']
        files = row['files']
        if not _keys(files, outputs) or not all(_ref(files[name]) for name in outputs):
            raise _Held('CONTEXT_INVALID', 'prefix row %d files must map exactly the plan outputs' % index)
        for name in outputs:
            st.pinned('prefix_file:%s/%s' % (order[index], name), files[name], LARGE_CAP, 'CONTEXT_INVALID')
        st.pinned('prefix_audit:' + order[index], row['audit'], JSON_CAP, 'CONTEXT_INVALID')
        authority.append({'item': order[index], 'audit_sha256': row['audit']['sha256']})
    return authority


def _freeze(st, req, authority):
    data, _ = st.pinned('publication_freeze', req['publication_freeze'], JSON_CAP, 'FREEZE_INVALID')
    doc = _parse(data, 'FREEZE_INVALID', 'publication freeze')
    if (not _keys(doc, FREEZE_KEYS) or not _same_str(doc['format'], FREEZE_FORMAT) or not _same_str(doc['mode'], req['mode'])
            or not _same_str(doc['job_dir'], req['job_dir']) or not _exact(doc['prefix_authority'], authority)):
        raise _Held('FREEZE_INVALID', 'freeze exact keys/format/mode/job_dir/prefix_authority')
    paths = doc['immutable_paths']
    if type(paths) is not list or not all(_norm_abs(p) for p in paths) or len(set(paths)) != len(paths):
        raise _Held('FREEZE_INVALID', 'freeze immutable_paths must be unique normalized absolute paths')
    return set(paths)


def _coverage(st, req, plan, expected_cfg, cfg, rinfo, frozen):
    publish = {req['publish_paths'][name] for name in PUBLISH_NAMES}
    evidence = set(st.cache)
    evidence |= {CAPTURE4_PATH, SCHEMA2_PATH, GATE_PATH, PLAN_PATH, plan['plan']['dm21_path'], rinfo['path']}
    evidence |= {req['job_dir'] + '/' + name for name in plan['job']['outputs']}
    evidence |= {expected_cfg['stdout'], expected_cfg['stderr'], expected_cfg['receipt'], cfg['stdout'], cfg['stderr']}
    evidence |= set(req['expected']['source_pins']) | set(req['expected']['input_pins'])
    evidence |= {pin['path'] for pin in cfg['pins']}
    collisions = sorted(publish & evidence)
    if collisions:
        raise _Held('REQUEST_INVALID', 'publish path collides with consumed or predicted evidence: ' + collisions[0])
    missing = sorted((evidence | publish) - frozen)
    if missing:
        raise _Held('FREEZE_COVERAGE_INCOMPLETE', 'freeze omits %d paths, first %s' % (len(missing), missing[0]))


def _records(a):
    req, plan, expected_cfg, cfg = a['req'], a['plan'], a['expected_cfg'], a['cfg']
    rinfo, receipt, expected = a['rinfo'], a['rinfo']['receipt'], a['req']['expected']
    expectation = {
        'format': EXPECTATION_FORMAT, 'mode': req['mode'], 'item': req['item'], 'plan_sha256': PLAN_SHA,
        'expected_exit': plan['job']['exit'], 'outputs': list(plan['job']['outputs']), 'job_dir': req['job_dir'],
        'capture_paths': {'stdout': expected_cfg['stdout'], 'stderr': expected_cfg['stderr']},
        'receipt_path': expected_cfg['receipt'], 'receipt_sha256': req['publication']['receipt']['sha256'],
        'resolved_argv': list(expected_cfg['argv']), 'go_sha256': expected['go']['sha256'],
        'source_pins': dict(expected['source_pins']), 'input_pins': dict(expected['input_pins']),
        'date_start': copy.deepcopy(expected['date_start']), 'date_end': copy.deepcopy(expected['date_end'])}
    observation = {
        'format': OBSERVATION_FORMAT, 'item': cfg['item'], 'plan_sha256': a['go']['plan_sha256'],
        'mode': a['go']['mode'], 'actual_exit': a['nested'],
        'captures': {name: copy.deepcopy(a['captures'][name]) for name in STREAM_NAMES},
        'artifacts': copy.deepcopy(a['arts']['artifacts']), 'actual_artifact_names': list(a['arts']['names']),
        'receipt': {'path': rinfo['path'], 'sha256': rinfo['sha256']}, 'settlement': copy.deepcopy(a['settlement']),
        'resolved_argv': list(a['launch']['argv']), 'go_sha256': receipt['authorization']['go_sha256'],
        'source_pins': dict(a['pins'][0]), 'input_pins': dict(a['pins'][1]),
        'date_start': copy.deepcopy(a['dates']['start']), 'date_end': copy.deepcopy(a['dates']['end'])}
    context = {
        'format': CONTEXT_FORMAT, 'plan': {'path': PLAN_PATH, 'sha256': PLAN_SHA},
        'original_dm21': copy.deepcopy(req['context']['original_dm21']), 'prefix': copy.deepcopy(req['context']['prefix']),
        'derivation': None, 'publication_freeze': copy.deepcopy(req['publication_freeze'])}
    records = {}
    for name, value in (('expectation', expectation), ('observation', observation), ('context', context)):
        text = _canonical(value)
        data = text.encode('ascii')
        records[name] = {'path': req['publish_paths'][name], 'sha256': _sha(data), 'length': len(data), 'text': text}
    return records
