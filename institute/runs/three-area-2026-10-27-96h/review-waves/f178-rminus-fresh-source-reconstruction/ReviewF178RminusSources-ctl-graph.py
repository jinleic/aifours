#!/usr/bin/env python3
"""ReviewF178RminusSources control 1: publisher Fig. 2 vector decoding, automorphisms, clique cover.

Exact, bounded. Inputs are reviewer-made renderings of the pinned publisher PDF (hash-pinned below).
Positive cases must pass; every mutation must fail for its stated reason. Exit 0 iff all expectations hold.
"""
import collections, csv, hashlib, itertools, json, math, pathlib, re, sys, time
import xml.etree.ElementTree as ET
from fractions import Fraction as F

W = pathlib.Path(__file__).resolve().parent
PINS = {
    "/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/public-sources/gurpinar-kybernetika60-2024-553-575.pdf":
        "373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8",
    str(W / "ReviewF178RminusSources-p18.svg"): "64142da3b73659d5085c072df2b01810d1b455b9f1149a3b30cb19e96402f9b7",
    str(W / "ReviewF178RminusSources-p18-words.tsv"): "0a96ad1a7c08dffedaa6190f9728aa4f35083383b6d112b3865d7680dee551cb",
}
out = {"control": "graph", "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "pins": {}, "cases": []}
ok_all = True


def case(name, expected, actual, reason):
    global ok_all
    passed = (expected == actual)
    ok_all &= passed
    out["cases"].append({"case": name, "expected": expected, "actual": actual, "as_expected": passed, "reason": reason})


for p, h in PINS.items():
    got = hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
    out["pins"][p] = {"expected": h, "actual": got, "ok": got == h}
    if got != h:
        print(json.dumps(out, indent=1)); sys.exit(2)

# ---- vector decoding of Fig. 2 (pdftocairo -svg of page 18) ----
root = ET.fromstring((W / "ReviewF178RminusSources-p18.svg").read_text())
tops = [c for c in root if c.tag.endswith("path")]
FIGT = "matrix(0.999096, 0, 0, -0.999096, 245.936549, 180.240056)"
fig = [p for p in tops if p.attrib.get("transform") == FIGT]
num = r"-?\d+\.?\d*(?:e-?\d+)?"


def tr(x, y):
    return (0.999096 * x + 245.936549, -0.999096 * y + 180.240056)


def parse(d):
    toks = re.findall(r"[MLCZ]|" + num, d); segs = []; cur = start = None; k = 0
    while k < len(toks):
        t = toks[k]
        if t == "M": cur = (float(toks[k + 1]), float(toks[k + 2])); start = cur; k += 3
        elif t == "L": q = (float(toks[k + 1]), float(toks[k + 2])); segs.append(("L", cur, q)); cur = q; k += 3
        elif t == "C":
            c1 = (float(toks[k + 1]), float(toks[k + 2])); c2 = (float(toks[k + 3]), float(toks[k + 4])); q = (float(toks[k + 5]), float(toks[k + 6]))
            segs.append(("C", cur, c1, c2, q)); cur = q; k += 7
        elif t == "Z":
            if cur != start: segs.append(("L", cur, start))
            cur = start; k += 1
        else: raise ValueError(t)
    return segs


def sample(seg, n=4000):
    if seg[0] == "L":
        (x0, y0), (x1, y1) = seg[1], seg[2]
        return [(x0 + (x1 - x0) * t / n, y0 + (y1 - y0) * t / n) for t in range(n + 1)]
    _, p0, p1, p2, p3 = seg; pts = []
    for k in range(n + 1):
        t = k / n; u = 1 - t
        pts.append((u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
                    u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1]))
    return pts


