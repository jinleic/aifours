#!/usr/bin/env python3
"""Corrected v3 PRIVATE controls; excluded from scientific coverage and executed only after parent GO.
Uses one real lane token, <=2 compute processes, frozen binary authorities, local reviewed r3 adapter and absolute
argv. No SIGKILL, deletion, shared-supervisor edit, RC3 rerun or automatic retry. Synthetic records test readers only.
Definite nonclean stops are distinguished from measurement uncertainty; the actual supervisor key is killpg_error.
"""
import argparse
import ast
import copy
import fcntl
import hashlib
import inspect as source_inspect
import io
import json
import os
import signal
import stat
import sys
import threading
import time
from pathlib import Path

import lane_new_data_accounting as A
import m2_item_owner_v3 as O
import m2_ms09_contract_v3 as C
import m2_ms09_evidence_v3 as E
import m2_native_staged_v3 as N
import m2_supervised_runtime_v3 as R
import run_m2_ms09_k1_v3 as TX

L = C.LANE
SELF = Path(__file__).resolve()
UNSAT = b'p cnf 1 2\n1 0\n-1 0\n'
SAT = b'p cnf 2 1\n1 2 0\n'


def dump(p,obj):
    p = Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f: json.dump(obj,f,indent=1)


def scope(root):
    tok = root/'cycle2/tokens'; tok.mkdir(parents=True)
    (tok/'COUNT').write_text('2\n')
    for name in ['t%d' % i for i in range(8)]+['bigmem']: (tok/name).write_bytes(b'')
    (root/'cycle2/accounting-v3').mkdir(parents=True)


def lock_free(p):
    fd = os.open(p,os.O_RDWR)
    try:
        try: fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: return False
        fcntl.flock(fd,fcntl.LOCK_UN); return True
    finally: os.close(fd)


def census_ref(root,usage=1,age=0.0):
    rec = {'schema':'PA19-ALLOCATED-CENSUS-v3','started_monotonic':time.monotonic()-age,'finished_monotonic':time.monotonic()-age,
           'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'ttl_seconds':R.CENSUS_TTL,
           'data':{'known':True,'stat_errors':[],'new_data_usage_upper_bytes':usage}}
    p = root/'cycle2/accounting-v3'/('control-%d.json' % time.time_ns())
    raw = (json.dumps(rec,indent=1)+'\n').encode(); p.write_bytes(raw)
    return {'path':str(p.relative_to(root)),'sha256':hashlib.sha256(raw).hexdigest()}


def authority(solver='/opt/homebrew/bin/kissat'):
    return {'python':{'path':os.path.abspath(sys.executable),'sha256':R.digest(os.path.abspath(sys.executable))},
            'solver':{'path':solver,'sha256':R.digest(solver)},
            'checker':{'path':str(L/'tools/drat-trim/drat-trim'),'sha256':R.digest(L/'tools/drat-trim/drat-trim')}}


def lease(root,deadline,owner=None,usage=1,age=0.0):
    return {'owner_pid':owner or os.getpid(),'projected_growth_bytes':R.ITEM_GROWTH,'census_reference':census_ref(root,usage,age),
            'whole_plan_remaining_bound_bytes':R.ALL_PLANNED_RETAINED_BOUND,'force_census_refresh':False,'binary_authority':authority(),
            'group_rss_cap_bytes':R.GROUP_RSS_CAP,'busy_units':2,'lane_busy_ceiling':4,
            'chunk_deadline_monotonic':deadline,'item_deadline_monotonic':deadline}


def providers(**changes):
    out = {'count':lambda:2,'free':lambda:R.BASE_GATE+R.ITEM_GROWTH,'clock':lambda:0,
           'rss':lambda:{'known':True,'rss_bytes':0,'current_group_and_owner_bytes':0},
           'binaries':lambda:{k:{'path':v['path'],'expected_sha256':v['sha256'],'observed_sha256':v['sha256'],'matches':True}
                               for k,v in authority().items()},
           'census':lambda:{'reference':{'path':'control','sha256':'0'*64},'age_seconds':0,'finished_monotonic':time.monotonic(),
                            'current_data_upper_bytes':1}}
    for k,v in changes.items(): out[k] = v if callable(v) else (lambda value=v:value)
    return out


