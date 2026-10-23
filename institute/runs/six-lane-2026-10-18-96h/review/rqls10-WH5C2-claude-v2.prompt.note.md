# Hostile review: RQLS10 phys-2 W8 slice, `WH_5 ⊗ C^2` orbit ansatz

**Verdict:** the mathematics is **VERIFIED inside (H)**. Counts: **FATAL 0 · MAJOR 0 · MINOR 6.**

- The outcome class UNRESOLVED is correct.
- Corollary 14 is unconditional within (H) for every cardinality. Its third clause holds only as amended by E2.
- Neither the package nor this review gives a witness, an ansatz-wide no-go (for any cardinality or for maximal cardinality), or any statement about unrestricted 1-RQLS(10).

**Files and reading order.**
- Aliases: `01` = `…/wh5-c2-written/01-wh5-c2-exact-system-v1.md`, `E1/E2` = erratum-1 items, `JSON` = `02-import-interface-map-v1.json`, `PE` = `review/rqls10-WH5C2-parent-erratum-v1.md`.
- Applied in the order 01 → erratum-1 → PE, with PE governing.
- I did not recompute hashes, the byte count (JSON LF11) or timestamps, because the instruction was no tools. This verdict applies to the text as pasted.

## Claim-by-claim (each re-derived, not taken from metadata)

**Thm 1 (LF39–59): VERIFIED; both directions hold.**
- **Rows.** After applying X^{−i1}⊗I, the Gram entries are tr(X_r^* Z^k X_s) = Σ_t ζ^{kt} h(t). By DFT inversion, "= δ_{k0}δ_{rs} for all k" holds iff h ≡ δ_{rs}/5. The pair {(i2,0),(i2,1)} is in M_Z, and nothing depends on i1.
- **Columns.** Use X^iZ^j = ζ^{−ij}Z^jX^i and X^k = Σ_m ζ^{−mk} f_m f_m^*. The pair {(0,j2),(1,j2)} is in M_X.
- **Transversals.** Use X^iZ^{−i} = κ_i(XZ^{−1})^i, XZ^{−1}g_m = ζ^{3−m}g_m and g_m^*Z^{s1} = g_{m−s1}^*. s2 = 0 gives {00,11}; s2 = 1 gives {01,10}.
- All phases involved are unimodular.
- 120 = 15·(4 + 2·2) is a count of equations, not a rank. No rank is claimed.

**Lem 2: VERIFIED.**
- √5[v^*X_r; v^*X_s] is square with orthonormal rows, so it is unitary.
- Summing over v ∈ β_b gives G_r + G_s = I for all six pairs. Hence G_r = I/2.
- Flatness ⇔ (R1) follows from v^*P_r v = 2|v^*X_r|².

**Thm 3: VERIFIED.**
- (a) Z^{−j1}X^aZ^{j1'} = ζ^{−a·j1} W_{(a, j1'−j1)}.
- (b) Equality in Cauchy–Schwarz gives W_wX_r = μX_r. Since X_r has rank 2 (Lem 2), this puts two independent vectors in one eigenspace. That contradicts Lem 9(ii) for w ≠ 0.
- (c) W_{w'}W_w^{−1} ∝ W_{w'−w}, and w' ↦ w'−w is a bijection. So two orbits' ray sets are equal or disjoint, and the ray count is 25 × (number of classes).
- (d) Each couple type gives forced orthogonality on its line:
  - M_Z: same row, w = (0,·).
  - M_X: same column, w = (·,0).
  - M_T: i2+j2 ≡ i2'+j2' (mod 2) and i1+j1 = i1'+j1', so w = (a,−a).
- (e) τ vanishes on L_{b(r,s)}. So maximality ⇔ 6·20 = 120 strict inequations. W_{−w} ∝ W_w^* gives |τ_sr(−w)| = |τ_rs(w)|.

**Thm 4: VERIFIED.**
- Facts (i)–(iv):
  - (i) K_b D K_b = D^*.
  - (ii) ⟨v, DK_b y⟩ = λ_v · conj⟨v,y⟩.
  - (iii) conj(ρ)J = (−ρ̄₂, ρ̄₁) spans the complement of ρ.
  - (iv) needs R' to be involutive, which holds at every use.
- Uniqueness holds because conj(v^*V_r)J ≠ 0 (its norm² is 2/5).
- A_{s→r} = −A_{r→s} follows from A V_s = V_r J, J^{−1} = −J, and −A ∈ Anti_b.

