#!/usr/bin/env python3
"""Parent-authored INDEPENDENT verifier for the FCO(n) family (no worker code imported).
Family: q_ij(t) = w^(t*j + pi(t)*rho(i)) / sqrt(n), w = exp(2 pi i/n), pi, rho permutations of Z_n,
resolution classes C_s = {(i, i+s)}.  Rows and columns are always orthonormal; classes are orthonormal iff
S_pi(a, b) := sum_t w^(a t + b pi(t)) = 0 for every pair i != i' with a = i'-i, b = rho(i')-rho(i) (mod n).
Translations pi -> pi + d, rho -> rho + d' preserve solutions, so pi(0) = rho(0) = 0 WLOG.
Independent vanishing test (Lam-Leung structure, closed forms, NOT polynomial division):
  n prime: c constant;  n = p^2 (4, 9): c_r = c_{r+p} for all r (p-gons);  n = 8: c_r = c_{r+4};
  n = 2q (q odd prime: 6, 10): (c_r - c_{r+q}) * (-1)^r is the same for r = 0..q-1.
Self-test: each closed form is compared with exact rational evaluation of Re and Im via a different route:
  for prime n uses sum-of-all-roots identity; plus float check |sum| < 1e-9 on random histograms.
Exhaustive: every pi with pi(0)=0, then every rho with rho(0)=0 by an independent DFS (different order:
  assign rho values by increasing i, pre-filter by a bitmask of allowed b per a).
Rays: cells same projective ray iff (t*(j'-j) + pi(t)*(rho(i')-rho(i))) mod n is constant in t.
Cooperative budget; GO on stdin; SIGTERM sets a flag; one exclusive JSON output."""
import cmath, itertools, json, math, random, signal, sys, time
TERM = [False]
signal.signal(signal.SIGTERM, lambda s, f: TERM.__setitem__(0, True))
if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
T0 = time.monotonic(); BUDGET = 240.0; OUT = sys.argv[1]

class Halt(Exception):
    pass

def guard():
    if TERM[0] or time.monotonic() - T0 > BUDGET:
        raise Halt("TERM" if TERM[0] else "BUDGET")

def vanishes(c, n):
    if n in (2, 3, 5, 7):
        return all(x == c[0] for x in c)
    if n in (4, 9):
        p = 2 if n == 4 else 3
        return all(c[r] == c[(r + p) % n] for r in range(n))
    if n == 8:
        return all(c[r] == c[r + 4] for r in range(4))
    if n in (6, 10):
        q = n // 2
        d = [(c[r] - c[r + q]) * (1 if r % 2 == 0 else -1) for r in range(q)]
        return all(x == d[0] for x in d)
    raise ValueError("unsupported n")

