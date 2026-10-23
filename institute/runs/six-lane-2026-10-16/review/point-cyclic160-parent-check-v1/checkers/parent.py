"""Definition-first parent verifier for a point-cyclic resolution of a cyclic 2-(v,4,1) design.

Definitions (Topalova-Zhelezova, Axioms 15(10):762, 2026, Definitions 2-5): every pair of points
lies in exactly one block; a parallel class partitions the point set; a resolution partitions the
blocks into parallel classes; a resolution is point-cyclic if some design automorphism that maps
parallel classes to parallel classes permutes the points in one cycle.  The certificate names the
v-cycle s(x) = x + 1 (mod v) on Z_v; this checker verifies that s preserves the block collection
and maps every listed class onto a listed class.  No difference-family argument is used.

Usage: FILE EXPECTED_V EXPECTED_SHA256 NEW_RECEIPT.json
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

NUM = r'(0|[1-9][0-9]*)'


class CertificateError(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise CertificateError(reason)


def orbit_lengths(items, shift):
    seen, lengths = set(), []
    for item in items:
        if item in seen:
            continue
        length, cur = 0, item
        while True:
            seen.add(cur)
            length += 1
            cur = shift(cur)
            if cur == item:
                break
            require(cur in items, 'orbit leaves the listed collection')
        lengths.append(length)
    return sorted(lengths)


def check(path, expected_v, expected_sha):
    raw = Path(path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == expected_sha, 'SHA256 mismatch')
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as e:
        raise CertificateError('non-ASCII certificate') from e
    require(text.endswith('\n') and '\r' not in text, 'noncanonical line ending')
    lines = text[:-1].split('\n')
    header = re.fullmatch(r'POINT-CYCLIC-RESOLUTION ([1-9][0-9]*) 4 ([1-9][0-9]*) ([1-9][0-9]*)', lines[0])
    require(header is not None, 'invalid header')
    v, c, b = map(int, header.groups())
    require(v == expected_v, 'v mismatch')
    require(v % 12 == 4, 'v is not 4 mod 12')
    require(c == (v - 1) // 3 and b == v // 4, 'class count or class size is not forced value')
    require(len(lines) == 1 + c * b, 'wrong number of block lines')
    classes = [[] for _ in range(c)]
    previous = 0
    for number, line in enumerate(lines[1:], start=2):
        m = re.fullmatch(' '.join([NUM] * 5), line)
        require(m is not None, f'line {number}: malformed block line')
        j, *pts = map(int, m.groups())
        require(j < c, f'line {number}: class index out of range')
        require(j >= previous, f'line {number}: class indices not nondecreasing')
        previous = j
        require(all(0 <= p < v for p in pts), f'line {number}: point out of range')
        require(pts[0] < pts[1] < pts[2] < pts[3], f'line {number}: points not strictly increasing')
        classes[j].append(frozenset(pts))
    require(all(len(cl) == b for cl in classes), 'a class does not have v/4 blocks')
    blocks = [blk for cl in classes for blk in cl]
    block_set = set(blocks)
    require(len(block_set) == len(blocks) == v * (v - 1) // 12, 'repeated block or wrong block count')
    pair_count = Counter(pair for blk in blocks for pair in combinations(sorted(blk), 2))
    all_pairs = set(combinations(range(v), 2))
    require(set(pair_count) == all_pairs, 'some pair lies in no block')
    require(all(n == 1 for n in pair_count.values()), 'some pair lies in two blocks')
    points = set(range(v))
    for j, cl in enumerate(classes):
        covered = Counter(p for blk in cl for p in blk)
        require(set(covered) == points and all(n == 1 for n in covered.values()), f'class {j} is not a partition of Z_v')
    shift_block = lambda blk: frozenset((p + 1) % v for p in blk)
    require({shift_block(blk) for blk in block_set} == block_set, 'block collection not invariant under x+1')
    class_set = {frozenset(cl) for cl in classes}
    require(len(class_set) == c, 'repeated class')
    shift_class = lambda cl: frozenset(shift_block(blk) for blk in cl)
    for j, cl in enumerate(classes):
        require(shift_class(frozenset(cl)) in class_set, f'class {j} is not mapped onto a listed class by x+1')
    class_orbits = orbit_lengths(class_set, shift_class)
    block_orbits = orbit_lengths(block_set, shift_block)
    return {'status': 'VALID_POINT_CYCLIC_RESOLUTION', 'v': v, 'k': 4, 'blocks': len(blocks),
            'pairs_covered_once': len(pair_count), 'all_pairs': len(all_pairs), 'classes': c,
            'blocks_per_class': b, 'automorphism': 'x -> x+1 mod v (one v-cycle)',
            'class_orbit_lengths': Counter(class_orbits), 'block_orbit_lengths': Counter(block_orbits)}


def main():
    if len(sys.argv) != 5:
        raise SystemExit('Usage: FILE EXPECTED_V EXPECTED_SHA256 NEW_RECEIPT.json')
    path, v, digest, out = sys.argv[1:]
    if Path(out).exists():
        raise SystemExit('Refusing to overwrite receipt')
    try:
        result = check(path, int(v), digest)
        result['class_orbit_lengths'] = {str(k): n for k, n in sorted(result['class_orbit_lengths'].items())}
        result['block_orbit_lengths'] = {str(k): n for k, n in sorted(result['block_orbit_lengths'].items())}
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
