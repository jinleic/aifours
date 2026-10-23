#!/usr/bin/env python3
"""Write spec files and compiled DMORBIT-MODEL v2 files for every enumerated group and every H^1 twist class
(sub-lane cfr21, worker InfoCFR27Lift). Usage: make_models_c21v1.py GROUPS.jsonl H1DIR OUTDIR
OUTDIR is created (must not exist). For group line i (name g{i:02d}-o{order}) and class c of H1DIR/<name>.h1.json:
OUTDIR/<name>-t{c}.spec.json with gens [[mu, pi, t_j], ...] (class 0 = untwisted, t = 0) and OUTDIR/<name>-t{c}.model from
code/dmorbit_compile_c21v1.py. Writes OUTDIR/index.json (name, order, class, trivial, spec/model sha256).
"""
import hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.join(HERE, "dmorbit_compile_c21v1.py")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    groups, h1dir, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.mkdir(outdir)
    index = []
    for i, line in enumerate(open(groups)):
        g = json.loads(line)
        name = "g%02d-o%d" % (i, g["order"])
        h1 = json.load(open(os.path.join(h1dir, name + ".h1.json")))
        if [[x[0], x[1]] for x in h1["gens"]] != [[x[0], x[1]] for x in g["gens"]]:
            raise SystemExit("generator mismatch for " + name)
        for c, cl in enumerate(h1["classes"]):
            if (c == 0) != cl["trivial"]:
                raise SystemExit("class 0 must be the trivial class (" + name + ")")
            gens = [[x[0], x[1], t] for x, t in zip(g["gens"], cl["generator_twists"])]
            spec = {"n": g["n"], "k": g["k"], "gens": gens, "group": name, "h1_class": c,
                    "source": "groups_enum_c21v1 line %d + twist_h1_c21v1 class %d" % (i, c)}
            sp = os.path.join(outdir, "%s-t%d.spec.json" % (name, c))
            mp = os.path.join(outdir, "%s-t%d.model" % (name, c))
            with open(sp, "x") as fh:
                json.dump(spec, fh)
            r = subprocess.run(["python3", COMP, sp, mp], capture_output=True, text=True)
            if r.returncode != 0:
                raise SystemExit("compile failed for %s class %d: %s" % (name, c, r.stderr[-300:]))
            info = json.loads(r.stdout)
            if info["group_order"] != g["order"]:
                raise SystemExit("order mismatch for %s class %d" % (name, c))
            index.append({"name": "%s-t%d" % (name, c), "group": name, "order": g["order"], "class": c,
                          "trivial": cl["trivial"], "spec_sha256": sha(sp), "model_sha256": sha(mp),
                          "rep_pairs": len(info["rep_pairs"]), "twisted_elements": info["twisted_elements"]})
    with open(os.path.join(outdir, "index.json"), "x") as fh:
        json.dump(index, fh, indent=1)
    print("models %d" % len(index))


if __name__ == "__main__":
    main()
