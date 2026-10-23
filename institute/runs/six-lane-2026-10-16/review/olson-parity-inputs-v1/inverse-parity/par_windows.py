#!/usr/bin/env python3
"""PAR aid: half windows (README Sec. 1) for RGR run data, and enumeration of
inherited PAR violators at N = 4p-2 (k <= p, some even run).  Aid only.

Conventions: runs indexed 0..k-1; rotation run i (a[i], b[i]) is followed by
reflection run S_i (l[i]); interval (s, t] = rotation runs s+1..t (mod k), boundary
reflection runs S_s and S_t; a pattern P is a bitmask of rotation runs (z_i = +1).
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'code'))


def params(a, b, l, p):
    k = len(a); A = sum(a); B = sum(b); R = A + B; F = sum(l)
    oF = sum(x & 1 for x in l)
    H = (F - oF) // 2
    kappa = p - 1 - H
    return dict(k=k, A=A, B=B, R=R, F=F, oF=oF, H=H, kappa=kappa)


def half_window_mask(P, a, b, l, p):
    """Exact half window I(P) = [L, U] for an arbitrary pattern P (bitmask), from the
    frozen formula (README Sec. 1).  Returns (L, U) (possibly L > U = empty)."""
    k = len(a); R = sum(a) + sum(b); F = sum(l)
    Phi = 0; delta = 0; Ep = 0
    for i in range(k):
        zi = (P >> i) & 1; zn = (P >> ((i + 1) % k)) & 1; f = zi ^ zn
        Phi += f
        if (l[i] - f) & 1:
            delta += 1
        Ep += a[i] if zi else b[i]
    Em = R - Ep; c = (F - delta) // 2
    U = min(p - Phi // 2, Ep + c - p, Ep // 2)
    L = max(-(p - Phi // 2), p - c - Em, -(Em // 2))
    return L, U


def interval_mask(s, t, k):
    """bitmask of rotation runs s+1..t (mod k); s != t (mod k)."""
    m = 0; i = (s + 1) % k
    while True:
        m |= 1 << i
        if i == t % k:
            break
        i = (i + 1) % k
    return m


def interval_window(s, t, a, b, l, p, kap):
    """(L, U) for interval (s, t] via the kappa form (README Sec. 1)."""
    k = len(a)
    P = interval_mask(s, t, k)
    Ep = sum(a[i] if (P >> i) & 1 else b[i] for i in range(k))
    Em = sum(a) + sum(b) - Ep
    e = (l[s % k] % 2 == 0) + (l[t % k] % 2 == 0)
    U = min(p - 1, Ep - kap - e, Ep // 2)
    L = max(-(p - 1), kap + e - Em, -(Em // 2))
    return L, U


def inherited(a, b, l, p):
    r = [x + y for x, y in zip(a, b)]
    R = sum(r); F = sum(l); H = sum(x // 2 for x in l)
    if R > 3 * p - 2: return False
    if F + sum(x // 2 for x in r) > 3 * p - 2: return False
    if R + H > 3 * p - 2: return False
    if H > p - 1: return False
    if max(a) > p - 1 or max(b) > p - 1: return False
    return True


def compositions(n, parts):
    if parts == 0:
        if n == 0:
            yield ()
        return
    for v in range(1, n - parts + 2):
        for rest in compositions(n - v, parts - 1):
            yield (v,) + rest


def run_data(p, N, kmin, kmax, violators_only=True):
    """Yield (a, b, l) for RGR run data at length N, k in [kmin, kmax], canonical
    under cyclic rotation of (r, l, a), inherited, and (if violators_only) with an
    even run."""
    for k in range(kmin, kmax + 1):
        for parts in compositions(N, 2 * k):
            r = parts[0::2]; l = parts[1::2]
            pairs = list(zip(r, l))
            if any(pairs[s:] + pairs[:s] < pairs for s in range(1, k)):
                continue
            if violators_only and all(x % 2 for x in r) and all(x % 2 for x in l):
                continue
            Hl = sum(x // 2 for x in l)
            if Hl > p - 1:
                continue
            ranges = [range(max(0, x - (p - 1)), min(x, p - 1) + 1) for x in r]
            for aa in itertools.product(*ranges):
                a = list(aa); b = [x - y for x, y in zip(r, a)]
                trip = list(zip(r, l, a))
                if any(trip[s:] + trip[:s] < trip for s in range(1, k)):
                    continue
                if not inherited(a, b, list(l), p):
                    continue
                yield a, b, list(l)
