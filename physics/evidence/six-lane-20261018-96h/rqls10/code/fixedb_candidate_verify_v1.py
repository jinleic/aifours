#!/usr/bin/env python3
"""fixedb_candidate_verify_v1: standard-library verifier for candidates of the fixed-B unitary model (lane note
evidence/fixedb-unitary-model-proposal-v1.md): q_ij = U_i e_j, U_0 = I, B a Latin square (resolution).

Usage:
  fixedb_candidate_verify_v1.py candidate IN OUT [DIGITS]
      IN = JSON object, or JSONL whose FIRST record with "maximal_candidate": true is used; keys U_re, U_im
      ((v-1) x v x v, U_1..U_{v-1}, row index = component) and B_matrix (v x v).
  fixedb_candidate_verify_v1.py selftest ANCHORS OUT [DIGITS]
      ANCHORS = evidence/fixedb_anchors_v1.result.json. Positive controls: the exact v = 7 (Huang-Li) and v = 8
      (Zhang-Cao) anchors in double precision, each perturbed by 1e-9 * (random complex matrix) per block (unitarity
      broken too); negative control: Haar-like random unitaries for the cyclic B at v = 7.
Checks (one implementation; this is NOT one of the three independent checkers by itself):
  E  EXACT: every stored double is converted exactly to a rational (Fraction); all 3v Gram matrices (rows, columns,
     B-classes) are computed exactly; reported: max over entries of |Re(G - I)| and |Im(G - I)| (exact, shown as float);
     min over unordered cell pairs of 1 - |<q,q'>|^2 / (|q|^2 |q'|^2) (exact, shown as float).
  H  HIGH PRECISION (decimal, DIGITS + 20 working digits): Newton-Schulz polar unitarisation X <- X (3I - X^* X) / 2;
     chord Gauss-Newton on the 2 v^2 (v-1) real residuals (M[p,p], M[p,pi(p)], M = U_i^* U_i') with the double
     precision Jacobian of the start point (normal equations + 1e-12 * max-diagonal regularisation, Cholesky), update
     U_k <- U_k expm(A_k) (Taylor series to 10^-(DIGITS+15)) + two Newton-Schulz steps; REFINED when max |F| <
     10^-DIGITS; otherwise NOT_NEAR_SOLUTION (start residual > 1e-6), STEP_TOO_LARGE (a step > 1e-3) or REFINE_FAILED
     (14 steps, or 3 steps without decrease); then the full Gram check of all 3v lines and the min ray separation at
     high precision; rays counted with merge threshold 10^-(DIGITS // 2).
"""
import hashlib, json, math, random, sys, time
from decimal import Decimal, getcontext
from fractions import Fraction

T0 = time.monotonic()
MODE, IN, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
DIGITS = int(sys.argv[4]) if len(sys.argv) > 4 else 60
getcontext().prec = DIGITS + 20


def cmm(A, B):
    Ar, Ai = A
    Br, Bi = B
    n, k, m = len(Ar), len(Br), len(Br[0])
    Cr = [[0] * m for _ in range(n)]
    Ci = [[0] * m for _ in range(n)]
    for r in range(n):
        rr, ri = Cr[r], Ci[r]
        for t in range(k):
            ar, ai = Ar[r][t], Ai[r][t]
            if ar == 0 and ai == 0:
                continue
            br, bi = Br[t], Bi[t]
            for c in range(m):
                rr[c] += ar * br[c] - ai * bi[c]
                ri[c] += ar * bi[c] + ai * br[c]
    return Cr, Ci


def ch(A):
    Ar, Ai = A
    n, m = len(Ar), len(Ar[0])
    return [[Ar[r][c] for r in range(n)] for c in range(m)], [[-Ai[r][c] for r in range(n)] for c in range(m)]


def ident(v, one):
    return [[one if r == c else 0 * one for c in range(v)] for r in range(v)], [[0 * one] * v for _ in range(v)]


