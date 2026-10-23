#!/usr/bin/env python3
"""M2H v6_4 = M2H v6_3 plus ONE feature: an EXPLICIT-SUBSET plan (--plan/--plan-sha256, mandatory). The runner reads the
full frozen contract (identical items, order and denominators to the v6_3 contract), validates the plan with plan_items
(unique well-formed ids, contract membership at the stated position, identical canonical item SHA-256, contract order,
complete split cases, no selected item with any v6_3 attempt) and attempts ONLY the selected items, each at most once,
through the unchanged admission/pin/lease/stop/publication/reader path. v6_4 attempts use their own namespace (_h6_4)
and also hold the v6_3 singleton lock, so v6_3 and v6_4 pipelines never run together.
Historical-M2 (A2 ms01..ms08) measured re-solve over the v6_3 transport (parent Codex review v2 HOLD fixes, plus the
v6_2 re-review fixes: ONE shared predicate for all five admissions; any signal/cancellation never qualifies, and the
publication window is signal-blocked with a final cancellation check; exact covered/excluded universe).
Each item regenerates its ORIGINAL independent-B formula; a mismatch with the bound historical receipt CNF is an
explicit pre-pin BindingRefusal (no pin/job/group, unattempted, chunk ends, no veto). CaDiCaL at the original 300/600
limit, drat-trim 1200, the same exact measured predicate, one attempt, no automatic retry, ONE pipeline (singleton
lock). Frozen policy clocks: no admission at/after 17:20 PDT (independent of STOP-K1; the v6_3 gates also refuse every
later worker/solver/checker phase); the chunk deadline is the 17:57 native end minus a 120 s cleanup allowance and
the runtime refuses any group whose 2400 s budget does not fit before it.
Historical receipts are validated per revision (5, 9, 12, 14, 15) with explicit layouts, and stay ORIGINAL-QUALIFIED
only. The M2H reader accepts ONLY the exact measured v6_3 schema with every primary/pin/commit binding; there is no
historical fallback. Whole-plan retained bound = runtime plan bound + every M2H item at the ordinary per-item bound.
Parent source GO required before running.
"""
import argparse
import datetime
import fcntl
import hashlib
import json
import os
import re
import signal
import time

import encode_skel_b as ENC
import m2_item_owner_v6_3 as OWNER
import m2_ms09_contract_v6_3 as COMMON
import m2_ms09_evidence_v6_3 as E
import m2_supervised_runtime_v6_3 as R
import run_m2_ms09_k1_v6_3 as TX

L = COMMON.LANE
SCHEMA = 'PA19-M2H-A2-v6_4'
RUNNER = 'run_m2h_v6_4.py'
EXTRA_SOURCES = ('src/freeze_m2h_v6_4.py','src/run_m2h_v6_4.py','src/final_m2h_inventory_v6_4.py')
POLICY_CLOCKS = {'admission_cutoff':'2026-10-18T17:20:00-07:00','native_end':'2026-10-18T17:57:00-07:00','cleanup_allowance_seconds':120}
SINGLETON = 'cycle2/m2h-v6_4-singleton.lock'
PRIOR_SINGLETON = 'cycle2/m2h-v6_3-singleton.lock'  # also held: one M2H pipeline across versions
PLAN_SCHEMA = 'PA19-M2H-SUBSET-PLAN-v6_4'
ID_RE = re.compile(r'ms\d{2}_b\d{5}(:\d{5}-\d{5})?')
SHA_RE = re.compile(r'[0-9a-f]{64}')
STAGED = r'^/opt/homebrew/bin/cadical -q -t (300|600) CNF PROOF; binary DRAT staged \(zstd-1 in memory\) then drat-trim -i -t 1200$'
STREAMED = r'^/opt/homebrew/bin/cadical -q -t (600) CNF PROOF; binary DRAT streamed to drat-trim -i -t %d$'
# Explicit historical layouts (mode, stream_check_revision) -> (solver-string pattern, required drat s_lines, replay required)
HISTORICAL = {('direct',5):(STREAMED % 1800,None,False),('direct',9):(STREAMED % 1800,['s VERIFIED'],False),
              ('partbatch',9):(STREAMED % 1200,['s VERIFIED'],False),('direct',12):(STAGED,['s VERIFIED'],True),
              ('direct',14):(STAGED,['s VERIFIED'],True),('partbatch',14):(STAGED,['s VERIFIED'],True),
              ('direct',15):(STAGED,['s VERIFIED'],True),('partbatch',15):(STAGED,['s VERIFIED'],True)}


