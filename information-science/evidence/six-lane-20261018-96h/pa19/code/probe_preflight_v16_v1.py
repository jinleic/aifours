#!/usr/bin/env python3
"""PA19 96h lane probe 9: read-only runtime preflight of runner v16 before GO request v4.

v16 = v15 with exactly lines 390-391 changed (span comparison and its message, token 290 -> 280),
per parent amendment control/resource-stability-addendum-v3.json (caf809ae...). run-002 (v15) refused
C4 admission with 'window span 280.0s < 290 s' (exit 20, no item started).

Order: (0) exclusive receipt <out>.receipt.json with PID/PGID/PPID/argv/cwd/source SHA BEFORE any work;
(1) v15/v16 pins and a difflib check that only lines 390-391 differ, each only by '290' -> '280';
(2) lstat type (regular, not symlink) and SHA-256 pin of every path v16 hashes, reads or executes;
    directories; run-003 absent;
(3) v16 registry_refusals() and stability_refusals(projected) on the live files (expected []);
(4) v16 ps_table() and identity_checked() on one harmless owned child (/bin/sleep 1, own session,
    reaped by Popen.wait(); no signal is ever sent);
(5) planning statistic only: replay of the v16 window clauses (count >= 25, span >= 280 vs the old 290,
    last age 0..30) over the monitor history at simulated instants; it is not an admission guarantee.
No runner launch, no solver/checker. Standard library only; children: /bin/date, /bin/ps, /bin/sleep.
Admission: fresh statvfs >= 12.2e9 + 16 MiB, no STOP/HALT/sat-candidate marker; self budget 280 s.
Output: one exclusive JSON (argv[1]) under LANE/evidence/probes/ plus its exclusive receipt.
"""
import bisect
import difflib
import hashlib
import importlib.util
import json
import os
import re
import stat
import subprocess
import sys
import time
from datetime import datetime

sys.dont_write_bytecode = True
T0 = time.monotonic()
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
V15 = (LANE + "/code/pilot_file_drat_v15.py", "d924e3731ec7be36571177e4fc6b8a1428397159d725f9d4e32c9a49c9f4ee69")
V16 = (LANE + "/code/pilot_file_drat_v16.py", "0ef4cfdcf7f0220bdde78829198bea7a8acf603e2678e88eedafe0c04bd3170e")
PY_REAL = ("/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/bin/python3.14",
           "cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43")
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def budget(stage):
    if time.monotonic() - T0 > BUDGET:
        raise SystemExit("BUDGET exceeded at " + stage)


def ltype(path):
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent", None
    m = st.st_mode
    t = ("regular" if stat.S_ISREG(m) else "symlink" if stat.S_ISLNK(m) else "directory" if stat.S_ISDIR(m)
         else "fifo" if stat.S_ISFIFO(m) else "other")
    return t, st.st_ino


def check_file(path, pin):
    t, ino = ltype(path)
    rec = {"path": path, "lstat_type": t, "inode": ino, "pin": pin}
    if t == "regular":
        with open(path, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        rec["sha256"] = h
        rec["pin_ok"] = None if pin is None else (h == pin)
    rec["ok"] = (t == "regular" and rec.get("pin_ok") is not False)
    return rec


def diff_check():
    with open(V15[0], "rb") as f:
        a_b = f.read()
    with open(V16[0], "rb") as f:
        b_b = f.read()
    a, b = a_b.decode().splitlines(keepends=True), b_b.decode().splitlines(keepends=True)
    ops = [list(op) for op in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if op[0] != "equal"]
    changed = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y] if len(a) == len(b) else None
    token_only = bool(changed) and all(a[i - 1].count("290") == 1 and b[i - 1] == a[i - 1].replace("290", "280")
                                       for i in changed)
    return {"v15_sha256": hashlib.sha256(a_b).hexdigest(), "v16_sha256": hashlib.sha256(b_b).hexdigest(),
            "line_counts": [len(a), len(b)], "byte_lengths": [len(a_b), len(b_b)], "difflib_nonequal_opcodes": ops,
            "changed_lines": changed, "changed_line_text": {str(i): [a[i - 1], b[i - 1]] for i in (changed or [])},
            "token_only_290_to_280": token_only,
            "ok": changed == [390, 391] and token_only and ops == [["replace", 389, 391, 389, 391]]}


