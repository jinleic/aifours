#!/usr/bin/env python3
"""Finite controls for proof-ROT-few-v2.md (not premises).

Part A2 (exhaustive over zero-sum-free multisets Y' of odd elements of Z_(2p)):
  LAYER : extras(Y') >= L - m  (hence m >= L - e, e = 2p-1-L)
  SET   : every zero-sum-free SET D has |A(D)| >= 2|D| (>= 2|D|+2 if |D| >= 3)
  MULTii: m >= max(2, e+1)  =>  g generator, Y' = g^m prod(d_j g), d_j odd >= 3, sum(d_j - 1) <= e
  MULTiii: 2p >= 3e+2  =>  m >= max(2, e+1)
  negative control NA: for each Y' and each odd x with -x in A(Y') (so Y'x is NOT zero-sum-free), test the LAYER
    inequality on Y'x; it must FAIL for some (the hypothesis matters and the test can fail).
Part S (Scherk, exhaustive over pairs of subsets of Z_n containing 0, n = 10, 12):
  positive: unique zero representation => |A+B| >= |A|+|B|-1 ; negative: without it, some pair violates the bound.
Part B2 (Steps 1-4 of Theorem ROT-FEW v2, exhaustive over (ZP) multisets of size R = 2p+2kappa-k, reduced by the unit
  group: the value 1 has maximal multiplicity, plus a separate pass where (1,0) is strictly most frequent):
  claim: a unique most frequent value g, a generator, multiplicity >= (4p-3k+1)/2, no (1,0), E_c <= k-1-|N_c|.
  negative control: the mutated bound E_c <= k-3-|N_c| must fail somewhere in scope.
  (p,k) = (13,5) and (17,7) in scope; (13,6) out of scope (fails (F2)), reported only.
Usage: check_rotfew_v2.py OUT.jsonl
"""
import itertools, json, sys, time

def rotl(mask, y, n, full):
    y %= n
    return ((mask << y) | (mask >> (n - y))) & full if y else mask

def pc(x):
    return bin(x).count("1")

def a_of(vals, n, full):
    A = 1
    for y in vals:
        A |= rotl(A, y, n, full)
    return A

def part_a2(p, out):
    n = 2 * p; full = (1 << n) - 1
    odd = [2 * t + 1 for t in range(p)]
    st = dict(part="A2", p=p, multisets=0, layer_fail=0, set_fail=0, multii_fail=0, multiii_fail=0,
              neg_tests=0, neg_layer_fail=0)
    for S in range(1, 1 << p):
        vals = [odd[t] for t in range(p) if S >> t & 1]
        A = 1; ok = True
        for y in vals:
            if (A >> ((n - y) % n)) & 1:
                ok = False; break
            A |= rotl(A, y, n, full)
        if ok:
            need = 2 * len(vals) + (2 if len(vals) >= 3 else 0)
            if pc(A) < need:
                st["set_fail"] += 1
                out.write(json.dumps(dict(p=p, kind="SET_FAIL", D=vals)) + "\n")
    mult = [0] * p
    def layer_ok(mv, A):
        L = sum(mv); m = max(mv)
        return pc(A) - 1 - L >= L - m
    def check(A):
        L = sum(mult)
        if L == 0:
            return
        st["multisets"] += 1
        e = n - 1 - L
        m = max(mult); gi = mult.index(m); g = odd[gi]
        if not layer_ok(mult, A):
            st["layer_fail"] += 1
            out.write(json.dumps(dict(p=p, kind="LAYER_FAIL", mult=mult)) + "\n")
        if m >= max(2, e + 1):
            good = g != p
            if good:
                ginv = pow(g, -1, n); tot = 0
                for t in range(p):
                    if t == gi or not mult[t]:
                        continue
                    r = (odd[t] * ginv) % n
                    good = good and r >= 3
                    tot += mult[t] * (r - 1)
                good = good and tot <= e
            if not good:
                st["multii_fail"] += 1
                out.write(json.dumps(dict(p=p, kind="MULTii_FAIL", mult=mult)) + "\n")
        if n >= 3 * e + 2 and not m >= max(2, e + 1):
            st["multiii_fail"] += 1
            out.write(json.dumps(dict(p=p, kind="MULTiii_FAIL", mult=mult)) + "\n")
        for t in range(p):  # negative control: one extra term creating a zero-sum
            x = odd[t]
            if (A >> ((n - x) % n)) & 1:
                st["neg_tests"] += 1
                mv = mult[:]; mv[t] += 1
                if not layer_ok(mv, A | rotl(A, x, n, full)):
                    st["neg_layer_fail"] += 1
    def dfs(t, A):
        if t == p:
            check(A); return
        dfs(t + 1, A)
        y = odd[t]; B = A; j = 0
        while not (B >> ((n - y) % n)) & 1:
            B |= rotl(B, y, n, full); j += 1; mult[t] = j
            dfs(t + 1, B)
        mult[t] = 0
    dfs(0, 1)
    return st

