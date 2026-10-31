#!/usr/bin/env python3
"""Independent exact f53 checks: cyclotomics, Latin incidence, GF(9) fragment."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
import json


def trim(a):
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def divide_monic(a,b):
    a=trim(list(a)); b=trim(list(b))
    if b[-1]!=1:
        raise ValueError('divisor must be monic')
    quotient=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b);c=a[-1];quotient[k]=c
        for i,v in enumerate(b):
            a[k+i]-=c*v
        trim(a)
    return trim(quotient),trim(a)


@lru_cache(None)
def phi(n):
    P=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            P,rem=divide_monic(P,phi(d))
            if any(rem):raise AssertionError('non-exact cyclotomic division')
    return tuple(P)


def is_solution(exponents,q):
    counts=[0]*q
    for a in exponents:
        for b in exponents:
            counts[(a-b)%q]+=1
    counts[0]-=8
    return not any(divide_monic(counts,phi(q))[1])


def root_sums():
    out=[]
    for q in (2,3,4,5,6,7,8,9,10,12,15):
        total=found=0
        for v in combinations_with_replacement(range(q),7):
            total+=1
            found+=is_solution(v,q)
        out.append({'q':q,'multisets':total,'solutions':found})
    example=(0,0,0,3,3,4,8)
    if not is_solution(example,12):raise AssertionError('composite counterexample failed')
    return {'domains':out,'q12_witness':example,'q12_phi':phi(12)}


def partitions(n, upper=None):
    if n==0:
        yield ()
        return
    upper=min(n,upper if upper is not None else n)
    for k in range(upper,0,-1):
        for rest in partitions(n-k,k):yield (k,)+rest


def check_41():
    parts=list(partitions(7))
    possible=[p for p in parts if sum(x*x for x in p)==9]
    if possible!=[(2,1,1,1,1,1)]:raise AssertionError('c0=9 partition error')
    return {'integer_partitions_of_7':len(parts),'c0_equals_9_cases':possible,
            'conclusion':'one duplicate forces a nonzero difference with multiplicity at least 2'}


def twophase():
    count=0
    for a in range(8):
        for b in range(8-a):
            c=7-a-b;v=49*(a-3)**2+7*(b-c)**2
            if v%7 or v==128:raise AssertionError('two-phase obstruction failed')
            count+=1
    return {'nonnegative_count_triples':count,'possible_target_128':False}


def incidence():
    n=10;cells=list(product(range(n),repeat=2))
    symbol=lambda r,c:(r+c)%n
    partner_counts=[]
    for ref in range(n):
        # Reference basis index is column i; its transversal label is ref+i.
        refsym={symbol(ref,c):c for c in range(n)}
        mult=Counter()
        for r,c in cells:
            if r==ref:continue
            zeros=frozenset((c,refsym[symbol(r,c)]))
            if len(zeros)!=2:raise AssertionError('zero labels coincide')
            mult[zeros]+=1
            partners=0
            for rr,cc in cells:
                if rr==ref or (rr,cc)==(r,c):continue
                if rr==r or cc==c or symbol(rr,cc)==symbol(r,c):continue
                other=frozenset((cc,refsym[symbol(rr,cc)]))
                if len(zeros&other)==1:partners+=1
            partner_counts.append(partners)
        if len(mult)!=45 or any(v!=2 for v in mult.values()):
            raise AssertionError('zero-pair multiplicity failed')
    B=[]
    for x,(r,c) in enumerate(cells):
        row=[]
        for y,(rr,cc) in enumerate(cells):
            shared=(r==rr or c==cc or symbol(r,c)==symbol(rr,cc))
            row.append(8 if x==y else 0 if shared else 1)
        B.append(row)
    if any(sum(row)!=80 for row in B):raise AssertionError('wrong row sum')
    for i in range(100):
        for j in range(100):
            if sum(B[i][k]*B[k][j] for k in range(100))!=10*B[i][j]+56:
                raise AssertionError('Gram polynomial mismatch')
    if min(partner_counts)<14:raise AssertionError('partner lower bound failed')
    return {'latin_order':n,'reference_rows':10,'nonreference_cells':len(partner_counts),
            'pair_multiplicity':2,'partner_min':min(partner_counts),'partner_max':max(partner_counts),
            'formal_gram_entries_checked':10000,'integer_identity':'B^2=10B+56J',
            'physical_lift_claimed':False}


def mul9(x,y):
    a,b=x;c,d=y
    return ((a*c-b*d)%3,(a*d+b*c)%3)


def sub9(x,y):return ((x[0]-y[0])%3,(x[1]-y[1])%3)


def fieldmul(x,y):
    a,b=x;c,d=y
    return (a*c-7*b*d,a*d+b*c)


def fieldsub(x,y):return (x[0]-y[0],x[1]-y[1])


def conference():
    V=list(product(range(3),repeat=2))
    squares={mul9(x,x) for x in V if x!=(0,0)}
    if len(squares)!=4:raise AssertionError('bad GF9 nonzero squares')
    U=[]
    for x in V:
        row=[]
        for y in V:
            if x==y:row.append((0,0))
            else:row.append((1,1 if sub9(x,y) in squares else -1))
        U.append(row)
    for i in range(9):
        for j in range(9):
            terms=[fieldmul(U[i][k],(U[j][k][0],-U[j][k][1])) for k in range(9)]
            result=tuple(sum(t[z] for t in terms) for z in (0,1))
            if result!=((64,0) if i==j else (0,0)):
                raise AssertionError(('not unitary',i,j,result))
    rays=[]
    for i in range(10):
        rays.append([(8,0) if i==j else (0,0) for j in range(10)])
    for c in range(9):rays.append([(0,0)]+[U[r][c] for r in range(9)])
    for v,w in combinations(rays,2):
        if not any(fieldsub(fieldmul(v[i],w[j]),fieldmul(v[j],w[i]))!=(0,0)
                   for i,j in combinations(range(10),2)):
            raise AssertionError('parallel rays')
    for c in range(9):
        col=[U[r][c] for r in range(9)]
        if sum(x==(0,0) for x in col)!=1 or any(a*a+7*b*b!=8 for a,b in col if (a,b)!=(0,0)):
            raise AssertionError('conference support/cross magnitude')
    return {'GF9_square_count':len(squares),'unitarity_entries':81,
            'distinct_rays':len(rays),'nonparallel_pairs':171,'scope':'two ONBs only'}


def main():
    return {'roots':root_sums(),'p41_multiplicities':check_41(),
            'two_phase':twophase(),'incidence':incidence(),'conference':conference()}


if __name__=='__main__':print(json.dumps(main(),indent=2))
