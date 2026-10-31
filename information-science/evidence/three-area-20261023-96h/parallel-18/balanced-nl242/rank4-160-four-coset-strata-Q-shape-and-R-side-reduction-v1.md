# Balanced NL242 (2,160) — the four-imbalanced-coset strata: shape of Q and R-side reduction

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 06:59:01 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is not reviewed or adopted. It is not machine-checked, formal, kernel-checked, executed or novelty-cleared. No interpreter, Eval, CAS, enumeration, solver, CLI, nested agent or GO was used; all arithmetic was done by hand in writing.

This packet narrows the strata that Theorem E of `u-class-L-parity-and-rank4-160-coset-projection-v1.md` (SHA `7cecd509…0c9b`) leaves at |Σ| = 4. It **excludes neither stratum**. The (2,160) type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Inputs and notation

The inputs are those of the parent packet `u-class-L-parity-and-rank4-160-coset-projection-v1.md`, all admitted at their cuts:

- S0017 (3), (5)–(13);
- the Gate II floor L ≥ 10;
- its own Theorems A and E, Proposition D and Corollary C.

The NONINPUT list is unchanged.

**Notation.**

- Σ = a + W = {ā_1, …, ā_4} is the imbalanced affine 2-flat, with W = ⟨v_1, v_2⟩.
- g(ā_i) = ±1 and G = Π g(ā_i) = −1.
- On V^⊥ ≅ F_2^4: h = −(1/2) Σ_i g(ā_i) χ_{ā_i}, and σ = (1/4) Σ_b c_b χ_b. Both are ±1-valued.
- Q := {h = σ} = supp(a) ∩ V^⊥, so |Q| = α.
- The R-side array a restricted to V^⊥ is written a_0. It is ±1 on Q.
- r_ā := Σ_{x∈Q} a_0(x)(−1)^{ā·x} = (1/32) Σ_{b∈ā} R(b).
- c := #{|R| = 8}, with u = z + 2c.

## 1. Q-shape lemma

**Lemma 1.** For every ā,

```
Ŵ(1_Q)(ā) = 8·[ā = 0] − Σ_i g(ā_i) c_{ā+ā_i},
Π_i g(ā_i) c_{ā+ā_i} = −(−1)^{B̄(v_1,v_2)}.
```

Consequently:

- **α = 4, i.e. B̄(v_1,v_2) = 1:** Q is an affine 2-flat.
- **α = 6, i.e. B̄(v_1,v_2) = 0:** Q is a zero-sum 6-set. It contains no zero-sum 4-subset and lies in no affine 3-flat.

*Proof.*

1. 1_Q = (1 + hσ)/2. The product hσ = −(1/8) Σ_{i,b} g_i c_b χ_{ā_i+b}, and summing characters gives the first formula.
2. {ā + ā_i} is a translate of the flat a + W. The sum of the quadratic D̄ over any translate of a 2-flat with direction W equals B̄(v_1, v_2). Hence Π_i c_{ā+ā_i} = (−1)^{B̄(v_1,v_2)}, and G = −1 gives the second formula.
3. **B̄ = 1.** The four signs have product +1, so they split 4–0 or 2–2. Every value Ŵ(1_Q)(ā) with ā ≠ 0 lies in {0, ±4}, which is ≡ |Q| (mod 4). That holds iff every functional has even size on Q, i.e. ΣQ = 0. A zero-sum 4-set is an affine 2-flat.
4. **B̄ = 0.** The product is −1, so the split is 3–1, Ŵ = ±2 ≡ 6 (mod 4), and again ΣQ = 0.
5. If T ⊂ Q has |T| = 4 and ΣT = 0, then Q ∖ T consists of two points with zero sum, i.e. two equal points. Impossible.
6. Every affine k-flat with k ≥ 2 has zero sum. If Q lay in an affine 3-flat, its two complementary points would therefore be equal. ∎

## 2. Walsh census of a_0 (exact counting identities)

**Four points on a 2-flat.** Either a_0 is ± a character on Q, and then |r| = 4 on exactly one coset K of the 2-dimensional annihilator Q_lin^0 and r = 0 elsewhere; or a_0 has odd Boolean weight, and then |r| = 2 at all 16 points.

**Six points.** For six ±1 values y_i the indicators are

- 1[Σy = 0] = (5 − e_2 + e_4 − 5e_6)/16;
- 1[|Σy| = 6] = (1 + e_2 + e_4 + e_6)/32.

These were checked on all splits (6,0), (5,1), (4,2) and (3,3). Put y_i = a_0(q_i)χ_ā(q_i) and sum over ā; Σ_ā e_2 = 0 because the points are distinct. This gives

