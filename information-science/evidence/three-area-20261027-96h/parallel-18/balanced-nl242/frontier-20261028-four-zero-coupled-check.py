#!/opt/homebrew/bin/python3
"""Independent direct checks of the second formal four-zero placement."""
import argparse
import collections
import itertools
import json
import pathlib


def anf_degree(v,n):
    a=list(v)
    for i in range(n):
        for x in range(1<<n):
            if x&(1<<i):a[x]^=a[x^(1<<i)]
    return max((x.bit_count() for x,t in enumerate(a) if t),default=0)


def main():
    p=argparse.ArgumentParser();p.add_argument('--input',type=pathlib.Path,required=True)
    p.add_argument('--histogram',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    placed=json.loads(args.input.read_text(encoding='utf-8'));model=json.loads(args.histogram.read_text(encoding='utf-8'))
    k=placed['spectrum_k'];hist={int(t):v for t,v in model['histogram'].items()}
    assert len(k)==512 and {t:k.count(t) for t in range(-7,8)}=={t:hist[t]+(t==0) for t in range(-7,8)}
    assert k[0]==0 and sum(k)==128 and sum(x*x for x in k)==16384 and max(map(abs,k))==7
    assert all((k[a]&1)==(a>>8) for a in range(512))
    zeros=[a for a in range(512) if k[a]==0]; fours=[a for a in range(512) if abs(k[a])==4]
    assert zeros==[0,64,128,192] and len(fours)==140
    zx=fx=0
    for a in zeros:zx^=a
    for a in fours:fx^=a
    assert zx==fx==0
    # r=(k-t)/2 mod2 is a polynomial on the entire frequency space. Its
    # degree<=2 implies all third additive differences of k vanish mod4.
    r=[((k[a]-(a>>8))//2)%2 for a in range(512)]
    assert anf_degree(r,9)<=2
    oddq=[((k[256+x]-1)//2)%2 for x in range(256)]
    evenq=[(k[x]//2)%2 for x in range(256)]
    assert sum(oddq)==144 and sum(1-v for v in evenq)==144
    assert all(oddq[x]==(evenq[x]^1) for x in range(256))
    P=[int(abs(k[256+x]) in (1,7)) for x in range(256)]
    assert anf_degree(P,8)==3
    mask=sum(v<<x for x,v in enumerate(P));subspaces=flats=0
    for pivots in itertools.combinations(range(8),5):
        free=[c for c in range(8) if c not in pivots]
        slots=[(r,c) for c in free for r in range(5) if c>pivots[r]]
        for assignment in range(1<<len(slots)):
            basis=[1<<v for v in pivots]
            for j,(row,col) in enumerate(slots):
                if assignment>>j&1:basis[row]|=1<<col
            span=[0]
            for b in basis:span += [x^b for x in span]
            subspaces+=1
            for coset in range(8):
                origin=sum(1<<free[i] for i in range(3) if coset>>i&1)
                flat=sum(1<<(origin^v) for v in span)
                assert (flat&mask).bit_count()%2==0;flats+=1
    assert subspaces==97155 and flats==777240
    inverse=[sum(v*(-1 if (a&x).bit_count()%2 else 1) for a,v in enumerate(k)) for x in range(512)]
    bad=sum(abs(x)!=128 for x in inverse);assert bad==placed['inverse_nonsign_count'] and bad>0
    correlations=[sum(k[a]*k[a^b] for a in range(512)) for b in range(512)]
    assert correlations[0]==16384 and any(correlations[1:])
    changed=P.copy();changed[0]^=1;assert anf_degree(changed,8)>3
    result={'four_zeros':True,'magnitude16_count':140,'peak28_count':200,
            'both_frequency_xors_zero':True,'same_polar_quadratics':True,'global_mod4_quadratic':True,
            'odd_peakunit_degree':3,'all_affine5flat_parities_checked':flats,'rref_directions':subspaces,
            'direct_inverse_512x512':True,'inverse_nonsign_count':bad,'inverse_l1':sum(map(abs,inverse)),
            'nonzero_offorigin_autocorrelations':sum(x!=0 for x in correlations[1:]),
            'mutation_rejected':True,'actual_boolean_witness':False,
            'limits':'selected filters only; not full Walsh realizability'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('mod4_degree=',anf_degree(r,9),'flats=',flats,'inverse_nonsign=',bad,'L1=',result['inverse_l1'])


if __name__=='__main__':main()
