#!/usr/bin/env python3
"""reviewer-controls-c4-v1.py  (f136 review, candidate 4: second-order lower bound (2)/(9)
and the t = sqrt(b)-2b clipped-square upper law).

Independent controls written from scratch by the reviewer; no author code imported or run.
Exact fractions.Fraction everywhere except: the positive-root formula (2) (mpmath, 60 digits)
and printed float ratios.  Reuses the reviewer's own polygon toolkit (copied, not imported from
any author file).
"""
from fractions import Fraction as F
import math, sys, time, random, os
import mpmath
mpmath.mp.dps = 60

OUT = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); OUT.append(s)
FAILS = []
def check(tag, cond, detail=""):
    st = "PASS" if cond else "FAIL"
    if not cond: FAILS.append(tag)
    say(f"[{st}] {tag} {detail}")

# ---- exact polygon toolkit (reviewer's own) ----
def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2: return pts
    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
        lo.append(p)
    up = []
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]
def area(poly):
    n = len(poly)
    if n < 3: return F(0)
    return sum(poly[i][0]*poly[(i+1) % n][1] - poly[(i+1) % n][0]*poly[i][1] for i in range(n))/2
def minkowski(P, Q): return hull([(p[0]+q[0], p[1]+q[1]) for p in P for q in Q])
def scale(P, k): return [(k*p[0], k*p[1]) for p in P]
def _isect(p1, p2, a, b):
    d1 = cross(a, b, p1); d2 = cross(a, b, p2); lam = d1/(d1-d2)
    return (p1[0]+lam*(p2[0]-p1[0]), p1[1]+lam*(p2[1]-p1[1]))
def clip(subject, clipper):
    out = list(subject); n = len(clipper)
    for i in range(n):
        a = clipper[i]; b = clipper[(i+1) % n]; inp = out; out = []
        if not inp: break
        s = inp[-1]; s_in = cross(a, b, s) >= 0
        for p in inp:
            p_in = cross(a, b, p) >= 0
            if p_in:
                if not s_in: out.append(_isect(s, p, a, b))
                out.append(p)
            elif s_in: out.append(_isect(s, p, a, b))
            s, s_in = p, p_in
    return out
def inside(poly, x):
    n = len(poly); return all(cross(poly[i], poly[(i+1) % n], x) >= 0 for i in range(n))
H = F(1, 2)
D = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1))]
S = [(H, -H), (H, H), (-H, H), (-H, -H)]
def rect(x0, x1, y0, y1): return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
def K_clip(t):
    return hull([(H, H-t), (H-t, H), (-H+t, H), (-H, H-t), (-H, -H+t), (-H+t, -H), (H-t, -H), (H, -H+t)])

# ---- closed forms ----
def Z1(b): return 1 + 2*b/(1-b)
def q0(b): return ((1-b)/(1+b))**2
def ZS(b): m = b/(1-b); return 1 + 6*m + 4*m*m
def Zt(b, t): m = b/(1-b); return (1-2*t*t) + (6-4*t)*m + 4*m*m
def U_square(b): return 2*b*(1-b)*(1+2*b-b*b)/((1+b)**2*(1+4*b-b*b))
def Q_idx_ge2(b): return 1 - q0(b)*(1+4*b)
def E_clip(b, t):
    A = 1-2*t*t; z = Zt(b, t); qq = q0(b)
    return (qq - (A + b*(1-A))/z) + (4-4*t*t)*b*(qq-1/z) + 4*t*t*(b*qq - b*b/z)
def U_clip(b, t): return E_clip(b, t) + Q_idx_ge2(b)

def lower_c4(b):
    """candidate 4 eq (2): [2B/(A+sqrt(A^2+4(1+b)B))]^2, A=b sqrt(8 q0), B=2b(1-b)q0  (mpmath)."""
    b = mpmath.mpf(b.numerator)/b.denominator if isinstance(b, F) else mpmath.mpf(b)
    qq = ((1-b)/(1+b))**2
    A = b*mpmath.sqrt(8*qq); B = 2*b*(1-b)*qq
    return (2*B/(A + mpmath.sqrt(A*A + 4*(1+b)*B)))**2

