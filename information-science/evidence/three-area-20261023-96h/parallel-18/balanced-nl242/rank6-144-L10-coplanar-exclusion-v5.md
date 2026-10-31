# Balanced NL242 (3,144) at L = 10, (10,0) with ΣΣ = 0 — the co-planar shape is excluded

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:15:00 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal or novelty claim. No program was run; all arithmetic was done by hand.

This addendum to `rank6-144-L10-ten-coset-partial-v4.md` (SHA `fb69ebd9…be03`) closes the co-planar shape listed there as open. **L = 10 at (3,144) is still NOT excluded.**

## Setting (from v4)

- Σ = {a, b, c, d, e, f} ∪ Γ with Γ = {g, h, i, j}. The 2-flats are F_1 = {a, b, c, d}, F_2 = {a, b, e, f} and F_3 = F_1 Δ F_2 = {c, d, e, f}.
- ΣΣ = 0 and G = g(Σ) = −1.
- v4 already showed: G_η ≡ −1 (B = 0); f_i := g(F_i) constant in η (B_i = 0); f_3 = f_1 f_2; and (f_1, f_2) ∈ {(1, −1), (−1, 1), (−1, −1)}.
- Then V′ = 27 + 4(f_1 + f_2 + f_3) = 23, so N_0 = (513 + 207)/24 = 30.

## Proof of exclusion

**1. The bracket does not depend on η.** Every relation r has g_η(r) = g(r) in every slice, because B_r = 0 on the whole span of Σ, F_1 and F_2. So for every pure coset ā = ΣT_0,

```
υ_η(ā) = (1/8) g_η(T_0) · Br(ā),     with Br(ā) := Σ_{r∈R} w(|T_0 Δ r|) g(r) independent of η.
```

Hence |υ_η| is the same in all three slices, and the pattern rule forces Br ∈ {0, ±48}. If Br = 0, the coset is **monochromatic**. Since ĥ_0 is proportional to Br as well, ĥ_0(ā) = 0 at that coset, and therefore G(ā) ∈ {−4, 12}.

**2. The brackets of the coset types** (hand-computed from the eight representation sizes; G = −1):

| Coset type | Br |
|---|---|
| x + y + z, one point from each line {a,b}, {c,d}, {e,f} (2 cosets) | 24(1 + f_1)(1 + f_2) |
| x + y + γ, with γ ∈ Γ and {x, y} lying in exactly one flat F_i (8 cosets per i) | 24(1 + f_i) |
| x + γ + γ′, with x in the F-part and γ, γ′ ∈ Γ (18 cosets) | 24(1 − f_3) |
| a + b + γ and analogues | 24(1 + f_1 + f_2 − f_1 f_2) = ±48 |
| γ + γ′ + γ″ | 48 |

**3. Count of monochromatic cosets.**

- (f_1, f_2) = (1, −1): 2 + 8 (pairs in F_2 only) + 8 (pairs in F_3 only) = **18**.
- (−1, 1): **18**, by symmetry.
- (−1, −1): 2 + 8 (pairs in F_1 only) + 8 (pairs in F_2 only) + 18 (cosets x + γ + γ′, since f_3 = +1) = **36**.

**4. Second-moment contradiction.** With N_0 = 30:

```
Σ_ā (G − 3.75)² = 64·30 − 30² = 1020,
```

while each monochromatic coset contributes at least (7.75)² = 60.06. Since 18 × 60.06 = 1081 > 1020, this is a contradiction in every case.

**All monochromatic cosets above are pure.** For instance, x + y + γ ∈ Σ would require a 4-relation containing a point of Γ, and none exists.

**Conclusion (WRITTEN).** The configuration (10,0) with ΣΣ = 0 is fully excluded, both the windmill and the co-planar shape.

## Remaining at (3,144), L = 10

- **(10,0) with ΣΣ ≠ 0 and n_8 ≤ 2.** The three-8-relation case is excluded in v4.
- **(8,1).**

Neither has been resolved. The floor stays L ≥ 10.

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
