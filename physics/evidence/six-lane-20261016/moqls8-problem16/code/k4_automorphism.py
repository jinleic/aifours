"""K4 base-CNF automorphism check (proposed README §9.1, orbit reduction). For a permutation σ of {0..7} fixing 0..4
(acting on rows, columns and coordinates simultaneously: cell (i,j) ↦ (σi, σj), |k⟩ ↦ |σk⟩) and the induced
relabelling ρ of the squares Q2, Q3, Q4 (whose (1,0) singletons are 5, 6, 7; Q1 and the weight-1 square 5 fixed),
build the variable permutation π on ALL variables of the K4 base CNF from their semantic names (g, b3, c4, u5, w3; the
auxiliary keys are re-normalised: b3 operand order, c4 sorted pair, frame lines by row/column identity), and check
(1) π is a bijection on 1..V, (2) π(F) = F as clause multisets (exact comparison of the sorted lists of per-clause
BLAKE2b-128 digests of the sorted literal tuples), (3) π maps each declared V1/V2 cube literal to the expected one.
The base is rebuilt in memory with gram_a_r3.py build() (recorded arguments) and its serialisation SHA-256 must equal
the pinned base SHA. Consequence used: for a CNF automorphism π, F ∧ c is UNSAT iff F ∧ π(c) is UNSAT.
python -B k4_automorphism.py --sigma 5:6,6:5 --sigma 6:7,7:6 --out ../evidence/k4_split_v1/AUTOMORPHISM_S3_567.json
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_SHA = "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7"
V1 = [57, 106, 155, 204, 253, 302, 351]
V2 = [64, 113, 162, 211, 260, 309, 358]


def load_r3():
    spec = importlib.util.spec_from_file_location("gram_a_r3", os.path.join(HERE, "gram_a_r3.py"))
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    return G


def line_of(c0, c1):
    return ("row", c0[0]) if c0[0] == c1[0] else ("col", c0[1])


def first_two(line):
    kind, x = line
    return ((x, 0), (x, 1)) if kind == "row" else ((0, x), (1, x))


def check(f, sig):
    sigma = list(range(8))
    for a, b in sig.items():
        sigma[a] = b
    assert sorted(sigma) == list(range(8)) and all(sigma[k] == k for k in range(5))
    coord = {2: 5, 3: 6, 4: 7}
    inv = {v: k for k, v in coord.items()}
    rho = {1: 1, 5: 5}
    for s, c in coord.items():
        rho[s] = inv[sigma[c]]
    cell = lambda p: (sigma[p[0]], sigma[p[1]])

    def img(name):
        t = name[0]
        if t == "g":
            return ("g", rho[name[1]]) + tuple(sorted((cell(name[2]), cell(name[3]))))
        if t == "b3":
            s, x, y, z = name[1:]
            return [("b3", rho[s], cell(x), cell(y), cell(z)), ("b3", rho[s], cell(y), cell(x), cell(z))]
        if t == "c4":
            s, a, p, q = name[1:]
            return ("c4", rho[s], cell(a)) + tuple(sorted((cell(p), cell(q))))
        if t == "u5":
            s, l0, l1, q, a = name[1:]
            kind, x = line_of(l0, l1)
            m0, m1 = first_two((kind, sigma[x]))
            return ("u5", rho[s], m0, m1, cell(q), cell(a))
        if t == "w3":
            s, l0, l1, p = name[1:]
            kind, x = line_of(l0, l1)
            m0, m1 = first_two((kind, sigma[x]))
            return ("w3", rho[s], m0, m1, cell(p))
        raise ValueError("unexpected variable family %r" % (t,))

    names = f.names
    perm = [0] * (f.nv + 1)
    missing = []
    for name, v in names.items():
        im = img(name)
        if isinstance(im, list):
            hits = [names[x] for x in im if x in names]
            if len(hits) != 1:
                missing.append([repr(name), len(hits)])
                continue
            perm[v] = hits[0]
        else:
            if im not in names:
                missing.append([repr(name), 0])
                continue
            perm[v] = names[im]
    bij = not missing and sorted(perm[1:]) == list(range(1, f.nv + 1))
    res = {"sigma": sigma, "rho": rho, "variables": f.nv, "unmapped_names": missing[:5],
           "unmapped_count": len(missing), "bijection": bij}
    if not bij:
        return res
    d0, d1 = [], []
    for cl in f.clauses:
        d0.append(hashlib.blake2b(" ".join(map(str, sorted(cl))).encode(), digest_size=16).digest())
        im = [perm[l] if l > 0 else -perm[-l] for l in cl]
        d1.append(hashlib.blake2b(" ".join(map(str, sorted(im))).encode(), digest_size=16).digest())
    d0.sort()
    d1.sort()
    res["clauses"] = len(d0)
    res["clause_multiset_invariant"] = d0 == d1
    del d0, d1
    lm = lambda l: perm[l] if l > 0 else -perm[-l]
    res["V1_image"] = [lm(v) for v in V1]
    res["V2_image"] = [lm(v) for v in V2]
    res["V1_expected"] = [V1[sigma[k] - 1] for k in range(1, 8)]
    res["V2_expected"] = [V2[sigma[k] - 1] for k in range(1, 8)]
    res["cube_vars_ok"] = res["V1_image"] == res["V1_expected"] and res["V2_image"] == res["V2_expected"]
    res["automorphism"] = bool(res["clause_multiset_invariant"] and res["cube_vars_ok"])
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sigma", action="append", required=True, help="e.g. 5:6,6:5 (repeatable)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    G = load_r3()
    f = G.build(8, "generic", [], [1, 2, 3, 4, 5], 0, [1, 2, 3, 4], True, True, None, True, False, True, 5)
    h = hashlib.sha256(("p cnf %d %d\n" % (f.nv, len(f.clauses))).encode())
    for cl in f.clauses:
        h.update((" ".join(map(str, cl)) + " 0\n").encode())
    out = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "gram_a_r3_sha256": hashlib.sha256(open(os.path.join(HERE, "gram_a_r3.py"), "rb").read()).hexdigest(),
           "rebuilt_sha256": h.hexdigest(), "base_sha_matches": h.hexdigest() == BASE_SHA, "checks": []}
    for s in a.sigma:
        sig = {int(x.split(":")[0]): int(x.split(":")[1]) for x in s.split(",")}
        r = check(f, sig)
        r["sigma_arg"] = s
        out["checks"].append(r)
        print(json.dumps({k: r.get(k) for k in ("sigma_arg", "bijection", "unmapped_count", "clauses",
                                                "clause_multiset_invariant", "cube_vars_ok", "automorphism")}),
              flush=True)
    out["all_automorphisms"] = out["base_sha_matches"] and all(r.get("automorphism") for r in out["checks"])
    with open(a.out, "x") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({"base_sha_matches": out["base_sha_matches"], "all_automorphisms": out["all_automorphisms"]}))


if __name__ == "__main__":
    main()
