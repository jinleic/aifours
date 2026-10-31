#!/usr/bin/env python3
"""Exact check of published OLS(10), plus three-partition two-symbol components.

Table: L. Weisner, Special Orthogonal Latin Squares of Order 10, Fig. 1,
Canad. Math. Bull. 6(1) (1963), DOI 10.4153/CMB-1963-009-0.
Each printed two-digit entry is (color, transversal label).
"""
from collections import Counter, defaultdict
from itertools import combinations

ROWS = (
    '00 28 59 84 67 32 15 93 71 46',
    '82 11 30 69 05 78 43 26 94 57',
    '95 03 22 41 79 16 80 54 37 68',
    '48 96 14 33 52 89 27 01 65 70',
    '76 50 97 25 44 63 09 38 12 81',
    '23 87 61 98 36 55 74 19 40 02',
    '51 34 08 72 90 47 66 85 29 13',
    '39 62 45 10 83 91 58 77 06 24',
    '17 49 73 56 21 04 92 60 88 35',
    '64 75 86 07 18 20 31 42 53 99',
)
N = 10
TABLE = tuple(tuple(tuple(map(int, word)) for word in row.split()) for row in ROWS)


def check_table():
    symbols = set(range(N))
    assert len(TABLE) == N and all(len(row) == N for row in TABLE)
    for coordinate in (0, 1):
        assert all({TABLE[r][c][coordinate] for c in range(N)} == symbols for r in range(N))
        assert all({TABLE[r][c][coordinate] for r in range(N)} == symbols for c in range(N))
    assert len({TABLE[r][c] for r in range(N) for c in range(N)}) == N*N


def components(color_a, color_b):
    vertices = {(r, c) for r in range(N) for c in range(N) if TABLE[r][c][0] in (color_a, color_b)}
    adjacency = {p: set() for p in vertices}
    # In each row, column and transversal pair the two specified colors.
    for axis in range(3):
        groups = defaultdict(list)
        for r, c in vertices:
            groups[(r, c, TABLE[r][c][1])[axis]].append((r, c))
        assert len(groups) == N and all(len(group) == 2 for group in groups.values())
        for x, y in groups.values():
            adjacency[x].add(y)
            adjacency[y].add(x)
    output = []
    remaining = set(vertices)
    while remaining:
        root = min(remaining)
        stack, component = [root], set()
        while stack:
            node = stack.pop()
            if node in component:
                continue
            component.add(node)
            stack.extend(adjacency[node] - component)
        remaining -= component
        output.append(tuple(sorted(component)))
    return tuple(sorted(output))


def main():
    check_table()
    print('published_table: PASS; both rows/columns Latin; 100 distinct ordered pairs')
    histogram = Counter()
    nontrivial = []
    for a, b in combinations(range(N), 2):
        comps = components(a, b)
        sizes = tuple(sorted(map(len, comps)))
        histogram[sizes] += 1
        if len(comps) > 1:
            nontrivial.append((a, b, sizes))
    print('all 45 color-pairs: component-size distribution', dict(sorted(histogram.items())))
    print('independent component switch opportunities:', len(nontrivial))
    for item in nontrivial:
        print('switch', *item)


if __name__ == '__main__':
    main()
