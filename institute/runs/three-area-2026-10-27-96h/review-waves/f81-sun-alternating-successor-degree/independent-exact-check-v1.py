#!/usr/bin/env python3
"""Reviewer-authored exact integer and permutation controls; not subgroup classification."""
from collections import deque
from itertools import combinations
from math import comb, factorial, gcd, isqrt, lcm


def isprime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def is_prime_power(n):
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            if not isprime(p):
                continue
            while n % p == 0:
                n //= p
            return n == 1
    return isprime(n)


def integer_repunit_hits(n):
    hits=[]
    # Minimum sum at q=2 is 2**d-1, so the loop exhausts every d >= 2.
    d=2
    while 2**d-1 <= n:
        q=2
        while True:
            value=sum(q**e for e in range(d))
            if value > n:
                break
            if value == n:
                hits.append((q,d,is_prime_power(q)))
            q += 1
        d += 1
    return hits


def dval(r,j):
    return (r+j)//gcd(r+j,lcm(*range(1,j+1)))


print('EXACT ELIGIBILITY, 19 AND SELECTED PRIMES')
for r in (19,419,421,431):
    assert isprime(r)
    hits=integer_repunit_hits(r)
    assert not any(pp for q,d,pp in hits)
    assert factorial(r-2) % (r+1) == 0
    print('r=',r,'mod8=',r%8,'all integer (q,d,is_prime_power) hits=',hits,'factorial_transfer=PASS')
print('\nFULL d_j AND BINOMIAL CONTROLS')
for r in (419,421,431):
    ds=[dval(r,j) for j in range(1,7)]
    print('r=',r,'d=',ds)
    for j,dj in enumerate(ds,1):
        values=[comb(r+j,u) for u in range(1,j+1)]
        remainders=[v%dj for v in values]
        assert dj > 7 and all(z == 0 for z in remainders)
        print(' j=',j,'L=',lcm(*range(1,j+1)),'d=',dj,'binomials=',values,'remainders=',remainders)
    b1=r+1
    b2=[comb(r+2,u) for u in (1,2)]
    b3=[comb(r+3,u) for u in (1,2,3)]
    print(' TYPED r=',r,'b1=',b1,'b2=',b2,'b3=',b3)
    for u2,v2 in enumerate(b2,1):
        for u3,v3 in enumerate(b3,1):
            if u3 in (1,3):
                divisor=14
                g=gcd(7*b1,7*v3)
                partner='type1'
            else:
                divisor=r+2
                g=gcd(7*v2,7*v3)
                partner='type2'
            assert g % divisor == 0 and g > 7
            print(' u2=',u2,'u3=',u3,'partner=',partner,'gcd_of_scaled_divisors=',g,'required_collision_divisor=',divisor)

print('\nRESIDUE/BOUND FINITE INTEGER SWEEP')
checks=0
for r in range(419,10020,2):
    for j in range(1,7):
        dj=dval(r,j)
        assert dj > 7
        assert all(comb(r+j,u)%dj==0 for u in range(1,j+1))
    b2=[comb(r+2,u) for u in (1,2)]
    b3=[comb(r+3,u) for u in (1,2,3)]
    assert all(v % (r+2)==0 for v in b2)
    assert b3[0]%2==0 and b3[2]%2==0 and b3[1]%(r+2)==0
    if r % 3 and r%4==1:
        assert dval(r,1)%2==dval(r,3)%2==0
    if r%8==3:
        assert dval(r,1)%2==dval(r,5)%2==0
    checks += 1
print('checked odd integers r=419..10019 inclusive:',checks,'(arithmetic only; not universal proof)')
print('borderline erroneous source inequality: r=419,j=1,r+j=',419+1,'>420 is',419+1>420,'while d1=',dval(419,1))

print('\nCOARSE r=431 TUPLE')
r=431
ds=[dval(r,j) for j in range(1,7)]
tuple7=[7*r]+[7*d for d in ds]
assert all(gcd(a,b)==1 for a,b in combinations(ds,2))
assert all(gcd(a,b)==7 for a,b in combinations(tuple7,2))
assert all((factorial(r+6)//2)%n==0 for n in tuple7)
type3=[comb(r+3,u) for u in (1,2,3)]
assert all(tuple7[3]%b!=0 for b in type3)
print('tuple=',tuple7,'all 21 pairwise gcds=7; all divide 437!/2')
print('1519 mod type3 binomials=',[tuple7[3]%b for b in type3],'type3 binomials=',type3)

print('\nINDEPENDENT A20 PERMUTATION CONSTRUCTION')
p=19
inf=p
T=tuple((x+1)%p if x!=inf else inf for x in range(p+1))
S=tuple(0 if x==inf else (inf if x==0 else -pow(x,-1,p)%p) for x in range(p+1))
def even(perm):
    return sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))%2==0
assert even(T) and even(S)
identity=tuple(range(p+1))
seen={identity}
work=deque([identity])
while work:
    a=work.popleft()
    for gen in (T,S):
        product=tuple(gen[a[i]] for i in range(p+1))
        if product not in seen:
            seen.add(product)
            work.append(product)
assert len(seen)==3420 and len({a[inf] for a in seen})==20
assert T[inf]==inf and all(T[x] == (x+1)%p for x in range(p))
assert all(even(a) for a in seen)
assert (factorial(19)//2)%len(seen)==0
assert (factorial(20)//(2*len(seen)))%20==0
print('generated <x+1,-1/x> with',len(seen),'even permutations; transitive on 20; T fixes infinity and is a 19-cycle')
print('proper transitive subgroup index A20=',factorial(20)//(2*len(seen)),'and is divisible by 20')
print('\nALL ASSERTIONS PASSED; exact controls are not a proof of the imported classification')
