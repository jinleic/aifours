# The isolated two-copy d=4 obligation T2: proved subclasses, exact search, second-order tests (v2)

**PhysicsResearch96h-2 / physics-1. WRITTEN plus exact-arithmetic computations; UNREVIEWED.** This self-contained successor replaces `frontier-20261029-d4-t2-two-copy-obligation-packet-v1.md` (SHA256 `de506bddeb9bfb8d5ab286eacc50bd9535997e3000057e64267b3982892bd998`), which is kept unchanged. It differs from v1 in three ways:

- it adds a second exact second-order test, at a normal equality point (§5.2);
- the status section uses precise class statements (§6): legs are attached to **sites**, and no undefined "concentrated" class is used;
- the Böttcher–Wenzel premise is stated as an explicit hypothesis (§3).

It relies on the v2 stratified packet `frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md` (SHA256 `bf50bfbf3d0f4d24ec6a9e5fc55b19ced5cd2acdb223bbb1518fe6ebf4177329`), which is under separate review. Nothing here alters that review's scope.

**Nonclaims.** The finite search and the second-order tests are evidence and local behaviour only. They are not a proof of T2, of q3 positivity, or of Z2/Z3. No literature-status, novelty, parent/f62/f153/f168, human/family/formal or operational claim is made. No held episode, consumer or guidance is used. Explicit operators are evaluated only in §§4–5, under Main's authorization of an exact counterexample search.

## 1. The obligation

At d=4, by v2 Theorem 1, the following are equivalent:

- **(T2, primal)** `q2(C)=||C||²−½||Tr_1C||²−½||Tr_2C||²+¼|TrC|²>=0` for every complex C on C⁴⊗C⁴ of rank≤2.
- **(T2, dual)** `σ1(X)²+σ2(X)²<=||X||²/2=2(||A||²+||B||²)` for every `X=A⊗I+I⊗B` with A,B traceless 4×4.

By v2 Corollary 1, the original three-copy target implies T2. With `X vecΨ=vec(AΨ+ΨB^T)`,

`σ1(X)²+σ2(X)² = max over Hilbert–Schmidt-orthonormal Ψ0,Ψ1 of Σ_r ||AΨ_r+Ψ_rB^T||²`.

Tracelessness is essential: the v2 packet records an exact non-traceless counterexample to the dual inequality.

*[Unverified recollection; not a premise and not a source result.]* The dual form resembles a matrix inequality discussed in the two-copy Werner-state distillability literature. Its status at d=4 was not checked; checking it would need a separately gated source.

## 2. Written proof when A or B is normal

Throughout, a **leg** of a subspace F⊂C⁴⊗C⁴ *at site i* is the smallest subspace E⊂C⁴ such that F lies in `E⊗C⁴` (i=1) or `C⁴⊗E` (i=2).

**Lemma 2.1.** Let F be a two-dimensional subspace of C⁴⊗C⁴ whose leg at **some site** has dimension ≤2. Then `||XP_F||²<=||X||²/2` for every X∈W_odd.

*Proof.* Suppose `||XP_F||²>||X||²/2` for some nonzero X, and put `C=XP_F`. Then C has rank≤2, `||C||²=||XP_F||²`, and `<X,C>=||XP_F||²`. Hence `||P_odd C||²>=|<X,C>|²/||X||²>||C||²/2`, so `q2(C)=||C||²−2||P_odd C||²<0` by v2 (1). But `ran C†⊂F`, so the input leg of C at that site has dimension ≤2. By v2 Theorem 6 with s=1, together with T1, `q2(C)>=0`. This is a contradiction. ∎

The same holds for left subspaces, by applying the lemma to X†∈W_odd.

**Theorem 2.2.** If A or B is normal, then the T2 dual inequality holds.

*Proof.* Suppose B is normal. Conjugation by `I⊗U` preserves W_odd, all norms and all singular values, so we may take `B=diag(b)`. Then `X=⊕_j(A+b_jI)` is block diagonal over the site-2 basis. Its top two right singular vectors may be chosen as `ψ⊗e_j` and `φ⊗e_l` (j=l allowed). Their span therefore has leg at site 2 inside `span{e_j,e_l}`. Lemma 2.1 gives `σ1²+σ2²<=||X||²/2`. The case of normal A follows by exchanging the sites. ∎

## 3. The commutator subclass, under an explicit imported premise

**Premise (Böttcher–Wenzel inequality, imported, not proved here):** `||[A,Ψ]||_F²<=2||A||_F²||Ψ||_F²` for all complex matrices A, Ψ.

**Under this premise**, if `B=−A^T` then `X vecΨ=vec[A,Ψ]`. So every `σ_k(X)²<=2||A||²`, and hence `σ1²+σ2²<=4||A||²=2(||A||²+||B||²)`. Without the premise, this subclass is not claimed.

