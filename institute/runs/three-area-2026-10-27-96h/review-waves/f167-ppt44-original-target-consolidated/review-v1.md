# Review v1: f167-ppt44-original-target-consolidated

- **Reviewer:** ReviewF167PPT44. This is an independent review by an agent running in the same harness as the author.
- **Clock before the first write of this file (/bin/date):** 2026-10-29T14:39:52Z (Thu Oct 29 07:39:53 PDT 2026)
- **Clock before the last in-place edit:** 2026-10-29T14:51:57Z. Earlier in-place edit: 14:49:58Z.
  - The edits aligned §7 with the v2 output: the check count, the B1 minimum slack, the triangle wording, and the B6 note.
  - They also clarified the N1 wording and the access-scope wording.
  - Nobody consumed this file before these edits.
- **Manifest:** `review-waves/f167-ppt44-original-target-consolidated/manifest-v1.json`
  - SHA-256 `17ad2a3d62c6540e6dceb802c6617df89bf296b248df05248fe3d5167c3049f0`. This matches the task value; checked at 13:54:06Z.
- **Declared input (the only one):** `physics/evidence/three-area-20261027-96h/parallel-18/ppt-schmidt44/frontier-20261028-original-target-consolidated-v1.md`
  - SHA-256 `9d14533ff5764965b05686c2e31809bfcfcc882816d97d2c98297fe126302b12`, 14214 bytes, 171 LF. All three values matched the manifest at 13:54:17Z, before I interpreted anything.
  - Read once, completely, with an exact raw read.
  - The manifest declares no errata, overlays or withdrawals.
- **Author (per manifest):** PhysicsPPT44-2. I did not contact the author.

## 0. Bottom line

**Counts:** 0 FATAL, 0 MAJOR, 0 MINOR. Six non-defect observations (O1–O6) are listed in §8.

**Claim A** (2-block-positive Z-correlated phase-covariant 4×4 operators are decomposable) is WRITTEN_SUPPORTED.
- The perfect-matching and spanning-star cases are self-contained.
- The disconnected case is conditional on Yang–Leung–Tang (YLT) Theorem 3.2, but only when a component has 3 vertices.
- I read Theorem 3.2 directly and transcribe it below. It is invoked within its hypotheses.

**Claim B** (exact rank-two minimisation for balanced-reciprocal weights, for any n) is WRITTEN_SUPPORTED.

**Explicit example (§A.5):** all displayed exact values are reproduced by my own code.

**No SN3 target solution follows.**
- The packet does not construct a 4×4 PPT state with Schmidt number ≥ 3.
- It does not prove that all 4×4 PPT states have Schmidt number ≤ 2.
- It does not claim either. Claim A is a no-go result inside one witness class: no Z-correlated phase-covariant 2-block-positive operator can be negative on a PPT state.

**Novelty was not assessed.** The candidate itself says novelty is UNCLEAR.

## 1. Imported theorem: transcription and hypothesis check

**Where I read it.** The candidate cites `arXiv:1603.03534` and the ar5iv anchor `#S3.Thmthm2`.
- I could not load ar5iv. Two read-tool attempts and one 60-second curl all timed out with 0 bytes.
- I read the arXiv-served PDF instead.
  - Watermark: "arXiv:1603.03534v1 [math-ph] 11 Mar 2016".
  - The arXiv abs page lists only `[v1] Fri, 11 Mar 2016`, so this is the only version.
  - SHA-256 `27e33b8e52c3647bb95fb6afd443a4265c4fd1468c0233ef765e154dae9e0683`, 116269 bytes. Two independent fetches gave the same hash.
- Location: Section 3, "A reduced situation in B(M₃(C), M₃(C))", page 9. Theorem 3.2 comes immediately after Lemma 3.1.

**Verbatim statement (YLT Theorem 3.2):**

> **Theorem 3.2.** *Every 2-positive or 2-copositive map φ in B(M₃(C), M₃(C)) is decomposable.*

**Definitions it relies on (YLT §1):**
- B(M_m(C), M_n(C)) is "the space of all linear maps from M_m(C) to M_n(C)".
- Definition 1.2: "A map φ is called k-positive if the map id_k ⊗ φ : M_k(M_m(C)) → M_k(M_n(C)) is positive. Similarly, a map φ is called k-copositive if the map τ_k ⊗ φ … is positive."
- "If a map is k-positive (resp. k-copositive) for every k, it is called completely positive (resp. completely copositive). A positive map is called decomposable if it can be written as the sum of a completely positive map and a completely copositive map."

