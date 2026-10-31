#!/usr/bin/env python3
"""Unexecuted, definition-first finite checks for the two frozen source images.

No files, subprocesses or network. Stdout is the sole output. This program is
intended for a separate parent static read, admission decision, and one shot.
A cooperative deadline reports INCOMPLETE, never a mathematical verdict.
"""
import json
import time


DEADLINE = time.monotonic() + 45.0


class CheckFailure(Exception):
    pass


class Deadline(Exception):
    pass


def tick():
    if time.monotonic() >= DEADLINE:
        raise Deadline()


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def expected_failure(name, reason, function):
    try:
        function()
    except CheckFailure as error:
        need(str(error) == reason, "control:wrong-reason:" + name + ":" + str(error))
        return {"mutant": name, "rejected_for": reason}
    raise CheckFailure("control:not-rejected:" + name)


class Band:
    def __init__(self, names, table, tau):
        self.names = tuple(names)
        self.index = {name: i for i, name in enumerate(self.names)}
        self.table = tuple(tuple(row) for row in table)
        self.tau = tuple(tau)

    def mul(self, left, right):
        return self.table[left][right]

    def act(self, grade, item):
        return self.tau[item] if grade else item

    def rows(self):
        return [[self.names[v] for v in row] for row in self.table]


def check_involution(band):
    n = len(band.names)
    need(len(band.tau) == n and all(0 <= x < n for x in band.tau),
         "involution:carrier")
    for a in range(n):
        need(band.tau[band.tau[a]] == a, "involution:order2")
        for b in range(n):
            need(band.tau[band.mul(a, b)] == band.mul(band.tau[a], band.tau[b]),
                 "involution:homomorphism")


def check_band(band):
    n = len(band.names)
    need(len(band.index) == n and len(band.table) == n, "band:carrier")
    need(all(len(row) == n and all(0 <= x < n for x in row)
             for row in band.table), "band:closure")
    for a in range(n):
        tick()
        need(band.mul(a, a) == a, "band:idempotence")
        for b in range(n):
            for c in range(n):
                need(band.mul(band.mul(a, b), c) == band.mul(a, band.mul(b, c)),
                     "band:associativity")
    check_involution(band)


TRANS_NAMES = ("I", "E", "F", "G", "A", "Z")
STATE_NAMES = ("p0", "pE", "pF", "acc", "rej")
TRANS = (
    (0, 1, 2, 3, 4),
    (1, 1, 1, 3, 4),
    (2, 2, 2, 3, 4),
    (4, 3, 4, 3, 4),
    (3, 3, 3, 3, 4),
    (4, 4, 4, 3, 4),
)
EXPECTED_TRANS_TABLE = (
    (0, 1, 2, 3, 4, 5),
    (1, 1, 2, 4, 4, 5),
    (2, 1, 2, 5, 4, 5),
    (3, 3, 3, 3, 3, 3),
    (4, 4, 4, 4, 4, 4),
    (5, 5, 5, 5, 5, 5),
)


def transformation_table(reverse=False):
    lookup = {v: i for i, v in enumerate(TRANS)}
    need(len(lookup) == 6, "transform:distinct")
    rows = []
    for left in TRANS:
        row = []
        for right in TRANS:
            composed = (tuple(left[right[i]] for i in range(5)) if reverse
                        else tuple(right[left[i]] for i in range(5)))
            need(composed in lookup, "transform:closure")
            row.append(lookup[composed])
        rows.append(tuple(row))
    return tuple(rows)


def check_transformation_table(table):
    need(table == EXPECTED_TRANS_TABLE, "transform:composition")


def build_transform_band():
    table = transformation_table()
    check_transformation_table(table)
    band = Band(TRANS_NAMES, table, range(6))
    check_band(band)
    return band


D_NAMES = ("0", "x", "y", "xy", "yx", "xyx", "yxy")
D_EXPECTED_ROWS = (
    ("0", "0", "0", "0", "0", "0", "0"),
    ("0", "x", "xy", "xy", "xyx", "xyx", "xy"),
    ("0", "yx", "y", "yxy", "yx", "yx", "yxy"),
    ("0", "xyx", "xy", "xy", "xyx", "xyx", "xy"),
    ("0", "yx", "yxy", "yxy", "yx", "yx", "yxy"),
    ("0", "xyx", "xy", "xy", "xyx", "xyx", "xy"),
    ("0", "yx", "yxy", "yxy", "yx", "yx", "yxy"),
)


