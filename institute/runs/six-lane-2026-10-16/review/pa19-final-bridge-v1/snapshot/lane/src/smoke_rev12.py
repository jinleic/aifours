#!/usr/bin/env python3
"""Focused smoke for stream_check12 (admission re-check inside the bigmem lock) and rss_watchdog3 (pause first,
proven token owner only). Output: cycle2/smoke-rev12-<time>.json (new name per attempt, never overwritten); small
files in cycle2/smoke12/. Production must be paused (COUNT=0, no rev-11/12 runner). The watchdog tests create the
production stop files; they are moved afterwards to archive/stopfiles-smoke12-<time>/ with archive/MANIFEST.tsv
lines, and COUNT is left at 0.
  M1 bigmem wait + stop file: BIG := 1 byte (every check needs the bigmem lock); thread 1 holds the lock 6 s;
     thread 2 solves ms04_s00000 (UNSAT) and waits for the lock; a stop file appears during the wait; after the
     release thread 2 must return UNKNOWN (admission_denied 'stop file ...') with 0 drat-trim spawns.
  M2 the same with the disk floor raised during the wait (DISK_FLOOR := 1e18): admission_denied 'disk floor',
     0 drat-trim spawns.
  W1 RSS-grace admission control: COUNT=1; a holder runner (token + 400 MiB helper) and a waiter runner (polls for
     the token; stop file STOP-hard12); rss_watchdog3 --once (limit 300 MiB) must set COUNT=0 and create the stop
     files BEFORE signalling the holder (action times), signal the holder (proven owner), the holder's helper ends
     (rc -15) before its token release; the waiter starts no child; when COUNT is set back to 1 afterwards the
     waiter acquires and is refused (AdmissionDenied, 0 children).
  W2 no eligible token owner: COUNT=0; a memhog process (400 MiB, no token) and rss_watchdog3 --once: trip, admissions
     paused, nothing signalled (outcome 'no proven token owner'), the memhog never sees SIGTERM and ends by itself.
  V1-V3 SAT verifier ownership (run_hard12.handle_sat, via smoke12_runner.py satverify): V1 normal -> both verifiers
     rc 0 under a token, candidate written; V2 stop file before verification -> deferred, candidate written, 0
     verifier children; V3 SIGTERM during a slow fake verifier (a single process: `exec sleep 30`) -> the verifier
     child is terminated (rc -15) within 10 s, the candidate is preserved, verification deferred. (Attempt 1 used
     `sleep 30` without exec: the shell died at once but its sleep grandchild kept the output pipe open, so the
     stage -- and its token -- waited 27 s for it; production helpers spawn no subprocesses.)
"""
import hashlib
import json
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel  # noqa: E402
import stream_check12 as S  # noqa: E402

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
D = os.path.join(C2, "smoke12")
FD = os.path.join(LANE, "scratch", "fifo", "smoke12")
PY = sys.executable
STOPS = ("STOP-hard12", "STOP-m2r12", "STOP-hard11", "STOP-m2r11")


def count_dt_spawns():
    calls = []
    orig = S.spawn

    def wrapped(cmd, stdin=False):
        if cmd and cmd[0] == S.DT:
            calls.append(time.time())
        return orig(cmd, stdin)

    S.spawn = wrapped
    return calls, orig


