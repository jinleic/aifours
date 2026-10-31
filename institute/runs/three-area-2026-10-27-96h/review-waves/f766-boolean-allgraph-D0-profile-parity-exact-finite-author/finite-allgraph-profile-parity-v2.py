#!/usr/bin/env python3
"""F766 independent bounded source proposal -- UNRUN, no child science.

Frozen input: f766 manifest a85434d6893fb935ff802c02b704a19cc9829932ec385591ce2225a48e1af2b2,
complete packet b00c3a145d4337ee744046eb921e7ad1d91be878130f9eb238ea748340b2f95d.
Native observation BEFORE v1 creation: 2026-10-30T17:51:46-0700 PDT.
ADDITIVE PRE-RUN CORRECTION: v1 SHA256 e56fc93e99a2df96a4208f2f34f618085ea8d04b7ebb691084c44dcad44d24df is preserved, superseded and NEVER RUN. Its ell0 row census wrongly expected 20 six-site rows AFTER the |Z|<=2 filter. Eight of those 20 give a |Z|=3 and must be removed, so the filtered count is 12. V1 would have stopped at E_DOMAIN_COUNT; this is a pre-run source-design error, not a failed run. This complete v2 is created exclusively in one write; no v1 or v2 file was edited. The E-row b=0 cancellation and common-residue mutant checks are also made direct.
No held episode/consumer, sibling proof, old code, or outgoing link is input.

Exact finite domain for the profile search: d_E=0; i,b in F2^2, h,ell in
F2; graph h=F_i with odd XOR F. Exactly four of the 16 graph mates have
X=+/-2 (D0), the other mates have X=0, and all graph sites have X=+/-1.
On ell=0, b=0 has X=0, and exactly six of the remaining 24 sites have
X=+/-2. Every one of the eight partial rows has sum zero. The SINGLE X is
used to calculate all seven eta=(s,alpha) != (0,0), every Z is integer,
and every one of those seven E+graph 8-vectors must be a singleton +/-2 or
four +/-1 on an affine two-flat with sign product -1. No separate columns,
no precondition from the candidate's parity argument, and no prechosen
Z2 location, phase, mate signs, U3 cap, or witness are assumed in that
search. The four graph occupancy multisets are 4000,3100,2200,2110;
1111 is outside this task's four claimed partitions. d_E=1,2,3,4 remain
outside this program. A zero X site in ell0/b!=0 has 18 possible Z4
locations, treated as an additional physical choice, not as a different X.

Reduction is exact for these predicates. The eight odd F tables are one
orbit under h -> h+delta(i), delta any affine F2-valued function on i:
this permutes ell0 physical sites, fixes b, and multiplies each s-column
by a quotient character, preserving the singleton/flat/sign conditions.
Multiplication of X by (-1)^(c*ell+beta.i) is another free 8-element
symmetry; it sets S_i(0)=+1 for i=0,1,2. It also preserves row-zero,
physical types, all seven profiles, and (3.1). Consequently each complete
canonical (F=(0,0,0,1), those three signs fixed) X represents exactly 64
labelled (F,X) pairs. For each canonical F/X, the actual set of 18 Z4
locations remains available. These reductions do NOT select the claimed
odd-row offsets, k0 covectors, or 211 N/O type; those are recorded ONLY
AFTER the same-X seven-profile check.

All row possibilities are generated from the definition. At F=0 their
zero-row-and-|Z|<=2 counts k=0..4 are 6,32,84,96,32. For k=4, 44 zero-row
choices reduce to 32: 12 have matching nonzero covectors in S and the
balanced four-site D sign and give a forbidden |Z|=3. For ell0 each of
four rows has 1,30,90,20 zero-sum possibilities with 0,2,4,6 nonzero
sites, before local cap: six in total gives 4*20+12*90*30+4*30**3=140480.
For six sites, eight patterns are +/-chi(h+alpha.b), alpha in F2^2,
and give a forbidden |Z|=3. Thus the local-cap counts are 1,30,90,12,
and six sites give 4*12+12*90*30+4*30**3=140448. These are before the
simultaneous seven-profile restrictions. The profile set is generated as 16 signed
singletons plus 14 affine planes times 8 odd-product signings =128.
The source derives candidate graph workload counts from the row sets;
no output is called complete before every graph and every compatible
ell0 row has finished. Time cutoff returns explicit PARTIAL, not PASS.

For the four shapes, the graph phase restrictions have row-linear parts
lambda_i an affine bijection F2^2 -> F2^2. Every permutation of four
2-bit values is such a bijection; all 24 and all 16 row constants are
allowed. For even k, S=epsilon*chi_xi and theta=lambda+xi. For odd k,
S=epsilon*(2*1_gamma-1) and kappa=lambda+3+Q(gamma), Q swaps bits. Since
XOR_i lambda_i=0 and the number of odd rows is 0 or 2, (3.1) is exactly
XOR_even xi XOR Q(XOR_odd gamma) XOR Q(XOR_D b)=0. This is evaluated only
after seven simultaneous profiles. Failure of an intermediate claim is
kept separately from failure of (3.1), with the actual canonical X.

The A1 check builds actual common graph a,g,X,Y and ell0 physical local
types, reconstructs every four-fibre inverse value in representative
arrays, and checks the A1/4 congruence. It enumerates every one-row sign,
D location, F bit, lambda, phase sign, mate sign pattern and alpha/s/beta
parity in an independent row reduction; the full representative arrays
cover all 24 lambda tables, 16 phase constants and single mate sign flips.
For arbitrary joint mate signs, flipping one changes A1 by +/-4, hence
changes A1/4 parity once. Row identities plus this linearity cover all
joint sign patterns; they are not a numerical enumeration of all global
Y. J=1, the U3 cap and a full physical caller are NOT assumed/tested.

For the candidate's derived 2+2 physical configuration, the source
constructs all Delta!=0, ordered distinct U,V, physical h choices, Z4
locations, and all X signs with row-zero. It independently checks each
actual Y sign arrangement yielding the displayed B support, including
the six E-row Y sites; it verifies the U extension-ratio flip, V fixed
ratio, and all N-row graph ratios. These are conditional consequences,
not a proof that the configuration is forced. The Z4 can share (i,b)
with Z2 only in the other physical h slot. The ell0 singleton control is
one accepted column only, emphatically NOT an all-seven-profile witness.

One new parent whole-source read and a separate GO (external cap <=55 s)
are required before running. This file imports only the stdlib, reads no
files or input, uses no subprocess/network/deletion, and emits one JSON
object to stdout. Its own cooperative wall deadline is 44 seconds. The
child has not run, compiled, tested, linted or built it. No result here is
parent adoption, a family/human/kernel check, an original caller, V,
all-rank2, or a global witness/proof.
"""

