# Werner d=4: exact duals, support ladder and a spread-covered region

**Disposition: same-harness written support with the five precision corrections below.** For `q_n(C)=Σ_{S⊆[n]}(−1/2)^|S| ‖Tr_S C‖²_HS` on complex operators, let T_n mean nonnegativity for every rank-≤2 C at fixed d, and Z_n the same assertion restricted to operators whose input/output legs at every site all have dimension at least three. The original problem is T_3 at d=4; it is **not proved here**.

At d=4, let W_odd be the Hilbert–Schmidt orthogonal sum of sectors `I_T⊗Y_T`, with |T| odd and Y_T traceless at every complementary site, and let P_odd be its orthogonal projection. The supported reformulations are:

- `q_n(C)=‖C‖²−2‖P_odd C‖²`, and `T_n` iff `σ₁(X)²+σ₂(X)²≤‖X‖²/2` for every X∈W_odd.
- For each two-plane F, `κ(F)=sup_{0≠X∈W_odd} ‖XP_F‖²/‖X‖²`; `T_n` iff `κ(F)≤1/2` for every F. For rank-≤2 C whose input or output range lies in F, `q_n(C)≥(1−2κ(F))‖C‖²`.
- `κ(F)≤s(F):=Σ_{|T| odd}4^(−|T|) ‖Tr_T P_F‖_∞`. In three copies this gives `q_3(C)≥[15/16−(λ₁+λ₂+λ₃)/2]‖C‖²`, where `λ_i=‖Tr_i P_F‖_∞`; hence the region `λ₁+λ₂+λ₃≤15/8` is covered. In two copies, `μ₁+μ₂≤2` suffices with the corresponding local reductions.

For every d, the exact one-leg Haar contraction identities imply the support ladder: positivity on all rank-≤2 operators with chosen 2-supported legs at s **distinct sites** is equivalent to T_(n−s). In particular T_3 implies T_2, the one-site supported stratum is equivalent to T_2, and `T_3⇔Z_2∧Z_3`. Rank-≤2 operators with 2-supported legs at two distinct sites are covered by T_1; all ranks are covered when every site has a chosen 2-supported leg. Same-site input/output supports do **not** constitute two distinct sites.

This is structural reduction and partial coverage, not an original q3 sign theorem, T_2 proof, full zero-leg exclusion, novelty or formal/kernel result. The earlier source/certificate dispositions, held episodes and product-equality result keep their exact separate scopes.

Native clock observed before composing: **2026-10-29T07:52:08-0700 PDT**; not a file-creation time.

## Parent reconstruction

With `Ω_i=vec I₄`, `P_i=|Ω_i⟩⟨Ω_i|/4` and `K_i=I−2P_i`, vectorization turns each partial trace into contraction against Ω_i. Expanding the tensor product of reflections gives `⊗K_i=I−2Π_odd`, proving the first identity. For fixed X, the maximal squared inner product with a unit rank-≤2 C is `σ₁(X)²+σ₂(X)²`, attained by its two-term singular truncation; exchanging the two suprema gives the Ky-Fan formulation. The same variational pairing restricted to `C=CP_F`, or its adjoint orientation, gives the range-wise formulation. Sectorwise partial-trace bounds, triangle inequality and weighted Cauchy–Schwarz give κ≤s, with orthogonality requiring traceless complementary factors.

For a 2-plane E at one site, the compressed local operator is `P_E⊗I−|Ω_E⟩⟨Ω_E|/2`. The two Haar moments on E decompose it as three times the integral of `|u⟩⟨u|⊗|ū⊥⟩⟨ū⊥|`, plus `P_E⊗(I−P̄_E)`. Tensoring the other local factors and vectorizing yields the exact output-leg contraction identity; the input case is its mirror. Contraction preserves rank and the other-site leg inclusions. Iterating gives the ladder; conversely tensoring with one-site pure projectors transfers lower-copy operators with the positive factor `q_1(|u⟩⟨u|)=1/2` per site.

