#!/usr/bin/env python3
"""Independent integer controls for f228, not a quantum-realizability test."""
from itertools import combinations


def incidence(m, counts):
    if len(counts) != m + 1 or any(n < 0 for n in counts):
        return "negative-or-wrong-counts"
    if sum(counts) != 64 - m:
        return "wrong-cell-total"
    if sum(k * n for k, n in enumerate(counts)) != 35 * m:
        return "wrong-incidence-total"
    if sum(k * (k - 1) // 2 * n for k, n in enumerate(counts)) != 20 * m * (m - 1) // 2:
        return "wrong-pair-intersection-total"
    return "ok"


# Solve the incidence equations over nonnegative integers, accounting for all
# 64 cells (the m copies of u are excluded from n_0,...,n_m).
m2 = []
for n2 in range(65):
    n1 = 70 - 2 * n2
    n0 = 62 - n1 - n2
    if incidence(2, (n0, n1, n2)) == "ok":
        m2.append((n0, n1, n2))
m3 = []
for n3 in range(65):
    n2 = 60 - 3 * n3
    n1 = 105 - 2 * n2 - 3 * n3
    n0 = 61 - n1 - n2 - n3
    if incidence(3, (n0, n1, n2, n3)) == "ok":
        m3.append((n0, n1, n2, n3))
assert m2 == [(12, 30, 20)]
assert len(m3) == 12 and [q[3] for q in m3] == list(range(5, 17))
assert max(q[0] for q in m3) == 11
assert incidence(2, (13, 29, 20)) == "wrong-incidence-total"
assert incidence(3, (-1, 36, 9, 17)) == "negative-or-wrong-counts"
print("incidence m2", m2)
print("incidence m3 n3 range", m3[0][3], m3[-1][3], "max n0", max(q[0] for q in m3))
print("incidence negatives rejected: wrong-incidence-total; negative-or-wrong-counts")

# A two-entry line is an edge of a matching, so, at L=14+s, at most
# floor(L/2) such lines exist. Compare against five classes independently.
for s in range(6):
    assert 5 * (7 - s) > (14 + s) // 2
assert 5 * (7 - 6) <= (14 + 6) // 2
print("matching s=0..5 impossible; s=6 is not excluded by this count")


def matching(edges):
    used = set()
    for a, b in edges:
        if a == b:
            return "self-edge"
        if a in used or b in used:
            return "reused-cell"
        used.add(a)
        used.add(b)
    return "ok"

assert matching([(0, 1), (2, 3)]) == "ok"
assert matching([(0, 1), (1, 2)]) == "reused-cell"
assert matching([(0, 0)]) == "self-edge"
print("matching negatives rejected: reused-cell; self-edge")

# Exhaust all labeled simple 7-vertex, 10-edge graphs in which vertex 6 has
# degree 2 and all others degree 3. Independently check the local triangle
# condition forced by the two-plane capacity and the resulting two-basis
# zero-pattern obstruction. Graphs alone do not imply complex realizability.
edges7 = list(combinations(range(7), 2))
triangle_subsets = list(combinations(range(7), 3))

def neighbor_pair_edges(adj, v):
    ns = [i for i in range(7) if adj[v] & (1 << i)]
    return sum(bool(adj[a] & (1 << b)) for a, b in combinations(ns, 2))


def local_reason(adj):
    deg = [bin(bits).count("1") for bits in adj]
    if deg != [3, 3, 3, 3, 3, 3, 2]:
        return "wrong-degree-sequence"
    if any(neighbor_pair_edges(adj, v) != 1 for v in range(6)):
        return "degree-three-neighbors-not-exactly-one-orthopair"
    if neighbor_pair_edges(adj, 6) > 1:
        return "degree-two-neighbors-too-many-orthopairs"
    return "ok"


def triangles(adj):
    return [t for t in triangle_subsets
            if all(adj[a] & (1 << b) for a, b in combinations(t, 2))]

wrong_degree = [0] * 7
assert local_reason(wrong_degree) == "wrong-degree-sequence"
total = valid = 0
first_local_negative = None
cross_hist = {}
for selected in combinations(edges7, 10):
    adj = [0] * 7
    for a, b in selected:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    if [bin(x).count("1") for x in adj] != [3, 3, 3, 3, 3, 3, 2]:
        continue
    total += 1
    reason = local_reason(adj)
    if reason != "ok":
        if first_local_negative is None:
            first_local_negative = reason
        continue
    valid += 1
    ts = triangles(adj)
    assert len(ts) == 2 and set(ts[0]).isdisjoint(ts[1])
    assert set(ts[0]) | set(ts[1]) == set(range(6))
    cross = sum(bool(adj[a] & (1 << b)) for a in ts[0] for b in ts[1])
    assert cross >= 2
    cross_hist[cross] = cross_hist.get(cross, 0) + 1
assert total > valid > 0
assert first_local_negative == "degree-three-neighbors-not-exactly-one-orthopair"
print("graphs degree-sequence", total, "local-condition", valid, "cross-edge histogram", sorted(cross_hist.items()))
print("graph negatives rejected: wrong-degree-sequence;", first_local_negative)
print("ALL EXACT INTEGER CONTROLS COMPLETED")
