#!/usr/bin/env python3
"""Creation-only v6 review pack: exact v5->v6 diff and a separately labelled rename-normalized diff.
v5 remains intact. Metadata only; no native controls/production.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import time
from pathlib import Path

import m2_ms09_contract_v6 as C
import m2_supervised_runtime_v6 as R

L = C.LANE
V5 = L/'cycle2/full-k1-v5-sourcepack-20261018T074247.json'
V5_SHA = '34b832d025ca59f4e2921e5065765dd28a2d7318b55fe0a569b93ae27957f9dd'
RENAMED = ('m2_supervised_runtime','m2_native_staged','m2_item_owner','m2_supervised_evidence','m2_ms09_evidence','m2_ms09_contract',
           'freeze_m2_ms09_k1','run_m2_ms09_k1','final_m2_ms09_inventory','check_m2_ms09_k1','run_m2_ms06_direct')


def normalize(text):
    for base in RENAMED: text = re.sub(r'(?<![A-Za-z0-9_])%s_v6(?![A-Za-z0-9_])' % base,base+'_v5',text)
    return text


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('ms09_contract'); ap.add_argument('ms06_contract'); args = ap.parse_args()
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+4*1024**2, 'fresh metadata growth gate'
        assert R.digest(V5) == V5_SHA
        old = json.loads(V5.read_bytes())['source_files']
        m9,m6 = json.loads(Path(args.ms09_contract).read_bytes()),json.loads(Path(args.ms06_contract).read_bytes())
        assert m9['source_sha256'] == m6['source_sha256'] and set(m9['source_sha256']) == set(C.SOURCE_FILES)
        sources,exact,normalized = {},[],[]
        for rel,h in sorted(m9['source_sha256'].items()):
            raw = (L/rel).read_bytes(); assert hashlib.sha256(raw).hexdigest() == h
            sources[rel] = {'sha256':h,'bytes':len(raw),'content':raw.decode()}
            before = rel.replace('_v6.py','_v5.py')
            assert before in old, ('v5 authority missing',before)
            a = old[before]['content']; assert hashlib.sha256(a.encode()).hexdigest() == old[before]['sha256']
            b = sources[rel]['content']
            exact.extend(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='v5/'+before,tofile='v6/'+rel))
            normalized.extend(difflib.unified_diff(a.splitlines(True),normalize(b).splitlines(True),fromfile='v5/'+before,tofile='v6-renames-normalized/'+rel))
        stamp = time.strftime('%Y%m%dT%H%M%S')
        deltas = {}
        for label,pieces in (('exact',exact),('rename-normalized',normalized)):
            p = L/'cycle2'/('full-k1-v6-%s-delta-%s.diff' % (label,stamp))
            with p.open('x') as f: f.write(''.join(pieces))
            deltas[label] = {'path':str(p.relative_to(L)),'sha256':R.digest(p)}
        pack = {'schema':'PA19-FULL-K1-SOURCEPACK-v6','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'status':'FROZEN FOR PARENT RE-REVIEW; native controls and production HOLD; controls NOT_RUN',
            'supersedes':{'path':str(V5.relative_to(L)),'sha256':V5_SHA},
            'v5_review':{'path':'institute/runs/six-lane-2026-10-16/review/pa19-full-k1-v5-source-codex-v1.note.md'},
            'folded_changes':['every started CNF feeder is settled with bounded joins after stop and before observations freeze; unsettled feeder = lifecycle INVALID',
                'synchronized delayed-publication control: real solver write failure published after the cap-induced bounded-exit stop yields persistent INVALID with clean supervision',
                'exceptional native controls assert exact injected reasons, injection markers and supervisor cleanup cause'],
            'deltas':deltas,'source_files':sources,
            'local_supervisor_adapter':{'path':str(R.SUP_PATH),'sha256':R.SUP_SHA},
            'contracts':[{'role':role,'path':str(Path(p).relative_to(L)),'sha256':R.digest(p)} for role,p in
                         [('ms09-full-cover-and14-validation',args.ms09_contract),('ms06-initial-direct-only',args.ms06_contract)]],
            'controls':{'source':'src/check_m2_ms09_k1_v6.py','sha256':sources['src/check_m2_ms09_k1_v6.py']['sha256'],
                        'observed_receipt':None,'production_coverage':False},
            'generator_sha256':R.digest(__file__)}
        dest = L/'cycle2'/('full-k1-v6-sourcepack-'+stamp+'.json')
        with dest.open('x') as f: json.dump(pack,f,indent=1)
        print(dest,R.digest(dest),flush=True); print(json.dumps({'deltas':deltas,'contracts':pack['contracts']},indent=1),flush=True)


if __name__ == '__main__':
    main()