def normal_word(word):
    need(bool(word) and all(c in "xy" for c in word), "freeband:word")
    reduced = []
    for char in word:
        if not reduced or reduced[-1] != char:
            reduced.append(char)
    if len(reduced) > 3:
        reduced = reduced[:2 if len(reduced) % 2 == 0 else 3]
    return "".join(reduced)


def signature(word):
    return (frozenset(word), word[0], word[-1])


def build_free_two_band():
    index = {name: i for i, name in enumerate(D_NAMES)}
    rows = []
    for left in D_NAMES:
        row = []
        for right in D_NAMES:
            value = "0" if "0" in (left, right) else normal_word(left + right)
            need(value in index, "freeband:closure")
            row.append(index[value])
        rows.append(row)
    swap = str.maketrans("xy", "yx")
    tau = [index[name if name == "0" else name.translate(swap)] for name in D_NAMES]
    band = Band(D_NAMES, rows, tau)
    need(tuple(tuple(band.names[v] for v in row) for row in band.table) == D_EXPECTED_ROWS,
         "freeband:table")
    words = D_NAMES[1:]
    need(len({signature(w) for w in words}) == 6, "freeband:distinct-signatures")
    for u in words:
        need(normal_word(u) == u, "freeband:normal")
        for v in words:
            actual = band.names[band.mul(index[u], index[v])]
            expected = (frozenset(u) | frozenset(v), u[0], v[-1])
            need(signature(actual) == expected, "freeband:signature-product")
    check_band(band)
    return band


class Host:
    def __init__(self, band, base):
        self.band = band
        self.letters = {}
        for name in ("a", "b", "e", "f", "g"):
            self.letters[name + "0"] = band.index[base[name]]
            self.letters[name + "1"] = band.tau[self.letters[name + "0"]]
        self.generators = {
            "a": (self.letters["a0"], 1),
            "ap": (self.letters["a1"], 1),
            "b": (self.letters["b0"], 1),
            "bp": (self.letters["b1"], 1),
            "e": (self.letters["e0"], 0),
            "f": (self.letters["f0"], 0),
            "g": (self.letters["g0"], 0),
        }
        self.elements = self.generated_image()
        self.position = {x: i for i, x in enumerate(self.elements)}

    def mul(self, left, right):
        return (self.band.mul(left[0], self.band.act(left[1], right[0])),
                left[1] ^ right[1])

    def generated_image(self):
        image = set(self.generators.values())
        while True:
            tick()
            current = tuple(image)
            products = {self.mul(x, y) for x in current for y in current}
            if products <= image:
                return tuple(sorted(image))
            image.update(products)

    def word(self, symbols):
        need(bool(symbols), "word:empty")
        value = self.generators[symbols[0]]
        for symbol in symbols[1:]:
            value = self.mul(value, self.generators[symbol])
        return value

    def label(self, element):
        return self.band.names[element[0]] + "@" + str(element[1])

    def table_rows(self):
        return [[self.label(self.mul(x, y)) for y in self.elements] for x in self.elements]


RELATIONS = (
    ("R1", ("e", "a", "ap"), ("e",)),
    ("R2", ("e", "b", "bp"), ("e",)),
    ("R3", ("ap", "a", "f", "g"), ("f", "g")),
    ("R4", ("bp", "b", "f", "ap", "e", "a", "f", "g"),
     ("f", "ap", "e", "a", "f", "g")),
)
U = ("e", "a", "f", "g")
V = ("e", "b", "f", "ap", "e", "a", "f", "g")


def relation_pairs(model):
    return [(name, model.word(left), model.word(right)) for name, left, right in RELATIONS]


def require_relations(model):
    for name, left, right in relation_pairs(model):
        need(left[1] == 0 and right[1] == 0, "relation:grade:" + name)
        need(left == right, "relation:" + name)


def check_grade(model, grade):
    elements = model.elements
    for x in elements:
        tick()
        for y in elements:
            need(grade(model.mul(x, y)) == (grade(x) ^ grade(y)),
                 "grade:homomorphism")
    need({grade(x) for x in elements} == {0, 1}, "grade:onto")
    for x in elements:
        need((grade(x) == 0) == (model.mul(x, x) == x), "grade:purity")


