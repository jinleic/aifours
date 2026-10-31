#!/usr/bin/env python3
"""reviewer-cyclo-v1.py  (review f137, reviewer-written; NOT derived from author scripts)

Independent exact arithmetic used by the f137 review controls:
  * integer polynomials, cyclotomic polynomials Phi_m from x^m-1 = prod_{d|m} Phi_d (exact division);
  * Z[zeta_m] in the POWER basis 1,x,...,x^{phi(m)-1} mod Phi_m  (author used Q(zeta8)(x)Q(zeta9) and
    Q(zeta3)(x)Q(zeta5) tensor bases; this is a different representation);
  * a second, tensor representation of Q(zeta3)(x)Q(zeta5) for zeta30 sums (reviewer's own conventions);
  * Q(omega), omega = zeta3, as pairs of Fractions a+b*omega with omega^2 = -1-omega
    (author used a+b*sqrt(-3) pairs);
  * polynomial gcd / exact division over Q(omega) and the mu72 root-closure test by LAYER STRIPPING
    (repeatedly divide by gcd(G, z^72-1)) -- not the author's squarefree-part test;
  * explicit enumeration of the 945 perfect matchings of K_10 as 45-bit masks (author used recursive
    bitmask search).
Self-tests run at load; any failure raises.
"""
from fractions import Fraction as Fr
from itertools import combinations
import cmath, math

# ---------------- integer polynomials (coefficient lists, low degree first) ----------------
def ptrim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p

def pmul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return ptrim(out)

def pdivmod_monic(a, b):
    """exact division by a MONIC integer polynomial b"""
    a = ptrim(a); b = ptrim(b)
    assert b and b[-1] == 1
    q = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        k = len(a) - len(b); c = a[-1]; q[k] = c
        for j, y in enumerate(b):
            a[k + j] -= c * y
        a = ptrim(a)
    return ptrim(q), a

def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]

def eulerphi(m):
    return sum(1 for k in range(1, m + 1) if math.gcd(k, m) == 1)

_PHI = {}
def cyclotomic(m):
    """Phi_m over Z via x^m - 1 = prod_{d|m} Phi_d"""
    if m in _PHI:
        return _PHI[m]
    num = [-1] + [0] * (m - 1) + [1]
    den = [1]
    for d in divisors(m):
        if d < m:
            den = pmul(den, cyclotomic(d))
    q, r = pdivmod_monic(num, den)
    assert r == [], (m, r)
    _PHI[m] = q
    return q

class Cyclo:
    """Exact Z[zeta_m] in the power basis mod Phi_m; tab[e] = coordinates of zeta_m^e."""
    def __init__(self, m):
        self.m = m
        self.phi = cyclotomic(m)
        self.deg = len(self.phi) - 1
        assert self.deg == eulerphi(m)
        tab = []
        cur = [1]
        for e in range(m):
            tab.append(tuple(cur + [0] * (self.deg - len(cur))))
            cur = self.reduce(pmul(cur, [0, 1]))
        assert ptrim(cur) == [1], "x^m must reduce to 1"
        self.tab = tab
        for e in range(m):  # numeric sanity of the table
            val = sum(c * cmath.exp(2j * math.pi * k / m) for k, c in enumerate(tab[e]))
            assert abs(val - cmath.exp(2j * math.pi * e / m)) < 1e-9, (m, e)

    def reduce(self, p):
        q, r = pdivmod_monic(p, self.phi)
        r = ptrim(r)
        return r + [0] * (self.deg - len(r))

    def vec(self, exps):
        acc = [0] * self.deg
        for e in exps:
            v = self.tab[e % self.m]
            for k in range(self.deg):
                acc[k] += v[k]
        return acc

    def vanishes(self, exps):
        """sum_t zeta_m^{e_t} == 0 exactly (power basis is a Q-basis of Q(zeta_m))"""
        return not any(self.vec(exps))

    def numeric(self, exps):
        return sum(cmath.exp(2j * math.pi * (e % self.m) / self.m) for e in exps)

