#!/usr/bin/env python3
"""Smoke for stream_check13 / run_hard13 helper safeguards; runs ALONGSIDE production without touching COUNT or the
production stop files: every CPU-using step holds a normal CPU token. Output cycle2/smoke-rev13-<time>.json (new name per
attempt); scratch files in cycle2/smoke13/.
  H1 per-helper RSS cap: HELPER_RSS_CAP_KB := 300 MiB; under a token, run_helper on a helper that touches 600 MiB and
     sleeps 60 s -> SIGTERM to the own child, rc -15 within 10 s, LAST_HELPER.cap_hit, peak >= 300 MiB.
  H2 lane-RSS headroom: LANE_RSS_LIMIT_KB := (current lane RSS + cap - 1) -> AdmissionDenied('lane RSS headroom'), no
     child started.
  H3 helper lock: the smoke holds cycle2/tokens/helper for 6 s; a run_helper call under a token must start its helper only
     after the lock is released.
  H5 stubborn helper above the cap: a helper that ignores SIGTERM, touches 600 MiB and exits 0 after 8 s, with the cap at
     300 MiB -> cap_hit, SIGTERM recorded, run_helper returns only after the helper exited by itself (the caller's token
     held throughout), rc 0 but cap_hit (callers treat this as failure).
  H4 extend failure handling (run_hard13.run_split with its cycle2 directory redirected to cycle2/smoke13/c2 and a fake
     extend command exiting 3): returns extend_failed, writes extend-failed-*.json, leaves no ext.json; with a fake extend
     that writes an empty placement list and exits 0: the temporary file is renamed to ext.json and an extend receipt is
     written (zero batches, so no solver runs).
"""
import json
import os
import sys
import threading
import time
import fcntl

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check13 as S  # noqa: E402

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
D = os.path.join(C2, "smoke13")
PY = sys.executable
BIG = ("b = bytearray(600 * 1024 * 1024)\nfor i in range(0, len(b), 4096):\n    b[i] = 1\nimport time\ntime.sleep(60)\n")


