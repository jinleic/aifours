# P44 prerequisite addendum1 — all input transposes and local-unitary rotations do not remove the fixed positive-reconstruction obstruction

Owner **PhysicsPPT44-2**, physics-3. Actual `/bin/date` immediately BEFORE this NEW immutable write: **Tue Oct 27 15:02:38 PDT 2026**. **WRITTEN, UNREVIEWED**, no identity machine-checked. This is a substantive continuation of the SAME S1 definition-first duty, not new source/proof permission or an edit to v1.

## 1. Exact dependency and question

Operative new-round author input: `prerequisite-derivation-v1.md`, SHA `7d00196376108da34c416b8e80f815adfc337d01cb24191f8ad40f6a47d8cdc4`, ENTIRE208LF. Its proof is AUTHOR-WRITTEN UNREVIEWED, not a parent-adopted import. Its original premises were the supplied S2 definitions and the explicitly reconstructed elementary matrix/spectral/trace facts. No old primary/review/held guide is added here.

V1 proves that nonempty trace-complement iterations map actual PPT inputs into the unnormalized SN<=2 cone, but their fixed positive linear-map cone cannot recover a nonzero multiple of the identity. The question here is genuinely broader: does allowing ALL FOUR input transposes and arbitrary local-unitary coordinate changes remove that obstruction?

**Answer at the exact family below: NO.** The proof uses the WHOLE doubly-traceless operator sector and a uniform linear-map inequality, not a selected state, real-only rank test, special basis, sample dimension or numerical norm computation. It says nothing about the original unrestricted P44 outcome.

## 2. Admissible map family and the important output-transpose limit

Let local dimensions a,b>=3; the original space has a=b=4. Work on the real space of bipartite Hermitian operators. Use the actual R_A,R_B,D_A,D_B,D_0 of v1.

Let T be ANY finite word made of

- arbitrary local-unitary conjugations `X -> (U tensor V)X(U tensor V)^*`, and
- Gamma_A and Gamma_B.

Thus the four basic input transposes id,Gamma_A,Gamma_B,FULL transpose are included, as are arbitrarily rotated transpose conventions. Let L be any local-unitary conjugation at the output. For p,q>=0 with p+q>=1, define

    F = L composed with R_A^p R_B^q composed with T.        (2.1)

One may also use noise maps

    N = L composed with D composed with T,
    D in {D_A,D_B,D_0}.                                   (2.2)

The positive-reconstruction cone consists of finite NONNEGATIVE sums of these actual linear maps, and their limits.

**Every F and N maps the PPT cone into C2.** To verify all steps: local-unitary conjugation preserves positivity and PPT because the partial transpose is the corresponding conjugation by `U tensor bar(V)`. It preserves C2 by the original tensor-rank definition. Gamma_B maps PPT onto PPT because both X and Gamma_B(X) are positive; Gamma_A follows by full transpose. Therefore T maps PPT to PPT without any assertion that it preserves C2. V1's nonempty complement block then produces C2 and preserves PPT at every iteration. L preserves the resulting C2 membership. For N, the actual marginals of a positive PPT input are positive, so D_A,D_B,D_0 produce separable positive operators, and L preserves that property.

**No arbitrary output partial transpose is admitted after the final complement block.** PPT positivity alone is not a proof that partial transpose preserves SN<=2. The order in(2.1) is a real hypothesis, not notation hiding that gap. Full transpose alone would preserve Schmidt rank, but the larger unsupported assertion for either partial transpose is not used.

No inverse filters, marginal normalization, matching-marginal scaling or selected physical state is introduced.

## 3. FULL invariant operator sectors

Let

    E00 = R(I_A tensor I_B),
    E10 = Herm_0(A) tensor R I_B,
    E01 = R I_A tensor Herm_0(B),
    E11 = Herm_0(A) tensor Herm_0(B).

This is the ENTIRE real Hermitian operator space as a direct sum. Here Herm_0 denotes all traceless Hermitian operators, not a chosen matrix. Equivalently E11 is the simultaneous kernel of BOTH partial traces.

For clarity, the four basic transposes act on the COMPLETE finer local decomposition

    Herm(C^d) = R I direct-sum Sym_0(R^d)
                           direct-sum i Skew(R^d).

Local transpose has eigenvalue +1 on the first TWO summands and -1 on the last; R_d has eigenvalue d-1 on the first and -1 on BOTH traceless summands. Their tensor products describe all nine joint summands. Hence every basic input transpose preserves E00 and E11, acts as the identity on E00, and is orthogonal on E11 for the Hilbert–Schmidt inner product. This is a whole-space identity, not a probe on one transpose-even tensor.

The same facts hold for ANY local-unitary conjugation. Partial traces transform by local conjugation, so their zero conditions are preserved; unitary conjugation fixes I. It preserves the Hilbert–Schmidt norm by trace cyclicity. Partial transpose also preserves that norm because it permutes the matrix entries in the Hilbert–Schmidt sum. Thus EVERY allowed word T restricts to an orthogonal operator on E11 and fixes E00. No Haar average, finite design, numerical matrix or norm estimate from an old source is required.

