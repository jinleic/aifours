# Referee report: Slice A (Theorem SEG after I.12, Part II, SEG‑p, SEG‑num with I.13)

**Text of record.** v5 `4e463746…cff1c`, read through errata 1–4 and erratum 5 (`40832206…4f85`), as supplied. I did not re-hash the files.

**Method.** Hand checks only: no tools, no computation, no edits, no delegation. W, Lemma 2.1, Facts 2.1/2.2, ARC+, Lemma SEG, Lemmas 3.1/3.2, BAL and the e5 rule are taken as stated with the erratum‑5 repairs; they were not re-audited.

## 1. Disposition

**Slice A overall: 0 FATAL / 0 MAJOR / 1 MINOR. No REJECT.**

| Target | Verdict | FATAL/MAJOR/MINOR | Minimal repair |
|---|---|---|---|
| Theorem SEG, Π_need ≥ 1 (I.12 clipped loop) and Π_need = 0 | ACCEPT‑WITH‑FIXES | 0/0/1 | S1: one-sentence documentation fix in e5 |
| Part II, R ≥ 2p+1 (Π_need < 0) | ACCEPT | 0/0/0 | none; cosmetics C3 optional |
| Corollary SEG‑p | ACCEPT | 0/0/0 | none |
| Corollary SEG‑num + I.13 (inactive max, integer ranges) | ACCEPT | 0/0/0 | none |

### Decision: Part II versus erratum 4

**Part II proves the printed Theorem SEG for R ≥ 2p+1 from (H1) and (H2) alone.**
- (H3) is vacuous there, since Π_need + 1 ≤ 0 ≤ g_E.
- Together with I.12, the printed theorem holds for every w in (S):
  - Π_need ≥ 1: the I.12 loop. This is the only branch that uses H3.
  - Π_need = 0: I.12.
  - Π_need < 0: Part II.

**Status of erratum 4.**
- Its narrowing is not mathematically needed.
- It remains true as a weaker statement.
- Its finding remains correct: the v5 proof text alone does not cover Π_need < 0.
- Under erratum 5 §0, switching away from erratum 4 needs a parent verdict. This review is the second-family review §0 asks for, and it recommends the switch.

**Codex findings.**
- The Codex MAJOR (negative budget) is closed by Part II without narrowing.
- The Codex MINOR (clipped gain) is closed by I.12.

**Downstream effect.** No application changes: SEG‑p, MID and SEG‑num all have Π_need ≥ 1. MID, TOP and the R = p table use no SEG statement that changes, so they were not reviewed.

### Finding

