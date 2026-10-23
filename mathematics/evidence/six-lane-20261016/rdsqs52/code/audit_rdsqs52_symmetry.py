#!/usr/bin/env python3
"""Exact symmetry audit of a cyclic RDSQS certificate (standard library only; reads the
certificate directly, imports nothing from the search code).

Checks and reports:
 1. the translation t: x -> x+1 and the multiplier m: x -> M*x (mod v) map the block set onto
    itself (generator images of every block);
 2. the multiplier group <M> and its order; block-orbit counts under Z_v and under Z_v x| <M>;
 3. the resolution at 0 is invariant (as a set of classes) under every element of <M>;
 4. for every x, the resolution listed at POINT x equals, as a set of classes, the translate
    by x of the resolution at 0, and equals g(resolution at 0) for the least g in
    G = {y -> m*y + b} (tuples ordered lexicographically) with g(0) = x — the pipeline's rule;
 5. the class structure at 0: orbits of <M> on the 25 classes.
Usage: audit_rdsqs52_symmetry.py CERT M OUT.json
"""
import hashlib
import json
import sys


def parse(path):
    v, blocks, res, cur = None, [], {}, None
    for raw in open(path):
        s = raw.split("#")[0].strip()
        if not s:
            continue
        t = s.split()
        if t[0] == "RDSQS":
            v = int(t[1])
        elif t[0] == "BLOCKS":
            continue
        elif t[0] == "POINT":
            cur = int(t[1]); res[cur] = []
        elif t[0] == "CLASS":
            res[cur].append([])
        elif cur is None:
            blocks.append(tuple(sorted(map(int, t))))
        else:
            res[cur][-1].append(tuple(sorted(map(int, t))))
    return v, blocks, res


def main():
    cert, M, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    v, blocks, res = parse(cert)
    B = set(blocks)
    img = lambda f, b: tuple(sorted(f(p) for p in b))
    tr = lambda p: (p + 1) % v
    mu = lambda p: (M * p) % v
    r = {"certificate": cert, "certificate_sha256": hashlib.sha256(open(cert, "rb").read()).hexdigest(),
         "v": v, "multiplier": M, "blocks": len(B)}
    r["translation_preserves_blocks"] = all(img(tr, b) in B for b in B)
    r["multiplier_preserves_blocks"] = all(img(mu, b) in B for b in B)
    grp, x = [], 1
    while True:
        grp.append(x); x = x * M % v
        if x == 1:
            break
    r["multiplier_group"] = sorted(grp)
    # orbit counts
    def orbits(funcs):
        seen, n, sizes = set(), 0, {}
        for b in sorted(B):
            if b in seen:
                continue
            orb, stack = {b}, [b]
            while stack:
                c = stack.pop()
                for f in funcs:
                    d = img(f, c)
                    if d not in orb:
                        orb.add(d); stack.append(d)
            seen |= orb; n += 1
            sizes[len(orb)] = sizes.get(len(orb), 0) + 1
        return n, dict(sorted(sizes.items()))
    r["block_orbits_Zv"] = orbits([tr])
    r["block_orbits_Zv_x_M"] = orbits([tr, mu])
    cls0 = [frozenset(C) for C in res[0]]
    set0 = set(cls0)
    r["res0_invariant_under_M"] = all({frozenset(img(lambda p, m=m: (m * p) % v, t) for t in C) for C in cls0} == set0
                                    for m in grp)
    # class orbits of <M> at 0
    seen, corb = set(), []
    for C in cls0:
        if C in seen:
            continue
        o = {frozenset(img(lambda p, m=m: (m * p) % v, t) for t in C) for m in grp}
        seen |= o; corb.append(len(o))
    r["class_orbit_sizes_at_0"] = sorted(corb)
    G = sorted(tuple((m * y + b) % v for y in range(v)) for m in grp for b in range(v))
    ok_tr, ok_rule = True, True
    for xx in range(v):
        listed = {frozenset(C) for C in res[xx]}
        trans = {frozenset(img(lambda p: (p + xx) % v, t) for t in C) for C in cls0}
        g = next(g for g in G if g[0] == xx)
        rule = [sorted(img(lambda p, g=g: g[p], t) for t in C) for C in res[0]]
        if listed != trans:
            ok_tr = False
        if [sorted(C) for C in res[xx]] != rule:
            ok_rule = False
    r["every_resolution_is_translate_of_res0_as_set"] = ok_tr
    r["every_resolution_equals_pipeline_transport_rule_in_order"] = ok_rule
    r["result"] = "PASS" if all(r[k] for k in ("translation_preserves_blocks", "multiplier_preserves_blocks",
                                              "res0_invariant_under_M", "every_resolution_is_translate_of_res0_as_set",
                                              "every_resolution_equals_pipeline_transport_rule_in_order")) else "FAIL"
    json.dump(r, open(out, "w"), indent=1)
    print(json.dumps(r, indent=1))


if __name__ == "__main__":
    main()
