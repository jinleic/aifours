#!/usr/bin/env python3
"""run_probe_v1.py (ContinueCFR21, frozen). Runs ONE frozen stdlib probe (<=300 s, <=16 MiB stdout).
usage: run_probe_v1.py <record_dir(new)> <python> <probe.py> [args...]
Writes <record_dir>/launch.json before start, stdout.json (byte-capped), stderr.txt (byte-capped), receipt.json.
Owned SIGTERM to the child's own process group only on overrun; bounded wait; never SIGKILL."""
import os, sys, json, time, hashlib, subprocess, signal
LANE = '/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/cfr21'
CAP = 16 * 1024 * 1024; WALL = 300.0; FLOOR = 12_200_000_000 + 2 * CAP
def bindate():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
rec_dir, py, probe, args = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
os.makedirs(rec_dir, exist_ok=False)
st = os.statvfs(LANE); free = st.f_bavail * st.f_frsize
launch = {"item": os.path.basename(rec_dir), "owner": "ContinueCFR21", "free_bytes_before": free, "floor_required": FLOOR,
          "python": py, "python_realpath": os.path.realpath(py), "python_sha256": sha(os.path.realpath(py)),
          "probe": probe, "probe_sha256": sha(probe), "args": args, "cwd": rec_dir,
          "cap_bytes_stdout": CAP, "cap_bytes_stderr": CAP, "wall_budget_s": WALL, "start": bindate()}
if free < FLOOR:
    launch["admitted"] = False
    with open(os.path.join(rec_dir, 'launch.json'), 'x') as f: json.dump(launch, f, indent=1)
    sys.exit(4)
env = {"PATH": "/usr/bin:/bin", "TMPDIR": LANE + "/tmp", "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
       "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "HOME": LANE + "/tmp", "LC_ALL": "C"}
argv = [py, '-I', '-B', probe] + args
launch["argv"] = argv; launch["argv_sha256"] = hashlib.sha256(json.dumps(argv).encode()).hexdigest(); launch["admitted"] = True
outp = os.path.join(rec_dir, 'stdout.json'); errp = os.path.join(rec_dir, 'stderr.txt')
fo = open(outp, 'xb'); fe = open(errp, 'xb')
t0 = time.monotonic()
child = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=rec_dir, env=env, start_new_session=True)
launch["pid"] = child.pid; launch["pgid"] = os.getpgid(child.pid); launch["absolute_end_budget_monotonic_s"] = WALL
with open(os.path.join(rec_dir, 'launch.json'), 'x') as f: json.dump(launch, f, indent=1)
import selectors
sel = selectors.DefaultSelector(); sel.register(child.stdout, selectors.EVENT_READ, 'o'); sel.register(child.stderr, selectors.EVENT_READ, 'e')
nb = {'o': 0, 'e': 0}; over = False; term_sent = False; open_streams = 2
while open_streams:
    for key, _ in sel.select(timeout=1.0):
        chunk = os.read(key.fileobj.fileno(), 65536)
        if not chunk:
            sel.unregister(key.fileobj); open_streams -= 1; continue
        tgt = fo if key.data == 'o' else fe
        room = CAP - nb[key.data]
        if room > 0: tgt.write(chunk[:room])
        nb[key.data] += len(chunk)
        if nb[key.data] > CAP: over = True
    if (over or time.monotonic() - t0 > WALL) and not term_sent:
        try:
            if os.getpgid(child.pid) == launch["pgid"]: os.killpg(launch["pgid"], signal.SIGTERM)
        except ProcessLookupError: pass
        term_sent = True; t_term = time.monotonic()
    if term_sent and time.monotonic() - t_term > 60: break
try:
    rc = child.wait(timeout=60)
except subprocess.TimeoutExpired:
    rc = None
fo.close(); fe.close()
rcpt = {"end": bindate(), "wall_s": round(time.monotonic() - t0, 3), "returncode": rc, "sigterm_sent": term_sent,
        "over_cap": over, "stdout_bytes_seen": nb['o'], "stderr_bytes_seen": nb['e'],
        "stdout_sha256": sha(outp), "stderr_sha256": sha(errp), "settled": rc is not None,
        "status": ("UNSETTLED" if rc is None else ("COMPLETED" if rc == 0 and not term_sent and not over else "FAILED_OR_STOPPED"))}
with open(os.path.join(rec_dir, 'receipt.json'), 'x') as f: json.dump(rcpt, f, indent=1)
print(json.dumps(rcpt))
