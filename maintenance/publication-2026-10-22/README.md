# Research assessment and publication — 2026-10-22

Status: repository/evidence review, with fresh bounded witness checks. This is not a new research
run, a full audit of every proof dependency, a novelty clearance or human peer review. The owner
explicitly requested this assessment, exclusion of bulky artifacts, and publication to the upstream
GitHub repository's main branch.

## What the evidence supports

Yes: the repository has meaningful specialist contributions and complete answers to several precisely
stated difficult targets. Broad book questions and all-parameter conjectures must be distinguished from
their finite instances. Internal acceptance is evidence about the recorded checking protocol, not
external mathematical acceptance.

| Result | Exact supported scope and authority | Verification boundary |
|---|---|---|
| Sun(7) | For every group, seven pairwise disjoint left cosets of finite-index subgroups force two subgroup indices to have gcd at least 7. [Final composition verdict](../../institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md). | Complete written composition internally accepted by two model families and the parent. No Lean or human review; conjecture for every k and priority unresolved. |
| LKTS(57), LKTS(87) | Explicit large sets of Kirkman triple systems settle both finite existence targets. [Verdict](../../institute/runs/six-lane-2026-10-16/review/lkts-57-87-parent-verdict.md). | Multiple independent direct verifiers and recorded Lean proofs/replays. Fresh witness checks passed; Lean was not rerun. All-orders existence remains open. |
| Six cyclic difference families | Explicit cyclic (v,5,1) families at v = 321, 501, 621, 681, 801, 901. [Verdict](../../institute/runs/six-lane-2026-10-16/review/cdf-k5-parent-verdict.md). | Fresh independent checks cover every directed difference exactly once. Recorded Lean replays; complete spectrum through 1001 additionally imports the published theorem. |
| Four BTD instances | Nonexistence for (12,15;6,2,10;8,6), (14,18;7,1,9;7,4), (12,20;4,3,10;6,4); existence for (14,28;8,3,14;7,6). [BTD12-20](../../institute/runs/six-lane-2026-10-16/review/btd12-20-parent-verdict.md), [BTD14-28](../../institute/runs/six-lane-2026-10-16/review/btd14-28-parent-verdict.md). | First two have recorded Lean proofs; third uses a structural reduction and 3073 DRAT proofs. Fresh definition-level check passed for the 14-by-28 witness. |
| Sharp two-qutrit bound | Maximum entangling power of a non-2-unitary dual or T-dual two-qutrit gate is exactly 15/16. [Verdict](../../institute/runs/six-lane-2026-10-16/review/qutrit-sharp-parent-verdict.md). | Reviewed written universal proof plus exact attaining gates. Fresh independent rational/surd arithmetic checked an attaining gate, not the entire universal proof. |
| M(7) = 2 | Every MOQLS(7) triple is classical; a nonclassical pair exists. [Final verdict v2](../../institute/runs/six-lane-2026-10-16/review/moqls7-M7-equals2-parent-gate-verdict-v2.md). | Internally accepted computer-assisted proof. 35 K2 classes lack script-hash-observed parent replay; M7 proof streams were neither retained nor digested. Fresh exact pair checking corroborates only the lower bound. |

Additional substantial scoped results include RDSQS(52), minimum-coloured mcDSQS(38), gcDCQS20/32
and imported infinite-family consequences, the ME(order at most 3) minimum-SCV theorem, no
point-cyclic resolution at order 88, CFR(5,27), and random regular graph colouring results. Their
individual verdicts own the hypotheses, classical imports and verification levels. For mcDSQS(38),
the underlying SQS was already published: the minimum colourings are the contribution.

## Novelty and unresolved targets

Priority remains unresolved for the shortlisted results. A bounded literature screen does not prove
first discovery. The [CPCW priority correction](../../institute/runs/six-lane-2026-10-16/review/cpcw-priority-addendum-v1.md)
records an earlier public construction on 2026-08-24, and the
[L(12,3) correction](../../institute/runs/six-lane-2026-10-16/review/cover12-3-priority-addendum-v1.md)
records an earlier public claim on 2026-09-07. Those results are independent confirmations here.

The [96-hour final report v17](../../institute/runs/six-lane-2026-10-18-96h/report/continuation-report-2026-10-22-final-v17.md)
leaves full ordered Olson, MOQLS(8), maximal 1-RQLS(10), PA(19,8,6), CFR(6,21) and six MOLS(39)
unresolved. Olson's all-primes terminal k=p+1 union is substantial partial progress; it is not the
full conjecture. PA19's restricted frontier is 128, not the unrestricted search universe. DELTA3,
ALL-R and TILE remain unpromoted. The report's process MAJORs and missing second-family gates remain
disclosed and are not cured by publication. Earlier summaries of the M(7) frontier are superseded by
its final verdict, rather than retroactively editing immutable research records.

Primary sources refreshed during this assessment:

