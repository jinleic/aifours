"""Certify that an explicit parametrized family list S (specs.py) is a
Groebner-Shirshov basis of the Artin group A(W) in the Artin-Garside alphabet,
for ALL parameter values / all word lengths.

Checks (each independent of the others):
 (V) validity: every instance LHS(p) = RHS(p) holds in A(W) for all p >= 0.
     Moving each power to the far right by conjugation, LHS = (A0...Ar) g_1^p1...g_r^pr
     with g_k = C_k^-1 x_k C_k, C_k = Ak...Ar (and similarly for the RHS, whose
     parameters may occur in another order); sufficient group identities:
     A-part = B-part, g_p = h_p, and g_p g_q = g_q g_p for swapped pairs, each
     decided by the Garside normal form in A(W) (coxeter.py).  Optional second
     proof (V2, check_transport): the same with positive braid-move identities,
     when every loop letter transports to a letter.
 (O) order: RHS(p) < LHS(p) in deg-lex for all p (first letter of the fixed
     prefix of RHS smaller, or RHS strictly shorter for all p).
 (G) growth certificate (CD lemma): the S-irreducible words are counted by a
     finite automaton (rational generating function, K states) and the counts
     are compared with the growth series of A(W) w.r.t. {s_i, Delta^+-1},
     (1-t^N) M(t) (1+t)/(1-t), up to length K+N+2.  Equality of the rational
     functions follows, so Irr(S) = normal forms, so S is a GS basis.
 (L) language equality of the positive leading words with the exact
     minimal-reducible-word automaton of automaton.py (independent route via
     the right-complement characterisation).
 (R) reducedness: no right side contains a leading word (for all p).
 (E) explicit cross-check against the oracle's reduced basis up to length Lmax.

Usage: python3 work/certify.py SPEC [--Lmax 13]
"""
from __future__ import annotations

import argparse
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from automaton import NFAutomaton, build_table  # noqa: E402
from coxeter import build  # noqa: E402
from gs_oracle import enumerate_basis, growth_counts  # noqa: E402
from specs import SPECS  # noqa: E402


def inv_word(w: str) -> str:
    out = []
    for c in reversed(w):
        if c == "1":
            out.append("0")
        elif c == "0":
            out.append("1")
        elif c.islower():
            out.append(c.upper())
        else:
            out.append(c.lower())
    return "".join(out)


def split(parts):
    """-> (fixed words A0..Ar, loop words x1..xr, param names)"""
    fixed, loops, names = [""], [], []
    for w, p in parts:
        if p is None:
            fixed[-1] += w
        else:
            loops.append(w)
            names.append(p)
            fixed.append("")
    return fixed, loops, names


def instantiate(parts, vals):
    return "".join(w * (vals[p] if p is not None else 1) for w, p in parts)


def expand(fam):
    """Human form (name, lhs, rhs, mins) -> internal form with all parameters >= 0."""
    name, lhs, rhs, mins = fam

    def ex(parts):
        out = []
        for w, p in parts:
            if p is None:
                out.append((w, None))
            else:
                if mins.get(p, 0):
                    out.append((w * mins[p], None))
                out.append((w, p))
        # merge adjacent fixed words
        merged = []
        for w, p in out:
            if p is None and merged and merged[-1][1] is None:
                merged[-1] = (merged[-1][0] + w, None)
            else:
                merged.append((w, p))
        return merged

    return name, ex(lhs), ex(rhs)


# ------------------------------------------------------------------ (V1)
def check_validity(G, fam):
    """Group identities (Garside normal form) implying LHS(p) = RHS(p) for all p >= 0.
    Write LHS = A0 x1^p1 A1 ... xr^pr Ar, RHS = B0 y^.. B1 ... (same parameters, any order).
    Moving each power to the far right by conjugation gives
        LHS = (A0...Ar) g_1^p1 ... g_r^pr,  g_k = C_k^-1 x_k C_k,  C_k = A_k ... A_r,
    and similarly RHS = (B0...Br) prod_{RHS order} h_p^{p}.  Sufficient (and, given the
    identities for all p, necessary): A0...Ar = B0...Br, g_p = h_p for every parameter p,
    and g_p g_q = g_q g_p whenever p, q occur in different relative order."""
    name, lhs, rhs = fam[:3]
    A, X, pl = split(lhs)
    B, Y, pr = split(rhs)
    if sorted(pl) != sorted(pr) or len(set(pl)) != len(pl):
        return False, 0
    is_id = lambda w: G.nf(w) == ""  # noqa: E731
    g, h = {}, {}
    for F, Lp, P, out in ((A, X, pl, g), (B, Y, pr, h)):
        for k in range(1, len(Lp) + 1):
            C = "".join(F[k:])
            out[P[k - 1]] = inv_word(C) + Lp[k - 1] + C
    conds = ["".join(A) + inv_word("".join(B))]
    conds += [g[p] + inv_word(h[p]) for p in pl]
    pos = {p: i for i, p in enumerate(pr)}
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            if pos[pl[i]] > pos[pl[j]]:
                gi, gj = g[pl[i]], g[pl[j]]
                conds.append(gi + gj + inv_word(gi) + inv_word(gj))
    ok = all(is_id(c) for c in conds)
    return ok, len(conds)


