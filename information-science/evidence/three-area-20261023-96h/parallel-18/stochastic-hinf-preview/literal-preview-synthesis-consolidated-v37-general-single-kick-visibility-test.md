# General (non-commuting) data: a finite algebraic "single-kick visibility" test that forces a STRICT literal-vs-RMS gap

Owner **InfoHinfPreview-2 / info-3**. Clock observed with `/bin/date` immediately before writing: **Tue Oct 27 07:28:08 PDT 2026**.

**Status.**

- NEW COMPLETE WRITTEN OWNER-CANDIDATE, written as a separate successor. Not reviewed, not adopted.
- Value side only, under v209 (`1ec52034…`).
- All-variable, source-fixed conventional proofs. No machine-checked identity.
- Only symbolic choices with explicit existence arguments. No chosen numeric probe.
- No scientific interpreter, Eval, calculator, CAS, program, enumeration, solver or replay. No new GO.
- The frozen v27–v32 are not modified. No v220 file, live review or assignment was read.

## 0. Statement

**Setting.** As in v34 Theorem R:

- uncontrolled constant data (A, A0, C, D0) with ANY commutation relation;
- any dimensions and any D0 rank;
- preview delay δ ≥ 0;
- the canonical one-Brownian filtration;
- EMS autonomous part.

Put Ā := A − A0^2/2, and use the spectral notation of v36: A0 = Σ_j (μ_j P_j + N_j) over C.

**Single-kick visibility (VIS-1).** There are j, k ≥ 0 and m_1, m_2 ∈ {0, …, n−1} such that

- Re μ_j ≠ 0 or k ≥ 1, and
- D0 Ā^{m_2} N_j^k P_j Ā^{m_1} C ≠ 0.

In words: some noise mode that amplifies (a real-part or nilpotent component of A0) is reachable from the input through Ā and observable at the output through Ā.

**Theorem W.** If VIS-1 holds, then G_rob = ∞. Consequently, at every preview δ ≥ 0,

`G2,∞ < G1,∞ ≤ √2·G2,∞`.

The printed literal gain STRICTLY exceeds the RMS gain.

**Corollary W1 (commuting case).** When AA0 = A0A, VIS-1 is exactly v36 VIS, because Ā commutes with N_j^k P_j. So Theorem W contains v36 Theorem V(a).

**Corollary W2 (rank-one real noise).** Let A0 = σ e e^T with σ ≠ 0 and |e| = 1, and A arbitrary. Then:

- the decomposition has μ = σ with P = e e^T, plus μ = 0 on e^⊥;
- VIS-1 holds iff D0 Ā^{m_2} e ≠ 0 and e^T Ā^{m_1} C ≠ 0 for some m_1, m_2. That is, e lies outside the unobservable subspace of (Ā, D0), and e is not orthogonal to the reachable subspace of (Ā, C).

Every EMS plant whose real noise direction e is visible in this sense therefore has a strict gap.

**Corollary W3 (genericity).** Fix (A, A0) with at least one bad component, i.e. Re μ_j ≠ 0 or N_j ≠ 0 for some j.

- The set of (C, D0) for which VIS-1 FAILS is a proper real-algebraic subset, cut out by the polynomial equations D0 Ā^{m_2} N_j^k P_j Ā^{m_1} C = 0.
- It is proper: the real and imaginary parts of P_j or N_j P_j are not both zero. So some real unit vectors x, y have y^T N_j^k P_j x ≠ 0 with k = 0 or 1 as appropriate. Then C = x and D0 = y^T give a nonzero term at m_1 = m_2 = 0.
- Hence, for such (A, A0), EQUALITY G1 = G2 can hold only on a proper algebraic subset of output/input maps.

**Residual class.** VIS-1 can fail for every (C, D0) only if A0 has no bad component, i.e. A0 is diagonalizable over C with purely imaginary spectrum. This is the "rotation-like" noise class. It includes v36 case (c). There, multi-kick words and switching effects may still give G_rob = ∞; this packet does not decide that class.

