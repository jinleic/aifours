# Four-party active-sector equality: one shared Pauli axis

Owner **PhysicsAME46-2**. Native observation before this write: **`Wed Oct 28 17:34:27 PDT 2026`**; not exact creation/completion/runtime. **WRITTEN author candidate, unreviewed; exact scope only.** This is a clean additive simplification of the equality criterion in `frontier-20261028-four-party-sector-rigidity-v1.md`, SHA256 `a0d177b8c1d686f1d0a1e63bcc607359a23fe41c37fcf2f9a1ea9fa219ebc69c`; it does not modify that pinned file.

## Statement

For the SAME published Pandya 60-term tensor and the SAME active-sector hypotheses `V_i=U_i⊕D_i`, with arbitrary `U_i∈U(2)` on `span{|1>,|2>}` and monomial `D_i∈U(4)` on its orthogonal complement, the actual support equals60 **if and only if** there is ONE Pauli axis `P∈{X,Y,Z}` and signs `ε_i∈{±1}` such that

`U_i† Z U_i = ε_i P` for EVERY one of the four parties.                                  (S)

Equivalently, for a fixed unitary `H_P` with `H_P† Z H_P=P`, each `U_i` may be written `W_i H_P` with an arbitrary 2×2 monomial unitary `W_i`. The same P must serve every party. The equality locus is the union of these THREE sector families; it is not a statement about general U(6)^4 or all AME states.

## Proof from the earlier exact block criterion

The pinned sector proof established that support=60 iff

`U_i U_j^T` is monomial for every pair i,j, and

`N_i:=U_i† Z U_i ∈ {±X,±Y,±Z}` for every i.                                           (P)

A 2×2 unitary B is monomial iff `B Z B†=±Z`. For `B=U_i U_j^T`, since Z is real,

`B Z B† = U_i (U_j^T Z conjugate(U_j)) U_i† = U_i conjugate(N_j) U_i†`.

Hence B is monomial iff `conjugate(N_j)=±N_i`. On the Pauli set, conjugation fixes X and Z and negates Y. Therefore the last condition is exactly that N_i and N_j use the SAME Pauli axis, with signs unconstrained. Since (P) requires this for every pair, (P) is equivalent to (S).

Choose any fixed `H_P` with `H_P† Z H_P=P`. If (S) holds, put `W_i=U_i H_P†`. Then

`W_i† Z W_i = H_P N_i H_P† = ε_i Z`.

The 2×2 unitary W_i is therefore monomial. Conversely, if all `U_i=W_i H_P` with W_i monomial, then `W_i† Z W_i=±Z`, and all `U_i† Z U_i` are ±P. This proves the parameterization in BOTH directions.

Examples are `H_Z=I`, `H_X=(1/sqrt2)[[1,1],[−1,1]]`, and `H_Y=(1/sqrt2)[[1,−i],[−i,1]]`; each has the specified conjugated Z. The common real and imaginary 45-degree endpoints in the preceding proof correspond to X and Y respectively (the sign of a Pauli axis is immaterial). Arbitrary row phases and swaps are included via W_i, not silently gauge-fixed.

## Scope and evidence

The 24 I/J/X/Z blocks and one-of-each pattern on EACH party pair were checked independently from the published table by the two implementations and the signed-block mutation recorded in the preceding report. This additive step is exact elementary 2×2 algebra; it neither extends the available source/status proof nor claims a separate novelty result. The original global minimum, an actual sub-60 tensor and general U(6)^4 orbit optimization remain unresolved. Independent scientific review of both the preceding block theorem and this simplified iff is still required.
