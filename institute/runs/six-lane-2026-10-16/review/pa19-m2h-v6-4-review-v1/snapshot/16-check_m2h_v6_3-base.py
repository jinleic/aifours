#!/usr/bin/env python3
"""PRIVATE M2H v6_3 control suite (parent Codex review v2 + v6_2 re-review requirements); excluded from scientific coverage.
New in v6_3: O3/O4 settlement-window signal in the REAL owner; T12 publication-window signal (deferred, record consistent,
runner stops); T13 cancellation between owner return and publication (UNKNOWN + persistent HALT); R15-R19 the shared
five-admission predicate (worker preconstruction gate missing/wrong cutoff/post-cutoff, valid five, UNSAT with cancellation);
V1-V3 exact covered/excluded universe (out-of-domain, duplicate, overlapping exclusion names).
No solver, checker or native child is started. All writes go to private shadow lanes under
cycle2/m2h-v6_3-controls-<ns>/ (symlinked read-only inputs, real new directories for outputs); module-global lane roots
of run_m2h_v6_3 / run_m2_ms09_k1_v6_3 / m2_item_owner_v6_3 / final_m2h_inventory_v6_3 are rebound to the shadow for one
test and restored. Stubs replace ONLY the stated component (owner execute, census, gate, formula bytes, reader),
never the code under test. One real lane token at a time (metadata Capacity / owner Capacity).
Families:
  G  runtime gates: frozen policy cutoff missing/past/future; gate records at_epoch and the cutoff
  C  Capacity: 2400 s budget refused before the chunk deadline (no child); observed supervisor signal sets the cancel flag
  O  owner: BindingRefusal -> unattempted before pin, no pin/job/veto; other constructor failure -> persistent INTEGRITY
  R  exact reader: a correctly bound UNKNOWN is UNQUALIFIED; historical wrapper, wrong contract/pin/interval/list/
     denominator/runner/coverage/historical reference/supervisor pin, post-cutoff gate, direct-with-list fields and an
     evidence-free UNSAT are INTEGRITY_VETO; a missing record is MISSING
  T  runner flow: pre-pin refusal, pre-worker refusal, pre-pin binding refusal through the REAL owner, worker refusal
     recorded UNKNOWN, existing UNKNOWN never retried, duplicate claim skipped, singleton lock, frozen 17:20 cutoff,
     existing record veto / resource STOP / persistent flag defer initialization
  I  inventory: a split case with one MISSING interval stays open; readiness false
Usage: check_m2h_v6_3.py CONTRACT SHA256
"""
import argparse
import fcntl
import hashlib
import json
import copy
import os
import signal
import sys
import time
import types
from pathlib import Path

import final_m2h_inventory_v6_3 as INV
import m2_item_owner_v6_3 as OWNER
import m2_ms09_contract_v6_3 as COMMON
import m2_ms09_evidence_v6_3 as E
import m2_supervised_runtime_v6_3 as R
import run_m2_ms09_k1_v6_3 as TX
import run_m2h_v6_3 as H

REAL = COMMON.LANE
SELF = Path(__file__).resolve()


def dump(p,obj):
    p = Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    raw = (json.dumps(obj,indent=1)+'\n').encode()
    with p.open('xb') as f: f.write(raw)
    return hashlib.sha256(raw).hexdigest()


def make_shadow(root,c,limit=8):
    """Private lane: src and skeletons symlinked read-only; historical receipts/lists symlinked only for the first
    `limit` items (the only ones a flow test can attempt); every output directory is a real new directory."""
    root.mkdir(parents=True)
    (root/'src').symlink_to(REAL/'src')
    (root/'cycle2').mkdir(); (root/'cycle2/skel-b').symlink_to(REAL/'cycle2/skel-b')
    for x in c['items'][:limit]:
        for rel in [x['historical']['path']]+([x['list']['path']] if x['mode'] == 'partbatch' else []):
            p = root/rel
            if not p.exists() and not p.is_symlink():
                p.parent.mkdir(parents=True,exist_ok=True); p.symlink_to(REAL/rel)
    return root


class Rebind:
    def __init__(self,root,modules=(H,TX,OWNER,INV)): self.root,self.modules,self.saved = root,modules,[]
    def __enter__(self):
        for m in self.modules: self.saved.append((m,m.L)); m.L = self.root
        return self
    def __exit__(self,*a):
        for m,v in self.saved: m.L = v


def gate_providers(cut_now):
    return {'census':lambda:{'reference':{'path':'cycle2/accounting-v3/CONTROL'},'current_data_upper_bytes':0,'age_seconds':0.0,'finished_monotonic':time.monotonic()},
            'rss':lambda:{'known':True,'rss_bytes':10**8,'current_group_and_owner_bytes':0},
            'binaries':lambda:{k:{'matches':True} for k in ('python','solver','checker')},
            'count':lambda:2,'free':lambda:10**12,'clock':time.monotonic,'wallclock':lambda:cut_now}


