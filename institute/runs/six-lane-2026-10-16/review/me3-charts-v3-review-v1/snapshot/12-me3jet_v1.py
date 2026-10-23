"""Forward-mode first-order jets over acb balls, for mean-value-form enclosures.

A jet J(v, d) carries a value enclosure v (acb) and the 3 partial-derivative enclosures d (acb) of a function of
3 real variables over a box. Evaluated with box balls as values and unit vectors as derivatives, every jet operation
encloses the true value and gradient over the box (ball arithmetic + the chain rule). Mean-value form:
  F(B) is contained in F(m) + sum_j dF_j(B) * [-h_j, h_j]
for F continuously differentiable on the box B with midpoint m and half-widths h_j.
"""
from flint import acb, arb


class J:
    __slots__ = ("v", "d")

    def __init__(self, v, d):
        self.v = v
        self.d = d

    def __add__(a, b):
        if isinstance(b, J):
            return J(a.v + b.v, (a.d[0] + b.d[0], a.d[1] + b.d[1], a.d[2] + b.d[2]))
        return J(a.v + b, a.d)

    __radd__ = __add__

    def __neg__(a):
        return J(-a.v, (-a.d[0], -a.d[1], -a.d[2]))

    def __sub__(a, b):
        if isinstance(b, J):
            return J(a.v - b.v, (a.d[0] - b.d[0], a.d[1] - b.d[1], a.d[2] - b.d[2]))
        return J(a.v - b, a.d)

    def __rsub__(a, b):
        return J(b - a.v, (-a.d[0], -a.d[1], -a.d[2]))

    def __mul__(a, b):
        if isinstance(b, J):
            return J(a.v * b.v, (a.v * b.d[0] + b.v * a.d[0], a.v * b.d[1] + b.v * a.d[1], a.v * b.d[2] + b.v * a.d[2]))
        return J(a.v * b, (a.d[0] * b, a.d[1] * b, a.d[2] * b))

    __rmul__ = __mul__

    def __truediv__(a, b):
        if isinstance(b, J):
            q = a.v / b.v
            return J(q, ((a.d[0] - q * b.d[0]) / b.v, (a.d[1] - q * b.d[1]) / b.v, (a.d[2] - q * b.d[2]) / b.v))
        return J(a.v / b, (a.d[0] / b, a.d[1] / b, a.d[2] / b))

    def __rtruediv__(a, b):
        q = b / a.v
        f = -q / a.v
        return J(q, (f * a.d[0], f * a.d[1], f * a.d[2]))


def EXP(x):
    if isinstance(x, J):
        e = x.v.exp()
        return J(e, (e * x.d[0], e * x.d[1], e * x.d[2]))
    return x.exp()


def LOG(x):
    """Principal log; derivative du/u (branch-independent). Caller handles the branch of the value."""
    if isinstance(x, J):
        return J(x.v.log(), (x.d[0] / x.v, x.d[1] / x.v, x.d[2] / x.v))
    return x.log()


def RE(x):
    if isinstance(x, J):
        return J(acb(x.v.real), (acb(x.d[0].real), acb(x.d[1].real), acb(x.d[2].real)))
    return acb(x.real)


def IM(x):
    if isinstance(x, J):
        return J(acb(x.v.imag), (acb(x.d[0].imag), acb(x.d[1].imag), acb(x.d[2].imag)))
    return acb(x.imag)


def jet_inputs(balls):
    z = acb(0)
    o = acb(1)
    units = [(o, z, z), (z, o, z), (z, z, o)]
    return [J(acb(b), units[i]) for i, b in enumerate(balls)]


def mvf(func, mids, balls, hballs):
    """Mean-value-form enclosures of the real outputs of func (a tuple of acb with zero imaginary part).
    mids: arb balls containing the midpoints, balls: arb balls containing the box ranges,
    hballs: arb balls containing [-h_j, h_j] (built as arb(-h).union(arb(h)) from exact half-widths).
    Returns a list of arb enclosures, one per output, valid on the whole box."""
    fm = func(*[acb(m) for m in mids])
    fj = func(*jet_inputs(balls))
    outs = []
    for k in range(len(fm)):
        e = fm[k].real
        for j in range(3):
            e = e + fj[k].d[j].real * hballs[j]
        outs.append(e)
    return outs
