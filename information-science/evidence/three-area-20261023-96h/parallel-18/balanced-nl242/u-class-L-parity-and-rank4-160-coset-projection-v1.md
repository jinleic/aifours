# Balanced NL242 — the class of u mod 8, even L at polar ranks 2/4/6, and the (2,160) coset projection (at least four imbalanced cosets)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 06:50:07 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is not reviewed or adopted. It is not machine-checked, formal, kernel-checked, executed or novelty-cleared. No interpreter, Eval, calculator, CAS, enumeration, solver, replay, CLI, nested agent or GO was used. All arithmetic was done by hand in writing.

This packet does not resolve the original problem. The (24,24,2) gap remains OPEN, and no whole residue type is excluded.

## 0. Inputs (admitted, at their parent cuts) and notation

**Authority.** v205 was read ENTIRE first; this is prospective, source-separated work.

**Admitted inputs:**

- **S0017** `global-all-rank-ternary-lift-and-dual-occupancy-v1.md` (SHA `842bb4e6…86bf`), an admitted Gate I source. Used: the ternary relation (3), the norm (5), the formulas (6)–(8), the census (9), (10) and (11), and the d160 relation (13). Its notation is used throughout:
  - B = HS/512 is the S-sector array (written u-array);
  - a = HR/512 is the R-sector array;
  - p = R/8, z = #{p = 0}, c = #{|p| = 1}, u = z + 2c;
  - q = εHχ/A_r, with U = supp q and t = |U| = 2^{2r};
  - α = #{x ∈ U : B = 0}, ν = #{x ∈ U : B = −q}, and N_+ := t − α − ν = #{x ∈ U : B = q};
  - w_R = wt(a);
  - δ = φ(ζ), where ζ = −(S + 4χ)/8, χ = (−1)^D and T = χS. Then δ = +χ on {T = −12}, δ = −χ on {T = 4}, and δ = 0 elsewhere, so wt(δ) = L.
- **Gate II floor:** L ≥ 10 at (2,160). **Gate III floor:** L ≥ 8 at every rank-6 weight. **Sparse floor:** L ≥ 4.
- **Ordinary mathematics:** quadratic forms over F_2 and their Walsh spectra, Fourier analysis on F_2^n over Z and F_3, Parseval.

**Not inputs:**

- the unreviewed own candidates v2–v12 (not read in this session; any coincidence of conclusions is noted, not used);
- the HELD u8/L14 lead;
- the v147-F1 and v112 scouts.

The d128/u8 branch is not developed here.

## 1. Theorem A — the class of u mod 8, for every residue type

**Theorem A.** u ≡ c_d (mod 8), where

| d | 192, 160, 128 | 112, 144 | 120 | 136 |
|---|---|---|---|---|
| c_d | 0 | 4 | 6 | 2 |

Hence u ≥ 8 for d ∈ {192, 160, 128}, u ≥ 4 for d ∈ {112, 144}, u ≥ 6 for d = 120 and u ≥ 2 for d = 136.

*Proof.*

1. By (6), R = 2Ha. Since R(0) = 0, Σ_x a(x) = 0. So a has as many +1 as −1 entries, and w_R is even. S0017 §6 used this argument only at d = 128.
2. By (9), w_R = 64 + 5d/16 − u/4. Requiring this to be even gives the table:
   - d = 160: w_R = 114 − u/4, so u/4 is even.
   - d = 192: w_R = 124 − u/4, so u/4 is even.
   - d = 128: w_R = 104 − u/4, so u/4 is even.
   - d = 112: w_R = 99 − u/4, so u/4 is odd.
   - d = 144: w_R = 109 − u/4, so u/4 is odd.
   - d = 120: w_R = 101.5 − u/4, so u/4 ≡ 3/2 (mod 2) and u ≡ 6 (mod 8).
   - d = 136: w_R = 106.5 − u/4, so u/4 ≡ 1/2 (mod 2) and u ≡ 2 (mod 8).
