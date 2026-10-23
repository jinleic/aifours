#!/usr/bin/env python3
"""Read-only proof-of-absence scan for live processes of the OLD hard12/m2r12 lane routes before STOP retirement.
Inspects every same-user process: argv (sysctl KERN_PROCARGS2 via the frozen v6 runtime helper), cwd (lsof -d cwd),
and parent ancestry. Lists any process whose argv or cwd references this lane. Writes one creation-only receipt.
Classifies old-route matches by runner names; the parent's own review-desk processes are reported separately.
"""
import json
import os
import subprocess
import time
from pathlib import Path

import m2_supervised_runtime_v6 as R

L = R.LANE
OLD_ROUTE_MARKERS = ('run_m2_10.py','run_m2_11.py','run_m2_12.py','run_m2_13.py','run_m2_14.py','run_m2_15.py','run_hard12.py',
    'run_hard10.py','run_m2skel','run_m2partbatch','stream_check1','extend_','rss_watchdog','m2r12','hard12')


def cwd_map():
    out = subprocess.run(['/usr/sbin/lsof','-a','-u',str(os.getuid()),'-d','cwd','-Fpn'],capture_output=True,text=True).stdout
    result,pid = {},None
    for line in out.splitlines():
        if line.startswith('p'): pid = int(line[1:])
        elif line.startswith('n') and pid is not None: result[pid] = line[1:]
    return result


def main():
    sup,cap,lane = R.supervisor(),R._argmax(),str(L.resolve())
    cwd = cwd_map()
    rows = []
    for pid in sup.list_pids(4,os.geteuid()):
        try: argv = [a.decode('utf-8','replace') for a in R._argv(pid,cap)]
        except (OSError,ValueError): argv = None
        state,rss,ident = sup.probe(pid)
        c = cwd.get(pid)
        hits_argv = argv is not None and any(lane in a for a in argv)
        hits_cwd = c is not None and (c == lane or c.startswith(lane+'/'))
        if not (hits_argv or hits_cwd): continue
        joined = ' '.join(argv or [])
        rows.append({'pid':pid,'ppid':ident.get('ppid'),'pgid':ident.get('pgid'),'state':state,'rss_bytes':rss,'cwd':c,
                     'argv':argv,'old_route_match':[m for m in OLD_ROUTE_MARKERS if m in joined],
                     'parent_review_desk':'institute/runs/six-lane-2026-10-16/review' in joined})
    old = [r for r in rows if r['old_route_match'] and not r['parent_review_desk'] and r['state'] == 'alive']
    receipt = {'schema':'PA19-OLD-ROUTE-LIVENESS-SCAN-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'scanner_sha256':R.digest(__file__),'lane':lane,'processes_referencing_lane':rows,'live_old_route_processes':old,
        'old_route_absent':not old,'scope':'same-user processes; argv via KERN_PROCARGS2, cwd via lsof; read-only'}
    dest = L/'cycle2'/('old-route-liveness-scan-%s-%d.json' % (time.strftime('%Y%m%dT%H%M%S'),time.time_ns()))
    with dest.open('x') as f: json.dump(receipt,f,indent=1)
    print(dest,R.digest(dest),flush=True)
    print(json.dumps({'old_route_absent':receipt['old_route_absent'],'n_referencing':len(rows),
                      'live_old':[(r['pid'],r['old_route_match']) for r in old],
                      'others':[(r['pid'],r['state'],(r['argv'] or ['?'])[0][-60:],r['parent_review_desk']) for r in rows if r not in old]},indent=1),flush=True)


if __name__ == '__main__':
    main()
