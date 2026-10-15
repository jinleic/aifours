"""Sanity checks of the Garside normal-form oracle (coxeter.py).

Run: python3 work/test_oracle.py
"""
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from coxeter import DELTA, DINV, build, letter  # noqa: E402

EXPECTED_N = {("A", 3): 6, ("A", 4): 10, ("B", 3): 9, ("B", 4): 16, ("D", 4): 12, ("D", 5): 20,
              ("E", 6): 36, ("E", 7): 63, ("E", 8): 120, ("F", 4): 24, ("H", 3): 15, ("H", 4): 60}


def alt(x: str, y: str, k: int) -> str:
    return "".join(x if j % 2 == 0 else y for j in range(k))


def check(typ, n=0, m=0, trials=300, seed=1):
    G = build(typ, n, m)
    W = G.W
    key = (typ, n) if typ != "I" else ("I", m)
    if typ == "I":
        assert W.N == m
    else:
        assert W.N == EXPECTED_N[key], (key, W.N)
    rng = random.Random(seed)
    gens = [letter(i) for i in range(W.n)]
    rels = []
    for i in range(W.n):
        for j in range(i + 1, W.n):
            mij = W.M[i][j]
            rels.append((alt(gens[i], gens[j], mij), alt(gens[j], gens[i], mij)))
    dw = G.delta_word()
    assert len(dw) == W.N
    assert G.nf(dw) == DELTA
    alphabet = gens + [DELTA, DINV]
    for _ in range(trials):
        u = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 12)))
        v = "".join(rng.choice(alphabet) for _ in range(rng.randint(0, 12)))
        a, b = rng.choice(rels)
        nf = G.nf(u + a + v)
        assert nf == G.nf(u + b + v)
        assert G.nf(u + DELTA + DINV + v) == G.nf(u + v) == G.nf(u + DINV + DELTA + v)
        assert G.nf(u + dw + v) == G.nf(u + DELTA + v)
        assert G.nf(nf) == nf
        x = rng.choice(gens)
        # x Delta = Delta phi(x)
        px = letter(W.phi[ord(x) - ord("a")])
        assert G.nf(u + x + DELTA + v) == G.nf(u + DELTA + px + v)
    return W.N, W.phi


if __name__ == "__main__":
    for args in [("A", 3), ("A", 4), ("B", 3), ("B", 4), ("D", 4), ("D", 5), ("F", 4), ("H", 3),
                 ("H", 4), ("E", 6)]:
        print(args, check(*args, trials=100))
    for m in range(3, 9):
        print(("I", m), check("I", 0, m, trials=200))
    print("ok")
