"""Independently verify an embedding certificate S -> B x| Z2 printed by embed_generic_sat.py.

Checks: B is a band; tau is an involutive automorphism of B; x -> (beta(x), sigma(x)) is injective and
beta(xy) = beta(x) . tau^{sigma(x)}(beta(y)) for all x, y in S (sigma = parity: idempotents of S
are 0..n-1 = even part).  The semidirect product B x| Z2 is then a semigroup containing an
isomorphic copy of S.

Usage: python3 work/verify_embedding_certificate.py S.json certificate_log [--require-locreg]
"""
from __future__ import annotations

import json
import sys


def main() -> None:
    T = json.load(open(sys.argv[1]))
    lines = open(sys.argv[2]).read().splitlines()
    B = json.loads(next(l for l in lines if l.startswith("B:"))[2:].strip())
    tl = next(l for l in lines if l.startswith("tau:"))
    tau = json.loads(tl.split("beta:")[0][4:].strip())
    beta = json.loads(tl.split("beta:")[1].strip())
    k, N = len(B), len(T)
    n = sum(1 for x in range(N) if T[x][x] == x)
    assert all(T[x][x] == x for x in range(n)), "idempotents must be exactly the prefix 0..n-1"
    sig = [0 if x < n else 1 for x in range(N)]
    # the parity map must be a homomorphism onto Z2 (second coordinate of the embedding)
    assert all(sig[T[x][y]] == (sig[x] + sig[y]) % 2 for x in range(N) for y in range(N)), "parity not a homomorphism"
    assert all(B[x][x] == x for x in range(k)), "B not idempotent"
    assert all(B[B[x][y]][z] == B[x][B[y][z]] for x in range(k) for y in range(k) for z in range(k)), "B not associative"
    assert all(tau[tau[x]] == x for x in range(k)), "tau not an involution"
    assert all(tau[B[x][y]] == B[tau[x]][tau[y]] for x in range(k) for y in range(k)), "tau not an automorphism"
    assert len({(beta[x], sig[x]) for x in range(N)}) == N, "x -> (beta(x), sigma(x)) not injective"
    for x in range(N):
        for y in range(N):
            rhs = beta[y] if sig[x] == 0 else tau[beta[y]]
            assert beta[T[x][y]] == B[beta[x]][rhs], f"beta not a homomorphism at {x},{y}"
    def regular_on(elems):
        return all(B[B[B[a][x]][y]][a] == B[B[B[B[a][x]][a]][y]][a] for a in elems for x in elems for y in elems)
    locreg = all(regular_on(sorted({B[B[e][x]][e] for x in range(k)})) for e in range(k))
    if "--require-locreg" in sys.argv:
        assert locreg, "B is not locally regular"
    print(f"certificate verified: |S|={N} embeds in B x| Z2 with |B|={k}; B locally regular: {locreg}")


if __name__ == "__main__":
    main()
