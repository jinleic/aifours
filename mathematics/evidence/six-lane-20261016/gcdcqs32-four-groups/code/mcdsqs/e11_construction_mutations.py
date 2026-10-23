#!/usr/bin/env python3
"""README E11d: construction-specific intended-reason mutations of the Construction 2.1 mcDSQS(128)
certificate (standard library + the two copied lane checkers in this directory).  Every mutated file is
retained; each must make BOTH checkers fail, each for the intended reason (regex on the failure message).
Mutations act at POINT 37 (group 1, translate a = 5) or on the local SQS(32) of group 2:
  m1  the local part of a merged hole-avoiding class split off as a 65th class;
  m2  that local part moved into a non-avoiding class instead;
  m3  one local triple replaced by the same Appendix B part triple under another translate a' != a;
  m4  one local SQS(32) block of group 2 dropped;
  m5  the local SQS(32) of group 2 relabelled by the transposition (65 66) (the block set stays an
      SQS(128)); the colourings are left unchanged.
Usage: e11_construction_mutations.py CERT OUTDIR C_CHECKER_BINARY"""
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402

G = 32
X = 37


def sections(L):
    blocks, pts, cur = [], {}, None
    for i, s in enumerate(L):
        t = s.split("#")[0].split()
        if not t:
            continue
        if t[0] == "POINT":
            cur = int(t[1])
            pts[cur] = []
        elif t[0] == "CLASS":
            pts[cur].append((i, []))
        elif cur is None and len(t) == 4:
            blocks.append(i)
        elif cur is not None:
            pts[cur][-1][1].append(i)
    return blocks, pts


def trip(L, i):
    return [int(z) for z in L[i].split()]


def mutations(L):
    blocks, pts = sections(L)
    grp, a = divmod(X, G)
    base = G * grp
    Gx = set(range(base, base + G))
    hole = Gx - {X}
    cls = pts[X]

    def local(i):
        return set(trip(L, i)) <= Gx

    merged = [(ci, tl) for ci, tl in cls if any(local(i) for i in tl)]
    nonavoid = [(ci, tl) for ci, tl in cls if not any(local(i) for i in tl)
                and any(set(trip(L, i)) & hole for i in tl)]
    assert len(merged) == 16 and len(nonavoid) == 48, (len(merged), len(nonavoid))
    out = {}

    def mut(name, py, c, f):
        M = list(L)
        f(M)
        out[name] = ("\n".join(M), py, c)

    def m1(M):
        ci, tl = merged[0]
        loc = [i for i in tl if local(i)]
        for i in loc:
            M[i] = ""
        last = cls[-1][1][-1]
        M[last] = M[last] + "\nCLASS 64\n" + "\n".join(L[i] for i in loc)
    mut("m1_local_part_as_extra_class", rf"POINT {X} has 65 classes, expected 64", r"too many classes", m1)

    def m2(M):
        ci, tl = merged[0]
        loc = [i for i in tl if local(i)]
        for i in loc:
            M[i] = ""
        nci, ntl = nonavoid[0]
        M[ntl[-1]] = M[ntl[-1]] + "\n" + "\n".join(L[i] for i in loc)
    mut("m2_local_part_into_nonavoiding_class", rf"POINT {X} class \d+ line \d+: triples not disjoint",
        r"class not point-disjoint", m2)

    def m3(M):
        for ci, tl in merged:
            for i in tl:
                if not local(i):
                    continue
                t = [p - base for p in trip(L, i)]
                kept = {p for k in tl if k != i for p in trip(L, k)}
                for d in range(1, G):
                    new = sorted(base + (p + d) % G for p in t)
                    if X in new or set(new) & kept:
                        continue
                    M[i] = " ".join(map(str, new))
                    return
        raise RuntimeError("no isolated translate")
    mut("m3_local_triple_other_translate", r"is not a block", r"triple plus POINT is not a block", m3)

    def m4(M):
        i = next(i for i in blocks if all(64 <= p < 96 for p in trip(L, i)))
        M[i] = ""
    mut("m4_drop_local_sqs_block_group2", r"^BLOCK: 85343 blocks, expected 85344", r"wrong number of blocks", m4)

    def m5(M):
        sw = {65: 66, 66: 65}
        for i in blocks:
            b = trip(L, i)
            if all(64 <= p < 96 for p in b):
                M[i] = " ".join(map(str, sorted(sw.get(p, p) for p in b)))
    mut("m5_relabelled_local_sqs_group2", r"is not a block", r"triple plus POINT is not a block", m5)
    return out


def main():
    cert, outdir, cbin = sys.argv[1:4]
    os.mkdir(outdir)
    L = open(cert).read().split("\n")
    results, ok_all = {}, True
    for name, (text, py_re, c_re) in mutations(L).items():
        p = os.path.join(outdir, name + ".txt")
        with xopen(p) as fh:
            fh.write(text)
        py = subprocess.run([sys.executable, os.path.join(HERE, "check_mcdsqs.py"), p], capture_output=True, text=True)
        pr = json.loads(py.stdout)
        cc = subprocess.run([cbin, p], capture_output=True, text=True)
        py_ok = py.returncode == 1 and pr["result"] == "FAIL" and re.search(py_re, pr.get("failure", "")) is not None
        c_ok = cc.returncode == 1 and cc.stdout.startswith("FAIL") and re.search(c_re, cc.stdout) is not None
        results[name] = {"mutated_file": p, "mutated_sha256": hashlib.sha256(text.encode()).hexdigest(),
                         "python": pr.get("failure", pr["result"]), "python_as_intended": py_ok,
                         "c": cc.stdout.strip(), "c_as_intended": c_ok}
        ok_all &= py_ok and c_ok
    base_py = json.loads(subprocess.run([sys.executable, os.path.join(HERE, "check_mcdsqs.py"), cert],
                                        capture_output=True, text=True).stdout)["result"]
    base_c = subprocess.run([cbin, cert], capture_output=True, text=True).stdout.strip()
    summary = {"certificate": cert, "certificate_sha256": hashlib.sha256(open(cert, "rb").read()).hexdigest(),
               "unmutated_python": base_py, "unmutated_c": base_c, "mutations": len(results),
               "as_intended": sum(r["python_as_intended"] and r["c_as_intended"] for r in results.values()),
               "results": results}
    with xopen(os.path.join(outdir, "construction-mutation-results.json")) as fh:
        json.dump(summary, fh, indent=1)
    print(f"{summary['as_intended']}/{summary['mutations']} construction mutations as intended; "
          f"unmutated: {base_py} / {base_c}")
    for n, r in results.items():
        print(n, "|", r["python"], "|", r["c"], "|", r["python_as_intended"] and r["c_as_intended"])
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