# ------------- tensor representation of Q(zeta3)(x)Q(zeta5), reviewer's own conventions -------------
# basis zeta3^i * zeta5^j, i in {0,1}, j in {0,1,2,3}; zeta3^2 = -1-zeta3; zeta5^4 = -1-zeta5-zeta5^2-zeta5^3.
# zeta30 = zeta30^31 = zeta30^15 * zeta30^10 * zeta30^6 = (-1) * zeta3 * zeta5, so zeta30^e = (-1)^e zeta3^e zeta5^e.
_Z3 = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
_Z5 = {0: (1, 0, 0, 0), 1: (0, 1, 0, 0), 2: (0, 0, 1, 0), 3: (0, 0, 0, 1), 4: (-1, -1, -1, -1)}
def tensor30(e):
    e %= 30
    s = -1 if e % 2 else 1
    a = _Z3[e % 3]; b = _Z5[e % 5]
    return tuple(s * x * y for x in a for y in b)
TENSOR30 = [tensor30(e) for e in range(30)]
def tensor30_vanishes(exps):
    acc = [0] * 8
    for e in exps:
        v = TENSOR30[e % 30]
        for k in range(8):
            acc[k] += v[k]
    return not any(acc)

# ---------------- Q(omega), omega = zeta3 ----------------
class Qw:
    __slots__ = ("a", "b")
    def __init__(self, a, b=0):
        self.a = Fr(a); self.b = Fr(b)
    def __add__(s, o): return Qw(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Qw(s.a - o.a, s.b - o.b)
    def __neg__(s): return Qw(-s.a, -s.b)
    def __mul__(s, o): return Qw(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a - s.b * o.b)
    def conj(s): return Qw(s.a - s.b, -s.b)
    def norm(s): return s.a * s.a - s.a * s.b + s.b * s.b
    def inv(s):
        n = s.norm(); assert n != 0
        c = s.conj(); return Qw(c.a / n, c.b / n)
    def __truediv__(s, o): return s * o.inv()
    def iszero(s): return s.a == 0 and s.b == 0
    def __eq__(s, o): return isinstance(o, Qw) and s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s): return f"({s.a}+{s.b}w)"
    def complex(s): return complex(s.a) + complex(s.b) * cmath.exp(2j * math.pi / 3)

ZETA6 = [Qw(1)]
for _k in range(1, 6):
    ZETA6.append(ZETA6[-1] * Qw(1, 1))   # zeta6 = 1 + omega
assert ZETA6[3] == Qw(-1) and ZETA6[-1] * Qw(1, 1) == Qw(1) and ZETA6[2] == Qw(0, 1)
for _k in range(6):
    assert abs(ZETA6[_k].complex() - cmath.exp(2j * math.pi * _k / 6)) < 1e-12

def qtrim(p):
    p = list(p)
    while p and p[-1].iszero():
        p.pop()
    return p

def qdivmod(a, b):
    a = qtrim(a); b = qtrim(b); assert b
    q = [Qw(0)] * max(0, len(a) - len(b) + 1)
    inv = b[-1].inv()
    while a and len(a) >= len(b):
        k = len(a) - len(b); c = a[-1] * inv; q[k] = c
        for j, y in enumerate(b):
            a[k + j] = a[k + j] - c * y
        a = qtrim(a)
    return qtrim(q), a

