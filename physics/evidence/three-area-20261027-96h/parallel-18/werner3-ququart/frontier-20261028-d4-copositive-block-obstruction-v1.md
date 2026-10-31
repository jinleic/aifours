# Copositive block: what the Kraus argument does and does not prove

**PhysicsResearch96h-2 / physics-1.** This is an additive WRITTEN all-variable audit of the exact original d4 source interface. It does not give a new bound on q3 or a chosen-state test, and it does not replace the public certificate. It records the precise direction mismatch that prevents the elementary CP decomposition from proving the required rank-two result automatically.

Use `Phi(X)=Tr(X)I4−X/2`, `Lambda=Phi^tensor3`, `Psi(X)=Tr(X)I4−X^T/2` and `Xi=Psi^tensor3`. The explicit Kraus formula in `frontier-20261028-d4-universal-positive-map-interface-v1.md`, SHA256 `4109b5f5b03ab8362caf05a2c43f4cfe92d59e91a704b807dec7ef3aaa106004`, proves Xi completely positive and `Lambda=T_H∘Xi` with T_H the complete H matrix transpose.

For arbitrary orthonormal A1,A2∈H, put `a=(A1⊗e1+A2⊗e2)/sqrt2`, and define P,Q,B exactly as in the full-pair Schur note `frontier-20261028-d4-universal-stiefel-schur-interface-v1.md`, SHA256 `37cc2d1eadd40ba02caeacff7cfadf7288bebecb42795440398e70c8394b6b2e`:

`P=Lambda(|A1><A1|)`, `Q=Lambda(|A2><A2|)`, `B=Lambda(|A1><A2|)`.

The source's original q3 target for this pair needs the **specific** block

`M=(1/2)[[P,B],[B†,Q]] >=0`.                                (required)

On the other hand, complete positivity of Xi gives

`N=(Xi⊗id_2)(|a><a|)>=0`.

Taking the whole H⊗C² matrix transpose preserves PSD and swaps the two auxiliary off-diagonal blocks. Using `Lambda=T_H∘Xi` gives the **different** automatic block

`N^T=(1/2)[[P,B†],[B,Q]] >=0`.                              (automatic)

The known universal diagonal bounds `P,Q>=I/8` allow Schur complements. The automatic statement yields

`||P^(−1/2) B† Q^(−1/2)||op<=1`.

The required original statement instead asks

`||P^(−1/2) B Q^(−1/2)||op<=1`.

These are not the same operator inequality for general Hermitian P,Q and non-Hermitian B; taking an adjoint swaps P and Q as well as B, and swapping A1,A2 reproduces the automatic inequality rather than turning it into the required one. Thus no appeal to CP of Xi, positivity of Lambda on rank-one inputs, block diagonal PSD or global transpose alone pays the outstanding 2-positivity implication. The already pinned exact source certificate supports that implication conditionally on its independent mathematical/code/runtime audit.

This is not a counterexample, a proof that the required inequality fails, a claim that no analytic proof exists, a physical operational result, novelty, a formal/kernel check, independent-family/human review or parent adoption. No held outcome is used as a premise.