**Hypotheses:**
- **(H1)** φ is a linear map M₃(C) → M₃(C).
- **(H2)** φ is 2-positive, or φ is 2-copositive.
- Nothing else is assumed: no unitality, no trace preservation, no symmetry.

**How YLT prove it (§§2–3).** This is a dependency of the import; I did not re-prove it.
- First a peel-off step: φ = ψ + κ̃_p. Here ψ is completely positive (or completely copositive), and κ̃_p is a trivial lifting of a *positive* map κ ∈ B(M₂, M₃). This is Theorem 2.7 / Corollary 2.10, with the condition 2 ≤ k < min{m, n}.
- Then Woronowicz's theorem (their reference [15]): every positive map M₂ → M₃ is decomposable.
- Lemma 3.1: a trivial lifting preserves decomposability.

**The candidate's transcription.** It reads: "every 2-positive or 2-copositive map M₃(C)→M₃(C) is a sum of a completely positive and a completely copositive map". This is exact.

**Does the invocation stay within hypotheses? Yes.** The theorem is used once, in §A.3, for a connected component C with |C| = 3.
1. The operator W_C is the restriction of W to span{|ij⟩ : i, j ∈ C} ≅ C³⊗C³. It is Hermitian and 2-block positive, because rank-≤2 coefficient matrices supported on C×C embed into the 4×4 problem with the same rank.
2. By YLT Remark 2.2, W_C = C_φ for a unique linear map φ. This gives (H1).
3. I reconstructed the identity ⟨η|(id₂⊗φ)(ξξ*)|η⟩ = ⟨v|C_φ|v⟩, where ξ = Σ_s e_s⊗w_s, η = Σ_s e_s⊗y_s and v = Σ_s w̄_s⊗y_s.
   - Every vector of Schmidt rank ≤ 2 has the form of v. So φ is 2-positive exactly when C_φ is 2-block positive.
   - This gives (H2), using only the 2-positive branch.
4. YLT then gives φ = φ₁ + φ₂, with φ₁ completely positive and φ₂ completely copositive.
   - Choi's theorem (YLT Theorem 2.3) gives C_{φ₁} ≥ 0.
   - Write τ for transposition. τ_k⊗φ₂ is positive for all k exactly when id_k⊗(φ₂∘τ) is positive for all k. This is because τ_k⊗τ is the full transpose, a bijection that preserves positivity.
   - So P := C_{φ₂∘τ} ≥ 0, and C_{φ₂} = P^{T_A} = (Pᵀ)^{T_B}, with Pᵀ ≥ 0.
   - Hence W_C = A_C + B_C^Γ, with A_C, B_C ≥ 0 and Γ the partial transpose on Bob.
5. Padding with zeros and lifting back to C⁴⊗C⁴ preserves PSD. It also commutes with Γ, because the restriction uses coordinate projectors.

My code checks the identities in steps 3 and 4 exactly: 30 random Gaussian-rational samples each, all passing (§7).

## 2. Verdict per claim

Verdict labels:
- **WS** = WRITTEN_SUPPORTED. I reconstructed the step independently and found no gap.
- **cond.** = the support is conditional on the dependency named in the same row.

