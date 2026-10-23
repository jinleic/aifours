#!/usr/bin/env python3
"""run_checker_controls_v1.py (ContinueCFR21; frozen; stdlib only). Executes the parent GO
NEW RUN/review/cfr-dm-checker-controls-parent-GO-v1.json (e9be557f…): ONE sequential pass = generator then checker on
every generated control, total self budget 280 s (absolute 300 s), one busy child at a time, byte caps 1 MiB per child
stream, owned SIGTERM to the child's own process group only on overrun, bounded wait, never SIGKILL.
Usage: run_checker_controls_v1.py <record_dir(new)> <python> <generator> <gen_sha> <checker> <chk_sha>
                                  <sage_src> <sage_sha> <p21_json> <p21_sha>
Writes <record_dir>/launch.json (before any child), per-child stdout/stderr files, controls/ (by the generator),
receipt.json (after settlement)."""
import os, sys, json, time, hashlib, subprocess, signal, selectors, resource
T0 = time.monotonic(); SELF = 280.0; CAP = 1 << 20
def bindate():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout.strip()
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
rec, py, gen, gen_sha, chk, chk_sha, sage, sage_sha, p21, p21_sha = sys.argv[1:11]
os.makedirs(rec, exist_ok=False)
pins = {}
for label, path, want in (("generator", gen, gen_sha), ("checker", chk, chk_sha), ("sage_source", sage, sage_sha), ("p21_json", p21, p21_sha)):
    if not os.path.isfile(path) or os.path.islink(path): print(json.dumps({"status": "NOT_REGULAR_FILE", "path": path})); sys.exit(3)
    got = sha(path); pins[label] = {"path": path, "sha256": got, "expected": want, "match": got == want}
if not all(v["match"] for v in pins.values()):
    with open(os.path.join(rec, 'launch.json'), 'x') as f: json.dump({"admitted": False, "pins": pins}, f, indent=1)
    print(json.dumps({"status": "PIN_MISMATCH"})); sys.exit(4)
st = os.statvfs(rec); free = st.f_bavail * st.f_frsize
env = {"PATH": "/usr/bin:/bin", "TMPDIR": os.path.dirname(os.path.dirname(os.path.abspath(rec))) + "/../tmp", "PYTHONDONTWRITEBYTECODE": "1",
       "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "LC_ALL": "C", "HOME": "/nonexistent"}
controls = os.path.join(rec, 'controls')
gen_argv = [py, '-I', '-B', gen, controls, sage, sage_sha, p21, p21_sha]
launch = {"item": "cfr-dm-checker-controls (parent GO e9be557f…)", "owner": "ContinueCFR21", "start": bindate(),
          "driver_argv": sys.argv, "driver_sha256": sha(os.path.abspath(__file__)), "python_realpath": os.path.realpath(py),
          "python_sha256": sha(os.path.realpath(py)), "pins": pins, "free_bytes_before": free, "cwd": rec,
          "generator_argv": gen_argv, "checker_argv_template": [py, '-I', '-B', chk, '<case.raw>', '<n>', '<k>'],
          "budget_self_s": SELF, "budget_absolute_s": 300, "stream_cap_bytes": CAP, "children_max": 1}
with open(os.path.join(rec, 'launch.json'), 'x') as f: json.dump(launch, f, indent=1)
records = []
def run_child(tag, argv):
    outp = os.path.join(rec, tag + '.stdout'); errp = os.path.join(rec, tag + '.stderr')
    fo = open(outp, 'xb'); fe = open(errp, 'xb')
    t1 = time.monotonic(); start = bindate()
    ch = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=rec, env=env, start_new_session=True)
    pgid = os.getpgid(ch.pid)
    sel = selectors.DefaultSelector(); sel.register(ch.stdout, selectors.EVENT_READ, 'o'); sel.register(ch.stderr, selectors.EVENT_READ, 'e')
    nb = {'o': 0, 'e': 0}; open_n = 2; term = False; over = False; t_term = None
    while open_n:
        for key, _ in sel.select(timeout=0.5):
            data = os.read(key.fileobj.fileno(), 65536)
            if not data: sel.unregister(key.fileobj); open_n -= 1; continue
            tgt = fo if key.data == 'o' else fe; room = CAP - nb[key.data]
            if room > 0: tgt.write(data[:room])
            nb[key.data] += len(data)
            if nb[key.data] > CAP: over = True
        if (over or time.monotonic() - T0 > SELF) and not term:
            try:
                if os.getpgid(ch.pid) == pgid: os.killpg(pgid, signal.SIGTERM)
            except ProcessLookupError: pass
            term = True; t_term = time.monotonic()
        if term and time.monotonic() - t_term > 15: break
    try: rc = ch.wait(timeout=15)
    except subprocess.TimeoutExpired: rc = None
    fo.close(); fe.close()
    r = {"tag": tag, "argv": argv, "argv_sha256": hashlib.sha256(json.dumps(argv).encode()).hexdigest(), "pid": ch.pid, "pgid": pgid,
         "start": start, "end": bindate(), "wall_s": round(time.monotonic() - t1, 3), "returncode": rc, "sigterm_sent": term,
         "over_cap": over, "stdout_bytes": nb['o'], "stderr_bytes": nb['e'], "stdout_sha256": sha(outp), "stderr_sha256": sha(errp),
         "settled": rc is not None, "children_maxrss_bytes_so_far": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}
    records.append(r); return r, outp, errp
