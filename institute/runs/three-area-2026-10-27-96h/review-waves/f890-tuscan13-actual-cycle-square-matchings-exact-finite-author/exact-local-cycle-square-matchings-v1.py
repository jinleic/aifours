#!/usr/bin/env python3
"""f890 exact LOCAL verifier, prepared UNRUN by VerifyF890TuscanExact (new source, no old code).

Scope (bounded, exact, stdlib only):
  * actual connected Hamilton 12-cycles on four labeled 3-cells A,B (opposite) and C,D (opposite);
  * zero-full grammar: every cyclic 8-run word with one double and one singleton per cell,
    one join per opposite pair between doubles, singleton transport; x 1296 labelings;
  * true directed squares x->z of consecutive x->y->z; explicit P/C/L/R and omitted pairs;
  * 3x3 lemmas: all 6 permutation matchings with their off-diagonal pair partitions (involution),
    third matching of two disjoint matchings, forward-degree multisets (8) and (11), count (5);
  * per-cell chord tables from actual labeled split cycles, four-row necessary table;
  * actual g=3 coupled shared-gap chord conclusion on actual U/W cycles.
NOT checked / NOT claimed: five-cycle residual decompositions, T13/T14 global branches, any
T2(11) array, M=C, existence or exhaustion of any global configuration. Old relaxed or
selected-interface fixtures are not used; every cycle passes guard_actual_cycle.
Execution: parent one-shot GO only; outer timeout <= 55 s; internal deadline 40 s.
No child process, network, file write or third-party import. Status lines are flushed JSON.
Exit 0 = all checks and intended-reason mutants pass; 1 = check failure; 2 = internal deadline.
"""
import hashlib
import itertools
import json
import sys
import time

T0 = time.monotonic()
INTERNAL_DEADLINE_S = 40.0
CELLS = ("A", "B", "C", "D")
OPP = {"A": "B", "B": "A", "C": "D", "D": "C"}
PAIRS = (("A", "B"), ("C", "D"))  # F joins A->B and C->D
VERTS = tuple((c, k) for c in CELLS for k in range(3))
ALPHA, BETA, GAMMA, DELTA = (1, 0), (2, 1), (0, 2), (2, 0)
NONF = (ALPHA, BETA, GAMMA, DELTA)
ARCNAME = {ALPHA: "alpha", BETA: "beta", GAMMA: "gamma", DELTA: "delta"}
F_ARCS = ((0, 1), (1, 2))
FILTER_REASONS = ("grammar_cell_layout", "regular_join_count", "regular_join_endpoint", "transport")
EXPECTED_CHORD = {
    ("source", ALPHA, "+"): 0, ("source", ALPHA, "-"): 2,
    ("source", BETA, "+"): 1, ("source", BETA, "-"): 0,
    ("source", GAMMA, "+"): 2, ("source", GAMMA, "-"): 1,
    ("source", DELTA, "+"): 0, ("source", DELTA, "-"): 1,
    ("target", ALPHA, "+"): 1, ("target", ALPHA, "-"): 2,
    ("target", BETA, "+"): 2, ("target", BETA, "-"): 0,
    ("target", GAMMA, "+"): 0, ("target", GAMMA, "-"): 1,
    ("target", DELTA, "+"): 2, ("target", DELTA, "-"): 1,
}
EXPECTED_FOUR = {
    ("source", 1): {("alpha", "gamma"), ("beta", "delta")},
    ("target", 1): {("alpha", "delta"), ("beta", "gamma")},
    ("source", 2): {("beta", "delta"), ("gamma", "alpha")},
    ("target", 2): {("alpha", "delta"), ("gamma", "beta")},
}


class Fail(Exception):
    def __init__(self, reason, detail=""):
        Exception.__init__(self, reason)
        self.reason = reason
        self.detail = str(detail)


def need(cond, reason, detail=""):
    if not cond:
        raise Fail(reason, detail)


def emit(stage, **kw):
    rec = {"stage": stage, "elapsed_s": round(time.monotonic() - T0, 6)}
    rec.update(kw)
    sys.stdout.write(json.dumps(rec, sort_keys=True, default=str) + "\n")
    sys.stdout.flush()


