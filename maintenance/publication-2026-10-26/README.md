# Contribution assessment and publication refresh — October 26, 2026

The repository contains complete, substantive resolutions of precisely scoped research targets.
The best-supported contribution claims are explicit finite constructions and theorems with
retained proofs, independent checks and honest boundaries. They do not establish that all broad
book problems were solved, worldwide priority, or human peer acceptance.

## Strongest supported results

| Result | What is complete | Verification and contribution boundary |
|---|---|---|
| Six cyclic `(v,5,1)` difference families | Explicit constructions for `v = 321, 501, 621, 681, 801, 901`. [Verdict](../../institute/runs/six-lane-2026-10-16/review/cdf-k5-parent-verdict.md). | Fresh independent exact checks passed for every nonzero directed difference. These match the six possible exceptions listed by [Hetman–Baicheva–Topalova, 2026, p.114](https://jacodesmath.com/index.php/jacodesmath/article/download/389/267/), checked live. The spectrum corollary imports the published other cases; worldwide priority remains unproved. |
| RDSQS(52) and mcDSQS(38) | Explicit resolvable/minimum-coloured derived Steiner quadruple systems. [RDSQS verdict](../../institute/runs/six-lane-2026-10-16/review/rdsqs52-parent-verdict.md), [mcDSQS verdict](../../institute/runs/six-lane-2026-10-16/review/mcdsqs38-parent-verdict.md). | Fresh checkers covered all 22,100 and 8,436 triples, respectively, plus all 52 resolutions and 38 optimal 19-colourings. Historical Lean replays were not rerun. The underlying SQS(38) was already published; its certified optimal colourings are the contribution. |
| Four Handbook BTD cases | Three nonexistence results and the explicit existence of `BTD(14,28;8,3,14;7,6)`. [Earlier assessment and exact cases](../publication-2026-10-22/README.md#what-the-evidence-supports). | Fresh independent check of the positive witness passed all row/column conditions and 91 row pairs. The other three proofs retain their historical Lean or 3073-DRAT verification; those were not freshly replayed. |
| CFR(5,27) | Two explicit circular Florentine rectangles establish existence and `F_c(27) >= 5`. [Verdict](../../institute/runs/six-lane-2026-10-16/review/cfr27-parent-verdict.md). | Both freshly checked against the definition: 3510 distinct circular symbol/displacement events each. This is an existence result, not an optimum determination; priority screening has access gaps. |
| Sharp two-qutrit entangling-power bound | The maximum for a non-2-unitary dual or T-dual two-qutrit gate is exactly `15/16`. [Verdict](../../institute/runs/six-lane-2026-10-16/review/qutrit-sharp-parent-verdict.md). | Reviewed written universal proof; fresh exact arithmetic checked one attaining gate, including unitarity, realignment, rank 6 and `tr(W^2) = 27/2`. This fresh check alone does not prove the universal upper bound. |
| Sun's disjoint-coset conjecture at seven cosets | The arbitrary-group `k = 7` statement has an internally accepted complete written composition. [Final verdict](../../institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md). | Historical model-review/parent protocol, not a new proof reconstruction in this pass. Not kernel-checked or human-reviewed; general `k` and priority remain unresolved. |

Additional supported targets include LKTS(57/87), gcDCQS(20^4:0) and gcDCQS(32^4:0), their
explicit derived designs, and the sharp PH-order theorem for Commault–Mocanu's stated
three-pole family. Published recursion and other imports retain their own boundaries.
The [Tan–Zhou source](https://arxiv.org/html/2503.11934v1) and
[original PH conjecture paper](https://people.smp.uq.edu.au/YoniNazarathy/AMSIschool2016/CommaultMocanu_forAssignment.pdf)
were checked as baselines, not as a complete present-day priority search.

The historical final `M(7) = 2` verdict retains the significant missing-stream/script-observation
qualifications in the [October 22 assessment](../publication-2026-10-22/README.md).
It was not freshly certified here. CPCW and `L(12,3) = 36` remain independent confirmations
of earlier public claims, not new discoveries.

## New work and unresolved targets

The [three-area round](../../institute/runs/three-area-2026-10-23-96h/README.md) is an active
research record, not a completed eighteen-problem success report. The reviewed entry README
identifies checkpoint 075; later checkpoint files are separate observations, not round closure.
Meaningful newer work includes written PH parameter-band results, Sun(8) for specified
SL/PSL families, all-law additive-noise privacy results at their source-equivalence ceiling,
PPT witness-class decompositions, and depolarizing equality/region theorems.
These proper-class and conditional results do not solve the original unrestricted targets.
Full ordered Olson, Shor finite-code completion, MOQLS(8), maximal 1-RQLS(10), and the other
open targets retain their explicit residual obligations.

All related limitations travel with the manuscripts:

- The [operative information-science overlay](../../information-science/evidence/three-area-20261023-96h/verification-OPERATIVE-OVERLAY-1.md)
  withdraws earlier new-round "kernel replay" wording: those were ordinary Fraction spot checks.
  Written identities require written proof; sampled arithmetic does not certify them.
- The [semigroup fatal disposition](../../institute/runs/three-area-2026-10-23-96h/semigroup-LG-supported-CG-RULU-fatal-parent-v1.md)
  supports the scoped LG construction but refutes CG and full RU–LU. Dependent withdrawn
  proofs remain historical research, not accepted theorems or a refutation of the original book problem.
- Source-access gaps, dependent-claim counts, process findings, parent-clock corrections,
  actual review scopes and the scientific execution hold remain as recorded. Publication
  neither erases them nor authorizes new research execution.

Negative results, failed approaches and withdrawals are retained where they explain a barrier,
correct a claim or preserve a published proof's dependency history. They are not success counts.

## Fresh verification

From any directory, run the stdlib-only compact witness audit:

```sh
python3 -B /path/to/aifours/maintenance/publication-2026-10-26/check_compact_witnesses.py
```

It independently checks the six CDFs, the BTD and both CFRs, then uses the separately authored
definition-first RDSQS/mcDSQS checkers. All eleven witness checks passed; three deliberate CDF,
BTD and CFR corruptions were rejected. [check_compact_witnesses.py](check_compact_witnesses.py)
contains the exact predicates and SHA-pinned design inputs.

For the exact attaining gate, use an environment with SymPy (the existing research environment
was used here), from the repository root:

```sh
python -B institute/runs/six-lane-2026-10-16/review/qutrit_sqrt6_gate_parent_check.py \
  /tmp/aifours-qutrit-exact-gate.json
```

The [retained receipt](qutrit-exact-gate-receipt.json) records all seven checks passing.
The [verification receipt](verification-receipt.json) also records a successful compact audit
from outside the repository and all 22 existing launcher/sandboxed-replay tests passing under
Python 3.14.3. These tests use fixtures and make no model calls.
Historical Lean, large UNSAT certificates and complete universal written proofs were not
re-executed by these bounded checks. They corroborate the named witnesses, not the whole repository.
Three read-only in-harness reviewers also inspected separate domain authorities. No external-model
CLI, paid API, research campaign or long solver computation was launched in this assessment.

## Publication contents and artifact limits

The root `.gitignore` now additionally covers source-paper HTML/text and archives outside
`sources/`, book/paper page renders, full downloaded CONTENTS indexes, and new-round raw
stdout/stderr. Generated literal review-input bundles (`*-sources-*` and `*-partN-v*`) are also
omitted: they duplicate retained manuscripts and sometimes external full-text sources.
Wave manifests, original research, source pins, actual returned reviews and final dispositions
remain available; exact replay of omitted input packets requires reconstruction or local copies.
Existing rules keep large SAT/DRAT/LRAT streams, arrays, environments, caches,
native binaries and exact large generated payloads local. The existing exact-exclusion refresh
was rerun without changing its selections. No local artifacts were deleted or moved.
The [additional exclusion inventory](additional-exclusions.tsv) records the newly ignored paths
and their observed byte sizes; it is not a complete census of previously excluded evidence.
At that observation, 612 additional local files totaling 73,289,520 bytes were excluded.
All 22 existing tests and the named witness checks passed. The staged secret scan had no
unreviewed findings after two inspected false positives in ordinary prose/Git metadata.
Nine whitespace findings in seven frozen incoming records were preserved to retain their
hash-bound bytes; maintained publication files passed the whitespace check.

Research sources, written proofs, compact witnesses, structured receipts, source pins,
corrections and review dispositions remain eligible. Existing tracked paths remain eligible;
the new exclusions do not silently remove compact historical checker output.
The public clone is not a full immediately replayable evidence bundle: large certificates and
external source copies require regeneration or separate retrieval, and some older proof streams
were never retained. Hashes and old receipts do not repair missing proof bytes.

The authorized destination is `https://github.com/jinleic/aifours`, branch `main` through
`origin/main`; no remote named `upstream` is configured. Publication uses the repository's
existing GitHub noreply identity and a normal fast-forward push. The actual final commit and
remote SHA comparison, rather than this procedure, establish that publication succeeded.
