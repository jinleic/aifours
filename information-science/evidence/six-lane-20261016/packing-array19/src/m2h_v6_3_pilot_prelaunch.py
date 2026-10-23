#!/usr/bin/env python3
"""Read-only prelaunch gate for the ONE bounded M2H v6_3 pipeline pilot frozen in a PRE-EXEC. It starts no native work and
creates no claim, pin, job or record. Fail-closed checks:
  hashes      every file bound by the PRE-EXEC, and the contract source map equals the PRE-EXEC copy and matches on disk;
  namespace   no v6_3 item artifact or claim exists, no M2H v6_3 chunk exists, nobody holds the singleton lock;
  registry    the shared admission union has no resource stop and no persistent veto;
  processes   no lane process other than the frozen monitors and this process's own ancestry; each monitor alive;
  clocks      frozen 17:20 admission / 17:57 native end leave the frozen launch headroom;
  disk        free >= 12.2e9 B + projected growth (whole-plan retained bound);
  preview     a gate preview newer than the PRE-EXEC, <= 600 s old, bound to the contract, every gate admitted;
  tokens      both lane tokens t0/t1 are unheld;
  long_job    the parent long-job disk-stability rule (applied although the pilot is expected to take minutes).
Usage: m2h_v6_3_pilot_prelaunch.py PRE_EXEC PRE_EXEC_SHA256 GATE_PREVIEW
Writes one creation-only receipt cycle2/m2h-v6_3-pilot-prelaunch-<stamp>.json; exit 0 iff every check passes.
"""
import datetime
import glob
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

L = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(L/'src'))
import m2_supervised_runtime_v6_3 as R  # noqa: E402  read-only use of admission_union


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def where(p):
    return Path(p) if str(p).startswith('/') else L/p


def epoch(text):
    return datetime.datetime.fromisoformat(text).timestamp()


def monitor_rule(path,rule,now):
    rows = [json.loads(s) for s in Path(path).read_text().splitlines()[-400:] if s.strip()]
    ts = [datetime.datetime.fromisoformat(r['t']) for r in rows]
    assert rows and all(t.tzinfo is not None for t in ts), 'monitor timestamps missing or not tz-aware'
    assert all(a < b for a,b in zip(ts,ts[1:])), 'monitor timestamps not strictly increasing'
    last = ts[-1].timestamp()
    out = {'samples_read':len(rows),'age_seconds':round(now-last,1)}
    assert 0 <= now-last <= rule['max_age_seconds'], 'parent monitor stale'
    win = [(t.timestamp(),int(r['free'])) for t,r in zip(ts,rows) if t.timestamp() >= last-rule['window_seconds']]
    out.update(window_samples=len(win),window_span_seconds=round(win[-1][0]-win[0][0],1),free_last=win[-1][1])
    assert len(win) >= rule['min_samples'] and win[-1][0]-win[0][0] >= rule['min_span_seconds'], 'monitor window too thin'
    peak,drop = -1,0
    for _,f in win:
        peak = max(peak,f); drop = max(drop,peak-f)
    limit = max(rule['drop_floor'],(win[-1][1]-rule['min_free'])/rule['runway_divisor'])
    out.update(max_peak_to_later_drop=drop,drop_limit=int(limit))
    assert win[-1][1] >= rule['min_free'] and drop <= limit, 'long-job disk-stability rule refuses'
    return out


