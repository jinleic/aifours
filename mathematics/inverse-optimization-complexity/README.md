# Inverse optimization complexity

**Outcome: partial resolution and corrected problem scope; the book's broad question is not solved here.** The standard full-linear binary case with a supplied feasible solution was already solved affirmatively by Schulz (2009). We reproduce that theorem, prove additional boundary results, and retain a precisely stated general-objective question. No natural NP-hard-forward/P-inverse counterexample was obtained.

## Source

- **Book:** 《10000个科学难题·数学卷》 (*10000 Selected Problems in Sciences: Mathematics*), Science Press, 2009.
- **Problem:** 组合优化反问题的计算复杂性 — *Relationship Between Inverse Problem and Direct Problem of Combinatorial Optimization*.
- **Author:** 杨晓光 (Xiaoguang Yang), Chinese Academy of Sciences, Academy of Mathematics and Systems Science.
- **Printed pages:** 535–536. **PDF pages:** 551–552.
- **Local excerpt:** [`sources/book-excerpt.txt`](sources/book-excerpt.txt). Extracted from `/Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf` with:

  ```sh
  pdftotext -layout -f 551 -l 552 "/Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf" mathematics/inverse-optimization-complexity/sources/book-excerpt.txt
  ```

The book's Ahuja–Orlin reference has inaccurate journal metadata. The journal paper is *Operations Research* **49**(5), 771–783 (2001), DOI [10.1287/opre.49.5.771.10607](https://doi.org/10.1287/opre.49.5.771.10607), not the printed 2000/35 entry.

## Problem

Heuberger's exact question, Section 5 item 1, author-manuscript PDF page 23, is:

> Consider the following “inverse” question: Given an optimization problem (2.1) with a polynomially solvable inverse problem (2.2) (for all c and x̂). What does this imply for the complexity of the original problem (2.1)? Does it necessarily belong to P?

