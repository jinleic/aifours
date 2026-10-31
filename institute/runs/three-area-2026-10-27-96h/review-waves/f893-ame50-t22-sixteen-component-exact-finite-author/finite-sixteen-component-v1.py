#!/usr/bin/env python3
# f893 UNRUN exact local finite source v1. Author: VerifyF893AME22Finite (GENERAL AUTHOR).
# Standard library only. No file writes, no network, no subprocess, no randomness.
"""Exact local enumeration, up to physical party/symbol relabeling, of connected
agreement-closed E components of a fixed size N (N=16 is the target; N=12 is used
only as an engine control) with a prescribed sorted local alphabet profile such that:

  (a) in each of the six physical pair systems every used pair value has exactly two
      extensions inside the component;
  (b) each of the three balanced cuts, restricted to the component, is a disjoint
      union of K2,2 blocks;
  (c) the agreement graph (distinct words sharing >=2 coordinates) is connected.

For every class it computes the maximum number of component words in a
two-symbol-per-party binary box (the actual-E necessary bound is <=7) and evaluates the
unit-phase block-cycle condition: every INTEGRAL left-kernel vector of the signed
square matrix (one row per cut-indexed K2,2 block: +1 diagonal, -1 off-diagonal) has
even coordinate sum.  Each verdict carries an independently re-verified exact
certificate: an odd-sum integral y with y^T A = 0, or a rational phase vector theta
with A theta - 1/2 in Z^rows.

This is a LOCAL component classification only: not a P22 completion, not an AME or
support-50 witness, not a global classification.  Cooperative internal limit LIMIT_S;
on timeout the run reports INCOMPLETE (exit 2), never PASS.
"""
import itertools
import json
import sys
import time
from fractions import Fraction

LIMIT_S = 38.0
_T0 = time.monotonic()
_DEADLINE = _T0 + LIMIT_S

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
CUTS = ((0, 5), (1, 4), (2, 3))  # indices into PAIRS: AB|CD, AC|BD, AD|BC
CUT_NAMES = ("AB|CD", "AC|BD", "AD|BC")
TARGET_PROFILES = ((2, 4, 4, 4), (3, 3, 3, 3), (3, 3, 3, 4),
                   (3, 3, 4, 4), (3, 4, 4, 4), (4, 4, 4, 4))
TARGET_N = 16


class Timeout(Exception):
    pass


def check_time():
    if time.monotonic() > _DEADLINE:
        raise Timeout()


def pval(w, p):
    i, j = PAIRS[p]
    return (w[i], w[j])


# ---------------------------------------------------------------------------
# Independent from-scratch structural validator (does not share code with search)
# ---------------------------------------------------------------------------

def alphabets(S):
    return [sorted({w[t] for w in S}) for t in range(4)]


def pair_extensions_ok(S):
    """Every used pair value, in each of the six pair systems, has exactly two words."""
    for p in range(6):
        g = {}
        for w in S:
            k = pval(w, p)
            g[k] = g.get(k, 0) + 1
        if any(c != 2 for c in g.values()):
            return False
    return True


def degrees(S):
    """degrees[t][x] = common number of partner symbols of x (party t) at every other
    party, or None when partner counts differ or occurrence != 2*partners."""
    out = []
    for t in range(4):
        d = {}
        for x in sorted({w[t] for w in S}):
            ws = [w for w in S if w[t] == x]
            parts = {len({w[u] for w in ws}) for u in range(4) if u != t}
            if len(parts) != 1:
                return None
            dx = next(iter(parts))
            if len(ws) != 2 * dx:
                return None
            d[x] = dx
        out.append(d)
    return out


def cut_is_k22_union(S, p1, p2):
    """Rows = pair-p1 values, columns = pair-p2 values, one edge per word."""
    rows, cols = {}, {}
    for w in S:
        r, c = pval(w, p1), pval(w, p2)
        rows.setdefault(r, set()).add(c)
        cols.setdefault(c, set()).add(r)
    if any(len(v) != 2 for v in rows.values()) or any(len(v) != 2 for v in cols.values()):
        return False
    for r, cs in rows.items():
        c1, c2 = sorted(cs)
        if cols[c1] - {r} != cols[c2] - {r}:
            return False
    return True


