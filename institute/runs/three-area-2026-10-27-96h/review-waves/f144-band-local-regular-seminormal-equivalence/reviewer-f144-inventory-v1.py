#!/usr/bin/env python3
"""Bind the completed f144 review and retained controls; no scientific code executed.
Metadata reads only; exclusively creates reviewer-f144-inventory-v1.json.
"""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent

def clock():
    return subprocess.check_output(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%SZ'], text=True).strip()

def meta(p):
    raw = p.read_bytes()
    result = dict(path=str(p), sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw))
    try:
        raw.decode('utf-8')
    except UnicodeDecodeError:
        result['LF'] = None
    else:
        result['LF'] = raw.count(b'\n')
    return result

if __name__ == '__main__':
    before = clock()
    dest = HERE / 'reviewer-f144-inventory-v1.json'
    if dest.exists():
        raise FileExistsError(dest)
    review = HERE / 'review-v1.md'
    if not review.is_file():
        raise FileNotFoundError(review)
    manifests = []
    for filename, expected in [('manifest-v1.json','24d290eac38f25d87fdaee0276f8ecae04609da0b20c810e852efc5e121f42d1'),
                               ('manifest-v2.json','843b051c235415a7e5faed2cd9a36e59737770a1c6b05acafc4c2c5b11a46344')]:
        path = HERE / filename
        pin = meta(path)
        if pin['sha256'] != expected:
            raise ValueError('manifest drift: ' + filename)
        manifest = json.loads(path.read_text())
        inputs = []
        for source in manifest['inputs_in_read_order']:
            actual = meta(Path(source['path']))
            for field in ('sha256','bytes','LF'):
                if source[field] != actual[field]:
                    raise ValueError('source drift: ' + source['path'] + ' field ' + field)
            inputs.append(actual)
        manifests.append(dict(manifest=pin, inputs=inputs))
    artifacts = [meta(path) for path in sorted(HERE.glob('reviewer-f144-*')) if path.is_file() and path != dest]
    scratch = [meta(Path('/tmp/f144-build') / name) for name in ('fb3','bands','bands2','sqsearch')]
    record = dict(
        kind='F144_REVIEW_AND_CONTROL_INTEGRITY_BINDING',
        clock_before_inventory=before,
        clock_after_input_reads=clock(),
        review=meta(review),
        manifests=manifests,
        reviewer_artifacts=artifacts,
        external_build_artifact_deviation=scratch,
        source_text_coverage=dict(v1=['full main proof','full author replay; read-only'],
                                  v2=['full mandatory seven-LF erratum','full main proof reread','full author replay reread; read-only']),
        native_clock_observations_utc=dict(original_manifest_check='2026-10-29T04:09:18Z',
            original_input_check='2026-10-29T04:09:31Z', manifest_v2_check='2026-10-29T04:26:57Z',
            erratum_check='2026-10-29T04:27:07Z',
            exact_controls_v1=['2026-10-29T04:27:49Z','2026-10-29T04:27:59Z'],
            fb3_exhaustive_v1=['2026-10-29T04:31:22Z','2026-10-29T04:31:23Z'],
            small_bands_v2=['2026-10-29T04:33:36Z','2026-10-29T04:33:48Z'],
            mutation_controls_v2=['2026-10-29T04:34:38Z','2026-10-29T04:34:38Z'],
            typed_assurance=['2026-10-29T05:07:41Z','2026-10-29T05:07:41Z'],
            extended_search_cancellation_upper_bound='2026-10-29T05:08:03Z'),
        execution_outcomes=dict(exact_controls_v1=dict(observed_exit=1,reason='reviewer negative-control design error; actual proof checks pass; v2 additive correction retained'),
            fb3_exhaustive_v1=dict(observed_exit=0),
            small_bands_v1=dict(observed_exit=0,accepted_as_evidence=False,reason='reviewer array-bound bug; only corrected v2 counts used'),
            small_bands_v2=dict(observed_exit=0),
            mutation_controls_v2=dict(observed_exit=0),
            assurance_v1=dict(complete_receipt_created=True,separate_python_wait_status_persisted=False),
            square_only_searches_length20=dict(observed_exit=3,conclusion='NOT_FOUND_WITHIN_SEARCH_BOUNDS; no universal conclusion'),
            square_only_searches_length24=dict(tool_status='cancelled',jobs=['bg_1134','bg_1135'],accepted_as_evidence=False,conclusion='INCONCLUSIVE')),
        final_disposition=dict(corrected_identity_equivalence='VERIFIED_WITH_EXPLICIT_CLASSICAL_IMPORT',
            fatal=0,major=0,historical_minor=1,historical_minor_repaired_by_frozen_erratum=True,
            same_harness_only=True,independent_family=False,human=False,kernel=False,novelty=False,
            output_directory_compliance=False,author_code_imported_or_executed=False),
        inventory_self_hash='not embedded recursively; printed after exclusive creation')
    with dest.open('x') as f:
        json.dump(record,f,indent=2)
        f.write('\n')
    print(json.dumps(dict(clock_after_inventory=clock(),inventory=meta(dest),review=meta(review)),indent=2))
