#!/usr/bin/env python3
"""Requested receipt-based ETA scenarios, not a completion guarantee. Run behind with_token15.
Read only the exact frozen B100 partition and hard queue. UNKNOWN attempts remain pending; no data are solved or
regenerated. Extrapolations are explicitly conditional constant-service-rate scenarios (not confidence bounds).
"""
import datetime
import hashlib
import json
import os
import statistics
import time
from pathlib import Path

import aggregate16 as AG

LANE = Path(__file__).resolve().parent.parent
C2 = LANE / 'cycle2'
PHASE = C2 / 'ms09-batch-denominators-v2-20261018T015110.json'
START = datetime.datetime.fromisoformat('2026-10-18T01:52:10-07:00')
DEADLINE = datetime.datetime.fromisoformat('2026-10-18T18:31:43-07:00')


def load(p):
    try:
        return json.loads(p.read_text())
    except FileNotFoundError:
        return None


def main():
    now = datetime.datetime.now().astimezone()
    phase = load(PHASE)
    cases, batches = [], []
    for row in phase['pending_batch_jobs']:
        mi, bi = map(int,row['job'].split(':'))
        n = row['complete_placement_denominator']
        records = []
        for lo in range(0,n,100):
            hi = min(n,lo+100)-1
            p = C2 / 'm2part_drat' / ('ms09_b%05d' % bi) / ('batch_%05d_%05d.json' % (lo,hi))
            r = load(p)
            if r is None:
                continue
            assert r.get('multiset') == mi and r.get('b_index') == bi and r.get('indices') == [lo,hi]
            rec = {'job':row['job'],'record':str(p.relative_to(LANE)),'record_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                   'placements':hi-lo+1,'indices':[lo,hi],'status':r['status'],'strict_checked':AG.certified(r),
                   'solve_seconds':r.get('solve_seconds',0),'check_seconds':r.get('check_seconds',0),
                   'encode_seconds':r.get('encode_seconds',0),'token_wait_seconds':r.get('token_wait_seconds',0),
                   'proof_bytes':r.get('drat_bytes'),'zbuf_bytes':r.get('zbuf_bytes'),
                   'solver_stop':r.get('solver_stop'),'events':r.get('events',[])}
            rec['service_seconds'] = rec['solve_seconds'] + rec['check_seconds']
            records.append(rec)
            batches.append(rec)
        good = [r for r in records if r['strict_checked']]
        attempted_n = sum(r['placements'] for r in records)
        good_n = sum(r['placements'] for r in good)
        cases.append({'job':row['job'],'placements':n,'full_batches':row['full_batch_count'],
          'written_batches':len(records),'strict_checked_batches':len(good),'strict_checked_placements':good_n,
          'unknown_or_unchecked_batches':len(records)-len(good),
          'measured_solve_seconds':sum(r['solve_seconds'] for r in records),
          'measured_check_seconds':sum(r['check_seconds'] for r in records),
          'attempted_placements':attempted_n,
          'measured_service_seconds_per_attempted_placement':sum(r['service_seconds'] for r in records)/attempted_n if attempted_n else None,
          'certified_service_seconds_per_placement':sum(r['service_seconds'] for r in good)/good_n if good_n else None})
    hard_ids = [int(line.strip().split(':')[1].split('-')[0]) for line in (C2/'m2-jobs-hard-direct.txt').read_text().splitlines() if line.strip()]
    hard = []
    for bi in hard_ids:
        p = C2/'m2skel_drat'/('ms06_b%05d.json' % bi)
        r = load(p)
        if r:
            hard.append({'job':'6:%d' % bi,'status':r['status'],'strict_checked':AG.certified(r),
                         'solve_seconds':r.get('solve_seconds',0),'check_seconds':r.get('check_seconds',0),
                         'service_seconds':r.get('solve_seconds',0)+r.get('check_seconds',0),
                         'record':str(p.relative_to(LANE)),'cnf_sha256':r.get('cnf_sha256')})
    good_b = [r for r in batches if r['strict_checked']]
    good_h = [r for r in hard if r['strict_checked']]
    remain_p = sum(c['placements']-c['strict_checked_placements'] for c in cases)
    remain_b = sum(c['full_batches']-c['strict_checked_batches'] for c in cases)
    remain_h = len(hard_ids)-len(good_h)
    scenarios = []
    if good_b and good_h:
        fast = min(good_b,key=lambda r:r['service_seconds']/r['placements'])
        slow = max(good_b,key=lambda r:r['service_seconds']/r['placements'])
        hfast = min(good_h,key=lambda r:r['service_seconds'])
        hslow = max(good_h,key=lambda r:r['service_seconds'])
        for name,b,h in [('optimistic fastest paired observed services',fast,hfast),('pessimistic slowest paired observed services',slow,hslow)]:
            solve = remain_p*b['solve_seconds']/b['placements'] + remain_h*h['solve_seconds']
            check = remain_p*b['check_seconds']/b['placements'] + remain_h*h['check_seconds']
            ideal = max((solve+check)/2,check)
            serial = solve+check
            scenarios.append({'scenario':name,'ms09_reference_record':b['record'],'ms09_reference_placements':b['placements'],
              'ms09_solve_seconds_per_placement':b['solve_seconds']/b['placements'],
              'ms09_check_seconds_per_placement':b['check_seconds']/b['placements'],
              'ms06_reference_record':h['record'],'ms06_reference_service_seconds':h['service_seconds'],
              'predicted_solver_work_seconds':solve,'predicted_checker_work_seconds':check,
              'ideal_COUNT2_serial_checker_lower_bound_hours':ideal/3600,
              'fully_serialized_same_service_scenario_hours':serial/3600,
              'ideal_finish_host':(now+datetime.timedelta(seconds=ideal)).isoformat(),
              'serial_finish_host':(now+datetime.timedelta(seconds=serial)).isoformat(),
              'fits_deadline_even_at_ideal':ideal <= (DEADLINE-now).total_seconds()})
    totals = {'frozen_ms09_pending_cases':len(cases),'frozen_ms09_placements':sum(c['placements'] for c in cases),
      'frozen_ms09_batches':sum(c['full_batches'] for c in cases),'written_batches_since_015210':len(batches),
      'strict_checked_batches':len(good_b),'strict_checked_placements':sum(r['placements'] for r in good_b),
      'unknown_or_unchecked_batches':len(batches)-len(good_b),'remaining_uncertified_ms09_batches':remain_b,
      'remaining_uncertified_ms09_placements':remain_p,'written_ms09_solve_seconds':sum(r['solve_seconds'] for r in batches),
      'written_ms09_check_seconds':sum(r['check_seconds'] for r in batches),
      'hard_ms06_jobs':len(hard_ids),'hard_ms06_written':len(hard),'hard_ms06_strict_checked':len(good_h),
      'hard_ms06_unknown_or_unchecked':len(hard)-len(good_h),'remaining_unresolved_ms06_cases':remain_h,
      'wall_elapsed_since_015210_seconds':(now-START).total_seconds(),'deadline_remaining_hours':(DEADLINE-now).total_seconds()/3600}
    result = {'host_clock':now.isoformat(),'deadline':DEADLINE.isoformat(),'phase_sha256':hashlib.sha256(PHASE.read_bytes()).hexdigest(),
      'totals':totals,'measured_ms09_batches':batches,'ms09_cases_ordered_by_placements':sorted(cases,key=lambda c:(c['placements'],c['job'])),
      'measured_ms06_hard_records':hard,'constant_service_scenarios':scenarios,
      'limitations':['These are observed-service extrapolation scenarios, NOT statistical confidence intervals or guaranteed ETAs.',
      'Fastest/slowest samples may not represent unmeasured skeletons. The optimistic capacity bound assumes perfect scheduling with two tokens and one serial BigLock checker; actual wait/build/compression overhead can only add time.',
      'A fully serialized scenario is a feasible conservative schedule ONLY if future services match its assumed measured rate; not an unconditional upper bound.',
      'No finite certification ETA exists under current direct GO for native UNKNOWN cases: they remain open and require the separately approved complete-cover route.',
      'The two approved ms06 split denominators are not yet enumerated; their helper/batch cost is excluded, so even the optimistic figure is incomplete for total certification.',
      'No M1 timing is treated as an observed M2 cost. The README 2.7s/100 benchmark maps ms09_s00001 to B9, not B0.']}
    stamp = now.strftime('%Y%m%dT%H%M%S')
    dest = C2/('m2-critical-path-'+stamp+'.json')
    with dest.open('x') as f:
        json.dump(result,f,indent=1)
    table = C2/('m2-ms09-size-costs-'+stamp+'.tsv')
    with table.open('x') as f:
        f.write('job\tplacements\tfull_B100_batches\tchecked_batches\twritten_batches\tmeasured_solve_s\tmeasured_check_s\tservice_s_per_attempted_placement\tcertified_service_s_per_placement\n')
        for c in result['ms09_cases_ordered_by_placements']:
            vals=[c[k] for k in ('job','placements','full_batches','strict_checked_batches','written_batches','measured_solve_seconds','measured_check_seconds','measured_service_seconds_per_attempted_placement','certified_service_seconds_per_placement')]
            f.write('\t'.join('-' if v is None else str(v) for v in vals)+'\n')
    print(dest)
    print(table)
    print(json.dumps({'totals':totals,'scenarios':scenarios,'measured_ms09_batches':batches},indent=1))


if __name__ == '__main__':
    main()