def agreement_connected(S):
    if not S:
        return False
    seen = {S[0]}
    stack = [S[0]]
    while stack:
        w = stack.pop()
        for v in S:
            if v not in seen and sum(1 for t in range(4) if v[t] == w[t]) >= 2:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(S)


def max_binary_box(S):
    """Maximum number of words of S inside A2 x B2 x C2 x D2 with |X2|=2 (or the whole
    used alphabet when it has fewer than two symbols)."""
    al = alphabets(S)
    choices = [list(itertools.combinations(a, 2)) if len(a) >= 2 else [tuple(a)] for a in al]
    best, arg = 0, None
    for box in itertools.product(*choices):
        c = sum(1 for w in S if all(w[t] in box[t] for t in range(4)))
        if c > best:
            best, arg = c, box
    return best, arg


def structural_reason(S, profile, n):
    """None if S satisfies (a),(b),(c), size n and sorted profile; else first reason."""
    if len(S) != n:
        return "SIZE"
    if len(set(S)) != n:
        return "REPEATED_WORD"
    if any(len(w) != 4 or any(type(x) is not int or not 0 <= x <= 5 for x in w) for w in S):
        return "BAD_WORD"
    if tuple(sorted(len(a) for a in alphabets(S))) != tuple(sorted(profile)):
        return "PROFILE"
    if not pair_extensions_ok(S):
        return "PAIR_EXTENSIONS"
    deg = degrees(S)
    if deg is None:
        return "DEGREE_INCONSISTENT"
    if any(d < 2 for dt in deg for d in dt.values()):
        return "DEGREE_LT_2"
    for (p1, p2) in CUTS:
        if not cut_is_k22_union(S, p1, p2):
            return "CUT_NOT_K22"
    if not agreement_connected(S):
        return "DISCONNECTED"
    return None


# ---------------------------------------------------------------------------
# Unit-phase block-cycle condition (integral left kernel, exact certificates)
# ---------------------------------------------------------------------------

def square_matrix(S):
    """One signed row per cut-indexed K2,2 block [[a,b],[c,d]]: +1 at a,d and -1 at b,c."""
    idx = {w: k for k, w in enumerate(S)}
    out = []
    for ci, (p1, p2) in enumerate(CUTS):
        cell, rows = {}, {}
        for w in S:
            r, c = pval(w, p1), pval(w, p2)
            cell[(r, c)] = w
            rows.setdefault(r, []).append(c)
        done = set()
        for r in sorted(rows):
            if r in done:
                continue
            c1, c2 = sorted(rows[r])
            r2 = next((rr for rr in sorted(rows) if rr != r and sorted(rows[rr]) == [c1, c2]), None)
            if r2 is None:
                raise ValueError("cut is not a union of K2,2 blocks")
            done.update((r, r2))
            a, b, c, d = cell[(r, c1)], cell[(r, c2)], cell[(r2, c1)], cell[(r2, c2)]
            row = [0] * len(S)
            row[idx[a]] += 1
            row[idx[d]] += 1
            row[idx[b]] -= 1
            row[idx[c]] -= 1
            out.append((CUT_NAMES[ci], (a, b, c, d), row))
    return out


def rowvec_times(y, A, ncols):
    return [sum(y[i] * A[i][j] for i in range(len(A))) for j in range(ncols)]


def integer_row_echelon(A, ncols):
    """Unimodular integer row reduction: returns H, V, pivot columns with V A = H."""
    m = len(A)
    H = [list(r) for r in A]
    V = [[int(i == j) for j in range(m)] for i in range(m)]
    piv = []
    r = 0
    for c in range(ncols):
        if r >= m:
            break
        while True:
            nz = [i for i in range(r, m) if H[i][c] != 0]
            if not nz:
                break
            s = min(nz, key=lambda i: (abs(H[i][c]), i))
            if s != r:
                H[r], H[s] = H[s], H[r]
                V[r], V[s] = V[s], V[r]
            clean = True
            for i in range(r + 1, m):
                if H[i][c]:
                    q = H[i][c] // H[r][c]
                    H[i] = [x - q * y for x, y in zip(H[i], H[r])]
                    V[i] = [x - q * y for x, y in zip(V[i], V[r])]
                    if H[i][c]:
                        clean = False
            if clean:
                break
        if H[r][c] != 0:
            piv.append(c)
            r += 1
    return H, V, piv