def main():
    os.makedirs(D, exist_ok=True)
    outp = os.path.join(C2, "smoke-rev13-%s.json" % time.strftime("%Y%m%dT%H%M%S"))
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    spawned = []
    orig = S.spawn

    def counting(cmd, stdin=False):
        spawned.append((time.time(), cmd[:2]))
        return orig(cmd, stdin)

    S.spawn = counting
    try:
        old_cap = S.HELPER_RSS_CAP_KB
        S.HELPER_RSS_CAP_KB = 300 * 1024
        with S.Token(stage="smoke13-H1") as tok:
            t0 = time.time()
            rc, _ = S.run_helper([PY, "-c", BIG])
            t1 = time.time()
        h = dict(S.LAST_HELPER)
        out["H1_cap"] = {"rc": rc, "seconds": round(t1 - t0, 1), "helper": h, "token": tok.name,
                         "ok": rc == -15 and h.get("cap_hit") and h.get("peak_rss_kb", 0) >= 300 * 1024 and t1 - t0 < 10}
        S.HELPER_RSS_CAP_KB = 300 * 1024
        stub = ("import signal, time\nsignal.signal(signal.SIGTERM, signal.SIG_IGN)\n"
                "b = bytearray(600 * 1024 * 1024)\nfor i in range(0, len(b), 4096):\n    b[i] = 1\ntime.sleep(8)\n")
        with S.Token(stage="smoke13-H5") as tok5:
            t0 = time.time()
            rc5, _ = S.run_helper([PY, "-c", stub])
            t1 = time.time()
            held_name = tok5.name
        h5 = dict(S.LAST_HELPER)
        S.HELPER_RSS_CAP_KB = old_cap
        out["H5_stubborn"] = {"rc": rc5, "seconds": round(t1 - t0, 1), "helper": h5, "token": held_name,
                              "ok": rc5 == 0 and h5.get("cap_hit") and any("SIGTERM" in str(e) for e in h5.get("events", []))
                              and t1 - t0 >= 8}
        n_before = len(spawned)
        old_lim = S.LANE_RSS_LIMIT_KB
        try:
            with S.Token(stage="smoke13-H2"):
                S.LANE_RSS_LIMIT_KB = S.lane_rss_kb() + S.HELPER_RSS_CAP_KB - 1
                try:
                    S.run_helper([PY, "-c", "pass"])
                    out["H2_headroom"] = {"ok": False, "note": "helper started"}
                except S.AdmissionDenied as e:
                    out["H2_headroom"] = {"denied": str(e), "children_started": len(spawned) - n_before,
                                          "ok": str(e).startswith("lane RSS headroom") and len(spawned) == n_before}
        finally:
            S.LANE_RSS_LIMIT_KB = old_lim
        S.HELPER_RSS_CAP_KB = old_cap
        lfd = os.open(S.HELPER_LOCK, os.O_CREAT | os.O_RDWR)
        fcntl.flock(lfd, fcntl.LOCK_EX)
        t_lock = time.time()
        res3 = {}

        def worker():
            with S.Token(stage="smoke13-H3"):
                res3["token_at"] = time.time()
                S.run_helper([PY, "-c", "pass"])
                res3["helper_done"] = time.time()

        th = threading.Thread(target=worker)
        th.start()
        time.sleep(6)
        t_unlock = time.time()
        fcntl.flock(lfd, fcntl.LOCK_UN)
        os.close(lfd)
        th.join()
        h3_spawn = [t for t, c in spawned if t >= t_lock]
        out["H3_lock"] = {"lock_released": t_unlock, "helper_spawned": h3_spawn, "token_at": res3.get("token_at"),
                          "ok": bool(h3_spawn) and min(h3_spawn) >= t_unlock}
        import run_hard13 as R
        R.C2 = os.path.join(D, "c2-%d" % time.time_ns())
        os.makedirs(os.path.join(R.C2, "part"), exist_ok=True)
        fake_fail = os.path.join(D, "fake_extend_fail.sh")
        with open(fake_fail, "w") as f:
            f.write("#!/bin/sh\nexit 3\n")
        os.chmod(fake_fail, 0o755)
        fake_ok = os.path.join(D, "fake_extend_ok.sh")
        with open(fake_ok, "w") as f:
            f.write("#!/bin/sh\n# args: extend_p1q.py SPEC OUT m\nprintf '{\"source\": \"fake\", \"raw\": 0, \"num_full\": 0, \"full\": []}' > \"$3\"\nexit 0\n")
        os.chmod(fake_ok, 0o755)
        R.VENV_PY = fake_fail
        r_fail = R.run_split("ms06_s00297", 600, 1200, 100)
        dfail = os.path.join(R.C2, "part", "ms06_s00297")
        R.VENV_PY = fake_ok
        r_ok = R.run_split("ms06_s00291", 600, 1200, 100)
        dok = os.path.join(R.C2, "part", "ms06_s00291")
        out["H4_extend"] = {"fail_result": r_fail, "fail_files": sorted(os.listdir(dfail)), "ok_result": r_ok,
                            "ok_files": sorted(os.listdir(dok))}
        out["H4_extend"]["ok"] = bool(r_fail and r_fail.get("extend_failed") and not os.path.exists(os.path.join(dfail, "ext.json"))
                                      and any(f.startswith("extend-failed-") for f in os.listdir(dfail))
                                      and os.path.exists(os.path.join(dok, "ext.json"))
                                      and any(f.startswith("extend-receipt-") for f in os.listdir(dok)))
        out["verdicts"] = {k: bool(out[k]["ok"]) for k in ("H1_cap", "H5_stubborn", "H2_headroom", "H3_lock", "H4_extend")}
        out["all_expected"] = all(out["verdicts"].values())
    finally:
        S.spawn = orig
        out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        with open(outp, "w") as f:
            json.dump(out, f, indent=1, default=str)
    print(outp)
    print(json.dumps({"verdicts": out.get("verdicts"), "all_expected": out.get("all_expected")}, indent=1))


if __name__ == "__main__":
    main()
