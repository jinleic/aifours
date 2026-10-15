"""Exact rational-input static-output-feedback DDP encodings.

This module is a research verifier, not a polynomial-time synthesis claim.
Z3's nonlinear-real solver uses exact arithmetic; unknown is never infeasible.
"""
from dataclasses import dataclass
import sympy as sp
import z3


@dataclass(frozen=True)
class Plant:
    A: sp.Matrix
    B: sp.Matrix
    E: sp.Matrix
    C1: sp.Matrix
    D1: sp.Matrix
    C2: sp.Matrix
    D2: sp.Matrix
    D22: sp.Matrix

    def __post_init__(self):
        n, m, p, q, r = self.dimensions
        expected = ((n, n), (n, m), (n, q), (p, n),
                    (p, q), (r, n), (r, m), (r, q))
        for name, shape in zip(self.__dataclass_fields__, expected):
            matrix = sp.Matrix(getattr(self, name))
            if matrix.shape != shape or not all(v.is_Rational for v in matrix):
                raise ValueError(f"{name}: expected rational matrix of shape {shape}")
            object.__setattr__(self, name, sp.ImmutableMatrix(matrix))
        if min(n, m, p, q, r) < 1:
            raise ValueError("All plant dimensions must be positive")

    @property
    def dimensions(self):
        return self.A.rows, self.B.cols, self.C1.rows, self.E.cols, self.C2.rows

    def gain(self):
        _, m, p, _, _ = self.dimensions
        return sp.Matrix(m, p, lambda i, j: sp.Symbol(f"k_{i}_{j}", real=True))

    def as_json(self):
        return {name: [[str(v) for v in row] for row in getattr(self, name).tolist()]
                for name in self.__dataclass_fields__}

    @classmethod
    def from_json(cls, data):
        return cls(**{name: sp.Matrix(data[name]) for name in cls.__dataclass_fields__})


def closed_loop(plant, gain):
    return (plant.A + plant.B * gain * plant.C1,
            plant.E + plant.B * gain * plant.D1,
            plant.C2 + plant.D2 * gain * plant.C1,
            plant.D22 + plant.D2 * gain * plant.D1)


def markov_equations(plant, gain):
    n = plant.A.rows
    M, G, F, J = closed_loop(plant, gain)
    equations = list(J)
    X = G
    for j in range(n):
        equations.extend(F * X)
        if j + 1 < n:
            X = M * X
    return [sp.expand(e) for e in equations]


def transfer_equations(plant, gain):
    """Independent numerator construction via adjugate, not Markov recursion."""
    M, G, F, J = closed_loop(plant, gain)
    s = sp.Symbol("s")
    pencil = s * sp.eye(M.rows) - M
    numerator = F * pencil.adjugate() * G + J * pencil.det()
    equations = []
    for entry in numerator:
        equations.extend(sp.Poly(sp.expand(entry), s).all_coeffs())
    return equations


def hurwitz_inequalities(matrix):
    """All leading Hurwitz determinants of a monic real characteristic polynomial."""
    n = matrix.rows
    coefficients = matrix.charpoly().all_coeffs()
    H = sp.Matrix(n, n, lambda i, j:
                  coefficients[2*j-i+1] if 0 <= 2*j-i+1 <= n else 0)
    return [sp.expand(H[:j, :j].det()) for j in range(1, n+1)]


def lyapunov_constraints(matrix):
    n = matrix.rows
    P = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"p_{min(i,j)}_{max(i,j)}", real=True))
    equations = list(matrix.T * P + P * matrix + sp.eye(n))
    positive = [sp.expand(P[:j, :j].det()) for j in range(1, n+1)]
    return equations, positive


def lifted_constraints(plant, gain, stable=False):
    """Degree-two encoding used for the existential-real size bound."""
    n, _, _, q, _ = plant.dimensions
    M, G, F, J = closed_loop(plant, gain)
    X = [sp.Matrix(n, q, lambda i, k: sp.Symbol(f"x_{j}_{i}_{k}", real=True))
         for j in range(n)]
    equations = list(J) + list(X[0] - G)
    for j in range(n):
        equations.extend(F * X[j])
        if j + 1 < n:
            equations.extend(X[j+1] - M * X[j])
    positive = []
    if stable:
        P = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"p_{min(i,j)}_{max(i,j)}", real=True))
        L = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"l_{i}_{j}", real=True) if j <= i else 0)
        equations.extend(P - L * L.T)
        equations.extend(M.T * P + P * M + sp.eye(n))
        positive.extend(L[i, i] for i in range(n))
    return [sp.expand(e) for e in equations], positive


def z3_polynomial(expression, variables):
    expression = sp.sympify(expression)
    if expression.is_Rational:
        return z3.RealVal(f"{expression.p}/{expression.q}")
    if expression.is_Symbol:
        return variables.setdefault(expression, z3.Real(str(expression)))
    if expression.is_Add:
        return z3.Sum(*(z3_polynomial(e, variables) for e in expression.args))
    if expression.is_Mul:
        result = z3.RealVal(1)
        for factor in expression.args:
            result *= z3_polynomial(factor, variables)
        return result
    if expression.is_Pow and expression.exp.is_Integer and expression.exp >= 0:
        return z3_polynomial(expression.base, variables) ** int(expression.exp)
    raise ValueError(f"Not a rational polynomial: {expression}")


def decide(equations, positive=(), timeout_ms=0):
    variables = {}
    constraints = [z3_polynomial(e, variables) == 0 for e in equations]
    constraints += [z3_polynomial(e, variables) > 0 for e in positive]
    solver = z3.SolverFor("QF_NRA")
    if timeout_ms:
        solver.set(timeout=timeout_ms)
    solver.add(*constraints)
    verdict = solver.check()
    if verdict == z3.unknown:
        raise RuntimeError("Unknown is not a decision: " + solver.reason_unknown())
    model = solver.model() if verdict == z3.sat else None
    if model is not None:
        if not all(z3.is_true(model.eval(c, model_completion=True)) for c in constraints):
            raise AssertionError("Exact model does not satisfy encoded constraints")
    witness = ({str(v): model.eval(zv, model_completion=True).sexpr()
                for v, zv in variables.items()} if model is not None else None)
    return verdict == z3.sat, witness, solver.to_smt2()


def fixed_subspace_rank_test(plant, T):
    n = plant.A.rows
    if T.rows != n or T.rank() != T.cols:
        raise ValueError("T must have full column rank and n rows")
    null = T.T.nullspace()
    N = sp.Matrix.vstack(*(v.T for v in null)) if null else sp.zeros(0, n)
    H = (N * plant.B).col_join(plant.D2)
    R = (plant.C1 * T).row_join(plant.D1)
    Q = (N * plant.A * T).row_join(N * plant.E).col_join(
        (plant.C2 * T).row_join(plant.D22))
    return R.col_join(Q).rank() == R.rank() and H.row_join(Q).rank() == H.rank()


def fixed_subspace_linear_test(plant, T):
    """Build the four original constraints, then solve the linear gain equations."""
    n = plant.A.rows
    null = T.T.nullspace()
    N = sp.Matrix.vstack(*(v.T for v in null)) if null else sp.zeros(0, n)
    K = plant.gain()
    M, G, F, J = closed_loop(plant, K)
    expressions = list(N * G) + list(N * M * T) + list(F * T) + list(J)
    coefficient, rhs = sp.linear_eq_to_matrix(expressions, list(K))
    return coefficient.rank() == coefficient.row_join(rhs).rank()