def check_image(model):
    band = model.band
    elements = model.elements
    expected = {(a, h) for a in range(len(band.names)) for h in (0, 1)}
    need(set(elements) == expected, "source:generated-image-onto-host")
    for name in ("a", "b", "e", "f", "g"):
        need(model.letters[name + "1"] == band.tau[model.letters[name + "0"]],
             "source:letter-equivariance")
    inverses = {}
    for x in elements:
        tick()
        for y in elements:
            need(model.mul(x, y) in model.position, "source:closure")
            for z in elements:
                need(model.mul(model.mul(x, y), z) == model.mul(x, model.mul(y, z)),
                     "source:associativity")
        inverse = next((y for y in elements
                        if model.mul(model.mul(x, y), x) == x
                        and model.mul(model.mul(y, x), y) == y), None)
        need(inverse is not None, "source:regular-inverse")
        inverses[model.label(x)] = model.label(inverse)
    check_grade(model, lambda x: x[1])
    require_relations(model)
    return inverses


def require_uv(model, expect_equal):
    left, right = model.word(U), model.word(V)
    need(left[1] == 1 and right[1] == 1, "uv:grade")
    need((left == right) == expect_equal, "uv:expectation")
    return left, right


def check_typed(model, wrong_shift=False):
    band = model.band
    for s in model.elements:
        tick()
        for t in model.elements:
            for h in (0, 1):
                lhs = band.act(h, model.mul(s, t)[0])
                shifted = h if wrong_shift else h ^ s[1]
                rhs = band.mul(band.act(h, s[0]), band.act(shifted, t[0]))
                need(lhs == rhs, "typed:cocycle")
    for word in (U, V):
        for h in (0, 1):
            index, product = h, None
            for symbol in word:
                source = model.generators[symbol]
                letter = band.act(index, source[0])
                product = letter if product is None else band.mul(product, letter)
                index ^= source[1]
            source_product = model.word(word)
            need(product == band.act(h, source_product[0]), "typed:word")
            need(index == (h ^ source_product[1]), "typed:word-grade")


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        self.parent[y] = x
        return True


def seed_congruence(model):
    uf = UnionFind(len(model.elements))
    for _, left, right in relation_pairs(model):
        uf.union(model.position[left], model.position[right])
    return uf


def check_congruence(model, uf):
    elements, pos = model.elements, model.position
    for i, x in enumerate(elements):
        tick()
        for j, y in enumerate(elements):
            if uf.find(i) != uf.find(j):
                continue
            for z in elements:
                need(uf.find(pos[model.mul(x, z)]) == uf.find(pos[model.mul(y, z)]),
                     "congruence:context")
                need(uf.find(pos[model.mul(z, x)]) == uf.find(pos[model.mul(z, y)]),
                     "congruence:context")


def least_congruence(model):
    elements, pos = model.elements, model.position
    uf = seed_congruence(model)
    changed = True
    while changed:
        tick()
        changed = False
        for i, x in enumerate(elements):
            for j in range(i + 1, len(elements)):
                if uf.find(i) != uf.find(j):
                    continue
                y = elements[j]
                for z in elements:
                    changed |= uf.union(pos[model.mul(x, z)], pos[model.mul(y, z)])
                    changed |= uf.union(pos[model.mul(z, x)], pos[model.mul(z, y)])
    check_congruence(model, uf)
    return uf


def quotient(model, uf):
    groups = {}
    for i in range(len(model.elements)):
        groups.setdefault(uf.find(i), []).append(i)
    classes = sorted(groups.values(), key=lambda group: group[0])
    owner = {i: k for k, group in enumerate(classes) for i in group}
    grades = []
    for group in classes:
        g = model.elements[group[0]][1]
        need(all(model.elements[i][1] == g for i in group), "congruence:grade")
        grades.append(g)
    table = []
    for left in classes:
        row = []
        for right in classes:
            a, b = model.elements[left[0]], model.elements[right[0]]
            row.append(owner[model.position[model.mul(a, b)]])
        table.append(row)
    n = len(classes)
    for a in range(n):
        tick()
        need((table[a][a] == a) == (grades[a] == 0), "quotient:purity")
        need(any(table[table[a][b]][a] == a and table[table[b][a]][b] == b
                 for b in range(n)), "quotient:inverse")
        for b in range(n):
            need(grades[table[a][b]] == (grades[a] ^ grades[b]), "quotient:grade")
            for c in range(n):
                need(table[table[a][b]][c] == table[a][table[b][c]],
                     "quotient:associativity")
    need(set(grades) == {0, 1}, "quotient:onto")
    return classes, owner, grades, table


