# Balanced NL242 (3,112) at L = 16 — s = 8 and s = 10 are excluded; s = 12 is reduced; with an addendum to v6 §2 item 4

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 09:19:05 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This file is the successor to `rank6-112-L16-reduction-v6.md` (450cd2ac…283d), which stays unchanged. It covers (3,112) at L = 16 only, where N_0 ≥ 52. **L = 16 is NOT excluded.**

## 0. Addendum to v6 §2 item 4 (omission; errata-not-edits)

The |P∖Σ| = 3 list in v6 omitted the balanced types (3,0) and (0,3). Such a coset carries three small values, and is active in **all three** slices η ≠ 0, because g_η = c(χ_1 + χ_2 + χ_3) = −cχ_4 ≠ 0. The (2,2) type is active in exactly one slice.

So the complete s = 8 menu (cost 8 on P∖Σ) is:

- **(A)** four (1,1);
- **(B)** (3,0), (3,0), (1,1);
- **(C)** (3,0), (1,1), (1,1), plus one 2-valued F-coset;
- **(D)** (2,2), (1,1), (1,1);
- **(E)** three (1,1), plus two extra values on F.

Extra values on F can only make some F-cosets inactive in some slices, which only removes representations.

## 1. Theorem P8-16: s = 8 is impossible at L = 16

As in v6 §2, at least 3 pure W_3-classes must have odd k. They then have G′ = 0, i.e. k = 3, so they are nonzero in **all** three slices. Each such class offset must therefore be reachable in every slice: it must lie in span{c_j : j ∈ J_η} for all η.

- **(C), (D), (E).** The common reachable set has at most 1 nonzero offset (E: 0; C: ⟨c_1⟩; D: at most ⟨c_1⟩). ✗

**Single-carrier lemma (general slice signs).** Let ā lie in a class reachable in slice η (11 active points) only as T = {p} ∪ E, with E ⊆ F even and ΣE = v ∈ W_3. Then by Lemma Φ (s = 11):

```
υ_η(ā) = −(g_η(p)/16)·Λ′(v),   Λ′(v) := Σ_{E⊆F even, ΣE=v} (−3)^{|E|/2} g_η(E).
```

Here g_η = g·(−1)^{β_x·η} is an **arbitrary** sign function on F; it need not be a character. Expand Π_{x∈F}(1 + i√3·g_η(x)(−1)^{ζ·x}), whose even part is 2^8 cos(πΨ′(ζ)/3) with Ψ′ the 8-term sum. Then for v ≠ 0, Λ′(v) = 48·Z′(v), where Z′(v) := Σ_{ζ∈N′} (−1)^{ζ·v} and N′ := {ζ ∈ F_2^3 : 3 | Ψ′(ζ)}. Hence υ_η(ā) = −3g_η(p)Z′(v).

If the class has k = 3, all 7 pure cosets (v ≠ 0) need |υ| = 6, i.e. |Z′(v)| = 2. Parseval then gives |N′|² + 7·4 = 8|N′|, which has no real solution (discriminant 64 − 112 < 0). **So a k = 3 class cannot have a single carrier in an 11-point slice.**

(Check: if g_η is an affine character, N′ has 7 elements, Λ′(v) = ∓48 for v ≠ 0, and Λ′(0) = 208.)

- **(B).** Here p_3 is inactive only at η_3^*, and the common set is ⟨c_1, c_2⟩ ∖ 0. In a slice where p_3 is active (11 points), the class c_1 has the single carrier p_1, since the offsets are independent. By the lemma this is impossible. ✗
- **(A).** Only the inactivity partition (2,1,1) survives (v6). Let I_{η_1} = {1,2}, I_{η_2} = {3} and I_{η_0} = {4}, so S = ⟨c_3, c_4⟩. In η_0 (J = {1,2,3}, 11 points), c_1, c_2, c_3 are independent: their span contains S and the whole configuration spans F_2^3. So the k = 3 class c_3 has the single carrier p_3. The other p_j have offsets ≠ c_3, so its 7 cosets with v ≠ 0 are pure. By the lemma this is impossible. ✗

(A pre-pin draft of this section assumed that g_η on F is an affine character. That assumption is not available in slices η ≠ 0. The corrected argument above uses arbitrary g_η, and the conclusion is unchanged.)

**So s = 8 is impossible at L = 16.** ∎

## 2. Theorem P10-16: s = 10 is impossible at L = 16

From v6 we have d = 4, dim R = 5 and n_4 = 15. N_0 ≥ 52 is equivalent to X := Σ_{r∈R} (−3)^{|r|/2} g(r) ≥ 736.

- **ΣΣ ≠ 0.** There is no 10-relation. The code-weight identity gives 60 + 6n_6 + 8n_8 ≤ 160 with n_6 + n_8 = 16, so n_8 ≤ 2. Then X ≤ 1 + 135 + 27(16 − n_8) + 81n_8 ≤ 676. ✗
- **ΣΣ = 0.** The relations form 15 pairs (plane, complementary 6-set), so X = 1 + 9A_4 − 27G·A_4 − 243G.
  - G = +1 gives X ≤ 28. ✗
  - G = −1 gives X = 244 + 36A_4 ≥ 736, so A_4 = 15: all planes are positive. The kernel K of g|_R then has dimension 4 and consists of 0 and the 15 planes. Its weight sum is 60, which is not ≡ 0 (mod 8) as a dimension-4 linear code requires. ✗

**So s = 10 is impossible at L = 16.** ∎

## 3. s = 12 at L = 16: reduction

- **Lemma PP** (≤ 12 nonzero values):
  - τ = 0 and G = −1 gives ≥ 52·36 > 768. ✗
  - τ ≠ 0 forces Ψ ≡ 0 on the even class, so Σ is a union of 6 τ-pairs and τ = 0. ✗
  - Hence **τ = 0 and G = +1**.
- **d = 6** (n_4 = 3, dim R = 5): the pairs are 3 (4,8) and 12 (6,6). Then X ≤ 1 + 729 + 90·3 + 27·24 = 1648 < 2944, the requirement for N_0 ≥ 52. ✗
- **d = 5** (n_4 = 15, dim R = 6): the pairs are 15 (4,8) and 16 (6,6). The maximum X is 1 + 729 + 1350 + 864 = 2944, and N_0 ≥ 52 forces **equality**. So every plane and every 8-relation is positive, every 6-relation is negative, and N_0 = 52. **OPEN.** This is the analogue of the v3 configuration and needs a p-half slice analysis with the L = 16 budget.
- **d = 4** (n_4 = 39: Σ = AG(4,2) minus a 2-flat). **OPEN.**

## 4. Status at (3,112), L = 16

Excluded: s ∈ {0, …, 11, 13}, together with s = 12 for d = 6, τ ≠ 0, or (τ = 0, G = −1).

Open:

- s = 12 with d ∈ {4, 5}, τ = 0 and G = +1;
- s = 14, 15, 16.

**The floor stays L ≥ 16** (T112, v5).

**Dependencies.** v5, v6, Lemma PP (v2), Lemma H (v4), the consolidated proof 6c5ce361 (Lemmas Φ, O, SV and the census), and S0017. Nothing from the NONINPUT set is used.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
