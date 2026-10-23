"""SOURCE ONLY, UNTESTED. Compose frozen parent beta consumers over pinned evidence.

The parent supplies input SHA256s as authority and retains the EvidenceReader on every exception.
This module reads/compiles only pinned consumer bytes inside evaluate_pinned, never imports them
by pathname, writes nothing and starts no processes. A decision is NOT a canonical audit or release.
A matching receipt hash authenticates bytes, not runtime truth. Parent-observed execution, actual
nested exit, complete captures, date provenance, full endedness and late resources remain required.
No raw shared-supervisor adapter is guessed here; it must be built against a reviewed final schema.
"""
import copy
import hashlib
import json
import math

PLAN_PATH = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v5.json'
PLAN_SHA = '254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731'
CAPTURE_PATH = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/beta_capture_audit_v1.py'
CAPTURE_SHA = '54ee4dcc221a0dfdad19a7475fcde1bb9ae47f269a62ff2edab74a3371dc51c3'
SCHEMA_PATH = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/beta_schema_audit_v1.py'
SCHEMA_SHA = '33900dc09c9eb62c8ecf87b66b9a1559b5ca40c0d7f3316441c0003f9f5f75ce'
CAP = 16 << 20
CAUSES = ('X1 EXIT_MISMATCH', 'X2 STDOUT_CAPTURE_MISSING', 'X2 STDOUT_CAPTURE_INCOMPLETE',
          'X2 STDOUT_NOT_EXACT_RESULT_LINE', 'X3 STDERR_CAPTURE_MISSING',
          'X3 STDERR_CAPTURE_INCOMPLETE', 'X3 STDERR_NONEMPTY', 'X4 ARTIFACT_SET_OR_DIGEST',
          'X5 RESULT_SCHEMA', 'X6 UNSETTLED', 'X7 PROVENANCE')


class SnapshotRefusal(ValueError):
    pass


def _tick(check):
    if not callable(check) or check() is not None:
        raise SnapshotRefusal('deadline_check must return None or raise')


def _hex(value):
    return type(value) is str and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def _exact(left, right):
    if type(left) is not type(right):
        return False
    if type(left) is dict:
        return set(left) == set(right) and all(_exact(left[k], right[k]) for k in left)
    if type(left) is list:
        return len(left) == len(right) and all(_exact(a, b) for a, b in zip(left, right))
    return left == right


def _json(data):
    def pairs(rows):
        value = {}
        for key, entry in rows:
            if key in value:
                raise SnapshotRefusal('duplicate JSON key')
            value[key] = entry
        return value
    def bad(_):
        raise SnapshotRefusal('nonfinite JSON')
    def number(text):
        value = float(text)
        if not math.isfinite(value):
            bad(text)
        return value
    if type(data) is not bytes or len(data) > CAP:
        raise SnapshotRefusal('JSON type/cap')
    return json.loads(data.decode('utf-8'), object_pairs_hook=pairs,
                      parse_constant=bad, parse_float=number)


def _pinned(ref, reader, check, cap=CAP):
    if type(ref) is not dict or set(ref) != {'path', 'sha256'} or not _hex(ref['sha256']):
        raise SnapshotRefusal('pinned reference schema')
    _tick(check)
    data = reader.read_bytes(ref['path'], cap)
    if type(data) is not bytes or hashlib.sha256(data).hexdigest() != ref['sha256']:
        raise SnapshotRefusal('pinned bytes mismatch')
    _tick(check)
    return data


def _load(path, digest, symbol, reader, check):
    source = _pinned({'path': path, 'sha256': digest}, reader, check, 1 << 20)
    code = compile(source, path, 'exec', dont_inherit=True)
    _tick(check)
    namespace = {'__name__': 'parent_beta_snapshot_consumer', '__file__': path}
    exec(code, namespace)
    _tick(check)
    function = namespace.get(symbol)
    if not callable(function):
        raise SnapshotRefusal('approved consumer entry missing')
    return function


