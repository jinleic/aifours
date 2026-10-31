from collections import Counter, deque
from fractions import Fraction
from itertools import combinations
from math import gcd
from time import monotonic

STOP = monotonic() + 50.0
P = (0, 3, 8, 11)
Q = (0, 1, 7, 13, 14)
WORDS = (
    "b", "a" * 3 + "b", "a" * 8 + "b", "a" * 11 + "b",
    "ba", "b" + "a" * 7, "b" + "a" * 13, "b" + "a" * 14,
)


class CheckFailure(ValueError):
    pass


def tick():
    if monotonic() > STOP:
        raise CheckFailure("DEADLINE")


def need(condition, reason):
    tick()
    if not condition:
        raise CheckFailure(reason)


def expect_failure(reason, thunk):
    try:
        thunk()
    except CheckFailure as exc:
        need(str(exc) == reason, "WRONG_MUTANT_REASON")
        return reason
    raise CheckFailure("MUTANT_SURVIVED")


def coefficients(n, a, b, k=1, drop_multiplicities=False):
    tick()
    mapped = tuple((k * x) % n for x in a)
    if drop_multiplicities:
        mapped = tuple(sorted(set(mapped)))
    result = [0] * n
    for x in mapped:
        tick()
        for y in b:
            result[(x + y) % n] += 1
    return tuple(result)


def unit_histogram(n, histogram):
    need(len(histogram) == n, "LENGTH")
    need(sum(histogram) == n, "MASS")
    need(all(c == 1 for c in histogram), "DIRECTNESS")


def admissible(k, size):
    need(gcd(k, size) == 1, "ADMISSIBILITY")


def exhaustive_small_tilings():
    rows = []
    total_nonunits = 0
    for n in range(1, 13):
        pairs = tilings = multipliers = nonunits = 0
        for size_a in range(1, n + 1):
            if n % size_a:
                continue
            size_b = n // size_a
            for aa in combinations(range(1, n), size_a - 1):
                a = (0,) + aa
                for bb in combinations(range(1, n), size_b - 1):
                    tick()
                    b = (0,) + bb
                    pairs += 1
                    original = coefficients(n, a, b)
                    if any(c != 1 for c in original):
                        continue
                    unit_histogram(n, original)
                    tilings += 1
                    for k in range(1, n + 1):
                        if gcd(k, size_a) != 1:
                            continue
                        admissible(k, size_a)
                        image = tuple((k * x) % n for x in a)
                        need(len(set(image)) == size_a, "INJECTIVITY")
                        unit_histogram(n, coefficients(n, a, b, k))
                        multipliers += 1
                        if gcd(k, n) != 1:
                            nonunits += 1
        total_nonunits += nonunits
        rows.append((n, pairs, tilings, multipliers, nonunits))
    need(total_nonunits > 0, "NONUNIT_COVERAGE")
    return tuple(rows)


def check_anchor_collisions():
    cases = (
        ("P", 2, 3, 1, 0, 7, 2),
        ("Q", 8, 8, 0, 0, 1, 2),
        ("Q", 3, 3, 0, 0, 1, 3),
        ("Q", 5, 8, 0, 3, 1, 5),
        ("Q", 11, 11, 0, 0, 1, 11),
    )
    rows = []
    for side, k, p1, q1, p2, q2, prime in cases:
        need(p1 in P and p2 in P, "ACTUAL_HEAD_ANCHORS")
        need(q1 in Q and q2 in Q, "ACTUAL_TAIL_ANCHORS")
        hp, hq = (k, 1) if side == "P" else (1, k)
        left = hp * p1 + hq * q1
        right = hp * p2 + hq * q2
        need(left == right, "ANCHOR_IDENTITY")
        need((p1, q1) != (p2, q2), "ORDERED_PAIR_IDENTITY")
        if side == "P":
            need(q1 != q2, "UNCHANGED_TAIL_DISTINCT")
        else:
            need(p1 != p2, "UNCHANGED_HEAD_DISTINCT")
        for size in range(1, 65):
            need(
                (gcd(k, size) == 1) == (size % prime != 0),
                "COPRIMALITY_EQUIVALENCE",
            )
        rows.append((side, k, (p1, q1), (p2, q2), left))
    return tuple(rows)