g, gout, gerr = run_child('generator', gen_argv)
evals = []; ok_all = g["returncode"] == 0 and g["stderr_bytes"] == 0
manifest = None
if ok_all:
    mpath = os.path.join(controls, 'manifest.json'); manifest = json.load(open(mpath))
INTENDED = {
 "neg_sage_dm21_k6_swap": ("row", 2), "neg_sage_dm33_k6_swap": ("row", 2), "neg_sage_dm39_k6_swap": ("row", 2),
 "neg_sage_dm51_k6_swap": ("row", 2), "neg_p21_sol1_swap": ("row", 4), "neg_p21_sol1_duprow": ("exact", [[4, 5]]),
 "neg_z9_rows_0_1_2_4": ("exact", [[1, 3]]), "neg_z21_rows_0_1_2_5": ("exact", [[2, 3]]), "neg_linear_z13_k7_swap": ("row", 6)}
if manifest:
    for case in manifest["cases"]:
        if time.monotonic() - T0 > SELF: evals.append({"case": case["name"], "status": "NOT_RUN_BUDGET"}); ok_all = False; continue
        if sha(case["file"]) != case["sha256"]: evals.append({"case": case["name"], "status": "INPUT_HASH_CHANGED"}); ok_all = False; continue
        r, outp, errp = run_child('check_' + case["name"], [py, '-I', '-B', chk, case["file"], str(case["n"]), str(case["k"])])
        ev = {"case": case["name"], "n": case["n"], "k": case["k"], "input_sha256": case["sha256"], "returncode": r["returncode"]}
        try:
            out = json.loads(open(outp).read())
        except Exception as e:
            out = None; ev["parse_error"] = repr(e)
        clean = r["stderr_bytes"] == 0 and out is not None and r["settled"] and not r["sigterm_sent"]
        if case["expected_overall"].startswith("PASS"):
            good = clean and r["returncode"] == 0 and out["overall"] == "PASS" and out["dm_verdict"] == "PASS" and \
                   out["mols_verdict"] == "PASS" and out["cfr_verdict"] == "PASS" and out["mols_count"] == case["k"] - 1
            ev["verdict"] = ("PASS_SAGE_TRANSCRIPTION_VERIFIED" if case["name"].startswith("pos_sage") else "PASS_AS_EXPECTED") if good else "UNEXPECTED"
        else:
            kind, spec = INTENDED[case["name"]]
            bad = out.get("dm_bad_pairs") if out else None
            if kind == "row": intended = bool(bad) and all(spec in p for p in bad) and out["dm_bad_pair_count"] == len(bad)
            else: intended = bad == spec
            good = clean and r["returncode"] == 1 and out["overall"] == "FAIL" and out["dm_verdict"] == "FAIL" and intended and \
                   out["mols_verdict"] == "FAIL" and out["cfr_verdict"] == "FAIL"
            ev["dm_bad_pairs"] = bad; ev["intended_spec"] = [kind, spec]
            ev["verdict"] = "FAIL_AS_INTENDED" if good else "UNEXPECTED"
        if out: ev.update({k2: out.get(k2) for k2 in ("dm_verdict", "mols_verdict", "cfr_verdict", "overall", "mols_count", "cfr_rows", "cfr_collisions")})
        if ev["verdict"] == "UNEXPECTED": ok_all = False
        evals.append(ev)
st2 = os.statvfs(rec)
receipt = {"end": bindate(), "wall_s": round(time.monotonic() - T0, 3), "all_settled": all(r["settled"] for r in records),
           "children": len(records), "max_child_rss_bytes": resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
           "free_bytes_after": st2.f_bavail * st2.f_frsize, "generator": g, "evaluations": evals,
           "acceptance": "ALL_EXPECTED" if ok_all and evals and all(e.get("verdict") in ("PASS_AS_EXPECTED", "PASS_SAGE_TRANSCRIPTION_VERIFIED", "FAIL_AS_INTENDED") for e in evals) else "NOT_MET",
           "records": records,
           "scope_note": "one checker implementation with three predicates; calibration only; no seven-row composite-order witness implied"}
with open(os.path.join(rec, 'receipt.json'), 'x') as f: json.dump(receipt, f, indent=1)
print(json.dumps({"acceptance": receipt["acceptance"], "wall_s": receipt["wall_s"], "cases": len(evals),
                  "verdicts": {e["case"]: e.get("verdict") for e in evals}}))