def base_lease(cut):
    now = time.monotonic()
    return {'owner_pid':os.getpid(),'projected_growth_bytes':R.ITEM_GROWTH,'census_reference':{'path':'x'},
            'whole_plan_remaining_bound_bytes':R.ALL_PLANNED_RETAINED_BOUND,'binary_authority':{},'group_rss_cap_bytes':R.GROUP_RSS_CAP,
            'busy_units':2,'lane_busy_ceiling':4,'chunk_deadline_monotonic':now+10**5,'item_deadline_monotonic':now+10**5,'admission_cutoff_epoch':cut}


def gate_controls(root):
    rows, t = [], time.time()
    for name,cut,wall_now,expect_err in [('G1 cutoff missing',None,t,'frozen policy admission cutoff missing'),
                                         ('G2 past cutoff',t-1,t,'admission closed by frozen policy clock'),
                                         ('G3 future cutoff',t+3600,t,None)]:
        g = R.full_gate(base_lease(cut),'solver',root,gate_providers(wall_now))
        ok = (expect_err in g['errors'] and not g['admitted']) if expect_err else (g['admitted'] and g['errors'] == [])
        ok = ok and type(g.get('at_epoch')) is float and g.get('admission_cutoff_epoch') == cut
        rows.append({'name':name,'errors':g['errors'],'admitted':g['admitted'],'ok':ok})
    return rows


def capacity_controls(root):
    rows = []
    orig_gate, orig_sup = R.full_gate, R.supervisor
    try:
        R.full_gate = lambda lease,phase,lane=None,providers=None: {'admitted':True,'errors':[],'phase':phase}
        with R.Capacity(time.monotonic()+1000,wait_allowance=60) as cap:
            rec,gate = cap.supervise([sys.executable,'-c','pass'],'CONTROL-budget',base_lease(time.time()+3600),root/'b.sup.json',root/'b.q.json')
        rows.append({'name':'C1 budget does not fit chunk deadline','rec':rec,'errors':gate['errors'],'children':len(cap.children),
                     'ok':rec is None and 'group budget 2400 s does not fit before the chunk deadline' in gate['errors'] and not cap.children})
        fake = types.SimpleNamespace(supervise=lambda *a,**k:{'leader_pid':None,'observed_signal':'SIGTERM','completed_cleanly':False})
        R.supervisor = lambda: fake
        R._CANCEL[0] = False
        with R.Capacity(time.monotonic()+5000) as cap:
            rec,gate = cap.supervise([sys.executable,'-c','pass'],'CONTROL-signal',base_lease(time.time()+3600),root/'s.sup.json',root/'s.q.json')
        rows.append({'name':'C2 observed supervisor signal sets cancel','cancel':R._CANCEL[0],'ok':R._CANCEL[0] is True and rec['observed_signal'] == 'SIGTERM'})
    finally:
        R.full_gate, R.supervisor = orig_gate, orig_sup
        R._CANCEL[0] = False
    return rows


def owner_controls(root,c,h):
    rows = []
    x = next(i for i in c['items'] if i['mode'] == 'direct')
    orig_gate = R.full_gate
    try:
        R.full_gate = lambda lease,phase,lane=None,providers=None: {'admitted':True,'errors':[],'phase':phase}
        for name,exc,want in [('O1 BindingRefusal is unattempted, no veto',OWNER.BindingRefusal('CONTROL binding mismatch'),'none'),
                              ('O2 other constructor failure stays a persistent INTEGRITY veto',AssertionError('CONTROL source drift'),'INTEGRITY')]:
            sub = root/name.split()[0]
            make_shadow(sub,{'items':[x]})
            with Rebind(sub):
                it = H.task(x); paths = TX.item_paths(it,sub/'scratch/stage')
                def boom(e=exc): raise e
                admission = {'binary_authority':c['binary_authority'],'census_reference':{'path':'x'},'whole_plan_remaining_bound_bytes':R.ALL_PLANNED_RETAINED_BOUND,
                             'admission_cutoff_epoch':time.time()+3600}
                r = OWNER.execute(boom,H.recipe(c,x),h,c['source_sha256'],paths,time.monotonic()+5000,admission,'cadical',600)
            flags = sorted(p.name for p in (sub/'cycle2').glob('m2k3-*.flag'))
            files = [k for k in ('pin','job','supervisor','worker_result','quarantine') if os.path.exists(paths[k])]
            ok = (r.get('binding_refusal') == 'CONTROL binding mismatch' and r.get('unattempted') == 'before-pin' and not r.get('halt_production')
                  and r.get('integrity_status') == 'NOT_EVALUATED' and not flags and not files) if want == 'none' else \
                 (r.get('integrity_status') == 'INVALID' and r.get('halt_production') is True and flags == ['m2k3-INTEGRITY.flag'] and not files)
            rows.append({'name':name,'flags':flags,'files':files,'unattempted':r.get('unattempted'),'integrity':r.get('integrity_status'),'ok':ok})
    finally:
        R.full_gate = orig_gate
    return rows


