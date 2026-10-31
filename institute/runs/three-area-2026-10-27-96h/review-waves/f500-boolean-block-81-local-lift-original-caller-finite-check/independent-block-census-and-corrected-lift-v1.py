from itertools import product
from time import perf_counter

START = perf_counter()

class CheckError(Exception):
    pass

def need(condition, reason):
    if not condition:
        raise CheckError(reason)

def budget():
    if perf_counter() - START > 50:
        raise RuntimeError("COOPERATIVE_BUDGET_50S")

def chi(s, w):
    return 1 if (s & w).bit_count() % 2 == 0 else -1

def walsh(v):
    n = len(v)
    need(n > 0 and (n & (n - 1)) == 0, "POWER_OF_TWO")
    out = []
    for s in range(n):
        budget()
        out.append(sum(v[w] * chi(s, w) for w in range(n)))
    return tuple(out)

def shape(v):
    t = walsh(v)
    if abs(t[1]) == 3:
        need(sum(x != 0 for x in v) == 3, "ODD_SUPPORT")
        need(all(abs(t[s]) == 1 for s in (0, 2, 3)), "ODD_SHAPE")
        return "T"
    if t[1] != 0:
        return "OUT"
    nz = tuple(s for s in range(4) if t[s] != 0)
    if not nz:
        need(not any(v), "ZERO_INVERSE")
        return "O"
    if len(nz) == 1 and abs(t[nz[0]]) == 4:
        return "F" + str(nz[0])
    if len(nz) == 2 and all(abs(t[s]) == 2 for s in nz):
        for pair, label in (((0, 2), "A"), ((0, 3), "B"), ((2, 3), "C")):
            if nz == pair:
                return label
    raise CheckError("UNCLASSIFIED_U1_ZERO_BLOCK")

local = tuple(product((-1, 0, 1), repeat=4))
need(len(local) == 81 and len(set(local)) == 81, "LOCAL_UNIVERSE")
support_hist = tuple(sum(sum(x != 0 for x in v) == m for v in local) for m in range(5))
need(support_hist == (1, 8, 24, 32, 16), "SUPPORT_HISTOGRAM")
u1_hist = tuple(sum(walsh(v)[1] == k for v in local) for k in range(-4, 5))
need(u1_hist == (1, 4, 10, 16, 19, 16, 10, 4, 1), "U1_HISTOGRAM")
labels = ("T", "A", "B", "C", "F0", "F2", "F3", "O", "OUT")
shape_hist = tuple(sum(shape(v) == label for v in local) for label in labels)
need(shape_hist == (8, 4, 4, 4, 2, 2, 2, 1, 54), "SHAPE_HISTOGRAM")
for v in local:
    print("BLOCK", v, "WALSH", walsh(v), "SUPPORT", sum(x != 0 for x in v), "CLASS", shape(v))
print("SUPPORT_HISTOGRAM", support_hist)
print("U1_HISTOGRAM", u1_hist)
print("SHAPE_HISTOGRAM", tuple(zip(labels, shape_hist)))

integer_solutions = []
for aa in range(23):
    for bb in range(25):
        for p3 in range(25 - bb):
            budget()
            cc = 22 - aa
            oo = 24 - bb - p3
            if 100 + 2 * bb + 4 * p3 != 116:
                continue
            if 16 + 4 * (aa + bb) != 56:
                continue
            if 2 + aa + oo != 23:
                continue
            integer_solutions.append((aa, bb, cc, 2, p3, oo))
need(integer_solutions == [(4, 6, 18, 2, 1, 17)], "INTEGER_CENSUS")
print("INTEGER_SOLUTIONS", tuple(integer_solutions))

D = (1, 2, 4, 7)
a = [0] * 64
g = [0] * 64
for h, d in product(range(8), repeat=2):
    i = 8 * h + d
    if d == 0:
        g[i] = 4 if h < 2 else -2
    elif d in D:
        b = D.index(d)
        j = h // 2
        x, y = j & 1, (j >> 1) & 1
        p, t = b & 1, (b >> 1) & 1
        f = (x * p + y * t) & 1
        r = (x * y + p * t + x * p) & 1
        on_support = (h & 1) == f
        rho = 1 if p * t else -1
        a[i] = (-1 if r else 1) if on_support else 0
        g[i] = rho * (-2 + 3 * int(on_support))
a, g = tuple(a), tuple(g)
full2 = tuple(i for i in range(64) if abs(g[i]) == 4)
twos = tuple(i for i in range(64) if a[i] == 0 and abs(g[i]) == 2)
inactive = tuple(i for i in range(64) if a[i] == 0 and g[i] == 0)
need(sum(x != 0 for x in a) == 16, "GRAPH_SIZE")
need((len(full2), len(twos), len(inactive)) == (2, 22, 24), "GRAPH_PARTITION")

