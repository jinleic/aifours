#!/usr/bin/env python3
"""Explicit rich-symmetry orbit matrices and published/relaxed controls."""
from pathlib import Path
import gzip
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
SEEDS = {
'dsbf40': '68B7EF2DA03B0D3EA00DB6A96DD99AEAFDB9C842B6D5DC8C4526CE0DD29020DBB75FE3314568344E73688FF0CB2482E065231869E1AA4583765CC491F8A8DB12',
'dsbf32': '125425D30A398F36508C06817BEE122E250D973314F976AED58A3EA9120DA4FE0E4D4575C42DD0426365EBA7FC5F45BE9B2F336981B5E1863618F49474F6FE00',
'rsbf56': '3740B6A118A1E19642A85E2B7E2F3C3CB65FA0D95EC9DB1EA92BDB3666185AE0087F5FE6E0757106A12FC918754C40E8A1BCCB7A714032A8961456E066E8A801',
'perm104-ac48': '7B8F94BAD364DAC9931906F9465FF33E921E13D7552DAFD684757B662FDA3C68FA8D94B3C3659B5FCC46FD1518050F97A1E02039AAF74337134F30AB5B41D9DE',
'perm74-ac64': '0331786B34D878855663A2E961F1CB4F779EBBF6881ABB24AC033E6C2B32E0493D0891DB1888EA5E6F910310311532FC68D5F2A4B5BE6445E41F64299F0CC99A'
}


def rotate3(x):
    return ((x << 3) | (x >> 6)) & 511


def reflect(x):
    return sum(((x >> i) & 1) << (8 - i) for i in range(9))


def orbit_partition(kind):
    seen = set()
    out = []
    for x in range(512):
        if x in seen:
            continue
        todo = [x]
        orb = {x}
        for y in todo:
            images = [] if kind == 'unrestricted' else [rotate3(y)]
            if kind == '3-dsbf':
                images.append(reflect(y))
            for z in images:
                if z not in orb:
                    orb.add(z)
                    todo.append(z)
        out.append(sorted(orb))
        seen |= orb
    return out


def sxor(bits):
    s = 0
    for x, b in enumerate(bits):
        if b:
            s ^= x
    return s


def main():
    start = time.monotonic()
    tables = {name: ''.join(format(int(ch, 16), '04b') for ch in hx) for name, hx in SEEDS.items()}
    allmeta = {'bit_order': 'bits[x]=f(x); x_i=(x>>i)&1', 'published_seeds': [], 'classes': {}}
    for name, text in tables.items():
        bits = list(map(int, text))
        allmeta['published_seeds'].append({'name': name, 'bits': text, 'weight': sum(bits), 'support_xor': sxor(bits), 'sha256_ascii_bits': hashlib.sha256(text.encode()).hexdigest()})
    for kind in ('3-dsbf', '3-rsbf', 'unrestricted'):
        orbits = orbit_partition(kind)
        n = len(orbits)
        assert n == {'3-dsbf': 104, '3-rsbf': 176, 'unrestricted': 512}[kind]
        sizes = [len(o) for o in orbits]
        xors = []
        for orb in orbits:
            v = 0
            for x in orb:
                v ^= x
            xors.append(v)
        reps = [o[0] for o in orbits]
        matrix = [[sum(1 - 2 * ((a & x).bit_count() & 1) for x in orb) for orb in orbits] for a in reps]
        invariant_seeds = []
        for name, text in tables.items():
            if all(len({text[x] for x in orb}) == 1 for orb in orbits):
                invariant_seeds.append((name, [int(text[o[0]]) for o in orbits]))
        assert invariant_seeds
        lines = [f'{n} {n} {len(invariant_seeds)}', ' '.join(map(str, sizes)), ' '.join(map(str, xors)), ' '.join(map(str, reps))]
        lines += [' '.join(map(str, row)) for row in matrix]
        lines += [name + ' ' + ''.join(map(str, bits)) for name, bits in invariant_seeds]
        raw = ('\n'.join(lines) + '\n').encode()
        path = ROOT / f'inputs/{kind}.matrix.txt'
        path.write_bytes(raw)
        meta = {'kind': kind, 'input_generators': [] if kind == 'unrestricted' else ['rotate nine-bit input left by3'] + (['reverse all9 bits'] if kind == '3-dsbf' else []),
                'orbits': orbits, 'representatives': reps, 'orbit_sizes': sizes, 'orbit_xors': xors,
                'C': matrix, 'invariant_published_seed_names': [name for name, bits in invariant_seeds],
                'matrix_sha256': hashlib.sha256(raw).hexdigest(), 'matrix_bytes': len(raw)}
        allmeta['classes'][kind] = meta
    payload = (json.dumps(allmeta, separators=(',', ':')) + '\n').encode()
    (ROOT / 'inputs/orbits.json.gz').write_bytes(gzip.compress(payload, mtime=0))
    print(json.dumps({'classes': {k: len(v['orbits']) for k, v in allmeta['classes'].items()}, 'elapsed_seconds': time.monotonic() - start}, sort_keys=True))


if __name__ == '__main__':
    main()
