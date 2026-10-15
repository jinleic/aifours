"""Bounded exact structural assay; run once after the proof stabilizes."""
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

import sympy as sp

from ddp_exact import (Plant, closed_loop, decide, fixed_subspace_linear_test,
                       fixed_subspace_rank_test, hurwitz_inequalities)
from grassmannian import coefficient_maps, classify_quadric, synthesize_two_port

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence/continuation"


def assert_zero(expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    assert all(sp.simplify(value) == 0 for value in entries), expression


def serial(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(v) for v in row] for row in value.tolist()]
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    if isinstance(value, sp.Basic):
        return str(value)
    return value


def curve_plant(hidden=None):
    if hidden is None:
        A, B, C1, E, C2 = -sp.eye(2), sp.eye(2), sp.eye(2), sp.Matrix([0, 1]), sp.Matrix([[1, 0]])
    else:
        A = sp.diag(-1, -1, hidden)
        B, C1 = sp.eye(3)[:, :2], sp.eye(3)[:2, :]
        E, C2 = sp.Matrix([0, 1, 0]), sp.Matrix([[1, 0, 0]])
    return Plant(A, B, E, C1, sp.Matrix([1, 0]), C2,
                 sp.Matrix([[0, 1]]), sp.zeros(1, 1))


def nonreal_plant():
    A = sp.Matrix([[-1, 0, 0, 1], [0, -1, -1, 0],
                   [1, 0, -1, 0], [0, 1, 0, -1]])
    return Plant(A, sp.eye(4)[:, :2], sp.Matrix([0, 1, 0, 0]),
                 sp.eye(4)[:2, :], sp.Matrix([1, 0]), sp.Matrix([[1, 0, 0, 0]]),
                 sp.Matrix([[0, 1]]), sp.zeros(1, 1))


def direct_identity(name, plant):
    """Use adjugate transfer construction, not the bordered determinant formula."""
    section = coefficient_maps(plant)
    K = plant.gain()
    delta = section.minors(K)
    assert_zero(section.gain(delta)-K)
    M, G, F, J = closed_loop(plant, K)
    s = section.variable
    pencil = s*sp.eye(M.rows)-M
    characteristic = sp.expand(pencil.det())
    assert_zero(section.characteristic(delta)-characteristic)
    independent = F*pencil.adjugate()*G+J*characteristic
    reconstructed = []
    for k, polynomials in enumerate(section.numerators):
        value = sp.expand(sum(poly.as_expr()*delta[i]
                              for i, poly in enumerate(polynomials)))
        assert_zero(value-independent[k])
        reconstructed.append(value)
    assert characteristic.coeff(s, M.rows) == 1
    return {"name": name, "plant": plant.as_json(),
            "coordinates": len(section.subsets), "all_symbolic_gains": True,
            "full_characteristic": characteristic,
            "numerators": reconstructed, "result": "exact polynomial identities"}


def dense_fixtures():
    A = sp.Matrix([[-2, 1], [-1, -3]])
    return [
        ("dense-all-feedthrough", Plant(A, sp.Matrix([[1, 2], [0, 1]]),
            sp.Matrix([[1, 1], [0, 2]]), sp.Matrix([[2, -1], [1, 1]]),
            sp.Matrix([[1, 2], [3, 1]]), sp.Matrix([[1, 0], [-1, 2]]),
            sp.Matrix([[2, 1], [1, -1]]), sp.Matrix([[1, 2], [-2, 0]]))),
        ("rectangular-p3-m2", Plant(A, sp.eye(2), sp.Matrix([1, 2]),
            sp.Matrix([[1, 0], [0, 1], [1, -1]]), sp.Matrix([1, 2, -1]),
            sp.Matrix([[1, -1]]), sp.Matrix([[1, 2]]), sp.Matrix([[3]]))),
        ("rectangular-p2-m3", Plant(A, sp.Matrix([[1, 0, 2], [0, 1, 1]]),
            sp.Matrix([1, 2]), sp.eye(2), sp.Matrix([1, 2]),
            sp.Matrix([[1, -1]]), sp.Matrix([[1, 2, -1]]), sp.Matrix([[3]])))
    ]


def check_lattice():
    plant = Plant(sp.Matrix([[0, 0, 0], [0, 0, 0], [1, -1, 0]]),
                  sp.Matrix([0, 0, 1]), sp.zeros(3, 1), sp.Matrix([[1, 1, 0]]),
                  sp.zeros(1, 1), sp.Matrix([[0, 0, 1]]), sp.zeros(1, 1), sp.zeros(1, 1))
    values = []
    for T, expected in [(sp.eye(3)[:, :1], True), (sp.eye(3)[:, 1:2], True),
                        (sp.eye(3)[:, :2], False)]:
        rank = fixed_subspace_rank_test(plant, T)
        direct = fixed_subspace_linear_test(plant, T)
        assert rank == direct == expected
        values.append(expected)
    return {"line1_line2_sum": values, "plant": plant.as_json()}


