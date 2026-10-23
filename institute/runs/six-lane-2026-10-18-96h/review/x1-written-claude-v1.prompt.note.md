**VERDICT: ACCEPT.** This covers the candidate read together with the mandatory pairwise-LFC clarification, which should stay attached (see m1).

There are no FATAL or MAJOR issues and two MINOR ones, both editorial and non-blocking. Every implication holds, and I found no gap and no counterexample. I reviewed the text as pasted and did not check the SHA-256.

## Issues

**m1 (MINOR): Imports item 1 contradicts the sentence after item 3.**
- Item 1 imports LFC in its general hereditary form "at its existing scope".
- The source proof of LFC (c) applies Sun(|T|) to fibre sets, here with |T| ≤ 4. That contradicts "the proof does not import Sun(3)–Sun(6)".
- The clarification closes the gap. Steps 2 and 4 use only the pairwise instance, which it proves from Sun(2) alone; I re-derived that proof below.
- *Smallest fix:* replace item 1 with: "If F ⊆ V∖{v} has pairwise-coprime local indices, then Σ_{j∈F} t_j ≤ n_v − 1, i.e. Σ_{j∈F} α_vj/g_vj ≤ 1 − 1/n_v." In Steps 2 and 4, read "no allowed set contains both / feasible" as "no fibre holds pieces of two members of F".

**m2 (MINOR): Setup line "so 1 ≤ α_ij ≤ g_ij − 1" has no derivation.**
- The upper bound is load-bearing: Step 2's dichotomy α_{d1c} ∈ {1,2} and Step 3's x ≤ 5 depend on it.
- *Smallest fix:* append "(lcm(n_i,n_j) | I_ij by Lagrange; μ(U_iU_j) = α_ij/g_ij < 1 because g_i⁻¹g_j ∉ U_iU_j)". Alternatively, it follows from INV, since α ≤ g − α* ≤ g − 1.

**Scope note (not a defect): the K5.3→X1 bridge is not certified here.**
- The "Bridge" paragraph's K5.3→X1 deletion bridge is not in the supplied material.
- Deleting cosets preserves disjointness and indices. So the bridge needs only that K5.3's definition makes the two D-cofactors odd and all five cofactors pairwise coprime. That definition was not supplied.
- ACCEPT covers the X1 statement, including the arbitrary-group lift.

## Independent verification

**Coset conventions (nonabelian, left cosets)**
- **Disjointness.** g_iU_i ∩ g_jU_j ≠ ∅ ⇔ g_i⁻¹g_j = uw⁻¹ ∈ U_iU_j for some u ∈ U_i, w ∈ U_j.
- **Product formula.** |AB| = |A||B|/|A∩B| holds for any subgroups, with no normality needed. So μ(U_iU_j) = I_ij/(n_in_j) = α_ij/g_ij.
- **R0 lift.**
  - core(U_i) is the kernel of G → Sym(G/U_i), so it has finite index.
  - N = ∩ core(U_i) lies in every U_i, and g_iU_iN = g_iU_i.
  - So the images in G/N are pairwise disjoint left cosets with unchanged indices. ✓
- **INV, the inversion.** (g_iU_i)⁻¹ = U_ig_i⁻¹ = g_i⁻¹(g_iU_ig_i⁻¹). Inversion is a bijection, so the inverted cosets are disjoint and keep the same labelled indices.
- **INV, the bound α + α* ≤ g.**
  - Put h = g_v⁻¹g_j. Conjugating by g_v turns U_v* ∩ U_j* into U_v ∩ hU_jh⁻¹.
  - |U_vhU_j| = |U_v·hU_jh⁻¹| = |U_v||U_j|/|U_v ∩ hU_jh⁻¹|, so μ(U_vhU_j) = α*_vj/g_vj.
  - Disjointness ⇔ h ∉ U_vU_j. So U_vhU_j and U_vU_j are distinct, hence disjoint, double cosets.
  - Therefore α_vj + α*_vj ≤ g_vj, and α* is symmetric. ✓
- **Pairwise LFC, counting fibres.**
  - The left U_v-cosets meeting g_jU_j are g_juU_v for u ∈ U_j. Two coincide iff u⁻¹u′ ∈ U_j∩U_v.
  - So there are exactly t_j = I_vj/n_j = n_vα_vj/g_vj of them, and none is g_vU_v.
- **Pairwise LFC, pieces.**
  - Take p_j ∈ g_jU_j ∩ xU_v. The piece is p_jU_j ∩ p_jU_v = p_j(U_j∩U_v), and x⁻¹p_j ∈ U_v.
  - So in every fibre, the translated piece is a left coset in U_v of U_v∩U_j.
  - Its index is λ_j = I_vj/n_v = n_jα_vj/g_vj, which does not depend on the fibre.
- **Pairwise LFC, coprime pieces cannot share a fibre.**
  - Suppose gcd(λ_j,λ_k) = 1, and put A = U_v∩U_j, B = U_v∩U_k.
  - [U_v : A∩B] is divisible by λ_jλ_k, and |AB| ≤ |U_v| bounds it above by λ_jλ_k.
  - So AB = U_v, and aA ∩ bB ≠ ∅ for all a, b ∈ U_v, since a⁻¹b ∈ AB.
