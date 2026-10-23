#!/usr/bin/env python3
"""enum_crosscheck.py -- independent recount of the case list of notes/case-split-r1.md Part C (stdlib + nauty genbg).

(1) Multigraphs.  A loopless multigraph with n vertices (no isolated vertex) and e edges is the same, up to isomorphism,
    as a bicoloured graph with n "vertex nodes" and e "edge nodes" of degree exactly 2 (parallel edges = edge nodes
    with equal neighbourhoods), up to colour-preserving isomorphism.  nauty `genbg -q -d2:2 -D6:2 n e 2e:2e` lists
    those with vertex-node degrees 2..6; keep vertex-node degrees in {2,4,6}.  This is a different nauty generator
    (genbg) from the geng | multig pipeline used for the case list; the counts must agree for every (n, e) used.
(2) e-multisets.  Burnside: the number of orbits of valid multiplicity vectors (all point degrees in {0,2,4,6},
    total in [1,12]) under the tetrad group equals (1/|G|) sum_g Fix(g); likewise for the full-support vectors.  Fix(g)
    is counted directly as the number of valid vectors constant on the cycles of g (a recursion over the cycles of g,
    not the orbit-marking search of code/e_multisets.py); the group itself is taken from code/e_multisets.py.
(3) The number of E1 patterns is recomputed from (1) and (2) as sum over e-part choices of the number of d-parts.
Usage: enum_crosscheck.py E.json OUT.json   (E.json from code/e_multisets.py; OUT exclusive)
"""
import json
import subprocess
import sys


def g6_decode(s):
    s = s.strip()
    data = [ord(c) - 63 for c in s]
    if data[0] < 63:
        n, pos = data[0], 1
    else:
        n, pos = (data[1] << 12) | (data[2] << 6) | data[3], 4
    bits = []
    for x in data[pos:]:
        for k in range(5, -1, -1):
            bits.append((x >> k) & 1)
    adj = [[0] * n for _ in range(n)]
    t = 0
    for j in range(1, n):
        for i in range(j):
            if bits[t]:
                adj[i][j] = adj[j][i] = 1
            t += 1
    return n, adj


def genbg_count(n, e):
    if e == 0 or not (2 * n <= 2 * e <= 6 * n):  # vertex-node degrees in [2, 6] sum to 2e
        return 0
    p = subprocess.run(["genbg", "-q", "-d2:2", "-D6:2", str(n), str(e), f"{2 * e}:{2 * e}"], capture_output=True,
                       check=True, text=True)
    c = 0
    for line in p.stdout.splitlines():
        if not line.strip():
            continue
        N, adj = g6_decode(line)
        assert N == n + e
        degs = [sum(adj[v]) for v in range(n)]
        assert all(sum(adj[n + q][:n]) == 2 for q in range(e)) and sum(degs) == 2 * e
        if all(dg in (2, 4, 6) for dg in degs):
            c += 1
    return c


