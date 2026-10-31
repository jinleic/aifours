# Balanced NL242 (3,144) at L = 10, (10,0) with ΣΣ ≠ 0 — the case of exactly one 8-relation is excluded

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:22:18 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This continues `rank6-144-L10-ten-coset-two-eight-relations-exclusion-v6.md` (a29f04d8). **L = 10 at (3,144) is still NOT excluded.**

## 1. Structure

Write π = {p, p′} with p + p′ = τ = ΣΣ, and r_1 = Σ∖π = Ψ, the unique 8-relation.

**Sign of r_1.** V′ = A_4 − 3A_6 + 9A_8 ≥ 13 forces g(r_1) = +1, and then A_4 − 3A_6 ∈ {6, 14}.

**Pairs.** The other six relations come in pairs (Z, Z Δ r_1) with equal signs. They are indexed by the three nonzero elements of the 2-dimensional quotient R/⟨r_1⟩. Their π-intersections form a linear image of rank 0, 1 or 2. Together with Σwt ≤ 40 and the sign equation, this leaves four configurations:

- **V′ = 23:** X = π ∪ X_0 and Y = π ∪ Y_0 with |X_0 ∩ Y_0| = 2, all four 6-sets of sign −1, and the 2-flats X_0 Δ Y_0 and Ψ∖(X_0 Δ Y_0) of sign +1.
- **(I) V′ = 15:** rank 0, three complementary pairs of 2-flats inside Ψ, all of sign +1.
- **(II) V′ = 15:** rank 1 with S = {p}: X = {p, a, b, c} and Y = {p, a, d, e} with their 6-partners (sign −1), and X+Y = {b, c, d, e} together with {a, f, g, h} (sign +1).
- **(III) V′ = 15:** rank 2: X = {p, a, b, c} and Y = {p′, a, d, e} with s_X = −s_Y, and the 6-sets X+Y and its partner of sign −1.

## 2. Slice tables and contradictions

In each slice write u = g_η(r_1), x = g_η(X) and y = g_η(Y).

**V′ = 23** (Ψ = {A, …, H}, X_0 = {A, B, C, D}, Y_0 = {A, B, E, F}).

1. The coset types p + A + C, p + A + E and p + C + E have the brackets (1 + x)(−3 − 27u + 9y(1 + u)), (1 + y)(−3 − 27u + 9x(1 + u)) and (1 + xy)(−3 − 27u) + 9(1 + u)(x + y).
2. Their pattern rules force λ_X ≡ λ_Y ≡ 0, i.e. x ≡ y ≡ −1.
3. Then p + C + E takes the value −12 when u = 1 and 6 when u = −1. Whether λ_1 vanishes or not, the pattern is (−12, −12, −12) or (6, 6, −12). Both are forbidden.

**(I).**

1. The cosets p + a + b (cross-block or block pairs) force λ_1 ≡ 0 (u ≡ 1), and force (λ_{F_1}, λ_{F_2}) to have rank 2.
2. Then p + p′ + a has bracket 78 − 18(g_1 + g_2 + g_1g_2) = 96 in every slice, i.e. the pattern (±12, ±12, ±12). Forbidden.

**(II).**

1. The coset p′ + b + d has bracket −3(1 + xy) + 9(x + y) − 27(u + xu + yu + xyu). It forbids (u, x, y) ∈ {(1, −1, −1), (−1, 1, 1), (−1, −1, −1)} in any slice, and allows −12 only at (1, 1, 1).
2. The linear image of η ↦ (λ_1, λ_X, λ_Y) must therefore be one of the planes S_1 = {(0,1,0), (0,0,1), (0,1,1)} or S_2 = {(1,1,0), (1,0,1), (0,1,1)}.
3. The coset p′ + a + f gives (0, 0, −12) on S_1 but (6, 6, −12) on S_2, so S_2 is excluded. Hence u ≡ 1.
4. Then p + p′ + f has bracket 78 + 18(x + y) − 18xy = 96 in all three slices. Forbidden.

**(III).** The coset p + p′ + f has bracket −3(1 + xyu) + 81u + 9(x + xu + y + yu + xy).

- Over all (u, x, y), the only allowed values are 6, at (1, −1, −1), and −12, when u = −1 and xy = −1. Zero is never attained.
- The pattern must therefore be (6, 6, 6). That needs x ≡ y ≡ −1, i.e. s_X = s_Y = −1, which contradicts s_X = −s_Y.

The cosets used are all pure, because no 4-relation contains both p and p′ or the indicated mixed triples.

**Conclusion (WRITTEN).** The case (10,0), ΣΣ ≠ 0, n_8 = 1 is excluded.

## 3. Remaining at (3,144), L = 10

- **(10,0) with ΣΣ ≠ 0 and n_8 = 0.** Here V′ = 15, n_6 ≥ 4, and every 4-relation has g = +1 while every 6-relation has g = −1, in the extremal configuration.
- **(8,1).**

The floor stays L ≥ 10.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
