#!/usr/bin/env python3
"""Independent finite controls for the f207 abstract claims; no author code."""
from itertools import combinations
from functools import reduce
import json
import operator


def subspaces(n, d):
    # Unique row-reduced bases, low-index pivot first.
    for piv in combinations(range(n), d):
        free = [(i, j) for i, p in enumerate(piv)
                for j in range(p + 1, n) if j not in piv]
        for mask in range(1 << len(free)):
            rows = [1 << p for p in piv]
            for k, (i, j) in enumerate(free):
                if (mask >> k) & 1:
                    rows[i] |= 1 << j
            yield tuple(rows)


def span(basis):
    s = [0]
    for x in basis:
        s += [v ^ x for v in s]
    return tuple(s)


def parity(x):
    return x.bit_count() & 1


def qhyp(x):
    return (((x >> 0) & 1) & ((x >> 1) & 1)) ^ (((x >> 2) & 1) & ((x >> 3) & 1)) ^ (((x >> 4) & 1) & ((x >> 5) & 1))


def qell(x):
    return qhyp(x) ^ ((x >> 4) & 1) ^ ((x >> 5) & 1)


def q2(x):
    u, v = (x >> 6) & 1, (x >> 7) & 1
    return (u & v) ^ u ^ v


def q4(x):
    # radical low four; one hyperbolic and one anisotropic plane
    u, v, w, z = ((x >> i) & 1 for i in range(4, 8))
    return (u & v) ^ (w & z) ^ w ^ z


def swap8(x):
    return ((x & 0x55) << 1) | ((x & 0xAA) >> 1)


def quotient_mask(rows, points):
    mask = 0
    for x in points:
        label = sum(parity(r & x) << i for i, r in enumerate(rows))
        mask ^= 1 << label
    return mask


def required_mask(c):
    return sum(parity(c & y) << y for y in range(8))


def slope_rank6(rows):
    # L is the common kernel of three linear forms rows.  Its intersection
    # with the radical R=<1,2> is zero exactly when the restricted row map
    # on R has rank 2.  Only then the rank-four radical induces nonzero slope.
    kernel = [c for c in range(1, 8)
              if reduce(operator.xor, (rows[i] for i in range(3) if c & (1 << i)), 0) & 3 == 0]
    return kernel[0] if len(kernel) == 1 else 0


def slope_rank8(rows):
    # The polar complement of L is obtained by swapping each hyperbolic pair.
    # Its Gram matrix is 3x3 alternating.  Rank 0 gives restricted rank 2;
    # rank 2 has a unique nonzero kernel, the rank-4 radical slope.
    gram = [[parity(a & swap8(b)) for b in rows] for a in rows]
    if not any(map(any, gram)):
        return 0
    kernel = [c for c in range(1, 8)
              if all((sum(gram[i][j] * ((c >> j) & 1) for j in range(3)) & 1) == 0 for i in range(3))]
    assert len(kernel) == 1
    return kernel[0]


def accepts(mask, slope):
    expected = required_mask(slope)
    return mask in (expected, expected ^ 255)


def graph(a, b, r0, r1, u=0, v=0):
    result = set()
    for x in range(2):
        for y in range(2):
            offset = ((x * u) ^ (y * v) ^ (x * y)) * r1
            base = ((x * a) ^ (y * b)) << 2
            for t in range(2):
                result.add(base ^ offset ^ (t * r0))
    return frozenset(result)


def equations(q, plane):
    # Coefficients for all degree <=2 Boolean monomials on six coordinates.
    xs = [x for x in range(64) if q(x) == 0]
    pairs = list(combinations(range(6), 2))
    pivots = {}
    for i, x in enumerate(xs):
        bits = [1] + [(x >> j) & 1 for j in range(6)] + [((x >> j) & 1) & ((x >> k) & 1) for j, k in pairs]
        coeff = sum(bit << j for j, bit in enumerate(bits))
        row = coeff | ((x in plane) << 22)
        witness = 1 << i
        while row & ((1 << 22) - 1):
            p = (row & ((1 << 22) - 1)).bit_length() - 1
            if p not in pivots:
                pivots[p] = (row, witness)
                break
            old, ow = pivots[p]
            row ^= old
            witness ^= ow
        else:
            if (row >> 22) & 1:
                points = [xs[j] for j in range(len(xs)) if (witness >> j) & 1]
                # The returned equation subset has zero coefficient XOR and RHS 1.
                def lhs(y):
                    return sum(bit << j for j, bit in enumerate([1] + [(y >> k) & 1 for k in range(6)] + [((y >> k) & 1) & ((y >> l) & 1) for k, l in pairs]))
                assert reduce(operator.xor, map(lhs, points), 0) == 0
                assert sum(x in plane for x in points) % 2 == 1
                return False, points
    return True, []


def first_witness(rows, mask, slope):
    return {"annihilator_rows_hex": [hex(x) for x in rows], "actual_parity_mask_hex": hex(mask), "required_slope_bits": slope, "required_mask_hex": hex(required_mask(slope))}


