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
Usage: cert_cells.py CERT.json [RESULT.json] [--prec BITS] [--require-r0 P/Q]

outer/ copy (2026-10-17) of code/cert_cells.py.  Mathematical checks unchanged; additions only:
result JSON (verdict, leaf counts, min margin, runtime, sha256, versions), preorder positions of
failed leaves, graceful FAIL on truncated/garbled trees, --require-r0 (frozen r1 = 1/10000),
--prec (default 200, must be >= 128), and a cache of the per-leaf vector (a_u) keyed by the
leaf's literal (y, mu0) strings (identical strings give identical rationals, hence identical a_u).
"""
import sys, json, itertools, time, hashlib, platform
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


def a_vector(y, mus):
    a = []
    for u in range(9):
        z = [fmpq(0)] * 4
        for e, (uu, k, vv, kv) in enumerate(EDGES):
            if uu == u:
                z[k] += y[e]
            if vv == u:
                z[kv] -= y[e]
        a.append(a_bound(z, mus[u]))
    return a


def check_dual_leaf(cell, y, mus, a=None):
    if a is None:
        a = a_vector(y, mus)
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


def main(path, require_r0=None, progress_every=20000):
    t_start = time.strftime('%Y-%m-%d %H:%M:%S %Z')
    raw = open(path, 'rb').read()
    cert = json.loads(raw)
    fi, fj = cert['facet']
    r0 = q(cert['r0'])
    nstar = [fmpq(1, 9)] * 4
    perms = [s for s in itertools.permutations(range(3)) if s[fi] != fj]
    assert len(perms) == 4
    root = [nstar] + [[fmpq(int(s[0] == 0), 3), fmpq(int(s[0] == 1), 3), fmpq(int(s[1] == 0), 3), fmpq(int(s[1] == 1), 3)] for s in perms]
    nodes = cert['tree']
    pos = 0
    stats = {'dual_leaves': 0, 'central_leaves': 0, 'splits': 0, 'failed': 0, 'cache_hits': 0,
             'maxdepth': 0}
    worst = [None]
    failed_at = []
    cache = {}
    t0 = time.time()

    def rec(cell, depth):
        nonlocal pos
        here = pos
        node = nodes[pos]; pos += 1
        stats['maxdepth'] = max(stats['maxdepth'], depth)
        if node[0] == 'S':
            i, j = node[1], node[2]
            mid = [(cell[i][k] + cell[j][k]) / 2 for k in range(4)]
            c1 = list(cell); c1[i] = mid
            c2 = list(cell); c2[j] = mid
            stats['splits'] += 1
            rec(c1, depth + 1); rec(c2, depth + 1)
        elif node[0] == 'C':
            ok = all(abs(p[k] - fmpq(1, 9)) <= r0 for p in cell for k in range(4))
            if not ok:
                stats['failed'] += 1
                failed_at.append([here, 'C', None])
            stats['central_leaves'] += 1
        elif node[0] == 'D':
            key = (tuple(node[1]), tuple(tuple(mu) for mu in node[2]))
            y = [q(x) for x in node[1]]
            mus = [[q(x) for x in mu] for mu in node[2]]
            a = cache.get(key)
            if a is None:
                a = a_vector(y, mus)
                if len(cache) > 4096:
                    cache.clear()
                cache[key] = a
            else:
                stats['cache_hits'] += 1
            ok, mg = check_dual_leaf(cell, y, mus, a)
            stats['dual_leaves'] += 1
            if not ok:
                stats['failed'] += 1
                failed_at.append([here, 'D', str(mg)])
            elif worst[0] is None or float(mg.mid()) < float(worst[0].mid()):
                worst[0] = mg
            if progress_every and stats['dual_leaves'] % progress_every == 0:
                print(json.dumps({'progress_dual_leaves': stats['dual_leaves'], 'failed': stats['failed'],
                                  'elapsed_s': round(time.time() - t0, 1)}), file=sys.stderr, flush=True)
        else:
            raise ValueError(node)

    reason = None
    try:
        rec(root, 0)
        if pos != len(nodes):
            reason = f'trailing nodes: replay consumed {pos} of {len(nodes)}'
    except IndexError:
        reason = f'tree truncated: replay needed node {pos} but tree has {len(nodes)}'
    except (ValueError, TypeError, KeyError) as ex:
        reason = f'malformed tree near node {pos}: {ex!r}'
    if require_r0 is not None and r0 != q(require_r0):
        reason = (reason + '; ' if reason else '') + f'r0 {cert["r0"]} != required {require_r0}'
    stats['min_margin'] = str(worst[0])
    stats['min_margin_float'] = None if worst[0] is None else float(worst[0].mid())
    stats['runtime_s'] = round(time.time() - t0, 2)
    stats['verdict'] = 'PASS' if stats['failed'] == 0 and reason is None else 'FAIL'
    stats['reason'] = reason
    stats['failed_at'] = failed_at[:500]
    stats['nodes_total'] = len(nodes)
    stats['facet'] = [fi, fj]
    stats['r0'] = cert['r0']
    stats['cert'] = path
    stats['cert_sha256'] = hashlib.sha256(raw).hexdigest()
    stats['prec_bits'] = flint.ctx.prec
    stats['versions'] = {'python': platform.python_version(), 'python-flint': flint.__version__}
    stats['started'] = t_start
    stats['finished'] = time.strftime('%Y-%m-%d %H:%M:%S %Z')
    return stats


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('cert')
    ap.add_argument('result', nargs='?')
    ap.add_argument('--prec', type=int, default=200)
    ap.add_argument('--require-r0', default=None)
    args = ap.parse_args()
    assert args.prec >= 128
    flint.ctx.prec = args.prec
    res = main(args.cert, args.require_r0)
    if args.result:
        with open(args.result, 'w') as f:
            json.dump(res, f, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'failed_at'}))
    sys.exit(0 if res['verdict'] == 'PASS' else 1)
