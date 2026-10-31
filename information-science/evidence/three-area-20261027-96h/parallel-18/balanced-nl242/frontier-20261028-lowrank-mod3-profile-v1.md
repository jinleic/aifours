# info-6 frontier: corrected mod-three invariant — withdrawn draft

Owner InfoBalancedNL242-2-2. Initial native clock **2026-10-29T00:43:35-0700**; correction clock **2026-10-29T00:51:12-0700**. This local draft and its accompanying `frontier-20261028-lowrank-mod3-profile-check.py` / result used an incorrect factor `256≡−1 mod 3`. Their proposed rank-branch profiles are **INVALID and NONINPUT**. They were never sent to Main, parent-adopted, or used as a premise in an immutable prior result. The checker's apparent “positive control” was a formal non-witness that did not satisfy the required inverse-caller assumptions.

The correct elementary relation for any signed δ:F₂⁸→{−1,0,1}, D=wt(δ), and `M=#{y:Walsh(δ)(y)≠0 mod3}` is

    M≡Σ_y Walsh(δ)(y)² = 256D ≡ D (mod 3),

because `256≡1 mod 3`. The incorrect previous factor invalidated the draft's refinement; **no numerical branch claim is asserted here**. Any successor must be independently derived with this corrected identity and a fresh checker. The invalid checker and receipt remain preserved, not deleted. **END.**
