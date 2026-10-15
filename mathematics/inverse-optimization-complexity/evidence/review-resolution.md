# Independent review resolution

Date: 2026-10-14 (America/Los_Angeles).

## Round 1

- Prompt: `proof-review.prompt.txt`; verbatim result: `proof-review.md`; execution metadata: `proof-review-run.json`.
- Reviewer: Codex CLI, registry model `gpt-6.1-sol`, reasoning effort `max`, read-only sandbox, ephemeral, no further delegation.
- Exit code: 0.
- Verdict: **READY-WITH-FIXES**.
- Sole finding: the text attributed both weighted l1 and weighted l-infinity directions to Heuberger Theorem 3.3, although that theorem explicitly states weighted l1.
- Resolution: **applied** in `proof.md` Section 5. Weighted infinity is now grounded separately in the same radius-variable LP/separation argument; Schulz Lemma 4 explicitly handles its unweighted instance. No mathematics changed.
- The reviewer affirmed the main reductions, positive-weight zero tests, rational output argument, dummy closure, explicitly restricted-cost counterexample, and infinity-norm formula. It explicitly did not certify a full solution of the book question.

## Round 2

- Prompt: `extension-review.prompt.txt`; verbatim result: `extension-review.md`; exact reviewed proof hash and command: `extension-review-run.json`.
- Same registry model and read-only controls; exit code 0.
- Verdict: **READY**, no mandatory mathematical corrections.
- Reviewed additions: UP/unique-optimum barrier, oracle-only lower bound, bottleneck threshold/pruning converse, recoverable binary-feature lift, and the explicitly unresolved normalized general-objective formulation.
- Optional wording suggestion: specify that original coordinates are the first features after a known permutation. The current proof already uses that ordering convention; no substantive gap was reported. This optional clarification was not needed to change the verified claims.
- The referee checked the criticism of Huang's universal/existential mistake and agreed that it invalidates that purported certificate argument, without asserting NP!=coNP.
- Crucial scope conclusion: **the general book question remains unsolved in this dossier; none of the reproduced or boundary results should count as a full solution or as evidence that the custom refinement is a source-certified still-open book problem.**

## Executable evidence

The author, not the reviewer, ran `python3 work/check.py --output evidence/check-results-extended.json` successfully on Python 3.14.3 using one process and exact rational arithmetic. The JSON binds the two Python source hashes and records all case counts. Earlier checks are retained separately. The independent model inspected the code and saved results but did not rerun them.

Both review processes exited normally and no reviewer process remains running. No live infrastructure, credentials, paid compute, commits, or external messages were used.