REQUIRED_ADMISSIONS = (('owner_preconstruction_gate','construct'),('owner_prespawn_gate','worker'),
                       ('worker_preconstruction_gate','construct'),('worker_solver_gate','solver'),('worker_checker_gate','checker'))


def admission_records(r):
    native = r.get('native_result') if isinstance(r.get('native_result'),dict) else {}
    gates = native.get('gates') if isinstance(native.get('gates'),list) else []
    return ({'owner_preconstruction_gate':r.get('owner_preconstruction_gate'),'owner_prespawn_gate':r.get('owner_prespawn_gate'),
             'worker_preconstruction_gate':native.get('worker_preconstruction_gate'),
             'worker_solver_gate':gates[0] if len(gates) > 0 else None,'worker_checker_gate':gates[1] if len(gates) > 1 else None},len(gates))


def admission_errors(r,cut,require_all):
    """ONE shared predicate for the five admissions of an item: every present admission record carries its phase and the
    frozen cutoff; every admitted one is timestamped strictly before the cutoff; a qualifying UNSAT needs all five admitted."""
    errors = []
    by,n = admission_records(r)
    if n > 2: errors.append('unexpected worker phase gate count %d' % n)
    for name,phase in REQUIRED_ADMISSIONS:
        g = by[name]
        if g is None:
            if require_all: errors.append('required admission missing: '+name)
            continue
        if not isinstance(g,dict): errors.append('admission record invalid: '+name); continue
        if g.get('phase') != phase: errors.append('admission phase differs: '+name)
        if g.get('admission_cutoff_epoch') != cut: errors.append('admission cutoff differs: '+name)
        if g.get('admitted') is True:
            if type(g.get('at_epoch')) not in (int,float) or not g['at_epoch'] < cut: errors.append('admission at/after the frozen cutoff or untimed: '+name)
        elif require_all: errors.append('required admission not admitted: '+name)
    return errors


def epochs(c=None):
    pc = POLICY_CLOCKS if c is None else c['policy_clocks']
    return (datetime.datetime.fromisoformat(pc['admission_cutoff']).timestamp(),datetime.datetime.fromisoformat(pc['native_end']).timestamp(),
            pc['cleanup_allowance_seconds'])


def resource_policy(n_items):
    p = COMMON.resource_policy()
    p['whole_plan_remaining_bound_bytes'] = R.ALL_PLANNED_RETAINED_BOUND+n_items*R.ITEM_ORDINARY_BOUND
    p['m2h_items_added_at_ordinary_bound'] = n_items
    return p


