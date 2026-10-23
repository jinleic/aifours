#!/usr/bin/env python3
"""Run method M1 (encoder E1 + kissat with DRAT proof) over generated case specs.

Usage: run_cases.py CASEDIR WORKERS TIMEOUT_S [TAG_PREFIX ...]
Resumable: cases with an existing results/<tag>.json are skipped.
"""
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_e1  # noqa: E402
import encode_q0  # noqa: E402
import encode_skel  # noqa: E402

LANE = os.path.dirname(HERE)
KISSAT = "/opt/homebrew/bin/kissat"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run_one(casedir, tag, timeout):
    spec = json.load(open(os.path.join(casedir, "specs", tag + ".json")))
    for d in ("cnf", "proof", "results", "logs", "models"):
        os.makedirs(os.path.join(casedir, d), exist_ok=True)
    cnf = os.path.join(casedir, "cnf", tag + ".cnf")
    if spec.get("kind") == "q0":
        F, X, _info = encode_q0.build(spec)
    elif spec.get("kind") == "skel":
        F, X, _info = encode_skel.build(spec)
    else:
        F, X = encode_e1.build(spec["N"], spec["k"], spec["q"], spec["profiles"], spec["M"],
                               lex=spec.get("lex", True), vp=spec.get("vp", True),
                               pb=spec.get("pb", False), dual=spec.get("dual", False),
                               cover=spec.get("cover", False))
    F.write(cnf)
    proof = os.path.join(casedir, "proof", tag + ".drat")
    log = os.path.join(casedir, "logs", tag + ".kissat.log")
    t0 = time.time()
    with open(log, "w") as lf:
        try:
            cmd = [KISSAT, "--seed=1", cnf] + ([] if os.environ.get("NOPROOF") else [proof])
            p = subprocess.run(cmd, stdout=lf, stderr=subprocess.STDOUT, timeout=timeout)
            rc = p.returncode
        except subprocess.TimeoutExpired:
            rc = -1
    dt = time.time() - t0
    status = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    res = {"tag": tag, "status": status, "returncode": rc, "seconds": round(dt, 2),
           "cnf": os.path.relpath(cnf, LANE), "cnf_sha256": sha(cnf),
           "vars": F.nv, "clauses": len(F.clauses), "solver": "kissat 4.0.4 --seed=1",
           "multiset": spec.get("multiset_index"), "mclass": spec.get("mclass_index"),
           "graph6": spec.get("graph6")}
    if os.path.exists(proof):
        res["proof"] = os.path.relpath(proof, LANE)
        res["proof_bytes"] = os.path.getsize(proof)
    if status == "SAT":
        vals = set()
        for line in open(log):
            if line.startswith("v "):
                vals.update(int(t) for t in line.split()[1:] if t != "0")
        N, k, q = spec["N"], spec["k"], spec["q"]
        arr = []
        for r in range(N):
            row = []
            for c in range(k):
                ss = [s for s in range(q) if X[r][c][s] in vals]
                row.append(ss[0] if len(ss) == 1 else -1)
            arr.append(row)
        mpath = os.path.join(casedir, "models", tag + ".txt")
        with open(mpath, "w") as f:
            f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
        v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), mpath,
                             str(N), str(k), str(q)], capture_output=True, text=True)
        v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), mpath, str(N), str(k), str(q)],
                            capture_output=True, text=True)
        res.update({"model": os.path.relpath(mpath, LANE), "model_sha256": sha(mpath),
                    "verify1": v1.stdout.strip(), "verify1_rc": v1.returncode,
                    "verify2": v2.stdout.strip(), "verify2_rc": v2.returncode})
    json.dump(res, open(os.path.join(casedir, "results", tag + ".json"), "w"), indent=1)
    return res


def main():
    casedir, workers, timeout = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    prefixes = sys.argv[4:]
    idx = json.load(open(os.path.join(casedir, "index.json")))
    tags = [c["tag"] for c in idx["cases"]
            if (not prefixes or any(c["tag"].startswith(p) for p in prefixes))
            and not os.path.exists(os.path.join(casedir, "results", c["tag"] + ".json"))]
    print("cases to run:", len(tags), flush=True)
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_one, casedir, t, timeout): t for t in tags}
        for fu in cf.as_completed(futs):
            r = fu.result()
            print(time.strftime("%H:%M:%S"), r["tag"], r["status"], r["seconds"],
                  r.get("proof_bytes"), r.get("verify1_rc"), r.get("verify2_rc"), flush=True)


if __name__ == "__main__":
    main()
