#!/usr/bin/env python3
"""Which cyclic R/F type patterns of length 4p-1 are covered by the
value-independent tools?
  EGZ:      R >= 3p-1
  Option a: EGZ on 2p-1 disjoint pair items (adjacent-in-F-order reflection
            pairs with an EMPTY inner gap, and rotation pairs from the rest);
            computed exactly as a max-matching DP over the cyclic pattern
  Theorem P: F + sum_t floor(n_t/2) >= 3p-1
Coverage depends only on the type pattern.  Output: counts of uncovered
patterns (up to rotation) and their run-length signatures.
"""
import sys
from collections import Counter


def canon_cyclic(s):
    return min(s[i:] + s[:i] for i in range(len(s)))


def gaps_of(s):
    # s cyclic string over 'R','F' with at least one F; return list of rotation counts per gap
    n = len(s)
    i0 = s.index('F')
    t = s[i0 + 1:] + s[:i0 + 1]  # starts after an F, ends with that F
    g = []
    cnt = 0
    for ch in t:
        if ch == 'R':
            cnt += 1
        else:
            g.append(cnt)
            cnt = 0
    return g  # gap before each F in cyclic order


def option_alpha_items(s):
    """max over sets B of non-overlapping cyclic reflection pairs (f_k,f_{k+1})
    of |B| + floor((R - inner(B))/2), inner(B) = rotations strictly inside the
    chosen pairs.  Pairs with inner >= 2 never help (they cost >= 1 item), so
    only inner in {0,1} are considered.  Exact cyclic DP."""
    g = gaps_of(s)          # g[k] = rotations before f_k ; pair (f_{k-1}, f_k) has inner g[k]
    F = len(g)
    R = sum(g)
    if F < 2:
        return R // 2
    NEG = -10**9
    best = NEG
    # pair index k means pair (f_{k-1}, f_k) using reflections k-1 and k, inner g[k]
    # cyclic: pairs k and k+1 conflict (share f_k); handle by fixing whether pair 0 used
    for use0 in (0, 1):
        if use0 and g[0] > 1:
            continue
        # dp over k=1..F-1: state (last_used, inner_parity) -> max (2*count - inner)
        dp = {}
        init_val = (2 - g[0]) if use0 else 0
        dp[(use0, (g[0] if use0 else 0) % 2)] = init_val
        for k in range(1, F):
            nd = {}
            for (last, par), val in dp.items():
                # skip pair k
                key = (0, par)
                nd[key] = max(nd.get(key, NEG), val)
                # use pair k
                if not last and g[k] <= 1 and not (k == F - 1 and use0):
                    key = (1, (par + g[k]) % 2)
                    nd[key] = max(nd.get(key, NEG), val + 2 - g[k])
            dp = nd
        for (last, par), val in dp.items():
            # val = 2*count - inner ; items = count + floor((R - inner)/2)
            # 2*items = 2*count + (R - inner) - ((R - inner) % 2) = val + R - ((R - inner)%2)
            rpar = (R - par) % 2
            items2 = val + R - rpar
            best = max(best, items2 // 2)
    return best


def main():
    p = int(sys.argv[1])
    N = 4 * p - 1
    seen = set()
    unc = Counter()
    tot = 0
    examples = {}
    for m in range(1 << N):
        s = ''.join('F' if m >> i & 1 else 'R' for i in range(N))
        c = canon_cyclic(s)
        if c in seen:
            continue
        seen.add(c)
        tot += 1
        R = c.count('R')
        F = N - R
        if R >= 3 * p - 1:
            continue
        g = gaps_of(c)
        Q = F + sum(x // 2 for x in g)
        if Q >= 3 * p - 1:
            continue
        a = option_alpha_items(c)
        if a >= 2 * p - 1:
            continue
        if max(g) >= 2 * p - 1:  # Doubling lemma via EGZ inside one gap
            continue
        # signature: run lengths
        sig = tuple(sorted(Counter(g).items()))
        key = (F, R, sum(1 for x in g if x % 2), sum(1 for x in g if x == 0))
        unc[key] += 1
        examples.setdefault(key, c)
    print('p', p, 'cyclic patterns', tot, 'uncovered', sum(unc.values()))
    for k in sorted(unc)[:60]:
        print('  F=%d R=%d oddgaps=%d emptygaps=%d : %d   e.g. %s' % (k + (unc[k], examples[k])))


if __name__ == '__main__':
    main()
