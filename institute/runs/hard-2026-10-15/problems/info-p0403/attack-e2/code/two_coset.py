"""Exact meet-in-the-middle search of 32 free sites in two parallel cosets.

Two cosets of a fixed four-dimensional V form an affine five-flat. Each
half has 16 unconstrained signs; catalogue all 65536 half spectra, then
intersect complete bitsets of all 65536 possible other halves. Covers
all 2^32 assignments exactly, with no random sampling.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path
import time
import numpy as np
from seeds import SEEDS,decode,fwht


def catalog():
    masks=np.arange(65536,dtype=np.int32)
    C=(1-2*((masks[:,None]>>np.arange(16))&1)).astype(np.int16)
    size=1
    while size<16:
        v=C.reshape(65536,-1,2*size)
        a=v[:,:,:size].copy(); b=v[:,:,size:].copy()
        v[:,:,:size]=a+b; v[:,:,size:]=a-b
        size*=2
    indices=((C+16)//2).astype(np.int8)
    eq=[]
    for h in range(16):
        eq.append([int.from_bytes(np.packbits(C[:,h]==v,bitorder='little').tobytes(),'little') for v in range(-16,17,2)])
    return C,indices,eq


def setup(name):
    f=np.array(decode(SEEDS[name]),dtype=np.int16)
    W=np.array(fwht(f),dtype=np.int16)
    record=json.loads(Path('results/flat-class.json').read_text())['seeds'][name]
    basis=record['basis']
    V=[]
    for t in range(16):
        x=0
        for i,b in enumerate(basis):
            if (t>>i)&1: x^=b
        V.append(x)
    reps=sorted({min(x^v for v in V) for x in range(512)})
    assert len(reps)==32
    core_rep=min(record['affine_origin']^v for v in V)
    dual=[sum((1<<i) for i,b in enumerate(basis) if bin(a&b).count('1')%2) for a in range(512)]
    return f,W,basis,V,reps,core_rep,dual


def solve_pair(f,W,V,dual,p,q,C,indices,eq,bound=28):
    oldA=np.array(fwht(f[[p^v for v in V]]),dtype=np.int16)
    oldB=np.array(fwht(f[[q^v for v in V]]),dtype=np.int16)
    offsets=[[[] for _ in range(2)] for _ in range(16)]
    for a in range(512):
        h=dual[a]
        d=bin(a&(p^q)).count('1')%2
        sign=1-2*(bin(a&p).count('1')%2)
        offsets[h][d].append(sign*int(W[a])-int(oldA[h])-(1-2*d)*int(oldB[h]))
    assert all(len(offsets[h][d])==16 for h in range(16) for d in range(2))
    allowed=[]
    zeromasks=[]
    alive=np.ones(65536,dtype=bool)
    for h in range(16):
        L0=-bound-min(offsets[h][0]); R0=bound-max(offsets[h][0])
        L1=-bound-min(offsets[h][1]); R1=bound-max(offsets[h][1])
        allowrow=[]; zerorow=[]
        for A in range(-16,17,2):
            low=max(-16,L0-A,A-R1)
            high=min(16,R0-A,A-L1)
            mask=0
            for B in range(-16,17,2):
                if low<=B<=high: mask|=eq[h][(B+16)//2]
            zmask=0
            values={-c-A for c in offsets[h][0]}|{A+c for c in offsets[h][1]}
            for B in values:
                if -16<=B<=16 and B%2==0: zmask|=eq[h][(B+16)//2]
            allowrow.append(mask); zerorow.append(zmask)
        allowed.append(allowrow); zeromasks.append(zerorow)
        alive &= np.array([bool(x) for x in allowrow],dtype=bool)[indices[:,h]]
    order=sorted(range(16),key=lambda h:sum(x.bit_length() for x in allowed[h]))
    legal_count=0
    balanced_count=0
    first=None
    alive_indices=np.flatnonzero(alive)
    outcome=hashlib.sha256()
    for i in alive_indices.tolist():
        mask=(1<<65536)-1
        for h in order:
            mask &= allowed[h][int(indices[i,h])]
            if not mask: break
        if mask:
            count=bin(mask).count('1')
            legal_count+=count
            z=0
            for h in range(16): z|=zeromasks[h][int(indices[i,h])]
            balanced=mask&z
            balanced_count+=bin(balanced).count('1')
            outcome.update(i.to_bytes(4,'little'))
            outcome.update(mask.to_bytes(8192,'little'))
            if balanced and first is None:
                first=(i,(balanced&-balanced).bit_length()-1)
    return {'coset_representatives':[p,q],'half_patterns_catalogued':65536,'full_assignments_covered':2**32,'first_half_patterns_after_individual_filters':len(alive_indices),'assignments_preserving_bound':legal_count,'assignments_preserving_bound_and_giving_a_zero':balanced_count,'legal_second_half_bitsets_sha256':outcome.hexdigest(),'first_target_pair':first}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seed',choices=SEEDS,default='dsbf40')
    parser.add_argument('--pairs',choices=('core','all'),default='core')
    parser.add_argument('--limit',type=int)
    parser.add_argument('--output',required=True)
    parser.add_argument('--compare',action='store_true')
    args=parser.parse_args()
    C,indices,eq=catalog()
    f,W,basis,V,reps,core_rep,dual=setup(args.seed)
    pairs=[(p,q) for p,q in combinations(reps,2) if args.pairs=='all' or core_rep in (p,q)]
    if args.limit: pairs=pairs[:args.limit]
    out={'seed':args.seed,'seed_hex':SEEDS[args.seed],'basis':basis,'ordered_linear_four_flat':V,'coset_representatives':reps,'core_coset_representative':core_rep,'pair_selection':args.pairs,'bound':28,'half_spectrum_catalogue_sha256':hashlib.sha256(C.astype('<i2').tobytes()).hexdigest(),'scope':'all assignments on each explicitly listed pair of V-cosets; all linear output shifts; restricted class only','cases':[]}
    start=time.monotonic()
    for number,(p,q) in enumerate(pairs,1):
        rec=solve_pair(f,W,V,dual,p,q,C,indices,eq)
        out['cases'].append(rec)
        if not args.compare: Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
        print(args.seed,number,'of',len(pairs),p,q,'A',rec['first_half_patterns_after_individual_filters'],'legal',rec['assignments_preserving_bound'],'zero-bearing',rec['assignments_preserving_bound_and_giving_a_zero'],'seconds',round(time.monotonic()-start,3),flush=True)
        if rec['first_target_pair'] is not None:
            A,B=rec['first_target_pair']
            h=f.copy()
            for j,v in enumerate(V):
                h[p^v]=(A>>j)&1
                h[q^v]=(B>>j)&1
            wh=fwht(h)
            shift=wh.index(0)
            bits=[int(h[x])^(bin(shift&x).count('1')%2) for x in range(512)]
            txt=''.join(map(str,bits))
            witness={'bits':txt,'bit_order':'bits[x]=f(x), x=0..511, x_i=(x>>i)&1','sha256_ascii_bits':hashlib.sha256(txt.encode()).hexdigest(),'weight':sum(bits),'walsh':fwht(bits),'nonlinearity':256-max(map(abs,fwht(bits)))//2,'class_case':rec}
            Path('results/two-coset-target.json').write_text(json.dumps(witness,indent=2)+'\n')
            print('TARGET FOUND; requires independent full direct check',flush=True)
            break
    if args.compare: assert json.loads(Path(args.output).read_text())==out
    print('Completed',len(out['cases']),'cases; seconds',round(time.monotonic()-start,3),flush=True)


if __name__=='__main__': main()
