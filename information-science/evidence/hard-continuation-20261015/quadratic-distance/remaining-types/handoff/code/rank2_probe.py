#!/usr/bin/env python3
"""Exploratory: which count constraints make the (2,192) joint coset relaxation hard?
z3 UNSAT/UNKNOWN here is NOT a certificate; only SAT witnesses are recorded as positive evidence."""
import argparse
import itertools
import json
from pathlib import Path
import time
import z3

ROOT = Path(__file__).resolve().parents[1]


def walsh2(bits):
    return tuple(sum((-1) ** (bits[x] ^ (bin(c & x).count('1') % 2)) for x in range(4)) for c in range(4))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--amod4', action='store_true')
    ap.add_argument('--s-energy', action='store_true')
    ap.add_argument('--s-cross', action='store_true')
    ap.add_argument('--seconds', type=int, default=300)
    ap.add_argument('--tag', required=True)
    args = ap.parse_args()
    t0 = time.monotonic()
    pats = []
    for ub in itertools.product((0, 1), repeat=4):
        for wb in itertools.product((0, 1), repeat=4):
            Wu, Ww = walsh2(ub), walsh2(wb)
            pats.append(([(Wu[c] - Ww[c]) // 2 for c in range(4)], [(Wu[c] + Ww[c]) // 2 for c in range(4)],
                         sum(1 for x in range(4) if ub[x] != wb[x]), ub, wb))
    z3.set_param('memory_max_size', 900)
    s = z3.Solver()
    s.set(timeout=args.seconds * 1000)
    x = [z3.Int('x%d' % i) for i in range(len(pats))]
    for v in x:
        s.add(v >= 0)
    s.add(z3.Sum(x) == 64)
    z = z3.Int('z')
    s.add(z >= 8, z <= 64, z % 2 == 0, z != 10)
    s.add(z3.Sum([x[i] * p[0][0] ** 2 for i, p in enumerate(pats)]) == 64 - z)
    s.add(z3.Sum([x[i] * p[0][0] for i, p in enumerate(pats)]) == 0)
    ell = [z3.Int('ell%d' % c) for c in (1, 2, 3)]
    acnt = [z3.Int('a%d' % c) for c in range(4)]
    for v in ell:
        s.add(v >= 0, v <= 28)
    for v in acnt:
        s.add(v >= 0, v <= 28)
    ctot, atot = z3.Sum(ell), z3.Sum(acnt)
    s.add(2 * (atot + ctot) + z <= 64, (z + 2 * ctot) % 8 == 0)
    if args.amod4:
        s.add(atot % 4 == 0)
    s.add(4 * z3.Sum([x[i] * p[2] for i, p in enumerate(pats)]) == 496 - z - 2 * ctot)
    k0 = [z3.Bool('k0_%d' % i) for i in range(len(pats))]
    s.add(z3.PbEq([(b, 1) for b in k0], 1))
    for i in range(len(pats)):
        s.add(z3.Implies(k0[i], x[i] >= 1))
    auxR, auxS = {}, {}
    for ci, c in enumerate((1, 2, 3)):
        l = ell[ci]
        ys = {}
        auxR[c] = ys
        for h in range(-4, 5):
            terms = []
            for Lam in range(-28, 29):
                if (4 * Lam - 16 * h) % 3:
                    continue
                y = z3.Int('yR%d_%d_%d' % (c, h, Lam))
                ys[(h, Lam)] = y
                s.add(y >= 0, z3.Implies(y > 0, z3.And(Lam <= l, -Lam <= l, (l - Lam) % 2 == 0)))
                terms.append(y)
            s.add(z3.Sum(terms) == z3.Sum([x[i] for i, p in enumerate(pats) if p[0][c] == h]))
        W = lambda h, L: (4 * L - 16 * h) // 3
        s.add(z3.Sum([y * W(h, L) ** 2 for (h, L), y in ys.items()]) == 4096)
        s.add(z3.Sum([y * h * h for (h, L), y in ys.items()]) == 144 - 2 * l)
        s.add(z3.Sum([y * L * L for (h, L), y in ys.items()]) == 64 * l)
        s.add(z3.Sum([y * L * h for (h, L), y in ys.items()]) == 4 * l)
    for c in range(4):
        av = acnt[c]
        sgn = -1 if c == 0 else 1
        ys = {}
        auxS[c] = ys
        for sv in range(-4, 5):
            terms = []
            for Lam in range(-28, 29):
                for d0 in (0, 1):
                    if (sgn * 32 * d0 + 4 * Lam - 16 * sv) % 3:
                        continue
                    y = z3.Int('yS%d_%d_%d_%d' % (c, sv, Lam, d0))
                    ys[(sv, Lam, d0)] = y
                    s.add(y >= 0, z3.Implies(y > 0, z3.And(Lam <= av, -Lam <= av, (av - Lam) % 2 == 0)))
                    terms.append(y)
            s.add(z3.Sum(terms) == z3.Sum([x[i] for i, p in enumerate(pats) if p[1][c] == sv]))
        s.add(z3.Sum([y for k, y in ys.items() if k[2] == 1]) == 1)
        for sv in range(-4, 5):
            s.add(z3.Implies(z3.Sum([y for k, y in ys.items() if k[2] == 1 and k[0] == sv]) == 1,
                             z3.Or([k0[i] for i, p in enumerate(pats) if p[1][c] == sv])))
        W = lambda sv, L, d0: (sgn * 32 * d0 + 4 * L - 16 * sv) // 3
        s.add(z3.Sum([y * W(*k) ** 2 for k, y in ys.items()]) == 4096)
        s.add(z3.Sum([y * k[1] ** 2 for k, y in ys.items()]) == 64 * av)
        s0 = z3.Sum([y * k[0] for k, y in ys.items() if k[2] == 1])
        L0 = z3.Sum([y * k[1] for k, y in ys.items() if k[2] == 1])
        if args.s_energy:
            s.add(z3.Sum([y * k[0] ** 2 for k, y in ys.items()]) == 140 - 2 * av + 4 * sgn * s0)
        if args.s_cross:
            s.add(z3.Sum([y * k[0] * k[1] for k, y in ys.items()]) == 4 * av + 2 * sgn * L0)
    r = s.check()
    out = {'tag': args.tag, 'amod4': args.amod4, 's_energy': args.s_energy, 's_cross': args.s_cross,
           'status': str(r), 'seconds': time.monotonic() - t0, 'limit': args.seconds,
           'certificate': 'NONE (solver verdict only)'}
    if r == z3.sat:
        m = s.model()
        out['z'] = m[z].as_long()
        out['ell'] = [m[v].as_long() for v in ell]
        out['a'] = [m[v].as_long() for v in acnt]
        out['pattern_counts'] = [{'u': list(p[3]), 'w': list(p[4]), 'count': m[x[i]].as_long()} for i, p in enumerate(pats) if m[x[i]].as_long()]
        out['kappa0_pattern'] = next({'u': list(p[3]), 'w': list(p[4])} for i, p in enumerate(pats) if z3.is_true(m.eval(k0[i], model_completion=True)))
        out['aux'] = {('R%d' % c): [list(k) + [m.eval(y, model_completion=True).as_long()] for k, y in ys.items() if m.eval(y, model_completion=True).as_long()] for c, ys in auxR.items()}
        out['aux'].update({('S%d' % c): [list(k) + [m.eval(y, model_completion=True).as_long()] for k, y in ys.items() if m.eval(y, model_completion=True).as_long()] for c, ys in auxS.items()})
    else:
        out['reason'] = s.reason_unknown() if r == z3.unknown else None
    (ROOT / ('results/rank2-probe-%s.json' % args.tag)).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ('tag', 'status', 'seconds')}))


if __name__ == '__main__':
    main()