def settlement_controls(root,c,h):
    """O3/O4: the REAL owner composes the outcome after a (fake) clean supervision; O3 delivers SIGTERM during settlement."""
    rows, x = [], next(i for i in c['items'] if i['mode'] == 'direct')
    orig = (R.full_gate,R.supervisor,R.Capacity._settle)
    try:
        R.full_gate = lambda lease,phase,lane=None,providers=None: {'admitted':True,'errors':[],'phase':phase}
        for name,signal_in_settle in [('O3 SIGTERM during settlement -> owner_cancelled UNKNOWN + HALT',True),('O4 same flow without a signal -> no cancellation, no veto',False)]:
            sub = root/name.split()[0]; make_shadow(sub,{'items':[x]})
            with Rebind(sub):
                it = H.task(x); paths = TX.item_paths(it,sub/'scratch/stage')
                def fake_supervise(command,nm,wall,cap,floor,lane,record,quarantine,grace=60,owner_child=None):
                    rec = {'leader_pid':None,'completed_cleanly':True,'uncertain':False,'observed_signal':None,'trip_reason':None,'stop':None,
                           'supervisor_sha256':R.SUP_SHA,'CONTROL':True}
                    dump(record,rec)
                    dump(paths['worker_result'],{'schema':'PA19-NATIVE-RESULT-v6_3','status':'UNKNOWN','integrity_status':'NOT_EVALUATED',
                         'integrity_errors':[],'sat_candidate':False,'halt_production':False,'bounded_unknown':'CONTROL'})
                    return rec
                R.supervisor = lambda: types.SimpleNamespace(supervise=fake_supervise)
                def fake_settle(self,rec,_sig=signal_in_settle):
                    if _sig: os.kill(os.getpid(),signal.SIGTERM)
                    self.settlement = {'group_quiescent':True,'leader_reaped':True,'explicit_owned_popen_wait':True,'owned_leader_pid':None,'CONTROL':True}
                    self.safe = True
                R.Capacity._settle = fake_settle
                admission = {'binary_authority':c['binary_authority'],'census_reference':{'path':'x'},'whole_plan_remaining_bound_bytes':R.ALL_PLANNED_RETAINED_BOUND,
                             'admission_cutoff_epoch':time.time()+3600}
                r = OWNER.execute(lambda: b'p cnf 1 1\n1 0\n',H.recipe(c,x),h,c['source_sha256'],paths,time.monotonic()+5000,admission,'cadical',600)
            cancelled = R._CANCEL[0]; R._CANCEL[0] = False
            flags = sorted(p.name for p in (sub/'cycle2').glob('m2k3-*.flag'))
            ok = (r.get('owner_cancelled') is True and r.get('status') == 'UNKNOWN' and r.get('halt_production') is True and flags == ['m2k3-HALT.flag'] and cancelled) \
                 if signal_in_settle else (not r.get('owner_cancelled') and r.get('status') == 'UNKNOWN' and not r.get('halt_production') and not flags)
            rows.append({'name':name,'owner_cancelled':r.get('owner_cancelled'),'status':r.get('status'),'halt':r.get('halt_production'),'flags':flags,'ok':ok})
    finally:
        R.full_gate,R.supervisor,R.Capacity._settle = orig
        R._CANCEL[0] = False
    return rows


def five_gates(cut):
    g = lambda phase: {'phase':phase,'admitted':True,'errors':[],'admission_cutoff_epoch':cut,'at_epoch':cut-3600.0}
    return g('construct'),g('worker'),{'worker_preconstruction_gate':g('construct'),'gates':[g('solver'),g('checker')]}


def universe_controls(c):
    rows = []
    covered = next(i for i in c['items'] if i['mode'] == 'direct')
    for name,mut,msg in [('V1 out-of-domain excluded name',lambda cc: cc['excluded_cases'][0].update(case='ms01_b99999'),'skeleton universe'),
                         ('V2 duplicate excluded name',lambda cc: cc['excluded_cases'].append(dict(cc['excluded_cases'][0])),'duplicate excluded case'),
                         ('V3 excluded name that is also covered',lambda cc: cc['excluded_cases'][0].update(case='ms%02d_b%05d' % (covered['multiset'],covered['b_index'])),'also covered')]:
        cc = copy.deepcopy(c); cc.pop('_path',None); mut(cc)
        try: H.verify(cc); err = None
        except AssertionError as exc: err = repr(exc)
        rows.append({'name':name,'error':err,'ok':err is not None and msg in err})
    return rows


