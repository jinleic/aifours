"""Definition-first parent verifier for an mcDSQS(v) certificate (Tan-Zhou, arXiv:2503.11934v1).

SQS(v): 4-subsets of {0..v-1} with every 3-subset in exactly one block.
Derived design at x: {B - {x} : x in B}, an STS(v-1) on the other v-1 points.
r-colouring of an STS: a partition of its triples into r colour classes, each a partial parallel
class (pairwise disjoint triples).  mcDSQS(v): an SQS(v) whose derived design at EVERY point
admits a chi'(v-1)-colouring, chi' being the minimum over all STS(v-1).

This checker does not import chi' from the literature.  It requires COLOURS r to equal the
counting lower bound L = ceil(D / M) valid for EVERY STS(v-1), where D = (v-1)(v-2)/6 triples and
M = floor((v-1)/3) is the largest possible partial parallel class.  An explicit r-colouring with
r = L at every point therefore shows chi'(v-1) = L and that every derived design is minimum
colourable.  The certificate must list the blocks and an explicit colouring for every point.

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


class CertificateError(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise CertificateError(reason)


def parse_points(line, size, v, what):
    require(re.fullmatch(r'(0|[1-9][0-9]*)( (0|[1-9][0-9]*)){%d}' % (size - 1), line) is not None,
            'invalid ' + what + ' syntax')
    points = tuple(int(x) for x in line.split(' '))
    require(all(0 <= p < v for p in points), what + ' point outside range')
    require(len(set(points)) == size, 'repeated point in ' + what)
    return points


def check(path, expected_v, expected_sha):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(digest == expected_sha, 'SHA256 mismatch')
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError as e:
        raise CertificateError('non-ASCII certificate') from e
    require(text.endswith('\n') and '\r' not in text, 'noncanonical line ending')
    lines = [l for l in text.split('\n')[:-1] if not l.startswith('#')]
    v = expected_v
    require(len(lines) >= 3 and lines[0] == 'MCDSQS %d' % v, 'header mismatch')
    require(v % 6 in (2, 4) and v >= 8, 'v is not an SQS order handled here')
    D = (v - 1) * (v - 2) // 6
    M = (v - 1) // 3
    lower = -(-D // M)
    require(lines[1] == 'COLOURS %d' % lower, 'COLOURS is not the counting lower bound ceil(D/M)')
    require(lines[2] == 'BLOCKS', 'missing BLOCKS section')
    nblocks = v * (v - 1) * (v - 2) // 24
    block_lines = lines[3:3 + nblocks]
    require(len(block_lines) == nblocks, 'truncated block list')
    blocks = [frozenset(parse_points(line, 4, v, 'block')) for line in block_lines]
    require(len(set(blocks)) == nblocks, 'duplicate block')
    triple_count = Counter(t for b in blocks for t in combinations(sorted(b), 3))
    universe = set(combinations(range(v), 3))
    require(set(triple_count) == universe, 'some 3-subset is uncovered')
    require(all(n == 1 for n in triple_count.values()), 'some 3-subset is covered twice')
    derived = {x: set() for x in range(v)}
    for b in blocks:
        for x in b:
            derived[x].add(frozenset(b - {x}))
    require(all(len(d) == D for d in derived.values()), 'derived design has wrong size')
    rest = lines[3 + nblocks:]
    pos = 0
    profiles = Counter()
    for x in range(v):
        require(pos < len(rest) and rest[pos] == 'POINT %d' % x, 'missing or out-of-order POINT %d' % x)
        pos += 1
        used = set()
        sizes = []
        for j in range(lower):
            require(pos < len(rest) and rest[pos] == 'CLASS %d' % j,
                    'missing or out-of-order CLASS %d at point %d' % (j, x))
            pos += 1
            covered = set()
            size = 0
            while pos < len(rest) and not rest[pos].startswith(('CLASS', 'POINT')):
                triple = frozenset(parse_points(rest[pos], 3, v, 'triple'))
                pos += 1
                require(x not in triple, 'class triple contains its own point')
                require(triple in derived[x], 'class triple is not a derived triple')
                require(triple not in used, 'derived triple coloured twice')
                require(not (triple & covered), 'colour class is not a partial parallel class')
                used.add(triple)
                covered |= triple
                size += 1
            require(size >= 1, 'empty colour class at point %d' % x)
            require(size <= M, 'colour class larger than a partial parallel class can be')
            sizes.append(size)
        require(used == derived[x], 'colouring does not use every derived triple')
        profiles[tuple(sorted(sizes, reverse=True))] += 1
    require(pos == len(rest), 'trailing lines after the last colouring')
    return {'status': 'VALID_MCDSQS', 'v': v, 'sha256': digest, 'blocks': nblocks,
            'distinct_triples_covered': len(triple_count), 'triple_universe': len(universe),
            'points_coloured': v, 'colours': lower,
            'lower_bound': {'derived_triples': D, 'max_partial_parallel_class': M, 'ceil_D_over_M': lower},
            'class_size_profiles': {' '.join(map(str, p)): n for p, n in profiles.items()}}


def main():
    if len(sys.argv) != 5:
        raise SystemExit('Usage: FILE EXPECTED_V EXPECTED_SHA256 NEW_RECEIPT.json')
    path, v, digest, out = sys.argv[1:]
    if Path(out).exists():
        raise SystemExit('Refusing to overwrite receipt')
    try:
        result = check(path, int(v), digest)
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
