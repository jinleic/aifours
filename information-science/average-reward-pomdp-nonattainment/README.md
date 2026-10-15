# Average-reward POMDP optimization: an optimizer need not exist

**Outcome:** a complete four-state counterexample refutes the unrestricted **expected-average optimizer-existence** reading of the book's request. Every history-dependent randomized policy has a well-defined reward strictly below 1, while finite-memory policies approach 1. This is **Certification, novelty unestablished**—not a claim to have solved general POMDP optimization or discovered a new obstruction.

## 1. Source

- Article: **部分可观马尔可夫决策过程的性能优化**.
- Authors: **汪德新、曹希仁**.
- 《10000个科学难题·信息科学卷》, Science Press, 2011, book **653–655**, PDF **674–676**.
- Authoritative scans: [653](sources/page-0674.png), [654](sources/page-0675.png), [655](sources/page-0676.png).
- Original PDF SHA-256: `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`.
- [Complete proof and exact source quotations](proof.md); [primary-source ledger](sources/references.md).

## 2. Problem and fixed readings

Book p.654:

> 在最一般的情况下，一个POMDP系统的策略是关于整个系统输出历史和行动历史的一个函数。

“In the most general case, a POMDP policy is a function of the entire output and action histories.”

> 则我们希望解决的问题是如何选取最优的策略u使得上式取得最大值。

“We wish to solve how to select an optimal policy u making the expression above attain its maximum.”

**Important convention:** the printed long-run sample-average formula does **not** show an expectation symbol. We adopt the standard numeric **expected-average** reading, state it explicitly, and do not silently equate it with pathwise worst-case optimization. All three article pages and the inspected front matter/TOC state no shared recurrence restriction; this is a source-local observation, not an examination of every cited paper's standing assumptions.

| Reading | Exact question | Verdict |
|---|---|---|
| R1 | For every finite rational POMDP, does an all-history expected-average maximizing policy exist? | **REFUTED / complete negative answer here.** Four states suffice; private randomization and unbounded memory do not repair nonattainment. |
| R2 | Find a maximizer whenever one exists, otherwise report that none exists | **Not settled.** Deciding existence and synthesizing a policy are separate computational questions. |
| R3 | Approximate the optimal expected value by finite-memory policies | **SOLVED-BY-PRIOR-WORK** for finite POMDPs: every positive epsilon admits such a policy. There is no computable general input-only memory bound in the cited theorem's setting. |
| R4 | Optimize an almost-surely guaranteed or best-case sample-path reward | **Different objective.** In our example every policy maximizes the guaranteed value 0; W C attains the best-case value 1. R1's negative answer does not transfer. |
| R5 | General practical optimization theory, including continuous states or recurrent models | **Not solved by this package.** The irreversible absorbing counterexample does not apply under additional communicating, unichain or ergodicity assumptions. |

“Complete negative answer here” refers to the precise R1 theorem, not novelty or the whole article's research programme.

## 3. Status as of 2026-10-14 PT

The R1 theorem is fully proved in [proof.md](proof.md), independently model-reviewed twice, and its finite identities are exercised exactly. No Lean/kernel verification or human peer review is claimed. No accessible source inspected in this round was verified to contain this exact four-state table; that search limitation is **not evidence of novelty**. The example is elementary and may well be standard.

The 2022 primary finite-memory paper defines the value as a supremum and proves epsilon-optimality, not general attainment. A 2005 learning paper assumes connectedness, explicitly excluding our noncommunicating example. Publisher access failed for other average-reward leads; no uninspected result is used.

## 4. State of the art

