"""Control (f'): exact symbolic verification of the function code used by the certified B&B ctl_f_d1bnb_v1.py.

The functions F_ball and grad_ball are extracted VERBATIM (Python AST) from ctl_f_d1bnb_v1.py (whose sha256 is
recorded in the output) and executed on sympy expressions through a thin wrapper class, so the check binds the exact
code that ran.  Checks (CERTIFIED = exact sympy):
  (g1) grad_ball(w, u) == (dF/dw, dF/du) of F_ball(w, u), as symbolic identities (0 < u < 2, w > 0);
  (g2) F_ball(w, u) + 1 == m0 m2 / m1^2 for the D1 closed-form moments of Lemma 5.3 with C = 1 - u and the minimizing
       sign S = -sqrt(u (2 - u)):  m0 = 1 - q (C - w S), m1 = 1 - q C, m2 = 2 (1 - q^2 (C + w S)), q = 1/(1 + w^2);
  (g3) spot checks of (g1), (g2) at rational points with 60-digit evaluation (redundant safety net).
The wrapper maps x.nonnegative_part() to the identity, valid because the only argument is u (2 - u) >= 0 on [0, 2].
"""
import os
import sys
import ast
import json
import time
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402

RUN = sys.argv[1]
T0 = time.time()
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ctl_f_d1bnb_v1.py")
with open(SRC, "rb") as fh:
    raw = fh.read()
src_sha = hashlib.sha256(raw).hexdigest()
tree = ast.parse(raw.decode())
funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ("F_ball", "grad_ball")]
mod = ast.Module(body=funcs, type_ignores=[])
ns = {}
exec(compile(mod, SRC, "exec"), ns)


class Sym:
    __slots__ = ("e",)

    def __init__(self, e):
        self.e = sp.sympify(e)

    @staticmethod
    def _v(o):
        return o.e if isinstance(o, Sym) else sp.sympify(o)

    def __add__(self, o):
        return Sym(self.e + Sym._v(o))

    __radd__ = __add__

    def __sub__(self, o):
        return Sym(self.e - Sym._v(o))

    def __rsub__(self, o):
        return Sym(Sym._v(o) - self.e)

    def __mul__(self, o):
        return Sym(self.e * Sym._v(o))

    __rmul__ = __mul__

    def __truediv__(self, o):
        return Sym(self.e / Sym._v(o))

    def __rtruediv__(self, o):
        return Sym(Sym._v(o) / self.e)

    def __neg__(self):
        return Sym(-self.e)

    def sqrt(self):
        return Sym(sp.sqrt(self.e))

    def nonnegative_part(self):
        return Sym(self.e)


w, u = sp.symbols("w u", positive=True)
F = ns["F_ball"](Sym(w), Sym(u)).e
gw, gu = ns["grad_ball"](Sym(w), Sym(u))
gw, gu = gw.e, gu.e
d_w = sp.simplify(sp.diff(F, w) - gw)
d_u = sp.simplify(sp.diff(F, u) - gu)
q = 1 / (1 + w ** 2)
C = 1 - u
S = -sp.sqrt(u * (2 - u))
m0 = 1 - q * (C - w * S)
m1 = 1 - q * C
m2 = 2 * (1 - q ** 2 * (C + w * S))
d_F = sp.simplify(F + 1 - m0 * m2 / m1 ** 2)
# Fallback for an inconclusive simplify: u = 2 s^2/(1 + s^2) (s > 0) is a bijection onto (0, 2) and makes
# sqrt(u (2 - u)) = 2 s/(1 + s^2) rational, so each residual becomes a rational function of (w, s).
s_ = sp.Symbol("s", positive=True)
usub = {u: 2 * s_ ** 2 / (1 + s_ ** 2)}
method = {}
res = {}
for name, expr in [("d_w", sp.diff(F, w) - gw), ("d_u", sp.diff(F, u) - gu), ("d_F", F + 1 - m0 * m2 / m1 ** 2)]:
    first = {"d_w": d_w, "d_u": d_u, "d_F": d_F}[name]
    if first == 0:
        res[name], method[name] = first, "simplify"
    else:
        r2 = sp.cancel(sp.simplify(expr.subs(usub)))
        res[name], method[name] = r2, "rationalized u = 2s^2/(1+s^2), cancel"
checks = {"g1_dF/dw_eq_grad_w": res["d_w"] == 0, "g1_dF/du_eq_grad_u": res["d_u"] == 0,
          "g2_F+1_eq_m0m2/m1^2_minimizing_sign": res["d_F"] == 0}
spots = []
for wq, uq in [("1/3", "1/7"), ("1", "7/10"), ("13/4", "19/10"), ("2/5", "1")]:
    sub = {w: sp.Rational(wq), u: sp.Rational(uq)}
    vals = [sp.N((sp.diff(F, w) - gw).subs(sub), 60), sp.N((sp.diff(F, u) - gu).subs(sub), 60),
            sp.N((F + 1 - m0 * m2 / m1 ** 2).subs(sub), 60)]
    spots.append({"w": wq, "u": uq, "residuals": [str(v) for v in vals],
                  "ok": all(abs(v) < sp.Float("1e-50") for v in vals)})
checks["g3_spot_checks_60_digits"] = all(s["ok"] for s in spots)
out = {"script": "ctl_f_gradsym_v1.py", "verified_source": "reductions/code/ctl_f_d1bnb_v1.py",
       "verified_source_sha256": src_sha, "functions_extracted": [f.name for f in funcs],
       "F_symbolic": str(F), "residuals_first_simplify": {"d_w": str(d_w), "d_u": str(d_u), "d_F": str(d_F)},
       "residuals_final": {k: str(v) for k, v in res.items()}, "residual_method": method,
       "spot_checks": spots, "checks": checks, "all_pass": all(checks.values()),
       "elapsed_s": round(time.time() - T0, 2)}
with lane_guard.xopen(os.path.join(RUN, "ctl_f_gradsym.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "checks": checks, "verified_source_sha256": src_sha,
                  "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if out["all_pass"] else 1)