## 4. Exact counterexample search (integer arithmetic only)

**Search.** `frontier-20261029-t2-exact-descent-search-v1.py`, SHA256 `485885e8017c751dd73cb3c39e368ef963c8d5526da2f47a8ae992ea384652d5`, minimizes `q2(UV†)/||UV†||²` over 16×2 Gaussian-integer matrices U,V. It uses exact gradients rounded to the integer grid and exact line search, with no floats.

**Result.** `frontier-20261029-t2-exact-descent-search-results-v1.json`, SHA256 `4eda6670d3f05c47d6382e97428a958ba60b35cb7ff7c61fd94f7b4e9f904bda`. Over 24 starts with 600 iterations each, **no negative value occurred**. Every run ended with a positive numerator and ratio below `10^(−10)`.

**Limit point.** An exact diagnostic on one limit point found that every local reduction has `e3/e1³` and `e4/e1⁴` below `10^(−10)`. So every leg is numerically within about 10^(−10) of being two-dimensional; strict two-dimensionality was not established. This is consistent with convergence toward the class where a leg at some site has dimension ≤2, where positivity is proved (v2 Theorem 6, s=1).

**Interpretation.** These are heuristic finite observations. They do not cover the space of rank-2 operators and prove nothing about T2.

## 5. Exact second-order tests at two equality points of the dual

Let `f(X)=σ1²+σ2²−||X||²/2` on W_odd. At each point below, the top eigenvalue of `X†X` is double and isolated, so f is real-analytic nearby. The second-order coefficient is

`c2(Y)=Tr(ΠY†Y)+Σ_(μ<λ) Tr(ΠH1P_μH1)/(λ−μ)−||Y||²/2`, with `H1=X†Y+Y†X`.

Each test computes c2 as an exact rational form on all 60 real directions of `sl4⊕sl4`, including non-normal ones, and finds its exact inertia. Fault controls that overestimate the perturbative term must produce positive inertia.

### 5.1 Cross-sector point

`X0=|0><1|⊗I+I⊗|0><1|`, with `σ1²+σ2²=4=||X0||²/2`.

- Script SHA256 `4ce2add20a4ba87b48bad53d597e408d972fc928c97a80aff15c5d51158a3e03`; result SHA256 `70b90bc41a34d96bb1806883986e00288216d57dfd8c465abbf82479eb1ea0ba`, PASS.
- **Inertia (0,34,26).**
- c2 vanishes along X0, along iX0 and along a local-unitary tangent.
- The faults give inertia (16,34,10) and (24,34,2).

### 5.2 Normal point

`X1=diag(3,−1,−1,−1)⊗I+I⊗diag(1,1,−1,−1)`, with `σ1²+σ2²=16+16=32=||X1||²/2`. The eigenvalues of `X1†X1` are 16 (×2), 4 (×8) and 0 (×6).

- Script `frontier-20261029-t2-normal-point-hessian-exact-check-v1.py`, SHA256 `dc572db4ba0e953a5219120df30606511ad6db63f2b6570276654fff41b51a44`; result `frontier-20261029-t2-normal-point-hessian-exact-check-results-v1.json`, PASS.
- **Inertia (0,38,22).**
- c2 vanishes along X1.
- The faults give inertia (8,38,14) and (6,38,16).

Both forms are negative semidefinite, so both points are second-order local maxima of f. The large null spaces are not explored to higher order. These are necessary-condition checks at two points only.

## 6. Status, stated by class

**Primal classes proved in WRITTEN form (v2 packet, source-independent):**

- rank≤1 C;
- rank≤2 C whose input or output leg at **some site** has dimension ≤2 (v2 Theorem 6, s=1, with T1);
- rank≤2 C whose input range or output range F has `μ1+μ2<=2`, where μ_j is the operator norm of the site-j reduction of P_F (v2 Theorem 3, n=2).

**Dual classes proved here:**

- every X with a top-2 right or left singular subspace whose leg at some site has dimension ≤2 (Lemma 2.1);
- in particular, A or B normal (Theorem 2.2);
- `B=−A^T`, only under the explicit Böttcher–Wenzel premise (§3).

**Open:** X ∈ W_odd for which neither Lemma 2.1 nor the spread criterion applies, i.e. both of the following hold:

- every top-2 right and every top-2 left singular subspace has legs of dimension ≥3 at **both** sites;
- each of these subspaces has `μ1+μ2>2`.

Separately, Z2 (rank≤2 C with all four legs of dimension ≥3) remains open. Through v2 Corollary 2, so does the original target's stratum with a ≤2-dimensional leg at some site.

**Provenance.** The work uses the original functional, the v2 ladder and duals, local unitary invariance, exact integer/Fraction arithmetic, and, in §3 only, the explicit Böttcher–Wenzel premise. No source premise, held material or guidance is used. Historical process findings and the f153/f62/f168 boundaries are unchanged.