def bigmem_case(trigger):
    b = S.cnf_bytes_of(encode_skel.build(json.load(open(os.path.join(LANE, "cases19skel", "specs", "ms04_s00000.json"))))[0])
    old_big, old_floor = S.BIG, S.DISK_FLOOR
    S.BIG = 1
    stopf = os.path.join(D, "STOP-test-%s-%d" % (trigger, time.time_ns()))
    S.set_stop_files([stopf])
    calls, orig = count_dt_spawns()
    out = {}

    def t1():
        with S.BigLock(True):
            out["lock_held_from"] = time.time()
            time.sleep(6)
        out["lock_released"] = time.time()

    def t2():
        time.sleep(0.5)
        out["r"] = S.kissat_staged(b, FD + "_" + trigger, 60, 60)
        out["t2_return"] = time.time()

    a, c = threading.Thread(target=t1), threading.Thread(target=t2)
    a.start()
    c.start()
    time.sleep(3)
    if trigger == "stop":
        with open(stopf, "w") as f:
            f.write("smoke12 stop during bigmem wait\n")
    else:
        S.DISK_FLOOR = 10 ** 18
    out["trigger_at"] = time.time()
    a.join()
    c.join()
    S.spawn = orig
    S.BIG, S.DISK_FLOOR = old_big, old_floor
    S.set_stop_files([])
    r = out["r"]
    res = {"status": r.get("status"), "solver_rc": r.get("solver_rc"), "admission_denied": r.get("admission_denied"),
           "checked": r.get("checked"), "drat_trim": r.get("drat_trim"), "bigmem_lock": r.get("bigmem_lock"),
           "dt_spawns": len(calls), "trigger_at": out["trigger_at"], "lock_released": out["lock_released"],
           "t2_return": out["t2_return"]}
    want = "stop file" if trigger == "stop" else "disk floor"
    res["ok"] = (r.get("solver_rc") == 20 and (r.get("admission_denied") or "").startswith(want) and not r.get("checked")
                 and r.get("drat_trim") is None and len(calls) == 0 and out["t2_return"] >= out["lock_released"] - 0.2)
    return res


def archive_stops(tag):
    moved = []
    dst_dir = os.path.join(LANE, "archive", "stopfiles-smoke12-%s-%s" % (tag, time.strftime("%Y%m%dT%H%M%S")))
    for n in STOPS:
        src = os.path.join(C2, n)
        if os.path.exists(src):
            os.makedirs(dst_dir, exist_ok=True)
            dst = os.path.join(dst_dir, n)
            if os.path.exists(dst):
                raise SystemExit("archive destination exists: " + dst)
            os.rename(src, dst)
            h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
            with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
                f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(src, LANE),
                                                  os.path.relpath(dst, LANE), h, "stop file created by rss_watchdog3 in smoke_rev12 %s" % tag))
            moved.append(os.path.relpath(dst, LANE))
    return moved


def setcount(n):
    with open(os.path.join(S.TOK, "COUNT"), "w") as f:
        f.write("%d\n" % n)


def wd_once(tag):
    return subprocess.run([PY, os.path.join(HERE, "rss_watchdog3.py"), "--limit-kb", str(300 * 1024), "--log",
                           os.path.join(D, "wd3-%s.log" % tag), "--once", "1"], capture_output=True, text=True)


def latest_record():
    recs = sorted(f for f in os.listdir(D) if f.startswith("RSS-WATCHDOG3-"))
    return (recs[-1], json.load(open(os.path.join(D, recs[-1])))) if recs else (None, {})


