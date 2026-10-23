#!/usr/bin/env python3
"""An explicit commuting linear shear exchanges balanced support types146 and511.
No solver visit or heuristic is launched, and no existing input is overwritten.
"""
from pathlib import Path
import gzip
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]


def M(x):
    return x ^ (365 if (x & 146).bit_count() & 1 else 0)


def MT(a):
    return a ^ (146 if (a & 365).bit_count() & 1 else 0)


def main():
    start = time.monotonic()
    raw = (ROOT / 'inputs/orbits.json.gz').read_bytes()
    cls = json.loads(gzip.decompress(raw))['classes']['3-dsbf']
    decomposition = json.loads((ROOT / 'inputs/decomposition.json').read_text())
    where = {x: j for j, orbit in enumerate(cls['orbits']) for x in orbit}
    rotation = lambda x: ((x << 3) | (x >> 6)) & 511
    reversal = lambda x: sum(((x >> i) & 1) << (8 - i) for i in range(9))
    point_map, dual_map = [M(x) for x in range(512)], [MT(x) for x in range(512)]
    assert sorted(point_map) == sorted(dual_map) == list(range(512))
    for x in range(512):
        assert M(M(x)) == MT(MT(x)) == x
        assert M(rotation(x)) == rotation(M(x))
        assert M(reversal(x)) == reversal(M(x))
    # Exact character pairing, not a fitted spectrum match.
    for a in range(512):
        for x in range(512):
            assert (a & M(x)).bit_count() % 2 == (MT(a) & x).bit_count() % 2
    primary = [where[M(orbit[0])] for orbit in cls['orbits']]
    frequency = [where[MT(orbit[0])] for orbit in cls['orbits']]
    assert sorted(primary) == sorted(frequency) == list(range(104))
    for i, orbit in enumerate(cls['orbits']):
        assert sorted(M(x) for x in orbit) == cls['orbits'][primary[i]]
        assert sorted(MT(x) for x in orbit) == cls['orbits'][frequency[i]]
    for i in range(104):
        for j in range(104):
            assert cls['C'][i][j] == cls['C'][frequency[i]][primary[j]]
    assert M(146) == 511 and M(511) == 146 and M(365) == 365
    assert primary[0] == 0
    for a in range(512):
        assert (a & 511).bit_count() % 2 == (MT(a) & 146).bit_count() % 2
    control = next(c for c in decomposition['controls'] if c['s'] == 146)
    old = list(map(int, control['bits']))
    bits = [old[M(x)] for x in range(512)]
    sx = 0
    for x, b in enumerate(bits):
        if b:
            sx ^= x
    W = [sum((1 - 2 * b) * (-1 if (a & x).bit_count() & 1 else 1) for x, b in enumerate(bits)) for a in range(512)]
    assert sum(bits) == 256 and sx == 511 and bits[0] == 0 and max(map(abs, W)) == 36
    assert W == [control['walsh'][MT(a)] for a in range(512)]
    text = ''.join(map(str, bits))
    out = {'input_sha256': hashlib.sha256(raw).hexdigest(),
           'formula': 'M(x)=x+365*((146 dot x)mod2); M^T(a)=a+146*((365 dot a)mod2)',
           'point_map': point_map, 'dual_map': dual_map,
           'input_orbit_permutation': primary, 'frequency_orbit_permutation': frequency,
           'type_map': {'146': 511, '511': 146, '365': 365},
           'all512_commutation_and_involution_checks': True,
           'all262144_character_pairing_checks': True, 'all10816_C_matrix_permutation_checks': True,
           'equivalence_scope': 'Exact linear equivalence of the balanced3-DSBF target branches146 and511; no inequivalence claim for365.',
           'transformed_balanced_control': {'source_type': 146, 'target_type': 511, 'bits': text, 'weight': 256,
                                           'support_xor': 511, 'max_abs_W': 36, 'walsh': W,
                                           'sha256_ascii_bits': hashlib.sha256(text.encode()).hexdigest()},
           'elapsed_seconds': time.monotonic() - start}
    path = ROOT / 'inputs/type-equivalence.json'
    assert not path.exists(), 'Preserve an existing equivalence artifact instead of overwriting it.'
    path.write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(json.dumps({'equivalent_types': [146, 511], 'transformed_control_peak': 36, 'elapsed_seconds': out['elapsed_seconds']}, sort_keys=True))


if __name__ == '__main__':
    main()
