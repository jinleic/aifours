#!/usr/bin/env python3
"""control64.py -- general-semantics positive control (README 1.5) on the published point-cyclic 2-(64,4,1)
resolution of Topalova-Zhelezova 2026 (PDF pp.6-7; type T1, class orbits 1, 4, 16).

Machine-parses the text layer `sources/tz2026-axioms-15-00762.layout.txt` (pdftotext -layout of
`../point-cyclic88/sources/axioms-15-00762.pdf`, SHA-256 d5170670...9608): the base blocks and the printed classes
P1, P2, P3 (points 1..64; only brace-delimited 4-sets are read, the cycle notation in parentheses is skipped).
Points are shifted to Z_64 (x - 1). Classes: P1; P2 + t (0 <= t < 4); P3 + t (0 <= t < 16), as stated in the source
(orbit lengths 1, 4, 16). Consistency: the union of all class blocks must equal the development of the printed base
blocks. Writes a strict certificate (own writer, no code shared with pc_expand.py) and runs pc_check.py on it.
Usage: control64.py OUTDIR
"""
import json
import os
import re
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT = os.path.join(LANE, "sources", "tz2026-axioms-15-00762.layout.txt")


def sets_in(region):
    return [tuple(sorted(int(x) - 1 for x in re.split(r",\s*", s))) for s in re.findall(r"\{([\d,\s]+)\}", region)]


def main(argv):
    out = argv[1]
    os.makedirs(out, exist_ok=True)
    text = open(TXT, encoding="utf-8").read()
    i0 = text.index("These are the design base blocks")
    i1 = text.index("The fixed parallel class P1")
    i2 = text.index("The parallel class P2 from")
    i3 = text.index("The parallel class P3 from")
    i4 = text.index("4. Construction Method")
    base, P1, P2, P3 = sets_in(text[i0:i1]), sets_in(text[i1:i2]), sets_in(text[i2:i3]), sets_in(text[i3:i4])
    v = 64
    shape = [len(base), len(P1), len(P2), len(P3)]

    def tr(B, d):
        return tuple(sorted((x + d) % v for x in B))

    classes = [sorted(P1)] + [sorted(tr(B, t) for B in P2) for t in range(4)] + \
              [sorted(tr(B, t) for B in P3) for t in range(16)]
    dev = {tr(B, t) for B in base for t in range(v)}
    union = {B for P in classes for B in P}
    consistent = union == dev
    classes.sort()
    lines = [f"POINT-CYCLIC-RESOLUTION {v} 4 {len(classes)} 16"]
    for c, P in enumerate(classes):
        lines += [f"{c} {B[0]} {B[1]} {B[2]} {B[3]}" for B in P]
    cert = os.path.join(out, "tz64.cert")
    with open(cert, "w") as f:
        f.write("\n".join(lines) + "\n")
    p = subprocess.run([sys.executable, os.path.join(LANE, "code", "pc_check.py"), cert,
                        "--json", os.path.join(out, "tz64-check.json")], capture_output=True, text=True)
    verdict = p.stdout.strip().split("\n")[-1]
    orbits = [l for l in p.stdout.split("\n") if l.startswith(("class_orbits", "type"))]
    ok = shape == [6, 16, 16, 16] and consistent and p.returncode == 0 and verdict == "PASS"
    rep = {"source_text": TXT, "parsed_counts(base,P1,P2,P3)": shape, "base_blocks_z64": base,
           "classes_equal_development_of_base_blocks": consistent, "check": verdict, "orbit_info": orbits,
           "all_ok": ok}
    with open(os.path.join(out, "control64-report.json"), "w") as f:
        json.dump(rep, f, indent=1)
        f.write("\n")
    print(f"parsed {shape}; classes == development of base blocks: {consistent}; check: {verdict}")
    print("\n".join(orbits))
    print("CONTROL64", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
