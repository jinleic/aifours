"""Extract explicit parametrized families of the reduced GS basis (positive part)
from the exact pair automaton, when every cyclic SCC of the trimmed automaton is
a single state with one self-loop letter ("bounded" case; e.g. B3 order 0,2,1 or
D4 with the centre largest).

Each accepting path through the condensation gives a family
    LHS = u0 x1^k1 u1 ... xr^kr ur   (k_i >= 0; x_i = loop letter of the i-th loop state).
Right sides are fitted to the transport form  RHS = R y1^k1 ... yr^kr  using the
Garside normal form (R = NF at k = 0, y_i from k = e_i), and the fit is checked on
random parameter vectors.  The output spec is certified independently by
work/certify.py (validity for all k, growth certificate, language equality).

Usage: python3 work/extract_families.py TYPE n --order 0,2,3,1 > work/specs_TYPE.json
"""
import argparse
import json
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from automaton import NFAutomaton, build_table  # noqa: E402
from classify import ACC, pair_graph, sccs, trim  # noqa: E402
from coxeter import build, letter  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("typ")
    ap.add_argument("n", type=int)
    ap.add_argument("--m", type=int, default=0)
    ap.add_argument("--order", required=True)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    order = [int(x) for x in a.order.split(",")]
    T = build_table(a.typ, a.n, a.m, order)
    A = NFAutomaton(T)
    G = build(a.typ, a.n, a.m, order)
    from fastnf import FastGarside
    FG = FastGarside(T)
    start, edges = pair_graph(A)
    g = trim(start, edges)
    comps = sccs(g)
    loop = {}
    for c in comps:
        cs = set(c)
        internal = [(v, y, w) for v in c for y, w in g[v] if w != ACC and w in cs]
        if not internal:
            continue
        if len(c) != 1 or len(internal) != 1:
            sys.exit("automaton not of bounded single-letter-loop shape")
        v, y, _w = internal[0]
        loop[v] = y
    # initial transitions: from 'init' reading y goes to (A.step(empty,y), empty)
    init_edges = []
    for y in range(T.n):
        O1 = A.step(frozenset(), y)
        if O1 is not None and (O1, frozenset()) in g:
            init_edges.append((y, (O1, frozenset())))
    fams = []

    def dfs(state, parts):
        # parts: list of [word, loopletter_or_None]
        if state in loop:
            parts = parts + [(letter(loop[state]), "LOOP")]
        for y, w in g[state]:
            if w != ACC and w == state:
                continue
            p2 = parts + [(letter(y), None)]
            if w == ACC:
                fams.append(p2)
            else:
                dfs(w, p2)

    for y, s in init_edges:
        dfs(s, [(letter(y), None)])
    rng = random.Random(a.seed)

    def runs(w):
        out = []
        for ch in w:
            if out and out[-1][0] == ch:
                out[-1][1] += 1
            else:
                out.append([ch, 1])
        return out

    def inst(lhs, vals):
        return "".join(w * (vals[p] if p else 1) for w, p in lhs)

    def fit(lhs, names):
        """RHS as fixed words and runs y^(k_i + c_i), c_i >= 0, parameters in LHS order."""
        if not names:
            return [(FG.nf(inst(lhs, {})), None)]
        base = {nm: 3 + 2 * j for j, nm in enumerate(names)}
        rb = runs(FG.nf(inst(lhs, base)))
        where = {}
        for nm in names:
            ri = runs(FG.nf(inst(lhs, dict(base, **{nm: base[nm] + 1}))))
            if len(ri) != len(rb):
                return None
            diff = [j for j in range(len(rb)) if ri[j] != rb[j]]
            if len(diff) != 1 or ri[diff[0]][1] != rb[diff[0]][1] + 1:
                return None
            where[nm] = diff[0]
        parts = []
        for j, (ch, ln) in enumerate(rb):
            ps = [nm for nm in names if where[nm] == j]
            c = ln - sum(base[nm] for nm in ps)
            if c < 0:
                return None
            if c:
                parts.append((ch * c, None))
            for nm in ps:
                parts.append((ch, nm))
        merged = []
        for w, p in parts:
            if p is None and merged and merged[-1][1] is None:
                merged[-1] = (merged[-1][0] + w, None)
            else:
                merged.append((w, p))
        for _ in range(25):
            vals = {nm: rng.choice([0, 0, 1, 1, 2, 3, 5]) for nm in names}
            if FG.nf(inst(lhs, vals)) != inst(merged, vals):
                return None
        return merged

    def normalize_lhs(parts):
        lhs, names = [], []
        for w, p in parts:
            if p is None:
                if lhs and lhs[-1][1] is None:
                    lhs[-1] = (lhs[-1][0] + w, None)
                else:
                    lhs.append((w, None))
            else:
                nm = f"k{len(names) + 1}"
                names.append(nm)
                lhs.append((w, nm))
        return lhs, names

    def solve(parts, depth=0):
        """Fit; on failure split the first loop into (absent) and (one fixed copy + loop)."""
        lhs, names = normalize_lhs(parts)
        rhs = fit(lhs, names)
        if rhs is not None:
            return [(lhs, rhs)]
        if depth > 2 or not names:
            return [(lhs, None)]
        for j, (w, p) in enumerate(parts):
            if p == "LOOP":
                without = parts[:j] + parts[j + 1:]
                with_one = parts[:j] + [(w, None), (w, "LOOP")] + parts[j + 1:]
                # try splitting this loop; keep the first split that helps
                r0, r1 = solve(without, depth + 1), solve(with_one, depth + 1)
                if all(r is not None for _l, r in r0 + r1):
                    return r0 + r1
        return [(lhs, None)]

    out = []
    for parts in fams:
        for lhs, rhs in solve(parts):
            out.append({"name": f"P{len(out) + 1}", "lhs": lhs, "rhs": rhs, "fitted": rhs is not None})
    print(json.dumps({"type": [a.typ, a.n, a.m], "order": order, "phi": G.W.phi,
                      "delta_word": G.delta_word(), "loop_states": len(loop),
                      "families": out}, indent=0))


if __name__ == "__main__":
    main()
