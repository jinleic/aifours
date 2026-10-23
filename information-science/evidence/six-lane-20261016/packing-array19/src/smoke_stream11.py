#!/usr/bin/env python3
"""Smoke tests for stream_check11 (revision 11) + rss_watchdog2. Writes cycle2/smoke-stream11.json; small test
files in cycle2/smoke11/. Sets cycle2/tokens/COUNT to 1 for the duration (production paused) and restores it.
  A UNSAT (19-row ms04_s00000): kissat_staged and cadical_staged checked, replay_ok, reader_ok;
  B SAT ((13,5,4) ms04_s00000): status SAT, not checked, models verified by BOTH verifiers (13 5 4);
  C native solver limit 3 s (ms09_s00004): UNKNOWN, not checked, no signals;
  D raw proof cap (MAX_RAW 100 kB, ms06_s00028): UNKNOWN, proof_cap_hit 'raw', solver SIGTERM recorded and
    effective (kissat ends within 30 s although it needs ~66 s to solve this CNF);
  E COUNT=1 serialization: two threads, the second waits for the first's token;
  F forged 'solver' writes the binary empty clause and exits 20 on the SAT CNF 'p cnf 1 1 / 1 0': not checked;
  G compressed-tail cap boundary: fake solver writes 64 KiB of random bytes and exits 20; MAX_ZBUF 32 KiB ->
    UNKNOWN with proof_cap_hit 'zbuf-tail' (zbuf before the tail <= cap, tail pushes it over); control with
    MAX_ZBUF 1 MiB -> no cap hit, reader_ok;
  H stubborn solver (ignores SIGTERM, sleeps 12 s; limit 1 s, GRACE 1, TERM_WAIT 2): quarantined, UNKNOWN; a
    second thread (COUNT=1) acquires the token only after the stubborn solver has exited;
  I stubborn checker (fake drat-trim ignoring SIGTERM, reads stdin, sleeps 10 s, then prints 's VERIFIED' and
    exits 0; budget 1 s): quarantined, NOT checked; second thread acquires only after it exited;
  J feed failure: fake drat-trim reads 100 bytes, prints 's VERIFIED', exits 0 -> replay_ok False, NOT checked;
  K admission re-check after acquisition: a stop file appears while thread 2 waits; when thread 1 releases,
    thread 2 acquires and is refused (AdmissionDenied) before starting anything;
  L helper memory + watchdog2 (--once, limit 300 MiB): a test runner holds a token and runs a 400 MiB helper via
    run_helper; the watchdog groups the helper under that runner, SIGTERMs the runner (newest token holder);
    the runner forwards SIGTERM to the helper and releases the token only after the helper has exited.
"""
import json
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel  # noqa: E402
import stream_check11 as S  # noqa: E402

LANE = os.path.dirname(HERE)
D = os.path.join(LANE, "cycle2", "smoke11")
FD = os.path.join(LANE, "scratch", "fifo", "smoke11")
KEYS = ("status", "checked", "solver_stop", "solver_rc", "solve_seconds", "encode_seconds", "check_seconds", "drat_trim",
        "events", "drat_bytes", "zbuf_bytes", "reader_ok", "replay_ok", "replay", "token", "proof_cap_hit",
        "admission_denied", "cnf_sha256")


def keep(r):
    return {k: r.get(k) for k in KEYS}


def skel_cnf(rel):
    F, X, _ = encode_skel.build(json.load(open(os.path.join(LANE, rel))))
    return S.cnf_bytes_of(F), X


def script(name, body):
    p = os.path.join(D, name)
    with open(p, "w") as f:
        f.write("#!/bin/sh\n" + body)
    os.chmod(p, 0o755)
    return p


def two_threads(stage_fn, delay=1.0):
    """thread 1 runs stage_fn; thread 2 starts after delay and acquires a token; returns timings"""
    out = {}

    def t1():
        out["t1_start"] = time.time()
        out["r1"] = stage_fn()
        out["t1_return"] = time.time()

    def t2():
        time.sleep(delay)
        out["t2_wait_start"] = time.time()
        with S.Token(stage="probe") as tok:
            out["t2_acquired"] = time.time()
            out["t2_token"] = tok.name

    a, b = threading.Thread(target=t1), threading.Thread(target=t2)
    a.start()
    b.start()
    a.join()
    b.join()
    return out


def _term(signum, frame):
    raise SystemExit(143)


