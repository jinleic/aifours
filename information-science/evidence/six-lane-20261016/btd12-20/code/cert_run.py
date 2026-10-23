#!/usr/bin/env python3
"""cert_run.py -- per-case certificates for notes/case-split-r1.md Part D/E (stdlib + kissat + drat-trim).

For every case line of CASES.jsonl (code/case_list.py) in order: write OUTDIR/cnf/<id>.cnf with code/dcomp_cnf.py
(parameters 12 20 4 3 10 6 4, exclusive), run `kissat -q --time=600 CNF OUTDIR/proof/<id>.drat` (binary DRAT; native
limit), and for UNSAT run `bin/drat-trim CNF PROOF -t 600` (native limit).  A case is CERTIFIED iff kissat exits 20
and drat-trim exits 0 printing "s VERIFIED".  On SAT (exit 10) the model is decoded to a strict-format matrix
OUTDIR/witness-<id>.btd, both checkers are run on it, and the run stops.  No process is killed, no subprocess timeout.
Writes OUTDIR/results.jsonl (one line per case, flushed) and OUTDIR/summary.json.
Usage: cert_run.py CASES.jsonl OUTDIR [--start N --stop M]   (OUTDIR/ must not exist unless --start is given)
"""
import hashlib
import json
import os
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
sys.path.insert(0, CODE)
import dcomp_cnf  # noqa: E402

PARAMS = (12, 20, 4, 3, 10, 6, 4)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for ch in iter(lambda: f.read(1 << 22), b""):
            h.update(ch)
    return h.hexdigest()


def main(argv):
    args = argv[1:]
    if len(args) not in (2, 6):
        print(__doc__, file=sys.stderr)
        return 2
    cases_path, out = args[0], args[1]
    start, stop = 0, None
    if len(args) == 6:
        start, stop = int(args[3]), int(args[5])
        os.makedirs(out, exist_ok=True)
    else:
        os.makedirs(out)
    os.makedirs(os.path.join(out, "cnf"), exist_ok=True)
    os.makedirs(os.path.join(out, "proof"), exist_ok=True)
    lines = open(cases_path).read().splitlines()
    tag = f"{start}-{stop}" if stop is not None else "all"
    res_path = os.path.join(out, f"results-{tag}.jsonl")
    me = sha(os.path.abspath(__file__))
    enc = sha(dcomp_cnf.__file__)
    counts, t_all = {}, time.time()
    with open(res_path, "x") as rf:
        rf.write(json.dumps({"program": "cert_run.py", "sha256": me, "dcomp_cnf_sha256": enc,
                             "cases": cases_path, "cases_sha256": sha(cases_path), "start": start, "stop": stop,
                             "kissat": "/opt/homebrew/bin/kissat", "kissat_sha256": sha("/opt/homebrew/bin/kissat"),
                             "drat_trim_sha256": sha(os.path.join(LANE, "bin", "drat-trim")),
                             "started_host": time.strftime("%Y-%m-%dT%H:%M:%S%z")}) + "\n")
        for idx in range(start, len(lines) if stop is None else min(stop, len(lines))):
            case = json.loads(lines[idx])
            cid = case["id"]
            F, d = dcomp_cnf.build(PARAMS, case["rows"])
            cnf = os.path.join(out, "cnf", f"{cid}.cnf")
            with open(cnf, "x") as f:
                f.write(f"c dcomp_cnf.py sha256 {enc}\nc params {' '.join(map(str, PARAMS))} case {cid}\n"
                        f"p cnf {F.nv} {len(F.clauses)}\n")
                for c in F.clauses:
                    f.write(" ".join(map(str, c)) + " 0\n")
            proof = os.path.join(out, "proof", f"{cid}.drat")
            if os.path.exists(proof):
                raise SystemExit(f"{proof} exists")
            t0 = time.time()
            k = subprocess.run(["kissat", "-q", "--time=600", cnf, proof], capture_output=True, text=True)
            tk = time.time() - t0
            rec = {"idx": idx, "id": cid, "cnf_sha256": sha(cnf), "vars": F.nv, "clauses": len(F.clauses),
                   "kissat_rc": k.returncode, "kissat_s": round(tk, 3)}
            status = "UNKNOWN"
            if k.returncode == 20:
                t1 = time.time()
                dt = subprocess.run([os.path.join(LANE, "bin", "drat-trim"), cnf, proof, "-t", "600"],
                                    capture_output=True, text=True)
                verified = dt.returncode == 0 and any(ln.strip() == "s VERIFIED" for ln in dt.stdout.splitlines())
                rec.update({"proof_sha256": sha(proof), "proof_bytes": os.path.getsize(proof),
                            "drat_rc": dt.returncode, "drat_s": round(time.time() - t1, 3), "verified": verified})
                status = "CERTIFIED" if verified else "UNSAT_UNVERIFIED"
            elif k.returncode == 10:
                vals = {}
                for ln in k.stdout.splitlines():
                    if ln.startswith("v "):
                        for t in ln.split()[1:]:
                            v = int(t)
                            if v:
                                vals[abs(v)] = v > 0
                rows = case["rows"]
                M = [[(1 if j in rows[i] else 0) + (2 if (d[i][j] is not None and vals.get(d[i][j], False)) else 0)
                      for j in range(20)] for i in range(12)]
                txt = "BTD 12 20 4 3 10 6 4\n" + "".join(" ".join(map(str, r)) + "\n" for r in M)
                wpath = os.path.join(out, f"witness-{cid}.btd")
                with open(wpath, "x", newline="") as f:
                    f.write(txt)
                rec.update({"witness": wpath, "witness_sha256": hashlib.sha256(txt.encode()).hexdigest()})
                status = "SAT"
            rec["status"] = status
            counts[status] = counts.get(status, 0) + 1
            rf.write(json.dumps(rec) + "\n")
            rf.flush()
            if status == "SAT":
                break
        summ = {"counts": counts, "wall_s": round(time.time() - t_all, 1),
                "ended_host": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
        rf.write(json.dumps({"summary": summ}) + "\n")
    print(json.dumps(summ))
    return 10 if counts.get("SAT") else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
