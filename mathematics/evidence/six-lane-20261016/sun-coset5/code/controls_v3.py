#!/usr/bin/env python3
"""controls_v3 -- re-run of controls_v2 with a cost cap (sanity controls, NOT gate evidence).

controls_v2 (52372b73...) was stopped cooperatively at 09:57 PDT. Its run (evidence/controls-v2-run1)
wrote no output, so its outcome is UNKNOWN. The likely cause, inferred and not established, is
rule FH1 being applied to random realisable families with an index-a subgroup for large a: the
fibre enumeration over a cosets is exponential in a.
This version imports controls_v2 unchanged (demos, lemma_R_check) and applies FH1 to a random
family only if every H1 triangle has a <= 6. Every family that skips FH1 is counted.
Usage: python3 controls_v3.py OUTDIR
"""
import hashlib
import importlib.util
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("c2", os.path.join(HERE, "controls_v2.py"))
c2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c2)
eng = c2.eng


def random_configs(seed=20261018, per_group=60):
    rnd = random.Random(seed)
    c = eng.perm_from_cycles
    groups = {
        "S4": (eng.closure([c(4, [(1, 2)]), c(4, [(1, 2, 3, 4)])], 4), 4),
        "S5": (eng.closure([c(5, [(1, 2)]), c(5, [(1, 2, 3, 4, 5)])], 5), 5),
        "A5": (eng.closure([c(5, [(1, 2, 3)]), c(5, [(1, 2, 3, 4, 5)])], 5), 5),
        "C2xS4": (eng.closure([c(6, [(1, 2)]), c(6, [(3, 4)]), c(6, [(3, 4, 5, 6)])], 6), 6),
        "S3xS3": (eng.closure([c(6, [(1, 2)]), c(6, [(1, 2, 3)]), c(6, [(4, 5)]), c(6, [(4, 5, 6)])], 6), 6),
        "D12": (eng.closure([c(6, [(1, 2, 3, 4, 5, 6)]), c(6, [(2, 6), (3, 5)])], 6), 6),
        "C4xC2xC3": (eng.closure([c(9, [(1, 2, 3, 4)]), c(9, [(5, 6)]), c(9, [(7, 8, 9)])], 9), 9),
    }
    res = {"seed": seed, "families": 0, "fh1_applied": 0, "fh1_skipped_large_m": 0, "engine_kills": [],
           "lemma_violations": [], "lemmaR_violations": [], "by_group": {}, "index_tuples_sample": []}
    rules_small = (("T", eng.rule_T), ("K", eng.rule_K), ("P", eng.rule_P), ("FH1", eng.rule_FH1))
    rules_nofh = (("T", eng.rule_T), ("K", eng.rule_K), ("P", eng.rule_P))
    for name in sorted(groups):
        G, N = groups[name]
        Gl = sorted(G)
        subsl, seen = [], set()
        for _ in range(400):
            gens = [rnd.choice(Gl) for _ in range(rnd.choice((1, 2)))]
            H = eng.closure(gens, N)
            if len(H) < len(G) and H not in seen:
                seen.add(H)
                subsl.append(H)
        subsl.sort(key=lambda H: (len(H), sorted(H)))
        made = tries = 0
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
                res["lemma_violations"].append({"group": name, "v": "not disjoint"})
                continue
            made += 1
            res["families"] += 1
            if len(res["index_tuples_sample"]) < 40:
                res["index_tuples_sample"].append([name, facts["n"]])
            if all(a <= 6 for _, a in eng.h1_triangles(p)):
                res["fh1_applied"] += 1
                w = eng.classify(p, rules_small)
            else:
                res["fh1_skipped_large_m"] += 1
                w = eng.classify(p, rules_nofh)
            if w is not None:
                res["engine_kills"].append({"group": name, "n": facts["n"], "alpha": facts["alpha"], "w": [str(x) for x in w]})
            if facts["lemma_violations_on_actual_data"]:
                res["lemma_violations"].append({"group": name, "n": facts["n"], "v": [str(x) for x in facts["lemma_violations_on_actual_data"]]})
            rv = c2.lemma_R_check(G, subs, reps)
            if rv:
                res["lemmaR_violations"].append({"group": name, "n": facts["n"], "v": [str(x) for x in rv]})
        res["by_group"][name] = {"order": len(G), "subgroups_sampled": len(subsl), "families": made}
    return res


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=False)
    t0 = time.time()
    shas = {}
    for fn in ("controls_v3.py", "controls_v2.py", "core5_engine_v1.py", "core5_check_v2.py"):
        with open(os.path.join(HERE, fn), "rb") as f:
            shas[fn] = hashlib.sha256(f.read()).hexdigest()
    res = {"sha256": shas, "python": sys.version, "demos": c2.demos()}
    t1 = time.time()
    res["random_realisable"] = random_configs()
    res["seconds_demos"] = round(t1 - t0, 1)
    res["seconds_total"] = round(time.time() - t0, 1)
    with open(os.path.join(out, "controls_v3.json"), "x") as f:
        json.dump(res, f, indent=1)
    rr = res["random_realisable"]
    print(json.dumps({"families": rr["families"], "fh1_applied": rr["fh1_applied"], "fh1_skipped": rr["fh1_skipped_large_m"],
                      "engine_kills": len(rr["engine_kills"]), "lemma_violations": len(rr["lemma_violations"]),
                      "lemmaR_violations": len(rr["lemmaR_violations"]),
                      "demos": [(d["label"], d["certificate_still_fires_on_mutant"]) for d in res["demos"]],
                      "seconds": res["seconds_total"]}))


if __name__ == "__main__":
    main()
