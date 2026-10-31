#!/usr/bin/env python3
"""Check a proposed pair of Latin squares; claims are not inputs."""

L1 = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,0,3,2,5,4,7,6,9,8],
    [2,3,4,5,6,7,8,9,0,1],
    [3,2,5,4,7,6,9,8,1,0],
    [4,5,6,7,8,9,0,1,2,3],
    [5,4,7,6,9,8,1,0,3,2],
    [6,7,8,9,0,1,2,3,4,5],
    [7,6,9,8,1,0,3,2,5,4],
    [8,9,0,1,2,3,4,5,6,7],
    [9,8,1,0,3,2,5,4,7,6],
]
L2 = [
    [0,1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,0,1],
    [4,5,6,7,8,9,0,1,2,3],
    [6,7,8,9,0,1,2,3,4,5],
    [8,9,0,1,2,3,4,5,6,7],
    [1,0,3,2,5,4,7,6,9,8],
    [3,2,5,4,7,6,9,8,1,0],
    [5,4,7,6,9,8,1,0,3,2],
    [7,6,9,8,1,0,3,2,5,4],
    [9,8,1,0,3,2,5,4,7,6],
]


def check(square):
    n = len(square)
    symbols = set(range(n))
    return (all(len(row) == n and set(row) == symbols for row in square),
            all({square[r][c] for r in range(n)} == symbols for c in range(n)))


def main():
    n = len(L1)
    assert len(L2) == n and all(len(row) == n for row in L1 + L2)
    for name, square in (("L1", L1), ("L2", L2)):
        print(name, "rows_latin", check(square)[0], "columns_latin", check(square)[1])
    pair_locations = {}
    for r in range(n):
        for c in range(n):
            pair_locations.setdefault((L1[r][c], L2[r][c]), []).append((r, c))
    repeats = [(pair, cells) for pair, cells in pair_locations.items() if len(cells) > 1]
    print("distinct_ordered_pairs", len(pair_locations), "of", n*n)
    print("repeated_pair_groups", len(repeats))
    print("first_repeated_pair", repeats[0] if repeats else None)
    print("orthogonal", all(check(square) == (True, True) for square in (L1, L2)) and not repeats)


if __name__ == "__main__":
    main()
