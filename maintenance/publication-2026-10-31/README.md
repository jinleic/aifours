# Contribution assessment and publication — October 31, 2026

The repository contains complete answers to several precisely scoped difficult targets and
substantial partial progress on others. The most defensible contribution claims are the
explicit finite constructions with independent definition-level checks. This assessment is
not a reconstruction of every universal proof or a complete current priority search.

## Completed targets and strength of evidence

| Result | Supported scope | Verification and contribution boundary |
|---|---|---|
| LKTS(57), LKTS(87) | Both finite existence problems have explicit large sets of Kirkman triple systems. [Verdict](../../institute/runs/six-lane-2026-10-16/review/lkts-57-87-parent-verdict.md). | Fresh independent checks covered all 29,260 and 105,995 triples and all constituent parallel classes. Historical Lean replays were not repeated. All-orders existence remains open. |
| Six cyclic difference families | Explicit `(v,5,1)` witnesses for `v=321,501,621,681,801,901`. [Verdict](../../institute/runs/six-lane-2026-10-16/review/cdf-k5-parent-verdict.md). | All six exact directed-difference checks passed again. The spectrum corollary also imports the published other cases. Priority remains unresolved. |
| RDSQS(52), mcDSQS(38) | Explicit derived-design certificates, including all 52 resolutions and all 38 optimal 19-colourings. [RDSQS](../../institute/runs/six-lane-2026-10-16/review/rdsqs52-parent-verdict.md), [mcDSQS](../../institute/runs/six-lane-2026-10-16/review/mcdsqs38-parent-verdict.md). | Fresh independent checks passed. The underlying SQS(38) was already public; the certified optimal colourings are the contribution. |
| Four BTD cases | Nonexistence at `(12,15;6,2,10;8,6)`, `(14,18;7,1,9;7,4)`, `(12,20;4,3,10;6,4)`; existence at `(14,28;8,3,14;7,6)`. [Prior assessment and authorities](../publication-2026-10-22/README.md). | The positive witness freshly passed every row/column condition and all 91 row-pair checks. Historical Lean/DRAT nonexistence certificates were not rerun. |
| CFR(5,27) | Two explicit circular Florentine rectangles prove existence and `F_c(27)>=5`. [Verdict](../../institute/runs/six-lane-2026-10-16/review/cfr27-parent-verdict.md). | Both freshly passed all 3,510 circular events. This does not determine the optimum. |
| Sharp two-qutrit bound | Maximum entangling power is `15/16` for non-2-unitary dual or T-dual two-qutrit gates. [Verdict](../../institute/runs/six-lane-2026-10-16/review/qutrit-sharp-parent-verdict.md). | Complete internally reviewed written upper bound and exact attaining gates. A domain reviewer freshly checked attainment in `Q(sqrt(6))`; this corroborates the lower bound, not the universal proof. No human or fresh kernel review. |
| Sun's seven-coset theorem | The arbitrary-group `k=7` statement has an internally accepted complete written composition. [Verdict](../../institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md). | Historical model/parent written review, not a fresh full reconstruction, Lean proof or human review. General `k` and priority remain unresolved. |

Additional complete scoped work includes gcDCQS(20^4:0), gcDCQS(32^4:0), their explicit
derived designs and qualified imported infinite-family consequences, and the stated
Commault–Mocanu three-pole PH-order formula. Their individual dispositions retain their
published imports. `M(7)=2` has an internally accepted computer-assisted verdict, with the
significant missing-proof-stream and 35-class replay qualifications in the
[October 22 assessment](../publication-2026-10-22/README.md). Its upper bound was not rerun.

