#!/usr/bin/env python3
"""controls_v2 -- extra controls for the frozen engine (sanity controls, NOT gate evidence).

(A) Targeted mutation demos. Each demo picks a Core(5) pattern whose FIRST firing rule is the
    rule under test, changes one label of that pattern's certificate, and records whether the
    certificate still fires. The intended reason is stated in each demo.
(B) Random realisable configurations in small permutation groups (fixed seed). For each one:
    the engine (rules T, K, P, FH1 on exact data) must not kill it; lemma predictions are
    checked on the exact data (rules-v1 L0.3, L1, L3, L4); proof-v1 Lemma R is checked on
    the exact data (R1, R2, and R5 on every overlap).
Usage: python3 controls_v2.py OUTDIR
"""
import hashlib
import importlib.util
import itertools
import json
import os
import random
import sys
import time
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("eng", os.path.join(HERE, "core5_engine_v1.py"))
eng = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)
spec2 = importlib.util.spec_from_file_location("chk", os.path.join(HERE, "core5_check_v2.py"))
chk = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(chk)

E5 = eng.edges(5)
EI = {e: t for t, e in enumerate(E5)}


def chk_first(al, e2, e3):
    p = chk.Pat(al, e2, e3)
    for f in chk.RULES:
        w = f(p)
        if w is not None:
            return w
    return None


def chk_fires(al, e2, e3, w):
    """Re-check one checker-v2 witness on (al,e2,e3)."""
    p = chk.Pat(al, e2, e3)
    kind = w[0]
    if kind == "T":
        x, y, z = w[1]
        a, b, c = p.A[x][y], p.A[x][z], p.A[y][z]
        return p.tm[tuple(w[1])] > min(a * b, a * c, b * c)
    if kind == "K":
        v, S = w[1], w[2]
        return sum(p.A[i][v] for i in S) >= 4 and all(chk.linked(p, v, i, j) for i, j in itertools.combinations(S, 2))
    if kind in ("PB", "Ppair"):
        r = chk.r_P(p)
        return r is not None and r[0] == kind and r[1] == w[1] and tuple(r[2]) == tuple(w[2])
    if kind == "N2":
        return chk.r_N2(p) is not None
    if kind == "FH2":
        r = chk.r_FH2(p)
        return r is not None and tuple(r[1]) == tuple(w[1])
    if kind == "RSD":
        v, ww = w[1], w[2]
        J = [j for j in range(5) if j not in (v, ww)]
        return p.A[v][ww] == 1 and all(p.A[v][j] == 3 for j in J) and all(
            p.taumin(v, ww, j) >= p.A[v][ww] * p.A[ww][j] for j in J)
    raise ValueError(kind)


