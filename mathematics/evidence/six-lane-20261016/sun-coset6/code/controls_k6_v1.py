#!/usr/bin/env python3
"""controls_k6_v1 -- controls for the k6 engines. Sanity only; they never gate anything, and they are
not evidence for the gate. Same-author code.

(C1) Reproduction. Engine v2 (hereditary rules T, K, RLP, P) is run in modes core45 and core34.
     Engine v1 already ran these modes, at 11:10. A difference from the k=5 / Prop 4.3 universes
     would be a reproduction mismatch, not a soundness signal.
(C2) Realisable families. Disjoint-coset families with indices 5r_i (the r_i pairwise coprime,
     k <= 5) are taken in Z5, A5 and S5, using a fixed random seed. The k-generic v2 rules
     T, K, RLP, P and FH5 are evaluated on the exact alpha data with the true markers. Every
     family must survive.
(C3) Selected mutations. For each certificate type of engine-v3-core56 (K, RLP, PB, FH5, N26,
     RPLP), take the first orbit carrying that type and find a single-label mutation (one alpha
     value or one marker) under which the same witness no longer verifies. Record the mutation
     and the reason.
Usage: python3 controls_k6_v1.py OUTDIR
"""
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
import random
import sys
import time
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


e2 = load("e2", "core56_engine_v2.py")
e3 = load("e3", "core56_engine_v3.py")


class KShape:
    def __init__(self, k, d=5):
        self.k, self.d = k, d


def perm_from_cycles(N, cycles):
    p = list(range(N + 1))
    for c in cycles:
        for i in range(len(c)):
            p[c[i]] = c[(i + 1) % len(c)]
    return tuple(p)


def pmul(p, q):
    return tuple(p[q[x]] for x in range(len(p)))


def closure(gens, N):
    e = tuple(range(N + 1))
    S, fr = {e}, [e]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                y = pmul(x, g)
                if y not in S:
                    S.add(y)
                    nf.append(y)
        fr = nf
    return frozenset(S)


def markers_of(rs):
    e2v, c2, e3v = None, 0, None
    for i, r in enumerate(rs):
        if r % 2 == 0:
            e2v, c2 = i, (1 if r % 4 else 2)
        if r % 3 == 0:
            e3v = i
    return (e2v, c2, e3v)