def child(mode,path,extra):
    cfg = json.loads(Path(path).read_bytes())
    if mode == 'mark':
        dump(cfg['marker'],{'new_child':True}); return
    if mode == 'late':
        signal.signal(signal.SIGTERM,signal.SIG_IGN)
        dump(cfg['marker'],{'pid':os.getpid()})
        time.sleep(2.0); return
    if mode == 'floor-worker':
        dump(cfg['worker_result'],cfg['native']); return
    if mode == 'emit':
        kind = extra[0]
        if (cfg.get('start_failure') or cfg.get('thread_failure')) and kind == 'solver':
            signal.signal(signal.SIGTERM,signal.SIG_IGN)
            dump(cfg['marker'],{'pid':os.getpid()}); time.sleep(2.0); return
        with open(extra[1],'rb') as f: f.read()
        if kind == 'solver':
            with open(extra[2],'wb') as f: f.write(b'')
            out,rc = cfg.get('solver_lines','s UNSATISFIABLE\n'),20
        else:
            sys.stdin.buffer.read(); out,rc = cfg.get('checker_lines','s VERIFIED\n'),cfg.get('checker_rc',0)
        sys.stdout.write(out); sys.stdout.flush(); raise SystemExit(rc)
    assert mode == 'pipeline'
    raw = SAT if cfg.get('real_negative') else UNSAT
    original = R.full_gate
    R.full_gate = lambda item,phase,*a,**k: original(item,phase,Path(cfg['scope']),providers(
        free=lambda:(lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L)),rss=lambda:R.lane_rss(L,os.getpgrp(),item['owner_pid'])))
    if cfg.get('feed_fault'):
        base = N.feed_cnf
        def short(fifo,data,record,stop,deadline):
            side = 'checker' if 'checker' in str(fifo) else 'solver'
            base(fifo,data[:len(data)//2] if side == cfg['feed_fault'] else data,record,stop,deadline)
        N.feed_cnf = short
    if cfg.get('fd_error'):
        side,operation = cfg['fd_error'].split('-'); target = Path(cfg['job']['workdir'])/(side+'-cnf.fifo')
        ow,oc = os.write,os.close
        def matches(fd):
            try: return os.fstat(fd).st_ino == target.stat().st_ino
            except OSError: return False
        def write(fd,data):
            if operation == 'write' and matches(fd): raise OSError('CONTROL CNF write failure')
            return ow(fd,data)
        def close(fd):
            fail = operation == 'close' and matches(fd); oc(fd)
            if fail: raise OSError('CONTROL CNF close failure after close')
        os.write,os.close = write,close
    if cfg.get('thread_failure'):
        start = threading.Thread.start
        def failing(thread):
            if thread._target is N.collector:
                time.sleep(0.2); raise RuntimeError('CONTROL collector start failure')
            return start(thread)
        threading.Thread.start = failing
    def commands(paths):
        if cfg.get('real_positive'):
            return ([N.KISSAT,'-q','-f','--seed=1','--time=600',paths['solver-cnf.fifo'],paths['proof.fifo']],[N.DT,paths['checker-cnf.fifo'],'-i','-t','1200'])
        solver = [sys.executable,'-B',str(SELF),'--child','emit',str(path),'solver',paths['solver-cnf.fifo'],paths['proof.fifo']]
        checker = [N.DT,paths['checker-cnf.fifo'],'-i','-t','1200'] if cfg.get('real_negative') else [sys.executable,'-B',str(SELF),'--child','emit',str(path),'checker',paths['checker-cnf.fifo']]
        return solver,checker
    def hook(p):
        time.sleep(0.2); raise RuntimeError('CONTROL post-Popen exception')
    dump(cfg['result'],N.pipeline(raw,cfg['job'],commands,hook if cfg.get('start_failure') else None))


def native_case(root,name,**options):
    folder = root/name; folder.mkdir(); priv = folder/'scope'; scope(priv)
    item = lease(priv,time.monotonic()+8000)
    cfg = dict(options,scope=str(priv),result=str(folder/'worker.json'),marker=str(folder/'marker.json'),
               job={'solver':'kissat','solver_seconds':600,'checker_seconds':1200,'lease':item,'workdir':str(folder/'fifo')})
    cp = folder/'config.json'; dump(cp,cfg)
    rec_path = folder/('absent/supervisor.json' if options.get('receipt_error') else 'supervisor.json')
    q_path = folder/('absent/quarantine.json' if options.get('receipt_error') else 'quarantine.json')
    original,sup = R.full_gate,R.supervisor().supervise
    R.full_gate = lambda x,phase,lane=None: original(x,phase,priv,providers(free=lambda:(lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L)),
        rss=lambda:R.lane_rss(L,owner=os.getpid())))
    if options.get('receipt_error'):
        def short_grace(*args,**kwargs):
            kwargs['grace'] = 0.05; return sup(*args,**kwargs)
        R.supervisor().supervise = short_grace
    observations,done = [],threading.Event()
    def watch():
        while not done.is_set():
            if (folder/'marker.json').exists():
                pid = json.loads((folder/'marker.json').read_bytes())['pid']
                state,_,_ = R.supervisor().probe(pid)
                observations.append({'native_state':state,'held_t0_free':lock_free(priv/'cycle2/tokens/t0')})
            time.sleep(0.02)
    th = threading.Thread(target=watch,daemon=True); th.start()
    try:
        with R.Capacity(time.monotonic()+8000,priv) as cap:
            item['owner_pid'] = os.getpid()
            rec,gate = cap.supervise([sys.executable,'-B',str(SELF),'--child','pipeline',str(cp)],'CONTROL-'+name,item,rec_path,q_path)
            assert rec is not None and gate['admitted'] and cap.safe and cap.settlement['leader_reaped'] is True, (name,gate,cap.settlement)
    finally:
        done.set(); th.join(); R.full_gate = original; R.supervisor().supervise = sup
    result = json.loads((folder/'worker.json').read_bytes())
    if options.get('start_failure') or options.get('thread_failure'):
        alive = [x for x in observations if x['native_state'] == 'alive']
        assert alive and all(x['held_t0_free'] is False for x in alive), 'owned token released while native alive'
        assert rec.get('trip_reason') and (rec.get('uncertain') is True or (rec.get('stop') or {}).get('listing_ok') is True), rec
        if options.get('receipt_error'): assert rec.get('record_write_error') and rec.get('cleanup_exception')
    assert all(lock_free(priv/'cycle2/tokens'/('t%d' % i)) for i in range(2))
    dump(folder/'control-receipt.json',{'result':result,'supervisor':rec,'observations':observations,'production_coverage':False})
    return {'name':name,'status':result['status'],'integrity_status':result['integrity_status'],
            'receipt':str((folder/'control-receipt.json').relative_to(L)),'sha256':E.digest(folder/'control-receipt.json')}


def gate_controls(root):
    priv = root/'gate-scope'; scope(priv); base = lease(priv,5000); rows = []
    assert R.full_gate(copy.deepcopy(base),'solver',priv,providers())['admitted']
    tests = [('free-minus1',{'free':R.BASE_GATE+R.ITEM_GROWTH-1}),('count3',{'count':3}),('count0',{'count':0}),
             ('rss-unknown',{'rss':{'known':False}}),('deadline',{'clock':3000}),
             ('census-stale',{'census':{'reference':{},'age_seconds':R.CENSUS_TTL+1,'finished_monotonic':0,'current_data_upper_bytes':1}}),
             ('census-unknown',{'census':lambda:(_ for _ in ()).throw(RuntimeError('CONTROL census unknown'))}),
             ('data-plus-margin',{'census':{'reference':{},'age_seconds':0,'finished_monotonic':time.monotonic(),
                'current_data_upper_bytes':R.DATA_CAP-R.ALL_PLANNED_RETAINED_BOUND-R.OTHER_WRITER_MARGIN+1}}),
             ('binary-drift',{'binaries':{'python':{'matches':True},'solver':{'matches':False},'checker':{'matches':True}}})]
    for name,change in tests:
        g = R.full_gate(copy.deepcopy(base),'solver',priv,providers(**change)); assert not g['admitted']; rows.append({'name':name,'errors':g['errors']})
    for name in ('STOP-m2r12','m2k3-SAT.flag','m2k3-INTEGRITY.flag','m2k3-HALT.flag','m2k3-QUARANTINE.flag'):
        p = root/('stop-'+name.replace('.','_')); scope(p); (p/'cycle2'/name).write_text('CONTROL')
        g = R.full_gate(copy.deepcopy(base),'solver',p,providers()); assert not g['admitted']; rows.append({'name':name,'errors':g['errors']})
    # Real cache semantics: fresh <=600s accepted, older refreshes by an actual exact census of a tiny private scope.
    fresh = R.census_for_gate(census_ref(priv,7,10),False,priv); assert fresh['current_data_upper_bytes'] == 7
    renewed = R.census_for_gate(census_ref(priv,7,R.CENSUS_TTL+5),False,priv)
    assert renewed['reference'] != fresh['reference'] and renewed['age_seconds'] <= R.CENSUS_TTL
    rows.append({'name':'real-census-cache-and-refresh','fresh_age':fresh['age_seconds'],'renewed_reference':renewed['reference']})
    return rows


def postwait_controls(root):
    rows = []
    for change in ('STOP','floor','binary','data'):
        folder = root/('postwait-'+change); folder.mkdir(); priv = folder/'scope'; scope(priv)
        token = os.open(priv/'cycle2/tokens/t0',os.O_RDWR); fcntl.flock(token,fcntl.LOCK_EX)
        (priv/'cycle2/tokens/COUNT').write_text('1\n')
        free = [R.BASE_GATE+R.ITEM_GROWTH]; drift = [False]; usage = [1]; original = R.full_gate; result = {}
        R.full_gate = lambda item,phase,lane=None: original(item,phase,priv,providers(free=lambda:free[0],
            binaries=lambda:{k:{'matches':not (drift[0] and k == 'solver')} for k in ('python','solver','checker')},
            census=lambda:{'reference':{},'age_seconds':0,'finished_monotonic':time.monotonic(),'current_data_upper_bytes':usage[0]}))
        config = folder/'marker.json'; dump(config,{'marker':str(folder/'FORBIDDEN.json')})
        entered,finished = threading.Event(),threading.Event()
        def admit():
            try:
                entered.set()
                with R.Capacity(time.monotonic()+8000,priv) as cap:
                    item = lease(priv,time.monotonic()+8000); item['owner_pid'] = os.getpid()
                    rec,gate = cap.supervise([sys.executable,'-B',str(SELF),'--child','mark',str(config)],'CONTROL-postwait',item,
                                             folder/'supervisor.json',folder/'quarantine.json')
                    result.update(rec=rec,gate=gate)
            except BaseException as exc: result['error'] = repr(exc)
            finally: finished.set()
        th = threading.Thread(target=admit,daemon=True); th.start()
        try:
            assert entered.wait(5); time.sleep(0.2)
            if change == 'STOP': (priv/'cycle2/STOP-m2r12').write_text('CONTROL during wait')
            elif change == 'floor': free[0] -= 1
            elif change == 'binary': drift[0] = True
            else: usage[0] = R.DATA_CAP
            fcntl.flock(token,fcntl.LOCK_UN); os.close(token); token = None
            assert finished.wait(5) and result.get('rec') is None and not result['gate']['admitted'], result
            assert not (folder/'FORBIDDEN.json').exists() and not (folder/'supervisor.json').exists()
            rows.append({'change':change,'errors':result['gate']['errors'],'new_children':0})
        finally:
            if token is not None: fcntl.flock(token,fcntl.LOCK_UN); os.close(token)
            R.full_gate = original
    return rows


def late_reap_control(root):
    folder = root/'late-leader-reap'; folder.mkdir(); priv = folder/'scope'; scope(priv)
    config = folder/'late.json'; dump(config,{'marker':str(folder/'marker.json')})
    original,sup = R.full_gate,R.supervisor().supervise
    R.full_gate = lambda item,phase,lane=None: original(item,phase,priv,providers(free=lambda:(lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L)),
        rss=lambda:R.lane_rss(L,owner=os.getpid())))
    def short(*args,**kwargs):
        kwargs['grace'] = 0.05; return sup(*args,**kwargs)
    R.supervisor().supervise = short
    item = lease(priv,time.monotonic()+8000)
    try:
        with R.Capacity(time.monotonic()+8000,priv) as cap:
            item['owner_pid'] = os.getpid(); item['item_deadline_monotonic'] = item['chunk_deadline_monotonic']
            def external_stop():
                while not (folder/'marker.json').exists(): time.sleep(0.02)
                os.kill(os.getpid(),signal.SIGTERM)  # supervise_r3's own handler records an external stop
            threading.Thread(target=external_stop,daemon=True).start()
            rec,gate = cap.supervise([sys.executable,'-B',str(SELF),'--child','late',str(config)],'CONTROL-late-reap',item,
                                     folder/'supervisor.json',folder/'quarantine.json')
            assert rec is not None and str(rec.get('trip_reason')).startswith('external SIGTERM'), rec
            assert rec.get('quarantine_record') and (rec.get('stop') or {}).get('survivors'), 'leader did not outlive the stop grace'
            assert cap.settlement['leader_reaped'] and cap.settlement['explicit_owned_popen_wait'] and cap.children[0].returncode == 0
            assert R._CANCEL[0] is False
    finally: R.full_gate,R.supervisor().supervise = original,sup
    return {'record':rec,'settlement':cap.settlement}


