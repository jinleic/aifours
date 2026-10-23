#!/usr/bin/env python3
"""find_nets.py: collect representatives of the isomorphism classes of 4-nets of order 7 (= paratopism classes of
2-MOLS(7)). Lane moqls7-maximum (stdlib only, plus the C helper code/net_canon).

Method: random Latin squares L of order 7 (randomised row-by-row completion), all orthogonal mates of L (all
transversals, then every partition of the 49 cells into 7 disjoint transversals), nets (rows, cols, L, M), then the
canonical key and |par| from code/net_canon. The two Desarguesian 4-nets (harmonic, equianharmonic) are added
directly. Source binding: Egan–Wanless Table 6 gives 7 classes with 342480 reduced lists in total, and Table 5 gives 5
maximal classes with 341880. By their Theorem 3.2 each class contributes 846720/|par|, so the search is complete for
our purposes when the collected classes reach these totals.

Usage: find_nets.py OUT.json [--max-squares N] [--seed S]
"""
import argparse
import json
import os
import random
import subprocess
import sys

import nets

HERE = os.path.dirname(os.path.abspath(__file__))
P = 7


def random_latin(rng):
    while True:
        L = []
        ok = True
        for r in range(P):
            cols_used = [set(L[i][c] for i in range(r)) for c in range(P)]
            row = [None] * P

            def bt(c, used):
                if c == P:
                    return True
                cand = [a for a in range(P) if a not in used and a not in cols_used[c]]
                rng.shuffle(cand)
                for a in cand:
                    row[c] = a
                    used.add(a)
                    if bt(c + 1, used):
                        return True
                    used.discard(a)
                return False
            if not bt(0, set()):
                ok = False
                break
            L.append(row[:])
        if ok:
            return L


def transversals(L):
    out = []

    def bt(r, usedc, useds, cur):
        if r == P:
            out.append(tuple(cur))
            return
        for c in range(P):
            if c in usedc or L[r][c] in useds:
                continue
            usedc.add(c)
            useds.add(L[r][c])
            cur.append(c)
            bt(r + 1, usedc, useds, cur)
            cur.pop()
            usedc.discard(c)
            useds.discard(L[r][c])
    bt(0, set(), set(), [])
    return out          # transversal t: t[r] = column in row r


def mates(L, limit=10000):
    T = transversals(L)
    masks = [sum(1 << (P * r + t[r]) for r in range(P)) for t in T]
    by_cell0 = [i for i, t in enumerate(T) if t[0] == 0]
    sols = []

    def cover(used, chosen):
        if len(sols) >= limit:
            return
        if len(chosen) == P:
            sols.append(list(chosen))
            return
        first = next(q for q in range(P * P) if not used >> q & 1)
        r0, c0 = divmod(first, P)
        for i, t in enumerate(T):
            if t[r0] == c0 and not masks[i] & used:
                chosen.append(i)
                cover(used | masks[i], chosen)
                chosen.pop()
    cover(0, [])
    out = []
    for s in sols:
        M = [[None] * P for _ in range(P)]
        for sym, i in enumerate(s):
            for r in range(P):
                M[r][T[i][r]] = sym
        out.append(M)
    return out, len(T)


def canon(netlist):
    exe = os.path.join(HERE, "net_canon")
    data = "".join(" ".join(str(v) for q in net for v in q) + "\n" for net in netlist)
    p = subprocess.run([exe], input=data, capture_output=True, text=True)
    res = []
    for line in p.stdout.splitlines():
        k, d, par, ex = line.split()
        res.append((k, int(d), int(par), ex == "1"))
    return res


def common_transversal_count_and_maximal(net):
    """Transversals of the 4-net and whether 7 disjoint ones exist (a 5th parallel class)."""
    L = [[net[P * r + c][2] for c in range(P)] for r in range(P)]
    M = [[net[P * r + c][3] for c in range(P)] for r in range(P)]
    T = [t for t in transversals(L) if len({M[r][t[r]] for r in range(P)}) == P]
    masks = [sum(1 << (P * r + t[r]) for r in range(P)) for t in T]
    found = [False]

    def cover(used, k):
        if found[0]:
            return
        if k == P:
            found[0] = True
            return
        first = next(q for q in range(P * P) if not used >> q & 1)
        r0, c0 = divmod(first, P)
        for i, t in enumerate(T):
            if t[r0] == c0 and not masks[i] & used:
                cover(used | masks[i], k + 1)
    cover(0, 0)
    return len(T), not found[0]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--max-squares", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=20261017)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    classes = {}
    cand = [("desarguesian-harmonic", nets.desarguesian_net(["inf", 0, 1, 2])),
            ("desarguesian-equianharmonic", nets.desarguesian_net(["inf", 0, 1, 3]))]
    # cyclic nets: L1(r,c) = c + r, L2(r,c) = c + a(r) for every orthomorphism a of Z_7 with a(0) = 0
    import itertools
    for a_ in itertools.permutations(range(P)):
        if a_[0] == 0 and len({(a_[r] - r) % P for r in range(P)}) == P:
            cand.append(("cyclic orthomorphism %s" % (a_,),
                         nets.net_from_mols([[(c + r) % P for c in range(P)] for r in range(P)],
                                            [[(c + a_[r]) % P for c in range(P)] for r in range(P)])))
    for name, net in cand:
        (k, d, par, ex), = canon([net])
        if k in classes:
            continue
        nt, mx = common_transversal_count_and_maximal(net)
        classes[k] = {"origin": name, "orbit": d, "par": par, "par_exact": ex, "transversals": nt, "maximal": mx,
                      "net": net}
    tried = 0
    with_mates = 0
    while tried < a.max_squares:
        tried += 1
        L = random_latin(rng)
        Ms, nT = mates(L, limit=200)
        if not Ms:
            continue
        with_mates += 1
        netlist = [nets.net_from_mols(L, M) for M in Ms]
        for net, (k, d, par, ex) in zip(netlist, canon(netlist)):
            if k not in classes:
                nt, mx = common_transversal_count_and_maximal(net)
                classes[k] = {"origin": "random square %d" % tried, "orbit": d, "par": par, "par_exact": ex,
                              "transversals": nt, "maximal": mx, "net": net}
                print(json.dumps({k2: v for k2, v in classes[k].items() if k2 != "net"}), flush=True)
        tot = sum(c["orbit"] for c in classes.values())
        totmax = sum(c["orbit"] for c in classes.values() if c["maximal"])
        if tot == 342480 and totmax == 341880:
            break
    tot = sum(c["orbit"] for c in classes.values())
    totmax = sum(c["orbit"] for c in classes.values() if c["maximal"])
    summary = {"squares_tried": tried, "squares_with_mates": with_mates, "classes": len(classes),
               "sum_orbits": tot, "sum_orbits_maximal": totmax,
               "egan_wanless_table6_total_342480": tot == 342480, "egan_wanless_table5_maximal_341880": totmax == 341880}
    out = {"summary": summary, "classes": [{"key": k, **v} for k, v in sorted(classes.items())]}
    with open(a.out, "w") as fh:
        json.dump(out, fh)
    print(json.dumps(summary))
