#!/usr/bin/env python3
"""Deterministic PRIVATE control for supervise_pa19_v5.py (safety-checked delayed reap); not production coverage.
The 08:45 record signature ('leader exits, first poll None') is reproduced by injection, not by the live kernel race:
the exact retained Popen is an instrumented subclass whose first N poll() calls return None WITHOUT waitpid. Events
inside the delayed-reap window are injected deterministically from inside poll(): a SIGTERM to this control process
(the supervisor's own handler records it), a statvfs shim reporting 0 free bytes, a probe wrapper reporting RSS above
the cap or an 'unknown' leader. The pinned v3/v5 files are loaded unchanged; only module-global names `subprocess`/`os`
are replaced for the duration of one case. One lane token is held (metadata Capacity); children are
`python -I -B -c ...`, never setuid; the only group signal is the adapter's own stop while the leader is unreaped.
After each case the control reaps the child (Popen.wait, no timeout) only when it is known exited.
Cases (expected):
  A  v3 inject1 exit0                    unclean, rc None, one poll (the production signature)
  B  v5 inject1 exit0                    clean rc0: the next real poll (after the safety checks) observed the exit
  C  v5 never reapable                   unclean rc None; polls stop by the 5 s bound (span <= 5.002 s)
  D  v5 inject1 exit3                    unclean rc3
  E  v5 no injection exit0               clean rc0
  G  v5 inject1 wall trip (monitor)      'wall cap', one poll, unclean        H  v3 same: same outcome
  I  v5 SIGTERM inside delayed reap      'external SIGTERM during delayed reap', stop while unreaped, observed_signal
  J  v5 wall exceeded inside delayed reap   'wall cap ... during delayed reap', unclean
  K  v5 floor breached inside delayed reap  'free bytes 0 below floor ... during delayed reap', unclean
  L  v5 RSS above cap inside delayed reap   'aggregate RSS ... during delayed reap', unclean
  M  v5 unknown leader inside delayed reap  uncertain trip + quarantine, unclean
  N  v5 SIGTERM right after the reap        'external SIGTERM before the completion record', no stop after reaping
"""
import hashlib
import importlib.util
import json
import os
import signal
import subprocess
import sys
import time
import types
from pathlib import Path

import m2_supervised_runtime_v6 as R6

L = Path(__file__).resolve().parent.parent
PINS = {'v3':('src/supervise_pa19_v3.py','79c463589c9c5d60fddff7c4397a4e90339bdb0f5a0b2542c865c02a387573b3'),
        'v5':('src/supervise_pa19_v5.py',None)}
CAP = R6.GROUP_RSS_CAP


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(label,sha):
    rel = PINS[label][0]
    assert digest(L/rel) == sha, ('pinned supervisor changed',rel)
    spec = importlib.util.spec_from_file_location('control_supervise5_'+label,str(L/rel))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


class Instrumented(subprocess.Popen):
    def __init__(self,*args,plan=None,**kwargs):
        self.plan, self.calls = plan or {}, []
        super().__init__(*args,**kwargs)

    def poll(self):
        t, n = time.monotonic(), len(self.calls)
        if n == 0 and self.plan.get('trigger') is not None: self.plan['trigger'][0] = True
        if self.plan.get('signal_at_call') == n: os.kill(os.getpid(),signal.SIGTERM)
        if n < self.plan.get('inject',0):
            self.calls.append({'t':t,'returned':None,'injected':True})
            return None
        rc = super().poll()
        self.calls.append({'t':t,'returned':rc,'injected':False})
        if rc is not None and self.plan.get('signal_on_reap') and not self.plan.get('sent'):
            self.plan['sent'] = True; os.kill(os.getpid(),signal.SIGTERM)
        return rc


class OsShim:
    """Real os except statvfs, which reports 0 free bytes once the trigger is set."""
    def __init__(self,trigger): self.trigger = trigger
    def __getattr__(self,name): return getattr(os,name)
    def statvfs(self,path):
        st = os.statvfs(path)
        return types.SimpleNamespace(f_bavail=0,f_frsize=st.f_frsize) if self.trigger[0] else st


