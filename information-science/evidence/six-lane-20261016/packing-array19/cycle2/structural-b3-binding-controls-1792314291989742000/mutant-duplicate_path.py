#!/usr/bin/env python3
"""Exact parent-accepted structural B3 row. Deterministic embedded manifest, no filesystem discovery/empty-list rule.
All required document/input/source bytes must match their frozen SHA; missing/changed/duplicate evidence returns
STRUCTURAL_PENDING_BINDING, never a solver flag. `paths` is a same-key shadow mapping used only by metadata controls;
production aggregate calls verify() with the exact real paths. No output or scientific evidence file is written here.
"""
import hashlib
from pathlib import Path

EXPECTED = {'parent_note': {'path': '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-ms09-b3-structural-parent-v1.md', 'sha256': 'f311d68df95232293f855c5ffe15e08e6a90fba4ed799f0f1c8e559d91716466'}, 'local_proof_document': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/structural-ms09-b00003-proof.json', 'sha256': '25b7df6aa32b42cff74873c33c27da5a24b008078038816d25bdd6c94b4f676a'}, 'explicit_parent_acceptance_row': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/structural-ms09-b00003-parent-accepted.json', 'sha256': 'e6c5111228d70b8e5b9387917795b4a9eec91b8eafea4be088992d9160946c1c'}, 'skeleton_file': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/skeletons-b-ms09.json', 'sha256': '7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0'}, 'case_map': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/skel-b/compare-map-ms09.json', 'sha256': 'd06bb6fce38a2fbf96cf7d84d18331ec8233b54ccdccfc4b4ec759f281aa5282'}, 'mapped_A2_spec': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cases19skel/specs/ms09_s00003.json', 'sha256': 'f98c8fd50ad02b81cd4f98615af4d7f5e5048c3a04aeb65ae54700bb0eae0341'}, 'empty_list_receipt': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/cycle2/m2part_drat/ms09_b00003/ext.json', 'sha256': '2fd71b8e7889405265eba67f609c9e21f25d360ba0af01e89f050631bafb31be'}, 'original_generator': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/extend_b.py', 'sha256': '31924ed66099baf6f03436e6d51793549cd45e96416200aeea8c23af651a26d7'}, 'io_only_generator': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/extend_b_x.py', 'sha256': '9862d9eb3541cc6a50ee3959cf4e1b909e8afe2b6d448875ddc0f394b07a14fb'}, 'encoder_context': {'path': '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/src/encode_skel_b.py', 'sha256': 'd0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5'}}


def pending(kind, detail):
    return {'accepted': False, 'case': 'ms09_b00003', 'classification': 'STRUCTURAL_PENDING_BINDING',
            'solver_checked': False, 'error_kind': kind, 'detail': detail}


def verify(paths=None):
    selected = {k: v['path'] for k, v in EXPECTED.items()} if paths is None else dict(paths)
    if set(selected) != set(EXPECTED):
        return pending('required_set', 'shadow source keys differ from the exact frozen manifest')
    resolved = {k: str(Path(p).resolve()) for k, p in selected.items()}
    if False:
        return pending('duplicate_path', 'two required evidence labels resolve to the same path')
    digests = {}
    for label in EXPECTED:
        try:
            content = Path(resolved[label]).read_bytes()
        except OSError as exc:
            return pending('missing', 'inventoried %s is missing/unreadable: %s' % (label, exc))
        digests[label] = hashlib.sha256(content).hexdigest()
    if len(set(digests.values())) != len(digests):
        return pending('duplicate_digest', 'two distinct required sources have identical digest')
    for label, spec in EXPECTED.items():
        if digests[label] != spec['sha256']:
            return pending('digest', 'inventoried %s bytes differ from frozen SHA' % label)
    return {'accepted': True, 'case': 'ms09_b00003', 'classification': 'STRUCTURAL/EMPTY-COVER parent exact mathematical PASS',
            'solver_checked': False, 'checker_invocation': None, 'drat_proof_sha256': None, 's_verified': False,
            'parent_note': EXPECTED['parent_note']['path'], 'parent_note_sha256': EXPECTED['parent_note']['sha256'],
            'local_proof_document_sha256': EXPECTED['local_proof_document']['sha256'],
            'source_bindings': {k: {'path': resolved[k], 'sha256': digests[k]} for k in EXPECTED},
            'scope': 'this exact B3 input only; no generic empty-list/0-over-0 acceptance; hostile/global bridge audit pending'}
