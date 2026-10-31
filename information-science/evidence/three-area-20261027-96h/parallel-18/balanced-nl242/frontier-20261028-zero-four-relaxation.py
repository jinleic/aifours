#!/opt/homebrew/bin/python3
"""Bounded exact LIA relaxation for a balanced peak-28 spectrum with four zeros.

A satisfying histogram is only a necessary-condition model, never a Boolean
function, code, realizability proof, or witness. D_j positivity is checked
independently on any output model, not assumed in this initial relaxation.
"""
import argparse
import json
import math
import pathlib
import time

import z3


def krawtchouk(n, w, j):
    return sum((-1) ** i * math.comb(w, i) * math.comb(n - w, j - i)
               for i in range(max(0, j - (n - w)), min(j, w) + 1))


def h_coeff(j):
    if j % 2 == 0:
        return (-1) ** (j // 2) * math.comb(7, j // 2)
    return 256 * (-1) ** ((j - 1) // 2) * math.comb(6, (j - 1) // 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--timeout-ms', type=int, required=True)
    ap.add_argument('--output', type=pathlib.Path, required=True)
    args = ap.parse_args()
    if not 1 <= args.timeout_ms <= 60000:
        raise ValueError('timeout must be 1..60000 ms')
    if args.output.exists():
        raise FileExistsError(args.output)
    a = {t: z3.Int(f'a_{t:+d}') for t in range(-7, 8)}
    s = z3.Solver()
    s.set(timeout=args.timeout_ms, random_seed=20261028)
    for t in a:
        s.add(a[t] >= 0, a[t] <= 511)
    s.add(a[0] == 3)
    s.add(z3.Sum(list(a.values())) == 511)
    s.add(z3.Sum([t * a[t] for t in a]) == 128)
    s.add(z3.Sum([t*t * a[t] for t in a]) == 16384)
    s.add(z3.Sum([a[t] for t in a if t % 2]) == 256)
    # Coefficientwise divisibility by 512 is necessary for the actual code.
    for j in range(15):
        coeffs = [krawtchouk(14, 7+t, j) for t in a]
        s.add((z3.Sum([coeffs[i] * a[t] for i, t in enumerate(a)]) + h_coeff(j)) % 512 == 0)
    start = time.monotonic()
    result = s.check()
    elapsed = time.monotonic() - start
    receipt = {'solver': 'z3', 'timeout_ms': args.timeout_ms, 'elapsed_seconds': elapsed,
               'status': str(result), 'scope': 'integer histogram relaxation only; no realization'}
    if result == z3.unknown:
        receipt['reason_unknown'] = s.reason_unknown()
    if result == z3.sat:
        m = s.model()
        values = {t: m.eval(a[t]).as_long() for t in a}
        assert values[0] == 3 and sum(values.values()) == 511
        assert sum(t*values[t] for t in values) == 128
        assert sum(t*t*values[t] for t in values) == 16384
        assert sum(values[t] for t in values if t % 2) == 256
        residue = [((sum(krawtchouk(14, 7+t, j)*values[t] for t in values)+h_coeff(j)) % 512)
                   for j in range(15)]
        assert residue == [0]*15
        # Exact independently evaluated long Krawtchouk sums; divisibility and
        # sign of every dual coefficient are checked without relying on Z3.
        numerators = [math.comb(256, j) + sum(values[t]*krawtchouk(256,128+t,j) for t in values)
                      for j in range(257)]
        assert all(n % 512 == 0 for n in numerators)
        negative = [j for j, n in enumerate(numerators) if n < 0]
        receipt['histogram'] = {str(t): values[t] for t in values}
        receipt['residues_15'] = residue
        receipt['negative_dual_indices'] = negative
        receipt['dual_nonnegative'] = not negative
        receipt['all_257_numerators_divisible_by_512'] = True
        receipt['dual_coefficients_decimal'] = [str(n//512) for n in numerators]
        receipt['mutation_control'] = any((n + (1 if j == 0 else 0)) % 512 for j, n in enumerate(numerators))
        assert receipt['mutation_control']
    with args.output.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print('status=', result, 'elapsed=', round(elapsed,3), 'negative_dual_indices=', receipt.get('negative_dual_indices'), flush=True)


if __name__ == '__main__':
    main()
