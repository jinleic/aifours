"""Re-check of the single v1 item E4_mstar_eq_minus_beta_cot_psi, which FAILED in run e01-exact.

The v1 test was simplify(-tan(p) cot(pi - 2p) - (1 - tan(p)^2)/2) == 0. v1 and its output stay unchanged; this
script tests the same identity three other ways to decide whether the FAIL is mathematical or a simplifier miss:
(a) expand_trig (double-angle expansion) then simplify; (b) the double-angle formula alone;
(c) rewrite(exp) then simplify; (d) 50-digit mpmath evaluation at p = k pi/97, k = 1..48 (smoke only).
argv[1] = run directory; writes e4.json (exclusive create).
"""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
p = sp.symbols("p", positive=True)
expr = -sp.tan(p) * sp.cot(sp.pi - 2 * p) - (1 - sp.tan(p) ** 2) / 2
out = {"expr_as_parsed": str(expr)}
out["a_expand_trig_simplify_zero"] = bool(sp.simplify(sp.expand_trig(expr)) == 0)
out["b_double_angle_cot_zero"] = bool(sp.simplify(sp.expand_trig(sp.cot(2 * p)) - (1 - sp.tan(p) ** 2) / (2 * sp.tan(p))) == 0)
out["c_rewrite_exp_zero"] = bool(sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0)
mp.mp.dps = 50
worst = mp.mpf(0)
for k in range(1, 49):
    pv = k * mp.pi / 97
    val = -mp.tan(pv) * mp.cot(mp.pi - 2 * pv) - (1 - mp.tan(pv) ** 2) / 2
    worst = max(worst, abs(val))
out["d_numeric_worst_abs"] = mp.nstr(worst, 5)
out["verdict"] = ("identity holds; v1 FAIL is a sympy simplify miss" if (out["a_expand_trig_simplify_zero"]
                  or out["c_rewrite_exp_zero"]) else "UNRESOLVED")
with lane_guard.xopen(RUN + "/e4.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
