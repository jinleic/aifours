#!/usr/bin/env python3
"""Unrun, exact local rank-two occupancy/profile source; see companion narrative.

No input files, network, subprocess, deletion, or output files.  One JSON result
is written to standard output.  The cooperative deadline is 42 s; a parent
must independently read the complete source and give a new one-shot GO with an
external limit <=55 s.  A completed run certifies only the scope in the JSON.
"""

import itertools
import json
import signal
import sys
import time
from collections import Counter, defaultdict

START = time.monotonic()
DEADLINE = START + 42.0
STOP = False


class Incomplete(Exception):
    pass


class Failure(Exception):
    pass


def on_signal(_signum, _frame):
    global STOP
    STOP = True


def guard():
    if STOP or time.monotonic() >= DEADLINE:
        raise Incomplete("cooperative deadline or signal")


def need(condition, reason):
    if not condition:
        raise Failure(reason)


def p2(x):
    return (x ^ (x >> 1)) & 1


def sign(bit):
    return 1 - 2 * (bit & 1)


def rho(b):
    return sign(1 + (b & 1) * ((b >> 1) & 1))


def col(ell, h, i, b):
    return (((2 * ell + h) * 4 + i) * 4 + b)


def raw_profile(row):
    """4*Z(s,alpha), eta order 4*s+alpha; row index is 4*h+b."""
    return tuple(sum(row[4*h+b] * sign(s*h + p2(alpha & b))
                     for h in range(2) for b in range(4))
                 for s in range(2) for alpha in range(4))


