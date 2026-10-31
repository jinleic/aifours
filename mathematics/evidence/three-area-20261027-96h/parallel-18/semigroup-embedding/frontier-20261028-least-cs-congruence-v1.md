# Least completely simple congruence of an arbitrary regular semigroup

**Status: NEW AUTHOR WRITTEN GENERAL OBSERVATION; UNREVIEWED / UNADOPTED.** This identifies the finest pure actor as a special case of the least CS quotient. It is not a claim of novelty, an embedding theorem, or a proof of original SEP/R/L.

## 1. General existence without a purity hypothesis

Let S be any nonempty regular semigroup. Let `ν` be the intersection of the kernels of ALL onto homomorphisms from S to completely simple semigroups. This is an intersection over a set: one may index by the congruences on the underlying set S whose quotient is CS. The family is nonempty, since the one-element quotient is CS. Then **S/ν is itself completely simple**; hence ν is the least CS congruence on S.

Proof. For every indexed congruence θ choose a Rees representation of S/θ. Their direct product is completely simple: its Rees group, row set, column set and sandwich matrix are coordinatewise products. The diagonal map of S into that product has kernel ν and regular image, because a homomorphic image of a regular semigroup is regular. A nonempty regular subsemigroup of a CS semigroup is CS: inherit the Green preorders using `x=ya`, `y=yzy` ⇒ `x=yzx`, then `xy R x,L y`, simplicity and primitive idempotents, as explicitly proved in `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`. Thus the diagonal image, isomorphic to S/ν, is CS. Ordinary set-theoretic choice and the Rees–Suschkewitsch theorem are named structural inputs. □

Regularity is important: no claim is made here that an arbitrary subsemigroup of a CS semigroup is CS. The product and image may be infinite; no finite intersection is assumed.

## 2. Exactly when this universal CS actor is pure

Let τ be the actual syntactic idempotence-context congruence. It is the **largest idempotent-pure congruence** on regular S: its quotient is pure by `frontier-20261028-syntactic-purity-all-regular-v1.md`, SHA `20b839e181bc4fff3655cc22cf07675357c0e4ddedb2998fdd1949642d1c1714`; and any pure quotient congruence θ is contained in τ because equal θ-values have equal idempotence tests in every context.

If S/τ is CS, then `ν⊆τ`. Since ν's quotient is CS and ν is contained in the idempotence-saturating τ, its quotient map is pure: if [s]_ν is idempotent, lift it to an actual idempotent p using regularity; then s ν p implies s τ p, so s is idempotent. Conversely, if the ν map is pure, then ν⊆τ and S/τ is its homomorphic image, hence CS. Therefore

`S/ν pure  ⇔  S/τ completely simple`.                   (1)

Under (1), S/ν is exactly the finest pure CS actor of the named explicit row/group/column construction. This shows the latter is actually **the least CS quotient**, not merely finest within the pure subfamily: ν is itself pure, and its kernel is contained in every CS quotient kernel, pure or otherwise.

## 3. Full congruence interval

When (1) holds, the congruence kernels whose quotients are both pure and CS are exactly

`[ν,τ] = {θ∈Con(S): ν⊆θ⊆τ}`.

Indeed, any pure CS quotient contains ν by minimality and lies within τ by maximal purity. Conversely, any θ in that interval is a quotient of the CS S/ν, hence CS, and θ⊆τ gives idempotence saturation and regular-source purity by the same lift. Thus the pure quotient lattice in `frontier-20261028-pure-cs-quotient-lattice-v1.md`, SHA `21646707ddc27c5fe4a9e6ab2dc2ec118661ed123e5cd8e800fc8b800c0d59bf`, is literally an interval of the ordinary congruence lattice. Its product-of-partitions description is the coordinate refinement of that interval under the candidate's hypotheses.

For S68, the pinned D12 map has kernel ν, the actual D8 map has kernel τ, and the interval has exactly two elements. For the glued chain-ideal band family, ν is the finest left-zero quotient and τ universal; the interval is the partition lattice of chain indices. These example identifications remain conditional on the independently unreviewed source/quotient checks.

No assertion here makes ν pure for every regular S or proves weak E-unitarity alone implies S/τ CS. The original local-r/SQ-E step and all canonical separation remain separate review obligations. No formal proof, independent review or novelty is claimed.
