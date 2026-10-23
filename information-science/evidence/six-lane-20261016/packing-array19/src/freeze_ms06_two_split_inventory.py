#!/usr/bin/env python3
"""Phase1 only for parent-approved M2 B6:68 and B6:73. Run behind with_token15.
No placement enumeration or solve. Freeze exact direct-CNF/source/skeleton bindings, the complete finite orbit
universe, a rigorous numeric output upper bound, and the B100 partition rule. Exact raw/orbit counts/list SHA and
explicit batch intervals must be pinned AFTER complete enumeration and BEFORE any batch solve. No partial lists.
DP is the unchanged per-membership-class bound from freeze_ms09_split_inventory, with only the scope assertion
retargeted to c0=6, two P1 columns, leave1. It omits inter-class incompatibilities, so upper >= raw >= orbit count.
"""
import hashlib
import json
import os
import time
from collections import Counter

import lane_new_data_accounting as ACCOUNT

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, 'cycle2')
P0 = [4, 3, 3, 3, 3, 3]
CNFS = {68:'3454e418ba61aff0220134779f3acaa7a7e9b7eef466ce9a94b53531d2a49c1a',
        73:'ea2d01da1fcb385085af10ffb17bf25fff0c4c30ee7b95f41a83ff5ecc34f67b'}