3. Finally u ≥ z ≥ 1, because p(0) = 0. ∎

## 2. Lemma B — coset parity at polar rank 6

**Lemma B.** Let r = 3, and let V be the radical of the polar form of D, so |V| = 4. For every c ∈ F_2^8, the set supp(a) ∩ (c + V^⊥) has even size. In particular α = |supp(a) ∩ U| is even.

*Proof.*

1. For every a_0 and c,

   Σ_{v∈V} R(a_0 + v)(−1)^{(a_0+v)·c} = 2|V| Σ_{x∈c+V^⊥} a(x)(−1)^{a_0·(x+c)}.

   This follows from R = 2Ha and Σ_{v∈V}(−1)^{v·y} = |V|·1[y ∈ V^⊥].
2. Because R ≡ 8D (mod 16), the left side is ≡ 8·#{b ∈ a_0+V : D(b) = 1} (mod 16).
3. For v ∈ V, D(a_0 + v) = D(a_0) + D(v), and D|_V is linear. So that count is 0 or 4 if D|_V = 0, and exactly 2 otherwise. In every case it is even.
4. Hence 8·Σ_{x∈c+V^⊥} a(x)(±1) ≡ 0 (mod 16). The signed sum is therefore even, which is the stated parity.
5. U is a coset of V^⊥, the support of the Walsh transform of a quadratic with radical V. So the lemma applies to α. ∎

## 3. Corollary C — exact L formulas and parity

Combining (10) and (11), Γ = −6656 − 64L + 40d − 32u = 2εA_r(t − α − 2ν), gives:

| r | Exact formula for L | Consequence |
|---|---|---|
| 1 (d=192) | L = 32 − u/2 − 4α − 8ν | L ≡ 0 (mod 4) |
| 2, d=160 | L = 2α + 4ν − 36 − u/2 = 28 − u/2 − 2α − 4N_+ | L even; L ≡ 2α (mod 4) |
| 2, d=128 | L = 2α + 4ν − 56 − u/2 | L even; L ≡ 2α (mod 4) |
| 3 | L = 5d/8 − 40 − u/2 − α − 2ν | L even; L ≡ α + 2ν (mod 4) |
| 4 | L = 5d/8 − 232 − u/2 + α/2 + ν | parity NOT determined |

Details:

- **Rank 2.** By Theorem A, u/2 ≡ 0 (mod 4). With d = 160, L = 28 − u/2 − 2α − 4N_+, so L ≡ 2α (mod 4).
- **Rank 6.** Theorem A gives u/2 ≡ 2 (mod 4) at d = 112 and 144, and u/2 ≡ 0 (mod 4) at d = 128. Lemma B gives α even. Hence L is even. Since −α ≡ α (mod 4) for even α, also L ≡ α + 2ν (mod 4).
- **Rank 8.** Here α = w_R. Writing u = 6 + 8s at d = 120 and u = 2 + 8s at d = 136, L = ν − 110 − 5s or L = ν − 95 − 5s respectively.

**So L is even at every polar rank 2, 4 and 6.** At polar rank 2 this is consistent with the parent-supported rank-2 values L ∈ {16, 20, 24, 28}. This parity conclusion may coincide with an own unreviewed NONINPUT claim; it is derived here only from S0017, Theorem A and Lemma B.

**Windows with the admitted floors** (WRITTEN; no type is excluded):

- **(2,160):**
  - u ∈ {8, 16, 24, 32};
  - L ∈ {10, 12, …, 24} with L ≡ 2α (mod 4);
  - L + u/2 = 28 − 2α − 4N_+, so N_+ ≤ 3 and α ≤ 7.
- **(2,128):** L ≥ 4, and S0017 (13) gives 2L + u ≤ 16, so L = 4 and u = 8. S0017 §6 then excludes this OLD type at its own boundary; nothing new is claimed.
- **Rank 6:** L ≥ 8 and even. L + u/2 + α + 2ν = 30, 40 or 50, so L ≤ 28, 36 or 48 respectively.
- **Rank 8:** L + N_+ = 46 − 3s (d = 120) or 55 − 3s (d = 136), where N_+ = 256 − α − ν.