def odd_multiplier(m):
    need(m > 0 and m % 2 == 1, "ODD_MODULUS")
    k = (m + 3) // 2
    if k % 2 == 0:
        k += m
    return k


def verify_multiplier(m, head_size, k, difference=12):
    need(m > 0 and m % 2 == 1, "ODD_MODULUS")
    need(k > 0 and k % 2 == 1, "ODD_REPRESENTATIVE")
    need((2 * k - 3) % m == 0, "CONGRUENCE_2K")
    need(gcd(k, head_size) == 1, "HEAD_COPRIMALITY")
    n = 4 * m
    need((8 * k - difference) % n == 0, "ANCHOR_DIFFERENCE")
    need((8 * k + 1 - 13) % n == 0, "ACTUAL_ANCHOR_COLLISION")
    return (n, head_size, k, gcd(k, n))


def check_multiplier_cases():
    cases = (
        (25, 165), (125, 825), (121, 165),
        (121, 1815), (55, 165), (3025, 165),
    )
    rows = []
    for u, w in cases:
        need(u > 0 and w > 0 and (u * w) % 2 == 1,
             "CARDINALITY_PARITY")
        need(u % 3 != 0, "HEAD_HAS_THREE")
        need(w % 165 == 0, "TAIL_PRIMES")
        m = u * w
        k = odd_multiplier(m)
        result = verify_multiplier(m, 2 * u, k)
        need(gcd(k, 4 * m) > 1, "NONUNIT_GROUP_CONTROL")
        need(gcd(k, 2 * w) > 1, "NONUNIT_TAIL_CONTROL")
        rows.append((u, w, result, (8 * k - 12) // (4 * m)))
    return tuple(rows)


def fiber_count(p, a, b, j, t):
    need(p in (3, 5, 11), "FIBER_PRIME")
    need(min(a, b, j, t) >= 1, "FIBER_PARAMETERS")
    return Fraction(
        2 ** (a + b) * p ** (j + t - 2),
        2 ** b * p ** t,
    )


def require_nonintegral(value):
    need(value.denominator != 1, "FIBER_NONINTEGRAL")


def check_integrality():
    rows = []
    for p in (3, 5, 11):
        for a in (1, 2):
            first = fiber_count(p, a, 1, 1, 1)
            second = fiber_count(p, a, 1, 2, 1)
            need(first.denominator == p, "J1_NONINTEGRAL")
            need(second == 2 ** a, "J2_INTEGRAL")
            rows.append((p, a, first, second))
    return tuple(rows)


def check_cyclic_barriers():
    cases = (
        (3, 1, 2, 3), (5, 1, 2, 3), (11, 1, 2, 3),
        (5, 2, 2, 3), (3, 1, 3, 4),
    )
    rows = []
    for p, a, j, v in cases:
        need(p in (3, 5, 11) and a >= 1 and j >= 2 and v >= j + 1,
             "BARRIER_PARAMETERS")
        odd = p ** v
        two = 2 ** (a + 1)
        n = odd * two
        inverse = pow(odd, -1, two)

        def crt(x, y):
            return (x + odd * (((y - x) * inverse) % two)) % n

        universe = set()
        for x in range(odd):
            tick()
            for y in range(two):
                z = crt(x, y)
                need(z % odd == x and z % two == y, "CRT_COORDINATES")
                universe.add(z)
        need(universe == set(range(n)), "CRT_FULL_UNIVERSE")
        head = tuple(sorted({
            crt(x, y)
            for x in range(p ** j)
            for y in range(0, two, 2)
        }))
        tail = tuple(sorted({
            crt(p ** j * h, y)
            for h in range(p ** (v - j))
            for y in (0, 1)
        }))
        need(len(head) == 2 ** a * p ** j, "BARRIER_HEAD_SIZE")
        need(len(tail) == 2 * p ** (v - j), "BARRIER_TAIL_SIZE")
        unit_histogram(n, coefficients(n, head, tail))
        need(all(x % 2 == 0 for x in head), "BARRIER_HEAD_EVEN")
        need(3 not in head, "BARRIER_MISSES_HEAD3")
        need({x % 2 for x in tail} == {0, 1}, "BARRIER_TAIL_PARITIES")
        need(all(x % (p * p) == 0 for x in tail), "BARRIER_TAIL_P2")
        need(len(head) % p == 0 and len(tail) % p == 0,
             "BARRIER_SHARED_PRIME")
        counts = Counter(x % (p * p) for x in head)
        expected = 2 ** a * p ** (j - 2)
        need(set(counts) == set(range(p * p)), "BARRIER_HEAD_COSETS")
        need(all(c == expected for c in counts.values()),
             "BARRIER_COSET_COUNTS")
        rows.append((p, a, j, v, n, len(head), len(tail), "NOT_ANCHORED"))
    return tuple(rows)


def validate_words(words):
    need(len(words) == len(set(words)), "DUPLICATE_WORD")
    need(all(isinstance(w, str) and w for w in words), "EMPTY_WORD")


def first_states(words):
    return frozenset(
        y[len(x):]
        for x in words
        for y in words
        if x != y and y.startswith(x)
    )


def next_states(states, words):
    result = set()
    for residual in states:
        tick()
        for word in words:
            if word.startswith(residual):
                result.add(word[len(residual):])
            if residual.startswith(word):
                result.add(residual[len(word):])
    return frozenset(result)


def sp_queue(words):
    validate_words(words)
    initial = first_states(words)
    queue = deque(sorted(initial))
    seen = set(initial)
    while queue:
        tick()
        residual = queue.popleft()
        if residual == "":
            return (False, "EPSILON", len(seen))
        for successor in sorted(next_states((residual,), words)):
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)
    return (True, "EXHAUSTED", len(seen))


def sp_levels(words):
    validate_words(words)
    state = first_states(words)
    seen = set()
    layers = []
    while True:
        tick()
        layers.append(state)
        if "" in state:
            return (False, "EPSILON", tuple(layers))
        if not state:
            return (True, "EMPTY", tuple(layers))
        if state in seen:
            return (True, "CYCLE", tuple(layers))
        seen.add(state)
        state = next_states(state, words)


def require_ud(words):
    valid, reason, count = sp_queue(words)
    if not valid:
        need(reason == "EPSILON", "SP_UNEXPECTED_FAILURE")
        raise CheckFailure("SP_EPSILON")
    return count


def word_borders(words):
    head = frozenset(
        len(w) - 1 for w in words
        if w.endswith("b") and w.count("b") == 1
        and set(w[:-1]) <= {"a"}
    )
    tail = frozenset(
        len(w) - 1 for w in words
        if w.startswith("b") and w.count("b") == 1
        and set(w[1:]) <= {"a"}
    )
    return head, tail


def verify_borders(head, tail):
    need(head == frozenset(P), "BORDER_HEAD")
    need(tail == frozenset(Q), "BORDER_TAIL")


def check_words():
    need(len(WORDS) == 8, "EIGHT_ORIGINAL_WORDS")
    expected = (
        frozenset("a" * d for d in (1, 6, 7, 12, 13, 14)),
        frozenset("a" * d + "b" for d in (1, 2, 4, 5, 7, 10)),
        frozenset(),
    )
    valid, reason, layers = sp_levels(WORDS)
    need(valid and reason == "EMPTY", "ORIGINAL_LEVEL_UD")
    need(layers == expected, "EXACT_RESIDUAL_LAYERS")
    valid_queue, queue_reason, count = sp_queue(WORDS)
    need(valid_queue and queue_reason == "EXHAUSTED", "ORIGINAL_QUEUE_UD")
    need(count == 12, "ORIGINAL_QUEUE_RESIDUAL_COUNT")
    mutant = tuple(
        "a" * 7 + "b" if w == "a" * 8 + "b" else w
        for w in WORDS
    )
    mutation_reason = expect_failure(
        "SP_EPSILON", lambda: require_ud(mutant)
    )
    mv, mr, ml = sp_levels(mutant)
    need(not mv and mr == "EPSILON", "MUTANT_LEVEL_EPSILON")
    need(len(ml) == 3 and "" in ml[-1], "MUTANT_EPSILON_STAGE")
    left = ("b" + "a" * 7, "b")
    right = ("b", "a" * 7 + "b")
    need(left != right, "MUTANT_DISTINCT_FACTORIZATIONS")
    need(set(left + right) <= set(mutant), "MUTANT_WITNESS_WORDS")
    need("".join(left) == "".join(right), "MUTANT_WITNESS_CONCATENATION")
    cycle_words = ("0", "01", "11")
    cv, cr, cl = sp_levels(cycle_words)
    need(cv and cr == "CYCLE", "CYCLE_CONTROL_LEVELS")
    cq, qr, unused_count = sp_queue(cycle_words)
    need(cq and qr == "EXHAUSTED", "CYCLE_CONTROL_QUEUE")
    head, tail = word_borders(WORDS)
    verify_borders(head, tail)
    border_reason = expect_failure(
        "BORDER_HEAD", lambda: verify_borders(tail, head)
    )
    return (WORDS, layers, count, cl, mutation_reason, border_reason)


def check_basic_controls():
    weighted = coefficients(4, (0, 2), (0, 1), 2)
    unweighted = coefficients(
        4, (0, 2), (0, 1), 2, drop_multiplicities=True
    )
    need(weighted == (2, 2, 0, 0), "WEIGHTED_FOLD_CONTROL")
    need(unweighted == (1, 1, 0, 0), "UNWEIGHTED_FOLD_CONTROL")
    reasons = []
    reasons.append(("drop_multiplicities", expect_failure(
        "MASS", lambda: unit_histogram(4, unweighted)
    )))
    reasons.append(("weighted_nondirect", expect_failure(
        "DIRECTNESS", lambda: unit_histogram(4, weighted)
    )))
    a, b, k = (0, 3), (0, 1, 2), 3
    unit_histogram(6, coefficients(6, a, b))
    admissible(k, len(a))
    unit_histogram(6, coefficients(6, a, b, k))
    need(len({k * x % 6 for x in a}) == len(a), "NONUNIT_INJECTIVITY")
    reasons.append(("gcd_with_group", expect_failure(
        "ADMISSIBILITY", lambda: admissible(k, 6)
    )))
    reasons.append(("gcd_with_opposite_factor", expect_failure(
        "ADMISSIBILITY", lambda: admissible(k, len(b))
    )))
    m = 25 * 165
    correct = odd_multiplier(m)
    verify_multiplier(m, 50, correct)
    reasons.append(("wrong_odd_representative", expect_failure(
        "ODD_REPRESENTATIVE",
        lambda: verify_multiplier(m, 50, correct + m),
    )))
    reasons.append(("wrong_anchor_difference", expect_failure(
        "ANCHOR_DIFFERENCE",
        lambda: verify_multiplier(m, 50, correct, difference=10),
    )))
    reasons.append(("three_in_head", expect_failure(
        "HEAD_COPRIMALITY",
        lambda: verify_multiplier(495, 6, odd_multiplier(495)),
    )))
    reasons.append(("j2_nonintegrality_claim", expect_failure(
        "FIBER_NONINTEGRAL",
        lambda: require_nonintegral(fiber_count(5, 1, 1, 2, 1)),
    )))
    return tuple(reasons)


def run():
    controls = check_basic_controls()
    anchors = check_anchor_collisions()
    multipliers = check_multiplier_cases()
    integrality = check_integrality()
    words = check_words()
    barriers = check_cyclic_barriers()
    small = exhaustive_small_tilings()
    tick()
    return (
        ("status", "ALL_CHECKS_COMPLETED"),
        ("controls", controls),
        ("actual_anchor_collisions", anchors),
        ("cardinality_multiplier_cases", multipliers),
        ("fiber_integrality", integrality),
        ("literal_word_checks", words),
        ("nonanchored_cyclic_barriers", barriers),
        ("normalized_small_tilings", small),
    )


RESULT = run()