def main():
    os.makedirs(D, exist_ok=True)
    assert open(os.path.join(S.TOK, "COUNT")).read().split()[0] == "0", "production must be paused (COUNT=0)"
    for n in STOPS:
        assert not os.path.exists(os.path.join(C2, n)), "stop file present before the smoke: " + n
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    outp = os.path.join(C2, "smoke-rev12-%s.json" % time.strftime("%Y%m%dT%H%M%S"))
    try:
        setcount(1)
        out["M1_bigmem_stop"] = bigmem_case("stop")
        out["M2_bigmem_floor"] = bigmem_case("floor")
        # W1
        hl, wl = os.path.join(D, "w1-holder-%d.json" % time.time_ns()), os.path.join(D, "w1-waiter-%d.json" % time.time_ns())
        holder = subprocess.Popen([PY, os.path.join(HERE, "smoke12_runner.py"), "holder", hl])
        time.sleep(3)
        waiter = subprocess.Popen([PY, os.path.join(HERE, "smoke12_runner.py"), "waiter", wl, os.path.join(C2, "STOP-hard12")])
        time.sleep(2)
        wd = wd_once("w1")
        holder.wait()
        name, rec = latest_record()
        time.sleep(5)  # the waiter keeps polling with COUNT=0
        waiter_alive_before = waiter.poll() is None
        setcount(1)  # allow acquisition: the stop file must still refuse the admission
        waiter.wait(timeout=60)
        h, w = json.load(open(hl)), json.load(open(wl))
        acts = rec.get("actions", [])
        t_count0 = [a["time"] for a in acts if "token_count" in a]
        t_stops = [a["time"] for a in acts if "created" in a]
        t_sig = [a["time"] for a in acts if "SIGTERM" in a]
        out["W1_rss_grace"] = {"watchdog_stdout": wd.stdout.strip(), "record": name, "actions": acts, "outcome": rec.get("outcome"),
                               "target": rec.get("target_runner"), "holder": h, "waiter": w,
                               "waiter_alive_while_count0": waiter_alive_before}
        out["W1_rss_grace"]["ok"] = bool(
            rec.get("target_runner") == h.get("pid") and t_count0 and t_stops and t_sig
            and max(t_count0 + t_stops) <= min(t_sig) and h.get("helper_rc") == -15
            and h.get("token_released", 0) >= h.get("helper_returned", 1e18)
            and w.get("spawned_children") == 0 and (w.get("admission_denied") or "").startswith("stop file")
            and waiter_alive_before)
        out["W1_archived_stops"] = archive_stops("W1")
        setcount(0)
        # W2
        ml = os.path.join(D, "w2-memhog-%d.json" % time.time_ns())
        hog = subprocess.Popen([PY, os.path.join(HERE, "smoke12_runner.py"), "memhog", ml, "25"])
        time.sleep(4)
        wd2 = wd_once("w2")
        name2, rec2 = latest_record()
        alive_after = hog.poll() is None
        hog.wait(timeout=120)
        m = json.load(open(ml))
        out["W2_no_owner"] = {"watchdog_stdout": wd2.stdout.strip(), "record": name2, "outcome": rec2.get("outcome"),
                              "target": rec2.get("target_runner"), "actions": rec2.get("actions"), "memhog": m,
                              "memhog_alive_after_watchdog": alive_after}
        out["W2_no_owner"]["ok"] = bool(rec2.get("target_runner") is None and "no proven token owner" in (rec2.get("outcome") or "")
                                        and not m.get("sigterm_seen") and alive_after
                                        and not any("SIGTERM" in a for a in rec2.get("actions", [])))
        out["W2_archived_stops"] = archive_stops("W2")
        setcount(1)
        for variant in ("normal", "stopfile", "sigterm"):
            lg = os.path.join(D, "v-%s-%d.json" % (variant, time.time_ns()))
            cmd = [PY, os.path.join(HERE, "smoke12_runner.py"), "satverify", lg, variant]
            if variant == "stopfile":
                cmd.append(os.path.join(D, "STOP-test-V2-%d" % time.time_ns()))
            subprocess.run(cmd, capture_output=True, text=True)
            v = json.load(open(lg))
            r = v["result"]
            if variant == "normal":
                ok = v["solve_status"] == "SAT" and r["verify1_rc"] == 0 and r["verify2_rc"] == 0 and r["verify_token"] and v["witness_exists"] \
                    and v["spawned_for_verify"] == 2
            elif variant == "stopfile":
                ok = v["solve_status"] == "SAT" and (r["verification_deferred"] or "").startswith("admission refused") and v["witness_exists"] \
                    and v["spawned_for_verify"] == 0
            else:
                ok = v["solve_status"] == "SAT" and r["verify1_rc"] == -15 and r["verification_deferred"] and v["witness_exists"] \
                    and v["spawned_for_verify"] == 1 and v["verify_end"] - v["sigterm_sent"] < 10
            out["V_%s" % variant] = dict(v, ok=bool(ok))
        setcount(0)
        out["verdicts"] = {k: out[k]["ok"] for k in ("M1_bigmem_stop", "M2_bigmem_floor", "W1_rss_grace", "W2_no_owner",
                                                      "V_normal", "V_stopfile", "V_sigterm")}
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
