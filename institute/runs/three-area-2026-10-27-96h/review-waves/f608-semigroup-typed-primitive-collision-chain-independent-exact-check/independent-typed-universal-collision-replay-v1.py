from collections import Counter
from itertools import product
from time import monotonic

class Rejected(Exception):
    pass

def need(condition, reason):
    if not condition:
        raise Rejected(reason)

LIMIT = None

def tick():
    if LIMIT is not None:
        need(monotonic() < LIMIT, "DEADLINE")

Q = dict(a=1, A=1, b=1, B=1, e=0, f=0, g=0)
R = {
    1: ("eaA", "e"),
    2: ("ebB", "e"),
    3: ("Aafg", "fg"),
    4: ("BbfAeafg", "fAeafg"),
}
ALL = frozenset(R)
U = "eafg"
V = "ebfAeafg"
SYMBOL = {
    "X": (0, "e"), "A": (0, "a"), "D": (1, "A"),
    "B": (0, "b"), "J": (1, "B"),
    "P": (1, "f"), "Q": (1, "g"),
}

def parity(s):
    need(type(s) is str and bool(s), "SOURCE_NONEMPTY")
    need(all(c in Q for c in s), "SOURCE_ALPHABET")
    return sum(Q[c] for c in s) % 2

def validate_word(w):
    need(type(w) is tuple and bool(w), "UNIVERSAL_NONEMPTY")
    for token in w:
        need(type(token) is tuple and len(token) == 2, "TOKEN")
        h, s = token
        need(type(h) is int and h in (0, 1), "GROUP_INDEX")
        parity(s)

def spelled(h, s):
    parity(s)
    out = []
    for c in s:
        out.append((h, c))
        h ^= Q[c]
    return tuple(out)

def symbols(s):
    return tuple(SYMBOL[c] for c in s)

def transition(kind, at, n, w, allowed=ALL, singles_only=False):
    tick()
    validate_word(w)
    need(type(at) is int and 0 <= at < len(w), "LOCUS")
    h, s = w[at]
    if kind == "E":
        need(type(n) is int and 0 < n < len(s), "SPLIT_NONEMPTY")
        left, right = s[:n], s[n:]
        middle = ((h, left), (h ^ parity(left), right))
        return w[:at] + middle + w[at + 1:]
    if kind == "C":
        need(at + 1 < len(w), "COCYCLE_PAIR")
        k, t = w[at + 1]
        need(k == (h ^ parity(s)), "COCYCLE_SHIFT")
        need(n == len(s), "CONTRACTION_SPLIT")
        return w[:at] + ((h, s + t),) + w[at + 2:]
    if kind == "N":
        need(n in allowed and n in R, "RELATION_MISSING")
        left, right = R[n]
        need(parity(left) == parity(right), "RELATION_GRADE")
        need(s == left or s == right, "RELATION_SOURCE_NAME")
        target = right if s == left else left
        return w[:at] + ((h, target),) + w[at + 1:]
    need(kind in ("I+", "I-"), "PRIMITIVE_KIND")
    need(type(n) is int and n > 0, "SQUARE_NONEMPTY")
    if singles_only:
        need(n == 1, "GENERATOR_ONLY_SQUARE")
    need(at + n <= len(w), "SQUARE_BLOCK")
    block = w[at:at + n]
    if kind == "I+":
        return w[:at] + block + block + w[at + n:]
    need(at + 2 * n <= len(w), "SQUARE_PAIR")
    need(w[at + n:at + 2 * n] == block, "SQUARE_EQUAL_HALVES")
    return w[:at] + block + w[at + 2 * n:]

TARGET_REASON = {
    "E": "COCYCLE_TARGET", "C": "COCYCLE_TARGET",
    "N": "ALIAS_TARGET",
    "I+": "SQUARE_TARGET", "I-": "SQUARE_TARGET",
}

def verify_event(event, allowed=ALL, singles_only=False):
    kind, at, n, before, after = event
    validate_word(after)
    expected = transition(kind, at, n, before, allowed, singles_only)
    need(expected == after, TARGET_REASON[kind])

