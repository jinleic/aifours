VERDICT: ACCEPT-WITH-FIXES

I found no critical or major defect. Theorem 1 follows from §§1–4 without [44] and without §6. Corollary 2 uses [44] legitimately and not circularly. Findings 1–3 are minor gaps in the written justification; findings 4–7 are cosmetic. None changes a statement.

## Findings

1. **Minor, rigor gap. §2, Prop. 2.4, "Because the action is free (Lemma 2.3) … these prescriptions are consistent."**
   - Freeness makes `h` unique for each point `y = h·y0`. But the prescription (`δψ(y0)` for even, `−conj δψ(y0)` for odd) is attached to a *word* for `h`.
   - Consistency also needs word-parity to depend only on `h`. Freeness does not give this; Lemma 2.2 does. Each generator acts by `t ↦ −t`, so a word of length `k` acts by `t ↦ (−1)^k t`, and `t ≠ −t` in `F3*`.
   - *Fix:* insert the following. "Let `ε(h) ∈ {0,1}` record whether `h` negates `t`. Then `ε` is the sign character of `H ≅ S3`, so `φ(h) := (z ↦ −z̄)^{ε(h)}` is a homomorphism `H → GL_R(C)`. The off-code kernel is `{δψ : δψ(hy) = φ(h)δψ(y)}`, which is `≅ C` on each free orbit."
   - Also add one clause: freeness of the *reflections* is what the count needs. A reflection fixing `y` would force `Re δψ(y) = 0`.

2. **Minor, rigor gap. §3, Prop. 3.1, code part, "hence these sums span all functions on C".**
   - The character argument gives the complex span with complex `θ_q`. The actual parameters are real: `h_q[x,x] = iθ_q(x)`.
   - *Fix, either:*
     - (a) `Re χ_w` and `Im χ_w` are real functions of a single `ℓ_q`, and they span `R^C`: take real parts of `v = Σ a_w χ_w`.
     - (b) Use the character-free decomposition in D5.

3. **Minor, load-bearing fact supported only by "(checked)". §1.3, last sentence.**
   - `O9 ⊆ D ∩ T` is needed by Cor. 3.2 and by §4 (`O9 ∩ W1 ⊆ D`).
   - *Fix:* give the hand proof. For each matching, `M_S(1_C)[s,t] = 1 ⟺ t = f_S(s)`, and `f_S` is a bijection by MDS, so `M_S` is a permutation matrix.
   - By §1.4, `P9 = M_12^T`, `P9^R = S9 M_13 S9` and `P9^Γ = S9 M_14^T`. This is already the first sentence of the proof of Lemma 2.1; cite it there.

4. **Cosmetic. §0 definition of `g·U`, used in §4 ("orbit of the compact connected Lie group G … constant rank by equivariance").**
   - As written, `g·(h·U) = (v1w1⊗v2w2) U (w3v3⊗w4v4)`. That is not a left action of `U(3)^4`.
   - *Fix:* take `G := U(3)×U(3)×U(3)^op×U(3)^op`, or act by `(v3⊗v4)^{-1}` on the right.
   - **Effect on the proof: none.**
     - The orbit set is unchanged.
     - The Lie-algebra image in Prop. 3.1 is the same real subspace; at most `h3, h4 ↦ −h3, −h4`.
     - `U(3)^op ≅ U(3)` via inversion, so the group is still compact and connected. The embedded-orbit and constant-rank facts then apply literally.
     - `Φ_g(D)=D`, `Φ_g(T)=T` and `Φ_g(O9)=O9` hold for each fixed `g` regardless.
     - In the ψ-picture (`v3^T⊗v4^T⊗v1⊗v2`), transposition already turns the opposite factors into a genuine action.

5. **Cosmetic. §4, "open `W2 ∋ P9` with `N ∩ W2 ⊆ O9`, therefore `D ∩ W2 = O9 ∩ W2`".**
   - The inclusion `D ∩ W2 ⊆ N` needs `W2 ⊆ W1`. *Fix:* state it.
   - `ε := dist(O9, V∖W)` is finite because `S ∈ D∖O9 ⊆ V∖W`. Alternatively, drop `W` and use homogeneity (D7).

6. **Cosmetic, non-load-bearing computational citations.**
   - Locations: §1.2 "exhaustive search"; §4 "explicit 129×129 minor"; §4 "Independent route" ("checked symbolically…" and "`P9·S = …`, evidence").
   - None is needed. The 129 independent components exist by linear algebra from Prop. 2.4.
   - The identities can be stated explicitly: `(US)^R = U^Γ S`, `P9 S = (Π2⊗I)P9` and `P9 = (I⊗Π2)P9^{[44]}`, with `Π2|x⟩=|2x⟩` (see D1, D7).

