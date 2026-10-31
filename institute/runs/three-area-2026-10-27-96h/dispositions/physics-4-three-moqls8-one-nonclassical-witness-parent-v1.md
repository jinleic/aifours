# An explicit nonclassical set of three MOQLS(8)

**Disposition: ACCEPT the finite physical witness; the numerical consequence is conditional on source priority.** Native clock observed before composing: **2026-10-28T20:17:05-0700 PDT**. Three same-harness exact verifiers agree; no human, independent-model-family, formal/kernel or novelty certification. The registered four-family target is not closed.

## Adopted statement

The pinned witness `frontier-20261028-three-family-mixed8-witness-v1.json` (SHA-256 `a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413`) is an actual set of three mutually orthogonal quantum Latin squares of order 8 in the same cell coordinates: each member's rows and columns are orthonormal bases of C⁸, and for each of the three pairs the 64 same-cell tensor products form an orthonormal basis of C⁸⊗C⁸. Two members are classical Latin squares in the supplied standard basis; the third has eight cells supported on `{e₀,e₁}` with entries `(e₀±e₁)/√2`, and its cells (0,0) and (2,2) have exact squared overlap 1/2, so it is genuinely nonclassical under the source's isotopy (per-cell phases, row/column permutations, one unitary per member).

Under the pinned primary source's definitions (Ball–Simoens, arXiv:2607.12933v2), a set is nonclassical when it is not classical up to isotopy, so one nonclassical member suffices and `M(n)` counts the size of such a set. Hence, **if** that paper's Table 2 entry `2≤M(8)≤5` is the current public lower bound, this witness gives `3≤M(8)≤5`. The source audit found no listed theorem producing a nonclassical triple at order 8 (Corollary 7 is inapplicable since 7 is prime; Theorem 4's triple clause needs n≥16; the checked references [2],[5],[7],[14] exclude or omit order 8), but **current literature-wide status is UNKNOWN** and no novelty or priority is certified.

## Verification evidence

- [Frozen manifest](../review-waves/f125-moqls8-actual-three-family-witness/manifest-v1.json): `bc1753bab7dc9efa691a13ab8fa03be2b403172c00b837d503d04a745f74f9f0`; [pinned witness copy](../review-waves/f125-moqls8-actual-three-family-witness/parent-inputs-v1/witness.json) and [physical definition](../review-waves/f125-moqls8-actual-three-family-witness/parent-inputs-v1/physical-definition-v1.md) `3df4d2bec7f566a66508110176e8217c15e38025323b6f19444e70e435c01fff`.
- [Verifier 1](../review-waves/f125-moqls8-actual-three-family-witness/verifier-review-v1.md) `0ac12db561ecdea3c0a131976275a5fa9775c3ac1894924ec41e57e513afdfb7`: exact Q(√2) arithmetic, 384 norms, 1,344 line overlaps, 3×4,096 product Gram entries, seven intended-reason mutation fixtures rejected.
- [Verifier 2, independently structured](../review-waves/f125-moqls8-actual-three-family-witness/replay-review-v1.md) `873c2f356dc3be88732b9e33a3c5d46eb008980e1ce903adaf3e2b8988dc05ec`: explicit 64-dimensional Kronecker vectors and full integer 64×64 Grams, overlap histograms, classical positive control, ten intended-reason negatives including one-member row/column permutation and transposition.
- [Parent verifier 3](../review-waves/f125-moqls8-actual-three-family-witness/parent-witness-exact-v1.py) and [actual result](../review-waves/f125-moqls8-actual-three-family-witness/parent-witness-exact-result-v1.json): integer-only strict parser, row/column/pair checks, seven mutation controls, run 2026-10-28 20:13:31 PDT, `VALID_THREE_MEMBER_FAMILY`, mixed cells `18,19,26,27,36,37,44,45`.
- [Source-definition audit](../review-waves/f125-moqls8-actual-three-family-witness/source-audit-v1.md) `21597f6603892084932d2bdd459431b2197e939a0be663fc297e739769dc048c`: verbatim scout report persisted by the parent; parent independently read the source's §§1–2.3, Theorem 5/6, Corollary 7 and §4.1 and agrees with the definition correspondence.

All three verifiers share the harness and Python runtime; none imports author or sibling code. The triple-verification standard for a finite witness is met at the same-vendor level only; no cross-vendor or human verification was performed.

## Boundaries

Not established: the registered four-family alternative (a fourth mate or a universal classicality proof), exact `M(8)`, current public status, novelty, or whether the construction (rotating an 8-cell two-symbol trade of a classical triple) is a routine instance of known methods. The author's related written bounds on mixed cells for two-classical-mate families are separate unreviewed candidates.
