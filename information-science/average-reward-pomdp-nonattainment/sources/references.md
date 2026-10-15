# References and source-access ledger

Date: 2026-10-14, America/Los_Angeles. Search results are leads only. Correctness, novelty and scope are separate questions.

| Source | Primary material actually read | Relevance and limit |
|---|---|---|
| 汪德新, 曹希仁, 部分可观马尔可夫决策过程的性能优化, in 《10000个科学难题·信息科学卷》 (2011), pp. 653–655 | PDF pages 674–676; authoritative rendered pages are alongside this file | The displayed long-run formula has a limit of sample averages but does not explicitly display an expectation. The prose requests a policy attaining the maximum; no recurrence or existence condition is given. We use the standard expected-average interpretation and disclose that choice. |
| Chatterjee, Saona, Ziliotto, *Finite-memory strategies in POMDPs with long-run average objectives*, [arXiv:1904.13360v2](https://arxiv.org/html/1904.13360), 28 September 2022; first version 30 April 2019 | Primary full HTML, model §2.1, Theorem 2.9, Corollary 2.11, Definition 3.1 and Corollary 3.2 | Finite hidden-state/action/observation sets and bounded rewards. Every epsilon admits a finite-memory epsilon-optimal policy. Their approximation decision problem is recursively enumerable but undecidable; memory has no computable input-only bound. The value is explicitly a supremum. These facts do not establish priority for our particular four-state example. |
| Even-Dar, Kakade, Mansour, *Reinforcement Learning in POMDPs Without Resets*, IJCAI 2005, [author-hosted PDF](https://homes.cs.washington.edu/~sham/papers/rl/learn_pomdp.pdf) | Primary full six-page PDF, especially §2 and Theorems 4.1/4.5 | Their model explicitly assumes connectedness. Their existence/learning claims for connected POMDPs do not apply to our irreversible absorbing example. Do not present it as a counterexample to their theorem. Their statement “Connectivity implies ... a strategy ... that maximizes the average reward” is cited, not independently proved here. |
| Li, Yin, Xi, *Finding optimal memoryless policies of POMDPs under the expected average reward criterion*, EJOR 211(3) (2011), DOI [10.1016/j.ejor.2010.12.014](https://doi.org/10.1016/j.ejor.2010.12.014) | [UNVERIFIED full text] Publisher route [S0377221710008805](https://www.sciencedirect.com/science/article/pii/S0377221710008805) returned HTTP 403; title/metadata were search leads only | No theorem or assumption from this inaccessible paper is used. A memoryless-policy result would not by itself settle all-history optimization. |
| DOI [10.1287/moor.9.4.558](https://pubsonline.informs.org/doi/10.1287/moor.9.4.558) | [UNVERIFIED] Publisher returned HTTP 403 | Search lead only; not used to attribute nonattainment or state a theorem. |

## Search scope and novelty

Queries included `finite POMDP average reward optimal policy need not exist`, `POMDP average reward supremum attained`, and blind-model waiting/stopping examples. Accessible primary literature supplies the general epsilon-optimality and complexity context. No accessible source read in this round was verified to contain this exact four-state transition table. That is **not evidence of novelty**: the construction is elementary, and no priority claim is made.

## Source PDF pin

Original: `/Users/jinleic/Documents/中文pdf/10000个科学难题·信息科学卷(10000个科学难题信息科学编委会).pdf`.
SHA-256: `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db`.