def main():
    pre_path,pre_sha,gp_path = sys.argv[1:4]
    assert digest(pre_path) == pre_sha, 'PRE-EXEC hash differs'
    pre = json.loads(Path(pre_path).read_bytes())
    assert pre['schema'] == 'PA19-M2H-V6_3-PILOT-PRE-EXEC-v1'
    now,checks = time.time(),{}

    def run(name,fn):
        try: checks[name] = dict(fn() or {},ok=True)
        except Exception as exc: checks[name] = {'ok':False,'error':repr(exc)}

    def hashes():
        bad = {p:h for p,h in pre['bindings'].items() if digest(where(p)) != h}
        assert not bad, bad
        c = json.loads((L/pre['contract']['path']).read_bytes())
        assert c['source_sha256'] == pre['contract']['source_sha256'], 'contract source map differs from the PRE-EXEC copy'
        bad = {p:h for p,h in c['source_sha256'].items() if digest(L/p) != h}
        assert not bad, bad
        return {'bindings':len(pre['bindings']),'contract_sources':len(c['source_sha256'])}

    def namespace():
        found = sorted(glob.glob(str(L/'cycle2/m2skel_drat/*_h6_3*'))+glob.glob(str(L/'cycle2/claims/m2h6_3_*')))
        chunks = sorted(os.listdir(L/'cycle2/m2h6_3-chunks')) if (L/'cycle2/m2h6_3-chunks').exists() else []
        assert not found and not chunks, (found[:5],chunks[:5])
        lock = L/'cycle2/m2h-v6_3-singleton.lock'
        holders = subprocess.run(['/usr/sbin/lsof','-t',str(lock)],capture_output=True,text=True).stdout.split() if lock.exists() else []
        assert not holders, ('singleton held',holders)
        return {'v6_3_item_artifacts_or_claims':0,'chunks':0,'singleton_lock_exists':lock.exists(),'singleton_holders':0}

    def registry():
        u = R.admission_union(L)
        assert not u['resource_stops'] and not u['persistent_vetoes'], u
        return {'admission_union':u}

    def processes():
        rows = {}
        for line in subprocess.run(['/bin/ps','-axo','pid=,ppid=,command='],capture_output=True,text=True,check=True).stdout.splitlines():
            parts = line.strip().split(None,2)
            if len(parts) >= 2: rows[int(parts[0])] = (int(parts[1]),parts[2] if len(parts) == 3 else '')
        mine,p = set(),os.getpid()
        while p in rows and p not in mine and p > 1:
            mine.add(p); p = rows[p][0]
        monitors = {m['pid']:m['marker'] for m in pre['monitors']}
        dead = {pid:mark for pid,mark in monitors.items() if pid not in rows or mark not in rows[pid][1]}
        assert not dead, ('monitor not alive',dead)
        markers = (str(L),'supervise_pa19','m2_native_staged','run_m2','m2h_')
        other = {pid:cmd[:200] for pid,(_,cmd) in rows.items() if pid not in mine and pid not in monitors and any(k in cmd for k in markers)}
        assert not other, ('lane process present',other)
        return {'monitors_alive':sorted(monitors),'other_lane_processes':0}

    def clocks():
        pc = pre['policy_clocks']; cut,end = epoch(pc['admission_cutoff']),epoch(pc['native_end'])
        head = min(cut-now,end-pc['cleanup_allowance_seconds']-now)
        assert head >= pre['min_launch_headroom_seconds'], ('headroom',head)
        return {'cutoff_remaining_seconds':round(cut-now),'native_end_remaining_seconds':round(end-now),'headroom_seconds':round(head)}

    def disk():
        s = os.statvfs(L); free = s.f_bavail*s.f_frsize
        need = pre['disk_gate']['base_gate_bytes']+pre['disk_gate']['projected_growth_bytes']
        assert free >= need, (free,need)
        return {'free_bytes':free,'required_bytes':need}

    def preview():
        g = json.loads(Path(gp_path).read_bytes())
        t = datetime.datetime.strptime(g['host_clock'],'%Y-%m-%dT%H:%M:%S%z').timestamp()
        assert g['schema'] and g['contract_sha256'] == pre['contract']['sha256'], 'preview not bound to the contract'
        assert g['usage_within_reservation'] is True and g['budget_2400_fits'] is True
        assert g['gates'] and all(v['admitted'] is True and not v['errors'] for v in g['gates'].values()), g['gates']
        assert not g['admission_union']['resource_stops'] and not g['admission_union']['persistent_vetoes']
        assert t >= epoch(pre['host_clock_iso']) and 0 <= now-t <= 600, ('preview age/order',now-t)
        return {'path':str(Path(gp_path).resolve().relative_to(L)),'sha256':digest(gp_path),'age_seconds':round(now-t,1)}

    def tokens():
        held = {t:subprocess.run(['/usr/sbin/lsof','-t',str(L/'cycle2/tokens'/t)],capture_output=True,text=True).stdout.split() for t in ('t0','t1')}
        assert not any(held.values()), held
        return {'held':held}

    def long_job():
        rule = pre['long_job_rule']
        assert digest(rule['amendment']['path']) == rule['amendment']['sha256']
        return monitor_rule(rule['monitor'],rule['rule'],now)

    for name,fn in [('hashes',hashes),('namespace',namespace),('registry',registry),('processes',processes),('clocks',clocks),
                    ('disk',disk),('preview',preview),('tokens',tokens),('long_job',long_job)]:
        run(name,fn)
    ok = all(v['ok'] for v in checks.values())
    out = {'schema':'PA19-M2H-V6_3-PILOT-PRELAUNCH-v1','host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'pre_exec':{'path':str(Path(pre_path).resolve().relative_to(L)),'sha256':pre_sha},'checks':checks,'all_passed':ok,
           'source_sha256':digest(__file__),'native_work_started':False}
    dest = L/'cycle2'/('m2h-v6_3-pilot-prelaunch-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f:
        json.dump(out,f,indent=1); f.write('\n')
    print(dest,digest(dest),'all_passed',ok,json.dumps({k:v['ok'] for k,v in checks.items()}),flush=True)
    for k,v in checks.items():
        if not v['ok']: print('FAIL',k,v['error'][:600],flush=True)
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
