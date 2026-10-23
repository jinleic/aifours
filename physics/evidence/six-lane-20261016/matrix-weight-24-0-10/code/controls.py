"""Explicit control codes: [[5,1,3]] stabilizer (AMH Example 6), hexacode (6,2^6,4), dodecacode (12,2^12,6).
Each is verified (commuting, independent, distance) by brute force before its pair counts are used.
The dodecacode is realized as the graph state of the circulant graph C12(1,3,6), found by exhaustive search over
all 63 circulant connection sets (the only two hits, (1,3,6) and (3,5,6), have the dodecacode weights
1 + 396y^6 + 1485y^8 + 1980y^10 + 234y^12); the (12,2^12,6) even additive code is unique up to equivalence."""
import json

from pairs import FIVE_QUBIT, check_commuting, group_from_generators, pair_counts, weight_distribution

# F4 = {0,1,w,w^2} encoded as Pauli: 0->I, 1->X, w->Z, w^2->Y  (addition = XOR of (x,z) bits)
F4P = {0: "I", 1: "X", 2: "Z", 3: "Y"}   # 2 = w, 3 = w^2
MUL = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]


def f4_row_to_pauli(row):
    return "".join(F4P[a] for a in row)


def hexacode_generators():
    G = [[1, 0, 0, 1, 2, 2], [0, 1, 0, 2, 1, 2], [0, 0, 1, 2, 2, 1]]
    gens = []
    for r in G:
        gens.append(f4_row_to_pauli(r))
        gens.append(f4_row_to_pauli([MUL[2][a] for a in r]))
    return gens


def circulant_edges(n, D):
    E = set()
    for v in range(n):
        for dd in D:
            w = (v + dd) % n
            E.add((min(v, w), max(v, w)))
    return sorted(E)


def graph_state_generators(n, edges):
    nb = {v: set() for v in range(n)}
    for a, b in edges:
        nb[a].add(b)
        nb[b].add(a)
    gens = []
    for v in range(n):
        s = ["I"] * n
        s[v] = "X"
        for w in nb[v]:
            s[w] = "Z"
        gens.append("".join(s))
    return gens


def verify(gens, n):
    assert check_commuting(gens)
    X, Z = group_from_generators(gens, n)
    wd = weight_distribution(X, Z, n)
    d = min(w for w in range(1, n + 1) if wd[w] > 0)
    return X, Z, wd, d


CONTROLS = [("five_qubit_stabilizer", FIVE_QUBIT, 5),
            ("hexacode", hexacode_generators(), 6),
            ("dodecacode_circulant_1_3_6", graph_state_generators(12, circulant_edges(12, (1, 3, 6))), 12)]

if __name__ == "__main__":
    out = {}
    for name, gens, n in CONTROLS:
        X, Z, wd, d = verify(gens, n)
        lam = pair_counts(X, Z, n)
        out[name] = {"n": n, "gens": gens, "group_size": len(X), "weight_distribution": wd.tolist(),
                     "min_nonzero_weight": int(d),
                     "lambda": {",".join(map(str, k)): v for k, v in sorted(lam.items())}}
        print(name, "size", len(X), "weights", wd.tolist(), "d", d, "#nonzero lambda", len(lam))
    json.dump(out, open("../evidence/control_pair_counts.json", "w"), indent=1)
    print("AMH Example 6 check:", out["five_qubit_stabilizer"]["lambda"])
