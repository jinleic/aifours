#!/usr/bin/env python3
"""Bounded exact or convex-relaxed search of the final canonical spectrum.
A solver UNSAT result is not by itself a certified class exclusion.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
import z3

ROOT = Path(__file__).resolve().parents[1]


def signed(m):
    return m if m % 8 == 2 else -m


def sum_smt(terms):
    if not terms:
        return '0'
    if len(terms) == 1:
        return terms[0]
    return '(+ ' + ' '.join(terms) + ')'


def signed_term(v, sign):
    return v if sign == 1 else '(- ' + v + ')'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=('lp', 'exact'), required=True)
    parser.add_argument('--seconds', type=int, default=300)
    parser.add_argument('--prefix', default=None)
    args = parser.parse_args()
    prefix = ROOT / (args.prefix or 'results/final-' + args.mode)
    start = time.monotonic()
    z3.set_param('memory_max_size', 3500)
    screen = json.loads(gzip.decompress((ROOT / 'results/screen.json.gz').read_bytes()))
    case = [r for r in screen['classes'] if r['class_stage'] == 'UNKNOWN']
    assert len(case) == 1 and case[0]['source'] == 96 and case[0]['normal'] == 511
    case = case[0]
    candidates = [q for q in case['quadratic_candidates'] if q['rejected_by'] is None]
    assert len(candidates) == 1
    q = candidates[0]
    maxima = q['maxima']
    inv = q['canonical_maximum_inverse']
    assert all(a % 16 == 0 for a in inv)
    D = (q['square_capacity'] - 65536) // 64
    assert D == 56
    domains = []
    for m0, vals in zip(maxima, q['magnitude_domains']):
        domains.append([((signed(m0) - signed(m)) // 16, (m0 * m0 - m * m) // 64, m) for m in vals])
    active = [b for b, vals in enumerate(domains) if len(vals) > 1]
    lines = ['(set-logic QF_LRA)' if args.mode == 'lp' else '(set-logic QF_LIA)']
    terms_cost = []
    for b in active:
        var = 'e' + str(b)
        lines.append('(declare-fun ' + var + ' () ' + ('Real' if args.mode == 'lp' else 'Int') + ')')
        vals = domains[b]
        if args.mode == 'lp':
            lo, hi = min(v[0] for v in vals), max(v[0] for v in vals)
            lines.append(f'(assert (and (>= {var} {lo}) (<= {var} {hi})))')
            weight = 1 if hi > 0 else -3
            assert all(d >= weight * e for e, d, m in vals)
            terms_cost.append(f'(* {weight} {var})')
        else:
            options = ' '.join(f'(= {var} {e})' for e, d, m in vals)
            lines.append(f'(assert (or {options}))')
            cost = str(vals[-1][1])
            for e, d, m in reversed(vals[:-1]):
                cost = f'(ite (= {var} {e}) {d} {cost})'
            terms_cost.append(cost)
    for x in range(256):
        expr = sum_smt([signed_term('e' + str(b), 1 - 2 * ((x & b).bit_count() & 1)) for b in active])
        a = inv[x] // 16
        if args.mode == 'lp':
            lines.append(f'(assert (and (>= {expr} {a-16}) (<= {expr} {a+16})))')
        else:
            lines.append(f'(assert (or (= {expr} {a-16}) (= {expr} {a+16})))')
    cost = sum_smt(terms_cost)
    lines.append(f'(assert (<= {cost} {D}))' if args.mode == 'lp' else f'(assert (= {cost} {D}))')
    # No zero is imposed for this surviving quadratic only.  Other quadratics
    # were discarded using the necessary-zero condition, so even a certified
    # UNSAT here would not exclude the zero-free class with odd halves.
    smt = '\n'.join(lines) + '\n'
    smt_bytes = smt.encode()
    prefix.with_suffix('.smt2.gz').write_bytes(gzip.compress(smt_bytes, mtime=0))
    build_elapsed = time.monotonic() - start
    solver = z3.SolverFor('QF_LRA' if args.mode == 'lp' else 'QF_LIA')
    solver.set(timeout=args.seconds * 1000)
    solver.from_string(smt)
    solve_start = time.monotonic()
    ans = solver.check()
    out = {'status': str(ans).upper(), 'certification': 'NONE; solver result only',
           'source': 96, 'normal': 511, 'mode': args.mode,
           'z3_version': z3.get_version_string(), 'active_variables': len(active),
           'smt_sha256': hashlib.sha256(smt_bytes).hexdigest(),
           'build_seconds': build_elapsed, 'solve_seconds': time.monotonic() - solve_start,
           'elapsed_seconds': time.monotonic() - start, 'timeout_seconds': args.seconds,
           'reason_unknown': solver.reason_unknown() if ans == z3.unknown else None}
    if ans == z3.sat:
        model = solver.model()
        out['e_assignment'] = {str(b): str(model.eval(z3.Real('e' + str(b)) if args.mode == 'lp' else z3.Int('e' + str(b)))) for b in active}
    prefix.with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'e_assignment'}, sort_keys=True))


if __name__ == '__main__':
    main()
