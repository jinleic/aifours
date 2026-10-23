# lpcert.py -- c2/README.md Sec. 12: lifted-interval LP on all-singleton words (anti runs at 0..B-1).
# Certified family via singleton extension; LP over reals solved exactly by z3; per total-multiple case z.
# Usage: python3 lpcert.py p k B [maxsize]
import sys, time
import z3

p, k, B = map(int, sys.argv[1:4]); maxsize = int(sys.argv[4]) if len(sys.argv) > 4 else k - 1
d = [-1] * B + [1] * (k - B)
R = k; kappa = (R + k - 2 * p) // 2; kB = kappa - B
full = (1 << k) - 1
anti = (1 << B) - 1; alig = full ^ anti
N = 1 << k
t0 = time.time()
lam = [0] * N
for Q in range(1, full):
    rot = ((Q << 1) | (Q >> (k - 1))) & full
    m = (Q & ~rot).bit_count()
    D = (Q & alig).bit_count() - (Q & anti).bit_count()
    lam[Q] = min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
def lo(Q): return lam[Q]
def hi(Q): return p - lam[full ^ Q]
cert = bytearray(N)
for t in range(k): cert[1 << t] = 1
order = sorted(range(1, full), key=lambda Q: Q.bit_count())
ncert = k
for Q in order:
    c = Q.bit_count()
    if c < 2 or c > maxsize: continue
    a, b = 1 - lam[full ^ Q], p + lam[Q] - 1
    q = Q
    while q:
        t = q & -q; q ^= t
        Qp = Q ^ t
        if cert[Qp] and lo(Qp) + lo(t) >= a and hi(Qp) + hi(t) <= b:
            cert[Q] = 1; ncert += 1; break
print({'p': p, 'k': k, 'B': B, 'kappa': kappa, 'kB': kB, 'certified': ncert, 'maxsize': maxsize, 'secs': round(time.time() - t0, 1)}, flush=True)
bysize = {}
for Q in range(1, full):
    if cert[Q]: bysize[Q.bit_count()] = bysize.get(Q.bit_count(), 0) + 1
print('certified by size', sorted(bysize.items()), flush=True)
x = [z3.Real('x%d' % t) for t in range(k)]
cons = []
for Q in range(1, full):
    if not cert[Q]: continue
    s = z3.Sum([x[t] for t in range(k) if (Q >> t) & 1])
    cons.append((Q, s))
def solver_with(extra):
    S = z3.Solver()
    for Q, s in cons:
        S.add(s >= lo(Q), s <= hi(Q))
    for e in extra: S.add(e)
    return S
tot = z3.Sum(x)
opt = z3.Optimize()
for Q, s in cons: opt.add(s >= lo(Q), s <= hi(Q))
h1 = opt.minimize(tot); r = opt.check()
print('LP status', r, flush=True)
if r == z3.sat:
    mn = opt.lower(h1)
    opt2 = z3.Optimize()
    for Q, s in cons: opt2.add(s >= lo(Q), s <= hi(Q))
    h2 = opt2.maximize(tot); opt2.check(); mx = opt2.upper(h2)
    print('X_total range', mn, mx, flush=True)
    mnv = z3.simplify(mn); mxv = z3.simplify(mx)
    import math
    lo_t = math.ceil(float(mnv.as_fraction()) / p - 1e-12) if hasattr(mnv, 'as_fraction') else None
    hi_t = math.floor(float(mxv.as_fraction()) / p + 1e-12) if hasattr(mxv, 'as_fraction') else None
    print('z candidates', lo_t, hi_t, flush=True)
    for z in range(lo_t, hi_t + 1):
        S = solver_with([tot == p * z])
        res = S.check()
        print('z =', z, res, flush=True)
        if res == z3.sat:
            M = S.model()
            print('  witness x =', [M.eval(xx) for xx in x], flush=True)
print('done secs', round(time.time() - t0, 1), flush=True)
