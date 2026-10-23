"""v2 (only change: theta1 by bisection; v1 crashed in findroot). EXPLORATORY generator of MUTATED sample files for the replay controls (the replays must flag every line).

primal_mutations.txt (chart-P format "OUTCOME rl rh wl wh pl ph"):
  M1 'SGE' box around the D1 minimizer (r ~ 0, omega ~ 1.0359, phi ~ 0.3370), where S ~ 0.2009 < 11/50;
  M2 'INFEAS' box with phi in [1, 2] < pi < theta1(r) (feasible);
  M3 'DPOS' box around a grid point found here with dS/dr < 0 (central differences, mpmath 30 digits).
dualG_mutations.txt (chart-G format "OUTCOME sl sh dl dh wl wh"):
  N1 'CERT:mutation' box around (s*, delta = 0, omega = 1.0359): at delta = 0 the hull is the closed unit disk and s*
     maximizes |W| on a grid (|W| > 1 is required and checked here), so W is outside the hull there;
  N2 'SKIP:mutation' box violating the G skip rule (omega_hi = 50 > 40);
  N3 'FAIL' box (a non-CERT, non-SKIP outcome).
The small evaluators below are throwaway search aids (not the replay code).
"""
import os
import sys
import json
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
mp.mp.dps = 30
log = {}


def S(r, w, p):
    c = mp.mpc(1, -r) * mp.exp(mp.mpc(r, -1) * p)
    z = 1 / mp.mpc(1 + r * w, -w)
    a = [1 - mp.re(c * z ** (k + 1)) for k in range(3)]
    return 2 * a[0] * a[2] / a[1] ** 2 - 1


def th1(r):  # v2: plain bisection (v1's bracketed anderson solve failed to converge)
    lo, hi = mp.pi, 2 * mp.pi
    for _ in range(110):
        mid = (lo + hi) / 2
        if mp.exp(r * mid) * (mp.cos(mid) - r * mp.sin(mid)) - 1 > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


lines_p = []
# M1
lines_p.append("SGE 0 1/100000 10359/10000 10360/10000 3370/10000 3371/10000")
log["M1_S_at_mid"] = mp.nstr(S(mp.mpf(1) / 200000, mp.mpf("1.03595"), mp.mpf("0.33705")), 15)
# M2
lines_p.append("INFEAS 1/10 1/5 1 2 1 2")
# M3: search dS/dr < 0
best = None
for r in [mp.mpf(x) / 4 for x in range(1, 12)]:
    t1 = th1(r)
    for w in [mp.mpf(x) for x in ("0.3", "0.6", "1", "2", "4", "8", "16", "32")]:
        for j in range(1, 40):
            p = t1 * j / 40
            d = mp.diff(lambda rr: S(rr, w, p), r)
            if best is None or d < best[0]:
                best = (d, r, w, p)
d, r, w, p = best
log["M3_search_min_dSdr"] = {"dSdr": mp.nstr(d, 15), "r": mp.nstr(r, 10), "w": mp.nstr(w, 10), "phi": mp.nstr(p, 15)}
if d < 0:
    rq, wq = Fr(mp.nstr(r, 12)), Fr(mp.nstr(w, 12))
    pq = Fr(int(mp.floor(p * 10 ** 6)), 10 ** 6)
    e = Fr(1, 10 ** 7)
    lines_p.append("DPOS %s %s %s %s %s %s" % (rq - e, rq + e, wq - e, wq + e, pq - e, pq + e))
    log["M3_made"] = True
else:
    log["M3_made"] = False

# N1: delta = 0, omega = 1.0359: maximize |W| over s
KAP = mp.mpf(50) / 61


def Wd(s, de, om):
    mu = s / (1 - s)
    Q = lambda y: (KAP * y * y - 2 * y + 2) / y ** 3  # noqa: E731
    return Q(mu * mp.mpc(1 + de, -om)) / Q(mu)


bestN = max(((abs(Wd(mp.mpf(j) / 2000, 0, mp.mpf("1.0359"))), j) for j in range(1, 2000)), key=lambda x: x[0])
log["N1_max_|W|_delta0"] = {"absW": mp.nstr(bestN[0], 15), "s": "%d/2000" % bestN[1]}
lines_d = []
if bestN[0] > 1:
    sq = Fr(bestN[1], 2000)
    lines_d.append("CERT:mutation %s %s 0 %s 10359/10000 10360/10000" % (sq - Fr(1, 10 ** 6), sq + Fr(1, 10 ** 6),
                                                                       Fr(1, 10 ** 8)))
    log["N1_made"] = True
else:
    log["N1_made"] = False
lines_d.append("SKIP:mutation 0 1 0 1 30 50")
lines_d.append("FAIL 0 1/2 1 2 300 400")
with lane_guard.xopen(os.path.join(RUN, "primal_mutations.txt")) as fh:
    fh.write("\n".join(lines_p) + "\n")
with lane_guard.xopen(os.path.join(RUN, "dualG_mutations.txt")) as fh:
    fh.write("\n".join(lines_d) + "\n")
with lane_guard.xopen(os.path.join(RUN, "mutations_log.json")) as fh:
    json.dump(log, fh, indent=1)
print(json.dumps(log))
