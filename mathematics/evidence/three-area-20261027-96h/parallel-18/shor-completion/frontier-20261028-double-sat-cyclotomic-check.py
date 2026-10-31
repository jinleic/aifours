#!/usr/bin/env python3
"""Exact finite checks for double-saturated Shor parity-class restrictions."""
from itertools import product
import json


def mono_remainder(k,p):
    """x^k mod Phi_(2p), p odd prime, in ascending power order."""
    k%=2*p;sign=1
    if k>=p:k-=p;sign=-1
    out=[0]*(p-1)
    if k<p-1:out[k]=sign
    else:
        for j in range(p-1):out[j]=sign*((-1)**(p-j))
    return out


def remainder(terms,p):
    out=[0]*(p-1)
    for k,c in terms:
        v=mono_remainder(k,p)
        out=[a+c*b for a,b in zip(out,v)]
    return out


def check_odd_primes():
    out=[]
    for p in (5,7,11,13,17,19):
        A=remainder([(0,1),(3,1),(8,1),(11,1)],p)
        if not any(A):raise AssertionError('old head polynomial vanishes')
        maxmono=max(max(abs(v) for v in mono_remainder(k,p)) for k in range(2*p))
        if maxmono!=1:raise AssertionError('monomial remainder coefficient bound failed')
        q=4*p;tested=0
        for a,b,c in product(range(min(p,7)),repeat=3):
            D=remainder([(0,-2),(11,-1),(16*a,1),(16*b,1),(11+16*c,1)],p)
            if max(abs(v) for v in D)>6:raise AssertionError('perturbation bound failed')
            if not any(q*x+y for x,y in zip(A,D)):
                raise AssertionError('unexpected head cancellation')
            tested+=1
        out.append({'p':p,'all_monomials_bounded_by':maxmono,'three_atom_residue_cases':tested})
    return out


def check_p3():
    zero=[];count=0
    for e1,e2,o1,o2 in product(range(7),repeat=4):
        real=-2*e1-e2-o1+o2
        omega=-e1+e2+o1+2*o2
        if real==0 and omega==0:zero.append((e1,e2,o1,o2))
        count+=1
    if zero!=[(0,0,0,0)]:raise AssertionError('p3 nonnegative cancellation classification failed')
    return {'count_vectors':count,'zero_solutions':zero}


def profile_checks():
    p=5
    E=[2,0,1,1,1];O=[0,2,1,1,1]
    C=[E[j%p] if j%2==0 else O[j%p] for j in range(2*p)]
    folded=[sum(C[j] for j in range(2*p) if j%p==b) for b in range(p)]
    if len(set(folded))!=1:raise AssertionError('prime-only control not balanced')
    if not any(remainder([(j,v) for j,v in enumerate(C)],p)):
        raise AssertionError('prime-only control unexpectedly satisfies Phi_2p')
    C2=[2 if j%2==0 else 3 for j in range(2*p)]
    if any(remainder([(j,v) for j,v in enumerate(C2)],p)):
        raise AssertionError('separate parity balance should satisfy Phi_2p')
    return {'prime_only_not_parity_uniform_control':'pass',
            'separate_parity_uniform_control':'pass','scope':'synthetic histograms, not Shor completions'}


if __name__=='__main__':
    print(json.dumps({'odd_prime_checks':check_odd_primes(), 'p3':check_p3(),
                      'parity_profile_controls':profile_checks()},indent=2))
