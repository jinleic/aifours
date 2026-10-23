# Díaz et al. Maximum Hypothesis: parent verdict

## Result

**The Maximum Hypothesis is proved by the computer-assisted certificate, with its written proof and revised checkers.** For the four-variable function F defined in the pinned Díaz–Kaporis–Kemkes–Kirousis–Pérez–Wormald preprint, over its entire closed domain Δ,

`F(n) < F(n*) = 5^(5/2)·25/24` for every `n ≠ n*`, where `n* = (1/9,1/9,1/9,1/9)`.

Boundary points and uniqueness are included. The revised Lemma F′ also proves that `b_s^u = w_s/8100` is the unique maximiser of the full spectral objective f on the paper's polytope, rather than merely computing its value.

**Graph corollary.** With Theorem 1.1 and the analytic arguments of the pinned preprint, this removes its Maximum Hypothesis and yields **χ(G_{n,5}) = 3 asymptotically almost surely**, for uniformly random simple 5-regular graphs as even n tends to infinity. The preprint was published as J. Graph Theory 61 (2009), 157–191, but its published body was not compared (publisher access returned HTTP 403). The invoked implication is therefore identified by the preprint's exact SHA, not an unverified claim of version equality.

Primary source: [author preprint](https://web.archive.org/web/20210315161735/users.monash.edu.au/~nwormald/papers/3col.pdf), pinned SHA-256 `5e317a44a75bd88fa454824ced64501b4d9eeb8c6fcd7adedeb29eb2219428b1`. Its p.4 states Hypothesis 1.1 and the conditional Theorem 1.1. Parent read those statements and the definitions of F and Δ directly.

Current proof: [CLAIM-r2.md](colour-complete-claim-snapshot-r2/CLAIM-r2.md), SHA-256 `7b593936ef3f679254c592ef58a53e8a443be22eb35f9cc2c67ca9857fd44db9`. Review fixes: [DISPOSITIONS-r2.md](colour-complete-claim-snapshot-r2/DISPOSITIONS-r2.md).

## What was certified

1. **Exact slice concavity.** A polynomial-matrix Hessian criterion reduces to positive coefficients of all 12 Sylvester-minor polynomials. The complete coefficient lists were independently reconstructed and matched. This replaces the paper's empirical inner-concavity assertion.
2. **Global weak-dual upper bounds.** A bound valid for every feasible spectral array, including empty overlap classes, produces a convex function of n. Each outer simplex is certified by checking its five vertices with outward-rounded arithmetic.
3. **Full closed-domain cover.** All nine tetrahedral facets of Δ are coned to n*. Exact rational edge-bisection trees cover all nine cones directly, without a symmetry shortcut.
4. **Unique central maximum.** An explicit local dual majorant is strictly concave on the box `|n_i−1/9| ≤ 1/10000`. Parametric Krawczyk, Loewner bounds, rational congruences and Gershgorin/Sylvester tests certify the whole box, not sampled grid points.
5. **Boundary and equality cases.** Every fibre is nonempty and compact. The boundary tangent argument and Gibbs equality prove the necessary global uniqueness at the centre and of b. The upper bound is exactly attained at n*.

## Verification evidence

| Item | Observed result | Artifact |
|---|---|---|
| Frozen inputs | All 55 r2 manifest entries SHA-verified; the original 41 entries remain unchanged | [r2 pin receipt](colour-complete-claim-snapshot-r2/parent-pin-receipt.json) |
| Slice-polynomial certificate | Parent plain-integer reconstruction, separate SymPy reconstruction, and Codex's independent integer reconstruction agree with the pinned coefficient lists; all coefficients positive. The standalone r2 program reproduces the coefficient JSON byte-for-byte | [parent derivation](slice-concavity-parent-verification.md), [parent r2 replay](colour-final-r2-parent-replay-v1/parent-result.json) |
| Outer checker A (Arb) | Parent re-execution: 9/9 cones PASS, 291,552 dual leaves, 4,616 central leaves, 296,159 splits, 0 failures | [receipt](colour-parent-replay-v1/parent-replay-result.json) |
| Outer checker B (mpmath.iv) | Independently authored worker implementation: all nine cones PASS with identical tree counts; hashes verified by parent | [pinned result](colour-complete-claim-snapshot-r2/checkerB/evidence/cells_iv_all9_final.json) |
| Independent outer checker C | Codex wrote it from the mathematical specification without access to A/B implementations. Parent ran all nine trees, 128/200-bit self-tests, a smaller positive certificate and eight intended-reason mutations: all behaved correctly | [receipt](colour-codex-checker-v1/parent-result.json) |
| Hardened central checker A | Parent r2 replay PASS: 1,728 parameter boxes and 256 overlap boxes, 0 failures. ε=0 fails; zero/negative subdivisions and optimised Python are rejected | [final r2 replay](colour-final-r2-parent-replay-v1/parent-result.json) |
| Hardened central checker B | Parent r2 replay PASS: 512 parameter boxes, 16 exact vertex tests, 0 failures. ε=0 fails; zero/negative subdivisions and optimised Python are rejected | [final r2 replay](colour-final-r2-parent-replay-v1/parent-result.json) |
| Bridge audit | The certified statement is exactly H1.1 on closed Δ; the same hypothesis serves every admissible congruence class of n in the preprint's Section 6 | [audit](colour-bridge-audit.md) |
| Central-implementation reviews | A: ACCEPT-WITH-FIXES (a vacuous-PASS guard bug for invalid grid arguments, fixed in new files). B: ACCEPT (assert-only checks hardened in new files). Neither invalidates the original positive-count, non-optimised replay | [A](colour-centralA-implementation-review.md), [B](colour-centralB-implementation-review.md) |
| Complete-claim reviews | Claude and Codex each returned ACCEPT-WITH-FIXES, with no fatal/major mathematical defect. Claude's two medium findings—spectral uniqueness and version scope—are addressed explicitly in r2 | [Claude](colour-complete-claim-hostile-review.note.md), [Codex](colour-codex-claim-review-v1/final.md) |
| Final disposition review | **Codex ACCEPT: no unresolved or incorrectly resolved finding.** It re-derived the equality/uniqueness argument, constructed all six vertex fibres exactly, checked coercivity and inspected the hardened code/receipts | [review](colour-r2-disposition-review.note.md), [identity receipt](colour-r2-disposition-review.receipt.json) |

Conservative certified bounds: outer margin ≥ **1.7270e−11**; central-A margins ≥ **0.0292** and **1.1650**; central-B parameter margin ≥ **0.0708**. Different central bases/enclosures give different intermediate margins. Both cover the same overlap box. A and C share Arb, whereas B uses mpmath.iv; separate authorship and separate arithmetic libraries are distinct forms of independence.

The final parent replay used CPython 3.13.9, python-flint 0.9.0 and mpmath 1.3.0, with optimisation disabled and PYTHONOPTIMIZE unset. No finite grid or floating-point optimiser is trusted for coverage or sign. Producers and numerical search heuristics are outside the trusted base.

## Imported trust and scope

- This is a **computer-assisted proof**, not a Lean-kernel formalization or human peer review. Arithmetic libraries, interpreter and host execution remain trusted.
- The graph corollary imports the pinned preprint's small-subgraph conditioning, moment asymptotics, lattice/Laplace analysis and Section 6 argument. These are listed in CLAIM-r2 §6a, not claimed independently re-proved.
- The lane exactly reproduced supporting paper anchors, including its constraint rank and restricted-Hessian data. Codex independently checked several anchors, but did not freshly recompute the full 301×301 determinant; the parent does not claim to have done so either. The Maximum Hypothesis certificate itself is independent of that determinant.
- No algorithm for finding a colouring of an individual graph is supplied. The result is asymptotic for the stated random model, not a statement that every 5-regular graph is 3-colourable.
- The published body and preprint were not compared; the source/version limit remains explicit.

## Priority and significance

A bounded audit ([report](colour-priority-audit.md)) found no earlier proof of the Maximum Hypothesis and no other unconditional proof of the random-5-regular 3-colourability assertion. The latest directly read status attestation is Ayre–Coja-Oghlan–Greenhill, [arXiv:1812.09691v4](https://arxiv.org/abs/1812.09691v4), p.2 (19 Oct 2021): Díaz et al. proved the result **if** an optimisation problem has its maximum at the specified point, supported by numerical evidence. Coja-Oghlan–Efthymiou–Hetterich (2013) explicitly called the case open. No later resolution was located in the checked 2022–2026 sources.

Priority limits matter: the ESA 2005 paper's abstract claims positive-probability 3-colourability, but its body was unread behind a paywall; Kemkes's thesis describes that result as conditional. Some later sources incorrectly described the 2009 result as already rigorous; ACG corrected its own wording in v3. A search miss is not proof of novelty.

**Significance:** potentially substantive specialist resolution, because it removes the numerical hypothesis from a 2009 conditional theorem on the low-degree random-regular colouring problem. The reduction and probabilistic theorem belong to Díaz et al.; convex-duality plus certified-global-optimisation architectures have precedents (Huang 2024; Shmalo 2026). No new general second-moment method is claimed.

**FRONTIER:** CORRECTNESS-ACCEPTED (computer-assisted), with the graph corollary explicitly scoped to the pinned preprint's analytic implication. NOVELTY-UNCLEAR after bounded audit. **The frozen phys-2 Maximum Hypothesis target gate is met** (2026-10-17 PT). Further expert scrutiny/publication would be separate actions and have not been authorised or performed.
