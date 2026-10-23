"""Float sanity checks of the identities in review/codex-phi-out.md. Codex supplied the claims; the lane
checks them here. These are numeric consistency checks, not proofs.

(2) doubling identity: for any finite group code K (subgroup of a product of groups, coordinatewise
    multiplication) and any law p on K, with Y, Y' iid ~ p and T = Y*Y':
        2 Phi(Y) = Phi(T) + E_t Phi(Y'|T=t) + 2 sum_v I(Y'_v ; T_{-v} | T_v)
    Tested on random subgroups of Z_2^10 and on a non-abelian subgroup of S_3^10 (coordinates are
    homomorphic images).
(1) minimisation lemma, one instance: min over laws on K of Phi equals min over subgroups J <= K of
    2 sum_v log|pi_v(J)| - 3 log|J|.  The subgroup side is enumerated exactly for a 16-element F_2-code;
    the law side is float-minimised (Adam).  The float min must not go below the subgroup min.
(3) component chain rule: for X_v = (Y^1_v, Y^2_v) with an arbitrary joint law,
        Phi(X) = Phi(Y^1) + E Phi(Y^2 | Y^1) + 2 sum_v I(Y^2_v ; Y^1_{-v} | Y^1_v).
"""
import sys, os, json, math, itertools
import numpy as np
from collections import defaultdict
rng = np.random.default_rng(20261016)
LOG = math.log2

def H(d):
    p = np.array([x for x in d.values() if x > 0]); return float(-(p * np.log2(p)).sum())
def marg(law, f):
    d = defaultdict(float)
    for x, p in law.items(): d[f(x)] += p
    return d
def Phi(law, n=10):
    return 2 * sum(H(marg(law, lambda x, v=v: x[v])) for v in range(n)) - 3 * H(law)
def cond_H(law, f, g):   # H(f | g)
    return H(marg(law, lambda x: (f(x), g(x)))) - H(marg(law, g))
def I_cond(law, f, g, c):  # I(f; g | c)
    return (H(marg(law, lambda x: (f(x), c(x)))) + H(marg(law, lambda x: (g(x), c(x))))
            - H(marg(law, lambda x: (f(x), g(x), c(x)))) - H(marg(law, c)))

def doubling_check(K, mul, n=10):
    p = rng.dirichlet(np.ones(len(K)) * 0.7); law = {k: q for k, q in zip(K, p)}
    joint = defaultdict(float)           # law of (T, Y')
    for y, py in law.items():
        for y2, py2 in law.items():
            joint[(mul(y, y2), y2)] += py * py2
    lawT = marg(joint, lambda x: x[0])
    lhs = 2 * Phi(law)
    phiT = Phi(lawT)
    ephi = 0.0
    for t, pt in lawT.items():
        cl = {x[1]: q / pt for x, q in joint.items() if x[0] == t}
        ephi += pt * Phi(cl)
    Isum = sum(I_cond(joint, lambda x, v=v: x[1][v], lambda x, v=v: tuple(x[0][u] for u in range(n) if u != v),
                      lambda x, v=v: x[0][v]) for v in range(n))
    return lhs, phiT + ephi + 2 * Isum

def span_f2(gens):
    S = {0}
    for g in gens:
        S |= {s ^ g for s in S}
    return sorted(S)
tup = lambda w: tuple((w >> v) & 1 for v in range(10))
xor = lambda a, b: tuple(x ^ y for x, y in zip(a, b))

# S_3 as permutations of (0,1,2)
S3 = list(itertools.permutations(range(3)))
comp = lambda a, b: tuple(a[b[i]] for i in range(3))
def sgn(p): return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]) % 2
c = (1, 2, 0)
inv = lambda p: tuple(sorted(range(3), key=lambda i: p[i]))
conj = lambda p: comp(comp(c, p), inv(c))

if __name__ == "__main__":
    out = {"doubling": [], "minimisation": None, "chain": []}
    for trial in range(3):
        gens = [int(x) for x in rng.integers(1, 1024, 4)]
        K = [tup(w) for w in span_f2(gens)]
        l, r = doubling_check(K, xor); out["doubling"].append(dict(group="F2 subcode", size=len(K), lhs=l, rhs=r, diff=l - r))
    # non-abelian: K = {(g, h, sgn g, g, conj h, h, g, sgn h, conj g, h) : g,h in S3}, coordinate values
    # are elements of S3 or Z2, so multiplication is coordinatewise.
    def emb(g, h): return (g, h, sgn(g), g, conj(h), h, g, sgn(h), conj(g), h)
    K = [emb(g, h) for g in S3 for h in S3]
    def mulS(a, b):
        return tuple((x + y) % 2 if isinstance(x, int) else comp(x, y) for x, y in zip(a, b))
    assert all(mulS(emb(g1, h1), emb(g2, h2)) == emb(comp(g1, g2), comp(h1, h2)) for g1 in S3 for h1 in S3 for g2 in S3 for h2 in S3)
    l, r = doubling_check(K, mulS); out["doubling"].append(dict(group="S3xS3 in S3^10", size=len(K), lhs=l, rhs=r, diff=l - r))
    # minimisation lemma instance
    gens = [0b1011010011, 0b0110101101, 0b1100110110, 0b0011011011]
    Kint = span_f2(gens); K = [tup(w) for w in Kint]; assert len(K) == 16
    subs = set()
    for r in range(0, 5):
        for gs in itertools.combinations(Kint[1:], r):
            subs.add(tuple(span_f2(list(gs))))
    sub_min = min(2 * sum(LOG(len({tup(w)[v] for w in J})) for v in range(10)) - 3 * LOG(len(J)) for J in subs)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from phi_codes import onehot, min_phi
    fmin, info = min_phi(onehot(K), len(K), restarts=8, iters=3000)
    out["minimisation"] = dict(n_subgroups=len(subs), subgroup_min=float(sub_min),
                               float_not_below=bool(fmin >= sub_min - 1e-6), gap=float(fmin - sub_min), float_law_min_value=float(fmin))
    # chain rule (3): random joint law on pairs of binary 10-vectors (small support)
    for trial in range(3):
        sup = [(tup(int(a)), tup(int(b))) for a, b in rng.integers(0, 1024, (12, 2))]
        p = rng.dirichlet(np.ones(len(sup))); law = defaultdict(float)
        for s, q in zip(sup, p): law[s] += q
        X = marg(law, lambda x: tuple((x[0][v], x[1][v]) for v in range(10)))
        lhs = Phi(X)
        Y1 = marg(law, lambda x: x[0])
        e = 0.0
        for y1, q1 in Y1.items():
            cl = defaultdict(float)
            for x, q in law.items():
                if x[0] == y1: cl[x[1]] += q / q1
            e += q1 * Phi(cl)
        Is = sum(I_cond(law, lambda x, v=v: x[1][v], lambda x, v=v: tuple(x[0][u] for u in range(10) if u != v),
                        lambda x, v=v: x[0][v]) for v in range(10))
        out["chain"].append(dict(lhs=lhs, rhs=Phi(Y1) + e + 2 * Is, diff=lhs - (Phi(Y1) + e + 2 * Is)))
    ok = (all(abs(d["diff"]) < 1e-9 for d in out["doubling"]) and out["minimisation"]["float_not_below"]
          and all(abs(d["diff"]) < 1e-9 for d in out["chain"]))
    out["all_ok"] = ok
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "codex-phi-identity-checks.json"), "w"), indent=1)
    print(json.dumps(out, indent=1)); sys.exit(0 if ok else 1)
