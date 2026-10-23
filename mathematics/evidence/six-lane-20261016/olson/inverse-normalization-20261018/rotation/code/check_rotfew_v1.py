#!/usr/bin/env python3
"""Finite controls for proof-ROT-few-v1.md (not premises).

Part A (Lemmas GROW, MULT; exhaustive over zero-sum-free multisets of odd elements of Z_(2p)):
  GROW : every zero-sum-free SET D of odd elements, d >= 3, |A(D)| <= 2p-2, has an x with drop >= 2.
  MULT (i)  : d >= 3  =>  d <= e - 1                       (e = 2p - 1 - L)
  MULT (ii) : m >= max(2, e+1) => g generator, Y' = g^m prod (d_j g), d_j odd >= 3, sum (d_j - 1) <= e
  MULT (iii): p >= 7 and 2p >= e^2 + 2  =>  m >= max(2, e+1)
  negative controls: mutated GROW' "EVERY x has drop >= 2" and MULT (i)' "d <= e - 2" must FAIL somewhere.
Part B (Steps 1-4 of Theorem ROT-FEW; exhaustive over multisets Y of odd elements of size R = 2p+2kappa-k with (ZP)):
  claim: the most frequent value g is unique, a generator, has multiplicity >= (4p-3k+1)/2, Y has no (1,0), and
         E_c <= k - 1 - |N_c| for c := g (SHgen weights).
  negative control: mutated bound E_c <= k - 3 - |N_c| must FAIL somewhere at an in-scope (p, k).
  out-of-scope report: (p, k) = (7, 5) (violates (F2), (F3)); violations there are reported, not expected either way.
Usage: check_rotfew_v1.py OUT.jsonl
"""
import json, sys, time

def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask

def popcount(x):
    return bin(x).count("1")

def part_a(p, out):
    n = 2 * p; full = (1 << n) - 1
    odd = [2 * t + 1 for t in range(p)]
    stats = dict(p=p, part="A", nodes=0, grow_sets=0, grow_fail=0, grow_every_fail=0,
                 multi_fail=0, multii_fail=0, multiii_fail=0, multi_mut_fail=0, maxL=0)
    # GROW over sets
    def A_of(vals):
        A = 1
        for y in vals:
            A |= rotl(A, y, n, full)
        return A
    for S in range(1, 1 << p):
        vals = [odd[t] for t in range(p) if S >> t & 1]
        A = 1; ok = True
        for y in vals:
            if (A >> ((n - y) % n)) & 1:
                ok = False; break
            A |= rotl(A, y, n, full)
        if not ok or len(vals) < 3:
            continue
        sz = popcount(A)
        if sz > n - 2:
            continue
        stats["grow_sets"] += 1
        drops = [sz - popcount(A_of([v for v in vals if v != x])) for x in vals]
        if max(drops) < 2:
            stats["grow_fail"] += 1
            out.write(json.dumps(dict(p=p, kind="GROW_FAIL", D=vals)) + "\n")
        if min(drops) < 2:
            stats["grow_every_fail"] += 1
    # MULT over zero-sum-free multisets (DFS over multiplicity vectors)
    mult = [0] * p
    def check(A):
        L = sum(mult)
        if L == 0:
            return
        stats["nodes"] += 1; stats["maxL"] = max(stats["maxL"], L)
        e = n - 1 - L
        d = sum(1 for x in mult if x)
        m = max(mult); gi = mult.index(m); g = odd[gi]
        if d >= 3 and not d <= e - 1:
            stats["multi_fail"] += 1
            out.write(json.dumps(dict(p=p, kind="MULTi_FAIL", mult=mult)) + "\n")
        if d >= 3 and not d <= e - 2:
            stats["multi_mut_fail"] += 1
        if m >= max(2, e + 1):
            good = g != p
            if good:
                ginv = pow(g, -1, n)
                tot = 0
                for t in range(p):
                    if t == gi or not mult[t]:
                        continue
                    r = (odd[t] * ginv) % n
                    if r < 3:
                        good = False
                    tot += mult[t] * (r - 1)
                good = good and tot <= e
            if not good:
                stats["multii_fail"] += 1
                out.write(json.dumps(dict(p=p, kind="MULTii_FAIL", mult=mult)) + "\n")
        if p >= 7 and n >= e * e + 2 and not m >= max(2, e + 1):
            stats["multiii_fail"] += 1
            out.write(json.dumps(dict(p=p, kind="MULTiii_FAIL", mult=mult)) + "\n")
    def dfs(t, A):
        if t == p:
            check(A); return
        dfs(t + 1, A)
        y = odd[t]; B = A; j = 0
        while True:
            if (B >> ((n - y) % n)) & 1:
                break
            B |= rotl(B, y, n, full); j += 1; mult[t] = j
            dfs(t + 1, B)
        mult[t] = 0
    dfs(0, 1)
    return stats

