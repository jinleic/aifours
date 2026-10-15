"""Independent exact checks of the all-n signed permutation convention in Theorem G.
Finite-rank checks support the implementation/formula; they do not prove the all-n theorem.
Uses no coxeter.py, roots, floating point, Garside normal form or completion.
"""
from collections import deque
import json
import math


def generator(v, i):
    w = list(v)
    n = len(w)
    if i == n - 1:
        w[0] = -w[0]
    else:
        p = n - i - 2
        w[p], w[p + 1] = w[p + 1], w[p]
    return tuple(w)


def length(v):
    return (sum(x < 0 for x in v)
            + sum(v[i] > v[j] for i in range(len(v)) for j in range(i + 1, len(v)))
            + sum(v[i] + v[j] < 0 for i in range(len(v)) for j in range(i + 1, len(v))))


def verify(n):
    identity = tuple(range(1, n + 1))
    distance = {identity: 0}
    queue = deque([identity])
    while queue:
        v = queue.popleft()
        for i in range(n):
            w = generator(v, i)
            if w not in distance:
                distance[w] = distance[v] + 1
                queue.append(w)
    assert len(distance) == (2 ** n) * math.factorial(n)
    for v, d in distance.items():
        assert length(v) == d
        for i in range(n):
            assert generator(generator(v, i), i) == v
    w0 = tuple(-i for i in range(1, n + 1))
    assert distance[w0] == n * n
    assert max(distance.values()) == n * n
    for i in range(n):
        for j in range(i + 1, n):
            m = 2 if j - i > 1 else (4 if j == n - 1 else 3)
            u = v = identity
            for k in range(m):
                u = generator(u, i if k % 2 == 0 else j)
                v = generator(v, j if k % 2 == 0 else i)
            assert u == v
    return {'rank':n,'order':len(distance),'length_formula_matches_all_elements':True,'N':n*n}


if __name__ == '__main__':
    print(json.dumps({'checks':[verify(n) for n in range(2, 7)],'ALL_OK':True},indent=1))
