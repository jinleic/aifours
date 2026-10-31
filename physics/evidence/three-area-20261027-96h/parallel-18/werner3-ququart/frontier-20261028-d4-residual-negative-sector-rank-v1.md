# Schmidt ranks inside individual negative residual-Choi sectors

**PhysicsResearch96h-2 / physics-1.** This is a WRITTEN universal structural lemma for the exact fixed residual operator, not a selected physical state/control, a rank-two witness, a q3 proof/counterexample, source novelty or parent/reviewer/formal result.

## 1. The actual negative sectors

The complete operator theorem `frontier-20261028-d4-residual-choi-partial-transpose-spectrum-v1.md`, SHA256 `dba645c69cadfa5d1d1f5d487107a75b0e21bd039e1553fa431dd78daf3d549a`, identifies the negative eigenspaces of `J(R)^(T_out)` in the local input/output-pair regrouping. Put `Omega_i=Σ_(r=0)^3 |r>_(in,i)⊗|r>_(out,i)`, `P_i=|Omega_i><Omega_i|/4`, `Q_i=I−P_i`.

For every site i, the sector with P_i and Q on the other two sites has eigenvalue −13/12. The all-P sector has eigenvalue −3/4. These are the **only** negative sectors; no original physical matrix C has been chosen or evaluated.

## 2. Exact Schmidt ranks inside each individual sector

Fix any i. Every vector in `range(P_i⊗Q_j⊗Q_k)` is of the form

`Omega_i ⊗ v`, with `v∈range(Q_j⊗Q_k)`.

The vector Omega_i has Schmidt rank4 across local input i | output i. Under the fixed regrouping into global input H_in | output H_out, Schmidt rank is multiplicative on tensor products. Consequently, for **every nonzero** v,

`SchmidtRank(Omega_i⊗v) = 4·SchmidtRank(v) >= 4`.

This statement holds simultaneously for all three possible sites and all such v. The all-P sector is one-dimensional, spanned by `Omega_1⊗Omega_2⊗Omega_3`, whose global Schmidt rank is exactly `4³=64`.

Thus no nonzero Schmidt-rank<=2 vector lies **entirely inside any single one** of these four negative eigensectors.

## 3. Why this is not a rank-two positivity proof

A general rank<=2 vector need not lie entirely in one spectral sector; components from different negative sectors and positive sectors can interfere in the global rank constraint. In particular, the absence of a low-rank vector inside each individual negative sector does **not** establish 2-block positivity, residual PPT, or domination by the separable S component. No assertion is made about the Schmidt ranks of arbitrary superpositions of different sectors or the sign of their quadratic form.

The full original target still needs `(S+N)^(T_H)>=0` for every global encoded-qubit input, or the separately audited public-source certificate. This note is a method-level structural fact only, not physical distillability, all-d/novelty, human/family, formal/Lean or parent/f62 acceptance. Historical held material is not a premise and the disclosed cadence gap remains unchanged.
