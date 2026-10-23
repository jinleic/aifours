#!/usr/bin/env python3
"""witness_controls.py -- controls for a pinned BRD(26,130,25,5,4) witness (README 1.6/1.7), stdlib only.

Usage: witness_controls.py CERT SHA256 MODEL ORIG_RUNDIR OUTDIR
  CERT/SHA256   the pinned witness and its expected sha256;
  MODEL         the model name that produced it (code/brd_models.py), ORIG_RUNDIR the run directory with
                MODEL.spec.json, MODEL.cnf and the solver record MODEL-kissat-t*.json;
  OUTDIR        new directory (must not exist) for the control files and witness-controls.json.
Checks:
  (1) verify_brd.py (with --expect and --sha256) and bin/brd_check (with parameters) both VALID;
  (2) intended-reason mutations of the witness rejected by both checkers with the intended reason
      (sign flip -> PAIRS, move within a row -> COLUMNS, move within a column -> ROWS, wrong lambda -> HEADER,
      CRLF / missing final LF -> FORMAT);
  (3) a third recomputation: integer Gram matrix W W^T == 25 I, |W| W-support Gram == 21 I + 4 J, column weights 5;
  (4) invariance W[pi(i)][tau(j)] == rho(i) sigma(j) W[i][j] for every generator of the model spec;
  (5) producer replay: regenerate spec and CNF in OUTDIR, compare sha256 with the originals, rerun the recorded kissat
      command (same options, same time limit) on the regenerated CNF and compare the decoded witness bytes.
Exit 0 iff all checks pass.
"""
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
PARAMS = [26, 130, 25, 5, 4]


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load(path):
    lines = open(path).read().split("\n")
    return [[int(t) for t in ln.split(" ")] for ln in lines[1:27]]


def text_of(params, rows):
    return "BRD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)


def checkers(path, expect, want_sha=None):
    a = [sys.executable, "-B", os.path.join(CODE, "verify_brd.py"), path, "--expect"] + [str(x) for x in expect]
    if want_sha:
        a += ["--sha256", want_sha]
    pa = subprocess.run(a, capture_output=True, text=True)
    pc = subprocess.run([os.path.join(LANE, "bin", "brd_check"), path] + [str(x) for x in expect],
                        capture_output=True, text=True)
    return pa.stdout.strip(), pc.stdout.strip()


def reason(s):
    if s.startswith("VALID"):
        return "VALID"
    if s.startswith("INVALID "):
        return s.split()[1].rstrip(":")
    return "ERROR"


