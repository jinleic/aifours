#!/usr/bin/env python3
"""Independent finite checks of exact seam convolution/Fourier dichotomies.

Profiles here need not be actual Shor completions. Exhaustion is over integer
profiles at n=4 and 6; the all-order proof is supplied separately.
"""
from itertools import product
import json


def compositions(total, count):
    if count == 1:
        yield (total,)
        return
    for v in range(total+1):
        for rest in compositions(total-v, count-1):
            yield (v,)+rest


def convolution(r,c):
    n=len(r)
    return tuple(sum(c[j]*r[(g-j)%n] for j in range(n)) for g in range(n))


def folded(profile, d):
    return tuple(sum(v for i,v in enumerate(profile) if i%d==r) for r in range(d))


def prime_uniform(profile,p):
    c=folded(profile,p)
    return len(set(c))==1


def power2_balanced(profile,d):
    c=folded(profile,d)
    return all(c[r]==c[r+d//2] for r in range(d//2))


def exhaustive(n):
    profiles=list(compositions(n,n))
    conserved=0
    for r,c in product(profiles, repeat=2):
        if convolution(r,c)!=(n,)*n:
            continue
        conserved+=1
        for p in (2,3):
            if n%p==0 and not (prime_uniform(r,p) or prime_uniform(c,p)):
                raise AssertionError(('prime dichotomy',n,p,r,c))
        if n%4==0 and not (power2_balanced(r,4) or power2_balanced(c,4)):
            raise AssertionError(('order-four dichotomy',n,r,c))
    return {'n':n,'profiles':len(profiles),'pairs':len(profiles)**2,'conserved':conserved}


def synthetic_rectangle():
    n=12; A=(0,1,2); Y=(0,3,6,9)
    pairs={(a,y) for a in A for y in Y}
    rows=tuple(sum(i==a for i,j in pairs) for a in range(n))
    cols=tuple(sum(j==a for i,j in pairs) for a in range(n))
    if len(pairs)!=n or convolution(rows,cols)!=(n,)*n:
        raise AssertionError('synthetic conservation failed')
    keys={(i,(j+k)%n,l) for i,j in pairs for k,l in pairs}
    if len(keys)!=n*n:
        raise AssertionError('synthetic 2-path uniqueness failed')
    changed=list(rows);changed[0]+=1;changed[1]-=1
    if convolution(changed,cols)==(n,)*n:
        raise AssertionError('deliberate degree mutation was not rejected')
    return {'n':n,'pairs':len(pairs),'path_keys':len(keys),'degree_mutation_rejected':True,
            'scope':'synthetic rectangle, NOT an extension of the Shor code'}


def main():
    return {'finite_profile_exhaustion':[exhaustive(4),exhaustive(6)],
            'synthetic_rectangle':synthetic_rectangle(),
            'scope':'exact finite algebra checks only; all-order proof separate'}


if __name__=='__main__':
    print(json.dumps(main(),indent=2))