def phase_evaluate(A, ncols):
    m = len(A)
    H, V, piv = integer_row_echelon(A, ncols)
    for i in range(m):
        if rowvec_times(V[i], A, ncols) != H[i]:
            return {"verdict": "INTERNAL_ERROR", "why": "V*A != H"}
    rank = len(piv)
    if any(any(H[i]) for i in range(rank, m)):
        return {"verdict": "INTERNAL_ERROR", "why": "nonzero row below rank"}
    basis = [V[i] for i in range(rank, m)]
    for y in basis:
        if any(rowvec_times(y, A, ncols)):
            return {"verdict": "INTERNAL_ERROR", "why": "basis row not in left kernel"}
    res = {"rows": m, "cols": ncols, "rank": rank, "left_kernel_rank": m - rank,
           "basis_sum_parities": [sum(y) % 2 for y in basis]}
    odd = [y for y in basis if sum(y) % 2]
    if odd:
        y = odd[0]
        ok = not any(rowvec_times(y, A, ncols)) and sum(y) % 2 == 1
        res["verdict"] = "ODD_INTEGRAL_DEPENDENCY" if ok else "INTERNAL_ERROR"
        res["certificate_y"] = y
        return res
    theta = [Fraction(0)] * ncols
    for k in range(rank - 1, -1, -1):
        c = piv[k]
        acc = Fraction(sum(V[k]), 2) - sum(H[k][j] * theta[j] for j in range(ncols) if j != c)
        theta[c] = acc / H[k][c]
    ok = all((sum(A[i][j] * theta[j] for j in range(ncols)) - Fraction(1, 2)).denominator == 1
             for i in range(m))
    res["verdict"] = "EVEN_PHASES_EXIST" if ok else "INTERNAL_ERROR"
    res["certificate_theta"] = [str(t) for t in theta]
    return res


def sign_only_solvable(A, ncols):
    """MUTANT evaluator: sign phases only, i.e. A x = 1 over F2."""
    rows = [[x % 2 for x in r] + [1] for r in A]
    m, r = len(rows), 0
    for c in range(ncols):
        s = next((i for i in range(r, m) if rows[i][c]), None)
        if s is None:
            continue
        rows[r], rows[s] = rows[s], rows[r]
        for i in range(m):
            if i != r and rows[i][c]:
                rows[i] = [x ^ y for x, y in zip(rows[i], rows[r])]
        r += 1
    return not any(rows[i][ncols] for i in range(r, m))


def phase_of_component(S):
    sq = square_matrix(S)
    return phase_evaluate([row for (_, _, row) in sq], len(S)), sq


# ---------------------------------------------------------------------------
# Exhaustive growth search (fresh-label symmetry breaking, forced K2,2 closure)
# ---------------------------------------------------------------------------