**Thm 5: VERIFIED in both directions, including all six coordinate forms at LF125–126.**
- **(⇒)** The projectors are APA etc., by (iv). (O) is exactly (R2) for {10,11}∈M_Z, {01,11}∈M_X and {01,10}∈M_T.
- **(⇐)** ⟨e,APAe⟩ = conj⟨Ae,PAe⟩ = ⟨e,Pe⟩ when Ae = λ_e e. This holds for any phase convention on β_b.
- **Coordinates.**
  - K_X = ΠK, because Σ f_m f_m^T = Π.
  - K_T = Q²ΠK, because (Σ g_m g_m^T)_{tt'} = ζ^{4t²}δ_{t',−t}. Hence C = QC_TQ^*·Q²ΠK = QC_TQΠK.
  - Using conj(C) = ΠC^*Π for circulant C, ΠQΠ = Q and conj(Q) = Q^*, each form checks. For example, CPC = M P̄ M̄ with M̄ = Q^*ΠC_T^*Q^*, which gives QC_TQ(ΠP̄Π)Q^*C_T^*Q^*.
- By Theorem 4 uniqueness, solutions correspond bijectively to tuples (P; A,B,C; V) with VV^* = P.

**Thm 6: VERIFIED.**
- Each K4 triangle has one edge in each M_b.
- V_r = ΘV_rJ³ = −ΘV_rJ, so ΘV_r = V_rJ and Θ²V_r = −V_r.
- Orientation does not matter.

**Lem 7: VERIFIED.**
- ⟨y,Θy⟩ = ⟨Θ²y,Θy⟩ = −⟨y,Θy⟩, so ⟨y,Θy⟩ = 0.
- Induction on E₋₁ shows it has even dimension. Non-real eigenvalues pair off because Θ is bijective. Hence dim E₊₁ ≡ n (mod 2).

**Cor 8: VERIFIED.**
- Re-derived identities:
  - QXQ^* = ζ²XZ^{−1}, since ζ^{2(t+1)²−2t²} = ζ^{4t+2}.
  - ΠXΠ = X^{−1}, ΠZΠ = Z^{−1}, ΠQ = QΠ.
  - conj(X) = X, conj(Z) = Z^{−1}.
- The N-factors collapse to Q^{±2}. The sign is minus exactly when the T-map is the middle factor.
- Θ² = M M̄ = γW_{w₀}.
  - If w₀ ≠ 0, the spectrum is simple.
  - If w₀ = 0, Lem 7 forces γ = 1, so E₋₁ = 0.

