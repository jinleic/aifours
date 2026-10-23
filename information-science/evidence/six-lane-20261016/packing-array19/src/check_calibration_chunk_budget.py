#!/usr/bin/env python3
"""Small metadata-only guard controls, one existing token. No scientific input, solver or checker is run.
Fake guard tests preserve base refusal/expiry/token polling; real <=0.03s alarms test no-child wait cancellation,
no extra signals to live/starting children and a private blocking-flock interruption. Five single-protection
mutants must be killed. All private fixture/receipt writes are creation-only, originals/evidence untouched.
"""
import fcntl
import hashlib
import json
import os
import signal
import threading
import time
import types
from pathlib import Path

import calibration_chunk_budget as B

LANE = Path(__file__).resolve().parent.parent


def fake():
    g = types.SimpleNamespace(ABORT=[False],SPAWNING=[False],ACTIVE=set(),_alock=threading.RLock(),flag=None,count_calls=0)
    g.AdmissionDenied = type('PrivateAdmissionDenied',(Exception,),{})
    g.admitted_reason = lambda: 'base refusal' if g.flag else ('abort' if g.ABORT[0] else None)
    def count():
        g.count_calls += 1
        return 2
    g.token_count = count
    return g


def suite(mod,root):
    checks = []
    g = fake()
    budget = mod.ChunkBudget(g,time.time()+100000)
    assert budget.reason() is None
    g.flag = True
    assert budget.reason() == 'base refusal'
    checks.append('base STOP/floor refusal preserved')
    g = fake()
    budget = mod.ChunkBudget(g,time.time()+100000)
    budget.deadline = time.monotonic()-1
    assert budget.reason() and 'allowance' in budget.reason()
    checks.append('expired post-wait admission refused')
    g = fake()
    budget = mod.ChunkBudget(g,time.time()+100000)
    with budget:
        budget.deadline = time.monotonic()-1
        denied = False
        try:
            g.token_count()
        except g.AdmissionDenied:
            denied = True
        assert denied and g.count_calls == 0
    checks.append('token-wait polling refuses before base token count')
    for mode in ('no-child','live-child','starting-child'):
        g = fake()
        child = types.SimpleNamespace(terminate_calls=0)
        # Hashable fake child; no native process exists and no terminate method is called.
        class Child:
            def poll(self): return None
            def terminate(self): child.terminate_calls += 1
        if mode == 'live-child':
            g.ACTIVE.add(Child())
        if mode == 'starting-child':
            g.SPAWNING[0] = True
        saved_reason,saved_count = g.admitted_reason,g.token_count
        budget = mod.ChunkBudget(g,time.time()+100000,chunk_seconds=30,reserve_seconds=0,allowance_seconds=0)
        raised = False
        try:
            with budget:
                signal.setitimer(signal.ITIMER_REAL,0.03)
                time.sleep(0.08)
        except g.AdmissionDenied:
            raised = True
        assert raised == (mode == 'no-child'), mode
        assert budget.alarm_fired and g.ABORT[0] and child.terminate_calls == 0, mode
        assert g.admitted_reason is saved_reason and g.token_count is saved_count and signal.getitimer(signal.ITIMER_REAL) == (0.0,0.0)
        checks.append('alarm '+mode+': abort/cancel wait, no extra signal, restore hooks')
    # Real blocking flock, on a private tiny file, interrupted while there is NO child.
    lp = root/('lock-'+str(time.time_ns()))
    with lp.open('x') as f:
        f.write('private control only\n')
    holder = os.open(lp,os.O_RDWR)
    waiter = os.open(lp,os.O_RDWR)
    fcntl.flock(holder,fcntl.LOCK_EX)
    g = fake()
    budget = mod.ChunkBudget(g,time.time()+100000,chunk_seconds=30,reserve_seconds=0,allowance_seconds=0)
    denied = False
    try:
        try:
            with budget:
                signal.setitimer(signal.ITIMER_REAL,0.03)
                fcntl.flock(waiter,fcntl.LOCK_EX)
                raise AssertionError('blocking waiter unexpectedly acquired')
        except g.AdmissionDenied:
            denied = True
        assert denied and g.ABORT[0]
        probe = os.open(lp,os.O_RDWR)
        held = False
        try:
            try: fcntl.flock(probe,fcntl.LOCK_EX|fcntl.LOCK_NB)
            except BlockingIOError: held = True
        finally:
            os.close(probe)
        assert held
    finally:
        os.close(waiter)
        fcntl.flock(holder,fcntl.LOCK_UN)
        os.close(holder)
    checks.append('private blocking-flock wait cancelled; holder capacity retained')
    return checks


def main():
    root = LANE/'cycle2'/('chunk-budget-controls-'+str(time.time_ns()))
    root.mkdir(exist_ok=False)
    source = Path(B.__file__).read_text()
    baseline = suite(B,root)
    changes = {
      'base_refusal': ('        if why:\n            return why','        if False:\n            return why'),
      'remaining_allowance': ('        if self.alarm_fired or time.monotonic()+self.allowance > self.deadline:','        if False:'),
      'token_poll': ('        if why:\n            raise self.guard.AdmissionDenied(why)\n        return self.base_count()','        if False:\n            raise self.guard.AdmissionDenied(why)\n        return self.base_count()'),
      'alarm_wait_cancel': ("            raise self.guard.AdmissionDenied('chunk/run reserved cutoff while waiting; no child started')",'            pass'),
      'alarm_abort': ('        self.guard.ABORT[0] = True','        self.guard.ABORT[0] = False')}
    kills = []
    for name,(anchor,replacement) in changes.items():
        assert source.count(anchor) == 1, name
        changed = source.replace(anchor,replacement,1)
        mod = types.ModuleType('chunk_budget_mutant_'+name)
        exec(compile(changed,'private-mutant-'+name,'exec'),mod.__dict__)
        error = None
        try:
            suite(mod,root)
        except Exception as exc:
            error = repr(exc)[:600]
        kills.append({'removed_protection':name,'mutant_sha256':hashlib.sha256(changed.encode()).hexdigest(),
                      'killed':error is not None,'observed_failure':error})
        assert error is not None, ('SURVIVED',name)
    record = {'host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'module_sha256':hashlib.sha256(source.encode()).hexdigest(),
              'controls':baseline,'control_count':len(baseline),'mutants':kills,'all_killed':all(x['killed'] for x in kills),
              'native_solvers_or_checkers_started':0,'scientific_inputs_changed':False,
              'scope':'new budget admission/alarm unit controls only; not native proof controls or an instantaneous wall/RSS-cap proof'}
    dest = root/'receipt.json'
    with dest.open('x') as f:
        json.dump(record,f,indent=1)
    print(dest)
    print(json.dumps({'controls':len(baseline),'mutants':len(kills),'all_killed':record['all_killed']}))


if __name__ == '__main__':
    main()