def tick():
    if time.monotonic() - T0 > INTERNAL_DEADLINE_S:
        raise Fail("internal_deadline")


def cellv(c):
    return [(c, 0), (c, 1), (c, 2)]


def guard_actual_cycle(cyc):
    need(isinstance(cyc, tuple) and len(cyc) == 12, "guard_not_12")
    need(set(cyc) == set(VERTS), "guard_not_hamilton")
    return cyc


def runs_of(cyc):
    n = len(cyc)
    starts = [i for i in range(n) if cyc[i][0] != cyc[i - 1][0]]
    need(starts, "guard_single_cell")
    rot = cyc[starts[0]:] + cyc[:starts[0]]
    out, cur = [], [rot[0]]
    for v in rot[1:]:
        if v[0] == cur[-1][0]:
            cur.append(v)
        else:
            out.append(tuple(cur))
            cur = [v]
    out.append(tuple(cur))
    return out


def squares(cyc, p, q):
    n = len(cyc)
    return frozenset((cyc[i], cyc[(i + 2) % n]) for i in range(n)
                     if cyc[i][0] == p and cyc[(i + 2) % n][0] == q)


def omitted(match, tails, heads):
    ts = {t for t, _ in match}
    hs = {h for _, h in match}
    need(len(match) == 2 and len(ts) == 2 and len(hs) == 2, "pair_not_matching", sorted(match))
    (u,) = tuple(set(tails) - ts)
    (v,) = tuple(set(heads) - hs)
    return (u, v)


def classify_zero_full(cyc):
    guard_actual_cycle(cyc)
    runs = runs_of(cyc)
    m = len(runs)
    lens = {}
    for r in runs:
        lens.setdefault(r[0][0], []).append(len(r))
    need(m == 8 and all(sorted(lens.get(c, [])) == [1, 2] for c in CELLS), "grammar_cell_layout")
    blocks = {}
    for (p, q) in PAIRS:
        here = [i for i in range(m) if {runs[i][0][0], runs[(i + 1) % m][0][0]} == {p, q}]
        need(len(here) == 1, "regular_join_count", (p, q, len(here)))
        i = here[0]
        need(len(runs[i]) == 2 and len(runs[(i + 1) % m]) == 2, "regular_join_endpoint", (p, q))
        blocks[(p, q)] = i
    for i in range(m):
        if len(runs[i]) == 1:
            c = runs[i][0][0]
            other = {"C", "D"} if c in ("A", "B") else {"A", "B"}
            need({runs[i - 1][-1][0], runs[(i + 1) % m][0][0]} == other, "transport", c)
    iX, iY = blocks[PAIRS[0]], blocks[PAIRS[1]]

    def gap_after(i):
        g, j = [], (i + 2) % m
        while len(runs[j]) == 1:
            g.append(runs[j][0][0])
            j = (j + 1) % m
        return g, j

    GX, jX = gap_after(iX)
    HX, jY = gap_after(iY)
    need(jX == iY and jY == iX, "grammar_extra", "blocks and gaps do not tile")
    x0, x1 = runs[iX][0][0], runs[(iX + 1) % m][0][0]
    y0, y1 = runs[iY][0][0], runs[(iY + 1) % m][0][0]
    if GX == [y0, x0, y1, x1] and HX == []:
        kind, gx = "grouped", "G"
    elif GX == [] and HX == [x0, y0, x1, y1]:
        kind, gx = "grouped", "H"
    elif GX == [y1, x0] and HX == [x1, y0]:
        kind, gx = "split", None
    else:
        raise Fail("grammar_extra", (GX, HX))
    swap = {"G": "H", "H": "G", None: None}
    role, arc = {}, {}
    for r in runs:
        c = r[0][0]
        if len(r) == 2:
            role[c] = (r[0], r[1]) + role.get(c, (None, None, None))[2:]
            arc[c] = (r[0][1], r[1][1])
    for r in runs:
        if len(r) == 1:
            c = r[0][0]
            role[c] = role[c][:2] + (r[0],)
    sign = {pq: ("+" if runs[blocks[pq]][0][0] == pq[0] else "-") for pq in PAIRS}
    gap = {PAIRS[0]: gx, PAIRS[1]: swap[gx]}
    after = None if kind == "split" else ("AB" if gx == "G" else "CD")
    return {"kind": kind, "sign": sign, "gap": gap, "after": after, "role": role, "arc": arc}


