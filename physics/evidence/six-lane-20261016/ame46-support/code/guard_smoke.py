#!/usr/bin/env python3
"""guard_smoke.py: smoke tests for the resource guard of engine v2 (code/large_t_lex.py), lane ame46-support.

Each run is a separate engine process on the small case (t, e) = (30, 0). Expected outcomes:
 S1 defaults, exploration                       -> EXCLUDED-EXPLORATION, guard not tripped
 S2 defaults, --proof                           -> EXCLUDED; compressed proof streams verified by both checkers
 S3 --rss-cap 20 MiB (intentionally too low)    -> UNKNOWN, guard tripped (RSS), excluded = false
 S4 --proof --disk-budget 1000 B (too low)      -> UNKNOWN, guard tripped (disk), excluded = false
 S5 --max-solutions 0                           -> UNKNOWN (solution cap), excluded = false
 S6 --max-product 50                            -> UNKNOWN (pre-bounds, not attempted), excluded = false
 S7 --max-group 1                               -> UNKNOWN (pre-bounds, not attempted), excluded = false
 S8 Guard around a live long-running CaDiCaL child (PHP(12,11) given on stdin), RSS cap = own RSS + 8 MiB
    -> the watchdog trips during the solve, sends SIGTERM (bounded wait, no SIGKILL), and the child exits by SIGTERM
       without a SAT/UNSAT answer
 S9 Guard with disk budget 65536 B around a live CaDiCaL child writing a compressed LRAT stream for PHP(12,11)
    -> the watchdog sees the growing .gz stream pass the budget, trips, and SIGTERMs the child; no answer, so no proof
"No partial result accepted" means: every guarded run reports outcome UNKNOWN and excluded = false, even when
some profiles had been enumerated before the guard fired.
Reports go to explore/guard_smoke/S*.json; the summary goes to evidence/guard_smoke.json.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
OUTD = os.path.join(LANE, "explore", "guard_smoke")
PY = sys.executable

RUNS = [
    ("S1", [], {"outcome_prefix": "EXCLUDED-EXPLORATION", "tripped": False, "excluded": False}),
    ("S2", ["--proof"], {"outcome_prefix": "EXCLUDED", "tripped": False, "excluded": True}),
    ("S3", ["--rss-cap", str(20 * 2 ** 20)], {"outcome_prefix": "UNKNOWN", "tripped": True, "excluded": False}),
    ("S4", ["--proof", "--disk-budget", "1000"], {"outcome_prefix": "UNKNOWN", "tripped": True, "excluded": False}),
    ("S5", ["--max-solutions", "0"], {"outcome_prefix": "UNKNOWN", "tripped": False, "excluded": False}),
    ("S6", ["--max-product", "50"], {"outcome_prefix": "UNKNOWN", "tripped": False, "excluded": False}),
    ("S7", ["--max-group", "1"], {"outcome_prefix": "UNKNOWN", "tripped": False, "excluded": False}),
]


def php_text(n_holes):
    pig = n_holes + 1
    v = lambda i, j: i * n_holes + j + 1
    cl = [[v(i, j) for j in range(n_holes)] for i in range(pig)]
    cl += [[-v(i, j), -v(k, j)] for j in range(n_holes) for i in range(pig) for k in range(i + 1, pig)]
    return "p cnf %d %d\n" % (pig * n_holes, len(cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cl)


def live_child_tests():
    sys.path.insert(0, HERE)
    import large_t_lex as eng
    out = []
    text = php_text(11)
    base = eng.Guard._rss(os.getpid())
    G = eng.Guard(base + 8 * 2 ** 20, 10 ** 9)
    t0 = time.time()
    st, _ = eng.solve(G, text, 120)
    G.stop()
    ok8 = G.tripped is not None and G.tripped.startswith("RSS") and st not in (10, 20)
    out.append({"run": "S8", "rss_cap_bytes": base + 8 * 2 ** 20, "guard": G.tripped, "solver_returncode": st,
                "seconds": round(time.time() - t0, 1), "match": ok8})
    gzp = os.path.join(OUTD, "S9_php12_11.lrat.gz")
    G = eng.Guard(6 * 2 ** 30, 65536)
    t0 = time.time()
    st, _ = eng.solve(G, text, 120, gzp)
    G.stop()
    ok9 = G.tripped is not None and G.tripped.startswith("disk") and st not in (10, 20)
    out.append({"run": "S9", "disk_budget_bytes": 65536, "guard": G.tripped, "solver_returncode": st,
                "stream_bytes_left": os.path.getsize(gzp) if os.path.exists(gzp) else 0,
                "seconds": round(time.time() - t0, 1), "match": ok9})
    for r in out:
        print(r["run"], "match" if r["match"] else "MISMATCH", "| guard:", r["guard"], "| rc:", r["solver_returncode"],
              flush=True)
    return out


def main():
    os.makedirs(OUTD, exist_ok=True)
    res, allok = [], True
    for name, args, want in RUNS:
        out = os.path.join(OUTD, name + ".json")
        t0 = time.time()
        p = subprocess.run([PY, "-B", os.path.join(HERE, "large_t_lex.py"), "--t", "30", "--e", "0", "--out", out]
                           + args, capture_output=True, text=True, cwd=HERE,
                           env=dict(os.environ, OMP_NUM_THREADS="1"))
        rep = json.load(open(out))
        tripped = rep["guard_tripped"] is not None
        got = {"outcome": rep["outcome"], "tripped": tripped, "guard": rep["guard_tripped"],
               "excluded": rep["excluded"], "seconds": round(time.time() - t0, 1),
               "profile_status": [pr.get("status") for pr in rep["profiles"]]}
        if name == "S2":
            proofs = []
            for pr in rep["profiles"]:
                fp = pr.get("final_proof") or {}
                proofs.append(bool(fp.get("C", {}).get("verified") and fp.get("py", {}).get("verified")))
                for r in pr.get("reps", []):
                    cp = r.get("completion_proof")
                    if cp:
                        proofs.append(bool(cp["C"]["verified"] and cp["py"]["verified"]))
            got["all_stream_proofs_verified_by_both"] = all(proofs) and bool(proofs)
        match = (got["outcome"].startswith(want["outcome_prefix"]) and got["tripped"] == want["tripped"]
                 and got["excluded"] == want["excluded"] and p.returncode == 0)
        if name == "S2":
            match = match and got["all_stream_proofs_verified_by_both"]
        allok &= match
        res.append({"run": name, "args": args, "expected": want, "got": got, "match": match,
                    "report": os.path.relpath(out, LANE), "exit": p.returncode,
                    "stdout_tail": p.stdout.strip().splitlines()[-1:] if p.stdout else [],
                    "stderr_tail": p.stderr.strip().splitlines()[-3:] if p.stderr else []})
        print(name, "match" if match else "MISMATCH", got["outcome"], "| guard:", got["guard"], flush=True)
    live = live_child_tests()
    res += live
    allok &= all(r["match"] for r in live)
    summary = {"runs": res, "all_required_true": bool(allok), "python": sys.version.split()[0]}
    with open(os.path.join(LANE, "evidence", "guard_smoke.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print("all_required_true:", allok)
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