def ineq9(b, T):
    """(1+b)T + b sqrt(8 q0 T) - 2b(1-b)q0  (>=0 is the inequality)."""
    b = mpmath.mpf(b.numerator)/b.denominator if isinstance(b, F) else mpmath.mpf(b)
    qq = ((1-b)/(1+b))**2
    return (1+b)*T + b*mpmath.sqrt(8*qq*T) - 2*b*(1-b)*qq

def brute_tv(b, core, M, Z):
    N = 2*M + 2
    hulls = [hull(core)] + [minkowski(core, scale(D, F(k))) for k in range(1, N+1)]
    Mh = M + H
    assert all(inside(hulls[N], (cx, cy)) for cx in (Mh, -Mh) for cy in (Mh, -Mh))
    z1 = Z1(b); tv = F(0)
    for i in range(-M, M+1):
        for j in range(-M, M+1):
            cell = rect(i-H, i+H, j-H, j+H); q = b**(abs(i)+abs(j))/z1**2; prev = F(0)
            for k in range(N+1):
                a = area(clip(cell, hulls[k])); shell = a - prev; prev = a
                if shell:
                    p = b**k/Z
                    if q > p: tv += shell*(q-p)
    marg = (1 + 2*sum(b**i for i in range(1, M+1)))/z1
    return tv, 1 - marg*marg

say("reviewer-controls-c4-v1.py start", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))

# ===== 1. root formula (2) solves (9) with equality; smaller T violates (negative) =====
say("\n== 1. (2) is the exact threshold of (9) ==")
for b in [F(1,10), F(1,2), F(1,16), F(1,10000), F(1,10**6), F(1,10**8)]:
    Lo = lower_c4(b)
    r0 = ineq9(b, Lo)
    check(f"1 (9) holds with equality at T=(2) b={b}", abs(r0) < mpmath.mpf(10)**-50, f"residual={mpmath.nstr(r0,5)}")
    check(f"1-neg (9) fails at T=0.999*(2) b={b}", ineq9(b, Lo*mpmath.mpf('0.999')) < 0)
    check(f"1 (9) holds at T=1.001*(2) b={b}", ineq9(b, Lo*mpmath.mpf('1.001')) > 0)
    bf = float(b); lo = float(Lo)
    say(f"    b={b}: lower={mpmath.nstr(Lo,15)}  [lower-2b+4b^1.5]/b^2={(lo-2*bf+4*bf**1.5)/bf**2:.6f}")

# ===== 2. consistency: (2) <= TV of every genuine private law computed earlier =====
say("\n== 2. (2) <= brute-force TV(Q,P) for actual private laws (necessary) ==")
for b, M in [(F(1,10), 6), (F(1,3), 10), (F(1,2), 14)]:
    tv, tail = brute_tv(b, S, M, ZS(b))
    check(f"2 (2) <= TV(Q,P_S) b={b}", lower_c4(b) <= mpmath.mpf(tv.numerator)/tv.denominator,
          f"lower={mpmath.nstr(lower_c4(b),8)} tv={float(tv):.8f}")
def t_c4(b):  # b=1/n^2 -> sqrt(b)=1/n
    n = int(round(math.sqrt(b.denominator))); assert n*n == b.denominator and b.numerator == 1
    return F(1, n) - 2*b
for b, M in [(F(1,16), 6), (F(1,100), 6), (F(1,400), 5)]:
    t = t_c4(b)
    sign = q0(b)*Zt(b, t) - 1
    check(f"2 sign q0*Z_t>=1 at t=sqrt(b)-2b b={b} t={t}", sign >= 0, f"{float(sign):.4e}  (q0Zt-1)/b^1.5={float(sign)/float(b)**1.5:.4f}")
    tv, tail = brute_tv(b, K_clip(t), M, Zt(b, t))
    E = E_clip(b, t); U = U_clip(b, t); Lo = lower_c4(b)
    check(f"2 tv in [E_clip,U_clip] b={b}", E <= tv <= U, f"E={float(E):.10f} tv={float(tv):.10f} U={float(U):.10f} tail={float(tail):.1e}")
    check(f"2 (2) <= TV(Q,P_t) b={b}", Lo <= mpmath.mpf(tv.numerator)/tv.denominator, f"lower={mpmath.nstr(Lo,10)}")
    bf = float(b)
    say(f"    b={b}: (tv-2b+4b^1.5)/b^2={(float(tv)-2*bf+4*bf**1.5)/bf**2:.4f}   (2b-4b^1.5-lower)/b^2={(2*bf-4*bf**1.5-float(Lo))/bf**2:.4f}   gap (tv-lower)/b^2={(float(tv)-float(Lo))/bf**2:.4f}")
