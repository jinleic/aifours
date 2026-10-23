"""Checker A (python-flint arb) for the outer cell certificate.

Mathematical content of one dual leaf (cell = 4-simplex K in n-space, multipliers y in Q^18,
inner points mu0^u in Q_{>0}^4):
  for every n in K and every feasible d in the fibre of n,
     ln Fhat(d) <= U_y(n) := sum_u [ n^u a_u + (3/2) n^u ln n^u ],
  where a_u >= Psi*(z^u), z^u = C_u y, is
     a_u = psi(m0) + <z, m0> + max_{s in S} <(1/2) ln m0 - ln mu0 + z, s - m0>,
     m0 = sum_s s w_s mu0^s / Phi(mu0),  psi(m0) = (1/2) sum m0 ln m0 + ln Phi(mu0) - <ln mu0, m0>.
  (Pairing terms sum to zero; per-class max-entropy; scaling psi(c m) = c psi(m) + (3/2) c ln c;
   supergradient inequality of the slice-concave psi on conv(S) = M0(1).)
  U_y is convex in n, so max over K is attained at a vertex; the leaf is accepted iff
  U_y(v) < L* = (5/2) ln 5 + ln(25/24) rigorously at all 5 vertices v.
Central leaf: all 5 vertices satisfy |n_k - 1/9| <= r0 (k = 00, 01, 10, 11); discharged by the
separate local-dual-concavity certificate on that box.
The tree replays exact rational bisections from the root simplex conv(n*, facet {n^{fi,fj} = 0}).
Usage: cert_cells.py CERT.json
"""
import sys, json, itertools, time
from fractions import Fraction
import flint
from flint import arb, fmpq

flint.ctx.prec = 200
sys.setrecursionlimit(100000)


def spectra():
    out = []
    for a, b, c in itertools.product(range(6), repeat=3):
        d = 5 - a - b - c
        if d < 0:
            continue
        if min(a + b, c + d) >= 1 and min(a + c, b + d) >= 1:
            out.append((a, b, c, d))
    return out


S = spectra()
assert len(S) == 36
FACT = [1, 1, 2, 6, 24, 120]
W = [120 // (FACT[a] * FACT[b] * FACT[c] * FACT[d]) for (a, b, c, d) in S]
OFF = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
VERT = [(i, j) for i in range(3) for j in range(3)]
# incidence C_u (class u, entry k) -> edge e with sign
EDGES, seen = [], set()
for u, (i, j) in enumerate(VERT):
    for k, (r, t) in enumerate(OFF):
        v = 3 * ((i + r) % 3) + (j + t) % 3
        kv = OFF.index((-r, -t))
        if (u, k) in seen:
            continue
        seen.add((u, k)); seen.add((v, kv))
        EDGES.append((u, k, v, kv))
assert len(EDGES) == 18
LSTAR = arb(5).log() * arb(fmpq(5, 2)) + (arb(25) / arb(24)).log()


def q(x):
    """exact rational from a hex-float string, an int, or a 'p/q' string"""
    if isinstance(x, str) and ('p' in x or 'x' in x):
        f = Fraction(float.fromhex(x))
    else:
        f = Fraction(x)
    return fmpq(f.numerator, f.denominator)


def nine(p):
    n1, n2, n3, n4 = p
    t = fmpq(1, 3)
    return [n1, n2, t - n1 - n2, n3, n4, t - n3 - n4, t - n1 - n3, t - n2 - n4, n1 + n2 + n3 + n4 - t]


def a_bound(z, mu):
    lmu = [arb(x).log() for x in mu]
    d = []
    for s, w in zip(S, W):
        t = arb(w)
        for k in range(4):
            if s[k]:
                t *= arb(mu[k]) ** s[k]
        d.append(t)
    Z = sum(d, arb(0))
    m0 = [sum((d[i] * S[i][k] for i in range(36)), arb(0)) / Z for k in range(4)]
    lm0 = [x.log() for x in m0]
    psi0 = sum((m0[k] * lm0[k] for k in range(4)), arb(0)) / 2 + Z.log() - sum((lmu[k] * m0[k] for k in range(4)), arb(0))
    g = [lm0[k] / 2 - lmu[k] + arb(z[k]) for k in range(4)]
    T = None
    for s in S:
        v = sum((g[k] * (arb(s[k]) - m0[k]) for k in range(4)), arb(0))
        T = v if T is None else T.max(v)
    return psi0 + sum((arb(z[k]) * m0[k] for k in range(4)), arb(0)) + T


def check_dual_leaf(cell, y, mus):
    a = []
    for u in range(9):
        z = [fmpq(0)] * 4
        for e, (uu, k, vv, kv) in enumerate(EDGES):
            if uu == u:
                z[k] += y[e]
            if vv == u:
                z[kv] -= y[e]
        a.append(a_bound(z, mus[u]))
    worst = None
    for p in cell:
        nn = nine(p)
        U = arb(0)
        for u in range(9):
            if nn[u] < 0:
                raise ValueError('vertex outside Delta')
            if nn[u] == 0:
                continue
            x = arb(nn[u])
            U += x * a[u] + arb(fmpq(3, 2)) * x * x.log()
        margin = LSTAR - U
        if not (margin > 0):
            return False, margin
        worst = margin if worst is None else worst.min(margin)
    return True, worst


def main(path):
    cert = json.load(open(path))
    fi, fj = cert['facet']
    r0 = q(cert['r0'])
    nstar = [fmpq(1, 9)] * 4
    perms = [s for s in itertools.permutations(range(3)) if s[fi] != fj]
    assert len(perms) == 4
    root = [nstar] + [[fmpq(int(s[0] == 0), 3), fmpq(int(s[0] == 1), 3), fmpq(int(s[1] == 0), 3), fmpq(int(s[1] == 1), 3)] for s in perms]
    nodes = cert['tree']
    pos = 0
    stats = {'dual_leaves': 0, 'central_leaves': 0, 'splits': 0, 'failed': 0}
    worst = [None]

    def rec(cell):
        nonlocal pos
        node = nodes[pos]; pos += 1
        if node[0] == 'S':
            i, j = node[1], node[2]
            mid = [(cell[i][k] + cell[j][k]) / 2 for k in range(4)]
            c1 = list(cell); c1[i] = mid
            c2 = list(cell); c2[j] = mid
            stats['splits'] += 1
            rec(c1); rec(c2)
        elif node[0] == 'C':
            ok = all(abs(p[k] - fmpq(1, 9)) <= r0 for p in cell for k in range(4))
            if not ok:
                stats['failed'] += 1
            stats['central_leaves'] += 1
        elif node[0] == 'D':
            y = [q(x) for x in node[1]]
            mus = [[q(x) for x in mu] for mu in node[2]]
            ok, mg = check_dual_leaf(cell, y, mus)
            stats['dual_leaves'] += 1
            if not ok:
                stats['failed'] += 1
            elif worst[0] is None or float(mg.mid()) < float(worst[0].mid()):
                worst[0] = mg
        else:
            raise ValueError(node)

    t0 = time.time()
    rec(root)
    assert pos == len(nodes), 'trailing nodes'
    stats['min_margin'] = str(worst[0])
    stats['runtime_s'] = round(time.time() - t0, 2)
    stats['verdict'] = 'PASS' if stats['failed'] == 0 else 'FAIL'
    return stats


if __name__ == '__main__':
    print(json.dumps(main(sys.argv[1])))
