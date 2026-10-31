#!/usr/bin/env python3
"""Independent, bounded exact controls; no author code is imported."""
import itertools
import json
import math
import sys


class Rejected(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Rejected(reason)


def negative(reason, function, *args):
    try:
        function(*args)
    except Rejected as exc:
        require(str(exc) == reason, 'NEGATIVE_WRONG_REASON:' + str(exc))
        return reason
    raise Rejected('NEGATIVE_UNEXPECTED_ACCEPTANCE:' + reason)


def tiling(A, B, n):
    return len(A) * len(B) == n and len({(a + b) % n for a in A for b in B}) == n


def divisor_set(A, n):
    return {math.gcd(a - b, n) for a in A for b in A}


def require_divisor_exclusion(A, B, n):
    require(len(A) * len(B) == n, 'SANDS_BAD_CARDINALITY')
    require(divisor_set(A, n).intersection(divisor_set(B, n)) == {n},
            'SANDS_COMMON_NONTRIVIAL_DIVISOR')


def require_unique_sums(A, B, n):
    seen = set()
    for a in A:
        for b in B:
            r = (a + b) % n
            require(r not in seen, 'BORDER_DUPLICATE_SUM')
            seen.add(r)
    require(len(seen) == n, 'BORDER_MISSING_SUM')


def border(atoms, n):
    P, Q = set(), set()
    for s in atoms:
        i = len(s) - len(s.lstrip('a'))
        if i < len(s) and set(s[i:]) == {'b'}:
            P.add(i % n)
        j = len(s) - len(s.rstrip('a'))
        if j < len(s) and set(s[:len(s)-j]) == {'b'}:
            Q.add(j % n)
    return P, Q


def divisors(n):
    result = set()
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            result.add(d)
            result.add(n // d)
    return sorted(result)


def transport(y, R, h):
    g0 = math.gcd(y, R)
    require(R % h == 0, 'TRANSPORT_H_NOT_DIVISOR_R')
    require(h % g0 == 0, 'TRANSPORT_H_NOT_MULTIPLE_G0')
    return math.gcd((h // g0) * y, R)


def collision(y, x, rho, R, K):
    require(y % 2 == 1 and x % 2 == 1, 'P5_DIFFERENCE_NOT_ODD')
    require(y % rho == 0, 'P5_RHO_NOT_DIVIDING_Y')
    g0 = math.gcd(y, R)
    require(x % g0 == 0, 'P5_X_NOT_MULTIPLE_G0')
    h = math.gcd(x, R)
    t = h // g0
    n = (1 << K) * rho * R
    lhs, rhs = math.gcd(t * y, n), math.gcd(rho * x, n)
    require(lhs == rho * h == rhs, 'P5_COLLISION_EQUALITY')
    return {'g0': g0, 'h': h, 't': t, 'n': n, 'gcd': lhs}


def require_coprime(t, size):
    require(math.gcd(t, size) == 1, 'DILATION_NONCOPRIME')


def require_separation(R, E, g):
    colours = {}
    for u in range(R):
        colour = u in E
        r = u % g
        if r in colours:
            require(colours[r] == colour, 'SEPARATION_MIXED_RESIDUE_CLASS')
        colours[r] = colour


def require_crt(a, b):
    require(math.gcd(a, b) == 1, 'CRT_NONCOPRIME_FULL_POWER')


def graph_components(R, E, moduli):
    parent = list(range(R))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def join(x, y):
        x, y = root(x), root(y)
        if x != y:
            parent[y] = x
    for m in moduli:
        require(R % m == 0, 'GRAPH_BAD_MODULUS')
        buckets = [[] for _ in range(m)]
        for u in range(R):
            buckets[u % m].append(u)
        for group in buckets:
            left = next((u for u in group if u in E), None)
            right = next((u for u in group if u not in E), None)
            if left is not None and right is not None:
                for u in group:
                    join(u, right if u in E else left)
    return len({root(u) for u in range(R)})


def require_connected(R, E, moduli):
    require(graph_components(R, E, moduli) == 1, 'GRAPH_DISCONNECTED')


def tail_equality(y, x, p, R, K, rho):
    require(x % 2 == 1, 'TAIL_X_EVEN')
    w = math.gcd(y, R)
    require(x % w == 0, 'TAIL_X_NOT_MULTIPLE_W')
    require(x % p != 0, 'TAIL_X_DIVISIBLE_P')
    h = math.gcd(x, R)
    t = h // w
    n = (1 << K) * rho * R
    lhs, rhs = math.gcd(t * y, n), math.gcd(x, n)
    require(lhs == h == rhs, 'TAIL_COLLISION_EQUALITY')
    return {'w': w, 'h': h, 't': t, 'n': n, 'gcd': lhs}


def parity_case(rho, R, K, a):
    b = K - a
    n = (1 << K) * rho * R
    block = rho * (1 << a)
    P = set(range(block))
    Q = {block * j for j in range(R * (1 << b))}
    require(tiling(P, Q, n), 'PARITY_SOURCE_NOT_TILING')
    RP = {(R * v) % n for v in P}
    rhoQ = {(rho * q) % n for q in Q}
    require(len(RP) == len(P) and tiling(RP, Q, n), 'RP_DILATION_FAILED')
    require(len(rhoQ) == len(Q) and tiling(P, rhoQ, n), 'RHOQ_DILATION_FAILED')
    qfib, pfib = [[] for _ in range(R)], [[] for _ in range(rho)]
    for q in Q:
        qfib[q % R].append(q)
    for v in P:
        pfib[v % rho].append(v)
    require(all(len(z) == (1 << b) for z in qfib), 'Q_FIBRE_CARDINALITY')
    require(all(len(z) == (1 << a) for z in pfib), 'P_FIBRE_CARDINALITY')
    mq = [len({z % 2 for z in fibre}) == 2 for fibre in qfib]
    mp = [len({z % 2 for z in fibre}) == 2 for fibre in pfib]
    require((all(mq) and not any(mp)) or (all(mp) and not any(mq)),
            'PARITY_DICHOTOMY')
    N = rho * (1 << K)
    Pbar = {v % N for v in P}
    require(len(Pbar) == len(P), 'P_PROJECTION_NOT_INJECTIVE')
    for u in sorted({0, 1, R - 1}):
        V = {((q - u) // R) % N for q in qfib[u]}
        require(len(V) == len(qfib[u]) and tiling(V, Pbar, N), 'QUOTIENT_TILING')
        scaled = {(rho * v) % N for v in V}
        require(len(scaled) == len(V) and tiling(scaled, Pbar, N), 'QUOTIENT_DILATION')
        for gamma in range(rho):
            AP = {v % (1 << K) for v in Pbar if v % rho == gamma}
            BV = {v % (1 << K) for v in scaled}
            require(tiling(AP, BV, 1 << K), 'CRT_PARITY_TILING')
    return {'R': R, 'rho': rho, 'K': K, 'a': a, 'b': b,
            'n': n, 'mixed': 'Q' if all(mq) else 'P'}


def main(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    out = {'classification': 'finite exact controls only; not a universal proof'}

    atoms = {'aa', 'b', 'ab'}
    require(all(not (x != y and y.startswith(x)) for x in atoms for y in atoms), 'BORDER_NOT_PREFIX')
    prefixes = {word[:i] for word in atoms for i in range(len(word) + 1)}
    require(all(s + 'a' in prefixes and s + 'b' in prefixes for s in ('', 'a')),
            'BORDER_PREFIX_TREE_NOT_COMPLETE')
    P, Q = border(atoms, 2)
    require(P == {0, 1} and Q == {0}, 'BORDER_POSITIVE_ATOMS')
    require_unique_sums(P, Q, 2)
    bad = atoms | {'ba'}
    BP, BQ = border(bad, 2)
    require('b' + 'ab' == 'ba' + 'b', 'BORDER_NEGATIVE_WORD')
    border_negative = negative('BORDER_DUPLICATE_SUM', require_unique_sums, BP, BQ, 2)
    out['actual_border_small_code'] = {'atoms': sorted(atoms), 'P': sorted(P), 'Q': sorted(Q),
        'negative_ambiguity_word': 'bab', 'negative': border_negative}

    totals = {}
    for n in data['sands_moduli']:
        subsets = [set(c) for k in range(1, n + 1) for c in itertools.combinations(range(n), k)]
        count = tiled = 0
        for A in subsets:
            for B in subsets:
                if len(A) * len(B) == n:
                    criterion = divisor_set(A, n).intersection(divisor_set(B, n)) == {n}
                    direct = tiling(A, B, n)
                    require(criterion == direct, 'SANDS_EXHAUSTIVE_MISMATCH')
                    count += 1
                    tiled += direct
        totals[str(n)] = {'cardinality_pairs': count, 'tilings': tiled}
    A, B, n = {0, 1, 2}, set(range(0, 60, 3)), 60
    require(tiling(A, B, n), 'DILATION_BASE_TILING')
    require_coprime(2, len(A))
    require(tiling({2*x % n for x in A}, B, n), 'DILATION_NONUNIT_MODULUS')
    require(tiling({-2*x % n for x in A}, B, n), 'DILATION_NEGATIVE_SCALAR')
    require(tiling({2*x % n for x in A}, {3*x % n for x in B}, n), 'DILATION_DOUBLE')
    require(tiling({0}, set(range(6)), 6), 'DILATION_ZERO_SINGLETON')
    require(not tiling({3*x % n for x in A}, B, n), 'DILATION_NEGATIVE_NO_COLLISION')
    out['sands_and_dilation'] = {'exhaustive': totals,
        'nonunit_example': {'n': n, 'scalar': 2, 'gcd_scalar_n': math.gcd(2, n)},
        'negative_sands': negative('SANDS_COMMON_NONTRIVIAL_DIVISOR', require_divisor_exclusion, {0, 1}, {0, 1, 2}, 6),
        'negative_dilation': negative('DILATION_NONCOPRIME', require_coprime, 3, len(A))}

    count = 0
    for R in data['transport_R']:
        for y in data['transport_y'] + [R, -R, 2*R]:
            g0 = math.gcd(y, R)
            for h in divisors(R):
                if h % g0 == 0:
                    require(transport(y, R, h) == h, 'TRANSPORT_IDENTITY')
                    count += 1
    require(transport(9, 495, 45) == 45, 'TRANSPORT_NONSQUAREFREE_POSITIVE')
    require(math.gcd(5 * 3, 495) != 45, 'TRANSPORT_DROPPED_POWER_NOT_DETECTED')
    out['transport'] = {'exact_identities': count, 'zero_and_negative_y_included': True,
        'nonsquarefree': {'R': 495, 'y': 9, 'h': 45, 'result': 45, 'wrong_reduced_y_gcd': math.gcd(15, 495)},
        'negative_not_multiple': negative('TRANSPORT_H_NOT_MULTIPLE_G0', transport, 9, 495, 5),
        'negative_not_divisor': negative('TRANSPORT_H_NOT_DIVISOR_R', transport, 9, 495, 18)}

    rho, R, K = 49, 495, 2
    y, x = rho * 9, 45 * 7**3
    good_collision = collision(y, x, rho, R, K)
    bad_lhs = math.gcd(5 * 9, (1 << K) * rho * R)
    bad_rhs = math.gcd(rho * x, (1 << K) * rho * R)
    require(bad_lhs != bad_rhs, 'P5_NEGATIVE_NOT_DISTINGUISHED')
    out['P5'] = {'positive': good_collision, 'x_contains_p_power': 3,
        'negative_missing_rho_lhs_rhs': [bad_lhs, bad_rhs],
        'negative_missing_rho': negative('P5_RHO_NOT_DIVIDING_Y', collision, 9, x, rho, R, K),
        'negative_not_same_g0_class': negative('P5_X_NOT_MULTIPLE_G0', collision, y, 5, rho, R, K)}

    parity = []
    for R in data['parity_R']:
        for rho in data['parity_rho']:
            for K in data['parity_K']:
                for a in range(K + 1):
                    parity.append(parity_case(rho, R, K, a))
    out['parity_fibres'] = {'cases': parity, 'all_fibres_checked': True,
        'quotient_fibres_checked': 'u=0,1,R-1; every gamma',
        'note': 'example tilings are not anchored target tilings'}

    R = data['stabilizer_modulus']
    pi = data['stabilizer_period']
    E = {u for u in range(R) if u % pi in data['stabilizer_E_residues']}
    stabilizer = [s for s in range(R) if {(u + s) % R for u in E} == E]
    require(stabilizer == list(range(0, R, pi)), 'STABILIZER_NOT_EXPECTED_SUBGROUP')
    require_separation(R, E, pi)
    require_separation(R, E, R)
    out['stabilizer'] = {'R': R, 'pi': pi, 'E_size': len(E), 'stabilizer': stabilizer,
        'negative': negative('SEPARATION_MIXED_RESIDUE_CLASS', require_separation, R, E, 3)}

    graphs1 = []
    for R, ell, full_power, pi in data['g1_cases']:
        require(R % full_power == 0 and pi == R // full_power, 'G1_FIXTURE_DIVISIBILITY')
        require(ell in (3, 5, 11) and pi % ell != 0, 'G1_FIXTURE_FREE_COORDINATE')
        require_crt(full_power, pi)
        E = {u for u in range(R) if u % pi == 0}
        require_connected(R, E, (3, 5, 11))
        graphs1.append({'R': R, 'free_prime': ell, 'full_power': full_power, 'pi': pi,
                        'E_size': len(E), 'components': 1})
    Ebad = {0}
    bad_components = graph_components(165, Ebad, (3, 5, 11))
    require(bad_components > 1, 'G1_NEGATIVE_NOT_DISCONNECTED')
    out['G1'] = {'positive': graphs1, 'negative_all_coordinates_needed': {
        'R': 165, 'pi': 165, 'E': [0], 'components': bad_components,
        'reason': negative('GRAPH_DISCONNECTED', require_connected, 165, Ebad, (3, 5, 11))},
        'negative_partial_prime_power': negative('CRT_NONCOPRIME_FULL_POWER', require_crt, 3, 165)}

    graphs2 = []
    for R, pi, w in data['g2_cases']:
        require(R % pi == 0 and R % w == 0 and pi % 165 == 0, 'G2_FIXTURE_DIVISIBILITY')
        require(math.gcd(pi, w) == 1, 'G2_FIXTURE_NOT_COPRIME')
        E = {u for u in range(R) if u % pi == 0}
        require_connected(R, E, (3, 5, 11, w))
        graphs2.append({'R': R, 'pi': pi, 'w': w, 'R_over_pi_w': R // (pi*w),
                        'E_size': len(E), 'components': 1})
    bad2 = graph_components(165, {0}, (3, 5, 11, 3))
    require(bad2 > 1, 'G2_NEGATIVE_NOT_DISCONNECTED')
    out['G2'] = {'positive': graphs2, 'negative_shared_coordinate': {
        'R': 165, 'pi': 165, 'w': 3, 'E': [0], 'components': bad2,
        'reason': negative('GRAPH_DISCONNECTED', require_connected, 165, {0}, (3, 5, 11, 3))}}

    f = data['tail_case']
    R, pi, p, K = f['R'], f['pi'], f['p'], f['K']
    rho = p ** f['e']
    v0 = rho * pi * f['odd_multiplier']
    y = 8 - v0
    w = math.gcd(y, R)
    require(y % 2 == 1 and y % rho == 8 % rho and y % pi == 8 % pi, 'TAIL_ODD_CONGRUENCES')
    require(math.gcd(y, p) == 1 and math.gcd(w, pi) == 1, 'TAIL_COPRIMALITIES')
    require(w == 13, 'TAIL_FIXTURE_W_NOT_13')
    pos = tail_equality(y, 13, p, R, K, rho)
    n = (1 << K) * rho * R
    require(math.gcd(13 * p, n) != pos['gcd'], 'TAIL_NEGATIVE_P_NOT_VISIBLE')
    out['tail_rule'] = {'v0': v0, 'y': y, 'positive': pos,
        'negative_divisible_p': negative('TAIL_X_DIVISIBLE_P', tail_equality, y, 13*p, p, R, K, rho),
        'negative_even_x': negative('TAIL_X_EVEN', tail_equality, y, 26, p, R, K, rho),
        'negative_p_gcd': math.gcd(13*p, n)}
    out['result'] = 'PASS'
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv[1])
