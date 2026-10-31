# Two value-side complements: the BMO surrogate is NOT exact for the adapted quotient, and the uncontrolled EMS literal gain lies in [G2, √2·G2]

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing this body: **Tue Oct 27 06:44:51 PDT 2026**.

**Status: NEW COMPLETE WRITTEN OWNER-CANDIDATE.** Not reviewed or adopted. Written under v209, value side only. Only all-variable, source-fixed conventional proofs are used. No identity was machine-checked, and nothing was evaluated numerically, decimalized or probed. No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay was used, and there is no new GO.

## 0. Statements

**Proposition O (precise obstruction).**

- **Setting.** The canonical one-Brownian filtration.
- **Claim.** The conditional future-energy norm `||r||_*` of v27 Theorem A does NOT evaluate the adapted input quotient nu exactly. There are progressive r ∈ E2 with nu(r) > ||r||_*.
- **Consequence for the constant.** Let c* be the best universal constant in nu ≤ c*·||·||_*. Then

  1 < c* ≤ √2,

  while the lower constant 1 is attained, for example by every deterministic r.
- **Consequence for evaluation.** Any exact evaluation of nu must use information beyond ||r||_*. Sharpness of √2 remains open.

**Corollary U (uncontrolled EMS slice, two-sided).**

- **Setting.**
  - Constant data (A, A0, C, D0), any D0 rank, any h ≥ 0, on the canonical filtration.
  - The autonomous system dX = AX dt + A0X dW is exponentially mean-square stable (EMS): E|X_t|^2 ≤ M e^{−λt}|x_0|^2 for every deterministic x_0.
- **Claim.** The uncontrolled response map (equivalently, the zero law u = 0 on any plant with these A, A0, C, D0) satisfies

  `G2,∞ ≤ G1,∞ ≤ √2·G2,∞`.
- **Descriptor reading.** When B = B0 = D1 = 0, the adopted descriptor equals G1,∞ = sup_T kappa_risk(T,h). The full uncontrolled EMS descriptor is therefore evaluated within a factor √2 by the Hilbert RMS gain.
- **Which part is new.** The lower bound is the ADOPTED v14 theorem at the zero law. The upper bound is v27 Corollary C1. The composition narrows the adopted v14 factor 2√2 to √2 on this slice.

**NOT delivered.** No exact literal gain, no exact nu, no √2 sharpness, no controller, no common causal or stationary policy, no internal-EMS synthesis, and no application outside the stated domains. Corollary U is NOT used to transfer RMS synthesis to controlled plants. The R4 RMS-transfer route stays STOPPED.

## 1. Authority, inputs, separation

**Authority.** v209 (`1ec52034…`), read FIRST. This packet continues the value-side series:

- v27 (`af2abd51001ca6d16dd3d4415d49104c25110b7f16415689052329f1a77f55b5`);
- v28 (`e30bdd3d196883dd1b7842472c7f9ab1386a06e4ac78ff96cff3a820f64ac87b`).

Both are unreviewed owner-candidates. Only v27 Theorem A, the definition of ||·||_*, and Corollary C1 are cited, and their full proofs are displayed in v27.

**Adopted inputs read completely before use, this session:**

| Source | Read | LF | SHA256 |
|---|---|---|---|
| v25 | complete | 348 | `8c381b1f…` |
| v26 | complete | 308 | `6666f555…` |
| v21/v25/v26 parent record | complete | 74 | `1f00e0c6…` |
| v14 parent adoption record `preview-v14-sequential-probability-parent-v1.md` | raw, through its bindings | 61 | `e89a06e05bb1506ff1d896ab9541bb9a6a4f00c89e8fea5e9731ea1e1f4cba07` |

**v14 domain as adopted.**

- One fixed deterministic, STATIONARY, measurable law with F(0,0) = 0, using the current state, a Hilbert current-input window and finitely many fixed taps.
- Strong all-input well-posedness and nonexplosion.
- STATE-LOC: state-local Lipschitz constants uniform over the same input tuple.
- Zero-window EMS with common M and λ for every deterministic initial state.
- Infinite horizon; canonical progressive expected-L2 inputs; local pathwise control admissibility.
- Conclusion: G2(F) ≤ G1(F) ≤ 2√2·G2(F).

**Separation.** None of the following is consumed:

- storage function, Riccati, Gramian or LMI certificate;
- a controller construction;
- a selected control or changed output;
- quarantined guidance from post56, post60, postS126 or the self-release;
- the RMS source.

Proposition O is a statement about dual norms of adapted processes, not about a plant.

## 2. Proof of Proposition O

**Parameters.** Fix c ∈ (0,1) and put σ_c := (1 − c^2)^{1/2} ∈ (0,1). Choose

- ε ∈ (0, σ_c^2];
- p ∈ (0, σ_c^2/(1 + σ_c + σ_c^2)).

By continuity of the Gaussian law there is κ with P(W_1 − W_{1−ε} > κ) = p. Put ξ := 1{W_1 − W_{1−ε} > κ}; it is F_1-measurable. All parameters are symbolic. Every c ∈ (0,1) admits such ε and p, and no instance is selected or evaluated.

**The test covector.** On [0, 2], define r_t := 1 for t ∈ [0,1] and r_t := c·ξ for t ∈ (1,2]. It is progressive and bounded, so r ∈ E2.

**Step 1: the conditional energy norm.** Write Y_s := E[∫_s^2 r^2 | F_s] and split by time.

