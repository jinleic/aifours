# Balanced NL242 (3,144) — the slice-value lemma and exclusion of L = 8, so L ≥ 10

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:43:45 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** The residue type (polar rank 6, weight 144), i.e. r = 3 and d = 144. This raises the admitted Gate III floor at this weight from L ≥ 8 to **L ≥ 10**. Weight 128 and the d128/u8 branch are untouched. The (3,144) type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Inputs

Admitted:

- S0017 (3) and (9)–(11); at d = 144 this gives α + 2ν = 50 − L − u/2;
- Gate III: L ≥ 8 at rank 6, which covers L ≤ 7.

Own WRITTEN premises (unreviewed):

- Theorem A: u ≡ 4 (mod 8), so u ≥ 4.
- Lemma B and Corollary C: L is even.
- Lemma O; Theorem M(a): aff(P) = F_2^6.
- The zero counts N_0 and the expansion φ(Σz) = 2^{1−s} Σ_{|T| odd} (−1)^{s−|T|}(−3)^{(|T|−1)/2} z^T, from `rank6-112-erratum-and-L10-exclusion-addendum-v1.md` (SHA `520f1484…41d4`).
- The reduction to (C1)/(C2) in `lifted-outside-coset-second-moment-and-144-L8-reduction-v1.md` (SHA `5c204162…bbb1`).

## 1. Lemma SV (slice values on pure cosets, rank-6 lifted)

Let ā be a coset with no small value, and let η ≠ 0. Then

```
υ_η(ā) = (1/8) Σ_β S(ā,β)(−1)^{β·η} = 3c_ā ε̂_ā(η) ∈ {0, ±6, ±12},
Σ_{η≠0} ε̂_ā(η)² ≤ 16.
```

Here T = −4 + 24ε_ā on the 4 points of the coset. A ±1 function on F_2^2 has ε̂ ∈ {0, ±2, ±4} and Σ_η ε̂² = 16.

On the other side, by (3) with q = 0 off U:

```
υ_η(ā) = Walsh(u_η)(ā) = −64 Σ_{|T| odd, ΣT = ā} b_{|T|} g_η(T),
```

with b_k = 2^{1−s}(−1)^{s−k}(−3)^{(k−1)/2}. Here g_η(x) := g(x)(−1)^{β_x·η} for a Σ-coset x carrying exactly one small value at position β_x.

## 2. Theorem S (L = 8 is impossible at (3,144))

*Proof.* The second-moment paper shows that only two configurations remain at L = 8. In both, Σ = P consists of 8 cosets, each carrying exactly one small value, so s = 8 and the coefficients are b_3 = 3/128, b_5 = −9/128, b_7 = 27/128.

**(C2): Σ zero-sum, G = +1.**

1. Every pure coset is the sum of exactly one triple T and its complementary 5-set.
2. g_η(T^c) = G_η g_η(T), where G_η := Π g_η = G(−1)^{B·η} and B := Σ_x β_x ∈ F_2^2.
3. Hence υ_η(ā) = −(1/2)(3 − 9G_η) g_η(T), which equals 3g_η(T) if G_η = 1 and −6g_η(T) if G_η = −1.
4. By Lemma SV the value ±3 is impossible, so G_η = −1, i.e. B·η = 1, for all three η ≠ 0.
5. But then B·(η_1 + η_2) = 0. Contradiction.

**(C1): the only relation is a zero-sum 6-subset Σ_6 = Σ ∖ {q_1, q_2}, with g(Σ_6) = −1.** Put G6_η := Π_{Σ_6} g_η.

- **Type (a)** pure cosets x + y + q_i (x, y ∈ Σ_6) are pure, since otherwise there would be a 4-relation. Their only other representative is (Σ_6 ∖ {x,y}) ∪ {q_i}. So υ_η = −(1/2)(3 − 9·G6_η) g_η(T). Lemma SV then forces **G6_η = −1 for every η ≠ 0**.
- **Type (c)** pure cosets x + q_1 + q_2 (x ∈ Σ_6) have the 7-set partner (Σ_6 ∖ {x}) ∪ {q_1, q_2}. So υ_η = −(1/2)(3 + 27·G6_η) g_η(T) = 12g_η(T), which gives |ε̂_ā(η)| = 4 for **all three** η ≠ 0. Then Σ_{η≠0} ε̂² = 48 > 16. Contradiction.

So both configurations are impossible. ∎

**Corollary.** At (3,144), every balanced peak-28 target has **L ≥ 10**, with L even. This raises the admitted Gate III floor of 8 at this single weight. It depends on own unreviewed Theorems A, M and O, Lemma B and the reduction packet; adoption requires reviewing the whole chain.

## 3. Rank-6 lifted floors after this packet (own WRITTEN)

| Type | Floor |
|---|---|
| (3,112) | L ≥ 12 (Theorem R′). At L = 12, \|Σ\| ∈ {10, 11, 12}. |
| (3,144) | L ≥ 10 (Theorem S). |
| (3,128) | NOT treated (avoided branch). Its admitted floor stays L ≥ 8. |

The (24,24,2) gap and the original problem remain OPEN. Novelty and priority are UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR, the cadence MAJORs, the checkpoint-054 attribution MINOR and the s = 6 erratum MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT; no early park.