def historical_errors(x,r):
    """Identity of one historical checked-UNSAT receipt against its contract item; per-revision explicit layout."""
    errors, rev = [], r.get('stream_check_revision')
    layout = HISTORICAL.get((x['mode'],rev)) if type(rev) is int else None
    if layout is None: return ['unsupported historical layout %r' % ((x['mode'],rev),)]
    pattern,lines,replay = layout
    m = re.fullmatch(pattern,str(r.get('solver')))
    if not m or int(m.group(1)) != x['native_seconds']: errors.append('historical solver/limit layout differs')
    if rev != x['historical']['revision']: errors.append('historical revision differs')
    if r.get('status') != 'UNSAT' or r.get('checked') is not True or r.get('solver_rc') != 20 or r.get('drat_trim_verified') is not True: errors.append('not historical checked UNSAT')
    dt = r.get('drat_trim') if isinstance(r.get('drat_trim'),dict) else {}
    if dt.get('rc') != 0 or dt.get('stop') != 'self' or dt.get('says_verified') is not True or dt.get('s_lines') != lines: errors.append('historical checker verdict layout differs')
    if replay and not (isinstance(r.get('replay'),dict) and r['replay'].get('ok') is True): errors.append('historical replay missing')
    if type(r.get('multiset')) is not int or r['multiset'] != x['multiset'] or type(r.get('b_index')) is not int or r['b_index'] != x['b_index']: errors.append('historical case identity differs')
    if x['mode'] == 'direct':
        if r.get('indices') is not None or r.get('encoder') != 'encode_skel_b.build_v2': errors.append('historical direct identity differs')
    elif not (isinstance(r.get('indices'),list) and len(r['indices']) == 2 and all(type(v) is int for v in r['indices'])
              and r['indices'] == x['indices'] and r.get('encoder') == 'encode_skel_b.build_partbatch'): errors.append('historical exact interval/encoder differs')
    if not (isinstance(r.get('cnf_sha256'),str) and SHA_RE.fullmatch(r['cnf_sha256']) and r['cnf_sha256'] == x['expected_cnf_sha256']): errors.append('historical CNF SHA differs')
    if not (type(r.get('cnf_bytes')) is int and r['cnf_bytes'] > 0 and r['cnf_bytes'] == x['expected_cnf_bytes']): errors.append('historical CNF bytes differ')
    return errors


def list_errors(x,ed):
    errors = []
    src, rel = ed.get('source'), 'cycle2/skel-b/skeletons-b-ms%02d.json' % x['multiset']
    if not isinstance(src,str) or os.path.realpath(src) != os.path.realpath(L/rel) or type(ed.get('index')) is not int or ed['index'] != x['b_index']:
        errors.append('list source/index differs')
    n = ed.get('num_placements')
    if not (type(n) is int and n > 0 and isinstance(ed.get('placements'),list) and n == len(ed['placements']) == x['list']['n']): errors.append('list denominator differs')
    return errors


def task(item,tag='h6_4'):
    if item['mode'] == 'direct':
        base = 'cycle2/m2skel_drat/ms%02d_b%05d_%s' % (item['multiset'],item['b_index'],tag)
        claim = 'cycle2/claims/m2%s_ms%02d_b%05d.claim' % (tag,item['multiset'],item['b_index'])
    else:
        lo,hi = item['indices']
        base = 'cycle2/m2part_drat/ms%02d_b%05d/batch_%05d_%05d_%s' % (item['multiset'],item['b_index'],lo,hi,tag)
        claim = 'cycle2/claims/m2%s_ms%02d_b%05d_%05d_%05d.claim' % (tag,item['multiset'],item['b_index'],lo,hi)
    return {'id':item['id'],'indices':item['indices'],'new_record':base+'.json','pin':base+'.cnf-pin.json',
            'commit':base+'.receipt.json','claim':claim}


def item_sha256(x):
    """Canonical identity of one contract item (sorted-key compact JSON)."""
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def plan_items(c,h,plan):
    """Exact explicit subset of the frozen full contract; items are never copied, mutated or renumbered. Requires unique
    well-formed ids, each a contract member (not an excluded case) at its stated position with an identical canonical item,
    contract order, every selected split case complete, and no selected item with any v6_3 attempt (record, pin, commit or
    claim). Returns the selected contract items in contract order."""
    assert isinstance(plan,dict) and plan.get('schema') == PLAN_SCHEMA, 'plan schema differs'
    assert plan.get('contract_sha256') == h, 'plan bound to another contract'
    sel = plan.get('items')
    assert isinstance(sel,list) and sel, 'empty selection'
    assert all(isinstance(s,dict) and set(s) == {'id','contract_position','item_sha256'} for s in sel), 'plan entry fields differ'
    ids = [s['id'] for s in sel]
    assert all(isinstance(i,str) and ID_RE.fullmatch(i) for i in ids), 'malformed selected id'
    assert len(set(ids)) == len(ids), 'duplicate selected id'
    excluded = {e['case'] for e in c['excluded_cases']}
    where = {x['id']:p for p,x in enumerate(c['items'])}
    out = []
    for s in sel:
        assert s['id'] not in excluded, 'selected id names an excluded case: '+s['id']
        assert s['id'] in where, 'selected id is not a member of the contract: '+s['id']
        assert type(s['contract_position']) is int and s['contract_position'] == where[s['id']], 'selected position differs: '+s['id']
        x = c['items'][s['contract_position']]
        assert item_sha256(x) == s['item_sha256'], 'selected item identity differs: '+s['id']
        old = task(x,'h6_3')
        assert not any((L/old[k]).exists() for k in ('new_record','pin','commit','claim')), 'selected item has a v6_3 attempt: '+s['id']
        out.append(x)
    pos = [s['contract_position'] for s in sel]
    assert pos == sorted(pos), 'selected positions not in contract order'
    for case in sorted({(x['multiset'],x['b_index']) for x in out if x['mode'] == 'partbatch'}):
        need = {x['id'] for x in c['items'] if x['mode'] == 'partbatch' and (x['multiset'],x['b_index']) == case}
        assert need <= set(ids), 'selected split case is incomplete: ms%02d_b%05d' % case
    return out


