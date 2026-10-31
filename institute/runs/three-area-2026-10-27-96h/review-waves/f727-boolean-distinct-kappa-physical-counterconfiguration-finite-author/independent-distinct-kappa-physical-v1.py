#!/usr/bin/env python3
"""UNRUN prospective finite source; parent full static read and separate GO required.

Scope: the single explicitly sheared f718 X and its one prescribed Y. This
program reconstructs their common four-fibre inverse for all 64 character
transports, with a direct Walsh sum and an independent butterfly transform.
It does not search all y, infer a global no-go, verify the definition of
H_local, restore V or the original caller, or establish novelty. Parent must
separately pin this source and its chosen interpreter, perform a complete
static read, and record a one-shot GO. Suggested supervision: cooperative
monotonic deadline 45 s, external hard limit at most 55 s. The source performs
no file, network, subprocess, or deletion operation; stdout is the only
result stream. A COMPLETE record is emitted only after all checks and controls.

Scientific input: the complete frozen f727 packet, including the unadopted
f718 and f717 texts (S1 and S3), the conditional S4/S5 dispositions, S6
erratum, and the S7 failed and S8 corrected historical run receipts. It does
not read any of those files at runtime. Packet SHA256:
ab1dde98809fd53370935e3e2188de5e83e3432d9ed50624aff68d83b8e3cde9.
Manifest SHA256:
a97fe5e514b2dec4672a535870827d0f3199b77aadf76e749b1d84b329834839.

Coordinates are c=(ell,h,j,b) with 2-bit j,b and encoding
(ell<<5)|(h<<4)|(j<<2)|b; p=1,q=2,r=3. Frequency and transport
indices use the same binary encoding and the usual bitwise dot product.
For w=0,1,2,3, chi_1=(-1)^w0, chi_2=(-1)^w1 and
chi_3=(-1)^(w0+w1). In particular no transformation of the fixed a or g
is applied when X and Y are both transported.
"""

import json
import sys
import time

START = time.monotonic()
DEADLINE = START + 45.0
P, Q, R = 1, 2, 3
KINDS = ("GRAPH", "F", "D0", "GRAPH_D3", "E_D3", "Z2", "Z4", "Z0")
TYPE_COUNTS = {"GRAPH": 16, "F": 2, "D0": 4, "GRAPH_D3": 12,
               "E_D3": 6, "Z2": 6, "Z4": 1, "Z0": 17}
LOCAL_SUPPORT = {"GRAPH": 3, "F": 4, "D0": 2, "GRAPH_D3": 2,
                 "E_D3": 2, "Z2": 2, "Z4": 4, "Z0": 0}
T0_CENSUS = {"GRAPH": 12, "F": 2, "D0": 3, "GRAPH_D3": 9,
             "E_D3": 1, "Z2": 3, "Z4": 1, "Z0": 0}
# Keys in these two independent literal tables are (j,h,b).
REFERENCE_Z2 = {(P, 1, Q): 2, (P, 1, R): -2,
                (Q, 1, P): -2, (Q, 1, R): 2,
                (R, 0, P): 2, (R, 0, Q): -2}
SHEARED_Z2 = {(P, 1, Q): -2, (P, 1, R): 2,
              (Q, 1, P): 2, (Q, 1, R): -2,
              (R, 0, P): -2, (R, 0, Q): 2}


class Failure(Exception):
    def __init__(self, reason, detail=""):
        super().__init__(reason + (": " + str(detail) if detail else ""))
        self.reason = reason
        self.detail = str(detail)


class Deadline(Exception):
    pass


def check(condition, reason, detail=""):
    if not condition:
        raise Failure(reason, detail)


def tick():
    if time.monotonic() >= DEADLINE:
        raise Deadline()


def emit(record):
    print(json.dumps(record, sort_keys=True, separators=(",", ":")), flush=True)


def coord(ell, h, j, b):
    return (ell << 5) | (h << 4) | (j << 2) | b


def unpack(c):
    return ((c >> 5) & 1, (c >> 4) & 1, (c >> 2) & 3, c & 3)


def sign(v, w):
    return -1 if (v & w).bit_count() % 2 else 1


def f(j):
    return (j & 1) * ((j >> 1) & 1)


def rho(b):
    return -1 if b != R else 1


def kind(c):
    ell, h, j, b = unpack(c)
    if ell:
        if h == f(j):
            return "GRAPH"
        return "D0" if b == j else "GRAPH_D3"
    if b == 0:
        return "F" if j == 0 else "E_D3"
    if (j, h, b) in SHEARED_Z2:
        return "Z2"
    if (h, j, b) == (0, 0, P):
        return "Z4"
    return "Z0"


