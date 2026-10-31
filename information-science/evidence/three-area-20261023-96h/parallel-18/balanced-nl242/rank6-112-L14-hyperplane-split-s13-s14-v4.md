# Balanced NL242 (3,112) at L = 14 — a hyperplane-split lemma excludes s = 13 and s = 14 with ΣΣ ≠ 0; the e7² configuration remains

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:53:41 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L14-s12-exclusion-v3.md` (3a29e817…d62b). It covers the residue type (polar rank 6, weight 112) at L = 14 only. **L = 14 is still NOT excluded**: one configuration class at s = 14 remains.

## 0. Setting

N_0 ≥ 50 (fc201185). For s ∈ {13, 14}, L = 14 leaves no room for a balanced coset, so P = Σ and dim aff(Σ) = 6 (Theorem M(a)).

- At s = 14, every coset carries one small value.
- At s = 13, one coset y carries two equal-type small values, and its slice-0 sign is the reduced residue of g(y) = ±2.

At slice 0 every point therefore has a sign ±1. For a signed point set Q put N(Q) := #{ξ ∈ F_2^6 : 3 | Σ_{x∈Q} g(x)(−1)^{x·ξ}}, which is given by (3.1).

## 1. Lemma H (hyperplane split)

For ω ≠ 0, put Σ_1 := {x ∈ Σ : x·ω = 1} and Σ_0 := Σ ∖ Σ_1, and let A and B be the signed character sums over Σ_0 and Σ_1. Then

```
N_0 ≤ 32 + ½·#{ξ : 3 | A(ξ) and 3 | B(ξ)} ≤ 32 + ½·min(N(Σ_0), N(Σ_1)).
```

*Proof.* We have Ψ(ξ) = A + B and Ψ(ξ + ω) = A − B. Both are divisible by 3 iff 3 | A and 3 | B. So each pair {ξ, ξ + ω} contributes at most one zero, except the pairs where 3 | A and 3 | B. ∎

**Corollary H1.** At (3,112) with L = 14, every ω ≠ 0 has N(Σ_0) ≥ 36 and N(Σ_1) ≥ 36, and neither side is empty because aff(Σ) = F_2^6. Formula (3.1) gives:

- for |Q| = 1, 2, 3: N = 0, 32, 16;
- for |Q| = 5, with at most one 2-flat inside: N ∈ {20, 8, 32};
- for |Q| = 4: N = 24 if Q is not a flat, N = 48 if Q is a 2-flat with g = +1, and N = 0 if it is a 2-flat with g = −1.

So **no side has size 1, 2, 3 or 5, and a side of size 4 is a positive 2-flat.** A side of size 7 needs X_7 = 1 + 9A_4 − 27A_6 ≤ −44. Seven points carry at most one 6-relation, so this means A_4 ≤ −2: at least 2 negative 2-flats inside.

**W-moments.** Put W(ω) := Σ_{x∈Σ} (−1)^{x·ω} = s − 2|Σ_1(ω)|. Then:

```
Σ_ω W² = 64s,    Σ_ω W⁴ = 64(3s² − 2s + 24 n_4),
```

where n_4 is the number of 2-flats in Σ. The pairing solutions number 3s² − 2s, and each 2-flat gives 24 ordered quadruples. Also |Σ_1(ω)| ≡ τ·ω (mod 2), with τ := ΣΣ.

## 2. Theorem P13: s = 13 is impossible at L = 14

1. By H1, |Σ_1(ω)| ∈ {4, 6, 7, 9} for all ω ≠ 0, so W ∈ {±5, ±1}.
2. Parseval: 169 + 25n_5 + (63 − n_5) = 832, so n_5 = 25.
3. Fourth moment: 13⁴ + 25·625 + 38·1 = 44224 = 64·691. Hence 691 = 3·169 − 26 + 24n_4 = 481 + 24n_4, so n_4 = 210/24, which is not an integer. ✗ ∎

(This includes the case y ∉ aff(Σ∖{y}): that would be a side of size 1.)

## 3. Theorem P14a: s = 14 with τ ≠ 0 is impossible at L = 14

1. By H1, |Σ_1| ∈ {4, 6, 7, 8, 10}, so W ∈ {±6, ±2, 0}, with W = 0 iff τ·ω = 1. For τ ≠ 0, that gives n_0 = 32.
2. Parseval (700 = 36n_6 + 4n_2) then gives n_6 = 18 and n_2 = 13.
3. Fourth moment: 1296·18 + 16·13 = 23536 = 1536n_4 − 2576, so n_4 = 17.
4. Each of the 32 hyperplanes with a 7|7 split has at least 2 negative 2-flats in each side. A 2-flat F lies inside one side of ω iff ω ∈ dir(F)^⊥, and at most 8 of those ω have τ·ω = 1. So 8n_4^− ≥ 32·4, which gives n_4^− ≥ 16 and therefore n_4^+ ≤ 1.
5. Each of the 18 hyperplanes with |W| = 6 has a 4-side that is a positive 2-flat F. ω must then be constant on Σ ∖ F. That set has 10 points, so dim aff(Σ ∖ F) ≥ 4, and at most 3 such ω exist for each F. Hence 18 ≤ 3n_4^+ ≤ 3. ✗ ∎

## 4. What remains at (3,112), L = 14

Only **s = 14 with τ = ΣΣ = 0 and G = −1** remains (v2 §4 excluded G = +1).

Then n_0 = 0, so 36n_6 + 4n_2 = 700 with n_6 + n_2 = 63, which gives n_6 = 14 and n_2 = 49; the fourth moment gives n_4 = 14. Hence the affine evaluation code of Σ has weight enumerator

```
1 + 14z^4 + 49z^6 + 49z^8 + 14z^10 + z^14.
```

**Remark (an h_0-level witness; NOT a function).** Hand-checked identity: take Σ = ((F_2^3 ∖ 0) × 0) ∪ (0 × (F_2^3 ∖ 0)) ⊆ F_2^6, with g = −1 on the first block and +1 on the second.

- τ = 0 and G = −1.
- The relation code is {(T_1, T_2) ∈ H_7 × H_7 : |T_1| + |T_2| even}, which is e7², and all 14 of its 2-flats are positive.
- Ψ(ξ_1, ξ_2) = 8([ξ_2 = 0] − [ξ_1 = 0]), so **N_0 = 50 exactly** and wt(h_0) = 14.
- (★) and S0017 (11) then force u = 4, ν = 0 and α = 14.

Every h_0-level and hyperplane-split test is therefore passed. Excluding this last class needs the η ≠ 0 slices: Lemma SV on the 50 pure cosets, with P_η = Σ in every slice.

**The (3,112) floor stays L ≥ 14.** L = 14 is now reduced to the single class above.

**Dependencies.** v2 (Lemma PP and §4), fc201185, the consolidated proof 6c5ce361 ((3.1) and Theorem M), and ordinary Fourier analysis and code counting. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
