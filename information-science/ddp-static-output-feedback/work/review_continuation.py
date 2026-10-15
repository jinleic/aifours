"""Retain a narrowly scoped, no-tools independent mathematical review."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = Path("/Users/jinleic/jinleic-workspace")
OUT = ROOT / "evidence" / "continuation"
MODELS = WORKSPACE / "docs/knowledge-system/DELEGATE_MODELS.json"


def main():
    model = json.loads(MODELS.read_text())["claude"]
    proof = (ROOT / "work/continuation-structural.md").read_text()
    prompt = """Act as a hostile independent mathematical referee, not a coauthor.
Review ONLY the supplied mathematical manuscript. No tools, filesystem reads,
network access, code execution, delegation, or proposed edits. Do not claim any
checks you did not perform. Identify a concrete counterexample or missing step
whenever possible. This is not a request to solve a different special case.

Audit: (1) the Cauchy-Binet/bordered determinant signs, dimensions, arbitrary
feedthrough and nonminimal realization; (2) complete big-chart coverage of every
finite real K, absence of false implicit controllers; (3) the arbitrary-order
m=p=2 unstabilized ONE-quadric theorem, every degenerate case and all-gain
parameterization; (4) strict full-state Hurwitz handling; (5) continuum plant,
unique admissible V, finite fixed-V/affine-family impossibility and claimed
irreducibility under Chen's reductions; (6) real-infeasible four-state example;
(7) whether the contribution is genuinely additional to an unknown-V rank test
or merely algebraic restatement, and whether the restricted/not-novel/full-book
verdict is honest. Source comparisons in the manuscript are evidence supplied
by the author, not sources you have independently read.

Return JSON as ordinary text (no enforced output schema), with fields verdict,
claims (array of id/status/reason), critical_findings, required_corrections,
novelty_scope, unverified_items. A conditional acceptance must name each missing
condition. Spend effort on the proof, not formatting. No further delegation.

MANUSCRIPT:\n""" + proof
    (OUT / "claude-review-prompt.txt").write_text(prompt)
    command = ["claude", "--model", model["model"], "--effort", model["effort"],
               "--safe-mode", "--no-chrome", "--tools", "",
               "--permission-mode", "dontAsk", "--no-session-persistence",
               "--output-format", "json", "-p", prompt]
    started = time.monotonic()
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                            timeout=900, env={**os.environ, "OMP_NUM_THREADS": "1",
                                              "OPENBLAS_NUM_THREADS": "1"})
    (OUT / "claude-review-output.json").write_text(result.stdout)
    (OUT / "claude-review-stderr.txt").write_text(result.stderr)
    receipt = {"command": command[:-1] + ["<contents of claude-review-prompt.txt>"],
               "cwd": str(ROOT), "model_configuration": model,
               "proof_sha256": hashlib.sha256(proof.encode()).hexdigest(),
               "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
               "returncode": result.returncode,
               "elapsed_seconds": round(time.monotonic()-started, 3),
               "tools": "none", "source_audit": "not delegated"}
    (OUT / "claude-review-receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps(receipt, indent=2))
    if result.returncode:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
