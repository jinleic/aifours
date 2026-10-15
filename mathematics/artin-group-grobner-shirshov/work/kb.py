"""Knuth-Bendix / Buchberger-Shirshov completion for monoid presentations
(string rewriting) with the deg-lex order, truncated at a maximal length.

Independent of coxeter.py: it only sees the defining relations.  Letters are
single characters and the letter order is Python's character order (so the
alphabet '0' < '1' < 'a' < 'b' < ... encodes Delta^{-1} < Delta < s_1 < ...).

For a presentation whose relations are length-preserving (Artin monoids) the
truncated completion is exact: every rule of the reduced complete system with
left side of length <= maxlen is found, because all derivations between words
of a given length stay in that length.  For non-homogeneous presentations
(the group with Delta^{+-1}) truncation is a heuristic, and its output is
cross-checked against the Garside oracle.

Usage (library): rws = KB(); rws.complete(equations, maxlen); rws.rules
"""
from __future__ import annotations

import heapq
from collections import defaultdict


def gt(x: str, y: str) -> bool:
    return (len(x), x) > (len(y), y)


class KB:
    def __init__(self):
        self.rules: dict[str, str] = {}
        self.lens: list[int] = []
        self.pre: dict[str, set[str]] = defaultdict(set)  # proper prefix -> lhs
        self.suf: dict[str, set[str]] = defaultdict(set)  # proper suffix -> lhs
        self.truncated = 0  # equations whose reduced left side exceeded maxlen
        self.skipped_overlaps = 0  # critical pairs longer than maxlen (not computed)

    # ------------------------------------------------------------ reduction
    def reduce(self, w: str) -> str:
        rules, lens = self.rules, self.lens
        out: list[str] = []
        inp = list(reversed(w))
        while inp:
            out.append(inp.pop())
            n = len(out)
            for L in lens:
                if L > n:
                    break
                r = rules.get("".join(out[n - L:]))
                if r is not None:
                    del out[n - L:]
                    inp.extend(reversed(r))
                    break
        return "".join(out)

    # ------------------------------------------------------------ rule set
    def _index(self, l: str) -> None:
        for k in range(1, len(l)):
            self.pre[l[:k]].add(l)
            self.suf[l[-k:]].add(l)

    def _unindex(self, l: str) -> None:
        for k in range(1, len(l)):
            self.pre[l[:k]].discard(l)
            self.suf[l[-k:]].discard(l)

    def _set_lens(self) -> None:
        self.lens = sorted({len(l) for l in self.rules})

    def _add(self, l: str, r: str, queue) -> None:
        # inter-reduce: rules whose lhs contains l are removed and re-queued
        doomed = [l2 for l2 in self.rules if l in l2]
        for l2 in doomed:
            r2 = self.rules.pop(l2)
            self._unindex(l2)
            heapq.heappush(queue, (len(l2), l2, r2))
        self.rules[l] = r
        self._index(l)
        self._set_lens()
        # right sides are kept reduced
        for l2, r2 in list(self.rules.items()):
            if l in r2:
                self.rules[l2] = self.reduce(r2)

    # ------------------------------------------------------------ completion
    def complete(self, equations, maxlen: int, verbose: bool = False) -> None:
        queue: list = []
        for s, t in equations:
            heapq.heappush(queue, (max(len(s), len(t)), s, t))
        added = 0
        while queue:
            _, s, t = heapq.heappop(queue)
            s, t = self.reduce(s), self.reduce(t)
            if s == t:
                continue
            if gt(t, s):
                s, t = t, s
            if len(s) > maxlen:
                self.truncated += 1
                continue
            self._add(s, t, queue)
            added += 1
            if verbose and added % 500 == 0:
                print("rules", len(self.rules), "queue", len(queue), flush=True)
            # critical pairs of s->t with every rule (including itself)
            l1, r1 = s, t
            for k in range(1, len(l1)):
                # suffix of l1 == proper prefix of l2
                for l2 in list(self.pre.get(l1[-k:], ())):
                    if len(l1) + len(l2) - k > maxlen:
                        self.skipped_overlaps += 1
                        continue
                    if l2 not in self.rules:
                        continue
                    r2 = self.rules[l2]
                    w1 = r1 + l2[k:]
                    w2 = l1[:-k] + r2
                    heapq.heappush(queue, (len(l1) + len(l2) - k, w1, w2))
                # suffix of l2 == proper prefix of l1
                for l2 in list(self.suf.get(l1[:k], ())):
                    if len(l1) + len(l2) - k > maxlen:
                        self.skipped_overlaps += 1
                        continue
                    if l2 not in self.rules:
                        continue
                    r2 = self.rules[l2]
                    w1 = r2 + l1[k:]
                    w2 = l2[:-k] + r1
                    heapq.heappush(queue, (len(l1) + len(l2) - k, w1, w2))
        # final normalisation of right sides
        for l2, r2 in list(self.rules.items()):
            self.rules[l2] = self.reduce(r2)
