#!/usr/bin/env python3
"""Fail-closed M2H (historical A2 ms01..ms08) component inventory. Counts ONLY measured-v6_3 qualified items.
A case is covered iff its direct item, or every interval of its exact complete B100 partition, is QUALIFIED.
--verify-formulas regenerates every consumed formula and compares it to the pinned bytes. Historical receipts remain
ORIGINAL-QUALIFIED only. Persistent vetoes or unknown records block final readiness. Not a global PA19 verdict.
"""
import argparse
import hashlib
import json
import time

import m2_ms09_contract_v6_3 as COMMON
import m2_ms09_evidence_v6_3 as E
import m2_supervised_runtime_v6_3 as R
import run_m2h_v6_3 as H

L = COMMON.LANE


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); ap.add_argument('--verify-formulas',action='store_true')
    args = ap.parse_args(); R.install_handlers()
    with R.Capacity(time.monotonic()+10800,metadata=True,wait_allowance=60):
        assert E.digest(args.contract) == args.sha256
        c = COMMON.read(args.contract); H.verify(c)
        skeletons = {int(k):COMMON.read(L/v['path']) for k,v in c['skeletons'].items()}
        cases,issues = {},[]
        for x in c['items']:
            q = H.inspect(c,args.sha256,x)
            if q['state'] in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN'): issues.append({'id':x['id'],'state':q['state'],'errors':q.get('errors')})
            ok = q['state'] == 'QUALIFIED'
            if ok and args.verify_formulas:
                raw = H.formula(c,x,skeletons)
                ok = len(raw) == x['expected_cnf_bytes'] and hashlib.sha256(raw).hexdigest() == x['expected_cnf_sha256']
                if not ok: issues.append({'id':x['id'],'state':'FORMULA_MISMATCH'})
            cases.setdefault((x['multiset'],x['b_index']),[]).append(ok)
        covered = sum(all(v) for v in cases.values())
        union = R.admission_union(L)
        out = {'schema':'PA19-M2H-INVENTORY-v6_3','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'contract_sha256':args.sha256,
            'cases':len(cases),'covered_cases':covered,'open_cases':len(cases)-covered,'issues':issues,'admission_union':union,
            'formula_verification_mode':args.verify_formulas,'excluded_cases_from_contract':len(c['excluded_cases']),
            'final_component_ready':bool(args.verify_formulas and covered == len(cases) and not issues and not union['persistent_vetoes']),
            'scope':'M2H component only; historical receipts never counted; not a global PA19 verdict'}
        dest = L/'cycle2'/('m2h-inventory-%s-%d.json' % (time.strftime('%Y%m%dT%H%M%S'),time.time_ns()))
        h = COMMON.publish_json(dest,out,L/'scratch/m2h-publish'/('inventory-'+str(time.time_ns())))
        print(dest,h,json.dumps({k:out[k] for k in ('cases','covered_cases','open_cases','final_component_ready')}),flush=True)


if __name__ == '__main__':
    main()