def make_array(A, B, F3):
    A, B, F3 = set(A), set(B), set(F3)
    need(A <= set(twos), "A_DOMAIN")
    need(B <= set(inactive) and F3 <= set(inactive), "INACTIVE_DOMAIN")
    need(not (B & F3), "INACTIVE_OVERLAP")
    rows = []
    for i in range(64):
        if a[i] != 0:
            hole = 0 if -g[i] * a[i] == 1 else 1
            row = tuple(0 if w == hole else a[i] * chi(1, w) for w in range(4))
        elif abs(g[i]) == 4:
            row = tuple((g[i] // 4) * chi(2, w) for w in range(4))
        elif abs(g[i]) == 2:
            sig = g[i] // 2
            if i in A:
                row = tuple(sig * (1 + chi(2, w)) // 2 for w in range(4))
            else:
                row = tuple(sig * (chi(2, w) + chi(3, w)) // 2 for w in range(4))
        elif i in B:
            row = tuple((1 + chi(3, w)) // 2 for w in range(4))
        elif i in F3:
            row = tuple(chi(3, w) for w in range(4))
        else:
            row = (0, 0, 0, 0)
        rows.append(row)
    return tuple(rows)

def check_array(rows, require_energy=True, require_zeros=True):
    need(len(rows) == 64, "BLOCK_COUNT")
    transforms = []
    for i, row in enumerate(rows):
        budget()
        need(len(row) == 4 and all(x in (-1, 0, 1) for x in row), "TERNARITY")
        u = walsh(row)
        need(not (u[1] == 0 and abs(u[0]) == 4), "H0_FORBIDDEN")
        need(u[1] == 3 * a[i], "U1_MISMATCH")
        need(u[2] == g[i], "U2_MISMATCH")
        transforms.append(u)
    mass = sum(x != 0 for row in rows for x in row)
    energy = sum(u[0] ** 2 for u in transforms)
    zeros = sum(u[3] == 0 for u in transforms)
    need(mass == 116, "SUPPORT_NOT_116")
    wa = walsh(tuple(u[1] // 3 for u in transforms))
    wg = walsh(tuple(u[2] for u in transforms))
    need(all(abs(x) == 4 for x in wa), "A_COMPLETE_SPECTRUM")
    for frequency, value in enumerate(wg):
        if frequency in (0, 1, 2, 4):
            need(value == 4, "G_NAMED_SMALL_SPECTRUM")
        else:
            need(abs(value) == 12, "G_COMPLETE_LARGE_SPECTRUM")
    if require_energy:
        need(energy == 56, "U0_ENERGY:" + str(energy))
    if require_zeros:
        need(zeros == 23, "U3_ZERO_COUNT:" + str(zeros))
    return mass, energy, zeros

good_A = tuple(8 * h for h in (2, 3, 4, 5))
good_B = tuple(8 * h + 3 for h in range(6))
good_F3 = (8 * 6 + 3,)
good = make_array(good_A, good_B, good_F3)
need(check_array(good) == (116, 56, 23), "CORRECTED_SUMMARY")
census_labels = ("A", "B", "C", "F2", "F3", "O")
physical_census = tuple(sum(shape(row) == label for row in good) for label in census_labels)
need(physical_census == (4, 6, 18, 2, 1, 17), "PHYSICAL_CENSUS")
flat_good = tuple(x for row in good for x in row)
need(len(flat_good) == 256, "ARRAY_LENGTH")
need(sum(flat_good) == -4, "DISPLAYED_BALANCE_DIAGNOSTIC")
print("CORRECTED_SUMMARY", check_array(good))
print("CORRECTED_PHYSICAL_CENSUS", physical_census)
print("CORRECTED_ARRAY_256", flat_good)
print("DISPLAYED_COORDINATE_SUM", sum(flat_good))

def recipe(k):
    need(0 <= k <= 22, "K_RANGE")
    return make_array(twos[:k], inactive[:8], ())

energy_only, zeros_only, joint = [], [], []
for k in range(23):
    summary = check_array(recipe(k), False, False)
    need(summary == (116, 48 + 4 * k, 18 + k), "RECIPE_FORMULA")
    if summary[1] == 56:
        energy_only.append(k)
    if summary[2] == 23:
        zeros_only.append(k)
    if summary[1:] == (56, 23):
        joint.append(k)
    print("RECIPE", k, summary)
need(energy_only == [2] and zeros_only == [5] and joint == [], "RECIPE_EXHAUSTION")
need(check_array(recipe(2), True, False) == (116, 56, 20), "ENERGY_ONLY_POSITIVE")
need(check_array(recipe(5), False, True) == (116, 68, 23), "ZEROS_ONLY_POSITIVE")
print("ENERGY_ONLY_K", tuple(energy_only))
print("ZEROS_ONLY_K", tuple(zeros_only))
print("JOINT_K", tuple(joint))

def expect_failure(label, action, reason):
    try:
        action()
    except CheckError as error:
        need(str(error) == reason, "CONTROL_WRONG_REASON:" + label + ":" + str(error))
        print("CONTROL_REJECTED", label, reason)
    else:
        raise CheckError("CONTROL_UNEXPECTED_PASS:" + label)

expect_failure("energy_only_fails_zeros", lambda: check_array(recipe(2)), "U3_ZERO_COUNT:20")
expect_failure("zeros_only_fails_energy", lambda: check_array(recipe(5)), "U0_ENERGY:68")
bad_h = list(good)
empty_index = next(i for i, row in enumerate(good) if shape(row) == "O")
bad_h[empty_index] = (1, 1, 1, 1)
expect_failure("forbidden_U0_peak", lambda: check_array(tuple(bad_h)), "H0_FORBIDDEN")
bad_u1 = list(good)
full_index = full2[0]
bad_u1[full_index] = (0,) + bad_u1[full_index][1:]
expect_failure("damaged_full_U2_block", lambda: check_array(tuple(bad_u1)), "U1_MISMATCH")
budget()
print("CHECKER_STATUS: PASS")
print("ELAPSED_SECONDS", perf_counter() - START)
