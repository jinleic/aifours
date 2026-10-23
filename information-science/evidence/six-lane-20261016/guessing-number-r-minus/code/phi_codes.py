"""Evaluate the target functional Phi = 2 sum_v H(X_v) - 3 H(V) on the EXISTING exactly FD-checked codes
(no new searches):
  - the 88-word binary CP-SAT code (evidence/mis-q2-Rminus-600s.json);
  - the 64-word positive-control code (evidence/biased-binary-search.jsonl);
  - the 625-word fan code.
For each: the exact code version g = 3 log2|C| - 2 sum_v log2|A_v| (sign decided by integer comparison),
Phi of the uniform distribution, and min Phi over distributions supported on the code (float Adam on
softmax logits, a few restarts).  By Lemma B plus the types bridge, a distribution with Phi < 0 would give
gn(R^-) > 20/3.  Float minima are exploratory; any Phi < 0 must be re-certified exactly with rational
weights before use.
"""
import sys, os, json, math, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from balancing_lemma import fan_code, fd_ok as fd_ok_tuple
from graphs import R_MINUS_EDGES, nbmasks
NBM = nbmasks(R_MINUS_EDGES)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def fd_ok_int(code):
    for v in range(10):
        seen = {}
        for x in code:
            if seen.setdefault(x & NBM[v], (x >> v) & 1) != (x >> v) & 1: return False
    return True

def onehot(code_tuples):
    """columns: for each vertex v, indicator matrix (|C| x |A_v|)."""
    mats = []
    for v in range(10):
        syms = sorted({x[v] for x in code_tuples}); idx = {s: i for i, s in enumerate(syms)}
        M = np.zeros((len(code_tuples), len(syms)))
        for r, x in enumerate(code_tuples): M[r, idx[x[v]]] = 1
        mats.append(M)
    return mats

def phi_and_grad(th, mats):
    p = np.exp(th - th.max()); p /= p.sum()
    lp = np.log2(p + 1e-300); H = -(p * lp).sum()
    dH = -(lp + 1 / math.log(2))
    S = 0.0; dS = np.zeros_like(p)
    for M in mats:
        q = M.T @ p; lq = np.log2(q + 1e-300)
        S += -(q * lq).sum(); dS += M @ (-(lq + 1 / math.log(2)))
    phi = 2 * S - 3 * H
    dphi = 2 * dS - 3 * dH
    g = p * (dphi - (p * dphi).sum())
    return phi, g, H, S

def min_phi(mats, n, restarts=6, iters=4000, lr=0.05, seed=0):
    rng = np.random.default_rng(seed); best = (math.inf, None)
    for r in range(restarts):
        th = np.zeros(n) if r == 0 else rng.normal(0, 0.5, n)
        m = np.zeros(n); s = np.zeros(n)
        for t in range(1, iters + 1):
            phi, g, H, S = phi_and_grad(th, mats)
            m = 0.9 * m + 0.1 * g; s = 0.999 * s + 0.001 * g * g
            th -= lr * (m / (1 - 0.9 ** t)) / (np.sqrt(s / (1 - 0.999 ** t)) + 1e-12)
        phi, g, H, S = phi_and_grad(th, mats)
        if phi < best[0]:
            p = np.exp(th - th.max()); p /= p.sum(); best = (phi, dict(H=H, sumHv=S, support=int((p > 1e-6).sum())))
    return best

def analyse(name, code_tuples):
    n = len(code_tuples); alph = [len({x[v] for x in code_tuples}) for v in range(10)]
    lhs, rhs = n ** 3, math.prod(a * a for a in alph)
    mats = onehot(code_tuples)
    phi_u, _, H_u, S_u = phi_and_grad(np.zeros(n), mats)
    best, info = min_phi(mats, n)
    rec = dict(code=name, size=n, alphabets=alph, code_version_beats=lhs > rhs,
               g_log2=3 * math.log2(n) - 2 * sum(math.log2(a) for a in alph),
               phi_uniform=phi_u, H_uniform=H_u, sumHv_uniform=S_u, phi_min_float=best, phi_min_info=info)
    print(json.dumps(rec), flush=True)
    return rec

if __name__ == "__main__":
    out = []
    c88 = json.load(open(os.path.join(ROOT, "evidence", "mis-q2-Rminus-600s.json")))["code"]
    assert fd_ok_int(c88)
    out.append(analyse("cpsat88", [tuple((x >> v) & 1 for v in range(10)) for x in c88]))
    for line in open(os.path.join(ROOT, "evidence", "biased-binary-search.jsonl")):
        r = json.loads(line)
        if r.get("control") == "positive" and "code" in r:
            assert fd_ok_int(r["code"])
            out.append(analyse("control64", [tuple((x >> v) & 1 for v in range(10)) for x in r["code"]])); break
    fc = fan_code(); assert fd_ok_tuple(fc)
    out.append(analyse("fan625", fc))
    json.dump(out, open(os.path.join(ROOT, "evidence", "phi-existing-codes.json"), "w"), indent=1)