def c2_realisable(seed=20261018):
    rnd = random.Random(seed)
    groups = {}
    groups["Z5"] = (closure([perm_from_cycles(5, [(1, 2, 3, 4, 5)])], 5), 5)
    groups["A5"] = (closure([perm_from_cycles(5, [(1, 2, 3)]), perm_from_cycles(5, [(1, 2, 3, 4, 5)])], 5), 5)
    groups["S5"] = (closure([perm_from_cycles(5, [(1, 2)]), perm_from_cycles(5, [(1, 2, 3, 4, 5)])], 5), 5)
    out = {"families": 0, "killed": [], "by_group": {}}
    for name in sorted(groups):
        G, N = groups[name]
        order = len(G)
        Gl = sorted(G)
        subs, seen = [], set()
        for _ in range(600):
            H = closure([rnd.choice(Gl) for _ in range(rnd.choice((1, 2)))], N)
            idx = order // len(H)
            if idx % 5 == 0 and H not in seen:
                seen.add(H)
                subs.append(H)
        subs.sort(key=lambda H: (len(H), sorted(H)))
        made = 0
        for _ in range(4000):
            if made >= 60:
                break
            size = rnd.choice((3, 4, 5))
            fam = []
            for _ in range(300):
                H = rnd.choice(subs)
                r = (order // len(H)) // 5
                if any(gcd(r, (order // len(H2)) // 5) != 1 for H2, g2 in fam):
                    continue
                g = rnd.choice(Gl)
                cs = frozenset(pmul(g, u) for u in H)
                if all(not (cs & frozenset(pmul(g2, u) for u in H2)) for H2, g2 in fam):
                    fam.append((H, g))
                    if len(fam) == size:
                        break
            if len(fam) < 3:
                continue
            k = len(fam)
            n = [order // len(H) for H, g in fam]
            rs = [x // 5 for x in n]
            A = [[0] * k for _ in range(k)]
            for i, j in itertools.combinations(range(k), 2):
                I = order // len(fam[i][0] & fam[j][0])
                A[i][j] = A[j][i] = I // (5 * rs[i] * rs[j])
            sp = markers_of(rs)
            S = KShape(k)
            w = None
            for tri in itertools.combinations(range(k), 3):
                if e2.taumin(A, *tri, sp) > e2.taumax(A, *tri):
                    w = ("T", tri)
                    break
            for f in (e2.rule_K, e2.rule_RLP, e2.rule_P, e2.rule_FH5):
                if w is None:
                    w = f(S, A, sp)
            made += 1
            out["families"] += 1
            if w is not None:
                out["killed"].append({"group": name, "n": n, "alpha": A, "markers": sp, "w": [str(x) for x in w]})
        out["by_group"][name] = {"order": order, "subgroups_index_5r": len(subs), "families": made}
    return out


def c3_mutations(engdir):
    with gzip.open(os.path.join(engdir, "orbits.jsonl.gz"), "rt") as f:
        lines = [json.loads(x) for x in f if x.strip()]
    S = e2.Shape("core56")
    first = {}
    for L in lines:
        first.setdefault(L["rule"], L)
    demos = []

    def mat(rep):
        A = [[0] * 6 for _ in range(6)]
        for (i, j), ch in zip(S.E, rep):
            A[i][j] = A[j][i] = int(ch)
        return A

    def recheck(rule, A, sp, w):
        if rule == "K":
            v, T = w[0], w[1]
            return sum(A[i][v] for i in T) >= 5 and all(e2.taumin(A, i, v, j, sp) == A[i][v] * A[v][j] for i, j in itertools.combinations(T, 2))
        if rule == "RLP":
            v = w[0]
            oth = [x for x in range(6) if x != v]
            st = tuple(e2.status(j, sp) for j in oth)
            return all(F(e3.rlp_dual(tuple(q), st)[1]["value"]) >= 1 for q in itertools.product(*[range(1, 6 - A[v][j]) for j in oth]))
        if rule in ("PB", "Ppair"):
            r = e2.rule_P(S, A, sp)
            return r is not None and r[0] == rule and r[1] == w[0]
        if rule == "FH5":
            r = e3.rule_FH5_3(S, A, sp)
            return r is not None and list(r[1]) == list(w[0])
        if rule == "N26":
            r = e3.rule_N26(S, A, sp)
            return r is not None and r[1] == w[0]
        if rule == "RPLP":
            v = w[0]
            oth = [x for x in range(6) if x != v]
            st = tuple(e2.status(j, sp) for j in oth)
            for q in itertools.product(*[range(1, 6 - A[v][j]) for j in oth]):
                if F(e3.rlp_dual(tuple(q), st)[1]["value"]) >= 1:
                    continue
                if e3.rplp_cert_q(A, sp, v, q) is None:
                    return False
            return True
        return None
    for rule in ("K", "RLP", "PB", "FH5", "N26", "RPLP"):
        L = first.get(rule)
        if L is None:
            continue
        sp = tuple(L["type"])
        A = mat(L["rep"])
        w = L["witness"]
        base = recheck(rule, A, sp, w)
        found = None
        # single alpha mutations (keep T-consistency so the mutant is a genuine leaf), then marker mutations
        for (i, j) in S.E:
            if found:
                break
            for x in (1, 2, 3, 4):
                if x == A[i][j]:
                    continue
                B = [row[:] for row in A]
                B[i][j] = B[j][i] = x
                if any(e2.taumin(B, *t, sp) > e2.taumax(B, *t) for t in itertools.combinations(range(6), 3)):
                    continue
                if not recheck(rule, B, sp, w):
                    found = {"mutation": "alpha(%d,%d) %d->%d" % (i, j, A[i][j], x), "mutant_T_consistent": True}
                    break
        if not found:
            for msp in [(None, 0, None), (None, 0, 0), (0, 1, None), (0, 2, None), (0, 1, 0), (0, 2, 0), (0, 1, 1), (0, 2, 1)]:
                if msp == sp:
                    continue
                if any(e2.taumin(A, *t, msp) > e2.taumax(A, *t) for t in itertools.combinations(range(6), 3)):
                    continue
                if not recheck(rule, A, msp, w):
                    found = {"mutation": "markers %s -> %s" % (sp, msp), "mutant_T_consistent": True}
                    break
        demos.append({"rule": rule, "type": list(sp), "rep": L["rep"], "witness_head": str(w)[:120],
                      "witness_verifies_on_original": base, "mutation_breaking_witness": found})
    return demos


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=False)
    t0 = time.time()
    shas = {}
    for fn in ("controls_k6_v1.py", "core56_engine_v2.py", "core56_engine_v3.py"):
        with open(os.path.join(HERE, fn), "rb") as f:
            shas[fn] = hashlib.sha256(f.read()).hexdigest()
    res = {"sha256": shas, "python": sys.version, "note": "controls record observations only; they do not gate"}
    res["C2_realisable"] = c2_realisable()
    res["C3_mutations"] = c3_mutations(os.path.join(LANE, "evidence", "engine-v3-core56"))
    res["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(out, "controls_k6.json"), "x") as f:
        json.dump(res, f, indent=1, default=str)
    print(json.dumps({"families": res["C2_realisable"]["families"], "killed_realisable": len(res["C2_realisable"]["killed"]),
                      "mutations": [(d["rule"], d["witness_verifies_on_original"], bool(d["mutation_breaking_witness"])) for d in res["C3_mutations"]],
                      "seconds": res["seconds"]}))


if __name__ == "__main__":
    main()