def safety_dominance_control():
    native = {'schema':'PA19-NATIVE-RESULT-v3','status':'UNKNOWN','integrity_status':'NOT_EVALUATED','bounded_unknown':'native wall',
              'halt_production':False,'sat_candidate':False}
    rec = {'completed_cleanly':False,'trip_reason':'free bytes 1 below floor 12000000000 at completion','uncertain':False,'stop':{}}
    settle = {'group_quiescent':True,'leader_reaped':True,'explicit_owned_popen_wait':True}
    out = O.apply_worker_outcome({'status':'UNKNOWN','checked':False,'halt_production':False},native,rec,settle)
    assert out['status'] == 'UNKNOWN' and out['halt_production'] is True and out['safety_veto']
    good = O.apply_worker_outcome({'status':'UNKNOWN','checked':False,'halt_production':False},native,
        {'completed_cleanly':True,'trip_reason':None,'uncertain':False,'stop':None},settle)
    assert good['status'] == 'UNKNOWN' and good['halt_production'] is False
    killpg = O.supervisor_safety_errors({'completed_cleanly':False,'trip_reason':'wall cap','uncertain':False,'stop':{'killpg_error':'CONTROL'}},settle)
    assert any('killpg_error' in e for e in killpg)
    return {'floor_plus_worker_UNKNOWN':out['safety_veto'],'actual_killpg_error_key':killpg}


