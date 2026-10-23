#!/usr/bin/env python3
"""Compare DM_33_6_1 between two pinned Sage database.py files (literals M, Mb and the expansion loop text).
Usage: sage_version_compare.py FILE_OLD FILE_NEW"""
import ast, hashlib, sys, warnings
warnings.simplefilter("ignore")


def grab(path):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "DM_33_6_1"]
    assert len(fn) == 1
    lit = {}
    for st in fn[0].body:
        if isinstance(st, ast.Assign) and isinstance(st.targets[0], ast.Name) and st.targets[0].id in ("M", "Mb"):
            lit[st.targets[0].id] = ast.literal_eval(st.value)
    seg = ast.get_source_segment(src, fn[0])
    loop = seg[seg.index("for R in zip(*M)"):].strip()
    grp = "G = AdditiveCyclic(33)" in seg and "IntegerModRing as AdditiveCyclic" in seg
    return hashlib.sha256(open(path, "rb").read()).hexdigest(), fn[0].lineno, fn[0].end_lineno, lit, loop, grp


a = grab(sys.argv[1]); b = grab(sys.argv[2])
print("old %s sha256 %s DM_33_6_1 lines %d-%d group IntegerModRing(33): %s" % (sys.argv[1], a[0], a[1], a[2], a[5]))
print("new %s sha256 %s DM_33_6_1 lines %d-%d group IntegerModRing(33): %s" % (sys.argv[2], b[0], b[1], b[2], b[5]))
print("literals M,Mb identical:", a[3] == b[3])
print("expansion loop text identical:", a[4] == b[4])
print("M =", b[3]["M"]); print("Mb(initial) =", b[3]["Mb"]); print("loop:\n" + b[4])
