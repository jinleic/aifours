#!/usr/bin/env python3
"""Independent exact arithmetic for the f99 review; no author checker is imported."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import gcd

# CRT Fourier/chirp phases in 2p dimensions, including the m=3 consequence.
for p in (3, 5):
    n = 2*p
    h = pow(2, -1, p)
    chirp = ((p+1)*(p+1)//4) % p
    qubit = p*p % (2*n)
    t = lambda a,b: (p*a+(p+1)*b) % n
    points = list(product(range(2), range(p)))
    assert {t(a,b) for a,b in points} == set(range(n))
    for (a,b),(c,d) in product(points, repeat=2):
        assert (2*t(a,b)*t(c,d) - n*a*c - 4*h*b*d) % (2*n) == 0
    for a,b in points:
        assert (t(a,b)**2 - qubit*a - 4*chirp*b*b) % (2*n) == 0
    print(f'CRT p={p}: bijection {n}, Fourier identities {n*n}, chirp identities {n}; Fourier coefficient {h}, qubit xi exponent {qubit}, five/three-factor chirp coefficient {chirp}')

# A Weyl operator Z^q X^r acts on |t> with the indicated output and root exponent.
def act(q,r,n,t):
    t = (t+r) % n
    return t, q*t % n

def power(q,r,n,t,count):
    phase=0
    for _ in range(count):
        t,e=act(q,r,n,t)
        phase=(phase+e) % n
    return t,phase

odd=Counter()
even=[]
for q,r in product(range(10), repeat=2):
    if q==r==0:
        continue
    if q%2 or r%2:
        axis=(q%2,r%2)
        diffs=[]
        for t in range(10):
            out,e=power(q,r,10,t,5)
            ref,er=power(axis[0],axis[1],10,t,5)
            assert out==ref
            diffs.append((e-er)%10)
        assert len(set(diffs))==1
        odd[axis]+=1
    else:
        Q,R=(3*q)%5,r%5
        assert (Q,R)!=(0,0)
        for a,b in product(range(2),range(5)):
            t=(5*a+6*b)%10
            out,e=act(q,r,10,t)
            bout,be=act(Q,R,5,b)
            assert out==(5*a+6*bout)%10
            assert (e-2*be)%10==0
        if R==0:
            assert len({act(Q,R,5,b)[1] for b in range(5)})==5
        else:
            for b in range(5):
                seen=[]
                z=b
                for _ in range(5):
                    seen.append(z)
                    z,_=act(Q,R,5,z)
                assert len(set(seen))==5 and z==b
                assert power(Q,R,5,b,5)==(b,0)
        even.append((Q,R))
assert odd==Counter({(1,0):25,(0,1):25,(1,1):25})
assert len(even)==len(set(even))==24
# For a flat pure qubit, X-unbiased requires relative phase +/-i; Y requires +/-1.
x_phases={1,3}; y_phases={0,2}  # exponents of i
assert not x_phases & y_phases
print(f'Weyl stabilizers: odd axes {dict(sorted(odd.items()))}; even labels {len(even)} all nonzero/distinct; all 5D spectra simple by exact diagonal/cycle checks')
print('Pure-qubit obstruction: fourth-root exponents X={1,3}, Y={0,2}, intersection empty')

# Check the X/Y amplitude identities as polynomials over Z in Re/Im parts.
def add(*polys):
    c=Counter()
    for p in polys:
        c.update(p)
    return {k:v for k,v in c.items() if v}
def neg(p): return {k:-v for k,v in p.items()}
def scale(p,n): return {k:v*n for k,v in p.items() if v*n}
def mul(p,q):
    c=Counter()
    for a,av in p.items():
        for b,bv in q.items():
            c[tuple(u+v for u,v in zip(a,b))] += av*bv
    return {k:v for k,v in c.items() if v}
def norm2(re,im): return add(mul(re,re),mul(im,im))
x={(1,0,0,0):1}; y={(0,1,0,0):1}; r={(0,0,1,0):1}; s={(0,0,0,1):1}
base=add(norm2(x,y),norm2(r,s))
reuv=add(mul(x,r),mul(y,s))
imuv=add(mul(x,s),neg(mul(y,r)))
assert norm2(add(x,r),add(y,s))==add(base,scale(reuv,2))
assert norm2(add(x,neg(r)),add(y,neg(s)))==add(base,scale(reuv,-2))
assert norm2(add(x,neg(s)),add(y,r))==add(base,scale(imuv,-2))
assert norm2(add(x,s),add(y,neg(r)))==add(base,scale(imuv,2))
print('Rank-2 equations: four X/Y amplitude expansions verified as exact integer polynomials')

# Arithmetic at a primitive fifth root: coefficients in Z[x]/Phi_5.
p=5
def canonical(a):
    return tuple(a[i]-a[p-1] for i in range(p-1))
def convolution(a,b):
    return [sum(a[i]*b[(j-i)%p] for i in range(p)) for j in range(p)]
def conjugate(a): return [a[-j%p] for j in range(p)]
def root_shift(a,k): return [a[(j-k)%p] for j in range(p)]
def gauss(q,j,c):
    a=[0]*p
    for t in range(p): a[(q*t*t+3*(c-j)*t)%p]+=1
    return a
orth=[0]*p
for t in range(p): orth[(3*t)%p]+=1
assert canonical(orth)==(0,0,0,0)
for q,j,c in product((3,4),range(p),range(p)):
    v=gauss(q,j,c)
    norm=convolution(v,conjugate(v)); norm[0]-=5
    assert canonical(norm)==(0,0,0,0)
ratios=[]
for j in range(p):
    a,b=gauss(3,j,0),gauss(3,j,1)
    ks=[k for k in range(p) if canonical([bj-aj for bj,aj in zip(b,root_shift(a,k))])==(0,0,0,0)]
    assert len(ks)==1
    ratios.append(ks[0])
    ubarv=convolution(conjugate(a),b)
    real_numerator=[z+w for z,w in zip(ubarv,conjugate(ubarv))]
    assert canonical(real_numerator)!=(0,0,0,0)
assert ratios==[3,2,1,0,4]
print(f'Rank-2 example: 50 exact Gauss squared norms = 5; W columns orthogonal; U ratios = {ratios}; all 5 real cross numerators nonzero in Q(zeta_5)')

# Exact solution of cyclic probability equations, no floating point.
def unique_solution(m,d):
    A=[[Fraction(0) for _ in range(m+1)] for _ in range(m)]
    for j in range(m):
        A[j][j]+=1
        A[j][(j-d)%m]+=1
        A[j][-1]=Fraction(2,m)
    row=0
    pivots=[]
    for col in range(m):
        pivot=next((r for r in range(row,m) if A[r][col]),None)
        if pivot is None: continue
        A[row],A[pivot]=A[pivot],A[row]
        a=A[row][col]
        A[row]=[v/a for v in A[row]]
        for r in range(m):
            if r!=row:
                a=A[r][col]
                A[r]=[u-a*v for u,v in zip(A[r],A[row])]
        pivots.append(col)
        row+=1
    assert pivots==list(range(m))
    return [A[j][-1] for j in range(m)]

def cycles(m,d):
    remaining=set(range(m)); result=[]
    while remaining:
        start=min(remaining); cycle=[]; j=start
        while j not in cycle:
            assert j in remaining
            remaining.remove(j); cycle.append(j); j=(j-d)%m
        assert j==start
        result.append(cycle)
    return result

def possible_product_exponents(choices,length):
    s={0}
    for _ in range(length): s={(a+b)%4 for a in s for b in choices}
    return s

for m in (3,5,9,15):
    lengths=set()
    for d in range(1,m):
        assert unique_solution(m,d)==[Fraction(1,m)]*m
        cs=cycles(m,d)
        for c in cs:
            ell=len(c)
            assert ell==m//gcd(m,d) and ell%2==1
            xs=possible_product_exponents((1,3),ell)
            ys=possible_product_exponents((0,2),ell)
            assert xs=={1,3} and ys=={0,2} and not xs&ys
            lengths.add(ell)
    print(f'Odd-cycle m={m}: {m-1} nonzero shifts, exact rational unique p_j=1/{m}, cycle lengths {sorted(lengths)}, lambda^ell X={{i,-i}} versus Y={{1,-1}}')

# Fourier-shift identity: coefficient equality for all indices; D commutes pointwise.
for m,h in ((3,1),(3,2),(5,1),(5,3),(9,1),(15,1)):
    for k in range(1,m):
        d=(k*pow(h,-1,m))%m
        for j,t in product(range(m),repeat=2):
            assert (-h*t*j+k*t+h*t*(j-d))%m==0
    print(f'Fourier character shift: m={m}, exponent coefficient h={h}, all k,j,t exact; any diagonal D commutes')

for p in (3,5):
    nonnegative_zero=[]
    for counts in product(range(p+1),repeat=p):
        if sum(counts)==p and len(set(counts))==1:
            nonnegative_zero.append(counts)
    assert nonnegative_zero==[(1,)*p]
    perms=list(permutations(range(p)))
    affine={tuple((a*t+b)%p for t in range(p)) for a in range(1,p) for b in range(p)}
    assert affine.issubset(set(perms)) and len(affine)==p*(p-1)
    print(f'Ratio census p={p}: Phi_p zero-count vector {nonnegative_zero[0]}; permutations={len(perms)}, affine={len(affine)}, nonaffine={len(perms)-len(affine)}')
print('ALL EXACT CHECKS PASSED; analytic arguments and scope limits are in the review, not implied by finite enumeration.')
