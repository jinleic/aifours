#!/usr/bin/env python3
"""pattern_check.py: independent stdlib evaluation of the pattern families F1-F4 (review/LEMMAS.md) on exact
supports, for nets of any order. Lane moqls7-maximum. Controls:
  C1 genuine non-classical: Psi(f) of Ball-Simoens Theorem 6 / Example 15 at q = 7, H = {1,2,4}, on the 3-net
     (rows, columns, symbol lines of Phi(m)) for each undetermined direction m != 0; frame = row 0 after the Fourier
     change of basis. Exact supports: y in supp(psi'_ij) iff x -> i f(x) + (j - y) x is not a permutation of F_7
     (a sum of 7 seventh roots of unity vanishes iff each root occurs once).
  C2 genuine non-classical: the 4 x 4 QLS printed in Ball-Simoens section 2.4 (2-net, frame row 0).
  C3 every model enumerated by encoders A and B (evidence/k1A, evidence/k1B) on the 7 nets.
  C4 mutations of C1, C2 and of the K1 weight-4 model: add or remove one coordinate at one point (all single
     mutations); report how many are rejected.
Usage: /usr/bin/python3 pattern_check.py CLASSFILE K1A_SUMMARY K1B_SUMMARY OUT.json
"""
import itertools
import json
import sys


def check(lines, supp, frame_basis, allowed=None):
    """Return list of violated families. lines: list of point lists; supp: point -> set; frame_basis: frame point ->
    coordinate (its support must be exactly that singleton); allowed: optional point -> set."""
    bad = set()
    for p, k in frame_basis.items():
        if supp[p] != {k}:
            bad.add("frame")
    for p, S in supp.items():
        if not S:
            bad.add("F1")
        if allowed is not None and not S <= allowed[p]:
            bad.add("allowed")
    n = len(frame_basis)
    for l in lines:
        for p, q in itertools.combinations(l, 2):
            if len(supp[p] & supp[q]) == 1:
                bad.add("F2")
        for k in range(n):
            cov = [p for p in l if k in supp[p]]
            if not cov:
                bad.add("F3")
            if len(cov) == 1 and len(supp[cov[0]]) != 1:
                bad.add("F4")
    return sorted(bad)


def net_lines(net):
    k = len(net[0])
    out = []
    for c in range(k):
        for b in sorted({q[c] for q in net}):
            out.append([p for p in range(len(net)) if net[p][c] == b])
    return out


def allowed_sets(net, frame, label):
    A = {}
    for p in range(len(net)):
        if p in label:
            A[p] = {label[p]}
            continue
        forb = {label[q] for c in range(1, len(net[0])) for q in frame if net[q][c] == net[p][c]}
        A[p] = set(range(len(frame))) - forb
    return A


def mutations(supp, frame_basis, n):
    for p in supp:
        if p in frame_basis:
            continue
        for k in range(n):
            T = dict(supp)
            T[p] = set(supp[p]) ^ {k}
            yield (p, k), T


def control_psi_f():
    P = 7
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(P)]
    is_perm = lambda g: len({g(x) % P for x in range(P)}) == P
    M0 = [m for m in range(P) if is_perm(lambda x: f0[x] - m * x)]
    res = []
    # proof of Theorem 6: replace f by f - m0 x (m0 in M0) so that f is a permutation and 0 lies in M = M0 - m0
    for m0 in M0:
        f = [(f0[x] - m0 * x) % P for x in range(P)]
        assert is_perm(lambda x: f[x])
        M = [(m - m0) % P for m in M0]
        for m in [m for m in M if m != 0]:
            assert is_perm(lambda x: f[x] - m * x)
            net = [(i, j, (m * i + j) % P) for i in range(P) for j in range(P)]      # point index 7i+j
            supp = {}
            for i in range(P):
                for j in range(P):
                    supp[P * i + j] = {y for y in range(P) if not is_perm(lambda x: i * f[x] + (j - y) * x)}
            label = {j: j for j in range(P)}
            A = allowed_sets(net, list(range(P)), label)
            lines = net_lines(net)
            v = check(lines, supp, label, A)
            weights = sorted({len(s) for s in supp.values()})
            muts = list(mutations(supp, label, P))
            rej = sum(1 for _, T in muts if check(lines, T, label, A))
            res.append({"m0": m0, "f": f, "m": m, "M_shifted": M, "violations": v, "weights": weights,
                        "mutations": len(muts), "mutations_rejected": rej})
    return res


def control_4x4():
    h = None
    # entries as supports in 0-indexed basis (from the printed square, |1>..|4> -> 0..3)
    S = [[{0}, {1}, {2}, {3}],
         [{1}, {0}, {3}, {2}],
         [{2}, {3}, {0, 1}, {0, 1}],
         [{3}, {2}, {0, 1}, {0, 1}]]
    net = [(i, j) for i in range(4) for j in range(4)]
    supp = {4 * i + j: S[i][j] for i in range(4) for j in range(4)}
    label = {j: j for j in range(4)}
    lines = net_lines(net)
    v = check(lines, supp, label)
    muts = list(mutations(supp, label, 4))
    rej = sum(1 for _, T in muts if check(lines, T, label))
    return {"violations": v, "mutations": len(muts), "mutations_rejected": rej}


def models_to_supp(model, fmt):
    supp = {}
    for s in model:
        p, rest = s.split(":")
        if fmt == "A":
            supp.setdefault(int(p), set()).add(int(rest))
        else:
            supp[int(p)] = {int(c) for c in rest}
    return supp


def main(classfile, sa, sb, out):
    data = json.load(open(classfile))
    A = json.load(open(sa))
    B = json.load(open(sb))
    res = {"C1_psi_f": control_psi_f(), "C2_4x4": control_4x4(), "C3_models": [], "C4_weight4_mutations": None}
    for idx, cls in enumerate(data["classes"]):
        net = [tuple(q) for q in cls["net"]]
        frame = [p for p in range(49) if net[p][0] == 0]
        label = {p: net[p][1] for p in frame}
        Al = allowed_sets(net, frame, label)
        lines = net_lines(net)
        for fmt, summ in (("A", A), ("B", B)):
            for mdl in summ["classes"][idx]["models"]:
                supp = models_to_supp(mdl, fmt)
                res["C3_models"].append({"class": idx, "encoder": fmt, "violations": check(lines, supp, label, Al),
                                         "weights": sorted({len(s) for s in supp.values()})})
        if idx == 6:
            w4 = [m for m, w in zip(A["classes"][6]["models"], A["classes"][6]["model_weight_sets"]) if w != [1]][0]
            supp = models_to_supp(w4, "A")
            muts = list(mutations(supp, label, 7))
            rej = sum(1 for _, T in muts if check(lines, T, label, Al))
            res["C4_weight4_mutations"] = {"mutations": len(muts), "rejected": rej}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({"C1": [(r["m0"], r["m"], r["violations"], r["weights"], r["mutations_rejected"], r["mutations"])
                             for r in res["C1_psi_f"]],
                      "C2": res["C2_4x4"],
                      "C3_all_pass": all(not r["violations"] for r in res["C3_models"]),
                      "C3_count": len(res["C3_models"]), "C4": res["C4_weight4_mutations"]}))


if __name__ == "__main__":
    main(*sys.argv[1:5])