def direct(values):
    n = len(values)
    check(n > 0 and n & (n - 1) == 0, "WALSH_LENGTH")
    out = []
    for frequency in range(n):
        tick()
        out.append(sum(value * sign(frequency, c)
                       for c, value in enumerate(values)))
    return out


def butterfly(values):
    n = len(values)
    check(n > 0 and n & (n - 1) == 0, "WALSH_LENGTH")
    out = list(values)
    stride = 1
    while stride < n:
        tick()
        for start in range(0, n, 2 * stride):
            for offset in range(stride):
                i, j = start + offset, start + offset + stride
                left, right = out[i], out[j]
                out[i], out[j] = left + right, left - right
        stride *= 2
    return out


def check_transform_agreement(d, b):
    check(d == b, "WALSH_DIRECT_BUTTERFLY")


def spectrum(values):
    d = direct(values)
    check_transform_agreement(d, butterfly(values))
    check(sum(v * v for v in d) == len(values) * sum(v * v for v in values),
          "WALSH_PARSEVAL")
    return d


def geometry():
    # z=(j,b): the f-polar radical must be exactly the b-plane.
    fz = [f(z >> 2) for z in range(16)]
    radical = [d for d in range(16)
               if all((fz[z ^ d] ^ fz[z] ^ fz[d] ^ fz[0]) == 0
                      for z in range(16))]
    check(radical == [0, 1, 2, 3], "F_POLAR_RADICAL", radical)
    fq, phase, phase_f = [], [], []
    for z in range(16):
        j, b = z >> 2, z & 3
        r = 0 if sign(j, b) == 1 else 1
        qb = 1 ^ ((b & 1) * ((b >> 1) & 1))
        fq.append(1 if (f(j) ^ qb) == 0 else -1)
        phase.append(1 if r == 0 else -1)
        phase_f.append(1 if (r ^ f(j)) == 0 else -1)
    for name, values in (("F_PLUS_Q", fq), ("R", phase), ("R_PLUS_F", phase_f)):
        check(all(abs(v) == 4 for v in spectrum(values)), "BENT_" + name)


def reference_x():
    out = [0] * 64
    for c in range(64):
        ell, h, j, b = unpack(c)
        if ell and h == f(j):
            out[c] = 2 * (b == j) - 1
        elif ell and h != f(j) and b == 0:
            out[c] = 2
        elif not ell:
            out[c] = REFERENCE_Z2.get((j, h, b), 0)
    return out


def shear(c):
    ell, h, j, b = unpack(c)
    return coord(ell, h, j, b ^ j)


def sheared_x():
    original = reference_x()
    check(len({shear(c) for c in range(64)}) == 64, "SHEAR_BIJECTION")
    check(all(shear(shear(c)) == c for c in range(64)), "SHEAR_INVOLUTION")
    x = [original[shear(c)] for c in range(64)]
    # Independent pointwise formula plus the literal sheared Z2 table.
    literal = []
    for c in range(64):
        ell, h, j, b = unpack(c)
        if ell and h == f(j):
            value = 2 * (b == 0) - 1
        elif ell and h != f(j) and b == j:
            value = 2
        elif not ell:
            value = SHEARED_Z2.get((j, h, b), 0)
        else:
            value = 0
        literal.append(value)
    check(x == literal, "SHEARED_X_LITERAL")
    return x


def fixed_ag():
    a, g = [0] * 64, [0] * 64
    for c in range(64):
        ell, h, j, b = unpack(c)
        if ell and h == f(j):
            a[c], g[c] = sign(j, b), rho(b)
        elif ell:
            g[c] = -2 * rho(b)
        elif b == 0:
            g[c] = 4 if j == 0 else -2
    return a, g


def prescribed_y(kinds):
    y = [0] * 64
    for c in range(64):
        ell, h, j, b = unpack(c)
        k = kinds[c]
        if k == "GRAPH":
            y[c] = sign(j ^ R, b)
        elif k in ("GRAPH_D3", "E_D3", "Z2"):
            y[c] = -2 if c == coord(0, 0, P, 0) else 2
        elif k == "Z4":
            y[c] = 4
    return y


