#!/usr/bin/env python3.14
"""lift_route2: count mod-3 rainbow lifts of the mod-q skeleton of a (Z_n,k;1) DM.

Route 2 (independent): depth-first search over (row, column) cells of the
normalised lift array, with rainbow (all-different) fibre filtering and a sound
GF(3) fibre-sum propagator. Every counted leaf is re-checked against the
rainbow definition. See README.md.
"""
import argparse
import hashlib
import json
import os
import sys
import time

B57 = (1, 6, 7, 9, 19, 38, 42, 49)


def gf8_mul(a, b):
    r = 0
    for i in range(3):
        if (b >> i) & 1:
            r ^= a << i
    for i in (4, 3):
        if (r >> i) & 1:
            r ^= 0b1011 << (i - 3)
    return r


def singer57_rows():
    cols = []
    for u in range(8):
        for v in range(8):
            vals = [u ^ gf8_mul(a, v) for a in range(8)]
            if len(set(vals)) == 1:
                continue
            cols.append([B57[w] for w in vals])
    cols.append([0] * 8)
    return [[cols[c][a] for c in range(len(cols))] for a in range(8)]


class Bail(Exception):
    def __init__(self, status, code, msg):
        super().__init__(msg)
        self.status, self.code, self.msg = status, code, msg


def is_lift(A, fibres):
    """Direct definition: every fibre's 3 differences pairwise distinct mod 3."""
    for (x, y, cols) in fibres:
        ds = {(A[x][c] - A[y][c]) % 3 for c in cols}
        if len(ds) != 3:
            return False
    return True


def normalise(A, k, n):
    return [[(A[x][c] - A[x][0]) % 3 for c in range(n)] for x in range(k)]


def rep_sha(A):
    txt = "\n".join(" ".join(str(v) for v in row) for row in A)
    return hashlib.sha256(txt.encode("ascii")).hexdigest()


# ---------------------------------------------------------------- linear layer
# State: dict pivot -> [const, {free_var: coeff}], meaning pivot = const + sum.
# All pivots are absent from every row's free part (reduced form).

def lin_assign(rows, v, val):
    """Impose cell v = val. Returns False on contradiction. Mutates rows."""
    if v in rows:
        const, fr = rows.pop(v)
        if not fr:
            return const == val
        # sum a_f f = val - const ; solve for one free var
        fstar = min(fr)
        astar = fr.pop(fstar)
        inv = astar  # in GF(3), 1^-1 = 1, 2^-1 = 2
        # fstar = inv*(val - const) - inv*sum_{f != fstar} a_f f
        nconst = (inv * (val - const)) % 3
        nfr = {f: (-inv * a) % 3 for f, a in fr.items()}
        nfr = {f: a for f, a in nfr.items() if a}
        _subst(rows, fstar, nconst, nfr)
        rows[fstar] = [nconst, nfr]
        return True
    _subst(rows, v, val % 3, {})
    return True


def _subst(rows, f, c0, expr):
    """Replace free var f by c0 + expr in every row."""
    for p, row in rows.items():
        fr = row[1]
        a = fr.pop(f, 0)
        if a:
            row[0] = (row[0] + a * c0) % 3
            for g, b in expr.items():
                nb = (fr.get(g, 0) + a * b) % 3
                if nb:
                    fr[g] = nb
                else:
                    fr.pop(g, None)


def lin_add_equation(rows, eq):
    """Add homogeneous equation sum eq[v]*v = 0 (dict). False on contradiction."""
    const = 0
    fr = {}
    for v, a in eq.items():
        if v in rows:
            c, e = rows[v]
            const = (const + a * c) % 3
            for g, b in e.items():
                fr[g] = (fr.get(g, 0) + a * b) % 3
        else:
            fr[v] = (fr.get(v, 0) + a) % 3
    fr = {g: b for g, b in fr.items() if b}
    if not fr:
        return const == 0
    fstar = min(fr)
    astar = fr.pop(fstar)
    inv = astar
    nconst = (-inv * const) % 3
    nfr = {g: (-inv * b) % 3 for g, b in fr.items()}
    nfr = {g: b for g, b in nfr.items() if b}
    _subst(rows, fstar, nconst, nfr)
    rows[fstar] = [nconst, nfr]
    return True


def copy_rows(rows):
    return {p: [r[0], dict(r[1])] for p, r in rows.items()}


# ---------------------------------------------------------------- main solver

