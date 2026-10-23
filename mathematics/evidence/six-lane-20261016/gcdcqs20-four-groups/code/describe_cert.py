#!/usr/bin/env python3
"""Read-only description of a pinned GCDCQS certificate built over A4 x C20 (standard library):
block orbit representatives under G (least block, orbit length, group profile), the colouring at
point 0 (class sizes, hole-avoiding flags), and the permutation induced by pi1 = (1 2 3) on the
group index on the classes at 0 (cycle type; checks pi1-invariance).  Writes OUT.json and OUT.md.
Usage: describe_cert.py CERT SEED.json OUT.json OUT.md"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402
from seed_tools import closure, read_cert  # noqa: E402


def main():
    cert, seedp, oj, om = sys.argv[1:5]
    header, head, groups, blocks, col = read_cert(cert)
    v, n, g = head["GCDCQS"]
    seed = json.load(open(seedp))
    G = closure([tuple(p) for p in seed["generators"]], v)
    gof = {p: i for i, Gr in enumerate(groups) for p in Gr}
    left, orbs = set(blocks), []
    for b in sorted(blocks):
        if b in left:
            orb = {tuple(sorted(e[p] for p in b)) for e in G}
            left -= orb
            prof = sorted([sum(1 for p in b if gof[p] == i) for i in range(n)], reverse=True)
            orbs.append({"rep": list(b), "length": len(orb), "profile": "+".join(str(c) for c in prof if c)})
    pi1 = tuple(g * [0, 2, 3, 1][a // g] + a % g for a in range(v))
    hole = {p for p in groups[gof[0]] if p != 0}
    cls = col[0]
    keys = [frozenset(C) for C in cls]
    perm = [keys.index(frozenset(tuple(sorted(pi1[p] for p in t)) for t in C)) for C in cls]
    cyc, seen = [], set()
    for i in range(len(perm)):
        if i in seen:
            continue
        L, j = 0, i
        while j not in seen:
            seen.add(j); j = perm[j]; L += 1
        cyc.append(L)
    avoid = [not any(set(t) & hole for t in C) for C in cls]
    fixed = [i for i in range(len(perm)) if perm[i] == i]
    desc = {"certificate": cert, "group_order": len(G), "block_orbits": len(orbs),
            "block_orbit_lengths": sorted({o["length"] for o in orbs}),
            "orbits": orbs, "class_sizes_at_0": [len(C) for C in cls], "hole_avoiding_at_0": avoid,
            "pi1_class_permutation": perm, "pi1_cycle_type": sorted(cyc), "pi1_fixed_classes": fixed,
            "fixed_class_triples": [list(t) for i in fixed for t in cls[i]]}
    with xopen(oj) as fh:
        json.dump(desc, fh, indent=1)
    L = [f"# Description of `{cert}`", "",
         f"G = A4 × C20 (order {len(G)}). Blocks: {len(orbs)} G-orbits.", "",
         "| # | least block | length | group profile |", "|---|---|---|---|"]
    L += [f"| {i} | {{{', '.join(map(str, o['rep']))}}} | {o['length']} | {o['profile']} |" for i, o in enumerate(orbs)]
    L += ["", f"Colouring at 0: class sizes {[len(C) for C in cls]}; hole-avoiding classes "
          f"{[i for i, a in enumerate(avoid) if a]}; π₁ permutes the classes with cycle type "
          f"{sorted(cyc)}, fixed class(es) {fixed}.", ""]
    for i in fixed:
        L.append(f"* fixed class {i}: " + " ".join("{" + ",".join(map(str, t)) + "}" for t in cls[i]))
    with xopen(om) as fh:
        fh.write("\n".join(L) + "\n")
    print(json.dumps({k: desc[k] for k in ("block_orbits", "block_orbit_lengths", "pi1_cycle_type", "pi1_fixed_classes")}))


if __name__ == "__main__":
    main()
