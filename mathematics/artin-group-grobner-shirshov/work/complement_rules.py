r"""Explicit GS rule transducers on atoms + Delta^{+-1}, uniformly for finite W.

No Artin normal-form computation is used to DEFINE the rules. For x in S and
q in {atoms t<x} union {Delta}, initialise e=x\q, output q rho(q\x).
Read y, emit rho(e\y), and replace e by y\e. Accept at the first e=1.
The positive equality e*(e\y)=y*(y\e) telescopes; proof.md Theorem G.

A filter (default) intersects the leading-word language with positive MinRed
from Theorem B; this gives minimal leading words, but right sides need not be
normal and a word can have several rules. This is NOT a reduced GS basis.
Unfiltered mode is the simpler uniform theorem and needs only |W| states.

Pairs of words form a monoid by coordinatewise concatenation. Exported rational
expressions are DAGs over pairs: + = union, . = concatenation, * = Kleene star.
The input/output choices stay COUPLED; projecting separately would be wrong.
"""
from __future__ import annotations

import argparse
import json
from collections import deque

from automaton import NFAutomaton, build_table
from classify import ACC, pair_graph, sccs, trim


class ComplementRules:
    def __init__(self, table):
        if table.W.N < 2:
            raise ValueError("Theorem G requires N >= 2; use Theorem C's rank-one basis")
        self.T = table
        self.rep = []
        for e in range(table.size):
            w, letters = e, []
            while w != table.e:
                bit = table.ld[w] & -table.ld[w]
                y = bit.bit_length() - 1
                letters.append(chr(97 + y))
                w = table.lmul[y][w]
            self.rep.append("".join(letters))
        self.transitions = {}

    def quotient(self, e, j):
        for y in self.rep[e]:
            j = self.T.lmul[ord(y) - 97][j]
        return j

    def step(self, e, y):
        key = e, y
        if key not in self.transitions:
            j = self.T.join(e, self.T.gen[y])
            residual = self.T.lmul[y][j]
            companion = self.quotient(e, j)
            assert self.T.length[e] + self.T.length[companion] == self.T.length[j]
            assert 1 + self.T.length[residual] == self.T.length[j]
            self.transitions[key] = residual, self.rep[companion]
        return self.transitions[key]

    def seeds(self):
        for x in range(self.T.n):
            for q in list(range(x)) + [None]:
                target = self.T.w0 if q is None else self.T.gen[q]
                j = self.T.join(self.T.gen[x], target)
                e = self.T.lmul[x][j]
                target_letter = "1" if q is None else chr(97 + q)
                output = target_letter + self.rep[self.quotient(target, j)]
                yield x, q, e, output

    def rhs(self, word, q):
        x = ord(word[0]) - 97
        seed = next(s for s in self.seeds() if s[0] == x and s[1] == q)
        e, output = seed[2], seed[3]
        for i, y in enumerate(word[1:], 1):
            e, emission = self.step(e, ord(y) - 97)
            output += emission
            if e == self.T.e:
                return output if i == len(word) - 1 else None
        return None

    def graph(self, filtered=True):
        """All accepting paths are explicit rule pairs. Vertices 0=start,1=accept.
        Edges (i,j,input,output); there is no edge out of the accept vertex.
        State labels are serializable and deterministic."""
        A = NFAutomaton(self.T) if filtered else None
        labels = ["start", "accept"]
        idx = {}
        queue = deque()
        edges = []

        def add_state(key):
            if key not in idx:
                idx[key] = len(labels)
                e, full, suffix = key
                labels.append([e, sorted(full) if full is not None else None,
                               sorted(suffix) if suffix is not None else None])
                queue.append(key)
            return idx[key]

        for x, q, e, output in self.seeds():
            full = A.step(frozenset(), x) if filtered else None
            key = (e, full, frozenset() if filtered else None)
            edges.append((0, add_state(key), chr(97 + x), output))
        while queue:
            key = queue.popleft()
            e, full, suffix = key
            for y in range(self.T.n):
                if filtered:
                    suffix2 = A.step(suffix, y)
                    if suffix2 is None:
                        continue
                    full2 = A.step(full, y)
                else:
                    full2 = suffix2 = None
                e2, output = self.step(e, y)
                if e2 == self.T.e:
                    if filtered:
                        assert full2 is None
                    dest = 1
                elif filtered and full2 is None:
                    continue  # a different witness killed the full prefix sooner
                else:
                    dest = add_state((e2, full2, suffix2))
                edges.append((idx[key], dest, chr(97 + y), output))
        # Trim states that cannot reach the accepting vertex.
        reverse = {i: [] for i in range(len(labels))}
        for s, t, _a, _b in edges:
            reverse[t].append(s)
        good, todo = {1}, [1]
        while todo:
            for s in reverse[todo.pop()]:
                if s not in good:
                    good.add(s)
                    todo.append(s)
        ids = {old: new for new, old in enumerate(sorted(good))}
        return {"states": [labels[i] for i in sorted(good)], "start": ids[0], "accept": ids[1],
                "edges": sorted(set((ids[s], ids[t], a, b) for s, t, a, b in edges
                                    if s in good and t in good)), "filtered_minimal_leading": filtered}


