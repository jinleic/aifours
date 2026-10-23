#!/usr/bin/env python3
r"""Group-algebra tiling criterion for ordered EGZ in D_{2p} (sufficient condition).

Unit = consecutive segment of the cyclic word.  S_u = {(value, size/2) in Z_p^2 :
internal selections with an even number of reflections and even size}; 0 in S_u.
depth(S_u) >= d  iff  e_const is in the span of {(m(a))_{deg m < d} : a in S_u \ {0}}
(i.e. exists c with c_0 = -1 ... element of J^d in F_p[Z_p^2]).  If the cyclic word is
partitioned into units with total depth >= 2p-1 (Loewy length of F_p[Z_p^2]), an
identity 2p-subword exists (proof: product of the unit elements is 0; coefficient of
[0] gives a nonempty zero-sum choice; even #F per unit keeps zones; half-size = p).
depth <= floor(len/2); "full" = equality.  Criterion used here: one odd unit of
length 1 or 3 (always full) + even full units of length <= LMAX.
Usage: tiling.py p nwords seed mode   (modes as in coverage_all.py)  or  tiling.py p "word"
"""
import sys, random, itertools, json
from functools import lru_cache
from collections import Counter

P = None

def unit_points(unit, p):
    """unit: tuple of ('R'|'F', val). Return set of (value, half) for nonempty
    selections with even #F and even size."""
    n = len(unit)
    pts = set()
    for mask in range(1, 1 << n):
        nf = 0; sz = 0; e = 1; v = 0
        for i in range(n):
            if mask >> i & 1:
                c, x = unit[i]
                sz += 1
                v = (v + e * x) % p
                if c == 'F':
                    nf += 1; e = -e
        if nf % 2 == 0 and sz % 2 == 0:
            pts.add((v, (sz // 2) % p))
    return pts

def rank_mod(rows, p):
    rows = [list(r) for r in rows]
    rk = 0; ncol = len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = None
        for i in range(rk, len(rows)):
            if rows[i][col] % p:
                piv = i; break
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = pow(rows[rk][col], p - 2, p)
        rows[rk] = [x * inv % p for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] % p:
                f = rows[i][col]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk

def depth_at_least(pts, d, p):
    """True iff e_const in span of evaluation vectors of monomials deg<d at pts."""
    if d <= 0:
        return True
    mons = [(i, j) for i in range(d) for j in range(d) if i + j < d]
    vecs = [[pow(a, i, p) * pow(h, j, p) % p for (i, j) in mons] for (a, h) in pts]
    e0 = [1 if (i, j) == (0, 0) else 0 for (i, j) in mons]
    if not vecs:
        return False
    r1 = rank_mod(vecs, p)
    r2 = rank_mod(vecs + [e0], p)
    return r1 == r2

@lru_cache(maxsize=None)
def full_unit(unit, p):
    L = len(unit)
    if L % 2:
        return False
    nf = sum(1 for c, _ in unit if c == 'F')
    if nf % 2:
        return False
    pts = unit_points(unit, p)
    return depth_at_least(pts, L // 2, p)

def tiles(word, p, lmax=8):
    """Search: cyclic word; choose odd unit (length 1 or 3) start s; tile the rest."""
    n = len(word)
    for olen in (1, 3):
        for s in range(n):
            lin = [word[(s + olen + i) % n] for i in range(n - olen)]
            m = len(lin)
            ok = [False] * (m + 1)
            ok[0] = True
            for i in range(m):
                if not ok[i]:
                    continue
                for L in range(2, lmax + 1, 2):
                    if i + L <= m and not ok[i + L]:
                        if full_unit(tuple(lin[i:i + L]), p):
                            ok[i + L] = True
            if ok[m]:
                return True
    return False

def parse(s):
    return [('R' if t[0] == 'r' else 'F', int(t[1:])) for t in s.split()]

def main():
    p = int(sys.argv[1])
    if len(sys.argv) == 3:
        w = parse(sys.argv[2]); print(tiles(w, p)); return
    nw = int(sys.argv[2]); seed = int(sys.argv[3]); mode = sys.argv[4]
    import coverage_all as ca
    import residual_stats as rs
    rng = random.Random(seed)
    N = 4 * p - 1
    st = Counter(); fails = []
    for it in range(nw):
        if mode in ('rotrigid', 'twoval', 'gr'):
            w = rs.make(mode, p, N, rng)
        elif mode == 'random':
            pr = rng.random()
            w = [('R', rng.randrange(p)) if rng.random() < pr else ('F', rng.randrange(p)) for _ in range(N)]
        elif mode == 'rigid':
            pr = rng.random()
            w = [('R', rng.choice([1, p - 1])) if rng.random() < pr else ('F', 0) for _ in range(N)]
        else:
            raise SystemExit('mode')
        t = tiles(w, p)
        res = ca.classify(w, p)
        old = any(res.values())
        st['tile' if t else 'notile'] += 1
        st[('old' if old else 'noold') + '_' + ('tile' if t else 'notile')] += 1
        if not t and not old and len(fails) < 10:
            fails.append(' '.join(('r%d' if c == 'R' else 's%d') % v for c, v in w))
    print(json.dumps({'p': p, 'mode': mode, 'n': nw, 'stats': dict(st)}))
    for f in fails:
        print('BOTHFAIL', f)

if __name__ == '__main__':
    main()
