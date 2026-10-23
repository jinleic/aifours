# Three-qubit depolarizing-output majorization: parent verdict

## Statement

For the qubit replacement-noise channel `D_p(X)=(1-p)X+(p/2)tr(X)I` and **every** three-qubit density operator `rho`,

`D_p^{tensor 3}(rho)  prec  D_p^{tensor 3}(|000><000|)`   for every physical `p in [0,4/3]`.

This is the `n=3, d=2` case of the output-majorization conjecture stated as Eq. (2) of Song–Wang–Tomamichel–Fang, [arXiv:2609.37240v1](https://arxiv.org/abs/2609.37240v1) (29 Sep 2026), whose general statement the authors leave open (Section 5: "A central one is to establish the full majorization relation in Eq. (2) in general"). The parent opened that primary text: Eq. (1) defines the channel for `0 <= p <= d^2/(d^2-1)`, which is `4/3` for qubits, and Eq. (2) quantifies over arbitrary, possibly entangled, inputs. The `p` here is replacement noise, not the total Pauli error used by the capacity lane.

The proof covers a wider Song–Chen weight region (Theorem A in the lane package): `Q=I/2` and comonotone singleton/pair target weights. General compatible-marginal spin alignment (arbitrary measures or arbitrary `Q`) remains open.

## Proof structure and imported input

1. Expand `D_p^{tensor 3}` into compatible marginals with weights `(1-p)^{|I|}p^{3-|I|}`.
2. Singleton block: commuting Kronecker sum, majorized by a doubly stochastic mixture of permutations.
3. Pair block: **imported** Song–Chen [arXiv:2603.25410v1](https://arxiv.org/html/2603.25410v1) Proposition 3. The parent opened its exact statement (`a,b,c>=0`, `a+b+c=1`, any three-qubit state) and proof outline; homogeneity removes the normalization.
4. Full-state block: every state is majorized by a pure state.
5. The targets are diagonal and nonincreasing in one common order, so Ky Fan sums add; subadditivity closes the chain.
6. For `p>1`: `sigma_y X^T sigma_y = tr(X)I-X` gives `J D_p = D_(2-p)`. The tensor power is conjugation by `sigma_y^{tensor n}` composed with the **global** transpose, so `D_p^{tensor n}` and `D_(2-p)^{tensor n}` outputs are isospectral for every input. Only this spectral identity is used, not positivity of `J`.

## Evidence

| Gate | Result | Artifact |
|---|---|---|
| Worker cross-vendor review | Codex `gpt-6.1-sol`, maximum effort: ACCEPT-WITH-FIXES, four low-severity fixes applied in `PROOF_v1_1.md` | `physics/evidence/six-lane-20261016/spin-alignment-n3/review/codex-theoremA-*`, `frozen-theoremA-v1/` |
| Parent same-vendor review | Claude Opus 5.5 maximum effort, prompt-only: **ACCEPT**, conditional only on Song–Chen Prop. 3 as quoted. It also proves a sharper comonotonicity condition (any labeling) and confirms the full `[0,4/3]` range. | `three-qubit-majorization-review.note.md`, receipt alongside |
| Spectral reflection | 20 exact rational matrix identities (`n=1..4`, five `p` values) pass; replacing transpose by adjoint is rejected. A first, unexpanded implementation timed out at 180 s without a verdict; that attempt is preserved in the receipt. | `check_qubit_depolarizing_spinflip.py`, `qubit-depolarizing-spinflip-check.json` |
| Primary sources | Parent opened SWTF Eq. (1)–(2), Section 5 and Song–Chen Prop. 3 and its proof | URLs above |

## Status

**Correctness:** written proof with two independent model reviews and exact finite checks. It depends on a published, refereeable but not re-proved Proposition 3. Not Lean-verified and not human peer reviewed.

**Priority and significance:** a dedicated primary-source priority screen is running (`DepolMajorizationPriority`). Until it returns, use: "an elementary consequence of Song–Chen Proposition 3 and a spin-flip spectral symmetry; settles the three-qubit case of an explicitly open 2026 conjecture if no earlier statement exists." It is not a new general method and does not settle the conjecture for `n>=4` or `d>=3`.

**FRONTIER:** NOVELTY-UNCLEAR. The lane slot has rotated to the four-qubit case (`transitions.json`).
