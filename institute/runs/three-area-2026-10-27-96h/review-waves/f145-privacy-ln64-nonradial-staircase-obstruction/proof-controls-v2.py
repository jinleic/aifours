#!/usr/bin/env python3
# proof-controls-v2.py  (v1 kept on record: its single failure was a checker range defect,
#   hull table k<=13 vs sampled |x|_1<=16; fixed here by extending the table to k<=17)
# Reviewer-authored exact controls for review wave
#   f145-privacy-ln64-nonradial-staircase-obstruction  (proof-reviewer slot)
# Pure Python 3 fractions.Fraction; NO author code is imported or executed
# (the candidate supplies prose only).  Every check is either a POSITIVE
# control (must pass) or a NEGATIVE control (a deliberately wrong input or a
# deliberately wrong law MUST be detected by the same checker).
# The script writes exactly one receipt file next to itself:
#   proof-controls-v2-receipt.json

from fractions import Fraction as F
from math import comb, ceil, gcd
import hashlib, json, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)


def clock():
    return subprocess.run(["/bin/date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                          capture_output=True, text=True).stdout.strip()


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def s(v):
    """stringify Fractions / tuples for the receipt"""
    if isinstance(v, F):
        return f"{v.numerator}/{v.denominator}"
    if isinstance(v, (tuple, list)):
        return [s(t) for t in v]
    if isinstance(v, dict):
        return {k: s(t) for k, t in v.items()}
    return v


T0 = clock()
R = {"script": os.path.basename(SELF), "script_sha256_at_start": sha256_file(SELF),
     "python": sys.version.split()[0], "clock_start_utc": T0, "checks": [], "any_fail": False,
     "info": {}}


def rec(name, ok, **info):
    R["checks"].append({"name": name, "ok": bool(ok), **{k: s(v) for k, v in info.items()}})
    if not ok:
        R["any_fail"] = True
        print("FAIL:", name, s(info))
    return bool(ok)


# ----------------------------------------------------------------------------
# 0. parameters exactly as candidate Eq.(1)
# ----------------------------------------------------------------------------
b = F(1, 64)
m = b / (1 - b)
a = F(3761763123, 10 ** 10)
z = F(3761763124, 10 ** 10)
eta = F(1, 100)
rec("0.m_equals_1_over_63", m == F(1, 63), m=m)
rec("0.z_minus_a_equals_1e-10", z - a == F(1, 10 ** 10))
rec("0.eta_lt_a_over_2", eta < a / 2, eta=eta, a_over_2=a / 2)
rec("0.a_gt_2eta_strict", a > 2 * eta)

# ----------------------------------------------------------------------------
# 1. geometric raw moments.  Independent derivation: memorylessness
#    P(N=k) = b P(N=k-1) (k>=1)  =>  E[N^j] = b E[(N+1)^j]
#    =>  E[N^j] = m * sum_{i<j} C(j,i) E[N^i].
#    Closed forms (candidate (6)) are polynomial identities in m of degree<=4;
#    agreement at 7 distinct m values proves them.
# ----------------------------------------------------------------------------


def raw_moments_recurrence(mm, jmax):
    E = [F(1)]
    for j in range(1, jmax + 1):
        E.append(mm * sum(comb(j, i) * E[i] for i in range(j)))
    return E


def raw_moments_closed(mm):
    return [F(1), mm, mm + 2 * mm ** 2, mm + 6 * mm ** 2 + 6 * mm ** 3,
            mm + 14 * mm ** 2 + 36 * mm ** 3 + 24 * mm ** 4]


for mm in [m, F(1), F(2), F(1, 2), F(1, 7), F(3, 5), F(5)]:
    rec(f"1.geometric_raw_moments_closed_form_m={mm}",
        raw_moments_recurrence(mm, 4) == raw_moments_closed(mm))

# second, fully independent route: exact partial sums + rigorous tail bound
# for k>=16, k^4 <= 2^k, so sum_{k>K} (1-b) b^k k^j <= (1-b)(2b)^{K+1}/(1-2b), K>=15
K1 = 120
tail1 = (1 - b) * (2 * b) ** (K1 + 1) / (1 - 2 * b)
E_closed = raw_moments_closed(m)
for j in range(1, 5):
    part = sum((1 - b) * b ** k * F(k) ** j for k in range(K1 + 1))
    rec(f"1.partial_sum_vs_closed_form_j={j}_K={K1}", abs(part - E_closed[j]) < tail1)


def M(j, g, mm=m):
    E = raw_moments_closed(mm)
    return sum(comb(j, i) * g ** (j - i) * E[i] for i in range(j + 1))


def M1(g): return M(1, g)
def M2(g): return M(2, g)
def M4(g): return M(4, g)


rec("1.M2_matches_candidate_(6)",
    all(M2(g) == g ** 2 + 2 * m * g + m + 2 * m ** 2 for g in [F(0), F(1), a, z, F(1, 3)]))
rec("1.M4_matches_candidate_(6)",
    all(M4(g) == g ** 4 + 4 * m * g ** 3 + 6 * (m + 2 * m ** 2) * g ** 2
        + 4 * (m + 6 * m ** 2 + 6 * m ** 3) * g + m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4
        for g in [F(0), F(1), a, z, F(1, 3)]))

# ----------------------------------------------------------------------------
# 2. exact polygon tools (shoelace area; Green's-theorem second moment)
# ----------------------------------------------------------------------------


def shoelace_area(P):
    n = len(P)
    acc = F(0)
    for i in range(n):
        x1, y1 = P[i]
        x2, y2 = P[(i + 1) % n]
        acc += x1 * y2 - x2 * y1
    return acc / 2


def second_moment(P):
    """integral of (x^2 + y^2) dA over a CCW simple polygon"""
    n = len(P)
    sx = F(0)
    sy = F(0)
    for i in range(n):
        x1, y1 = P[i]
        x2, y2 = P[(i + 1) % n]
        c = x1 * y2 - x2 * y1
        sx += (x1 * x1 + x1 * x2 + x2 * x2) * c
        sy += (y1 * y1 + y1 * y2 + y2 * y2) * c
    return (sx + sy) / 12


# sanity of the polygon formulas on shapes with hand-known integrals
sq = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
tri = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
rec("2.polygon_formula_unit_square", shoelace_area(sq) == 1 and second_moment(sq) == F(2, 3))
rec("2.polygon_formula_unit_triangle", shoelace_area(tri) == F(1, 2) and second_moment(tri) == F(1, 6))


def octagon(Rr, e):
    c = Rr - e
    return [(c, e), (e, c), (-e, c), (-c, e), (-c, -e), (-e, -c), (e, -c), (c, -e)]


def diamond(Rr):
    return [(Rr, F(0)), (F(0), Rr), (-Rr, F(0)), (F(0), -Rr)]


def cap(Rr, e):  # +x1 axis cap {x in R D : x1 >= R - e}, CCW
    return [(Rr - e, -e), (Rr, F(0)), (Rr - e, e)]


def L_closed(Rr): return 2 * Rr ** 2 - 4 * eta ** 2            # area of T_R
def Q_closed(Rr): return F(2, 3) * Rr ** 4 - 4 * Rr ** 2 * eta ** 2 + F(16, 3) * Rr * eta ** 3 - F(8, 3) * eta ** 4
def cap_moment_closed(Rr): return Rr ** 2 * eta ** 2 - F(4, 3) * Rr * eta ** 3 + F(2, 3) * eta ** 4


for Rr in [a, a + 1, a + 2, a + 5, F(7, 3), F(1), F(3, 100)]:
    oc = octagon(Rr, eta)
    dm = diamond(Rr)
    cp = cap(Rr, eta)
    rec(f"2.octagon_area_R={Rr}", shoelace_area(oc) == L_closed(Rr))
    rec(f"2.octagon_moment_R={Rr}", second_moment(oc) == Q_closed(Rr))
    rec(f"2.diamond_area_R={Rr}", shoelace_area(dm) == 2 * Rr ** 2)
    rec(f"2.diamond_moment_R={Rr}", second_moment(dm) == F(2, 3) * Rr ** 4)
    rec(f"2.cap_area_eta^2_R={Rr}", shoelace_area(cp) == eta ** 2)
    rec(f"2.cap_moment_(4)_R={Rr}", second_moment(cp) == cap_moment_closed(Rr))
    rec(f"2.diamond_minus_4caps_equals_octagon_R={Rr}",
        shoelace_area(dm) - 4 * shoelace_area(cp) == shoelace_area(oc)
        and second_moment(dm) - 4 * second_moment(cp) == second_moment(oc))

# ----------------------------------------------------------------------------
# 3. exact Minkowski-sum control for candidate (3):  S + kD = T_{a+k}
#    (convex hull of pairwise vertex sums, exact rational monotone chain)
# ----------------------------------------------------------------------------


def cross(o, p, q):
    return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])


def hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 1:
        return pts
    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def minkowski(P, Q):
    return hull([(p[0] + q[0], p[1] + q[1]) for p in P for q in Q])


def inside(P, x):  # closed convex CCW polygon
    n = len(P)
    return all(cross(P[i], P[(i + 1) % n], x) >= 0 for i in range(n))


S = hull(octagon(a, eta))
rec("3.S_is_a_genuine_octagon", len(S) == 8)
for k in [0, 1, 2, 3, 7, 10]:
    kD = hull(diamond(F(k))) if k > 0 else [(F(0), F(0))]
    MS = minkowski(S, kD)
    T = hull(octagon(a + k, eta))
    rec(f"3.S_plus_{k}D_equals_T_a+{k}_exact_hull", sorted(MS) == sorted(T), hull_vertices=len(MS))

# NEGATIVE control: with 2*eta > a the identity (3) is FALSE and the checker sees it.
a2, e2 = F(3, 10), F(2, 10)
S2 = hull([(sg * (a2 - e2), tg * (a2 - e2)) for sg in (1, -1) for tg in (1, -1)])   # S is then a square
MS2 = minkowski(S2, hull(diamond(F(1))))
T2 = hull(octagon(a2 + 1, e2))
bad = (a2 + 1 - e2, e2)
rec("3.NEGATIVE_2eta_gt_a_identity_fails_and_is_detected",
    sorted(MS2) != sorted(T2) and inside(T2, bad) and not inside(MS2, bad), witness=bad)