def local_status(row, role, graph_h=None, full_row=False):
    if len(row) != 8:
        return "ROW_LENGTH", None
    for h in range(2):
        for b in range(4):
            v = row[4*h+b]
            if role == "graph":
                if h == graph_h and v not in (-1, 1):
                    return "GRAPH_VALUE", None
                if h != graph_h and v not in (-2, 0, 2):
                    return "MATE_VALUE", None
            elif role == "ell0":
                if v not in (-2, 0, 2):
                    return "ELL0_VALUE", None
                if full_row and b == 0 and v != 0:
                    return "FULL_BLOCK_VALUE", None
            else:
                return "ROLE", None
    if sum(row) != 0:
        return "ZERO_ETA", None
    q = raw_profile(row)
    if any(x % 4 for x in q):
        return "PROFILE_NONINTEGRAL", None
    z = tuple(x // 4 for x in q)
    if any(abs(x) > 2 for x in z):
        return "LOCAL_PROFILE_CAP", None
    if 2 * sum(x*x for x in z) != sum(x*x for x in row):
        return "LOCAL_PARSEVAL", None
    return "OK", z


def bool_class(v):
    """Actual two-bit sign table classification, not a guessed parity rule."""
    if len(v) != 4 or any(x not in (-1, 1) for x in v):
        return "INVALID"
    w = [sum(v[b] * sign(p2(a & b)) for b in range(4))
         for a in range(4)]
    if sorted(abs(x) for x in w) == [0, 0, 0, 4]:
        return "character"
    if all(abs(x) == 2 for x in w):
        return "bent"
    return "INVALID"


def phase_relation_status(xg, ag, yg):
    if bool_class(ag) != "character":
        return "PHASE_NONAFFINE"
    if any(yg[b] != -ag[b] * rho(b) * xg[b] for b in range(4)):
        return "GRAPH_RELATION"
    return "OK"


def lambda_status(v):
    if len(v) != 8 or any(type(x) is not int or abs(x) > 2 for x in v):
        return "LAMBDA_DOMAIN"
    if sum(x*x for x in v) != 4:
        return "LAMBDA_ENERGY"
    support = [i for i, x in enumerate(v) if x]
    if len(support) == 1 and abs(v[support[0]]) == 2:
        return "OK"
    if len(support) != 4 or any(abs(v[i]) != 1 for i in support):
        return "LAMBDA_FORM"
    if support[0] ^ support[1] ^ support[2] ^ support[3]:
        return "LAMBDA_NONFLAT"
    prod = 1
    for i in support:
        prod *= v[i]
    if prod != -1:
        return "LAMBDA_SIGN_PRODUCT"
    return "OK"


def all_lambda_profiles():
    result = []
    for i in range(8):
        for s in (-2, 2):
            v = [0]*8
            v[i] = s
            result.append(tuple(v))
    planes = 0
    for points in itertools.combinations(range(8), 4):
        if points[0] ^ points[1] ^ points[2] ^ points[3]:
            continue
        planes += 1
        for ss in itertools.product((-1, 1), repeat=4):
            if ss[0]*ss[1]*ss[2]*ss[3] != -1:
                continue
            v = [0]*8
            for i, s in zip(points, ss):
                v[i] = s
            result.append(tuple(v))
    need(planes == 14 and len(result) == 128 and len(set(result)) == 128,
         "PROFILE_SET_CARDINALITY")
    need(all(lambda_status(v) == "OK" for v in result), "PROFILE_SET_CHECK")
    return result


def enumerate_graph_rows():
    counts = [defaultdict(Counter) for _ in range(2)]
    reps = [{}, {}]
    zero_counts = [Counter(), Counter()]
    all_status = [Counter(), Counter()]
    phase_types = Counter()
    for fh in range(2):
        n = 0
        for gs in itertools.product((-1, 1), repeat=4):
            for ms in itertools.product((-2, 0, 2), repeat=4):
                n += 1
                if n % 64 == 0:
                    guard()
                row = [0]*8
                for b in range(4):
                    row[4*fh+b] = gs[b]
                    row[4*(1-fh)+b] = ms[b]
                k = sum(v != 0 for v in ms)
                if sum(row) == 0:
                    zero_counts[fh][k] += 1
                why, z = local_status(row, "graph", fh)
                all_status[fh][why] += 1
                if why != "OK":
                    continue
                lam = z[4]
                counts[fh][k][lam] += 1
                reps[fh].setdefault((k, lam), tuple(row))
                xc = bool_class(gs)
                need(xc == ("bent" if k % 2 else "character"),
                     "GRAPH_X_CLASS")
                for cov in range(4):
                    for const in (0, 1):
                        aa = tuple(sign(const + p2(cov & b)) for b in range(4))
                        yy = tuple(-aa[b] * rho(b) * gs[b] for b in range(4))
                        need(phase_relation_status(gs, aa, yy) == "OK", "GRAPH_REL")
                        yc = bool_class(yy)
                        need(yc == ("character" if k % 2 else "bent"),
                             "GRAPH_Y_CLASS")
                        phase_types[(fh, k, xc, yc)] += 1
        need(n == 1296, "GRAPH_DOMAIN_SIZE")
        need([zero_counts[fh][k] for k in range(5)] == [6, 32, 84, 96, 44],
             "GRAPH_ZERO_ETA_CENSUS")
        need([sum(counts[fh][k].values()) for k in range(5)] == [6, 32, 84, 96, 32],
             "GRAPH_LOCAL_CAP_CENSUS")
    return counts, reps, zero_counts, all_status, phase_types


def enumerate_ell0_row(full_row):
    positions = [4*h+b for h in range(2) for b in range(4)
                 if not (full_row and b == 0)]
    counts = Counter()
    reps = {}
    statuses = Counter()
    for n, values in enumerate(itertools.product((-2, 0, 2), repeat=len(positions))):
        if n % 128 == 0:
            guard()
        row = [0]*8
        for p, v in zip(positions, values):
            row[p] = v
        why, z = local_status(row, "ell0", full_row=full_row)
        statuses[why] += 1
        if why != "OK":
            continue
        e = sum(row[4*h] != 0 for h in range(2))
        nz = sum(row[4*h+b] != 0 for h in range(2) for b in (1, 2, 3))
        key = (e, nz, z[4])
        counts[key] += 1
        reps.setdefault(key, tuple(row))
    return counts, reps, statuses


def ell0_combinations(profiles, standard, full):
    prefixes = [set() for _ in range(5)]
    for p in profiles:
        for j in range(5):
            prefixes[j].add(p[:j])
    # key (E-D0 count, Z2 count, lambda prefix) -> (multiplicity, rows)
    dp = {(0, 0, ()): (1, ())}
    for i in range(4):
        hist, representatives, _ = full if i == 0 else standard
        nxt = {}
        step = 0
        for (e, z, prefix), (n0, rows) in dp.items():
            for (de, dz, lam), n1 in hist.items():
                step += 1
                if step % 512 == 0:
                    guard()
                pp = prefix + (lam,)
                key = (e+de, z+dz, pp)
                if e+de > 4 or z+dz > 6 or pp not in prefixes[i+1]:
                    continue
                prior = nxt.get(key)
                if prior is None:
                    nxt[key] = (n0*n1, rows + (representatives[(de, dz, lam)],))
                else:
                    nxt[key] = (prior[0]+n0*n1, prior[1])
        dp = nxt
    return dp


def graph_combinations(f, ks, counts, reps, prefixes):
    dp = {(): (1, ())}
    for i in range(4):
        nxt = {}
        for pref, (n0, rows) in dp.items():
            for lam, n1 in counts[f[i]][ks[i]].items():
                pp = pref + (lam,)
                if pp not in prefixes[i+1]:
                    continue
                cand = rows + (reps[f[i]][(ks[i], lam)],)
                old = nxt.get(pp)
                if old is None:
                    nxt[pp] = (n0*n1, cand)
                else:
                    nxt[pp] = (old[0]+n0*n1, old[1])
        dp = nxt
    return dp


def inverse_u(x, a, g, y):
    u = []
    for c in range(64):
        for w in range(4):
            c1 = sign(w & 1)
            c2 = sign((w >> 1) & 1)
            num = x[c] + 3*a[c]*c1 + g[c]*c2 + y[c]*c1*c2
            need(num % 4 == 0, "INVERSE_NONINTEGRAL")
            value = num // 4
            need(value in (-1, 0, 1), "INVERSE_NONTERNARY")
            u.append(value)
    return u


def physical_status(f, x, a, g, y):
    counts = Counter()
    for ell in range(2):
        for h in range(2):
            for i in range(4):
                for b in range(4):
                    c = col(ell, h, i, b)
                    if ell == 1 and h == f[i]:
                        if abs(x[c]) != 1 or abs(a[c]) != 1 or g[c] != rho(b):
                            return "GRAPH_DOMAIN", counts
                        if y[c] != -a[c]*g[c]*x[c]:
                            return "GRAPH_RELATION", counts
                        counts["S"] += 1
                    elif ell == 1 or (b == 0 and i != 0):
                        if a[c] != 0:
                            return "D_A", counts
                        expected_g = -2*rho(b) if ell == 1 else -2
                        if g[c] != expected_g:
                            return "D_G", counts
                        if abs(x[c]) == 2 and y[c] == 0:
                            counts["D0"] += 1
                        elif x[c] == 0 and abs(y[c]) == 2:
                            counts["D3"] += 1
                        else:
                            return "D_FORM", counts
                    elif b == 0:
                        if x[c] != 0 or y[c] != 0 or a[c] != 0 or g[c] != 4:
                            return "F_FORM", counts
                        counts["F"] += 1
                    else:
                        if a[c] != 0 or g[c] != 0:
                            return "Z_AG", counts
                        if x[c] == 0 and y[c] == 0:
                            counts["Z0"] += 1
                        elif abs(x[c]) == 2 and abs(y[c]) == 2:
                            counts["Z2"] += 1
                        elif x[c] == 0 and abs(y[c]) == 4:
                            counts["Z4"] += 1
                        else:
                            return "Z_FORM", counts
    for name, value in (("S", 16), ("F", 2), ("D0", 4), ("Z2", 6),
                        ("Z4", 1), ("D3", 18), ("Z0", 17)):
        if counts[name] != value:
            return name + "_COUNT", counts
    return "OK", counts


def arrays_from_rows(f, graph_rows, ell_rows):
    x = [0]*64
    a = [0]*64
    g = [0]*64
    y = [0]*64
    zfree = []
    d3 = []
    for ell in range(2):
        for h in range(2):
            for i in range(4):
                for b in range(4):
                    c = col(ell, h, i, b)
                    x[c] = (graph_rows if ell else ell_rows)[i][4*h+b]
                    if ell == 1 and h == f[i]:
                        a[c] = sign(p2(i & b))
                        g[c] = rho(b)
                        y[c] = -a[c]*g[c]*x[c]
                    elif ell == 1 or (b == 0 and i != 0):
                        g[c] = -2*rho(b) if ell == 1 else -2
                        if x[c] == 0:
                            y[c] = 2
                            d3.append(c)
                    elif b == 0:
                        g[c] = 4
                    elif x[c] != 0:
                        y[c] = 2
                    else:
                        zfree.append(c)
    need(len(zfree) == 18 and len(d3) == 18, "FIXTURE_FREE_SITE_COUNT")
    y[zfree[0]] = 4
    u = inverse_u(x, a, g, y)
    if sum(u[4*c] != 0 for c in range(64)) % 2 == 0:
        y[d3[0]] = -y[d3[0]]
        u = inverse_u(x, a, g, y)
    return x, a, g, y, u


def walsh(v):
    return [sum(v[c] * sign((c & xi).bit_count()) for c in range(len(v)))
            for xi in range(len(v))]


def bent4(v):
    return len(v) == 16 and all(abs(x) == 4 for x in walsh(v))


def describe_fixture(f, graph_rows, ell_rows):
    x, a, g, y, u = arrays_from_rows(f, graph_rows, ell_rows)
    why, counts = physical_status(f, x, a, g, y)
    need(why == "OK", "PHYSICAL_" + why)
    for c in range(64):
        for k, want in ((0, x[c]), (1, 3*a[c]), (2, g[c]), (3, y[c])):
            got = sum(u[4*c+w] * sign(p2(k & w)) for w in range(4))
            need(got == want, "INVERSE_RECONSTRUCTION")
    row_profiles = []
    for i in range(4):
        why, z = local_status(ell_rows[i], "ell0", full_row=(i == 0))
        need(why == "OK", "ELL_FIXTURE_" + why)
        row_profiles.append(z)
    for i in range(4):
        why, z = local_status(graph_rows[i], "graph", f[i])
        need(why == "OK", "GRAPH_FIXTURE_" + why)
        row_profiles.append(z)
    lp = tuple(z[4] for z in row_profiles)
    need(lambda_status(lp) == "OK", "FIXTURE_LAMBDA_PROFILE")
    need(sum(sum(v*v for v in z) for z in row_profiles) == 28,
         "FIXTURE_PROFILE_ENERGY")
    need(sum(sum(v*v for v in z) for z in row_profiles[4:]) == 16,
         "FIXTURE_GRAPH_PROFILE_ENERGY")
    need(sum(sum(v*v for v in z) for z in row_profiles[:4]) == 12,
         "FIXTURE_ELL_PROFILE_ENERGY")
    need(sum(v*v for v in x) == 56 and sum(v*v for v in y) == 128,
         "FIXTURE_ENERGIES")
    need(sum(v != 0 for v in u) == 116 and sum(v == 0 for v in y) == 23,
         "FIXTURE_SUPPORT_OR_ZEROES")
    need(not any(a[c] == 0 and abs(x[c]) == 4 for c in range(64)), "FIXTURE_H")
    need(sum(u[4*c] != 0 for c in range(64)) % 2 == 1, "FIXTURE_J")
    fq = [sign(f[i] + 1 + (b & 1)*((b >> 1) & 1))
          for i in range(4) for b in range(4)]
    rr = [sign(p2(i & b)) for i in range(4) for b in range(4)]
    rf = [sign(p2(i & b) + f[i]) for i in range(4) for b in range(4)]
    need(bent4(fq) and bent4(rr) and bent4(rf), "FIXTURE_COMMON_BENT")
    xw, yw, aw, gw = walsh(x), walsh(y), walsh(a), walsh(g)
    need(all(abs(v) == 4 for v in aw), "FIXTURE_A_BENT")
    need(sorted(abs(v) for v in gw) == [4]*4 + [12]*60, "FIXTURE_G_SPECTRUM")
    need(xw[0] == 0, "FIXTURE_SELECTED_T_ZERO")
    return {
        "F": list(f), "x": x, "a": a, "g": g, "y": y, "u_by_c_then_w": u,
        "physical_counts": dict(counts), "J": 1, "H_local": 0,
        "lambda_profile_ell0_then_ell1": list(lp),
        "x_energy": 56, "y_energy": 128, "u_support": 116, "y_zeroes": 23,
        "xhat_at_selected_t0": xw[0],
        "all_xhat_divisible_by_8": all(v % 8 == 0 for v in xw),
        "all_xhat_abs_le_8": all(abs(v) <= 8 for v in xw),
        "all_yhat_abs_le_12": all(abs(v) <= 12 for v in yw),
        "all_yhat_4_mod_8": all(v % 8 == 4 for v in yw),
        "max_abs_xhat": max(abs(v) for v in xw),
        "max_abs_yhat": max(abs(v) for v in yw),
        "phase": "f(i,b)=F[i], r(i,b)=i dot b; q=1+b0*b1; t=0"
    }


def make_manual_positive():
    f = (0, 0, 0, 1)
    graph = []
    for fh in f:
        row = [0]*8
        for b in range(4):
            row[4*fh+b] = sign(b & 1)
        graph.append(tuple(row))
    rows = [[0]*8 for _ in range(4)]
    rows[0][1], rows[0][2] = 2, -2
    rows[1][0], rows[1][1], rows[1][4], rows[1][5] = 2, 2, -2, -2
    rows[2][0], rows[2][1], rows[2][4], rows[2][5] = 2, -2, -2, 2
    return f, tuple(graph), tuple(tuple(row) for row in rows)


def controls():
    seen = {}
    f, gr, er = make_manual_positive()
    good = describe_fixture(f, gr, er)
    need(good["lambda_profile_ell0_then_ell1"] == [0, 2, 0, 0, 0, 0, 0, 0],
         "MANUAL_POSITIVE_LAMBDA")
    x, a, g, y, _u = arrays_from_rows(f, gr, er)

    def expect(name, actual, wanted):
        need(actual == wanted, "CONTROL_" + name + "_GOT_" + actual)
        seen[name] = actual

    row = list(gr[0]); row[0] = 0
    expect("bad_graph_value", local_status(row, "graph", 0)[0], "GRAPH_VALUE")
    row = list(gr[0]); row[4] = 1
    expect("bad_mate_value", local_status(row, "graph", 0)[0], "MATE_VALUE")
    row = list(gr[0]); row[0] = -row[0]
    expect("zero_eta", local_status(row, "graph", 0)[0], "ZERO_ETA")
    row = [sign(b & 1) for b in range(4)] + [2*sign(b & 1) for b in range(4)]
    expect("local_profile_over_cap", local_status(row, "graph", 0)[0], "LOCAL_PROFILE_CAP")
    row = list(er[0]); row[0] = 2
    expect("full_block_value", local_status(row, "ell0", full_row=True)[0], "FULL_BLOCK_VALUE")
    xx = tuple(sign(b & 1) for b in range(4))
    aa = (1, 1, 1, 1)
    yy = tuple(-aa[b]*rho(b)*xx[b] for b in range(4))
    bad_y = (-yy[0],) + yy[1:]
    expect("graph_relation", phase_relation_status(xx, aa, bad_y), "GRAPH_RELATION")
    nonlinear_a = tuple(sign((b & 1)*((b >> 1) & 1)) for b in range(4))
    expect("phase_nonaffine", phase_relation_status(xx, nonlinear_a, yy), "PHASE_NONAFFINE")
    expect("lambda_energy", lambda_status((2, 1, 0, 0, 0, 0, 0, 0)), "LAMBDA_ENERGY")
    expect("lambda_nonflat", lambda_status((1, 1, 1, 0, 0, 0, 0, -1)), "LAMBDA_NONFLAT")
    expect("lambda_sign_product", lambda_status((1, 1, 1, 1, 0, 0, 0, 0)),
           "LAMBDA_SIGN_PRODUCT")

    # Physical inverse mutants: change a D3 into D0, a Z2 into Z0, or the Z4
    # into Z0.  Rebuild the actual ternary inverse before checking counts.
    c_d3 = next(col(1, 1-f[i], i, b) for i in range(4) for b in range(4)
                if x[col(1, 1-f[i], i, b)] == 0)
    bx, by = x[:], y[:]
    bx[c_d3], by[c_d3] = 2, 0
    inverse_u(bx, a, g, by)
    expect("physical_d0_count", physical_status(f, bx, a, g, by)[0], "D0_COUNT")
    c_z2 = next(col(0, h, i, b) for h in range(2) for i in range(4)
                for b in (1, 2, 3) if x[col(0, h, i, b)] != 0)
    bx, by = x[:], y[:]
    bx[c_z2], by[c_z2] = 0, 0
    inverse_u(bx, a, g, by)
    expect("physical_z2_count", physical_status(f, bx, a, g, by)[0], "Z2_COUNT")
    c_z4 = next(c for c in range(64) if abs(y[c]) == 4)
    by = y[:]; by[c_z4] = 0
    inverse_u(x, a, g, by)
    expect("physical_z4_count", physical_status(f, x, a, g, by)[0], "Z4_COUNT")

    # This mutation preserves a real ternary inverse, all physical local counts,
    # per-row zero-eta and local caps, but produces two lambda entries of 2.
    bad_er = [list(r) for r in er]
    bad_er[2][1], bad_er[2][5] = 2, -2
    bx, ba, bg, by, _bu = arrays_from_rows(f, gr, tuple(tuple(r) for r in bad_er))
    need(physical_status(f, bx, ba, bg, by)[0] == "OK", "LAMBDA_MUTANT_PHYSICAL")
    lams = []
    for i in range(4):
        why, p = local_status(bad_er[i], "ell0", full_row=(i == 0))
        need(why == "OK", "LAMBDA_MUTANT_ELL_LOCAL")
        lams.append(p[4])
    for i in range(4):
        why, p = local_status(gr[i], "graph", f[i])
        need(why == "OK", "LAMBDA_MUTANT_GRAPH_LOCAL")
        lams.append(p[4])
    expect("physical_lambda_energy", lambda_status(tuple(lams)), "LAMBDA_ENERGY")
    return seen, good


def main():
    profiles = all_lambda_profiles()
    graph_counts, graph_reps, zero, graph_statuses, phase_types = enumerate_graph_rows()
    standard = enumerate_ell0_row(False)
    full = enumerate_ell0_row(True)
    edp = ell0_combinations(profiles, standard, full)
    by_graph = defaultdict(list)
    gprefix = [set() for _ in range(5)]
    for p in profiles:
        by_graph[p[4:]].append(p[:4])
        for j in range(5):
            gprefix[j].add(p[4:4+j])
    all_f = [f for f in itertools.product((0, 1), repeat=4) if sum(f) % 2 == 1]
    need(len(all_f) == 8, "ODD_F_DOMAIN")
    ordered = Counter()
    shapes = Counter()
    energy = Counter()
    fixture_rows = {}
    keys = []
    for ks in itertools.product(range(5), repeat=4):
        if sum(ks) > 4:
            continue
        de = 4 - sum(ks)
        shape = (de, tuple(sorted(ks, reverse=True)))
        ordered[ks] += 0
        shapes[shape] += 0
        keys.append(ks)
        for f in all_f:
            guard()
            gp = graph_combinations(f, ks, graph_counts, graph_reps, gprefix)
            for glambda, (ng, grows) in gp.items():
                for elambda in by_graph.get(glambda, ()):
                    item = edp.get((de, 6, elambda))
                    if item is None:
                        continue
                    ne, erows = item
                    weight = ng * ne
                    ordered[ks] += weight
                    shapes[shape] += weight
                    eg = sum(v*v for v in glambda)
                    ee = sum(v*v for v in elambda)
                    need(eg + ee == 4, "LAMBDA_ENERGY_ASSEMBLY")
                    energy[(shape, eg, ee)] += weight
                    fixture_rows.setdefault(shape, (f, grows, erows))
    need(len(keys) == 70 and len(shapes) == 12, "OCCUPANCY_DOMAIN")
    fixtures = []
    for shape, rowdata in sorted(fixture_rows.items()):
        guard()
        obj = describe_fixture(*rowdata)
        obj["ell0_D0"] = shape[0]
        obj["graph_D0_multiset_descending"] = list(shape[1])
        fixtures.append(obj)
    need((4, (0, 0, 0, 0)) in fixture_rows, "NO_POSITIVE_INVERSE_FIXTURE")
    control_results, manual = controls()
    guard()
    return {
        "status": "PASS_EXACT_LOCAL_AND_LAMBDA_SCOPE_ONLY",
        "deadline_seconds": 42,
        "domain": "8 odd F tables; each graph row all 2^4*3^4 x patterns; 70 ordered graph occupancy vectors with residual E D0; six Z2 and one independent Z4 location",
        "zero_eta_graph_counts_each_F_bit": [[zero[fh][k] for k in range(5)] for fh in range(2)],
        "locally_cap_necessary_graph_counts_each_F_bit": [[sum(graph_counts[fh][k].values()) for k in range(5)] for fh in range(2)],
        "graph_lambda_histograms": [{str(k): dict(sorted(graph_counts[fh][k].items())) for k in range(5)} for fh in range(2)],
        "graph_row_status_counts": [dict(s) for s in graph_statuses],
        "phase_class_counts": [{"F_bit": fh, "mate_D0": k, "x_class": xc, "y_class": yc, "count": n}
                               for (fh, k, xc, yc), n in sorted(phase_types.items())],
        "ell0_local_status_counts": {"full_i0": dict(full[2]), "other_i": dict(standard[2])},
        "lambda_profile_count": len(profiles),
        "ordered_occupancy_counts": [{"graph_D0_i0_to_i3": list(ks), "ell0_D0": 4-sum(ks), "F_and_x_arrays": ordered[ks]} for ks in sorted(keys)],
        "occupancy_shape_counts": [{"ell0_D0": shape[0], "graph_D0_multiset_descending": list(shape[1]), "F_and_x_arrays": n,
                                    "F_x_and_Z4_locations": 18*n} for shape, n in sorted(shapes.items())],
        "lambda_energy_compatibility": [{"ell0_D0": shape[0], "graph_D0_multiset_descending": list(shape[1]),
                                          "graph_lambda_energy": eg, "ell0_lambda_energy": ee, "F_and_x_arrays": n}
                                         for (shape, eg, ee), n in sorted(energy.items())],
        "controls_expected_and_observed": control_results,
        "manual_positive_physical_inverse": manual,
        "one_physical_inverse_per_nonempty_shape": fixtures,
        "counting_note": "Counts distinguish F and full X, not r phases, y signs or complete u; choosing any one of 18 Z4 locations multiplies F/X counts by 18. Four ordered graph cosets remain labeled in ordered_occupancy_counts.",
        "scope_note": "Every nonzero eta has an integer per-coset value in [-2,2]; ONLY lambda is required to be one actual 128-vector profile. This is necessary-profile enumeration, not simultaneous satisfaction of the other six full profiles, all U0 caps/divisibility, all U3 caps, original carried t, V, or the original caller. Fixtures use the displayed single common physical f,r and t=0, not arbitrary original caller data.",
        "elapsed_seconds": time.monotonic() - START
    }


if __name__ == "__main__":
    signal.signal(signal.SIGINT, on_signal)
    signal.signal(signal.SIGTERM, on_signal)
    try:
        result = main()
        sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
    except Incomplete as exc:
        sys.stdout.write(json.dumps({"status": "INCOMPLETE", "reason": str(exc),
                                     "elapsed_seconds": time.monotonic()-START}) + "\n")
        sys.exit(2)
    except Exception as exc:
        sys.stdout.write(json.dumps({"status": "FAIL", "error_type": type(exc).__name__,
                                     "reason": str(exc),
                                     "elapsed_seconds": time.monotonic()-START}) + "\n")
        sys.exit(1)
