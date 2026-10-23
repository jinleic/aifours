#!/usr/bin/env python3
"""Runner revision 8 (= run_hard5 with stream_check5: kissat/cadical binary DRAT streamed into
drat-trim, acceptance on drat-trim only; results in cycle2/hard5; claims h5_<tag>). Revision 5 text:
Runner revision 5 for the undecided A2 cases (stream_check4: native limits, no SIGKILL,
strict checker gating). Several runner processes may run at once: each tag is claimed with an
exclusive-create claim file (cycle2/claims/<tag>.claim) and skipped if a result exists.

modes:
  directk  encode_skel CNF regenerated in memory (SHA compared with pass 1) -> kissat_stream
           (kissat --time=LIMIT, DRAT -> drat-trim -> LRAT -> lrat-check). result:
           cycle2/hard/<tag>.json
  directc  same CNF -> cadical_stream (cadical -t LIMIT, LRAT -> lrat-check).
  part     A3' partial split (extend_p1q m=1, encode_partq) -> kissat_stream per subcase.
           results: cycle2/part/<tag>/fNNNNN.json and summary.json
A SAT answer writes the model, verifies it with both verifiers and stops this runner.
Usage: run_hard5.py MODE LIMIT_S CHECK_BUDGET_S TAG [TAG ...]   (single worker per process)
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_partq  # noqa: E402
import encode_skel  # noqa: E402
import stream_check5 as S  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "cycle2")
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")


def claim(tag):
    d = os.path.join(OUT, "claims")
    os.makedirs(d, exist_ok=True)
    try:
        fd = os.open(os.path.join(d, tag + ".claim"), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%d %s\n" % (os.getpid(), time.strftime("%Y-%m-%dT%H:%M:%S%z"))).encode())
    os.close(fd)
    return True


def decode(solver_out, X, N, k, q):
    vals = set()
    for line in solver_out.splitlines():
        if line.startswith("v "):
            vals.update(int(t) for t in line.split()[1:] if t != "0")
    return [[([s for s in range(q) if X[r][c][s] in vals] + [-1])[0] for c in range(k)] for r in range(N)]


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


def run_direct(tag, limit, budget, solver):
    out = os.path.join(OUT, "hard5", tag + ".json")
    if os.path.exists(out):
        return None
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
    F, X, _ = encode_skel.build(spec)
    b = S.cnf_bytes_of(F)
    p1 = json.load(open(os.path.join(LANE, "cases19skel", "results", tag + ".json")))
    wd = os.path.join(LANE, "scratch", "fifo", "v8%s_%s" % (solver, tag))
    res = S.kissat_drat(b, wd, limit, budget) if solver == "k" else S.cadical_drat(b, wd, limit, budget)
    res.update({"tag": tag, "mode": "direct" + solver, "encoder": "encode_skel.py", "runner": "run_hard8.py",
                "cnf_matches_pass1_sha": res["cnf_sha256"] == p1["cnf_sha256"]})
    if res["status"] == "SAT":
        handle_sat("direct_" + tag, res, X, spec)
    res["solver_out"] = ""
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(res, open(out, "w"), indent=1)
    return res


def run_part(tag, limit, budget):
    d = os.path.join(OUT, "part", tag)
    summary = os.path.join(d, "summary.json")
    if os.path.exists(summary):
        return None
    os.makedirs(d, exist_ok=True)
    spec_path = os.path.join(LANE, "cases19skel", "specs", tag + ".json")
    ext = os.path.join(d, "ext.json")
    if not os.path.exists(ext):
        subprocess.run([VENV_PY, os.path.join(HERE, "extend_p1q.py"), spec_path, ext, "1"], check=True,
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
            F, X, _ = encode_partq.build(sub)
            r = S.kissat_stream(S.cnf_bytes_of(F), os.path.join(LANE, "scratch", "fifo", "v5p_%s_%05d" % (tag, i)),
                                limit, budget)
            r.update({"tag": tag, "sub_index": i, "encoder": "encode_partq.py", "runner": "run_hard8.py"})
            if r["status"] == "SAT":
                handle_sat("part_%s_f%05d" % (tag, i), r, X, sub)
            r["solver_out"] = ""
            json.dump(r, open(rp, "w"), indent=1)
        if r["status"] == "UNSAT":
            st["UNSAT_checked" if r["checked"] else "UNSAT_unchecked"] += 1
        else:
            st[r["status"]] += 1
        if r["status"] == "SAT":
            break
    res = {"tag": tag, "mode": "part", "num_sub": E["num_full"], "raw": E["raw"], **st}
    res["decided_unsat"] = st["UNSAT_checked"] == E["num_full"]
    json.dump(res, open(summary, "w"), indent=1)
    return res


def main():
    mode, limit, budget = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    for tag in sys.argv[4:]:
        if not claim("h5_" + tag):
            continue
        if mode == "part":
            r = run_part(tag, limit, budget)
        else:
            r = run_direct(tag, limit, budget, "k" if mode == "directk" else "c")
        if r is None:
            continue
        print(time.strftime("%H:%M:%S"), json.dumps({k: r.get(k) for k in (
            "tag", "mode", "status", "checked", "solve_seconds", "check_seconds", "cnf_matches_pass1_sha",
            "num_sub", "UNSAT_checked", "UNSAT_unchecked", "SAT", "UNKNOWN", "decided_unsat")}), flush=True)
        if r.get("status") == "SAT" or r.get("SAT"):
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
