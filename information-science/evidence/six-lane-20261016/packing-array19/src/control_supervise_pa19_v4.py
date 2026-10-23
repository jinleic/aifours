#!/usr/bin/env python3
"""Deterministic PRIVATE control for supervise_pa19_v4.py (bounded re-poll); not production coverage.
It reproduces the record signature observed at 2026-10-18 08:45 ('leader exits, first poll None': completed_cleanly
false, leader_returncode None, no trip) by injection, not by the live kernel race: the exact retained Popen is an
instrumented subclass whose first N poll() calls return None WITHOUT waitpid; later calls are the real poll(). The
pinned v3/v4 files are loaded unchanged; only their module-global name `subprocess` is replaced, for the duration of
one case, by a namespace providing that Popen and the real DEVNULL (the only two names the adapter uses).
One lane token is held (metadata Capacity); children are `python -I -B -c ...`, never setuid; the only signal is the
adapter's own wall-trip SIGTERM to its own group (cases G/H). After each case the control reaps the child with
Popen.wait() (no timeout) only when the record shows no survivor. Records/receipt are creation-only.
Cases:
  A v3 inject1 exit0          -> unclean, returncode None, one poll          (reproduces the production record)
  B v4 inject1 exit0          -> clean, returncode 0; a REAL poll >= 10 ms after the injected one observed the exit
  C v4 never reapable (inject all) exit0 -> unclean, returncode None; re-poll bounded: span >= 5 s and < 6 s
  D v4 inject1 exit3          -> unclean, returncode 3 (re-poll observes a nonzero exit; predicate unchanged)
  E v4 no injection exit0     -> clean, returncode 0 (normal path)
  G v4 inject1 wall trip      -> trip 'wall cap', exactly ONE poll (no re-poll when a reason is set), unclean
  H v3 inject1 wall trip      -> same observable outcome as G
"""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import time
import types
from pathlib import Path

import m2_supervised_runtime_v6 as R6

L = Path(__file__).resolve().parent.parent
PINS = {'v3':('src/supervise_pa19_v3.py','79c463589c9c5d60fddff7c4397a4e90339bdb0f5a0b2542c865c02a387573b3'),
        'v4':('src/supervise_pa19_v4.py','3b5c1808813a1f0627a4ebb721f197294659ddd66fcc7ecc09213b972c4b9f17')}
CAP = R6.GROUP_RSS_CAP


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(label):
    rel,h = PINS[label]
    assert digest(L/rel) == h, ('pinned supervisor changed',rel)
    spec = importlib.util.spec_from_file_location('control_supervise_'+label,str(L/rel))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


class Instrumented(subprocess.Popen):
    def __init__(self,*args,inject=0,**kwargs):
        self.inject, self.calls = inject, []
        super().__init__(*args,**kwargs)

    def poll(self):
        t = time.monotonic()
        if len(self.calls) < self.inject:
            self.calls.append({'t':t,'returned':None,'injected':True})
            return None
        rc = super().poll()
        self.calls.append({'t':t,'returned':rc,'injected':False})
        return rc


def run_case(out,name,mod,label,code,inject,wall):
    made = []

    def factory(*args,**kwargs):
        p = Instrumented(*args,inject=inject,**kwargs); made.append(p); return p
    saved = mod.subprocess
    mod.subprocess = types.SimpleNamespace(Popen=factory,DEVNULL=subprocess.DEVNULL)
    owned = []
    try:
        rec = mod.supervise([sys.executable,'-I','-B','-c',code],'CONTROL-'+name,wall,CAP,R6.FLOOR,str(L),
                            str(out/(name+'.supervisor.json')),str(out/(name+'.quarantine.json')),grace=10.0,owner_child=owned)
    finally:
        mod.subprocess = saved
    assert len(made) == 1 and owned == made, 'exact retained Popen not observed'
    child = made[0]; calls = list(child.calls)
    stop = rec.get('stop') or {}
    survivor = bool(stop.get('survivors') or (stop and not stop.get('listing_ok')) or rec.get('uncertain') or rec.get('quarantine_record'))
    reaped = None if survivor else child.wait()
    real = [c for c in calls if not c['injected']]
    return {'case':name,'module':label,'module_sha256':PINS[label][1],'child_code':code,'inject':'all' if inject >= 10**6 else inject,
            'wall_seconds':wall,'record':str((out/(name+'.supervisor.json')).relative_to(L)),'record_sha256':digest(out/(name+'.supervisor.json')),
            'completed_cleanly':rec['completed_cleanly'],'leader_returncode':rec['leader_returncode'],'trip_reason':rec['trip_reason'],
            'uncertain':rec['uncertain'],'quarantine_record':rec['quarantine_record'],'stop_survivors':stop.get('survivors'),
            'poll_calls':len(calls),'injected_calls':len(calls)-len(real),
            'first_real_offset_s':round(real[0]['t']-calls[0]['t'],4) if real and calls else None,
            'last_returned':calls[-1]['returned'] if calls else None,'poll_span_s':round(calls[-1]['t']-calls[0]['t'],4) if calls else None,
            'natural_race_on_first_real_poll':bool(real) and real[0]['returned'] is None,
            'reaped_by_control_returncode':reaped,'not_waited_because_possible_survivor':survivor}


