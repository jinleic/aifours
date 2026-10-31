#!/usr/bin/env python3
"""reviewer-controls-c123-v1.py  (f136 review, candidates 1-3)

Independent exact controls written from scratch by the reviewer.  No author
checker is imported or executed.  All geometry/arithmetic uses
fractions.Fraction; floats appear only in printed ratios and in one mpmath
quadrature cross-check of an elementary integral.

Conventions (reviewer's own, stated in review-v1.md):
  S = [-1/2,1/2]^2 ; D = closed l1 unit diamond ; b in (0,1) ; m = b/(1-b)
  Q  = product staircase, density b^(n1+n2)/Z1^2, n_i = ceil(max(|x_i|-1/2,0)), Z1 = 1+2m
  P_K = shell law with core K: density b^(n_K(x))/Z_K, n_K(x) = min{k : x in K+kD}
  TV(mu,nu) = sup_A |mu(A)-nu(A)| = integral (f-g)_+
"""
from fractions import Fraction as F
import math, sys, hashlib, time, random, os

OUT = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); OUT.append(s)

FAILS = []
def check(tag, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    if not cond: FAILS.append(tag)
    say(f"[{status}] {tag} {detail}")

# ---------------- exact convex polygon toolkit ----------------
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]          # CCW, no collinear vertices

def area(poly):
    n = len(poly)
    if n < 3:
        return F(0)
    s = F(0)
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i+1) % n]
        s += x1*y2 - x2*y1
    return s/2

def minkowski(P, Q):
    return hull([(p[0]+q[0], p[1]+q[1]) for p in P for q in Q])

def scale(P, k):
    return [(k*p[0], k*p[1]) for p in P]

def translate(P, v):
    return [(p[0]+v[0], p[1]+v[1]) for p in P]

def _isect(p1, p2, a, b):
    d1 = cross(a, b, p1); d2 = cross(a, b, p2)
    lam = d1/(d1-d2)
    return (p1[0]+lam*(p2[0]-p1[0]), p1[1]+lam*(p2[1]-p1[1]))

def clip(subject, clipper):
    """Sutherland-Hodgman: convex CCW subject clipped by convex CCW clipper (exact)."""
    out = list(subject)
    n = len(clipper)
    for i in range(n):
        a = clipper[i]; b = clipper[(i+1) % n]
        inp = out; out = []
        if not inp:
            break
        s = inp[-1]; s_in = cross(a, b, s) >= 0
        for p in inp:
            p_in = cross(a, b, p) >= 0
            if p_in:
                if not s_in:
                    out.append(_isect(s, p, a, b))
                out.append(p)
            elif s_in:
                out.append(_isect(s, p, a, b))
            s, s_in = p, p_in
    return out

def inside(poly, x):
    n = len(poly)
    return all(cross(poly[i], poly[(i+1) % n], x) >= 0 for i in range(n))

