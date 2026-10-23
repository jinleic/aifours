#!/usr/bin/env python3
"""e_combos.py -- A-patterns containing at least one full-support e7 or e8 component (README 1.4(a); exploratory).

Reads E.json from code/e_multisets.py.  An A-pattern here is: one or two full-support e-components (e7 on 7 columns
needs every point degree in {2,4,6}; e8 on 8 columns likewise), placed on disjoint column blocks from column 0, plus a
d-type part: a multigraph with the remaining number of edges (12 minus the e-rows), all degrees in {2,4,6}, from
nauty `geng -q -d1 -D6 n 1:e | multig -q -e<e> -D6 -T` for every n with 2n <= remaining columns (vertex v -> the next
two unused columns).  Columns not covered are free.  Writes OUT.jsonl (exclusive), one JSON line per A-pattern
{"name", "rows"}.  Usage: e_combos.py E.json OUT.jsonl
"""
import json
import subprocess
import sys

B, V = 20, 12


def multigraphs(e, nmax):
    """all multigraphs with exactly e edges, n <= nmax non-isolated vertices, degrees in {2,4,6} (nauty)."""
    if e == 0:
        return [(0, [])]
    out = []
    for n in range(2, nmax + 1):
        lo = max(1, (n + 1) // 2)
        if e < lo:
            continue
        g = subprocess.run(["geng", "-q", "-d1", "-D6", str(n), f"{lo}:{e}"], capture_output=True, check=True)
        mg = subprocess.run(["multig", "-q", f"-e{e}", "-D6", "-T"], input=g.stdout, capture_output=True, check=True)
        for line in mg.stdout.decode().splitlines():
            t = line.split()
            if not t:
                continue
            nv, ne = int(t[0]), int(t[1])
            edges = []
            deg = [0] * nv
            for q in range(ne):
                u, v, mu = int(t[2 + 3 * q]), int(t[3 + 3 * q]), int(t[4 + 3 * q])
                edges += [(u, v)] * mu
                deg[u] += mu
                deg[v] += mu
            if len(edges) == e and all(d in (2, 4, 6) for d in deg):
                out.append((nv, edges))
    return out


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    E = json.load(open(argv[1]))
    comps = []
    for name in ("e7", "e8"):
        tets = E[name]["tetrads"]
        npts = E[name]["points"]
        for idx, ms in enumerate(E[name]["multisets"]):
            if ms["support"] != npts:
                continue
            rows = []
            for t, mu in zip(tets, ms["mult"]):
                rows += [list(t)] * mu
            comps.append((f"{name}#{idx}", npts, rows))
    print("full-support e-components:", len(comps), file=sys.stderr)
    cache = {}
    n_out = 0
    with open(argv[2], "x") as f:
        choices = [[c] for c in comps] + [[comps[i], comps[j]] for i in range(len(comps)) for j in range(i, len(comps))]
        for ch in choices:
            ncols = sum(c[1] for c in ch)
            nrows = sum(len(c[2]) for c in ch)
            if ncols > B or nrows > V:
                continue
            e = V - nrows
            nmax = (B - ncols) // 2
            key = (e, nmax)
            if key not in cache:
                cache[key] = multigraphs(e, nmax)
            base, off = [], 0
            for c in ch:
                base += [[off + x for x in r] for r in c[2]]
                off += c[1]
            for nv, edges in cache[key]:
                rows = base + [[off + 2 * u, off + 2 * u + 1, off + 2 * v, off + 2 * v + 1] for (u, v) in edges]
                assert len(rows) == V and max(max(r) for r in rows) < B
                name = "+".join(c[0] for c in ch) + f"+mg(n={nv},e={e},{edges})"
                f.write(json.dumps({"name": name, "rows": rows}) + "\n")
                n_out += 1
    print("A-patterns written:", n_out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