def qmul(a, b):
    a = qtrim(a); b = qtrim(b)
    if not a or not b:
        return []
    out = [Qw(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = out[i + j] + x * y
    return qtrim(out)

def qgcd(a, b):
    """monic gcd in Q(omega)[z] (Euclid); [] if both zero"""
    a, b = qtrim(a), qtrim(b)
    while b:
        a, b = b, qdivmod(a, b)[1]
    if not a:
        return []
    inv = a[-1].inv()
    return [x * inv for x in a]

def qderiv(p):
    return qtrim([p[i] * Qw(i) for i in range(1, len(p))])

def qmonic(p):
    p = qtrim(p)
    if not p:
        return []
    inv = p[-1].inv()
    return [x * inv for x in p]

Z72_MINUS_1 = [Qw(-1)] + [Qw(0)] * 71 + [Qw(1)]

def all_roots_in_mu72(G):
    """layer stripping: every root of G (with multiplicity) is a 72nd root of unity"""
    G = qtrim(G); assert G
    while len(G) > 1:
        g = qgcd(G, Z72_MINUS_1)
        if len(g) <= 1:
            return False
        G, r = qdivmod(G, g)
        assert not r
    return True

def reciprocal_conj(P):
    P = qtrim(P)
    return [x.conj() for x in reversed(P)]

def unit_root_closure(P):
    """True iff every unit-circle root of P in Q(omega)[z] lies in mu72.
    (|z|=1 and P(z)=0 imply P*(z)=0 for the reversed-conjugate P*, so z is a root of G=gcd(P,P*);
    we then require all roots of G to be in mu72 by layer stripping.)"""
    P = qtrim(P); assert P
    G = qgcd(P, reciprocal_conj(P))
    if len(G) <= 1:
        return True
    return all_roots_in_mu72(G)

def naive_closure(P):
    """the earlier, too-strong author test: G divides z^72-1 (fails on repeated mu72 roots)"""
    P = qtrim(P)
    G = qgcd(P, reciprocal_conj(P))
    if len(G) <= 1:
        return True
    return not qdivmod(Z72_MINUS_1, G)[1]

def gcd_has_repeated_root(P):
    P = qtrim(P)
    G = qgcd(P, reciprocal_conj(P))
    if len(G) <= 1:
        return False
    return len(qgcd(G, qderiv(G))) > 1

def laurent_to_poly(coeffs_by_exp):
    """dict exponent->Qw  ->  (monic coefficient list low..high after removing z-powers) or None if zero"""
    items = [(k, v) for k, v in coeffs_by_exp.items() if not v.iszero()]
    if not items:
        return None
    lo = min(k for k, _ in items); hi = max(k for k, _ in items)
    p = [Qw(0)] * (hi - lo + 1)
    for k, v in items:
        p[k - lo] = v
    return tuple(qmonic(p))

# ---------------- perfect matchings of K_10 ----------------
PAIRS = list(combinations(range(10), 2))
PIDX = {p: i for i, p in enumerate(PAIRS)}
def all_perfect_matchings(n=10):
    out = []
    def rec(rem, mask):
        if not rem:
            out.append(mask); return
        a = rem[0]
        for b in rem[1:]:
            rec([x for x in rem if x != a and x != b], mask | (1 << PIDX[(a, b)]))
    rec(list(range(n)), 0)
    return out
PM10 = all_perfect_matchings()
assert len(PM10) == 945 and len(set(PM10)) == 945
for _m in PM10:
    assert bin(_m).count("1") == 5
def has_pm(edge_mask):
    """edge_mask: 45-bit mask over PAIRS; True iff some perfect matching of K_10 lies inside the graph"""
    return any((m & ~edge_mask) == 0 for m in PM10)
def edges_to_mask(edges):
    m = 0
    for c, d in edges:
        if c > d:
            c, d = d, c
        m |= 1 << PIDX[(c, d)]
    return m

# ---------------- self-tests ----------------
def _selftest():
    assert cyclotomic(72) == [1] + [0] * 11 + [-1] + [0] * 11 + [1]          # x^24 - x^12 + 1
    assert cyclotomic(6) == [1, -1, 1] and cyclotomic(3) == [1, 1, 1] and cyclotomic(5) == [1, 1, 1, 1, 1]
    assert cyclotomic(30) == [1, 1, 0, -1, -1, -1, 0, 1, 1]                     # Phi_30 = Phi_15(-x)
    C3, C6, C10, C30, C72 = Cyclo(3), Cyclo(6), Cyclo(10), Cyclo(30), Cyclo(72)
    assert C3.vanishes([0, 1, 2]) and not C3.vanishes([0, 1])
    assert C6.vanishes([0, 2, 4]) and C6.vanishes([1, 4]) and not C6.vanishes([0, 1, 2])
    assert C72.vanishes([0, 24, 48]) and C72.vanishes([5, 41]) and C72.vanishes(list(range(0, 72, 8)))
    assert not C72.vanishes([0, 1]) and not C72.vanishes([0, 24])
    assert C10.vanishes(list(range(10))) and C10.vanishes([0, 5]) and not C10.vanishes([0, 1, 2])
    # tensor vs power-basis agreement on all 10-term sums from a random sample
    import random
    rng = random.Random(137)
    for _ in range(3000):
        ex = [rng.randrange(30) for _ in range(rng.randrange(1, 11))]
        a = C30.vanishes(ex); b = tensor30_vanishes(ex); c = abs(C30.numeric(ex)) < 1e-9
        assert a == b == c, (ex, a, b, c)
    assert tensor30_vanishes([0, 15]) and tensor30_vanishes([0, 6, 12, 18, 24]) and tensor30_vanishes([0, 10, 20])
    assert not tensor30_vanishes([0, 3]) and not tensor30_vanishes([1, 16, 0])
    # Q(omega) and gcd
    one = Qw(1); z = [Qw(0), one]
    A = qmul([Qw(-1), one], [Qw(-2), one]); B = qmul([Qw(-1), one], [Qw(-3), one])
    assert qgcd(A, B) == [Qw(-1), one]
    phi6 = [one, Qw(-1), one]
    assert unit_root_closure(phi6) and naive_closure(phi6) and not gcd_has_repeated_root(phi6)
    sq = qmul(phi6, phi6)
    assert unit_root_closure(sq) and not naive_closure(sq) and gcd_has_repeated_root(sq)
    bad = [one, Qw(Fr(-1, 2)), one]                       # roots e^{+-i t}, cos t = 1/4: not roots of unity
    assert not unit_root_closure(bad) and not naive_closure(bad)
    assert not unit_root_closure(qmul(phi6, bad))
    assert unit_root_closure([one, Qw(0), one])           # z^2+1, roots in mu4
    assert unit_root_closure([Qw(-2), Qw(0), Qw(0), one]) # z^3-2, no unit roots
    assert unit_root_closure([one, Qw(-2), one])          # (z-1)^2 repeated
    assert unit_root_closure([Qw(c) for c in cyclotomic(9)]) and unit_root_closure([Qw(c) for c in cyclotomic(8)])
    assert not unit_root_closure([Qw(c) for c in cyclotomic(16)]) and not unit_root_closure([Qw(c) for c in cyclotomic(5)])
    assert not unit_root_closure([Qw(c) for c in cyclotomic(7)]) and unit_root_closure([Qw(c) for c in cyclotomic(72)])
    assert unit_root_closure([Qw(c) for c in cyclotomic(36)]) and not unit_root_closure([Qw(c) for c in cyclotomic(144)])
    # a Q(omega)-coefficient polynomial with a unit root outside mu72: z - u where u = (3+4*omega... ) not unit; use
    # z^2 - (omega - omega^2)/2 * z + 1 ... keep simple: (z - zeta6)(z - r) with r = (1/2)(1+i*sqrt3)/... skip
    # perfect matchings
    full = (1 << 45) - 1
    assert has_pm(full) and not has_pm(0)
    assert has_pm(PM10[0]) and has_pm(PM10[944])
    star = edges_to_mask([(0, d) for d in range(1, 10)])
    assert not has_pm(star)
    k55 = edges_to_mask([(c, d) for c in range(5) for d in range(5, 10)])
    assert has_pm(k55)
    two_k5 = edges_to_mask([p for p in PAIRS if (p[0] < 5) == (p[1] < 5)])
    assert not has_pm(two_k5)
    iso = full & ~edges_to_mask([(0, d) for d in range(1, 10)])
    assert not has_pm(iso)
_selftest()

if __name__ == "__main__":
    print("reviewer-cyclo-v1 selftest OK; |PM10| =", len(PM10), "; Phi72 =", cyclotomic(72))
