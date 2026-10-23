#!/usr/bin/env python3
"""Creation-only v3 parent review pack. Metadata only; no native child, controls or production.
Diff authority is the immutable v2 pack; the local supervisor adapter is diffed against the unchanged shared r3.
"""
import argparse
import difflib
import hashlib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract_v3 as C
import m2_supervised_runtime_v3 as R

L = C.LANE
V2 = L/'cycle2/full-k1-v2-sourcepack-20261018T062146.json'
V2_SHA = '22f435a1b6a4907f2e377d31df0e93b2a77f5593db3c7bc08a2384cc0de0d3b5'
UPSTREAM = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code/supervise_r3.py')
UPSTREAM_SHA = '0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d'
RENAMED = {'src/m2_ms09_evidence.py':'src/m2_ms09_evidence_v3.py','src/m2_ms09_contract.py':'src/m2_ms09_contract_v3.py',
    'src/freeze_m2_ms09_k1.py':'src/freeze_m2_ms09_k1_v3.py','src/run_m2_ms09_k1.py':'src/run_m2_ms09_k1_v3.py',
    'src/final_m2_ms09_inventory.py':'src/final_m2_ms09_inventory_v3.py','src/m2_supervised_runtime_v2.py':'src/m2_supervised_runtime_v3.py',
    'src/m2_native_staged_v2.py':'src/m2_native_staged_v3.py','src/m2_item_owner_v2.py':'src/m2_item_owner_v3.py',
    'src/m2_supervised_evidence_v2.py':'src/m2_supervised_evidence_v3.py','src/run_m2_ms06_direct_v2.py':'src/run_m2_ms06_direct_v3.py',
    'src/check_m2_ms09_k1.py':'src/check_m2_ms09_k1_v3.py'}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ms09_contract'); ap.add_argument('ms06_contract'); args = ap.parse_args()
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+4*1024**2, 'fresh metadata growth gate'
        assert R.digest(V2) == V2_SHA and R.digest(UPSTREAM) == UPSTREAM_SHA
        old = json.loads(V2.read_bytes())['source_files']
        m9,m6 = json.loads(Path(args.ms09_contract).read_bytes()),json.loads(Path(args.ms06_contract).read_bytes())
        assert m9['source_sha256'] == m6['source_sha256'] and set(m9['source_sha256']) == set(C.SOURCE_FILES)
        sources = {}
        for rel,h in m9['source_sha256'].items():
            raw = (L/rel).read_bytes(); assert hashlib.sha256(raw).hexdigest() == h
            sources[rel] = {'sha256':h,'bytes':len(raw),'content':raw.decode()}
        pieces = []
        for rel in sorted(sources):
            before = next((k for k,v in RENAMED.items() if v == rel),rel)
            if rel == 'src/supervise_pa19_v3.py':
                a,label = UPSTREAM.read_text(),'shared-r3/'+UPSTREAM.name
            elif before in old:
                assert hashlib.sha256(old[before]['content'].encode()).hexdigest() == old[before]['sha256']
                a,label = old[before]['content'],'v2/'+before
            else: continue
            pieces.extend(difflib.unified_diff(a.splitlines(True),sources[rel]['content'].splitlines(True),fromfile=label,tofile='v3/'+rel))
        stamp = time.strftime('%Y%m%dT%H%M%S')
        delta = L/'cycle2'/('full-k1-v3-delta-'+stamp+'.diff')
        with delta.open('x') as f: f.write(''.join(pieces))
        pack = {'schema':'PA19-FULL-K1-SOURCEPACK-v3','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT SOURCE REVIEW; native controls and production HOLD; controls NOT_RUN',
            'supersedes':{'path':str(V2.relative_to(L)),'sha256':V2_SHA},
            'v2_hostile_review':{'path':'institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v2-source-codex-v1.note.md',
                                 'sha256':'31f26091b56542f22fb9530e11bc18641faa9da7c7e466a4c3f92379851c3dcf'},
            'parent_v3_decisions':['no automatic retries','contract-only binary authority checked before every spawn',
                'supervisor safety dominates worker outcome','explicit retained-Popen reaping plus group quiescence','cached exact census amendment',
                'scientific UNKNOWN with separate persistent integrity veto','corrected controls'],
            'accounting_residual':m9['resource_policy']['residual'],
            'delta':{'path':str(delta.relative_to(L)),'sha256':R.digest(delta)},'source_files':sources,
            'shared_supervisor_unchanged':{'path':str(UPSTREAM),'sha256':UPSTREAM_SHA},
            'local_supervisor_adapter':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
            'contracts':[{'role':role,'path':str(Path(p).relative_to(L)),'sha256':R.digest(p)} for role,p in
                         [('ms09-full-cover-and14-validation',args.ms09_contract),('ms06-initial-direct-only',args.ms06_contract)]],
            'controls':{'source':'src/check_m2_ms09_k1_v3.py','sha256':sources['src/check_m2_ms09_k1_v3.py']['sha256'],
                        'observed_receipt':None,'production_coverage':False},
            'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('full-k1-v3-sourcepack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(delta,R.digest(delta),flush=True)
        print(json.dumps(pack['contracts'],indent=1),flush=True)


if __name__ == '__main__':
    main()