def part_b(p, k, kappa, out, scope):
    n = 2 * p; full = (1 << n) - 1
    R = 2 * p + 2 * kappa - k
    lo = 2 * kappa + 2
    zpmask = 0
    for l in range(lo, n + 1):
        zpmask |= 1 << l
    odd = [2 * t + 1 for t in range(p)]
    stats = dict(p=p, k=k, kappa=kappa, R=R, part="B", scope=scope, found=0, fail=0, mut_fail=0)
    mult = [0] * p
    gbound = (4 * p - 3 * k + 1) / 2
    def evaluate():
        stats["found"] += 1
        m = max(mult); idx = [t for t in range(p) if mult[t] == m]
        bad = []
        if len(idx) != 1:
            bad.append("tie")
        gi = idx[0]; g = odd[gi]
        if g == p:
            bad.append("g=(1,0)")
        if m < gbound:
            bad.append("G<bound")
        if mult[(p - 1) // 2]:  # residue p = (1,0)
            bad.append("rho0")
        E = None; Nn = None
        if g != p:
            ginv = pow(g, -1, n)
            E = 0; Nn = 0
            for t in range(p):
                if not mult[t]:
                    continue
                r = (odd[t] * ginv) % n          # element = r g, r odd in [1, 2p-1]
                if r == p:
                    E += mult[t] * (p - 1); continue
                b = r if r < p else r - n      # signed odd weight, |b| <= p-2
                E += mult[t] * (abs(b) - 1)
                if b < 0:
                    Nn += mult[t]
            if E > k - 1 - Nn:
                bad.append("E>k-1-N")
            if E > k - 3 - Nn:
                stats["mut_fail"] += 1
        if bad:
            stats["fail"] += 1
            if stats["fail"] <= 20:
                out.write(json.dumps(dict(p=p, k=k, kappa=kappa, kind="B_FAIL", scope=scope, why=bad,
                                          mult={odd[t]: mult[t] for t in range(p) if mult[t]}, E=E, N=Nn)) + "\n")
    def dfs(t, reach, size):
        # reach[l] = bitmask of sums of l-element sub-multisets (l <= n)
        if size == R:
            evaluate(); return
        if t == p:
            return
        dfs(t + 1, reach, size)
        y = odd[t]; cur = list(reach); j = 0
        while size + j < R:
            nxt = cur[:]
            for l in range(n, 0, -1):
                nxt[l] |= rotl(cur[l - 1], y, n, full)
            viol = False
            for l in range(lo, n + 1):
                if nxt[l] & 1:
                    viol = True; break
            if viol:
                break
            cur = nxt; j += 1; mult[t] = j
            dfs(t + 1, cur, size + j)
        mult[t] = 0
    reach0 = [0] * (n + 1); reach0[0] = 1
    dfs(0, reach0, 0)
    return stats

def main():
    outp = sys.argv[1]
    with open(outp, "x") as out:
        for p in (7, 11):
            t0 = time.time(); s = part_a(p, out); s["sec"] = round(time.time() - t0, 1)
            out.write(json.dumps(s) + "\n"); out.flush(); print(s, flush=True)
        for (p, k, scope) in ((7, 5, "out"), (11, 5, "in")):
            for kappa in range(0, k):
                t0 = time.time(); s = part_b(p, k, kappa, out, scope); s["sec"] = round(time.time() - t0, 1)
                out.write(json.dumps(s) + "\n"); out.flush(); print(s, flush=True)
        t0 = time.time(); s = part_a(13, out); s["sec"] = round(time.time() - t0, 1)
        out.write(json.dumps(s) + "\n"); out.flush(); print(s, flush=True)

if __name__ == "__main__":
    main()