import itertools
import json
import time

START = time.monotonic()
DEADLINE = START + 44.0
TICKS = 0
REPORT = {
    "source_status": "PARENT_EXECUTION_ONLY_AFTER_WHOLE_SOURCE_READ_AND_NEW_GO",
    "scope": "d_E0; four graph partitions; same-X seven profiles; no U3/V/caller",
    "cooperative_seconds": 44,
    "stages": {},
    "warnings": [
        "No parent adoption or family/human/kernel verification follows.",
        "Graph 1111 and d_E=1,2,3,4 are outside the enumerated parity domain.",
        "The ell0 singleton control is a column, not a seven-profile witness.",
        "Derived 2+2 physical pattern is conditional, not its forcing proof.",
        "On cutoff, started graph tuples may not have all E completions visited."
    ]
}


class Expired(Exception):
    pass


class Finding(Exception):
    def __init__(self, reason, data=None):
        self.reason = reason
        self.data = data
        super().__init__(reason)


def tick():
    global TICKS
    TICKS += 1
    if TICKS % 128 == 0 and time.monotonic() >= DEADLINE:
        raise Expired()


def need(condition, reason, data=None):
    if not condition:
        raise Finding(reason, data)


def dot(a, b):
    return (a & b).bit_count() & 1


def sgn(bit):
    return -1 if bit & 1 else 1


def Q(v):
    return ((v & 1) << 1) | ((v & 2) >> 1)


def xor_all(values):
    out = 0
    for value in values:
        out ^= value
    return out


def walsh(values, alpha):
    return sum(values[b] * sgn(dot(alpha, b)) for b in range(4))


