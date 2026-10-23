"""beta_schema_audit_v1: X5 RESULT_SCHEMA predicate for MOLS39/CFR21 ext-search-plan-v5 (beta parent consumer slice).

STATUS: SOURCE ONLY. Authored without execution, import, compile, syntax check or test. It stays untrusted until
parent source review and a separately admitted finite behavioral qualification; source readiness grants no launch,
canonical audit, release or admission.

Authority (SHA-256 verified by metadata reads while authoring, 2026-10-19; RUN = /Users/jinleic/repos/aifours/
institute/runs/six-lane-2026-10-18-96h, MOLS = /Users/jinleic/repos/aifours/information-science/evidence/
six-lane-20261018-96h/mols39):
  consumer contract  RUN/control/beta-audit-consumer-contract-v1.json       b26a98caba1fbf17de0376fde24905052b68ebc0d5f567cdebfac092a6cdfd96
  plan               MOLS/evidence/ext-search-plan-v5.json                    254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731
  schema contract    MOLS/evidence/ext-search-successor4-contract-v3.md       ad5bb631adbe55511851fa54b0fb684807051436e35a5f4030a59ec674fc5f72
  gate validator     MOLS/code/ext4_gate.py                                   8d04c5ce7b9fdf3f42c5537bdf32c892b6c1af09e3e31096e41b2506597624fa

Interface (frozen by the consumer contract):
  audit_schema(plan_bytes, item, files, prefix, original_dm21, deadline_check) -> [] or ['X5 RESULT_SCHEMA']

Pure predicate: no file writes, no process calls, no verdicts, no module-level state. Importing this module performs
no imports and no reads. Each explicit call reads exactly one file, the approved gate source, through a
descriptor-anchored bounded reader, checks its SHA-256 against the pin, compiles and executes those verified
definitions in a fresh namespace whose __name__ is not '__main__', and reuses the gate's strict JSON parse,
canonical, exact, digest, hex64, finite_wall, rawrows, validate_result and verify_controls. The gate's main is never
referenced or called; only the per-item structure of its audited-prefix loop is transcribed here so that it runs on
caller-supplied bytes instead of directory reads.

Sole namespace substitution: anchored_read_bytes is replaced by an explicitly labelled OFFLINE SNAPSHOT reader that
serves only plan.dm21_path from the supplied original_dm21 bytes after checking their digest against
plan.dm21_sha256, and rejects every other path. This is offline snapshot evaluation, not a real-path reader smoke and
never kernel or filesystem evidence.

Schema is not authority. [] says only that the supplied bytes satisfy the pinned schemas plus the dependency, peer and
gate recomputations. The parent separately binds actual receipts, exits, captures, settlement, /bin/date records and
provenance; canonical prior-audit syntax proves none of them. A qualified final G-CONTROLS means controls only;
target_claim is always UNEVALUATED; nothing here is six-MOLS39/CFR21 scientific acceptance.
"""

__all__ = ('audit_schema',)

SCHEMA_CAUSE = 'X5 RESULT_SCHEMA'
PLAN_SHA256 = '254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731'
GATE_PATH = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/code/ext4_gate.py'
GATE_SHA256 = '8d04c5ce7b9fdf3f42c5537bdf32c892b6c1af09e3e31096e41b2506597624fa'
GATE_SOURCE_CAP = 1 << 20  # successor4 contract v3: algorithm-source cap 1 MiB
PLAN_CAP = 16 << 20  # gate CAP for its own plan read; pre-hash bound only (the pin fixes the actual length)
AUDIT_CAP = 1 << 20  # gate: readat(audit, item + '.audit.json', 1<<20)
DM21_CAP = 1 << 20  # gate verify_controls: anchored_read_bytes(plan['dm21_path'], 1<<20)
PLAN_JOB_COUNT = 20
LOADED_GATE_NAME = 'ext4_gate_pinned_for_beta_schema_audit_v1'  # deliberately not '__main__'
GATE_CALLABLES = ('Failure', 'parse', 'canonical', 'exact', 'digest', 'hex64', 'finite_wall', 'rawrows',
                  'validate_result', 'verify_controls', 'anchored_read_bytes')
