"""First-order jets over acb balls, version 2: identical to me3jet_v1.py plus SQRT (d sqrt(u) = du / (2 sqrt u),
principal branch; callers use it only on arguments with positive real part)."""
from me3jet_v1 import J, EXP, LOG, RE, IM, jet_inputs, mvf  # noqa: F401


def SQRT(x):
    if isinstance(x, J):
        r = x.v.sqrt()
        f = 1 / (2 * r)
        return J(r, (f * x.d[0], f * x.d[1], f * x.d[2]))
    return x.sqrt()
