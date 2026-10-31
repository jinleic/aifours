"""Unrun local support/word assay; NOT a global AME or phase enumerator.

No program-directed file, standard-stream, network, or subprocess I/O.  A
parent may interpret exit 0 only after a separate whole-source read and GO.
Exit 10--19: small supports; 20--29: cube/structured five; 30--39: exact
unitaries; 40--49: matching; 50--59: mixed bundles; 60--69: binary boxes;
70--79: no-bundle/constant incidence; 80--89: one-bundle incidence;
123: external interrupt; 124: cooperative deadline; 125: unexpected error.
All scientific checks are explicit, not Python assertions.  Python must load
this source and its standard library normally; there is no explicit file I/O.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
import signal
import sys
import time


class CheckFailure(Exception):
    def __init__(self, code):
        self.code = code


class Deadline(Exception):
    pass


class Interrupted(Exception):
    pass


DEADLINE = None
PAIRS = tuple(combinations(range(4), 2))
CUTS = ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2))
BINARY = tuple(product((0, 1), repeat=4))
WORDS4 = tuple(product(range(4), repeat=4))
EVEN = frozenset(w for w in BINARY if sum(w) % 2 == 0)
BALANCED = frozenset(w for w in BINARY if sum(w) == 2)


def require(condition, code):
    if not condition:
        raise CheckFailure(code)


def tick():
    if time.monotonic() >= DEADLINE:
        raise Deadline()


def on_alarm(_signum, _frame):
    raise Deadline()


def on_interrupt(_signum, _frame):
    raise Interrupted()


def column_masks(rows, width):
    return tuple(sum(((row >> j) & 1) << i for i, row in enumerate(rows))
                 for j in range(width))


def mask_rows(mask, height, width):
    return tuple((mask >> (i * width)) & ((1 << width) - 1)
                 for i in range(height))


def min_two(rows, cols):
    return all(x.bit_count() >= 2 for x in rows + cols)


def no_single_overlap(lines):
    return all((a & b).bit_count() != 1 for a, b in combinations(lines, 2))


def connected(rows, cols):
    reached_rows, reached_cols = 1, 0
    while True:
        next_cols = reached_cols
        for i, row in enumerate(rows):
            if reached_rows & (1 << i):
                next_cols |= row
        next_rows = reached_rows
        for j, col in enumerate(cols):
            if next_cols & (1 << j):
                next_rows |= col
        if (next_rows, next_cols) == (reached_rows, reached_cols):
            break
        reached_rows, reached_cols = next_rows, next_cols
    return reached_rows == (1 << len(rows)) - 1 and reached_cols == (1 << len(cols)) - 1


def distinct_low_pairs(lines):
    lows = [x for x in lines if x.bit_count() == 2]
    return len(lows) == len(set(lows))


def twin_clean(rows, cols):
    # In a connected unitary support of square order > 2, two degree-two
    # lines with the same support would isolate a 2x2 unitary component.
    return len(rows) == 2 or (distinct_low_pairs(rows) and distinct_low_pairs(cols))


def degrees(lines):
    return tuple(sorted((x.bit_count() for x in lines), reverse=True))


def support_domain():
    raw, clean = Counter(), Counter()
    raw4, clean4 = Counter(), Counter()
    rectangular = Counter()
    for height in range(1, 5):
        for width in range(1, 5):
            seen = 0
            for mask in range(1 << (height * width)):
                seen += 1
                if mask % 256 == 0:
                    tick()
                rows = mask_rows(mask, height, width)
                cols = column_masks(rows, width)
                if not min_two(rows, cols):
                    continue
                if not connected(rows, cols):
                    continue
                if not no_single_overlap(rows) or not no_single_overlap(cols):
                    continue
                if height != width:
                    rectangular[height, width] += 1
                    continue
                excess = mask.bit_count() - 2 * height
                raw[height, excess] += 1
                if height == 4 and excess in (4, 5):
                    raw4[excess, degrees(rows), degrees(cols)] += 1
                if twin_clean(rows, cols):
                    clean[height, excess] += 1
                    if height == 4 and excess in (4, 5):
                        clean4[excess, degrees(rows), degrees(cols)] += 1
            require(seen == 1 << (height * width), 10)
    expected_raw = {
        (2, 0): 1, (3, 2): 9, (3, 3): 1,
        (4, 4): 132, (4, 5): 240, (4, 6): 120,
        (4, 7): 16, (4, 8): 1,
    }
    expected_clean = dict(expected_raw)
    expected_clean[4, 4] = 96
    require(dict(raw) == expected_raw and dict(clean) == expected_clean, 11)
    p33, p42, p4333, p4432 = (3, 3, 3, 3), (4, 4, 2, 2), (4, 3, 3, 3), (4, 4, 3, 2)
    require(dict(raw4) == {
        (4, p33, p33): 24, (4, p42, p33): 36,
        (4, p33, p42): 36, (4, p42, p42): 36,
        (5, p4333, p4333): 96, (5, p4432, p4432): 144,
    }, 12)
    require(dict(clean4) == {
        (4, p33, p33): 24, (4, p42, p33): 36,
        (4, p33, p42): 36,
        (5, p4333, p4333): 96, (5, p4432, p4432): 144,
    }, 13)
    require(rectangular[2, 3] > 0 and rectangular[3, 2] > 0, 14)

    # These controls exercise different actual failure mechanisms.
    r = (1, 3)
    require(not min_two(r, column_masks(r, 2)), 15)
    r = (3, 3, 12, 12)
    c = column_masks(r, 4)
    require(min_two(r, c) and no_single_overlap(r) and no_single_overlap(c)
            and not connected(r, c), 16)
    r = (3, 6, 5)
    c = column_masks(r, 3)
    require(min_two(r, c) and connected(r, c)
            and not no_single_overlap(r) and not no_single_overlap(c), 17)
    r = (3, 3, 15, 15)
    c = column_masks(r, 4)
    require(min_two(r, c) and connected(r, c) and no_single_overlap(r)
            and no_single_overlap(c) and not twin_clean(r, c), 18)
    r = (7, 7)
    c = column_masks(r, 3)
    require(min_two(r, c) and connected(r, c) and no_single_overlap(r)
            and no_single_overlap(c) and len(r) != len(c), 19)


def cube_and_structured_five():
    histogram = Counter()
    total = 0
    for chosen in combinations(range(8), 5):
        vertices = set(chosen)
        by_direction = tuple(sum(1 for x in chosen if not (x & (1 << axis))
                                 and (x | (1 << axis)) in vertices)
                             for axis in range(3))
        pair_edges = sum((x ^ y).bit_count() == 1 for x, y in combinations(chosen, 2))
        require(sum(by_direction) == pair_edges and pair_edges <= 5, 20)
        require(not all(x >= 2 for x in by_direction), 21)
        histogram[pair_edges] += 1
        total += 1
    require(total == 56 and dict(histogram) == {3: 8, 4: 24, 5: 24}, 22)
    star = {0, 1, 2, 4, 7}
    require(tuple(sum(1 for x in star if not (x & (1 << axis))
                      and (x | (1 << axis)) in star) for axis in range(3)) == (1, 1, 1), 23)

    # Extra structured case only: order 5, both sides exactly degree 3.
    # Sorting row neighborhoods is complete modulo row permutations, which
    # preserve both column degrees and every overlap condition.
    choices = tuple(sum(1 << j for j in comb) for comb in combinations(range(5), 3))
    seen = regular = passing = 0
    for rows in combinations_with_replacement(choices, 5):
        seen += 1
        if seen % 128 == 0:
            tick()
        cols = column_masks(rows, 5)
        if all(col.bit_count() == 3 for col in cols):
            regular += 1
            if no_single_overlap(rows) and no_single_overlap(cols):
                passing += 1
    require(seen == 2002 and regular > 0 and passing == 0, 24)
    cycle = tuple(sum(1 << ((i + k) % 5) for k in range(3)) for i in range(5))
    require(all(x.bit_count() == 3 for x in column_masks(cycle, 5))
            and not no_single_overlap(cycle), 25)


def z(real=0, imag=0):
    return (Fraction(real), Fraction(imag))


def za(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def zconj(a):
    return (a[0], -a[1])


def gram(matrix, column=False, conjugate=True):
    n = len(matrix)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            value = z()
            for k in range(n):
                a = matrix[k][i] if column else matrix[i][k]
                b = matrix[k][j] if column else matrix[j][k]
                value = za(value, zm(a, zconj(b) if conjugate else b))
            row.append(value)
        result.append(tuple(row))
    return tuple(result)


def phased(real_matrix):
    row_phase = (z(1), z(Fraction(3, 5), Fraction(4, 5)),
                 z(Fraction(5, 13), Fraction(12, 13)))
    col_phase = (z(Fraction(5, 13), Fraction(12, 13)), z(1),
                 z(Fraction(3, 5), Fraction(-4, 5)))
    return tuple(tuple(zm(zm(z(real_matrix[i][j]), row_phase[i]), col_phase[j])
                       for j in range(3)) for i in range(3))


def rational_unitaries():
    f = Fraction
    minus = phased(((0, f(3, 5), f(4, 5)),
                    (f(3, 5), f(16, 25), f(-12, 25)),
                    (f(4, 5), f(-12, 25), f(9, 25))))
    full = phased(((f(7, 9), f(-4, 9), f(-4, 9)),
                   (f(-4, 9), f(1, 9), f(-8, 9)),
                   (f(-4, 9), f(-8, 9), f(1, 9))))
    identity = tuple(tuple(z(i == j) for j in range(3)) for i in range(3))
    for matrix, support in ((minus, 8), (full, 9)):
        require(sum(entry != z() for row in matrix for entry in row) == support, 30)
        require(any(entry[1] != 0 for row in matrix for entry in row), 31)
        require(gram(matrix) == identity and gram(matrix, column=True) == identity, 32)
        require(gram(matrix, conjugate=False) != identity, 33)
    wrong_norm = (tuple((z(1),) + minus[0][1:]), minus[1], minus[2])
    require(gram(wrong_norm)[0][0] == z(2), 34)
    duplicate = (minus[0], minus[0], minus[2])
    duplicate_gram = gram(duplicate)
    require(all(duplicate_gram[i][i] == z(1) for i in range(3))
            and duplicate_gram[0][1] == z(1), 35)
    support_only = tuple(tuple(z(1 if (i, j) != (0, 0) else 0)
                               for j in range(3)) for i in range(3))
    require(sum(x != z() for row in support_only for x in row) == 8
            and gram(support_only) != identity, 36)


def complement(pair):
    return tuple(i for i in range(4) if i not in pair)


def forced_binary(c):
    words = set()
    for i, j, k, l in CUTS:
        for w in BINARY:
            if (w[i] ^ w[j]) == c[tuple(sorted((i, j)))] and \
               (w[k] ^ w[l]) == c[tuple(sorted((k, l)))]:
                words.add(w)
    return frozenset(words)


def local_matching_possible(c, words):
    for i, j, k, l in CUTS:
        first, second = tuple(sorted((i, j))), tuple(sorted((k, l)))
        high_neighbors = {(b, b ^ c[second]) for b in (0, 1)}
        low_neighbors = set()
        for bit in (0, 1):
            neighbors = {(w[k], w[l]) for w in words
                         if w[i] == bit and w[j] == (bit ^ c[first])}
            if not high_neighbors.issubset(neighbors) or len(neighbors) > 3:
                return False
            low_neighbors.update(neighbors - high_neighbors)
        if len(low_neighbors) > 1:
            return False
    return True


def switched(word, switches):
    return tuple((v ^ switches[i]) if v < 2 else v for i, v in enumerate(word))


def matching_dichotomy():
    valid = []
    for bits in product((0, 1), repeat=6):
        c = dict(zip(PAIRS, bits))
        parities = (c[0, 1] ^ c[2, 3], c[0, 2] ^ c[1, 3], c[0, 3] ^ c[1, 2])
        compatible = len(set(parities)) == 1
        words = forced_binary(c)
        require(local_matching_possible(c, words) == compatible, 40)
        if not compatible:
            continue
        p = parities[0]
        switch = (0, c[0, 1] ^ p, c[0, 2] ^ p, c[0, 3] ^ p)
        require(all((c[i, j] ^ switch[i] ^ switch[j]) == p for i, j in PAIRS), 41)
        normalized = frozenset(switched(w, switch) for w in words)
        require(normalized == (EVEN if p == 0 else BALANCED), 42)
        valid.append((c, p, switch))
    require(len(valid) == 16 and sum(p == 0 for _, p, _ in valid) == 8
            and sum(p == 1 for _, p, _ in valid) == 8, 43)
    bad = dict(zip(PAIRS, (0, 0, 0, 0, 0, 1)))
    require(not local_matching_possible(bad, forced_binary(bad)), 44)
    return valid


def pair_count(words, pair, a, b):
    i, j = pair
    return sum(w[i] == a and w[j] == b for w in words)


def bundle_words(missing, majority, low):
    present = tuple(i for i in range(4) if i != missing)
    result = set()
    for odd in present:
        w = [majority] * 4
        w[missing] = low
        w[odd] = 1 - majority
        result.add(tuple(w))
    return frozenset(result)


def local_bundle_closure(seed, c):
    result = {seed}
    high = [i for i in range(4) if seed[i] < 2]
    for i, j in combinations(high, 2):
        if seed[i] ^ seed[j] == c[i, j]:
            mate = list(seed)
            mate[i] ^= 1
            mate[j] ^= 1
            result.add(tuple(mate))
    return frozenset(result)


def mixed_bundles(valid):
    checked_gauges = checked_seeds = checked_pairs = 0
    for c, p, switch in valid:
        if p != 1:
            continue
        checked_gauges += 1
        base = frozenset(switched(w, switch) for w in BALANCED)
        bundles = []
        for missing in range(4):
            for majority in (0, 1):
                for low in (2, 3):
                    bundle = frozenset(switched(w, switch)
                                       for w in bundle_words(missing, majority, low))
                    require(len(bundle) == 3 and bundle.isdisjoint(base), 50)
                    for seed in bundle:
                        require(local_bundle_closure(seed, c) == bundle, 51)
                        checked_seeds += 1
                    triple = tuple(i for i in range(4) if i != missing)
                    for i, j in combinations(triple, 2):
                        for bit in (0, 1):
                            require(pair_count(base | bundle, (i, j), bit,
                                               bit ^ c[i, j]) == 3, 52)
                    bundles.append(bundle)
        require(len(bundles) == 16 and len(set(bundles)) == 16, 53)
        for first, second in combinations(bundles, 2):
            combined = base | first | second
            overflow = any(pair_count(combined, (i, j), bit, bit ^ c[i, j]) > 3
                           for i, j in PAIRS for bit in (0, 1))
            require(overflow, 54)
            checked_pairs += 1
        example = next(iter(bundles[0]))
        require(len(local_bundle_closure(example, c) - {example}) == 2, 55)
    require((checked_gauges, checked_seeds, checked_pairs) == (8, 384, 960), 56)


def low_binary_overflow(words, high_parity):
    return any(pair_count(words, pair, bit, bit ^ (1 - high_parity)) > 2
               for pair in PAIRS for bit in (0, 1))


def extension_words(cells, high_parity):
    result = set()
    for pair in PAIRS:
        i, j = pair
        k, l = complement(pair)
        for bit in (0, 1):
            w = [None] * 4
            w[i], w[j] = bit, bit ^ high_parity
            w[k], w[l] = cells[pair]
            result.add(tuple(w))
    return frozenset(result)


def consistent_low_cells(cells):
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            seen = []
            for pair in PAIRS:
                if i in pair and j not in pair:
                    seen.append(cells[pair][complement(pair).index(j)])
            if len(set(seen)) != 1:
                return False
    return True


def actual_degree_three(base, extra):
    words = base | extra
    return all(len({w[j] for w in words if w[i] == 0}) == 3
               for i in range(4) for j in range(4) if i != j)


def box_and_no_bundle():
    # All candidate shared complementary values, not a selected example.
    for pair in PAIRS:
        i, j = pair
        k, l = complement(pair)
        accepted = set()
        for a, b in product(range(4), repeat=2):
            if (a, b) in ((0, 0), (1, 1)):
                continue
            extras = set()
            for bit in (0, 1):
                w = [None] * 4
                w[i], w[j], w[k], w[l] = bit, bit, a, b
                extras.add(tuple(w))
            require(len(extras) == 2 and extras.isdisjoint(EVEN), 60)
            if not low_binary_overflow(EVEN | extras, 0):
                accepted.add((a, b))
        require(accepted == set(product((2, 3), repeat=2)), 61)
    # Concrete high/nonhigh candidate fails because an already full low pair
    # receives an additional occurrence, not merely because it is unwanted.
    bad_extras = {(0, 0, 0, 2), (1, 1, 0, 2)}
    require(pair_count(EVEN, (0, 2), 1, 0) == 2
            and pair_count(EVEN | bad_extras, (0, 2), 1, 0) == 3, 62)

    consistent = 0
    for index, values in enumerate(product((2, 3), repeat=12)):
        if index % 64 == 0:
            tick()
        cells = {pair: (values[2 * n], values[2 * n + 1])
                 for n, pair in enumerate(PAIRS)}
        even_extra = extension_words(cells, 0)
        anti_extra = extension_words(cells, 1)
        require(len(even_extra) == len(anti_extra) == 12, 63)
        yes = consistent_low_cells(cells)
        require(actual_degree_three(EVEN, even_extra) == yes
                and actual_degree_three(BALANCED, anti_extra) == yes, 64)
        if not yes:
            continue
        consistent += 1
        unified = []
        for j in range(4):
            used = {cells[pair][complement(pair).index(j)]
                    for pair in PAIRS if j not in pair}
            require(len(used) == 1, 65)
            unified.append(next(iter(used)))
        for i in range(4):
            require(sum(w[i] == unified[i] for w in even_extra) == 6, 66)
            for bit in (0, 1):
                require(sum(w[i] == bit for w in EVEN | even_extra) == 7, 67)
                require(sum(w[i] == bit for w in BALANCED | anti_extra) == 6, 70)
                for j in range(4):
                    if j != i:
                        require(sum(w[i] == bit and w[j] == bit
                                    for w in BALANCED | anti_extra) == 1, 71)
                # Under degree 3 and h=1 there is one further occurrence.
                # Exhaust all symbol words: covering all three missing equal
                # pairs in that one occurrence forces the excluded constant.
                candidates = [w for w in WORDS4 if w[i] == bit
                              and w != (bit, bit, bit, bit)
                              and all(w[j] == bit for j in range(4) if j != i)]
                require(not candidates, 72)
        available = [tuple(v for v in (2, 3) if v != unified[j]) for j in range(4)]
        require(len(tuple(product(*available))) == 1 and 24 - 8 - 12 == 4, 68)
    require(consistent == 16, 69)

    # Every weight-1/3 binary word forces a mate in its high row.  Their
    # common low complementary pair already has one balanced occurrence.
    for w in BINARY:
        if sum(w) not in (1, 3):
            continue
        violations = 0
        for i, j in PAIRS:
            if w[i] ^ w[j] != 1:
                continue
            k, l = complement((i, j))
            require(w[k] == w[l], 73)
            mate = list(w)
            mate[i] ^= 1
            mate[j] ^= 1
            mate = tuple(mate)
            require(w not in BALANCED and mate not in BALANCED and mate != w, 74)
            require(pair_count(BALANCED, (k, l), w[k], w[l]) == 1, 75)
            require(pair_count(BALANCED | {w, mate}, (k, l), w[k], w[l]) == 3, 76)
            violations += 1
        require(violations > 0, 77)
    # Low rows are degree two: 0000 creates an overlap at 00, so 1111 is
    # the only remaining column that can prevent a singleton overlap.
    for i, j, k, l in CUTS:
        base = BALANCED | {(0, 0, 0, 0)}
        row00 = {(w[k], w[l]) for w in base if w[i] == w[j] == 0}
        row11 = {(w[k], w[l]) for w in base if w[i] == w[j] == 1}
        require(row00 == {(0, 0), (1, 1)} and row11 == {(0, 0)}, 78)
        possible = [(a, b) for a, b in product((0, 1), repeat=2)
                    if (a, b) not in row11 and len(row00 & (row11 | {(a, b)})) != 1]
        require(possible == [(1, 1)], 79)
    require(BALANCED | {(0, 0, 0, 0), (1, 1, 1, 1)} == EVEN, 79)


def one_bundle():
    for missing in range(4):
        others = tuple(i for i in range(4) if i != missing)
        for majority in (0, 1):
            for low in (2, 3):
                bundle = bundle_words(missing, majority, low)
                base = BALANCED | bundle
                require(not low_binary_overflow(base, 1), 80)
                for bit in (majority, 1 - majority):
                    maxima = []
                    for w in WORDS4:
                        if w[missing] != bit or w in base or w == (bit,) * 4:
                            continue
                        if low_binary_overflow(base | {w}, 1):
                            continue
                        maxima.append(sum(w[j] == bit for j in others))
                    require(max(maxima) == (1 if bit == majority else 2), 81)
                # Every choice of the six binary low symbols in the three
                # shared complementary pairs gives six distinct D-high words.
                for values in product((2, 3), repeat=6):
                    extra = set()
                    for index, j in enumerate(others):
                        rest = tuple(k for k in others if k != j)
                        for bit in (0, 1):
                            w = [None] * 4
                            w[missing], w[j] = bit, 1 - bit
                            w[rest[0]], w[rest[1]] = values[2 * index:2 * index + 2]
                            extra.add(tuple(w))
                    require(len(extra) == 6 and extra.isdisjoint(base), 82)
                    for bit in (0, 1):
                        require(sum(w[missing] == bit for w in base | extra) == 6, 83)
                        for j in others:
                            require(sum(w[missing] == bit and w[j] == bit
                                        for w in base | extra) == 1, 84)
                # Three remaining equal pairs need at least 3 or 2 new
                # occurrences; s=2d+1 makes both lower bounds at least 9.
                require(6 + 3 == 9 and 6 + 2 == 8 and 2 * 4 + 1 == 9
                        and 4 + 4 + 2 + 2 > 11, 85)


def run():
    support_domain()
    cube_and_structured_five()
    rational_unitaries()
    valid = matching_dichotomy()
    mixed_bundles(valid)
    box_and_no_bundle()
    one_bundle()
    tick()


def main():
    global DEADLINE
    DEADLINE = time.monotonic() + 44.0
    signal.signal(signal.SIGALRM, on_alarm)
    signal.signal(signal.SIGINT, on_interrupt)
    signal.signal(signal.SIGTERM, on_interrupt)
    signal.setitimer(signal.ITIMER_REAL, 44.0)
    try:
        run()
    except CheckFailure as exc:
        return exc.code
    except Deadline:
        return 124
    except Interrupted:
        return 123
    except Exception:
        return 125
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    return 0


if __name__ == "__main__":
    sys.exit(main())
