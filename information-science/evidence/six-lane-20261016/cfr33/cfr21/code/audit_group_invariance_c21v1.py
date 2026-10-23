#!/usr/bin/env python3
"""Audit: is the column multiset of a (Z_n, k; 1)-DM invariant under given maps? (lane cfr33/cfr27, InfoCFR27Lift)

Usage: audit_group_invariance_v1.py DMRAW K N SPEC.json CONTROLS.json OUT.json      (OUT written with mode 'x')
The claim audited is COLUMN-MULTISET invariance of the DM, not an isotopy of CFR rows.
A column c = (c_0, ..., c_{k-1}) is taken modulo constants (normalised c - c_0). A map s = (mu, pi[, t]) with pi[i] the
image of row i acts by (s c)_{pi[i]} = mu * c_i + t_{pi[i]} (equivalently (s c)_x = mu c_{pi^-1(x)} + t_x), the
convention of code/dm_orbit_cnf.py and dmorbit_compile_v1/v2. For every generator of SPEC (expected: invariant) and every
element of CONTROLS (expected: NOT invariant) the multiset of normalised images is compared with the multiset of
normalised columns. Also re-checks the DM property and reports orbit sizes under the generated group.
Written separately from the solver (no shared code). Exit 0 iff every expectation holds.
"""
import hashlib, json, sys
from collections import Counter


def main():
    path, k, n, specp, ctrlp, outp = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6]
    raw = open(path, "rb").read()
    lines = raw.decode("ascii").split("\n")
    assert lines[-1] == "" and len(lines) == k + 1, "expected k LF-terminated lines"
    D = [[int(x) for x in ln.split(" ")] for ln in lines[:k]]
    assert all(len(r) == n and all(0 <= x < n for x in r) for r in D)
    dm_ok = all(len({(D[i][c] - D[j][c]) % n for c in range(n)}) == n for i in range(k) for j in range(i + 1, k))
    cols = [tuple(D[i][c] for i in range(k)) for c in range(n)]

    def normc(c):
        return tuple((x - c[0]) % n for x in c)

    def act(s, c):
        mu, pi = s[0] % n, s[1]
        t = s[2] if len(s) > 2 else [0] * k
        out = [None] * k
        for i in range(k):
            out[pi[i]] = (mu * c[i] + t[pi[i]]) % n
        return normc(tuple(out))

    base = Counter(normc(c) for c in cols)

    def invariant(s):
        assert sorted(s[1]) == list(range(k)), "not a permutation"
        return Counter(act(s, c) for c in base.elements()) == base

    spec = json.load(open(specp))
    controls = json.load(open(ctrlp))
    res = {"dmraw": path, "dmraw_sha256": hashlib.sha256(raw).hexdigest(), "spec": specp,
           "spec_sha256": hashlib.sha256(open(specp, "rb").read()).hexdigest(), "dm_property": dm_ok,
           "distinct_normalised_columns": len(base), "generators": [], "controls": []}
    ok = dm_ok and len(base) == n
    for g in spec["gens"]:
        inv = invariant(g)
        res["generators"].append({"element": g, "invariant": inv})
        ok &= inv
    for g in controls:
        inv = invariant(g)
        res["controls"].append({"element": g, "invariant": inv, "expected": False})
        ok &= not inv
    # orbit sizes under the generated group (closure on the column set)
    seen, sizes = set(), []
    for c in base:
        if c in seen:
            continue
        orb, frontier = {c}, [c]
        while frontier:
            new = []
            for x in frontier:
                for g in spec["gens"]:
                    y = act(g, x)
                    if y not in orb:
                        orb.add(y)
                        new.append(y)
            frontier = new
        seen |= orb
        sizes.append(len(orb))
    res["orbit_sizes"] = sorted(sizes)
    res["all_as_expected"] = bool(ok)
    with open(outp, "x") as fh:
        json.dump(res, fh, indent=1)
    print("AUDIT", "PASS" if ok else "FAIL", json.dumps({"dm": dm_ok, "gens": [x["invariant"] for x in res["generators"]],
                                                          "controls": [x["invariant"] for x in res["controls"]], "orbits": res["orbit_sizes"]}))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
