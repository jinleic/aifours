#!/usr/bin/env python3
"""Finite-exact aid for Lemma INC (proof-ROT-o3-v3.md Sec. 0): enumerate ALL multisets of rotation values x in Z_p
(elements (1, x) of Z_2 x Z_p) of length L = 2p-1-e, 0 <= e <= 3, that are zero-sum-free in Z_(2p) (no nonempty
sub-multiset of even size with value sum 0 mod p), by a DFS over multiplicities pruned as soon as a zero-sum appears.
Check: each is c^L (c != 0) or c^(L-1) (3c).  Mutation control: e = 4 must produce a survivor outside that form
(e.g. c^(L-2)(3c)^2 or c^(L-1)(5c)).  Usage: check_inc_v1.py p [p ...]
"""
import json, sys


def survivors(p, L):
    full = (1 << p) - 1
    out = []

    def addcopy(prof, v):
        nx = prof[:]
        for l in range(len(prof) - 1):
            m = prof[l]
            if m:
                s = v % p
                nx[l + 1] |= (((m << s) | (m >> (p - s))) & full) if s else m
        return nx

    def zs(prof):
        return any(prof[l] & 1 for l in range(2, len(prof), 2))

    def rec(v, left, cnt, prof):
        if v == p:
            if left == 0:
                out.append(cnt[:])
            return
        c = 0
        pr = prof
        while True:
            cnt.append(c)
            rec(v + 1, left - c, cnt, pr)
            cnt.pop()
            if c == left:
                break
            pr = addcopy(pr, v)
            c += 1
            if zs(pr):
                break

    prof0 = [0] * (L + 1)
    prof0[0] = 1
    rec(0, L, [], prof0)
    return out


def form_ok(cnt, p, L, e):
    vals = [v for v in range(p) if cnt[v]]
    if len(vals) == 1:
        return vals[0] != 0 and cnt[vals[0]] == L
    if len(vals) == 2 and e >= 2:
        for c in vals:
            other = [v for v in vals if v != c][0]
            if c != 0 and cnt[c] == L - 1 and cnt[other] == 1 and other == (3 * c) % p:
                return True
    return False


def main():
    for p in map(int, sys.argv[1:]):
        for e in range(0, 5):
            L = 2 * p - 1 - e
            S = survivors(p, L)
            bad = [s for s in S if not form_ok(s, p, L, min(e, 3))]
            print(json.dumps({'p': p, 'e': e, 'L': L, 'survivors': len(S), 'outside_INC_form': len(bad),
                              'example_outside': bad[:2]}), flush=True)


if __name__ == '__main__':
    main()
