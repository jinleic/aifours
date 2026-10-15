"""Exact growth classification of the reduced deg-lex GS basis (leading words)
via strongly connected components of the trimmed pair automaton.

For a trim deterministic automaton with c(L) accepted words of length L:
  - finite language                   if no SCC contains a cycle;
  - "polynomial degree d-1"           if every cyclic SCC is a single simple cycle,
                                      d = max number of cyclic SCCs on a path:
                                      c(L) = O(L^(d-1)) and c(L) >= c L^(d-1) along an
                                      arithmetic progression of lengths;
  - "exponential"                     if some SCC has a vertex with >= 2 internal
                                      out-edges: limsup c(L)^(1/L) > 1 (growth along an
                                      arithmetic progression, not necessarily every L).

Usage: python3 work/classify.py TYPE n [--m M] [--order ...] [--monoid] [--all-orders]
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from automaton import NFAutomaton, build_table  # noqa: E402

ACC = "ACCEPT"


def pair_graph(A: NFAutomaton):
    n = A.T.n
    start = []
    edges = {}  # state -> list of (letter, target or ACC)
    todo = []
    for y in range(n):
        O1 = A.step(frozenset(), y)
        if O1 is not None:
            s = (O1, frozenset())
            start.append(s)
            todo.append(s)
    seen = set(todo)
    while todo:
        st = todo.pop()
        Of, Os = st
        out = []
        for y in range(n):
            Os2 = A.step(Os, y)
            if Os2 is None:
                continue
            Of2 = A.step(Of, y)
            if Of2 is None:
                out.append((y, ACC))
            else:
                t = (Of2, Os2)
                out.append((y, t))
                if t not in seen:
                    seen.add(t)
                    todo.append(t)
        edges[st] = out
    return start, edges


def trim(start, edges):
    # co-reachable: can reach ACC
    rev = {s: [] for s in edges}
    good = set()
    for s, out in edges.items():
        for _y, t in out:
            if t == ACC:
                good.add(s)
            else:
                rev[t].append(s)
    stack = list(good)
    while stack:
        s = stack.pop()
        for p in rev[s]:
            if p not in good:
                good.add(p)
                stack.append(p)
    return {s: [(y, t) for y, t in out if t == ACC or t in good] for s, out in edges.items() if s in good}


def sccs(graph):
    index, low, onstack, stack, comps = {}, {}, set(), [], []
    counter = [0]
    sys.setrecursionlimit(100000)

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        onstack.add(v)
        for _y, w in graph[v]:
            if w == ACC:
                continue
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.discard(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(comp)

    for v in graph:
        if v not in index:
            strong(v)
    return comps


def classify(A: NFAutomaton):
    start, edges = pair_graph(A)
    g = trim(start, edges)
    comps = sccs(g)
    cid = {}
    for i, c in enumerate(comps):
        for v in c:
            cid[v] = i
    cyclic = [False] * len(comps)
    simple = [True] * len(comps)
    for i, c in enumerate(comps):
        cs = set(c)
        for v in c:
            internal = [w for _y, w in g[v] if w != ACC and w in cs]
            if internal:
                cyclic[i] = True
            if len(internal) > 1:
                simple[i] = False
    if any(cyclic[i] and not simple[i] for i in range(len(comps))):
        return {"growth": "exponential", "trim_states": len(g), "sccs": len(comps)}
    # longest path counting cyclic SCCs in the condensation DAG (Tarjan gives reverse topological order)
    best = [0] * len(comps)
    for i, c in enumerate(comps):  # successors appear earlier in Tarjan output
        cs = set(c)
        succ = {cid[w] for v in c for _y, w in g[v] if w != ACC and w not in cs}
        best[i] = (1 if cyclic[i] else 0) + max((best[j] for j in succ), default=0)
    starts = [s for s in start if s in g]
    d = max((best[cid[s]] for s in starts), default=0)
    if d == 0:
        return {"growth": "finite", "trim_states": len(g), "sccs": len(comps)}
    return {"growth": f"polynomial degree {d - 1}", "trim_states": len(g), "sccs": len(comps)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("typ")
    ap.add_argument("n", type=int)
    ap.add_argument("--m", type=int, default=0)
    ap.add_argument("--order", default=None)
    ap.add_argument("--monoid", action="store_true")
    ap.add_argument("--all-orders", action="store_true")
    a = ap.parse_args()
    nn = 2 if a.typ == "I" else a.n
    orders = list(itertools.permutations(range(nn))) if a.all_orders else \
        [tuple(int(x) for x in a.order.split(","))] if a.order else [tuple(range(nn))]
    for order in orders:
        T = build_table(a.typ, a.n, a.m, list(order))
        A = NFAutomaton(T, monoid=a.monoid)
        r = classify(A)
        r.update({"type": a.typ, "n": a.n, "m": a.m, "order": list(order), "monoid": a.monoid})
        print(json.dumps(r), flush=True)


if __name__ == "__main__":
    main()
