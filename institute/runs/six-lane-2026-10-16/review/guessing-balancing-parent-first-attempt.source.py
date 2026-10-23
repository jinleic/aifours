"""Exact parent checks for triangle alphabet balancing; imports no lane code."""
from datetime import datetime
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo

EDGES = [(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,3),(2,7),(2,9),(2,10),
         (3,4),(3,8),(3,9),(4,5),(4,8),(4,10),(5,6),(5,9),(5,10),
         (6,7),(6,8),(6,9),(7,8),(7,10),(8,9),(8,10)]
COVER = [(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
NEIGHBOURS = [sorted(b if a == v else a for a,b in EDGES if a == v or b == v) for v in range(1,11)]


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def fd_failure(code):
    for v, neighbours in enumerate(NEIGHBOURS):
        decoded = {}
        for row in code:
            key = tuple(row[u-1] for u in neighbours)
            if key in decoded and decoded[key] != row[v]:
                return v+1
            decoded[key] = row[v]
    return None


def triangle_code(triangle, q):
    rows = []
    for a,b in itertools.product(range(q), repeat=2):
        row = [0]*10
        for vertex, value in zip(triangle, (a,b,(-a-b)%q)):
            row[vertex-1] = value
        rows.append(tuple(row))
    return rows


def matmul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: check_guessing_balancing_independent.py PINNED_INPUT_DIR OUTPUT.json')
    folder, out = map(Path, sys.argv[1:])
    require(not out.exists(), 'Refusing to overwrite prior evidence')
    edge_set = set(map(frozenset, EDGES))
    require(all(all(frozenset(pair) in edge_set for pair in itertools.combinations(t,2)) for t in COVER),
            'Every padding set must be a clique')
    incidence = [[int(v in t) for t in COVER] for v in range(1,11)]
    inverse = [[Q(x) for x in row] for row in json.loads((folder/'evidence/balancing-lemma-check.json').read_text())['Binv']]
    identity = [[Q(i == j) for j in range(10)] for i in range(10)]
    require(matmul(incidence,inverse) == identity and matmul(inverse,incidence) == identity,
            'Two-sided rational incidence inverse')
    require(all(sum(row) == 3 for row in incidence), 'Three incident triangles per vertex')
    require(all(sum(row) == Q(1,3) for row in inverse), 'Strictly positive balancing ray')
    wrong_inverse = [row[:] for row in inverse]
    wrong_inverse[0][0] += 1
    require(matmul(incidence,wrong_inverse) != identity, 'Inverse-entry mutation must break matrix identity')
    triangle_controls = []
    for triangle in COVER:
        for q in (2,3):
            rows = triangle_code(triangle,q)
            require(len(set(rows)) == q*q, 'Triangle parity code dimension')
            require(fd_failure(rows) is None, 'Triangle parity-code FDs')
            require([len({row[v] for row in rows}) for v in range(10)] ==
                    [q if v+1 in triangle else 1 for v in range(10)], 'Actual triangle projections')
            triangle_controls.append({'triangle':triangle,'q':q,'words':len(rows)})
    words = ['00000','00110','10010','11110','10001']
    fans = [(1,2,3,4,5),(1,2,7,6,5),(8,10,4,3,9),(8,10,7,6,9)]
    fan_rows = []
    for choices in itertools.product(words, repeat=4):
        symbols = ['']*10
        for fan, choice in zip(fans,choices):
            for vertex, bit in zip(fan,choice):
                symbols[vertex-1] += bit
        fan_rows.append(tuple(symbols))
    a_rows = triangle_code((4,8,10),3)
    b_rows = triangle_code((1,2,3),2)
    product_rows = [tuple((f[v],a[v],b[v]) for v in range(10))
                    for f,a,b in itertools.product(fan_rows,a_rows,b_rows)]
    require(len(set(product_rows)) == 22500, 'Product map injectivity')
    require(fd_failure(product_rows) is None, 'Actual nonuniform product preserves all FDs')
    bad_rows = product_rows[:]
    changed = list(bad_rows[0])
    old = changed[2]
    changed[2] = (old[0],old[1],1-old[2])
    bad_rows[0] = tuple(changed)
    failure = fd_failure(bad_rows)
    require(failure == 3, 'Mutation must violate vertex-3 decoding')
    result = {'status':'PARENT_EXACT_BALANCING_MECHANICS_PASS',
              'recorded_at_pt':datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'proposed_inverse_witness_sha256':hashlib.sha256((folder/'evidence/balancing-lemma-check.json').read_bytes()).hexdigest(),
              'incidence_inverse_entries_checked':200,'positive_balancing_ray':'B^{-1}1=(1/3)1',
              'triangle_controls':triangle_controls,'product_code_words':22500,
              'actual_product_projection_sizes':[len({row[v] for row in product_rows}) for v in range(10)],
              'product_FDs':True,'mutated_product_FD_failure_vertex':failure,'inverse_mutation_rejected':True,
              'scope':'Finite algebra and code mechanics, not a new guessing-number bound. Universal balancing/type-class proof is reviewed separately.',
              'shared_dependency':'The graph edge list is the worker transcription of the original figure, not independently re-derived here.'}
    with out.open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
