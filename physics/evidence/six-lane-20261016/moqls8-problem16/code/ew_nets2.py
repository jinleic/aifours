"""Consistency checks for the 2165 E–W species representatives of 2-MOLS(8) (README §4):
Latin + orthogonality of every pair; existence of a third square orthogonal to both (exact SAT, CNF streamed to
CaDiCaL's stdin, nothing stored): expected UNSAT for the 2127 maximal, SAT for the 38 non-maximal; nauty canonical
certificates of the 4-net incidence graphs (64 points + 32 lines) pairwise distinct; relabelled-copy controls.
env/venv8/bin/python -B ew_nets2.py --out ../evidence/k3_fixed/ew_nets2.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys

import pynauty

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "sources", "ew_data"))
N = 8


def parse(path):
    lines = open(path).read().split("\n")
    n, k, m = (int(x) for x in lines[0].split()[:3])
    sq, cur = [], []
    for line in lines[1:]:
        s = line.strip()
        if not s:
            if cur:
                sq.append(cur)
                cur = []
            continue
        if len(s) != n or not all("a" <= ch <= "h" for ch in s):
            break
        cur.append([ord(ch) - 97 for ch in s])
    if cur:
        sq.append(cur)
    assert len(sq) == m
    return sq


def latin(L):
    return all(sorted(r) == list(range(N)) for r in L) and \
        all(sorted(L[i][j] for i in range(N)) == list(range(N)) for j in range(N))


def orth(A, B):
    return len({(A[i][j], B[i][j]) for i in range(N) for j in range(N)}) == N * N


def third_square(sqs):
    var = lambda i, j, x: 1 + (i * N + j) * N + x
    cls = []
    for i in range(N):
        for j in range(N):
            cls.append([var(i, j, x) for x in range(N)])
            for x, y in itertools.combinations(range(N), 2):
                cls.append([-var(i, j, x), -var(i, j, y)])
    for x in range(N):
        for i in range(N):
            for j1, j2 in itertools.combinations(range(N), 2):
                cls.append([-var(i, j1, x), -var(i, j2, x)])
        for j in range(N):
            for i1, i2 in itertools.combinations(range(N), 2):
                cls.append([-var(i1, j, x), -var(i2, j, x)])
    for j in range(N):
        cls.append([var(0, j, j)])
    cells = [(i, j) for i in range(N) for j in range(N)]
    for L in sqs:
        for c1, c2 in itertools.combinations(cells, 2):
            if L[c1[0]][c1[1]] == L[c2[0]][c2[1]]:
                for x in range(N):
                    cls.append([-var(c1[0], c1[1], x), -var(c2[0], c2[1], x)])
    text = "p cnf %d %d\n" % (N ** 3, len(cls)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cls)
    r = subprocess.run(["cadical", "-q", "-t", "600"], input=text, capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(r.returncode, "UNKNOWN(%d)" % r.returncode)


def graph(sqs, rng=None):
    cells = [(i, j) for i in range(N) for j in range(N)]
    lab = [lambda c: c[0], lambda c: c[1]] + [(lambda L: (lambda c: L[c[0]][c[1]]))(L) for L in sqs]
    K = len(lab)
    pid = list(range(64))
    cperm = list(range(K))
    lperm = [list(range(N)) for _ in range(K)]
    if rng:
        rng.shuffle(pid)
        rng.shuffle(cperm)
        for q in lperm:
            rng.shuffle(q)
    V = 64 + K * N
    adj = {v: [] for v in range(V)}
    for idx, c in enumerate(cells):
        for cl in range(K):
            line = 64 + cperm[cl] * N + lperm[cl][lab[cl](c)]
            adj[pid[idx]].append(line)
            adj[line].append(pid[idx])
    return pynauty.Graph(V, directed=False, adjacency_dict=adj, vertex_coloring=[set(range(64)), set(range(64, V))])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rng = random.Random(20261017)
    files = [("max", os.path.join(SRC, "maxMOLS8.2.txt")), ("nmax", os.path.join(SRC, "nmaxMOLS8.2.txt"))]
    res = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "sources": {k: hashlib.sha256(open(p, "rb").read()).hexdigest() for k, p in files}, "nets": {}}
    certs = {}
    ctrl_ok = True
    for kind, path in files:
        sq = parse(path)
        for s in range(len(sq) // 2):
            tag = "%s%04d" % (kind, s)
            sqs = sq[2 * s:2 * s + 2]
            g = graph(sqs)
            cert = pynauty.certificate(g)
            certs[tag] = cert
            if s % 50 == 0:                      # relabelled-copy control on a sample of nets
                ctrl_ok &= pynauty.certificate(graph(sqs, rng)) == cert
            res["nets"][tag] = {"latin": all(latin(L) for L in sqs), "orthogonal": orth(*sqs),
                                "third": third_square(sqs), "cert": hashlib.sha256(cert).hexdigest()[:24]}
            if s % 200 == 0:
                print(json.dumps({"tag": tag, **res["nets"][tag]}), flush=True)
    nets = res["nets"]
    res["summary"] = {"nets": len(nets), "max": sum(t.startswith("max") for t in nets),
                      "nmax": sum(t.startswith("nmax") for t in nets),
                      "all_latin_orthogonal": all(v["latin"] and v["orthogonal"] for v in nets.values()),
                      "max_third_UNSAT": all(v["third"] == "UNSAT" for t, v in nets.items() if t.startswith("max")),
                      "nmax_third_SAT": all(v["third"] == "SAT" for t, v in nets.items() if t.startswith("nmax")),
                      "distinct_certificates": len(set(certs.values())), "relabel_controls_ok": ctrl_ok}
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res["summary"]))


if __name__ == "__main__":
    main()
