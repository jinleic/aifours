"""Independent direct-sum seed invariants, without producer imports."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def reconstruct():
    source = Path('selection-inputs/literature/kavut-yucel.reader.md').read_text()
    raw = re.findall(r'(?m)^([0-9A-F]{64}) ([0-9A-F]{64})$', source.split('#### 3.2')[0])
    assert len(raw) == 3
    result = {}
    for name, parts in zip(('dsbf40', 'dsbf32', 'rsbf56'), raw):
        hx = ''.join(parts)
        text = ''.join(format(int(c, 16), '04b') for c in hx)
        f = [int(b) for b in text]
        W = [sum((-1) ** (f[x] + bin(a & x).count('1')) for x in range(512)) for a in range(512)]
        AC = [sum((-1) ** (f[x] + f[x ^ t]) for x in range(512)) for t in range(512)]
        result[name] = {
            'hex': hx, 'sha256_ascii_bits': hashlib.sha256(text.encode()).hexdigest(),
            'weight': sum(f), 'walsh': W, 'autocorrelation': AC,
            'absolute_walsh_histogram': {str(k): v for k, v in sorted(Counter(map(abs, W)).items())},
            'absolute_indicator': max(abs(a) for a in AC[1:]),
            'minimum_balancing_distance_original_origin': abs(W[0]) // 2,
            'minimum_balancing_distance_over_linear_shifts': min(map(abs, W)) // 2,
        }
    return {'bit_order': 'bits[x]=f(x); x=0..511; x_i=(x>>i)&1; hex MSB first',
            'literature_sha256': hashlib.sha256(source.encode()).hexdigest(), 'seeds': result}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--write', action='store_true')
    args = p.parse_args()
    out = reconstruct()
    path = Path('results/seed-invariants.json')
    if args.write:
        path.write_text(json.dumps(out, indent=2) + '\n')
    else:
        assert json.loads(path.read_text()) == out
    indicators = [r['absolute_indicator'] for r in out['seeds'].values()]
    assert indicators == [40, 32, 56]
    assert len(set(indicators)) == 3
    for name, r in out['seeds'].items():
        print(name, 'weight', r['weight'], 'max|W|', max(map(abs, r['walsh'])),
              'min|W|', min(map(abs, r['walsh'])), 'absolute indicator', r['absolute_indicator'])
    print('PASS: distinct absolute indicators prohibit pairwise extended-affine equivalence.')


if __name__ == '__main__':
    main()
