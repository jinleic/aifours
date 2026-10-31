#!/usr/bin/env python3
"""Independent support and exact AME check of the published six-level tensor.

Table 1 is transcribed separately below; the local source file is read once and
compared cell by cell.  Coefficients are exact integer pairs a+b*sqrt(2).
No author checker imports, dependencies, file writes, or numerical threshold.
"""
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import sys

# Independent transcription of Pandya arXiv:2610.16673v1 Table 1.
SOURCE = """
-12 +21 | -02 +20 | -01 +10 | s44 | s55 | s33
-01 -10 | +00 +54 | +35 +43 | -15 -32 | -23 +41 | -24 +52
+02 +20 | -35 +43 | +00 -54 | -25 +31 | -13 +42 | +14 +51
s34 | -23 -41 | +13 +42 | s50 | -11 +22 | s05
s53 | +15 -32 | +25 +31 | +11 +22 | s04 | s40
s45 | -14 +51 | +24 +52 | s03 | s30 | +12 +21
"""


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def parse_terms(tokens):
    result = {}
    for token in tokens:
        require(len(token) == 3 and token[0] in '+-s' and token[1:].isdigit(), "invalid term")
        c, d = int(token[1]), int(token[2])
        require(0 <= c < 6 and 0 <= d < 6 and (c, d) not in result, "invalid/repeated ket")
        result[c, d] = (0, 1) if token[0] == 's' else ((1 if token[0] == '+' else -1), 0)
    require(1 <= len(result) <= 2, "invalid officer size")
    return result


def parse_primary():
    rows = [line.split('|') for line in SOURCE.strip().splitlines()]
    require(len(rows) == 6 and all(len(row) == 6 for row in rows), "primary dimensions")
    return {(a, b): parse_terms(rows[a][b].split()) for a, b in product(range(6), repeat=2)}


