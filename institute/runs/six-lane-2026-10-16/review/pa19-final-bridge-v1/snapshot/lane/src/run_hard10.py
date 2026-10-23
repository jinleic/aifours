#!/usr/bin/env python3
"""Runner revision 10 for the remaining M1 ms06 hard cases, staged token-gated pipeline
(stream_check10.kissat_staged: kissat 4.0.4 --seed=1 binary DRAT buffered zstd-1 in memory, then
drat-trim -i; one lane CPU token per pipeline covers CNF construction, solve and check).
  direct TAG...: encode_skel(spec) CNF (SHA compared with pass 1) -> cycle2/hard5/<tag>.json
                 (claims h5_<tag>, shared with run_hard8.py; a tag with an existing record is skipped)
  split TAG...:  one-column placements cycle2/part/<tag>/ext.json (extend_p1q m=1, created if missing)
                 in batches of BATCH -> cycle2/part/<tag>/batch_*.json + summary_batched.json
                 (claims pb9_<tag>, shared with run_hard9.py)
A SAT result writes the decoded array to cycle2/witness/, runs both verifiers and stops the runner.
Stop file cycle2/STOP-hard10 (checked before every case/batch; a released claim is moved to
archive/claims-released/ with a line in archive/MANIFEST.tsv); parent disk floor checked likewise.
Usage: run_hard10.py MODE LIMIT_S CHECK_BUDGET_S BATCH TAG [TAG ...]
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_partbatch  # noqa: E402
import encode_skel  # noqa: E402
import stream_check10 as S  # noqa: E402

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")
STOP = os.path.join(C2, "STOP-hard10")


def claim(name):
    d = os.path.join(C2, "claims")
    os.makedirs(d, exist_ok=True)
    try:
        fd = os.open(os.path.join(d, name + ".claim"), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%d %s run_hard10\n" % (os.getpid(), time.strftime("%Y-%m-%dT%H:%M:%S%z"))).encode())
    os.close(fd)
    return True


def release(name, why):
    src = os.path.join(C2, "claims", name + ".claim")
    rel = os.path.join(LANE, "archive", "claims-released")
    os.makedirs(rel, exist_ok=True)
    dst = os.path.join(rel, name + ".%s.claim" % time.strftime("%Y%m%dT%H%M%S"))
    if os.path.exists(dst):
        raise SystemExit("archive destination exists: " + dst)
    os.rename(src, dst)
    h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
        f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(src, LANE),
                                          os.path.relpath(dst, LANE), h, why))


def must_stop():
    if not os.path.exists(STOP) and not S.disk_free_ok():
        with open(STOP, "w") as f:
            f.write("%s disk floor: free %d < %d bytes\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), S.disk_free_bytes(),
                                                            S.DISK_FLOOR))
    return os.path.exists(STOP)


def handle_sat(name, res, X, spec):
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    vals = set()
    for line in res["solver_out"].splitlines():
        if line.startswith("v "):
            vals.update(int(t) for t in line.split()[1:] if t != "0")
    arr = [[([s for s in range(q) if X[r][c][s] in vals] + [-1])[0] for c in range(k)] for r in range(N)]
    os.makedirs(os.path.join(C2, "witness"), exist_ok=True)
    p = os.path.join(C2, "witness", name + ".txt")
    with open(p, "w") as f:
        f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
    v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), p, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), p, str(N), str(k), str(q)], capture_output=True, text=True)
    res.update({"model_file": os.path.relpath(p, LANE), "verify1_rc": v1.returncode, "verify1": v1.stdout.strip(),
                "verify2_rc": v2.returncode, "verify2": v2.stdout.strip()})


def run_direct(tag, limit, budget):
    out = os.path.join(C2, "hard5", tag + ".json")
    if os.path.exists(out):
        return None
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
    p1 = json.load(open(os.path.join(LANE, "cases19skel", "results", tag + ".json")))
    hold = {}

    def build():
        F, X, _ = encode_skel.build(spec)
        hold["X"] = X
        return S.cnf_bytes_of(F)

    res = S.kissat_staged(build, os.path.join(LANE, "scratch", "fifo", "v10k_" + tag), limit, budget)
    res.update({"tag": tag, "mode": "directk-staged", "encoder": "encode_skel.py", "runner": "run_hard10.py",
                "cnf_matches_pass1_sha": res["cnf_sha256"] == p1["cnf_sha256"]})
    if res["status"] == "SAT":
        handle_sat("direct10_" + tag, res, hold["X"], spec)
    res["solver_out"] = ""
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1)
    return res


def run_split(tag, limit, budget, bsize):
    d = os.path.join(C2, "part", tag)
    if os.path.exists(os.path.join(d, "summary.json")) or os.path.exists(os.path.join(d, "summary_batched.json")):
        return None
    os.makedirs(d, exist_ok=True)
    spec_path = os.path.join(LANE, "cases19skel", "specs", tag + ".json")
    ext = os.path.join(d, "ext.json")
    if not os.path.exists(ext):
        with S.Token():
            subprocess.run([VENV_PY, os.path.join(HERE, "extend_p1q.py"), spec_path, ext, "1"], check=True,
                           capture_output=True)
    E = json.load(open(ext))
    spec = json.load(open(spec_path))
    n = E["num_full"]
    st = {"single_checked": 0, "batches": 0, "batch_UNSAT_checked": 0, "batch_other": 0, "SAT": 0}
    for j in range(0, n, bsize):
        idx = list(range(j, min(n, j + bsize)))
        bp = os.path.join(d, "batch_%05d_%05d.json" % (idx[0], idx[-1]))
        if not os.path.exists(bp) and must_stop():
            return {"stopped": True}
        if os.path.exists(bp):
            r = json.load(open(bp))
        else:
            hold = {}

            def build():
                F, X, sel = encode_partbatch.build(spec, [E["full"][i] for i in idx])
                hold["X"] = X
                return S.cnf_bytes_of(F)

            r = S.kissat_staged(build, os.path.join(LANE, "scratch", "fifo", "v10pb_%s_%05d" % (tag, idx[0])), limit, budget)
            r.update({"tag": tag, "indices": idx, "encoder": "encode_partbatch.py", "runner": "run_hard10.py"})
            if r["status"] == "SAT":
                handle_sat("partbatch10_%s_%05d" % (tag, idx[0]), r, hold["X"], spec)
            r["solver_out"] = ""
            json.dump(r, open(bp, "w"), indent=1)
        st["batches"] += 1
        if r["status"] == "UNSAT" and r["checked"]:
            st["batch_UNSAT_checked"] += len(idx)
        elif r["status"] == "SAT":
            st["SAT"] += 1
            break
        else:
            st["batch_other"] += len(idx)
    res = {"tag": tag, "num_sub": n, **st, "runner": "run_hard10.py"}
    res["decided_unsat"] = st["batch_UNSAT_checked"] == n and st["SAT"] == 0
    json.dump(res, open(os.path.join(d, "summary_batched.json"), "w"), indent=1)
    return res


def main():
    mode, limit, budget, bsize = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    for tag in sys.argv[5:]:
        if must_stop():
            print(time.strftime("%H:%M:%S"), "STOP -- stopping", flush=True)
            return
        cn = ("h5_" if mode == "direct" else "pb9_") + tag
        if not claim(cn):
            continue
        r = run_direct(tag, limit, budget) if mode == "direct" else run_split(tag, limit, budget, bsize)
        if r is None:
            continue
        if r.get("stopped"):
            release(cn, "run_hard10 stop: claim released between batches")
            print(time.strftime("%H:%M:%S"), "stopped inside", cn, "-- claim released", flush=True)
            return
        keep = ("tag", "status", "checked", "solve_seconds", "check_seconds", "drat_bytes", "token", "token_wait_seconds",
                "drat_trim_peak_rss_kb", "num_sub", "batches", "batch_UNSAT_checked", "batch_other", "SAT", "decided_unsat")
        print(time.strftime("%H:%M:%S"), json.dumps({k: r.get(k) for k in keep if k in r}), flush=True)
        if r.get("status") == "SAT" or r.get("SAT"):
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
