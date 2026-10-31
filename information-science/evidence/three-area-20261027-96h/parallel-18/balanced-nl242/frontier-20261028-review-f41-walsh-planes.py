#!/usr/bin/env python3
"""Independent Walsh-zero, transversal and rank-one ray census for F2^3."""

import argparse
import collections
import itertools
import json
from pathlib import Path

N = 8


def chi(a, x):
    return 1 - 2 * ((a & x).bit_count() & 1)


def require_permutation(f):
    if len(f) != N or sorted(f) != list(range(N)) or f[0] != 0:
        raise ValueError("expected normalized permutation")


def beta_columns(f):
    return (f[3] ^ f[1] ^ f[2], f[5] ^ f[1] ^ f[4], f[6] ^ f[2] ^ f[4])


def rank(vectors):
    space = {0}
    for value in vectors:
        space |= {x ^ value for x in space}
    return len(space).bit_length() - 1


def walsh_rows(f):
    return [[sum(chi(u, f[x]) * chi(v, x) for x in range(N)) for v in range(N)] for u in range(N)]


def verify_planes(f, w):
    b23, b31, b12 = f[6] ^ f[2] ^ f[4], f[5] ^ f[4] ^ f[1], f[3] ^ f[1] ^ f[2]
    j = lambda u: ((u & b23).bit_count() & 1) | (((u & b31).bit_count() & 1) << 1) | (((u & b12).bit_count() & 1) << 2)
    for u in range(1, N):
        radical = j(u)
        if radical:
            if ((u & f[radical]).bit_count() & 1) != 1:
                raise ValueError("nonlinear component has wrong radical value")
            for v in range(N):
                zero_expected = ((v & radical).bit_count() & 1) == 0
                if (w[u][v] == 0) != zero_expected or (not zero_expected and abs(w[u][v]) != 4):
                    raise ValueError("Walsh zero plane mismatch")
        else:
            nonzero = [(v, w[u][v]) for v in range(N) if w[u][v] != 0]
            if len(nonzero) != 1 or nonzero[0][0] == 0 or nonzero[0][1] != 8:
                raise ValueError("linear component Walsh row mismatch")


def count_transversals(w):
    permutation = [0] * N
    def visit(row, used):
        if row == N:
            return 1
        total = 0
        for value in range(1, N):
            if used & (1 << value):
                continue
            if all(w[row ^ earlier][value ^ permutation[earlier]] == 0 for earlier in range(row)):
                permutation[row] = value
                total += visit(row + 1, used | (1 << value))
        return total
    return visit(1, 1)


def inspect_rank1(f):
    require_permutation(f)
    if rank(beta_columns(f)) != 1:
        raise ValueError("expected polar rank one")
    rays = [[tuple(chi(i, f[x]) * chi(j, x) for x in range(N)) for j in range(N)] for i in range(N)]
    counts = collections.Counter(ray for row in rays for ray in row)
    if len(counts) != 16 or set(counts.values()) != {4}:
        raise ValueError("rank-one ray multiplicities differ")
    first = frozenset(rays[0])
    row_sets = collections.Counter(frozenset(row) for row in rays)
    if len(row_sets) != 2 or set(row_sets.values()) != {4} or first not in row_sets:
        raise ValueError("rank-one row types differ")
    other = next(row for row in row_sets if row != first)
    if first & other:
        raise ValueError("rank-one ray bases overlap")
    e, h = list(first), list(other)
    graph = {("e", i): set() for i in range(8)} | {("h", i): set() for i in range(8)}
    for i, left in enumerate(e):
        for j, right in enumerate(h):
            value = sum(x * y for x, y in zip(left, right))
            if value not in (0, -4, 4):
                raise ValueError("cross-ray overlap magnitude differs")
            if value:
                graph[("e", i)].add(("h", j))
                graph[("h", j)].add(("e", i))
    if any(len(neighbors) != 4 for neighbors in graph.values()):
        raise ValueError("cross-ray degree differs")
    unseen = set(graph)
    components = []
    while unseen:
        node = next(iter(unseen))
        unseen.remove(node)
        todo, component = [node], set()
        while todo:
            current = todo.pop()
            component.add(current)
            for neighbor in graph[current]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    todo.append(neighbor)
        components.append(component)
    if len(components) != 2 or any(len(c) != 8 or sum(v[0] == "e" for v in c) != 4 for c in components):
        raise ValueError("cross-ray components differ")
    checks = 0
    for i in range(N):
        for a in range(N):
            for b in range(N):
                expected = 8 if a == b else 0
                if sum(x * y for x, y in zip(rays[i][a], rays[i][b])) != expected:
                    raise ValueError("row Gram mismatch")
                if sum(x * y for x, y in zip(rays[a][i], rays[b][i])) != expected:
                    raise ValueError("column Gram mismatch")
                checks += 2
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    rank_counts = [0] * 4
    tested = [0] * 4
    passed = [0] * 4
    minima = [5041] * 4
    maxima = [0] * 4
    gram_checks = rank1_count = 0
    for tail in itertools.permutations(range(1, N)):
        f = (0,) + tail
        r = rank(beta_columns(f))
        rank_counts[r] += 1
        w = walsh_rows(f)
        verify_planes(f, w)
        # DFS counts all normalized permutation transversals without materializing their list.
        count = count_transversals(w)
        tested[r] += 5040
        passed[r] += count
        minima[r] = min(minima[r], count)
        maxima[r] = max(maxima[r], count)
        if r == 1:
            gram_checks += inspect_rank1(f)
            rank1_count += 1
    controls = {}
    for label, f, expected in (("rank0", tuple(range(N)), "expected polar rank one"),
                               ("nonpermutation", (0, 1, 2, 3, 4, 5, 6, 6), "expected normalized permutation")):
        try:
            inspect_rank1(f)
        except ValueError as error:
            if str(error) != expected:
                raise RuntimeError("negative control failed for an unexpected reason") from error
            controls[label] = "rejected for expected reason"
        else:
            raise RuntimeError("negative control unexpectedly passed")
    result = {"normalized_F_counts_by_rank": rank_counts, "normalized_pi_count_per_F": 5040,
              "transversals_tested_by_rank": tested, "transversals_passed_by_rank": passed,
              "minimum_per_F_by_rank": minima, "maximum_per_F_by_rank": maxima,
              "walsh_zero_planes_checked_for_every_F": True,
              "rank_one_structure_count": rank1_count, "rank_one_row_column_gram_entries": gram_checks,
              "controls": controls,
              "method": "direct character sums, independent DFS of actual transversal permutations, explicit ray overlaps"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print(f"F_rank_counts={rank_counts} tested={tested} passed={passed} per_F_min={minima} per_F_max={maxima}")
    print(f"walsh_planes=ALL_PASS rank1_structures={rank1_count} gram_entries={gram_checks} controls={controls}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()
