# The isolated two-copy d=4 obligation T2: proved subclasses, exact search, second-order rigidity

**PhysicsResearch96h-2 / physics-1. WRITTEN plus exact-arithmetic computations; UNREVIEWED.** This packet works on the obligation that Main isolated from the frozen v2 stratified packet, `frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md`, SHA256 `bf50bfbf3d0f4d24ec6a9e5fc55b19ced5cd2acdb223bbb1518fe6ebf4177329`. It contains:

- an exact counterexample search, which found no counterexample;
- an exact second-order rigidity test at a cross-sector equality point, which passed;
- written proofs of T2 on two structured subclasses.

It is **not** a proof of T2, of the original three-copy target, or of Z2/Z3. Nor is it a literature-status, novelty, parent/f62/f153/human/family/formal or operational claim. No held episode, consumer or guidance is used. Main authorized this counterexample search; it is the only place where explicit operators are evaluated.

## 1. The obligation

At d=4, with Theorem 1 and the ladder of the v2 packet, the following are equivalent:

- **(T2, primal)** `q2(C)=||C||²−½||Tr_1C||²−½||Tr_2C||²+¼|TrC|² >= 0` for every complex C on C⁴⊗C⁴ of rank≤2;
- **(T2, dual)** `σ1(X)²+σ2(X)² <= ||X||²/2 = 2(||A||²+||B||²)` for every `X=A⊗I+I⊗B` with A,B traceless.

The original target implies T2 (v2, Corollary 1), and the one-leg stratum of the original target is equivalent to T2 (v2, Corollary 2).

Under vectorization `vec Ψ=Σ Ψ_ab|a>|b>`, we have `X vecΨ=vec(AΨ+ΨB^T)`. Hence

`σ1(X)²+σ2(X)² = max over HS-orthonormal Ψ0,Ψ1 of Σ_r ||AΨ_r+Ψ_rB^T||²`.   (1)

**Tracelessness is essential.** The v2 packet gives an exact non-traceless counterexample to the dual inequality, so any proof must use tracelessness.

*[INFERENCE, unverified recollection, not a premise.]* The dual form appears to coincide with a matrix inequality discussed in the two-copy Werner-state distillability literature: the sum of the two largest squared singular values of `A⊗I+I⊗B` for traceless A,B. This owner does not know its current status at d=4. Checking it would require a separately gated literature source; none was consulted here.

## 2. Written proof for the subclass where A or B is normal

**Lemma 2.1 (supported-leg ranges are safe).** Let F⊂C⁴⊗C⁴ be two-dimensional with some ≤2-dimensional local leg, i.e. `F⊂C⁴⊗E` or `F⊂E⊗C⁴` with dim E≤2. Then `||XP_F||²<=||X||²/2` for every X∈W_odd.

*Proof.* Suppose instead that `||XP_F||²>||X||²/2` for some unit X. Then, as in the converse of v2 Theorem 2, the operator `C=XP_F` has rank≤2 and `q2(C)<0`. But `ran C†⊂F`, so C has a ≤2-dimensional input leg at that site. By the v2 ladder (Theorem 6, s=1 with T1), `q2(C)>=0`. This is a contradiction. The case of left (output) subspaces follows by applying the argument to X†∈W_odd. ∎

**Theorem 2.2.** If B is normal, or A is normal, then `σ1(X)²+σ2(X)²<=2(||A||²+||B||²)`.

*Proof.* Suppose B is normal and write `B=U diag(b)U†`. Conjugation by the local unitary `I⊗U` preserves W_odd, the norms and the singular values. So we may assume `B=diag(b)`. Then `X=⊕_j(A+b_jI)` is block diagonal over the site-2 basis. Its singular values are the union of the blocks' singular values, and its top two right singular vectors can be chosen as `ψ⊗e_j` and `φ⊗e_l` (j=l allowed). Their span F lies in `C⁴⊗span{e_j,e_l}`, which is ≤2-dimensional. Lemma 2.1 then gives `σ1²+σ2²=||XP_F||²<=||X||²/2`. If A is normal, the same argument applies with the sites exchanged. ∎

For example, when both are normal the eigenvalues are `a_i+b_j`, and the statement reduces to an elementary inequality for traceless 4-vectors. It is attained, for instance, by `a=(3,−1,−1,−1)`, `b=(1,1,−1,−1)`, where `16+16=2(12+4)`. This symbolic instance is shown only to illustrate sharpness.

## 3. Written proof for the commutator subclass, with a named import

