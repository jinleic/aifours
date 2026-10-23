"""Exact check for reductions-v3 (fix of reductions-v2 LF373; finding 5 of review me3-charts-v2-delta-codex-v1.note.md,
sha256 df03a74a1be4f5c50d931463507f7e2859010b96ca0e60895167dcd2fe2ce474).  SymPy exact integers/rationals only, no floats.
q = x^3 - 9x^2 + 18x - 6,  g = 24y - x(9 - x)^2 + 24,  h = 32y^3 - 144y^2 + 135y - 27.
(a) Res_x(q, g) - 432 h == 0 (sp.resultant, and independently the 6x6 Sylvester determinant);
(b) Res / LC_y(Res) == h/32 (monic normalization);  (c) WRONG CONTROL: the v2 wording "Res == h/32" must be False;
(d) LC_y(Res) == 24^3 == 13824.
"""
import os
import sys
import ast
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402

RUN = sys.argv[1]
with open(os.path.abspath(__file__)) as fh:
    _tree = ast.parse(fh.read())
_bad = [n.lineno for n in ast.walk(_tree)
        if isinstance(n, ast.Constant) and not isinstance(n.value, (bool, int, str, type(None)))]
assert not _bad, _bad

x, y = sp.symbols("x y")
q = x ** 3 - 9 * x ** 2 + 18 * x - 6
g = 24 * y - x * (9 - x) ** 2 + 24
h = 32 * y ** 3 - 144 * y ** 2 + 135 * y - 27
R = sp.expand(sp.resultant(q, g, x))
cq = sp.Poly(q, x).all_coeffs()
cg = sp.Poly(g, x).all_coeffs()
syl = sp.Matrix([[0] * i + cq + [0] * (2 - i) for i in range(3)] + [[0] * i + cg + [0] * (2 - i) for i in range(3)])
D = sp.expand(syl.det())
PR = sp.Poly(R, y)
wrong = sp.expand(R - h / 32) == 0
checks = {
    "a_Res_minus_432h_eq_0": sp.expand(R - 432 * h) == 0,
    "a_Sylvester_det_minus_432h_eq_0": sp.expand(D - 432 * h) == 0,
    "b_monic_Res_eq_h/32": sp.expand(PR.monic().as_expr() - h / 32) == 0,
    "c_WRONG_CONTROL_v2_wording_Res_eq_h/32_evaluates_False": wrong is False,
    "d_LC_y_Res_eq_24^3_eq_13824": PR.LC() == 24 ** 3 == 13824,
}
out = {"script": "resultant_check_v1.py", "label": "EXACT (sympy integers/rationals; no floats)",
       "Res_x(q,g)": str(R), "sylvester_det": str(D), "432*h": str(sp.expand(432 * h)),
       "monic_Res": str(PR.monic().as_expr()), "LC_y_Res": str(PR.LC()),
       "wrong_control_v2_wording": {"claim": "Res == h/32", "evaluates": wrong,
                                    "residual_Res_minus_h/32": str(sp.expand(R - h / 32))},
       "checks": checks, "all_pass": all(checks.values())}
with lane_guard.xopen(os.path.join(RUN, "resultant_check.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "checks": checks, "LC_y_Res": out["LC_y_Res"]}))
sys.exit(0 if out["all_pass"] else 1)
