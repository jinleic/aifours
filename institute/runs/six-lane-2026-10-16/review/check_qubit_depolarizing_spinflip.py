"""Exact finite controls for qubit depolarizing spectral symmetry p <-> 2-p.

Universal proof: J(X)=sigma_y X^T sigma_y=tr(X)I-X, so J D_p=D_(2-p).
Tensoring all local transposes is the global transpose, hence J^tensor n is conjugated global
transpose and preserves every eigenvalue. These controls supplement, not replace, that proof.
The parameter here is D_p=(1-p)id+p tr(.)I/2, NOT the total Pauli error convention.
"""
import hashlib
import json
from pathlib import Path

import sympy as s


def bitlist(value, n):
    return [(value >> (n-1-j)) & 1 for j in range(n)]


def replacement(rho, keep, n):
    """Return Tr_complement(rho) tensor unnormalized I_complement in original order."""
    keep = tuple(keep)
    discard = tuple(j for j in range(n) if j not in keep)
    dimension = 1 << n
    reduced = s.zeros(1 << len(keep))
    for x in range(dimension):
        bx = bitlist(x, n)
        for y in range(dimension):
            by = bitlist(y, n)
            if any(bx[j] != by[j] for j in discard):
                continue
            u = sum(bx[j] << (len(keep)-1-k) for k,j in enumerate(keep))
            v = sum(by[j] << (len(keep)-1-k) for k,j in enumerate(keep))
            reduced[u,v] += rho[x,y]
    output = s.zeros(dimension)
    for x in range(dimension):
        bx = bitlist(x, n)
        for y in range(dimension):
            by = bitlist(y, n)
            if all(bx[j] == by[j] for j in discard):
                u = sum(bx[j] << (len(keep)-1-k) for k,j in enumerate(keep))
                v = sum(by[j] << (len(keep)-1-k) for k,j in enumerate(keep))
                output[x,y] = reduced[u,v]
    return output


def depolarize(rho, p, n):
    output = s.zeros(1 << n)
    for mask in range(1 << n):
        keep = [j for j in range(n) if mask & (1 << j)]
        output += (1-p)**len(keep)*(p/2)**(n-len(keep))*replacement(rho, keep, n)
    return output.applyfunc(s.expand)


def main():
    Y = s.Matrix([[0,-s.I],[s.I,0]])
    reports = []
    bad_adjoint_rejected = False
    for n in range(1, 5):
        U = Y
        for _ in range(n-1):
            U = s.kronecker_product(U, Y)
        vector = s.Matrix([((3*j+1)%7-3) + s.I*((5*j+2)%11-5) for j in range(1<<n)])
        rho = (vector*vector.H).applyfunc(s.expand)/s.expand((vector.H*vector)[0])
        for p in map(s.Rational, ['1/4','2/3','1','7/6','4/3']):
            positive = depolarize(rho, p, n)
            mirrored = depolarize(rho, 2-p, n)
            error = (mirrored-U*positive.T*U).applyfunc(s.expand)
            if error != s.zeros(1<<n):
                raise ValueError(f'spin-flip identity failed at n={n}, p={p}')
            if positive.trace() != 1 or mirrored.trace() != 1:
                raise ValueError('trace not preserved')
            reports.append({'n':n,'p':str(p),'mirror_parameter':str(2-p),'matrix_identity_exact':True})
            if n == 3 and p == s.Rational(1,4):
                bad_adjoint_rejected = (mirrored-U*positive.H*U).applyfunc(s.expand) != s.zeros(1<<n)
    if not bad_adjoint_rejected:
        raise ValueError('complex transpose/adjoint control did not discriminate')
    print(json.dumps({'status':'EXACT_FINITE_CONTROLS_PASS','cases':reports,
                      'transpose_replaced_by_adjoint_rejected':bad_adjoint_rejected,
                      'sympy':s.__version__,
                      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'limits':'Finite matrix controls, not a proof of majorization. The universal spectral symmetry is the algebraic J D_p identity in the docstring.'},indent=2))


if __name__ == '__main__':
    main()
