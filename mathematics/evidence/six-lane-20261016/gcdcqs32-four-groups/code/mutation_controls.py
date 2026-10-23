#!/usr/bin/env python3
"""Intended-reason mutation controls for GCDCQS certificates.  Every mutated certificate is
WRITTEN AND RETAINED in OUTDIR (exclusive create) with its sha256; both lane checkers must fail
it for the intended reason (regex on the failure message).
Usage: mutation_controls.py CERT OUTDIR [C_CHECKER_BINARY]"""
import lane_guard  # noqa: F401

import hashlib
import json
import os
import re
import subprocess
import sys

from lane_guard import fresh_dir, xopen

HERE = os.path.dirname(os.path.abspath(__file__))


def parse_layout(L):
    head, groups, blocks, pts, cur = {}, [], [], {}, None
    state = "head"
    for i, s in enumerate(L):
        t = s.split("#")[0].split()
        if not t:
            continue
        if t[0] in ("GCDCQS", "COLOURS", "HOLEFREE"):
            head[t[0]] = i
        elif t[0] == "GROUPS":
            state = "groups"
        elif t[0] == "BLOCKS":
            state = "blocks"
        elif t[0] == "POINT":
            cur = int(t[1]); pts[cur] = []; state = "points"
        elif t[0] == "CLASS":
            pts[cur].append((i, []))
        elif state == "groups":
            groups.append(i)
        elif state == "blocks":
            blocks.append(i)
        else:
            pts[cur][-1][1].append(i)
    return head, groups, blocks, pts


def nums(L, i):
    return [int(x) for x in L[i].split()]


