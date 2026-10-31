#!/usr/bin/env python3
"""Unexecuted F781 exact local checker; parent-only admission after whole read.

No arguments, input files, output files, network, subprocesses, deletion, or
non-stdlib dependencies. The only stream output is the final JSON on stdout.
The 44-second cooperative deadline is internal; a separate parent supervisor
must provide the <=55-second external limit and preserve the actual JSON status.
This is a local finite conditional assay, not an f/R, common-Y or caller test.
"""

import itertools
import json
import signal
import sys
import time

SECONDS = 44.0
START = time.monotonic()
INTERRUPTED = None
RESULT = {
    "status": "IN_PROGRESS",
    "budget": {"cooperative_seconds": SECONDS, "external_seconds_parent_only": 55},
    "scope": "finite local X/profile and conditional 22 reconstruction only",
    "f_R_phase": "NOT_DEFINED_FOR_THE_THREE_LITERAL_FIXTURES; NOT_TESTED",
    "not_tested": ["actual f/R and common phase existence", "common physical Y/J1/U3 caps",
                   "full ternary inverse, V, actual selected T and original caller",
                   "d_E=2 and d_E=4", "global rank-two or NL242 exclusion",
                   "exhaustive simultaneous seven-profile 2110 enumeration",
                   "parent disposition, human, model-family or kernel verification"],
    "stages": {},
}
CURRENT = None


class Stop(Exception):
    pass


class Failure(Exception):
    def __init__(self, reason, detail=None):
        self.reason = reason
        self.detail = detail
        super().__init__(reason)


def on_signal(signum, _frame):
    global INTERRUPTED
    INTERRUPTED = signum


signal.signal(signal.SIGINT, on_signal)
signal.signal(signal.SIGTERM, on_signal)


def checkpoint():
    if INTERRUPTED is not None:
        raise Stop("signal_%d" % INTERRUPTED)
    if time.monotonic() - START >= SECONDS:
        raise Stop("cooperative_deadline")


def need(condition, reason, detail=None):
    if not condition:
        raise Failure(reason, detail)


def xor_all(items):
    value = 0
    for item in items:
        value ^= item
    return value


def dot(a, b):
    x = a & b
    return (x & 1) ^ ((x >> 1) & 1)


def chi(a, b):
    return -1 if dot(a, b) else 1


def swap(v):
    return ((v & 1) << 1) | ((v >> 1) & 1)


def point(gamma):
    return tuple(1 if b == gamma else -1 for b in range(4))


def character(sign, covector):
    return tuple(sign * chi(covector, b) for b in range(4))


def covector(S):
    found = [a for a in range(4) if all(S[b] == S[0] * chi(a, b) for b in range(4))]
    need(len(found) == 1, "CHARACTER_RECONSTRUCTION", list(S))
    return found[0]


def odd_exception(S):
    found = [b for b in range(4) if all(S[c] == -S[b] for c in range(4) if c != b)]
    need(len(found) == 1, "ODD_EXCEPTION", list(S))
    return found[0]


def row_values(S, d, F):
    out = {}
    for s in range(2):
        for a in range(4):
            n = sum((S[b] + 2 * ((-1) ** s) * d[b]) * chi(a, b) for b in range(4))
            n *= (-1) ** (s * F)
            if n % 4:
                return None
            out[s, a] = n // 4
    return out


def row_guard(S, d, F):
    if sum(S) + 2 * sum(d) != 0:
        return "ROW_ZERO"
    values = row_values(S, d, F)
    if values is None:
        return "ROW_INTEGRALITY"
    if any(abs(v) > 2 for v in values.values()):
        return "ROW_CAP"
    return "OK"


def profile_guard(z):
    if len(z) != 8 or any(not isinstance(v, int) for v in z):
        return "PROFILE_TYPE"
    if sum(v * v for v in z) != 4:
        return "PROFILE_ENERGY"
    nz = [i for i, v in enumerate(z) if v]
    if len(nz) == 1:
        return "OK" if abs(z[nz[0]]) == 2 else "PROFILE_SINGLETON"
    if len(nz) != 4 or any(abs(z[i]) != 1 for i in nz):
        return "PROFILE_SHAPE"
    if xor_all(nz):
        return "PROFILE_NONFLAT"
    prod = 1
    for i in nz:
        prod *= z[i]
    return "OK" if prod == -1 else "PROFILE_SIGN_PRODUCT"


