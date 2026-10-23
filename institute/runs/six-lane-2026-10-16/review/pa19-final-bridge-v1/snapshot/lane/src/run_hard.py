#!/usr/bin/env python3
"""Cycle-2 driver for the A2 cases left UNKNOWN by pass 1 (method M1 family, online-checked).

mode a3:     A3 full-skeleton split (extend_p1.py, all special columns) -> encode_full ->
             kissat_stream (binary DRAT -> drat-trim -> LRAT -> lrat-check, all streamed).
mode direct: encode_skel CNF regenerated in memory (SHA-256 compared with pass 1) ->
             cadical_stream (LRAT -> lrat-check, streamed).
Nothing but small JSON results is written. A SAT answer stops the run after the model is
written and verified by both verifiers.
Usage: run_hard.py MODE WORKERS TIMEOUT_S TAG [TAG ...]
"""
import concurrent.futures as cf
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_full  # noqa: E402
import encode_skel  # noqa: E402
import stream_check  # noqa: E402

LANE = os.path.dirname(HERE)
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")
OUT = os.path.join(LANE, "cycle2")


def decode(solver_out, X, N, k, q):
    vals = set()
    for line in solver_out.splitlines():
        if line.startswith("v "):
            vals.update(int(t) for t in line.split()[1:] if t != "0")
    arr = []
    for r in range(N):
        row = []
        for c in range(k):
            ss = [s for s in range(q) if X[r][c][s] in vals]
            row.append(ss[0] if len(ss) == 1 else -1)
        arr.append(row)
    return arr


def handle_sat(name, res, X, spec):
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    arr = decode(res["solver_out"], X, N, k, q)
    os.makedirs(os.path.join(OUT, "witness"), exist_ok=True)
    p = os.path.join(OUT, "witness", name + ".txt")
    with open(p, "w") as f:
        f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
    v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), p, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), p, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    res.update({"model_file": os.path.relpath(p, LANE), "verify1_rc": v1.returncode, "verify1": v1.stdout.strip(),
                "verify2_rc": v2.returncode, "verify2": v2.stdout.strip()})


def run_direct(tag, timeout):
    out = os.path.join(OUT, "hard", tag + ".json")
    if os.path.exists(out):
        return json.load(open(out))
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
    F, X, _ = encode_skel.build(spec)
    b = stream_check.cnf_bytes_of(F)
    p1 = json.load(open(os.path.join(LANE, "cases19skel", "results", tag + ".json")))
    res = stream_check.cadical_stream(b, os.path.join(LANE, "scratch", "fifo", "d_" + tag), timeout)
    res.update({"tag": tag, "mode": "direct", "encoder": "encode_skel.py",
                "cnf_matches_pass1_sha": res["cnf_sha256"] == p1["cnf_sha256"],
                "regenerate": "python3 src/encode_skel.py via run_hard.py direct (spec cases19skel/specs/%s.json)" % tag})
    if res["status"] == "SAT":
        handle_sat("direct_" + tag, res, X, spec)
    res["solver_out"] = ""
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1)
    return res


def run_a3(tag, timeout):
    summary = os.path.join(OUT, "a3", tag, "summary.json")
    if os.path.exists(summary):
        return json.load(open(summary))
    d = os.path.join(OUT, "a3", tag)
    os.makedirs(d, exist_ok=True)
    spec_path = os.path.join(LANE, "cases19skel", "specs", tag + ".json")
    ext = os.path.join(d, "ext.json")
    if not os.path.exists(ext):
        subprocess.run([VENV_PY, os.path.join(HERE, "extend_p1.py"), spec_path, ext], check=True,
                       capture_output=True)
    E = json.load(open(ext))
    spec = json.load(open(spec_path))
    st = {"UNSAT_checked": 0, "UNSAT_unchecked": 0, "SAT": 0, "UNKNOWN": 0}
    for i, pl in enumerate(E["full"]):
        rp = os.path.join(d, "f%05d.json" % i)
        if os.path.exists(rp):
            r = json.load(open(rp))
        else:
            sub = dict(spec)
            sub["placed"] = pl
            F, X, info = encode_full.build(sub)
            b = stream_check.cnf_bytes_of(F)
            r = stream_check.kissat_stream(b, os.path.join(LANE, "scratch", "fifo", "a3_%s_%05d" % (tag, i)), timeout)
            r.update({"tag": tag, "full_index": i, "encoder": "encode_full.py", "leave": info["leave"]})
            if r["status"] == "SAT":
                handle_sat("a3_%s_f%05d" % (tag, i), r, X, sub)
            r["solver_out"] = ""
            json.dump(r, open(rp, "w"), indent=1)
        if r["status"] == "UNSAT":
            st["UNSAT_checked" if r["checked"] else "UNSAT_unchecked"] += 1
        else:
            st[r["status"]] += 1
        if r["status"] == "SAT":
            break
    res = {"tag": tag, "mode": "a3", "num_full": E["num_full"], "raw": E["raw"], **st}
    res["decided_unsat"] = st["UNSAT_checked"] == E["num_full"]
    json.dump(res, open(summary, "w"), indent=1)
    return res


def main():
    mode, workers, timeout = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    tags = sys.argv[4:]
    fn = run_direct if mode == "direct" else run_a3
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fn, t, timeout): t for t in tags}
        for fu in cf.as_completed(futs):
            r = fu.result()
            print(time.strftime("%H:%M:%S"), json.dumps({k: r.get(k) for k in (
                "tag", "status", "checked", "solve_seconds", "cnf_matches_pass1_sha", "num_full",
                "UNSAT_checked", "UNSAT_unchecked", "SAT", "UNKNOWN", "decided_unsat")}), flush=True)
            if r.get("status") == "SAT" or r.get("SAT"):
                print("SAT FOUND -- stopping", flush=True)
                os._exit(3)


if __name__ == "__main__":
    main()
