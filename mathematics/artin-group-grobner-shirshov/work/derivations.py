"""Explicit braid-relation derivation chains for the positive identities used in
the validity proofs (right transport + base identities) of an explicit family
spec.  Each chain is a sequence of words, consecutive ones differing by one
application of a defining relation  Pi_m(s,t) = Pi_m(t,s).  Human-checkable.

Usage: python3 work/derivations.py SPEC > evidence/certify/SPEC_derivations.txt
"""
import sys
from collections import deque

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from certify import braid_relations, split  # noqa: E402
from coxeter import build  # noqa: E402
from specs import SPECS  # noqa: E402


def chain(u, v, rels):
    if u == v:
        return [u]
    parent = {u: None}
    dq = deque([u])
    while dq:
        w = dq.popleft()
        for a, b in rels:
            k = w.find(a)
            while k != -1:
                x = w[:k] + b + w[k + len(a):]
                if x not in parent:
                    parent[x] = (w, k, a, b)
                    if x == v:
                        out = [x]
                        while parent[out[-1]] is not None:
                            out.append(parent[out[-1]][0])
                        return out[::-1]
                    dq.append(x)
                k = w.find(a, k + 1)
    return None


def main():
    spec = SPECS[sys.argv[1]]()
    typ, n, m = spec["type"]
    G = build(typ, n, m, spec["order"])
    W = G.W
    rels = braid_relations(W.M)
    dw = G.delta_word()
    print(f"# {sys.argv[1]}: type {spec['type']} order {spec['order']}; Delta = {dw}")
    print("# relations:", ", ".join(f"{a}={b}" for a, b in rels[::2]))
    for name, lhs, rhs, mins in spec["families"]:
        if name in ("I1", "I2"):
            continue
        ids = []
        if name.startswith("T"):
            x = name[1]
            y = chr(97 + W.phi[ord(x) - 97])
            ids.append((x + dw, dw + y) if name.endswith("+") else (dw + x, y + dw))
        else:
            A, X, _ = split(lhs)
            B, Y, _ = split(rhs)
            for k in range(1, len(X) + 1):
                rho = "".join(A[k:])
                ids.append((X[k - 1] + rho, rho + Y[k - 1]))
            ids.append(("".join(A), B[0].replace("1", dw)))
        print(f"\n[{name}] {lhs} -> {rhs} mins={mins}")
        for u, v in ids:
            c = chain(u, v, rels)
            print(f"  {u} = {v}:  " + (" -> ".join(c) if c else "NOT DERIVED"))


if __name__ == "__main__":
    main()
