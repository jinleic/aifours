# Erratum 2 (short written-only addendum) to the rank-two dual master reduction

**Status: WRITTEN-ONLY, UNREVIEWED.** Corrects two displayed claims found by the parent's complete read. No calculation, test, replay or code of any kind was executed for this addendum. Original `...master-reduction-v1.md` SHA c9003960… and erratum-1 SHA fd5cd81e… are preserved byte-unchanged. Nothing here asserts the former errors became correct; the mathematical source remains unreviewed.

## 1. Normalization error in erratum-1 §2, (Q)⇒(T2) step

Erratum-1 displayed `√(2L)·√(q(R))`, whose best conclusion is only `2√L·||R||` and does not close the implication. The correct chain is:

`|⟨(Tr_B R)_0,A⟩+⟨(Tr_A R)_0,B⟩| ≤ √L·√(q(R)) ≤ √(2L)·||R||`,

using `q(R)=||(Tr_B R)_0||²+||(Tr_A R)_0||²` for the 4×4 traceless projections and (Q). Hence `|Tr(R†X)|² ≤ 2L||R||_F²`, and Ky Fan over unit rank≤2 R gives `S2(X) ≤ 2L`. The (T2)⇒(∗) and (∗)⇒(Q) directions of erratum-1 §2 are unaffected.

## 2. Withdrawal of the original §5 route-closure

Withdrawn: the claimed structural impossibility and the pair-space variance argument. In fact `G(R,R):=||R||_F²+|Tr R|²−||Tr_B R||_F²−||Tr_A R||_F²` IS the diagonal of a Hermitian sesquilinear form on the operator space (Gram pieces of the identity, trace, and the two partial-trace maps), so operator-space polarization is available; the pair-space objection conflated two different polarizations and closes no route. Retained claim, exactly and only: **rank-one positivity `G(r,r)=4p(r)≥0` by itself does not establish the rank-two bound needed in the corrected condition (2.2′); whether G is positive semidefinite — or satisfies the needed Cauchy–Schwarz bound — on rank-two spans is the genuine unpaid extension.** No impossibility statement of any strength is claimed.

## 3. Standing boundaries

Master reduction, erratum-1 and this addendum remain UNREVIEWED and are to be read together; no unrestricted T2/T3/Z2/q3, f274 η, physical counterexample, execution, selected parameter, novelty or adoption is claimed. The quarantined cross-term episode remains HELD/ZERO/NONINPUT and unused.
