#!/usr/bin/env python3
"""PA19 96h lane probe 8: read-only runtime preflight of runner v15 before GO request v3.

Motivation: run-001 (runner v14) exited 60 before any child because KISSAT pointed at a Homebrew
symlink and sha_file() refuses non-regular files; static reviews never exercised runtime path types.
This probe (no runner launch, no solver/checker) checks, against the v15 module imported read-only:
  1. lstat type (regular, not symlink) and SHA-256 pin of every path the runner hashes, reads or
     executes; directory checks for the listed directories; run-002 output path absent.
  2. registry_refusals() and stability_refusals(projected) on the live files (expected: []).
  3. ps parsing used by the runner: ps_table() and identity_checked() on one harmless owned child
     (/bin/sleep 1, own session, reaped by Popen.wait(); no signal is ever sent).
Standard library only; children: /bin/date, /bin/ps (via the runner functions) and /bin/sleep.
Admission: fresh statvfs >= 12.2e9 + 16 MiB, no new-round marker; self budget 280 s.
Output: one exclusive JSON (argv[1]) under LANE/evidence/probes/.
"""
import hashlib
import importlib.util
import json
import os
import re
import stat
import subprocess
import sys
import time

sys.dont_write_bytecode = True
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
V15 = (LANE + "/code/pilot_file_drat_v15.py", "d924e3731ec7be36571177e4fc6b8a1428397159d725f9d4e32c9a49c9f4ee69")
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
T0 = time.monotonic()


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


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
        h = hashlib.sha256(open(path, "rb").read()).hexdigest()
        rec["sha256"] = h
        rec["pin_ok"] = None if pin is None else (h == pin)
    rec["ok"] = (t == "regular" and rec.get("pin_ok") is not False)
    return rec


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(LANE + "/evidence/probes/"):
        raise SystemExit("REFUSED: output outside probes")
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    v15 = check_file(*V15)
    if not v15["ok"]:
        raise SystemExit("REFUSED: v15 pin mismatch")
    spec = importlib.util.spec_from_file_location("pilot_v15_readonly", V15[0])
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)  # module top level defines constants only; main() is not called
    files = [("runner_v15", V15[0], V15[1]), ("kissat", M.KISSAT[0], M.KISSAT[1]),
             ("drat_trim_old", M.DRAT_OLD[0], M.DRAT_OLD[1]), ("drat_trim_lane_copy", M.DRAT, M.DRAT_OLD[1]),
             ("encoder", M.ENC[0], M.ENC[1]), ("skeleton", M.SKEL[0], M.SKEL[1]),
             ("stop_registry", M.REGISTRY[0], M.REGISTRY[1]), ("launch_contract", M.LAUNCH_CONTRACT[0], M.LAUNCH_CONTRACT[1]),
             ("binary_imports", M.BINARY_IMPORTS[0], M.BINARY_IMPORTS[1]),
             ("kissat_source_evidence", M.KISSAT_SOURCE[0], M.KISSAT_SOURCE[1]), ("monitor", M.MONITOR, None),
             ("bin_date", "/bin/date", None), ("bin_ps", "/bin/ps", None), ("bin_sleep", "/bin/sleep", None)]
    files += [("item_list_" + it["id"], it["list"][0], it["list"][1]) for it in M.ITEMS]
    files += [("inherited_marker_" + n, M.OLD + "/cycle2/" + n, h) for n, h in M.OLD_LIVE_MARKERS.items()]
    checks = [dict(check_file(p, h), role=r) for r, p, h in files]
    drat_inodes_distinct = ltype(M.DRAT)[1] != ltype(M.DRAT_OLD[0])[1]
    py = {"invoked_symlink": "/opt/homebrew/bin/python3", "invoked_lstat": ltype("/opt/homebrew/bin/python3")[0],
          "realpath": os.path.realpath("/opt/homebrew/bin/python3"), "this_probe_sys_executable": sys.executable}
    py["realpath_check"] = check_file(py["realpath"], "cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43")
    dirs = {p: ltype(p)[0] for p in (LANE + "/control", RUN + "/control", M.OLD + "/cycle2", LANE + "/tmp",
                                     LANE + "/evidence/pilot-v1")}
    run002 = LANE + "/evidence/pilot-v1/run-002"
    reg = M.registry_refusals()
    projected_max = M.PROOF_CAP + M.LOG_CAP + 3 * M.RECORD_MAX
    projected_ctrl = M.LOG_CAP + M.CONTROL_PROOF_CAP + 3 * M.RECORD_MAX
    stab_max = M.stability_refusals(projected_max)
    stab_ctrl = M.stability_refusals(projected_ctrl)
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
    ok = (all(c["ok"] for c in checks if not c["role"].startswith("bin_")) and drat_inodes_distinct
          and all(dirs[p] == "directory" for p in dirs) and not os.path.lexists(run002)
          and reg == [] and stab_max == [] and stab_ctrl == [] and ident_err is None
          and len(in_table) == 1 and in_table[0][2] == child.pid)
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-PREFLIGHT-V15-v1", "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3),
           "probe_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "file_checks": checks, "drat_inodes_distinct": drat_inodes_distinct, "python": py, "dirs": dirs,
           "run002_absent": not os.path.lexists(run002), "registry_refusals": reg,
           "stability_refusals": {"projected_item_max": [projected_max, stab_max], "projected_control": [projected_ctrl, stab_ctrl]},
           "ps_table_rows": len(rows), "identity_checked_on_sleep_child": {"pid": child.pid, "identity": ident,
                                                                           "error": ident_err, "ps_table_row": in_table,
                                                                           "returncode": rc},
           "all_ok": ok,
           "scope": "read-only runtime preflight; no runner launch, no solver/checker; one /bin/sleep 1 child reaped by wait()"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", ok)


if __name__ == "__main__":
    main()
