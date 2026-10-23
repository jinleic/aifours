#!/usr/bin/env python3
"""wh10_design_check_v1: deterministic stdlib design check (NO search, NO optimisation) of the gate quantities of the
proposed numpy assay code/rqls_wh10_lm_v1.py, recomputed independently in pure Python complex arithmetic:
 (1) basis self-test for d in {2, 5, 6, 7, 9, 10}: the Fourier basis and f_k(t) = lam_k^-t omega^(-t(t-1)/2)/sqrt d,
     lam_k = exp(-i pi (d-1)/d) omega^k, are orthonormal and diagonalise X and U = X Z^-1;
 (2) every stage-A anchor (d = 5, 7, 9; valid a; b in {0, 1}): residual 2-norm, full Gram deviation, ray count, mutation
     residual and deviation, compared with the frozen gate thresholds;
 (3) local structure at the KP anchors: singular values of the residual Jacobian (3d x 2d) at x_t = omega^(a t^2)/sqrt d
     (a = smallest valid), to see whether the near-anchor gate "all amp <= 1e-2 runs verify" is appropriate;
 (4) d = 10 relaxed anchors (Chu, constant, e_0): residual on the used families, full residual, CRT Bloch components.
Float values here are design evidence only. Standard library; budget 120 s; output JSON (exclusive) argv[1].
"""
import cmath, json, math, sys, time

T0 = time.monotonic()
OUT = sys.argv[1]
VALID = {5: [1, 3, 4], 7: [1, 2, 4, 5, 6], 9: [2, 5, 8]}