def unknown_controls(root):
    h = hashlib.sha256(UNSAT).hexdigest(); ph = hashlib.sha256(b'').hexdigest()
    feed = {'bytes':len(UNSAT),'sha256':h,'complete':True,'close_ok':True,'error':None}
    base = {'cnf_bytes':len(UNSAT),'cnf_sha256':h,'solver_rc':20,'checker_rc':0,
        'solver_collector':{'complete':True,'error':None,'status_lines':['s UNSATISFIABLE']},
        'checker_collector':{'complete':True,'error':None,'status_lines':['s VERIFIED']},
        'cnf_feeds':{'solver':copy.deepcopy(feed),'checker':copy.deepcopy(feed)},
        'proof_stream':{'reader_complete':True,'reader_error':None,'raw_bytes':0,'raw_sha256':ph},
        'proof_delivery':{'bytes':0,'sha256':ph,'complete':True,'close_ok':True,'error':None}}
    assert N.outcome(base)['status'] == 'UNSAT'
    rows = []
    for side in ('solver','checker'):
        for key,value in (('bytes',len(UNSAT)-1),('sha256','0'*64),('complete',False),('close_ok',False),('error','CONTROL')):
            r = copy.deepcopy(base); r['cnf_feeds'][side][key] = value; o = N.outcome(r)
            assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'INVALID' and o['halt_production']; rows.append(side+'-'+key)
    for lines in (['s NOT VERIFIED'],['s VERIFIED']*2,[' s VERIFIED'],[]):
        r = copy.deepcopy(base); r['checker_collector']['status_lines'] = lines; o = N.outcome(r)
        assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'INVALID'; rows.append('checker-'+repr(lines))
    r = copy.deepcopy(base); r['checker_collector']['status_lines'] = ['s TIMEOUT']; o = N.outcome(r)
    assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'NOT_EVALUATED' and not o['halt_production']
    r = copy.deepcopy(base); r['solver_rc'] = 10; r['solver_collector']['status_lines'] = ['s SATISFIABLE']; o = N.outcome(r)
    assert o['status'] == 'UNKNOWN' and o['sat_candidate'] and o['halt_production']
    for raw,expected in ((b's VERIFIED\r\n',['s VERIFIED']),(b' s VERIFIED\n',[]),(b's NOT VERIFIED\n',['s NOT VERIFIED'])):
        out = {}; N.collector(io.BytesIO(raw),out); assert out['complete'] and out['status_lines'] == expected
    return rows