GATE_CONSTANTS = ('KEYS', 'MFILES', 'GKEYS', 'AKEYS', 'CAP')
PREFIX_RECORD_KEYS = frozenset(('item', 'files', 'audit_bytes'))
DATA_RESULT_KEYS = ('status', 'reason', 'files', 'manifest_sha256', 'wall_s')
DATA_MANIFEST_KEYS = ('format', 'dm21_input_sha256', 'files', 'controls')
CONTROL_NAMES = ('N6', 'N12', 'P21', 'P57', 'BAD_DM', 'BAD_PIN')
PLANNED_STATUS = (('COMPLETE_ZERO', 'COMPLETE'), ('COMPLETE_CONTAINS', 'COMPLETE'), ('NOT_DM', 'NOT_DM'),
                  ('INPUT_PIN_MISMATCH', 'INPUT_PIN_MISMATCH'))


class _Reject(Exception):
    """Internal fail-closed signal; audit_schema maps it, like every other Exception, to X5."""


def audit_schema(plan_bytes, item, files, prefix, original_dm21, deadline_check):
    """Return [] only when the current item's declared outputs and its complete audited prefix satisfy the pinned
    plan-v5 / successor4-contract-v3 schemas; otherwise return ['X5 RESULT_SCHEMA'].

    plan_bytes      exact bytes of ext-search-plan-v5.json (SHA-256 254b44c3...).
    item            one of the twenty plan items; calibration items (CAL-beta, CAL-joint) and unknown names fail.
    files           plain dict mapping exactly the item's declared output basenames to immutable bytes objects.
    prefix          plain list holding one record per preceding plan item, in plan order; each record is a plain
                    dict with exactly {item, files, audit_bytes}: files as above for that item, audit_bytes the
                    canonical ext-search-job-audit-v1 record bytes. DATA requires prefix == [].
    original_dm21   bytes of plan.dm21_path whose SHA-256 equals plan.dm21_sha256 (offline snapshot binding).
    deadline_check  zero-argument callable: returns None while budget remains and raises on expiry. Any Exception it
                    raises, or any non-None return value, is a deadline failure and yields X5.

    Every defined input, read, loader, schema or deadline failure (any Exception) yields X5; only a completed
    validation path yields []. Non-Exception BaseExceptions (KeyboardInterrupt, SystemExit) propagate unchanged and
    never yield [].
    """
    try:
        if not callable(deadline_check):
            raise _Reject('deadline_check must be callable')
        tick = _deadline_tick(deadline_check)
        tick()
        verdict = _audit(plan_bytes, item, files, prefix, original_dm21, tick)
        tick()  # late completion is never timely evidence
    except Exception:
        return [SCHEMA_CAUSE]
    if verdict is not True:
        return [SCHEMA_CAUSE]
    return []


def _deadline_tick(deadline_check):
    """Wrap the parent deadline callable in the gate's tick convention: return None or raise."""
    def tick():
        if deadline_check() is not None:
            raise _Reject('deadline_check returned a value; None-or-raise is required')
    return tick


