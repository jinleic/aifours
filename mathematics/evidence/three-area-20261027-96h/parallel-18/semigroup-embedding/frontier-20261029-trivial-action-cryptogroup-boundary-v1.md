# Exactly the cryptogroup sources admit trivial-action physical hosts

**Status: NEW AUTHOR WRITTEN EXACT CLASSIFICATION with a finite nontrivial-action certificate; UNREVIEWED / UNADOPTED.** This strengthens the earlier positive cryptogroup theorem with a converse for arbitrary actor/band. It is a sharp representation boundary, not a full originalQ1 solution, and is not claimed novel.

## 1. General regular-source theorem

Let S be a nonempty regular semigroup. Then S embeds in a trivial-action physical product `B×D`, with B seminormal and D completely simple, **iff** all three conditions hold:

1. S is a cryptogroup: completely regular, with Green H a semigroup congruence;
2. its actual idempotence-context quotient q is completely simple (q is then automatically pure);
3. the band `S/H` is seminormal.

The assertion allows arbitrary finite/infinite B,D and does not fix the actor. It does not replace a nontrivial group action by a trivial one.

## 2. Necessity

The ambient direct product B×D is completely regular: for each (b,d), the ambient H-cell `{b}×H_d` is a group. If regular S embeds in it, Green preorders in S are inherited from the ambient semigroup: `x=ya` and y=yzy with z∈S imply x=yzx; dualize for L. In the ambient product every x is H-related to x², so the same holds in S. A regular element with x H x² is a group element; hence S is completely regular.

The ambient H relation is a congruence: in B, H is equality; in D, H means equal Rees row and column, which multiply by keeping the first row/last column independently of group coefficients. Thus the quotient map

`B×D→B×(I×Λ)`

has precisely H as its kernel. Its restriction to S has kernel H_S by Green inheritance, so H_S is a congruence and `S/H_S` is isomorphic to a subband of `B×(I×Λ)`. Since rectangular bands are seminormal and the variety is closed under products/subbands, condition3 holds. Conditions1 and3 therefore follow without any actor-transport theorem.

The source actor image is a regular subsemigroup of D and hence CS. Its map from S is pure, because an idempotent actor value paired with any band coefficient is idempotent and the host is faithful. Thus actual q is a homomorphic image of that CS actor and is CS, giving2. This step uses ordinary CS/Rees structure, not an original-source SQ-E assumption.

## 3. Sufficiency and the original class

Assume1–3. Define

`j(s)=([s]_H,q(s)) ∈ (S/H)×(S/τ)`.

It is a homomorphism into a trivial-action SN-band-by-CS product. If j(s)=j(t), then s,t lie in the SAME source maximal subgroup, and q(s)=q(t). The restriction of pure q to that subgroup is injective: q(st⁻¹) is the target local-group identity, so purity makes st⁻¹ an idempotent group element and hence its identity. Thus s=t, proving sufficiency.

For an original regular weakly-E locally-r source, condition2 follows from the freshly written source-class theorem. If S is cryptogroup, then each local corner of S/H is isomorphic to the regular band E(eSe): every H-class is a group and has a unique idempotent; sandwiching gives representatives in eSe for the corner's classes, so the restriction of S→S/H on E(eSe) is a bijective band homomorphism. Hence S/H is locally regular and therefore seminormal by the independently unreviewed local-regular/SN identity proof plus its mandatory band-content rationale erratum. Thus within the original class the exact criterion simplifies to **S is a cryptogroup**. This recovers the earlier positive theorem but adds the necessary direction.

## 4. The 68-source requires a genuine nontrivial action

The pinned S68 is completely regular but H is NOT a congruence: source indices24 and26 are H-related, while `8·24=36` and `8·26=38` are not H-related. Therefore it lies outside the exact trivial-action class despite having a faithful 8-band/refined-CS host.

There is a shorter direct obstruction independent of the general theorem. For ANY source homomorphism ρ into ANY band, the literal source equations

`27²=25`, `8·27=39`, `8·25=37`, `39²=61`

give `ρ(27)=ρ(25)`, hence `ρ(39)=ρ(37)`, and `ρ(39)=ρ(61)`, so `ρ(37)=ρ(61)`. On the other hand `37·61=61`, `61·37=37` and `0·37=0·61` force the two idempotents to have the SAME value under every CS homomorphism: same row from the R equations, same column from the equal left context, and the cell idempotent is unique. Thus a direct-product B×D image can never separate the distinct elements37,61, regardless of B's variety or D/action conventions. The failure is not a small-band search limit.

`frontier-20261029-source68-nontrivial-action-checker-v1.py`, SHA `ad958968f9c9a4a10ab72dee49c9111dd54f302510e736b8dc238c62d1027b1e`, ran in the Python eval kernel before Thu Oct29 00:38:02 PDT2026. It checks all displayed source equations, complete regularity by commuting inverses, and the principal-ideal H-congruence counterexample. Its first development run mistakenly tested element27 as a non-completely-regular witness and failed; the source is in fact completely regular. The corrected final verifier proves the relevant H-congruence failure instead. This development error is disclosed rather than treating the failed diagnostic as a source fact.

The group action is therefore not cosmetic in the matching original task. Source-specific faithful nontrivial-action hosts, the universal one-sided decomposition and exact Green reflections do not yet construct the required cocycle for arbitrary noncryptogroup one-sided sources. GeneralQ1/Q2, novelty, formal proof and independent review remain open.
