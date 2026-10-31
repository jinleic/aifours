#!/usr/bin/env python3
"""Independent reviewer control (f141): exhaustive support-pattern enumeration for
square 0/1 patterns with every row/column degree >= 2 and exactly 2n+e nonzeros,
filtered by NECESSARY conditions for being the support of a complex unitary:
  F1 no two rows share exactly one column      (row orthogonality)
  F2 no two columns share exactly one row      (column orthogonality)
  F3 every connected support component is square (orthonormal rows AND columns)
  F4 algebraic 2x2 rules:
     R1 two rows with identical 2-element support => no other row touches those
        columns (their restrictions span C^2); symmetric for columns
     R2 two columns supported on exactly two rows => those rows have degree 2
        (the 2x2 submatrix is unitary and exhausts the row norms); symmetric
Rows are enumerated as a nondecreasing mask sequence (kills row permutations);
labeled counts are recovered by the multinomial multiplicity. Columns are labeled.
Written by the reviewer from the mathematical statements only; no author code
was read or executed.  Finite checks do NOT prove the all-n lemmas."""
import itertools, json, math, sys, time, hashlib, subprocess
from collections import Counter

def popcount(x): return bin(x).count("1")

def row_masks(n, dmin, dmax):
    out = []
    for d in range(dmin, dmax + 1):
        for cols in itertools.combinations(range(n), d):
            m = 0
            for c in cols: m |= 1 << c
            out.append(m)
    return sorted(out)

def enumerate_patterns(n, e, apply_F1_in_recursion=True):
    """Yield nondecreasing row-mask tuples with popcounts >=2 summing to 2n+e,
    pairwise overlap != 1 (if apply_F1_in_recursion)."""
    total = 2 * n + e
    masks = row_masks(n, 2, min(n, total - 2 * (n - 1)))
    res = []
    def rec(rows, start_idx, budget):
        k = len(rows)
        if k == n:
            if budget == 0: res.append(tuple(rows))
            return
        remaining_rows = n - k
        for idx in range(start_idx, len(masks)):
            m = masks[idx]
            pm = popcount(m)
            if pm > budget - 2 * (remaining_rows - 1): continue
            if apply_F1_in_recursion and any(popcount(m & r) == 1 for r in rows): continue
            rows.append(m); rec(rows, idx, budget - pm); rows.pop()
    rec([], 0, total)
    return res

def col_masks_of(rows, n):
    cols = [0] * n
    for i, r in enumerate(rows):
        for c in range(n):
            if r >> c & 1: cols[c] |= 1 << i
    return cols

def F1(rows): return all(popcount(a & b) != 1 for a, b in itertools.combinations(rows, 2))
def F2(cols): return all(popcount(a & b) != 1 for a, b in itertools.combinations(cols, 2))
def coldeg_ok(cols): return all(popcount(c) >= 2 for c in cols)

def components(rows, n):
    """Connected components of the bipartite support graph. Returns list of (rowset, colset, nnz)."""
    seen_r, comps = set(), []
    for r0 in range(n):
        if r0 in seen_r: continue
        R, C, stack = set(), set(), [("r", r0)]
        while stack:
            kind, v = stack.pop()
            if kind == "r":
                if v in R: continue
                R.add(v)
                for c in range(n):
                    if rows[v] >> c & 1: stack.append(("c", c))
            else:
                if v in C: continue
                C.add(v)
                for r in range(n):
                    if rows[r] >> v & 1: stack.append(("r", r))
        seen_r |= R
        nnz = sum(popcount(rows[r]) for r in R)
        comps.append((frozenset(R), frozenset(C), nnz))
    return comps

def F3(rows, n): return all(len(R) == len(C) for R, C, _ in components(rows, n))

def R1(vecs):
    """vecs: masks of one side (rows or columns), other side labeled by bits.
    If two vectors have identical 2-element support, no third vector may touch those positions."""
    cnt = Counter(v for v in vecs if popcount(v) == 2)
    for v, c in cnt.items():
        if c >= 2:
            if any((w & v) and w != v for w in vecs): return False
            if c >= 3: return False  # three orthonormal vectors in C^2
    return True

def R2(side, other, n):
    """side: masks (e.g. columns, bits=rows); if two of them have identical support of size 2
    (i.e. supported on exactly the same two 'other' indices), those two 'other' vectors must have degree 2."""
    for a, b in itertools.combinations(range(n), 2):
        if popcount(side[a]) == 2 and side[a] == side[b]:
            for t in range(n):
                if side[a] >> t & 1 and popcount(other[t]) != 2: return False
    return True

def F4(rows, cols, n):
    return R1(rows) and R1(cols) and R2(cols, rows, n) and R2(rows, cols, n)

def multiplicity(rows):
    m = math.factorial(len(rows))
    for c in Counter(rows).values(): m //= math.factorial(c)
    return m

def structure(rows, n):
    return tuple(sorted((len(R), nnz) for R, C, nnz in components(rows, n)))

