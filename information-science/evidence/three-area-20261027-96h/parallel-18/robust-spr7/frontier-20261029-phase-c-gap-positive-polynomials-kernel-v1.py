#!/usr/bin/env python3
"""Exact finite hard-vertex expansion for phase-C gap nodes; standard library only.

Executed by the owner in an Eval kernel, not a formal proof or independent review.
Variable order B,U,V,X,Y,Z,P,W,R. All must be strictly positive.
"""
from itertools import combinations
from functools import reduce
from fractions import Fraction
from hashlib import sha256
import json

N = 9
ZERO = (0,) * N

def const(c):
    return {ZERO: c} if c else {}

def add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}

def negative(poly):
    return {monomial: -coefficient for monomial, coefficient in poly.items()}

def subtract(x, y):
    return add(x, negative(y))

def multiply(x, y):
    out = {}
    for u, p in x.items():
        for v, q in y.items():
            monomial = tuple(u[j] + v[j] for j in range(N))
            out[monomial] = out.get(monomial, 0) + p*q
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}

def product(polys):
    out = const(1)
    for poly in polys:
        out = multiply(out, poly)
    return out

def elementary(polys, m):
    return const(1) if m == 0 else add(*(product(c) for c in combinations(polys, m)))

def numeric_elementary(values, m):
    return Fraction(1) if m == 0 else sum((reduce(lambda x, y: x*y, c, Fraction(1)) for c in combinations(values, m)), Fraction(0))

variables = [{tuple(int(i == j) for i in range(N)): 1} for j in range(N)]
B,U,V,X,Y,Z,P,W,R = variables
a = const(1)
b = add(a, B)
u1 = add(b, U)
c = add(u1, V)
u2 = add(c, X)
u3 = add(u2, Y)
d = add(u3, Z)
u4 = add(d, P)
e = add(u4, W)
f = add(e, R)
nodes = [u1,u2,u3,u4]

def numerator(first_root, m):
    if first_root == 0:
        den = [subtract(f,u1),subtract(f,u2),subtract(u3,a),subtract(u4,a)]
        n = [product([nodes[i],subtract(d,nodes[i]),subtract(e,nodes[i])]) for i in (0,1)]
        n += [product([nodes[i],subtract(nodes[i],b),subtract(nodes[i],c)]) for i in (2,3)]
    else:
        den = [subtract(f,u1),subtract(f,u2),const(1),const(1)]
        n = [product([subtract(nodes[i],a),subtract(d,nodes[i]),subtract(e,nodes[i])]) for i in (0,1)]
        n += [product([subtract(nodes[i],b),subtract(nodes[i],c)]) for i in (2,3)]
    terms = []
    for i in range(4):
        others = [j for j in range(4) if j != i]
        weight = elementary([nodes[j] for j in others], m)
        vandermonde = product([subtract(nodes[v],nodes[u]) for u,v in combinations(others,2)])
        term = product([weight,n[i],vandermonde,*[den[j] for j in others]])
        terms.append(term if i in (1,2) else negative(term))
    return add(*terms)

def evaluate(poly, values):
    return sum(coefficient * reduce(lambda x, j: x*values[j]**monomial[j], range(N), Fraction(1)) for monomial,coefficient in poly.items())

def direct_scaled(values, first_root, m):
    B,U,V,X,Y,Z,P,W,R = values
    a = Fraction(1); b = a+B; u1 = b+U; c = u1+V
    u2 = c+X; u3 = u2+Y; d = u3+Z; u4 = d+P; e = u4+W; f = e+R
    nodes = [u1,u2,u3,u4]
    out = Fraction(0)
    for i,t in enumerate(nodes):
        others = [nodes[j] for j in range(4) if j != i]
        Hprime = reduce(lambda v,z: v*(t-z), others, Fraction(1))
        oddroots = (b,c,f) if i < 2 else (a,d,e)
        O = reduce(lambda v,z: v*(z-t), oddroots, Fraction(1))
        E = (first_root-t)*(c-t)*(d-t)
        F = (-t)*(b-t)*(e-t)
        out += numeric_elementary(others,m)*E*F/(t*O*Hprime)
    Vdm = reduce(lambda v,ij: v*(nodes[ij[1]]-nodes[ij[0]]), combinations(range(4),2), Fraction(1))
    denominator = (f-u1)*(f-u2)
    if first_root == 0:
        denominator *= (u3-a)*(u4-a)
    return out*Vdm*denominator

expected = {
(0,0):(11357,'21dfbc28fccdfb436ac7d562582bc13df6f128484d713147bb799c9307ee0102'),
(0,1):(27170,'9a9f4d4684a79da37811f9a022622bc8d529263008d02e5bdca6288c51118943'),
(0,2):(53462,'f039fa325cfdc0daeafaf8e66b9f64736cfadc4c031e3ea65242d8a6dfb9dcf5'),
(0,3):(89883,'2eba62731d20117bfcfe90fb9e3a5b4789dc34353e765c01bd0a7c2d772e0b72'),
(1,0):(1292,'dd3834e2a6101f0e53c1f4ba21668fafc92124841d58e4891be43d1f73cdaa21'),
(1,1):(4969,'595e513f1b7c574181835e515b49ba0e125fbe05975f32fbb97ca244ed92780d'),
(1,2):(12719,'7e621b63f691e412ea15f69e8d0fee8439bc02290886661de1dc6e69dbb078d5'),
(1,3):(24167,'4d7bf583f8fd0f45f37a67e801b6cf98f66e751298037162fc5105ddaf616099'),
}
samples = [
    list(map(Fraction,['1','2','1','1','2','1','3','1','2'])),
    list(map(Fraction,['1/3','1/5','7/4','2/7','3/8','1/4','5/3','1/9','9/5'])),
]
records = []
for first_root in (0,1):
    for m in range(4):
        poly = numerator(first_root,m)
        digest = sha256()
        for monomial, coefficient in sorted(poly.items()):
            digest.update((','.join(map(str,monomial))+':'+str(coefficient)+'\n').encode())
        count, expected_hash = expected[(first_root,m)]
        assert len(poly) == count and digest.hexdigest() == expected_hash
        assert poly and min(poly.values()) > 0
        checks = [evaluate(poly, sample) == direct_scaled(sample, first_root, m) for sample in samples]
        assert all(checks)
        records.append({'first_root': first_root, 'm':m, 'monomials':len(poly),
                        'min_coefficient':min(poly.values()), 'max_coefficient':max(poly.values()),
                        'coefficient_sum':sum(poly.values()), 'sha256':digest.hexdigest(),
                        'two_direct_fraction_identities':checks})
print(json.dumps({'arithmetic':'integer multivariate expansion plus Fraction point identities',
                  'variable_order':['B','U','V','X','Y','Z','P','W','R'],
                  'all_coefficients_strictly_positive':True,'records':records},indent=2,sort_keys=True))