# ----------------------------------------------------------------------------
# 4. shell index from the DEFINITION via exact l1 distance to S (clipping lemma):
#    for p=|x1|, q=|x2|:  dist_1(x,S) = p+q - min(a, min(p,a-eta)+min(q,a-eta)).
#    n_S(x) = ceil(dist_1).  Cross-validated against hull membership.
# ----------------------------------------------------------------------------


def dist1_S(x, aa=a, ee=eta):
    p, q = abs(x[0]), abs(x[1])
    return p + q - min(aa, min(p, aa - ee) + min(q, aa - ee))


def n_index(x, aa=a, ee=eta):
    return ceil(dist1_S(x, aa, ee))


HULLS = [hull(octagon(a + k, eta)) for k in range(0, 18)]


def n_hull(x):
    for k, Hk in enumerate(HULLS):
        if inside(Hk, x):
            return k
    return None


rng = random.Random(20261028)


def rf(lo, hi, den=10 ** 6):
    return F(rng.randint(int(lo * den), int(hi * den)), den)


ok = True
boundary_pts = []
for k in range(0, 5):
    oc = octagon(a + k, eta)
    for i in range(8):
        v = oc[i]
        w = oc[(i + 1) % 8]
        boundary_pts += [v, ((v[0] + w[0]) / 2, (v[1] + w[1]) / 2)]
for x in boundary_pts + [(rf(-8, 8), rf(-8, 8)) for _ in range(4000)]:
    if n_index(x) != n_hull(x):
        ok = False
        break
rec("4.dist_index_equals_hull_index_on_boundary_and_random", ok)
# boundary semantics: an octagon vertex of T_{a+k} has index exactly k, and a
# point moved outward by any positive rational factor has index k+1
ok = True
for k in range(0, 5):
    for v in octagon(a + k, eta):
        if n_index(v) != k:
            ok = False
        vv = (v[0] * (1 + F(1, 10 ** 9)), v[1] * (1 + F(1, 10 ** 9)))
        if n_index(vv) != k + 1:
            ok = False
