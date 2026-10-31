from functools import lru_cache
from itertools import product
from time import monotonic

WORK_SECONDS = 50.0
deadline = monotonic() + WORK_SECONDS
completed = 0

class WorkLimit(Exception):
    pass

def gate():
    if monotonic() >= deadline:
        raise WorkLimit()

def need(condition, message):
    if not condition:
        raise ValueError(message)

@lru_cache(maxsize=65536)
def normal(word):
    gate()
    if not word:
        return ()
    content = frozenset(word)
    seen = set()
    for left, letter in enumerate(word):
        seen.add(letter)
        if seen == content:
            break
    seen.clear()
    for right in range(len(word) - 1, -1, -1):
        seen.add(word[right])
        if seen == content:
            break
    return (normal(word[:left]) + (word[left], word[right])
            + normal(word[right + 1:]))

RULES = (
    ((4, 0, 1), (4,)),
    ((4, 2, 3), (4,)),
    ((1, 0, 5, 6), (5, 6)),
    ((3, 2, 5, 1, 4, 0, 5, 6), (5, 1, 4, 0, 5, 6)),
)
UWORD = (4, 0, 5, 6)
VWORD = (4, 2, 5, 1, 4, 0, 5, 6)
GENERATOR_NAMES = ("a", "ap", "b", "bp", "e", "f", "g")

def main():
    global completed
    letters = tuple(normal((i,)) for i in range(3))
    carrier = list(letters)
    present = set(carrier)
    cursor = 0
    while cursor < len(carrier):
        gate()
        word = carrier[cursor]
        cursor += 1
        for letter in letters:
            value = normal(word + letter)
            if value not in present:
                present.add(value)
                carrier.append(value)
                need(len(carrier) <= 256, "Candidate band carrier cap exceeded")
    carrier.sort()
    index = {word: i for i, word in enumerate(carrier)}
    n = len(carrier)
    table = []
    for word in carrier:
        gate()
        row = []
        for other in carrier:
            value = normal(word + other)
            need(value in index, "Candidate band not closed")
            row.append(index[value])
        table.append(row)
    for i in range(n):
        gate()
        need(table[i][i] == i, "Candidate band not idempotent")
        for j in range(n):
            left_row = table[table[i][j]]
            for k in range(n):
                need(left_row[k] == table[i][table[j][k]],
                     "Candidate band not associative")
    involution = []
    for word in carrier:
        shifted = tuple(1 - x if x < 2 else 2 for x in word)
        value = normal(shifted)
        need(value in index, "Involution leaves candidate carrier")
        involution.append(index[value])
    for i in range(n):
        gate()
        need(involution[involution[i]] == i, "Involution not order two")
        for j in range(n):
            need(involution[table[i][j]]
                 == table[involution[i]][involution[j]],
                 "Involution not an automorphism")
    atoms = tuple(index[word] for word in letters)

    def ambient_mul(x, y):
        i, h = x
        j, k = y
        return (table[i][involution[j] if h else j], h ^ k)

    for assignment in product(range(3), repeat=5):
        gate()
        av, bv, ev, fv, gv = (atoms[x] for x in assignment)
        generators = (
            (av, 1), (involution[av], 1),
            (bv, 1), (involution[bv], 1),
            (ev, 0), (fv, 0), (gv, 0),
        )
        source = list(dict.fromkeys(generators))
        source_index = {value: i for i, value in enumerate(source)}
        cursor = 0
        while cursor < len(source):
            gate()
            value = source[cursor]
            cursor += 1
            for generator in generators:
                result = ambient_mul(value, generator)
                if result not in source_index:
                    source_index[result] = len(source)
                    source.append(result)
        size = len(source)
        source_table = []
        for value in source:
            gate()
            row = []
            for other in source:
                result = ambient_mul(value, other)
                need(result in source_index, "Source image not closed")
                row.append(source_index[result])
            source_table.append(row)
        gen_indices = tuple(source_index[x] for x in generators)

        def evaluate(word):
            value = gen_indices[word[0]]
            for letter in word[1:]:
                value = source_table[value][gen_indices[letter]]
            return value

        parent = list(range(size))
        weights = [1] * size

        def find(value):
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        pending = [(evaluate(left), evaluate(right))
                   for left, right in RULES]
        while pending:
            gate()
            left, right = pending.pop()
            left, right = find(left), find(right)
            if left == right:
                continue
            need(source[left][1] == source[right][1],
                 "Congruence merge changes group grade")
            if weights[left] < weights[right]:
                left, right = right, left
            parent[right] = left
            weights[left] += weights[right]
            for context in range(size):
                pending.append((source_table[context][left],
                                source_table[context][right]))
                pending.append((source_table[left][context],
                                source_table[right][context]))
        representatives = [find(i) for i in range(size)]
        for i in range(size):
            gate()
            for j in range(size):
                need(find(source_table[i][j])
                     == find(source_table[representatives[i]]
                                             [representatives[j]]),
                     "Computed equivalence is not a congruence")
        for left, right in RULES:
            need(find(evaluate(left)) == find(evaluate(right)),
                 "Source relation absent from computed congruence")
        completed += 1
        uroot, vroot = find(evaluate(UWORD)), find(evaluate(VWORD))
        if uroot == vroot:
            continue

        roots = sorted(set(representatives))
        class_number = {root: i for i, root in enumerate(roots)}
        qtable = []
        for left in roots:
            gate()
            qtable.append([class_number[find(source_table[left][right])]
                           for right in roots])
        grades = [source[root][1] for root in roots]
        need(set(grades) == {0, 1}, "Quotient group map not onto")
        inverses = []
        for i in range(len(roots)):
            gate()
            need((grades[i] == 0) == (qtable[i][i] == i),
                 "Quotient group map not idempotent-pure")
            for j in range(len(roots)):
                need(grades[qtable[i][j]] == (grades[i] ^ grades[j]),
                     "Quotient group map not a homomorphism")
            inverse = next(
                (j for j in range(len(roots))
                 if qtable[qtable[i][j]][i] == i
                 and qtable[qtable[j][i]][j] == j),
                None,
            )
            need(inverse is not None, "Quotient not regular")
            inverses.append(inverse)
        gate()
        print("SEPARATOR_FOUND")
        print("COMPLETED_ASSIGNMENTS", completed)
        print("BAND_SIZE", n)
        print("BAND_CARRIER_WORDS", carrier)
        print("BAND_GENERATORS", *atoms)
        print("BAND_INVOLUTION", *involution)
        for i, row in enumerate(table):
            print("BAND_ROW", i, *row)
        print("ASSIGNMENT_a0_b0_e0_f0_g0", *assignment)
        print("SOURCE_IMAGE_SIZE", size)
        print("QUOTIENT_SIZE", len(roots))
        print("GENERATOR_ORDER", *GENERATOR_NAMES)
        print("QUOTIENT_GENERATORS",
              *(class_number[find(x)] for x in gen_indices))
        print("QUOTIENT_GRADES", *grades)
        print("QUOTIENT_INVERSES", *inverses)
        print("U_V", class_number[uroot], class_number[vroot])
        for i, row in enumerate(qtable):
            print("QUOTIENT_ROW", i, *row)
        return
    print("SELECTED_ASSIGNMENTS_EXHAUSTED", completed)
    print("NO_SEP_CONCLUSION_FOR_ORIGINAL_SOURCE")

if __name__ == "__main__":
    try:
        main()
    except WorkLimit:
        print("COOPERATIVE_WORK_LIMIT")
        print("COMPLETED_ASSIGNMENTS", completed)
        print("NO_SEP_CONCLUSION_FOR_ORIGINAL_SOURCE")