def bound_record(c,h,x,root,mutate=None,record_override=None):
    it = H.task(x)
    enc = 'encode_skel_b.build_v2' if x['mode'] == 'direct' else 'encode_skel_b.build_partbatch'
    pin = {'schema':'PA19-K1-CNF-PIN-v6_3','production_contract_sha256':h,'multiset':x['multiset'],'b_index':x['b_index'],'indices':x['indices'],
           'cnf_sha256':x['expected_cnf_sha256'],'cnf_bytes':x['expected_cnf_bytes'],'recipe':H.recipe(c,x),'source_sha256':c['source_sha256'],
           'supervisor_sha256':R.SUP_SHA,'binary_authority':c['binary_authority']}
    rec = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v6_3','status':'UNKNOWN','checked':False,'integrity_status':'NOT_EVALUATED','integrity_errors':[],
           'sat_candidate':False,'halt_production':False,'group_started':False,'production_contract_sha256':h,'multiset':x['multiset'],
           'b_index':x['b_index'],'indices':x['indices'],'encoder':enc,'cnf_sha256':x['expected_cnf_sha256'],'cnf_bytes':x['expected_cnf_bytes'],
           'pre_child_pin_path':it['pin'],'runner':H.RUNNER,'count_for_scientific_coverage':True,'historical_receipt':x['historical']}
    if x['mode'] == 'partbatch': rec.update(list_sha256=x['list']['sha256'],complete_denominator=x['list']['n'],enumerator='extend_b.py')
    commit = {'schema':'PA19-K1-RECEIPT-v6_3','production_contract_sha256':h,'b_index':x['b_index'],'indices':x['indices']}
    if mutate: mutate(pin,rec,commit)
    ph = dump(root/it['pin'],pin)
    rec.setdefault('pre_child_pin_sha256',ph)
    raw = record_override if record_override is not None else (json.dumps(rec,indent=1)+'\n').encode()
    commit.setdefault('pin_sha256',ph); commit.setdefault('record_sha256',hashlib.sha256(raw).hexdigest())
    dump(root/it['commit'],commit)
    p = root/it['new_record']; p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as f: f.write(raw)
    return it