def step(log, w, kind, at, n):
    after = transition(kind, at, n, w)
    event = (kind, at, n, w, after)
    verify_event(event)
    log.append(event)
    return after

def inverted(log):
    inverse_kind = {"E": "C", "C": "E", "N": "N",
                    "I+": "I-", "I-": "I+"}
    return [(inverse_kind[k], p, n, after, before)
            for k, p, n, before, after in reversed(log)]

def macro_template(rid, override_start=None):
    h = {1: 0, 2: 0, 3: 1, 4: 1}[rid]
    if override_start is not None:
        h = override_start
    left, right = R[rid]
    w = spelled(h, left)
    log = []
    for unused in range(len(left) - 1):
        w = step(log, w, "C", 0, len(w[0][1]))
    w = step(log, w, "N", 0, rid)
    for cut in range(len(right) - 1, 0, -1):
        w = step(log, w, "E", 0, cut)
    need(w == spelled(h, right), "MACRO_TEMPLATE_END")
    return log

def use_macro(log, w, rid, at, reverse=False, override_start=None):
    template = macro_template(rid, override_start)
    if reverse:
        template = inverted(template)
    first = template[0][3]
    need(0 <= at and w[at:at + len(first)] == first, "MACRO_MATCH")
    prefix, suffix = w[:at], w[at + len(first):]
    for kind, local, n, before, after in template:
        need(w == prefix + before + suffix, "MACRO_CONTEXT")
        event = (kind, at + local, n, w, prefix + after + suffix)
        verify_event(event)
        log.append(event)
        w = event[4]
    return w

U_PLAN = [
    ("H", 3, 2, True), ("I+", 2, 1),
    ("H", 1, 0, False), ("H", 3, 1, False),
]
U_WORDS = ["XAPQ", "XADAPQ", "XADDAPQ", "XDAPQ", "XPQ"]
V_PLAN = [
    ("H", 4, 2, True), ("I+", 2, 1),
    ("H", 2, 0, False), ("H", 4, 1, False),
    ("H", 3, 5, True), ("I+", 5, 1),
    ("H", 1, 3, False), ("H", 3, 4, False),
    ("I+", 4, 1), ("H", 3, 5, True), ("I+", 5, 1),
    ("H", 3, 6, False), ("I-", 0, 3),
    ("H", 3, 3, True), ("I-", 2, 1),
    ("H", 3, 2, False), ("I-", 1, 1),
]
V_WORDS = [
    "XBPDXAPQ", "XBJBPDXAPQ", "XBJJBPDXAPQ", "XJBPDXAPQ",
    "XPDXAPQ", "XPDXADAPQ", "XPDXADDAPQ", "XPDXDAPQ",
    "XPDXPQ", "XPDXPPQ", "XPDXPDAPQ", "XPDXPDDAPQ",
    "XPDXPDPQ", "XPDPQ", "XPDDAPQ", "XPDAPQ", "XPPQ", "XPQ",
]

def branch(source, plan, expected_words):
    need(len(expected_words) == len(plan) + 1, "PLAN_LENGTH")
    w = ((0, source),)
    log = []
    for cut in range(len(source) - 1, 0, -1):
        w = step(log, w, "E", 0, cut)
    need(w == symbols(expected_words[0]), "ENDPOINT_EXPANSION")
    snapshots = [w]
    for instruction, expected in zip(plan, expected_words[1:]):
        if instruction[0] == "H":
            unused, rid, at, reverse = instruction
            w = use_macro(log, w, rid, at, reverse)
        else:
            kind, at, n = instruction
            w = step(log, w, kind, at, n)
        need(w == symbols(expected), "NAMED_MACRO_WORD")
        snapshots.append(w)
    return log, snapshots

def replay(log, start, end, allowed=ALL, singles_only=False):
    w = start
    counts = Counter()
    for event in log:
        need(event[3] == w, "CHAIN_CONTINUITY")
        verify_event(event, allowed, singles_only)
        counts[event[0]] += 1
        w = event[4]
    need(w == end, "CHAIN_ENDPOINT")
    return counts

