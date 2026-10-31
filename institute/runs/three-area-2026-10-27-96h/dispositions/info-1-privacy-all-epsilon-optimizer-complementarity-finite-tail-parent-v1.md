# Full-law privacy optimization: attained value, optimizer complementarity and a finite-profile tail reduction

**Disposition: same-harness written support for Theorems A–B of the twice-corrected f261 composite, for every finite epsilon>0.** This is an optimizer-structure and variational reduction, **not a closed-form solution**, uniqueness theorem, book-equivalence claim or novelty determination.

Let b=exp(-epsilon), D be the FULL CLOSED l1 unit ball in R², and F_b all Borel probability laws satisfying mu(A)≤b⁻¹mu(A+h) for every Borel event A and every h∈D. Put V=inf_{mu∈F_b} E_mu||X||₂². No radiality, independence, lattice, convex-level or restricted-shift premise is imposed on the original law.

Native clock before composing: **2026-10-29T15:57:06-0700 PDT**.

## Supported statements and exact representatives

1. **Attainment and phases.** 0<V≤4/epsilon² and V is attained. Every optimal law admits an exact measurable mixture of optimal geometric-phase laws. For almost every phase, its levels have compact canonical essential-support representatives K_i with positive initial area, 0∈int(K_0), D4 symmetry, centered axis/diagonal sections, finite weighted mass/moment, and literal K_i+D⊆K_{i+1}. These conclusions are derived from all-shift weak closure, a bounded everywhere-private ball-average density representative, the exact phase integral, four separate Steiner optimality comparisons and essential-support regularization; they are not imported from the unadopted f238 aside.
2. **Necessary complementarity.** With B̄ the closed Euclidean ball of radius sqrt(V), K_0⊆B̄ and, for i≥1,

   K_{i-1}+D ⊆ K_i ⊆ (K_{i-1}+D)∪B̄.

   For every i≥0, the set ((K_{i+1}⊖D)∩B(0,sqrt(V))) minus K_i has area zero, where E⊖D={x:x+D⊆E}. The essential-support recurrences of candidate (8) hold literally for these representatives. Raw zero-area erosion exceptions and arbitrary Borel versions are not asserted to coincide as sets.
3. **Exact eventual coherence.** For every i≥ceil(sqrt(2V)), K_i=K_{i-1}+D exactly. The uniform cutoff **N=ceil(2sqrt(2)/epsilon)** therefore works for every optimal phase. Its tail is K_{N-1}+jD, j≥1. Different phases may have different tail cores; the finite earlier transitions are not asserted parallel.
4. **Attained finite-profile reformulation.** V equals the attained minimum of the exact ratio R_N=N_N/Z_N in candidate (B1)–(B5), over N compact canonical profiles F_i with t_i≥0, F_i(t_i)=t_i, F_i nonincreasing, F_i(y)+y nondecreasing, and the exact profile inequalities expressing C_i+D⊆C_{i+1}. There are finitely many **profile functions**, not finitely many scalar variables. Singleton t=0 profiles are permitted feasible competitors, not actual positive-area optimizer levels. N=1 and positivity of the denominator are included.
5. **Necessary restrictions are not a solver.** The same attained minimum persists when the feasible tuples are restricted by candidate (B6) and R_N≤U=4/epsilon², because an actual optimizer tuple remains and every tuple still yields a full-class feasible law. Neither condition is asserted sufficient for optimality. The optional f245 square establishes B6/local-condition insufficiency only, not membership in the U-capped class.

## Parent reconstruction of decisive steps

