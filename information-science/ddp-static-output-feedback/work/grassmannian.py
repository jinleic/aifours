"""Plant-derived graph-minor maps and complete two-port unstabilized synthesis.

No QE or nonlinear solver is used by synthesize_two_port. The returned radical
charts have explicit real domains and cover every gain, not only witnesses.
General port counts are supported by coefficient_maps, not by the closed
quadric synthesis theorem. See continuation-structural.md for proofs.
"""
from dataclasses import dataclass
from itertools import combinations

import sympy as sp


@dataclass(frozen=True)
class GraphSection:
    subsets: tuple
    variable: sp.Symbol
    denominator: sp.Matrix
    numerators: tuple
    linear_constraints: sp.Matrix
    m: int
    p: int

    def gain(self, delta):
        """Extract the finite gain on the normalized top-minor-one chart."""
        top = tuple(range(self.p))
        if sp.simplify(delta[self.subsets.index(top)] - 1) != 0:
            raise ValueError("The graph chart requires the top minor to equal one")
        return sp.Matrix(self.m, self.p, lambda i, j:
                         (-1)**(self.p-1-j) * delta[self.subsets.index(
                             tuple(k for k in top if k != j)+(self.p+i,))])

    def minors(self, gain):
        graph = sp.eye(self.p).col_join(gain)
        return sp.Matrix([graph[list(I), :].det() for I in self.subsets])

    def characteristic(self, delta):
        n = self.denominator.rows-1
        coefficients = self.denominator * delta
        return sp.expand(sum(coefficients[j]*self.variable**(n-j)
                             for j in range(n+1)))


def coefficient_maps(plant):
    """Build plant-only determinant coefficient maps, descending in s."""
    n, m, p, q, r = plant.dimensions
    s = sp.Symbol("s")
    subsets = tuple(combinations(range(p+m), p))
    state = (s*sp.eye(n)-plant.A).col_join(-plant.C1)
    ports = sp.zeros(n, p).row_join(-plant.B).col_join(
        sp.eye(p).row_join(sp.zeros(p, m)))
    denominator_polys = [sp.Poly(state.row_join(ports[:, list(I)]).det(), s)
                         for I in subsets]
    denominator = sp.Matrix(n+1, len(subsets), lambda j, k:
                            denominator_polys[k].nth(n-j))
    numerators = []
    constraint_rows = []
    for alpha in range(r):
        bordered_state = state.col_join(plant.C2[alpha, :])
        bordered_ports = ports.col_join(sp.zeros(1, p).row_join(plant.D2[alpha, :]))
        for beta in range(q):
            last = (-plant.E[:, beta]).col_join(-plant.D1[:, beta]).col_join(
                sp.Matrix([[plant.D22[alpha, beta]]]))
            polys = tuple(sp.Poly(bordered_state.row_join(
                bordered_ports[:, list(I)]).row_join(last).det(), s)
                for I in subsets)
            numerators.append(polys)
            constraint_rows.extend([[polynomial.nth(n-j) for polynomial in polys]
                                    for j in range(n+1)])
    return GraphSection(subsets, s, denominator, tuple(numerators),
                        sp.Matrix(constraint_rows), m, p)


def diagonal_congruence(matrix):
    """Return rational U,D with U invertible and U.T*matrix*U=D diagonal."""
    size = matrix.rows
    current, transform = sp.Matrix(matrix), sp.eye(size)
    if current != current.T:
        raise ValueError("Congruence input must be symmetric")
    for k in range(size):
        pivot = next((i for i in range(k, size) if current[i, i] != 0), None)
        if pivot is None:
            pair = next(((i, j) for i in range(k, size)
                         for j in range(i+1, size) if current[i, j] != 0), None)
            if pair is None:
                break
            i, j = pair
            change = sp.eye(size)
            change[j, i] = 1
            current = change.T*current*change
            transform = transform*change
            pivot = i
        if pivot != k:
            change = sp.eye(size)
            change.col_swap(k, pivot)
            current = change.T*current*change
            transform = transform*change
        change = sp.eye(size)
        for j in range(k+1, size):
            change[k, j] = -current[k, j]/current[k, k]
        current = change.T*current*change
        transform = transform*change
    return transform, current