def run_case(out,name,mod,label,sha,code,plan,wall,grace=10.0,floor_shim=False,probe_mode=None):
    made, trigger = [], [False]
    plan = dict(plan); plan['trigger'] = trigger

    def factory(*args,**kwargs):
        p = Instrumented(*args,plan=plan,**kwargs); made.append(p); return p
    real_probe = mod.probe

    def probe_fn(pid,pidinfo=None):
        st,rss,ident = real_probe(pid,pidinfo)
        if trigger[0] and probe_mode == 'rss' and pid == os.getpid(): return st,CAP+1,ident
        if trigger[0] and probe_mode == 'unknown' and made and pid == made[0].pid: return 'unknown',0,{}
        return st,rss,ident
    saved = (mod.subprocess,mod.os)
    mod.subprocess = types.SimpleNamespace(Popen=factory,DEVNULL=subprocess.DEVNULL)
    if floor_shim: mod.os = OsShim(trigger)
    owned = []
    try:
        rec = mod.supervise([sys.executable,'-I','-B','-c',code],'CONTROL5-'+name,wall,CAP,R6.FLOOR,str(L),
                            str(out/(name+'.supervisor.json')),str(out/(name+'.quarantine.json')),grace=grace,
                            probe_fn=probe_fn,owner_child=owned)
    finally:
        mod.subprocess,mod.os = saved
    assert len(made) == 1 and owned == made, 'exact retained Popen not observed'
    child = made[0]; calls = list(child.calls)
    state_now = real_probe(child.pid)[0] if child.returncode is None else 'reaped'
    reaped = child.returncode if child.returncode is not None else (child.wait() if state_now in ('zombie','gone') else None)
    real = [c for c in calls if not c['injected']]
    return {'case':name,'module':label,'module_sha256':sha,'child_code':code,'inject':'all' if plan.get('inject',0) >= 10**6 else plan.get('inject',0),
            'events':{k:plan.get(k) for k in ('signal_at_call','signal_on_reap') if plan.get(k) is not None} or None,
            'floor_shim':floor_shim,'probe_mode':probe_mode,'wall_seconds':wall,
            'record':str((out/(name+'.supervisor.json')).relative_to(L)),'record_sha256':digest(out/(name+'.supervisor.json')),
            'completed_cleanly':rec['completed_cleanly'],'leader_returncode':rec['leader_returncode'],'trip_reason':rec['trip_reason'],
            'uncertain':rec['uncertain'],'quarantine_record':rec['quarantine_record'],'stop_ran':rec.get('stop') is not None,
            'observed_signal':rec.get('observed_signal'),'poll_calls':len(calls),'injected_calls':len(calls)-len(real),
            'first_real_offset_s':round(real[0]['t']-calls[0]['t'],4) if real and calls else None,
            'last_returned':calls[-1]['returned'] if calls else None,'poll_span_s':round(calls[-1]['t']-calls[0]['t'],4) if calls else None,
            'reaped_by_control_or_record_returncode':reaped,'leader_state_after_case':state_now}