def reader_controls(root,c,h):
    rows = []
    d = [i for i in c['items'] if i['mode'] == 'direct']
    s = [i for i in c['items'] if i['mode'] == 'partbatch']
    cut = H.epochs(c)[0]
    unsat = lambda p,r,k: r.update(status='UNSAT',checked=True,integrity_status='VALIDATED',group_started=True,supervisor={'supervisor_sha256':R.SUP_SHA})
    cases = [('R0 correctly bound UNKNOWN',d[0],None,None,'UNQUALIFIED'),
             ('R1 historical receipt wrapped as primary',d[1],None,'historical','INTEGRITY_VETO'),
             ('R2 wrong contract SHA',d[2],lambda p,r,k:(p.update(production_contract_sha256='1'*64),r.update(production_contract_sha256='1'*64),k.update(production_contract_sha256='1'*64)),None,'INTEGRITY_VETO'),
             ('R3 wrong pin SHA in commit',d[3],lambda p,r,k:k.update(pin_sha256='2'*64),None,'INTEGRITY_VETO'),
             ('R4 wrong interval',s[0],lambda p,r,k:r.update(indices=[s[0]['indices'][0]+1,s[0]['indices'][1]]),None,'INTEGRITY_VETO'),
             ('R5 wrong list SHA',s[1],lambda p,r,k:r.update(list_sha256='3'*64),None,'INTEGRITY_VETO'),
             ('R6 wrong denominator',s[2],lambda p,r,k:r.update(complete_denominator=s[2]['list']['n']+1),None,'INTEGRITY_VETO'),
             ('R7 wrong runner',d[4],lambda p,r,k:r.update(runner='run_m2h_v6_1.py'),None,'INTEGRITY_VETO'),
             ('R8 coverage flag false',d[5],lambda p,r,k:r.update(count_for_scientific_coverage=False),None,'INTEGRITY_VETO'),
             ('R9 wrong historical reference',d[6],lambda p,r,k:r.update(historical_receipt=dict(d[6]['historical'],sha256='4'*64)),None,'INTEGRITY_VETO'),
             ('R10 admitted gate after the cutoff',d[7],lambda p,r,k:r.update(owner_preconstruction_gate={'admitted':True,'admission_cutoff_epoch':cut,'at_epoch':cut+1.0}),None,'INTEGRITY_VETO'),
             ('R11 pin binds the v3 supervisor',d[8],lambda p,r,k:p.update(supervisor_sha256='79c463589c9c5d60fddff7c4397a4e90339bdb0f5a0b2542c865c02a387573b3'),None,'INTEGRITY_VETO'),
             ('R12 direct record carrying list fields',d[9],lambda p,r,k:r.update(list_sha256='5'*64),None,'INTEGRITY_VETO'),
             ('R13 evidence-free UNSAT',d[10],unsat,None,'INTEGRITY_VETO')]
    def gated(kind):
        def m(p,r,k):
            unsat(p,r,k); g1,g2,nat = five_gates(cut); r.update(owner_preconstruction_gate=g1,owner_prespawn_gate=g2,native_result=nat)
            w = r['native_result']
            if kind == 'missing': del w['worker_preconstruction_gate']
            if kind == 'cutoff': w['worker_preconstruction_gate']['admission_cutoff_epoch'] = cut+1.0
            if kind == 'late': w['worker_preconstruction_gate']['at_epoch'] = cut+5.0
            if kind == 'cancelled': r['owner_cancelled'] = True
        return m
    predicate = [('R15 UNSAT missing worker preconstruction admission',d[12],gated('missing'),'required admission missing: worker_preconstruction_gate'),
                 ('R16 worker preconstruction admission with a wrong cutoff',d[13],gated('cutoff'),'admission cutoff differs: worker_preconstruction_gate'),
                 ('R17 worker preconstruction admission after the cutoff',d[14],gated('late'),'admission at/after the frozen cutoff or untimed: worker_preconstruction_gate'),
                 ('R18 UNSAT carrying an owner cancellation',d[15],gated('cancelled'),'UNSAT record carries a signal/cancellation'),
                 ('R19 all five admissions valid: predicate passes, evidence reader still rejects',d[16],gated('valid'),None)]
    sub = root/'R'; make_shadow(sub,c)
    with Rebind(sub):
        for name,x,mut,special,want in cases:
            override = (REAL/x['historical']['path']).read_bytes() if special == 'historical' else None
            bound_record(c,h,x,sub,mut,override)
            q = H.inspect(c,h,x)
            rows.append({'name':name,'id':x['id'],'state':q['state'],'errors':[str(e)[:200] for e in q.get('errors') or []][:3],'ok':q['state'] == want})
        for name,x,mut,msg in predicate:
            bound_record(c,h,x,sub,mut,None)
            q = H.inspect(c,h,x); text = ' '.join(str(e) for e in q.get('errors') or [])
            own = ('required admission missing','admission cutoff differs','admission at/after the frozen cutoff','admission phase differs',
                   'required admission not admitted','admission record invalid','UNSAT record carries a signal/cancellation')
            ok = q['state'] == 'INTEGRITY_VETO' and ((msg in text) if msg else not any(o in text for o in own))
            rows.append({'name':name,'id':x['id'],'state':q['state'],'errors':[str(e)[:240] for e in q.get('errors') or []][:3],'ok':ok})
        q = H.inspect(c,h,d[11])
        rows.append({'name':'R14 missing record','id':d[11]['id'],'state':q['state'],'ok':q['state'] == 'MISSING'})
    return rows


class StubOwner:
    """Replaces ONLY OWNER.execute for runner-flow tests; mirrors the real owner's result keys."""
    def __init__(self,c,h,mode): self.c,self.h,self.mode,self.calls = c,h,mode,[]
    def execute(self,constructor,recipe,contract_sha,source_sha,paths,deadline,admission,solver='kissat',seconds=600):
        self.calls.append(paths['id'])
        base = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v6_3','status':'UNKNOWN','checked':False,'integrity_status':'NOT_EVALUATED','integrity_errors':[],
                'sat_candidate':False,'halt_production':False,'group_started':False,'production_contract_sha256':contract_sha,
                'multiset':recipe['multiset'],'b_index':recipe['b_index'],'indices':recipe.get('indices'),
                'encoder':'encode_skel_b.build_v2' if recipe['mode'] == 'direct' else 'encode_skel_b.build_partbatch'}
        if self.mode == 'pre-pin': return dict(base,unattempted='before-pin',chunk_stop=True,resource_refusal=['CONTROL refusal'])
        x = next(i for i in self.c['items'] if i['id'] == paths['id'])
        pin = {'schema':'PA19-K1-CNF-PIN-v6_3','production_contract_sha256':contract_sha,'multiset':recipe['multiset'],'b_index':recipe['b_index'],
               'indices':recipe.get('indices'),'cnf_sha256':x['expected_cnf_sha256'],'cnf_bytes':x['expected_cnf_bytes'],'recipe':recipe,
               'source_sha256':source_sha,'supervisor_sha256':R.SUP_SHA,'binary_authority':admission['binary_authority']}
        ph = dump(paths['pin'],pin)
        base.update(cnf_sha256=x['expected_cnf_sha256'],cnf_bytes=x['expected_cnf_bytes'],pre_child_pin_sha256=ph,pre_child_pin_path=str(Path(paths['pin']).relative_to(H.L)))
        if self.mode == 'pre-worker':
            dump(paths['job'],{'schema':'PA19-NATIVE-JOB-v6_3','CONTROL':True})
            return dict(base,unattempted='after-pin-before-worker',chunk_stop=True,resource_refusal=['CONTROL refusal'])
        if self.mode in ('unknown-continue','unknown-continue-cancel'):
            if self.mode == 'unknown-continue-cancel': os.kill(os.getpid(),signal.SIGTERM)  # cancel handler runs before the runner publishes
            return dict(base,chunk_stop=False,bounded_unknown='CONTROL native limit')
        return dict(base,chunk_stop=True,resource_refusal=['CONTROL worker admission refusal'])


