#!/usr/bin/env python3
"""Fixed, bounded trace checker for one source equality; not a band word solver.

No file, network, subprocess, package, input, or deletion operations. The child
who authored this source did not execute it. A parent may statically inspect it
and, if authorized, run it once with an external 55-second limit.
"""

import time

START = time.monotonic()
DEADLINE_SECONDS = 45.0


class Reject(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def fail(code):
    raise Reject(code)


def tick():
    if time.monotonic() - START >= DEADLINE_SECONDS:
        fail("DEADLINE")


def require(condition, code):
    if not condition:
        fail(code)


TAU = {
    "a0": "a1", "a1": "a0", "b0": "b1", "b1": "b0",
    "e0": "e1", "e1": "e0", "f0": "f1", "f1": "f0",
    "g0": "g1", "g1": "g0",
}
GEN = {
    "a": (("a0",), 1), "a'": (("a1",), 1),
    "b": (("b0",), 1), "b'": (("b1",), 1),
    "e": (("e0",), 0), "f": (("f0",), 0),
    "g": (("g0",), 0),
}
BAND_ALPHABET = frozenset(TAU)
SOURCE_ALPHABET = frozenset(GEN)

# All words are tuples of indivisible, explicitly subscripted symbols.
I1_LEFT = ("a", "a'", "b")
I1_RIGHT = ("a", "b'", "b")
I2_LEFT = ("e", "a", "f", "a'", "e", "a", "f")
I2_RIGHT = ("e", "a", "f")
W = ("f", "a'", "e", "a", "f", "g")
BW = ("b", "f", "a'", "e", "a", "f", "g")
V = ("e", "b", "f", "a'", "e", "a", "f", "g")
P = ("e", "a", "a'", "b", "f", "a'", "e", "a", "f", "g")
Q = ("e", "a", "b'", "b", "f", "a'", "e", "a", "f", "g")
R = ("e", "a", "f", "a'", "e", "a", "f", "g")
U = ("e", "a", "f", "g")

# Raw semidirect coordinates, BEFORE any band-word square replacement.
SOURCE_COORDINATES = (
    ("V", V, ("e0", "b0", "f1", "a0", "e0", "a0", "f1", "g1"), 1),
    ("P", P, ("e0", "a0", "a0", "b0", "f1", "a0", "e0", "a0", "f1", "g1"), 1),
    ("Q", Q, ("e0", "a0", "b0", "b0", "f1", "a0", "e0", "a0", "f1", "g1"), 1),
    ("R", R, ("e0", "a0", "f1", "a0", "e0", "a0", "f1", "g1"), 1),
    ("U", U, ("e0", "a0", "f1", "g1"), 1),
)


def check_tau(tau):
    expected = {}
    for letter in ("a", "b", "e", "f", "g"):
        expected[letter + "0"] = letter + "1"
        expected[letter + "1"] = letter + "0"
    require(tau == expected, "TAU")
    for symbol in expected:
        require(tau[tau[symbol]] == symbol, "TAU_INVOLUTION")


def check_definitions():
    expected = {
        "a": (("a0",), 1), "a'": (("a1",), 1),
        "b": (("b0",), 1), "b'": (("b1",), 1),
        "e": (("e0",), 0), "f": (("f0",), 0),
        "g": (("g0",), 0),
    }
    require(GEN == expected, "GENERATOR_DEFINITION")
    check_tau(TAU)


def source_word(word):
    require(bool(word), "EMPTY_SOURCE_WORD")
    require(all(s in SOURCE_ALPHABET for s in word), "NON_SOURCE_LETTER")


def coordinate(word, tau=TAU, generators=GEN):
    source_word(word)
    raw = []
    grade = 0
    for symbol in word:
        tick()
        band_word, h = generators[symbol]
        require(h in (0, 1), "GENERATOR_GRADE")
        for letter in band_word:
            raw.append(tau[letter] if grade else letter)
        grade ^= h
    return tuple(raw), grade


def check_coordinate(word, expected_raw, expected_grade, tau=TAU, generators=GEN):
    actual_raw, actual_grade = coordinate(word, tau, generators)
    require(actual_grade == expected_grade, "GRADE")
    require(actual_raw == expected_raw, "COORDINATE")
    return actual_raw, actual_grade


def typed_path(word, start):
    source_word(word)
    require(start in (0, 1), "PATH_START")
    h = start
    path = []
    for symbol in word:
        path.append((h, symbol))
        h ^= GEN[symbol][1]
    return tuple(path)


def check_composable(path, start):
    require(start in (0, 1), "PATH_START")
    h = start
    for index, symbol in path:
        tick()
        require(symbol in SOURCE_ALPHABET, "NON_SOURCE_LETTER")
        require(index == h, "NONCOMPOSABLE")
        h ^= GEN[symbol][1]
    return h


def square_move(name, before, after, pos, left, block, right, direction):
    return {"name": name, "before": before, "after": after, "pos": pos,
            "left": left, "block": block, "right": right,
            "direction": direction}


T0 = ("e0", "a0", "f1", "a0", "e0", "a0", "f1")
T1 = ("e0", "a0", "f1", "a0", "e0", "a0", "f1", "a0", "f1")
T2 = ("e0", "a0", "f1", "a0", "f1")
T3 = ("e0", "a0", "f1")
SQUARES = (
    square_move("I1-left", ("a0", "a0", "b0"), ("a0", "b0"),
                0, (), ("a0",), ("b0",), "contract"),
    square_move("I1-right", ("a0", "b0", "b0"), ("a0", "b0"),
                1, ("a0",), ("b0",), (), "contract"),
    square_move("I2-expand-yz", T0, T1, 5,
                ("e0", "a0", "f1", "a0", "e0"), ("a0", "f1"), (), "expand"),
    square_move("I2-contract-xyzy", T1, T2, 0,
                (), ("e0", "a0", "f1", "a0"), ("f1",), "contract"),
    square_move("I2-contract-yz", T2, T3, 1,
                ("e0",), ("a0", "f1"), (), "contract"),
)


def check_square(move, generator_only=False):
    tick()
    before, after = move["before"], move["after"]
    left, block, right = move["left"], move["block"], move["right"]
    require(bool(block), "EMPTY_SQUARE")
    require(all(x in BAND_ALPHABET for x in before + after + left + block + right),
            "NON_BAND_LETTER")
    require(move["pos"] == len(left), "SQUARE_LOCUS")
    if generator_only and len(block) != 1:
        fail("GENERATOR_ONLY")
    if move["direction"] == "expand":
        old, new = block, block + block
    elif move["direction"] == "contract":
        old, new = block + block, block
    else:
        fail("SQUARE_DIRECTION")
    require(before == left + old + right, "SQUARE_LOCUS")
    require(after == left + new + right, "SQUARE_RESULT")


# R1/R4 are the actual source pairs, not relations on ambient band letters.
# I1/I2 may be used only after the explicit semidirect/square checks below.
RULES = {
    "R1": (("e", "a", "a'"), ("e",)),
    "R4": (("b'", "b", "f", "a'", "e", "a", "f", "g"), W),
    "I1": (I1_LEFT, I1_RIGHT),
    "I2": (I2_LEFT, I2_RIGHT),
}


def source_move(name, rule, reverse, before, after, pos, left, right):
    return {"name": name, "rule": rule, "reverse": reverse,
            "before": before, "after": after, "pos": pos,
            "left": left, "right": right}


STEPS = (
    source_move("R1-right-context", "R1", True, V, P, 0, (), BW),
    source_move("I1-source-context", "I1", False, P, Q, 1, ("e",), W),
    source_move("R4-left-context", "R4", False, Q, R, 2, ("e", "a"), ()),
    source_move("I2-right-context", "I2", False, R, U, 0, (), ("g",)),
)


def check_source_step(step):
    tick()
    require(step["rule"] in RULES, "UNKNOWN_RULE")
    require(type(step["reverse"]) is bool, "RULE_DIRECTION")
    lhs, rhs = RULES[step["rule"]]
    if step["reverse"]:
        lhs, rhs = rhs, lhs
    left, right = step["left"], step["right"]
    require(step["pos"] == len(left), "SOURCE_LOCUS")
    source_word(step["before"])
    source_word(step["after"])
    source_word(lhs)
    source_word(rhs)
    require(all(s in SOURCE_ALPHABET for s in left + right), "NON_SOURCE_LETTER")
    require(step["before"] == left + lhs + right, "SOURCE_CONTEXT")
    require(step["after"] == left + rhs + right, "SOURCE_CONTEXT")
    require(coordinate(lhs)[1] == coordinate(rhs)[1], "RULE_GRADE")
    require(coordinate(step["before"])[1] == coordinate(step["after"])[1],
            "CONTEXT_GRADE")
    for word in (step["before"], step["after"]):
        path = typed_path(word, 0)
        require(check_composable(path, 0) == coordinate(word)[1], "PATH_GRADE")


def show_square(move):
    print("SQUARE", move["name"], move["direction"], "pos", move["pos"],
          "left", move["left"], "block", move["block"], "right", move["right"],
          "before", move["before"], "after", move["after"])


def show_source(move):
    print("SOURCE", move["name"], "rule", move["rule"], "reverse", move["reverse"],
          "pos", move["pos"], "left", move["left"], "right", move["right"],
          "before", move["before"], "after", move["after"])


def check_positive():
    check_definitions()
    require(BW == ("b",) + W, "BW_CONTEXT")
    require(RULES["R4"][0] == ("b'", "b") + W, "R4_DEFINITION")
    require(RULES["R1"] == (("e", "a", "a'"), ("e",)), "R1_DEFINITION")

    left1 = check_coordinate(I1_LEFT, ("a0", "a0", "b0"), 1)[0]
    right1 = check_coordinate(I1_RIGHT, ("a0", "b0", "b0"), 1)[0]
    left2 = check_coordinate(I2_LEFT, T0, 1)[0]
    right2 = check_coordinate(I2_RIGHT, T3, 1)[0]
    require(SQUARES[0]["before"] == left1 and SQUARES[1]["before"] == right1,
            "I1_ENDPOINT")
    require(SQUARES[0]["after"] == SQUARES[1]["after"], "I1_COMMON_WORD")
    require(SQUARES[2]["before"] == left2 and SQUARES[4]["after"] == right2,
            "I2_ENDPOINT")
    require(SQUARES[2]["after"] == SQUARES[3]["before"] and
            SQUARES[3]["after"] == SQUARES[4]["before"], "I2_CHAIN")
    for move in SQUARES:
        check_square(move)
        show_square(move)

    for name, word, raw, grade in SOURCE_COORDINATES:
        actual_raw, actual_grade = check_coordinate(word, raw, grade)
        require(check_composable(typed_path(word, 0), 0) == grade, "PATH_GRADE")
        print("COORDINATE", name, "word", word, "raw", actual_raw, "grade", actual_grade)

    current = V
    for move in STEPS:
        require(move["before"] == current, "SOURCE_CHAIN")
        check_source_step(move)
        show_source(move)
        current = move["after"]
    require(current == U, "SOURCE_ENDPOINT")
    # This flag is returned only after the fixed primitive and source checks.
    return True


def expect_reject(name, action, expected_code):
    try:
        action()
    except Reject as exc:
        require(exc.code == expected_code, "CONTROL_WRONG_REASON:" + name + ":" + exc.code)
        print("CONTROL", name, "REJECTED", exc.code)
        return
    fail("CONTROL_ACCEPTED:" + name)


def scope_guard(claim, source_chain_checked, finite_image_equal):
    # Deliberately conservative: a finite-image coincidence is never source proof.
    if claim == "U_EQ_V":
        require(source_chain_checked, "SOURCE_EVIDENCE_REQUIRED")
        return "EXACT_SOURCE_EQUALITY"
    if claim == "DESIGNATED_SEP_FAILED":
        require(source_chain_checked, "SOURCE_EVIDENCE_REQUIRED")
        return "DESIGNATED_SEP_FAILED"
    if claim == "U_NE_V":
        if source_chain_checked:
            fail("SEP_CONTRADICTS_SOURCE_EQUALITY")
        fail("SEP_NOT_PROVED")
    if claim in ("ALLHOST_EMBEDS", "ALLHOST_NONEMBEDS"):
        fail("ALLHOST_NOT_DECIDED")
    fail("UNKNOWN_SCOPE")


def generator_only_control():
    # Idempotent transformations p and q, applied left factor first, need not
    # have idempotent product. This is not a band and is not a source image.
    p = (0, 0, 2)
    q = (0, 1, 1)
    compose = lambda first, second: tuple(second[first[i]] for i in range(3))
    require(compose(p, p) == p and compose(q, q) == q, "CONTROL_IDEMPOTENTS")
    pq = compose(p, q)
    require(pq == (0, 0, 1), "CONTROL_PRODUCT")
    require(compose(pq, pq) == (0, 0, 0) and compose(pq, pq) != pq,
            "CONTROL_PRODUCT_NOT_IDEMPOTENT")
    print("CONTROL", "GENERATOR_IDEMPOTENCE_NOT_BAND", "p", p, "q", q,
          "pq", pq, "pqpq", compose(pq, pq))


def negative_controls(source_checked):
    bad_tau = dict(TAU)
    bad_tau["a1"] = "a1"
    expect_reject("WRONG_TAU_DEFINITION", lambda: check_tau(bad_tau), "TAU")
    expect_reject("WRONG_TAU_COORDINATE",
                  lambda: check_coordinate(I1_LEFT, ("a0", "a0", "b0"), 1, tau=bad_tau),
                  "COORDINATE")
    bad_gen = dict(GEN)
    bad_gen["a"] = (("a0",), 0)
    expect_reject("WRONG_GENERATOR_GRADE",
                  lambda: check_coordinate(I1_LEFT, ("a0", "a0", "b0"), 1,
                                           generators=bad_gen), "GRADE")
    bad_square = square_move("nonsquare", ("a0", "f1", "a0", "e0"),
                             ("a0", "f1"), 0, (), ("a0", "f1"), (), "contract")
    expect_reject("ILLEGAL_SQUARE", lambda: check_square(bad_square), "SQUARE_LOCUS")
    expect_reject("GENERATOR_ONLY_MISSES_COMPOSITE",
                  lambda: check_square(SQUARES[3], generator_only=True), "GENERATOR_ONLY")
    generator_only_control()

    expect_reject("R1_WRONG_LOCUS", lambda: check_source_step(dict(STEPS[0], pos=1)),
                  "SOURCE_LOCUS")
    expect_reject("R1_WRONG_RIGHT_CONTEXT",
                  lambda: check_source_step(dict(STEPS[0], right=("b",))), "SOURCE_CONTEXT")
    expect_reject("R4_WRONG_LOCUS", lambda: check_source_step(dict(STEPS[2], pos=1)),
                  "SOURCE_LOCUS")
    expect_reject("R4_WRONG_LEFT_CONTEXT",
                  lambda: check_source_step(dict(STEPS[2], left=("e",), pos=1)),
                  "SOURCE_CONTEXT")
    require(check_composable(((1, "a'"), (0, "a'")), 1) == 1, "COMPOSABLE_CONTROL")
    expect_reject("NONCOMPOSABLE_DUPLICATION",
                  lambda: check_composable(((1, "a'"), (1, "a'")), 1), "NONCOMPOSABLE")

    require(scope_guard("U_EQ_V", source_checked, False) == "EXACT_SOURCE_EQUALITY",
            "SOURCE_SCOPE")
    require(scope_guard("DESIGNATED_SEP_FAILED", source_checked, False) ==
            "DESIGNATED_SEP_FAILED", "SEP_SCOPE")
    expect_reject("FINITE_IMAGE_IS_NOT_SOURCE_EQUALITY",
                  lambda: scope_guard("U_EQ_V", False, True), "SOURCE_EVIDENCE_REQUIRED")
    expect_reject("FALSE_DESIGNATED_SEP",
                  lambda: scope_guard("U_NE_V", source_checked, False),
                  "SEP_CONTRADICTS_SOURCE_EQUALITY")
    expect_reject("FALSE_ALLHOST_EMBEDDING_INFERENCE",
                  lambda: scope_guard("ALLHOST_EMBEDS", source_checked, False),
                  "ALLHOST_NOT_DECIDED")
    expect_reject("FALSE_ALLHOST_NONEMBEDDING_INFERENCE",
                  lambda: scope_guard("ALLHOST_NONEMBEDS", source_checked, False),
                  "ALLHOST_NOT_DECIDED")


def main():
    tick()
    source_checked = check_positive()
    negative_controls(source_checked)
    tick()
    print("RESULT EXACT_SOURCE_U_EQ_V; DESIGNATED_SEP_FAILED; ALLHOST_UNDECIDED")
    print("LIMIT fixed-trace replay only; no general word problem or formal kernel")


if __name__ == "__main__":
    try:
        main()
    except Reject as exc:
        print("FAIL", exc.code)
        raise SystemExit(1)
