#!/usr/bin/env python3
"""pandya_control.py: exact positive control for lane ame46-support.

Rebuilds Pandya arXiv:2610.16673v1 Table I (pinned layout LF74-84) as W = sqrt(72)*psi, whose entries lie in
{0, +-1, sqrt2}, using exact arithmetic in Z[sqrt2] (pairs (p, q) = p + q*sqrt2). Checks, definition-first:
  - all six two-party marginals: 72*rho_ij = 2*I_36 (equivalently rho_ij = I/36), computed from the tensor itself;
  - support s = 60, classical officers t = 12 (|psi| = 1/6), all other moduli 1/sqrt72;
  - the classical officers equal Pandya's quartets P1 u P2 u P3 (LF269-272) and form a code with minimum distance 3;
  - every reshaping has twelve 1x1 and twelve 2x2 connected components;
  - the relaxed combinatorial model constraints C1-C4 of README 0.2 hold, and e = s - (72 - t) = 0.
Mutation controls must all be rejected by the marginal check. Writes evidence/pandya_control.json.
"""
import itertools
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = (0, 1)   # sqrt2


def zmul(a, b):
    return (a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


# Table I: officer (a, b) -> list of (coefficient in Z[sqrt2], ket (c, d)).  "S" marks a classical sqrt2|cd>.
TABLE = {
    (0, 0): [(-1, "12"), (1, "21")], (0, 1): [(-1, "02"), (1, "20")], (0, 2): [(-1, "01"), (1, "10")],
    (0, 3): [("S", "44")], (0, 4): [("S", "55")], (0, 5): [("S", "33")],
    (1, 0): [(-1, "01"), (-1, "10")], (1, 1): [(1, "00"), (1, "54")], (1, 2): [(1, "35"), (1, "43")],
    (1, 3): [(-1, "15"), (-1, "32")], (1, 4): [(-1, "23"), (1, "41")], (1, 5): [(-1, "24"), (1, "52")],
    (2, 0): [(1, "02"), (1, "20")], (2, 1): [(-1, "35"), (1, "43")], (2, 2): [(1, "00"), (-1, "54")],
    (2, 3): [(-1, "25"), (1, "31")], (2, 4): [(-1, "13"), (1, "42")], (2, 5): [(1, "14"), (1, "51")],
    (3, 0): [("S", "34")], (3, 1): [(-1, "23"), (-1, "41")], (3, 2): [(1, "13"), (1, "42")],
    (3, 3): [("S", "50")], (3, 4): [(-1, "11"), (1, "22")], (3, 5): [("S", "05")],
    (4, 0): [("S", "53")], (4, 1): [(1, "15"), (-1, "32")], (4, 2): [(1, "25"), (1, "31")],
    (4, 3): [(1, "11"), (1, "22")], (4, 4): [("S", "04")], (4, 5): [("S", "40")],
    (5, 0): [("S", "45")], (5, 1): [(-1, "14"), (1, "51")], (5, 2): [(1, "24"), (1, "52")],
    (5, 3): [("S", "03")], (5, 4): [("S", "30")], (5, 5): [(1, "12"), (1, "21")],
}
P_QUARTETS = ["0344", "3505", "4053", "5430", "0455", "3034", "4540", "5303", "0533", "3350", "4404", "5045"]
PAIRS = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]          # coordinate pairs (0-based)
RESHAPINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def build():
    W = {}
    for (a, b), terms in TABLE.items():
        for coef, ket in terms:
            x = (a, b, int(ket[0]), int(ket[1]))
            assert x not in W
            W[x] = R2 if coef == "S" else (coef, 0)
    return W


def marginal(W, keep):
    """72*rho on the coordinates `keep` (a pair), traced over the complement, as a dict of Z[sqrt2] entries."""
    rest = [i for i in range(4) if i not in keep]
    rho = {}
    for z1 in itertools.product(range(6), repeat=2):
        for z2 in itertools.product(range(6), repeat=2):
            acc = (0, 0)
            for y in itertools.product(range(6), repeat=2):
                x1 = [0] * 4
                x2 = [0] * 4
                for k, i in enumerate(keep):
                    x1[i] = z1[k]
                    x2[i] = z2[k]
                for k, i in enumerate(rest):
                    x1[i] = y[k]
                    x2[i] = y[k]
                u, v = W.get(tuple(x1)), W.get(tuple(x2))
                if u is not None and v is not None:
                    acc = zadd(acc, zmul(u, v))     # real entries: conj is identity
            if acc != (0, 0):
                rho[(z1, z2)] = acc
    return rho


def is_two_identity(rho):
    return rho == {(z, z): (2, 0) for z in itertools.product(range(6), repeat=2)}