def run_main(c,h,sub,owner=None,max_attempts=2,formula=None,epochs=None,real_gate_admit=False,publish_signal=False):
    saved = (H.OWNER,H.formula,H.epochs,H.verify,R.create_census,R.census_for_gate,R.full_gate,sys.argv,COMMON.publish_bytes)
    orig_verify = H.verify
    def verify_real(cc):
        keep = H.L; H.L = REAL
        try: return orig_verify(cc)
        finally: H.L = keep
    try:
        if owner is not None: H.OWNER = types.SimpleNamespace(execute=owner.execute,BindingRefusal=OWNER.BindingRefusal,persist_veto=OWNER.persist_veto)
        if publish_signal:
            orig_pb, sent = COMMON.publish_bytes, []
            def pb(path,raw,stage):
                if str(path).endswith('_h6_3.json') and not sent: sent.append(1); os.kill(os.getpid(),signal.SIGTERM)
                return orig_pb(path,raw,stage)
            COMMON.publish_bytes = pb
        if formula is not None: H.formula = formula
        if epochs is not None: H.epochs = epochs
        H.verify = verify_real
        R.create_census = lambda: {'path':'cycle2/accounting-v3/CONTROL'}
        R.census_for_gate = lambda ref,force=False,lane=None: {'reference':ref,'current_data_upper_bytes':0,'age_seconds':0.0,'finished_monotonic':time.monotonic(),'record':{}}
        if real_gate_admit: R.full_gate = lambda lease,phase,lane=None,providers=None: {'admitted':True,'errors':[],'phase':phase}
        sys.argv = ['run_m2h_v6_3.py',str(c['_path']),h,'--max-attempts',str(max_attempts)]
        with Rebind(sub): H.main()
    finally:
        H.OWNER,H.formula,H.epochs,H.verify,R.create_census,R.census_for_gate,R.full_gate,sys.argv,COMMON.publish_bytes = saved
        R._CANCEL[0] = False
    chunks = sorted((sub/'cycle2/m2h6_3-chunks').glob('*'))
    return chunks[-1] if chunks else None


