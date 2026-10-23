"""Exact (sympy) checks of the algebra behind Lemma T and Lemma N1 of review/LEMMA_R_PROOF.md.

Lemma T: u1 J v1^T + u2 J v2^T = 0  =>  rank(u1 (x) v1 + u2 (x) v2) <= 2   (2x2 matrices, J = [[0,1],[-1,0]]).
 T1  invertible case, u1 = I, u = u2 generic: v1 := -v2 adj(u) solves the hypothesis, and
     I(x)v1 + u(x)v2 == (I(x)v2) (u(x)I + I(x)u - tr(u) I4)  (polynomial identity);
 T2  every 3x3 minor of L(u) = u(x)I + I(x)u - tr(u) I4 vanishes identically (so rank L <= 2 for EVERY u,
     including non-diagonalisable u);
 T3  J adj(u)^T == u J identically, i.e. the hypothesis with u1 = I is equivalent to v1 = -v2 adj(u);
 T4  singular-pencil cases: u_k = a_k b^T  or  u_k = a b_k^T  give rank <= 2 identically (generic symbols);
 T5  tensor form: a tensor T[s,c,a,d] symmetric in (a,d) with rank_{(s,a)|(c,d)} <= 2 has
     Sum_k u_k J v_k^T = 0 for any rank-2 decomposition (symbolic identity on the antisymmetric part);
 T6  exact random rational instances (fixed seed) of the hypothesis: rank F <= 2; control: dropping the
     hypothesis gives rank 4.
Lemma N1 (gauge A = Sym): for symmetric N_d with N_0,N_1,N_2 independent, Sum Y_d N_d^dag = 0 = Sum N_d^dag Y_d
 forces Y_d symmetric.
 N1  symbolic: the antisymmetric parts delta_d satisfy J * Sum delta_d conj(N_d) = Sum (Y_d - Y_d^T) conj(N_d)
     = (Sum Y_d N_d^dag) - (Sum N_d^dag Y_d)^T  identically (so both hypotheses give Sum delta_d conj(N_d) = 0).
Writes ../evidence/lemma_T_exact.json.  Run: python -B lemma_T_exact.py
"""
import itertools
import json
import os
import random

import sympy as sp
from sympy import Matrix, eye, symbols
from sympy.physics.quantum import TensorProduct as kron

J = Matrix([[0, 1], [-1, 0]])


def adj2(u):
    return Matrix([[u[1, 1], -u[0, 1]], [-u[1, 0], u[0, 0]]])


def gen(name):
    a, b, c, d = symbols(name + "0:4")
    return Matrix([[a, b], [c, d]])


def all_minors_zero(M, k):
    n = M.shape[0]
    for rows in itertools.combinations(range(n), k):
        for cols in itertools.combinations(range(n), k):
            if sp.expand(M.extract(list(rows), list(cols)).det()) != 0:
                return False
    return True


def main():
    out = {}
    u, v2 = gen("u"), gen("w")
    v1 = -v2 * adj2(u)
    out["T1 hypothesis holds for v1=-v2 adj(u)"] = sp.expand(J * v1.T + u * J * v2.T) == sp.zeros(2, 2)
    L = kron(u, eye(2)) + kron(eye(2), u) - (u[0, 0] + u[1, 1]) * eye(4)
    F = kron(eye(2), v1) + kron(u, v2)
    out["T1 F == (I(x)v2) L(u)"] = sp.expand(F - kron(eye(2), v2) * L) == sp.zeros(4, 4)
    out["T2 all 3x3 minors of L(u) vanish identically"] = all_minors_zero(L, 3)
    out["T2 control: some 2x2 minor of L(u) is nonzero"] = not all_minors_zero(L, 2)
    out["T3 J adj(u)^T == u J"] = sp.expand(J * adj2(u).T - u * J) == sp.zeros(2, 2)

    a1, a2, b = Matrix(symbols("a1_0:2")), Matrix(symbols("a2_0:2")), Matrix(symbols("b0:2"))
    w1, w2 = gen("p"), gen("q")
    F1 = kron(a1 * b.T, w1) + kron(a2 * b.T, w2)
    F2 = kron(b * a1.T, w1) + kron(b * a2.T, w2)
    out["T4 u_k = a_k b^T: rank <= 2 identically"] = all_minors_zero(F1, 3)
    out["T4 u_k = a b_k^T: rank <= 2 identically"] = all_minors_zero(F2, 3)

    # T5: T[s,c,a,d] = sum_k u_k[s,a] v_k[c,d]; antisymmetric part in (a,d) at (a,d)=(0,1) equals sum_k u_k J v_k^T
    us, vs = [gen("x"), gen("y")], [gen("z"), gen("t")]
    ok5 = True
    for s, c in itertools.product(range(2), repeat=2):
        anti = sum(us[k][s, 0] * vs[k][c, 1] - us[k][s, 1] * vs[k][c, 0] for k in range(2))
        ujv = sum((us[k] * J * vs[k].T)[s, c] for k in range(2))
        ok5 &= sp.expand(anti - ujv) == 0
    out["T5 antisym part of T in (a,d) == sum_k u_k J v_k^T"] = bool(ok5)

    rnd = random.Random(20261017)
    rq = lambda: sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5))
    ranks, ctrl = [], []
    for _ in range(40):
        U1 = Matrix(2, 2, lambda i, j: rq())
        while U1.det() == 0:
            U1 = Matrix(2, 2, lambda i, j: rq())
        U2, V2 = Matrix(2, 2, lambda i, j: rq()), Matrix(2, 2, lambda i, j: rq())
        V1 = (-(J.inv() * U1.inv() * U2 * J * V2.T)).T          # solves U1 J V1^T + U2 J V2^T = 0
        assert U1 * J * V1.T + U2 * J * V2.T == sp.zeros(2, 2)
        ranks.append((kron(U1, V1) + kron(U2, V2)).rank())
        V1bad = Matrix(2, 2, lambda i, j: rq())
        ctrl.append((kron(U1, V1bad) + kron(U2, V2)).rank())
    out["T6 exact random instances: max rank F (must be <= 2)"] = max(ranks)
    out["T6 control without hypothesis: ranks seen"] = sorted(set(ctrl))

    Ns = [Matrix([[symbols("n%d_0" % d), symbols("n%d_1" % d)], [symbols("n%d_1" % d), symbols("n%d_2" % d)]]) for d in range(3)]
    Nc = [Matrix([[symbols("m%d_0" % d), symbols("m%d_1" % d)], [symbols("m%d_1" % d), symbols("m%d_2" % d)]]) for d in range(3)]
    Ys = [gen("Y%d_" % d) for d in range(3)]
    lhs = sum(((Ys[d] - Ys[d].T) * Nc[d] for d in range(3)), sp.zeros(2, 2))
    hyp1 = sum((Ys[d] * Nc[d].T for d in range(3)), sp.zeros(2, 2))          # Sum Y_d N_d^dag (N_d^dag = conj(N_d)^T)
    hyp2 = sum((Nc[d].T * Ys[d] for d in range(3)), sp.zeros(2, 2))          # Sum N_d^dag Y_d
    out["N1 sum (Y_d - Y_d^T) conj(N_d) == hyp1 - hyp2^T"] = sp.expand(lhs - (hyp1 - hyp2.T)) == sp.zeros(2, 2)
    out["all_ok"] = bool(all(v for k, v in out.items() if isinstance(v, bool))
                         and out["T6 exact random instances: max rank F (must be <= 2)"] <= 2
                         and 4 in out["T6 control without hypothesis: ranks seen"])
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "lemma_T_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
