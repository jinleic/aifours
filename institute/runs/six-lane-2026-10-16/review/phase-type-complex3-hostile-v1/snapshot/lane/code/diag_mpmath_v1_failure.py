"""Diagnostic for the aborted run f01-mpmath (ph3_mpmath_v1.py). Executes v1's definitions verbatim (source text up
to its sweep loop), replays the identical seeded sequence, and reports the first sample whose build() raises,
with n*, W and the 1-norm of -T0, to confirm or refute the scaling explanation recorded in ph3_mpmath_v2.py.
argv[1] = run directory; writes diag.json (exclusive create)."""
import sys
import json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
src_path = __file__.rsplit("/", 1)[0] + "/ph3_mpmath_v1.py"
src = open(src_path).read()
head = src.split("t_start = time.time()")[0]
ns = {"__file__": src_path}
exec(compile(head, src_path, "exec"), ns)
mp, rng, build, check, nstar = ns["mp"], ns["rng"], ns["build"], ns["check"], ns["nstar"]
out = {"dps": int(mp.mp.dps)}
for k in range(160):
    c = mp.mpf(10) ** rng.uniform(-3, 3)
    delta = mp.mpf(10) ** rng.uniform(-3, 3)
    beta = mp.mpf(10) ** rng.uniform(-2, 1.1)
    a, b = c + delta, beta * delta
    try:
        alpha, T, info = build(a, b, c)
    except ZeroDivisionError as e:
        n = nstar(a, b, c)
        rho = (1 + beta ** 2) / 2
        out["first_failure"] = {"k": k, "n_star": n, "beta": mp.nstr(beta, 15), "c": mp.nstr(c, 15),
                                "a_minus_c": mp.nstr(delta, 15), "rho": mp.nstr(rho, 10),
                                "rho_pow_n_minus_3": mp.nstr(rho ** (n - 3), 10), "error": repr(e)}
        break
    check(alpha, T, a, b, c, density=(k < 40))
    out.setdefault("passed_before_failure", 0)
    out["passed_before_failure"] += 1
with lane_guard.xopen(RUN + "/diag.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
