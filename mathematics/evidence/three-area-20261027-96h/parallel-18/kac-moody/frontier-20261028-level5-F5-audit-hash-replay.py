#!/usr/bin/env python3
"""Replay the named F5 audit manifest SHA/LF/byte bindings only.

No mathematical proof, certificate computation, atomic snapshot, B4 finding
resolution, or parent adoption is inferred.
"""
import hashlib
import json
from pathlib import Path
REPO=Path('/Users/jinleic/repos/aifours')
ROOT=REPO/'mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody'


def main():
    manifest=ROOT/'frontier-20261028-level5-F5-all-new-audit-manifest-v1.json'
    digest=hashlib.sha256(manifest.read_bytes()).hexdigest();assert digest=='2467097afa3a04ce228dc4230e853214a72dbcc0d3e92de9b41b8e3530a66eb1'
    J=json.loads(manifest.read_bytes());assert J['artifact_count']==len(J['artifacts'])==188
    keys=set()
    for item in J['artifacts']:
        path=(REPO/item['path']).resolve();assert path.is_relative_to(REPO) and item['path'] not in keys;keys.add(item['path'])
        raw=path.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==item['sha256'] and len(raw)==item['bytes'] and raw.count(b'\n')==item['LF'],item['path']
    supp=json.loads((ROOT/'frontier-20261028-level5-F5-all-new-audit-manifest-source-supplement-v1.json').read_bytes())
    for item in supp['sources']:
        path=(REPO/item['path']).resolve();assert path.is_relative_to(REPO)
        raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256'] and len(raw)==item['bytes'] and raw.count(b'\n')==item['LF'],item['path']
    bounded=ROOT/'frontier-20261028-levi-level1-check-results-v1.json';raw=bounded.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='a526e5b0682048d1f27330faf5f6367950eee0acc35788d76c98dad5e6e0dfa6'
    result={'manifest_sha256':digest,'manifest_unique_files_checked':len(keys),'transitive_source_supplement_files_checked':len(supp['sources']),
            'level_one_bounded_result_hash_checked':True,'all_sha_lf_bytes_match':True,
            'status':'PASS_SEQUENTIAL_CURRENT_FILE_BINDINGS',
            'scope':'sequential post-metadata hash check only; not atomic with metadata execution, not proof/code replay/B4 or F5 adoption'}
    out=ROOT/'frontier-20261028-level5-F5-audit-hash-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS sequential SHA/LF/bytes: 188 manifest, four transitive sources, one bounded-result file;',out.name,flush=True)

if __name__=='__main__':main()
