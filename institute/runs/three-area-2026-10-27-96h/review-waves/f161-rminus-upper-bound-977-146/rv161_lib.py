"""Reviewer-authored (wave f161) independent semantics for the R-minus entropy LP.

Nothing here is imported from, copied from, or executed from author code.
Sources of truth used:
  * Graph R: Baber-Christofides-Dang-Riis-Vaughan, arXiv:1410.8349 e-print,
    figure file RGraph.ps (edges = stroked paths between the ten vertex discs;
    vertex labels read from the rendered figure).  R^- = R minus the undirected
    edge {9,10} (TeX source, "the graph R^- which is identical to R but with the
    undirected edge between vertices 9 and 10 removed").
  * Vertex names a..j = 1..10, copy-branch structure and extra single copies:
    the candidate packets' prose (upper-bound-10834-1619-v1.md, addendum-1).
  * Copy Lemma: DFZ arXiv:1104.3602 Lemma (C1 marginal equality, C2 CI).
"""
import hashlib
import re
from fractions import Fraction

ORIG = list("abcdefghij")
NUMV = {i + 1: ch for i, ch in enumerate(ORIG)}
VNUM = {ch: i + 1 for i, ch in enumerate(ORIG)}

RGRAPH_PS_SHA256 = "0913813c0e110f1ec2d29b3839bad7b6f0ddeaa29ff57dac830b257b1279a403"
# Vertex disc centres in the stroke coordinate system (after "1 0 0 -1 0 284 cm"),
# labelled from the rendered figure (rv161-RGraph-render.png).
PS_VERTEX_LABELS = {
    (200.0, 182.84): 1, (200.0, 110.219): 2, (231.445, 164.684): 3,
    (262.891, 219.148): 4, (200.0, 219.148): 5, (137.109, 219.148): 6,
    (168.555, 164.684): 7, (200.0, 25.289): 8, (336.441, 261.613): 9,
    (63.559, 261.613): 10,
}


def parse_rgraph_edges(ps_path):
    raw = open(ps_path, "rb").read()
    if hashlib.sha256(raw).hexdigest() != RGRAPH_PS_SHA256:
        raise SystemExit("RGraph.ps hash mismatch")
    text = raw.decode("ascii")
    strokes = re.findall(r"q 1 0 0 -1 0 284 cm\s+(.*?)\sS Q", text, flags=re.S)
    edges, frame = set(), 0
    for s in strokes:
        toks = s.split()
        i = toks.index("m")
        a = (float(toks[i - 2]), float(toks[i - 1]))
        b = (float(toks[-3]), float(toks[-2]))
        if a in PS_VERTEX_LABELS and b in PS_VERTEX_LABELS:
            u, v = PS_VERTEX_LABELS[a], PS_VERTEX_LABELS[b]
            assert u != v
            e = frozenset((u, v))
            assert e not in edges, "duplicate stroke"
            edges.add(e)
        else:
            frame += 1
    assert frame == 1, "expected exactly one non-edge stroke (page frame)"
    return edges


def graph_checks(E_R):
    """Consistency checks of the parsed figure against statements in the BCDRV TeX."""
    E_Rm = E_R - {frozenset((9, 10))}
    out = {"R_edges": len(E_R), "Rminus_edges": len(E_Rm)}
    tri = [(1, 2, 3), (1, 4, 5), (1, 6, 7), (2, 3, 9), (2, 7, 10), (3, 8, 9),
           (4, 5, 10), (4, 8, 10), (5, 6, 9), (6, 7, 8)]
    out["clique_cover_triangles_are_cliques_in_Rminus"] = all(
        frozenset((x, y)) in E_Rm for t in tri for x in t for y in t if x < y)
    out["edge_9_10_in_R"] = frozenset((9, 10)) in E_R
    out["edge_3_8_in_R"] = frozenset((3, 8)) in E_R          # R_c^- removes {3,8}
    out["vertex1_nonadjacent_8_9_10"] = all(frozenset((1, x)) not in E_R for x in (8, 9, 10))  # R^S adds 1->8,9,10
    return E_Rm, out


def neighbourhoods(E):
    N = {v: set() for v in range(1, 11)}
    for e in E:
        u, v = tuple(e)
        N[u].add(v)
        N[v].add(u)
    return N


