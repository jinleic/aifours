#!/opt/homebrew/bin/python3
"""Finite controls for the rank-six weight-eight simplex argument."""
import argparse
import collections
import itertools
import json
import pathlib


def B(a,b):
    return sum((((a>>(2*i))&1)*((b>>(2*i+1))&1)) ^
               (((a>>(2*i+1))&1)*((b>>(2*i))&1)) for i in range(3))%2


def rank(rows):
    piv={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)


def subspaces(n,d):
    for pivots in itertools.combinations(range(n),d):
        free=[x for x in range(n) if x not in pivots]
        slots=[(r,c) for c in free for r in range(d) if c>pivots[r]]
        for assignment in range(1<<len(slots)):
            basis=[1<<x for x in pivots]
            for j,(r,c) in enumerate(slots):
                if assignment>>j&1:basis[r]|=1<<c
            span=[0]
            for v in basis:span += [x^v for x in span]
            yield basis,frozenset(span),free


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    S={0,1,2,7,11,31,47,63};assert len(S)==8
    vectors=sorted(S-{0});assert all(B(a,b)==1 for a,b in itertools.combinations(vectors,2))
    assert rank(vectors)==6
    xor=0
    for x in S:xor^=x
    assert xor==0
    anf=[int(x in S) for x in range(64)]
    for i in range(6):
        for x in range(64):
            if x>>i&1:anf[x]^=anf[x^(1<<i)]
    assert max(x.bit_count() for x,v in enumerate(anf) if v)==4
    assert [x for x,v in enumerate(anf) if v and x.bit_count()==4]==[15,51,60]
    planes=[];patterns=collections.Counter();vector_inc=collections.Counter()
    for basis,space,free in subspaces(6,4):
        gram=[sum(B(a,b)<<j for j,b in enumerate(basis)) for a in basis]
        if rank(gram)!=4:continue
        planes.append(space)
        for v in space-{0}:vector_inc[v]+=1
        counts=[]
        for c in range(4):
            origin=sum(1<<free[j] for j in range(2) if c>>j&1)
            counts.append(sum((origin^v) in S for v in space))
        assert all(c%2==1 for c in counts)
        patterns[tuple(sorted(counts))]+=1
    assert len(planes)==336 and set(vector_inc.values())=={80} and len(vector_inc)==63
    assert patterns=={(1,1,3,3):280,(1,1,1,5):56}
    pair_incidence=sum(sum(1 for a,b in itertools.combinations(S,2) if a^b in L) for L in planes)
    triple_incidence=sum(sum(1 for a,b,c in itertools.combinations(S,3) if a^b in L and a^c in L) for L in planes)
    assert pair_incidence==2240 and triple_incidence==1120
    classes=collections.Counter()
    for basis,D,_ in subspaces(6,2):
        typ='nondegenerate' if B(*basis) else 'isotropic'
        containing=sum(D<=L for L in planes)
        assert containing==(20 if typ=='nondegenerate' else 16)
        classes[typ]+=1
    assert classes=={'nondegenerate':336,'isotropic':315}
    for linear in range(64):
        for c in range(2):
            def Q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2 ^ ((linear&x).bit_count()%2) ^ c
            assert sum(Q(x) for x in S)%2==1
    result={'simplex_vertices':sorted(S),'gram_rank':6,'support_xor':xor,'anf_quartic_terms':[15,51,60],
            'nondegenerate_four_subspaces':336,'incidence_per_nonzero_vector':80,
            'coset_patterns':{'1,1,3,3':280,'1,1,1,5':56},'pair_incidence':2240,'triple_incidence':1120,
            'two_plane_counts':dict(classes),'nondegenerate_extension_counts':{'nondegenerate':20,'isotropic':16},
            'same_polar_quadratic_shifts_checked':128,'simplex_Q_weight_always_odd':True,
            'note':'one explicit control and full finite incidence counts; written proof remains necessary'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('symplectic_4planes=336 simplex_patterns=',dict(patterns),'Q shifts=128',flush=True)


if __name__=='__main__':main()
