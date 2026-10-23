#!/usr/bin/env python3
"""control52.py -- positive control on the six published point-cyclic 2-(52,4,1) resolutions (README 1.5).

1. Machine-parses Appendix A of Lam-Miao-Mishima 2001 (preprint text layer `sources/lmm2001-preprint.layout.txt`,
   produced by `pdftotext -layout` from `sources/lmm2001-preprint-a0801799.pdf`): for each design number, the five
   base blocks in Z_4 x Z_13 (short block, three blocks developed under (i,0), one transversal block).
2. Maps them to Z_52 by CRT (x = i mod 4, x = j mod 13; LMM's automorphism (i,j) -> (i,j)+(1,1) becomes x -> x+1),
   writes PC-T2-SEED files (H = the published short block), expands them with code/pc_expand.py and checks the
   certificates with code/pc_check.py. All six must PASS (type T2, class orbits 13, 4).
3. For every R1-found v = 52 seed given on the command line: expands it and tests whether an affine map
   x -> u x + t (u a unit mod 52) maps its design onto one of the six published designs, and its classes onto the
   published classes (consistency check of the whole search pipeline).
Usage: control52.py OUTDIR [found52.seed ...]
"""
import json
import os
import re
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
TXT = os.path.join(LANE, "sources", "lmm2001-preprint.layout.txt")


def crt52(i, j):
    for x in range(52):
        if x % 4 == i and x % 13 == j:
            return x
    raise ValueError


def parse_appendix():
    text = open(TXT, encoding="utf-8").read()
    app = text[text.index("Appendix A:"):]
    designs = []
    cur = None
    for line in app.split("\n"):
        m = re.search(r"No\.(\d+)", line)
        if m:
            cur = {"no": int(m.group(1)), "blocks": [], "lines": []}
            designs.append(cur)
            continue
        if cur is not None and "{" in line:
            body = re.search(r"\{([^}]*)\}", line).group(1)
            pairs = [(int(a), int(b)) for a, b in re.findall(r"\((\d+),\s*(\d+)\)", body)]
            mod = re.search(r"mod \((.*?)\)", line).group(1)
            cur["blocks"].append(pairs)
            cur["lines"].append(line.strip())
            cur.setdefault("mods", []).append(mod)
    return designs


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout


def read_cert(path):
    lines = open(path).read().rstrip("\n").split("\n")[1:]
    classes = {}
    for line in lines:
        t = list(map(int, line.split()))
        classes.setdefault(t[0], []).append(tuple(t[1:]))
    return [frozenset(P) for P in classes.values()]


def main(argv):
    if len(argv) < 2:
        print("usage: control52.py OUTDIR [found52.seed ...]", file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out, exist_ok=True)
    designs = parse_appendix()
    report = {"source_text": TXT, "designs": [], "found": []}
    ok = True
    pub = {}
    if [d["no"] for d in designs] != [125, 132, 163, 164, 167, 168]:
        print("unexpected design list", [d["no"] for d in designs])
        return 1
    for d in designs:
        bl = d["blocks"]
        good = (len(bl) == 5 and all(len(B) == 4 for B in bl) and d["mods"][0].strip().endswith("13")
                and d["mods"][0].strip() != "4, 13" and all(m.strip() == "4, 13" for m in d["mods"][1:]))
        z = [sorted(crt52(i, j) for i, j in B) for B in bl]
        seed = os.path.join(out, f"lmm52_no{d['no']}.seed")
        with open(seed, "w") as f:
            f.write("PC-T2-SEED 52\n")
            f.write("H " + " ".join(map(str, z[0])) + "\n")
            for B in z[1:4]:
                f.write("X " + " ".join(map(str, B)) + "\n")
            f.write("Y " + " ".join(map(str, z[4])) + "\n")
        cert = seed.replace(".seed", ".cert")
        rc1, o1 = run([PY, os.path.join(LANE, "code", "pc_expand.py"), seed, cert])
        rc2, o2 = run([PY, os.path.join(LANE, "code", "pc_check.py"), cert])
        verdict = o2.strip().split("\n")[-1] if o2 else "none"
        orbits = [l for l in o2.split("\n") if l.startswith("class_orbits")]
        entry = {"no": d["no"], "published_lines": d["lines"], "z52_blocks": z, "format_ok": good,
                 "expand_rc": rc1, "expand_out": o1.strip(), "check_rc": rc2, "verdict": verdict,
                 "class_orbits": orbits[0] if orbits else None}
        report["designs"].append(entry)
        print(f"No.{d['no']}: format_ok={good} expand_rc={rc1} check={verdict}")
        ok &= good and rc1 == 0 and rc2 == 0 and verdict == "PASS"
        if rc1 == 0:
            pub[d["no"]] = read_cert(cert)
    units = [u for u in range(52) if u % 2 and u % 13]
    for seed in argv[2:]:
        cert = os.path.join(out, "found_" + os.path.basename(seed).replace(".seed", ".cert"))
        rc1, _ = run([PY, os.path.join(LANE, "code", "pc_expand.py"), seed, cert])
        rc2, o2 = run([PY, os.path.join(LANE, "code", "pc_check.py"), cert])
        cl = read_cert(cert)
        blocks = frozenset(B for P in cl for B in P)
        match = None
        for no, pcl in pub.items():
            pblocks = frozenset(B for P in pcl for B in P)
            pset = set(pcl)
            for u in units:
                for t in range(52):
                    img = lambda B: tuple(sorted((u * x + t) % 52 for x in B))
                    if frozenset(img(B) for B in blocks) != pblocks:
                        continue
                    if {frozenset(img(B) for B in P) for P in cl} == pset:
                        match = {"no": no, "u": u, "t": t, "classes_match": True}
                    else:
                        match = match or {"no": no, "u": u, "t": t, "classes_match": False}
                    if match.get("classes_match"):
                        break
                if match and match.get("classes_match"):
                    break
            if match and match.get("classes_match"):
                break
        verdict = o2.strip().split("\n")[-1]
        report["found"].append({"seed": seed, "check": verdict, "affine_match": match})
        print(f"found {seed}: check={verdict} affine_match={match}")
        ok &= rc1 == 0 and rc2 == 0 and match is not None and match.get("classes_match", False)
    report["all_ok"] = bool(ok)
    with open(os.path.join(out, "control52-report.json"), "w") as f:
        json.dump(report, f, indent=1)
        f.write("\n")
    print("CONTROL52", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
