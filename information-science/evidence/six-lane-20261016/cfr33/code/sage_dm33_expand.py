#!/usr/bin/env python3
"""Re-implement SageMath's DM_33_6_1() expansion from the pinned source text, without Sage (lane cfr33).

Usage: sage_dm33_expand.py OUT_DM_RAW
Reads sources/web/sage-designs-database.py (sha256 must equal PINNED), locates `def DM_33_6_1` with `ast`,
takes the literal lists assigned to M and Mb, and expands exactly as the Sage code does:
    for R in zip(*M): for i in range(5): Mb.append([a,b,c,d,e,f]); a,b,c,d,e,f = 4*e,4*a,4*b,4*c,4*d,4*f
Entries are reduced mod 33 (Sage evaluates them in AdditiveCyclic(33) = Z_33).
Writes the 6 x 33 difference matrix (row i = coordinate i of every Mb tuple) in dm-raw format: 6 LF-terminated
lines of 33 single-space-separated canonical decimals. Mode 'x' (never overwrites).
"""
import ast, hashlib, os, sys

PINNED = "55a30e8aebba5b1d34f8e6469dad746a42757b1c2c549715a04b00069be423a9"
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    out = sys.argv[1]
    src_path = os.path.join(LANE, "sources", "web", "sage-designs-database.py")
    raw = open(src_path, "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    assert h == PINNED, h
    tree = ast.parse(raw.decode("utf-8"))
    fn = [nd for nd in tree.body if isinstance(nd, ast.FunctionDef) and nd.name == "DM_33_6_1"]
    assert len(fn) == 1
    lits = {}
    for st in fn[0].body:
        if isinstance(st, ast.Assign) and len(st.targets) == 1 and isinstance(st.targets[0], ast.Name):
            name = st.targets[0].id
            if name in ("M", "Mb"):
                lits[name] = ast.literal_eval(st.value)
    M, Mb = lits["M"], lits["Mb"]
    assert len(M) == 6 and all(len(r) == 6 for r in M) and len(Mb) == 3
    for R in zip(*M):
        a, b, c, d, e, f = R
        for i in range(5):
            Mb.append([a, b, c, d, e, f])
            a, b, c, d, e, f = 4 * e, 4 * a, 4 * b, 4 * c, 4 * d, 4 * f
    assert len(Mb) == 33 and all(len(t) == 6 for t in Mb)
    D = [[Mb[t][i] % 33 for t in range(33)] for i in range(6)]
    text = "".join(" ".join(str(x) for x in row) + "\n" for row in D)
    with open(out, "x") as fh:
        fh.write(text)
    print("source sha256 %s; DM written %s sha256 %s" % (h, out, hashlib.sha256(text.encode()).hexdigest()))
    print("literal M =", M)
    print("literal Mb(initial 3) =", Mb[:3])


if __name__ == "__main__":
    main()
