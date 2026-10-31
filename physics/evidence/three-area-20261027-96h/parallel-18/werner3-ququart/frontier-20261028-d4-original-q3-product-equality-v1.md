# Exact product-operator equality and the full-domain strict-gap obstruction

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 21:24:26 PDT 2026. This is a **WRITTEN universal theorem** for every product operator in the actual d4 rank<=2 domain, and it disproves a strictly positive lower bound on the entire original domain. It does **not** prove q3>=0 for arbitrary nonproduct operators, establish a global equality classification or claim novelty. The earlier public Tomar v4 source already states a sharpness/equality clause for dimensions at least2; the present derivation is an independent elementary check, not priority evidence.

## 1. Exact factorization for all product operators

For arbitrary complex 4×4 matrices X1,X2,X3, let `C=X1⊗X2⊗X3`. For any subset S of the three sites, the **unnormalized** partial trace is

`Tr_S C = [product_(i in S) Tr(X_i)] · tensor_(i notin S) X_i`.

Therefore the actual original q3 functional factors exactly:

`q3(C)=product_(i=1)^3 g(X_i)`,
`g(X)=||X||HS²−(1/2)|Tr X|²`.                                      (1)

This follows by distributing the eight terms; no real/Hermitian/normal or product-vector condition is assumed on the X_i.

## 2. Complete rank<=2 product equality characterization

Suppose C is nonzero with rank<=2. Each X_i is nonzero, and tensor-product rank multiplicativity leaves exactly two possibilities: all three X_i have rank1; or exactly one X_i has rank2 and the other two have rank1.

For any nonzero rank-r X, singular-value decomposition and Cauchy–Schwarz give

`|Tr X| <= ||X||_1 <= sqrt(r)||X||HS`.                                  (2)

If r=1, (2) gives `g(X)>=||X||HS²/2>0`. If r=2, it gives `g(X)>=0`. Hence (1) is nonnegative for **every** product C in the original rank<=2 domain, and it is strictly positive when all three factors have rank1.

For rank2, equality `g(X)=0` holds **if and only if** X is a nonzero complex scalar multiple of an orthogonal rank-two projection. Indeed, write `X=Σ_(j=1,2) s_j |u_j><v_j|` with positive singular values and orthonormal singular vectors. Equality in (2) forces `s1=s2` and equality in the triangle/inner-product inequalities for `Tr X=Σ s_j <v_j,u_j>`; thus `u_j=e^(i theta)v_j` for both j with the same phase. Conversely every such scalar projection has equality.

Combining with the rank classification:

**For every nonzero product C with rank<=2, `q3(C)=0` iff exactly one local factor is a scalar rank-two orthogonal projection and the other two factors have rank1.** All other such product operators have q3(C)>0.

## 3. Consequence on the entire original domain, and precise limits

Rank-two orthogonal projections and nonzero rank-one matrices exist on C⁴, so the equality class above is nonempty. The q3 functional is homogeneous of degree2, and its members can be normalized to `||C||HS=1`. Consequently **there is no universal constant delta>0 for which `q3(C)>=delta||C||HS²` holds for every original rank<=2 C**. This is an original-domain falsification of a strict-gap premise, not a proof that q3 is nonnegative on all nonproduct inputs.

The separate public-source certificate asserts/supports the whole arbitrary-complex rank<=2 inequality at d4 under the explicit code/runtime/review gates in `frontier-20261028-d4-consolidated-proof-dossier-v3.md`, SHA256 `5fd7eae54aecf154113461982fb429704dfe0cf53bbc786281c54356e280b223`. **Only if** that full nonnegativity is accepted does the present equality class additionally imply that the normalized global infimum equals0. No general equality classification, nonproduct conclusion, all-d/operational result, source novelty, human/family, formal/Lean or parent/f62 adoption is asserted.

## 4. Provenance boundary

Main actually read `frontier-20261028-2121-selected-operator-probe-self-stop-v1.json`, SHA256 `d523c4596b86b409a19dae5f62fb764aa5d431eed4cb606895530c4bfbe9f822`, and explicitly released prospective original research under contract-addendum-2, while directing that the earlier elected quarantine not be reconstructed or salvaged. This theorem uses only the original q3 definition, elementary tensor identities and singular-value decomposition; no content, conclusion or route-selection guidance from that quarantined episode is used. The earlier process disclosure remains immutable, previous held outcomes remain nonpremises, and no retroactive clean-provenance or prior-acceptance inference is made.