**NOT delivered.**

- A characterization when VIS-1 fails for non-commuting data.
- Exact gains.
- Controlled data, a controller, synthesis, or an RMS-to-literal transfer. C1–C3 and R4 STOPPED.

## 1. Inputs and separation

**Adopted inputs** (read completely this session):

| Input | LF | Pin |
|---|---|---|
| v25 | 348 | `8c381b1f…` |
| v26 | 308 | `6666f555…` |
| parent | 74 | `1f00e0c6…` |

**Cited owner packets** (unreviewed):

| Packet | Pin | Used for |
|---|---|---|
| v27 | `af2abd51…` | the √2 upper bound |
| v31 | `4c2a7b9b…` | G2,∞ < ∞ and G2,∞ ≤ G1,∞ |
| v34 | `6fcca986…` | Lemma DS, the definitions of k_ℓ, Ψ_ℓ and G_rob, and Theorem R |
| v36 | `4ecfa7c6…` | the spectral notation, and Lemma EP (bounded exponential polynomials, with complete proof there) |

**Separation.** None of the following is used:

- storage, Riccati/Gramian/LMI, a controller construction, a selected control or a changed output;
- quarantined guidance or the RMS source.

**Ordinary tools.**

- The linear-ODE flow bound ||Ψ − I|| ≤ e^{εc} − 1 for a generator of norm ≤ c over a time ε.
- Identity theorem for entire functions of two variables.
- Continuity of window averages.

## 2. Proof of Theorem W

**Step 1 — a nonzero two-time coefficient.**

- Take (j, k, m_1, m_2) from VIS-1 and an entry (a, b) such that e_a^T D0 Ā^{m_2} N_j^k P_j Ā^{m_1} C e_b ≠ 0.
- The function H(u_1, u_2) := e_a^T D0 e^{Āu_2} N_j^k P_j e^{Āu_1} C e_b is entire in (u_1, u_2). One of its Taylor coefficients is nonzero, so H ≢ 0.
- The zero set of a nonzero entire function of two variables has empty interior. So there are u_1*, u_2* > 0 with H(u_1*, u_2*) ≠ 0.

**Step 2 — windows.** Fix 0 < Δ < u_1* and put ρ := δ + u_1*.

- The input window is s ∈ [δ, δ+Δ] in plant time, i.e. v supported on [0, Δ].
- The noise "kick" ramp is [ρ, ρ+ε] for a symbolic ε > 0.
- The output window is t ∈ [ρ+ε+u_2*, ρ+ε+u_2*+Δ].

Define

- L_in := ∫_δ^{δ+Δ} e^{Ā(ρ−s)} ds;
- L_out := ∫ over the output window of e^{Ā(t−ρ−ε)} dt, which does not depend on ε.

As Δ → 0, L_in/Δ → e^{Āu_1*} and L_out/Δ → e^{Āu_2*}.

**Step 3 — the kicked kernel.** For θ ∈ R let ℓ_θ be the following continuous path with ℓ_θ(0) = 0: zero on [0, ρ], linear from 0 to θ on [ρ, ρ+ε], and θ afterwards. By the definition of Ψ_ℓ in v34:

- on [0, ρ] the generator is Ā, so Ψ(ρ, s) = e^{Ā(ρ−s)};
- on [ρ+ε, ·) the generator is e^{−A0θ} Ā e^{A0θ}, so Ψ(t, ρ+ε) = e^{−A0θ} e^{Ā(t−ρ−ε)} e^{A0θ};
- on the ramp the generator norm is at most c(θ) := sup_{|ϑ|≤|θ|} ||e^{−A0ϑ} Ā e^{A0ϑ}|| < ∞, so ||Ψ_ramp − I|| ≤ e^{ε c(θ)} − 1.

Hence, for s in the input window and t in the output window,

