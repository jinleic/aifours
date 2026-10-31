#!/opt/homebrew/bin/python3
"""Finite controls for three analytically classified rank-eight extremal forms."""
import argparse
import collections
import itertools
import json
import pathlib


def flat(points):
    p = min(points)
    span = {0}
    for x in points:
        span |= {y ^ x ^ p for y in tuple(span)}
    return {p ^ y for y in span}


def q6(x):
    return sum(((x >> i) & 1) * ((x >> (i + 1)) & 1) for i in (0, 2, 4)) & 1


def quadratic_support(linear, constant):
    return {x for x in range(64) if q6(x) ^ ((linear & x).bit_count() & 1) ^ constant}


def q8(x, linear, constant):
    return q6(x & 63) ^ (((x >> 6) & 1) * ((x >> 7) & 1)) ^ ((linear & x).bit_count() & 1) ^ constant


def truth(slices):
    return [int((x & 63) in slices[x >> 6]) for x in range(256)]


def anf(values):
    a = values[:]
    for j in range(8):
        for x in range(256):
            if x & (1 << j):
                a[x] ^= a[x ^ (1 << j)]
    return [x for x, v in enumerate(a) if v]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', type=pathlib.Path, required=True)
    a = p.parse_args()
    if a.output.exists():
        raise ValueError('output already exists')
    simplex = {0, 1, 2, 7, 11, 31, 47, 63}
    canon10 = {0, 3, 7, 11, 12, 13, 14, 16, 32, 48}
    max3 = max(len(flat(set(c)) & canon10) for c in itertools.combinations(canon10, 4))
    assert max3 == 5
    seven_flats = sorted({tuple(sorted(f)) for c in itertools.combinations(canon10, 5)
                          if len(f := flat(set(c))) == 16 and len(f & canon10) == 7})
    assert len(seven_flats) == 3
    hs = [set(f) for f in seven_flats]
    h5 = set(range(16))
    assert len(h5 & simplex) == 5
    d7 = quadratic_support(12, 1)
    d3 = quadratic_support(60, 0)
    assert len(d7) == len(d3) == 28
    assert len(d7 & simplex) == 7 and d3 & simplex == simplex - h5
    assert len((hs[0] ^ hs[1] ^ hs[2])) == 28
    representatives = {
        '8-8-8-22': [simplex, simplex, simplex, simplex ^ d7],
        '8-8-14-16': [simplex, simplex, simplex ^ h5, simplex ^ (h5 ^ d3)],
        '10-12-12-12': [canon10] + [canon10 ^ h for h in hs],
    }
    result = {'scope': 'finite representative and phase controls; no Boolean witness',
              'canon10_affine_3flat_max_intersection': max3,
              'canon10_seven_point_flats': seven_flats, 'representatives': {}}
    expected_quartic = [15, 51, 60, 195, 204, 240]
    expected = {120: {20: 126, 22: 120, 36: 10}, 136: {10: 10, 24: 120, 26: 126}}
    for name, slices in representatives.items():
        v = truth(slices)
        terms = anf(v)
        assert sum(v) == 46 and max(t.bit_count() for t in terms) == 4
        assert [t for t in terms if t.bit_count() == 4] == expected_quartic
        assert sorted(map(len, slices)) == list(map(int, name.split('-')))
        joint = {120: collections.Counter(), 136: collections.Counter()}
        for linear in range(256):
            for constant in (0, 1):
                Q = [q8(x, linear, constant) for x in range(256)]
                joint[sum(Q)][sum(x * y for x, y in zip(v, Q))] += 1
        assert {weight: dict(counter) for weight, counter in joint.items()} == expected
        result['representatives'][name] = {'slice_sizes': list(map(len, slices)),
                                          'weight': sum(v), 'quartic_terms': expected_quartic,
                                          'joint_counts': {str(k): dict(c) for k, c in joint.items()}}
    assert 22 not in result['representatives']['10-12-12-12']['joint_counts']['136']
    with a.output.open('x', encoding='utf-8') as out:
        json.dump(result, out, indent=2, sort_keys=True)
        out.write('\n')
    print('three representatives; all 512 quadratic phases per representative checked')


if __name__ == '__main__':
    main()
