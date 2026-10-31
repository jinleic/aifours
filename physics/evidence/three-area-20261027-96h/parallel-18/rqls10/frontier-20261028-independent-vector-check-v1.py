#!/usr/bin/env python3
"""Direct numerical original-definition checker, independent of search scorer.

Input is a 10x100 complex array indexed as v[:,10*r+c]. Verification is
floating-point only. It cannot certify an exact witness.
"""
import argparse
import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('reference', HERE / 'frontier-20261028-rigidity-orbit-check-v1.py')
reference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reference)
N = 10


def check(v, label):
    if v.shape != (10, 100) or not np.isfinite(v).all():
        raise ValueError('expected finite 10x100 array')
    blocks = reference.block_list()
    max_norm_error = 0.0
    for x in range(N*N):
        value = float(abs(np.vdot(v[:,x],v[:,x])-1))
        max_norm_error = max(max_norm_error,value)
    worst = (0.0, None)
    for ib, block in enumerate(blocks):
        assert len(block) == N
        for i,(r,c) in enumerate(block):
            for s,d in block[i+1:]:
                value = float(abs(np.vdot(v[:,10*r+c],v[:,10*s+d])))
                if value > worst[0]:
                    worst = (value,(ib,(r,c),(s,d)))
    max_ray_overlap = 0.0
    worst_ray = None
    parallel_pairs = 0
    for x in range(N*N):
        for y in range(x+1,N*N):
            denom = np.linalg.norm(v[:,x])*np.linalg.norm(v[:,y])
            if denom == 0:
                raise ValueError('zero vector')
            overlap = float(abs(np.vdot(v[:,x],v[:,y])) / denom)
            if overlap > max_ray_overlap:
                max_ray_overlap,worst_ray = overlap,(x,y)
            if overlap >= 1-1e-8:
                parallel_pairs += 1
    print(label, 'max_norm_error', max_norm_error)
    print(label, 'max_required_offdiagonal_overlap', worst)
    print(label, 'max_normalized_distinct_pair_overlap', max_ray_overlap, 'pair', worst_ray)
    print(label, 'near_parallel_distinct_pairs_1e-8', parallel_pairs, 'of 4950')
    print(label, 'numerical_feasible_at_1e-10', max_norm_error<1e-10 and worst[0]<1e-10 and max_ray_overlap<1-1e-8)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('path',nargs='?')
    args=p.parse_args()
    if args.path:
        v=np.load(args.path,allow_pickle=False)
        check(v,args.path)
    else:
        v=np.zeros((N,N*N),dtype=complex)
        for r in range(N):
            for c in range(N):
                v[reference.color[r][c],N*r+c]=1
        check(v,'exact-classical-reference')


if __name__=='__main__':
    main()
