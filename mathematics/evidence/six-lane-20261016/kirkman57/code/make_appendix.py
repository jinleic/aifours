#!/usr/bin/env python3
"""Generate a self-contained appendix (markdown) listing, for every base of a
seed, the block-orbit representatives under the stated base symmetry group K and
the class-orbit representatives under the stated resolution group R, and verify
that these representatives regenerate exactly the seed's base block set and base
resolution (standard library only).

Usage: make_appendix.py ORDER SEED OUT.md     (ORDER = 57 or 87)
"""
import hashlib
import json
import sys
from collections import deque


def comp(p, q):
    return tuple(p[x] for x in q)


def closure(gens, n):
    e = tuple(range(n)); seen = {e}; dq = deque([e])
    while dq:
        a = dq.popleft()
        for g in gens:
            b = comp(g, a)
            if b not in seen:
                seen.add(b); dq.append(b)
    return seen


def perm57(f):
    out = [0] * 57
    for i in range(3):
        for x in range(19):
            x2, i2 = f(x, i)
            out[19 * i + x] = 19 * (i2 % 3) + (x2 % 19)
    return tuple(out)


def perm87(f):
    out = [0] * 87
    for j in range(2):
        for x in range(43):
            x2, j2 = f(x, j)
            out[43 * j + x] = 43 * j2 + (x2 % 43)
    out[86] = 86
    return tuple(out)


def groups57():
    tau = perm57(lambda x, i: (x + 1, i)); nu = perm57(lambda x, i: (4 * x, i + 1)); rho = perm57(lambda x, i: (x, i + 1))
    mu = perm57(lambda x, i: (7 * x, i + 1)); mup = perm57(lambda x, i: (11 * x, i + 1))
    gam = lambda c, e: perm57(lambda x, i: (x + c * ([1, 7, 11] if e == 1 else [1, 11, 7])[i], i + 1))
    K = {"S0": ([nu, rho], "P27 = <nu, rho>"),
         "B1": ([tau, mu, gam(1, 1)], "<tau, mu, gamma_1>"), "B2": ([tau, mu, gam(2, 1)], "<tau, mu, gamma_2>"),
         "B3": ([tau, mup, gam(1, -1)], "<tau, mu', gamma'_1>"), "B4": ([tau, mup, gam(2, -1)], "<tau, mu', gamma'_2>")}
    R = {"S0": ([nu], "<nu>"), "B1": ([mu, gam(1, 1)], "<mu, gamma_1>"), "B2": ([mu, gam(2, 1)], "<mu, gamma_2>"),
         "B3": ([mup, gam(1, -1)], "<mu', gamma'_1>"), "B4": ([mup, gam(2, -1)], "<mu', gamma'_2>")}
    pt = lambda p: f"({p % 19},{p // 19})"
    return K, R, pt, 57


def groups87():
    tau = perm87(lambda x, j: (x + 1, j)); m = perm87(lambda x, j: (9 * x, j))
    K = {"S0": ([m], "<m>"), "B1": ([tau], "<tau>"), "B2": ([tau], "<tau>")}
    R = {"S0": ([m], "<m>"), "B1": ([tau], "<tau>"), "B2": ([tau], "<tau>")}
    pt = lambda p: "inf" if p == 86 else f"({p % 43},{p // 43})"
    return K, R, pt, 87


def main():
    order, seed_path, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
    K, R, pt, n = groups57() if order == 57 else groups87()
    seed = json.load(open(seed_path))
    img = lambda g, b: tuple(sorted(g[p] for p in b))
    lines = [f"# Appendix: base orbit data for the LKTS({order}) seed",
             "",
             f"Seed `{seed_path}` sha256 `{hashlib.sha256(open(seed_path, 'rb').read()).hexdigest()}`. "
             "Generated and self-checked by `code/make_appendix.py` (standard library): the listed "
             "representatives, acted on by the stated groups, regenerate exactly each base's block set and "
             "its 'classes' list (as a set of classes).", ""]
    for base in seed["bases"]:
        name = base["name"]
        classes = [frozenset(tuple(b) for b in C) for C in base["classes"]]
        blocks = set().union(*classes)
        Kg, Kname = K[name]; Rg, Rname = R[name]
        KG = closure(Kg, n); RG = closure(Rg, n)
        seen, breps = set(), []
        for b in sorted(blocks):
            if b in seen:
                continue
            o = {img(g, b) for g in KG}
            assert o <= blocks
            seen |= o; breps.append((b, len(o)))
        assert seen == blocks
        cseen, creps = set(), []
        cset = set(classes)
        for C in sorted(classes, key=lambda c: sorted(c)):
            if C in cseen:
                continue
            o = {frozenset(img(g, b) for b in C) for g in RG}
            assert o <= cset
            cseen |= o; creps.append((sorted(C), len(o)))
        assert cseen == cset
        lines.append(f"## {name}")
        lines.append(f"Block set = union of {Kname}-orbits (|K|={len(KG)}) of the {len(breps)} representatives "
                     f"(orbit length in brackets):")
        lines.append("")
        lines.append("; ".join("{" + ",".join(pt(p) for p in b) + f"}}[{s}]" for b, s in breps))
        lines.append("")
        lines.append(f"Resolution = all {Rname}-images (|R|={len(RG)}) of the following {len(creps)} classes "
                     f"(orbit length in brackets):")
        lines.append("")
        for k, (C, s) in enumerate(creps):
            lines.append(f"* C{k} [{s}]: " + " ".join("{" + ",".join(pt(p) for p in b) + "}" for b in C))
        lines.append("")
    open(out, "w").write("\n".join(lines) + "\n")
    print("wrote", out, "bases", len(seed["bases"]))


if __name__ == "__main__":
    main()