## 4. The (2,160) coset projection

Here D̄ is the bent weight-10 quotient form on F_2^8/V ≅ F_2^4, and A_D = U = V^⊥.

- c_ā = (−1)^{D̄(ā)}, and σ = q on V^⊥. Then Σ_x σ(x)(−1)^{ā·x} = 4c_ā.
- For each coset ā, k_ā, λ_ā and μ_ā count T = −28, −12 and 4 in ā.
- u_0 = B|_{V^⊥}, and s_ā = Σ_{x∈V^⊥} u_0(x)(−1)^{ā·x}. Fourier summation and the T census give

```
Σ_{b∈ā} S(b) = 32 s_ā,       Y_ā := 20 − 2c_ā s_ā = 3k_ā + 2λ_ā + μ_ā,
k_ā + λ_ā + μ_ā ≤ 16,        k_ā ≡ μ_ā (mod 2).                           (P1)
```

**Proposition D (exact projection of S0017 (3)).**

- Let g(ā) := Σ_{b∈ā} δ(b) = c_ā(λ_ā − μ_ā), and let h(x) := Σ_ā g(ā)(−1)^{ā·x} mod 3 for x ∈ V^⊥. Then u_0 ≡ σ − h (mod 3). Hence

  N_+ = #{h ≡ 0},  α = #{h ≡ σ},  ν = #{h ≡ −σ}.

- Let Σ := {ā : λ_ā ≢ μ_ā (mod 3)} = supp g. Then **L ≥ |Σ|**.
- If N_+ = 0, treat h as a ±1 integer function. Then u_0 = (h − σ)/2, so s_ā = (ĥ(ā) − 4c_ā)/2 and **Y_ā = 24 − c_ā ĥ(ā)**, where ĥ(ā) = Σ_x h(x)(−1)^{ā·x}.

*Proof.*

1. For x ∈ U, (3) gives B ≡ q − Hδ (mod 3), and (Hδ)(x) = Σ_ā g(ā)(−1)^{ā·x}.
2. B takes values in {0, ±1}, so B equals its residue: B = 0 where h ≡ σ, B = σ where h ≡ 0, and B = −σ where h ≡ −σ.
3. If h is never 0, then B = (h − σ)/2 pointwise. ∎

**Theorem E (at least four imbalanced cosets).** Use the admitted L ≥ 10 and Theorem A (u ≥ 8). Then |Σ| ≥ 4. If |Σ| = 4, then:

- Σ is an affine 2-flat a + W, with W = ⟨v_1, v_2⟩;
- the product of the g values on Σ is −1;
- N_+ = 0;
- either B̄(v_1, v_2) = 1, g = c on Σ, α = 4 and (L, u) ∈ {(12, 16), (16, 8)};
- or B̄(v_1, v_2) = 0, gc = −1 at exactly one point of Σ, α = 6 and (L, u) = (12, 8).

Here B̄ is the polar form of D̄. In both cases Y_ā = 24 off Σ, and Y_ā = 24 + 8c_ā g(ā) ∈ {32, 16} on Σ.

*Proof.* Write y_i := g(ā_i)(−1)^{ā_i·x} for the points ā_i of Σ. Recall that L + u/2 = 28 − 2α − 4N_+ (Corollary C).

**|Σ| = 0.** Then h ≡ 0, so N_+ = 16 and L + u/2 < 0. Impossible.

**|Σ| = 1**, Σ = {α*} and g(α*) = cε′ with c = c_{α*}.

1. h = cε′χ_{α*} is never 0, so N_+ = 0.
2. α = (16 + Σσh)/2 = 8 + 2ε′.
3. If ε′ = +1: L + u/2 = 8, so L ≤ 4 < 10. Impossible.
4. If ε′ = −1: α = 6 and L + u/2 = 16. So L = 12 and u = 8, because L is even with L ≥ 10 and u ∈ 8Z_{>0}.
5. ĥ(α*) = 16cε′, so Y_{α*} = 24 + 16 = 40.
6. But all 12 small values lie in α*, so λ + μ = 12 and k ≤ 4. Then 3k + 2λ + μ ≤ 12 + 24 = 36 < 40, contradicting (P1).

