#!/usr/bin/env python3
"""Mutation / positive controls for the three LKTS checkers on a certificate.

Writes every mutated certificate to OUTDIR (retained fixtures), runs
  A = code/check_lkts57.py (lane, Python), B = prior dossier work/check_lkts.py
  (read-only), C = code/bin/check_lkts57_c (lane, C)
and records verdicts in OUTDIR/mutation-results.json.  Seeds fixed.
"""
import hashlib
import json
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PRIOR = "/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/work/check_lkts.py"


def parse(path):
    v, systems = None, []
    for raw in open(path):
        line = raw.split("#")[0].strip()
        if not line:
            continue
        t = line.split()
        if t[0] == "LKTS":
            v = int(t[1])
        elif t[0] == "KTS":
            systems.append([])
        elif t[0] == "CLASS":
            systems[-1].append([])
        else:
            systems[-1][-1].append(tuple(int(x) for x in t))
    return v, systems


def dump(v, systems, path, header=None):
    lines = []
    if header:
        lines.append(f"# {header}")
    lines.append(f"LKTS {v}")
    for k, S in enumerate(systems):
        lines.append(f"KTS {k}")
        for c, C in enumerate(S):
            lines.append(f"CLASS {c}")
            lines.extend(f"{a} {b} {d}" for a, b, d in C)
    open(path, "w").write("\n".join(lines) + "\n")


def deep(systems):
    return [[list(C) for C in S] for S in systems]


def run_checkers(path):
    out = {}
    a = subprocess.run([sys.executable, os.path.join(HERE, "check_lkts57.py"), path], capture_output=True, text=True)
    out["A_lane_py"] = "PASS" if a.returncode == 0 else "FAIL"
    b = subprocess.run([sys.executable, PRIOR, path], capture_output=True, text=True)
    try:
        out["B_prior_py"] = json.loads(b.stdout).get("verdict", "FAIL")
    except Exception:
        out["B_prior_py"] = "FAIL"
    c = subprocess.run([os.path.join(HERE, "bin", "check_lkts57_c"), path], capture_output=True, text=True)
    out["C_lane_c"] = "PASS" if c.returncode == 0 and c.stdout.startswith("PASS") else "FAIL"
    return out


def main():
    cert, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    v, base = parse(cert)
    rng = random.Random(20261016)
    cases = []

    def case(name, systems, expect, vv=None):
        p = os.path.join(outdir, f"{name}.txt")
        dump(vv if vv is not None else v, systems, p, header=f"mutation control {name}; expected {expect}")
        res = run_checkers(p)
        cases.append({"case": name, "expect": expect, "sha256": hashlib.sha256(open(p, "rb").read()).hexdigest(), **res})

    # positive controls
    perm = list(range(v)); rng.shuffle(perm)
    case("pos_relabel_points", [[[tuple(sorted(perm[x] for x in b)) for b in C] for C in S] for S in base], "PASS")
    s = deep(base); rng.shuffle(s)
    for S in s:
        rng.shuffle(S)
        for C in S:
            rng.shuffle(C)
    case("pos_shuffle_order", s, "PASS")
    # negative controls
    s = deep(base); C = s[3][5]; b0, b1 = list(C[0]), list(C[1]); b0[0], b1[0] = b1[0], b0[0]
    C[0], C[1] = tuple(b0), tuple(b1); case("neg_swap_points_within_class", s, "FAIL")
    s = deep(base); b = list(s[10][2][4]); b[2] = (b[2] + 1) % v if (b[2] + 1) % v not in b else (b[2] + 2) % v
    s[10][2][4] = tuple(b); case("neg_change_one_point", s, "FAIL")
    s = deep(base); s[0][0][0], s[1][0][0] = s[1][0][0], s[0][0][0]; case("neg_swap_blocks_between_systems", s, "FAIL")
    s = deep(base); del s[7][13]; case("neg_delete_class", s, "FAIL")
    s = deep(base); del s[54]; case("neg_delete_system", s, "FAIL")
    s = deep(base); s[2][0], s[5][0] = s[5][0], s[2][0]; case("neg_swap_classes_between_systems", s, "FAIL")
    case("neg_wrong_header_v63", deep(base), "FAIL", vv=63)
    s = deep(base); s[1] = deep([s[0]])[0]; case("neg_duplicate_system", s, "FAIL")
    s = deep(base); relab = list(range(v)); relab[0], relab[1] = 1, 0
    s[20] = [[tuple(sorted(relab[x] for x in b)) for b in C] for C in s[20]]; case("neg_relabel_one_system", s, "FAIL")
    s = deep(base); s[30][0][0], s[30][1][0] = s[30][1][0], s[30][0][0]; case("neg_swap_blocks_between_classes", s, "FAIL")
    s = deep(base); s[44][27].append(s[44][27][0]); case("neg_repeat_block_in_class", s, "FAIL")
    s = deep(base); s[12][3] = s[12][3][:-1]; case("neg_drop_block", s, "FAIL")
    s = deep(base); b = s[9][9][9]; s[9][9][9] = (b[0], b[0], b[2]); case("neg_degenerate_triple", s, "FAIL")
    s = deep(base); b = s[16][1][1]; s[16][1][1] = (b[0], b[1], v); case("neg_point_out_of_range", s, "FAIL")
    ok = all(c[k] == c["expect"] for c in cases for k in ("A_lane_py", "B_prior_py", "C_lane_c"))
    rec = {"certificate": cert, "certificate_sha256": hashlib.sha256(open(cert, "rb").read()).hexdigest(),
           "seed": 20261016, "all_as_expected": ok, "cases": cases}
    json.dump(rec, open(os.path.join(outdir, "mutation-results.json"), "w"), indent=1)
    for c in cases:
        print(c["case"], c["expect"], c["A_lane_py"], c["B_prior_py"], c["C_lane_c"])
    print("ALL AS EXPECTED" if ok else "UNEXPECTED RESULT PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
