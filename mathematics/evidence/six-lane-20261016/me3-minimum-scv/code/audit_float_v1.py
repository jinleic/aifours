"""Float-contamination audit, version 1 (hostile review me3-charts-codex-v1, finding 1 follow-up).

Part A (STATIC, exhaustive): parse every listed source file and list every site of the classes that can inject Python
float arithmetic: true division `/` (BinOp and AugAssign), `**`, float/complex literals, calls into math/numpy/mpmath,
float()/round()/complex(), and imports of float libraries. Output: static_sites.json and static_sites.txt (one line per
site with a stable id FILE:LINE:COL:KIND and the exact source segment). Dispositions are written in
proof/float-audit-v1.md.

Part B (DYNAMIC type trace, supporting evidence only): load the evaluator modules and the drivers' definition
prefixes (all top-level statements before the branch-and-bound loop) from source with every BinOp (+ - * / **)
rewritten to a call that records (left type, right type, result type) and then performs the same operation. Run the
certified chart evaluators on boxes from the coverage audits' samples (recorded leaves; the recomputed outcome must
equal the recorded one) and on initial cells (coarse boxes, to exercise failing branches). A site is FLAGGED if any
traced operation had a Python float operand or result, or was int/int true division, or int ** negative int.
Unexercised sites are listed (they rely on the static dispositions only).
argv[1] = run dir. Writes static_sites.json, static_sites.txt, trace.json (exclusive create).
"""
import sys
import ast
import json
import collections
import importlib.abc
import importlib.util
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
from flint import fmpq  # noqa: E402

RUN = sys.argv[1]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"
C = L + "code/"
FILES = ["cert_primal_v3.py", "me3lib_v1.py", "me3jet_v1.py", "me3jet_v2.py", "me3dual_v3.py", "me3dual_v4.py",
         "me3dual_v6.py", "me3dual_v7.py", "me3dual_v8.py", "me3dual_v9.py", "cert_dual_v5.py", "cert_dual_v6.py",
         "cert_dual_v7.py", "check_cover_v1.py", "check_cover_v2.py", "check_cover_v3.py", "lane_guard.py"]
FLOATMODS = {"math", "numpy", "np", "mpmath", "decimal", "cmath", "random", "statistics"}

# ------------------------------------------------------------------------------------------------ Part A (static)
static = []
for fn in FILES:
    src = open(C + fn).read()
    tree = ast.parse(src)
    parents = {}
    for node in ast.walk(tree):
        for ch in ast.iter_child_nodes(node):
            parents[ch] = node

    def func_of(node):
        while node in parents:
            node = parents[node]
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                return node.name
        return "<module>"

    def add(node, kind, extra=None):
        static.append({"id": f"{fn}:{node.lineno}:{node.col_offset}:{kind}", "file": fn, "line": node.lineno,
                       "kind": kind, "function": func_of(node), "segment": ast.get_source_segment(src, node),
                       **(extra or {})})
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            add(node, "div", {"left": ast.get_source_segment(src, node.left),
                              "right": ast.get_source_segment(src, node.right)})
        elif isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Div):
            add(node, "augdiv")
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            add(node, "pow", {"exponent": ast.get_source_segment(src, node.right)})
        elif isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            add(node, "float-literal", {"value": repr(node.value)})
        elif isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id in FLOATMODS:
                add(node, "float-lib-call")
            elif isinstance(f, ast.Name) and f.id in ("float", "round", "complex"):
                add(node, "float-builtin-call")
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module or ""]
            if any(n.split(".")[0] in FLOATMODS for n in names):
                add(node, "float-lib-import")
with lane_guard.xopen(RUN + "/static_sites.json") as fh:
    json.dump(static, fh, indent=0)
with lane_guard.xopen(RUN + "/static_sites.txt") as fh:
    for s in static:
        fh.write(f"{s['id']}\t{s['function']}\t{s['segment']}\n")
print("static sites", len(static), collections.Counter(s["kind"] for s in static))

# ------------------------------------------------------------------------------------------------ Part B (dynamic)
TRACE = collections.defaultdict(collections.Counter)
SEG = {}


def tname(x):
    return type(x).__name__


def __tb__(a, b, op, sid):
    if op == "Div":
        r = a / b
    elif op == "Pow":
        r = a ** b
    elif op == "Add":
        r = a + b
    elif op == "Sub":
        r = a - b
    else:
        r = a * b
    TRACE[sid][(tname(a), tname(b), tname(r))] += 1
    return r


class Tx(ast.NodeTransformer):
    OPS = {ast.Div: "Div", ast.Pow: "Pow", ast.Add: "Add", ast.Sub: "Sub", ast.Mult: "Mult"}

    def __init__(self, fn, src):
        self.fn, self.src = fn, src

    def visit_BinOp(self, node):
        seg = ast.get_source_segment(self.src, node)
        self.generic_visit(node)
        op = self.OPS.get(type(node.op))
        if op is None:
            return node
        sid = f"{self.fn}:{node.lineno}:{node.col_offset}:{op}"
        SEG[sid] = seg
        call = ast.Call(func=ast.Name("__tb__", ast.Load()),
                        args=[node.left, node.right, ast.Constant(op), ast.Constant(sid)], keywords=[])
        return ast.copy_location(call, node)


def traced_code(fn, stop_line=None):
    src = open(C + fn).read()
    tree = ast.parse(src)
    if stop_line is not None:
        tree.body = [st for st in tree.body if st.lineno < stop_line]
    tree = ast.fix_missing_locations(Tx(fn, src).visit(tree))
    return compile(tree, C + fn, "exec")


