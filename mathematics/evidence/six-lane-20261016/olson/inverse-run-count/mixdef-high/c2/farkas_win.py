# farkas.py -- c2/README.md Sec. 12: extract and exactly verify a Farkas certificate for the lifted LP of an
# all-singleton word (anti runs at 0..B-1).  Steps: certified family (singleton extension, = Lemma BC step
# condition with Y a single run); z3 unsat core over tracked bound constraints; deletion-minimisation of the
# core; exact Farkas multipliers (z3 LRA on the dual of the core); independent re-check in fractions.
# Usage: python3 farkas.py p k B [window]  -- window w: only constraints for patterns inside runs 0..w-1
# (certification still uses the whole word).  farkas_win.py = this variant.  'sym' as 5th argument:
# window = runs at cyclic distance <= w from run 0.
import sys, time
from fractions import Fraction
import z3

p, k, B = map(int, sys.argv[1:4]); win = int(sys.argv[4]) if len(sys.argv) > 4 else k; WM = (1 << win) - 1
if len(sys.argv) > 5 and sys.argv[5] == 'sym':   # symmetric window: runs at cyclic distance <= win from run 0
    WM = sum(1 << t for t in range(k) if min(t, k - t) <= win)
R = k; kappa = (R + k - 2 * p) // 2; kB = kappa - B
full = (1 << k) - 1; anti = (1 << B) - 1; alig = full ^ anti; N = 1 << k
def lamf(Q):
    rot = ((Q << 1) | (Q >> (k - 1))) & full
    m = (Q & ~rot).bit_count()
    D = (Q & alig).bit_count() - (Q & anti).bit_count()
    return min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
lam = [0] * N
for Q in range(1, full): lam[Q] = lamf(Q)
cert = bytearray(N); via = [0] * N
for t in range(k): cert[1 << t] = 1
for Q in sorted(range(1, full), key=lambda Q: Q.bit_count()):
    if Q.bit_count() < 2: continue
    a, b = 1 - lam[full ^ Q], p + lam[Q] - 1
    q = Q
    while q:
        t = q & -q; q ^= t; Qp = Q ^ t
        if cert[Qp] and lam[Qp] + lam[t] >= a and (p - lam[full ^ Qp]) + (p - lam[full ^ t]) <= b:
            cert[Q] = 1; via[Q] = t; break
x = [z3.Real('x%d' % t) for t in range(k)]
S = z3.Solver()
tags = {}
for Q in range(1, full):
    if not cert[Q] or (Q & ~WM): continue
    s = z3.Sum([x[t] for t in range(k) if (Q >> t) & 1])
    bl = z3.Bool('L%d' % Q); bu = z3.Bool('U%d' % Q)
    S.add(z3.Implies(bl, s >= lam[Q])); S.add(z3.Implies(bu, s <= p - lam[full ^ Q]))
    tags[bl] = ('L', Q); tags[bu] = ('U', Q)
t0 = time.time()
r = S.check(list(tags.keys()))
print('full LP', r, 'secs', round(time.time() - t0, 1), flush=True)
if r != z3.unsat: sys.exit(0)
core = list(S.unsat_core())
print('core size', len(core), flush=True)
# deletion minimisation on a small solver containing only the core constraints
def small_unsat(cl):
    T = z3.Solver()
    for kind, Q in cl:
        s = z3.Sum([x[t] for t in range(k) if (Q >> t) & 1])
        T.add(s >= lam[Q] if kind == 'L' else s <= p - lam[full ^ Q])
    return T.check() == z3.unsat
cur = [tags[c] for c in core]
i = 0
while i < len(cur):
    trial = cur[:i] + cur[i + 1:]
    if small_unsat(trial): cur = trial
    else: i += 1
print('minimal core size', len(cur), flush=True)
cons = cur
# exact Farkas multipliers: y_c >= 0, sum_c y_c * sign_c * [t in Q_c] = 0 for all t, sum_c y_c * sign_c * bound_c = -1
# constraint forms:  L: -X_Q <= -lam(Q)  ;  U: X_Q <= p - lam(Q^c)
y = [z3.Real('y%d' % i) for i in range(len(cons))]
F = z3.Solver()
for yi in y: F.add(yi >= 0)
for t in range(k):
    F.add(z3.Sum([(-1 if kind == 'L' else 1) * y[i] for i, (kind, Q) in enumerate(cons) if (Q >> t) & 1] + [z3.RealVal(0)]) == 0)
F.add(z3.Sum([y[i] * (-lam[Q] if kind == 'L' else p - lam[full ^ Q]) for i, (kind, Q) in enumerate(cons)]) == -1)
print('dual', F.check(), flush=True)
M = F.model()
ys = []
for i in range(len(cons)):
    v = M.eval(y[i], model_completion=True)
    fr = v.as_fraction() if hasattr(v, 'as_fraction') else Fraction(str(v))
    ys.append(Fraction(fr))
# independent exact re-check
def lam2(Q):   # recomputed independently
    bits = [(Q >> t) & 1 for t in range(k)]
    m = sum(1 for t in range(k) if bits[t] and not bits[t - 1])
    D = sum((1 if t >= B else -1) for t in range(k) if bits[t])
    return min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
def certified_chain(Q):   # rebuild a singleton-extension chain and check every step with lam2
    chain = []
    cur = Q
    while cur.bit_count() > 1:
        t = via[cur]; Qp = cur ^ t
        if not (lam2(Qp) + lam2(t) + lam2(full ^ cur) >= 1 and lam2(cur) + lam2(full ^ Qp) + lam2(full ^ t) >= p + 1):
            return False
        cur = Qp
    return True
ok = all(v >= 0 for v in ys)
for t in range(k):
    ok &= sum(((-1 if kind == 'L' else 1) * ys[i]) for i, (kind, Q) in enumerate(cons) if (Q >> t) & 1) == 0
rhs = sum(ys[i] * (-lam2(Q) if kind == 'L' else p - lam2(full ^ Q)) for i, (kind, Q) in enumerate(cons))
ok &= rhs < 0
ok &= all(certified_chain(Q) for (kind, Q) in cons)
print('exact recheck', ok, 'rhs', rhs, flush=True)
for i, (kind, Q) in enumerate(cons):
    if ys[i] == 0: continue
    bits = ''.join('1' if (Q >> t) & 1 else '.' for t in range(k))
    rot = ((Q << 1) | (Q >> (k - 1))) & full
    print(' %s %s size=%d m=%d bound=%d y=%s' % (kind, bits, Q.bit_count(), (Q & ~rot).bit_count(),
          lam[Q] if kind == 'L' else p - lam[full ^ Q], ys[i]), flush=True)
