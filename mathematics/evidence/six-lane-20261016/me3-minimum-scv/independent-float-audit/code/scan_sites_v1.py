"""Independent float-contamination site scanner (static; stdlib only; reads lane files as TEXT, imports nothing
from the lane's code/ directory).

argv[1] = run directory (created by code/run_v1.sh). Writes, exclusive create:
  sites.tsv       one row per syntactic site of interest in the audited Python files:
                  file, line, col, kind, enclosing function, source segment, extra (operands / exponent / args)
  json_types.tsv  every leaf value of the audited spec JSONs with its parsed Python type and Q()-acceptability
  summary.json    per-file counts by kind, file sha256, JSON duplicate-key and float findings
Kinds: DIV, FLOORDIV, MOD, POW, AUGDIV, AUGPOW, FLOATLIT, NEGLIT, CALL:<name>, MATHATTR, IMPORT, COMPARE, DEFAULT,
       METHOD:<name>, FSTRING-SPEC.
"""
import ast
import hashlib
import json
import os
import re
import sys

RUN = sys.argv[1]
PYFILES = ["code/cert_primal_v3.py", "code/me3lib_v1.py", "code/me3jet_v1.py", "code/me3jet_v2.py",
           "code/cert_dual_v5.py", "code/me3dual_v7.py", "code/me3dual_v6.py", "code/me3dual_v4.py",
           "code/me3dual_v3.py", "code/cert_dual_v7.py", "code/me3dual_v9.py", "code/check_cover_v1.py",
           "code/check_cover_v2.py", "code/lane_guard.py"]
OTHER = ["code/run_v1.sh"]
SPECS = ["code/spec_primal_P_v1.json", "code/spec_dual_v1.json", "code/spec_dual_v3.json"]
CALLS = {"float", "round", "int", "str", "complex", "abs", "divmod", "pow", "sum", "min", "max", "bool",
         "Fraction", "fmpq", "arb", "acb", "fmpz", "len", "range", "open"}
METHODS = {"upper", "lower", "mid", "rad", "man_exp", "unique_fmpz", "union", "intersection", "is_finite",
           "exp", "log", "sqrt", "arg", "cos", "sin", "tan", "real", "imag", "pi", "load", "loads", "time",
           "floor", "ceil"}
FLOATMODS = {"math", "numpy", "np", "mpmath", "decimal", "fractions", "statistics", "cmath", "time", "json"}


def xopen(path):
    return open(path, "x")


def seg(src, node):
    s = ast.get_source_segment(src, node)
    return " ".join(s.split()) if s is not None else "?"


class V(ast.NodeVisitor):
    def __init__(self, fname, src):
        self.f, self.src, self.rows, self.func = fname, src, [], ["<module>"]

    def add(self, node, kind, extra=""):
        self.rows.append((self.f, node.lineno, node.col_offset, kind, self.func[-1], seg(self.src, node), extra))

    def visit_FunctionDef(self, node):
        for d in node.args.defaults + [d for d in node.args.kw_defaults if d is not None]:
            self.add(d, "DEFAULT", f"in def {node.name}")
        self.func.append(node.name)
        self.generic_visit(node)
        self.func.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Lambda(self, node):
        for d in node.args.defaults:
            self.add(d, "DEFAULT", "in lambda")
        self.generic_visit(node)

    def visit_BinOp(self, node):
        op = type(node.op).__name__
        kind = {"Div": "DIV", "FloorDiv": "FLOORDIV", "Mod": "MOD", "Pow": "POW"}.get(op)
        if kind:
            extra = f"L=[{seg(self.src, node.left)}] R=[{seg(self.src, node.right)}]"
            if kind == "POW":
                r = node.right
                neg = (isinstance(r, ast.UnaryOp) and isinstance(r.op, ast.USub)) or (
                    isinstance(r, ast.Constant) and isinstance(r.value, (int, float)) and r.value < 0)
                flt = isinstance(r, ast.Constant) and isinstance(r.value, float)
                extra += " NEG-EXP-LITERAL" if neg else ""
                extra += " FLOAT-EXP" if flt else ""
            self.add(node, kind, extra)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        op = type(node.op).__name__
        if op in ("Div", "FloorDiv", "Pow", "Mod"):
            self.add(node, "AUG" + op.upper(), "")
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return
        if isinstance(node.value, (float, complex)):
            self.add(node, "FLOATLIT", repr(node.value))

    def visit_UnaryOp(self, node):
        if isinstance(node.op, ast.USub) and isinstance(node.operand, ast.Constant) and \
                isinstance(node.operand.value, (int, float)) and not isinstance(node.operand.value, bool):
            self.add(node, "NEGLIT", repr(node.operand.value))
        self.generic_visit(node)

    def visit_Call(self, node):
        fn = node.func
        if isinstance(fn, ast.Name) and fn.id in CALLS:
            self.add(node, "CALL:" + fn.id, "args=" + " | ".join(seg(self.src, a) for a in node.args))
        elif isinstance(fn, ast.Attribute):
            fn._is_func = True
            base = fn.value
            if isinstance(base, ast.Name) and base.id in FLOATMODS:
                self.add(node, f"CALL:{base.id}.{fn.attr}", "args=" + " | ".join(seg(self.src, a) for a in node.args))
            elif fn.attr in METHODS:
                self.add(node, "METHOD:" + fn.attr, f"recv=[{seg(self.src, base)}]")
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name) and node.value.id in FLOATMODS and not getattr(node, "_is_func", False):
            self.add(node, "MODATTR", f"{node.value.id}.{node.attr}")
        self.generic_visit(node)

    def visit_Import(self, node):
        self.add(node, "IMPORT", ",".join(a.name for a in node.names))

    def visit_ImportFrom(self, node):
        self.add(node, "IMPORT", f"from {node.module} import " + ",".join(a.name for a in node.names))

    def visit_Compare(self, node):
        ops = ",".join(type(o).__name__ for o in node.ops)
        flt = any(isinstance(c, ast.Constant) and isinstance(c.value, float) for c in [node.left] + node.comparators)
        self.add(node, "COMPARE", ops + (" FLOAT-CONST" if flt else ""))
        self.generic_visit(node)

    def visit_JoinedStr(self, node):
        for v in node.values:
            if isinstance(v, ast.FormattedValue) and (v.format_spec is not None or v.conversion != -1):
                self.add(v, "FSTRING-SPEC", "")
        self.generic_visit(node)


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


