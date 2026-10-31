#!/usr/bin/env python3
"""F778: definition-first, exact finite source PREPARED ONLY; NOTTESTED.

ADDITIVE PRE-RUN V2 CORRECTION: the first complete source v1, SHA256
9a48f1a2e6b41cdfa933d42f1a197fc6da2fa6153d0a7627abfb9c8af297f2f7,
is preserved SUPERSEDED and UNRUN. Its FAIL handler could receive a
tuple-keyed diagnostic dictionary that json.dumps cannot serialize.
V2 reports failure detail with repr as a JSON string. This was a
design-inspection finding, not a test or an observed program failure.

NONBLIND same-harness prospective author, not an external/human/kernel review.
The parent must read ALL of these bytes, pin them, and issue a NEW explicit GO
before one execution.  The GO must impose an external limit <=55 seconds.  This
program checks its own cooperative monotonic deadline of 45 seconds and emits
one JSON object to stdout; it performs no input/file/network/subprocess/delete
operations and uses only itertools, json and time from Python >=3.10 stdlib.
FAIL and INCOMPLETE are nonzero exits.  PASS, if later observed, means only the
finite checks described below, not that the original mathematical target holds.

SOURCE BOUNDARY AND PINS (paths relative to institute/runs/
three-area-2026-10-27-96h/; whole files rendered in the sole frozen packet):
S1 review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/
   author-quotient-census-erratum-v1.md
   90c4242e118be887f19b61ccba23f4af0c6062516142962b9a315557c0e03606 LF1-9
S2 review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/
   author-candidate-v1-addendum-1.md
   4dddaf7084e784b8c8d2b51b857320a26438a6a669b1ad9dee2f8d19268c4114 LF1-15
S3 review-waves/f748-boolean-remaining-d0-same-object-u3-frontier-author/
   parent-omitted-ell0-lambda-singleton-proof-gap-major-v1.md
   79a618853b07f6e9dd30bc16592cb378a861c6b625cc7e3171e0a2779c2f0dca LF1-7
S4 review-waves/f754-boolean-four-E-row-and-U3-count-proof-author/
   author-candidate-v1.md
   018c8b9b56b1d2f5d26808204b9a1217c189a2ec0de2afa8fda1361fd52555cd LF1-188
S5 review-waves/f753-boolean-E-row-parity-and-lambda-complete-proof-author/
   author-candidate-v1.md
   e4e1c4a1812a03d0334dbee16dec50650d6a904e0e68b75dbcddae22e73aefa8 LF1-121
S6 dispositions/info-6-entire-four-distinct-d0-rank2-same-object-obstruction-
   parent-v1.md
   ae6fccd2b7206a1813ac3d3762774b3296fc70df6a83e24c6026391bac68c928 LF1-31
S7 parent-recovered-local-H-definition-and-general-g-foundation-v1.md
   a99db1148434016f1d995b83b758692d6ce94b6e27a87dbdde29e345923f88ef LF1-13
S8 dispositions/info-6-actual-rank2-seven-profile-and-four-distinct-d0-cross-
   fibre-parent-v1.md
   44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a LF1-37
Manifest a20ce7d1276521ceec038b8c8988482f4d6df18c1090bef16d8222a80f7c1d83;
packet 00eaaa2f6ef578c49a147f5b5963789be0a8a9cd73593900bd3817e3826abf4e,
455 LF, S1-S8 complete.  Source assertions below are proposed checks, NOT
reported results; no scientific program, compilation, test, or solver was run.

EXACT WRITTEN INTERFACE.  Coordinates (ell,h,i,b) use two-bit integers for i,b,
with u=b0 as bit value 2 and v=b1 as bit value 1.  A site is the six-bit vector
ell:h:i:b.  The six S5 arrays and the S4 example below are independently entered
from the literal spatial sites, then checked against their separately entered
seven-column tables.  Their graph is h=F_i on ell=1; graph mates are at the
other h with identical i,b.  E are ell=0,b=0,i!=0; the two full sites have
ell=0,b=0,i=0; all ell=0,b!=0 are Z.  One still-empty Z is designated Z4
only for the X-side census, with no Y assigned to it.  For each example and
ALL 64 specified character values t, the code constructs x(c)=(-1)^<t,c>X(c),
checks both 64-point direct and butterfly Walsh transforms, translation of the
same X spectrum, xhat(t)=0, and the three physical divisibility clauses (C)
on the actual graph-negative P, D0/Z2 set W, and its negative subset N.  It
checks every nonzero (s,alpha) column on the same X.  Four signed plane entries
have four plane Walsh values, EACH WITH TWO EXTENSIONS to the eight quotient
characters: the S1 correction is eight, not four, values +/-2.  A singleton
also gives eight +/-2 values.  Their factor 4 yields eight full coefficients
+/-8 for each nonzero eta; eta zero has eight zeros.  These are U0-side
countermodels only: no common Y, ternary u, J=1, all U3 caps or original
caller is supplied, and X transport does not independently change a,g or f.

UNIVERSAL FINITE GRAPH PARITY INTERFACE.  At d_E=4 the all-zero eta forces each
balanced graph X row to one of six signed nonconstant b characters.  Any
four-point quotient plane intersects ell=1 in 0,2,4 points; a graph +/-1 is
not a singleton +/-2.  Therefore each theta multiplicity is even.  Four equal
thetas would put a whole graph plane in both s columns, whose sign products
are opposite since XOR_i F_i=1; both cannot be -1.  Thus theta is 2+2 and
XOR_i theta_i=0.  The named actual graph phase supplies four DISTINCT row
covectors lambda_i, so XOR_i lambda_i=0 and mu_i=lambda_i XOR theta_i has
XOR_i mu_i=0.  The code checks all theta/sign/odd-F cases of this inference,
then the larger domain of ALL 4^3 ordered mu-tuples with XOR zero, ALL 2^4
row signs and ALL eight odd-parity F, at ALL s,alpha,beta.  It verifies the
bent-row transform directly and by its closed expression.

For fixed s, graph partial Walsh is a sum of four +/-2 terms.  Its quotient by
4 has parity equal to the parity of the number of negative row terms.  XOR mu=0
makes their product alpha-independent; XOR_i beta(i)=0 makes it beta-independent;
odd F makes the product flip when s flips.  On d_E=4 all 16 physical graph
mates are D3.  For one row D(b)=+/-1, 2 Dhat(alpha) mod 8 is independent of
alpha AND of its row multiplier +/-1, because each character changes the sign
of zero or two entries.  All 16 row sign patterns are checked directly.  Their
four row contributions add mod 8 to either 0 or 4, independently of alpha,
beta AND s; both aggregate residues are checked for every graph case.  This
factorization covers the parity consequence for all mate assignments but does
NOT enumerate all 16^4 assignments or claim an exhaustive search of full Y.

COMMON-Y CONSEQUENCE BEING CHECKED, WITH IMPORTS NOT CREATED BY THIS PROGRAM:
Assume the SAME physical x,y and actual normalization/graph phase, d_E=4,
J=1, y-energy 128, all 64 U3 coefficients congruent 4 mod 8 and capped at 12,
their common specified transport, the full same-X U0 profiles, the actual
unique Z4 and physical ell=0 opposite-h types.  These imports imply exactly
eight magnitude-4 full coefficients; |A0|+|A1|<=12 for each of 32 pairs.
In the even A1/4 slice let n count |A1|=8; in the opposite slice let m count
|A1|=4.  Partial Parseval on the SAME ell=1 Y, with energy 16+16*4=80, gives
m+4n+9(16-m)=160, and the eight-small bound gives n+m<=8.  The source derives
the possible n,m and ALL compatible allocations of the eight small full
coefficients, rather than treating either slice independently.  In both cases
it checks that every A0 in the odd slice must be zero.  Inversion in alpha,
beta then forces Y(0,0,i,b)+(-1)^s Y(0,1,i,b)=0 at all i,b.  At the actual
unique Z4, Y=+/-4 while its opposite-h distinct Z is 0 or +/-2; none cancels.
The program checks those exact finite integers; inversion, phase, profile,
physical bridge and existence of a common actual Y are mathematical imports,
not proved by the finite checks.  No d_E=0/2, all-rank2, V or NL242 conclusion.

Reason-specific negative controls explicitly reject a nonzero mu XOR that
breaks alpha-uniformity, a scrambled same-multiset slice, same rather than
opposite slice parities, a second Z4 allowing cancellation, an altered named
countermodel site, and omission of the two quotient-character extensions.
These are formal mutations/guard checks, not claimed physical counterexamples.
"""