def _schema_inputs(context, expectation, reader, check):
    if type(context) is not dict or set(context) != {'format', 'plan', 'original_dm21', 'prefix', 'derivation'}:
        raise SnapshotRefusal('schema context keys')
    if context['format'] != 'beta-parent-schema-context-v1':
        raise SnapshotRefusal('schema context format')
    if not _exact(context['plan'], {'path': PLAN_PATH, 'sha256': PLAN_SHA}):
        raise SnapshotRefusal('context plan authority')
    plan_bytes = _pinned(context['plan'], reader, check)
    plan = _json(plan_bytes)
    if not _exact(context['original_dm21'], {'path': plan['dm21_path'], 'sha256': plan['dm21_sha256']}):
        raise SnapshotRefusal('original DM21 binding')
    original = _pinned(context['original_dm21'], reader, check, 1 << 20)
    if type(context['prefix']) is not list or len(context['prefix']) > 19:
        raise SnapshotRefusal('prefix count/type')
    prefix = []
    for row in context['prefix']:
        _tick(check)
        if type(row) is not dict or set(row) != {'item', 'files', 'audit'} or type(row['files']) is not dict:
            raise SnapshotRefusal('prefix reference keys')
        if len(row['files']) > 256:
            raise SnapshotRefusal('prefix file cap')
        files = {name: _pinned(ref, reader, check) for name, ref in row['files'].items()}
        prefix.append({'item': row['item'], 'files': files,
                       'audit_bytes': _pinned(row['audit'], reader, check, 1 << 20)})
    outputs, directory = expectation['outputs'], expectation['job_dir']
    if type(outputs) is not list or not 1 <= len(outputs) <= 256 or type(directory) is not str:
        raise SnapshotRefusal('current outputs binding')
    current = {}
    for name in outputs:
        if type(name) is not str or name in ('', '.', '..') or '/' in name or '\x00' in name:
            raise SnapshotRefusal('current output name')
        current[name] = reader.read_bytes(directory + '/' + name, CAP)
    return plan_bytes, original, prefix, current


def _verify_derivation(manifest_ref, refs, expected, observed, capture, schema_args, schema, reader, check):
    """Verify an approved, labelled transformation; never rewrite the genuine upstream receipt or exit.

    The input manifest hash is parent authority. This proves an exact derivation from supplied pinned
    upstream evidence, NOT that upstream runtime claims were true; that is the separate parent transaction.
    """
    if expected['mode'] != 'FIXTURE' or observed['mode'] != 'FIXTURE':
        raise SnapshotRefusal('synthetic derivatives are fixture-only')
    manifest = _json(_pinned(manifest_ref, reader, check, 1 << 20))
    keys = {'format', 'expectation_sha256', 'observation_sha256', 'upstream_observation', 'mutations'}
    if type(manifest) is not dict or set(manifest) != keys or manifest['format'] != 'beta-parent-synthetic-derivation-v1':
        raise SnapshotRefusal('derivation schema')
    if (manifest['expectation_sha256'] != refs['expectation']['sha256']
            or manifest['observation_sha256'] != refs['observation']['sha256']):
        raise SnapshotRefusal('derivation input pins')
    upstream = _json(_pinned(manifest['upstream_observation'], reader, check))
    if capture(expected, upstream, reader.read_bytes) != []:
        raise SnapshotRefusal('synthetic upstream capture baseline invalid')
    plan_bytes, original, prefix, current = schema_args
    if schema(plan_bytes, expected['item'], current, prefix, original, check) != []:
        raise SnapshotRefusal('synthetic upstream schema baseline invalid')
    mutations = manifest['mutations']
    if type(mutations) is not list or not 1 <= len(mutations) <= 8:
        raise SnapshotRefusal('synthetic mutation count')
    derived = copy.deepcopy(upstream)
    seen = set()
    for mutation in mutations:
        if type(mutation) is not dict or set(mutation) != {'path', 'value'} or type(mutation['path']) is not list:
            raise SnapshotRefusal('mutation schema')
        path = mutation['path']
        allowed = (path == ['actual_exit'] or path == ['captures', 'stderr']
                   or (len(path) == 3 and path[:2] == ['captures', 'stderr']
                       and path[2] in ('present', 'bytes_seen', 'bytes_stored', 'eof', 'overflow', 'error')))
        if not allowed:
            raise SnapshotRefusal('unlicensed synthetic field mutation')
        key = tuple(path)
        if key in seen:
            raise SnapshotRefusal('duplicate mutation')
        seen.add(key)
        target = derived
        for component in path[:-1]:
            if type(target) is not dict or component not in target:
                raise SnapshotRefusal('mutation parent unavailable')
            target = target[component]
        if type(target) is not dict or path[-1] not in target:
            raise SnapshotRefusal('mutation field unavailable')
        target[path[-1]] = mutation['value']
    if not _exact(derived, observed):
        raise SnapshotRefusal('transformed observation differs from approved derivation')
    return {'manifest': manifest_ref, 'upstream_observation': manifest['upstream_observation'],
            'mutations': mutations, 'actual_exit_is_measured': False}


