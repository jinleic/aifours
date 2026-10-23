#!/usr/bin/env python3
"""type_table.py -- exact arithmetic of GENERAL-REDUCTION.md (lane point-cyclic-table200): admissible orbit types.

For v = 4n with v = 4 (mod 12) (so n = 1 mod 3), r = (v-1)/3 classes, the structure theorem (Theorem A') says
that a point-cyclic resolution (with respect to x -> x+1 on Z_v) determines
  * t: the length of the unique class orbit O_S that contains short blocks; t | n, t = 1 (mod 4)
    (t = 1: type T1, t = n: type T2, otherwise type T3), and
  * a multiset K of positive divisors k of n with 4k <= n (one entry per class orbit without short blocks; that
    orbit has length 4k),
with (E1)  t + 4 * sum(K) = r, and (Corollary E) n | lcm({t if t > 1} u {4k : k in K}).
This script enumerates all (t, K) satisfying these conditions (no search over blocks). It is a control of the
finite arithmetic only; the proofs are in GENERAL-REDUCTION.md.

Usage: type_table.py VMAX [--json OUT]     (prints every v = 4 mod 12, 16 <= v <= VMAX)
"""
import json
import math
import sys


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def partitions(total, parts, maxpart=None):
    """All multisets (nonincreasing tuples) of elements of `parts` with the given sum."""
    parts = sorted(parts, reverse=True)
    out = []

    def rec(rem, idx, acc):
        if rem == 0:
            out.append(tuple(acc))
            return
        for i in range(idx, len(parts)):
            p = parts[i]
            if p <= rem:
                acc.append(p)
                rec(rem - p, i, acc)
                acc.pop()
    rec(total, 0, [])
    return out


def lcm_all(xs):
    g = 1
    for x in xs:
        g = g * x // math.gcd(g, x)
    return g


def analyse(v):
    n, r = v // 4, (v - 1) // 3
    ks = [k for k in divisors(n) if 4 * k <= n]
    ts = [t for t in divisors(n) if t % 4 == 1]
    rows = []
    for t in ts:
        rest = r - t
        if rest < 0 or rest % 4:
            continue
        for K in partitions(rest // 4, ks):
            L = ([t] if t > 1 else []) + [4 * k for k in K]
            g = lcm_all(L) if L else 1
            rows.append({'t': t, 'type': 'T1' if t == 1 else ('T2' if t == n else 'T3'), 'K': list(K),
                         'orbit_lengths': [t] + [4 * k for k in K], 'base_blocks': (t - 1) // 4 + sum(K),
                         'lcm': g, 'lcm_ok': g % n == 0})
    return {'v': v, 'n': n, 'r': r, 'full_orbits': (n - 1) // 3, 't_options': ts, 'k_options': ks,
            'types': rows, 'admissible': [x for x in rows if x['lcm_ok']]}


def main(argv):
    vmax = int(argv[1])
    res = []
    for v in range(16, vmax + 1, 12):
        a = analyse(v)
        for row in a['types']:
            assert row['base_blocks'] == a['full_orbits'], (v, row)   # (E1) <=> (E2) consistency
        res.append(a)
        adm = a['admissible']
        tag = 'EXCLUDED (no admissible type)' if not adm else f'{len(adm)} admissible type(s)'
        print(f"v={v} n={a['n']} r={a['r']} full_orbits={a['full_orbits']} t_options={a['t_options']} "
              f"k_options={a['k_options']}: {tag}")
        for row in a['types']:
            print(f"   t={row['t']:>3} {row['type']} K={row['K']} orbit lengths={row['orbit_lengths']} "
                  f"lcm={row['lcm']} {'ok' if row['lcm_ok'] else 'fails n | lcm'}")
    if len(argv) == 4 and argv[2] == '--json':
        with open(argv[3], 'x') as f:
            json.dump(res, f, indent=1)
            f.write('\n')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
