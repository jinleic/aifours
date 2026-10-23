# cutgen.py -- c2/README.md Sec. 12/13: lifted-interval LP by constraint generation, for all-singleton words
# (anti runs at 0..B-1).  Certified family = singleton extension (Lemma BC step condition with Y one run).
# Loop: exact LP (z3, rationals) on the current constraint set; if infeasible -> minimal core, exact Farkas
# multipliers, independent re-check in fractions; if feasible -> separation over ALL certified patterns with
# the model (float pass, exact re-check of the selected cuts); no violated pattern -> the full lifted LP is
# feasible (this certificate family does not kill the word).  Usage: python3 cutgen.py p k B [cuts_per_round]
import sys, time
from fractions import Fraction
import z3

p, k, B = map(int, sys.argv[1:4]); CPR = int(sys.argv[4]) if len(sys.argv) > 4 else 300
R = k; kappa = (R + k - 2 * p) // 2; kB = kappa - B
full = (1 << k) - 1; anti = (1 << B) - 1; alig = full ^ anti; N = 1 << k
t0 = time.time()
lam = [0] * N
for Q in range(1, full):
    rot = ((Q << 1) | (Q >> (k - 1))) & full
    m = (Q & ~rot).bit_count()
    D = (Q & alig).bit_count() - (Q & anti).bit_count()
    lam[Q] = min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
cert = bytearray(N); via = [0] * N
for t in range(k): cert[1 << t] = 1
# popcount order without sorting 4M items: iterate masks by size via Gosper's hack
for c in range(2, k):
    Q = (1 << c) - 1
    while Q < full:
        a, b = 1 - lam[full ^ Q], p + lam[Q] - 1
        q = Q
        while q:
            t = q & -q; q ^= t; Qp = Q ^ t
            if cert[Qp] and lam[Qp] + lam[t] >= a and (p - lam[full ^ Qp]) + (p - lam[full ^ t]) <= b:
                cert[Q] = 1; via[Q] = t; break
        u = Q & -Q; v = Q + u; Q = (((v ^ Q) >> 2) // u) | v
ncert = sum(cert)
print({'p': p, 'k': k, 'B': B, 'kappa': kappa, 'kB': kB, 'certified': ncert, 'of': N - 2, 'secs': round(time.time() - t0, 1)}, flush=True)
x = [z3.Real('x%d' % t) for t in range(k)]
def term(Q): return z3.Sum([x[t] for t in range(k) if (Q >> t) & 1])
C = [('L', 1 << t) for t in range(k)] + [('U', 1 << t) for t in range(k)]
inC = set(C)
def build(cl):
    S = z3.Solver()
    for kind, Q in cl:
        S.add(term(Q) >= lam[Q] if kind == 'L' else term(Q) <= p - lam[full ^ Q])
    return S
rnd = 0
while True:
    rnd += 1
    S = build(C); r = S.check()
    if r == z3.unsat:
        print('round', rnd, 'LP infeasible with', len(C), 'constraints', flush=True)
        break
    M = S.model()
    xs = [M.eval(xx, model_completion=True) for xx in x]
    xf = [float(v.as_fraction()) for v in xs]
    X = [0.0] * N
    for Q in range(1, N):
        lb = Q & -Q
        X[Q] = X[Q ^ lb] + xf[lb.bit_length() - 1]
    viol = []
    for Q in range(1, full):
        if not cert[Q]: continue
        lo = lam[Q] - X[Q]
        if lo > 1e-9: viol.append((lo, 'L', Q))
        up = X[Q] - (p - lam[full ^ Q])
        if up > 1e-9: viol.append((up, 'U', Q))
    print('round', rnd, 'constraints', len(C), 'violated', len(viol), 'secs', round(time.time() - t0, 1), flush=True)
    if not viol:
        print('FULL lifted LP FEASIBLE; model x =', [str(v) for v in xs], flush=True)
        sys.exit(0)
    viol.sort(reverse=True)
    added = 0
    for _, kind, Q in viol:
        if (kind, Q) in inC: continue
        C.append((kind, Q)); inC.add((kind, Q)); added += 1
        if added >= CPR: break
# minimal core (deletion) and exact Farkas multipliers
cur = C[:]
S = z3.Solver(); tags = {}
for i, (kind, Q) in enumerate(cur):
    bb = z3.Bool('c%d' % i); tags[bb] = (kind, Q)
    S.add(z3.Implies(bb, term(Q) >= lam[Q] if kind == 'L' else term(Q) <= p - lam[full ^ Q]))
S.check(list(tags.keys())); cur = [tags[c] for c in S.unsat_core()]
i = 0
while i < len(cur):
    trial = cur[:i] + cur[i + 1:]
    if build(trial).check() == z3.unsat: cur = trial
    else: i += 1
print('minimal core size', len(cur), flush=True)
y = [z3.Real('y%d' % i) for i in range(len(cur))]
F = z3.Solver()
for yi in y: F.add(yi >= 0)
for t in range(k):
    F.add(z3.Sum([(-1 if kind == 'L' else 1) * y[i] for i, (kind, Q) in enumerate(cur) if (Q >> t) & 1] + [z3.RealVal(0)]) == 0)
F.add(z3.Sum([y[i] * (-lam[Q] if kind == 'L' else p - lam[full ^ Q]) for i, (kind, Q) in enumerate(cur)]) == -1)
print('dual', F.check(), flush=True)
Mf = F.model()
ys = [Fraction(Mf.eval(y[i], model_completion=True).as_fraction()) for i in range(len(cur))]
def lam2(Q):
    bits = [(Q >> t) & 1 for t in range(k)]
    m = sum(1 for t in range(k) if bits[t] and not bits[t - 1])
    D = sum((1 if t >= B else -1) for t in range(k) if bits[t])
    return min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
def chain_ok(Q):
    cur_ = Q
    while cur_.bit_count() > 1:
        t = via[cur_]; Qp = cur_ ^ t
        if t == 0 or not (Qp & t) == 0 or not (lam2(Qp) + lam2(t) + lam2(full ^ cur_) >= 1 and lam2(cur_) + lam2(full ^ Qp) + lam2(full ^ t) >= p + 1):
            return False
        cur_ = Qp
    return True
ok = all(v >= 0 for v in ys)
for t in range(k):
    ok &= sum(((-1 if kind == 'L' else 1) * ys[i]) for i, (kind, Q) in enumerate(cur) if (Q >> t) & 1) == 0
rhs = sum(ys[i] * (-lam2(Q) if kind == 'L' else p - lam2(full ^ Q)) for i, (kind, Q) in enumerate(cur))
ok &= rhs < 0
ok &= all(chain_ok(Q) for (kind, Q) in cur)
print('exact recheck', ok, 'rhs', rhs, flush=True)
for i, (kind, Q) in enumerate(cur):
    if ys[i] == 0: continue
    bits = ''.join('1' if (Q >> t) & 1 else '.' for t in range(k))
    rot = ((Q << 1) | (Q >> (k - 1))) & full
    print(' %s %s size=%d m=%d bound=%d y=%s' % (kind, bits, Q.bit_count(), (Q & ~rot).bit_count(),
          lam[Q] if kind == 'L' else p - lam[full ^ Q], ys[i]), flush=True)
print('total secs', round(time.time() - t0, 1), flush=True)