| ID | Candidate location / claim | Verdict |
|---|---|---|
| D0 | Definitions. A decomposable W is nonnegative on PPT states, since Tr(B^Γρ) = Tr(Bρ^Γ). | WS |
| D1 | In local dimension ≤ 2, 2-block positive implies PSD. | WS |
| D2 | A 2-block-positive operator on C³⊗C³ is decomposable (YLT 3.2 plus Choi). | WS, cond. on YLT Theorem 3.2 (§1) |
| A1 | Setup (§A.1): phase-covariant form; a_i, d_ij ≥ 0 from product vectors; gauge invariance of the conclusion. | WS |
| A2a | Eq. (1): a_i a_j ≥ k_ij², from x\|ii⟩ + y\|jj⟩. | WS |
| A2b | Eq. (2): the matching inequality f_M(z) ≥ 0. AM–GM infimum 2q_ij z_i z_j; limits when a coefficient or z_i z_j is zero. | WS |
| A2c | Z-matrix lemma: a copositive Z-matrix is PSD. | WS (the Z sign is necessary: control N5) |
| A2d | Eq. (3): PSD pair block B_ij(c); B^Γ has correlated entry −c; residual diagonals d(1−c/q) ≥ 0. | WS |
| A3a | Graph split: every 4-vertex graph is disconnected, contains a perfect matching, or is a spanning star. | WS (all 64 graphs checked, §7) |
| A3b | Disconnected case. | WS, cond. on D2 (only when a component has 3 vertices) |
| A3c | Perfect-matching case: the residual is a Z-matrix with quadratic form f_M. | WS |
| A4 | Spanning-star Schur comparison: eqs. (4), (5), R − C ≥ 0 entrywise, R copositive Z-matrix hence PSD. | WS |
| **A** | **Claim A** overall. | **WS, cond. on YLT Theorem 3.2 (3-vertex-component subcase only)** |
| A5 | Explicit example W_*: 2-block positive, not PSD, not coPSD, rank-2 negative correlated part, explicit decomposition. | WS (exact, §4) |
| **B** | **Claim B**: the iff with m(x) in eqs. (6)–(7), for any n. | **WS** |
| B′ | Equal geometric means do not by themselves force common reciprocal weights r_i. | WS (control B5) |
| C1 | Complex-phase version of the disconnected argument. Consequence: the low graph √(d_ij d_ji) < \|H_ij\| must be connected for a 2-block-positive indecomposable operator. | WS, cond. on D2 |
| C2 | Gauge balance holds exactly when every oriented cycle has ∏(−H_ij/\|H_ij\|) = 1. Balanced patterns are excluded subject to Claim A. | WS, cond. on A |
| C3 | Frustration can be real (a triangle with positive edge product). | WS |
| C4 | Open routes and limits; the statement that no held material is imported. | Not mathematical claims. Consistent with the packet. The held-material statement is a process assertion I did not, and must not, verify (§6). |
| P1 | Li–Wu, arXiv:1704.01288v1, Theorem 2.8 description. | WS as a transcription (§5) |
| P2 | Gulati–Nechita–Park, arXiv:2509.15201v4, Example 5.8: expectations −2λ (DUC) and −2 (CDUC). | WS (exact, §5) |
| N | Novelty. | NOT ASSESSED (out of scope) |

## 3. Independent reconstruction (load-bearing steps)

**Notation.** |X⟩ = Σ_{ij} X_ij |ij⟩, and the Schmidt rank of |X⟩ equals rank X.
- Phase covariance means invariance under every diagonal U⊗Ū. With U = diag(e^{iφ_i}), the entry ⟨ij|W|kl⟩ picks up the phase e^{i(φ_i−φ_j−φ_k+φ_l)}. So it survives only if (i = j and k = l) or (i = k and j = l).
- Hence W = Σ_{i≠j} d_ij[ij] + Σ_{i,k} H_ik |ii⟩⟨kk|, and ⟨X|W|X⟩ = z*Hz + Σ_{i≠j} d_ij|X_ij|², where z = diag X.

**Gauge.** A diagonal-unitary gauge commutes with U⊗Ū and preserves Schmidt rank. Undoing it on both summands of a decomposition is legitimate, because (V⊗V′)B^Γ(V⊗V′)* = ((V⊗V̄′)B(V⊗V̄′)*)^Γ.

**Eq. (2), the matching inequality.**
- Take M = {ij, kl} and z ≥ 0. Let X = diag(z) plus the off-diagonals (u, z_i z_j/u) inside each matched block. Each block has determinant 0, so rank X ≤ 2.
- Off-diagonal cost of block ij: d_ij u² + d_ji z_i² z_j²/u² ≥ 2q_ij z_i z_j, with equality at u⁴ = d_ji z_i² z_j²/d_ij.
- The correlated part with real z ≥ 0 is Σ a_i z_i² − 2Σ k_ij z_i z_j. This gives (2).
- Zero coefficients are handled by finite-u limits, as the candidate states.

**Eq. (3).** B_ij(c) = (c/q)[[d_ij, −q], [−q, d_ji]] has determinant 0 and nonnegative trace, so it is PSD. Γ maps |ij⟩⟨ji| to |ii⟩⟨jj|, so B^Γ has correlated entry −c.

**Graph split.**
- Pairwise-intersecting edges form either a star or a triangle. A triangle leaves one vertex isolated.
- Disconnected graphs have components of size ≤ 3.
- Exhaustive check: of the 64 graphs, 16 are disconnected with a 3-vertex component, 10 are disconnected with components of size ≤ 2, 34 are connected with a perfect matching, and 4 are spanning stars. Nothing else occurs.