def part_s(n, out):
    full = (1 << n) - 1
    st = dict(part="S", n=n, pairs_unique=0, fail_unique=0, pairs_nonunique=0, viol_nonunique=0)
    subsets = [s for s in range(1 << n) if s & 1]
    for A in subsets:
        for B in subsets:
            sumset = 0; uniq = True
            for b in range(n):
                if B >> b & 1:
                    sumset |= rotl(A, b, n, full)
                    if b and (A >> ((n - b) % n)) & 1:
                        uniq = False
            bound = pc(A) + pc(B) - 1
            if uniq:
                st["pairs_unique"] += 1
                if pc(sumset) < min(bound, n) and pc(sumset) < bound:
                    st["fail_unique"] += 1
            else:
                st["pairs_nonunique"] += 1
                if pc(sumset) < bound:
                    st["viol_nonunique"] += 1
    return st

def part_b2(p, k, kappa, out, scope, special):
    n = 2 * p; full = (1 << n) - 1
    R = 2 * p + 2 * kappa - k
    lo = 2 * kappa + 2
    odd = [2 * t + 1 for t in range(p)]
    zt = (p - 1) // 2                       # index of (1,0) = residue p
    first = zt if special else 0            # type with maximal multiplicity
    order = [first] + [t for t in range(p) if t != first]
    st = dict(part="B2", p=p, k=k, kappa=kappa, R=R, scope=scope, pass_="(1,0)-max" if special else "1-max",
              found=0, fail=0, mut_fail=0, nodes=0)
    mult = [0] * p
    gbound = (4 * p - 3 * k + 1) / 2
    def evaluate():
        st["found"] += 1
        m = max(mult); idx = [t for t in range(p) if mult[t] == m]
        bad = []
        if len(idx) != 1:
            bad.append("tie")
        gi = idx[0]; g = odd[gi]
        if g == p:
            bad.append("g=(1,0)")
        if m < gbound:
            bad.append("G<bound")
        if mult[zt]:
            bad.append("rho0")
        E = Nn = None
        if g != p:
            ginv = pow(g, -1, n); E = 0; Nn = 0
            for t in range(p):
                if not mult[t]:
                    continue
                r = (odd[t] * ginv) % n
                if r == p:
                    E += mult[t] * (p - 1); continue
                b = r if r < p else r - n
                E += mult[t] * (abs(b) - 1)
                if b < 0:
                    Nn += mult[t]
            if E > k - 1 - Nn:
                bad.append("E>k-1-N")
            if E > k - 3 - Nn:
                st["mut_fail"] += 1
        if bad:
            st["fail"] += 1
            if st["fail"] <= 20:
                out.write(json.dumps(dict(p=p, k=k, kappa=kappa, kind="B2_FAIL", scope=scope, why=bad,
                                          mult={odd[t]: mult[t] for t in range(p) if mult[t]}, E=E, N=Nn)) + "\n")
    def add(reach, y):
        nxt = reach[:]
        for l in range(n, 0, -1):
            nxt[l] |= rotl(reach[l - 1], y, n, full)
        for l in range(lo, n + 1):
            if nxt[l] & 1:
                return None
        return nxt
    def dfs(pos, reach, size, cap):
        st["nodes"] += 1
        if size == R:
            evaluate(); return
        if pos == p or size + (p - pos) * cap < R:
            return
        t = order[pos]
        dfs(pos + 1, reach, size, cap)
        cur = reach; j = 0
        lim = cap if not special else cap - 1   # special pass: others strictly below the (1,0) multiplicity
        while j < lim and size + j < R:
            cur = add(cur, odd[t])
            if cur is None:
                break
            j += 1; mult[t] = j
            dfs(pos + 1, cur, size + j, cap)
        mult[t] = 0
    reach0 = [0] * (n + 1); reach0[0] = 1
    # choose the multiplicity of the first type, then recurse with cap = that multiplicity
    cur = reach0; j = 0
    t0 = order[0]
    seq = []
    while j < R:
        cur = add(cur, odd[t0])
        if cur is None:
            break
        j += 1; seq.append((j, cur))
    for j, reach in seq:
        mult[t0] = j
        dfs(1, reach, j, j)
    mult[t0] = 0
    return st

def main():
    with open(sys.argv[1], "x") as out:
        def emit(s, t0):
            s["sec"] = round(time.time() - t0, 1)
            out.write(json.dumps(s) + "\n"); out.flush(); print(s, flush=True)
        for n in (8, 10):
            t0 = time.time(); emit(part_s(n, out), t0)
        for p in (7, 11, 13, 17):
            t0 = time.time(); emit(part_a2(p, out), t0)
        for (p, k, scope) in ((13, 5, "in"), (13, 6, "out"), (17, 7, "in")):
            for kappa in range(0, k):
                for special in (False, True):
                    t0 = time.time(); emit(part_b2(p, k, kappa, out, scope, special), t0)

if __name__ == "__main__":
    main()
