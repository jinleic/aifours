#!/usr/bin/env python3
"""Check the actual Pandya table's disjoint-sector rank witnesses exactly.

This checks finite source structure and partitioning only. Invariance under
arbitrary local invertibles and its physical caller are written arguments.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path

TABLE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt')
EXPECTED = 'cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38'
OUT = Path(__file__).with_name('parent-sector-structure-result-v1.json')
H = {1, 2}
K = {0, 3, 4, 5}


def parse(raw):
    points = {}
    cells = set()
    for line in raw.decode('ascii').splitlines():
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        a, b = map(int, fields[:2])
        if (a, b) in cells or not (0 <= a < 6 and 0 <= b < 6):
            raise ValueError('TABLE_CELL')
        cells.add((a, b))
        for token in fields[2:]:
            if len(token) != 3 or token[0] not in '+-s' or any(x not in '012345' for x in token[1:]):
                raise ValueError('TOKEN')
            x = (a, b, int(token[1]), int(token[2]))
            if x in points:
                raise ValueError('DUPLICATE')
            points[x] = token[0]
    if len(cells) != 36:
        raise ValueError('CELL_COUNT')
    return points


def check(points):
    groups = collections.defaultdict(dict)
    for x, coefficient in points.items():
        active = tuple(i for i, v in enumerate(x) if v in H)
        groups[active][x] = coefficient
    pairs = list(itertools.combinations(range(4), 2))
    if set(groups) != {()} | set(pairs):
        raise ValueError('SECTOR_SET')
    if len(groups[()]) != 12 or any(v != 's' for v in groups[()].values()):
        raise ValueError('P_SECTOR')
    if any(len(groups[pair]) != 8 or any(c not in '+-' for c in groups[pair].values()) for pair in pairs):
        raise ValueError('E_SECTOR')
    for left in pairs:
        right = tuple(i for i in range(4) if i not in left)
        rows = {tuple(x[i] for i in left) for x in groups[()]}
        cols = {tuple(x[i] for i in right) for x in groups[()]}
        if len(rows) != 12 or len(cols) != 12:
            raise ValueError('P_MATCHING')
    blocks = 0
    for i, j in pairs:
        k, l = (t for t in range(4) if t not in (i, j))
        block = collections.defaultdict(dict)
        for x, sign in groups[(i, j)].items():
            block[(x[k], x[l])][(x[i], x[j])] = 1 if sign == '+' else -1
        if len(block) != 4 or {x for x, _ in block} != K or {y for _, y in block} != K:
            raise ValueError('E_SPECTATOR_MATCHING')
        for entries in block.values():
            a, b = entries.get((1, 1), 0), entries.get((1, 2), 0)
            c, d = entries.get((2, 1), 0), entries.get((2, 2), 0)
            if len(entries) != 2 or a*d-b*c == 0:
                raise ValueError('E_BLOCK_DETERMINANT')
            blocks += 1
    # A single unrestricted party still leaves all seven original sectors
    # distinguishable by the preserved H/K pattern of the other parties.
    for free in range(4):
        patterns = {tuple(int(j in active) for j in range(4) if j != free) for active in groups}
        if len(patterns) != 7 or (1, 1, 1) in patterns:
            raise ValueError('FREE_PARTY_PATTERN')
    return {'support': len(points), 'p_terms': len(groups[()]), 'e_sectors': len(pairs),
            'e_terms_each': 8, 'p_bipartitions': len(pairs), 'nonzero_2x2_blocks': blocks,
            'free_party_choices': 4, 'distinct_patterns_each': 7}


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    raw = TABLE.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED:
        raise ValueError('TABLE_HASH')
    points = parse(raw)
    counts = check(points)
    if counts['support'] != 60:
        raise ValueError('SUPPORT_COUNT')
    broken = dict(points)
    del broken[next(x for x in broken if sum(v in H for v in x) == 2)]
    try:
        check(broken)
    except ValueError as exc:
        control = str(exc) == 'E_SECTOR'
    else:
        control = False
    if not control:
        raise ValueError('DELETION_CONTROL')
    result = {'verdict': 'PASS', 'table_sha256': digest, 'checked': counts,
              'delete_E_coefficient_control': 'E_SECTOR',
              'scope': 'Finite source-sector matching and coefficient structure only; not an all-orbit AME lower bound.'}
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with OUT.open('x', encoding='utf-8') as f:
        f.write(text)
    print(text, end='')


if __name__ == '__main__':
    main()
