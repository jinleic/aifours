"""Reproduce bounded exact checks; no floating point is used for verdicts.

Run from the target directory with the pinned environment:
../../scratch/ai4s-ddp-static-output-feedback/venv/bin/python work/verify.py
"""
import hashlib
import itertools
import json
from pathlib import Path
import platform
import random
import sys
import time
from fractions import Fraction

import sympy as sp
import z3
from ddp_exact import (Plant, closed_loop, decide, fixed_subspace_linear_test,
                       fixed_subspace_rank_test, hurwitz_inequalities,
                       lifted_constraints, lyapunov_constraints,
                       markov_equations, transfer_equations, z3_polynomial)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence"
SEED = 20261014


def scalar_plant(values):
    return Plant(*(sp.Matrix([[v]]) for v in values))


def scalar_oracle(values, stable):
    """Analytic union of two affine root sets; independent of matrix encodings."""
    a, b, e, c1, d1, c2, d2, d22 = values
    for branch in (((d2*d1, d22), (d2*c1, c2)),
                   ((d2*d1, d22), (b*d1, e))):
        candidate = None
        possible = True
        for slope, intercept in branch:
            if slope == 0:
                possible &= intercept == 0
            else:
                root = Fraction(-intercept, slope)
                if candidate is not None and candidate != root:
                    possible = False
                candidate = root
        if possible:
            if not stable:
                return True
            if candidate is None:
                if b*c1 != 0 or a < 0:
                    return True
            elif a+b*c1*candidate < 0:
                return True
    return False


def exhaustive_scalars():
    digest = hashlib.sha256()
    counts = {"plants": 0, "ddp_sat": 0, "stable_ddp_sat": 0}
    for values in itertools.product((-1, 0, 1), repeat=8):
        plant = scalar_plant(values)
        K = plant.gain()
        equations = markov_equations(plant, K)
        M = closed_loop(plant, K)[0]
        results = []
        for stable in (False, True):
            positive = hurwitz_inequalities(M) if stable else []
            actual, _, _ = decide(equations, positive, timeout_ms=10000)
            expected = scalar_oracle(values, stable)
            assert actual == expected, (values, stable, actual, expected)
            results.append(actual)
        # In one state, the only candidate subspaces are {0} and R.
        geometric = any(fixed_subspace_rank_test(plant, T)
                        for T in (sp.zeros(1, 0), sp.eye(1)))
        assert geometric == results[0], (values, "rank condition")
        counts["plants"] += 1
        counts["ddp_sat"] += results[0]
        counts["stable_ddp_sat"] += results[1]
        digest.update(json.dumps([values, results], separators=(",", ":")).encode())
    counts["decision_digest_sha256"] = digest.hexdigest()
    counts["checks"] = "All 3^8 scalar plants; two solver decisions and two fixed-V rank tests per plant"
    return counts


def random_matrix(rng, rows, cols):
    return sp.Matrix(rows, cols, lambda i, j: rng.choice((-2, -1, 0, 1, 2)))


def random_plant(rng, n, m, p, q=1, r=1):
    shapes = ((n, n), (n, m), (n, q), (p, n),
              (p, q), (r, n), (r, m), (r, q))
    return Plant(*(random_matrix(rng, *shape) for shape in shapes))


def symbolic_equivalence(plant, K):
    variables = {}
    markov = z3.And(*(z3_polynomial(e, variables) == 0 for e in markov_equations(plant, K)))
    numerator = z3.And(*(z3_polynomial(e, variables) == 0 for e in transfer_equations(plant, K)))
    solver = z3.SolverFor("QF_NRA")
    solver.set(timeout=30000)
    solver.add(z3.Xor(markov, numerator))
    verdict = solver.check()
    assert verdict == z3.unsat, ("Universal equivalence failed/unknown", verdict)