say("  second-order coefficient diagnostics (exact E_clip, t=sqrt b-2b):")
for n in [10, 100, 1000, 10000]:
    b = F(1, n*n); t = F(1, n) - 2*b; bf = float(b)
    E = E_clip(b, t); U = U_clip(b, t); Lo = lower_c4(b)
    say(f"    b=1e-{2*len(str(n))-2}: (E_clip-2b+4b^1.5)/b^2={(float(E)-2*bf+4*bf**1.5)/bf**2:.4f}  (U_clip-2b+4b^1.5)/b^2={(float(U)-2*bf+4*bf**1.5)/bf**2:.4f}  (lower-2b+4b^1.5)/b^2={(float(Lo)-2*bf+4*bf**1.5)/bf**2:.4f}  (q0Zt-1)/b^1.5={float(q0(b)*Zt(b,t)-1)/bf**1.5:.4f}")

# ===== 3. bathtub inequality (7) on exact step functions; negative control =====
say("\n== 3. bathtub: int_0^(1/2) d h(d) dd >= H^2/(2 q0) for 0<=h<=q0 ; negative control ==")
random.seed(4)
qq = F(2, 3)
def step_moments(steps):   # steps: list of (d0,d1,c)
    H_ = sum((d1-d0)*c for d0, d1, c in steps)
    M_ = sum((d1*d1-d0*d0)/2*c for d0, d1, c in steps)
    return H_, M_
viol = 0
for trial in range(400):
    cuts = sorted({F(random.randint(0, 500), 1000) for _ in range(random.randint(1, 8))} | {F(0), F(1,2)})
    steps = [(cuts[i], cuts[i+1], F(random.randint(0, 1000), 1000)*qq) for i in range(len(cuts)-1)]
    H_, M_ = step_moments(steps)
    if not (M_ >= H_*H_/(2*qq)): viol += 1
check("3 bathtub holds on 400 random step functions (not nec. monotone)", viol == 0, f"violations={viol}")
# equality for the bathtub shape
for Hv in [F(1,10), F(1,4), F(3,10)]:
    steps = [(F(0), Hv/qq, qq), (Hv/qq, F(1,2), F(0))]
    H_, M_ = step_moments(steps)
    check(f"3 equality for h=q0 on [0,H/q0], H={Hv}", H_ == Hv and M_ == Hv*Hv/(2*qq))
# negative control: a function exceeding the cap q0 can beat the bound
steps = [(F(0), F(1,20), 3*qq), (F(1,20), F(1,2), F(0))]
H_, M_ = step_moments(steps)
check("3-neg h=3q0 on [0,1/20] violates (7) (cap needed)", M_ < H_*H_/(2*qq), f"M={M_} H^2/2q0={H_*H_/(2*qq)}")

# ===== 4. geometry of (6) and (9): exact area elements =====
say("\n== 4. area elements: inward depth-s triangle has |{depth<=s}|=s^2/2 ; outside corner {1-a-c in (d0,d1]} area = int (1-d)dd ==")
for s in [F(1,10), F(1,4), F(1,2)]:
    tri = [(H, H), (H-s, H), (H, H-s)]   # inward corner triangle of depth s
    check(f"4 |C(s)|=s^2/2 s={s}", area(hull(tri)) == s*s/2)
for d0, d1 in [(F(0), F(1,4)), (F(1,4), F(1,2)), (F(1,2), F(1)), (F(3,10), F(9,10))]:
    # outside region: a,c>0, 1-a-c in (d0,d1]  <=> a+c in [1-d1, 1-d0)
    big = hull([(H, H), (H+(1-d0), H), (H, H+(1-d0))]) if d0 < 1 else []
    small = hull([(H, H), (H+(1-d1), H), (H, H+(1-d1))])
    reg = area(big) - area(small)
    check(f"4 outside band area d in ({d0},{d1}]", reg == ((1-d0)**2 - (1-d1)**2)/2, f"{reg}")
