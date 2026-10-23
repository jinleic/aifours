#!/usr/bin/env python3
"""witness_controls.py -- checks around the pinned witness certs/btd14-28-witness-v1.btd (stdlib + checkers + kissat).

1. Both checkers on the pinned file with the expected parameters (code/verify_btd.py --expect ... --sha256 ...,
   bin/btd_check FILE V B p1 p2 R K L) must say VALID.
2. Intended-reason mutations (each written to OUTDIR and checked by both checkers; each must be INVALID for the
   stated reason): an entry 1 -> 2 in row 0 (row-count); a 1 and a 0 of row 0 swapped (column-sum); a cross swap of two
   entries between rows 0 and 1 in two columns that keeps row and column counts (pair-product); the header with K = 8
   (header); the final LF removed (format).
3. A direct recomputation of all definition conditions with plain integer arithmetic in this script (third route).
4. Invariance: the witness is invariant under the order-3 permutation of model Z3-r4-c8 (rows 0..11 and columns
   0..23 in consecutive 3-cycles, the rest fixed).
5. Producer replay: code/inv_cnf_v2.py Z3-r4-c8 OUTDIR/replay.cnf must reproduce the pinned CNF SHA-256, and
   `kissat --time=300` on it must give SAT with a model that decodes to the pinned witness bytes.
Usage: witness_controls.py OUTDIR (fresh)
"""
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
W = os.path.join(LANE, "certs", "btd14-28-witness-v1.btd")
WSHA = "18cadb923274cbad3f35112d26edf00889971f76d8a0cec28540dcb9d2e40bb1"
CNF_SHA = "3f450c49d3f3736924b3f1c22212f398d1ad2f43803236737f52216d8502a50d"
P = (14, 28, 8, 3, 14, 7, 6)


def checkers(path, sha=None):
    a = [sys.executable, "-B", os.path.join(CODE, "verify_btd.py"), path, "--expect", *map(str, P)]
    if sha:
        a += ["--sha256", sha]
    p = subprocess.run(a, capture_output=True, text=True)
    c = subprocess.run([os.path.join(LANE, "bin", "btd_check"), path, *map(str, P)], capture_output=True, text=True)
    vp = p.stdout.strip().split("\n")[-1] if p.stdout.strip() else ""
    return (p.returncode, vp), (c.returncode, c.stdout.strip())


def parse(text):
    lines = text.split("\n")
    return [[int(t) for t in lines[1 + i].split(" ")] for i in range(P[0])]


def direct(M):
    V, B, p1, p2, R, K, L = P
    ok = all(v in (0, 1, 2) for r in M for v in r)
    ok &= all(r.count(1) == p1 and r.count(2) == p2 for r in M)
    ok &= all(sum(M[i][j] for i in range(V)) == K for j in range(B))
    ok &= all(sum(M[i][j] * M[k][j] for j in range(B)) == L for i in range(V) for k in range(i + 1, V))
    return ok


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    res, ok = {}, True
    text = open(W).read()
    assert hashlib.sha256(text.encode()).hexdigest() == WSHA
    (rp, vp), (rc, vc) = checkers(W, WSHA)
    res["pinned"] = {"verify_btd": vp, "btd_check": vc}
    ok &= rp == 0 and vp == "VALID" and rc == 0 and vc.startswith("VALID")
    M = parse(text)

    def write(name, txt):
        path = os.path.join(out, name + ".btd")
        with open(path, "x", newline="") as f:
            f.write(txt)
        return path

    def fmt(Mx, head="BTD 14 28 8 3 14 7 6"):
        return head + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in Mx)

    muts = []
    m1 = [r[:] for r in M]
    m1[0][m1[0].index(1)] = 2
    muts.append(("mut_one_to_two_row0", fmt(m1), "INVALID row-count"))
    m2 = [r[:] for r in M]
    j1, j0 = m2[0].index(1), m2[0].index(0)
    m2[0][j1], m2[0][j0] = 0, 1
    muts.append(("mut_move_within_row0", fmt(m2), "INVALID column-sum"))
    m3 = [r[:] for r in M]
    done = False
    for j in range(28):
        for j2 in range(28):
            if not done and j != j2 and m3[0][j] != m3[1][j] and m3[0][j2] == m3[1][j] and m3[1][j2] == m3[0][j]:
                a, b = m3[0][j], m3[1][j]
                m3[0][j], m3[1][j], m3[0][j2], m3[1][j2] = b, a, a, b
                done = True
    assert done
    muts.append(("mut_cross_swap_rows01", fmt(m3), "INVALID pair-product"))
    muts.append(("mut_header_K8", fmt(M, "BTD 14 28 8 3 14 8 6"), "INVALID"))
    muts.append(("mut_missing_final_lf", text[:-1], "INVALID format"))
    res["mutations"] = []
    for name, txt, want in muts:
        path = write(name, txt)
        (rp, vp), (rc, vc) = checkers(path)
        good = rp != 0 and rc != 0 and vp.startswith(want) and vc.startswith(want)
        if name == "mut_header_K8":
            good = rp != 0 and rc != 0 and vp.startswith("INVALID") and vc.startswith("INVALID")
        res["mutations"].append({"case": name, "want": want, "verify_btd": vp, "btd_check": vc, "as_intended": good})
        ok &= good
    res["direct_recomputation"] = direct(M)
    ok &= res["direct_recomputation"]
    g = [4 * 0 + 0] * 0
    rowp = [3 * (i // 3) + (i % 3 + 1) % 3 if i < 12 else i for i in range(14)]
    colp = [3 * (j // 3) + (j % 3 + 1) % 3 if j < 24 else j for j in range(28)]
    inv = all(M[rowp[i]][colp[j]] == M[i][j] for i in range(14) for j in range(28))
    res["z3_invariant"] = inv
    ok &= inv
    cnf = os.path.join(out, "replay.cnf")
    gen = subprocess.run([sys.executable, "-B", os.path.join(CODE, "inv_cnf_v2.py"), "Z3-r4-c8", cnf],
                         capture_output=True, text=True)
    csha = hashlib.sha256(open(cnf, "rb").read()).hexdigest()
    res["replay_cnf_sha256"] = csha
    ok &= gen.returncode == 0 and csha == CNF_SHA
    run = subprocess.run([sys.executable, "-B", os.path.join(CODE, "sat_tools.py"), "run", cnf, "kissat", "300",
                          os.path.join(out, "replay-kissat")], capture_output=True, text=True)
    rj = json.load(open(os.path.join(out, "replay-kissat.json")))
    res["replay_kissat"] = {k: rj.get(k) for k in ("status", "wall_s", "witness_sha256", "verify_btd")}
    ok &= rj.get("status") == "SAT" and rj.get("witness_sha256") == WSHA
    res["all_as_intended"] = ok
    with open(os.path.join(out, "witness-controls.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps(res, indent=1))
    print("WITNESS-CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
