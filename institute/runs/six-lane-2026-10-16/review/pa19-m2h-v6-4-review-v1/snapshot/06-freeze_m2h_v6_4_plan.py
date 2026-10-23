#!/usr/bin/env python3
"""Creation-only explicit-subset plan for the frozen M2H v6_4 contract. Each entry carries the contract position and the
canonical item SHA-256 (run_m2h_v6_4.item_sha256); the plan is validated with run_m2h_v6_4.plan_items, the runner's own
predicate, before it is published. Items are referenced, never copied, mutated or renumbered; denominators stay those
of the full contract. Metadata only (one lane token): no claim, pin, record or native work.
Usage: freeze_m2h_v6_4_plan.py CONTRACT SHA256 ID [ID ...]
"""
import argparse
import json
import time
from pathlib import Path

import m2_ms09_contract_v6_3 as COMMON
import m2_ms09_evidence_v6_3 as E
import m2_supervised_runtime_v6_3 as R
import run_m2h_v6_4 as H

L = COMMON.LANE


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); ap.add_argument('ids',nargs='+')
    args = ap.parse_args()
    assert E.digest(args.contract) == args.sha256
    c = COMMON.read(args.contract); H.verify(c)
    where = {x['id']:p for p,x in enumerate(c['items'])}
    missing = [i for i in args.ids if i not in where]
    assert not missing and len(set(args.ids)) == len(args.ids), ('ids must be unique contract members',missing)
    sel = sorted(args.ids,key=where.__getitem__)
    plan = {'schema':H.PLAN_SCHEMA,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            'contract_path':str(Path(args.contract).resolve().relative_to(L)),'contract_sha256':args.sha256,
            'contract_identical_to':c['identical_to_contract'],
            'items':[{'id':i,'contract_position':where[i],'item_sha256':H.item_sha256(c['items'][where[i]])} for i in sel],
            'rule':'explicit ids only: every other contract item is not attempted under this plan; items, order and denominators '
                   'remain those of the full contract; each selected item at most once; no automatic retry',
            'source_sha256':{'src/run_m2h_v6_4.py':E.digest(L/'src/run_m2h_v6_4.py'),'src/freeze_m2h_v6_4_plan.py':E.digest(Path(__file__))}}
    chosen = [x['id'] for x in H.plan_items(c,args.sha256,plan)]
    assert chosen == sel
    dest = L/'cycle2'/('m2h-v6_4-subset-plan-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    h = COMMON.publish_json(dest,plan,L/'scratch/m2h-publish'/('plan-'+str(time.time_ns())))
    print(dest,h,json.dumps([(s['id'],s['contract_position']) for s in plan['items']]),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        main()
