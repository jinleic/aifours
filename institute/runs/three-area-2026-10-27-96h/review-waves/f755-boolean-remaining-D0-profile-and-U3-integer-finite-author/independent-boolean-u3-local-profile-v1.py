#!/usr/bin/env python3
"""Unrun F755 exact finite-scope proposal. Stdlib only; JSON stdout; no inputs.

This is a prospective checker, not a physical witness, a proof of simultaneous
seven profiles, a construction of Y, or a parent GO.  Its single E-lambda
counterconfiguration is only an exact LOCAL relaxation of the actual caller.
"""
import itertools
import json
import signal
import sys
import time

START = time.monotonic()
DEADLINE = START + 42.0
TICKS = 0


class Incomplete(Exception):
    pass


class Reject(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


def stop_signal(signum, _frame):
    raise Incomplete("SIGNAL_" + str(signum))


signal.signal(signal.SIGTERM, stop_signal)
signal.signal(signal.SIGINT, stop_signal)


def tick():
    global TICKS
    TICKS += 1
    if TICKS % 512 == 0 and time.monotonic() >= DEADLINE:
        raise Incomplete("COOPERATIVE_DEADLINE")


def need(condition, reason):
    if not condition:
        raise Reject(reason)


def expect_reason(name, reason, action, results):
    try:
        action()
    except Reject as exc:
        if exc.reason != reason:
            raise Reject("CONTROL_WRONG_REASON_" + name + "_" + exc.reason)
        results[name] = exc.reason
        return
    raise Reject("CONTROL_ACCEPTED_" + name)


def chi(alpha, x):
    return -1 if (alpha & x).bit_count() % 2 else 1


def check_pairs(pairs, d):
    need(0 <= d <= 4, "D_RANGE")
    need(len(pairs) == 32, "PAIR_COUNT")
    need(all(isinstance(u, int) and isinstance(v, int) for u, v in pairs),
         "PAIR_INTEGER")
    need(all(u % 8 == 4 and v % 8 == 4 for u, v in pairs), "U3_RESIDUE")
    need(all(abs(u) <= 12 and abs(v) <= 12 for u, v in pairs), "U3_CAP")
    need(sum(u*u + v*v for u, v in pairs) == 64*128, "TOTAL_ENERGY_128")
    a1 = [(u-v)//2 for u, v in pairs]
    need(sum(x*x for x in a1) == 32*(64+4*d), "PARTIAL_ENERGY")
    return a1


def check_census(row, d):
    e, o, p, z, h, z4 = row
    need(0 <= d <= 4, "D_RANGE")
    need(all(isinstance(x, int) and x >= 0 for x in row), "NONNEGATIVE_CENSUS")
    need(e+o+p+z == 32, "PAIR_COUNT")
    need(h <= o, "H_BOUND")
    need(z4 <= z, "Z4_BOUND")
    need(e+o+h+2*z4 == 8, "SMALL_CENSUS")
    need(o+4*e+9*p == 128+8*d, "PARTIAL_ENERGY")


def compare_declared(actual, declared):
    need(actual == declared, "DECLARED_TABLE_MISMATCH")


def integer_census():
    # Generate the six local pair types from ALL ordered actual full values,
    # rather than importing the displayed four-variable table as an axiom.
    values = [v for v in range(-12, 13) if v % 8 == 4]
    signatures = set()
    for u, v in itertools.product(values, repeat=2):
        a0, a1 = (u+v)//2, (u-v)//2
        need(2*a0 == u+v and 2*a1 == u-v, "HALF_INTEGRAL_PAIR")
        need(a0 % 4 == 0 and a1 % 4 == 0, "PAIR_NOT_MULTIPLE_OF_FOUR")
        need((a0//4-a1//4) % 2 != 0, "PAIR_PARITY")
        cat = {0: "Z", 4: "O", 8: "E", 12: "P"}.get(abs(a1))
        need(cat is not None, "PAIR_CATEGORY")
        signatures.add((cat, int(cat == "O" and a0 == 0),
                        int(cat == "Z" and abs(a0) == 4),
                        int(abs(u) == 4)+int(abs(v) == 4), a1*a1))
    expected = {("E", 0, 0, 1, 64), ("O", 0, 0, 1, 16),
                ("O", 1, 0, 2, 16), ("P", 0, 0, 0, 144),
                ("Z", 0, 0, 0, 0), ("Z", 0, 1, 2, 0)}
    need(signatures == expected, "PAIR_SIGNATURES")

    # All multiplicities of those six signatures: choose E,O,P,Z; H selects
    # O's double-small subtype, Z4 selects Z's double-small subtype.
    # The exact full energy is equivalent to eight small coefficients among 64.
    result = {}
    for d in range(5):
        rows = set()
        for e in range(9):
            for o in range(9-e):
                for p in range(33-e-o):
                    tick()
                    z = 32-e-o-p
                    if 64*e + 16*o + 144*p != 32*(64+4*d):
                        continue
                    for h in range(o+1):
                        for z4 in range(z+1):
                            if e+o+h+2*z4 == 8:
                                row = (e, o, p, z, h, z4)
                                check_census(row, d)
                                rows.add(row)
        result[d] = sorted(rows)
    declared = {
        0: {(0,2,14,16), (1,7,13,11), (2,3,13,14),
            (4,4,12,12), (7,1,11,13)},
        2: {(0,0,16,16), (1,5,15,11), (2,1,15,14), (4,2,14,12)},
        4: {(0,7,17,8), (1,3,17,11), (3,4,16,9),
            (4,0,16,12), (6,1,15,10)},
    }
    comparisons = {}
    for d, wanted in declared.items():
        actual = {r[:4] for r in result[d]}
        comparisons[str(d)] = {
            "declared_only": sorted(wanted-actual),
            "enumerated_only": sorted(actual-wanted),
            "match": actual == wanted,
        }
    return result, comparisons, sorted(signatures), declared


def graph_transform(f, graph, mate):
    return tuple(sum((graph[b]*((-1)**(s*f)) +
                      mate[b]*((-1)**(s*(1-f))))*chi(alpha, b)
                     for b in range(4))
                 for s in range(2) for alpha in range(4))


def check_graph(f, graph, mate, enforce_cap=True):
    need(f in (0, 1), "GRAPH_H")
    need(len(graph) == 4 and all(x in (-1, 1) for x in graph), "GRAPH_VALUE")
    need(len(mate) == 4 and all(x in (-2, 0, 2) for x in mate), "MATE_VALUE")
    need(sum(graph)+sum(mate) == 0, "ZERO_ETA")
    k = sum(x != 0 for x in mate)
    negative = sum(x == -1 for x in graph)
    need((negative-k) % 2 == 0, "GRAPH_PARITY")
    numerators = graph_transform(f, graph, mate)
    need(all(n % 4 == 0 for n in numerators), "GRAPH_ETA_INTEGRAL")
    z = tuple(n//4 for n in numerators)
    need(z[0] == 0, "ZERO_ETA")
    expected = -((-1)**f)*sum(x//2 for x in mate)
    need(z[4] == expected, "GRAPH_LAMBDA_IDENTITY")
    need(z[4] % 2 == k % 2, "LAMBDA_PARITY")
    if enforce_cap:
        need(all(abs(x) <= 2 for x in z), "LOCAL_PROFILE_CAP")
    return z


def graph_cases():
    data = {}
    summaries = {}
    for f in (0, 1):
        raw = [0]*5
        admitted = [0]*5
        census = [dict() for _ in range(5)]
        choices = {}
        for graph in itertools.product((-1, 1), repeat=4):
            for mate in itertools.product((-2, 0, 2), repeat=4):
                tick()
                if sum(graph)+sum(mate) != 0:
                    continue
                k = sum(x != 0 for x in mate)
                raw[k] += 1
                z = check_graph(f, graph, mate, False)
                if any(abs(x) > 2 for x in z):
                    continue
                check_graph(f, graph, mate)
                admitted[k] += 1
                lam = z[4]
                census[k][lam] = census[k].get(lam, 0)+1
                choices.setdefault((k, lam), (graph, mate))
        need(raw == [6,32,84,96,44], "GRAPH_ZERO_ETA_CENSUS")
        need(admitted == [6,32,84,96,32], "GRAPH_LOCAL_CAP_CENSUS")
        wanted = [{0:6}, {-1:16,1:16}, {-2:6,0:72,2:6},
                  {-1:48,1:48}, {-2:4,0:24,2:4}]
        need(census == wanted, "GRAPH_LAMBDA_CENSUS")
        data[f] = choices
        summaries[str(f)] = {"zero_eta_by_k": raw, "local_cap_by_k": admitted,
                             "lambda_census_by_k": census}
    for k in range(5):
        need({lam for kk, lam in data[0] if kk == k} ==
             {lam for kk, lam in data[1] if kk == k}, "H_LAMBDA_SUPPORT")
    return data, summaries


def ell_transform(row):
    return tuple(sum(row[4*h+b]*((-1)**(s*h))*chi(alpha, b)
                     for h in range(2) for b in range(4))
                 for s in range(2) for alpha in range(4))


def ell_options():
    # i=0 has two physical full blocks at b=0; i=1,2,3 have E sites there.
    options = []
    raw_counts = []
    for i in range(4):
        positions = [(h,b) for h in range(2) for b in range(4)
                     if not (i == 0 and b == 0)]
        by_lambda = {}
        count = 0
        for vals in itertools.product((-2, 0, 2), repeat=len(positions)):
            tick()
            row = [0]*8
            for (h,b), x in zip(positions, vals):
                row[4*h+b] = x
            if sum(row) != 0:
                continue
            d = sum(row[4*h] != 0 for h in range(2)) if i else 0
            z = sum(row[4*h+b] != 0 for h in range(2) for b in (1,2,3))
            if d > 4 or z > 6:
                continue
            nums = ell_transform(row)
            if any(n % 4 for n in nums) or any(abs(n) > 8 for n in nums):
                continue
            need(nums[0] == 0, "ELL_ZERO_ETA")
            lam = nums[4]//4
            by_lambda.setdefault(lam, {}).setdefault((d,z), tuple(row))
            count += 1
        options.append(by_lambda)
        raw_counts.append(count)
    return options, raw_counts


def check_profile(v):
    need(len(v) == 8 and all(isinstance(x, int) for x in v), "LAMBDA_VECTOR")
    need(sum(x*x for x in v) == 4, "LAMBDA_ENERGY")
    support = [i for i, x in enumerate(v) if x]
    if len(support) == 1:
        need(abs(v[support[0]]) == 2, "LAMBDA_SINGLETON_VALUE")
        return "singleton"
    need(len(support) == 4 and all(abs(v[i]) == 1 for i in support),
         "LAMBDA_SUPPORT")
    xor = 0
    for i in support:
        xor ^= i
    need(xor == 0, "LAMBDA_NONFLAT")
    product = 1
    for i in support:
        product *= v[i]
    need(product == -1, "LAMBDA_SIGN_PRODUCT")
    return "four_flat"


def all_profiles():
    result = []
    for i in range(8):
        for x in (-2, 2):
            v = [0]*8
            v[i] = x
            check_profile(v)
            result.append(tuple(v))
    for support in itertools.combinations(range(8), 4):
        if support[0] ^ support[1] ^ support[2] ^ support[3]:
            continue
        for signs in itertools.product((-1,1), repeat=4):
            if signs[0]*signs[1]*signs[2]*signs[3] != -1:
                continue
            v = [0]*8
            for i,x in zip(support, signs):
                v[i] = x
            check_profile(v)
            result.append(tuple(v))
    need(len(result) == 128 and len(set(result)) == 128, "PROFILE_CENSUS")
    return result


def ell_witnesses(options, lambdas):
    # A fixed signed lambda-vector; keep a real row-pattern witness for every
    # achievable (E-D0,Z2) count, not just an energy or a formal profile.
    states = {(0,0): ()}
    for i, lam in enumerate(lambdas):
        nxt = {}
        for (d,z), rows in states.items():
            for (di,zi), row in options[i].get(lam, {}).items():
                tick()
                if d+di <= 4 and z+zi <= 6:
                    nxt.setdefault((d+di,z+zi), rows+(row,))
        states = nxt
    return states


def graph_shape(k):
    return "".join(str(x) for x in sorted(k, reverse=True))


def site_lower_bound(v, actual_ell_support):
    # zero eta makes each h-cell sum opposite. |lambda|=1 needs two
    # signed amplitude-2 sites, |lambda|=2 needs four.
    need(2*sum(abs(x) for x in v[:4]) <= actual_ell_support,
         "INSUFFICIENT_ELL_SUPPORT")


def graph_ell_relaxation(graph_data, ell_data, profiles):
    tuples = [k for k in itertools.product(range(5), repeat=4) if sum(k) <= 4]
    need(len(tuples) == 70, "LABELED_OCCUPANCY_COUNT")
    f = (0,0,0,1)  # this one sample is the packet's F, not a general f claim
    summary = {}
    witnesses = {}
    ell_cache = {}
    for v in profiles:
        check_profile(v)
        lv = v[:4]
        if lv not in ell_cache:
            ell_cache[lv] = ell_witnesses(ell_data, lv)
        for k in tuples:
            tick()
            d = 4-sum(k)
            rows = ell_cache[lv].get((d,6))
            if rows is None:
                continue
            if not all((k[i], v[4+i]) in graph_data[f[i]] for i in range(4)):
                continue
            site_lower_bound(v, 6+d)
            key = (d, graph_shape(k))
            energy = sum(x*x for x in v[4:])
            entry = summary.setdefault(key, {"profiles": set(), "graph_energies": set(),
                                             "ell_support_sizes": set(),
                                             "labeled_occupancies": set()})
            entry["profiles"].add(v)
            entry["graph_energies"].add(energy)
            entry["ell_support_sizes"].add(sum(x != 0 for x in lv))
            entry["labeled_occupancies"].add(k)
            if energy == 0 and check_profile(v) == "singleton" and key not in witnesses:
                graph_rows = []
                for i in range(4):
                    g,m = graph_data[f[i]][(k[i],v[4+i])]
                    zz = check_graph(f[i], g, m)
                    graph_rows.append({"h_graph":f[i], "graph":g, "mate":m,
                                       "all_local_eta":zz})
                witnesses[key] = {"d_E":d, "graph_occupancies":k,
                                  "lambda_ell_then_graph":v,
                                  "ell_rows_h0_then_h1":rows,
                                  "ell_local_eta":[tuple(n//4 for n in ell_transform(row))
                                                   for row in rows],
                                  "graph_rows":graph_rows}
    need(all(d % 2 == 0 for d, _shape in summary), "ODD_E_LOCAL_PARITY")
    # A genuine local physical-site pattern, not just a fabricated profile:
    # it must have all six Z2 sites, no E D0 and a graph 4 or 2+2 occupancy.
    for key in ((0,"4000"), (0,"2200")):
        need(key in witnesses, "MISSING_ELL_SINGLETON_CONTROL_"+key[1])
        v = witnesses[key]["lambda_ell_then_graph"]
        need(sum(x != 0 for x in v[:4]) == 1 and
             sum(x*x for x in v[4:]) == 0, "ELL_SINGLETON_CONTROL")
        site_lower_bound(v, 6)
    packed = {}
    for (d,shape), ent in sorted(summary.items()):
        packed[str(d)+":"+shape] = {
            "distinct_signed_lambda_profiles":len(ent["profiles"]),
            "graph_lambda_energies":sorted(ent["graph_energies"]),
            "ell_lambda_support_sizes":sorted(ent["ell_support_sizes"]),
            "labeled_graph_occupancies":len(ent["labeled_occupancies"]),
        }
    return packed, {str(d)+":"+shape:value
                    for (d,shape),value in sorted(witnesses.items())}


def verify_missing(single_sign, missing_sign):
    need(single_sign == missing_sign, "HEAVY_MISSING_SIGN")


def check_heavy(row, triple_h, missing, single_b, wrong_formula=False):
    # row contains the actual signs X/2, with four physical nonzero sites.
    triple = [b for b in range(4) if b != missing]
    need(sum(row[4*triple_h+b] != 0 for b in range(4)) == 3, "HEAVY_TRIPLE")
    need(sum(row[4*(1-triple_h)+b] != 0 for b in range(4)) == 1,
         "HEAVY_SINGLE")
    need(row[4*(1-triple_h)+single_b] != 0 and sum(row) == 0,
         "HEAVY_ZERO_ETA")
    extensions = [(c,alpha) for c in (-1,1) for alpha in range(4)
                  if all(row[4*triple_h+b] == c*chi(alpha,b) for b in triple)]
    need(len(extensions) == 1, "HEAVY_AFFINE_EXTENSION")
    c, star = extensions[0]
    need(star != 0, "HEAVY_NONCONSTANT_EXTENSION")
    verify_missing(row[4*(1-triple_h)+single_b], c*chi(star,missing))
    a = sum(row[b] for b in range(4))
    need(abs(a) == 1, "HEAVY_LAMBDA")
    p = missing if triple_h == 0 else single_b
    q = single_b if triple_h == 0 else missing
    star_numerators = []
    for alpha in range(4):
        for s in range(2):
            actual = sum(row[4*h+b]*((-1)**(s*h))*chi(alpha,b)
                         for h in range(2) for b in range(4))
            if alpha == star:
                star_numerators.append(abs(actual))
                continue
            sign = 1 if wrong_formula else -1
            proposed = a*(chi(alpha,p) + sign*((-1)**s)*chi(alpha,q))
            need(actual == proposed, "HEAVY_FOURIER_FORMULA")
    need(sorted(star_numerators) == [2,4], "HEAVY_STAR_MAGNITUDES")
    return {"a":a, "alpha_star":star, "virtual_or_actual_p":p,
            "virtual_or_actual_q":q, "missing_sign":c*chi(star,missing)}


def check_light(row, p, q, a):
    need(abs(a) == 1 and row[p] == a and row[4+q] == -a and
         sum(x != 0 for x in row) == 2, "LIGHT_SITES")
    for alpha in range(4):
        for s in range(2):
            actual = sum(row[4*h+b]*((-1)**(s*h))*chi(alpha,b)
                         for h in range(2) for b in range(4))
            need(actual == a*(chi(alpha,p)-((-1)**s)*chi(alpha,q)),
                 "LIGHT_FOURIER_FORMULA")


def heavy_cases():
    lights = []
    for i in range(4):
        cases = {}
        for p,q,a in itertools.product(range(4),range(4),(-1,1)):
            if i == 0 and (p == 0 or q == 0):
                continue
            row = [0]*8
            row[p], row[4+q] = a, -a
            check_light(row,p,q,a)
            d = 0 if i == 0 else int(p == 0)+int(q == 0)
            cases.setdefault(d, tuple(row))
        lights.append(cases)
    counts = {}
    sample = None
    for i in range(4):
        for h in range(2):
            for missing in range(4):
                triple = [b for b in range(4) if b != missing]
                for signs in itertools.product((-1,1), repeat=3):
                    if abs(sum(signs)) != 1:
                        continue
                    for single_b in range(4):
                        tick()
                        if i == 0 and (missing != 0 or single_b == 0):
                            continue  # both i=0,b=0 full sites are zero
                        row = [0]*8
                        for b,sign in zip(triple,signs):
                            row[4*h+b] = sign
                        row[4*(1-h)+single_b] = -sum(signs)
                        info = check_heavy(row,h,missing,single_b)
                        own_d = 0 if i == 0 else int(row[0] != 0)+int(row[4] != 0)
                        # Check extendability to exactly four E D0 and six Z2,
                        # preserving the actual i=0 full-block exclusions.
                        states = {(own_d, (own_d if i else 0,)): ()}
                        for j in range(4):
                            if j == i:
                                continue
                            nxt = {}
                            for (total, _), selected in states.items():
                                for dj,other in lights[j].items():
                                    if total+dj <= 4:
                                        ds = tuple(x[0] for x in selected)+((j,dj),)
                                        nxt.setdefault((total+dj, ds), selected+((j,dj,other),))
                            states = nxt
                        extensions = [selected for (total,_),selected in states.items()
                                      if total == 4]
                        if not extensions:
                            continue
                        chosen = extensions[0]
                        physical_rows = {i:tuple(row)}
                        physical_rows.update({j:r for j,_d,r in chosen})
                        d_by_i = [sum(physical_rows[j][4*hh] != 0 for hh in range(2))
                                  if j else 0 for j in range(4)]
                        need(sum(d_by_i) == 4 and
                             sum(sum(v != 0 for v in r) for r in physical_rows.values()) == 10,
                             "HEAVY_PHYSICAL_SITE_COUNTS")
                        shape = tuple(sorted(d_by_i[1:], reverse=True))
                        need(shape in ((2,2,0),(2,1,1)), "HEAVY_E_OCCUPANCY")
                        key = str(i)+":"+str(h)+":"+"".join(map(str,shape))
                        counts[key] = counts.get(key,0)+1
                        if sample is None:
                            sample = {"i":i,"triple_h":h,"missing":missing,
                                      "single_b":single_b,"row_signs":tuple(row),
                                      "derived":info,"extension_rows":physical_rows,
                                      "E_occupancies":d_by_i}
    need(sample is not None, "NO_HEAVY_PHYSICAL_SITE_PATTERNS")
    return counts, sample


def literal_x_fixture():
    # The exact X component, and only that component, displayed in packet S4.
    # It is not a full ternary u/y fixture and cannot prove the U3 hypotheses.
    f = (0,0,0,1)
    ell = [[0]*8 for _ in range(4)]
    for i,h,b,val in ((0,0,1,2),(0,0,2,-2),
                       (1,0,0,2),(1,0,1,2),(1,1,0,-2),(1,1,1,-2),
                       (2,0,0,2),(2,1,1,2),(2,0,1,-2),(2,1,0,-2)):
        ell[i][4*h+b] = val
    graph = []
    for i in range(4):
        g = tuple(chi(1,b) for b in range(4))
        mate = (0,0,0,0)
        z = check_graph(f[i],g,mate)
        graph.append((g,mate,z))
    lam = tuple(ell_transform(row)[4]//4 for row in ell)+tuple(g[2][4] for g in graph)
    need(lam == (0,2,0,0,0,0,0,0), "LITERAL_X_LAMBDA")
    check_profile(lam)
    need(sum(sum(x*x for x in row) for row in ell)+16 == 56, "LITERAL_X_ENERGY")
    d = sum(ell[i][4*h] != 0 for i in (1,2,3) for h in range(2))
    z2 = sum(ell[i][4*h+b] != 0 for i in range(4) for h in range(2)
             for b in (1,2,3))
    need((d,z2) == (4,6), "LITERAL_X_SITE_COUNTS")
    # Direct full Walsh of exactly this x, no y or fabricated ternary inverse.
    def xval(l,h,i,b):
        if l == 0:
            return ell[i][4*h+b]
        return graph[i][0 if h == f[i] else 1][b]
    spectrum = [sum(xval(l,h,i,b)*((-1)**(nu*l+s*h))*chi(beta,i)*chi(alpha,b)
                    for l in range(2) for h in range(2)
                    for i in range(4) for b in range(4))
                for nu in range(2) for s in range(2)
                for beta in range(4) for alpha in range(4)]
    return {"F":f,"t":0,"ell_rows_h0_then_h1":ell,"lambda":lam,
            "E_D0":d,"Z2":z2,"x_energy":56,
            "actual_x_walsh_cap_flag":all(abs(x) <= 8 for x in spectrum),
            "actual_x_walsh_divisibility_flag":all(x % 8 == 0 for x in spectrum),
            "actual_x_balance_at_fixture_t":spectrum[0],
            "actual_x_max_abs_walsh":max(map(abs,spectrum)),
            "scope":"literal X component only; no Y/u/Z4 chosen"}


def controls(graph_data, declared, heavy_sample):
    r = {}
    pairs = ([(12,4)]*2 + [(12,-12)]*14 + [(4,4)]*3 + [(12,12)]*13)
    check_pairs(pairs,0)
    expect_reason("residue", "U3_RESIDUE",
                  lambda: check_pairs([(0,4)]+pairs[1:],0), r)
    expect_reason("cap", "U3_CAP",
                  lambda: check_pairs([(20,4)]+pairs[1:],0), r)
    expect_reason("full_energy", "TOTAL_ENERGY_128",
                  lambda: check_pairs(pairs[:19]+[(4,4)]+pairs[20:],0), r)
    expect_reason("partial_energy", "PARTIAL_ENERGY",
                  lambda: check_pairs(pairs[:2]+[(12,12)]+pairs[3:],0), r)
    expect_reason("pair_count", "PAIR_COUNT", lambda: check_pairs(pairs[:-1],0), r)
    expect_reason("small_census_parity", "SMALL_CENSUS",
                  lambda: check_census((5,0,12,15,0,1),0), r)
    expect_reason("h_bound", "H_BOUND",
                  lambda: check_census((0,2,14,16,3,0),0), r)
    expect_reason("z4_bound", "Z4_BOUND",
                  lambda: check_census((0,0,31,1,0,2),0), r)
    altered = set(declared[0])
    altered.remove((0,2,14,16))
    expect_reason("declared_table", "DECLARED_TABLE_MISMATCH",
                  lambda: compare_declared(declared[0], altered), r)
    expect_reason("graph_value", "GRAPH_VALUE",
                  lambda: check_graph(0,(0,1,-1,-1),(0,0,0,0)), r)
    expect_reason("mate_value", "MATE_VALUE",
                  lambda: check_graph(0,(1,1,-1,-1),(1,0,0,0)), r)
    expect_reason("graph_zero_eta", "ZERO_ETA",
                  lambda: check_graph(0,(1,1,1,1),(0,0,0,0)), r)
    expect_reason("lambda_energy", "LAMBDA_ENERGY",
                  lambda: check_profile((2,2,0,0,0,0,0,0)), r)
    expect_reason("lambda_nonflat", "LAMBDA_NONFLAT",
                  lambda: check_profile((-1,1,1,0,1,0,0,0)), r)
    expect_reason("lambda_sign_product", "LAMBDA_SIGN_PRODUCT",
                  lambda: check_profile((1,1,1,1,0,0,0,0)), r)
    four_ell = (-1,1,1,1,0,0,0,0)
    check_profile(four_ell)
    expect_reason("four_ell_needs_eight_sites", "INSUFFICIENT_ELL_SUPPORT",
                  lambda: site_lower_bound(four_ell,6), r)
    single_ell = (2,0,0,0,0,0,0,0)
    need(check_profile(single_ell) == "singleton", "SINGLETON_PROFILE_CONTROL")
    site_lower_bound(single_ell,6)
    row = heavy_sample["row_signs"]
    expect_reason("heavy_virtual_sign", "HEAVY_MISSING_SIGN",
                  lambda: verify_missing(1,-1), r)
    expect_reason("heavy_wrong_fourier_sign", "HEAVY_FOURIER_FORMULA",
                  lambda: check_heavy(row,heavy_sample["triple_h"],
                                      heavy_sample["missing"],
                                      heavy_sample["single_b"],True), r)
    return r


def main():
    integer, comparisons, signatures, declared = integer_census()
    graph_data, graph_summary = graph_cases()
    ell_data, ell_counts = ell_options()
    profiles = all_profiles()
    local, witnesses = graph_ell_relaxation(graph_data, ell_data, profiles)
    heavy, sample = heavy_cases()
    fixture = literal_x_fixture()
    negative_controls = controls(graph_data, declared, sample)
    need(time.monotonic() < DEADLINE, "COOPERATIVE_DEADLINE_FINAL")
    mismatch = any(not item["match"] for item in comparisons.values())
    return {
        "status": "COMPLETE_DECLARED_TABLE_MISMATCH" if mismatch else "COMPLETE_FINITE_SCOPE_ONLY",
        "not_tested_in_child": True,
        "table_pair_signatures": signatures,
        "six_tuple_order": ["E","O","P","Z","H","Z4"],
        "all_d_0_through_4": integer,
        "f748_even_d_projection_comparisons":comparisons,
        "graph_local_F_0_and_1":graph_summary,
        "ell_zero_eta_and_local_cap_row_counts":ell_counts,
        "lambda_profiles":len(profiles),
        "local_lambda_relaxation":local,
        "ell_singleton_actual_site_pattern_examples":witnesses,
        "heavy_patterns_by_actual_row_h_and_E_occupancy":heavy,
        "one_heavy_site_pattern":sample,
        "literal_packet_x_component_fixture":fixture,
        "reason_specific_controls":negative_controls,
        "elapsed_seconds":time.monotonic()-START,
        "scope": [
            "All six-count pair types are exact consequences of full U3 residue/cap and 128 energy plus ell1 partial energy 64+4*d; arbitrary pairing multiplicities are necessary spectra, not constructed spatial Y.",
            "Graph checks cover every four-site sign/mate pattern and both graph h bits; ell-side enumeration uses the actual two F sites, six E sites, six Z2 and all local eta bounds, but assembles only the lambda global profile.",
            "Graph and ell examples are necessary local relaxations, not full seven-profile or full physical ternary witnesses. No all-kappa or arbitrary phase assumption is made.",
            "The singleton control distinguishes the admissible E-side plus/minus 2 profile from four E-side plus/minus 1 entries. It does not disprove f748 under its complete hypotheses.",
            "Heavy Fourier formula is checked only for actual zero-mean 3+1 site rows, in both orientations, all sign patterns and characters other than their nonconstant affine extension, with actual E/F location and d_E=4 site-count extendability; the virtual missing coordinate is never an occupied site.",
            "No simultaneous seven full columns, common physical Y/U3 cap, full inverse, J, V, original caller, family, kernel, human or novelty assurance. The literal fixture is only the X component specified in the packet."
        ]}


try:
    result = main()
except Incomplete as exc:
    result = {"status":"INCOMPLETE", "reason":str(exc)}
except Reject as exc:
    result = {"status":"INCOMPLETE", "reason":exc.reason}
except Exception as exc:
    result = {"status":"INCOMPLETE", "reason":"UNEXPECTED_"+type(exc).__name__,
              "detail":str(exc)}
sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":"))+"\n")
sys.stdout.flush()
if result["status"] != "COMPLETE_FINITE_SCOPE_ONLY":
    sys.exit(1)
