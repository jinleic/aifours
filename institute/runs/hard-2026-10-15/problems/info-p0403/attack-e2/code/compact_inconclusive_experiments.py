"""Replace unclaimed UNKNOWN-instance caches by exact regeneration recipes.

No artifact cited by claims.json may be removed. Accepted CNFs, metadata,
proofs, tables, controls and complete enumeration outputs stay delivered.
"""
import gzip
import hashlib
import json
from pathlib import Path


data=json.loads(Path('claims.json').read_text())
load_bearing={p for c in data['claims'] for p in c['evidence']}
records=[]
for i,choice in enumerate((0,32,120,251)):
    prefix='results/slice-completion%d'%i
    run=json.loads(Path(prefix+'-search-run.json').read_text())
    assert run['status']=='UNKNOWN' and not run['proof_produced']
    regeneration='python3 code/slice_sat_experiment.py --choice %d --prefix %s --build-only'%(choice,prefix)
    for suffix in ('.cnf.gz','.encoding.json.gz'):
        path=Path(prefix+suffix)
        assert str(path) not in load_bearing
        if path.exists():
            raw=path.read_bytes(); unpacked=gzip.decompress(raw)
            records.append({'path':str(path),'compressed_bytes':len(raw),
                            'compressed_sha256':hashlib.sha256(raw).hexdigest(),
                            'uncompressed_bytes':len(unpacked),
                            'uncompressed_sha256':hashlib.sha256(unpacked).hexdigest(),
                            'regenerate_command':regeneration,'status':'unclaimed UNKNOWN cache; no negative result'})
for i in (0,3):
    prefix='results/slice-lowbit%d'%i
    run=json.loads(Path(prefix+'-search-run.json').read_text())
    assert run['status']=='UNKNOWN' and not run['proof_produced']
    regeneration='python3 code/slice_lowbit_experiment.py --base results/slice-completion%d --prefix %s --seconds 180'%(i,prefix)
    for suffix in ('.cnf.gz','.encoding.json.gz'):
        path=Path(prefix+suffix)
        assert str(path) not in load_bearing
        if path.exists():
            raw=path.read_bytes(); unpacked=gzip.decompress(raw)
            records.append({'path':str(path),'compressed_bytes':len(raw),
                            'compressed_sha256':hashlib.sha256(raw).hexdigest(),
                            'uncompressed_bytes':len(unpacked),
                            'uncompressed_sha256':hashlib.sha256(unpacked).hexdigest(),
                            'regenerate_command':regeneration,'prerequisite':'regenerate the base completion instance first',
                            'status':'unclaimed UNKNOWN cache; no negative result'})
manifest={'scope':'These are discarded caches of inconclusive experimental searches, not missing proof evidence.',
          'artifacts':records,'accepted_evidence_removed':False,
          'remaining_evidence_all_present':all(Path(p).is_file() for p in load_bearing)}
assert manifest['remaining_evidence_all_present']
Path('results/inconclusive-artifact-recipes.json').write_text(json.dumps(manifest,indent=2)+'\n')
for rec in records:
    Path(rec['path']).unlink()
print('Removed',len(records),'unclaimed regenerable UNKNOWN caches;',sum(r['compressed_bytes'] for r in records),'bytes saved.')
