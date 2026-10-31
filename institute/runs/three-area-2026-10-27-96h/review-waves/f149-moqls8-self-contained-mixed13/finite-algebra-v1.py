#!/usr/bin/env python3
"""Bounded symbolic and finite support checks, without external packages."""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import subprocess
import sys
from fractions import Fraction as F


def stamp():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


# Sparse formal commutative polynomials with independently named conjugates.
def var(s): return {(s,):1}
def add(a,b):
    z=collections.Counter(a)
    z.update(b)
    return {m:c for m,c in z.items() if c}
def mul(a,b):
    z=collections.Counter()
    for x,c in a.items():
        for y,d in b.items(): z[tuple(sorted(x+y))]+=c*d
    return {m:c for m,c in z.items() if c}


def symbolic_controls():
    zero={}
    A,B,Ac,Bc=map(var,('a','b','a_conjugate','b_conjugate'))
    C=[[zero,A],[B,zero]]
    Cstar=[[zero,Bc],[Ac,zero]]
    product=[[add(mul(Cstar[i][0],C[0][j]),mul(Cstar[i][1],C[1][j])) for j in range(2)] for i in range(2)]
    assert product==[[mul(Bc,B),zero],[zero,mul(Ac,A)]]
    # Orthogonal basis u1,u2,z. x1=alpha*u2+beta*z and
    # x2=gamma*u1+delta*z: the inner product has one monomial.
    ab,bb,gamma,delta=map(var,('alpha_conjugate','beta_conjugate','gamma','delta'))
    xx=[zero,ab,bb]; yy=[gamma,zero,delta]
    inner=add(add(mul(xx[0],yy[0]),mul(xx[1],yy[1])),mul(xx[2],yy[2]))
    assert inner==mul(bb,delta)
    # Dropping the beta!=0/full-support assumption permits beta=0, so the
    # sole monomial vanishes identically even when delta!=0.
    beta_zero={m:c for m,c in inner.items() if 'beta_conjugate' not in m}
    assert beta_zero=={}
    return {'cross_gram_star_times_cross_gram':'diag(b_conjugate*b, a_conjugate*a)',
            'three_space_inner_product':'beta_conjugate*delta',
            'mutation_allow_beta_zero_inner_polynomial':'0'}


def exact_dot(a,b):
    return (sum(x[0]*y[0]+x[1]*y[1] for x,y in zip(a,b)),
            sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(a,b)))


def exact_plane_controls():
    z=(F(0),F(0)); one=(F(1),F(0))
    ez=(z,z,one)
    u=((F(3,5),F(0)),(F(0),F(4,5)),z)
    v=((F(3,5),F(0)),(F(0),F(-4,5)),z)
    X=(ez,u); Y=(v,ez)
    for basis in (X,Y):
        assert all(exact_dot(basis[i],basis[j]) == (F(i==j),F(0)) for i in range(2) for j in range(2))
    gram=[[exact_dot(x,y) for y in Y] for x in X]
    assert gram==[[(F(0),F(0)),(F(1),F(0))],[(F(-7,25),F(0)),(F(0),F(0))]]
    assert X[0]==Y[1] and u!=v
    return {'shared_line':2,'cross_gram':[[[str(a),str(b)] for a,b in row] for row in gram],
            'zero_diagonal_and_unit_offdiagonal':True}


def support_counts():
    triples=[frozenset(s) for s in itertools.combinations(range(3),2)]+[frozenset(range(3))]
    total=0; mutant=None
    for p,q,qp,r,rp in itertools.product(triples,repeat=5):
        original=(sum(len(s)==2 for s in (p,q,qp))<=1 and sum(len(s)==2 for s in (p,r,rp))<=1)
        common=p&q&qp&r&rp
        if original:
            total+=1
            assert common
        elif not common and mutant is None:
            mutant=[sorted(x) for x in (p,q,qp,r,rp)]
    assert total==52 and mutant is not None
    # A support-2 vector and support-3 vectors orthogonal to it cannot
    # intersect its support in precisely one axis. Count only candidate
    # triples with no such single intersections inside a 4-axis line.
    pairs=[frozenset(s) for s in itertools.combinations(range(4),2)]
    threes=[frozenset(s) for s in itertools.combinations(range(4),3)]
    same=distinct=0
    for u,x,y in itertools.product(pairs,threes,threes):
        if len(u&x)==1 or len(u&y)==1: continue
        assert u<=x and u<=y
        if x==y: same+=1
        else: distinct+=1
    assert (same,distinct)==(12,12)
    return {'P23_five_ray_support_patterns':total,'P23_all_have_common_coordinate':True,
            'mutation_drop_degree3_at_most_one_support2':mutant,
            'P21_degree4_support2_plus_two_support3_patterns':{'same_3set':same,'distinct_3sets':distinct},
            'P21_conclusion':'same: remaining orthogonal line vector is a singleton; distinct: nonzero common projection on the 2-plane'}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',required=True); a=p.parse_args()
    out=pathlib.Path(a.out)
    if out.exists(): raise SystemExit('refusing overwrite')
    begin=stamp()
    result={'kind':'finite-algebra-v1','python':sys.version,'script_sha256':sha(__file__),
            'earlier_result_sha256':sha('finite-results-v1.json'),'clock_before':begin,
            'formal_identities':symbolic_controls(),'exact_plane':exact_plane_controls(),
            'finite_support':support_counts()}
    result['clock_immediately_before_output']=stamp()
    with out.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps({'output':str(out),'sha256':sha(out),'script_sha256':result['script_sha256'],
                      'clock_before_output':result['clock_immediately_before_output']}))


if __name__=='__main__': main()