Primary source: [Heuberger (2004), DOI 10.1023/B:JOCO.0000038914.26975.9b](https://doi.org/10.1023/B%3AJOCO.0000038914.26975.9b); full local manuscript [`sources/heuberger-2004.pdf`](sources/heuberger-2004.pdf), text lines 1250–1256. His model in equations (2.1)–(2.2) allows general fixed objectives f(c,x), feasible sets F_g contained in R^n, supplied feasible targets, multiple feasible sets, and optional lower/upper bounds on modified costs. It is broader than full-linear binary optimization. His norm discussion is not a theorem that sum-Hamming and bottleneck-Hamming have the same complexity.

### Explicit standard model

An instance descriptor I defines F(I) contained in {0,1}^n, with n polynomially bounded and polynomial-time feasibility checking. The objective is min c·x, with **every signed rational c allowed** and F independent of c. Forward optimization returns an optimizer or reports emptiness. Its known-start version additionally receives x_start in F. The inverse input receives c, a **feasible** x0 in F, and strictly positive rational weights. It minimizes the distance between c and a rational d subject to x0 minimizing d·x. Ties are permitted; no uniqueness is required. Modified costs are unrestricted in the main model.

Distances are weighted l1, weighted l-infinity, squared weighted l2, **sum-Hamming** (sum of weights of changed coordinates), and **bottleneck-Hamming** (maximum such weight, or zero). Integers/rational numerators/denominators are binary-encoded, all input bits count, and answers are exact, not approximate or pseudopolynomial. Full definitions, existence/output-size arguments, and proofs are in [`proof.md`](proof.md), Section 2.

### Retained general-objective research target

To avoid claiming that a solved special case is still open, the active refinement is now **the general-objective converse**, spelled out in `proof.md` Section 8e: polynomial-time rational objectives f_n(c,x), polynomial output bit length, binary feasible solutions with polynomial membership and a supplied feasible start, all rational parameter vectors allowed, f_n(0,x)=0, exact weighted-l1 inverse optimization for all feasible targets, with an explicit attainment and polynomial-rational-output premise. Does inverse in P imply forward global optimization in P?

The normalization excludes artificial inverse infeasibility; the supplied start excludes feasibility-only hardness. **This exact encoded refinement is ours, motivated by Heuberger and the 2025 broad-open statement; no opened source states every one of these restrictions verbatim. Its global literature status is not independently certified.** The broad book question remains unresolved in this dossier, not replaced by a trivial counterexample.

## Status as of 2026-10-14

| Scope | Status and opened primary evidence |
|---|---|
| Full-linear binary objectives, arbitrary cost replacements, explicitly known feasible start | **Solved affirmatively in prior literature.** Schulz, [DOI 10.1007/978-3-540-76796-1_19](https://doi.org/10.1007/978-3-540-76796-1_19), Assumptions 1–2 and Theorem 1, proves oracle-polynomial equivalence of forward optimization, inverse l1/l-infinity optimization, and optimality verification. Full author manuscript opened. |
| The book's broad converse | **Open according to the latest directly opened broad survey statement:** Guan–Pardalos–Zhang, July 2025, [DOI 10.1007/978-3-031-91175-0_1](https://doi.org/10.1007/978-3-031-91175-0_1). Its public abstract explicitly calls NP-hard-forward/P-inverse “an unresolved challenge.” Full chapter unavailable. This does not override Schulz's specific theorem; the search is not proof that no later 2026 result exists. |
| General mixed-integer inverse complexity | **Substantially classified, under a different target convention.** Bulut–Ralphs (2021), [arXiv:2104.09002](https://arxiv.org/abs/2104.09002), [DOI 10.1137/20M1377369](https://doi.org/10.1137/20M1377369): inverse primal-bound verification coNP-complete, dual-bound verification NP-complete, exact-value verification DP-complete. Their S+=S union {x0} allows targets outside S; this is not automatically a promised-feasible-target result. |
| Full-cost binary model without an available feasible start and without dummy closure | **Not resolved here.** Our additional Proposition U shows an NP-hard forward threshold problem with a polynomial inverse would imply NP=UP; this is not a P!=NP contradiction. |
| General normalized nonlinear refinement above | **OPEN here, not solved by the reproduced linear theorem.** Bottleneck and independently parametrized recoverable binary-feature subcases are eliminated by complete proofs below. |

## State of the art

1. **Forward-to-inverse direction:** Heuberger Theorem 3.3 states the Ahuja–Orlin/Yang–Zhang weighted-l1 separation/ellipsoid theorem. The weighted-infinity LP follows from the same argument; Schulz Lemma 4 gives the unweighted infinity case explicitly. Neither argument establishes the same statement for sum-Hamming. The inaccessible Ahuja journal PDF is not falsely counted as read; see the access ledger.
2. **The decisive converse:** [Schulz (2009)](https://doi.org/10.1007/978-3-540-76796-1_19), full manuscript [`sources/schulz-2009.pdf`](sources/schulz-2009.pdf), supplies exactly the missing verification-to-optimization connection for binary linear problems, with known start and arbitrary signed costs. We reproduce Lemma 19's target-coordinate penalties and Lemma 5's bit scaling. This is prior art, not a new solution.
3. **Huang's 2005 algorithms are pseudopolynomial:** [DOI 10.1007/11496199_45](https://doi.org/10.1007/11496199_45), publisher abstract opened. It says this for inverse knapsack and inverse integer programming with a fixed number of constraints. It is not a P-inverse/NP-hard-forward counterexample in binary encoding.
4. **Berg–Hempel is a different inverse notion:** [DOI 10.1007/978-0-387-09680-3_5](https://doi.org/10.1007/978-0-387-09680-3_5), full PDF opened. Its input is an explicit set of verifier certificates; the task asks for an instance having exactly those certificates. It does not minimize cost changes making a supplied solution optimal.
5. **Recent general Hamming/infinity algorithms:** Bérczi–Mendoza-Cadena–Varga, [arXiv:2302.13411](https://arxiv.org/abs/2302.13411), [DOI 10.1007/s11590-024-02183-0](https://doi.org/10.1007/s11590-024-02183-0): O(n) forward-oracle calls for the constrained weighted **bottleneck-Hamming** Newton algorithm, improved to O(log n) calls by the journal version's binary-search algorithm; a pseudopolynomial Newton-type weighted-infinity algorithm, strongly polynomial for unit weights with a matching forward oracle; and an exact unconstrained weighted-infinity min-max formula. The weighted-infinity algorithm's bound does not negate older weakly polynomial ellipsoid solvability. Both the preprint and final journal PDF were opened and saved.
6. **Partial inverse targets are genuinely different:** Ley–Merkert (2025), [DOI 10.1007/s10898-025-01529-x](https://doi.org/10.1007/s10898-025-01529-x), full open-access article: with weight increases only, partial inverse shortest path on DAGs and partial inverse assignment are NP-complete even with one required arc/edge. These demonstrate the *opposite* complexity direction and do not settle the book's converse.
7. **Center-location precedent:** Cai–Yang–Zhang (1999), [DOI 10.1023/A:1008360312607](https://doi.org/10.1023/A%3A1008360312607), opened primary abstract proves inverse NP-hardness despite polynomial forward optimization. The book's adjective “strongly” was not verified against the unavailable full original proof; we do not strengthen the abstract's claim.
8. **Demange–Monnot:** [DOI 10.1002/9781119005353.ch17](https://doi.org/10.1002/9781119005353.ch17), metadata verified, but publisher/PDF endpoints returned 403 and no accessible author manuscript was located. **[UNVERIFIED]** what this chapter says about the converse; no result is attributed to its unseen contents.
9. **Rejected claimed resolution:** Huang, [arXiv:2103.15337](https://arxiv.org/abs/2103.15337), studies inverse KKT points, not necessarily global optima, and its Theorem 4.4 infers a universal no-KKT certificate from checking one candidate. That inference is invalid. We do not accept its claimed coNP=NP proof; this is a critique of its argument, not a proof of NP!=coNP.

Detailed excerpts, exact scope caveats, and access failures: [`sources/literature-notes.md`](sources/literature-notes.md). Download provenance/hashes: [`evidence/source-downloads.json`](evidence/source-downloads.json).

## Attack

### Completed mathematical work

- **Reconstructed the correct converse:** exact inverse optimum zero iff the target is already optimal. A big-M target-agreement test recovers a strictly improving binary point in at most n+1 yes/no optimality calls. Bit scaling then obtains a forward optimum in O(n² L) verification calls, where L is the bit length after rational denominator clearing. No hidden optimizing oracle or feasible-set restriction is used. This reproduces Schulz with explicit promises.
- **Norm and domain boundaries:** the same converse works for exact weighted l2 and either positive-weight Hamming variant because only their zero test is needed. Nonnegative costs suffice for constant-cardinality families by common coefficient shifts.
- **Feasibility obstruction:** an explicit dummy-solution closure supplies an initial point and detects original infeasibility. Without closure, unique lexicographic optimality certificates put the threshold language in UP. A separate hidden-singleton oracle proof explains why membership/inverse black boxes alone cannot generically locate the first point; it is explicitly not an explicit NP-hard construction.
- **Attacked the nonlinear bottleneck case:** for f(c,X)=max_{i in X} c_i and nonempty feasible objects, 0/1 cost queries at the *same supplied target* decide whether any feasible object lies inside an arbitrary allowed set. Binary search and greedy deletion then find a bottleneck optimum in O(n+log n) verification calls. This eliminates bottleneck-with-known-start as a candidate, rather than assuming the linear theorem covers it.
- **Attacked nonlinear feature objectives:** polynomially many independently mutable binary features containing the original coordinates lift to the solved binary model. Fully parametrized pseudo-Boolean polynomial objectives with linear terms are therefore not counterexamples either.
- **Retained but did not promote degenerate examples:** SAT witnesses times a free Boolean cube, with witness costs fixed to zero, has NP-hard feasibility-bearing forward optimization and a coordinate-clipping inverse in P for all five distances. Uniform-cost Hamiltonian cycles give a familiar but equally feasibility-only example. These **do not** solve the intended nondegenerate question or refute the full-cost theorem. The checker includes a negative control showing clipping fails when witness costs are freed.

### Failed/limited routes

The initial normal-cone/max-mean direction was superseded by the simpler established Schulz reduction; no new result is claimed from that exploration. A polynomial optimum-checker alone cannot be treated as a forward optimizer without constructing the missing search reduction. For arbitrary normalized f(c,x), target-coordinate penalties may not be expressible through admissible parameter changes and binary coefficient scaling may not preserve objective comparisons. Our bottleneck threshold and feature-lifting methods do not bridge that gap. KKT certification, partial inverse observations, pseudopolynomial algorithms, and certificate-set inversion were rejected as substitutions for global exact inverse optimization.

### Reproduction and exercised checks

From this directory, run:

```sh
python3 work/check.py --output evidence/check-results-extended.json
```

No external packages, solver installation, paid compute, or parallel worker pool is used. The checker runs one process (below the 4-thread cap), with exact integers and `fractions.Fraction`; seed 20261014. The exercised extended run passed:

| Check | Cases / observations |
|---|---:|
| Verification-to-augmentation vs exhaustive optimum | 27,948 cases |
| Forward reduction vs exhaustive optimum | 28,188 cases; 116,116 verifier calls |
| Dummy closure, including empty original feasible sets | 7,068 cases |
| Weighted-infinity formula vs independent exact LP vertex enumeration | 160 cases; 1,913 feasible LP vertices |
| SAT-to-restricted-family feasibility/threshold reduction | 81 formulas |
| Restricted inverse clipping | 8,640 cases; 43,200 comparisons across five distances |
| Uniform Hamiltonian-cycle illustration | 216 graph/cost cases |
| Unique-optimum threshold certificate | 49,140 cases |
| Nonlinear bottleneck reduction | 12,207 cases; 29,931 verifier calls |
| Invalid full-cost extension of clipping | 1 required negative control |

Authoritative result: [`evidence/check-results-extended.json`](evidence/check-results-extended.json), including source hashes. The earlier run is preserved separately. Finite tests are sanity checks, not the proof of the universal statements. The independent LP checker does not call the min-max formula being tested.

## Claims

| Claim | Status | Evidence path |
|---|---|---|
| Full-linear binary known-start inverse-P implies forward-P | PROVED | `proof.md` §§3–5; `sources/schulz-2009.pdf`, Theorem 1 |
| Exact weighted l2 and both Hamming zero tests yield the same converse | PROVED | `proof.md` Lemma Z and Theorem F |
| Dummy closure removes the first-feasible-point obstruction | PROVED | `proof.md` Theorem G |
| Full-cost inverse-P implies threshold language in UP | PROVED | `proof.md` Proposition U |
| Membership-only hidden-singleton model has an exponential oracle obstruction | PROVED | `proof.md` Proposition O; explicitly oracle-only |
| Known-start minmax/bottleneck converse | PROVED | `proof.md` Theorem B |
| Independent recoverable binary-feature converse | PROVED | `proof.md` §8d |
| Restricted-cost feasibility-only NP-hard-forward/P-inverse example | PROVED | `proof.md` Proposition C; explicitly not the full-cost question |
| Weighted-infinity min-max characterization | PROVED | `proof.md` Proposition L; `sources/berczi-mendoza-varga.pdf`, Theorem 14 |
| Exact finite sanity checks and independent LP comparisons | COMPUTED+VERIFIED | `evidence/check-results-extended.json`; `work/check.py` |
| Clipping still works after freeing SAT-witness costs | REFUTED | `proof.md` §7 negative example; checker negative control |
| Huang's Theorem 4.4 establishes the claimed universal certificate | REFUTED | `sources/huang-2021.txt:367-377`; `sources/literature-notes.md` |
| Normalized general-objective converse, with known start | OPEN | `proof.md` §8e; broad literature context in 2025 publisher abstract |
| Full-cost converse with no feasible start and no closure | OPEN | `proof.md` §§8a–8b and §9; status unresolved here, not a certified literature-wide claim |

## Independent review

The required Codex CLI review used the live registry's `gpt-6.1-sol`, effort `max`, `--sandbox read-only --ephemeral --skip-git-repo-check`, with a prompt restricting reads to this target and forbidding further delegation. Commands, model, PID, timestamps, and proof hashes are recorded in [`evidence/proof-review-run.json`](evidence/proof-review-run.json).

The first verdict was **READY-WITH-FIXES**: no mathematical flaw in the principal reductions under their promises; one low-severity attribution correction. It correctly noted that Heuberger Theorem 3.3 explicitly covers weighted l1, not both norms. The attribution in `proof.md` Section 5 has been repaired; the infinity-norm argument remains justified separately. The referee explicitly agrees that the natural counterexample was not supplied and the broad question is not solved. Verbatim review: [`evidence/proof-review.md`](evidence/proof-review.md).

The added UP/oracle/bottleneck/feature/general-objective sections received a separate focused review: **READY**, no mandatory mathematical corrections. The referee confirmed each added argument and expressly stated that neither the book's general question nor the exact refinement's literature status is settled by this dossier. Verbatim output: [`evidence/extension-review.md`](evidence/extension-review.md); pinned proof hash/command: [`evidence/extension-review-run.json`](evidence/extension-review-run.json); all resolutions: [`evidence/review-resolution.md`](evidence/review-resolution.md). Both reviewer processes exited normally.

## Next steps

**Selection decision:** the parent retired this target from the five-open-problem selection. Seymour's second-neighborhood conjecture was proposed next, but its later September 2026 OpenAI/math family-173 full-proof claim superseded the July open-status source; that short intake is preserved separately. The active replacement is the book's nonsymmetrizable Kac–Moody defining-relations conjecture (pp.226–227), in `../kac-moody-serre-relations/`. This folder remains a partial investigation, not a newly solved book problem. The actions below describe its unresolved research gap, not the active replacement assignment.

1. **Resolve the general objective gap, not the solved binary case.** For the exact formulation in `proof.md` §8e, establish a parameter-based global search reduction that does not assume independently adjustable linear penalties, or produce an explicit nondegenerate objective family refuting it. A candidate must have a polynomially supplied feasible start, f(0,x)=0, an attained rational inverse optimum, and a polynomial inverse algorithm for **every** feasible target—not just a selected easy target.
2. Before claiming a natural candidate qualifies, check the already proved exclusions: full cost freedom/Schulz, bottleneck threshold-pruning, recoverable binary features, and dummy closure. If proposing an NP-hard threshold family without a start, account for the proved NP=UP consequence rather than using P!=NP alone as if it excluded that collapse.
3. Obtain the full 2025 chapter and Demange–Monnot chapter through legitimate author/institutional access, then compare their exact conventions with §8e. Current accessible abstracts cannot certify the precise refinement's community-wide open status. No paywall bypass or purchase was attempted.

This folder is a reproducible partial research dossier. It is **not** a newly solved book problem, and the standard linear rediscovery should not be counted as one of five still-open problems solved or selected anew.
