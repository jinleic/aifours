"""Producer + receipt for the GENERIC-mode controls (encoder A + CaDiCaL and encoder B + kissat), FRESH directory.

python -B run_generic_controls.py --outdir ../evidence/kctl_v2

Controls (expected SAT; the decoded model must pass check_model.py, which exits non-zero on any violation):
  G1  one quantum square + one generic classical square, quantum square has a weight>=3 entry (Cor-7 type exists)
  G2  two quantum squares (no classical), Psi1 has a weight>=3 entry (the Cor-7 pair exists)
  G3/G4/G5  (informational, not part of the pass criterion; shorter timeout) the K2/K3/K4 generic encodings WITHOUT
            (P4) and without SB2 (classical configurations exist, e.g. squares of
            AG(2,7)); exercises the generic MOLS encoding with 2/1/0 variable classical squares and 2/3/4 pattern squares
Nothing is deleted or overwritten (directory must not exist; files opened with mode 'x').
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENC = os.path.join(HERE, "k2_encode_a_r2.py")
ENCB = os.path.join(HERE, "k2_encode_b_r2.py")
CHK = os.path.join(HERE, "check_model_r2.py")
N = 7


def decode_b(model_path, map_path, out_path):
    """independent decoder for encoder B models (variable table keys are JSON tuples)."""
    true = set()
    for line in open(model_path):
        if line.startswith("v "):
            true.update(int(t) for t in line.split()[1:] if int(t) > 0)
    table = json.load(open(map_path))
    L, S = {}, {}
    for key, v in table.items():
        k = json.loads(key)
        if not isinstance(k, list) or v not in true:
            continue
        if k[0] == "L":
            _, t, r, c, x = k
            L.setdefault(t, [[None] * N for _ in range(N)])[r][c] = x
        elif k[0] == "S":
            _, s_, r, c, kk = k
            S.setdefault(s_, [[[] for _ in range(N)] for _ in range(N)])[r][c].append(kk)
    out = {}
    for t, A in L.items():
        A[0] = list(range(N))
        out["L%d" % t] = A
    for s_, P in S.items():
        for j in range(N):
            P[0][j] = [j]
        out["S%d" % s_] = [[sorted(x) for x in row] for row in P]
    with open(out_path, "x") as fh:
        json.dump(out, fh, indent=1)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run(cmd, full_stdout=False, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    return {"argv": cmd, "exit": r.returncode, "stdout": r.stdout if full_stdout else r.stdout[-4000:],
            "stderr": r.stderr[-4000:]}


CONTROLS = [   # (tag, encoder args, --w3 labels for the checker, ignore-P3, required)
    ("G1", ["--quantum", "1", "--ngeneric", "1", "--p4", "1"], "1", False, True),
    ("G2", ["--quantum", "12", "--ngeneric", "0", "--p4", "1"], "1", False, True),
    ("G3_K2_noP4", ["--quantum", "12", "--ngeneric", "2", "--p4", "none"], "none", False, False),
    ("G4_K3_noP4", ["--quantum", "123", "--ngeneric", "1", "--p4", "none"], "none", False, False),
    ("G5_K4_noP4", ["--quantum", "1234", "--ngeneric", "0", "--p4", "none"], "none", False, False),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--extra-timeout", type=int, default=1200)
    ap.add_argument("--jobs", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    rec = {"argv": sys.argv, "python": sys.version, "script_sha256": sha(__file__), "encoder_a_sha256": sha(ENC),
           "encoder_b_sha256": sha(ENCB), "checker_sha256": sha(CHK),
           "cadical": run(["cadical", "--version"])["stdout"].strip(),
           "kissat": run(["kissat", "--version"])["stdout"].strip(),
           "cadical_binary_sha256": sha(os.path.realpath("/opt/homebrew/bin/cadical")),
           "kissat_binary_sha256": sha(os.path.realpath("/opt/homebrew/bin/kissat")), "controls": []}
    import concurrent.futures as cf

    def one(spec):
        tag0, args, w3, nop3, required, enc_tag = spec
        tag = "%s_%s" % (enc_tag.lower(), tag0)
        tmo = a.timeout if required else a.extra_timeout
        cnf = os.path.join(a.outdir, tag + ".cnf")
        mp = cnf + ".map.json"
        if enc_tag == "A":
            e = run([sys.executable, "-B", ENC, "--mode", "generic"] + args + ["--cnf", cnf, "--map", mp])
            solver = ["cadical", "-q", "-t", str(tmo), cnf]
        else:
            e = run([sys.executable, "-B", ENCB, "--mode", "generic"] + args + ["--cnf", cnf])
            solver = ["kissat", "-q", "--time=%d" % tmo, cnf]
        item = {"tag": tag, "encoder": enc_tag, "required": required, "encode": e}
        if e["exit"] == 0:
            item["cnf_sha256"] = sha(cnf)
            s_ = run(solver, full_stdout=True)          # full model (the v2 run truncated it: bug)
            model = os.path.join(a.outdir, tag + ".model.txt")
            with open(model, "x") as fh:
                fh.write(s_["stdout"])
            item["solve"] = {k: s_[k] for k in ("argv", "exit", "stderr")}
            item["status"] = {10: "SAT", 20: "UNSAT"}.get(s_["exit"], "ERR%d" % s_["exit"])
            if item["status"] == "SAT":
                pat = os.path.join(a.outdir, tag + ".pattern.json")
                if enc_tag == "A":
                    item["decode"] = run([sys.executable, "-B", ENC, "--decode", model, "--map", mp, "--out", pat])
                else:
                    decode_b(model, mp, pat)
                    item["decode"] = {"decoder": "decode_b (this script)"}
                item["check"] = run([sys.executable, "-B", CHK, pat, "--w3", w3] + (["--no-p3"] if nop3 else []),
                                    cwd=HERE)
        item["pass"] = item.get("status") == "SAT" and item.get("check", {}).get("exit") == 0
        with open(os.path.join(a.outdir, "RECEIPT_%s.json" % tag), "x") as fh:
            json.dump(item, fh, indent=1)
        print(json.dumps({"tag": tag, "required": required, "status": item.get("status"),
                          "check_exit": item.get("check", {}).get("exit"), "pass": item["pass"]}), flush=True)
        return item

    specs = [c + (enc,) for c in CONTROLS for enc in ("A", "B")]
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        rec["controls"] = list(ex.map(one, specs))
    ok_all = all(i["pass"] for i in rec["controls"] if i["required"])
    rec["informational"] = {i["tag"]: (i.get("status"), i["pass"]) for i in rec["controls"] if not i["required"]}
    rec["all_required_pass"] = ok_all
    with open(os.path.join(a.outdir, "RECEIPT.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({"all_required_pass": ok_all, "informational": rec["informational"]}))
    if not ok_all:
        sys.exit("GENERIC CONTROL FAILURE")


if __name__ == "__main__":
    main()
