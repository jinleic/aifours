#!/usr/bin/env python3
"""Complete free lowest source by modular kernel + exact lift, DESCENDING Lyndon columns.

Columns: ALL standard-bracketed Lyndon words of root(a,b,7). Rows: the
coefficients of the f1/f2 images at ALL target Lyndon words; this restriction
is injective on Lie elements by Lyndon unitriangularity. The kernel RREF is
computed modulo several 62-bit primes, CRT/rationally reconstructed, then the
WHOLE result is verified exactly: every vector is f1/f2-lowest in integer
tensor coordinates, the RREF identity proves independence, and the kernel
dimension equals the exact Witt/Weyl lowest multiplicity (completeness).
"""
import argparse
import hashlib
import io
import json
import math
import sys
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint
import importlib.util

BASE='frontier-20261029-trace-invariant-canonical.py'
BASE_SHA='80ed94050a08dd39cc3878da2c4d2ee837aa3e1777f852a139db477702efd1fb'
WEIGHTS=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))


def load_base():
    raw=(ROOT/BASE).read_bytes();assert hashlib.sha256(raw).hexdigest()==BASE_SHA
    spec=importlib.util.spec_from_file_location('pinned_word_tools',ROOT/BASE)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def is_prime(n):
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0:return n==p
    d=n-1;s=0
    while d%2==0:d//=2;s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True


def code(word):
    v=0
    for x in word:v=8*v+x
    return v


def bracket(a,b):
    out=Counter()
    for u,x in a.items():
        for v,y in b.items():out[u+v]+=x*y;out[v+u]-=x*y
    return {w:c for w,c in out.items() if c}


def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))


@lru_cache(None)
def expansion(word):
    if len(word)==1:return {word:1}
    cut=next(i for i in range(1,len(word)) if lyndon(word[i:]))
    out=bracket(expansion(word[:cut]),expansion(word[cut:]))
    assert min(out)==word and out[word]==1
    return out


def root_words(a,b,n=7):
    out=[]
    def visit(prefix,left,x,y):
        if min(x,y)<0 or max(x,y)>2*left:return
        if left==0:
            if x==y==0:out.append(prefix)
            return
        for j,(dx,dy) in enumerate(WEIGHTS):visit(prefix+(j,),left-1,x-dx,y-dy)
    visit((),n,a,b)
    return sorted(out)


