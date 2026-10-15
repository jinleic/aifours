"""Independent checks of exported pair-regex GS bases (Theorem G).

Does not import complement_rules.py. Recomputes finite Coxeter joins by exhaustive
weak-order upper bounds, validates every pair-labelled edge, replays each GNFA
elimination identity, checks the entire leading language against MinRed, compares
all-length rational growth, and compares random reductions to Garside normal form.
Finite calculations certify these files, NOT the all-n theorem (written proof).
"""
from __future__ import annotations

import argparse
import json
import random
from collections import deque
from math import factorial

from automaton import NFAutomaton, build_table
from certify import NFA, irreducible_dfa_counts
from coxeter import build


def replay_regex(data):
    graph, cert = data["graph"], data["paired_regex"]
    nodes = cert["nodes"]
    lookup = {tuple(n): i for i, n in enumerate(nodes)}
    assert nodes[:2] == [["empty"], ["epsilon"]]
    assert len(lookup) == len(nodes)
    for i, node in enumerate(nodes):
        if node[0] in ("concat", "union", "star"):
            assert all(0 <= child < i for child in node[1:])

    def union(a, b):
        if not a or a == b:
            return b
        if not b:
            return a
        return lookup[("union", min(a, b), max(a, b))]

    def product(a, b):
        if not a or not b:
            return 0
        if a == 1:
            return b
        if b == 1:
            return a
        return lookup[("concat", a, b)]

    edges = {}
    for i, j, left, right in graph["edges"]:
        edges[i, j] = union(edges.get((i, j), 0), lookup[("pair", left, right)])
    remaining = set(range(len(graph["states"]))) - {graph["start"], graph["accept"]}
    for k in cert["elimination_order"]:
        assert k in remaining
        loop = edges.get((k, k), 0)
        loopstar = 1 if loop in (0, 1) else lookup[("star", loop)]
        incoming = [(i, val) for (i, j), val in edges.items() if j == k and i != k]
        outgoing = [(j, val) for (i, j), val in edges.items() if i == k and j != k]
        for i, left in incoming:
            for j, right in outgoing:
                edges[i, j] = union(edges.get((i, j), 0), product(product(left, loopstar), right))
        edges = {key: val for key, val in edges.items() if k not in key}
        remaining.remove(k)
    assert not remaining
    assert edges.get((graph["start"], graph["accept"]), 0) == cert["root"]
    return True


def exact_table_audit(data, T):
    """Certify the candidate finite permutation group, lengths and weak order
    without floating roots. Upward weak-order sets are exact integer bitsets."""
    typ, n, m = data["type"]
    orders = {"A": factorial(n + 1), "B": 2**n * factorial(n),
              "D": 2**(n-1) * factorial(n) if n else 1,
              "F": 1152, "H": 120 if n == 3 else 14400, "I": 2*m}
    assert T.size == orders[typ]
    distance = [-1] * T.size
    distance[T.e] = 0
    queue = deque([T.e])
    while queue:
        w = queue.popleft()
        for i in range(T.n):
            v = T.rmul[w][i]
            assert T.rmul[v][i] == w
            if distance[v] < 0:
                distance[v] = distance[w] + 1
                queue.append(v)
    assert distance == T.length
    for i in range(T.n):
        for j in range(i + 1, T.n):
            assert T.alt(i, j, T.M[i][j]) == T.alt(j, i, T.M[i][j])
    # Certify that the separately stored left action is the left regular action.
    for i in range(T.n):
        assert T.lmul[i][T.e] == T.gen[i]
        for w in range(T.size):
            for j in range(T.n):
                assert T.lmul[i][T.rmul[w][j]] == T.rmul[T.lmul[i][w]][j]
    assert distance[T.w0] == max(distance) == T.W.N
    assert distance.count(T.W.N) == 1
    upward = [0] * T.size
    for w in sorted(range(T.size), key=lambda v: distance[v], reverse=True):
        bits = 1 << w
        for i in range(T.n):
            v = T.rmul[w][i]
            if distance[v] == distance[w] + 1:
                bits |= upward[v]
        upward[w] = bits
    return distance, upward