def automorphisms(E):
    N = neighbourhoods(E)
    deg = {v: len(N[v]) for v in N}
    res = []

    def bt(i, mp, used):
        if i > 10:
            res.append(dict(mp))
            return
        for w in range(1, 11):
            if w in used or deg[w] != deg[i]:
                continue
            if all((frozenset((u, i)) in E) == (frozenset((mp[u], w)) in E) for u in range(1, i)):
                mp[i] = w
                used.add(w)
                bt(i + 1, mp, used)
                used.discard(w)
                del mp[i]

    bt(1, {}, set())
    return res


def fs(*xs):
    return frozenset(xs)


# Copy steps exactly as worded in the packet (copy-vars, copied originals, over-set).
COPYSTEPS = {
    ("b'0",): dict(orig=("b",), over=fs(*"adefghij")),
    ("d'1", "e'1"): dict(orig=("d", "e"), over=fs(*"abcfghi")),
    ("g'2",): dict(orig=("g",), over=fs("a", "b", "c", "d", "e'1", "f", "h", "i")),
    ("f'3", "g'3"): dict(orig=("f", "g"), over=fs(*"abcdehij")),
    ("h'4",): dict(orig=("h",), over=fs("a", "b", "c", "d", "e", "f", "f'3", "i", "j")),
}
BRANCHVARS = {
    1: ORIG + ["b'0"],
    2: ORIG + ["d'1", "e'1", "g'2"],
    3: ORIG + ["f'3", "g'3", "h'4"],
}
# All variables existing when the copy step is performed (Copy Lemma "D" = all of them minus over-set).
EXIST_BEFORE = {
    ("b'0",): set(ORIG),
    ("d'1", "e'1"): set(ORIG),
    ("g'2",): set(ORIG) | {"d'1", "e'1"},
    ("f'3", "g'3"): set(ORIG),
    ("h'4",): set(ORIG) | {"f'3", "g'3"},
}


def mask2set(L, mask):
    assert mask >= 0 and mask < (1 << len(L))
    return frozenset(L[k] for k in range(len(L)) if (mask >> k) & 1)


def addh(expr, S, coef):
    S = frozenset(S)
    if S:
        expr[S] = expr.get(S, 0) + coef


def clean(e):
    return {S: v for S, v in e.items() if v != 0}


def cmi_expr(X, Y, Z):
    X, Y, Z = frozenset(X), frozenset(Y), frozenset(Z)
    e = {}
    addh(e, X | Z, 1)
    addh(e, Y | Z, 1)
    addh(e, X | Y | Z, -1)
    addh(e, Z, -1)
    return clean(e)


def dfz_expr(co, A, B, C, D, Z):
    """RHS - LHS of the DFZ four-copy form (arXiv:1104.3602 Sec. FourCopies), every term conditioned on Z:
    b I(A;B|C) + c I(A;C|B) + d I(B;C|A) + e I(A;B|D) + f I(A;D|B) + g I(B;D|A) + h I(C;D) + i I(C;D|A) - a I(A;B)."""
    a_, b_, c_, d_, e_, f_, g_, h_, i_ = co
    terms = [(b_, A, B, C | Z), (c_, A, C, B | Z), (d_, B, C, A | Z), (e_, A, B, D | Z), (f_, A, D, B | Z),
             (g_, B, D, A | Z), (h_, C, D, Z), (i_, C, D, A | Z), (-a_, A, B, Z)]
    e = {}
    for k, X, Y, W in terms:
        if k:
            for S, v in cmi_expr(X, Y, W).items():
                addh(e, S, k * v)
    return clean(e)


# Orientation of equality rows.  Equality multipliers are sign-free, so orientation does not
# affect validity; these are the orientations under which the stored multipliers match.
CONV = dict(fd=1, copy=1, indep=-1, sym=1, xcopy=1, xindep=-1)