def mutations(L):
    head, groups, blocks, pts = parse_layout(L)
    v, n, g = [int(x) for x in L[head["GCDCQS"]].split()[1:]]
    group_of = {}
    for gi, i in enumerate(groups):
        for p in nums(L, i):
            group_of[p] = gi
    out = {}
    not_applicable = {}

    def mut(name, py, c, f):
        M = list(L)
        try:
            f(M)
        except RuntimeError as e:  # no isolated instance exists in this certificate
            not_applicable[name] = str(e)
            return
        out[name] = ("\n".join(M), py, c)

    mut("drop_block", r"^BLOCK: \d+ blocks", r"wrong number of blocks", lambda M: M.__setitem__(blocks[5], ""))
    mut("duplicate_block", r"repeated block", r"two blocks \(or repeated block\)",
        lambda M: M.__setitem__(blocks[7], M[blocks[3]]))

    def corrupt(M):
        # replace one point of a block by another point of the same group: keeps the group
        # profile (no three in a group) but breaks exact coverage
        b = nums(L, blocks[11])
        q = next(p for p in range(v) if group_of[p] == group_of[b[0]] and p not in b)
        M[blocks[11]] = " ".join(map(str, sorted([q] + b[1:])))
    mut("corrupt_block_point", r"^COVERAGE|repeated block", r"3-subset in two blocks|lies in no block", corrupt)

    def three_in_group(M):
        b = nums(L, blocks[13])
        G0 = sorted(p for p in range(v) if group_of[p] == 0)
        M[blocks[13]] = " ".join(map(str, sorted(G0[:3] + [next(p for p in range(v) if group_of[p] == 1)])))
    mut("block_with_three_points_in_a_group", r"three points in one group", r"three block points in one group", three_in_group)

    def group_twice(M):
        a = nums(L, groups[0])[0]
        G1 = nums(L, groups[1])
        G1[0] = a
        M[groups[1]] = " ".join(map(str, G1))
    mut("group_point_in_two_groups", r"^GROUPS: .*(two groups|distinct)", r"point in two groups", group_twice)

    def group_swap(M):
        G0, G1 = nums(L, groups[0]), nums(L, groups[1])
        G0[0], G1[0] = G1[0], G0[0]
        M[groups[0]] = " ".join(map(str, G0))
        M[groups[1]] = " ".join(map(str, G1))
    mut("groups_swap_two_points", r"three points in one group|3-subset of a group",
        r"three block points in one group|group triple lies in a block", group_swap)

    x = 3
    cls = pts[x]
    hole = {p for p in range(v) if group_of[p] == group_of[x] and p != x}

    def move_conflict(M):
        c1pts = {p for i in cls[1][1] for p in nums(L, i)}
        i = next(i for i in cls[0][1] if set(nums(L, i)) & c1pts)
        M[i] = ""
        M[cls[1][0]] = M[cls[1][0]] + "\n" + L[i]
    mut("move_triple_into_clashing_class", r"not disjoint", r"class not point-disjoint", move_conflict)

    bset = {frozenset(nums(L, i)) for i in blocks}

    def nonderived(M):
        # replace one point by a point unused in the class such that T ∪ {x} is not a block:
        # the only defect is "not a block"
        i = cls[2][1][0]
        t = nums(L, i)
        used = {p for j in cls[2][1] for p in nums(L, j)}
        cand = next(p for p in range(v) if p not in used and p != x
                    and frozenset([t[0], t[1], p, x]) not in bset)
        M[i] = " ".join(map(str, sorted([t[0], t[1], cand])))
    mut("non_derived_triple", r"is not a block", r"triple plus POINT is not a block", nonderived)

    def dup_triple(M):
        for ci, tl in sorted(cls, key=lambda c: len(c[1])):
            for j in [None] + tl:
                kept = {p for k in tl if k != j for p in nums(L, k)}
                for oi, otl in cls:
                    if oi == ci:
                        continue
                    for i in otl:
                        if not set(nums(L, i)) & kept:
                            if j is None:
                                M[ci] = M[ci] + "\n" + L[i]
                            else:
                                M[j] = L[i]
                            return
        raise RuntimeError("no isolated duplicate position")
    mut("triple_listed_twice", r"listed twice", r"listed twice", dup_triple)
    mut("delete_triple", r"not the derived design", r"derived design not fully listed",
        lambda M: M.__setitem__(cls[6][1][0], ""))

    def contains_x(M):
        i = cls[4][1][0]
        t = nums(L, i)
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
        _, tl = cls[0]
        M[tl[len(tl) // 2]] = "CLASS 1\n" + L[tl[len(tl) // 2]]
        for k, (ci, _) in enumerate(cls[1:], start=2):
            M[ci] = f"CLASS {k}"
    mut("split_class_extra_colour", r"classes, expected", r"too many classes", split_class)

    def empty_class(M):
        for i in cls[5][1]:
            M[i] = ""
    mut("empty_class", r"is empty", r"empty class", empty_class)

    r = int(L[head["COLOURS"]].split()[1])
    s = int(L[head["HOLEFREE"]].split()[1])
    mut("colours_header_not_chi", r"^PARAMS: COLOURS", r"COLOURS differs",
        lambda M: M.__setitem__(head["COLOURS"], f"COLOURS {r + 1}"))
    mut("holefree_header_wrong", r"^PARAMS: HOLEFREE", r"HOLEFREE differs",
        lambda M: M.__setitem__(head["HOLEFREE"], f"HOLEFREE {s + 1}"))
    mut("class_id_out_of_order", r"out of order", r"class id out of order",
        lambda M: M.__setitem__(cls[3][0], "CLASS 4"))

    def other_point_triple(M):
        for i in (j for c in pts[4] for j in c[1]):
            t = set(nums(L, i))
            if x in t:
                continue
            for ci, tl in sorted(cls, key=lambda c: len(c[1])):
                for j in [None] + tl:
                    kept = {p for k in tl if k != j for p in nums(L, k)}
                    if not t & kept:
                        if j is None:
                            M[ci] = M[ci] + "\n" + L[i]
                        else:
                            M[j] = L[i]
                        return
        raise RuntimeError("no isolated foreign triple")
    mut("triple_from_other_point", r"is not a block", r"not a block", other_point_triple)
    mut("v_header", r"^PARAMS", r"bad v, n, g|not an STS order",
        lambda M: M.__setitem__(head["GCDCQS"], f"GCDCQS {v - 1} {n} {g}"))

    # Kempe-chain swap between a hole-avoiding class a and a non-avoiding class b at some point:
    # both remain partial parallel classes and the listed triples are unchanged, but afterwards both
    # a and b contain hole points -> only the hole-avoiding count (s - 1) is wrong.
    def kempe(M):
        for y in sorted(pts):
            hy = {p for p in range(v) if group_of[p] == group_of[y] and p != y}
            cl = pts[y]
            sets = [[nums(L, i) for i in tl] for _, tl in cl]
            avoid = [k for k, C in enumerate(sets) if not any(set(t) & hy for t in C)]
            for a in avoid:
                for b in range(len(cl)):
                    if b in avoid:
                        continue
                    items = [(a, i) for i in cl[a][1]] + [(b, i) for i in cl[b][1]]
                    adj = {it: [] for it in items}
                    for p1 in items:
                        for p2 in items:
                            if p1[0] != p2[0] and set(nums(L, p1[1])) & set(nums(L, p2[1])):
                                adj[p1].append(p2)
                    seen = set()
                    for st in items:
                        if st in seen:
                            continue
                        comp_, stack = [], [st]
                        seen.add(st)
                        while stack:
                            u = stack.pop()
                            comp_.append(u)
                            for w in adj[u]:
                                if w not in seen:
                                    seen.add(w)
                                    stack.append(w)
                        moved_hole = [it for it in comp_ if it[0] == b and set(nums(L, it[1])) & hy]
                        left_hole = [i for i in cl[b][1] if set(nums(L, i)) & hy and (b, i) not in comp_]
                        if moved_hole and left_hole:
                            for side, i in comp_:
                                M[i] = ""
                                target = cl[b][0] if side == a else cl[a][0]
                                M[target] = M[target] + "\n" + L[i]
                            return
        raise RuntimeError("no Kempe swap that reduces the number of hole-avoiding classes")
    mut("kempe_swap_no_hole_avoiding_class", r"classes avoid the hole, expected exactly",
        r"wrong number of hole-avoiding classes", kempe)
    return out, not_applicable


def main():
    cert, outdir = sys.argv[1], sys.argv[2]
    cbin = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "bin", "check_gcdcqs_c")
    fresh_dir(outdir)
    L = open(cert).read().split("\n")
    results, ok_all = {}, True
    muts, not_applicable = mutations(L)
    for name, (text, py_re, c_re) in muts.items():
        p = os.path.join(outdir, name + ".txt")
        with xopen(p) as fh:
            fh.write(text)
        py = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs.py"), p], capture_output=True, text=True)
        pr = json.loads(py.stdout)
        cc = subprocess.run([cbin, p], capture_output=True, text=True)
        py_ok = py.returncode == 1 and pr["result"] == "FAIL" and re.search(py_re, pr.get("failure", "")) is not None
        c_ok = cc.returncode == 1 and cc.stdout.startswith("FAIL") and re.search(c_re, cc.stdout) is not None
        results[name] = {"mutated_file": p, "mutated_sha256": hashlib.sha256(text.encode()).hexdigest(),
                         "python": pr.get("failure", pr["result"]), "python_as_intended": py_ok,
                         "c": cc.stdout.strip(), "c_as_intended": c_ok}
        ok_all &= py_ok and c_ok
    base_py = json.loads(subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs.py"), cert],
                                        capture_output=True, text=True).stdout)["result"]
    base_c = subprocess.run([cbin, cert], capture_output=True, text=True).stdout.strip()
    summary = {"certificate": cert, "certificate_sha256": hashlib.sha256(open(cert, "rb").read()).hexdigest(),
               "unmutated_python": base_py, "unmutated_c": base_c, "mutations": len(results),
               "as_intended": sum(r["python_as_intended"] and r["c_as_intended"] for r in results.values()),
               "results": results,
               "not_constructible_in_this_certificate": not_applicable}
    with xopen(os.path.join(outdir, "mutation-results.json")) as fh:
        json.dump(summary, fh, indent=1)
    print(f"{summary['as_intended']}/{summary['mutations']} mutations as intended; unmutated: {base_py} / {base_c}")
    for nm, why in not_applicable.items():
        print("NOT CONSTRUCTIBLE", nm, why)
    for nm, rr in results.items():
        if not (rr["python_as_intended"] and rr["c_as_intended"]):
            print("NOT AS INTENDED", nm, rr["python"], "|", rr["c"])
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
