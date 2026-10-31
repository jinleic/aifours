#!/opt/homebrew/bin/python3
"""Small complete checks of shared-polar-form quadratic weight constraints."""
import argparse
import collections
import itertools
import json
import pathlib


def rank(rows):
    piv={}
    for row in rows:
        v=row
        while v:
            b=v.bit_length()-1
            if b in piv:v^=piv[b]
            else:piv[b]=v;break
    return len(piv)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    summaries={}
    for n in (4,5):
        terms=[(i,) for i in range(n)]+list(itertools.combinations(range(n),2))
        masks=[sum(1<<x for x in range(1<<n) if all(x>>i&1 for i in term)) for term in terms]
        allones=(1<<(1<<n))-1
        affine=[]
        for v in range(1<<(n+1)):
            m=allones if v>>n&1 else 0
            for i in range(n):
                if v>>i&1:m^=masks[i]
            affine.append(m)
        q=0;oldgray=0;tested=0;pairs=collections.Counter()
        for index in range(1<<len(terms)):
            gray=index^(index>>1)
            if index:
                changed=gray^oldgray;q^=masks[changed.bit_length()-1]
            oldgray=gray
            rows=[0]*n
            for j,(u,v) in enumerate(itertools.combinations(range(n),2),start=n):
                if gray>>j&1:rows[u]|=1<<v;rows[v]|=1<<u
            r=rank(rows);assert r%2==0
            z=(1<<n)-q.bit_count()
            for shift in affine:
                ones=(q^shift).bit_count();imbalance=abs((1<<n)-2*ones)
                assert imbalance in (0,1<<(n-r//2))
                if r==n:assert imbalance!=0
                pairs[(z,ones)]+=1;tested+=1
        summaries[str(n)]={'zero_constant_quadratics':1<<len(terms),'affine_shifts_each':len(affine),
                           'quadratic_pairs':tested,'distinct_weight_pairs':len(pairs)}
    # Explicit 8-variable rank-6 pair from the second placed relaxation.
    def q(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))%2
    assert sum(q(x)==0 for x in range(256))==144
    assert sum((q(x)^1)==1 for x in range(256))==144
    receipt={'dimensions_4_and_5_exhausted':summaries,'rank_even_all':True,
             'quadratic_weight_formula_all':True,'full_rank_never_balanced':True,
             'explicit_dimension8_qzero_Qone_pair':[144,144],
             'note':'finite controls, not a substitute for the all-dimensional written proof'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('quadratic_pairs_n4=',summaries['4']['quadratic_pairs'],'n5=',summaries['5']['quadratic_pairs'],flush=True)


if __name__=='__main__':main()
