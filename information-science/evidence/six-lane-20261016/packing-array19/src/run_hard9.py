#!/usr/bin/env python3
"""Runner revision 9 (= run_hard6 with stream_check9.kissat_drat: kissat binary DRAT -> drat-trim -i only,
strict 's ' line verdict; claims pb9_<tag>; FIFO prefix v9pb_; stop file cycle2/STOP-hard9 checked between
batches (the claim is then moved to archive/claims-released/ with a MANIFEST line); parent disk floor
checked before every batch). Used for M1 cases whose direct proof could not be checked within the
per-case checker budget. Revision 6 text:
Runner revision 6: A3'' batched one-column placements (M1: extend_p1q + encode_partbatch +
kissat_stream from stream_check4; native limits, no SIGKILL, strict checker gating).
For each tag: placements from cycle2/part/<tag>/ext.json (created with extend_p1q m=1 if
missing); placements already covered by a checked UNSAT single-subcase result f*.json (from
run_hard5 part) are skipped; the rest are solved in batches of BATCH. Batch results:
cycle2/part/<tag>/batch_<i0>_<i1>.json; final cycle2/part/<tag>/summary_batched.json.
Claims: cycle2/claims/pb_<tag>.claim (exclusive create). Tags whose run_hard5 summary.json
exists are skipped. A SAT batch writes the model, verifies it (both verifiers) and stops.
Usage: run_hard6.py LIMIT_S CHECK_BUDGET_S BATCH TAG [TAG ...]
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_partbatch  # noqa: E402
import stream_check9 as S  # noqa: E402
import hashlib  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "cycle2", "part")
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")
STOP = os.path.join(LANE, "cycle2", "STOP-hard9")


def claim(name):
    d = os.path.join(LANE, "cycle2", "claims")
    os.makedirs(d, exist_ok=True)
    try:
        fd = os.open(os.path.join(d, name + ".claim"), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%d %s\n" % (os.getpid(), time.strftime("%Y-%m-%dT%H:%M:%S%z"))).encode())
    os.close(fd)
    return True


def handle_sat(name, r, X, spec):
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    vals = set()
    for line in r["solver_out"].splitlines():
        if line.startswith("v "):
            vals.update(int(t) for t in line.split()[1:] if t != "0")
    arr = [[([s for s in range(q) if X[a][c][s] in vals] + [-1])[0] for c in range(k)] for a in range(N)]
    os.makedirs(os.path.join(LANE, "cycle2", "witness"), exist_ok=True)
    p = os.path.join(LANE, "cycle2", "witness", name + ".txt")
    with open(p, "w") as f:
        f.write("".join(" ".join(map(str, row)) + "\n" for row in arr))
    v1 = subprocess.run([sys.executable, os.path.join(HERE, "verify_pa.py"), p, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    v2 = subprocess.run([os.path.join(LANE, "bin", "verify_pa2"), p, str(N), str(k), str(q)],
                        capture_output=True, text=True)
    r.update({"model_file": os.path.relpath(p, LANE), "verify1_rc": v1.returncode, "verify2_rc": v2.returncode,
              "verify1": v1.stdout.strip(), "verify2": v2.stdout.strip()})


def run(tag, limit, budget, bsize):
    d = os.path.join(OUT, tag)
    if os.path.exists(os.path.join(d, "summary.json")) or os.path.exists(os.path.join(d, "summary_batched.json")):
        return None
    os.makedirs(d, exist_ok=True)
    spec_path = os.path.join(LANE, "cases19skel", "specs", tag + ".json")
    ext = os.path.join(d, "ext.json")
    if not os.path.exists(ext):
        subprocess.run([VENV_PY, os.path.join(HERE, "extend_p1q.py"), spec_path, ext, "1"], check=True,
                       capture_output=True)
    E = json.load(open(ext))
    spec = json.load(open(spec_path))
    n = E["num_full"]
    covered = set()
    for i in range(n):
        fp = os.path.join(d, "f%05d.json" % i)
        if os.path.exists(fp):
            r = json.load(open(fp))
            if r["status"] == "UNSAT" and r["checked"]:
                covered.add(i)
    todo = [i for i in range(n) if i not in covered]
    st = {"single_checked": len(covered), "batches": 0, "batch_UNSAT_checked": 0, "batch_other": 0, "SAT": 0}
    for j in range(0, len(todo), bsize):
        idx = todo[j:j + bsize]
        bp = os.path.join(d, "batch_%05d_%05d.json" % (idx[0], idx[-1]))
        if not os.path.exists(bp) and not os.path.exists(STOP) and not S.disk_free_ok():
            with open(STOP, "w") as f:
                f.write("%s disk floor: free %d < %d bytes\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                                                                S.disk_free_bytes(), S.DISK_FLOOR))
        if not os.path.exists(bp) and os.path.exists(STOP):
            return {"stopped": True}
        if os.path.exists(bp):
            r = json.load(open(bp))
        else:
            F, X, sel = encode_partbatch.build(spec, [E["full"][i] for i in idx])
            r = S.kissat_drat(S.cnf_bytes_of(F), os.path.join(LANE, "scratch", "fifo", "v9pb_%s_%05d" % (tag, idx[0])),
                              limit, budget)
            r.update({"tag": tag, "indices": idx, "encoder": "encode_partbatch.py", "runner": "run_hard9.py"})
            if r["status"] == "SAT":
                handle_sat("partbatch_%s_%05d" % (tag, idx[0]), r, X, spec)
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
    res = {"tag": tag, "num_sub": n, **st}
    res["decided_unsat"] = st["single_checked"] + st["batch_UNSAT_checked"] == n and st["SAT"] == 0
    json.dump(res, open(os.path.join(d, "summary_batched.json"), "w"), indent=1)
    return res


def main():
    limit, budget, bsize = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
    for tag in sys.argv[4:]:
        if os.path.exists(STOP):
            print(time.strftime("%H:%M:%S"), "STOP file present -- stopping", flush=True)
            return
        cn = "pb9_" + tag
        if not claim(cn):
            continue
        r = run(tag, limit, budget, bsize)
        if r is None:
            continue
        if r.get("stopped"):
            src = os.path.join(LANE, "cycle2", "claims", cn + ".claim")
            rel = os.path.join(LANE, "archive", "claims-released")
            os.makedirs(rel, exist_ok=True)
            dst = os.path.join(rel, cn + ".%s.claim" % time.strftime("%Y%m%dT%H%M%S"))
            if os.path.exists(dst):
                raise SystemExit("archive destination exists: " + dst)
            os.rename(src, dst)
            h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
            with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
                f.write("%s\t%s\t%s\t%s\trun_hard9 stop: claim released\n" % (
                    time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(src, LANE), os.path.relpath(dst, LANE), h))
            print(time.strftime("%H:%M:%S"), "stopped inside", cn, "-- claim released", flush=True)
            return
        print(time.strftime("%H:%M:%S"), json.dumps(r), flush=True)
        if r["SAT"]:
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
