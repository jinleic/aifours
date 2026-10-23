#!/usr/bin/env python3
"""Working-precision report for certifiers A and B (diagnostic; uses their own code paths).

For each row of a trials file this runs certify_a.certify() and certify_b.certify()
unchanged, except that their decimal display helpers are replaced by a recorder
that keeps the exact Fraction values. Widths are then computed exactly.
Reported per row:

  * working precision: A uses a binary grid of P = T + 192 + 8m bits; B uses a
    decimal grid of D = floor((T + 220) * 0.30103) + 10 digits;
  * the maximal width over j <= T of the certified enclosure of mu_j. This is
    the quantity that alternating-sum cancellation (a factor up to ~2^j) inflates;
  * the width of the final Psi_T enclosure.

A row passes iff all four widths (A and B, mu and Psi) are below 1e-40. If
cancellation had exhausted the working precision, some mu_j enclosure would have
width of order 1, because both certifiers clip only to the proved range
0 <= mu_j <= 1. Explicit checks only; exit 1 on failure.
"""
import argparse
import json
import sys
from fractions import Fraction
from math import log10
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import certify_a  # noqa: E402
import certify_b  # noqa: E402

LIMIT = Fraction(1, 10 ** 40)
_store = []


def _record(q, upper=False, places=20):
    _store.append(Fraction(q))
    return f'#{len(_store) - 1}'


def _val(token):
    return _store[int(token[1:])]


def log10_abs(q):
    """log10 |q| for a nonzero Fraction (math.log10 accepts arbitrarily large ints)."""
    q = abs(Fraction(q))
    return log10(q.numerator) - log10(q.denominator)


def show(q):
    return 'exactly 0' if q == 0 else f'10^{log10_abs(q):.2f}'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--trials', default='certificates/trials.json')
    ap.add_argument('--output', default='certificates/precision.json')
    args = ap.parse_args()
    trials = json.loads(Path(args.trials).read_text())['trials']
    certify_a.dec = _record
    certify_b.dstr = _record
    out, ok = [], True
    for t in trials:
        ra = certify_a.certify(t, verbose=False)
        rb = certify_b.certify(t, verbose=False)
        T, m = int(t['T']), len(t['rates'])
        wa, wb = _val(ra['mu_max_width']), _val(rb['mu_max_width'])
        pa = _val(ra['psi_enclosure'][1]) - _val(ra['psi_enclosure'][0])
        pb = _val(rb['psi_enclosure'][1]) - _val(rb['psi_enclosure'][0])
        good = all(x < LIMIT for x in (wa, wb, pa, pb))
        ok &= good
        rec = dict(name=t['name'], T=T, m=m,
                   A_precision_bits=ra['precision_bits'], A_rule='T + 192 + 8m bits',
                   B_decimal_digits=rb['decimal_digits'], B_rule='floor((T + 220) * 0.30103) + 10 digits',
                   cancellation_factor_at_j_eq_T=f'2^{T} = 10^{T * log10(2):.1f}',
                   A_mu_max_width=show(wa), B_mu_max_width=show(wb),
                   A_psi_width=show(pa), B_psi_width=show(pb), all_widths_below_1e_40=good)
        out.append(rec)
        print(f"PRECISION {t['name']}: A {rec['A_precision_bits']} bits: max width(mu_j) {rec['A_mu_max_width']}, "
              f"width(Psi) {rec['A_psi_width']} | B {rec['B_decimal_digits']} digits: max width(mu_j) {rec['B_mu_max_width']}, "
              f"width(Psi) {rec['B_psi_width']} | cancellation factor up to {rec['cancellation_factor_at_j_eq_T']} "
              f"-> {'OK' if good else 'INSUFFICIENT'}", flush=True)
    Path(args.output).write_text(json.dumps({'rows': out}, indent=1) + '\n')
    if not ok:
        print('FAIL: some enclosure width is not below 1e-40', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
