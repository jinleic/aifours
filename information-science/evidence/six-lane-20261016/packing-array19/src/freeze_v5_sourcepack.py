#!/usr/bin/env python3
"""Creation-only v5 review pack: exact v4->v5 diff and a separately labelled rename-normalized diff.
v4 remains intact. Metadata only; no native controls/production.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import time
from pathlib import Path

import m2_ms09_contract_v5 as C
import m2_supervised_runtime_v5 as R

L = C.LANE
V4 = L/'cycle2/full-k1-v4-sourcepack-20261018T072429.json'
V4_SHA = 'aeb0d85cbbcbf0711d3458f8a33b862afeb3bbd795cf3902fb2ab15bab1eb064'
RENAMED = ('m2_supervised_runtime','m2_native_staged','m2_item_owner','m2_supervised_evidence','m2_ms09_evidence','m2_ms09_contract',
           'freeze_m2_ms09_k1','run_m2_ms09_k1','final_m2_ms09_inventory','check_m2_ms09_k1','run_m2_ms06_direct')


def normalize(text):
    for base in RENAMED: text = re.sub(r'(?<![A-Za-z0-9_])%s_v5(?![A-Za-z0-9_])' % base,base+'_v4',text)
    return text


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ms09_contract'); ap.add_argument('ms06_contract'); args = ap.parse_args()
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+4*1024**2, 'fresh metadata growth gate'
        assert R.digest(V4) == V4_SHA
        old = json.loads(V4.read_bytes())['source_files']
        m9,m6 = json.loads(Path(args.ms09_contract).read_bytes()),json.loads(Path(args.ms06_contract).read_bytes())
        assert m9['source_sha256'] == m6['source_sha256'] and set(m9['source_sha256']) == set(C.SOURCE_FILES)
        sources,exact,normalized = {},[],[]
        for rel,h in sorted(m9['source_sha256'].items()):
            raw = (L/rel).read_bytes(); assert hashlib.sha256(raw).hexdigest() == h
            sources[rel] = {'sha256':h,'bytes':len(raw),'content':raw.decode()}
            before = rel.replace('_v5.py','_v4.py')
            assert before in old, ('v4 authority missing',before)
            a = old[before]['content']; assert hashlib.sha256(a.encode()).hexdigest() == old[before]['sha256']
            b = sources[rel]['content']
            exact.extend(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='v4/'+before,tofile='v5/'+rel))
            normalized.extend(difflib.unified_diff(a.splitlines(True),normalize(b).splitlines(True),fromfile='v4/'+before,tofile='v5-renames-normalized/'+rel))
        stamp = time.strftime('%Y%m%dT%H%M%S')
        deltas = {}
        for label,pieces in (('exact',exact),('rename-normalized',normalized)):
            p = L/'cycle2'/('full-k1-v5-%s-delta-%s.diff' % (label,stamp))
            with p.open('x') as f: f.write(''.join(pieces))
            deltas[label] = {'path':str(p.relative_to(L)),'sha256':R.digest(p)}
        pack = {'schema':'PA19-FULL-K1-SOURCEPACK-v5','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT RE-REVIEW; native controls and production HOLD; controls NOT_RUN',
            'supersedes':{'path':str(V4.relative_to(L)),'sha256':V4_SHA},
            'v4_review':{'path':'institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v4-source-codex-v1.note.md'},
            'folded_changes':['real CNF open/write/close failures classified before cap/bounded outcomes with bound-induced cancellation provenance',
                'no-retry control asserts the exact timestamped archived claim and unchanged first UNKNOWN','change-counted targeted mutants incl. checker-feed enforcement removal',
                'specific-cause assertions for gates, post-wait, natives and safety-trip','full classified admission union in inventory/init receipts; resource-stop init class'],'deltas':deltas,'source_files':sources,
            'local_supervisor_adapter':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
            'contracts':[{'role':role,'path':str(Path(p).relative_to(L)),'sha256':R.digest(p)} for role,p in
                         [('ms09-full-cover-and14-validation',args.ms09_contract),('ms06-initial-direct-only',args.ms06_contract)]],
            'controls':{'source':'src/check_m2_ms09_k1_v5.py','sha256':sources['src/check_m2_ms09_k1_v5.py']['sha256'],
                        'observed_receipt':None,'production_coverage':False},
            'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('full-k1-v5-sourcepack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(json.dumps({'deltas':deltas,'contracts':pack['contracts']},indent=1),flush=True)


if __name__ == '__main__':
    main()