def check_cr_h(model):
    elements = model.elements
    for x in elements:
        square = model.mul(x, x)
        need(model.mul(square, square) == square, "cr:square-idempotent")
        need(model.mul(square, x) == x and model.mul(x, square) == x, "cr:cube")
    right = {x: frozenset([x] + [model.mul(x, z) for z in elements]) for x in elements}
    left = {x: frozenset([x] + [model.mul(z, x) for z in elements]) for x in elements}

    def related(x, y):
        return right[x] == right[y] and left[x] == left[y]

    for x in elements:
        tick()
        for y in elements:
            need(related(x, y) == (x[0] == y[0]), "green:H-classes")
            if related(x, y):
                for z in elements:
                    need(related(model.mul(x, z), model.mul(y, z)), "green:H-right")
                    need(related(model.mul(z, x), model.mul(z, y)), "green:H-left")
            xy = model.mul(x, y)
            need(model.mul(xy, xy) == model.mul(model.mul(x, x), model.mul(y, y)),
                 "square:homomorphism")
    return [[model.label(x) for x in elements if related(x, y)]
            for y in elements if y[1] == 0]


def model_report(model, inverses):
    band = model.band
    relations = {name: {"left": model.label(left), "right": model.label(right)}
                 for name, left, right in relation_pairs(model)}
    u, v = require_uv(model, True)
    return {
        "band_carrier": list(band.names),
        "band_table_row_and_column_order": list(band.names),
        "band_table": band.rows(),
        "band_involution": {name: band.names[band.tau[i]] for i, name in enumerate(band.names)},
        "original_letter_map": {name: band.names[value] for name, value in model.letters.items()},
        "seven_generators": {name: model.label(value) for name, value in model.generators.items()},
        "source_carrier_and_table_order": [model.label(x) for x in model.elements],
        "source_multiplication_table": model.table_rows(),
        "grade": {model.label(x): x[1] for x in model.elements},
        "regular_inverses": inverses,
        "relations": relations,
        "U": model.label(u), "V": model.label(v),
        "counts": {"band_assoc": len(band.names) ** 3,
                   "band_idempotence": len(band.names),
                   "source_assoc": len(model.elements) ** 3,
                   "grade_homomorphism_pairs": len(model.elements) ** 2,
                   "typed_cocycle_triples": 2 * len(model.elements) ** 2},
    }


