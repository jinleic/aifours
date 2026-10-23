#!/usr/bin/env python3
"""Intended-reason mutation controls for MCDSQS certificates (standard library + the two lane
checkers).  Each mutation must make BOTH checkers fail, each for the intended reason (regex on
the failure message).  Usage: mutation_controls_mcdsqs.py CERT OUTDIR [C_CHECKER_BINARY]

Copy of mcdsqs38/code/mutation_controls.py (sha256 e2fa6511…c902ca), changed only to import the
no-deletion guard, create a fresh output directory, write exclusively and RETAIN every mutated file."""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402


def load(path):
    return open(path).read().split("\n")


def sections(L):
    """Indices: header lines, block lines, point -> list of (class line idx, [triple line idx])."""
    blocks, pts, cur = [], {}, None
    for i, s in enumerate(L):
        t = s.split("#")[0].split()
        if not t:
            continue
        if t[0] == "POINT":
            cur = int(t[1]); pts[cur] = []
        elif t[0] == "CLASS":
            pts[cur].append((i, []))
        elif cur is None and len(t) == 4:
            blocks.append(i)
        elif cur is not None:
            pts[cur][-1][1].append(i)
    return blocks, pts


def trip(L, i):
    return [int(x) for x in L[i].split()]


def mutations(L):
    blocks, pts = sections(L)
    v = int(next(s.split()[1] for s in L if s.startswith("MCDSQS")))
    head = next(i for i, s in enumerate(L) if s.startswith("COLOURS"))
    vline = next(i for i, s in enumerate(L) if s.startswith("MCDSQS"))
    out = {}

    def mut(name, py, c, f):
        M = list(L)
        f(M)
        out[name] = ("\n".join(M), py, c)

    mut("drop_block", r"^BLOCK: \d+ blocks", r"wrong number of blocks", lambda M: M.__setitem__(blocks[5], ""))
    mut("duplicate_block", r"^BLOCK: .*repeated block", r"two blocks \(or repeated block\)",
        lambda M: M.__setitem__(blocks[7], M[blocks[3]]))

    def corrupt(M):
        b = [int(x) for x in M[blocks[11]].split()]
        new = next(p for p in range(v) if p not in b)
        b[0] = new
        M[blocks[11]] = " ".join(map(str, sorted(b)))
    mut("corrupt_block_point", r"^COVERAGE", r"3-subset (in two blocks|lies in no block)", corrupt)

    x = 3
    cls = pts[x]

    def move_conflict(M):
        # move a triple of class 0 at POINT x into class 1, choosing one that meets class 1
        c1pts = {p for i in cls[1][1] for p in trip(L, i)}
        i = next(i for i in cls[0][1] if set(trip(L, i)) & c1pts)
        M[i] = ""
        M[cls[1][0]] = M[cls[1][0]] + "\n" + L[i]
    mut("move_triple_into_clashing_class", r"^COLOURING: .*not disjoint", r"class not point-disjoint", move_conflict)

    # replace one point by a point unused in the class, so the only defect is "not a block"
    def nonderived_isolated(M):
        i = cls[2][1][0]
        t = trip(L, i)
        used = {p for j in cls[2][1] for p in trip(L, j)}
        cand = next(p for p in range(v) if p not in used and p != x)
        M[i] = " ".join(map(str, sorted([t[0], t[1], cand])))
    mut("non_derived_triple", r"is not a block", r"triple plus POINT is not a block", nonderived_isolated)

    def dup_triple(M):
        # copy a triple of another class into a class that misses all its points (or replace one
        # triple of that class so the copy clashes with nothing): the only defect is the repeat
        for ci, tl in sorted(cls, key=lambda c: len(c[1])):
            for j in [None] + tl:
                kept = {p for k in tl if k != j for p in trip(L, k)}
                for oi, otl in cls:
                    if oi == ci:
                        continue
                    for i in otl:
                        if not set(trip(L, i)) & kept:
                            if j is None:
                                M[ci] = M[ci] + "\n" + L[i]
                            else:
                                M[j] = L[i]
                            return
        raise RuntimeError("no isolated duplicate position")
    mut("triple_listed_twice", r"listed twice", r"listed twice", dup_triple)
    mut("delete_triple", r"not the derived design", r"derived triples not all listed",
        lambda M: M.__setitem__(cls[6][1][0], ""))

    def contains_x(M):
        i = cls[7][1][0]
        t = trip(L, i)
        M[i] = " ".join(map(str, sorted([t[0], t[1], x])))
    mut("triple_contains_point", r"not 3 distinct points", r"triple contains its POINT", contains_x)

    def drop_last_point(M):
        last = max(pts)
        start = next(i for i, s in enumerate(L) if s == f"POINT {last}")
        for i in range(start, len(M)):
            M[i] = ""
    mut("drop_point_section", r"^COMPLETENESS", r"missing POINT sections", drop_last_point)

    def relabel_point(M):
        i = next(i for i, s in enumerate(L) if s == "POINT 6")
        M[i] = "POINT 5"
    mut("point_label_twice", r"^COMPLETENESS: POINT 5 appears twice", r"POINT listed twice", relabel_point)

    def split_class(M):
        # split class 0 at POINT x into two classes (r+1 classes)
        i0, tl = cls[0]
        M[tl[len(tl) // 2]] = "CLASS 1\n" + L[tl[len(tl) // 2]]
        for k, (ci, _) in enumerate(cls[1:], start=2):
            M[ci] = f"CLASS {k}"
    mut("split_class_extra_colour", r"classes, expected", r"too many classes", split_class)

    def colours_plus(M):
        r = int(L[head].split()[1])
        M[head] = f"COLOURS {r + 1}"
    mut("colours_header_not_chi", r"^COLOURS: r=", r"COLOURS differs", colours_plus)

    def class_id_skip(M):
        M[cls[3][0]] = "CLASS 4"
    mut("class_id_out_of_order", r"out of order", r"class id out of order", class_id_skip)

    def other_point_triple(M):
        # a valid triple of POINT 4 (avoiding x) added to / substituted into a class of POINT x
        # where it clashes with nothing: the only defect is that t ∪ {x} is not a block
        for i in (j for c in pts[4] for j in c[1]):
            t = set(trip(L, i))
            if x in t:
                continue
            for ci, tl in sorted(cls, key=lambda c: len(c[1])):
                for j in [None] + tl:
                    kept = {p for k in tl if k != j for p in trip(L, k)}
                    if not t & kept:
                        if j is None:
                            M[ci] = M[ci] + "\n" + L[i]
                        else:
                            M[j] = L[i]
                        return
        raise RuntimeError("no isolated foreign triple")
    mut("triple_from_other_point", r"is not a block", r"not a block", other_point_triple)

    def bad_v(M):
        M[vline] = f"MCDSQS {v - 1}"
    mut("v_header", r"^BLOCK: v=", r"v out of range or not 2,4 mod 6", bad_v)
    return out


def main():
    cert, outdir = sys.argv[1], sys.argv[2]
    cbin = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "bin", "check_mcdsqs_c")
    fresh_dir(outdir)
    L = load(cert)
    results = {}
    ok_all = True
    for name, (text, py_re, c_re) in mutations(L).items():
        p = os.path.join(outdir, name + ".txt")
        with xopen(p) as fh:
            fh.write(text)
        py = subprocess.run([sys.executable, os.path.join(HERE, "check_mcdsqs.py"), p], capture_output=True, text=True)
        pr = json.loads(py.stdout)
        cc = subprocess.run([cbin, p], capture_output=True, text=True)
        py_ok = py.returncode == 1 and pr["result"] == "FAIL" and re.search(py_re, pr.get("failure", "")) is not None
        c_ok = cc.returncode == 1 and cc.stdout.startswith("FAIL") and re.search(c_re, cc.stdout) is not None
        results[name] = {"python": pr.get("failure", pr["result"]), "python_as_intended": py_ok,
                         "c": cc.stdout.strip(), "c_as_intended": c_ok}
        ok_all &= py_ok and c_ok
    base_py = json.loads(subprocess.run([sys.executable, os.path.join(HERE, "check_mcdsqs.py"), cert],
                                        capture_output=True, text=True).stdout)["result"]
    base_c = subprocess.run([cbin, cert], capture_output=True, text=True).stdout.strip()
    summary = {"certificate": cert, "unmutated_python": base_py, "unmutated_c": base_c,
               "mutations": len(results), "as_intended": sum(r["python_as_intended"] and r["c_as_intended"]
                                                             for r in results.values()),
               "results": results}
    with xopen(os.path.join(outdir, "mutation-results.json")) as fh:
        json.dump(summary, fh, indent=1)
    print(f"{summary['as_intended']}/{summary['mutations']} mutations as intended; unmutated: {base_py} / {base_c}")
    for n, r in results.items():
        if not (r["python_as_intended"] and r["c_as_intended"]):
            print("NOT AS INTENDED", n, r)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