7. **Cosmetic, optional. §5, "By [44] again, `D∖O9` is exactly the set of non-2-unitary dual gates."**
   - This second use of [44] is unnecessary. `O9 ⊆ T` gives `D∖T ⊆ D∖O9` without [44].
   - Hence `sup_{D∖T} e_p ≤ max_{D∖O9} e_p < 1`. [44] is then used exactly once, to exclude `e_p(U*) = 1`. Likewise `T∖D ⊆ T∖O9`.

**Sign/index errors:** none found. The corrected `M_14 = (U^Γ)^T S9` is right.

**Circularity:** none. §§1–4 never invoke [44]; §1.2 only relates other descriptions of P9 by local permutations.

## Independent derivations

**D1. Conventions and dictionary.**
- The listed ones give `P9|ab⟩ = |2a+b, a+b⟩`; I checked all nine.
- `C = {(a,b,2a+b,a+b)}` has 2×2 generator minors (12,13,14,23,24,34) = (1,1,1,1,2,1), so it is MDS.
- Survey eq. (12): the coefficient of `|abcd⟩` is `(1/3)U[(c,d),(a,b)]`, matching the dictionary.
- The reshapings, entry by entry:
  - `M_12[(a,b),(c,d)] = U[(c,d),(a,b)]`, so `M_12 = U^T`.
  - `M_13[(a,c),(b,d)] = U^R[(c,a),(d,b)]`, so `M_13 = S9 U^R S9`.
  - `M_14[(a,d),(b,c)] = U^Γ[(c,b),(a,d)]`, so `M_14 = (U^Γ)^T S9`.
- Cross-check against the survey's own interpretation:
  - `ρ_AC = (1/9)S9 U^R U^R† S9`, so `1 − Tr ρ_AC² = E(U)`.
  - Likewise `1 − Tr ρ_BC² = E(US)`.
  - So R corresponds to 13|24 and Γ to 14|23, as the write-up uses.
- [44]'s listing, 0-indexed, is `(a,b) ↦ (2a+b, 2a+2b)`, and applying `(I⊗Π2)` gives P9. Read as the inverse, it is `(x,y) ↦ (x+y, 2x+y) = (Π2⊗Π2)P9(I⊗Π2)`. Either way it lies in O9, without using [44]'s uniqueness.
- Every linear or affine `|ab⟩ ↦ |A(a,b)+v⟩` with `A ∈ GL2(F3)` and all entries nonzero lies in O9. Coordinate scalings act by `A ↦ D1 A D2` and normalize `A` to `[[1,1],[1,2]]`.

**D2. LU covariance.** I re-derived both formulas of §1.3 entry by entry, including `W^Γ = (v1⊗v4^T)U^Γ(v3⊗v2^T)`.

**D3. Linearization.**
- At a unitary `M`, `M†(δM M† + M δM†)M = δM†M + M†δM`, so the two kernels agree.
- `M_12M_12† = (U†U)^T`, `M_13M_13† = S9 U^R U^R† S9` and `M_14M_14† = (U^Γ†U^Γ)^T`.
- Lemma 2.1 reproduces, including the bijection between pairs `(s,s')` with `s≠s'` and points `y∉C` (72 each).

**D4. τ and the S3 action.** I checked the formulas on `y = e1`, i.e. `(c,q,t) = (0,1,1)`.
- `τ_12(e1)`: the direct π-computation gives `(0,0,2,1)`; the formula gives `g_12 − e1 = (1,0,2,1) − e1`, the same point.
- `τ_13(e1) = (0,1,0,2)` both ways, with `g_13 = (1,1,0,2)`.
- `ρ = τ_12τ_13`: directly `τ_12(0,1,0,2) = (1,1,1,1)`; by formula `w_1 = g_13 − g_12 = (0,1,1,1)` and `e1 + w1 = (1,1,1,1)`.
- In general `ρ^k(c,q,t) = (c + k t w_q, q, t)` with `w_q ≠ 0` and `(w_q)_q = 0`.
- Exactly three codewords share each value of the q-coordinate. So the ρ-orbit is `{(c',q,t) : c'_q = c_q}`, and the H-orbit adds `{(c',q,−t) : c'_q = c_q+t}`.
- H-orbits therefore correspond to pairs `(q, {u,v})`: 4·3 = 12 orbits of size 6. The kernel has dimension 9 + 24 = 33.

**D5. Tangent count over R.**
- The tangent map is block-diagonal:
  - Off-diagonal entries of `h_q` only reach off-code points, with value `h_q[c_q+t, c_q]`. This part is injective, giving 24.
  - Diagonal entries only reach codewords.