**Disconnected case.**
- For every cross pair, c = k_ij ≤ q_ij. The residual is ⊕_C W_C plus a nonnegative diagonal on the cross pairs, and there are no remaining cross entries.
- |C| ≤ 2: W_C is PSD by D1.
- |C| = 3: W_C is decomposable by D2.

**Matching case.**
- With c = q on the two low matched edges, the residual correlated block has diagonal a, matched entries q − k < 0, and unmatched entries −k ≤ 0. It is a Z-matrix whose form on z ≥ 0 equals f_M(z) ≥ 0, so it is PSD.
- The remaining diagonals are ≥ 0.

**Star case (center 0, leaves 1, 2, 3).**
- In a spanning star, every leaf pair is a non-edge, so s_ij ≥ 0. Also t_i > q_{0i} ≥ 0 ⇒ b_i ∈ (0, t_i], and (1) ⇒ a_0 > 0 and a_i ≥ t_i²/a_0.
- With c_{0i} = q_{0i} and c_ij = min(q_ij, k_ij + b_i b_j/a_0), the residual correlated block is [[a_0, −bᵀ], [−b, L]], where L_ij = min(s_ij, b_i b_j/a_0). The Schur complement is exactly (4), a Z-matrix with diagonal ≥ a_i − t_i²/a_0 ≥ 0.
- Branch where some pair jk has s_jk ≤ t_j t_k/a_0: substitute z_0 = (b_i z_i + t_j z_j + t_k z_k)/a_0 ≥ 0 into f_M with M = {0i, jk}. Completing the square gives the form with matrix C of (5), and C_jk ≤ 0.
- Entrywise comparison:
  - R_ii = C_ii.
  - R_jj − C_jj = (t_j² − b_j²)/a_0 ≥ 0.
  - Mixed entries: R_ij − C_ij ≥ k_ij ≥ 0, because h_ij ≤ b_i b_j/a_0 ≤ b_i t_j/a_0 (this uses s_ij ≥ 0).
  - The jk entry: two sub-cases, both ≥ 0.
- So zᵀRz ≥ zᵀCz ≥ 0 on z ≥ 0. A copositive Z-matrix is PSD, so R ⪰ 0, and with a_0 > 0 the block is PSD.
- Otherwise every h_ij = 0 and R is a nonnegative diagonal matrix.

I found no gap in any case.

**Claim B.**
- Put Y = TXT⁻¹ with T = diag(√r_i). Then rank and diagonal are unchanged, and Σ d_ij|X_ij|² = qΣ_{i≠j}|Y_ij|².
- Lower bound:
  - s₁ = ‖Y‖_op ≥ |Y_ii|, so s₁ ≥ L.
  - Let D = diag(e^{−i arg z_i}). Then S = tr(DY) ≤ ‖Y‖₁ = s₁ + s₂.
  - Minimising s₁² + s₂² subject to s₁ ≥ L, s₁ + s₂ ≥ S and s₂ ≥ 0 gives exactly (6).
- Attainment:
  - Case L ≥ S/2: G = L e eᵀ + w wᵀ with disjoint supports, so ‖G‖_F² = L² + (S−L)².
  - Case L ≤ S/2: closing a polygon gives VᵀV = (S/2)I, so ‖G‖_F² = tr((VᵀV)²) = S²/2.
  - Multiplying by a diagonal phase matrix and conjugating back by T preserves all of this.
- Since q ≥ 0, the minimum over rank-≤2 X with diagonal z is z*Hz + q(m(|z|) − Σ|z_i|²). Therefore 2-block positivity holds exactly when (7) holds.
- The examples m(1,1,1,1) = 8 and m(3,1,1,0) = 13, and their disjoint-block attainments, are correct.

**Section C.**
- **Complex cross blocks.** Use B_ij = (c/q)[[d_ij, −q·ph], [−q·ph̄, d_ji]] with c = |H_ij| and ph = −H_ij/|H_ij|. This is PSD with determinant 0, and B^Γ cancels H_ij exactly.
- **Gauge solvability.** The gauge D H D* multiplies H_ij by e^{i(α_i−α_j)}. Making every off-diagonal entry nonpositive is possible exactly when every cycle in the support has product ∏(−H_ij/|H_ij|) = 1. These products are gauge invariant.

## 4. Explicit example (§A.5): my exact values

**Parameters**, read back from my own 16×16 build of W_*:
- a = (251/100, 261/100, 68/25, 141/50).
- k₀₁ = 101/100; every other k_ij = 1.
- d₀ᵢ = dᵢ₀ = 13/25; d₁₂ = d₂₁ = 107/100; d₁₃ = d₃₁ = 101/50; d₂₃ = d₃₂ = 151/50. Hence q = d.

