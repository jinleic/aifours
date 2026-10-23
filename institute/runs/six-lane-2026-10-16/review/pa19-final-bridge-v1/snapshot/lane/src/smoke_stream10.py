#!/usr/bin/env python3
"""Smoke tests for stream_check10 (staged, token-gated). Writes cycle2/smoke-stream10.json.
  A UNSAT (cases19skel ms04_s00000): kissat_staged and cadical_staged checked, replay SHA matches,
    staged (drat-trim started after the solver exited: check start >= solver end);
  B SAT ((13,5,4) ms04_s00000): status SAT, not checked, no signals, no drat-trim run; the model is
    decoded into a 13x5 array and verified by BOTH verifiers (src/verify_pa.py, bin/verify_pa2);
  C native solver limit 3 s (ms09_s00004): UNKNOWN, not checked, no signals;
  D proof size cap: MAX_RAW set to 100 kB for ms06_s00028 (proof ~160 MB): UNKNOWN with
    proof_cap_hit, the solver stopped by SIGTERM (recorded), not checked;
  E token semaphore with COUNT=1 (cycle2/tokens/COUNT temporarily 1): two threads each running
    ms01_s00890 (pass-1 UNSAT, a few seconds) must not overlap (intervals recorded);
  F a drat-trim negative through the same staged path: the SAT CNF 'p cnf 1 1 / 1 0' with a
    forged 'solver' that writes the binary empty clause and exits 20 -> must NOT be checked.
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
import stream_check10 as S  # noqa: E402

LANE = os.path.dirname(HERE)
FD = os.path.join(LANE, "scratch", "fifo", "smoke10")


def keep(r):
    return {k: r.get(k) for k in ("status", "checked", "solver_stop", "solve_seconds", "encode_seconds", "check_seconds",
                                   "drat_trim", "events", "drat_bytes", "zbuf_bytes", "replay_sha256_matches", "token",
                                   "proof_cap_hit", "drat_trim_peak_rss_kb", "cnf_sha256")}


def skel_cnf(rel):
    F, _, _ = encode_skel.build(json.load(open(os.path.join(LANE, rel))))
    return S.cnf_bytes_of(F)


def main():
    out = {}
    b = skel_cnf("cases19skel/specs/ms04_s00000.json")
    out["A_kissat"] = keep(S.kissat_staged(b, FD + "_Ak", 60))
    out["A_cadical"] = keep(S.cadical_staged(lambda: b, FD + "_Ac", 60))
    F13, X13, _ = encode_skel.build(json.load(open(os.path.join(LANE, "controls", "c13skel", "specs", "ms04_s00000.json"))))
    b = S.cnf_bytes_of(F13)
    for name, fn in (("B_kissat", S.kissat_staged), ("B_cadical", S.cadical_staged)):
        r = fn(b, FD + "_" + name, 60)
        out[name] = keep(r)
        vals = set()
        for line in r.get("solver_out", "").splitlines():
            if line.startswith("v "):
                vals.update(int(t) for t in line.split()[1:] if t != "0")
        arr = [[([s for s in range(4) if X13[a][c][s] in vals] + [-1])[0] for c in range(5)] for a in range(13)]
        wp = os.path.join(LANE, "cycle2", "smoke10-%s-model.txt" % name)
        with open(wp, "w") as f:
            f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
        v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), wp, "13", "5", "4"], capture_output=True, text=True)
        v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), wp, "13", "5", "4"], capture_output=True, text=True)
        out[name].update({"model_file": os.path.relpath(wp, LANE), "verify1_rc": v1.returncode, "verify1": v1.stdout.strip()[-200:],
                          "verify2_rc": v2.returncode, "verify2": v2.stdout.strip()[-200:]})
    b = skel_cnf("cases19skel/specs/ms09_s00004.json")
    out["C_kissat"] = keep(S.kissat_staged(b, FD + "_Ck", 3))
    out["C_cadical"] = keep(S.cadical_staged(b, FD + "_Cc", 3))
    old = S.MAX_RAW
    S.MAX_RAW = 100 * 1024
    out["D_cap"] = keep(S.kissat_staged(skel_cnf("cases19skel/specs/ms06_s00028.json"), FD + "_D", 600))
    S.MAX_RAW = old
    cnt = os.path.join(S.TOK, "COUNT")
    prev = open(cnt).read()
    open(cnt, "w").write("1\n")
    iv = []
    b = open(os.path.join(LANE, "cases19skel", "cnf", "ms01_s00890.cnf"), "rb").read()

    def one(k):
        t0 = time.time()
        r = S.kissat_staged(b, FD + "_E%d" % k, 120)
        iv.append({"k": k, "returned": round(time.time() - t0, 2), "token": r.get("token"), "wait": r.get("token_wait_seconds"),
                   "status": r["status"], "checked": r["checked"], "busy": round(r["solve_seconds"] + r.get("check_seconds", 0), 2)})

    th = [threading.Thread(target=one, args=(k,)) for k in range(2)]
    for t in th:
        t.start()
    for t in th:
        t.join()
    open(cnt, "w").write(prev)
    iv.sort(key=lambda x: x["returned"])
    out["E_token"] = iv
    e_ok = len(iv) == 2 and all(x["checked"] for x in iv) and iv[1]["wait"] >= 0.8 * iv[0]["busy"]
    forged = os.path.join(LANE, "scratch", "fifo", "forged_solver.sh")
    with open(forged, "w") as f:
        f.write("#!/bin/sh\n# forged solver for a negative control: writes the binary empty clause, claims UNSAT\n"
                "printf 'a\\000' > \"$2\"\nexit 20\n")
    os.chmod(forged, 0o755)
    r = S._drat_staged(b"p cnf 1 1\n1 0\n", FD + "_F", 30, 60, lambda c, p, lim: [forged, c, p], "kissat")
    out["F_forged_empty_clause"] = keep(r)
    ok = (out["A_kissat"]["checked"] and out["A_cadical"]["checked"]
          and out["A_kissat"]["replay_sha256_matches"] and out["A_cadical"]["replay_sha256_matches"]
          and out["B_kissat"]["status"] == "SAT" and out["B_cadical"]["status"] == "SAT"
          and not out["B_kissat"]["checked"] and not out["B_cadical"]["checked"]
          and not out["B_kissat"]["events"] and not out["B_cadical"]["events"]
          and out["B_kissat"]["verify1_rc"] == 0 and out["B_kissat"]["verify2_rc"] == 0
          and out["B_cadical"]["verify1_rc"] == 0 and out["B_cadical"]["verify2_rc"] == 0
          and out["C_kissat"]["status"] == "UNKNOWN" and out["C_cadical"]["status"] == "UNKNOWN"
          and not out["C_kissat"]["events"] and not out["C_cadical"]["events"]
          and out["D_cap"]["status"] == "UNKNOWN" and out["D_cap"]["proof_cap_hit"] and not out["D_cap"]["checked"]
          and e_ok and out["F_forged_empty_clause"]["status"] == "UNSAT" and not out["F_forged_empty_clause"]["checked"])
    out["all_expected"] = bool(ok)
    out["E_serialized"] = bool(e_ok)
    json.dump(out, open(os.path.join(LANE, "cycle2", "smoke-stream10.json"), "w"), indent=1)
    print(json.dumps({k: ((v.get("status"), v.get("checked"), v.get("solve_seconds"), v.get("check_seconds"))
                          if isinstance(v, dict) else v) for k, v in out.items()}, indent=1))


if __name__ == "__main__":
    main()
