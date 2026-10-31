# The original local map does not admit free non-unitary whitening

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN all-variable algebraic obstruction to a tempting use of the generic full-support domain. It neither proves nor disproves the original three-copy q3 target, does not evaluate any physical C/state/control, and is unreviewed until a prospective independent assessment.

## Exact covariance criterion

Let `Phi(X)=Tr(X)I4−X/2`. For an invertible complex 4×4 matrix G, the identity

`Phi(G X G†) = G Phi(X) G† for EVERY complex X`                         (1)

holds **if and only if** `G=sqrt(c) U` for some c>0 and unitary U.

To prove necessity, expand both sides of (1). The `−G X G†/2` terms cancel, leaving

`Tr(G†G X) I4 = Tr(X) G G†` for every X.                               (2)

For all traceless X, (2) gives `Tr(G†G X)=0`. The trace pairing on complex matrices is nondegenerate and the annihilator of the traceless subspace is the scalar span of I, so `G†G=c I4`. Invertibility gives c>0, and the polar decomposition gives G=sqrt(c)U. Conversely such a G satisfies (1) by ordinary unitary invariance of trace.

## Exact relevance to the original q3 route

The unreviewed dense-domain lemma `frontier-20261028-d4-dense-local-support-boundary-extension-v1.md`, SHA256 `4e6fe20463ddba8ebf32fba9cfd9139d058837b05a618732cc0b85eb91bffff3`, proves that all three local reductions of a generic global isometry `V:C²→(C⁴)^tensor3` are invertible and that any proof of the original global PSD inequality on **all** such generic V would extend to every boundary by continuity.

The present criterion shows that one cannot simply whiten a non-scalar local reduction by a non-unitary G and then cancel the filter through the **same** original Phi by (1). The absence of that free covariance is an exact obstacle to this particular naive step, even though the local inverse exists. It does not assert that a more sophisticated dual/conjugate filter, a proof tailored to the actual correlated source pair, or any other analytic method fails.

No selected G or physical state was tested, and no tensor-stability, q3 inequality, counterexample, uniform gap, physical operational consequence, all-d/novelty, parent/f62, human/model-family or Lean/kernel acceptance is claimed. Historical held results are not premises; the separately disclosed 19:04 cadence deviation is not retroactively cured.
