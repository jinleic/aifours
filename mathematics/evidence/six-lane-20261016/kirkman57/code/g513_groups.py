"""Generators for G513 = (Z19 x| Z9) x Z3 acting on Z19 x Z3, point (x,i) -> 19*i + x."""
N = 57

def P(f):
    out = [0] * N
    for i in range(3):
        for x in range(19):
            x2, i2 = f(x, i)
            out[19 * i + x] = 19 * (i2 % 3) + (x2 % 19)
    return tuple(out)

tau = P(lambda x, i: (x + 1, i))          # translation
nu = P(lambda x, i: (4 * x, i + 1))       # order 9, nu^3 = omega
rho = P(lambda x, i: (x, i + 1))          # layer rotation
omega0 = P(lambda x, i: (7 * x, i))       # omega = 7, f = 3
mu = P(lambda x, i: (7 * x, i + 1))       # omega*rho, fixed-point free
mup = P(lambda x, i: (11 * x, i + 1))     # omega^2*rho

G_GENS = [tau, nu, rho]
P27 = [nu, rho]
F57 = [tau, mu]
F57P = [tau, mup]


def gamma(c, e=1):
    """gamma_c^(e): (x,i) -> (x + c*omega^(e*i), i+1); normalizes F57 (e=1) or F57' (e=-1).
    Not in G513 for c != 0.  Used only as an extra automorphism of a base."""
    w = [1, 7, 11] if e == 1 else [1, 11, 7]
    return P(lambda x, i: (x + c * w[i], i + 1))