def shadow_lane(root,name,contract):
    """Private metadata lane: copied frozen sources, read-only symlinked inputs, no proof/CNF copies."""
    shadow = root/name; shadow.mkdir()
    def input_link(rel):
        if Path(rel).is_absolute(): return
        target = shadow/rel
        if target.exists(): return
        target.parent.mkdir(parents=True,exist_ok=True)
        os.symlink(str(L/rel),target)  # readonly metadata input, never a proof/CNF copy
    for rel in contract['source_sha256']:
        p = shadow/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes((L/rel).read_bytes())
    for rel in (contract['skeleton_path'],contract['map_path'],contract['phase_path']): input_link(rel)
    for ca0 in contract['cases']:
        if ca0.get('list'): input_link(ca0['list']['path'])
    for ref in contract['frozen_original_records']: input_link(ref['path'])
    for ref in contract['calibration_reservations']:
        for field in ('record','pin','calibration_contract'): input_link(ref[field])
        for rel in ref['source_sha256']: input_link(rel)
    return shadow


def coverage_controls(root,contract,h):
    C.verify_sources(contract)
    rows = []
    def reject(name,edit):
        bad = copy.deepcopy(contract); edit(bad)
        try: C.verify_sources(bad)
        except (AssertionError,KeyError,ValueError,StopIteration): rows.append(name); return
        raise AssertionError('coverage/source mutation survived: '+name)
    reject('unknown-schema',lambda c:c.update(schema='UNKNOWN'))
    reject('missing-case',lambda c:c['cases'].pop())
    reject('pending-order-reversed',lambda c:c['pending_order'].reverse())
    reject('validation-order-reversed',lambda c:c['validation_order'].reverse())
    reject('validation-missing-one',lambda c:c['validation_tasks'].pop())
    reject('source-set-missing-one',lambda c:c['source_sha256'].pop(next(iter(c['source_sha256']))))
    ca = next(x for x in contract['cases'] if x['intervals'])
    bi = ca['b_index']
    reject('interval-gap',lambda c:c['cases'][bi]['intervals'].pop())
    reject('interval-overlap',lambda c:c['cases'][bi]['intervals'].append(copy.deepcopy(c['cases'][bi]['intervals'][-1])))
    reject('wrong-final-partial',lambda c:c['cases'][bi]['intervals'][-1]['indices'].__setitem__(1,c['cases'][bi]['intervals'][-1]['indices'][1]+1))
    reject('denominator-plus-one',lambda c:c['cases'][bi]['list'].__setitem__('n',c['cases'][bi]['list']['n']+1))
    no = copy.deepcopy(contract['cases'][3]); no['b_index'] = 0
    assert not C.structural_acceptance(contract,no)['accepted']; rows.append('no-generic-empty-acceptance')
    assert not hasattr(C,'parent_reuse'); rows.append('withdrawn-reuse-has-no-alias')
    dest,stage = root/'atomic.json',root/'atomic-stage'
    C.publish_json(dest,{'unchanged':1},stage); before = dest.read_bytes()
    try: C.publish_json(dest,{'must_not_replace':1},stage)
    except FileExistsError: pass
    else: raise AssertionError('atomic publication overwrote')
    assert dest.read_bytes() == before; rows.append('creation-collision-no-overwrite')
    assert not C.inventory(contract,h)['final_ms09_acceptance_ready']; rows.append('no-historical-final-vacuity')
    # Actual publication function -> reader -> resume veto in an isolated metadata shadow, no scientific files.
    shadow = shadow_lane(root,'transaction-shadow',contract)
    old_c,old_tx = C.LANE,TX.L
    try:
        C.LANE = TX.L = shadow
        it = C.new_task(70,[0,24]); ca = copy.deepcopy(contract['cases'][70])
        expected = next(x['expected'] for x in contract['validation_tasks'] if x['id'] == it['id'])
        recipe = {'mode':'partbatch','multiset':9,'b_index':70,'indices':[0,24],
            'skeleton_path':contract['skeleton_path'],'skeleton_sha256':contract['skeleton_sha256'],
            'encoder_sha256':contract['source_sha256']['src/encode_skel_b.py'],'list_path':ca['list']['path'],
            'list_sha256':ca['list']['sha256'],'complete_denominator':ca['list']['n']}
        pin = {'schema':'PA19-K1-CNF-PIN-v3','production_contract_sha256':h,'multiset':9,'b_index':70,'indices':[0,24],
               'recipe':recipe,'binary_authority':contract['binary_authority'],'cnf_sha256':expected['cnf_sha256'],'cnf_bytes':expected['cnf_bytes'],
               'source_sha256':contract['source_sha256'],'supervisor_sha256':R.SUP_SHA}
        ph = C.publish_json(shadow/it['pin'],pin,shadow/'stage')
        dump(shadow/'cycle2'/'m2k3-INTEGRITY.flag',{'status':'UNKNOWN','veto':'INTEGRITY','CONTROL':True})
        result = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v3','status':'UNKNOWN','integrity_status':'INVALID','integrity_errors':['CONTROL invalid proof'],'sat_candidate':False,'checked':False,'halt_production':True,
                  'cnf_sha256':pin['cnf_sha256'],'cnf_bytes':pin['cnf_bytes'],'pre_child_pin_sha256':ph,
                  'native_result':{'status':'UNKNOWN','integrity_status':'INVALID','checker_collector':{'status_lines':['s NOT VERIFIED']}}}
        TX.publish_item(result,contract,h,ca,it,shadow/'stage')
        q = C.inspect_new(contract,h,ca,it)
        assert q['state'] == 'INTEGRITY_VETO' and any('persistent INVALID integrity/verdict' in e for e in q['errors']), q
        snap = C.inventory(contract,h)
        assert snap['integrity_issues'] and not snap['final_ms09_acceptance_ready']
        original_cap,original_owner,argv = R.Capacity,O.execute,sys.argv
        class AlreadyHeld:
            def __enter__(self): return self
            def __exit__(self,*args): pass
        calls = []
        def forbidden_native(*args,**kwargs):
            calls.append('NATIVE MUST NOT START'); raise AssertionError('veto failed')
        try:
            R.Capacity = lambda *args,**kwargs:AlreadyHeld()  # REAL outer control token remains held
            O.execute = forbidden_native
            sys.argv = [str(L/'src/run_m2_ms09_k1_v3.py'),str(L/contract['_control_contract_path']),h,'--max-attempts','1']
            TX.main()
        finally:
            R.Capacity,O.execute,sys.argv = original_cap,original_owner,argv
        assert not calls and list((shadow/'cycle2'/'m2k3-chunks').glob('*/initialization-deferred.json'))
        rows.append('actual-publisher-reader-inventory-resumed-runner-invalid-veto')
        assert b'NOT VERIFIED' in (shadow/it['new_record']).read_bytes()
        for variant in ('positive-UNKNOWN','omit-pin','omit-commit','bad-record-sha','boolean-pin-id','bad-CNF-sha','unknown-pin-schema','unknown-pipeline','interrupted-before-primary'):
            fixture = dict(it)
            prefix = Path('transaction-fixtures')/variant
            fixture.update(new_record=str(prefix/'record.json'),pin=str(prefix/'pin.json'),commit=str(prefix/'commit.json'))
            pp = copy.deepcopy(pin)
            if variant == 'boolean-pin-id': pp['b_index'] = True
            if variant == 'bad-CNF-sha': pp['cnf_sha256'] = '0'*64
            if variant == 'unknown-pin-schema': pp['schema'] = 'UNKNOWN'
            ph2 = E.digest(shadow/it['pin']) if variant == 'omit-pin' else C.publish_json(shadow/fixture['pin'],pp,shadow/'stage')
            rr = dict(result,status='UNKNOWN',integrity_status='NOT_EVALUATED',integrity_errors=[],sat_candidate=False,checked=False,halt_production=False,native_result={},pre_child_pin_sha256=ph2)
            if variant == 'unknown-pipeline': rr['pipeline_schema'] = 'UNKNOWN'
            rb = (json.dumps(rr,indent=1)+'\n').encode()
            cc = {'schema':'PA19-K1-RECEIPT-v3','production_contract_sha256':h,'b_index':70,'indices':[0,24],
                  'pin_sha256':ph2,'record_sha256':'0'*64 if variant == 'bad-record-sha' else hashlib.sha256(rb).hexdigest()}
            if variant != 'omit-commit': C.publish_json(shadow/fixture['commit'],cc,shadow/'stage')
            if variant != 'interrupted-before-primary': C.publish_bytes(shadow/fixture['new_record'],rb,shadow/'stage')
            qq = C.inspect_new(contract,h,ca,fixture)
            expected_state = 'UNQUALIFIED' if variant == 'positive-UNKNOWN' else ('MISSING' if variant == 'interrupted-before-primary' else 'INTEGRITY_VETO')
            assert qq['state'] == expected_state, (variant,qq)
            rows.append('transaction-'+variant)
    finally:
        C.LANE,TX.L = old_c,old_tx
    return rows


