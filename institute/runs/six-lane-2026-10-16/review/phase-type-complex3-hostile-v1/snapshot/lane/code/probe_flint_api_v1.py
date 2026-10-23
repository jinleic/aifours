"""API probe (no science): which python-flint 0.9.0 arb/acb/matrix features exist and how comparisons behave.
argv[1] = run directory (created by run_v1.sh). Writes probe.json there (exclusive create)."""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402  (must be first lane import)
import flint  # noqa: E402

out = {}
flint.ctx.prec = 128
x = flint.arb(2)
out["arb_methods_present"] = {m: hasattr(x, m) for m in [
    "sin", "cos", "tan", "cot", "atan", "sqrt", "mid", "rad", "lower", "upper", "contains", "overlaps",
    "is_finite", "union", "sin_cos", "exp", "log", "abs_upper", "abs_lower", "is_exact", "unique_fmpz"]}
out["arb_static"] = {m: hasattr(flint.arb, m) for m in ["pi", "const_pi"]}
a = flint.arb(1)
b = flint.arb(2)
ov = flint.arb("1.5") + flint.arb(0, 1)  # ball [0.5, 2.5]
out["cmp"] = {"1<2": bool(a < b), "1>2": bool(a > b), "ov<2": bool(ov < b), "ov>=2": bool(ov >= b),
              "ov>0": bool(ov > 0), "ov==ov": bool(ov == ov)}
out["arb_from_float_str"] = [str(flint.arb(0.1)), str(flint.arb("0.1")), str(flint.arb(flint.fmpq(1, 3)))]
out["arb_ctor_mid_rad"] = str(flint.arb(1, flint.arb(2) ** -10))
try:
    out["pi"] = str(flint.arb.pi())
except Exception as e:  # noqa: BLE001
    out["pi"] = "ERR " + repr(e)
try:
    out["cot"] = str(flint.arb("0.7").cot())
except Exception as e:  # noqa: BLE001
    out["cot"] = "ERR " + repr(e)
M = flint.arb_mat(2, 2)
M[0, 0] = 2
M[0, 1] = 1
M[1, 0] = 1
M[1, 1] = 3
out["arb_mat_methods"] = {m: hasattr(M, m) for m in ["solve", "inv", "det", "charpoly", "transpose", "nrows", "eig"]}
B = flint.arb_mat(2, 1)
B[0, 0] = 1
B[1, 0] = 1
try:
    X = M.solve(B)
    out["solve"] = [str(X[0, 0]), str(X[1, 0])]
except Exception as e:  # noqa: BLE001
    out["solve"] = "ERR " + repr(e)
C = flint.acb_mat(2, 2)
C[0, 0] = 0
C[0, 1] = 1
C[1, 0] = -1
C[1, 1] = 0
out["acb_mat_methods"] = {m: hasattr(C, m) for m in ["solve", "inv", "eig", "charpoly"]}
try:
    out["acb_eig"] = [str(e) for e in C.eig()]
except Exception as e:  # noqa: BLE001
    out["acb_eig"] = "ERR " + repr(e)
p = flint.arb_poly([1, 2, 3])
out["arb_poly_methods"] = {m: hasattr(p, m) for m in ["coeffs", "degree", "taylor_shift", "__divmod__",
                                                      "__floordiv__", "__mod__", "__call__", "roots"]}
try:
    q, r = divmod(flint.arb_poly([-1, 0, 0, 1]), flint.arb_poly([-1, 1]))
    out["divmod"] = [str(q), str(r)]
except Exception as e:  # noqa: BLE001
    out["divmod"] = "ERR " + repr(e)
z = flint.acb(1, 2)
out["acb"] = {"str": str(z), "real": str(z.real), "imag": str(z.imag), "abs": str(abs(z))}
with lane_guard.xopen(sys.argv[1] + "/probe.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
