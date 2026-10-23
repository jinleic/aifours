#!/usr/bin/env python3
"""Re-run individual UNKNOWN subcases with a longer limit (no existing file is overwritten;
results go to <subcase>_r2.json next to the original).
kinds:
  a3   cycle2/a3/<tag>/fNNNNN.json  (encode_full on the A3 full skeleton NNNNN)
  part cycle2/part/<tag>/fNNNNN.json (encode_partq on the A3' placement NNNNN)
Solver: CaDiCaL -t LIMIT with LRAT streamed into lrat-check (stream_check4, no SIGKILL).
Usage: rerun_unknown.py KIND TAG INDEX LIMIT_S CHECK_BUDGET_S
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_full  # noqa: E402
import encode_partq  # noqa: E402
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def main():
    kind, tag, idx, limit, budget = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
    base = os.path.join(LANE, "cycle2", "a3" if kind == "a3" else "part", tag)
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
    E = json.load(open(os.path.join(base, "ext.json")))
    if kind == "partbatch":
        # idx is the original batch file stem, e.g. batch_04300_04399
        orig = json.load(open(os.path.join(base, idx + ".json")))
        out = os.path.join(base, idx + "_r2.json")
        if os.path.exists(out):
            print("exists", out)
            return
        import encode_partbatch
        F, X, _ = encode_partbatch.build(spec, [E["full"][i] for i in orig["indices"]])
        enc = "encode_partbatch.py"
        name = "r2_pb_%s_%s" % (tag, idx)
    else:
        idx = int(idx)
        out = os.path.join(base, "f%05d_r2.json" % idx)
        if os.path.exists(out):
            print("exists", out)
            return
        sub = dict(spec)
        sub["placed"] = E["full"][idx]
        if kind == "a3":
            F, X, _ = encode_full.build(sub)
            enc = "encode_full.py"
        else:
            F, X, _ = encode_partq.build(sub)
            enc = "encode_partq.py"
        name = "r2_%s_%s_%05d" % (kind, tag, idx)
    r = S.cadical_stream(S.cnf_bytes_of(F), os.path.join(LANE, "scratch", "fifo", name), limit, budget)
    r.update({"tag": tag, "index": idx, "kind": kind, "encoder": enc, "runner": "rerun_unknown.py"})
    if kind == "partbatch":
        r["indices"] = orig["indices"]
    if r["status"] == "SAT":
        os.makedirs(os.path.join(LANE, "cycle2", "witness"), exist_ok=True)
        open(os.path.join(LANE, "cycle2", "witness", name + ".solver.txt"), "w").write(r["solver_out"])
        vals = set()
        for line in r["solver_out"].splitlines():
            if line.startswith("v "):
                vals.update(int(t) for t in line.split()[1:] if t != "0")
        arr = [[([s for s in range(6) if X[a][c][s] in vals] + [-1])[0] for c in range(8)] for a in range(19)]
        wp = os.path.join(LANE, "cycle2", "witness", name + ".txt")
        open(wp, "w").write("".join(" ".join(map(str, row)) + "\n" for row in arr))
        import subprocess
        v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), wp, "19", "8", "6"],
                            capture_output=True, text=True)
        v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), wp, "19", "8", "6"], capture_output=True, text=True)
        r.update({"model_file": os.path.relpath(wp, LANE), "verify1_rc": v1.returncode, "verify2_rc": v2.returncode,
                  "verify1": v1.stdout.strip(), "verify2": v2.stdout.strip()})
    r["solver_out"] = ""
    json.dump(r, open(out, "w"), indent=1)
    print(json.dumps({k: r.get(k) for k in ("tag", "index", "status", "checked", "solve_seconds", "check_seconds")}))


if __name__ == "__main__":
    main()
