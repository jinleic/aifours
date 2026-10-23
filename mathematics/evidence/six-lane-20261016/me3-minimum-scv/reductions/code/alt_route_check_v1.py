"""Exact check for reductions-v4 Remark 5.6a (alternative hand route of review me3-reductions-claude-v1, MINOR-2).
Fractions (decisions) + SymPy (one symbolic derivative); no floats.
(a) (1/4 - 1/25)/(1 + 1/25) == 21/104;  (b) 21/104 > 773/3844 (21*3844 = 80724 > 80392 = 773*104);
(c) d/dw [(1/4 - w^2)/(1 + w^2)] == -(5/2) w/(1 + w^2)^2 (decreasing for w > 0);  (d) 21/104 > 0.20090156350055;
(e) WRONG CONTROL: with only Delta3 > 1/4 the omega <= 1/4 tail gives (1/4 - 1/16)/(1 + 1/16) = 3/17, and the claim
    "3/17 > 773/3844" must be False (why the hand route needs the tail omega <= 1/5).
"""
import os
import sys
import ast
import json
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402

RUN = sys.argv[1]
with open(os.path.abspath(__file__)) as fh:
    _tree = ast.parse(fh.read())
_bad = [n.lineno for n in ast.walk(_tree)
        if isinstance(n, ast.Constant) and not isinstance(n.value, (bool, int, str, type(None)))]
assert not _bad, _bad

V = Fr(773, 3844)
tail15 = (Fr(1, 4) - Fr(1, 25)) / (1 + Fr(1, 25))
tail14 = (Fr(1, 4) - Fr(1, 16)) / (1 + Fr(1, 16))
w = sp.Symbol("w", positive=True)
dexpr = sp.simplify(sp.diff((sp.Rational(1, 4) - w ** 2) / (1 + w ** 2), w) + sp.Rational(5, 2) * w / (1 + w ** 2) ** 2)
wrong = tail14 > V
checks = {
    "a_tail_at_1/5_eq_21/104": tail15 == Fr(21, 104),
    "b_21/104_gt_773/3844": tail15 > V and 21 * 3844 == 80724 and 773 * 104 == 80392 and 80724 > 80392,
    "c_derivative_identity": dexpr == 0,
    "d_21/104_gt_L_0.20090156350055": tail15 > Fr(20090156350055, 10 ** 14),
    "e_WRONG_CONTROL_3/17_gt_773/3844_is_False": tail14 == Fr(3, 17) and wrong is False,
}
out = {"script": "alt_route_check_v1.py", "label": "EXACT (Fractions; one SymPy derivative identity)",
       "tail_omega<=1/5": str(tail15), "tail_omega<=1/4_with_Delta3>1/4_only": str(tail14),
       "wrong_control_evaluates": wrong, "derivative_residual": str(dexpr), "checks": checks,
       "all_pass": all(checks.values())}
with lane_guard.xopen(os.path.join(RUN, "alt_route_check.json")) as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"all_pass": out["all_pass"], "checks": checks}))
sys.exit(0 if out["all_pass"] else 1)
