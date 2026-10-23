"""Aid: z3 helpers for piecewise-linear window inequalities (all parameters symbolic integers).
g(m, E, kap, beta) = min(p - m, E + m - kap - 1 - beta, floor(E/2)) with h = H - beta, H = p-1-kap."""
from z3 import Int, Solver, If, And, Or, Not, sat, unsat


def zmin(*xs):
    r = xs[0]
    for x in xs[1:]:
        r = If(x < r, x, r)
    return r


def zfloor2(E):
    # floor(E/2) for any integer E (z3 '/' on Int is floor division for positive divisor)
    return E / 2


def g(p, m, E, kap, beta=0):
    return zmin(p - m, E + m - kap - 1 - beta, zfloor2(E))


def prove(hyps, goal, name, show=True):
    s = Solver()
    s.add(*hyps)
    s.add(Not(goal))
    r = s.check()
    if show:
        print(name, 'PROVED' if r == unsat else ('COUNTEREXAMPLE' if r == sat else 'UNKNOWN'))
    if r == sat:
        return s.model()
    return None
