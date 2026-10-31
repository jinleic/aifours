#!/usr/bin/env python3
"""ReviewF178RminusSources control 2: exact copy-lemma row semantics and strategy-product semantics.

Part A builds one joint law by sequential conditional-kernel copies (DFZ formula, exact Fractions) mimicking
every copy-row shape used by certificate v12c: two-entry step then a step whose over-set contains an earlier
copy and an original (publisher 1(b)/1(c)), repeated single-entry copies of one original with earlier copies in
the over-set (programs m0..m5), and an extra single copy (xcopy). Positive rows must hold exactly; each mutation
must fail for its stated reason. Part B checks the guessing-strategy product on R-minus.
Exit 0 iff all expectations hold.
"""
import itertools, json, math, pathlib, random, sys, time
from collections import defaultdict
from fractions import Fraction as F

W = pathlib.Path(__file__).resolve().parent
out = {"control": "copy-and-product", "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "cases": []}
ok_all = True


def case(name, expected, actual, reason):
    global ok_all
    passed = expected == actual
    ok_all &= passed
    out["cases"].append({"case": name, "expected": expected, "actual": actual, "as_expected": passed, "reason": reason})


rnd = random.Random(1780)
names = ["A", "B", "C", "D", "E"]
law = {}
for atom in itertools.product([0, 1], repeat=5):
    law[atom] = F(rnd.randint(1, 97))
tot = sum(law.values()); law = {k: v / tot for k, v in law.items()}


def marg(law, names, sub):
    idx = [names.index(s) for s in sub]; m = defaultdict(F)
    for a, p in law.items():
        m[tuple(a[i] for i in idx)] += p
    return dict(m)


def H(law, names, sub):
    return -sum(float(p) * math.log2(float(p)) for p in marg(law, names, sub).values() if p > 0)


def copy_step(law, names, over, copied, new):
    """p'(e, n) = p(e) p(over=e_over, copied=n) / p(over=e_over)  (DFZ Copy Lemma proof, lines 363-366)."""
    pOC = marg(law, names, over + copied); pO = marg(law, names, over)
    io = [names.index(s) for s in over]; nl = {}
    for a, p in law.items():
        o = tuple(a[i] for i in io)
        for n in itertools.product([0, 1], repeat=len(copied)):
            q = pOC.get(o + n, F(0))
            if q:
                nl[a + n] = p * q / pO[o]
    return nl, names + new


def same_law(law, names, sub1, sub2):
    return marg(law, names, sub1) == marg(law, names, sub2)


def indep(law, names, X, Y, Z):
    pXYZ, pZ, pXZ, pYZ = marg(law, names, X + Y + Z), marg(law, names, Z), marg(law, names, X + Z), marg(law, names, Y + Z)
    nx, ny = len(X), len(Y)
    for xs in itertools.product([0, 1], repeat=nx):
        for ys in itertools.product([0, 1], repeat=ny):
            for zs in pZ:
                if pXYZ.get(xs + ys + zs, F(0)) * pZ[zs] != pXZ.get(xs + zs, F(0)) * pYZ.get(ys + zs, F(0)):
                    return False
    return True


def cmi(law, names, X, Y, Z):
    return H(law, names, X + Z) + H(law, names, Y + Z) - H(law, names, X + Y + Z) - (H(law, names, Z) if Z else 0.0)


base_law, base_names = dict(law), list(names)
STEPS = [  # (branch, over, copied, new)
    ("P", ["A", "B"], ["C", "D"], ["C'", "D'"]),             # two-entry step, Y = {E}
    ("P", ["A", "C'", "D"], ["E"], ["E''"]),                 # over has an earlier copy and an original
    ("Q", ["A", "D", "E"], ["B"], ["q0"]),                   # program-style single entry
    ("Q", ["A", "B", "E", "q0"], ["D"], ["q1"]),
    ("Q", ["A", "B", "E", "q0", "q1"], ["D"], ["q2"]),       # re-copy of D with its earlier copy q1 in the over-set
    ("X", ["B", "C", "E"], ["A"], ["s"]),                    # extra single copy
]
cur, cn = dict(base_law), list(base_names)
for (br, over, copied, new) in STEPS:
    before = list(cn)
    cur, cn = copy_step(cur, cn, over, copied, new)
    # positive: every U subset of over, every nonempty Q subset of entries
    good = True; nchk = 0
    for r in range(len(over) + 1):
        for U in itertools.combinations(over, r):
            for qn in range(1, len(new) + 1):
                for Qi in itertools.combinations(range(len(new)), qn):
                    nchk += 1
                    good &= same_law(cur, cn, list(U) + [new[i] for i in Qi], list(U) + [copied[i] for i in Qi])
    case(f"{br}: {new} copy of {copied} over {over}: law(U+new_Q)==law(U+old_Q) for all U<=over, Q", True, good, f"{nchk} exact marginal identities")
    rest = [x for x in before if x not in over]
    case(f"{br}: {new} independent of all earlier variables {rest} given over (exact factorisation)", True, indep(cur, cn, new, rest, over), "C2 / I(new; existing | over)=0")
joint, jn = cur, cn
# one construction vs separate branch laws
for br in "PQX":
    sl, sn = dict(base_law), list(base_names)
    for (b, over, copied, new) in STEPS:
        if b == br:
            sl, sn = copy_step(sl, sn, over, copied, new)
    case(f"branch {br}: marginal of joint construction == separately built branch law", True, marg(joint, jn, sn) == sl, "shared family and independent branch laws give identical branch marginals")


def neg(name, sub1, sub2, reason):
    differ = not same_law(joint, jn, sub1, sub2)
    dh = abs(H(joint, jn, sub1) - H(joint, jn, sub2))
    case("MUTATION " + name, False, (not differ) or dh < 1e-9, reason + f"; |dH|={dh:.6g} bits")


neg("U contains Y-variable E for step (C',D'): h(ABE+C')=h(ABE+C)", ["A", "B", "E", "C'"], ["A", "B", "E", "C"], "U not subset of over")
neg("U contains sibling original D with Q={C}: h(ABD+C')=h(ABD+C)", ["A", "B", "D", "C'"], ["A", "B", "D", "C"], "other entry of same step is not in over")
neg("mixed tuple: U contains sibling copy D' with original C: h(AB+D'+C)=h(AB+D+C)", ["A", "B", "D'", "C"], ["A", "B", "D", "C"], "mixed old/new tuple is not a copy marginal")
neg("wrong tuple map: h(AB+C')=h(AB+D)", ["A", "B", "C'"], ["A", "B", "D"], "copied tuple mapping is load-bearing")
neg("forward reference: U contains later E'' for step (C',D')", ["A", "B", "E''", "C'"], ["A", "B", "E''", "C"], "variable created after the step")
neg("U contains copied original D for step q1: h(ABEq0D+q1)=h(ABEq0D+D)", ["A", "B", "E", "q0", "D", "q1"], ["A", "B", "E", "q0", "D"], "copied original not in over")
neg("extra copy s with U containing A: h(BCA+s)=h(BCA+A)", ["B", "C", "A", "s"], ["B", "C", "A"], "copied original not in over")
case("MUTATION independence with later variable: I(C'D'; E'' | AB)=0", False, indep(joint, jn, ["C'", "D'"], ["E''"], ["A", "B"]),
     f"E'' is created later and depends on C'; CMI={cmi(joint, jn, ['C\'', 'D\''], ['E\'\''], ['A', 'B']):.6g}")
case("MUTATION independence with over-set missing B: I(C'D'; E | A)=0", False, indep(joint, jn, ["C'", "D'"], ["E"], ["A"]),
     f"conditioning set must be the declared over-set; CMI={cmi(joint, jn, ['C\'', 'D\''], ['E'], ['A']):.6g}")

# ---- Part B: strategy product on R-minus ----
NT = {1: [2, 3, 4, 5, 6, 7], 2: [1, 3, 7, 9, 10], 3: [1, 2, 4, 8, 9], 4: [1, 3, 5, 8, 10], 5: [1, 4, 6, 9, 10],
      6: [1, 5, 7, 8, 9], 7: [1, 2, 6, 8, 10], 8: [3, 4, 6, 7, 9, 10], 9: [2, 3, 5, 6, 8], 10: [2, 4, 5, 7, 8]}
V = list(range(1, 11))
g1 = {i + 1: x for i, x in enumerate([8, 10, 7, 6, 9, 3, 4, 1, 2, 5])}
g2 = {i + 1: x for i, x in enumerate([1, 5, 6, 7, 2, 3, 4, 8, 9, 10])}
tri = [(1, 2, 3), (4, 5, 10), (6, 8, 9)]  # triangles of R-minus; vertex 7 guesses 0


def f(v, xn):  # xn: dict u->colour for u in N(v)
    for t in tri:
        if v in t:
            a, b = [u for u in t if u != v]
            return xn[a] ^ xn[b]
    return 0


assert all(all(u in NT[v] for u in t if u != v) for t in tri for v in t)
Wset = [x for x in itertools.product([0, 1], repeat=10) if all(x[v - 1] == f(v, {u: x[u - 1] for u in NT[v]}) for v in V)]
case("toy strategy: |W| == 2^6", True, len(Wset) == 64, "three parity triangles, vertex 7 constant")


def group(gens):
    G = [tuple(V)]; fr = [tuple(V)]
    while fr:
        nw = []
        for x in fr:
            for g in gens:
                y = tuple(g[x[i]] for i in range(10))
                if y not in G: G.append(y); nw.append(y)
        fr = nw
    return [{v: x[v - 1] for v in V} for x in G]


def prep(Gl):  # for each (v, k): image vertex g(v) and, per neighbour w of g(v), the Y-coordinate g^-1(w) holding X^(g)_w
    tab = {}
    for k, g in enumerate(Gl):
        inv = {g[u]: u for u in V}
        for v in V:
            tab[(v, k)] = (g[v], [(w, inv[w]) for w in NT[g[v]]])
    return tab


def reads_only_neighbours(Gl):
    return all({src for _, src in prep(Gl)[(v, k)][1]} == set(NT[v]) for v in V for k in range(len(Gl)))


def product_wins(Gl, y, tab=None):  # y[v] = tuple over g in Gl; component k of Y_v is X^(g_k)_{g_k(v)}
    tab = tab or prep(Gl)
    for v in V:
        for k in range(len(Gl)):
            gv, srcs = tab[(v, k)]
            if y[v][k] != f(gv, {w: y[src][k] for w, src in srcs}): return False
    return True


def embed(Gl, xs):  # xs[k] = configuration x^(g_k); returns y
    return {v: tuple(xs[k][g[v] - 1] for k, g in enumerate(Gl)) for v in V}


G2 = group([g2])
T2 = prep(G2)
WY = [y for y in (dict(zip(V, c)) for c in itertools.product(list(itertools.product([0, 1], repeat=2)), repeat=10)) if product_wins(G2, y, T2)]
emb = {tuple(sorted(embed(G2, xs).items())) for xs in itertools.product(Wset, repeat=2)}
case("<g2> product: winning set == embedded W x W (full 4^10 enumeration)", True,
     len(WY) == 64 ** 2 and {tuple(sorted(y.items())) for y in WY} == emb, "componentwise decoders; |W_Y| = |W|^|G|")
case("<g2> product objective: log_4 |W_Y| == log_2 |W| (exact integers)", True, len(WY) == len(Wset) ** 2, "log_{q^|G|} |W|^|G| = log_q |W|")


def Hcount(configs, S):
    c = defaultdict(int)
    for y in configs: c[tuple(y[v] for v in S)] += 1
    n = len(configs)
    return -sum(k / n * math.log2(k / n) for k in c.values())


subsets = [S for r in range(1, 11) for S in itertools.combinations(V, r)]
Wd = [dict(zip(V, x)) for x in Wset]
mx = max(abs(Hcount(WY, S) - (Hcount(Wd, S) + Hcount(Wd, tuple(sorted(g2[v] for v in S))))) for S in subsets)
case("<g2> product: H(Y_S) == H(X_S) + H(X_g2(S)) for all 1023 S (float, tol 1e-9)", True, mx < 1e-9, f"max deviation {mx:.3g}")
mi = max(abs(Hcount(WY, S) - Hcount(WY, tuple(sorted(g2[v] for v in S)))) for S in subsets)
case("<g2> product: H(Y_S) == H(Y_g2(S)) (float, tol 1e-9)", True, mi < 1e-9, f"max deviation {mi:.3g}")
mn = max(abs(Hcount(Wd, S) - Hcount(Wd, tuple(sorted(g2[v] for v in S)))) for S in subsets)
case("MUTATION unsymmetrised X: H(X_S) == H(X_g2(S)) for all S", False, mn < 1e-9, f"max asymmetry {mn:.3g} bits: symmetry rows need the product")
G8 = group([g1, g2])
case("|G| == 8 for <g1,g2>", True, len(G8) == 8, "")
case("full-G product decoder of every v reads exactly Y_N(v) (g(N(v)) = N(g(v)))", True, reads_only_neighbours(G8), "automorphism property makes the product a strategy on the same graph")
g2bad = dict(g2); g2bad[9], g2bad[10] = 10, 9
case("MUTATION product over {id, g2 with 9,10 swapped}: decoder reads only Y_N(v)", False, reads_only_neighbours([{v: v for v in V}, g2bad]), "non-automorphism forces reading a non-neighbour")
smp = [tuple(rnd.choice(Wset) for _ in range(8)) for _ in range(300)]
case("full-G product: 300 sampled elements of W^8 are winning for product strategy on alphabet 2^8", True,
     all(product_wins(G8, embed(G8, xs)) for xs in smp), "soundness direction on sample; only-if direction is componentwise")
bad = [list(xs) for xs in smp[:50]]
for b in bad: b[3] = tuple(1 - c if i == 6 else c for i, c in enumerate(b[3]))  # flip X_7 in copy k=3 (7 must be 0)
case("MUTATION full-G product with one component outside W is winning", False, any(product_wins(G8, embed(G8, xs)) for xs in bad), "a losing component makes Y lose")
out["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
out["all_as_expected"] = ok_all
(W / "ReviewF178RminusSources-ctl-copy-out.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
print("all_as_expected", ok_all, "cases", len(out["cases"]))
sys.exit(0 if ok_all else 1)