def main():
    planes = {frozenset((0, a, b, a ^ b)) for a in range(1, 64) for b in range(a + 1, 64)}
    assert len(planes) == 651
    isotropic_h = [p for p in planes if all(qhyp(x) == 0 for x in p)]
    isotropic_e = [p for p in planes if all(qell(x) == 0 for x in p)]
    nondeg = [p for p in planes if parity((sorted(p)[1] & swap8(sorted(p)[2]))) == 1]
    assert (sum(qhyp(x) == 0 for x in range(64)), sum(qell(x) == 0 for x in range(64))) == (36, 28)
    assert (len(isotropic_h), len(isotropic_e), len(nondeg)) == (105, 45, 336)
    sets = set()
    totals = [0, 0, 0]
    for p in planes:
        a, b = sorted(p)[1:3]
        for r0 in (1, 2, 3):
            r1 = next(r for r in (1, 2, 3) if r != r0)
            for u in range(2):
                for v in range(2):
                    z = graph(a, b, r0, r1, u, v)
                    assert len(z) == 8 and 0 in z and reduce(operator.xor, z, 0) == 0
                    assert z not in sets
                    sets.add(z)
                    totals[0] += all(qhyp(x >> 2) == 0 for x in z)
                    totals[1] += all(qell(x >> 2) == 0 for x in z)
                    totals[2] += all((qhyp(x >> 2) ^ ((x >> 1) & 1)) == 0 for x in z)
    assert len(sets) == 7812 and totals == [1260, 540, 336]
    hyper_eq = [equations(qhyp, p) for p in isotropic_h]
    elliptic_eq = [equations(qell, p) for p in isotropic_e]
    assert all(not ok for ok, _ in hyper_eq) and all(ok for ok, _ in elliptic_eq)
    particular_p = frozenset((0, 1, 4, 5))
    ok, moment_witness = equations(qhyp, particular_p)
    assert not ok
    positive_h = graph(1, 4, 1, 2)
    positive_l = graph(1, 2, 1, 2)
    linear_r6 = frozenset(span((1, 4, 16)))
    wrong = set(positive_h)
    wrong.remove(1); wrong.add(2)
    wrong.remove(5); wrong.add(6)
    wrong = frozenset(wrong)
    assert len(wrong) == 8 and 0 in wrong and reduce(operator.xor, wrong, 0) == 0
    assert all(qhyp(x >> 2) == 0 for x in positive_h)
    assert all((qhyp(x >> 2) ^ ((x >> 1) & 1)) == 0 for x in positive_l)
    rank4_space = frozenset(span((1, 2, 4)))
    rank8_space = frozenset(span((1, 4, 16)))
    candidates = {"r6_isotropic_graph": positive_h, "r6_nondegenerate_graph": positive_l, "r6_linear_negative": linear_r6, "r6_two_pair_differences_negative": wrong, "r4_singular_flat": rank4_space, "r8_singular_flat_negative": rank8_space}
    failures = {k: 0 for k in candidates}
    witnesses = {}
    n = rank2_count = rank4_count = 0
    for rows in subspaces(8, 3):
        n += 1
        points = span(rows)
        rank2_count += all(q2(x) == 0 for x in points)
        rank4_count += all(q4(x) == 0 for x in points)
        for name, z in candidates.items():
            slope = 0 if name.startswith("r4_") else (slope_rank8(rows) if name.startswith("r8_") else slope_rank6(rows))
            mask = quotient_mask(rows, z)
            if not accepts(mask, slope):
                failures[name] += 1
                if name not in witnesses:
                    witnesses[name] = first_witness(rows, mask, slope)
    assert (n, rank2_count, rank4_count) == (97155, 1395, 715)
    assert failures["r6_isotropic_graph"] == failures["r6_nondegenerate_graph"] == failures["r4_singular_flat"] == 0
    assert failures["r6_linear_negative"] > 0 and failures["r6_two_pair_differences_negative"] > 0 and failures["r8_singular_flat_negative"] > 0
    syndrome = {}
    for kind, chars in (("independent", (0, 1, 2, 4)), ("dependent", (0, 1, 2, 3))):
        totals3 = set()
        for signs in range(16):
            count = 0
            for x in range(256):
                s = sum((-1 if (signs >> i) & 1 else 1) * (-1 if parity(c & x) else 1) for i, c in enumerate(chars))
                count += s % 3 == 0
            totals3.add(count)
        syndrome[kind] = sorted(totals3)
    assert syndrome == {"independent": [96], "dependent": [0, 192]}
    pair_counts = sorted({sum(((-1 if parity(x & 1) else 1) + sign * (-1 if parity(x & 2) else 1)) % 3 == 0 for x in range(256)) for sign in (-1, 1)})
    assert pair_counts == [128]
    print(json.dumps({"subspaces_5_exhausted_per_parity_case": n, "rank2_q_singular_3spaces": rank2_count, "rank4_q_singular_3spaces": rank4_count, "V_two_planes": len(planes), "V_singular_planes_hyperbolic_elliptic": [len(isotropic_h), len(isotropic_e)], "V_nondegenerate_planes": len(nondeg), "rank6_distinct_zero_sets": len(sets), "rank6_q_compatible_counts_hyperbolic_elliptic_nonzero_lambda": totals, "P_star_failures_by_abstract_case": failures, "P_star_first_negative_witnesses": witnesses, "hyperbolic_moment_inconsistent_planes": len(hyper_eq), "elliptic_moment_consistent_planes": len(elliptic_eq), "hyperbolic_moment_negative_certificate_plane_0_1_4_5": moment_witness, "mod3_four_term_cancellation_counts": syndrome, "mod3_two_term_cancellation_counts": pair_counts}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
