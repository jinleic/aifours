"""Exploratory float search: how negative can the Ingleton score  Ing(U,V;P,Q)/H(P,Q)  be for
distributions satisfying the diamond FDs?
   Ing = I(U;V|P) + I(U;V|Q) + I(P;Q) - I(U;V)
Diamond FDs: U = u(P,Q), V = v(P,Q); P determined by (U,Q,V); Q determined by (U,P,V) on the support.
Search: alphabets |P|=|Q|=k, |U|=|V|=m; random function pairs (u,v) satisfying the injectivity
conditions on the full grid, then optimise the joint law pi(p,q) by projected gradient-free Adam on
softmax logits.  (Restricting the support only helps the FDs, so full-grid injectivity is a
conservative choice; a second mode allows zero-mass cells by letting logits go to -inf.)
Prints the best score found; AND/OR uniform gives c_AO = (5/2 - 3/2 log2 3)/2 = 0.06128."""
import sys, json, math, itertools
import numpy as np

def H(p):
    p = p[p > 1e-15]; return float(-(p * np.log2(p)).sum())

def score(pi, u, v, k, m):
    # pi: k x k joint law of (P,Q)
    def marg(f):  # law of f(p,q) as dict
        d = {}
        for p in range(k):
            for q in range(k):
                key = f(p, q); d[key] = d.get(key, 0.0) + pi[p, q]
        return np.array(list(d.values()))
    HP = H(pi.sum(1)); HQ = H(pi.sum(0)); HPQ = H(pi.ravel())
    HU = H(marg(lambda p, q: u[p, q])); HV = H(marg(lambda p, q: v[p, q]))
    HUV = H(marg(lambda p, q: (u[p, q], v[p, q])))
    HUP = H(marg(lambda p, q: (u[p, q], p))); HVP = H(marg(lambda p, q: (v[p, q], p)))
    HUVP = H(marg(lambda p, q: (u[p, q], v[p, q], p)))
    HUQ = H(marg(lambda p, q: (u[p, q], q))); HVQ = H(marg(lambda p, q: (v[p, q], q)))
    HUVQ = H(marg(lambda p, q: (u[p, q], v[p, q], q)))
    I_UV = HU + HV - HUV
    I_UV_P = HUP + HVP - HUVP - HP
    I_UV_Q = HUQ + HVQ - HUVQ - HQ
    I_PQ = HP + HQ - HPQ
    Ing = I_UV_P + I_UV_Q + I_PQ - I_UV
    return Ing / HPQ if HPQ > 1e-9 else 0.0, Ing, HPQ

def fd_ok(u, v, k, support):
    for q in range(k):
        seen = set()
        for p in range(k):
            if not support[p, q]: continue
            key = (u[p, q], v[p, q])
            if key in seen: return False
            seen.add(key)
    for p in range(k):
        seen = set()
        for q in range(k):
            if not support[p, q]: continue
            key = (u[p, q], v[p, q])
            if key in seen: return False
            seen.add(key)
    return True

def optimise(u, v, k, m, rng, iters=400):
    th = rng.normal(0, 1, (k, k)); best = (1e9, None)
    step = 0.5
    cur = None
    for t in range(iters):
        pi = np.exp(th - th.max()); pi /= pi.sum()
        s, Ing, HPQ = score(pi, u, v, k, m)
        if cur is None or s < cur: cur = s; best = (s, pi.copy())
        # random coordinate perturbation (cheap derivative-free)
        cand = th + rng.normal(0, step, th.shape)
        pi2 = np.exp(cand - cand.max()); pi2 /= pi2.sum()
        s2 = score(pi2, u, v, k, m)[0]
        if s2 < s: th = cand
        else: step *= 0.995
    return best

if __name__ == "__main__":
    k, m, trials, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    rng = np.random.default_rng(seed); full = np.ones((k, k), bool)
    best = (1e9, None, None, None)
    for t in range(trials):
        u = rng.integers(0, m, (k, k)); v = rng.integers(0, m, (k, k))
        if not fd_ok(u, v, k, full): continue
        s, pi = optimise(u, v, k, m, rng)
        if s < best[0]:
            best = (s, pi, u, v)
            print(json.dumps(dict(trial=t, score=s, u=u.tolist(), v=v.tolist(), pi=np.round(pi, 4).tolist())), flush=True)
    print(json.dumps(dict(k=k, m=m, best_score=best[0], c_AO=(2.5 - 1.5 * math.log2(3)) / 2)))
