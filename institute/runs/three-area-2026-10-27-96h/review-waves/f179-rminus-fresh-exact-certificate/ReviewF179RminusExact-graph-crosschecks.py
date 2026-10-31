#!/usr/bin/env python3
"""ReviewF179RminusExact: graph cross-checks of the reviewer's Fig. 2 transcription against
two further printed source statements (exact, integer):
  (1) publisher Appendix B: Aut(R^L) = Aut(R) = <(25)(36)(47), (26)(35)(8 10), (24)(57)(89)>,
      with R = R^- + edge 9-10 (publisher p569 / BCDRV Section 6);
  (2) BCDRV Lemma 6.1 proof: the ten weight-1/3 cliques of an optimal fractional clique cover
      of R^- must be cliques of R^- covering every vertex exactly three times.
"""
import json
import sys

E = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 7), (2, 9), (2, 10),
     (3, 4), (3, 8), (3, 9), (4, 5), (4, 8), (4, 10), (5, 6), (5, 9), (5, 10), (6, 7),
     (6, 8), (6, 9), (7, 8), (7, 10), (8, 9), (8, 10)]
RM = set(tuple(sorted(e)) for e in E)
R = RM | {(9, 10)}
GENS_R = [[(2, 5), (3, 6), (4, 7)], [(2, 6), (3, 5), (8, 10)], [(2, 4), (5, 7), (8, 9)]]
TRI = [{1, 2, 3}, {1, 4, 5}, {1, 6, 7}, {2, 3, 9}, {2, 7, 10}, {3, 8, 9}, {4, 5, 10}, {4, 8, 10},
       {5, 6, 9}, {6, 7, 8}]


def perm(cycles):
    p = {v: v for v in range(1, 11)}
    for c in cycles:
        for k, v in enumerate(c):
            p[v] = c[(k + 1) % len(c)]
    return p


def is_aut(p, es):
    return set(tuple(sorted((p[a], p[b]))) for a, b in es) == es


def aut_order(es):
    nbr = {v: set() for v in range(1, 11)}
    for a, b in es:
        nbr[a].add(b)
        nbr[b].add(a)
    order = sorted(range(1, 11), key=lambda v: -len(nbr[v]))
    cnt = [0]

    def bt(k, m, used):
        if k == 10:
            cnt[0] += 1
            return
        v = order[k]
        for w in range(1, 11):
            if w in used or len(nbr[w]) != len(nbr[v]):
                continue
            if all((u in nbr[v]) == (m[u] in nbr[w]) for u in m):
                m[v] = w
                used.add(w)
                bt(k + 1, m, used)
                used.discard(w)
                del m[v]
    bt(0, {}, set())
    return cnt[0]


def main():
    out = {"aut_R_generators_are_automorphisms_of_R": [is_aut(perm(g), R) for g in GENS_R],
           "aut_R_order_backtracking": aut_order(R),
           "aut_Rminus_order_backtracking": aut_order(RM),
           "bcdrv_triangles_are_cliques": all(tuple(sorted((a, b))) in RM for t in TRI for a in t for b in t if a < b),
           "bcdrv_cover_multiplicity": sorted({v: sum(v in t for t in TRI) for v in range(1, 11)}.items()),
           "edges_not_in_bcdrv_triangles": sorted(RM - {tuple(sorted((a, b))) for t in TRI for a in t for b in t if a < b})}
    ok = all(out["aut_R_generators_are_automorphisms_of_R"]) and out["bcdrv_triangles_are_cliques"] and \
        all(m == 3 for _, m in out["bcdrv_cover_multiplicity"])
    out["pass"] = ok
    print(json.dumps(out, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
