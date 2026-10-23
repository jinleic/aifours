#!/usr/bin/env python3
"""Finite-exact aid (NOT a premise) for proof-ROT-lowodd-v1.md: the zero-pattern sequence statements (*) of K1
and (**) of K2, checked over ALL multisets of rotation values for p = 5, 7.
  (*)  |Y| = 2p-1+s (0 <= s <= p-1), no zero-sum (even length L, value sum 0 mod p) with L in [s+1, 2p]
       => s = 0 and Y = c^(2p-1), c != 0.
  (**) |Y| = 2p-2+2t (0 <= t <= (p-1)/2), no zero-sum with L in [2t+2, 2p]
       => t = 0 and Y = c^(2p-2), or t = 1 and Y within {c, -c}, c != 0.
Mutation controls: the same enumeration with the forbidden interval's lower end raised by 2 must produce
survivors violating the conclusion (shows the check is sensitive).
"""
import itertools, json, sys


def zero_lengths(mult, p, maxL):
    """mult[v] = multiplicity of value v.  Returns set of lengths L <= maxL of zero-sum sub-multisets (L >= 1)."""
    full = (1 << p) - 1
    reach = [0] * (maxL + 1)
    reach[0] = 1
    for v in range(p):
        c = mult[v]
        if not c:
            continue
        new = reach[:]
        for L in range(maxL + 1):
            m = reach[L]
            if not m:
                continue
            for j in range(1, c + 1):
                if L + j > maxL:
                    break
                s = (j * v) % p
                new[L + j] |= ((m << s) | (m >> (p - s))) & full if s else m
        reach = new
    return {L for L in range(1, maxL + 1) if reach[L] & 1}


def multisets(p, n):
    for comb in itertools.combinations_with_replacement(range(p), n):
        mult = [0] * p
        for v in comb:
            mult[v] += 1
        yield mult


def conclusion_k1(mult, p, s):
    vals = [v for v in range(p) if mult[v]]
    return s == 0 and len(vals) == 1 and vals[0] != 0


def conclusion_k2(mult, p, t):
    vals = [v for v in range(p) if mult[v]]
    if 0 in vals:
        return False
    if t == 0:
        return len(vals) == 1
    if t == 1:
        return len(vals) == 1 or (len(vals) == 2 and (vals[0] + vals[1]) % p == 0)
    return False


def run(p, shift):
    out = {'p': p, 'shift': shift, 'K1': {}, 'K2': {}}
    for s in range(0, p):
        n = 2 * p - 1 + s
        lo = s + 1 + shift
        surv = viol = 0
        for mult in multisets(p, n):
            Ls = zero_lengths(mult, p, 2 * p)
            if any(lo <= L <= 2 * p and L % 2 == 0 for L in Ls):
                continue
            surv += 1
            viol += not conclusion_k1(mult, p, s)
        out['K1'][s] = [surv, viol]
    for t in range(0, (p - 1) // 2 + 1):
        n = 2 * p - 2 + 2 * t
        lo = 2 * t + 2 + shift
        surv = viol = 0
        for mult in multisets(p, n):
            Ls = zero_lengths(mult, p, 2 * p)
            if any(lo <= L <= 2 * p and L % 2 == 0 for L in Ls):
                continue
            surv += 1
            viol += not conclusion_k2(mult, p, t)
        out['K2'][t] = [surv, viol]
    return out


if __name__ == '__main__':
    for p in (5, 7):
        for shift in (0, 2):
            print(json.dumps(run(p, shift)), flush=True)