def check_case(name, plant, expected=None, include_lifted=False):
    K = plant.gain()
    M = closed_loop(plant, K)[0]
    equations = markov_equations(plant, K)
    numerator = transfer_equations(plant, K)
    symbolic_equivalence(plant, K)
    ddp, witness, smt = decide(equations, timeout_ms=30000)
    direct, _, _ = decide(numerator, timeout_ms=30000)
    assert ddp == direct
    stable, stable_witness, smt_stable = decide(equations, hurwitz_inequalities(M), timeout_ms=30000)
    leq, lpositive = lyapunov_constraints(M)
    lyapunov_strategy = "unrestricted alternate encoding"
    try:
        lyapunov, _, _ = decide(numerator+leq, lpositive, timeout_ms=30000)
    except RuntimeError as error:
        if not str(error).startswith("Unknown is not a decision: timeout"):
            raise
        # These exact, redundant cuts preserve the feasible set. The fallback
        # is joint-certificate evidence, not an independent stability decision.
        lyapunov_strategy = "timeout retained; exact retry with redundant Hurwitz cuts"
        lyapunov, _, _ = decide(numerator+leq, lpositive+hurwitz_inequalities(M), timeout_ms=30000)
    assert stable == lyapunov, (name, "Hurwitz versus Lyapunov")
    if expected is not None:
        assert (ddp, stable) == expected, (name, ddp, stable, expected)
    if include_lifted:
        for stable_flag in (False, True):
            leq, lpos = lifted_constraints(plant, K, stable_flag)
            variables = set().union(*(e.free_symbols for e in leq+lpos))
            assert all(sp.Poly(e, *sorted(variables, key=str)).total_degree() <= 2 for e in leq+lpos)
            lifted, _, _ = decide(leq, lpos, timeout_ms=30000)
            assert lifted == (stable if stable_flag else ddp)
    (OUT / f"{name}.smt2").write_text("(set-logic QF_NRA)\n" + smt)
    (OUT / f"{name}-stable.smt2").write_text("(set-logic QF_NRA)\n" + smt_stable)
    return {"name": name, "plant": plant.as_json(), "ddp": ddp, "stable_ddp": stable,
            "gain_and_auxiliary_witness": witness, "stable_witness": stable_witness,
            "symbolic_markov_equations": [str(e) for e in equations],
            "transfer_numerator_coefficients": [str(e) for e in numerator],
            "hurwitz_minors": [str(e) for e in hurwitz_inequalities(M)],
            "universal_markov_numerator_xor": "unsat", "lyapunov_agrees": True,
            "lyapunov_strategy": lyapunov_strategy,
            "lifted_checked": include_lifted}


def named_cases():
    cases = []
    cases.append(("feedthrough-cancellation", scalar_plant((-1, 1, 1, 0, 1, 1, 1, 1)), (True, True)))
    cases.append(("incompatible-common-gain", scalar_plant((-1, 1, 1, 0, 1, 1, 1, 0)), (False, False)))
    cases.append(("strict-stability-boundary", scalar_plant((0, 0, 0, 1, 0, 0, 0, 0)), (True, False)))
    n = 2
    zero = sp.zeros
    cases.append(("last-markov-essential", Plant(sp.Matrix([[-1, 1], [0, -2]]), zero(n, 1),
        sp.Matrix([0, 1]), zero(1, n), zero(1, 1), sp.Matrix([[1, 0]]), zero(1, 1), zero(1, 1)), (False, False)))
    cases.append(("hidden-unstable-mode", Plant(sp.diag(-1, 1), zero(n, 1),
        sp.Matrix([1, 0]), zero(1, n), zero(1, 1), sp.Matrix([[0, 1]]), zero(1, 1), zero(1, 1)), (True, False)))
    A = sp.Matrix([[-1, 1, 0], [0, -2, 1], [0, 0, -3]])
    B = sp.Matrix([[1, 0], [0, 1], [0, 0]])
    C1 = sp.Matrix([[0, 1, 0], [0, 0, 1]])
    cases.append(("noninvertible-two-branches", Plant(A, B, sp.Matrix([0, 0, 1]), C1,
        zero(2, 1), sp.Matrix([[1, 0, 0]]), zero(1, 2), zero(1, 1)), (True, True)))
    cases.append(("noninvertible-infeasible", Plant(A, B, sp.Matrix([1, 0, 0]), C1,
        zero(2, 1), sp.Matrix([[1, 0, 0]]), zero(1, 2), zero(1, 1)), (False, False)))
    return [check_case(name, plant, expected, include_lifted=True) for name, plant, expected in cases]


