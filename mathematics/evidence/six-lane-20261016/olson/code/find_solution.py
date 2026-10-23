#!/usr/bin/env python3
"""Find and print identity 2p-subwords of a word over D_{2p} (exact DP + backtrack).
Usage: find_solution.py p "r1 s0 ..." [maxsol]
Prints selections as the word with selected letters in [brackets], plus
zone signs, and counts of all solutions (up to maxsol enumerated)."""
import sys
from functools import lru_cache

def parse(s):
    out = []
    for tok in s.split():
        out.append(('R' if tok[0] == 'r' else 'F', int(tok[1:])))
    return out

def main():
    p = int(sys.argv[1]); word = parse(sys.argv[2])
    maxsol = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    n = len(word); n2 = 2 * p
    # reach[i] = set of states (size, e, v) achievable using letters < i
    sys.setrecursionlimit(10000)
    @lru_cache(maxsize=None)
    def can(i, size, e, v):
        # can we complete from position i to size 2p with final (0, +1)?
        if size == n2:
            return e == 1 and v % p == 0
        if n - i < n2 - size:
            return False
        c, val = word[i]
        if can(i + 1, size, e, v):
            return True
        if c == 'R':
            return can(i + 1, size + 1, e, (v + e * val) % p)
        return can(i + 1, size + 1, -e, (v + e * val) % p)
    sols = []
    def enum(i, size, e, v, chosen):
        if len(sols) >= maxsol:
            return
        if size == n2:
            if e == 1 and v % p == 0:
                sols.append(list(chosen))
            return
        if i >= n or not can(i, size, e, v):
            return
        c, val = word[i]
        # take
        if c == 'R':
            ne, nv = e, (v + e * val) % p
        else:
            ne, nv = -e, (v + e * val) % p
        if can(i + 1, size + 1, ne, nv):
            chosen.append(i); enum(i + 1, size + 1, ne, nv, chosen); chosen.pop()
        if can(i + 1, size, e, v):
            enum(i + 1, size, e, v, chosen)
    enum(0, 0, 1, 0, [])
    print('solutions_found', len(sols), 'exists', can(0, 0, 1, 0))
    for s in sols:
        ss = set(s); out = []; e = 1
        for i, (c, val) in enumerate(word):
            tok = ('r%d' if c == 'R' else 's%d') % val
            if i in ss:
                out.append('[' + tok + ('+' if e == 1 else '-') + ']')
                if c == 'F':
                    e = -e
            else:
                out.append(tok)
        nf = sum(1 for i in s if word[i][0] == 'F')
        print('F=%d R=%d :' % (nf, len(s) - nf), ' '.join(out))

if __name__ == '__main__':
    main()