def geng_multig_count(n, e):
    lo = max(1, (n + 1) // 2)
    if e < lo:
        return 0
    g = subprocess.run(["geng", "-q", "-d1", "-D6", str(n), f"{lo}:{e}"], capture_output=True, check=True)
    m = subprocess.run(["multig", "-q", f"-e{e}", "-D6", "-T"], input=g.stdout, capture_output=True, check=True)
    c = 0
    for line in m.stdout.decode().splitlines():
        t = line.split()
        if not t:
            continue
        nv, ne = int(t[0]), int(t[1])
        deg = [0] * nv
        tot = 0
        for q in range(ne):
            u, v, mu = int(t[2 + 3 * q]), int(t[3 + 3 * q]), int(t[4 + 3 * q])
            deg[u] += mu
            deg[v] += mu
            tot += mu
        if tot == e and all(dg in (2, 4, 6) for dg in deg):
            c += 1
    return c


def burnside(npts, tets, G):
    """Burnside counts of valid / full-support valid multiplicity vectors: for each group element g, count the vectors
    constant on the cycles of g (exactly the vectors fixed by g) by direct recursion over the cycles."""
    nt = len(tets)
    inc = [[1 if p in t else 0 for p in range(npts)] for t in tets]
    fix_all = fix_full = 0
    n_valid = n_full = None
    for g in G:
        seen, cycles = set(), []
        for s in range(nt):
            if s in seen:
                continue
            cyc, x = [], s
            while x not in seen:
                seen.add(x)
                cyc.append(x)
                x = g[x]
            cycles.append(cyc)
        cdeg = [[sum(inc[s][p] for s in cyc) for p in range(npts)] for cyc in cycles]
        clen = [len(c) for c in cycles]
        cnt = [0, 0]
        deg = [0] * npts

        def rec(ci, total):
            if ci == len(cycles):
                if total >= 1 and all(dg in (0, 2, 4, 6) for dg in deg):
                    cnt[0] += 1
                    if all(dg > 0 for dg in deg):
                        cnt[1] += 1
                return
            c = 0
            while True:
                rec(ci + 1, total + c * clen[ci])
                c += 1
                if total + c * clen[ci] > 12 or any(deg[p] + cdeg[ci][p] > 6 for p in range(npts)):
                    c -= 1
                    break
                for p in range(npts):
                    deg[p] += cdeg[ci][p]
            for p in range(npts):
                deg[p] -= c * cdeg[ci][p]

        rec(0, 0)
        fix_all += cnt[0]
        fix_full += cnt[1]
        if all(g[s] == s for s in range(nt)):
            n_valid, n_full = cnt
    assert fix_all % len(G) == 0 and fix_full % len(G) == 0
    return n_valid, fix_all // len(G), n_full, fix_full // len(G), None


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    E = json.load(open(argv[1]))
    rep, ok = {"multigraphs": {}, "e": {}}, True
    needed = {(n, 12) for n in range(4, 11)}
    # e-part choices (as in code/e_combos.py): full-support e7 / e8 representatives, singles and unordered pairs
    comps = []
    for name in ("e7", "e8"):
        for ms in E[name]["multisets"]:
            if ms["support"] == E[name]["points"]:
                comps.append((name, E[name]["points"], ms["rows"]))
    choices = [[c] for c in comps] + [[comps[i], comps[j]] for i in range(len(comps)) for j in range(i, len(comps))]
    plan = []
    for ch in choices:
        ncols, nrows = sum(c[1] for c in ch), sum(c[2] for c in ch)
        if ncols > 20 or nrows > 12:
            continue
        e, nmax = 12 - nrows, (20 - ncols) // 2
        plan.append((e, nmax))
        for n in range(2, nmax + 1):
            if e > 0:
                needed.add((n, e))
    for (n, e) in sorted(needed):
        a, b = genbg_count(n, e), geng_multig_count(n, e)
        rep["multigraphs"][f"n={n},e={e}"] = {"genbg": a, "geng_multig": b}
        ok &= a == b
    # (2) Burnside for the e-multisets
    import importlib.util
    spec = importlib.util.spec_from_file_location("e_multisets", __file__.replace("enum_crosscheck.py", "e_multisets.py"))
    em = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(em)
    for name, npts, tets in (("e7", 7, em.e7_tetrads()), ("e8", 8, em.e8_tetrads())):
        G = em.group_on_tetrads(npts, tets)
        nv, no, nvf, nof, _ = burnside(npts, tets, G)
        listed = len(E[name]["multisets"])
        listed_full = sum(1 for ms in E[name]["multisets"] if ms["support"] == npts)
        rep["e"][name] = {"group_order": len(G), "valid_vectors": nv, "burnside_orbits": no, "listed": listed,
                          "valid_full_vectors": nvf, "burnside_full_orbits": nof, "listed_full": listed_full}
        ok &= no == listed and nof == listed_full
    # (3) E1 total
    total = 0
    for e, nmax in plan:
        total += 1 if e == 0 else sum(rep["multigraphs"][f"n={n},e={e}"]["genbg"] for n in range(2, nmax + 1)
                                      if f"n={n},e={e}" in rep["multigraphs"])
    rep["E1_recount"] = total
    rep["E0_recount"] = sum(rep["multigraphs"][f"n={n},e=12"]["genbg"] for n in range(4, 11))
    rep["all_pass"] = ok
    with open(argv[2], "x") as f:
        json.dump(rep, f, indent=1)
    print(json.dumps({k: rep[k] for k in ("E0_recount", "E1_recount", "all_pass")}), json.dumps(rep["e"]))
    print("ENUM-CROSSCHECK", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