def check_anchors(x):
    anchors = []
    for j in range(4):
        sites = [b for b in range(4) if x[coord(1, 1 ^ f(j), j, b)] != 0]
        check(len(sites) == 1, "D0_ROW_CARDINALITY", (j, sites))
        check(abs(x[coord(1, 1 ^ f(j), j, sites[0])]) == 2,
              "D0_ANCHOR_MAGNITUDE", j)
        anchors.append(sites[0])
    check(len(set(anchors)) == 4, "D0_ANCHORS_DISTINCT", anchors)
    check(anchors == [0, P, Q, R], "D0_ANCHOR_LOCATION", anchors)
    return anchors


def check_graph_relation(x, y, a, g):
    for j in range(4):
        for b in range(4):
            c = coord(1, f(j), j, b)
            check(abs(x[c]) == 1 and abs(a[c]) == 1 and abs(g[c]) == 1,
                  "GRAPH_MAGNITUDES", (j, b))
            check(y[c] == -a[c] * g[c] * x[c],
                  "GRAPH_PHYSICAL_RELATION", (j, b))


def graph_rows(y, aligned=False):
    return [[y[coord(1, f(j), j, b ^ (j if aligned else 0))]
             for b in range(4)] for j in range(4)]


def check_character_rows(rows, expected):
    check(len(rows) == 4 and all(len(row) == 4 for row in rows),
          "CHARACTER_ROW_SHAPE")
    kappas, sigmas = [], []
    for j, row in enumerate(rows):
        check(all(v in (-1, 1) for v in row), "CHARACTER_SIGNS", j)
        sigma = row[0]
        k = (int(row[P] != sigma) | (int(row[Q] != sigma) << 1))
        check(all(row[b] == sigma * sign(k, b) for b in range(4)),
              "CHARACTER_AFFINE", j)
        kappas.append(k)
        sigmas.append(sigma)
    check(len(set(kappas)) == 4, "CHARACTER_DISTINCT", kappas)
    check(kappas == expected, "CHARACTER_KAPPA_FORMULA", kappas)
    return kappas, sigmas


def inverse(x, a, g, y):
    u = []
    for c in range(64):
        tick()
        row = []
        for w in range(4):
            numerator = (x[c] + 3 * a[c] * sign(1, w)
                         + g[c] * sign(2, w) + y[c] * sign(3, w))
            check(numerator % 4 == 0, "INVERSE_NONINTEGRAL", (c, w, numerator))
            value = numerator // 4
            check(value in (-1, 0, 1), "INVERSE_NONTERNARY", (c, w, value))
            row.append(value)
        u.append(row)
    return u


def check_roundtrip(u, x, a, g, y):
    for c in range(64):
        row = u[c]
        check(sum(row) == x[c], "INVERSE_COMPONENT_X", c)
        check(sum(sign(1, w) * row[w] for w in range(4)) == 3 * a[c],
              "INVERSE_COMPONENT_3A", c)
        check(sum(sign(2, w) * row[w] for w in range(4)) == g[c],
              "INVERSE_COMPONENT_G", c)
        check(sum(sign(3, w) * row[w] for w in range(4)) == y[c],
              "INVERSE_COMPONENT_Y", c)


def check_energy(values, expected, label):
    energy = sum(v * v for v in values)
    check(energy == expected, label, energy)


def check_spatial(x, y):
    check_energy(x, 56, "X_ENERGY")
    check_energy(y, 128, "Y_ENERGY")
    check(sum(v != 0 for v in x) == 26, "X_SPATIAL_SUPPORT")
    check(sum(v != 0 for v in y) == 41, "Y_SPATIAL_SUPPORT")
    check(sum(v == 0 for v in y) == 23, "Y_SPATIAL_ZEROS")


def xor_all(values):
    result = 0
    for value in values:
        result ^= value
    return result