def require_path(w):
    validate_word(w)
    for (h, s), (k, unused) in zip(w, w[1:]):
        need(k == (h ^ parity(s)), "NOT_SOURCE_PATH")

def conclusion_guard(coll, sep, negative_witness):
    if negative_witness:
        need(coll is True and sep is True, "SEP_UNPROVED")
    return "COLL_ONLY" if coll and sep is not True else "SCOPED"

def reject(label, expected_reason, action):
    try:
        action()
    except Rejected as error:
        need(str(error) == expected_reason, "WRONG_REJECTION:" + label)
        print("CONTROL", label, "REJECTED", expected_reason)
        return
    raise Rejected("MUTANT_ACCEPTED:" + label)

def controls(ulog, us, vs, chain):
    reject("H3_WRONG_START", "MACRO_MATCH",
           lambda: use_macro([], us[0], 3, 2, True, 0))
    reject("H4_WRONG_START", "MACRO_MATCH",
           lambda: use_macro([], vs[0], 4, 2, True, 0))
    kind, at, n, before, after = ulog[0]
    wrong_after = after[:1] + ((0, after[1][1]),) + after[2:]
    wrong_shift = (kind, at, n, before, wrong_after)
    reject("OMITTED_Q_SHIFT", "COCYCLE_TARGET",
           lambda: verify_event(wrong_shift))
    reject("GENERATOR_ONLY_SQUARES", "GENERATOR_ONLY_SQUARE",
           lambda: replay(chain, ((0, U),), ((0, V),),
                          singles_only=True))
    reject("WRONG_MACRO_POSITION", "MACRO_MATCH",
           lambda: use_macro([], us[0], 3, 1, True))
    require_path(us[1])
    reject("DD_SOURCE_COMPOSABLE", "NOT_SOURCE_PATH",
           lambda: require_path(us[2]))
    empty_square = ("I+", 0, 0, ((0, U),), ((0, U),))
    reject("EMPTY_XK", "SQUARE_NONEMPTY",
           lambda: verify_event(empty_square))
    need(vs[12] == symbols("XPDXPDPQ"), "CORRECT_V12")
    reject("WRONG_V12_WORD", "V12_LITERAL",
           lambda: need(vs[12] == symbols("XPDXPPQ"), "V12_LITERAL"))
    reject("MISSING_R4", "RELATION_MISSING",
           lambda: replay(chain, ((0, U),), ((0, V),),
                          allowed=frozenset((1, 2, 3))))
    need(conclusion_guard(True, None, False) == "COLL_ONLY", "SCOPE")
    reject("COLL_AS_NEGATIVE_WITNESS_SCOPE_GUARD", "SEP_UNPROVED",
           lambda: conclusion_guard(True, None, True))

