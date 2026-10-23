#!/usr/bin/env python3
"""core56_engine_v3 -- certificate-producing engine for rules-k6-v1 + v2 + v3 (lane sun-coset6).

Imports the frozen core56_engine_v2.py, whose sha256 is checked at start, for: Shape, the edge order,
taumin/taumax, status, gcd_alpha_r, canon, rule_K and rule_P.
New in v3:
  * RLP with exact dual certificates. The exact packing simplex returns y. Duals for every
    admissible q are stored in rlp_duals.json under the key "q|stats".
  * FH5 with assignment counts for each E5 placement (same hereditary test as v2).
  * N2-6 (rules-k6-v3 L11).
  * RPLP (rules-k6-v3 L12). For each admissible q, either a reference to an RLP dual with value
    >= 1, or an exact RPLP dual vector (a, b, u, l). Duals are found by float simplex, rationalised
    and verified exactly; if verification fails, the exact Fraction simplex is used.
  * For each type, the sha256 of the sorted labelled leaf codes (lets the tree be re-checked).
Usage: python3 core56_engine_v3.py OUTDIR      (mode core56 only)
"""
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
import platform
import sys
import time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
V2_SHA = "f9b837318bbdf8ea2f0cedaf3e272085c4f134b5f527b1454aed81b498485ee8"
with open(os.path.join(HERE, "core56_engine_v2.py"), "rb") as _f:
    assert hashlib.sha256(_f.read()).hexdigest() == V2_SHA, "core56_engine_v2.py hash mismatch"
_spec = importlib.util.spec_from_file_location("e2", os.path.join(HERE, "core56_engine_v2.py"))
e2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e2)
BIG = 50


# ------------------------------------------------------------ exact simplex (packing form)
def packing_exact(M, c):
    """max c.z s.t. M z <= 1, z >= 0 (exact Fractions, Bland). Returns ('opt', value, z) or ('unb', None, None)."""
    m, n = len(M), len(c)
    T = [[F(x) for x in row] + [F(1 if r == i else 0) for r in range(m)] + [F(1)] for i, row in enumerate(M)]
    obj = [-F(x) for x in c] + [F(0)] * m + [F(0)]
    basis = [n + i for i in range(m)]
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            z = [F(0)] * n
            for i, b in enumerate(basis):
                if b < n:
                    z[b] = T[i][-1]
            return "opt", obj[-1], z
        leave, best = None, None
        for i in range(m):
            if T[i][enter] > 0:
                ratio = T[i][-1] / T[i][enter]
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave is None:
            d = [F(0)] * n
            if enter < n:
                d[enter] = F(1)
            for i, b in enumerate(basis):
                if b < n:
                    d[b] = -T[i][enter]
            return "unb", sum(F(x) * y for x, y in zip(c, d)), d
        pv = T[leave][enter]
        T[leave] = [x / pv for x in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0:
                f = T[i][enter]
                T[i] = [a - f * b for a, b in zip(T[i], T[leave])]
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, T[leave])]
        basis[leave] = enter


def packing_float(M, c, tol=1e-9):
    m, n = len(M), len(c)
    T = [list(map(float, row)) + [1.0 if r == i else 0.0 for r in range(m)] + [1.0] for i, row in enumerate(M)]
    obj = [-float(x) for x in c] + [0.0] * m + [0.0]
    basis = [n + i for i in range(m)]
    for _ in range(20000):
        enter = next((j for j in range(n + m) if obj[j] < -tol), None)
        if enter is None:
            z = [0.0] * n
            for i, b in enumerate(basis):
                if b < n:
                    z[b] = T[i][-1]
            return "opt", obj[-1], z
        leave, best = None, None
        for i in range(m):
            if T[i][enter] > tol:
                ratio = T[i][-1] / T[i][enter]
                if best is None or ratio < best - 1e-12 or (abs(ratio - best) <= 1e-12 and basis[i] < basis[leave]):
                    best, leave = ratio, i
        if leave is None:
            d = [0.0] * n
            if enter < n:
                d[enter] = 1.0
            for i, b in enumerate(basis):
                if b < n:
                    d[b] = -T[i][enter]
            return "unb", sum(float(x) * y for x, y in zip(c, d)), d
        pv = T[leave][enter]
        T[leave] = [x / pv for x in T[leave]]
        for i in range(m):
            if i != leave and T[i][enter] != 0.0:
                f = T[i][enter]
                T[i] = [a - f * b for a, b in zip(T[i], T[leave])]
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, T[leave])]
        basis[leave] = enter
    return "iter", None, None