By definition, both R_A and R_B restrict to -id on E11. On E00 they act as multiplication by a-1 and b-1 respectively. Every noise map D_A,D_B,D_0 kills E11; on E00 its multiplier is positive.

## 4. Uniform inequality for the enlarged positive cone

For a generator F in(2.1), write lambda_0(F) for its scalar on E00. Then

    lambda_0(F)=(a-1)^p(b-1)^q,
    F restricted to E11 = (-1)^(p+q) times an orthogonal map.

In particular, for `mu=min(a-1,b-1)>1`,

    lambda_0(F)>=mu,       ||F restricted to E11||_(HS->HS)=1.

For a noise generator N, lambda_0(N)>=0 and its E11 restriction is zero. Both inequalities are exact symbolic statements for ALL allowed words and dimensions.

For any finite nonnegative combination Phi of generators, triangle inequality on the entire E11 space gives

    ||Phi restricted to E11|| <= sum_(F generators) c_F,
    lambda_0(Phi) >= mu * sum_(F generators) c_F.

Consequently the enlarged cone satisfies the universal necessary inequality

    lambda_0(Phi) >= mu * ||Phi restricted to E11||.         (4.1)

If Phi=c*id with c>0, its two sides would require c>=mu*c, impossible since mu>1. The same inequality survives every finite-dimensional superoperator-norm limit: the common invariant-subspace property, the identity-sector scalar and the restricted operator norm are continuous. Thus no limit of the enlarged positive cone equals a nonzero positive multiple of the identity either.

This is stronger than the four-basic-transpose statement, because it covers arbitrary local-unitary words before them, between them, and at the output, within the exact order that preserves the C2-output proof. It does not rely on those operations commuting with one another.

All degeneracies are explicit. Zero coefficients/noise-only maps have zero E11 restriction and still satisfy(4.1). The zero map is allowed. A local dimension two would give mu=1 in the relevant bound, so this argument does NOT assert a strict exclusion there. The original4x4 dimensions satisfy the stated strict dimension hypothesis; no new parameter case was selected for viability testing.

## 5. The actual-original-input caller, and non-converses

The exclusion is not evaded by asking equality only on EVERY original PPT state instead of on every Hermitian operator. The PPT cone spans the real Hermitian operator space: local positive operators span each local Hermitian space by their positive/negative spectral parts, and their tensor products span the bipartite Hermitian space. Positive product operators are separable and PPT. Hence equality of two fixed linear maps on ALL PPT states extends by scaling and linearity to the whole operator space. This argument quantifies over every product input and both full local spaces; it is not a selected-state check.

Therefore a fixed positive map decomposition from this enlarged family cannot supply an identity-resolution proof of SN<=2 for ALL original PPT inputs. Although each generator's actual output is C2, positivity of those outputs does not furnish a valid positive linear reconstruction of rho from them.

**Exact non-converses:** this is NOT an original-state counterexample, NOT a universal no-go for PPT SN>=3, NOT a theorem that no other SN2-producing maps exist, and NOT an exclusion of coefficients chosen nonlinearly from the particular rho. It does not license output partial transpose of arbitrary C2 states. No criterion for actual global two-block-positivity or a negative rho,W pair is supplied by(4.1).

The original joint-certificate/no-go target remains open. The bound identifies a strictly limited reconstruction step that fails, even after the full admitted coordinate/transposition enlargement; it must not be promoted beyond that scope.

## 6. Exact next prerequisite and source/method boundary

A genuine further original conclusion now needs a coupling outside THIS fixed positive-reconstruction cone, or an independently certified actual eligible negative pair. More repetitions or local-unitary rotations of these same identities cannot pay that premise. In particular the derivation does not silently replace a positive sum by subtraction.

The next tempting enlargement to nonunitary local congruences/marginal normalization is NOT pursued here: the inherited record includes held matching-marginal/scaling/normal-form guidance, and this packet supplies no independently admitted source/method separation for such a continuation. That branch is STOPPED before its source/proof/method expansion; no protected formula, instance or private guide is reconstructed. This is a specific missing-separation boundary, not an all-route exhaustion statement or a claim that every possible new method is unavailable.

Main can bind a genuinely independent narrow input or a full review duty while the current exact original premise remains unpaid. This addendum supplies a genuine continuation and refined limitation; it is not an instruction to idle for the96-hour window or a generic ACK loop.

## 7. Assurance

The ONLY new elementary facts used beyond v1 are finite-dimensional Hilbert–Schmidt invariance/triangle inequality, the full identity/traceless and transpose-eigenspace direct sums, and spectral spanning. Their actual uses are written above. No additional source, proof/review body, scientific computation, selected state/control/decimal/limit/boundary probe, program/enumeration/solver/replay/build/test/typechecker, nested agent/modelCLI/paidAPI, Git/delete/contact/publication/infrastructure action occurred.

Old STOP/HOLD/ZERO and every finding, N4 UNKNOWN/historical exit unestablished, old21 NR and auxiliary214 STOP remain. No independent-cognition, novelty, formal/kernel/executable/human/configured-family or original-outcome claim. This is **WRITTEN UNREVIEWED**, at the SAME S1 narrow release; Main must read the complete union and full-scope returns before adoption. Successor research deadline2026-10-31T21:23:27.000Z unchanged.
