# Balanced NL242 (3,112) — the last L = 14 class (s = 14, ΣΣ = 0, G = −1) is rigid and is excluded by slices; hence L ≥ 16

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:03:08 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L14-hyperplane-split-s13-s14-v4.md` (dde04191…2985). It covers the residue type (polar rank 6, weight 112) only. The type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Setting

The class is s = 14, P = Σ, τ = 0, G = −1. From v4 §4, the hyperplane profile is (n_6, n_2, n_0) = (14, 49, 0) and Σ contains n_4 = 14 two-flats. C denotes the affine evaluation code of Σ and R = C^⊥ the relation code; both are [14, 7] codes containing 1^14.

## 1. Rigidity theorem

**Statement.** Up to the choice of origin o ∉ Σ:

- Σ = o + ((V_1 ∖ 0) ∪ (V_2 ∖ 0)), with V_1 ⊕ V_2 = F_2^6 and dim V_i = 3;
- g(o + u) = ε_i(−1)^{n·u} for u ∈ V_i ∖ 0, with ε_1ε_2 = −1;
- N_0 = 50, and ĥ_0 vanishes at every pure coset.

*Proof.*

1. **All 2-flats are positive C-words.** The 14 hyperplanes with |W| = 6 give 14 distinct weight-4 words of C. By Corollary H1 each is a 2-flat with g = +1, hence also a word of R. Since n_4 = 14, these are all the 2-flats of Σ, and all are positive.
2. **Even meetings.** C ⊥ R, so two 2-flats meet in 0 or 2 points.
3. **Clusters.** If F and F′ meet in 2 points, then F + F′ is a third 2-flat, and all three lie in the 3-flat Φ = aff(F ∪ F′) with |Φ ∩ Σ| ≥ 6.
   - Φ ⊆ Σ is impossible. Φ would hold all 14 two-flats, and for the 7 nonzero ω ∈ dir(Φ)^⊥ the opposite side would be all of Q_6 := Σ ∖ Φ, because a 4-side must be a 2-flat. So Q_6 would lie in a parallel 3-flat and contain 3 more 2-flats. ✗
   - Hence |Φ ∩ Σ| ∈ {6, 7}, carrying 3 or 7 two-flats.
   - Two flats from different clusters are disjoint by item 2. Every point of a cluster lies on one of its flats, so clusters are pairwise disjoint.
   - Counting flats and points: with a clusters of 7 points, b clusters of 6 points and c isolated flats, 14 = 7a + 3b + c and 7a + 6b + 4c ≤ 14. The only solution is a = 2, b = c = 0.
   - So Σ = (Φ_1 ∖ {o_1}) ∪ (Φ_2 ∖ {o_2}). Then τ = o_1 + o_2 = 0, so o_1 = o_2 = o, Φ_1 ∩ Φ_2 = {o}, and aff(Σ) = F_2^6 gives V_1 ⊕ V_2 = F_2^6.
4. **Signs.** g(F) = +1 on the 7 planes of each block forces g|_{block i} = ε_i·χ_{n_i}, since the solutions form the Hamming code H_7 = e7^⊥. Then G = −1 gives ε_1ε_2 = −1.
5. **h_0.** Centred at o, Ψ = 8ε_1([ξ_1 = n_1] − [ξ_2 = n_2]). So N_0 = 1 + 49 = 50, and ĥ_0(o + a) = −8ε_1((−1)^{a_1·n_1}[a_2 = 0] − (−1)^{a_2·n_2}[a_1 = 0]). This is supported on Σ. ∎

## 2. Slice lemma

In slice η ≠ 0, g_η = g·(−1)^{β_x·η}. On each block, g_η is a sign function on V_i ∖ 0. Since H_7 is perfect, it is one of two types:

- **H7-type**: ±χ_n;
- **B-type**: ε·χ_n with one flipped point u_0. Flipping always gives κ = −ε (the other sign would need g(u_0) = 3ε).

Centred at o, υ_η(o + a) = −(2/√3)·Im(P_1(a_1)P_2(a_2)), where P_i(a) := Σ_ξ ω^{B_i(ξ) mod 3}(−1)^{a·ξ} and ω = e^{2πi/3}. Put z_e := ω^e − 1. Up to real signs, for a ≠ 0:

| Type | Generic a | Special a = u_0 | a = 0 |
|---|---|---|---|
| H7(ε) | iε√3 | — | −4 − 3iε√3 |
| B(ε) | z_{−ε} | ω^{−ε} + 3 − 4ω^ε | ω^{−ε} + 3 + 4ω^ε |

Hand products at the pure cosets (a_1 ≠ 0 ≠ a_2, and a = 0):

- **H7 × B.** Generic times generic gives υ = ±3, and generic times special gives ±9. **Forbidden.**
- **H7 × H7.** Mixed cosets give 0. At a = 0, υ = −24(ε_1 + ε_2), so ε_1 = −ε_2 is needed. Then **every pure value is 0.**
- **B × B.** Generic times generic gives ±3 unless ε_1 = −ε_2, in which case it gives 0. With ε_1 = −ε_2:
  - special times special = 39, so υ = 0;
  - at a = 0 the product is 7, so υ = 0;
  - generic times special = −2 + 7ω^{ε_1} − 5ω^{−ε_1}, with imaginary part 6ε_1√3, so **υ = ±12**.

  So a B×B slice has exactly 12 nonzero pure cosets, S_η = {(a_1, u^{(2)}_η) : a_1 ∉ {0, u^{(1)}_η}} ∪ {(u^{(1)}_η, a_2) : a_2 ∉ {0, u^{(2)}_η}}.

**At most one slice is B×B.** For two B×B slices η ≠ η′:

- if u^{(1)}_η ≠ u^{(1)}_{η′} and u^{(2)}_η ≠ u^{(2)}_{η′}, then (u^{(1)}_{η′}, u^{(2)}_η) ∈ S_η ∩ S_{η′};
- if they agree on one block, S_η ∩ S_{η′} contains at least 5 cosets.

Either way some pure coset has ±12 in two slices, which Lemma SV forbids.

## 3. Second-moment contradiction

Every slice is H7×H7 or B×B, and at most one is B×B. So at least 50 − 12 = 38 pure cosets have υ_η = 0 for all η ≠ 0. By Lemma SV they have k ∈ {0, 4}. Also ĥ_0 = 0 there (§1), so G = 4k − 4 ∈ {−4, 12}.

With N_0 = 50: Σ_ā (G − 50/8)² = 64·50 − 50² = 700. But these 38 cosets alone contribute at least 38·(12 − 6.25)² = 38·33.0625 = 1256.375 > 700. ✗

## 4. Theorem T112: (3,112) has L ≥ 16

Every case at L = 14 is now excluded:

| Case | Excluded by |
|---|---|
| s = 0; s ≤ 9; s = 11; the 3-flat | fc201185 |
| s = 10 | v2 P10 |
| s = 12 | v2 P12 and v3 P12′ |
| s = 13 | v4 P13 |
| s = 14 with τ = 0, G = +1 | v2 §4 |
| s = 14 with τ ≠ 0 | v4 P14a |
| s = 14 with τ = 0, G = −1 | this file |

s ≤ L = 14 always. L is even (Corollary C), so **(3,112): L ≥ 16** (WRITTEN, own, unreviewed). The admitted window then gives 16 ≤ L ≤ 28.

**Assurance caveat.** This is a long chain of hand computations: v2–v5, the complex products in §2, and the cluster counting. An independent entire review is REQUIRED before any adoption.

**Dependencies.** S0017 (3), (6), (9)–(11); the consolidated proof 6c5ce361 (Lemmas Φ, O, SV, Theorem M, the second-moment identity and the census); fc201185; v2–v4. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
