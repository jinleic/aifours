"""Definition-first parent verifier for an RDSQS(v) certificate.

SQS(v): 4-subsets of {0..v-1} with every 3-subset in exactly one block.
RDSQS(v): an SQS(v) whose derived STS(v-1) at EVERY point x is resolvable.
The derived STS at x is {B - {x} : x in B}; a resolution partitions it into
parallel classes, each partitioning the v-1 points other than x.
The certificate must list the blocks and an explicit resolution for every point.

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
    require(lines and lines[0] == 'RDSQS %d' % expected_v, 'header mismatch')
    v = expected_v
    require(v % 6 in (2, 4) and v >= 4, 'v is not an SQS order')
    nblocks = v * (v - 1) * (v - 2) // 24
    require(len(lines) > 1 and lines[1] == 'BLOCKS', 'missing BLOCKS section')
    block_lines = lines[2:2 + nblocks]
    require(len(block_lines) == nblocks, 'truncated block list')
    blocks = []
    for line in block_lines:
        blocks.append(frozenset(parse_points(line, 4, v, 'block')))
    require(len(set(blocks)) == nblocks, 'duplicate block')
    triple_count = Counter()
    for block in blocks:
        for triple in combinations(sorted(block), 3):
            triple_count[triple] += 1
    universe = set(combinations(range(v), 3))
    require(set(triple_count) == universe, 'some 3-subset is uncovered')
    require(all(n == 1 for n in triple_count.values()), 'some 3-subset is covered twice')
    derived = {x: set() for x in range(v)}
    for block in blocks:
        for x in block:
            derived[x].add(frozenset(block - {x}))
    nclasses = (v - 2) // 2
    per_class = (v - 1) // 3
    rest = lines[2 + nblocks:]
    pos = 0
    resolved = []
    for x in range(v):
        require(pos < len(rest) and rest[pos] == 'POINT %d' % x, 'missing or out-of-order POINT %d' % x)
        pos += 1
        used = set()
        for j in range(nclasses):
            require(pos < len(rest) and rest[pos] == 'CLASS %d' % j,
                    'missing or out-of-order CLASS %d at point %d' % (j, x))
            pos += 1
            covered = set()
            for _ in range(per_class):
                require(pos < len(rest), 'truncated class at point %d' % x)
                triple = frozenset(parse_points(rest[pos], 3, v, 'triple'))
                pos += 1
                require(x not in triple, 'class triple contains its own point')
                require(triple in derived[x], 'class triple is not a derived triple')
                require(triple not in used, 'derived triple used twice in a resolution')
                require(not (triple & covered), 'class is not a partial partition')
                used.add(triple)
                covered |= triple
            require(covered == set(range(v)) - {x}, 'class does not partition the derived point set')
        require(used == derived[x], 'resolution does not use every derived triple')
        resolved.append(x)
    require(pos == len(rest), 'trailing lines after the last resolution')
    return {'status': 'VALID_RDSQS', 'v': v, 'sha256': digest, 'blocks': nblocks,
            'distinct_triples_covered': len(triple_count), 'triple_universe': len(universe),
            'points_resolved': len(resolved), 'classes_per_point': nclasses,
            'triples_per_class': per_class,
            'derived_triples_per_point': sorted({len(d) for d in derived.values()})}


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