def main():
    b = build_transform_band()
    d = build_free_two_band()
    m_b = Host(b, {"a": "I", "b": "I", "e": "E", "f": "F", "g": "G"})
    m_d = Host(d, {"a": "x", "b": "x", "e": "0", "f": "0", "g": "0"})
    inv_b = check_image(m_b)
    inv_d = check_image(m_d)
    check_typed(m_b)
    check_typed(m_d)
    need(tuple(map(m_b.label, require_uv(m_b, True))) == ("Z@1", "Z@1"), "uv:B-values")
    need(tuple(map(m_d.label, require_uv(m_d, True))) == ("0@1", "0@1"), "uv:D-values")

    rb_left = m_b.word(("e", "f", "e", "g", "e"))
    rb_right = m_b.word(("e", "f", "g", "e"))
    need((m_b.label(rb_left), m_b.label(rb_right)) == ("A@0", "Z@0"), "band:RB-witness")
    a, ap = m_d.generators["a"], m_d.generators["ap"]
    cube = m_d.mul(m_d.mul(a, a), a)
    need(m_d.label(a) == "x@1" and m_d.label(cube) == "xyx@1" and cube != a,
         "source:cube-witness")
    st = m_d.mul(a, ap)
    square_st = m_d.mul(st, st)
    product_squares = m_d.mul(m_d.mul(a, a), m_d.mul(ap, ap))
    need((m_d.label(square_st), m_d.label(product_squares)) == ("x@0", "xyx@0"),
         "square:outside-class-witness")
    h_classes = check_cr_h(m_b)

    for model in (m_b, m_d):
        uf = least_congruence(model)
        classes, _, _, _ = quotient(model, uf)
        need(len(classes) == len(model.elements), "congruence:positive-not-identity")

    controls = []
    controls.append(expected_failure("reversed transformation order", "transform:composition",
                                     lambda: check_transformation_table(transformation_table(True))))
    controls.append(expected_failure("flipped actual grade", "grade:homomorphism",
                                     lambda: check_grade(m_b, lambda x: x[1] ^ 1)))
    bad_tau = list(d.tau)
    bad_tau[d.index["y"]] = d.index["y"]
    bad_band = Band(d.names, d.table, bad_tau)
    controls.append(expected_failure("non-involutive letter action", "involution:order2",
                                     lambda: check_involution(bad_band)))
    bad_model = Host(b, {"a": "F", "b": "I", "e": "E", "f": "F", "g": "G"})
    need(set(bad_model.elements) == {(i, h) for i in range(6) for h in (0, 1)},
         "control:actual-image")
    controls.append(expected_failure("physical R1 failure", "relation:R1",
                                     lambda: require_relations(bad_model)))
    seed = seed_congruence(bad_model)
    e0, f0, g0 = ((b.index[name], 0) for name in ("E", "F", "G"))
    a0, z0 = ((b.index[name], 0) for name in ("A", "Z"))
    need(seed.find(bad_model.position[e0]) == seed.find(bad_model.position[f0]),
         "control:physical-seed")
    need(bad_model.mul(e0, g0) == a0 and bad_model.mul(f0, g0) == z0,
         "control:physical-context")
    need(seed.find(bad_model.position[a0]) != seed.find(bad_model.position[z0]),
         "control:seed-not-already-closed")
    controls.append(expected_failure("omit physical semigroup contexts", "congruence:context",
                                     lambda: check_congruence(bad_model, seed)))
    closed = least_congruence(bad_model)
    need(closed.find(bad_model.position[a0]) == closed.find(bad_model.position[z0]),
         "congruence:missing-right-context")
    qclasses, qowner, qgrades, qtable = quotient(bad_model, closed)
    need(len(qclasses) == 8, "congruence:physical-quotient-size")
    require_uv(bad_model, True)
    qu = qowner[bad_model.position[bad_model.word(U)]]
    qv = qowner[bad_model.position[bad_model.word(V)]]
    need(qu == qv, "congruence:UV")
    controls.append(expected_failure("unshifted typed cocycle", "typed:cocycle",
                                     lambda: check_typed(m_d, True)))
    for name, model in (("B", m_b), ("D", m_d)):
        controls.append(expected_failure("false separation expectation " + name, "uv:expectation",
                                         lambda model=model: require_uv(model, False)))

    result = {
        "status": "PASS_SCOPED_IF_RUN_TO_COMPLETION",
        "scope": "Two actual source images and one physical congruence control; neither image separates U,V. No SEP decision or all-host conclusion.",
        "transform_states": list(STATE_NAMES),
        "transform_maps": {name: [STATE_NAMES[i] for i in image]
                           for name, image in zip(TRANS_NAMES, TRANS)},
        "composition": "left factor first, then right factor",
        "B_cross_C2": model_report(m_b, inv_b),
        "D_semidirect_C2": model_report(m_d, inv_d),
        "identity_boundaries": {
            "B_EFEGE": m_b.label(rb_left), "B_EFGE": m_b.label(rb_right),
            "B_CR_and_actual_Green_H_congruence": True,
            "B_actual_H_classes": h_classes,
            "B_square_identity_checked_for_all_ordered_pairs": len(m_b.elements) ** 2,
            "D_a": m_d.label(a), "D_a_cubed": m_d.label(cube),
            "D_square_of_a_ap": m_d.label(square_st),
            "D_a_square_times_ap_square": m_d.label(product_squares),
            "D_outside_CR_class_not_a_separator": True,
        },
        "physical_context_control": {
            "actual_letter_map": {name: b.names[value] for name, value in bad_model.letters.items()},
            "actual_seven_generators": {name: bad_model.label(value) for name, value in bad_model.generators.items()},
            "source_carrier_and_table_order": [bad_model.label(x) for x in bad_model.elements],
            "source_table": bad_model.table_rows(),
            "four_relation_pairs_before_quotient": {name: [bad_model.label(left), bad_model.label(right)]
                                                     for name, left, right in relation_pairs(bad_model)},
            "right_context": "E@0 ~ F@0; multiplying by G@0 forces A@0 ~ Z@0",
            "quotient_classes": [[bad_model.label(bad_model.elements[i]) for i in group] for group in qclasses],
            "quotient_grade_by_class_index": qgrades,
            "quotient_table_by_class_index": qtable,
            "quotient_U_class": qu, "quotient_V_class": qv,
        },
        "negative_controls": controls,
        "limits": "Free-band theory on the original ten letters and universal COLL are imported written interfaces, not checked by this finite program. No kernel, external theorem, novelty, family or human acceptance.",
    }
    tick()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Deadline:
        print(json.dumps({"status": "INCOMPLETE", "reason": "cooperative 45-second deadline"}))
        raise SystemExit(1)
    except CheckFailure as error:
        print(json.dumps({"status": "FAIL", "reason": str(error)}))
        raise SystemExit(1)