def verify_packing(M, c, z):
    if any(x < 0 for x in z):
        return False
    for row in M:
        if sum(a * b for a, b in zip(row, z) if a) > 1:
            return False
    return sum(a * b for a, b in zip(c, z)) >= 1


# ------------------------------------------------------------ RLP with duals
def exps(q, st):
    a = e2.vp(q, 2) + (0 if st[0] == 0 else (1 if st[0] == 1 else BIG))
    b = e2.vp(q, 3) + (BIG if st[1] else 0)
    return a, b


def hereditary(T, g):
    return all(any(g(x, y) >= len(U) for x, y in itertools.combinations(U, 2))
               for r in range(2, len(T) + 1) for U in itertools.combinations(T, r))


_RLPD = {}


def rlp_dual(qs, stats, d=5):
    key = "%s|%s" % (",".join(map(str, qs)), ";".join("%d%d" % s for s in stats))
    if key in _RLPD:
        return key, _RLPD[key]
    n = len(qs)
    ex = [exps(qs[x], stats[x]) for x in range(n)]

    def g(x, y):
        return 2 ** min(ex[x][0], ex[y][0]) * 3 ** min(ex[x][1], ex[y][1])
    allowed = [frozenset(T) for r in range(1, n + 1) for T in itertools.combinations(range(n), r) if r == 1 or hereditary(T, g)]
    maximal = [T for T in allowed if not any(T < U for U in allowed)]
    M = [[1 if j in T else 0 for j in range(n)] for T in maximal]
    st, val, y = packing_exact(M, [F(q, d) for q in qs])
    rec = {"value": str(val), "y": [str(x) for x in y]}
    _RLPD[key] = rec
    return key, rec


def rule_RLP3(S, A, sp):
    k, d = S.k, S.d
    for v in range(k):
        oth = [w for w in range(k) if w != v]
        stats = tuple(e2.status(j, sp) for j in oth)
        dead = True
        for q in itertools.product(*[range(1, d - A[v][j] + 1) for j in oth]):
            key, rec = rlp_dual(tuple(q), stats, d)
            if F(rec["value"]) < 1:
                dead = False
                break
        if dead:
            return ("RLP", v)
    return None


# ------------------------------------------------------------ FH5 with counts
def fibre5_count(S, A, sp, e5, inside, fixed):
    k, m = S.k, 5
    opts = []
    for l in range(k):
        ts = [1] if l in inside else ([fixed[l]] if l in fixed else range(1, m + 1))
        o = [(t, M) for t in ts for M in itertools.combinations(range(m), t)]
        if l == inside[0]:
            o = [(1, (0,))]
        opts.append(o)
    count = 0
    for combo in itertools.product(*opts):
        count += 1
        t = [cc[0] for cc in combo]
        if any(t[i] == 1 and A[i][l] > t[l] for i in range(k) for l in range(k) if l != i):
            continue
        Vv = [e2.fibre_vals(l, t[l], sp, e5) for l in range(k)]

        def g(x, y):
            return 2 ** min(Vv[x][0], Vv[y][0]) * 3 ** min(Vv[x][1], Vv[y][1]) * 5 ** min(Vv[x][2], Vv[y][2])
        ok = True
        for cst in range(m):
            Sc = [l for l in range(k) if cst in combo[l][1]]
            if len(Sc) >= 2 and not hereditary(Sc, g):
                ok = False
                break
        if ok:
            return True, count
    return False, count


def rule_FH5_3(S, A, sp):
    k = S.k
    for a, b in itertools.combinations(range(k), 2):
        if A[a][b] != 1:
            continue
        Vs = {v: A[v][a] for v in range(k) if v not in (a, b) and A[v][a] == A[v][b]}
        if not Vs:
            continue
        inside = [a, b] + sorted(v for v, c in Vs.items() if c == 1)
        fixed = {v: c for v, c in Vs.items() if c > 1}
        counts = []
        dead = True
        for e5 in [None] + list(range(k)):
            feas, cnt = fibre5_count(S, A, sp, e5, inside, fixed)
            counts.append(cnt)
            if feas:
                dead = False
                break
        if dead:
            return ("FH5", [a, b], sorted(Vs), counts)
    return None


# ------------------------------------------------------------ N2-6
def rule_N26(S, A, sp):
    e2v, c2, e3v = sp
    k = S.k
    for v in range(k):
        if v == e2v:
            continue
        nb = [w for w in range(k) if w != v]
        if any(A[v][j] != 2 for j in nb):
            continue
        if any(A[j][kk] not in (2, 4) for j, kk in itertools.combinations(nb, 2)):
            continue
        if v == e3v:
            ok = True
            for j, kk, l in itertools.combinations(nb, 3):
                tm, tM = e2.taumin(A, j, kk, l, sp), e2.taumax(A, j, kk, l)
                if tm % 3 != 0 and tM >= 3 * tm:
                    ok = False
                    break
            if not ok:
                continue
        return ("N26", v)
    return None