def ratio_guard(r0, r1):
    return "OK" if abs(r0) == abs(r1) == 1 and r0 == -r1 else "EXTENSION_RATIO"


def ix(ell, h, i, b):
    return (((2 * ell + h) * 4 + i) * 4 + b)


def make_array(F, S, mates, e_sites):
    X = [0] * 64
    for i in range(4):
        for b in range(4):
            X[ix(1, F[i], i, b)] = S[i][b]
        for b, sign in mates[i].items():
            X[ix(1, 1 - F[i], i, b)] = 2 * sign
    for h, i, b, value in e_sites:
        X[ix(0, h, i, b)] = value
    return X


def local_guard(X, F, z4):
    if len(X) != 64 or len(F) != 4 or any(f not in (0, 1) for f in F):
        return "ARRAY_SHAPE"
    if sum(F) % 2 != 1:
        return "GRAPH_F_PARITY"
    if any(abs(X[ix(1, F[i], i, b)]) != 1 for i in range(4) for b in range(4)):
        return "GRAPH_VALUE"
    if any(X[ix(1, 1-F[i], i, b)] not in (-2, 0, 2) for i in range(4) for b in range(4)):
        return "MATE_VALUE"
    if sum(X[ix(1, 1-F[i], i, b)] != 0 for i in range(4) for b in range(4)) != 4:
        return "GRAPH_D0_COUNT"
    if any(X[ix(0, h, i, 0)] != 0 for h in range(2) for i in range(4)):
        return "E_B0_VALUE"
    if any(X[ix(0, h, i, b)] not in (-2, 0, 2) for h in range(2) for i in range(4) for b in (1, 2, 3)):
        return "E_VALUE"
    if sum(X[ix(0, h, i, b)] != 0 for h in range(2) for i in range(4) for b in (1, 2, 3)) != 6:
        return "Z2_COUNT"
    h, i, b = z4
    if h not in (0, 1) or i not in range(4) or b not in (1, 2, 3):
        return "Z4_SITE"
    if X[ix(0, h, i, b)] != 0:
        return "Z4_OVERLAP"
    for i in range(4):
        if sum(X[ix(0, h, i, b)] for h in range(2) for b in range(4)) != 0:
            return "E_ROW_ZERO"
        if sum(X[ix(1, h, i, b)] for h in range(2) for b in range(4)) != 0:
            return "GRAPH_ROW_ZERO"
    return "OK"


def entries(items):
    z = [0] * 8
    for ell, i, value in items:
        need(z[4 * ell + i] == 0, "DUPLICATE_EXPECTED_ENTRY")
        z[4 * ell + i] = value
    return z