def verify_sources(c):
    assert c['schema'] == SCHEMA and set(c['source_sha256']) == set(tuple(COMMON.SOURCE_FILES)+EXTRA_SOURCES)
    for p,h in c['source_sha256'].items(): assert E.digest(L/p) == h, ('frozen source changed',p)
    assert c['supervisor'] == {'path':str(R.SUP_PATH),'sha256':R.SUP_SHA} and E.digest(R.SUP_PATH) == R.SUP_SHA


def verify(c):
    verify_sources(c)
    assert c['policy_clocks'] == POLICY_CLOCKS
    assert c['resource_policy'] == resource_policy(len(c['items'])) and c['automatic_retry_allowed'] is False and c['check_seconds'] == 1200
    assert c['binary_authority']['solver']['path'] == '/opt/homebrew/bin/cadical'
    assert c['binary_authority']['checker']['path'] == str(L/'tools/drat-trim/drat-trim')
    assert sorted(c['skeletons']) == [str(m) for m in range(1,9)]
    totals = {}
    for mi,s in c['skeletons'].items():
        assert s['path'] == 'cycle2/skel-b/skeletons-b-ms%02d.json' % int(mi) and E.digest(L/s['path']) == s['sha256']
        totals[int(mi)] = len(COMMON.read(L/s['path'])['skeletons'])
    ids = [x['id'] for x in c['items']]
    assert c['order'] == ids and len(set(ids)) == len(ids)
    direct = [(x['multiset'],x['b_index']) for x in c['items'] if x['mode'] == 'direct']
    split = {(x['multiset'],x['b_index']) for x in c['items'] if x['mode'] == 'partbatch'}
    assert len(set(direct)) == len(direct) and not (set(direct) & split)
    lists = {}
    for x in c['items']:
        assert x['solver'] == 'cadical' and x['native_seconds'] in (300,600) and type(x['multiset']) is int and 1 <= x['multiset'] <= 8
        assert type(x['b_index']) is int and 0 <= x['b_index'] < totals[x['multiset']]
        exp_id = 'ms%02d_b%05d' % (x['multiset'],x['b_index']) if x['mode'] == 'direct' else 'ms%02d_b%05d:%05d-%05d' % (x['multiset'],x['b_index'],*x['indices'])
        assert x['id'] == exp_id and SHA_RE.fullmatch(x['expected_cnf_sha256']) and type(x['expected_cnf_bytes']) is int and x['expected_cnf_bytes'] > 0
        assert E.digest(L/x['historical']['path']) == x['historical']['sha256'], ('historical receipt changed',x['id'])
        errs = historical_errors(x,COMMON.read(L/x['historical']['path']))
        assert not errs, (x['id'],errs)
        if x['mode'] == 'partbatch':
            assert x['historical']['path'].startswith('cycle2/m2part_drat/ms%02d_b%05d/' % (x['multiset'],x['b_index']))
            lists.setdefault(x['list']['path'],(x['list']['sha256'],x['list']['n'],(x['multiset'],x['b_index'])))
            assert lists[x['list']['path']] == (x['list']['sha256'],x['list']['n'],(x['multiset'],x['b_index']))
            assert x['list']['path'] == 'cycle2/m2part_drat/ms%02d_b%05d/ext.json' % (x['multiset'],x['b_index'])
        else:
            assert x['mode'] == 'direct' and x['indices'] is None and x['historical']['path'] == 'cycle2/m2skel_drat/ms%02d_b%05d.json' % (x['multiset'],x['b_index'])
    for path,(h,n,case) in lists.items():
        assert E.digest(L/path) == h
        first = next(x for x in c['items'] if x['mode'] == 'partbatch' and x['list']['path'] == path)
        assert not list_errors(first,COMMON.read(L/path)), (path,list_errors(first,COMMON.read(L/path)))
        got = sorted(x['indices'] for x in c['items'] if x['mode'] == 'partbatch' and (x['multiset'],x['b_index']) == case)
        assert got == [[lo,min(n,lo+100)-1] for lo in range(0,n,100)], ('split item set is not the exact complete B100 partition',case)
    assert c['cases_direct'] == len(direct) and c['cases_split'] == len(split) and c['split_intervals'] == sum(x['mode'] == 'partbatch' for x in c['items'])
    excluded = [e['case'] for e in c['excluded_cases']]
    covered = {'ms%02d_b%05d' % k for k in set(direct) | split}
    universe = {'ms%02d_b%05d' % (mi,bi) for mi,n in totals.items() for bi in range(n)}
    assert len(set(excluded)) == len(excluded), 'duplicate excluded case'
    assert not (set(excluded) & covered), 'excluded case is also covered'
    assert set(excluded) | covered == universe, 'covered/excluded is not exactly the A2 ms01..ms08 skeleton universe'