def expected_sets(info, p, q, swap_gap=False):
    pm, pp, p0 = info["role"][p]
    qm, qp, q0 = info["role"][q]
    s = info["sign"][(p, q)]
    if info["kind"] == "grouped":
        g = info["gap"][(p, q)]
        if swap_gap:
            g = "H" if g == "G" else "G"
        if s == "+":
            return ("P", {(pm, qm), (pp, qp), (p0, q0)}, "C", {(qp, p0)} if g == "G" else {(q0, pm)})
        return ("C", {(pp, q0)} if g == "G" else {(p0, qm)}, "P", {(qm, pm), (qp, pp), (q0, p0)})
    if s == "+":
        return ("L", {(pm, qm), (pp, qp)}, "R", {(qp, p0), (q0, pm)})
    return ("L", {(pp, q0), (p0, qm)}, "R", {(qm, pm), (qp, pp)})


def check_row(cyc, info, swap_gap=False):
    for (p, q) in PAIRS:
        n1, e1, n2, e2 = expected_sets(info, p, q, swap_gap)
        need(squares(cyc, p, q) == frozenset(e1), n1 + "_formula", (p, q))
        need(squares(cyc, q, p) == frozenset(e2), n2 + "_formula", (q, p))
        if info["kind"] == "split":
            pm, pp, p0 = info["role"][p]
            qm, qp, q0 = info["role"][q]
            oL = omitted(squares(cyc, p, q), cellv(p), cellv(q))
            oR = omitted(squares(cyc, q, p), cellv(q), cellv(p))
            exp = ((p0, q0), (qm, pp)) if info["sign"][(p, q)] == "+" else ((pm, qp), (q0, p0))
            need((oL, oR) == exp, "omit_table", (p, q))


def record_chord(chord, cyc, info):
    for (p, q) in PAIRS:
        u, v = omitted(squares(cyc, q, p), cellv(q), cellv(p))
        for rl, cell, vert in (("source", p, v), ("target", q, u)):
            key = (rl, info["arc"][cell], info["sign"][(p, q)])
            if key in chord:
                need(chord[key] == vert[1], "chord_single_valued", key)
            else:
                chord[key] = vert[1]


def compare_chord(chord, expected):
    for key, val in expected.items():
        need(key in chord, "chord_missing", key)
        need(chord[key] == val, "chord_table", key)


def four_row_table(chord):
    res = {}
    for rl in ("source", "target"):
        for eX in NONF:
            rest = [e for e in NONF if e != eX]
            for signs in itertools.product("+-", repeat=3):
                npos = signs.count("+")
                if npos not in (1, 2):
                    continue
                if len({chord[(rl, e, s)] for e, s in zip(rest, signs)}) != 3:
                    continue
                minority = "+" if npos == 1 else "-"
                (eu,) = [e for e, s in zip(rest, signs) if s == minority]
                res.setdefault((rl, npos), set()).add((ARCNAME[eX], ARCNAME[eu]))
    return res


def compare_four(res, expected):
    need(res == expected, "four_row_table", sorted((k, sorted(v)) for k, v in res.items()))


def word_cycle(word, lab):
    out = []
    for c, ln in word:
        m, p, z = lab[c]
        out.extend([(c, m), (c, p)] if ln == 2 else [(c, z)])
    return tuple(out)


def zero_full_words():
    toks = [(c, 2) for c in CELLS] + [(c, 1) for c in CELLS]
    first = ("A", 2)
    for perm in itertools.permutations([t for t in toks if t != first]):
        w = (first,) + perm
        if all(w[i][0] != w[i - 1][0] for i in range(8)):
            yield w


