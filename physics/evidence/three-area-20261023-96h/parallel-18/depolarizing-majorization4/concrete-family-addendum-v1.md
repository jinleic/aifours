# Concrete family decided by proof-v1

Observed before creation: **2026-10-23T14:14:40-0700**. This addendum is part of the same one-problem attack. Status: **CANDIDATE**, not separately accepted or priority-cleared.

The pinned candidate is `proof-v1.md`, SHA-256 `5e801b156b8f19ce4048dbe8a5ec3fb0f6499eba1ca42b2cdddcaa8d61a91b7e`.

## Exact non-biseparable family

For every real t, set

`psi_t=(|0000>+|1111>+t|0011>+t|1100>)/sqrt(2+2t^2)`.

Distinct support strings differ in at least two bits, so the one-qubit off-diagonal entries vanish after tracing out the other three qubits. The strings occur in complementary pairs with equal squared amplitudes. Thus every one-qubit marginal is exactly I/2, and `R=0`. Four-qubit spin flip has positive sign on all four even-weight support strings and interchanges complementary strings. Therefore it fixes psi_t and `C=1`. Consequently

`3R+2C=2<157/36`.

Theorem B of the candidate therefore proves **all fifteen** channel partial-sum inequalities, including the previously missing k=2,3,4 and k=6..10, for this entire family and **every physical replacement p in [0,4/3]**.

For `t != 1,-1`, this is not reducible to the earlier three-qubit result by taking a product factor:

- Every one|three Schmidt rank is two, since the one-qubit marginal is I/2.
- Across `12|34`, the nonzero coefficient matrix is `[[1,t],[t,1]]/sqrt(2+2t^2)`, of rank two when t is not ±1.
- Across `13|24` and `14|23`, the coefficient matrix is diagonal up to a column permutation, with entries `(1,t,t,1)/sqrt(2+2t^2)`. It has rank four for nonzero t; at t=0 it still has rank two.

Hence the pure state is entangled across every bipartition for t not ±1. This is a genuine four-party input family, not a biseparable tensor product or a three-qubit corollary.

A compact exact example is

`psi_(1/2)=(2|0000>+|0011>+|1100>+2|1111>)/sqrt(10)`.

Its density matrix is positive and trace one by this normalized vector representation. No numerical state-positivity or eigensolver claim is needed.

## A strict missing-index certificate at the exact example

For every member of this family, the derived identities give

`Tr X_2^2=42`, `Tr X_3^2=10` and `rank X_3<=13`.

For k=6, the spectral moment bound in dimension 16 gives

`K_6(X_2) <=9+sqrt((6*10/16)*(42-36)) =9+sqrt(45/2) <19`,

because `45/2<100`. For k=10 the same square-root term gives

`K_10(X_2)<=15+sqrt(45/2)<23`,

because `45/2<64`. The other central indices and low-noise indices follow from the complete rational-threshold proof, not just these two examples. The common-order bridge converts each to the correct depolarizing-output comparison.

## Honest comparison and residual obligation

The read baseline closes specific indices for **all inputs** and has numerical controls at isolated GHZ/W/cluster/Bell-product states. It does not contain the above state-region proof or this continuum-family derivation. The result here is an actual sufficient-input-region theorem, but it is **not claimed that the family itself was previously open in the literature**, or that an elementary direct diagonalization could not already prove a larger such family. Novelty and specialist significance remain unestablished.

The unrestricted target is unchanged. The first frozen residual is

`K_6(X_2(|psi><psi|))<=19`

for every pure four-qubit psi satisfying `10R+4C>74/3`; such a state necessarily has `R>62/27`. The present family does not meet that residual condition, and proving it therefore does not finish the full target. A further near-product argument addresses a different part of this residual; it must remain separately scoped.
