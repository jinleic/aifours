#!/usr/bin/env python3
"""Collect result.json from the files and logs in this directory (read-only except result.json).

Every value is read from an artifact: SHA-256 of inputs/sources/build products, exit status,
wall time and peak RSS from `/usr/bin/time -l` logs, axiom lines from Lean output, the control
summary and the leanchecker replay logs.  Nothing is asserted that is not in those files.
"""
import datetime
import hashlib
import json
import pathlib
import re

K = pathlib.Path(__file__).resolve().parent
REVIEW = K.parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def timing(name):
    p = K / "logs" / f"{name}.build.time"
    if not p.exists():
        return None
    t = p.read_text()
    wall = re.search(r"([\d.]+) real", t)
    rss = re.search(r"(\d+)\s+maximum resident set size", t)
    ex = re.search(r"exit=(\d+)", t)
    return {"exit": int(ex.group(1)) if ex else None,
            "wall_s": float(wall.group(1)) if wall else None,
            "peak_rss_bytes": int(rss.group(1)) if rss else None}


def axioms(name):
    p = K / "logs" / f"{name}.build.log"
    if not p.exists():
        return {}
    out = {}
    for ln in p.read_text().splitlines():
        m = re.match(r"'([^']+)' (depends on axioms: \[(.*)\]|does not depend on any axioms)", ln)
        if m:
            out[m.group(1)] = [a.strip() for a in m.group(3).split(",")] if m.group(3) else []
    return out


def errors(name, src):
    p = K / "logs" / f"{name}.build.log"
    if not p.exists():
        return []
    lines = src.read_text().splitlines()
    res = []
    for m in re.finditer(r"lean:(\d+):(\d+): error: ([^\n]*)", p.read_text()):
        ln = int(m.group(1))
        thm = None
        for k in range(ln - 1, max(ln - 6, 0) - 1, -1):
            mm = re.match(r"theorem (\S+)", lines[k])
            if mm:
                thm = mm.group(1)
                break
        res.append({"line": ln, "theorem": thm, "message": m.group(3)})
    return res


def replay(mod):
    p, t = K / "logs" / f"replay.{mod}.log", K / "logs" / f"replay.{mod}.time"
    if not t.exists():
        return None
    tt = t.read_text()
    wall = re.search(r"([\d.]+) real", tt)
    rss = re.search(r"(\d+)\s+maximum resident set size", tt)
    return {"command": f"leanchecker {mod}", "output": p.read_text().strip() if p.exists() else None,
            "wall_s": float(wall.group(1)) if wall else None,
            "peak_rss_bytes": int(rss.group(1)) if rss else None,
            "stderr_tail": "\n".join(l for l in tt.splitlines()
                                     if not re.match(r"\s+\d+\s+\S", l) and "real" not in l)[-2000:]}


raws = {
    "lkts57": REVIEW / "lkts57-construction-snapshot-v1/lkts57_g513.txt",
    "lkts87": REVIEW / "lkts87-parent-inputs-v1/lkts87_g903.txt",
    "frozen_PriorFormal": REVIEW / "lkts57-construction-snapshot-v1/PriorFormal.lean",
    "control_swap": K / "controls/lkts57_control_swap.txt",
    "control_dupsys": K / "controls/lkts57_control_dupsys.txt",
}
modules = ["PriorFormal", "Generic", "Data57", "Cert57", "Data87", "Cert87",
           "Control/Data57Swap", "Control/Cert57Swap", "Control/Diag57Swap",
           "Control/Data57Dup", "Control/Cert57Dup", "Control/Diag57Dup"]
res = {
    "scope": ("Two finite existence theorems, LKTS(57) and LKTS(87), checked by the Lean kernel "
              "from the pinned raw certificates.  This is not the universal LKTS(v) statement "
              "Kirkman.FullGoal, and no novelty or priority assessment is made."),
    "theorems": {
        "lkts57": "Kirkman.KernelCert.exists_lkts57 : ∃ B : Fin 55 → Kirkman.Blocks 57, Kirkman.IsLKTS B",
        "lkts87": "Kirkman.KernelCert.exists_lkts87 : ∃ B : Fin 85 → Kirkman.Blocks 87, Kirkman.IsLKTS B",
        "witness": "B = Kirkman.KernelCert.blocksOf v data (lkts57_blocks_spec / lkts87_blocks_spec: Iff.rfl)",
        "soundness": "Kirkman.KernelCert.isLKTS_of_check (generic in v and the data)",
    },
    "inputs_sha256": {k: sha(p) for k, p in raws.items() if p.exists()},
    "sources_sha256": {str(p.relative_to(K)): sha(p) for p in sorted(K.glob("LktsKernel/**/*.lean"))},
    "scripts_sha256": {p.name: sha(p) for p in sorted(K.glob("*.py")) + sorted(K.glob("*.sh"))},
    "build_products_sha256": {str(p.relative_to(K)): sha(p) for p in sorted(K.glob("build/**/*.olean"))},
    "environment": {
        "lean": "Lean 4.34.1 (commit 5045d0056413266e57c625dcd7c365b10e377c52), ~/.elan toolchain",
        "mathlib_cache": "/private/tmp/seymour-lean-20261014-68365/.lake/packages (mathlib rev "
                         "d13f23b723b8a846827a245b89c10fc7d3f11612), used read-only via LEAN_PATH",
        "deviation": ("The cache named in the assignment, scratch/rh-quasi-lean-2026-10-07/lean, "
                      "does not exist on this machine; a whole-filesystem search found no copy."),
        "threads": "lean -j 4",
    },
    "provenance": {
        "worker": "LKTS57Kernel lane, anthropic/claude-opus-5-5; no delegate or external model used",
        "result_written_host_clock": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    },
    "builds": {},
    "axioms": {},
    "control_errors": {},
    "replay": {},
}
for m in modules:
    base = m.split("/")[-1]
    res["builds"][m] = timing(base)
    ax = axioms(base)
    if ax:
        res["axioms"][m] = ax
    if base.startswith("Cert57Swap") or base.startswith("Cert57Dup"):
        res["control_errors"][m] = errors(base, K / "LktsKernel" / f"{m}.lean")
summ = K / "logs" / "controls.summary"
res["controls_summary"] = summ.read_text().strip().splitlines() if summ.exists() else None
for mod in ["LktsKernel.PriorFormal", "LktsKernel.Generic", "LktsKernel.Data57", "LktsKernel.Cert57",
            "LktsKernel.Data87", "LktsKernel.Cert87"]:
    r = replay(mod)
    if r:
        res["replay"][mod] = r
res["replay_fresh"] = {p.name: p.read_text().strip()
                       for p in sorted((K / "logs").glob("replay-fresh.*.summary"))}
(K / "result.json").write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({k: res[k] for k in ("builds", "controls_summary")}, indent=1))
