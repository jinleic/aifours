#!/usr/bin/env python3
"""UNRUN candidate: exact, bounded checks of the f786 t=22 local interfaces.

No inputs, filesystem writes, solver, floating point, network, or third-party
packages.  Coefficients for the local gadget are integers representing the
actual coefficients divided by sqrt(2).  This is NOT a P-completion search,
a 28-word E search, a 50-word state, or a global AME bound.

Parent must whole-read these exact source bytes and separately authorize any
execution.  A successful run would check only the explicit finite assertions
below and their named mutants, not prove an unbounded or global statement.
"""

from itertools import combinations, combinations_with_replacement, product
import json


CUTS = (
    ("AB|CD", (0, 1), (2, 3)),
    ("AC|BD", (0, 2), (1, 3)),
    ("AD|BC", (0, 3), (1, 2)),
)
ALPHABET = range(6)


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def word(text):
    return tuple(int(c) for c in text)


def project(w, indices):
    return tuple(w[i] for i in indices)


def squares(words, cut):
    """Return physically realized K2,2 blocks in a cut, or None on failure.

    Each square is (upper-left, upper-right, lower-left, lower-right), where
    row and column values are sorted.  Input words are actual four-tuples.
    The entire active support must partition into full two-regular squares.
    """
    _, row_positions, col_positions = cut
    cells = {}
    row_neighbors = {}
    col_neighbors = {}
    for w in words:
        r = project(w, row_positions)
        c = project(w, col_positions)
        if (r, c) in cells:
            return None
        cells[r, c] = w
        row_neighbors.setdefault(r, set()).add(c)
        col_neighbors.setdefault(c, set()).add(r)
    if not cells:
        return None
    if any(len(neighbors) != 2 for neighbors in row_neighbors.values()):
        return None
    if any(len(neighbors) != 2 for neighbors in col_neighbors.values()):
        return None
    seen_rows = set()
    result = []
    for r in sorted(row_neighbors):
        if r in seen_rows:
            continue
        cols = sorted(row_neighbors[r])
        rows = sorted(col_neighbors[cols[0]])
        if len(rows) != 2 or r not in rows:
            return None
        if any(row_neighbors[rr] != set(cols) for rr in rows):
            return None
        if any(col_neighbors[cc] != set(rows) for cc in cols):
            return None
        if seen_rows.intersection(rows):
            return None
        seen_rows.update(rows)
        result.append((cells[rows[0], cols[0]], cells[rows[0], cols[1]],
                       cells[rows[1], cols[0]], cells[rows[1], cols[1]]))
    if len(seen_rows) != len(row_neighbors) or 4 * len(result) != len(cells):
        return None
    return result


def square_row(square):
    a, b, c, d = square
    return {a: 1, b: -1, c: -1, d: 1}


def cut_errors(tensor, cut):
    """Check one physical 36x36 flattening using exact integer Grams.

    Only active rows/columns should have squared integer norm 2; the other
    30 on each side are zero.  All off-diagonal Gram entries must vanish.
    Scaling every integer by 1/sqrt(2) then gives unit active blocks.
    """
    _, row_positions, col_positions = cut
    matrix = [[0] * 36 for _ in range(36)]
    for w, value in tensor.items():
        require(len(w) == 4 and all(x in ALPHABET for x in w), "word domain")
        require(isinstance(value, int) and value != 0, "nonzero integer entry")
        r0, r1 = project(w, row_positions)
        c0, c1 = project(w, col_positions)
        r, c = 6 * r0 + r1, 6 * c0 + c1
        require(matrix[r][c] == 0, "duplicate physical matrix cell")
        matrix[r][c] = value

    row_degrees = [sum(value != 0 for value in row) for row in matrix]
    col_degrees = [sum(matrix[r][c] != 0 for r in range(36))
                   for c in range(36)]
    active_rows = [r for r in range(36) if row_degrees[r]]
    active_cols = [c for c in range(36) if col_degrees[c]]
    errors = set()
    if len(active_rows) != 6 or len(active_cols) != 6:
        errors.add("active_shape")
    if (any(row_degrees[r] != 2 for r in active_rows) or
            any(col_degrees[c] != 2 for c in active_cols)):
        errors.add("pair_multiplicity")
    blocks = squares(tensor, cut)
    if blocks is None or len(blocks) != 3:
        errors.add("blocks")

    for r in range(36):
        norm = sum(matrix[r][c] ** 2 for c in range(36))
        if norm != (2 if row_degrees[r] else 0):
            errors.add("row_norm")
    for c in range(36):
        norm = sum(matrix[r][c] ** 2 for r in range(36))
        if norm != (2 if col_degrees[c] else 0):
            errors.add("col_norm")
    for r, s in combinations(range(36), 2):
        if sum(matrix[r][c] * matrix[s][c] for c in range(36)):
            errors.add("row_orth")
    for c, d in combinations(range(36), 2):
        if sum(matrix[r][c] * matrix[r][d] for r in range(36)):
            errors.add("col_orth")
    return errors


