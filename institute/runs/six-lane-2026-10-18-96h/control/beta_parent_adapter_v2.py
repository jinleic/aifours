"""SOURCE ONLY, UNTESTED. V2 coherent snapshot repair. Compose frozen parent beta consumers over pinned evidence.

The parent supplies input SHA256s as authority and retains the EvidenceReader on every exception.
This module reads/compiles only pinned consumer bytes inside evaluate_pinned, never imports them
by pathname, writes nothing and starts no processes. A decision is NOT a canonical audit or release.
A matching receipt hash authenticates bytes, not runtime truth. Parent-observed execution, actual
nested exit, complete captures, date provenance, full endedness and late resources remain required.
REQUIRED EXTERNAL PRECONDITION: the parent enforces an exclusive immutable publication freeze across every supplied file, namespace and alias for the whole decision. This is not established by NOFOLLOW or hashes alone. No raw shared-supervisor adapter is guessed here; it must be built against a reviewed final schema.
"""
import copy
import hashlib
import json
import math

PLAN_PATH = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/ext-search-plan-v5.json'
PLAN_SHA = '254b44c372fd170640198dbdc773cca2a1893607127d373320b8518a54e59731'
CAPTURE_PATH = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/beta_capture_audit_v4.py'
CAPTURE_SHA = '9b50052136d82bd21914ca0ec83f561881fbee280ef472f09a20354e89b6c645'
SCHEMA_PATH = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/beta_schema_audit_v2.py'
SCHEMA_SHA = '9e910e2d90ad1b80266fd38abc69d73e597fc589763b4464cb9251dd209be103'
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


class _Bundle:
    """One private acquisition per path. Both consumers see these exact bytes and selected actual metadata.

    Base-reader ownership remains available to the caller on every exception. Final fresh reads test
    persistence but are not an atomic filesystem snapshot; the publication-freeze precondition is mandatory.
    """
    def __init__(self, reader, check):
        self.reader, self.check = reader, check
        self.entries = {}

    def read_bytes(self, path, cap):
        _tick(self.check)
        if type(path) is not str or type(cap) is not int or cap < 0:
            raise SnapshotRefusal('bundle path/cap')
        if path not in self.entries:
            data = self.reader.read_bytes(path, cap)
            meta = self.reader.last_file(path)
            if (type(data) is not bytes or len(data) > cap or type(meta) is not dict
                    or meta.get('path') != path or meta.get('completed') is not True
                    or meta.get('bytes_seen') != len(data)
                    or meta.get('sha256') != hashlib.sha256(data).hexdigest()):
                raise SnapshotRefusal('missing current successful actual acquisition')
            self.entries[path] = {'bytes': data, 'metadata': copy.deepcopy(meta), 'cap': cap}
        entry = self.entries[path]
        if len(entry['bytes']) > cap:
            raise SnapshotRefusal('cached immutable acquisition exceeds requested cap')
        _tick(self.check)
        return entry['bytes']

    def revalidate(self):
        """Fresh same-path readbacks must match the originally SELECTED bytes and actual identity."""
        results = []
        for path, selected in self.entries.items():
            current = self.reader.read_bytes(path, selected['cap'])
            actual = self.reader.last_file(path)
            if (type(actual) is not dict or actual.get('completed') is not True
                    or current != selected['bytes']
                    or not _exact(actual.get('after'), selected['metadata'].get('after'))):
                raise SnapshotRefusal('publication changed after selected acquisition: ' + path)
            results.append({'path': path, 'sha256': selected['metadata']['sha256'],
                            'actual_metadata': copy.deepcopy(actual['after'])})
            _tick(self.check)
        return results


def _directory_snapshot(reader, path, check):
    names = reader.directory_names(path)
    report = reader.report()
    if type(report) is not dict or not report.get('observations'):
        raise SnapshotRefusal('directory census report unavailable')
    row = report['observations'][-1]
    if (row.get('kind') != 'directory' or row.get('path') != path or row.get('completed') is not True
            or sorted(row.get('names', [])) != names):
        raise SnapshotRefusal('current directory census not established')
    result = {'names': list(names), 'before': copy.deepcopy(row['before']), 'after': copy.deepcopy(row['after'])}
    _tick(check)
    return result


