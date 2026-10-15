"""Scalar finite-grid specializations of proof Theorem 4, using exact rationals.

Segments are half-open index ranges [a, b), with their optimal constant center.
This code does not estimate an unknown kernel from a seismic trace.
"""
from fractions import Fraction
from typing import Sequence


Segment = tuple[int, int, Fraction]


def greedy_segments(values: Sequence[int | Fraction], tolerance: Fraction) -> list[Segment]:
    """Minimize segment count under a nonnegative uniform error tolerance."""
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")
    result: list[Segment] = []
    start = 0
    while start < len(values):
        low = high = Fraction(values[start])
        end = start + 1
        while end < len(values):
            next_low = min(low, values[end])
            next_high = max(high, values[end])
            if next_high - next_low > 2 * tolerance:
                break
            low, high = next_low, next_high
            end += 1
        result.append((start, end, (low + high) / 2))
        start = end
    return result


def minimax_segments(values: Sequence[int | Fraction], k: int) -> tuple[Fraction, list[Segment]]:
    """Minimize worst absolute error among exactly k nonempty segments."""
    n = len(values)
    if not 1 <= k <= n:
        raise ValueError("k must be between 1 and the number of values")
    costs: dict[tuple[int, int], Fraction] = {}
    centers: dict[tuple[int, int], Fraction] = {}
    for start in range(n):
        low = high = Fraction(values[start])
        for end in range(start + 1, n + 1):
            low = min(low, values[end - 1])
            high = max(high, values[end - 1])
            costs[start, end] = Fraction(high - low) / 2
            centers[start, end] = Fraction(high + low) / 2
    best: dict[tuple[int, int], Fraction] = {(0, 0): Fraction(0)}
    previous: dict[tuple[int, int], int] = {}
    for count in range(1, k + 1):
        for end in range(count, n + 1):
            candidates = ((max(best[count - 1, start], costs[start, end]), start)
                          for start in range(count - 1, end)
                          if (count - 1, start) in best)
            best[count, end], previous[count, end] = min(candidates)
    pieces: list[Segment] = []
    end = n
    for count in range(k, 0, -1):
        start = previous[count, end]
        pieces.append((start, end, centers[start, end]))
        end = start
    pieces.reverse()
    return best[k, n], pieces
