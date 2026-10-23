#!/usr/bin/env python3
"""Route-2 exhaustive search for one new G-equivariant row of a (Z_n,k;1)-DM.

Independent implementation written from the task definitions only; see
README.md for the definitions, the algorithm, the CLI and the exit codes.
Python 3.14 stdlib only; single process; no threads, subprocesses or network.

Usage:
  python3.14 -I -B ext_route2.py RAW SHA256 N GENS_JSON BUDGET_S OUT_DIR MAX_SOLUTIONS [--fix-zero-column]
"""

import hashlib
import json
import math
import os
import re
import sys
import time

FIX_ZERO_FLAG = "--fix-zero-column"
USAGE = ("usage: ext_route2.py RAW SHA256 N GENS_JSON BUDGET_S OUT_DIR "
         "MAX_SOLUTIONS [--fix-zero-column]")
MAX_WRITTEN = 20      # at most this many solution files are written
CHECK_EVERY = 4096    # the clock is read once every CHECK_EVERY search nodes
INT_TOKEN = re.compile(r"[+-]?[0-9]+")


def parse_int(text):
    token = text.strip()
    if not INT_TOKEN.fullmatch(token):
        raise ValueError(f"not an integer: {text!r}")
    return int(token)


def parse_matrix(data, n):
    """Rows of a raw file (k lines of n integers), entries reduced mod n."""
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise ValueError("raw file is not ASCII text") from None
    rows = []
    for lineno, line in enumerate(text.splitlines(), 1):
        tokens = line.split()
        if not tokens:
            continue
        if len(tokens) != n:
            raise ValueError(f"raw line {lineno} has {len(tokens)} entries, expected {n}")
        row = []
        for token in tokens:
            if not INT_TOKEN.fullmatch(token):
                raise ValueError(f"raw line {lineno}: bad entry {token!r}")
            row.append(int(token) % n)
        rows.append(row)
    if not rows:
        raise ValueError("raw file has no rows")
    return rows


def is_difference_matrix(rows, n):
    """Distinct columns and, for every pair of rows, n distinct differences mod n."""
    if any(len(row) != n for row in rows):
        return False
    if len(set(zip(*rows))) != n:
        return False
    for i in range(len(rows)):
        row_i = rows[i]
        for j in range(i + 1, len(rows)):
            row_j = rows[j]
            if len({(row_i[c] - row_j[c]) % n for c in range(n)}) != n:
                return False
    return True


def parse_generators(obj, n, k):
    """Validate the decoded GENS_JSON; return a list of (mu mod n, perm tuple)."""
    if not isinstance(obj, list):
        raise ValueError("GENS_JSON must be a JSON list of [mu, perm] pairs")
    gens = []
    for idx, item in enumerate(obj):
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError(f"generator {idx} is not a pair [mu, perm]")
        mu, perm = item
        if isinstance(mu, bool) or not isinstance(mu, int):
            raise ValueError(f"generator {idx}: mu is not an integer")
        if math.gcd(mu % n, n) != 1:
            raise ValueError(f"generator {idx}: mu={mu} is not a unit mod {n}")
        if not isinstance(perm, list) or len(perm) != k:
            raise ValueError(f"generator {idx}: perm is not a list of length {k}")
        if any(isinstance(x, bool) or not isinstance(x, int) for x in perm):
            raise ValueError(f"generator {idx}: perm has a non-integer entry")
        if sorted(perm) != list(range(k)):
            raise ValueError(f"generator {idx}: perm is not a permutation of 0..{k - 1}")
        gens.append((mu % n, tuple(perm)))
    return gens


def act(g, v, n):
    """g.v for g = (mu, perm): (g.v)[perm[x]] = mu * v[x] mod n."""
    mu, perm = g
    out = [0] * len(v)
    for x, value in enumerate(v):
        out[perm[x]] = (mu * value) % n
    return tuple(out)


def compose(a, b, n):
    """The element a*b, acting as v -> a.(b.v); multipliers multiply."""
    return ((a[0] * b[0]) % n, tuple(a[1][y] for y in b[1]))


def group_closure(gens, n, k):
    """All elements of G = <gens> as (mu, perm) pairs, BFS order, identity first."""
    identity = (1 % n, tuple(range(k)))
    elems = [identity]
    seen = {identity}
    head = 0
    while head < len(elems):
        h = elems[head]
        head += 1
        for g in gens:
            e = compose(g, h, n)
            if e not in seen:
                seen.add(e)
                elems.append(e)
    return elems


