"""Certification receipt for the six FINAL CNFs (evidence/final_v1): fresh solver runs (no proof) with full raw
output, and drat-trim checks of the hash-pinned lane-local proofs against the final CNFs. Fresh output directory;
nothing deleted/overwritten.

python -B certify_final.py --final ../evidence/final_v1 --outdir ../evidence/final_v1/cert --jobs 2
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
DRAT = os.path.join(LANE, "env", "drat-trim", "drat-trim")
PROOFS = {  # (encoder, class): (proof path relative to lane, generating command as executed, cwd, recorded result)
    ("A", "K2"): ("evidence/k2/a_generic_sb2.drat", "cadical -q --no-binary a_generic_sb2.cnf a_generic_sb2.drat",
                  "evidence/k2", "exit 20, 2026-10-17 03:39:53-03:40:34 PDT"),
    ("A", "K3"): ("evidence/k3/a_k3_sb2.drat", "cadical -q --no-binary a_k3_sb2.cnf a_k3_sb2.drat",
                  "evidence/k3", "exit 20, 03:40:55-03:41:28 PDT"),
    ("A", "K4"): ("evidence/k4/a_k4_sb2.drat", "cadical -q a_k4_sb2.cnf a_k4_sb2.drat",
                  "evidence/k4", "exit 20, 03:52:24-04:06:22 PDT"),
    ("B", "K2"): ("evidence/k2/b_generic_sb2.drat", "kissat -q b_generic_sb2.cnf b_generic_sb2.drat",
                  "evidence/k2", "exit 20, 03:45:18-03:52:04 PDT"),
    ("B", "K3"): ("evidence/k3/b_k3_sb2.drat", "kissat -q b_k3_sb2.cnf b_k3_sb2.drat",
                  "evidence/k3", "see evidence/k3/b_k3_sb2.proofrun.txt and LOG"),
    ("B", "K4"): ("evidence/k4/b_k4_sb2.drat", "kissat -q b_k4_sb2.cnf b_k4_sb2.drat",
                  "evidence/k4", "see evidence/k4/b_k4_sb2.proofrun.txt and LOG"),
}


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def timed(cmd, out_path):
    t0 = time.time()
    with open(out_path, "x") as fh:
        r = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT, text=True)
    return {"argv": cmd, "exit": r.returncode, "secs": round(time.time() - t0, 1), "raw_output": out_path}


def job(inst, outdir, final):
    enc, cls = inst["encoder"], inst["class"]
    cnf = os.path.join(LANE, "evidence", inst["cnf"])
    tag = "%s_%s" % (enc.lower(), cls)
    res = {"encoder": enc, "class": cls, "cnf": inst["cnf"], "cnf_sha256_receipt": inst["cnf_sha256"],
           "cnf_sha256_now": sha(cnf)}
    solver = ["cadical", cnf] if enc == "A" else ["kissat", cnf]
    s = timed(solver, os.path.join(outdir, tag + ".solve.log"))
    s["status_line"] = next((l.strip() for l in open(s["raw_output"]) if l.startswith("s ")), None)
    res["solve"] = s
    proof, gen_cmd, gen_cwd, gen_res = PROOFS[(enc, cls)]
    ppath = os.path.join(LANE, proof)
    res["proof"] = {"path": proof, "exists": os.path.exists(ppath), "generated_by": gen_cmd, "cwd": gen_cwd,
                    "generation_result": gen_res}
    if os.path.exists(ppath):
        res["proof"]["bytes"] = os.path.getsize(ppath)
        res["proof"]["sha256"] = sha(ppath)
        d = timed([DRAT, cnf, ppath, "-t", "50000"], os.path.join(outdir, tag + ".drat-trim.log"))
        txt = open(d["raw_output"]).read()
        d["verified"] = "s VERIFIED" in txt
        d["not_verified"] = "NOT VERIFIED" in txt
        res["drat_trim"] = d
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--jobs", type=int, default=2)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    rec = json.load(open(os.path.join(a.final, "INSTANCES_RECEIPT.json")))
    head = {"argv": sys.argv, "python": sys.version, "script_sha256": sha(__file__),
            "instances_receipt_sha256": sha(os.path.join(a.final, "INSTANCES_RECEIPT.json")),
            "cadical_version": subprocess.run(["cadical", "--version"], capture_output=True, text=True).stdout.strip(),
            "kissat_version": subprocess.run(["kissat", "--version"], capture_output=True, text=True).stdout.strip(),
            "cadical_binary": os.path.realpath("/opt/homebrew/bin/cadical"),
            "kissat_binary": os.path.realpath("/opt/homebrew/bin/kissat"),
            "drat_trim_binary": DRAT, "drat_trim_binary_sha256": sha(DRAT),
            "drat_trim_source_sha256": sha(os.path.join(LANE, "env", "drat-trim", "drat-trim.c"))}
    head["cadical_binary_sha256"] = sha(head["cadical_binary"])
    head["kissat_binary_sha256"] = sha(head["kissat_binary"])
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        results = list(ex.map(lambda inst: job(inst, a.outdir, a.final), rec["instances"]))
    head["results"] = results
    head["all_unsat"] = all(r["solve"]["exit"] == 20 for r in results)
    head["all_proofs_verified"] = all(r.get("drat_trim", {}).get("verified") for r in results)
    with open(os.path.join(a.outdir, "CERT_RECEIPT.json"), "x") as fh:
        json.dump(head, fh, indent=1)
    print(json.dumps({"all_unsat": head["all_unsat"], "all_proofs_verified": head["all_proofs_verified"],
                      "per": [(r["encoder"], r["class"], r["solve"]["exit"], r.get("drat_trim", {}).get("verified"))
                              for r in results]}))


if __name__ == "__main__":
    main()