def expect(r):
    n, tr = r['case'], str(r['trip_reason'])
    if n == 'A': return r['completed_cleanly'] is False and r['leader_returncode'] is None and r['trip_reason'] is None and r['poll_calls'] == 1 and r['reaped_by_control_or_record_returncode'] == 0
    if n == 'B': return (r['completed_cleanly'] is True and r['leader_returncode'] == 0 and r['trip_reason'] is None and r['injected_calls'] == 1
                         and r['poll_calls'] >= 2 and r['first_real_offset_s'] is not None and r['last_returned'] == 0 and not r['stop_ran'])
    if n == 'C': return (r['completed_cleanly'] is False and r['leader_returncode'] is None and r['trip_reason'] is None and r['injected_calls'] == r['poll_calls'] >= 2
                         and 4.95 <= r['poll_span_s'] <= 5.002 and not r['stop_ran'] and r['reaped_by_control_or_record_returncode'] == 0)
    if n == 'D': return r['completed_cleanly'] is False and r['leader_returncode'] == 3 and r['trip_reason'] is None and r['last_returned'] == 3
    if n == 'E': return r['completed_cleanly'] is True and r['leader_returncode'] == 0 and r['trip_reason'] is None and r['injected_calls'] == 0
    if n in ('G','H'): return (r['completed_cleanly'] is False and tr.startswith('wall cap') and 'delayed reap' not in tr and r['poll_calls'] == 1
                               and r['stop_ran'] and not r['uncertain'] and r['quarantine_record'] is None and r['reaped_by_control_or_record_returncode'] == -15)
    if n == 'I': return (r['completed_cleanly'] is False and tr == 'external SIGTERM during delayed reap' and r['stop_ran'] and r['observed_signal'] == 'SIGTERM'
                         and r['quarantine_record'] is None and r['reaped_by_control_or_record_returncode'] == 0)
    if n == 'J': return r['completed_cleanly'] is False and tr.startswith('wall cap') and tr.endswith('during delayed reap') and r['stop_ran'] and r['reaped_by_control_or_record_returncode'] == 0
    if n == 'K': return r['completed_cleanly'] is False and tr.startswith('free bytes 0 below floor') and tr.endswith('during delayed reap') and r['stop_ran']
    if n == 'L': return r['completed_cleanly'] is False and tr.startswith('aggregate RSS') and tr.endswith('during delayed reap') and r['stop_ran']
    if n == 'M': return r['completed_cleanly'] is False and r['trip_reason'] is not None and r['uncertain'] is True and r['quarantine_record'] is not None and r['stop_ran']
    if n == 'N': return (r['completed_cleanly'] is False and tr == 'external SIGTERM before the completion record' and not r['stop_ran']
                         and r['leader_returncode'] == 0 and r['observed_signal'] == 'SIGTERM')
    raise KeyError(n)


def main(v5sha):
    out = L/'cycle2'/('supervise-v5-control-%s' % time.strftime('%Y%m%dT%H%M%S')); out.mkdir(exist_ok=False)
    started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    shas = {'v3':PINS['v3'][1],'v5':v5sha}
    mods = {k:load(k,shas[k]) for k in shas}
    ok, sleep30 = 'pass', 'import time; time.sleep(30)'
    plan = [('A','v3',ok,{'inject':1},60.0,{}),('B','v5',ok,{'inject':1},60.0,{}),('C','v5',ok,{'inject':10**9},60.0,{}),
            ('D','v5','import sys; sys.exit(3)',{'inject':1},60.0,{}),('E','v5',ok,{},60.0,{}),
            ('G','v5',sleep30,{'inject':1},1.0,{}),('H','v3',sleep30,{'inject':1},1.0,{}),
            ('I','v5',ok,{'inject':3,'signal_at_call':2},60.0,{}),('J','v5',ok,{'inject':10**9},1.0,{}),
            ('K','v5',ok,{'inject':1},60.0,{'floor_shim':True}),('L','v5',ok,{'inject':1},60.0,{'probe_mode':'rss'}),
            ('M','v5',ok,{'inject':1},60.0,{'probe_mode':'unknown','grace':2.0}),('N','v5',ok,{'inject':1,'signal_on_reap':True},60.0,{})]
    rows = []
    for name,label,code,pl,wall,kw in plan:
        r = run_case(out,name,mods[label],label,shas[label],code,pl,wall,**kw); r['expected_ok'] = expect(r); rows.append(r)
        print(json.dumps({k:r[k] for k in ('case','module','completed_cleanly','leader_returncode','trip_reason','stop_ran','poll_calls','poll_span_s','expected_ok')}),flush=True)
    receipt = {'schema':'PA19-SUPERVISE-V5-CONTROL-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'control_source_sha256':digest(__file__),'pins':{k:{'path':PINS[k][0],'sha256':shas[k]} for k in shas},'python':sys.version.split()[0],
        'cases':rows,'all_expected':all(r['expected_ok'] for r in rows),'production_coverage':False,
        'scope':'injected events reproduce record signatures and delayed-reap trips; the live kernel race itself is not reproduced'}
    with (out/'receipt.json').open('x') as f: json.dump(receipt,f,indent=1); f.write('\n')
    print(out/'receipt.json',digest(out/'receipt.json'),'all_expected',receipt['all_expected'],flush=True)


if __name__ == '__main__':
    R6.install_handlers()
    with R6.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R6.BASE_GATE+16*1024**2
        main(sys.argv[1])