def main(argv):
    if len(argv) != 6:
        print(__doc__, file=sys.stderr)
        return 2
    cert, want, model, orig, out = argv[1:]
    os.makedirs(out)
    res, ok = {}, True
    # (1)
    a, c = checkers(cert, PARAMS, want)
    res["checkers"] = {"verify_brd": a, "brd_check": c}
    ok &= reason(a) == "VALID" and reason(c) == "VALID"
    rows = load(cert)
    # (2)
    muts = []
    i0 = 0
    j0 = next(j for j in range(130) if rows[i0][j] != 0)
    jz = next(j for j in range(130) if rows[i0][j] == 0)
    iz = next(i for i in range(26) if rows[i][j0] == 0)
    m = [r[:] for r in rows]
    m[i0][j0] = -m[i0][j0]
    muts.append(("sign-flip", "PAIRS", text_of(PARAMS, m).encode(), PARAMS))
    m = [r[:] for r in rows]
    m[i0][jz], m[i0][j0] = m[i0][j0], 0
    muts.append(("move-within-row", "COLUMNS", text_of(PARAMS, m).encode(), PARAMS))
    m = [r[:] for r in rows]
    m[iz][j0], m[i0][j0] = m[i0][j0], 0
    muts.append(("move-within-column", "ROWS", text_of(PARAMS, m).encode(), PARAMS))
    muts.append(("header-lambda-6", "HEADER", text_of([26, 130, 25, 5, 6], rows).encode(), PARAMS))
    base = text_of(PARAMS, rows)
    muts.append(("crlf", "FORMAT", base.replace("\n", "\r\n").encode(), PARAMS))
    muts.append(("no-final-lf", "FORMAT", base[:-1].encode(), PARAMS))
    mres = []
    for name, intended, data, exp in muts:
        p = os.path.join(out, f"mut-{name}.brd")
        with open(p, "xb") as f:
            f.write(data)
        a, c = checkers(p, exp)
        good = reason(a) == intended and reason(c) == intended
        ok &= good
        mres.append({"mutation": name, "intended": intended, "verify_brd": a, "brd_check": c, "pass": good})
    res["mutations"] = mres
    # (3)
    gram_ok = all(sum(rows[i][j] * rows[i2][j] for j in range(130)) == (25 if i == i2 else 0)
                  for i in range(26) for i2 in range(26))
    sup_ok = all(sum(abs(rows[i][j]) * abs(rows[i2][j]) for j in range(130)) == (25 if i == i2 else 4)
                 for i in range(26) for i2 in range(26))
    colw_ok = all(sum(abs(rows[i][j]) for i in range(26)) == 5 for j in range(130))
    res["third_recomputation"] = {"WWt_eq_25I": gram_ok, "support_gram_eq_21I_plus_4J": sup_ok,
                                  "column_weights_5": colw_ok}
    ok &= gram_ok and sup_ok and colw_ok
    # (4)
    spec = json.load(open(os.path.join(orig, f"{model}.spec.json")))
    inv_ok = True
    for g in spec["generators"]:
        for i in range(26):
            pi, rs = g["rows"][i]
            for j in range(130):
                tj, cs = g["cols"][j]
                if rows[pi][tj] != rs * cs * rows[i][j]:
                    inv_ok = False
    res["invariance_under_model_generators"] = inv_ok
    ok &= inv_ok
    # (5)
    rspec = os.path.join(out, f"{model}.spec.json")
    rcnf = os.path.join(out, f"{model}.cnf")
    subprocess.run([sys.executable, "-B", os.path.join(CODE, "brd_models.py"), model, rspec], check=True,
                   capture_output=True)
    orig_cnf = os.path.join(orig, f"{model}.cnf")
    orig_map = json.load(open(orig_cnf + ".map.json"))
    extra = (["--s0"] if orig_map.get("s0") else []) + (["--unsigned"] if orig_map.get("unsigned") else [])
    subprocess.run([sys.executable, "-B", os.path.join(CODE, "brd_cnf.py"), rspec, rcnf] + extra, check=True,
                   capture_output=True)
    recs = sorted(f for f in os.listdir(orig) if f.startswith(f"{model}-kissat") and f.endswith(".json"))
    rec = None
    for f in recs:
        r = json.load(open(os.path.join(orig, f)))
        if r.get("witness_sha256") == want:
            rec = r
    replay = {"spec_sha256_equal": sha(rspec) == sha(os.path.join(orig, f"{model}.spec.json")),
              "cnf_sha256_equal": sha(rcnf) == sha(orig_cnf)}
    if rec is None:
        replay["solver_record"] = "not found"
        ok = False
    else:
        cmd = rec["command"]
        secs = [x for x in cmd if x.startswith("--time=")][0].split("=")[1]
        seed = [x.split("=")[1] for x in cmd if x.startswith("--seed=")]
        args = [sys.executable, "-B", os.path.join(CODE, "brd_run.py"), rcnf, secs, os.path.join(out, "replay")]
        if seed:
            args += ["--seed", seed[0]]
        subprocess.run(args, capture_output=True, text=True)
        rp = os.path.join(out, "replay.brd")
        replay["original_command"] = cmd
        replay["replay_witness_sha256"] = sha(rp) if os.path.exists(rp) else None
        replay["identical_witness_bytes"] = replay["replay_witness_sha256"] == want
    res["producer_replay"] = replay
    ok &= replay.get("spec_sha256_equal", False) and replay.get("cnf_sha256_equal", False) and \
        replay.get("identical_witness_bytes", False)
    res["verdict"] = "WITNESS-CONTROLS PASS" if ok else "WITNESS-CONTROLS FAIL"
    res["cert"], res["cert_sha256"] = cert, sha(cert)
    with open(os.path.join(out, "witness-controls.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps({"verdict": res["verdict"], "replay": replay}, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
