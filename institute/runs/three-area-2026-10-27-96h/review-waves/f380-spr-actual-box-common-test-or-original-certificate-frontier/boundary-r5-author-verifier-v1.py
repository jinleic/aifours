
from fractions import Fraction as Q

def need(condition, reason):
    if not condition:
        raise ValueError(reason)

def product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result

def sign(value):
    return (value > 0) - (value < 0)

def roots_coefficients(roots):
    coefficients = [Q(1)]
    for root in roots:
        updated = [Q(0)] * (len(coefficients) + 1)
        for j, value in enumerate(coefficients):
            updated[j] += root * value
            updated[j + 1] -= value
        coefficients = updated
    return tuple(coefficients)

e0_coeff = roots_coefficients((Q(1, 2), Q(2), Q(4)))
om_coeff = roots_coefficients((Q(19, 20), Q(7, 2), Q(9, 2)))
op_coeff = roots_coefficients((Q(1), Q(3), Q(5)))

need(e0_coeff == (Q(4), Q(-11), Q(13, 2), Q(-1)), "even expansion")
need(
    om_coeff == (Q(1197, 80), Q(-467, 20), Q(179, 20), Q(-1)),
    "odd minus expansion",
)
need(op_coeff == (Q(15), Q(-23), Q(9), Q(-1)), "odd plus expansion")
need(
    tuple(p - m for p, m in zip(op_coeff, om_coeff))
    == (Q(3, 80), Q(7, 20), Q(1, 20), Q(0)),
    "actual odd width polynomial",
)

def even(t, endpoint):
    return (Q(1, 2) - t) * (2 - t) * (4 - t) + Q(endpoint, 4)

def odd(t, endpoint):
    if endpoint == 1:
        return (1 - t) * (3 - t) * (5 - t)
    if endpoint == -1:
        return (Q(19, 20) - t) * (Q(7, 2) - t) * (Q(9, 2) - t)
    raise ValueError("odd endpoint label")

def test_f(t):
    return -t * (1 - t) * (Q(9, 2) - t)

hb_nodes = (Q(19, 20), Q(1), Q(3), Q(7, 2), Q(9, 2), Q(5))
hb_signs = (-1, -1, 1, 1, -1, -1)
for t, wanted in zip(hb_nodes, hb_signs):
    for endpoint in (-1, 1):
        need(sign(even(t, endpoint)) == wanted, "uniform even HB sign")
need(even(Q(0), -1) == Q(15, 4), "positive even constant")

intervals = (
    (Q(15, 4), Q(17, 4)),
    (Q(1197, 80), Q(15)),
    (Q(11), Q(11)),
    (Q(23), Q(467, 20)),
    (Q(13, 2), Q(13, 2)),
    (Q(179, 20), Q(9)),
    (Q(1), Q(1)),
    (Q(1), Q(1)),
)

def actual_coefficients(e_endpoint, o_endpoint):
    oc = op_coeff if o_endpoint == 1 else om_coeff
    return (
        Q(4) + Q(e_endpoint, 4), oc[0], Q(11), -oc[1],
        Q(13, 2), oc[2], Q(1), Q(1),
    )

h = Q(1, 10000)
nodes = (Q(1, 2), Q(39, 40), 1 - h, 1 + h, Q(7, 2))
e_labels = (1, 1, 1, -1, -1)
o_labels = (1, -1, 1, 1, 1)
need(all(nodes[i] < nodes[i + 1] for i in range(4)), "node order")

evens = []
odds = []
for t, et, ot in zip(nodes, e_labels, o_labels):
    coefficients = actual_coefficients(et, ot)
    need(
        all(lo <= c <= hi for c, (lo, hi) in zip(coefficients, intervals)),
        "actual coefficient membership",
    )
    ep = sum(((-1) ** r) * coefficients[2 * r] * t ** r for r in range(4))
    op = sum(((-1) ** r) * coefficients[2 * r + 1] * t ** r for r in range(4))
    need(ep == even(t, et), "direct even parity")
    need(op == odd(t, ot), "direct odd parity")
    need(et == (-1 if test_f(t) >= 0 else 1), "piecewise actual even envelope")
    evens.append(ep)
    odds.append(op)

need(tuple(map(sign, odds)) == (1, -1, 1, -1, 1), "R5 odd orientation")
derivatives = tuple(
    product(t - v for j, v in enumerate(nodes) if j != i)
    for i, t in enumerate(nodes)
)
weights = tuple(
    1 / (t * o * derivative)
    for t, o, derivative in zip(nodes, odds, derivatives)
)
need(all(w > 0 for w in weights), "positive actual R5 weights")

for r in range(4):
    need(
        sum(t ** r / derivative for t, derivative in zip(nodes, derivatives)) == 0,
        "Lagrange annihilation",
    )
need(
    sum(t ** 4 / derivative for t, derivative in zip(nodes, derivatives)) == 1,
    "Lagrange normalization",
)

rows = tuple(
    (e, t * o, -t * e, -t ** 2 * o,
     t ** 2 * e, t ** 3 * o, -t ** 3 * e, -t ** 4 * o)
    for t, e, o in zip(nodes, evens, odds)
)
aggregate = tuple(
    sum(w * row[j] for w, row in zip(weights, rows))
    for j in range(8)
)
need(
    tuple(map(sign, aggregate)) == (-1, 0, 1, 0, -1, 0, 1, 0),
    "all eight aggregate signs",
)

parts = tuple(
    w * e * test_f(t) for w, e, t in zip(weights, evens, nodes)
)
pairing = sum(parts)
coefficient_pairing = (
    Q(9, 2) * aggregate[2] + Q(11, 2) * aggregate[4] + aggregate[6]
)
need(pairing == coefficient_pairing, "raw-coordinate pairing identity")

def c_value(t, endpoint):
    return -even(t, endpoint) * (Q(9, 2) - t) / ((3 - t) * (5 - t))

def d_value(t):
    return (t - Q(1, 2)) * (t - Q(39, 40)) * (Q(7, 2) - t)

need(0 < c_value(nodes[2], 1) < Q(3, 5), "left local quotient bound")
need(c_value(nodes[3], -1) > Q(7, 10), "right local quotient bound")
need(d_value(nodes[2]) > Q(3, 100), "left derivative factor bound")
need(d_value(nodes[3]) < Q(4, 125), "right derivative factor bound")
need(parts[2] + parts[3] < -9375, "negative paired contribution")
need(parts[0] < 0, "first contribution sign")
need(0 < parts[1] < 1500, "second contribution bound")
need(0 < parts[4] < 1, "fifth contribution bound")
need(pairing < -7874, "negative actual-envelope R5 pairing")

for j, value in enumerate(aggregate):
    print("aggregate[" + str(j) + "]=" + str(value))
for i, value in enumerate(weights):
    print("weight[" + str(i + 1) + "]=" + str(value))
print("fixed_F_pairing=" + str(pairing))
print("finite_actual_R5_check=PASS")
print("scope=fixed boundary F only; not an eight-strict-negative SPR certificate")

