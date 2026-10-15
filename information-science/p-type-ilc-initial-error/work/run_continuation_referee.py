"""Run an isolated other-vendor proof review with the proof embedded in context."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--rectification", action="store_true")
parser.add_argument("--rational-focused", action="store_true")
options = parser.parse_args()
OUT = ROOT / "evidence/continuation"
if options.rectification:
    OUT = OUT / "rectification-review"
elif options.rational_focused:
    OUT = OUT / "rational-focused-review"
OUT.mkdir(parents=True, exist_ok=True)
settings = json.loads((WORKSPACE / "docs/knowledge-system/DELEGATE_MODELS.json").read_text())["claude"]
proof_path = ROOT / ("work/rectification-boundary.md" if options.rectification else "work/continuation-theorems.md")
proof = proof_path.read_text()
prompt = """Act as a hostile mathematical referee. You are the independent other-vendor reviewer, not an implementer. Use ONLY the mathematical text embedded below. No tools, filesystem reads, web access, writes, or further delegation. Do not evaluate novelty from memory. Return a focused, self-contained mathematical review with theorem-level verdicts, actual counterexamples if any, and precise repairs. Audit every quantifier and especially: the rational learner class; analytic continuation past interior poles; whether nominal convergence forces K to have a pole at one; all q,m boundary approaches including q=m=1; the single bounded infinite adversary; forgetting residual; nonlinear coordinate witnesses; and why compact-inverse impossibility is only about input reconstruction. Distinguish proof gaps from presentation improvements. The user wants a wider-class obstruction rather than repeating failure of one constant-gain law. Identify any overclaim about time-varying gains, MIMO, nonlinear controllers, or the original unresolved problem. No need to reproduce all calculations if correct. Final answer must say whether each claimed theorem is correct under the stated assumptions.\n\nBEGIN MATHEMATICAL TEXT\n""" + proof + "\nEND MATHEMATICAL TEXT\n"
if options.rectification:
    old = (ROOT / "work/theorems.md").read_text()
    theorem_b = old.split("## 3. Theorem B:", 1)[1].split("## 4. Theorem C:", 1)[0]
    prompt = """Act as an independent hostile mathematical referee, not an implementer. Use ONLY the mathematical text embedded below. No tools, external reads, web access, writes, or further delegation. Do not judge novelty from memory. Audit F1 and F2 independently: the exact rectified-error recurrence; Bessel integral bound and gamma powers; uniformity at t=0; summable delayed quadratic; nominal convergence for every continuous feasible input; fixed-start tail conclusion; and the common-initial-interval, continuous-noise, single-infinite-sequence quantifiers in F2. Check that this is neither a finite-basis/full-state design nor a claim of full arbitrary-noise robustness. The needed prior pure-P theorem is embedded too. Return theorem-level verdicts and only substantive objections/corrections, with enough derivation to explain any objection.\\n\\nBEGIN NEW PROOF\\n""" + proof + "\\nEND NEW PROOF\\n\\nBEGIN PRIOR THEOREM B\\n" + theorem_b + "\\nEND PRIOR THEOREM B\\n"
if options.rational_focused:
    prompt = (ROOT / "evidence/continuation/rational-focused.prompt.txt").read_text()
(OUT / "claude-referee.prompt.txt").write_text(prompt)
args = ["claude", "--model", settings["model"], "--effort", settings["effort"],
        "--safe-mode", "--no-chrome", "--tools", "", "--permission-mode", "dontAsk",
        "--no-session-persistence", "--output-format", "json", "-p", prompt]
started = time.time()
with (OUT / "claude-referee.stdout.json").open("w") as stdout, (OUT / "claude-referee.stderr.txt").open("w") as stderr:
    result = subprocess.run(args, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                            cwd=OUT, timeout=1800, env={**os.environ, "OMP_NUM_THREADS": "1"})
metadata = {"command": "python3 work/run_continuation_referee.py" + (" --rectification" if options.rectification else " --rational-focused" if options.rational_focused else ""), "argv_without_prompt": args[:-1],
            "proof_sha256": hashlib.sha256(proof.encode()).hexdigest(), "seconds": time.time()-started,
            "returncode": result.returncode, "model_requested": settings, "proof_path": str(proof_path),
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()}
if result.returncode == 0:
    data = json.loads((OUT / "claude-referee.stdout.json").read_text())
    events = data if isinstance(data, list) else [data]
    final = [event for event in events if event.get("type") == "result"][-1]
    metadata["modelUsage"] = final.get("modelUsage")
    metadata["subtype"] = final.get("subtype")
    metadata["is_error"] = final.get("is_error")
    (OUT / "claude-referee.txt").write_text(final.get("result", ""))
    assert final.get("subtype") == "success" and not final.get("is_error"), final
(OUT / "claude-referee-run.json").write_text(json.dumps(metadata, indent=2)+"\n")
print(json.dumps(metadata, indent=2))
raise SystemExit(result.returncode)