- **Pairwise LFC, the count.**
  - A pairwise-coprime family F has at most one member per fibre, so Σ_F t_j ≤ n_v − 1.
  - All three weight vectors in the proof are indicators of such families: {d_2,c}, {d_1,d_2,j} and {d_1,d_2,j,k}. ✓
- **T, lower bound.**
  - Each n_i | T and I_xy | T.
  - L = lcm(n_x,n_y)·ℓ_z, because ℓ_z = n_z/gcd(n_z, lcm(n_x,n_y)).
  - Hence α_xy | ℓ_zτ, so τ is a positive multiple of τ_min.
- **T, upper bound.**
  - μ(U_y(U_x∩U_z)) = T/(n_yI_xz) = τ/(γ_yα_xz).
  - U_y(U_x∩U_z) ⊆ U_yU_x ∩ U_yU_z gives τ ≤ τ_max.
  - The omitted floor is harmless because τ_min is an integer. T uses no disjointness. ✓

**Gcds**
- g_{d1d2} = 3·gcd(r_1,r_2) = 3.
- g_{d_ic} = 3·gcd(r_i, 2r_c) = 3. This needs r_i odd; otherwise it would be 6.
- g_{cc′} = 6·gcd(r_c, r_{c′}) = 6, whatever the parity. ✓

**Step 1 (orientation)**
- On the edge d_1d_2, both α and α* lie in {1,2} and sum to at most 3, so one of them equals 1.
- If a configuration exists, so does its inverse, with the same labelled tuple. Refuting whichever one has α_{d1d2} = 1 is enough.
- The orientation is chosen once. Steps 2–4 never re-invert, and the d_1↔d_2 swap uses only α_{d2d1} = α_{d1d2} = 1.
- Step 1 is load-bearing. With α_{d1d2} = 2, λ_{d2} = 2r_2 shares the factor 2 with λ_c ∈ {2r_c, 4r_c}, and Step 2 fails. ✓

**Step 2 (d–C edges)**
- At d_1, λ_{d2} = r_2 with t = r_1.
- If α_{d1c} = 2, then λ_c = 4r_c with t = 2r_1.
- gcd(r_2, 4r_c) = 1 because r_2 is odd. So Σt = 3r_1 = n_{d1} > n_{d1} − 1.
- At d_2 the argument is symmetric, using r_1 odd. ✓

**Step 3 (C–C edges), for each i ∈ {1,2}, in the triangle (d_i, c, c′)**
- γ_{d_i} = lcm(3,3) = 3 and γ_c = γ_{c′} = lcm(3,6) = 6, so ℓ_{d_i} = r_i.
- **τ_min.**
  - The edges d_ic and d_ic′ have α = 1 and each contribute 1.
  - Those are the only places ℓ_c and ℓ_{c′} could enter. So the C-cofactors' parity and their 2-, 3- and 5-valuations really are irrelevant.
  - The edge cc′, opposite d_i, contributes x/gcd(x, r_i).
- **τ_max.**
  - Apex d_i gives 3·x·⅓ = x.
  - Apex c or c′ gives 6·1·min(⅓, x/6) = min(2, x).

| x | τ_min (r_i odd) | τ_max | Result |
|---|---|---|---|
| 1 | 1 | 1 | survives |
| 2 | 2 | 2 | survives |
| 3 | 1 if 3∣r_i, else 3 | 2 | needs 3∣r_1 and 3∣r_2 ✗ |
| 4 | 4 | 2 | ✗ (either triangle) |
| 5 | 1 if 5∣r_i, else 5 | 2 | needs 5∣r_1 and 5∣r_2 ✗ |

**Step 4 (LFC at a C-vertex c), using α_{cd_i} = 1 from Step 2 by symmetry**
- **Local data.**
  - λ_{d_i} = r_i with t = 2r_c.
  - λ_j = α_{cj}·r_j with t_j = α_{cj}·r_c.
- **Case α_{cj} = 2.**
  - The indices r_1, r_2 and 2r_j are pairwise coprime. This needs r_1 and r_2 odd; r_j may be even.
  - Σt = 2r_c + 2r_c + 2r_c = 6r_c = n_c. ✗
- **Case α_{cj} = α_{ck} = 1.**
  - The indices r_1, r_2, r_j and r_k are pairwise coprime.
  - Σt = 2r_c + 2r_c + r_c + r_c = 6r_c = n_c. ✗
- Given Step 3, the case split is exhaustive. Only the two C-edges at c are actually needed. ✓

**Strictness**
- Every contradiction is Σ_F t_j = n_v exactly, against the bound n_v − 1.
- The strictness comes from the exclusive fibre g_vU_v, which is correctly left out of the count.
- A non-strict bound would prove nothing. ✓

**Edge cases and where each hypothesis is used**
- **Degenerate values.** r_i = 1 is allowed (λ = 1 just means a piece fills its fibre), and so are repeated indices. Nothing assumes distinct indices or r_i > 1.
- **r_1 and r_2 odd.** Used for g_{d_ic} = 3, in Step 2, in Step 3 at x = 4, and in Step 4's case α_{cj} = 2.
- **gcd(r_1, r_2) = 1.** This is what kills x = 3 and x = 5.
- **All five vertices.** The case α_{cj} = α_{ck} = 1 needs both of the other C-vertices. With only one, the sum would be ⅚.
- **Imports.** The route uses no computed value, no Sun(t) with t ≥ 3, and nothing from RPLP, Menon or Margolis–Schnabel. As written, it can replace the StageA certificate for X1.
