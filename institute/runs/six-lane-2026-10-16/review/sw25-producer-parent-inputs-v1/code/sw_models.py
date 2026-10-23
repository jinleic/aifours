#!/usr/bin/env python3
"""Model specs (signed permutation groups acting on SW(n,w) by W -> H W H^T) for lane sw25-16.

Usage: python3 -B code/sw_models.py KIND ARGS... OUT.spec.json
  trivial N W                 G = 1
  cyc N W R F                 one unsigned permutation of cycle type R^S 1^F (cycles first: points R*t..R*t+R-1
                              map u -> u+1 inside each cycle; fixed points R*S..N-1)
  inv N W A B C               involution: C plain swaps (2t <-> 2t+1, t < C), then A fixed points with sign +1,
                              then B fixed points with sign -1
  gens N W JSONFILE           generators given explicitly as [{"perm": [...], "sign": [...]}, ...]
A generator H is (perm, sign) with H e_j = sign[j] e_{perm[j]}; invariance is W[perm i][perm j] = sign i sign j W[i][j].
The spec file is written with mode x; its sha256 is printed.
"""
import hashlib
import json
import sys


def check_gen(n, g):
    p, s = g["perm"], g["sign"]
    assert sorted(p) == list(range(n)), "perm is not a permutation"
    assert len(s) == n and all(x in (1, -1) for x in s), "bad signs"


def order_of(n, g):
    p, s = g["perm"], g["sign"]
    cur_p, cur_s = list(range(n)), [1] * n
    for k in range(1, 10 * n + 2):
        # compose H^k = H o H^(k-1): j -> p[cur_p[j]] with sign cur_s[j] * s[cur_p[j]]
        cur_s = [cur_s[j] * s[cur_p[j]] for j in range(n)]
        cur_p = [p[cur_p[j]] for j in range(n)]
        if cur_p == list(range(n)) and all(x == 1 for x in cur_s):
            return k
    raise ValueError("order not found")


def build(argv):
    kind = argv[0]
    if kind == "trivial":
        n, w = int(argv[1]), int(argv[2])
        return {"name": f"trivial-n{n}", "n": n, "w": w, "generators": []}
    if kind == "cyc":
        n, w, r, f = map(int, argv[1:5])
        s = (n - f) // r
        assert r * s + f == n
        perm = list(range(n))
        for t in range(s):
            for u in range(r):
                perm[r * t + u] = r * t + (u + 1) % r
        g = {"perm": perm, "sign": [1] * n}
        return {"name": f"cyc-n{n}-r{r}-f{f}", "n": n, "w": w, "generators": [g],
                "description": f"unsigned permutation of cycle type {r}^{s} 1^{f}"}
    if kind == "inv":
        n, w, a, b, c = map(int, argv[1:6])
        assert a + b + 2 * c == n
        perm = list(range(n))
        sign = [1] * n
        for t in range(c):
            perm[2 * t], perm[2 * t + 1] = 2 * t + 1, 2 * t
        for k in range(2 * c + a, n):
            sign[k] = -1
        g = {"perm": perm, "sign": sign}
        return {"name": f"inv-n{n}-a{a}-b{b}-c{c}", "n": n, "w": w, "generators": [g],
                "description": f"involution: {c} plain swaps, {a} fixed points sign +1, {b} fixed points sign -1"}
    if kind == "gens":
        n, w = int(argv[1]), int(argv[2])
        gens = json.load(open(argv[3]))
        return {"name": f"gens-n{n}-" + argv[3].split("/")[-1].replace(".json", ""), "n": n, "w": w,
                "generators": gens}
    raise ValueError(kind)


def main():
    spec = build(sys.argv[1:-1])
    for g in spec["generators"]:
        check_gen(spec["n"], g)
    spec["generator_orders"] = [order_of(spec["n"], g) for g in spec["generators"]]
    text = json.dumps(spec, indent=1) + "\n"
    with open(sys.argv[-1], "x") as f:
        f.write(text)
    print(spec["name"], spec["generator_orders"], hashlib.sha256(text.encode()).hexdigest())


if __name__ == "__main__":
    main()
