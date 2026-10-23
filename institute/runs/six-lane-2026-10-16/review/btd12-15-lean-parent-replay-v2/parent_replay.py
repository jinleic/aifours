#!/usr/bin/python3
"""Parent replay of the BTD(12,15;6,2,10;8,6) Lean development (stdlib only).

Steps: verify source pins against the worker manifest, run the parent's own forbidden-token scan, build the three
worker modules and the parent-authored ParentAudit.lean (fresh build dir), require the four parent negative controls
to FAIL with a type mismatch, run `leanchecker --fresh` on ParentAudit, and parse the `#print axioms` output.
Refuses to overwrite parent-result.json. One Lean process at a time; no timeouts/kills (Lean runs to completion).
"""
import hashlib, json, os, re, subprocess, sys, time
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "parent-result.json")
if os.path.exists(OUT) or os.path.exists(os.path.join(HERE, "build")):
    sys.exit("refusing: parent-result.json or build/ already exists")

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def now():
    return datetime.now().astimezone().isoformat()

res = {"started_at_pt": now(), "steps": [], "supersedes": "btd12-15-lean-parent-replay-v1 (retained): its driver matched lowercase 'type mismatch' but Lean 4.34.1 prints 'Type mismatch', so it stopped before the fresh kernel check; all v1 builds/negatives/axioms otherwise behaved as intended."}
wm = json.load(open(os.path.join(HERE, "worker-manifest.json")))["files"]
srcs = ["BTDKernel/Target.lean", "BTDKernel/Proof.lean", "BTDKernel/Audit.lean"]
res["source_pins"] = {s: sha(os.path.join(HERE, s)) for s in srcs}
res["pins_match_worker_manifest"] = all(res["source_pins"][s] == wm[s] for s in srcs)
parent_files = ["ParentAudit.lean", "NegLambdaFive.lean", "NegColSumSeven.lean", "NegThreeTwos.lean",
                "NegThirteenRows.lean", "lean_env.sh", "build_module.sh", "parent_replay.py"]
res["parent_file_sha256"] = {p: sha(os.path.join(HERE, p)) for p in parent_files}

FORBIDDEN = [r"\bsorry\b", r"\badmit\b", r"native_decide", r"ofReduceBool", r"ofReduceNat", r"implemented_by",
             r"\bextern\b", r"\bunsafe\b", r"^\s*axiom\b", r"\bopaque\b", r"csimp", r"\bmacro\b", r"\bsyntax\b",
             r"\belab\b", r"\bnotation\b", r"run_cmd", r"#eval", r"skipKernelTC", r"import\s+Lean\b",
             r"debug\.", r"Lean\.Elab"]
scan = {}
for s in srcs + ["ParentAudit.lean"]:
    text = open(os.path.join(HERE, s), encoding="utf-8").read().split("\n")
    hits = [(i + 1, pat) for i, line in enumerate(text) for pat in FORBIDDEN if re.search(pat, line)]
    opts = [(i + 1, line.strip()) for i, line in enumerate(text) if "set_option" in line]
    imps = [line.strip() for line in text if line.startswith("import ")]
    scan[s] = {"forbidden_hits": hits, "set_options": opts, "imports": imps}
res["scan"] = scan

def run(name, cmd, expect_fail=False):
    t0 = time.time()
    p = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
    step = {"name": name, "command": cmd, "exit_code": p.returncode, "wall_seconds": round(time.time() - t0, 3),
            "stdout_tail": p.stdout[-1500:], "stderr_tail": p.stderr[-1500:]}
    res["steps"].append(step)
    with open(os.path.join(HERE, "steps.jsonl"), "a") as f:
        f.write(json.dumps({"at": now(), **{k: step[k] for k in ("name", "exit_code", "wall_seconds")}}) + "\n")
    return p

ok = res["pins_match_worker_manifest"] and not any(v["forbidden_hits"] for v in scan.values())
for m in srcs + ["ParentAudit.lean"]:
    if ok:
        ok = run("build-" + m, ["sh", "build_module.sh", m]).returncode == 0
logs = os.path.join(HERE, "logs")
res["negatives"] = {}
if ok:
    for n in ["NegLambdaFive", "NegColSumSeven", "NegThreeTwos", "NegThirteenRows"]:
        p = run("negative-" + n, ["sh", "build_module.sh", n + ".lean"], expect_fail=True)
        log = open(os.path.join(logs, n + ".build.log"), encoding="utf-8", errors="replace").read()
        res["negatives"][n] = {"exit_code": p.returncode, "type_mismatch_reported": "type mismatch" in log.lower(),
                               "olean_written": os.path.exists(os.path.join(HERE, "build", n + ".olean"))}
    ok = all(v["exit_code"] != 0 and v["type_mismatch_reported"] for v in res["negatives"].values())
if ok:
    p = run("fresh-ParentAudit", ["sh", "-c", '. ./lean_env.sh; exec /usr/bin/time -l "$LEANCHECKER" --fresh -v ParentAudit'])
    res["fresh_output_tail"] = (p.stdout + p.stderr)[-3000:]
    ok = p.returncode == 0
alog = os.path.join(logs, "ParentAudit.build.log")
axioms = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", open(alog).read()) if os.path.exists(alog) else []
res["axioms"] = {k: [a.strip() for a in v.split(",")] for k, v in axioms}
allowed = {"propext", "Classical.choice", "Quot.sound"}
res["axioms_ok"] = (set(res["axioms"]) == {"ParentBtdAudit.no_btd", "ParentBtdAudit.small_exists"}
                    and all(set(v) <= allowed for v in res["axioms"].values()))
res["status"] = "PARENT_BTD_LEAN_BINDING_REBUILD_AND_FRESH_KERNEL_PASS" if ok and res["axioms_ok"] else "FAIL"
res["finished_at_pt"] = now()
res["limits"] = ("Same Lean 4.34.1 kernel implementation for lean and leanchecker; Mathlib from the read-only "
                 "prebuilt cache; not Comparator, not an independent external kernel.")
with open(OUT, "x") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(res["status"])