def evaluate_pinned(inputs, reader, deadline_check):
    """Return an evidence decision, never write canonical audit/release files.

    Caller must retain reader on BaseException. Unexpected ordinary exceptions produce failed decisions,
    including their retained reader ledger. Provenance of expectation/input SHA pins is external parent
    authority; never pass child-authored pins as approval. Raw process-receipt adaptation is still separate.
    """
    fired, errors = set(), []
    synthetic = None
    observed = None
    expected = None
    try:
        _tick(deadline_check)
        if type(inputs) is not dict or set(inputs) != {'expectation', 'observation', 'context'}:
            raise SnapshotRefusal('input reference keys')
        expected = _json(_pinned(inputs['expectation'], reader, deadline_check))
        observed = _json(_pinned(inputs['observation'], reader, deadline_check))
        context = _json(_pinned(inputs['context'], reader, deadline_check))
        capture = _load(CAPTURE_PATH, CAPTURE_SHA, 'audit_capture', reader, deadline_check)
        schema = _load(SCHEMA_PATH, SCHEMA_SHA, 'audit_schema', reader, deadline_check)
        capture_causes = capture(expected, observed, reader.read_bytes)
        if type(capture_causes) is not list or any(type(c) is not str or c not in CAUSES for c in capture_causes):
            raise SnapshotRefusal('consumer returned invalid causes')
        fired.update(capture_causes)
        try:
            args = _schema_inputs(context, expected, reader, deadline_check)
            plan_bytes, original, prefix, current = args
            schema_causes = schema(plan_bytes, expected['item'], current, prefix, original, deadline_check)
            if schema_causes not in ([], ['X5 RESULT_SCHEMA']):
                raise SnapshotRefusal('schema returned invalid causes')
            fired.update(schema_causes)
            if context['derivation'] is not None:
                synthetic = _verify_derivation(context['derivation'], inputs, expected, observed,
                                               capture, args, schema, reader, deadline_check)
        except Exception as exc:
            fired.add('X5 RESULT_SCHEMA')
            if type(context) is dict and context.get('derivation') is not None:
                fired.add('X7 PROVENANCE')
            errors.append({'stage': 'schema_context_or_derivation', 'error': repr(exc)})
        try:
            names = reader.directory_names(expected['job_dir'])
            if not _exact(sorted(names), sorted(observed['actual_artifact_names'])) or set(names) != set(expected['outputs']):
                fired.add('X4 ARTIFACT_SET_OR_DIGEST')
            for name in expected['outputs']:
                path = expected['job_dir'] + '/' + name
                actual = reader.last_file(path)
                record = observed['artifacts'][name]
                if (actual is None or not actual['completed'] or not _exact(record['ino'], actual['after']['ino'])
                        or not _exact(record['nlink'], actual['after']['nlink'])
                        or not _exact(record['bytes'], actual['bytes_seen'])
                        or not _exact(record['sha256'], actual['sha256'])):
                    fired.add('X4 ARTIFACT_SET_OR_DIGEST')
        except Exception as exc:
            fired.add('X4 ARTIFACT_SET_OR_DIGEST')
            errors.append({'stage': 'actual_artifact_identity_census', 'error': repr(exc)})
        _tick(deadline_check)
    except Exception as exc:
        fired.add('X7 PROVENANCE')
        errors.append({'stage': 'input_or_consumer', 'error': repr(exc)})
    report = reader.report()
    if type(report) is not dict or report.get('unresolved') != []:
        fired.add('X6 UNSETTLED')
    causes = [cause for cause in CAUSES if cause in fired]
    return {'format': 'beta-parent-consumer-decision-v1',
            'verdict': 'AUDITED_FAIL' if causes else 'AUDITED_PASS', 'causes': causes,
            'input_pins': inputs, 'consumer_pins': {'capture': CAPTURE_SHA, 'schema': SCHEMA_SHA},
            'synthetic_derivation': synthetic, 'mode': expected.get('mode') if type(expected) is dict else None,
            'actual_exit': observed.get('actual_exit') if type(observed) is dict else None,
            'errors': errors, 'reader': report, 'canonical_audit_written': False,
            'release_authority': False, 'runtime_authority': False,
            'boundary': 'Pinned snapshot predicates only; parent actual execution, date, process endedness and full five-part transaction remain external required evidence.'}
