#!/usr/bin/env python3
"""Run the explicitly requested read-only hostile referee and bind its inputs."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = Path('/Users/jinleic/jinleic-workspace/scratch/ai4s-positive-tfd-marginals')
PROMPT = f"Act as a hostile mathematical referee. Read ONLY files inside your working directory {ROOT}." """ Do not delegate, browse externally, modify anything, or read any other local path. Review proof.md, README.md, sources/references.md and the source page images/text as needed. Check EVERY proof step, quantifier, integrability hypothesis, Fourier sign/normalization, the distinction between joint measures and densities, and faithfulness to the literal Chinese book question. In particular scrutinize the finite-energy analytic negative-IF witness; the explicit L=129 analytic GD cutoff construction and each rational bound; the Strassen kernel lifting; the Fourier covariance identity; the rational and smooth-density two-regression counterexamples; the Wigner and quadratic-rule proofs. Check prior-art claims only against provided primary text, not unsupported memory. Return numbered findings with severity (fatal/major/minor), precise locations, evidence and proposed correction. Distinguish genuine mathematical errors from missing novelty clearance. End with a verdict on which formal readings are completely settled and whether the unrestricted book question is solved. No filler. The assignment expressly requires classical written proofs, not Lean; absence of Lean must be disclosed but is not itself an error."""


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--round', type=int, choices=(1, 2, 3, 4), default=1)
    args = parser.parse_args()
    prefix = 'codex-referee' if args.round == 1 else f'codex-referee-{args.round}'
    prompt = PROMPT
    if args.round == 2:
        prompt += """ This is a focused second review. Read evidence/codex-referee.md first. Check that both minor findings are fixed. Then verify the newly added analytic-subspace extension in Theorem 8, and audit work/check_exact.py plus evidence/exact-checks.json against the mathematical constraints (read only; do not run code). The remaining theorems were accepted in round 1; revisit only if a real issue arises. Verify README's new computational claims and metadata caveats. Return any remaining numbered findings, or explicitly state none."""
    if args.round == 3:
        prompt = f"Act as a hostile mathematical referee. Read ONLY inside {ROOT};" """ do not browse, delegate, modify files, or execute project code. This continuation asks whether an exact one-conditional-mean DENSITY criterion, applicable to genuine Fourier marginals, closes a gap left in the previous accepted results. Focus on proof.md SECTION 9, Theorem9 and Corollary9.1. Independently verify necessity via countably many contact barriers, the assertion nu(I)=1 using atomlessness, existence of the adaptive countable interval partition, the intermediate discrete law gamma between alpha and nu in convex order, and the disintegration/pullback construction of a Lebesgue density. Try hard to find counterexamples or a missing hypothesis; distinguish dominating from being dominated in absolute continuity. Existing sections1-8 were accepted in two prior reviews and need not be re-reviewed. README has not yet been updated for this continuation, so its old open-density statement is historical, not a theorem defect. Give numbered findings with fatal/major/minor severity, locations and proposed fixes; or explicitly none. State whether Section9 actually gives the advertised iff criterion and whether its Fourier application is sound. Novelty is NOT claimed."""
    if args.round == 4:
        prompt = f"Act as a hostile mathematical referee. Read ONLY inside {ROOT};" """ do not browse, delegate, modify files, or execute code (static audit only; the parent will replay the checker). Sections 0-9 of proof.md were accepted in earlier rounds (evidence/codex-referee*.md). Focus on proof.md SECTION 10 (Theorem 10, a claimed genuine Fourier-pair counterexample to sufficiency of two convex orders plus the covariance identity for joint IF+GD couplings), the decisive checker work/verify_fourier_obstruction.py, evidence/fourier-certificate.json, evidence/fourier-obstruction-verification.json, and the README/references statements about Theorems 9-10 and prior art. Independently check by hand: Fourier invariance S=s under the unitary e^{-i w t} convention (Hermite polynomial calculus, eigenvalue signs, normalization irrelevance); E=55/49 and rho; the phase derivative f=14p'/(196+p^2); absence of zeros; g=-f; the covariance identity. Scrutinize the all-real-strike convex-order argument (symmetry reduction, sup bound via Sturm + FLINT root isolation, monotone sandwich on a finite grid, tail strikes, negative strikes) and whether each code path computes what the proof claims (sturm_count, positive_simple_roots, sign_intervals, moment recursions, call functions, closed form E|f(T)|). Scrutinize the dual certificate: the full-plane extension and Lemma 10.1, the corner check, the formula for Lambda including tails, integrability and conditioning, and whether the code's certificate_total matches it. Check the chirp controls' formulas and that controls/mutations are not load-bearing. Check Theorem 9's application (strict potential gap) and claims of prior art/novelty. Report numbered findings with fatal/major/minor severity, exact locations and fixes, or explicitly none. State whether Theorem 10 is proved as stated, conditional only on correct execution of the audited checker."""
    SCRATCH.mkdir(parents=True, exist_ok=True)
    command = ['codex', 'exec', '-m', 'gpt-6.1-sol', '-c',
               'model_reasoning_effort=max', '--sandbox', 'read-only',
               '--ephemeral', '--skip-git-repo-check', '-C', str(ROOT),
               '-o', str(SCRATCH / (prefix + '.md')), prompt]
    receipt = {
        'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'command': command,
        'stdin': '/dev/null',
        'timeout_seconds': 2700,
        'reviewed_sha256': {str(p.relative_to(ROOT)): sha(p)
                            for p in sorted(ROOT.rglob('*')) if p.is_file()},
    }
    env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               MKL_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
    try:
        with (SCRATCH / (prefix + '-stdout.log')).open('w') as out, \
             (SCRATCH / (prefix + '-stderr.log')).open('w') as err:
            result = subprocess.run(command, cwd=ROOT, env=env,
                                    stdin=subprocess.DEVNULL, stdout=out,
                                    stderr=err, timeout=2700)
        receipt['returncode'] = result.returncode
    except subprocess.TimeoutExpired:
        receipt['timeout'] = True
        receipt['returncode'] = None
    receipt['ended_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result_file = SCRATCH / (prefix + '.md')
    if result_file.exists():
        receipt['result_sha256'] = sha(result_file)
        (ROOT / 'evidence' / (prefix + '.md')).write_bytes(result_file.read_bytes())
    (ROOT / 'evidence' / (prefix + '-receipt.json')).write_text(
        json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: receipt[k] for k in ('started_utc', 'ended_utc', 'returncode')}))