Two primary baselines were refreshed online on October 31. [Wang's v1 conclusion](https://arxiv.org/html/2607.21521v1)
still identifies 57 and 87 as the two possible LKTS exceptions below 200. The
[AME survey v3](https://arxiv.org/html/2508.04777v3) describes `15/16` as the likely
two-qutrit optimum and says the rigorous gap remains to be established. These baselines
explain why the targets matter; they do not establish worldwide priority for this repository.

## Meaningful newer work, with residual obligations

The [October 23–27 final report](../../institute/runs/three-area-2026-10-23-96h/final-report-v2.md)
and [October 27–31 rolling report v36](../../institute/runs/three-area-2026-10-27-96h/rolling-report-20261030-v36.md)
with its [mandatory erratum](../../institute/runs/three-area-2026-10-27-96h/rolling-report-20261030-v36-erratum-1.md)
own the later scopes. V36 remains nonfinal. Ledger rows and review counts are not discovery counts.

- The [MOQLS(8) triple](../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-4-three-moqls8-one-nonclassical-witness-parent-v1.md)
  is a concrete new finite witness: three mutually orthogonal squares, one nonclassical.
  Fresh integer/rational checks passed, including squared overlap `1/2`, and seven
  corruption controls were rejected. This does not decide the four-family target or `M(8)`;
  a numerical literature-bound improvement remains conditional on source status.
- The [R-minus certificate](../../institute/runs/three-area-2026-10-27-96h/dispositions/info-5-rminus-guessing-number-upper-bound-716-107-conditional-dfz-parent-v1.md)
  supports `20/3 <= gn(R−) <= 716/107`, conditional on the named DFZ inequality.
  Fresh exact arithmetic checked 2,377 records and 2,873 coordinates, with residual zero.
  It does not determine the exact guessing number or prove the imported inequality.
- The [PH parameter-band theorem](../../institute/runs/three-area-2026-10-27-96h/dispositions/math-1-ph7-no-seven-states-above-83over100-parent-v1.md)
  gives minimum order eight for the displayed squared three-pole transform on
  `z in [83/100,8/9]`, under its stated imports. The full order function remains open.
- The [ordered-dihedral deficit-six theorem](../../institute/runs/three-area-2026-10-27-96h/dispositions/math-2-actual-ordered-dihedral-projection-deficit-six-mixed-selector-parent-v1.md)
  closes that entire named band for odd primes at least seven, with the exact word/gap
  hypotheses retained. It does not settle unrestricted ordered Olson.
- The [AME support composition](../../institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-conditional-minimum-support-50-to-60-same-tensor-union-parent-v1.md)
  gives conditional `50 <= minimum support <= 60`, importing named lower-bound and
  enumerator chains. Source/provenance qualifications remain; the exact minimum is open.

The current six targets in each domain remain open at their registered full scope.
Other new manuscripts contain useful class exclusions, equality cases, reductions and
counterexamples. They travel with their dependencies, returned reviews and dispositions.
CPCW and `L(12,3)=36`, and the new Werner certificate, remain independent confirmations
of prior public claims. The semigroup CG/RU–LU claims are refuted; the
[fatal disposition](../../institute/runs/three-area-2026-10-23-96h/semigroup-LG-supported-CG-RULU-fatal-parent-v1.md)
and all withdrawals remain. The stochastic-Hinf presource errata are retained explicitly.
Publication does not release held claims or turn documentary checks into scientific acceptance.

## Fresh verification

[verification-receipt.json](verification-receipt.json) records commands, outputs and the new
MOQLS witness/checker hashes. The compact audit, both LKTS checks, exact R-minus certificate
check and all 22 existing launcher/sandboxed-replay fixture tests passed. No external-model
CLI, paid API, solver campaign, dependency install or research continuation was launched.

[static-checks.json](static-checks.json) records a Python 3.14.3 syntax scan of 4,782 incoming
Python files. Nine do not compile: six deliberately malformed PH hardening fixtures and three
historical candidate/control scripts with syntax or captured-output truncation defects. Their
bytes are preserved as research history; they need repair or replacement before executable
use and do not support this assessment's successful fresh checks. The new assessment's local
links resolve, and no currently tracked file is covered by the ignore policy.

The existing compact audit is portable from any working directory:

```sh
python3 -B /path/to/aifours/maintenance/publication-2026-10-26/check_compact_witnesses.py
```

The new R-minus verifier still embeds local paths and requires separately retrieved source
texts. Large proof streams, environments and some historical proof bytes are omitted or were
never retained. The public clone is therefore a research-source publication, not a complete
immediately replayable proof bundle. Fresh witness checks do not certify every manuscript.

## Artifact policy and publication

[prepare_local_exclusions.py](prepare_local_exclusions.py) defaults to a dry run; `--apply`
refreshes only this publication's block in `.gitignore` and the
[path/size inventory](additional-exclusions.tsv). It preserves all files on disk and never
stages, untracks or deletes files. The inventory covers 7,591 local files totaling
18,749,371,175 logical bytes, including overlap with earlier cache/source exclusions.
Git's own matcher confirmed every inventoried path is ignored.

The new policy keeps solver DRUP streams and CNF bodies, vendored Python packages, downloaded
pages/archives and page renders, duplicate review-input packets, native executables, and
generated non-source payloads over one MiB local. Original proof/code/Lean sources, compact
witnesses, source pins, manifests, returned reviews, final dispositions and corrections remain
eligible. Existing tracked evidence is preserved. Original packets can require local copies
or reconstruction, and hashes do not replace missing proof bytes.

The authorized destination is `https://github.com/jinleic/aifours`, `main` through `origin`.
There is no configured remote named `upstream`. Publication uses the established GitHub
noreply identity and a normal fast-forward push; the final reported remote SHA establishes
the actual publication result.