from itertools import combinations, product
import json
import time

START = time.monotonic()
DEADLINE_SECONDS = 45.0


class CheckFailure(Exception):
    def __init__(self, reason, detail=None):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


class DeadlineReached(Exception):
    pass


def deadline():
    if time.monotonic() - START >= DEADLINE_SECONDS:
        raise DeadlineReached()


def require(condition, reason, detail=None):
    if not condition:
        raise CheckFailure(reason, detail)


def expect_reason(action, wanted):
    try:
        action()
    except CheckFailure as error:
        require(error.reason == wanted, "MUTANT_WRONG_REASON",
                {"wanted": wanted, "got": error.reason})
        return wanted
    raise CheckFailure("MUTANT_ACCEPTED", wanted)


def parity(a, b):
    return (a & b).bit_count() & 1


def pm(bit):
    return 1 - 2 * (bit & 1)


def site(ell, h, i, b):
    return (ell << 5) | (h << 4) | (i << 2) | b


def xor_all(values):
    result = 0
    for value in values:
        result ^= value
    return result


def direct_walsh(values):
    return [sum(value * pm(parity(k, x)) for x, value in enumerate(values))
            for k in range(len(values))]


def butterfly_walsh(values):
    result = list(values)
    half = 1
    while half < len(result):
        for base in range(0, len(result), half * 2):
            for j in range(half):
                x, y = result[base + j], result[base + j + half]
                result[base + j], result[base + j + half] = x + y, x - y
        half *= 2
    return result