def fixtures():
    # Binary integer 2 denotes the written bit pair 10; 1 denotes 01.
    # F764 uses A=00, B=10, C=01, D=11. F765 uses A=00,B=01,C=10,D=11.
    return [
        {
            "name": "f764-I-3100", "F": (0, 0, 0, 1),
            "S": (point(2), character(-1, 1), point(0), character(-1, 3)),
            "mates": ({2: 1, 1: -1, 3: 1}, {}, {3: 1}, {}),
            "E": ((0, 0, 2, 2), (1, 0, 3, -2), (0, 2, 2, -2),
                  (1, 2, 2, 2), (1, 1, 2, 2), (1, 1, 3, -2)),
            "expected": {
                (1, 0): [(1,0,-1),(1,2,-1),(0,0,1),(0,2,-1)],
                (0, 2): [(1,0,-2)],
                (1, 2): [(1,0,1),(1,2,1),(0,0,-1),(0,2,1)],
                (0, 1): [(1,0,1),(1,1,-1),(0,0,1),(0,1,1)],
                (1, 1): [(1,2,1),(1,1,-1),(0,2,-1),(0,1,-1)],
                (0, 3): [(1,2,1),(1,3,-1),(0,0,-1),(0,1,-1)],
                (1, 3): [(1,0,-1),(1,3,1),(0,2,1),(0,1,1)],
            },
        },
        {
            "name": "f764-II-2110-N", "F": (0, 0, 0, 1),
            "S": (point(0), character(1, 2), point(0), character(-1, 2)),
            "mates": ({0: 1}, {0: 1, 1: -1}, {1: 1}, {}),
            "E": ((0, 0, 2, 2), (1, 0, 3, -2), (0, 2, 2, -2),
                  (1, 2, 2, 2), (0, 1, 2, -2), (0, 1, 3, 2)),
            "expected": {
                (1, 0): [(1,0,-1),(1,2,-1),(0,0,1),(0,2,-1)],
                (0, 2): [(1,0,1),(1,2,1),(1,1,1),(1,3,-1)],
                (1, 2): [(1,1,1),(1,3,1),(0,0,-1),(0,2,1)],
                (0, 1): [(1,0,1),(1,1,1),(0,0,1),(0,1,-1)],
                (1, 1): [(1,2,1),(1,1,-1),(0,2,-1),(0,1,-1)],
                (0, 3): [(1,0,1),(1,1,1),(0,0,-1),(0,1,1)],
                (1, 3): [(1,2,1),(1,1,-1),(0,2,1),(0,1,1)],
            },
        },
        {
            "name": "f765-3100", "F": (1, 0, 0, 0),
            "S": (point(2), point(0), character(1, 2), character(-1, 3)),
            "mates": ({1: 1, 2: -1, 3: 1}, {0: 1}, {}, {}),
            "E": ((0, 0, 2, 2), (1, 0, 3, -2), (0, 1, 2, 2),
                  (1, 1, 1, -2), (0, 2, 1, 2), (0, 2, 3, -2)),
            "expected": {
                (1, 0): [(1,0,1),(1,1,-1),(0,0,1),(0,1,1)],
                (0, 1): [(1,0,-1),(1,1,1),(0,0,1),(0,1,1)],
                (1, 1): [(1,0,-2)],
                (0, 2): [(1,1,1),(1,2,1),(0,1,-1),(0,2,1)],
                (1, 2): [(1,0,1),(1,2,1),(0,0,-1),(0,2,1)],
                (0, 3): [(1,1,1),(1,3,-1),(0,0,-1),(0,2,-1)],
                (1, 3): [(1,0,1),(1,3,-1),(0,1,-1),(0,2,-1)],
            },
        },
    ]


