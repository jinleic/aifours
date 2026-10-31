#!/usr/bin/env python3
"""Parent exact diagnostics: disconnected shell privacy and negative floor."""
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-full-critical-moment-region-v1.md')
PIN = 'c8ce61fb2d40463f5fdf488cb2ed5aebe40bf59c8bd97dc18b7674caf94bf463'
OUT = ROOT / 'parent-disconnected-shell-check-result-v1.json'


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, text=True, capture_output=True).stdout.strip()


def shift_norm(x):
    t = abs(x)
    return 2*t*t - Q(2, 3)*t*t*t if t <= 1 else 2*t - Q(2, 3)


def ceil_q(x):
    return -((-x.numerator) // x.denominator)


def level(point):
    # Four separated closed diamonds, radius 1/3, centered at (+/-2,+/-2).
    distance = min(abs(point[0]-i) + abs(point[1]-j)
                   for i, j in itertools.product((-2, 2), repeat=2))
    return ceil_q(max(Q(0), distance - Q(1, 3)))


def main():
    started = clock()
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != PIN:
        raise ValueError('SOURCE_HASH_MISMATCH')
    if OUT.exists():
        raise FileExistsError(OUT)
    axis = [Q(i, 2) for i in range(-8, 9)]
    points = list(itertools.product(axis, repeat=2))
    shifts = [(Q(i, 2), Q(j, 2)) for i, j in itertools.product(range(-2, 3), repeat=2)
              if abs(i) + abs(j) <= 2]
    comparisons = 0
    wrong_exponent_failures = 0
    for point in points:
        for shift in shifts:
            other = tuple(x+h for x, h in zip(point, shift))
            delta = abs(level(point)-level(other))
            if delta > 1:
                raise AssertionError('FULL_DIAMOND_SHIFT_FAILURE')
            wrong_exponent_failures += 2*delta > 1
            comparisons += 1
    # Exact closed-boundary levels and a missing-core control.
    if level((Q(7, 3), Q(2))) != 0 or level((Q(10, 3), Q(2))) != 1:
        raise AssertionError('CLOSED_SHELL_BOUNDARY')
    if level((Q(0), Q(0))) == 0 or not wrong_exponent_failures:
        raise AssertionError('DISCONNECTED_CONTROL')
    floor_checks = 0
    for theta in (-1, -2, -10):
        s = Q(1, 4*abs(theta))
        for x, y in points:
            norm2 = x*x+y*y
            q = shift_norm(x)+shift_norm(y)
            if not 0 <= q <= 2*norm2:
                raise AssertionError('DIAMOND_TRANSLATE_BOUND')
            actual = Q(2, 3)+2*norm2+theta*s*(Q(4, 3)+q)
            lower = Q(2, 3)-Q(4, 3)*abs(theta)*s+norm2
            if actual < lower:
                raise AssertionError('NEGATIVE_THETA_FLOOR')
            floor_checks += 1
    # Translation-mixture moment identity for arbitrary symmetric finite cores.
    atoms = [(Q(x), Q(y)) for x, y in itertools.product((-2, 2), repeat=2)]
    original_j = sum(x*x+y*y for x, y in atoms)/len(atoms)
    original_l = sum(abs(x)+abs(y) for x, y in atoms)/len(atoms)
    delta = Q(1, 13)
    moved_j = sum((x+1)**2+y*y for x, y in atoms)/len(atoms)
    moved_l = sum(abs(x+1)+abs(y) for x, y in atoms)/len(atoms)
    mixed_j = (1-delta)*original_j+delta*moved_j
    mixed_l = (1-delta)*original_l+delta*moved_l
    if mixed_j-original_j != delta or abs(mixed_l-original_l) > delta:
        raise AssertionError('VERTICAL_RAY_MOMENT_IDENTITY')
    receipt = {'kind': 'PARENT_DISCONNECTED_SHELL_DIAGNOSTIC',
               'started_native_clock': started, 'finished_native_clock': clock(),
               'candidate_sha256': digest,
               'exact_shift_pairs': comparisons,
               'wrong_doubled_level_failures': wrong_exponent_failures,
               'negative_theta_floor_checks': floor_checks,
               'core_contains_origin': False,
               'closed_boundary_checks': True,
               'translation_moment_increase': str(mixed_j-original_j),
               'limits': 'Finite rational diagnostics only. No general all-law proof, '
                         'asymptotic, topology or novelty certification.'}
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(receipt, sort_keys=True))


if __name__ == '__main__':
    main()