| Result | Hypotheses / limit | Primary source inspected |
|---|---|---|
| Every epsilon>0 admits a finite-memory epsilon-optimal policy | Finite state/action/observation sets, bounded reward; expected liminf-average | [Chatterjee–Saona–Ziliotto, arXiv:1904.13360v2](https://arxiv.org/html/1904.13360), Theorem 2.9; primary model and theorem read |
| Approximation promise problem is r.e. but undecidable; no computable general memory bound | Their Definition 3.1 promise problem; undecidability lower bound attributed to earlier work | Same source, §3.1, Corollary 3.2 and Remark 3.3; primary text read |
| Near-optimal learning without resets, under connectedness | Does not include our absorbing example | [Even-Dar–Kakade–Mansour, IJCAI 2005](https://homes.cs.washington.edu/~sham/papers/rl/learn_pomdp.pdf), §2 and Theorems 4.1/4.5; primary PDF read |

These references provide context, not premises of the nonattainment proof. Full access limits are in the source ledger.

## 5. Results and exercised evidence

The example has an unobserved readiness transition, then an irreversible commit. After n waits, commit succeeds with probability `1−2^(−n)`. Never committing earns zero. Every policy reduces, before commit, to a privately randomized waiting time N independent of the hidden transitions:

\[
J(\pi)=\sum_{n\ge0}P(N=n)(1-2^{-n}),\qquad
1-J(\pi)=P(N=\infty)+\sum_{n\ge0}P(N=n)2^{-n}>0.
\]

| Claim | Evidence / scope |
|---|---|
| Supremum 1 is unattained for every admissible all-history randomized policy | **PROVED**, written all-policy argument; Certification, novelty unclear |
| Every policy is explicitly improvable; finite-memory epsilon-optimal counters exist | **PROVED**, including heavy-tailed waiting-time laws |
| Nonattainment already within randomized memoryless and fixed-size randomized controllers | **PROVED**, exact stationary gain `(1−c)/(1+c)` for c>0, but gain 0 at c=0 |
| Deterministic time-homogeneous k-state controllers, no external clock, do attain their restricted maximum | **PROVED**, restricted value `1−2^(−(k−1))`; not confused with unrestricted policies |
| Readiness observed instead of hidden removes this obstruction | **PROVED**, full-observation positive control |
| State propagation, first-commit mixtures and changed-model rejection | **COMPUTED+VERIFIED**, 90 deterministic checks, 20 stationary-mixture checks, 3 negative controls; not a proof of the infinite quantifier |

Actual smoke command from the repository root:

```sh
python3 -B information-science/average-reward-pomdp-nonattainment/work/check_nonattainment.py \
  --output information-science/average-reward-pomdp-nonattainment/evidence/exact-checks.json
```

Observed: `PASS`; 90 deterministic checks, 20 stationary checks, all 3 invalid-model controls rejected. [Output](evidence/exact-checks.json), [command/source receipt](evidence/exact-check-receipt.json). Python standard library only. An isolated replay may pass a different `--output` path; it will not rewrite delivered evidence.

## 6. Independent review and dispositions

Configured other-vendor reviewer: **Claude Opus 5.5, max**, no tools, embedded proof only. Both runs exited successfully. [First report](review/claude-referee.result.md), [first receipt](review/receipt.json), [second report](review/claude-referee-2.result.md), [second receipt](review/receipt-2.json).

| Finding | Disposition |
|---|---|
| 1 Major: the book-model match was only paraphrased | **Fixed:** neutral theorem title, verbatim Chinese/translation/formula, inspected-source limits, explicit expectation and policy-class conditions |
| 2: nonattainment is not an undecidability or synthesis result | **Fixed:** “no map, computable or not”; existence-decision and conditional-synthesis readings excluded |
| 3: pathwise criteria need not have the same answer | **Fixed:** expected criteria separated from ess inf / ess sup |
| 4: restricted deterministic policy classes can attain a maximum | **Fixed:** exact fixed-k result, time-homogeneity and no-clock qualifications |
| 5: citation scope and attribution were vague | **Fixed:** exact primary locators and criterion; earlier undecidability attribution preserved; parent checked those sources, no-tools reviewer did not |
| 6: private-randomness reduction and null conditioning needed precision | **Fixed:** explicit behavioral kernels and joint-probability chain rule |
| 7: strict-improvement and compactness wording | **Fixed:** explicit improvement map and failure of upper semicontinuity |

Second verdict: **ACCEPT**, no mathematical error or scope overclaim. Its optional clarifications were applied: general-policy reading made explicit, citation-check provenance stated, epsilon≥1 handled, deterministic clock convention clarified. Those final local wording/boundary clarifications postdate the second proof snapshot and add no substantive theorem. Source images were inspected by this package's author, not independently by the no-tools reviewer.

## 7. Book-level verdict

The literal universal request to return an **expected-average** maximizing all-history policy is impossible without extra hypotheses: a maximizing policy may not exist. That precise claim has a complete negative answer. The book prints no expectation symbol and also discusses a broader methodology; neither ambiguity is silently removed. This dossier is **not** counted as a newly solved, previously open general POMDP problem.

## 8. Next steps

No missing proof obligation remains for R1. Any further research must choose a genuinely different target: existence classification on a specified recurrent class, optimizer synthesis when existence is promised, or epsilon-optimal value/synthesis under explicit computational assumptions. Priority for the elementary example remains unestablished; no publication or external contact is authorized or undertaken.
