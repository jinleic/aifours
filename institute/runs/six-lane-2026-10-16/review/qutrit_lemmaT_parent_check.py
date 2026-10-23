"""Parent-authored exact random-instance check of Lemma T (not a proof): for 2x2 complex-rational u1,u2,
the solutions (v1,v2) of u1 J v1^T + u2 J v2^T = 0 form a linear space; for random points of it,
rank(u1 (x) v1 + u2 (x) v2) <= 2. Pencil types: generic, common image (u_k = a b_k^T), common kernel
(u_k = a_k b^T), one-dimensional span, nilpotent part. Control: random (v1,v2) without the hypothesis gives rank 4.
Usage: python -B qutrit_lemmaT_parent_check.py NEW_RECEIPT.json   (needs sympy)
"""
from datetime import datetime
import json
from pathlib import Path
import random
import sys
from zoneinfo import ZoneInfo
import sympy as sp

J = sp.Matrix([[0, 1], [-1, 0]])
rng = random.Random(20261017)


def q():
    return sp.Rational(rng.randint(-9, 9), rng.randint(1, 5)) + sp.I * sp.Rational(rng.randint(-9, 9), rng.randint(1, 5))


def mat():
    return sp.Matrix(2, 2, lambda i, j: q())


def vec():
    return sp.Matrix(2, 1, lambda i, j: q())


def solutions(u1, u2):
    syms = sp.symbols('w0:8')
    v1 = sp.Matrix(2, 2, syms[:4])
    v2 = sp.Matrix(2, 2, syms[4:])
    eqs = list(u1 * J * v1.T + u2 * J * v2.T)
    A, b = sp.linear_eq_to_matrix(eqs, syms)
    return A.nullspace()


def tensor(u, v):
    return sp.Matrix(sp.kronecker_product(u, v))


def main():
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    kinds = {
        'generic': lambda: (mat(), mat()),
        'common-image': lambda: (lambda a: (a * vec().T, a * vec().T))(vec()),
        'common-kernel': lambda: (lambda b: (vec() * b.T, vec() * b.T))(vec()),
        'one-dimensional': lambda: (lambda m: (m, q() * m))(mat()),
        'nilpotent-pencil': lambda: (sp.eye(2), sp.Matrix([[q(), 1], [0, 0]]) + sp.Matrix([[0, 0], [0, 0]])),
        'jordan-pencil': lambda: (lambda l: (sp.eye(2), sp.Matrix([[l, 1], [0, l]])))(q()),
    }
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'cases': {}, 'status': 'FAILED'}
    ok = True
    for name, gen in kinds.items():
        ranks = []
        for _ in range(12):
            u1, u2 = gen()
            basis = solutions(u1, u2)
            coeffs = [q() for _ in basis]
            w = sum((c * v for c, v in zip(coeffs, basis)), sp.zeros(8, 1))
            v1 = sp.Matrix(2, 2, list(w[:4]))
            v2 = sp.Matrix(2, 2, list(w[4:]))
            assert (u1 * J * v1.T + u2 * J * v2.T).expand() == sp.zeros(2, 2)
            ranks.append((tensor(u1, v1) + tensor(u2, v2)).rank(simplify=True))
        result['cases'][name] = {'instances': len(ranks), 'max_rank': max(ranks), 'ranks': ranks}
        ok &= max(ranks) <= 2
    control = [(tensor(mat(), mat()) + tensor(mat(), mat())).rank(simplify=True) for _ in range(6)]
    result['control_without_hypothesis_ranks'] = control
    ok &= 4 in control
    result['status'] = 'PARENT_LEMMA_T_RANDOM_EXACT_INSTANCES_PASS' if ok else 'FAILED'
    result['limits'] = 'Random exact instances only; the proof is the written Lemma T argument.'
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({k: (v if k != 'cases' else {n: c['max_rank'] for n, c in v.items()}) for k, v in result.items()}, indent=1))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
