# Static float-contamination audit of the desk's own checkers (v1)

Written 2026-10-18 ~05:56 PDT by ME3ParentPrimal after the parent note on Python-float contamination. Machine scan:
run `a01-float-audit` (`code/float_audit_v1.py`, AST scan, no import of the scanned code), output
`runs/a01-float-audit/RESULT.json`. Scanned files and sha256 at scan time:

| file | sha256 | role |
|---|---|---|
| code/p_core_v1.py | d003d0ba4f2e9b9be8a6dfa2e4c3aac3bc8dfeb610581c986089203bddb5a14e | CERTIFIED path (evaluator + coverage) |
| code/p_replay_v2.py | 77ccdf751fbbd404d8a34b11755f16f969ace4ce85b8ad67868755709c25fefe | driver of the full replay r01 |
| code/p_replay_v1.py | 700f5eb2b18c4a1948561c5395a80f422096400e40116d6b47046c33680b2eed | sample-only driver (s01) |
| code/red_checks_v1.py | 54e6e0c31bd6612a54be23fd8d708f16d0e611c347cf8876e9978548160661a4 | CERTIFIED exact reductions checks |
| code/d1_lower_v1.py | c8858b6aef74a067cdbdae4178e9c9033e79669d754d9a2894a0295b685c3150 | optional decimal v_cos lower certificate |
| code/p_controls_v1.py | 77a2418a8359eea8069eb96dbb1e55fad6536505ed4a29ed8e5815e39503d251 | mutation controls |
| code/p_formulas_v1.py | 5e6137b1f7c8e1e4f9bb0aa0ebfa18734b0dca6443654950a3488ca49766256b | exact sympy identities + diagnostics |

## Classification of every hit

**p_core_v1.py (certified): 0 float literals, 0 float() calls, 0 math uses.** All 7 true divisions:
* lines 90, 183, 184: `(lo + hi) / 2`, `(hi - lo) / 2` on box coordinates. Every coordinate is a `Fraction`
  (region via `parse_q` → `Fraction(int, int)`; `cell_box` = Fraction + Fraction·Fraction; `split` = Fraction/2),
  so these are exact `Fraction` divisions, never int/int.
* lines 169, 272: `1 / acb(...)` (int ÷ acb → acb ball).
* lines 194, 256: `rmi / (1 + r*r)` (acb ÷ arb → acb ball).
* Every rational enters Arb only through `qa(x) = arb(fmpq(x.numerator, x.denominator))`. A Python float has no
  `.numerator` attribute, so a float reaching `qa` raises `AttributeError` (fail-closed, cannot be silently used).
  All other Arb operands are Python ints (`1`, `2`, `k+1`, `dsign = ±1`), which python-flint converts exactly.
  Comparisons are certified ball comparisons against ints, `arb.pi()` or `qa(...)` balls.

**red_checks_v1.py (certified): 0 float literals, 0 float() calls, 0 math, mpmath not imported** (the single
"mpmath" hit is the docstring sentence saying it is not used). 26 divisions: sympy exact (Rational/symbolic:
lines 66, 67, 125, 153, 160, 176, 178, 188, 191, 196, 197, 208, 216, 217, 285), `Fraction` exact (lines 219, 222,
333) or Arb balls (lines 98, 245, 251, 274). Decimal constants (U, lo, hi, θ1 brackets, contract band) enter as
`Fraction("decimal string")` / `sp.Rational("...")` (exact).

**d1_lower_v1.py (optional certificate): 0 float literals/calls/math.** Divisions: Fraction (35, 37, 80, 83), Arb
(70). L is parsed as an exact `Fraction` from its decimal string.

**p_replay_v1/v2.py (drivers): no hit in a certified quantity.** `1.4` (RSS-cap guard), `float(sys.argv[10])`
(stop-time guard) and `float(G.lower())` etc. inside `diag` (informational text written to subdivisions.txt.gz
after the certification decision) are non-certifying. Boxes come from `Geometry` (Fractions); claims are decided
by `Evaluator.verify` / `verify_subdiv` only.

**p_controls_v1.py (controls): mpmath only for mutation construction** (choosing feasible-corner leaves, an
approximate θ1 to widen INFEAS boxes, rounding T′ upward), always converted to exact `Fraction`s; every
accept/reject decision is made by the Arb rules of p_core_v1. Division at line 235 is arb/arb.

**p_formulas_v1.py:** F1–F3 are exact sympy identities; F4/F6 are labelled diagnostics using mpmath
(`1j`, `mp.mpf(...)/int`, `0.0` report variable); F5 compares Arb point balls with 60-digit sympy values with an
Arb tolerance parsed from a string. None is a certificate step.

Conclusion: no int `/` producing a Python float, no float literal and no `math.*` occurs in any certified quantity
of the primal replay (p_core_v1 + p_replay_v2), the reductions checker (red_checks_v1) or the optional D1
certificate (d1_lower_v1).