H = F(1, 2)
D = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))]
S = [(H, -H), (H, H), (-H, H), (-H, -H)]
def rect(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
def K_clip(t):
    return hull([(H, H-t), (H-t, H), (-H+t, H), (-H, H-t), (-H, -H+t), (-H+t, -H), (H-t, -H), (H, -H+t)])

# ---------------- closed forms under review ----------------
def Z1(b):  m = b/(1-b); return 1 + 2*m
def q0(b):  return ((1-b)/(1+b))**2
def ZS(b):  m = b/(1-b); return 1 + 6*m + 4*m*m
def Zt(b, t):
    m = b/(1-b); A = 1 - 2*t*t
    return A + (6-4*t)*m + 4*m*m
def U_square(b):
    return 2*b*(1-b)*(1+2*b-b*b)/((1+b)**2*(1+4*b-b*b))
def L_c1(b, d):      # candidate 1, side-delta/4 corner square
    return 2*b*(1-d)**2*q0(b)*(1-b)/(1 + 32*b*(1-d)**2/(d*d))
def L_c2(b, d):      # candidate 2/3, exact overlap triangle (float because of log)
    return float(2*b*(1-b)*q0(b)*(1-d)**2)/(1 + 8*float(b)*(1/float(d) + math.log(float(d)) - 1))
def Q_idx_ge2(b):
    return 1 - q0(b)*(1+4*b)          # = (8b^2-4b^3)/(1+b)^2
def E_clip(b, t):
    """Reviewer's explicit part of TV(Q,P_t) (valid when q0*Zt>=1): core deficit +
    one-axis strip mismatch on strips inside K_t+D (area 4-4t^2) + excluded strip
    triangles (area 4t^2, where P_t has index 2)."""
    A = 1 - 2*t*t; z = Zt(b, t); qq = q0(b)
    core = qq - (A + b*(1-A))/z
    strips_in = (4 - 4*t*t)*b*(qq - 1/z)
    strips_out = 4*t*t*(b*qq - b*b/z)
    return core + strips_in + strips_out
def U_clip(b, t):
    return E_clip(b, t) + Q_idx_ge2(b)

say("reviewer-controls-c123-v1.py  start", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
say("python", sys.version.split()[0])

# ============ A. Minkowski area of square core ============
say("\n== A. |S+tD| = 1+4t+2t^2 (exact hull areas) ==")
for t in [F(1,3), F(1,2), F(1), F(7,5), F(3)]:
    a = area(minkowski(S, scale(D, t)))
    check(f"A |S+{t}D|", a == 1 + 4*t + 2*t*t, f"area={a}")

# ============ B. Minkowski area of clipped square ============
say("\n== B. |K_t+kD| = (1-2t^2)+(4-4t)k+2k^2 (exact) ; negative control with unclipped 4k ==")
for t in [F(1,10), F(1,8), F(1,4), F(2,5)]:
    Kt = K_clip(t)
    check(f"B |K_t| t={t}", area(Kt) == 1 - 2*t*t, f"area={area(Kt)} nverts={len(Kt)}")
    for k in [F(1,2), F(1), F(2), F(3)]:
        a = area(minkowski(Kt, scale(D, k)))
        good = (1-2*t*t) + (4-4*t)*k + 2*k*k
        bad = (1-2*t*t) + 4*k + 2*k*k
        check(f"B |K_t+kD| t={t} k={k}", a == good, f"area={a}")
        check(f"B-neg unclipped-perimeter formula differs t={t} k={k}", a != bad, f"bad={bad}")

# ============ C. Normalizers ============
say("\n== C. shell areas and normalizers ==")
prev = area(S)
for k in range(1, 7):
    cur = area(minkowski(S, scale(D, F(k))))
    check(f"C square shell {k} area = 4k+2", cur - prev == 4*k + 2, f"{cur-prev}")
    prev = cur
t = F(1, 8); prev = area(K_clip(t))
for k in range(1, 7):
    cur = area(minkowski(K_clip(t), scale(D, F(k))))
    check(f"C clipped shell {k} area = 4k+2-4t (t=1/8)", cur - prev == 4*k + 2 - 4*t, f"{cur-prev}")
    prev = cur
for b in [F(1,10), F(1,3), F(1,2), F(9,10)]:
    m = b/(1-b)
    # exact rational identities for the geometric sums
    check(f"C sum k b^k = m+m^2 (b={b})", b/(1-b)**2 == m + m*m)
    check(f"C Z_S identity (b={b})", 1 + 4*b/(1-b)**2 + 2*b/(1-b) == ZS(b))
    check(f"C Z_t identity (b={b},t=1/8)", (1-2*t*t) + (2-4*t)*b/(1-b) + 4*b/(1-b)**2 == Zt(b, t), "A + (2-4t)m + 4 sum k b^k")
    check(f"C q0 = 1/Z1^2 (b={b})", q0(b) == 1/Z1(b)**2)
    # partial sum convergence (float) as a sanity net
    ps = 1 + sum(float(b)**k*(4*k+2) for k in range(1, 400))
    check(f"C Z_S partial sum (b={b})", abs(ps - float(ZS(b))) < 1e-12, f"{ps} vs {float(ZS(b))}")

# ============ D. Square-core TV closed form ============
say("\n== D. U_square closed form, C=Z_S/Z1^2, Cb<1, Q(k=1) ==")
for b in [F(1,10), F(1,2), F(1,3), F(1,100), F(99,100)]:
    m = b/(1-b); C = ZS(b)/Z1(b)**2
    check(f"D C>1 and Cb<1 (b={b})", C > 1 and C*b < 1, f"C={C} Cb={float(C*b):.6f}")
    check(f"D C = (1+4b-b^2)/(1+b)^2 (b={b})", C == (1+4*b-b*b)/(1+b)**2)
    Qk1 = 2*m*m/(1+2*m)**2
    check(f"D Q(k=1)=2b^2/(1+b)^2 (b={b})", Qk1 == 2*b*b/(1+b)**2)
    tv1 = Qk1*(1/(C*b) - 1); tv2 = (1-Qk1)*(1 - 1/C)
    check(f"D two TV expressions agree (b={b})", tv1 == tv2, f"{tv1}")
    check(f"D closed form U_square (b={b})", tv1 == U_square(b), f"{U_square(b)}")
check("D U_square(1/10)=2142/16819", U_square(F(1,10)) == F(2142, 16819), str(U_square(F(1,10))))
check("D U_square(1/2)=14/99", U_square(F(1,2)) == F(14, 99), str(U_square(F(1,2))))

# ============ E. brute-force TV ============
def brute_tv(b, core, M, N=None, pdens_scale=None, Z=None):
    """Exact rational integral of (q-p)_+ over the cell block |i|,|j|<=M, where p is the
    shell law with the given convex core (index via Minkowski membership, N shells).
    Returns (tv_block, tail) with true TV in [tv_block, tv_block+tail]."""
    if N is None:
        N = 2*M + 2
    hulls = [minkowski(core, scale(D, F(k))) if k > 0 else hull(core) for k in range(N+1)]
    # block must be covered by shells 0..N: check corners of the block are in hull N
    Mh = M + H
    for cx in (Mh, -Mh):
        for cy in (Mh, -Mh):
            assert inside(hulls[N], (cx, cy)), "block not covered"
    if Z is None:
        Z = sum(b**k*(area(hulls[k]) - (area(hulls[k-1]) if k else 0)) for k in range(N+1))
        # add geometric tail of the normalizer exactly via shell-area pattern? no: use exact closed form supplied by caller
    z1 = Z1(b)
    tv = F(0)
    for i in range(-M, M+1):
        for j in range(-M, M+1):
            cell = rect(i-H, i+H, j-H, j+H)
            q = b**(abs(i)+abs(j))/z1**2
            prev = F(0)
            for k in range(N+1):
                a = area(clip(cell, hulls[k]))
                shell = a - prev; prev = a
                if shell:
                    p = b**k/Z
                    if q > p:
                        tv += shell*(q - p)
    marg = (1 + 2*sum(b**i for i in range(1, M+1)))/z1
    tail = 1 - marg*marg
    return tv, tail

say("\n== E. brute-force TV of square-core law vs U_square ==")
for b, M in [(F(1,10), 6), (F(1,3), 10), (F(1,2), 14)]:
    tv, tail = brute_tv(b, S, M, Z=ZS(b))
    diff = U_square(b) - tv
    check(f"E brute TV(Q,P_S) b={b}: U_square - tv_block in [0,tail]", 0 <= diff <= tail,
          f"tv_block={float(tv):.12f} U={float(U_square(b)):.12f} diff={float(diff):.3e} tail={float(tail):.3e}")
# negative control: wrong normalizer Z1^2 for P_S must NOT reproduce U_square
b = F(1,10)
tv_bad, tail = brute_tv(b, S, 6, Z=Z1(b)**2)
check("E-neg wrong normalizer Z1^2 breaks the match (b=1/10)", not (0 <= U_square(b) - tv_bad <= tail),
      f"tv_bad={float(tv_bad):.9f} U={float(U_square(b)):.9f}")
# negative control: TV(Q,Q)=0 by the same routine? (use core=S with Z=Z1^2 and q=p requires identical shells; skip)

# ============ F. clipped-square law: sign condition, exact part, brute force ============
say("\n== F. clipped-square law P_t: q0*Z_t>=1, E_clip, brute-force TV, comparison ==")
def t_c3(n):   # b = 1/n^4 -> t = (1-b^(1/4)) sqrt(b) = (n-1)/n^3
    return F(n-1, n**3)
for n, M in [(2, 6), (3, 6), (4, 5)]:
    b = F(1, n**4); t = t_c3(n)
    sign = q0(b)*Zt(b, t) - 1
    say(f"  b=1/{n**4}={float(b):.6g}  t={t}={float(t):.6g}  q0*Z_t-1={float(sign):.6g}")
    check(f"F sign q0*Z_t>=1 (b=1/{n**4})", sign >= 0)
    tv, tail = brute_tv(b, K_clip(t), M, Z=Zt(b, t))
    E = E_clip(b, t); U = U_clip(b, t)
    check(f"F tv_block in [E_clip, U_clip] (b=1/{n**4})", E <= tv <= U,
          f"E={float(E):.10f} tv={float(tv):.10f} U={float(U):.10f} tail={float(tail):.2e}")
    check(f"F clipped beats square (b=1/{n**4})", tv + tail < U_square(b),
          f"tv+tail={float(tv+tail):.10f} U_square={float(U_square(b)):.10f}")
    say(f"    2b-4bt={float(2*b-4*b*t):.10f}  (tv-E)/b^3={float((tv-E)/b**3):.4f}  2b-tv={float(2*b-tv):.6e}  4b^1.5={4*float(b)**1.5:.6e}")
# author-reported sign checks recomputed independently
for b, t in [(F(1,10000), F(9,1000)), (F(1,10**8), F(99,10**6))]:
    sign = q0(b)*Zt(b, t) - 1
    check(f"F sign q0*Z_t>1 at b={b} t={t}", sign > 0, f"{float(sign):.6e} ; 4b^(5/4)={4*float(b)**1.25:.6e}")
# where does the sign condition fail with t = sqrt(b) exactly?
for n in [2, 3, 4, 10]:
    b = F(1, n**4); t = F(1, n*n)
    check(f"F-neg t=sqrt(b) violates sign (b=1/{n**4})", q0(b)*Zt(b, t) - 1 < 0, f"{float(q0(b)*Zt(b,t)-1):.3e}")

# ============ G. strip exclusion area 4t^2 ============
say("\n== G. strips \\ (K_t+D) has exact area 4t^2 ==")
for t in [F(1,10), F(1,8), F(1,4), F(2,5)]:
    KD = minkowski(K_clip(t), D)
    strips = [rect(H, 3*H, -H, H), rect(-3*H, -H, -H, H), rect(-H, H, H, 3*H), rect(-H, H, -3*H, -H)]
    excl = sum(area(s) - area(clip(s, KD)) for s in strips)
    check(f"G excluded strip area t={t}", excl == 4*t*t, f"{excl}")
    # and the excluded points have index exactly 2: they lie in K_t+2D
    K2 = minkowski(K_clip(t), scale(D, F(2)))
    check(f"G strips inside K_t+2D t={t}", all(area(clip(s, K2)) == area(s) for s in strips))

# ============ H. overlap triangle C_y ============
say("\n== H. |S ∩ (y-D)| = (1-a-c)^2/2 for corner points y=(1/2+a,1/2+c) ==")
for a, c in [(F(1,10), F(1,5)), (F(1,3), F(1,4)), (F(1,100), F(9,10)), (F(2,5), F(2,5))]:
    y = (H + a, H + c)
    ov = clip(S, translate(D, y))
    check(f"H overlap a={a} c={c}", area(ov) == (1-a-c)**2/2, f"area={area(ov)} verts={len(ov)}")
# candidate 1's square C_sigma: all of it within distance <1 of every y in K_delta
d = F(3, 10)
check("H candidate-1 square: max distance (1-d)+d/2 < 1", (1-d) + d/2 < 1)

# ============ I. the elementary integral and lower-bound asymptotics ============
say("\n== I. integral_0^(1-d) r/(1-r)^2 dr = 1/d + log d - 1 ; L bounds ==")
import mpmath
for d in [0.01, 0.1, 0.3, 0.5, 0.9]:
    num = mpmath.quad(lambda r: r/(1-r)**2, [0, 1-d])
    cf = 1/d + math.log(d) - 1
    check(f"I integral d={d}", abs(float(num) - cf) < 1e-12, f"quad={float(num):.12f} closed={cf:.12f}")
    check(f"I 1/d+log d-1 >= 0 (d={d})", cf >= 0)
# L <= every private law's TV (necessary consistency)
for n in [2, 3, 4]:
    b = F(1, n**4); t = t_c3(n)
    for dd in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]:
        L2 = L_c2(b, dd); L1 = float(L_c1(b, F(dd).limit_denominator(1000)))
        check(f"I L_c2<=U_clip<=U_square? b=1/{n**4} d={dd}", L2 <= float(U_clip(b, t)) and L2 <= float(U_square(b)),
              f"L2={L2:.6f} U_clip={float(U_clip(b,t)):.6f} U_sq={float(U_square(b)):.6f}")
        check(f"I L_c1<=U_square b=1/{n**4} d={dd}", L1 <= float(U_square(b)), f"L1={L1:.6f}")
# optimal delta ~ 2 sqrt(b) and the 16 b^(3/2) constant
say("  (2b-L_c2(b,2sqrt b))/b^1.5 and argmax delta:")
for k in [2, 3, 4, 5, 6]:
    b = F(1, 10**k); bf = float(b)
    L = L_c2(b, 2*math.sqrt(bf))
    best = max(((L_c2(b, dd), dd) for dd in [i/10000 for i in range(1, 9999)]))
    say(f"    b=1e-{k}: (2b-L)/b^1.5={(2*bf-L)/bf**1.5:.4f}  argmax d={best[1]:.4f} vs 2sqrt(b)={2*math.sqrt(bf):.4f}  (2b-Lbest)/b^1.5={(2*bf-best[0])/bf**1.5:.4f}")
    L1 = float(L_c1(b, F(bf**(1/3)).limit_denominator(10**6)))
    say(f"             candidate1 delta=b^(1/3): (2b-L1)/b^(4/3)={(2*bf-L1)/bf**(4/3):.4f}")
say("  (2b-U_square)/b^2 -> 10 ? ; (2b-U_clip)/b^1.5 and (2b-E_clip)/b^1.5 -> 4 ?")
for n in [2, 3, 4, 6, 10, 20, 50]:
    b = F(1, n**4); t = t_c3(n); bf = float(b)
    say(f"    b=1/{n**4}: (2b-U_sq)/b^2={float((2*b-U_square(b))/b**2):.4f}  (2b-U_clip)/b^1.5={float(2*b-U_clip(b,t))/bf**1.5:.4f}  (2b-E_clip)/b^1.5={float(2*b-E_clip(b,t))/bf**1.5:.4f}  4-4b^(1/4)={4-4*bf**0.25:.4f}")

# ============ J. inequality chain controls ============
say("\n== J. lower-bound chain: positive control mu=P_S, negative control mu=Q ==")
b = F(1, 10); dd = F(3, 5)
K_area = 2*(1-dd)**2
T = U_square(b)
corr = 2*float(b)*float(T)*4*(1/float(dd) + math.log(float(dd)) - 1)
rhs = float(b*q0(b)*K_area) - corr
mu_K = float(b/ZS(b)*K_area)          # K_delta lies in shell 1 of P_S (a+c<1)
check("J P_S: mu(K)>= b q0|K| - 2bT*4(1/d+log d-1)", mu_K >= rhs, f"mu(K)={mu_K:.6f} rhs={rhs:.6f}")
# verify K_delta really sits in shell 1 of P_S exactly (clip the four triangles)
tri = [(H, H), (H + (1-dd), H), (H, H + (1-dd))]
h1 = minkowski(S, D); h0 = hull(S)
check("J K_delta triangle inside S+D and disjoint from S", area(clip(tri, h1)) == area(tri) and area(clip(tri, h0)) == 0)
# pointwise identity for P_S: f(y) = b mu(C_y)/|C_y| exactly (C_y inside core)
a, c = F(1,5), F(1,10); y = (H+a, H+c)
check("J P_S pointwise f(y) == b*mu(C_y)/|C_y|", b/ZS(b) == b*(area(clip(S, translate(D, y)))/ZS(b))/area(clip(S, translate(D, y))))
# negative: Q itself (T=0) violates the chain's first inequality
Q_K = float(b*b*q0(b)*K_area)
check("J-neg Q (non-private) violates mu(K) >= b q0 |K| with T=0", not (Q_K >= float(b*q0(b)*K_area)), f"Q(K)={Q_K:.6f} b q0|K|={float(b*q0(b)*K_area):.6f}")
# negative: dropping the TV correction (delta->0) yields 2b(1-b)q0 which EXCEEDS a genuine private law's TV at small b
for n in [3, 4]:
    b = F(1, n**4); t = t_c3(n)
    naive = 2*b*(1-b)*q0(b)
    check(f"J-neg naive bound 2b(1-b)q0 > U_clip (b=1/{n**4}) => correction term essential", naive > U_clip(b, t),
          f"naive={float(naive):.8f} U_clip={float(U_clip(b,t)):.8f}")

# ============ K. privacy spot checks ============
say("\n== K. full-D privacy of shell laws (index jump <=1) ; negative controls ==")
random.seed(136)
def index_of(hulls, x):
    for k, hk in enumerate(hulls):
        if inside(hk, x):
            return k
    return None
NS = 6
hS = [hull(S)] + [minkowski(S, scale(D, F(k))) for k in range(1, NS+1)]
t = F(1, 8)
hT = [K_clip(t)] + [minkowski(K_clip(t), scale(D, F(k))) for k in range(1, NS+1)]
def rnd(lo, hi):
    return F(random.randint(lo*1000, hi*1000), 1000)
viol = 0; tested = 0
for _ in range(3000):
    x = (rnd(-3, 3), rnd(-3, 3))
    v1 = rnd(-1, 1); v2 = rnd(-1, 1)
    if abs(v1) + abs(v2) > 1:
        continue
    xp = (x[0]+v1, x[1]+v2)
    for hh in (hS, hT):
        i0 = index_of(hh, x); i1 = index_of(hh, xp)
        if i0 is None or i1 is None:
            continue
        tested += 1
        if abs(i0 - i1) > 1:
            viol += 1
check("K shell-index jump <=1 on random D-shifts (P_S and P_t)", viol == 0, f"tested={tested} violations={viol}")
# negative control 1: Q's own index n1+n2 jumps by 2 inside the diamond
def q_index(x):
    return sum(math.ceil(max(abs(xi) - F(1,2), 0)) for xi in x)
x = (F(9,20), F(9,20)); xp = (F(11,20), F(11,20))
check("K-neg Q index jumps by 2 for a D-shift of l1 length 1/5", abs(q_index(x) - q_index(xp)) == 2 and abs(xp[0]-x[0])+abs(xp[1]-x[1]) <= 1,
      f"n(x)={q_index(x)} n(x')={q_index(xp)} => q(x')/q(x)=b^2<b")
# negative control 2: half-width shells (core S, steps D/2) violate
hHalf = [hull(S)] + [minkowski(S, scale(D, F(k, 2))) for k in range(1, 2*NS+1)]
x = (F(1,2), F(0)); xp = (F(3,2), F(0))
check("K-neg half-width shells jump by 2 under unit shift", abs(index_of(hHalf, x) - index_of(hHalf, xp)) == 2,
      f"{index_of(hHalf, x)} -> {index_of(hHalf, xp)}")
# convexity identity kD + D = (k+1)D used in the privacy proof (exact hull check)
for k in [1, 2, 3]:
    check(f"K kD+D=(k+1)D (k={k})", area(minkowski(scale(D, F(k)), D)) == area(scale(D, F(k+1))) and hull(minkowski(scale(D, F(k)), D)) == hull(scale(D, F(k+1))))

say("\n== SUMMARY ==")
say("failures:", len(FAILS), FAILS if FAILS else "")
say("end", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "reviewer-controls-c123-v1-output.txt"), "w") as fh:
    fh.write("\n".join(OUT) + "\n")
