#!/usr/bin/env python3
"""Test runner for smoke_rev12 (stream_check12 + rss_watchdog3). Modes:
  holder LOG          : SIGTERM handler; acquire a token; run a 400 MiB helper via run_helper; log times/rc.
  waiter LOG STOPFILE : SIGTERM handler; stop files = [STOPFILE]; wait for a token, then (if admitted) run a short
                        helper; logs every child start (spawned_children) and any AdmissionDenied.
  memhog LOG SECONDS  : touch 400 MiB in this process WITHOUT any token, sleep SECONDS, exit; logs whether it saw a
                        SIGTERM (handler records it).
  satverify LOG VARIANT [STOPFILE] : solve the SAT (13,5,4) skeleton ms04_s00000 (kissat_staged) and pass the result to
                        run_hard12.handle_sat with its witness directory redirected to cycle2/smoke12/witness.
                        VARIANT normal: both verifiers run under a token; stopfile: STOPFILE exists before handle_sat
                        (verification deferred, candidate preserved, no verifier started); sigterm: a slow fake verifier
                        is used and this process sends itself SIGTERM 3 s after it started (verifier child terminated,
                        candidate preserved, verification deferred).
"""
import json
import os
import signal
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check12 as S  # noqa: E402

HELPER = ("b = bytearray(400 * 1024 * 1024)\n"
          "for i in range(0, len(b), 4096):\n"
          "    b[i] = 1\n"
          "import time\n"
          "time.sleep(90)\n")


def main():
    mode, logp = sys.argv[1], sys.argv[2]
    log = {"pid": os.getpid(), "mode": mode, "start": time.time(), "spawned_children": 0}
    if mode == "memhog":
        got = []
        signal.signal(signal.SIGTERM, lambda *a: got.append(time.time()))
        b = bytearray(400 * 1024 * 1024)
        for i in range(0, len(b), 4096):
            b[i] = 1
        log["allocated"] = time.time()
        t_end = time.time() + float(sys.argv[3])
        while time.time() < t_end:
            time.sleep(0.5)
        log["sigterm_seen"] = got
        log["end"] = time.time()
        with open(logp, "w") as f:
            json.dump(log, f, indent=1)
        return
    S.install_sigterm_handler()
    orig_spawn = S.spawn

    def counting_spawn(cmd, stdin=False):
        log["spawned_children"] += 1
        log.setdefault("spawn_times", []).append(time.time())
        return orig_spawn(cmd, stdin)

    S.spawn = counting_spawn
    if mode == "satverify":
        import encode_skel
        import run_hard12 as R
        variant = sys.argv[3]
        R.C2 = os.path.join(os.path.dirname(HERE), "cycle2", "smoke12")
        spec = json.load(open(os.path.join(os.path.dirname(HERE), "controls", "c13skel", "specs", "ms04_s00000.json")))
        F, X, _ = encode_skel.build(spec)
        res = S.kissat_staged(S.cnf_bytes_of(F), os.path.join(os.path.dirname(HERE), "scratch", "fifo", "smoke12sv"), 60)
        log["solve_status"] = res["status"]
        log["spawned_before_verify"] = log["spawned_children"]
        if variant == "stopfile":
            S.set_stop_files([sys.argv[4]])
            with open(sys.argv[4], "w") as f:
                f.write("smoke12 satverify stop\n")
        if variant == "sigterm":
            slow = os.path.join(R.C2, "slow_verifier.sh")
            with open(slow, "w") as f:
                f.write("#!/bin/sh\nexec sleep 30\n")  # single process, like every production helper
            os.chmod(slow, 0o755)
            R.VERIFIERS = [[slow], [slow]]
            import threading

            def later():
                time.sleep(3)
                log["sigterm_sent"] = time.time()
                os.kill(os.getpid(), signal.SIGTERM)

            threading.Thread(target=later, daemon=True).start()
        name = "satverify-%s-%d" % (variant, time.time_ns())
        try:
            R.handle_sat(name, res, X, spec)
        except SystemExit as e:
            log["system_exit_in_handle_sat"] = repr(e)
        log["verify_end"] = time.time()
        log["result"] = {k: res.get(k) for k in ("model_file", "solver_output_file", "verify_token", "verify1_rc", "verify2_rc",
                                                 "verification_deferred")}
        log["witness_exists"] = os.path.exists(os.path.join(os.path.dirname(HERE), res.get("model_file", "-"))) if res.get("model_file") else False
        log["spawned_for_verify"] = log["spawned_children"] - log["spawned_before_verify"]
        log["abort_flag"] = S.ABORT[0]
        with open(logp, "w") as f:
            json.dump(log, f, indent=1)
        return
    try:
        if mode == "holder":
            with S.Token(stage="smoke12-holder") as tok:
                log["token"], log["token_acquired"] = tok.name, time.time()
                rc, out = S.run_helper([sys.executable, "-c", HELPER])
                log["helper_rc"], log["helper_returned"] = rc, time.time()
            log["token_released"] = time.time()
        elif mode == "waiter":
            S.set_stop_files([sys.argv[3]])
            log["waiting_since"] = time.time()
            with S.Token(stage="smoke12-waiter") as tok:
                log["token"], log["token_acquired"] = tok.name, time.time()
                rc, out = S.run_helper([sys.executable, "-c", "pass"])
                log["helper_rc"] = rc
            log["token_released"] = time.time()
    except S.AdmissionDenied as e:
        log["admission_denied"], log["denied_at"] = str(e), time.time()
    except SystemExit as e:
        log["system_exit"], log["exit_at"] = repr(e), time.time()
    log["abort_flag"] = S.ABORT[0]
    with open(logp, "w") as f:
        json.dump(log, f, indent=1)


if __name__ == "__main__":
    main()
