#!/usr/bin/env python3
"""Independent full-source and shifted-grid replay for two stored L6 minors.

Source completeness uses independently rebuilt horizontal combinations plus
exact Witt-character multiplicity, not the producer's kernel-dimension header.
All source brackets, actions and D3 images use the independent tree-Jacobi
engine. Both complete polynomials are checked on a shifted unisolvent grid.
FLINT exact determinants are a SHARED arithmetic library with the native minor
producer; source reconstruction, interpolation checks and replay code differ.
No formal or cross-model assurance is inferred.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-fastalgebra'))
import flint

sp = importlib.util.spec_from_file_location('tree_replay', ROOT / 'frontier-20261028-levi-critical-independent-replay.py')
ind = importlib.util.module_from_spec(sp)
sp.loader.exec_module(ind)
DATA = None


def init(data):
    global DATA
    DATA = data


def check_point(task):
    x, y, numerator, denominator, row_scale = task
    value = flint.fmpz_mat([[a + x * b + y * c for a, b, c in row] for row in DATA]).det()
    if value * denominator != numerator * row_scale:
        raise ArithmeticError(('shifted-grid determinant mismatch', x, y))
    return x, y


def lowest_multiplicity(a, b):
    weights = ((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))
    char = Counter()
    for d, mu in ((1,1),(2,-1),(3,-1),(6,1)):
        p = Counter({(0,0):1})
        for _ in range(6 // d):
            q = Counter()
            for (u,v), c in p.items():
                for i,j in weights:
                    q[u+i,v+j] += c
            p = q
        for (u,v),c in p.items():
            char[d*u,d*v] += mu*c
    assert all(c % 6 == 0 for c in char.values())
    char = {m:c//6 for m,c in char.items()}
    value = char.get((a,b),0)-char.get((a-1,b),0)-char.get((a,b-1),0)+char.get((a-2,b-1),0)+char.get((a-1,b-2),0)-char.get((a-2,b-2),0)
    return char[a,b], value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--workers', type=int, default=4)
    args = ap.parse_args()
    ab = str(args.a) + str(args.b)
    names = [f'frontier-20261028-level6-{ab}6-minor-{tag}-v1.json' for tag in ('baseline','seed1')]
    out = ROOT / f'frontier-20261028-level6-{ab}6-native-source-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    minors, pins = [], []
    for name in names:
        raw = (ROOT/name).read_bytes()
        minors.append(json.loads(raw))
        pins.append({'file':name,'sha256':hashlib.sha256(raw).hexdigest()})
    assert minors[0]['pencil_sha256'] == minors[1]['pencil_sha256']
    praw = (ROOT/minors[0]['pencil']).read_bytes()
    assert hashlib.sha256(praw).hexdigest() == minors[0]['pencil_sha256']
    P = json.loads(praw)
    degree = (args.a,args.b,6)
    assert P['degree'] == list(degree)
    source_words = P['source_words']
    assert tuple(source_words) == ind.lyndon_words(degree)
    basis = [ind.ind.standard_bracket(w) for w in source_words]
    assert all(v.get(w)==1 and min(v)==w for w,v in zip(source_words,basis))
    k = P['joint_horizontal_kernel_dim']
    weight_dimension, expected = lowest_multiplicity(args.a,args.b)
    assert len(basis) == weight_dimension and k == expected
    coefficients = P['horizontal_kernel_coefficients']
    assert len(coefficients) == k
    vectors = [ind.combine(basis,c) for c in coefficients]
    for v in vectors:
        for generator in ('f1','f2'):
            assert not ind.act(v,generator,6,6)
    aa = [ind.d3(v,degree,6,6) for v in vectors]
    bb = [ind.d3(v,degree,7,6) for v in vectors]
    cc = [ind.d3(v,degree,6,7) for v in vectors]
    target = sorted(set(w for p in aa+bb+cc for w in p))
    rows = {w:[[Q(aa[j].get(w,0)),Q(bb[j].get(w,0))-Q(aa[j].get(w,0)),Q(cc[j].get(w,0))-Q(aa[j].get(w,0))]
               for j in range(k)] for w in target}
    for w, row in zip(P['selected_target_words'],P['matrix']):
        assert rows[w] == [[Q(c) for c in e] for e in row]
    # A nonzero actual D3 minor proves the source combinations independent;
    # their membership and the independently computed dimension k then prove
    # they are the WHOLE source. No large coefficient-space RREF is needed.
    base = [[rows[w][j][0] for j in range(k)] for w in P['selected_target_words']]
    assert flint.fmpq_mat([[flint.fmpq(v.numerator,v.denominator) for v in row] for row in base]).det() != 0
    counts = []
    for M in minors:
        assert len(M['rows']) == k == len(set(M['rows']))
        matrix = [rows[w] for w in M['rows']]
        scales = [math.lcm(*(v.denominator for e in row for v in e)) for row in matrix]
        row_scale = math.prod(scales)
        data = [[[int(v*scale) for v in e] for e in row] for row,scale in zip(matrix,scales)]
        coefficients = {(e['x_power'],e['y_power']):Q(e['coefficient']) for e in M['coefficients']}
        assert len(coefficients) == len(M['coefficients']) and all(i+j<=k for i,j in coefficients)
        den = math.lcm(*(v.denominator for v in coefficients.values()))
        numerators = {mon:int(v*den) for mon,v in coefficients.items()}
        tasks = []
        for i in range(k+1):
            x = i-2
            xp = [x**u for u in range(k+1)]
            inner = [0]*(k+1)
            for (u,v),c in numerators.items():
                inner[v] += c*xp[u]
            for j in range(k+1-i):
                y = j+1
                z = 0
                for c in reversed(inner):
                    z = z*y+c
                tasks.append((x,y,z,den,row_scale))
        with Pool(args.workers,initializer=init,initargs=(data,)) as pool:
            checked = list(pool.imap_unordered(check_point,tasks,chunksize=16))
        assert len(checked) == len(tasks) == (k+1)*(k+2)//2
        counts.append(len(checked))
    result = {'degree':list(degree),'minor_inputs':pins,'pencil_sha256':hashlib.sha256(praw).hexdigest(),
              'Lyndon_source_count':len(basis),'lowest_character_multiplicity':expected,
              'independent_horizontal_vectors':k,'horizontal_actions_checked':2*k,
              'source_independence':'nonzero independently rebuilt exact D3 baseline minor',
              'independently_rebuilt_target_rows':len(target),'shifted_grid_minor_checks':counts,
              'status':'PASS_COMPLETE_SOURCE_AND_BOTH_STORED_MINOR_IDENTITIES',
              'shared_library':'FLINT exact determinant arithmetic; source and shifted-grid replay are separate code',
              'limits':'named Witt/finite-Levi/actual-source interfaces; no formal or independent-model acceptance'}
    with out.open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print('PASS complete source and both minors',degree,'lowest',k,'target rows',len(target),'grids',counts,out.name,flush=True)


if __name__=='__main__':
    main()