circles = []
for i, p in enumerate(fig):
    if p.attrib.get("fill", "none") != "none":
        v = [float(t) for t in re.findall(num, p.attrib["d"])]
        xs, ys = v[0::2], v[1::2]
        circles.append((i, (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2, (max(xs) - min(xs)) / 2))
words = [r for r in csv.DictReader(open(W / "ReviewF178RminusSources-p18-words.tsv"), delimiter="\t")
         if r["text"].isdigit() and 80 < float(r["top"]) < 240]
label_of = {}
label_margin = []
for r in words:
    c = (float(r["left"]) + float(r["width"]) / 2, float(r["top"]) + float(r["height"]) / 2)
    d = sorted((math.dist(c, tr(cx, cy)), i) for (i, cx, cy, _) in circles)
    label_of[d[0][1]] = int(r["text"]); label_margin.append((int(r["text"]), round(d[0][0], 2), round(d[1][0], 2)))
centers = {label_of[i]: (cx, cy, rad) for (i, cx, cy, rad) in circles}
case("ten node circles, ten distinct digit labels, bijective nearest-label map", True,
     len(circles) == 10 and sorted(label_of.values()) == list(range(1, 11)) and all(a < 10 < b for _, a, b in label_margin),
     f"label (nearest, second-nearest) distances pt: {sorted(label_margin)}")

strokes = []
for i, p in enumerate(fig):
    if p.attrib.get("fill", "none") != "none": continue
    for seg in parse(p.attrib["d"]):
        P = sample(seg); hits = []
        for v, (cx, cy, rad) in centers.items():
            ds = [math.dist(q, (cx, cy)) for q in P]; m = min(ds)
            if m <= rad + 0.5: hits.append((ds.index(m), v))
        strokes.append((p.attrib["stroke"], [v for _, v in sorted(hits)], seg[0]))
BLACK = "rgb(0%, 0%, 0%)"
EH, EC, WHITE = set(), set(), []
for col, seq, kind in strokes:
    if col != BLACK: WHITE.append(seq); continue
    for a, b in zip(seq, seq[1:]): EH.add(frozenset((a, b)))
    EC.add(frozenset((seq[0], seq[-1])))
through = [seq for col, seq, _ in strokes if col == BLACK and len(seq) > 2]
out["fig2"] = {"black_strokes": sum(1 for s in strokes if s[0] == BLACK), "pass_through_strokes": through, "white_strokes": WHITE,
               "edges_subdivided_reading": sorted(sorted(e) for e in EH), "edges_endpoint_reading": sorted(sorted(e) for e in EC)}

BUNDLE = "12 13 14 15 16 17 23 27 29 2-10 34 38 39 45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10".split()
EB = {frozenset(map(int, t.split("-"))) if "-" in t else frozenset((int(t[0]), int(t[1]))) for t in BUNDLE}
NT = {1: [2, 3, 4, 5, 6, 7], 2: [1, 3, 7, 9, 10], 3: [1, 2, 4, 8, 9], 4: [1, 3, 5, 8, 10], 5: [1, 4, 6, 9, 10],
      6: [1, 5, 7, 8, 9], 7: [1, 2, 6, 8, 10], 8: [3, 4, 6, 7, 9, 10], 9: [2, 3, 5, 6, 8], 10: [2, 4, 5, 7, 8]}
ENT = {frozenset((v, u)) for v, l in NT.items() for u in l}
case("bundle 26-edge list == bundle neighbourhood table (symmetric)", True,
     EB == ENT and len(EB) == 26 and all(v in NT[u] for v, l in NT.items() for u in l), "two bundle encodings agree")
case("Fig.2 subdivided reading == bundle 26 edges", True, EH == EB, "pass-through strokes read as paths through mid-side nodes")
case("MUTATION Fig.2 endpoint-only (chord) reading == bundle", False, EC == EB, "chords 2-4,2-6,4-6 replace hexagon 2-3-4-5-6-7")
case("9-10 drawn only in white (invisible), i.e. absent", True, [10, 9] in WHITE or [9, 10] in WHITE, "R minus edge 9<->10")

V = list(range(1, 11))


def cyc(s):
    p = {v: v for v in V}
    for c in re.findall(r"\(([^)]*)\)", s):
        parts = c.split(); el = [int(x) for x in parts] if len(parts) > 1 else [int(ch) for ch in parts[0]]
        for k in range(len(el)): p[el[k]] = el[(k + 1) % len(el)]
    return p


g1 = {i + 1: x for i, x in enumerate([8, 10, 7, 6, 9, 3, 4, 1, 2, 5])}
g2 = {i + 1: x for i, x in enumerate([1, 5, 6, 7, 2, 3, 4, 8, 9, 10])}
sigma, tau = cyc("(18)(2 10 5 9)(3746)"), cyc("(25)(36)(47)")
case("bundle g1 == publisher sigma, g2 == publisher tau (Appendix B)", True, g1 == sigma and g2 == tau, "cycle notation transcribed from layout lines 1143-1146")


def is_aut(p, E):
    return sorted(p.values()) == V and all(frozenset((p[a], p[b])) in E for a, b in map(tuple, E))


def closure(gens):
    G = {tuple(V)}; fr = [tuple(V)]
    while fr:
        nw = []
        for x in fr:
            for g in gens:
                y = tuple(g[x[i]] for i in range(10))
                if y not in G: G.add(y); nw.append(y)
        fr = nw
    return G


def all_auts(E):
    deg = {v: sum(1 for e in E if v in e) for v in V}; res = []
    def bt(k, p, used):
        if k == 11: res.append(tuple(p[v] for v in V)); return
        for w in V:
            if w in used or deg[w] != deg[k]: continue
            if all((frozenset((p[u], w)) in E) == (frozenset((u, k)) in E) for u in range(1, k)):
                p[k] = w; used.add(w); bt(k + 1, p, used); used.discard(w); del p[k]
    bt(1, {}, set()); return set(res)


G = closure([g1, g2])
case("|<g1,g2>| == 8 and every element an automorphism of bundle graph", True, len(G) == 8 and all(is_aut({v: x[v - 1] for v in V}, EB) for x in G), "group closure")
case("full Aut(bundle graph) == <g1,g2> (publisher: Aut(R-) = <sigma,tau>)", True, all_auts(EB) == G, "backtracking enumeration")
case("MUTATION chord reading: sigma automorphism", False, is_aut(sigma, EC), "publisher group statement selects subdivided reading")
case("MUTATION chord reading: |Aut| == 8", False, len(all_auts(EC)) == 8, "chord reading has |Aut| = %d" % len(all_auts(EC)))
RH = EB | {frozenset((9, 10))}
pubR = [cyc("(25)(36)(47)"), cyc("(26)(35)(8 10)"), cyc("(24)(57)(89)")]
case("R = bundle + 9-10: Aut(R) == publisher <(25)(36)(47),(26)(35)(8 10),(24)(57)(89)>", True, all_auts(RH) == closure(pubR), "cross-check of R via Appendix B line 1149")
case("MUTATION R from chord reading: Aut == publisher group", False, all_auts(EC | {frozenset((9, 10))}) == closure(pubR), "chord reading inconsistent with Aut(R)")
case("MUTATION drop edge 3-4: g1 still automorphism", False, is_aut(g1, EB - {frozenset((3, 4))}), "g1 maps 3-4 to 7-6")
case("MUTATION add edge 9-10: g1 still automorphism", False, is_aut(g1, RH), "g1 maps 9-10 to 2-5, a non-edge")
g2bad = dict(g2); g2bad[9], g2bad[10] = 10, 9
case("MUTATION g2 with images of 9,10 swapped is automorphism", False, is_aut(g2bad, EB), "9-10 transposition breaks adjacency")
lab_swap = {**{v: v for v in V}, 3: 7, 7: 3}
case("MUTATION label swap 3<->7 leaves edge set unchanged", False, {frozenset(lab_swap[x] for x in e) for e in EH} == EB, "labels are load-bearing")


def cliques(E):
    return [S for k in range(1, 11) for S in itertools.combinations(V, k) if all(frozenset(pr) in E for pr in itertools.combinations(S, 2))]


def tri3(E):
    tris = [S for S in cliques(E) if len(S) == 3]; sol = []
    def bt(s, cnt, ch):
        if len(ch) == 10:
            if all(c == 3 for c in cnt.values()): sol.append(list(ch)); return True
            return False
        for i in range(s, len(tris)):
            t = tris[i]
            if all(cnt[v] < 3 for v in t):
                for v in t: cnt[v] += 1
                ch.append(t)
                if bt(i + 1, cnt, ch): return True
                ch.pop()
                for v in t: cnt[v] -= 1
        return False
    bt(0, collections.Counter({v: 0 for v in V}), []); return sol[0] if sol else None


for nm, E in [("R-", EB), ("R", RH)]:
    om = max(len(c) for c in cliques(E)); cov = tri3(E)
    case(f"cp_f({nm}) == 10/3 by exact primal 3-fold triangle cover and dual y=1/3 (omega<=3)", True,
         om == 3 and cov is not None and all(sum(F(1, 3) for t in cov if v in t) == 1 for v in V),
         f"omega={om}; cover={cov}; lower bound 10-10/3=20/3 (publisher lines 901-902)")
# symmetrisation algebra: S -> sum_{g in G} h(g S) is G-invariant for arbitrary h; fails for a non-subgroup
import random
rnd = random.Random(178)
subsets = [frozenset(S) for k in range(1, 11) for S in itertools.combinations(V, k)]
h = {S: F(rnd.randint(1, 10 ** 6), rnd.randint(1, 1000)) for S in subsets}
def sym_avg(Gset):
    return {S: sum(h[frozenset(x[v - 1] for v in S)] for x in Gset) for S in subsets}
hy = sym_avg(G)
case("sum_g h(g(S)) over G is invariant under g1 and g2 (all 1023 S, exact)", True,
     all(hy[S] == hy[frozenset(g[v] for v in S)] for S in subsets for g in (g1, g2)), "reindexing g -> g*k is a bijection of a group")
nonsub = {tuple(V), tuple(g1[v] for v in V)}
hn = sym_avg(nonsub)
case("MUTATION non-subgroup {id,g1}: invariance under g1", False, all(hn[S] == hn[frozenset(g1[v] for v in S)] for S in subsets), "needs closure under composition")
out["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
out["all_as_expected"] = ok_all
(W / "ReviewF178RminusSources-ctl-graph-out.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
print("all_as_expected", ok_all, "cases", len(out["cases"]))
sys.exit(0 if ok_all else 1)
