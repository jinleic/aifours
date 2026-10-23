"""ME3 parent desk (ME3ParentPrimal): static float-contamination audit of the desk's own checkers (AST, no import).

Usage: float_audit_v1.py RUN_DIR FILE [FILE ...]
For every listed Python file reports, with line numbers and source text:
  * float literals (ast.Constant of type float, incl. scientific notation) and complex literals;
  * every true division `/` (ast.Div) with its operand source text (int/int would yield a Python float);
  * calls of float(...), and any use of the math module / `import math`;
  * any comparison whose operands contain a float literal;
  * mpmath usage lines (mp.* / mpmath.*), which the desk allows only in non-certifying diagnostics or mutation
    construction.
The classification of each hit (certified path or not, operand types) is done by the parent in the receipt.
Writes RUN_DIR/RESULT.json (exclusive create).
"""
import ast
import json
import os
import sys

RUN = sys.argv[1]
out = {"script": "float_audit_v1.py", "files": {}}
for path in sys.argv[2:]:
    src = open(path).read()
    tree = ast.parse(src)
    lines = src.splitlines()
    rep = {"float_literals": [], "complex_literals": [], "divisions": [], "float_calls": [], "math_uses": [],
           "float_comparisons": [], "mpmath_lines": []}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            rep["float_literals"].append([node.lineno, ast.get_source_segment(src, node)])
        if isinstance(node, ast.Constant) and isinstance(node.value, complex):
            rep["complex_literals"].append([node.lineno, ast.get_source_segment(src, node)])
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            rep["divisions"].append([node.lineno, ast.get_source_segment(src, node.left),
                                     ast.get_source_segment(src, node.right)])
        if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Div):
            rep["divisions"].append([node.lineno, "augassign", ast.get_source_segment(src, node)])
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "float":
            rep["float_calls"].append([node.lineno, ast.get_source_segment(src, node)])
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "math":
            rep["math_uses"].append([node.lineno, ast.get_source_segment(src, node)])
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names]
            mod = getattr(node, "module", None)
            if "math" in names or mod == "math":
                rep["math_uses"].append([node.lineno, "import math"])
        if isinstance(node, ast.Compare):
            has_f = any(isinstance(n, ast.Constant) and isinstance(n.value, float) for n in ast.walk(node))
            if has_f:
                rep["float_comparisons"].append([node.lineno, ast.get_source_segment(src, node)])
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if ("mp." in s or "mpmath" in s) and not s.startswith("#"):
            rep["mpmath_lines"].append([i, s[:160]])
    rep["counts"] = {k: len(v) for k, v in rep.items() if isinstance(v, list)}
    out["files"][path] = rep
with open(os.path.join(RUN, "RESULT.json"), "x") as fh:
    json.dump(out, fh, indent=1)
for p, r in out["files"].items():
    print(p, json.dumps(r["counts"]))
