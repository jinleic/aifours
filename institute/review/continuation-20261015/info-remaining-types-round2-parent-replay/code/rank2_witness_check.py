#!/usr/bin/env python3
"""Check the three round-1 (2,192) count witnesses against the new exact constraints.

For every coset histogram in a witness, reconstruct the signed Walsh values
W(kappa) and Lambda(kappa). The R side uses W = (4*Lam - 16*h)/3. The S side
uses W = ((2D_c-1)*32*delta + 4*Lam - 16*s)/3. Then test:

  (M1) first moment: sum_kappa W(kappa) = +-64 (any Boolean function on F_2^6);
  (M2) first moment: sum_kappa Lambda(kappa) in {0, +-64} (signed point set);
  (A)  #{kappa : W = 8 mod 16} in {0, 32, 64} (Lemma A for even ell/a, z = 8);
  (C)  the |W| histogram is a completion histogram of the correct cubic class.
       The R side uses the zero-flat class x0x1x2. The S side may use any
       class with W = 0 mod 8.

Each witness is refuted if any test fails on any coset. Input: the class
table results/rank2-cubic-classes.json. Refuses to overwrite its output.
"""
import json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
OUT = os.path.join(ROOT, 'results', 'rank2-witness-check.json')
WITNESSES = ['round1-rank2-probe-senergy-scross-aux.json',
             'round1-rank2-probe-senergy-aux.json',
             'round1-rank2-probe-scross-aux.json']


def need(cond, label):
    if not cond:
        raise ValueError('check failed: ' + label)


def main():
    if os.path.exists(OUT):
        print('refusing to overwrite', OUT)
        sys.exit(2)
    table = json.load(open(os.path.join(ROOT, 'results', 'rank2-cubic-classes.json')))
    zero_flat = {tuple(map(tuple, c['hist'])) for c in table['zero_flat_cubic']['classes']}
    even_any = set()
    for cl in table['cubic_classes']:
        if cl['W_mod_8'] == 0:
            for h in cl['completion_abs_walsh_histograms']:
                even_any.add(tuple(map(tuple, h['hist'])))
    report = []
    for fname in WITNESSES:
        w = json.load(open(os.path.join(ROOT, 'inputs', fname)))
        need(w['z'] == 8, 'witness has z = 8')
        res = {'witness': fname, 'z': w['z'], 'ell': w['ell'], 'a': w['a'], 'cosets': []}
        for key, rows in sorted(w['aux'].items()):
            side, c = key[0], int(key[1])
            Ws, Ls, n = Counter(), 0, 0
            Wsum = 0
            mod16 = 0
            for row in rows:
                if side == 'R':
                    h, lam, cnt = row
                    num = 4 * lam - 16 * h
                else:
                    s, lam, d0, cnt = row
                    sgn = -1 if c == 0 else 1
                    num = sgn * 32 * d0 + 4 * lam - 16 * s
                need(num % 3 == 0, 'integral W in witness')
                W = num // 3
                Ws[abs(W)] += cnt
                Wsum += W * cnt
                Ls += lam * cnt
                n += cnt
                if W % 16 == 8:
                    mod16 += cnt
            need(n == 64, 'histogram covers 64 characters')
            hist = tuple(sorted(Ws.items()))
            allowed = zero_flat if side == 'R' else even_any
            checks = {
                'M1_sum_W_is_pm64': Wsum in (64, -64),
                'M2_sum_Lambda_in_0_pm64': Ls in (0, 64, -64),
                'A_count_W_8mod16_in_0_32_64': mod16 in (0, 32, 64),
                'C_cubic_class_histogram': hist in allowed,
            }
            res['cosets'].append({'coset': key, 'abs_W_hist': [list(p) for p in hist],
                                  'sum_W': Wsum, 'sum_Lambda': Ls, 'count_W_8_mod_16': mod16,
                                  'checks': checks})
        res['refuted'] = any(not all(cs['checks'].values()) for cs in res['cosets'])
        res['violations'] = sorted({k for cs in res['cosets'] for k, v in cs['checks'].items() if not v})
        report.append(res)
    out = {'witnesses': report, 'all_refuted': all(r['refuted'] for r in report)}
    with open(OUT, 'w') as fh:
        json.dump(out, fh, indent=1)
    for r in report:
        print(r['witness'], 'refuted' if r['refuted'] else 'NOT refuted', r['violations'])
        for cs in r['cosets']:
            bad = [k for k, v in cs['checks'].items() if not v]
            print('   ', cs['coset'], cs['abs_W_hist'], 'sumW', cs['sum_W'], 'sumLam', cs['sum_Lambda'], 'fails', bad)


if __name__ == '__main__':
    main()
