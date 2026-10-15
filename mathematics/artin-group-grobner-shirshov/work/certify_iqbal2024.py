"""All-lengths certification of the (misprint-corrected) complete presentation of
the Artin monoid of type B3 = MB_{1,3} from Iqbal-Munir-Ayub-Nizami, Rev. Un.
Mat. Argentina 67(2) (2024) 503-516, Thm 2.3 (see check_iqbal2024.py for the
misprints: R3, R6, R9 need z2^(n+1) on the left).

Letters a=z1 < b=z2 < c=z3; our order [2,1,0] of Bourbaki B3.  Exponents n_i >= 1
(R1: n >= 0), T = empty or b{a,b}* (the tails of R9-R11).

Checks:
 (V) validity for all parameters: conjugation/transport identities in the group
     (Garside normal form) for the T-free families, plus x.cbabc = cbabc.x
     (x = a, b), which moves an arbitrary tail T through cbabc;
 (G) growth certificate for the MONOID: words avoiding all leading words are
     counted by a DFA with K states; compared with M(t) = 1/D(t) up to K+N+2;
     equality => Irr = lexmin words => GS basis (Lemma 1, monoid version);
 (L) inclusion of the exact minimal-non-lexmin automaton language (Theorem B,
     monoid) in the leading-word language.
Usage: python3 work/certify_iqbal2024.py
"""
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from automaton import NFAutomaton, build_table  # noqa: E402
from certify import NFA, check_validity  # noqa: E402
from coxeter import build  # noqa: E402
from gs_oracle import growth_counts  # noqa: E402

G = build("B", 3, 0, [2, 1, 0])
FREE = ("ab", "FREE")

# (name, lhs parts, rhs parts) ; ("w", p) loop, FREE = any word over {a,b}
P = lambda w: (w, None)  # noqa: E731
FAMS = [
    ("R0", [P("ca")], [P("ac")]),
    ("Rbr1", [P("cbc")], [P("bcb")]),
    ("Rbr2", [P("baba")], [P("abab")]),
    ("R1", [P("ba"), ("a", "n"), P("bab")], [P("ababb"), ("a", "n")]),
    ("R2", [P("cba"), ("a", "n"), P("c")], [P("bcba"), ("a", "n")]),
    ("R3", [P("cbb"), ("b", "n"), P("cb")], [P("bcbbc"), ("c", "n")]),
    ("R4", [P("cba"), ("a", "n"), P("b"), ("b", "m"), P("cb")],
     [P("bcba"), ("a", "n"), P("bc"), ("c", "m")]),
    ("R5", [P("cbab"), ("b", "n"), P("cb")], [P("bcbabc"), ("c", "n")]),
    ("R6", [P("cbb"), ("b", "n"), P("a"), ("a", "m"), P("cbab")],
     [P("bcbbac"), ("c", "n"), P("ba"), ("a", "m")]),
    ("R7", [P("cba"), ("a", "n"), P("b"), ("b", "m"), P("a"), ("a", "k"), P("cbab")],
     [P("bcba"), ("a", "n"), P("bac"), ("c", "m"), P("ba"), ("a", "k")]),
    ("R8", [P("cbab"), ("b", "n"), P("a"), ("a", "m"), P("cbab")],
     [P("bacbabc"), ("c", "n"), P("ba"), ("a", "m")]),
]
# tail families: T = "" or "b"+FREE inserted before the final cbabc, appended after the final c
TAILS = [
    ("R9", [P("cbb"), ("b", "n"), P("a"), ("a", "m")], [P("bcbbac"), ("c", "n"), P("ba"), ("a", "m"), P("c")]),
    ("R10", [P("cba"), ("a", "n"), P("b"), ("b", "m"), P("a"), ("a", "k")],
     [P("bcba"), ("a", "n"), P("bac"), ("c", "m"), P("ba"), ("a", "k"), P("c")]),
    ("R11", [P("cbab"), ("b", "n"), P("a"), ("a", "m")], [P("bacbabc"), ("c", "n"), P("ba"), ("a", "m"), P("c")]),
]


def main():
    rep = {}
    # (V) T-free validity (all parameters >= 0 in this decomposition)
    val = {}
    for name, l, r in FAMS:
        val[name] = check_validity(G, (name, l, r))[0]
    for name, l, r in TAILS:
        val[name + "(T=empty)"] = check_validity(G, (name, l + [P("cbabc")], r))[0]
    comm = {x: G.nf(x + "cbabc") == G.nf("cbabc" + x) for x in "ab"}
    rep["validity"] = val
    rep["tail_commutation x.cbabc=cbabc.x"] = comm
    # leading-word NFA (with FREE tails)
    N = NFA()
    for name, l, r in FAMS:
        N.add_family(l)
    for name, l, r in TAILS:
        N.add_family(l + [P("cbabc")])
        # T = b{a,b}* : build manually
        s = 0
        for w, p in l + [P("b")]:
            if p is None:
                for ch in w:
                    t = N.new()
                    N.add(s, ch, t)
                    s = t
            else:
                N.add(s, w, s)
        for ch in "ab":
            N.add(s, ch, s)
        for ch in "cbabc":
            t = N.new()
            N.add(s, ch, t)
            s = t
        N.final.add(s)
    gens = ["a", "b", "c"]
    # (G) monoid growth certificate
    start = frozenset([0])
    states, trans, todo = {start: 0}, {}, [start]
    while todo:
        S = todo.pop()
        for ch in gens:
            T = N.step(S, ch) | {0}
            if T & N.final:
                trans[(S, ch)] = None
                continue
            T = frozenset(T)
            trans[(S, ch)] = T
            if T not in states:
                states[T] = len(states)
                todo.append(T)
    K = len(states)
    Lg = K + G.W.N + 2
    cur, counts = {start: 1}, [1]
    for _ in range(Lg):
        nxt = {}
        for S, k in cur.items():
            for ch in gens:
                T = trans[(S, ch)]
                if T is not None:
                    nxt[T] = nxt.get(T, 0) + k
        cur = nxt
        counts.append(sum(cur.values()))
    Mt = growth_counts(G.W, Lg, "monoid")
    rep["growth_certificate_monoid"] = {"dfa_states": K, "checked_up_to": Lg, "equal": counts == Mt}
    # (L) inclusion MinRed(monoid) subset of Lead
    A = NFAutomaton(build_table("B", 3, 0, [2, 1, 0]), monoid=True)
    init = ("init",)
    seen, todo, ok = {(start, init)}, [(start, init)], True
    while todo and ok:
        S, Pst = todo.pop()
        if Pst == ("acc",) and not (S & N.final):
            ok = False
            break
        for y, ch in enumerate(gens):
            S2 = N.step(S, ch)
            if Pst == init:
                P2 = (A.step(frozenset(), y), frozenset())
            elif Pst in (("acc",), ("dead",)):
                continue
            else:
                Of, Os = Pst
                Os2 = A.step(Os, y)
                if Os2 is None:
                    continue
                Of2 = A.step(Of, y)
                P2 = ("acc",) if Of2 is None else (Of2, Os2)
            st = (S2, P2)
            if st not in seen:
                seen.add(st)
                todo.append(st)
    rep["minred_subset_of_leading_words"] = {"holds": ok, "product_states": len(seen)}
    rep["ALL_OK"] = all(val.values()) and all(comm.values()) and rep["growth_certificate_monoid"]["equal"] and ok
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    main()
