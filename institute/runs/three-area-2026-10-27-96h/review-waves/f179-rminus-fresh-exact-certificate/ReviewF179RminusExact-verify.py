#!/usr/bin/env python3
"""ReviewF179RminusExact: own exact rational verifier for the raw R-minus certificate v12c.

Written by the reviewer from the stated semantic contract (bundle Section 2, publisher
Theorem 5.2 / Lemma 2.10 / Appendix B, DFZ packet lines) and the raw data only.  No
author/producer/checker code, result or receipt is read or executed.

Semantics implemented (all independently derived; see review-v1.md):
  * coordinates h_B(S): S a nonempty set of variable names of ONE branch B.  If S contains
    only originals a..j (= X1..X10) the coordinate is shared ('O', S) because every branch
    is an extension of the same (symmetrised) law of X1..X10; otherwise it is private
    (B, S).  h(empty) = 0.
  * >=0 rows (mono, cmi, dfz) need multiplier <= 0; cap rows (expression h(v), bound 1)
    need multiplier >= 0; equality rows (fd, sym, copy, independence, xcopy,
    xindependence, mcopy, mindependence) may carry either sign.
  * claim: sum_i w_i * expr_i == h('O', V) coefficientwise  =>  h(V) <= sum caps.
Exit codes: 0 VALID, 1 INVALID, 2 UNKNOWN, 3 input binding failure.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from fractions import Fraction

CERT = ("/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/"
        "f178-rminus-fresh-source-reconstruction/parent-input-certificate-v12c.json")
CERT_SHA = "6d5dc5c62833243db23870bcc34f3869149bd48e13843bee4ca977cd04eca886"
DFZP = ("/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/"
        "f178-rminus-fresh-source-reconstruction/parent-dfz-primary-extract-v1.txt")
DFZP_SHA = "2b59a111a1cb7f69de0385926305d5f7456ef67b6045a78d98bba3fcd0f072a6"
LAYOUT = ("/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/"
          "parallel-18/guessing-rminus/gurpinar-publisher-layout-v1.txt")
LAYOUT_SHA = "98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88"

ORIG = list("abcdefghij")          # a..j = X1..X10
V_ALL = frozenset(ORIG)

# Fig. 2 (printed p570), reviewer transcription; equal to the reviewer's vector extraction.
EDGES = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 7), (2, 9), (2, 10),
         (3, 4), (3, 8), (3, 9), (4, 5), (4, 8), (4, 10), (5, 6), (5, 9), (5, 10), (6, 7),
         (6, 8), (6, 9), (7, 8), (7, 10), (8, 9), (8, 10)]
# Appendix B (printed p575): sigma = (18)(2 10 5 9)(3746), tau = (25)(36)(47).
SIGMA_CYCLES = [(1, 8), (2, 10, 5, 9), (3, 7, 4, 6)]
TAU_CYCLES = [(2, 5), (3, 6), (4, 7)]
# Theorem 5.2 item 1 (printed p571), reviewer transcription: (new names, copied, over).
PUBLISHER = {
    "P1": [(["b'0"], [2], [1, 4, 5, 6, 7, 8, 9, 10])],
    "P2": [(["d'1", "e'1"], [4, 5], [1, 2, 3, 6, 7, 8, 9]),
           (["g'2"], [7], [1, 2, 3, 4, 6, 8, 9, "e'1"])],
    "P3": [(["f'3", "g'3"], [6, 7], [1, 2, 3, 4, 5, 8, 9, 10]),
           (["h'4"], [8], [1, 2, 3, 4, 5, 6, 9, 10, "f'3"])],
}
DECLARED_DFZ = [3, 7, 2, 2, 3, 0, 0, 3, 2]
TOP_KEYS = {"source_result_sha256", "branches", "extra_single_copies", "programs",
            "support_rows", "bound", "bound_float", "float_objective", "convention",
            "multipliers", "elapsed_s"}
GE0 = {"mono", "cmi", "dfz"}
EQ = {"fd", "sym", "copy", "independence", "xcopy", "xindependence", "mcopy", "mindependence"}
MULT_RE = re.compile(r"^-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?$")


class Fail(Exception):
    pass


class Report:
    def __init__(self):
        self.reasons = []      # (code, detail) -> INVALID
        self.unknown = []      # (code, detail) -> UNKNOWN
        self.warnings = []

    def bad(self, code, detail):
        if len(self.reasons) < 400:
            self.reasons.append([code, detail])
        else:
            self.reasons[-1] = [code, "(truncated further reasons)"]

    def codes(self):
        return sorted({c for c, _ in self.reasons})


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def is_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def perm_from_cycles(cycles):
    p = {v: v for v in range(1, 11)}
    for cyc in cycles:
        for k, v in enumerate(cyc):
            p[v] = cyc[(k + 1) % len(cyc)]
    return p


def strict_load(raw, rep):
    def hook(pairs):
        d = {}
        for k, v in pairs:
            if k in d:
                raise Fail("JSON_DUPLICATE_KEY:%s" % k)
            d[k] = v
        return d

    def const(c):
        raise Fail("JSON_NONFINITE:%s" % c)

    if raw.startswith(b"\xef\xbb\xbf"):
        raise Fail("JSON_BOM")
    text = raw.decode("utf-8", errors="strict")
    return json.loads(text, object_pairs_hook=hook, parse_constant=const)


# ----------------------------------------------------------------------------- source binding
def bind_sources(rep, info):
    lay = open(LAYOUT, "rb").read()
    info["layout_sha256"] = sha_bytes(lay)
    if info["layout_sha256"] != LAYOUT_SHA:
        raise Fail("INPUT_HASH_MISMATCH:layout")
    lines = lay.decode("utf-8").split("\n")
    tok = re.compile(r"X(\d+)(\u2032*)")
    prime_name = {(2, 1): "b'0", (4, 2): "d'1", (5, 2): "e'1", (7, 3): "g'2",
                  (6, 4): "f'3", (7, 4): "g'3", (8, 5): "h'4"}

    def toks(n):
        out = []
        for m in tok.finditer(lines[n - 1]):
            v, pr = int(m.group(1)), len(m.group(2))
            out.append(v if pr == 0 else prime_name[(v, pr)])
        return out

    # Every expectation below is DERIVED from the PUBLISHER transcription, then compared with
    # the printed token streams: header line = new copies, Y-part (= existing - over - copied,
    # as a set), copied tuple; over line = over-set (as a set); 1(a) prints no over-set, so
    # over = existing - Y - copied must hold for the printed Y.
    layout_lines = {("P1", 0): (940, None), ("P2", 0): (941, 942), ("P2", 1): (943, 944),
                    ("P3", 0): (945, 946), ("P3", 1): (947, 948)}
    elem_lines = {"P1": 951, "P2": 953, "P3": 955}
    checked = []
    for bid, steps in PUBLISHER.items():
        existing = set(range(1, 11))
        for s, (new, old, over) in enumerate(steps):
            hl, ol = layout_lines[(bid, s)]
            got = toks(hl)
            k, m = len(new), len(old)
            g_new, g_y, g_old = got[:k], got[k:len(got) - m], got[len(got) - m:]
            y_der = existing - set(over) - set(old)
            if g_new != list(new) or g_old != list(old) or set(g_y) != y_der:
                raise Fail("PUBLISHER_TRANSCRIPTION_MISMATCH:line%d:%r" % (hl, got))
            if ol is None:
                if set(over) != existing - set(g_y) - set(old):
                    raise Fail("PUBLISHER_TRANSCRIPTION_MISMATCH:implicit-over line%d" % hl)
            elif set(toks(ol)) != set(over) or len(toks(ol)) != len(over):
                raise Fail("PUBLISHER_TRANSCRIPTION_MISMATCH:line%d:%r" % (ol, toks(ol)))
            checked.append([bid, s, hl, ol])
            existing |= set(new)
        if set(toks(elem_lines[bid])) != existing or len(toks(elem_lines[bid])) != len(existing):
            raise Fail("PUBLISHER_TRANSCRIPTION_MISMATCH:elemental line%d" % elem_lines[bid])
    info["publisher_text_binding"] = {"steps_checked": checked, "elemental_lines": elem_lines,
                                      "result": "token streams of layout lines equal transcription"}

    pk = open(DFZP, "rb").read()
    info["dfz_packet_sha256"] = sha_bytes(pk)
    if info["dfz_packet_sha256"] != DFZP_SHA:
        raise Fail("INPUT_HASH_MISMATCH:dfz_packet")
    pl = {}
    for line in pk.decode("utf-8").split("\n"):
        m = re.match(r"^S1\|(\d+)\|(.*)$", line)
        if m:
            pl[int(m.group(1))] = m.group(2)
    form = pl[1960] + pl[1961] + pl[1962]
    lhs, rhs = form.split("&\\leq&")
    term = re.compile(r"([a-i])I\(([A-D]+);([A-D]+)(?:\|([A-D]+))?\)")
    L = term.findall(lhs)
    R = term.findall(rhs)
    if [t[0] for t in L] != ["a"] or [t[0] for t in R] != list("bcdefghi"):
        raise Fail("DFZ_FORM_PARSE")
    dfz_form = {"lhs": L[0], "rhs": R}
    items = {}
    for n in range(2084, 2093):
        m = re.match(r"^\\item ((?:\d+ ){9})(.*)$", pl[n])
        if not m:
            raise Fail("DFZ_ITEM_PARSE:%d" % n)
        items[tuple(int(x) for x in m.group(1).split())] = (n, m.group(2))
    info["dfz_form_from_packet"] = {"lhs": "".join(L[0]), "rhs": ["".join(t) for t in R]}
    info["dfz_packet_items"] = {" ".join(map(str, k)): v for k, v in items.items()}
    return dfz_form, items


# ----------------------------------------------------------------------------- graph / group
def build_graph(rep, info, edges, mut):
    nbr = {v: set() for v in range(1, 11)}
    for a, b in edges:
        nbr[a].add(b)
        nbr[b].add(a)
    info["edge_count"] = len(set(tuple(sorted(e)) for e in edges))
    if info["edge_count"] != 26 and mut not in ("graph_edge_9_10", "graph_drop_3_4"):
        rep.bad("GRAPH_EDGE_COUNT", info["edge_count"])
    sig, tau = perm_from_cycles(SIGMA_CYCLES), perm_from_cycles(TAU_CYCLES)
    if mut == "sym_sigma_inverse":
        sig = {sig[v]: v for v in sig}
    es = set(tuple(sorted(e)) for e in edges)
    for name, g in (("sigma", sig), ("tau", tau)):
        img = set(tuple(sorted((g[a], g[b]))) for a, b in es)
        if img != es:
            rep.bad("GRAPH_AUTOMORPHISM_FAIL", name)
    # group closure
    ident = tuple(range(1, 11))
    gens = [tuple(sig[v] for v in range(1, 11)), tuple(tau[v] for v in range(1, 11))]
    grp, frontier = {ident}, [ident]
    while frontier:
        new = []
        for p in frontier:
            for g in gens:
                q = tuple(g[p[v - 1] - 1] for v in range(1, 11))
                if q not in grp:
                    grp.add(q)
                    new.append(q)
        frontier = new
    info["group_order"] = len(grp)
    info["sigma_images_1_10"] = [sig[v] for v in range(1, 11)]
    info["tau_images_1_10"] = [tau[v] for v in range(1, 11)]
    # full automorphism count by backtracking (informational)
    order = sorted(range(1, 11), key=lambda v: -len(nbr[v]))
    cnt = [0]

    def bt(k, m, used):
        if k == 10:
            cnt[0] += 1
            return
        v = order[k]
        for w in range(1, 11):
            if w in used or len(nbr[w]) != len(nbr[v]):
                continue
            if all((u in nbr[v]) == (m[u] in nbr[w]) for u in m):
                m[v] = w
                used.add(w)
                bt(k + 1, m, used)
                used.discard(w)
                del m[v]
    bt(0, {}, set())
    info["full_automorphism_group_order"] = cnt[0]
    return nbr, sig, tau


# ----------------------------------------------------------------------------- branches
class Branch:
    def __init__(self, bid, vars_, steps):
        self.id = bid
        self.vars = vars_
        self.pos = {n: i for i, n in enumerate(vars_)}
        self.steps = steps    # list of dict(new, old, over, existing, atomic)


def make_publisher(rep):
    out = {}
    for bid, steps in PUBLISHER.items():
        vars_ = list(ORIG)
        st = []
        for new, old, over in steps:
            existing = set(vars_)
            oldn = [ORIG[v - 1] for v in old]
            overn = [ORIG[x - 1] if is_int(x) else x for x in over]
            if not set(oldn) <= existing or not set(overn) <= existing or set(oldn) & set(overn):
                raise Fail("PUBLISHER_STEP_INCONSISTENT:%s" % bid)
            st.append({"new": list(new), "old": oldn, "over": set(overn),
                       "existing": frozenset(existing), "atomic": False})
            vars_ = vars_ + list(new)
        out[bid] = Branch(bid, vars_, st)
    return out


def make_extras(rep, data):
    out = {}
    if not isinstance(data, list):
        raise Fail("EXTRA_SCHEMA:not list")
    for k, item in enumerate(data):
        if not (isinstance(item, list) and len(item) == 2 and all(isinstance(x, list) for x in item)):
            raise Fail("EXTRA_SCHEMA:%d" % k)
        S, T = item
        for x in S + T:
            if not is_int(x) or not 1 <= x <= 10:
                raise Fail("EXTRA_SCHEMA:%d:entry %r" % (k, x))
        if len(set(S)) != len(S) or len(set(T)) != len(T) or set(S) & set(T) or not S:
            raise Fail("EXTRA_SCHEMA:%d:overlap/dup/empty" % k)
        name = "s'%d" % k
        st = [{"new": [name], "old": [ORIG[v - 1] for v in S], "over": {ORIG[v - 1] for v in T},
               "existing": V_ALL, "atomic": len(S) > 1}]
        out["X%d" % k] = Branch("X%d" % k, list(ORIG) + [name], st)
    return out


def make_programs(rep, data, mut):
    out = {}
    if not isinstance(data, list):
        raise Fail("PROGRAM_SCHEMA:not list")
    for p, prog in enumerate(data):
        if not isinstance(prog, dict) or set(prog) != {"id", "steps"} or not isinstance(prog["id"], str) \
                or not isinstance(prog["steps"], list) or not prog["steps"]:
            raise Fail("PROGRAM_SCHEMA:%d" % p)
        made = []          # names of copies created so far, in order
        vars_ = list(ORIG)
        st = []
        for s, step in enumerate(prog["steps"]):
            if not isinstance(step, dict) or set(step) != {"copy", "over"} or \
                    not isinstance(step["copy"], list) or not isinstance(step["over"], list) or not step["copy"]:
                raise Fail("PROGRAM_SCHEMA:%d:%d" % (p, s))

            def resolve(x, where):
                if is_int(x):
                    if not 1 <= x <= 10:
                        raise Fail("PROGRAM_SCHEMA:%d:%d:%s:%r" % (p, s, where, x))
                    return ORIG[x - 1]
                if isinstance(x, str):
                    m = re.fullmatch(r"c(0|[1-9][0-9]*)", x)
                    if not m:
                        raise Fail("PROGRAM_SCHEMA:%d:%d:%s:%r" % (p, s, where, x))
                    j = int(m.group(1))
                    if j >= len(made):
                        rep.bad("PROGRAM_FUTURE_REFERENCE", "m%d step %d %s references %s (only %d copies exist)"
                                % (p, s, where, x, len(made)))
                        raise Fail("PROGRAM_FUTURE_REFERENCE")
                    return made[j]
                if isinstance(x, list):
                    raise Fail("UNSUPPORTED_ATOMIC_TUPLE")
                raise Fail("PROGRAM_SCHEMA:%d:%d:%s:%r" % (p, s, where, x))

            olds = [resolve(x, "copy") for x in step["copy"]]
            overs = [resolve(x, "over") for x in step["over"]]
            if len(set(olds)) != len(olds) or len(set(overs)) != len(overs) or set(olds) & set(overs):
                raise Fail("PROGRAM_SCHEMA:%d:%d:dup/overlap" % (p, s))
            existing = frozenset(vars_)
            new = []
            for _ in olds:
                nm = "m%d.c%d" % (p, len(made))
                made.append(nm)
                new.append(nm)
            st.append({"new": new, "old": olds, "over": set(overs), "existing": existing, "atomic": False})
            vars_ = vars_ + new
        out["M%d" % p] = Branch("M%d" % p, vars_, st)
    return out


# ----------------------------------------------------------------------------- expressions
def key(br, names):
    s = frozenset(names)
    if not s:
        return None
    if s <= V_ALL:
        return ("O", s)
    return (br.id, s)


def add(expr, k, c):
    if k is None or c == 0:
        return
    v = expr.get(k, 0) + c
    if v == 0:
        expr.pop(k, None)
    else:
        expr[k] = v


def h(expr, br, names, c=1):
    add(expr, key(br, names), Fraction(c))


def cmi(expr, br, X, Y, Z, c=1):
    X, Y, Z = set(X), set(Y), set(Z)
    h(expr, br, X | Z, c)
    h(expr, br, Y | Z, c)
    h(expr, br, X | Y | Z, -c)
    h(expr, br, Z, -c)


def bits(mask, n):
    return [i for i in range(n) if mask >> i & 1]


# ----------------------------------------------------------------------------- main
def run(mut, sleep_s, capture=None):
    t0 = time.time()
    rep = Report()
    info = {"mutation": mut}
    raw = open(CERT, "rb").read()
    info["certificate_sha256"] = sha_bytes(raw)
    info["certificate_bytes"] = len(raw)
    info["certificate_LF"] = raw.count(b"\n")
    pinned = CERT_SHA if mut != "hash_pin_wrong" else "0" * 64
    if info["certificate_sha256"] != pinned or info["certificate_bytes"] != 239532 or info["certificate_LF"] != 1:
        raise Fail("INPUT_HASH_MISMATCH:certificate")
    if sleep_s:
        time.sleep(sleep_s)
    if mut == "dup_json_key":
        i = raw.index(b'"bound": ')
        raw = raw[:i] + b'"bound": "716/107", ' + raw[i:]
    cert = strict_load(raw, rep)
    if not isinstance(cert, dict) or set(cert) != TOP_KEYS:
        raise Fail("JSON_SCHEMA:top-level keys %r" % (sorted(cert) if isinstance(cert, dict) else type(cert)))
    dfz_form, dfz_items = bind_sources(rep, info)

    edges = list(EDGES)
    if mut == "graph_edge_9_10":
        edges.append((9, 10))
    if mut == "graph_drop_3_4":
        edges.remove((3, 4))
    nbr, sig, tau = build_graph(rep, info, edges, mut)
    gens = [sig, tau]
    fd_nbr = {v: set(nbr[v]) for v in nbr}
    if mut == "graph_fd_nbr":
        fd_nbr[1].discard(7)

    if mut == "program_overset_drop":
        cert["programs"][4]["steps"][0]["over"].remove(10)
    if mut == "program_overset_add":
        cert["programs"][4]["steps"][0]["over"].append(3)
    if mut == "future_copy_ref":
        ov = cert["programs"][4]["steps"][1]["over"]
        ov[ov.index("c0")] = "c2"
    if mut == "future_copy_self":
        cert["programs"][4]["steps"][1]["over"].append("c1")

    branches = {"B": Branch("B", list(ORIG), [])}
    branches.update(make_publisher(rep))
    branches.update(make_extras(rep, cert["extra_single_copies"]))
    branches.update(make_programs(rep, cert["programs"], mut))
    by_vars = {tuple(b.vars): b for b in branches.values()}
    if len(by_vars) != len(branches):
        rep.bad("BRANCH_VARLIST_COLLISION", len(branches) - len(by_vars))
    owner = {}
    for b in branches.values():
        if len(set(b.vars)) != len(b.vars) or b.vars[:10] != ORIG:
            rep.bad("BRANCH_VARLIST_MALFORMED", b.id)
        for nm in b.vars[10:]:
            if nm in owner or nm in V_ALL:
                rep.bad("COPY_NAME_SHARED_ACROSS_BRANCHES", [nm, owner.get(nm), b.id])
            owner[nm] = b.id
    info["private_copy_names"] = len(owner)
    pub_step = {}
    for bid in ("P1", "P2", "P3"):
        for s, st in enumerate(branches[bid].steps):
            pub_step[tuple(st["new"])] = (branches[bid], st)
    if capture is not None:            # used only by the reviewer's float semantic self-test
        capture["branches"] = branches
        capture["rows"] = []

    M = cert["multipliers"]
    if not isinstance(M, list):
        raise Fail("JSON_SCHEMA:multipliers")
    M_orig = json.loads(json.dumps(M))
    mi = None                           # index of the single mutated record, if any
    if mut == "flip_sign_cmi":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "cmi")
        M[mi]["multiplier"] = M[mi]["multiplier"].lstrip("-")
    if mut == "cap_value":
        mi = next(k for k, m in enumerate(M) if m["row"] == ["cap", 4])
        M[mi]["multiplier"] = "281/107"
    if mut == "cap_vertex":
        mi = next(k for k, m in enumerate(M) if m["row"] == ["cap", 4])
        M[mi]["row"] = ["cap", 3]
    if mut == "drop_row_dfz":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "dfz")
        M.pop(mi)
    if mut == "drop_row_cmi":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "cmi")
        M.pop(mi)
    if mut == "cross_branch_varlist":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "cmi" and "g'3" in m["row"][1])
        M[mi]["row"][1] = [("g'2" if x == "g'3" else x) for x in M[mi]["row"][1]]
    if mut == "dfz_coeff":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "dfz")
        M[mi]["row"][1][0] = 4
    if mut == "copy_u_outside":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "copy" and m["row"][1] == ["d'1", "e'1"])
        M[mi]["row"][3] |= 1 << 3       # add X4 (= copied variable, not in over-set)
    if mut == "xcopy_u_outside":
        mi = next(k for k, m in enumerate(M) if m["row"][0] == "xcopy" and m["row"][1] == 0)
        M[mi]["row"][2] |= 1 << 0       # add X1 (copied variable of extra branch 0)
    if mi is not None:
        info["mutated_record_index"] = mi
        info["mutated_record_original"] = M_orig[mi]
        info["mutated_record_after"] = None if mut.startswith("drop_row") else M[mi]

    total = {}
    seen = {}
    sem_seen = {}
    counts, bcounts, sign_ok = {}, {}, {"ge0_nonpositive": 0, "cap_nonnegative": 0, "eq_any": 0}
    cap_sum = Fraction(0)
    cap_vertices = {}
    zero_rows = 0
    coord_rows = {}
    dfz_rows = []
    denoms = set()

    def decode(idx, row):
        """Rebuild one row expression from its declared semantics; raises Fail on any defect."""
        expr = {}
        br = branches["B"]
        sem = None
        if not isinstance(row, list) or not row or not isinstance(row[0], str):
            raise Fail("ROW_SCHEMA")
        kind = row[0]
        if kind == "mono":
            if len(row) != 3 or not isinstance(row[1], list) or not is_int(row[2]):
                raise Fail("ROW_SCHEMA")
            br = by_vars.get(tuple(row[1]))
            if br is None:
                raise Fail("VARLIST_NOT_A_BRANCH")
            n = len(br.vars)
            i = row[2]
            if not 0 <= i < n:
                raise Fail("INDEX_RANGE")
            h(expr, br, br.vars, 1)
            h(expr, br, [x for k, x in enumerate(br.vars) if k != i], -1)
            sem = ("mono", br.id, i)
        elif kind == "cmi":
            if len(row) != 5 or not isinstance(row[1], list) or not all(is_int(x) for x in row[2:]):
                raise Fail("ROW_SCHEMA")
            br = by_vars.get(tuple(row[1]))
            if br is None:
                raise Fail("VARLIST_NOT_A_BRANCH")
            n = len(br.vars)
            i, j, K = row[2], row[3], row[4]
            if not (0 <= i < n and 0 <= j < n and i != j and 0 <= K < (1 << n)):
                raise Fail("INDEX_RANGE")
            if K >> i & 1 or K >> j & 1:
                raise Fail("CMI_INDEX_IN_CONDITION")
            if i > j:
                rep.warnings.append("cmi i>j at %d" % idx)
            cmi(expr, br, [br.vars[i]], [br.vars[j]], [br.vars[k] for k in bits(K, n)])
            sem = ("cmi", br.id, min(i, j), max(i, j), K)
        elif kind == "fd":
            if len(row) != 2 or not is_int(row[1]) or not 1 <= row[1] <= 10:
                raise Fail("ROW_SCHEMA")
            v = row[1]
            N = [ORIG[u - 1] for u in sorted(fd_nbr[v])]
            h(expr, br, N + [ORIG[v - 1]], 1)
            h(expr, br, N, -1)
        elif kind == "cap":
            if len(row) != 2 or not is_int(row[1]) or not 1 <= row[1] <= 10:
                raise Fail("ROW_SCHEMA")
            h(expr, br, [ORIG[row[1] - 1]], 1)
        elif kind == "sym":
            if len(row) != 3 or not is_int(row[1]) or not is_int(row[2]):
                raise Fail("ROW_SCHEMA")
            g, S = row[1], row[2]
            if g not in (0, 1) or not 1 <= S < 1024:
                raise Fail("INDEX_RANGE")
            Sv = [k + 1 for k in bits(S, 10)]
            h(expr, br, [ORIG[v - 1] for v in Sv], 1)
            h(expr, br, [ORIG[gens[g][v] - 1] for v in Sv], -1)
        elif kind in ("copy", "independence"):
            if len(row) < 2 or not isinstance(row[1], list) or tuple(row[1]) not in pub_step:
                raise Fail("UNKNOWN_COPY_STEP")
            br, st = pub_step[tuple(row[1])]
            if kind == "copy":
                if len(row) != 4 or not is_int(row[2]) or not is_int(row[3]):
                    raise Fail("ROW_SCHEMA")
                copy_row(expr, br, st, row[2], row[3], mut)
            else:
                if len(row) != 2:
                    raise Fail("ROW_SCHEMA")
                indep_row(expr, br, st, mut)
        elif kind in ("xcopy", "xindependence"):
            if len(row) < 2 or not is_int(row[1]) or "X%d" % row[1] not in branches:
                raise Fail("INDEX_RANGE")
            br = branches["X%d" % row[1]]
            st = br.steps[0]
            if kind == "xcopy":
                if len(row) != 3 or not is_int(row[2]):
                    raise Fail("ROW_SCHEMA")
                copy_row(expr, br, st, (1 << len(st["new"])) - 1, row[2], mut)
            else:
                if len(row) != 2:
                    raise Fail("ROW_SCHEMA")
                indep_row(expr, br, st, mut)
        elif kind in ("mcopy", "mindependence"):
            if len(row) < 3 or not isinstance(row[1], str) or not re.fullmatch(r"m(0|[1-9][0-9]*)", row[1]):
                raise Fail("ROW_SCHEMA")
            bid = "M" + row[1][1:]
            if bid not in branches or not is_int(row[2]) or not 0 <= row[2] < len(branches[bid].steps):
                raise Fail("INDEX_RANGE")
            br = branches[bid]
            st = br.steps[row[2]]
            if kind == "mcopy":
                if len(row) != 5 or not is_int(row[3]) or not is_int(row[4]):
                    raise Fail("ROW_SCHEMA")
                copy_row(expr, br, st, row[3], row[4], mut)
            else:
                if len(row) != 3:
                    raise Fail("ROW_SCHEMA")
                indep_row(expr, br, st, mut)
        elif kind == "dfz":
            if len(row) != 7 or not isinstance(row[1], list) or len(row[1]) != 9 or \
                    not all(is_int(x) for x in row[1]) or not all(is_int(x) for x in row[2:]):
                raise Fail("ROW_SCHEMA")
            coef = row[1]
            masks = row[2:]
            if not all(0 <= m < 1024 for m in masks) or not all(masks[:4]):
                raise Fail("INDEX_RANGE")
            for a in range(5):
                for b in range(a + 1, 5):
                    if masks[a] & masks[b]:
                        raise Fail("DFZ_BLOCKS_NOT_DISJOINT")
            blk = {L: [ORIG[k] for k in bits(m, 10)] for L, m in zip("ABCD", masks[:4])}
            Z = [ORIG[k] for k in bits(masks[4], 10)]
            c = dict(zip("abcdefghi", coef))
            (lc, lx, ly, lz) = dfz_form["lhs"]
            cmi(expr, br, sum((blk[q] for q in lx), []), sum((blk[q] for q in ly), []),
                sum((blk[q] for q in lz), []) + Z, -c[lc])
            for (rc, rx, ry, rz) in dfz_form["rhs"]:
                cmi(expr, br, sum((blk[q] for q in rx), []), sum((blk[q] for q in ry), []),
                    sum((blk[q] for q in rz), []) + Z, c[rc])
            sem = ("dfz", {"coefficients": coef, "A": blk["A"], "B": blk["B"], "C": blk["C"],
                           "D": blk["D"], "Z": Z, "packet_line": dfz_items.get(tuple(coef), [None])[0],
                           "expanded_coordinates": len(expr)})
        else:
            raise Fail("UNKNOWN_ROW_KIND")
        return kind, br, expr, sem

    for idx, rec in enumerate(M):
        if not isinstance(rec, dict) or set(rec) != {"row", "multiplier"}:
            rep.bad("ROW_SCHEMA", "record %d keys" % idx)
            continue
        row, ms = rec["row"], rec["multiplier"]
        if not isinstance(ms, str) or not MULT_RE.match(ms):
            rep.bad("MULTIPLIER_FORMAT", "record %d: %r" % (idx, ms))
            continue
        w = Fraction(ms)
        if str(w) != ms:
            rep.warnings.append("non-canonical multiplier at %d: %s" % (idx, ms))
        if w == 0:
            rep.warnings.append("ZERO_MULTIPLIER record %d (not a support row)" % idx)
        denoms.add(w.denominator)
        sk = json.dumps(row, sort_keys=True)
        if sk in seen:
            rep.warnings.append("DUPLICATE_ROW records %d and %d" % (seen[sk], idx))
        seen[sk] = idx
        try:
            kind, br, expr, sem = decode(idx, row)
            if capture is not None:
                capture["rows"].append((idx, kind, br.id, expr, Fraction(ms)))
        except Fail as e:
            rep.bad(str(e).split(":")[0], "record %d row %s" % (idx, json.dumps(row)[:160]))
            continue
        if kind == "dfz":
            coef = row[1]
            if tuple(coef) not in dfz_items:
                rep.bad("DFZ_TUPLE_NOT_IN_SOURCE", coef)
            if coef != DECLARED_DFZ:
                rep.bad("DFZ_TUPLE_NOT_DECLARED", coef)
            d = dict(sem[1])
            d.update({"record": idx, "multiplier": ms})
            dfz_rows.append(d)
        elif sem is not None:
            if sem in sem_seen:
                rep.warnings.append("DUPLICATE_ROW_SEMANTIC records %d and %d" % (sem_seen[sem], idx))
            sem_seen[sem] = idx
        # sign discipline
        if kind in GE0:
            if w > 0:
                rep.bad("SIGN_GE0_POSITIVE", "record %d %s mult %s" % (idx, kind, ms))
            else:
                sign_ok["ge0_nonpositive"] += 1
        elif kind == "cap":
            if w < 0:
                rep.bad("SIGN_CAP_NEGATIVE", "record %d mult %s" % (idx, ms))
            else:
                sign_ok["cap_nonnegative"] += 1
            cap_sum += w
            cap_vertices[row[1]] = cap_vertices.get(row[1], 0) + 1
        else:
            sign_ok["eq_any"] += 1
        if not expr:
            zero_rows += 1
        counts[kind] = counts.get(kind, 0) + 1
        bcounts["%s@%s" % (kind, br.id)] = bcounts.get("%s@%s" % (kind, br.id), 0) + 1
        for k2, c2 in expr.items():
            add(total, k2, w * c2)
            coord_rows.setdefault(k2, set()).add(br.id)

    target = ("O", V_ALL)
    residual = dict(total)
    add(residual, target, Fraction(-1))
    if mi is not None:
        # reason-specific check: the residual must be exactly (mutated - original) contribution
        # of the single mutated record (the unmutated identity holds, see the 'none' control)
        delta = {}
        _, _, e0, _ = decode(-1, M_orig[mi]["row"])
        for k2, c2 in e0.items():
            add(delta, k2, -Fraction(M_orig[mi]["multiplier"]) * c2)
        mode = "record dropped"
        if not mut.startswith("drop_row"):
            try:
                _, _, e1, _ = decode(-1, M[mi]["row"])
                for k2, c2 in e1.items():
                    add(delta, k2, Fraction(M[mi]["multiplier"]) * c2)
                mode = "record replaced"
            except Fail as e:
                mode = "mutated record rejected (%s), so excluded from the sum" % e
        info["intended_delta_mode"] = mode
        info["residual_equals_intended_delta"] = (residual == delta)
        info["intended_delta_nonzero_coordinates"] = len(delta)
    scopes = {}
    for k2 in coord_rows:
        scopes.setdefault(k2[0], 0)
        scopes[k2[0]] += 1
    private_mixed = [k2 for k2, bs in coord_rows.items() if k2[0] != "O" and bs != {k2[0]}]
    if private_mixed:
        rep.bad("CROSS_BRANCH_PRIVATE_COORDINATE", len(private_mixed))
    if residual:
        items = sorted(residual.items(), key=lambda kv: (kv[0][0], len(kv[0][1]), sorted(kv[0][1])))
        rep.bad("IDENTITY_RESIDUAL", {"nonzero_coordinates": len(items),
                                      "all": [[k2[0], "".join(sorted(k2[1])) if k2[0] == "O" else sorted(k2[1]),
                                               str(v)] for k2, v in items[:300]]})
    declared = Fraction(cert["bound"]) if isinstance(cert["bound"], str) and MULT_RE.match(cert["bound"]) else None
    if declared is None or declared != cap_sum:
        rep.bad("BOUND_MISMATCH", {"declared": cert["bound"], "cap_sum": str(cap_sum)})
    if not is_int(cert["support_rows"]) or cert["support_rows"] != len(M):
        rep.bad("SUPPORT_COUNT_MISMATCH", {"declared": cert["support_rows"], "records": len(M)})
    if any(c > 1 for c in cap_vertices.values()):
        rep.warnings.append("repeated cap vertex")
    lcm = 1
    for d in denoms:
        from math import gcd
        lcm = lcm * d // gcd(lcm, d)
    info.update({
        "records": len(M),
        "row_kind_counts": dict(sorted(counts.items())),
        "row_kind_by_branch": dict(sorted(bcounts.items())),
        "sign_checks": sign_ok,
        "cap_rows": {str(v): str(next(Fraction(m["multiplier"]) for m in M if m["row"] == ["cap", v]))
                     for v in sorted(cap_vertices)},
        "cap_sum": str(cap_sum),
        "declared_bound": cert["bound"],
        "bound_float_info": [cert["bound_float"], cert["float_objective"], float(cap_sum)],
        "distinct_coordinates_touched": len(coord_rows),
        "coordinates_by_scope": dict(sorted(scopes.items())),
        "shared_coordinates_used_by_multiple_branches": sum(1 for k2, bs in coord_rows.items()
                                                             if k2[0] == "O" and len(bs) > 1),
        "nonzero_total_coordinates": len(total),
        "total_at_target": str(total.get(target, 0)),
        "residual_nonzero_coordinates": len(residual),
        "zero_expression_rows": zero_rows,
        "multiplier_denominator_lcm": lcm,
        "branches": {b.id: {"vars": b.vars,
                            "steps": [{"new": s["new"], "copied": s["old"], "over": sorted(s["over"]),
                                       "existing_at_step": sorted(s["existing"])} for s in b.steps]}
                     for b in branches.values()},
        "unused_branches": sorted(set(branches) - {k.split("@")[1] for k in bcounts}),
        "dfz_rows": dfz_rows,
        "cert_metadata": {"branches_label": cert["branches"], "convention": cert["convention"],
                          "source_result_sha256": cert["source_result_sha256"], "elapsed_s": cert["elapsed_s"]},
        "runtime_s": round(time.time() - t0, 3),
    })
    if rep.reasons:
        status = "INVALID"
    elif rep.unknown:
        status = "UNKNOWN"
    else:
        status = "VALID"
    return status, rep, info


def copy_row(expr, br, st, qmask, umask, mut):
    n = len(br.vars)
    k = len(st["new"])
    if not 1 <= qmask < (1 << k):
        raise Fail("COPY_QMASK_RANGE")
    if not 0 <= umask < (1 << n):
        raise Fail("INDEX_RANGE")
    U = [br.vars[i] for i in bits(umask, n)]
    if not set(U) <= st["over"]:
        raise Fail("COPY_U_NOT_IN_OVERSET")
    q = bits(qmask, k)
    if mut == "qmask_bit_order" and k == 2:
        q = [1 - t for t in q]
    if st["atomic"]:
        newQ, oldQ = st["new"], st["old"]
    else:
        newQ = [st["new"][t] for t in q]
        oldQ = [st["old"][t] for t in q]
    h(expr, br, U + newQ, 1)
    h(expr, br, U + oldQ, -1)


def indep_row(expr, br, st, mut):
    """Copy-step independence I(new ; E_s - O_s | O_s) = 0, E_s = variables existing BEFORE the
    step.  It is an equality, so its orientation is a pure encoding convention; the raw data
    uses the orientation  -I(...)  (all 13 such rows carry multipliers < 0, i.e. they enter
    the identity as +|w| * I).  The reviewer's first development run used +I and failed with
    residual exactly 2*sum(w*I); mutation 'indep_orientation_plus' reproduces that run."""
    E = set(st["existing"])
    if mut == "chronology_final_E":
        E = set(br.vars) - set(st["new"])
    O = set(st["over"])
    if not O <= E:
        raise Fail("INDEPENDENCE_OVERSET_UNAVAILABLE")
    cmi(expr, br, st["new"], E - O, O, 1 if mut == "indep_orientation_plus" else -1)


MUTATIONS = ["none", "flip_sign_cmi", "cap_value", "cap_vertex", "program_overset_drop",
             "program_overset_add", "future_copy_ref", "future_copy_self", "chronology_final_E",
             "graph_fd_nbr", "graph_edge_9_10", "graph_drop_3_4", "drop_row_dfz", "drop_row_cmi",
             "dup_json_key", "cross_branch_varlist", "dfz_coeff", "copy_u_outside", "xcopy_u_outside",
             "sym_sigma_inverse", "qmask_bit_order", "indep_orientation_plus", "hash_pin_wrong"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutate", default="none", choices=MUTATIONS)
    ap.add_argument("--sleep", type=float, default=0.0, help="timeout-driver probe only")
    a = ap.parse_args()
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    try:
        status, rep, info = run(a.mutate, a.sleep)
        out = {"status": status, "reason_codes": rep.codes(), "reasons": rep.reasons,
               "warnings": rep.warnings[:50], "warning_count": len(rep.warnings), "info": info}
    except Fail as e:
        code = str(e).split(":")[0]
        status = "UNKNOWN" if code.startswith("UNSUPPORTED") else "INVALID"
        if code == "INPUT_HASH_MISMATCH":
            status = "BINDING_FAILURE"
        out = {"status": status, "reason_codes": [code], "reasons": [[code, str(e)]], "info": {"mutation": a.mutate}}
    out["verifier_sha256"] = sha_bytes(open(__file__, "rb").read())
    out["started_utc"] = started
    out["finished_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(json.dumps(out, sort_keys=True, default=str))
    return {"VALID": 0, "INVALID": 1, "UNKNOWN": 2, "BINDING_FAILURE": 3}[out["status"]]


if __name__ == "__main__":
    sys.exit(main())