def _audit(plan_bytes, item, files, prefix, original_dm21, tick):
    import hashlib
    if type(plan_bytes) is not bytes or len(plan_bytes) > PLAN_CAP:
        raise _Reject('plan bytes type/cap')
    if hashlib.sha256(plan_bytes).hexdigest() != PLAN_SHA256:
        raise _Reject('plan bytes differ from pinned ext-search-plan-v5')
    if type(item) is not str or type(files) is not dict or type(prefix) is not list:
        raise _Reject('item/files/prefix types')
    if type(original_dm21) is not bytes or len(original_dm21) > DM21_CAP:
        raise _Reject('original DM21 snapshot type/cap')
    files = dict(files)
    prefix = list(prefix)
    tick()
    gate = _load_pinned_gate(tick)
    plan, jobs, order, calibrations = _plan_tables(gate, plan_bytes, tick)
    # Sole substitution in the verified namespace: verify_controls' original-DM21 read becomes the offline snapshot.
    gate['anchored_read_bytes'] = _offline_snapshot_dm21_reader(plan, original_dm21, tick)
    return _replay(gate, plan, jobs, order, calibrations, item, files, prefix, tick)


def _load_pinned_gate(tick):
    """Explicit-call verified-source loader: anchored bounded read, SHA-256 pin, compile, exec as a non-main module."""
    import hashlib
    source = _anchored_source_bytes(GATE_PATH, GATE_SOURCE_CAP, tick)
    if hashlib.sha256(source).hexdigest() != GATE_SHA256:
        raise _Reject('gate source differs from the approved pin')
    tick()
    code = compile(source, GATE_PATH, 'exec', dont_inherit=True)
    namespace = {'__name__': LOADED_GATE_NAME, '__file__': GATE_PATH}
    exec(code, namespace)  # verified definitions only; __name__ != '__main__', so the gate's main guard stays inert
    tick()
    for name in GATE_CALLABLES:
        if not callable(namespace.get(name)):
            raise _Reject('pinned gate definition missing: ' + name)
    for name in GATE_CONSTANTS:
        if name not in namespace:
            raise _Reject('pinned gate constant missing: ' + name)
    return namespace


def _anchored_source_bytes(path, cap, tick):
    """Bounded read of the approved gate source; the only file this module ever opens.

    The absolute normalized path is walked from a retained '/' descriptor with O_DIRECTORY|O_NOFOLLOW on every parent;
    the leaf is opened O_RDONLY|O_NONBLOCK|O_NOFOLLOW relative to the retained parent; fstat must show a regular
    one-link file within cap BEFORE any read; the same descriptor is read in <=64 KiB blocks consuming at most cap+1
    bytes; afterwards device/inode, size, link count, mtime and ctime must be unchanged and the size must equal the
    bytes read; the descriptor is closed and the deadline is checked again after close.
    """
    import os
    import stat
    if type(path) is not str or type(cap) is not int or cap < 0 or not path.startswith('/') or '\x00' in path:
        raise _Reject('absolute source path and integer cap required')
    parts = path.split('/')[1:]
    if not parts or any(part in ('', '.', '..') for part in parts):
        raise _Reject('normalized source path required')
    tick()
    parent = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in parts[:-1]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
            previous, parent = parent, child
            os.close(previous)
        fd = os.open(parts[-1], os.O_RDONLY | os.O_NONBLOCK | os.O_NOFOLLOW, dir_fd=parent)
    finally:
        os.close(parent)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1 or before.st_size > cap:
            raise _Reject('source must be a regular one-link file within cap')
        blocks = []
        total = 0
        while True:
            tick()
            block = os.read(fd, min(65536, cap + 1 - total))
            tick()
            if not block:
                break
            total += len(block)
            if total > cap:
                raise _Reject('source grew beyond cap')
            blocks.append(block)
        after = os.fstat(fd)
        if (not stat.S_ISREG(after.st_mode) or after.st_nlink != 1
                or (after.st_dev, after.st_ino) != (before.st_dev, before.st_ino)
                or after.st_size != before.st_size or after.st_size != total
                or after.st_mtime_ns != before.st_mtime_ns or after.st_ctime_ns != before.st_ctime_ns):
            raise _Reject('source identity, size or link count changed during read')
        data = b''.join(blocks)
    finally:
        os.close(fd)
    tick()
    return data