# Literal F753 rows A,B,C,D = 00,01,10,11.  A graph pair is (sign,covector).
# Mate tuples are (i,b,sign of X/2); ell0 tuples are (i,h,b,sign of X/2).
F753_F = (0, 0, 0, 1)
SPECS = (
    {"name": "I", "F": F753_F,
     "graph": ((1, 2), (1, 2), (1, 3), (1, 3)),
     "mates": ((0, 0, 1), (0, 1, -1), (0, 2, 1), (0, 3, -1)),
     "ell0": ((2, 0, 2, 1), (2, 0, 3, 1), (2, 1, 1, -1),
              (2, 1, 2, -1), (3, 0, 1, 1), (3, 0, 3, -1)),
     "E": (0, 0, 0, 0), "M": (4, 0, 0, 0)},
    {"name": "II", "F": F753_F,
     "graph": ((1, 2), (1, 2), (1, 1), (-1, 1)),
     "mates": ((0, 0, 1), (0, 2, -1), (1, 0, -1), (1, 2, 1)),
     "ell0": ((2, 0, 1, 1), (2, 0, 2, 1), (2, 1, 1, -1),
              (2, 1, 3, -1), (3, 0, 2, 1), (3, 0, 3, -1)),
     "E": (0, 0, 0, 0), "M": (2, 2, 0, 0)},
    {"name": "III", "F": F753_F,
     "graph": ((1, 2), (-1, 2), (-1, 3), (1, 1)),
     "mates": ((0, 0, 1), (0, 1, -1)),
     "ell0": ((2, 0, 0, 1), (2, 0, 1, 1), (2, 1, 0, -1),
              (2, 1, 3, -1), (3, 0, 1, 1), (3, 0, 2, -1),
              (0, 0, 2, 1), (0, 0, 3, -1)),
     "E": (0, 0, 2, 0), "M": (2, 0, 0, 0)},
    {"name": "IIIprime", "F": F753_F,
     "graph": ((1, 2), (1, 2), (-1, 3), (-1, 1)),
     "mates": ((0, 0, 1), (0, 1, -1)),
     "ell0": ((2, 0, 2, 1), (2, 0, 3, 1), (2, 1, 0, -1),
              (2, 1, 3, -1), (3, 0, 0, 1), (3, 0, 3, -1),
              (0, 0, 2, 1), (0, 0, 3, -1)),
     "E": (0, 0, 1, 1), "M": (2, 0, 0, 0)},
    {"name": "IV", "F": F753_F,
     "graph": ((1, 2), (-1, 2), (1, 1), (1, 1)), "mates": (),
     "ell0": ((1, 0, 0, 1), (1, 0, 3, 1), (1, 1, 0, -1),
              (1, 1, 3, -1), (2, 0, 0, 1), (2, 0, 2, -1),
              (2, 1, 0, 1), (2, 1, 1, -1), (3, 0, 1, 1),
              (3, 0, 2, -1)),
     "E": (0, 2, 2, 0), "M": (0, 0, 0, 0)},
    {"name": "IVprime", "F": F753_F,
     "graph": ((1, 2), (-1, 2), (1, 1), (1, 1)), "mates": (),
     "ell0": ((1, 0, 1, 1), (1, 0, 2, 1), (1, 1, 0, -1),
              (1, 1, 3, -1), (2, 0, 0, 1), (2, 0, 2, -1),
              (2, 1, 0, -1), (2, 1, 1, 1), (3, 0, 0, 1),
              (3, 0, 3, -1)),
     "E": (0, 1, 2, 1), "M": (0, 0, 0, 0)},
    {"name": "F754", "F": (0, 0, 1, 0),
     "graph": ((1, 1), (1, 2), (1, 2), (-1, 1)), "mates": (),
     "ell0": ((2, 0, 0, 1), (2, 0, 2, 1), (2, 1, 0, -1),
              (2, 1, 1, -1), (1, 0, 0, 1), (1, 0, 3, -1),
              (3, 0, 0, 1), (3, 0, 1, -1), (3, 0, 2, -1),
              (3, 0, 3, 1)),
     "E": (0, 1, 2, 1), "M": (0, 0, 0, 0)},
)


def build_x(spec):
    values = [0] * 64
    F = spec["F"]
    require(sum(F) % 2 == 1, "GRAPH_F_NOT_ODD", spec["name"])
    for i, (sgn, theta) in enumerate(spec["graph"]):
        require(sgn in (-1, 1) and theta in (1, 2, 3), "GRAPH_LITERAL")
        for b in range(4):
            values[site(1, F[i], i, b)] = sgn * pm(parity(theta, b))
    for i, b, sgn in spec["mates"]:
        p = site(1, 1 - F[i], i, b)
        require(values[p] == 0 and sgn in (-1, 1), "MATE_DUPLICATE")
        values[p] = 2 * sgn
    for i, h, b, sgn in spec["ell0"]:
        p = site(0, h, i, b)
        require(values[p] == 0 and sgn in (-1, 1), "ELL0_DUPLICATE")
        values[p] = 2 * sgn
    return values


