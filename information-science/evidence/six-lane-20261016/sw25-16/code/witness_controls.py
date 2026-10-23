#!/usr/bin/env python3
"""Witness controls for a pinned SW(25,16) (lane sw25-16).

Usage (lane root): python3 -B code/witness_controls.py CERT.sw SHA256 OUTDIR ORIG_RUN_PREFIX
  ORIG_RUN_PREFIX e.g. runs/b2-z5-plain-v1/z5-plain (its .spec.json, .cnf, -kissat.json are read, never changed).
OUTDIR must not exist.  Steps:
 1. both checkers VALID on CERT (python with --sha256);
 2. third recomputation with numpy (entries, W = W^T, W W^T = 16 I, row weights, eigenvalues, trace);
 3. intended-reason mutations (mode x files): row 0 negated -> SYMMETRY only; symmetric off-diagonal sign flip ->
    ORTHO only; diagonal flip -> ORTHO only; entry 2 -> ENTRIES (+WEIGHT,ORTHO); zeroed pair -> WEIGHT (+ORTHO);
    header 'SW 25 9' -> HEADER; CRLF -> FORMAT; no final LF -> FORMAT; both checkers must agree;
 4. invariance under the producing model's generators (from the original spec);
 5. producer replay: regenerate spec and CNF with the lane code (sha256 must equal the original run's), rerun the
    recorded solver command through code/sat_run.py (with and without proof stream), decode, compare bytes with CERT.
Writes OUTDIR/witness-controls.json and prints WITNESS-CONTROLS PASS/FAIL.
"""
import hashlib
import json
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = [sys.executable, "-B"]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def checkers(path, n=25, w=16, sha_exp=None):
    a = PY + [os.path.join(LANE, "code/verify_sw.py"), path, "--expect", str(n), str(w)]
    if sha_exp:
        a += ["--sha256", sha_exp]
    py = subprocess.run(a, capture_output=True, text=True).stdout.strip()
    cc = subprocess.run([os.path.join(LANE, "bin/sw_check"), path, str(n), str(w)], capture_output=True,
                        text=True).stdout.strip()
    return py, cc


def parse(line):
    if line.startswith("RESULT VALID"):
        return ("VALID", "", "")
    d = dict(p.split("=", 1) for p in line.split()[2:] if "=" in p)
    return ("INVALID", d.get("primary"), d.get("failing"))