rec("4.boundary_vertices_index_k_and_just_outside_k+1", ok)
# nonradiality at a common l1 radius r in (a-eta, a)
r = (2 * a - eta) / 2
rec("4.nonradial_axis_index_1_diagonal_index_0", n_index((r, F(0))) == 1 and n_index((r / 2, r / 2)) == 0,
    r=r)

# ----------------------------------------------------------------------------
# 5. privacy-index control: |n_S(x+h) - n_S(x)| <= 1 for all h in closed D
# ----------------------------------------------------------------------------


def rand_in_D():
    t = rf(0, 1)
    rr = F(1) if rng.random() < 0.3 else rf(0, 1)      # 30% exactly on the boundary |h|_1 = 1
    return (rng.choice([1, -1]) * rr * t, rng.choice([1, -1]) * rr * (1 - t))


maxd = 0
seen = set()
for _ in range(30000):
    x = (rf(-6, 6), rf(-6, 6))
    h = rand_in_D()
    d = n_index((x[0] + h[0], x[1] + h[1])) - n_index(x)
    seen.add(d)
    maxd = max(maxd, abs(d))
rec("5.privacy_index_random_|dn|<=1", maxd <= 1 and seen == {-1, 0, 1}, deltas_seen=sorted(seen))
Hs = [(F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(0), F(-1)), (F(1, 2), F(1, 2)), (F(-1, 2), F(1, 2)),
      (F(1, 3), F(-2, 3)), (F(-2, 3), F(-1, 3)), (F(0), F(0)), (F(1, 7), F(6, 7))]
maxd = 0
for x in boundary_pts:
    for h in Hs:
        maxd = max(maxd, abs(n_index((x[0] + h[0], x[1] + h[1])) - n_index(x)))
rec("5.privacy_index_structured_boundary_|dn|<=1", maxd <= 1, max_abs_delta=maxd)

# NEGATIVE controls for the privacy checker
# (i) a shift OUTSIDE D (|h|_1 = 2) moves the index by 2
found = [abs(n_index((x[0] + 2, x[1])) - n_index(x)) for x in [(F(0), F(0)), (a - eta, F(0)), (F(1, 2), F(1, 2))]]
rec("5.NEGATIVE_shift_outside_D_changes_index_by_2", 2 in found, deltas=found)


# (ii) a deliberately wrong law (half-width shells) is caught with h in D
def n_half(x):
    return ceil(2 * dist1_S(x))


found = [abs(n_half((x[0] + h[0], x[1] + h[1])) - n_half(x))
         for x in [(F(0), F(0)), (a, F(0)), (F(1, 2), F(1, 2))]
         for h in [(F(1), F(0)), (F(0), F(1)), (F(1, 2), F(1, 2))]]
rec("5.NEGATIVE_halfwidth_shell_law_violates_bound", max(found) >= 2, deltas=found)

# ----------------------------------------------------------------------------
# 6. exact cost of P_S: closed form (5) and an independent direct layer sum
# ----------------------------------------------------------------------------
Z_S = 2 * M2(a) - 4 * eta ** 2
N_S = F(2, 3) * M4(a) - 4 * M2(a) * eta ** 2 + F(16, 3) * M1(a) * eta ** 3 - F(8, 3) * eta ** 4
J_S = N_S / Z_S
J_S_cand = F(4355768046089487574226880288026708390699272667,
             26721376640271909097532496900000000000000000000)
rec("6.J_PS_equals_candidate_(9)", J_S == J_S_cand, J_S=J_S, J_S_float=float(J_S))
# direct layer sum (no Abel summation): weights b^k on T_{a+k} \ T_{a+k-1}
K6 = 80
Zp = F(0)
Np = F(0)
Lprev = F(0)
Qprev = F(0)
for k in range(K6 + 1):
    Hk = hull(octagon(a + k, eta))
    Lk = shoelace_area(Hk)
    Qk = second_moment(Hk)
    Zp += b ** k * (Lk - Lprev)
    Np += b ** k * (Qk - Qprev)
    Lprev, Qprev = Lk, Qk