def counts(a,b):
    ch=Counter({(0,0):1})
    for _ in range(7):
        nxt=Counter()
        for (u,v),c in ch.items():
            for i,j in WEIGHTS:nxt[u+i,v+j]+=c
        ch=nxt
    def lie(x,y):
        if x<0 or y<0:return 0
        # Prime level7 Witt formula: (T7(x,y)-T1(x/7,y/7))/7, where T1 counts
        # level-one LETTERS of that weight (two letters have weight(1,1)).
        extra=sum(1 for w in WEIGHTS if x%7==0 and y%7==0 and w==(x//7,y//7))
        assert (ch[x,y]-extra)%7==0
        return (ch[x,y]-extra)//7
    low=lie(a,b)-lie(a-1,b)-lie(a,b-1)+lie(a-2,b-1)+lie(a-1,b-2)-lie(a-2,b-2)
    return lie(a,b),lie(a-1,b),lie(a,b-1),low


def ratrec(x,m):
    # Wang rational reconstruction with |num|,den <= sqrt(m/2)
    bound=math.isqrt(m//2)
    r0,r1=m,x%m;s0,s1=0,1
    while r1>bound:
        q=r0//r1;r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1
    if s1==0 or abs(s1)>bound:return None
    if s1<0:r1,s1=-r1,-s1
    if math.gcd(r1,s1)!=1:return None
    return Q(r1,s1)


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--max-primes',type=int,default=8)
    args=ap.parse_args();a,b=args.a,args.b
    stem=f'frontier-20261029-level7-{a}{b}-modular-lowest-source-reverse'
    outs=[ROOT/f'{stem}-words-v1.npy',ROOT/f'{stem}-vectors-v1.npy',ROOT/f'{stem}-v1.json']
    if any(p.exists() for p in outs):raise FileExistsError(stem)
    T=load_base();local=T.local
    N,N1,N2,k=counts(a,b)
    words=root_words(a,b);lyn=[w for w in words if lyndon(w)][::-1];assert len(lyn)==N
    targets={}
    for g,(x,y) in (('f1',(a-1,b)),('f2',(a,b-1))):
        tl=[w for w in root_words(x,y) if lyndon(w)];targets[g]={w:i for i,w in enumerate(tl)}
    assert len(targets['f1'])==N1 and len(targets['f2'])==N2
    action={g:[{int(t):int(c) for t,c in row.items()} for row in local.ACTION[g]] for g in ('f1','f2')}
    entries=[]
    for j,w in enumerate(lyn):
        P=expansion(w)
        for gi,g in enumerate(('f1','f2')):
            img=Counter()
            for word,c in P.items():
                for pos,letter in enumerate(word):
                    for new,d in action[g][letter].items():
                        img[word[:pos]+(new,)+word[pos+1:]]+=c*d
            offset=0 if g=='f1' else N1
            for word,c in img.items():
                if c and word in targets[g]:entries.append((offset+targets[g][word],j,c))
    R=N1+N2
    print('ROOT',(a,b,7),'Lie',N,'rows',R,'entries',len(entries),'lowest',k,flush=True)
    primes=[];candidate=(1<<62)-1;residue_rows=None;modulus=1;pivots=None;solution=None
    while len(primes)<args.max_primes:
        while not is_prime(candidate):candidate-=2
        p=candidate;candidate-=2
        M=flint.nmod_mat(R,N,p)
        for i,j,c in entries:M[i,j]=(int(M[i,j])+c)%p
        X,nullity=M.nullspace();assert nullity==k,'kernel dimension mismatch modulo p'
        K=flint.nmod_mat(k,N,[int(X[j,i]) for i in range(k) for j in range(N)],p)
        Rr,rank=K.rref();assert rank==k
        piv=[next(j for j in range(N) if int(Rr[i,j])) for i in range(k)]
        rows=[[int(Rr[i,j]) for j in range(N)] for i in range(k)]
        if pivots is None:pivots=piv;residue_rows=rows;modulus=p
        else:
            assert piv==pivots,'unlucky prime pivot profile'
            inv=pow(modulus%p,-1,p)
            residue_rows=[[x+((y-x)*inv%p)*modulus for x,y in zip(rx,ry)] for rx,ry in zip(residue_rows,rows)]
            modulus*=p
        primes.append(p)
        print('PRIME',len(primes),'kernel',k,flush=True)
        candidate_rows=[]
        for row in residue_rows:
            den=1;out=[]
            for x in row:
                y=(x*den)%modulus
                if y>modulus//2:y-=modulus
                if abs(y)<=math.isqrt(modulus//2):out.append(Q(y,den));continue
                q=ratrec(x,modulus)
                if q is None:break
                den=math.lcm(den,q.denominator);out.append(q)
            else:
                candidate_rows.append(out);continue
            break
        if len(candidate_rows)!=k:continue
        integer=[]
        for row in candidate_rows:
            den=math.lcm(*(q.denominator for q in row));integer.append([int(q*den) for q in row])
        codes=np.array([code(w) for w in words],dtype=np.uint32);index={w:i for i,w in enumerate(words)}
        V=np.zeros((k,len(words)),dtype=np.int64);ok=True
        for i,row in enumerate(integer):
            vec=Counter()
            for j,c in enumerate(row):
                if c:
                    for word,d in expansion(lyn[j]).items():vec[word]+=c*d
            if any(abs(v)>=2**62 for v in vec.values()):ok=False;break
            for word,c in vec.items():V[i,index[word]]=c
        if not ok:continue
        space=T.Words(7)
        assert np.array_equal(space.root(a,b)[0],codes)
        _,F1=space.action((a,b),'f1');_,F2=space.action((a,b),'f2')
        if all(not np.any(F1.apply(v)) and not np.any(F2.apply(v)) for v in V):
            solution=(integer,V,codes);break
        print('exact verification failed; adding prime',flush=True)
    assert solution is not None,'no verified exact lift'
    integer,V,codes=solution
    detectors=[int(np.searchsorted(codes,code(lyn[j]))) for j in pivots]
    minor=flint.fmpz_mat(V[:,detectors].T.tolist());assert minor.det()
    files=[]
    for path,data in zip(outs[:2],(codes,V)):
        with path.open('xb') as stream:np.save(stream,data,allow_pickle=False)
        raw=path.read_bytes();files.append({'file':path.name,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    record={'owner':'MathKacMoody-2','degree':[a,b,7],'entire_lowest_dimension':k,'free_Lie_dimension':N,
            'target_Lie_dimensions':[N1,N2],'whole_tensor_word_count':len(words),'files':files,
            'lyndon_pivot_words':[''.join(map(str,lyn[j])) for j in pivots],
            'integer_lyndon_coefficients_max_bits':max(abs(c).bit_length() for row in integer for c in row),
            'coefficient_detector_indices':detectors,'primes_used':[str(p) for p in primes],
            'exact_verification':'every integer tensor vector checked killed by BOTH actual finite-Levi lowerings (signed-int64 bounded word arithmetic); RREF identity on pivot Lyndon coordinates gives independence; k equals exact Witt/Weyl lowest multiplicity, hence completeness',
            'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_word_tools':{'file':BASE,'sha256':BASE_SHA},
            'numpy_version':np.__version__,'flint_version':flint.__version__,
            'status':'COMPLETE_EXACT_FREE_LOWEST_SOURCE_CANDIDATE',
            'limits':'Free-source only. Shared FLINT/NumPy. Alternate reconstruction, canonical pencil, determinant and actual quotient work are separate obligations. No parent/formal/configured-family/human/novelty acceptance.'}
    with outs[2].open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('WROTE',outs[2].name,'dimension',k,'primes',len(primes),flush=True)


if __name__=='__main__':main()
