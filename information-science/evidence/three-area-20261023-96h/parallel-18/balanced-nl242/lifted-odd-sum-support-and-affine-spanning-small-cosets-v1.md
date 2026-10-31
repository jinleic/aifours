# Balanced NL242 — odd-sum support of off-dual slices, and affine spanning of the small-value cosets at (2,160)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:08:10 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed and unadopted. It is not machine-checked, formal, kernel-checked or novelty-cleared. No program, Eval, CAS, enumeration, solver, CLI, nested agent or GO was used; all arithmetic was done by hand in writing.

This packet does **not** exclude a residue type. The (2,160) type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Inputs

Admitted at their cuts:

- **S0017** `global-all-rank-ternary-lift-and-dual-occupancy-v1.md` (SHA `842bb4e6…86bf`): relation (3), B ≡ q − Hδ (mod 3); formulas (6) and (9); and the meaning of δ (δ = ±χ exactly on {|S| ∈ {4, 12}}).
- The lifted-bent structure: Lemma 4.1 of `global-exact-occupancy-identity-and-lifted-coset-structure-v1.md`, which is standard quadratic-form theory.
- From own candidates (cited as context only, not as premises of the main theorem): Theorem E of `u-class-L-parity-and-rank4-160-coset-projection-v1.md` (SHA `7cecd509…0c9b`) and Theorem 2 of `rank4-160-four-coset-strata-Q-shape-and-R-side-reduction-v1.md` (SHA `5517814f…7962`). They are used only in Corollary O2.

The NONINPUT set is unchanged, and the d128/u8 branch is not touched.

## 1. Setting (every lifted type)

Let d ∈ {192, 160, 112, 144}, i.e. Ŵ_D(0) ≠ 0.

- V is the radical of D, D = D̄∘π, and U = V^⊥ (Lemma 4.1).
- Coordinates: a = (ā, β), with ā ∈ F_2^8/V ≅ F_2^{2r} and β ∈ V. Dually x = (ξ, η), with V^⊥ = {(ξ, 0)}.
- The slice functions are u_η(ξ) := B(ξ, η). Then υ_η(ā) := (1/2|V|) Σ_{β} S(ā,β)(−1)^{β·η} = Σ_ξ u_η(ξ)(−1)^{ā·ξ}. This follows from S = 2HB.
- P ⊆ F_2^{2r} is the set of V-cosets that contain at least one small value (|S| ∈ {4, 12}).
- OddSums(P) := {Σ_{t∈T} t : T ⊆ P, |T| odd}.

## 2. Lemma O (odd-sum support)

**Lemma O.** For every η ≠ 0, the Walsh transform of u_η is supported in OddSums(P). Consequently, for every coset ā ∉ OddSums(P):

- the S-row on ā is constant;
- T ≡ −28 or T ≡ 20 on the whole coset;
- s_ā := υ_0(ā) = c_ā T/2 ∈ {−14c_ā, 10c_ā}, so **|s_ā| ≥ 10**.

*Proof.*

1. For η ≠ 0, the point (ξ, η) lies outside U, so q(ξ, η) = 0. S0017 (3) gives

   B(ξ,η) ≡ −Σ_ā g_η(ā) y_ā (mod 3),  with y_ā := (−1)^{ā·ξ} and g_η(ā) := Σ_β δ(ā,β)(−1)^{β·η}.

   Here g_η(ā) = 0 for ā ∉ P.
2. B takes values in {0, ±1}, so B = Ψ_η((y_ā)_{ā∈P}), where Ψ_η(y) is the centred residue of −Σ g_η(ā) y_ā. Ψ_η is an odd function on {±1}^P.
3. In its multilinear (Fourier–Walsh) expansion Ψ_η = Σ_T Ψ̂_T Π_{t∈T} y_t, only odd |T| occur. Moreover Π_{t∈T} y_t = (−1)^{(ΣT)·ξ}.
4. Hence u_η = Σ_{|T| odd} Ψ̂_T (−1)^{(ΣT)·ξ}, and its Walsh support lies in OddSums(P).
5. Now let ā ∉ OddSums(P). Then Σ_β S(ā,β)(−1)^{β·η} = 2|V|·υ_η(ā) = 0 for all η ≠ 0, so S(ā,·) is constant on the coset.
6. Since ā ∉ P, there are no small values, so T ∈ {−28, 20} is constant.
7. Finally 2|V| s_ā = Σ_{b∈ā} S(b) = |V| c_ā T. ∎

