"""Audit named affine symmetries and resolution transport on a pinned RDSQS witness.
This is not a substitute for the separate full RDSQS validity checker.
Usage: FILE EXPECTED_V MULTIPLIER EXPECTED_SHA NEW_RECEIPT.json
"""
from collections import Counter
from datetime import datetime
import hashlib
from math import gcd
from pathlib import Path
import json
import sys
from zoneinfo import ZoneInfo


def image(block, f):
    return frozenset(f(x) for x in block)


def image_class(cls, f):
    return frozenset(image(t, f) for t in cls)


def image_resolution(res, f):
    return frozenset(image_class(c, f) for c in res)


def orbit_sizes(items, generators):
    unseen, sizes = set(items), []
    while unseen:
        first = next(iter(unseen))
        orbit, stack = set(), [first]
        while stack:
            x = stack.pop()
            if x in orbit:
                continue
            if x not in items:
                raise ValueError('generator leaves the named set')
            orbit.add(x)
            stack.extend(g(x) for g in generators)
        unseen -= orbit
        sizes.append(len(orbit))
    return {str(k): v for k, v in sorted(Counter(sizes).items())}


def main():
    file, v, multiplier, expected_sha, output = sys.argv[1:]
    v, multiplier = int(v), int(multiplier)
    if Path(output).exists():
        raise ValueError('refusing overwrite')
    raw = Path(file).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha:
        raise ValueError('input SHA mismatch')
    lines = [l for l in raw.decode('ascii').splitlines() if not l.startswith('#')]
    if lines[:2] != ['RDSQS ' + str(v), 'BLOCKS'] or gcd(v, multiplier) != 1:
        raise ValueError('header or multiplier')
    pos, nb = 2, v * (v - 1) * (v - 2) // 24
    blocks = frozenset(frozenset(map(int, row.split())) for row in lines[pos:pos + nb])
    pos += nb
    resolutions = {}
    for x in range(v):
        if lines[pos] != 'POINT ' + str(x):
            raise ValueError('point order')
        pos += 1
        classes = []
        for c in range((v - 2) // 2):
            if lines[pos] != 'CLASS ' + str(c):
                raise ValueError('class order')
            pos += 1
            count = (v - 1) // 3
            classes.append(frozenset(frozenset(map(int, row.split())) for row in lines[pos:pos + count]))
            pos += count
        resolutions[x] = frozenset(classes)
    if pos != len(lines):
        raise ValueError('unconsumed data')
    shift = lambda x: (x + 1) % v
    scale = lambda x: multiplier * x % v
    shift_ok = frozenset(image(b, shift) for b in blocks) == blocks
    scale_ok = frozenset(image(b, scale) for b in blocks) == blocks
    h, m = [], 1
    while m not in h:
        h.append(m)
        m = m * multiplier % v
    if m != 1:
        raise ValueError('unit subgroup cycle')
    res0 = resolutions[0]
    invariant_res0 = image_resolution(res0, scale) == res0
    transported = all(image_resolution(res0, lambda y, x=x: (y + x) % v) == resolutions[x]
                      for x in range(v))
    classwise_negation = all(image_class(c, lambda x: -x % v) == c for c in res0)
    transposition = lambda x: 1 if x == 0 else 0 if x == 1 else x
    negative_rejected = frozenset(image(b, transposition) for b in blocks) != blocks
    if not all([shift_ok, scale_ok, invariant_res0, transported, negative_rejected]):
        raise ValueError('symmetry/transport/control failed')
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'status': 'PARENT_AFFINE_SYMMETRY_AND_RESOLUTION_TRANSPORT_PASS',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'v': v, 'input_sha256': expected_sha, 'multiplier': multiplier,
              'multiplicative_subgroup': sorted(h), 'subgroup_order': len(h),
              'affine_group_order': v * len(h), 'block_set_preserved_by_translation': shift_ok,
              'block_set_preserved_by_multiplier': scale_ok,
              'block_orbits_affine': orbit_sizes(blocks, [lambda b: image(b, shift), lambda b: image(b, scale)]),
              'block_orbits_translation': orbit_sizes(blocks, [lambda b: image(b, shift)]),
              'resolution0_invariant_as_class_set': invariant_res0,
              'class_orbits_at0': orbit_sizes(res0, [lambda c: image_class(c, scale)]),
              'each_class_at0_fixed_by_negation': classwise_negation,
              'every_listed_resolution_is_translation_of_resolution0': transported,
              'transposition_control_rejected': negative_rejected,
              'limits': 'Audits this subgroup, not the full automorphism group. Transport compares unordered class sets; ordered class labels may be permuted by the expander.'}
    with Path(output).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
