"""Parent stdlib checker for cyclic (v,k,1) difference families; imports no worker code.

Usage:
  check_cdf_independent.py --controls OUTPUT.json
  check_cdf_independent.py CERTIFICATE EXPECTED_V EXPECTED_SHA256 OUTPUT.json
Certificate format: optional '#' comment lines, one header 'CDF v k', then one block per line
(k distinct integers in [0,v), separated by single spaces). Any other line is rejected.
"""
from datetime import datetime
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

INTEGER = re.compile(r'(?:0|[1-9][0-9]*)\Z')


class CertificateError(ValueError):
    pass


def parse(text):
    header, blocks = None, []
    for number, line in enumerate(text.split('\n'), 1):
        if line == '' or line.startswith('#'):
            continue
        tokens = line.split(' ')
        if tokens[0] == 'CDF':
            if header is not None or len(tokens) != 3 or not all(INTEGER.fullmatch(t) for t in tokens[1:]):
                raise CertificateError(f'line {number}: bad or repeated header')
            header = tuple(map(int, tokens[1:]))
        else:
            if header is None or not all(INTEGER.fullmatch(t) for t in tokens):
                raise CertificateError(f'line {number}: unrecognized line')
            blocks.append(tuple(map(int, tokens)))
    if header is None:
        raise CertificateError('missing header')
    return header, blocks


def check(v, k, blocks):
    if k < 2 or v < 2 or (v - 1) % (k * (k - 1)):
        raise CertificateError('parameters do not satisfy v = 1 mod k(k-1)')
    expected = (v - 1) // (k * (k - 1))
    if len(blocks) != expected:
        raise CertificateError(f'expected {expected} blocks, found {len(blocks)}')
    seen = [0] * v
    for block in blocks:
        if len(block) != k or len(set(block)) != k or min(block) < 0 or max(block) >= v:
            raise CertificateError(f'invalid block {block}')
        for a in block:
            for b in block:
                if a != b:
                    seen[(a - b) % v] += 1
    if seen[0] != 0 or any(seen[d] != 1 for d in range(1, v)):
        bad = [d for d in range(1, v) if seen[d] != 1][:5]
        raise CertificateError(f'difference multiset not exactly once; first bad residues {bad}')
    pair_count = {}
    for block in blocks:
        for t in range(v):
            shifted = sorted((x + t) % v for x in block)
            for pair in combinations(shifted, 2):
                pair_count[pair] = pair_count.get(pair, 0) + 1
    if len(pair_count) != v * (v - 1) // 2 or set(pair_count.values()) != {1}:
        raise CertificateError('cyclic development is not a Steiner 2-design')
    for i, a in enumerate(blocks):
        sa = set(a)
        for j, b in enumerate(blocks):
            for shift in range(v if i != j else v - 1):
                s = shift if i != j else shift + 1
                overlap = len(sa & {(x + s) % v for x in b})
                if overlap > 1:
                    raise CertificateError('periodic correlation exceeds one')
    return {'v': v, 'k': k, 'blocks': len(blocks), 'differences_once': v - 1,
            'development_pairs': len(pair_count), 'max_correlation': 1}


def expand(v, initial, invariant_count, multiplier, order):
    blocks = [tuple(b) for b in initial[:invariant_count]]
    for block in initial[invariant_count:]:
        for power in range(order):
            factor = pow(multiplier, power, v)
            blocks.append(tuple((factor * x) % v for x in block))
    return blocks


def controls():
    known = {
        81: [(0, 1, 5, 12, 26), (0, 2, 10, 40, 64), (0, 3, 18, 47, 53), (0, 9, 32, 48, 68)],
        121: [(0, 14, 26, 51, 60), (0, 15, 31, 55, 59), (0, 10, 23, 52, 58), (0, 3, 36, 56, 57),
              (0, 7, 18, 45, 50), (0, 8, 30, 47, 49)],
        141: [(0, 33, 60, 92, 97), (0, 3, 45, 88, 110), (0, 18, 39, 68, 139), (0, 12, 67, 75, 113),
              (0, 1, 15, 84, 94), (0, 7, 11, 24, 30), (0, 36, 90, 116, 125)],
        221: [(0, 1, 24, 61, 116), (0, 3, 46, 65, 113), (0, 4, 73, 89, 130), (0, 6, 39, 50, 118),
              (0, 7, 66, 81, 94), (0, 8, 38, 64, 139), (0, 9, 29, 80, 107), (0, 10, 35, 93, 135),
              (0, 12, 34, 52, 88), (0, 14, 31, 63, 84), (0, 5, 77, 122, 124)],
        381: expand(381, [(0, 127, 1, 19, 361), (0, 2, 5, 79, 245), (0, 4, 26, 101, 199),
                          (0, 25, 52, 137, 200), (0, 36, 66, 187, 331), (0, 65, 114, 198, 285),
                          (0, 8, 41, 130, 258)], 1, 19, 3)}
    report = {'positive': {}, 'negative': {}}
    for v, blocks in known.items():
        report['positive'][str(v)] = check(v, 5, blocks)
    base = known[81]
    mutations = {
        'changed_element': [(0, 1, 5, 12, 27)] + base[1:],
        'dropped_block': base[:-1],
        'duplicated_block': base[:-1] + [base[0]],
        'repeated_point': [(0, 1, 5, 12, 12)] + base[1:],
        'out_of_range': [(0, 1, 5, 12, 81)] + base[1:],
    }
    for name, blocks in mutations.items():
        try:
            check(81, 5, blocks)
        except CertificateError as exc:
            report['negative'][name] = f'rejected: {exc}'
        else:
            raise SystemExit(f'Negative control accepted: {name}')
    try:
        check(101, 5, base)
    except CertificateError as exc:
        report['negative']['wrong_v'] = f'rejected: {exc}'
    else:
        raise SystemExit('Wrong-v control accepted')
    for name, text in {'bad_header': 'CDF 81\n0 1 5 12 26\n', 'noncanonical_token': 'CDF 81 5\n0 01 5 12 26\n',
                       'tab_separator': 'CDF 81 5\n0\t1 5 12 26\n'}.items():
        try:
            header, blocks = parse(text)
            check(*header, blocks)
        except CertificateError as exc:
            report['negative'][name] = f'rejected: {exc}'
        else:
            raise SystemExit(f'Parser control accepted: {name}')
    return report


def main():
    stamp = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    me = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if len(sys.argv) == 3 and sys.argv[1] == '--controls':
        out = Path(sys.argv[2])
        if out.exists():
            raise SystemExit('Refusing to overwrite prior evidence')
        result = {'status': 'CONTROLS_PASS', 'recorded_at_pt': stamp, 'checker_sha256': me, **controls()}
    elif len(sys.argv) == 5:
        cert, expected_v, expected_sha, out = Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
        if out.exists():
            raise SystemExit('Refusing to overwrite prior evidence')
        payload = cert.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        if digest != expected_sha:
            raise SystemExit(f'SHA-256 mismatch: {digest}')
        (v, k), blocks = parse(payload.decode('ascii'))
        if v != expected_v or k != 5:
            raise SystemExit('Unexpected parameters')
        result = {'status': 'VALID', 'recorded_at_pt': stamp, 'checker_sha256': me,
                  'certificate': str(cert), 'certificate_sha256': digest, **check(v, k, blocks)}
    else:
        raise SystemExit(__doc__)
    with out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
