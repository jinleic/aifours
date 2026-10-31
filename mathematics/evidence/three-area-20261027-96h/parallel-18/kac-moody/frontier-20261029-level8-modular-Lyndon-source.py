#!/usr/bin/env python3
"""New complete grade8 source representation after a bounded direct run.

Kernel proposal: modular RREF on coefficients at ALL target Lyndon words.
Exact certificate: clear each lifted row denominator and check BOTH entire
word-coordinate action matrices times that integer basis equal zero. RREF
pivot identities give independence; the grade8 Witt/Weyl count gives the
entire source dimension. No mere modular rank is an accepted source proof.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MODTOOLS='frontier-20261029-level7-modular-lowest-source.py'
MODTOOLS_SHA='9b751a7e12b0e67bef0b63071fc08028449423ad1029eff143f89cc9522c80a1'
CANONICAL='frontier-20261029-level6-canonical-contraction.py'
CANONICAL_SHA='0b0cb4438aa7787ebc974452db769c86caf37344bfe390f6100b61395097a6d8'
GRADE=8


def load(name,file,sha):
    raw=(ROOT/file).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha,file
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def dimensions(weights,a,b):
    counts=[Counter({(0,0):1})]
    for n in range(1,9):
        following=Counter()
        for (x,y),c in counts[-1].items():
            for dx,dy in weights:following[x+dx,y+dy]+=c
        counts.append(following)
    def lie(x,y):
        if min(x,y)<0:return 0
        c=counts[8][x,y]-(counts[4][x//2,y//2] if x%2==y%2==0 else 0)
        assert c%8==0;return c//8
    return lie(a,b),lie(a,b)-lie(a-1,b)-lie(a,b-1)+lie(a-2,b-1)+lie(a-1,b-2)-lie(a-2,b-2)


def main():
    if not __debug__:raise RuntimeError('assertions disabled')
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    ap.add_argument('--max-primes',type=int,default=8);args=ap.parse_args();a,b=args.a,args.b
    out=ROOT/f'frontier-20261029-level8-{a}{b}-modular-Lyndon-source-v1.json'
    if out.exists():raise FileExistsError(out)
    M=load('frozen_modular_kernel_tools',MODTOOLS,MODTOOLS_SHA)
    C=load('whole_integer_finite_actions',CANONICAL,CANONICAL_SHA);F=C.flint
    N,k=dimensions(M.WEIGHTS,a,b);assert 0<k<=300 and N<=1200
    words=[w for w in M.root_words(a,b,n=GRADE) if M.lyndon(w)]
    assert len(words)==N
    target_sets={}
    for g,(x,y) in (('f1',(a-1,b)),('f2',(a,b-1))):
        target_sets[g]=set(w for w in M.root_words(x,y,n=GRADE) if M.lyndon(w))
    all_images=[];all_labels=set();restricted_labels=set()
    for word in words:
        expansion=M.expansion(word)
        col={}
        for g in ('f1','f2'):
            full=C.action2(expansion,g)
            col.update({(g,w):int(c) for w,c in full.items() if c})
        all_images.append(col);all_labels.update(col)
        restricted_labels.update((g,w) for g,w in col if w in target_sets[g])
    labels=sorted(all_labels);small=sorted(restricted_labels)
    label_index={w:i for i,w in enumerate(labels)};small_index={w:i for i,w in enumerate(small)}
    full=F.fmpz_mat(len(labels),N)
    for j,col in enumerate(all_images):
        for w,c in col.items():full[label_index[w],j]=c
    print('NEW MODULAR SOURCE',(a,b,8),'whole Lie',N,'lowest',k,'full word rows',len(labels),'Lyndon detector rows',len(small),flush=True)
    primes=[];candidate=(1<<62)-1;acc=None;modulus=1;pivots=None;solution=None
    while len(primes)<args.max_primes:
        while not M.is_prime(candidate):candidate-=2
        p=candidate;candidate-=2
        assert F.fmpz(p).is_prime(),'source modulus not prime under exact FLINT primality API'
        action=F.nmod_mat(len(small),N,p)
        for j,col in enumerate(all_images):
            for w,c in col.items():
                if w in small_index:action[small_index[w],j]=c%p
        nullspace,nullity=action.nullspace();assert nullity==k
        rows=F.nmod_mat(k,N,[int(nullspace[j,i]) for i in range(k) for j in range(N)],p)
        reduced,rank=rows.rref();assert rank==k
        pivot=[next(j for j in range(N) if int(reduced[i,j])) for i in range(k)]
        residues=[[int(reduced[i,j]) for j in range(N)] for i in range(k)]
        if pivots is None:pivots=pivot;acc=residues;modulus=p
        else:
            assert pivot==pivots,'prime pivot profile changed'
            inverse=pow(modulus%p,-1,p)
            acc=[[x+((y-x)*inverse%p)*modulus for x,y in zip(rx,ry)] for rx,ry in zip(acc,residues)];modulus*=p
        primes.append(p);proposed=[]
        for row in acc:
            denominator=1;co=[]
            for x in row:
                z=(x*denominator)%modulus
                if z>modulus//2:z-=modulus
                if abs(z)<=math.isqrt(modulus//2):co.append(Q(z,denominator));continue
                rational=M.ratrec(x,modulus)
                if rational is None:break
                denominator=math.lcm(denominator,rational.denominator);co.append(rational)
            else:proposed.append(co);continue
            break
        if len(proposed)!=k:continue
        assert all(co[j]==int(i==q) for i,co in enumerate(proposed) for q,j in enumerate(pivots))
        denominators=[math.lcm(*(c.denominator for c in row)) for row in proposed]
        integer=F.fmpz_mat(N,k,[int(proposed[i][j]*denominators[i]) for j in range(N) for i in range(k)])
        if full*integer==F.fmpz_mat(len(labels),k):solution=proposed;break
        print('Exact whole-word lift not yet verified; adding a prime',len(primes),flush=True)
    assert solution is not None,'no exact complete source lift returned'
    rows=[{str(j):str(c) for j,c in enumerate(co) if c} for co in solution]
    matrix_digest=hashlib.sha256(json.dumps([[[g,''.join(map(str,w))],j,str(c)] for j,col in enumerate(all_images) for (g,w),c in sorted(col.items())],separators=(',',':')).encode()).hexdigest()
    record={'owner':'MathKacMoody-2','degree':[a,b,8],'complete_free_weight_dimension':N,'entire_lowest_dimension':k,
        'source_words':[''.join(map(str,w)) for w in words],'source_coefficients':rows,'detector_Lyndon_indices':pivots,
        'full_word_action_row_count':len(labels),'restricted_Lyndon_action_row_count':len(small),
        'whole_action_matrix_sparse_sha256':matrix_digest,'all_full_word_F1_F2_integer_products_zero':True,
        'RREF_identity_on_all_pivot_coordinates':True,'grade8_Witt_Weyl_count':k,'primes_used':[str(p) for p in primes],
        'exact_modulus_primality_API_checks':True,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'libraries':[{'file':MODTOOLS,'sha256':MODTOOLS_SHA},{'file':CANONICAL,'sha256':CANONICAL_SHA}],
        'status':'COMPLETE_EXACT_GRADE8_MODULAR_LYNDON_SOURCE',
        'limits':'Modular arithmetic only proposes the source; membership/independence/completeness have exact integer/classical certificates. Shared FLINT and finite actions. Actual-source/seed/PBW and D3 consequences still UNREVIEWED; no f173 transfer, scientific parent/formal/kernel/configured-family/human/native-library/novelty adoption.'}
    with out.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('PASS NEW complete exact modular source',(a,b,8),'dimension',k,'primes',len(primes),out.name,flush=True)


if __name__=='__main__':main()