def check_quadric_branches():
    x, y, z = sp.symbols("x y z", real=True)
    cases = [
        ("null-linear", x*x+2*y+3, (x, y), True),
        ("zero-form-all", 0, (x, y), True),
        ("zero-form-empty", 1, (x, y), False),
        ("psd-positive-level", x*x+2*y*y-3, (x, y), True),
        ("psd-zero-level", (x+y)**2, (x, y), True),
        ("psd-negative-level", x*x+y*y+1, (x, y), False),
        ("nsd-negative-level", -x*x-2*y*y+3, (x, y), True),
        ("nsd-positive-level", -x*x-y*y-1, (x, y), False),
        ("indefinite-zero-diagonal", 2*x*y+2*x+4*y+5, (x, y), True),
        ("singular-range-linear", (x+y)**2+2*x+2*y+z*0-2, (x, y, z), True),
        ("zero-dimensional-point", 0, (), True),
        ("zero-dimensional-empty", 1, (), False)
    ]
    results = []
    for name, f, variables, expected in cases:
        f = sp.sympify(f)
        result = classify_quadric(f, variables)
        assert result["feasible"] == expected, name
        assert_zero(result["U"].T*result["H"]*result["U"]-result["D"])
        if variables:
            assert result["U"].det() != 0
        if expected:
            assert_zero(f.subs(dict(zip(variables, result["witness"]))))
            for chart in result["charts"]:
                assert_zero(f.subs(dict(zip(variables, chart["point"])), simultaneous=True))
        else:
            assert decide([f])[0] is False
        results.append({"name": name, "polynomial": f, "variables": variables,
                        "classification": result})
    return results


def check_two_port(plant, expected):
    result = synthesize_two_port(plant)
    assert result["feasible"] == expected
    if result["kind"] == "linear-inconsistent":
        certificate = result["linear_certificate"]
        assert_zero(certificate.T*result["linear_matrix"])
        assert (certificate.T*result["linear_rhs"])[0] != 0
    else:
        assert_zero(result["linear_matrix"]*result["base"]-result["linear_rhs"])
        assert_zero(result["linear_matrix"]*result["basis"])
        for chart in result["charts"]:
            assert_zero(result["section"].minors(chart["gain"])-chart["delta"])
            assert_zero(result["linear_matrix"]*chart["delta"]-result["linear_rhs"])
    if expected:
        K = result["witness"]
        M, G, F, J = closed_loop(plant, K)
        s = sp.Symbol("s")
        assert_zero(F*(s*sp.eye(M.rows)-M).adjugate()*G+J*(s*sp.eye(M.rows)-M).det())
    return {key: value for key, value in result.items() if key != "section"}


def check_curve_and_hidden():
    a = sp.Symbol("a", real=True)
    K = sp.Matrix([[a, -2*a*a], [0, -a]])
    plant = curve_plant()
    M, G, F, J = closed_loop(plant, K)
    assert_zero(G-sp.Matrix([a, 1]))
    assert_zero(F-sp.Matrix([[1, -a]]))
    assert_zero(M*G-(-1-a)*G)
    assert G.rank() == F.rank() == 1
    assert_zero(F*G)
    assert F.cols-F.rank() == G.cols
    determinants = hurwitz_inequalities(M)
    assert_zero(determinants[0]-2)
    assert_zero(determinants[1]-2*(1-a*a))
    assert decide([], [*determinants, a-1])[0] is False
    assert decide([], [*determinants, -1-a])[0] is False
    for endpoint in (-1, 1):
        assert not all(d.subs(a, endpoint) > 0 for d in determinants)
    for witness in (sp.Rational(-1, 2), 0, sp.Rational(1, 2)):
        assert all(d.subs(a, witness) > 0 for d in determinants)
    # State-order irreducibility evidence: both output-nulling free-input pairs
    # are controllable; no invariant-zero or output-visible state remains.
    A_friend = sp.Matrix([[-1, 0], [-1, -1]])
    free_B = sp.Matrix([1, 0])
    dual_friend = sp.Matrix([[-1, -1], [0, -1]])
    dual_free = sp.Matrix([0, 1])
    assert free_B.row_join(A_friend*free_B).det() != 0
    assert dual_free.row_join(dual_friend*dual_free).det() != 0
    hidden = []
    for h in (-1, 0, 1):
        P = curve_plant(h)
        Mh, Gh, Fh, Jh = closed_loop(P, K)
        s = sp.Symbol("s")
        characteristic = (s*sp.eye(3)-Mh).det()
        assert_zero(characteristic-(s-h)*((s+1)**2-a*a))
        assert_zero(Fh*(s*sp.eye(3)-Mh).adjugate()*Gh+Jh*characteristic)
        inequalities = hurwitz_inequalities(Mh)
        feasible, witness, smt = decide([], inequalities)
        assert feasible == (h < 0)
        (OUT/f"hidden-mode-{h}-stable.smt2").write_text(smt)
        hidden.append({"hidden_eigenvalue": h, "stable_feasible": feasible,
                       "characteristic": characteristic,
                       "hurwitz_minors": inequalities, "witness": witness})
    return {"all_gains": K, "unique_admissible_basis": G, "output_row": F,
            "hurwitz_minors": determinants, "stable_interval": "-1<a<1",
            "hidden_modes": hidden}


