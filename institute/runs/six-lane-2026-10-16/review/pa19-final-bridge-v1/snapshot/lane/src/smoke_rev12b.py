#!/usr/bin/env python3
"""Smoke for rss_watchdog4 (REV11b, signal-free). Output cycle2/smoke-rev12b-<time>.json (new name per attempt).
Preconditions: COUNT=0, no STOP-hard12/STOP-m2r12, no lane runner alive.
  S0 static (AST, so docstring words do not count): rss_watchdog4.py imports no signal module and has no .kill/.killpg/
     .terminate/.send_signal attribute and no 'kill'/'pkill'/'killall' command string. (Attempt 1 used a substring check
     that matched the docstring sentence stating the absence of such code.)
  S1 a memhog fixture (smoke12_runner.py memhog: 400 MiB, no token, records any SIGTERM it receives, sleeps 25 s) and
     COUNT=1; rss_watchdog4 (limit 300 MiB) must trip: COUNT=0, both stop files created, alert JSON with the memhog's
     group RSS, signals_sent 0, watchdog exits; the memhog receives no SIGTERM and ends by itself.
  S2 no new admissions afterwards: COUNT is set back to 1 by the smoke; a waiter runner (stop file STOP-hard12) acquires
     a token and is refused (AdmissionDenied) with 0 child processes.
Afterwards the stop files are moved to archive/stopfiles-smoke12b-<time>/ (archive/MANIFEST.tsv) and COUNT is set to 0.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
TOK = os.path.join(C2, "tokens")
D = os.path.join(C2, "smoke12b")
PY = sys.executable
STOPS = ("STOP-hard12", "STOP-m2r12")


def setcount(n):
    with open(os.path.join(TOK, "COUNT"), "w") as f:
        f.write("%d\n" % n)


def main():
    os.makedirs(D, exist_ok=True)
    assert open(os.path.join(TOK, "COUNT")).read().split()[0] == "0", "production must be paused"
    for n in STOPS:
        assert not os.path.exists(os.path.join(C2, n)), n
    outp = os.path.join(C2, "smoke-rev12b-%s.json" % time.strftime("%Y%m%dT%H%M%S"))
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    try:
        src = open(os.path.join(HERE, "rss_watchdog4.py")).read()
        import ast
        bad = []
        for node in ast.walk(ast.parse(src)):
            if isinstance(node, ast.Import) and any(a.name.split(".")[0] == "signal" for a in node.names):
                bad.append("import signal")
            if isinstance(node, ast.ImportFrom) and (node.module or "").split(".")[0] == "signal":
                bad.append("from signal import")
            if isinstance(node, ast.Attribute) and node.attr in ("kill", "killpg", "terminate", "send_signal", "pidfd_send_signal"):
                bad.append("attribute ." + node.attr)
            if isinstance(node, ast.Name) and node.id in ("kill", "killpg", "signal"):
                bad.append("name " + node.id)
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value in ("kill", "pkill", "killall"):
                bad.append("string %r" % node.value)
        out["S0_static"] = {"method": "AST walk: no signal import, no .kill/.killpg/.terminate/.send_signal attribute, no kill/pkill/killall command string",
                            "forbidden_found": bad, "sha256": hashlib.sha256(src.encode()).hexdigest(), "ok": not bad}
        setcount(1)
        ml = os.path.join(D, "memhog-%d.json" % time.time_ns())
        hog = subprocess.Popen([PY, os.path.join(HERE, "smoke12_runner.py"), "memhog", ml, "25"])
        time.sleep(4)
        wd = subprocess.run([PY, os.path.join(HERE, "rss_watchdog4.py"), "--limit-kb", str(300 * 1024), "--log",
                             os.path.join(D, "wd4.log"), "1"], capture_output=True, text=True)
        t_after = time.time()
        count_after = open(os.path.join(TOK, "COUNT")).read().split()[0]
        stops_after = [n for n in STOPS if os.path.exists(os.path.join(C2, n))]
        hog_alive = hog.poll() is None
        hog.wait(timeout=120)
        m = json.load(open(ml))
        wdo = json.loads(wd.stdout.strip().splitlines()[-1]) if wd.stdout.strip() else {}
        alert = json.load(open(wdo["alert"])) if wdo.get("alert") else {}
        grp = [g for g in alert.get("groups", []) if g.get("runner") == m.get("pid")]
        out["S1_trip"] = {"watchdog_rc": wd.returncode, "watchdog_stdout": wd.stdout.strip(), "alert": wdo.get("alert"),
                          "alert_signals_sent": alert.get("signals_sent"), "alert_token_count": alert.get("token_count"),
                          "alert_stop_files_created": alert.get("stop_files_created"),
                          "memhog_group_rss_kb": grp[0]["rss_kb"] if grp else None, "count_after": count_after,
                          "stops_after": stops_after, "memhog_alive_after_watchdog": hog_alive, "memhog": m,
                          "watchdog_exited_at": t_after}
        out["S1_trip"]["ok"] = bool(wd.returncode == 0 and alert.get("signals_sent") == 0 and count_after == "0"
                                    and sorted(stops_after) == sorted(STOPS) and grp and grp[0]["rss_kb"] >= 350 * 1024
                                    and hog_alive and not m.get("sigterm_seen"))
        setcount(1)
        wl = os.path.join(D, "waiter-%d.json" % time.time_ns())
        subprocess.run([PY, os.path.join(HERE, "smoke12_runner.py"), "waiter", wl, os.path.join(C2, "STOP-hard12")],
                       capture_output=True, text=True)
        w = json.load(open(wl))
        out["S2_no_admission"] = {"waiter": w, "ok": bool((w.get("admission_denied") or "").startswith("stop file")
                                                         and w.get("spawned_children") == 0)}
        setcount(0)
        moved = []
        dst_dir = os.path.join(LANE, "archive", "stopfiles-smoke12b-%s" % time.strftime("%Y%m%dT%H%M%S"))
        for n in STOPS:
            s = os.path.join(C2, n)
            if os.path.exists(s):
                os.makedirs(dst_dir, exist_ok=True)
                d = os.path.join(dst_dir, n)
                if os.path.exists(d):
                    raise SystemExit("archive destination exists: " + d)
                os.rename(s, d)
                h = hashlib.sha256(open(d, "rb").read()).hexdigest()
                with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
                    f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(s, LANE),
                                                      os.path.relpath(d, LANE), h, "stop file created by rss_watchdog4 in smoke_rev12b"))
                moved.append(os.path.relpath(d, LANE))
        out["archived_stop_files"] = moved
        out["verdicts"] = {k: out[k]["ok"] for k in ("S0_static", "S1_trip", "S2_no_admission")}
        out["all_expected"] = all(out["verdicts"].values())
    finally:
        setcount(0)
        out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        with open(outp, "w") as f:
            json.dump(out, f, indent=1, default=str)
    print(outp)
    print(json.dumps({"verdicts": out.get("verdicts"), "all_expected": out.get("all_expected")}, indent=1))


if __name__ == "__main__":
    main()
