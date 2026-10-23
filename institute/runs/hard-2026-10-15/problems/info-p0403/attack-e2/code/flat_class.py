"""Enumerate the entire 16-free-point coordinate subcube for each seed.

This is not a group-invariant symmetry class. All 2^16 assignments on a
specified affine four-flat are enumerated, with all 512 linear output
shifts accounted for by Walsh zeros. Reduces the spectrum computation
to 16-point transforms; an independent checker uses full 512-point
transforms of every table instead.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import numpy as np
from seeds import SEEDS,decode,fwht


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def produce(name,hx,r4,compare):
    f=np.array(decode(hx),dtype=np.int16)
    W=np.array(fwht(f),dtype=np.int16)
    core=sorted({x for points in r4['seeds'][name]['four_sets_preserving_bound'] for x in points})
    origin=core[0]
    V={0}
    basis=[]
    for x in core:
        v=x^origin
        if v not in V:
            basis.append(v)
            V|={u^v for u in list(V)}
    assert len(basis)==4 and len(V)==16
    points=[]
    for t in range(16):
        x=origin
        for i,v in enumerate(basis):
            if (t>>i)&1: x^=v
        points.append(x)
    old=1-2*f[points]
    Uold=np.array(fwht(f[points]),dtype=np.int16)
    cosets=[[] for _ in range(16)]
    for a in range(512):
        h=sum((1<<i) for i,v in enumerate(basis) if bin(a&v).count('1')%2)
        sign=1-2*(bin(a&origin).count('1')%2)
        cosets[h].append(sign*int(W[a])-int(Uold[h]))
    assert all(len(c)==32 for c in cosets)
    flipmasks=np.arange(65536,dtype=np.int32)
    signs=old[None,:]*(1-2*((flipmasks[:,None]>>np.arange(16))&1)).astype(np.int16)
    U=signs.copy()
    k=1
    while k<16:
        view=U.reshape(-1,16//(2*k),2*k)
        a=view[:,:,:k].copy()
        b=view[:,:,k:].copy()
        view[:,:,:k]=a+b
        view[:,:,k:]=a-b
        k*=2
    maxima=np.zeros(65536,dtype=np.int16)
    zeros=np.zeros(65536,dtype=np.int16)
    for h,offsets in enumerate(cosets):
        extrema=np.maximum(abs(U[:,h]+min(offsets)),abs(U[:,h]+max(offsets)))
        maxima=np.maximum(maxima,extrema)
        count=Counter(offsets)
        for offset,multiplicity in count.items():
            zeros+=(U[:,h]==-offset).astype(np.int16)*multiplicity
    balanced=(zeros>0)
    bestM=int(min(maxima[balanced]))
    mask=int(np.flatnonzero(balanced&(maxima==bestM))[0])
    unbalanced242=int(np.count_nonzero(maxima<=28))
    assert not np.any((maxima<=28)&balanced)
    binary=np.column_stack((maxima,zeros)).astype('<i2').tobytes()
    binpath=Path('results/%s-flat-outcomes.bin'%name)
    if compare: assert binpath.read_bytes()==binary
    else: binpath.write_bytes(binary)
    h=f.copy()
    for j,x in enumerate(points):
        if (mask>>j)&1: h[x]^=1
    wh=fwht(h)
    shift=wh.index(0)
    g=[int(h[x])^(bin(shift&x).count('1')%2) for x in range(512)]
    wg=fwht(g)
    txt=''.join(map(str,g))
    wit={'bits':txt,'bit_order':'bits[x]=f(x), x=0..511; x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':sum(g),'walsh':wg,'nonlinearity':256-max(map(abs,wg))//2,'seed':name,'free_points_in_flip_mask_bit_order':points,'flip_mask':mask,'linear_shift':shift,'scope':'attainer for the restricted 16-free-point class only'}
    witpath=Path('results/%s-flat-attainer.json'%name)
    if compare: assert json.loads(witpath.read_text())==wit
    else: witpath.write_text(json.dumps(wit,indent=2)+'\n')
    return {'seed_hex':hx,'core_from_all_radius_four_survivors':core,'affine_origin':origin,'basis':basis,'free_points_in_flip_mask_bit_order':points,'free_points_sorted':sorted(points),'patterns_exhausted':65536,'outcomes_file':str(binpath),'outcomes_format':'65536 rows in increasing flip-mask order; each row [max_abs_W,number_of_zero_W], little-endian signed int16','outcomes_sha256':hashlib.sha256(binary).hexdigest(),'patterns_with_zero':int(np.count_nonzero(balanced)),'linear_output_shifts_yielding_balance':int(zeros.sum()),'patterns_preserving_max_abs_W_at_most_28':unbalanced242,'patterns_preserving_28_and_having_zero':int(np.count_nonzero((maxima<=28)&balanced)),'exact_maximum_balanced_nonlinearity_with_linear_output_shift':256-bestM//2,'best_balanced_max_abs_W':bestM,'attainer':str(witpath),'attainer_flip_mask':mask,'attainer_linear_shift':shift}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--compare',action='store_true')
    args=p.parse_args()
    r4=json.loads(Path('results/radius4.json').read_text())
    out={'scope':'For each seed g, arbitrary flips on its specified 16-point affine four-flat, then any linear output shift; not arbitrary Boolean functions.','seeds':{}}
    for name,hx in SEEDS.items():
        rec=produce(name,hx,r4,args.compare)
        out['seeds'][name]=rec
        print(name,'exhausted',rec['patterns_exhausted'],'max balanced NL',rec['exact_maximum_balanced_nonlinearity_with_linear_output_shift'],'242 patterns',rec['patterns_preserving_max_abs_W_at_most_28'],'242 with zero',rec['patterns_preserving_28_and_having_zero'],flush=True)
    path=Path('results/flat-class.json')
    if args.compare: assert json.loads(path.read_text())==out
    else: path.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__': main()
