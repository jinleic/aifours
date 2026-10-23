#!/usr/bin/env python3
"""Mod-q relaxation of the odd CFR(r,n) normal form (lane cfr33; notes/facts-v5.md L1).

Usage: oddmod_relax_cnf.py N Q R OUT_PREFIX [UNITS_JSON]
Half-columns a = 1..M (M = (N-1)/2). DM rows: 0 (zero), 1 (id: a mod Q), 2..R (unknown fbar_1..fbar_{R-1} in Z_Q).
Necessary condition (an odd CFR(R,N) reduced mod Q, Q | N, Q odd): for every pair of DM rows and every class
g in {0, 1, ..., (Q-1)/2}, the number of half-columns a with D(a) = r_i(a) - r_j(a) in {g, -g} (mod Q) equals
(N/Q - 1)/2 for g = 0 and N/Q otherwise.
Variables: one-hot Y(j,a,v); for unknown-unknown pairs one-hot DD(i,j,a,d) with table clauses; class indicators
Z = OR of two literals (full equivalence); exact cardinalities by a sequential counter with full equivalences.
UNITS_JSON (optional): list of [j, a, v] forcing fbar_j(a) = v.
Writes OUT_PREFIX.cnf and OUT_PREFIX.map.json (mode 'x').
"""
import hashlib, json, sys

N, Q, R, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
units = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else []
assert N % Q == 0 and Q % 2 == 1 and N % 2 == 1
M = (N - 1) // 2
J = list(range(1, R))                  # unknown rows fbar_1..fbar_{R-1} (DM rows 2..R)
nv = 0
def newv():
    global nv
    nv += 1
    return nv
clauses = []
def add(c):
    clauses.append(c)
Y = {(j, a, v): newv() for j in J for a in range(1, M + 1) for v in range(Q)}
for j in J:
    for a in range(1, M + 1):
        lits = [Y[j, a, v] for v in range(Q)]
        add(lits)
        for x in range(Q):
            for y in range(x + 1, Q):
                add([-lits[x], -lits[y]])
for (j, a, v) in units:
    add([Y[j, a, v % Q]])
DD = {}
for i in J:
    for j in J:
        if i < j:
            for a in range(1, M + 1):
                for d in range(Q):
                    DD[i, j, a, d] = newv()
                for u in range(Q):
                    for w in range(Q):
                        add([-Y[i, a, u], -Y[j, a, w], DD[i, j, a, (u - w) % Q]])
                lits = [DD[i, j, a, d] for d in range(Q)]
                for x in range(Q):
                    for y in range(x + 1, Q):
                        add([-lits[x], -lits[y]])
def lit_value(row, a, v):
    """literal (or True/False) for 'row value at half-column a equals v (mod Q)'; row 0 zero, row 1 id, row j+1 fbar_j"""
    if row == 0:
        return v % Q == 0
    if row == 1:
        return (a - v) % Q == 0
    return Y[row - 1, a, v % Q]
def diff_lit(ri, rj, a, d):
    d %= Q
    if ri >= 2 and rj >= 2:
        i, j = ri - 1, rj - 1
        if i < j:
            return DD[i, j, a, d]
        return DD[j, i, a, (-d) % Q]
    # at least one fixed row: D = r_i - r_j
    if ri <= 1 and rj <= 1:
        val = ((0 if ri == 0 else a) - (0 if rj == 0 else a)) % Q
        return val == d
    if ri <= 1:     # r_i fixed value c: c - r_j = d  <=> r_j = c - d
        c = 0 if ri == 0 else a
        return lit_value(rj, a, c - d)
    c = 0 if rj == 0 else a   # r_i - c = d <=> r_i = c + d
    return lit_value(ri, a, c + d)
def orlit(l1, l2):
    if l1 is True or l2 is True:
        return True
    ls = [l for l in (l1, l2) if l is not False]
    if not ls:
        return False
    if len(ls) == 1 or ls[0] == ls[-1]:
        return ls[0]
    z = newv()
    add([-z] + ls)
    for l in ls:
        add([z, -l])
    return z
def exactly(lits, k):
    """exact count via sequential counter with full equivalence; lits may contain True/False"""
    const = sum(1 for l in lits if l is True)
    xs = [l for l in lits if l not in (True, False)]
    k2 = k - const
    if k2 < 0 or k2 > len(xs):
        add([])   # infeasible
        return
    # S[i][c] for c = 1..k2+1
    prev = {c: False for c in range(1, k2 + 2)}
    prev[0] = True
    for x in xs:
        cur = {0: True}
        for c in range(1, k2 + 2):
            a_ = prev[c]; b_ = prev[c - 1]
            # cur[c] <-> a_ or (x and b_)
            s = newv()
            # s -> a_ or x ; s -> a_ or b_
            def L(v):
                return v
            terms_a = [] if a_ is False else ([] if a_ is True else [a_])
            if a_ is True:
                add([s]); cur[c] = s; continue
            if b_ is False:
                # s <-> a_
                if a_ is False:
                    add([-s])
                else:
                    add([-s, a_]); add([s, -a_])
                cur[c] = s
                continue
            if b_ is True:
                # s <-> a_ or x
                ls = ([a_] if a_ is not False else []) + [x]
                add([-s] + ls)
                for l in ls:
                    add([s, -l])
                cur[c] = s
                continue
            # general: s <-> a_ or (x and b_)
            add([-s] + ([a_] if a_ is not False else []) + [x])
            add([-s] + ([a_] if a_ is not False else []) + [b_])
            if a_ is not False:
                add([s, -a_])
            add([s, -x, -b_])
            cur[c] = s
        prev = cur
    top = prev[k2]; over = prev[k2 + 1]
    if top is not True:
        add([top] if top is not False else [])
    if over is True:
        add([])
    elif over is not False:
        add([-over])
rows = list(range(0, R + 1))
half = (Q - 1) // 2
for ri in rows:
    for rj in rows:
        if ri >= rj:
            continue
        for g in range(half + 1):
            lits = []
            for a in range(1, M + 1):
                if g == 0:
                    lits.append(diff_lit(ri, rj, a, 0))
                else:
                    lits.append(orlit(diff_lit(ri, rj, a, g), diff_lit(ri, rj, a, -g)))
            exactly(lits, (N // Q - 1) // 2 if g == 0 else N // Q)
text = "p cnf %d %d\n" % (nv, len(clauses)) + "".join(" ".join(map(str, c)) + " 0\n" for c in clauses)
with open(out + ".cnf", "x") as fh:
    fh.write(text)
info = {"N": N, "Q": Q, "R": R, "units": units, "cnf_sha256": hashlib.sha256(text.encode()).hexdigest(), "vars": nv,
        "clauses": len(clauses), "Y": [[j, a, v, Y[j, a, v]] for (j, a, v) in Y], "encoder": "oddmod_relax_cnf.py v1"}
with open(out + ".map.json", "x") as fh:
    json.dump(info, fh)
print(json.dumps({k: info[k] for k in ("cnf_sha256", "vars", "clauses")}))