def validate_edges(data, T):
    distance, upward = exact_table_audit(data, T)
    reps = data["simple_words"]
    assert len(reps) == T.size
    for i, w in enumerate(reps):
        assert len(w) == distance[i]
        assert T.word_elem([ord(c) - 97 for c in w]) == i
    twists = []
    for i in range(T.n):
        conjugate = T.rmul[T.w0][i]
        for c in reps[T.w0]:
            conjugate = T.rmul[conjugate][ord(c) - 97]
        phi_i = T.gen.index(conjugate)
        for delta in "01":
            twists.append([chr(97 + i) + delta, delta + chr(97 + phi_i)])
    assert sorted(data["twists"]) == sorted(twists)
    assert sorted(data["cancellations"]) == [["01", ""], ["10", ""]]
    cached = {}

    def join(a, b):
        key = a, b
        if key not in cached:
            mask = upward[a] & upward[b]
            uppers = [u for u in range(T.size) if (mask >> u) & 1]
            j = min(uppers, key=distance.__getitem__)
            assert upward[j] & mask == mask
            cached[key] = j
        return cached[key]

    def quotient(a, j):
        for c in reps[a]:
            j = T.lmul[ord(c) - 97][j]
        return j

    graph = data["graph"]
    for s, t, left, right in graph["edges"]:
        assert len(left) == 1 and 'a' <= left < chr(97 + T.n)
        y = ord(left) - 97
        dest = T.e if t == graph["accept"] else graph["states"][t][0]
        if s == graph["start"]:
            assert right
            q = T.w0 if right[0] == '1' else T.gen[ord(right[0]) - 97]
            assert right[0] == '1' or right[0] < left
            j = join(T.gen[y], q)
            assert dest == T.lmul[y][j]
            assert right[1:] == reps[quotient(q, j)]
        else:
            e = graph["states"][s][0]
            assert e != T.e
            j = join(e, T.gen[y])
            assert dest == T.lmul[y][j]
            f = quotient(e, j)
            assert right == reps[f]
            assert T.length[e] + T.length[f] == 1 + T.length[dest] == T.length[j]
    return {"edges_verified": len(graph["edges"]), "joins_checked_exhaustively": len(cached),
            "candidate_group_order_verified": T.size, "all_lengths_verified": True,
            "join_method": "exact Cayley-distance weak-order bitsets; no root rounding"}


def language_check(data, T):
    graph = data["graph"]
    outgoing = {i: {} for i in range(len(graph["states"]))}
    for i, j, a, b in graph["edges"]:
        outgoing[i].setdefault(a, set()).add(j)
    A = NFAutomaton(T)
    start = (frozenset([graph["start"]]), "start")
    seen, todo = {start}, deque([start])
    while todo:
        subset, state = todo.popleft()
        assert (graph["accept"] in subset) == (state == "accept")
        for y in range(T.n):
            a = chr(97 + y)
            out = frozenset(t for s in subset for t in outgoing[s].get(a, ()))
            if state == "start":
                dst = (A.step(frozenset(), y), frozenset())
            elif isinstance(state, str):
                dst = "dead"
            else:
                full, suffix = state
                suffix2 = A.step(suffix, y)
                if suffix2 is None:
                    dst = "dead"
                else:
                    full2 = A.step(full, y)
                    dst = "accept" if full2 is None else (full2, suffix2)
            pair = out, dst
            if pair not in seen:
                seen.add(pair)
                todo.append(pair)
    return len(seen)


def exact_growth(T, bound):
    """Parabolic inclusion-exclusion using exact subgroup BFS in the finite table."""
    denominator = [0] * (T.W.N + 1)
    for mask in range(1 << T.n):
        gens = [i for i in range(T.n) if mask & (1 << i)]
        subgroup, todo = {T.e}, [T.e]
        while todo:
            w = todo.pop()
            for i in gens:
                v = T.rmul[w][i]
                if v not in subgroup:
                    subgroup.add(v)
                    todo.append(v)
        degree = max(T.length[w] for w in subgroup)
        denominator[degree] += (-1)**len(gens)
    monoid = [1] + [0]*bound
    answer, cumulative = [], 0
    for k in range(bound + 1):
        if k:
            monoid[k] = -sum(denominator[j]*monoid[k-j]
                             for j in range(1, min(k, T.W.N) + 1))
        free = monoid[k] - (monoid[k-T.W.N] if k >= T.W.N else 0)
        answer.append(free + 2*cumulative)
        cumulative += free
    return answer


