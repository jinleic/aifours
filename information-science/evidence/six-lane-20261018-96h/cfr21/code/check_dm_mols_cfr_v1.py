#!/usr/bin/env python3
"""check_dm_mols_cfr_v1.py — checker A (ContinueCFR21; written from definitions only; stdlib only).
Usage: check_dm_mols_cfr_v1.py <raw_file> <n> <k>
<raw_file>: exactly k non-empty lines, each with exactly n integers in [0, n) separated by whitespace: the rows
D_0..D_{k-1} of a candidate (Z_n,k;1) difference matrix (columns indexed 0..n-1; no normalisation assumed).
Checks, each from its own definition:
 (1) DM: for every pair of rows i<j the n values (D_i(c) - D_j(c)) mod n are pairwise distinct.
 (2) MOLS: the k-1 arrays L_t(c,g) = (D_t(c) - D_0(c) + g) mod n, t=1..k-1, c,g in Z_n, are each Latin
     (every row and column a permutation of Z_n) and pairwise orthogonal (all n^2 ordered pairs distinct).
 (3) CFR (CPro1 circular-florentine-rectangle predicate, re-implemented): rows t=1..k-1 with
     arr_t[p] = the unique symbol s with (D_t(s) - D_0(s)) mod n = p; every row a permutation of the n symbols and,
     for every m in 1..n-1, symbols a != b, at most one row has b exactly m steps (cyclically) to the right of a.
Prints one JSON object; exit code 0 iff all three verdicts are PASS (exit 1 otherwise, 2 on malformed input)."""
import sys, json, hashlib
def main():
    path, n, k = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    raw = open(path, 'rb').read()
    out = {"input": path, "input_sha256": hashlib.sha256(raw).hexdigest(), "n": n, "k": k}
    try:
        lines = [ln for ln in raw.decode('ascii').splitlines() if ln.strip()]
        D = [[int(t) for t in ln.split()] for ln in lines]
    except Exception as e:
        out["malformed"] = repr(e); print(json.dumps(out)); return 2
    if len(D) != k or any(len(r) != n for r in D) or any(not (0 <= x < n) for r in D for x in r):
        out["malformed"] = "shape or range"; print(json.dumps(out)); return 2
    # (1) DM
    bad = []
    for i in range(k):
        for j in range(i + 1, k):
            if len({(D[i][c] - D[j][c]) % n for c in range(n)}) != n: bad.append([i, j])
    out["dm_verdict"] = "PASS" if not bad else "FAIL"; out["dm_bad_pairs"] = bad[:20]; out["dm_bad_pair_count"] = len(bad)
    # (2) MOLS
    squares = []
    for t in range(1, k):
        squares.append([[(D[t][c] - D[0][c] + g) % n for g in range(n)] for c in range(n)])
    latin_bad = []
    full = set(range(n))
    for t, L in enumerate(squares, start=1):
        rows_ok = all(set(L[c]) == full for c in range(n))
        cols_ok = all({L[c][g] for c in range(n)} == full for g in range(n))
        if not (rows_ok and cols_ok): latin_bad.append(t)
    orth_bad = []
    for a in range(len(squares)):
        for b in range(a + 1, len(squares)):
            La, Lb = squares[a], squares[b]
            if len({(La[c][g], Lb[c][g]) for c in range(n) for g in range(n)}) != n * n: orth_bad.append([a + 1, b + 1])
    out["mols_count"] = len(squares)
    out["mols_verdict"] = "PASS" if (not latin_bad and not orth_bad) else "FAIL"
    out["mols_nonlatin"] = latin_bad[:20]; out["mols_nonorthogonal_pairs"] = orth_bad[:20]
    # (3) CFR
    arrs = []; cfr_ok = True
    for t in range(1, k):
        tau = [(D[t][s] - D[0][s]) % n for s in range(n)]
        if len(set(tau)) != n: cfr_ok = False; arrs.append(None); continue
        arr = [0] * n
        for s in range(n): arr[tau[s]] = s
        arrs.append(arr)
    collisions = 0
    if cfr_ok:
        seen = set()
        for arr in arrs:
            for m in range(1, n):
                for p in range(n):
                    key = (m, arr[p], arr[(p + m) % n])
                    if key in seen: collisions += 1
                    else: seen.add(key)
        cfr_ok = collisions == 0
        out["cfr_events_total"] = len(seen) + collisions
    out["cfr_rows"] = k - 1; out["cfr_verdict"] = "PASS" if cfr_ok else "FAIL"; out["cfr_collisions"] = collisions
    out["overall"] = "PASS" if (out["dm_verdict"] == out["mols_verdict"] == out["cfr_verdict"] == "PASS") else "FAIL"
    if out["overall"] == "PASS":
        out["cfr_rows_sha256"] = hashlib.sha256(json.dumps(arrs).encode()).hexdigest()
    print(json.dumps(out, sort_keys=True))
    return 0 if out["overall"] == "PASS" else 1
if __name__ == '__main__':
    sys.exit(main())