# ------------------------------------------------------------ RPLP
def p_bounds(A, sp, v, j, kk, d=5):
    """(lo, hi) for |X_j cap X_k| at v (rules-k6-v1 L4), as Fractions."""
    a = A[j][kk]
    u = F(1, d * e2.gcd_alpha_r(a, v, sp))
    Xj, Xk = F(A[v][j], d), F(A[v][kk], d)
    lo = max(F(e2.taumin(A, v, j, kk, sp), d * a), Xj + Xk - 1, F(0))
    q = lo / u
    lo = (-((-q.numerator) // q.denominator)) * u
    mm = min(Xj, Xk)
    q = mm / u
    hi = (q.numerator // q.denominator) * u
    if hi == mm:
        def k2(v_, j_, k_):
            return A[v_][j_] + A[k_][j_] <= d - 1
        if Xj < Xk:
            ok = k2(v, j, kk)
        elif Xk < Xj:
            ok = k2(v, kk, j)
        else:
            ok = k2(v, j, kk) and k2(v, kk, j)
        if not ok:
            hi -= u
    return lo, hi


def rplp_lp(A, sp, v, q, d=5):
    """Return (M, c) of the dual packing LP for vertex v and q (rules-k6-v3 L12), canonical order."""
    oth = [w for w in range(6) if w != v]
    stats = {j: e2.status(j, sp) for j in oth}
    qd = dict(zip(oth, q))
    ex = {j: exps(qd[j], stats[j]) for j in oth}

    def g(x, y):
        return 2 ** min(ex[x][0], ex[y][0]) * 3 ** min(ex[x][1], ex[y][1])
    forced = [(w, j) for w in oth for j in oth if w != j and e2.taumin(A, v, w, j, sp) >= A[v][w] * A[w][j]]
    pairs = list(itertools.combinations(oth, 2))
    cols = []
    for r in range(1, 6):
        for Aset in itertools.combinations(oth, r):
            As = set(Aset)
            if any(j in As and w not in As for (w, j) in forced):
                continue
            for rr in range(0, r + 1):
                for Sset in itertools.combinations(Aset, rr):
                    if rr >= 2 and not hereditary(Sset, g):
                        continue
                    cols.append((As, set(Sset)))
    M = []
    for As, Ss in cols:
        sa = [1 if j in Ss else 0 for j in oth]
        aa = [1 if j in As else 0 for j in oth]
        pp = [1 if (j in As and kk in As) else 0 for j, kk in pairs]
        M.append(sa + [-x for x in sa] + aa + [-x for x in aa] + [-x for x in pp] + pp)
    c = [F(qd[j], d) for j in oth] + [-F(qd[j], d) for j in oth]
    c += [F(d - A[v][j], d) for j in oth] + [-F(d - A[v][j], d) for j in oth]
    yhi, ylo = [], []
    for j, kk in pairs:
        lo, hi = p_bounds(A, sp, v, j, kk, d)
        base = 1 - F(A[v][j] + A[v][kk], d)
        yhi.append(base + hi)
        ylo.append(base + lo)
    c += [-x for x in yhi] + ylo
    return M, c

def _combine(z):
    a = [z[i] - z[5 + i] for i in range(5)]
    b = [z[10 + i] - z[15 + i] for i in range(5)]
    return [str(x) for x in a + b + list(z[20:30]) + list(z[30:40])]


def rplp_cert_q(A, sp, v, q):
    """Exact dual (a_j[5], b_j[5], u_jk[10], l_jk[10]) proving min >= 1, or None if not certified.
    If the dual LP is unbounded (primal infeasible), the certificate is the ray d scaled to c.d = 1:
    then M z <= 0 <= 1 and c.z = 1 (Farkas; checked by the same verifier)."""
    M, c = rplp_lp(A, sp, v, q)
    st, val, z = packing_float(M, c)
    if st == "opt" and val < 1 - 1e-9:
        return None
    if st == "opt":
        zf = [F(x).limit_denominator(100000) if x > 1e-12 else F(0) for x in z]
        if verify_packing(M, c, zf):
            return _combine(zf)
    if st == "unb" and val > 1e-12:
        zf = [F(x / val).limit_denominator(100000) if x > 1e-12 else F(0) for x in z]
        if verify_packing(M, c, zf):
            return _combine(zf)
    st, val, z = packing_exact(M, c)
    if st == "opt":
        if val >= 1:
            return _combine(z)
        return None
    if st == "unb" and val > 0:
        zf = [x / val for x in z]
        if verify_packing(M, c, zf):
            return _combine(zf)
    return None


def rule_RPLP(S, A, sp):
    k, d = S.k, S.d
    for v in range(k):
        oth = [w for w in range(k) if w != v]
        stats = tuple(e2.status(j, sp) for j in oth)
        certs = []
        dead = True
        for q in itertools.product(*[range(1, d - A[v][j] + 1) for j in oth]):
            key, rec = rlp_dual(tuple(q), stats, d)
            if F(rec["value"]) >= 1:
                certs.append(["R", key])
                continue
            cq = rplp_cert_q(A, sp, v, q)
            if cq is None or cq == "UNBOUNDED":
                dead = False
                break
            certs.append(["P", cq])
        if dead:
            return ("RPLP", v, certs)
    return None


# ------------------------------------------------------------ run
def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=False)
    t0 = time.time()
    with open(os.path.abspath(__file__), "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    S = e2.Shape("core56")
    k = S.k
    rules = [("K", e2.rule_K), ("RLP", rule_RLP3), ("P", e2.rule_P), ("FH5", rule_FH5_3), ("N26", rule_N26), ("RPLP", rule_RPLP)]
    lines, survivors, summary = [], [], {}
    for sp in S.types:
        tt = time.time()
        A = [[0] * k for _ in range(k)]
        seen = {}
        leafcodes = []
        npruned = 0

        def rec(t):
            nonlocal npruned
            if t == len(S.E):
                leafcodes.append("".join(str(A[i][j]) for i, j in S.E))
                c = e2.canon(S, A, sp)
                if c not in seen:
                    seen[c] = [row[:] for row in A]
                return
            i, j = S.E[t]
            for al in range(1, S.amax + 1):
                A[i][j] = A[j][i] = al
                if all(e2.taumin(A, a, b, cc, sp) <= e2.taumax(A, a, b, cc) for (a, b, cc) in S.tri_at[t]):
                    rec(t + 1)
                else:
                    npruned += 1
            A[i][j] = A[j][i] = 0
        rec(0)
        leafcodes.sort()
        counts = {}
        for c, M in sorted(seen.items()):
            w = None
            for name, f in rules:
                w = f(S, M, sp)
                if w is not None:
                    break
            code = "".join(map(str, c))
            if w is None:
                counts["SURVIVE"] = counts.get("SURVIVE", 0) + 1
                survivors.append({"type": list(sp), "code": code, "alpha": {"%d%d" % (i, j): M[i][j] for i, j in S.E}})
                lines.append(json.dumps({"type": list(sp), "code": code, "rep": "".join(str(M[i][j]) for i, j in S.E), "rule": "SURVIVE"}))
            else:
                counts[w[0]] = counts.get(w[0], 0) + 1
                lines.append(json.dumps({"type": list(sp), "code": code, "rep": "".join(str(M[i][j]) for i, j in S.E),
                                         "rule": w[0], "witness": list(w[1:])}, separators=(",", ":")))
        summary[str(sp)] = {"leaves_labelled": len(leafcodes), "pruned_nodes": npruned, "orbits": len(seen),
                            "leafcodes_sha256": hashlib.sha256(("\n".join(leafcodes) + "\n").encode()).hexdigest(),
                            "orbit_rule_counts": counts, "seconds": round(time.time() - tt, 1)}
        print(sp, summary[str(sp)], flush=True)
    blob = ("\n".join(lines) + "\n").encode()
    with open(os.path.join(outdir, "orbits.jsonl.gz"), "xb") as f:
        f.write(gzip.compress(blob, mtime=0))
    with open(os.path.join(outdir, "rlp_duals.json"), "x") as f:
        json.dump(_RLPD, f, sort_keys=True)
    with open(os.path.join(outdir, "survivors.json"), "x") as f:
        json.dump(survivors, f, indent=1)
    runrec = {"engine": "core56_engine_v3", "sha256": sha, "imports_v2_sha256": V2_SHA, "python": sys.version,
              "platform": platform.platform(), "summary": summary, "total_orbits": sum(v["orbits"] for v in summary.values()),
              "total_survivors": len(survivors), "orbits_jsonl_sha256_uncompressed": hashlib.sha256(blob).hexdigest(),
              "rlp_dual_entries": len(_RLPD), "seconds": round(time.time() - t0, 1)}
    with open(os.path.join(outdir, "run.json"), "x") as f:
        json.dump(runrec, f, indent=1)
    print(json.dumps({"total_orbits": runrec["total_orbits"], "survivors": len(survivors), "seconds": runrec["seconds"]}))


if __name__ == "__main__":
    main()
