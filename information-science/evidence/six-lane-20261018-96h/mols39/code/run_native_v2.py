#!/usr/bin/env python3
"""run_native_v2.py (ContinueCFR21, mols39 lane; frozen; stdlib only). Supervises ONE native solver child.
v2 of run_native_v1.py (7e380eeb…, never executed): after the stream loop the child is polled with the same
absolute-end/SIGTERM/120 s bounded-wait rule instead of an unbounded wait().
Usage: run_native_v1.py <record_dir(new)> <job.json> <job_sha256>
job.json keys: item, go_path, go_sha256, argv (list), inputs [{path, sha256}], budget_s (child self-limit, passed in
argv by the job author), rss_cap_bytes, stdout_cap_bytes, stderr_cap_bytes, projected_disk_bytes, long_job (bool).
Before launch (fail closed): job pin; every input a regular non-symlink file with matching SHA-256; no lane STOP marker
(evidence/STOP-*.json); now <= native launch stop 2026-10-22T20:56:33-07:00; absolute child end = now + budget_s + 120
must be <= min(now + 10800 - 120, owned_compute_settled_by 2026-10-22T21:56:33-07:00 - 180); fresh statvfs free >=
12.2e9 + projected_disk_bytes; if long_job: parent observer v3 stability rule (300 s window, >=25 samples, span >=290 s,
last age <=30 s, strictly increasing tz-aware timestamps, last free >= 13.5e9 + projected, peak-to-later drop <=
max(3e8, (last-13.5e9)//12)).
During run (every 10 s): stdout/stderr byte caps; RSS of the child (/bin/ps; unreadable while alive -> recorded);
free space floor 12e9; lane STOP marker; absolute end. Any trigger -> owned SIGTERM to the child's own process group
(identity: pgid recorded at launch), then bounded 120 s wait; never SIGKILL. Receipt records settlement."""
import os, sys, json, time, hashlib, subprocess, signal, selectors, datetime, glob
LANE = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39'
OBS = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/resource-observer-live-v3.jsonl'
LAUNCH_STOP = datetime.datetime.fromisoformat('2026-10-22T20:56:33-07:00')
SETTLE_BY = datetime.datetime.fromisoformat('2026-10-22T21:56:33-07:00')
def bindate(): return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()
def now(): return datetime.datetime.now(datetime.timezone.utc)
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
def free_bytes(): st = os.statvfs(LANE); return st.f_bavail * st.f_frsize
def stability(projected):
    try:
        lines = open(OBS, 'rb').read().decode().split('\n')
    except Exception as e: return False, "observer unreadable %r" % (e,)
    complete = lines[:-1]; samples = []
    for ln in complete:
        if not ln.strip(): continue
        try:
            d = json.loads(ln); t = datetime.datetime.fromisoformat(d["t"])
            if t.tzinfo is None: return False, "naive timestamp"
            samples.append((t, int(d["free"])))
        except Exception as e: return False, "malformed line %r" % (e,)
    if not samples: return False, "no samples"
    for i in range(1, len(samples)):
        if samples[i][0] <= samples[i - 1][0]: return False, "non-increasing timestamps"
    tl = samples[-1][0]; age = (now() - tl).total_seconds()
    if age < 0 or age > 30: return False, "last sample age %.1f" % age
    win = [s for s in samples if (tl - s[0]).total_seconds() <= 300]
    if len(win) < 25: return False, "only %d samples" % len(win)
    if (tl - win[0][0]).total_seconds() < 290: return False, "span too short"
    last = win[-1][1]
    if last < 13_500_000_000 + projected: return False, "last free %d too low" % last
    maxdrop = 0; peak = -1
    for _, f in win:
        peak = max(peak, f); maxdrop = max(maxdrop, peak - f)
    lim = max(300_000_000, (last - 13_500_000_000) // 12)
    if maxdrop > lim: return False, "drop %d > %d" % (maxdrop, lim)
    return True, {"samples": len(win), "last_free": last, "max_drop": maxdrop, "limit": lim, "age_s": age}
def stop_markers(): return sorted(glob.glob(os.path.join(LANE, 'evidence', 'STOP-*.json')))
def main():
    rec, jpath, jsha = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(rec, exist_ok=False)
    raw = open(jpath, 'rb').read()
    launch = {"start_bin_date": bindate(), "job_path": jpath, "job_sha256": hashlib.sha256(raw).hexdigest(), "runner_sha256": sha(os.path.abspath(__file__))}
    def refuse(reason):
        launch["admitted"] = False; launch["refusal"] = reason
        with open(os.path.join(rec, 'launch.json'), 'x') as f: json.dump(launch, f, indent=1)
        print(json.dumps({"admitted": False, "refusal": reason})); sys.exit(4)
    if launch["job_sha256"] != jsha: refuse("job pin mismatch")
    job = json.loads(raw); launch["job"] = job
    for inp in job["inputs"]:
        p = inp["path"]
        if os.path.islink(p) or not os.path.isfile(p): refuse("input not regular file: " + p)
        if sha(p) != inp["sha256"]: refuse("input pin mismatch: " + p)
    if stop_markers(): refuse("lane STOP marker present: %r" % stop_markers())
    t_now = now()
    if t_now > LAUNCH_STOP: refuse("after native launch stop")
    budget = float(job["budget_s"])
    abs_end = t_now + datetime.timedelta(seconds=budget + 120)
    lim_end = min(t_now + datetime.timedelta(seconds=10800 - 120), SETTLE_BY - datetime.timedelta(seconds=180))
    if abs_end > lim_end: refuse("chunk does not fit: abs_end %s > %s" % (abs_end.isoformat(), lim_end.isoformat()))
    fb = free_bytes(); launch["free_bytes_before"] = fb
    if fb < 12_200_000_000 + int(job["projected_disk_bytes"]): refuse("free space %d below gate" % fb)
    if job.get("long_job") or budget >= 3600:
        ok, info = stability(int(job["projected_disk_bytes"]))
        launch["stability"] = info
        if not ok: refuse("stability rule: %s" % info)
    env = {"PATH": "/usr/bin:/bin", "TMPDIR": os.path.join(LANE, "tmp"), "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
           "OPENBLAS_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "LC_ALL": "C", "HOME": os.path.join(LANE, "tmp")}
    outp = os.path.join(rec, 'stdout.txt'); errp = os.path.join(rec, 'stderr.txt')
    fo = open(outp, 'xb'); fe = open(errp, 'xb')
    argv = job["argv"]
    ch = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=rec, env=env, start_new_session=True)
    pgid = os.getpgid(ch.pid); t0 = time.monotonic()
    launch.update({"admitted": True, "pid": ch.pid, "pgid": pgid, "argv": argv, "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(),
                   "cwd": rec, "absolute_end_utc": abs_end.isoformat(), "launch_utc": t_now.isoformat(), "env": env})
    with open(os.path.join(rec, 'launch.json'), 'x') as f: json.dump(launch, f, indent=1)
    sel = selectors.DefaultSelector(); sel.register(ch.stdout, selectors.EVENT_READ, 'o'); sel.register(ch.stderr, selectors.EVENT_READ, 'e')
    caps = {'o': int(job["stdout_cap_bytes"]), 'e': int(job["stderr_cap_bytes"])}; nb = {'o': 0, 'e': 0}
    open_n = 2; term = None; t_term = None; last_sample = 0; maxrss = 0; samples = []; rss_unread = 0
    hout = hashlib.sha256()
    def send_term(reason):
        nonlocal term, t_term
        if term is None:
            try:
                if os.getpgid(ch.pid) == pgid: os.killpg(pgid, signal.SIGTERM)
            except ProcessLookupError: pass
            term = reason; t_term = time.monotonic()
    while open_n:
        for key, _ in sel.select(timeout=1.0):
            data = os.read(key.fileobj.fileno(), 65536)
            if not data: sel.unregister(key.fileobj); open_n -= 1; continue
            tgt = fo if key.data == 'o' else fe; room = caps[key.data] - nb[key.data]
            if room > 0:
                tgt.write(data[:room])
                if key.data == 'o': hout.update(data[:room])
            nb[key.data] += len(data)
            if nb[key.data] > caps[key.data]: send_term("output cap " + key.data)
        el = time.monotonic() - t0
        if el - last_sample >= 10:
            last_sample = el
            r = subprocess.run(['/bin/ps', '-o', 'rss=', '-p', str(ch.pid)], capture_output=True, text=True, stdin=subprocess.DEVNULL)
            try: rss = int(r.stdout.strip()) * 1024
            except ValueError: rss = None
            if rss is None and ch.poll() is None: rss_unread += 1
            if rss: maxrss = max(maxrss, rss)
            fb = free_bytes()
            if len(samples) < 2000: samples.append([round(el, 1), rss, fb])
            if rss and rss > int(job["rss_cap_bytes"]): send_term("rss cap")
            if fb < 12_000_000_000: send_term("free space floor")
            if stop_markers(): send_term("lane STOP marker")
        if now() >= abs_end: send_term("absolute end")
        if term is not None and time.monotonic() - t_term > 120: break
    while ch.poll() is None:
        if now() >= abs_end: send_term("absolute end")
        if stop_markers(): send_term("lane STOP marker")
        if term is not None and time.monotonic() - t_term > 120: break
        time.sleep(1)
    rc = ch.poll()
    fo.close(); fe.close()
    res = "UNKNOWN"
    try:
        for ln in open(outp, 'rb').read().decode(errors='replace').splitlines():
            if ln.startswith('s '): res = ln[2:].strip()
    except Exception: pass
    rcpt = {"end_bin_date": bindate(), "wall_s": round(time.monotonic() - t0, 3), "returncode": rc, "settled": rc is not None,
            "sigterm_reason": term, "stdout_bytes_seen": nb['o'], "stderr_bytes_seen": nb['e'],
            "stdout_sha256": sha(outp), "stderr_sha256": sha(errp), "max_rss_bytes": maxrss, "rss_unreadable_samples": rss_unread,
            "samples": samples, "solver_result": res, "free_bytes_after": free_bytes(),
            "status": ("UNSETTLED" if rc is None else ("COMPLETED" if term is None else "STOPPED:" + term))}
    with open(os.path.join(rec, 'receipt.json'), 'x') as f: json.dump(rcpt, f, indent=1)
    print(json.dumps({k: rcpt[k] for k in ("status", "solver_result", "wall_s", "returncode", "max_rss_bytes")}))
if __name__ == '__main__':
    main()
