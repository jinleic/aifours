"""Develop resolved base constituents by a group G into a labelled LKTS
certificate (text format of check_lkts57.py).

bases: list of (classes, H_elements) where classes is a list of (v-1)/2 lists of
point triples (a resolution of the base) and H_elements the base stabilizer in G.
The constituents are g(base) for g ranging over left coset representatives of
G/H; resolutions are transported by g.
"""
from __future__ import annotations

from lkts_core import compose


def coset_reps(G, H):
    Hs = set(H)
    reps, seen = [], set()
    for g in G:
        if g in seen:
            continue
        reps.append(g)
        seen.update(compose(g, h) for h in Hs)
    return reps


def develop(G, bases, v):
    constituents = []
    for classes, H in bases:
        for g in coset_reps(G, H):
            constituents.append([[tuple(sorted(g[p] for p in b)) for b in C] for C in classes])
    assert len(constituents) == v - 2, len(constituents)
    return constituents


def write_certificate(constituents, v, path, header_comment=""):
    lines = [f"# {header_comment}"] if header_comment else []
    lines.append(f"LKTS {v}")
    for k, classes in enumerate(constituents):
        lines.append(f"KTS {k}")
        for c, C in enumerate(classes):
            lines.append(f"CLASS {c}")
            for b in sorted(C):
                lines.append(f"{b[0]} {b[1]} {b[2]}")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
