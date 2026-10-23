#!/usr/bin/env python3
"""Intended-reason mutation controls for an RDSQS certificate (standard library only).

Every mutated certificate is written to OUTDIR (retained fixture) and checked by
code/check_rdsqs.py.  A negative case passes the control only if the checker FAILS
with the intended category prefix (COVERAGE / BLOCK / RESOLUTION / COMPLETENESS);
a positive case must PASS.  Seed fixed.  Usage: mutation_controls_rdsqs.py CERT OUTDIR
"""
import hashlib
import json
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def parse(path):
    v, blocks, pts, cur = None, [], {}, None
    order = []
    for raw in open(path):
        line = raw.split("#")[0].strip()
        if not line:
            continue
        t = line.split()
        if t[0] == "RDSQS":
            v = int(t[1])
        elif t[0] == "BLOCKS":
            continue
        elif t[0] == "POINT":
            cur = int(t[1]); pts[cur] = []; order.append(cur)
        elif t[0] == "CLASS":
            pts[cur].append([])
        elif cur is None:
            blocks.append(tuple(int(x) for x in t))
        else:
            pts[cur][-1].append(tuple(int(x) for x in t))
    return v, blocks, [(x, pts[x]) for x in order]


def dump(path, v, blocks, sections, header):
    out = [f"# {header}", f"RDSQS {v}", "BLOCKS"]
    out.extend(" ".join(map(str, b)) for b in blocks)
    for x, classes in sections:
        out.append(f"POINT {x}")
        for c, C in enumerate(classes):
            out.append(f"CLASS {c}")
            out.extend(" ".join(map(str, t)) for t in C)
    open(path, "w").write("\n".join(out) + "\n")


def run_checker(path):
    p = subprocess.run([sys.executable, os.path.join(HERE, "check_rdsqs.py"), path], capture_output=True, text=True)
    r = json.loads(p.stdout)
    return r["result"], r.get("reason", "")


def run_c_checker(path):
    v = next(int(l.split()[1]) for l in open(path) if l.startswith("RDSQS"))
    binary = "check_rdsqs_c" if v <= 64 else "check_rdsqs_c128"   # identical logic, larger MAXV
    p = subprocess.run([os.path.join(HERE, "bin", binary), path], capture_output=True, text=True)
    return ("PASS" if p.returncode == 0 and p.stdout.startswith("PASS") else "FAIL"), p.stdout.strip()[:120]


def deep(sections):
    return [(x, [list(C) for C in cl]) for x, cl in sections]