def _plan_tables(gate, plan_bytes, tick):
    """Strictly parse the pinned plan with the gate's parser and derive the twenty-job tables."""
    plan = gate['parse'](plan_bytes)
    tick()
    if type(plan) is not dict:
        raise _Reject('plan must be an object')
    job_list = plan['jobs']
    order = plan['order']
    if type(job_list) is not list or type(order) is not list:
        raise _Reject('plan jobs/order must be lists')
    jobs = {}
    for job in job_list:
        if type(job) is not dict or type(job.get('item')) is not str or job['item'] in jobs:
            raise _Reject('plan job identity')
        jobs[job['item']] = job
    if len(jobs) != PLAN_JOB_COUNT or order != [job['item'] for job in job_list]:
        raise _Reject('plan order must list exactly the twenty jobs')
    final_gate = plan['final_gate']
    if type(final_gate) is not str or final_gate != order[-1] or jobs[final_gate]['kind'] != 'gate':
        raise _Reject('plan final gate')
    gate_program = plan['programs']['gate']
    if (gate_program['algorithm'] != GATE_PATH or gate_program['algorithm_sha256'] != GATE_SHA256
            or {'path': GATE_PATH, 'sha256': GATE_SHA256} not in plan['pins']):
        raise _Reject('plan gate program differs from the approved validator pin')
    calibrations = frozenset(job['item'] for job in plan['future_calibration_jobs'])
    if calibrations & frozenset(jobs):
        raise _Reject('calibration items must stay outside the twenty-job plan')
    return plan, jobs, order, calibrations


def _offline_snapshot_dm21_reader(plan, original_dm21, tick):
    """Build the OFFLINE SNAPSHOT replacement for the gate's anchored_read_bytes (only verify_controls reads).

    Offline snapshot evaluation, NOT a real-path reader smoke and never kernel or filesystem evidence: it serves the
    caller-supplied original_dm21 bytes for exactly plan.dm21_path, only while their SHA-256 equals plan.dm21_sha256
    and their length is within the requested cap, and rejects every other requested path.
    """
    import hashlib
    bound_path = plan['dm21_path']
    bound_sha256 = plan['dm21_sha256']
    if type(bound_path) is not str or type(bound_sha256) is not str or type(original_dm21) is not bytes:
        raise _Reject('offline DM21 snapshot binding types')
    if hashlib.sha256(original_dm21).hexdigest() != bound_sha256:
        raise _Reject('offline DM21 snapshot digest differs from plan.dm21_sha256')

    def offline_snapshot_dm21_read_bytes(path, cap, check=None):
        tick()
        if type(path) is not str or path != bound_path:
            raise OSError('offline DM21 snapshot serves only plan.dm21_path')
        if type(cap) is not int or len(original_dm21) > cap:
            raise OSError('offline DM21 snapshot exceeds the requested cap')
        if hashlib.sha256(original_dm21).hexdigest() != bound_sha256:
            raise OSError('offline DM21 snapshot digest differs from plan.dm21_sha256')
        if check is not None:
            check()
        tick()
        return original_dm21

    return offline_snapshot_dm21_read_bytes


def _replay(gate, plan, jobs, order, calibrations, item, files, prefix, tick):
    """Replay the complete audited prefix in plan order, then check the current item's declared outputs."""
    if item in calibrations or item not in jobs:
        raise _Reject('item outside the twenty-job plan (calibrations are excluded)')
    position = order.index(item)
    if len(prefix) != position:
        raise _Reject('prefix must hold exactly the preceding plan items')
    state = {'ok': {}, 'states': {}, 'records': [], 'controls': None, 'datafiles': None}
    for index in range(position):
        tick()
        name = order[index]
        job = jobs[name]
        record = prefix[index]
        if type(record) is not dict or any(type(key) is not str for key in record) or set(record) != PREFIX_RECORD_KEYS:
            raise _Reject('prefix record must be exactly {item, files, audit_bytes}')
        if type(record['item']) is not str or record['item'] != name:
            raise _Reject('prefix order differs from plan order')
        record_files = _declared_files(job, record['files'], gate['CAP'])
        audit_bytes = record['audit_bytes']
        if type(audit_bytes) is not bytes or len(audit_bytes) > AUDIT_CAP:
            raise _Reject('prefix audit_bytes type/cap')
        hashes = {output: gate['digest'](record_files[output]) for output in job['outputs']}
        tick()
        _check_audit(gate, job, audit_bytes, hashes)
        _check_job(gate, plan, order, job, record_files, state, tick)
        state['ok'][name] = True
        state['records'].append({'item': name, 'problems': [], 'artifacts': hashes})
    tick()
    current = _declared_files(jobs[item], files, gate['CAP'])
    _check_job(gate, plan, order, jobs[item], current, state, tick)
    tick()
    return True