- Code part: `R^{F3²} = R·1 ⊕ V_1 ⊕ … ⊕ V_4`, where `V_q = {θ∘ℓ_q : Σθ = 0}` has dimension 2.
- The summands are orthogonal. For `q≠q'`, `(ℓ_q, ℓ_q')` is a bijection of `F3²`, because the `ℓ`'s are the four points of `P¹(F3)`. So `⟨θ∘ℓ_q, θ'∘ℓ_q'⟩ = (Σθ)(Σθ') = 0`, and each `V_q` is orthogonal to `1`.
- The code part therefore has dimension 1 + 8 = 9. Its kernel is constant `θ_q` with `Σ = 0`: the 3 phases.

**D6. Tangent equals kernel directly, without counting dimensions.**
- Take `y = (c,q,t)`, so `δψ(y) = h_q[c_q+t, c_q]`.
- Then `τ_S y = (c+tg, q, −t)` with `(c+tg)_q = c_q+t`. Hence `δψ(τ_S y) = h_q[c_q, c_q+t] = −conj δψ(y)` for every S, and ρ preserves `c_q` and `t`.
- So on the orbit `(q,{u,v})` the tangent supplies an arbitrary complex value `h_q[u,v]`, which is exactly the kernel's copy of `C`. On codewords both are `iR^C`.
- This also checks the signs in Lemmas 2.1 and 2.2 independently.

**D7. §4 logic.**
- `F'` is a submersion near P9, because full rank is an open condition. No constant-rank assumption on the full F is used.
- The upper bound on D comes from `D ⊆ F'^{-1}(0)`.
- O9 is an embedded submanifold because it is a compact orbit. The inclusion `O9∩W1 → N` is smooth because N is embedded, and it is an immersion between manifolds of equal dimension. So it is open.
- Uniform tube by homogeneity:
  - Pick `ε` with `B(P9,ε) ⊆ W2`.
  - If `U ∈ D` and `‖U − g·P9‖ < ε`, then `Φ_g^{-1}U ∈ D ∩ B(P9,ε) ⊆ O9`.
- Swap identity: `(US)^R[(i,j),(α,β)] = (US)[(i,α),(j,β)] = U[(i,α),(β,j)] = U^Γ[(i,j),(β,α)] = (U^ΓS)[(i,j),(α,β)]`.
- `P9S|ab⟩ = |a+2b, a+b⟩ = (Π2⊗I)P9|ab⟩`. Since `U ↦ US` is an isometry with `O9S = O9`, the same ε works for D and T.
- `D∖O9 = D ∩ (V∖W)` is closed in the compact set D, hence compact.

**D8. §5.**
- Lemma 5.1 reproduces.
- `I^R = |Φ⟩⟨Φ|` has rank one, so `E(I) = 0` and `e_p(S) = e_p(I) = 0`. Both complements are therefore nonempty.
- Why the gap must be stated on D and T:
  - For all gates, `x = E(U)/E(S) ≤ 1` and `y = E(US)/E(S) ≤ 1`.
  - Then `(e_p, g_t) = (x+y−1, (x−y+1)/2)` lies in a wedge with apex `(1, 1/2)`. Its edges are `g_t = 1 − e_p/2` (dual) and `g_t = e_p/2` (T-dual).
  - For generic Hermitian `H`, `e^{isH}P9` leaves O9 for small `s ≠ 0` (velocity outside the 33-dim tangent space, secant argument). By Theorem 1 those gates are not dual, yet `e_p → 1`.
  - So a gap "over all gates" is false, and Corollary 2 is the correct formalization.

**D9. Readings of T7.**
- **Literal reading:** yes, trivially. `(v⊗I)P9 ∈ O9 ⊆ D∩T` and `(v⊗I)P9 → P9`.
- **Non-trivial reading, near P9 or near O9:** no, by Theorem 1 alone. This is exactly the survey's "U9 seems isolated…", since U9 is defined as O9.
- **Near "the 2-unitary set", and the e_p gap:** these need [44] to identify `D∩T` with O9.

## Trust limits
- I used no tools. I did not open `evidence/`, run code, or verify the pinned SHA256; this review covers the pasted text only. Nothing above relies on §6.
- **Not seen:** source (C7) and (C8), state (14), Sec. III A, [44] (A14), and the wording of T7.
  - "(C7) = this permutation" is the write-up's claim. D1 shows the conclusion is insensitive to it within the linear/affine class.
  - The literal versus non-trivial split is judged against the write-up's paraphrase of T7 and the survey's isolation/gap passage.
- **Not re-checked:** [44, Thm 1], and through it the non-existence of two-qutrit universal entanglers.
  - Theorem 1 and the "near P9 / near O9" answer do not depend on them.
  - Corollary 2 and the "2-unitary set" answer do.
- **§7, d = 4 control, partly checked.**
  - Checked: the code tangent count 1+4·3 = 13; the enphasing directions span `iR^C`, giving rank 64; and the secant argument that the curve leaves O16.
  - Not verified: the Klein-four freeness and the kernel dimension 136. These are not load-bearing.
- Correctness only; no novelty or priority assessment.
