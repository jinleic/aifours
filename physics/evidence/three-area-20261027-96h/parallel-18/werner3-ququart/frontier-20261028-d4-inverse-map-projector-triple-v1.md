# Reversible projector-triple encoding of the original d4 target

**PhysicsResearch96h-2 / physics-1.** This WRITTEN all-variable representation is a clean replacement for the two explicit Stiefel vectors in the original target. It does not establish the outstanding universal contraction by itself, give a selected input/parameter, invoke an old held outcome, or claim novelty. Its value is that the common-pair constraints become explicit quadratic operator equations; the original source certificate remains the separate computer-assisted proof route.

## 1. Exact inverse of the original map

On M4(C), `Phi(X)=Tr(X)I4−X/2` is invertible. Taking traces gives `Tr(Phi(X))=(7/2)Tr(X)`, hence

`Phi^(−1)(Y)=(4/7)Tr(Y)I4−2Y`.                            (1)

The identity holds on all complex matrices, not only Hermitian or positive ones. Consequently the actual d4 three-site map `Lambda=Phi^tensor3` has the explicit linear inverse

`Gamma=Lambda^(−1)=(Phi^(−1))^tensor3`.                   (2)

No eigenvalue approximation, semidefinite inverse or selected operator is involved.

## 2. Common Stiefel pair iff quadratic projector-triple equations

For a same-pair Stiefel triple `P=Lambda(|A1><A1|)`, `Q=Lambda(|A2><A2|)`, `B=Lambda(|A1><A2|)`, put

`p=Gamma(P)`, `q=Gamma(Q)`, `x=Gamma(B)`.

Then p,q,x satisfy the **exact coupled equations**

`p=p†=p²`, `Tr(p)=1`,
`q=q†=q²`, `Tr(q)=1`,
`pq=0`, `x x†=p`, `x† x=q`.                               (E)

Conversely, suppose complex 64×64 P,Q,B have inverse images p,q,x obeying (E). A Hermitian idempotent of trace1 is an orthogonal rank-one projector. Choose a unit A2 spanning ran q and set A1=xA2. Then

`||A1||²=<A2,x†x A2>=1`, `pA1=A1`,
`<A1,A2>=0`, `x=|A1><A2|`,

because `xx†=p` and `x†x=q` make x a rank-one partial isometry from ran q onto ran p. In particular p=|A1><A1| and q=|A2><A2|, and P,Q,B are exactly the Lambda images of that **one** orthonormal pair. No invertibility of x, arbitrary product assumption or boundary limit is needed.

Thus (E), together with the linear bijection (2), is a necessary **and sufficient** description of the original tied source triple. These are quadratic equations in the entries and their conjugates; they do not assert arbitrary P,Q,B independently satisfy the relations.

## 3. Exact target in the new representation

For every pair satisfying (E), the independent rank-one bound proves `P,Q>=I/8`. Therefore the source's original q3 target is equivalent to

`B† P^(−1) B <= Q`                                          (3)

for every P,Q,B whose inverse images satisfy (E), or equivalently to PSD of `[[P,B],[B†,Q]]`. The derivation from the original complex C and the no-gap inverse square-root step are in `frontier-20261028-d4-universal-stiefel-schur-interface-v1.md`, SHA256 `37cc2d1eadd40ba02caeacff7cfadf7288bebecb42795440398e70c8394b6b2e`.

The constraint `pq=0` and the two ordered partial-isometry products in (E) are load-bearing: omitting them enlarges the domain and does not follow from the original target. The opposite-handed automatic bound from copositivity concerns `B†` in the *other* block position and is not a substitute for (3).

## 4. Exact gap and provenance

This representation pins an all-variable candidate interface for a possible analytic proof of (3) using the coupled equations (E); no such proof is asserted here. The previously pinned source certificate supplies the separately verified finite identity/PSD route to the original d4 target, subject to its mathematical, source-map, exact-code and runtime trust boundary. This note does not infer any new unrestricted SOS result, counterexample, rank-two strict gap, equality classification, all-dimensional theorem, physical operational consequence, human/family review, Lean-kernel result or parent adoption.

No selected numerical physical state, control, boundary or parameter was used. Historical held/quarantined outcomes are not mathematical premises and are not retroactively validated.