class ComponentSearch:
    def __init__(self, q, n):
        self.q = tuple(q)
        self.n = n
        self.minq_other = [min(q[u] for u in range(4) if u != t) for t in range(4)]
        self.words = []
        self.wset = set()
        self.pv = {}
        self.cnt = [[0] * 6 for _ in range(4)]
        self.nodes = 0
        self.found = []

    @staticmethod
    def keys(w):
        return [(p, w[PAIRS[p][0]], w[PAIRS[p][1]]) for p in range(6)]

    def add(self, w):
        self.words.append(w)
        self.wset.add(w)
        for k in self.keys(w):
            self.pv.setdefault(k, []).append(w)
        for t in range(4):
            self.cnt[t][w[t]] += 1

    def remove(self, w):
        if self.words[-1] != w:
            raise RuntimeError("non-LIFO removal")
        self.words.pop()
        self.wset.discard(w)
        for k in self.keys(w):
            L = self.pv[k]
            L.remove(w)
            if not L:
                del self.pv[k]
        for t in range(4):
            self.cnt[t][w[t]] -= 1

    def used(self, t):
        return sum(1 for c in self.cnt[t] if c)

    def can_add(self, v):
        if v in self.wset or len(self.words) >= self.n:
            return False
        if any(v[t] >= self.q[t] for t in range(4)):
            return False
        return all(len(self.pv.get(k, ())) <= 1 for k in self.keys(v))

    def propagate(self):
        """Close every cut 4-cycle forced by two known mates; None on contradiction."""
        added = []
        changed = True
        while changed:
            changed = False
            for (p1, p2) in CUTS:
                (i, j), (k, l) = PAIRS[p1], PAIRS[p2]
                for w in list(self.words):
                    L1 = self.pv[(p1, w[i], w[j])]
                    L2 = self.pv[(p2, w[k], w[l])]
                    if len(L1) != 2 or len(L2) != 2:
                        continue
                    w1 = L1[1] if L1[0] == w else L1[0]
                    u = L2[1] if L2[0] == w else L2[0]
                    v = [0, 0, 0, 0]
                    v[i], v[j], v[k], v[l] = u[i], u[j], w1[k], w1[l]
                    v = tuple(v)
                    if v in self.wset:
                        continue
                    if not self.can_add(v):
                        for x in reversed(added):
                            self.remove(x)
                        return None
                    self.add(v)
                    added.append(v)
                    changed = True
        return added

    def bounds_ok(self):
        rem = self.n - len(self.words)
        per_p = [0] * 6
        pending = 0
        pc = [[[0] * 4 for _ in range(6)] for _ in range(4)]
        for (p, a, b), L in self.pv.items():
            per_p[p] += 1
            if len(L) == 1:
                pending += 1
            i, j = PAIRS[p]
            pc[i][a][j] += 1
            pc[j][b][i] += 1
        if any(c > self.n // 2 for c in per_p):
            return False
        if pending > 6 * rem:
            return False
        for t in range(4):
            need, used = 0, 0
            for x in range(6):
                c = self.cnt[t][x]
                if not c:
                    continue
                used += 1
                req = max(4, 2 * max(pc[t][x]), c + (c & 1))
                if req > 2 * self.minq_other[t]:
                    return False
                need += req - c
            need += 4 * (self.q[t] - used)
            if need > rem:
                return False
        return True

    def candidates(self, key):
        p, a, b = key
        i, j = PAIRS[p]
        k, l = [t for t in range(4) if t not in (i, j)]
        out = []
        for x in range(min(self.used(k) + 1, self.q[k])):
            for y in range(min(self.used(l) + 1, self.q[l])):
                v = [0, 0, 0, 0]
                v[i], v[j], v[k], v[l] = a, b, x, y
                v = tuple(v)
                if self.can_add(v):
                    out.append(v)
        return out

    def rec(self):
        self.nodes += 1
        if not self.nodes & 255:
            check_time()
        added = self.propagate()
        if added is None:
            return
        self.branch()
        for x in reversed(added):
            self.remove(x)

    def branch(self):
        n = len(self.words)
        pending = [k for k, L in self.pv.items() if len(L) == 1]
        if not pending:
            if n == self.n and all(self.used(t) == self.q[t] for t in range(4)):
                self.found.append(tuple(sorted(self.words)))
            return
        if n >= self.n or not self.bounds_ok():
            return
        best = None
        for key in sorted(pending):
            c = self.candidates(key)
            if best is None or len(c) < len(best):
                best = c
                if len(c) <= 1:
                    break
        for v in best:
            self.add(v)
            self.rec()
            self.remove(v)

    def run(self):
        self.add((0, 0, 0, 0))
        self.rec()
        return self.found


# ---------------------------------------------------------------------------
# Relabeling classes (structure-only labeled growth; exact isomorphism test)
# ---------------------------------------------------------------------------

def normalize(S):
    sizes = [len({w[t] for w in S}) for t in range(4)]
    order = sorted(range(4), key=lambda t: (sizes[t], t))
    return [tuple(w[t] for t in order) for w in S], tuple(sizes[t] for t in order)


def size_preserving_perms(sizes):
    return [s for s in itertools.permutations(range(4))
            if all(sizes[s[t]] == sizes[t] for t in range(4))]


def relabel_run(S, sigma, base):
    """Deterministic relabeling of S: parties reordered by sigma, base word -> 0000, then
    repeatedly add the pair mate completing the lexicographically least pending labeled
    pair value; new symbols get the next free label per party."""
    W = [tuple(w[sigma[t]] for t in range(4)) for w in S]
    b = tuple(base[sigma[t]] for t in range(4))
    group = {}
    for w in W:
        for p in range(6):
            i, j = PAIRS[p]
            group.setdefault((p, w[i], w[j]), []).append(w)
    lab = [dict() for _ in range(4)]
    out, cnt, keyword = [], {}, {}

    def addw(w):
        for t in range(4):
            if w[t] not in lab[t]:
                lab[t][w[t]] = len(lab[t])
        lw = tuple(lab[t][w[t]] for t in range(4))
        out.append(lw)
        for p in range(6):
            i, j = PAIRS[p]
            k = (p, lw[i], lw[j])
            cnt[k] = cnt.get(k, 0) + 1
            keyword[k] = w

    addw(b)
    while len(out) < len(W):
        pend = [k for k, c in cnt.items() if c == 1]
        if not pend:
            return None
        k = min(pend)
        w = keyword[k]
        i, j = PAIRS[k[0]]
        g = group[(k[0], w[i], w[j])]
        if len(g) != 2:
            return None
        addw(g[1] if g[0] == w else g[0])
    return tuple(sorted(out))


def all_outputs(S, sizes):
    return {relabel_run(S, s, b) for s in size_preserving_perms(sizes) for b in S}


def classify(raw, sizes):
    classes = []
    for S in raw:
        check_time()
        S = list(S)
        x = relabel_run(S, (0, 1, 2, 3), S[0])
        for C in classes:
            if x in C["outputs"]:
                C["raw_hits"] += 1
                break
        else:
            outs = all_outputs(S, sizes)
            classes.append({"rep": S, "outputs": outs, "canon": min(outs), "raw_hits": 1})
    return classes


def relabel_invariance_ok(C, sizes):
    """Apply a fixed nontrivial relabeling (last size-preserving party permutation and
    reversal of every used alphabet) and require the same canonical form."""
    sigma = size_preserving_perms(sizes)[-1]
    al = alphabets(C["rep"])
    flip = [{x: a[len(a) - 1 - n] for n, x in enumerate(a)} for a in al]
    G = [tuple(flip[sigma[t]][w[sigma[t]]] for t in range(4)) for w in C["rep"]]
    return min(all_outputs(G, sizes)) == C["canon"]


def wstr(w):
    return "".join(str(x) for x in w)


def describe_class(C, sizes, n, profile):
    S = C["rep"]
    nperm = len(size_preserving_perms(sizes))
    reason = structural_reason(S, profile, n)
    box, boxarg = max_binary_box(S)
    deg = degrees(S)
    phase, sq = phase_of_component(S) if reason is None else ({"verdict": "NOT_EVALUATED"}, [])
    canon = list(C["canon"])
    return {
        "canonical_words": [wstr(w) for w in canon],
        "raw_labeled_hits": C["raw_hits"],
        "automorphisms": Fraction(nperm * n, len(C["outputs"])).__str__(),
        "independent_structural_reason": reason,
        "degree_multisets": [sorted(d.values()) for d in deg] if deg else None,
        "max_binary_box": box,
        "binary_box_argmax": [list(a) for a in boxarg] if boxarg else None,
        "binary_box_ok": box <= 7,
        "relabel_invariance_ok": relabel_invariance_ok(C, sizes),
        "phase": phase,
        "squares": [[nm, [wstr(x) for x in abcd]] for (nm, abcd, _) in sq],
    }


def run_profile(q, n):
    s = ComponentSearch(q, n)
    raw = s.run()
    classes = classify(raw, tuple(q))
    rep = {"profile": "".join(map(str, q)), "n": n, "search_nodes": s.nodes,
           "raw_labeled_solutions": len(raw),
           "raw_failing_independent_validator": sum(
               1 for S in raw if structural_reason(list(S), q, n) is not None),
           "classes": []}
    for C in classes:
        check_time()
        rep["classes"].append(describe_class(C, tuple(q), n, q))
    rep["n_classes"] = len(classes)
    rep["n_classes_box_le_7"] = sum(1 for c in rep["classes"] if c["binary_box_ok"])
    rep["n_classes_box_le_7_and_even"] = sum(
        1 for c in rep["classes"]
        if c["binary_box_ok"] and c["phase"].get("verdict") == "EVEN_PHASES_EXIST")
    return rep, classes


# ---------------------------------------------------------------------------
# Literal controls and intended-reason mutants
# ---------------------------------------------------------------------------

EVEN8 = [w for w in itertools.product((0, 1), repeat=4) if sum(w) % 2 == 0]
CYCLE8 = [(k % 2, k // 2, k % 2, k // 2) for k in range(4)] + \
         [(k % 2, k // 2, (k + 1) % 4 % 2, (k + 1) % 4 // 2) for k in range(4)]
GADGET12 = [(i, i, i, d) for i in range(3) for d in (0, 1)] + \
           [(i, (i - 1) % 3, (i + 1) % 3, d) for i in range(3) for d in (0, 1)]
PRISM12 = [t + (d,) for t in ((0, 2, 0), (0, 0, 2), (2, 0, 0), (1, 2, 1), (1, 1, 2), (2, 1, 1))
           for d in (0, 1)]
S7_ROWS = [[1, 1, -1, -1, 0, 0], [1, -1, 0, 0, 1, -1], [0, 0, 1, -1, -1, 1]]
# Fresh written 16-word examples over parties (A,B,C,D), D binary (sorted profile 2444):
# BIP16: triple graph is the bipartite L/R graph L_i=(i,i,i), R_i=(i,i+1,i+2) mod 4 -> EVEN;
# TRI16: triple graph contains the triangle (000,011,110) -> ODD.  Neither is an E28/P22 object.
BIP16 = [(i, i, i, d) for i in range(4) for d in (0, 1)] + \
        [(i, (i + 1) % 4, (i + 2) % 4, d) for i in range(4) for d in (0, 1)]
TRI16 = [t + (d,) for t in ((0, 0, 0), (0, 1, 1), (1, 1, 0), (1, 2, 2),
                            (2, 0, 3), (2, 3, 1), (3, 2, 3), (3, 3, 2)) for d in (0, 1)]


def n16_controls(cls):
    """Engine completeness controls at N=16: both written 2444 examples must be found."""
    out = []
    sizes = (2, 4, 4, 4)
    canons = [C["canon"] for C in cls]
    for name, words, verdict in (("E3 bipartite 2444 example found, box<=7, EVEN", BIP16, "EVEN_PHASES_EXIST"),
                                 ("E4 triangle 2444 example found, box<=7, ODD", TRI16,
                                  "ODD_INTEGRAL_DEPENDENCY")):
        g = normalize(words)[0]
        obs = [structural_reason(g, sizes, 16), max_binary_box(g)[0] <= 7,
               phase_of_component(g)[0]["verdict"], min(all_outputs(g, sizes)) in canons]
        exp = [None, True, verdict, True]
        out.append({"control": name, "expected": exp, "observed": obs, "pass": exp == obs})
    return out


def run_controls():
    res = []

    def ctl(name, expected, observed):
        res.append({"control": name, "expected": expected, "observed": observed,
                    "pass": expected == observed})

    ctl("M1 cut 8-cycle AB|CD is not a K2,2 union", False, cut_is_k22_union(CYCLE8, 0, 5))
    ctl("M1+ even-8 cuts are K2,2 unions", [True, True, True],
        [cut_is_k22_union(EVEN8, p1, p2) for (p1, p2) in CUTS])
    ctl("M2 even-8 minus one word fails pair extensions", False, pair_extensions_ok(EVEN8[1:]))
    ctl("M3 even-8 passes (a)(b)(c) structurally", None, structural_reason(EVEN8, (2, 2, 2, 2), 8))
    ctl("M3 even-8 binary box maximum is 8 (>7)", 8, max_binary_box(EVEN8)[0])
    ph8, _ = phase_of_component(EVEN8)
    ctl("M4 even-8 integral verdict", "ODD_INTEGRAL_DEPENDENCY", ph8["verdict"])
    ph7 = phase_evaluate(S7_ROWS, 6)
    ctl("M5 S7 formal rows integral verdict", "EVEN_PHASES_EXIST", ph7["verdict"])
    ctl("M5 S7 formal rows sign-only MUTANT verdict", False, sign_only_solvable(S7_ROWS, 6))
    g = normalize(GADGET12)[0]
    pr = normalize(PRISM12)[0]
    ctl("M6 canonical 2333 gadget structural", None, structural_reason(g, (2, 3, 3, 3), 12))
    ctl("M6 canonical gadget box <= 7", True, max_binary_box(g)[0] <= 7)
    ctl("M6 canonical gadget phase", "EVEN_PHASES_EXIST", phase_of_component(g)[0]["verdict"])
    ctl("M7 triangular prism structural", None, structural_reason(pr, (2, 3, 3, 3), 12))
    ctl("M7 triangular prism box <= 7", True, max_binary_box(pr)[0] <= 7)
    ctl("M7 triangular prism phase", "ODD_INTEGRAL_DEPENDENCY", phase_of_component(pr)[0]["verdict"])
    copy = [(a + 3, b + 3, c + 3, d + 2) for (a, b, c, d) in GADGET12]
    ctl("M8 two disjoint gadgets are disconnected", "DISCONNECTED",
        structural_reason(GADGET12 + copy, (4, 6, 6, 6), 24))
    ctl("M9 gadget against profile 3333", "PROFILE", structural_reason(GADGET12, (3, 3, 3, 3), 12))
    # engine controls at N=12 (adopted S5: every 12-word component is the 2333 gadget)
    e3333, _ = run_profile((3, 3, 3, 3), 12)
    ctl("E1 engine N=12 profile 3333 classes", 0, e3333["n_classes"])
    e2333, cls = run_profile((2, 3, 3, 3), 12)
    sizes = (2, 3, 3, 3)
    gcanon = min(all_outputs(g, sizes))
    pcanon = min(all_outputs(pr, sizes))
    canons = [C["canon"] for C in cls]
    even = [C["canon"] for C, d in zip(cls, e2333["classes"])
            if d["phase"].get("verdict") == "EVEN_PHASES_EXIST"]
    ctl("E2 engine N=12 2333 finds gadget", True, gcanon in canons)
    ctl("E2 engine N=12 2333 finds prism", True, pcanon in canons)
    ctl("E2 engine N=12 2333 phase-feasible classes are exactly the gadget", [gcanon], even)
    ctl("E2 engine N=12 raw solutions pass independent validator", 0,
        e2333["raw_failing_independent_validator"])
    summary = {"n12_3333": {k: e3333[k] for k in ("search_nodes", "raw_labeled_solutions", "n_classes")},
               "n12_2333": {k: e2333[k] for k in ("search_nodes", "raw_labeled_solutions", "n_classes",
                                                   "n_classes_box_le_7_and_even")},
               "even8_certificate_y": ph8.get("certificate_y"),
               "s7_theta": ph7.get("certificate_theta")}
    return res, summary


def main():
    report = {"source": "f893 finite-sixteen-component-v1.py", "limit_s": LIMIT_S,
              "scope": "LOCAL connected 16-word E components only; not P22, not AME, not global"}
    status, code = "COMPLETE_LOCAL", 0
    try:
        controls, summary = run_controls()
        report["controls"] = controls
        report["control_summary"] = summary
        if not all(c["pass"] for c in controls):
            status, code = "CONTROL_FAIL", 3
        profiles = []
        report["profiles"] = profiles
        for q in TARGET_PROFILES:
            report["in_progress_profile"] = "".join(map(str, q))
            rep, cls = run_profile(q, TARGET_N)
            profiles.append(rep)
            if q == (2, 4, 4, 4):
                for c in n16_controls(cls):
                    controls.append(c)
                    if not c["pass"] and code == 0:
                        status, code = "CONTROL_FAIL", 3
            for c in rep["classes"]:
                bad = (c["independent_structural_reason"] is not None or not c["relabel_invariance_ok"]
                       or c["phase"].get("verdict") == "INTERNAL_ERROR")
                if bad and code == 0:
                    status, code = "INTERNAL_INCONSISTENCY", 4
            if rep["raw_failing_independent_validator"] and code == 0:
                status, code = "INTERNAL_INCONSISTENCY", 4
        report["in_progress_profile"] = None
    except Timeout:
        status, code = "INCOMPLETE", 2
    report["status"] = status
    report["elapsed_s"] = round(time.monotonic() - _T0, 6)
    print(json.dumps(report, indent=1, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main())