def solve(Bm, k, n, q, fibres, use_linear, deadline, out):
    # cell id = x*n + c ; row 0 and column 0 fixed to 0
    ncell = k * n
    fixed = [None] * ncell
    for c in range(n):
        fixed[0 * n + c] = 0
    for x in range(k):
        fixed[x * n] = 0
    # per-cell incident fibres: list of (fibre index, partner cell, sign)
    inc = [[] for _ in range(ncell)]
    for fi, (x, y, cols) in enumerate(fibres):
        for c in cols:
            inc[x * n + c].append((fi, y * n + c, 1))
            inc[y * n + c].append((fi, x * n + c, -1))
    stats = {"nodes": 0, "leaves": 0}
    found = []
    out["stats"] = stats
    out["found"] = found
    rows = {}
    if use_linear:
        for (x, y, cols) in fibres:
            if time.monotonic() > deadline:
                raise Bail("INCOMPLETE_BUDGET", 0, "budget")
            eq = {}
            for c in cols:
                for cell, s in ((x * n + c, 1), (y * n + c, -1)):
                    if fixed[cell] is None:
                        eq[cell] = (eq.get(cell, 0) + s) % 3
            eq = {v: a for v, a in eq.items() if a}
            if not lin_add_equation(rows, eq):
                return False  # impossible: T is a solution (self-test then fails)

    def fibre_ok(vals, fi):
        x, y, cols = fibres[fi]
        seen = 0
        for c in cols:
            a, b = vals[x * n + c], vals[y * n + c]
            if a is None or b is None:
                continue
            bit = 1 << ((a - b) % 3)
            if seen & bit:
                return False
            seen |= bit
        return True

    def assign(vals, rows, cell, v, touched):
        """Set cell=v and run linear forcing to fixpoint. Returns False on conflict."""
        stack = [(cell, v)]
        while stack:
            cl, val = stack.pop()
            cur = vals[cl]
            if cur is not None:
                if cur != val:
                    return False
                continue
            vals[cl] = val
            touched.append(cl)
            if use_linear:
                if not lin_assign(rows, cl, val):
                    return False
                for p, r in rows.items():
                    if not r[1] and vals[p] is None:
                        stack.append((p, r[0]))
        return True

    def domain(vals, cl):
        dom = 7
        for (fi, partner, s) in inc[cl]:
            pv = vals[partner]
            if pv is None:
                continue
            x, y, cols = fibres[fi]
            used = 0
            for c in cols:
                a, b = vals[x * n + c], vals[y * n + c]
                if a is None or b is None:
                    continue
                used |= 1 << ((a - b) % 3)
            for w in range(3):
                if dom >> w & 1:
                    d = (w - pv) % 3 if s == 1 else (pv - w) % 3
                    if used >> d & 1:
                        dom &= ~(1 << w)
        return dom

    def dfs(vals, rows):
        if time.monotonic() > deadline:
            raise Bail("INCOMPLETE_BUDGET", 0, "budget")
        stats["nodes"] += 1
        best = None
        bestcnt = 4
        for cl in range(ncell):
            if vals[cl] is not None:
                continue
            dm = domain(vals, cl)
            cnt = (dm & 1) + (dm >> 1 & 1) + (dm >> 2 & 1)
            if cnt < bestcnt:
                best, bestdom, bestcnt = cl, dm, cnt
                if cnt <= 1:
                    break
        if best is None:
            A = [[vals[x * n + c] for c in range(n)] for x in range(k)]
            stats["leaves"] += 1
            if not is_lift(A, fibres):
                raise Bail("INTERNAL_ERROR", 4, "leaf fails rainbow re-check")
            found.append(A)
            return
        if bestcnt == 0:
            return
        for w in range(3):
            if not (bestdom >> w & 1):
                continue
            nvals = list(vals)
            nrows = copy_rows(rows) if use_linear else rows
            touched = []
            if not assign(nvals, nrows, best, w, touched):
                continue
            ok = True
            seenf = set()
            for cl in touched:
                for (fi, _p, _s) in inc[cl]:
                    if fi not in seenf:
                        seenf.add(fi)
                        if not fibre_ok(nvals, fi):
                            ok = False
                            break
                if not ok:
                    break
            if ok:
                dfs(nvals, nrows)

    vals0 = list(fixed)
    ok0 = True
    if use_linear:
        # cells already determined by the fibre-sum system alone
        for p in [p for p, r in rows.items() if not r[1]]:
            if p in rows and vals0[p] is None:
                if not assign(vals0, rows, p, rows[p][0], []):
                    ok0 = False
                    break
    if ok0:
        for fi in range(len(fibres)):
            if not fibre_ok(vals0, fi):
                ok0 = False
                break
    if ok0:
        dfs(vals0, rows)
    return True