def components(words):
    """Connected components of agreement in at least two physical parties."""
    remaining = set(words)
    result = []
    while remaining:
        root = min(remaining)
        remaining.remove(root)
        component = {root}
        frontier = [root]
        while frontier:
            a = frontier.pop()
            neighbors = {b for b in remaining
                         if sum(x == y for x, y in zip(a, b)) >= 2}
            remaining.difference_update(neighbors)
            component.update(neighbors)
            frontier.extend(neighbors)
        result.append(component)
    return result


def check_gadget():
    # Written independently both as a literal signed list and by the L/R rule.
    literal = (
        ("0000", 1), ("0001", 1), ("0210", 1), ("0211", -1),
        ("1110", 1), ("1111", 1), ("1020", 1), ("1021", -1),
        ("2220", 1), ("2221", 1), ("2100", 1), ("2101", -1),
    )
    tensor = {word(text): value for text, value in literal}
    require(len(tensor) == len(literal) == 12, "gadget word count/distinctness")
    formula = {}
    for i in range(3):
        left = (i, i, i)
        right = (i, (i - 1) % 3, (i + 1) % 3)
        for d in range(2):
            formula[left + (d,)] = 1
            formula[right + (d,)] = -1 if d == 1 else 1
    require(tensor == formula, "gadget literal versus L/R formula")
    require(tuple(len({w[i] for w in tensor}) for i in range(4)) == (3, 3, 3, 2),
            "gadget physical alphabet profile")
    for i in range(4):
        multiplicities = sorted(sum(w[i] == x for w in tensor)
                                for x in {w[i] for w in tensor})
        require(multiplicities == ([4, 4, 4] if i < 3 else [6, 6]),
                "gadget one-party word multiplicities")
    require(len(components(tensor)) == 1, "gadget agreement connectedness")
    for cut in CUTS:
        require(not cut_errors(tensor, cut), "gadget cut " + cut[0])
        blocks = squares(tensor, cut)
        require(blocks is not None and len(blocks) == 3, "gadget square count")
        for a, b, c, d in blocks:
            require(tensor[a] * tensor[d] + tensor[b] * tensor[c] == 0,
                    "gadget simultaneous phase equation")

    # A single wrong phase preserves support/norms but breaks both Grams in
    # every cut.  It must not be rejected for an unrelated structural reason.
    one_phase = tensor.copy()
    one_phase[word("0211")] *= -1
    for cut in CUTS:
        require(cut_errors(one_phase, cut) == {"row_orth", "col_orth"},
                "single-phase mutant intended orthogonality reason " + cut[0])

    # Two D=1 flips preserve the AD|BC cut, while AB|CD and AC|BD fail.
    # This catches a checker which only pays attention to that one good cut.
    one_cut_only = tensor.copy()
    for w in (word("0001"), word("0211")):
        one_cut_only[w] *= -1
    require(cut_errors(one_cut_only, CUTS[0]) == {"row_orth", "col_orth"},
            "one-cut mutant AB|CD intended reason")
    require(cut_errors(one_cut_only, CUTS[1]) == {"row_orth", "col_orth"},
            "one-cut mutant AC|BD intended reason")
    require(not cut_errors(one_cut_only, CUTS[2]),
            "one-cut mutant AD|BC must still pass")

    amplitude = tensor.copy()
    amplitude[word("0000")] = 2
    for cut in CUTS:
        require(cut_errors(amplitude, cut) ==
                {"row_norm", "col_norm", "row_orth", "col_orth"},
                "amplitude mutant norm and orthogonality reasons " + cut[0])

    missing = tensor.copy()
    del missing[word("0000")]
    for cut in CUTS:
        errors = cut_errors(missing, cut)
        require({"pair_multiplicity", "blocks", "row_norm", "col_norm"} <= errors,
                "missing-word mutant singleton/block reasons " + cut[0])
    return {"words": len(tensor), "active_shape_per_cut": [6, 6],
            "blocks_per_cut": 3, "agreement_components": 1,
            "mutants": ["single_phase", "one_cut_only", "amplitude", "missing_word"]}


def find_square(blocks, wanted):
    hits = [square for square in blocks if set(square) == wanted]
    require(len(hits) == 1, "specified physical square must occur exactly once")
    return square_row(hits[0])


def linear_combination(rows, coefficients, words):
    return {w: sum(coefficient * row.get(w, 0)
                   for row, coefficient in zip(rows, coefficients)) for w in words}


