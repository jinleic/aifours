# Balanced NL242 (3,112) at L = 14 — the case s = 12 is excluded (the balanced coset p cannot be consistent in both p-active slices)

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:45:30 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L14-parity-parseval-s10-s12-v2.md` (ab790de4…c204). It covers the residue type (polar rank 6, weight 112) at L = 14 only. **L = 14 is still NOT excluded**, because s = 13 and parts of s = 14 remain open.

## 0. Setting

By v2 Theorem P12 and fc201185, s = 12 at L = 14 forces:

- τ := ΣΣ = 0 and G = +1;
- dim aff(Σ) = 5, so Σ ⊆ Π_5 = a + W_5 with W_5 = ω^⊥;
- since L = 14 = 12 + 2, every Σ-coset carries exactly one small value, and P = Σ ∪ {p} with p a balanced (1,1) coset;
- p ∉ Π_5, because dim aff(P) = 6 (Theorem M(a)).

**Slice data.** These come from the consolidated proof 6c5ce361, §1 and Lemmas O and SV.

- T := χS, and χ = c_ā on the coset ā, so 8υ_η(ā) = c_ā Σ_β T(ā,β)(−1)^{β·η}.
- g_η(x) = ±1 for x ∈ Σ.
- p has −12 at β^λ and 4 at β^μ, and values t_3, t_4 ∈ {−28, 20} at the other two positions β_3, β_4. p is active (g_η(p) = ±2 ≡ ∓1 mod 3, with reduced sign ε_p) exactly in the two slices η_1, η_2 with d_p·η = 1, where d_p := β^λ + β^μ. It is inactive at η_0 = η_1 + η_2.
- Classes: Ψ_η(ξ) := Σ_{x∈Σ} g_η(x)(−1)^{x·ξ}. This satisfies Ψ_η(ξ + ω) = ±Ψ_η(ξ), so 3 | Ψ_η is a property of the 32 classes ζ ∈ F_2^6/⟨ω⟩. Let m_η be the number of classes with 3 ∤ Ψ_η, and S_η that set of classes.

## 1. Slice values on the p-half

Take a p-active slice η, so |P_η| = 13, and a coset ā = p + v with v ∈ W_5.

1. Every odd T ⊆ P_η with ΣT = ā contains p, with T = {p} ∪ E, E ⊆ Σ even and ΣE = v.
2. Lemma Φ with s = 13 gives b_{|E|+1} = 2^{−12}(−3)^{|E|/2}. Hence
   ```
   υ_η(p + v) = −(ε_p/64) Λ_η(v),   Λ_η(v) := Σ_{E⊆Σ even, ΣE=v} (−3)^{|E|/2} g_η(E).
   ```
3. Character sums over W_5, using Π_x(1 + i√3 y_x) = 2^{12} e^{iπΨ/3} with even part 2^{12} cos(πΨ/3), give
   ```
   Λ_η(v) = 128 Σ_ζ (−1)^{ζ·v} cos(πΨ_η(ζ)/3).
   ```
   Here Ψ_η is even, so cos(πΨ_η/3) = 1 if 3 | Ψ_η and −1/2 otherwise.
4. Therefore:
   - **(1a)** for v ≠ 0: υ_η(p + v) = 3ε_p F_η(v), with F_η(v) := Σ_{ζ∈S_η} (−1)^{ζ·v};
   - **(1b)** υ_η(p) = ε_p(3m_η − 64).

   Check of (1b): Λ_η(0) = Σ_{r∈R} (−3)^{|r|/2} g_η(r) = 96N_η − 2048, by Lemma Φ(ii) summed over ξ. With N_η = 2(32 − m_η) this is 4096 − 192m_η, which agrees.

## 2. Three constraints

**(C1) m_η ≡ 0 (mod 4) in both p-active slices.**

1. The 31 cosets p + v with v ≠ 0 are pure, since P ∩ (F_2^6 ∖ Π_5) = {p}.
2. At η_0, P_{η_0} = Σ and OddSums(Σ) ⊆ Π_5, so υ_{η_0}(p + v) = 0 by Lemma O.
3. By Lemma SV the triple is then (0,0,0) or a single ±12. So 3F_η(v) ∈ {0, ±12}, i.e. F_η(v) ∈ {0, ±4}.
4. Parseval on F_2^5 gives m_η² + Σ_{v≠0} F_η(v)² = 32m_η. So m_η² ≡ 0 (mod 16), and m_η ≡ 0 (mod 4).

**(C2) m_η ≠ 20 in every slice.** τ = 0, so w_η has constant parity G_η by Lemma PP(a), and Σ_classes Ψ_η² = 384. Let j be the number of classes with |Ψ_η| = 10.

- If G_η = −1: Ψ_η ∈ {±2, ±6, ±10}, and the classes with 3 | Ψ_η have |Ψ_η| = 6. Then 36(32 − m) + 4(m − j) + 100j = 384, i.e. 32m = 768 + 96j, so m = 24 + 3j ∈ {24, 27, 30}.
- If G_η = +1: Ψ_η ∈ {0, ±4, ±8, ±12}, with m = m_4 + m_8. Then 16m_4 + 64m_8 + 144m_12 = 384, i.e. 16m + 48m_8 + 144m_12 = 384. For m = 20 this would need 48m_8 + 144m_12 = 64, which is impossible (64 is not a multiple of 48 or of 144, and 48 + 144 > 64). The admissible values are m ∈ {3, 6, 9, 12, 15, 18, 21, 24}.

In particular **m = 20 is impossible in either parity.**

**(C3) The T-row of p.** In a p-active slice, (−1)^{β^μ·η} = −(−1)^{β^λ·η}. Also β_3 + β_4 = d_p, so the characters at β_3 and β_4 are opposite. Hence

```
8|υ_η(p)| = |−16 + (−1)^{(β_3+β^λ)·η} Δ|,   Δ := t_3 − t_4 ∈ {0, ±48}.
```

Since β_3 + β^λ ∉ {0, d_p}, we have (β_3 + β^λ)·η_0 = 1, so the sign (−1)^{(β_3+β^λ)·η} differs between η_1 and η_2. Therefore:

- if Δ = 0, then {|υ_{η_1}(p)|, |υ_{η_2}(p)|} = {2, 2};
- if Δ = ±48, then {|υ_{η_1}(p)|, |υ_{η_2}(p)|} = {4, 8}.

## 3. Theorem P12′: s = 12 is impossible at L = 14

By (1b), |υ_{η_j}(p)| = |3m_j − 64|. By (C1) this is ≡ 0 (mod 4), which excludes {2, 2}. So {m_1, m_2} = {20, 24}, since |3m − 64| = 4 forces m = 20 and = 8 forces m = 24. But (C2) excludes m = 20. Contradiction. ∎

Together with v2 Theorem P12: **s = 12 is impossible at L = 14 at (3,112).**

## 4. Open list at (3,112), L = 14 (updated)

- **s = 13.** Here P = Σ, and one same-sign 2-value coset y is active at η = 0 and at exactly one η*.
- **s = 14**, with τ ≠ 0, or with τ = 0 and G = −1. Here P = Σ and all cosets are single.

Everything else is excluded. **The floor stays L ≥ 14.**

**Dependencies.** Lemma PP and Theorem P12 (v2); fc201185; the consolidated proof 6c5ce361 (Lemmas Φ, O, SV and Theorem M); S0017 (3), (6) and the T-values. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