def flow_controls(root,c,h):
    rows, first, second = [], c['items'][0], c['items'][1]
    def summary(chunk): return json.loads((chunk/'summary.json').read_bytes()) if chunk and (chunk/'summary.json').exists() else None
    def archived(sub): return sorted(p.name.split('.claim')[0] for p in (sub/'archive/k1-v6_3-unattempted').glob('*')) if (sub/'archive/k1-v6_3-unattempted').exists() else []
    # T1 pre-pin refusal
    sub = make_shadow(root/'T1',c); own = StubOwner(c,h,'pre-pin'); ch = run_main(c,h,sub,own)
    sm = summary(ch); it = H.task(first)
    rows.append({'name':'T1 pre-pin refusal','stop':sm and sm['stop_reason'],'calls':own.calls,'archived':archived(sub),
                 'ok':sm['stop_reason'] == 'pre-pin refusal' and own.calls == [first['id']] and not (sub/it['new_record']).exists()
                      and not (sub/it['claim']).exists() and len(archived(sub)) == 1})
    # T2 pre-worker refusal after pin
    sub = make_shadow(root/'T2',c); own = StubOwner(c,h,'pre-worker'); ch = run_main(c,h,sub,own)
    sm = summary(ch); it = H.task(first)
    left = [k for k in ('pin','claim','new_record') if (sub/it[k]).exists()]
    rows.append({'name':'T2 pre-worker refusal retires own pin/job/claim','stop':sm and sm['stop_reason'],'left':left,
                 'ok':sm['stop_reason'] == 'pre-worker refusal' and not left and not os.path.exists(str(sub/it['new_record'])+'.job.json')})
    # T3 binding refusal through the REAL owner (only the gate and the formula bytes are stubbed)
    sub = make_shadow(root/'T3',c)
    ch = run_main(c,h,sub,None,formula=lambda cc,x,sk: b'p cnf 1 1\n1 0\n',real_gate_admit=True)
    sm = summary(ch); it = H.task(first)
    refusal = sorted(ch.glob('binding-refusal-*.json')) if ch else []
    flags = sorted(p.name for p in (sub/'cycle2').glob('m2k3-*.flag'))
    rows.append({'name':'T3 pre-pin binding refusal (real owner)','stop':sm and sm['stop_reason'],'receipts':[p.name for p in refusal],'flags':flags,
                 'ok':sm['stop_reason'] == 'pre-pin binding refusal' and len(refusal) == 1 and not flags and not (sub/it['pin']).exists()
                      and not (sub/it['new_record']).exists() and not (sub/it['claim']).exists()})
    # T4 worker admission refusal recorded UNKNOWN, then T5 existing UNKNOWN never retried
    sub = make_shadow(root/'T4',c); own = StubOwner(c,h,'worker-refusal'); ch = run_main(c,h,sub,own)
    sm = summary(ch); it = H.task(first)
    q = H_inspect_in(sub,c,h,first)
    rows.append({'name':'T4 worker refusal recorded UNKNOWN (UNQUALIFIED, no veto)','stop':sm and sm['stop_reason'],'state':q['state'],
                 'flags':sorted(p.name for p in (sub/'cycle2').glob('m2k3-*.flag')),
                 'ok':sm['stop_reason'] == 'worker admission refusal recorded UNKNOWN; chunk ends' and q['state'] == 'UNQUALIFIED'
                      and not list((sub/'cycle2').glob('m2k3-*.flag'))})
    before = hashlib.sha256((sub/it['new_record']).read_bytes()).hexdigest()
    own2 = StubOwner(c,h,'pre-pin'); ch2 = run_main(c,h,sub,own2)
    sm2 = summary(ch2)
    rows.append({'name':'T5 existing UNKNOWN is skipped, never retried','calls':own2.calls,
                 'ok':own2.calls == [second['id']] and hashlib.sha256((sub/it['new_record']).read_bytes()).hexdigest() == before and sm2['stop_reason'] == 'pre-pin refusal'})
    # T6 duplicate claim skipped
    sub = make_shadow(root/'T6',c); it = H.task(first)
    dump(sub/it['claim'],{'CONTROL':'claimed by another pipeline'})
    own = StubOwner(c,h,'pre-pin'); ch = run_main(c,h,sub,own)
    rows.append({'name':'T6 duplicate claim skipped','calls':own.calls,'ok':own.calls == [second['id']] and (sub/it['claim']).exists()})
    # T7 singleton lock
    sub = make_shadow(root/'T7',c)
    fd = os.open(sub/H.SINGLETON,os.O_CREAT|os.O_RDWR,0o644); fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
    try:
        own = StubOwner(c,h,'pre-pin'); ch = run_main(c,h,sub,own)
    finally:
        fcntl.flock(fd,fcntl.LOCK_UN); os.close(fd)
    rows.append({'name':'T7 second pipeline refused by singleton lock','calls':own.calls,
                 'ok':own.calls == [] and ch is not None and (ch/'singleton-refusal.json').exists() and not (sub/'cycle2/claims').exists()})
    # T8 frozen cutoff reached
    sub = make_shadow(root/'T8',c); own = StubOwner(c,h,'pre-pin')
    real_epochs = H.epochs
    ch = run_main(c,h,sub,own,epochs=lambda cc=None:(time.time()-1.0,)+real_epochs(cc)[1:])
    rows.append({'name':'T8 admission closed by the frozen policy clock','calls':own.calls,
                 'ok':own.calls == [] and ch is not None and (ch/'admission-closed.json').exists() and not (sub/'cycle2/claims').exists()})
    # T9-T11 initialization deferral: existing record veto, resource STOP, persistent flag
    for name,setup in [('T9 existing record veto defers initialization',lambda sub: bound_record(c,h,first,sub,None,(REAL/first['historical']['path']).read_bytes())),
                       ('T10 resource STOP-K1 defers initialization',lambda sub: dump(sub/'cycle2/STOP-K1',{'CONTROL':True})),
                       ('T11 persistent HALT flag defers initialization',lambda sub: dump(sub/'cycle2/m2k3-HALT.flag',{'CONTROL':True}))]:
        sub = make_shadow(root/name.split()[0],c)
        with Rebind(sub): setup(sub)
        own = StubOwner(c,h,'pre-pin'); ch = run_main(c,h,sub,own)
        rows.append({'name':name,'calls':own.calls,'ok':own.calls == [] and ch is not None and (ch/'initialization-deferred.json').exists()})
    # T12 signal inside the publication window: deferred, the published record stays consistent, the runner then stops
    sub = make_shadow(root/'T12',c); own = StubOwner(c,h,'unknown-continue'); ch = run_main(c,h,sub,own,max_attempts=3,publish_signal=True)
    sm = summary(ch); it = H.task(first); q = H_inspect_in(sub,c,h,first)
    rec = json.loads((sub/it['new_record']).read_bytes()) if (sub/it['new_record']).exists() else {}
    rows.append({'name':'T12 signal in the publication window is deferred; runner stops','calls':own.calls,'stop':sm and sm['stop_reason'],'state':q['state'],
                 'ok':own.calls == [first['id']] and sm['stop_reason'] == 'deadline/cancellation; no new native' and q['state'] == 'UNQUALIFIED'
                      and 'owner_cancelled' not in rec and not list((sub/'cycle2').glob('m2k3-*.flag'))})
    # T13 cancellation after the owner returned and before publication: UNKNOWN + persistent HALT, never qualified
    sub = make_shadow(root/'T13',c); own = StubOwner(c,h,'unknown-continue-cancel'); ch = run_main(c,h,sub,own,max_attempts=3)
    sm = summary(ch); it = H.task(first)
    rec = json.loads((sub/it['new_record']).read_bytes()) if (sub/it['new_record']).exists() else {}
    flags = sorted(p.name for p in (sub/'cycle2').glob('m2k3-*.flag'))
    rows.append({'name':'T13 cancellation before publication marks UNKNOWN + HALT','stop':sm and sm['stop_reason'],'flags':flags,
                 'ok':own.calls == [first['id']] and rec.get('owner_cancelled') is True and rec.get('status') == 'UNKNOWN'
                      and rec.get('halt_production') is True and flags == ['m2k3-HALT.flag'] and sm['stop_reason'] == 'persistent veto'})
    return rows


