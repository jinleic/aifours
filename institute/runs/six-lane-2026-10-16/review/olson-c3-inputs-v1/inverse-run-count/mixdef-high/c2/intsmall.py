# intsmall.py -- c2/README.md Sec. 15: integer core test with small patterns (|Q| <= s or |Q| >= k - s) for W(p, kB)
# (k = p + 1 + kB single-letter runs, anti run at 0, B = 1).  Usage: python3 intsmall.py p kB s
import sys, itertools, z3
p, kB, s = map(int, sys.argv[1:4]); k = p + 1 + kB; B = 1; kappa = kB + 1
full = (1 << k) - 1
def lam(Q):
    rot = ((Q << 1) | (Q >> (k - 1))) & full
    m = (Q & ~rot).bit_count(); e = Q & 1; j = Q.bit_count() - e; D = j - e
    return min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1)
x = [z3.Int('x%d' % t) for t in range(k)]
cons = []
for size in list(range(1, s + 1)) + list(range(k - s, k)):
    for c in itertools.combinations(range(k), size):
        Q = sum(1 << t for t in c)
        cons.append(Q)
S = z3.Solver(); tags = {}
S.add(z3.Sum(x) == p)
for Q in cons:
    b = z3.Bool('q%d' % Q); tags[b] = Q
    S.add(z3.Implies(b, z3.Sum([x[t] for t in range(k) if (Q >> t) & 1]) >= lam(Q)))
r = S.check(list(tags.keys()))
print({'p': p, 'kB': kB, 'k': k, 's': s, 'constraints': len(cons), 'result': str(r)}, flush=True)
if r == z3.unsat:
    core = [tags[c] for c in S.unsat_core()]
    def unsat(cl):
        T = z3.Solver(); T.add(z3.Sum(x) == p)
        for Q in cl: T.add(z3.Sum([x[t] for t in range(k) if (Q >> t) & 1]) >= lam(Q))
        return T.check() == z3.unsat
    i = 0
    while i < len(core):
        trial = core[:i] + core[i + 1:]
        if unsat(trial): core = trial
        else: i += 1
    print('minimal core', len(core), flush=True)
    for Q in sorted(core, key=lambda Q: (Q.bit_count(), Q)):
        rot = ((Q << 1) | (Q >> (k - 1))) & full
        print('  ', ''.join('1' if (Q >> t) & 1 else '.' for t in range(k)), 'size=%d m=%d lam=%d' % (Q.bit_count(), (Q & ~rot).bit_count(), lam(Q)), flush=True)
else:
    M = S.model(); print('  feasible x =', [M.eval(v) for v in x], flush=True)