def parse_file(data):
    cells = {}
    for line in data.decode('utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        require(len(fields) in (3, 4), "file row size")
        a, b = int(fields[0]), int(fields[1])
        require(0 <= a < 6 and 0 <= b < 6 and (a, b) not in cells, "file coordinate")
        cells[a, b] = parse_terms(fields[2:])
    require(set(cells) == set(product(range(6), repeat=2)), "file officer coverage")
    return cells


def algebra_mul(x, y):
    a, b = x
    c, d = y
    return (a*c + 2*b*d, a*d + b*c)


def check_ame(tensor):
    for pair in combinations(range(4), 2):
        rest = tuple(i for i in range(4) if i not in pair)
        rows = {}
        for index, value in tensor.items():
            r, k = tuple(index[i] for i in pair), tuple(index[i] for i in rest)
            rows.setdefault(r, {})[k] = value
        require(len(rows) == 36, ("missing marginal row", pair))
        for u, v in product(product(range(6), repeat=2), repeat=2):
            a, b = rows.get(u, {}), rows.get(v, {})
            total = (0, 0)
            for k in a.keys() & b.keys():
                m = algebra_mul(a[k], b[k])
                total = (total[0] + m[0], total[1] + m[1])
            require(total == ((2, 0) if u == v else (0, 0)), ("AME gram", pair, u, v))


def components(edges):
    adjacency = {('r', r): set() for r in range(6)}
    adjacency.update({('c', c): set() for c in range(6)})
    for r, c in edges:
        a, b = ('r', r), ('c', c)
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen, sizes = set(), []
    for v in adjacency:
        if v in seen or not adjacency[v]:
            continue
        work, seen_component = deque([v]), {v}
        while work:
            for n in adjacency[work.popleft()]:
                if n not in seen_component:
                    seen_component.add(n)
                    work.append(n)
        seen.update(seen_component)
        sizes.append(len(seen_component))
    return sorted(sizes), [len(adjacency[v]) for v in adjacency if adjacency[v]]


def run_pencils(tensor):
    classes = Counter()
    survivor_masks = 0
    for spectator in range(4):
        counts = []
        for level in range(6):
            fixed = [index for index in tensor if index[spectator] == level]
            counts.append(len(fixed))
            for axis in [a for a in range(4) if a != spectator]:
                others = [a for a in range(4) if a not in (spectator, axis)]
                cells = [set() for _ in range(6)]
                ownership = {}
                for index in fixed:
                    owner = index[axis]
                    rc = (index[others[0]], index[others[1]])
                    require(rc not in ownership, ("cell ownership", spectator, level, axis, rc))
                    ownership[rc] = owner
                    cells[owner].add(rc)
                require(all(cells), ("zero generator", spectator, level, axis))
                edges = set(ownership)
                surviving = []
                for mask in range(1, 64):
                    union = set().union(*(cells[j] for j in range(6) if mask & (1 << j)))
                    rr = {r for r, _ in union}
                    cc = {c for _, c in union}
                    if len(union) == len(rr)*len(cc):
                        surviving.append(mask)
                sizes, degrees = components(edges)
                if len(fixed) == 12:
                    require(not surviving, ("12 mask", spectator, level, axis, surviving))
                    require(sizes == [12] and all(d == 2 for d in degrees), "12-cycle")
                    require(all(len(x) == 2 and len({r for r, _ in x}) == 2
                                and len({c for _, c in x}) == 2 for x in cells), "12 ownership")
                    classes[12] += 1
                elif len(fixed) == 9:
                    require(len(surviving) == 3 and all(m & (m-1) == 0 for m in surviving),
                            ("9 masks", spectator, level, axis, surviving))
                    singleton_owners = {1 << j for j in range(6) if len(cells[j]) == 1}
                    require(set(surviving) == singleton_owners, "singleton ownership")
                    require(sizes == [2, 2, 2, 6], "9 graph components")
                    require(Counter(degrees) == Counter({1: 6, 2: 6}), "9 graph degrees")
                    require(sorted(map(len, cells)) == [1, 1, 1, 2, 2, 2], "9 ownership counts")
                    for cellset in cells:
                        if len(cellset) == 2:
                            require(len({r for r, _ in cellset}) == 2
                                    and len({c for _, c in cellset}) == 2, "9 owner matching")
                    classes[9] += 1
                else:
                    raise ValueError(("unexpected slice size", spectator, level, len(fixed)))
                survivor_masks += len(surviving)
        require(counts == [9, 12, 12, 9, 9, 9], ("slice counts", spectator, counts))
    require(classes == Counter({12: 24, 9: 48}), ("pencil coverage", classes))
    require(survivor_masks == 144, "mask total")
    return classes, survivor_masks


def main(path):
    data = Path(path).read_bytes()
    cells = parse_file(data)
    require(cells == parse_primary(), "local table differs from primary transcription")
    tensor = {(a, b, c, d): value for (a, b), terms in cells.items() for (c, d), value in terms.items()}
    require(len(tensor) == 60, "support size")
    require(sum(1 for v in tensor.values() if v == (0, 1)) == 12, "sqrt2 count")
    check_ame(tensor)
    classes, masks = run_pencils(tensor)
    print("table_sha256=", sha256(data).hexdigest(), sep="")
    print("source_table_cells=36 support=60 sqrt2_coefficients=12")
    print("PASS primary-transcription equality; all six exact two-party Gram marginals = 2I before normalization")
    print("pencils=72 pencil12=", classes[12], " pencil9=", classes[9], " rectangular_masks=", masks, sep="")
    print("PASS all 24 spectator slices, all 63 nonempty masks per pencil, ownership and graph structures")
    # A mutation in one supplied source coefficient must fail the independent primary comparison.
    altered = {k: dict(v) for k, v in cells.items()}
    key = (0, 0)
    removed = next(iter(altered[key]))
    del altered[key][removed]
    require(altered != parse_primary(), "negative-control source mismatch")
    print("CONTROL deleting one source-table coefficient rejected at primary-transcription comparison")
    print("LIMIT: exact finite tensor/certificate; arbitrary complex local-map lower bound is proved separately")


if __name__ == '__main__':
    require(len(sys.argv) == 2, "usage: checker TABLE")
    main(sys.argv[1])
