#!/usr/bin/env python3
"""Fresh post-binding admission evidence for the frozen M2H v6_2 contract (parent Codex v2 requirement), metadata only.
Under one lane token: verify the contract, scan the shared veto/STOP registry, take a FRESH exact allocated-data census,
build the same lease the v6_2 owner builds, and evaluate the real v6_2 full_gate for the 'construct' and 'worker'
phases. Nothing is constructed, pinned, claimed or spawned; no solver/checker. The receipt records the census bytes
against the whole-plan reservation (usage must be <= DATA_CAP - bound - margin), floor, RSS headroom, binary identities,
census TTL, COUNT, policy cutoff and the 2400 s budget fit. Usage: m2h_gate_preview_v6_2.py CONTRACT SHA256
"""
import argparse
import json
import os
import time

import m2_ms09_contract_v6_2 as COMMON
import m2_ms09_evidence_v6_2 as E
import m2_supervised_runtime_v6_2 as R
import run_m2h_v6_2 as H

L = COMMON.LANE


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); args = ap.parse_args()
    assert E.digest(args.contract) == args.sha256
    c = COMMON.read(args.contract); H.verify(c)
    cut,end,cleanup = H.epochs(c)
    deadline = min(time.monotonic()+10800,time.monotonic()+(end-time.time())-cleanup)
    union = R.admission_union(L)
    bound = c['resource_policy']['whole_plan_remaining_bound_bytes']
    reference = R.create_census(); census = R.census_for_gate(reference)
    now = time.monotonic()
    lease = {'owner_pid':os.getpid(),'projected_growth_bytes':R.ITEM_GROWTH,'census_reference':reference,'whole_plan_remaining_bound_bytes':bound,
             'force_census_refresh':False,'binary_authority':c['binary_authority'],'group_rss_cap_bytes':R.GROUP_RSS_CAP,'busy_units':2,
             'lane_busy_ceiling':4,'chunk_deadline_monotonic':deadline,'item_deadline_monotonic':now+2400,'admission_cutoff_epoch':cut}
    gates = {phase:R.full_gate(dict(lease),phase) for phase in ('construct','worker')}
    out = {'schema':'PA19-M2H-V6_2-GATE-PREVIEW-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'contract_sha256':args.sha256,
        'admission_union':union,'census':{'reference':reference,'current_data_upper_bytes':census['current_data_upper_bytes'],'age_seconds':census['age_seconds']},
        'whole_plan_remaining_bound_bytes':bound,'usage_limit_bytes':R.DATA_CAP-bound-R.OTHER_WRITER_MARGIN,
        'usage_within_reservation':census['current_data_upper_bytes'] <= R.DATA_CAP-bound-R.OTHER_WRITER_MARGIN,
        'deadline_remaining_seconds':round(deadline-time.monotonic(),1),'budget_2400_fits':deadline-time.monotonic() >= 2400,
        'cutoff_remaining_seconds':round(cut-time.time(),1),
        'gates':{k:{kk:g.get(kk) for kk in ('admitted','errors','count','free_bytes','required_free_bytes','rss','binary_observations',
                                             'at_epoch','admission_cutoff_epoch')} for k,g in gates.items()},
        'nothing_constructed_pinned_claimed_or_spawned':True,'production_coverage':False}
    dest = L/'cycle2'/('m2h-v6_2-gate-preview-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    h = COMMON.publish_json(dest,out,L/'scratch/m2h-publish'/('gate-preview-'+str(time.time_ns())))
    print(dest,h,json.dumps({k:out[k] for k in ('usage_within_reservation','budget_2400_fits','cutoff_remaining_seconds')}),
          {k:(g['admitted'],g['errors']) for k,g in gates.items()},flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
