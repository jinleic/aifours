#!/usr/bin/env python3
"""Pre-production binding census for the frozen M2H v6_1 contract: regenerate EVERY item's ORIGINAL independent-B
formula in memory (run_m2h_v6_1.formula, the exact production constructor path) and compare bytes/SHA-256 with the
historical receipt CNF bound in the contract. No solver, checker, helper or child process; no CNF is written.
A mismatch would make production refuse that item before pin and end the chunk, so it is reported up front.
One lane token held (metadata Capacity). SIGTERM sets the cooperative cancel flag; the census then stops at an item
boundary and writes a partial receipt (status STOPPED). Output: cycle2/m2h-v6_1-binding-census-<stamp>.json (creation-only).
Usage: m2h_binding_census_v6_1.py CONTRACT SHA256
"""
import argparse
import hashlib
import json
import os
import time

import m2_ms09_contract_v6_1 as COMMON
import m2_ms09_evidence_v6_1 as E
import m2_supervised_runtime_v6_1 as R
import run_m2h_v6_1 as H

L = COMMON.LANE


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); args = ap.parse_args()
    started, t0 = time.strftime('%Y-%m-%dT%H:%M:%S%z'), time.monotonic()
    assert E.digest(args.contract) == args.sha256
    c = COMMON.read(args.contract); H.verify(c)
    skeletons = {int(k):COMMON.read(L/v['path']) for k,v in c['skeletons'].items()}
    checked, mismatches, stopped = 0, [], False
    for x in c['items']:
        if R._CANCEL[0]: stopped = True; break
        raw = H.formula(c,x,skeletons); h = hashlib.sha256(raw).hexdigest()
        if len(raw) != x['expected_cnf_bytes'] or h != x['expected_cnf_sha256']:
            mismatches.append({'id':x['id'],'expected_sha256':x['expected_cnf_sha256'],'expected_bytes':x['expected_cnf_bytes'],'got_sha256':h,'got_bytes':len(raw)})
        checked += 1
        if checked % 500 == 0: print(time.strftime('%H:%M:%S'),'checked',checked,'mismatches',len(mismatches),flush=True)
    H.verify_sources(c)
    out = {'schema':'PA19-M2H-BINDING-CENSUS-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'seconds':round(time.monotonic()-t0,1),'contract':str(os.path.relpath(os.path.abspath(args.contract),L)),'contract_sha256':args.sha256,
        'census_source_sha256':E.digest(__file__),'items':len(c['items']),'checked':checked,'matches':checked-len(mismatches),'mismatches':mismatches,
        'status':'STOPPED' if stopped else 'COMPLETE','no_cnf_written':True,'production_coverage':False,
        'scope':'formula/receipt binding only; says nothing about satisfiability'}
    dest = L/'cycle2'/('m2h-v6_1-binding-census-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f: json.dump(out,f,indent=1); f.write('\n')
    print(dest,E.digest(dest),out['status'],'checked',checked,'mismatches',len(mismatches),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
