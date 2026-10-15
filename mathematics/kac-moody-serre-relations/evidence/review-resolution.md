# Independent review resolutions

Date: 2026-10-14 (PT). All three Codex CLI invocations exited normally with code 0. Their stderr headers confirm **gpt-6.1-sol**, reasoning effort **max**, sandbox **read-only**. Prompts limited reads to this target and forbade further delegation and code execution. Commands, timestamps, PIDs and reviewed hashes are preserved in the corresponding `*-run.json` files.

## Round 1: main algebra and initial checker

- Prompt/output: `proof-review.prompt.txt`, `proof-review.md`.
- Verdict: **READY-WITH-FIXES**.
- Mathematical audit: no error found in the exact descent recurrence, Serre recursion, coefficient-one theorem, necessary condition A alpha<=0, or sign conventions.
- Sole mandatory finding: checker PASS trusted certificate-provided height and matrix collection rather than binding them to an independent requested scope. A whole omitted matrix could evade its original negative controls.
- Resolution: **applied**. The current checker requires explicit `--height` and `--matrices`, compares entries with the fixed specification, and records all scope identifiers and hashes. Six negative controls include omitted/altered matrices and height.
- The original full tensor-elimination implementation is preserved as `check_certificate-reviewed.py`. Its two unfinished runs were cancelled; they never produced an accepted receipt and are not counted as passes.

## Round 2: scope-bound quotient checker

- Prompt/output: `checker-review.prompt.txt`, `checker-review.md`.
- Verdict: **READY**, no new correctness repair required.
- It accepted external scope binding, complete degree coverage, and the efficient quotient-injectivity proof. The checker independently regenerates I, uses word-deletion lowerings, and certifies injectivity of L/I into lower quotients; proved I-stability and lower-degree equality justify omitting ideal columns.
- Independence limit is explicit: the checker shares standard free-Lie/Lyndon mathematics with the producer, but imports no producer code. This is not Lean/kernel verification.
- The reviewer saw the height-10 PASS. Height 12 was still pending at its final inventory, then **passed after that review** with the same checked checker source hash. Do not misquote the review as having executed or already observed the later run.
- Completed receipts: `rational-height10/independent-check.json` (all five matrices, 1,290 degree records); `rational-height12/independent-check.json` (A_one, 421 degree records). Both rejected all six negative controls.

## Round 3: uniform rank-three height-six theorem

- Prompt/output: `symbolic-review.prompt.txt`, `symbolic-review.md`.
- Verdict: **READY**, no mathematical or checker error requiring repair.
- Reviewed the complete bridge from coefficient-one equality to degree222, all64 unbounded parameter cells, constant Serre spans, affine parameter dependence, quotient bases, index-permutation coverage, denominator clearing, exact Bareiss identities, and coefficientwise positivity.
- Confirmed that six inconclusive direct minors were not omitted: 1→2, 17→6, 21→22, 33→10, 37→22, 49→11 under verified permutations. The degree222 claim is invariant under the simultaneous index renaming.
- Verified statically that the saved all-cell PASS receipt matches the hashes of all16 representative certificates, all64 coverage entries, and the three checker files. The parent executed the checker; the referee did not rerun it.
- Accepted scope: **every rank-three GCM through height six**. Not all heights, not all ranks, not a proof of the full book conjecture, and no novelty assertion.

## Failures kept visible

- `symbolic-222-first-attempt.json`: a SymPy BooleanAtom reporting exception, fixed before the successful regeneration. No unsaved mathematical result from that failed run is claimed.
- `symbolic-222/direct-check-rejection.json`: the direct all-positive-minor approach failed at mask1. The accepted proof uses complete independently verified permutation coverage, not suppression of that failure.
- The failed Zellhofer HTML response remains marked unusable as a paper; the initial Williams download problem was resolved using a directly opened alternate public PDF link.

## Final boundary

The full characteristic-zero defining-relations conjecture remains unresolved in this dossier. The main deliverables are a proved infinite boundary family, a computer-assisted uniform rank-three height-six theorem, and exact independently checked finite comparisons at heights10/12. All reviewer processes and computation jobs started by this worker have finished or were explicitly cancelled; no background computation remains.