**S1 (MINOR; e5 as read under I.7, about SEG's use).**

e5 says SEG's explicit change rule "is a special case" of the e5 realisation rule. It is not:
- Removing a whole AB pair-arc, or adding an AB pair-arc as one arc, is none of e5's three moves (delete a singleton, add a singleton on an unused block, split a pair).
- I.7's rereading still names only those three moves.

The SEG proof is unaffected, because its rule is self-contained:
- In SEG every c_j is 0 or 1.
- Each move deletes or adds the unique base arc of M_j.
- This flips the parity of c_j, changes the arc count by ±1, and keeps at most one arc per M_j. That is all BAL needs.

*Repair:* in e5 replace "(… is a special case)" with "(… toggles c_j ∈ {0,1} by deleting or adding the unique base arc of M_j; the e5 moves are not used)". The same sentence covers MID, which is out of scope here.

### Cosmetic notes (not findings)

- **C1 (I.12).** "At most Π_need − G_b steps" should read "at most max(0, Π_need − G_b) steps".
- **C2 (SEG‑p, (H2)).** The printed "iff κ ≤ (p−3)/2" governs only the middle link of the chain.
- **C3 (Part II).**
  - The letters a, b, c reuse a_t, b_t (and v5's b_i) and c_i. Rename them, e.g. a*, b*, c*.
  - At "κ+1 ≤ p", cite H ≥ 0.
  - State that γ_m(E±) ≥ 1, so the window has exactly γ₊ + γ₋ + 1 integers.
- **C4 (SEG‑num, (H2)).** After I.13 gives m_lo ≥ 2, the max(4, ·) branch is never used.
- **C5 (I.14, last clause).** "Satisfy the hypotheses of Theorem SEG" inherits whichever SEG version governs. After the switch it also includes R ≥ 2p+1 words that meet the printed H1–H2. No universal band changes.

### Repairs that change how a foundation lemma is used in Slice A

- **I.3.** It replaces the v5 remark that SEG's "lower the t_j minimally" step relied on. I.12 is the matching repair; checked in A4.
- **I.7/e5.** See S1.
- **I.1, I.2, I.4, I.5, I.6.** All consistent with the use made here:
  - several segments may sit in one gap;
  - the base has at least 2 arcs;
  - classes are read via |M_i|;
  - parities are invariant under segments, and the m-range is monotone;
  - q ≥ n_CA ≥ 4.
- **I.8.** Its hypotheses (w avoids, R = p) hold where SEG‑p and I.13 (δ = 0) use the Sec. 4 data.
- **I.9–I.11 (K2P+, IIIb‑X, ETA).** Not used. SEG's "as in K2P+ (g)" reuses an argument, which A2 redoes directly; it is not a dependency.

## 2. Proof checks

### A. Theorem SEG for Π_need ≥ 0 (v5 + e1 + I.12)

**A1. Base and balancing.**
- Choose O_0 ⊆ C ∪ AB with |O_0| = N_O = 2m_lo+2, using H2.
- Each arc is either the single block of M_i (C, ν = 1) or M_i as one pair-arc (AB). The pair's internal run is empty and genuine, so ν = 2.
- There is one arc per M_i, so the arcs are disjoint and have empty internal runs.
- Apply BAL at i ∈ O_0 with SEG's toggle (I.6, S1):
  - If |T| ≤ d already, then |O| = N_O.
  - Otherwise i loses its arc, and i′ ≠ i loses or gains one.
- Result: |O| ∈ {N_O−2, N_O}, m_b ∈ {m_lo, m_lo+1}, and |O| ≥ 2m_lo ≥ 2, so the base is an arc system.
- L ∩ O_0 = ∅, so |L ∩ O| ≤ 1. Also |T| ≤ d. ✓

**A2. The floor window holds on [m_lo, m_hi].**
- Lower condition: ⌈E_min/2⌉ ≥ ⌈(R−d)/4⌉ ≥ κ+1−m_lo ≥ κ+1−m. The middle step holds in both branches, since max(1, x) ≥ x.
- Upper condition: ⌊E_max/2⌋ ≤ ⌊(R+d)/4⌋ = p−m_hi ≤ p−m.
- Segments insert an even number of singletons inside one M_j. So the parities, z, T and E± are those of the base (I.5).
- By Fact 2.1, γ_m(E±) = ⌊E±/2⌋ for every m in [m_lo, m_hi]. ✓

**A3. Segments and capacity.**
- The segments are:
  - M_j for j ∈ (AB ∪ L) ∖ O, with b′ ≥ 2;
  - M_j minus its first block for j ∈ L ∩ O, with b′ = e_j ≥ 2.
- They are pairwise disjoint, disjoint from the base, and each lies in one base gap (I.1 handles several segments in one gap).
- Saturated capacity, using e = 0 on C:
  G_b + Σ_j (b′_j − 1) = |AB∩O| + |AB∖O| + Σ_{L∖O} e_j + Σ_{L∩O} (e_j − 1) = g_E − |L∩O|.
- By H3 and |L ∩ O| ≤ 1, this is ≥ Π_need. The identity also covers the case of no segments. ✓

**A4. The I.12 loop for Π_need ≥ 1.** Since w avoids, R ≥ p (Fact 2.2), so Π_need ≤ (p−1)/2.
- **A raisable j exists.** Suppose the certified gain is < Π_need and every t_j is saturated. Then each g_j = min(p−1, b′_j−1). Either some g_j = p−1 ≥ Π_need, or the gains sum to the A3 capacity, which is ≥ Π_need. Both contradict the loop condition.
- **Each step adds at least 1.** Before the step, g_j ≤ gain < Π_need ≤ (p−1)/2, and 2t_j < b′_j−1. So g_j = 2t_j ≤ p−2. After it, min(p−1, 2t_j+2, b′_j−1) ≥ 2t_j+1.
- **Realisability.** t_j is raised only from 2t_j ≤ b′_j−2, so t_j ≤ ⌊b′_j/2⌋ always.
- **Bound on m.** There are at most max(0, Π_need − G_b) steps, so Σt_j ≤ Π_need. Every m in [m_b, m_b+Σt_j] then lies in [m_lo, m_lo+1+Π_need] ⊆ [m_lo, m_hi], by H1.
- **Closing.** f₊ + f₋ ≥ ⌈R/2⌉ − 1, since E₊ + E₋ = R. Adding the certified gain gives ≥ p − 1. Lemma 3.2 then applies, via ARC+ (iii), Lemma 2.1 and Lemma W with β = 0. ✓

**A5. Π_need = 0, i.e. R ∈ {2p−1, 2p}.**
- Set every t_j = 0.
- H1 gives m_hi ≥ m_lo+1, so m_b lies in [m_lo, m_hi].
- f₊ + f₋ ≥ p − 1 and the gain is ≥ 0, so Lemma ARC closes the case. H3 is not used. ✓

**A6. Π_need < 0.**
- v5 + I.12 give nothing here: Σt_j ≤ Π_need < 0 is impossible, and H1 allows m_hi < m_lo.
- Erratum 4 covers this case in narrowed form; Part II covers it as printed.

### B. Part II

Notation: ℓ = m_lo, c = ⌈R/2⌉ ≥ p+1, a = ⌈(R−d)/4⌉, b = ⌊(R+d)/4⌋.

- **B1.** H1 reads (p−b) − ℓ ≥ (p−c) + 1, i.e. c − b ≥ ℓ+1. ✓
- **B2 (a + b ≥ c − 1).**
  - a ≥ (R−d)/4.
  - b ≥ (R+d−3)/4, because R+d is an integer.
  - So a + b ≥ R/2 − 3/4.
  - For R even this gives a + b ≥ R/2 = c; for R odd, a + b ≥ (R−1)/2 = c−1. ✓
- **B3.** a ≥ c − 1 − b ≥ ℓ, by B1 and B2. ✓
- **B4 (ℓ ≤ (p−1)/2 in both branches of the max).**
  - If κ+1−a ≤ 1, then ℓ = 1 ≤ (p−1)/2.
  - Otherwise ℓ = κ+1−a ≥ 2, and B3 gives ℓ ≤ κ+1−ℓ. So 2ℓ ≤ κ+1 ≤ p (using H ≥ 0), and ℓ ≤ (p−1)/2 since p is odd. ✓
- **B5 (base).** Build the base as in A1 with N_O = 2ℓ+2 (H2) and add no segments. Then m ∈ {ℓ, ℓ+1} ⊆ [1, (p+1)/2], |T| ≤ d, and there are at least 2 arcs. ✓
- **B6.**
  - f₊ + f₋ ≥ c − 1 ≥ p.
  - max f± = ⌊E_max/2⌋ ≤ b, since E_max ≤ (R+d)/2.
  - min f± ≥ c − 1 − b ≥ ℓ ≥ m − 1. ✓
- **B7 (Fact 2.1 lower condition).**
  - ⌈E_min/2⌉ ≥ a ≥ κ+1−ℓ ≥ κ+1−m, since ℓ ≥ κ+1−a in both branches.
  - Equivalently, E − κ + m − 1 ≥ ⌊E/2⌋ for E = E±.
  - Hence γ_m(E±) = min(p−m, f±).
  - The upper condition can fail, so the clipped form is really needed. ✓
- **B8 (clipped endpoint sum).**
  - Σ min(p−m, f±) ≥ min(2(p−m), (p−m) + min f±, f₊ + f₋).
  - The three terms are bounded by p−1 (using m ≤ (p+1)/2), p−1 (using min f ≥ m−1) and p, respectively, so the sum is ≥ p − 1.
  - Both endpoints are ≥ 1, since p−m ≥ (p−1)/2 and f± ≥ ℓ ≥ 1.
  - So the window [−γ_m(E₋), γ_m(E₊)] has at least p integers and covers every residue. ✓
- **B9 (Lemma 2.1 and Lemma W).**
  - Take any a_i ∈ X_i and b_i ∈ Y_i. The resulting P is proper, with m(P) = m exactly and E±(P) = E± (Lemmas 2.1 and 3.1).
  - With β = 0, I(P) is exactly this window, so it contains u_P.
  - Lemma W gives an identity 2p-subword. No Cauchy–Davenport or ARC+ step is needed. ✓
- **B10.** H3 is vacuous and not used. ✓
  - Optional remark: B1–B9 also cover Π_need = 0. With c = p, f₊ + f₋ ≥ p − 1 suffices.
- **B11 (shape example: p = 11, R = 25, κ = 10, d = 3, q = 13; 9 C-runs and 4 AB-runs).**
  - Structure: k = 2p − R + 2κ = 17 = 9 + 2·4; H = 0, F = 17, F + R = 42 = 4p − 2; g_E = 4.
  - Parameters: a = 6, b = 7, c = 13, so m_lo = 5, m_hi = 4, Π_need = −2.
  - Hypotheses: H1 is −1 ≥ −1 (equality); H2 is 13 ≥ 12; H3 is 4 ≥ −1.
  - Necessary conditions for avoiders all hold:
    - 4 ≤ B ≤ κ (from A ≤ 2p−1 and Z0);
    - d ≤ 2(R−p) + 1;
    - κ ≤ o_F − 1.
  - No avoidance is claimed, as the text says.
  - Part II is tight on this example:
    - ℓ = 5 = (p−1)/2.
    - At m = 6, both (E₊, E₋) = (13, 12) and (14, 11) give γ₆ = (5, 5), a window of exactly 11 = p integers.
  - The floor window does fail here, e.g. at m = 5 with |T| = 3, ⌊14/2⌋ = 7 > p − m = 6. This matches the remark.
  - Erratum 4's example (p = 11, κ = 8, k = 12, R = 26) is consistent at parameter level: 2p − k + 2κ = 26, Π_need = −2, and 5 ≤ B ≤ 8 is possible. ✓

### C. SEG‑p

- **C1.** For an avoider with R = p, Fact 2.2 gives:
  - every run has at most one letter;
  - q = p, k = p + 2κ, g_E = 2κ, d = 1;
  - r = ⌈(p−1)/4⌉ = ⌊(p+1)/4⌋.
- **C2.** κ + 1 − r ≥ 1:
  - for p = 4a+1, r = a and κ ≥ a+1;
  - for p = 4a+3, r = a+1 and κ ≥ a+1.
  So m_lo = κ+1−r, m_hi = p−r, and Π_need = (p−1)/2 ≥ 2. Only I.12's Π_need ≥ 1 branch is used; Part II and erratum 4 are irrelevant here. ✓
- **C3 (H1).** m_hi − m_lo = p−1−κ ≥ (p+1)/2 ⟺ κ ≤ (p−3)/2. ✓
- **C4 (H2).**
  - |L| ≤ g_E/2 = κ, so n_CA ≥ p − κ.
  - We need p − κ ≥ 2κ + 4 − 2r, i.e. 3κ ≤ p − 4 + 2r.
  - From κ ≤ (p−3)/2, 3κ ≤ (3p−9)/2, and (3p−9)/2 ≤ p − 4 + 2r ⟺ 4r ≥ p − 1. ✓
- **C5 (H3).** 2κ ≥ (p+1)/2 ⟺ κ ≥ (p+1)/4. ✓
- **C6 (spot checks and ambient conditions).**
  - p = 7, κ = 2, which has m_lo = 1 at the edge of the max: H1 is 4 ≥ 4, H2 is ≥ 5 ≥ 4, H3 is 4 ≥ 4.
  - p = 13, κ = 5: H2 is tight, 8 ≥ 8.
  - The κ-range is empty at p = 5.
  - F ≥ 1 is automatic, since F = 0 would force R = 4p − 2.
  - Normalisation keeps R, κ and the blocks. ✓

### D. SEG‑num with I.13

- **D1.** For an avoider: d ≤ 2δ+1, q ≥ 2p − R = p − δ, q ≤ R, and k = p − δ + 2κ. ✓
- **D2 (I.13: the max is inactive).**
  - δ ≥ 1: κ ≥ (R + 2δ + 2)/4 ≥ R/4 + 1, so κ ≥ ⌈R/4⌉ + 1 ≥ ⌈(R−d)/4⌉ + 1.
  - δ = 0: d = 1, and ⌈(p+2)/4⌉ = r + 1 in both residue classes mod 4.
  - So m_lo = κ + 1 − ⌈(R−d)/4⌉ ≥ 2.
  - Withdrawing "(or more if m_lo = 1)" is correct: taking max(1, ·) can only shrink m_hi − m_lo. ✓
- **D3 (H1).**
  - m_hi − m_lo = H − (⌊(R+d)/4⌋ − ⌈(R−d)/4⌉) ≥ H − ⌊d/2⌋ ≥ p − 1 − κ − δ.
  - p − 1 − κ − δ ≥ (p−δ)/2 + 1 ⟺ κ ≤ (p−δ−4)/2.
  - (p−δ)/2 + 1 ≥ ⌊(p−δ)/2⌋ + 1 = Π_need + 1. ✓
- **D4 (H3).** g_E = k − q ≥ k − R = 2κ − 2δ ≥ (p−δ)/2 + 1 ⟺ κ ≥ (p+3δ+2)/4. ✓
- **D5 (H2).**
  - n_CA ≥ (3q − k)/2 ≥ p − δ − κ.
  - 2m_lo + 2 = 2κ + 4 − 2⌈(R−d)/4⌉ ≤ 2κ + 4 − (p−δ−1)/2, since R − d ≥ p − δ − 1.
  - p − δ − κ ≥ 2κ + 4 − (p−δ−1)/2 ⟺ κ ≤ (p−δ−3)/2, which holds. ✓
- **D6 (Π_need ≥ 1).** 5δ ≤ p − 10 gives R ≤ (6p − 10)/5 ≤ 2p − 2. Only I.12's Π_need ≥ 1 branch is used. ✓
- **D7 (exact integer coverage).**
  - The covered band is ⌈(p+3δ+2)/4⌉ ≤ κ ≤ ⌊(p−δ−4)/2⌋. This matches the I.14 row.
  - The band is nonempty over the reals ⟺ 5δ ≤ p − 10. That condition is only necessary for an integer cell: at p = 11, δ = 0 the band is [4, 3], and SEG‑p covers κ ∈ {3, 4} instead.
  - At δ = 0, SEG‑num ⊆ SEG‑p.
  - k ≡ R (mod 2) and k ∈ [(3p+δ+2)/2, 2p−2δ−4].
  - The first cell with δ ≥ 1 is p = 17, δ = 1, κ = 6, k = 28. A direct SEG check at d = 3 gives m_lo = 3, m_hi = 12, Π_need = 8, and H1 9 ≥ 9, H2 ≥ 10 ≥ 8, H3 ≥ 10 ≥ 9. ✓

## 3. Not reviewed; open

**Not reviewed:**
- the foundation lemmas (as instructed);
- K2P+, FP/FP‑1, ETA, MID, TOP;
- the R = p table in I.14;
- the SEG‑k, transfer and region‑B files.

**OPEN:** REFL(p), REFL‑HI(p), RES‑HI(p), the reflection half of INV*(p), INV*(p), and ordered Olson for D_2p. The separately accepted sequence-level Olson cells are unrelated. No novelty, priority or Lean claim is made.