def labelings():
    perms = list(itertools.permutations(range(3)))
    for combo in itertools.product(perms, repeat=4):
        yield dict(zip(CELLS, combo))


F_ROW = tuple((c, k) for c in CELLS for k in range(3))


def check_F():
    guard_actual_cycle(F_ROW)
    need([len(r) for r in runs_of(F_ROW)] == [3, 3, 3, 3], "F_formula", "four full runs")
    for (p, q) in PAIRS:
        need(squares(F_ROW, p, q) == frozenset({((p, 1), (q, 0)), ((p, 2), (q, 1))}), "F_formula", (p, q))
        need(squares(F_ROW, q, p) == frozenset(), "F_formula", (q, p))


def V(s):
    return (s[0], int(s[1]))


def cyc_of(text):
    return tuple(V(t) for t in text.split())


PC_GROUPED = cyc_of("A2 A0 B1 B0 C2 A1 D1 B2 C1 C0 D0 D2")
PC_SPLIT = cyc_of("B0 B2 A1 A0 C1 B1 D2 D1 C2 C0 A2 D0")
PC_W3 = cyc_of("B2 B1 A0 A2 C1 B0 D2 D0 C2 C0 A1 D1")
PC_TRANSPORT_BAD = cyc_of("A0 A1 B0 B1 C2 A2 C0 C1 D0 D1 B2 D2")


def sq(*pairs):
    return frozenset((V(a), V(b)) for a, b in (x.split(">") for x in pairs))


def positive_controls():
    check_F()
    g = classify_zero_full(PC_GROUPED)
    need((g["kind"], g["sign"][PAIRS[0]], g["sign"][PAIRS[1]], g["after"]) == ("grouped", "+", "+", "AB"),
         "positive_control", "grouped shape")
    need(squares(PC_GROUPED, "A", "B") == sq("A2>B1", "A0>B0", "A1>B2"), "positive_control", "P_AB")
    need(squares(PC_GROUPED, "B", "A") == sq("B0>A1"), "positive_control", "C_BA")
    need(squares(PC_GROUPED, "C", "D") == sq("C1>D0", "C0>D2", "C2>D1"), "positive_control", "P_CD")
    need(squares(PC_GROUPED, "D", "C") == sq("D1>C1"), "positive_control", "C_DC")
    check_row(PC_GROUPED, g)
    s = classify_zero_full(PC_SPLIT)
    need((s["kind"], s["sign"][PAIRS[0]], s["sign"][PAIRS[1]]) == ("split", "-", "-"), "positive_control", "split")
    need(squares(PC_SPLIT, "B", "A") == sq("B0>A1", "B2>A0"), "positive_control", "R_BA")
    need(squares(PC_SPLIT, "A", "B") == sq("A0>B1", "A2>B0"), "positive_control", "L_AB")
    need(squares(PC_SPLIT, "D", "C") == sq("D2>C2", "D1>C0"), "positive_control", "R_DC")
    need(squares(PC_SPLIT, "C", "D") == sq("C0>D0", "C1>D2"), "positive_control", "L_CD")
    check_row(PC_SPLIT, s)
    w = classify_zero_full(PC_W3)
    need((w["kind"], w["sign"][PAIRS[0]], w["sign"][PAIRS[1]]) == ("split", "-", "-"), "positive_control", "W3")
    check_row(PC_W3, w)
    n = g3_pair_conclusion(g, PC_GROUPED, w, PC_W3, require=True)
    need(n == 1, "positive_control", "g3 literal pair")
    return g, s, w


def arcs_distinct(ui, wi):
    return all(len({F_ARCS[0], F_ARCS[1], ui["arc"][c], wi["arc"][c]}) == 4 for c in CELLS)


def g3_key_U(U):
    cba, cdc = squares(U, "B", "A"), squares(U, "D", "C")
    need(len(cba) == 1 and len(cdc) == 1, "C_formula", "U reverse squares")
    return (next(iter(cba)), next(iter(cdc)))