**Remark (sanity checks of the expansion, by hand).**

- If |supp g_η| = 2, then u_η = (y_1 + y_2)/2.
- If |supp g_η| = 3, then u_η = (−Σy + 3y_1y_2y_3)/4.
- For four ±1 terms, F(Σz) = (1/8)e_1 − (3/8)e_3.

In every case the Walsh support is visibly inside the odd sums.

## 3. Theorem O (the small-value cosets span affinely)

Parseval on U gives Σ_ā s_ā² = 2^{2r}·|supp u_0| ≤ 2^{4r}. Each coset outside OddSums(P) contributes at least 100. Also OddSums(P) ⊆ aff(P), since an odd sum of points of an affine flat lies in the flat.

**Theorem O.**

**(a) At (2,160)**, where the quotient is F_2^4:

- at most 2 cosets lie outside OddSums(P);
- P is contained in no affine hyperplane of F_2^4, otherwise at least 8 cosets would be excluded;
- hence P affinely spans F_2^4, and |P| ≥ 5.

**(b) At rank-6 lifted types** (d = 112, 144; quotient F_2^6, bound 4096):

- at most 40 cosets lie outside OddSums(P), so |aff(P)| ≥ 24;
- hence dim aff(P) ≥ 5 and |P| ≥ 6.

**(c) At (1,192)**, the bound is 16 < 100, so OddSums(P) = F_2^2, and P has at least 3 points.

## 4. Corollaries at (2,160)

**Corollary O1.** At (2,160), the set of V-cosets carrying small values is never contained in an affine 2-flat or an affine 3-flat of F_2^8/V. Equivalently, the small-value positions are contained in no affine hyperplane of F_2^8 that is a union of V-cosets.

**Corollary O2 (strata of Theorem E).** In every |Σ| = 4 stratum, at least two cosets outside the imbalanced flat Σ carry small values.

- This is because aff(Σ ∪ Σ_0) = F_2^4 requires two points beyond the 2-flat.
- Each such coset has λ ≡ μ (mod 3) with (λ, μ) ≠ (0, 0), so it carries at least 2 small values.
- Hence L ≥ L_Σ + 4. In particular, the stratum (α, L, u) = (4, 16, 8) with every small value inside Σ, which survived Lemma S, is now **excluded**.
- In all three strata (6,12,8), (4,12,16) and (4,16,8), L_Σ ≤ L − 4.

Corollary O2 strengthens Corollary S of `rank4-160-four-coset-slice-count-mod4-addendum-v1.md` (SHA `b45484ec…a5e4`), which forced only one off-Σ coset, and only in the L = 12 strata.

## 5. Status

**WRITTEN:** Lemma O, Theorem O (a)–(c), and Corollaries O1 and O2.

**Not proved:** any whole residue type; the |Σ| = 4 strata with off-Σ small values; any |Σ| ≥ 5 case; rank 6 or rank 8. The (24,24,2) gap and the original problem remain OPEN.

**First unproved step.** Exploit Lemma O quantitatively. A pure coset ā ∉ P with 0 < k < 16 needs Σ_{η≠0} υ_η(ā)² = (9/4)k(16 − k). That energy can only come from the |T| ≥ 3 coefficients Ψ̂_T of the slices. For example, a three-point support gives 12 at the triple sum, and a four-point non-flat support gives −6 at each triple sum. Balance this against the slice counts m_η and the census.

Novelty and priority are UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR and the own attribution MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 2026-10-27T11:05:38-07:00; no early park.
