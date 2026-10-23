#!/usr/bin/env python3
"""Run CPro1's own CFR acceptance predicate (problem_def.v with utils.parsesoltext), extracted by AST from
the commit-pinned upstream files (Apache-2.0, Constructive-Codes/CPro1 @ 827f02b4), on the parent-pinned
CFR(5,27) raws and on parent control fixtures. Only the three named function definitions are executed."""
import ast, hashlib, json, os, re, time, types
HERE = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cfr27-cpro1-predicate-v1"
REV = os.path.dirname(HERE)
PIN = {"problem_def.py": "44f4d4ff86757bd221a4875a8e84d3d5195deb483dcde1119154bfc901bf70aa",
       "utils.py": "b4f7c66df6e70959244816aa9eef042b8719e5f8939110c569fd30ec99099c26"}
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
src = {}
for k, h in PIN.items():
    b = open(HERE + "/upstream/" + k, "rb").read()
    assert hashlib.sha256(b).hexdigest() == h, k
    src[k] = b.decode()
def extract(text, names):
    tree = ast.parse(text)
    got = {n.name: ast.get_source_segment(text, n) for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names}
    assert sorted(got) == sorted(names), got.keys()
    return got
u = extract(src["utils.py"], ["parsesoltext"])
p = extract(src["problem_def.py"], ["getsol", "v"])
uns = {"re": re}
exec(u["parsesoltext"], uns)
utils = types.SimpleNamespace(parsesoltext=uns["parsesoltext"])
pns = {"utils": utils}
exec(p["getsol"], pns); exec(p["v"], pns)
v = pns["v"]
cases = []
for name in ["A-CFR", "B-CFR"]:
    path = REV + "/cfr27-parent-inputs-v1/" + name + ".raw"
    cases.append({"case": name, "sha256": sha(path), "expect": True, "v": v(open(path).read(), [5, 27])})
ctl = REV + "/cfr27-parent-controls-v1"
for fn in sorted(os.listdir(ctl)):
    if not fn.endswith(".raw"):
        continue
    meta = json.load(open(ctl + "/" + fn[:-4] + ".json"))
    if meta["kind"] != "cfr":
        continue
    path = ctl + "/" + fn
    cases.append({"case": meta["case"], "sha256": sha(path), "expect": meta["status"] == "PASS",
                  "parent_category": meta.get("actual_category"), "v": v(open(path).read(), [5, 27])})
for c in cases:
    c["agree"] = c["v"] == c["expect"]
res = {"upstream": {k: {"sha256": h, "url": "https://raw.githubusercontent.com/Constructive-Codes/CPro1/827f02b4048fc96a6b79f0970c87ca5a54f31f40/CPro1/" +
                         ("design_definitions/circular-florentine-rectangle/" if k == "problem_def.py" else "code/") + k} for k, h in PIN.items()},
       "license": "Apache-2.0 (GitHub API spdx_id at fetch)", "executed_functions": ["utils.parsesoltext", "problem_def.getsol", "problem_def.v"],
       "runner_sha256": sha(__file__), "cases": cases, "n": len(cases), "n_agree": sum(c["agree"] for c in cases),
       "finished": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
with open(HERE + "/result.json", "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps({k: res[k] for k in ("n", "n_agree", "finished")}), [(c["case"], c["v"], c["expect"]) for c in cases if not c["agree"] or c["case"] in ("A-CFR", "B-CFR")])