| Range of s | Value of Y_s | Bound |
|---|---|---|
| s ∈ [0, 1−ε] | (1 − s) + c^2 p, since ξ depends only on increments after 1−ε | ≤ 1 + c^2 p, equality at s = 0 |
| s ∈ (1−ε, 1] | (1 − s) + c^2 P(ξ=1 \| F_s) | ≤ ε + c^2 ≤ σ_c^2 + c^2 = 1 |
| s ∈ (1, 2] | c^2 ξ (2 − s) | ≤ c^2 < 1 |

Hence ||r||_*^2 = 1 + c^2 p.

**Step 2: a better adapted input.** Let β := c/σ_c and take w_t := 1 on [0,1] and w_t := βξ on (1,2]. It is progressive, so it is an original E2 input. Then

- E<r,w> = 1 + cβp;
- N1(w) = E(1 + β^2 ξ)^{1/2} = 1 + p((1+β^2)^{1/2} − 1).

Since cβ = (1−σ_c^2)/σ_c and (1+β^2)^{1/2} = 1/σ_c, set m := p(1−σ_c). Then

`E<r,w>/N1(w) = (σ_c + m(1+σ_c))/(σ_c + m) = 1 + mσ_c/(σ_c + m)`.

**Step 3: exact comparison.** Note ||r||_*^2 = 1 + m(1+σ_c). Expand and multiply by (σ_c+m)^2/m > 0:

`[(1 + mσ_c/(σ_c+m))^2 − (1 + m(1+σ_c))]·(σ_c+m)^2/m = σ_c^2(1−σ_c) − σ_c^2 m − m^2(1+σ_c)`.

Write the right side as σ_c^2(1−σ_c) − m(σ_c^2 + m(1+σ_c)). The choice of p gives

- m = p(1−σ_c) < σ_c^2(1−σ_c)/(1+σ_c+σ_c^2) ≤ 1, and therefore
- m(σ_c^2 + m(1+σ_c)) ≤ m(1+σ_c+σ_c^2) < σ_c^2(1−σ_c).

So the right side is positive, and nu(r) ≥ E<r,w>/N1(w) > (1 + c^2 p)^{1/2} = ||r||_*.

**Step 4: why the time window matters.**

- If ξ were revealed by a Brownian event spread over [0,1], then ess sup P(ξ=1 | F_s) would approach 1 at early s. That would raise ||r||_*^2 toward 1 + c^2, and the strict gap could fail.
- Taking the late increment window (1−ε, 1] with ε ≤ σ_c^2 keeps every conditional term below the s = 0 value.
- This is the precise continuous-filtration mechanism; no discrete-time jump is used.

∎

**Remarks.**

- For deterministic r, ||r||_* = ||r||_{L2} = nu(r), so the lower constant 1 is attained.
- Proposition O concerns nu itself. It does NOT decide whether the DESCRIPTOR-level sandwich of v27 Theorem B, beta1 ≤ kappa_risk ≤ √2·beta1, is ever strict on the left, because the supremum over duals could restore equality. That question remains OPEN, and the gate-I value question is part of it.

## 3. Proof of Corollary U

**The zero law is in the adopted v14 domain.**

- F ≡ 0 is deterministic, stationary and measurable, with F(0,0) = 0.
- The closed loop is the linear SDE dX = (AX + Cw(t−h))dt + A0X dW. It has strong all-input well-posedness and nonexplosion for every canonical progressive expected-L2 input; this is ordinary linear-SDE theory.
- STATE-LOC holds trivially, since the law is constant in the state.
- Zero-window EMS is the stated hypothesis, with common M and λ for every deterministic initial state.
- Output: z = D0X, since u = 0. Control admissibility is trivial.

**Lower bound.** The adopted v14 theorem gives G2,∞ ≤ G1,∞ for this law.

**Upper bound.** v27 Corollary C1 applies to the same uncontrolled response map T_C, at any D0 rank and any h. It gives G1(T,h) ≤ √2·G2(T,h) for every finite T. Hence

G1,∞ = sup_T G1(T,h) ≤ √2·sup_T G2(T,h) ≤ √2·G2,∞.

Two adopted v26 facts are used in this step:

- prefix and zero-extension comparison;
- UC-INF/UC-ALL for B = B0 = D1 = 0.

Finally G1,∞ = sup_T kappa_risk(T,h), by the adopted UC-ALL and UC-INF. ∎

**Remarks.**

- EMS makes G2,∞ finite.
- Without EMS only the upper half is asserted, in extended reals.
- At the source-fixed gate-I anchor this reproduces γ* ≤ G1 ≤ √2γ*, consistent with v27. The exact gate-I value remains OPEN.

## 4. Boundaries

**Open value-side questions.**

- The exact nu.
- The optimal constant c* ∈ (1, √2].
- Descriptor-level exactness: whether kappa_risk = beta1, or whether G1 = g12 on uncontrolled data.
- Lower bounds of kappa_risk by g2^ol at actuated data.
- Gate-I exact value.

**Out of scope.** Corollary U is stated only for the uncontrolled response (the zero law). No extension to nonzero laws or controlled closed loops is made here. In particular this packet supplies no RMS-to-literal synthesis transfer, which stays STOPPED as route R4.

**Original problem.** The common causal/stationary printed controller, internal EMS, prescribed-γ synthesis and the CP/non-E1 application boundaries remain UNRESOLVED. The realization routes C1–C3 stay STOPPED (v209).

## 5. Process and assurance

**What was done.** Written exact mathematics only: v209 was read FIRST, and the adopted inputs were read completely before use. No pinned, frozen or shared edit was made. No Git, deletion, publication or external model was used.

**Retained.** All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, the protected S242 window, and HELD_C889 (never opened).

**Limits.** This is not formal, kernel, human, configured-family, executable or novelty acceptance. Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v29.**