def g3_key_W(W):
    return (omitted(squares(W, "B", "A"), cellv("B"), cellv("A")),
            omitted(squares(W, "D", "C"), cellv("D"), cellv("C")))


def g3_pair_conclusion(ui, U, wi, W, require=False, use_filter=True):
    if g3_key_U(U) != g3_key_W(W):
        need(not require, "g3_key", "literal pair key")
        return 0
    if use_filter and not arcs_distinct(ui, wi):
        need(not require, "arc_repeat", "literal pair arcs")
        return 0
    cells = ("A", "D") if ui["after"] == "AB" else ("B", "C")
    for c in cells:
        need({ui["arc"][c], wi["arc"][c]} == {GAMMA, DELTA}, "g3_conclusion", (c, ui["arc"][c], wi["arc"][c]))
        need(ui["role"][c][2] == wi["role"][c][2] if c in ("A", "D") and ui["after"] == "AB" else True,
             "g3_endpoint", c)
    return 1


def g3_all(Us, Ws, use_filter=True):
    index = {}
    for W, wi in Ws:
        index.setdefault(g3_key_W(W), []).append((W, wi))
    surv = {"AB": 0, "CD": 0}
    for U, ui in Us:
        tick()
        for W, wi in index.get(g3_key_U(U), ()):
            surv[ui["after"]] += g3_pair_conclusion(ui, U, wi, W, use_filter=use_filter)
    need(surv["AB"] > 0 and surv["CD"] > 0, "g3_vacuous", surv)
    return surv


ALL9 = frozenset((t, h) for t in range(3) for h in range(3))
PMS = [frozenset((t, p[t]) for t in range(3)) for p in itertools.permutations(range(3))]
TWO = [frozenset(x) for x in itertools.combinations(sorted(ALL9), 2)
       if x[0][0] != x[1][0] and x[0][1] != x[1][1]]
F9 = frozenset({(1, 0), (2, 1)})  # F_AB with a1->b0, a2->b1 as (tail, head) indices


def is_J(parts):
    cnt = {}
    for part in parts:
        for e in part:
            cnt[e] = cnt.get(e, 0) + 1
    return len(cnt) == 9 and all(v == 1 for v in cnt.values())


def pairings(items):
    if not items:
        yield []
        return
    for i in range(1, len(items)):
        for tail in pairings(items[1:i] + items[i + 1:]):
            yield [frozenset((items[0], items[i]))] + tail


def lemma_involution():
    shapes = []
    for pi_set in PMS:
        pi = dict(pi_set)
        piinv = {a: b for b, a in pi_set}
        adm = []
        for prs in pairings(sorted(ALL9 - pi_set)):
            try:
                adm.append([omitted(pr, range(3), range(3)) for pr in prs])
            except Fail:
                continue
        need(len(adm) == 4, "involution_partition_count", len(adm))
        kinds = []
        for oms in adm:
            need(len({u for u, _ in oms}) == 3 and len({v for _, v in oms}) == 3, "involution_distinct")
            tau = dict(oms)
            rel = {u: piinv[tau[u]] for u in range(3)}
            need(all(rel[rel[u]] == u for u in range(3)), "involution", oms)
            kinds.append(sum(rel[u] == u for u in range(3)))
            need(any(pi[u] == v for u, v in oms), "involution_edge", oms)
        need(sorted(kinds) == [1, 1, 1, 3], "involution_kinds", kinds)
        shapes.append(sorted(kinds))
    return shapes


def check_third_instance(R, S, W, c):
    need(is_J([R, S, W, frozenset([c])]), "J_mismatch")
    piR, piS = dict(R), dict(S)
    piRinv = {a: b for b, a in R}
    delta = {b: piRinv[piS[b]] for b in range(3)}
    need(all(delta[b] != b for b in range(3)), "third_delta_fixed")
    need(all(delta[delta[delta[b]]] == b for b in range(3)), "third_delta_cycle")
    need(frozenset((b, piR[delta[delta[b]]]) for b in range(3)) == ALL9 - R - S, "third_rho")
    u, v = omitted(W, range(3), range(3))
    need(c == (u, v) and v == piR[delta[delta[u]]], "third_C", (c, u, v))