def main(argv):
    sys.setrecursionlimit(20000)
    t0 = time.monotonic()
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--raw")
    g.add_argument("--builtin", choices=["singer57"])
    ap.add_argument("--sha256")
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--rows")
    ap.add_argument("--budget-s", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-linear", action="store_true")
    a = ap.parse_args(argv)
    res = {"status": None, "n": a.n, "q": None, "k": None,
           "input_sha256": None, "fibres_all_size_3": None,
           "T_is_lift": None, "minusT_is_lift": None, "N_total": None,
           "N_classes": None, "classes": [], "nodes": 0, "wall_s": None,
           "linear_propagator": not a.no_linear, "rows_kept": None}
    code = 0
    if os.path.lexists(a.out):
        res["status"] = "BAD_INPUT"
        res["message"] = "--out already exists (exclusive create)"
        print(json.dumps(res, sort_keys=True))
        return 2
    try:
        code = run(a, res, t0)
    except Bail as e:
        res["status"] = e.status
        res["message"] = e.msg
        code = e.code
    res["wall_s"] = round(time.monotonic() - t0, 3)
    txt = json.dumps(res, sort_keys=True)
    with open(a.out, "x") as fh:
        fh.write(txt + "\n")
    print(txt)
    return code


def run(a, res, t0):
    n = a.n
    if n < 3 or n % 3 != 0 or (n // 3) % 3 == 0:
        raise Bail("BAD_INPUT", 2, "n must be 3q with gcd(3,q)=1")
    q = n // 3
    res["q"] = q
    if a.builtin:
        if a.sha256:
            raise Bail("BAD_INPUT", 2, "--sha256 not allowed with --builtin")
        Dm = singer57_rows()
        res["input_sha256"] = "builtin"
    else:
        if not a.sha256:
            raise Bail("BAD_INPUT", 2, "--sha256 required with --raw")
        try:
            with open(a.raw, "rb") as fh:
                data = fh.read()
        except OSError as e:
            raise Bail("BAD_INPUT", 2, "cannot read --raw: %s" % e)
        h = hashlib.sha256(data).hexdigest()
        res["input_sha256"] = h
        if h != a.sha256.lower():
            raise Bail("INPUT_PIN_MISMATCH", 2, "sha256 mismatch")
        try:
            Dm = [[int(t) for t in ln.split()] for ln in data.decode("ascii").splitlines() if ln.strip()]
        except ValueError:
            raise Bail("BAD_INPUT", 2, "non-integer token")
    if not Dm or any(len(r) != n for r in Dm):
        raise Bail("BAD_INPUT", 2, "each row must have n entries")
    if a.rows is not None:
        try:
            keep = [int(t) for t in a.rows.split(",")]
        except ValueError:
            raise Bail("BAD_INPUT", 2, "bad --rows")
        if len(set(keep)) != len(keep) or any(r < 0 or r >= len(Dm) for r in keep):
            raise Bail("BAD_INPUT", 2, "bad --rows")
        Dm = [Dm[r] for r in keep]
        res["rows_kept"] = keep
    k = len(Dm)
    res["k"] = k
    if k < 2:
        raise Bail("BAD_INPUT", 2, "need k >= 2")
    Dm = [[v % n for v in r] for r in Dm]
    for x in range(k):
        for y in range(x + 1, k):
            if len({(Dm[x][c] - Dm[y][c]) % n for c in range(n)}) != n:
                raise Bail("OLD_NOT_DM", 3, "rows %d,%d not a DM" % (x, y))
    E = [[(Dm[x][c] - Dm[0][c]) % n for c in range(n)] for x in range(k)]
    Bm = [[v % q for v in r] for r in E]
    T = [[v % 3 for v in r] for r in E]
    fibres = []
    allsz3 = True
    for x in range(k):
        for y in range(x + 1, k):
            buckets = [[] for _ in range(q)]
            for c in range(n):
                buckets[(Bm[x][c] - Bm[y][c]) % q].append(c)
            for t in range(q):
                if len(buckets[t]) != 3:
                    allsz3 = False
                fibres.append((x, y, tuple(buckets[t])))
    res["fibres_all_size_3"] = allsz3
    if not allsz3:
        raise Bail("BAD_INPUT", 2, "fibre size != 3")
    mT = [[(-v) % 3 for v in r] for r in T]
    res["T_is_lift"] = is_lift(T, fibres)
    res["minusT_is_lift"] = is_lift(mT, fibres)
    Tn = normalise(T, k, n)
    mTn = normalise(mT, k, n)
    out = {}
    deadline = t0 + a.budget_s
    status = "COMPLETE"
    try:
        solve(Bm, k, n, q, fibres, not a.no_linear, deadline, out)
    except Bail as e:
        if e.status != "INCOMPLETE_BUDGET":
            raise
        status = "INCOMPLETE_BUDGET"
    res["nodes"] = out["stats"]["nodes"] if "stats" in out else 0
    found = out.get("found", [])
    reps = []
    seen = set()
    for A in found:
        key = tuple(tuple(r) for r in A)
        if key in seen:
            raise Bail("INTERNAL_ERROR", 4, "duplicate leaf")
        seen.add(key)
        if A == Tn:
            eqs = "T"
        elif A == mTn:
            eqs = "-T"
        else:
            eqs = "other"
        reps.append({"equals": eqs, "rep_sha256": rep_sha(A)})
    reps.sort(key=lambda r: ({"T": 0, "-T": 1, "other": 2}[r["equals"]], r["rep_sha256"]))
    res["classes"] = reps
    if status == "COMPLETE":
        if not (any(r["equals"] == "T" for r in reps) and any(r["equals"] == "-T" for r in reps)):
            raise Bail("INTERNAL_ERROR", 4, "self-test: T or -T not found by search")
        res["N_classes"] = len(reps)
        res["N_total"] = len(reps) * 3 ** (k - 1)
    res["status"] = status
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
