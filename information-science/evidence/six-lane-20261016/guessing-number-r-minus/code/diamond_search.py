"""Search for distributions violating Ingleton(U,V;P,Q) under the 'diamond' functional dependencies
  H(U|PQ)=H(V|PQ)=0,  H(P|UQV)=H(Q|UPV)=0
(equivalently: U,V are functions of (P,Q) and every (U,V)-cell is a partial matching between P- and
Q-values).  Under these FDs Ing = I(P;Q|U)+I(P;Q|V)-H(P|UV).
Exploratory: random restarts + hill climbing over labelings U,V of a support S subset [k]x[k] with weights.
"""
import sys, math, random, json
from collections import defaultdict

def H(counts, total):
    return -sum(c / total * math.log2(c / total) for c in counts if c > 0)

def ing(points, w, U, V):
    # points: list of (p,q); w: weights; U,V: labels per point
    tot = sum(w)
    def ent(key):
        d = defaultdict(float)
        for i, (p, q) in enumerate(points):
            d[key(i, p, q)] += w[i]
        return H(d.values(), tot)
    hPQ = ent(lambda i, p, q: (p, q))
    hU = ent(lambda i, p, q: U[i]); hV = ent(lambda i, p, q: V[i])
    hPU = ent(lambda i, p, q: (p, U[i])); hQU = ent(lambda i, p, q: (q, U[i]))
    hPV = ent(lambda i, p, q: (p, V[i])); hQV = ent(lambda i, p, q: (q, V[i]))
    hUV = ent(lambda i, p, q: (U[i], V[i])); hPUV = ent(lambda i, p, q: (p, U[i], V[i]))
    I_PQ_U = hPU + hQU - hPQ - hU   # H(PQU)=H(PQ)
    I_PQ_V = hPV + hQV - hPQ - hV
    H_P_UV = hPUV - hUV
    return I_PQ_U + I_PQ_V - H_P_UV

def matching_ok(points, U, V):
    seenP = {}; seenQ = {}
    for i, (p, q) in enumerate(points):
        c = (U[i], V[i])
        if (c, p) in seenP or (c, q) in seenQ: return False
        seenP[(c, p)] = 1; seenQ[(c, q)] = 1
    return True

def search(k, m, iters, seed, weighted=False):
    rnd = random.Random(seed)
    points = [(p, q) for p in range(k) for q in range(k)]
    n = len(points)
    best = (1e9, None)
    for restart in range(iters):
        w = [rnd.random() if weighted else 1.0 for _ in range(n)]
        # random valid labeling: assign U randomly, then V greedily to keep matchings
        U = [rnd.randrange(m) for _ in range(n)]
        V = [rnd.randrange(m) for _ in range(n)]
        if not matching_ok(points, U, V):
            continue
        cur = ing(points, w, U, V)
        for step in range(400):
            i = rnd.randrange(n); which = rnd.random() < 0.5
            old = (U[i], V[i])
            if which: U[i] = rnd.randrange(m)
            else: V[i] = rnd.randrange(m)
            if weighted and rnd.random() < 0.3:
                j = rnd.randrange(n); oldw = w[j]; w[j] = max(1e-6, w[j] * math.exp(rnd.gauss(0, 0.5)))
            else:
                j = None
            if not matching_ok(points, U, V):
                U[i], V[i] = old
                if j is not None: w[j] = oldw
                continue
            new = ing(points, w, U, V)
            if new <= cur + 1e-12:
                cur = new
            else:
                U[i], V[i] = old
                if j is not None: w[j] = oldw
        if cur < best[0]:
            best = (cur, dict(U=list(U), V=list(V), w=list(w)))
    return best

if __name__ == "__main__":
    out = []
    for k in (2, 3, 4):
        for m in (2, 3, 4, 6):
            for weighted in (False, True):
                b = search(k, m, 300, 1000 * k + m + (7 if weighted else 0), weighted)
                out.append(dict(k=k, m=m, weighted=weighted, min_ingleton=b[0]))
                print(json.dumps(out[-1])); sys.stdout.flush()
