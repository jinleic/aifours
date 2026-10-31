from fractions import Fraction as Q
from itertools import product
from math import prod
from time import monotonic

DEADLINE = monotonic() + 55.0

class InvariantError(Exception):
    def __init__(self, tag, detail=""):
        super().__init__(tag + ": " + detail)
        self.tag = tag
        self.detail = detail

def need(condition, tag, detail=""):
    if monotonic() > DEADLINE:
        raise RuntimeError("55-second cooperative deadline exceeded")
    if not condition:
        raise InvariantError(tag, detail)

def multiply(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return tuple(out)

def from_roots(roots):
    p = (Q(1),)
    for r in roots:
        p = multiply(p, (r, Q(-1)))
    return p

def value(p, t):
    out = Q(0)
    for c in reversed(p):
        out = out * t + c
    return out

def derivative_value(p, t):
    return sum((k * p[k] * t ** (k - 1)
                for k in range(1, len(p))), Q(0))

def shifted_constant(p, delta):
    return (p[0] + delta,) + p[1:]

def sign(x):
    return (x > 0) - (x < 0)

BOUNDS = (
    (Q(15, 4), Q(17, 4)),
    (Q(1197, 80), Q(15)),
    (Q(11), Q(11)),
    (Q(23), Q(467, 20)),
    (Q(13, 2), Q(13, 2)),
    (Q(179, 20), Q(9)),
    (Q(1), Q(1)),
    (Q(1), Q(1)),
)
CHOICES = tuple(tuple(sorted(set(pair))) for pair in BOUNDS)
CORNERS = tuple(tuple(a) for a in product(*CHOICES))
need(len(CORNERS) == 16 and len(set(CORNERS)) == 16,
     "ACTUAL_CORNER_COUNT")

def parity_values(member, t):
    even, odd = Q(0), Q(0)
    for j, coefficient in enumerate(member):
        term = coefficient * ((-1) ** (j // 2)) * t ** (j // 2)
        if j % 2:
            odd += term
        else:
            even += term
    return even, odd

def coefficient_envelopes(parity):
    lower, upper = [], []
    for k, j in enumerate(range(parity, 8, 2)):
        lo, hi = BOUNDS[j]
        s = (-1) ** k
        lower.append(s * (lo if s > 0 else hi))
        upper.append(s * (hi if s > 0 else lo))
    return tuple(lower), tuple(upper)

def corner(even_label, odd_label):
    out = []
    for j, (lo, hi) in enumerate(BOUNDS):
        label = odd_label if j % 2 else even_label
        s = (-1) ** (j // 2)
        pick_high = (label == "+") if s > 0 else (label == "-")
        out.append(hi if pick_high else lo)
    result = tuple(out)
    need(result in CORNERS, "ACTUAL_CORNER_MEMBERSHIP")
    return result

E_ROOTS = (Q(1, 2), Q(2), Q(4))
OM_ROOTS = (Q(19, 20), Q(7, 2), Q(9, 2))
OP_ROOTS = (Q(1), Q(3), Q(5))
F_ROOTS = (Q(0), Q(1), Q(9, 2))
E0 = from_roots(E_ROOTS)
EM = shifted_constant(E0, Q(-1, 4))
EP = shifted_constant(E0, Q(1, 4))
OM, OP = from_roots(OM_ROOTS), from_roots(OP_ROOTS)
F = from_roots(F_ROOTS)
need(E0 == (Q(4), Q(-11), Q(13, 2), Q(-1)),
     "EVEN_FACTOR_EXPANSION")
need(coefficient_envelopes(0) == (EM, EP),
     "EVEN_BOX_VS_FACTORS")
need(coefficient_envelopes(1) == (OM, OP),
     "ODD_BOX_VS_FACTORS")
need(tuple(OP[k] - OM[k] for k in range(4)) ==
     (Q(3, 80), Q(7, 20), Q(1, 20), Q(0)),
     "ODD_ENVELOPE_DIFFERENCE")
need(F == (Q(0), Q(-9, 2), Q(11, 2), Q(-1)),
     "NUMERATOR_FACTOR_EXPANSION")

a, b, c, d, e, f = (
    Q(19, 20), Q(1), Q(3), Q(7, 2), Q(9, 2), Q(5)
)
ODD_ENDPOINTS = (
    (a, Q(0), Q(3321, 8000)),
    (b, Q(-7, 16), Q(0)),
    (c, Q(-123, 80), Q(0)),
    (d, Q(0), Q(15, 8)),
    (e, Q(0), Q(21, 8)),
    (f, Q(-243, 80), Q(0)),
)
for t, low, high in ODD_ENDPOINTS:
    need((value(OM, t), value(OP, t)) == (low, high),
         "ODD_ENDPOINT_EXACT_VALUE", str(t))

EVEN_ENDPOINTS = (
    (Q(0), EM, Q(15, 4), 1),
    (a, EP, Q(-9529, 8000), -1),
    (b, EP, Q(-5, 4), -1),
    (c, EM, Q(9, 4), 1),
    (d, EM, Q(2), 1),
    (e, EP, Q(-19, 4), -1),
    (f, EP, Q(-53, 4), -1),
)
for t, envelope, exact, required_sign in EVEN_ENDPOINTS:
    need(value(envelope, t) == exact,
         "EVEN_ENDPOINT_EXACT_VALUE", str(t))
    for member in CORNERS:
        E, O = parity_values(member, t)
        need(sign(E) == required_sign,
             "CORNER_HB_ENDPOINT_SIGN", str((t, member)))
        need(member[0] + member[2] + member[4] + member[6] > 0,
             "HB_REAL_POINT_EVEN_ORIENTATION")
        need(member[1] + member[3] + member[5] + member[7] > 0,
             "HB_REAL_POINT_ODD_ORIENTATION")

h = Q(1, 10000)
NODES = (Q(1, 2), Q(39, 40), Q(1) - h, Q(1) + h, Q(7, 2))
LABELS = (("+", "+"), ("+", "-"), ("+", "+"), ("-", "+"), ("-", "+"))
MEMBERS = tuple(corner(ep, op) for ep, op in LABELS)
need(all(t > 0 for t in NODES) and
     all(NODES[i] < NODES[i + 1] for i in range(4)),
     "POSITIVE_ORDERED_DISTINCT_NODES")

POINTS = tuple(sorted(set((Q(0), a, b, c, d, e, f) + NODES)))
for t in POINTS:
    values = tuple(parity_values(member, t) for member in CORNERS)
    need(min(x[0] for x in values) == value(EM, t) and
         max(x[0] for x in values) == value(EP, t),
         "FINITE_EVEN_ENVELOPE", str(t))
    need(min(x[1] for x in values) == value(OM, t) and
         max(x[1] for x in values) == value(OP, t),
         "FINITE_ODD_ENVELOPE", str(t))

EO = tuple(parity_values(member, t)
           for member, t in zip(MEMBERS, NODES))
FV = tuple(value(F, t) for t in NODES)
HP = tuple(prod((t - s for j, s in enumerate(NODES) if j != i),
                start=Q(1)) for i, t in enumerate(NODES))
EXPECTED = (
    (Q(1, 4), Q(45, 8), Q(-1), Q(1424999943, 4000000000)),
    (Q(-78259, 64000), Q(-14241, 64000), Q(-5499, 64000),
     Q(-119935581, 160000000000)),
    (Q(-1249899964999, 10**12), Q(800060001, 10**12),
     Q(-349974999, 10**12), Q(62240039502, 10**16)),
    (Q(-1750099965001, 10**12), Q(-799940001, 10**12),
     Q(350024999, 10**12), Q(-62760039498, 10**16)),
    (Q(2), Q(15, 8), Q(35, 4), Q(189374999697, 4000000000)),
)
for i, ((E, O), t, (ep, op)) in enumerate(zip(EO, NODES, LABELS)):
    need((E, O, FV[i], HP[i]) == EXPECTED[i],
         "EXACT_ATOM_TABLE", str(i + 1))
    E_factor = prod((r - t for r in E_ROOTS), start=Q(1))
    E_factor += Q(1, 4) if ep == "+" else Q(-1, 4)
    roots = OP_ROOTS if op == "+" else OM_ROOTS
    O_factor = prod((r - t for r in roots), start=Q(1))
    need((E, O) == (E_factor, O_factor),
         "RAW_COEFFICIENT_VS_FACTOR_ATOM", str(i + 1))
need(tuple(sign(O) for E, O in EO) == (1, -1, 1, -1, 1),
     "ODD_RAY_ORIENTATION")
need(tuple(sign(x) for x in HP) == (1, -1, 1, -1, 1),
     "LAGRANGE_DERIVATIVE_SIGNS")
MU = tuple(1 / (t * EO[i][1] * HP[i]) for i, t in enumerate(NODES))
need(all(w > 0 for w in MU), "POSITIVE_RAY_WEIGHTS")

def verify_even_minimizers(members):
    for i, (member, t) in enumerate(zip(members, NODES)):
        need(member in CORNERS, "ACTUAL_CORNER_MEMBERSHIP", str(i + 1))
        selected = parity_values(member, t)[0] * value(F, t)
        minimum = min(parity_values(v, t)[0] * value(F, t)
                      for v in CORNERS)
        need(selected == minimum, "EVEN_POINTWISE_MINIMIZER", str(i + 1))

verify_even_minimizers(MEMBERS)

def verify_moments(weights):
    for r in range(4):
        moment = sum((weights[i] * t ** (r + 1) * EO[i][1]
                      for i, t in enumerate(NODES)), Q(0))
        need(moment == 0, "ODD_MOMENTS", str((r, moment)))

verify_moments(MU)
for r in range(5):
    lagrange = sum((t ** r / HP[i] for i, t in enumerate(NODES)), Q(0))
    need(lagrange == (Q(1) if r == 4 else Q(0)),
         "LAGRANGE_NORMALIZATION", str(r))

ROWS = []
for t, (E, O) in zip(NODES, EO):
    row = []
    for j in range(8):
        k = j // 2
        row.append(((-1) ** k) * t ** (k + j % 2) *
                   (O if j % 2 else E))
    need(tuple(row) == (E, t*O, -t*E, -t*t*O,
                        t*t*E, t**3*O, -t**3*E, -t**4*O),
         "RAW_ROW_SIGN_CONVENTION")
    ROWS.append(tuple(row))
M = tuple(sum((MU[i] * ROWS[i][j] for i in range(5)), Q(0))
          for j in range(8))
U = tuple(sum((MU[i] * t**r * EO[i][0]
               for i, t in enumerate(NODES)), Q(0)) for r in range(4))
need(M == (U[0], Q(0), -U[1], Q(0), U[2], Q(0), -U[3], Q(0)),
     "ALL_EIGHT_COORDINATES")
need(tuple(sign(x) for x in M) == (-1, 0, 1, 0, -1, 0, 1, 0),
     "AGGREGATE_SIGNS_NOT_EIGHT_STRICT_NEGATIVES")
need(MU[0] < Q(5, 3) and MU[4] < Q(1, 180) and MU[2] > 5000000,
     "EVEN_MOMENT_WEIGHT_BOUNDS")
for r in range(4):
    need(0 < MU[0] * NODES[0]**r * EO[0][0] < 1,
         "FIRST_POSITIVE_EVEN_CONTRIBUTION", str(r))
    need(0 < MU[4] * NODES[4]**r * EO[4][0] < 1,
         "LAST_POSITIVE_EVEN_CONTRIBUTION", str(r))
    need(MU[2] * NODES[2]**r * EO[2][0] < -2500000,
         "DOMINANT_NEGATIVE_EVEN_CONTRIBUTION", str(r))
    need(U[r] < -2499998, "EVEN_MOMENT_STRICT_BOUND", str(r))

B = (Q(0), Q(0), Q(9, 2), Q(0), Q(11, 2), Q(0), Q(1), Q(0))
CONTRIBUTIONS = tuple(MU[i] * EO[i][0] * FV[i] for i in range(5))
L = sum(CONTRIBUTIONS, Q(0))
for i in range(5):
    need(sum((B[j] * ROWS[i][j] for j in range(8)), Q(0)) ==
         EO[i][0] * FV[i], "COEFFICIENT_ROW_PAIRING", str(i + 1))
need(sum((B[j] * M[j] for j in range(8)), Q(0)) == L,
     "DIRECT_AGGREGATE_PAIRING")
need(Q(9, 2)*M[2] + Q(11, 2)*M[4] + M[6] == L,
     "EVEN_COORDINATE_PAIRING_IDENTITY")

C = []
for i, (t, (E, O), (ep, op)) in enumerate(zip(NODES, EO, LABELS)):
    offset = Q(1, 4) if ep == "+" else Q(-1, 4)
    E_factor = prod((r - t for r in E_ROOTS), start=Q(1)) + offset
    if op == "+":
        cancelled = -E_factor * (Q(9, 2) - t) / ((3 - t) * (5 - t))
    else:
        numerator = prod((r - t for r in F_ROOTS), start=Q(1))
        denominator = t * prod((r - t for r in OM_ROOTS), start=Q(1))
        cancelled = E_factor * numerator / denominator
    need(cancelled == E * FV[i] / (t * O),
         "FACTORIZED_VS_COEFFICIENT_SCALAR", str(i + 1))
    C.append(cancelled)
need((C[0], C[1], C[4]) == (Q(-4, 45), Q(-78259, 161600), Q(8, 3)),
     "UNPAIRED_EXACT_CANCELLED_VALUES")
need(sum((C[i] / HP[i] for i in range(5)), Q(0)) == L,
     "FACTOR_FORMULA_TOTAL_PAIRING")

def D(t):
    return (t - Q(1, 2)) * (t - Q(39, 40)) * (Q(7, 2) - t)

D3, D4 = D(NODES[2]), D(NODES[3])
need((D3, D4) == (Q(31120019751, 10**12), Q(31380019749, 10**12)),
     "PAIRED_DENOMINATORS_EXACT")
need(HP[2] == 2*h*D3 and HP[3] == -2*h*D4,
     "PAIRED_DERIVATIVE_SIGNS")
direct_pair = CONTRIBUTIONS[2] + CONTRIBUTIONS[3]
factor_pair = (C[2]/D3 - C[3]/D4) / (2*h)
need(direct_pair == factor_pair, "PAIR_DECOMPOSITION_SIGN")
need(0 < C[2] < Q(3, 5) and C[3] > Q(7, 10),
     "PAIRED_NUMERATOR_BOUNDS")
need(D3 > Q(3, 100) and 0 < D4 < Q(4, 125),
     "PAIRED_DENOMINATOR_BOUNDS")
need(direct_pair < -9375, "PAIRED_NEGATIVE_BOUND")
need(CONTRIBUTIONS[0] < 0 and 0 < CONTRIBUTIONS[1] < 1500 and
     0 < CONTRIBUTIONS[4] < 1, "UNPAIRED_CONTRIBUTION_BOUNDS")
need(L < -7874, "FIXED_F_SCALAR_BOUND")

dF, dO = derivative_value(F, Q(1)), derivative_value(OP, Q(1))
need(value(F, Q(1)) == value(OP, Q(1)) == 0 and
     (dF, dO) == (Q(7, 2), Q(-8)), "DERIVATIVE_COMMON_ZERO_DATA")
g_plus = -dF * value(EP, Q(1)) / dO
g_minus = -dF * value(EM, Q(1)) / dO
need((g_plus, g_minus) == (Q(-35, 64), Q(-49, 64)) and
     g_plus != g_minus, "INCOMPATIBLE_G_AT_ONE")

CONTROL_RESULTS = []

def expect_rejection(label, expected_tag, action):
    try:
        action()
    except InvariantError as failure:
        need(failure.tag == expected_tag, "WRONG_MUTATION_FAILURE",
             label + ": " + failure.tag)
        CONTROL_RESULTS.append((label, failure.tag, failure.detail))
    else:
        raise InvariantError("MUTATION_NOT_REJECTED", label)

def verify_odd_minimum(candidate):
    true_min = min(parity_values(v, Q(1))[1] for v in CORNERS)
    need(value(candidate, Q(1)) == true_min, "ODD_ENVELOPE_MINIMUM",
         "candidate=" + str(value(candidate, Q(1))) +
         ", true_min=" + str(true_min))

verify_odd_minimum(OM)
bad_odd = list(OM)
bad_odd[1] = Q(-23)
bad_member = list(corner("-", "-"))
bad_member[3] = Q(23)
need(tuple(bad_member) in CORNERS, "MUTATION_SETUP_ODD_ACTUAL_MEMBER")
need(value(tuple(bad_odd), Q(1)) ==
     parity_values(tuple(bad_member), Q(1))[1] == Q(-7, 80),
     "MUTATION_SETUP_ODD_VALUE")
need(value(tuple(bad_odd), Q(1)) - value(OM, Q(1)) == Q(7, 20),
     "MUTATION_SETUP_ODD_GAP")
expect_rejection("wrong odd envelope coefficient", "ODD_ENVELOPE_MINIMUM",
                 lambda: verify_odd_minimum(tuple(bad_odd)))

bad_members = list(MEMBERS)
bad_members[3] = corner("+", "+")
need(all(v in CORNERS for v in bad_members),
     "MUTATION_SETUP_STALE_EVEN_ACTUAL")
need((parity_values(bad_members[3], NODES[3])[0] - EO[3][0]) * FV[3] ==
     FV[3] / 2 > 0, "MUTATION_SETUP_STALE_EVEN_GAP")
expect_rejection("stale actual even minimizer", "EVEN_POINTWISE_MINIMIZER",
                 lambda: verify_even_minimizers(tuple(bad_members)))

bad_mu = list(MU)
bad_mu[0] *= 2
need(all(w > 0 for w in bad_mu), "MUTATION_SETUP_POSITIVE_WEIGHTS")
bad_moment = sum((bad_mu[i] * t * EO[i][1]
                  for i, t in enumerate(NODES)), Q(0))
need(bad_moment == 1 / HP[0] > 0, "MUTATION_SETUP_MOMENT_RESIDUAL")
expect_rejection("positive weight moment corruption", "ODD_MOMENTS",
                 lambda: verify_moments(tuple(bad_mu)))

bad_pair = (C[2]/D3 + C[3]/D4) / (2*h)
need(bad_pair - direct_pair == C[3] / (h*D4) > 0,
     "MUTATION_SETUP_PAIRED_SIGN_GAP")
expect_rejection(
    "wrong paired sign", "PAIR_DECOMPOSITION_SIGN",
    lambda: need(bad_pair == direct_pair, "PAIR_DECOMPOSITION_SIGN",
                 "addition does not reconstruct the direct pair"))

need(len(CONTROL_RESULTS) == 4, "CONTROL_COUNT")
print("FINITE_CHECKS_PASS")
print("actual_corner_count", len(CORNERS))
for i in range(5):
    print("atom", i + 1, "u", NODES[i],
          "member", " ".join(str(x) for x in MEMBERS[i]))
    print("E O F Hprime", EO[i][0], EO[i][1], FV[i], HP[i])
    print("mu", MU[i], "scalar_contribution", CONTRIBUTIONS[i])
for r, x in enumerate(U):
    print("U", r, x)
for j, x in enumerate(M):
    print("M", j, x)
print("aggregate_signs", tuple(sign(x) for x in M))
print("L_direct", L)
print("L_factorized", sum((C[i] / HP[i] for i in range(5)), Q(0)))
print("paired_contribution", direct_pair)
print("required_G_at_one", g_plus, g_minus)
for label, tag, detail in CONTROL_RESULTS:
    print("CONTROL_REJECTED", label, tag, detail)
print("LIMITS: finite exact checks only; no universal HB/cusp gate,")
print("novelty, other-F exclusion, or common-SPR synthesis acceptance.")