# ------------------------------------------------------------------ (V2)
def braid_relations(M):
    rels = []
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            from specs import alt
            u, v = alt(chr(97 + i), chr(97 + j), M[i][j]), alt(chr(97 + j), chr(97 + i), M[i][j])
            rels += [(u, v), (v, u)]
    return rels


def positive_equal(u: str, v: str, rels, limit=2_000_000) -> bool:
    """Decide u = v in the Artin monoid by exploring the (finite) class of u
    under the braid relations; pure word combinatorics (no Garside theory)."""
    if len(u) != len(v):
        return False
    if u == v:
        return True
    seen = {u}
    todo = [u]
    while todo:
        w = todo.pop()
        for a, b in rels:
            k = w.find(a)
            while k != -1:
                x = w[:k] + b + w[k + len(a):]
                if x == v:
                    return True
                if x not in seen:
                    seen.add(x)
                    todo.append(x)
                    if len(seen) > limit:
                        raise RuntimeError("class too large")
                k = w.find(a, k + 1)
    return False


def check_transport(fam, rels, delta_word, phi):
    """Independent validity proof by right transport (positive identities only)."""
    name, lhs, rhs = fam[:3]
    sub = lambda w: w.replace("1", delta_word)  # noqa: E731
    if name in ("I1", "I2"):
        return True, ["trivial"]
    if name.startswith("T"):
        x = name[1]
        y = chr(97 + phi[ord(x) - 97])
        if name.endswith("+"):  # x Delta = Delta phi(x)
            ok = positive_equal(x + delta_word, delta_word + y, rels)
            return ok, [f"{x}.Delta = Delta.{y}"]
        ok = positive_equal(delta_word + x, y + delta_word, rels)  # x Delta^-1 = Delta^-1 phi(x)
        return ok, [f"Delta.{x} = {y}.Delta"]
    A, X, pl = split(lhs)
    B, Y, pr = split(rhs)
    if sorted(pl) != sorted(pr) or len(set(pl)) != len(pl):
        return False, ["parameters must occur once on each side"]
    gens = sorted({c for c in delta_word})
    proofs, ok = [], True
    # move every loop to the far right on both sides:  x rho = rho w,  y sigma = sigma w
    wl, wr = {}, {}
    for side, F, Lp, P, out in (("L", A, X, pl, wl), ("R", B, Y, pr, wr)):
        for k in range(1, len(Lp) + 1):
            rho = sub("".join(F[k:]))
            if len(Lp[k - 1]) != 1:
                return False, ["loop words must be letters"]
            w = next((c for c in gens if positive_equal(Lp[k - 1] + rho, rho + c, rels)), None)
            out[P[k - 1]] = w
            proofs.append(f"{side}: {Lp[k-1]}.{rho or '1'} = {rho or '1'}.{w}")
    if any(v is None for v in list(wl.values()) + list(wr.values())):
        return None, proofs + ["not applicable: some loop letter does not transport to a letter"]
    ok &= all(wl[p] == wr[p] for p in pl)
    # the blocks w^p are now in LHS order on one side and RHS order on the other:
    # every pair whose relative order differs must commute
    pos = {p: i for i, p in enumerate(pr)}
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            if pos[pl[i]] > pos[pl[j]]:
                c = positive_equal(wl[pl[i]] + wl[pl[j]], wl[pl[j]] + wl[pl[i]], rels)
                proofs.append(f"commute {wl[pl[i]]}{wl[pl[j]]}: {c}")
                ok &= c
    base = positive_equal(sub("".join(A)), sub("".join(B)), rels)
    proofs.append(f"base {''.join(A)} = {''.join(B)}: {base}")
    return ok and base, proofs