def lemma_third():
    sols = 0
    for R in PMS:
        for S in PMS:
            if R & S:
                continue
            for W in TWO:
                for c in sorted(ALL9):
                    if is_J([R, S, W, frozenset([c])]):
                        check_third_instance(R, S, W, c)
                        sols += 1
    need(sols == 36, "third_count", sols)
    return sols


def lemma_forward8():
    sols = 0
    for c in sorted(ALL9):
        tick()
        for trip in itertools.combinations_with_replacement(TWO, 3):
            if is_J([F9, frozenset([c])] + list(trip)):
                oms = [omitted(L, range(3), range(3)) for L in trip]
                need(sorted(t for t, _ in oms) == sorted([1, 2, c[0]]), "forward8_tails", (c, oms))
                need(sorted(h for _, h in oms) == sorted([0, 1, c[1]]), "forward8_heads", (c, oms))
                sols += 1
    need(sols > 0, "forward8_vacuous")
    return sols


def lemma_forward11():
    sols = 0
    for PU in PMS:
        for LW in TWO:
            for cR, cS in itertools.combinations_with_replacement(sorted(ALL9), 2):
                if is_J([F9, PU, LW, frozenset([cR]), frozenset([cS])]):
                    t, h = omitted(LW, range(3), range(3))
                    need(sorted([cR[0], cS[0]]) == sorted([0, t]), "forward11_tails", (cR, cS, t))
                    need(sorted([cR[1], cS[1]]) == sorted([2, h]), "forward11_heads", (cR, cS, h))
                    sols += 1
    need(sols > 0, "forward11_vacuous")
    return sols


def lemma_count(shape):
    need(shape == {"grouped": {(3, 1)}, "split": {(2, 2)}}, "count_shape", shape)
    sols = []
    for kinds in itertools.product(("grouped", "split"), repeat=4):
        for signs in itertools.product("+-", repeat=4):
            ab = 2
            for k, s in zip(kinds, signs):
                same, rev = next(iter(shape[k]))
                ab += same if s == "+" else rev
            g = kinds.count("grouped")
            n = sum(1 for k, s in zip(kinds, signs) if k == "grouped" and s == "+")
            need((ab == 9) == (g == 2 * n + 1), "count_identity", (kinds, signs))
            if ab == 9:
                sols.append(g)
    need(sorted(set(sols)) == [1, 3], "count_g_values", sorted(set(sols)))
    return len(sols)


def expect_reason(name, fn, reason):
    try:
        fn()
    except Fail as e:
        need(e.reason == reason, "mutant_wrong_reason", (name, e.reason, reason))
        emit("mutant", name=name, caught=reason)
        return
    raise Fail("mutant_not_caught", name)


