#!/usr/bin/env python3
"""Bounded operational checkpointing requested by the lane contract, not a solver-progress poller.
Write host time, aggregate observed owned-process RSS/CPU, and free disk to an exclusive JSONL stream every
15 minutes while the assistant may be blocked in wait's 30-minute safety cap. Never read solver logs or
infer SAT/UNSAT; native job completion receipts remain authoritative. This process sleeps between samples,
launches only a short ps command, and stops cooperatively on SIGTERM or at the fixed contract deadline.
An approaching resource limit ends the monitor with a warning so the background completion wakes the owner.
Usage: resource_checkpoints.py NEW_OUTDIR
"""
import lane_guard  # noqa: F401
import json
import os
import shutil
import signal
import subprocess
import sys
import threading
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEADLINE = datetime.fromisoformat('2026-10-18T18:31:43-07:00')
MARKERS = ('runs/b1f-fixed-kf6-s1-v2', 'runs/b1g-fixed-kf6-s1',
           'runs/b2-direct-p332-s1', 'runs/b2-direct-rd-p332-s1')


def main():
    out = sys.argv[1]
    os.mkdir(out)
    stopped = threading.Event()
    signal.signal(signal.SIGTERM, lambda *_: stopped.set())
    signal.signal(signal.SIGINT, lambda *_: stopped.set())
    with open(os.path.join(out, 'owner.json'), 'x') as fh:
        json.dump({'pid':os.getpid(), 'deadline':DEADLINE.isoformat(), 'interval_seconds':900,
                   'started_at_host':datetime.now().astimezone().isoformat()}, fh, indent=1)
    with open(os.path.join(out, 'resource-checkpoints.jsonl'), 'x') as stream:
        while not stopped.is_set():
            now = datetime.now().astimezone()
            if now >= DEADLINE:
                break
            text = subprocess.check_output(['ps','-axo','pid=,pcpu=,rss=,etime=,command='], text=True)
            rows=[]
            for line in text.splitlines():
                p=line.split(None,4)
                if len(p)==5 and any(k in p[4] for k in MARKERS):
                    if '/bin/zsh -c' in p[4] or 'codex exec ' in p[4] or 'claude ' in p[4]:
                        continue
                    rows.append({'pid':int(p[0]),'cpu_percent':float(p[1]),'rss_bytes':int(p[2])*1024,
                                 'elapsed':p[3],'command':p[4]})
            rss=sum(r['rss_bytes'] for r in rows)
            free=shutil.disk_usage(ROOT).free
            record={'host_time':now.isoformat(),'rss_bytes_observed_sum':rss,
                    'busy_at_sample':sum(r['cpu_percent']>=1 for r in rows),'host_free_disk_bytes':free,
                    'processes':rows,'scope':'operational sample only, no solver verdict or aggregate peak inferred'}
            warning = free < 12_200_000_000 or rss > 7_500_000_000
            record['resource_margin_warning']=warning
            stream.write(json.dumps(record)+'\n');stream.flush()
            print(json.dumps({k:record[k] for k in ('host_time','rss_bytes_observed_sum','busy_at_sample',
                                                    'host_free_disk_bytes','resource_margin_warning')}),flush=True)
            if warning:
                return 3
            stopped.wait(min(900,max(0,(DEADLINE-now).total_seconds())))
        stream.write(json.dumps({'host_time':datetime.now().astimezone().isoformat(),
                                 'monitor_stopped':True,'signal_received':stopped.is_set()})+'\n')
    return 0


if __name__=='__main__':
    sys.exit(main())