def _context(context, expected, bundle, check):
    keys = {'format', 'plan', 'original_dm21', 'prefix', 'derivation', 'publication_freeze'}
    if type(context) is not dict or set(context) != keys or context['format'] != 'beta-parent-schema-context-v2':
        raise SnapshotRefusal('schema context v2 keys/format')
    if not _exact(context['plan'], {'path': PLAN_PATH, 'sha256': PLAN_SHA}):
        raise SnapshotRefusal('context plan authority')
    plan_bytes = _pinned(context['plan'], bundle, check)
    plan = _json(plan_bytes)
    if not _exact(context['original_dm21'], {'path': plan['dm21_path'], 'sha256': plan['dm21_sha256']}):
        raise SnapshotRefusal('original DM21 binding')
    original = _pinned(context['original_dm21'], bundle, check, 1 << 20)
    if type(context['prefix']) is not list or len(context['prefix']) > 19:
        raise SnapshotRefusal('prefix count/type')
    prefix, authority = [], []
    for row in context['prefix']:
        _tick(check)
        if type(row) is not dict or set(row) != {'item', 'files', 'audit'} or type(row['files']) is not dict:
            raise SnapshotRefusal('prefix reference keys')
        files = {name: _pinned(ref, bundle, check) for name, ref in row['files'].items()}
        prefix.append({'item': row['item'], 'files': files,
                       'audit_bytes': _pinned(row['audit'], bundle, check, 1 << 20)})
        authority.append({'item': row['item'], 'audit_sha256': row['audit']['sha256']})
    freeze = _json(_pinned(context['publication_freeze'], bundle, check, 1 << 20))
    freeze_keys = {'format', 'mode', 'job_dir', 'immutable_paths', 'prefix_authority'}
    if (type(freeze) is not dict or set(freeze) != freeze_keys
            or freeze['format'] != 'beta-parent-publication-freeze-v1'
            or not _exact(freeze['mode'], expected['mode']) or not _exact(freeze['job_dir'], expected['job_dir'])
            or not _exact(freeze['prefix_authority'], authority)
            or type(freeze['immutable_paths']) is not list
            or any(type(path) is not str for path in freeze['immutable_paths'])
            or len(freeze['immutable_paths']) != len(set(freeze['immutable_paths']))):
        raise SnapshotRefusal('parent publication-freeze authority/binding')
    # This checks the parent-authenticated declaration, not that a child cannot mutate the OS.
    return plan_bytes, original, prefix, freeze


def _current_files(expected, bundle):
    outputs, directory = expected['outputs'], expected['job_dir']
    if type(outputs) is not list or not outputs or type(directory) is not str:
        raise SnapshotRefusal('current output binding')
    result = {}
    for name in outputs:
        if type(name) is not str or name in ('', '.', '..') or '/' in name or '\x00' in name:
            raise SnapshotRefusal('current output name')
        result[name] = bundle.read_bytes(directory + '/' + name, CAP)
    return result


def _derivation(manifest_ref, refs, expected, observed, capture, schema, schema_args, bundle, check):
    """Verify exactly the approved transformation; never change upstream receipt or measured-exit evidence."""
    if expected['mode'] != 'FIXTURE' or observed['mode'] != 'FIXTURE':
        raise SnapshotRefusal('synthetic derivatives are fixture-only')
    manifest = _json(_pinned(manifest_ref, bundle, check, 1 << 20))
    keys = {'format', 'expectation_sha256', 'observation_sha256', 'upstream_observation', 'mutations'}
    if type(manifest) is not dict or set(manifest) != keys or manifest['format'] != 'beta-parent-synthetic-derivation-v1':
        raise SnapshotRefusal('derivation schema')
    if (manifest['expectation_sha256'] != refs['expectation']['sha256']
            or manifest['observation_sha256'] != refs['observation']['sha256']):
        raise SnapshotRefusal('derivation input pins')
    upstream = _json(_pinned(manifest['upstream_observation'], bundle, check))
    if capture(expected, upstream, bundle.read_bytes) != []:
        raise SnapshotRefusal('synthetic upstream capture baseline invalid')
    plan_bytes, original, prefix, current = schema_args
    if schema(plan_bytes, expected['item'], current, prefix, original, check, bundle.read_bytes) != []:
        raise SnapshotRefusal('synthetic upstream schema baseline invalid')
    mutations = manifest['mutations']
    if type(mutations) is not list or not 1 <= len(mutations) <= 8:
        raise SnapshotRefusal('synthetic mutation count')
    paths = []
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
        if any(key[:len(prior)] == prior or prior[:len(key)] == key for prior in paths):
            raise SnapshotRefusal('duplicate or ancestor/descendant mutation conflict')
        paths.append(key)
    derived = copy.deepcopy(upstream)
    for mutation in mutations:
        target = derived
        for component in mutation['path'][:-1]:
            if type(target) is not dict or component not in target:
                raise SnapshotRefusal('mutation parent unavailable')
            target = target[component]
        field = mutation['path'][-1]
        if type(target) is not dict or field not in target or _exact(target[field], mutation['value']):
            raise SnapshotRefusal('mutation absent or no-op')
        target[field] = copy.deepcopy(mutation['value'])
    if _exact(derived, upstream) or not _exact(derived, observed):
        raise SnapshotRefusal('transformed input is unchanged or differs from approved derivation')
    return {'manifest': copy.deepcopy(manifest_ref), 'verified': True,
            'upstream_observation': copy.deepcopy(manifest['upstream_observation']),
            'upstream_parent_reported_exit': upstream.get('actual_exit'),
            'mutations': copy.deepcopy(mutations), 'actual_exit_is_measured': False}