def check_x_physical_divisibility(x, kinds):
    negative_graph = [c for c in range(64) if kinds[c] == "GRAPH" and x[c] < 0]
    weighted = [c for c in range(64) if kinds[c] in ("D0", "Z2")]
    check(len(weighted) == 10 and all(abs(x[c]) == 2 for c in weighted),
          "X_WEIGHTED_SITES")
    negative_weighted = [c for c in weighted if x[c] < 0]
    check(len(negative_graph) % 2 == 0, "GRAPH_NEGATIVE_PARITY")
    check((len(negative_graph) // 2 + len(negative_weighted)) % 2 == 1,
          "X_QUARTER_PARITY")
    check(xor_all(negative_graph) == xor_all(weighted), "X_PHYSICAL_XOR")


def check_x_spectrum(xhat, t):
    check(len(xhat) == 64, "X_SPECTRUM_LENGTH")
    check(all(v % 8 == 0 for v in xhat), "X_DIVISIBILITY")
    check(all(abs(v) <= 8 for v in xhat), "X_U0_CAP")
    check(xhat[t] == 0, "X_CARRIED_ZERO", (t, xhat[t]))
    check(sum(v == 0 for v in xhat) == 8, "X_EIGHT_ZEROS")
    check(all(v in (-8, 0, 8) for v in xhat), "X_SPECTRUM_VALUES")


def check_y_spectrum(yhat, t):
    check(len(yhat) == 64, "Y_SPECTRUM_LENGTH")
    check(all(v % 8 == 4 for v in yhat), "Y_RESIDUE")
    check(yhat[t] == 52, "Y_CARRIED_52", (t, yhat[t]))
    check(abs(yhat[t]) > 12, "Y_U3_FAILURE")


def check_u3_caps(yhat):
    check(all(abs(v) <= 12 for v in yhat), "U3_CAP")


def check_translation(actual, base, t, label):
    check(all(actual[k] == base[k ^ t] for k in range(64)), label, t)


def check_total_support(u):
    support = sum(value != 0 for row in u for value in row)
    check(support == 116, "U_SUPPORT", support)
    return support


def check_local_support(u, kinds):
    for c, row in enumerate(u):
        check(sum(value != 0 for value in row) == LOCAL_SUPPORT[kinds[c]],
              "U_LOCAL_SUPPORT", (c, kinds[c]))


def w0_census(u, kinds):
    counts = {k: 0 for k in KINDS}
    by_b = [0] * 4
    for c in range(64):
        if u[c][0] != 0:
            counts[kinds[c]] += 1
            if kinds[c] == "GRAPH":
                by_b[unpack(c)[3]] += 1
    return counts, by_b


def predicted_census(t, x0, y0, a, g, kinds):
    # These are pointwise physical identities, not a second call to inverse().
    counts = {k: 0 for k in KINDS}
    for c, k in enumerate(kinds):
        phase = sign(t, c)
        if k == "GRAPH":
            live = a[c] * g[c] == 1 or phase * x0[c] == a[c]
        elif k == "F" or k == "Z4":
            live = True
        elif k == "D0":
            live = phase * x0[c] + g[c] != 0
        elif k in ("GRAPH_D3", "E_D3"):
            live = g[c] + phase * y0[c] != 0
        elif k == "Z2":
            live = x0[c] + y0[c] != 0
        else:
            live = False
        counts[k] += int(live)
    return counts


def check_census(actual, expected):
    for k in KINDS:
        check(actual[k] == expected[k], "CENSUS_" + k,
              (actual[k], expected[k]))


def check_j(u):
    j = sum(row[0] != 0 for row in u) % 2
    check(j == 1, "J_PARITY", j)
    return j


def check_w0_fourier(u, xhat, ahat, ghat, yhat, j):
    w0hat = spectrum([row[0] for row in u])
    for k in range(64):
        check(4 * w0hat[k] == xhat[k] + 3 * ahat[k] + ghat[k] + yhat[k],
              "W0_FOURIER_IDENTITY", k)
        check((4 * w0hat[k] - 4 * j) % 8 == 0, "W0_J_RESIDUE", k)
        check((yhat[k] - 4 * j) % 8 == 0, "Y_J_RESIDUE", k)


def expect_failure(controls, name, reason, fn):
    tick()
    try:
        fn()
    except Failure as exc:
        check(exc.reason == reason, "CONTROL_WRONG_REASON",
              (name, reason, exc.reason, exc.detail))
        controls.append({"control": name, "expected_reason": reason})
        return
    raise Failure("CONTROL_MISSED", (name, reason))


def negative_controls(x, y, a, g, kinds, xhat, yhat, u):
    controls = []
    altered = butterfly(x)
    altered[0] += 8
    expect_failure(controls, "butterfly-value", "WALSH_DIRECT_BUTTERFLY",
                   lambda: check_transform_agreement(xhat, altered))

    bad_y = y[:]
    bad_y[coord(1, f(0), 0, 0)] *= -1
    expect_failure(controls, "forced-graph-value", "GRAPH_PHYSICAL_RELATION",
                   lambda: check_graph_relation(x, bad_y, a, g))

    rows = graph_rows(y)
    duplicate = [row[:] for row in rows]
    duplicate[0] = duplicate[1][:]
    expected_k = [j ^ R for j in range(4)]
    expect_failure(controls, "repeated-kappa", "CHARACTER_DISTINCT",
                   lambda: check_character_rows(duplicate, expected_k))
    noncharacter = [row[:] for row in rows]
    noncharacter[0][R] *= -1
    expect_failure(controls, "noncharacter-row", "CHARACTER_AFFINE",
                   lambda: check_character_rows(noncharacter, expected_k))

    bad_x = x[:]
    bad_x[coord(1, 1 ^ f(P), P, P)] = 0
    bad_x[coord(1, 1 ^ f(P), P, 0)] = 2
    expect_failure(controls, "duplicate-anchor", "D0_ANCHORS_DISTINCT",
                   lambda: check_anchors(bad_x))

    bad_y = y[:]
    bad_y[coord(1, f(0), 0, 0)] += 1
    expect_failure(controls, "fractional-inverse", "INVERSE_NONINTEGRAL",
                   lambda: inverse(x, a, g, bad_y))
    bad_y = y[:]
    bad_y[coord(0, 0, 0, 0)] = 4
    expect_failure(controls, "nonternary-inverse", "INVERSE_NONTERNARY",
                   lambda: inverse(x, a, g, bad_y))

    bad_u = [row[:] for row in u]
    bad_u[coord(0, 0, 0, 0)][0] = 0
    expect_failure(controls, "four-fibre-roundtrip", "INVERSE_COMPONENT_X",
                   lambda: check_roundtrip(bad_u, x, a, g, y))
    expect_failure(controls, "wrong-116-support", "U_SUPPORT",
                   lambda: check_total_support(bad_u))
    expect_failure(controls, "wrong-F-census", "CENSUS_F",
                   lambda: check_census(w0_census(bad_u, kinds)[0], T0_CENSUS))
    expect_failure(controls, "even-J", "J_PARITY", lambda: check_j(bad_u))

    bad_x = x[:]
    bad_x[coord(0, 0, 0, 0)] = 2
    expect_failure(controls, "wrong-x-energy", "X_ENERGY",
                   lambda: check_energy(bad_x, 56, "X_ENERGY"))
    bad_y = y[:]
    bad_y[coord(0, 0, 0, Q)] = 2
    expect_failure(controls, "wrong-y-energy", "Y_ENERGY",
                   lambda: check_energy(bad_y, 128, "Y_ENERGY"))
    bad_x = x[:]
    bad_x[coord(1, f(0), 0, 0)] = -1
    expect_failure(controls, "odd-negative-graph-count", "GRAPH_NEGATIVE_PARITY",
                   lambda: check_x_physical_divisibility(bad_x, kinds))

    bad_xhat = xhat[:]
    bad_xhat[0] = 1
    expect_failure(controls, "u0-divisibility", "X_DIVISIBILITY",
                   lambda: check_x_spectrum(bad_xhat, 0))
    bad_xhat = xhat[:]
    bad_xhat[0] = 16
    expect_failure(controls, "u0-cap", "X_U0_CAP",
                   lambda: check_x_spectrum(bad_xhat, 0))
    bad_xhat = xhat[:]
    bad_xhat[0] = 8
    expect_failure(controls, "carried-x-zero", "X_CARRIED_ZERO",
                   lambda: check_x_spectrum(bad_xhat, 0))
    bad_xhat = xhat[:]
    bad_xhat[0] += 8
    expect_failure(controls, "wrong-x-transport", "X_TRANSPORT",
                   lambda: check_translation(bad_xhat, xhat, 0, "X_TRANSPORT"))

    bad_yhat = yhat[:]
    bad_yhat[0] += 1
    expect_failure(controls, "y-residue", "Y_RESIDUE",
                   lambda: check_y_spectrum(bad_yhat, 0))
    bad_yhat = yhat[:]
    bad_yhat[0] = 12
    expect_failure(controls, "wrong-carried-52", "Y_CARRIED_52",
                   lambda: check_y_spectrum(bad_yhat, 0))
    # A synthetic all-zero spectrum merely checks the cap predicate is not
    # vacuous. The actual prescribed y is required to trigger its cap failure.
    check_u3_caps([0] * 64)
    expect_failure(controls, "actual-one-y-u3-violation", "U3_CAP",
                   lambda: check_u3_caps(yhat))
    return controls


def main():
    tick()
    check(len(sys.argv) == 1, "UNEXPECTED_ARGUMENT")
    emit({"event": "START", "scope": "one f718 shear and one prescribed y",
          "cooperative_seconds": 45, "external_max_seconds": 55,
          "H_local_definition": "NOTTESTED", "V": "NOTTESTED",
          "original_caller": "NOTTESTED", "all_y_search": "NOTRUN"})
    geometry()
    kinds = [kind(c) for c in range(64)]
    check({k: kinds.count(k) for k in KINDS} == TYPE_COUNTS, "TYPE_COUNTS")
    x0, a, g = sheared_x(), *fixed_ag()
    y0 = prescribed_y(kinds)
    check_spatial(x0, y0)
    check_anchors(x0)
    check_graph_relation(x0, y0, a, g)
    check_x_physical_divisibility(x0, kinds)
    ahat, ghat = spectrum(a), spectrum(g)
    check(all(abs(v) == 4 for v in ahat), "A_BENT_SPECTRUM")
    check(all(v % 8 == 4 for v in ghat), "G_RESIDUE")
    check(all((3 * ahat[k] + ghat[k]) % 8 == 0 for k in range(64)),
          "AG_COMBINED_RESIDUE")
    base_xhat, base_yhat = spectrum(x0), spectrum(y0)
    check_x_spectrum(base_xhat, 0)
    check_y_spectrum(base_yhat, 0)

    u0 = None
    for t in range(64):
        tick()
        x = [sign(t, c) * x0[c] for c in range(64)]
        y = [sign(t, c) * y0[c] for c in range(64)]
        check_spatial(x, y)
        anchors = check_anchors(x)
        check_graph_relation(x, y, a, g)
        check_x_physical_divisibility(x, kinds)
        expected_k = [j ^ R ^ (t & 3) for j in range(4)]
        kappas, sigmas = check_character_rows(graph_rows(y), expected_k)
        aligned_kappas, aligned_sigmas = check_character_rows(graph_rows(y, True), expected_k)
        check(sigmas == [sign(t, coord(1, f(j), j, 0)) for j in range(4)],
              "GRAPH_TRANSPORT_SIGMAS")
        xhat, yhat = spectrum(x), spectrum(y)
        check_translation(xhat, base_xhat, t, "X_TRANSPORT")
        check_translation(yhat, base_yhat, t, "Y_TRANSPORT")
        check_x_spectrum(xhat, t)
        check_y_spectrum(yhat, t)
        u = inverse(x, a, g, y)
        check_roundtrip(u, x, a, g, y)
        support = check_total_support(u)
        check_local_support(u, kinds)
        actual_census, graph_by_b = w0_census(u, kinds)
        check_census(actual_census, predicted_census(t, x0, y0, a, g, kinds))
        if t == 0:
            check_census(actual_census, T0_CENSUS)
            check(graph_by_b == [4, 2, 2, 4], "CENSUS_GRAPH_BY_B", graph_by_b)
            check(sum(actual_census.values()) == 31, "CENSUS_T0_TOTAL")
            u0 = u
        j_value = check_j(u)
        check_w0_fourier(u, xhat, ahat, ghat, yhat, j_value)
        emit({"event": "TRANSPORT", "t": t, "anchors_b": anchors,
              "kappas": kappas, "graph_sigmas": sigmas,
              "aligned_kappas": aligned_kappas, "aligned_sigmas": aligned_sigmas,
              "xhat": xhat, "yhat": yhat, "x_energy": 56, "y_energy": 128,
              "u_support": support, "w0_census": actual_census,
              "w0_graph_by_b": graph_by_b, "J": j_value,
              "yhat_at_t": yhat[t],
              "u3_cap_violations": sum(abs(v) > 12 for v in yhat)})

    check(u0 is not None, "MISSING_T0")
    controls = negative_controls(x0, y0, a, g, kinds, base_xhat, base_yhat, u0)
    tick()
    emit({"event": "COMPLETE", "result": "PASS_ONE_PHYSICAL_COUNTERCONFIGURATION_ONLY",
          "transports": 64, "x_walsh_per_transport": 64,
          "y_walsh_per_transport": 64, "four_fibre_entries_per_transport": 256,
          "controls": controls, "H_local_definition": "NOTTESTED",
          "V": "NOTTESTED", "original_caller": "NOTTESTED",
          "all_y_search": "NOTRUN", "global_claim": "NONE",
          "elapsed_seconds": time.monotonic() - START})


if __name__ == "__main__":
    try:
        main()
    except Deadline:
        emit({"event": "INCOMPLETE_COOPERATIVE_DEADLINE", "seconds": 45})
        sys.exit(2)
    except Failure as exc:
        emit({"event": "FAIL", "reason": exc.reason, "detail": exc.detail})
        sys.exit(1)