def check_even_dependency():
    even = {w for w in product((0, 1), repeat=4) if sum(w) % 2 == 0}
    expected_words = {word(s) for s in
                      ("0000", "0011", "0101", "0110",
                       "1001", "1010", "1100", "1111")}
    require(even == expected_words and len(even) == 8, "eight even words")
    blocks = [squares(even, cut) for cut in CUTS]
    require(all(b is not None and len(b) == 2 for b in blocks),
            "even support has two physical squares per cut")
    specs = (
        {"0000": 1, "1111": 1, "0011": -1, "1100": -1},
        {"0011": 1, "1100": 1, "0110": -1, "1001": -1},
        {"0000": 1, "1111": 1, "0110": -1, "1001": -1},
    )
    rows = []
    for cut_blocks, spec in zip(blocks, specs):
        expected = {word(k): v for k, v in spec.items()}
        actual = find_square(cut_blocks, set(expected))
        require(actual == expected, "declared cut, words, and square signs")
        rows.append(actual)
    y = (1, 1, -1)
    exact = linear_combination(rows, y, even)
    require(all(v == 0 for v in exact.values()) and sum(y) % 2 == 1,
            "odd-sum exact integer dependency")

    # Independent row-orientation changes must not alter the obstruction.
    for flips in product((-1, 1), repeat=3):
        flipped_rows = [{w: flips[i] * v for w, v in row.items()}
                        for i, row in enumerate(rows)]
        flipped_y = tuple(flips[i] * y[i] for i in range(3))
        require(all(v == 0 for v in
                    linear_combination(flipped_rows, flipped_y, even).values())
                and sum(flipped_y) % 2 == 1, "row orientation invariance")

    # This actual three-row example is a mod-2 kernel trap: coefficients
    # (1,1,1) have odd sum and vanish mod 2, but their integer sum is 2*r3.
    mod2_mutant = (1, 1, 1)
    residue = linear_combination(rows, mod2_mutant, even)
    require(sum(mod2_mutant) % 2 == 1 and
            all(v % 2 == 0 for v in residue.values()) and
            any(v != 0 for v in residue.values()) and
            all(residue[w] == 2 * rows[2].get(w, 0) for w in even),
            "mod-2-only dependency mutant must fail integer kernel")
    even_y = (2, 2, -2)
    require(all(v == 0 for v in linear_combination(rows, even_y, even).values())
            and sum(even_y) % 2 == 0,
            "even-sum dependency mutant must fail oddness")
    return {"words": len(even), "squares_per_cut": 2,
            "dependency": list(y), "coefficient_sum": sum(y),
            "orientation_choices": 8,
            "mutants": ["mod2_not_integer_kernel", "even_coefficient_sum"]}


def moments(q):
    return (6 * sum(q) - 56,
            sum(q[i] * q[j] for i, j in combinations(range(4), 2)) - 84)


