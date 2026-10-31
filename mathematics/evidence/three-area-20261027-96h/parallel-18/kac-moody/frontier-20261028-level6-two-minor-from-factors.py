#!/usr/bin/env python3
"""Two-minor resultant certificate from two stored, factored level-six minors.

Inputs: two factor files written by frontier-20261028-level6-minor-factor.py.
Their minor files and the pencil are hash-checked.  Bad (not one-sign) factors
of the two minors must be pairwise coprime.  For each bad pair an elimination
variable is chosen; the exact resultant H is computed from exact univariate
resultants on an integer grid (process pool) plus exact interpolation; its
squarefree part is certified for integer roots by Cauchy bound and Hensel
uniqueness.  Leading-coefficient degeneracy is handled exactly: every
nonnegative integer at which a leading coefficient vanishes is added to the
fibre list.  On every listed fibre the two univariate restrictions are tested
for common nonnegative integer roots, and any remaining point is tested by an
exact full-matrix rank computation.  Exact computation for review only.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gen = load('general', 'frontier-20261028-level6-two-minor-general.py')
S, al6 = gen.S, gen.al6
x, y = gen.x, gen.y
WORK = None


def init(work):
    global WORK
    WORK = work


def specialize(d, idx, t0, n):
    v = [0] * (n + 1)
    for mon, c in d.items():
        v[mon[idx]] += c * t0**mon[1 - idx]
    return v


def res_at(t0):
    Bd, Cd, idx, mB, mC = WORK
    t = S.Symbol('t')
    f = S.Poly(list(reversed(specialize(Bd, idx, t0, mB))), t, domain=S.ZZ)
    g = S.Poly(list(reversed(specialize(Cd, idx, t0, mC))), t, domain=S.ZZ)
    if f.degree() != mB or g.degree() != mC:
        return t0, None
    return t0, int(S.resultant(f, g))


def hashed(name):
    raw = (ROOT / name).read_bytes()
    return raw, hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--factors1', required=True)
    ap.add_argument('--factors2', required=True)
    ap.add_argument('--tag', required=True)
    ap.add_argument('--workers', type=int, default=12)
    args = ap.parse_args()
    F = []
    for name in (args.factors1, args.factors2):
        raw, sha = hashed(name)
        f = json.loads(raw)
        mraw, msha = hashed(f['minor'])
        assert msha == f['minor_sha256']
        m = json.loads(mraw)
        praw, psha = hashed(m['pencil'])
        assert psha == m['pencil_sha256']
        F.append((name, sha, f, m, psha))
    assert F[0][3]['pencil'] == F[1][3]['pencil'] and F[0][3]['rows'] != F[1][3]['rows']
    degree = F[0][3]['degree']
    out = ROOT / f"frontier-20261028-level6-{degree[0]}{degree[1]}6-two-minor-{args.tag}-v1.json"
    if out.exists():
        raise FileExistsError(out)
    bad = []
    for name, sha, f, m, psha in F:
        polys = []
        for e in f['factors']:
            if not e['strictly_positive_on_quadrant']:
                polys.append({(t['x_power'], t['y_power']): int(Q(t['coefficient'])) for t in e['coefficients']})
                assert all(Q(t['coefficient']).denominator == 1 for t in e['coefficients'])
        bad.append(polys)
    pairs = []
    fibre_points = set()
    for Bd in bad[0]:
        for Cd in bad[1]:
            B = S.Poly(sum(c * x**i * y**j for (i, j), c in Bd.items()), x, y)
            C = S.Poly(sum(c * x**i * y**j for (i, j), c in Cd.items()), x, y)
            assert S.gcd(B, C).total_degree() == 0
            choice = []
            for idx, var in ((0, x), (1, y)):
                mB, mC = B.degree(var), C.degree(var)
                lB = S.Poly(B, var).LC()
                lC = S.Poly(C, var).LC()
                const = int(bool(lB.is_number)) + int(bool(lC.is_number))
                choice.append((-const, mB * mC, idx, var, mB, mC, lB, lC))
            choice.sort(key=lambda z: (z[0], z[1]))
            _, _, idx, var, mB, mC, lB, lC = choice[0]
            other = y if idx == 0 else x
            bound = B.total_degree() * C.total_degree()
            with Pool(args.workers, initializer=init, initargs=((Bd, Cd, idx, mB, mC),)) as pool:
                got = dict(pool.imap_unordered(res_at, range(bound + 40), chunksize=2))
            pts = [t0 for t0 in sorted(got) if got[t0] is not None][:bound + 9]
            assert len(pts) == bound + 9
            # Lagrange-free exact interpolation on possibly gapped integer points via Newton divided differences.
            xs = pts[:bound + 1]
            coeffs = [Q(got[t]) for t in xs]
            n = len(xs)
            for j in range(1, n):
                for i in range(n - 1, j - 1, -1):
                    coeffs[i] = (coeffs[i] - coeffs[i - 1]) / (xs[i] - xs[i - j])
            H = [Q(0)]
            for i in range(n - 1, -1, -1):
                H = [Q(0)] + H
                for k in range(len(H) - 1):
                    H[k] -= xs[i] * H[k + 1]
                H[0] += coeffs[i]
            while len(H) > 1 and H[-1] == 0:
                H.pop()
            assert all(c.denominator == 1 for c in H)
            H = [int(c) for c in H]
            for t0 in pts:
                assert gen.peval(H, t0) == got[t0], t0
            t = S.Symbol('t')
            HP = S.Poly(list(reversed(H)), t, domain=S.ZZ)
            G = S.gcd(HP, HP.diff(t))
            W, rem = S.div(HP, G)
            assert rem.is_zero
            roots, cert = gen.integer_roots([int(c) for c in reversed(W.all_coeffs())])
            degenerate = []
            for lc in (lB, lC):
                if not lc.is_number:
                    lp = S.Poly(lc, other)
                    lr, _ = gen.integer_roots([int(c) for c in reversed(S.Poly(lp.as_expr(), other).sqf_part().all_coeffs())])
                    degenerate += [r for r in lr if r >= 0]
            fibres = []
            for t0 in sorted(set([r for r in roots if r >= 0] + degenerate)):
                fB = S.Poly(list(reversed(specialize(Bd, idx, t0, mB))), t)
                fC = S.Poly(list(reversed(specialize(Cd, idx, t0, mC))), t)
                common = S.gcd(fB, fC)
                ints = sorted({int(r) for r in common.ground_roots() if r.is_integer and r >= 0}) if common.degree() > 0 else []
                if fB.is_zero or fC.is_zero:
                    ints = ['WHOLE_FIBRE']
                fibres.append({'fixed_' + str(other): t0, 'common_gcd_degree': common.degree(), 'nonnegative_integer_common_roots': ints})
                for r in ints:
                    assert r != 'WHOLE_FIBRE', 'zero restriction needs separate handling'
                    fibre_points.add((r, t0) if idx == 0 else (t0, r))
            pairs.append({'eliminated_variable': str(var), 'resultant_variable': str(other),
                          'B_total_degree': B.total_degree(), 'C_total_degree': C.total_degree(),
                          'B_degree_in_var': mB, 'C_degree_in_var': mC,
                          'leading_coefficients_constant': [bool(lB.is_number), bool(lC.is_number)],
                          'resultant_degree': len(H) - 1, 'resultant_degree_bound': bound,
                          'grid_points_used': len(pts), 'skipped_degenerate_grid_points': [t0 for t0 in got if got[t0] is None],
                          'resultant_coefficients_low_to_high': [str(c) for c in H],
                          'repeated_part_degree': G.degree(), 'squarefree_part_degree': W.degree(),
                          'squarefree_part_integer_roots': roots, 'hensel_certificate': cert,
                          'leading_coefficient_nonnegative_integer_zeros': sorted(set(degenerate)),
                          'fibres': fibres})
    ranks = []
    if fibre_points:
        P = json.loads((ROOT / F[0][3]['pencil']).read_text())
        rows = al6.full_rows(P)
        for (x0, y0) in sorted(fibre_points):
            span = al6.lift.Span()
            words = sorted(rows)
            n = len(rows[words[0]])
            for j in range(n):
                col = {i: rows[w][j][0] + x0 * rows[w][j][1] + y0 * rows[w][j][2] for i, w in enumerate(words)}
                span.add({i: q for i, q in col.items() if q})
            ranks.append({'x': x0, 'y': y0, 'rank': len(span), 'columns': n})
    full = all(r['rank'] == r['columns'] for r in ranks)
    result = {'degree': degree, 'variables': 'x=r-6,y=s-6',
              'inputs': [{'factor_file': name, 'factor_sha256': sha, 'minor_file': f['minor'], 'minor_sha256': f['minor_sha256'],
                          'pencil_sha256': psha} for name, sha, f, m, psha in F],
              'bad_factor_counts': [len(b) for b in bad], 'pairs': pairs,
              'points_needing_rank_check': [list(p) for p in sorted(fibre_points)], 'direct_rank_checks': ranks,
              'status': 'ALL_INTEGER_QUADRANT_POINTS_FULL_RANK' if full else 'RANK_DEFECT_FOUND',
              'scope': 'exact certificate on the free-Levi pencil; actual source identification for r,s>=6 is a written input',
              'not_formal_or_external_model_review': True}
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('DONE', degree, result['status'], 'pairs', len(pairs), 'rank-checked points', len(ranks), out.name, flush=True)


if __name__ == '__main__':
    main()
