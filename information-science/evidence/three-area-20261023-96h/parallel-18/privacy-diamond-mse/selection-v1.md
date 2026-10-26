# Frozen info-1 selection: diamond-sensitivity planar MSE

Startup observed clock: **2026-10-23T14:46:06-0700**. Owner: `InfoResearch96h`; slot: `info-1`. This selection binds the complete parent amendment [info-1-replacement-v1.json](../../../../../institute/runs/three-area-2026-10-23-96h/info-1-replacement-v1.json), SHA-256 `6bff9ae10614c3537b81a4aaf5433a6561e9ebda8899ecfcc2164e311876dfca`. The October 27, 2026 12:35:38 PDT hard deadline is unchanged. Only this new root is writable. The former `../sof24/` root is read-only retirement evidence; P34 is an inactive recorded alternative, not a second investigation.

**Selection status: UNCERTIFIED-OPEN / NOVELTY_UNCLEAR.** No scientific-program, solver, exact-verifier, model-CLI or nested-agent execution is authorized. Written reasoning only. The parent's timestamp and verification errata remain mandatory; no formal/kernel verification is claimed.

## 1. Exact primary question

Write `D={h in R^2: |h1|+|h2|<=1}`. For every epsilon>0 let M(epsilon) consist of **all Borel probability measures** mu on R^2 satisfying

`mu(E) <= exp(epsilon) mu(E+h)`

for **every** Borel E and **every** h in D. These are query-output-independent additive pure-DP noise laws for the entire prescribed sensitivity diamond, not for discrete shifts, Euclidean sensitivity, approximate DP, independent coordinate noise, or data-dependent mechanisms. Set

`V(epsilon)=inf_{mu in M(epsilon)} integral (x1^2+x2^2) dmu(x)`.

For b=exp(-epsilon) and gamma in [0,1], define f_gamma(x) up to its unique probability normalization by

- `b^k` if `||x||_1 in [k,k+gamma)`;
- `b^(k+1)` if `||x||_1 in [k+gamma,k+1)`;

for integers k>=0. Endpoint parameters use their normalized almost-everywhere meaning. The frozen question is:

**For every epsilon>0, is V(epsilon) equal to the minimum squared-Euclidean cost over this entire diamond-staircase family?**

A complete affirmative answer must prove the global all-law lower bound and attainment for all epsilon. A complete negative answer may give **one exact positive epsilon** and one fully specified admissible probability law with cost **strictly below every gamma-staircase**, thereby refuting the literal conjecture. Such a refutation would not by itself determine V(epsilon), its minimizer, an all-epsilon alternative family, or the full book question.

## 2. Exact book provenance and primary conjecture

*10000 Selected Problems in Sciences: Information Science*, Science Press 2011, ISBN 978-7-03-031911-1: Yang Xiaochun and Yu Ge, **Privacy Protection for Sensitive Data**, printed pp.583–586 / PDF pp.604–607. The actual p.583 image was opened, and the four-page extraction was read at its substantive problem statements and author attribution. The article asks how to evaluate shared-data usefulness and trade privacy/security against information loss. **It does not literally state differential privacy or the exact planar optimization here.** This target is a precise modern subquestion of the printed tradeoff, not the full-book problem.

Read-only source records:

- `../sof24/source-excerpts/book-privacy-583-586.txt`, SHA-256 `014581a2312b2e68d6bab236a8be8f4f84e77f1f78d7fdf13baac1257f0806d0`;
- `../sof24/source-excerpts/book-privacy-0604.png`, actually opened source image;
- routed source-volume SHA-256 `9b3f16ee6b558f7c289a7208cec01a9811091863631d09908b8f4cb66d2027db` (not rehashed here).

