"""Parent definition-first covering-sequence checker; imports no lane code.
Strict two-line ASCII format: COVERING-SEQUENCE n R L, then exactly L space-separated bits, final newline.
Checks EVERY binary n-word, including 0^n and 1^n, against all cyclic windows modulo the actual L.
CLI: FILE EXPECTED_N EXPECTED_R EXPECTED_L EXPECTED_SHA256 NEW_RECEIPT.json
Scope: exact exhaustive checking for 1<=n<=16 (the active target is n=12,R=3,L<=36).
"""
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo


class CertificateError(ValueError):
    pass


def require(ok, reason):
    if not ok:
        raise CertificateError(reason)


def check(path, expected_n, expected_r, expected_l, expected_sha):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == expected_sha, 'input SHA mismatch')
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as exc:
        raise CertificateError('certificate is not ASCII') from exc
    require(text.endswith('\n'), 'missing final newline')
    lines = text.splitlines()
    require(len(lines) == 2, 'expected exactly two lines')
    match = re.fullmatch(r'COVERING-SEQUENCE ([1-9][0-9]*) (0|[1-9][0-9]*) ([1-9][0-9]*)', lines[0])
    require(match is not None, 'invalid header')
    n, radius, length = map(int, match.groups())
    require((n, radius, length) == (expected_n, expected_r, expected_l), 'expected parameter mismatch')
    require(1 <= n <= 16 and 0 <= radius <= n, 'unsupported n or invalid radius')
    require(re.fullmatch(r'[01]( [01])*', lines[1]) is not None, 'invalid bit line')
    bits = [int(x) for x in lines[1].split(' ')]
    require(len(bits) == length, 'bit count differs from header length')
    windows = []
    for j in range(length):
        word = 0
        for k in range(n):
            word = (word << 1) | bits[(j + k) % length]
        windows.append(word)
    hist = Counter()
    endpoints = {}
    for target in range(1 << n):
        nearest = min(bin(target ^ word).count('1') for word in windows)
        require(nearest <= radius, f'uncovered word {target:0{n}b}: nearest distance {nearest} exceeds {radius}')
        hist[nearest] += 1
        if target in (0, (1 << n) - 1):
            endpoints[f'{target:0{n}b}'] = nearest
    return {'status': 'VALID_COVERING_SEQUENCE', 'n': n, 'R': radius, 'L': length,
            'input_sha256': digest, 'words_checked': 1 << n, 'covering_radius': max(hist),
            'nearest_distance_histogram': dict(sorted(hist.items())), 'endpoint_distances': endpoints}


def main():
    if len(sys.argv) != 7:
        raise SystemExit('Usage: FILE EXPECTED_N EXPECTED_R EXPECTED_L EXPECTED_SHA256 NEW_RECEIPT.json')
    path, n, radius, length, digest, output = sys.argv[1:]
    out = Path(output)
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    try:
        result = check(path, int(n), int(radius), int(length), digest)
        rc = 0
    except (CertificateError, OSError) as exc:
        result = {'status': 'INVALID', 'error_type': type(exc).__name__, 'reason': str(exc)}
        rc = 1
    result['recorded_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    result['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result))
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
