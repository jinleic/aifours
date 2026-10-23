"""Implementation B: four-party STATE picture, pure Python (stdlib only), modular + exact integer arithmetic.

State: psi(a,b,c,d) = P[(c,d),(a,b)] (source eq. C8, unnormalized 0/1). Cut S|S^c (S = 2 parties):
the reshaping M_S with rows = S-assignments is unitary iff rho_S = M_S M_S^dagger = 1. Linearization at psi:
    E_S(s,s') = sum_t [ psi(s,t) conj(dpsi(s',t)) + dpsi(s,t) conj(psi(s',t)) ] = 0   for all s, s'.
Unknowns: Re dpsi(y), Im dpsi(y), y in [d]^4 (index ord(y), then d^4 + ord(y)).
Cuts: unitarity = {0,1}|{2,3}; realignment R = {0,2}|{1,3}; partial transpose G = {0,3}|{1,2} (parties a,b,c,d).
Certificate: rank_Q(E) >= rank_p(E) (p prime) and kernel contains explicit exact integer vectors whose rank_p
gives a lower bound on their rank over Q; if both bounds meet, the kernel dimension is exact.
Also: involutions tau_S on [d]^4 defined combinatorially from the code; orbit structure; explicit kernel basis.

python -B implB_state_pure.py --out ../evidence/implB.json [--check-kernel-dir ../evidence/implA_kernels]
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import sys
import time

from perms import PERMS

PRIMES = (2305843009213693951, 1000000007)
CUTS = {"U": (0, 1), "R": (0, 2), "G": (0, 3)}


def points(d):
    return list(itertools.product(range(d), repeat=4))


def ordp(y, d):
    a, b, c, e = y
    return ((a * d + b) * d + c) * d + e


def psi_from_perm(d, ones):
    """psi(a,b,c,d) = P[(c,d),(a,b)]  (P|ab> = |cd>)."""
    psi = {}
    for r, col in ones:
        a, b = divmod(col, d)
        c, e = divmod(r, d)
        psi[(a, b, c, e)] = 1
    return psi


def split(y, S):
    Sc = tuple(q for q in range(4) if q not in S)
    return tuple(y[q] for q in S), tuple(y[q] for q in Sc), Sc


def join(s, t, S, Sc):
    y = [0] * 4
    for q, v in zip(S, s):
        y[q] = v
    for q, v in zip(Sc, t):
        y[q] = v
    return tuple(y)


def cut_equations(d, psi, S):
    """sparse integer rows {var: coeff} for Re and Im of E_S(s,s')."""
    Sc = tuple(q for q in range(4) if q not in S)
    N = d ** 4
    rows = []
    assign = list(itertools.product(range(d), repeat=2))
    for s in assign:
        for s2 in assign:
            re, im = {}, {}
            for t in assign:
                y1, y2 = join(s, t, S, Sc), join(s2, t, S, Sc)
                p1, p2 = psi.get(y1, 0), psi.get(y2, 0)
                # psi real: psi1 * conj(dpsi(y2)) + dpsi(y1) * psi2
                if p1:
                    re[ordp(y2, d)] = re.get(ordp(y2, d), 0) + p1
                    im[N + ordp(y2, d)] = im.get(N + ordp(y2, d), 0) - p1
                if p2:
                    re[ordp(y1, d)] = re.get(ordp(y1, d), 0) + p2
                    im[N + ordp(y1, d)] = im.get(N + ordp(y1, d), 0) + p2
            for r in (re, im):
                r = {k: v for k, v in r.items() if v}
                if r:
                    rows.append(r)
    return rows


def rank_mod_p(rows, p):
    """sparse echelon over GF(p) with min-column pivots (terminates: min column strictly increases)."""
    piv = {}
    for r0 in rows:
        row = {c: v % p for c, v in r0.items() if v % p}
        while row:
            c = min(row)
            if c in piv:
                f = row[c]
                for cc, vv in piv[c].items():
                    nv = (row.get(cc, 0) - f * vv) % p
                    if nv:
                        row[cc] = nv
                    elif cc in row:
                        del row[cc]
            else:
                inv = pow(row[c], p - 2, p)
                piv[c] = {cc: vv * inv % p for cc, vv in row.items()}
                break
    return len(piv)


def dot(row, vec):
    return sum(v * vec[k] for k, v in row.items())


def u_basis(d):
    """Z-basis of u(d) as lists of (row, col, re, im) entries."""
    out = []
    for k in range(d):
        out.append(("iE%d%d" % (k, k), [(k, k, 0, 1)]))
    for k in range(d):
        for l in range(k + 1, d):
            out.append(("A%d%d" % (k, l), [(k, l, 1, 0), (l, k, -1, 0)]))
            out.append(("S%d%d" % (k, l), [(k, l, 0, 1), (l, k, 0, 1)]))
    return out


def tangent_vectors(d, psi):
    """(h acting on party q) psi for q = 0..3 and h in the u(d) basis; exact integer vectors."""
    N = d ** 4
    vecs, labels = [], []
    for q in range(4):
        for name, ent in u_basis(d):
            v = [0] * (2 * N)
            for y in points(d):
                for (rr, cc, er, ei) in ent:
                    if y[q] != rr:
                        continue
                    y2 = list(y)
                    y2[q] = cc
                    pv = psi.get(tuple(y2), 0)
                    if pv:
                        v[ordp(y, d)] += er * pv
                        v[N + ordp(y, d)] += ei * pv
            vecs.append(v)
            labels.append("%s@party%d" % (name, q))
    return vecs, labels


def rank_vectors_mod_p(vecs, p):
    return rank_mod_p([{k: x for k, x in enumerate(v) if x} for v in vecs], p)


# ---------------------------------------------------------------- tau involutions and the hand-proof kernel basis
def code_maps(d, psi):
    C = [y for y in psi]
    by = {}
    mds = True
    for S in itertools.combinations(range(4), 2):
        m = {}
        for c in C:
            key = tuple(c[q] for q in S)
            if key in m:
                mds = False
            m[key] = c
        by[S] = m
    return C, by, mds


def tau(d, by, S, y):
    Sc = tuple(q for q in range(4) if q not in S)
    c1 = by[S][tuple(y[q] for q in S)]      # codeword agreeing with y on S
    c2 = by[Sc][tuple(y[q] for q in Sc)]    # codeword agreeing with y on S^c
    z = [0] * 4
    for q in S:
        z[q] = c2[q]
    for q in Sc:
        z[q] = c1[q]
    return tuple(z)


def group_analysis(d, psi, S1, S2):
    C, by, mds = code_maps(d, psi)
    pts = points(d)
    idx = {y: k for k, y in enumerate(pts)}
    g1 = tuple(idx[tau(d, by, S1, y)] for y in pts)
    g2 = tuple(idx[tau(d, by, S2, y)] for y in pts)
    ident = tuple(range(len(pts)))
    parity = {ident: 0}
    frontier = [ident]
    consistent = True
    while frontier:
        nf = []
        for g in frontier:
            for h in (g1, g2):
                gh = tuple(h[g[k]] for k in range(len(pts)))     # apply g then h
                par = parity[g] ^ 1
                if gh in parity:
                    if parity[gh] != par:
                        consistent = False
                else:
                    parity[gh] = par
                    nf.append(gh)
        frontier = nf
    Cset = set(idx[c] for c in C)
    off = [k for k in range(len(pts)) if k not in Cset]
    seen, orbits = set(), []
    for k in off:
        if k in seen:
            continue
        orb = {}
        for g, par in parity.items():
            orb.setdefault(g[k], set()).add(par)
        seen |= set(orb)
        orbits.append(orb)
    stab_free = all(sum(1 for g in parity if g[k] == k) == 1 for k in off)
    involutive = all(g1[g1[k]] == k for k in range(len(pts))) and all(g2[g2[k]] == k for k in range(len(pts)))
    fixes_code = all(g1[k] == k and g2[k] == k for k in Cset)
    no_fix_off = all(g1[k] != k and g2[k] != k for k in off)
    return {"mds": mds, "group_order": len(parity), "parity_consistent": consistent,
            "involutions": involutive, "fix_code_pointwise": fixes_code, "no_fixed_points_off_code": no_fix_off,
            "free_on_off_code": stab_free, "n_off_code": len(off), "n_orbits": len(orbits),
            "orbit_sizes": sorted(len(o) for o in orbits),
            "predicted_kernel_dim_if_free": len(C) + 2 * len(orbits)}, orbits, pts, Cset


def orbit_kernel_basis(d, orbits, pts, Cset):
    """hand-proof basis: Im at code points; per free orbit: (Re = +-1 by parity) and (Im = 1 on the orbit)."""
    N = d ** 4
    vecs = []
    for k in sorted(Cset):
        v = [0] * (2 * N)
        v[N + k] = 1
        vecs.append(v)
    for orb in orbits:
        if any(len(par) != 1 for par in orb.values()):
            continue  # not free: skip (only used when the action is free)
        va, vb = [0] * (2 * N), [0] * (2 * N)
        for k, par in orb.items():
            pr = next(iter(par))
            va[k] = 1 if pr == 0 else -1     # z = 1: even -> 1, odd -> -conj(1) = -1
            vb[N + k] = 1                    # z = i: even -> i, odd -> -conj(i) = i
        vecs += [va, vb]
    return vecs


def analyse(name, d, ones, cut_names, kernel_check=None):
    t0 = time.time()
    psi = psi_from_perm(d, ones)
    N = d ** 4
    rows = []
    for cn in cut_names:
        rows += cut_equations(d, psi, CUTS[cn])
    uniq = {tuple(sorted(r.items())) for r in rows}
    rows = [dict(r) for r in sorted(uniq)]
    ranks = {str(p): rank_mod_p(rows, p) for p in PRIMES}
    tv, labels = tangent_vectors(d, psi)
    tan_ok = all(dot(r, v) == 0 for v in tv for r in rows)
    tan_rank = {str(p): rank_vectors_mod_p(tv, p) for p in PRIMES}
    rec = {"perm": name, "d": d, "cuts": cut_names, "n_vars": 2 * N, "n_equations_unique": len(rows),
           "rank_mod_p": ranks, "kernel_dim_upper_bound": 2 * N - max(ranks.values()),
           "tangent_vectors_exactly_in_kernel": tan_ok, "tangent_rank_mod_p": tan_rank,
           "kernel_dim_lower_bound": max(tan_rank.values()) if tan_ok else None}
    rec["certified_kernel_dim"] = (rec["kernel_dim_upper_bound"] if tan_ok and
                                   rec["kernel_dim_upper_bound"] == rec["kernel_dim_lower_bound"] else None)
    if len(cut_names) == 2 and cut_names[0] == "U":
        ga, orbits, pts, Cset = group_analysis(d, psi, CUTS["U"], CUTS[cut_names[1]])
        rec["tau_group"] = ga
        if ga["free_on_off_code"] and ga["parity_consistent"]:
            kb = orbit_kernel_basis(d, orbits, pts, Cset)
            rec["orbit_basis_size"] = len(kb)
            rec["orbit_basis_exactly_in_kernel"] = all(dot(r, v) == 0 for v in kb for r in rows)
            rec["orbit_basis_rank_mod_p"] = {str(p): rank_vectors_mod_p(kb, p) for p in PRIMES}
            # same space as the LU tangent? rank of the union
            rec["rank_orbit_basis_union_tangent_mod_p"] = {str(p): rank_vectors_mod_p(kb + tv, p) for p in PRIMES}
    if kernel_check:
        data = json.load(open(kernel_check))
        bad = 0
        mapped = []
        for x in data["basis"]:
            # A's coordinates: x[(r*n + c)] = Re X[r][c], x[n^2 + ...] = Im; X[(k,l),(i,j)] -> dpsi(i,j,k,l)
            n = d * d
            v = [0] * (2 * N)
            for r in range(n):
                for c in range(n):
                    k, l = divmod(r, d)
                    i, j = divmod(c, d)
                    v[ordp((i, j, k, l), d)] = x[r * n + c]
                    v[N + ordp((i, j, k, l), d)] = x[n * n + r * n + c]
            mapped.append(v)
            if any(dot(rw, v) != 0 for rw in rows):
                bad += 1
        rec["implA_kernel_basis_check"] = {"file": kernel_check, "vectors": len(data["basis"]), "violations": bad,
                                           "rank_mod_p": rank_vectors_mod_p(mapped, PRIMES[0]) if mapped else 0}
    rec["secs"] = round(time.time() - t0, 2)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--check-kernel-dir", default=None)
    ap.add_argument("--skip-d4", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    out = {"implementation": "B (state picture, pure Python stdlib)", "python": sys.version.split()[0],
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "perms_sha256": hashlib.sha256(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "perms.py"), "rb").read()).hexdigest(),
           "runs": []}
    jobs = [("C7", ["U", "R"]), ("C7", ["U", "G"]), ("eq14", ["U", "R"]), ("eq14", ["U", "G"]),
            ("ref44_A14", ["U", "R"]), ("ref44_A14", ["U", "G"]), ("C7", ["U"]), ("C7", ["U", "R", "G"])]
    if not a.skip_d4:
        jobs += [("P16_gf4", ["U", "R"]), ("P16_gf4", ["U", "G"])]
    shape_name = {"U": "id", "R": "R", "G": "G"}
    for name, cuts in jobs:
        d, ones = PERMS[name]
        kc = None
        if a.check_kernel_dir and name in ("C7", "P16_gf4"):
            f = os.path.join(a.check_kernel_dir, "%s_%s.json" % (name, "-".join(shape_name[c] for c in cuts)))
            kc = f if os.path.exists(f) else None
        rec = analyse(name, d, ones, cuts, kc)
        out["runs"].append(rec)
        print(json.dumps({k: rec.get(k) for k in ("perm", "cuts", "rank_mod_p", "kernel_dim_upper_bound",
                                                  "kernel_dim_lower_bound", "certified_kernel_dim", "tau_group",
                                                  "orbit_basis_exactly_in_kernel", "rank_orbit_basis_union_tangent_mod_p",
                                                  "implA_kernel_basis_check", "secs")}), flush=True)
    out["secs"] = round(time.time() - t0, 1)
    json.dump(out, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