class PairRegex:
    """Hash-consed expression DAG. Nodes always reference lower-indexed nodes."""
    def __init__(self):
        self.nodes = [["empty"], ["epsilon"]]
        self.cache = {("empty",): 0, ("epsilon",): 1}

    def node(self, op, *args):
        key = (op,) + args
        if key not in self.cache:
            self.cache[key] = len(self.nodes)
            self.nodes.append(list(key))
        return self.cache[key]

    def add(self, a, b):
        if a == 0 or a == b:
            return b
        if b == 0:
            return a
        return self.node("union", *sorted((a, b)))

    def cat(self, a, b):
        if 0 in (a, b):
            return 0
        if a == 1:
            return b
        if b == 1:
            return a
        return self.node("concat", a, b)

    def star(self, a):
        return 1 if a in (0, 1) else self.node("star", a)

    def eliminate(self, graph):
        edges = {}
        for i, j, a, b in graph["edges"]:
            edges[i, j] = self.add(edges.get((i, j), 0), self.node("pair", a, b))
        remaining = set(range(len(graph["states"]))) - {graph["start"], graph["accept"]}
        order = []
        while remaining:
            incoming, outgoing = {}, {}
            for (i, j), label in edges.items():
                if label and i != j:
                    outgoing.setdefault(i, set()).add(j)
                    incoming.setdefault(j, set()).add(i)
            k = min(remaining, key=lambda v: (len(incoming.get(v, ())) * len(outgoing.get(v, ())), v))
            left, right = sorted(incoming.get(k, ())), sorted(outgoing.get(k, ()))
            loop = self.star(edges.get((k, k), 0))
            for i in left:
                prefix = self.cat(edges[i, k], loop)
                for j in right:
                    edges[i, j] = self.add(edges.get((i, j), 0), self.cat(prefix, edges[k, j]))
            for key in [key for key in edges if k in key]:
                del edges[key]
            remaining.remove(k)
            order.append(k)
        root = edges.get((graph["start"], graph["accept"]), 0)
        return {"nodes": self.nodes, "root": root, "elimination_order": order,
                "semantics": "paired words; union, coordinatewise concat, coupled Kleene star"}


def scc_report(table):
    A = NFAutomaton(table)
    starts, edges = pair_graph(A)
    graph = trim(starts, edges)
    components = sccs(graph)
    multi = []
    for comp in components:
        vertices = set(comp)
        internal = [(s, y, t) for s in comp for y, t in graph[s] if t != ACC and t in vertices]
        if len(internal) > len(comp):
            # Stable state names use explicit obligation sets, not arbitrary object IDs.
            vertices = sorted(comp, key=lambda p: (sorted(p[0]), sorted(p[1])))
            index = {s: i for i, s in enumerate(vertices)}
            multi.append({"states": [[sorted(s[0]), sorted(s[1])] for s in vertices],
                          "edges": sorted((index[s], index[t], chr(97 + y)) for s, y, t in internal)})
    return multi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("typ")
    parser.add_argument("n", type=int)
    parser.add_argument("--order")
    parser.add_argument("--m", type=int, default=0)
    parser.add_argument("--unfiltered", action="store_true")
    args = parser.parse_args()
    order = [int(i) for i in args.order.split(",")] if args.order else None
    T = build_table(args.typ, args.n, args.m, order)
    if order is None:
        order = list(range(T.n))
    R = ComplementRules(T)
    graph = R.graph(not args.unfiltered)
    regex = PairRegex().eliminate(graph)
    print(json.dumps({"type": [args.typ, args.n, args.m], "order": order,
                      "alphabet": "0=Delta^-1, 1=Delta, a<b<c<...", "simple_words": R.rep,
                      "graph": graph, "paired_regex": regex,
                      "original_multicycle_components": scc_report(T),
                      "twists": [[chr(97 + i) + d, d + chr(97 + T.phi[i])]
                                 for i in range(T.n) for d in "01"],
                      "cancellations": [["01", ""], ["10", ""]]}, separators=(",", ":")))


if __name__ == "__main__":
    main()
