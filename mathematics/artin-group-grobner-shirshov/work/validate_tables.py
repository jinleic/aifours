"""Exact (integer) validation of the numerically generated Coxeter-group tables.

coxeter.py builds roots in floating point and identifies them by rounding; the
resulting permutation tables are then checked here with integer arithmetic only,
for EVERY generator labelling (order) used in the growth classification:
  (1) the generators are involutions and satisfy the braid relations
      (so the permutation group is a quotient of W), and the group order equals
      the known |W| (so it is W);
  (2) |Phi^+| equals the known N;
  (3) the root-count length of every element equals its breadth-first distance
      from 1 in the Cayley graph (= Coxeter length);
  (4) left/right descent bitmasks agree with the BFS distances;
  (5) the prefix-order test leq(a,b) (inclusion of inversion sets, used for
      right complements and joins) agrees with the combinatorial definition
      "b is reachable from a by length-increasing right multiplications":
      exhaustively for |W| <= 2000; for H4 on 300 random a (all b) per labelling
      (the second independent review checked all 207,360,000 H4 pairs of the
      default labelling exhaustively, evidence/codex-review2.md);
  (6) w0 is the unique element of length N.
Usage: python3 work/validate_tables.py > evidence/validate_tables.json
"""
import json
import random
import sys
from itertools import permutations

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from automaton import build_table  # noqa: E402

ORDERS = {("A", 3): 24, ("A", 4): 120, ("B", 3): 48, ("B", 4): 384, ("D", 4): 192,
          ("F", 4): 1152, ("H", 3): 120, ("H", 4): 14400}
NPOS = {("A", 3): 6, ("A", 4): 10, ("B", 3): 9, ("B", 4): 16, ("D", 4): 12, ("F", 4): 24,
        ("H", 3): 15, ("H", 4): 60}


def validate(typ, n, m=0, order=None):
    T = build_table(typ, n, m, order)
    key = (typ, n) if typ != "I" else None
    expect = ORDERS[key] if key else 2 * m
    npos = NPOS[key] if key else m
    rep = {"type": typ, "n": n, "m": m, "order": order, "size": T.size, "expected_size": expect}
    ok = T.size == expect and T.W.N == npos
    # (1) relations
    for i in range(T.n):
        ok &= all(T.rmul[T.rmul[w][i]][i] == w for w in range(T.size))
        for j in range(i + 1, T.n):
            ok &= T.alt(i, j, T.M[i][j]) == T.alt(j, i, T.M[i][j])
    # (3) BFS distances
    dist = [-1] * T.size
    dist[T.e] = 0
    frontier = [T.e]
    while frontier:
        nxt = []
        for w in frontier:
            for i in range(T.n):
                v = T.rmul[w][i]
                if dist[v] < 0:
                    dist[v] = dist[w] + 1
                    nxt.append(v)
        frontier = nxt
    ok &= all(dist[w] == T.length[w] for w in range(T.size))
    # (4) descents
    for w in range(T.size):
        rd = sum(1 << i for i in range(T.n) if dist[T.rmul[w][i]] < dist[w])
        ld = sum(1 << i for i in range(T.n) if dist[T.lmul[i][w]] < dist[w])
        ok &= rd == T.rd[w] and ld == T.ld[w]
    # (5) prefix order
    rng = random.Random(0)
    sample = range(T.size) if T.size <= 2000 else [rng.randrange(T.size) for _ in range(300)]
    checked = 0
    for a in sample:
        up = {a}
        frontier = [a]
        while frontier:
            nxt = []
            for w in frontier:
                for i in range(T.n):
                    v = T.rmul[w][i]
                    if dist[v] == dist[w] + 1 and v not in up:
                        up.add(v)
                        nxt.append(v)
            frontier = nxt
        for b in range(T.size):
            ok &= T.leq(a, b) == (b in up)
            checked += 1
    # (6) w0
    ok &= [w for w in range(T.size) if dist[w] == T.W.N] == [T.w0]
    rep.update({"N": T.W.N, "leq_pairs_checked": checked,
                "leq_exhaustive": T.size <= 2000, "ok": bool(ok)})
    return rep


if __name__ == "__main__":
    out = [validate("I", 0, m) for m in range(3, 13)]
    for t, n in ORDERS:  # every labelling used in the growth classification
        for order in permutations(range(n)):
            out.append(validate(t, n, 0, list(order)))
    print(json.dumps({"all_ok": all(r["ok"] for r in out), "tables": len(out),
                      "details": out}, indent=1))
