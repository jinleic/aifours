#!/usr/bin/env python3
"""Seven required v2 pre-production control families; all outputs PRIVATE and excluded from scientific coverage.
Native fixtures use one REAL existing lane token, <=2 compute processes, unchanged reviewed supervise_r3 and
absolute argv. Private shadow token files test ownership/failed receipts without changing real COUNT or STOPs.
No /bin/ps/setuid helpers, SIGKILL, deletion, production CNF/proof copies, or rerun of parent's RC3 experiment.
Synthetic metadata controls test the reader, never certify a PA19 input. RSS observations are NOT hard-cap proofs.
"""
import argparse
import ast
import inspect as source_inspect
import copy
import fcntl
import hashlib
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
import m2_item_owner_v2 as O
import m2_ms09_contract as C
import m2_ms09_evidence as E
import m2_native_staged_v2 as N
import m2_supervised_runtime_v2 as R
import run_m2_ms09_k1 as TX

L = C.LANE
SELF = Path(__file__).resolve()
UNSAT = b'p cnf 1 2\n1 0\n-1 0\n'
SAT = b'p cnf 2 1\n1 2 0\n'


def dump(p,obj):
    p = Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f: json.dump(obj,f,indent=1)


def child(mode,path,extra):
    cfg = json.loads(Path(path).read_bytes())
    if mode == 'mark':
        dump(cfg['marker'],{'new_child':True}); return
    if mode == 'emit':
        kind = extra[0]
        if (cfg.get('start_failure') or cfg.get('thread_failure')) and kind == 'solver':
            signal.signal(signal.SIGTERM,signal.SIG_IGN)
            dump(cfg['marker'],{'pid':os.getpid(),'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z')})
            time.sleep(2.0)
            return
        with open(extra[1],'rb') as f: f.read()
        if kind == 'solver':
            with open(extra[2],'wb') as f: f.write(b'')
            output,rc = cfg.get('solver_lines','s UNSATISFIABLE\n'),20
        else:
            sys.stdin.buffer.read()
            output,rc = cfg.get('checker_lines','s VERIFIED\n'),cfg.get('checker_rc',0)
        sys.stdout.write(output); sys.stdout.flush()
        raise SystemExit(rc)
    assert mode == 'pipeline'
    original_gate = R.full_gate
    def controlled_gate(lease,phase,*args,**kwargs):
        providers = {'count':lambda:R.token_count(L),
            'free':lambda:(lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L)),
            'rss':lambda:R.lane_rss(L,os.getpgrp(),lease['owner_pid'])}
        return original_gate(lease,phase,Path(cfg['scope']),providers)
    R.full_gate = controlled_gate
    raw = SAT if cfg.get('real_negative') else UNSAT
    if cfg.get('feed_fault'):
        original_feed = N.feed_cnf
        def broken_feed(fifo,data,record,stop,deadline):
            side = 'checker' if 'checker' in str(fifo) else 'solver'
            if side == cfg['feed_fault']:
                original_feed(fifo,data[:len(data)//2],record,stop,deadline)
            else: original_feed(fifo,data,record,stop,deadline)
        N.feed_cnf = broken_feed
    if cfg.get('fd_error'):
        side,operation = cfg['fd_error'].split('-')
        target = Path(cfg['job']['workdir'])/(side+'-cnf.fifo')
        original_write,original_close = os.write,os.close
        def matches(fd):
            try: return os.fstat(fd).st_ino == target.stat().st_ino
            except OSError: return False
        def faulty_write(fd,data):
            if operation == 'write' and matches(fd): raise OSError('CONTROL successful-open CNF write exception')
            return original_write(fd,data)
        def faulty_close(fd):
            fail = operation == 'close' and matches(fd)
            original_close(fd)
            if fail: raise OSError('CONTROL final CNF close exception after actual close')
        os.write,os.close = faulty_write,faulty_close
    def commands(paths):
        if cfg.get('real_positive'):
            return ([N.KISSAT,'-q','-f','--seed=1','--time=600',paths['solver-cnf.fifo'],paths['proof.fifo']],
                    [N.DT,paths['checker-cnf.fifo'],'-i','-t','1200'])
        solver = [sys.executable,'-B',str(SELF),'--child','emit',str(path),'solver',paths['solver-cnf.fifo'],paths['proof.fifo']]
        checker = ([N.DT,paths['checker-cnf.fifo'],'-i','-t','1200'] if cfg.get('real_negative') else
            [sys.executable,'-B',str(SELF),'--child','emit',str(path),'checker',paths['checker-cnf.fifo']])
        return solver,checker
    def hook(p):
        if cfg.get('start_failure'):
            time.sleep(0.2)
            raise RuntimeError('CONTROL post-Popen/pre-collector-start exception')
    if cfg.get('thread_failure'):
        original_start = threading.Thread.start
        def failed_start(thread):
            if thread._target is N.collector:
                time.sleep(0.2)
                raise RuntimeError('CONTROL collector Thread.start failed after Popen')
            return original_start(thread)
        threading.Thread.start = failed_start
    result = N.pipeline(raw,cfg['job'],commands,hook if cfg.get('start_failure') else None)
    dump(cfg['result'],result)


def lease(deadline,tier=1,owner=None):
    return {'owner_pid':owner or os.getpid(),'projected_growth_bytes':R.ITEM_GROWTH,
        'accounting_envelope':{'known':True,'upper_bytes':R.ALL_PLANNED_RETAINED_BOUND+1024**3},
        'group_rss_cap_bytes':R.GROUP_CAPS[tier],'tier':tier,'busy_units':2,'lane_busy_ceiling':4,
        'exclusive_bigmem':tier == 2,'held_token_indices':list(range(8)) if tier == 2 else [0],
        'chunk_deadline_monotonic':deadline,'item_deadline_monotonic':deadline}


def scope(root):
    tok = root/'cycle2'/'tokens'; tok.mkdir(parents=True)
    (tok/'COUNT').write_text('2\n')
    for name in ['t%d' % i for i in range(8)]+['bigmem']:
        (tok/name).write_bytes(b'')


def lock_available(p):
    fd = os.open(p,os.O_RDWR)
    try:
        try: fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: return False
        fcntl.flock(fd,fcntl.LOCK_UN); return True
    finally: os.close(fd)


def native_case(root,name,**options):
    folder = root/name; folder.mkdir()
    priv = folder/'scope'; scope(priv)
    cfg = dict(options,scope=str(priv),result=str(folder/'worker.json'),marker=str(folder/'native-marker.json'))
    cfg['job'] = {'solver':'kissat','solver_seconds':600,'checker_seconds':1200,
        'lease':lease(time.monotonic()+8000,2),'workdir':str(folder/'fifo')}
    cp = folder/'config.json'; dump(cp,cfg)
    recpath = folder/('absent-parent/supervisor.json' if options.get('receipt_error') else 'supervisor.json')
    qpath = folder/('absent-parent/quarantine.json' if options.get('receipt_error') else 'quarantine.json')
    original_gate = R.full_gate
    actual_supervise = R.supervisor().supervise
    if options.get('receipt_error'):
        def short_control_grace(*args,**kwargs):
            kwargs['grace'] = 0.05  # fixture outlives this short grace; production remains60s
            return actual_supervise(*args,**kwargs)
        R.supervisor().supervise = short_control_grace
    R.full_gate = lambda item,phase,lane=None: original_gate(item,phase,priv,{
        'count':lambda:R.token_count(L),'free':lambda:(lambda s:s.f_bavail*s.f_frsize)(os.statvfs(L)),
        'rss':lambda:R.lane_rss(L,owner=os.getpid())})
    observations,done = [],threading.Event()
    def inspect_locks():
        while not done.is_set():
            marker = folder/'native-marker.json'
            if marker.exists():
                pid = json.loads(marker.read_bytes())['pid']
                state,_,_ = R.supervisor().probe(pid)
                observations.append({'at_monotonic':time.monotonic(),'native_state':state,
                    'token_free':[lock_available(priv/'cycle2'/'tokens'/('t%d' % i)) for i in range(8)],
                    'bigmem_free':lock_available(priv/'cycle2'/'tokens'/'bigmem')})
            time.sleep(0.02)
    watcher = threading.Thread(target=inspect_locks,daemon=True); watcher.start()
    try:
        with R.Capacity(time.monotonic()+8000,priv,tier=2) as cap:
            command = [sys.executable,'-B',str(SELF),'--child','pipeline',str(cp)]
            rec,gate = cap.supervise(command,'CONTROL-'+name,cfg['job']['lease'],recpath,qpath)
            assert rec is not None and gate['admitted'], (name,gate)
            assert cap.safe
    finally:
        done.set(); watcher.join(); R.full_gate = original_gate; R.supervisor().supervise = actual_supervise
    result = json.loads((folder/'worker.json').read_bytes())
    if options.get('start_failure') or options.get('thread_failure'):
        alive = [x for x in observations if x['native_state'] == 'alive']
        assert alive and all(not any(x['token_free']) and not x['bigmem_free'] for x in alive), 'ownership released while native alive'
        assert rec['uncertain'] is True and rec.get('trip_reason')
        if options.get('receipt_error'):
            assert rec.get('record_write_error') and rec.get('cleanup_exception')
    assert all(lock_available(priv/'cycle2'/'tokens'/('t%d' % i)) for i in range(8))
    assert lock_available(priv/'cycle2'/'tokens'/'bigmem')
    dump(folder/'control-receipt.json',{'result':result,'supervisor':rec,'lock_observations':observations,
        'all_private_flocks_available_only_after_known_quiescence':True,'production_coverage':False})
    return {'name':name,'status':result['status'],'result':result,'receipt':str((folder/'control-receipt.json').relative_to(L)),
            'sha256':E.digest(folder/'control-receipt.json'),'peak_sampled_rss_bytes':rec['peak_sampled_rss_bytes']}


def gate_controls(root):
    priv = root/'gate-scope'; scope(priv)
    base = lease(5000)
    good_rss = {'known':True,'rss_bytes':0,'current_group_and_owner_bytes':0}
    def gate(item=None,phase='solver',**changes):
        pp = {'count':lambda:2,'free':lambda:R.BASE_GATE+R.ITEM_GROWTH,'rss':lambda:copy.deepcopy(good_rss),'clock':lambda:0}
        for key,value in changes.items(): pp[key] = value if callable(value) else (lambda v=value:v)
        return R.full_gate(item or base,phase,priv,pp)
    assert gate()['admitted']
    rows = []
    tests = [('floor-minus1',{'free':R.BASE_GATE+R.ITEM_GROWTH-1}),('count3',{'count':3}),('count-unknown',{'count':None}),
             ('count0',{'count':0}),('rss-unknown',{'rss':{'known':False}}),('rss-headroom',{'rss':{'known':True,'rss_bytes':R.LANE_CAP,'current_group_and_owner_bytes':0}}),
             ('deadline',{'clock':3000}),('sampler-error',{'free':lambda:(_ for _ in ()).throw(OSError('CONTROL sampler'))})]
    for name,changes in tests:
        r = gate(**changes); assert not r['admitted']; rows.append({'name':name,'errors':r['errors']})
    for key,value in [('accounting_envelope',{'known':False}),('projected_growth_bytes',0),('busy_units',3),('tier',True),('held_token_indices',[])]:
        b = copy.deepcopy(base); b[key] = value
        r = gate(b); assert not r['admitted']; rows.append({'name':'lease-'+key,'errors':r['errors']})
    for name in ('STOP-m2r12','m2k1-SAT.flag','m2k1-INVALID.flag','m2k1-HALT.flag'):
        s = root/('stop-scope-'+name.replace('.','_')); scope(s); (s/'cycle2'/name).write_text('CONTROL')
        r = R.full_gate(base,'solver',s,{'count':lambda:2,'free':lambda:R.BASE_GATE+R.ITEM_GROWTH,'rss':lambda:copy.deepcopy(good_rss),'clock':lambda:0})
        assert not r['admitted']; rows.append({'name':'post-lock-'+name,'errors':r['errors']})
    t2 = lease(5000,2); assert gate(t2)['admitted']
    t2['exclusive_bigmem'] = False; assert not gate(t2)['admitted']
    return rows


def postwait_controls(root):
    rows = []
    for change in ('STOP','floor'):
        folder = root/('postwait-'+change); folder.mkdir()
        priv = folder/'scope'; scope(priv)
        big = os.open(priv/'cycle2/tokens/bigmem',os.O_RDWR); fcntl.flock(big,fcntl.LOCK_EX)
        entered,finish = threading.Event(),threading.Event()
        original_hold,original_gate = R.Capacity._hold,R.full_gate
        free = [R.BASE_GATE+R.ITEM_GROWTH]
        def hold(cap,path,index=None):
            if Path(path).name == 'bigmem': entered.set()
            return original_hold(cap,path,index)
        R.Capacity._hold = hold
        R.full_gate = lambda item,phase,lane=None: original_gate(item,phase,priv,{'count':lambda:2,'free':lambda:free[0],
            'rss':lambda:{'known':True,'rss_bytes':0,'current_group_and_owner_bytes':0}})
        observation = {}
        config = folder/'marker-config.json'; dump(config,{'marker':str(folder/'FORBIDDEN-child.json')})
        def wait_and_admit():
            try:
                with R.Capacity(time.monotonic()+8000,priv,tier=2) as cap:
                    rec,gate = cap.supervise([sys.executable,'-B',str(SELF),'--child','mark',str(config)],
                        'CONTROL-postwait',lease(time.monotonic()+8000,2),folder/'supervisor.json',folder/'quarantine.json')
                    observation.update(record=rec,gate=gate)
            except BaseException as exc: observation['error'] = repr(exc)
            finally: finish.set()
        thread = threading.Thread(target=wait_and_admit,daemon=True); thread.start()
        try:
            assert entered.wait(5), 'tier2 never reached held bigmem wait'
            if change == 'STOP': (priv/'cycle2/STOP-m2r12').write_text('CONTROL changed DURING wait')
            else: free[0] -= 1
            fcntl.flock(big,fcntl.LOCK_UN); os.close(big); big = None
            assert finish.wait(5), observation
            assert observation.get('record') is None and observation['gate']['admitted'] is False
            expected = 'STOP' if change == 'STOP' else 'growth/floor'
            assert any(expected in e for e in observation['gate']['errors']), observation
            assert not (folder/'FORBIDDEN-child.json').exists() and not (folder/'supervisor.json').exists()
            rows.append({'change':change,'gate':observation['gate'],'new_supervised_children':0})
        finally:
            if big is not None: fcntl.flock(big,fcntl.LOCK_UN); os.close(big)
            R.Capacity._hold,R.full_gate = original_hold,original_gate
    cancelled = R._CANCEL[0]
    R._CANCEL[0] = True
    try:
        g = R.full_gate(lease(time.monotonic()+8000),'solver',priv,{'count':lambda:2,
            'free':lambda:R.BASE_GATE+R.ITEM_GROWTH,'rss':lambda:{'known':True,'rss_bytes':0,'current_group_and_owner_bytes':0}})
        assert not g['admitted'] and 'owner cancelled' in g['errors']
    finally: R._CANCEL[0] = cancelled
    return rows


def feed_and_verdict_controls(root):
    h = hashlib.sha256(UNSAT).hexdigest()
    feed = {'bytes':len(UNSAT),'sha256':h,'complete':True,'close_ok':True,'error':None}
    proof_sha = hashlib.sha256(b'').hexdigest()
    base = {'cnf_bytes':len(UNSAT),'cnf_sha256':h,'solver_rc':20,'checker_rc':0,
        'solver_collector':{'complete':True,'error':None,'status_lines':['s UNSATISFIABLE']},
        'checker_collector':{'complete':True,'error':None,'status_lines':['s VERIFIED']},
        'cnf_feeds':{'solver':copy.deepcopy(feed),'checker':copy.deepcopy(feed)},
        'proof_stream':{'reader_complete':True,'reader_error':None,'raw_bytes':0,'raw_sha256':proof_sha},
        'proof_delivery':{'bytes':0,'sha256':proof_sha,'complete':True,'close_ok':True,'error':None}}
    assert N.outcome(base) == ('UNSAT',False)
    rows = []
    for side in ('solver','checker'):
        for field,val in [('bytes',len(UNSAT)-1),('sha256','0'*64),('complete',False),('close_ok',False),('error','CONTROL write failure')]:
            r = copy.deepcopy(base); r['cnf_feeds'][side][field] = val
            assert N.outcome(r) == ('INVALID',True); rows.append(side+'-feed-'+field)
    for side,lines in [('solver',[]),('solver',['s UNSATISFIABLE']*2),('solver',['s SATISFIABLE','s UNSATISFIABLE']),
                       ('checker',['s NOT VERIFIED']),('checker',['s VERIFIED']*2),('checker',[' s VERIFIED']),('checker',[])]:
        r = copy.deepcopy(base); r[side+'_collector']['status_lines'] = lines
        assert N.outcome(r) == ('INVALID',True); rows.append(side+'-lines-'+repr(lines))
    for field in ('complete','close_ok'):
        r = copy.deepcopy(base); r['proof_delivery'][field] = False
        assert N.outcome(r) == ('INVALID',True); rows.append('proof-delivery-'+field)
    r = copy.deepcopy(base); r['checker_collector']['status_lines'] = ['s TIMEOUT']; assert N.outcome(r) == ('UNKNOWN',False)
    r = copy.deepcopy(base); r['solver_rc'] = 0; r['solver_collector']['status_lines'] = []; assert N.outcome(r) == ('UNKNOWN',False)
    for raw,expected in [(b's VERIFIED\r\n',['s VERIFIED']),(b's VER\rIFIED\n',['s VERIFIED']),
                         (b' s VERIFIED\n',[]),(b's NOT VERIFIED\n',['s NOT VERIFIED'])]:
        out = {}; N.collector(io.BytesIO(raw),out)
        assert out['complete'] and out['status_lines'] == expected
    # Failed proof writes / failed final close count only actual successful delivery.
    zc = N.zstd.ZstdCompressor(level=1); packed = zc.compress(b'abc')+zc.flush()
    class Sink:
        def __init__(self,fail_write=False,fail_close=False): self.fail_write,self.fail_close = fail_write,fail_close
        def write(self,data):
            if self.fail_write: raise BrokenPipeError('CONTROL proof write')
            return len(data)
        def close(self):
            if self.fail_close: raise BrokenPipeError('CONTROL proof close')
    for write,close in ((True,False),(False,True)):
        out = {}; N.replay([packed],Sink(write,close),out)
        assert not out['complete'] and out['error'] and out['bytes'] == (0 if write else 3)
    # No actual process for FIFO open stall: finite deadline reports UNKNOWN-compatible incomplete feed.
    p = root/'unread.fifo'; os.mkfifo(p)
    out = {}; N.feed_cnf(str(p),UNSAT,out,threading.Event(),time.monotonic()+0.05)
    assert out['complete'] is False and out['bytes'] == 0 and out['error']
    # Exact narrow compressed flush-tail boundary, with all production constants restored afterward.
    for margin,hit in ((0,False),(-1,True)):
        folder = root/('tail-'+str(margin)); folder.mkdir(); fifo = folder/'proof.fifo'; os.mkfifo(fifo)
        zc = N.zstd.ZstdCompressor(level=1); expected = zc.compress(b'abcdef')+zc.flush()
        old = N.MAX_ZBUF; N.MAX_ZBUF = len(expected)+margin
        thread = threading.Thread(target=lambda:(lambda f:(f.write(b'abcdef'),f.close()))(open(fifo,'wb')),daemon=True); thread.start()
        state = {}; N.proof_reader(str(fifo),state,threading.Event()); thread.join(); N.MAX_ZBUF = old
        assert bool(state.get('proof_cap_hit')) is hit and state['reader_complete'] is (not hit)
    return rows


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
    shadow = root/'transaction-shadow'; shadow.mkdir()
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
    old_c,old_tx = C.LANE,TX.L
    try:
        C.LANE = TX.L = shadow
        it = C.new_task(70,[0,24]); ca = copy.deepcopy(contract['cases'][70])
        expected = next(x['expected'] for x in contract['validation_tasks'] if x['id'] == it['id'])
        recipe = {'mode':'partbatch','multiset':9,'b_index':70,'indices':[0,24],
            'skeleton_path':contract['skeleton_path'],'skeleton_sha256':contract['skeleton_sha256'],
            'encoder_sha256':contract['source_sha256']['src/encode_skel_b.py'],'list_path':ca['list']['path'],
            'list_sha256':ca['list']['sha256'],'complete_denominator':ca['list']['n']}
        pin = {'schema':'PA19-K1-CNF-PIN-v2','production_contract_sha256':h,'multiset':9,'b_index':70,'indices':[0,24],
               'tier':1,'recipe':recipe,'cnf_sha256':expected['cnf_sha256'],'cnf_bytes':expected['cnf_bytes'],
               'source_sha256':contract['source_sha256'],'supervisor_sha256':R.SUP_SHA}
        ph = C.publish_json(shadow/it['pin'],pin,shadow/'stage')
        dump(shadow/'cycle2'/'m2k1-INVALID.flag',{'status':'INVALID','CONTROL':True})
        result = {'pipeline_schema':'PA19-SUPERVISED-DRAT-v2','status':'INVALID','checked':False,'halt_production':True,
                  'cnf_sha256':pin['cnf_sha256'],'cnf_bytes':pin['cnf_bytes'],'pre_child_pin_sha256':ph,'tier':1,
                  'native_result':{'status':'INVALID','checker_collector':{'status_lines':['s NOT VERIFIED']}}}
        TX.publish_item(result,contract,h,ca,it,shadow/'stage')
        q = C.inspect_new(contract,h,ca,it)
        assert q['state'] == 'INVALID' and any('persistent invalid verdict' in e for e in q['errors']), q
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
            sys.argv = [str(L/'src/run_m2_ms09_k1.py'),str(L/contract['_control_contract_path']),h,'--max-attempts','1']
            TX.main()
        finally:
            R.Capacity,O.execute,sys.argv = original_cap,original_owner,argv
        assert not calls and list((shadow/'cycle2'/'m2k1-chunks').glob('*/initialization-deferred.json'))
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
            rr = dict(result,status='UNKNOWN',checked=False,halt_production=False,native_result={},pre_child_pin_sha256=ph2)
            if variant == 'unknown-pipeline': rr['pipeline_schema'] = 'UNKNOWN'
            rb = (json.dumps(rr,indent=1)+'\n').encode()
            cc = {'schema':'PA19-K1-RECEIPT-v2','production_contract_sha256':h,'b_index':70,'indices':[0,24],
                  'tier':1,'pin_sha256':ph2,'record_sha256':'0'*64 if variant == 'bad-record-sha' else hashlib.sha256(rb).hexdigest()}
            if variant != 'omit-commit': C.publish_json(shadow/fixture['commit'],cc,shadow/'stage')
            if variant != 'interrupted-before-primary': C.publish_bytes(shadow/fixture['new_record'],rb,shadow/'stage')
            qq = C.inspect_new(contract,h,ca,fixture)
            expected_state = 'UNQUALIFIED' if variant == 'positive-UNKNOWN' else ('MISSING' if variant == 'interrupted-before-primary' else 'INVALID')
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


def retry_controls():
    cap = R.GROUP_CAPS[1]
    base = {'trip_reason':'aggregate RSS %d above %d' % (cap+1,cap),'uncertain':False,
            'stop':{'listing_ok':True,'survivors':[],'kill_error':None}}
    assert R.rss_only_retry(base,1)
    rows = []
    for name,edit in [('floor',lambda x:x.update(trip_reason='free bytes1 below floor12000000000')),
        ('wall',lambda x:x.update(trip_reason='wall cap2400 s')),('uncertain',lambda x:x.update(uncertain=True)),
        ('survivor',lambda x:x['stop'].update(survivors=[{'pid':1}])),('record-io',lambda x:x.update(record_write_error='CONTROL'))]:
        b = copy.deepcopy(base); edit(b); assert not R.rss_only_retry(b,1); rows.append(name)
    assert not R.rss_only_retry(base,2)
    assert not R.rss_only_retry(base,1,{'status':'INVALID'})
    return rows


def mutation_controls(root):
    """Three independent in-memory source omissions must be caught by their matching negative controls."""
    def mutant(fn,transform,name):
        tree = ast.parse(source_inspect.getsource(fn))
        tree = transform().visit(tree); ast.fix_missing_locations(tree)
        source = ast.unparse(tree)+'\n'
        (root/(name+'.py')).write_text(source)
        namespace = dict(fn.__globals__); exec(compile(tree,str(root/(name+'.py')),'exec'),namespace)
        return namespace[fn.__name__]
    class NoCheckerFeedLoop(ast.NodeTransformer):
        def visit_For(self,node):
            if ast.unparse(node.iter) == "result['cnf_feeds'].values()": return None
            return self.generic_visit(node)
    class UnknownRssAccepted(ast.NodeTransformer):
        def visit_Expr(self,node):
            if ast.unparse(node) == "errors.append('unknown RSS/headroom')": return ast.Pass()
            return self.generic_visit(node)
    class AnyEmptyCase(ast.NodeTransformer):
        def visit_Compare(self,node):
            if ast.unparse(node) == "ca['b_index'] == 3": return ast.Constant(value=True)
            return self.generic_visit(node)
    h = hashlib.sha256(UNSAT).hexdigest(); ph = hashlib.sha256(b'').hexdigest()
    f = {'bytes':len(UNSAT),'sha256':h,'complete':True,'close_ok':True,'error':None}
    r = {'cnf_bytes':len(UNSAT),'cnf_sha256':h,'solver_rc':20,'checker_rc':0,
        'solver_collector':{'complete':True,'error':None,'status_lines':['s UNSATISFIABLE']},
        'checker_collector':{'complete':True,'error':None,'status_lines':['s VERIFIED']},
        'cnf_feeds':{'solver':f,'checker':dict(f,bytes=len(UNSAT)-1)},
        'proof_stream':{'reader_complete':True,'reader_error':None,'raw_bytes':0,'raw_sha256':ph},
        'proof_delivery':{'bytes':0,'sha256':ph,'complete':True,'close_ok':True,'error':None}}
    m = mutant(N.outcome,NoCheckerFeedLoop,'mutant-omitted-checker-feed')
    assert N.outcome(r) == ('INVALID',True) and m(r) == ('UNSAT',False)
    p = root/'mutant-gate-scope'; scope(p)
    providers = {'count':lambda:2,'free':lambda:R.BASE_GATE+R.ITEM_GROWTH,'rss':lambda:{'known':False},'clock':lambda:0}
    m = mutant(R.full_gate,UnknownRssAccepted,'mutant-unknown-rss-accepted')
    assert not R.full_gate(lease(5000),'solver',p,providers)['admitted'] and m(lease(5000),'solver',p,providers)['admitted']
    m = mutant(C.structural_acceptance,AnyEmptyCase,'mutant-generic-empty-acceptance')
    case = {'b_index':0,'list':{'n':0,'sha256':C.B3.EXPECTED['empty_list_receipt']['sha256']}}
    c = {'skeleton_sha256':C.SKELETON_SHA}
    assert not C.structural_acceptance(c,case)['accepted'] and m(c,case)['accepted']
    return ['checker-CNF-delivery omission killed','unknown-RSS admission omission killed','exact-structural-case restriction omission killed']


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--child':
        child(sys.argv[2],Path(sys.argv[3]),sys.argv[4:]); return
    ap = argparse.ArgumentParser(); ap.add_argument('contract'); ap.add_argument('sha256'); args = ap.parse_args()
    R.install_handlers()
    root = L/'cycle2'/('v2-required-controls-'+str(time.time_ns())); root.mkdir()
    result = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'schema':'PA19-V2-SEVEN-CONTROL-FAMILIES-v1',
        'production_coverage':False,'control_source_sha256':E.digest(SELF),'contract_sha256':args.sha256,'families':{}}
    try:
        with R.Capacity(time.monotonic()+10800):  # one REAL token, no real bigmem; <=2 compute processes
            st = os.statvfs(L); assert st.f_bavail*st.f_frsize >= R.BASE_GATE+R.ITEM_GROWTH
            c = C.load(args.contract,args.sha256)
            c['_control_contract_path'] = str(Path(args.contract).resolve())
            result['families']['2_fresh_gate_boundaries'] = gate_controls(root)
            result['families']['2_postwait_STOP_floor_no_child'] = postwait_controls(root)
            result['families']['3_4_measured_feeds_and_verdict_predicates'] = feed_and_verdict_controls(root)
            natives = []
            for name,opts in [('valid-full-feed',{'real_positive':True}),('solver-prefix',{'feed_fault':'solver'}),
                ('checker-prefix',{'feed_fault':'checker'}),('solver-write-error',{'fd_error':'solver-write'}),
                ('checker-write-error',{'fd_error':'checker-write'}),('solver-close-error',{'fd_error':'solver-close'}),
                ('checker-close-error',{'fd_error':'checker-close'}),('real-SAT-invalid-proof',{'real_negative':True}),
                ('post-Popen-exception',{'start_failure':True}),('collector-Thread.start-exception',{'thread_failure':True}),
                ('post-Popen-plus-receipt-OSError',{'start_failure':True,'receipt_error':True})]:
                entry = native_case(root,name,**opts); natives.append(entry)
                expected = 'UNSAT' if name == 'valid-full-feed' else ('UNKNOWN' if opts.get('start_failure') or opts.get('thread_failure') else 'INVALID')
                assert entry['status'] == expected, (name,entry['status'],expected)
            result['families']['1_exceptional_ownership'] = [x for x in natives if 'exception' in x['name'] or 'OSError' in x['name']]
            result['families']['3_4_native_transport'] = [x for x in natives if x not in result['families']['1_exceptional_ownership']]
            result['families']['5_6_inventory_and_persistent_veto'] = coverage_controls(root,c,args.sha256)
            result['families']['7_actual_filetype_byte_accounting'] = accounting_controls(root)
            result['families']['tier2_sole_RSS_only'] = retry_controls()
            result['source_omission_mutants_killed'] = mutation_controls(root)
            result.update(status='PASS',finished_host_clock=time.strftime('%Y-%m-%dT%H:%M:%S%z'),
                resource_claim='small controlled observations only; no instantaneous production RSS-cap proof')
            dest = root/'receipt.json'; dump(dest,result)
            print(dest,E.digest(dest),flush=True)
    except BaseException as exc:
        result.update(status='FAIL_OR_DEFERRED',error=repr(exc),finished_host_clock=time.strftime('%Y-%m-%dT%H:%M:%S%z'))
        dest = root/'failure-receipt.json'; dump(dest,result)
        print(dest,E.digest(dest),flush=True)
        raise


if __name__ == '__main__':
    main()