def struct(B):
    v = len(B)
    pos = [{B[i][j]: j for j in range(v)} for i in range(v)]
    res = []
    for i in range(v):
        for ip in range(i + 1, v):
            for p in range(v):
                res.append((i, ip, p, p))
            for p in range(v):
                res.append((i, ip, p, pos[ip][B[i][p]]))
    lines = [[(i, j) for j in range(v)] for i in range(v)] + [[(i, j) for i in range(v)] for j in range(v)]
    cls = {}
    for i in range(v):
        for j in range(v):
            cls.setdefault(B[i][j], []).append((i, j))
    lines += [cls[s] for s in sorted(cls)]
    return res, lines


def vecs(U):
    """cell (i, j) -> (re list, im list) of column j of U_i."""
    v = len(U)
    return {(i, j): ([U[i][0][s][j] for s in range(v)], [U[i][1][s][j] for s in range(v)])
            for i in range(v) for j in range(v)}


def ip(x, y):
    xr, xi = x
    yr, yi = y
    re = sum(a * b for a, b in zip(xr, yr)) + sum(a * b for a, b in zip(xi, yi))
    im = sum(a * b for a, b in zip(xr, yi)) - sum(a * b for a, b in zip(xi, yr))
    return re, im


def gram_report(U, lines, one):
    Q = vecs(U)
    fam = {}
    names = ("rows", "columns", "classes")
    v = len(U)
    for li, L in enumerate(lines):
        f = names[li // v]
        m = fam.get(f, 0 * one)
        for a in range(len(L)):
            for b in range(a, len(L)):
                re, im = ip(Q[L[a]], Q[L[b]])
                if a == b:
                    re = re - one
                m = max(m, abs(re), abs(im))
        fam[f] = m
    return fam, Q


def min_margin(Q, cells, one):
    nrm = {c: ip(Q[c], Q[c])[0] for c in cells}
    best, pairs = None, []
    for a in range(len(cells)):
        for b in range(a + 1, len(cells)):
            re, im = ip(Q[cells[a]], Q[cells[b]])
            mg = one - (re * re + im * im) / (nrm[cells[a]] * nrm[cells[b]])
            pairs.append(mg)
            if best is None or mg < best:
                best = mg
    return best, pairs


def to_U(Ure, Uim, conv, one):
    v = len(Ure) + 1
    U = [ident(v, one)]
    for k in range(v - 1):
        U.append(([[conv(x) for x in row] for row in Ure[k]], [[conv(x) for x in row] for row in Uim[k]]))
    return U


def exact_check(Ure, Uim, B):
    _, lines = struct(B)
    v = len(B)
    U = to_U(Ure, Uim, Fraction, Fraction(1))
    fam, Q = gram_report(U, lines, Fraction(1))
    cells = [(i, j) for i in range(v) for j in range(v)]
    best, _ = min_margin(Q, cells, Fraction(1))
    return {"gram_maxdev_by_family": {k: float(x) for k, x in fam.items()},
            "gram_maxdev": float(max(fam.values())), "min_ray_margin": float(best),
            "min_ray_margin_positive": bool(best > 0)}


# ----- high precision
def D(x):
    return Decimal(x) if isinstance(x, float) else Decimal(x)


def newton_schulz(X, steps, tol):
    v = len(X[0])
    I3 = ident(v, Decimal(3))
    for _ in range(steps):
        Y = cmm(ch(X), X)
        dev = max(max(abs(Y[0][r][c] - (1 if r == c else 0)), abs(Y[1][r][c])) for r in range(v) for c in range(v))
        if dev < tol:
            break
        Z = ([[I3[0][r][c] - Y[0][r][c] for c in range(v)] for r in range(v)], [[-Y[1][r][c] for c in range(v)] for r in range(v)])
        P = cmm(X, Z)
        X = ([[x / 2 for x in row] for row in P[0]], [[x / 2 for x in row] for row in P[1]])
    return X


def residual(U, res):
    v = len(U)
    Ms = {}
    for (i, ipr, p, q) in res:
        if (i, ipr) not in Ms:
            Ms[(i, ipr)] = cmm(ch(U[i]), U[ipr])
    return [(Ms[(i, ipr)][0][p][q], Ms[(i, ipr)][1][p][q]) for (i, ipr, p, q) in res], Ms


def jac_normal(Uf, res, v):
    """double precision normal matrix N = J^T J (P x P) for the chart U_k expm(A_k), A_k zero-diagonal skew-Hermitian;
    returns N and the sparse complex rows."""
    pl = [(a, b) for a in range(v) for b in range(a + 1, v)]
    pidx = {}
    for k, (a, b) in enumerate(pl):
        pidx[(a, b)] = k
        pidx[(b, a)] = k
    half, nb = len(pl), 2 * len(pl)
    P = (v - 1) * nb
    Mf = {}
    rows = []
    for (i, ipr, p, q) in res:
        if (i, ipr) not in Mf:
            A = Uf[i]
            Bm = Uf[ipr]
            Mf[(i, ipr)] = [[sum(A[t][r].conjugate() * Bm[t][c] for t in range(v)) for c in range(v)] for r in range(v)]
        M = Mf[(i, ipr)]
        row = {}
        if i >= 1:
            for r in range(v):
                if r != p:
                    sg = 1.0 if r > p else -1.0
                    base = (i - 1) * nb + pidx[(p, r)]
                    row[base] = -sg * M[r][q]
                    row[base + half] = -1j * M[r][q]
        for r in range(v):
            if r != q:
                sg = 1.0 if q > r else -1.0
                base = (ipr - 1) * nb + pidx[(r, q)]
                row[base] = sg * M[p][r]
                row[base + half] = 1j * M[p][r]
        rows.append(row)
    N = [[0.0] * P for _ in range(P)]
    for row in rows:
        items = list(row.items())
        for part in (0, 1):
            vals = [(k, (c.real if part == 0 else c.imag)) for k, c in items]
            vals = [(k, x) for k, x in vals if x != 0.0]
            for k1, x1 in vals:
                Nk = N[k1]
                for k2, x2 in vals:
                    Nk[k2] += x1 * x2
    return N, rows, pl, half, nb, P


def cholesky(N):
    P = len(N)
    mu = 1e-12 * max(N[k][k] for k in range(P))
    L = [[0.0] * P for _ in range(P)]
    for j in range(P):
        s = N[j][j] + mu - sum(L[j][t] * L[j][t] for t in range(j))
        if s <= 0:
            raise ValueError("Cholesky pivot <= 0 at %d" % j)
        L[j][j] = math.sqrt(s)
        Lj = L[j]
        for i in range(j + 1, P):
            Li = L[i]
            L[i][j] = (N[i][j] - sum(Li[t] * Lj[t] for t in range(j))) / Lj[j]
    return L


def chol_solve(L, b):
    P = len(L)
    y = [0.0] * P
    for i in range(P):
        y[i] = (b[i] - sum(L[i][t] * y[t] for t in range(i))) / L[i][i]
    x = [0.0] * P
    for i in range(P - 1, -1, -1):
        x[i] = (y[i] - sum(L[t][i] * x[t] for t in range(i + 1, P))) / L[i][i]
    return x


def expm_taylor(A, tol):
    v = len(A[0])
    E = ident(v, Decimal(1))
    T = ident(v, Decimal(1))
    for n in range(1, 60):
        T = cmm(T, A)
        T = ([[x / n for x in row] for row in T[0]], [[x / n for x in row] for row in T[1]])
        E = ([[E[0][r][c] + T[0][r][c] for c in range(v)] for r in range(v)],
             [[E[1][r][c] + T[1][r][c] for c in range(v)] for r in range(v)])
        if max(max(abs(x) for x in row) for row in T[0] + T[1]) < tol:
            break
    return E


def fmt(x):
    return format(x, ".3E") if x != 0 else "0"


def refine(Ure, Uim, B):
    v = len(B)
    res, lines = struct(B)
    tolu = Decimal(10) ** (-(DIGITS + 10))
    U = to_U(Ure, Uim, D, Decimal(1))
    U = [U[0]] + [newton_schulz(U[k], 12, tolu) for k in range(1, v)]
    Uf = [[[complex(float(U[k][0][r][c]), float(U[k][1][r][c])) for c in range(v)] for r in range(v)] for k in range(v)]
    N, rows0, pl, half, nb, P = jac_normal(Uf, res, v)
    L = cholesky(N)
    hist = []
    status = "REFINE_FAILED"
    target = Decimal(10) ** (-DIGITS)
    worse, prev = 0, None
    for step in range(15):
        F, _ = residual(U, res)
        fmax = max(max(abs(a), abs(b)) for a, b in F)
        hist.append(fmt(fmax))
        if fmax < target:
            status = "REFINED"
            break
        if step == 0 and fmax > Decimal("1e-6"):
            status = "NOT_NEAR_SOLUTION"
            break
        if prev is not None and fmax >= prev:
            worse += 1
            if worse >= 3:
                break
        prev = fmax
        if step == 14:
            break
        # chord: Jacobian of the start point (rows0) is reused; g = J0^T F
        Fr = [float(a) for a, b in F]
        Fi = [float(b) for a, b in F]
        g = [0.0] * P
        for k, row in enumerate(rows0):
            for idx, c in row.items():
                g[idx] += c.real * Fr[k] + c.imag * Fi[k]
        delta = chol_solve(L, [-x for x in g])
        if max(abs(x) for x in delta) > 1e-3:
            status = "STEP_TOO_LARGE"
            break
        newU = [U[0]]
        for kb in range(1, v):
            off = (kb - 1) * nb
            Ar = [[Decimal(0)] * v for _ in range(v)]
            Ai = [[Decimal(0)] * v for _ in range(v)]
            for t, (a, b) in enumerate(pl):
                x, y = Decimal(delta[off + t]), Decimal(delta[off + half + t])
                Ar[a][b], Ai[a][b] = x, y
                Ar[b][a], Ai[b][a] = -x, y
            E = expm_taylor((Ar, Ai), Decimal(10) ** (-(DIGITS + 15)))
            newU.append(newton_schulz(cmm(U[kb], E), 2, tolu))
        U = newU
    fam, Q = gram_report(U, lines, Decimal(1))
    cells = [(i, j) for i in range(v) for j in range(v)]
    best, margins = min_margin(Q, cells, Decimal(1))
    thr = Decimal(10) ** (-(DIGITS // 2))
    parent = list(range(len(cells)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    k = 0
    for a in range(len(cells)):
        for b in range(a + 1, len(cells)):
            if margins[k] < thr:
                parent[find(a)] = find(b)
            k += 1
    rays = len({find(a) for a in range(len(cells))})
    return {"status": status, "steps": len(hist), "maxabs_residual_history": hist, "digits": DIGITS,
            "gram_maxdev_by_family": {kk: fmt(x) for kk, x in fam.items()}, "gram_maxdev": fmt(max(fam.values())),
            "min_ray_margin": fmt(best), "rays": rays,
            "U_refined_re": [[[str(x) for x in row] for row in U[kb][0]] for kb in range(1, v)],
            "U_refined_im": [[[str(x) for x in row] for row in U[kb][1]] for kb in range(1, v)]}


def load_candidate(path):
    with open(path, "rb") as f:
        raw = f.read()
    h = hashlib.sha256(raw).hexdigest()
    txt = raw.decode("utf-8")
    if path.endswith(".jsonl"):
        for line in txt.splitlines():
            if not line.strip():
                continue
            o = json.loads(line)
            if o.get("maximal_candidate") and "U_re" in o:
                return o, h
        raise SystemExit("no maximal candidate record with U data in " + path)
    return json.loads(txt), h


out = {"verifier": "fixedb_candidate_verify_v1", "mode": MODE, "digits": DIGITS}
if MODE == "candidate":
    cand, h = load_candidate(IN)
    out["input"] = {"path": IN, "sha256": h, "tag": cand.get("tag"), "seed": cand.get("seed")}
    B = cand["B_matrix"]
    out["exact"] = exact_check(cand["U_re"], cand["U_im"], B)
    out["high_precision"] = refine(cand["U_re"], cand["U_im"], B)
elif MODE == "selftest":
    with open(IN, "rb") as f:
        raw = f.read()
    out["input"] = {"path": IN, "sha256": hashlib.sha256(raw).hexdigest()}
    AN = json.loads(raw.decode("utf-8"))
    rng = random.Random(4242)
    tests = []
    for key, N, den in (("v7", 7, 7.0), ("v8", 8, 2.0)):
        z = [complex(math.cos(2 * math.pi * k / N), math.sin(2 * math.pi * k / N)) for k in range(N)]
        UF = AN[key]["U_form"]
        v = len(UF)
        B = AN[key]["B"]
        Uc = [[[sum(c * z[k] for k, c in enumerate(UF[i][j][s])) / den for j in range(v)] for s in range(v)]
              for i in range(1, v)]
        Ure = [[[x.real for x in row] for row in M] for M in Uc]
        Uim = [[[x.imag for x in row] for row in M] for M in Uc]
        e0 = exact_check(Ure, Uim, B)
        eps = 1e-9
        Pre = [[[x + eps * rng.gauss(0, 1) for x in row] for row in M] for M in Ure]
        Pim = [[[x + eps * rng.gauss(0, 1) for x in row] for row in M] for M in Uim]
        e1 = exact_check(Pre, Pim, B)
        h1 = refine(Pre, Pim, B)
        tests.append({"anchor": key, "exact_unperturbed": e0, "exact_perturbed": e1,
                      "refined": {k: h1[k] for k in h1 if not k.startswith("U_refined")}})
    # negative control: random unitaries (Gram-Schmidt of Gaussian columns), cyclic B, v = 7
    v = 7
    B = [[(j - i) % v for j in range(v)] for i in range(v)]
    Ure, Uim = [], []
    for _ in range(v - 1):
        cols = []
        while len(cols) < v:
            x = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(v)]
            for c in cols:
                o = sum(a.conjugate() * b for a, b in zip(c, x))
                x = [b - o * a for a, b in zip(c, x)]
            nrm = math.sqrt(sum(abs(t) ** 2 for t in x))
            cols.append([t / nrm for t in x])
        Ure.append([[cols[c][r].real for c in range(v)] for r in range(v)])
        Uim.append([[cols[c][r].imag for c in range(v)] for r in range(v)])
    en = exact_check(Ure, Uim, B)
    hn = refine(Ure, Uim, B)
    tests.append({"anchor": "negative_random_cyc7", "exact": en,
                  "refined": {k: hn[k] for k in hn if not k.startswith("U_refined")}})
    out["tests"] = tests
    t7, t8, tn = tests
    out["gates"] = {
        "exact_unperturbed_anchors": all(t["exact_unperturbed"]["gram_maxdev"] < 1e-14 for t in (t7, t8)),
        "exact_perturbed_seen": all(1e-11 < t["exact_perturbed"]["gram_maxdev"] < 1e-7 for t in (t7, t8)),
        "positive_refined": all(t["refined"]["status"] == "REFINED" and Decimal(t["refined"]["gram_maxdev"]) <
                                Decimal(10) ** (-(DIGITS - 5)) for t in (t7, t8)),
        "positive_rays": t7["refined"]["rays"] == 49 and t8["refined"]["rays"] == 64,
        "negative_not_refined": tn["refined"]["status"] != "REFINED" and tn["exact"]["gram_maxdev"] > 1e-2}
else:
    raise SystemExit("unknown mode")
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
summary = {k: out[k] for k in ("mode", "gates", "elapsed_s") if k in out}
if MODE == "selftest":
    summary["tests"] = [{"anchor": t["anchor"], "status": t["refined"]["status"], "hist": t["refined"]["maxabs_residual_history"],
                         "gram": t["refined"]["gram_maxdev"], "rays": t["refined"]["rays"],
                         "margin": t["refined"]["min_ray_margin"]} for t in out["tests"]]
print(json.dumps(summary))