def bases(d):
    om = cmath.exp(2j * math.pi / d)
    lam0 = cmath.exp(-1j * math.pi * (d - 1) / d)
    Z = [[1.0 + 0j if t == k else 0j for t in range(d)] for k in range(d)]
    F = [[om ** (k * t) / math.sqrt(d) for t in range(d)] for k in range(d)]
    Fk = [[(lam0 * om ** k) ** (-t) * om ** (-(t * (t - 1) // 2)) / math.sqrt(d) for t in range(d)] for k in range(d)]
    return om, lam0, {"rows": Z, "columns": F, "classes": Fk}


def ip(u, v):
    return sum(u[i].conjugate() * v[i] for i in range(len(u)))


def X_apply(v):
    d = len(v)
    return [v[(t - 1) % d] for t in range(d)]


def selftest(d):
    om, lam0, B = bases(d)
    dev = 0.0
    for name in ("columns", "classes"):
        V = B[name]
        for a in range(d):
            for b in range(d):
                dev = max(dev, abs(ip(V[a], V[b]) - (1.0 if a == b else 0.0)))
    for k in range(d):
        f = B["columns"][k]
        Xf = X_apply(f)
        dev = max(dev, max(abs(Xf[t] - om ** (-k) * f[t]) for t in range(d)))
        g = B["classes"][k]
        Ug = X_apply([om ** (-t) * g[t] for t in range(d)])
        dev = max(dev, max(abs(Ug[t] - lam0 * om ** k * g[t]) for t in range(d)))
    return dev


def resid(x, d, fams, B):
    return [abs(ip(v, x)) ** 2 - 1.0 / d for f in fams for v in B[f]]


def config(x, d, om):
    n = math.sqrt(sum(abs(z) ** 2 for z in x))
    x = [z / n for z in x]
    Q = {}
    for i in range(d):
        for j in range(d):
            zx = [om ** (j * t) * x[t] for t in range(d)]
            Q[(i, j)] = [zx[(t - i) % d] for t in range(d)]
    return Q


def gram_dev(Q, d):
    fam = {"rows": [[(i, j) for j in range(d)] for i in range(d)],
           "columns": [[(i, j) for i in range(d)] for j in range(d)],
           "classes": [[(i, (s - i) % d) for i in range(d)] for s in range(d)]}
    out = {}
    for name, lines in fam.items():
        m = 0.0
        for L in lines:
            for a in range(d):
                for b in range(a, d):
                    m = max(m, abs(ip(Q[L[a]], Q[L[b]]) - (1.0 if a == b else 0.0)))
        out[name] = m
    return out


def rays(Q):
    keys = list(Q)
    reps = []
    minsep = 1.0
    for k in keys:
        v = Q[k]
        for u in reps:
            s = 1.0 - abs(ip(u, v)) ** 2
            if s < 1e-7:
                break
            minsep = min(minsep, s)
        else:
            reps.append(v)
    return len(reps)


def jacobi_eigs(S):
    n = len(S)
    A = [row[:] for row in S]
    for _ in range(80):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-30:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
                c, s = math.cos(th), math.sin(th)
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p], A[k][q] = c * akp - s * akq, s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k], A[q][k] = c * apk - s * aqk, s * apk + c * aqk
    return sorted(A[i][i] for i in range(n))


def jac_singular(x, d, B):
    rows = []
    for f in ("rows", "columns", "classes"):
        for v in B[f]:
            c = ip(v, x)
            # r = |<v,x>|^2; dr/dRe x_t = 2 Re(conj(c) conj(v_t)), dr/dIm x_t = 2 Re(conj(c) i conj(v_t))
            rows.append([2 * (c.conjugate() * v[t].conjugate()).real for t in range(d)] +
                        [2 * (c.conjugate() * 1j * v[t].conjugate()).real for t in range(d)])
    n = 2 * d
    JTJ = [[sum(r[a] * r[b] for r in rows) for b in range(n)] for a in range(n)]
    ev = jacobi_eigs(JTJ)
    return [math.sqrt(max(e, 0.0)) for e in ev]


out = {"probe": "wh10_design_check_v1", "kind": "deterministic float design check; no search"}
out["selftest_max_dev"] = {str(d): selftest(d) for d in (2, 5, 6, 7, 9, 10)}
anch = []
for d in (5, 7, 9):
    om, lam0, B = bases(d)
    for a in VALID[d]:
        for b in (0, 1):
            x = [om ** (a * t * t + b * t) / math.sqrt(d) for t in range(d)]
            r = resid(x, d, ("rows", "columns", "classes"), B)
            Q = config(x, d, om)
            gd = gram_dev(Q, d)
            xm = list(x)
            xm[0] *= om
            rm = resid(xm, d, ("rows", "columns", "classes"), B)
            gm = gram_dev(config(xm, d, om), d)
            rec = {"d": d, "a": a, "b": b, "res": math.sqrt(sum(v * v for v in r)), "md": max(gd.values()), "rays": rays(Q),
                   "mut_res": math.sqrt(sum(v * v for v in rm)), "mut_md": max(gm.values())}
            rec["gate_pass"] = bool(rec["res"] < 1e-12 and rec["md"] < 1e-12 and rec["rays"] == d and rec["mut_res"] >= 0.01
                                    and rec["mut_md"] >= 0.01)
            anch.append(rec)
out["anchors"] = anch
jac = {}
for d in (5, 7, 9):
    om, lam0, B = bases(d)
    x = [om ** (VALID[d][0] * t * t) / math.sqrt(d) for t in range(d)]
    sv = jac_singular(x, d, B)
    jac[str(d)] = {"a": VALID[d][0], "singular_values_ascending": sv,
                   "n_below_1e-8": sum(1 for s in sv if s < 1e-8), "smallest_above_1e-8": min((s for s in sv if s >= 1e-8), default=None)}
out["jacobian_at_KP_anchors"] = jac
om, lam0, B = bases(10)
t10 = range(10)
rel = []
for name, x, fams, free in (("chu", [cmath.exp(2j * math.pi * t * t / 20) / math.sqrt(10) for t in t10], ("rows", "columns"), "y"),
                             ("constant", [1 / math.sqrt(10) + 0j for t in t10], ("rows", "classes"), "x"),
                             ("e0", [1.0 + 0j if t == 0 else 0j for t in t10], ("columns", "classes"), "z")):
    r = resid(x, 10, fams, B)
    rf = resid(x, 10, ("rows", "columns", "classes"), B)
    gd = gram_dev(config(x, 10, om), 10)
    b0 = [x[t] for t in range(10) if t % 2 == 0]
    b0 = {t % 5: x[t] for t in range(10) if t % 2 == 0}
    b1 = {t % 5: x[t] for t in range(10) if t % 2 == 1}
    r00 = sum(abs(b0[s]) ** 2 for s in range(5))
    r11 = sum(abs(b1[s]) ** 2 for s in range(5))
    r01 = sum(b0[s].conjugate() * b1[s] for s in range(5))
    bl = {"z": abs(r00 - r11), "x": abs(2 * r01.real), "y": abs(2 * r01.imag)}
    paired = {"rows": "z", "columns": "x", "classes": "y"}
    rec = {"anchor": name, "fams": list(fams), "res": math.sqrt(sum(v * v for v in r)), "full_res": math.sqrt(sum(v * v for v in rf)),
           "dev": gd, "bloch": bl}
    rec["gate_pass"] = bool(rec["res"] < 1e-12 and max(gd[f] for f in fams) < 1e-12 and rec["full_res"] >= 0.01
                            and all(bl[paired[f]] < 1e-12 for f in fams) and bl[free] > 0.5)
    rel.append(rec)
out["d10_relaxed"] = rel
out["all_anchor_gates_pass"] = all(r["gate_pass"] for r in anch) and all(r["gate_pass"] for r in rel)
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"selftest": out["selftest_max_dev"], "all_anchor_gates_pass": out["all_anchor_gates_pass"],
                  "anchor_min_mut_res": min(r["mut_res"] for r in anch), "anchor_min_mut_md": min(r["mut_md"] for r in anch),
                  "anchor_max_res": max(r["res"] for r in anch), "anchor_rays": sorted({(r["d"], r["rays"]) for r in anch}),
                  "jac": {d: (v["n_below_1e-8"], v["smallest_above_1e-8"]) for d, v in jac.items()},
                  "relaxed": [(r["anchor"], r["res"], r["full_res"], r["bloch"], r["gate_pass"]) for r in rel],
                  "elapsed_s": out["elapsed_s"]}))