def orbit_data(elems, cols, col_index, n):
    """Orbits of G on the columns as (rep, members, mults, stab).

    rep is the smallest column index of the orbit, members its sorted column
    indices, mults[t] the multiplier of one g in G with g.col[rep] =
    col[members[t]] (the identity for rep itself), stab the sorted multipliers
    of the stabiliser of col[rep].
    """
    orbit_id = [-1] * len(cols)
    orbits = []
    for rep in range(len(cols)):
        if orbit_id[rep] != -1:
            continue
        r = cols[rep]
        mult_of = {}
        stab = set()
        for g in elems:
            image = col_index[act(g, r, n)]
            if image not in mult_of:
                mult_of[image] = g[0]
            if image == rep:
                stab.add(g[0])
        members = sorted(mult_of)
        for c in members:
            if orbit_id[c] != -1:
                raise RuntimeError("orbits overlap: group closure is inconsistent")
            orbit_id[c] = len(orbits)
        orbits.append((rep, members, [mult_of[c] for c in members], sorted(stab)))
    return orbits


def value_masks(rows, members, f_vals, n):
    """Per old row, the bitmask of (D[i][v] - f(v)) mod n over the orbit members.

    Returns None if two members give the same value in some row.
    """
    masks = []
    for row in rows:
        mask = 0
        for c, fv in zip(members, f_vals):
            bit = 1 << ((row[c] - fv) % n)
            if mask & bit:
                return None
            mask |= bit
        masks.append(mask)
    return tuple(masks)


def orbit_candidates(orbit, rows, n, force_zero):
    """Surviving (w, masks) pairs for one orbit, w increasing.

    w is admissible iff (mu_h - 1) * w = 0 mod n for every h in the stabiliser
    of the representative (only w = 0 when force_zero); it determines
    f(g.rep) = mu_g * w on the whole orbit.
    """
    rep, members, mults, stab = orbit
    if force_zero:
        values = [0]
    else:
        values = [w for w in range(n) if all(((m - 1) * w) % n == 0 for m in stab)]
    out = []
    for w in values:
        masks = value_masks(rows, members, [(m * w) % n for m in mults], n)
        if masks is not None:
            out.append((w, masks))
    return out


def search(cands, k, max_solutions, deadline):
    """Depth-first backtracking; cands[d] = surviving (w, masks) of the d-th orbit.

    used[i] is the bitmask of values already taken in old row i.  A node is a
    partial assignment (the root counts).  Returns (status, nodes, solutions,
    kept), kept = w-tuples of the first MAX_WRITTEN solutions in search order.
    """
    depth = len(cands)
    used = [0] * k
    nxt = [0] * depth    # next candidate index to try, per depth
    pick = [0] * depth   # candidate index currently placed, per depth
    nodes = 1
    solutions = 0
    kept = []
    d = 0
    while True:
        lst = cands[d]
        end = len(lst)
        i = nxt[d]
        while i < end:
            masks = lst[i][1]
            for u, m in zip(used, masks):
                if u & m:
                    break
            else:
                break  # candidate i is disjoint from used in every row
            i += 1
        if i == end:
            # depth d exhausted: backtrack and undo the placement at depth d - 1
            d -= 1
            if d < 0:
                return "COMPLETE", nodes, solutions, kept
            masks = cands[d][pick[d]][1]
            for r in range(k):
                used[r] ^= masks[r]
            continue
        nxt[d] = i + 1
        pick[d] = i
        nodes += 1
        if d == depth - 1:
            solutions += 1
            if len(kept) < MAX_WRITTEN:
                kept.append(tuple(cands[e][pick[e]][0] for e in range(depth)))
            if solutions >= max_solutions:
                return "STOPPED_AT_MAX_SOLUTIONS", nodes, solutions, kept
        else:
            for r in range(k):
                used[r] |= masks[r]
            d += 1
            nxt[d] = 0
        if nodes % CHECK_EVERY == 0 and time.monotonic() > deadline:
            return "INCOMPLETE_BUDGET", nodes, solutions, kept


def build_row(choice, order, orbits, n):
    """The new row f (indexed by column) for one solution's per-depth w values."""
    f = [0] * n
    for w, o in zip(choice, order):
        rep, members, mults, stab = orbits[o]
        for c, m in zip(members, mults):
            f[c] = (m * w) % n
    return f