def accounting_controls(root):
    folder = root/'accounting'; folder.mkdir()
    regular = folder/'metadata.bin'; regular.write_bytes(b'x'*4096)
    os.link(regular,folder/'metadata-hardlink.bin'); os.symlink(str(regular),folder/'metadata-symlink')
    os.mkfifo(folder/'empty.fifo')
    got = A.account(folder)
    entries = [folder]+list(folder.iterdir())
    logical = sum(p.lstat().st_size for p in entries)
    allocated = sum(p.lstat().st_blocks*512 for p in entries)
    assert got['known'] and got['charged_logical_bytes'] == logical and got['charged_allocated_bytes'] == allocated
    assert stat.S_ISFIFO((folder/'empty.fifo').lstat().st_mode)
    return {'logical_bytes':logical,'allocated_bytes':allocated,'hardlinks_charged_per_path':True,'fifo_zero_bytes':(folder/'empty.fifo').lstat().st_size}



def no_retry_control(root,contract,h):
    """Actual runner over a private shadow: an existing UNKNOWN first-attempt receipt is skipped, never retried."""
    shadow = shadow_lane(root,'no-retry-shadow',contract)
    old = (C.LANE,TX.L,R.create_census,R.census_for_gate,R.Capacity,O.execute,sys.argv)
    calls = []
    try:
        C.LANE = TX.L = shadow
        first,second = contract['pending_order'][:2]
        byid = {it['id']:(ca,it) for ca in contract['cases'] for it in ca['intervals']}
        ca,it = byid[first]
        recipe = {'mode':'partbatch','multiset':9,'b_index':ca['b_index'],'indices':it['indices'],'skeleton_path':contract['skeleton_path'],
            'skeleton_sha256':contract['skeleton_sha256'],'encoder_sha256':contract['source_sha256']['src/encode_skel_b.py'],
            'list_path':ca['list']['path'],'list_sha256':ca['list']['sha256'],'complete_denominator':ca['list']['n']}
        pin = {'schema':'PA19-K1-CNF-PIN-v3','production_contract_sha256':h,'multiset':9,'b_index':ca['b_index'],'indices':it['indices'],
            'recipe':recipe,'cnf_sha256':hashlib.sha256(UNSAT).hexdigest(),'cnf_bytes':len(UNSAT),'source_sha256':contract['source_sha256'],
            'supervisor_sha256':R.SUP_SHA,'binary_authority':contract['binary_authority']}
        ph = C.publish_json(shadow/it['pin'],pin,shadow/'stage')
        r = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v3','status':'UNKNOWN','checked':False,'integrity_status':'NOT_EVALUATED',
             'integrity_errors':[],'sat_candidate':False,'halt_production':False,'cnf_sha256':pin['cnf_sha256'],'cnf_bytes':len(UNSAT),
             'pre_child_pin_sha256':ph,'native_result':{'status':'UNKNOWN','integrity_status':'NOT_EVALUATED','bounded_unknown':'CONTROL'}}
        TX.publish_item(r,contract,h,ca,it,shadow/'stage')
        assert C.inspect_new(contract,h,ca,it)['state'] == 'UNQUALIFIED'
        R.create_census = lambda lane=shadow: old[2](lane)
        R.census_for_gate = lambda ref,force=False,lane=shadow: old[3](ref,force,lane)
        class AlreadyHeld:
            def __enter__(self): return self
            def __exit__(self,*a): pass
        R.Capacity = lambda *a,**k: AlreadyHeld()
        def record(constructor,recipe,contract_sha,source_sha,paths,deadline,admission,*a,**k):
            calls.append(paths['id']); return {'status':'UNKNOWN'}
        O.execute = record
        sys.argv = [str(L/'src/run_m2_ms09_k1_v3.py'),contract['_control_contract_path'],h,'--max-attempts','1']
        TX.main()
    finally:
        C.LANE,TX.L,R.create_census,R.census_for_gate,R.Capacity,O.execute,sys.argv = old
    assert calls == [second], ('existing UNKNOWN was retried or queue changed',calls,first,second)
    assert list((shadow/'archive/k1-v3-unattempted-claims').glob('*.claim'))
    return {'skipped_existing_unknown':first,'next_attempted':second,'calls':calls}


