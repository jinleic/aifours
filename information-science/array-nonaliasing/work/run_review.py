"""Obtain a tool-free hostile review of the frozen complete public proof."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=2400)
    args = parser.parse_args()
    proof = HERE / "evidence/reviewed-proof.txt"
    models_path = Path("/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json")
    config = json.loads(models_path.read_text())["claude"]
    files = [proof, *sorted((HERE / "sources").iterdir())]
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in files if p.is_file()}
    prompt = """You are a hostile independent mathematical referee. No tools, browsing,
filesystem access, external contact, code execution or further delegation. All context is
embedded below. Audit every quantifier, proof, finite bound, algebraic termination claim,
zero-gain case and claimed scope. Independently derive both rational examples. The question
is whether the isotropic book reading is SOLVED-BY-PRIOR-WORK, and whether two published
shortcuts are false as stated. Do not approve merely because the examples look plausible.
Return ONLY JSON with keys verdict (ACCEPT/REVISE/REJECT), theorem_assessment,
independent_example_derivations, findings (list of objects with id, severity, location,
issue, required_change), prior_art_scope, and limitations. Correctness is separate from
novelty. We do not claim Lean verification. Code is not included; this is a proof review.
Return at most 1200 words of JSON. Focus on substantive mathematical defects; do not
restate the full proof. A finite complete review, not open-ended research, is required.

Primary source inspected: Tucker, Zhao, Ahmad, Potter, Alias-Free Arrays, IEEE SPL 29
(2022) 2457-2461, DOI 10.1109/LSP.2022.3224834, PMC9757818. It assumes rank(P)=d,
P=pi D, and defines Lambda={x:Px=0 mod 2pi}. In its Section III.B a nontrivial full-rank
lattice is assumed. Proposition 3: alias-free on B iff translates B+u_i,B+u_j are disjoint
for all distinct lattice points. Corollary 4: alias-free on its full physical direction
domains iff smallest nonzero lattice norm is greater than 2.
VERBATIM Corollary 5: 'An array with lattice basis V is alias-free if and only if the
vertices of the parallelepiped defined by V are separated by more than 2.' Its sufficiency
proof states: 'the union of all 2^d parallelepipeds of the shape Omega and having one
vertex at the origin will guarantee cover of the nonzero lattice point with the smallest
norm.' Section IV.B: 'For any basis V', C contains binary columns 1,...,2^d-1, and
Eq. (11) is min sqrt(diag(C^T V^T V C))>2, asserted equivalent to Corollary 4.
Kastinen-Kero, AMT 13 (2020), 6813-6835, DOI 10.5194/amt-13-6813-2020, Section 2.1,
defines arbitrary complex gain steering responses, normalizes by norm, and calls distinct
nonzero responses perfectly ambiguous when their absolute normalized Hermitian inner
product equals one. It uses numerical scattered gradient searches, not exact global
certification. Godara-Cantoni DOI 10.1121/1.386790 primary abstract and author metadata
were opened; original full theorem text was inaccessible. The 2022 article explicitly
attributes the original N&S integer-image test to 1981 Theorem 6.

SOURCE HASH BINDINGS:\n""" + json.dumps(hashes, indent=2) + "\n\nCOMPLETE PROOF:\n" + proof.read_text()
    prompt_path = args.output.with_suffix(".prompt.txt")
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt)
    command = ["claude", "--model", config["model"], "--effort", config["effort"],
               "--safe-mode", "--no-chrome", "--tools", "", "--permission-mode", "dontAsk",
               "--no-session-persistence", "--output-format", "json", "-p", prompt]
    started = time.monotonic()
    try:
        result = subprocess.run(command, cwd=HERE, stdin=subprocess.DEVNULL,
                                capture_output=True, text=True, timeout=args.timeout)
    except subprocess.TimeoutExpired as error:
        for suffix, data in ((".stdout.json", error.stdout), (".stderr.txt", error.stderr)):
            if isinstance(data, bytes):
                data = data.decode(errors="replace")
            args.output.with_suffix(suffix).write_text(data or "")
        args.output.write_text(json.dumps({
            "status": "TIMEOUT_NO_VERDICT", "requested_model": config["model"],
            "requested_effort": config["effort"], "source_sha256": hashes,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "duration_seconds": time.monotonic() - started,
        }, indent=2) + "\n")
        raise SystemExit("Reviewer timed out; partial output preserved; no verdict accepted")
    args.output.with_suffix(".stdout.json").write_text(result.stdout)
    args.output.with_suffix(".stderr.txt").write_text(result.stderr)
    if result.returncode:
        raise SystemExit(f"Reviewer exited {result.returncode}; preserved raw output")
    events = json.loads(result.stdout)
    if isinstance(events, dict):
        events = [events]
    finals = [e for e in events if e.get("type") == "result"]
    if not finals or finals[-1].get("subtype") != "success" or finals[-1].get("is_error", False):
        raise SystemExit("No successful final review result")
    final = finals[-1]
    text = final["result"].strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    review = json.loads(text)
    receipt = {"requested_model": config["model"], "requested_effort": config["effort"],
               "reported_init_models": [e.get("model") for e in events if e.get("type") == "system"],
               "reported_model_usage": final.get("modelUsage", {}), "source_sha256": hashes,
               "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
               "duration_seconds": time.monotonic() - started, "returncode": result.returncode,
               "review": review}
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "verdict": review["verdict"],
                      "findings": len(review.get("findings", []))}))


if __name__ == "__main__":
    main()
