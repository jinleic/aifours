#!/usr/bin/env python3
"""Exact interval certificate using integers, Fractions and isqrt only.

Part 1: for an explicit 11-atom law nu0 on [0,1], rigorous bounds
   F(nu0) in [F_lo, F_hi]  (so kappa >= F_lo),  sup_t f0(t) <= SUP_hi,
   with f0(t)=E[B_t^2/sqrt(Y0)], and the tangent bound kappa <= (F_hi+SUP_hi)/2.
Part 2: rigorous lower bound V_lo for the relaxed two-stage lag-eta0 strategy
   V = N/D,  N = 2 phi(theta) + E[sqrt(eta0 B^2+(1-eta0)(B+sqrt(c) zeta)^2); |B|<theta],
   D = 1 + (sqrt(1+c)-1) P(|B|<theta).
Every Darboux integrand is nonincreasing (justified in the written record). All values
are rounded outward to integers scaled by 2^SC; floats only prioritise refinement.
"""
from fractions import Fraction as Fr
from math import isqrt
import heapq

SC = 96
ONE = 1 << SC


def fl(x):  # floor(x*ONE) for Fraction x
    return (x.numerator * ONE) // x.denominator


def ce(x):  # ceil(x*ONE)
    return -((-x.numerator * ONE) // x.denominator)


def ffl(x):  # floor of an already-scaled Fraction
    return x.numerator // x.denominator


def fce(x):  # ceil of an already-scaled Fraction
    return -((-x.numerator) // x.denominator)


def invsqrt_scaled(x):
    """(lo,hi) integers with lo<=ONE/sqrt(x)<=hi for rational x>0."""
    num = ONE * ONE * x.denominator
    lo = isqrt(num // x.numerator)
    hi = isqrt(-((-num) // x.numerator)) + 1
    return lo, hi


def sqrt_scaled(x):
    num = ONE * ONE * x.numerator
    lo = isqrt(num // x.denominator)
    hi = isqrt(-((-num) // x.denominator)) + 1
    return lo, hi


def pi_bounds():
    def atan_partial(q, last):
        return sum((Fr((-1) ** k, (2 * k + 1) * q ** (2 * k + 1)) for k in range(last + 1)), Fr(0))
    lo = 16 * atan_partial(5, 11) - 4 * atan_partial(239, 2)
    hi = 16 * atan_partial(5, 10) - 4 * atan_partial(239, 3)
    assert lo < hi
    return lo, hi


PI_LO, PI_HI = pi_bounds()
ISP_LO = Fr(invsqrt_scaled(PI_HI)[0], ONE)    # <= 1/sqrt(pi)
ISP_HI = Fr(invsqrt_scaled(PI_LO)[1], ONE)    # >= 1/sqrt(pi)


def alt_bounds(y, kind):
    """Bracket S(y)=sum(-1)^n y^n/(n!(2n+1)) [kind='erf'] or e^{-y} [kind='exp']."""
    t = Fr(1)
    s = Fr(1)
    n = 0
    sums = [s]
    while True:
        if kind == 'erf':
            t = t * y * (2 * n + 1) / ((n + 1) * (2 * n + 3))
        else:
            t = t * y / (n + 1)
        n += 1
        s = s - t if n % 2 == 1 else s + t
        sums.append(s)
        if n > y + 2 and t < Fr(1, 1 << 120):
            break
    a, b = sums[-1], sums[-2]
    return min(a, b), max(a, b)


def dy(y, up):  # outward dyadic rounding of a rational to 2^-64 grid
    z = Fr(y.numerator * (1 << 64) // y.denominator, 1 << 64)
    return z if not up else z + Fr(1, 1 << 64)


# ---------------- Part 1 ----------------
S = [Fr(7, 10), Fr(19, 25), Fr(81, 100), Fr(17, 20), Fr(177, 200), Fr(183, 200),
     Fr(47, 50), Fr(24, 25), Fr(39, 40), Fr(247, 250), Fr(1)]
P = [Fr(n, 10000) for n in (127, 174, 229, 260, 293, 320, 337, 342, 349, 434, 7135)]
K = len(S)
assert sum(P) == 1 and all(p > 0 for p in P) and all(S[i] < S[i + 1] for i in range(K - 1))
GAPS = [S[0]] + [S[i] - S[i - 1] for i in range(1, K)]
DIAG0 = [1 / GAPS[i] + (1 / GAPS[i + 1] if i < K - 1 else 0) for i in range(K)]
OFF = [-1 / GAPS[i + 1] for i in range(K - 1)]
DETSIG = Fr(1)
for g in GAPS:
    DETSIG *= g
DETD = Fr(1)
for p in P:
    DETD *= p
NQ = 2 + K + 2 * (K - 1)


def node1(u):
    two_u2 = 2 * u * u
    d = [DIAG0[i] + two_u2 * P[i] for i in range(K)]
    th = [Fr(1), d[0]]
    for i in range(1, K):
        th.append(d[i] * th[i] - OFF[i - 1] ** 2 * th[i - 1])
    ph = [Fr(0)] * (K + 2)
    ph[K] = Fr(1)
    ph[K - 1] = d[K - 1]
    for i in range(K - 2, -1, -1):
        ph[i] = d[i] * ph[i + 1] - OFF[i] ** 2 * ph[i + 2]
    detT = th[K]
    assert detT == ph[0] and detT > 0
    rl, rh = invsqrt_scaled(DETSIG * detT)
    cd = [th[i] * ph[i + 1] / detT for i in range(K)]
    co = [-OFF[i] * th[i] * ph[i + 2] / detT for i in range(K - 1)]
    iu2 = 1 / (u * u)
    out = [(ffl((ONE - rh) * iu2), fce((ONE - rl) * iu2)), (rl, rh)]
    for i in range(K):
        out.append((ffl(rl * cd[i]), fce(rh * cd[i])))
    for sgn in (1, -1):
        for i in range(K - 1):
            q = cd[i] + cd[i + 1] + 2 * sgn * co[i]
            assert q >= 0
            out.append((ffl(rl * q), fce(rh * q)))
    return out


def node1_zero():
    vals = [sum(P[i] * S[i] for i in range(K)), Fr(1)] + list(S)
    for sgn in (1, -1):
        vals += [S[i] + S[i + 1] + 2 * sgn * S[i] for i in range(K - 1)]
    return [(fl(v), ce(v)) for v in vals]


def darboux(fn, v0, edges, nq, prio, budget):
    cache = {Fr(0): v0}
    def val(x):
        if x not in cache:
            cache[x] = fn(x)
        return cache[x]
    lows = [0] * nq          # scaled by ONE, times widths (Fractions)
    highs = [0] * nq
    lows = [Fr(0)] * nq
    highs = [Fr(0)] * nq
    heap = []
    seq = 0
    def push(a, b):
        nonlocal seq
        va, vb = val(a), val(b)
        w = b - a
        lo = [w * vb[q][0] for q in range(nq)]
        hi = [w * va[q][1] for q in range(nq)]
        pr = sum(prio[q] * float(hi[q] - lo[q]) for q in range(nq)) / ONE
        for q in range(nq):
            lows[q] += lo[q]
            highs[q] += hi[q]
        heapq.heappush(heap, (-pr, seq, a, b, lo, hi))
        seq += 1
    for a, b in zip(edges, edges[1:]):
        push(a, b)
    for _ in range(budget):
        _, _, a, b, lo, hi = heapq.heappop(heap)
        for q in range(nq):
            lows[q] -= lo[q]
            highs[q] -= hi[q]
        m = (a + b) / 2
        push(a, m)
        push(m, b)
    return [x / ONE for x in lows], [x / ONE for x in highs], len(cache)


def part1(budget):
    U = Fr(128)
    edges = [Fr(0)] + [Fr(2) ** j / 64 for j in range(14)]
    prio = [6.0, 1.0] + [1.0] * K + [0.3] * (2 * (K - 1))
    lows, highs, nodes = darboux(node1, node1_zero(), edges, NQ, prio, budget)
    sdd_lo = Fr(sqrt_scaled(DETSIG * DETD)[0], ONE)
    C = 1 / sdd_lo                                  # >= (detSig detD)^(-1/2)
    tp = Fr(sqrt_scaled(Fr(2) ** K)[0], ONE)        # <= 2^(K/2)
    g_tail_lo = 1 / U - C / tp / (K + 1) / U ** (K + 1)
    g_tail_hi = 1 / U
    inv_tail = C / tp / (K - 1) / U ** (K - 1)
    def qtail(qc):
        return C * qc / (2 * tp) / (K + 1) / U ** (K + 1)
    F_lo = ISP_LO * (lows[0] + g_tail_lo)
    F_hi = ISP_HI * (highs[0] + g_tail_hi)
    jl, jh = 2 * ISP_LO, 2 * ISP_HI
    Jinv_hi = jh * (highs[1] + inv_tail)
    Jd_hi = [jh * (highs[2 + i] + qtail(1 / P[i])) for i in range(K)]
    Jp_hi = [jh * (highs[2 + K + i] + qtail(2 * (1 / P[i] + 1 / P[i + 1]))) for i in range(K - 1)]
    Jm_lo = [jl * lows[2 + K + (K - 1) + i] for i in range(K - 1)]
    Jx_hi = [(Jp_hi[i] - Jm_lo[i]) / 4 for i in range(K - 1)]
    def qmax(a0, a1, a2):
        c = [a0, a0 + a1 + a2]
        if a2 < 0:
            lam = -a1 / (2 * a2)
            if 0 < lam < 1:
                c.append(a0 + a1 * lam + a2 * lam * lam)
        return max(c)
    sup = qmax(Fr(0), S[0] * Jinv_hi, Jd_hi[0] - S[0] * Jinv_hi)
    for j in range(K - 1):
        A, B, Cc, L, E = Jd_hi[j], Jx_hi[j], Jd_hi[j + 1], GAPS[j + 1], Jinv_hi
        sup = max(sup, qmax(A, -2 * A + 2 * B + L * E, A - 2 * B + Cc - L * E))
    return F_lo, F_hi, sup, (F_hi + sup) / 2, nodes


# ---------------- Part 2 ----------------
ETA0, THETA, CC = Fr(37, 50), Fr(9, 40), Fr(27, 100)
YIN = THETA * THETA / 2
XIN_LO = Fr(sqrt_scaled(YIN)[0], ONE)
XIN_HI = Fr(sqrt_scaled(YIN)[1], ONE)
_s = alt_bounds(YIN, 'erf')
PIN_LO = 2 * ISP_LO * XIN_LO * _s[0]
PIN_HI = min(Fr(1), 2 * ISP_HI * XIN_HI * _s[1])
YCUT = Fr(9)


def node2(u):
    alpha = u * u * (1 - ETA0)
    one2 = 1 + 2 * alpha * CC
    Kk = 2 * (u * u * ETA0 + alpha / one2)
    y = THETA * THETA * (1 + Kk) / 2
    if y > YCUT:
        erf_hi = Fr(1)
    else:
        s_hi = alt_bounds(dy(y, False), 'erf')[1]       # S decreasing in y
        x_hi = Fr(sqrt_scaled(y)[1], ONE)
        erf_hi = min(Fr(1), 2 * ISP_HI * x_hi * s_hi)
    a_hi = Fr(invsqrt_scaled(one2)[1], ONE)
    b_hi = Fr(invsqrt_scaled(1 + Kk)[1], ONE)
    lo = (PIN_LO - a_hi * b_hi * erf_hi) / (u * u)
    return [(fl(lo), None)]


def part2(budget):
    U = Fr(128)
    edges = [Fr(0)] + [Fr(2) ** j / 1024 for j in range(18)]
    cache = {}
    def lo(x):
        if x not in cache:
            cache[x] = node2(x)[0][0]
        return cache[x]
    total = Fr(0)
    heap = []
    seq = 0
    def push(a, b):
        nonlocal seq, total
        c = (b - a) * lo(b)
        total += c
        ref = lo(a) if a > 0 else lo(b) * 4
        heapq.heappush(heap, (-float((b - a) * (ref - lo(b))) / ONE, seq, a, b, c))
        seq += 1
    for a, b in zip(edges, edges[1:]):
        push(a, b)
    for _ in range(budget):
        _, _, a, b, c = heapq.heappop(heap)
        total -= c
        m = (a + b) / 2
        push(a, m)
        push(m, b)
    integral_lo = total / ONE
    tail_lo = PIN_LO / U - Fr(invsqrt_scaled(2 * ETA0)[1], ONE) / (2 * U * U)
    T2_lo = ISP_LO * (integral_lo + tail_lo)
    e_lo = alt_bounds(THETA * THETA / 2, 'exp')[0]
    twophi_lo = 2 * e_lo * Fr(invsqrt_scaled(2 * PI_HI)[0], ONE)
    N_lo = twophi_lo + T2_lo
    D_hi = 1 + (Fr(sqrt_scaled(1 + CC)[1], ONE) - 1) * PIN_HI
    return N_lo / D_hi, len(cache), T2_lo, twophi_lo, D_hi


def dn(x, k=7):  # decimal string rounded DOWN (for lower bounds)
    q = (x.numerator * 10 ** k) // x.denominator
    return '%s%d.%0*d' % ('-' if q < 0 else '', abs(q) // 10 ** k, k, abs(q) % 10 ** k)


def up(x, k=7):  # decimal string rounded UP (for upper bounds)
    q = -((-x.numerator * 10 ** k) // x.denominator)
    return '%s%d.%0*d' % ('-' if q < 0 else '', abs(q) // 10 ** k, k, abs(q) % 10 ** k)


def main(b1=20000, b2=6000):
    F_lo, F_hi, sup, k_hi, n1 = part1(b1)
    V_lo, n2, t2, tp, dh = part2(b2)
    print('pi in [%s, %s]' % (dn(PI_LO, 15), up(PI_HI, 15)))
    print('Part1: nodes %d; F(nu0) in [%s, %s]; sup f0 <= %s' % (n1, dn(F_lo), up(F_hi), up(sup)))
    print('Part1: %s <= kappa <= %s' % (dn(F_lo), up(k_hi)))
    print('Part2: eta0=%s theta=%s c=%s; nodes %d' % (ETA0, THETA, CC, n2))
    print('Part2: T2 >= %s; 2phi >= %s; D <= %s; V >= %s' % (dn(t2), dn(tp), up(dh), dn(V_lo)))
    assert V_lo > k_hi, 'certificate failed'
    print('PASS: exact rational inequality V_lo > kappa_hi verified; V_lo - kappa_hi >= %s' % dn(V_lo - k_hi))


if __name__ == '__main__':
    main()