def profile(X, s, a):
    ans = []
    for ell in range(2):
        for i in range(4):
            n = sum(X[ix(ell,h,i,b)] * ((-1) ** (s*h)) * chi(a,b)
                    for h in range(2) for b in range(4))
            need(n % 4 == 0, "PROFILE_INTEGRALITY", [ell, i, s, a, n])
            ans.append(n // 4)
    return ans


def direct_walsh(X, nu, s, beta, alpha):
    return sum(X[ix(ell,h,i,b)] * ((-1) ** (nu*ell + s*h + dot(beta,i) + dot(alpha,b)))
               for ell in range(2) for h in range(2) for i in range(4) for b in range(4))


def row_signature(S, d):
    k = sum(value != 0 for value in d)
    P = xor_all(b for b in range(4) if S[b] == -1)
    D = xor_all(b for b in range(4) if d[b] != 0)
    return k, P, D


def verify_row(S, d, F, values, stats):
    k, P, D = row_signature(S, d)
    stats["accepted_by_k"][k] += 1
    need(values[0,0] == 0 and values[1,0] == -((-1) ** F) * sum(d), "ROW_LAMBDA")
    for alpha in (1,2,3):
        need((values[0,alpha] & 1) == (1 ^ dot(alpha, P ^ D)), "ROW_30",
             {"F":F,"S":S,"d":d,"alpha":alpha})
    if k % 2 == 0:
        xi = covector(S)
        need(P == swap(xi), "EVEN_NEGATIVE_XOR")
        gamma = None
    else:
        gamma = odd_exception(S)
        need(P == gamma, "ODD_NEGATIVE_XOR")
        xi = None
    for lam in range(4):
        phase = (lam ^ xi) if k % 2 == 0 else (lam ^ 3 ^ swap(gamma))
        need(phase == (lam ^ swap(P) ^ (3 if k % 2 else 0)), "ROW_31")
        stats["phase_row_checks"] += 1
    if k == 0:
        need(xi != 0 and values[1,0] == 0, "K0_LAMBDA")
        for a in (1,2,3):
            need(all(abs(values[s,a]) == (1 if a == xi else 0) for s in range(2)), "K0_PATTERN")
        name = "k0"
    elif k in (1,3):
        epsilon = S[gamma]
        occupied = [b for b in range(4) if d[b]]
        if k == 1:
            u = occupied[0]
            need(d[u] == epsilon, "K1_SIGN")
            special = None
        else:
            u = next(b for b in range(4) if not d[b])
            minority = [b for b in occupied if d[b] == -epsilon]
            need(len(minority) == 1 and sum(d) == epsilon, "K3_SIGNS")
            special = swap(u ^ minority[0])
        need(abs(values[1,0]) == 1, "ODD_ROW_LAMBDA")
        delta = gamma ^ u
        for a in (1,2,3):
            main = dot(a,delta)
            need(abs(values[main,a]) == 1, "ODD_ROW_MAIN")
            need(abs(values[1-main,a]) == (2 if special == a else 0), "ODD_ROW_OTHER")
        name = "k%d" % k
    elif k == 2:
        occupied = [b for b in range(4) if d[b]]
        u,v = occupied
        a = swap(u ^ v)
        if d[u] == d[v]:
            need(xi == 0 and abs(values[1,0]) == 2, "K2_ACTIVE_LAMBDA")
            for alpha in (1,2,3):
                need(all(abs(values[s,alpha]) == (1 if alpha == a else 0) for s in range(2)), "K2_ACTIVE")
            name = "k2_active"
        elif xi == a:
            need(values[1,0] == 0, "K2_N_LAMBDA")
            for alpha in (1,2,3):
                need(all(abs(values[s,alpha]) == 1 for s in range(2)), "K2_N")
            name = "k2_N"
        else:
            need(xi not in (0,a) and values[1,0] == 0, "K2_O_LAMBDA")
            for alpha in (1,2,3):
                got = sorted(abs(values[s,alpha]) for s in range(2))
                want = [0,2] if alpha == xi else ([0,0] if alpha == a else [1,1])
                need(got == want, "K2_O", [alpha,got,want])
            name = "k2_O"
    elif k == 4:
        if sum(d):
            need(xi == 0 and abs(values[1,0]) == 2, "K4_ACTIVE_LAMBDA")
            for a in (1,2,3):
                need(all(abs(values[s,a]) == 1 for s in range(2)), "K4_ACTIVE")
            name = "k4_active"
        else:
            a = covector(d)
            need(a != 0 and xi not in (0,a) and values[1,0] == 0, "K4_INACTIVE_LAMBDA")
            for alpha in (1,2,3):
                target = 2 if alpha == a else (1 if alpha == xi else 0)
                need(all(abs(values[s,alpha]) == target for s in range(2)), "K4_INACTIVE")
            name = "k4_inactive"
    else:
        raise Failure("INVALID_K")
    stats["branches"][name] = stats["branches"].get(name,0) + 1


def stage_one_rows(stats):
    stats.update({"raw_per_F":1296,"F_values":[0,1],"accepted_by_k":[0]*5,
                  "branches":{},"phase_row_checks":0,"three_nonzero_alpha_per_row":True})
    for F in range(2):
        for S in itertools.product((-1,1), repeat=4):
            for d in itertools.product((-1,0,1), repeat=4):
                checkpoint()
                if row_guard(S,d,F) != "OK":
                    continue
                verify_row(S,d,F,row_values(S,d,F),stats)
    need(stats["accepted_by_k"] == [12,64,168,192,64], "ROW_COUNTS", stats["accepted_by_k"])
    need(sum(stats["accepted_by_k"]) == 500, "ROW_TOTAL")
    stats["quantifier"] = "all 2*16*81 raw one-row S,D,F; accepted rows checked at every alpha and extension"


def stage_flats(stats):
    flats = 0
    valid = 0
    sign_mutants = 0
    for supp in itertools.combinations(range(8),4):
        checkpoint()
        if xor_all(supp):
            continue
        flats += 1
        need(sum(q >= 4 for q in supp) % 2 == 0, "FLAT_GRAPH_PARITY", supp)
        for signs in itertools.product((-1,1),repeat=4):
            z = [0]*8
            for q,v in zip(supp,signs):
                z[q] = v
            product_sign = signs[0]*signs[1]*signs[2]*signs[3]
            reason = profile_guard(z)
            if product_sign == -1:
                need(reason == "OK", "VALID_FLAT_REJECTED")
                valid += 1
            else:
                need(reason == "PROFILE_SIGN_PRODUCT", "BAD_FLAT_ACCEPTED")
                sign_mutants += 1
    for q in range(8):
        for sign in (-2,2):
            z = [0]*8
            z[q] = sign
            need(profile_guard(z) == "OK", "SINGLETON_REJECTED")
    need((flats,valid,sign_mutants) == (14,112,112), "FLAT_COUNTS")
    stats.update({"affine_flats":flats,"valid_signed_flats":valid,"bad_signings_rejected":sign_mutants,
                  "singletons":16,
                  "implication":"each flat meets graph half evenly; local (3.0) plus XOR linearity gives global (3.0); local phase identity plus even odd-row count and XOR(lambda)=0 gives (3.1)",
                  "not_claimed":"no exhaustive global seven-profile 2110 census"})


def stage_fixtures(stats):
    results = []
    for model in fixtures():
        checkpoint()
        F,S,mates = model["F"],model["S"],model["mates"]
        X = make_array(F,S,mates,model["E"])
        z4 = (0,3,1)  # Explicit local designation; f764 did not specify a Z4 site.
        need(local_guard(X,F,z4) == "OK", "FIXTURE_LOCAL", model["name"])
        need(sum(x*x for x in X) == 56, "FIXTURE_ENERGY", model["name"])
        profiles = {}
        need(profile(X,0,0) == [0]*8, "FIXTURE_ZERO_PROFILE", model["name"])
        for s in range(2):
            for a in range(4):
                if (s,a) == (0,0):
                    continue
                actual = profile(X,s,a)
                expected = entries(model["expected"][s,a])
                need(actual == expected, "FIXTURE_LITERAL_TABLE", [model["name"],s,a,actual,expected])
                need(profile_guard(actual) == "OK", "FIXTURE_PROFILE", [model["name"],s,a])
                profiles["%d,%d" % (s,a)] = actual
        walsh = []
        for nu,s,beta,alpha in itertools.product(range(2),range(2),range(4),range(4)):
            value = direct_walsh(X,nu,s,beta,alpha)
            need(value % 8 == 0 and abs(value) <= 8, "FIXTURE_DIRECT_WALSH", [model["name"],nu,s,beta,alpha,value])
            need((value == 0) == (s == 0 and alpha == 0), "FIXTURE_WALSH_ZERO_FLAT")
            walsh.append([nu,s,beta,alpha,value])
        P = []
        B = 0
        odd = []
        xi = []
        for i in range(4):
            d = tuple(mates[i].get(b,0) for b in range(4))
            k,p,di = row_signature(S[i],d)
            P.append(p)
            B ^= di
            if k % 2:
                gamma = odd_exception(S[i])
                u = next(b for b in range(4) if (d[b] != 0) == (k == 1))
                odd.append([i,gamma ^ u])
                xi.append(None)
            else:
                xi.append(covector(S[i]))
        need(xor_all(P) == B, "FIXTURE_30", model["name"])
        phase_tables = 0
        for lam in itertools.product(range(4),repeat=4):
            if xor_all(lam):
                continue
            left = 0
            for i in range(4):
                left ^= (lam[i] ^ xi[i]) if xi[i] is not None else (lam[i] ^ 3 ^ swap(P[i]))
            need(left == swap(B), "FIXTURE_31", [model["name"],lam])
            phase_tables += 1
        need(phase_tables == 64, "PHASE_TABLE_COUNT")
        if model["name"] == "f764-I-3100":
            need(odd == [[0,2],[2,3]] and xi[1] == 1 and xi[3] == 3, "FIRST_DISCRIMINATOR")
        elif model["name"] == "f764-II-2110-N":
            need(odd == [[0,0],[2,1]] and xi[1] == swap(0 ^ 1), "N_DISCRIMINATOR")
        else:
            need(odd == [[0,2],[1,0]] and xi[2] == 2 and xi[3] == 3, "THIRD_DISCRIMINATOR")
        results.append({"name":model["name"],"F":F,"odd_offsets_by_i":odd,"even_row_covectors":xi,
                        "B_D":B,"P_xor":xor_all(P),"symbolic_zero_xor_lambda_tables":phase_tables,
                        "zero_profile":[0]*8,"seven_profiles":profiles,"direct_64_walsh":walsh,
                        "counts_local_designation":{"graph_S":16,"graph_D0":4,"graph_D3":12,
                            "E_D3":6,"Z2":6,"Z4":1,"Z0":17,"F":2,"energy_X":56},
                        "Z4_site_h_i_b":z4,
                        "qualification":"X and local type designation only; not a common Y, f/R, or physical-caller witness"})
    stats["examples"] = results
    stats["coverage"] = "all three literal X arrays; 7 simultaneous profiles plus zero, 64 direct Walsh each"


def stage_controls(stats):
    observations = {}
    def control(name, observed, expected):
        need(observed == expected, "CONTROL_WRONG_REASON", [name,observed,expected])
        observations[name] = {"observed":observed,"expected":expected,"status":"PASS"}
    model = fixtures()[0]
    X = make_array(model["F"],model["S"],model["mates"],model["E"])
    F = model["F"]
    control("baseline_local",local_guard(X,F,(0,3,1)),"OK")
    bad = list(X)
    bad[ix(1,F[0],0,0)] = 0
    control("graph_value",local_guard(bad,F,(0,3,1)),"GRAPH_VALUE")
    bad = list(X)
    bad[ix(0,0,0,2)] = 0
    control("z2_count",local_guard(bad,F,(0,3,1)),"Z2_COUNT")
    control("z4_overlap",local_guard(X,F,(0,0,2)),"Z4_OVERLAP")
    bad = list(X)
    bad[ix(0,1,0,3)] = 2
    control("ell0_row_zero",local_guard(bad,F,(0,3,1)),"E_ROW_ZERO")
    control("row_zero",row_guard((1,1,1,1),(0,0,0,0),0),"ROW_ZERO")
    control("valid_singleton",profile_guard([2,0,0,0,0,0,0,0]),"OK")
    control("energy",profile_guard([2,2,0,0,0,0,0,0]),"PROFILE_ENERGY")
    control("nonflat",profile_guard([1,1,1,0,-1,0,0,0]),"PROFILE_NONFLAT")
    control("sign_product",profile_guard([1,1,1,1,0,0,0,0]),"PROFILE_SIGN_PRODUCT")
    control("ratio_mutant",ratio_guard(1,1),"EXTENSION_RATIO")
    control("ratio_valid",ratio_guard(1,-1),"OK")
    stats["controls"] = observations


def site_options(epsilon, target):
    options = []
    for y0,y1 in itertools.product((0,-2,2,-4,4),repeat=2):
        if (abs(y0) == 4) + (abs(y1) == 4) > 1:
            continue
        if y0 + epsilon*y1 == target:
            options.append((y0,y1))
    return options


def z2_coefficient(sites, signs, row, s, alpha):
    n = sum(2*sign * ((-1) ** (s*h)) * chi(alpha,b)
            for (i,b,h),sign in zip(sites,signs) if i == row)
    need(n % 4 == 0, "DERIVED22_PROFILE_INTEGRALITY")
    return n//4


def stage_22(stats):
    stats.update({"site_option_checks":0,"label_flat_checks":0,"N_graph_checks":0,
                  "layouts_started":0,"Y_sign_completions_checked":0,"X_sign_assignments_checked":0,
                  "rowzero_candidates":0,"lambda_candidates":0,"ratio_checks":0,
                  "conditional_not_forcing":True})
    # Independently enumerate possible two-h local Y values at a B=0 or B=+/-2 site.
    for eps in (-1,1):
        for target in (0,-2,2):
            for y0,y1 in site_options(eps,target):
                stats["site_option_checks"] += 1
                n2 = (abs(y0)==2) + (abs(y1)==2)
                n4 = (abs(y0)==4) + (abs(y1)==4)
                if target == 0:
                    need((n2,n4) in ((0,0),(2,0)), "BZERO_SITE_CLASS")
                else:
                    need((n2,n4) in ((1,0),(1,1)), "B2_SITE_CLASS")
    # All distinct quotient labels: graph/ell0 support is a flat iff pair differences match.
    for U in range(4):
        for V in range(4):
            if U == V:
                continue
            for A,B in itertools.combinations(range(4),2):
                support = (U,V,4+A,4+B)
                need((xor_all(support) == 0) == ((U ^ V) == (A ^ B)), "QUOTIENT_FLAT")
                stats["label_flat_checks"] += 1
    # Every N-type graph row, including F and both independent signed factors.
    for delta in (1,2,3):
        a = swap(delta)
        others = [v for v in (1,2,3) if v != a]
        for u in range(4):
            v = u ^ delta
            for F,sgnS,sgnD in itertools.product(range(2),(-1,1),(-1,1)):
                d = [0]*4
                d[u],d[v] = sgnD,-sgnD
                S = character(sgnS,a)
                vals = row_values(S,d,F)
                need(vals is not None and row_guard(S,d,F) == "OK", "N_GRAPH_ROW")
                for alpha in others:
                    need(abs(vals[0,alpha]) == abs(vals[1,alpha]) == 1, "N_GRAPH_ODD")
                    need(vals[0,alpha]*vals[1,alpha] == (-1)**(F+1), "N_GRAPH_RATIO")
                    stats["N_graph_checks"] += 1
    # Canonical distinct U=0,V=1; all label pairs were checked above.  Affine
    # quotient relabeling preserves equality of pair differences; no physical
    # f/R or Y forcing is inferred from that relabeling.
    U,V = 0,1
    for delta in (1,2,3):
        a = swap(delta)
        p,q = [b for b in (1,2,3) if b != delta]
        need((p ^ q) == delta, "PAIR_GEOMETRY")
        support = [(U,p),(U,q),(V,p),(V,q)]
        zero_cols = [(i,b) for i in range(4) for b in (1,2,3) if (i,b) not in support]
        for zindex in range(4):
            for h4 in range(2):
                for bits in range(8):
                    for ci,cb in zero_cols:
                        checkpoint()
                        stats["layouts_started"] += 1
                        z4site = (support[zindex][0],support[zindex][1],h4)
                        sites = []
                        j = 0
                        for index,(i,b) in enumerate(support):
                            if index == zindex:
                                h = 1-h4
                            else:
                                h = (bits >> j) & 1
                                j += 1
                            sites.append((i,b,h))
                        sites += [(ci,cb,0),(ci,cb,1)]
                        need(len(set(sites)) == 6 and z4site not in sites, "LAYOUT_DISTINCT")
                        for s,P,sgnU,sgnV,cancel in itertools.product(range(2),(-1,1),(-1,1),(-1,1),(-1,1)):
                            eps = (-1)**s
                            target = {(U,p):2*sgnU,(U,q):2*sgnU*P,
                                      (V,p):2*sgnV,(V,q):2*sgnV*P}
                            y = {}
                            for index,(i,b) in enumerate(support):
                                val = target[i,b]
                                if index == zindex:
                                    h = z4site[2]
                                    y[i,b,h] = 2*val*(eps if h else 1)
                                    hh = 1-h
                                    y[i,b,hh] = -val*(eps if hh else 1)
                                else:
                                    h = sites[index][2]
                                    y[i,b,h] = val*(eps if h else 1)
                            y[ci,cb,0] = 2*cancel
                            y[ci,cb,1] = -2*cancel*eps
                            need(sum(abs(v)==2 for v in y.values()) == 6 and
                                 sum(abs(v)==4 for v in y.values()) == 1, "Y_PHYSICAL_COUNTS")
                            for i in range(4):
                                for b in (1,2,3):
                                    got = y.get((i,b,0),0) + eps*y.get((i,b,1),0)
                                    need(got == target.get((i,b),0), "B_RECONSTRUCTION")
                            stats["Y_sign_completions_checked"] += 1
                        for signs in itertools.product((-1,1),repeat=6):
                            stats["X_sign_assignments_checked"] += 1
                            totals = [sum(2*t for (i,b,h),t in zip(sites,signs) if i == row) for row in range(4)]
                            if any(totals):
                                continue
                            stats["rowzero_candidates"] += 1
                            nums = [sum(2*t*((-1)**h) for (i,b,h),t in zip(sites,signs) if i == row) for row in range(4)]
                            need(all(n % 4 == 0 for n in nums), "LAMBDA_INTEGRALITY")
                            lambdas = [n//4 for n in nums]
                            if ci not in (U,V):
                                need(abs(lambdas[ci]) == 1, "THIRD_ROW_PAIR_LAMBDA")
                            if any(abs(x) not in (0,2) for x in lambdas) or sum(x != 0 for x in lambdas) > 1:
                                continue
                            stats["lambda_candidates"] += 1
                            need(ci in (U,V) and cb == delta, "CANCELLING_PAIR_LOCATION")
                            heavy = ci
                            light = V if heavy == U else U
                            alphas = [x for x in (1,2,3) if x != a]
                            ur = []
                            vr = []
                            for alpha in alphas:
                                u0 = z2_coefficient(sites,signs,heavy,0,alpha)
                                u1 = z2_coefficient(sites,signs,heavy,1,alpha)
                                v0 = z2_coefficient(sites,signs,light,0,alpha)
                                v1 = z2_coefficient(sites,signs,light,1,alpha)
                                need(abs(u0)==abs(u1)==abs(v0)==abs(v1)==1, "DERIVED22_ODD_PROFILE")
                                ur.append(u0*u1)
                                vr.append(v0*v1)
                            need(ratio_guard(ur[0],ur[1]) == "OK" and vr[0] == vr[1], "DERIVED22_RATIO")
                            ua = [abs(z2_coefficient(sites,signs,heavy,s,a)) for s in range(2)]
                            va = [z2_coefficient(sites,signs,light,s,a) for s in range(2)]
                            need((sorted(ua) == [0,2] if lambdas[heavy] == 0 else ua == [0,0]) and va == [0,0],
                                 "DERIVED22_SPECIAL_ALPHA")
                            for graph_ratio_product in (-1,1):
                                r0 = ur[0]*vr[0]*graph_ratio_product
                                r1 = ur[1]*vr[1]*graph_ratio_product
                                need(r0*r1 == -1, "DERIVED22_SIGN_PRODUCT_CONTRADICTION")
                                stats["ratio_checks"] += 1
    need(stats["lambda_candidates"] > 0 and stats["ratio_checks"] > 0, "DERIVED22_VACUOUS")
    stats["scope"] = ("conditional on the supplied B support, physical site types, X row zero and singleton lambda; "
                      "all canonical local layouts and signs, all b differences and quotient-label flat checks; "
                      "does not derive B from U3 or force it from any fixture")


def run_stage(name, function):
    global CURRENT
    CURRENT = name
    stats = {"status":"RUNNING"}
    RESULT["stages"][name] = stats
    checkpoint()
    function(stats)
    stats["status"] = "COMPLETE"


def main():
    exit_code = 0
    try:
        run_stage("literal_X_countermodels",stage_fixtures)
        run_stage("all_one_row_patterns",stage_one_rows)
        run_stage("all_affine_odd_supports_and_parity",stage_flats)
        run_stage("reason_specific_mutants",stage_controls)
        run_stage("conditional_physical_22",stage_22)
        RESULT["status"] = "COMPLETE_FINITE_LOCAL_SCOPES_ONLY"
    except Stop as exc:
        RESULT["status"] = "PARTIAL_COOPERATIVE_DEADLINE" if INTERRUPTED is None else "PARTIAL_SIGNAL"
        RESULT["stop_reason"] = str(exc)
        if CURRENT is not None:
            RESULT["stages"][CURRENT]["status"] = "PARTIAL"
        exit_code = 2
    except Failure as exc:
        RESULT["status"] = "FAIL"
        RESULT["failure"] = {"stage":CURRENT,"reason":exc.reason,"detail":exc.detail}
        if CURRENT is not None:
            RESULT["stages"][CURRENT]["status"] = "FAIL"
        exit_code = 1
    except Exception as exc:
        RESULT["status"] = "ERROR"
        RESULT["failure"] = {"stage":CURRENT,"type":type(exc).__name__,"message":str(exc)}
        if CURRENT is not None:
            RESULT["stages"][CURRENT]["status"] = "ERROR"
        exit_code = 1
    RESULT["elapsed_seconds"] = time.monotonic() - START
    RESULT["control_policy"] = "JSON status and each stage/control govern; process exit alone is not a verdict"
    json.dump(RESULT,sys.stdout,sort_keys=True,separators=(',',':'))
    sys.stdout.write('\n')
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
