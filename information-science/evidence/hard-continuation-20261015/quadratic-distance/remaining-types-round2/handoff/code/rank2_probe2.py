#!/usr/bin/env python3
"""Exploratory: the round-1 (2,192) joint count relaxation at z = 8, strengthened.

This adds the round-2 exact constraints for every coset histogram:
  (C)  the |W| histogram is a genuine cubic completion histogram. The R side
       uses the zero-flat class x0x1x2. The S side uses one shared class with
       W = 0 mod 8, the same for all four S cosets.
  (M1) sum_kappa W = +-64;  (M2) sum_kappa Lambda in {0,+-64};
  (A)  #{W = 8 mod 16} in {0,32,64}.

The solver's sat verdict comes with an explicit witness, which
rank2_witness_check-style tests and the audit recheck. An unsat/unknown
verdict is NOT a certificate and carries no claim.
"""
import argparse, itertools, json, os, sys, time
import z3

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')


def walsh2(bits):
    return [sum((-1) ** (bits[x] ^ (bin(x & c).count('1') & 1)) for x in range(4)) for c in range(4)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seconds', type=int, default=600)
    ap.add_argument('--tag', required=True)
    args = ap.parse_args()
    out_path = os.path.join(ROOT, 'results', 'rank2-probe2-%s.json' % args.tag)
    if os.path.exists(out_path):
        print('refusing to overwrite', out_path)
        sys.exit(2)
    table = json.load(open(os.path.join(ROOT, 'results', 'rank2-cubic-classes.json')))
    zf = [dict((v, n) for v, n in c['hist']) for c in table['zero_flat_cubic']['classes']]
    sclasses = [[dict((v, n) for v, n in h['hist']) for h in cl['completion_abs_walsh_histograms']]
                for cl in table['cubic_classes'] if cl['W_mod_8'] == 0]
    t0 = time.monotonic()
    pats = []
    for ub in itertools.product((0, 1), repeat=4):
        for wb in itertools.product((0, 1), repeat=4):
            Wu, Ww = walsh2(ub), walsh2(wb)
            pats.append(([(Wu[c] - Ww[c]) // 2 for c in range(4)], [(Wu[c] + Ww[c]) // 2 for c in range(4)],
                         sum(1 for x in range(4) if ub[x] != wb[x]), ub, wb))
    z3.set_param('memory_max_size', 1500)
    s = z3.Solver()
    s.set(timeout=args.seconds * 1000)
    x = [z3.Int('x%d' % i) for i in range(len(pats))]
    for v in x:
        s.add(v >= 0)
    s.add(z3.Sum(x) == 64)
    z = 8
    s.add(z3.Sum([x[i] * p[0][0] ** 2 for i, p in enumerate(pats)]) == 64 - z)
    s.add(z3.Sum([x[i] * p[0][0] for i, p in enumerate(pats)]) == 0)
    ell = [z3.Int('ell%d' % c) for c in (1, 2, 3)]
    acnt = [z3.Int('a%d' % c) for c in range(4)]
    for v in ell + acnt:
        s.add(v >= 0, v <= 28, v % 2 == 0)
    ctot, atot = z3.Sum(ell), z3.Sum(acnt)
    s.add(2 * (atot + ctot) + z <= 64, (z + 2 * ctot) % 8 == 0, atot % 4 == 0)
    s.add(4 * z3.Sum([x[i] * p[2] for i, p in enumerate(pats)]) == 496 - z - 2 * ctot)
    k0 = [z3.Bool('k0_%d' % i) for i in range(len(pats))]
    s.add(z3.PbEq([(b, 1) for b in k0], 1))
    for i in range(len(pats)):
        s.add(z3.Implies(k0[i], x[i] >= 1))

    def strengthen(ys, Wof, Lof, allowed, name):
        Wvals = sorted({abs(Wof(k)) for k in ys})
        for v in Wvals:
            if v not in {a for h in allowed for a in h} and v != 0:
                s.add(z3.Sum([y for k, y in ys.items() if abs(Wof(k)) == v]) == 0)
        sel = [z3.Bool('%s_cls%d' % (name, j)) for j in range(len(allowed))]
        s.add(z3.PbEq([(b, 1) for b in sel], 1))
        allv = sorted({a for h in allowed for a in h} | set(Wvals))
        for j, h in enumerate(allowed):
            s.add(z3.Implies(sel[j], z3.And([z3.Sum([y for k, y in ys.items() if abs(Wof(k)) == v] or [z3.IntVal(0)]) == h.get(v, 0) for v in allv])))
        sw = z3.Sum([y * Wof(k) for k, y in ys.items()])
        s.add(z3.Or(sw == 64, sw == -64))
        sl = z3.Sum([y * Lof(k) for k, y in ys.items()])
        s.add(z3.Or(sl == 0, sl == 64, sl == -64))
        m16 = z3.Sum([y for k, y in ys.items() if Wof(k) % 16 == 8] or [z3.IntVal(0)])
        s.add(z3.Or(m16 == 0, m16 == 32, m16 == 64))
        return sel

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
        Wf = lambda k: (4 * k[1] - 16 * k[0]) // 3
        s.add(z3.Sum([y * Wf(k) ** 2 for k, y in ys.items()]) == 4096)
        s.add(z3.Sum([y * k[0] ** 2 for k, y in ys.items()]) == 144 - 2 * l)
        s.add(z3.Sum([y * k[1] ** 2 for k, y in ys.items()]) == 64 * l)
        s.add(z3.Sum([y * k[1] * k[0] for k, y in ys.items()]) == 4 * l)
        strengthen(ys, Wf, lambda k: k[1], zf, 'R%d' % c)
    scls = [z3.Bool('Scls%d' % j) for j in range(len(sclasses))]
    s.add(z3.PbEq([(b, 1) for b in scls], 1))
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
        Wf = (lambda sg: (lambda k: (sg * 32 * k[2] + 4 * k[1] - 16 * k[0]) // 3))(sgn)
        s.add(z3.Sum([y * Wf(k) ** 2 for k, y in ys.items()]) == 4096)
        s.add(z3.Sum([y * k[1] ** 2 for k, y in ys.items()]) == 64 * av)
        s0 = z3.Sum([y * k[0] for k, y in ys.items() if k[2] == 1])
        L0 = z3.Sum([y * k[1] for k, y in ys.items() if k[2] == 1])
        s.add(z3.Sum([y * k[0] ** 2 for k, y in ys.items()]) == 140 - 2 * av + 4 * sgn * s0)
        s.add(z3.Sum([y * k[0] * k[1] for k, y in ys.items()]) == 4 * av + 2 * sgn * L0)
        union = []
        owner = []
        for j, cl in enumerate(sclasses):
            for h in cl:
                union.append(h)
                owner.append(j)
        sel = strengthen(ys, Wf, lambda k: k[1], union, 'S%d' % c)
        for b, j in zip(sel, owner):
            s.add(z3.Implies(b, scls[j]))
    r = s.check()
    out = {'tag': args.tag, 'z': z, 'status': str(r), 'seconds': time.monotonic() - t0,
           'limit': args.seconds, 'certificate': 'NONE (solver verdict only; sat comes with an explicit witness)'}
    if r == z3.sat:
        m = s.model()
        out['ell'] = [m[v].as_long() for v in ell]
        out['a'] = [m[v].as_long() for v in acnt]
        out['pattern_counts'] = [{'u': list(p[3]), 'w': list(p[4]), 'count': m[x[i]].as_long()} for i, p in enumerate(pats) if m[x[i]].as_long()]
        out['aux'] = {('R%d' % c): [list(k) + [m.eval(y, model_completion=True).as_long()] for k, y in ys.items() if m.eval(y, model_completion=True).as_long()] for c, ys in auxR.items()}
        out['aux'].update({('S%d' % c): [list(k) + [m.eval(y, model_completion=True).as_long()] for k, y in ys.items() if m.eval(y, model_completion=True).as_long()] for c, ys in auxS.items()})
    else:
        out['reason'] = s.reason_unknown() if r == z3.unknown else None
    with open(out_path, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: out[k] for k in ('tag', 'status', 'seconds')}))


if __name__ == '__main__':
    main()
