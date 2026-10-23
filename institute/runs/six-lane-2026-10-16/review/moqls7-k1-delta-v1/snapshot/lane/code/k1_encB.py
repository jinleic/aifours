#!/usr/bin/env python3
"""k1_encB.py: independent K1 pattern encoder B (stdlib only). Lane moqls7-maximum.

Same mathematical conditions as encoder A (review/LEMMAS.md, families F1-F4), different encoding: every point p
chooses exactly one support set S (one-hot variable s[p,S]) among the nonempty subsets of its allowed set
(computed here from scratch: the frame line is the class-0 line with label 0, its point with class-1 label j is
e_j, and a point off it avoids the 3 coordinates where its class-1/2/3 lines meet the frame line).
  F2: forbidden pairs: collinear p,q with |S cap S'| = 1;
  F3: on every line every coordinate lies in some chosen support;
  F4: a chosen support S of size >= 2 containing k needs another point of the line covering k.
Enumerates all models (projected on the chosen supports) with CaDiCaL + blocking clauses, then proves the final
CNF UNSAT with kissat (text DRAT) and checks with the lane drat-trim.
Usage: /usr/bin/python3 k1_encB.py CLASSFILE OUTDIR
"""
import hashlib
import itertools
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DRAT_TRIM = os.path.join(HERE, "..", "env", "drat-trim", "drat-trim")


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def encode(net):
    pts = range(len(net))
    lines = []
    for c in range(4):
        for b in sorted({q[c] for q in net}):
            lines.append([p for p in pts if net[p][c] == b])
    frame = [p for p in pts if net[p][0] == 0]
    assert len(frame) == 7
    label = {p: net[p][1] for p in frame}
    allowed = {}
    for p in pts:
        if p in label:
            allowed[p] = (label[p],)
            continue
        forb = set()
        for c in (1, 2, 3):
            (q,) = [q for q in frame if net[q][c] == net[p][c]]
            forb.add(label[q])
        allowed[p] = tuple(k for k in range(7) if k not in forb)
    nv = 0
    s = {}
    for p in pts:
        for r in range(1, len(allowed[p]) + 1):
            for S in itertools.combinations(allowed[p], r):
                nv += 1
                s[(p, S)] = nv
    clauses = []
    for p in pts:
        opts = [s[(p, S)] for (q, S) in s if q == p]
        clauses.append(opts)
        for a, b in itertools.combinations(opts, 2):
            clauses.append([-a, -b])
    opts_of = {p: [S for (q, S) in s if q == p] for p in pts}
    for l in lines:
        for p, q in itertools.combinations(l, 2):
            for S in opts_of[p]:
                for T in opts_of[q]:
                    if len(set(S) & set(T)) == 1:
                        clauses.append([-s[(p, S)], -s[(q, T)]])
        for k in range(7):
            clauses.append([s[(p, S)] for p in l for S in opts_of[p] if k in S])
            for p in l:
                for S in opts_of[p]:
                    if k in S and len(S) >= 2:
                        clauses.append([-s[(p, S)]] + [s[(q, T)] for q in l if q != p for T in opts_of[q] if k in T])
    return nv, clauses, s


def text(nv, clauses):
    return "p cnf %d %d\n" % (nv, len(clauses)) + "".join(" ".join(map(str, c)) + " 0\n" for c in clauses)


def main(classfile, outdir):
    os.makedirs(outdir, exist_ok=True)
    data = json.load(open(classfile))
    out = {"classfile_sha256": sha(classfile), "encoder": "k1_encB.py", "k1_encB_sha256": sha(os.path.abspath(__file__)),
           "drat_trim_sha256": sha(DRAT_TRIM), "classes": []}
    for idx, cls in enumerate(data["classes"]):
        net = [tuple(q) for q in cls["net"]]
        nv, clauses, s = encode(net)
        inv = {v: k for k, v in s.items()}
        blocks, models = [], []
        while True:
            p = subprocess.run(["cadical", "-q"], input=text(nv, clauses + blocks), capture_output=True, text=True)
            if p.returncode == 20:
                break
            assert p.returncode == 10
            m = set()
            for line in p.stdout.splitlines():
                if line.startswith("v "):
                    m |= {int(t) for t in line.split()[1:] if int(t) > 0}
            chosen = sorted(v for v in m if v in inv)
            models.append(sorted("%d:%s" % (inv[v][0], "".join(map(str, inv[v][1]))) for v in chosen))
            blocks.append([-v for v in chosen])      # one-hot: forbidding the chosen tuple blocks exactly this model
        cnf = os.path.join(outdir, "c%d.B.final.cnf" % idx)
        prf = os.path.join(outdir, "c%d.B.drat" % idx)
        with open(cnf, "w") as f:
            f.write(text(nv, clauses + blocks))
        r = subprocess.run(["kissat", "-q", "--no-binary", cnf, prf], capture_output=True, text=True)
        assert r.returncode == 20, r.returncode
        d = subprocess.run([DRAT_TRIM, cnf, prf], capture_output=True, text=True)
        lines = [l.strip() for l in d.stdout.replace("\r", "\n").splitlines()]
        ok = "s VERIFIED" in lines and "s NOT VERIFIED" not in lines
        wsets = [sorted({len(e.split(":")[1]) for e in mdl}) for mdl in models]
        rec = {"class": idx, "n_models": len(models), "model_weight_sets": wsets, "models": models,
               "final_cnf_sha256": sha(cnf), "drat_sha256": sha(prf), "drat_trim": "s VERIFIED" if ok else "NOT VERIFIED"}
        out["classes"].append(rec)
        print(json.dumps({k: rec[k] for k in ("class", "n_models", "model_weight_sets", "drat_trim")}), flush=True)
    with open(os.path.join(outdir, "summaryB.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