rows = []
summary = {"files": {}, "json": {}}
for f in PYFILES:
    src = open(f, encoding="utf-8").read()
    tree = ast.parse(src, filename=f)
    v = V(f, src)
    v.visit(tree)
    rows.extend(v.rows)
    kinds = {}
    for r in v.rows:
        k = r[3]
        kinds[k] = kinds.get(k, 0) + 1
    summary["files"][f] = {"sha256": sha(f), "lines": src.count("\n"), "kinds": dict(sorted(kinds.items()))}
for f in OTHER:
    src = open(f, encoding="utf-8").read()
    summary["files"][f] = {"sha256": sha(f), "lines": src.count("\n"), "kinds": "manual (shell)"}

with xopen(RUN + "/sites.tsv") as fh:
    fh.write("file\tline\tcol\tkind\tfunction\tsegment\textra\n")
    for r in sorted(rows, key=lambda r: (PYFILES.index(r[0]), r[1], r[2], r[3])):
        fh.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")

QRE = re.compile(r"^-?\d+(/-?\d+)?$")
jrows = []
for f in SPECS:
    dups = []

    def hook(pairs, f=f, dups=dups):
        seen = set()
        for k, _ in pairs:
            if k in seen:
                dups.append(k)
            seen.add(k)
        return dict(pairs)

    raw = open(f, encoding="utf-8").read()
    data = json.loads(raw, object_pairs_hook=hook)

    def walk(x, path):
        if isinstance(x, dict):
            for k, val in x.items():
                walk(val, path + "/" + k)
        elif isinstance(x, list):
            for i, val in enumerate(x):
                walk(val, path + f"[{i}]")
        else:
            t = type(x).__name__
            qok = "" if not isinstance(x, (str, int)) or isinstance(x, bool) else (
                "Q-ok" if QRE.match(str(x)) else "Q-reject")
            jrows.append((f, path, t, repr(x)[:80], qok))

    walk(data, "")
    nfloat = sum(1 for r in jrows if r[0] == f and r[2] == "float")
    summary["json"][f] = {"sha256": sha(f), "duplicate_keys": dups, "float_values": nfloat,
                          "leaves": sum(1 for r in jrows if r[0] == f),
                          "types": {t: sum(1 for r in jrows if r[0] == f and r[2] == t)
                                    for t in sorted({r[2] for r in jrows if r[0] == f})},
                          "nonstring_numbers": [[r[1], r[2], r[3]] for r in jrows
                                                if r[0] == f and r[2] in ("int", "float")]}

with xopen(RUN + "/json_types.tsv") as fh:
    fh.write("file\tpath\ttype\tvalue\tQ\n")
    for r in jrows:
        fh.write("\t".join(r) + "\n")
summary["total_sites"] = len(rows)
with xopen(RUN + "/summary.json") as fh:
    json.dump(summary, fh, indent=1)
print(json.dumps({"total_sites": len(rows), "json_leaves": len(jrows),
                  "json_floats": {f: summary["json"][f]["float_values"] for f in SPECS},
                  "json_dups": {f: summary["json"][f]["duplicate_keys"] for f in SPECS}}))