def random_cases():
    rng = random.Random(SEED)
    records = []
    for i in range(32):
        n = 2 if i < 24 else 3
        m = 1 if i % 3 else 2
        p = 1 if i % 4 else 2
        plant = random_plant(rng, n, m, p)
        records.append(check_case(f"random-{i:02}", plant))
    return records


def fixed_subspace_checks():
    rng = random.Random(SEED+1)
    rows = []
    for i in range(256):
        n = 1 + i % 4
        m, p = 1+i%2, 1+(i//2)%2
        q, r = 1+(i//4)%2, 1+(i//8)%2
        plant = random_plant(rng, n, m, p, q, r)
        d = i % (n+1)
        while True:
            T = random_matrix(rng, n, d)
            if T.rank() == d:
                break
        rank_test = fixed_subspace_rank_test(plant, T)
        linear_test = fixed_subspace_linear_test(plant, T)
        assert rank_test == linear_test, (i, plant.as_json(), T)
        rows.append({"index": i, "dimensions": plant.dimensions, "dimension_V": d,
                     "feasible": rank_test, "T": [[str(x) for x in row] for row in T.tolist()]})
    return rows


def lattice_and_mutation_checks():
    A = sp.Matrix([[0, 0, 0], [0, 0, 0], [1, -1, 0]])
    plant = Plant(A, sp.Matrix([0, 0, 1]), sp.zeros(3, 1), sp.Matrix([[1, 1, 0]]),
                  sp.zeros(1, 1), sp.Matrix([[0, 0, 1]]), sp.zeros(1, 1), sp.zeros(1, 1))
    tests = [(sp.eye(3)[:, :1], True), (sp.eye(3)[:, 1:2], True), (sp.eye(3)[:, :2], False)]
    for T, expected in tests:
        assert fixed_subspace_rank_test(plant, T) == expected
        assert fixed_subspace_linear_test(plant, T) == expected
    # Detect the two easy modeling mistakes with exact negative controls.
    essential = Plant(sp.Matrix([[-1, 1], [0, -2]]), sp.zeros(2, 1), sp.Matrix([0, 1]),
                      sp.zeros(1, 2), sp.zeros(1, 1), sp.Matrix([[1, 0]]), sp.zeros(1, 1), sp.zeros(1, 1))
    M, G, F, J = closed_loop(essential, essential.gain())
    assert decide(list(J)+list(F*G))[0] is True
    assert decide(markov_equations(essential, essential.gain()))[0] is False
    direct = scalar_plant((-1, 0, 0, 0, 0, 0, 0, 1))
    equations = markov_equations(direct, direct.gain())
    assert decide(equations[1:])[0] is True and decide(equations)[0] is False
    k = sp.Symbol("nonreal_k", real=True)
    assert decide([k*k+1])[0] is False
    return {"lattice": [True, True, False], "omitting_last_markov_detected": True,
            "omitting_feedthrough_detected": True, "real_not_complex_feasibility_checked": True}


def main():
    start = time.monotonic()
    OUT.mkdir(exist_ok=True)
    result = {"command": f"{sys.executable} {Path(__file__).resolve()}",
              "seed": SEED, "python": platform.python_version(), "sympy": sp.__version__,
              "z3": z3.get_version_string(), "scope": "bounded exact small-instance validation, not a performance campaign"}
    result["adversarial"] = named_cases()
    result["random"] = random_cases()
    result["fixed_subspaces"] = fixed_subspace_checks()
    result["negative_controls"] = lattice_and_mutation_checks()
    result["exhaustive_scalars"] = exhaustive_scalars()
    result["elapsed_seconds"] = round(time.monotonic()-start, 3)
    result["outcome"] = "PASS"
    result["script_sha256"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in (ROOT/"work/ddp_exact.py", ROOT/"work/verify.py")}
    (OUT/"verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in ("outcome", "exhaustive_scalars", "elapsed_seconds", "python", "sympy", "z3")}, indent=2))


if __name__ == "__main__":
    main()