def write_solutions(out_dir, rows, new_rows, n):
    """Exclusive-create one (k+1)-row raw file per solution; re-verify from disk."""
    os.makedirs(out_dir, exist_ok=False)
    written = []
    for j, f in enumerate(new_rows):
        path = os.path.abspath(os.path.join(out_dir, f"solution_{j:02d}.raw"))
        text = "".join(" ".join(map(str, row)) + "\n" for row in rows + [f])
        with open(path, "xb") as fh:
            fh.write(text.encode("ascii"))
        with open(path, "rb") as fh:
            back = fh.read()
        try:
            back_rows = parse_matrix(back, n)
            dm_ok = len(back_rows) == len(rows) + 1 and is_difference_matrix(back_rows, n)
        except ValueError:
            dm_ok = False
        written.append({
            "path": path,
            "sha256": hashlib.sha256(back).hexdigest(),
            "dm_ok": dm_ok,
            "constant": len(set(f)) == 1,
        })
    return written


def main(argv):
    t0 = time.monotonic()
    report = {
        "status": None,
        "input_sha256": None,
        "n": None,
        "k_old": None,
        "group_order": None,
        "orbit_sizes": None,
        "admissible_pairs": None,
        "solutions": None,
        "nodes": None,
        "written": [],
        "wall_s": None,
        "detail": None,
    }

    def finish(status, code, detail=None):
        report["status"] = status
        report["detail"] = detail
        report["wall_s"] = round(time.monotonic() - t0, 6)
        sys.stdout.write(json.dumps(report) + "\n")
        sys.stdout.flush()
        return code

    fix_zero = FIX_ZERO_FLAG in argv
    positional = [a for a in argv if a != FIX_ZERO_FLAG]
    if len(positional) != 7:
        return finish("BAD_INPUT", 2, USAGE)
    raw_path, pin, n_text, gens_text, budget_text, out_dir, max_text = positional
    try:
        n = parse_int(n_text)
        if n < 1:
            raise ValueError(f"N must be >= 1, got {n}")
        report["n"] = n
        budget = float(budget_text)
        if not (math.isfinite(budget) and budget >= 0):
            raise ValueError(f"BUDGET_S must be a finite number >= 0, got {budget_text!r}")
        max_solutions = parse_int(max_text)
        if max_solutions < 1:
            raise ValueError(f"MAX_SOLUTIONS must be >= 1, got {max_solutions}")
        gens_obj = json.loads(gens_text)
        if not out_dir:
            raise ValueError("OUT_DIR is empty")
        if os.path.lexists(out_dir):
            raise ValueError(f"OUT_DIR already exists: {out_dir}")
    except ValueError as exc:
        return finish("BAD_INPUT", 2, str(exc))

    try:
        with open(raw_path, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        return finish("BAD_INPUT", 2, f"cannot read RAW: {exc}")
    sha = hashlib.sha256(data).hexdigest()
    report["input_sha256"] = sha
    if sha != pin.strip().lower():
        return finish("INPUT_PIN_MISMATCH", 2, f"pinned sha256 {pin.strip().lower()}")

    try:
        rows = parse_matrix(data, n)
        report["k_old"] = len(rows)
        gens = parse_generators(gens_obj, n, len(rows))
    except ValueError as exc:
        return finish("BAD_INPUT", 2, str(exc))
    k = len(rows)

    if not is_difference_matrix(rows, n):
        return finish("OLD_NOT_DM", 3, "old rows are not a (Z_n,k;1)-DM with distinct columns")

    cols = list(zip(*rows))
    col_index = {col: c for c, col in enumerate(cols)}
    for idx, g in enumerate(gens):
        for c, col in enumerate(cols):
            if act(g, col, n) not in col_index:
                return finish("NOT_INVARIANT", 3,
                              f"generator {idx} maps column {c} outside the column set")

    zero_col = None
    if fix_zero:
        zero_col = col_index.get((0,) * k)
        if zero_col is None:
            return finish("NO_ZERO_COLUMN", 3, "no all-zero column")

    elems = group_closure(gens, n, k)
    report["group_order"] = len(elems)
    orbits = orbit_data(elems, cols, col_index, n)
    report["orbit_sizes"] = sorted(len(orbit[1]) for orbit in orbits)

    order = sorted(range(len(orbits)), key=lambda o: (-len(orbits[o][1]), orbits[o][0]))
    cands = [orbit_candidates(orbits[o], rows, n, orbits[o][0] == zero_col) for o in order]
    report["admissible_pairs"] = sum(len(c) for c in cands)

    status, nodes, solutions, kept = search(cands, k, max_solutions, t0 + budget)
    report["solutions"] = solutions
    report["nodes"] = nodes
    if kept:
        new_rows = [build_row(choice, order, orbits, n) for choice in kept]
        report["written"] = write_solutions(out_dir, rows, new_rows, n)
    return finish(status, 0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
