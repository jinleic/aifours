"""Finite exact-Fraction audit of the pinned double-double primitives, not a universal proof."""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'depolarizing-dd-snapshot.py'
PIN = 'cbfb39f420cf9fe47476c088e4f40650e5a4b1f35675c37def14834335237a21'
EPS = F(1, 2 ** 100)


def exact(x) -> F:
    return F.from_float(float(x))


def value(x) -> F:
    return exact(x.hi) + exact(x.lo)


def main() -> None:
    actual = hashlib.sha256(SNAP.read_bytes()).hexdigest()
    if actual != PIN:
        raise RuntimeError('Primitive snapshot hash mismatch')
    spec = importlib.util.spec_from_file_location('pinned_dd', SNAP)
    dd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dd)
    rng = random.Random(20261016)
    counts = {'add': 0, 'mul': 0, 'mul_d': 0, 'sqrt_int': 0, 'recip_int': 0}
    ratios = {'add': F(0), 'mul': F(0), 'mul_d': F(0)}
    for trial in range(3000):
        exponent = rng.randint(-900, 0)
        hi = math.ldexp(1.0 + rng.random(), exponent)
        lo = math.ldexp((rng.random() - 0.5), exponent - 53)
        a = dd.DD(hi, lo)
        bh = math.ldexp(1.0 + rng.random(), rng.randint(-20, -1))
        bl = math.ulp(bh) * (rng.random() - 0.5)
        b = dd.DD(bh, bl)
        other_h = math.ldexp(1.0 + rng.random(), rng.randint(-900, 0))
        other = dd.DD(other_h, math.ulp(other_h) * (rng.random() - 0.5))
        for kind, result, target, scale in (
            ('add', dd.add(a, other), value(a) + value(other), value(a) + value(other)),
            ('mul', dd.mul(a, b), value(a) * value(b), value(a) * value(b)),
            ('mul_d', dd.mul_d(a, bh), value(a) * exact(bh), value(a) * exact(bh)),
        ):
            error = abs(value(result) - target)
            ratio = error / (EPS * scale)
            if ratio > 1:
                raise RuntimeError(f'{kind} bound failed at trial {trial}: ratio={ratio}')
            ratios[kind] = max(ratios[kind], ratio)
            counts[kind] += 1
        m = rng.randint(1, 100_000_000)
        z = value(dd.sqrt_int(m))
        if not z * z / (1 + EPS) ** 2 <= m <= z * z / (1 - EPS) ** 2:
            raise RuntimeError(f'sqrt bound failed at m={m}')
        counts['sqrt_int'] += 1
        m = rng.randint(1, 1_000_000)
        z = value(dd.recip_int(m))
        if abs(z - F(1, m)) > EPS / m:
            raise RuntimeError(f'reciprocal bound failed at m={m}')
        counts['recip_int'] += 1
    # A one-ulp corrupt high word must be rejected by the same exact gate.
    bad = dd.DD(math.nextafter(1.0, math.inf), 0.0)
    if abs(value(bad) - 1) <= EPS:
        raise RuntimeError('Corruption control failed to discriminate')
    print(json.dumps({'status': 'FINITE_EXACT_CONTROLS_PASS', 'snapshot_sha256': actual,
                      'seed': 20261016, 'counts': counts,
                      'maximum_fraction_of_claimed_error_allowance': {k: float(v) for k, v in ratios.items()},
                      'one_ulp_corruption_rejected': True,
                      'limits': 'Finite exact-rational audit on the nonnegative state/coefficient domains. Does not prove primitive worst-case bounds, error accumulation, sector decomposition, entropy enclosures or any capacity theorem.'}, indent=2))


if __name__ == '__main__':
    main()