def H_inspect_in(sub,c,h,x):
    with Rebind(sub): return H.inspect(c,h,x)


def inventory_controls(root,c,h):
    sub = make_shadow(root/'I',c)
    split_case = next((i['multiset'],i['b_index']) for i in c['items'] if i['mode'] == 'partbatch')
    split_ids = [i['id'] for i in c['items'] if (i['multiset'],i['b_index']) == split_case]
    direct_id = next(i['id'] for i in c['items'] if i['mode'] == 'direct')
    qualified = set(split_ids[:-1]) | {direct_id}
    saved, argv = H.inspect, sys.argv
    orig_verify = H.verify
    try:
        H.inspect = lambda cc,hh,x: {'state':'QUALIFIED' if x['id'] in qualified else 'MISSING'}
        H.verify = lambda cc: orig_verify(cc)
        sys.argv = ['final_m2h_inventory_v6_3.py',str(c['_path']),h]
        with Rebind(sub,(INV,)): INV.main()
    finally:
        H.inspect, sys.argv = saved, argv
    out = json.loads(sorted((sub/'cycle2').glob('m2h-inventory-*.json'))[-1].read_bytes())
    return [{'name':'I1 split case with one MISSING interval stays open','covered':out['covered_cases'],'open':out['open_cases'],
             'ready':out['final_component_ready'],'ok':out['covered_cases'] == 1 and out['open_cases'] == out['cases']-1 and out['final_component_ready'] is False}]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); args = ap.parse_args()
    assert E.digest(args.contract) == args.sha256
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        c = COMMON.read(args.contract); H.verify(c); c['_path'] = Path(args.contract).resolve()
    root = REAL/'cycle2'/('m2h-v6_3-controls-%d' % time.time_ns()); root.mkdir()
    started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    fams = {}
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):  # one token; tests below never nest tokens
        fams['G_runtime_gates'] = gate_controls(root)
    fams['C_capacity'] = capacity_controls(root)
    fams['O_owner'] = owner_controls(root,c,args.sha256)+settlement_controls(root,c,args.sha256)
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        fams['R_exact_reader'] = reader_controls(root,c,args.sha256)
    fams['T_runner_flow'] = flow_controls(root,c,args.sha256)
    fams['I_inventory'] = inventory_controls(root,c,args.sha256)
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        fams['V_exact_universe'] = universe_controls(c)
    allok = all(r['ok'] for rows in fams.values() for r in rows)
    out = {'schema':'PA19-M2H-V6_3-CONTROLS-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'control_source_sha256':E.digest(SELF),'contract':str(c['_path'].relative_to(REAL)),'contract_sha256':args.sha256,
        'sources':{k:E.digest(REAL/k) for k in c['source_sha256']},'families':fams,'all_expected':allok,'native_children_started':0,
        'production_coverage':False,'scope':'private shadow lanes; stubs only for the named component; no solver/checker/native child'}
    dest = root/'receipt.json'
    with dest.open('x') as f: json.dump(out,f,indent=1,default=str); f.write('\n')
    print(dest,E.digest(dest),'all_expected',allok,flush=True)
    for fam,rows in fams.items():
        for r in rows: print(fam,r['name'],'ok' if r['ok'] else 'FAIL',flush=True)


if __name__ == '__main__':
    R.install_handlers()
    s = os.statvfs(REAL); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
    main()  # each family/step acquires its own single lane token; no outer token, so tokens never nest