# the four depth-1/2 inward triangles are disjoint (pairwise intersection area 0) and lie in S
tris = [hull([(sx*H, sy*H), (sx*H - sx*H, sy*H), (sx*H, sy*H - sy*H)]) for sx in (1, -1) for sy in (1, -1)]
ok = all(area(clip(tris[i], tris[j])) == 0 for i in range(4) for j in range(4) if i < j) and all(area(clip(t_, S)) == area(t_) for t_ in tris)
check("4 four depth-1/2 corner triangles pairwise disjoint and inside S", ok, f"areas={[area(t_) for t_ in tris]}")

# ===== 5. whole chain on an explicit private law (positive) and on Q (negative) =====
say("\n== 5. chain (6)-(9) for mu=P_S (positive), mu=Q (negative) ==")
for b in [F(1,10), F(1,3)]:
    T = U_square(b); h = q0(b) - 1/ZS(b)      # e is constant on S for P_S
    check(f"5 P_S: e=q0-1/Z_S>0 b={b}", h > 0, f"h={float(h):.6f}")
    M4 = 4*(h/8)                              # sum_sigma int_0^(1/2) d h dd
    check(f"5 P_S: (6) sum M_sigma<=T b={b}", M4 <= T, f"{float(M4):.6f} <= {float(T):.6f}")
    W = 4*(h/2)                               # sum_sigma int_0^1 (1-d) h dd
    bound8 = math.sqrt(8*float(q0(b)*T)) + float(T)
    check(f"5 P_S: (8) W<=sqrt(8q0T)+T b={b}", float(W) <= bound8, f"W={float(W):.6f} bound={bound8:.6f}")
    muK = b/ZS(b)*2; rhs = 2*b*q0(b) - b*W
    check(f"5 P_S: mu(K)>=2bq0-bW (integrated (5), equality expected) b={b}", muK >= rhs and muK == rhs, f"{float(muK):.6f} vs {float(rhs):.6f}")
    check(f"5 P_S: (9) holds b={b}", ineq9(b, mpmath.mpf(T.numerator)/T.denominator) >= 0)
check("5-neg Q (T=0) violates (9): 0 >= 2b(1-b)q0 false", ineq9(F(1,10), mpmath.mpf(0)) < 0)
# negative control for (5)-geometry: using a corner triangle of the WRONG depth (d+0.1) would claim a larger overlap;
# verify exact overlap equals depth exactly d, not d+1/10
a, c = F(1,5), F(3,10); y = (H+a, H+c); d = 1-a-c
ov = clip(S, [(y[0]+p[0], y[1]+p[1]) for p in D])
check("5 overlap depth equals 1-a-c exactly (not larger)", area(ov) == d*d/2 and area(ov) != (d+F(1,10))**2/2)

# ===== 6. comparison of the three lower bounds =====
say("\n== 6. lower bounds compared: candidate 2 best-delta vs candidate 4 (2) ==")
def L_c2(b, dd): return float(2*b*(1-b)*q0(b)*(1-dd)**2)/(1 + 8*float(b)*(1/dd + math.log(dd) - 1))
for k in [1, 2, 3, 4, 6]:
    b = F(1, 10**k); bf = float(b)
    best = max(L_c2(b, i/10000) for i in range(1, 9999))
    say(f"    b=1e-{k}: L_c2best={best:.10g}  L_c4={mpmath.nstr(lower_c4(b),10)}  2b={2*bf:.10g}  ratio (2b-L_c2)/(2b-L_c4)={(2*bf-best)/(2*bf-float(lower_c4(b))):.3f}")
    check(f"6 L_c4 >= L_c2best b=1e-{k}", float(lower_c4(b)) >= best)

say("\n== SUMMARY ==")
say("failures:", len(FAILS), FAILS if FAILS else "")
say("end", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "reviewer-controls-c4-v1-output.txt"), "w") as fh:
    fh.write("\n".join(OUT) + "\n")