def classify_quadric(polynomial, variables):
    """Classify every real zero and return complete charts plus a witness.

Each chart is {parameters: tuple, point: vector in the original variables,
nonnegative: tuple}. Its domain requires every listed expression >= 0.
Coefficients must be rational; no numerical sign decisions are made.
"""
    variables = tuple(variables)
    dimension = len(variables)
    polynomial = sp.expand(polynomial)
    if dimension:
        H = sp.hessian(polynomial, variables)/2
        origin = dict.fromkeys(variables, 0)
        g = sp.Matrix([sp.diff(polynomial, v).subs(origin)/2 for v in variables])
    else:
        H, g, origin = sp.zeros(0), sp.zeros(0, 1), {}
    constant = polynomial.subs(origin)
    if not all(value.is_Rational for value in [*H, *g, constant]):
        raise ValueError("Expected a quadratic polynomial with rational coefficients")
    if dimension:
        t = sp.Matrix(variables)
        if sp.expand((t.T*H*t)[0]+2*(g.T*t)[0]+constant-polynomial) != 0:
            raise ValueError("Expected degree at most two")
    U, D = diagonal_congruence(H)
    h = U.T*g
    shift = sp.Matrix([-h[i]/D[i, i] if D[i, i] != 0 else 0
                       for i in range(dimension)]) if dimension else sp.zeros(0, 1)
    rho = sp.expand(-constant+sum(h[i]**2/D[i, i] for i in range(dimension)
                                 if D[i, i] != 0))
    nonzero = [i for i in range(dimension) if D[i, i] != 0]
    null_linear = [i for i in range(dimension) if D[i, i] == 0 and h[i] != 0]
    positive = [i for i in nonzero if D[i, i] > 0]
    negative = [i for i in nonzero if D[i, i] < 0]
    result = {"H": H, "g": g, "constant": constant, "U": U, "D": D,
              "h": h, "shift": shift, "rho": rho,
              "inertia": (len(positive), len(negative), dimension-len(nonzero))}

    def convert(x):
        return (U*(x+shift)).applyfunc(sp.simplify)

    if null_linear:
        j = null_linear[0]
        indices = [i for i in range(dimension) if i != j]
        params = sp.symbols(f"v0:{len(indices)}", real=True)
        x = sp.zeros(dimension, 1)
        for i, value in zip(indices, params):
            x[i] = value
        other = sum(D[i, i]*x[i]**2 for i in nonzero)
        other += 2*sum(h[i]*x[i] for i in null_linear if i != j)
        x[j] = sp.expand((rho-other)/(2*h[j]))
        point = convert(x)
        result.update(feasible=True, kind="null-linear", charts=[
            {"parameters": params, "point": point, "nonnegative": ()}],
            witness=point.subs(dict.fromkeys(params, 0)))
        return result
    if not nonzero:
        feasible = rho == 0
        params = sp.symbols(f"v0:{dimension}", real=True)
        point = sp.Matrix(params) if dimension else sp.zeros(0, 1)
        result.update(feasible=feasible, kind="zero-form", charts=[
            {"parameters": params, "point": point, "nonnegative": ()}]
            if feasible else [], witness=sp.zeros(dimension, 1) if feasible else None)
        return result
    feasible = bool((positive and negative) or (positive and rho >= 0)
                    or (negative and rho <= 0))
    result.update(feasible=feasible, kind="central-quadric", charts=[], witness=None)
    if not feasible:
        return result
    j = next((i for i in nonzero if rho/D[i, i] >= 0), nonzero[0])
    indices = [i for i in range(dimension) if i != j]
    params = sp.symbols(f"v0:{len(indices)}", real=True)
    x = sp.zeros(dimension, 1)
    for i, value in zip(indices, params):
        x[i] = value
    radicand = sp.expand((rho-sum(D[i, i]*x[i]**2 for i in indices))/D[j, j])
    for sign in (1, -1):
        branch = x.copy()
        branch[j] = sign*sp.sqrt(radicand)
        result["charts"].append({"parameters": params, "point": convert(branch),
                                  "nonnegative": (radicand,)})
    witness = sp.zeros(dimension, 1)
    witness[j] = sp.sqrt(rho/D[j, j])
    result["witness"] = convert(witness)
    return result


def synthesize_two_port(plant):
    """Return all real DDP gains for m=p=2; no stability selection is asserted."""
    if plant.dimensions[1:3] != (2, 2):
        raise ValueError("The complete quadric synthesis theorem requires m=p=2")
    section = coefficient_maps(plant)
    equations = section.linear_constraints.col_join(sp.Matrix([[1, 0, 0, 0, 0, 0]]))
    rhs = sp.zeros(equations.rows, 1)
    rhs[-1] = 1
    result = {"section": section, "linear_matrix": equations, "linear_rhs": rhs}
    try:
        solution, parameters = equations.gauss_jordan_solve(rhs)
    except ValueError:
        certificate = next(v for v in equations.T.nullspace() if (v.T*rhs)[0] != 0)
        result.update(feasible=False, kind="linear-inconsistent",
                      linear_certificate=certificate, charts=[], witness=None)
        return result
    base = solution.subs(dict.fromkeys(parameters, 0))
    basis_vectors = equations.nullspace()
    basis = sp.Matrix.hstack(*basis_vectors) if basis_vectors else sp.zeros(6, 0)
    variables = sp.symbols(f"t0:{basis.cols}", real=True)
    delta = base+basis*sp.Matrix(variables) if variables else base
    polynomial = sp.expand(delta[0]*delta[5]-delta[1]*delta[4]+delta[2]*delta[3])
    quadric = classify_quadric(polynomial, variables)
    charts = []
    for chart in quadric["charts"]:
        d = base+basis*chart["point"]
        charts.append({"parameters": chart["parameters"],
                       "gain": section.gain(d), "delta": d,
                       "nonnegative": chart["nonnegative"]})
    witness_delta = base+basis*quadric["witness"] if quadric["feasible"] else None
    result.update(feasible=quadric["feasible"], kind=quadric["kind"], base=base,
                  basis=basis, variables=variables, quadric_polynomial=polynomial,
                  quadric=quadric, charts=charts,
                  witness=section.gain(witness_delta) if witness_delta is not None else None)
    return result
