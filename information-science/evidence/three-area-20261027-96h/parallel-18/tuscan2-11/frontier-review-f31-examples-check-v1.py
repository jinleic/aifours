#!/usr/bin/env python3
"""Reconstruct named f31 example bits and direct Walsh sums, independently."""
import hashlib
import json
import sys
from pathlib import Path

if len(sys.argv) != 4:
    raise SystemExit('usage: SCRIPT SEED_FILE AUTHOR_ROOT OUTPUT')
seed_file, author_root, destination = map(Path, sys.argv[1:])
seed_raw = seed_file.read_bytes()
seeds = [line for line in seed_raw.decode().splitlines() if line and not line.startswith('#')]
if len(seeds) != 3 or any(len(line) != 128 for line in seeds):
    raise ValueError('invalid seed file')
expected_twists = [155, 54, 2]
checks = []
for index, (text, twist) in enumerate(zip(seeds, expected_twists), start=1):
    bits = [int(bit) for char in text for bit in format(int(char, 16), '04b')]
    expected = ''.join(str(bit ^ int(x in (0, 1)) ^ ((x & twist).bit_count() & 1))
                       for x, bit in enumerate(bits))
    candidate_file = author_root / ('frontier-20261028-best-seed%d.json' % index)
    raw = candidate_file.read_bytes()
    candidate = json.loads(raw)
    if (candidate['seed_index_1based'] != index or candidate['flip_indices'] != [0, 1]
            or candidate['affine_twist_frequency'] != twist or candidate['bits'] != expected):
        raise AssertionError('candidate truth table or displayed relation mismatch')
    output_bits = [int(bit) for bit in candidate['bits']]
    w = [sum(1 if not (bit ^ ((a & x).bit_count() & 1)) else -1
             for x, bit in enumerate(output_bits)) for a in range(512)]
    peak = max(abs(value) for value in w)
    checks.append({'seed': index, 'candidate_sha256': hashlib.sha256(raw).hexdigest(),
                   'bit_relation_exact': True, 'weight': sum(output_bits), 'W0': w[0],
                   'peak': peak, 'nonlinearity': (512 - peak) // 2,
                   'walsh_zeroes': sum(value == 0 for value in w),
                   'parseval': sum(value * value for value in w)})
result = {'seed_sha256': hashlib.sha256(seed_raw).hexdigest(), 'checks': checks,
          'scope': 'Actual three author truth-table files; not a target witness.'}
with destination.open('x', encoding='utf-8') as stream:
    json.dump(result, stream, indent=2, sort_keys=True)
    stream.write('\n')
print(json.dumps(result, sort_keys=True))