def n_errors(q, counts):
    require(len(counts) == 5, "five k-counts")
    s1, s2 = moments(q)
    errors = set()
    if any(not isinstance(n, int) or n < 0 for n in counts):
        errors.add("nonnegative_integer")
    if sum(counts) != 22:
        errors.add("count_22")
    if sum(k * counts[k] for k in range(5)) != s1:
        errors.add("first_moment")
    if sum((k * (k - 1) // 2) * counts[k] for k in range(5)) != s2:
        errors.add("second_moment")
    full_parties = sum(size == 6 for size in q)
    if any(counts[k] for k in range(full_parties)):
        errors.add("full_alphabet_lower_k")
    return errors


def moment_solutions(q):
    """All nonnegative n_0,...,n_4 satisfying moments and full-party bound."""
    s1, _ = moments(q)
    result = set()
    for n0 in range(23):
        for n1 in range(23 - n0):
            for n2 in range(23 - n0 - n1):
                rest = 22 - n0 - n1 - n2
                n4 = s1 - n1 - 2 * n2 - 3 * rest
                n3 = rest - n4
                if n3 < 0 or n4 < 0:
                    continue
                counts = (n0, n1, n2, n3, n4)
                if not n_errors(q, counts):
                    result.add(counts)
    return result


def degree_vectors(size, maximum):
    return {v for v in combinations_with_replacement(range(2, maximum + 1), size)
            if sum(v) == 14}


def degree_errors(vector, size, maximum):
    errors = set()
    if len(vector) != size:
        errors.add("degree_length")
    if sum(vector) != 14:
        errors.add("degree_sum")
    if any(d < 2 for d in vector):
        errors.add("degree_min")
    if any(d > maximum for d in vector):
        errors.add("degree_max")
    return errors


def check_profiles():
    require(tuple(3 - 2 * k + k * (k - 1) // 2 for k in range(5)) ==
            (3, 1, 0, 0, 1), "moment identity coefficients")
    candidates = [q for q in combinations_with_replacement(range(3, 7), 4)
                  if all(q[i] * q[j] >= 14 for i, j in combinations(range(4), 2))]
    require(len(candidates) == 19, "19 alphabet profiles before moment exclusion")
    rejected = {}
    retained = set()
    for q in candidates:
        s1, s2 = moments(q)
        defect = 66 - 2 * s1 + s2
        if defect < 0:
            rejected[q] = defect
        else:
            retained.add(q)
            require(moment_solutions(q), "retained profile has a moment count vector")
    expected_rejected = {
        (3, 5, 5, 5): -2, (3, 5, 5, 6): -1,
        (4, 4, 4, 4): -2, (4, 4, 4, 5): -2,
        (4, 4, 4, 6): -2, (4, 4, 5, 5): -1,
    }
    expected_retained = {
        (3, 5, 6, 6), (3, 6, 6, 6), (4, 4, 5, 6), (4, 4, 6, 6),
        (4, 5, 5, 5), (4, 5, 5, 6), (4, 5, 6, 6), (4, 6, 6, 6),
        (5, 5, 5, 5), (5, 5, 5, 6), (5, 5, 6, 6), (5, 6, 6, 6),
        (6, 6, 6, 6),
    }
    require(rejected == expected_rejected and retained == expected_retained,
            "exact six excluded and thirteen necessary profiles")
    special = {
        (3, 5, 6, 6): ((64, 63), (0, 0, 3, 18, 1)),
        (3, 6, 6, 6): ((70, 78), (0, 0, 0, 18, 4)),
        (4, 4, 5, 6): ((58, 50), (0, 0, 8, 14, 0)),
    }
    for q, (expected_moments, expected_counts) in special.items():
        require(moments(q) == expected_moments, "special profile moments")
        require(moment_solutions(q) == {expected_counts}, "special k-count uniqueness")

    require(degree_vectors(3, 5) == {(4, 5, 5)}, "3566 three-symbol degrees")
    require(degree_vectors(5, 3) == {(2, 3, 3, 3, 3)}, "3566 five-symbol degrees")
    require(degree_vectors(6, 3) == {(2, 2, 2, 2, 3, 3)}, "six-symbol degrees")
    require(degree_vectors(3, 6) == {(2, 6, 6), (3, 5, 6),
                                     (4, 4, 6), (4, 5, 5)},
            "3666 three-symbol degrees")
    require(degree_vectors(4, 4) == {(2, 4, 4, 4), (3, 3, 4, 4)},
            "4456 four-symbol degrees")
    require(degree_vectors(5, 4) == {(2, 2, 2, 4, 4), (2, 2, 3, 3, 4),
                                     (2, 3, 3, 3, 3)},
            "4456 five-symbol degrees")
    # In 4456, n_2+n_3=22; a P word covers at most two of the five
    # outside-alphabet incidences at a fixed symbol of the full party.
    # That symbol occurs in 6-d P words, hence 2*(6-d) >= 5.
    outside = (6 - 4) + (6 - 4) + (6 - 5)
    allowed = tuple(d for d in range(2, 5) if 2 * (6 - d) >= outside)
    require(outside == 5 and allowed == (2, 3), "4456 full-party degree bound")
    require(degree_vectors(6, max(allowed)) == {(2, 2, 2, 2, 3, 3)},
            "4456 full-party degrees")

    # Each mutant is required to pass other displayed filters and fail for
    # exactly the named intended reason; none is evidence of realizability.
    require(n_errors((3, 5, 6, 6), (0, 0, 2, 20, 0)) == {"second_moment"},
            "wrong second-moment mutant intended reason")
    require(n_errors((3, 5, 6, 6), (0, 1, 0, 21, 0)) ==
            {"full_alphabet_lower_k"}, "full-alphabet mutant intended reason")
    require(degree_errors((3, 5, 6), 3, 5) == {"degree_max"},
            "partner-alphabet degree mutant intended reason")
    unrefined = (2, 2, 2, 2, 2, 4)
    require(not degree_errors(unrefined, 6, 4) and
            degree_errors(unrefined, 6, 3) == {"degree_max"},
            "4456 outside-incidence degree mutant intended reason")
    require((4, 4, 4, 4) in rejected and rejected[(4, 4, 4, 4)] == -2,
            "negative-defect profile mutant intended reason")
    return {"capacity_profiles": len(candidates), "moment_exclusions": len(rejected),
            "necessary_profiles": len(retained),
            "special_profiles": ["3566", "3666", "4456"],
            "mutants": ["second_moment", "full_alphabet_lower_k", "degree_max",
                        "4456_outside_incidence", "negative_defect"]}


def main():
    result = {"scope": "local exact checks only; no P completion or global witness",
              "gadget": check_gadget(),
              "even_square_dependency": check_even_dependency(),
              "profile_arithmetic": check_profiles()}
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