def main():
    import signal
    signal.signal(signal.SIGTERM, _term)  # a stray SIGTERM ends the smoke through the finally block (COUNT restored)
    os.makedirs(D, exist_ok=True)
    cnt = os.path.join(S.TOK, "COUNT")
    prev = open(cnt).read()
    open(cnt, "w").write("1\n")
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    try:
        b, _ = skel_cnf("cases19skel/specs/ms04_s00000.json")
        out["A_kissat"] = keep(S.kissat_staged(b, FD + "_Ak", 60))
        out["A_cadical"] = keep(S.cadical_staged(lambda: b, FD + "_Ac", 60))
        b13, X13 = skel_cnf("controls/c13skel/specs/ms04_s00000.json")
        for name, fn in (("B_kissat", S.kissat_staged), ("B_cadical", S.cadical_staged)):
            r = fn(b13, FD + "_" + name, 60)
            out[name] = keep(r)
            vals = set()
            for line in r.get("solver_out", "").splitlines():
                if line.startswith("v "):
                    vals.update(int(t) for t in line.split()[1:] if t != "0")
            arr = [[([s for s in range(4) if X13[a][c][s] in vals] + [-1])[0] for c in range(5)] for a in range(13)]
            wp = os.path.join(D, "%s-model.txt" % name)
            with open(wp, "w") as f:
                f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
            v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), wp, "13", "5", "4"], capture_output=True, text=True)
            v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), wp, "13", "5", "4"], capture_output=True, text=True)
            out[name].update({"verify1_rc": v1.returncode, "verify2_rc": v2.returncode})
        b9, _ = skel_cnf("cases19skel/specs/ms09_s00004.json")
        out["C_kissat"] = keep(S.kissat_staged(b9, FD + "_Ck", 3))
        out["C_cadical"] = keep(S.cadical_staged(b9, FD + "_Cc", 3))
        old = S.MAX_RAW
        S.MAX_RAW = 100 * 1024
        out["D_cap_raw"] = keep(S.kissat_staged(skel_cnf("cases19skel/specs/ms06_s00028.json")[0], FD + "_D", 600))
        S.MAX_RAW = old
        bb = open(os.path.join(LANE, "cases19skel", "cnf", "ms01_s00890.cnf"), "rb").read()
        e = two_threads(lambda: S.kissat_staged(bb, FD + "_E", 120), delay=0.5)
        out["E_serial"] = {"r1": keep(e["r1"]), "t1_return": e["t1_return"], "t2_acquired": e["t2_acquired"]}
        e_ok = e["t2_acquired"] >= e["t1_return"] - 0.5 and e["r1"]["checked"]
        forged = script("forged_empty.sh", "printf 'a\\000' > \"$2\"\nexit 20\n")
        out["F_forged"] = keep(S._drat_staged(b"p cnf 1 1\n1 0\n", FD + "_F", 30, 60, lambda c, p, lim: [forged, c, p], "kissat"))
        rnd = os.path.join(D, "random64k.bin")
        with open(rnd, "wb") as f:
            f.write(os.urandom(65536))
        gsol = script("rand_proof.sh", "cat \"%s\" > \"$2\"\nexit 20\n" % rnd)
        oldz = S.MAX_ZBUF
        S.MAX_ZBUF = 32 * 1024
        out["G_tail_cap"] = keep(S._drat_staged(b"p cnf 1 1\n1 0\n", FD + "_G", 30, 60, lambda c, p, lim: [gsol, c, p], "kissat"))
        S.MAX_ZBUF = 1024 * 1024
        out["G_control"] = keep(S._drat_staged(b"p cnf 1 1\n1 0\n", FD + "_G2", 30, 60, lambda c, p, lim: [gsol, c, p], "kissat"))
        S.MAX_ZBUF = oldz
        g_ev = [x for x in (out["G_tail_cap"]["events"] or []) if "proof_cap" in x]
        g_ok = (out["G_tail_cap"]["status"] == "UNKNOWN" and out["G_tail_cap"]["proof_cap_hit"] == "zbuf-tail" and g_ev
                and g_ev[0]["zbuf_before_tail"] <= 32 * 1024 and not out["G_tail_cap"]["checked"]
                and out["G_control"]["proof_cap_hit"] is None and out["G_control"]["reader_ok"])
        S.GRACE, S.TERM_WAIT = 1, 2
        stub = script("stubborn_solver.sh", "trap '' TERM\nexec 3>\"$2\"\nsleep 12\nexit 0\n")
        h = two_threads(lambda: S._drat_staged(b"p cnf 1 1\n1 0\n", FD + "_H", 1, 60, lambda c, p, lim: [stub, c, p], "kissat"))
        out["H_stubborn_solver"] = {"r1": keep(h["r1"]), "t1_start": h["t1_start"], "t1_return": h["t1_return"],
                                    "t2_acquired": h["t2_acquired"]}
        h_ok = (h["r1"]["solver_stop"] == "quarantined" and h["r1"]["status"] == "UNKNOWN" and not h["r1"]["checked"]
                and h["t2_acquired"] >= h["t1_start"] + 12 and h["t2_acquired"] >= h["t1_return"] - 0.5)
        olddt = S.DT
        S.DT = script("stubborn_checker.sh", "trap '' TERM\ncat > /dev/null\nsleep 10\necho 's VERIFIED'\nexit 0\n")
        i = two_threads(lambda: S.kissat_staged(b, FD + "_I", 60, 1))
        out["I_stubborn_checker"] = {"r1": keep(i["r1"]), "t1_return": i["t1_return"], "t2_acquired": i["t2_acquired"]}
        i_ok = ((i["r1"]["drat_trim"] or {}).get("stop") == "quarantined" and not i["r1"]["checked"]
                and i["t2_acquired"] >= i["t1_return"] - 0.5)
        S.DT = script("short_reader_checker.sh", "head -c 100 > /dev/null\necho 's VERIFIED'\nexit 0\n")
        out["J_feed_failure"] = keep(S.kissat_staged(b, FD + "_J", 60, 60))
        S.DT = olddt
        j = out["J_feed_failure"]
        j_ok = (not j["checked"] and j["replay_ok"] is False and (j["drat_trim"] or {}).get("rc") == 0
                and (j["drat_trim"] or {}).get("says_verified"))
        S.GRACE, S.TERM_WAIT = 60, 60
        kstop = os.path.join(D, "STOP-test-K-%d" % time.time_ns())
        S.set_stop_files([kstop])
        kres = {}

        def k1():
            with S.Token(stage="hold"):
                kres["t1_acquired"] = time.time()
                time.sleep(6)
            kres["t1_released"] = time.time()

        def k2():
            time.sleep(1)
            try:
                with S.Token(stage="probe"):
                    kres["t2"] = "ADMITTED"
            except S.AdmissionDenied as ex:
                kres["t2"] = "AdmissionDenied: %s" % ex
                kres["t2_time"] = time.time()
                kres["active_children"] = len(S.ACTIVE)

        ta, tb = threading.Thread(target=k1), threading.Thread(target=k2)
        ta.start()
        tb.start()
        time.sleep(2.5)
        with open(kstop, "w") as f:
            f.write("test stop file for smoke K\n")
        ta.join()
        tb.join()
        S.set_stop_files([])
        out["K_admission_after_acquire"] = kres
        k_ok = kres.get("t2", "").startswith("AdmissionDenied") and kres.get("t2_time", 0) >= kres.get("t1_released", 1e18) - 0.5 \
            and kres.get("active_children") == 0
        lg = os.path.join(D, "helper-runner-log-%d.json" % time.time_ns())
        hr = subprocess.Popen([sys.executable, os.path.join(HERE, "smoke11_helper_runner.py"), lg])
        time.sleep(4)
        wd = subprocess.run([sys.executable, os.path.join(HERE, "rss_watchdog2.py"), "--limit-kb", str(300 * 1024), "--log",
                             os.path.join(D, "wd2-test.log"), "--once", "1"], capture_output=True, text=True)
        hr.wait()
        hl = json.load(open(lg))
        recs = sorted(f for f in os.listdir(D) if f.startswith("RSS-WATCHDOG2-"))
        wrec = json.load(open(os.path.join(D, recs[-1]))) if recs else {}
        grp = [g for g in wrec.get("groups", []) if g.get("runner") == hl.get("pid")]
        out["L_helper_watchdog"] = {"watchdog_stdout": wd.stdout.strip(), "helper_runner_log": hl,
                                    "watchdog_record": recs[-1] if recs else None, "target": wrec.get("target_runner"),
                                    "runner_group_rss_kb": grp[0]["rss_kb"] if grp else None,
                                    "runner_group_members": [m["exe"] for m in grp[0]["members"]] if grp else None}
        l_ok = (wrec.get("target_runner") == hl.get("pid") and hl.get("helper_rc") == -15
                and hl.get("token_released", 0) >= hl.get("helper_returned", 1e18) and grp and grp[0]["rss_kb"] >= 350 * 1024)
        a_ok = all(out[k]["checked"] and out[k]["replay_ok"] and out[k]["reader_ok"] for k in ("A_kissat", "A_cadical"))
        b_ok = all(out[k]["status"] == "SAT" and not out[k]["checked"] and not out[k]["events"] and out[k]["verify1_rc"] == 0
                   and out[k]["verify2_rc"] == 0 for k in ("B_kissat", "B_cadical"))
        c_ok = all(out[k]["status"] == "UNKNOWN" and not out[k]["checked"] and not out[k]["events"] for k in ("C_kissat", "C_cadical"))
        d_ok = (out["D_cap_raw"]["status"] == "UNKNOWN" and out["D_cap_raw"]["proof_cap_hit"] == "raw" and not out["D_cap_raw"]["checked"]
                and out["D_cap_raw"]["solve_seconds"] < 30 and out["D_cap_raw"]["solver_stop"] in ("self", "term"))  # SIGTERM reached kissat
        f_ok = out["F_forged"]["status"] == "UNSAT" and not out["F_forged"]["checked"]
        out["verdicts"] = {"A": a_ok, "B": b_ok, "C": c_ok, "D": d_ok, "E": bool(e_ok), "F": f_ok, "G": bool(g_ok),
                           "H": bool(h_ok), "I": bool(i_ok), "J": bool(j_ok), "K": bool(k_ok), "L": bool(l_ok)}
        out["all_expected"] = all(out["verdicts"].values())
    finally:
        open(cnt, "w").write(prev)
        out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        with open(os.path.join(LANE, "cycle2", "smoke-stream11.json"), "w") as f:
            json.dump(out, f, indent=1, default=str)
    print(json.dumps({"verdicts": out.get("verdicts"), "all_expected": out.get("all_expected")}, indent=1))


if __name__ == "__main__":
    main()
