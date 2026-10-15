# Run and verification provenance

Date: 2026-10-14 (PT). Working directory for commands below: `/Users/jinleic/jinleic-workspace/ai4s/visual-cryptography-optimality`, unless stated otherwise.

## Environment

The prescribed `uv venv /Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv` selected **CPython3.12.12**, not the Python3.14 described as generally available in the assignment. This is recorded rather than silently claiming 3.14 execution. Installed only numpy2.5.4, scipy1.18.1, z3-solver5.1.0.0. Versions are pinned in `work/requirements.txt`. One process and one BLAS/OMP/HiGHS thread were used for generation; verification was sequential. Measured footprint with `du -sh ai4s/visual-cryptography-optimality scratch/ai4s-visual-cryptography-optimality`: 6.1MB durable target, 203MB scratch environment at the measurement time.

Use `PY=/Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv/bin/python` in the commands below. Do not use Python's `-O`: the exact verifier intentionally uses assertions.

## Cheap controls, before the frozen sweep

Commands:

```sh
$PY work/solve.py --max-n 3 --output evidence/controls-n3.json
$PY work/verify.py evidence/controls-n3.json --output evidence/controls-verification.json --queries evidence/controls-smt
```

Observed: 12 isomorphism classes, 12 exact rational LP certificates, 36 integer witnesses; all verified. All four negative controls rejected (LP multiplier, column count, gap/objective, missing coverage). These are controls, not separate statistical samples.

## Frozen sweep

Registered with:

```sh
python3 ../../scripts/campaign.py init --gate exact-strong-vcs-n5 --prereg pre_statement.md --agent VisualCryptoOptimality
```

Run ID: `20261014T084950Z_c585326d_3cdc4c499527`.

Commands:

```sh
$PY work/solve.py --max-n 5 --output evidence/certificates-n5.json
$PY work/verify.py evidence/certificates-n5.json --output evidence/verification-n5.json --queries evidence/smt
```

Observed: generation22.7543s; independent verification2.0147s. Every n<=5 basis row certified: 248 LP primal/dual pairs checked with exact fractions, 744 integer witness checks using full forbidden projected-column histograms, 726 rational/integrality/divisibility bounds, 18 UNSAT integer lower-bound queries in independently derived Mobius coordinates. The candidate generator's security constraints and the verifier's direct projected-pattern checks use different representations. The independent instance enumerator uses antichain backtracking rather than the generator's monotone truth-table recursion. The two share Python's integer arithmetic and elementary set/permutation primitives; the integer lower-bound checks trust Z3, not a proof-assistant kernel.

Coverage by n: class counts1,3,8,28,208; labelled nonconstant structures1,4,18,166,7579. No instance timed out, no row was omitted, and no unresolved integer objective was promoted to certified. The same four negative controls were rejected in the complete run.

## Bounded collection-model extension

After the basis sweep, a necessary universal black-matrix constraint was derived from the definition, as documented in `work/model.md`. This is a **post-sweep proof/certification extension**, not a preregistered discovery or independent held-out experiment. It does not alter or replace the frozen basis table.

Command:

```sh
$PY work/collection_bounds.py evidence/certificates-n5.json --output evidence/collection-bounds.json --queries evidence/collection-smt
```

The first invocation failed before producing a certificate because `solver.add` received a Python list plus a separate Boolean in the same call. The argument was split into two calls and the command rerun. The failure was an API usage error, not mathematical infeasibility. The successful run checked nine cases; four were UNSAT and five SAT in the necessary relaxation. **SAT is not a collection VCS.** This extension certifies all four collection objectives for n<=4 and for203/208 n5 structures; five remain intervals. No larger collection search was represented as completed.

## Tables and primary-source comparisons

Command:

```sh
$PY work/summarize.py
```

Outputs: `table-n4.csv`, `table-n5.csv`, `summary.json`. Observed: 23 exact primary-source comparisons match (19 expansion checks and four 2-out-of-n contrast checks). The small structures and source identifiers are embedded in the script and summary. No value from an inaccessible IEEE paper is used as a comparison anchor. The malformed text-extraction row13 of Ateniese1996 Table1 is explicitly skipped rather than guessed.

## Source acquisition commands

Book images were visually read before copying from the supplied staging directory with `cp .../pdfpage-0430.png .../pdfpage-0431.png sources/book/`. For each author-supplied PostScript file:

```sh
curl -L --fail https://cs.uwaterloo.ca/~dstinson/papers/IC.ps -o sources/ateniese-1996.ps
ps2pdf sources/ateniese-1996.ps sources/ateniese-1996.pdf
pdftotext -layout sources/ateniese-1996.pdf sources/ateniese-1996.txt
```

The same sequence used `contrast.ps` -> `blundo-1999` and `COTVCS.ps` -> `blundo-2003`. ECCC source:

```sh
curl -L --fail https://eccc.weizmann.ac.il/report/2000/003/download -o sources/krause-simon-2000.pdf
pdftotext -layout sources/krause-simon-2000.pdf sources/krause-simon-2000.txt
```

That ECCC PDF's text extraction is garbled; only its primary HTML abstract is relied on. Public URL-reader calls and the failed IEEE full-text endpoints are itemized in `sources/references.md`.

## Independent model review

The commands follow `docs/knowledge-system/MODEL_DELEGATION.md`, using the configured Codex model and effort, read-only sandbox, ephemeral sessions, and no further delegation. Exact prompt files: `codex-referee.prompt.txt` and `codex-collection.prompt.txt`; final replies and the resolution ledger are stored alongside them. The main prompt limits reads to this target and its cited public sources. The collection addendum is self-contained and requests no tools. Reviews are advice checked against the mathematical derivations and retained certificates, not an automatic proof or novelty clearance.

## Final binding and campaign closure

Commands:

```sh
$PY work/review_controls.py
python3 ../../scripts/campaign.py heartbeat
$PY work/seal.py
python3 ../../scripts/campaign.py freeze
python3 ../../scripts/campaign.py close --verdict FROZEN-CERTIFIED
```

`evidence/acceptance.json` and the campaign copy bind the completed code, sources, exact certificates, human-readable tables, prompts, replies and resolution ledger by SHA-256. `FROZEN-CERTIFIED` applies only to the explicitly scoped finite certification claims. The receipt separately records `original_problem_solved: false` and `PARTIALLY-SOLVED`; it does not turn the open original problem into a completed proof. Both Codex processes and all computational jobs finished before handoff.
