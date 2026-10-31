#!/usr/bin/env python3
"""Independent exact divisor-clique and primitive-prime controls for PSU3.

This is bounded integer arithmetic only, not a proof of classification,
Zsigmondy, actual coset existence, or all-field unitary group statements.
"""
from itertools import product, combinations
from math import gcd, isqrt, factorial, prod
import json


def divisors(factors):
    return sorted(prod(p**a for (p,_),a in zip(factors,exps))
                  for exps in product(*(range(e+1) for _,e in factors)))


def max_clique(nums):
    n=len(nums); adj=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if 2<=gcd(nums[i],nums[j])<=7:
                adj[i]|=1<<j;adj[j]|=1<<i
    best=(); nodes=0
    def dfs(mask,chosen):
        nonlocal best,nodes
        nodes+=1
        if len(chosen)>len(best): best=chosen
        while mask and len(chosen)+mask.bit_count()>len(best):
            bit=mask & -mask;j=bit.bit_length()-1;mask^=bit
            dfs(mask & adj[j],chosen+(j,))
    dfs((1<<n)-1,())
    return {'candidate_divisors':n,'max_clique':len(best),
            'one_clique':[nums[j] for j in best],'search_nodes':nodes}


def isprime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True


def prime_factors(n):
    out=[]
    for p in range(2,n+1):
        if n%p==0 and isprime(p):out.append(p)
    return out


def mod_order(a,r):
    x=1
    for k in range(1,r):
        x=x*(a%r)%r
        if x==1:return k
    raise ValueError('multiplicative order absent')


def primitive(p,f):
    d=6*f
    for r in range(d+1,500001,d):
        if not isprime(r) or r==p or pow(p,d,r)!=1:continue
        if any(pow(p,d//s,r)==1 for s in prime_factors(d)):continue
        q=p**f
        beta=all(pow(p,3*f//k,r)!=r-1 for k in prime_factors(f) if k%2 and k!=r)
        order=q**3*(q**3+1)*(q*q-1)//gcd(3,q+1)
        ordp,ordq=mod_order(p,r),mod_order(q,r)
        assert ordp==d and ordq==6 and beta and order%r==0 and order>factorial(7)
        return {'p':p,'f':f,'q':q,'primitive_r':r,
                'order_p_mod_r':ordp,'order_q_mod_r':ordq,
                'beta':beta,'r_divides_group_order':order%r==0,
                'group_order_gt_7_factorial':order>factorial(7)}
    return {'p':p,'f':f,'status':'UNKNOWN within bound 500000'}


def control(values):
    return {'indices':values,'pair_gcds':[gcd(a,b) for a,b in combinations(values,2)],
            'seven_divisible':sum(x%7==0 for x in values),
            'limits':'arithmetic support pattern only; not an actual coset family'}


small=[]
for q,factors in ((3,((2,5),(3,3),(7,1))), (5,((2,4),(3,2),(5,3),(7,1)))):
    nums=[x for x in divisors(factors) if x>=8]
    small.append({'q':q,'group_order':prod(p**e for p,e in factors),**max_clique(nums)})
f6=7**12-7**6+1
f6_isprime=isprime(f6)
f6_order=mod_order(7,f6) if f6_isprime else None
f6_beta=pow(7,6,f6)!=f6-1
assert f6==13841169553 and f6_isprime and f6_order==36 and f6_beta
print(json.dumps({'small_fields':small,
                  'bounded_primitive':[primitive(p,f) for p in (2,3,5,7) for f in (2,3,4)],
                  'prime_field_q7_control':{'r':43,'isprime':isprime(43),'order_7_mod_43':mod_order(7,43)},
                  'f6_cyclotomic_control':{'r':f6,'isprime':f6_isprime,'order_7_mod_r':f6_order,'beta':f6_beta},
                  'excluded_index7_control':control([7,14,21,35]),
                  'seven_squared_control':control([49,14,21,35]),
                  'limits':'divisor graph is an overapproximation, not actual coset or classification verification'},indent=2))