**|Σ| = 2.** h ≡ 0 iff y_1 = −y_2. That condition is one nontrivial character condition, so N_+ = 8 and L + u/2 ≤ 28 − 32 < 0. Impossible.

**|Σ| = 3.** h ≡ 0 iff y_1 = y_2 = y_3. The two conditions use the characters ā_1 + ā_2 and ā_2 + ā_3, which are distinct and nonzero, hence independent. So N_+ = 4. Then L + u/2 ≤ 12, and u ≥ 8 gives L ≤ 8 < 10. Impossible.

**|Σ| = 4.** h ≡ 0 iff two y_i are +1 and two are −1.

1. For four ±1 values, 1[Σy = 0] = 3/8 − e_2/8 + 3e_4/8, where e_2 = Σ_{i<j} y_i y_j and e_4 = Π y_i. (Check the cases 4+, 3+1−, 2+2−.)
2. Σ_x y_i y_j = 0 for i ≠ j, because the ā_i are distinct.
3. Σ_x e_4 = 16·G·1[Σā_i = 0], where G = Π g(ā_i).
4. Hence N_+ = 6 + 6G·1[Σā_i = 0] ∈ {0, 6, 12}.
5. N_+ ≥ 6 forces L + u/2 ≤ 4. Impossible. So N_+ = 0, Σā_i = 0 (Σ is an affine 2-flat) and G = −1.
6. Now Σ y_i = ±2 everywhere, so h = −(Σ_i y_i)/2 as a ±1 function. Then α = (16 + Σ_x hσ)/2 = 8 − Σ_i g(ā_i)c_{ā_i}.
7. L + u/2 = 28 − 2α ≥ 14 forces Σ g c ∈ {2, 4}.
8. Π(gc) = G·Πc = −(−1)^{ΣD̄(Σ)} = −(−1)^{B̄(v_1,v_2)}, since the sum of a quadratic over an affine 2-flat equals the polar value. So Σgc = 4 iff B̄(v_1,v_2) = 1, and Σgc = 2 iff B̄(v_1,v_2) = 0.
9. The values of (L, u) follow from L + u/2 = 28 − 2α with L even, L ≥ 10, L ≡ 2α (mod 4) and u ∈ 8Z_{>0}.
10. ĥ(ā) = −8g(ā) on Σ and 0 elsewhere, which gives the Y values. ∎

**R-side remark for |Σ| = 4** (WRITTEN; used only as a description of the remaining strata).

- Let Q = supp(a) ∩ V^⊥, so |Q| = α, and r_ā := (1/32)Σ_{b∈ā} R(b) = Σ_{x∈Q} a(x)(−1)^{ā·x}.
- On a D̄ = 1 coset with no |R| = 8 value, the coset census forces 3(n24^+ − n24^−) = 4r_ā, so r_ā ∈ 3Z.
- For α = 4 the values r_ā are even with |r_ā| ≤ 4, so r_ā = 0 on every such coset. Each D̄ = 1 coset with r_ā ≠ 0 therefore needs an |R| = 8 value. The count c = #{|p| = 1} = #{|R| = 8} satisfies c ≤ (u − 2)/2, because z ≥ 2.
- Computed instance: in the normal form a1a2 + a1 + a2 + b1b2, take Σ = {0, e_{a1}, e_{a2}, e_{a1} + e_{a2}}, where the signs c_ā are (1, −1, −1, −1), and take g(ā) = c_ā on Σ. Write V^⊥-points in dual coordinates x = (x1, x2, y1, y2). Then h = 1 exactly where (x1, x2) = (0, 0), and σ(x) = (−1)^{(1+x1)(1+x2) + y1y2}. So Q = {x : (y1, y2) = (1, 1)}, a 2-flat with α = 4.
  - If a|_Q has odd Boolean weight, its four Walsh values are all ±2, so r_ā ≠ 0 at all 10 D̄ = 1 cosets. That needs c ≥ 10, so u ≥ 22, contradicting u ∈ {8, 16}.
  - If a|_Q is ± a character, the instance survives this test.