def finite_image():
    carrier = ((0, 0), (0, 1), (1, 0), (1, 1))
    index = {x: i for i, x in enumerate(carrier)}
    def mul(i, j):
        left, h = carrier[i]
        unused, k = carrier[j]
        return index[(left, h ^ k)]
    table = tuple(tuple(mul(i, j) for j in range(4))
                  for i in range(4))
    expected = ((0, 1, 0, 1), (1, 0, 1, 0),
                (2, 3, 2, 3), (3, 2, 3, 2))
    need(table == expected, "IMAGE_TABLE")
    grades = tuple(h for unused, h in carrier)
    for i, j, k in product(range(4), repeat=3):
        tick()
        need(mul(mul(i, j), k) == mul(i, mul(j, k)), "IMAGE_ASSOC")
    for i, j in product(range(4), repeat=2):
        need(grades[mul(i, j)] == (grades[i] ^ grades[j]), "IMAGE_Q")
    for i in range(4):
        inverse = i
        need(mul(mul(i, inverse), i) == i, "IMAGE_INVERSE_LEFT")
        need(mul(mul(inverse, i), inverse) == inverse,
             "IMAGE_INVERSE_RIGHT")
        need((mul(i, i) == i) == (grades[i] == 0), "IMAGE_PURITY")
    need(set(grades) == {0, 1}, "IMAGE_ONTO")
    for h, k, l in product(range(2), repeat=3):
        need(((h ^ k) ^ l) == (h ^ (k ^ l)), "GROUP_ASSOC")
    for h in range(2):
        need((h ^ 0) == h and (0 ^ h) == h and (h ^ h) == 0,
             "GROUP_IDENTITY_INVERSE")
    gen = dict(a=3, A=3, b=3, B=3, e=0, f=2, g=2)
    for c in Q:
        need(grades[gen[c]] == Q[c], "GENERATOR_GRADE")
    def evaluate(s):
        parity(s)
        result = gen[s[0]]
        for c in s[1:]:
            result = mul(result, gen[c])
        return result
    relation_images = []
    for rid, (left, right) in R.items():
        a, b = evaluate(left), evaluate(right)
        need(a == b, "IMAGE_R" + str(rid))
        relation_images.append((rid, a, b))
    generated = set(gen.values())
    while True:
        expanded = generated | {mul(i, j) for i in generated
                                 for j in generated}
        if expanded == generated:
            break
        generated = expanded
    need(generated == set(range(4)), "IMAGE_GENERATED_CARRIER")
    need(evaluate("ef") != evaluate("fe"), "IMAGE_NONCOMMUTING")
    need(evaluate(U) == evaluate(V) == 1, "IMAGE_UV_EQUAL")
    print("IMAGE_TABLE", table)
    print("IMAGE_Q", grades, "INVERSES", tuple(range(4)))
    print("IMAGE_RELATIONS", relation_images)
    print("IMAGE_CHECKS", "64 associativity; 16 q; 4 inverse; 4 purity")
    print("IMAGE_EF_FE", evaluate("ef"), evaluate("fe"))
    print("IMAGE_U_V", evaluate(U), evaluate(V), "NOT_SOURCE_SEP")

def show_source(s):
    return "".join({"A": "a'", "B": "b'"}.get(c, c) for c in s)

def show_word(w):
    return " ".join("(%d,%s)" % (h, show_source(s)) for h, s in w)

def print_chain(chain):
    primitive = 0
    for kind, at, n, before, after in chain:
        if kind == "N":
            label = "NAME R%d (zero primitive steps)" % n
        else:
            primitive += 1
            label = "STEP %02d %s parameter=%d" % (primitive, kind, n)
        print(label, "LOCUS", at)
        print("BEFORE", show_word(before))
        print("AFTER ", show_word(after))
    need(primitive == 80, "PRINTED_PRIMITIVE_COUNT")

def main():
    global LIMIT
    LIMIT = monotonic() + 55.0
    ulog, us = branch(U, U_PLAN, U_WORDS)
    vlog, vs = branch(V, V_PLAN, V_WORDS)
    common = symbols("XPQ")
    uc = replay(ulog, ((0, U),), common)
    vc = replay(vlog, ((0, V),), common)
    need(uc == Counter({"C": 6, "E": 7, "I+": 1, "N": 3}),
         "U_COUNTS")
    need(vc == Counter({"C": 28, "E": 31, "I+": 4, "I-": 3, "N": 10}),
         "V_COUNTS")
    chain = ulog + inverted(vlog)
    counts = replay(chain, ((0, U),), ((0, V),))
    need(counts == Counter({"C": 37, "E": 35, "I+": 4, "I-": 4, "N": 13}),
         "FULL_COUNTS")
    controls(ulog, us, vs, chain)
    finite_image()
    print_chain(chain)
    tick()
    print("COUNTS_U", dict(uc))
    print("COUNTS_V", dict(vc))
    print("COUNTS_FULL", dict(counts))
    print("RESULT COLL_FINITE_WORD_REPLAY; SEP_UNKNOWN; NO_NEGATIVE_WITNESS")

if __name__ == "__main__":
    main()