`k_{ℓ_θ}(t,s) = D0 e^{A0θ} Ψ(t,s) C = D0 e^{Ā(t−ρ−ε)} e^{A0θ} Ψ_ramp e^{Ā(ρ−s)} C`.

With v := e_b 1_{[0,Δ]} and φ := e_a 1_{output window},

`<φ, T_{ℓ_θ} v> = e_a^T D0 L_out e^{A0θ} Ψ_ramp L_in C e_b =: g_Δ(θ) + r_ε(θ)`,

where g_Δ(θ) := e_a^T D0 L_out e^{A0θ} L_in C e_b and |r_ε(θ)| ≤ ||D0|| ||L_out|| ||e^{A0θ}|| (e^{εc(θ)} − 1) ||L_in|| ||C||. For fixed θ, r_ε(θ) → 0 as ε → 0.

**Step 4 — unboundedness.** Expand e^{A0θ} = Σ_{j',k'} e^{μ_{j'}θ}(θ^{k'}/k'!) N_{j'}^{k'} P_{j'}. Then g_Δ is an exponential polynomial in θ.

- Its coefficient at the bad pair (μ_j, k), divided by Δ^2, tends to H(u_1*, u_2*)/k! ≠ 0 as Δ → 0.
- Fix Δ so that this coefficient is nonzero. By v36 Lemma EP, sup_θ |g_Δ(θ)| = ∞.
- Given K > 1, pick θ_K with |g_Δ(θ_K)| ≥ K, then ε_K small with |r_{ε_K}(θ_K)| ≤ 1.
- Since ||v|| = ||φ|| = Δ^{1/2},

  ||T_{ℓ_{θ_K}}|| ≥ (K − 1)/Δ,

  with T = ρ + ε_K + u_2* + Δ. Δ is fixed, so G_rob = ∞.

**Step 5 — strictness.** v31 Step 0 gives G2,∞ < ∞ = G_rob. Then v34 Theorem R item 2 gives G1,∞ > G2,∞. The upper bound √2·G2,∞ is v27 Corollary C1. ∎

**Corollaries.**

- **W1.** Commutation moves Ā^{m_2} through N_j^k P_j.
- **W2.** For A0 = σ e e^T, A0 e = σ e and A0 = 0 on e^⊥, with P_σ = e e^T and N = 0. VIS-1 needs Re μ ≠ 0, which only the σ-component has. Then D0 Ā^{m_2} e e^T Ā^{m_1} C ≠ 0 for some m_1, m_2 iff both factors are nonzero for some m_1, m_2. A rank-one product is nonzero iff both factors are.
- **W3.** As displayed in §0. A nonzero complex matrix Q has nonzero real or imaginary part, so some real unit vectors give y^T Q x ≠ 0. ∎

## 3. Meaning (value side only)

- **Generic strictness.** For every uncontrolled EMS plant whose noise matrix has an amplifying component, the printed E path-L2 optimal level equals the mean-square level only on a proper algebraic set of input/output maps.
- **Visible amplifying noise.** As soon as an amplifying noise mode is reachable and observable through Ā, the mean-square replacement is STRICTLY optimistic, at every preview.
- **Undecided class.** Only rotation-like noise (A0 diagonalizable with imaginary spectrum) remains undecided.

## 4. Process and assurance

- Written exact mathematics only, after v209 was read FIRST and the adopted inputs were read completely.
- The frozen v27–v32 are untouched. No v220 file, review or assignment was opened.
- No pinned/frozen/shared edit. No Git, deletion, publication or external model.
- All permanent findings and ZERO quarantines remain: post56, post60, postS126, the self-released v163 assessment, and the protected S242 window. HELD_C889 was never opened.
- No formal, kernel, human, configured-family, executable or novelty acceptance.
- Same18, HOLD v2, science cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 apply. This is not an early final park.

**END OF COMPLETE v37.**