def main():
    src = open(__file__, "rb").read()
    emit("start", python=sys.version.split()[0], source_sha256=hashlib.sha256(src).hexdigest(),
         internal_deadline_s=INTERNAL_DEADLINE_S, outer_timeout_s_max=55)
    g, s, w = positive_controls()
    emit("positive_actual_cycle_controls", status="PASS", grouped=g["kind"], split=s["kind"])
    words, filtered, forms = 0, {}, {}
    accepted = []
    for word in zero_full_words():
        words += 1
        try:
            info = classify_zero_full(word_cycle(word, {"A": (0, 1, 2), "B": (0, 1, 2),
                                                        "C": (0, 1, 2), "D": (0, 1, 2)}))
        except Fail as e:
            need(e.reason in FILTER_REASONS, e.reason, e.detail)
            filtered[e.reason] = filtered.get(e.reason, 0) + 1
            continue
        key = info["kind"] + ":" + (info["after"] or "split")
        forms[key] = forms.get(key, 0) + 1
        accepted.append(word)
    need(forms == {"grouped:AB": 4, "grouped:CD": 4, "split:split": 4}, "grammar_forms", forms)
    emit("grammar_words", maximal_words=words, filtered=filtered, accepted_forms=forms)
    chord, shape, Us, Ws, cycles = {}, {"grouped": set(), "split": set()}, [], [], 0
    for word in accepted:
        for lab in labelings():
            cyc = word_cycle(word, lab)
            info = classify_zero_full(cyc)
            check_row(cyc, info)
            cycles += 1
            for (p, q) in PAIRS:
                fwd = (p, q) if info["sign"][(p, q)] == "+" else (q, p)
                shape[info["kind"]].add((len(squares(cyc, *fwd)), len(squares(cyc, fwd[1], fwd[0]))))
            if info["kind"] == "split":
                record_chord(chord, cyc, info)
                if info["sign"] == {PAIRS[0]: "-", PAIRS[1]: "-"}:
                    Ws.append((cyc, info))
            elif info["sign"] == {PAIRS[0]: "+", PAIRS[1]: "+"}:
                Us.append((cyc, info))
        tick()
    emit("actual_labeled_cycles", status="PASS", cycles=cycles, U_pp=len(Us), W_mm=len(Ws))
    emit("count_identity_5", status="PASS", solutions=lemma_count(shape))
    emit("involution_7", status="PASS", shapes=lemma_involution())
    emit("third_matching_10", status="PASS", solutions=lemma_third())
    emit("forward_degree_8", status="PASS", solutions=lemma_forward8())
    emit("forward_degree_11", status="PASS", solutions=lemma_forward11())
    compare_chord(chord, EXPECTED_CHORD)
    four = four_row_table(chord)
    compare_four(four, EXPECTED_FOUR)
    need(all(eX != "delta" for v in four.values() for eX, _ in v), "chord_claim1")
    emit("chord_tables_12", status="PASS", four_row={"%s,%d" % k: sorted(v) for k, v in sorted(four.items())})
    surv = g3_all(Us, Ws)
    emit("g3_shared_gap_13", status="PASS", surviving_pairs=surv)
    flipped = dict(EXPECTED_CHORD)
    flipped[("source", DELTA, "+")] = 2
    dropped = {k: set(v) for k, v in EXPECTED_FOUR.items()}
    dropped[("source", 1)].discard(("beta", "delta"))
    R0, S0 = PMS[0], next(S for S in PMS if not (S & PMS[0]))
    mutants = [
        ("relaxed_repeated_vertex", lambda: guard_actual_cycle(F_ROW[:11] + (F_ROW[0],)), "guard_not_hamilton"),
        ("relaxed_short_path", lambda: guard_actual_cycle(F_ROW[:11]), "guard_not_12"),
        ("transport_violation", lambda: classify_zero_full(PC_TRANSPORT_BAD), "transport"),
        ("swapped_gap_C", lambda: check_row(PC_GROUPED, g, swap_gap=True), "C_formula"),
        ("non_matching_pair", lambda: omitted(frozenset({(0, 0), (0, 1)}), range(3), range(3)),
         "pair_not_matching"),
        ("third_wrong_entry", lambda: check_third_instance(R0, S0, next(iter(TWO)), next(iter(R0))),
         "J_mismatch"),
        ("chord_entry_flip", lambda: compare_chord(chord, flipped), "chord_table"),
        ("four_row_drop", lambda: compare_four(four, dropped), "four_row_table"),
        ("g3_without_arc_uniqueness", lambda: g3_all(Us, Ws, use_filter=False), "g3_conclusion"),
    ]
    for name, fn, reason in mutants:
        expect_reason(name, fn, reason)
    emit("final", status="COMPLETE_LOCAL_ONLY", mutants=len(mutants),
         nonclaims="no five-cycle residual decomposition, T13/T14 branch, T2(11) array, M=C, "
                   "existence or exhaustion claim; relaxed selected-interface fixtures unused")
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Fail as exc:
        emit("final", status="FAIL", reason=exc.reason, detail=exc.detail)
        code = 2 if exc.reason == "internal_deadline" else 1
    except Exception as exc:  # unexpected error is a failure, never a pass
        emit("final", status="ERROR", error=repr(exc))
        code = 1
    sys.exit(code)