def span_history(monitor):
    """Planning statistic: replay of the v16 window clauses at simulated instants (not a guarantee)."""
    with open(monitor, "rb") as f:
        raw = f.read()
    ts = []
    for ln in raw.split(b"\n")[:-1]:
        o = json.loads(ln)
        if "t" in o:
            ts.append(datetime.fromisoformat(o["t"]).timestamp())
    gaps = {}
    for x, y in zip(ts, ts[1:]):
        g = round(y - x, 3)
        gaps[str(g)] = gaps.get(str(g), 0) + 1
    out = {"samples": len(ts), "first_t": ts[0], "last_t": ts[-1], "gap_histogram_seconds": gaps,
           "assumption": "a row is visible from its 1 s-truncated timestamp t + delay d; real write time is within "
                         "about 1 s after t (observer writes right after /bin/date); simulated now on a 0.25 s grid "
                         "from first_t + 300 to last_t; the window, count, span and age clauses mirror v16 "
                         "stability_refusals; free-space clauses are not replayed",
           "variants": {}}
    for d in (0.0, 1.0):
        n_inst = refuse_count = refuse_280 = refuse_290 = refuse_age = 0
        spans = {}
        now = ts[0] + 300.0
        while now <= ts[-1]:
            hi = bisect.bisect_right(ts, now - d)  # rows visible at now
            lo = bisect.bisect_left(ts, now - 300.0)
            win = ts[lo:hi]
            n_inst += 1
            age = now - ts[hi - 1] if hi else None
            if age is None or not (0 <= age <= 30):
                refuse_age += 1
            if len(win) < 25:
                refuse_count += 1
            else:
                sp = win[-1] - win[0]
                spans[str(round(sp, 3))] = spans.get(str(round(sp, 3)), 0) + 1
                refuse_280 += sp < 280
                refuse_290 += sp < 290
            now += 0.25
        out["variants"]["delay_%gs" % d] = {
            "instants": n_inst, "refused_count_lt_25": refuse_count, "refused_age": refuse_age,
            "refused_span_lt_280_v16": refuse_280, "refused_span_lt_290_v15": refuse_290,
            "fraction_span_lt_280": round(refuse_280 / n_inst, 6), "fraction_span_lt_290": round(refuse_290 / n_inst, 6),
            "span_histogram_seconds": spans}
    return out


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")):
        raise SystemExit("REFUSED: output outside probes or not .json")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "read-only preflight; children /bin/date, /bin/ps, one /bin/sleep 1 reaped by wait()"}
    with open(receipt_path, "xb") as f:
        f.write(json.dumps(receipt, indent=1, sort_keys=True).encode())
    print("RECEIPT", receipt_path, receipt["pid"], flush=True)
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    v16 = check_file(*V16)
    v15 = check_file(*V15)
    if not (v16["ok"] and v15["ok"]):
        raise SystemExit("REFUSED: runner pin mismatch")
    dchk = diff_check()
    budget("diff")
    spec = importlib.util.spec_from_file_location("pilot_v16_readonly", V16[0])
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)  # module top level defines constants only; main() is not called
    files = [("runner_v16", V16[0], V16[1]), ("runner_v15_diff_base", V15[0], V15[1]),
             ("kissat", M.KISSAT[0], M.KISSAT[1]),
             ("drat_trim_old", M.DRAT_OLD[0], M.DRAT_OLD[1]), ("drat_trim_lane_copy", M.DRAT, M.DRAT_OLD[1]),
             ("encoder", M.ENC[0], M.ENC[1]), ("skeleton", M.SKEL[0], M.SKEL[1]),
             ("stop_registry", M.REGISTRY[0], M.REGISTRY[1]), ("launch_contract", M.LAUNCH_CONTRACT[0], M.LAUNCH_CONTRACT[1]),
             ("binary_imports", M.BINARY_IMPORTS[0], M.BINARY_IMPORTS[1]),
             ("kissat_source_evidence", M.KISSAT_SOURCE[0], M.KISSAT_SOURCE[1]), ("monitor", M.MONITOR, None),
             ("python_real", PY_REAL[0], PY_REAL[1]),
             ("bin_date", "/bin/date", None), ("bin_ps", "/bin/ps", None), ("bin_sleep", "/bin/sleep", None)]
    files += [("item_list_" + it["id"], it["list"][0], it["list"][1]) for it in M.ITEMS]
    files += [("inherited_marker_" + n, M.OLD + "/cycle2/" + n, h) for n, h in M.OLD_LIVE_MARKERS.items()]
    checks = [dict(check_file(p, h), role=r) for r, p, h in files]
    budget("file checks")
    drat_inodes_distinct = ltype(M.DRAT)[1] != ltype(M.DRAT_OLD[0])[1]
    dirs = {p: ltype(p)[0] for p in (LANE + "/control", RUN + "/control", M.OLD + "/cycle2", LANE + "/tmp",
                                     LANE + "/evidence/pilot-v1")}
    run003 = LANE + "/evidence/pilot-v1/run-003"
    reg = M.registry_refusals()
    projected_max = M.PROOF_CAP + M.LOG_CAP + 3 * M.RECORD_MAX
    projected_ctrl = M.LOG_CAP + M.CONTROL_PROOF_CAP + 3 * M.RECORD_MAX
    stab_at = clock()
    stab_max = M.stability_refusals(projected_max)
    stab_ctrl = M.stability_refusals(projected_ctrl)
    budget("admission functions")
    rows = M.ps_table()
    child = subprocess.Popen(["/bin/sleep", "1"], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL, start_new_session=True, close_fds=True, cwd=LANE + "/tmp")
    try:
        ident = M.identity_checked(child.pid, os.getpid())
        ident_err = None
    except Exception as exc:
        ident, ident_err = None, repr(exc)
    rows2 = M.ps_table()
    in_table = [r for r in rows2 if r[0] == child.pid]
    rc = child.wait()
    budget("ps")
    hist = span_history(M.MONITOR)
    budget("span history")
    ok = (dchk["ok"] and all(c["ok"] for c in checks if not c["role"].startswith("bin_")) and drat_inodes_distinct
          and all(dirs[p] == "directory" for p in dirs) and not os.path.lexists(run003)
          and reg == [] and stab_max == [] and stab_ctrl == [] and ident_err is None
          and len(in_table) == 1 and in_table[0][2] == child.pid)
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-PREFLIGHT-V16-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "runner_diff_check": dchk, "file_checks": checks, "drat_inodes_distinct": drat_inodes_distinct,
           "dirs": dirs, "run003_absent": not os.path.lexists(run003), "registry_refusals": reg,
           "stability_refusals": {"evaluated_after_host_clock": stab_at,
                                  "projected_item_max": [projected_max, stab_max],
                                  "projected_control": [projected_ctrl, stab_ctrl]},
           "ps_table_rows": len(rows), "identity_checked_on_sleep_child": {"pid": child.pid, "identity": ident,
                                                                           "error": ident_err, "ps_table_row": in_table,
                                                                           "returncode": rc},
           "span_history_planning_statistic": hist,
           "all_ok": ok,
           "all_ok_scope": "diff check, pins/types, dirs, run-003 absent, registry and stability refusals empty at "
                           "the evaluated instant, ps identity; the span-history statistic is informational only",
           "scope": "read-only runtime preflight; no runner launch, no solver/checker; one /bin/sleep 1 child reaped by wait()"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", ok, flush=True)


if __name__ == "__main__":
    main()