def _declared_files(job, files, cap):
    """Private copy holding exactly the job's declared outputs as immutable bytes within the gate artifact cap."""
    outputs = job['outputs']
    if (type(outputs) is not list or not outputs or any(type(name) is not str for name in outputs)
            or len(set(outputs)) != len(outputs)):
        raise _Reject('plan declared outputs')
    if type(files) is not dict or any(type(name) is not str for name in files) or set(files) != set(outputs):
        raise _Reject('files must map exactly the declared output names')
    copy = {}
    for name in outputs:
        if not name or '/' in name or '\x00' in name or name in ('.', '..'):
            raise _Reject('declared output must be a plain name')
        data = files[name]
        if type(data) is not bytes or len(data) > cap:
            raise _Reject('declared output must be bytes within the gate artifact cap')
        copy[name] = data
    return copy


def _check_audit(gate, job, audit_bytes, hashes):
    """Exact canonical ext-search-job-audit-v1 schema as the gate consumes it (syntax only, never provenance)."""
    exact = gate['exact']
    akeys = gate['AKEYS']
    audit = gate['canonical'](audit_bytes, akeys)
    if type(audit) is not dict or set(audit) != set(akeys):
        raise _Reject('audit keys')
    wanted = {'format': 'ext-search-job-audit-v1', 'item': job['item'], 'plan_sha256': PLAN_SHA256,
              'verdict': 'AUDITED_PASS', 'settled': True, 'exit_code': job['exit']}
    for key, value in wanted.items():
        if not exact(audit[key], value):
            raise _Reject('audit ' + key)
    if not exact(audit['declared_output_sha256'], hashes):
        raise _Reject('audit output digests differ from the supplied declared outputs')
    if not gate['hex64'](audit['receipt_sha256']):
        raise _Reject('audit receipt_sha256 must be lowercase 64-hex')
    if any(type(audit[key]) is not str for key in ('auditor', 'at', 'notes')) or not audit['auditor'] or not audit['at']:
        raise _Reject('audit string fields')


def _check_job(gate, plan, order, job, files, state, tick):
    """Dispatch on the plan job kind exactly as the gate's audited-prefix loop does."""
    kind = job['kind']
    if kind == 'data':
        _check_data(gate, plan, files, state, tick)
    elif kind == 'search':
        _check_search(gate, plan, job, files, state, tick)
    elif kind == 'gate':
        _check_gate(gate, plan, order, job, files, state, tick)
    else:
        raise _Reject('unknown job kind')