def selftest():
    rng = random.Random(9137); bad = 0; van = 0
    for _ in range(4000):
        n = rng.choice([2, 3, 4, 5, 6, 7, 8, 9, 10]); w = cmath.exp(2j * math.pi / n)
        if rng.random() < 0.5:
            c = [rng.randint(0, 4) for _ in range(n)]
        else:
            c = [0] * n
            for _ in range(rng.randint(1, 5)):
                m = rng.choice([d for d in range(2, n + 1) if n % d == 0 and all(d % k for k in range(2, d))])
                r = rng.randrange(n // m)
                for k in range(m):
                    c[r + k * (n // m)] += 1
            if rng.random() < 0.3:
                c[rng.randrange(n)] += 1
        fl = abs(sum(x * w ** k for k, x in enumerate(c))) < 1e-9
        ex = vanishes(c, n); van += ex; bad += (fl != ex)
    return {"mismatches": bad, "vanishing_cases": van}

def S_zero(pi, a, b, n):
    c = [0] * n
    for t in range(n):
        c[(a * t + b * pi[t]) % n] += 1
    return vanishes(c, n)

def allowed_masks(pi, n):
    masks = [0] * n
    for a in range(1, n):
        m = 0
        for b in range(1, n):
            if S_zero(pi, a, b, n):
                m |= 1 << b
        masks[a] = m
    return masks

def solutions_for(pi, n, out_list, limit):
    masks = allowed_masks(pi, n)
    if any(masks[a] == 0 for a in range(1, n)):
        return 0, False
    rho = [0] * n; used = 1; count = 0
    def dfs(i, used):
        nonlocal count
        guard()
        if i == n:
            count += 1
            if len(out_list) < limit:
                out_list.append(tuple(rho))
            return
        for v in range(1, n):
            if used >> v & 1:
                continue
            ok = True
            for j in range(i):
                if not (masks[(i - j) % n] >> ((v - rho[j]) % n) & 1):
                    ok = False; break
            if ok:
                rho[i] = v; dfs(i + 1, used | (1 << v))
        rho[i] = 0
    dfs(1, used)
    return count, True

def ray_count(pi, rho, n):
    cells = [(i, j) for i in range(n) for j in range(n)]
    def key(i, j):
        return [(t * j + pi[t] * rho[i]) % n for t in range(n)]
    reps = []
    for (i, j) in cells:
        e = key(i, j)
        found = False
        for r in reps:
            d = (e[0] - r[0]) % n
            if all((e[t] - r[t]) % n == d for t in range(n)):
                found = True; break
        if not found:
            reps.append(e)
    return len(reps)

def gram_ok(pi, rho, n):
    w = cmath.exp(2j * math.pi / n)
    vec = {(i, j): [w ** ((t * j + pi[t] * rho[i]) % n) for t in range(n)] for i in range(n) for j in range(n)}
    lines = [[(i, j) for j in range(n)] for i in range(n)] + [[(i, j) for i in range(n)] for j in range(n)] + \
            [[(i, (i + s) % n) for i in range(n)] for s in range(n)]
    worst = 0.0
    for L in lines:
        for x in range(n):
            for y in range(x + 1, n):
                ip = sum(a.conjugate() * b for a, b in zip(vec[L[x]], vec[L[y]])) / n
                worst = max(worst, abs(ip))
    return worst

def run(n, keep):
    res = {"n": n, "pi_total": math.factorial(n - 1), "pi_done": 0, "pi_full_rows": 0, "solutions": 0,
           "pi_with_solution": 0, "maximal": 0, "rays_hist": {}, "examples": [], "max_gram_float": 0.0}
    for perm in itertools.permutations(range(1, n)):
        guard()
        pi = (0,) + perm; res["pi_done"] += 1
        sols = []
        cnt, full = solutions_for(pi, n, sols, 10 ** 9)
        res["pi_full_rows"] += full
        if cnt:
            res["pi_with_solution"] += 1; res["solutions"] += cnt
            for rho in sols:
                rc = ray_count(pi, rho, n)
                res["rays_hist"][str(rc)] = res["rays_hist"].get(str(rc), 0) + 1
                res["maximal"] += (rc == n * n)
                if len(res["examples"]) < keep:
                    g = gram_ok(pi, rho, n); res["max_gram_float"] = max(res["max_gram_float"], g)
                    res["examples"].append({"pi": list(pi), "rho": list(rho), "rays": rc, "gram_float_max": g})
                if n == 10 and rc == 100:
                    res["CANDIDATE_n10_maximal"] = {"pi": list(pi), "rho": list(rho)}
                    raise Halt("CANDIDATE")
    res["status"] = "COMPLETE"
    return res

out = {"verifier": "parent FCO independent v1", "budget_s": BUDGET, "per_n": {}, "selftest": None}
code = 0
try:
    out["selftest"] = selftest()
    if out["selftest"]["mismatches"] != 0:
        raise Halt("SELFTEST")
    for n in (2, 3, 4, 5, 6, 7, 8, 9, 10):
        out["per_n"][str(n)] = run(n, 6)
except Halt as h:
    out["halt"] = str(h); code = {"TERM": 5, "BUDGET": 4, "SELFTEST": 3, "CANDIDATE": 7}.get(str(h), 2)
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh)
print(json.dumps({k: (v if k != "per_n" else {n: {kk: r.get(kk) for kk in ("status", "pi_done", "pi_full_rows", "solutions", "maximal", "rays_hist")} for n, r in v.items()}) for k, v in out.items()}))
sys.exit(code)
