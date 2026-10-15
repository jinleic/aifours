#!/usr/bin/env python3
"""Run the requested other-vendor mathematical review of a hash-bound snapshot."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--previous", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    workspace = Path("/Users/jinleic/jinleic-workspace")
    models = json.loads((workspace / "docs/knowledge-system/DELEGATE_MODELS.json").read_text())
    inputs = [root / "proof.md", root / "sources/problem.zh-en.txt"]
    if args.previous is not None:
        inputs.append(args.previous.resolve())
        inputs.extend([root / "evidence/referee-dispositions.json",
                       root / "sources/status.json", root / "evidence/check.json",
                       root / "evidence/supplement-access.json"])
    hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    prompt = """You are a hostile independent mathematical referee, not a collaborator seeking acceptance. Do not use tools, do not delegate, do not edit anything. Review the complete proof below, including exact book excerpts. The main question demands strong stability (finite time-average expected total backlog) with an arbitrary interference graph, every strictly admissible load, and local queue/channel distributed random access.

Theorem 1 treats synchronous block fading. Theorem 2 is a substantive extension to continuously changing finite-state Markov channels, including channel jumps during both control and data service. Both make substantial architecture assumptions: perfect instantaneous sensing/switching, synchronized slot sampling, and deterministic time-inhomogeneous clocks R_t=exp((t+1)^2). Theorem 2 runs clocks throughout the slot, pays initial control overhead delta_t=1/(t+2), and permits no positive later switching delay. We explicitly classify the book as PARTIAL.

Do NOT excuse a flaw merely because this is a partial result. Check all mathematical bridges, especially the all-zero reset coupling event, entropy/TV loss, uniform-in-time constants, conditional independence after conditioning on the channel path, the no-jump window argument (C2)-(C5), integration of actual continuous-time service, both Poisson equations, quadratic drift constants, and conversion to a uniform exponential moment. Check the six-state counterexample and deterministic bounded-arrival cycle formula. Check whether any hidden central oracle/global queue max is used, and whether the scope caveat is strong enough. Distinguish a valid but deliberately impractical scoped theorem from a full book solution. If a previous review is included, first check any prior findings, then fully audit the added continuous-channel theorem; acceptance of the old theorem is not acceptance of the extension.

Return ONLY one JSON object with keys: verdict (ACCEPT_SCOPED, NEEDS_FIX, or REJECT), exact_accepted_claim (string), findings (array of objects with id,severity,location,issue,required_fix), scope_assessment (string), novelty_assessment (string), and first_independent_check (string). Do not claim to have executed computations. Any absent source is unverified.

"""
    prompt += "BOUND INPUT SHA256:\n" + json.dumps(hashes, indent=2) + "\n\n"
    for path in inputs:
        prompt += "===== " + str(path.relative_to(root)) + " =====\n" + path.read_text() + "\n\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    prompt_path = args.output.with_suffix(".prompt.txt")
    raw_path = args.output.with_suffix(".raw.json")
    stderr_path = args.output.with_suffix(".stderr.txt")
    prompt_path.write_text(prompt)
    command = ["claude", "--model", models["claude"]["model"], "--effort", models["claude"]["effort"],
               "--safe-mode", "--no-chrome", "--tools", "", "--permission-mode", "dontAsk",
               "--no-session-persistence", "--output-format", "json", "-p", prompt]
    start = time.time()
    env = os.environ.copy()
    env.update({"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1"})
    with raw_path.open("w") as stdout, stderr_path.open("w") as stderr:
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                cwd=root, env=env, timeout=2400, check=False)
    receipt = {"source_hashes": hashes, "requested_model": models["claude"],
               "returncode": result.returncode, "elapsed_seconds": round(time.time() - start, 3),
               "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
               "prompt": str(prompt_path), "raw": str(raw_path), "stderr": str(stderr_path)}
    if result.returncode:
        receipt["status"] = "CLI_FAILED"
    else:
        raw = json.loads(raw_path.read_text())
        events = raw if isinstance(raw, list) else [raw]
        finals = [e for e in events if e.get("type") == "result"]
        final = finals[-1] if finals else {}
        receipt["init_models"] = [e.get("model") for e in events if e.get("type") == "system" and e.get("subtype") == "init"]
        receipt["model_usage"] = final.get("modelUsage", {})
        receipt["final_subtype"] = final.get("subtype")
        receipt["is_error"] = final.get("is_error")
        receipt["result_text"] = final.get("result", "")
        success = final.get("subtype") == "success" and final.get("is_error") is False
        receipt["status"] = "SUCCESS" if success else "RESULT_FAILED"
        if success:
            text = receipt["result_text"].strip()
            if text.startswith("```"):
                text = text[text.index("\n") + 1:text.rfind("```")].strip()
            receipt["review"] = json.loads(text)
    args.output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": receipt["status"], "output": str(args.output),
                      "verdict": receipt.get("review", {}).get("verdict"),
                      "elapsed_seconds": receipt["elapsed_seconds"]}))
    if receipt["status"] != "SUCCESS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