def digest(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def upper_count(data, index):
    sk = data['skeletons'][index]
    c0, leave = data['c0'], data['L']
    special = [p for p in data['profiles'] if list(p) != P0]
    assert c0 == 6 and leave == 1 and len(special) == 2 and all(list(p) == [4,4,3,3,3,2] for p in special)
    ns = len(special)
    types = [tuple(t) for t in sk['types']]
    degrees = [sum(v in t for t in types) for v in range(c0)]
    members = list(types)
    for v in range(c0):
        members += [(v,)] * (4 - degrees[v])
    members += [()] * sk['empty']
    assert len(members) == 19
    classes = Counter(members)

    def row_ok(t,e):
        return t + e - (ns - 1) <= 2 and t + e + (ns - 1) >= 2 - leave

    dp = {(0,0,0): 1}
    options = []
    for ms,cap in classes.items():
        per_block = 1 if ms else cap
        choices = []
        for a in range(min(per_block,cap,4) + 1):
            for b in range(min(per_block,cap-a,4) + 1):
                for p in range(min(per_block,cap-a-b,2) + 1):
                    rest = cap-a-b-p
                    if a+b and not row_ok(len(ms),1):
                        continue
                    if p and not row_ok(len(ms),-1):
                        continue
                    if rest and not row_ok(len(ms),0):
                        continue
                    choices.append((a,b,p))
        options.append({'membership':list(ms),'rows':cap,'role_count_options':len(choices)})
        nd = {}
        for (sa,sb,sp),n in dp.items():
            for a,b,p in choices:
                state = (sa+a,sb+b,sp+p)
                if state[0] <= 4 and state[1] <= 4 and state[2] <= 2:
                    nd[state] = nd.get(state,0) + n
        dp = nd
    return dp.get((4,4,2),0), options


def main():
    skpath = os.path.join(C2,'skel-b','skeletons-b-ms06.json')
    data = json.load(open(skpath))
    mapath = os.path.join(C2,'skel-b','compare-map-ms06.json')
    mapping = json.load(open(mapath))
    assert mapping['bijection'] is True
    jobs = []
    for bi in (68,73):
        rp = os.path.join(C2,'m2skel_drat','ms06_b%05d.json' % bi)
        r = json.load(open(rp))
        assert r['status'] == 'UNKNOWN' and r['solver_rc'] == 0 and r['solver_stop'] == 'self'
        assert r['cnf_sha256'] == CNFS[bi] and r['check_seconds'] == 0 and r['reader_ok'] is True
        assert '-t 300 ' in r['solver'] and r['stream_check_revision'] == 15
        ais = [ai for ai,v in enumerate(mapping['a_to_b']) if v == bi]
        assert len(ais) == 1
        tag = 'ms06_s%05d' % ais[0]
        spec = os.path.join(LANE,'cases19skel','specs',tag+'.json')
        ext = os.path.join(C2,'m2part_drat','ms06_b%05d' % bi,'ext.json')
        assert not os.path.exists(ext), 'existing list requires explicit reconciliation, never overwrite'
        ub,opts = upper_count(data,bi)
        jobs.append({'job':'6:%d' % bi,'b_index':bi,'mapped_A2_tag':tag,'mapped_A2_spec_path':os.path.relpath(spec,LANE),
          'mapped_A2_spec_sha256':digest(spec),'source_direct_record':os.path.relpath(rp,LANE),'source_direct_record_sha256':digest(rp),
          'source_cnf_sha256':r['cnf_sha256'],'source_cnf_bytes':r['cnf_bytes'],
          'source_cnf_replay':'encode_skel_b.build_v2(c0, exact types, empty, special profiles) then cnf_bytes; no new CNF copy',
          'missing_list':True,'raw_assignment_dp_upper':ub,'complete_output_upper_bytes':60*ub+65536,
          'skeleton_sha256':hashlib.sha256(json.dumps(data['skeletons'][bi],sort_keys=True).encode()).hexdigest(),
          'class_options':opts,'denominator':'ALL compatible first-P1 role-count assignments modulo full skeleton automorphisms and A/B swap; no truncation'})
    prior = []
    for bi in range(71):
        p = os.path.join(C2,'m2part_drat','ms09_b%05d' % bi,'ext.json')
        if os.path.exists(p):
            prior.append({'path':os.path.relpath(p,LANE),'sha256':digest(p)})
    assert len(prior) == 70
    source_names = ['extend_b.py','extend_b_x.py','encode_skel_b.py','run_m2_15.py','stream_check15.py',
                    'enumeration_helper_guard_v3.py','lane_new_data_accounting.py','freeze_ms06_two_split_inventory.py']
    out = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'scope':'EXACT two parent-approved M2 cases6:68 and6:73; direct UNKNOWNs retained',
      'source_sha256':{p:digest(os.path.join(LANE,'src',p)) for p in source_names},'skeleton_file_sha256':digest(skpath),
      'skeleton_file_path':os.path.relpath(skpath,LANE),'case_map_path':os.path.relpath(mapath,LANE),'case_map_sha256':digest(mapath),
      'approved_wrapper_base_v4_sha256':'a03c0c2c0a4b497e4695b90145354de40c59b51458bb9278f8751aef2b863f77',
      'actual_retargeted_wrapper':'requires separate new-source hash/delta freeze and parent source-review GO before execution',
      'jobs':jobs,'hard_lists_unchanged':prior,'whole_plan_generator_output_bound_bytes':sum(j['complete_output_upper_bytes'] for j in jobs),
      'whole_plan_receipt_margin_bytes':len(jobs)*1048576,'current_new_data_accounting':ACCOUNT.account(LANE),
      'complete_placement_universe': 'Reconstruct all19 rows by exact P0-quad memberships. For each equal-membership class exhaust every count(a,b,p) with totals4,4,2 and residual triple rows, row-budget compatibility, capacity and pairwise P0-disjointness in A/B/P. Quotient within-class row permutations by canonical row allocation and full skeleton automorphisms plus A/B swap. Every valid array maps to one retained first-P1 placement. Generator has no solution/list-count cap: any incomplete/time/memory/floor failure is UNKNOWN and yields no denominator.',
      'dp_bound_argument': 'DP enumerates all per-class role-count choices allowed by the same necessary row/capacity conditions, omitting inter-class P0 incompatibilities. Each actual raw generator assignment is one DP path; orbits<=raw<=DP upper. At most ten row IDs<=18 per placement, so JSON body<=60*upper plus65536 header margin.',
      'batch_rule': {'size':100,'exact_partition':'indices [j,min(n,j+100)-1] for j=0,100,...<n; explicit intervals/list SHA and sum of sizes=n must be pinned after complete enumeration and before any solve'},
      'numeric_denominator_state':'NOT ENUMERATED; raw/orbit counts and complete-list SHA must be pinned in phase2; no solve admitted now',
      'stop_rule':'Unknown helper/batch => exact case stays open; empty list needs its own parent structural check, never generic0/0; no native/check-budget/cap increase',
      'helper_caps':{'helper_seconds':1800,'chunk_seconds':10800,'shutdown_reserve_seconds':90,'sampled_rss_limit_bytes':5*1024**3,
                     'in_flight_floor_bytes':12000000000,'post_lock_gate':'max(12334217728,12267108864+output_bound+1048576)',
                     'lane_memory_cap_bytes':8*1024**3,'original_new_data_cap_bytes':10*1024**3,'enforced_new_data_cap_bytes':10000000000}}
    dest = os.path.join(C2,'ms06-two-split-inventory-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with open(dest,'x') as f:
        json.dump(out,f,indent=1)
    print(dest)
    print(json.dumps({'jobs':[{k:j[k] for k in ('job','raw_assignment_dp_upper','complete_output_upper_bytes')} for j in jobs],
                      'whole_generator_bound':out['whole_plan_generator_output_bound_bytes'],'unchanged_prior_lists':len(prior)}))


if __name__ == '__main__':
    main()