def check_nonreal():
    plant = nonreal_plant()
    result = check_two_port(plant, False)
    a = sp.Symbol("a", real=True)
    K = sp.Matrix([[a, -2*a*a], [0, -a]])
    M, G, F, J = closed_loop(plant, K)
    s = sp.Symbol("s")
    numerator = sp.expand((F*(s*sp.eye(4)-M).adjugate()*G+J*(s*sp.eye(4)-M).det())[0])
    assert_zero(numerator-(a*a+1)*(s+1))
    assert_zero(numerator.subs(a, sp.I))
    feasible, _, smt = decide([a*a+1])
    assert feasible is False
    (OUT/"real-infeasible-quadric.smt2").write_text(smt)
    return {"plant": plant.as_json(), "synthesis": result,
            "reduced_numerator": sp.factor(numerator),
            "complex_gain": K.subs(a, sp.I), "real_certificate": "a^2+1>0 for all real a"}


def main():
    start = time.monotonic()
    result = {"date_pt": "2026-10-14", "scope": "bounded symbolic proof/counterexample assay",
              "command": f"{sys.executable} {Path(__file__).resolve()}",
              "python": platform.python_version(), "sympy": sp.__version__,
              "blas_threads": 1, "kernel_proof": False}
    # The lattice falsification is performed first, not assumed away.
    result["old_lattice"] = check_lattice()
    fixtures = dense_fixtures()
    result["symbolic_identities"] = [direct_identity(name, plant) for name, plant in
        fixtures+[("continuum-curve", curve_plant()), ("real-infeasible", nonreal_plant())]]
    result["quadratic_branches"] = check_quadric_branches()
    result["curve_synthesis"] = check_two_port(curve_plant(), True)
    result["curve_and_hidden_modes"] = check_curve_and_hidden()
    result["real_infeasibility"] = check_nonreal()
    result["linear_infeasibility"] = check_two_port(fixtures[0][1], False)
    # Degenerate all-gain class and unique finite gain exercise d=5 and d=0.
    all_gain = Plant(-sp.eye(2), sp.eye(2), sp.zeros(2, 1), sp.eye(2),
                     sp.zeros(2, 1), sp.zeros(1, 2), sp.zeros(1, 2), sp.zeros(1, 1))
    unique_gain = Plant(-2*sp.eye(2), sp.eye(2), -sp.eye(2), sp.eye(2),
                        sp.eye(2), sp.zeros(2), sp.eye(2), -sp.eye(2))
    result["all_gain_synthesis"] = check_two_port(all_gain, True)
    result["unique_gain_synthesis"] = check_two_port(unique_gain, True)
    assert_zero(sp.Matrix(result["unique_gain_synthesis"]["witness"])-sp.eye(2))
    assert result["all_gain_synthesis"]["basis"].cols == 5
    assert result["unique_gain_synthesis"]["basis"].cols == 0
    paths = [ROOT/"work/grassmannian.py", ROOT/"work/verify_continuation.py",
             ROOT/"work/continuation-structural.md", OUT/"protocol.json",
             ROOT/"sources/papers/chen-2000.pdf",
             ROOT/"sources/papers/gorla-rosenthal-2009-v1.pdf",
             ROOT/"sources/papers/eremenko-gabrielov-real-feedback.pdf"]
    result["sha256"] = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in paths}
    result["elapsed_seconds"] = round(time.monotonic()-start, 3)
    result["outcome"] = "PASS"
    (OUT/"verification.json").write_text(json.dumps(serial(result), indent=2)+"\n")
    print(json.dumps({"outcome": "PASS", "symbolic_plants": len(result["symbolic_identities"]),
                      "quadric_branches": len(result["quadratic_branches"]),
                      "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
