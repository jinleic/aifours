#!/usr/bin/env python3
"""check_m2_ms09_k1_v6_1.py = check_m2_ms09_k1_v8.py (sha256 74194dde16e10d47ff84f545cb4b3904511e6ac8cad56a6932300e553afd86ce) with the v6->v6_1 module rename and its two
receipt labels renamed v8->v6_1; nothing else changed. Not used by M2H production.
v8 control harness (production v6_1 sources/contracts unchanged; v7 path-classification bug fixed). PRIVATE controls; excluded from scientific coverage and executed only after parent GO.
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
import m2_item_owner_v6_1 as O
import m2_ms09_contract_v6_1 as C
import m2_ms09_evidence_v6_1 as E
import m2_native_staged_v6_1 as N
import m2_supervised_runtime_v6_1 as R
import run_m2_ms06_direct_v6_1 as M6
import run_m2_ms09_k1_v6_1 as TX

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
        if kind == 'solver' and cfg.get('delayed_publication'):
            with open(extra[2],'wb') as f: f.write(b'\0'*65536)  # exceeds the control-only small raw cap
            dump(cfg['solver_alive_marker'],{'pid':os.getpid(),'proof_written_and_closed':True})
            deadline = time.monotonic()+120  # only detects a broken handshake; normal exit is explicitly permitted
            while not Path(cfg['solver_exit_permission']).exists():
                if time.monotonic() > deadline:
                    dump(cfg['handshake_failure'],{'broken':'solver exit permission never granted'}); raise SystemExit(3)
                time.sleep(0.01)
            raise SystemExit(0)
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
            side = 'checker' if Path(fifo).name == 'checker-cnf.fifo' else 'solver'  # basename only; case folders may contain role words
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
    # Scoped instrumentation ONLY: the pipeline module sees a proxy; process-global threading primitives stay intact.
    real_threading,natives = threading,[]
    main_ident = real_threading.get_ident()
    main_stop_seen,join_entered = real_threading.Event(),real_threading.Event()
    class StopEvent(real_threading.Event):
        def set(self):
            if real_threading.get_ident() == main_ident: main_stop_seen.set()  # identifier only; no Thread lookup
            return super().set()
    class AckJoinThread(real_threading.Thread):
        def join(self,timeout=None):
            join_entered.set()  # the settlement join has begun
            return super().join(timeout)
    class FailingStartThread(real_threading.Thread):
        def start(self):
            time.sleep(0.2); dump(cfg['injection_marker'],{'injected':'CONTROL collector start failure'})
            raise RuntimeError('CONTROL collector start failure')
    class PipelineThreading:
        def __init__(self): self.stop_event = None
        def __getattr__(self,name): return getattr(real_threading,name)
        def Event(self):
            if self.stop_event is None and cfg.get('delayed_publication'):
                self.stop_event = StopEvent(); return self.stop_event
            return real_threading.Event()
        def Thread(self,*args,**kwargs):
            target = kwargs.get('target')
            if cfg.get('thread_failure') and target is N.collector: return FailingStartThread(*args,**kwargs)
            if cfg.get('delayed_publication') and target is delayed_feed and Path(kwargs.get('args',('',))[0]).name == 'solver-cnf.fifo':
                return AckJoinThread(*args,**kwargs)
            return real_threading.Thread(*args,**kwargs)
    N.threading = PipelineThreading()
    real_feed = N.feed_cnf
    def delayed_feed(fifo,data,record,stop,deadline):
        private = {}
        real_feed(fifo,data,private,stop,deadline)
        if Path(fifo).name == 'solver-cnf.fifo':
            if not join_entered.wait(120):  # only detects a broken handshake
                dump(cfg['handshake_failure'],{'broken':'settlement join never began'}); return
            dump(cfg['injection_marker'],{'published_after_settlement_join_entered':True,'main_stop_seen':main_stop_seen.is_set(),'feed':private})
        record.update(private)
    if cfg.get('delayed_publication'):
        # Deterministic race model: the solver feeder suffers a REAL write failure; publication waits for the
        # worker's settlement join, which can only begin after the main-thread bounded-exit stop.
        N.MAX_RAW = 1000
        N.feed_cnf = delayed_feed
        real_start = N.start_native
        def capture(*args,**kwargs):
            p,t = real_start(*args,**kwargs); natives.append(p); return p,t
        N.start_native = capture
    pipeline = N.pipeline
    if cfg.get('mutant_no_settle'):
        class RemoveSettleJoin(ast.NodeTransformer):
            changes = 0
            def visit_For(self,node):
                if ast.unparse(node.target) == '(name, thread)' and ast.unparse(node.iter) == 'feeders':
                    RemoveSettleJoin.changes += 1; return ast.Pass()
                return self.generic_visit(node)
        tree = RemoveSettleJoin().visit(ast.parse(source_inspect.getsource(N.pipeline))); ast.fix_missing_locations(tree)
        assert RemoveSettleJoin.changes == 1, 'removed-join mutant did not hit the settlement loop'
        namespace = dict(N.__dict__); exec(compile(tree,str(Path(cfg['result']).parent/'mutant-no-settle.py'),'exec'),namespace)
        pipeline = namespace['pipeline']
    def commands(paths):
        if cfg.get('real_positive'):
            return ([N.KISSAT,'-q','-f','--seed=1','--time=600',paths['solver-cnf.fifo'],paths['proof.fifo']],[N.DT,paths['checker-cnf.fifo'],'-i','-t','1200'])
        solver = [sys.executable,'-B',str(SELF),'--child','emit',str(path),'solver',paths['solver-cnf.fifo'],paths['proof.fifo']]
        checker = [N.DT,paths['checker-cnf.fifo'],'-i','-t','1200'] if cfg.get('real_negative') else [sys.executable,'-B',str(SELF),'--child','emit',str(path),'checker',paths['checker-cnf.fifo']]
        return solver,checker
    def hook(p):
        time.sleep(0.2); dump(cfg['injection_marker'],{'injected':'CONTROL post-Popen exception'})
        raise RuntimeError('CONTROL post-Popen exception')
    result = pipeline(raw,cfg['job'],commands,hook if cfg.get('start_failure') else None)
    if cfg.get('delayed_publication'):
        Path(cfg['solver_exit_permission']).write_text('granted after pipeline return')
        deadline = time.monotonic()+60  # only detects a broken handshake; no subprocess timeout
        for p in natives:
            while p.poll() is None:
                if time.monotonic() > deadline: raise RuntimeError('CONTROL handshake broken: solver still alive')
                time.sleep(0.01)
            p.wait()
        result['control_acknowledgments'] = {'main_stop_seen':main_stop_seen.is_set(),'join_entered':join_entered.is_set()}
    dump(cfg['result'],result)


def native_case(root,name,**options):
    folder = root/name; folder.mkdir(); priv = folder/'scope'; scope(priv)
    item = lease(priv,time.monotonic()+8000)
    cfg = dict(options,scope=str(priv),result=str(folder/'worker.json'),marker=str(folder/'marker.json'),injection_marker=str(folder/'injection.json'),
               solver_alive_marker=str(folder/'solver-alive.json'),solver_exit_permission=str(folder/'solver-exit-permission'),
               handshake_failure=str(folder/'handshake-failure.json'),
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
        injected = 'CONTROL collector start failure' if options.get('thread_failure') else 'CONTROL post-Popen exception'
        assert json.loads((folder/'injection.json').read_bytes()) == {'injected':injected}, 'injection did not run'
        assert result.get('lifecycle_error') == repr(RuntimeError(injected)), result.get('lifecycle_error')
        assert result.get('unknown_reason') == 'incomplete native lifecycle: '+repr(RuntimeError(injected)), result.get('unknown_reason')
        assert str(rec.get('trip_reason')).startswith('group member alive after leader exit'), rec.get('trip_reason')
        if options.get('receipt_error'):
            assert rec.get('record_write_error') and rec.get('cleanup_exception') and rec.get('uncertain') is True
        else:
            assert rec.get('uncertain') is False and (rec.get('stop') or {}).get('listing_ok') is True and (rec.get('stop') or {}).get('survivors') == []
    if options.get('delayed_publication'):
        assert not (folder/'handshake-failure.json').exists(), json.loads((folder/'handshake-failure.json').read_bytes())
        assert json.loads((folder/'solver-alive.json').read_bytes())['proof_written_and_closed'] is True
        assert result.get('bounded_unknown') and result.get('proof_cap_hit') == 'raw' and result['feeders_settled'] == ['solver']
        assert result['control_acknowledgments']['main_stop_seen'] is True
        assert rec.get('completed_cleanly') is True and not rec.get('trip_reason'), ('supervision must be clean',rec)
    if options.get('delayed_publication') and options.get('mutant_no_settle'):
        assert not (folder/'injection.json').exists() and result['control_acknowledgments']['join_entered'] is False
        assert (result['status'],result['integrity_status'],result['unknown_reason']) == ('UNKNOWN','NOT_EVALUATED','declared proof cap; not certified'), result
    elif options.get('delayed_publication'):
        late = json.loads((folder/'injection.json').read_bytes())
        assert late['published_after_settlement_join_entered'] is True and late['main_stop_seen'] is True
        assert late['feed']['error'] == repr(OSError('CONTROL CNF write failure')) and late['feed']['cancelled'] is None
        composed = O.apply_worker_outcome({'status':'UNKNOWN','checked':False,'halt_production':False,'sat_candidate':False,
            'integrity_status':result['integrity_status']},result,rec,cap.settlement)
        saved_lane = O.L
        try:
            O.L = priv
            O.persist_veto(composed,{'worker_result':priv/'cycle2/CONTROL-worker.json','supervisor':priv/'cycle2/CONTROL-supervisor.json'},'CONTROL',{})
        finally: O.L = saved_lane
        assert composed['halt_production'] is True and (priv/'cycle2/m2k3-INTEGRITY.flag').exists(), 'persistent veto missing'
    assert all(lock_free(priv/'cycle2/tokens'/('t%d' % i)) for i in range(2))
    dump(folder/'control-receipt.json',{'result':result,'supervisor':rec,'observations':observations,'production_coverage':False})
    return {'name':name,'status':result['status'],'integrity_status':result['integrity_status'],'unknown_reason':result.get('unknown_reason'),
            'receipt':str((folder/'control-receipt.json').relative_to(L)),'sha256':E.digest(folder/'control-receipt.json')}


def gate_controls(root):
    priv = root/'gate-scope'; scope(priv); base = lease(priv,5000); rows = []
    assert R.full_gate(copy.deepcopy(base),'solver',priv,providers())['admitted']
    tests = [('free-minus1',{'free':R.BASE_GATE+R.ITEM_GROWTH-1},'fresh statvfs growth/floor gate'),('count3',{'count':3},'COUNT ceiling/format'),
             ('count0',{'count':0},'new admissions paused'),('rss-unknown',{'rss':{'known':False}},'unknown RSS/headroom'),
             ('deadline',{'clock':3000},'deadline allowance'),
             ('census-stale',{'census':{'reference':{},'age_seconds':R.CENSUS_TTL+1,'finished_monotonic':0,'current_data_upper_bytes':1}},'stale/unknown census age'),
             ('census-unknown',{'census':lambda:(_ for _ in ()).throw(RuntimeError('CONTROL census unknown'))},'gate measurement/authority error'),
             ('data-plus-margin',{'census':{'reference':{},'age_seconds':0,'finished_monotonic':time.monotonic(),
                'current_data_upper_bytes':R.DATA_CAP-R.ALL_PLANNED_RETAINED_BOUND-R.OTHER_WRITER_MARGIN+1}},'allocated-data cap with whole-plan reservation/margin'),
             ('binary-drift',{'binaries':{'python':{'matches':True},'solver':{'matches':False},'checker':{'matches':True}}},'contract binary drift')]
    for name,change,cause in tests:
        g = R.full_gate(copy.deepcopy(base),'solver',priv,providers(**change))
        assert not g['admitted'] and any(e.startswith(cause) for e in g['errors']), (name,cause,g['errors'])
        rows.append({'name':name,'required_cause':cause,'errors':g['errors']})
    for name in R.ADMISSION_MARKERS:  # shared registry: old m2k1 and new m2k3 persistent markers plus resource STOPs
        p = root/('stop-'+name.replace('.','_')); scope(p); (p/'cycle2'/name).write_text('CONTROL')
        g = R.full_gate(copy.deepcopy(base),'solver',p,providers())
        assert not g['admitted'] and g['errors'] == ['STOP/veto '+name], (name,g['errors'])
        rows.append({'name':name,'class':'resource-stop' if name in R.RESOURCE_STOPS else 'persistent-veto','errors':g['errors']})
    # Real cache semantics: fresh <=600s accepted, older refreshes by an actual exact census of a tiny private scope.
    fresh = R.census_for_gate(census_ref(priv,7,10),False,priv); assert fresh['current_data_upper_bytes'] == 7
    renewed = R.census_for_gate(census_ref(priv,7,R.CENSUS_TTL+5),False,priv)
    assert renewed['reference'] != fresh['reference'] and renewed['age_seconds'] <= R.CENSUS_TTL
    rows.append({'name':'real-census-cache-and-refresh','fresh_age':fresh['age_seconds'],'renewed_reference':renewed['reference']})
    return rows


def postwait_controls(root):
    rows = []
    causes = {'STOP':'STOP/veto STOP-m2r12','floor':'fresh statvfs growth/floor gate','binary':'contract binary drift',
              'data':'allocated-data cap with whole-plan reservation/margin','old-marker':'STOP/veto m2k1-HALT.flag'}
    for change in ('STOP','floor','binary','data','old-marker'):
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
            elif change == 'data': usage[0] = R.DATA_CAP
            else: (priv/'cycle2/m2k1-HALT.flag').write_text('{"CONTROL":"old v1 persistent veto appears during capacity wait"}')
            fcntl.flock(token,fcntl.LOCK_UN); os.close(token); token = None
            assert finished.wait(5) and result.get('rec') is None and not result['gate']['admitted'], result
            assert result['gate']['errors'] == [causes[change]], (change,result['gate']['errors'])
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
    native = {'schema':'PA19-NATIVE-RESULT-v6_1','status':'UNKNOWN','integrity_status':'NOT_EVALUATED','bounded_unknown':'native wall',
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
    timeout = copy.deepcopy(base); timeout['checker_collector']['status_lines'] = ['s TIMEOUT']
    timeout['proof_delivery'] = {'bytes':0,'sha256':ph,'complete':False,'close_ok':True,'error':'BrokenPipeError: checker exited at timeout'}
    o = N.outcome(timeout); assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'NOT_EVALUATED' and not o['halt_production']
    rows.append('TIMEOUT-with-expected-incomplete-replay: ordinary UNKNOWN')
    bad = copy.deepcopy(timeout); bad['cnf_feeds']['checker']['sha256'] = '0'*64; o = N.outcome(bad)
    assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'INVALID' and o['halt_production']; rows.append('TIMEOUT-plus-bad-checker-feed: INVALID veto')
    bad = copy.deepcopy(timeout); bad['proof_delivery'] = {'bytes':1,'sha256':'1'*64,'complete':True,'close_ok':True,'error':None}; o = N.outcome(bad)
    assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'INVALID' and o['halt_production']; rows.append('TIMEOUT-plus-bad-completed-replay: INVALID veto')
    bad = copy.deepcopy(timeout); bad['cnf_feeds']['checker']['complete'] = False; bad['cnf_feeds']['checker']['error'] = 'CONTROL'; o = N.outcome(bad)
    assert o['status'] == 'UNKNOWN' and o['integrity_status'] == 'INVALID'; rows.append('TIMEOUT-plus-incomplete-checker-feed: INVALID veto')
    bad = copy.deepcopy(base); bad['bounded_unknown'] = 'CONTROL'; bad['cnf_feeds']['solver']['sha256'] = '0'*64; o = N.outcome(bad)
    assert o['integrity_status'] == 'INVALID'; rows.append('bounded-stop-plus-completed-bad-solver-feed: INVALID veto')
    real_write = {'complete':False,'close_ok':True,'error':"OSError('CONTROL write failure')",'cancelled':None,'close_error':None,'bytes':1,'sha256':'0'*64}
    real_close = {'complete':False,'close_ok':False,'error':"OSError('CONTROL close failure')",'cancelled':None,'close_error':"OSError('CONTROL close failure')",'bytes':len(UNSAT),'sha256':h}
    stop_cancel = {'complete':False,'close_ok':True,'error':"TimeoutError('CNF write cancelled: stop-event')",'cancelled':'stop-event','close_error':None,'bytes':1,'sha256':'0'*64}
    deadline_cancel = dict(stop_cancel,cancelled='item-deadline',error="TimeoutError('CNF write cancelled: item-deadline')")
    for bound in ('proof_cap_hit','bounded_unknown'):
        for side in ('solver','checker'):
            for label,feed,wanted in (('real-write',real_write,('INVALID','CNF transport failure (not bound-induced cancellation): '+side)),
                                      ('real-close',real_close,('INVALID','CNF FIFO close failed: '+side)),
                                      ('stop-cancel',stop_cancel,('NOT_EVALUATED','declared proof cap; not certified' if bound == 'proof_cap_hit' else 'bounded native stop')),
                                      ('deadline-cancel',deadline_cancel,('NOT_EVALUATED','declared proof cap; not certified' if bound == 'proof_cap_hit' else 'bounded native stop'))):
                case = copy.deepcopy(base); case[bound] = 'raw' if bound == 'proof_cap_hit' else 'CONTROL'; case['cnf_feeds'][side] = dict(feed)
                o = N.outcome(case)
                assert o['status'] == 'UNKNOWN' and (o['integrity_status'],o['unknown_reason']) == wanted, (bound,side,label,o)
                assert o['halt_production'] is (wanted[0] == 'INVALID')
                rows.append('%s+%s-%s -> %s' % (bound,side,label,wanted[0]))
    r = copy.deepcopy(base); r['solver_rc'] = 10; r['solver_collector']['status_lines'] = ['s SATISFIABLE']; o = N.outcome(r)
    assert o['status'] == 'UNKNOWN' and o['sat_candidate'] and o['halt_production']
    for raw,expected in ((b's VERIFIED\r\n',['s VERIFIED']),(b' s VERIFIED\n',[]),(b's NOT VERIFIED\n',['s NOT VERIFIED'])):
        out = {}; N.collector(io.BytesIO(raw),out); assert out['complete'] and out['status_lines'] == expected
    return rows


def scoped_contract(validated,path,h):
    """Control adapter: contract ALREADY loaded against the production authority root; shadow re-verifies inputs only."""
    def load(p,s):
        assert Path(p).resolve() == Path(path).resolve() and s == h, 'scoped adapter only serves the validated contract'
        c = copy.deepcopy(validated); C.verify_sources(c)
        return c
    return load


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
        pin = {'schema':'PA19-K1-CNF-PIN-v6_1','production_contract_sha256':h,'multiset':9,'b_index':70,'indices':[0,24],
               'recipe':recipe,'binary_authority':contract['binary_authority'],'cnf_sha256':expected['cnf_sha256'],'cnf_bytes':expected['cnf_bytes'],
               'source_sha256':contract['source_sha256'],'supervisor_sha256':R.SUP_SHA}
        ph = C.publish_json(shadow/it['pin'],pin,shadow/'stage')
        dump(shadow/'cycle2'/'m2k3-INTEGRITY.flag',{'status':'UNKNOWN','veto':'INTEGRITY','CONTROL':True})
        result = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v6_1','status':'UNKNOWN','integrity_status':'INVALID','integrity_errors':['CONTROL invalid proof'],'sat_candidate':False,'checked':False,'halt_production':True,
                  'cnf_sha256':pin['cnf_sha256'],'cnf_bytes':pin['cnf_bytes'],'pre_child_pin_sha256':ph,
                  'native_result':{'status':'UNKNOWN','integrity_status':'INVALID','checker_collector':{'status_lines':['s NOT VERIFIED']}}}
        TX.publish_item(result,contract,h,ca,it,shadow/'stage')
        q = C.inspect_new(contract,h,ca,it)
        assert q['state'] == 'INTEGRITY_VETO' and any('persistent INVALID integrity/verdict' in e for e in q['errors']), q
        snap = C.inventory(contract,h)
        assert snap['integrity_issues'] and not snap['final_ms09_acceptance_ready']
        original_cap,original_owner,argv,original_load = R.Capacity,O.execute,sys.argv,C.load
        class AlreadyHeld:
            def __enter__(self): return self
            def __exit__(self,*args): pass
        calls = []
        def forbidden_native(*args,**kwargs):
            calls.append('NATIVE MUST NOT START'); raise AssertionError('veto failed')
        try:
            R.Capacity = lambda *args,**kwargs:AlreadyHeld()  # REAL outer control token remains held
            C.load = scoped_contract(contract,contract['_control_contract_path'],h)
            O.execute = forbidden_native
            sys.argv = [str(L/'src/run_m2_ms09_k1_v6_1.py'),str(L/contract['_control_contract_path']),h,'--max-attempts','1']
            TX.main()
        finally:
            R.Capacity,O.execute,sys.argv,C.load = original_cap,original_owner,argv,original_load
        deferred = [json.loads(p.read_bytes()) for p in (shadow/'cycle2'/'m2k3-chunks').glob('*/initialization-deferred.json')]
        assert not calls and len(deferred) == 1 and deferred[0]['init_stage'] == 'inventory', deferred
        assert 'persistent SAT/integrity/safety veto' in deferred[0]['reason'] and 'm2k3-INTEGRITY.flag' in deferred[0]['veto_detail']['veto_markers']
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
            cc = {'schema':'PA19-K1-RECEIPT-v6_1','production_contract_sha256':h,'b_index':70,'indices':[0,24],
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
    original_load = C.load
    try:
        C.LANE = TX.L = shadow; C.load = scoped_contract(contract,contract['_control_contract_path'],h)
        first,second = contract['pending_order'][:2]
        byid = {it['id']:(ca,it) for ca in contract['cases'] for it in ca['intervals']}
        ca,it = byid[first]
        recipe = {'mode':'partbatch','multiset':9,'b_index':ca['b_index'],'indices':it['indices'],'skeleton_path':contract['skeleton_path'],
            'skeleton_sha256':contract['skeleton_sha256'],'encoder_sha256':contract['source_sha256']['src/encode_skel_b.py'],
            'list_path':ca['list']['path'],'list_sha256':ca['list']['sha256'],'complete_denominator':ca['list']['n']}
        pin = {'schema':'PA19-K1-CNF-PIN-v6_1','production_contract_sha256':h,'multiset':9,'b_index':ca['b_index'],'indices':it['indices'],
            'recipe':recipe,'cnf_sha256':hashlib.sha256(UNSAT).hexdigest(),'cnf_bytes':len(UNSAT),'source_sha256':contract['source_sha256'],
            'supervisor_sha256':R.SUP_SHA,'binary_authority':contract['binary_authority']}
        ph = C.publish_json(shadow/it['pin'],pin,shadow/'stage')
        r = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v6_1','status':'UNKNOWN','checked':False,'integrity_status':'NOT_EVALUATED',
             'integrity_errors':[],'sat_candidate':False,'halt_production':False,'cnf_sha256':pin['cnf_sha256'],'cnf_bytes':len(UNSAT),
             'pre_child_pin_sha256':ph,'native_result':{'status':'UNKNOWN','integrity_status':'NOT_EVALUATED','bounded_unknown':'CONTROL'}}
        TX.publish_item(r,contract,h,ca,it,shadow/'stage')
        assert C.inspect_new(contract,h,ca,it)['state'] == 'UNQUALIFIED'
        first_record_sha = E.digest(shadow/it['new_record'])
        second_claim = byid[second][1]['claim']
        R.create_census = lambda lane=shadow: old[2](lane)
        R.census_for_gate = lambda ref,force=False,lane=shadow: old[3](ref,force,lane)
        class AlreadyHeld:
            def __enter__(self): return self
            def __exit__(self,*a): pass
        R.Capacity = lambda *a,**k: AlreadyHeld()
        def record(constructor,recipe,contract_sha,source_sha,paths,deadline,admission,*a,**k):
            calls.append(paths['id']); return {'status':'UNKNOWN'}
        O.execute = record
        sys.argv = [str(L/'src/run_m2_ms09_k1_v6_1.py'),contract['_control_contract_path'],h,'--max-attempts','1']
        TX.main()
    finally:
        C.LANE,TX.L,R.create_census,R.census_for_gate,R.Capacity,O.execute,sys.argv = old; C.load = original_load
    assert calls == [second], ('existing UNKNOWN was retried or queue changed',calls,first,second)
    import re as regex
    archived = [p for p in (shadow/'archive/k1-v6_1-unattempted').iterdir() if regex.fullmatch(regex.escape(Path(second_claim).name)+r'\.[0-9]+',p.name)]
    assert len(archived) == 1 and not (shadow/second_claim).exists(), ('second claim not archived with timestamp suffix',archived)
    assert E.digest(shadow/it['new_record']) == first_record_sha, 'first UNKNOWN receipt changed'
    return {'skipped_existing_unknown':first,'next_attempted':second,'calls':calls,'archived_claim':str(archived[0].relative_to(shadow)),
            'first_record_unchanged_sha256':first_record_sha}


def refusal_controls(root,contract,h):
    """v4 refusal rules through the ACTUAL runner+owner+private Capacity+local r3 adapter. Private shadow flags only."""
    rows = {}
    for mode in ('before-pin','after-pin-before-worker','started-group-safety-trip'):
        shadow = shadow_lane(root,'refusal-'+mode,contract); scope(shadow)
        saved = (C.LANE,TX.L,O.L,O.WORKER,R.create_census,R.census_for_gate,R.Capacity,R.full_gate,sys.argv)
        original_capacity,original_gate = R.Capacity,R.full_gate
        refusing = {'before-pin':'construct','after-pin-before-worker':'worker'}.get(mode)
        original_load = C.load
        try:
            C.LANE = TX.L = O.L = shadow; C.load = scoped_contract(contract,contract['_control_contract_path'],h)
            R.create_census = lambda lane=shadow: saved[4](lane)
            R.census_for_gate = lambda ref,force=False,lane=shadow: saved[5](ref,force,lane)
            R.Capacity = lambda deadline,lane=None,metadata=False,wait_allowance=2550: original_capacity(deadline,shadow,metadata,wait_allowance)
            R.full_gate = lambda item,phase,lane=None: original_gate(item,phase,shadow,providers(
                free=(lambda: 0) if phase == refusing else (lambda:(lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L)))))
            if mode == 'started-group-safety-trip':
                O.WORKER = SELF  # fake worker sleeps; owner/runner/Capacity/supervisor remain the real code paths
                def external_stop():
                    while not list(shadow.glob('cycle2/m2part_drat/*/*_k1_v6_1.json.job.json')): time.sleep(0.02)
                    time.sleep(0.5); os.kill(os.getpid(),signal.SIGTERM)
                threading.Thread(target=external_stop,daemon=True).start()
            sys.argv = [str(L/'src/run_m2_ms09_k1_v6_1.py'),contract['_control_contract_path'],h,'--max-attempts','1']
            TX.main()
        finally:
            C.LANE,TX.L,O.L,O.WORKER,R.create_census,R.census_for_gate,R.Capacity,R.full_gate,sys.argv = saved; C.load = original_load
        ident = contract['pending_order'][0]
        ca,it = next((ca,it) for ca in contract['cases'] for it in ca['intervals'] if it['id'] == ident)
        flags = sorted(p.name for p in (shadow/'cycle2').glob('m2k3-*.flag'))
        archived = sorted(str(p.relative_to(shadow)) for p in (shadow/'archive').rglob('*') if p.is_file() and p.name != 'MANIFEST.tsv') if (shadow/'archive').exists() else []
        record = shadow/it['new_record']
        if mode == 'before-pin':
            assert not record.exists() and not (shadow/it['pin']).exists() and flags == [], (flags,record)
            assert any(Path(a).name.startswith(Path(it['claim']).name) for a in archived)
        elif mode == 'after-pin-before-worker':
            assert not record.exists() and not (shadow/it['pin']).exists() and flags == [], (flags,record)
            names = [Path(a).name for a in archived]
            assert any(n.startswith(Path(it['pin']).name) for n in names) and any(n.startswith(Path(it['claim']).name) for n in names)
            assert any(n.startswith(Path(it['new_record']).name+'.job.json') for n in names)
            assert not Path(str(record)+'.supervisor.json').exists() and not Path(str(record)+'.worker.json').exists()
        else:
            assert record.exists() and flags == ['m2k3-HALT.flag'], (flags,record)
            saved_record = json.loads(record.read_bytes())
            assert saved_record['status'] == 'UNKNOWN' and saved_record['halt_production'] is True and saved_record['safety_veto']
            sup,settle = saved_record['supervisor'],saved_record['owner_settlement']
            assert saved_record['group_started'] is True and sup['leader_pid'] and str(sup['trip_reason']).startswith('external SIGTERM'), sup
            assert settle['group_quiescent'] is True and settle['leader_reaped'] is True and settle['explicit_owned_popen_wait'] is True
            assert settle['owned_leader_pid'] == sup['leader_pid'] and type(settle['leader_returncode']) is int
            old_lane = C.LANE
            try:
                C.LANE = shadow
                assert C.inspect_new(contract,h,ca,it)['state'] == 'HALT_UNKNOWN'
            finally: C.LANE = old_lane
        rows[mode] = {'flags':flags,'record_exists':record.exists(),'archived':archived}
    return rows


def mutation_controls(root):
    """Each mutant must make EXACTLY its expected AST change; original rejects while mutant accepts the same fixture."""
    def mutant(fn,transformer,name,expected_changes):
        tree = transformer.visit(ast.parse(source_inspect.getsource(fn))); ast.fix_missing_locations(tree)
        assert transformer.changes == expected_changes, (name,'mutation did not hit the intended enforcement',transformer.changes)
        (root/(name+'.py')).write_text(ast.unparse(tree)+'\n')
        namespace = dict(fn.__globals__); exec(compile(tree,str(root/(name+'.py')),'exec'),namespace)
        return namespace[fn.__name__]
    class Counting(ast.NodeTransformer):
        def __init__(self): self.changes = 0
    class CheckerFeedAlwaysExact(Counting):
        def visit_Assign(self,node):
            if [ast.unparse(t) for t in node.targets] == ['checker_feed_exact']:
                self.changes += 1; node.value = ast.Constant(value=True)
            return node
    class AcceptUnknownRss(Counting):
        def visit_Expr(self,node):
            if ast.unparse(node) == "errors.append('unknown RSS/headroom')": self.changes += 1; return ast.Pass()
            return node
    class AcceptBinaryDrift(Counting):
        def visit_Expr(self,node):
            if ast.unparse(node) == "errors.append('contract binary drift')": self.changes += 1; return ast.Pass()
            return node
    class IgnoreSafety(Counting):
        def visit_If(self,node):
            if ast.unparse(node.test) == 'safety': self.changes += 1; node.test = ast.Constant(value=False)
            return self.generic_visit(node)
    class AnyEmptyCase(Counting):
        def visit_Compare(self,node):
            if ast.unparse(node) == "ca['b_index'] == 3": self.changes += 1; return ast.Constant(value=True)
            return self.generic_visit(node)
    class SkipCompletedReplayMismatch(Counting):
        def visit_If(self,node):
            if ast.unparse(node.test).startswith("r.get('complete') and (r.get('bytes')"): self.changes += 1; node.test = ast.Constant(value=False)
            return self.generic_visit(node)
    class SkipRealFeedFailure(Counting):
        def visit_If(self,node):
            if ast.unparse(node.test).startswith("feed.get('error') is not None and feed.get('cancelled')"): self.changes += 1; node.test = ast.Constant(value=False)
            return self.generic_visit(node)
    class NewMarkersOnly(Counting):
        def visit_For(self,node):
            if ast.unparse(node.iter) == 'ADMISSION_MARKERS':
                self.changes += 1
                node.iter = ast.parse("('STOP-hard12','STOP-m2r12','STOP-K1','m2k3-SAT.flag','m2k3-INTEGRITY.flag','m2k3-HALT.flag','m2k3-QUARANTINE.flag')",mode='eval').body
            return self.generic_visit(node)
    h,ph = hashlib.sha256(UNSAT).hexdigest(),hashlib.sha256(b'').hexdigest()
    f = {'bytes':len(UNSAT),'sha256':h,'complete':True,'close_ok':True,'error':None}
    good = {'cnf_bytes':len(UNSAT),'cnf_sha256':h,'solver_rc':20,'checker_rc':0,
         'solver_collector':{'complete':True,'error':None,'status_lines':['s UNSATISFIABLE']},
         'checker_collector':{'complete':True,'error':None,'status_lines':['s VERIFIED']},
         'cnf_feeds':{'solver':dict(f),'checker':dict(f)},
         'proof_stream':{'reader_complete':True,'reader_error':None,'raw_bytes':0,'raw_sha256':ph},
         'proof_delivery':{'bytes':0,'sha256':ph,'complete':True,'close_ok':True,'error':None}}
    assert N.outcome(good)['status'] == 'UNSAT'
    # Only the final checker-feed predicate catches a stop-cancelled incomplete checker feed with a VERIFIED checker.
    cancelled = copy.deepcopy(good); cancelled['cnf_feeds']['checker'] = {'bytes':0,'sha256':ph,'complete':False,'close_ok':True,
        'error':"TimeoutError('CNF write cancelled: stop-event')",'cancelled':'stop-event','close_error':None}
    m = mutant(N.outcome,CheckerFeedAlwaysExact(),'mutant-checker-feed-enforcement-removed',1)
    assert N.outcome(cancelled)['integrity_status'] == 'INVALID' and m(cancelled)['status'] == 'UNSAT'
    capped = copy.deepcopy(good); capped['proof_cap_hit'] = 'raw'
    capped['cnf_feeds']['solver'] = {'bytes':1,'sha256':'0'*64,'complete':False,'close_ok':True,'error':"OSError('CONTROL write')",'cancelled':None,'close_error':None}
    m = mutant(N.outcome,SkipRealFeedFailure(),'mutant-cap-hides-real-feed-failure',1)
    assert N.outcome(capped)['integrity_status'] == 'INVALID' and m(capped)['integrity_status'] == 'NOT_EVALUATED'
    p = root/'mutant-scope'; scope(p); item = lease(p,5000)
    m = mutant(R.full_gate,AcceptUnknownRss(),'mutant-unknown-rss',1)
    assert not R.full_gate(copy.deepcopy(item),'solver',p,providers(rss={'known':False}))['admitted']
    assert m(copy.deepcopy(item),'solver',p,providers(rss={'known':False}))['admitted']
    drift = {'python':{'matches':True},'solver':{'matches':False},'checker':{'matches':True}}
    m = mutant(R.full_gate,AcceptBinaryDrift(),'mutant-binary-drift',1)
    assert not R.full_gate(copy.deepcopy(item),'solver',p,providers(binaries=drift))['admitted']
    assert m(copy.deepcopy(item),'solver',p,providers(binaries=drift))['admitted']
    native = {'status':'UNKNOWN','integrity_status':'NOT_EVALUATED','halt_production':False}
    rec = {'completed_cleanly':False,'trip_reason':'free bytes 1 below floor 12000000000','uncertain':False,'stop':{}}
    settle = {'group_quiescent':True,'leader_reaped':True,'explicit_owned_popen_wait':True}
    m = mutant(O.apply_worker_outcome,IgnoreSafety(),'mutant-safety-not-dominant',1)
    assert O.apply_worker_outcome({},native,rec,settle)['halt_production'] is True and m({},native,rec,settle)['halt_production'] is False
    m = mutant(C.structural_acceptance,AnyEmptyCase(),'mutant-generic-empty',1)
    case,c = {'b_index':0,'list':{'n':0,'sha256':C.B3.EXPECTED['empty_list_receipt']['sha256']}},{'skeleton_sha256':C.SKELETON_SHA}
    assert not C.structural_acceptance(c,case)['accepted'] and m(c,case)['accepted']
    t = copy.deepcopy(good); t['checker_collector']['status_lines'] = ['s TIMEOUT']
    t['proof_delivery'] = {'bytes':0,'sha256':'1'*64,'complete':True,'close_ok':True,'error':None}  # equal length, wrong SHA
    m = mutant(N.outcome,SkipCompletedReplayMismatch(),'mutant-timeout-hides-bad-replay',1)
    assert N.outcome(t)['integrity_status'] == 'INVALID' and m(t)['integrity_status'] == 'NOT_EVALUATED'
    old = root/'mutant-old-marker'; scope(old); (old/'cycle2/m2k1-INVALID.flag').write_text('{}')
    m = mutant(R.full_gate,NewMarkersOnly(),'mutant-drops-old-markers',1)
    assert not R.full_gate(copy.deepcopy(item),'solver',old,providers())['admitted'] and m(copy.deepcopy(item),'solver',old,providers())['admitted']
    return ['checker-feed enforcement removal','cap hides real feed failure','unknown-RSS admission','binary-drift admission',
            'safety dominance removal','generic empty acceptance','TIMEOUT hides completed bad replay','old persistent markers dropped from gate']


def resource_stop_init_control(root,contract,h):
    """ACTUAL M9 runner: a lone resource STOP is reported in the full union and deferred with its own class."""
    shadow = shadow_lane(root,'resource-stop-shadow',contract); scope(shadow)
    (shadow/'cycle2/STOP-m2r12').write_text('CONTROL resource stop only')
    saved,calls = (C.LANE,TX.L,R.Capacity,O.execute,sys.argv,C.load),[]
    class AlreadyHeld:
        def __enter__(self): return self
        def __exit__(self,*a): pass
    def forbidden(*a,**k):
        calls.append('owner must not run'); raise AssertionError('resource stop bypassed')
    try:
        C.LANE = TX.L = shadow; C.load = scoped_contract(contract,contract['_control_contract_path'],h)
        R.Capacity = lambda *a,**k: AlreadyHeld(); O.execute = forbidden
        sys.argv = [str(L/'src/run_m2_ms09_k1_v6_1.py'),contract['_control_contract_path'],h,'--max-attempts','1']
        TX.main()
    finally:
        C.LANE,TX.L,R.Capacity,O.execute,sys.argv,C.load = saved
    deferred = [json.loads(p.read_bytes()) for p in (shadow/'cycle2/m2k3-chunks').glob('*/initialization-deferred.json')]
    assert not calls and len(deferred) == 1 and deferred[0]['init_stage'] == 'resource-stop', deferred
    union = deferred[0]['veto_detail']['admission_union']
    assert union == {'resource_stops':['STOP-m2r12'],'persistent_vetoes':[]}, union
    return {'deferred':deferred[0],'owner_calls':0}


def m6_old_marker_control(root,path6,sha6):
    """ACTUAL M6 adapter: its frozen contract is validated at the production root first, then served to a scoped
    shadow containing only an OLD persistent v1 marker. Inventory/veto scan must refuse before any claim/native."""
    assert E.digest(path6) == sha6
    c6 = M6.COMMON.read(path6); M6.verify(c6)
    shadow = root/'m6-old-marker-shadow'; shadow.mkdir()
    def link(rel):
        target = shadow/rel
        if target.exists(): return
        target.parent.mkdir(parents=True,exist_ok=True); os.symlink(str(L/rel),target)
    for rel in c6['source_sha256']:
        p = shadow/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes((L/rel).read_bytes())
    link(M6.QUEUE); link(M6.SK)
    for row in c6['rows']:
        if row['original_record']: link(row['original_record'])
    scope(shadow)
    (shadow/'cycle2/m2k1-HALT.flag').write_text('{"CONTROL":"old persistent v1 marker"}')
    saved = (M6.L,M6.COMMON.LANE,M6.verify,R.Capacity,R.create_census,R.census_for_gate,M6.OWNER.execute,sys.argv)
    original_capacity,calls = R.Capacity,[]
    def scoped_verify(c):
        assert c == c6, 'scoped M6 adapter serves only the production-validated contract'
    def forbidden(*args,**kwargs):
        calls.append('M6 owner must not run'); raise AssertionError('old-marker veto bypassed')
    try:
        M6.L = M6.COMMON.LANE = shadow; M6.verify = scoped_verify
        R.Capacity = lambda deadline,lane=None,metadata=False,wait_allowance=2550: original_capacity(deadline,shadow,metadata,wait_allowance)
        R.create_census = lambda lane=shadow: saved[4](lane)
        R.census_for_gate = lambda ref,force=False,lane=shadow: saved[5](ref,force,lane)
        M6.OWNER.execute = forbidden
        sys.argv = [str(L/'src/run_m2_ms06_direct_v6_1.py'),str(Path(path6).resolve()),sha6,'--max-attempts','1']
        M6.main()
    finally:
        M6.L,M6.COMMON.LANE,M6.verify,R.Capacity,R.create_census,R.census_for_gate,M6.OWNER.execute,sys.argv = saved
    deferred = [json.loads(p.read_bytes()) for p in (shadow/'cycle2/m2k3-chunks').glob('ms06-*/initialization-deferred.json')]
    assert not calls and len(deferred) == 1 and deferred[0]['init_stage'] == 'veto-scan', deferred
    assert deferred[0]['veto_markers'] == ['m2k1-HALT.flag'] and deferred[0]['native_has_started'] is False
    assert not (shadow/'cycle2/claims').exists() or not list((shadow/'cycle2/claims').iterdir())
    return {'deferred':deferred[0],'claims_created':0,'owner_calls':0}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--child':
        child(sys.argv[2],Path(sys.argv[3]),sys.argv[4:]); return
    if len(sys.argv) == 3 and sys.argv[1].endswith('.job.json'):
        time.sleep(30); return  # control-only fake worker; the safety-trip control stops it via the real supervisor
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256')
    ap.add_argument('ms06_contract'); ap.add_argument('ms06_sha256'); args = ap.parse_args()
    R.install_handlers()
    root = L/'cycle2'/('v6_1_1-required-controls-'+str(time.time_ns())); root.mkdir()
    out = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'schema':'PA19-V6_1_1-REQUIRED-CONTROLS-v1','production_coverage':False,
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
                ('delayed-real-feed-failure-across-bounded-exit',{'delayed_publication':True,'fd_error':'solver-write'}),
                ('delayed-feed-removed-join-MUTANT-must-lose-veto',{'delayed_publication':True,'fd_error':'solver-write','mutant_no_settle':True}),
                ('post-Popen-exception',{'start_failure':True}),('collector-Thread.start-exception',{'thread_failure':True}),
                ('post-Popen-plus-receipt-OSError',{'start_failure':True,'receipt_error':True})]:
                entry = native_case(root,name,**opts); natives.append(entry)
                reasons = {'valid-full-feed':None,'solver-prefix':'completed CNF delivery differs from pinned formula: solver',
                    'checker-prefix':'completed CNF delivery differs from pinned formula: checker',
                    'solver-write-error':'CNF transport failure (not bound-induced cancellation): solver',
                    'checker-write-error':'CNF transport failure (not bound-induced cancellation): checker',
                    'solver-close-error':'CNF FIFO close failed: solver','checker-close-error':'CNF FIFO close failed: checker',
                    'real-SAT-invalid-proof':'checker NOT VERIFIED',
                    'delayed-real-feed-failure-across-bounded-exit':'CNF transport failure (not bound-induced cancellation): solver',
                    'delayed-feed-removed-join-MUTANT-must-lose-veto':'declared proof cap; not certified',
                    'post-Popen-exception':'incomplete native lifecycle: '+repr(RuntimeError('CONTROL post-Popen exception')),
                    'collector-Thread.start-exception':'incomplete native lifecycle: '+repr(RuntimeError('CONTROL collector start failure')),
                    'post-Popen-plus-receipt-OSError':'incomplete native lifecycle: '+repr(RuntimeError('CONTROL post-Popen exception'))}
                wanted = {'valid-full-feed':('UNSAT','VALIDATED'),'delayed-feed-removed-join-MUTANT-must-lose-veto':('UNKNOWN','NOT_EVALUATED')}.get(name,('UNKNOWN','INVALID'))
                assert (entry['status'],entry['integrity_status']) == wanted, (name,entry,wanted)
                assert entry['unknown_reason'] == reasons[name], (name,entry['unknown_reason'],reasons[name])
            out['families']['1_exceptional_ownership'] = [x for x in natives if 'exception' in x['name'] or 'OSError' in x['name']]
            out['families']['1_late_leader_reap'] = late_reap_control(root)
            out['families']['3_measured_native_transport'] = [x for x in natives if x not in out['families']['1_exceptional_ownership']]
            out['families']['3_safety_dominates_worker_UNKNOWN'] = safety_dominance_control()
            out['families']['5_6_publisher_reader_inventory_runner_veto'] = coverage_controls(root,c,args.sha256)
            out['families']['5_no_automatic_retry'] = no_retry_control(root,c,args.sha256)
            out['families']['refusal_rules_and_real_safety_trip'] = refusal_controls(root,c,args.sha256)
            out['families']['1_M6_old_marker_initialization_veto'] = m6_old_marker_control(root,args.ms06_contract,args.ms06_sha256)
            out['families']['5_resource_stop_initialization_class'] = resource_stop_init_control(root,c,args.sha256)
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
