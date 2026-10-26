# Source boundary for the unrestricted low-privacy candidate

Observed clock before creation: **2026-10-23T15:14:04-0700**. This is a bounded source-interface companion to [proof-unrestricted-low-privacy-constant-v1.md](proof-unrestricted-low-privacy-constant-v1.md), SHA-256 `2a7c0e4ad18fcbed81ab119e5634b112e39b9252403752c2ea20c2c18865eeff`. It neither changes that frozen manuscript nor transfers the octagonal packet's mathematical verdict to it. **NOVELTY_UNCLEAR; no execution or publication/contact.**

## 1. Exact possible delta, not the known ingredients

The candidate statements are solely:

- for **every Borel noise law** satisfying the frozen all-continuous-diamond translation constraint, the finite-b lower bound `V_b >= 2 sqrt(b/(3pi)+b^2/pi^2) - 2b/pi`;
- the matching unrestricted leading asymptotic `V_b/sqrt(b) -> 2/sqrt(3pi)` as b=exp(-epsilon) tends to zero.

They do not assert the exact finite-b optimum, an optimal finite-b core, a new general privacy mechanism, a new absolute-continuity principle, or a new bathtub inequality. The complete author proof independently derives every measure/cap/tail step, but independent derivation alone does not establish priority.

Known/prior ingredients explicitly retained:

1. **Arbitrary cores and Minkowski reachability shells:** SCDF2013 Section6/Theorem13 construction, authenticated/pinned in [the prior-mechanism addendum](proof-diamond-staircase-counterexample-ADDENDUM-1-prior-mechanism.md). For sufficiently small b the disk core is coordinate-downward and lies inside D, so the upper family is contained. No claim of a new mechanism.
2. **Absolute continuity under a fixed positive-radius shift comparison:** Melbourne–Diaz–Asoodeh [arXiv:2601.14597v1](https://arxiv.org/html/2601.14597v1), AppendixA-A, **Theorem7**, expressly states this for all Borel sets and all shifts in a norm ball. The actual statement and its surrounding proof interface were read in this follow-on screen. This is prior theorem-level treatment of that intermediate fact; we neither import nor certify its full proof here. Our short null-set integration is a standalone proof, not claimed as a novel absolute-continuity result.
3. **Geometric density-level expansion:** the same January2026 paper's Theorem3 and SCDF's earlier construction. Again not new.
4. **The density-cap quadratic-moment/bathtub principle and Tonelli/Radon–Nikodym/AM–GM tools:** not claimed as inventions. The manuscript proves the exact planar cap constant used and supplies its own null-set/essential-peak argument rather than relying on an unread citation.

The exact combination yielding the frozen **mixed** full-diamond/squared-Euclidean optimum constant is the only further possible scientific delta. No current novelty clearance is implied by the list above.

## 2. Current-version and model checks

The actual public arXiv API queries for [2601.14597](https://export.arxiv.org/api/query?id_list=2601.14597) and [1312.0655](https://export.arxiv.org/api/query?id_list=1312.0655) returned the **v1** entry links. This is a version-identity check, not a new theorem verification. The actual [Geng–Viswanath record](https://arxiv.org/abs/1312.0655) gives December2,2013; the actual [Melbourne–Diaz–Asoodeh record](https://arxiv.org/abs/2601.14597) gives January21,2026.

The January2026 optimality result still imposes **Assumption1: `Phi(x)=varphi(||x||)` with the same norm as sensitivity**. Its absolute-continuity and level-set tools are more general, but the final cost-optimality assertion cannot simply be applied to squared-Euclidean cost with diamond sensitivity. The source's related-work discussion describes vector optimality under Gaussian/log-concave restrictions, other privacy notions and large-composition/small-sensitivity limits; those are not silently used as claims about epsilon tending to infinity in this frozen model.

The 2025 [general-staircase paper](https://proceedings.mlr.press/v258/kulesza25a.html) likewise uses the same K norm for its theoretical error. Its **public notebook was now read beyond the README**, at the actual experiment-scope comments and metric implementations:

[General_staircase_mechanism_exp_aistats_2025.ipynb](https://raw.githubusercontent.com/google-research/google-research/master/general_staircase_mechanism/General_staircase_mechanism_exp_aistats_2025.ipynb).

The Markdown cell immediately before gamma optimization says the experiments use gamma-star known optimal **when the target metric norm matches K**. Later cells compare K shapes against several target norms empirically; the displayed `MetricEval` for ell2 uses the norm itself, not its square. These are comparisons with vanilla K-norm/Laplace and gamma sensitivity, not an authenticated exact non-homothetic-core/all-law mixed-MSE theorem. No notebook code or experiment was executed. The source was read only.

## 3. Strong-looking later/older claims screened at actual interfaces

The earlier [bounded comparison audit](source-audit-comparison-v1.md), SHA-256 `6d0b131cbd5b26c2af603d78ad15d510b808cf094f2688ac3de7f0dfcd131485`, records 75 indexed SCDF-citing titles and the strongest matching primary model interfaces. It is not an exhaustive read of those manuscripts. The same model distinctions remain relevant to the new asymptotic; no automatic negative novelty result is inferred from a title.

Two additional direct interfaces were opened in this follow-on screen:

- **Koufogiannis–Han–Pappas, Optimality of the Laplace Mechanism in Differential Privacy**, [arXiv:1504.00065v2](https://arxiv.org/html/1504.00065), April7,2015. The actual Introduction and **Definition2/eq.(4)** were read, not just the abstract. Their Lipschitz privacy bounds log-probability differences by epsilon times the input distance **for every pair**. The current model only requires the fixed factor exp(epsilon) for all shifts of l1 length at most1; it permits geometric density jumps. The stronger metric assumption therefore changes the feasible class. Its MSE-optimal Laplace theorem does not establish the present optimum or contradict the candidate.
- **Pihur, The Podium Mechanism: Improving on the Laplace and Staircase Mechanisms**, [arXiv:1905.00191v2](https://arxiv.org/html/1905.00191), August1,2019. The actual abstract, Introduction and local bounded-input model were read. It explicitly changes the finite-support noise distribution's shape **depending on the input value**, rather than using one translation-independent noise law over the plane. Its direct “improving staircase” title is not a matched prior proof of the frozen planar additive comparison or asymptotic.

Other actually checked primary interfaces, detailed in the linked audit, include scalar distributionally-robust optimization, large-composition KL-optimal Cactus/multidimensional mechanisms, discrete noise, local/shuffle Minkowski Response and same-norm norm-monotone costs. No exact matched all-law low-privacy constant was located at those read interfaces. This is a bounded finding, not proof of absence elsewhere.

## 4. Operative status and next gate

- The **octagonal strict comparison** has its own in-harness written disposition, recorded separately by the parent. That does not verify this stronger packet.
- The **finite-b all-law bound and leading unrestricted optimum** remain **CANDIDATE** until their own actual independent and parent reconstructions are returned and read.
- Mechanism priority is **PRIOR**, and the general measure/geometric tools are known, not extra discoveries.
- The precise mixed-model asymptotic's priority remains **NOVELTY_UNCLEAR**. No worldwide novelty, publication readiness, formal verification or blind review is claimed.
- The frozen proof is preserved pending assignment. No extra dimension, privacy notion, program or separately counted problem has been activated.
