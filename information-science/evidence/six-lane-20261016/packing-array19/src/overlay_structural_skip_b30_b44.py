#!/usr/bin/env python3
"""Recorded skip overlay for parent-ACCEPTED structural exclusion of ms09 b30/b44 under the frozen v6 runner.
Creates the runner's own exclusive claim files for exactly those 35 intervals BEFORE production, so the unchanged
runner treats them as owned elsewhere and never spends native time on them. The frozen contract is not edited;
the v6 inventory will still show these intervals uncovered until a final reader consumes the parent verdict.
Creation-only claims and receipt; refuses if any claim/new record already exists.
"""
import hashlib
import json
import os
import time
from pathlib import Path

import m2_ms09_contract_v6 as C

L = C.LANE
CONTRACT = L/'cycle2/m2-ms09-k1-v6-contract-20261018T075542.json'
CONTRACT_SHA = '072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8'
VERDICT = Path('/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-b30-b44-parent-verdict-v1.md')
VERDICT_SHA = '0e56374c3967ef5c1e3425804ce7eb5c89bd0233d36d1240d8e417db8c8d5d1e'
CANDIDATE_SHA = '04cdca2316d5b3b9e38ad8189409929d0b25390ea2b44a1a528c9e570302fbba'


def main():
    assert C.E.digest(CONTRACT) == CONTRACT_SHA and C.E.digest(VERDICT) == VERDICT_SHA
    c = json.loads(CONTRACT.read_bytes())
    tasks = [it for ca in c['cases'] if ca['b_index'] in (30,44) for it in ca['intervals']]
    assert len(tasks) == 35 and sum(it['indices'][1]-it['indices'][0]+1 for it in tasks) == 3405
    assert all(it['id'] in c['pending_order'] for it in tasks)
    for it in tasks:
        assert not (L/it['claim']).exists() and not (L/it['new_record']).exists(), it['id']
    stamp = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    rows = []
    for it in tasks:
        line = ('overlay %s %s %s parent-ACCEPTED structural exclusion verdict %s candidate %s; no native attempt\n'
                % (stamp,CONTRACT_SHA,it['id'],VERDICT_SHA,CANDIDATE_SHA)).encode()
        fd = os.open(L/it['claim'],os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o644)
        try: os.write(fd,line)
        finally: os.close(fd)
        rows.append({'id':it['id'],'claim':it['claim'],'claim_sha256':hashlib.sha256(line).hexdigest()})
    receipt = {'schema':'PA19-STRUCTURAL-SKIP-OVERLAY-v1','host_clock':stamp,'contract':str(CONTRACT.relative_to(L)),'contract_sha256':CONTRACT_SHA,
        'parent_verdict':{'path':str(VERDICT),'sha256':VERDICT_SHA},'candidate_sha256':CANDIDATE_SHA,'cases':[30,44],
        'intervals':35,'placements':3405,'claims':rows,'frozen_contract_unchanged':True,
        'scope':'operational skip only; mathematical acceptance is the parent verdict, not a solver result'}
    dest = L/'cycle2'/('structural-skip-overlay-b30-b44-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f: json.dump(receipt,f,indent=1)
    print(dest,C.E.digest(dest),flush=True)


if __name__ == '__main__':
    main()