ETAS = ((1, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (1, 3))


def signed_character(values):
    for covector in range(4):
        for epsilon in (-1, 1):
            if all(values[b] == epsilon * sgn(dot(covector, b)) for b in range(4)):
                return epsilon, covector
    return None


def odd_exception(values):
    for epsilon in (-1, 1):
        for gamma in range(4):
            if all(values[b] == epsilon * (2 * (b == gamma) - 1) for b in range(4)):
                return epsilon, gamma
    return None


def raw_graph_z(S, D, F, s, alpha):
    # Direct 8-site partial transform, independent of the two-Walsh formula.
    numerator = 0
    for h in range(2):
        for b in range(4):
            value = S[b] if h == F else 2 * D[b]
            numerator += value * sgn(s * h + dot(alpha, b))
    need(numerator % 4 == 0, "ROW_NONINTEGRAL", [S, D, F, s, alpha, numerator])
    return numerator // 4


def row_reason(S, D):
    if len(S) != 4 or any(x not in (-1, 1) for x in S):
        return "GRAPH_VALUE"
    if len(D) != 4 or any(x not in (-1, 0, 1) for x in D):
        return "MATE_VALUE"
    if sum(S) + 2 * sum(D) != 0:
        return "ROW_ZERO"
    for s, alpha in ETAS:
        n = walsh(S, alpha) + 2 * sgn(s) * walsh(D, alpha)
        if n % 4:
            return "ROW_NONINTEGRAL"
        if abs(n // 4) > 2:
            return "ROW_CAP"
    return None


def make_row(S, D, F):
    k = sum(v != 0 for v in D)
    z = tuple(raw_graph_z(S, D, F, s, alpha) for s, alpha in ETAS)
    for j, (s, alpha) in enumerate(ETAS):
        numerator = sgn(s * F) * (walsh(S, alpha) + 2 * sgn(s) * walsh(D, alpha))
        need(numerator == 4 * z[j], "ROW_FORMULA", [S, D, F, s, alpha])
    need(z[0] == -sgn(F) * sum(D), "ROW_LAMBDA", [S, D, F])
    r = {"S": S, "D": D, "F": F, "z": z, "k": k}
    if k % 2 == 0:
        sc = signed_character(S)
        need(sc is not None, "EVEN_NOT_CHARACTER", [S, D])
        r["eps"], r["xi"] = sc
    else:
        oc = odd_exception(S)
        need(oc is not None, "ODD_NOT_EXCEPTION", [S, D])
        r["eps"], r["gamma"] = oc
    def pair(alpha):
        j = 1 + 2 * (alpha - 1)
        return abs(z[j]), abs(z[j + 1])
    if k == 0:
        need(r["xi"] != 0 and z[0] == 0, "K0_CLASS", [S, D])
        r["type"] = "k0"
    elif k == 1:
        u = next(b for b in range(4) if D[b])
        need(D[u] == r["eps"] and abs(z[0]) == 1, "K1_LAMBDA", [S, D])
        for alpha in range(1, 4):
            main = dot(alpha, r["gamma"] ^ u)
            p = pair(alpha)
            need(p[main] == 1 and p[1 - main] == 0, "K1_EXTENSION", [S, D, alpha, p])
        r.update(type="k1", u=u)
    elif k == 2:
        u, v = (b for b in range(4) if D[b])
        a = Q(u ^ v)
        if D[u] == D[v]:
            need(r["xi"] == 0 and abs(z[0]) == 2, "K2_ACTIVE_LAMBDA", [S, D])
            for alpha in range(1, 4):
                need(pair(alpha) == ((1, 1) if alpha == a else (0, 0)),
                     "K2_ACTIVE_EXTENSION", [S, D, alpha])
            typ = "k2_active"
        elif r["xi"] == a:
            need(z[0] == 0 and all(pair(alpha) == (1, 1) for alpha in range(1, 4)),
                 "K2_N_EXTENSION", [S, D])
            typ = "k2_N"
        else:
            need(z[0] == 0, "K2_O_LAMBDA", [S, D])
            for alpha in range(1, 4):
                expected = (0, 0) if alpha == a else ((1, 1) if alpha == (a ^ r["xi"]) else None)
                p = pair(alpha)
                need((sorted(p) == [0, 2]) if expected is None else (p == expected),
                     "K2_O_EXTENSION", [S, D, alpha, p])
            typ = "k2_O"
        r.update(type=typ, a_D=a)
    elif k == 3:
        u = next(b for b in range(4) if not D[b])
        minority = [b for b in range(4) if D[b] == -r["eps"]]
        need(len(minority) == 1 and sum(D) == r["eps"] and abs(z[0]) == 1,
             "K3_LAMBDA", [S, D])
        special = Q(u ^ minority[0])
        for alpha in range(1, 4):
            main = dot(alpha, r["gamma"] ^ u)
            p = pair(alpha)
            need(p[main] == 1 and p[1-main] == (2 if alpha == special else 0),
                 "K3_EXTENSION", [S, D, alpha, p])
        r.update(type="k3", u=u, special=special)
    elif k == 4:
        if sum(D):
            need(abs(sum(D)) == 2 and r["xi"] == 0 and abs(z[0]) == 2,
                 "K4_ACTIVE_LAMBDA", [S, D])
            need(all(pair(alpha) == (1, 1) for alpha in range(1, 4)),
                 "K4_ACTIVE_EXTENSION", [S, D])
            r["type"] = "k4_active"
        else:
            dc = signed_character(D)
            need(dc is not None and dc[1] != 0 and dc[1] != r["xi"] and r["xi"] != 0,
                 "K4_INACTIVE_COVECTOR", [S, D])
            for alpha in range(1, 4):
                expected = (2, 2) if alpha == dc[1] else ((1, 1) if alpha == r["xi"] else (0, 0))
                need(pair(alpha) == expected, "K4_INACTIVE_EXTENSION", [S, D, alpha])
            r.update(type="k4_inactive", a_D=dc[1])
    else:
        raise Finding("K_OUT_OF_RANGE", k)
    return r


def make_rows():
    rows = {0: {k: [] for k in range(5)}, 1: {k: [] for k in range(5)}}
    total_candidates = 0
    for S in itertools.product((-1, 1), repeat=4):
        for D in itertools.product((-1, 0, 1), repeat=4):
            tick()
            total_candidates += 1
            if row_reason(S, D) is not None:
                continue
            for F in (0, 1):
                row = make_row(S, D, F)
                rows[F][row["k"]].append(row)
    for F in (0, 1):
        actual = [len(rows[F][k]) for k in range(5)]
        need(actual == [6, 32, 84, 96, 32], "ROW_DOMAIN_COUNT", [F, actual])
    REPORT["stages"]["one_row"] = {
        "complete": True, "raw_S_D_pairs": total_candidates,
        "counts_per_F_for_k0_to_4": [6, 32, 84, 96, 32],
        "F_values": [0, 1], "row_zero_and_every_eta_integer_and_local_abs_at_most_2": True,
        "classes": "k0,k1,k2 active/N/O,k3,k4 active/inactive; exact extensions"
    }
    return rows


def profile_reason(p):
    if len(p) != 8 or any(type(x) is not int for x in p):
        return "PROFILE_VALUE"
    if sum(x * x for x in p) != 4:
        return "PROFILE_ENERGY"
    nz = [i for i, x in enumerate(p) if x]
    if len(nz) == 1 and abs(p[nz[0]]) == 2:
        return None
    if len(nz) != 4 or any(abs(p[i]) != 1 for i in nz):
        return "PROFILE_SHAPE"
    if xor_all(nz) != 0:
        return "PROFILE_NONFLAT"
    product = 1
    for i in nz:
        product *= p[i]
    return None if product == -1 else "PROFILE_SIGN_PRODUCT"


def make_profiles():
    profiles = []
    for i in range(8):
        for sign in (-2, 2):
            p = [0] * 8
            p[i] = sign
            profiles.append(tuple(p))
    flats = 0
    for locations in itertools.combinations(range(8), 4):
        if xor_all(locations):
            continue
        flats += 1
        for signs in itertools.product((-1, 1), repeat=4):
            if signs[0] * signs[1] * signs[2] * signs[3] != -1:
                continue
            p = [0] * 8
            for i, sign in zip(locations, signs):
                p[i] = sign
            profiles.append(tuple(p))
    need(flats == 14 and len(profiles) == 128 and len(set(profiles)) == 128,
         "PROFILE_DOMAIN_COUNT", [flats, len(profiles)])
    need(all(profile_reason(p) is None for p in profiles), "PROFILE_CONSTRUCTION")
    gmasks = {}
    emasks = [{v: 0 for v in (-2, -1, 0, 1, 2)} for _ in range(4)]
    for j, p in enumerate(profiles):
        bit = 1 << j
        gmasks[p[4:]] = gmasks.get(p[4:], 0) | bit
        for i in range(4):
            emasks[i][p[i]] |= bit
    REPORT["stages"]["profile_universe"] = {
        "complete": True, "singleton_profiles": 16, "affine_flats": 14,
        "odd_signings_per_flat": 8, "all_profiles": 128
    }
    return gmasks, emasks


def e_reason(values):
    if len(values) != 6 or any(x not in (-2, 0, 2) for x in values):
        return "E_VALUE"
    if sum(values) != 0:
        return "E_ROW_ZERO"
    return None


def e_transform(values):
    result = []
    for s, alpha in ETAS:
        n = sum(values[3*h+b-1] * sgn(s*h + dot(alpha, b))
                for h in range(2) for b in range(1, 4))
        need(n % 4 == 0, "E_NONINTEGRAL", [values, s, alpha, n])
        result.append(n // 4)
    return tuple(result)


def make_erows():
    options = []
    for values in itertools.product((-2, 0, 2), repeat=6):
        tick()
        if e_reason(values) is None:
            z = e_transform(values)
            if all(abs(x) <= 2 for x in z):
                options.append({"values": values, "z": z,
                                "r": sum(x != 0 for x in values)})
    counts = [sum(e["r"] == n for e in options) for n in (0, 2, 4, 6)]
    need(counts == [1, 30, 90, 12], "E_DOMAIN_COUNT", counts)
    REPORT["stages"]["ell0_rows"] = {
        "complete": True, "counts_at_0_2_4_6": counts,
        "zero_sum_counts_before_local_cap": [1, 30, 90, 20],
        "six_Z2_arrays_before_local_cap": 4*20 + 12*90*30 + 4*30**3,
        "six_Z2_arrays_after_local_cap_before_full_profiles": 4*12 + 12*90*30 + 4*30**3,
        "Z4_locations_per_array": 18
    }
    return options


def layout_reason(z2, z4):
    if len(z2) != 6 or len(set(z2)) != 6:
        return "Z2_COUNT"
    if z4 in z2:
        return "Z4_OVERLAP"
    if any(i not in range(4) or h not in range(2) or b not in (1, 2, 3)
           for i, h, b in z2 + (z4,)):
        return "PHYSICAL_SITE"
    return None


def ratio_reason(u0, u1, v0, v1):
    if u0 not in (-1, 1) or u1 != -u0:
        return "EXTENSION_RATIO"
    if v0 not in (-1, 1) or v1 != v0:
        return "EXTENSION_RATIO"
    return None


def controls():
    singleton = (2, 0, 0, 0, 0, 0, 0, 0)
    need(profile_reason(singleton) is None, "SINGLETON_POSITIVE_CONTROL")
    checks = {
        "ell0_singleton_omission": ("ELL0_SINGLETON_OMISSION",
            "ELL0_SINGLETON_OMISSION" if sum(abs(x) == 1 for x in singleton) != 4 else None),
        "wrong_graph_value": ("GRAPH_VALUE", row_reason((2, 1, -1, -1), (0, 0, 0, 0))),
        "row_zero": ("ROW_ZERO", row_reason((1, 1, 1, 1), (0, 0, 0, 0))),
        "k4_magnitude_three": ("ROW_CAP", row_reason((1, 1, -1, -1), (1, 1, -1, -1))),
        "profile_energy": ("PROFILE_ENERGY", profile_reason((1, 0, 0, 0, 0, 0, 0, 0))),
        "profile_nonflat": ("PROFILE_NONFLAT", profile_reason((-1, 1, 1, 0, 1, 0, 0, 0))),
        "profile_sign_product": ("PROFILE_SIGN_PRODUCT", profile_reason((1, 1, 1, 1, 0, 0, 0, 0))),
        "ell0_value": ("E_VALUE", e_reason((1, 0, 0, 0, 0, 0))),
        "ell0_row_zero": ("E_ROW_ZERO", e_reason((2, 0, 0, 0, 0, 0))),
        "z2_count": ("Z2_COUNT", layout_reason(((0,0,1),), (1,0,1))),
        "z4_overlap": ("Z4_OVERLAP", layout_reason(((0,0,1),(0,0,2),(0,1,1),(0,1,2),
                                                       (1,0,1),(1,0,2)), (1,0,2))),
        "extension_ratio": ("EXTENSION_RATIO", ratio_reason(1, 1, -1, -1))
    }
    for name, (expected, actual) in checks.items():
        need(actual == expected, "CONTROL_WRONG_REASON", [name, expected, actual])
    REPORT["stages"]["controls"] = {
        "complete": True, "intended_reasons": {name: expected for name, (expected, _) in checks.items()},
        "singleton_accepted_by_real_predicate": True,
        "singleton_is_only_one_column_not_a_full_witness": True
    }


def eta_value(values, s, alpha):
    n = sum(values[3*h+b-1] * sgn(s*h + dot(alpha, b))
            for h in range(2) for b in range(1, 4))
    need(n % 4 == 0, "DERIVED_E_NONINTEGRAL")
    return n // 4


def derived_22():
    layouts = x_layouts = y_patterns = graph_ratios = 0
    for delta in range(1, 4):
        a = Q(delta)
        p, q = [b for b in (1, 2, 3) if b != delta]
        other_alpha = [alpha for alpha in (1, 2, 3) if alpha != a]
        for U in range(4):
            for V in range(4):
                if U == V:
                    continue
                for hu in range(2):
                    for hv in range(2):
                        z2 = ((U,0,delta), (U,1,delta), (U,hu,p),
                              (U,1-hu,q), (V,hv,p), (V,hv,q))
                        for target in z2[2:]:
                            i, h, b = target
                            z4 = (i, 1-h, b)
                            need(layout_reason(z2, z4) is None, "LAYOUT_CONSTRUCTION")
                            layouts += 1
                            local_x = 0
                            for signs in itertools.product((-1, 1), repeat=6):
                                tick()
                                if sum(signs[:4]) or sum(signs[4:]):
                                    continue
                                local_x += 1
                                x_layouts += 1
                                vals = {U: [0]*6, V: [0]*6}
                                for (i, h, b), sign in zip(z2, signs):
                                    vals[i][3*h+b-1] = 2*sign
                                lam_u = eta_value(vals[U], 1, 0)
                                need(lam_u in (-2, 0, 2) and eta_value(vals[V], 1, 0) == 0,
                                     "DERIVED_LAMBDA")
                                ru, rv = [], []
                                for alpha in other_alpha:
                                    u0, u1 = (eta_value(vals[U], s, alpha) for s in (0, 1))
                                    v0, v1 = (eta_value(vals[V], s, alpha) for s in (0, 1))
                                    need(abs(u0) == abs(u1) == abs(v0) == abs(v1) == 1,
                                         "DERIVED_NONZERO_EXTENSIONS", [delta, U, V, signs, alpha])
                                    ru.append(u0*u1)
                                    rv.append(v0*v1)
                                need(ratio_reason(ru[0], ru[1], rv[0], rv[1]) is None,
                                     "DERIVED_EXTENSION_RATIO")
                                za = [abs(eta_value(vals[U], s, a)) for s in (0, 1)]
                                need(sorted(za) == ([0, 2] if lam_u == 0 else [0, 0]),
                                     "DERIVED_A_COLUMN", [delta, signs, za, lam_u])
                            need(local_x == 12, "DERIVED_X_SIGN_COUNT", local_x)
                            for s in (0, 1):
                                good = 0
                                for signs in itertools.product((-1, 1), repeat=7):
                                    tick()
                                    Y = {site: 2*sign for site, sign in zip(z2, signs[:6])}
                                    Y[z4] = 4*signs[6]
                                    def B(i, b):
                                        return Y.get((i,0,b), 0) + sgn(s)*Y.get((i,1,b), 0)
                                    ok = B(U, delta) == 0 and B(V, delta) == 0
                                    ok = ok and all(abs(B(i, b)) == 2 for i in (U,V) for b in (p,q))
                                    if ok:
                                        good += 1
                                need(good == 32, "DERIVED_Y_SIGN_COUNT", [z2, z4, s, good])
                                # Enumerate the two physical b=0 Y signs directly;
                                # three E rows are independent and the F row is zero.
                                e_choices = sum(1 for e0,e1 in itertools.product((-1,1), repeat=2)
                                                if 2*e0 + sgn(s)*2*e1 == 0)
                                need(e_choices == 2, "E_ROW_CANCELLATION", [s,e_choices])
                                y_patterns += good * e_choices**3
        # Actual graph N rows, independently of ell0 signs and layout.
        for u, v in itertools.combinations(range(4), 2):
            if (u ^ v) != delta:
                continue
            for dsign, eps, F in itertools.product((-1,1), (-1,1), (0,1)):
                D = tuple(dsign if b == u else (-dsign if b == v else 0) for b in range(4))
                S = tuple(eps * sgn(dot(a,b)) for b in range(4))
                row = make_row(S, D, F)
                need(row["type"] == "k2_N", "DERIVED_N_CLASS")
                for alpha in other_alpha:
                    z0 = raw_graph_z(S, D, F, 0, alpha)
                    z1 = raw_graph_z(S, D, F, 1, alpha)
                    need(abs(z0) == abs(z1) == 1 and z0*z1 == -sgn(F),
                         "DERIVED_GRAPH_EXTENSION_RATIO", [delta,u,v,alpha,F])
                    graph_ratios += 1
    need(layouts == 576 and x_layouts == 6912 and y_patterns == 294912 and graph_ratios == 96,
         "DERIVED_DOMAIN_COUNT", [layouts,x_layouts,y_patterns,graph_ratios])
    REPORT["stages"]["derived_22"] = {
        "complete": True, "conditional_not_forcing": True, "physical_layouts_with_Z4": layouts,
        "labelled_X_and_Z4": x_layouts, "Y_sign_patterns_with_slice_and_E_signs_per_layout": y_patterns,
        "joint_labelled_X_Z4_Y_slice": 12*y_patterns, "graph_N_row_extension_checks": graph_ratios,
        "ratio_consequence": "U flips, V and each N graph row are constant; four-plane product cannot be -1 in both extensions at both alphas",
        "nonflat_support": "if A xor B differs from U xor V the four support sites are not an affine plane"
    }


def local_a1(rows):
    local_cases = residue_checks = aligned_checks = 0
    for F in (0, 1):
        for k in range(5):
            for r in rows[F][k]:
                for lam in range(4):
                    for phase in (0, 1):
                        G = tuple(sgn(phase + ((b & 1) != 0 and (b & 2) != 0) + dot(lam,b))*r["S"][b]
                                  for b in range(4))
                        mates = [b for b in range(4) if not r["D"][b]]
                        if k % 2 == 0:
                            theta = lam ^ r["xi"]
                            sigma_bit = (1 - sgn(phase)*r["eps"]) // 2
                        else:
                            kappa = lam ^ 3 ^ Q(r["gamma"])
                        for alpha in range(4):
                            gw = walsh(G, alpha)
                            if k % 2 == 0:
                                db = sigma_bit + dot(alpha, Q(theta)) + (theta == 3) + ((alpha & 1) != 0 and (alpha & 2) != 0)
                                need(gw == 2 * sgn(db), "BENT_DUAL", [r,lam,phase,alpha,gw])
                            else:
                                need(abs(gw) == (4 if alpha == kappa else 0),
                                     "ODD_GRAPH_CHARACTER", [r,lam,phase,alpha,gw])
                            aligned = sum(G[b]*sgn(dot(alpha,b))*(3 if b in mates else 1) for b in range(4))
                            mag = abs(aligned)
                            if k == 0:
                                good = mag == 6
                            elif k == 1:
                                good = mag == (10 if alpha == kappa else 2)
                            elif k == 2:
                                u, v = (b for b in range(4) if r["D"][b])
                                pred2 = G[u]*G[v]*sgn(dot(alpha,u ^ v)) == 1
                                good = mag == (2 if pred2 else 6)
                            elif k == 3:
                                good = mag <= 6
                            else:
                                good = mag == 2
                            need(good, "A1_ROW_MAGNITUDE", [r,lam,phase,alpha,mag])
                            aligned_checks += 1
                        for mate_signs in itertools.product((-1,1), repeat=len(mates)):
                            tick()
                            local_cases += 1
                            nnegative = sum(e == -1 for e in mate_signs)
                            for alpha in range(4):
                                for s in (0,1):
                                    for beta_parity in (0,1):
                                        row_sum = sgn(s*F + beta_parity) * (
                                            walsh(G,alpha) + 2*sgn(s)*sum(
                                                e*sgn(dot(alpha,b)) for b,e in zip(mates,mate_signs)))
                                        need(row_sum % 2 == 0, "A1_ROW_NOT_EVEN")
                                        if k % 2 == 0:
                                            d = sigma_bit + ((alpha ^ theta) == 3) + s*F + beta_parity
                                            graph_half = 1 - 2*d
                                        else:
                                            graph_half = 2*(alpha == kappa)
                                        exponent_sum = sum(s*(1+F) + dot(alpha,b) + beta_parity for b in mates)
                                        expected = graph_half + len(mates) - 2*(nnegative + exponent_sum)
                                        need((row_sum//2 - expected) % 4 == 0,
                                             "A1_ROW_RESIDUE", [r,lam,phase,mate_signs,alpha,s,beta_parity])
                                        residue_checks += 1
    REPORT["stages"]["a1_one_row"] = {
        "complete": True, "local_mate_sign_configurations": local_cases,
        "mod4_half_row_checks": residue_checks, "aligned_row_magnitude_checks": aligned_checks,
        "quantifiers": "all 250 local S,D per F, both F, all four lambda, two phases, every mate sign, every alpha/s/beta parity"
    }


def representative_array(graph_rows, lambdas, phases):
    X = [[[[0 for b in range(4)] for h in range(2)] for i in range(4)] for ell in range(2)]
    Y = [[[[0 for b in range(4)] for h in range(2)] for i in range(4)] for ell in range(2)]
    A = [[[[0 for b in range(4)] for h in range(2)] for i in range(4)] for ell in range(2)]
    G = [[[[0 for b in range(4)] for h in range(2)] for i in range(4)] for ell in range(2)]
    for i in range(4):
        for h in range(2):
            G[0][i][h][0] = 4 if i == 0 else -2
            Y[0][i][h][0] = 0 if i == 0 else 2
    for i in range(3):
        X[0][i][0][1], X[0][i][0][2] = 2, -2
        Y[0][i][0][1] = Y[0][i][0][2] = 2
    Y[0][3][0][1] = 4
    mate_sites = []
    for i, r in enumerate(graph_rows):
        F = r["F"]
        for b in range(4):
            rho = -sgn(((b & 1) != 0) and ((b & 2) != 0))
            aa = sgn(phases[i] + dot(lambdas[i], b))
            X[1][i][F][b] = r["S"][b]
            X[1][i][1-F][b] = 2*r["D"][b]
            A[1][i][F][b] = aa
            G[1][i][F][b] = rho
            G[1][i][1-F][b] = -2*rho
            Y[1][i][F][b] = -aa*rho*r["S"][b]
            if not r["D"][b]:
                Y[1][i][1-F][b] = 2
                mate_sites.append((i,1-F,b))
    need(len(mate_sites) == 12, "REPRESENTATIVE_D0_COUNT")
    for ell in (0,1):
        for i in range(4):
            for h in range(2):
                for b in range(4):
                    x, y = X[ell][i][h][b], Y[ell][i][h][b]
                    aa, gg = A[ell][i][h][b], G[ell][i][h][b]
                    for u, v in itertools.product((0,1), repeat=2):
                        n = x + 3*aa*sgn(u) + gg*sgn(v) + y*sgn(u+v)
                        need(n % 4 == 0 and n//4 in (-1,0,1), "PHYSICAL_INVERSE",
                             [ell,i,h,b,u,v,x,y,aa,gg,n])
    return X, Y, mate_sites


def parity31(rows):
    graph_xi = xor_all(r["xi"] for r in rows if r["k"] % 2 == 0)
    gamma = xor_all(r["gamma"] for r in rows if r["k"] % 2)
    bd = xor_all(b for r in rows for b in range(4) if r["D"][b])
    return graph_xi ^ Q(gamma) ^ Q(bd)


def a1_reason(value, predicted):
    if value % 4:
        return "A1_NOT_DIVISIBLE_BY_4"
    if ((value//4) & 1) != predicted:
        return "A1_COMMON_RESIDUE"
    return None


def a1_arrays(rows):
    configs = comparisons = flip_comparisons = parity31_configs = 0
    representative_shapes = ((4,0,0,0), (3,1,0,0), (2,2,0,0), (2,1,1,0))
    Ftable = (0,0,0,1)
    control_done = False
    for shape in representative_shapes:
        graph_rows = [rows[Ftable[i]][shape[i]][0] for i in range(4)]
        for lambdas in itertools.permutations(range(4)):
            for phases in itertools.product((0,1), repeat=4):
                tick()
                _, Y, mates = representative_array(graph_rows, lambdas, phases)
                configs += 1
                even = [i for i,r in enumerate(graph_rows) if r["k"] % 2 == 0]
                odd = [i for i,r in enumerate(graph_rows) if r["k"] % 2]
                theta = {i: lambdas[i] ^ graph_rows[i]["xi"] for i in even}
                kappa = {i: lambdas[i] ^ 3 ^ Q(graph_rows[i]["gamma"]) for i in odd}
                bd = xor_all(b for r in graph_rows for b in range(4) if r["D"][b])
                v = bd ^ Q(xor_all(theta.values()))
                c = 6 + len(even)//2 + sum(
                    (1 - sgn(phases[i])*graph_rows[i]["eps"])//2 + (theta[i] == 3) for i in even)
                has31 = parity31(graph_rows) == 0
                if has31:
                    parity31_configs += 1
                for s in (0,1):
                    common = None
                    for alpha in range(4):
                        for beta in range(4):
                            value = sum(Y[1][i][h][b]*sgn(s*h+dot(alpha,b)+dot(beta,i))
                                        for i in range(4) for h in range(2) for b in range(4))
                            predicted = (c+s+sum(k == alpha for k in kappa.values())+dot(alpha,v)) & 1
                            reason = a1_reason(value, predicted)
                            need(reason is None, reason or "A1_UNEXPECTED", [shape,lambdas,phases,s,alpha,beta,value,predicted])
                            comparisons += 1
                            if not control_done:
                                observed = a1_reason(value, predicted ^ 1)
                                need(observed == "A1_COMMON_RESIDUE", "CONTROL_WRONG_REASON", "A1_COMMON_RESIDUE")
                                control_done = True
                            if has31:
                                if common is None:
                                    common = predicted
                                need(predicted == common, "A1_NOT_COMMON", [shape,lambdas,phases,s,alpha,beta])
                            for i,h,b in mates:
                                changed = value - 4*sgn(s*h+dot(alpha,b)+dot(beta,i))
                                need(((changed//4)&1) == (predicted ^ 1), "A1_FLIPPED_MATE_RESIDUE")
                                flip_comparisons += 1
    REPORT["stages"]["a1_physical_arrays"] = {
        "complete": True, "representative_physical_arrays": configs,
        "A1_residue_checks": comparisons, "single_mate_flip_checks": flip_comparisons,
        "representatives_satisfying_algebraic_31": parity31_configs,
        "phase_scope": "all 24 affine-bijection lambda tables, all 16 row constants",
        "full_inverse": "all 256 entries checked ternary per representative",
        "joint_mate_signs": "covered by row enumeration and exact +/-4 flip linearity, not brute-force global enumeration",
        "seven_profiles_on_representatives": "not required; no witness claim",
        "common_residue_mutant_reason": "A1_COMMON_RESIDUE"
    }


def input_snapshot(graph_rows, erows):
    return {"F": [r["F"] for r in graph_rows],
            "graph_S": [r["S"] for r in graph_rows],
            "mate_D": [r["D"] for r in graph_rows],
            "ell0_h0b1b2b3_h1b1b2b3": [e["values"] for e in erows]}


def update_obligations(stats, graph_rows, erows, shape):
    # Crucially this is called only at a leaf satisfying all seven profiles.
    tests = {"final_31": parity31(graph_rows) == 0}
    odd = [r for r in graph_rows if r["k"] % 2]
    if len(odd) == 2:
        tests["odd_offsets_equal"] = (odd[0]["gamma"] ^ odd[0]["u"]) == (odd[1]["gamma"] ^ odd[1]["u"])
    if shape == (3,1,0,0):
        zero = [r for r in graph_rows if r["k"] == 0]
        tests["3100_k0_covectors_equal"] = zero[0]["xi"] == zero[1]["xi"]
    if shape == (2,1,1,0):
        pair = next(r for r in graph_rows if r["k"] == 2)
        tests["2110_k2_not_N"] = pair["type"] != "k2_N"
        tests["2110_k2_inactive"] = pair["type"] != "k2_active"
    for name, passed in tests.items():
        stats["obligation_checks"][name] = stats["obligation_checks"].get(name, 0) + 1
        if not passed:
            stats["obligation_failures"][name] = stats["obligation_failures"].get(name, 0) + 1
            if name not in stats["first_discriminators"]:
                stats["first_discriminators"][name] = input_snapshot(graph_rows, erows)


def graph_search(rows, eoptions, gmasks, emasks):
    Ftable = (0,0,0,1)
    shapes = ((4,0,0,0), (3,1,0,0), (2,2,0,0), (2,1,1,0))
    stage = {"complete": False, "shapes": {}, "orbit_factor_F_times_sign": 64,
             "one_Z4_choice_per_zero_site": 18,
             "obligations_applied_as_prefilters": False}
    REPORT["stages"]["same_X_seven_profiles"] = stage
    for shape in shapes:
        key = "".join(map(str, shape))
        permutations = sorted(set(itertools.permutations(shape)))
        expected_graphs = 0
        for ks in permutations:
            n = 1
            for i,k in enumerate(ks):
                table = rows[Ftable[i]][k]
                n *= sum(r["S"][0] == 1 for r in table) if i < 3 else len(table)
            expected_graphs += n
        stats = {"complete": False, "canonical_graph_tuples_expected": expected_graphs,
                 "canonical_graph_tuples_started": 0, "canonical_graph_tuples_finished": 0,
                 "graph_tuples_rejected_before_E": 0, "same_X_profile_arrays": 0,
                 "obligation_checks": {}, "obligation_failures": {}, "first_discriminators": {}}
        stage["shapes"][key] = stats
        for ks in permutations:
            tables = []
            for i,k in enumerate(ks):
                tables.append([r for r in rows[Ftable[i]][k] if i == 3 or r["S"][0] == 1])
            for graph_rows in itertools.product(*tables):
                tick()
                stats["canonical_graph_tuples_started"] += 1
                masks = [gmasks.get(tuple(graph_rows[i]["z"][j] for i in range(4)), 0) for j in range(7)]
                if not all(masks):
                    stats["graph_tuples_rejected_before_E"] += 1
                    stats["canonical_graph_tuples_finished"] += 1
                    continue
                candidates = []
                for i in range(4):
                    permissible = []
                    for e in eoptions:
                        if all(masks[j] & emasks[i][e["z"][j]] for j in range(7)):
                            permissible.append(e)
                    candidates.append(permissible)
                if all(candidates):
                    selected = []
                    def visit(i, count, current):
                        tick()
                        if i == 4:
                            if count == 6:
                                stats["same_X_profile_arrays"] += 1
                                update_obligations(stats, graph_rows, selected, shape)
                            return
                        for e in candidates[i]:
                            n = count + e["r"]
                            if n > 6 or n + 6*(3-i) < 6:
                                continue
                            next_masks = tuple(current[j] & emasks[i][e["z"][j]] for j in range(7))
                            if not all(next_masks):
                                continue
                            selected.append(e)
                            visit(i+1, n, next_masks)
                            selected.pop()
                    visit(0, 0, masks)
                stats["canonical_graph_tuples_finished"] += 1
        need(stats["canonical_graph_tuples_finished"] == expected_graphs, "GRAPH_DOMAIN_COUNT", key)
        stats["complete"] = True
        stats["labelled_F_X_count"] = stats["same_X_profile_arrays"] * 64
        stats["labelled_F_X_Z4_count"] = stats["same_X_profile_arrays"] * 64 * 18
    stage["complete"] = True


def main():
    try:
        rows = make_rows()
        gmasks, emasks = make_profiles()
        eoptions = make_erows()
        controls()
        derived_22()
        local_a1(rows)
        a1_arrays(rows)
        graph_search(rows, eoptions, gmasks, emasks)
        failed = any(s["obligation_failures"] for s in REPORT["stages"]["same_X_seven_profiles"]["shapes"].values())
        REPORT["status"] = "COMPLETE_WITH_DISCRIMINATORS" if failed else "COMPLETE_FINITE_SCOPE_ONLY"
    except Expired:
        REPORT["status"] = "PARTIAL_COOPERATIVE_DEADLINE"
    except Finding as exc:
        REPORT["status"] = "CHECK_FAILED_OR_DOMAIN_DISCRIMINATOR"
        REPORT["failure"] = {"reason": exc.reason, "data": exc.data}
    except Exception as exc:
        REPORT["status"] = "SOURCE_ERROR"
        REPORT["failure"] = {"type": type(exc).__name__, "message": str(exc)}
    REPORT["elapsed_seconds"] = time.monotonic() - START
    print(json.dumps(REPORT, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
