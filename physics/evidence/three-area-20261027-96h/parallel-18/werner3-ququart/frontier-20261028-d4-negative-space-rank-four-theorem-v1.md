# Every nonzero two-local three-ququart operator has rank at least four

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 21:12:53 PDT 2026. This is a **WRITTEN all-operator theorem**, not a selected original target state/control, numerical q3 probe, q3 positivity proof, physical counterexample, novelty claim, parent/f62, independent human/family or formal/Lean result.

## 1. Theorem

Let `H=(C⁴)^tensor3`. A two-local operator is an arbitrary complex linear combination of operators acting nontrivially on at most two of the three sites (with identity on the remaining sites). **Every nonzero two-local operator C on H has rank at least4.** No Hermitian, positivity, commutation or product-operator assumption is made.

### Elementary traceless rank-one span

On any complex C⁴, the linear span of rank-one operators `|y><x|` with `<x,y>=0` is the whole traceless matrix space sl₄. In any orthonormal basis, the off-diagonal matrix units have this form. A diagonal difference is also a linear combination of two such operators: for formal distinct basis labels i,j, put `x=e_i+e_j`, `y=e_i−e_j`; then `<x,y>=0` and

`( |x><y| + |y><x| )/2 = |e_i><e_i|−|e_j><e_j|`.

These are auxiliary linear-algebra functionals used to prove a spanning statement; no original physical C, target state or q3 value is chosen or probed. The trace pairing is nondegenerate on sl₄, so tensor products of these rank-one traceless operators separate every nonzero element of `sl₄⊗sl₄`.

### Actual rank proof

Use the commuting local projections `E_i(X)=(I_i/4)⊗Tr_i X`, `T_i=Id−E_i`. They decompose the full operator space into scalar, one-site, two-site and three-site traceless-support components. For a two-local C the three-site component vanishes.

If some two-site component is nonzero, say `H_12⊗I_3` with `H_12∈sl₄⊗sl₄`, the spanning statement yields local vectors x1,y1 and x2,y2 with `<x_i,y_i>=0` such that

`c=<x1⊗x2, H_12 (y1⊗y2)> != 0`.

Define the linear compression maps `L=<x1|⊗<x2|⊗I_3` and `R=|y1>⊗|y2>⊗I_3`. Every scalar/one-site component and each two-site component not supported on both sites1,2 vanishes under this compression because it contains an identity at a site where `<x_i,y_i>=0`. The sole surviving component gives

`L C R = c I_3`.

Thus `4=rank(c I_3)<=rank(C)`. This is a universal proof for arbitrary C; x/y are abstract dual linear-algebra witnesses depending on C, not a concrete chosen physical input or numerical probe.

If no two-site component is nonzero but a one-site traceless component is, the same one-factor argument compresses C to a nonzero scalar identity on the other two sites and yields rank>=16. If only the scalar component remains, nonzero C is a scalar I_H and has rank64. The theorem follows.

## 2. Consequence for the entire residual negative subspace

`frontier-20261028-d4-residual-negative-space-local-operator-v1.md`, SHA256 `f4505459db3a8a45915eb894dca6aa9eb81bb25fa767f175b925945346a9fb35`, proves that the **entire** negative eigenspace of the residual Choi partial transpose corresponds under global vectorization to operators of the form

`C = c I_H + I_1⊗H_23 + I_2⊗H_13 + I_3⊗H_12`,

with each H_ij locally traceless in both of its factors. This is a subset of the theorem's full two-local space. Therefore every **nonzero** vector lying entirely in the complete negative eigenspace has global Schmidt rank>=4; in particular that entire negative space contains no nonzero Schmidt-rank<=3 vector. This closes the mixed-negative-sector rank question left open in `frontier-20261028-d4-residual-negative-sector-rank-v1.md`, SHA256 `3301a558ee0d815991b05737cfc31a7447b57c4a3f53dc968cb09526824ed274`.

## 3. Crucial boundary: this does not prove original q3

A rank<=2 vector may have both negative and positive Choi spectral components; absence of rank<=2 vectors **entirely inside** the negative eigenspace does not control their relative weights or the sign of the full quadratic form. Thus neither residual 2-positivity/PPT nor domination by the separable S component is proved. The original q3 target remains the full arbitrary-complex rank<=2 statement; its separately checked public-source certificate and exact review/runtime limitations are unchanged.

This is an all-operator abstract proof, with no chosen original physical state/control or numerical target value, no old held premise, no source novelty, all-d/operational, parent/f62, human/family or formal/Lean claim. Earlier disclosed cadence deviations and Main's actual prospective resumption remain unchanged.
