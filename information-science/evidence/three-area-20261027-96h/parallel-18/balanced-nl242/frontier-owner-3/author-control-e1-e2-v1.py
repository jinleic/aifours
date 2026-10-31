#!/usr/bin/env python3
"""Author finite-identity control for the f270 erratum (E1, E2) of
successor-20261029-info6-uv-caller-coupling-necessary-v1.md.

Standard library only; seeded synthetic balanced Boolean functions on F2^n
(n=5,7,9); NO search over the NL242 target space, no spectrum/atom selection.
Checks (all exact integer arithmetic):
  A. u/v construction: uv=0, u^2+v^2=1, s|_V=u+v, s|_{V+T}=u-v
  B. Theorem 1 caller split: W_f(r)=2*Uhat(r) on K; W_f(r+a0)=2*Vhat(r)
  C. Lemma 1: all W_f == 0 (mod 4)
  D. E1 count identity: q := #{y in V: f(y+T)=1} == p + n_minus  EXACTLY
     (p = #{v=+1}, n_minus = #{u=-1}); and wt checks
     wt(f|_V) = (|supp v| - p) + n_minus, total wt = 2^(n-1)
  E. pair identity: T == XOR(supp_v) xor (q mod 2)*T  exactly
  F. E2 reconstruction: rebuilt f' from (u,v) has
     XOR(supp f') == XOR(supp_v) xor ((p + n_minus) mod 2)*T ; and when
     n_minus even & p odd & XOR(supp_v)==0 this equals T
  G. sum(v) = 2p - |supp v|; sum(v) = 2 (mod 4) iff p odd
Covers both m = |supp u| parities mod 4 where they occur (m is data-dependent).
"""
import random, sys

def dot(a, b):  # a,b bitmasks; pairing
    x, c = a & b, 0
    while x: c ^= 1; x &= x - 1
    return c

def xor_all(xs):
    t = 0
    for x in xs: t ^= x
    return t

def run(n, seed):
    rng = random.Random(seed)
    N = 1 << n
    while True:
        supp = rng.sample(range(N), N // 2)
        T = xor_all(supp)
        if T != 0: break
    f = [0]*N; s = [1]*N
    for x in supp: f[x] = 1; s[x] = -1
    a0 = next(a for a in range(1, N) if dot(a, T) == 1)
    V = [y for y in range(N) if dot(a0, y) == 0]
    u = {}; v = {}
    for y in V:
        u[y] = (s[y] + s[y ^ T]) // 2
        v[y] = (s[y] - s[y ^ T]) // 2
    # A
    for y in V:
        assert u[y]*v[y] == 0 and u[y]**2 + v[y]**2 == 1
        assert s[y] == u[y] + v[y] and s[y ^ T] == u[y] - v[y]
    # B, C
    Wf = [sum(s[x]*(-1)**dot(a, x) for x in range(N)) for a in range(N)]
    for a in range(N):
        assert Wf[a] % 4 == 0, "Lemma1 fail"
    for r in range(N):
        if dot(r, T) == 0:
            Uh = sum(u[y]*(-1)**dot(r, y) for y in V)
            assert Wf[r] == 2*Uh, "caller split K fail"
        else:
            # a = r has a.T=1; its V-character equals (r+a0)'s
            Vh = sum(v[y]*(-1)**dot(r ^ a0, y) for y in V)
            assert Wf[r] == 2*Vh, "caller split off-K fail"
    m = sum(1 for y in V if u[y] != 0)
    n_minus = sum(1 for y in V if u[y] == -1)
    n_plus = sum(1 for y in V if u[y] == 1)
    assert n_plus == n_minus and n_plus + n_minus == m
    p = sum(1 for y in V if v[y] == 1)
    suppv = 2**(n-1) - m
    # D
    q = sum(1 for y in V if f[y ^ T] == 1)
    assert q == p + n_minus, "E1 count identity fail"
    wtV = sum(f[y] for y in V)
    assert wtV == (suppv - p) + n_minus
    assert sum(f) == 2**(n-1)
    # E
    xs = xor_all([y for y in V if v[y] != 0])
    assert T == xs ^ ((q % 2) * T), "pair identity fail"
    assert all(dot(a0, y) == 0 for y in [y for y in V if v[y] != 0])
    # F  (rebuild f' from u,v exactly as the manuscript does)
    f2 = [0]*N
    for y in V:
        f2[y] = (1 - (u[y] + v[y])) // 2
        f2[y ^ T] = (1 - (u[y] - v[y])) // 2
    assert xor_all([x for x in range(N) if f2[x] == 1]) == xs ^ (((p + n_minus) % 2) * T), "E2 formula fail"
    if n_minus % 2 == 0 and p % 2 == 1 and xs == 0:
        assert xor_all([x for x in range(N) if f2[x] == 1]) == T, "E2 sufficiency fail"
    # G  (exact identity; the biconditional sum(v)=2 mod 4 iff p odd is
    #    SCOPE-CONDITIONAL: it needs |supp v| = 0 mod 4, true at the frozen
    #    scope where |supp v| = 140; check it only under that hypothesis)
    sumv = sum(v[y] for y in V)
    suppv = 2**(n-1) - m
    assert sumv == 2*p - suppv
    if suppv % 4 == 0:
        assert (sumv % 4 == 2) == (p % 2 == 1)
    return n, seed, m, q, p, n_minus, q - p

def main():
    seen_m_parity = set()
    rows = []
    cases = [(5, 1), (5, 2), (7, 3), (7, 4), (9, 5), (9, 6), (9, 7), (9, 8)]
    for n, seed in cases:
        r = run(n, seed)
        rows.append(r)
        seen_m_parity.add(r[2] % 4)
    for r in rows:
        print("PASS n=%d seed=%d m=%d m%%4=%d q=%d p=%d n_minus=%d q-p-n_minus=0" % (r[0], r[1], r[2], r[2] % 4, r[3], r[4], r[5]))
    print("m mod-4 classes covered:", sorted(seen_m_parity))
    print("ALL CHECKS PASS")

if __name__ == "__main__":
    main()