```
n_0 := #{r = 0} = 5 + A_4(Q) − 5ε_Q,      n_6 := #{|r| = 6} = (1 + A_4 + ε_Q)/2,
```

where A_4(Q) = Σ a_0(T) over zero-sum 4-subsets T ⊆ Q, and ε_Q = 1[ΣQ = 0]·Π_Q a_0.

## 3. R-side admissibility

On a coset with D̄ = 1 and no |R| = 8 value, every R value is ±24. Hence 3(n24^+ − n24^−) = 4r_ā, and **r_ā ∈ 3Z**. So every D̄ = 1 coset with r_ā ∉ 3Z contains an |R| = 8 value, which forces c ≥ #{ā ∈ A1 : r_ā ∉ 3Z}. Also z ≥ 2, so c ≤ (u − 2)/2.

**Theorem 2 (reduction of both |Σ| = 4 strata).**

**(α = 4)**, with (L, u) ∈ {(12, 16), (16, 8)}:

- Q is an affine 2-flat and a_0 is ± a character on Q.
- r = ±4 exactly on one coset K of Q_lin^0, and r = 0 elsewhere.
- Every D̄ = 1 coset in K contains an |R| = 8 value.
- If (L, u) = (16, 8), then c ≤ 3 and K ⊄ A1.

*Proof.* If a_0 has odd weight, |r| = 2 on all ten D̄ = 1 cosets, so c ≥ 10 and u ≥ 22. That is impossible because u ≤ 16. ∎

**(α = 6)**, with (L, u) = (12, 8), so c ≤ 3 and z = 8 − 2c:

- ΣQ = 0, A_4 = 0 and Π_Q a_0 = −1.
- r ∈ {0, ±4}, with exactly six nonzero cosets N.
- #(N ∩ A1) ≤ c ≤ 3, so #(N ∩ A0) ≥ 3.

*Proof.* Lemma 1 gives ΣQ = 0 and A_4 = 0. Suppose Π_Q a_0 = +1. Then n_0 = 0 and n_6 = 1, and Parseval (Σr² = 96) leaves fifteen values with |r| = 2. Then at least nine D̄ = 1 cosets have r ∉ 3Z, so c ≥ 9. Impossible. Hence Π_Q a_0 = −1, so n_0 = 10 and n_6 = 0. Parseval then forces the six nonzero values to be ±4. ∎

**Both α = 6 Q-shapes occur in principle.** The relation space of Q is {0, 1⃗, d, d + 1⃗} with wt(d) ∈ {1, 3, 5}.

- **(3,3):** Q = (P_1 ∪ P_2) ∖ {0}, where F_2^4 = P_1 ⊕ P_2. Then N = ā* + ((P_1^0 ∪ P_2^0) ∖ {0}), a "cross". The centre ā* can be placed at any point by choice of signs.
- **(1,5):** Q = {0} ∪ (a frame f_1, …, f_4, Σf_i). Then N − ā_0 = {0, 1111, 0111, 1011, 1101, 1110} in frame-dual coordinates.

**Hand-computed instance (does NOT exclude the stratum).**

- Normal form D̄ = [a ≠ 0] + b1b2. Take Σ = ⟨e_{a1}, e_{b1}⟩, c = (1, −1, 1, −1), and the special point 0.
- Then Q = {0100, 0101, 0110, 0011, 1010, 1110}, which splits as {0100, 1010, 1110} ∪ {0101, 0110, 0011}. This is shape (3,3).
- Take a_0 = +1 on the first triple and −1 on the second. Then N = {1010, 0001, 1011, 1000, 0111, 1111}, and N ∩ A1 = {1010, 1000}.
- So c ∈ {2, 3}, and this instance passes every test above.

## 4. Status and first unproved step

**WRITTEN:** Lemma 1, the census identities of §2 and Theorem 2. These are exact necessary conditions.

**Not proved:** the exclusion of either |Σ| = 4 stratum; any |Σ| ≥ 5 case; the whole (2,160) type.

**First unproved step.** Use the 15 other V^⊥-cosets (slices η ≠ 0). There u ≡ −Hδ (mod 3), so supp(a) on slice η is {x : Σ_ā g_η(ā) χ_ā(x) ≡ 0}, where g_η(ā) = Σ_{b∈ā} δ(b)(−1)^{b·η}. These must be combined with the per-row R and S censuses. All this data is fixed by the four signed small-value sets inside the cosets of Σ, together with the remaining λ ≡ μ cosets.

Novelty and priority are UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR and the own attribution MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 2026-10-27T11:05:38-07:00; no early park.