- For a fixed full closed-D shift, weak convergence preserves the inequality against bounded continuous test functions, hence as finite Borel measures. The same weak subsequence works for each arbitrarily chosen shift, without an uncountable exceptional-set argument. The product-Laplace witness gives tightness and the stated upper bound; lower semicontinuity gives attainment.
- A one-level feasible replacement changes N−VZ by (1−b)b^i times the integral of its signed indicator against ||x||²−V. Deleting positive-area unforced material outside the cost ball, or adding positive-area available erosion inside it, would contradict V. Closed retained sets and essential support upgrade the pruning inclusion; the circle contributes zero area.
- K_{i-1}+D contains iD. By ||x||₁≤sqrt(2)||x||₂, iD contains B̄ once i≥sqrt(2V), including the boundary equality. The complementarity sandwich then forces the exact tail. V≤4/epsilon² gives the explicit N.
- Reindexing the infinite tail gives **b^{N−1} E[A(C_{N−1}+GD)]** and the analogous moment, where P(G=j)=(1−b)b^j. There is no extra (1−b) factor on that tail. Every admissible profile tuple produces a feasible phase, while an extracted optimal phase supplies a tuple attaining V; compactness of the whole profile search space is not assumed.

## Mandatory corrections and read chronology

Use the source only with both author corrections, in order:

1. First fiber convention: /Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-1-f250-steiner-fibers.md, SHA-256 **6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27**, 48 LF. Zero-length fibers are empty, positive finite fibers are closed centered intervals, infinite fibers are the line.
2. Geometry/cap correction: same directory/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-2-f256-geometry-and-cap-scope.md, SHA-256 **89f91e9004c9563caf3d4cc831b1101c4e4ade8a138b006b5af7f00c1fddbb14**, 77 LF. The boundary count is at most one per open half-plane (two on a full vertical fiber) away from countably many jumps; centered-section uniqueness is finite-length/a.e., not infinite-length; the optional square does not establish the extra U-cap condition.
3. Unchanged base: same directory/frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1.md, SHA-256 **4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43**, 274 LF.

The parent fully read both corrections and then completed a fresh full read of the unchanged candidate after them. Earlier candidate reads predated these corrections and are not backdated. The first f250 and later f256 findings remain their actual frozen verdicts, not retrospectively cleared by newly created files.

## Reviewed evidence and residual

- Frozen manifest: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f261-privacy-optimizer-twice-corrected-composite/manifest-v1.json, SHA-256 **66b77dd60b4a5ca5e69004806b1bcda5731f62f26a53a79bdd23271c49f6ce5d**. All five declared input SHA/byte/LF bindings matched at 15:54:53 PDT.
- Slice A: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f261-privacy-optimizer-twice-corrected-composite/review-A-v1.md, SHA-256 **57242551c9b288192c62921c2790dcc9b4aaf8976a62459a2dfc7b1712a173ed**, 107 LF, 0F/0M/0m on existence/phase/geometry. Slice B: /Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f261-privacy-optimizer-twice-corrected-composite/review-B-v1.md, SHA-256 **2e073535188901bea86dcd72599a0d9ec24679d9df3a3a3d1d4670d8b522dc63**, 135 LF, 0F/0M/0m on perturbation/tail/minimum **conditional on its listed geometry imports**, which A reconstructs. Parent displayed both complete reviews and did not substitute one slice for the other.
- A uses written proofs and counterexamples only. B records two reviewer-owned exact controls with actual exit 0, input/code hashes and intended-reason negatives; they check finite geometry/arithmetic, not the infinite-dimensional theorem. This disposition does not newly replay those controls or execute author code.
- The B-review's additional erosion lemma, stronger whole-range square-cap comparison and separate reviewer-derived capped-counterexample instance are **not automatically adopted here**; the main theorems do not need them. The exact **global optimization over the finite nonparallel prefix**, value formula, early-shell coherence and uniqueness remain open at this boundary.
- Standard named mathematical imports include Prokhorov/tightness, Radon–Nikodym and Lebesgue differentiation, Borel-measure regularity, Tonelli/Fubini/monotone convergence and elementary one-dimensional rearrangement/inner regularity. No LAW642, matching-norm theorem, f238 optimizer aside or held/f161/f162 result is a premise of A–B. Assurance is **same-harness written review and parent reconstruction**, not human, independent-model-family, formal/kernel, source-equivalence or novelty verification.