**Graph.** The low graph is {01, 02, 03}, a spanning star centred at 0.

**Star quantities:**
- t = (101/100, 1, 1), b = (49/100, 12/25, 12/25).
- s₁₂ = 7/100, s₁₃ = 51/50, s₂₃ = 101/50.
- Leaf coefficients: c₁₂ = 107/100 (= q₁₂; the min is binding), c₁₃ = 6863/6275, c₂₃ = 6851/6275.

**Decomposition:**
- A = W_* − B^Γ is PSD of rank 8. B is PSD of rank 6.
- W_* = A + B^Γ holds exactly.
- Every PSD verdict carries an exact LDLᵀ certificate that is re-multiplied and compared entry by entry.

**R and C:**
- h₁₂ = 119/5020 (the candidate's "deficit"); h₁₃ = h₂₃ = 0.
- R = [[6311/2510, −119/5020, 0], [−119/5020, 16492/6275, 0], [0, 0, 34239/12550]], which matches eq. (4).
- The branch pair is jk = 12, with i = 3.
- C (leaf order 1, 2, 3) = [[5531/2510, −8343/25100, −7487/6275], [−8343/25100, 14568/6275, −299/251], [−7487/6275, −299/251, 34239/12550]].
- R − C ≥ 0 entrywise. R and C are both PSD of rank 3.
- The identity f_M(z₀*(z), z) = zᵀCz holds at 25 random rational points.

**Negative tests and structure:**
- ⟨ω|W_*|ω⟩ = −34/25 and ⟨02+20|W_*^Γ|02+20⟩ = −24/25, as displayed in the candidate.
- LDL witnesses independently confirm that W_* is not PSD and W_*^Γ is not PSD.
- W_*'s 2-block positivity is supported as follows:
  - The identity W₀ = ¼(2I−[ω]) + ¾(4Σ[ii]−[ω]) holds exactly.
  - 4Σ[ii]−[ω] is PSD (rank 3), and 2I−[v] is PSD.
  - 2I−[ω] is *not* PSD, as expected. Its 2-block positivity rests on the stated inequality |tr X|² ≤ 2‖X‖_F² for rank X ≤ 2, which I re-derived via ‖X‖₁ ≤ √2‖X‖_F.
- [ω] + [v]/100 has rank 2, so this is not the single-projector subcase.
- W_* is invariant under U⊗Ū for rational-phase U = diag(1, (3+4i)/5, (5+12i)/13, (8+15i)/17), and not invariant under U⊗U.
- These values agree with the candidate's reported checker outcomes: ranks 8 and 6, deficit 119/5020, R and C PSD, the two negative tests. That agreement is not used as evidence (§6).

## 5. Prior-art triage: transcription checks only

**Li–Wu, arXiv:1704.01288v1, Theorem 2.8.** The source states:
- Hypotheses: a, c₁, …, c_n are positive real numbers, and l_min(σ) ≥ 2. The proof notes this means "σ has no fixed point".
- Conclusion: Θ^{(n,σ)}[a; c] is completely positive ⇔ 2-positive ⇔ a ≥ n. Θ is a D-type map (eq. 1.1).

The candidate's description is accurate. My exact checks for n = 4 and σ = a 4-cycle:
- The Choi matrix lies in Claim A's class: Z-correlated, with the single projector [ω].
- It is PSD at a = 4 and not PSD at a = 7/2.
- Run through Claim A's recipe, a = 4 is DECOMPOSED and a = 7/2 is REFUTED by an explicit rank-2 vector. This is consistent with Li–Wu's (ii)⇒(iii).

**Gulati–Nechita–Park, arXiv:2509.15201v4, Example 5.8.** The source states:
- H̃ = |v⟩⟨v| + 2(E₀₃ + E₃₀) with v = (1, −1, 1, −1). I verified this transcription exactly.
- Pair (I₄ + λJ̊₄, H̃ − λJ̊₄), stated to be in PCOP₄ \ PDEC₄ for λ ∈ [1/2, 1).

Using their Proposition 2.12 Choi forms, for λ ∈ {1/2, 3/4, 99/100}:
- DUC: ⟨00+11| X^{CLDUI} |00+11⟩ = −2λ.
- CDUC: ⟨01+10| X^{LDUI} |01+10⟩ = −2.

Both values are exactly as the candidate states. GNP claim only positivity and indecomposability, not 2-positivity. The candidate's remark is therefore a correct relevance note, not a correction of GNP (observation O3).

## 6. Exact dependency list

**Import (I1).** Yang–Leung–Tang, arXiv:1603.03534v1, §3, Theorem 3.2, transcribed in §1.
- Its own dependencies: YLT Theorem 2.7, Corollary 2.10, Lemmas 2.5 and 3.1; Woronowicz 1976 (positive maps M₂→M₃ are decomposable); Choi 1975.
- Used only in the 3-vertex-component subcase of Claim A, and in C1.

**Standard facts I reconstructed** (no other imports):
- The k-positive ⇔ k-block-positive Choi correspondence.
- C_{φ∘τ} = C_φ^{T_A} = ((C_φ)ᵀ)^{T_B}.
- The Schur-complement PSD criterion with a positive pivot.
- Trace-norm duality, and ‖Y‖_op ≥ |Y_ii|.
- The polygon-closure criterion: the largest length is at most the sum of the others.
- AM–GM.
- Cycle-product invariance under diagonal gauge.

**Conditional premises of Claim A:**
- Local dimension exactly 4.
- W is invariant under diagonal U⊗Ū.
- One diagonal-unitary gauge makes every correlated off-diagonal entry real and ≤ 0.
- W is 2-block positive.

**Claim B premises:** d_ij = q r_i/r_j with q ≥ 0, r_i > 0, and arbitrary Hermitian H.

**Pinned data:** none. There are no certificates, solver outputs or held payloads; only the displayed rational parameters of W_*.

**Not used as evidence:**
- The candidate's checker `frontier-20261028-Z-correlated-star-check.py`. I hashed it only; I did not read or execute it. At the inferred sibling path its SHA-256 is `1b5d0bcc…3b7af`, equal to the citation.
- The candidate's "checked" statements.
- The candidate's process assertion in §C ("no … held … consumer is imported"). Checking it would require held material, which I did not and must not open.

## 7. Reviewer controls with receipts

**Files** (all in this directory):

| File | SHA-256 | Bytes |
|---|---|---|
| `f167r-controls-v1.py` | `5e356d148140189578589f8e941b9b6da881655d5c0428033d6aec83624efd4f` | 47456 |
| `f167r-controls-v1.out.json` | `18d394033b37b92179200dd372dc9e0a6209438b907e0375cef3f8c1ac6608b3` | 10663 |
| `f167r-controls-v2.py` | `f5c843269551013738591b0745db420633b05be1a0bf26ae6ac8bbd3cc933c52` | 52351 |
| `f167r-controls-v2.out.json` | `8fd5e1fa03a0cb4566b18760c9228e0650a5ee59e97218fff7b29148e73a11f0` | 11381 |
| `f167r-receipts-v1.txt` | `5c7c72afdc23e2ea271e73f74cb66991837674251c1fd8afdc96c5f0621b7e96` | 4279 |

The receipts file holds every clock, URL, hash and run line.

**Runs.** Command: `PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 <script> <out.json>`, run from this directory with Python 3.14.3.
- v1: 2026-10-29T14:25:05Z → 14:25:08Z, exit 0, `all_pass: true`.
- v2: 14:30:12Z → 14:30:17Z, exit 0, `all_pass: true`, 61 named checks (v1 had 58).
- v2 is a byte copy of v1 plus two boundary-biased generators, a PSD/coPSD tally, and the Choi identities. Both outputs are retained.

**Method.**
- Exact arithmetic throughout: Fractions and Gaussian rationals.
- PSD verdicts come from symmetric-pivoted LDLᵀ. The certificate Σ d_p l_p l_pᵀ is re-multiplied and compared entry by entry.
- Non-PSD verdicts come with an explicit vector of negative value. Complex Hermitian matrices are handled through the real embedding [[Re, −Im], [Im, Re]].

**Positive controls (v2):**
- **§4 example.** Every value listed in §4.
- **Graph split.** Exhaustive over all 64 graphs.
- **Random falsification of Claim A** (seed 20261029; 1750 instances from six generators).
  - On every instance outside the YLT subcase, the candidate's recipe either decomposes W, or W is refuted by an explicit rank-≤2 coefficient matrix with ⟨X|W|X⟩ < 0.
    - Decomposed instances carry exact PSD certificates for A and B, and W = A + B^Γ holds exactly.
    - For refutations, the vector comes from the Z-matrix |x| trick, then z₀*(z), then the matching blocks, so the predicted contrapositive is exercised.
  - Route outcomes:

    | Route | DECOMPOSED | REFUTED |
    |---|---|---|
    | Disconnected (components ≤ 2) | 142 | — |
    | Matching | 38 | 375 |
    | Star | 95 | 333 |

  - Pre-screen refutations: 820 by the 2×2 test (1) and 5 by a product vector.
  - **0** instances fell in NEITHER, ANOMALY or SPLIT_VIOLATION.
  - In 264 decomposed instances, W was neither PSD nor coPSD in 225. So both summands are usually needed.
  - Every instance also checked: eq. (4), R − C ≥ 0, C_jk ≤ 0, and the identities f_M(z₀*, z) = zᵀCz and f_M = zᵀA_corr z.
  - 31 instances fell in the 3-vertex-component (YLT) subcase. They were only counted, not machine-checked.
- **Section C example (complex phases).**
  - Setup: components {0,1} and {2,3}; W is neither PSD nor coPSD; the support triangle 0-1-2 of H is frustrated.
  - With phase-cancelling cross blocks, A ⪰ 0 (rank 10) and B ⪰ 0 (rank 4), and W = A + B^Γ holds exactly.
  - The cycle product is gauge invariant. No ±1 gauge makes an all-(+1) real triangle nonpositive.
- **Claim B checks.**
  - 3000 exact real rank-2 tests of ‖Y‖_F² ≥ m(|diag Y|); minimum slack 0 in v2 (some samples attain the bound) and 1/36 in v1.
  - 250 exact weighted instances: the T-similarity identity holds, and the bound (7) is respected.
  - Exact attainment in five configurations, each with rational unit phases, and including an equality check of the weighted value against the LHS of (7):
    - x = (1,1,1,1), both as disjoint blocks and as a rotated polygon;
    - x = (3,1,1,0);
    - the polygon x = (1, 65/32, 65/32), whose G has no zero off-diagonal entry;
    - x = (16,4,1,9), in the L ≥ S/2 branch.
- **Choi identities.** 30 samples each, all exact (§1).
- **Prior-art values.** As listed in §5.

**Negative controls.** Each must fail, and the failure must have the stated cause.
- **N1.** W_* is not PSD and W_*^Γ is not PSD. My LDL code finds its own witness vectors, which differ from the candidate's displayed vectors. The displayed vectors themselves evaluate to −34/25 and −24/25 (§4).
- **N2.** The covariance test can fail: W_* is not invariant under U⊗U.
- **N3.** Drop the `min` in c₁₂. Then c₁₂ > q₁₂, the residual |12⟩ diagonal becomes −119/5020, and A is no longer PSD, while B stays PSD. So the min clause is necessary.
- **N4.** A hand-made star instance passes every 2×2 screen, yet the recipe's R is not PSD.
  - Setup: a = 1, k₀ᵢ = 1, d₀ᵢ = dᵢ₀ = 0, k_leaf = 0, d_leaf = 1/2.
  - The explicit rank-2 matrix X = diag(2,1,1,0) + E₁₂ + E₂₁ gives ⟨X|W|X⟩ = −1. So the failure is a genuine loss of 2-block positivity, as the theorem predicts.
- **N5.** The copositive non-Z matrix [[0,1],[1,0]] is not PSD (x = (1,−1) gives −2). So the Z sign hypothesis is essential.
- **N6.** 2I−[ω] is not PSD, and the rank-3 matrix X = diag(1,1,1,0) gives −3. So the rank-2 restriction is essential.
- **N7.** In Claim B, rank-4 and rank-3 identities beat m (4 < 8 and 3 < 9/2). So the rank constraint is essential.
- **N8.** In the complex cross block, the wrong phase sign leaves 2H_ij behind and a non-PSD residual.
- **N9.** The Li–Wu Choi matrix at a = 7/2 is not PSD and is refuted through Claim A's machinery.

**Supplementary, not exact (B6).** 2000 complex rank-2 samples at 50 digits with mpmath; minimum relative slack 0.126.

v1 and v2 report the same B6 minimum, and this is not a stale file. The likely cause (an inference I have not proven): B6's draws depend on the data, because each sample's size is chosen at random, so the shifted random stream re-synchronised onto the same samples.

An unsaved inline diagnostic used the same B6 code with fresh streams at offsets 0, 1, 1000 and 123457. It gave 0.0826 for the first three and 0.126 for the last. This shows the minimum does depend on the stream state. The two B6 runs should not be counted as independent samples.

**Limits of these controls.**
- Sampling is not proof. The universal statements rest on the written reconstruction in §3.
- The random search cannot exclude a counterexample.
- No solver was used, so no "UNKNOWN" or budget-hit result could be read as an exclusion.

## 8. Observations (non-defects) and deviations

**Observations:**
- **O1.** The ar5iv anchor could not be loaded from this environment. Theorem 3.2's number and statement were confirmed on the arXiv v1 PDF. A citation of the form "arXiv:1603.03534v1, §3, Theorem 3.2" would not depend on the HTML renderer.
- **O2.** The checker script is cited by filename only, without a directory. I found it at the inferred sibling path, and its hash matched (hash only).
- **O3.** GNP do not claim 2-positivity for Example 5.8. The candidate's sentence is accurate, and its next sentence makes this clear. It should not be read as an erratum to GNP.
- **O4.** Claim A depends on YLT only in the 3-vertex-component subcase. The matching and star cases are self-contained.
- **O5.** The §C process assertion about held material was not verified (see §6).
- **O6.** Li–Wu's theorem covers all n. The candidate's phrase "narrower special class" is accurate only within the 4×4 setting.

**Deviations:**
- **Public sources.** Network reads of public sources only: the arXiv abs page, the three named arXiv PDFs, and failed ar5iv attempts. Methods were the read tool, curl and urllib. PDFs were not saved.
- **Outside-directory access.** One hash-only access to the author's checker outside my directory. It was not read and not executed.
- **Script versions.** Two control-script versions were run (v1, then v2). Both outputs are kept and nothing was overwritten.
- **Unsaved inline commands.** I also ran inline Python one-offs that are not saved as artifacts: JSON inspection of my own outputs, the B6 stream-offset diagnostic, and the urllib fetches recorded in the receipts.
- **File permissions.** The write tool automatically set the executable bit on `f167r-controls-v1.py`, and `cp` carried it to v2.
- **Unrelated notices.** During the review I received two status-only notices from Main, about f162 and f161 holds. This review never opened f161 or f162 material.
- **Scope of access.**
  - Run tree: I read only this wave's manifest and my own files. I did not read the manifest's authority file.
  - Outside the run tree: only the declared input, the hash of the cited checker, and the named public sources.
- **Absent:**
  - temp directories and pycache (`PYTHONDONTWRITEBYTECODE=1`, no local imports);
  - Git;
  - web_search;
  - external models or paid APIs;
  - contact with the author;
  - held, ZERO or quarantined payloads;
  - deletion, publication, infrastructure changes;
  - unrelated builds, linters or tests.

**What this review is not.** It was done in the same harness as the author. It is not a human review, not a review by an independent model family, not formal or kernel-checked verification, and not a novelty assessment. Author "PASS" or "checked" statements were not used as evidence.

## 9. Summary

I verified the declared input and read Yang–Leung–Tang Theorem 3.2 directly on the arXiv v1 PDF.
- The theorem reads "Every 2-positive or 2-copositive map φ in B(M₃(C), M₃(C)) is decomposable".
- The candidate applies it only to the 2-block-positive restriction of W to a 3-vertex component of the low graph. Through the Choi correspondence, which I reconstructed and checked exactly, that is within the theorem's hypotheses.

I independently reconstructed every load-bearing step of Claim A:
- the 2×2 bound;
- the matching inequality;
- the Z-matrix lemma;
- the PSD pair blocks;
- the exhaustive graph split;
- the disconnected, perfect-matching and spanning-star cases, including the Schur comparison R ≥ C entrywise.

I found no gap. Exact controls confirm the explicit example:
- A of rank 8 and B of rank 6, with W_* = A + B^Γ;
- deficit 119/5020;
- R and C both PSD;
- ⟨ω|W_*|ω⟩ = −34/25 and ⟨02+20|W_*^Γ|02+20⟩ = −24/25.

A 1750-instance randomized exact falsification search found no instance where the recipe fails without an explicit rank-≤2 violation of 2-block positivity. Claim B's equivalence is correct for any n, including exact attainment of m(x) in both branches. The Section C consequences and the two prior-art transcriptions are accurate.

I report 0 FATAL, 0 MAJOR and 0 MINOR findings. Claim A's support is conditional on the YLT import in its 3-vertex subcase. Novelty is not assessed.

No SN3 target solution follows. The packet neither constructs a 4×4 PPT state of Schmidt number ≥ 3 nor proves that none exists, and it does not claim to. Claim A only rules out Z-correlated phase-covariant witnesses. Frustrated and non-phase-covariant routes remain open, as the candidate states.
