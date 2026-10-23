"""DIMACS encoding of a cyclic (v,k,1) difference family with t = (v-1)/(k(k-1)) base blocks.

Variables x[i][e] (block i contains e).  Classes c = 1..(v-1)/2 (difference +-c).
  z[i][a][c] <-> x[i][a] & x[i][a+c]   (pair {a, a+c} lies in block i)
  every class: at least one z, and at most one z (sequential counter over all t*v pairs)
  every block: at most k elements (sequential counter).  With every class covered, the count
  sum_i C(k_i,2) >= (v-1)/2 = t*C(k,2) forces k_i = k for all i.
Symmetry breaking (each is a normalisation every DF admits): 0 in every block (translate each block),
and the pair {0,1} in block 0 (relabel the block holding class 1, translate it).
Optional --order: blocks 1..t-1 are ordered by the least class they contain (value precedence on
the block index of each class).

usage: python3 sat_cdf.py v k OUT.cnf [--order]
"""
import sys

def main():
    v, k, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    order = "--order" in sys.argv
    assert (v - 1) % (k * (k - 1)) == 0
    t, nc = (v - 1) // (k * (k - 1)), (v - 1) // 2
    nv = [0]
    def new():
        nv[0] += 1; return nv[0]
    X = [[new() for e in range(v)] for i in range(t)]
    cls = []
    def amo_seq(lits):
        # Sinz sequential at-most-one
        n = len(lits)
        if n <= 1: return
        s = [new() for _ in range(n - 1)]
        cls.append([-lits[0], s[0]])
        for j in range(1, n - 1):
            cls.append([-lits[j], s[j]]); cls.append([-s[j - 1], s[j]]); cls.append([-lits[j], -s[j - 1]])
        cls.append([-lits[n - 1], -s[n - 2]])
    def atmost_k(lits, K):
        n = len(lits)
        s = [[new() for _ in range(K)] for _ in range(n)]
        cls.append([-lits[0], s[0][0]])
        for j in range(1, K): cls.append([-s[0][j]])
        for a in range(1, n):
            cls.append([-lits[a], s[a][0]]); cls.append([-s[a - 1][0], s[a][0]])
            for j in range(1, K):
                cls.append([-lits[a], -s[a - 1][j - 1], s[a][j]]); cls.append([-s[a - 1][j], s[a][j]])
            cls.append([-lits[a], -s[a - 1][K - 1]])
    for i in range(t): cls.append([X[i][0]])
    cls.append([X[0][1]])
    for i in range(t): atmost_k(X[i], k)
    Y = {}  # Y[(c, i)] : class c covered in block i (for --order)
    for c in range(1, nc + 1):
        zs = []
        for i in range(t):
            zi = []
            for a in range(v):
                b = (a + c) % v
                z = new(); zi.append(z)
                cls.append([-z, X[i][a]]); cls.append([-z, X[i][b]]); cls.append([-X[i][a], -X[i][b], z])
            zs += zi
            if order:
                y = new(); Y[(c, i)] = y
                cls.append([-y] + zi)
                for z in zi: cls.append([-z, y])
        cls.append(zs)
        amo_seq(zs)
    if order:
        # value precedence on block indices 1..t-1: block i (i >= 2) may cover class c only if
        # block i-1 covers some class < c.  P[i][c] = block i covers some class <= c.
        P = {}
        for i in range(1, t):
            for c in range(1, nc + 1):
                p = new(); P[(i, c)] = p
                prev = [P[(i, c - 1)]] if c > 1 else []
                cls.append([-p, Y[(c, i)]] + prev)
                cls.append([-Y[(c, i)], p])
                if prev: cls.append([-prev[0], p])
        for i in range(2, t):
            for c in range(1, nc + 1):
                if c == 1: cls.append([-Y[(c, i)]])
                else: cls.append([-Y[(c, i)], P[(i - 1, c - 1)]])
    with open(out, "w") as f:
        f.write(f"c cyclic ({v},{k},1) DF, t={t}, order={order}\n")
        f.write(f"p cnf {nv[0]} {len(cls)}\n")
        for C in cls: f.write(" ".join(map(str, C)) + " 0\n")
    # variable map for decoding: x[i][e] = 1 + i*v + e
    print(f"vars={nv[0]} clauses={len(cls)} t={t} x_var(i,e)=1+i*{v}+e")

if __name__ == "__main__":
    main()