def growth_check(data, T):
    graph = data["graph"]
    N = NFA()
    for _ in range(len(graph["states"]) - 1):
        N.new()
    for i, j, a, _ in graph["edges"]:
        N.add(i, a, j)
    assert graph["start"] == 0
    N.final.add(graph["accept"])
    for lhs, rhs in data["twists"] + data["cancellations"]:
        N.add_family([(lhs, None)])
    alphabet = "01" + "".join(chr(97 + i) for i in range(T.n))
    _, K, _, _ = irreducible_dfa_counts(N, alphabet, 0)
    bound = K + T.W.N + 2
    counts, _, _, _ = irreducible_dfa_counts(N, alphabet, bound)
    expected = exact_growth(T, bound)
    assert counts == expected
    return {"dfa_states": K, "rational_identity_bound": bound, "all_coefficients_match": True,
            "first_counts": counts[:13]}


def make_reducer(data):
    graph = data["graph"]
    edges = {i: {} for i in range(len(graph["states"]))}
    for i, j, a, b in graph["edges"]:
        edges[i].setdefault(a, []).append((j, b))
    fixed = dict(data["twists"] + data["cancellations"])

    def reduce(word):
        for _ in range(100000):
            replacement = None
            for i in range(len(word)):
                if word[i:i+2] in fixed:
                    replacement = i, i+2, fixed[word[i:i+2]]
                    break
                paths = {graph["start"]: ""}
                for j in range(i, len(word)):
                    nxt = {}
                    for s, out in paths.items():
                        for t, emission in edges[s].get(word[j], ()):
                            nxt.setdefault(t, out + emission)
                    if graph["accept"] in nxt:
                        replacement = i, j+1, nxt[graph["accept"]]
                        break
                    if not nxt:
                        break
                    paths = nxt
                if replacement:
                    break
            if replacement is None:
                return word
            i, j, tail = replacement
            new = word[:i] + tail + word[j:]
            assert (len(new), new) < (len(word), word)
            word = new
        raise RuntimeError("reduction step cap exceeded")
    return reduce


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('spec')
    parser.add_argument('--random', type=int, default=400)
    args = parser.parse_args()
    data = json.load(open(args.spec))
    typ, n, m = data['type']
    T = build_table(typ, n, m, data['order'])
    edges = validate_edges(data, T)
    replay = replay_regex(data)
    states = language_check(data, T)
    growth = growth_check(data, T)
    reduce = make_reducer(data)
    G = build(typ, n, m, data['order'])
    rng = random.Random(20261014)
    alphabet = '01' + ''.join(chr(97 + i) for i in range(T.n))
    # The rule reducer and normal-form oracle are separate algorithms.
    for _ in range(args.random):
        word = ''.join(rng.choice(alphabet) for _ in range(rng.randrange(45)))
        reduced = reduce(word)
        assert reduced == G.nf(word)
        assert reduce(reduced) == reduced
    # Mutations must be rejected, rather than merely repeating successful checks.
    altered = json.loads(json.dumps(data))
    altered['paired_regex']['root'] = 0
    try:
        replay_regex(altered)
    except AssertionError:
        regex_mutation_rejected = True
    else:
        raise AssertionError('bad regex certificate accepted')
    altered = json.loads(json.dumps(data))
    altered['graph']['edges'][0][3] += 'a'
    try:
        validate_edges(altered, T)
    except AssertionError:
        output_mutation_rejected = True
    else:
        raise AssertionError('bad output accepted')
    print(json.dumps({'type': data['type'], 'order': data['order'], **edges,
                      'regex_replay': replay, 'leading_language_product_states': states,
                      'growth_certificate': growth, 'random_word_equalities': args.random,
                      'mutation_checks': [regex_mutation_rejected, output_mutation_rejected],
                      'ALL_OK': True}, indent=1))


if __name__ == '__main__':
    main()
