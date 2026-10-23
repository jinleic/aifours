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

**Correctness:** written proof with two independent model reviews and exact finite checks. It imports Proposition 3 from the cited Song–Chen preprint; that proposition was not re-proved here. Not Lean-verified and not human peer reviewed.

**Priority and significance:** **modest extension**, an elementary corollary of Song–Chen Proposition 3 and an existing spin-flip mechanism. The bounded [priority screen](three-qubit-majorization-priority-audit.md) located no earlier explicit three-qubit statement, which does not establish priority. The general depolarizing-majorization conjecture already appears in [Alhejji–Knill, §III](https://arxiv.org/html/2307.06894v3#S3), before SWTF. The two-copy case for `p<=1` follows from their decomposition and Alhejji's [Proposition 4.4](https://arxiv.org/html/2410.18254v3). No new general method or resolution for `n>=4` or `d>=3` is claimed.

**FRONTIER:** NOVELTY-UNCLEAR. The lane slot has rotated to the four-qubit case (`transitions.json`).

## Amosov prior-work applicability check

The scout flagged [Amosov, arXiv:2401.05104v1](https://arxiv.org/html/2401.05104v1), Theorem 2 (v1 accessed 2026-10-16). It cannot be imported as a valid proof of the target: its tensor step explicitly invokes Proposition 1, which is false as stated. The separate same-coset issue below is a likely drafting defect, not the decisive objection.

- **Composition gap:** Proposition 1 asserts `Phi o Psi prec P star Q` whenever the two channels are separately majorized and `dim H>=mn`. Take both channels to be `T_A(rho)=I_A/2 tensor tr_A(rho)` on two qubits, with `P=Q=(1/2,1/2)`. Both hypotheses hold for every input, and `dim H=mn=4`. But the composition is the same idempotent channel: on `|00><00|` it has spectrum `(1/2,1/2,0,0)`, violating the claimed `(1/4,1/4,1/4,1/4)` bound. The parent's [exact checker](check_amosov_composition.py) confirms the channel identity and idempotence on all 16 matrix units and a separate-factor positive control ([receipt](amosov-composition-parent-check.json)).
- **Literal versus intended hypothesis:** condition (8) includes equal cosets. Setting `[U]=[V]` forces equal weights within each coset. For the standard representation with the nontrivial diagonal Weyl subgroup, the identity coset has weights `1-p+p/d^2` and `p/d^2`, unequal unless `p=1`. Thus that representation fails the printed condition for `p<1`. If the condition instead compares only **distinct** cosets (or uses strict `<`), that standard representation **does** satisfy it throughout `0<=p<=1`. The scout's literal-applicability inference was corrected; its amended-reading inference is valid. We make no arbitrary-representation or arbitrary-subgroup nonexistence claim.
- **Limit:** the counterexample refutes Proposition 1 as stated, not tensor-product majorization. It does not rule out a repaired proof using the special structure of the channels in Theorem 2. A bounded audit of a proof gap does not settle the target or establish our priority.

A prompt-only cross-vendor Claude Opus 5.5 maximum-effort hostile review returned **ACCEPT-WITH-FIXES** ([note](amosov-priority-correction-review.note.md), [receipt](amosov-priority-correction-review.receipt.json)); the applicability/emphasis fixes above are applied ([dispositions](amosov-priority-review-dispositions.json)). The reviewer checked the quoted mathematics, not the primary pages or programs; those were checked separately by the parent. This is not a new review of the three-qubit proof.

