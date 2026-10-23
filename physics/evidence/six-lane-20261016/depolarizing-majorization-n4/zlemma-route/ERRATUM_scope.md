# Erratum (scope limits) to FROZEN_STATEMENTS.md (frozen doc kept unchanged; parent precision correction)

1. Section 2 ("no PPT/decomposable certificate exists ... at any k ≤ 4"). The exact rational feasible points show
   only that the PARTICULAR relaxation encoded here is not tight. That relaxation is the conj(U)⊗U-twirled PPT
   relaxation, i.e. a degree-2 decomposable certificate in the (σ, Π) bilinear encoding with the stated
   constraints. The points do NOT rule out low-degree SOS certificates under other constraint sets or encodings,
   for example ones using purity, rank, Schmidt or auxiliary variables.
2. Section 3 ("a spectral, non-polynomial compatibility condition, consistent with low-degree SOS failing"). Selecting
   the top Schmidt branch is semialgebraic. It can be encoded with auxiliary PSD or order constraints, for example
   `ρ_l ⪰ μ |a⟩⟨a| ...` with an eigenvalue-order constraint. "Non-polynomial form" is therefore NOT an impossibility
   argument. The numerical failures for arbitrary subspaces or post-selections show only that such an encoding
   must include the top-branch condition.
3. Status unchanged: n = 4 is PARTIAL (certified indices only). The route is stopped by parent decision; no
   higher hierarchy levels or repeated sweeps.