def evaluate_pinned(inputs, reader, deadline_check):
    """Caller owns reader and parent SHA authority. No writes, launch, canonical audit or release.

    Both consumers receive ONE acquired byte/identity bundle; an external publication freeze is mandatory.
    The parent retains this reader on every BaseException. Failed tail construction never returns PASS.
    """
    fired, errors = set(), []
    refs, expected, observed, context = None, None, None, None
    synthetic, selected, persistence = None, {}, []
    before_dir, after_dir, context_values, current = None, None, None, None
    bundle = _Bundle(reader, deadline_check)
    try:
        _tick(deadline_check)
        if type(inputs) is not dict or set(inputs) != {'expectation', 'observation', 'context'}:
            raise SnapshotRefusal('input reference keys')
        refs = copy.deepcopy(inputs)
        _tick(deadline_check)
        expected = _json(_pinned(refs['expectation'], bundle, deadline_check))
        observed = _json(_pinned(refs['observation'], bundle, deadline_check))
        context = _json(_pinned(refs['context'], bundle, deadline_check))
        if type(context) is dict and context.get('derivation') is not None:
            synthetic = {'requested': True, 'verified': False,
                         'manifest': copy.deepcopy(context['derivation']), 'actual_exit_is_measured': False}
        capture = _load(CAPTURE_PATH, CAPTURE_SHA, 'audit_capture', bundle, deadline_check)
        schema = _load(SCHEMA_PATH, SCHEMA_SHA, 'audit_schema', bundle, deadline_check)
        try:
            before_dir = _directory_snapshot(reader, expected['job_dir'], deadline_check)
        except Exception as exc:
            fired.add('X4 ARTIFACT_SET_OR_DIGEST')
            errors.append({'stage': 'initial_artifact_census', 'error': repr(exc)})
        capture_causes = capture(expected, observed, bundle.read_bytes)
        if type(capture_causes) is not list or any(type(c) is not str or c not in CAUSES for c in capture_causes):
            raise SnapshotRefusal('capture returned invalid causes')
        fired.update(capture_causes)
        try:
            context_values = _context(context, expected, bundle, deadline_check)
        except Exception as exc:
            fired.add('X7 PROVENANCE')
            errors.append({'stage': 'context_authority', 'error': repr(exc)})
        try:
            current = _current_files(expected, bundle)
        except Exception as exc:
            fired.update(('X4 ARTIFACT_SET_OR_DIGEST', 'X5 RESULT_SCHEMA'))
            errors.append({'stage': 'current_artifact_bytes', 'error': repr(exc)})
        if context_values is not None and current is not None:
            plan_bytes, original, prefix, freeze = context_values
            schema_causes = schema(plan_bytes, expected['item'], current, prefix, original,
                                   deadline_check, bundle.read_bytes)
            if schema_causes not in ([], ['X5 RESULT_SCHEMA']):
                raise SnapshotRefusal('schema returned invalid causes')
            fired.update(schema_causes)
            if synthetic is not None:
                try:
                    synthetic = _derivation(context['derivation'], refs, expected, observed, capture, schema,
                                            (plan_bytes, original, prefix, current), bundle, deadline_check)
                except Exception as exc:
                    fired.add('X7 PROVENANCE')
                    errors.append({'stage': 'synthetic_derivation', 'error': repr(exc)})
        try:
            after_dir = _directory_snapshot(reader, expected['job_dir'], deadline_check)
            if (before_dir is None or not _exact(before_dir, after_dir)
                    or not _exact(after_dir['names'], sorted(observed['actual_artifact_names']))
                    or set(after_dir['names']) != set(expected['outputs'])):
                fired.add('X4 ARTIFACT_SET_OR_DIGEST')
            for name in expected['outputs']:
                path = expected['job_dir'] + '/' + name
                entry = bundle.entries[path]
                meta, record = entry['metadata'], observed['artifacts'][name]
                if (not _exact(record['ino'], meta['after']['ino'])
                        or not _exact(record['nlink'], meta['after']['nlink'])
                        or not _exact(record['bytes'], len(entry['bytes']))
                        or not _exact(record['sha256'], meta['sha256'])):
                    fired.add('X4 ARTIFACT_SET_OR_DIGEST')
                selected[name] = {'path': path, 'sha256': meta['sha256'],
                                  'bytes': len(entry['bytes']), 'actual_metadata': copy.deepcopy(meta['after'])}
        except Exception as exc:
            fired.add('X4 ARTIFACT_SET_OR_DIGEST')
            errors.append({'stage': 'selected_artifact_identity_census', 'error': repr(exc)})
        if context_values is not None:
            freeze = context_values[3]
            if not set(bundle.entries).issubset(set(freeze['immutable_paths'])):
                fired.add('X7 PROVENANCE')
                errors.append({'stage': 'publication_freeze', 'error': 'freeze does not cover every acquisition path'})
        try:
            persistence = bundle.revalidate()
        except Exception as exc:
            fired.update(('X4 ARTIFACT_SET_OR_DIGEST', 'X7 PROVENANCE'))
            errors.append({'stage': 'snapshot_persistence', 'error': repr(exc)})
        _tick(deadline_check)
    except Exception as exc:
        fired.add('X7 PROVENANCE')
        errors.append({'stage': 'input_or_consumer', 'error': repr(exc)})
    try:
        report = reader.report()
        if type(report) is not dict or report.get('unresolved') != []:
            fired.add('X6 UNSETTLED')
        decision = {'format': 'beta-parent-consumer-decision-v2',
                    'verdict': 'AUDITED_FAIL' if fired else 'AUDITED_PASS',
                    'causes': [cause for cause in CAUSES if cause in fired],
                    'input_pins': copy.deepcopy(refs),
                    'consumer_pins': {'capture': CAPTURE_SHA, 'schema': SCHEMA_SHA},
                    'synthetic_derivation': copy.deepcopy(synthetic),
                    'mode': expected.get('mode') if type(expected) is dict else None,
                    'nested_exit': {'value': observed.get('actual_exit') if type(observed) is dict else None,
                                    'kind': 'SYNTHETIC_PREDICATE_INPUT' if synthetic is not None
                                            else 'UNVERIFIED_PARENT_REPORTED_NESTED_EXIT'},
                    'selected_artifacts': copy.deepcopy(selected),
                    'snapshot_persistence': copy.deepcopy(persistence),
                    'directory_before': copy.deepcopy(before_dir), 'directory_after': copy.deepcopy(after_dir),
                    'errors': copy.deepcopy(errors), 'reader': report,
                    'canonical_audit_written': False, 'release_authority': False, 'runtime_authority': False,
                    'boundary': 'Pinned immutable acquisition bundle under parent-enforced publication freeze; actual execution/date/endedness and independent five-part transaction remain external required evidence.'}
        _tick(deadline_check)  # AFTER the complete detached report and result have been assembled
        return decision
    except Exception as exc:
        # This path may not certify timeliness; it can only fail. Parent keeps the original reader regardless.
        fired.add('X7 PROVENANCE')
        try:
            retained = reader.report()
        except Exception as report_exc:
            retained = {'report_unavailable': repr(report_exc)}
            fired.add('X6 UNSETTLED')
        if retained.get('unresolved') != []:
            fired.add('X6 UNSETTLED')
        return {'format': 'beta-parent-consumer-decision-v2', 'verdict': 'AUDITED_FAIL',
                'causes': [cause for cause in CAUSES if cause in fired],
                'input_pins': refs, 'synthetic_derivation': synthetic,
                'nested_exit': {'value': observed.get('actual_exit') if type(observed) is dict else None,
                                'kind': 'SYNTHETIC_PREDICATE_INPUT' if synthetic is not None else 'UNVERIFIED'},
                'errors': errors + [{'stage': 'final_report_or_deadline', 'error': repr(exc)}],
                'reader': retained, 'canonical_audit_written': False,
                'release_authority': False, 'runtime_authority': False}
