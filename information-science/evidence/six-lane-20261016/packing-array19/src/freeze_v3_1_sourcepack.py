#!/usr/bin/env python3
"""Creation-only v3.1 review pack: exact v3->v3.1 diff plus a separately labelled rename-normalized diff.
Metadata only; no native controls/production. Authority is the immutable v3 pack.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import time
from pathlib import Path

import m2_ms09_contract_v3_1 as C
import m2_supervised_runtime_v3 as R

L = C.LANE
V3 = L/'cycle2/full-k1-v3-sourcepack-20261018T070626.json'
V3_SHA = 'cf82ed1f2a67beb356cf630ac8a827f8cec0eccb3c6c94f899233d8ff81bbca0'
RENAMED = ('m2_native_staged','m2_item_owner','m2_supervised_evidence','m2_ms09_evidence','m2_ms09_contract','freeze_m2_ms09_k1',
           'run_m2_ms09_k1','final_m2_ms09_inventory','check_m2_ms09_k1','run_m2_ms06_direct')


def normalize(text):
    for base in RENAMED: text = re.sub(r'(?<![A-Za-z0-9_])%s_v3_1(?![A-Za-z0-9_])' % base,base+'_v3',text)
    return text


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ms09_contract'); ap.add_argument('ms06_contract'); args = ap.parse_args()
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+4*1024**2, 'fresh metadata growth gate'
        assert R.digest(V3) == V3_SHA
        old = json.loads(V3.read_bytes())['source_files']
        m9,m6 = json.loads(Path(args.ms09_contract).read_bytes()),json.loads(Path(args.ms06_contract).read_bytes())
        assert m9['source_sha256'] == m6['source_sha256'] and set(m9['source_sha256']) == set(C.SOURCE_FILES)
        sources,exact,normalized = {},[],[]
        for rel,h in sorted(m9['source_sha256'].items()):
            raw = (L/rel).read_bytes(); assert hashlib.sha256(raw).hexdigest() == h
            sources[rel] = {'sha256':h,'bytes':len(raw),'content':raw.decode()}
            before = rel.replace('_v3_1.py','_v3.py')
            assert before in old, ('v3 authority missing',before)
            a = old[before]['content']; assert hashlib.sha256(a.encode()).hexdigest() == old[before]['sha256']
            b = sources[rel]['content']
            exact.extend(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='v3/'+before,tofile='v3.1/'+rel))
            normalized.extend(difflib.unified_diff(a.splitlines(True),normalize(b).splitlines(True),fromfile='v3/'+before,tofile='v3.1-renames-normalized/'+rel))
        stamp = time.strftime('%Y%m%dT%H%M%S')
        paths = {}
        for label,pieces in (('exact',exact),('rename-normalized',normalized)):
            p = L/'cycle2'/('full-k1-v3_1-%s-delta-%s.diff' % (label,stamp))
            with p.open('x') as f: f.write(''.join(pieces))
            paths[label] = {'path':str(p.relative_to(L)),'sha256':R.digest(p)}
        pack = {'schema':'PA19-FULL-K1-SOURCEPACK-v3.1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR EXTENDED v3 SOURCE REVIEW; native controls and production HOLD; controls NOT_RUN',
            'supersedes':{'path':str(V3.relative_to(L)),'sha256':V3_SHA},
            'parent_v3_1_rules':['pre-construction refusal: unattempted, no record/HALT, claim retired','pre-worker refusal after pin/job: retire own pin/job/claim, no record/HALT',
                'started group supervisor safety trip: UNKNOWN + persistent HALT','worker solver/checker admission refusal: recorded UNKNOWN, chunk ends, no persistent HALT'],
            'deltas':paths,'source_files':sources,'unchanged_runtime':{'path':'src/m2_supervised_runtime_v3.py','sha256':sources['src/m2_supervised_runtime_v3.py']['sha256']},
            'local_supervisor_adapter':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
            'contracts':[{'role':role,'path':str(Path(p).relative_to(L)),'sha256':R.digest(p)} for role,p in
                         [('ms09-full-cover-and14-validation',args.ms09_contract),('ms06-initial-direct-only',args.ms06_contract)]],
            'controls':{'source':'src/check_m2_ms09_k1_v3_1.py','sha256':sources['src/check_m2_ms09_k1_v3_1.py']['sha256'],
                        'observed_receipt':None,'production_coverage':False},
            'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('full-k1-v3_1-sourcepack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(json.dumps({'deltas':paths,'contracts':pack['contracts']},indent=1),flush=True)


if __name__ == '__main__':
    main()
