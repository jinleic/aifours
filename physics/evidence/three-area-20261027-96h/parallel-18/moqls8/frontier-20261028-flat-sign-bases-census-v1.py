#!/usr/bin/env python3
"""Exact exhaustive classification of real flat sign-ray ONBs in dimension 8.

Enumerates all64 even-parity rays and all8-cliques of their orthogonality
graph; not an enumeration of MOQLS families or a no-go certificate.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time


def raw7(a):
    return a | ((a.bit_count() % 2) << 6)


def orth(a,b):
    return (raw7(a)^raw7(b)).bit_count()==4


def walsh(a,u):
    z=0;mask=raw7(a)
    for x in range(8):
        signbit=0 if x==0 else ((mask>>(x-1))&1)
        z += -1 if signbit ^ ((u&x).bit_count()&1) else 1
    return z


def is_basis(cells):
    return len(cells)==8 and len(set(cells))==8 and all(orth(a,b) for a,b in itertools.combinations(cells,2))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    start=time.monotonic()
    neighbor=[{b for b in range(64) if b!=a and orth(a,b)} for a in range(64)]
    if set(map(len,neighbor))!={35}:raise ValueError('orthogonality degree mismatch')
    supports=[];light=heavy=0
    for a in range(64):
        W=[walsh(a,u) for u in range(8)]
        nz=[x for x in W if x]
        if len(nz)==1 and abs(nz[0])==8:light+=1
        elif len(nz)==4 and all(abs(x)==4 for x in nz):heavy+=1
        else:raise ValueError('unexpected exact Walsh profile')
        supports.append({u for u,v in enumerate(W) if v})
    bases=[]
    def extend(prefix,candidates):
        if len(prefix)==8:
            bases.append(tuple(prefix));return
        if len(prefix)+len(candidates)<8:return
        while candidates:
            v=candidates.pop()
            if len(prefix)+1+len(candidates)<8:break
            extend(prefix+[v],candidates & neighbor[v])
    extend([],set(range(64)))
    unique={tuple(sorted(B)) for B in bases}
    if len(unique)!=len(bases):raise ValueError('duplicate clique enumeration')
    if len(unique)!=240:raise ValueError('basis count differs from 240')
    anchor=[]
    heavy_per_basis=collections.Counter()
    for basis in unique:
        if not is_basis(basis):raise ValueError('emitted nonbasis')
        translated={x^basis[0] for x in basis}
        if len(translated)!=8 or any((x^y) not in translated for x in translated for y in translated):
            raise ValueError('basis is not affine F2^3 coset')
        anchor.append(tuple(sorted(translated)))
        count=sum(len(supports[x])==4 for x in basis)
        heavy_per_basis[count]+=1
        if count not in (0,4,6,7,8):raise ValueError('invalid heavy count')
        for axis in range(8):
            cover=sum(axis in supports[x] for x in basis if len(supports[x])==4)
            singles=sum(supports[x]=={axis} for x in basis)
            if 4*singles+cover!=4:raise ValueError('coordinate completeness failed')
    codes=set(anchor)
    if len(codes)!=30:raise ValueError('nonlinear basis subspace count differs from30')
    sample=list(next(iter(unique)))
    mutated=sample[:-1]+[sample[0]]
    if is_basis(mutated):raise ValueError('duplicate-ray negative control not rejected')
    report={'result':'PASS_COMPLETE_64_RAY_240_BASIS_CENSUS',
            'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
            'even_sign_rays':64,'orthogonality_graph_degree':35,
            'first_row_Walsh_light_rays':light,'four_support_heavy_rays':heavy,
            'all_orthonormal_bases_enumerated':len(unique),'underlying_binary_subspaces':len(codes),
            'heavy_entries_per_basis_histogram':{str(k):v for k,v in sorted(heavy_per_basis.items())},
            'all_basis_affine_xor_closure':True,'all_coordinate_completeness_checks':True,
            'duplicate_ray_negative_control_rejected':True,'seconds':time.monotonic()-start,
            'limits':'One fixed flat-real 8D ray alphabet; no family enumeration or global witness.'}
    with pathlib.Path(args.output).open('x',encoding='utf-8') as h:json.dump(report,h,indent=2);h.write('\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