def mutation_controls(root):
    def mutant(fn,transform,name):
        tree = transform().visit(ast.parse(source_inspect.getsource(fn))); ast.fix_missing_locations(tree)
        (root/(name+'.py')).write_text(ast.unparse(tree)+'\n')
        namespace = dict(fn.__globals__); exec(compile(tree,str(root/(name+'.py')),'exec'),namespace)
        return namespace[fn.__name__]
    class DropCheckerFeeds(ast.NodeTransformer):
        def visit_For(self,node):
            return None if ast.unparse(node.iter) == "result['cnf_feeds'].values()" else self.generic_visit(node)
    class AcceptUnknownRss(ast.NodeTransformer):
        def visit_Expr(self,node):
            return ast.Pass() if ast.unparse(node) == "errors.append('unknown RSS/headroom')" else self.generic_visit(node)
    class AcceptBinaryDrift(ast.NodeTransformer):
        def visit_Expr(self,node):
            return ast.Pass() if ast.unparse(node) == "errors.append('contract binary drift')" else self.generic_visit(node)
    class IgnoreSafety(ast.NodeTransformer):
        def visit_If(self,node):
            if ast.unparse(node.test) == 'safety': node.test = ast.Constant(value=False)
            return self.generic_visit(node)
    class AnyEmptyCase(ast.NodeTransformer):
        def visit_Compare(self,node):
            return ast.Constant(value=True) if ast.unparse(node) == "ca['b_index'] == 3" else self.generic_visit(node)
    h,ph = hashlib.sha256(UNSAT).hexdigest(),hashlib.sha256(b'').hexdigest()
    f = {'bytes':len(UNSAT),'sha256':h,'complete':True,'close_ok':True,'error':None}
    r = {'cnf_bytes':len(UNSAT),'cnf_sha256':h,'solver_rc':20,'checker_rc':0,
         'solver_collector':{'complete':True,'error':None,'status_lines':['s UNSATISFIABLE']},
         'checker_collector':{'complete':True,'error':None,'status_lines':['s VERIFIED']},
         'cnf_feeds':{'solver':f,'checker':dict(f,bytes=len(UNSAT)-1)},
         'proof_stream':{'reader_complete':True,'reader_error':None,'raw_bytes':0,'raw_sha256':ph},
         'proof_delivery':{'bytes':0,'sha256':ph,'complete':True,'close_ok':True,'error':None}}
    m = mutant(N.outcome,DropCheckerFeeds,'mutant-omitted-checker-feed')
    assert N.outcome(r)['integrity_status'] == 'INVALID' and m(r)['status'] == 'UNSAT'
    p = root/'mutant-scope'; scope(p); item = lease(p,5000)
    m = mutant(R.full_gate,AcceptUnknownRss,'mutant-unknown-rss')
    assert not R.full_gate(copy.deepcopy(item),'solver',p,providers(rss={'known':False}))['admitted']
    assert m(copy.deepcopy(item),'solver',p,providers(rss={'known':False}))['admitted']
    drift = {'python':{'matches':True},'solver':{'matches':False},'checker':{'matches':True}}
    m = mutant(R.full_gate,AcceptBinaryDrift,'mutant-binary-drift')
    assert not R.full_gate(copy.deepcopy(item),'solver',p,providers(binaries=drift))['admitted']
    assert m(copy.deepcopy(item),'solver',p,providers(binaries=drift))['admitted']
    native = {'status':'UNKNOWN','integrity_status':'NOT_EVALUATED','halt_production':False}
    rec = {'completed_cleanly':False,'trip_reason':'free bytes 1 below floor 12000000000','uncertain':False,'stop':{}}
    settle = {'group_quiescent':True,'leader_reaped':True,'explicit_owned_popen_wait':True}
    m = mutant(O.apply_worker_outcome,IgnoreSafety,'mutant-safety-not-dominant')
    assert O.apply_worker_outcome({},native,rec,settle)['halt_production'] is True and m({},native,rec,settle)['halt_production'] is False
    m = mutant(C.structural_acceptance,AnyEmptyCase,'mutant-generic-empty')
    case,c = {'b_index':0,'list':{'n':0,'sha256':C.B3.EXPECTED['empty_list_receipt']['sha256']}},{'skeleton_sha256':C.SKELETON_SHA}
    assert not C.structural_acceptance(c,case)['accepted'] and m(c,case)['accepted']
    return ['checker-feed omission','unknown-RSS admission','binary-drift admission','safety dominance removal','generic empty acceptance']


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--child':
        child(sys.argv[2],Path(sys.argv[3]),sys.argv[4:]); return
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); args = ap.parse_args()
    R.install_handlers()
    root = L/'cycle2'/('v3-required-controls-'+str(time.time_ns())); root.mkdir()
    out = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'schema':'PA19-V3-REQUIRED-CONTROLS-v1','production_coverage':False,
           'control_source_sha256':E.digest(SELF),'contract_sha256':args.sha256,'families':{}}
    try:
        with R.Capacity(time.monotonic()+10800):  # one real lane token; private shadow tokens for lifecycle fixtures
            st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+R.ITEM_GROWTH
            c = C.load(args.contract,args.sha256); c['_control_contract_path'] = str(Path(args.contract).resolve())
            assert all(v['matches'] for v in R.binary_observations(c['binary_authority']).values())
            out['families']['2_gate_census_and_boundaries'] = gate_controls(root)
            out['families']['2_postwait_STOP_floor_binary_data_no_child'] = postwait_controls(root)
            out['families']['4_scientific_UNKNOWN_and_integrity'] = unknown_controls(root)
            natives,expect = [],{}
            for name,opts in [('valid-full-feed',{'real_positive':True}),('solver-prefix',{'feed_fault':'solver'}),
                ('checker-prefix',{'feed_fault':'checker'}),('solver-write-error',{'fd_error':'solver-write'}),
                ('checker-write-error',{'fd_error':'checker-write'}),('solver-close-error',{'fd_error':'solver-close'}),
                ('checker-close-error',{'fd_error':'checker-close'}),('real-SAT-invalid-proof',{'real_negative':True}),
                ('post-Popen-exception',{'start_failure':True}),('collector-Thread.start-exception',{'thread_failure':True}),
                ('post-Popen-plus-receipt-OSError',{'start_failure':True,'receipt_error':True})]:
                entry = native_case(root,name,**opts); natives.append(entry)
                wanted = ('UNSAT','VALIDATED') if name == 'valid-full-feed' else ('UNKNOWN','INVALID')
                assert (entry['status'],entry['integrity_status']) == wanted, (name,entry,wanted)
            out['families']['1_exceptional_ownership'] = [x for x in natives if 'exception' in x['name'] or 'OSError' in x['name']]
            out['families']['1_late_leader_reap'] = late_reap_control(root)
            out['families']['3_measured_native_transport'] = [x for x in natives if x not in out['families']['1_exceptional_ownership']]
            out['families']['3_safety_dominates_worker_UNKNOWN'] = safety_dominance_control()
            out['families']['5_6_publisher_reader_inventory_runner_veto'] = coverage_controls(root,c,args.sha256)
            out['families']['5_no_automatic_retry'] = no_retry_control(root,c,args.sha256)
            out['families']['7_actual_filetype_byte_accounting'] = accounting_controls(root)
            out['source_omission_mutants_killed'] = mutation_controls(root)
            out.update(status='PASS',finished_host_clock=time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                       resource_claim='small controlled observations; no instantaneous production RSS or disk guarantee')
            dest = root/'receipt.json'; dump(dest,out); print(dest,E.digest(dest),flush=True)
    except BaseException as exc:
        out.update(status='FAIL_OR_DEFERRED',error=repr(exc),finished_host_clock=time.strftime('%Y-%m-%dT%H:%M:%S%z'))
        dest = root/'failure-receipt.json'; dump(dest,out); print(dest,E.digest(dest),flush=True); raise


if __name__ == '__main__':
    main()