def expect(r):
    n = r['case']
    if n == 'A': return (r['completed_cleanly'] is False and r['leader_returncode'] is None and r['trip_reason'] is None and r['poll_calls'] == 1
                         and r['injected_calls'] == 1 and r['reaped_by_control_returncode'] == 0)
    if n == 'B': return (r['completed_cleanly'] is True and r['leader_returncode'] == 0 and r['trip_reason'] is None and r['injected_calls'] == 1
                         and r['poll_calls'] >= 2 and r['first_real_offset_s'] >= 0.009 and r['last_returned'] == 0 and r['poll_span_s'] < 5.1)
    if n == 'C': return (r['completed_cleanly'] is False and r['leader_returncode'] is None and r['trip_reason'] is None
                         and r['injected_calls'] == r['poll_calls'] >= 2 and 5.0 <= r['poll_span_s'] < 6.0 and r['reaped_by_control_returncode'] == 0)
    if n == 'D': return (r['completed_cleanly'] is False and r['leader_returncode'] == 3 and r['trip_reason'] is None and r['injected_calls'] == 1
                         and r['last_returned'] == 3 and r['reaped_by_control_returncode'] == 3)
    if n == 'E': return r['completed_cleanly'] is True and r['leader_returncode'] == 0 and r['trip_reason'] is None and r['injected_calls'] == 0
    if n in ('G','H'): return (r['completed_cleanly'] is False and str(r['trip_reason']).startswith('wall cap') and r['poll_calls'] == 1
                               and r['injected_calls'] == 1 and r['leader_returncode'] is None and not r['uncertain'] and r['quarantine_record'] is None
                               and r['reaped_by_control_returncode'] == -15)
    raise KeyError(n)


def main():
    out = L/'cycle2'/('supervise-v4-control-%s' % time.strftime('%Y%m%dT%H%M%S')); out.mkdir(exist_ok=False)
    started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    mods = {k:load(k) for k in PINS}
    plan = [('A','v3','pass',1,60.0),('B','v4','pass',1,60.0),('C','v4','pass',10**9,60.0),('D','v4','import sys; sys.exit(3)',1,60.0),
            ('E','v4','pass',0,60.0),('G','v4','import time; time.sleep(30)',1,1.0),('H','v3','import time; time.sleep(30)',1,1.0)]
    rows = []
    for name,label,code,inject,wall in plan:
        r = run_case(out,name,mods[label],label,code,inject,wall); r['expected_ok'] = expect(r); rows.append(r)
        print(json.dumps({k:r[k] for k in ('case','module','completed_cleanly','leader_returncode','trip_reason','poll_calls','poll_span_s','expected_ok')}),flush=True)
    receipt = {'schema':'PA19-SUPERVISE-V4-CONTROL-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'control_source_sha256':digest(__file__),'pins':{k:{'path':v[0],'sha256':v[1]} for k,v in PINS.items()},'python':sys.version.split()[0],
        'cases':rows,'all_expected':all(r['expected_ok'] for r in rows),'production_coverage':False,
        'scope':'injected first-poll-None reproduces the 08:45 record signature; the live kernel race itself is not reproduced'}
    with (out/'receipt.json').open('x') as f: json.dump(receipt,f,indent=1); f.write('\n')
    print(out/'receipt.json',digest(out/'receipt.json'),'all_expected',receipt['all_expected'],flush=True)


if __name__ == '__main__':
    R6.install_handlers()
    with R6.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R6.BASE_GATE+16*1024**2
        main()