def column(values, s, alpha):
    result = []
    for ell in range(2):
        for i in range(4):
            numerator = sum(values[site(ell, h, i, b)] *
                            pm((s * h) ^ parity(alpha, b))
                            for h in range(2) for b in range(4))
            require(numerator % 4 == 0, "COLUMN_NOT_INTEGRAL",
                    [ell, i, s, alpha, numerator])
            result.append(numerator // 4)
    return result


def named_column(name, s, alpha):
    # E_i=i, G_i=4+i.  A=0, B=1, C=2, D=3.
    r = pm(s)
    if alpha == 0:
        terms = [(2 if name in ("I", "II", "III", "IIIprime", "F754") else 1, 2)]
    elif name == "I":
        terms = ({2: [(4, 1), (5, 1), (2, -1), (3, 1)],
                  1: [(4, 2 * r)],
                  3: [(6, 1), (7, r), (2, r), (3, -1)]})[alpha]
    elif name == "II":
        terms = ({2: [(4 if s == 0 else 5, 2)],
                  1: [(6, 1), (7, -r), (2, r), (3, 1)],
                  3: [(4, r), (5, -r), (2, -1), (3, -1)]})[alpha]
    elif name == "III":
        terms = ({2: [(4, 1), (5, -1), (2, 1), (3, 1)],
                  1: [(4, r), (7, r), (0, 1), (3, -1)],
                  3: [(4, r), (6, -1), (2, -r), (0, -1)]})[alpha]
    elif name == "IIIprime":
        terms = ({2: [(4, 1), (5, 1), (2, -1), (3, 1)],
                  1: [(4, r), (7, -r), (0, 1), (3, 1)],
                  3: [(4, r), (6, -1), (2, -r), (0, -1)]})[alpha]
    elif name == "IV":
        terms = ({2: [(4, 1), (5, -1), (2, 1), (3, 1)],
                  1: [(6, 1), (7, r), (2, r), (3, -1)],
                  3: [(2 if s == 0 else 1, 2)]})[alpha]
    elif name == "IVprime":
        terms = ({2: [(4, 1), (5, -1), (2, 1), (3, 1)],
                  1: [(6, 1), (7, r), (2, -r), (3, 1)],
                  3: [(1, -2)] if s == 0 else [(2, 2)]})[alpha]
    elif name == "F754":
        terms = ({2: [(5, 1), (6, r), (1, 1), (2, -r)],
                  1: [(4, 1), (7, -1), (1, 1), (2, 1)],
                  3: [(3, 2)]})[alpha]
    else:
        raise CheckFailure("UNKNOWN_NAMED_EXAMPLE", name)
    result = [0] * 8
    for row, coefficient in terms:
        result[row] += coefficient
    return result


def require_profile(z):
    support = [i for i, value in enumerate(z) if value]
    if len(support) == 1:
        require(abs(z[support[0]]) == 2, "SINGLETON_MAGNITUDE", z)
        return "singleton"
    require(len(support) == 4 and all(abs(z[i]) == 1 for i in support),
            "PLANE_SIZE_OR_MAGNITUDE", z)
    require(xor_all(support) == 0, "PLANE_NOT_AFFINE", z)
    sign_product = 1
    for i in support:
        sign_product *= z[i]
    require(sign_product == -1, "PLANE_SIGN_PRODUCT", z)
    return "plane"


def check_named_columns(spec, values):
    for s in range(2):
        for alpha in range(4):
            if s == 0 and alpha == 0:
                continue
            actual = column(values, s, alpha)
            expected = named_column(spec["name"], s, alpha)
            require(actual == expected, "NAMED_PROFILE_MISMATCH",
                    {"name": spec["name"], "s": s, "alpha": alpha,
                     "actual": actual, "expected": expected})


def graph_and_sites(spec, values):
    F = spec["F"]
    graph = [site(1, F[i], i, b) for i in range(4) for b in range(4)]
    mates = [[site(1, 1 - F[i], i, b) for b in range(4)] for i in range(4)]
    E = [[site(0, h, i, 0) for h in range(2)] for i in range(1, 4)]
    full = [site(0, h, 0, 0) for h in range(2)]
    Z = [site(0, h, i, b) for h in range(2) for i in range(4)
         for b in (1, 2, 3)]
    require(all(abs(values[p]) == 1 for p in graph), "GRAPH_CENSUS")
    require(all(values[p] == 0 for p in full), "FULL_SITE_NONZERO")
    all_D = [p for row in mates + E for p in row]
    require(len(all_D) == 22 and all(abs(values[p]) in (0, 2) for p in all_D),
            "D_VALUE_CENSUS")
    require(all(abs(values[p]) in (0, 2) for p in Z), "Z_VALUE_CENSUS")
    E_counts = (0,) + tuple(sum(values[p] != 0 for p in row) for row in E)
    M_counts = tuple(sum(values[p] != 0 for p in row) for row in mates)
    require(E_counts == spec["E"] and M_counts == spec["M"],
            "NAMED_OCCUPANCY", {"E": E_counts, "M": M_counts})
    d0 = [p for p in all_D if values[p] != 0]
    z2 = [p for p in Z if values[p] != 0]
    empty_z = [p for p in Z if values[p] == 0]
    require((len(d0), len(all_D) - len(d0), len(z2), len(empty_z)) ==
            (4, 18, 6, 18), "D_Z_CENSUS")
    require(sum(x * x for x in values) == 56, "X_ENERGY")
    W = d0 + z2
    require(len(set(W)) == 10, "W_CENSUS")
    return graph, W, {"F": list(F), "E_D0_by_row": list(E_counts),
                      "graph_mate_D0_by_row": list(M_counts),
                      "D0": len(d0), "D3": len(all_D) - len(d0),
                      "Z2": len(z2), "designated_Z4_site": empty_z[0],
                      "Z0": len(empty_z) - 1}


def clauses_c(x, graph, W):
    negatives = [p for p in graph if x[p] < 0]
    negative_W = [p for p in W if x[p] < 0]
    n, nW = len(negatives), len(negative_W)
    data = {"P_size": n, "N_size": nW, "xor_P": xor_all(negatives),
            "xor_W": xor_all(W)}
    require(n % 2 == 0, "C_GRAPH_PARITY", data)
    require((n // 2 + nW) % 2 == 1, "C_NEGATIVE_PARITY", data)
    require(data["xor_P"] == data["xor_W"], "C_LOCATION_XOR", data)
    return data


def require_eight_quotient(values):
    require(len(values) == 8 and all(abs(v) == 2 for v in values),
            "QUOTIENT_EIGHT_REQUIRED", values)


def check_examples():
    records = []
    saved = []
    for spec in SPECS:
        deadline()
        X = build_x(spec)
        graph, W, counts = graph_and_sites(spec, X)
        require(column(X, 0, 0) == [0] * 8, "ZERO_ETA", spec["name"])
        check_named_columns(spec, X)
        W_direct, W_fast = direct_walsh(X), butterfly_walsh(X)
        require(W_direct == W_fast, "X_WALSH_ALGORITHMS", spec["name"])
        kinds = {"singleton": 0, "plane": 0}
        profiles = []
        for s in range(2):
            for alpha in range(4):
                z = column(X, s, alpha)
                if s or alpha:
                    kind = require_profile(z)
                    kinds[kind] += 1
                    profiles.append({"s": s, "alpha": alpha, "Z": z,
                                     "kind": kind})
                quotient = []
                for nu in range(2):
                    for beta in range(4):
                        q = sum(z[(ell << 2) | i] *
                                pm((nu * ell) ^ parity(beta, i))
                                for ell in range(2) for i in range(4))
                        quotient.append(q)
                        k = site(nu, s, beta, alpha)
                        require(W_direct[k] == 4 * q, "QUOTIENT_IDENTITY",
                                [spec["name"], s, alpha, nu, beta])
                if s or alpha:
                    require_eight_quotient(quotient)
                else:
                    require(quotient == [0] * 8, "ZERO_QUOTIENT")
        require(len(profiles) == 7 and sum(kinds.values()) == 7,
                "PROFILE_COVERAGE")
        zero_C = None
        for t in range(64):
            if t % 8 == 0:
                deadline()
            x = [v * pm(parity(t, c)) for c, v in enumerate(X)]
            transformed = direct_walsh(x)
            require(transformed == butterfly_walsh(x), "TRANSPORT_WALSH", t)
            require(transformed == [W_direct[k ^ t] for k in range(64)],
                    "SPECIFIED_TRANSPORT", t)
            require(transformed[t] == 0, "CARRIED_ZERO", t)
            require(all(v in (-8, 0, 8) for v in transformed),
                    "U0_CAP_OR_DIVISIBILITY", t)
            C = clauses_c(x, graph, W)
            if t == 0:
                zero_C = C
        records.append({"name": spec["name"], "physical_counts": counts,
                        "profiles": profiles, "profile_kinds": kinds,
                        "C_at_t_zero": zero_C,
                        "transported_t_checked": 64,
                        "walsh_coefficients_each_transform": 64})
        saved.append((spec, X))
    return records, saved


def q2(b):
    return ((b >> 1) & 1) * (b & 1)


def odd_F_domain():
    return [tuple((mask >> i) & 1 for i in range(4)) for mask in range(16)
            if mask.bit_count() % 2 == 1]


def theta_inference():
    planes = [p for p in combinations(range(8), 4) if xor_all(p) == 0]
    intersections = sorted({len(set(p) & {4, 5, 6, 7}) for p in planes})
    require(intersections == [0, 2, 4], "PLANE_GRAPH_INTERSECTION")
    Fs = odd_F_domain()
    signs = list(product((-1, 1), repeat=4))
    cases = {"odd_multiplicity_excluded": 0,
             "multiplicity_four_excluded": 0, "remaining_2plus2": 0}
    for theta in product((1, 2, 3), repeat=4):
        mult = [theta.count(a) for a in (1, 2, 3)]
        for F in Fs:
            for sig in signs:
                if any(x % 2 for x in mult):
                    cases["odd_multiplicity_excluded"] += 1
                elif 4 in mult:
                    products = []
                    for s in range(2):
                        value = 1
                        for i in range(4):
                            value *= sig[i] * pm(s * F[i])
                        products.append(value)
                    require(products[0] == -products[1],
                            "FOUR_THETA_SIGN_FLIP")
                    cases["multiplicity_four_excluded"] += 1
                else:
                    require(sorted(mult) == [0, 2, 2] and xor_all(theta) == 0,
                            "THETA_2PLUS2_XOR")
                    cases["remaining_2plus2"] += 1
    require(sum(cases.values()) == 3 ** 4 * len(Fs) * len(signs),
            "THETA_COVERAGE")
    return {"affine_planes": len(planes), "graph_intersections": intersections,
            "cases_derived": cases, "odd_F_count": len(Fs),
            "row_sign_choices": len(signs)}


def mu_xor_guard(mu):
    require(len(mu) == 4 and all(0 <= x < 4 for x in mu) and xor_all(mu) == 0,
            "MU_XOR_NONZERO", list(mu))


def check_local_mates():
    patterns = list(product((-1, 1), repeat=4))
    residues = set()
    for D in patterns:
        row = []
        for alpha in range(4):
            hat = sum(D[b] * pm(parity(alpha, b)) for b in range(4))
            require(hat % 2 == 0, "MATE_HAT_NOT_EVEN", [D, alpha])
            value = (2 * hat) % 8
            row.append(value)
            for weight in (-1, 1):
                require((weight * 2 * hat) % 8 == value,
                        "MATE_WEIGHT_MOD8", [D, alpha, weight])
        require(len(set(row)) == 1, "MATE_ALPHA_MOD8", [D, row])
        require(row[0] == 4 * (sum(v < 0 for v in D) % 2),
                "MATE_NEGATIVE_PARITY", [D, row])
        residues.add(row[0])
    require(residues == {0, 4}, "MATE_RESIDUE_DOMAIN")
    aggregate = {0}
    for _ in range(4):
        aggregate = {(x + y) % 8 for x in aggregate for y in residues}
    require(aggregate == {0, 4}, "MATE_AGGREGATE_DOMAIN")
    return {"local_sign_patterns_checked": len(patterns),
            "alphas_each": 4, "row_weights_each": 2,
            "one_row_residues": sorted(residues),
            "four_row_sum_residues": sorted(aggregate),
            "all_four_row_arrays_enumerated": False}, sorted(aggregate)


def validate_slice_parities(slices):
    require(len(slices) == 2 and all(len(row) == 16 for row in slices),
            "SLICE_DIMENSION")
    require(all(len({a % 2 for a in row}) == 1 for row in slices),
            "SLICE_NOT_UNIFORM")
    require(slices[0][0] % 2 != slices[1][0] % 2,
            "SLICE_PARITY_NOT_OPPOSITE")


def check_uniform_graph(aggregate_residues):
    mu_domain = [(a, b, c, a ^ b ^ c)
                 for a in range(4) for b in range(4) for c in range(4)]
    sign_domain = list(product((-1, 1), repeat=4))
    Fs = odd_F_domain()
    require(len(mu_domain) == 4 ** 3 and len(set(mu_domain)) == len(mu_domain),
            "MU_DOMAIN_COVERAGE")
    graph_cases = 0
    row_walsh_checks = 0
    triple_cells = 0
    residue_cells = 0
    for mu in mu_domain:
        mu_xor_guard(mu)
        for tau in sign_domain:
            for F in Fs:
                if graph_cases % 64 == 0:
                    deadline()
                # Direct b-sum, independently checked against bent dual formula.
                dual = []
                for alpha in range(4):
                    row = []
                    for i in range(4):
                        direct = sum(tau[i] * pm(q2(b) ^ parity(mu[i], b) ^
                                                 parity(alpha, b))
                                     for b in range(4))
                        formula = 2 * tau[i] * pm(q2(alpha ^ mu[i]))
                        require(direct == formula, "BENT_DUAL_FORMULA",
                                [mu, tau, F, i, alpha, direct, formula])
                        row.append(direct // 2)
                        row_walsh_checks += 1
                    dual.append(row)
                parity_slices = {r: [[], []] for r in aggregate_residues}
                for s in range(2):
                    for alpha in range(4):
                        for beta in range(4):
                            terms = [dual[alpha][i] *
                                     pm(parity(beta, i) ^ (s * F[i]))
                                     for i in range(4)]
                            graph_value = 2 * sum(terms)
                            require(graph_value % 4 == 0, "GRAPH_NOT_MULTIPLE4")
                            negatives = sum(term < 0 for term in terms)
                            require((graph_value // 4) % 2 == negatives % 2,
                                    "GRAPH_SIGN_PARITY")
                            triple_cells += 1
                            for residue in aggregate_residues:
                                value = graph_value + residue
                                require(value % 4 == 0, "PARTIAL_NOT_MULTIPLE4")
                                parity_slices[residue][s].append(value // 4)
                                residue_cells += 1
                for slices in parity_slices.values():
                    validate_slice_parities(slices)
                graph_cases += 1
    require(graph_cases == len(mu_domain) * len(sign_domain) * len(Fs),
            "GRAPH_CASE_COVERAGE")
    require(row_walsh_checks == graph_cases * 4 * 4, "ROW_COVERAGE")
    require(triple_cells == graph_cases * 2 * 4 * 4, "TRIPLE_COVERAGE")
    require(residue_cells == triple_cells * len(aggregate_residues),
            "RESIDUE_COVERAGE")
    return {"mu_tuples_derived": len(mu_domain),
            "row_sign_tuples_derived": len(sign_domain),
            "odd_F_tuples_derived": len(Fs), "graph_cases": graph_cases,
            "direct_bent_row_values": row_walsh_checks,
            "s_alpha_beta_cells": triple_cells,
            "aggregate_residue_cell_checks": residue_cells,
            "full_Y_search": False}


def integer_arithmetic():
    # Enumerate signed-pair magnitudes after division by four.  Opposite parity
    # and a+b<=3 are the 4 mod 8 residue and common pair-cap consequences.
    pairs = []
    for a in range(4):
        for b in range(4):
            if a + b <= 3 and (a - b) % 2:
                small = int(abs(a + b) == 1) + int(abs(a - b) == 1)
                pairs.append((a, b, small))
    expected = [(0, 1, 2), (0, 3, 0), (1, 0, 2),
                (1, 2, 1), (2, 1, 1), (3, 0, 0)]
    require(pairs == expected, "SMALL_PAIR_CLASSIFICATION", pairs)
    small_totals = [k for k in range(65)
                    if 16 * k + 144 * (64 - k) == 64 * 128]
    require(small_totals == [8], "FULL_PARSEVAL_SMALL_COUNT", small_totals)
    solutions = []
    for n in range(17):
        for m in range(17):
            if n + m > 8 or m + 4 * n + 9 * (16 - m) != 160:
                continue
            # h of the m odd |A1|=4 pairs have |A0|=0, rather than 8;
            # q of the 16-n even |A1|=0 pairs have |A0|=4, rather than 12.
            for h in range(m + 1):
                for q in range(17 - n):
                    if n + m + h + 2 * q == 8:
                        solutions.append({"n": n, "m": m, "h": h, "q": q})
    require(solutions == [{"n": 4, "m": 0, "h": 0, "q": 2},
                          {"n": 6, "m": 1, "h": 1, "q": 0}],
            "N_M_SMALL_CASES", solutions)
    require(all(item["h"] == item["m"] for item in solutions),
            "ODD_SLICE_A0_NOT_FORCED_ZERO")

    # Broader paired-frequency arithmetic table: this is only a relaxation,
    # and z4 below is a number of frequency pairs, NOT the physical Z4 site.
    table = {}
    for d in (0, 2, 4):
        rows = {}
        for E in range(9):
            for O in range(9 - E):
                for P in range(33):
                    Z = 32 - E - O - P
                    if Z < 0 or O + 4 * E + 9 * P != 128 + 8 * d:
                        continue
                    for H in range(O + 1):
                        for z4 in range(Z + 1):
                            if E + O + H + 2 * z4 == 8:
                                rows.setdefault((E, O, P, Z), []).append((H, z4))
        table[d] = rows
    expected_table = {
        0: {(0, 2, 14, 16): [(0, 3), (2, 2)],
            (1, 7, 13, 11): [(0, 0)],
            (2, 3, 13, 14): [(1, 1), (3, 0)],
            (4, 4, 12, 12): [(0, 0)], (7, 1, 11, 13): [(0, 0)]},
        2: {(0, 0, 16, 16): [(0, 4)],
            (1, 5, 15, 11): [(0, 1), (2, 0)],
            (2, 1, 15, 14): [(1, 2)],
            (4, 2, 14, 12): [(0, 1), (2, 0)]},
        4: {(0, 7, 17, 8): [(1, 0)],
            (1, 3, 17, 11): [(0, 2), (2, 1)],
            (3, 4, 16, 9): [(1, 0)], (4, 0, 16, 12): [(0, 2)],
            (6, 1, 15, 10): [(1, 0)]}}
    require(table == expected_table, "NECESSARY_INTEGER_TABLE", table)
    serial_table = {str(d): [{"E_O_P_Z": list(key),
                               "H_zsmall": [list(pair) for pair in values]}
                              for key, values in sorted(rows.items())]
                    for d, rows in table.items()}
    return {"paired_cases_a_b_small": [list(p) for p in pairs],
            "total_small_full_coefficients": small_totals,
            "n_m_allocations": solutions, "relaxed_integer_table": serial_table}


def check_opposite_z(value):
    require(value in (-2, 0, 2), "OPPOSITE_ANOTHER_Z4", value)


def noncancellation():
    checks = 0
    for s in range(2):
        for zsign in (-1, 1):
            for opposite in (-2, 0, 2):
                check_opposite_z(opposite)
                require(4 * zsign + pm(s) * opposite != 0,
                        "Z4_UNEXPECTED_CANCELLATION")
                checks += 1
    return {"opposite_types": [-2, 0, 2], "s_values": 2,
            "Z4_signs": 2, "noncancellation_checks": checks,
            "inversion_is_written_import_not_computationally_proved": True}


def controls(saved):
    found = []
    bad_mu = (0, 0, 0, 1)
    products = []
    for alpha in range(4):
        value = 1
        for mu in bad_mu:
            value *= pm(q2(alpha ^ mu))
        products.append(value)
    require(len(set(products)) > 1, "XOR_MUTANT_NOT_DISCRIMINATING")
    found.append(expect_reason(lambda: mu_xor_guard(bad_mu), "MU_XOR_NONZERO"))

    # Same multiset of (|A1|/4,|A0|/4), same energy and small count as the
    # n=4,m=0 formal case, but one complete pair exchanged between slices.
    pairs = [[(2, 1)] * 4 + [(0, 1)] * 2 + [(0, 3)] * 10,
             [(3, 0)] * 16]
    original = [list(row) for row in pairs]
    pairs[0][6], pairs[1][0] = pairs[1][0], pairs[0][6]
    require(sorted(original[0] + original[1]) == sorted(pairs[0] + pairs[1]),
            "SLICE_MUTANT_CHANGED_MULTISET")
    found.append(expect_reason(
        lambda: validate_slice_parities([[a for a, _ in row] for row in pairs]),
        "SLICE_NOT_UNIFORM"))
    found.append(expect_reason(lambda: validate_slice_parities([[0] * 16,
                                                                 [2] * 16]),
                               "SLICE_PARITY_NOT_OPPOSITE"))
    require(-4 + 4 == 0, "Z4_MUTANT_NOT_DISCRIMINATING")
    found.append(expect_reason(lambda: check_opposite_z(4),
                               "OPPOSITE_ANOTHER_Z4"))
    spec, X = saved[0]
    corrupt = list(X)
    p = site(0, 0, 2, 2)
    require(corrupt[p] == 2, "MUTANT_LITERAL_SITE")
    corrupt[p] = -corrupt[p]
    found.append(expect_reason(lambda: check_named_columns(spec, corrupt),
                               "NAMED_PROFILE_MISMATCH"))
    good_z = column(X, 1, 0)
    quotient = [sum(good_z[(ell << 2) | i] *
                    pm((nu * ell) ^ parity(beta, i))
                    for ell in range(2) for i in range(4))
                for nu in range(2) for beta in range(4)]
    require_eight_quotient(quotient)
    found.append(expect_reason(lambda: require_eight_quotient(quotient[:4]),
                               "QUOTIENT_EIGHT_REQUIRED"))
    return {"reason_specific_mutations": found,
            "nonzero_xor_product_over_alpha": products,
            "slice_mutant_preserves_joint_pair_multiset": True,
            "mutants_claim_physical_realizability": False}


def main():
    examples, saved = check_examples()
    deadline()
    theta = theta_inference()
    local_mates, aggregate = check_local_mates()
    graph = check_uniform_graph(aggregate)
    arithmetic = integer_arithmetic()
    unique_Z4 = noncancellation()
    mutations = controls(saved)
    deadline()
    return {"status": "PASS_FINITE_SCOPES_ONLY", "source_status_before_GO": "NOTTESTED",
            "examples": examples, "theta_inference": theta,
            "local_mates": local_mates, "uniform_graph_parity": graph,
            "integer_cases": arithmetic, "unique_Z4": unique_Z4,
            "negative_controls": mutations,
            "limitations": [
                "No full common-Y sign completion or U3-cap witness constructed",
                "No enumeration of all full-Y arrays or all 16^4 mate arrays",
                "X examples are not physical inverse/J1/all-U3 callers",
                "General graph phase, physical inverse, common-Y residue and Walsh inversion are imports",
                "No d_E=0/2 exclusion, V or global rank2/five-span/NL242 conclusion",
                "No independent-family, human, kernel, novelty or parent adoption claim"],
            "elapsed_seconds": time.monotonic() - START}


if __name__ == "__main__":
    try:
        result = main()
    except DeadlineReached:
        print(json.dumps({"status": "INCOMPLETE_COOPERATIVE_DEADLINE",
                          "deadline_seconds": DEADLINE_SECONDS}, sort_keys=True))
        raise SystemExit(2)
    except CheckFailure as error:
        print(json.dumps({"status": "FAIL", "reason": error.reason,
                          "detail_repr": repr(error.detail)}, sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))