def demos():
    out = []
    al_all = list(itertools.product((1, 2, 3), repeat=10))
    specials = [(e2, e3) for e2 in (None, 0, 1, 2, 3, 4) for e3 in (None, 0, 1, 2, 3, 4)]

    def find(pred):
        for al in al_all:
            for e2, e3 in specials:
                w = chk_first(al, e2, e3)
                if w is not None and pred(al, e2, e3, w):
                    return al, e2, e3, w
        return None

    def record(label, reason, found, mut):
        al, e2, e3, w = found
        al2, e22, e32 = mut(list(al), e2, e3)
        out.append({"label": label, "intended_reason": reason,
                    "pattern": ["".join(map(str, al)), e2, e3], "first_certificate": [str(x) for x in w],
                    "mutant": ["".join(map(str, al2)), e22, e32],
                    "certificate_still_fires_on_mutant": chk_fires(tuple(al2), e22, e32, w),
                    "mutant_first_certificate": [str(x) for x in (chk_first(tuple(al2), e22, e32) or ["SURVIVE"])]})

    # (a) T on a (1,1,2) triangle: making the shared vertex even must break it
    f = find(lambda al, e2, e3, w: w[0] == "T" and sorted([al[EI[(w[1][0], w[1][1])]], al[EI[(w[1][0], w[1][2])]], al[EI[(w[1][1], w[1][2])]]]) == [1, 1, 2] and e2 is None)
    if f:
        x, y, z = f[3][1]
        A = {(x, y): f[0][EI[(x, y)]], (x, z): f[0][EI[(x, z)]], (y, z): f[0][EI[(y, z)]]}
        shared = [v for v in (x, y, z) if all(A[e] == 1 for e in A if v in e)][0]
        record("T_(1,1,2)", "alpha_2-edge | r_shared tau; making the shared vertex even lowers tau_min to 1 <= tau_max",
               f, lambda al, e2, e3: (al, shared, e3))
    # (b) K with |S|=2 on a (1,3,3) triangle: lowering the 3-edge at v to 2 makes the sum 3
    def pk(al, e2, e3, w):
        if w[0] != "K" or len(w[2]) != 2:
            return False
        v, (i, j) = w[1], w[2]
        vals = sorted([al[EI[tuple(sorted((v, i)))]], al[EI[tuple(sorted((v, j)))]]])
        return vals == [1, 3]
    f = find(pk)
    if f:
        v, (i, j) = f[3][1], f[3][2]
        e3edge = tuple(sorted((v, i))) if f[0][EI[tuple(sorted((v, i)))]] == 3 else tuple(sorted((v, j)))
        def mut(al, e2, e3, e3edge=e3edge):
            al[EI[e3edge]] = 2
            return al, e2, e3
        record("K_(1,3)_pair", "L3 needs sum alpha_iv >= 4 for a contradiction; 1+2 = 3 is allowed", f, mut)
    # (c) P-Bonferroni: making the vertex special for alpha_jk refines the granularity and breaks it
    f = find(lambda al, e2, e3, w: w[0] == "PB" and e2 is None and e3 is None)
    if f:
        v = f[3][1]
        record("PB_granularity", "u = |G|/(4 gcd(r_v, alpha_jk)); making v the 3-vertex refines u to |G|/12, so the Bonferroni bound weakens",
               f, lambda al, e2, e3: (al, e2, v))
    # (d) N2: changing one alpha removes the hypothesis
    al = [2] * 10
    record("N2", "the hypothesis is that all ten alpha equal 2", (tuple(al), None, None, ("N2",)),
           lambda al, e2, e3: ([1] + al[1:], e2, e3))
    # (e) FH2 on S-B: removing the alpha=1 edge removes H2
    al = [2] * 10
    al[EI[(0, 1)]] = 1
    w = chk_first(tuple(al), None, None)
    def mut_e(al, e2, e3):
        al = list(al)
        al[EI[(0, 1)]] = 2
        return al, e2, e3
    record("FH2_S-B", "H2 needs alpha_ab = 1", (tuple(al), None, None, w), mut_e)
    # (f) RSD on S-D: changing alpha_23 from 3 to 2 breaks the star (1,3,3,3) at v=2
    al = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
    w = chk_first(tuple(al), 1, 0)
    def mut_f(al, e2, e3):
        al = list(al)
        al[EI[(2, 3)]] = 2
        return al, e2, e3
    record("RSD_S-D", "Lemma R at v=2 needs alpha_2j = 3 for the three j != 0", (tuple(al), 1, 0, w), mut_f)
    return out