def run_case(n, e):
    t0 = time.time()
    pats = enumerate_patterns(n, e)
    c = {"F1_rowseq": len(pats), "F1_labeled": sum(multiplicity(p) for p in pats)}
    s2, s3, s4 = [], [], []
    for p in pats:
        cols = col_masks_of(p, n)
        if not coldeg_ok(cols) or not F2(cols): continue
        s2.append(p)
        if not F3(p, n): continue
        s3.append(p)
        if not F4(p, cols, n): continue
        s4.append(p)
    c["F2_labeled"] = sum(multiplicity(p) for p in s2)
    c["F3_labeled"] = sum(multiplicity(p) for p in s3)
    c["F4_labeled"] = sum(multiplicity(p) for p in s4)
    c["F3_rowseq"] = len(s3); c["F4_rowseq"] = len(s4)
    c["F3_structures"] = sorted({str(structure(p, n)) for p in s3})
    c["F4_structures"] = sorted({str(structure(p, n)) for p in s4})
    c["seconds"] = round(time.time() - t0, 3)
    return c

def negative_controls():
    out = {}
    # (a) author-cited rectangular n=5 pattern: rows {0,1,2},{0,1,2},{3,4},{3,4},{3,4} = masks 7,7,24,24,24
    p = (7, 7, 24, 24, 24); n = 5; cols = col_masks_of(p, n)
    out["rect_2x3_plus_3x2_n5_e2"] = {"nnz": sum(map(popcount, p)), "F1": F1(p), "coldeg": coldeg_ok(cols),
                                      "F2": F2(cols), "F3": F3(p, n), "expected": "F3 False"}
    # (b) 6-cycle n=3 e=0: rows {0,1},{1,2},{0,2}
    p = (3, 6, 5); n = 3; cols = col_masks_of(p, n)
    out["six_cycle_n3_e0"] = {"nnz": sum(map(popcount, p)), "F1": F1(p), "expected": "F1 False"}
    # (c) algebraic-only rejection: n=4 e=4 rows {a,b},{a,b},{a,b,c,d},{a,b,c,d}
    p = (3, 3, 15, 15); n = 4; cols = col_masks_of(p, n)
    out["identical_pairs_touched_n4_e4"] = {"nnz": sum(map(popcount, p)), "F1": F1(p), "coldeg": coldeg_ok(cols),
                                            "F2": F2(cols), "F3": F3(p, n), "F4": F4(p, cols, n), "expected": "F1-F3 True, F4 False"}
    # (d) positive: full 3x3 (+) 2x2 (+) 2x2, n=7, e=3 : rows {0,1,2}x3, {3,4}x2, {5,6}x2
    p = (7, 7, 7, 24, 24, 96, 96); n = 7; cols = col_masks_of(p, n)
    out["pos_3full_2_2_n7_e3"] = {"nnz": sum(map(popcount, p)), "F1": F1(p), "coldeg": coldeg_ok(cols),
                                  "F2": F2(cols), "F3": F3(p, n), "F4": F4(p, cols, n), "expected": "all True"}
    # (e) positive: 3x3 with 8 nonzeros (+) 2x2, n=5, e=2: rows {0,1},{0,1,2},{0,1,2},{3,4},{3,4}
    p = (3, 7, 7, 24, 24); n = 5; cols = col_masks_of(p, n)
    out["pos_3eight_2_n5_e2"] = {"nnz": sum(map(popcount, p)), "F1": F1(p), "coldeg": coldeg_ok(cols),
                                 "F2": F2(cols), "F3": F3(p, n), "F4": F4(p, cols, n), "expected": "all True"}
    return out

def examined_two_excess_labeled(n):
    """Author-convention cross-check: labeled candidate counts for the two row-degree patterns of e=2."""
    one4 = n * math.comb(n, 4) * math.comb(n, 2) ** (n - 1) if n >= 4 else 0
    two3 = math.comb(n, 2) * math.comb(n, 3) ** 2 * math.comb(n, 2) ** (n - 2)
    return {"one_degree4": one4, "two_degree3": two3, "total": one4 + two3}

if __name__ == "__main__":
    cases = [(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),
             (3,2),(4,2),(5,2),(6,2),(7,2),(8,2),
             (3,3),(4,3),(5,3),(6,3),(7,3),(8,3),(9,3)]
    clock0 = subprocess.run(["/bin/date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()
    results = {}
    for n, e in cases:
        results[f"n{n}_e{e}"] = run_case(n, e)
        print(f"n={n} e={e}: {results[f'n{n}_e{e}']}", flush=True)
    neg = negative_controls()
    print("controls:", json.dumps(neg, indent=1))
    ex = {f"n{n}": examined_two_excess_labeled(n) for n in (3, 4, 5)}
    print("two-excess labeled candidate counts by formula:", ex)
    clock1 = subprocess.run(["/bin/date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()
    src = open(__file__, "rb").read()
    receipt = {"script": __file__.split("/")[-1], "script_sha256": hashlib.sha256(src).hexdigest(),
               "clock_start_utc": clock0, "clock_end_utc": clock1, "python": sys.version.split()[0],
               "cases": results, "intended_reason_controls": neg, "two_excess_candidate_formula": ex,
               "nonclaim": "Finite necessary-condition enumeration; does not prove the all-n unitary lemmas and does not test sufficiency."}
    out = __file__.replace(".py", "-receipt.json")
    with open(out, "w") as f: json.dump(receipt, f, indent=1)
    print("receipt", out)