# tail: for k>=17, (a+k)^4 <= 2^k; shell measure <= 2(a+k)^2, shell moment <= (2/3)(a+k)^4
tailZ = 2 * (2 * b) ** (K6 + 1) / (1 - 2 * b)
tailN = F(2, 3) * (2 * b) ** (K6 + 1) / (1 - 2 * b)
rec("6.direct_layer_sum_Z_vs_closed_(5)", abs(Zp - Z_S) < tailZ)
rec("6.direct_layer_sum_N_vs_closed_(5)", abs(Np - N_S) < tailN)
R["info"]["Z_S"] = s(Z_S)
R["info"]["N_S"] = s(N_S)

# ----------------------------------------------------------------------------
# 7. staircase family: J(g) = M4(g)/(3 M2(g)); derivative sign quintic (7)
# ----------------------------------------------------------------------------


def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]


def pneg(p): return [-c for c in p]


def pmul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, c in enumerate(p):
        for j, d in enumerate(q):
            out[i + j] += c * d
    return out


def pderiv(p): return [i * p[i] for i in range(1, len(p))]
def peval(p, g): return sum(c * g ** i for i, c in enumerate(p))
def pint01(p): return sum(c / (i + 1) for i, c in enumerate(p))   # integral over [0,1]


def quintic_from_moments(mm):
    E = raw_moments_closed(mm)
    M2p = [E[2], 2 * E[1], F(1)]
    M4p = [E[4], 4 * E[3], 6 * E[2], 4 * E[1], F(1)]
    num = padd(pmul(pderiv(M4p), M2p), pneg(pmul(M4p, pderiv(M2p))))
    return [c / 2 for c in num], M2p, M4p


def quintic_claimed(mm):
    return [mm ** 2 * (1 + 2 * mm), -mm * (1 + 2 * mm) * (1 + 6 * mm), 12 * mm ** 3 - 2 * mm,
            2 * mm + 12 * mm ** 2, 5 * mm, F(1)]


for mm in [m, F(1), F(2), F(1, 2), F(1, 7), F(3, 5), F(5), F(11, 13)]:
    rec(f"7.quintic_(7)_identity_m={mm}", quintic_from_moments(mm)[0] == quintic_claimed(mm))
Pm, M2p, M4p = quintic_from_moments(m)
rec("7.M2_M4_all_coefficients_positive_(increasing_on_g>=0)", all(c > 0 for c in M2p) and all(c > 0 for c in M4p))
rec("7.P(0)>0", peval(Pm, F(0)) > 0, P0=peval(Pm, F(0)))
rec("7.P(a)<0", peval(Pm, a) < 0, Pa=float(peval(Pm, a)))
rec("7.P(z)>0", peval(Pm, z) > 0, Pz=float(peval(Pm, z)))
rec("7.P(1)>0", peval(Pm, F(1)) > 0, P1=peval(Pm, F(1)))
csign = [1 if c > 0 else (-1 if c < 0 else 0) for c in Pm]
changes = sum(1 for i in range(5) if csign[i] != csign[i + 1])
rec("7.descartes_two_sign_changes_no_zero_coeff", changes == 2 and 0 not in csign, coefficient_signs=csign)
rec("7.J(0)_equals_J(1)", peval(M4p, F(0)) * peval(M2p, F(1)) == peval(M4p, F(1)) * peval(M2p, F(0)))
# P positive on a dense sample of (z, 5] (consistent with no root past z)
rec("7.P_positive_sampled_(z,5]", all(peval(Pm, z + F(i, 1000) * (5 - z)) > 0 for i in range(1, 1001)))
# locate the smaller root r1 in (0,a) by exact bisection (informational)
lo, hi = F(0), a
for _ in range(40):
    mid = (lo + hi) / 2
    if peval(Pm, mid) > 0:
        lo = mid
    else:
        hi = mid
rec("7.smaller_root_bracket_in_(0,a)", 0 < lo < hi < a, r1_bracket=(float(lo), float(hi)))
# NEGATIVE control for the root enclosure: the adjacent 1e-10 cell (a-1e-10, a) has no sign change
rec("7.NEGATIVE_shifted_bracket_(a-1e-10,a)_has_no_sign_change",
    not (peval(Pm, a - F(1, 10 ** 10)) < 0 < peval(Pm, a)))


def J(g): return M4(g) / (3 * M2(g))


