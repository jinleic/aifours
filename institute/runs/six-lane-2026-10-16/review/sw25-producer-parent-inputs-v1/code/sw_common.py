"""Shared helpers for lane sw25-16 (stdlib only): parsing posted matrices, strict witness I/O, small constructions.

Nothing here decides validity; the checkers are code/verify_sw.py and bin/sw_check.
"""
import re


def parse_magma(path):
    """Parse a Munemasa-style 'W:=Matrix(Integers(),n,n,[ ... ]);' file; returns list of rows."""
    s = open(path, encoding="ascii").read()
    m = re.search(r"Matrix\(Integers\(\),\s*(\d+)\s*,\s*(\d+)\s*,\s*\[(.*?)\]\s*\)", s, re.S)
    if m is None:
        raise ValueError("no Matrix(...) found in " + path)
    r, c = int(m.group(1)), int(m.group(2))
    vals = [int(t) for t in re.findall(r"-?\d+", m.group(3))]
    if len(vals) != r * c:
        raise ValueError(f"{path}: {len(vals)} values for {r}x{c}")
    return [vals[i * c:(i + 1) * c] for i in range(r)]


def parse_bracket(path):
    """Parse a Dinitz-style file: bracketed rows '[ a b c ]' / '[a, b, c]', or one flat bracketed list of n*n values."""
    s = open(path, encoding="ascii").read()
    rows = []
    for m in re.finditer(r"\[([^\[\]]*)\]", s):
        vals = [int(t) for t in re.findall(r"-?\d+", m.group(1))]
        if vals:
            rows.append(vals)
    if len(rows) == 1:
        flat = rows[0]
        n = int(round(len(flat) ** 0.5))
        if n * n != len(flat):
            raise ValueError(f"{path}: flat list of {len(flat)} values is not square")
        rows = [flat[i * n:(i + 1) * n] for i in range(n)]
    n = len(rows)
    if any(len(r) != n for r in rows):
        raise ValueError(f"{path}: ragged rows")
    return rows


def to_strict(W, n, w):
    """Strict witness text: 'SW n w' then n lines of n entries separated by single spaces, LF endings."""
    out = [f"SW {n} {w}"]
    for row in W:
        out.append(" ".join(str(int(x)) for x in row))
    return "\n".join(out) + "\n"


def read_strict(path):
    """Read a strict witness file without validating it (validation is the checkers' job)."""
    lines = open(path, encoding="ascii").read().split("\n")
    _, n, w = lines[0].split(" ")
    n = int(n)
    W = [[int(t) for t in lines[1 + i].split(" ")] for i in range(n)]
    return n, int(w), W


def gram(W):
    n = len(W)
    return [[sum(W[i][k] * W[j][k] for k in range(len(W[0]))) for j in range(n)] for i in range(n)]


def is_weighing(W, w):
    G = gram(W)
    n = len(W)
    return all(G[i][j] == (w if i == j else 0) for i in range(n) for j in range(n))


def gf_elements(p, k, modpoly):
    """Elements of GF(p^k) as tuples (coefficients of 1, x, ..); modpoly gives x^k = sum modpoly[i] x^i."""
    import itertools
    return [tuple(t) for t in itertools.product(range(p), repeat=k)]


def gf_mul(a, b, p, modpoly):
    k = len(a)
    prod = [0] * (2 * k - 1)
    for i in range(k):
        for j in range(k):
            prod[i + j] = (prod[i + j] + a[i] * b[j]) % p
    for d in range(2 * k - 2, k - 1, -1):
        c = prod[d]
        if c:
            prod[d] = 0
            for i in range(k):
                prod[d - k + i] = (prod[d - k + i] + c * modpoly[i]) % p
    return tuple(prod[:k])


def gf_sub(a, b, p):
    return tuple((x - y) % p for x, y in zip(a, b))


def paley_conference(p, k, modpoly):
    """Symmetric conference matrix of order q+1 (q = p^k = 1 mod 4): [[0, 1^T], [1, Q]], Q_xy = chi(y - x)."""
    els = gf_elements(p, k, modpoly)
    zero = tuple([0] * k)
    squares = set(gf_mul(a, a, p, modpoly) for a in els if a != zero)
    q = len(els)

    def chi(a):
        if a == zero:
            return 0
        return 1 if a in squares else -1

    C = [[0] * (q + 1) for _ in range(q + 1)]
    for i in range(q):
        C[0][i + 1] = 1
        C[i + 1][0] = 1
        for j in range(q):
            C[i + 1][j + 1] = chi(gf_sub(els[j], els[i], p))
    return C


def sylvester(m):
    H = [[1]]
    for _ in range(m):
        H = [r + r for r in H] + [r + [-x for x in r] for r in H]
    return H