def lemma_R_check(G, subs, reps):
    """Check proof-v1 Lemma R on exact data: for each v, the D_j (with g_v moved to 1)."""
    k = len(subs)
    order = len(G)
    viol = []
    for v in range(k):
        gv = reps[v]
        gvi = tuple(sorted(range(len(gv)), key=lambda x: gv[x]))  # inverse permutation
        Uv = subs[v]
        D = {}
        for j in range(k):
            if j == v:
                continue
            gj = eng.pmul(gvi, reps[j])
            Dj = frozenset(eng.pmul(eng.pmul(a, gj), b) for a in Uv for b in subs[j])
            UvUj = eng.setprod(Uv, subs[j])
            if Dj & UvUj:
                viol.append(("R1", v, j))
            g = gcd(order // len(Uv), order // len(subs[j]))
            if len(Dj) % (order // g):
                viol.append(("R2", v, j))
            D[j] = (Dj, len(Dj) // len(subs[j]))
        for j, l in itertools.combinations(sorted(D), 2):
            if D[j][0] & D[l][0] and gcd(D[j][1], D[l][1]) < 2:
                viol.append(("R5", v, j, l))
    return viol


def random_configs(seed=20261018, per_group=60):
    rnd = random.Random(seed)
    c = eng.perm_from_cycles
    groups = {}
    S4 = eng.closure([c(4, [(1, 2)]), c(4, [(1, 2, 3, 4)])], 4)
    groups["S4"] = (S4, 4)
    groups["S5"] = (eng.closure([c(5, [(1, 2)]), c(5, [(1, 2, 3, 4, 5)])], 5), 5)
    groups["A5"] = (eng.closure([c(5, [(1, 2, 3)]), c(5, [(1, 2, 3, 4, 5)])], 5), 5)
    groups["C2xS4"] = (eng.closure([c(6, [(1, 2)]), c(6, [(3, 4)]), c(6, [(3, 4, 5, 6)])], 6), 6)
    groups["S3xS3"] = (eng.closure([c(6, [(1, 2)]), c(6, [(1, 2, 3)]), c(6, [(4, 5)]), c(6, [(4, 5, 6)])], 6), 6)
    groups["D12"] = (eng.closure([c(6, [(1, 2, 3, 4, 5, 6)]), c(6, [(2, 6), (3, 5)])], 6), 6)
    groups["C4xC2xC3"] = (eng.closure([c(9, [(1, 2, 3, 4)]), c(9, [(5, 6)]), c(9, [(7, 8, 9)])], 9), 9)
    res = {"seed": seed, "families": 0, "engine_kills": [], "lemma_violations": [], "lemmaR_violations": [],
           "by_group": {}}
    for name in sorted(groups):
        G, N = groups[name]
        Gl = sorted(G)
        subsl = []
        seen = set()
        for _ in range(400):
            gens = [rnd.choice(Gl) for _ in range(rnd.choice((1, 2)))]
            H = eng.closure(gens, N)
            if len(H) < len(G) and H not in seen:
                seen.add(H)
                subsl.append(H)
        subsl.sort(key=lambda H: (len(H), sorted(H)))
        made = 0
        tries = 0
        while made < per_group and tries < 20000:
            tries += 1
            size = rnd.choice((3, 4, 5))
            fam = []
            for _ in range(200):
                H = rnd.choice(subsl)
                g = rnd.choice(Gl)
                cs = frozenset(eng.pmul(g, u) for u in H)
                if all(not (cs & frozenset(eng.pmul(g2, u) for u in H2)) for H2, g2 in fam):
                    fam.append((H, g))
                    if len(fam) == size:
                        break
            if len(fam) < 3:
                continue
            subs = [H for H, g in fam]
            reps = [g for H, g in fam]
            p, facts = eng.realised_pattern(G, subs, reps)
            if not facts["disjoint"]:
                res["lemma_violations"].append((name, "not disjoint"))
                continue
            made += 1
            res["families"] += 1
            w = eng.classify(p, (("T", eng.rule_T), ("K", eng.rule_K), ("P", eng.rule_P), ("FH1", eng.rule_FH1)))
            if w is not None:
                res["engine_kills"].append({"group": name, "n": facts["n"], "alpha": facts["alpha"], "w": [str(x) for x in w]})
            if facts["lemma_violations_on_actual_data"]:
                res["lemma_violations"].append({"group": name, "n": facts["n"], "v": [str(x) for x in facts["lemma_violations_on_actual_data"]]})
            rv = lemma_R_check(G, subs, reps)
            if rv:
                res["lemmaR_violations"].append({"group": name, "n": facts["n"], "v": [str(x) for x in rv]})
        res["by_group"][name] = {"order": len(G), "subgroups_sampled": len(subsl), "families": made}
    return res


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=False)
    t0 = time.time()
    shas = {}
    for fn in ("controls_v2.py", "core5_engine_v1.py", "core5_check_v2.py"):
        with open(os.path.join(HERE, fn), "rb") as f:
            shas[fn] = hashlib.sha256(f.read()).hexdigest()
    res = {"sha256": shas, "python": sys.version, "demos": demos(), "random_realisable": random_configs()}
    res["seconds"] = round(time.time() - t0, 1)
    with open(os.path.join(out, "controls_v2.json"), "x") as f:
        json.dump(res, f, indent=1)
    rr = res["random_realisable"]
    print(json.dumps({"families": rr["families"], "engine_kills": len(rr["engine_kills"]),
                      "lemma_violations": len(rr["lemma_violations"]), "lemmaR_violations": len(rr["lemmaR_violations"]),
                      "demos": [(d["label"], d["certificate_still_fires_on_mutant"]) for d in res["demos"]],
                      "seconds": res["seconds"]}))


if __name__ == "__main__":
    main()
