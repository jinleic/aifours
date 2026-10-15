"""One bounded, targeted Billhardt-condition search, not an exhaustive portfolio.

The two size arguments specify the even and odd cardinalities. All four
distinguished odd elements are required to be distinct. No negative result
from this search implies any general embedding theorem.
"""
import datetime
import itertools
import json
from pathlib import Path
import sys
import time

import z3

ROOT = Path(__file__).resolve().parent
NE, NA = (int(x) for x in sys.argv[1:3])
assert NE >= 3 and NA >= 4
N = NE + NA
E = range(NE)
A = range(NE, N)
M = z3.Function('M', z3.IntSort(), z3.IntSort(), z3.IntSort())
solver = z3.Solver()
solver.set(timeout=60000, threads=1)
start = time.monotonic()

for i, j in itertools.product(range(N), repeat=2):
    even = (i < NE) == (j < NE)
    solver.add(M(i, j) >= (0 if even else NE), M(i, j) < (NE if even else N))
for i in E:
    solver.add(M(i, i) == i)
for i, j, k in itertools.product(range(N), repeat=3):
    solver.add(M(M(i, j), k) == M(i, M(j, k)))
for i in A:
    solver.add(z3.Or(*[
        z3.And(M(M(i, j), i) == i, M(M(j, i), j) == j) for j in A]))

# Local regularity of the even band: all three inputs belong to eEe.
for e, a, x, y in itertools.product(E, repeat=4):
    local = z3.And(*[z3.And(M(e, b) == b, M(b, e) == b) for b in (a, x, y)])
    solver.add(z3.Implies(local,
        M(M(M(M(a, x), a), y), a) == M(M(M(a, x), y), a)))

def word(*xs):
    result = xs[0]
    for x in xs[1:]:
        result = M(result, x)
    return result

e, f, g = 0, 1, 2
a, b, ap, bp = NE, NE + 1, NE + 2, NE + 3
solver.add(word(a, ap, a) == a, word(ap, a, ap) == ap)
solver.add(word(b, bp, b) == b, word(bp, b, bp) == bp)
solver.add(word(e, a, ap) == e, word(e, b, bp) == e)
solver.add(word(ap, a, f, g) == word(f, g))
solver.add(word(bp, b, f, ap, e, a, f, g) == word(f, ap, e, a, f, g))
solver.add(word(e, a, f, g) != word(e, b, f, ap, e, a, f, g))

print(json.dumps({'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'even_size': NE, 'odd_size': NA, 'threads': 1, 'solver_timeout_ms': 60000,
    'constraints': len(solver.assertions())}), flush=True)
result = solver.check()
report = {'result': str(result), 'elapsed_seconds': time.monotonic() - start,
          'full_goal_resolved': False,
          'scope': f'One presentation with {NE} even and {NA} odd elements, with four distinguished distinct odd elements.'}
if result == z3.unknown:
    report['reason_unknown'] = solver.reason_unknown()
if result == z3.sat:
    model = solver.model()
    table = [[model.eval(M(i, j)).as_long() for j in range(N)] for i in range(N)]
    report['candidate_table'] = table
    def mul(i, j):
        return table[i][j]
    def value(*xs):
        r = xs[0]
        for x in xs[1:]:
            r = mul(r, x)
        return r
    assert all(value(i, j, k) == mul(i, mul(j, k))
               for i, j, k in itertools.product(range(N), repeat=3))
    assert {i for i in range(N) if mul(i, i) == i} == set(E)
    assert all(mul(i, j) in E for i, j in itertools.product(E, repeat=2))
    assert all(any(value(i, j, i) == i and value(j, i, j) == j for j in range(N))
               for i in range(N))
    assert all(not (mul(e0, x) == x and mul(x, e0) == x and
                    mul(e0, y) == y and mul(y, e0) == y and
                    mul(e0, z) == z and mul(z, e0) == z) or
               value(x, y, x, z, x) == value(x, y, z, x)
               for e0, x, y, z in itertools.product(E, repeat=4))
    assert all(not (e0 == mul(h, s) and e0 == mul(s, k)) or s in E
               for e0, s, h, k in itertools.product(E, range(N), E, E))
    assert value(a, ap, a) == a and value(ap, a, ap) == ap
    assert value(b, bp, b) == b and value(bp, b, bp) == bp
    assert value(e, a, ap) == e and value(e, b, bp) == e
    assert value(ap, a, f, g) == value(f, g)
    assert value(bp, b, f, ap, e, a, f, g) == value(f, ap, e, a, f, g)
    assert value(e, a, f, g) != value(e, b, f, ap, e, a, f, g)
    report['independent_table_checks_pass'] = True
    report['sigma_witness'] = 'ap*b is even and idempotent; every group image equates a and b.'
    (ROOT / 'attempts' / f'obstruction-candidate-{NE}-{NA}.json').write_text(json.dumps(report, indent=2) + '\n')
(ROOT / 'attempts' / f'obstruction-result-{NE}-{NA}.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report), flush=True)