def _check_data(gate, plan, files, state, tick):
    """DATA maker result, control manifest, DM21 provenance pin and verify_controls (gate main DATA branch)."""
    exact = gate['exact']
    digest = gate['digest']
    mfiles = gate['MFILES']
    tick()
    maker = gate['canonical'](files['result.json'], DATA_RESULT_KEYS)
    tick()
    if not gate['finite_wall'](maker['wall_s']):
        raise _Reject('maker wall field')
    if (not exact(maker['status'], 'OK') or maker['reason'] is not None or not exact(maker['files'], list(mfiles))
            or not exact(maker['manifest_sha256'], digest(files['manifest.json']))):
        raise _Reject('maker result')
    manifest = gate['canonical'](files['manifest.json'], DATA_MANIFEST_KEYS)
    tick()
    if (not exact(manifest['format'], 'ext-search-controls-v1') or type(manifest['files']) is not dict
            or set(manifest['files']) != set(mfiles)):
        raise _Reject('control manifest')
    if not exact(manifest['dm21_input_sha256'], plan['dm21_sha256']):
        raise _Reject('DM21 provenance pin')
    for name in mfiles:
        if not exact(manifest['files'][name], {'sha256': digest(files[name]), 'bytes': len(files[name])}):
            raise _Reject('control data hash')
    controls = manifest['controls']
    if (type(controls) is not list or any(type(control) is not dict for control in controls)
            or [control.get('name') for control in controls] != list(CONTROL_NAMES)):
        raise _Reject('control names')
    tick()
    derived = gate['verify_controls'](manifest, files, plan, tick)
    tick()
    state['controls'] = derived
    state['datafiles'] = files


def _check_search(gate, plan, job, files, state, tick):
    """Search result: planned status/reason site, exact typed per-status schema, actual raw digest, pinned program
    digest, COMPLETE extension/chunk checks, parity/planted premises and exact independent peer equality."""
    exact = gate['exact']
    if not state['ok'].get('DATA') or state['controls'] is None:
        raise _Reject('unaudited DATA dependency')
    control = state['controls'][job['control']]
    raw = state['datafiles'][control['raw']]
    if not exact(job['status'], dict(PLANNED_STATUS)[control['expected']]):
        raise _Reject('planned status differs from the derived control premise')
    program = plan['programs'][job['program']]
    pinned = program['algorithm_sha256']
    if not gate['hex64'](pinned) or {'path': program['algorithm'], 'sha256': pinned} not in plan['pins']:
        raise _Reject('plan program pin')
    tick()
    result = gate['validate_result'](files['result.json'], job, raw, control)
    tick()
    if not exact(result['program_sha256'], pinned):
        raise _Reject('result program_sha256 differs from the pinned algorithm source digest')
    if control['expected'] == 'COMPLETE_ZERO' and result['solutions']:
        raise _Reject('parity control notzero')
    if control['expected'] == 'COMPLETE_CONTAINS':
        known = gate['rawrows'](state['datafiles'][control['known']])[0]
        if known not in result['solutions']:
            raise _Reject('known deleted row missing')
    state['states'][job['item']] = result
    peer = job.get('compare_to')
    if peer is not None:
        if (not state['ok'].get(peer) or state['states'][peer]['solutions'] != result['solutions']
                or state['states'][peer]['solutions_sha256'] != result['solutions_sha256']):
            raise _Reject('independent COMPLETE sets disagree')


def _check_gate(gate, plan, order, job, files, state, tick):
    """Gate result: OK record for its exact prefix, qualified only for the final gate, UNEVALUATED target claim,
    finite float wall and items exactly equal to the records recomputed from the actual supplied prefix."""
    exact = gate['exact']
    item = job['item']
    tick()
    result = gate['canonical'](files['result.json'], gate['GKEYS'])
    tick()
    expected = {'status': 'OK', 'reason': None, 'self': item, 'plan_sha256': PLAN_SHA256,
                'prefix': order[:order.index(item)], 'all_as_expected': True,
                'qualified': item == plan['final_gate'], 'target_claim': 'UNEVALUATED'}
    for key, value in expected.items():
        if not exact(result[key], value):
            raise _Reject('gate field ' + key)
    if not gate['finite_wall'](result['wall_s']) or type(result['items']) is not list:
        raise _Reject('gate wall/items schema')
    if not exact(result['items'], state['records']):
        raise _Reject('gate item records differ from the recomputed audited prefix')