def build_row(r, cert, ctx):
    """Return (linear form as {frozenset: int}, kind) with kind in {'ineq','eq','cap'}."""
    NB, gens, conv = ctx["NB"], ctx["gens"], ctx["conv"]
    k = r[0]
    if k == "cmi":
        L, i, j, mask = r[1], r[2], r[3], r[4]
        assert len(set(L)) == len(L) and i != j and not (mask >> i) & 1 and not (mask >> j) & 1
        assert tuple(L) in ctx["allowed_lists"], L
        return cmi_expr({L[i]}, {L[j]}, mask2set(L, mask)), "ineq"
    if k == "mono":
        L, i = r[1], r[2]
        assert tuple(L) in ctx["allowed_lists"], L
        e = {}
        addh(e, set(L), 1)
        addh(e, set(L) - {L[i]}, -1)
        return clean(e), "ineq"
    if k == "fd":
        v = NUMV[r[1]]
        e = {}
        addh(e, NB[v] | {v}, conv["fd"])
        addh(e, NB[v], -conv["fd"])
        return clean(e), "eq"
    if k == "cap":
        return {frozenset({NUMV[r[1]]}): 1}, "cap"
    if k == "copy":
        cv, sel, mask = tuple(r[1]), r[2], r[3]
        st = COPYSTEPS[cv]
        L = [BRANCHVARS[b] for b in BRANCHVARS if cv[0] in BRANCHVARS[b]][0]
        T = mask2set(L, mask)
        assert T <= st["over"], (cv, T)
        assert 1 <= sel < (1 << len(cv))
        Wc = {cv[t] for t in range(len(cv)) if (sel >> t) & 1}
        Wo = {st["orig"][t] for t in range(len(cv)) if (sel >> t) & 1}
        e = {}
        addh(e, Wc | T, conv["copy"])
        addh(e, Wo | T, -conv["copy"])
        return clean(e), "eq"
    if k == "independence":
        cv = tuple(r[1])
        st = COPYSTEPS[cv]
        rest = EXIST_BEFORE[cv] - st["over"]
        return {S: conv["indep"] * v for S, v in cmi_expr(set(cv), rest, st["over"]).items()}, "eq"
    if k == "sym":
        g = gens[r[1]]
        S = mask2set(ORIG, r[2])
        gS = frozenset(g[x] for x in S)
        e = {}
        addh(e, S, conv["sym"])
        addh(e, gS, -conv["sym"])
        return clean(e), "eq"
    if k == "dfz":
        co = r[1]
        A, B, C, D, Z = [mask2set(ORIG, m) for m in r[2:7]]
        assert tuple(co) in ctx["dfz_tuples"], co
        return dfz_expr(co, A, B, C, D, Z), "ineq"
    if k == "dfzb":
        assert r[1] == "b1"
        co = r[2]
        A, B, C, D, Z = [mask2set(BRANCHVARS[1], m) for m in r[3:8]]
        assert tuple(co) in ctx["dfz_tuples"], co
        return dfz_expr(co, A, B, C, D, Z), "ineq"
    if k == "xcopy":
        kk, mask = r[1], r[2]
        Sx, Tx = cert["extra_single_copies"][kk]
        assert len(Sx) == 1
        name = "s'%d" % kk
        Sset = {NUMV[v] for v in Sx}
        Tset = {NUMV[v] for v in Tx}
        U = mask2set(ORIG, mask)
        assert U <= Tset
        e = {}
        addh(e, {name} | U, conv["xcopy"])
        addh(e, Sset | U, -conv["xcopy"])
        return clean(e), "eq"
    if k == "xindependence":
        kk = r[1]
        Sx, Tx = cert["extra_single_copies"][kk]
        name = "s'%d" % kk
        Tset = {NUMV[v] for v in Tx}
        rest = set(ORIG) - Tset
        return {S: conv["xindep"] * v for S, v in cmi_expr({name}, rest, Tset).items()}, "eq"
    raise ValueError("unknown row kind %r" % (k,))


def check_certificate(cert, ctx, objective=None):
    """Exact check: sum_i w_i row_i == h(V) coefficientwise; signs; bound = sum of cap multipliers."""
    tot, sign_violations, capsum, kinds = {}, [], Fraction(0), {}
    for idx, m in enumerate(cert["multipliers"]):
        w = Fraction(m["multiplier"])
        e, typ = build_row(m["row"], cert, ctx)
        kinds[m["row"][0]] = kinds.get(m["row"][0], 0) + 1
        if typ == "ineq" and w > 0:
            sign_violations.append(idx)
        if typ == "cap":
            if w < 0:
                sign_violations.append(idx)
            capsum += w
        for S, v in e.items():
            tot[S] = tot.get(S, 0) + w * v
    obj = objective if objective is not None else {frozenset(ORIG): 1}
    for S, v in obj.items():
        tot[S] = tot.get(S, 0) - v
    resid = {S: v for S, v in tot.items() if v != 0}
    return dict(residual_nonzero_coordinates=len(resid),
                residual_l1=str(sum(abs(v) for v in resid.values())),
                residual_sample=sorted(("".join(sorted(S)), str(v)) for S, v in resid.items())[:8],
                sign_violations=len(sign_violations), sign_violation_rows=sign_violations[:8],
                cap_sum=str(capsum), kinds=kinds)