- The full classification over all flats and both α values is NOT completed here.

## 5. Proposition F — exact ternary zero count of the small-value pattern at (2,160)

**Proposition F.** Let Z_3(δ) := #{x ∈ F_2^8 : (Hδ)(x) ≡ 0 (mod 3)}. Then

```
Z_3(δ) = 100 + L/2 + 3 N_+.
```

Equivalently, summing over even-size zero-sum subsets T ⊆ supp δ (T = ∅ included):

```
Σ_T (−3)^{|T|/2} δ(T) = 2^{L−9} (44 + 3L/2 + 9N_+).
```

*Proof.*

1. By (3), B ≡ q − Hδ (mod 3) everywhere, and q = 0 off U. So Hδ ≡ 0 exactly on (supp(a) ∖ U) ∪ {x ∈ U : B = q}. Hence Z_3 = (w_R − α) + N_+.
2. Insert w_R = 114 − u/4 and the relation u/4 = 14 − L/2 − α − 2N_+ (Corollary C).
3. For the second form use Z_3 = (1/3)(256 + 2 Re Σ_x ω^{(Hδ)(x)}) and the identity ω^{εχ} = −1/2 + (i√3/2)εχ for ε, χ = ±1. Expanding the product over supp δ, then summing characters, gives

   Σ_x ω^{Hδ} = 256 Σ_{ΣT=0} (−1/2)^{L−|T|} (i√3/2)^{|T|} δ(T).

4. Only even |T| contribute to the real part. Since L is even, each term equals 2^{−L}(−3)^{|T|/2}δ(T). ∎

**Consistency check.** Each term with |T| ≥ 4 is divisible by 9, so the left side is ≡ 1 (mod 9). The right side is ≡ 1 (mod 9) for every even L from 10 to 24; this was checked by hand from 2^{L−9}(44 + 3L/2) mod 9.

**Consequence (mod 27).** Let A_4 := Σ δ(T) over the affine 2-flats T ⊆ supp δ. Then

- A_4 ≡ 1 + 2N_+ (mod 3) for L ∈ {10, 12, 16, 18, 22, 24};
- A_4 ≡ 2N_+ (mod 3) for L ∈ {14, 20}.

For example, in the extremal stratum (N_+ = α = 0, L ∈ {16, 24}), supp δ must contain affine 2-flats.

Z_3 is far above the generic value 256/3 ≈ 85.3, because 100 + L/2 ≥ 105. So the small-value pattern of every (2,160) target is strongly additively structured. This is a necessary condition, not an exclusion.

## 6. Scope

**Proved (WRITTEN, from the admitted S0017 cut):**

- Theorem A, Lemma B and Corollary C;
- Proposition D;
- Theorem E: at least four imbalanced cosets, the |Σ| = 4 structure, and in particular exclusion of the one-coset stratum (correcting the v1 Corollary 4.4(b), which stopped at L = 12);
- Proposition F and its mod-27 consequence.

**Not proved:**

- the |Σ| = 4 strata in general, and every |Σ| ≥ 5;
- the full (2,160), rank-6 and rank-8 types;
- the (24,24,2) gap and the original problem, which remain OPEN.

No numerical nonlinearity, witness or global claim is made. Novelty and priority are UNCLEARED. Adoption requires a fresh, entire review.

All earlier own, parent and reviewer findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR and the attribution erratum `global-exact-occupancy-identity-attribution-erratum-v1.md`. Same 18 owners, OWN root and HOLD. Science cutoff 2026-10-27T11:05:38-07:00; deadline 12:35:38. No early park.
