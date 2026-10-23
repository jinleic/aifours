#!/usr/bin/env python3
"""phase_check.py: exact structural and phase checks for a support pattern (lane ame46-support).

Given a pattern (T, N) of 4-tuples over [6]:
  components(S, reshaping) -> connected components of the bipartite support graph;
  analyse(T, N) -> per reshaping the component sizes and entry counts, e = s - (72 - t), and the 2x2-block phase
  system  phi_rc - phi_rc' - phi_r'c + phi_r'c' == pi (mod 2 pi), written as A theta == 1/2 (mod 1), theta = phi/(2 pi).
  consistency over R/Z (complex phases): A theta == v (mod 1) is solvable iff every integer left-kernel vector n
  (n^T A = 0) has n.v in Z, i.e. sum(n) even (v = 1/2). We compute a unimodular U with U A = H (Hermite form by
  integer row operations); the rows of U at the zero rows of H form a Z-basis of the left kernel. If consistent, an
  explicit rational theta is produced by back substitution and verified exactly (A theta - v integral).
  consistency over F2 (real phases, theta in {0, 1/2}): Gaussian elimination mod 2.
Only 2x2 components contribute phase conditions here; larger components are reported, not analysed.
"""
import itertools
from fractions import Fraction as Fr

RESHAPINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def components(S, rows, cols):
    adj = {}
    for x in S:
        r = ("r", tuple(x[i] for i in rows))
        c = ("c", tuple(x[i] for i in cols))
        adj.setdefault(r, set()).add(c)
        adj.setdefault(c, set()).add(r)
    seen, comps = set(), []
    for v in adj:
        if v in seen:
            continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        rs = sorted(u[1] for u in comp if u[0] == "r")
        cs = sorted(u[1] for u in comp if u[0] == "c")
        elems = sorted(x for x in S if tuple(x[i] for i in rows) in rs)
        comps.append((rs, cs, elems))
    return comps


def block_equations(S):
    """List of (reshaping index, [(x, sign)]) for every 2x2 component with 4 entries."""
    eqs = []
    for k, (rows, cols) in enumerate(RESHAPINGS):
        for rs, cs, elems in components(S, rows, cols):
            if len(rs) == 2 and len(cs) == 2 and len(elems) == 4:
                (r1, r2), (c1, c2) = rs, cs

                def el(r, c):
                    x = [0] * 4
                    x[rows[0]], x[rows[1]] = r
                    x[cols[0]], x[cols[1]] = c
                    return tuple(x)
                eqs.append((k, [(el(r1, c1), 1), (el(r1, c2), -1), (el(r2, c1), -1), (el(r2, c2), 1)]))
    return eqs


def hermite_left_kernel(A):
    """A: list of integer rows. Returns (H, U) with U unimodular, U A = H in row echelon form."""
    m = len(A)
    n = len(A[0]) if m else 0
    H = [list(r) for r in A]
    U = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    piv_row = 0
    for col in range(n):
        if piv_row >= m:
            break
        while True:
            nz = [i for i in range(piv_row, m) if H[i][col] != 0]
            if not nz:
                break
            p = min(nz, key=lambda i: abs(H[i][col]))
            H[piv_row], H[p] = H[p], H[piv_row]
            U[piv_row], U[p] = U[p], U[piv_row]
            done = True
            for i in range(piv_row + 1, m):
                if H[i][col] != 0:
                    q = H[i][col] // H[piv_row][col]
                    if q:
                        H[i] = [a - q * b for a, b in zip(H[i], H[piv_row])]
                        U[i] = [a - q * b for a, b in zip(U[i], U[piv_row])]
                    if H[i][col] != 0:
                        done = False
            if done:
                break
        if any(H[i][col] != 0 for i in range(piv_row, m)):
            piv_row += 1
    return H, U, piv_row


def phase_consistency(eqs, elems):
    pos = {x: i for i, x in enumerate(elems)}
    A = []
    for _, terms in eqs:
        row = [0] * len(elems)
        for x, s in terms:
            row[pos[x]] += s
        A.append(row)
    if not A:
        return {"complex_consistent": True, "real_consistent": True, "n_eq": 0}
    H, U, rank = hermite_left_kernel(A)
    kernel = U[rank:]
    bad = [n for n in kernel if sum(n) % 2 != 0]
    res = {"n_eq": len(A), "n_var": len(elems), "rank": rank, "kernel_dim": len(kernel),
           "complex_consistent": not bad}
    if bad:
        n = min(bad, key=lambda v: sum(1 for a in v if a))
        res["obstruction"] = [(i, a) for i, a in enumerate(n) if a]
        chk = [sum(n[i] * A[i][j] for i in range(len(A))) for j in range(len(elems))]
        res["obstruction_verified"] = all(c == 0 for c in chk) and sum(n) % 2 == 1
    else:
        # explicit rational solution of H theta = U v (v = 1/2), free variables 0, verified on A theta - v in Z^m
        v = [Fr(1, 2)] * len(A)
        Uv = [sum(Fr(a) * b for a, b in zip(U[i], v)) for i in range(len(A))]
        theta = [Fr(0)] * len(elems)
        for i in reversed(range(rank)):
            pc = next(j for j in range(len(elems)) if H[i][j] != 0)
            sres = Uv[i] - sum(H[i][j] * theta[j] for j in range(pc + 1, len(elems)))
            theta[pc] = sres / H[i][pc]
        resid = [sum(A[i][j] * theta[j] for j in range(len(elems))) - v[i] for i in range(len(A))]
        res["theta_verified"] = all(r.denominator == 1 for r in resid)
        res["theta"] = {str(elems[j]): str(theta[j]) for j in range(len(elems)) if theta[j] != 0}
    # real phases: A t == 1 over F2
    M = [[a % 2 for a in row] + [1] for row in A]
    rr = 0
    ncol = len(elems)
    for col in range(ncol):
        p = next((i for i in range(rr, len(M)) if M[i][col]), None)
        if p is None:
            continue
        M[rr], M[p] = M[p], M[rr]
        for i in range(len(M)):
            if i != rr and M[i][col]:
                M[i] = [(a + b) % 2 for a, b in zip(M[i], M[rr])]
        rr += 1
    res["real_consistent"] = not any(all(a == 0 for a in row[:-1]) and row[-1] == 1 for row in M)
    return res


def analyse(T, N):
    T, N = set(T), set(N)
    S = T | N
    out = {"s": len(S), "t": len(T), "e": len(S) - (72 - len(T))}
    comp_info = {}
    for k, (rows, cols) in enumerate(RESHAPINGS):
        comps = components(S, rows, cols)
        comp_info[k] = sorted((len(rs), len(cs), len(el)) for rs, cs, el in comps)
    out["components"] = comp_info
    eqs = block_equations(S)
    elems = sorted({x for _, terms in eqs for x, _ in terms})
    out["phase"] = phase_consistency(eqs, elems)
    return out


if __name__ == "__main__":
    import json
    import pandya_control as pc
    W = pc.build()
    T = [x for x, v in W.items() if v == pc.R2]
    N = [x for x, v in W.items() if v != pc.R2]
    r = analyse(T, N)
    r["phase"].pop("theta", None)
    print(json.dumps(r, indent=1, default=str))