# ------------------------------------------------------------------ (O)
def check_order(fam):
    name, lhs, rhs = fam[:3]
    A, X, pl = split(lhs)
    B, Y, pr = split(rhs)
    # length as affine function: const + sum coef*p (coefficients matched by parameter name)
    cL = sum(len(a) for a in A)
    cR = sum(len(b) for b in B)
    coefL = {p: len(x) for p, x in zip(pl, X)}
    coefR = {p: len(y) for p, y in zip(pr, Y)}
    if any(coefL.get(p, 0) < coefR.get(p, 0) for p in set(coefL) | set(coefR)) or cL < cR:
        return False
    strictly_shorter = cL > cR
    if strictly_shorter:
        return True
    # equal length possible: need first letter of RHS < first letter of LHS
    if not A[0] or not B[0]:
        return False
    return B[0][0] < A[0][0]


# ------------------------------------------------------------------ NFA of a family language
class NFA:
    """NFA with epsilon moves into fresh loop states, so that consecutive powers
    x^p y^q are recognised exactly (not as (x|y)*)."""

    def __init__(self):
        self.trans = [dict()]  # state -> letter -> set(states)
        self.eps = [set()]
        self.final = set()

    def new(self):
        self.trans.append(dict())
        self.eps.append(set())
        return len(self.trans) - 1

    def add(self, s, c, t):
        self.trans[s].setdefault(c, set()).add(t)

    def add_family(self, parts, start=0):
        assert parts[0][1] is None and parts[0][0], "family must start with a fixed word"
        s = start
        for w, p in parts:
            if p is None:
                for c in w:
                    t = self.new()
                    self.add(s, c, t)
                    s = t
            else:
                loop = self.new()
                self.eps[s].add(loop)
                cur = loop
                for j, c in enumerate(w):
                    t = loop if j == len(w) - 1 else self.new()
                    self.add(cur, c, t)
                    cur = t
                s = loop
        self.final.add(s)

    def closure(self, S):
        out, todo = set(S), list(S)
        while todo:
            for t in self.eps[todo.pop()]:
                if t not in out:
                    out.add(t)
                    todo.append(t)
        return out

    def step(self, S, c):
        out = set()
        for s in S:
            out |= self.trans[s].get(c, set())
        return frozenset(self.closure(out))


def leading_nfa(families):
    N = NFA()
    for _name, lhs, _rhs in families:
        N.add_family(lhs)
    return N


# ------------------------------------------------------------------ (G)
def irreducible_dfa_counts(N: NFA, alphabet, Lmax):
    """Count words with no factor in L(N); returns counts and #DFA states."""
    start = frozenset([0])
    states = {start: 0}
    trans = {}
    todo = [start]
    while todo:
        S = todo.pop()
        for c in alphabet:
            T = N.step(S, c) | {0}
            if T & N.final:
                trans[(S, c)] = None
                continue
            T = frozenset(T)
            trans[(S, c)] = T
            if T not in states:
                states[T] = len(states)
                todo.append(T)
    K = len(states)
    L = max(Lmax, 0)
    cur = {start: 1}
    counts = [1]
    for _ in range(L):
        nxt = {}
        for S, k in cur.items():
            for c in alphabet:
                T = trans[(S, c)]
                if T is not None:
                    nxt[T] = nxt.get(T, 0) + k
        cur = nxt
        counts.append(sum(cur.values()))
    return counts, K, trans, states


# ------------------------------------------------------------------ (L)
def language_equal(N: NFA, A: NFAutomaton, gens):
    init = ("init",)
    start = (frozenset([0]), init)
    seen = {start}
    todo = [start]
    while todo:
        S, P = todo.pop()
        fam_acc = bool(S & N.final)
        aut_acc = P == ("acc",)
        if fam_acc != aut_acc:
            return False, (S, P)
        for y, c in enumerate(gens):
            S2 = N.step(S, c)
            if P == init:
                P2 = (A.step(frozenset(), y), frozenset())
            elif P in (("acc",), ("dead",)):
                P2 = ("dead",)
            else:
                Of, Os = P
                Os2 = A.step(Os, y)
                if Os2 is None:
                    P2 = ("dead",)
                else:
                    Of2 = A.step(Of, y)
                    P2 = ("acc",) if Of2 is None else (Of2, Os2)
            if not S2 and P2 == ("dead",):
                continue
            st = (S2, P2)
            if st not in seen:
                seen.add(st)
                todo.append(st)
    return True, len(seen)


