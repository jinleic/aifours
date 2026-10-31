#!/usr/bin/env python3
"""Independent exact matrix/normal-order checks for the f43 Levi review."""
from fractions import Fraction
from functools import lru_cache
import json


def unit(i, j):
    return tuple(Fraction(int(k == 3*i+j)) for k in range(9))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def matmul(a, b):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))
                 for i in range(3) for j in range(3))


def bracket(a, b):
    return sub(matmul(a,b), matmul(b,a))


def rank(vectors):
    M = [list(row) for row in zip(*vectors)]
    pivot = 0
    for c in range(len(vectors)):
        p = next((i for i in range(pivot, len(M)) if M[i][c]), None)
        if p is None:
            continue
        M[pivot], M[p] = M[p], M[pivot]
        divisor = M[pivot][c]
        M[pivot] = [v/divisor for v in M[pivot]]
        for i in range(len(M)):
            if i != pivot:
                factor = M[i][c]
                M[i] = [u-factor*v for u,v in zip(M[i], M[pivot])]
        pivot += 1
        if pivot == len(M):
            break
    return pivot


def ensure(flag, msg):
    if not flag:
        raise ValueError(msg)


def verify_basis(actual, expected):
    ensure(actual == expected, 'MODEL_BASIS_MISMATCH')
    ensure(rank(actual) == 8, 'DEPENDENT_BASIS')


def verify_cartan(c1, c2, c3, basis, increments, wrong=False):
    A = Fraction(2*c1+c2, 3)
    B = Fraction(c1+2*c2, 3)
    lam = c3+c1+c2 + int(wrong)
    h1 = sub(unit(0,0), unit(1,1))
    h2 = sub(unit(1,1), unit(2,2))
    H = add(scale(A, h1), scale(B, h2))
    for b, (i,j) in zip(basis, increments):
        actual = add(bracket(H,b),scale(lam,b))
        expected = scale(c3+i*c1+j*c2,b)
        ensure(actual == expected, 'CARTAN_ACTION_MISMATCH')


@lru_cache(None)
def normal(word):
    # x<z<y, with yx=xy-z, zx=xz and yz=zy.
    for i in range(len(word)-1):
        pair = word[i:i+2]
        if pair == ('y','x'):
            a = normal(word[:i]+('x','y')+word[i+2:])
            b = normal(word[:i]+('z',)+word[i+2:])
            out = dict(a)
            for k,v in b:
                out[k] = out.get(k,0)-v
            return tuple(sorted((k,v) for k,v in out.items() if v))
        if pair in (('z','x'),('y','z')):
            return normal(word[:i]+(pair[1],pair[0])+word[i+2:])
    return ((word,1),)


def poly(*terms):
    out = {}
    for coefficient, word in terms:
        for w,v in normal(tuple(word)):
            out[w] = out.get(w,0)+coefficient*v
    return {w:v for w,v in out.items() if v}


def main():
    E12,E23,E21,E32,E13,E31 = [unit(*p) for p in ((0,1),(1,2),(1,0),(2,1),(0,2),(2,0))]
    h1, h2 = bracket(E12,E21), bracket(E23,E32)
    z = bracket(E12,E23)
    ensure(z == E13, 'Z_MISMATCH')
    zero = (Fraction(0),)*9
    ensure(bracket(E12,z) == zero and bracket(E23,z) == zero, 'LEVI_SERRE_MISMATCH')
    ensure(bracket(E12,bracket(E12,E31)) == zero and bracket(E23,bracket(E23,E31)) == zero,
           'CYCLIC_SERRE_MISMATCH')
    ensure(bracket(E21,E31) == zero and bracket(E32,E31) == zero, 'LOWERING_MISMATCH')
    x = lambda v: bracket(E12,v)
    y = lambda v: bracket(E23,v)
    zz = lambda v: bracket(z,v)
    basis = [E31,x(E31),y(E31),zz(E31),x(y(E31)),zz(x(E31)),zz(y(E31)),zz(zz(E31))]
    expected = [E31,scale(-1,E32),E21,sub(unit(0,0),unit(2,2)),h1,
                scale(-1,E12),scale(-1,E23),scale(-2,E13)]
    verify_basis(basis,expected)
    ensure(poly((1,'xxyy'),(-1,'yyxx'),(-4,'zxy'),(2,'zz')) == {}, 'NORMAL_ORDER_MISMATCH')
    ensure(poly((1,'xxy'),(-1,'yxx'),(-2,'zx')) == {}, 'COMMUTATOR_MISMATCH')
    increments = [(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)]
    for c in ((1,0,0),(0,1,0),(0,0,1)):
        verify_cartan(*c,basis,increments)
    controls=[]
    damaged = list(expected);damaged[1]=scale(-1,damaged[1])
    try: verify_basis(basis,damaged)
    except ValueError as e:
        ensure(str(e)=='MODEL_BASIS_MISMATCH','wrong mutation outcome');controls.append(str(e))
    else: raise AssertionError('sign mutation accepted')
    damaged = list(basis);damaged[7]=damaged[6]
    try: verify_basis(damaged,damaged)
    except ValueError as e:
        ensure(str(e)=='DEPENDENT_BASIS','wrong mutation outcome');controls.append(str(e))
    else: raise AssertionError('rank mutation accepted')
    try: verify_cartan(1,0,0,basis,increments,wrong=True)
    except ValueError as e:
        ensure(str(e)=='CARTAN_ACTION_MISMATCH','wrong mutation outcome');controls.append(str(e))
    else: raise AssertionError('Cartan mutation accepted')
    return {'matrix_basis_rank':rank(basis), 'basis_entries_exact':True,
            'normal_order_identities_checked':2, 'full_Cartan_symbolic_coefficient_checks':24,
            'Serre_and_lowering_model_checks':True, 'intended_mutation_rejections':controls,
            'scope':'exact finite matrix/coefficient/normal-order identities only; no quotient proof'}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