[Quan Geng and Pramod Viswanath, arXiv:1312.0655v1](https://arxiv.org/html/1312.0655), model in Section II and **last paragraph of Section III**, supplies the literal d=2 conjecture for `L(x)=||x||_2^2` under the l1-sensitivity model. It explicitly says that a different proof technique is needed because layer averaging does not work for costs not depending only on the l1 norm. The paragraph and theorem/model interfaces were actually read.

## 3. Matched baseline and current-source firewall

The complete two-proposal screen, sources, access boundaries and corpus matches are preserved at [replacement-target-screen-v1.md](../sof24/replacement-target-screen-v1.md), SHA-256 `83cc147391a3588bb7484a5f3fe7d8d716222039425588d0bfd8f02bedd9918f`. No open-status inference is made from a search miss alone.

- Geng–Kairouz–Oh–Viswanath 2015: [actual journal PDF](https://pramodv.ece.illinois.edu/pubs/GKOV.pdf), DOI10.1109/JSTSP.2015.2425831; printed p.1179 image opened. Equation(9) gives the full l1 privacy constraint; equation(10)/Theorem1 prove optimality for **l1 loss**, not the frozen mixed cost.
- Kulesza–Suresh–Wang [AISTATS2025](https://proceedings.mlr.press/v258/kulesza25a.html): actual paper Sections1–3, Definition5 and Theorems1/2 use **the same K norm** for sensitivity and theoretical loss. The [GoogleResearch repository README](https://github.com/google-research/google-research/tree/master/general_staircase_mechanism) claims implementation/experiments for that result. No mixed-cost theorem was identified at the read interface.
- Melbourne–Diaz–Asoodeh [arXiv:2601.14597v1](https://arxiv.org/html/2601.14597): actual model and **Assumption1** require `Phi(x)=varphi(||x||)` for the same norm as sensitivity. Squared Euclidean cost is not l1-radial: `(1,0)` and `(1/2,1/2)` both have l1 norm1 but costs1 and1/2. Choosing the Euclidean norm changes the privacy set and does not settle this question.
- Amorino–Gloter [2603.27572](https://arxiv.org/abs/2603.27572) is local-DP Fisher-information optimization (abstract read); Hillebrand et al.'s [2026 TPDP preprint](https://tpdp.journalprivacyconfidentiality.org/2026/pdfs/hillebrand.pdf) uses integer-valued discrete-Laplace postprocessing and unbiased estimation (abstract/introduction/model read). Neither accessible statement covers the frozen all-continuous-shifts model.

The actual EulerSolve full listing, retained remote/current-local openai/math catalogs, public AIM record, GoogleResearch implementation README and targeted later-claim/repository searches were checked before this freeze; precise screening scope and hashes are in the screen. No matched resolution was located, but **global current openness/novelty is not certified**. The all-dimension same-norm staircase conjecture is already resolved and is not our target.

## 4. First consequential action and missing ingredient

First reconstruct the **complete normalized staircase second-moment function** and its global gamma minimum, including endpoints and tails. Then examine non-homothetic superlevel sets: successive levels can expand by the sensitivity diamond while the initial level is a different shape. Do not assume such a family is optimal or even feasible until every-shift privacy is proved.

The missing ingredient is either:

1. an explicit non-diamond law with a rigorous every-shift DP proof and exact full-tail cost bound below the **global** staircase-family minimum; or
2. a genuinely new all-law dual/rearrangement inequality proving that none can improve the optimized diamond staircase.

A finite grid, sampled gamma, truncated tail without a bound, scalar-coordinate comparison, lower cost than Laplace alone, or reuse of the same-norm theorem is not sufficient. The first research checkpoint must contain a complete written claim delta or an exact obstruction, not an experiment plan.

## 5. Verification, preservation and redirect

For a negative candidate, independently check normalization, integrability, all-shift privacy (including density interfaces up to null sets), exact global staircase lower bound, every infinite-tail estimate and strict inequality at its explicit parameter. Parent and independent in-harness written reconstruction must be scoped separately from formal verification, finite calculation, prior-art status and publication novelty. Any future scientific execution needs a fresh exact resource/control request and GO; this selection grants none.

All previous candidates and source corrections retain their qualifications. P24/P33/source-sign correction are prior-claimed, not counted as current unsolved targets. The surrogate stack retains Kuroki ACCESS_BLOCKED; it is not a new primary here. New evidence is English and exclusive to this root.

Redirect only when a current primary source covers the **exact** mixed interface, or a complete obstruction closes the bounded chosen route without solving the conjecture. Preserve the obstruction and ask parent to bind a genuinely new representation/target; P34 remains only the pre-screened alternative. An access/quota gate is not mathematical exhaustion.