def recipe(c,x):
    r = {'mode':x['mode'],'multiset':x['multiset'],'b_index':x['b_index'],'indices':x['indices'],
         'skeleton_path':c['skeletons'][str(x['multiset'])]['path'],'skeleton_sha256':c['skeletons'][str(x['multiset'])]['sha256'],
         'encoder_sha256':c['source_sha256']['src/encode_skel_b.py']}
    if x['mode'] == 'partbatch': r.update(list_path=x['list']['path'],list_sha256=x['list']['sha256'],complete_denominator=x['list']['n'])
    return r


def inspect(c,h,x):
    """EXACT measured v6_3 reader: every binding must hold; nothing historical can qualify here."""
    it = task(x)
    if not (L/it['new_record']).exists(): return {'state':'MISSING','record':None,'errors':[]}
    try:
        raw = (L/it['new_record']).read_bytes(); r = json.loads(raw)
        pin,k = COMMON.read(L/it['pin']),COMMON.read(L/it['commit'])
        assert pin['schema'] == 'PA19-K1-CNF-PIN-v6_3' and k['schema'] == 'PA19-K1-RECEIPT-v6_3'
        assert pin['production_contract_sha256'] == k['production_contract_sha256'] == h
        assert type(pin['multiset']) is int and pin['multiset'] == x['multiset'] and type(pin['b_index']) is int and pin['b_index'] == k['b_index'] == x['b_index']
        assert pin['indices'] == x['indices'] == k['indices'] and pin['recipe'] == recipe(c,x)
        assert pin['source_sha256'] == c['source_sha256'] and pin['binary_authority'] == c['binary_authority'] and pin['supervisor_sha256'] == R.SUP_SHA
        assert pin['cnf_sha256'] == x['expected_cnf_sha256'] and pin['cnf_bytes'] == x['expected_cnf_bytes']
        assert k['pin_sha256'] == E.digest(L/it['pin']) and k['record_sha256'] == hashlib.sha256(raw).hexdigest()
        assert isinstance(r,dict) and r.get('pipeline_schema') == 'PA19-SUPERVISED-DRAT-v6_3'
        assert r.get('production_contract_sha256') == h and r.get('pre_child_pin_sha256') == k['pin_sha256'] and r.get('pre_child_pin_path') == it['pin']
        assert r.get('runner') == RUNNER and r.get('count_for_scientific_coverage') is True and r.get('historical_receipt') == x['historical']
        assert r.get('multiset') == x['multiset'] and r.get('b_index') == x['b_index'] and r.get('indices') == x['indices']
        if x['mode'] == 'partbatch':
            assert r.get('list_sha256') == x['list']['sha256'] and r.get('complete_denominator') == x['list']['n'] and r.get('enumerator') == 'extend_b.py'
        else:
            assert not any(key in r for key in ('list_sha256','complete_denominator','enumerator'))
        if r.get('group_started'): assert (r.get('supervisor') or {}).get('supervisor_sha256') == R.SUP_SHA
        errs = admission_errors(r,epochs(c)[0],r.get('status') == 'UNSAT')
        assert not errs, errs
        if r.get('status') == 'UNSAT':
            assert not r.get('owner_cancelled') and not r.get('observed_signal') and not (r.get('supervisor') or {}).get('observed_signal'), \
                'UNSAT record carries a signal/cancellation'
    except (OSError,ValueError,KeyError,TypeError,AssertionError,StopIteration) as exc:
        return {'state':'INTEGRITY_VETO','errors':[repr(exc)]}
    enc = 'encode_skel_b.build_v2' if x['mode'] == 'direct' else 'encode_skel_b.build_partbatch'
    ex = E.expected(x['multiset'],x['b_index'],x['indices'],pin['cnf_sha256'],pin['cnf_bytes'],enc,x['native_seconds'],False)
    ex.update(binary_authority=c['binary_authority'],lane_root=str(L),source_sha256=c['source_sha256'],recipe=pin['recipe'])
    return E.inspect(L/it['new_record'],ex,k['record_sha256'])


