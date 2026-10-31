#!/opt/homebrew/bin/python3
"""Finite controls for the even-half quadratic and the four-zero obstruction."""
import argparse
import collections
import itertools
import json
import pathlib


def quadratic_truth(n,coeff):
    terms=[(i,) for i in range(n)]+list(itertools.combinations(range(n),2))
    bits=0
    for x in range(1<<n):
        value=0
        for j,term in enumerate(terms):
            if coeff>>j&1 and all((x>>i)&1 for i in term): value^=1
        bits|=value<<x
    return bits


def check_truth_case(bits):
    n=512; support=[i for i in range(n) if bits[i]]
    assert len(support)==256
    T=0
    for x in support: T^=x
    kernel=[a for a in range(n) if (a&T).bit_count()%2==0]
    pivots={}; basis=[]
    for a in kernel:
        v=a
        while v:
            p=v.bit_length()-1
            if p in pivots: v^=pivots[p]
            else: pivots[p]=v; basis.append(a); break
    d=len(basis); assert d==(9 if T==0 else 8) and len(kernel)==1<<d
    counts=[sum((b&x).bit_count()%2 for x in support) for b in basis]
    assert all(c%2==0 for c in counts)
    pair={(i,j):sum(((basis[i]&x).bit_count()%2)*((basis[j]&x).bit_count()%2)
                      for x in support)%2 for i in range(d) for j in range(i+1,d)}
    mismatch=0; mutant_mismatch=0
    for mask in range(1<<d):
        a=0
        for i,b in enumerate(basis):
            if mask>>i&1: a^=b
        na=sum((a&x).bit_count()%2 for x in support)
        k=(na-128) if a else 0
        assert k%2==0
        actual=(k//2)%2
        predicted=(sum((counts[i]//2)*(mask>>i&1) for i in range(d))+
                   sum(v*(mask>>i&1)*(mask>>j&1) for (i,j),v in pair.items()))%2
        mismatch+=actual!=predicted
        mutant_mismatch+=actual!=(predicted^(mask&1))
    assert mismatch==0 and mutant_mismatch>0
    return {'T':T,'kernel_dimension':d,'frequencies_checked':len(kernel),'mutation_mismatches':mutant_mismatch}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--balanced',type=pathlib.Path,required=True)
    p.add_argument('--formal',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True)
    args=p.parse_args()
    if args.output.exists(): raise FileExistsError(args.output)
    # Full binary parity expansion mod 4 for every pair a,x in F_2^9.
    for a in range(512):
        for x in range(512):
            n=(a&x).bit_count()
            assert (n-2*(n*(n-1)//2))%4==n%2
    distributions={}
    for n in (4,5):
        degree_terms=n+n*(n-1)//2
        zeros=collections.Counter()
        for coeff in range(1<<degree_terms):
            q=quadratic_truth(n,coeff)
            assert not q&1
            z=(1<<n)-q.bit_count()
            assert z>=1<<(n-2)
            zeros[z]+=1
        distributions[str(n)]={str(k):v for k,v in sorted(zeros.items())}
    # The degree-two lower bound is sharp as a statement about q alone.
    q=sum(1<<x for x in range(256) if ((x&1)^((x>>1)&1)^((x&1)&((x>>1)&1))))
    assert not q&1 and 256-q.bit_count()==64
    data=json.loads(args.balanced.read_text(encoding='utf-8'))
    sample=[int(c) for c in data['bits']]
    case_nonzero=check_truth_case(sample)
    case_zero=check_truth_case([x&1 for x in range(512)])
    assert case_zero['T']==0
    formal=json.loads(args.formal.read_text(encoding='utf-8'))['spectrum_k']
    cube=[0,8,16,24,32,40,48,56]
    values=[formal[x] for x in cube]
    signed=sum((-1 if (i.bit_count()%2)==0 else 1)*values[i] for i in range(8))
    assert values==[0,-6,-6,-6,-6,-6,-6,-6] and signed%4==2
    qzeros=sum(x%4==0 for x in formal[:256])
    assert qzeros==8
    receipt={'parity_expansion_pairs_checked':512*512,'quadratic_zero_distributions_n4_n5':distributions,
             'dimension8_filter_only_sharp_zero_count':64,'balanced_truth_controls':[case_nonzero,case_zero],
             'formal_even_half_q_zero_count':qzeros,'formal_third_difference_directions':[8,16,32],
             'formal_cube_values':values,'formal_third_difference_mod4':signed%4,
             'formal_fails_boolean_caller':True,'numerical_tests_do_not_replace_written_proof':True}
    with args.output.open('x',encoding='utf-8') as out: json.dump(receipt,out,indent=2,sort_keys=True); out.write('\n')
    print('parity_pairs=',512*512,'quadratics_n4=1024 quadratics_n5=32768 formal_cube_mod4=',signed%4,flush=True)


if __name__=='__main__': main()