**Lem 9: VERIFIED.**
- (i) Completing the square works because 2a and 4a are units.
- (ii) The text's s' equals −s. The argument also uses that an eigenvalue exists.
- (iii) 3(k'−k) ≢ 0 for k ≠ k'.
- (iv) X^cψ^k_m = ζ^{3kc²−mc} ψ^k_{m−6kc}, and 6 ≡ 1.
- (v) The symplectic product is nonzero off L_b, which gives a 5-cycle.

**Lem 10: VERIFIED.**
- c₀ = R(1)/5 and c₄ = ζ²R_η(1)/5.
- With Fourier support {1,2,3}, |u_t|² has frequencies −2,…,2. These are pairwise distinct mod 5 (no wrap-around), which gives c₁c̄₃ = 0 and c₁c̄₂ + c₂c̄₃ = 0. So exactly one c_f is nonzero.
- Then γ⁵ = 1 and t(t−1)/2 ≡ 3t(t−1), which gives u = ε₀ψ^f_{g−3f}.
- The proof uses only unbiasedness to β_Z plus two lag-one sums. No classification of vectors unbiased to β_Z and β_X is used.

**Cor 11: VERIFIED as stated.**
- (a) The complementary vector y is forced to be unbiased to all three bases, so y ∝ ψ^{k'}. Orthogonality then forces k' = k.
- (b) P = uu^* + (W_wu)(W_wu)^* needs ⟨u,W_wu⟩ = 0, which LF204 assumes.
  - If w ∉ L_b, then H(v) + H(σv) = 2/5. Since σ² is a 5-cycle, H ≡ 1/5.

**Prop 12: VERIFIED.**
- K_Zψ^k_m = ψ^{−k}_{−m}, K_Xψ^k_m = ψ^{−k}_m, and K_Tψ^k_m = ψ^{3−k}_m (because 3(3−k) ≡ 4−3k).
- The shift coefficients 1, −κ, −(1+κ) are units wherever they are used.
- u = Dψ^κ_n is orthogonal to Y_b u. So Cor 11(b) is applied strictly within its hypothesis.

**Thm 13 (with E1): VERIFIED.**
- **Step 1 (slopes).** β_X: (m'−m)/(6k). β_T: (m'−m)/(2(3k−2)), with 3k−2 ∈ {1,4,2}. p_r(n) ≠ 0 because |G(a)| = √5.
- **Step 2.** If a_r ≠ ±a_s, the four frequencies are distinct, so U_rU_s^* = 0, which is impossible. If a_r = ±a_s, U_rU_s^* is monomial with ratio in −μ₅.
- **Step 3.** ratio(MN) = ratio(M)·ratio(N)^{±1}. So the product of three such factors has ratio in −μ₅, which does not contain 1.

**Cor 14 (with E2): VERIFIED, and unconditional within (H) for any cardinality.**
- The proof chain is (R1), (R2), Lem 2, Thm 4, Lem 9–10, Cor 11, Prop 12, Thm 13.
- It never uses ray distinctness, Haagerup, Chebotarev, or float data.
- Clause 3 without "u ⊥ W_w u" is unproved (though not refuted), so E2 is required.

**§9 system (LF260–269) under PE: VERIFIED.**
- P1–P3 ⇔ (H). P1's "equivalently" holds given flatness, by Cor 11(a).
- P1–P4 ⇔ (H) with 100 distinct rays. The wording "any V" needs MINOR-1.

**Errata.**
- E1 is correct and sufficient.
- E2 is correct: the added condition is exactly Cor 11(b)'s hypothesis, and Prop 12 (LF221–222) already satisfies it.
- PE is correct and fixes JSON LF44/LF47 and 01 LF258. Its "LF251–252 where applicable" leaves a residual issue (MINOR-3).

**Conventions** (K/K_X/K_T, Π, Q, J with J^{−1} = −J and R(YJ) = (RY)J, couples as same i2 / same j2 / same i2+j2 mod 2): all consistent. Anti_b does not depend on the phase convention for β_b.

**Imports.**
- I1 is used in Thm 1, Lem 9(i), Lem 10 and Thm 13.
- I2 is used for Cauchy–Schwarz (Thm 3), the spectral theorem (Lem 7 and Lem 9(ii)) and antiunitary algebra.
- No step silently needs Haagerup, because Lem 10 bypasses it by using β_T.
- No step needs Chebotarev, because the only non-vanishing used is a Gauss-sum modulus.
- Float data appears only at LF255–256 and LF273, labelled as context and not premises.
- The forward references (Thm 3 → Lem 9) are not circular.

**Attacks tried, all failed:**
- Lem 10 against two-level Legendre sequences e^{iθ(t|5)}: R(1) = 0 forces cos θ = (−1±√5)/4. That yields ζ^{±t²} and ζ^{±2t²}, i.e. ψ², ψ³, ψ¹, and ψ⁴ 

∈ β_T, which c₄ ≠ 0 correctly excludes. This is consistent with the lemma.
- **Thm 13, Step 3:** a diagonal product formed from two antidiagonal factors still has ratio in −μ₅, so it cannot equal I.
- **Prop 12 at κ = 0 (b = T, k = 3) and κ = 4 (b = Z, k = 1):** here K_bS_r is a non-flat β_X- or β_T-pair plane. The shift coefficients −1 and 1 are still units, and Cor 11(b) is applied to the flat S_s, not to K_bS_r.
- **Cor 11(b) without orthogonality:** the step P = uu^* + (W_wu)(W_wu)^* fails, so E2 is necessary.

## Findings (exact lines, minimal repairs)

**MINOR-1: V-independence is asserted but not proved.**
- **Where:** 01 LF136–137 (Remark 1). It is used at LF268–269 (P4, "any V") and in JSON LF28 and LF31.
- **Problem:** P4's "any V" depends on invariance under V → VU, which is stated without proof. The statement is true.
- **Repair (append to LF137):** "Proof: A(VU) = (AV)Ū, and ŪJ = conj(det U)·JU for U ∈ U(2). So V ↦ VU sends X₀₀ ↦ X₀₀U and X_r ↦ conj(det U)·X_rU for r ≠ 00. Every cell vector is therefore multiplied by the fixed unitary I₅ ⊗ U^T, up to a unimodular scalar. Hence (H), (F), (O) and every |τ_rs(w)| are unchanged."
- **JSON LF31:** replace "changes nothing" with "multiplies every cell vector by I₅ ⊗ U^T up to phases; (F), (O) and P4 are unchanged".
- **Zero-proof alternative:** write "for some V" in P4. That version follows directly from the bijection in Thm 5.

**MINOR-2: summaries overstate Cor 8.**
- **Where:** 01 LF13–14 and LF252–253, relative to Cor 8 at LF156–158.
- **Problem:** Cor 8 excludes only triangles whose three couple maps are *all* of WH type. One or two WH-type maps in a triangle are not excluded.
- **Repair at LF13–14:** replace "…excluding Weyl-Heisenberg-type couple maps" with "…excluding every K4 triangle whose three couple maps are all of Weyl–Heisenberg (incl. scalar) type".
- **Repair at LF252–253:** replace with "triangles all three of whose couple maps are of Weyl–Heisenberg or scalar type (excluded by Corollary 8; individual WH-type couple maps are not excluded)".
- LF254 and LF258 are already correct.

**MINOR-3: undefined plane family left after PE.**
- **Where:** 01 LF251–252, "planes spanned by WH or complementary-basis vectors (excluded by Corollary 14)".
- **Problem:** "WH vectors" is undefined, and PE's "where applicable" does not say which reading is meant.
- **Repair:** replace the phrase with the three cases below.
  - Planes containing a vector of β_Z ∪ β_X ∪ β_T are never flat, since v^*Pv = 1 ≠ 2/5.
  - Planes containing a complementary-basis vector ψ^k_m with k ∈ {1,2,3} are excluded by Corollary 14, clauses 1–2. This covers all MUB-pair planes.
  - Planes span(u, W_wu) with w ≠ 0, ‖u‖ = 1 and ⟨u, W_wu⟩ = 0 are excluded by Corollary 14, clause 3 as amended.
  - Planes span(u, W_wu) with ⟨u, W_wu⟩ ≠ 0 are not excluded in writing.

**MINOR-4: wording conflicts with the non-claims.**
- **Where:** 01 LF14, "a new import-free lemma", conflicts with the no-novelty statement at LF5. LF15, "exactly the 15 vectors", is imprecise.
- **Repair:**
  - Delete "new".
  - Replace "exactly the 15 vectors" with "exactly the unimodular multiples of the 15 vectors ψ^k_m, k ∈ {1,2,3}", as Lemma 10 itself says at LF187–188.

**MINOR-5: cross-document claims cannot be verified from the packet.**
- **Where:** 01 LF16–17, LF247–248 and LF282; JSON LF57–58 and LF70.
- **Problem:** these lines claim three things:
  - Prop B "needed" Haagerup.
  - Cor 14 "removes [I-H]".
  - Cor 14 "settles (E4)".
- These depend on `w8-decision-v1.md` §4 and its addendum-1, which are not in the packet. What I did verify is narrower: Cor 14 as stated is import-free.
- **Repair:** quote Prop B and (E4) verbatim next to Cor 14, or change "settles" to "is offered as settling, subject to parent comparison". The parent should not record (E4) as closed on the strength of this review alone.

**MINOR-6: JSON dependency lists are incomplete.**
- **Where:** JSON LF38 (Thm 5) and LF47 (Cor 14).
- **Problem:**
  - Thm 5 uses Lem 2 (isometry, and flatness ⇔ (R1)) in both directions, but LF38 omits it.
  - Cor 14 clauses 2–3 need S_r to be flat, which is the hypothesis of Cor 11 and comes from Lem 2. LF47 omits Lem 2.
- **Repair:** add "Lem2" to both `uses` arrays.

## Notes (not counted)

- **N1.** In Thm 3(d), "30 in all" counts only cross-orbit zeros. (R1) also forces τ_rr(w) = 0 for w ∈ (L_Z ∪ L_X ∪ L_T)∖{0}, which is 12 per orbit and 48 in total. The statement is correct as written and these zeros are not needed for (e). Writing "cross-orbit" would make that explicit.
- **N2.** In Lem 7, LF153 "dim E₊₁ = n mod 2" should read ≡. The "onto" at LF148 follows from Θ being bijective; one clause would say so.
- **N3.** The equation counts at LF42 and LF137–138 are counts, not ranks. No independence is claimed.
- **N4.** The scope freeze (LF48–49) asks for further imports to be named at their point of use. Cauchy–Schwarz (Thm 3) and the spectral theorem (Lem 7, Lem 9(ii)) are named only in §10 under I2. This is within I2 as defined, so the issue is procedural only.

## Recommendation and scope

- No finding blocks the restricted mathematics.
- MINOR-1, MINOR-2 and MINOR-3 are the same kind of issue PE addressed (precision in summaries and the interface), so they are worth recording in a parent erratum. MINOR-4, MINOR-5 and MINOR-6 are housekeeping.
- Acceptance remains with the parent; this review grants none.
- This review covers only the restricted ansatz (H). The open part is unchanged: the non-MUB-pair flat planes, items (C1)–(C3).
- None of the following follows from the package or this review:
  - a witness;
  - an ansatz-wide no-go, for any cardinality or for maximal cardinality;
  - any statement about unrestricted 1-RQLS(10), whose maximal target remains OPEN / UNKNOWN.