# ------------------------------------------------------------------ (R)
def rhs_irreducible(families, Nlead: NFA, alphabet):
    R = NFA()
    for _name, _lhs, rhs in families:
        if not rhs or not rhs[0][0]:
            continue
        R.add_family(rhs)
    start = (frozenset([0]), frozenset([0]))
    seen = {start}
    todo = [start]
    while todo:
        S, T = todo.pop()
        for c in alphabet:
            S2 = R.step(S, c)
            if not S2:
                continue
            T2 = Nlead.step(T, c) | {0}
            if T2 & Nlead.final:
                return False
            st = (S2, frozenset(T2))
            if st not in seen:
                seen.add(st)
                todo.append(st)
    return True


# ------------------------------------------------------------------ (E)
def instances_upto(families, Lmax):
    out = {}
    for name, lhs, rhs in families:
        _, X, names = split(lhs)
        base = len(instantiate(lhs, {p: 0 for p in names}))

        def rec(i, vals):
            if i == len(names):
                u = instantiate(lhs, vals)
                if len(u) <= Lmax:
                    assert u not in out, f"duplicate leading word {u}"
                    out[u] = instantiate(rhs, vals)
                return
            for v in range(0, Lmax + 1):
                vals2 = dict(vals, **{names[i]: v})
                if base + sum(len(X[j]) * vals2[names[j]] for j in range(i + 1)) > Lmax:
                    break
                rec(i + 1, vals2)

        rec(0, {})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--Lmax", type=int, default=13)
    a = ap.parse_args()
    spec = SPECS[a.spec]()
    typ, n, m = spec["type"]
    G = build(typ, n, m, spec["order"])
    W = G.W
    assert W.phi == spec["phi"], (W.phi, spec["phi"])
    fams_h = spec["families"]
    fams = [expand(f) for f in fams_h]
    gens = [chr(97 + i) for i in range(W.n)]
    alphabet = ["0", "1"] + gens
    report = {"spec": a.spec, "type": spec["type"], "order": spec["order"],
              "delta_word": G.delta_word(), "N": W.N, "families": len(fams)}
    # (V1) group identities via Garside normal form; (V2) positive transport identities via
    # braid-relation class exploration (independent of Garside theory); (O) order
    report["validity"] = {f[0]: check_validity(G, f[:3]) for f in fams_h}
    rels = braid_relations(W.M)
    tr = {f[0]: check_transport(f[:3], rels, G.delta_word(), W.phi) for f in fams_h}
    report["validity_transport"] = {k: v[0] for k, v in tr.items()}
    report["transport_proofs"] = {k: v[1] for k, v in tr.items()}
    report["order_ok"] = {f[0]: check_order(f) for f in fams}
    # (G)
    Nlead = leading_nfa(fams)
    counts0, K, _, _ = irreducible_dfa_counts(Nlead, alphabet, 0)
    Lg = K + W.N + 2
    counts, K, _, _ = irreducible_dfa_counts(Nlead, alphabet, Lg)
    growth = growth_counts(W, Lg, "group")
    report["growth_certificate"] = {"dfa_states": K, "checked_up_to": Lg,
                                    "equal": counts == growth,
                                    "first_counts": counts[:12]}
    # (L)
    pos = [f for f in fams if all(c not in "01" for c in f[1][0][0])]
    Npos = leading_nfa(pos)
    T = build_table(typ, n, m, spec["order"])
    A = NFAutomaton(T)
    eq, info = language_equal(Npos, A, gens)
    report["language_equal_minred_automaton"] = {"equal": eq, "product_states": info if eq else str(info)}
    # (R)
    report["rhs_irreducible"] = rhs_irreducible(fams, Nlead, alphabet)
    # (E)
    rules, _ = enumerate_basis(G, a.Lmax)
    oracle = dict(rules)
    inst = instances_upto(fams, a.Lmax)
    report["oracle_crosscheck"] = {"Lmax": a.Lmax, "oracle_rules": len(oracle),
                                   "family_instances": len(inst), "equal": oracle == inst}
    if oracle != inst:
        report["oracle_crosscheck"]["missing"] = sorted(set(oracle) - set(inst), key=lambda u: (len(u), u))[:20]
        report["oracle_crosscheck"]["extra"] = sorted(set(inst) - set(oracle), key=lambda u: (len(u), u))[:20]
        report["oracle_crosscheck"]["rhs_diff"] = [(u, oracle[u], inst[u]) for u in oracle
                                                   if u in inst and oracle[u] != inst[u]][:20]
    allok = (all(v[0] is True for v in report["validity"].values()) and all(report["order_ok"].values())
             and all(v is not False for v in report["validity_transport"].values())
             and report["growth_certificate"]["equal"] and eq and report["rhs_irreducible"]
             and report["oracle_crosscheck"]["equal"])
    report["ALL_OK"] = allok
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
