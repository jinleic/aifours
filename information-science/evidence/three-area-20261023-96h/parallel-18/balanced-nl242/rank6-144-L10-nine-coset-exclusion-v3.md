# Balanced NL242 (3,144) at L = 10 — the (9,0) configuration is excluded; (8,1) and (10,0) remain

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:09:47 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This packet extends `rank6-144-L10-slice-pattern-reduction-v2.md` (SHA `f689a454…4d78`). **L = 10 at (3,144) is still NOT excluded.**

## 0. Configuration and tools

**(9,0).** P = Σ consists of 9 cosets. Exactly one coset y carries 2 small values of the same sign, so it is active only in the slice η_y ⊥ (β_1 + β_2). The other 8 cosets are single-valued and always active.

- dim aff(Σ) = 6, so the dependency code R has dimension 2.
- The tools (Lemmas O, Φ, SV, Theorem M, the slice-pattern rule and the census c s = 4 − 1.5G + cĥ_0/2) are as in `rank6-lifted-floors-consolidated-proof-v1.md` (6c5ce361).

**N_0 condition.** (255 − 9A_4 + 27A_6 − 81A_8)/12 ≥ 26 and must be an integer. So V := −A_4 + 3A_6 − 9A_8 ≥ 7 with V ≡ 1 (mod 4).

The dimension-2 code has three codewords, Σwt ≤ 18, and each coordinate lies in 0 or 2 of them. That leaves exactly three relation patterns:

- **(0,3,0)** three 6-relations, all with g = +1 (V = 9, N_0 = 28);
- **(2,0,1)** two disjoint 2-flats c_4 and c_4′ with c_8 = c_4 ∪ c_4′, g(c_8) = −1 and g(c_4) = −g(c_4′) (V = 9);
- **(1,1,1)** relations c_4, c_6 and c_8 = c_4 Δ c_6 with |c_4 ∩ c_6| = 1, and g = (−1, +1, −1) (V = 13, N_0 = 31).

The patterns (3,0,0), (2,1,0) and (1,2,0) give V ≤ 5.

## 1. Exclusions

**(0,3,0).** All 9 coordinates are active, so y lies in exactly two relations. Hence Σ∖{y} carries the single 6-relation c_y, and the y-inactive slices look like (C1).

1. The type-(a) cosets force G6_η = −1 in both y-inactive slices.
2. The type-(c) cosets x + q_1 + q_2 then take the value 12g in both of those slices. Two entries ±12 are forbidden.

**(1,1,1).** Write p_0 for the common point of c_4 and c_6.

- **y = p_0.** Then Σ∖{y} = c_8 is zero-sum. Its triple cosets force G8_η = −1 in both y-inactive slices, hence B8 = 0 and G8_{η_y} = −1, so (G4, G6) ∈ {(1,−1), (−1,1)} at η_y. For the triples T ⊆ c_6∖{y} (a = 0), the η_y value is −(1/4)[−3 − 27G4 − 3G6 + 9G8]g, which equals 9g or −3g. That is not ±6, as the required pattern (±6, ±6, ±6) demands.
- **y ∈ c_4∖{p_0}.** In the y-inactive slices the single relation is c_6, and the (C1)-type argument applies: type (a) forces G6 = −1, and type (c) then gives two entries ±12.
- **y ∈ c_6∖{p_0}.** In the y-inactive slices the single relation is c_4. Cosets x + x′ + w force G4 = −1. Then the pure coset x + p_0 + y, with x ∈ c_4∖{p_0}, has the 5-set representation {x} ∪ (c_6∖{p_0, y}) and the 7-set partner. Its value is −(1/2)(−9 + 27G4)g = 18g, which exceeds 12.

**(2,0,1) with y ∈ c_8** (say y ∈ c_4). In the y-inactive slices the single relation is c_4′.

1. Cosets x + x′ + w (x, x′ ∈ c_4′) force G4′ = −1.
2. The pure coset x + z + y (x ∈ c_4′, z the free point) has the 5-set representation {x, z} ∪ (c_4∖{y}) with a 7-set partner. Its value is −(1/2)(−9 + 27G4′)g = 18g. Too large.

**(2,0,1) with y = z, the free point.** Write c_8 = (a + W) ∪ (b + W′) with W ∩ W′ = 0 and U_4 = W + W′.

The 55 pure cosets split as:

- 24 in aff(c_8): the classes a + U_4 and b + U_4;
- 31 involving y: the classes y + U_4 and y + a + b + U_4.

The y-cosets are active only at η_y, where the values are as follows.

- **y + w + w′:** value −(9/4)(1 + G4)(1 + G4′)g. Excluding −9g forces (G4, G4′)_{η_y} ≠ (1, 1).
- **y + p + p′:** value −(1/4)[−3 + 9G4 + 9G4′ − 27G4G4′]g. This forces (G4, G4′)_{η_y} = (−1, −1), giving the value 12g.
- **Consequence.** All 15 cosets in y + U_4 ∖ {y} have value ≡ 0 in every slice, so they are monochromatic.

Write ε := g(c_4).

1. ĥ_0 vanishes at the 9 cosets y + w + w′. It also vanishes at the 3 cosets "y + pair" whose pair lies in the flat with g = −1. So at least **12 monochromatic cosets have G ∈ {−4, 12}**.
2. The aff(c_8) cosets have the y-inactive values −(1/2)(1 + G4′)(3 − 9G4)g (class a + U_4) and −(1/2)(1 + G4)(3 − 9G4′)g (class b + U_4). Their value at η_y is 0. The pattern rule therefore allows at most one y-inactive slice with G4 = 1, and at most one with G4′ = 1.
3. Write G4_η = ε(−1)^{B4·η} and G4′_η = −ε(−1)^{B4′·η}. With G4 = G4′ = −1 at η_y, the parity constraints force **B4 = 0** (then G4 ≡ −1 and ε = −1) or **B4′ = 0** (then G4′ ≡ −1 and ε = +1). Any other choice puts value +1 into both y-inactive slices.
4. In the first case all 12 cosets of class b + U_4 have value ≡ 0. In the second, all 12 of class a + U_4 do. In either case ĥ_0 = 0 there, so G ∈ {−4, 12}.
5. That makes **24 monochromatic cosets with (G − 3.5)² ≥ 56.25**, so Σ(G − 3.5)² ≥ 1350. But the total is 64N_0 − N_0² = 1008 with N_0 = 28. Contradiction.

**Hence (9,0) is excluded at L = 10.**

## 2. Remaining at (3,144), L = 10 (NOT excluded)

- **(8,1):** 8 single-value Σ-cosets plus one balanced coset p, active in 2 slices.
  - If dim R(Σ) = 1, Σ is of (C1) or (C2) type and p lies in a relation r = T_p ∪ {p}.
  - If dim R(Σ) = 2, then 3A_4 − 9A_6 + 27A_8 ≥ 9.
  - In the C2-type sub-case the slice η_0 where p is inactive forces υ = −6g on all 56 triple cosets, so η_1 and η_2 must give ±6 as well. This was not resolved.
- **(10,0):** all single-value, with no inactive slices. It needs the two-value condition M_γ = A + 24c ε(γ) on all 54 pure cosets. Not resolved.

## Status

**WRITTEN:** the (9,0) exclusion. The (3,144) floor stays L ≥ 10; L = 10 is reduced to (8,1) and (10,0).

The type, the (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