def main():
    cert, sha_exp, out, orig = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    os.mkdir(out)
    res = {"cert": cert, "cert_sha256": sha(cert)}
    ok = res["cert_sha256"] == sha_exp
    # 1
    py, cc = checkers(cert, sha_exp=sha_exp)
    res["checkers"] = {"verify_sw_py": py, "sw_check_c": cc}
    ok &= py.startswith("RESULT VALID SW(25,16)") and cc.startswith("RESULT VALID SW(25,16)")
    # 2
    n, w, Wl = C.read_strict(cert)
    W = np.array(Wl, dtype=np.int64)
    G = W @ W.T
    ev = np.linalg.eigvalsh(W.astype(float))
    npres = {"ternary": bool(np.isin(W, [-1, 0, 1]).all()), "symmetric": bool((W == W.T).all()),
             "gram_is_16I": bool((G == 16 * np.eye(n, dtype=np.int64)).all()),
             "row_weights": sorted(set((W != 0).sum(axis=1).tolist())), "trace": int(np.trace(W)),
             "eigen_plus4": int(np.sum(np.isclose(ev, 4.0))), "eigen_minus4": int(np.sum(np.isclose(ev, -4.0))),
             "nonzero_diagonal": int(np.count_nonzero(np.diag(W)))}
    res["numpy"] = npres
    ok &= npres["ternary"] and npres["symmetric"] and npres["gram_is_16I"] and npres["row_weights"] == [16]
    # 3
    muts = []

    def put(name, text, primary, failing, raw=None):
        p = os.path.join(out, name)
        with open(p, "xb") as f:
            f.write(raw if raw is not None else text.encode("ascii"))
        a, b = checkers(p)
        pa, pb = parse(a), parse(b)
        good = pa == pb == ("INVALID", primary, failing)
        muts.append({"file": name, "sha256": sha(p), "intended_primary": primary, "intended_failing": failing,
                     "verify_sw_py": a, "sw_check_c": b, "pass": good})
        return good

    M = [r[:] for r in Wl]
    M[0] = [-x for x in M[0]]
    ok &= put("mut-row0-negated.sw", C.to_strict(M, n, w), "SYMMETRY", "SYMMETRY")
    i, j = next((i, j) for i in range(n) for j in range(i + 1, n) if Wl[i][j] != 0)
    M = [r[:] for r in Wl]
    M[i][j], M[j][i] = -M[i][j], -M[j][i]
    ok &= put("mut-signflip-pair.sw", C.to_strict(M, n, w), "ORTHO", "ORTHO")
    d = next(k for k in range(n) if Wl[k][k] != 0)
    M = [r[:] for r in Wl]
    M[d][d] = -M[d][d]
    ok &= put("mut-diag-flip.sw", C.to_strict(M, n, w), "ORTHO", "ORTHO")
    M = [r[:] for r in Wl]
    M[i][j] = M[j][i] = 2
    ok &= put("mut-entry-2.sw", C.to_strict(M, n, w), "ENTRIES", "ENTRIES,WEIGHT,ORTHO")
    M = [r[:] for r in Wl]
    M[i][j] = M[j][i] = 0
    ok &= put("mut-zero-pair.sw", C.to_strict(M, n, w), "WEIGHT", "WEIGHT,ORTHO")
    txt = open(cert).read()
    ok &= put("mut-header-w9.sw", txt.replace("SW 25 16", "SW 25 9", 1), "HEADER", "HEADER")
    ok &= put("mut-crlf.sw", txt.replace("\n", "\r\n"), "FORMAT", "FORMAT")
    ok &= put("mut-no-final-lf.sw", txt[:-1], "FORMAT", "FORMAT")
    res["mutations"] = muts
    res["mutation_note"] = f"pair ({i},{j}) used for sign flip / entry 2 / zero; diagonal index {d}"
    # 4
    spec = json.load(open(orig + ".spec.json"))
    inv = all(Wl[g["perm"][a]][g["perm"][b]] == g["sign"][a] * g["sign"][b] * Wl[a][b]
              for g in spec["generators"] for a in range(n) for b in range(n))
    res["invariance"] = {"spec": orig + ".spec.json", "spec_sha256": sha(orig + ".spec.json"), "invariant": inv}
    ok &= inv
    # 5 replay
    orig_run = json.load(open(orig + "-kissat.json"))
    model_args = None
    batch_dir = os.path.dirname(orig)
    for line in open(os.path.join(batch_dir, "batch.jsonl")):
        r = json.loads(line)
        if r["name"] == os.path.basename(orig):
            model_args = r["job"]["model"]
            cnf_opts = r["job"].get("cnf_opts", [])
            tlim = r["job"]["time"]
    R = lambda s: os.path.join(out, "replay" + s)  # noqa: E731
    subprocess.run(PY + [os.path.join(LANE, "code/sw_models.py")] + model_args + [R(".spec.json")], check=True,
                   capture_output=True)
    subprocess.run(PY + [os.path.join(LANE, "code/sw_cnf.py"), R(".spec.json"), R(".cnf")] + cnf_opts, check=True,
                   capture_output=True)
    rep = {"model_args": model_args, "cnf_opts": cnf_opts,
           "spec_sha256": sha(R(".spec.json")), "spec_sha256_orig": sha(orig + ".spec.json"),
           "cnf_sha256": sha(R(".cnf")), "cnf_sha256_orig": orig_run["cnf_sha256"]}
    # the replay spec file differs from the original only if the code changed; the CNF must match byte for byte
    for tag, extra in (("proof", ["--proof"]), ("noproof", [])):
        so = subprocess.run(PY + [os.path.join(LANE, "code/sat_run.py"), "kissat", R(".cnf"), str(tlim),
                                  R("-" + tag + "-kissat")] + extra, capture_output=True, text=True).stdout
        rep[f"solve_{tag}"] = json.loads(so)
        dec = subprocess.run(PY + [os.path.join(LANE, "code/sw_decode.py"), R(".cnf.map.json"),
                                   R("-" + tag + "-kissat.stdout"), R("-" + tag + ".sw")], capture_output=True,
                             text=True).stdout
        rep[f"decode_{tag}"] = json.loads(dec)
        rep[f"identical_bytes_{tag}"] = sha(R("-" + tag + ".sw")) == res["cert_sha256"]
    res["replay"] = rep
    ok &= rep["cnf_sha256"] == rep["cnf_sha256_orig"] and rep["spec_sha256"] == rep["spec_sha256_orig"]
    ok &= rep["identical_bytes_proof"] and rep["identical_bytes_noproof"]
    res["all_pass"] = bool(ok)
    with open(os.path.join(out, "witness-controls.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps({k: res[k] for k in ("cert_sha256", "checkers", "numpy", "invariance")}, indent=1))
    for m in muts:
        print("mutation", m["file"], m["pass"])
    print("replay", json.dumps({k: v for k, v in rep.items() if not k.startswith("decode")}))
    print("WITNESS-CONTROLS", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
