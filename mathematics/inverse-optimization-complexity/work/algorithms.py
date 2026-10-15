"""Algorithms corresponding to proof.md; no external packages.

The forward reduction takes only a yes/no optimality oracle and a valid feasible
start. Enumerating a feasible set is used only in the separately named inverse
reference, never disguised as a polynomial forward algorithm.
"""
from fractions import Fraction
from math import lcm


def augment(verify, cost, target):
    """Schulz's verification -> augmentation reduction (proof Lemma A).

    Return a strictly better feasible tuple, or None if target is optimal.
    verify(cost, target) must be exact, allow arbitrary signed rational costs,
    and accept every feasible target for one fixed binary feasible set.
    """
    target = tuple(target)
    if verify(cost, target):
        return None
    penalty = 1 + sum(map(abs, cost))
    query = list(cost)
    matches = [False] * len(target)
    for i, bit in enumerate(target):
        shift = penalty * (2 * bit - 1)
        query[i] -= shift
        if verify(query, target):
            query[i] += shift
        else:
            matches[i] = True
    return tuple(bit if keep else 1 - bit for bit, keep in zip(target, matches))


def optimize_from_verification(verify, cost, feasible_start):
    """Exact bit-polynomial oracle reduction, including signed/rational costs.

    verify returns only a Boolean, never a better point or objective value.
    Existence of feasible_start is a necessary input promise, not solved here.
    """
    rational = tuple(map(Fraction, cost))
    denominator = lcm(*(value.denominator for value in rational))
    integer = tuple(int(value * denominator) for value in rational)
    flipped = tuple(value < 0 for value in integer)
    absolute = tuple(abs(value) for value in integer)
    bits = max((value.bit_length() for value in absolute), default=0)
    z = tuple(1 - bit if flip else bit for bit, flip in zip(feasible_start, flipped))

    def virtual_verify(virtual_cost, virtual_target):
        original_cost = tuple(-value if flip else value for value, flip in zip(virtual_cost, flipped))
        original_target = tuple(1 - bit if flip else bit for bit, flip in zip(virtual_target, flipped))
        return verify(original_cost, original_target)

    prefix = [0] * len(integer)
    for position in reversed(range(bits)):
        prefix = [2 * old + ((value >> position) & 1) for old, value in zip(prefix, absolute)]
        while True:
            better = augment(virtual_verify, prefix, z)
            if better is None:
                break
            z = better
    return tuple(1 - bit if flip else bit for bit, flip in zip(z, flipped))


def optimize_bottleneck(verify, cost, feasible_start):
    """Theorem B: global min-max optimization using only YES/NO verification.

    Every feasible set must be nonempty. All queries use 0/1 costs and the
    original feasible_start, not a hypothetical feasible restricted target.
    """
    n = len(cost)
    support = {i for i, bit in enumerate(feasible_start) if bit}

    def contains_feasible(allowed):
        if support <= allowed:
            return True
        query = tuple(0 if i in allowed else 1 for i in range(n))
        return not verify(query, feasible_start)

    levels = sorted(set(cost))
    low, high = 0, len(levels) - 1
    while low < high:
        middle = (low + high) // 2
        allowed = {i for i, value in enumerate(cost) if value <= levels[middle]}
        if contains_feasible(allowed):
            high = middle
        else:
            low = middle + 1
    allowed = {i for i, value in enumerate(cost) if value <= levels[low]}
    for i in range(n):
        if i in allowed and contains_feasible(allowed - {i}):
            allowed.remove(i)
    return tuple(int(i in allowed) for i in range(n))


def clip_free_costs(cost, free_target):
    """Exact inverse for SAT x cube with witness costs fixed at zero (Prop. C)."""
    return tuple(min(value, 0) if bit else max(value, 0)
                 for value, bit in zip(cost, free_target))


def inverse_linf_enumerated(feasible, cost, target, weights):
    """Exponential exact reference implementing Proposition L, not a P claim."""
    cost = tuple(map(Fraction, cost))
    weights = tuple(map(Fraction, weights))
    radius = Fraction(0)
    for y in feasible:
        changed = [i for i, (a, b) in enumerate(zip(target, y)) if a != b]
        if not changed:
            continue
        gap = sum(cost[i] * (target[i] - y[i]) for i in changed)
        denominator = sum(1 / weights[i] for i in changed)
        radius = max(radius, gap / denominator)
    modified = tuple(value - radius * (2 * bit - 1) / weight
                     for value, bit, weight in zip(cost, target, weights))
    return modified, radius
