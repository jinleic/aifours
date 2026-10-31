# Intrinsic actor-core separation for the physical Q1 target

**Status: NEW AUTHOR WRITTEN CONDITIONAL INTERFACE; UNREVIEWED / UNADOPTED.** This substitutes the finest pure actor for the coarsest syntactic actor in the remaining exact separation problem. It uses the named universal-actor and same-band lifting candidates; it does not solve separation or establish the printed-book product convention.

## 1. Actor-indistinguishable pairs

Let S be regular with actual idempotence-context quotient q completely simple. Its purity is automatic by `frontier-20261028-syntactic-purity-all-regular-v1.md`, SHA `20b839e181bc4fff3655cc22cf07675357c0e4ddedb2998fdd1949642d1c1714`. Let `q̂:S→D̂` be the finest pure CS quotient from `frontier-20261028-finest-pure-cs-actor-v1.md`, SHA `772cf39e2d5c6aab1c127ed73edaf3e7c2e617deda8f3113b8059df19f4c83ab`.

For any s,t∈S, the following are equivalent:

* `q̂(s)=q̂(t)`;
* every idempotent-pure homomorphism from S to a CS semigroup sends s,t to the same element.

The first implies the second by universal factorization; the second implies the first because q̂ itself is pure and CS. In source terms, equality means that s,t have the same finest row class, the same finest column class, and the same actual q value. Thus these pairs are **intrinsically actor-indistinguishable** in every faithful physical host: its actor projection is pure. Conversely, pairs separated by q̂ are separated by at least one pure actor, though that alone does NOT construct a faithful band host.

## 2. Exact all-actor source separation target

Let C be the canonical seminormal-band quotient over q̂, with its source band-coordinate map β. Conditional on the standard canonical universal property, the following are equivalent:

1. S embeds into some seminormal-band-by-CS physical product, with arbitrary actor.
2. The canonical physical map `κ_q̂:S→P(C,D̂)` is injective.
3. β separates every distinct pair e,f∈E(S) with `q̂(e)=q̂(f)`.

1⇒2 uses the SAME-band lift of an arbitrary host to q̂ from `frontier-20261028-finest-actor-same-band-lift-v1.md`, SHA `fa8bcc7beb069fbe873380429415f9c90723420a241abd078fe206973d1d8c3c`; the canonical band maps equivariantly into that host, so canonical equality would contradict faithfulness. 2⇒1 is the canonical host. The equivalence 2⇔3 is the direct idempotent-separation argument in `frontier-20261028-seminormal-physical-canonical-interface-v1.md`, SHA `12f3a3c4e46d7d3460e0dba7d46b800a263ab3d1f7490e08644a5450367a3ac2`, applied to the pure q̂ rather than q; it uses the same-q̂ products with an inverse and natural-order antisymmetry, not an unstated global R/L result.

Within each idempotent q̂-fibre, β is a band homomorphism. Therefore full separation can be broken into comparable, R and L separation by the elementary reduction in the cited interface. The necessary distinct pairs are generally fewer than for coarsest q: S68 has actual actor8 and finest actor12, and its q̂-host needs band8 whereas the fixed-q host needs band10. The reduction neither proves any of the three pieces nor permits transferring an old quarantined proof as guidance.

## 3. Scope

For finite S, the finitely many q̂-idempotent pairs and the canonical band can be decided in principle as in `frontier-20261028-finite-any-actor-band-optimum-v1.md`, SHA `eaeb5b0b24ed5aa33ed2fe898a50e033443b99f3b02d3e91ba1cfebc88fa8e61`. This is not an efficient general decision bound and does not settle infinite S. The original WEU/local-r hypothesis still needs the named SQ-E CS assertion to enter this interface. All antecedent theorems, finite witness, proof and source conventions remain unreviewed; no novelty or formal proof is claimed.
