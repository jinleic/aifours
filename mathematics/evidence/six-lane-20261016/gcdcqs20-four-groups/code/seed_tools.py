#!/usr/bin/env python3
"""Standard-library seed tools for GCDCQS certificates built over a transitive group G given by
generators (permutations of the v labels).

make   CERT GROUP OUT.json   seed = {header, v, n, g, r, s, groups, generators (as image lists),
                              block orbit representatives (least block of each G-orbit), classes at 0}
expand SEED.json OUT [COMPARE]  G = closure(generators); blocks = union of G-orbits of the
                              representatives; colouring at y = e(classes at 0) for the least e in G
                              (sorted image tuples) with e(0) = y; certificate text exactly as the
                              pipeline writes it; optional byte comparison.
audit  CERT SEED.json OUT.json   checks: blocks G-invariant; every POINT y section equals e_y(POINT 0)
                              class by class; every element of G maps the colouring at 0 onto the
                              colouring at its image (as sets of classes).
All writes exclusive-create; no imports beyond the standard library (and lane_guard).
"""
import hashlib
import json
import os
import sys
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402


def closure(gens, v):
    e = tuple(range(v))
    G, dq = {e}, deque([e])
    while dq:
        a = dq.popleft()
        for p in gens:
            c = tuple(p[a[y]] for y in range(v))
            if c not in G:
                G.add(c)
                dq.append(c)
    return sorted(G)


def read_cert(path):
    header, head, groups, blocks, col, cur, state = None, {}, [], [], {}, None, "head"
    for raw in open(path):
        line = raw.rstrip("\n")
        if header is None and line.startswith("#"):
            header = line
        s = line.split("#")[0].strip()
        if not s:
            continue
        t = s.split()
        if t[0] in ("GCDCQS", "COLOURS", "HOLEFREE"):
            head[t[0]] = [int(z) for z in t[1:]]
        elif t[0] == "GROUPS":
            state = "groups"
        elif t[0] == "BLOCKS":
            state = "blocks"
        elif t[0] == "POINT":
            cur = int(t[1]); col[cur] = []; state = "points"
        elif t[0] == "CLASS":
            col[cur].append([])
        elif state == "groups":
            groups.append([int(z) for z in t])
        elif state == "blocks":
            blocks.append(tuple(sorted(int(z) for z in t)))
        else:
            col[cur][-1].append(tuple(sorted(int(z) for z in t)))
    return header, head, groups, blocks, col


def cert_text(header, v, n, g, r, s, groups, blocks, col):
    lines = [header, f"GCDCQS {v} {n} {g}", f"COLOURS {r}", f"HOLEFREE {s}", "GROUPS"]
    lines += [" ".join(map(str, G)) for G in groups]
    lines.append("BLOCKS")
    lines += [" ".join(map(str, b)) for b in sorted(blocks)]
    for y in range(v):
        lines.append(f"POINT {y}")
        for j, C in enumerate(col[y]):
            lines.append(f"CLASS {j}")
            lines += [" ".join(map(str, t)) for t in C]
    return "\n".join(lines) + "\n"


def expand(seed):
    v = seed["v"]
    G = closure([tuple(p) for p in seed["generators"]], v)
    blocks = set()
    for b in seed["block_orbit_representatives"]:
        for e in G:
            blocks.add(tuple(sorted(e[p] for p in b)))
    classes0 = [[tuple(t) for t in C] for C in seed["classes_at_0"]]
    col = {}
    for e in G:
        y = e[0]
        if y not in col:
            col[y] = [sorted(tuple(sorted(e[p] for p in t)) for t in C) for C in classes0]
    assert sorted(col) == list(range(v)), "group is not transitive"
    text = cert_text(seed["header"], v, seed["n"], seed["g"], seed["r"], seed["s"], seed["groups"], blocks, col)
    return text, G, blocks, col


def main():
    mode = sys.argv[1]
    if mode == "make":
        cert, group, out = sys.argv[2], sys.argv[3], sys.argv[4]
        import groups as grp  # lane module (pure Python, no numpy)
        header, head, groups_, blocks, col = read_cert(cert)
        v, n, g = head["GCDCQS"]
        spec = grp.build(group, n, g)
        G = closure(spec["gens"], v)
        left, reps = set(blocks), []
        for b in sorted(blocks):
            if b in left:
                orb = {tuple(sorted(e[p] for p in b)) for e in G}
                assert orb <= left
                left -= orb
                reps.append(list(b))
        seed = {"header": header, "v": v, "n": n, "g": g, "r": head["COLOURS"][0], "s": head["HOLEFREE"][0],
                "groups": groups_, "group_name": group, "generators": [list(p) for p in spec["gens"]],
                "block_orbit_representatives": reps, "classes_at_0": [[list(t) for t in C] for C in col[0]],
                "rule": "see code/seed_tools.py expand"}
        with xopen(out) as fh:
            json.dump(seed, fh)
        print("block orbits", len(reps), "classes", len(col[0]))
    elif mode == "expand":
        seed = json.load(open(sys.argv[2]))
        text, G, blocks, col = expand(seed)
        data = text.encode()
        with xopen(sys.argv[3], "xb") as fh:
            fh.write(data)
        print("group order", len(G), "blocks", len(blocks), "sha256", hashlib.sha256(data).hexdigest())
        if len(sys.argv) > 4:
            same = open(sys.argv[4], "rb").read() == data
            print("byte-identical to", sys.argv[4], ":", same)
            sys.exit(0 if same else 1)
    elif mode == "audit":
        cert, seedp, out = sys.argv[2], sys.argv[3], sys.argv[4]
        header, head, groups_, blocks, col = read_cert(cert)
        seed = json.load(open(seedp))
        v = head["GCDCQS"][0]
        gens = [tuple(p) for p in seed["generators"]]
        G = closure(gens, v)
        B = set(blocks)
        rec = {"certificate": cert, "group_order": len(G)}
        rec["blocks_invariant_under_generators"] = all(tuple(sorted(p[y] for y in b)) in B for p in gens for b in B)
        rec["transitive"] = sorted({e[0] for e in G}) == list(range(v))
        first = {}
        for e in G:
            first.setdefault(e[0], e)
        c0 = [frozenset(tuple(C)) for C in col[0]]
        rec["points_are_least_element_images"] = all(
            [frozenset(tuple(sorted(first[y][p] for p in t)) for t in C) for C in c0] == [frozenset(C) for C in col[y]]
            for y in range(v))
        rec["every_g_maps_colouring_0_to_colouring_g0"] = all(
            {frozenset(tuple(sorted(e[p] for p in t)) for t in C) for C in c0} == {frozenset(C) for C in col[e[0]]}
            for e in G)
        rec["result"] = "PASS" if all(rec[k] for k in rec if k not in ("certificate", "group_order")) else "FAIL"
        with xopen(out) as fh:
            json.dump(rec, fh, indent=1)
        print(json.dumps(rec))
    else:
        raise SystemExit("mode must be make, expand or audit")


if __name__ == "__main__":
    main()
