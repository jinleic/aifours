#!/usr/bin/env python3
"""Raw ordered-product DPs for D_(2p) (reflection slice; no window formula anywhere in this file).

Convention (olson/proof-dihedral-partial.md Sec. 0): (v,e)(v',e') = (v + e v', e e'); rho_x = (x,+1), sigma_y = (y,-1).
A word is a list of letters ('R', x) or ('F', y).  An identity 2p-subword is an increasing index set of size 2p whose
ordered product is (0,+1).  Existence is invariant under cyclic rotation, so the linear word is checked as given.

dp1: forward DP over states (size, sign e) -> bitmask of values v (bit v set iff (v,e) reachable with that size).
dp2: independent formulation: every element (v,e) acts on Z_p by i -> v + e*i; it is encoded by the pair of images
     (f(0), f(1)); the composition f_g o f_h equals f_(gh).  States are dicts size -> set of encoded maps; a letter is
     appended on the RIGHT (product g * letter), i.e. new map = f_g o f_letter.
witness: returns an explicit increasing index list (dp1 back-pointers), re-multiplied by mult() for every reported YES.
"""

def mult(g, h, p):
    (v, e), (w, f) = g, h
    return ((v + e * w) % p, e * f)

def letter(c, x, p):
    return (x % p, 1) if c == 'R' else (x % p, -1)

def product(word, idx, p):
    g = (0, 1)
    for i in idx:
        g = mult(g, letter(*word[i], p), p)
    return g

def dp1(word, p):
    n2 = 2 * p
    full = (1 << p) - 1
    reach = [[0, 0] for _ in range(n2 + 1)]   # reach[size][0 for e=+1, 1 for e=-1]
    reach[0][0] = 1
    for c, x in word:
        x %= p
        for sz in range(n2 - 1, -1, -1):
            for es in (0, 1):
                m = reach[sz][es]
                if not m:
                    continue
                e = 1 if es == 0 else -1
                # (v,e)*(x, s) = (v + e x, e s)
                sh = (e * x) % p
                mm = ((m << sh) | (m >> (p - sh))) & full if sh else m
                if c == 'R':
                    reach[sz + 1][es] |= mm
                else:
                    reach[sz + 1][1 - es] |= mm
    return bool(reach[n2][0] & 1)

def dp2(word, p):
    n2 = 2 * p
    def enc(v, e):
        return (v % p, (v + e) % p)
    def comp(f, g):          # (f o g)(i) = f(g(i)); maps encoded by (image of 0, image of 1)
        f0, f1 = f
        ef = (f1 - f0) % p   # +1 or p-1
        def fa(i):
            return (f0 + ef * i) % p
        return (fa(g[0]), fa(g[1]))
    states = {0: {enc(0, 1)}}
    for c, x in word:
        L = enc(x, 1) if c == 'R' else enc(x, -1)
        for sz in sorted(states.keys(), reverse=True):
            if sz >= n2:
                continue
            s = states[sz]
            t = states.setdefault(sz + 1, set())
            for f in list(s):
                t.add(comp(f, L))
    return enc(0, 1) in states.get(n2, set())

def witness(word, p):
    """Explicit identity 2p-subword (increasing indices) or None, via dp1 with back-pointers."""
    n2 = 2 * p
    n = len(word)
    # layer[i] = dict (size, v, e) -> predecessor info, after processing letters 0..i-1
    cur = {(0, 0, 1): None}
    hist = [cur]
    for i in range(n):
        g = letter(*word[i], p)
        nxt = dict(cur)
        for (sz, v, e), _ in cur.items():
            if sz >= n2:
                continue
            nv, ne = mult((v, e), g, p)
            key = (sz + 1, nv, ne)
            if key not in nxt:
                nxt[key] = (i, (sz, v, e))
        cur = nxt
        hist.append(cur)
    target = (n2, 0, 1)
    if target not in cur:
        return None
    idx = []
    key = target
    i = n
    while key != (0, 0, 1):
        # find the earliest layer where key appeared: walk back while key present in previous layer
        while i > 0 and key in hist[i - 1]:
            i -= 1
        info = hist[i][key]
        j, prev = info
        idx.append(j)
        key = prev
        i = j
    idx.reverse()
    assert len(idx) == n2 and idx == sorted(idx) and len(set(idx)) == n2
    assert product(word, idx, p) == (0, 1)
    return idx

def solvable(word, p):
    a, b = dp1(word, p), dp2(word, p)
    if a != b:
        raise AssertionError("dp1/dp2 disagree")
    return a