## Corrections and assurance ceiling

The complete review found 0 FATAL / 0 MAJOR and five MINORs; this disposition adopts only the following corrected interpretation:

1. The two-leg coverage and remainder must refer to **two distinct sites**. Input and output support at the same site leave a stratum itself equivalent to T_2, not a proved case.
2. Rank-one positivity is supplied explicitly by the review's independent proof: `q_n(|a⟩⟨b|)=⟨a⊗b|⊗_i(I−F_i/2)|a⊗b⟩≥2^(−n)‖a‖²‖b‖²`, where F_i swaps the local copies. Thus W_odd contains no nonzero rank-one operator; no unsupported rank assertion is needed.
3. In the zero-integral characterization, Haar gives almost-everywhere vanishing first. The contraction integrand is continuous and phase-invariant and Haar has full support, so vanishing extends to every contraction.
4. Strictly positive open sets are relative to the rank-exactly-two operator manifold (and corresponding full-leg stratum). Positive weights alone do not make the spread bound strict. For maximally correlated range weights w, require `max w<1` for two copies and `<5/8` for three; uniform weights 1/2 give strict margins. Continuity of the range projection at fixed rank and of s, together with the open full-leg condition, gives nonempty relatively open covered sets.
5. Avoid the undefined phrase "concentrated range". The uncovered range test is explicitly `s(F)>1/2` with κ still unbounded by 1/2; equivalence of target statements is not an identification of a set of operators with an inequality.

The candidate's additional coverage bullet importing an earlier support-family packet is INCONCLUSIVE in f168 and is not adopted from that cross-reference. No claim about T_2 or T_3's literature status follows.

## Evidence

Parent read both complete frozen sources: the 153-LF [stratified v2 candidate](../../../../physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md), SHA-256 `bf50bfbf3d0f4d24ec6a9e5fc55b19ced5cd2acdb223bbb1518fe6ebf4177329`, and its 15-LF [author check addendum](../../../../physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261029-d4-stratified-v2-exact-check-addendum-1.json), read/hash only. Parent read the complete 428-LF [f168 review](../review-waves/f168-werner-stratified-source-independent-v2/review-v1.md), SHA-256 `75ba9dff87069c45765f523a06562ae0e50bbce4ac41172ed9a8efbb57c19ffe`. The [manifest](../review-waves/f168-werner-stratified-source-independent-v2/manifest-v1.json) is `9edf4483e76b21c59c24e796ffef67b4e43a629c733b4e3b11250dddb2a71e7b`.

The independent reviewer [results](../review-waves/f168-werner-stratified-source-independent-v2/f168rv-controls-v1-results.json), SHA-256 `5f66069652c34587b903acd0ad158967d2128122bcee4743e57ff98c27cbcd12`, and [receipt](../review-waves/f168-werner-stratified-source-independent-v2/f168rv-controls-v1-receipt.txt), SHA-256 `c4b043d424ac70564dc360cca4c18f0069b7fe7a82c8a9ea5eec13fd7ee69072`, record 23 positive and 22 intended-reason negative controls, including exact contraction identities at every site and both orientations for n=2,3. Numerical SVD/range checks are separately identified and are not proof of the open target.

Parent also executed a separate in-memory standard-library Fraction [spot check](../review-waves/f168-werner-stratified-source-independent-v2/parent-odd-sector-spotcheck-v1.json), SHA-256 `7b2098a218bacf22449dfd236ff5f2b5550d00adc863cd1d7b2a803f3e16ae82`: direct original-functional and odd-sector evaluations agree on actual rational rank-≤2 fixtures at n=1,2,3; two correlated-range spread examples pass; changing the coefficient from −1/2 to −1/3 is detected. These are finite examples, not a universal sign proof. All evidence is same-harness, not human, independent-model-family, formal/kernel or novelty acceptance.
