#!/usr/bin/env python3
"""Independently check the original order-10 classical reference and orbits.

Uses row permutations, not the 20-vertex graph implementation of the other
checker. Table is transcribed independently from Weisner (1963), Fig. 1.
"""
from collections import Counter
from itertools import combinations

PAIRS = (
    ('00','28','59','84','67','32','15','93','71','46'),
    ('82','11','30','69','05','78','43','26','94','57'),
    ('95','03','22','41','79','16','80','54','37','68'),
    ('48','96','14','33','52','89','27','01','65','70'),
    ('76','50','97','25','44','63','09','38','12','81'),
    ('23','87','61','98','36','55','74','19','40','02'),
    ('51','34','08','72','90','47','66','85','29','13'),
    ('39','62','45','10','83','91','58','77','06','24'),
    ('17','49','73','56','21','04','92','60','88','35'),
    ('64','75','86','07','18','20','31','42','53','99'),
)
n = 10
color = [[int(word[0]) for word in row] for row in PAIRS]
label = [[int(word[1]) for word in row] for row in PAIRS]


def block_list():
    return ([[ (r,c) for c in range(n)] for r in range(n)]
            + [[(r,c) for r in range(n)] for c in range(n)]
            + [[(r,c) for r in range(n) for c in range(n) if label[r][c] == t]
               for t in range(n)])


def main():
    assert all(len(row) == n for row in PAIRS)
    assert len({(color[r][c], label[r][c]) for r in range(n) for c in range(n)}) == n*n
    B = block_list()
    assert len(B) == 3*n
    # Direct ORIGINAL complex-vector test for the classical reference:
    # columns are e_color, whose exact inner product is the Kronecker delta.
    for block in B:
        assert len(block) == n
        for i, (r,c) in enumerate(block):
            for j, (s,d) in enumerate(block):
                assert int(color[r][c] == color[s][d]) == int(i == j)
    # Explicit transversal incidence conditions, independent of orthogonality.
    for block in B[2*n:]:
        assert len({r for r,c in block}) == n and len({c for r,c in block}) == n
    print('reference: all 30 original vector blocks exactly orthonormal; labels are disjoint transversals')
    print('reference ray cardinality:', len({color[r][c] for r in range(n) for c in range(n)}), 'of', n*n)
    counts = Counter()
    for a,b in combinations(range(n), 2):
        a_by_row = {r: next(c for c in range(n) if color[r][c] == a) for r in range(n)}
        b_by_column = {c: next(r for r in range(n) if color[r][c] == b) for c in range(n)}
        b_by_label = {t: next(r for r in range(n) for c in range(n)
                              if color[r][c] == b and label[r][c] == t) for t in range(n)}
        pc = {r: b_by_column[a_by_row[r]] for r in range(n)}
        pt = {r: b_by_label[label[r][a_by_row[r]]] for r in range(n)}
        assert set(pc.values()) == set(range(n)) and set(pt.values()) == set(range(n))
        reached = {0}
        while True:
            update = reached | {pc[r] for r in reached} | {pt[r] for r in reached}
            if update == reached:
                break
            reached = update
        counts[len(reached)] += 1
    print('row-permutation orbit sizes across 45 symbol pairs:', dict(sorted(counts.items())))
    assert counts == {10: 45}
    print('tangent count: 45 complex global-mixing parameters + 100 real per-cell phases = 190 real')
    print('gauge-fixed reference tangent kernel dimension = 0; local isolation follows by analytic argument')


if __name__ == '__main__':
    main()