- [Wang, LKTS construction](https://arxiv.org/abs/2607.21521), still exposing v1.
- [Ball–Simoens, MOQLS v2](https://arxiv.org/html/2607.12933v2), including its Problem 16 and historical bounds.
- [Zhu, Sun's disjoint-coset conjecture](https://arxiv.org/abs/0807.2207), which proves k=3,4.
- [AME survey v3](https://arxiv.org/html/2508.04777v3), containing the historical 15/16 conjectural optimum.

These checks confirm the referenced historical baselines, not a complete current priority search.

## Fresh bounded verification

Three in-harness reviewers independently inspected the mathematics, information-science and physics
authorities. No external-model CLI, paid API, solver campaign or new research job was launched.

- LKTS57 and LKTS87: direct checks passed for all 29,260 and 105,995 triples respectively.
- RDSQS52: independent parent checker returned VALID for all 52 resolutions.
- mcDSQS38: independent parent checker returned VALID for all 38 minimum 19-colourings.
- All six CDF raw witnesses: exact directed-difference multisets passed independent stdlib checks.
- Both CFR(5,27) witnesses: all 3510 circular events per witness were distinct.
- BTD14-28: all row compositions, column sums and 91 pairwise dot products passed.
- Nonclassical MOQLS7 pair: 1176 cell pairs checked exactly; wrong-partner and classical controls behaved correctly.
- Qutrit attaining gate: independent arithmetic over Q(sqrt(6)) verified unitarity, self-realignment,
  rank of the partial transpose equal to 6, tr(W squared) = 27/2 and entangling power 15/16.

Historical Lean replays and large UNSAT/Arb certificates were not re-executed in this publication pass.
Several historical environments no longer exist; some commands still need the documented path
translation or environment reconstruction. The entire repository is not certified portable.

The existing launcher suite also passed: 17 tests with
`~/.local/state/research-explorer/venv/bin/python -B institute/tests/test_parallel.py`
(Python 3.14.3). The system `python3` initially failed on `hashlib.file_digest`, which requires
Python 3.11 or newer; rerunning in the documented environment passed without changing launcher code.

## Artifact policy and reproducibility

Nothing is deleted or moved by this publication pass. `.gitignore` retains source PDFs, rendered
third-party pages/full text, environments, build products, native executables, raw logs and large
generated artifacts locally. Sources, written proofs, compact mathematical witnesses, review notes,
structured receipts, source pins and manifests remain eligible for publication, including scoped
negative results and limitations that explain what was learned.

[prepare_local_exclusions.py](prepare_local_exclusions.py) refreshes a marked exact-path block in
the root `.gitignore` and [exact-exclusions.tsv](exact-exclusions.tsv). It excludes generated
non-source files over 5 MiB, generated controls/duplicate enumerations over 1 MiB, and native
executables identified by file signatures. It preserves code and Markdown regardless of size.
Generic file-type and location rules remain in `.gitignore`; the TSV inventories only the exact-path
block, not every ignored file. Do not interpret it as a deletion manifest or a complete evidence census.

There is deliberately no blanket `*.gz` or `evidence/` exclusion: compact compressed certificates
such as Sun6's witness data remain useful. Large evidence exclusions are substantive:

- BTD12-20's 3073 DRATs total about 666 MB, and 3088 CNFs total about 1.20 GB even though each is
  below 5 MiB. Generic CNF/DRAT rules exclude them; generators, case lists, hashes and receipts stay.
- The nine random-5-regular cone JSON trees are about 39–41 MiB each. Their direct checkers need
  them; the package's producer and recorded regeneration commands remain available.
- ME3's large compressed chart leaves are already local-only under the existing `leaves.txt.gz`
  rule; complete Arb replay requires regeneration or separately preserved payloads.
- Some PA19 restricted proofs are very large; some earlier measured-stream receipts already lack
  retained proof bytes. Exclusion does not repair that provenance gap.

Therefore this publication provides reproducibility sources and verification records, with compact
witnesses, rather than every proof byte required for immediate independent replay. Historical
manifests and append-only records can still name excluded local files; those files are not promised
to exist in a fresh clone.

## Git publication procedure

The established identity is the repository's existing GitHub noreply identity. `origin` is
`https://github.com/jinleic/aifours.git`; its actual default branch is `main`. There is no separate
remote named `upstream`, so the owner's upstream/main request resolves to `origin/main`.

Before publication, preserve the unpushed WIP commit under a local backup ref. Build a clean
publication commit directly on the fetched `origin/main`, omitting ignored files from its tree and
its new ancestry. This avoids uploading the bulky contents of the old unpushed commit. The push
is a normal fast-forward, with no remote history rewrite or force push. Previously published
history and the local backup remain intact. Excluded worktree files remain on disk.

Review the candidate tree for secrets, prohibited artifact types, file sizes, source/witness retention
and unexpected changes before pushing, then compare the remote main SHA with the published commit.
The final Git commit and remote receipt identify the actual publication; this procedure alone is
not a claim that the push succeeded.
