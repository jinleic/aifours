"""Definition-first parent verifier for optimal (v,k,1) CPCW/OOC witnesses.
Checks all cyclic auto/cross intersections and the developed packing independently of differences.
Usage: FILE EXPECTED_V EXPECTED_K EXPECTED_SHA256 NEW_RECEIPT.json
"""
from collections import Counter
from datetime import datetime
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo


class CertificateError(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise CertificateError(reason)


def check(path, expected_v, expected_k, expected_sha):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == expected_sha, 'SHA256 mismatch')
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as e:
        raise CertificateError('non-ASCII certificate') from e
    require(text.endswith('\n') and '\r' not in text, 'noncanonical line ending')
    lines = text.splitlines()
    require(bool(lines), 'missing header')
    header = re.fullmatch(r'CPCW ([1-9][0-9]*) ([1-9][0-9]*)', lines[0])
    require(header is not None, 'invalid header')
    v, k = map(int, header.groups())
    require((v, k) == (expected_v, expected_k), 'parameter mismatch')
    require(2 <= k < v, 'invalid parameters')
    size = (v - 1) // (k * (k - 1))
    require(len(lines) == size + 1, 'codeword count is not optimal bound')
    words = []
    for line in lines[1:]:
        require(re.fullmatch(r'(0|[1-9][0-9]*)( (0|[1-9][0-9]*))*', line) is not None,
                'invalid codeword syntax')
        word = tuple(map(int, line.split(' ')))
        require(len(word) == k, 'wrong codeword weight')
        require(all(0 <= x < v for x in word), 'point outside Z_v')
        require(list(word) == sorted(set(word)), 'codeword entries not strictly increasing')
        words.append(frozenset(word))
    require(len(set(words)) == size, 'duplicate codeword')
    auto_max, cross_max = 0, 0
    for i, word in enumerate(words):
        for t in range(1, v):
            intersection = word & frozenset((x + t) % v for x in word)
            require(len(intersection) <= 1, 'auto-correlation exceeds one')
            auto_max = max(auto_max, len(intersection))
        for other in words[i + 1:]:
            for t in range(v):
                intersection = word & frozenset((x + t) % v for x in other)
                require(len(intersection) <= 1, 'cross-correlation exceeds one')
                cross_max = max(cross_max, len(intersection))
    differences = Counter((x - y) % v for word in words for x in word for y in word if x != y)
    require(0 not in differences and all(n == 1 for n in differences.values()),
            'ordered difference collision')
    leave = set(range(1, v)) - set(differences)
    require(not (v % 2 == 0) or v // 2 in leave, 'half-order difference covered')
    blocks, covered = set(), set()
    for word in words:
        for t in range(v):
            block = tuple(sorted((x + t) % v for x in word))
            require(block not in blocks, 'cyclic development has a short or repeated orbit')
            blocks.add(block)
            for pair in combinations(block, 2):
                require(pair not in covered, 'developed pair covered twice')
                covered.add(pair)
    all_pairs = set(combinations(range(v), 2))
    uncovered = all_pairs - covered
    expected_uncovered = {tuple(sorted((x, (x + d) % v))) for x in range(v) for d in leave}
    require(uncovered == expected_uncovered, 'developed leave differs from difference leave')
    return {'status': 'VALID_OPTIMAL_CPCW', 'v': v, 'k': k, 'codewords': size,
            'optimal_bound': size, 'sha256': digest,
            'auto_correlation_max': auto_max, 'cross_correlation_max': cross_max,
            'nonzero_ordered_differences': len(differences), 'uncovered_differences': sorted(leave),
            'developed_blocks': len(blocks), 'covered_unordered_pairs': len(covered),
            'uncovered_unordered_pairs': len(uncovered), 'all_pairs': len(all_pairs),
            'exact_developed_leave_matches': True}


def main():
    if len(sys.argv) != 6:
        raise SystemExit('Usage: FILE EXPECTED_V EXPECTED_K EXPECTED_SHA256 NEW_RECEIPT.json')
    path, v, k, digest, out = sys.argv[1:]
    if Path(out).exists():
        raise SystemExit('Refusing to overwrite receipt')
    try:
        result = check(path, int(v), int(k), digest)
        rc = 0
    except (CertificateError, OSError) as e:
        result = {'status': 'INVALID', 'error_type': type(e).__name__, 'reason': str(e)}
        rc = 1
    result.update(recorded_at_pt=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input=str(Path(path).resolve()))
    with Path(out).open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result))
    return rc


if __name__ == '__main__':
    raise SystemExit(main())
