#!/usr/bin/env python3
"""Bind every actual source/code/data input for the all-new-map F5 route.

This only checks file presence, hashes, LF counts and the previously generated
r1 index bindings. It is NOT a scientific review, source authentication, code
replay, acceptance or a claim that external dependencies are byte-pinned.
"""
import hashlib
import json
from pathlib import Path
REPO=Path('/Users/jinleic/repos/aifours')
OWNER=REPO/'mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody'
RUN=REPO/'institute/runs/three-area-2026-10-27-96h'


def main():
    dest=OWNER/'frontier-20261028-level5-F5-all-new-audit-manifest-v1.json'
    if dest.exists():raise FileExistsError(dest)
    files={}
    def add(path,role,expected=None):
        p=Path(path);data=p.read_bytes();digest=hashlib.sha256(data).hexdigest()
        if expected:assert digest==expected,(p,digest,expected)
        key=str(p.relative_to(REPO))
        row=files.setdefault(key,{'path':key,'sha256':digest,'bytes':len(data),'LF':data.count(b'\n'),'roles':[]})
        assert row['sha256']==digest and role not in row['roles']
        row['roles'].append(role)
    def own(name,role,expected=None):add(OWNER/name,role,expected)
    for name,expected in [
      ('frontier-20261028-fixed-levi-level1-independent-v1.md','a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a'),
      ('frontier-20261028-Levi-free-quotient-critical-reduction-v1.md','e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f')]:own(name,'shared unreviewed mathematical source',expected)
    for name,expected in [
      ('written-releases/math-3-serre-family-packet-v1.md','8b811cbc88e55b5b48bebef299f356bf10c808968c967ab2ed4aca1065cc03a6'),
      ('written-releases/math-3-positive-freeness-pbw-transcription-addendum-v1.json','21b5b074fdf6b20784ec640037aaffa8d0964f6c2aa3d7855ff955bf2873f247'),
      ('dispositions/math-3-full-cartan-radical-serre-containment-and-first-defect-parent-v1.md','08217c89602bbed5bb05447144addfb1978037ad3e4c2e57271d88b794d98be9'),
      ('dispositions/math-3-preliminary-free-lie-and-serre-transport-parent-v1.md','f08daf3e2259a563a426e8982be78a36094bb58e4d56f587b2b51f14fa8df46d')]:add(RUN/name,'named prior structural or PBW qualification input',expected)
    for name in [
      'frontier-20261028-level5-all-parameters-F5-B5-composition-candidate-v1.md',
      'frontier-20261028-level5-all-parameters-F5-B5-r1-replacement-addendum-v1.md',
      'frontier-20261028-level5-all-parameters-F5-B5-invariant-replacement-addendum-v1.md',
      'frontier-20261028-level5-r1-seven-entire-maps-candidate-v1.md',
      'frontier-20261028-level5-r1-invariant-independent-candidate-v1.md',
      'frontier-20261028-level5-r2-seven-entire-maps-candidate-v1.md',
      'frontier-20261028-level5-r3-seven-entire-maps-candidate-v1.md',
      'frontier-20261028-level5-fixed-r3-s2-seven-entire-maps-candidate-v1.md',
      'frontier-20261028-level5-invariant-full-quotient-independent-v1.md',
      'frontier-20261028-level5-64-entire-quadrant-candidate-v1.md',
      'frontier-20261028-level5-35-and-dual-entire-quadrant-candidate-v1.md',
      'frontier-20261028-level5-27-entire-quadrant-candidate-v1.md',
      'frontier-20261028-level5-10-and-dual-entire-quadrant-candidate-v1.md',
      'frontier-20261028-level5-8-entire-quadrant-candidate-v1.md']:
        own(name,'unreviewed F5 component or logical composition')
    for name in [
      'frontier-20261028-lift-exact.py','frontier-20261028-levi-level1-check.py',
      'frontier-20261028-levi-lie-engine.py','frontier-20261028-symbolic-minors.py',
      'frontier-20261028-214-independent-replay.py','frontier-20261028-levi-critical-independent-replay.py',
      'frontier-review-f18-ph7-independent-check.py',
      'frontier-20261028-level5-type-determinant.py','frontier-20261028-level5-free-type-pencil.py',
      'frontier-20261028-level5-free-type-independent-replay.py',
      'frontier-20261028-level5-35-alternate-minor-search.py',
      'frontier-20261028-level5-35-alternate-independent-replay.py',
      'frontier-20261028-level5-10-alternate-minor-search.py',
      'frontier-20261028-level5-alternate-type-minor-search.py',
      'frontier-20261028-level5-alternate-type-independent-replay.py',
      'frontier-20261028-invariant5-symbolic-minors.py','frontier-20261028-invariant5-independent-replay.py',
      'frontier-20261028-level5-r3-quotient-type-pencil.py','frontier-20261028-level5-r3-quotient-determinant.py',
      'frontier-20261028-level5-r3-alternate-minor-search.py',
      'frontier-20261028-level5-r3-quotient-independent-replay.py',
      'frontier-20261028-level5-r3-baseline-quotient-independent-replay.py',
      'frontier-20261028-level5-small-row-quotient-pencil.py','frontier-20261028-level5-small-row-quotient-determinant.py',
      'frontier-20261028-level5-small-row-quotient-independent-replay.py',
      'frontier-20261028-level5-small-row-alternate-minor-search.py',
      'frontier-20261028-level5-small-row-alternate-independent-replay.py',
      'frontier-20261028-level5-fixed-quotient-case.py','frontier-20261028-level5-fixed-quotient-independent-replay.py',
      'frontier-20261028-level5-r1-seven-map-index.py']:
        own(name,'actual current producer/replay/helper/index code')
    own('frontier-20261028-level5-r1-seven-map-index-v1.json','complete 49-artifact r1 nontrivial index','b0ae80b9caaa8d0e536ff793613f2c1c86ca5775931524eb46f53253f747b36c')
    r1=json.loads((OWNER/'frontier-20261028-level5-r1-seven-map-index-v1.json').read_text())
    assert (r1['uniform_count'],r1['fixed_count'])==(7,14)
    count=0
    for item in r1['types']:
        for artifact in item['uniform_s_ge_4']['artifacts']:
            own(artifact['path'],'r1 nontrivial actual source or determinant or replay',artifact['sha256']);count+=1
        for case in item['fixed_s2_s3']:
            for artifact in case['artifacts']:
                own(artifact['path'],'r1 nontrivial actual source or determinant or replay',artifact['sha256']);count+=1
    assert count==49
    for ab in ('22','32','23','33','43','34','44'):
        for suffix in ('quotient-pencil-v1.json','quotient-determinant-v1.json'):
            own(f'frontier-20261028-level5-r3-{ab}-{suffix}','r3 whole quotient source or initial determinant')
        if ab in ('32','33','44'):
            own(f'frontier-20261028-level5-r3-{ab}-alternate-minor-search-v1.json','r3 actual alternate determinant')
            own(f'frontier-20261028-level5-r3-{ab}-quotient-independent-replay-v1.json','r3 independent alternate replay')
        else:own(f'frontier-20261028-level5-r3-{ab}-baseline-independent-replay-v1.json','r3 independent baseline replay')
        for suffix in ('smallrow-pencil-v1.json','smallrow-determinant-v1.json'):
            own(f'frontier-20261028-level5-r2-{ab}-{suffix}','r2 whole quotient source or initial determinant')
        if ab=='23':
            own(f'frontier-20261028-level5-r2-{ab}-smallrow-alternate-v1.json','r2 actual alternate determinant')
            own(f'frontier-20261028-level5-r2-{ab}-smallrow-alternate-independent-replay-v1.json','r2 independent alternate replay')
        else:own(f'frontier-20261028-level5-r2-{ab}-smallrow-independent-replay-v1.json','r2 independent baseline replay')
        for suffix in ('v1.json','independent-replay-v1.json'):
            own(f'frontier-20261028-level5-fixed-{ab}-r3-s2-{suffix}','fixed r3s2 complete quotient or replay')
    for ab,label in [('22',None),('32','35'),('33','27'),('43','10'),('44','8')]:
        for suffix in ('pencil-v1.json','determinant-v1.json'):
            own(f'frontier-20261028-level5-free-{ab}-{suffix}','large-row full source or initial determinant')
        if label:
            own(f'frontier-20261028-level5-{label}-alternate-minor-search-v1.json','large-row alternate determinant')
            own(f'frontier-20261028-level5-{label}-alternate-independent-replay-v1.json','large-row alternate independent replay')
        else:own('frontier-20261028-level5-free-22-independent-replay-v1.json','large-row independent baseline replay')
    for name in ['frontier-20261028-invariant5-r5-s5-v1.json','frontier-20261028-invariant5-independent-replay-v1.json',
                 'frontier-20261028-level5-r1-55-smallrow-pencil-v1.json','frontier-20261028-level5-r1-55-smallrow-determinant-v1.json',
                 'frontier-20261028-level5-r1-55-smallrow-independent-replay-v1.json',
                 'frontier-20261028-level5-fixed-55-r1-s2-v1.json','frontier-20261028-level5-fixed-55-r1-s2-independent-replay-v1.json',
                 'frontier-20261028-level5-fixed-55-r1-s3-v1.json','frontier-20261028-level5-fixed-55-r1-s3-independent-replay-v1.json']:
        own(name,'actual invariant source or determinant or independent replay')
    result={'schema_version':1,'scope':'all-new-map F5 route for original A(r,s), all positive r,s; excludes optional B4 proof and old invariant theorem proofs',
            'artifact_count':len(files),'artifacts':[files[k] for k in sorted(files)],
            'source_and_code_review_pending':True,'metadata_only_not_mathematical_acceptance':True,
            'runtime_dependency':'Python 3, Fraction; SymPy 1.14.0 for independently computed invariant determinant; runtime/library bytes not pinned here',
            'limits':'No old H13/old19 authentication, no parent adoption, no all-level/arbitrary-GCM, no formal/kernel/human/independent-family/novelty claim.'}
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PINNED',len(files),'F5 audit source/code/data artifacts;',dest.name,flush=True)

if __name__=='__main__':main()