def formula(c,x,skeletons):
    D = skeletons[x['multiset']]; sk = D['skeletons'][x['b_index']]
    special = [p for p in D['profiles'] if list(p) != COMMON.P0]
    if x['mode'] == 'direct':
        nv,cl = ENC.build_v2(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special)
    else:
        assert E.digest(L/x['list']['path']) == x['list']['sha256']
        ed = COMMON.read(L/x['list']['path']); lo,hi = x['indices']
        assert not list_errors(x,ed)
        nv,cl = ENC.build_partbatch(D['c0'],[tuple(t) for t in sk['types']],sk['empty'],special,[ed['placements'][i] for i in range(lo,hi+1)])
    return ENC.cnf_bytes(nv,cl)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); ap.add_argument('--max-attempts',type=int)
    ap.add_argument('--plan',required=True); ap.add_argument('--plan-sha256',required=True)
    args = ap.parse_args(); R.install_handlers()
    cut,end,cleanup = epochs()
    logs = L/'cycle2/m2h6_4-chunks'/('%s-%d' % (time.strftime('%Y%m%dT%H%M%S'),time.time_ns())); logs.mkdir(parents=True,exist_ok=False)
    stage = L/'scratch/m2h-publish'/logs.name
    locks = []
    try:
        for name in (PRIOR_SINGLETON,SINGLETON):
            locks.append(os.open(L/name,os.O_CREAT|os.O_RDWR,0o644)); fcntl.flock(locks[-1],fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:
        COMMON.publish_json(logs/'singleton-refusal.json',{'status':'REFUSED','reason':'another M2H v6_3/v6_4 pipeline holds a singleton lock',
            'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
        print('M2H singleton refusal',flush=True)
        for fd in locks: os.close(fd)
        return
    try:
        run_locked(args,cut,end,cleanup,logs,stage)
    finally:
        for fd in locks: fcntl.flock(fd,fcntl.LOCK_UN); os.close(fd)


def run_locked(args,cut,end,cleanup,logs,stage):
    """Body of main() while this process holds the M2H singleton lock."""
    if time.time() >= cut:
        COMMON.publish_json(logs/'admission-closed.json',{'status':'REFUSED','reason':'frozen 17:20 policy admission cutoff reached',
            'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
        print('M2H admission closed by the frozen policy clock',flush=True); return
    deadline = min(time.monotonic()+10800,time.monotonic()+(end-time.time())-cleanup)
    with R.Capacity(deadline,metadata=True,wait_allowance=60):
        st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+1024**2
        assert E.digest(args.contract) == args.sha256
        c = COMMON.read(args.contract); verify(c)
        assert E.digest(args.plan) == args.plan_sha256, 'plan hash differs'
        selected = plan_items(c,args.sha256,COMMON.read(args.plan))
        union = R.admission_union(L)
        record_vetoes = {x['id']:s for x in c['items'] if (L/task(x)['new_record']).exists()
                         for s in [inspect(c,args.sha256,x)['state']] if s in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN')}
        if union['persistent_vetoes'] or union['resource_stops'] or record_vetoes:
            COMMON.publish_json(logs/'initialization-deferred.json',{'status':'UNKNOWN','admission_union':union,'record_vetoes':record_vetoes,
                'init_stage':'veto-scan' if (union['persistent_vetoes'] or record_vetoes) else 'resource-stop','native_has_started':False,
                'contract_sha256':args.sha256,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
            print('M2H initialization refusal',union,record_vetoes,flush=True); return
        assert all(v['matches'] for v in R.binary_observations(c['binary_authority']).values())
        bound = c['resource_policy']['whole_plan_remaining_bound_bytes']
        reference = R.create_census(); census = R.census_for_gate(reference)
        assert census['current_data_upper_bytes']+bound+R.OTHER_WRITER_MARGIN <= R.DATA_CAP
        admission = {'binary_authority':c['binary_authority'],'census_reference':reference,'whole_plan_remaining_bound_bytes':bound,
                     'admission_cutoff_epoch':cut}
        skeletons = {int(k):COMMON.read(L/v['path']) for k,v in c['skeletons'].items()}
    records,attempts,stop = [],0,None
    for x in selected:
        if args.max_attempts is not None and attempts >= args.max_attempts: stop = 'operational tranche reached'; break
        if time.time() >= cut: stop = 'admission closed by the frozen 17:20 policy clock'; break
        if R._CANCEL[0] or time.monotonic()+2550 > deadline: stop = 'deadline/cancellation; no new native'; break
        it = task(x)
        if (L/it['new_record']).exists():
            q = inspect(c,args.sha256,x)
            if q['state'] in ('INTEGRITY_VETO','SAT_VETO','HALT_UNKNOWN'): stop = 'existing persistent veto '+x['id']; break
            continue  # every previous UNKNOWN remains; no retry
        if not TX.claim(it['claim'],args.sha256,it['id']): continue

        def build():
            assert E.digest(args.contract) == args.sha256
            verify_sources(c)
            assert not (L/it['new_record']).exists()
            ref = c['skeletons'][str(x['multiset'])]
            assert E.digest(L/ref['path']) == ref['sha256'] and E.digest(L/x['historical']['path']) == x['historical']['sha256']
            raw = formula(c,x,skeletons)
            got = (hashlib.sha256(raw).hexdigest(),len(raw))
            if got != (x['expected_cnf_sha256'],x['expected_cnf_bytes']):
                raise OWNER.BindingRefusal('regenerated formula %s/%d differs from bound historical CNF %s/%d' % (got+(x['expected_cnf_sha256'],x['expected_cnf_bytes'])))
            return raw
        paths = TX.item_paths(it,stage)
        try:
            r = OWNER.execute(build,recipe(c,x),args.sha256,c['source_sha256'],paths,deadline,admission,'cadical',x['native_seconds'])
        except BaseException as exc:
            COMMON.publish_json(logs/('owner-exception-'+x['id'].replace(':','_')+'.json'),{'status':'UNKNOWN','reason':repr(exc),'id':x['id']},stage)
            if not (L/it['pin']).exists(): TX.release_unattempted(it['claim'],'M2H owner refused before pin/native')
            stop = 'owner admission/exception'; break
        if r.get('binding_refusal'):
            assert not any(os.path.exists(paths[k]) for k in ('pin','job','supervisor','worker_result','quarantine')), 'binding refusal after a pin/job/group'
            COMMON.publish_json(logs/('binding-refusal-'+x['id'].replace(':','_')+'.json'),{'status':'UNATTEMPTED','id':x['id'],
                'reason':r['binding_refusal'],'no_pin_job_group':True,'veto':None,'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')},stage)
            TX.release_unattempted(it['claim'],'M2H pre-pin binding refusal; no pin/job/group; no veto'); stop = 'pre-pin binding refusal'; break
        if r.get('unattempted') == 'before-pin' and not (L/it['pin']).exists():
            TX.release_unattempted(it['claim'],'refusal rule1: M2H refused before pin/job; no record or HALT'); stop = 'pre-pin refusal'; break
        if r.get('unattempted') == 'after-pin-before-worker':
            TX.retire_unattempted_after_pin(it,paths,'refusal rule2: M2H refused before worker; no record or HALT'); stop = 'pre-worker refusal'; break
        if not r.get('pre_child_pin_sha256'):
            COMMON.publish_json(logs/('binding-or-construction-'+x['id'].replace(':','_')+'.json'),r,stage)
            TX.release_unattempted(it['claim'],'M2H construction refused before immutable pin/native'); stop = 'construction refusal'; break
        blocked = signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGTERM,signal.SIGINT})  # v6_3 publication window
        try:
            if R._CANCEL[0] and not r.get('owner_cancelled'):  # a cancellation after the owner composed the outcome
                r.update(status='UNKNOWN',checked=False,owner_cancelled=True,halt_production=True,chunk_stop=True,
                         safety_veto=list(r.get('safety_veto') or [])+['cancellation before publication'])
                OWNER.persist_veto(r,paths,args.sha256,recipe(c,x))
            r.update(runner=RUNNER,count_for_scientific_coverage=True,historical_receipt=x['historical'])
            if x['mode'] == 'partbatch': r.update(list_sha256=x['list']['sha256'],complete_denominator=x['list']['n'],enumerator='extend_b.py')
            raw = (json.dumps(r,indent=1)+'\n').encode(); rh = hashlib.sha256(raw).hexdigest()
            COMMON.publish_json(L/it['commit'],{'schema':'PA19-K1-RECEIPT-v6_3','production_contract_sha256':args.sha256,'b_index':x['b_index'],
                'indices':x['indices'],'record_sha256':rh,'pin_sha256':r['pre_child_pin_sha256']},stage)
            COMMON.publish_bytes(L/it['new_record'],raw,stage)  # primary LAST
        finally:
            signal.pthread_sigmask(signal.SIG_SETMASK,blocked)  # a signal in this window now reaches the cancel handler
        attempts += 1
        item = {'id':x['id'],'record':it['new_record'],'sha256':rh,'status':r['status'],'checked':r['checked'],'integrity_status':r['integrity_status'],
                'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')}
        records.append(item); print(json.dumps(item),flush=True)
        for gate in (r.get('native_result') or {}).get('gates') or []:
            if gate.get('census'): admission['census_reference'] = gate['census']['reference']
        if r.get('sat_candidate') or r.get('integrity_status') == 'INVALID' or r.get('halt_production'): stop = 'persistent veto'; break
        if r.get('chunk_stop'): stop = 'worker admission refusal recorded UNKNOWN; chunk ends'; break
    COMMON.publish_json(logs/'summary.json',{'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'contract_sha256':args.sha256,'attempts':attempts,
        'records':records,'stop_reason':stop,'automatic_retry_allowed':False,'policy_clocks':POLICY_CLOCKS,
        'selection_plan':{'path':os.path.realpath(args.plan),'sha256':args.plan_sha256,'selected_ids':[x['id'] for x in selected]}},stage)
    print(logs,flush=True)


if __name__ == '__main__':
    main()