Suppose `B=−A^T`. Then `X vecΨ=vec[A,Ψ]`. The **Böttcher–Wenzel inequality** `||[A,Ψ]||²<=2||A||²||Ψ||²` (imported classical theorem) gives every `σ_k(X)²<=2||A||²`. Hence `σ1²+σ2²<=4||A||²=2(||A||²+||B||²)`. This case is conditional only on that named imported theorem.

## 4. Exact counterexample search (authorized; integer arithmetic only)

The script `frontier-20261029-t2-exact-descent-search-v1.py`, SHA256 `485885e8017c751dd73cb3c39e368ef963c8d5526da2f47a8ae992ea384652d5`, uses the parametrization `C=UV†`, where U,V are 16×2 Gaussian-integer matrices. It minimizes `q2(C)/||C||²` by exact gradient steps rounded to the integer grid, with exact line search. Every comparison is an integer cross-multiplication; no floats are used. The evaluator was validated on:

- the equality operator `(|01>+|10>)<11|+|00>(<10|+<01|)`, where `4q2=0`;
- the nilpotent product `|02><13|`, where the ratio is exactly 1.

The result file `frontier-20261029-t2-exact-descent-search-results-v1.json` has SHA256 `4eda6670d3f05c47d6382e97428a958ba60b35cb7ff7c61fd94f7b4e9f904bda`. Over 24 random starts with 600 iterations each, **no negative value was found**. Every run ended with a strictly positive numerator and a ratio below `10^(−10)`.

A separate exact diagnostic was run on one limit point, computing the elementary symmetric functions of all four local reductions. It showed `e3/e1³` and `e4/e1⁴` below `10^(−10)`. The descent therefore converges to equality points in the **qubit corner**, where all four legs are effectively two-dimensional and positivity is already proved (v2 §6). This is heuristic evidence only. A nonnegative search outcome is not a proof.

## 5. Exact second-order rigidity at a cross-sector equality point

Let `X0=|0><1|⊗I+I⊗|0><1|`, a genuine two-sector point. The eigenvalues of `X0†X0` are:

- 2, twice, on `|11>` and `(|10>+|01>)/sqrt2`;
- 1, four times;
- 0, ten times.

So `σ1²+σ2²=4=||X0||²/2`, and X0 is an equality point of the dual. Because the top pair is isolated, `f=σ1²+σ2²−||X||²/2` is real-analytic near X0. Its first-order coefficient vanishes in every direction, by direct calculation. The second-order coefficient is

`c2(Y)=Tr(ΠY†Y)+Tr(ΠH1P1H1)+½Tr(ΠH1P0H1)−½||Y||²`, with `H1=X0†Y+Y†X0`.

The script `frontier-20261029-t2-cross-sector-hessian-exact-check-v1.py`, SHA256 `4ce2add20a4ba87b48bad53d597e408d972fc928c97a80aff15c5d51158a3e03`, builds c2 as an exact rational form on all 60 real directions in `sl4⊕sl4`. Its result `frontier-20261029-t2-cross-sector-hessian-exact-check-results-v1.json`, SHA256 `70b90bc41a34d96bb1806883986e00288216d57dfd8c465abbf82479eb1ea0ba`, is PASS:

- **The form has inertia (positive, negative, zero) = (0, 34, 26), i.e. it is negative semidefinite.** X0 is therefore a second-order local maximum of f, and no direction raises f to second order.
- The null checks give c2=0 along X0, along iX0, and along a local-unitary tangent.
- Overestimating the perturbative denominators makes the form indefinite: (16,34,10) and (24,34,2). This shows the test detects positivity when it is present.

The 26-dimensional null space suggests a large equality family through X0, and higher-order terms along it are not tested. This is a necessary-condition check at one point, not a local or global proof.

## 6. Status and exact remaining gap

**Proved (written):**

- T2 for A or B normal;
- T2 for `B=−A^T`, given the named import;
- T2 for every rank≤2 C with a supported leg or a spread range (v2);
- equivalently, the dual inequality whenever the top-2 singular space has a ≤2-dimensional leg.

**Evidence:** an exact search found no counterexample, and the exact Hessian at a cross-sector equality point is negative semidefinite.

**Open:** T2 for X whose top-2 right *and* left singular spaces both have all legs of dimension ≥3 and are not spread. Equivalently, Z2 is open, and so is the original target's one-leg stratum.

**Provenance and nonclaims.** The work uses the original functional, the v2 ladder and duals, local unitary invariance, the Böttcher–Wenzel import (in §3 only), and exact integer/Fraction arithmetic. No source premise, held material or held guidance is used. Historical process findings and the f153/f62 scopes are unchanged.
