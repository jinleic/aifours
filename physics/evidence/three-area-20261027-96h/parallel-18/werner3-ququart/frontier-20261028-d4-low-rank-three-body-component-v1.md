# Every nonzero original low-rank operator has a three-body component

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN universal corollary of the exact two-local rank theorem, not an evaluated physical input/state/control or a proof/counterexample of the original q3 inequality. It is unreviewed and carries no novelty, operational, all-d, human/family, formal/Lean or parent/f62 acceptance.

For `H=(C⁴)^tensor3`, use the commuting local operator projections

`E_i(C)=(I_i/4)⊗Tr_i C`, `T_i=Id−E_i`.

The operator space decomposes as the direct sum of the eight products of E_i/T_i. In particular, `T_1T_2T_3 C=0` is **equivalent** to C being two-local: all its surviving components have at least one local identity factor and therefore act nontrivially on at most two sites.

The separate exact theorem `frontier-20261028-d4-negative-space-rank-four-theorem-v1.md`, SHA256 `eb07a8ce4d5f3c121873e3d28f628b82a102698c5d8711225c82b81705904172`, proves that every nonzero two-local complex operator has rank at least4. Hence, for **every** nonzero complex C with rank<=3,

`T_1 T_2 T_3 C != 0`.                                               (1)

Under global operator vectorization, T_i corresponds to the complement `Q_i=I−|Omega_i><Omega_i|/4` of the local input-output Bell projector. Therefore (1) says every nonzero original rank<=2 operator has a nonzero component in `Q_1⊗Q_2⊗Q_3`. In the separately derived full residual-Choi-partial-transpose spectrum, that is the k=0 **positive** spectral sector (eigenvalue 3/4).

This is a necessary structural component, not an energy-domination estimate. The same rank<=2 vector may also have components in the negative sectors, and (1) does not bound their relative size or prove the total quadratic form nonnegative. In particular no original q3, residual 2-positivity/PPT, strict gap, equality classification, physical operational or new-discovery claim follows. The previous exact source certificate and its parent/review/runtime limitations remain separate, as do the earlier disclosed cadence deviations.