MODS = {"me3jet_v1", "me3jet_v2", "me3lib_v1", "me3dual_v3", "me3dual_v4", "me3dual_v6", "me3dual_v7", "me3dual_v9"}


class Finder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, name, path=None, target=None):
        if name in MODS:
            return importlib.util.spec_from_loader(name, self, origin=C + name + ".py")
        return None

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        module.__dict__["__tb__"] = __tb__
        module.__file__ = C + module.__name__ + ".py"
        exec(traced_code(module.__name__ + ".py"), module.__dict__)


sys.meta_path.insert(0, Finder())


def driver_ns(fn, argv):
    src = open(C + fn).read()
    stop = next(st.lineno for st in ast.parse(src).body
                if isinstance(st, ast.Assign) and ast.get_source_segment(src, st).startswith("t0 = time.time()"))
    ns = {"__tb__": __tb__, "__file__": C + fn, "__name__": "traced_" + fn[:-3]}
    old = sys.argv
    sys.argv = [C + fn] + argv
    try:
        exec(traced_code(fn, stop), ns)
    finally:
        sys.argv = old
    return ns


def Qs(x):
    if "/" in x:
        a, b = x.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(x))


def sample_boxes(chart, limit):
    out = []
    for line in open(L + f"runs/b03-cover-{chart}/sample_boxes.txt"):
        p = line.split()
        if len(p) == 7:
            v = [Qs(x) for x in p[1:]]
            out.append((p[0], ((v[0], v[1]), (v[2], v[3]), (v[4], v[5]))))
    step = max(1, len(out) // limit)
    return out[::step][:limit]


report = {"charts": {}}
mism = []
# primal chart P
ns = driver_ns("cert_primal_v3.py", [RUN, C + "spec_primal_P_v1.json"])
boxes = sample_boxes("P", 120)
for rec, box in boxes:
    o = ns["classify"](box)
    if o != rec:
        mism.append(("P", rec, o, [[str(a), str(b)] for a, b in box]))
cells = []
spec = json.load(open(C + "spec_primal_P_v1.json"))
reg = [(Qs(spec["region"][k][0]), Qs(spec["region"][k][1])) for k in ("r", "w", "phi")]
ns_ = [spec["initial_split"][k] for k in ("r", "w", "phi")]
for i in range(0, ns_[0], 3):
    for j in range(0, ns_[1], 11):
        for k in range(0, ns_[2], 9):
            idx = (i, j, k)
            cells.append(tuple((reg[d][0] + (reg[d][1] - reg[d][0]) * idx[d] / ns_[d],
                                reg[d][0] + (reg[d][1] - reg[d][0]) * (idx[d] + 1) / ns_[d]) for d in range(3)))
for cell in cells:
    ns["classify"](cell)
report["charts"]["P"] = {"sample_leaves": len(boxes), "initial_cells": len(cells)}
# dual charts
for chart, drv, specf in [("G", "cert_dual_v5.py", "spec_dual_v1.json"), ("SWB", "cert_dual_v5.py", "spec_dual_v1.json"),
                          ("LW", "cert_dual_v5.py", "spec_dual_v1.json"), ("LD1", "cert_dual_v5.py", "spec_dual_v1.json"),
                          ("LD2", "cert_dual_v5.py", "spec_dual_v1.json"), ("SWC", "cert_dual_v7.py", "spec_dual_v3.json")]:
    ns = driver_ns(drv, [RUN, C + specf, chart])
    boxes = sample_boxes(chart, 120)
    for rec, box in boxes:
        ok, tag = ns["evaluate"](box)
        o = (tag if tag.startswith("SKIP") else "CERT:" + tag) if ok else "FAIL:" + tag
        if o != rec:
            mism.append((chart, rec, o, [[str(a), str(b)] for a, b in box]))
    bps = ns["bps"]
    cl = [((bps[0][a], bps[0][a + 1]), (bps[1][b], bps[1][b + 1]), (bps[2][c], bps[2][c + 1]))
          for a in range(len(bps[0]) - 1) for b in range(len(bps[1]) - 1) for c in range(len(bps[2]) - 1)]
    cl = cl[::max(1, len(cl) // 60)][:60]
    for cell in cl:
        ns["evaluate"](cell)
    report["charts"][chart] = {"driver": drv, "spec": specf, "sample_leaves": len(boxes), "initial_cells": len(cl)}

flags = {}
for sid, cnt in TRACE.items():
    bad = []
    for (lt, rt, res), k in cnt.items():
        op = sid.rsplit(":", 1)[1]
        if "float" in (lt, rt, res) or "complex" in (lt, rt, res):
            bad.append([lt, rt, res, k])
        elif op == "Div" and lt == "int" and rt == "int":
            bad.append([lt, rt, res, k])
    if bad:
        flags[sid] = {"segment": SEG.get(sid), "bad_type_triples": bad}
exercised = {sid: {"segment": SEG[sid], "types": sorted([list(t) + [k] for t, k in cnt.items()])}
             for sid, cnt in TRACE.items()}
unexercised = sorted(sid for sid in SEG if sid not in TRACE)
report.update({"traced_sites": len(SEG), "exercised_sites": len(exercised), "unexercised_sites": unexercised,
               "flagged_sites": flags, "outcome_mismatches": mism, "exercised": exercised})
with lane_guard.xopen(RUN + "/trace.json") as fh:
    json.dump(report, fh, indent=0, sort_keys=True)
print(json.dumps({"traced_sites": len(SEG), "exercised": len(exercised), "unexercised": len(unexercised),
                  "flagged": {k: v["segment"] for k, v in flags.items()}, "outcome_mismatches": len(mism),
                  "charts": report["charts"]}, indent=1))