R["info"]["J_staircase_at_0"] = float(J(F(0)))
R["info"]["J_staircase_at_a"] = float(J(a))
R["info"]["J_staircase_at_z"] = float(J(z))

# ----------------------------------------------------------------------------
# 8. the gap: LB = M4(a)/(3 M2(z)) - J(P_S), parent correction, >1e-6
# ----------------------------------------------------------------------------
LB = M4(a) / (3 * M2(z)) - J_S
corr_num = 55892104628095766169604064637687395172793197064705238995982813
corr_den = 28589579218686463271455054512504719394059809867200000000000000000000
cand_den = 28589579218686463271455054512504719394059809867200000000000000
rec("8.gap_LB_equals_parent_corrected_fraction", LB == F(corr_num, corr_den), LB=LB, LB_float=float(LB))
rec("8.parent_corrected_fraction_is_in_lowest_terms", gcd(corr_num, corr_den) == 1)
rec("8.candidate_printed_denominator_is_exactly_1e6_too_small", corr_den == cand_den * 10 ** 6)
rec("8.gap_LB_gt_1e-6", LB > F(1, 10 ** 6))
rec("8.candidate_misprint_value_exceeds_J_PS_itself_(impossible)", F(corr_num, cand_den) > J_S)
UB = M4(z) / (3 * M2(a)) - J_S
rec("8.true_family_gap_enclosure_LB<UB", LB < UB, UB_float=float(UB))
rec("8.M4(a)<M4(z)_and_M2(a)<M2(z)", M4(a) < M4(z) and M2(a) < M2(z))
# author-reported failed coarse bracket reproduces a NEGATIVE outward gap (sensitivity control)
LBc = M4(F(37617, 100000)) / (3 * M2(F(37618, 100000))) - J_S
rec("8.NEGATIVE_coarse_bracket_gives_negative_outward_gap", LBc < 0, LBc_float=float(LBc))
# every-staircase strict inequality chain, evaluated at a sample of gammas incl. endpoints
rec("8.sampled_gammas_J(Pgamma)>J_PS+1e-6",
    all(J(F(i, 97)) > J_S + F(1, 10 ** 6) for i in range(0, 98)))

# ----------------------------------------------------------------------------
# 9. l1-radial identity J = (2/3) W  (ONLY the identity; the unsupplied MDA26
#    premise is NOT checked here).  In l1-polar coordinates x = r (t, 1-t) on
#    each edge the Jacobian is r, so the edge average of |x|_2^2 / |x|_1^2 is
#    int_0^1 (t^2 + (1-t)^2) dt  =  2/3.
# ----------------------------------------------------------------------------
edge_poly = padd(pmul([F(0), F(1)], [F(0), F(1)]), pmul([F(1), F(-1)], [F(1), F(-1)]))   # t^2 + (1-t)^2
rec("9.radial_identity_edge_average_two_thirds", pint01(edge_poly) == F(2, 3) and pint01([F(1)]) == 1)
# consistency: int_{RD}|x|_2^2 = (2/3) R^4 (polygon) while int_{RD}|x|_1^2 = int_0^R r^2 * 4r dr = R^4
rec("9.int_RD_|x|_2^2_two_thirds_of_int_RD_|x|_1^2",
    all(second_moment(diamond(Rr)) == F(2, 3) * Rr ** 4 for Rr in [F(1), F(2), F(7, 3)]))

# ----------------------------------------------------------------------------
T1 = clock()
R["clock_end_utc"] = T1
R["n_checks"] = len(R["checks"])
R["n_fail"] = sum(1 for c in R["checks"] if not c["ok"])
R["script_sha256_at_end"] = sha256_file(SELF)
out = os.path.join(HERE, "proof-controls-v2-receipt.json")
with open(out, "w") as fh:
    json.dump(R, fh, indent=1)
print(f"checks={R['n_checks']} fail={R['n_fail']} start={T0} end={T1}")
print("J_S =", s(J_S), "~", float(J_S))
print("LB  =", s(LB), "~", float(LB))
print("UB  ~", float(UB), " J(0) ~", float(J(F(0))), " J(a) ~", float(J(a)))
print("receipt:", out)