def main():
    cert, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    v, blocks, sections = parse(cert)
    rng = random.Random(20261016)
    bset = set(tuple(sorted(b)) for b in blocks)
    cases = []

    def case(name, intended, b, s, vv=None):
        p = os.path.join(outdir, f"{name}.txt")
        dump(p, vv if vv is not None else v, b, s, f"mutation {name}; intended {intended}")
        res, reason = run_checker(p)
        cres, creason = run_c_checker(p)
        ok = (res == "PASS") if intended == "PASS" else (res == "FAIL" and reason.startswith(intended))
        cok = (cres == "PASS") if intended == "PASS" else (cres == "FAIL")
        cases.append({"case": name, "intended": intended, "result": res, "reason": reason[:160],
                      "as_intended": ok, "c_result": cres, "c_reason": creason, "c_as_expected": cok,
                      "sha256": hashlib.sha256(open(p, "rb").read()).hexdigest()})

    # positive controls
    perm = list(range(v)); rng.shuffle(perm)
    rb = [tuple(sorted(perm[p] for p in b)) for b in blocks]
    rs = [(perm[x], [[tuple(sorted(perm[p] for p in t)) for t in C] for C in cl]) for x, cl in sections]
    case("pos_relabel_points", "PASS", rb, rs)
    sb = list(blocks); rng.shuffle(sb)
    ss = deep(sections); rng.shuffle(ss)
    for _, cl in ss:
        rng.shuffle(cl)
        for C in cl:
            rng.shuffle(C)
    case("pos_shuffle_order", "PASS", sb, ss)
    # (1) triple coverage
    b = list(blocks); k = 7; old = b[k]
    for p in range(v):
        if p not in old:
            nb = tuple(sorted(old[:3] + (p,)))
            if nb not in bset:
                b[k] = nb; break
    case("cov_change_point_in_block", "COVERAGE", b, deep(sections))
    b = list(blocks); b1, b2 = list(b[3]), list(b[200 % len(b)])
    i1 = next(i for i, p in enumerate(b1) if p not in b2); i2 = next(i for i, p in enumerate(b2) if p not in b1)
    b1[i1], b2[i2] = b2[i2], b1[i1]
    b[3], b[200 % len(b)] = tuple(sorted(b1)), tuple(sorted(b2))
    if len(set(b)) == len(b):
        case("cov_swap_points_between_blocks", "COVERAGE", b, deep(sections))
    b = list(blocks); b[11] = b[12]
    case("block_duplicate", "BLOCK", b, deep(sections))
    b = list(blocks); del b[5]
    case("block_missing", "BLOCK", b, deep(sections))
    case("block_wrong_header_v", "BLOCK", list(blocks), deep(sections), vv=v + 6)
    # (2) per-point resolution
    s = deep(sections); x, cl = s[2]
    cl[0][0], cl[1][0] = cl[1][0], cl[0][0]
    case("res_swap_triples_between_classes", "RESOLUTION", list(blocks), s)
    s = deep(sections); x, cl = s[4]
    cl[1].append(cl[0].pop())
    case("res_move_triple_between_classes", "RESOLUTION", list(blocks), s)
    s = deep(sections); x, cl = s[5]
    der = set(tuple(p for p in bb if p != x) for bb in bset if x in bb)
    others = [y for y in range(v) if y != x]
    while True:
        t = tuple(sorted(rng.sample(others, 3)))
        if t not in der:
            break
    cl[3][0] = t
    case("res_nonderived_triple", "RESOLUTION", list(blocks), s)
    s = deep(sections); x, cl = s[6]
    del cl[-1]
    case("res_drop_class", "RESOLUTION", list(blocks), s)
    s = deep(sections)
    (x1, c1), (x2, c2) = s[8], s[9]
    s[8], s[9] = (x1, c2), (x2, c1)
    case("res_swap_point_labels", "RESOLUTION", list(blocks), s)
    # (3) missing-point completeness
    s = deep(sections); del s[10]
    case("comp_missing_point_section", "COMPLETENESS", list(blocks), s)
    s = deep(sections); s[12] = (s[13][0], s[12][1])
    case("comp_duplicate_point_label", "COMPLETENESS", list(blocks), s)
    s = deep(sections); s[1] = (v, s[1][1])
    case("comp_out_of_range_point_label", "COMPLETENESS", list(blocks), s)
    ok = all(c["as_intended"] and c["c_as_expected"] for c in cases)
    rec = {"certificate": cert, "certificate_sha256": hashlib.sha256(open(cert, "rb").read()).hexdigest(),
           "checker": "code/check_rdsqs.py",
           "checker_sha256": hashlib.sha256(open(os.path.join(HERE, "check_rdsqs.py"), "rb").read()).hexdigest(),
           "seed": 20261016, "all_as_intended": ok, "cases": cases}
    json.dump(rec, open(os.path.join(outdir, "mutation-results.json"), "w"), indent=1, ensure_ascii=False)
    for c in cases:
        print(f"{c['case']:36s} intended={c['intended']:12s} py={c['result']:4s} ok={c['as_intended']} | C={c['c_result']} ok={c['c_as_expected']} | {c['reason'][:60]}")
    print("ALL AS INTENDED" if ok else "UNEXPECTED RESULT PRESENT")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