def all_marginals_ok(W):
    return all(is_two_identity(marginal(W, keep)) for keep in PAIRS)


def components(S, rows, cols):
    """Connected components of the bipartite support graph of a reshaping; returns sorted list of (k_rows, k_cols)."""
    adj = {}
    for x in S:
        r = ("r", tuple(x[i] for i in rows))
        c = ("c", tuple(x[i] for i in cols))
        adj.setdefault(r, set()).add(c)
        adj.setdefault(c, set()).add(r)
    seen, sizes = set(), []
    for v in adj:
        if v in seen:
            continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        sizes.append((sum(1 for u in comp if u[0] == "r"), sum(1 for u in comp if u[0] == "c")))
    return sorted(sizes)


def rcm_check(S, T):
    """README 0.2 constraints C1-C4 on a pattern (S, T)."""
    S, T = set(S), set(T)
    lines = {}
    for P in PAIRS:
        for x in S:
            lines.setdefault((P, tuple(x[i] for i in P)), set()).add(x)
    c1 = all((P, z) in lines for P in PAIRS for z in itertools.product(range(6), repeat=2))
    c2 = all(sum(1 for i in range(4) if x[i] == y[i]) <= 1 for x in T for y in S if y != x)
    c3 = all(next(iter(L)) in T for L in lines.values() if len(L) == 1)
    c4 = True
    for rows, cols in RESHAPINGS:
        for a_idx, b_idx in ((rows, cols), (cols, rows)):
            sets = {}
            for x in S:
                sets.setdefault(tuple(x[i] for i in a_idx), set()).add(tuple(x[i] for i in b_idx))
            for (r1, s1), (r2, s2) in itertools.combinations(sets.items(), 2):
                if len(s1 & s2) == 1:
                    c4 = False
    return {"C1": c1, "C2": c2, "C3": c3, "C4": c4}


def main():
    W = build()
    S = sorted(W)
    T = sorted(x for x, v in W.items() if v == R2)
    others_unit = all(v in ((1, 0), (-1, 0)) for x, v in W.items() if v != R2)
    t, s = len(T), len(S)
    marg = {f"rho_{i + 1}{j + 1}": is_two_identity(marginal(W, (i, j))) for i, j in PAIRS}
    code_ok = all(sum(1 for i in range(4) if x[i] == y[i]) <= 1 for x, y in itertools.combinations(T, 2))
    T_str = sorted("".join(map(str, x)) for x in T)
    comps = {f"{r[0] + 1}{r[1] + 1}|{c[0] + 1}{c[1] + 1}": components(S, r, c) for r, c in RESHAPINGS}
    comp_ok = all(v == sorted([(1, 1)] * 12 + [(2, 2)] * 12) for v in comps.values())
    rcm = rcm_check(S, T)
    # mutation controls: each must break some marginal
    muts = {}
    x0 = (0, 0, 1, 2)                       # entangled coefficient -1
    m1 = dict(W)
    m1[x0] = (1, 0)
    muts["flip sign of 0012"] = m1
    m2 = dict(W)
    del m2[x0]
    muts["delete 0012"] = m2
    m3 = dict(W)
    m3[(0, 3, 4, 4)] = (1, 0)
    muts["classical 0344 set to modulus 1/sqrt72"] = m3
    m4 = dict(W)
    m4[(1, 1, 0, 1)] = m4.pop((1, 1, 0, 0))
    muts["move 1100 to 1101"] = m4
    m5 = dict(W)
    del m5[(0, 3, 4, 4)]
    muts["delete classical 0344"] = m5
    mut_res = {k: all_marginals_ok(v) for k, v in muts.items()}
    out = {
        "note": "exact positive control: Pandya arXiv:2610.16673v1 Table I, W = sqrt72*psi over Z[sqrt2]",
        "support_s": s, "classical_t": t, "e": s - (72 - t),
        "non_classical_moduli_all_1_over_sqrt72": others_unit,
        "classical_set_equals_P1uP2uP3": T_str == sorted(P_QUARTETS),
        "classical_code_min_distance_3": code_ok,
        "marginals_72rho_eq_2I": marg,
        "components_per_reshaping": {k: [list(c) for c in v] for k, v in comps.items()},
        "components_twelve_1x1_twelve_2x2": comp_ok,
        "RCM_C1_C4": rcm,
        "mutations_accepted_by_marginal_check (all must be False)": mut_res,
    }
    out["all_required_true"] = bool(s == 60 and t == 12 and out["e"] == 0 and others_unit
                                    and out["classical_set_equals_P1uP2uP3"] and code_ok and all(marg.values())
                                    and comp_ok and all(rcm.values()) and not any(mut_res.values()))
    with open(os.path.join(HERE, "..", "evidence", "pandya_control.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
